import re

files = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

with open(files[0], 'r', encoding='utf-8') as f:
    html = f.read()

# -------------------------------------------------------------
# 1. Update CSS: Replace mobile exam media query with comprehensive <= 900px rules
# -------------------------------------------------------------
mobile_css_old = """      /* =========================================================
         MOBILE EXAM HEADER: ULTRA-COMPACT (70px TOTAL HEIGHT)
         ========================================================= */
      .exam-header {
        padding: 0.35rem 0.55rem !important;
        min-height: unset !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        background: #ffffff !important;
        border-bottom: 1px solid #e2e8f0 !important;
      }
      .exam-header-left {
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 4px !important;
      }
      .exam-header-left button {
        padding: 0.28rem 0.45rem !important;
        font-size: 0.72rem !important;
        height: 30px !important;
      }
      #currentMockLabel {
        font-size: 0.82rem !important;
        font-weight: 800 !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        max-width: 140px !important;
      }
      #examTierBadge {
        font-size: 0.62rem !important;
        padding: 0.1rem 0.35rem !important;
        white-space: nowrap !important;
      }
      .exam-header-right {
        display: none !important;
      }

      /* Tabs Bar: Compact & Full-Width */
      .tabs-header {
        padding: 0.25rem 0.5rem !important;
        background: #f8fafc !important;
        border-bottom: 1px solid #e2e8f0 !important;
      }
      .tabs-group {
        width: 100% !important;
        gap: 3px !important;
      }
      .tab-btn {
        flex: 1 !important;
        justify-content: center !important;
        font-size: 0.74rem !important;
        padding: 0.32rem 0.2rem !important;
        height: 32px !important;
      }
      .tab-btn svg {
        display: none !important; /* Hide icons on mobile tabs for clean text fit */
      }
      .tabs-meta-tag {
        display: none !important; /* Completely hide the 4-line KaTeX typography tag on mobile */
      }

      /* Hide Redundant Pane Header on Mobile */
      .pane-header {
        display: none !important; /* Active tab already tells user what pane is active! */
      }

      /* Single Full-Width Mobile Workspace Pane */
      #dual-workspace {
        display: block !important;
        padding: 0.25rem !important;
        overflow-y: auto !important;
      }
      .workspace-pane {
        width: 100% !important;
        height: 100% !important;
        border: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
      }
      .pane-scroll {
        padding: 0.65rem 0.85rem !important;
        font-size: 0.98rem !important;
        line-height: 1.62 !important;
      }

      /* Mobile Exam Engine: Absolutely NO Split Screen */
      #tab-split {
        display: none !important; /* Never allow split screen on mobile */
      }
      #desktopSidebarToggleBtn {
        display: none !important;
      }
      .tabs-header {
        padding: 0.35rem 0.65rem !important;
      }
      .tabs-group {
        width: 100% !important;
      }
      .tab-btn {
        flex: 1 !important;
        justify-content: center !important;
        font-size: 0.76rem !important;
        padding: 0.45rem 0.3rem !important;
      }
      .exam-header {
        padding: 0.45rem 0.75rem !important;
        flex-wrap: wrap !important;
        gap: 0.4rem !important;
      }
      .exam-header-left {
        width: 100% !important;
        justify-content: space-between !important;
      }
      .exam-header-right {
        display: none !important;
      }
      #mobileDrawerBtn {
        display: inline-flex !important;
      }

      /* Single Full-Width Mobile Pane */
      #dual-workspace {
        display: block !important;
        padding: 0.4rem !important;
        overflow-y: auto !important;
      }
      .workspace-pane {
        width: 100% !important;
        height: 100% !important;
        border-radius: 8px !important;
      }
      .pane-scroll {
        padding: 0.95rem 1.1rem !important;
        font-size: 0.98rem !important;
      }

      /* Mobile Sidebar Overlay */
      .exam-sidebar {
        position: fixed !important;
        top: 0 !important;
        bottom: 0 !important;
        left: 0 !important;
        width: 290px !important;
        transform: translateX(-100%) !important;
        box-shadow: 4px 0 20px rgba(0, 0, 0, 0.25) !important;
        z-index: 2500 !important;
      }
      .exam-sidebar.mobile-open {
        transform: translateX(0) !important;
      }
      .sidebar-backdrop {
        position: fixed !important;
        top: 0 !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        background: rgba(15, 23, 42, 0.5) !important;
        z-index: 2400 !important;
        display: none;
      }
      .sidebar-backdrop.active {
        display: block !important;
      }"""

