with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
pos = text.find('function setViewMode')
print(text[pos:pos+2000])

