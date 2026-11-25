targets = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

upgraded_open_payment_modal = '''    let pendingCheckoutAfterAuth = false;

    function openPaymentModal() {
      // Phase 18 Mandatory Scenario 1: Authentication is mandatory before checkout!
      const user = currentUser || localStorage.getItem('scale_test_user');
      if (!user) {
        pendingCheckoutAfterAuth = true;
        showToast("Authentication is mandatory before checkout. Please sign in or register.", "info");
        openAuthModal();
        return;
      }

      // Phase 18 Mandatory Scenario 2: If user already owns access, do not charge again!
      if (isUserPaid) {
        showToast("You already have active lifetime access to all 60 mock tests!", "info");
        return;
      }

      // 1. If Razorpay Payment Link exists, open it directly in a new tab!
      if (window.RAZORPAY_PAYMENT_URL && window.RAZORPAY_PAYMENT_URL.startsWith('http')) {
        window.open(window.RAZORPAY_PAYMENT_URL, '_blank');
        return;
      }

      // 2. Otherwise open the payment dialog
      document.getElementById('paymentModal').classList.add('active');
      const savedUrl = localStorage.getItem('scale_razorpay_url') || window.RAZORPAY_PAYMENT_URL || '';
      const inp = document.getElementById('rzpConfigInput');
      if (inp && savedUrl) inp.value = savedUrl;
    }

    async function processPayment() {
      // Enforce authentication
      const user = currentUser || localStorage.getItem('scale_test_user');
      if (!user) {
        closePaymentModal();
        openAuthModal();
        return;
      }

      // Priority 1: Direct Razorpay Payment Link (rzp.io or pages.razorpay.com)
      const payLink = window.RAZORPAY_PAYMENT_URL || localStorage.getItem('scale_razorpay_url');
      if (payLink && payLink.startsWith('http')) {
        closePaymentModal();
        window.open(payLink, '_blank');
        return;
      }

      // Priority 2: Server-Side Razorpay Order Creation via Render Backend
      showToast("Creating secure Razorpay order...", "info");
      const orderRes = await apiRequest('/api/payments/create-order', { method: 'POST', body: {} });

      if (orderRes.ok && orderRes.data && orderRes.data.orderId) {
        const orderData = orderRes.data;
        if (orderData.alreadyPurchased) {
          showToast("You already own this test series!", "info");
          closePaymentModal();
          handlePaymentSuccess("ALREADY_PURCHASED");
          return;
        }

        const studentEmail = (currentUser && currentUser.email) ? currentUser.email : localStorage.getItem('scale_test_user') || 'student@scaleseries.com';

        const rzpOptions = {
          "key": orderData.keyId || window.RAZORPAY_KEY_ID,
          "amount": orderData.amount, // 99900 paise = ₹999
          "currency": "INR",
          "name": "Scale Test Series",
          "description": "All-Access Master Pass (60 Full-Length NEET Mocks)",
          "order_id": orderData.orderId,
          "image": "logo.png",
          "handler": async function (response) {
            showToast("Verifying payment with secure server...", "info");
            const verifyRes = await apiRequest('/api/payments/verify', {
              method: 'POST',
              body: {
                orderId: orderData.orderId,
                paymentId: response.razorpay_payment_id,
                signature: response.razorpay_signature
              }
            });

            if (verifyRes.ok && verifyRes.data && verifyRes.data.success) {
              handlePaymentSuccess(response.razorpay_payment_id);
            } else {
              showToast("Payment verification failed. Please contact support.", "error");
            }
          },
          "prefill": {
            "name": "NEET Aspirant",
            "email": studentEmail
          },
          "theme": { "color": "#059669" },
          "modal": {
            "ondismiss": function() { showToast("Payment cancelled."); }
          }
        };

        if (typeof Razorpay !== 'undefined') {
          try {
            const rzp = new Razorpay(rzpOptions);
            rzp.on('payment.failed', function(resp) {
              showToast("Payment error: " + (resp.error ? resp.error.description : "Failed"), "error");
            });
            closePaymentModal();
            rzp.open();
            return;
          } catch (e) {
            console.warn("Razorpay instance error:", e);
          }
        }
      }

      // Priority 3: Fallback configuration prompt or test unlock
      showToast("Please paste your Razorpay Link/Key below or use 'Instant Test Unlock'", "info");
      const inp = document.getElementById('rzpConfigInput');
      if (inp) inp.focus();
    }'''

for target in targets:
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace openPaymentModal and processPayment
    idx_start = content.find('function openPaymentModal()')
    idx_end = content.find('function handlePaymentSuccess(')

    if idx_start != -1 and idx_end != -1:
        content = content[:idx_start] + upgraded_open_payment_modal + '\n\n    ' + content[idx_end:]

    # In handleEmailAuth and handleGoogleSignIn, trigger pendingCheckoutAfterAuth
    resume_auth = '''        if (typeof pendingCheckoutAfterAuth !== 'undefined' && pendingCheckoutAfterAuth) {
          pendingCheckoutAfterAuth = false;
          setTimeout(() => openPaymentModal(), 400);
        }'''
    if 'pendingCheckoutAfterAuth = false;' not in content:
        content = content.replace("updateAuthUI({ email });", "updateAuthUI({ email });\n" + resume_auth)
        content = content.replace("updateAuthUI({ email: 'student@scaleseries.com' });", "updateAuthUI({ email: 'student@scaleseries.com' });\n" + resume_auth)

    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {target}")

