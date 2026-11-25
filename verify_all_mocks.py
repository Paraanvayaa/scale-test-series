import glob
import re

print("Verifying all 40 NEET Mock Tests across both folders...")

for base in ["neet_mock_tests", "mock_tests/neet"]:
    print(f"\n--- Checking base directory: {base} ---")
    for m in range(1, 41):
        pad = f"{m:02d}"
        path = f"{base}/Mock_{pad}/Question_Paper.md"
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Split by questions
        parts = text.split("#### Q")
        q_bodies = []
        for p in parts[1:]:
            lines = p.split('\n')
            body_lines = []
            for line in lines[1:]:
                if '<div class="options-container">' in line:
                    break
                body_lines.append(line)
            body = '\n'.join(body_lines).strip()
            q_bodies.append(body)
        
        assert len(q_bodies) == 200, f"Mock {m}: Expected 200, got {len(q_bodies)}"
        unique_count = len(set(q_bodies))
        assert unique_count == 200, f"Mock {m}: Expected 200 unique, got {unique_count}"

print("\nALL 40 MOCKS CONFIRMED: Each mock has 200/200 100% unique questions with ZERO repeats!")
