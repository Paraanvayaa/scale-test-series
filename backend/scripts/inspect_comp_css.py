with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'\.col-feature', text)]
print("Occurrences of .col-feature at:", matches)
for pos in matches:
    print("--- at", pos, "---")
    print(text[pos-100:pos+300])
