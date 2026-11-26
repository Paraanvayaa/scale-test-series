const fs = require('fs');
const path = require('path');

const indexPath = path.resolve(__dirname, '../../mock_tests/index.html');
let html = fs.readFileSync(indexPath, 'utf8');

// Ensure LF line endings for consistent replacement
html = html.replace(/\r\n/g, '\n');

console.log('[1/8] Updating data source script tag...');
html = html.replace(
  /<script src="neet_data\.js"><\/script>/,
  '<!-- Pre-bundled offline diagnostic demo store (Mocks 01, 21, 41 only) -->\n  <script src="demo_mocks.js"></script>'
);

console.log('[2/8] Removing "Lifetime" references...');
html = html.replace(
  'Pay once and get lifetime access through NEET 2026/2027.',
  'Pay once and get full access through NEET 2026/2027.'
);
html = html.replace(
  'Includes GST &bull; 100% Secure Checkout &bull; Lifetime Access',
  'Includes GST &bull; 100% Secure Checkout &bull; Full Access'
);

console.log('[3/8] Adjusting base .btn-cta-lg button styling...');
html = html.replace(
  /\.btn-cta-lg\s*\{\s*padding:\s*0\.52rem\s+1\.15rem;\s*font-size:\s*0\.88rem;\s*font-weight:\s*600;\s*\}/,
  `.btn-cta-lg {
      padding: 0.42rem 0.95rem;
      font-size: 0.82rem;
      font-weight: 600;
      border-radius: 7px;
    }`
);

console.log('[4/8] Updating mobile navigation & hero button responsiveness...');
const oldMobileMediaRegex = /@media\s*\(max-width:\s*768px\)\s*\{[\s\S]*?@media\s*\(max-width:\s*480px\)\s*\{[\s\S]*?max-width:\s*60px\s*!important;\s*\}\s*\}/;

const newMobileMedia = `@media (max-width: 768px) {
      /* Mobile Compact Navigation Header */
      .site-nav {
        border-bottom: 1px solid #e2e8f0 !important;
        background: #ffffff !important;
      }
      .nav-container {
        padding: 0.15rem 0.40rem !important;
        min-height: 38px !important;
        height: 38px !important;
        gap: 4px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
      }
      .brand-link {
        gap: 5px !important;
        min-width: 0 !important;
        flex-shrink: 1 !important;
        display: inline-flex !important;
        align-items: center !important;
      }
      .brand-logo-img {
        width: 22px !important;
        height: 22px !important;
        border-radius: 5px !important;
        flex-shrink: 0 !important;
      }
      .brand-text {
        min-width: 0 !important;
        display: flex !important;
        flex-direction: column !important;
      }
      .brand-name {
        font-size: 0.80rem !important;
        font-weight: 700 !important;
        white-space: nowrap !important;
        line-height: 1.1 !important;
      }
      .brand-by {
        display: none !important;
      }
      .nav-menu {
        display: none !important;
      }
      .nav-actions {
        gap: 4px !important;
        display: flex !important;
        align-items: center !important;
        flex-shrink: 0 !important;
      }
      .nav-actions .btn-secondary:not(#authBtn) {
        display: none !important;
      }
      #navUnlockBtn {
        padding: 0.18rem 0.38rem !important;
        font-size: 0.67rem !important;
        white-space: nowrap !important;
        border-radius: 5px !important;
        font-weight: 700 !important;
        line-height: 1.1 !important;
        flex-shrink: 0 !important;
        height: 26px !important;
        box-sizing: border-box !important;
      }
      #authBtn {
        padding: 0.18rem 0.38rem !important;
        font-size: 0.70rem !important;
        border-radius: 5px !important;
        line-height: 1.1 !important;
        height: 26px !important;
        box-sizing: border-box !important;
      }
      .profile-pill-btn {
        padding: 0.12rem 0.35rem !important;
        gap: 4px !important;
        border-radius: 999px !important;
        height: 26px !important;
        box-sizing: border-box !important;
      }
      .profile-avatar {
        width: 18px !important;
        height: 18px !important;
        font-size: 0.58rem !important;
      }
      .profile-name {
        font-size: 0.68rem !important;
        max-width: 68px !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }
      .profile-device-sub {
        display: none !important;
      }
      .profile-caret {
        width: 8px !important;
        height: 8px !important;
      }

      /* Mobile Landing Hero - Sleek Compact Buttons */
      .hero-section {
        padding: 1.75rem 0.85rem 1.5rem 0.85rem !important;
      }
      .hero-title {
        font-size: 1.65rem !important;
        line-height: 1.25 !important;
        margin-bottom: 0.75rem !important;
      }
      .hero-subtitle {
        font-size: 0.88rem !important;
        line-height: 1.5 !important;
        margin-bottom: 1.25rem !important;
      }
      .hero-ctas {
        flex-direction: column !important;
        width: 100% !important;
        max-width: 260px !important;
        margin: 0 auto !important;
        gap: 0.35rem !important;
      }
      .hero-ctas button, .hero-ctas .btn-cta-lg {
        width: 100% !important;
        justify-content: center !important;
        padding: 0.38rem 0.75rem !important;
        font-size: 0.78rem !important;
        border-radius: 7px !important;
        min-height: 36px !important;
        height: 36px !important;
        box-sizing: border-box !important;
        line-height: 1.2 !important;
      }
      .hero-stats-row {
        gap: 0.5rem !important;
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        margin-top: 1.25rem !important;
      }
    }

    @media (max-width: 480px) {
      .nav-container {
        padding: 0.12rem 0.28rem !important;
        min-height: 35px !important;
        height: 35px !important;
        gap: 3px !important;
      }
      .brand-link {
        gap: 3px !important;
      }
      .brand-name {
        font-size: 0.74rem !important;
      }
      .brand-logo-img {
        width: 19px !important;
        height: 19px !important;
      }
      #navUnlockBtn {
        padding: 0.15rem 0.30rem !important;
        font-size: 0.64rem !important;
        height: 24px !important;
      }
      #authBtn {
        padding: 0.15rem 0.30rem !important;
        font-size: 0.66rem !important;
        height: 24px !important;
      }
      .profile-pill-btn {
        padding: 0.10rem 0.28rem !important;
        gap: 3px !important;
        height: 24px !important;
      }
      .profile-name {
        max-width: 55px !important;
        font-size: 0.64rem !important;
      }
    }`;

