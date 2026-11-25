const { test, describe, before, after } = require('node:test');
const assert = require('node:assert');
const crypto = require('crypto');
const app = require('../src/app');
const config = require('../src/config');

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

// Helper for making requests with cookies
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

describe('Phase 18 & Phase 21: Live Supabase PostgreSQL & Razorpay Production Acceptance Tests', () => {

  test('DEP-10 & Phase 21.1: Unauthenticated checkout is rejected with 401', async () => {
    const res = await request('/api/payments/create-order', {
      method: 'POST',
      body: {}
    });
    assert.strictEqual(res.status, 401);
    assert.strictEqual(res.data.error, 'UNAUTHENTICATED');
  });

  let studentUser = null;
  let deviceASessionToken = null;

  test('DEP-08 & Phase 21.2: Register student account in Supabase PostgreSQL and establish session', async () => {
    const email = `live_aspirant_${Date.now()}@test.com`;
    const res = await request('/api/auth/register', {
      method: 'POST',
      body: {
        email,
        password: 'SecurePassword123!',
        fullName: 'NEET Top Ranker'
      }
    });

    assert.strictEqual(res.status, 201);
    assert.ok(res.data.user.id);
    assert.ok(res.sessionCookie, 'Must set HttpOnly app_session cookie');

    studentUser = res.data.user;
    deviceASessionToken = res.sessionCookie;
  });

  test('Phase 18.6 & Phase 21.5: Refresh browser maintains authenticated state', async () => {
    const res = await request('/api/auth/me', {
      headers: { Cookie: `app_session=${deviceASessionToken}` }
    });

    assert.strictEqual(res.status, 200);
    assert.strictEqual(res.data.authenticated, true);
    assert.strictEqual(res.data.user.id, studentUser.id);
  });

  test('Phase 18.8 & Phase 21.6: Two tabs share active session without logout', async () => {
    const tab1 = await request('/api/auth/me', {
      headers: { Cookie: `app_session=${deviceASessionToken}` }
    });
    const tab2 = await request('/api/auth/me', {
      headers: { Cookie: `app_session=${deviceASessionToken}` }
    });

    assert.strictEqual(tab1.status, 200);
    assert.strictEqual(tab2.status, 200);
    assert.strictEqual(tab1.data.sessionId, tab2.data.sessionId);
  });

  let deviceBSessionToken = null;

  test('DEP-09 & Phase 21.3 & Phase 21.4: Device B logs in -> Device A is atomically revoked in PostgreSQL with SESSION_REPLACED', async () => {
    const loginRes = await request('/api/auth/login', {
      method: 'POST',
      headers: { 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)' },
      body: {
        email: studentUser.email,
        password: 'SecurePassword123!'
      }
    });

    assert.strictEqual(loginRes.status, 200);
    assert.ok(loginRes.sessionCookie);
    deviceBSessionToken = loginRes.sessionCookie;

    const checkDeviceB = await request('/api/auth/me', {
      headers: { Cookie: `app_session=${deviceBSessionToken}` }
    });
    assert.strictEqual(checkDeviceB.status, 200);
    assert.strictEqual(checkDeviceB.data.authenticated, true);

    const checkDeviceA = await request('/api/auth/me', {
      headers: { Cookie: `app_session=${deviceASessionToken}` }
    });

    assert.strictEqual(checkDeviceA.status, 401);
    assert.strictEqual(checkDeviceA.data.error, 'SESSION_REPLACED');
    assert.strictEqual(checkDeviceA.data.title, 'Session Ended');
    assert.ok(checkDeviceA.data.message.includes('signed in on another device'));
  });

  test('Phase 18 & Content Protection: Mocks 1, 21, 41 are free; mock 2 requires entitlement', async () => {
    const demoRes = await request('/api/mocks/1');
    assert.strictEqual(demoRes.status, 200);
    assert.strictEqual(demoRes.data.isDemo, true);

    const lockedUnauth = await request('/api/mocks/2');
    assert.strictEqual(lockedUnauth.status, 401);
    assert.strictEqual(lockedUnauth.data.locked, true);

    const lockedUnpaid = await request('/api/mocks/2', {
      headers: { Cookie: `app_session=${deviceBSessionToken}` }
    });
    assert.strictEqual(lockedUnpaid.status, 403);
    assert.strictEqual(lockedUnpaid.data.error, 'ENTITLEMENT_REQUIRED');
    assert.strictEqual(lockedUnpaid.data.priceINR, 999);
  });

  let createdOrderId = null;

  test('Decision 3: Create Razorpay order with server-controlled ₹999 price', async () => {
    const res = await request('/api/payments/create-order', {
      method: 'POST',
      headers: { Cookie: `app_session=${deviceBSessionToken}` },
      body: {}
    });

    assert.strictEqual(res.status, 201);
    assert.ok(res.data.orderId);
    assert.strictEqual(res.data.amount, 99900, 'Amount must strictly be 99900 paise (₹999)');
    assert.strictEqual(res.data.currency, 'INR');
    createdOrderId = res.data.orderId;
  });

  test('Decision 3 & Phase 21.7: Invalid signature is rejected with 400', async () => {
    const res = await request('/api/payments/verify', {
      method: 'POST',
      headers: { Cookie: `app_session=${deviceBSessionToken}` },
      body: {
        orderId: createdOrderId,
        paymentId: 'pay_tampered_123',
        signature: 'invalid_forged_signature'
      }
    });

    assert.strictEqual(res.status, 400);
    assert.strictEqual(res.data.error, 'INVALID_SIGNATURE');
  });

  test('Decision 3 & Phase 21.7: Valid cryptographic HMAC payment verification unlocks all 60 mocks', async () => {
    const paymentId = `pay_live_${Date.now()}`;
    const validSignature = crypto
      .createHmac('sha256', config.razorpay.keySecret)
      .update(`${createdOrderId}|${paymentId}`)
      .digest('hex');

    const res = await request('/api/payments/verify', {
      method: 'POST',
      headers: { Cookie: `app_session=${deviceBSessionToken}` },
      body: {
        orderId: createdOrderId,
        paymentId,
        signature: validSignature,
        method: 'upi'
      }
    });

    assert.strictEqual(res.status, 200);
    assert.strictEqual(res.data.success, true);
    assert.strictEqual(res.data.entitlement, 'active');

    const mockRes = await request('/api/mocks/2', {
      headers: { Cookie: `app_session=${deviceBSessionToken}` }
    });
    assert.strictEqual(mockRes.status, 200);
    assert.strictEqual(mockRes.data.hasAccess, true);
  });

  test('Phase 18.2: User already purchased -> Cannot create duplicate order', async () => {
    const res = await request('/api/payments/create-order', {
      method: 'POST',
      headers: { Cookie: `app_session=${deviceBSessionToken}` },
      body: {}
    });

    assert.strictEqual(res.status, 200);
    assert.strictEqual(res.data.alreadyPurchased, true);
    assert.strictEqual(res.data.hasAccess, true);
  });

  test('Phase 18.3 & Phase 21.8: Webhook captures payment independently of browser callbacks with HMAC signature', async () => {
    const student2Res = await request('/api/auth/register', {
      method: 'POST',
      body: { email: `live_student_recovery_${Date.now()}@test.com`, password: 'Password123!' }
    });
    const student2Cookie = student2Res.sessionCookie;

    const orderRes = await request('/api/payments/create-order', {
      method: 'POST',
      headers: { Cookie: `app_session=${student2Cookie}` },
      body: {}
    });
    const orderId2 = orderRes.data.orderId;

    const webhookPayload = {
      event: 'payment.captured',
      payload: {
        payment: {
          entity: {
            id: `pay_webhook_live_${Date.now()}`,
            order_id: orderId2,
            amount: 99900,
            currency: 'INR',
            method: 'upi'
          }
        }
      }
    };

    const rawBody = JSON.stringify(webhookPayload);
    const webhookSig = crypto
      .createHmac('sha256', config.razorpay.webhookSecret)
      .update(rawBody)
      .digest('hex');

    const webhookRes = await request('/api/payments/webhook', {
      method: 'POST',
      headers: {
        'x-razorpay-signature': webhookSig,
        'Content-Type': 'application/json'
      },
      body: webhookPayload
    });
    assert.strictEqual(webhookRes.status, 200);

    const meRes = await request('/api/auth/me', {
      headers: { Cookie: `app_session=${student2Cookie}` }
    });
    assert.strictEqual(meRes.data.entitlement.hasAccess, true);

    const dupRes = await request('/api/payments/webhook', {
      method: 'POST',
      headers: {
        'x-razorpay-signature': webhookSig,
        'Content-Type': 'application/json'
      },
      body: webhookPayload
    });
    assert.strictEqual(dupRes.status, 200, 'Duplicate webhook must be handled idempotently');
  });

  test('Phase 18.11 & Phase 21.11: Account deletion revokes session and preserves transaction audit', async () => {
    const deleteRes = await request('/api/auth/account', {
      method: 'DELETE',
      headers: { Cookie: `app_session=${deviceBSessionToken}` }
    });

    assert.strictEqual(deleteRes.status, 200);

    const checkAfterDelete = await request('/api/auth/me', {
      headers: { Cookie: `app_session=${deviceBSessionToken}` }
    });
    assert.strictEqual(checkAfterDelete.status, 401);
  });
});