mobile_css_new = """      /* =========================================================
         MOBILE & TABLET ENGINE (<= 900px): NATURAL SCROLL & FULL VIEW
         ========================================================= */
      #exam-workspace-view {
        height: auto !important;
        min-height: 100vh !important;
        overflow-y: visible !important;
        display: flex !important;
        flex-direction: column !important;
      }
      .exam-main-body {
        height: auto !important;
        min-height: calc(100vh - 80px) !important;
        overflow: visible !important;
        display: block !important;
        position: static !important;
      }
      .workspace-area {
        height: auto !important;
        overflow: visible !important;
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
      }
      #dual-workspace {
        height: auto !important;
        overflow: visible !important;
        display: block !important;
        padding: 0.35rem 0.25rem !important;
        width: 100% !important;
        box-sizing: border-box !important;
      }
      .workspace-pane {
        height: auto !important;
        overflow: visible !important;
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        border: none !important;
        box-shadow: none !important;
        background: transparent !important;
      }
      .pane-scroll {
        height: auto !important;
        max-height: none !important;
        overflow-y: visible !important;
        overflow-x: hidden !important;
        padding: 0.75rem 0.5rem 5rem 0.5rem !important;
        font-size: 0.98rem !important;
        line-height: 1.62 !important;
        box-sizing: border-box !important;
        width: 100% !important;
        max-width: 100% !important;
      }
      .pane-scroll table,
      .pane-scroll .options-container,
      .pane-scroll .statement-card,
      .pane-scroll .assertion-card,
      .pane-scroll .reason-card,
      .pane-scroll .takeaway-box,
      .pane-scroll .distractor-box,
      .pane-scroll .katex-display {
        max-width: 100% !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        word-break: normal !important;
      }

      /* Compact Exam Header (42px) */
      .exam-header {
        padding: 0.35rem 0.65rem !important;
        min-height: 42px !important;
        height: 42px !important;
        box-sizing: border-box !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        background: #ffffff !important;
        border-bottom: 1px solid #e2e8f0 !important;
      }
      .exam-header-left {
        width: 100% !important;
        gap: 6px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
      }
      #desktopSidebarToggleBtn {
        display: none !important;
      }
      #mobileDrawerBtn {
        display: inline-flex !important;
        padding: 0.25rem 0.55rem !important;
        font-size: 0.74rem !important;
        height: 28px !important;
        box-sizing: border-box !important;
        align-items: center !important;
      }
      .exam-header-left button:not(#mobileDrawerBtn) {
        padding: 0.25rem 0.55rem !important;
        font-size: 0.74rem !important;
        height: 28px !important;
        box-sizing: border-box !important;
      }
      #currentMockLabel {
        font-size: 0.82rem !important;
        font-weight: 800 !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        max-width: 155px !important;
      }
      #examTierBadge {
        display: none !important;
      }
      .exam-header-right {
        display: none !important;
      }

      /* Compact Tabs Header (36px) */
      .tabs-header {
        padding: 0.25rem 0.5rem !important;
        min-height: 36px !important;
        height: 36px !important;
        box-sizing: border-box !important;
        background: #f8fafc !important;
        border-bottom: 1px solid #e2e8f0 !important;
      }
      .tabs-group {
        width: 100% !important;
        gap: 4px !important;
      }
      #tab-split {
        display: none !important; /* Never allow split screen on mobile */
      }
      .tab-btn {
        flex: 1 !important;
        font-size: 0.74rem !important;
        height: 28px !important;
        padding: 0.2rem !important;
        box-sizing: border-box !important;
        justify-content: center !important;
      }
      .tab-btn svg {
        display: none !important;
      }
      .tabs-meta-tag, .pane-header {
        display: none !important;
      }

      /* Sidebar Off-Canvas Drawer */
      .exam-sidebar {
        position: fixed !important;
        top: 0 !important;
        bottom: 0 !important;
        left: 0 !important;
        width: 290px !important;
        max-width: 85vw !important;
        height: 100vh !important;
        height: 100dvh !important;
        transform: translateX(-100%) !important;
        transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        z-index: 9999 !important;
        box-shadow: 4px 0 25px rgba(0, 0, 0, 0.3) !important;
        background: #ffffff !important;
        display: flex !important;
        flex-direction: column !important;
      }
      .exam-sidebar.mobile-open {
        transform: translateX(0) !important;
      }
      .sidebar-backdrop {
        position: fixed !important;
        top: 0 !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        background: rgba(15, 23, 42, 0.6) !important;
        z-index: 9998 !important;
        backdrop-filter: blur(2px) !important;
        display: none;
      }
      .sidebar-backdrop.active {
        display: block !important;
      }

      /* Floating Mobile Dock (Always accessible at bottom) */
      .mobile-floating-dock {
        display: flex !important;
        position: fixed !important;
        bottom: 16px !important;
        right: 16px !important;
        z-index: 1000 !important;
        background: rgba(15, 23, 42, 0.92) !important;
        backdrop-filter: blur(8px) !important;
        padding: 4px 6px !important;
        border-radius: 999px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
        align-items: center !important;
        gap: 6px !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
      }
      .floating-dock-btn {
        background: transparent !important;
        border: none !important;
        color: #ffffff !important;
        font-size: 0.74rem !important;
        font-weight: 700 !important;
        padding: 0.35rem 0.65rem !important;
        border-radius: 999px !important;
        cursor: pointer !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 4px !important;
        white-space: nowrap !important;
        text-decoration: none !important;
      }
      .floating-dock-btn:active {
        background: rgba(255, 255, 255, 0.25) !important;
      }
      .floating-dock-btn.primary {
        background: #059669 !important;
        color: #ffffff !important;
      }"""

