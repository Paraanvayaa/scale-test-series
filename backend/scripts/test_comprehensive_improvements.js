const fs = require('fs');
const path = require('path');
const assert = require('assert');

async function runTests() {
  console.log('====================================================');
  console.log('🧪 RUNNING COMPREHENSIVE IMPROVEMENTS VERIFICATION');
  console.log('====================================================\n');

  const htmlPath = path.resolve(__dirname, '../../mock_tests/index.html');
  const html = fs.readFileSync(htmlPath, 'utf8');

  // Test 1: Target Student option in registration
  console.log('TEST 1: Checking Target Student in Registration HTML...');
  assert(html.includes('<option value="NEET Aspirant" selected>NEET Aspirant</option>'), 'NEET Aspirant option must be present and selected');
  assert(!html.includes('JEE Main'), 'JEE Main option must be completely removed');
  assert(!html.includes('value="NEET 2026"'), 'Old NEET 2026 option value must be removed');
  assert(!html.includes('value="NEET 2027"'), 'Old NEET 2027 option value must be removed');
  assert(html.includes('<label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Target Student</label>'), 'Target Student label must be present');
  console.log('✅ TEST 1 PASSED: Only "NEET Aspirant" is available in Target Student registration.\n');

  // Test 2: Show Password / Hide Password
  console.log('TEST 2: Checking Password Visibility Toggle...');
  assert(html.includes("togglePasswordVisibility('authPassword', this)"), 'Login password toggle button present');
  assert(html.includes("togglePasswordVisibility('regPassword', this)"), 'Registration password toggle button present');
  assert(html.includes('function togglePasswordVisibility(inputId, btn)'), 'togglePasswordVisibility function defined');
  console.log('✅ TEST 2 PASSED: Show/Hide Password buttons and toggle handler configured.\n');

  // Test 3: Success Screen after Account Creation
  console.log('TEST 3: Checking Post-Registration Success View...');
  assert(html.includes('id="authSuccessView"'), 'authSuccessView element must exist');
  assert(html.includes('Account Created Successfully!'), 'Success heading present');
  assert(html.includes('Your ScaleTestSeries account is ready.'), 'Success description present');
  assert(html.includes('Continue to Dashboard &rarr;'), 'Primary next-step button present');
  assert(html.includes('proceedToDashboardFromSuccess()'), 'proceedToDashboardFromSuccess function wired');
  assert(html.includes('function showAuthSuccessScreen(user)'), 'showAuthSuccessScreen function defined');
  console.log('✅ TEST 3 PASSED: Post-registration success screen and Next Step button implemented.\n');

  // Test 4: Inline Error Display for Login & Registration
  console.log('TEST 4: Checking Inline Error Containers & Validation Messages...');
  assert(html.includes('id="loginErrorMsg"'), 'loginErrorMsg element must exist');
  assert(html.includes('id="registerErrorMsg"'), 'registerErrorMsg element must exist');
  assert(html.includes('Incorrect email or password. Please check your credentials and try again.'), 'Invalid credentials error text present');
  assert(html.includes('Please enter your email address.'), 'Empty email validation message present');
  assert(html.includes('Please enter your password.'), 'Empty password validation message present');
  assert(html.includes('Please enter a valid email address.'), 'Invalid email validation message present');
  assert(html.includes('Your account is currently suspended. Please contact support.'), 'Suspended account message present');
  console.log('✅ TEST 4 PASSED: Inline error containers and all required validation messages configured.\n');

  // Test 5: Question Paper & Solution Content Protection
  console.log('TEST 5: Checking Content Protection (CSS & JS)...');
  assert(html.includes('-webkit-user-select: none !important;'), 'user-select: none applied in CSS');
  assert(html.includes('.content-watermark-overlay'), 'content-watermark-overlay CSS defined');
  assert(html.includes('id="pane-left-watermark"'), 'Left pane watermark element present');
  assert(html.includes('id="pane-right-watermark"'), 'Right pane watermark element present');
  assert(html.includes('function initContentProtection()'), 'initContentProtection function defined');
  assert(html.includes('function updateContentWatermarks()'), 'updateContentWatermarks function defined');
  assert(html.includes('@media print'), 'Print media query present');
  assert(html.includes('Reproduction, distribution, or printing of proprietary examination papers'), 'Print protection message present');
  assert(html.includes('protected-blurred'), 'Blur deterrent class present');
  console.log('✅ TEST 5 PASSED: Content selection, copy, right-click, print, and blur deterrents implemented.\n');

  // Test 6: Mobile Navbar & Responsive Breakpoints
  console.log('TEST 6: Checking Mobile Navbar Safeguards (320px - 768px)...');
  assert(html.includes('@media (max-width: 480px)'), '480px breakpoint present');
  assert(html.includes('@media (max-width: 360px)'), '360px breakpoint present');
  console.log('✅ TEST 6 PASSED: Mobile navbar breakpoints configured.\n');

  // Test 7: Backend API Verification
  console.log('TEST 7: Testing Backend API Endpoints on http://localhost:4000...');
  
  // 7a: Invalid credentials test
  const loginRes = await fetch('http://localhost:4000/api/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'nonexistent_student_test@example.com', password: 'wrongpassword123' })
  });
  const loginData = await loginRes.json();
  console.log('  Login with invalid credentials status:', loginRes.status);
  console.log('  Login error message:', loginData.message);
  assert.strictEqual(loginRes.status, 401, 'Must return 401 for invalid credentials');
  assert.strictEqual(loginData.message, 'Incorrect email or password. Please check your credentials and try again.');

  // 7b: Target Student invalid value validation
  const testEmail = `student_${Date.now()}@example.com`;
  const invalidTargetRes = await fetch('http://localhost:4000/api/auth/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      fullName: 'Test Student',
      email: testEmail,
      password: 'password123',
      targetStudent: 'INVALID_EXAM_XYZ'
    })
  });
  const invalidTargetData = await invalidTargetRes.json();
  console.log('  Register with invalid target student status:', invalidTargetRes.status);
  console.log('  Invalid target response message:', invalidTargetData.message);
  assert.strictEqual(invalidTargetRes.status, 400, 'Must return 400 for invalid target student');
  assert.strictEqual(invalidTargetData.error, 'INVALID_TARGET_STUDENT');

  // 7c: Successful registration with NEET Aspirant
  const validRegRes = await fetch('http://localhost:4000/api/auth/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      fullName: 'NEET Aspirant Student',
      email: testEmail,
      password: 'password123',
      targetStudent: 'NEET Aspirant'
    })
  });
  const validRegData = await validRegRes.json();
  console.log('  Register with NEET Aspirant status:', validRegRes.status);
  console.log('  User created:', validRegData.user?.email);
  assert.strictEqual(validRegRes.status, 201, 'Must return 201 for valid registration');
  assert(validRegData.success, 'Registration must be successful');
  assert.strictEqual(validRegData.user?.email, testEmail);

  // 7d: Login with newly created user
  const validLoginRes = await fetch('http://localhost:4000/api/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: testEmail, password: 'password123' })
  });
  const validLoginData = await validLoginRes.json();
  console.log('  Login with valid credentials status:', validLoginRes.status);
  assert.strictEqual(validLoginRes.status, 200, 'Must return 200 for valid credentials');
  assert(validLoginData.success, 'Login must succeed');

  console.log('✅ TEST 7 PASSED: Backend API validation, invalid credentials error, and registration fully verified.\n');

  console.log('====================================================');
  console.log('🎉 ALL 7 TEST SUITES PASSED FLAWLESSLY!');
  console.log('====================================================');
}

runTests().catch(err => {
  console.error('❌ TEST FAILED:', err);
  process.exit(1);
});

