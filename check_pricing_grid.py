with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

p = text.find('.pricing-grid {')
print(text[p:p+400].encode('ascii', 'backslashreplace').decode('ascii'))

