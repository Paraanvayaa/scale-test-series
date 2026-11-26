const http = require('http');
const fs = require('fs');
const path = require('path');

function request(options, body = null) {
  return new Promise((resolve, reject) => {
    const req = http.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, headers: res.headers, data: JSON.parse(data) });
        } catch (e) {
          resolve({ status: res.statusCode, headers: res.headers, data });
        }
      });
    });
    req.on('error', reject);
    if (body) {
      req.write(typeof body === 'string' ? body : JSON.stringify(body));
    }
    req.end();
  });
}

function parseCookies(res) {
  const raw = res.headers['set-cookie'];
  if (!raw) return '';
  return raw.map(c => c.split(';')[0]).join('; ');
}

async function runTests() {
  console.log('========================================================');
  console.log('STARTING END-TO-END SECURITY & UI VERIFICATION TESTS');
  console.log('========================================================\n');

  // TEST 1: Free Diagnostic Mock 01 Accessible for anonymous users
  console.log('[Test 1] Anonymous GET /api/mocks/1/content (Free Demo)...');
  const mock1Res = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/mocks/1/content',
    method: 'GET'
  });
  if (mock1Res.status === 200 && mock1Res.data.success && mock1Res.data.qpContent) {
    console.log('  PASS: Mock 01 returned full content for demo. Has QP length:', mock1Res.data.qpContent.length);
  } else {
    console.error('  FAIL: Mock 01 failed:', mock1Res.status, mock1Res.data);
    process.exit(1);
  }

  // TEST 2: Paid Mock 02 Rejected with 401 for anonymous users
  console.log('\n[Test 2] Anonymous GET /api/mocks/2/content (Paid Mock)...');
  const mock2Anon = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/mocks/2/content',
    method: 'GET'
  });
  if (mock2Anon.status === 401) {
    console.log('  PASS: Anonymous user correctly rejected with 401 Unauthorized.');
  } else {
    console.error('  FAIL: Mock 02 should return 401, got:', mock2Anon.status, mock2Anon.data);
    process.exit(1);
  }

  // TEST 3: Student Registration with "NEET Aspirant"
  const testStudentEmail = `verify_student_${Date.now()}@scaletest.test`;
  console.log(`\n[Test 3] Registering student: ${testStudentEmail}...`);
  const regRes = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/auth/register',
    method: 'POST',
    headers: { 'Content-Type': 'application/json' }
  }, {
    email: testStudentEmail,
    password: 'SecurePassword123!',
    fullName: 'Test NEET Aspirant',
    targetExamination: 'NEET Aspirant'
  });

  if ((regRes.status !== 200 && regRes.status !== 201) || !regRes.data.success) {
    console.error('  FAIL: Student registration failed:', regRes.status, regRes.data);
    process.exit(1);
  }
  const studentCookie = parseCookies(regRes);
  const studentId = regRes.data.user.id;
  console.log('  PASS: Student registered successfully. ID:', studentId);

  // TEST 4: Student without entitlement accessing Mock 02
  console.log('\n[Test 4] Authenticated Unpaid Student GET /api/mocks/2/content...');
  const mock2Unpaid = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/mocks/2/content',
    method: 'GET',
    headers: { Cookie: studentCookie }
  });
  if (mock2Unpaid.status === 403 && mock2Unpaid.data.error === 'ENTITLEMENT_REQUIRED') {
    console.log('  PASS: Correctly rejected with 403 ENTITLEMENT_REQUIRED.');
  } else {
    console.error('  FAIL: Expected 403 ENTITLEMENT_REQUIRED, got:', mock2Unpaid.status, mock2Unpaid.data);
    process.exit(1);
  }

  // TEST 5: Admin Login
  console.log('\n[Test 5] Logging in as Super Admin...');
  const adminLoginRes = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/admin/auth/login',
    method: 'POST',
    headers: { 'Content-Type': 'application/json' }
  }, {
    email: 'admin@scaletestseries.com',
    password: 'SuperAdmin@Scale2026!'
  });

  if (adminLoginRes.status !== 200 || !adminLoginRes.data.success) {
    console.error('  FAIL: Admin login failed:', adminLoginRes.status, adminLoginRes.data);
    process.exit(1);
  }
  const adminCookie = parseCookies(adminLoginRes);
  console.log('  PASS: Super Admin authenticated successfully.');

  // TEST 6: Admin Grants Complimentary Access
  console.log('\n[Test 6] Admin grants complimentary examination access to student...');
  const grantRes = await request({
    hostname: 'localhost',
    port: 4000,
    path: `/api/admin/students/${studentId}/grant-access`,
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Cookie: adminCookie }
  }, {
    reason: 'Complimentary scholarship pass verified by Super Admin'
  });

  if (grantRes.status !== 200 || !grantRes.data.success) {
    console.error('  FAIL: Grant access failed:', grantRes.status, grantRes.data);
    process.exit(1);
  }
  console.log('  PASS: Admin granted complimentary access successfully.');

  // TEST 7: Student verifies entitlement via /api/auth/me
  console.log('\n[Test 7] Checking student entitlement via GET /api/auth/me...');
  const meRes = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/auth/me',
    method: 'GET',
    headers: { Cookie: studentCookie }
  });
  if (meRes.status === 200 && meRes.data.entitlement?.hasAccess === true) {
    console.log('  PASS: hasAccess is TRUE for student after admin grant.');
  } else {
    console.error('  FAIL: Expected hasAccess: true, got:', meRes.status, meRes.data);
    process.exit(1);
  }

  // TEST 8: Student fetches Mock 02 (Paid Mock) with Entitlement
  console.log('\n[Test 8] Entitled Student GET /api/mocks/2/content...');
  const mock2Paid = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/mocks/2/content',
    method: 'GET',
    headers: { Cookie: studentCookie }
  });
  if (mock2Paid.status === 200 && mock2Paid.data.success && mock2Paid.data.qpContent) {
    console.log('  PASS: Mock 02 loaded successfully!');
    console.log('  PASS: Watermark verified:', mock2Paid.data.watermarkInfo.studentEmail);
  } else {
    console.error('  FAIL: Expected 200 with content, got:', mock2Paid.status, mock2Paid.data);
    process.exit(1);
  }

  // TEST 9: Admin Revokes Examination Access
  console.log('\n[Test 9] Admin revokes student examination access...');
  const revokeRes = await request({
    hostname: 'localhost',
    port: 4000,
    path: `/api/admin/students/${studentId}/revoke-access`,
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Cookie: adminCookie }
  }, {
    reason: 'Trial period expired'
  });
  if (revokeRes.status === 200 && revokeRes.data.success) {
    console.log('  PASS: Admin revoked access successfully.');
  } else {
    console.error('  FAIL: Revoke access failed:', revokeRes.status, revokeRes.data);
    process.exit(1);
  }

  // TEST 10: Student entitlement check reflects revocation
  console.log('\n[Test 10] Checking student entitlement after revocation...');
  const meRevoked = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/auth/me',
    method: 'GET',
    headers: { Cookie: studentCookie }
  });
  if (meRevoked.status === 200 && meRevoked.data.entitlement?.hasAccess === false) {
    console.log('  PASS: hasAccess is FALSE after revocation.');
  } else {
    console.error('  FAIL: Expected hasAccess: false, got:', meRevoked.status, meRevoked.data);
    process.exit(1);
  }

  // TEST 11: Student access to Mock 02 immediately blocked after revocation
  console.log('\n[Test 11] Revoked Student GET /api/mocks/2/content...');
  const mock2Blocked = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/mocks/2/content',
    method: 'GET',
    headers: { Cookie: studentCookie }
  });
  if (mock2Blocked.status === 403 && mock2Blocked.data.error === 'ENTITLEMENT_REQUIRED') {
    console.log('  PASS: Content access immediately blocked with 403 ENTITLEMENT_REQUIRED.');
  } else {
    console.error('  FAIL: Expected 403 ENTITLEMENT_REQUIRED, got:', mock2Blocked.status, mock2Blocked.data);
    process.exit(1);
  }

  // TEST 12: Admin Suspends Student Account
  console.log('\n[Test 12] Admin suspends student account...');
  const suspendRes = await request({
    hostname: 'localhost',
    port: 4000,
    path: `/api/admin/students/${studentId}/suspend`,
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Cookie: adminCookie }
  }, {
    reason: 'Security violation test',
    suspensionType: 'TEMPORARY_SUSPENSION'
  });
  if (suspendRes.status === 200 && suspendRes.data.success) {
    console.log('  PASS: Account suspended successfully.');
  } else {
    console.error('  FAIL: Suspend failed:', suspendRes.status, suspendRes.data);
    process.exit(1);
  }

  // TEST 13: Suspended student blocked even from Free Demo Mock 01
  console.log('\n[Test 13] Suspended student GET /api/mocks/1/content...');
  const mock1Suspended = await request({
    hostname: 'localhost',
    port: 4000,
    path: '/api/mocks/1/content',
    method: 'GET',
    headers: { Cookie: studentCookie }
  });
  if (mock1Suspended.status === 403 && mock1Suspended.data.error === 'ACCOUNT_SUSPENDED') {
    console.log('  PASS: Suspended student blocked from all mock materials.');
  } else {
    console.error('  FAIL: Expected 403 ACCOUNT_SUSPENDED, got:', mock1Suspended.status, mock1Suspended.data);
    process.exit(1);
  }

  // TEST 14: Content Access Audit Logs
  console.log('\n[Test 14] Admin queries /api/admin/content-access-logs...');
  const logsRes = await request({
    hostname: 'localhost',
    port: 4000,
    path: `/api/admin/content-access-logs?userId=${studentId}`,
    method: 'GET',
    headers: { Cookie: adminCookie }
  });
  if (logsRes.status === 200 && logsRes.data.success && logsRes.data.logs.length > 0) {
    console.log(`  PASS: Content access logs verified! Found ${logsRes.data.logs.length} logged events.`);
    console.log('  Sample logged event:', {
      mockId: logsRes.data.logs[0].mock_id,
      granted: logsRes.data.logs[0].access_granted,
      denialReason: logsRes.data.logs[0].denial_reason
    });
  } else {
    console.error('  FAIL: Content access logs failed:', logsRes.status, logsRes.data);
    process.exit(1);
  }

  // TEST 15: Public Files Verification
  console.log('\n[Test 15] Verifying absence of public neet_data.js files...');
  const publicNeetData1 = path.resolve(__dirname, '../../mock_tests/neet_data.js');
  const publicNeetData2 = path.resolve(__dirname, '../../mock_tests/neet/neet_data.js');
  const publicNeetData3 = path.resolve(__dirname, '../../neet_mock_tests/neet_data.js');

  if (!fs.existsSync(publicNeetData1) && !fs.existsSync(publicNeetData2) && !fs.existsSync(publicNeetData3)) {
    console.log('  PASS: Confirmed all public neet_data.js bundles have been deleted.');
  } else {
    console.error('  FAIL: neet_data.js still exists in public web root!');
    process.exit(1);
  }

  // TEST 16: Check files synchronization (Golden Rule)
  console.log('\n[Test 16] Verifying Golden Rule file sync across all 3 HTML directories...');
  const h1 = fs.readFileSync(path.resolve(__dirname, '../../mock_tests/index.html'), 'utf8');
  const h2 = fs.readFileSync(path.resolve(__dirname, '../../mock_tests/neet/index.html'), 'utf8');
  const h3 = fs.readFileSync(path.resolve(__dirname, '../../neet_mock_tests/index.html'), 'utf8');
  if (h1 === h2 && h2 === h3) {
    console.log('  PASS: All 3 index.html files are 100% byte-for-byte identical.');
  } else {
    console.error('  FAIL: HTML files are not identical!');
    process.exit(1);
  }

  console.log('\n========================================================');
  console.log('ALL 16 VERIFICATION TESTS PASSED PERFECTLY!');
  console.log('========================================================');
}

runTests().catch(err => {
  console.error('Test suite error:', err);
  process.exit(1);
});