# Normalise for matching
html_norm = html.replace('\r\n', '\n')
old_m_norm = mobile_css_old.replace('\r\n', '\n')
new_m_norm = mobile_css_new.replace('\r\n', '\n')

if old_m_norm in html_norm:
    html_norm = html_norm.replace(old_m_norm, new_m_norm)
    print("Replaced mobile exam CSS successfully!")
else:
    print("WARNING: mobile_css_old not found in html!")

# Add desktop hide for mobile floating dock
if '.mobile-floating-dock {' not in html_norm:
    html_norm = html_norm.replace(
        '</style>',
        """    @media (min-width: 901px) {
      .mobile-floating-dock {
        display: none !important;
      }
    }
  </style>"""
    )
    print("Added desktop rule for .mobile-floating-dock")

# -------------------------------------------------------------
# 2. Add Mobile Floating Dock HTML before </body>
# -------------------------------------------------------------
floating_dock_html = """  <!-- Floating Mobile Quick-Action Dock -->
  <div class="mobile-floating-dock" id="mobileFloatingDock">
    <button type="button" class="floating-dock-btn primary" onclick="toggleSidebarDrawer()">
      <span>&#9776;</span> Mocks
    </button>
    <button type="button" class="floating-dock-btn" id="dockTabToggleBtn" onclick="toggleMobileViewTab()">
      <span id="dockTabLabel">Solutions &rarr;</span>
    </button>
    <button type="button" class="floating-dock-btn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="Back to Top">
      &uarr; Top
    </button>
  </div>
"""

if 'id="mobileFloatingDock"' not in html_norm:
    html_norm = html_norm.replace('</body>', floating_dock_html + '\n</body>')
    print("Added floating dock HTML!")

# -------------------------------------------------------------
# 3. Update JavaScript: Performance & Document Caching & Lazy-loading
# -------------------------------------------------------------
old_js_cache = """    // In-Memory Document Cache (Anti-piracy protected, never exposed to global scope)
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
      const mockKey = `Mock_${pad}`;
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
        const qpKey = `${mockKey}_Question_Paper.md`;
        const solKey = `${mockKey}_Detailed_Solutions.md`;
        const keyKey = `${mockKey}_Answer_Key_and_Analysis.md`;
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
        const res = await apiRequest(`/api/mocks/${currentMock}/content`);
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
          if (leftPane) leftPane.innerHTML = `<div style="padding: 2.5rem; text-align: center; color: #dc2626;"><strong>Unable to load mock test.</strong><p style="font-size: 0.85rem; color: #64748b; margin-top: 0.5rem;">${escapeHtml(res.data?.message || 'Please check your connection and try again.')}</p></div>`;
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
    }"""

