const fs = require('fs');
const path = require('path');

const targetPath = path.resolve(__dirname, '../../mock_tests/index.html');
let content = fs.readFileSync(targetPath, 'utf8');
const isCrlf = content.includes('\r\n');
const normalizeEol = (str) => isCrlf ? str.replace(/\r?\n/g, '\r\n') : str.replace(/\r\n/g, '\n');

function replaceBlock(label, oldStr, newStr) {
  console.log(`Applying: ${label}`);
  const normOld = normalizeEol(oldStr);
  const normNew = normalizeEol(newStr);
  if (!content.includes(normOld)) {
    console.error(`ERROR in ${label}: Old block not found!`);
    console.error('Expected snippet:\n', normOld.slice(0, 120));
    process.exit(1);
  }
  content = content.replace(normOld, normNew);
}

// --------------------------------------------------------------------------
// 1. Content Protection CSS & Watermark CSS & Mobile Navbar Safeguards
// --------------------------------------------------------------------------
replaceBlock(
  '1. Content Protection & Print CSS',
  `    /* Test Examination View Layout */
    #exam-workspace-view {`,
  `    /* Proprietary Examination Content Protection & Deterrents (Phase 5 & 6) */
    .workspace-pane,
    .pane-scroll,
    #dual-workspace,
    #pane-left-content,
    #pane-right-content {
      -webkit-user-select: none !important;
      -moz-user-select: none !important;
      -ms-user-select: none !important;
      user-select: none !important;
      -webkit-touch-callout: none !important;
    }

    .workspace-pane {
      position: relative;
    }

    .content-watermark-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 2;
      opacity: 0.065;
      background-repeat: repeat;
    }

    .protected-blurred {
      filter: blur(12px) grayscale(30%) !important;
      transition: filter 0.12s ease-out !important;
      pointer-events: none !important;
    }

    @media print {
      #exam-workspace-view,
      #dual-workspace,
      .workspace-pane,
      .pane-scroll {
        display: none !important;
      }
      body::before {
        content: "Scale Test Series: Reproduction, distribution, or printing of proprietary examination papers and step-by-step solutions is strictly prohibited under applicable copyright laws.";
        display: block !important;
        padding: 3rem 2rem;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        color: #dc2626;
        text-align: center;
        border: 2px dashed #f87171;
        margin: 3rem auto;
        max-width: 650px;
        border-radius: 12px;
        background: #fef2f2;
      }
    }

    /* Test Examination View Layout */
    #exam-workspace-view {`
);

// --------------------------------------------------------------------------
// 2. Mobile Navbar width safeguards for 320px - 480px viewports
// --------------------------------------------------------------------------
replaceBlock(
  '2. Mobile Navbar 320px - 480px CSS',
  `      .hero-stats-row {
        gap: 0.75rem !important;
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
      }`,
  `      .hero-stats-row {
        gap: 0.75rem !important;
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
      }
    }

    @media (max-width: 480px) {
      .nav-container {
        padding: 0.20rem 0.40rem !important;
        gap: 4px !important;
      }
      .brand-link {
        gap: 4px !important;
      }
      .brand-name {
        font-size: 0.82rem !important;
      }
      .brand-logo-img {
        width: 24px !important;
        height: 24px !important;
      }
      #navUnlockBtn {
        padding: 0.20rem 0.35rem !important;
        font-size: 0.67rem !important;
      }
      #authBtn {
        padding: 0.20rem 0.35rem !important;
        font-size: 0.70rem !important;
      }
      .profile-pill-btn {
        padding: 0.18rem 0.35rem !important;
        gap: 3px !important;
      }
      .profile-name {
        max-width: 60px !important;
        font-size: 0.68rem !important;
      }
    }

    @media (max-width: 360px) {
      .brand-name {
        font-size: 0.78rem !important;
      }
      .brand-logo-img {
        width: 22px !important;
        height: 22px !important;
      }
      #navUnlockBtn {
        font-size: 0.63rem !important;
        padding: 0.18rem 0.30rem !important;
      }
      #authBtn {
        font-size: 0.66rem !important;
        padding: 0.18rem 0.30rem !important;
      }`
);

