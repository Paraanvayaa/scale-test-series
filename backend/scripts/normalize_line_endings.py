with open('mock_tests/index.html', 'rb') as f:
    raw = f.read()

# Normalize CRLF to LF
normalized = raw.replace(b'\r\n', b'\n')
with open('mock_tests/index.html', 'wb') as f:
    f.write(normalized)

print("Normalized mock_tests/index.html to LF. Length:", len(normalized))
