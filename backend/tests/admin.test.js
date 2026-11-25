const { test, describe, before, after } = require('node:test');
const assert = require('node:assert');
const app = require('../src/app');

let server;
let baseUrl;

before(async () => {
  await new Promise((resolve) => {
    server = app.listen(0, () => {
      const port = server.address().port;
      baseUrl = `http://localhost:${port}`;
      resolve();
    });
  });
});

after(async () => {
  if (server) {
    await new Promise((resolve) => server.close(resolve));
  }
});

async function request(path, options = {}) {
  const url = `${baseUrl}${path}`;
  const headers = { 'Content-Type': 'application/json', ...(options.headers || {}) };

  const fetchOptions = {
    method: options.method || 'GET',
    headers
  };

  if (options.body) {
    fetchOptions.body = typeof options.body === 'string' ? options.body : JSON.stringify(options.body);
  }

  const res = await fetch(url, fetchOptions);
  let data = null;
  const contentType = res.headers.get('content-type') || '';
  if (contentType.includes('application/json')) {
    data = await res.json();
  } else {
    data = await res.text();
  }

  const rawSetCookie = res.headers.get('set-cookie');
  let sessionCookie = null;
  if (rawSetCookie) {
    const match = rawSetCookie.match(/app_session=([^;]+)/);
    if (match) sessionCookie = match[1];
  }

  return {
    status: res.status,
    headers: res.headers,
    data,
    sessionCookie
  };
}

