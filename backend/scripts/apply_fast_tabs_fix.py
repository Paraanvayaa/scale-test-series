import re

files_to_update = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. FIX CSS: Remove `display: block !important;` from `.workspace-pane` in @media (max-width: 768px)
pattern_pane_css = r'(\.workspace-pane\s*\{[^}]*?)display:\s*block\s*!important;\s*([^}]*\})'
if re.search(pattern_pane_css, content):
    content = re.sub(pattern_pane_css, r'\1\2', content)
    print("Removed display: block !important from .workspace-pane in responsive CSS!")
else:
    print("WARNING: Could not find display: block !important in .workspace-pane")

# 2. FIX setViewMode to use setProperty with !important and scroll to top on mobile
old_set_view_mode = """    function setViewMode(mode) {
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

      // Load & render the selected document view
      loadActiveDocuments();
    }"""

new_set_view_mode = """    function setViewMode(mode) {
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
        dualWorkspace.style.setProperty('display', 'flex', 'important');
        paneLeft.style.setProperty('display', 'flex', 'important');
        paneRight.style.setProperty('display', 'flex', 'important');
      } else if (mode === 'test-only') {
        dualWorkspace.style.setProperty('display', isMobile ? 'block' : 'flex', 'important');
        paneLeft.style.setProperty('display', isMobile ? 'block' : 'flex', 'important');
        paneRight.style.setProperty('display', 'none', 'important');
      } else if (mode === 'sol-only' || mode === 'key') {
        dualWorkspace.style.setProperty('display', isMobile ? 'block' : 'flex', 'important');
        paneLeft.style.setProperty('display', 'none', 'important');
        paneRight.style.setProperty('display', isMobile ? 'block' : 'flex', 'important');
      }

      // On mobile, instantly scroll to top of workspace so student sees the newly selected tab
      if (isMobile) {
        window.scrollTo({ top: 0, behavior: 'instant' });
      }

      // Load & render the selected document view
      loadActiveDocuments();
    }"""

if old_set_view_mode in content:
    content = content.replace(old_set_view_mode, new_set_view_mode)
    print("Replaced setViewMode with high-priority display styling and scroll!")
else:
    print("WARNING: Could not find exact old_set_view_mode string!")

# 3. FIX launchDemoTest and showExamWorkspace to avoid duplicate loading
old_launch_func = """    function launchDemoTest(m) {
      currentMock = m;
      if (m <= 20) currentTier = 'foundation';
      else if (m <= 40) currentTier = 'moderate';
      else currentTier = 'difficult';
      
      showExamWorkspace();
      selectMock(m);
      window.scrollTo({ top: 0, behavior: 'instant' });
    }"""

new_launch_func = """    function launchDemoTest(m) {
      currentMock = m;
      if (m <= 20) currentTier = 'foundation';
      else if (m <= 40) currentTier = 'moderate';
      else currentTier = 'difficult';
      
      showExamWorkspace(m);
    }"""

old_show_exam = """    function showExamWorkspace() {
      document.body.classList.add('exam-mode');
      document.getElementById('landing-view').style.display = 'none';
      document.getElementById('exam-workspace-view').style.display = 'flex';
      renderSidebar();
      prewarmDemoMocks();
      updateHeaderBadge();
      loadActiveDocuments();
    }"""

new_show_exam = """    function showExamWorkspace(targetMock) {
      document.body.classList.add('exam-mode');
      document.getElementById('landing-view').style.display = 'none';
      document.getElementById('exam-workspace-view').style.display = 'flex';
      
      if (typeof targetMock === 'number') {
        selectMock(targetMock);
      } else {
        renderSidebar();
        prewarmDemoMocks();
        updateHeaderBadge();
        loadActiveDocuments();
      }
      window.scrollTo({ top: 0, behavior: 'instant' });
    }"""

if old_launch_func in content:
    content = content.replace(old_launch_func, new_launch_func)
    print("Updated launchDemoTest!")
if old_show_exam in content:
    content = content.replace(old_show_exam, new_show_exam)
    print("Updated showExamWorkspace!")

# 4. ENHANCE prewarmDemoMocks & ADD prewarmRenderedHtml
old_prewarm = """    // Pre-cache Demo Mocks (01, 21, 41) synchronously into memory on load
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

new_prewarm = """    // Pre-cache Demo Mocks (01, 21, 41) synchronously into memory on load
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
    }

    // Pre-render demo mocks HTML in background for 0ms instantaneous switching
    function prewarmRenderedHtml() {
      if (!window.DEMO_MOCKS) return;
      setTimeout(() => {
        [1, 21, 41].forEach(m => {
          const pad = String(m).padStart(2, '0');
          const mockKey = `Mock_${pad}`;
          const qpKey = `${mockKey}_qp`;
          const solKey = `${mockKey}_sol`;
          const keyKey = `${mockKey}_key`;
          const rawQp = window.DEMO_MOCKS[`${mockKey}_Question_Paper.md`];
          const rawSol = window.DEMO_MOCKS[`${mockKey}_Detailed_Solutions.md`];
          const rawKey = window.DEMO_MOCKS[`${mockKey}_Answer_Key_and_Analysis.md`];

          if (rawQp && !mockRenderedHtmlCache[qpKey]) {
            const dummy = document.createElement('div');
            renderProtectedMarkdown(rawQp, dummy, (html) => { mockRenderedHtmlCache[qpKey] = html; });
          }
          if (rawSol && !mockRenderedHtmlCache[solKey]) {
            const dummy = document.createElement('div');
            renderProtectedMarkdown(rawSol, dummy, (html) => { mockRenderedHtmlCache[solKey] = html; });
          }
          if (rawKey && !mockRenderedHtmlCache[keyKey]) {
            const dummy = document.createElement('div');
            renderProtectedMarkdown(rawKey, dummy, (html) => { mockRenderedHtmlCache[keyKey] = html; });
          }
        });
      }, 60);
    }"""

if old_prewarm in content:
    content = content.replace(old_prewarm, new_prewarm)
    print("Enhanced prewarm functions with background prewarmRenderedHtml!")

# Add prewarmRenderedHtml() call to DOMContentLoaded
content = content.replace(
    'prewarmDemoMocks();\n      updateHeaderBadge();',
    'prewarmDemoMocks();\n      prewarmRenderedHtml();\n      updateHeaderBadge();'
)

# Write to all 3 files
for p in files_to_update:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {p}")

c = [open(f, 'rb').read() for f in files_to_update]
assert c[0] == c[1] == c[2], "Mismatch!"
print("Golden Rule verified! Length:", len(c[0]))

