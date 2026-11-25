const { Pool } = require('pg');
const crypto = require('crypto');
const config = require('../config');

let dbPool = null;
const dbUrl = process.env.DATABASE_URL;

if (dbUrl) {
  try {
    dbPool = new Pool({
      connectionString: dbUrl,
      ssl: { rejectUnauthorized: false }
    });
    console.log('[Database] Connected to Supabase PostgreSQL Database (Postgres 17 pooler)');
  } catch (err) {
    console.warn('[Database] Failed to initialize Postgres pool, falling back to local engine:', err.message);
  }
} else {
  console.log('[Database] DATABASE_URL not provided in environment. Using in-memory engine.');
}

// In-Memory Fallback Store (Implements identical logic for testing and offline fallback)
class LocalDatabaseStore {
  constructor() {
    this.users = new Map();
    this.userSessions = new Map();
    this.orders = new Map();
    this.payments = new Map();
    this.userEntitlements = new Map();
    this.examProgress = new Map();
    this.auditLogs = [];
    this.adminNotes = [];
    this.adminNotifications = [];
    this.suspensions = [];
  }

  hashToken(token) {
    return crypto.createHash('sha256').update(token).digest('hex');
  }

  async replaceUserSession({ userId, rawToken, deviceInfo, ipAddress }) {
    const tokenHash = this.hashToken(rawToken);
    let revokedSessionId = null;
    for (const [id, session] of this.userSessions.entries()) {
      if (session.user_id === userId && session.is_active) {
        session.is_active = false;
        session.revoked_at = new Date().toISOString();
        session.revocation_reason = 'REPLACED_BY_NEW_DEVICE';
        revokedSessionId = id;
      }
    }
    const newSessionId = crypto.randomUUID();
    const newSession = {
      id: newSessionId,
      user_id: userId,
      token_hash: tokenHash,
      device_info: deviceInfo || 'Unknown Device',
      ip_address: ipAddress || '127.0.0.1',
      is_active: true,
      created_at: new Date().toISOString(),
      last_seen_at: new Date().toISOString(),
      revoked_at: null,
      revocation_reason: null
    };
    this.userSessions.set(newSessionId, newSession);
    return { newSessionId, revokedSessionId };
  }

  async getActiveSessionByToken(rawToken) {
    if (!rawToken) return null;
    const tokenHash = this.hashToken(rawToken);
    for (const session of this.userSessions.values()) {
      if (session.token_hash === tokenHash) {
        if (session.is_active) {
          session.last_seen_at = new Date().toISOString();
          return { ...session, is_valid: true };
        } else {
          return { ...session, is_valid: false, reason: session.revocation_reason || 'REVOKED' };
        }
      }
    }
    return null;
  }

  async revokeSessionByToken(rawToken, reason = 'USER_LOGOUT') {
    if (!rawToken) return false;
    const tokenHash = this.hashToken(rawToken);
    for (const session of this.userSessions.values()) {
      if (session.token_hash === tokenHash && session.is_active) {
        session.is_active = false;
        session.revoked_at = new Date().toISOString();
        session.revocation_reason = reason;
        return true;
      }
    }
    return false;
  }

  async revokeAllUserSessions(userId, reason = 'PASSWORD_CHANGED') {
    let count = 0;
    for (const session of this.userSessions.values()) {
      if (session.user_id === userId && session.is_active) {
        session.is_active = false;
        session.revoked_at = new Date().toISOString();
        session.revocation_reason = reason;
        count++;
      }
    }
    return count;
  }

  async createOrder({ userId, orderId, amountPaise, currency = 'INR', productCode }) {
    const order = {
      id: crypto.randomUUID(),
      user_id: userId,
      order_id: orderId,
      amount_paise: amountPaise,
      currency,
      status: 'created',
      product_code: productCode,
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    };
    this.orders.set(orderId, order);
    return order;
  }

  async getOrderByOrderId(orderId) {
    return this.orders.get(orderId) || null;
  }

  async hasActiveEntitlement(userId, productCode) {
    const key = `${userId}:${productCode}`;
    const ent = this.userEntitlements.get(key);
    return !!(ent && ent.status === 'active');
  }

  async activateEntitlementIdempotent({ userId, orderId, paymentId, amountPaise, currency, method, signature, rawPayload }) {
    const order = this.orders.get(orderId);
    if (order) {
      order.status = 'paid';
      order.updated_at = new Date().toISOString();
    }
    if (!this.payments.has(paymentId)) {
      this.payments.set(paymentId, {
        id: crypto.randomUUID(),
        order_id: orderId,
        payment_id: paymentId,
        amount_paise: amountPaise,
        currency: currency || 'INR',
        status: 'captured',
        method: method || 'unknown',
        signature: signature || null,
        verified_at: new Date().toISOString(),
        raw_payload: rawPayload || {},
        created_at: new Date().toISOString()
      });
    }
    const key = `${userId}:SCALE_NEET_60_MOCKS`;
    this.userEntitlements.set(key, {
      id: crypto.randomUUID(),
      user_id: userId,
      product_code: 'SCALE_NEET_60_MOCKS',
      status: 'active',
      source_type: 'PURCHASE',
      granted_via_order_id: orderId,
      granted_at: new Date().toISOString()
    });
    return true;
  }

