import re

files = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

# Read first file
with open(files[0], 'r', encoding='utf-8') as f:
    content = f.read()

content_norm = content.replace('\r\n', '\n')

# -------------------------------------------------------------
# 1. Comparison Cards CSS & Styles
# -------------------------------------------------------------
comp_css = """    /* Comparison Section & Responsive Stacked Cards */
    .comparison-section {
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: var(--radius-xl);
      padding: 2.5rem 2rem;
      margin: 3.5rem 0;
    }
    .comparison-table-wrap {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .comparison-table {
      width: 100%;
      min-width: 640px;
      border-collapse: separate;
      border-spacing: 0;
      background: #ffffff;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid #cbd5e1;
      margin-top: 1.5rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .comparison-cards-mobile {
      display: none;
      flex-direction: column;
      gap: 1.1rem;
      margin-top: 1.25rem;
    }
    .comp-card {
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }
    .comp-card-header {
      background: #f1f5f9;
      padding: 0.8rem 1rem;
      font-weight: 800;
      font-size: 0.95rem;
      color: #0f172a;
      border-bottom: 1px solid #e2e8f0;
      letter-spacing: -0.01em;
    }
    .comp-card-body {
      padding: 0.9rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .comp-option {
      padding: 0.75rem 0.85rem;
      border-radius: 8px;
      font-size: 0.86rem;
      line-height: 1.5;
    }
    .comp-option-coaching {
      background: #fef2f2;
      border: 1px solid #fecaca;
      color: #7f1d1d;
    }
    .comp-option-scale {
      background: #ecfdf5;
      border: 1.5px solid #a7f3d0;
      color: #064e3b;
    }
    .comp-label {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 0.3rem;
      display: flex;
      align-items: center;
      gap: 5px;
    }"""

old_comp_css = """    .comparison-section {
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: var(--radius-xl);
      padding: 2.5rem 2rem;
      margin: 3.5rem 0;
    }
    .comparison-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      background: #ffffff;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid #cbd5e1;
      margin-top: 1.5rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }"""

if old_comp_css in content_norm:
    content_norm = content_norm.replace(old_comp_css, comp_css)
    print("Updated comparison CSS!")
else:
    print("WARNING: old_comp_css not found!")

# -------------------------------------------------------------
# 2. Add Mobile Comparison Cards HTML
# -------------------------------------------------------------
mobile_cards_html = """        <!-- Mobile Responsive Comparison Cards (<= 768px) -->
        <div class="comparison-cards-mobile">
          <div class="comp-card">
            <div class="comp-card-header">Question Architecture</div>
            <div class="comp-card-body">
              <div class="comp-option comp-option-coaching">
                <div class="comp-label"><span class="badge-cross">&#10008;</span> Traditional Coaching</div>
                <div>80% direct formula-plugging; out of sync with 2024-2026 NTA pattern</div>
              </div>
              <div class="comp-option comp-option-scale">
                <div class="comp-label"><span class="badge-check">&#10004;</span> Scale Test Series (2026-2027)</div>
                <div><strong>Exact 2026 NTA Blueprint</strong>: Statement I &amp; II, Assertion-Reason, Match Lists</div>
              </div>
            </div>
          </div>
          <div class="comp-card">
            <div class="comp-card-header">Authorship &amp; Pedigree</div>
            <div class="comp-card-body">
              <div class="comp-option comp-option-coaching">
                <div class="comp-label"><span class="badge-cross">&#10008;</span> Traditional Coaching</div>
                <div>Outsourced aggregators &amp; faculty using 10-year old modules</div>
              </div>
              <div class="comp-option comp-option-scale">
                <div class="comp-label"><span class="badge-check">&#10004;</span> Scale Test Series (2026-2027)</div>
                <div><strong>Curated by Top 50 AIR Rankers &amp; AIIMS New Delhi Medicos</strong></div>
              </div>
            </div>
          </div>
          <div class="comp-card">
            <div class="comp-card-header">Cognitive Progression</div>
            <div class="comp-card-body">
              <div class="comp-option comp-option-coaching">
                <div class="comp-label"><span class="badge-cross">&#10008;</span> Traditional Coaching</div>
                <div>One flat, random difficulty: creates false confidence or panic</div>
              </div>
              <div class="comp-option comp-option-scale">
                <div class="comp-label"><span class="badge-check">&#10004;</span> Scale Test Series (2026-2027)</div>
                <div><strong>3 Stepped Scientific Tiers</strong>: Ignite (Foundation) &rarr; Conquer (Speed) &rarr; Dominate (Rank Deciders)</div>
              </div>
            </div>
          </div>
          <div class="comp-card">
            <div class="comp-card-header">Explanation Quality</div>
            <div class="comp-card-body">
              <div class="comp-option comp-option-coaching">
                <div class="comp-label"><span class="badge-cross">&#10008;</span> Traditional Coaching</div>
                <div>Brief 2-line formula steps with no reason why distractors are wrong</div>
              </div>
              <div class="comp-option comp-option-scale">
                <div class="comp-label"><span class="badge-check">&#10004;</span> Scale Test Series (2026-2027)</div>
                <div><strong>NCERT Line Citation + Distractor Deconstruction</strong> for every single question</div>
              </div>
            </div>
          </div>
          <div class="comp-card">
            <div class="comp-card-header">Test Taking Realism</div>
            <div class="comp-card-body">
              <div class="comp-option comp-option-coaching">
                <div class="comp-label"><span class="badge-cross">&#10008;</span> Traditional Coaching</div>
                <div>PDF downloads or slow web interfaces without instant comparison</div>
              </div>
              <div class="comp-option comp-option-scale">
                <div class="comp-label"><span class="badge-check">&#10004;</span> Scale Test Series (2026-2027)</div>
                <div><strong>Real Dual Split-Screen Mode</strong>: Question paper on left, instant solutions on right</div>
              </div>
            </div>
          </div>
          <div class="comp-card">
            <div class="comp-card-header">Pricing &amp; Value</div>
            <div class="comp-card-body">
              <div class="comp-option comp-option-coaching">
                <div class="comp-label"><span class="badge-cross">&#10008;</span> Traditional Coaching</div>
                <div>&#8377;12,000 to &#8377;25,000 for just 15 to 20 mock papers</div>
              </div>
              <div class="comp-option comp-option-scale">
                <div class="comp-label"><span class="badge-check">&#10004;</span> Scale Test Series (2026-2027)</div>
                <div><strong>&#8377;999 for all 60 Full-Length Mocks (12,000 Qs)</strong> &bull; Less than &#8377;12 per paper</div>
              </div>
            </div>
          </div>
        </div>"""