// --------------------------------------------------------------------------
// 3. Watermark elements inside Left and Right workspace panes
// --------------------------------------------------------------------------
replaceBlock(
  '3. Watermark element Left Pane',
  `          <!-- Left Pane -->
          <div class="workspace-pane" id="pane-left">`,
  `          <!-- Left Pane -->
          <div class="workspace-pane" id="pane-left">
            <div class="content-watermark-overlay" id="pane-left-watermark"></div>`
);

replaceBlock(
  '4. Watermark element Right Pane',
  `          <!-- Right Pane -->
          <div class="workspace-pane" id="pane-right">`,
  `          <!-- Right Pane -->
          <div class="workspace-pane" id="pane-right">
            <div class="content-watermark-overlay" id="pane-right-watermark"></div>`
);

// --------------------------------------------------------------------------
// 5. Auth Modal Forms: Target Student only NEET Aspirant, Show/Hide Password,
//    inline error boxes, and post-registration Success View
// --------------------------------------------------------------------------
const oldAuthModalForms = `        <!-- 1. SIGN IN FORM -->
        <form id="signInForm" onsubmit="handleStudentLogin(event)" style="display: block;">
          <div style="margin-bottom: 0.9rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Email Address</label>
            <input type="email" id="authEmail" class="form-input" placeholder="student@example.com" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
          </div>
          <div style="margin-bottom: 1.25rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Password</label>
            <input type="password" id="authPassword" class="form-input" placeholder="••••••••" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
          </div>
          <button type="submit" id="authSubmitBtn" class="btn-primary" style="width: 100%; justify-content: center; padding: 0.75rem; font-size: 0.95rem; border-radius: 8px;">
            Sign In to Account &rarr;
          </button>
          <div style="text-align: center; margin-top: 1rem; font-size: 0.82rem; color: #64748b;">
            New student? <a onclick="setAuthTab('register')" style="color: #059669; font-weight: 600; cursor: pointer; text-decoration: underline;">Create your profile</a>
          </div>
        </form>

        <!-- 2. CREATE PROFILE / SIGN UP FORM -->
        <form id="signUpForm" onsubmit="handleStudentRegister(event)" style="display: none;">
          <div style="margin-bottom: 0.85rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Full Name</label>
            <input type="text" id="regFullName" class="form-input" placeholder="e.g. Sanket Sharma" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
          </div>
          <div style="margin-bottom: 0.85rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Email Address</label>
            <input type="email" id="regEmail" class="form-input" placeholder="student@example.com" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
          </div>
          <div style="margin-bottom: 0.85rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Password (Min 6 Characters)</label>
            <input type="password" id="regPassword" class="form-input" placeholder="••••••••" minlength="6" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
          </div>
          <div style="margin-bottom: 1.25rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Target Examination</label>
            <select id="regTargetExam" class="form-input" style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; background: #ffffff;">
              <option value="NEET 2026">NEET UG 2026 Aspirant</option>
              <option value="NEET 2027">NEET UG 2027 Aspirant</option>
              <option value="JEE Main 2026">JEE Main 2026 Aspirant</option>
            </select>
          </div>
          <button type="submit" id="regSubmitBtn" class="btn-primary" style="width: 100%; justify-content: center; padding: 0.75rem; font-size: 0.95rem; border-radius: 8px;">
            Create Profile & Sign In &rarr;
          </button>
          <div style="text-align: center; margin-top: 1rem; font-size: 0.82rem; color: #64748b;">
            Already registered? <a onclick="setAuthTab('login')" style="color: #059669; font-weight: 600; cursor: pointer; text-decoration: underline;">Sign In</a>
          </div>
        </form>`;

