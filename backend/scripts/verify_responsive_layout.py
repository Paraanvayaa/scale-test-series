with open("mock_tests/index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

import re
errors = []

# 1. Total CSS brace check
style_blocks = []
start = 0
while True:
    s_open = html.find('<style', start)
    if s_open == -1:
        break
    s_close = html.find('</style>', s_open)
    if s_close == -1:
        break
    style_content = html[s_open:s_close]
    style_blocks.append(style_content)
    start = s_close + 8

for idx, block in enumerate(style_blocks):
    open_c = block.count('{')
    close_c = block.count('}')
    print(f"Style Block #{idx+1}: {open_c} open braces, {close_c} close braces. Balance: {open_c - close_c}")
    if open_c != close_c:
        errors.append(f"Style block #{idx+1} has brace mismatch: {open_c} vs {close_c}")

# 2. Check absence of unwanted elements
if 'id="mobileFloatingDock"' in html or 'mobile-floating-dock' in html:
    errors.append("ERROR: mobileFloatingDock still exists in HTML!")
else:
    print("PASS: mobileFloatingDock completely removed.")

# 3. Check exam-header structure
if 'exam-header-row-1' in html and 'exam-header-row-2' in html:
    print("PASS: 2-row exam-header markup verified.")
else:
    errors.append("ERROR: 2-row exam-header markup missing!")

# 4. Check comparison section
if 'comparison-grid' in html and 'comp-column-legacy' in html and 'comp-column-scale' in html:
    print("PASS: Modern 2-column comparison grid markup verified.")
else:
    errors.append("ERROR: Comparison grid markup missing!")

# 5. Check CSS rules in the main responsive block
pos_matches = [m.start() for m in re.finditer(r'@media\s*\(\s*max-width:\s*768px\s*\)', html)]
if len(pos_matches) >= 2:
    css_768 = html[pos_matches[1]:pos_matches[1] + 12000]
    required_rules = [
        '.exam-sidebar',
        'transform: translateX(-100%)',
        '#desktopSidebarToggleBtn',
        'display: none',
        '#mobileDrawerBtn',
        'display: inline-flex',
        '.pane-scroll',
        'overflow: visible',
        'height: auto',
        '.footer-container',
        'grid-template-columns: 1fr'
    ]
    for r in required_rules:
        if r in css_768:
            print(f"PASS: Found rule '{r}' in responsive engine @media (max-width: 768px)")
        else:
            errors.append(f"ERROR: Missing rule '{r}' in responsive engine @media (max-width: 768px)")
else:
    errors.append("ERROR: Second @media (max-width: 768px) block not found!")

# 6. Verify Golden Rule
files = ['mock_tests/index.html', 'mock_tests/neet/index.html', 'neet_mock_tests/index.html']
contents = [open(f, 'rb').read() for f in files]
if contents[0] == contents[1] == contents[2]:
    print(f"PASS: Golden Rule verified! All 3 files identical ({len(contents[0])} bytes).")
else:
    errors.append("ERROR: Golden Rule mismatch between files!")

if errors:
    print("\nFAILED with errors:")
    for e in errors:
        print(" -", e)
    exit(1)
else:
    print("\nALL RESPONSIVE AUDIT & VERIFICATION CHECKS PASSED PERFECTLY!")