  async registerUser({ email, password, fullName, role = 'STUDENT' }) {
    const existing = await this.getUserByEmail(email);
    if (existing) {
      const err = new Error('User already exists');
      err.code = 'USER_EXISTS';
      throw err;
    }
    const userId = crypto.randomUUID();
    const user = {
      id: userId,
      email,
      passwordHash: crypto.createHash('sha256').update(password).digest('hex'),
      full_name: fullName,
      role,
      is_suspended: false,
      created_at: new Date().toISOString()
    };
    this.users.set(userId, user);
    return user;
  }

  async getUserByEmail(email) {
    for (const user of this.users.values()) {
      if (user.email.toLowerCase() === email.toLowerCase()) return user;
    }
    return null;
  }

  async getUserById(userId) {
    return this.users.get(userId) || null;
  }

  async authenticateUser({ email, password }) {
    const user = await this.getUserByEmail(email);
    if (!user) {
      const err = new Error('Invalid credentials');
      err.code = 'INVALID_CREDENTIALS';
      throw err;
    }
    const hash = crypto.createHash('sha256').update(password).digest('hex');
    if (user.passwordHash !== hash) {
      const err = new Error('Invalid credentials');
      err.code = 'INVALID_CREDENTIALS';
      throw err;
    }
    return user;
  }

  async deleteAccount(userId) {
    await this.revokeAllUserSessions(userId, 'ACCOUNT_DELETED');
    const user = this.users.get(userId);
    if (user) user.deleted_at = new Date().toISOString();
    return true;
  }

  // Admin In-Memory Methods
  async getDashboardOverview() {
    let totalStudents = 0;
    let activeAccounts = 0;
    let suspendedAccounts = 0;
    const now = new Date();
    const todayStr = now.toISOString().slice(0, 10);
    let newRegistrationsToday = 0;

    for (const u of this.users.values()) {
      if (u.role === 'STUDENT' && !u.deleted_at) {
        totalStudents++;
        if (u.is_suspended) suspendedAccounts++;
        else activeAccounts++;
        if (u.created_at && u.created_at.slice(0, 10) === todayStr) {
          newRegistrationsToday++;
        }
      }
    }

    let totalSuccessfulPayments = 0;
    let totalRevenuePaise = 0;
    let todayRevenuePaise = 0;
    for (const p of this.payments.values()) {
      if (p.status === 'captured') {
        totalSuccessfulPayments++;
        totalRevenuePaise += p.amount_paise || 0;
        if (p.created_at && p.created_at.slice(0, 10) === todayStr) {
          todayRevenuePaise += p.amount_paise || 0;
        }
      }
    }

    let activeSessions = 0;
    for (const s of this.userSessions.values()) {
      if (s.is_active) activeSessions++;
    }

    let paidStudents = 0;
    for (const ent of this.userEntitlements.values()) {
      if (ent.status === 'active') paidStudents++;
    }

    return {
      totalStudents,
      newRegistrationsToday,
      activeAccounts,
      suspendedAccounts,
      totalSuccessfulPayments,
      totalRevenueINR: totalRevenuePaise / 100,
      todayRevenueINR: todayRevenuePaise / 100,
      activeSessions,
      paidStudents
    };
  }

  async getStudents({ search = '', filterStatus = '', filterPaid = '', page = 1, limit = 25 }) {
    let list = [];
    for (const u of this.users.values()) {
      if (u.role === 'STUDENT' && !u.deleted_at) {
        if (search) {
          const q = search.toLowerCase();
          const match = (u.email && u.email.toLowerCase().includes(q)) ||
                        (u.full_name && u.full_name.toLowerCase().includes(q)) ||
                        u.id.includes(q);
          if (!match) continue;
        }
        if (filterStatus === 'ACTIVE' && u.is_suspended) continue;
        if (filterStatus === 'SUSPENDED' && !u.is_suspended) continue;

        const isPaid = await this.hasActiveEntitlement(u.id, 'SCALE_NEET_60_MOCKS');
        if (filterPaid === 'PAID' && !isPaid) continue;
        if (filterPaid === 'FREE' && isPaid) continue;

        let hasActiveSession = false;
        let lastLogin = u.created_at;
        for (const s of this.userSessions.values()) {
          if (s.user_id === u.id) {
            if (s.is_active) hasActiveSession = true;
            if (s.last_seen_at && s.last_seen_at > lastLogin) lastLogin = s.last_seen_at;
          }
        }

        list.push({
          id: u.id,
          email: u.email,
          full_name: u.full_name,
          phone: u.phone || 'N/A',
          created_at: u.created_at,
          last_login: lastLogin,
          is_suspended: u.is_suspended,
          suspension_reason: u.suspension_reason,
          is_paid: isPaid,
          has_active_session: hasActiveSession
        });
      }
    }

    const total = list.length;
    const offset = (page - 1) * limit;
    const paginated = list.slice(offset, offset + limit);

    return { students: paginated, total, page, limit, totalPages: Math.ceil(total / limit) || 1 };
  }