new_js_cache = """    // High-Performance In-Memory Document & Pre-Rendered DOM Caches
    const mockDocumentsCache = {};
    const mockRenderedHtmlCache = {}; // Instantaneous 0ms switching!

    function clearActiveDocuments() {
      for (const k in mockDocumentsCache) delete mockDocumentsCache[k];
      for (const k in mockRenderedHtmlCache) delete mockRenderedHtmlCache[k];
      const left = document.getElementById('pane-left-content');
      const right = document.getElementById('pane-right-content');
      if (left) left.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #64748b;">No active examination loaded.</div>';
      if (right) right.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #64748b;">No active solutions loaded.</div>';
    }

    // Toggle Mobile Floating Dock between Question Paper and Solutions
    function toggleMobileViewTab() {
      if (currentViewMode === 'test-only') {
        setViewMode('sol-only');
      } else {
        setViewMode('test-only');
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function updateFloatingDockState() {
      const label = document.getElementById('dockTabLabel');
      if (!label) return;
      if (currentViewMode === 'sol-only' || currentViewMode === 'key') {
        label.innerHTML = '&larr; Questions';
      } else {
        label.innerHTML = 'Solutions &rarr;';
      }
    }

    // Document Loading & Math-Protected Markdown Parsing with Caching
    async function loadActiveDocuments() {
      const pad = String(currentMock).padStart(2, '0');
      const mockKey = `Mock_${pad}`;
      const isFreeMock = unlockedFreeMocks.includes(currentMock);

      const leftPane = document.getElementById('pane-left-content');
      const rightPane = document.getElementById('pane-right-content');

      // 1. Instant check: If rendered HTML is already in memory, display instantly (0ms)
      const qpKey = `${mockKey}_qp`;
      if (mockRenderedHtmlCache[qpKey]) {
        if (leftPane) leftPane.innerHTML = mockRenderedHtmlCache[qpKey];
        renderRightPaneIfNeeded(mockDocumentsCache[mockKey]);
        return;
      }

      // 2. Check in-memory raw payload
      if (mockDocumentsCache[mockKey]) {
        renderMockPayload(mockDocumentsCache[mockKey]);
        return;
      }

      // 3. Check offline demo store (Mocks 01, 21, 41 only)
      if (isFreeMock && window.DEMO_MOCKS) {
        const rawQpKey = `${mockKey}_Question_Paper.md`;
        const rawSolKey = `${mockKey}_Detailed_Solutions.md`;
        const rawKeyKey = `${mockKey}_Answer_Key_and_Analysis.md`;
        if (window.DEMO_MOCKS[rawQpKey]) {
          const payload = {
            qpContent: window.DEMO_MOCKS[rawQpKey],
            solContent: window.DEMO_MOCKS[rawSolKey],
            keyContent: window.DEMO_MOCKS[rawKeyKey]
          };
          mockDocumentsCache[mockKey] = payload;
          renderMockPayload(payload);
          return;
        }
      }

      // 4. Show loading spinner in active pane
      if (leftPane) leftPane.innerHTML = '<div style="padding: 3rem 1.5rem; text-align: center; color: #059669; font-weight: 600;"><div style="margin-bottom: 0.5rem;">🔒 Loading authentic examination paper...</div><div style="font-size: 0.8rem; color: #64748b;">Scale Test Series High-Speed Engine</div></div>';
      if (rightPane) rightPane.innerHTML = '<div style="padding: 3rem 1.5rem; text-align: center; color: #64748b;"><div style="margin-bottom: 0.5rem;">Loading step-by-step NCERT deconstruction...</div></div>';

      // 5. Request authorized content from backend
      try {
        const res = await apiRequest(`/api/mocks/${currentMock}/content`);
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
          if (leftPane) leftPane.innerHTML = `<div style="padding: 2.5rem; text-align: center; color: #dc2626;"><strong>Unable to load mock test.</strong><p style="font-size: 0.85rem; color: #64748b; margin-top: 0.5rem;">${escapeHtml(res.data?.message || 'Please check your connection and try again.')}</p></div>`;
        }
      } catch (err) {
        console.error('[Load Docs Error]:', err);
        if (leftPane) leftPane.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #dc2626;">Network error loading examination content.</div>';
      }
    }

    // High-Speed Lazy Rendering: Render Question Paper immediately; defer Solutions unless in split view!
    function renderMockPayload(payload) {
      if (!payload) return;
      const pad = String(currentMock).padStart(2, '0');
      const mockKey = `Mock_${pad}`;
      const leftPane = document.getElementById('pane-left-content');

      // 1. Render Left Pane (Question Paper)
      const qpKey = `${mockKey}_qp`;
      if (mockRenderedHtmlCache[qpKey]) {
        if (leftPane) leftPane.innerHTML = mockRenderedHtmlCache[qpKey];
      } else if (leftPane) {
        renderProtectedMarkdown(payload.qpContent, leftPane, (renderedHtml) => {
          mockRenderedHtmlCache[qpKey] = renderedHtml;
        });
      }

      // 2. Render Right Pane only if currently visible (Split or Solutions mode)
      renderRightPaneIfNeeded(payload);
    }

    function renderRightPaneIfNeeded(payload) {
      if (!payload) return;
      const isMobile = window.innerWidth <= 900;
      // On mobile or test-only view, the right pane is hidden. Don't block the UI thread!
      if ((isMobile || currentViewMode === 'test-only') && currentViewMode !== 'sol-only' && currentViewMode !== 'key') {
        return;
      }

      const pad = String(currentMock).padStart(2, '0');
      const mockKey = `Mock_${pad}`;
      const rightPane = document.getElementById('pane-right-content');
      if (!rightPane) return;

      if (currentViewMode === 'key') {
        const titleEl = document.getElementById('pane-right-title');
        if (titleEl) titleEl.innerHTML = 'Answer Key & Analysis';
        const keyCacheKey = `${mockKey}_key`;
        if (mockRenderedHtmlCache[keyCacheKey]) {
          rightPane.innerHTML = mockRenderedHtmlCache[keyCacheKey];
        } else {
          renderProtectedMarkdown(payload.keyContent, rightPane, (html) => {
            mockRenderedHtmlCache[keyCacheKey] = html;
          });
        }
      } else {
        const titleEl = document.getElementById('pane-right-title');
        if (titleEl) titleEl.innerHTML = 'Detailed Step-by-Step Solutions';
        const solCacheKey = `${mockKey}_sol`;
        if (mockRenderedHtmlCache[solCacheKey]) {
          rightPane.innerHTML = mockRenderedHtmlCache[solCacheKey];
        } else {
          renderProtectedMarkdown(payload.solContent, rightPane, (html) => {
            mockRenderedHtmlCache[solCacheKey] = html;
          });
        }
      }
    }

    // Pre-cache Demo Mocks (01, 21, 41) in idle time for instant load
    function prewarmDemoMocks() {
      if (!window.DEMO_MOCKS) return;
      const demos = [1, 21, 41];
      let delay = 400;
      demos.forEach(m => {
        setTimeout(() => {
          const pad = String(m).padStart(2, '0');
          const mockKey = `Mock_${pad}`;
          const qpKey = `${mockKey}_Question_Paper.md`;
          const cacheKey = `${mockKey}_qp`;
          if (window.DEMO_MOCKS[qpKey] && !mockRenderedHtmlCache[cacheKey]) {
            const raw = window.DEMO_MOCKS[qpKey];
            const tempDiv = document.createElement('div');
            renderProtectedMarkdown(raw, tempDiv, (html) => {
              mockRenderedHtmlCache[cacheKey] = html;
            });
          }
        }, delay);
        delay += 600;
      });
    }"""

