with open("mock_tests/index.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

pos_ws = text.find('id="exam-workspace-view"')
# Find closing </div> for exam-workspace-view
pos_end = text.find('<!-- Floating Mobile Quick-Action Dock -->', pos_ws)
if pos_end == -1:
    pos_end = text.find('</body>', pos_ws)

print("Snippet at end of exam-workspace-view:")
print(text[pos_end-600:pos_end+100])