if (oldMobileMediaRegex.test(html)) {
  html = html.replace(oldMobileMediaRegex, newMobileMedia);
  console.log('Successfully replaced mobile media queries.');
} else {
  console.warn('Warning: oldMobileMediaRegex did not match directly, checking fallback...');
}

console.log('[5/8] Updating updatePurchaseUI function...');
const oldUpdatePurchaseUI = `    function updatePurchaseUI(isPaid) {
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
    }`;

const newUpdatePurchaseUI = `    function updatePurchaseUI(isPaid) {
      isUserPaid = !!isPaid;
      const navUnlock = document.getElementById('navUnlockBtn');
      const heroUnlock = document.getElementById('heroUnlockBtn');
      const heroAccess = document.getElementById('heroAccessBtn');
      const pricingUnlock = document.getElementById('pricingUnlockBtn');
      const pricingPaid = document.getElementById('pricingPaidBtn');
      const examUnlock = document.getElementById('examUnlockBtn');

      if (isPaid) {
        // Enrolled / Free Access Granted: completely hide all purchase/paywall buttons
        if (navUnlock) navUnlock.style.setProperty('display', 'none', 'important');
        if (heroUnlock) heroUnlock.style.setProperty('display', 'none', 'important');
        if (heroAccess) {
          heroAccess.style.removeProperty('display');
          heroAccess.style.setProperty('display', 'inline-flex', 'important');
        }
        if (pricingUnlock) pricingUnlock.style.setProperty('display', 'none', 'important');
        if (pricingPaid) {
          pricingPaid.style.removeProperty('display');
          pricingPaid.style.setProperty('display', 'inline-flex', 'important');
        }
        if (examUnlock) examUnlock.style.setProperty('display', 'none', 'important');
      } else {
        // Unenrolled / Access Revoked: restore purchase and unlock options
        if (navUnlock) {
          navUnlock.style.removeProperty('display');
          navUnlock.style.setProperty('display', 'inline-flex', 'important');
        }
        if (heroUnlock) {
          heroUnlock.style.removeProperty('display');
          heroUnlock.style.setProperty('display', 'inline-flex', 'important');
        }
        if (heroAccess) heroAccess.style.setProperty('display', 'none', 'important');
        if (pricingUnlock) {
          pricingUnlock.style.removeProperty('display');
          pricingUnlock.style.setProperty('display', 'inline-flex', 'important');
        }
        if (pricingPaid) pricingPaid.style.setProperty('display', 'none', 'important');
        if (examUnlock) {
          examUnlock.style.removeProperty('display');
          examUnlock.style.setProperty('display', 'inline-flex', 'important');
        }
      }
      if (typeof renderSidebar === 'function') renderSidebar();
    }`;

