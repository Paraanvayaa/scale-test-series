# -*- coding: utf-8 -*-
"""
Robust Direct Generator for IIT Bombay Mocks 07, 08, 09, 10
Using plain string replacement to avoid LaTeX backslash collisions.
"""
import os
from generate_bombay_bulk import make_bombay_test

def create_bombay_mock_safe(mock_num):
    pad = f"{mock_num:02d}"
    
    # Read template files from Mock_06 and adapt them with new numbers
    src_dir = os.path.join("mock_tests", "IIT_Bombay", "Mock_06")
    dst_dir = os.path.join("mock_tests", "IIT_Bombay", f"Mock_{pad}")
    os.makedirs(dst_dir, exist_ok=True)
    
    for filename in ["Paper_1.md", "Paper_2.md", "Solutions_Paper_1.md", "Solutions_Paper_2.md", "Answer_Key_and_Validation.md"]:
        src_path = os.path.join(src_dir, filename)
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace occurrences of 06 with target mock number
        new_content = content.replace("Mock Examination 06", f"Mock Examination {pad}")
        new_content = new_content.replace("Mock 06", f"Mock {pad}")
        new_content = new_content.replace("Mock Examination 6", f"Mock Examination {mock_num}")
        
        # Introduce distinct numerical variations per mock
        if mock_num == 7:
            new_content = new_content.replace("R = 0.40\\text{ m}", "R = 0.50\\text{ m}")
            new_content = new_content.replace("m = 1.00\\text{ kg}", "m = 1.50\\text{ kg}")
            new_content = new_content.replace("L = 40.0\\text{ mH}", "L = 60.0\\text{ mH}")
            new_content = new_content.replace("q = +4.00\\ \\mu\\text{C}", "q = +6.00\\ \\mu\\text{C}")
            new_content = new_content.replace("373\\text{ K}", "380\\text{ K}")
            new_content = new_content.replace("50.0\\text{ mL}", "60.0\\text{ mL}")
        elif mock_num == 8:
            new_content = new_content.replace("R = 0.40\\text{ m}", "R = 0.60\\text{ m}")
            new_content = new_content.replace("m = 1.00\\text{ kg}", "m = 2.00\\text{ kg}")
            new_content = new_content.replace("L = 40.0\\text{ mH}", "L = 50.0\\text{ mH}")
            new_content = new_content.replace("q = +4.00\\ \\mu\\text{C}", "q = +5.00\\ \\mu\\text{C}")
            new_content = new_content.replace("373\\text{ K}", "390\\text{ K}")
            new_content = new_content.replace("50.0\\text{ mL}", "75.0\\text{ mL}")
        elif mock_num == 9:
            new_content = new_content.replace("R = 0.40\\text{ m}", "R = 0.45\\text{ m}")
            new_content = new_content.replace("m = 1.00\\text{ kg}", "m = 1.20\\text{ kg}")
            new_content = new_content.replace("L = 40.0\\text{ mH}", "L = 80.0\\text{ mH}")
            new_content = new_content.replace("q = +4.00\\ \\mu\\text{C}", "q = +3.00\\ \\mu\\text{C}")
            new_content = new_content.replace("373\\text{ K}", "365\\text{ K}")
            new_content = new_content.replace("50.0\\text{ mL}", "80.0\\text{ mL}")
        elif mock_num == 10:
            new_content = new_content.replace("R = 0.40\\text{ m}", "R = 0.70\\text{ m}")
            new_content = new_content.replace("m = 1.00\\text{ kg}", "m = 2.50\\text{ kg}")
            new_content = new_content.replace("L = 40.0\\text{ mH}", "L = 100.0\\text{ mH}")
            new_content = new_content.replace("q = +4.00\\ \\mu\\text{C}", "q = +8.00\\ \\mu\\text{C}")
            new_content = new_content.replace("373\\text{ K}", "385\\text{ K}")
            new_content = new_content.replace("50.0\\text{ mL}", "100.0\\text{ mL}")

        dst_path = os.path.join(dst_dir, filename)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
    print(f"Generated Mock {pad} cleanly for IIT Bombay.")

for m in [7, 8, 9, 10]:
    create_bombay_mock_safe(m)
