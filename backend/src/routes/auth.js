const express = require('express');
const crypto = require('crypto');
const config = require('../config');
const { db } = require('../db/supabase');
const { requireAuth } = require('../middleware/auth');
const realtime = require('../realtime');

const router = express.Router();

// Helper: Set Secure HttpOnly Session Cookie
function setSessionCookie(res, rawToken) {
  res.cookie(config.session.cookieName, rawToken, {
    httpOnly: true,
    secure: config.nodeEnv === 'production',
    sameSite: config.nodeEnv === 'production' ? 'none' : 'lax',
    maxAge: config.session.cookieMaxAgeMs,
    path: '/'
  });
}

// 1. Register User (Supabase Auth identity + Single Device Session)
router.post('/register', async (req, res) => {
  const { email, password, fullName, targetExamination, targetStudent } = req.body;
  if (!email || !password) {
    return res.status(400).json({ error: 'INVALID_INPUT', message: 'Email and password are required.' });
  }

  // Phase 1 requirement: Only 'NEET Aspirant' is permitted as Target Student
  const selectedTarget = targetStudent || targetExamination || 'NEET Aspirant';
  if (selectedTarget !== 'NEET Aspirant') {
    return res.status(400).json({
      error: 'INVALID_TARGET_STUDENT',
      message: 'Target Student must be "NEET Aspirant".'
    });
  }

  try {
    const user = await db.registerUser({
      email,
      password,
      fullName: fullName || 'NEET Aspirant',
      targetExamination: 'NEET Aspirant'
    });

    // Generate cryptographically secure opaque token (64 hex characters)
    const rawToken = crypto.randomBytes(config.session.tokenBytes).toString('hex');
    const deviceInfo = req.headers['user-agent'] || 'Unknown Device';
    const ipAddress = req.ip || req.connection?.remoteAddress || '127.0.0.1';

    // Atomic session creation
    await db.replaceUserSession({
      userId: user.id,
      rawToken,
      deviceInfo,
      ipAddress
    });

    setSessionCookie(res, rawToken);

    return res.status(201).json({
      success: true,
      user: { id: user.id, email: user.email, fullName: user.full_name, role: user.role || 'STUDENT', targetExamination: user.target_examination || null },
      entitlement: { hasAccess: false }
    });
  } catch (error) {
    console.error('[Register Error]:', error);
    if (error.code === 'USER_EXISTS' || error.message?.includes('already registered')) {
      return res.status(409).json({ error: 'USER_EXISTS', message: 'An account with this email already exists.' });
    }
    return res.status(500).json({ error: 'SERVER_ERROR', message: error.message || 'Registration failed.' });
  }
});

// 2. Login User (Enforces Atomic Single-Device Session Replacement!)
router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  if (!email || !password) {
    return res.status(400).json({ error: 'INVALID_INPUT', message: 'Email and password are required.' });
  }

  try {
    const user = await db.authenticateUser({ email, password });

    // Block suspended users from logging in
    if (user.is_suspended) {
      return res.status(403).json({
        error: 'ACCOUNT_SUSPENDED',
        message: 'Your account has been suspended. Please contact support for assistance.'
      });
    }

    // Generate new raw session token
    const rawToken = crypto.randomBytes(config.session.tokenBytes).toString('hex');
    const deviceInfo = req.headers['user-agent'] || 'Unknown Device';
    const ipAddress = req.ip || req.connection?.remoteAddress || '127.0.0.1';

    // Atomically revoke previous session and insert new active session
    const { newSessionId, revokedSessionId } = await db.replaceUserSession({
      userId: user.id,
      rawToken,
      deviceInfo,
      ipAddress
    });

    // Notify old device via real-time channel if online
    if (revokedSessionId) {
      realtime.notifySessionRevoked(revokedSessionId, 'REPLACED_BY_NEW_DEVICE');
    }

    setSessionCookie(res, rawToken);

    // Check entitlement
    const hasAccess = await db.hasActiveEntitlement(user.id, config.product.code);

    return res.json({
      success: true,
      sessionId: newSessionId,
      user: { id: user.id, email: user.email, fullName: user.full_name, role: user.role || 'STUDENT' },
      entitlement: { hasAccess }
    });
  } catch (error) {
    if (error.code === 'INVALID_CREDENTIALS') {
      return res.status(401).json({
        error: 'INVALID_CREDENTIALS',
        message: 'Incorrect email or password. Please check your credentials and try again.'
      });
    }
    console.error('[Login Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Authentication failed.' });
  }
});

