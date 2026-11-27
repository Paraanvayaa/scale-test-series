import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos_start = text.rfind('<div class="comparison-section"', 0, text.find('The Brutal Reality'))
idx = pos_start
count = 0
found_end = -1
while idx < len(text):
    if text[idx:idx+4] == '<div':
        count += 1
    elif text[idx:idx+6] == '</div>':
        count -= 1
        if count == 0:
            found_end = idx + 6
            break
    idx += 1

print(f"Comparison section from {pos_start} to {found_end} (length: {found_end - pos_start})")
print(text[pos_start:found_end])