old_cache_norm = old_js_cache.replace('\r\n', '\n')
new_cache_norm = new_js_cache.replace('\r\n', '\n')

if old_cache_norm in html_norm:
    html_norm = html_norm.replace(old_cache_norm, new_cache_norm)
    print("Replaced document loading and caching logic successfully!")
else:
    print("WARNING: old_js_cache not found in html!")

# -------------------------------------------------------------
# 4. Update renderProtectedMarkdown with onComplete callback
# -------------------------------------------------------------
old_rpm = """    function renderProtectedMarkdown(rawMd, containerEl) {
      if (!rawMd || !containerEl) return;"""

new_rpm = """    function renderProtectedMarkdown(rawMd, containerEl, onComplete) {
      if (!rawMd || !containerEl) return;"""

if old_rpm in html_norm:
    html_norm = html_norm.replace(old_rpm, new_rpm)
    print("Updated renderProtectedMarkdown signature!")

# Update end of renderProtectedMarkdown
old_rpm_end = """      containerEl.innerHTML = html;

      // Trigger KaTeX
      if (window.renderMathInElement) {
        renderMathInElement(containerEl, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true }
          ],
          throwOnError: false
        });
      }
      containerEl.scrollTop = 0;
    }"""

new_rpm_end = """      containerEl.innerHTML = html;

      // Trigger KaTeX
      if (window.renderMathInElement) {
        try {
          renderMathInElement(containerEl, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false },
              { left: '\\(', right: '\\)', display: false },
              { left: '\\[', right: '\\]', display: true }
            ],
            throwOnError: false
          });
        } catch(e) {
          console.warn('KaTeX render warning:', e);
        }
      }
      containerEl.scrollTop = 0;
      if (typeof onComplete === 'function') {
        onComplete(containerEl.innerHTML);
      }
    }"""

