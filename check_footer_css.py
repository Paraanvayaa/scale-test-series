with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'class="([^"]*footer[^"]*)"', text)
print("Footer classes:", set(matches))
p = text.find('.site-footer')
if p != -1:
    print(text[p:p+400].encode('ascii', 'backslashreplace').decode('ascii'))

