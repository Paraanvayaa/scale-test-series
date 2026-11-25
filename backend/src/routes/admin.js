const express = require('express');
const crypto = require('crypto');
const config = require('../config');
const { db } = require('../db/supabase');
const { requireAdmin, requireSuperAdmin } = require('../middleware/adminAuth');

const router = express.Router();

function setSessionCookie(res, rawToken) {
  res.cookie(config.session.cookieName, rawToken, {
    httpOnly: true,
    secure: config.nodeEnv === 'production',
    sameSite: config.nodeEnv === 'production' ? 'none' : 'lax',
    maxAge: config.session.cookieMaxAgeMs,
    path: '/'
  });
}

// ====================================================================
// ADMIN AUTHENTICATION
// ====================================================================

// 1. Admin Login (Dedicated, role-verified, rate-safe)
router.post('/auth/login', async (req, res) => {
  const { email, password } = req.body;
  if (!email || !password) {
    return res.status(400).json({ error: 'INVALID_INPUT', message: 'Email and password are required.' });
  }

  try {
    const user = await db.authenticateUser({ email, password });

    // Enforce administrative role verification on server
    const adminRoles = ['SUPER_ADMIN', 'ADMIN', 'SUPPORT'];
    if (!adminRoles.includes(user.role)) {
      return res.status(403).json({
        error: 'FORBIDDEN',
        message: 'Access denied: You do not have administrative privileges.'
      });
    }

    if (user.is_suspended) {
      return res.status(403).json({
        error: 'ACCOUNT_SUSPENDED',
        message: 'Your administrator account has been suspended.'
      });
    }

    // Generate secure opaque token
    const rawToken = crypto.randomBytes(config.session.tokenBytes).toString('hex');
    const deviceInfo = req.headers['user-agent'] || 'Admin Console';
    const ipAddress = req.ip || req.connection?.remoteAddress || '127.0.0.1';

    // Replace session atomically
    await db.replaceUserSession({
      userId: user.id,
      rawToken,
      deviceInfo,
      ipAddress
    });

    setSessionCookie(res, rawToken);

    return res.json({
      success: true,
      admin: {
        id: user.id,
        email: user.email,
        fullName: user.full_name,
        role: user.role
      }
    });
  } catch (error) {
    if (error.code === 'INVALID_CREDENTIALS') {
      return res.status(401).json({ error: 'INVALID_CREDENTIALS', message: 'Invalid administrator credentials.' });
    }
    console.error('[Admin Login Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Admin authentication failed.' });
  }
});

// 2. Admin Get Profile & Permissions
router.get('/auth/me', requireAdmin, (req, res) => {
  return res.json({
    authenticated: true,
    admin: req.admin
  });
});

// 3. Admin Logout
router.post('/auth/logout', async (req, res) => {
  const rawToken = req.cookies?.[config.session.cookieName] || req.headers.authorization?.slice(7).trim();
  if (rawToken) {
    await db.revokeSessionByToken(rawToken, 'ADMIN_LOGOUT');
  }
  res.clearCookie(config.session.cookieName, { path: '/' });
  return res.json({ success: true, message: 'Administrator logged out successfully.' });
});

// ====================================================================
// DASHBOARD OVERVIEW & ANALYTICS
// ====================================================================

router.get('/dashboard/overview', requireAdmin, async (req, res) => {
  try {
    const stats = await db.getDashboardOverview();
    return res.json({ success: true, stats });
  } catch (error) {
    console.error('[Dashboard Overview Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to fetch dashboard metrics.' });
  }
});

// ====================================================================
// STUDENT MANAGEMENT
// ====================================================================

// 1. List Students (Paginated, Search, Filter)
router.get('/students', requireAdmin, async (req, res) => {
  try {
    const { search = '', filterStatus = '', filterPaid = '', page = 1, limit = 25 } = req.query;
    const result = await db.getStudents({
      search,
      filterStatus,
      filterPaid,
      page: parseInt(page, 10) || 1,
      limit: parseInt(limit, 10) || 25
    });
    return res.json({ success: true, ...result });
  } catch (error) {
    console.error('[Get Students Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to fetch student directory.' });
  }
});

