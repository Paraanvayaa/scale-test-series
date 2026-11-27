with open('mock_tests/demo_mocks.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('Mock_21_Answer_Key_and_Analysis.md')
print(text[pos:pos+1500])
