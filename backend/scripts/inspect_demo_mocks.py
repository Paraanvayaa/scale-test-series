with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [line.strip() for line in text.splitlines() if 'DEMO_MOCKS' in line or 'prewarmDemoMocks' in line]
for m in matches:
    print(m)