// 2. Student Detail Profile
router.get('/students/:studentId', requireAdmin, async (req, res) => {
  try {
    const profile = await db.getStudentProfileDetail(req.params.studentId);
    if (!profile) {
      return res.status(404).json({ error: 'NOT_FOUND', message: 'Student profile not found.' });
    }
    return res.json({ success: true, profile });
  } catch (error) {
    console.error('[Get Student Profile Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to fetch student profile.' });
  }
});

// 3. Suspend Student Account
router.post('/students/:studentId/suspend', requireAdmin, async (req, res) => {
  const { reason, suspensionType = 'TEMPORARY_SUSPENSION', adminNotes = '', expiresAt = null } = req.body;
  if (!reason || !reason.trim()) {
    return res.status(400).json({ error: 'REASON_REQUIRED', message: 'A valid suspension reason is mandatory.' });
  }

  try {
    await db.suspendStudent({
      studentId: req.params.studentId,
      adminId: req.admin.id,
      adminEmail: req.admin.email,
      adminRole: req.admin.role,
      suspensionType,
      reason,
      adminNotes,
      expiresAt
    });

    return res.json({
      success: true,
      message: 'Student account suspended successfully. All active sessions have been revoked.'
    });
  } catch (error) {
    console.error('[Suspend Student Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: error.message || 'Failed to suspend account.' });
  }
});

// 4. Reactivate Student Account
router.post('/students/:studentId/reactivate', requireAdmin, async (req, res) => {
  const { reason = 'Administrator review completed' } = req.body;

  try {
    await db.reactivateStudent({
      studentId: req.params.studentId,
      adminId: req.admin.id,
      adminEmail: req.admin.email,
      adminRole: req.admin.role,
      reason
    });

    return res.json({
      success: true,
      message: 'Student account reactivated successfully. Student must log in again.'
    });
  } catch (error) {
    console.error('[Reactivate Student Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: error.message || 'Failed to reactivate account.' });
  }
});

// 5. Grant Complimentary Access
router.post('/students/:studentId/grant-access', requireAdmin, async (req, res) => {
  const { reason, productCode = 'SCALE_NEET_60_MOCKS', expiresAt = null } = req.body;
  if (!reason || !reason.trim()) {
    return res.status(400).json({ error: 'REASON_REQUIRED', message: 'Reason for complimentary access is mandatory.' });
  }

  try {
    await db.grantComplimentaryAccess({
      studentId: req.params.studentId,
      adminId: req.admin.id,
      adminEmail: req.admin.email,
      adminRole: req.admin.role,
      productCode,
      reason,
      expiresAt
    });

    return res.json({
      success: true,
      message: 'Complimentary examination access granted successfully.'
    });
  } catch (error) {
    console.error('[Grant Access Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: error.message || 'Failed to grant access.' });
  }
});

// 6. Revoke Examination Access
router.post('/students/:studentId/revoke-access', requireAdmin, async (req, res) => {
  const { reason, productCode = 'SCALE_NEET_60_MOCKS' } = req.body;
  if (!reason || !reason.trim()) {
    return res.status(400).json({ error: 'REASON_REQUIRED', message: 'Reason for revocation is mandatory.' });
  }

  try {
    await db.revokeAccess({
      studentId: req.params.studentId,
      adminId: req.admin.id,
      adminEmail: req.admin.email,
      adminRole: req.admin.role,
      productCode,
      reason
    });

    return res.json({
      success: true,
      message: 'Examination access revoked successfully. Financial transaction records preserved.'
    });
  } catch (error) {
    console.error('[Revoke Access Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: error.message || 'Failed to revoke access.' });
  }
});

// 7. Revoke Student Active Session
router.post('/students/:studentId/revoke-session', requireAdmin, async (req, res) => {
  try {
    const count = await db.revokeAllUserSessions(req.params.studentId, 'ADMIN_FORCE_LOGOUT');
    return res.json({
      success: true,
      message: `Revoked ${count} active session(s) for student.`
    });
  } catch (error) {
    console.error('[Revoke Session Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to revoke student sessions.' });
  }
});

// 8. Add Admin Internal Note
router.post('/students/:studentId/notes', requireAdmin, async (req, res) => {
  const { note } = req.body;
  if (!note || !note.trim()) {
    return res.status(400).json({ error: 'NOTE_REQUIRED', message: 'Note text is required.' });
  }

  try {
    const item = await db.addAdminNote({
      studentId: req.params.studentId,
      adminId: req.admin.id,
      adminEmail: req.admin.email,
      note: note.trim()
    });

    return res.json({ success: true, note: item });
  } catch (error) {
    console.error('[Add Note Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to save admin note.' });
  }
});

// ====================================================================
// PAYMENTS & RECONCILIATION
// ====================================================================

router.get('/payments', requireAdmin, async (req, res) => {
  try {
    const { search = '', status = '', page = 1, limit = 25 } = req.query;
    const result = await db.getPayments({
      search,
      status,
      page: parseInt(page, 10) || 1,
      limit: parseInt(limit, 10) || 25
    });
    return res.json({ success: true, ...result });
  } catch (error) {
    console.error('[Get Payments Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to fetch payments.' });
  }
});

// ====================================================================
// DEVICE SESSIONS DIRECTORY
// ====================================================================

router.get('/sessions', requireAdmin, async (req, res) => {
  try {
    const { page = 1, limit = 25 } = req.query;
    const result = await db.getSessions({
      page: parseInt(page, 10) || 1,
      limit: parseInt(limit, 10) || 25
    });
    return res.json({ success: true, ...result });
  } catch (error) {
    console.error('[Get Sessions Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to fetch device sessions.' });
  }
});

