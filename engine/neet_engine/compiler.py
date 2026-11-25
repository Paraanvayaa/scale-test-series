# -*- coding: utf-8 -*-
"""
NEET Mock Generation Compiler
Compiles and generates all 200 questions, detailed solutions, and analysis reports.
Generates to both neet_mock_tests and mock_tests/neet.
Supports:
  - Mocks 01 to 20: Easy / NCERT Foundation Tier
  - Mocks 21 to 40: Moderate / 2026 Analytical Rigor Tier (Exact NEET 2026 Question Distribution)
  - Mocks 41 to 60: Difficult / 2026-2027 Advanced Predicted Rigor Tier
"""
import os
import sys

# Ensure local imports work regardless of execution context
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from neet_models import format_question_paper, format_detailed_solutions, format_answer_key_and_analysis

# Foundation Curricula (Mocks 01 - 20)
from curriculum_physics import get_physics_questions
from curriculum_chemistry import get_chemistry_questions
from curriculum_botany import get_botany_questions
from curriculum_zoology import get_zoology_questions

# Moderate / 2026 Analytical Curricula (Mocks 21 - 40)
from curriculum_physics_mod import get_physics_questions_mod
from curriculum_chemistry_mod import get_chemistry_questions_mod
from curriculum_botany_mod import get_botany_questions_mod
from curriculum_zoology_mod import get_zoology_mod_questions

# Difficult / 2026-2027 Advanced Predicted Rigor Curricula (Mocks 41 - 60)
from curriculum_physics_diff import get_physics_questions_diff
from curriculum_chemistry_diff import get_chemistry_questions_diff
from curriculum_botany_diff import get_botany_questions_diff
from curriculum_zoology_diff import get_zoology_diff_questions

def build_mock(mock_num, output_bases=["neet_mock_tests", "mock_tests/neet"]):
    pad = f"{mock_num:02d}"
    
    # 1. Gather all 200 questions according to Tier
    if mock_num <= 20:
        physics_qs = get_physics_questions(mock_num)
        chemistry_qs = get_chemistry_questions(mock_num)
        botany_qs = get_botany_questions(mock_num)
        zoology_qs = get_zoology_questions(mock_num)
        tier_label = "Ignite / NCERT Foundation"
    elif mock_num <= 40:
        physics_qs = get_physics_questions_mod(mock_num)
        chemistry_qs = get_chemistry_questions_mod(mock_num)
        botany_qs = get_botany_questions_mod(mock_num)
        zoology_qs = get_zoology_mod_questions(mock_num)
        tier_label = "Conquer / 2026 Analytical Rigor"
    else:
        physics_qs = get_physics_questions_diff(mock_num)
        chemistry_qs = get_chemistry_questions_diff(mock_num)
        botany_qs = get_botany_questions_diff(mock_num)
        zoology_qs = get_zoology_diff_questions(mock_num)
        tier_label = "Dominate / 2026-2027 Advanced Predicted Rigor"
    
    all_qs = physics_qs + chemistry_qs + botany_qs + zoology_qs
    assert len(all_qs) == 200, f"Expected 200 questions, got {len(all_qs)}"
    
    # Balance and distribute correct option indices across (1), (2), (3), (4)
    for q in all_qs:
        seed = q.q_num * 7 + mock_num * 13
        target_idx = seed % 4
        if target_idx != q.correct_idx and q.q_type == "Direct MCQ":
            orig_correct_opt = q.options[q.correct_idx]
            swapped_opt = q.options[target_idx]
            q.options[q.correct_idx] = swapped_opt
            q.options[target_idx] = orig_correct_opt
            q.correct_idx = target_idx
    
    # 2. Format outputs
    paper_content = format_question_paper(mock_num, all_qs)
    sol_content = format_detailed_solutions(mock_num, all_qs)
    ans_content = format_answer_key_and_analysis(mock_num, all_qs)
    
    # 3. Write files to disk for each output base
    for output_base in output_bases:
        mock_dir = os.path.join(output_base, f"Mock_{pad}")
        os.makedirs(mock_dir, exist_ok=True)
        
        paper_path = os.path.join(mock_dir, "Question_Paper.md")
        sol_path = os.path.join(mock_dir, "Detailed_Solutions.md")
        ans_path = os.path.join(mock_dir, "Answer_Key_and_Analysis.md")
        
        with open(paper_path, "w", encoding="utf-8") as f:
            f.write(paper_content)
        with open(sol_path, "w", encoding="utf-8") as f:
            f.write(sol_content)
        with open(ans_path, "w", encoding="utf-8") as f:
            f.write(ans_content)
            
    print(f"Mock {pad} [{tier_label}] compiled successfully: 200 Qs across Physics, Chemistry, Botany, Zoology.")
    return len(all_qs)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        m = int(sys.argv[1])
        build_mock(m)
    else:
        print("Compiling all 60 NEET Mock Tests (Mocks 01 to 60)...")
        for m in range(1, 61):
            build_mock(m)
        print("All 60 NEET Mock Tests compiled successfully!")