const newAuthModalForms = `        <!-- 1. SIGN IN FORM -->
        <form id="signInForm" onsubmit="handleStudentLogin(event)" style="display: block;">
          <div style="margin-bottom: 0.9rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Email Address</label>
            <input type="email" id="authEmail" class="form-input" placeholder="student@example.com" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
          </div>
          <div style="margin-bottom: 1.15rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Password</label>
            <div style="position: relative; display: flex; align-items: center;">
              <input type="password" id="authPassword" class="form-input" placeholder="••••••••" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 2.6rem 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
              <button type="button" class="password-toggle-btn" onclick="togglePasswordVisibility('authPassword', this)" aria-label="Show password" title="Show password" style="position: absolute; right: 0.75rem; background: transparent; border: none; cursor: pointer; padding: 4px; display: flex; align-items: center; justify-content: center; color: #64748b;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="eye-icon"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
              </button>
            </div>
          </div>
          <div id="loginErrorMsg" style="display: none; background: #fef2f2; border: 1px solid #fecaca; color: #dc2626; padding: 0.65rem 0.75rem; border-radius: 8px; font-size: 0.84rem; margin-bottom: 1rem; line-height: 1.4; text-align: left;"></div>
          <button type="submit" id="authSubmitBtn" class="btn-primary" style="width: 100%; justify-content: center; padding: 0.75rem; font-size: 0.95rem; border-radius: 8px;">
            Sign In to Account &rarr;
          </button>
          <div style="text-align: center; margin-top: 1rem; font-size: 0.82rem; color: #64748b;">
            New student? <a onclick="setAuthTab('register')" style="color: #059669; font-weight: 600; cursor: pointer; text-decoration: underline;">Create your profile</a>
          </div>
        </form>

        <!-- 2. CREATE PROFILE / SIGN UP FORM -->
        <form id="signUpForm" onsubmit="handleStudentRegister(event)" style="display: none;">
          <div style="margin-bottom: 0.85rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Full Name</label>
            <input type="text" id="regFullName" class="form-input" placeholder="e.g. Sanket Sharma" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
          </div>
          <div style="margin-bottom: 0.85rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Email Address</label>
            <input type="email" id="regEmail" class="form-input" placeholder="student@example.com" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
          </div>
          <div style="margin-bottom: 0.85rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Password (Min 6 Characters)</label>
            <div style="position: relative; display: flex; align-items: center;">
              <input type="password" id="regPassword" class="form-input" placeholder="••••••••" minlength="6" required style="width: 100%; box-sizing: border-box; padding: 0.72rem 2.6rem 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem;">
              <button type="button" class="password-toggle-btn" onclick="togglePasswordVisibility('regPassword', this)" aria-label="Show password" title="Show password" style="position: absolute; right: 0.75rem; background: transparent; border: none; cursor: pointer; padding: 4px; display: flex; align-items: center; justify-content: center; color: #64748b;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="eye-icon"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
              </button>
            </div>
          </div>
          <div style="margin-bottom: 1.15rem; text-align: left;">
            <label style="display: block; font-size: 0.82rem; font-weight: 600; color: #334155; margin-bottom: 0.3rem;">Target Student</label>
            <select id="regTargetExam" class="form-input" style="width: 100%; box-sizing: border-box; padding: 0.72rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; background: #ffffff;">
              <option value="NEET Aspirant" selected>NEET Aspirant</option>
            </select>
          </div>
          <div id="registerErrorMsg" style="display: none; background: #fef2f2; border: 1px solid #fecaca; color: #dc2626; padding: 0.65rem 0.75rem; border-radius: 8px; font-size: 0.84rem; margin-bottom: 1rem; line-height: 1.4; text-align: left;"></div>
          <button type="submit" id="regSubmitBtn" class="btn-primary" style="width: 100%; justify-content: center; padding: 0.75rem; font-size: 0.95rem; border-radius: 8px;">
            Create Profile & Sign In &rarr;
          </button>
          <div style="text-align: center; margin-top: 1rem; font-size: 0.82rem; color: #64748b;">
            Already registered? <a onclick="setAuthTab('login')" style="color: #059669; font-weight: 600; cursor: pointer; text-decoration: underline;">Sign In</a>
          </div>
        </form>

        <!-- 3. SUCCESS SCREEN AFTER REGISTRATION -->
        <div id="authSuccessView" style="display: none; text-align: center; padding: 0.75rem 0.25rem;">
          <div style="width: 56px; height: 56px; margin: 0 auto 1.15rem; background: #ecfdf5; border: 2px solid #a7f3d0; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #059669;">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          </div>
          <h3 style="font-size: 1.30rem; font-weight: 800; color: #0f172a; margin-bottom: 0.45rem;">Account Created Successfully!</h3>
          <p style="font-size: 0.90rem; color: #475569; margin-bottom: 1.25rem; line-height: 1.5;">Your ScaleTestSeries account is ready.</p>
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.85rem 1rem; margin-bottom: 1.5rem; text-align: left;">
            <div style="font-size: 0.72rem; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 0.25rem;">Authenticated Student</div>
            <div id="authSuccessUserName" style="font-size: 0.95rem; font-weight: 700; color: #0f172a;"></div>
            <div id="authSuccessUserEmail" style="font-size: 0.82rem; color: #059669; font-weight: 600;"></div>
          </div>
          <button type="button" class="btn-primary" onclick="proceedToDashboardFromSuccess()" style="width: 100%; justify-content: center; padding: 0.80rem; font-size: 0.95rem; font-weight: 700; border-radius: 8px;">
            Continue to Dashboard &rarr;
          </button>
        </div>`;

