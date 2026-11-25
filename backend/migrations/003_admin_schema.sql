-- ====================================================================
-- SCALE TEST SERIES - PHASE 13 ADMIN DASHBOARD SCHEMA MIGRATION
-- Target: Supabase PostgreSQL (xkemqdthtkkfxaltigii)
-- ====================================================================

-- 1. Extend Scale Users with RBAC and Suspension Columns
ALTER TABLE public.scale_users 
ADD COLUMN IF NOT EXISTS role VARCHAR(30) NOT NULL DEFAULT 'STUDENT',
ADD COLUMN IF NOT EXISTS is_suspended BOOLEAN NOT NULL DEFAULT false,
ADD COLUMN IF NOT EXISTS suspension_reason TEXT,
ADD COLUMN IF NOT EXISTS suspended_at TIMESTAMPTZ,
ADD COLUMN IF NOT EXISTS suspended_by UUID;

CREATE INDEX IF NOT EXISTS idx_scale_users_role ON public.scale_users(role);
CREATE INDEX IF NOT EXISTS idx_scale_users_suspended ON public.scale_users(is_suspended);

-- 2. Extend Scale User Entitlements with Source Tracking (Complimentary vs Purchased)
ALTER TABLE public.scale_user_entitlements
ADD COLUMN IF NOT EXISTS source_type VARCHAR(50) NOT NULL DEFAULT 'PURCHASE',
ADD COLUMN IF NOT EXISTS admin_notes TEXT,
ADD COLUMN IF NOT EXISTS revoked_at TIMESTAMPTZ,
ADD COLUMN IF NOT EXISTS revoked_by UUID;

CREATE INDEX IF NOT EXISTS idx_scale_entitlements_source ON public.scale_user_entitlements(source_type);

-- 3. Account Suspensions History Table (Immutable Audit Trail)
CREATE TABLE IF NOT EXISTS public.scale_account_suspensions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.scale_users(id) ON DELETE CASCADE,
  suspension_type VARCHAR(50) NOT NULL DEFAULT 'TEMPORARY_SUSPENSION', -- 'TEMPORARY_SUSPENSION', 'PERMANENT_ACCESS_BLOCK'
  reason TEXT NOT NULL,
  admin_notes TEXT,
  suspended_by UUID NOT NULL REFERENCES public.scale_users(id),
  started_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  expires_at TIMESTAMPTZ,
  reactivated_at TIMESTAMPTZ,
  reactivated_by UUID REFERENCES public.scale_users(id),
  status VARCHAR(30) NOT NULL DEFAULT 'ACTIVE' -- 'ACTIVE', 'REACTIVATED', 'EXPIRED'
);

CREATE INDEX IF NOT EXISTS idx_scale_suspensions_user ON public.scale_account_suspensions(user_id);
CREATE INDEX IF NOT EXISTS idx_scale_suspensions_status ON public.scale_account_suspensions(status);

-- 4. Admin Audit Logs (Append-Only Sensitive Operation Records)
CREATE TABLE IF NOT EXISTS public.scale_admin_audit_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  admin_id UUID NOT NULL REFERENCES public.scale_users(id),
  admin_email TEXT NOT NULL,
  admin_role VARCHAR(30) NOT NULL,
  action VARCHAR(100) NOT NULL,
  target_user_id UUID,
  target_record_id VARCHAR(100),
  reason TEXT,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  ip_address TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_scale_audit_logs_action ON public.scale_admin_audit_logs(action);
CREATE INDEX IF NOT EXISTS idx_scale_audit_logs_admin ON public.scale_admin_audit_logs(admin_id);
CREATE INDEX IF NOT EXISTS idx_scale_audit_logs_target ON public.scale_admin_audit_logs(target_user_id);
CREATE INDEX IF NOT EXISTS idx_scale_audit_logs_created ON public.scale_admin_audit_logs(created_at DESC);

-- 5. Admin Notes on Students (Internal Collaboration)
CREATE TABLE IF NOT EXISTS public.scale_admin_notes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id UUID NOT NULL REFERENCES public.scale_users(id) ON DELETE CASCADE,
  admin_id UUID NOT NULL REFERENCES public.scale_users(id),
  admin_email TEXT NOT NULL,
  note TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_scale_admin_notes_student ON public.scale_admin_notes(student_id);

-- 6. Admin Notifications (Real-time Platform Alert Feed)
CREATE TABLE IF NOT EXISTS public.scale_admin_notifications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  notification_type VARCHAR(50) NOT NULL, -- 'NEW_REGISTRATION', 'PAYMENT_SUCCESS', 'PAYMENT_FAILED', 'SUSPENSION', 'RECONCILIATION_NEEDED'
  title TEXT NOT NULL,
  message TEXT NOT NULL,
  related_user_id UUID,
  related_record_id VARCHAR(100),
  is_read BOOLEAN NOT NULL DEFAULT false,
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_scale_admin_notifs_read ON public.scale_admin_notifications(is_read);
CREATE INDEX IF NOT EXISTS idx_scale_admin_notifs_created ON public.scale_admin_notifications(created_at DESC);

-- ====================================================================
-- ATOMIC ADMIN STORED FUNCTIONS
-- ====================================================================