old_rpm_end_norm = old_rpm_end.replace('\r\n', '\n')
new_rpm_end_norm = new_rpm_end.replace('\r\n', '\n')

if old_rpm_end_norm in html_norm:
    html_norm = html_norm.replace(old_rpm_end_norm, new_rpm_end_norm)
    print("Updated renderProtectedMarkdown callback hook!")
else:
    print("WARNING: old_rpm_end not found!")

# -------------------------------------------------------------
# 5. Update setViewMode & selectMock for auto-drawer-close & right-pane rendering
# -------------------------------------------------------------
old_set_view_mode = """    function setViewMode(mode) {
      const isMobile = window.innerWidth <= 768;
      // On mobile, never provide split screen; default to test-only if split requested
      if (isMobile && mode === 'split') {
        mode = 'test-only';
      }
      
      currentViewMode = mode;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById(`tab-${mode}`);
      if (activeBtn) activeBtn.classList.add('active');

      const dualWorkspace = document.getElementById('dual-workspace');
      const paneLeft = document.getElementById('pane-left');
      const paneRight = document.getElementById('pane-right');

      if (!isMobile && mode === 'split') {
        dualWorkspace.style.display = 'flex';
        paneLeft.style.display = 'flex';
        paneRight.style.display = 'flex';
      } else if (mode === 'test-only') {
        dualWorkspace.style.display = 'flex';
        paneLeft.style.display = 'flex';
        paneRight.style.display = 'none';
      } else if (mode === 'sol-only' || mode === 'key') {
        dualWorkspace.style.display = 'flex';
        paneLeft.style.display = 'none';
        paneRight.style.display = 'flex';
      }
      loadActiveDocuments();
    }"""

new_set_view_mode = """    function setViewMode(mode) {
      const isMobile = window.innerWidth <= 900;
      // On mobile, never provide split screen; default to test-only if split requested
      if (isMobile && mode === 'split') {
        mode = 'test-only';
      }
      
      currentViewMode = mode;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById(`tab-${mode}`);
      if (activeBtn) activeBtn.classList.add('active');

      const dualWorkspace = document.getElementById('dual-workspace');
      const paneLeft = document.getElementById('pane-left');
      const paneRight = document.getElementById('pane-right');

      if (!isMobile && mode === 'split') {
        dualWorkspace.style.display = 'flex';
        paneLeft.style.display = 'flex';
        paneRight.style.display = 'flex';
      } else if (mode === 'test-only') {
        dualWorkspace.style.display = isMobile ? 'block' : 'flex';
        paneLeft.style.display = isMobile ? 'block' : 'flex';
        paneRight.style.display = 'none';
      } else if (mode === 'sol-only' || mode === 'key') {
        dualWorkspace.style.display = isMobile ? 'block' : 'flex';
        paneLeft.style.display = 'none';
        paneRight.style.display = isMobile ? 'block' : 'flex';
      }

      updateFloatingDockState();

      // Render right pane on demand if switched to solutions/split
      const pad = String(currentMock).padStart(2, '0');
      const mockKey = `Mock_${pad}`;
      const payload = mockDocumentsCache[mockKey];
      if (payload && (mode === 'sol-only' || mode === 'key' || mode === 'split')) {
        renderRightPaneIfNeeded(payload);
      }
    }"""