replaceBlock('5. Auth Modal Forms with Password Toggle, NEET Aspirant, Error Boxes, and Success View', oldAuthModalForms, newAuthModalForms);

// --------------------------------------------------------------------------
// 6. JavaScript Logic Updates:
//    - Password visibility toggle function
//    - Watermark generator and updater
//    - Content protection and visibilitychange deterrent
//    - Refined login and registration validation & error handlers
//    - Post-registration success view transition & dashboard navigation
// --------------------------------------------------------------------------

// Add helpers right after showToast function
const oldShowToast = `    function showToast(msg, type = 'success') {
      const container = document.getElementById('toastContainer');
      const toast = document.createElement('div');
      toast.className = \`toast \${type}\`;
      toast.innerHTML = msg;
      container.appendChild(toast);
      setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.3s';
        setTimeout(() => toast.remove(), 300);
      }, 4000);
    }`;

const newShowToastWithHelpers = `    function showToast(msg, type = 'success') {
      const container = document.getElementById('toastContainer');
      if (!container) return;
      const toast = document.createElement('div');
      toast.className = \`toast \${type}\`;
      toast.innerHTML = msg;
      container.appendChild(toast);
      setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.3s';
        setTimeout(() => toast.remove(), 300);
      }, 4000);
    }

    // Password Visibility Toggle (Phase 2)
    function togglePasswordVisibility(inputId, btn) {
      const input = document.getElementById(inputId);
      if (!input) return;
      const isPassword = input.type === 'password';
      input.type = isPassword ? 'text' : 'password';
      btn.setAttribute('aria-label', isPassword ? 'Hide password' : 'Show password');
      btn.setAttribute('title', isPassword ? 'Hide password' : 'Show password');
      btn.innerHTML = isPassword
        ? \`<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>\`
        : \`<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>\`;
    }

    // Inline Error Helpers for Auth Forms (Phase 2)
    function showLoginFormError(msg) {
      const el = document.getElementById('loginErrorMsg');
      if (el) {
        el.innerText = msg;
        el.style.display = 'block';
      } else {
        showToast(msg, 'error');
      }
    }

    function clearLoginFormError() {
      const el = document.getElementById('loginErrorMsg');
      if (el) {
        el.innerText = '';
        el.style.display = 'none';
      }
    }

    function showRegisterFormError(msg) {
      const el = document.getElementById('registerErrorMsg');
      if (el) {
        el.innerText = msg;
        el.style.display = 'block';
      } else {
        showToast(msg, 'error');
      }
    }

    function clearRegisterFormError() {
      const el = document.getElementById('registerErrorMsg');
      if (el) {
        el.innerText = '';
        el.style.display = 'none';
      }
    }

    // Dynamic Personalized Watermarks (Phase 6)
    function updateContentWatermarks() {
      const user = currentUser;
      const email = user?.email || localStorage.getItem('scale_test_user') || 'Authorized NEET Student';
      const fullName = user?.fullName || user?.displayName || localStorage.getItem('scale_test_user_name') || 'NEET Aspirant';
      const studentId = user?.id ? user.id.slice(0, 8).toUpperCase() : 'DEMO';

      const watermarkText = \`ScaleTestSeries • \${fullName} • \${email} • ID: \${studentId}\`;
      const svg = \`<svg xmlns="http://www.w3.org/2000/svg" width="420" height="240"><text x="20" y="140" fill="%230f172a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" transform="rotate(-25 210 120)">\${watermarkText}</text></svg>\`;
      const dataUri = \`url("data:image/svg+xml;utf8,\${encodeURIComponent(svg)}")\`;

      const leftWm = document.getElementById('pane-left-watermark');
      const rightWm = document.getElementById('pane-right-watermark');
      if (leftWm) leftWm.style.backgroundImage = dataUri;
      if (rightWm) rightWm.style.backgroundImage = dataUri;
    }

    // Proprietary Content Protection & Screen Capture Deterrents (Phase 5 & 6)
    function initContentProtection() {
      const workspace = document.getElementById('dual-workspace');
      if (workspace) {
        // Prevent copy, cut, and drag operations originating inside protected content
        ['copy', 'cut', 'dragstart'].forEach(evt => {
          workspace.addEventListener(evt, (e) => {
            e.preventDefault();
            if (evt === 'copy' || evt === 'cut') {
              showToast('Content copying is disabled to protect proprietary examination material.', 'info');
            }
          });
        });

        // Prevent right-click context menu within protected examination content
        workspace.addEventListener('contextmenu', (e) => {
          e.preventDefault();
        });
      }

      // Visibility Change Deterrent: Obscure content when document loses visibility
      document.addEventListener('visibilitychange', () => {
        const ws = document.getElementById('dual-workspace');
        if (!ws) return;
        if (document.visibilityState === 'hidden') {
          ws.classList.add('protected-blurred');
        } else {
          ws.classList.remove('protected-blurred');
        }
      });
    }`;

