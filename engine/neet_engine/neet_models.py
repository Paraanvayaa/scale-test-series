# -*- coding: utf-8 -*-
"""
NEET Mock Generation Engine - Data Models and Formatters
Calibrated against authentic NTA NEET-UG standards (2021-2026).
"""
import os
import re

class NeetQuestion:
    def __init__(self, q_num, subject, section, chapter, topic, q_type, text, options, correct_idx, solution_steps, distractor_analysis, takeaway):
        self.q_num = q_num  # 1 to 200
        self.subject = subject  # Physics, Chemistry, Botany, Zoology
        self.section = section  # Section A, Section B
        self.chapter = chapter
        self.topic = topic
        self.q_type = q_type  # Statement I & II, Match List, Assertion-Reason, Multi-Statement, Conceptual MCQ
        self.text = text
        self.options = options  # List of 4 strings (A, B, C, D)
        self.correct_idx = correct_idx  # 0, 1, 2, 3 -> corresponding to (1), (2), (3), (4)
        self.solution_steps = solution_steps
        self.distractor_analysis = distractor_analysis
        self.takeaway = takeaway

    @property
    def correct_letter(self):
        return ["(1)", "(2)", "(3)", "(4)"][self.correct_idx]


def normalize_latex(text):
    """
    Sanitizes LaTeX and chemical formula syntax across Python escape artifacts.
    """
    if not text:
        return ""
    
    # Restore Python escape artifact bytes
    text = text.replace('\x07lpha', r'\alpha')
    text = text.replace('\x08eta', r'\beta')
    text = text.replace('\x0crac', r'\frac')
    text = text.replace('\x0b', '')
    
    # Fix tab characters absorbed in LaTeX commands
    text = re.sub(r'(?<!\\)\btext\{', r'\\text{', text)
    text = re.sub(r'\t+ext\{', r'\\text{', text)
    text = re.sub(r'\t+heta\b', r'\\theta', text)
    text = re.sub(r'\t+o\b', r'\\to', text)
    text = re.sub(r'\t+au\b', r'\\tau', text)
    
    # Fix reaction arrows inside math: -> to \to
    text = re.sub(r'(\$[^\$]*?)(?<!-)->(?!\>)([^\$]*?\$)', r'\1\\to\2', text)
    
    # Fix any $$...$ where display math opened but closed with a single $
    text = re.sub(r'\$\$([^\$\n]+?)\$(?![\$])([\.,;]?\s*(?:\n|\Z|$))', r'$$\1$$\2', text)

    return text


def clean_option_text(opt):
    """
    Ensures options with mathematical expressions, variables, units, or chemical
    formulas are properly wrapped in KaTeX math delimiters ($...$) without raw
    LaTeX command leaks.
    """
    if not opt:
        return ""
    opt = normalize_latex(opt.strip())
    
    # If opt has unbalanced single dollar: e.g. starts without $ but ends with $ or vice versa
    if opt.count('$') == 1:
        if opt.endswith('$'):
            opt = '$' + opt
        elif opt.startswith('$'):
            opt = opt + '$'

    # Check if there are raw LaTeX symbols outside $...$
    stripped = re.sub(r'\$[^\$]*?\$', '', opt)
    
    latex_symbols = [
        r'\alpha', r'\beta', r'\gamma', r'\Delta', r'\delta', r'\lambda', r'\mu', 
        r'\pi', r'\rho', r'\sigma', r'\omega', r'\Omega', r'\nu', r'\theta', r'\epsilon',
        r'\varepsilon', r'\sqrt', r'\frac', r'\times', r'\to', r'\rightarrow', r'\pm', r'\circ',
        r'\text', r'\vec', r'\hat', r'\ln', r'\log', r'\int', r'\approx', r'\neq', r'\le', r'\ge',
        r'E_{ax}', r'E_{eq}', r'\Delta L'
    ]
    
    has_raw_latex = any(sym in stripped for sym in latex_symbols)
    has_caret_or_sub = bool(re.search(r'[a-zA-Z0-9\)\}][\^_][a-zA-Z0-9\(\{]', stripped))
    has_isolated_var = bool(re.search(r'\b[txyzEkFRCLIAVv]\b', stripped)) and any(c in stripped for c in ['^', '/', '=', '+', '-'])
    
    if (has_raw_latex or has_caret_or_sub or has_isolated_var) and '$' not in opt:
        # If option has formula with parenthetical text note like "t^0 (constant)" or "\sqrt{3} (1.732)"
        paren_match = re.search(r'^(.*?)\s*(\([^\)]+\))$', opt)
        if paren_match and not any(k in opt for k in ['because', 'since', 'due to', 'Solid']):
            math_part, paren_part = paren_match.groups()
            return f"${math_part.strip()}$ {paren_part}"
        elif any(k in opt for k in ['because', 'since', 'Solid']):
            return re.sub(r'\(([kR0-9\s/=^\^]+)\)', r'($\1$)', opt)
        else:
            return f"${opt}$"
            
    return opt


