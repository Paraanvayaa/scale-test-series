import urllib.request
import subprocess

html = urllib.request.urlopen('https://scaletestseries.web.app/').read().decode('utf-8', errors='ignore')

import re
scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', html, re.DOTALL)
for i, s in enumerate(scripts):
    if '@context' in s:
        continue
    with open('live_test.js', 'w', encoding='utf-8') as f:
        f.write(s)
    res = subprocess.run(['node', '-c', 'live_test.js'], capture_output=True, text=True)
    print(f"Live Script #{i} syntax exit code: {res.returncode}")
    if res.returncode == 0:
        print("PASS: Live site JavaScript syntax is 100% valid with 0 errors!")
    else:
        print("ERROR:", res.stderr)

