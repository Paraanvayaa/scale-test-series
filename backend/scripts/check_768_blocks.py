with open("mock_tests/index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer(r'@media\s*\(\s*max-width:\s*768px\s*\)', html)]
print("Found @media (max-width: 768px) at indices:", matches)
for i, pos in enumerate(matches):
    print(f"--- Block #{i+1} at index {pos} ---")
    print(html[pos:pos+300])
