#!/usr/bin/env node
/**
 * fix_frontend.js
 * Applies all required fixes to the 3 identical student-facing HTML files:
 * 1. Removes localStorage session token storage (security violation)
 * 2. Adds checkServerSession() on page load (session persistence fix)
 * 3. Replaces direct Razorpay links with auth-gated Checkout.js flow
 * 4. Fixes handlePaymentSuccess to only work from backend verification
 * 5. Removes Firebase Auth fallback login (bypasses backend)
 */
const fs = require('fs');
const path = require('path');

const FILES = [
  path.resolve(__dirname, '../../mock_tests/index.html'),
  path.resolve(__dirname, '../../mock_tests/neet/index.html'),
  path.resolve(__dirname, '../../neet_mock_tests/index.html'),
];

function applyFixes(html) {
  let result = html;
  let changeCount = 0;

  function replace(label, search, replacement) {
    if (typeof search === 'string') {
      if (result.includes(search)) {
        result = result.split(search).join(replacement);
        changeCount++;
        console.log(`  ✓ ${label}`);
      } else {
        console.log(`  ⚠ ${label} — target not found`);
      }
    } else {
      // RegExp
      const before = result;
      result = result.replace(search, replacement);
      if (result !== before) {
        changeCount++;
        console.log(`  ✓ ${label}`);
      } else {
        console.log(`  ⚠ ${label} — regex did not match`);
      }
    }
  }

  // =========================================================
  // 1. REMOVE localStorage session token storage
  // =========================================================

  // Remove from handleStudentLogin
  replace(
    'Remove localStorage sessionToken in handleStudentLogin',
    /if \(res\.data\.sessionToken\) \{\s*\n?\s*localStorage\.setItem\('scale_student_session_token',\s*res\.data\.sessionToken\);\s*\n?\s*\}/g,
    '// Session token is stored in HttpOnly cookie only (no localStorage)'
  );

  // Remove from handleStudentRegister
  replace(
    'Remove localStorage sessionToken in handleStudentRegister',
    /if \(res\.data\.sessionToken\) \{\s*\n?\s*localStorage\.setItem\('scale_student_session_token',\s*res\.data\.sessionToken\);\s*\n?\s*\}/g,
    '// Session token is stored in HttpOnly cookie only (no localStorage)'
  );

  // Remove from handleGoogleSignIn - the whole ssoRes.data?.sessionToken block
  replace(
    'Remove localStorage sessionToken in handleGoogleSignIn',
    /if \(ssoRes\.ok && ssoRes\.data\?\.sessionToken\) \{\s*\n?\s*localStorage\.setItem\('scale_student_session_token',\s*ssoRes\.data\.sessionToken\);\s*\n?\s*if \(ssoRes\.data\.user\) \{\s*\n?\s*localStorage\.setItem\('scale_student_profile',\s*JSON\.stringify\(ssoRes\.data\.user\)\);\s*\n?\s*localStorage\.setItem\('scale_test_user_name',\s*ssoRes\.data\.user\.fullName\);\s*\n?\s*\}\s*\n?\s*if \(ssoRes\.data\.entitlement\?\.hasAccess\) \{\s*\n?\s*isUserPaid = true;\s*\n?\s*localStorage\.setItem\('scale_test_series_paid',\s*'true'\);\s*\n?\s*\}\s*\n?\s*\}/g,
    `if (ssoRes.ok && ssoRes.data?.success) {
            // Session cookie set by backend via HttpOnly cookie
            if (ssoRes.data.user) {
              localStorage.setItem('scale_student_profile', JSON.stringify(ssoRes.data.user));
              localStorage.setItem('scale_test_user_name', ssoRes.data.user.fullName);
            }
            if (ssoRes.data.entitlement?.hasAccess) {
              isUserPaid = true;
              localStorage.setItem('scale_test_series_paid', 'true');
            }
          }`
  );

  // Remove from handleStudentLogout
  replace(
    'Remove localStorage sessionToken removal in logout',
    "localStorage.removeItem('scale_student_session_token');",
    '// Session cookie cleared by backend'
  );

  // =========================================================
  // 2. FIX handleStudentLogin - remove Firebase fallback, clean up
  // =========================================================

  // Remove the Firebase Auth fallback in handleStudentLogin
  replace(
    'Remove Firebase Auth fallback in handleStudentLogin',
    /\/\/ Fallback to Firebase Auth if backend reports invalid credentials\s*\n?\s*if \(fbAuth\) \{\s*\n?\s*try \{\s*\n?\s*await fbAuth\.signInWithEmailAndPassword\(email, pass\);\s*\n?\s*localStorage\.setItem\('scale_test_user', email\);\s*\n?\s*showToast\('Signed in successfully!'\);\s*\n?\s*closeAuthModal\(\);\s*\n?\s*updateAuthUI\(\{ email \}\);\s*\n?\s*await checkServerSession\(\);\s*\n?\s*return;\s*\n?\s*\} catch \{\}\s*\n?\s*\}/g,
    '// Backend is the sole source of truth for authentication'
  );

  // =========================================================
  // 3. FIX handleGoogleSignIn - remove fake fallback
  // =========================================================

  replace(
    'Remove fake Google SSO fallback',
    /\} else \{\s*\n?\s*\/\/ Fallback: no Firebase\s*\n?\s*localStorage\.setItem\('scale_test_user',\s*'student@scaleseries\.com'\);\s*\n?\s*localStorage\.setItem\('scale_test_user_name',\s*'Student Aspirant'\);\s*\n?\s*showToast\('Signed in successfully!'\);\s*\n?\s*closeAuthModal\(\);\s*\n?\s*updateAuthUI\(\{\s*email:\s*'student@scaleseries\.com',\s*fullName:\s*'Student Aspirant'\s*\}\);\s*\n?\s*\}/g,
    `} else {
          showToast('Google Sign-In is not available. Please sign in with email.', 'error');
        }`
  );

  // =========================================================
  // 4. REPLACE openPaymentModal and processPayment with auth-gated flow
  // =========================================================

  replace(
    'Replace openPaymentModal and processPayment',
    /let pendingCheckoutAfterAuth = false;\s*\n?\s*function openPaymentModal\(\) \{\s*\n?\s*window\.location\.href = "https:\/\/rzp\.io\/rzp\/txETH4p";\s*\n?\s*\}\s*\n?\s*function processPayment\(\) \{\s*\n?\s*window\.location\.href = "https:\/\/rzp\.io\/rzp\/txETH4p";\s*\n?\s*\}/g,
    `let pendingCheckoutAfterAuth = false;

    // Auth-Gated Unlock Flow: Check auth → Create order → Open Razorpay Checkout.js → Verify → Unlock
    async function handleUnlock() {
      // Step 1: Check authentication via backend
      const authRes = await apiRequest('/api/auth/me');
      if (!authRes.ok || !authRes.data?.authenticated) {
        // Not authenticated → show auth modal, preserve unlock intent
        pendingCheckoutAfterAuth = true;
        openAuthModal();
        showToast('Please sign in first to unlock all mock tests.', 'info');
        return;
      }

      // Step 2: Check if already purchased
      if (authRes.data.entitlement?.hasAccess) {
        isUserPaid = true;
        localStorage.setItem('scale_test_series_paid', 'true');
        handlePaymentSuccess('ALREADY_ENTITLED');
        return;
      }

      // Step 3: Create Razorpay order via backend
      const orderBtn = document.querySelector('#examUnlockBtn') || document.querySelector('#navUnlockBtn');
      if (orderBtn) { orderBtn.disabled = true; orderBtn.innerText = 'Creating order...'; }

      const orderRes = await apiRequest('/api/payments/create-order', { method: 'POST' });
      if (!orderRes.ok) {
        showToast(orderRes.data?.message || 'Failed to create payment order. Please try again.', 'error');
        if (orderBtn) { orderBtn.disabled = false; orderBtn.innerText = 'Unlock All 60 Mocks • ₹999'; }
        return;
      }

      if (orderRes.data.alreadyPurchased) {
        isUserPaid = true;
        localStorage.setItem('scale_test_series_paid', 'true');
        handlePaymentSuccess('ALREADY_ENTITLED');
        return;
      }

      // Step 4: Open Razorpay Checkout.js
      const { orderId, amount, currency, keyId, product } = orderRes.data;
      const user = authRes.data.user;

      const rzpOptions = {
        key: keyId,
        amount: amount,
        currency: currency,
        name: 'Scale Test Series',
        description: product?.name || 'All-Access Master Pass — 60 Full-Length NEET Mocks',
        order_id: orderId,
        prefill: {
          email: user.email || '',
          contact: ''
        },
        theme: { color: '#059669' },
        modal: {
          ondismiss: function() {
            showToast('Payment cancelled. You can try again anytime.', 'info');
            if (orderBtn) { orderBtn.disabled = false; orderBtn.innerText = 'Unlock All 60 Mocks • ₹999'; }
          }
        },
        handler: async function(response) {
          // Step 5: Verify payment on backend
          if (orderBtn) { orderBtn.innerText = 'Verifying payment...'; }
          const verifyRes = await apiRequest('/api/payments/verify', {
            method: 'POST',
            body: JSON.stringify({
              orderId: response.razorpay_order_id,
              paymentId: response.razorpay_payment_id,
              signature: response.razorpay_signature
            })
          });

          if (verifyRes.ok && verifyRes.data?.success) {
            // Step 6: Backend verified! Activate entitlement
            handlePaymentSuccess(response.razorpay_payment_id);
          } else {
            showToast('Payment verification failed. If money was deducted, it will be refunded within 5-7 days. Please contact support.', 'error');
            if (orderBtn) { orderBtn.disabled = false; orderBtn.innerText = 'Unlock All 60 Mocks • ₹999'; }
          }
        }
      };

      try {
        const rzp = new Razorpay(rzpOptions);
        rzp.on('payment.failed', function(response) {
          showToast('Payment failed: ' + (response.error?.description || 'Unknown error') + '. Please try again.', 'error');
          if (orderBtn) { orderBtn.disabled = false; orderBtn.innerText = 'Unlock All 60 Mocks • ₹999'; }
        });
        rzp.open();
      } catch (err) {
        console.error('Razorpay Checkout error:', err);
        showToast('Payment gateway error. Please try again.', 'error');
        if (orderBtn) { orderBtn.disabled = false; orderBtn.innerText = 'Unlock All 60 Mocks • ₹999'; }
      }
    }

    // Legacy function aliases for backward compatibility
    function openPaymentModal() { handleUnlock(); }
    function processPayment() { handleUnlock(); }`
  );

  // =========================================================
  // 5. FIX handlePaymentSuccess - driven by backend verification only
  // =========================================================

  replace(
    'Fix handlePaymentSuccess',
    /function handlePaymentSuccess\(txId\) \{\s*\n?\s*isUserPaid = true;\s*\n?\s*localStorage\.setItem\('scale_test_series_paid', 'true'\);\s*\n?\s*localStorage\.setItem\('scale_payment_id', txId\);\s*\n?\s*closePaymentModal\(\);\s*\n?\s*showToast\('Payment Successful! All 60 Mock Papers Unlocked 🎉', 'success'\);/g,
    `function handlePaymentSuccess(txId) {
      isUserPaid = true;
      localStorage.setItem('scale_test_series_paid', 'true');
      if (txId && txId !== 'ALREADY_ENTITLED') {
        localStorage.setItem('scale_payment_id', txId);
      }
      try { closePaymentModal(); } catch(e) {}
      if (txId === 'ALREADY_ENTITLED') {
        showToast('You already have full access to all 60 Mock Tests! ✓', 'success');
      } else {
        showToast('Payment Verified! All 60 Mock Papers Unlocked 🎉', 'success');
      }`
  );

  // =========================================================
  // 6. FIX navUnlockBtn - replace hardcoded Razorpay link
  // =========================================================

  replace(
    'Fix navUnlockBtn in nav',
    /<a href="https:\/\/rzp\.io\/rzp\/txETH4p" class="btn-primary" id="navUnlockBtn" onclick="window\.location\.href='https:\/\/rzp\.io\/rzp\/txETH4p'; return false;"[^>]*>Unlock 60 Mocks &bull; ₹999<\/a>/g,
    `<button class="btn-primary" id="navUnlockBtn" onclick="handleUnlock()" style="display: inline-flex; align-items: center;">Unlock 60 Mocks &bull; ₹999</button>`
  );

  // Fix hero CTA unlock button
  replace(
    'Fix hero CTA unlock button',
    /<a href="https:\/\/rzp\.io\/rzp\/txETH4p" class="btn-primary btn-cta-lg" onclick="window\.location\.href=\\'https:\/\/rzp\.io\/rzp\/txETH4p\\'[^"]*"[^>]*>\s*<svg[^>]*><rect[^>]*><\/rect><path[^>]*><\/path><\/svg>\s*Unlock All 60 Mocks @ &#8377;999 \(Lifetime\)<\/a>/g,
    `<button class="btn-primary btn-cta-lg" onclick="handleUnlock()" style="display: inline-flex; align-items: center; gap: 8px;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          Unlock All 60 Mocks @ &#8377;999 (Lifetime)</button>`
  );

  // Fix payment modal "Pay ₹999" button
  replace(
    'Fix payment modal Pay button',
    /<a href="https:\/\/rzp\.io\/rzp\/txETH4p" class="btn-primary" onclick="window\.location\.href='https:\/\/rzp\.io\/rzp\/txETH4p'; return false;"[^>]*>Pay ₹999 &amp; Unlock All 60 Mocks &rarr;<\/a>/g,
    `<button class="btn-primary" onclick="handleUnlock()" style="width: 100%; justify-content: center; padding: 0.85rem; font-size: 1rem; display: inline-flex; align-items: center;">Pay ₹999 &amp; Unlock All 60 Mocks &rarr;</button>`
  );

  // =========================================================
  // 7. FIX DOMContentLoaded - add checkServerSession() call
  // =========================================================

  replace(
    'Add checkServerSession on DOMContentLoaded',
    /window\.addEventListener\('DOMContentLoaded', \(\) => \{\s*\n?\s*\/\/ Check for Razorpay payment redirect \/ callback/g,
    `window.addEventListener('DOMContentLoaded', async () => {
      // Restore session from HttpOnly cookie on page load
      try { await checkServerSession(); } catch(e) { console.warn('[Session] Cookie restore failed:', e); }

      // Check for Razorpay payment redirect / callback`
  );

  // Fix the Razorpay redirect handler to verify via backend
  replace(
    'Fix Razorpay redirect handler to verify via backend',
    /if \(rzpPayId \|\| rzpStatus === 'paid' \|\| rzpStatus === 'true'\) \{\s*\n?\s*handlePaymentSuccess\(rzpPayId \|\| \('RZP_' \+ Date\.now\(\)\)\);\s*\n?\s*\}/g,
    `if (rzpPayId || rzpStatus === 'paid' || rzpStatus === 'true') {
          // Payment redirect detected — verify entitlement from backend
          const verifyRes = await apiRequest('/api/auth/me');
          if (verifyRes.ok && verifyRes.data?.entitlement?.hasAccess) {
            handlePaymentSuccess(rzpPayId || 'RZP_REDIRECT');
          } else {
            showToast('Payment received! Verifying access — please wait...', 'info');
            // Retry after 3 seconds (webhook may take a moment)
            setTimeout(async () => {
              const retryRes = await apiRequest('/api/auth/me');
              if (retryRes.ok && retryRes.data?.entitlement?.hasAccess) {
                handlePaymentSuccess(rzpPayId || 'RZP_REDIRECT');
              }
            }, 3000);
          }
        }`
  );

  // =========================================================
  // 8. FIX checkServerSession - also handle pending unlock intent
  // =========================================================

  replace(
    'Enhance checkServerSession with pending unlock intent',
    /async function checkServerSession\(\) \{\s*\n?\s*const res = await apiRequest\('\/api\/auth\/me'\);\s*\n?\s*if \(res\.ok && res\.data\.authenticated\) \{\s*\n?\s*currentUser = res\.data\.user;\s*\n?\s*if \(res\.data\.entitlement && res\.data\.entitlement\.hasAccess\) \{\s*\n?\s*isUserPaid = true;\s*\n?\s*localStorage\.setItem\('scale_test_series_paid', 'true'\);\s*\n?\s*\}\s*\n?\s*updateAuthUI\(currentUser\);\s*\n?\s*initRealtimeSessionEvents\(\);\s*\n?\s*\}\s*\n?\s*\}/g,
    `async function checkServerSession() {
      const res = await apiRequest('/api/auth/me');
      if (res.ok && res.data.authenticated) {
        currentUser = res.data.user;
        if (res.data.entitlement && res.data.entitlement.hasAccess) {
          isUserPaid = true;
          localStorage.setItem('scale_test_series_paid', 'true');
        }
        updateAuthUI(currentUser);
        initRealtimeSessionEvents();

        // If user just authenticated and had a pending unlock intent, trigger it
        if (pendingCheckoutAfterAuth) {
          pendingCheckoutAfterAuth = false;
          setTimeout(() => handleUnlock(), 500);
        }
      } else {
        // Not authenticated — clear any stale UI state
        if (!currentUser) {
          localStorage.removeItem('scale_test_series_paid');
          isUserPaid = localStorage.getItem('scale_test_series_paid') === 'true';
        }
      }
    }`
  );

  // =========================================================
  // 9. Remove the "Instant Test Unlock" dev bypass button
  // =========================================================

  replace(
    'Remove Instant Test Unlock dev bypass',
    /<button onclick="handlePaymentSuccess\('DEMO_TEST_' \+ Date\.now\(\)\)"[^>]*>\s*⚡ Instant Test Unlock\s*<\/button>/g,
    `<!-- Dev bypass removed for security -->`
  );

  // =========================================================
  // 10. Remove the Razorpay config section from payment modal
  // =========================================================

  replace(
    'Remove Razorpay config input from payment modal',
    /<button onclick="window\.location\.href='https:\/\/rzp\.io\/rzp\/txETH4p'"[^>]*>Save<\/button>/g,
    `<button onclick="saveCustomRazorpay()" style="background: #0f172a; color: #ffffff; border: none; border-radius: 6px; padding: 0.4rem 0.75rem; font-size: 0.75rem; font-weight: 600; cursor: pointer;">Save</button>`
  );

  console.log(`  Total changes applied: ${changeCount}`);
  return result;
}

// =========================================================
// MAIN
// =========================================================
let success = 0;
for (const filePath of FILES) {
  console.log(`\nProcessing: ${filePath}`);
  if (!fs.existsSync(filePath)) {
    console.log(`  ✗ File not found, skipping`);
    continue;
  }
  const original = fs.readFileSync(filePath, 'utf8');
  const fixed = applyFixes(original);
  if (fixed !== original) {
    fs.writeFileSync(filePath, fixed, 'utf8');
    console.log(`  ✓ File updated successfully`);
    success++;
  } else {
    console.log(`  ⚠ No changes made`);
  }
}
console.log(`\nDone. ${success}/${FILES.length} files updated.`);

