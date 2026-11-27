with open("mock_tests/index.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

pos_ws = text.find('<div id="exam-workspace-view">')
i = pos_ws
count = 0
found_end = -1
while i < len(text):
    if text[i:i+4] == '<div':
        count += 1
    elif text[i:i+6] == '</div>':
        count -= 1
        if count == 0:
            found_end = i
            break
    i += 1

print("Found end of exam-workspace-view at index:", found_end)
print("Snippet around end:")
print(text[found_end-150:found_end+150])
