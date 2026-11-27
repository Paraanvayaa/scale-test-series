files = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

# Read first file
with open(files[0], 'r', encoding='utf-8') as f:
    content = f.read()

content_norm = content.replace('\r\n', '\n')

old_load_docs_block = """    // Document Loading & Math-Protected Markdown Parsing with Caching
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

new_load_docs_block = """    // Document Loading & Math-Protected Markdown Parsing with Caching
    async function loadActiveDocuments() {
      const pad = String(currentMock).padStart(2, '0');
      const mockKey = `Mock_${pad}`;
      const isFreeMock = unlockedFreeMocks.includes(currentMock);

      const leftPane = document.getElementById('pane-left-content');
      const rightPane = document.getElementById('pane-right-content');

      // 1. Ensure raw payload is available in mockDocumentsCache
      let payload = mockDocumentsCache[mockKey];
      if (!payload && isFreeMock && window.DEMO_MOCKS) {
        const rawQpKey = `${mockKey}_Question_Paper.md`;
        const rawSolKey = `${mockKey}_Detailed_Solutions.md`;
        const rawKeyKey = `${mockKey}_Answer_Key_and_Analysis.md`;
        if (window.DEMO_MOCKS[rawQpKey]) {
          payload = {
            qpContent: window.DEMO_MOCKS[rawQpKey],
            solContent: window.DEMO_MOCKS[rawSolKey],
            keyContent: window.DEMO_MOCKS[rawKeyKey]
          };
          mockDocumentsCache[mockKey] = payload;
        }
      }

      // 2. If payload is in memory, render immediately!
      if (payload) {
        renderMockPayload(payload);
        return;
      }

      // 3. Show loading spinners while fetching authorized payload
      if (leftPane && (currentViewMode === 'split' || currentViewMode === 'test-only')) {
        leftPane.innerHTML = '<div style="padding: 3rem 1.5rem; text-align: center; color: #059669; font-weight: 600;"><div style="margin-bottom: 0.5rem;">🔒 Loading authentic examination paper...</div><div style="font-size: 0.8rem; color: #64748b;">Scale Test Series High-Speed Engine</div></div>';
      }
      if (rightPane && (currentViewMode === 'split' || currentViewMode === 'sol-only' || currentViewMode === 'key')) {
        rightPane.innerHTML = '<div style="padding: 3rem 1.5rem; text-align: center; color: #64748b;"><div style="margin-bottom: 0.5rem;">Loading step-by-step NCERT deconstruction...</div></div>';
      }

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

    // High-Speed Lazy Rendering: Render only the active view pane(s)
    function renderMockPayload(payload) {
      if (!payload) return;
      const pad = String(currentMock).padStart(2, '0');
      const mockKey = `Mock_${pad}`;
      const leftPane = document.getElementById('pane-left-content');
      const rightPane = document.getElementById('pane-right-content');

      // 1. Render Left Pane (Question Paper)
      if (leftPane && (currentViewMode === 'split' || currentViewMode === 'test-only')) {
        const qpKey = `${mockKey}_qp`;
        if (mockRenderedHtmlCache[qpKey]) {
          leftPane.innerHTML = mockRenderedHtmlCache[qpKey];
        } else {
          renderProtectedMarkdown(payload.qpContent, leftPane, (renderedHtml) => {
            mockRenderedHtmlCache[qpKey] = renderedHtml;
          });
        }
      }

      // 2. Render Right Pane (Detailed Solutions OR Answer Key)
      if (rightPane && (currentViewMode === 'split' || currentViewMode === 'sol-only' || currentViewMode === 'key')) {
        const titleEl = document.getElementById('pane-right-title');
        if (currentViewMode === 'key') {
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
    }

    // Pre-cache Demo Mocks (01, 21, 41) synchronously into memory on load
    function prewarmDemoMocks() {
      if (!window.DEMO_MOCKS) return;
      const demos = [1, 21, 41];
      demos.forEach(m => {
        const pad = String(m).padStart(2, '0');
        const mockKey = `Mock_${pad}`;
        const rawQpKey = `${mockKey}_Question_Paper.md`;
        const rawSolKey = `${mockKey}_Detailed_Solutions.md`;
        const rawKeyKey = `${mockKey}_Answer_Key_and_Analysis.md`;
        if (window.DEMO_MOCKS[rawQpKey]) {
          mockDocumentsCache[mockKey] = {
            qpContent: window.DEMO_MOCKS[rawQpKey],
            solContent: window.DEMO_MOCKS[rawSolKey],
            keyContent: window.DEMO_MOCKS[rawKeyKey]
          };
        }
      });
    }"""

old_svm_block = """      updateFloatingDockState();

      // Render right pane on demand if switched to solutions/split
      const pad = String(currentMock).padStart(2, '0');
      const mockKey = `Mock_${pad}`;
      const payload = mockDocumentsCache[mockKey];
      if (payload && (mode === 'sol-only' || mode === 'key' || mode === 'split')) {
        renderRightPaneIfNeeded(payload);
      }
    }"""

new_svm_block = """      updateFloatingDockState();

      // Load & render the selected document view
      loadActiveDocuments();
    }"""

assert old_load_docs_block in content_norm, "old_load_docs_block not found!"
assert old_svm_block in content_norm, "old_svm_block not found!"

content_norm = content_norm.replace(old_load_docs_block, new_load_docs_block)
content_norm = content_norm.replace(old_svm_block, new_svm_block)

for f in files:
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content_norm)
    print(f"Updated {f}")

# Verify Golden Rule
with open(files[0], 'rb') as fh: c1 = fh.read()
with open(files[1], 'rb') as fh: c2 = fh.read()
with open(files[2], 'rb') as fh: c3 = fh.read()

assert c1 == c2 == c3, "Mismatch!"
print("SUCCESS: Solutions and Answer Key rendering fixed across all 3 files!")

