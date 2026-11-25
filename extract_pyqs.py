# -*- coding: utf-8 -*-
import pypdf
import re
import json
import os

pdf_configs = [
    {
        "file": "NEET/NEET 2024 Question Paper with Answer Key.pdf",
        "year": "NEET 2024",
        "total": 200,
        "sections": {"botany": (1, 50), "zoology": (51, 100), "chemistry": (101, 150), "physics": (151, 200)}
    },
    {
        "file": "NEET/NEET 2023 Question Paper with Answer Key.pdf",
        "year": "NEET 2023",
        "total": 200,
        "sections": {"botany": (1, 50), "zoology": (51, 100), "chemistry": (101, 150), "physics": (151, 200)}
    },
    {
        "file": "NEET/NEET 2024 (Re-Examination) Question Paper with Answer Key.pdf",
        "year": "NEET 2024 Re-Exam",
        "total": 200,
        "sections": {"botany": (1, 50), "zoology": (51, 100), "chemistry": (101, 150), "physics": (151, 200)}
    },
    {
        "file": "NEET/NEET 2023 Manipur Question Paper with Answer Key.pdf",
        "year": "NEET 2023 Manipur",
        "total": 200,
        "sections": {"botany": (1, 50), "zoology": (51, 100), "chemistry": (101, 150), "physics": (151, 200)}
    },
    {
        "file": "NEET/NEET 2025 Question Paper with Answer Key.pdf",
        "year": "NEET 2025",
        "total": 180,
        "sections": {"botany": (1, 45), "zoology": (46, 90), "chemistry": (91, 135), "physics": (136, 180)}
    },
    {
        "file": "NEET/NEET 2026 Question Paper with Answer Key.pdf",
        "year": "NEET 2026",
        "total": 180,
        "sections": {"botany": (1, 45), "zoology": (46, 90), "chemistry": (91, 135), "physics": (136, 180)}
    }
]

def extract_answers_from_pdf(reader):
    full_text = ""
    for p in range(len(reader.pages) - 6, len(reader.pages)):
        full_text += "\n" + reader.pages[p].extract_text()
    
    # Matches patterns like "1.B", "101.C", "20. D"
    pairs = re.findall(r'(\d+)\s*[\.:]\s*([A-D])', full_text)
    ans_map = {}
    for num_str, letter in pairs:
        q_idx = int(num_str)
        if q_idx not in ans_map:
            ans_map[q_idx] = letter
    return ans_map

all_questions_db = {
    "physics": [],
    "chemistry": [],
    "botany": [],
    "zoology": []
}

for cfg in pdf_configs:
    fpath = cfg["file"]
    if not os.path.exists(fpath):
        print(f"Skipping {fpath} (not found)")
        continue
    
    print(f"Processing {cfg['year']} from {fpath}...")
    reader = pypdf.PdfReader(fpath)
    ans_map = extract_answers_from_pdf(reader)
    print(f"  Extracted {len(ans_map)} answers for {cfg['year']}.")
    
    # Extract questions
    full_text = ""
    for p in range(len(reader.pages)):
        full_text += f"\n=== PAGE {p} ===\n" + reader.pages[p].extract_text()
        
    pattern = r'Q(\d+)\.M\s*CQ[^\n]*\n([\s\S]*?)\((?:A)\)([\s\S]*?)\((?:B)\)([\s\S]*?)\((?:C)\)([\s\S]*?)\((?:D)\)([\s\S]*?)(?:Open solution|Keep practising|=== PAGE|$)'
    matches = re.findall(pattern, full_text)
    print(f"  Extracted {len(matches)} questions.")
    
    letter_to_idx = {"A": 0, "B": 1, "C": 2, "D": 3}
    
    for q_num_str, q_text, opt_a, opt_b, opt_c, opt_d in matches:
        q_num = int(q_num_str)
        correct_letter = ans_map.get(q_num, "A")
        correct_idx = letter_to_idx.get(correct_letter, 0)
        
        # Clean question text
        clean_text = q_text.strip()
        # Clean options
        clean_opts = [opt_a.strip(), opt_b.strip(), opt_c.strip(), opt_d.strip()]
        
        # Determine subject
        subj = None
        for s_name, (start_q, end_q) in cfg["sections"].items():
            if start_q <= q_num <= end_q:
                subj = s_name
                break
                
        if not subj:
            continue
            
        # Determine q_type
        if "Match List" in clean_text or "List - I" in clean_text or "List I" in clean_text:
            q_type = "Match List"
        elif "Statement I" in clean_text and "Statement II" in clean_text:
            q_type = "Statement I & II"
        elif "Assertion" in clean_text and "Reason" in clean_text:
            q_type = "Assertion & Reason"
        elif any(f"{c}." in clean_text for c in ["A", "B", "C", "D", "E"]) and "Choose the correct" in clean_text:
            q_type = "Multi-Statement"
        else:
            q_type = "Direct MCQ"
            
        item = {
            "source": f"{cfg['year']} Q{q_num}",
            "subject": subj.capitalize(),
            "q_type": q_type,
            "text": clean_text,
            "options": clean_opts,
            "correct_idx": correct_idx,
            "correct_letter": correct_letter
        }
        all_questions_db[subj].append(item)

out_file = "pyq_database.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions_db, f, indent=2)

print("\n=== EXTRACTION SUMMARY ===")
for subj, items in all_questions_db.items():
    print(f"  {subj.capitalize()}: {len(items)} authentic questions")
print(f"Saved total database to {out_file}")