if 'class="comparison-cards-mobile"' not in content_norm:
    target_table_end = '        </div>\n      </div>\n    </section>\n\n    <!-- 3 Tiers Progression Section -->'
    replacement_table = '        </div>\n' + mobile_cards_html + '\n      </div>\n    </section>\n\n    <!-- 3 Tiers Progression Section -->'
    if target_table_end in content_norm:
        content_norm = content_norm.replace(target_table_end, replacement_table)
        print("Inserted comparison-cards-mobile HTML!")
    else:
        print("WARNING: target_table_end not found!")

# -------------------------------------------------------------
# 3. Exam Header Redesign (Mobile Alignment & Centering)
# -------------------------------------------------------------
old_exam_header_html = """    <!-- Top Examination Header -->
    <header class="exam-header">
      <div class="exam-header-left">
        <button class="btn-secondary" id="mobileDrawerBtn" onclick="toggleSidebarDrawer()" style="padding: 0.35rem 0.65rem; font-size: 0.78rem; display: none; align-items: center; gap: 5px;">
          <span>&#9776;</span> <strong>Mocks</strong>
        </button>
        <button class="btn-secondary" id="desktopSidebarToggleBtn" onclick="toggleSidebarCollapse()" style="padding: 0.35rem 0.65rem; font-size: 0.78rem; display: inline-flex; align-items: center; gap: 5px;" title="Collapse/Expand Mock List">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
          <span id="sidebarToggleText">Sidebar</span>
        </button>
        <button class="btn-secondary" onclick="showLandingView()" style="padding: 0.35rem 0.65rem; font-size: 0.78rem;">
          &larr; Home
        </button>
        <div style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 0.96rem;" id="currentMockLabel">
          <span>NEET Mock - 01 [Ignite]</span>
        </div>
        <span id="examTierBadge" style="font-size: 0.70rem; font-weight: 700; padding: 0.15rem 0.5rem; border-radius: 9999px; background: #dcfce7; color: #166534;">
          Ignite Tier
        </span>
      </div>

      <div class="exam-header-right">
        <div id="userStatusTag" style="font-size: 0.75rem; font-weight: 700; color: #059669; background: #ecfdf5; padding: 0.2rem 0.55rem; border-radius: 6px; border: 1px solid #a7f3d0;">
          Free Demo
        </div>
        <button class="btn-primary" id="examUnlockBtn" onclick="openPaymentModal()" style="padding: 0.38rem 0.8rem; font-size: 0.78rem;">
          Unlock All 60 Mocks &bull; &#8377;999
        </button>
      </div>
    </header>"""

