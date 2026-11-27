import re

files_to_update = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up old comparison section CSS in content
old_comp_css_pattern = r'/\* =========================================================\s*COMPARISON SECTION STYLES \(DESKTOP & BASE\)\s*========================================================= \*/.*?@media \(min-width: 769px\) \{\s*\.comparison-table-wrap \{\s*display: block !important;\s*\}\s*\.comparison-cards-mobile \{\s*display: none !important;\s*\}\s*\}'
content = re.sub(old_comp_css_pattern, '', content, flags=re.DOTALL)

# Remove any mobile comparison-section overrides in @media (max-width: 768px)
old_mobile_comp = r'/\* 1\. Comparison Section: Stacked Cards \*/\s*\.comparison-section\s*\{.*?\}\s*\.comparison-table-wrap\s*\{.*?\}\s*\.comparison-cards-mobile\s*\{.*?\}'
content = re.sub(old_mobile_comp, '', content, flags=re.DOTALL)

# Also check for remaining .comparison-table-wrap or .comparison-cards-mobile in styles
content = re.sub(r'\.comparison-table-wrap\s*\{[^}]*\}', '', content)
content = re.sub(r'\.comparison-cards-mobile\s*\{[^}]*\}', '', content)

# 2. Modern 2-Column Comparison CSS
new_comp_css = """    /* =========================================================
       THE BRUTAL REALITY: MODERN 2-COLUMN COMPARISON GRID
       ========================================================= */
    .comparison-section {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 20px;
      padding: 3.5rem 2rem;
      margin: 3.5rem auto;
      max-width: 1180px;
      box-shadow: 0 4px 25px -4px rgba(15, 23, 42, 0.06);
      box-sizing: border-box;
    }
    .comparison-badge {
      background: #fee2e2;
      color: #991b1b;
      border: 1px solid #fecaca;
      font-size: 0.76rem;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      padding: 0.3rem 0.85rem;
      border-radius: 9999px;
      display: inline-block;
      margin-bottom: 0.75rem;
    }
    .comparison-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      margin-top: 2.5rem;
      align-items: stretch;
    }
    .comp-column {
      border-radius: 16px;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      position: relative;
      box-sizing: border-box;
    }
    .comp-column-legacy {
      background: #fafaf9;
      border: 1px solid #e7e5e4;
    }
    .comp-column-scale {
      background: #ffffff;
      border: 2px solid #059669;
      box-shadow: 0 10px 30px -5px rgba(5, 150, 105, 0.15);
      position: relative;
    }
    .comp-col-badge-top {
      position: absolute;
      top: -13px;
      left: 50%;
      transform: translateX(-50%);
      background: #059669;
      color: #ffffff;
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      padding: 0.25rem 0.9rem;
      border-radius: 9999px;
      white-space: nowrap;
      box-shadow: 0 2px 8px rgba(5, 150, 105, 0.35);
    }
    .comp-col-header {
      margin-bottom: 1.5rem;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 1.25rem;
    }
    .comp-col-tag {
      font-size: 0.80rem;
      font-weight: 800;
      margin-bottom: 0.35rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .legacy-tag {
      color: #dc2626;
    }
    .scale-tag {
      color: #059669;
    }
    .comp-col-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: #0f172a;
      margin: 0 0 0.35rem 0;
      line-height: 1.25;
    }
    .comp-col-desc {
      font-size: 0.88rem;
      color: #64748b;
      margin: 0;
      line-height: 1.4;
    }
    .comp-list {
      list-style: none;
      padding: 0;
      margin: 0 0 1.5rem 0;
      display: flex;
      flex-direction: column;
      gap: 1.1rem;
      flex: 1;
    }
    .comp-item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 0.90rem;
      line-height: 1.45;
    }
    .comp-icon {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
      font-weight: 800;
      flex-shrink: 0;
      margin-top: 2px;
    }
    .legacy-icon {
      background: #fee2e2;
      color: #dc2626;
    }
    .scale-icon {
      background: #dcfce7;
      color: #15803d;
    }
    .comp-content strong {
      display: block;
      color: #0f172a;
      font-size: 0.92rem;
      margin-bottom: 0.2rem;
      font-weight: 700;
    }
    .comp-content p {
      margin: 0;
      color: #475569;
      font-size: 0.86rem;
      line-height: 1.45;
    }
    .comp-column-scale .comp-content strong {
      color: #047857;
    }
    .comp-cta-wrap {
      margin-top: auto;
      padding-top: 1rem;
    }
    .comp-unlock-btn {
      width: 100%;
      height: 44px;
      border-radius: 9px;
      font-size: 0.92rem;
      font-weight: 800;
      background: #059669;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 12px rgba(5, 150, 105, 0.25);
      border: none;
      cursor: pointer;
      transition: background 0.15s ease, transform 0.15s ease;
    }
    .comp-unlock-btn:hover {
      background: #047857;
      transform: translateY(-1px);
    }

    @media (max-width: 768px) {
      .comparison-section {
        padding: 2rem 1rem !important;
        margin: 2rem 0.5rem !important;
        border-radius: 14px !important;
      }
      .comparison-grid {
        grid-template-columns: 1fr !important;
        gap: 1.75rem !important;
        margin-top: 2rem !important;
      }
      .comp-column {
        padding: 1.25rem 1rem !important;
      }
      .comp-col-title {
        font-size: 1.2rem !important;
      }
      .comp-list {
        gap: 0.9rem !important;
      }
      .comp-item {
        font-size: 0.85rem !important;
      }
      .comp-content strong {
        font-size: 0.88rem !important;
      }
      .comp-content p {
        font-size: 0.82rem !important;
      }
    }"""

