import re

files_to_update = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update renderProtectedMarkdown to wrap tables
old_marked_code = """      let html = marked.parse(safeText);

      // Restore Math Tokens
      html = html.replace(/@@@MATH_BLOCK_(\\d+)@@@/g, (match, idx) => mathTokens[parseInt(idx, 10)]);
      html = html.replace(/@@@MATH_INLINE_(\\d+)@@@/g, (match, idx) => mathTokens[parseInt(idx, 10)]);

      containerEl.innerHTML = html;"""

new_marked_code = """      let html = marked.parse(safeText);

      // Restore Math Tokens
      html = html.replace(/@@@MATH_BLOCK_(\\d+)@@@/g, (match, idx) => mathTokens[parseInt(idx, 10)]);
      html = html.replace(/@@@MATH_INLINE_(\\d+)@@@/g, (match, idx) => mathTokens[parseInt(idx, 10)]);

      // Wrap all tables in a touch-friendly, horizontal scrolling responsive wrapper with mobile hint
      html = html.replace(/<table(\\s*[^>]*)>/gi, '<div class="table-scroll-hint">&#8644; Scroll horizontally to view full matrix &amp; topics</div><div class="table-responsive"><table$1>');
      html = html.replace(/<\\/table>/gi, '</table></div>');

      containerEl.innerHTML = html;"""

if old_marked_code in content:
    content = content.replace(old_marked_code, new_marked_code)
    print("Wrapped tables in table-responsive in renderProtectedMarkdown!")
else:
    # Try regex match
    pattern = r'(let html = marked\.parse\(safeText\);[\s\S]*?containerEl\.innerHTML = html;)'
    def repl(m):
        block = m.group(1)
        if 'table-responsive' not in block:
            return block.replace(
                'containerEl.innerHTML = html;',
                '// Wrap all tables in a touch-friendly, horizontal scrolling responsive wrapper with mobile hint\n      html = html.replace(/<table(\\s*[^>]*)>/gi, \'<div class="table-scroll-hint">&#8644; Scroll horizontally to view full matrix &amp; topics</div><div class="table-responsive"><table$1>\');\n      html = html.replace(/<\\/table>/gi, \'</table></div>\');\n\n      containerEl.innerHTML = html;'
            )
        return block
    content = re.sub(pattern, repl, content, count=1)
    print("Wrapped tables via regex replacer!")

# 2. Add base table-responsive CSS
old_table_css = """    /* High-Fidelity Tables: Match Lists & Answer Key */
    table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      margin: 1rem 0 1.35rem 0;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
      font-size: 0.92rem !important;
    }"""

new_table_css = """    /* High-Fidelity Tables: Match Lists & Answer Key */
    .table-scroll-hint {
      display: none;
      font-size: 0.74rem;
      font-weight: 700;
      color: #059669;
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      padding: 0.28rem 0.65rem;
      border-radius: 6px;
      margin: 0.85rem 0 0.4rem 0;
      align-items: center;
      gap: 6px;
      width: fit-content;
    }
    .table-responsive {
      width: 100%;
      max-width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin: 0.5rem 0 1.5rem 0;
      border: 1px solid #cbd5e1;
      border-radius: 10px;
      background: #ffffff;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
      position: relative;
      box-sizing: border-box;
    }
    .table-responsive::-webkit-scrollbar {
      height: 6px;
    }
    .table-responsive::-webkit-scrollbar-track {
      background: #f1f5f9;
      border-radius: 4px;
    }
    .table-responsive::-webkit-scrollbar-thumb {
      background: #059669;
      border-radius: 4px;
    }
    .table-responsive table {
      width: 100%;
      min-width: 640px; /* Guarantees all 5 columns (Q.No, Subject, Option, Question Type, Topic) are fully readable */
      border-collapse: separate;
      border-spacing: 0;
      margin: 0;
      background: #ffffff;
      border: none;
      box-shadow: none;
      border-radius: 0;
      font-size: 0.90rem !important;
    }
    table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      margin: 1rem 0 1.35rem 0;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
      font-size: 0.92rem !important;
    }"""

if old_table_css in content:
    content = content.replace(old_table_css, new_table_css)
    print("Added table-responsive and table-scroll-hint base CSS!")
else:
    print("Searching table base CSS with alternative...")
    content = content.replace('/* High-Fidelity Tables: Match Lists & Answer Key */\n    table {', new_table_css.replace('table {', ''))

# 3. Add responsive table rules in @media (max-width: 768px)
mobile_table_css = """      .table-scroll-hint {
        display: inline-flex !important;
      }
      .table-responsive {
        margin: 0.65rem 0 1.25rem 0 !important;
        border-radius: 8px !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
      }
      .table-responsive table {
        min-width: 620px !important;
      }
      .table-responsive th {
        padding: 0.55rem 0.75rem !important;
        font-size: 0.78rem !important;
        white-space: nowrap !important;
      }
      .table-responsive td {
        padding: 0.55rem 0.75rem !important;
        font-size: 0.85rem !important;
      }"""

if '.table-scroll-hint {' not in content.split('@media (max-width: 768px)')[1]:
    marker = '@media (max-width: 768px) {'
    content = content.replace(marker, marker + '\n' + mobile_table_css, 1)
    print("Added responsive table rules to @media (max-width: 768px)!")

# Write to all 3 files
for p in files_to_update:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {p}")

# Verify Golden Rule
c = [open(f, 'rb').read() for f in files_to_update]
assert c[0] == c[1] == c[2], "Mismatch!"
print("Golden Rule verified! Length:", len(c[0]))

