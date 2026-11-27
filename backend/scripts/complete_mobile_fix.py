import re
import os

files_to_update = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. REMOVE THE BOTTOM DOCK COMPLETELY (Markup)
# Find and remove <!-- Floating Mobile Quick-Action Dock --> and its div
content = re.sub(
    r'\s*<!-- Floating Mobile Quick-Action Dock -->\s*<div class="mobile-floating-dock" id="mobileFloatingDock">.*?</div>',
    '',
    content,
    flags=re.DOTALL
)

# 2. REMOVE JS REFERENCES TO mobileFloatingDock / updateFloatingDockState
content = re.sub(
    r'\s*updateFloatingDockState\(\);',
    '',
    content
)
content = re.sub(
    r'\s*// Toggle Mobile Floating Dock between Question Paper and Solutions\s*function updateFloatingDockState\(\)\s*\{.*?function toggleMobileViewTab\(\)\s*\{.*?\}',
    '',
    content,
    flags=re.DOTALL
)

# 3. UPDATE .exam-header HTML WITH 2-ROW DELIBERATE RESPONSIVE LAYOUT
old_header_pattern = r'<header class="exam-header">.*?</header>'
new_header_html = """<header class="exam-header" id="examHeader">
      <!-- Row 1: Brand & Actions -->
      <div class="exam-header-row exam-header-row-1">
        <div class="exam-header-brand" onclick="showLandingView()" title="Scale Test Series - Return to Home">
          <img src="logo.png" alt="Scale Test Series Logo" class="exam-brand-logo">
          <span class="exam-brand-name">Scale Test Series</span>
        </div>
        <div class="exam-header-row1-actions">
          <div id="userStatusTag" class="exam-user-status">Free Demo</div>
          <button class="btn-primary exam-header-unlock-btn" id="examUnlockBtn" onclick="openPaymentModal()">
            Unlock 60 Mocks &bull; &#8377;999
          </button>
        </div>
      </div>

      <!-- Row 2: Mock Navigation Controls & Current Test Title -->
      <div class="exam-header-row exam-header-row-2">
        <div class="exam-header-nav-btns">
          <button class="btn-secondary exam-nav-btn" id="mobileDrawerBtn" onclick="toggleSidebarDrawer()" title="Open Mocks List">
            <span>&#9776;</span> <strong>Mocks</strong>
          </button>
          <button class="btn-secondary exam-nav-btn" id="desktopSidebarToggleBtn" onclick="toggleSidebarCollapse()" title="Collapse/Expand Mock List">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
            <span id="sidebarToggleText">Sidebar</span>
          </button>
          <button class="btn-secondary exam-nav-btn" id="examHomeBtn" onclick="showLandingView()" title="Back to Home">
            &larr; Home
          </button>
        </div>

        <div class="exam-header-title-box">
          <div id="currentMockLabel" class="exam-title-text" title="Current Active Mock">
            <span>NEET Mock - 01 [Ignite]</span>
          </div>
          <span id="examTierBadge" class="exam-tier-tag">Ignite Tier &bull; NCERT Core (01-20)</span>
        </div>
      </div>
    </header>"""

if re.search(old_header_pattern, content, flags=re.DOTALL):
    content = re.sub(old_header_pattern, new_header_html, content, count=1, flags=re.DOTALL)
    print("Replaced exam-header HTML with 2-row layout!")
else:
    print("WARNING: Could not find old exam-header HTML pattern!")

# 4. ADD MOBILE DRAWER CLOSE BUTTON TO SIDEBAR
sidebar_drawer_header = """      <aside class="exam-sidebar" id="appSidebar">
        <!-- Mobile Drawer Close Header -->
        <div class="sidebar-drawer-header">
          <div class="drawer-header-title">
            <span style="color: #059669;">&#9679;</span> 60 NEET Mocks
          </div>
          <button type="button" class="drawer-close-btn" onclick="toggleSidebarDrawer()" title="Close Mocks Drawer">&times;</button>
        </div>"""

if '<div class="sidebar-drawer-header">' not in content:
    content = content.replace(
        '<aside class="exam-sidebar" id="appSidebar">',
        sidebar_drawer_header
    )
    print("Added sidebar-drawer-header to appSidebar!")

# 5. RESTRUCTURE THE CSS:
# Ensure @media (max-width: 360px) is properly closed, and replace the mobile responsive block with clean, un-nested rules!

