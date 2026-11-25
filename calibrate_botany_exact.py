# -*- coding: utf-8 -*-
with open('engine/neet_engine/curriculum_botany_diff.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Item 18 (Placentation) with Direct MCQ
old_18 = '''        # 18. Morphology - Placentation Types (Match List)
        ("Morphology of Flowering Plants", "Types of Placentation and Representative Plant Examples", "Match List",
         "Match List-I with List-II for placentation patterns and their characteristic plant examples:\\n\\n"
         "| List-I (Placentation Type) | List-II (Representative Plant Example) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Marginal | **I.** Pea ($Pisum sativum$) |\\n"
         "| **B.** Axile | **II.** China rose, Tomato, Lemon |\\n"
         "| **C.** Parietal | **III.** Mustard, Argemone (with false septum / replum) |\\n"
         "| **D.** Free central | **IV.** Dianthus and Primrose (ovules on central axis, no septa) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-IV, B-II, C-III, D-I"], 0,'''

new_18 = '''        # 18. Morphology - Placentation Types
        ("Morphology of Flowering Plants", "Types of Placentation and Representative Plant Examples", "Direct MCQ",
         "In which of the following pairs of plants are the ovules borne directly on a central axis with the septa being completely absent (Free central placentation)?",
         ["Dianthus and Primrose", "China rose and Tomato", "Mustard and Argemone", "Sunflower and Marigold"], 0,'''

# Replace Item 41 (Organ Modifications) with Direct MCQ
old_41 = '''        # 41. Morphology - Plant Organ Modifications (Match List)
        ("Morphology of Flowering Plants", "Homologous vs Analogous Plant Organ Modifications", "Match List",
         "Match List-I with List-II for plant morphological modifications and their anatomical organ derivations:\\n\\n"
         "| List-I (Modified Plant Structure) | List-II (True Morphological Organ of Origin) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Tendrils of Gourds (Cucumber, Pumpkin) | **I.** Stem modification (axillary buds) |\\n"
         "| **B.** Tendrils of Pea | **II.** Leaf modification (leaflets) |\\n"
         "| **C.** Thorns of $Citrus$ and $Bougainvillea$ | **III.** Stem modification (axillary buds) |\\n"
         "| **D.** Spines of $Opuntia$ (Prickly pear) | **IV.** Leaf modification (defense & transpiration reduction) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,'''

new_41 = '''        # 41. Morphology - Plant Organ Modifications
        ("Morphology of Flowering Plants", "Homologous vs Analogous Plant Organ Modifications", "Direct MCQ",
         "Tendrils in gourds (cucumber, pumpkin) and thorns in Citrus and Bougainvillea are homologous structures representing modifications of:",
         ["Axillary stem buds", "Foliar leaf blades", "Adventitious roots", "Stipules"], 0,'''

# Replace Item 47 (Microbial Organic Acids) with Direct MCQ
old_47 = '''        # 47. Microbes in Human Welfare - Organic Acids (Match List)
        ("Microbes in Human Welfare", "Industrial Microbial Production of Organic Acids", "Match List",
         "Match List-I with List-II for industrial organic chemicals and their microbial fermentation sources:\\n\\n"
         "| List-I (Industrial Product / Enzyme) | List-II (Microbial Producer Organism) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Citric acid | **I.** $Aspergillus niger$ (fungus) |\\n"
         "| **B.** Acetic acid (vinegar) | **II.** $Acetobacter aceti$ (bacterium) |\\n"
         "| **C.** Butyric acid | **III.** $Clostridium butylicum$ (bacterium) |\\n"
         "| **D.** Clot buster (Streptokinase) | **IV.** $Streptococcus$ (bacterium modified by genetic engineering) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,'''

new_47 = '''        # 47. Microbes in Human Welfare - Organic Acids
        ("Microbes in Human Welfare", "Industrial Microbial Production of Organic Acids", "Direct MCQ",
         "Citric acid, an organic acid widely used in food processing and pharmaceuticals, is produced on a commercial industrial scale by aerobic fermentation using which microorganism?",
         ["$Aspergillus niger$ (fungus)", "$Acetobacter aceti$ (bacterium)", "$Clostridium butylicum$ (bacterium)", "$Lactobacillus$ (bacterium)"], 0,'''

# Replace Item 38 (Pleiotropy) with Direct MCQ
old_38 = '''        # 38. Genetics - Pleiotropy vs Polygenic (Statement I & II)
        ("Principles of Inheritance and Variation", "Pleiotropy Manifestation vs Polygenic Inheritance", "Statement I & II",
         "Given below are two statements regarding non-Mendelian genetic phenomena:\\n\\n"
         "Statement I: Pleiotropy occurs when a single gene mutation influences multiple, seemingly unrelated phenotypic traits simultaneously (e.g. phenylketonuria in humans).\\n\\n"
         "Statement II: Polygenic inheritance occurs when multiple independent genes cumulatively influence a single quantitative phenotypic trait (e.g. human height and skin color).\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,'''

new_38 = '''        # 38. Genetics - Pleiotropy vs Polygenic
        ("Principles of Inheritance and Variation", "Pleiotropy Manifestation vs Polygenic Inheritance", "Direct MCQ",
         "The hereditary disease phenylketonuria in humans, where a single defective gene manifests simultaneously as mental retardation, eczema, and reduction in skin and hair pigmentation, is a classic example of:",
         ["Pleiotropy", "Polygenic inheritance", "Multiple allelism", "Incomplete dominance"], 0,'''

# Normalize CRLF
text = text.replace('\r\n', '\n')
old_18 = old_18.replace('\r\n', '\n')
new_18 = new_18.replace('\r\n', '\n')
old_41 = old_41.replace('\r\n', '\n')
new_41 = new_41.replace('\r\n', '\n')
old_47 = old_47.replace('\r\n', '\n')
new_47 = new_47.replace('\r\n', '\n')
old_38 = old_38.replace('\r\n', '\n')
new_38 = new_38.replace('\r\n', '\n')

assert old_18 in text, 'old_18 not found'
text = text.replace(old_18, new_18)
assert old_41 in text, 'old_41 not found'
text = text.replace(old_41, new_41)
assert old_47 in text, 'old_47 not found'
text = text.replace(old_47, new_47)
assert old_38 in text, 'old_38 not found'
text = text.replace(old_38, new_38)

# Clean any remaining \%
text = text.replace(r'\%', '%')

with open('engine/neet_engine/curriculum_botany_diff.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully calibrated Botany Diff to exact 2026 proportions!")

