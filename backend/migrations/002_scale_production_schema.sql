-- ====================================================================
-- SCALE TEST SERIES - PRODUCTION DATABASE MIGRATION
-- Target: Supabase PostgreSQL (xkemqdthtkkfxaltigii)
-- Isolated with scale_ prefix to coexist with OMR tables
-- ====================================================================

-- 1. Scale Users
CREATE TABLE IF NOT EXISTS public.scale_users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  full_name TEXT,
  phone TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  deleted_at TIMESTAMPTZ
);

CREATE INDEX IF NOT EXISTS idx_scale_users_email ON public.scale_users(email);

-- 2. Scale Single-Device Application Sessions
CREATE TABLE IF NOT EXISTS public.scale_user_sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.scale_users(id) ON DELETE CASCADE,
  token_hash VARCHAR(64) NOT NULL UNIQUE,
  device_info TEXT,
  ip_address TEXT,
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  last_seen_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  revoked_at TIMESTAMPTZ,
  revocation_reason TEXT
);

-- Phase 19: Critical partial unique index enforcing exactly 1 active session per user!
CREATE UNIQUE INDEX IF NOT EXISTS idx_scale_active_user_session 
ON public.scale_user_sessions (user_id) 
WHERE (is_active = true);

CREATE INDEX IF NOT EXISTS idx_scale_user_sessions_lookup 
ON public.scale_user_sessions (token_hash, is_active);

-- 3. Scale Orders (Financial Audit Trail)
CREATE TABLE IF NOT EXISTS public.scale_orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.scale_users(id) ON DELETE RESTRICT,
  order_id VARCHAR(100) NOT NULL UNIQUE,
  amount_paise INTEGER NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'INR',
  status VARCHAR(50) NOT NULL DEFAULT 'created',
  product_code VARCHAR(50) NOT NULL DEFAULT 'SCALE_NEET_60_MOCKS',
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_scale_orders_user_id ON public.scale_orders(user_id);
CREATE INDEX IF NOT EXISTS idx_scale_orders_order_id ON public.scale_orders(order_id);

-- 4. Scale Payments (Idempotent Transactions)
CREATE TABLE IF NOT EXISTS public.scale_payments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id VARCHAR(100) NOT NULL REFERENCES public.scale_orders(order_id) ON DELETE RESTRICT,
  payment_id VARCHAR(100) NOT NULL UNIQUE,
  amount_paise INTEGER NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'INR',
  status VARCHAR(50) NOT NULL,
  method VARCHAR(50),
  signature VARCHAR(255),
  verified_at TIMESTAMPTZ,
  raw_payload JSONB,
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_scale_payments_payment_id ON public.scale_payments(payment_id);
CREATE INDEX IF NOT EXISTS idx_scale_payments_order_id ON public.scale_payments(order_id);

-- 5. Scale Entitlements (Paid Access Control)
CREATE TABLE IF NOT EXISTS public.scale_user_entitlements (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.scale_users(id) ON DELETE CASCADE,
  product_code VARCHAR(50) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'active',
  granted_via_order_id VARCHAR(100) REFERENCES public.scale_orders(order_id) ON DELETE RESTRICT,
  granted_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  expires_at TIMESTAMPTZ,
  CONSTRAINT uq_scale_user_product_entitlement UNIQUE (user_id, product_code)
);

CREATE INDEX IF NOT EXISTS idx_scale_entitlements_lookup ON public.scale_user_entitlements(user_id, product_code, status);

-- 6. Scale Exam Progress
CREATE TABLE IF NOT EXISTS public.scale_exam_progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.scale_users(id) ON DELETE CASCADE,
  mock_id INTEGER NOT NULL,
  responses JSONB NOT NULL DEFAULT '{}'::jsonb,
  status VARCHAR(50) NOT NULL DEFAULT 'in_progress',
  updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  CONSTRAINT uq_scale_user_mock_progress UNIQUE (user_id, mock_id)
);

-- ====================================================================
-- ATOMIC STORED FUNCTIONS
-- ====================================================================

-- Atomic Single-Device Session Replacement
CREATE OR REPLACE FUNCTION public.scale_replace_user_session(
  p_user_id UUID,
  p_token_hash VARCHAR(64),
  p_device_info TEXT,
  p_ip_address TEXT
)
RETURNS TABLE (
  new_session_id UUID,
  revoked_session_id UUID
) 
LANGUAGE plpgsql
AS $$
DECLARE
  v_old_session_id UUID;
  v_new_session_id UUID;
BEGIN
  SELECT id INTO v_old_session_id
  FROM public.scale_user_sessions
  WHERE user_id = p_user_id AND is_active = true
  FOR UPDATE;

  IF v_old_session_id IS NOT NULL THEN
    UPDATE public.scale_user_sessions
    SET is_active = false,
        revoked_at = timezone('utc'::text, now()),
        revocation_reason = 'REPLACED_BY_NEW_DEVICE'
    WHERE id = v_old_session_id;
  END IF;

  INSERT INTO public.scale_user_sessions (
    user_id,
    token_hash,
    device_info,
    ip_address,
    is_active,
    created_at,
    last_seen_at
  )
  VALUES (
    p_user_id,
    p_token_hash,
    p_device_info,
    p_ip_address,
    true,
    timezone('utc'::text, now()),
    timezone('utc'::text, now())
  )
  RETURNING id INTO v_new_session_id;

  RETURN QUERY SELECT v_new_session_id, v_old_session_id;
END;
$$;

-- Atomic Idempotent Entitlement Activation
CREATE OR REPLACE FUNCTION public.scale_activate_entitlement_idempotent(
  p_user_id UUID,
  p_order_id VARCHAR(100),
  p_payment_id VARCHAR(100),
  p_amount_paise INTEGER,
  p_currency VARCHAR(10),
  p_method VARCHAR(50),
  p_signature VARCHAR(255),
  p_raw_payload JSONB
)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE public.scale_orders
  SET status = 'paid',
      updated_at = timezone('utc'::text, now())
  WHERE order_id = p_order_id;

  INSERT INTO public.scale_payments (
    order_id,
    payment_id,
    amount_paise,
    currency,
    status,
    method,
    signature,
    verified_at,
    raw_payload
  )
  VALUES (
    p_order_id,
    p_payment_id,
    p_amount_paise,
    p_currency,
    'captured',
    p_method,
    p_signature,
    timezone('utc'::text, now()),
    p_raw_payload
  )
  ON CONFLICT (payment_id) DO UPDATE
  SET status = 'captured',
      verified_at = timezone('utc'::text, now());

  INSERT INTO public.scale_user_entitlements (
    user_id,
    product_code,
    status,
    granted_via_order_id,
    granted_at
  )
  VALUES (
    p_user_id,
    'SCALE_NEET_60_MOCKS',
    'active',
    p_order_id,
    timezone('utc'::text, now())
  )
  ON CONFLICT (user_id, product_code) DO UPDATE
  SET status = 'active',
      granted_via_order_id = p_order_id;

  RETURN TRUE;
END;
$$;

-- Revoke all sessions
CREATE OR REPLACE FUNCTION public.scale_revoke_all_user_sessions(
  p_user_id UUID,
  p_reason TEXT
)
RETURNS INTEGER
LANGUAGE plpgsql
AS $$
DECLARE
  v_count INTEGER;
BEGIN
  UPDATE public.scale_user_sessions
  SET is_active = false,
      revoked_at = timezone('utc'::text, now()),
      revocation_reason = p_reason
  WHERE user_id = p_user_id AND is_active = true;

  GET DIAGNOSTICS v_count = ROW_COUNT;
  RETURN v_count;
END;
$$;

