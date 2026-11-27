with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [line.strip() for line in text.splitlines() if 'showExamWorkspace' in line or 'selectMock' in line or 'Launch' in line or 'Demo Mocks' in line]
for m in matches:
    print(m[:120])
