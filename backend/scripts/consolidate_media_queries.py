import re

files_to_update = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find the media query inside the comparison section CSS and move it into the main responsive engine block
media_comp_pattern = r'@media\s*\(\s*max-width:\s*768px\s*\)\s*\{\s*\.comparison-section\s*\{[^}]*\}\s*\.comparison-grid\s*\{[^}]*\}\s*\.comp-column\s*\{[^}]*\}\s*\.comp-col-title\s*\{[^}]*\}\s*\.comp-list\s*\{[^}]*\}\s*\.comp-item\s*\{[^}]*\}\s*\.comp-content\s*strong\s*\{[^}]*\}\s*\.comp-content\s*p\s*\{[^}]*\}\s*\}'

match = re.search(media_comp_pattern, content)
if match:
    comp_media_rules = """      /* The Brutal Reality: Mobile 2-Column Comparison Stack */
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
      }"""
    content = content[:match.start()] + content[match.end():]
    # insert inside the main responsive engine block
    main_marker = '/* =========================================================\n       RESPONSIVE ENGINE: COMPREHENSIVE MOBILE RULES (<= 768px)\n       ========================================================= */\n    @media (max-width: 768px) {'
    content = content.replace(main_marker, main_marker + '\n' + comp_media_rules)
    print("Consolidated comparison media query into main responsive engine!")

for p in files_to_update:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {p}")

c = [open(f, 'rb').read() for f in files_to_update]
assert c[0] == c[1] == c[2], "Mismatch!"
print("Golden Rule verified! Length:", len(c[0]))