# Let's inspect where @media (max-width: 360px) starts and ends
pos_360 = content.find('@media (max-width: 360px)')
pos_engine = content.find('/* =========================================================\n         RESPONSIVE ENGINE: COMPREHENSIVE MOBILE & TABLET RULES')
if pos_engine == -1:
    pos_engine = content.find('RESPONSIVE ENGINE: COMPREHENSIVE MOBILE & TABLET RULES')

print("pos_360:", pos_360, "pos_engine:", pos_engine)

# Everything from pos_engine to the end of that style block or next section
pos_style_end = content.find('</style>', pos_engine)

# New Comprehensive Clean CSS for Desktop & Mobile
new_responsive_css = """    /* =========================================================
       EXAM HEADER STYLES (DESKTOP & BASE)
       ========================================================= */
    .exam-header {
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      box-sizing: border-box;
      width: 100%;
      z-index: 100;
    }
    .exam-header-row {
      display: flex;
      align-items: center;
    }
    .exam-header-brand {
      display: flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
    }
    .exam-brand-logo {
      width: 24px;
      height: 24px;
      border-radius: 6px;
      object-fit: cover;
    }
    .exam-brand-name {
      font-weight: 800;
      font-size: 0.90rem;
      color: #0f172a;
      white-space: nowrap;
    }
    .exam-header-row1-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .exam-user-status {
      font-size: 0.75rem;
      font-weight: 600;
      color: #059669;
      background: #ecfdf5;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      border: 1px solid #a7f3d0;
      white-space: nowrap;
    }
    .exam-header-unlock-btn {
      padding: 0.25rem 0.65rem;
      font-size: 0.76rem;
      font-weight: 700;
      border-radius: 6px;
      height: 30px;
      display: inline-flex;
      align-items: center;
      white-space: nowrap;
    }
    .exam-header-nav-btns {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .exam-nav-btn {
      height: 30px;
      padding: 0.25rem 0.65rem;
      font-size: 0.78rem;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      color: #0f172a;
      cursor: pointer;
    }
    .exam-nav-btn:hover {
      background: #f1f5f9;
    }
    .exam-header-title-box {
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 0;
    }
    .exam-title-text {
      font-size: 0.88rem;
      font-weight: 800;
      color: #0f172a;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .exam-tier-tag {
      font-size: 0.70rem;
      font-weight: 700;
      padding: 0.15rem 0.5rem;
      border-radius: 5px;
      white-space: nowrap;
      background: #dcfce7;
      color: #15803d;
    }

    /* Sidebar Drawer Header (Hidden on Desktop) */
    .sidebar-drawer-header {
      display: none;
      align-items: center;
      justify-content: space-between;
      padding: 0.65rem 0.85rem;
      border-bottom: 1px solid #e2e8f0;
      background: #f8fafc;
    }
    .drawer-header-title {
      font-size: 0.88rem;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .drawer-close-btn {
      background: none;
      border: none;
      font-size: 1.4rem;
      line-height: 1;
      cursor: pointer;
      color: #64748b;
      padding: 0 4px;
    }
    .drawer-close-btn:hover {
      color: #0f172a;
    }

    /* Desktop Exam Header Layout (> 768px) */
    @media (min-width: 769px) {
      .exam-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.45rem 1.25rem;
        height: 52px;
        min-height: 52px;
        gap: 1rem;
      }
      .exam-header-row-1 {
        display: flex;
        align-items: center;
        gap: 1rem;
        flex-shrink: 0;
      }
      .exam-header-row-2 {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex: 1;
        min-width: 0;
        gap: 1rem;
      }
      #mobileDrawerBtn {
        display: none !important;
      }
      #desktopSidebarToggleBtn {
        display: inline-flex !important;
      }
      .exam-header-row1-actions {
        order: 3;
      }
    }

    /* =========================================================
       RESPONSIVE ENGINE: COMPREHENSIVE MOBILE RULES (<= 768px)
       ========================================================= */
    @media (max-width: 768px) {
      /* 1. Comparison Section: Stacked Cards */
      .comparison-section {
        padding: 1.5rem 0.85rem !important;
        margin: 2rem 0 !important;
      }
      .comparison-table-wrap {
        display: none !important;
      }
      .comparison-cards-mobile {
        display: flex !important;
        flex-direction: column !important;
        gap: 1.25rem !important;
        margin-top: 1.5rem !important;
      }

      /* 2. Natural Document-Level Full-Page Scrolling */
      html, body {
        height: auto !important;
        min-height: 100% !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        -webkit-overflow-scrolling: touch !important;
      }
      body.exam-mode {
        height: auto !important;
        min-height: 100% !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        -webkit-overflow-scrolling: touch !important;
      }
      #exam-workspace-view {
        height: auto !important;
        min-height: 100vh !important;
        overflow: visible !important;
        overflow-y: visible !important;
        position: static !important;
        display: none; /* toggled by showExamWorkspace */
        flex-direction: column !important;
      }
      .exam-main-body {
        height: auto !important;
        min-height: auto !important;
        overflow: visible !important;
        overflow-y: visible !important;
        display: block !important;
        position: static !important;
      }
      .workspace-area {
        height: auto !important;
        min-height: auto !important;
        overflow: visible !important;
        overflow-y: visible !important;
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        flex: 1 1 100% !important;
        padding: 0 !important;
        margin: 0 !important;
      }
      #dual-workspace {
        height: auto !important;
        min-height: auto !important;
        overflow: visible !important;
        overflow-y: visible !important;
        display: block !important;
        padding: 0.5rem 0.5rem 2.5rem 0.5rem !important;
        width: 100% !important;
        box-sizing: border-box !important;
      }
      .workspace-pane {
        height: auto !important;
        min-height: auto !important;
        overflow: visible !important;
        overflow-y: visible !important;
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        border: none !important;
        box-shadow: none !important;
        background: transparent !important;
        display: block !important;
      }
      .pane-scroll {
        height: auto !important;
        min-height: auto !important;
        max-height: none !important;
        overflow: visible !important;
        overflow-y: visible !important;
        overflow-x: hidden !important;
        padding: 0.5rem 0.35rem !important;
        font-size: 0.98rem !important;
        line-height: 1.62 !important;
        box-sizing: border-box !important;
        width: 100% !important;
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

      /* 3. Mobile Exam Navbar (2 deliberate compact rows) */
      .exam-header {
        display: flex !important;
        flex-direction: column !important;
        padding: 0.35rem 0.65rem !important;
        background: #ffffff !important;
        border-bottom: 1px solid #e2e8f0 !important;
        gap: 0.35rem !important;
        width: 100% !important;
        box-sizing: border-box !important;
        position: relative !important;
      }
      .exam-header-row-1 {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
        gap: 6px !important;
      }
      .exam-header-brand {
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        min-width: 0 !important;
        flex-shrink: 1 !important;
      }
      .exam-brand-logo {
        width: 22px !important;
        height: 22px !important;
        border-radius: 5px !important;
        flex-shrink: 0 !important;
      }
      .exam-brand-name {
        font-weight: 700 !important;
        font-size: 0.82rem !important;
        color: #0f172a !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }
      .exam-header-row1-actions {
        display: flex !important;
        align-items: center !important;
        gap: 5px !important;
        flex-shrink: 0 !important;
      }
      .exam-user-status {
        display: none !important; /* Conceal secondary tag on narrow headers */
      }
      .exam-header-unlock-btn {
        padding: 0.22rem 0.50rem !important;
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        border-radius: 6px !important;
        height: 28px !important;
        background: #059669 !important;
        color: #ffffff !important;
        display: inline-flex !important;
        align-items: center !important;
      }
      .exam-header-row-2 {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
        gap: 6px !important;
        border-top: 1px solid #f1f5f9 !important;
        padding-top: 0.28rem !important;
      }
      .exam-header-nav-btns {
        display: flex !important;
        align-items: center !important;
        gap: 5px !important;
        flex-shrink: 0 !important;
      }
      #mobileDrawerBtn {
        display: inline-flex !important;
        height: 28px !important;
        padding: 0.2rem 0.55rem !important;
        font-size: 0.74rem !important;
        border-radius: 6px !important;
        align-items: center !important;
        gap: 4px !important;
        background: #f8fafc !important;
        border: 1px solid #cbd5e1 !important;
        color: #0f172a !important;
      }
      #desktopSidebarToggleBtn {
        display: none !important; /* Strictly hidden on mobile */
      }
      #examHomeBtn {
        display: inline-flex !important;
        height: 28px !important;
        padding: 0.2rem 0.48rem !important;
        font-size: 0.74rem !important;
        border-radius: 6px !important;
        background: #f8fafc !important;
        border: 1px solid #cbd5e1 !important;
        color: #0f172a !important;
      }
      .exam-header-title-box {
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-end !important;
        text-align: right !important;
        min-width: 0 !important;
        flex: 1 !important;
      }
      .exam-title-text {
        font-size: 0.78rem !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        max-width: 100% !important;
      }
      .exam-tier-tag {
        font-size: 0.62rem !important;
        font-weight: 600 !important;
        padding: 1px 6px !important;
        border-radius: 4px !important;
        white-space: nowrap !important;
        max-width: 100% !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }

      /* 4. Tab Navigation Strip */
      .tabs-header {
        padding: 0.35rem 0.5rem !important;
        background: #f8fafc !important;
        border-bottom: 1px solid #e2e8f0 !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        display: flex !important;
      }
      .tabs-group {
        display: flex !important;
        gap: 4px !important;
        width: 100% !important;
      }
      #tab-split {
        display: none !important; /* Hide dual split view tab on mobile */
      }
      .tab-btn {
        flex: 1 1 0 !important;
        min-width: 0 !important;
        white-space: nowrap !important;
        padding: 0.25rem 0.35rem !important;
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        border-radius: 6px !important;
        height: 30px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 4px !important;
      }
      .tab-btn svg {
        display: none !important;
      }
      .tabs-meta-tag, .pane-header {
        display: none !important;
      }

      /* 5. Mock Navigation Sidebar: Pure Off-Canvas Drawer (Zero space when closed) */
      .exam-sidebar {
        position: fixed !important;
        top: 0 !important;
        bottom: 0 !important;
        left: 0 !important;
        width: min(310px, 86vw) !important;
        max-width: 86vw !important;
        height: 100vh !important;
        height: 100dvh !important;
        transform: translateX(-100%) !important;
        transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        z-index: 10000 !important;
        box-shadow: 4px 0 25px rgba(0, 0, 0, 0.35) !important;
        background: #ffffff !important;
        display: flex !important;
        flex-direction: column !important;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch !important;
      }
      .exam-sidebar.mobile-open {
        transform: translateX(0) !important;
      }
      .sidebar-drawer-header {
        display: flex !important;
      }
      .sidebar-backdrop {
        position: fixed !important;
        top: 0 !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        background: rgba(15, 23, 42, 0.6) !important;
        z-index: 9999 !important;
        backdrop-filter: blur(2px) !important;
        display: none;
      }
      .sidebar-backdrop.active {
        display: block !important;
      }

      /* 6. Footer Responsive Layout */
      .site-footer {
        padding: 2.5rem 1rem calc(2rem + env(safe-area-inset-bottom, 0px)) 1rem !important;
      }
      .footer-container {
        grid-template-columns: 1fr !important;
        gap: 1.75rem !important;
        margin-bottom: 2rem !important;
      }
      .footer-links {
        gap: 0.6rem !important;
      }
      .footer-links a {
        padding: 0.2rem 0 !important;
        display: inline-block !important;
        font-size: 0.92rem !important;
      }
      .footer-bottom {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 0.6rem !important;
        padding-top: 1.5rem !important;
      }
    }
  """

# Now let's carefully replace from pos_engine to pos_style_end
# First let's check what was before pos_engine to ensure clean closing of max-width: 360px
before_engine = content[:pos_engine]
# Check if max-width: 360px has an unclosed brace in before_engine
slice_360 = before_engine[pos_360:]
if slice_360.count('{') > slice_360.count('}'):
    needed_closes = slice_360.count('{') - slice_360.count('}')
    print(f"Closing {needed_closes} unclosed braces before responsive engine block!")
    before_engine = before_engine.rstrip() + ('\n    }' * needed_closes) + '\n\n'

after_style = content[pos_style_end:]
new_content = before_engine + new_responsive_css + '\n  ' + after_style

# Write to all 3 files for Golden Rule
for path in files_to_update:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {path}")

# Verify Golden Rule
c_check = [open(f, 'rb').read() for f in files_to_update]
assert c_check[0] == c_check[1] == c_check[2], "Golden Rule mismatch!"
print("Golden Rule verified: all 3 files are 100% byte-for-byte identical! Length:", len(c_check[0]))