-- Function: Suspend Student Account and Revoke All Active Sessions Atomically
CREATE OR REPLACE FUNCTION public.scale_suspend_student(
  p_student_id UUID,
  p_admin_id UUID,
  p_admin_email TEXT,
  p_admin_role TEXT,
  p_suspension_type TEXT,
  p_reason TEXT,
  p_admin_notes TEXT,
  p_expires_at TIMESTAMPTZ
)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
BEGIN
  -- 1. Mark user as suspended
  UPDATE public.scale_users
  SET is_suspended = true,
      suspension_reason = p_reason,
      suspended_at = timezone('utc'::text, now()),
      suspended_by = p_admin_id,
      updated_at = timezone('utc'::text, now())
  WHERE id = p_student_id;

  -- 2. Revoke all active sessions immediately
  UPDATE public.scale_user_sessions
  SET is_active = false,
      revoked_at = timezone('utc'::text, now()),
      revocation_reason = 'ACCOUNT_SUSPENDED'
  WHERE user_id = p_student_id AND is_active = true;

  -- 3. Record in suspensions history
  INSERT INTO public.scale_account_suspensions (
    user_id,
    suspension_type,
    reason,
    admin_notes,
    suspended_by,
    started_at,
    expires_at,
    status
  )
  VALUES (
    p_student_id,
    p_suspension_type,
    p_reason,
    p_admin_notes,
    p_admin_id,
    timezone('utc'::text, now()),
    p_expires_at,
    'ACTIVE'
  );

  -- 4. Record in audit logs
  INSERT INTO public.scale_admin_audit_logs (
    admin_id,
    admin_email,
    admin_role,
    action,
    target_user_id,
    reason,
    metadata
  )
  VALUES (
    p_admin_id,
    p_admin_email,
    p_admin_role,
    'STUDENT_SUSPENDED',
    p_student_id,
    p_reason,
    jsonb_build_object(
      'suspension_type', p_suspension_type,
      'admin_notes', p_admin_notes,
      'expires_at', p_expires_at
    )
  );

  -- 5. Create notification
  INSERT INTO public.scale_admin_notifications (
    notification_type,
    title,
    message,
    related_user_id
  )
  VALUES (
    'SUSPENSION',
    'Student Account Suspended',
    'Account suspended by ' || p_admin_email || '. Reason: ' || p_reason,
    p_student_id
  );

  RETURN TRUE;
END;
$$;

-- Function: Reactivate Suspended Account Atomically
CREATE OR REPLACE FUNCTION public.scale_reactivate_student(
  p_student_id UUID,
  p_admin_id UUID,
  p_admin_email TEXT,
  p_admin_role TEXT,
  p_reason TEXT
)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
BEGIN
  -- 1. Restore account eligibility
  UPDATE public.scale_users
  SET is_suspended = false,
      suspension_reason = NULL,
      suspended_at = NULL,
      suspended_by = NULL,
      updated_at = timezone('utc'::text, now())
  WHERE id = p_student_id;

  -- 2. Mark suspension history as REACTIVATED
  UPDATE public.scale_account_suspensions
  SET status = 'REACTIVATED',
      reactivated_at = timezone('utc'::text, now()),
      reactivated_by = p_admin_id
  WHERE user_id = p_student_id AND status = 'ACTIVE';

  -- 3. Record in audit log
  INSERT INTO public.scale_admin_audit_logs (
    admin_id,
    admin_email,
    admin_role,
    action,
    target_user_id,
    reason
  )
  VALUES (
    p_admin_id,
    p_admin_email,
    p_admin_role,
    'STUDENT_REACTIVATED',
    p_student_id,
    p_reason
  );

  RETURN TRUE;
END;
$$;

-- Function: Grant Complimentary Access
CREATE OR REPLACE FUNCTION public.scale_grant_complimentary_access(
  p_student_id UUID,
  p_admin_id UUID,
  p_admin_email TEXT,
  p_admin_role TEXT,
  p_product_code TEXT,
  p_reason TEXT,
  p_expires_at TIMESTAMPTZ
)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
BEGIN
  INSERT INTO public.scale_user_entitlements (
    user_id,
    product_code,
    status,
    source_type,
    admin_notes,
    granted_at,
    expires_at
  )
  VALUES (
    p_student_id,
    p_product_code,
    'active',
    'COMPLIMENTARY',
    p_reason,
    timezone('utc'::text, now()),
    p_expires_at
  )
  ON CONFLICT (user_id, product_code) DO UPDATE
  SET status = 'active',
      source_type = 'COMPLIMENTARY',
      admin_notes = p_reason,
      granted_at = timezone('utc'::text, now()),
      expires_at = p_expires_at;

  INSERT INTO public.scale_admin_audit_logs (
    admin_id,
    admin_email,
    admin_role,
    action,
    target_user_id,
    reason,
    metadata
  )
  VALUES (
    p_admin_id,
    p_admin_email,
    p_admin_role,
    'COMPLIMENTARY_ACCESS_GRANTED',
    p_student_id,
    p_reason,
    jsonb_build_object('product_code', p_product_code, 'expires_at', p_expires_at)
  );

  RETURN TRUE;
END;
$$;

-- Function: Revoke Examination Access
CREATE OR REPLACE FUNCTION public.scale_revoke_access(
  p_student_id UUID,
  p_admin_id UUID,
  p_admin_email TEXT,
  p_admin_role TEXT,
  p_product_code TEXT,
  p_reason TEXT
)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE public.scale_user_entitlements
  SET status = 'revoked',
      revoked_at = timezone('utc'::text, now()),
      revoked_by = p_admin_id,
      admin_notes = coalesce(admin_notes || ' | Revoked: ', 'Revoked: ') || p_reason
  WHERE user_id = p_student_id AND product_code = p_product_code;

  INSERT INTO public.scale_admin_audit_logs (
    admin_id,
    admin_email,
    admin_role,
    action,
    target_user_id,
    reason,
    metadata
  )
  VALUES (
    p_admin_id,
    p_admin_email,
    p_admin_role,
    'ACCESS_REVOKED',
    p_student_id,
    p_reason,
    jsonb_build_object('product_code', p_product_code)
  );

  RETURN TRUE;
END;
$$;