replaceBlock('6. Add Toast & Content Protection Helpers', oldShowToast, newShowToastWithHelpers);

// Update setAuthTab to reset success view and clear errors
const oldSetAuthTab = `function setAuthTab(tab) {
      const isLogin = tab === 'login';
      const tabSignInBtn = document.getElementById('tabSignInBtn');
      const tabSignUpBtn = document.getElementById('tabSignUpBtn');
      const signInForm = document.getElementById('signInForm');
      const signUpForm = document.getElementById('signUpForm');
      const modalTitle = document.getElementById('authModalTitle');
      const subTitle = document.getElementById('authSubtitle');
      const googleBtnText = document.getElementById('googleBtnText');

      if (isLogin) {
        if (tabSignInBtn) {
          tabSignInBtn.style.background = '#ffffff';
          tabSignInBtn.style.color = '#059669';
          tabSignInBtn.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
        }
        if (tabSignUpBtn) {
          tabSignUpBtn.style.background = 'transparent';
          tabSignUpBtn.style.color = '#64748b';
          tabSignUpBtn.style.boxShadow = 'none';
        }
        if (signInForm) signInForm.style.display = 'block';
        if (signUpForm) signUpForm.style.display = 'none';
        if (modalTitle) modalTitle.innerText = 'Student Sign In';
        if (subTitle) subTitle.innerText = 'Sign in to access your mock tests and saved diagnostic progress.';
        if (googleBtnText) googleBtnText.innerText = 'Continue with Google';
      } else {
        if (tabSignUpBtn) {
          tabSignUpBtn.style.background = '#ffffff';
          tabSignUpBtn.style.color = '#059669';
          tabSignUpBtn.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
        }
        if (tabSignInBtn) {
          tabSignInBtn.style.background = 'transparent';
          tabSignInBtn.style.color = '#64748b';
          tabSignInBtn.style.boxShadow = 'none';
        }
        if (signInForm) signInForm.style.display = 'none';
        if (signUpForm) signUpForm.style.display = 'block';
        if (modalTitle) modalTitle.innerText = 'Create Student Profile';
        if (subTitle) subTitle.innerText = 'Create your account to track scores, unlock 60 full mocks, and get AI analytics.';
        if (googleBtnText) googleBtnText.innerText = 'Sign Up with Google';
      }
    }`;

