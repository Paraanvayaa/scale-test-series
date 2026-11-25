const config = require('../config');
const { db } = require('../db/supabase');

async function requireAdmin(req, res, next) {
  let rawToken = req.cookies?.[config.session.cookieName];
  if (!rawToken && req.headers.authorization?.startsWith('Bearer ')) {
    rawToken = req.headers.authorization.slice(7).trim();
  }

  if (!rawToken) {
    return res.status(401).json({
      error: 'UNAUTHENTICATED',
      message: 'Administrator authentication required.'
    });
  }

  try {
    const session = await db.getActiveSessionByToken(rawToken);
    if (!session || !session.is_valid) {
      res.clearCookie(config.session.cookieName);
      return res.status(401).json({
        error: 'SESSION_EXPIRED',
        message: 'Your administrator session has expired or was revoked. Please log in again.'
      });
    }

    // Fetch user details and role from database
    const user = await db.getUserById(session.user_id);
    if (!user) {
      res.clearCookie(config.session.cookieName);
      return res.status(401).json({ error: 'USER_NOT_FOUND', message: 'User not found.' });
    }

    if (user.is_suspended) {
      res.clearCookie(config.session.cookieName);
      return res.status(403).json({
        error: 'ACCOUNT_SUSPENDED',
        message: 'This account has been suspended by an administrator.'
      });
    }

    const adminRoles = ['SUPER_ADMIN', 'ADMIN', 'SUPPORT'];
    if (!adminRoles.includes(user.role)) {
      return res.status(403).json({
        error: 'FORBIDDEN',
        message: 'Access denied: Administrative privileges required.'
      });
    }

    req.user = user;
    req.admin = {
      id: user.id,
      email: user.email,
      fullName: user.full_name,
      role: user.role
    };
    req.session = session;
    next();
  } catch (error) {
    console.error('[Admin Auth Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to authenticate administrator.' });
  }
}

function requireSuperAdmin(req, res, next) {
  if (!req.admin || req.admin.role !== 'SUPER_ADMIN') {
    return res.status(403).json({
      error: 'SUPER_ADMIN_REQUIRED',
      message: 'Access denied: Only Super Administrators can perform this action.'
    });
  }
  next();
}

module.exports = { requireAdmin, requireSuperAdmin };