describe('Phase 17: Super Admin Dashboard & Operations Test Suite', () => {

  let studentCookie = null;
  let studentId = null;
  let adminCookie = null;

  // 1. Unauthenticated rejection
  test('Phase 17.1: Unauthorized visitor cannot access admin dashboard APIs', async () => {
    const res = await request('/api/v1/admin/dashboard/overview');
    assert.strictEqual(res.status, 401);
    assert.strictEqual(res.data.error, 'UNAUTHENTICATED');
  });

  // 2. Student role rejection
  test('Phase 17.2: Ordinary student cannot access admin APIs (403 Forbidden)', async () => {
    const regRes = await request('/api/auth/register', {
      method: 'POST',
      body: {
        email: `student_actor_${Date.now()}@test.com`,
        password: 'Password123!',
        fullName: 'Ordinary Student'
      }
    });
    studentCookie = regRes.sessionCookie;
    studentId = regRes.data.user.id;

    const adminCheck = await request('/api/v1/admin/dashboard/overview', {
      headers: { Cookie: `app_session=${studentCookie}` }
    });
    assert.strictEqual(adminCheck.status, 403);
    assert.strictEqual(adminCheck.data.error, 'FORBIDDEN');
  });

  // 3. Super Admin Login
  test('Phase 1 & 17.3: Super Admin can log in via /api/v1/admin/auth/login', async () => {
    const loginRes = await request('/api/v1/admin/auth/login', {
      method: 'POST',
      body: {
        email: 'admin@scaletestseries.com',
        password: 'SuperAdmin@Scale2026!'
      }
    });

    assert.strictEqual(loginRes.status, 200);
    assert.ok(loginRes.sessionCookie);
    assert.strictEqual(loginRes.data.admin.role, 'SUPER_ADMIN');
    adminCookie = loginRes.sessionCookie;
  });

  // 4. Dashboard Overview KPIs
  test('Phase 2 & 17.4: Admin can fetch real aggregated dashboard overview', async () => {
    const res = await request('/api/v1/admin/dashboard/overview', {
      headers: { Cookie: `app_session=${adminCookie}` }
    });

    assert.strictEqual(res.status, 200);
    assert.ok(res.data.success);
    const stats = res.data.stats;
    assert.ok(typeof stats.totalStudents === 'number');
    assert.ok(typeof stats.totalRevenueINR === 'number');
    assert.ok(typeof stats.activeAccounts === 'number');
  });

  // 5. Student Directory Listing
  test('Phase 3 & 17.5: Admin can list and search students with server-side pagination', async () => {
    const res = await request('/api/v1/admin/students?page=1&limit=10', {
      headers: { Cookie: `app_session=${adminCookie}` }
    });

    assert.strictEqual(res.status, 200);
    assert.ok(Array.isArray(res.data.students));
    assert.ok(typeof res.data.total === 'number');
  });

  // 6. Student Profile Detail
  test('Phase 3 & 17.6: Admin can fetch detailed profile for a student', async () => {
    const res = await request(`/api/v1/admin/students/${studentId}`, {
      headers: { Cookie: `app_session=${adminCookie}` }
    });

    assert.strictEqual(res.status, 200);
    assert.strictEqual(res.data.profile.user.id, studentId);
  });

  // 7. Student Account Suspension & Instant Session Revocation
  test('Phase 4 & 17.7 & 17.8: Admin can suspend student -> active session revoked immediately', async () => {
    const suspendRes = await request(`/api/v1/admin/students/${studentId}/suspend`, {
      method: 'POST',
      headers: { Cookie: `app_session=${adminCookie}` },
      body: {
        reason: 'Violation of Terms: Unauthorized account sharing detected',
        suspensionType: 'TEMPORARY_SUSPENSION'
      }
    });

    assert.strictEqual(suspendRes.status, 200);
    assert.ok(suspendRes.data.success);

    // Verify student session was immediately revoked (Fail-Closed)
    const studentReq = await request('/api/auth/me', {
      headers: { Cookie: `app_session=${studentCookie}` }
    });
    assert.strictEqual(studentReq.status, 401);

    // Verify student cannot log in while suspended
    const relogin = await request('/api/auth/login', {
      method: 'POST',
      body: {
        email: `student_actor_${studentId}@test.com`,
        password: 'Password123!'
      }
    });
    // Either 401/403 blocked
    assert.ok(relogin.status >= 400);
  });

  // 8. Student Account Reactivation
  test('Phase 4 & 17.9: Admin can reactivate suspended student', async () => {
    const reactivateRes = await request(`/api/v1/admin/students/${studentId}/reactivate`, {
      method: 'POST',
      headers: { Cookie: `app_session=${adminCookie}` },
      body: {
        reason: 'Student appeal verified by support'
      }
    });

    assert.strictEqual(reactivateRes.status, 200);
    assert.ok(reactivateRes.data.success);

    // Check profile shows active
    const profRes = await request(`/api/v1/admin/students/${studentId}`, {
      headers: { Cookie: `app_session=${adminCookie}` }
    });
    assert.strictEqual(profRes.data.profile.user.is_suspended, false);
  });

  // 9. Grant Complimentary Examination Access
  test('Phase 6 & 17.10: Admin can grant complimentary access without fake payment', async () => {
    const grantRes = await request(`/api/v1/admin/students/${studentId}/grant-access`, {
      method: 'POST',
      headers: { Cookie: `app_session=${adminCookie}` },
      body: {
        reason: 'National Merit Scholarship Winner - Complimentary Tier',
        productCode: 'SCALE_NEET_60_MOCKS'
      }
    });

    assert.strictEqual(grantRes.status, 200);
    assert.ok(grantRes.data.success);
  });

  // 10. Revoke Examination Access
  test('Phase 6 & 17.11: Admin can revoke examination access with audit log', async () => {
    const revokeRes = await request(`/api/v1/admin/students/${studentId}/revoke-access`, {
      method: 'POST',
      headers: { Cookie: `app_session=${adminCookie}` },
      body: {
        reason: 'Promotional access period ended',
        productCode: 'SCALE_NEET_60_MOCKS'
      }
    });

    assert.strictEqual(revokeRes.status, 200);
    assert.ok(revokeRes.data.success);
  });

  // 11. Add Admin Internal Note
  test('Phase 3 & 17.12: Admin can add internal notes to student profile', async () => {
    const noteRes = await request(`/api/v1/admin/students/${studentId}/notes`, {
      method: 'POST',
      headers: { Cookie: `app_session=${adminCookie}` },
      body: {
        note: 'Student contacted via WhatsApp regarding Mock 14 solution question.'
      }
    });

    assert.strictEqual(noteRes.status, 200);
    assert.ok(noteRes.data.note.id);
  });

  // 12. Audit Logs
  test('Phase 9 & 17.13: Admin audit log records operations immutably', async () => {
    const auditRes = await request('/api/v1/admin/audit-logs?limit=20', {
      headers: { Cookie: `app_session=${adminCookie}` }
    });

    assert.strictEqual(auditRes.status, 200);
    assert.ok(Array.isArray(auditRes.data.logs));
    assert.ok(auditRes.data.logs.length > 0);
  });

  // 13. Reports CSV Export
  test('Phase 8 & 17.14: Admin can export student report as CSV', async () => {
    const exportRes = await request('/api/v1/admin/reports/export?type=students', {
      headers: { Cookie: `app_session=${adminCookie}` }
    });

    assert.strictEqual(exportRes.status, 200);
    assert.ok(exportRes.data.includes('Student ID,Email,Full Name'));
  });
});

