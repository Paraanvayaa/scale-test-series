with open("mock_tests/index.html", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'function toggleSidebarDrawer' in line:
        for j in range(max(0, i-2), min(len(lines), i+20)):
            print(f'{j}: {lines[j]}', end='')
