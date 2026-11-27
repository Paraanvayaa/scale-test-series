with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = 62037
print(text[pos-200:pos+500])