def clean_markdown_text(text):
    """
    Ensures clean spacing and paragraph separation for Statements, Assertions,
    and multi-statement items.
    """
    if not text:
        return ""
    
    text = normalize_latex(text)
    
    # Ensure Given below are two statements is its own paragraph
    text = re.sub(r'(Given below are two statements[^\n:]*:?)(?:\s+|\n+)(\*{0,2}Statement\s+I)', r'\1\n\n\2', text, flags=re.IGNORECASE)
    # Ensure Statement I and Statement II are distinct paragraphs
    text = re.sub(r'(\*{0,2}Statement\s+I\s*:\*{0,2}.*?)(?:\s+|\n+)(\*{0,2}Statement\s+II\s*:\*{0,2})', r'\1\n\n\2', text)
    # Ensure Assertion (A) and Reason (R) are distinct paragraphs
    text = re.sub(r'(\*{0,2}Assertion\s*(?:\([AR]\))?\s*:\*{0,2}.*?)(?:\s+|\n+)(\*{0,2}Reason\s*(?:\([AR]\))?\s*:\*{0,2})', r'\1\n\n\2', text)
    # Ensure multi-statement items A., B., C., D., E. each start on a new paragraph
    text = re.sub(r'(?:\n|\A)([A-E]\.\s+)', r'\n\n\1', text)
    # Ensure prompt lines have an empty line before them
    text = re.sub(r'(?:\n|\s+)(In the light of the above statements, choose the (?:most appropriate|correct) answer from the options given below:)', r'\n\n\1', text, flags=re.IGNORECASE)
    text = re.sub(r'(?:\n|\s+)(Choose the correct (?:answer|option) from the options given below:)', r'\n\n\1', text, flags=re.IGNORECASE)
    
    return text.strip()


def format_question_paper(mock_num, questions):
    """
    Formats the 200 questions into standard NEET Question Paper Markdown
    with clean spacing and isolated option rows.
    """
    pad = f"{mock_num:02d}"
    lines = [
        f"# NATIONAL ELIGIBILITY CUM ENTRANCE TEST (UG) - NEET (UG)",
        f"## ALL INDIA MASTER MOCK TEST - {pad}",
        f"**Duration:** 3 Hours 20 Minutes (200 Minutes) | **Maximum Marks:** 720 Marks",
        f"**Test Pattern:** Exact NTA NEET-UG Modern Pattern (200 Questions, Attempt 180 Questions)",
        "",
        "---",
        "### IMPORTANT INSTRUCTIONS FOR CANDIDATES",
        "1. **Structure of the Examination:**",
        "   - The Question Paper consists of **200 Multiple Choice Questions** divided into four subjects: **Physics**, **Chemistry**, **Botany**, and **Zoology**.",
        "   - Each Subject contains two sections: **Section A** (35 Questions, Q1–35, mandatory) and **Section B** (15 Questions, Q36–50, candidates attempt any 10).",
        "   - Total questions to be answered: **180 Questions**.",
        "2. **Marking Scheme:**",
        "   - **+4 Marks** for each correct response.",
        "   - **-1 Mark** for each incorrect response (Negative Marking).",
        "   - **0 Marks** for unattempted or unanswered questions.",
        "3. **Syllabus & Cognitive Rigor:**",
        "   - Aligned strictly with NCERT line-by-line core text and NTA cognitive depth.",
        "   - Includes authentic Statement I & II, Assertion-Reason, Match List-I & II, and Multi-Statement analytical frameworks.",
        "---",
        ""
    ]

    current_subject = None
    current_section = None

    for q in questions:
        if q.subject != current_subject:
            current_subject = q.subject
            lines.append(f"\n# PART {get_part_num(current_subject)}: {current_subject.upper()}\n")
            current_section = None

        if q.section != current_section:
            current_section = q.section
            lines.append(f"## {current_section.upper()}\n")
            if "A" in current_section:
                lines.append("*(Questions 1 to 35 in each subject are Mandatory. Answer all questions.)*\n")
            else:
                lines.append("*(Questions 36 to 50 in each subject. Answer ANY 10 questions out of 15.)*\n")

        lines.append(f"#### Q{q.q_num}. [{q.q_type} | {q.chapter}]")
        lines.append("")
        lines.append(clean_markdown_text(q.text))
        lines.append("")
        
        # Options formatted as distinct lines with clean spacing and bold prefixes
        lines.append("<div class=\"options-container\">")
        lines.append("")
        for idx, opt in enumerate(q.options):
            cleaned_opt = clean_option_text(opt)
            lines.append(f"- **({idx + 1})** {cleaned_opt}")
        lines.append("")
        lines.append("</div>")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def format_detailed_solutions(mock_num, questions):
    """
    Formats the 200 questions into exhaustive step-by-step pedagogical solutions.
    """
    pad = f"{mock_num:02d}"
    lines = [
        f"# NATIONAL ELIGIBILITY CUM ENTRANCE TEST (UG) - NEET (UG)",
        f"## DETAILED STEP-BY-STEP PEDAGOGICAL SOLUTIONS - MOCK {pad}",
        f"**Comprehensive Concept Blueprints, NCERT Citations & Distractor Deconstruction**",
        "",
        "---",
        ""
    ]

    current_subject = None
    for q in questions:
        if q.subject != current_subject:
            current_subject = q.subject
            lines.append(f"\n# PART {get_part_num(current_subject)}: {current_subject.upper()} - SOLUTIONS\n")

        lines.append(f"---")
        lines.append(f"### Question {q.q_num}")
        lines.append(f"**Subject:** {q.subject} | **Section:** {q.section} | **Chapter:** {q.chapter} ({q.topic})")
        lines.append(f"**Question Type:** {q.q_type}")
        lines.append(f"**Correct Answer:** Option **{q.correct_letter}**")
        lines.append("")
        lines.append("#### Step-by-Step Pedagogical Explanation:")
        lines.append(clean_markdown_text(q.solution_steps))
        lines.append("")
        lines.append("#### Distractor & Option Deconstruction:")
        lines.append(clean_markdown_text(q.distractor_analysis))
        lines.append("")
        lines.append(f"**Key NCERT Principle / High-Yield Takeaway:** {clean_markdown_text(q.takeaway)}")
        lines.append("")

    return "\n".join(lines)


