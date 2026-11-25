const fs = require('fs');
const path = require('path');

const filePath = path.resolve(__dirname, '../../mock_tests/index.html');
let content = fs.readFileSync(filePath, 'utf8');
const isCrlf = content.includes('\r\n');
const normalizeEol = (str) => isCrlf ? str.replace(/\r?\n/g, '\r\n') : str.replace(/\r\n/g, '\n');

function replaceBlock(label, oldStr, newStr) {
  console.log(label);
  const normalizedOld = normalizeEol(oldStr);
  const normalizedNew = normalizeEol(newStr);
  if (!content.includes(normalizedOld)) {
    console.error(`ERROR in ${label}: old block not found`);
    console.error('Expected snippet starts with:\n', normalizedOld.slice(0, 100));
    process.exit(1);
  }
  content = content.replace(normalizedOld, normalizedNew);
}

replaceBlock('[1/7] Updating .btn-cta-lg base CSS...',
`    .btn-cta-lg {
      padding: 0.85rem 1.75rem;
      font-size: 1.05rem;
      border-radius: 10px;
    }`,
`    .btn-cta-lg {
      padding: 0.52rem 1.15rem;
      font-size: 0.88rem;
      font-weight: 600;
      border-radius: 8px;
    }`);

replaceBlock('[2/7] Updating mobile nav & hero CSS...',
`      /* Mobile Navigation Header */
      .nav-container {
        padding: 0.5rem 0.75rem !important;
      }
      .brand-logo-img {
        width: 34px !important;
        height: 34px !important;
        border-radius: 8px !important;
      }
      .brand-name {
        font-size: 1.05rem !important;
      }
      .brand-by {
        font-size: 0.62rem !important;
      }
      .nav-menu {
        display: none !important;
      }
      .nav-actions {
        gap: 0.4rem !important;
      }
      .nav-actions .btn-secondary {
        display: none !important;
      }
      .nav-actions .btn-primary {
        padding: 0.4rem 0.75rem !important;
        font-size: 0.78rem !important;
      }

      /* Mobile Landing Hero */
      .hero-section {
        padding: 2.25rem 1rem 1.75rem 1rem !important;
      }
      .hero-title {
        font-size: 1.85rem !important;
        line-height: 1.25 !important;
        margin-bottom: 0.85rem !important;
      }
      .hero-subtitle {
        font-size: 0.95rem !important;
        line-height: 1.55 !important;
        margin-bottom: 1.5rem !important;
      }
      .hero-ctas {
        flex-direction: column !important;
        width: 100% !important;
        gap: 0.75rem !important;
      }
      .hero-ctas button {
        width: 100% !important;
        justify-content: center !important;
      }`,
`      /* Mobile Navigation Header */
      .site-nav {
        border-bottom: 1px solid #e2e8f0 !important;
      }
      .nav-container {
        padding: 0.25rem 0.50rem !important;
        min-height: 40px !important;
        gap: 6px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
      }
      .brand-link {
        gap: 6px !important;
        min-width: 0 !important;
        flex-shrink: 1 !important;
      }
      .brand-logo-img {
        width: 26px !important;
        height: 26px !important;
        border-radius: 6px !important;
        flex-shrink: 0 !important;
      }
      .brand-text {
        min-width: 0 !important;
      }
      .brand-name {
        font-size: 0.88rem !important;
        font-weight: 700 !important;
        white-space: nowrap !important;
        line-height: 1.15 !important;
      }
      .brand-by {
        display: none !important;
      }
      .nav-menu {
        display: none !important;
      }
      .nav-actions {
        gap: 5px !important;
        display: flex !important;
        align-items: center !important;
        flex-shrink: 0 !important;
      }
      .nav-actions .btn-secondary {
        display: none !important;
      }
      #navUnlockBtn {
        padding: 0.25rem 0.45rem !important;
        font-size: 0.70rem !important;
        white-space: nowrap !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        flex-shrink: 0 !important;
      }
      #authBtn {
        padding: 0.25rem 0.45rem !important;
        font-size: 0.72rem !important;
        border-radius: 6px !important;
      }
      .profile-pill-btn {
        padding: 0.20rem 0.40rem !important;
        gap: 4px !important;
        border-radius: 999px !important;
      }
      .profile-avatar {
        width: 20px !important;
        height: 20px !important;
        font-size: 0.62rem !important;
      }
      .profile-name {
        font-size: 0.72rem !important;
        max-width: 75px !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }
      .profile-device-sub {
        display: none !important;
      }
      .profile-caret {
        width: 9px !important;
        height: 9px !important;
      }

      /* Mobile Landing Hero */
      .hero-section {
        padding: 2.25rem 1rem 1.75rem 1rem !important;
      }
      .hero-title {
        font-size: 1.85rem !important;
        line-height: 1.25 !important;
        margin-bottom: 0.85rem !important;
      }
      .hero-subtitle {
        font-size: 0.95rem !important;
        line-height: 1.55 !important;
        margin-bottom: 1.5rem !important;
      }
      .hero-ctas {
        flex-direction: column !important;
        width: 100% !important;
        max-width: 290px !important;
        margin: 0 auto !important;
        gap: 0.45rem !important;
      }
      .hero-ctas button {
        width: 100% !important;
        justify-content: center !important;
        padding: 0.45rem 0.85rem !important;
        font-size: 0.80rem !important;
        border-radius: 7px !important;
      }`);

