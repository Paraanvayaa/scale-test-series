# Script to generate comprehensive historical intelligence profiles report
import json

def generate_markdown():
    with open('iit_analysis_summary.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    md = []
    md.append("# JEE Advanced: Independent Historical Examination Intelligence Profiles & Architecture\n")
    md.append("> **Analysis Scope**: 40 Official Question Papers | 7 Organising IITs | 2,298 Analysed Historical Questions | Direct Empirical Extraction\n")
    md.append("> **Operational Directive**: Establish seven completely independent, evidence-backed IIT style profiles to drive the 20-mock examination generation engine without generic templating or artificial exaggeration.\n\n")

    md.append("## Executive Summary & System Architecture\n")
    md.append("To eliminate generic examination generation, the IIT-Specific Examination Generation Engine anchors each mock test to the historically observed question-setting characteristics of the specific IIT that organised the examination. The historical dataset covers **40 complete papers across 7 institutes** from 2007 through 2026.\n\n")
    md.append("The empirical analysis reveals distinct structural, pedagogical, and stylistic signatures across the organising IITs, while confirming a shared, uncompromising JEE Advanced standard of academic rigor.\n\n")

    md.append("### Key Empirical Distinctions Identified Across IITs\n")
    md.append("| Organising IIT | Analysed Years | Total Questions | Primary Distinguishing Characteristic | Dominant Format | Calculation / Diagram Profile |\n")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
    md.append("| **IIT Bombay** | 2007, 2015, 2022 | 360 | Structural format innovations & multi-concept chemical thermodynamics | Balanced (SC 45.3%, Num 26.7%, MC 28.1%) | Moderate calculation; high thermochemical / electrochem rigor; 63 Physics diagrams |\n")
    md.append("| **IIT Delhi** | 2012, 2013, 2020 | 348 | Rigorous multi-correct questions with independent option verification | Multi-Correct heavy (31.3% MC, highest ratio) | High algebraic rigor; tricky edge cases; 54 Physics diagrams |\n")
    md.append("| **IIT Guwahati** | 2009, 2016, 2023 | 327 | Conceptual elegance, symmetry arguments & physical insight over brute calculation | Balanced distribution with high P2 numerical focus (54) | Low brute-force math; high conceptual reasoning; 51 Physics diagrams |\n")
    md.append("| **IIT Kanpur** | 2011, 2018, 2025 | 333 | Extreme numerical intensity, precision tolerances & rigorous analytical calculus | Numerical dominant (38.7% Num, highest overall) | Heavy multi-step numerical derivations; exact decimals; 41 Physics diagrams |\n")
    md.append("| **IIT Kharagpur** | 2014, 2021 | 234 | Polarised Paper 1 vs Paper 2 structure & intricate organic reaction pathways | Asymmetric (P1 has 0 Single Choice; P2 has 60 Single Choice) | Longest chemistry question statements (64.2 words avg); 48 Physics diagrams |\n")
    md.append("| **IIT Madras** | 2010, 2017, 2024 | 351 | Electromagnetism prominence & high-speed coordinate/algebraic synthesis | Sharp Single Correct (48.4%) + P2 Numericals (30 in 2024) | High geometric/vector elegance; 64 Physics diagrams; partial marking pioneer |\n")
    md.append("| **IIT Roorkee** | 2008, 2019, 2026 | 345 | Mechanics dominance, experimental apparatus setups & high statement verbosity | High Single Correct + Multi-Correct (53.0% SC, 25.2% MC) | Highest statement length (Phys 127.4 words); highest diagram density (71 Physics diagrams) |\n\n")

    md.append("---\n\n")

    # Detailed IIT Profiles
    iit_details = [
        {
            'name': 'IIT Bombay',
            'id': 'IIT_BOMBAY_STYLE',
            'folder': 'IIT BOMBAY',
            'years': '2007, 2015, 2022',
            'q_count': 360,
            'confidence': 'High (3 cycles across 15 years: 2007 offline, 2015 offline transition, 2022 online CBT)',
            'key_traits': [
                '**Structural Format Pioneer**: IIT Bombay historically drives major structural evolutions in JEE. In 2015, it introduced non-negative integer questions and high negative marking (-2) in multiple-choice questions. In 2022, it introduced STEM numericals with decimal precision.',
                '**Chemical Thermodynamics & Physical Equilibria**: Prominent focus on real calorimeter setups (bomb calorimeters), enthalpy cycle loops, and multistep electrochemical redox potentials.',
                '**Physics Multiconcept Synthesis**: Integrates mechanics with electrodynamics (e.g. conducting rotating cylinders in magnetic fields, induction combined with SHM).',
                '**Mathematics**: High concentration of calculus coupled with functional inequalities and trigonometric transformations.'
            ],
            'subject_dist': {
                'Physics': 'Electromagnetism (31.0%), Mechanics (28.6%), Optics & Wave Motion (26.2%), Modern Physics (9.5%), Thermodynamics & Heat (6.3%)',
                'Chemistry': 'Physical Chemistry (68.0%), Organic Chemistry (18.5%), Inorganic Chemistry (13.7%) - strong thermochemistry & chemical kinetics weightage',
                'Mathematics': 'Calculus & Functions (27.5%), Trigonometry & Geometry (52.5% combined), Algebra (42.5%)'
            },
            'paper_split': 'Paper 1 and Paper 2 maintain identical question counts (54 each in 2022; 60 each in 2015). Paper 1 balances single correct, multi-correct, and numericals; Paper 2 intensifies multi-correct partial marking dilemmas.',
            'limitations': 'Gap between 2007 and 2015 spans the transition from subjective/OMR to mixed format; 2022 represents the modern online paradigm.'
        },
        {
            'name': 'IIT Delhi',
            'id': 'IIT_DELHI_STYLE',
            'folder': 'IIT DELHI',
            'years': '2012, 2013, 2020',
            'q_count': 348,
            'confidence': 'High (3 cycles: 2012 offline, 2013 inaugural JEE Advanced, 2020 pandemic online edition)',
            'key_traits': [
                '**Option-Checking Multi-Correct Complexity**: Highest ratio of multiple-correct questions (31.3%). Each option frequently acts as an independent sub-problem requiring separate mathematical evaluation.',
                '**Rigorous Boundary Conditions & Edge Cases**: Questions frequently test limiting behaviors, domain restrictions, and sign conventions in calculus and optics.',
                '**Physics - Circuit Transients & Field Distributions**: Heavy emphasis on RC/LR/LCR transient states, Faraday law boundary conditions, and classical rolling mechanics.',
                '**Chemistry**: High emphasis on coordination isomerism counts, organic stereochemical pathways, and ionic equilibrium buffers.'
            ],
            'subject_dist': {
                'Physics': 'Mechanics (33.6%), Electromagnetism (31.1%), Optics & Waves (18.9%), Modern Physics (8.2%), Thermodynamics & Heat (7.4%)',
                'Chemistry': 'Physical Chemistry (71.4%), Organic Chemistry (15.6%), Inorganic Chemistry (13.0%) - high coordination chemistry & solid state presence',
                'Mathematics': 'Algebra (37.1%), Calculus (28.4%), Trigonometry (48.3%), Coordinate Geometry (15.5%), Vectors & 3D (12.1%)'
            },
            'paper_split': 'Paper 1 features standard single correct and integer/numerical; Paper 2 shifts heavily towards analytical multi-correct (60 questions across dataset) and numericals (36 questions in 2020 P2).',
            'limitations': '2012 and 2013 were consecutive years under transitioning exam bodies; 2020 represents the established online CBT mode.'
        },
        {
            'name': 'IIT Guwahati',
            'id': 'IIT_GUWAHATI_STYLE',
            'folder': 'IIT Guwahati',
            'years': '2009, 2016, 2023',
            'q_count': 327,
            'confidence': 'High (3 cycles: 2009 offline, 2016 offline, 2023 modern CBT)',
            'key_traits': [
                '**Conceptual Elegance over Tedious Algebra**: Questions are engineered to collapse into simple 2-3 step solutions if the student identifies the core physical symmetry or invariant quantity (e.g. angular momentum conservation, energy invariants).',
                '**Thermodynamics & Modern Physics Weightage**: Highest proportion of Modern Physics (16 questions) and Heat/Thermodynamics (15 questions) in physics.',
                '**Mathematics - Geometric Insight**: Integrates vector geometry with coordinate conic sections and complex numbers locus problems without requiring brute-force coordinate expansions.',
                '**Chemistry - Clean Reaction Sequences**: Organic synthesis focuses on well-defined named reactions with unambiguous stereochemical outcomes; physical chemistry focuses on gaseous state and phase equilibria.'
            ],
            'subject_dist': {
                'Physics': 'Mechanics (35.7%), Electromagnetism (30.4%), Optics & Waves (25.2%), Modern Physics (13.9%), Thermodynamics & Heat (13.0%)',
                'Chemistry': 'Physical Chemistry (67.8%), Organic Chemistry (21.7%), Inorganic Chemistry (10.5%)',
                'Mathematics': 'Trigonometry & Locus (51.4%), Algebra (36.7%), Calculus (29.4%), Coordinate Geometry (20.2%), Vectors & 3D (11.0%)'
            },
            'paper_split': 'Paper 1 emphasises fundamental single correct and multi-correct conceptual checks; Paper 2 introduces concentrated numerical questions (54 numericals in dataset, 30 in 2023 P2 alone).',
            'limitations': '2023 introduced lower total question counts (51 per paper), reflecting modern post-pandemic calibration.'
        },
        {
            'name': 'IIT Kanpur',
            'id': 'IIT_KANPUR_STYLE',
            'folder': 'IIT KANPUR',
            'years': '2011, 2018, 2025',
            'q_count': 333,
            'confidence': 'High (3 cycles: 2011 high-question offline exam, 2018 first online CBT, 2025 modern online paper)',
            'key_traits': [
                '**Supreme Numerical Intensity & Exactness**: Kanpur has the highest proportion of Numerical/Integer questions (38.7% overall; 129 questions). Questions demand exact intermediate calculations, strict decimal adherence, and zero tolerance for rounding errors.',
                '**Advanced Analytical Calculus**: Deep integration of differential equations with physical models (e.g. damped oscillations, rate laws, population kinetics, orthogonal trajectories).',
                '**Physics - Precision Mechanics & Field Integrals**: Extensive use of non-uniform mass distributions, variable density integration, variable B-fields, and Poynting vector / radiation pressure concepts.',
                '**Chemistry - Quantitative Physical Chemistry**: Extensive multi-step problems in chemical thermodynamics, ionic equilibria, and concentration cell EMF calculations.'
            ],
            'subject_dist': {
                'Physics': 'Mechanics (36.8%), Electromagnetism (34.2%), Optics & Wave Motion (17.9%), Modern Physics (8.5%), Thermodynamics & Heat (6.8%)',
                'Chemistry': 'Physical Chemistry (69.5%), Organic Chemistry (20.5%), Inorganic Chemistry (9.9%)',
                'Mathematics': 'Algebra (41.4%), Trigonometry & Analytical Geometry (41.4%), Calculus (31.5%), Coordinate Geometry (17.1%), Vectors & 3D (11.7%)'
            },
            'paper_split': 'Consistent heavy numerical presence in both Paper 1 (63 numericals) and Paper 2 (66 numericals). Neither paper gives relief from computational rigor.',
            'limitations': '2011 paper had 69 questions in P1; modern papers (2018, 2025) scaled down to 54 and 48 questions, elevating per-question depth.'
        },
        {
            'name': 'IIT Kharagpur',
            'id': 'IIT_KHARAGPUR_STYLE',
            'folder': 'IIT KHARAGPUR',
            'years': '2014, 2021',
            'q_count': 234,
            'confidence': 'Moderate (2 cycles: 2014 offline, 2021 online CBT; 4 papers total)',
            'key_traits': [
                '**Paper 1 vs Paper 2 Radical Asymmetry**: In 2014, Paper 1 contained 0 single-choice questions (only 30 numericals and 30 multi-correct), while Paper 2 was 100% single-choice (60 questions). In 2021, P1 and P2 balanced stem-based questions with matching lists.',
                '**Highest Chemistry Verbosity & Organic Complexity**: Average chemistry word count is 64.2 words (highest across all IITs). Organic chemistry features complex multi-step synthesis schemes with 3-5 consecutive reagents and stereochemical branching.',
                '**Physics - Detailed Physical Contexts**: Questions provide exhaustive real-world or experimental setup narratives (e.g. ultrasonic interferometer, solar sail mechanics, cantilever deflection).',
                '**Mathematics - Conic Section Geometry**: Pure geometric definitions, focal properties, and locus intersections.'
            ],
            'subject_dist': {
                'Physics': 'Mechanics (34.1%), Electromagnetism (32.9%), Optics & Waves (14.6%), Modern Physics (9.8%), Thermodynamics & Heat (9.8%)',
                'Chemistry': 'Physical Chemistry (66.1%), Organic Chemistry (21.4%), Inorganic Chemistry (12.5%) - extensive multistep organic retrosynthesis',
                'Mathematics': 'Algebra (41.0%), Trigonometry (38.5%), Calculus (28.2%), Coordinate Geometry (20.5%), Vectors & 3D (7.7%)'
            },
            'paper_split': 'Sharp format divergence between P1 and P2: P1 focuses on high-pressure numerical and multi-correct problem solving; P2 features comprehension paragraphs, match lists, and multi-concept single correct problems.',
            'limitations': 'Only 2 cycles (4 papers) available in dataset compared to 6 papers for other IITs. Dataset is fully robust for qualitative and format style, but carries slightly wider confidence intervals for chapter frequencies.'
        },
        {
            'name': 'IIT Madras',
            'id': 'IIT_MADRAS_STYLE',
            'folder': 'IIT MADRAS',
            'years': '2010, 2017, 2024',
            'q_count': 351,
            'confidence': 'High (3 cycles: 2010 offline 84-question marathon, 2017 landmark scoring paper, 2024 recent online paper)',
            'key_traits': [
                '**Electromagnetism Pre-eminence**: Highest absolute and relative volume of Electromagnetism questions (46 questions, 37.4% of physics). Features complex flux linkages, mutual inductances, and motion of charged particles in crossed E and B fields.',
                '**Mathematical Coordinate & Algebraic Integration**: High volume of problems connecting complex numbers geometry, coordinate conics, and vector dot/cross products.',
                '**Diagrammatic Precision**: 64 physics questions with explicit technical diagrams and schematics.',
                '**Chemistry - Salt Analysis & Coordination Chemistry**: In-depth qualitative inorganic chemistry (precipitation tests, flame colors, ligand field splitting) combined with rate kinetics.'
            ],
            'subject_dist': {
                'Physics': 'Electromagnetism (37.4%), Mechanics (35.0%), Optics & Wave Motion (22.0%), Thermodynamics & Heat (8.9%), Modern Physics (6.5%)',
                'Chemistry': 'Physical Chemistry (73.0%), Organic Chemistry (18.4%), Inorganic Chemistry (8.6%)',
                'Mathematics': 'Trigonometry & Conics (54.7%), Algebra (42.7%), Calculus (31.6%), Coordinate Geometry (15.4%), Vectors & 3D (12.8%)'
            },
            'paper_split': 'Paper 1 is designed for high tempo and broad syllabus coverage (83 single correct, 63 numericals in dataset); Paper 2 features challenging multi-concept problems and numerical concentration (30 numericals in 2024 P2).',
            'limitations': '2010 paper format had 84 questions in P1; modern papers (2017, 2024) stabilised at 54 and 51 questions.'
        },
        {
            'name': 'IIT Roorkee',
            'id': 'IIT_ROORKEE_STYLE',
            'folder': 'IIT Roorkee',
            'years': '2008, 2019, 2026',
            'q_count': 345,
            'confidence': 'High (3 cycles: 2008 offline, 2019 online CBT, 2026 latest online examination)',
            'key_traits': [
                '**Mechanics Hegemony & Rotational Dynamics**: 55 questions in Mechanics (~45.5% of physics, highest among all IITs). In-depth problems on rolling with slipping, angular impulse, gyroscope principles, non-inertial frames, and fluid dynamics.',
                '**Highest Diagram & Graphical Frequency**: 71 physics questions with diagrams (88 diagrams total). Tests graphical interpretation of thermodynamic PV/TS diagrams, field lines, and phase trajectories.',
                '**Highest Problem Statement Verbosity**: Average word count is 127.4 words in Physics, 69.3 words in Chemistry, and 57.8 words in Mathematics. Questions feature elaborate physical narratives and engineering contexts.',
                '**Chemistry - Industrial & Environmental Inorganic**: High presence of extraction metallurgy, ore processing, silicates, and p-block chemistry.'
            ],
            'subject_dist': {
                'Physics': 'Mechanics (45.5%), Electromagnetism (26.4%), Optics & Waves (23.1%), Thermodynamics & Heat (13.2%), Modern Physics (9.9%)',
                'Chemistry': 'Physical Chemistry (66.9%), Organic Chemistry (20.9%), Inorganic Chemistry (12.3%) - highest inorganic extraction presence',
                'Mathematics': 'Trigonometry & Functions (57.4%), Algebra (46.1%), Calculus (28.7%), Coordinate Geometry (14.8%), Vectors & 3D (9.6%)'
            },
            'paper_split': 'Both Paper 1 and Paper 2 feature extensive reading density. Paper 1 emphasises Single Correct and Multi-Correct; Paper 2 intensifies numerical calculations (45 numericals in P2 dataset).',
            'limitations': '2008 paper had 69/66 questions without numerical entry; 2019 and 2026 represent modern format with 54 questions per paper.'
        }
    ]

    for p in iit_details:
        md.append(f"## {p['name']} Historical Intelligence Profile ({p['id']})\n")
        md.append(f"- **Organising Institute**: {p['name']}\n")
        md.append(f"- **Profile Identifier**: `{p['id']}`\n")
        md.append(f"- **Source Dataset Years**: {p['years']}\n")
        md.append(f"- **Total Analysed Questions**: {p['q_count']}\n")
        md.append(f"- **Statistical Confidence Level**: {p['confidence']}\n\n")
        
        md.append("### Core Observed Characteristics\n")
        for trait in p['key_traits']:
            md.append(f"- {trait}\n")
        md.append("\n")

        md.append("### Subject-Wise Observed Distribution & Focus Areas\n")
        md.append(f"- **Physics**: {p['subject_dist']['Physics']}\n")
        md.append(f"- **Chemistry**: {p['subject_dist']['Chemistry']}\n")
        md.append(f"- **Mathematics**: {p['subject_dist']['Mathematics']}\n\n")

        md.append("### Paper 1 vs Paper 2 Structural Profile\n")
        md.append(f"{p['paper_split']}\n\n")

        md.append("### Identified Dataset Limitations & Calibration Rules\n")
        md.append(f"{p['limitations']}\n\n")
        md.append("---\n\n")

    # Comparative IIT Style Matrix
    md.append("## Comparative IIT Style Matrix\n\n")
    md.append("This matrix outlines the empirical differences across all seven organizing IITs across the nine core dimensions required for generation:\n\n")
    md.append("| Dimension | IIT Bombay | IIT Delhi | IIT Guwahati | IIT Kanpur | IIT Kharagpur | IIT Madras | IIT Roorkee |\n")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
    md.append("| **Profile ID** | `IIT_BOMBAY_STYLE` | `IIT_DELHI_STYLE` | `IIT_GUWAHATI_STYLE` | `IIT_KANPUR_STYLE` | `IIT_KHARAGPUR_STYLE` | `IIT_MADRAS_STYLE` | `IIT_ROORKEE_STYLE` |\n")
    md.append("| **Primary Physics Anchor** | Balanced Mechanics & EM; Rotating frames | Circuits, Transients & Boundary conditions | Symmetry arguments, Invariants, Modern Phys | Precision mechanics & Field integration | Real-world physical apparatus context | Electromagnetism & Crossed field dynamics | Rigid body dynamics & Fluid mechanics |\n")
    md.append("| **Primary Chemistry Anchor** | Thermochemical cycles & Calorimetry | Coordination isomers & Ionic buffers | Named reactions & Gaseous equilibrium | Quantitative thermodynamics & Electrochemistry | Multistep organic synthesis pathways | Salt analysis & Coordination ligand fields | Industrial metallurgy & p-block reactions |\n")
    md.append("| **Primary Math Anchor** | Calculus with functional inequalities | Multi-case analysis & Edge-case domain bounds | Geometric insights & Vector conics | Differential equations & Analytical calculus | Pure conic locus & Tangent geometry | Complex numbers & Vector geometry synthesis | Extensive trigonometry & Function transformations |\n")
    md.append("| **Question Type Skew** | Balanced (SC, MC, Num) | Highest Multi-Correct (31.3%) | High P2 Numericals | Highest Numerical (38.7%) | Radical P1 vs P2 Asymmetry | High Single Correct (48.4%) | High SC + Diagrammatic MC |\n")
    md.append("| **Math Complexity** | High Conceptual | High Deductive | High Elegance | High Computational | High Algebraic | High Geometric | High Interpretive |\n")
    md.append("| **Diagram / Graphical Index** | High (63 Phys) | Moderate (54 Phys) | Moderate (51 Phys) | Moderate (41 Phys) | High (48 Phys) | High (64 Phys) | Highest (71 Phys) |\n")
    md.append("| **Avg Statement Length** | Moderate (118 words) | Moderate (118 words) | High (126 words) | Moderate (116 words) | Longest Chem (64.2 words) | Moderate (115 words) | Longest Phys (127.4 words) |\n")
    md.append("| **Distractor Trap Design** | Format shocks & Sign traps | Partial truth options in Multi-Correct | Invariant violation traps | Rounding & Precision boundary traps | Intermediate product traps | Formula misapplication traps | Diagram misinterpretation traps |\n\n")

    md.append("---\n\n")

    # Allocation Plan
    md.append("## Recommended Allocation of the 20 Mock Examinations\n\n")
    md.append("The 20 mock examinations (40 individual papers) are allocated across all seven IIT profiles in strict accordance with historical dataset volume, structural diversity, and profile reliability:\n\n")
    md.append("| Mock Test | Assigned IIT Style Profile | Profile Identifier | Target Structure & Key Emphasis |\n")
    md.append("| :--- | :--- | :--- | :--- |\n")
    md.append("| **Mock 01** | IIT Bombay-inspired | `IIT_BOMBAY_STYLE` | Standard modern balanced format (54 Q/paper); high thermochemistry & electromagnetic rotation |\n")
    md.append("| **Mock 02** | IIT Bombay-inspired | `IIT_BOMBAY_STYLE` | 2015-style structural shock: high-penalty multi-correct and non-negative integer questions |\n")
    md.append("| **Mock 03** | IIT Bombay-inspired | `IIT_BOMBAY_STYLE` | Modern STEM numerical format with decimal ranges and functional calculus inequalities |\n")
    md.append("| **Mock 04** | IIT Delhi-inspired | `IIT_DELHI_STYLE` | Option-checking multi-correct dominance; edge-case boundary conditions in calculus |\n")
    md.append("| **Mock 05** | IIT Delhi-inspired | `IIT_DELHI_STYLE` | Circuit transient states (RC/LCR), wave interference, and stereochemical isomer counting |\n")
    md.append("| **Mock 06** | IIT Delhi-inspired | `IIT_DELHI_STYLE` | 2020-style analytical numerical focus in Paper 2 with coordination complex equilibrium |\n")
    md.append("| **Mock 07** | IIT Guwahati-inspired | `IIT_GUWAHATI_STYLE` | Conceptual symmetry and invariants; rapid elegant solutions over brute calculation |\n")
    md.append("| **Mock 08** | IIT Guwahati-inspired | `IIT_GUWAHATI_STYLE` | Elevated Modern Physics and Thermodynamics & Heat share; organic named reactions |\n")
    md.append("| **Mock 09** | IIT Guwahati-inspired | `IIT_GUWAHATI_STYLE` | 2023-style CBT calibration with clean vector geometry and phase equilibrium problems |\n")
    md.append("| **Mock 10** | IIT Kanpur-inspired | `IIT_KANPUR_STYLE` | Extreme numerical intensity; exact decimal tolerances; multi-step analytical derivations |\n")
    md.append("| **Mock 11** | IIT Kanpur-inspired | `IIT_KANPUR_STYLE` | Differential equations integrated with physical systems and quantitative solution chemistry |\n")
    md.append("| **Mock 12** | IIT Kanpur-inspired | `IIT_KANPUR_STYLE` | Heavy calculus integration, non-uniform mass distributions, and concentration cell EMF |\n")
    md.append("| **Mock 13** | IIT Kharagpur-inspired | `IIT_KHARAGPUR_STYLE` | Radical Paper 1 vs Paper 2 dichotomy: P1 Numerical/Multi-Correct, P2 Single Correct/Match Lists |\n")
    md.append("| **Mock 14** | IIT Kharagpur-inspired | `IIT_KHARAGPUR_STYLE` | Complex multi-reagent organic synthesis cascades; detailed physical context narratives |\n")
    md.append("| **Mock 15** | IIT Madras-inspired | `IIT_MADRAS_STYLE` | Electromagnetism prominence (induction, crossed fields); coordinate conics and complex vectors |\n")
    md.append("| **Mock 16** | IIT Madras-inspired | `IIT_MADRAS_STYLE` | High-tempo Paper 1 single-correct dominance + Paper 2 numerical challenge; qualitative salt analysis |\n")
    md.append("| **Mock 17** | IIT Madras-inspired | `IIT_MADRAS_STYLE` | Partial-marking multi-correct design (+4/+1/-2); LC oscillations and Faraday rail mechanics |\n")
    md.append("| **Mock 18** | IIT Roorkee-inspired | `IIT_ROORKEE_STYLE` | Mechanics dominance (45% of physics); rotational dynamics, rolling with slipping, fluid statics |\n")
    md.append("| **Mock 19** | IIT Roorkee-inspired | `IIT_ROORKEE_STYLE` | Highest graphical and schematic frequency; PV/TS thermodynamic cycles and ray optics diagrams |\n")
    md.append("| **Mock 20** | IIT Roorkee-inspired | `IIT_ROORKEE_STYLE` | Elaborate engineering/experimental problem statements; metallurgy and p-block chemistry |\n\n")

    md.append("---\n\n")

    # Solution Engine & Distinctiveness Validation
    md.append("## Solution Engine & Verification Protocols\n")
    md.append("Each mock examination solution will be generated under the unified pedagogical standard:\n")
    md.append("1. **First Critical Observation**: What physical/mathematical feature should immediately be noticed.\n")
    md.append("2. **Underlying Principle**: Identification of the governing laws and potential hidden traps.\n")
    md.append("3. **Step-by-Step Derivation**: Full analytical work without skipping algebraic intermediate steps.\n")
    md.append("4. **Alternative / Shortcut Approaches**: Elegant symmetry or dimension-based shortcuts where valid.\n")
    md.append("5. **Traps & Distractor Analysis**: Explicit explanation of why each incorrect option was selected by paper-setters.\n\n")

    md.append("## Approval Checkpoint\n")
    md.append("As mandated by the execution instruction, **all seven intelligence profiles and the 20-mock test allocation plan are submitted for user review and approval** prior to initiating the generation of individual mock examination questions.\n")

    return "".join(md)

if __name__ == '__main__':
    content = generate_markdown()
    with open('profiles/IIT_HISTORICAL_INTELLIGENCE_PROFILES.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Generated profiles/IIT_HISTORICAL_INTELLIGENCE_PROFILES.md')

