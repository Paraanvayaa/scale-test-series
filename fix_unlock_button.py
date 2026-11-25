targets = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

clean_payment_flow = '''    function openPaymentModal() {
      // 1. If Razorpay Payment Link exists, open it directly!
      if (window.RAZORPAY_PAYMENT_URL && window.RAZORPAY_PAYMENT_URL.startsWith('http')) {
        window.open(window.RAZORPAY_PAYMENT_URL, '_blank');
        return;
      }

      // 2. Open the payment dialog reliably
      const modal = document.getElementById('paymentModal');
      if (modal) {
        modal.classList.add('active');
      }

      // Populate saved config input if present
      const savedUrl = localStorage.getItem('scale_razorpay_url') || window.RAZORPAY_PAYMENT_URL || '';
      const inp = document.getElementById('rzpConfigInput');
      if (inp && savedUrl) inp.value = savedUrl;
    }

    function processPayment() {
      // Priority 1: Direct Razorpay Payment Link (rzp.io or pages.razorpay.com)
      const payLink = window.RAZORPAY_PAYMENT_URL || localStorage.getItem('scale_razorpay_url');
      if (payLink && payLink.startsWith('http')) {
        closePaymentModal();
        window.open(payLink, '_blank');
        return;
      }

      const activeKey = window.RAZORPAY_KEY_ID || "rzp_live_Tln6miI6q4JfC1";
      const studentEmail = (currentUser && currentUser.email) ? currentUser.email : (localStorage.getItem('scale_test_user') || 'student@scaleseries.com');

      // Priority 2: Direct Razorpay Checkout with Live Key
      if (typeof Razorpay !== 'undefined') {
        const rzpOptions = {
          "key": activeKey,
          "amount": 99900, // 99900 paise = ₹999 INR
          "currency": "INR",
          "name": "Scale Test Series",
          "description": "All-Access Master Pass (60 Full-Length NEET Mocks)",
          "image": "logo.png",
          "handler": function (response) {
            handlePaymentSuccess(response.razorpay_payment_id || "PAY_" + Date.now());
          },
          "prefill": {
            "name": (currentUser && currentUser.displayName) ? currentUser.displayName : "NEET Aspirant",
            "email": studentEmail,
            "contact": ""
          },
          "notes": {
            "product": "Scale Test Series 60 Mocks",
            "tier": "All-Access Lifetime"
          },
          "theme": {
            "color": "#059669"
          },
          "modal": {
            "ondismiss": function() {
              showToast("Payment window closed.");
            }
          }
        };

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
      } else {
        // Dynamically load Razorpay SDK if not yet loaded
        showToast("Loading Razorpay Checkout...", "info");
        const script = document.createElement('script');
        script.src = "https://checkout.razorpay.com/v1/checkout.js";
        script.onload = () => processPayment();
        document.body.appendChild(script);
        return;
      }

      // Priority 3: Fallback configuration prompt or test unlock
      showToast("Please paste your Razorpay Link/Key below or use 'Instant Test Unlock'", "info");
      const inp = document.getElementById('rzpConfigInput');
      if (inp) inp.focus();
    }'''

for target in targets:
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()

    idx_start = content.find('function openPaymentModal()')
    idx_end = content.find('function handlePaymentSuccess(')

    if idx_start != -1 and idx_end != -1:
        content = content[:idx_start] + clean_payment_flow + '\n\n    ' + content[idx_end:]

    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {target}")