const newSetAuthTab = `    function setAuthTab(tab) {
      clearLoginFormError();
      clearRegisterFormError();
      const isLogin = tab === 'login';
      const tabSignInBtn = document.getElementById('tabSignInBtn');
      const tabSignUpBtn = document.getElementById('tabSignUpBtn');
      const signInForm = document.getElementById('signInForm');
      const signUpForm = document.getElementById('signUpForm');
      const successView = document.getElementById('authSuccessView');
      const modalTitle = document.getElementById('authModalTitle');
      const subTitle = document.getElementById('authSubtitle');
      const googleBtnText = document.getElementById('googleBtnText');
      const googleBtn = document.getElementById('googleSsoBtn');
      const divider = document.querySelector('.auth-divider');

      if (successView) successView.style.display = 'none';
      if (googleBtn) googleBtn.style.display = 'inline-flex';
      if (divider) divider.style.display = 'flex';
      if (tabSignInBtn && tabSignInBtn.parentElement) tabSignInBtn.parentElement.style.display = 'flex';
      if (subTitle) subTitle.style.display = 'block';

      if (isLogin) {
        if (tabSignInBtn) {
          tabSignInBtn.style.background = '#ffffff';
          tabSignInBtn.style.color = '#059669';
          tabSignInBtn.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
        }
        if (tabSignUpBtn) {
          tabSignUpBtn.style.background = 'transparent';
          tabSignUpBtn.style.color = '#64748b';
          tabSignUpBtn.style.boxShadow = 'none';
        }
        if (signInForm) signInForm.style.display = 'block';
        if (signUpForm) signUpForm.style.display = 'none';
        if (modalTitle) modalTitle.innerText = 'Student Sign In';
        if (subTitle) subTitle.innerText = 'Sign in to access your mock tests and saved diagnostic progress.';
        if (googleBtnText) googleBtnText.innerText = 'Continue with Google';
      } else {
        if (tabSignUpBtn) {
          tabSignUpBtn.style.background = '#ffffff';
          tabSignUpBtn.style.color = '#059669';
          tabSignUpBtn.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
        }
        if (tabSignInBtn) {
          tabSignInBtn.style.background = 'transparent';
          tabSignInBtn.style.color = '#64748b';
          tabSignInBtn.style.boxShadow = 'none';
        }
        if (signInForm) signInForm.style.display = 'none';
        if (signUpForm) signUpForm.style.display = 'block';
        if (modalTitle) modalTitle.innerText = 'Create Student Profile';
        if (subTitle) subTitle.innerText = 'Create your account to track scores, unlock 60 full mocks, and get AI analytics.';
        if (googleBtnText) googleBtnText.innerText = 'Sign Up with Google';
      }
    }

    function showAuthSuccessScreen(user) {
      clearLoginFormError();
      clearRegisterFormError();
      const tabSignInBtn = document.getElementById('tabSignInBtn');
      const signInForm = document.getElementById('signInForm');
      const signUpForm = document.getElementById('signUpForm');
      const successView = document.getElementById('authSuccessView');
      const modalTitle = document.getElementById('authModalTitle');
      const subTitle = document.getElementById('authSubtitle');
      const googleBtn = document.getElementById('googleSsoBtn');
      const divider = document.querySelector('.auth-divider');

      if (tabSignInBtn && tabSignInBtn.parentElement) tabSignInBtn.parentElement.style.display = 'none';
      if (signInForm) signInForm.style.display = 'none';
      if (signUpForm) signUpForm.style.display = 'none';
      if (googleBtn) googleBtn.style.display = 'none';
      if (divider) divider.style.display = 'none';
      if (subTitle) subTitle.style.display = 'none';

      if (modalTitle) modalTitle.innerText = 'Welcome to Scale Test Series';
      const nameEl = document.getElementById('authSuccessUserName');
      const emailEl = document.getElementById('authSuccessUserEmail');
      if (nameEl) nameEl.innerText = user.fullName || user.email.split('@')[0];
      if (emailEl) emailEl.innerText = user.email;

      if (successView) successView.style.display = 'block';
    }

    function proceedToDashboardFromSuccess() {
      closeAuthModal();
      showExamWorkspace();
    }`;