  async suspendStudent({ studentId, adminId, adminEmail, adminRole, suspensionType, reason, adminNotes, expiresAt }) {
    const user = this.users.get(studentId);
    if (!user) throw new Error('Student not found');
    user.is_suspended = true;
    user.suspension_reason = reason;
    await this.revokeAllUserSessions(studentId, 'ACCOUNT_SUSPENDED');
    this.auditLogs.unshift({
      id: crypto.randomUUID(),
      admin_id: adminId,
      admin_email: adminEmail,
      admin_role: adminRole,
      action: 'STUDENT_SUSPENDED',
      target_user_id: studentId,
      reason,
      created_at: new Date().toISOString()
    });
    return true;
  }

  async reactivateStudent({ studentId, adminId, adminEmail, adminRole, reason }) {
    const user = this.users.get(studentId);
    if (!user) throw new Error('Student not found');
    user.is_suspended = false;
    user.suspension_reason = null;
    this.auditLogs.unshift({
      id: crypto.randomUUID(),
      admin_id: adminId,
      admin_email: adminEmail,
      admin_role: adminRole,
      action: 'STUDENT_REACTIVATED',
      target_user_id: studentId,
      reason,
      created_at: new Date().toISOString()
    });
    return true;
  }

  async grantComplimentaryAccess({ studentId, adminId, adminEmail, adminRole, productCode = 'SCALE_NEET_60_MOCKS', reason, expiresAt }) {
    const key = `${studentId}:${productCode}`;
    this.userEntitlements.set(key, {
      id: crypto.randomUUID(),
      user_id: studentId,
      product_code: productCode,
      status: 'active',
      source_type: 'COMPLIMENTARY',
      admin_notes: reason,
      granted_at: new Date().toISOString(),
      expires_at: expiresAt || null
    });
    this.auditLogs.unshift({
      id: crypto.randomUUID(),
      admin_id: adminId,
      admin_email: adminEmail,
      admin_role: adminRole,
      action: 'COMPLIMENTARY_ACCESS_GRANTED',
      target_user_id: studentId,
      reason,
      created_at: new Date().toISOString()
    });
    return true;
  }

  async revokeAccess({ studentId, adminId, adminEmail, adminRole, productCode = 'SCALE_NEET_60_MOCKS', reason }) {
    const key = `${studentId}:${productCode}`;
    const ent = this.userEntitlements.get(key);
    if (ent) {
      ent.status = 'revoked';
      ent.revoked_at = new Date().toISOString();
      ent.revoked_by = adminId;
    }
    this.auditLogs.unshift({
      id: crypto.randomUUID(),
      admin_id: adminId,
      admin_email: adminEmail,
      admin_role: adminRole,
      action: 'ACCESS_REVOKED',
      target_user_id: studentId,
      reason,
      created_at: new Date().toISOString()
    });
    return true;
  }

  async addAdminNote({ studentId, adminId, adminEmail, note }) {
    const item = {
      id: crypto.randomUUID(),
      student_id: studentId,
      admin_id: adminId,
      admin_email: adminEmail,
      note,
      created_at: new Date().toISOString()
    };
    this.adminNotes.unshift(item);
    return item;
  }

  async getAdminNotes(studentId) {
    return this.adminNotes.filter(n => n.student_id === studentId);
  }

  async getPayments({ search = '', status = '', page = 1, limit = 25 }) {
    let list = [];
    for (const p of this.payments.values()) {
      if (status && p.status !== status) continue;
      const order = this.orders.get(p.order_id);
      const user = order ? this.users.get(order.user_id) : null;
      if (search) {
        const q = search.toLowerCase();
        const match = p.payment_id.toLowerCase().includes(q) ||
                      p.order_id.toLowerCase().includes(q) ||
                      (user && user.email.toLowerCase().includes(q));
        if (!match) continue;
      }
      list.push({
        id: p.id,
        payment_id: p.payment_id,
        order_id: p.order_id,
        amount_inr: (p.amount_paise || 99900) / 100,
        currency: p.currency || 'INR',
        status: p.status,
        method: p.method || 'upi',
        student_email: user ? user.email : 'Unknown Student',
        student_id: user ? user.id : null,
        created_at: p.created_at
      });
    }
    const total = list.length;
    const offset = (page - 1) * limit;
    return { payments: list.slice(offset, offset + limit), total, page, limit, totalPages: Math.ceil(total / limit) || 1 };
  }