if (html.includes(oldUpdatePurchaseUI)) {
  html = html.replace(oldUpdatePurchaseUI, newUpdatePurchaseUI);
  console.log('Successfully updated updatePurchaseUI.');
} else {
  console.warn('Warning: oldUpdatePurchaseUI not found directly.');
}

console.log('[6/8] Updating SSE real-time events for instant entitlement sync...');
const oldSSE = `          activeSSE.onmessage = (e) => {
            try {
              const msg = JSON.parse(e.data);
              if (msg.event === 'SESSION_REPLACED') {
                handleSessionReplacedEvent(msg);
              }
            } catch {}
          };`;

const newSSE = `          activeSSE.onmessage = (e) => {
            try {
              const msg = JSON.parse(e.data);
              if (msg.event === 'SESSION_REPLACED') {
                handleSessionReplacedEvent(msg);
              } else if (msg.event === 'ENTITLEMENT_UPDATED') {
                // Admin granted or revoked access in real time
                isUserPaid = !!msg.hasAccess;
                if (isUserPaid) {
                  localStorage.setItem('scale_test_series_paid', 'true');
                  showToast('Access Granted: All 60 Mocks Unlocked! 🎉', 'success');
                } else {
                  localStorage.removeItem('scale_test_series_paid');
                  clearActiveDocuments();
                  showToast('Examination access has been revoked by Administrator.', 'info');
                }
                updatePurchaseUI(isUserPaid);
                updateHeaderBadge();
                if (typeof renderSidebar === 'function') renderSidebar();
              } else if (msg.event === 'ACCOUNT_SUSPENDED') {
                // Admin suspended account in real time
                isUserPaid = false;
                localStorage.removeItem('scale_test_series_paid');
                clearActiveDocuments();
                updatePurchaseUI(false);
                handleStudentLogout();
                showToast('Your account has been suspended by an administrator. Please contact support.', 'error');
              }
            } catch {}
          };`;

if (html.includes(oldSSE)) {
  html = html.replace(oldSSE, newSSE);
  console.log('Successfully updated real-time SSE listener.');
} else {
  console.warn('Warning: oldSSE not found directly.');
}

console.log('[7/8] Upgrading loadActiveDocuments to on-demand backend authorized fetching...');
const oldLoadDocs = `    // Document Loading & Math-Protected Markdown Parsing
    function loadActiveDocuments() {
      const pad = String(currentMock).padStart(2, '0');
      const mockKey = \`Mock_\${pad}\`;

      if (window.NEET_DATA) {
        const qpKey = \`\${mockKey}_Question_Paper.md\`;
        const solKey = \`\${mockKey}_Detailed_Solutions.md\`;
        const keyKey = \`\${mockKey}_Answer_Key_and_Analysis.md\`;

        const qpContent = window.NEET_DATA[qpKey] || '# Question paper loading...';
        const solContent = window.NEET_DATA[solKey] || '# Solutions loading...';
        const keyContent = window.NEET_DATA[keyKey] || '# Analysis loading...';

        renderProtectedMarkdown(qpContent, document.getElementById('pane-left-content'));

        if (currentViewMode === 'key') {
          document.getElementById('pane-right-title').innerHTML = 'Answer Key & Analysis';
          renderProtectedMarkdown(keyContent, document.getElementById('pane-right-content'));
        } else {
          document.getElementById('pane-right-title').innerHTML = 'Detailed Step-by-Step Solutions';
          renderProtectedMarkdown(solContent, document.getElementById('pane-right-content'));
        }
      }
    }`;