def format_answer_key_and_analysis(mock_num, questions):
    """
    Formats the Master Answer Key and statistical cognitive breakdown.
    """
    pad = f"{mock_num:02d}"
    lines = [
        f"# NATIONAL ELIGIBILITY CUM ENTRANCE TEST (UG) - NEET (UG)",
        f"## MASTER ANSWER KEY & COGNITIVE BLUEPRINT - MOCK {pad}",
        f"**Official Scoring Key & Question Classification Matrix**",
        "",
        "---",
        "",
        "### SECTION 1: MASTER ANSWER KEY TABLE",
        "",
        "| Q.No | Subject | Correct Option | Question Type | Topic Focus |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]

    for q in questions:
        lines.append(f"| **{q.q_num}** | {q.subject} ({q.section[-1]}) | **{q.correct_letter}** | {q.q_type} | {q.topic} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("### SECTION 2: SUBJECT-WISE QUESTION BREAKDOWN")
    lines.append("")
    lines.append("| Subject | Section A (Mandatory) | Section B (Attempt 10/15) | Total Questions | Total Marks |")
    lines.append("| :--- | :--- | :--- | :--- | :--- |")
    lines.append("| **Physics** | 35 Questions (Q1–35) | 15 Questions (Q36–50) | 50 Questions | 180 Marks |")
    lines.append("| **Chemistry** | 35 Questions (Q51–85) | 15 Questions (Q86–100) | 50 Questions | 180 Marks |")
    lines.append("| **Botany** | 35 Questions (Q101–135) | 15 Questions (Q136–150) | 50 Questions | 180 Marks |")
    lines.append("| **Zoology** | 35 Questions (Q151–185) | 15 Questions (Q186–200) | 50 Questions | 180 Marks |")
    lines.append("| **Grand Total** | **140 Questions** | **60 Questions** | **200 Questions** | **720 Marks** |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Question Type Distribution Matrix
    from collections import Counter
    type_counts = Counter(q.q_type for q in questions)
    lines.append("### SECTION 3: COGNITIVE RIGOR & QUESTION TYPE DISTRIBUTION")
    lines.append("")
    lines.append("| Question Type | Question Count | Percentage | NTA NEET-UG Benchmark |")
    lines.append("| :--- | :--- | :--- | :--- |")
    for q_t, cnt in type_counts.most_common():
        pct = (cnt / len(questions)) * 100
        lines.append(f"| **{q_t}** | {cnt} | {pct:.1f}% | High-Yield 2026 Distribution |")

    lines.append("")
    lines.append("---")

    return "\n".join(lines)


def get_part_num(subject):
    mapping = {
        "Physics": "1",
        "Chemistry": "2",
        "Botany": "3",
        "Zoology": "4"
    }
    return mapping.get(subject, "1")
