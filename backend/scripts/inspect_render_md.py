import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('function renderProtectedMarkdown')
print(text[pos:pos+2500])