replaceBlock('7. Update setAuthTab & Success View Transitions', oldSetAuthTab, newSetAuthTab);

// Replace handleStudentLogin and handleStudentRegister with comprehensive validation
const i1 = content.indexOf('    async function handleStudentLogin(e) {');
const i2 = content.indexOf('        let pendingCheckoutAfterAuth = false;');
const oldAuthHandlers = content.slice(i1, i2);

const newAuthHandlers = `    async function handleStudentLogin(e) {
      e.preventDefault();
      clearLoginFormError();
      const emailInput = document.getElementById('authEmail');
      const passInput = document.getElementById('authPassword');
      const email = emailInput ? emailInput.value.trim() : '';
      const pass = passInput ? passInput.value : '';
      const btn = document.getElementById('authSubmitBtn');

      // Client-side validations with required error messages (Phase 2)
      if (!email) {
        showLoginFormError('Please enter your email address.');
        return;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        showLoginFormError('Please enter a valid email address.');
        return;
      }
      if (!pass) {
        showLoginFormError('Please enter your password.');
        return;
      }

      if (btn) { btn.disabled = true; btn.innerText = 'Signing In...'; }

      try {
        const res = await apiRequest('/api/auth/login', {
          method: 'POST',
          body: JSON.stringify({ email, password: pass })
        });

        if (res.ok && res.data.success) {
          const user = res.data.user;
          currentUser = user;
          localStorage.setItem('scale_test_user', user.email);
          localStorage.setItem('scale_test_user_name', user.fullName || email.split('@')[0]);
          localStorage.setItem('scale_student_profile', JSON.stringify(user));
          if (res.data.entitlement?.hasAccess) {
            isUserPaid = true;
            localStorage.setItem('scale_test_series_paid', 'true');
          }
          showToast(\`Welcome back, \${user.fullName || email}! Active on 1 device.\`, 'success');
          closeAuthModal();
          updateAuthUI(user);
          updatePurchaseUI(isUserPaid);
          updateContentWatermarks();
          await checkServerSession();
          return;
        }

        // Invalid credentials or suspended account error display inside login form
        if (res.status === 401 || res.data?.error === 'INVALID_CREDENTIALS') {
          showLoginFormError('Incorrect email or password. Please check your credentials and try again.');
        } else if (res.status === 403 || res.data?.error === 'ACCOUNT_SUSPENDED') {
          showLoginFormError('Your account is currently suspended. Please contact support.');
        } else {
          showLoginFormError(res.data?.message || 'Unable to establish your session. Please try again.');
        }
      } catch (err) {
        showLoginFormError('Unable to connect. Please try again.');
      } finally {
        if (btn) { btn.disabled = false; btn.innerText = 'Sign In to Account →'; }
      }
    }

    async function handleStudentRegister(e) {
      e.preventDefault();
      clearRegisterFormError();
      const fullName = document.getElementById('regFullName').value.trim();
      const email = document.getElementById('regEmail').value.trim();
      const pass = document.getElementById('regPassword').value;
      const targetExam = 'NEET Aspirant'; // Enforce only NEET Aspirant
      const btn = document.getElementById('regSubmitBtn');

      // Client-side validations (Phase 1 & 2)
      if (!fullName) {
        showRegisterFormError('Please enter your full name.');
        return;
      }
      if (!email) {
        showRegisterFormError('Please enter your email address.');
        return;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        showRegisterFormError('Please enter a valid email address.');
        return;
      }
      if (!pass) {
        showRegisterFormError('Please enter your password.');
        return;
      }
      if (pass.length < 6) {
        showRegisterFormError('Password must be at least 6 characters.');
        return;
      }

      if (btn) { btn.disabled = true; btn.innerText = 'Creating Profile...'; }

      try {
        const res = await apiRequest('/api/auth/register', {
          method: 'POST',
          body: JSON.stringify({ fullName, email, password: pass, targetExamination: targetExam, targetStudent: targetExam })
        });

        if (res.ok && res.data.success) {
          const user = res.data.user;
          currentUser = user;
          localStorage.setItem('scale_test_user', user.email);
          localStorage.setItem('scale_test_user_name', user.fullName || fullName);
          localStorage.setItem('scale_student_profile', JSON.stringify(user));
          updateAuthUI(user);
          updatePurchaseUI(isUserPaid);
          updateContentWatermarks();

          // Phase 1 requirement: Show post-registration success screen with Next Step button
          showAuthSuccessScreen(user);
          await checkServerSession();
          return;
        }

        showRegisterFormError(res.data?.message || 'Registration failed. Email may already be registered.');
      } catch (err) {
        showRegisterFormError('Unable to connect. Please try again.');
      } finally {
        if (btn) { btn.disabled = false; btn.innerText = 'Create Profile & Sign In →'; }
      }
    }
`;

