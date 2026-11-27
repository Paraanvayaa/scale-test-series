import re

files_to_update = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove toggleMobileViewTab and updateFloatingDockState functions
pattern_remove_dock_funcs = r'\s*// Toggle Mobile Floating Dock between Question Paper and Solutions\s*function toggleMobileViewTab\(\)\s*\{.*?function updateFloatingDockState\(\)\s*\{.*?\}'
if re.search(pattern_remove_dock_funcs, content, flags=re.DOTALL):
    content = re.sub(pattern_remove_dock_funcs, '', content, flags=re.DOTALL)
    print("Cleaned up obsolete dock functions!")

# Also check for any standalone updateFloatingDockState
content = re.sub(r'\s*function updateFloatingDockState\(\)\s*\{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'\s*updateFloatingDockState\(\);?', '', content)

# Write to all 3 files
for path in files_to_update:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

# Verify Golden Rule
c = [open(f, 'rb').read() for f in files_to_update]
assert c[0] == c[1] == c[2], "Mismatch!"
print("Golden Rule verified! Length:", len(c[0]))
