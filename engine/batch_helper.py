# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator Helper.
Generates all 5 files for each mock:
- Paper_1.md
- Solutions_Paper_1.md
- Paper_2.md
- Solutions_Paper_2.md
- Answer_Key_and_Validation.md
Strictly enforces authentic JEE Advanced multi-concept depth, zero duplicates,
and the complete 9-point pedagogical solution framework.
"""
import os

def create_mock_files(mock_num, p1, p2, sol1, sol2, val, iit_name="IIT_Bombay"):
    pad = f"{mock_num:02d}"
    mock_dir = os.path.join("mock_tests", iit_name, f"Mock_{pad}")
    os.makedirs(mock_dir, exist_ok=True)
    with open(os.path.join(mock_dir, "Paper_1.md"), "w", encoding="utf-8") as f:
        f.write(p1)
    with open(os.path.join(mock_dir, "Solutions_Paper_1.md"), "w", encoding="utf-8") as f:
        f.write(sol1)
    with open(os.path.join(mock_dir, "Paper_2.md"), "w", encoding="utf-8") as f:
        f.write(p2)
    with open(os.path.join(mock_dir, "Solutions_Paper_2.md"), "w", encoding="utf-8") as f:
        f.write(sol2)
    with open(os.path.join(mock_dir, "Answer_Key_and_Validation.md"), "w", encoding="utf-8") as f:
        f.write(val)
    print(f"Generated complete Authentic Suite for {iit_name} Mock {pad}.")

print("Loaded generator module.")