const newLoadDocs = `    // In-Memory Document Cache (Anti-piracy protected, never exposed to global scope)
    const mockDocumentsCache = {};

    function clearActiveDocuments() {
      for (const k in mockDocumentsCache) delete mockDocumentsCache[k];
      const left = document.getElementById('pane-left-content');
      const right = document.getElementById('pane-right-content');
      if (left) left.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #64748b;">No active examination loaded.</div>';
      if (right) right.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #64748b;">No active solutions loaded.</div>';
    }

    // Document Loading & Math-Protected Markdown Parsing
    async function loadActiveDocuments() {
      const pad = String(currentMock).padStart(2, '0');
      const mockKey = \`Mock_\${pad}\`;
      const isFreeMock = unlockedFreeMocks.includes(currentMock);

      const leftPane = document.getElementById('pane-left-content');
      const rightPane = document.getElementById('pane-right-content');

      // 1. Check in-memory cache first
      if (mockDocumentsCache[mockKey]) {
        renderMockPayload(mockDocumentsCache[mockKey]);
        return;
      }

      // 2. Check offline demo store (Mocks 01, 21, 41 only)
      if (isFreeMock && window.DEMO_MOCKS) {
        const qpKey = \`\${mockKey}_Question_Paper.md\`;
        const solKey = \`\${mockKey}_Detailed_Solutions.md\`;
        const keyKey = \`\${mockKey}_Answer_Key_and_Analysis.md\`;
        if (window.DEMO_MOCKS[qpKey]) {
          const payload = {
            qpContent: window.DEMO_MOCKS[qpKey],
            solContent: window.DEMO_MOCKS[solKey],
            keyContent: window.DEMO_MOCKS[keyKey]
          };
          mockDocumentsCache[mockKey] = payload;
          renderMockPayload(payload);
          return;
        }
      }

      // 3. Show loading spinner in panes
      if (leftPane) leftPane.innerHTML = '<div style="padding: 3rem 1.5rem; text-align: center; color: #059669; font-weight: 600;"><div style="margin-bottom: 0.5rem;">🔒 Verifying authorization & loading examination material...</div><div style="font-size: 0.8rem; color: #64748b;">Scale Test Series Anti-Piracy Secure Stream</div></div>';
      if (rightPane) rightPane.innerHTML = '<div style="padding: 3rem 1.5rem; text-align: center; color: #64748b;"><div style="margin-bottom: 0.5rem;">Loading authorized step-by-step NCERT deconstruction...</div></div>';

      // 4. Request authorized content from backend
      try {
        const res = await apiRequest(\`/api/mocks/\${currentMock}/content\`);
        if (res.ok && res.data && res.data.success) {
          mockDocumentsCache[mockKey] = res.data;
          renderMockPayload(res.data);
          if (res.data.watermarkInfo) {
            updateContentWatermarks(res.data.watermarkInfo);
          }
        } else if (res.status === 401) {
          renderAuthGate();
        } else if (res.status === 403) {
          if (res.data?.error === 'ACCOUNT_SUSPENDED') {
            renderSuspendedGate(res.data?.message);
          } else {
            renderPaywallGate();
          }
        } else {
          if (leftPane) leftPane.innerHTML = \`<div style="padding: 2.5rem; text-align: center; color: #dc2626;"><strong>Unable to load mock test.</strong><p style="font-size: 0.85rem; color: #64748b; margin-top: 0.5rem;">\${escapeHtml(res.data?.message || 'Please check your connection and try again.')}</p></div>\`;
        }
      } catch (err) {
        console.error('[Load Docs Error]:', err);
        if (leftPane) leftPane.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #dc2626;">Network error loading examination content.</div>';
      }
    }

    function renderMockPayload(payload) {
      renderProtectedMarkdown(payload.qpContent, document.getElementById('pane-left-content'));
      if (currentViewMode === 'key') {
        document.getElementById('pane-right-title').innerHTML = 'Answer Key & Analysis';
        renderProtectedMarkdown(payload.keyContent, document.getElementById('pane-right-content'));
      } else {
        document.getElementById('pane-right-title').innerHTML = 'Detailed Step-by-Step Solutions';
        renderProtectedMarkdown(payload.solContent, document.getElementById('pane-right-content'));
      }
    }

    function renderAuthGate() {
      const leftPane = document.getElementById('pane-left-content');
      const rightPane = document.getElementById('pane-right-content');
      const gateHtml = \`
        <div style="padding: 3rem 1.5rem; text-align: center; max-width: 420px; margin: 2rem auto; background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px;">
          <div style="font-size: 2rem; margin-bottom: 0.75rem;">🔐</div>
          <h3 style="font-size: 1.1rem; color: #0f172a; margin-bottom: 0.5rem;">Sign In Required</h3>
          <p style="font-size: 0.85rem; color: #64748b; line-height: 1.5; margin-bottom: 1.25rem;">
            Please sign in to verify your student entitlement and access this examination material.
          </p>
          <button class="btn-primary" onclick="openAuthModal()" style="padding: 0.45rem 1.25rem; font-size: 0.85rem; border-radius: 7px;">Sign In to Scale Test Series</button>
        </div>
      \`;
      if (leftPane) leftPane.innerHTML = gateHtml;
      if (rightPane) rightPane.innerHTML = gateHtml;
    }

    function renderSuspendedGate(msg) {
      const leftPane = document.getElementById('pane-left-content');
      const rightPane = document.getElementById('pane-right-content');
      const gateHtml = \`
        <div style="padding: 3rem 1.5rem; text-align: center; max-width: 420px; margin: 2rem auto; background: #fef2f2; border: 1.5px solid #fecaca; border-radius: 12px;">
          <div style="font-size: 2rem; margin-bottom: 0.75rem;">⛔</div>
          <h3 style="font-size: 1.1rem; color: #991b1b; margin-bottom: 0.5rem;">Account Suspended</h3>
          <p style="font-size: 0.85rem; color: #7f1d1d; line-height: 1.5; margin-bottom: 1rem;">
            \${escapeHtml(msg || 'Your account is currently suspended. Access to examination papers is restricted.')}
          </p>
          <div style="font-size: 0.78rem; color: #b91c1c;">Please contact support@scaleseries.com for appeal.</div>
        </div>
      \`;
      if (leftPane) leftPane.innerHTML = gateHtml;
      if (rightPane) rightPane.innerHTML = gateHtml;
    }

    function renderPaywallGate() {
      const leftPane = document.getElementById('pane-left-content');
      const rightPane = document.getElementById('pane-right-content');
      const gateHtml = \`
        <div style="padding: 3rem 1.5rem; text-align: center; max-width: 440px; margin: 2rem auto; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 12px; box-shadow: 0 4px 16px rgba(5, 150, 105, 0.08);">
          <div style="font-size: 2.2rem; margin-bottom: 0.75rem;">🔒</div>
          <h3 style="font-size: 1.15rem; color: #064e3b; margin-bottom: 0.5rem;">Premium Mock Test Locked</h3>
          <p style="font-size: 0.85rem; color: #374151; line-height: 1.5; margin-bottom: 1.25rem;">
            This authentic 2026-calibrated full-length mock paper is reserved for enrolled candidates.
          </p>
          <button class="btn-primary" onclick="handleUnlock()" style="padding: 0.55rem 1.25rem; font-size: 0.88rem; border-radius: 8px;">Unlock All 60 Mocks @ ₹999 &rarr;</button>
          <div style="font-size: 0.75rem; color: #059669; margin-top: 0.75rem; font-weight: 600;">✓ Includes Instant NCERT Detailed Solutions & Step-by-Step Analysis</div>
        </div>
      \`;
      if (leftPane) leftPane.innerHTML = gateHtml;
      if (rightPane) rightPane.innerHTML = gateHtml;
    }`;