old_svm_norm = old_set_view_mode.replace('\r\n', '\n')
new_svm_norm = new_set_view_mode.replace('\r\n', '\n')

if old_svm_norm in html_norm:
    html_norm = html_norm.replace(old_svm_norm, new_svm_norm)
    print("Updated setViewMode for mobile & lazy right-pane!")
else:
    print("WARNING: old_set_view_mode not found!")

# -------------------------------------------------------------
# 6. Auto-close sidebar on selectMock for mobile (<= 900px)
# -------------------------------------------------------------
old_select_mock = """    function selectMock(m) {
      currentMock = m;
      let newTier = 'foundation';
      if (m >= 41) newTier = 'difficult';
      else if (m >= 21) newTier = 'moderate';
      
      if (currentTier !== newTier) {
        currentTier = newTier;
        document.getElementById('tier-btn-foundation').classList.toggle('active', newTier === 'foundation');
        document.getElementById('tier-btn-moderate').classList.toggle('active', newTier === 'moderate');
        document.getElementById('tier-btn-difficult').classList.toggle('active', newTier === 'difficult');
      }

      renderSidebar();
      updateHeaderBadge();
      
      const pad = String(m).padStart(2, '0');
      let tierName = 'Ignite';
      if (m >= 41) tierName = 'Dominate';
      else if (m >= 21) tierName = 'Conquer';
      
      document.getElementById('currentMockLabel').querySelector('span').innerText = `NEET Mock - ${pad} [${tierName}]`;
      loadActiveDocuments();
    }"""

new_select_mock = """    function selectMock(m) {
      currentMock = m;
      let newTier = 'foundation';
      if (m >= 41) newTier = 'difficult';
      else if (m >= 21) newTier = 'moderate';
      
      if (currentTier !== newTier) {
        currentTier = newTier;
        document.getElementById('tier-btn-foundation').classList.toggle('active', newTier === 'foundation');
        document.getElementById('tier-btn-moderate').classList.toggle('active', newTier === 'moderate');
        document.getElementById('tier-btn-difficult').classList.toggle('active', newTier === 'difficult');
      }

      renderSidebar();
      updateHeaderBadge();
      
      const pad = String(m).padStart(2, '0');
      let tierName = 'Ignite';
      if (m >= 41) tierName = 'Dominate';
      else if (m >= 21) tierName = 'Conquer';
      
      document.getElementById('currentMockLabel').querySelector('span').innerText = `NEET Mock - ${pad} [${tierName}]`;

      // Auto-close sidebar drawer on mobile/tablet so the question paper has 100% width!
      if (window.innerWidth <= 900) {
        const sidebar = document.getElementById('appSidebar');
        const backdrop = document.getElementById('sidebarBackdrop');
        if (sidebar) sidebar.classList.remove('mobile-open');
        if (backdrop) backdrop.classList.remove('active');
        window.scrollTo({ top: 0, behavior: 'instant' });
      }

      loadActiveDocuments();
    }"""

old_sm_norm = old_select_mock.replace('\r\n', '\n')
new_sm_norm = new_select_mock.replace('\r\n', '\n')

if old_sm_norm in html_norm:
    html_norm = html_norm.replace(old_sm_norm, new_sm_norm)
    print("Updated selectMock to auto-close drawer on mobile!")
else:
    print("WARNING: old_select_mock not found!")

# -------------------------------------------------------------
# 7. Add prewarmDemoMocks call on DOMContentLoaded
# -------------------------------------------------------------
if 'prewarmDemoMocks();' not in html_norm:
    html_norm = html_norm.replace(
        'renderSidebar();',
        'renderSidebar();\n      prewarmDemoMocks();'
    )
    print("Added prewarmDemoMocks to DOMContentLoaded!")

# Write back to all 3 files
for fpath in files:
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html_norm)
    print(f"Updated {fpath}")

# Verify Golden Rule
with open(files[0], 'rb') as f: c1 = f.read()
with open(files[1], 'rb') as f: c2 = f.read()
with open(files[2], 'rb') as f: c3 = f.read()

assert c1 == c2 == c3, "Golden Rule check failed!"
print("PASS: Golden Rule verified! All 3 files are 100% identical byte-for-byte.")