replaceBlock('[3/7] Updating hero-ctas HTML (smaller, remove lifetime, add IDs)...',
`      <div class="hero-ctas">
        <button class="btn-primary btn-cta-lg" onclick="handleUnlock()" style="display: inline-flex; align-items: center; gap: 8px;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          Unlock All 60 Mocks @ &#8377;999 (Lifetime)</button>
        <button class="btn-secondary btn-cta-lg" onclick="launchDemoTest(1)">
          Try Free Demo Mocks (01, 21, 41) &rarr;
        </button>
      </div>`,
`      <div class="hero-ctas">
        <button class="btn-primary btn-cta-lg" id="heroUnlockBtn" onclick="handleUnlock()" style="display: inline-flex; align-items: center; gap: 6px;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          Unlock All 60 Mocks @ &#8377;999
        </button>
        <button class="btn-primary btn-cta-lg" id="heroAccessBtn" onclick="showExamWorkspace()" style="display: none; align-items: center; gap: 6px; background: #059669;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          Access All 60 Mocks &rarr;
        </button>
        <button class="btn-secondary btn-cta-lg" id="heroDemoBtn" onclick="launchDemoTest(1)">
          Try Free Demo Mocks (01, 21, 41) &rarr;
        </button>
      </div>`);

replaceBlock('[4/7] Updating pricing section unlock button with dynamic state...',
`          <button class="btn-primary" onclick="handleUnlock()" style="width: 100%; justify-content: center; padding: 0.85rem; display: inline-flex; align-items: center;">Unlock All 60 Mocks @ ₹999</button>`,
`          <button class="btn-primary" id="pricingUnlockBtn" onclick="handleUnlock()" style="width: 100%; justify-content: center; padding: 0.75rem; display: inline-flex; align-items: center;">Unlock All 60 Mocks @ ₹999</button>
          <button class="btn-primary" id="pricingPaidBtn" onclick="showExamWorkspace()" style="display: none; width: 100%; justify-content: center; padding: 0.75rem; background: #059669; font-weight: 700; align-items: center; gap: 6px;">✓ All 60 Mocks Unlocked &bull; Go to Workspace &rarr;</button>`);

replaceBlock('[5/7] Adding CSS classes to profile pill template in updateAuthUI...',
`        const profilePillHtml = \`
          <div id="studentProfileContainer" style="position: relative; display: inline-block;">
            <button id="authBtn" type="button" onclick="toggleStudentMenu()" style="display: flex; align-items: center; gap: 8px; background: #ffffff; border: 1.5px solid #a7f3d0; padding: 0.35rem 0.75rem; border-radius: 999px; cursor: pointer; transition: all 0.2s;">
              <div style="width: 24px; height: 24px; border-radius: 50%; background: #059669; color: #ffffff; font-weight: 700; font-size: 0.72rem; display: flex; align-items: center; justify-content: center;">
                \${initials}
              </div>
              <div style="display: flex; flex-direction: column; text-align: left; line-height: 1.1;">
                <span style="font-size: 0.80rem; font-weight: 700; color: #0f172a; max-width: 110px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">\${escapeHtml(fullName)}</span>
                <span style="font-size: 0.65rem; color: #059669; font-weight: 600;">● 1 Active Device</span>
              </div>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2.5"><path d="M6 9l6 6 6-6"></path></svg>
            </button>`,
`        const profilePillHtml = \`
          <div id="studentProfileContainer" style="position: relative; display: inline-block;">
            <button id="authBtn" class="profile-pill-btn" type="button" onclick="toggleStudentMenu()" style="display: flex; align-items: center; gap: 8px; background: #ffffff; border: 1.5px solid #a7f3d0; padding: 0.35rem 0.75rem; border-radius: 999px; cursor: pointer; transition: all 0.2s;">
              <div class="profile-avatar" style="width: 24px; height: 24px; border-radius: 50%; background: #059669; color: #ffffff; font-weight: 700; font-size: 0.72rem; display: flex; align-items: center; justify-content: center;">
                \${initials}
              </div>
              <div class="profile-text-wrap" style="display: flex; flex-direction: column; text-align: left; line-height: 1.1;">
                <span class="profile-name" style="font-size: 0.80rem; font-weight: 700; color: #0f172a; max-width: 110px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">\${escapeHtml(fullName)}</span>
                <span class="profile-device-sub" style="font-size: 0.65rem; color: #059669; font-weight: 600;">● 1 Active Device</span>
              </div>
              <svg class="profile-caret" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2.5"><path d="M6 9l6 6 6-6"></path></svg>
            </button>`);