router.post('/sessions/:sessionId/revoke', requireAdmin, async (req, res) => {
  try {
    const revoked = await db.revokeSessionById(req.params.sessionId, 'ADMIN_FORCE_LOGOUT');
    return res.json({ success: revoked, message: revoked ? 'Session revoked.' : 'Session already revoked or not found.' });
  } catch (error) {
    console.error('[Revoke Session Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to revoke session.' });
  }
});

// ====================================================================
// AUDIT LOGS & NOTIFICATIONS
// ====================================================================

router.get('/audit-logs', requireAdmin, async (req, res) => {
  try {
    const logs = await db.getAuditLogs({ limit: parseInt(req.query.limit || 50, 10) });
    return res.json({ success: true, logs });
  } catch (error) {
    console.error('[Get Audit Logs Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to fetch audit logs.' });
  }
});

router.get('/notifications', requireAdmin, async (req, res) => {
  try {
    const notifications = await db.getAdminNotifications({ limit: parseInt(req.query.limit || 30, 10) });
    return res.json({ success: true, notifications });
  } catch (error) {
    console.error('[Get Notifications Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to fetch notifications.' });
  }
});

// ====================================================================
// REPORTS & CSV EXPORT
// ====================================================================

router.get('/reports/export', requireAdmin, async (req, res) => {
  const type = req.query.type || 'students';

  try {
    if (type === 'students') {
      const data = await db.getStudents({ limit: 1000 });
      let csv = 'Student ID,Email,Full Name,Phone,Registered At,Last Login,Account Status,Paid Status\n';
      data.students.forEach(s => {
        csv += `"${s.id}","${s.email}","${s.full_name || ''}","${s.phone || ''}","${s.created_at}","${s.last_login || ''}","${s.is_suspended ? 'SUSPENDED' : 'ACTIVE'}","${s.is_paid ? 'PAID' : 'FREE'}"\n`;
      });
      res.setHeader('Content-Type', 'text/csv');
      res.setHeader('Content-Disposition', 'attachment; filename="scale_students_report.csv"');
      return res.send(csv);
    } else if (type === 'payments') {
      const data = await db.getPayments({ limit: 1000 });
      let csv = 'Payment ID,Order ID,Student Email,Amount INR,Currency,Method,Status,Created At\n';
      data.payments.forEach(p => {
        csv += `"${p.payment_id}","${p.order_id}","${p.student_email || ''}","${p.amount_inr}","${p.currency}","${p.method}","${p.status}","${p.created_at}"\n`;
      });
      res.setHeader('Content-Type', 'text/csv');
      res.setHeader('Content-Disposition', 'attachment; filename="scale_payments_report.csv"');
      return res.send(csv);
    } else {
      return res.status(400).json({ error: 'INVALID_TYPE', message: 'Invalid export type. Use "students" or "payments".' });
    }
  } catch (error) {
    console.error('[Export Report Error]:', error);
    return res.status(500).json({ error: 'SERVER_ERROR', message: 'Failed to generate export report.' });
  }
});

module.exports = router;

