import re

files_to_update = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken trailing syntax
bad_snippet = """      if (left) left.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #64748b;">No active examination loaded.</div>';
      if (right) right.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #64748b;">No active solutions loaded.</div>';
    } else {
        label.innerHTML = 'Solutions &rarr;';
      }
    }"""

good_snippet = """      if (left) left.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #64748b;">No active examination loaded.</div>';
      if (right) right.innerHTML = '<div style="padding: 2.5rem; text-align: center; color: #64748b;">No active solutions loaded.</div>';
    }"""

if bad_snippet in content:
    content = content.replace(bad_snippet, good_snippet)
    print("Fixed bad syntax snippet in clearActiveDocuments!")
else:
    print("Searching with regex...")
    content = re.sub(
        r"if \(right\) right\.innerHTML = '<div style=\"padding: 2\.5rem; text-align: center; color: #64748b;\">No active solutions loaded\.</div>';\s*\}\s*else\s*\{\s*label\.innerHTML\s*=\s*'Solutions &rarr;';\s*\}\s*\}",
        "if (right) right.innerHTML = '<div style=\"padding: 2.5rem; text-align: center; color: #64748b;\">No active solutions loaded.</div>';\n    }",
        content
    )
    print("Replaced with regex!")

# Write to all 3 files
for p in files_to_update:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {p}")

# Verify Golden Rule
c = [open(f, 'rb').read() for f in files_to_update]
assert c[0] == c[1] == c[2], "Mismatch!"
print("Golden Rule verified! Length:", len(c[0]))

