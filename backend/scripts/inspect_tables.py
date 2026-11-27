with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

print("=== Base Table Styles at 37533 ===")
print(text[37450:38500])

print("\n=== Responsive Table Styles at 62896 ===")
print(text[62850:63400])
