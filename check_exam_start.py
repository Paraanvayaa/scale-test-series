with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

p = text.find('id="exam-workspace-view"')
print(text[p-200:p+50].encode('ascii', 'backslashreplace').decode('ascii'))

