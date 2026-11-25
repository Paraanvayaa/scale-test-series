# -*- coding: utf-8 -*-
with open('engine/neet_engine/curriculum_zoology_diff.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Item 10 (ART) with Direct MCQ
old_10 = '''        # 10. Reproductive Health - ART Techniques (Match List)
        ("Reproductive Health", "Assisted Reproductive Technologies Clinical Indications", "Match List",
         "Match List-I with List-II for Assisted Reproductive Technology (ART) procedures and their clinical definitions:\\n\\n"
         "| List-I (ART Procedure) | List-II (Clinical Methodology) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** ZIFT (Zygote Intra-Fallopian Transfer) | **I.** Transfer of zygote or early embryo up to $8$ blastomeres into fallopian tube |\\n"
         "| **B.** IUT (Intra-Uterine Transfer) | **II.** Transfer of embryo with more than $8$ blastomeres directly into uterus |\\n"
         "| **C.** GIFT (Gamete Intra-Fallopian Transfer) | **III.** Transfer of an ovum collected from a donor into fallopian tube of female |\\n"
         "| **D.** ICSI (Intra-Cytoplasmic Sperm Injection) | **IV.** Direct microinjection of a single sperm into ovum cytoplasm in vitro |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,'''

new_10 = '''        # 10. Reproductive Health - ART Techniques
        ("Reproductive Health", "Assisted Reproductive Technologies Clinical Indications", "Direct MCQ",
         "A specialized Assisted Reproductive Technology (ART) procedure in which a single sperm is directly microinjected into the cytoplasm of an ovum in the laboratory to form an embryo is:",
         ["Intra-Cytoplasmic Sperm Injection (ICSI)", "Zygote Intra-Fallopian Transfer (ZIFT)", "Gamete Intra-Fallopian Transfer (GIFT)", "Intra-Uterine Insemination (IUI)"], 0,'''

# Replace Item 47 (Endocrine Disorders) with Direct MCQ
old_47 = '''        # 47. Endocrine - Endocrine Disorders (Match List)
        ("Chemical Coordination and Integration", "Endocrine Hypersecretion and Hyposecretion Clinical Syndromes", "Match List",
         "Match List-I with List-II for endocrine disorders and their underlying hormonal etiologies:\\n\\n"
         "| List-I (Endocrine Disorder) | List-II (Hormonal Etiology & Clinical Symptoms) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Addison\\'s disease | **I.** Hyposecretion of adrenal cortex hormones; bronze skin, hypoglycemia |\\n"
         "| **B.** Cushing\\'s syndrome | **II.** Hypersecretion of cortisol; moon face, buffalo hump, hyperglycemia |\\n"
         "| **C.** Graves\\' disease (Exophthalmic goitre) | **III.** Hyperthyroidism; protruding eyeballs (exophthalmos), elevated BMR |\\n"
         "| **D.** Acromegaly | **IV.** Hypersecretion of Growth Hormone (GH) in adults; facial bone disfigurement |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,'''

new_47 = '''        # 47. Endocrine - Endocrine Disorders
        ("Chemical Coordination and Integration", "Endocrine Hypersecretion and Hyposecretion Clinical Syndromes", "Direct MCQ",
         "A patient diagnosed with hypersecretion of cortisol from the adrenal cortex presenting with central obesity, 'moon face', 'buffalo hump', hypertension, and persistent hyperglycemia suffers from:",
         ["Cushing\\'s syndrome", "Addison\\'s disease", "Graves\\' disease", "Acromegaly"], 0,'''

# Normalize CRLF
text = text.replace('\r\n', '\n')
old_10 = old_10.replace('\r\n', '\n')
new_10 = new_10.replace('\r\n', '\n')
old_47 = old_47.replace('\r\n', '\n')
new_47 = new_47.replace('\r\n', '\n')

assert old_10 in text, 'old_10 not found'
text = text.replace(old_10, new_10)
assert old_47 in text, 'old_47 not found'
text = text.replace(old_47, new_47)

# Clean any remaining \%
text = text.replace(r'\%', '%')

with open('engine/neet_engine/curriculum_zoology_diff.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully calibrated Zoology Diff to exact 2026 proportions!")