  async getSessions({ page = 1, limit = 25, activeOnly = true }) {
    let list = [];
    for (const s of this.userSessions.values()) {
      if (activeOnly && !s.is_active) continue;
      const u = this.users.get(s.user_id);
      // count active devices for this user
      let userActiveDevices = 0;
      for (const sess of this.userSessions.values()) {
        if (sess.user_id === s.user_id && sess.is_active) userActiveDevices++;
      }
      list.push({
        id: s.id,
        user_id: s.user_id,
        student_email: u ? u.email : 'Unknown',
        student_name: u ? u.full_name : 'Unknown',
        device_info: s.device_info,
        ip_address: s.ip_address,
        is_active: s.is_active,
        created_at: s.created_at,
        last_seen_at: s.last_seen_at,
        revocation_reason: s.revocation_reason,
        user_active_devices_count: userActiveDevices
      });
    }
    const total = list.length;
    const offset = (page - 1) * limit;
    return { sessions: list.slice(offset, offset + limit), total, page, limit, totalPages: Math.ceil(total / limit) || 1 };
  }

  async getAuditLogs({ limit = 50 }) {
    return this.auditLogs.slice(0, limit);
  }
}

const localStore = new LocalDatabaseStore();

// ====================================================================
// Database Service Interface (Delegates to PostgreSQL Pool or localStore)
// ====================================================================
const db = {
  isConfigured: () => !!dbPool,
  pool: dbPool,

  async replaceUserSession({ userId, rawToken, deviceInfo, ipAddress }) {
    if (dbPool) {
      const tokenHash = crypto.createHash('sha256').update(rawToken).digest('hex');
      const res = await dbPool.query(
        'SELECT * FROM public.scale_replace_user_session($1, $2, $3, $4)',
        [userId, tokenHash, deviceInfo, ipAddress]
      );
      return {
        newSessionId: res.rows[0]?.new_session_id,
        revokedSessionId: res.rows[0]?.revoked_session_id
      };
    }
    return localStore.replaceUserSession({ userId, rawToken, deviceInfo, ipAddress });
  },

  async getActiveSessionByToken(rawToken) {
    if (!rawToken) return null;
    const tokenHash = crypto.createHash('sha256').update(rawToken).digest('hex');

    if (dbPool) {
      const res = await dbPool.query(
        'SELECT * FROM public.scale_user_sessions WHERE token_hash = $1',
        [tokenHash]
      );
      if (res.rows.length === 0) return null;
      const session = res.rows[0];
      if (session.is_active) {
        await dbPool.query(
          'UPDATE public.scale_user_sessions SET last_seen_at = now() WHERE id = $1',
          [session.id]
        );
        return { ...session, is_valid: true };
      }
      return { ...session, is_valid: false, reason: session.revocation_reason || 'REVOKED' };
    }
    return localStore.getActiveSessionByToken(rawToken);
  },

  async revokeSessionByToken(rawToken, reason = 'USER_LOGOUT') {
    if (!rawToken) return false;
    const tokenHash = crypto.createHash('sha256').update(rawToken).digest('hex');

    if (dbPool) {
      const res = await dbPool.query(
        'UPDATE public.scale_user_sessions SET is_active = false, revoked_at = now(), revocation_reason = $1 WHERE token_hash = $2 AND is_active = true',
        [reason, tokenHash]
      );
      return res.rowCount > 0;
    }
    return localStore.revokeSessionByToken(rawToken, reason);
  },

  async revokeSessionById(sessionId, reason = 'ADMIN_REVOKED') {
    if (dbPool) {
      const res = await dbPool.query(
        'UPDATE public.scale_user_sessions SET is_active = false, revoked_at = now(), revocation_reason = $1 WHERE id = $2 AND is_active = true',
        [reason, sessionId]
      );
      return res.rowCount > 0;
    }
    const session = localStore.userSessions.get(sessionId);
    if (session && session.is_active) {
      session.is_active = false;
      session.revoked_at = new Date().toISOString();
      session.revocation_reason = reason;
      return true;
    }
    return false;
  },

  async revokeAllUserSessions(userId, reason = 'PASSWORD_CHANGED') {
    if (dbPool) {
      const res = await dbPool.query(
        'SELECT public.scale_revoke_all_user_sessions($1, $2) as count',
        [userId, reason]
      );
      return res.rows[0]?.count || 0;
    }
    return localStore.revokeAllUserSessions(userId, reason);
  },

  async createOrder({ userId, orderId, amountPaise, currency = 'INR', productCode }) {
    if (dbPool) {
      const res = await dbPool.query(
        `INSERT INTO public.scale_orders (user_id, order_id, amount_paise, currency, product_code)
         VALUES ($1, $2, $3, $4, $5)
         RETURNING *`,
        [userId, orderId, amountPaise, currency, productCode]
      );
      return res.rows[0];
    }
    return localStore.createOrder({ userId, orderId, amountPaise, currency, productCode });
  },

  async getOrderByOrderId(orderId) {
    if (dbPool) {
      const res = await dbPool.query(
        'SELECT * FROM public.scale_orders WHERE order_id = $1',
        [orderId]
      );
      return res.rows[0] || null;
    }
    return localStore.getOrderByOrderId(orderId);
  },

  async hasActiveEntitlement(userId, productCode) {
    if (dbPool) {
      const res = await dbPool.query(
        'SELECT id FROM public.scale_user_entitlements WHERE user_id = $1 AND product_code = $2 AND status = $3',
        [userId, productCode, 'active']
      );
      return res.rows.length > 0;
    }
    return localStore.hasActiveEntitlement(userId, productCode);
  },

  async activateEntitlementIdempotent(params) {
    if (dbPool) {
      await dbPool.query(
        'SELECT public.scale_activate_entitlement_idempotent($1, $2, $3, $4, $5, $6, $7, $8)',
        [
          params.userId,
          params.orderId,
          params.paymentId,
          params.amountPaise,
          params.currency || 'INR',
          params.method || 'unknown',
          params.signature || null,
          JSON.stringify(params.rawPayload || {})
        ]
      );
      return true;
    }
    return localStore.activateEntitlementIdempotent(params);
  },

  async registerUser({ email, password, fullName, role = 'STUDENT', targetExamination }) {
    const passwordHash = crypto.createHash('sha256').update(password).digest('hex');

    if (dbPool) {
      try {
        const res = await dbPool.query(
          `INSERT INTO public.scale_users (email, password_hash, full_name, role, target_examination)
           VALUES ($1, $2, $3, $4, $5)
           RETURNING id, email, full_name, role, target_examination, account_status, profile_completion_status`,
          [email.toLowerCase(), passwordHash, fullName || 'NEET Aspirant', role, targetExamination || null]
        );
        return res.rows[0];
      } catch (err) {
        if (err.code === '23505') {
          const error = new Error('User already exists');
          error.code = 'USER_EXISTS';
          throw error;
        }
        throw err;
      }
    }
    return localStore.registerUser({ email, password, fullName, role });
  },

  async authenticateUser({ email, password }) {
    const passwordHash = crypto.createHash('sha256').update(password).digest('hex');

    if (dbPool) {
      const res = await dbPool.query(
        'SELECT id, email, full_name, role, is_suspended, suspension_reason, password_hash FROM public.scale_users WHERE lower(email) = lower($1) AND deleted_at IS NULL',
        [email]
      );
      if (res.rows.length === 0 || res.rows[0].password_hash !== passwordHash) {
        const err = new Error('Invalid credentials');
        err.code = 'INVALID_CREDENTIALS';
        throw err;
      }
      const { password_hash, ...userWithoutHash } = res.rows[0];
      return userWithoutHash;
    }
    return localStore.authenticateUser({ email, password });
  },

  async getUserById(userId) {
    if (dbPool) {
      const res = await dbPool.query(
        'SELECT id, email, full_name, role, is_suspended, suspension_reason, created_at, target_examination, account_status, profile_completion_status FROM public.scale_users WHERE id = $1 AND deleted_at IS NULL',
        [userId]
      );
      return res.rows[0] || null;
    }
    return localStore.getUserById(userId);
  },

  async getUserByEmail(email) {
    if (!email) return null;
    if (dbPool) {
      const res = await dbPool.query(
        'SELECT id, email, full_name, role, is_suspended, suspension_reason, created_at, target_examination, account_status, profile_completion_status FROM public.scale_users WHERE lower(email) = lower($1) AND deleted_at IS NULL',
        [email.trim()]
      );
      return res.rows[0] || null;
    }
    return localStore.getUserByEmail(email);
  },

  async deleteAccount(userId) {
    if (dbPool) {
      await dbPool.query(
        'UPDATE public.scale_users SET deleted_at = now(), email = $1 WHERE id = $2',
        [`deleted_${userId.slice(0, 8)}@deleted.scaleseries.com`, userId]
      );
      await this.revokeAllUserSessions(userId, 'ACCOUNT_DELETED');
      return true;
    }
    return localStore.deleteAccount(userId);
  },

  // ------------------------------------------------------------------
  // ADMIN DASHBOARD METHODS
  // ------------------------------------------------------------------
  async getDashboardOverview() {
    if (dbPool) {
      const [studentsRes, paymentsRes, sessionsRes, entitlementsRes] = await Promise.all([
        dbPool.query(`
          SELECT 
            count(*) as total_students,
            count(*) FILTER (WHERE is_suspended = true) as suspended_students,
            count(*) FILTER (WHERE is_suspended = false) as active_students,
            count(*) FILTER (WHERE created_at >= date_trunc('day', now())) as registrations_today,
            count(*) FILTER (WHERE created_at >= date_trunc('month', now())) as registrations_month
          FROM public.scale_users
          WHERE role = 'STUDENT' AND deleted_at IS NULL;
        `),
        dbPool.query(`
          SELECT 
            count(*) FILTER (WHERE status = 'captured') as total_payments,
            coalesce(sum(amount_paise) FILTER (WHERE status = 'captured'), 0) as total_revenue_paise,
            coalesce(sum(amount_paise) FILTER (WHERE status = 'captured' AND created_at >= date_trunc('day', now())), 0) as today_revenue_paise,
            coalesce(sum(amount_paise) FILTER (WHERE status = 'captured' AND created_at >= date_trunc('month', now())), 0) as month_revenue_paise
          FROM public.scale_payments;
        `),
        dbPool.query(`
          SELECT count(*) as active_sessions 
          FROM public.scale_user_sessions 
          WHERE is_active = true;
        `),
        dbPool.query(`
          SELECT count(DISTINCT user_id) as paid_students 
          FROM public.scale_user_entitlements 
          WHERE status = 'active';
        `)
      ]);

      const st = studentsRes.rows[0] || {};
      const pm = paymentsRes.rows[0] || {};
      const se = sessionsRes.rows[0] || {};
      const en = entitlementsRes.rows[0] || {};

      return {
        totalStudents: parseInt(st.total_students || 0, 10),
        newRegistrationsToday: parseInt(st.registrations_today || 0, 10),
        registrationsThisMonth: parseInt(st.registrations_month || 0, 10),
        activeAccounts: parseInt(st.active_students || 0, 10),
        suspendedAccounts: parseInt(st.suspended_students || 0, 10),
        totalSuccessfulPayments: parseInt(pm.total_payments || 0, 10),
        totalRevenueINR: parseFloat(pm.total_revenue_paise || 0) / 100,
        todayRevenueINR: parseFloat(pm.today_revenue_paise || 0) / 100,
        monthlyRevenueINR: parseFloat(pm.month_revenue_paise || 0) / 100,
        activeSessions: parseInt(se.active_sessions || 0, 10),
        paidStudents: parseInt(en.paid_students || 0, 10)
      };
    }
    return localStore.getDashboardOverview();
  },

  async getStudents({ search = '', filterStatus = '', filterPaid = '', page = 1, limit = 25 }) {
    if (dbPool) {
      const offset = (page - 1) * limit;
      let conditions = ["u.role = 'STUDENT'", "u.deleted_at IS NULL"];
      let params = [];

      if (search) {
        params.push(`%${search}%`);
        conditions.push(`(u.email ILIKE $${params.length} OR u.full_name ILIKE $${params.length} OR u.id::text ILIKE $${params.length})`);
      }
      if (filterStatus === 'ACTIVE') {
        conditions.push("(u.is_suspended = false AND (u.account_status IS NULL OR u.account_status != 'SUSPENDED'))");
      } else if (filterStatus === 'SUSPENDED') {
        conditions.push("(u.is_suspended = true OR u.account_status = 'SUSPENDED')");
      }
      if (filterPaid === 'PAID') {
        conditions.push("e.id IS NOT NULL AND e.status = 'active'");
      } else if (filterPaid === 'FREE') {
        conditions.push("(e.id IS NULL OR e.status != 'active')");
      }

      const whereClause = conditions.length ? 'WHERE ' + conditions.join(' AND ') : '';

      const countQuery = `
        SELECT count(DISTINCT u.id) as total
        FROM public.scale_users u
        LEFT JOIN public.scale_user_entitlements e 
          ON u.id = e.user_id AND e.product_code = 'SCALE_NEET_60_MOCKS'
        ${whereClause};
      `;
      const countRes = await dbPool.query(countQuery, params);
      const total = parseInt(countRes.rows[0]?.total || 0, 10);

      params.push(limit);
      const limitParam = `$${params.length}`;
      params.push(offset);
      const offsetParam = `$${params.length}`;

      const dataQuery = `
        SELECT 
          u.id, 
          u.email, 
          u.full_name, 
          u.phone, 
          u.is_suspended, 
          u.account_status,
          u.suspension_reason, 
          u.created_at,
          coalesce(max(s.last_seen_at), u.created_at) as last_login,
          bool_or(s.is_active) as has_active_session,
          count(s.id) FILTER (WHERE s.is_active = true) as active_devices_count,
          (e.id IS NOT NULL AND e.status = 'active') as is_paid,
          e.source_type as entitlement_source
        FROM public.scale_users u
        LEFT JOIN public.scale_user_sessions s ON u.id = s.user_id
        LEFT JOIN public.scale_user_entitlements e 
          ON u.id = e.user_id AND e.product_code = 'SCALE_NEET_60_MOCKS' AND e.status = 'active'
        ${whereClause}
        GROUP BY u.id, e.id, e.status, e.source_type
        ORDER BY u.created_at DESC
        LIMIT ${limitParam} OFFSET ${offsetParam};
      `;
      const dataRes = await dbPool.query(dataQuery, params);

      return {
        students: dataRes.rows,
        total,
        page,
        limit,
        totalPages: Math.ceil(total / limit) || 1
      };
    }
    return localStore.getStudents({ search, filterStatus, filterPaid, page, limit });
  },

  async getStudentProfileDetail(studentId) {
    if (dbPool) {
      const [userRes, sessionsRes, paymentsRes, entitlementsRes, notesRes, suspensionsRes] = await Promise.all([
        dbPool.query('SELECT * FROM public.scale_users WHERE id = $1', [studentId]),
        dbPool.query('SELECT * FROM public.scale_user_sessions WHERE user_id = $1 ORDER BY created_at DESC', [studentId]),
        dbPool.query(`
          SELECT p.*, o.product_code
          FROM public.scale_payments p
          JOIN public.scale_orders o ON p.order_id = o.order_id
          WHERE o.user_id = $1
          ORDER BY p.created_at DESC;
        `, [studentId]),
        dbPool.query('SELECT * FROM public.scale_user_entitlements WHERE user_id = $1', [studentId]),
        dbPool.query('SELECT * FROM public.scale_admin_notes WHERE student_id = $1 ORDER BY created_at DESC', [studentId]),
        dbPool.query('SELECT * FROM public.scale_account_suspensions WHERE user_id = $1 ORDER BY started_at DESC', [studentId])
      ]);

      if (userRes.rows.length === 0) return null;
      return {
        user: userRes.rows[0],
        sessions: sessionsRes.rows,
        payments: paymentsRes.rows,
        entitlements: entitlementsRes.rows,
        notes: notesRes.rows,
        suspensions: suspensionsRes.rows
      };
    }
    const user = await localStore.getUserById(studentId);
    if (!user) return null;
    const isPaid = await localStore.hasActiveEntitlement(studentId, 'SCALE_NEET_60_MOCKS');
    const notes = await localStore.getAdminNotes(studentId);
    return {
      user: { ...user, is_paid: isPaid },
      sessions: Array.from(localStore.userSessions.values()).filter(s => s.user_id === studentId),
      payments: Array.from(localStore.payments.values()),
      entitlements: Array.from(localStore.userEntitlements.values()).filter(e => e.user_id === studentId),
      notes,
      suspensions: []
    };
  },

  async suspendStudent({ studentId, adminId, adminEmail, adminRole, suspensionType = 'TEMPORARY_SUSPENSION', reason, adminNotes = '', expiresAt = null }) {
    if (dbPool) {
      await dbPool.query(
        'SELECT public.scale_suspend_student($1, $2, $3, $4, $5, $6, $7, $8)',
        [studentId, adminId, adminEmail, adminRole, suspensionType, reason, adminNotes, expiresAt]
      );
      return true;
    }
    return localStore.suspendStudent({ studentId, adminId, adminEmail, adminRole, suspensionType, reason, adminNotes, expiresAt });
  },

  async reactivateStudent({ studentId, adminId, adminEmail, adminRole, reason }) {
    if (dbPool) {
      await dbPool.query(
        'SELECT public.scale_reactivate_student($1, $2, $3, $4, $5)',
        [studentId, adminId, adminEmail, adminRole, reason]
      );
      return true;
    }
    return localStore.reactivateStudent({ studentId, adminId, adminEmail, adminRole, reason });
  },

  async grantComplimentaryAccess({ studentId, adminId, adminEmail, adminRole, productCode = 'SCALE_NEET_60_MOCKS', reason, expiresAt = null }) {
    if (dbPool) {
      await dbPool.query(
        'SELECT public.scale_grant_complimentary_access($1, $2, $3, $4, $5, $6, $7)',
        [studentId, adminId, adminEmail, adminRole, productCode, reason, expiresAt]
      );
      return true;
    }
    return localStore.grantComplimentaryAccess({ studentId, adminId, adminEmail, adminRole, productCode, reason, expiresAt });
  },

  async revokeAccess({ studentId, adminId, adminEmail, adminRole, productCode = 'SCALE_NEET_60_MOCKS', reason }) {
    if (dbPool) {
      await dbPool.query(
        'SELECT public.scale_revoke_access($1, $2, $3, $4, $5, $6)',
        [studentId, adminId, adminEmail, adminRole, productCode, reason]
      );
      return true;
    }
    return localStore.revokeAccess({ studentId, adminId, adminEmail, adminRole, productCode, reason });
  },

  async addAdminNote({ studentId, adminId, adminEmail, note }) {
    if (dbPool) {
      const res = await dbPool.query(
        `INSERT INTO public.scale_admin_notes (student_id, admin_id, admin_email, note)
         VALUES ($1, $2, $3, $4)
         RETURNING *`,
        [studentId, adminId, adminEmail, note]
      );
      return res.rows[0];
    }
    return localStore.addAdminNote({ studentId, adminId, adminEmail, note });
  },

  async getPayments({ search = '', status = '', page = 1, limit = 25 }) {
    if (dbPool) {
      const offset = (page - 1) * limit;
      let conditions = [];
      let params = [];

      if (status) {
        params.push(status);
        conditions.push(`p.status = $${params.length}`);
      }
      if (search) {
        params.push(`%${search}%`);
        conditions.push(`(p.payment_id ILIKE $${params.length} OR p.order_id ILIKE $${params.length} OR u.email ILIKE $${params.length})`);
      }

      const whereClause = conditions.length ? 'WHERE ' + conditions.join(' AND ') : '';

      const countRes = await dbPool.query(`
        SELECT count(*) as total
        FROM public.scale_payments p
        JOIN public.scale_orders o ON p.order_id = o.order_id
        JOIN public.scale_users u ON o.user_id = u.id
        ${whereClause};
      `, params);
      const total = parseInt(countRes.rows[0]?.total || 0, 10);

      params.push(limit);
      const limitParam = `$${params.length}`;
      params.push(offset);
      const offsetParam = `$${params.length}`;

      const dataRes = await dbPool.query(`
        SELECT 
          p.id,
          p.payment_id,
          p.order_id,
          p.amount_paise / 100 as amount_inr,
          p.currency,
          p.status,
          p.method,
          p.created_at,
          u.email as student_email,
          u.id as student_id
        FROM public.scale_payments p
        JOIN public.scale_orders o ON p.order_id = o.order_id
        JOIN public.scale_users u ON o.user_id = u.id
        ${whereClause}
        ORDER BY p.created_at DESC
        LIMIT ${limitParam} OFFSET ${offsetParam};
      `, params);

      return {
        payments: dataRes.rows,
        total,
        page,
        limit,
        totalPages: Math.ceil(total / limit) || 1
      };
    }
    return localStore.getPayments({ search, status, page, limit });
  },

  async getSessions({ page = 1, limit = 25, activeOnly = true }) {
    if (dbPool) {
      const offset = (page - 1) * limit;
      const whereClause = activeOnly ? 'WHERE s.is_active = true' : '';
      const countRes = await dbPool.query(`SELECT count(*) as total FROM public.scale_user_sessions s ${whereClause}`);
      const total = parseInt(countRes.rows[0]?.total || 0, 10);

      const dataRes = await dbPool.query(`
        SELECT 
          s.id,
          s.user_id,
          s.device_info,
          s.ip_address,
          s.is_active,
          s.created_at,
          s.last_seen_at,
          s.revoked_at,
          s.revocation_reason,
          u.email as student_email,
          u.full_name as student_name,
          (SELECT count(*) FROM public.scale_user_sessions active_s WHERE active_s.user_id = s.user_id AND active_s.is_active = true) as user_active_devices_count
        FROM public.scale_user_sessions s
        JOIN public.scale_users u ON s.user_id = u.id
        ${whereClause}
        ORDER BY s.is_active DESC, s.created_at DESC
        LIMIT $1 OFFSET $2;
      `, [limit, offset]);

      return {
        sessions: dataRes.rows,
        total,
        page,
        limit,
        totalPages: Math.ceil(total / limit) || 1
      };
    }
    return localStore.getSessions({ page, limit });
  },

  async getAuditLogs({ limit = 50 }) {
    if (dbPool) {
      const res = await dbPool.query(
        'SELECT * FROM public.scale_admin_audit_logs ORDER BY created_at DESC LIMIT $1',
        [limit]
      );
      return res.rows;
    }
    return localStore.getAuditLogs({ limit });
  },

  async recordAuditLog({ adminId, adminEmail, adminRole, action, targetUserId, targetRecordId, reason, metadata = {}, ipAddress = null }) {
    if (dbPool) {
      await dbPool.query(
        `INSERT INTO public.scale_admin_audit_logs 
         (admin_id, admin_email, admin_role, action, target_user_id, target_record_id, reason, metadata, ip_address)
         VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)`,
        [adminId, adminEmail, adminRole, action, targetUserId, targetRecordId || null, reason || null, JSON.stringify(metadata), ipAddress]
      );
      return true;
    }
    return true;
  },

  async getAdminNotifications({ limit = 30 }) {
    if (dbPool) {
      const res = await dbPool.query(
        'SELECT * FROM public.scale_admin_notifications ORDER BY created_at DESC LIMIT $1',
        [limit]
      );
      return res.rows;
    }
    return localStore.adminNotifications.slice(0, limit);
  },

  // Generic query pass-through for ad-hoc SQL (profile updates, etc.)
  async query(text, params) {
    if (dbPool) {
      return dbPool.query(text, params);
    }
    throw new Error('Database not connected');
  }
};

module.exports = { db, localStore };