# Insert new CSS before `/* =========================================================\n       EXAM HEADER STYLES (DESKTOP & BASE)`
target_marker = '/* =========================================================\n       EXAM HEADER STYLES (DESKTOP & BASE)'
if target_marker in content:
    content = content.replace(target_marker, new_comp_css + '\n\n    ' + target_marker)
else:
    pos_style = content.find('</style>')
    content = content[:pos_style] + '\n' + new_comp_css + '\n' + content[pos_style:]

# 3. Modern 2-Column Comparison HTML
new_comp_html = """      <section class="comparison-section" id="comparison">
        <div class="section-header" style="text-align: center; margin-bottom: 1.5rem;">
          <span class="comparison-badge">The Brutal Reality</span>
          <h2 class="section-title">Why 95% of Coaching Institute Test Series Fail You</h2>
          <p class="section-desc" style="max-width: 680px; margin: 0 auto;">
            Most tuitions and coaching institutes charge &#8377;15,000+ for outdated question banks created by outsourced typists. Here is how Scale Test Series is fundamentally different.
          </p>
        </div>

        <div class="comparison-grid">
          <!-- Card 1: Traditional Coaching -->
          <div class="comp-column comp-column-legacy">
            <div class="comp-col-header">
              <div class="comp-col-tag legacy-tag">&#10008; Traditional Coaching</div>
              <h3 class="comp-col-title">The Outdated Model</h3>
              <p class="comp-col-desc">Recycled question banks sold at premium coaching prices</p>
            </div>
            <ul class="comp-list">
              <li class="comp-item legacy-item">
                <div class="comp-icon legacy-icon">&#10008;</div>
                <div class="comp-content">
                  <strong>Outdated Question Style</strong>
                  <p>80% direct formula-plugging drills out of sync with modern NTA patterns.</p>
                </div>
              </li>
              <li class="comp-item legacy-item">
                <div class="comp-icon legacy-icon">&#10008;</div>
                <div class="comp-content">
                  <strong>Outsourced Content</strong>
                  <p>Aggregated by typists &amp; junior faculty using 10-year-old classroom sheets.</p>
                </div>
              </li>
              <li class="comp-item legacy-item">
                <div class="comp-icon legacy-icon">&#10008;</div>
                <div class="comp-content">
                  <strong>Flat Difficulty Curve</strong>
                  <p>Randomly mixed questions creating false confidence or exam-day panic.</p>
                </div>
              </li>
              <li class="comp-item legacy-item">
                <div class="comp-icon legacy-icon">&#10008;</div>
                <div class="comp-content">
                  <strong>Bare Minimum Solutions</strong>
                  <p>Brief 2-line answer keys with zero explanation of why wrong options fail.</p>
                </div>
              </li>
              <li class="comp-item legacy-item">
                <div class="comp-icon legacy-icon">&#10008;</div>
                <div class="comp-content">
                  <strong>Clunky PDFs &amp; Portals</strong>
                  <p>Static PDF downloads or slow web portals with zero analysis tools.</p>
                </div>
              </li>
              <li class="comp-item legacy-item">
                <div class="comp-icon legacy-icon">&#10008;</div>
                <div class="comp-content">
                  <strong>&#8377;15,000 &ndash; &#8377;25,000 Price</strong>
                  <p>Exorbitant fees for a meager 15 to 20 uncalibrated mock tests.</p>
                </div>
              </li>
            </ul>
          </div>

          <!-- Card 2: Scale Test Series (Featured & Highlighted) -->
          <div class="comp-column comp-column-scale">
            <div class="comp-col-badge-top">Curated by AIIMS Medicos &bull; AIR &lt; 50</div>
            <div class="comp-col-header">
              <div class="comp-col-tag scale-tag">&#10004; Scale Test Series (2026&ndash;2027)</div>
              <h3 class="comp-col-title">The Modern Standard</h3>
              <p class="comp-col-desc">Engineered specifically for the evolving NEET-UG battle</p>
            </div>
            <ul class="comp-list">
              <li class="comp-item scale-item">
                <div class="comp-icon scale-icon">&#10004;</div>
                <div class="comp-content">
                  <strong>Exact 2026 NTA Blueprint</strong>
                  <p>Heavy emphasis on Statement I &amp; II, Assertion-Reason, and Match List matrices.</p>
                </div>
              </li>
              <li class="comp-item scale-item">
                <div class="comp-icon scale-icon">&#10004;</div>
                <div class="comp-content">
                  <strong>Topper &amp; Medico Curated</strong>
                  <p>Handcrafted by Top 50 AIR Rankers and AIIMS New Delhi medical students.</p>
                </div>
              </li>
              <li class="comp-item scale-item">
                <div class="comp-icon scale-icon">&#10004;</div>
                <div class="comp-content">
                  <strong>3 Stepped Scientific Tiers</strong>
                  <p>Ignite (Foundation) &rarr; Conquer (Speed) &rarr; Dominate (Rank Deciders).</p>
                </div>
              </li>
              <li class="comp-item scale-item">
                <div class="comp-icon scale-icon">&#10004;</div>
                <div class="comp-content">
                  <strong>NCERT Line Citations &amp; Distractor Analysis</strong>
                  <p>Instant step-by-step NCERT deconstruction explaining why distractors are wrong.</p>
                </div>
              </li>
              <li class="comp-item scale-item">
                <div class="comp-icon scale-icon">&#10004;</div>
                <div class="comp-content">
                  <strong>Real Dual Split-Screen Engine</strong>
                  <p>View question paper and step-by-step solutions side-by-side with zero lag.</p>
                </div>
              </li>
              <li class="comp-item scale-item">
                <div class="comp-icon scale-icon">&#10004;</div>
                <div class="comp-content">
                  <strong>All 60 Mocks for &#8377;999</strong>
                  <p>12,000 questions across 60 mocks &bull; Less than &#8377;17 per full examination.</p>
                </div>
              </li>
            </ul>
            <div class="comp-cta-wrap">
              <button type="button" class="btn-primary comp-unlock-btn" onclick="openPaymentModal()">
                Unlock All 60 Mocks &bull; &#8377;999 &rarr;
              </button>
            </div>
          </div>
        </div>
      </section>"""

# Replace the old comparison-section HTML
pos_start = content.rfind('<div class="comparison-section"', 0, content.find('The Brutal Reality'))
# Find closing </div>
idx = pos_start
count = 0
found_end = -1
while idx < len(content):
    if content[idx:idx+4] == '<div':
        count += 1
    elif content[idx:idx+6] == '</div>':
        count -= 1
        if count == 0:
            found_end = idx + 6
            break
    idx += 1

print(f"Old comparison section found from {pos_start} to {found_end}")
content = content[:pos_start] + new_comp_html.strip() + content[found_end:]
print("Replaced old comparison section HTML with modern 2-column comparison grid!")

# Write to all 3 files
for p in files_to_update:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {p}")

# Verify Golden Rule
c = [open(f, 'rb').read() for f in files_to_update]
assert c[0] == c[1] == c[2], "Mismatch!"
print("Golden Rule verified! Length:", len(c[0]))