new_exam_header_html = """    <!-- Top Examination Header - Fully Balanced & Responsive -->
    <header class="exam-header">
      <div class="exam-header-left">
        <button class="btn-secondary" id="mobileDrawerBtn" onclick="toggleSidebarDrawer()" title="Open Mocks List">
          <span>&#9776;</span> <strong>Mocks</strong>
        </button>
        <button class="btn-secondary" id="desktopSidebarToggleBtn" onclick="toggleSidebarCollapse()" title="Collapse/Expand Mock List">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
          <span id="sidebarToggleText">Sidebar</span>
        </button>
        <button class="btn-secondary" id="examHomeBtn" onclick="showLandingView()" title="Back to Home">
          &larr; Home
        </button>
      </div>

      <div class="exam-header-center">
        <div id="currentMockLabel">
          <span>NEET Mock - 01 [Ignite]</span>
        </div>
        <span id="examTierBadge">
          Ignite Tier
        </span>
      </div>

      <div class="exam-header-right">
        <div id="userStatusTag">
          Free Demo
        </div>
        <button class="btn-primary" id="examUnlockBtn" onclick="openPaymentModal()">
          Unlock 60 Mocks &bull; &#8377;999
        </button>
      </div>
    </header>"""

if old_exam_header_html in content_norm:
    content_norm = content_norm.replace(old_exam_header_html, new_exam_header_html)
    print("Replaced exam-header HTML with 3-part layout!")
else:
    print("WARNING: old_exam_header_html not found!")

# -------------------------------------------------------------
# 4. Comprehensive Media Queries (Navbar, Sidebar Drawer, Global Scroll)
# -------------------------------------------------------------
mobile_query_target = """      /* =========================================================
         MOBILE & TABLET ENGINE (<= 900px): NATURAL SCROLL & FULL VIEW
         ========================================================= */"""

# Let's inspect where the mobile query starts
query_end_marker = """      /* Floating Mobile Dock (Always accessible at bottom) */"""

new_responsive_block = """      /* =========================================================
         RESPONSIVE ENGINE: COMPREHENSIVE MOBILE & TABLET RULES
         ========================================================= */
      @media (max-width: 768px) {
        /* 1. Comparison Section: Switch Table to Stacked Cards */
        .comparison-section {
          padding: 1.5rem 0.85rem !important;
          margin: 2rem 0 !important;
        }
        .comparison-table-wrap {
          display: none !important;
        }
        .comparison-cards-mobile {
          display: flex !important;
        }

        /* 2. Global Document-Level Scrolling for Mock Tests */
        body.exam-mode {
          height: auto !important;
          overflow-y: auto !important;
          -webkit-overflow-scrolling: touch;
        }
        #exam-workspace-view {
          display: none;
          height: auto !important;
          min-height: 100vh !important;
          overflow-y: visible !important;
          position: relative !important;
          flex-direction: column !important;
        }
        .exam-main-body {
          height: auto !important;
          min-height: 100% !important;
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
          padding: 0.5rem 0.4rem 6rem 0.4rem !important;
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
          display: block !important;
        }
        .pane-scroll {
          height: auto !important;
          max-height: none !important;
          overflow-y: visible !important;
          overflow-x: hidden !important;
          padding: 0.5rem 0.25rem !important;
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

        /* 3. Mobile Exam Header: Perfectly Balanced & Centered */
        .exam-header {
          display: flex !important;
          align-items: center !important;
          justify-content: space-between !important;
          padding: 0.4rem 0.75rem !important;
          height: 48px !important;
          min-height: 48px !important;
          background: #ffffff !important;
          border-bottom: 1px solid #e2e8f0 !important;
          box-sizing: border-box !important;
          position: relative !important;
        }
        .exam-header-left {
          display: flex !important;
          align-items: center !important;
          gap: 6px !important;
          flex-shrink: 0 !important;
        }
        #desktopSidebarToggleBtn {
          display: none !important;
        }
        #mobileDrawerBtn {
          display: inline-flex !important;
          height: 32px !important;
          padding: 0.25rem 0.55rem !important;
          font-size: 0.76rem !important;
          border-radius: 7px !important;
          align-items: center !important;
          gap: 4px !important;
        }
        #examHomeBtn {
          display: inline-flex !important;
          height: 32px !important;
          padding: 0.25rem 0.55rem !important;
          font-size: 0.76rem !important;
          border-radius: 7px !important;
        }
        .exam-header-center {
          position: absolute !important;
          left: 50% !important;
          transform: translateX(-50%) !important;
          display: flex !important;
          align-items: center !important;
          justify-content: center !important;
          pointer-events: none !important;
          max-width: calc(100% - 190px) !important;
        }
        #currentMockLabel {
          font-size: 0.86rem !important;
          font-weight: 800 !important;
          color: #0f172a !important;
          white-space: nowrap !important;
          text-align: center !important;
          overflow: hidden !important;
          text-overflow: ellipsis !important;
        }
        #examTierBadge {
          display: none !important;
        }
        .exam-header-right {
          display: flex !important;
          align-items: center !important;
          gap: 4px !important;
          flex-shrink: 0 !important;
        }
        #userStatusTag {
          display: none !important;
        }
        #examUnlockBtn {
          height: 32px !important;
          padding: 0.25rem 0.65rem !important;
          font-size: 0.74rem !important;
          white-space: nowrap !important;
          border-radius: 7px !important;
        }

        /* 4. Compact Tabs Header (36px) */
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
          display: none !important;
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

        /* 5. Sidebar Off-Canvas Drawer */
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

        /* 6. Polished Floating Mobile Dock */
        .mobile-floating-dock {
          display: flex !important;
          position: fixed !important;
          bottom: calc(14px + env(safe-area-inset-bottom, 0px)) !important;
          left: 50% !important;
          transform: translateX(-50%) !important;
          z-index: 1000 !important;
          background: rgba(15, 23, 42, 0.94) !important;
          backdrop-filter: blur(12px) !important;
          padding: 5px 8px !important;
          border-radius: 999px !important;
          box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35) !important;
          align-items: center !important;
          gap: 6px !important;
          border: 1px solid rgba(255, 255, 255, 0.18) !important;
        }
        .floating-dock-btn {
          background: rgba(255, 255, 255, 0.12) !important;
          border: none !important;
          color: #ffffff !important;
          font-size: 0.76rem !important;
          font-weight: 700 !important;
          padding: 0.38rem 0.75rem !important;
          border-radius: 999px !important;
          cursor: pointer !important;
          display: inline-flex !important;
          align-items: center !important;
          gap: 4px !important;
          white-space: nowrap !important;
          text-decoration: none !important;
        }
        .floating-dock-btn.primary {
          background: #059669 !important;
          color: #ffffff !important;
        }
        .floating-dock-btn:active {
          transform: scale(0.96) !important;
        }
      }"""

