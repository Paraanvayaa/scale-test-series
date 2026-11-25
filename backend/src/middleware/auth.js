const config = require('../config');
const { db } = require('../db/supabase');

async function requireAuth(req, res, next) {
  // Extract token from HttpOnly cookie or Authorization header
  let rawToken = req.cookies?.[config.session.cookieName];
  if (!rawToken && req.headers.authorization?.startsWith('Bearer ')) {
    rawToken = req.headers.authorization.slice(7).trim();
  }

  if (!rawToken) {
    return res.status(401).json({
      error: 'UNAUTHENTICATED',
      message: 'Authentication is mandatory before accessing this resource.'
    });
  }

  try {
    const session = await db.getActiveSessionByToken(rawToken);

    if (!session) {
      res.clearCookie(config.session.cookieName);
      return res.status(401).json({
        error: 'INVALID_SESSION',
        message: 'Your session is invalid or expired. Please sign in again.'
      });
    }

    if (!session.is_valid) {
      // Session exists but was revoked (e.g. replaced by newer device login)
      res.clearCookie(config.session.cookieName);
      return res.status(401).json({
        error: 'SESSION_REPLACED',
        title: 'Session Ended',
        message: 'Your account was signed in on another device. For security, this session has been logged out.',
        action: 'Sign In Again'
      });
    }

    // Valid active session
    req.user = { id: session.user_id };
    req.session = session;
    req.rawToken = rawToken;
    next();
  } catch (error) {
    console.error('[Auth Middleware Error]:', error);
    return res.status(500).json({
      error: 'AUTH_SERVER_ERROR',
      message: 'Failed to validate application session.'
    });
  }
}

// Optional Auth (e.g. For landing page / demo checks)
async function optionalAuth(req, res, next) {
  let rawToken = req.cookies?.[config.session.cookieName];
  if (!rawToken && req.headers.authorization?.startsWith('Bearer ')) {
    rawToken = req.headers.authorization.slice(7).trim();
  }

  if (!rawToken) {
    req.user = null;
    req.session = null;
    return next();
  }

  try {
    const session = await db.getActiveSessionByToken(rawToken);
    if (session && session.is_valid) {
      req.user = { id: session.user_id };
      req.session = session;
    } else {
      req.user = null;
      req.session = null;
    }
  } catch {
    req.user = null;
    req.session = null;
  }
  next();
}

module.exports = { requireAuth, optionalAuth };

