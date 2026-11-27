with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('let html = marked.parse(safeText);')
print(text[pos-200:pos+500])
