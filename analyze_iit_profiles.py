import os, glob, re, json
from pypdf import PdfReader
from collections import defaultdict

folders = ['IIT BOMBAY', 'IIT DELHI', 'IIT Guwahati', 'IIT KANPUR', 'IIT KHARAGPUR', 'IIT MADRAS', 'IIT Roorkee']

physics_topics = {
    'Mechanics': ['velocity', 'acceleration', 'friction', 'momentum', 'collision', 'torque', 'angular', 'center of mass', 'gravitation', 'spring', 'pendulum', 'pulley', 'rotat', 'oscillation', 'shm', 'fluid', 'viscosity', 'surface tension', 'bernoulli', 'moment of inertia'],
    'Electromagnetism': ['electric field', 'charge', 'potential', 'capacit', 'current', 'resistance', 'resistor', 'magnetic', 'lorentz', 'induction', 'flux', 'solenoid', 'circuit', 'em wave', 'dipole', 'gauss', 'faraday', 'ampere', 'eddy'],
    'Thermodynamics & Heat': ['carnot', 'isothermal', 'adiabatic', 'entropy', 'ideal gas', 'heat capacity', 'molar heat', 'conduction', 'radiation', 'calorimet', 'thermodynamic', 'heat engine', 'stefan', 'wien'],
    'Optics & Wave Motion': ['wave', 'sound', 'doppler', 'string', 'lens', 'mirror', 'refraction', 'interference', 'diffraction', 'prism', 'focal', 'slit', 'optical', 'polarization', 'young'],
    'Modern Physics': ['photoelectric', 'bohr', 'de broglie', 'radioactive', 'decay', 'nucleus', 'x-ray', 'hydrogen atom', 'binding energy', 'work function', 'quantum', 'rutherford', 'fission', 'fusion']
}

chem_topics = {
    'Physical Chemistry': ['thermodynamics', 'enthalpy', 'entropy', 'gibbs', 'equilibrium', 'kinetics', 'rate constant', 'order', 'electrochemistry', 'nernst', 'conductance', 'solution', 'colligative', 'osmotic', 'vapor pressure', 'atomic structure', 'solid state', 'lattice', 'gaseous state', 'ideal gas', 'adsorption', 'surface chemistry', 'calorimeter', 'partial pressure', 'activation energy', 'mole fraction', 'electrolytic'],
    'Inorganic Chemistry': ['coordination', 'ligand', 'isomers', 'crystal field', 'p-block', 'd-block', 'f-block', 'metallurgy', 'extraction', 'qualitative', 'salt analysis', 'ore', 'bauxite', 'halogen', 'noble gas', 'bonding', 'hybridization', 'dipole moment', 'paramagnetic', 'diamagnetic', 'periodic', 'boron', 'silicon', 'lanthanoid', 'complex', 'oxidation state'],
    'Organic Chemistry': ['reaction sequence', 'product', 'reagent', 'alkene', 'alkyne', 'aromatic', 'benzene', 'electrophilic', 'nucleophilic', 'sn1', 'sn2', 'elimination', 'alcohol', 'phenol', 'ether', 'aldehyde', 'ketone', 'carboxylic', 'amine', 'diazonium', 'polymer', 'biomolecule', 'glucose', 'amino acid', 'carbohydrate', 'stereochemistry', 'enantiomer', 'diastereomer', 'chiral', 'ozonolysis', 'grignard', 'carbocation', 'tautomerism']
}

math_topics = {
    'Calculus': ['derivative', 'differentiab', 'continuous', 'integral', 'integration', 'area under', 'differential equation', 'maxima', 'minima', 'tangent', 'normal', 'limit', 'function', 'monotonic', 'rolle', 'mean value', 'definite integral', 'leibnitz'],
    'Algebra': ['quadratic', 'complex number', 'argument', 'modulus', 'progression', 'ap', 'gp', 'hp', 'permutation', 'combination', 'probability', 'binomial', 'matrices', 'matrix', 'determinant', 'system of equations', 'eigen', 'independent events', 'bayes'],
    'Coordinate Geometry': ['straight line', 'circle', 'parabola', 'ellipse', 'hyperbola', 'eccentricity', 'focus', 'directrix', 'chord', 'locus', 'asymptote', 'foci'],
    'Vectors & 3D Geometry': ['vector', 'dot product', 'cross product', 'plane', 'line in space', 'direction cosine', 'skew lines', 'coplanar', 'tetrahedron', 'scalar triple', 'vector triple'],
    'Trigonometry': ['sin', 'cos', 'tan', 'trigonometric', 'inverse trig', 'heights and distances', 'triangle properties', 'sine rule', 'cosine rule']
}

