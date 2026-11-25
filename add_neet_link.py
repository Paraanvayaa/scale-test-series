with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<div class="header-actions">'
replacement = '<div class="header-actions">\n      <a href="/neet/index.html" class="action-btn" style="background: #059669; color: white; border: none; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 0.4rem;"><span>🩺</span> NEET (UG) Series (20 Mocks) &rarr;</a>'

if target in html and '/neet/index.html' not in html:
    html = html.replace(target, replacement)
    with open('mock_tests/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated mock_tests/index.html with link to NEET portal')
else:
    print('Already updated or target not found')

