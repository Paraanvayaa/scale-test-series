import re
import subprocess
import os

with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', text, re.DOTALL)
for i, s in enumerate(scripts):
    if '@context' in s:
        print(f"Script #{i} is JSON-LD schema, skipping.")
        continue
    with open(f'temp_script_{i}.js', 'w', encoding='utf-8') as tf:
        tf.write(s)
    res = subprocess.run(['node', '-c', f'temp_script_{i}.js'], capture_output=True, text=True)
    print(f"Script #{i} syntax check exit code: {res.returncode}")
    if res.returncode != 0:
        print("ERROR:", res.stderr)
        exit(1)
    else:
        print("PASS: Main application JavaScript syntax is 100% valid with 0 errors!")
    if os.path.exists(f'temp_script_{i}.js'):
        os.remove(f'temp_script_{i}.js')

print("ALL JS SYNTAX VALIDATION PASSED!")