replaceBlock('8. Update Login & Register Handlers', oldAuthHandlers, newAuthHandlers);

// Update updateAuthUI to refresh watermarks
replaceBlock(
  '9. Update updateAuthUI with watermark synchronization',
  `      updatePurchaseUI(isUserPaid);
    }`,
  `      updatePurchaseUI(isUserPaid);
      updateContentWatermarks();
    }`
);

// Update DOMContentLoaded to initialize content protection & watermarks
replaceBlock(
  '10. Initialize Content Protection & Watermarks on DOMContentLoaded',
  `      renderSidebar();
      updateHeaderBadge();
      updatePurchaseUI(isUserPaid);`,
  `      renderSidebar();
      updateHeaderBadge();
      updatePurchaseUI(isUserPaid);
      initContentProtection();
      updateContentWatermarks();`
);

// Save to mock_tests/index.html and copy to other two files
console.log('Saving mock_tests/index.html...');
fs.writeFileSync(targetPath, content, 'utf8');

const target1 = path.resolve(__dirname, '../../mock_tests/neet/index.html');
const target2 = path.resolve(__dirname, '../../neet_mock_tests/index.html');

console.log('Propagating identically to mock_tests/neet/index.html and neet_mock_tests/index.html...');
fs.writeFileSync(target1, content, 'utf8');
fs.writeFileSync(target2, content, 'utf8');

console.log('SUCCESS: All 3 files updated with all improvements!');
