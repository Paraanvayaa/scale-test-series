with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

for func_name in ['function launchDemoTest', 'function showExamWorkspace', 'function selectMock']:
    pos = text.find(func_name)
    if pos != -1:
        print(f"=== {func_name} ===")
        print(text[pos:pos+600])
        print('-'*50)
