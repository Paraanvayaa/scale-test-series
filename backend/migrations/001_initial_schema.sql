-- ====================================================================
-- SCALE TEST SERIES - PHASE 18 & 19 PRODUCTION DATABASE SCHEMA
-- Target Database: Supabase PostgreSQL
-- ====================================================================

-- 1. Profiles Table (Mirrors Supabase auth.users)
CREATE TABLE IF NOT EXISTS public.profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT NOT NULL,
  full_name TEXT,
  phone TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  deleted_at TIMESTAMPTZ
);

-- Index on email
CREATE INDEX IF NOT EXISTS idx_profiles_email ON public.profiles(email);

-- 2. Single-Device Application Sessions
-- Stores cryptographic hashes of opaque application session tokens
CREATE TABLE IF NOT EXISTS public.user_sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  token_hash VARCHAR(64) NOT NULL UNIQUE,
  device_info TEXT,
  ip_address TEXT,
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  last_seen_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  revoked_at TIMESTAMPTZ,
  revocation_reason TEXT
);

-- Critical constraint: exactly ONE active session per user at any time!
CREATE UNIQUE INDEX IF NOT EXISTS idx_active_user_session 
ON public.user_sessions (user_id) 
WHERE (is_active = true);

CREATE INDEX IF NOT EXISTS idx_user_sessions_lookup 
ON public.user_sessions (token_hash, is_active);

-- 3. Orders Table (Financial Audit Trail - Preserved on Account Deletion)
CREATE TABLE IF NOT EXISTS public.orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE RESTRICT,
  order_id VARCHAR(100) NOT NULL UNIQUE, -- Razorpay order_id
  amount_paise INTEGER NOT NULL,          -- e.g. 99900 = Rs 999
  currency VARCHAR(10) NOT NULL DEFAULT 'INR',
  status VARCHAR(50) NOT NULL DEFAULT 'created', -- 'created', 'pending', 'paid', 'failed'
  product_code VARCHAR(50) NOT NULL DEFAULT 'SCALE_NEET_60_MOCKS',
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_orders_user_id ON public.orders(user_id);
CREATE INDEX IF NOT EXISTS idx_orders_order_id ON public.orders(order_id);

-- 4. Payments Table (Idempotent Payment Transactions)
CREATE TABLE IF NOT EXISTS public.payments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id VARCHAR(100) NOT NULL REFERENCES public.orders(order_id) ON DELETE RESTRICT,
  payment_id VARCHAR(100) NOT NULL UNIQUE, -- Razorpay payment_id
  amount_paise INTEGER NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'INR',
  status VARCHAR(50) NOT NULL,            -- 'captured', 'failed', 'refunded'
  method VARCHAR(50),                     -- 'upi', 'card', 'netbanking'
  signature VARCHAR(255),
  verified_at TIMESTAMPTZ,
  raw_payload JSONB,
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_payments_payment_id ON public.payments(payment_id);
CREATE INDEX IF NOT EXISTS idx_payments_order_id ON public.payments(order_id);

-- 5. User Entitlements (Paid Access Control)
CREATE TABLE IF NOT EXISTS public.user_entitlements (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  product_code VARCHAR(50) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'active', -- 'active', 'revoked', 'expired'
  granted_via_order_id VARCHAR(100) REFERENCES public.orders(order_id) ON DELETE RESTRICT,
  granted_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  expires_at TIMESTAMPTZ,
  -- Ensures idempotent entitlement activation (no duplicate purchases)
  CONSTRAINT uq_user_product_entitlement UNIQUE (user_id, product_code)
);

CREATE INDEX IF NOT EXISTS idx_entitlements_user_product ON public.user_entitlements(user_id, product_code, status);

-- 6. Exam Progress & Answer Submissions (Student Data Isolation)
CREATE TABLE IF NOT EXISTS public.exam_progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  mock_id INTEGER NOT NULL,
  responses JSONB NOT NULL DEFAULT '{}'::jsonb,
  status VARCHAR(50) NOT NULL DEFAULT 'in_progress', -- 'in_progress', 'completed'
  score INTEGER,
  time_spent_seconds INTEGER DEFAULT 0,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
  CONSTRAINT uq_user_mock_progress UNIQUE (user_id, mock_id)
);

-- ====================================================================
-- ATOMIC DATABASE FUNCTIONS
-- ====================================================================

-- Function 1: Atomic Single-Device Session Replacement
-- Atomically revokes any existing active session and inserts new active session
CREATE OR REPLACE FUNCTION public.replace_user_session(
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
SECURITY DEFINER
AS $$
DECLARE
  v_old_session_id UUID;
  v_new_session_id UUID;
BEGIN
  -- 1. Find and revoke existing active session for this user
  SELECT id INTO v_old_session_id
  FROM public.user_sessions
  WHERE user_id = p_user_id AND is_active = true
  FOR UPDATE;

  IF v_old_session_id IS NOT NULL THEN
    UPDATE public.user_sessions
    SET is_active = false,
        revoked_at = timezone('utc'::text, now()),
        revocation_reason = 'REPLACED_BY_NEW_DEVICE'
    WHERE id = v_old_session_id;
  END IF;

  -- 2. Insert new active session
  INSERT INTO public.user_sessions (
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

-- Function 2: Atomic Idempotent Payment Reconciliation & Entitlement Grant
CREATE OR REPLACE FUNCTION public.activate_entitlement_idempotent(
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
SECURITY DEFINER
AS $$
BEGIN
  -- 1. Update Order status to 'paid'
  UPDATE public.orders
  SET status = 'paid',
      updated_at = timezone('utc'::text, now())
  WHERE order_id = p_order_id;

  -- 2. Insert payment record (Idempotent via ON CONFLICT)
  INSERT INTO public.payments (
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

  -- 3. Activate Entitlement (Idempotent via ON CONFLICT)
  INSERT INTO public.user_entitlements (
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

-- Function 3: Revoke all user sessions (Password Change / Account Deletion)
CREATE OR REPLACE FUNCTION public.revoke_all_user_sessions(
  p_user_id UUID,
  p_reason TEXT
)
RETURNS INTEGER
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
  v_count INTEGER;
BEGIN
  UPDATE public.user_sessions
  SET is_active = false,
      revoked_at = timezone('utc'::text, now()),
      revocation_reason = p_reason
  WHERE user_id = p_user_id AND is_active = true;

  GET DIAGNOSTICS v_count = ROW_COUNT;
  RETURN v_count;
END;
$$;

-- ====================================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- ====================================================================
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.orders ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.payments ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_entitlements ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.exam_progress ENABLE ROW LEVEL SECURITY;

-- Profiles: Users can read and update their own profile
CREATE POLICY "Users can read own profile" ON public.profiles
  FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users can update own profile" ON public.profiles
  FOR UPDATE USING (auth.uid() = id);

-- Exam Progress: Students can access only their own progress
CREATE POLICY "Users access own exam progress" ON public.exam_progress
  FOR ALL USING (auth.uid() = id);

-- Entitlements: Users can view own entitlements
CREATE POLICY "Users can view own entitlements" ON public.user_entitlements
  FOR SELECT USING (auth.uid() = user_id);

-- Backend Service Role handles all session & payment validation with privileged key

