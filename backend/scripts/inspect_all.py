import re

with open("mock_tests/index.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("File length:", len(text))

# Check for floating dock
print("Has mobileFloatingDock:", "mobileFloatingDock" in text)
print("Has toggleMobileViewTab:", "toggleMobileViewTab" in text)

# Check media query nesting
pos_360 = text.find("@media (max-width: 360px)")
pos_768 = text.find("@media (max-width: 768px)", pos_360 if pos_360 != -1 else 0)
print("pos_360:", pos_360, "pos_768:", pos_768)

if pos_360 != -1 and pos_768 != -1:
    slice_text = text[pos_360:pos_768]
    print("Braces between 360 and 768 -> open:", slice_text.count("{"), "close:", slice_text.count("}"))

# Check exam-workspace-view parent and styles
pos_ws = text.find('id="exam-workspace-view"')
if pos_ws != -1:
    print("\n--- HTML snippet around exam-workspace-view ---")
    print(text[pos_ws-150:pos_ws+350])

# Check tabs header HTML
pos_tabs = text.find('class="tabs-header"')
if pos_tabs != -1:
    print("\n--- HTML snippet around tabs-header ---")
    print(text[pos_tabs:pos_tabs+600])

# Check footer HTML
pos_ft = text.find('class="site-footer"')
if pos_ft != -1:
    print("\n--- HTML snippet around site-footer ---")
    print(text[pos_ft:pos_ft+400])