def classify_topics(text, sub):
    text_lower = text.lower()
    mapping = {}
    if sub == 'Physics':
        mapping = physics_topics
    elif sub == 'Chemistry':
        mapping = chem_topics
    elif sub == 'Mathematics':
        mapping = math_topics
    
    matched = []
    for topic, kws in mapping.items():
        for kw in kws:
            if re.search(r'\b' + re.escape(kw), text_lower):
                matched.append(topic)
                break
    return matched if matched else ['Uncategorized']

def analyze():
    all_data = {}
    for folder in folders:
        files = sorted(glob.glob(os.path.join(folder, '*.pdf')))
        folder_stats = {
            'iit': folder,
            'files_count': len(files),
            'years': set(),
            'total_questions': 0,
            'subject_counts': defaultdict(int),
            'q_type_counts': defaultdict(int),
            'topic_distribution': {
                'Physics': defaultdict(int),
                'Chemistry': defaultdict(int),
                'Mathematics': defaultdict(int)
            },
            'paper_stats': [],
            'avg_word_count': {'Physics': [], 'Chemistry': [], 'Mathematics': []},
            'diagram_count': {'Physics': 0, 'Chemistry': 0, 'Mathematics': 0},
            'multi_concept_count': {'Physics': 0, 'Chemistry': 0, 'Mathematics': 0},
            'numerical_details': {'decimal_range': 0, 'integer_exact': 0},
            'p1_vs_p2': {'Paper 1': defaultdict(int), 'Paper 2': defaultdict(int)},
            'year_profiles': defaultdict(lambda: {
                'total_q': 0,
                'q_types': defaultdict(int),
                'subjects': defaultdict(int)
            })
        }
        
        for f in files:
            fname = os.path.basename(f)
            reader = PdfReader(f)
            y_m = re.search(r'(20\d\d)', fname)
            year = y_m.group(1) if y_m else 'Unknown'
            p_m = re.search(r'Paper\s*([12])', fname, re.I)
            paper_num = f'Paper {p_m.group(1)}' if p_m else 'Unknown'
            
            folder_stats['years'].add(year)
            
            full_text = ''
            for p in reader.pages:
                full_text += (p.extract_text() or '') + '\n'
            
            # Normalize kerning
            full_text = re.sub(r'M\s+athematics', 'Mathematics', full_text)
            full_text = re.sub(r'M\s+CQ', 'MCQ', full_text)
            full_text = re.sub(r'M\s+ore', 'More', full_text)
            
            # Split into questions
            # Pattern: Q\d+\.
            q_splits = re.split(r'\nQ(\d+)\.', full_text)
            # q_splits[0] is header
            
            paper_entry = {
                'file': fname,
                'year': year,
                'paper': paper_num,
                'questions': []
            }
            
            current_subject = 'Unknown'
            
            # Check subject headers in text before Q1 or track as we go
            # Let's inspect each split block
            for idx in range(1, len(q_splits), 2):
                q_num = q_splits[idx]
                q_content = q_splits[idx+1] if idx+1 < len(q_splits) else ''
                
                # Check if subject header appeared right before or at top
                # Look for subject announcement in q_content or preceding text
                # Often ExamGoal has Chemistry18 questions, etc.
                sub_header = re.search(r'(Chemistry|Physics|Mathematics)\s*(\d+)?\s*questions?', q_content, re.I)
                if sub_header:
                    current_subject = sub_header.group(1).capitalize()
                
                # If subject is still Unknown, check question range
                # In JEE Advanced:
                # 66 questions: 1-22 Chem, 23-44 Math, 45-66 Phys (or similar)
                # 60 questions: 1-20 Chem, 21-40 Math, 41-60 Phys
                # 54 questions: 1-18 Chem, 19-36 Math, 37-54 Phys
                # 48 questions: 1-16 Chem, 17-32 Math, 33-48 Phys
                # 51 questions: 1-17 Chem, 18-34 Math, 35-51 Phys
                # 57 questions: 1-19 Chem, 20-38 Math, 39-57 Phys
                # Let's verify with subject markers inside text
                q_int = int(q_num)
                # Also check keywords inside question
                first_line = q_content.strip().split('\n')[0] if q_content.strip() else ''
                
                # Question type
                q_type = 'Single Correct'
                if 'Numerical' in first_line:
                    q_type = 'Numerical'
                elif 'More than One' in first_line or 'Multiple Correct' in first_line:
                    q_type = 'Multiple Correct'
                elif 'Single Correct' in first_line:
                    q_type = 'Single Correct'
                elif 'Matrix' in first_line or 'Match' in first_line:
                    q_type = 'Matrix Match'
                elif 'Paragraph' in first_line or 'Comprehension' in first_line:
                    q_type = 'Paragraph'
                else:
                    # check first 100 chars
                    intro = q_content[:150]
                    if 'Numerical' in intro:
                        q_type = 'Numerical'
                    elif 'More than One' in intro or 'Multiple Correct' in intro:
                        q_type = 'Multiple Correct'
                    elif 'Single Correct' in intro:
                        q_type = 'Single Correct'
                    elif 'Matrix' in intro or 'Match' in intro:
                        q_type = 'Matrix Match'
                    elif 'List-I' in intro or 'List - I' in intro:
                        q_type = 'Match List'
                
                # Check subject heuristic if not announced
                # Usually sections are grouped in thirds
                total_in_paper = len(q_splits) // 2
                third = max(1, total_in_paper // 3)
                inferred_sub = current_subject
                if inferred_sub == 'Unknown':
                    if q_int <= third:
                        inferred_sub = 'Chemistry'
                    elif q_int <= 2 * third:
                        inferred_sub = 'Mathematics'
                    else:
                        inferred_sub = 'Physics'
                
                # Verify inferred sub with subject markers
                # If text contains "Physics" or "Chemistry" or "Mathematics" header
                if 'Physics' in q_content[:80]:
                    inferred_sub = 'Physics'
                elif 'Chemistry' in q_content[:80]:
                    inferred_sub = 'Chemistry'
                elif 'Mathematics' in q_content[:80]:
                    inferred_sub = 'Mathematics'
                current_subject = inferred_sub
                
                # Topic detection
                topics = classify_topics(q_content, current_subject)
                
                # Indicators
                words = re.findall(r'\b[A-Za-z]{2,}\b', q_content)
                word_count = len(words)
                
                has_diagram = bool(re.search(r'\b(figure|graph|plot|shown in figure|circuit|diagram|ray|lens|mirror|schematic|table|List-I)\b', q_content, re.I))
                is_multi_concept = len(topics) > 1
                
                # Numerical type
                if q_type == 'Numerical':
                    if re.search(r'to\s+\d+\.\d+|\.\d{2}', q_content):
                        folder_stats['numerical_details']['decimal_range'] += 1
                    else:
                        folder_stats['numerical_details']['integer_exact'] += 1
                
                # Aggregate
                folder_stats['total_questions'] += 1
                folder_stats['subject_counts'][current_subject] += 1
                folder_stats['q_type_counts'][q_type] += 1
                for t in topics:
                    folder_stats['topic_distribution'][current_subject][t] += 1
                folder_stats['avg_word_count'][current_subject].append(word_count)
                if has_diagram:
                    folder_stats['diagram_count'][current_subject] += 1
                if is_multi_concept:
                    folder_stats['multi_concept_count'][current_subject] += 1
                
                folder_stats['p1_vs_p2'][paper_num][q_type] += 1
                folder_stats['year_profiles'][year]['total_q'] += 1
                folder_stats['year_profiles'][year]['q_types'][q_type] += 1
                folder_stats['year_profiles'][year]['subjects'][current_subject] += 1
                
                paper_entry['questions'].append({
                    'q_num': q_int,
                    'subject': current_subject,
                    'type': q_type,
                    'topics': topics,
                    'word_count': word_count,
                    'has_diagram': has_diagram,
                    'is_multi_concept': is_multi_concept
                })
            folder_stats['paper_stats'].append(paper_entry)
        
        folder_stats['years'] = sorted(list(folder_stats['years']))
        # calculate averages
        for s in ['Physics', 'Chemistry', 'Mathematics']:
            wc_list = folder_stats['avg_word_count'][s]
            folder_stats['avg_word_count'][s] = round(sum(wc_list)/len(wc_list), 1) if wc_list else 0
        
        all_data[folder] = folder_stats

    # Convert defaultdicts to dicts for json dump
    def default_to_dict(d):
        if isinstance(d, defaultdict):
            d = {k: default_to_dict(v) for k, v in d.items()}
        elif isinstance(d, dict):
            d = {k: default_to_dict(v) for k, v in d.items()}
        elif isinstance(d, list):
            d = [default_to_dict(v) for v in d]
        return d

    clean_data = default_to_dict(all_data)
    with open('iit_analysis_summary.json', 'w', encoding='utf-8') as out:
        json.dump(clean_data, out, indent=2)
    print('Analysis complete. Written to iit_analysis_summary.json')

if __name__ == '__main__':
    analyze()

