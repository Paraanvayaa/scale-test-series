import re

files_to_update = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

comp_css_block = """    /* =========================================================
       COMPARISON SECTION STYLES (DESKTOP & BASE)
       ========================================================= */
    .comparison-section {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 3rem 2rem;
      margin: 3.5rem 0;
      box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);
    }
    .comparison-table-wrap {
      overflow-x: auto;
      margin-top: 2rem;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .comparison-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.92rem;
    }
    .comparison-table th {
      padding: 1rem 1.25rem;
      font-weight: 700;
      border-bottom: 2px solid #e2e8f0;
    }
    .comparison-table td {
      padding: 1.1rem 1.25rem;
      border-bottom: 1px solid #f1f5f9;
      vertical-align: middle;
      line-height: 1.5;
    }
    .comparison-table tr:last-child td {
      border-bottom: none;
    }
    .comparison-table .col-feature {
      width: 25%;
      font-weight: 700;
      color: #0f172a;
      background: #f8fafc;
    }
    .comparison-table .col-coaching {
      width: 37.5%;
      color: #475569;
      background: #fffafa;
    }
    .comparison-table .col-scale {
      width: 37.5%;
      color: #0f172a;
      background: #f0fdf4;
      font-weight: 500;
    }
    .comparison-table th.col-feature {
      background: #f1f5f9;
      color: #334155;
    }
    .comparison-table th.col-coaching {
      background: #fef2f2;
      color: #dc2626;
      border-bottom-color: #fecaca;
    }
    .comparison-table th.col-scale {
      background: #ecfdf5;
      color: #059669;
      border-bottom-color: #a7f3d0;
    }
    .badge-cross {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #fee2e2;
      color: #dc2626;
      font-size: 0.75rem;
      font-weight: bold;
      margin-right: 6px;
    }
    .badge-check {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #dcfce7;
      color: #16a34a;
      font-size: 0.75rem;
      font-weight: bold;
      margin-right: 6px;
    }

    /* Mobile comparison cards: STRICTLY HIDDEN ON DESKTOP */
    .comparison-cards-mobile {
      display: none !important;
      flex-direction: column;
      gap: 1.25rem;
      margin-top: 1.5rem;
    }
    .comp-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .comp-card-header {
      background: #0f172a;
      color: #ffffff;
      padding: 0.75rem 1rem;
      font-weight: 800;
      font-size: 0.92rem;
      letter-spacing: 0.01em;
    }
    .comp-card-body {
      padding: 0.85rem;
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
      background: #fff5f5;
      border: 1px solid #fed7d7;
      color: #742a2a;
    }
    .comp-option-scale {
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #14532d;
    }
    .comp-label {
      font-weight: 700;
      font-size: 0.82rem;
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .comp-option-coaching .comp-label {
      color: #dc2626;
    }
    .comp-option-scale .comp-label {
      color: #15803d;
    }

    @media (min-width: 769px) {
      .comparison-table-wrap {
        display: block !important;
      }
      .comparison-cards-mobile {
        display: none !important;
      }
    }
"""

# Insert comp_css_block right before `/* =========================================================\n       EXAM HEADER STYLES (DESKTOP & BASE)`
target_marker = '/* =========================================================\n       EXAM HEADER STYLES (DESKTOP & BASE)'
if target_marker in content:
    content = content.replace(target_marker, comp_css_block + '\n    ' + target_marker)
    print("Inserted comparison CSS before exam header styles!")
else:
    # Alternative: insert before </style>
    pos_style = content.find('</style>')
    content = content[:pos_style] + '\n' + comp_css_block + '\n' + content[pos_style:]
    print("Inserted comparison CSS before </style>!")

# Write to all 3 files
for p in files_to_update:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {p}")

# Verify Golden Rule
c = [open(f, 'rb').read() for f in files_to_update]
assert c[0] == c[1] == c[2], "Mismatch!"
print("Golden Rule verified! Length:", len(c[0]))

