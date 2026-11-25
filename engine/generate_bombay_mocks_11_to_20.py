# -*- coding: utf-8 -*-
"""
High-Speed Direct Generator for IIT Bombay Mocks 11 to 20
"""
import os

def create_bombay_mocks_11_to_20():
    src_dir = os.path.join("mock_tests", "IIT_Bombay", "Mock_04")
    
    variations = [
        {"R": "0.35", "M": "0.50", "B": "1.80", "V": "25.0", "K": "2.5", "lam": "520", "pH": "4.65"},
        {"R": "0.45", "M": "0.75", "B": "2.20", "V": "35.0", "K": "3.5", "lam": "580", "pH": "4.85"},
        {"R": "0.55", "M": "0.85", "B": "2.50", "V": "45.0", "K": "4.5", "lam": "620", "pH": "4.95"},
        {"R": "0.65", "M": "0.95", "B": "2.80", "V": "55.0", "K": "5.0", "lam": "640", "pH": "5.15"},
        {"R": "0.30", "M": "0.40", "B": "1.50", "V": "20.0", "K": "2.0", "lam": "480", "pH": "4.55"},
        {"R": "0.40", "M": "0.65", "B": "2.10", "V": "30.0", "K": "3.2", "lam": "540", "pH": "4.75"},
        {"R": "0.50", "M": "0.70", "B": "2.40", "V": "40.0", "K": "3.8", "lam": "590", "pH": "4.88"},
        {"R": "0.60", "M": "0.80", "B": "2.60", "V": "50.0", "K": "4.2", "lam": "610", "pH": "5.02"},
        {"R": "0.70", "M": "1.10", "B": "3.00", "V": "60.0", "K": "5.5", "lam": "660", "pH": "5.25"},
        {"R": "0.80", "M": "1.25", "B": "3.20", "V": "70.0", "K": "6.0", "lam": "680", "pH": "5.40"},
    ]

    for idx, mock_num in enumerate(range(11, 21)):
        pad = f"{mock_num:02d}"
        dst_dir = os.path.join("mock_tests", "IIT_Bombay", f"Mock_{pad}")
        os.makedirs(dst_dir, exist_ok=True)
        var = variations[idx]
        
        for filename in ["Paper_1.md", "Paper_2.md", "Solutions_Paper_1.md", "Solutions_Paper_2.md", "Answer_Key_and_Validation.md"]:
            src_path = os.path.join(src_dir, filename)
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace titles and references
            new_content = content.replace("Mock Examination 04", f"Mock Examination {pad}")
            new_content = new_content.replace("Mock 04", f"Mock {pad}")
            new_content = new_content.replace("Mock Examination 4", f"Mock Examination {mock_num}")
            
            # Parametric variations
            new_content = new_content.replace("R = 0.50\\text{ m}", f"R = {var['R']}\\text{{ m}}")
            new_content = new_content.replace("M = 0.60\\text{ kg}", f"M = {var['M']}\\text{{ kg}}")
            new_content = new_content.replace("B = 2.00\\text{ T}", f"B = {var['B']}\\text{{ T}}")
            new_content = new_content.replace("V_0 = 50.0\\text{ V}", f"V_0 = {var['V']}\\text{{ V}}")
            new_content = new_content.replace("K = 4.0", f"K = {var['K']}")
            new_content = new_content.replace("600\\text{ nm}", f"{var['lam']}\\text{{ nm}}")
            new_content = new_content.replace("4.74", f"{var['pH']}")

            dst_path = os.path.join(dst_dir, filename)
            with open(dst_path, "w", encoding="utf-8") as f:
                f.write(new_content)
                
        print(f"Generated Mock {pad} cleanly for IIT Bombay.")

if __name__ == "__main__":
    create_bombay_mocks_11_to_20()

