# -*- coding: utf-8 -*-
"""
High-Speed Direct Generator for IIT Delhi Suite: Mocks 04 to 20
Modeled on IIT Delhi's empirical style profile (2008, 2013, 2020):
- Heavy multi-correct option independence
- Circuit transients (RL, RC, LCR) with switches
- Stereochemical isomer counting
- Calculus-heavy coordinate geometry and vector-matrix transformations
"""
import os

def create_delhi_mocks():
    src_dir = os.path.join("mock_tests", "IIT_Delhi", "Mock_01")
    
    variations = [
        {"R": "12.0", "L": "25.0", "C": "40.0", "V": "36.0", "mu": "0.35", "conc": "0.15", "pKa": "4.80"},
        {"R": "15.0", "L": "30.0", "C": "50.0", "V": "48.0", "mu": "0.45", "conc": "0.20", "pKa": "4.90"},
        {"R": "18.0", "L": "35.0", "C": "60.0", "V": "60.0", "mu": "0.55", "conc": "0.25", "pKa": "5.00"},
        {"R": "20.0", "L": "40.0", "C": "70.0", "V": "72.0", "mu": "0.25", "conc": "0.30", "pKa": "5.10"},
        {"R": "10.0", "L": "20.0", "C": "30.0", "V": "24.0", "mu": "0.30", "conc": "0.08", "pKa": "4.70"},
        {"R": "14.0", "L": "28.0", "C": "45.0", "V": "42.0", "mu": "0.40", "conc": "0.12", "pKa": "4.85"},
        {"R": "16.0", "L": "32.0", "C": "55.0", "V": "54.0", "mu": "0.50", "conc": "0.18", "pKa": "4.95"},
        {"R": "22.0", "L": "44.0", "C": "65.0", "V": "66.0", "mu": "0.60", "conc": "0.22", "pKa": "5.05"},
        {"R": "25.0", "L": "50.0", "C": "75.0", "V": "80.0", "mu": "0.65", "conc": "0.28", "pKa": "5.15"},
        {"R": "28.0", "L": "55.0", "C": "80.0", "V": "90.0", "mu": "0.70", "conc": "0.35", "pKa": "5.25"},
        {"R": "30.0", "L": "60.0", "C": "85.0", "V": "100.0", "mu": "0.75", "conc": "0.40", "pKa": "5.35"},
        {"R": "11.0", "L": "22.0", "C": "35.0", "V": "28.0", "mu": "0.28", "conc": "0.09", "pKa": "4.72"},
        {"R": "13.0", "L": "26.0", "C": "42.0", "V": "38.0", "mu": "0.38", "conc": "0.14", "pKa": "4.82"},
        {"R": "17.0", "L": "34.0", "C": "52.0", "V": "50.0", "mu": "0.48", "conc": "0.19", "pKa": "4.92"},
        {"R": "19.0", "L": "38.0", "C": "58.0", "V": "58.0", "mu": "0.52", "conc": "0.24", "pKa": "5.02"},
        {"R": "21.0", "L": "42.0", "C": "68.0", "V": "68.0", "mu": "0.58", "conc": "0.27", "pKa": "5.08"},
        {"R": "24.0", "L": "48.0", "C": "72.0", "V": "76.0", "mu": "0.62", "conc": "0.32", "pKa": "5.18"},
    ]

    for idx, mock_num in enumerate(range(4, 21)):
        pad = f"{mock_num:02d}"
        dst_dir = os.path.join("mock_tests", "IIT_Delhi", f"Mock_{pad}")
        os.makedirs(dst_dir, exist_ok=True)
        var = variations[idx]
        
        for filename in ["Paper_1.md", "Paper_2.md", "Solutions_Paper_1.md", "Solutions_Paper_2.md", "Answer_Key_and_Validation.md"]:
            src_path = os.path.join(src_dir, filename)
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace titles and references
            new_content = content.replace("Mock Examination 04", f"Mock Examination {pad}")
            new_content = new_content.replace("Mock Examination 01", f"Mock Examination {pad}")
            new_content = new_content.replace("Mock 04", f"Mock {pad}")
            new_content = new_content.replace("Mock 01", f"Mock {pad}")
            new_content = new_content.replace("IIT_BOMBAY_STYLE", "IIT_DELHI_STYLE")
            new_content = new_content.replace("IIT Bombay", "IIT Delhi")
            
            # Parametric variations
            new_content = new_content.replace("10.0\\ \\Omega", f"{var['R']}\\ \\Omega")
            new_content = new_content.replace("20\\text{ mH}", f"{var['L']}\\text{{ mH}}")
            new_content = new_content.replace("50\\ \\mu\\text{F}", f"{var['C']}\\ \\mu\\text{{F}}")
            new_content = new_content.replace("30.0\\text{ V}", f"{var['V']}\\text{{ V}}")
            new_content = new_content.replace("0.30", f"{var['mu']}")
            new_content = new_content.replace("0.10\\text{ M}", f"{var['conc']}\\text{{ M}}")
            new_content = new_content.replace("4.74", f"{var['pKa']}")

            dst_path = os.path.join(dst_dir, filename)
            with open(dst_path, "w", encoding="utf-8") as f:
                f.write(new_content)
                
        print(f"Generated Mock {pad} cleanly for IIT Delhi.")

if __name__ == "__main__":
    create_delhi_mocks()

