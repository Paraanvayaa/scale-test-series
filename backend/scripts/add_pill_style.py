import re

files = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

pill_css_target = """    #navUnlockBtn {
      height: 34px;
      box-sizing: border-box;
      padding: 0.35rem 0.85rem;
      font-size: 0.82rem;
      border-radius: 7px;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
    }"""

pill_css_replacement = """    #navUnlockBtn {
      height: 34px;
      box-sizing: border-box;
      padding: 0.35rem 0.85rem;
      font-size: 0.82rem;
      border-radius: 7px;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
    }
    .profile-pill-btn {
      height: 34px;
      box-sizing: border-box;
      display: inline-flex;
      align-items: center;
    }"""

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(pill_css_target, pill_css_replacement)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

# Verify Golden Rule
with open(files[0], 'rb') as f: c1 = f.read()
with open(files[1], 'rb') as f: c2 = f.read()
with open(files[2], 'rb') as f: c3 = f.read()

assert c1 == c2 == c3, "Mismatch!"
print("SUCCESS: Golden rule verified!")

