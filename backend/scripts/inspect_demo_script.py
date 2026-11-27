with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'demo_mocks.js' in line:
        for j in range(max(0, i-5), min(len(lines), i+10)):
            print(f"{j}: {lines[j]}", end='')
