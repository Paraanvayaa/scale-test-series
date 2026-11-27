with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('function apiRequest')
if pos == -1:
    pos = text.find('apiRequest')

print(text[pos-100:pos+800])