replaceBlock('[6/7] Adding updatePurchaseUI() and wiring into session and logout handlers...',
`    function updateAuthUI(user) {`,
`    function updatePurchaseUI(isPaid) {
      isUserPaid = !!isPaid;
      const navUnlock = document.getElementById('navUnlockBtn');
      const heroUnlock = document.getElementById('heroUnlockBtn');
      const heroAccess = document.getElementById('heroAccessBtn');
      const pricingUnlock = document.getElementById('pricingUnlockBtn');
      const pricingPaid = document.getElementById('pricingPaidBtn');
      const examUnlock = document.getElementById('examUnlockBtn');

      if (isPaid) {
        if (navUnlock) navUnlock.style.setProperty('display', 'none', 'important');
        if (heroUnlock) heroUnlock.style.setProperty('display', 'none', 'important');
        if (heroAccess) heroAccess.style.display = 'inline-flex';
        if (pricingUnlock) pricingUnlock.style.setProperty('display', 'none', 'important');
        if (pricingPaid) pricingPaid.style.display = 'inline-flex';
        if (examUnlock) examUnlock.style.setProperty('display', 'none', 'important');
      } else {
        if (navUnlock) {
          navUnlock.style.removeProperty('display');
          navUnlock.style.display = 'inline-flex';
        }
        if (heroUnlock) {
          heroUnlock.style.removeProperty('display');
          heroUnlock.style.display = 'inline-flex';
        }
        if (heroAccess) heroAccess.style.display = 'none';
        if (pricingUnlock) {
          pricingUnlock.style.removeProperty('display');
          pricingUnlock.style.display = 'inline-flex';
        }
        if (pricingPaid) pricingPaid.style.display = 'none';
        if (examUnlock) {
          examUnlock.style.removeProperty('display');
          examUnlock.style.display = 'inline-flex';
        }
      }
      if (typeof renderSidebar === 'function') renderSidebar();
    }

    function updateAuthUI(user) {`);

replaceBlock('Rewiring updateAuthUI unlock toggle...',
`      const unlockBtn = document.getElementById('navUnlockBtn');
      const examUnlockBtn = document.getElementById('examUnlockBtn');
      if (isUserPaid) {
        if (unlockBtn) unlockBtn.style.display = 'none';
        if (examUnlockBtn) examUnlockBtn.style.display = 'none';
      } else {
        if (unlockBtn) unlockBtn.style.display = '';
        if (examUnlockBtn) examUnlockBtn.style.display = '';
      }
      if (typeof renderSidebar === 'function') renderSidebar();`,
`      updatePurchaseUI(isUserPaid);`);

replaceBlock('Rewiring checkServerSession authenticated branch...',
`        updateAuthUI(currentUser);
        initRealtimeSessionEvents();`,
`        updateAuthUI(currentUser);
        updatePurchaseUI(isUserPaid);
        initRealtimeSessionEvents();`);

replaceBlock('Rewiring checkServerSession unauthenticated branch...',
`        // Not authenticated — show sign-in UI
        currentUser = null;
        isUserPaid = false;
        localStorage.removeItem('scale_test_series_paid');
        updateAuthUI(null);`,
`        // Not authenticated — show sign-in UI
        currentUser = null;
        isUserPaid = false;
        localStorage.removeItem('scale_test_series_paid');
        updateAuthUI(null);
        updatePurchaseUI(false);`);

replaceBlock('Rewiring handlePaymentSuccess...',
`      const unlockBtn = document.getElementById('examUnlockBtn');
      if (unlockBtn) {
        unlockBtn.innerText = "✓ Full Access Active";
        unlockBtn.style.background = "#059669";
        unlockBtn.disabled = true;
      }
      const navBtn = document.getElementById('navUnlockBtn');
      if (navBtn) {
        navBtn.innerText = "✓ Unlocked";
        navBtn.disabled = true;
      }`,
`      updatePurchaseUI(true);`);

replaceBlock('Rewiring handleStudentLogout...',
`      isUserPaid = false;
      currentUser = null;
      updateAuthUI(null);`,
`      isUserPaid = false;
      currentUser = null;
      updateAuthUI(null);
      updatePurchaseUI(false);`);

replaceBlock('Rewiring DOMContentLoaded...',
`      renderSidebar();
      updateHeaderBadge();
      // updateAuthUI is handled by checkServerSession() above`,
`      renderSidebar();
      updateHeaderBadge();
      updatePurchaseUI(isUserPaid);
      // updateAuthUI is handled by checkServerSession() above`);

console.log('[7/7] Writing changes to mock_tests/index.html, mock_tests/neet/index.html, and neet_mock_tests/index.html...');
fs.writeFileSync(filePath, content, 'utf8');

const target1 = path.resolve(__dirname, '../../mock_tests/neet/index.html');
const target2 = path.resolve(__dirname, '../../neet_mock_tests/index.html');

fs.writeFileSync(target1, content, 'utf8');
fs.writeFileSync(target2, content, 'utf8');

console.log('SUCCESS: All 3 files updated identically and written to disk.');