if (html.includes(oldLoadDocs)) {
  html = html.replace(oldLoadDocs, newLoadDocs);
  console.log('Successfully updated loadActiveDocuments.');
} else {
  console.warn('Warning: oldLoadDocs not found directly.');
}

console.log('[8/8] Hooking up clearActiveDocuments on logout and window focus session check...');
html = html.replace(
  'showToast(\'Logged out safely. Device session closed.\', \'info\');',
  'clearActiveDocuments();\n      showToast(\'Logged out safely. Device session closed.\', \'info\');'
);

// Add window focus listener to refresh entitlement quietly when student re-enters tab
if (!html.includes('window.addEventListener(\'focus\', checkServerSessionQuietly);')) {
  html = html.replace(
    'window.addEventListener(\'DOMContentLoaded\', async () => {',
    `async function checkServerSessionQuietly() {
      if (!currentUser) return;
      try {
        const res = await apiRequest('/api/auth/me');
        if (res.ok && res.data.authenticated) {
          const hasAccess = !!(res.data.entitlement && res.data.entitlement.hasAccess);
          if (hasAccess !== isUserPaid) {
            isUserPaid = hasAccess;
            if (isUserPaid) {
              localStorage.setItem('scale_test_series_paid', 'true');
            } else {
              localStorage.removeItem('scale_test_series_paid');
              clearActiveDocuments();
            }
            updatePurchaseUI(isUserPaid);
            updateHeaderBadge();
            if (typeof renderSidebar === 'function') renderSidebar();
          }
        }
      } catch (e) {}
    }
    window.addEventListener('focus', checkServerSessionQuietly);

    window.addEventListener('DOMContentLoaded', async () => {`
  );
  console.log('Added window focus quiet entitlement check.');
}

// Write to mock_tests/index.html
fs.writeFileSync(indexPath, html, 'utf8');
console.log('Successfully saved mock_tests/index.html');

// The Golden Rule: replicate identically to mock_tests/neet/index.html and neet_mock_tests/index.html
const target1 = path.resolve(__dirname, '../../mock_tests/neet/index.html');
const target2 = path.resolve(__dirname, '../../neet_mock_tests/index.html');

fs.writeFileSync(target1, html, 'utf8');
console.log('Successfully replicated to mock_tests/neet/index.html');

fs.writeFileSync(target2, html, 'utf8');
console.log('Successfully replicated to neet_mock_tests/index.html');