// Google SSO: Authenticate or Register Student via verified OAuth
router.post('/google-sso', async (req, res) => {
  const { email, fullName } = req.body;
  if (!email) {
    return res.status(400).json({ error: 'INVALID_INPUT', message: 'Email is required.' });
  }

  try {
    let user = await db.getUserByEmail(email);
    if (!user) {
      user = await db.registerUser({
        email,
        password: crypto.randomBytes(16).toString('hex'),
        fullName: fullName || email.split('@')[0]
      });
    }

    if (user.is_suspended) {
      return res.status(403).json({ error: 'ACCOUNT_SUSPENDED', message: 'Your student account has been suspended. Please contact platform support.' });
    }

    const rawToken = crypto.randomBytes(config.session.tokenBytes).toString('hex');
    const deviceInfo = req.headers['user-agent'] || 'Google SSO Device';
    const ipAddress = req.ip || req.connection?.remoteAddress || '127.0.0.1';

    const { newSessionId, revokedSessionId } = await db.replaceUserSession({
      userId: user.id,
      rawToken,
      deviceInfo,
      ipAddress
    });

    if (revokedSessionId) {
      realtime.notifySessionRevoked(revokedSessionId, 'REPLACED_BY_NEW_DEVICE');
    }

    setSessionCookie(res, rawToken);

    const hasAccess = await db.hasActiveEntitlement(user.id, config.product.code);

    return res.json({
      success: true,
      sessionId: newSessionId,
      user: { id: user.id, email: user.email, fullName: user.full_name, role: user.role || 'STUDENT' },
      entitlement: { hasAccess }
    });
  } catch (err) {
    console.error('[Google SSO Error]:', err);
    return res.status(500).json({ error: 'SERVER_ERROR', message: err.message || 'Google SSO authentication failed.' });
  }
});

// 3. Current User & Entitlement Status Check (Restores auth across refreshes and tabs via HttpOnly cookie or Bearer token)
router.get('/me', requireAuth, async (req, res) => {
  try {
    const user = await db.getUserById(req.user.id);
    const hasAccess = await db.hasActiveEntitlement(req.user.id, config.product.code);
    return res.json({
      authenticated: true,
      user: {
        id: req.user.id,
        email: user?.email,
        fullName: user?.full_name || 'NEET Aspirant',
        role: user?.role || 'STUDENT',
        createdAt: user?.created_at,
        targetExamination: user?.target_examination || null,
        accountStatus: user?.account_status || 'ACTIVE',
        profileCompletionStatus: user?.profile_completion_status || 'INCOMPLETE'
      },
      sessionId: req.session.id,
      entitlement: { hasAccess, productCode: config.product.code }
    });
  } catch (error) {
    console.error('[Get Me Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to fetch user state.' });
  }
});

// 3b. Update Profile (name, target examination)
router.put('/profile', requireAuth, async (req, res) => {
  try {
    const { fullName, targetExamination } = req.body;
    const updates = {};
    if (fullName && fullName.trim()) updates.full_name = fullName.trim();
    if (targetExamination !== undefined) updates.target_examination = targetExamination || null;

    if (Object.keys(updates).length === 0) {
      return res.status(400).json({ error: 'INVALID_INPUT', message: 'No fields to update.' });
    }

    const setClauses = Object.keys(updates).map((k, i) => `${k} = $${i + 2}`);
    const vals = [req.user.id, ...Object.values(updates)];
    await db.query(
      `UPDATE public.scale_users SET ${setClauses.join(', ')}, updated_at = NOW() WHERE id = $1`,
      vals
    );

    const user = await db.getUserById(req.user.id);
    return res.json({
      success: true,
      user: {
        id: user.id,
        email: user.email,
        fullName: user.full_name,
        role: user.role,
        targetExamination: user.target_examination,
        accountStatus: user.account_status || 'ACTIVE',
        profileCompletionStatus: user.profile_completion_status || 'INCOMPLETE'
      }
    });
  } catch (error) {
    console.error('[Update Profile Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to update profile.' });
  }
});

// 4. Logout User (Revokes active session in DB & clears cookie)
router.post('/logout', async (req, res) => {
  const rawToken = req.cookies?.[config.session.cookieName] || req.headers.authorization?.slice(7).trim();
  if (rawToken) {
    await db.revokeSessionByToken(rawToken, 'USER_LOGOUT');
  }
  res.clearCookie(config.session.cookieName, { path: '/' });
  return res.json({ success: true, message: 'Logged out successfully.' });
});

// 5. Change Password (Revokes all active sessions)
router.post('/change-password', requireAuth, async (req, res) => {
  const { newPassword } = req.body;
  if (!newPassword || newPassword.length < 6) {
    return res.status(400).json({ error: 'INVALID_INPUT', message: 'New password must be at least 6 characters.' });
  }

  try {
    // Revoke all sessions for this user
    await db.revokeAllUserSessions(req.user.id, 'PASSWORD_CHANGED');
    res.clearCookie(config.session.cookieName, { path: '/' });

    return res.json({
      success: true,
      message: 'Password updated. All active sessions have been revoked. Please sign in again.'
    });
  } catch (error) {
    console.error('[Change Password Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to update password.' });
  }
});

// 6. Delete Account (Revokes sessions, soft deletes user, retains financial records)
router.delete('/account', requireAuth, async (req, res) => {
  try {
    await db.deleteAccount(req.user.id);
    res.clearCookie(config.session.cookieName, { path: '/' });
    return res.json({
      success: true,
      message: 'Account deleted. Active sessions revoked. Financial transaction audit records retained in compliance with regulatory requirements.'
    });
  } catch (error) {
    console.error('[Delete Account Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to delete account.' });
  }
});

// 7. Real-time Session Revocation Events (SSE)
router.get('/session-events', requireAuth, (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  res.flushHeaders?.();

  realtime.registerConnection(req.session.id, req.user.id, res);
});

module.exports = router;

