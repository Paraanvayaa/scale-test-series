with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [line.strip() for line in text.splitlines() if any(k in line.lower() for k in ['launch', 'mock test', 'demo mock']) and ('button' in line or 'onclick' in line or '<a' in line)]
for m in matches:
    print(m)