# Find the block from mobile_query_target to the end of .floating-dock-btn.primary
old_responsive_block_regex = r'/\* =========================================================\s+MOBILE & TABLET ENGINE \(<= 900px\): NATURAL SCROLL & FULL VIEW[\s\S]+?\.floating-dock-btn\.primary \{\s+background: #059669 !important;\s+color: #ffffff !important;\s+\}'

if re.search(old_responsive_block_regex, content_norm):
    content_norm = re.sub(old_responsive_block_regex, new_responsive_block, content_norm)
    print("Replaced responsive block with comprehensive Phase 1-6 rules!")
else:
    print("WARNING: old_responsive_block_regex did not match!")

# Desktop styles for exam-header-center
desktop_exam_header_styles = """    .exam-header-center {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    #currentMockLabel {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 0.96rem;
    }
    #examTierBadge {
      font-size: 0.70rem;
      font-weight: 700;
      padding: 0.15rem 0.5rem;
      border-radius: 9999px;
      background: #dcfce7;
      color: #166534;
    }"""

if '.exam-header-center {' not in content_norm:
    content_norm = content_norm.replace(
        '.exam-header-left {',
        desktop_exam_header_styles + '\n    .exam-header-left {'
    )
    print("Added desktop styles for .exam-header-center!")

# Update showExamWorkspace and showLandingView to add/remove exam-mode class
content_norm = content_norm.replace(
    "function showExamWorkspace() {\n      document.getElementById('landing-view').style.display = 'none';",
    "function showExamWorkspace() {\n      document.body.classList.add('exam-mode');\n      document.getElementById('landing-view').style.display = 'none';"
)
content_norm = content_norm.replace(
    "function showLandingView() {\n      document.getElementById('landing-view').style.display = 'block';",
    "function showLandingView() {\n      document.body.classList.remove('exam-mode');\n      document.getElementById('landing-view').style.display = 'block';"
)

for f in files:
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content_norm)
    print(f"Updated {f}")

# Verify Golden Rule
with open(files[0], 'rb') as fh: c1 = fh.read()
with open(files[1], 'rb') as fh: c2 = fh.read()
with open(files[2], 'rb') as fh: c3 = fh.read()

assert c1 == c2 == c3, "Mismatch!"
print("SUCCESS: Complete responsive audit & overhaul applied identically across all 3 files!")

