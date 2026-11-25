# -*- coding: utf-8 -*-
"""
Calibrate curriculum_chemistry_mod.py and curriculum_botany_mod.py
to match exact 2026 NEET proportions:
- Direct MCQ: 29
- Statement I & II: 7
- Match List: 7
- Assertion & Reason: 4
- Multi-Statement: 3
Total: 50
"""
import re

# 1. Update curriculum_chemistry_mod.py
with open("engine/neet_engine/curriculum_chemistry_mod.py", "r", encoding="utf-8") as f:
    chem = f.read()

# Let's inspect current types in chem
# We need to change specific topics
print("Updating Chemistry...")

# Statement I & II conversions:
# A) Acidic Strength Comparison of Substituted Phenols (Topic 21)
old_chem_p1 = '''        # 21. Alcohols: Acidic Strength of Phenols
        ("Alcohols, Phenols and Ethers", "Acidic Strength Comparison of Substituted Phenols", "Direct MCQ",
         "The correct decreasing order of acidic strength among the following substituted phenols is:",
         ["2,4,6-Trinitrophenol (Picric acid) > 4-Nitrophenol > 4-Chlorophenol > Phenol > 4-Methoxyphenol",
          "Phenol > 4-Nitrophenol > 4-Methoxyphenol > Picric acid",
          "4-Methoxyphenol > Phenol > 4-Chlorophenol > 4-Nitrophenol",
          "Picric acid > 4-Methoxyphenol > 4-Nitrophenol > Phenol"], 0,'''

new_chem_p1 = '''        # 21. Alcohols: Acidic Strength of Phenols
        ("Alcohols, Phenols and Ethers", "Acidic Strength Comparison of Substituted Phenols", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "**Statement I:** 2,4,6-Trinitrophenol (picric acid) is a much stronger acid than phenol and even stronger than acetic acid ($pK_a = 0.38$).\\n\\n"
         "**Statement II:** The presence of three strongly electron-withdrawing nitro groups ($-\\text{NO}_2$) at ortho and para positions powerfully stabilizes the conjugate phenoxide anion via strong $-M$ and $-I$ resonance delocalization.\\n\\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,'''

chem = chem.replace(old_chem_p1, new_chem_p1)

# B) Negative Deviation from Raoult's Law (Topic 3)
old_chem_p2 = '''        # 3. Solutions: Non-Ideal Solutions Raoult's Law Deviation
        ("Solutions", "Negative Deviation from Raoult's Law and Intermolecular H-Bonding", "Direct MCQ",
         "A mixture of acetone ($\\text{CH}_3\\text{COCH}_3$) and chloroform ($\\text{CHCl}_3$) exhibits negative deviation from Raoult's law. This negative deviation occurs because:",
         ["Intermolecular hydrogen bonding between acetone and chloroform ($A-B$ attraction) is stronger than $A-A$ and $B-B$ interactions",
          "Intermolecular forces between acetone and chloroform are weaker than pure component interactions",
          "The mixing process is endothermic ($\\Delta H_{\\text{mix}} > 0$)",
          "Volume increases upon mixing ($\\Delta V_{\\text{mix}} > 0$)"], 0,'''

new_chem_p2 = '''        # 3. Solutions: Non-Ideal Solutions Raoult's Law Deviation
        ("Solutions", "Negative Deviation from Raoult's Law and Intermolecular H-Bonding", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "**Statement I:** A liquid mixture of acetone and chloroform exhibits negative deviation from Raoult's law and forms a maximum boiling azeotrope.\\n\\n"
         "**Statement II:** Mixing acetone and chloroform leads to intermolecular hydrogen bonding between chloroform hydrogen and acetone carbonyl oxygen ($A-B$ attraction), which is stronger than the attractive interactions between like molecules ($A-A$ and $B-B$).\\n\\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,'''

chem = chem.replace(old_chem_p2, new_chem_p2)

# C) Lead storage battery (Topic 5)
old_chem_p3 = '''        # 5. Electrochemistry: Lead Storage Battery
        ("Electrochemistry", "Reactions in Lead Storage Battery During Discharge", "Direct MCQ",
         "During the discharging of a lead storage battery in an automobile, which of the following chemical processes occurs?",
         ["$\\text{PbSO}_4(s)$ is formed at both anode and cathode, and sulphuric acid is consumed (density of $\\text{H}_2\\text{SO}_4$ decreases)",
          "$\\text{PbO}_2$ is deposited on the anode and $\\text{Pb}$ on the cathode",
          "Concentration of sulphuric acid increases",
          "$\\text{SO}_2$ gas is liberated at the anode"], 0,'''

new_chem_p3 = '''        # 5. Electrochemistry: Lead Storage Battery
        ("Electrochemistry", "Reactions in Lead Storage Battery During Discharge", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "**Statement I:** During the discharge of a lead storage battery, insoluble lead sulphate ($\\text{PbSO}_4$) is deposited on both the lead anode and the lead dioxide cathode.\\n\\n"
         "**Statement II:** During discharge, sulphuric acid ($\\text{H}_2\\text{SO}_4$) is consumed, causing the specific gravity and density of the battery electrolyte to decrease.\\n\\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,'''

chem = chem.replace(old_chem_p3, new_chem_p3)

# D) Disproportionation of Manganate(VI) (Topic 15)
old_chem_p4 = '''        # 15. d-Block: Manganate Disproportionation
        ("The d- and f-Block Elements", "Disproportionation of Manganate(VI) in Acidic Medium", "Direct MCQ",
         "In neutral or acidic aqueous solution, green manganate ion ($\\text{MnO}_4^{2-}$) is unstable and undergoes disproportionation. The balanced products are:",
         ["Permanganate ($\\text{MnO}_4^-$) and Manganese dioxide ($\\text{MnO}_2$)",
          "$\\text{Mn}^{2+}$ and oxygen gas",
          "$\\text{MnO}_2$ and ozone",
          "Permanganate ($\\text{MnO}_4^-$) and $\\text{Mn}^{2+}$ ions only"], 0,'''

new_chem_p4 = '''        # 15. d-Block: Manganate Disproportionation
        ("The d- and f-Block Elements", "Disproportionation of Manganate(VI) in Acidic Medium", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "**Statement I:** In acidic or neutral aqueous solution, dark green manganate ions ($\\text{MnO}_4^{2-}$) are thermodynamically unstable and disproportionate into purple permanganate ($\\text{MnO}_4^-$) and brown manganese dioxide ($\\text{MnO}_2$).\\n\\n"
         "**Statement II:** In strongly alkaline solutions, manganate ion ($\\text{MnO}_4^{2-}$) is stable and does not undergo disproportionation.\\n\\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,'''

chem = chem.replace(old_chem_p4, new_chem_p4)

# E) SN1 Stereochemistry (Topic 20)
old_chem_p5 = '''        # 20. Haloalkanes: SN1 Stereochemistry
        ("Haloalkanes and Haloarenes", "Stereochemical Fate of Chiral Substrates in SN1", "Direct MCQ",
         "When an optically active pure enantiomer of a secondary alkyl halide undergoes nucleophilic substitution via an $S_N1$ mechanism, the product typically exhibits:",
         ["Partial racemization with an excess of inversion of configuration",
          "Complete retention of configuration ($100\\%$)",
          "Complete inversion of configuration ($100\\%$ Walden inversion)",
          "Zero optical rotation due to exactly $50:50$ racemic mixture"], 0,'''

new_chem_p5 = '''        # 20. Haloalkanes: SN1 Stereochemistry
        ("Haloalkanes and Haloarenes", "Stereochemical Fate of Chiral Substrates in SN1", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "**Statement I:** An $S_N1$ reaction of an optically active haloalkane at an asymmetric chiral carbon always results in partial racemization accompanied by net excess of inversion of configuration.\\n\\n"
         "**Statement II:** The departing halide leaving group momentarily blocks the front side of the carbocation as an intimate ion-pair, forcing the incoming nucleophile to attack more frequently from the opposite (rear) side.\\n\\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,'''

chem = chem.replace(old_chem_p5, new_chem_p5)

# Match List conversions:
# F) Coordination complexes (Topic 2)
old_chem_m1 = '''        # 2. Solutions: Freezing Point of Coordination Complex
        ("Solutions", "Freezing Point Depression and Complex Formula", "Direct MCQ",
         "A $0.01\\text{ m}$ aqueous solution of a coordination compound of cobalt with empirical formula $\\text{CoCl}_3\\cdot 5\\text{NH}_3$ freezes at $-0.0558^\\circ\\text{C}$. Given $K_f = 1.86\\text{ K kg mol}^{-1}$ for water, the structural formula of the complex is:",
         ["$[\\text{Co}(\\text{NH}_3)_5\\text{Cl}]\\text{Cl}_2$ (yielding 3 ions)",
          "$[\\text{Co}(\\text{NH}_3)_5]\\text{Cl}_3$ (yielding 4 ions)",
          "$[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]\\text{Cl}\\cdot\\text{NH}_3$",
          "$[\\text{Co}(\\text{NH}_3)_3\\text{Cl}_3]\\cdot 2\\text{NH}_3$"], 0,'''

new_chem_m1 = '''        # 2. Solutions: Freezing Point of Coordination Complex
        ("Solutions", "Coordination Complexes and Ionization in Aqueous Solution", "Match List",
         "Match List-I with List-II:\\n\\n"
         "| List-I (Werner Complex Formula) | List-II (Total Number of Ions Produced per Formula Unit) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** $[\\text{Co}(\\text{NH}_3)_6]\\text{Cl}_3$ | **I.** 4 ions (van 't Hoff factor $i = 4$) |\\n"
         "| **B.** $[\\text{Co}(\\text{NH}_3)_5\\text{Cl}]\\text{Cl}_2$ | **II.** 3 ions (van 't Hoff factor $i = 3$) |\\n"
         "| **C.** $[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]\\text{Cl}$ | **III.** 2 ions (van 't Hoff factor $i = 2$) |\\n"
         "| **D.** $[\\text{Co}(\\text{NH}_3)_3\\text{Cl}_3]$ | **IV.** 0 ions (non-electrolyte, $i = 1$) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-IV, B-III, C-II, D-I"], 0,'''

chem = chem.replace(old_chem_m1, new_chem_m1)

# G) Organic functional tests (Topic 22)
old_chem_m2 = '''        # 22. Aldehydes: Clemmensen vs Wolff-Kishner
        ("Aldehydes, Ketones and Carboxylic Acids", "Selective Carbonyl Reduction Reagents", "Direct MCQ",
         "To convert 4-oxobutanoic acid ($\\text{OHC}-\\text{CH}_2\\text{CH}_2-\\text{COOH}$) into butanoic acid without affecting the carboxylic acid group, which reagent is most appropriate?",
         ["Wolff-Kishner reduction ($\\text{NH}_2\\text{NH}_2 / \\text{KOH} / \\text{glycol}$, heat)",
          "Clemmensen reduction ($\\text{Zn}-\\text{Hg} / \\text{conc. }\\text{HCl}$)",
          "$\\text{LiAlH}_4$ in dry ether",
          "$\\text{NaBH}_4$ in ethanol"], 0,'''

new_chem_m2 = '''        # 22. Aldehydes: Clemmensen vs Wolff-Kishner
        ("Aldehydes, Ketones and Carboxylic Acids", "Organic Functional Group Diagnostic Reagents", "Match List",
         "Match List-I with List-II:\\n\\n"
         "| List-I (Diagnostic Chemical Test) | List-II (Specific Functional Group Detected) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Lucas test (anhydrous $\\text{ZnCl}_2 + \\text{conc. HCl}$) | **I.** Distinction among $1^\\circ, 2^\\circ,$ and $3^\\circ$ alcohols |\\n"
         "| **B.** Iodoform test ($\\text{I}_2 + \\text{NaOH}$) | **II.** Methyl ketones ($\\text{CH}_3\\text{CO}-$) and $\\text{CH}_3\\text{CH(OH)}-$ groups |\\n"
         "| **C.** Tollens' test (Ammoniacal $\\text{AgNO}_3$) | **III.** Aldehydes (produces silver mirror) |\\n"
         "| **D.** Carbylamine test ($\\text{CHCl}_3 + \\text{alc. KOH}$) | **IV.** Primary amines ($1^\\circ$ aliphatic and aromatic) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-II, C-I, D-IV"], 0,'''

chem = chem.replace(old_chem_m2, new_chem_m2)

# H) Qualitative inorganic cations (Topic 25)
old_chem_m3 = '''        # 25. Practical Chemistry: Cation Group Separation
        ("Practical Chemistry", "Group II vs Group IV Cation Precipitation Reagents", "Direct MCQ",
         "In qualitative inorganic salt analysis, Group II cations (e.g. $\\text{Cu}^{2+}, \\text{Pb}^{2+}$) and Group IV cations (e.g. $\\text{Zn}^{2+}, \\text{Ni}^{2+}$) are both precipitated as sulphides using $\\text{H}_2\\text{S}$ gas. Why are Group IV cations NOT precipitated in Group II?",
         ["In Group II, dilute $\\text{HCl}$ suppresses the ionization of $\\text{H}_2\\text{S}$ via common ion effect ($\\text{H}^+$), keeping $[\\text{S}^{2-}]$ low enough to exceed only the very low $K_{sp}$ of Group II sulphides",
          "Group IV sulphides are soluble in water at all temperatures",
          "$\\text{HCl}$ oxidises Group IV cations into soluble oxoanions",
          "Group IV cations do not form sulphides with $\\text{H}_2\\text{S}$"], 0,'''

new_chem_m3 = '''        # 25. Practical Chemistry: Cation Group Separation
        ("Practical Chemistry", "Qualitative Cation Analysis Group Reagents", "Match List",
         "Match List-I with List-II:\\n\\n"
         "| List-I (Analytical Cation Group) | List-II (Specific Group Precipitation Reagent) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Group I ($\\text{Pb}^{2+}, \\text{Ag}^+$) | **I.** Dilute $\\text{HCl}$ (precipitated as chlorides) |\\n"
         "| **B.** Group II ($\\text{Cu}^{2+}, \\text{Pb}^{2+}, \\text{Cd}^{2+}$) | **II.** $\\text{H}_2\\text{S}$ gas in presence of dilute $\\text{HCl}$ |\\n"
         "| **C.** Group III ($\\text{Fe}^{3+}, \\text{Al}^{3+}, \\text{Cr}^{3+}$) | **III.** $\\text{NH}_4\\text{OH}$ in presence of excess $\\text{NH}_4\\text{Cl}$ |\\n"
         "| **D.** Group IV ($\\text{Zn}^{2+}, \\text{Ni}^{2+}, \\text{Mn}^{2+}$) | **IV.** $\\text{H}_2\\text{S}$ gas in presence of $\\text{NH}_4\\text{OH}$ and $\\text{NH}_4\\text{Cl}$ |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-III, C-II, D-IV",
          "A-IV, B-II, C-III, D-I"], 0,'''

chem = chem.replace(old_chem_m3, new_chem_m3)

# Assertion & Reason conversions:
# I) Lewis acid boron (Topic 11)
old_chem_ar1 = '''        # 11. Chemical Bonding: Back Bonding in Boron Halides
        ("Chemical Bonding and Molecular Structure", "Lewis Acid Strength of Boron Trihalides", "Direct MCQ",
         "The correct increasing order of Lewis acid strength among boron trihalides is:",
         ["$\\text{BF}_3 < \\text{BCl}_3 < \\text{BBr}_3 < \\text{BI}_3$",
          "$\\text{BI}_3 < \\text{BBr}_3 < \\text{BCl}_3 < \\text{BF}_3$",
          "$\\text{BF}_3 < \\text{BI}_3 < \\text{BCl}_3 < \\text{BBr}_3$",
          "$\\text{BCl}_3 < \\text{BF}_3 < \\text{BBr}_3 < \\text{BI}_3$"], 0,'''

new_chem_ar1 = '''        # 11. Chemical Bonding: Back Bonding in Boron Halides
        ("Chemical Bonding and Molecular Structure", "Lewis Acid Strength of Boron Trihalides", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\\n\\n"
         "**Assertion (A):** The Lewis acid strength of boron trihalides follows the order: $\\text{BF}_3 < \\text{BCl}_3 < \\text{BBr}_3 < \\text{BI}_3$, despite fluorine being the most electronegative halogen.\\n\\n"
         "**Reason (R):** Strong $p\\pi-p\\pi$ back-bonding occurs between the filled $2p$ orbital of fluorine and the vacant $2p$ orbital of boron due to effective size and energy match, which significantly reduces electron deficiency at the boron atom in $\\text{BF}_3$.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,'''

chem = chem.replace(old_chem_ar1, new_chem_ar1)

# J) Ortho effect benzoic (Topic 17)
old_chem_ar2 = '''        # 17. Organic Principles: Ortho Effect in Benzoic Acids
        ("Organic Chemistry - Some Basic Principles", "Ortho Effect on Acid Strength of Benzoic Acids", "Direct MCQ",
         "Among the following substituted benzoic acids, which compound exhibits the highest acidic strength ($pK_a$ lowest)?",
         ["2-Methylbenzoic acid (o-Toluic acid)",
          "4-Methylbenzoic acid (p-Toluic acid)",
          "3-Methylbenzoic acid (m-Toluic acid)",
          "Benzoic acid"], 0,'''

new_chem_ar2 = '''        # 17. Organic Principles: Ortho Effect in Benzoic Acids
        ("Organic Chemistry - Some Basic Principles", "Ortho Effect on Acid Strength of Benzoic Acids", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\\n\\n"
         "**Assertion (A):** 2-Methylbenzoic acid (o-toluic acid) is a stronger acid than benzoic acid, despite the methyl group having an electron-donating ($+I$ and hyperconjugative) effect.\\n\\n"
         "**Reason (R):** Due to steric hindrance (ortho-effect), the bulky ortho substituent twists the carboxyl group out of the benzene ring plane, inhibiting resonance with the ring and facilitating resonance stabilization of the carboxylate anion.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,'''

chem = chem.replace(old_chem_ar2, new_chem_ar2)

# K) Anisole ether cleavage (Topic 32)
old_chem_ar3 = '''        ("Alcohols, Phenols and Ethers", "Ether Cleavage with Excess Hot Concentrated HI", "Direct MCQ",
         "When anisole (methoxybenzene, $\\text{C}_6\\text{H}_5\\text{OCH}_3$) is heated with concentrated hydroiodic acid ($\\text{HI}$), the products formed are:",
         ["Phenol and Iodomethane ($\\text{CH}_3\\text{I}$)",
          "Iodobenzene and Methanol",
          "Phenol and Methanol",
          "Iodobenzene and Iodomethane"], 0,'''

new_chem_ar3 = '''        ("Alcohols, Phenols and Ethers", "Ether Cleavage with Excess Hot Concentrated HI", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\\n\\n"
         "**Assertion (A):** Heating anisole (methoxybenzene) with concentrated hydroiodic acid ($\\text{HI}$) yields phenol and iodomethane ($\\text{CH}_3\\text{I}$), but never iodobenzene and methanol.\\n\\n"
         "**Reason (R):** The phenyl-oxygen bond ($\\text{C}_{sp^2}-\\text{O}$) possesses partial double-bond character due to resonance and is stronger than the methyl-oxygen single bond ($\\text{C}_{sp^3}-\\text{O}$).\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,'''

chem = chem.replace(old_chem_ar3, new_chem_ar3)

# L) Hydrolysis of XeF4 (Topic 16)
old_chem_ar4 = '''        # 16. p-Block: Hydrolysis of XeF4
        ("p-Block Elements", "Disproportionation Hydrolysis of Xenon Tetrafluoride", "Direct MCQ",
         "The complete hydrolysis of xenon tetrafluoride ($\\text{XeF}_4$) at room temperature is a disproportionation reaction yielding:",
         ["$\\text{Xe}, \\text{XeO}_3, \\text{HF},$ and $\\text{O}_2$",
          "$\\text{XeO}_3$ and $\\text{HF}$ only",
          "$\\text{XeOF}_4$ and $\\text{HF}$ only",
          "$\\text{Xe}$ and $\\text{F}_2$ gases"], 0,'''

new_chem_ar4 = '''        # 16. p-Block: Hydrolysis of XeF4
        ("p-Block Elements", "Disproportionation Hydrolysis of Xenon Tetrafluoride", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\\n\\n"
         "**Assertion (A):** The complete hydrolysis of xenon tetrafluoride ($\\text{XeF}_4$) at room temperature is a redox disproportionation reaction yielding both elemental xenon ($\\text{Xe}$) and xenon trioxide ($\\text{XeO}_3$).\\n\\n"
         "**Reason (R):** In $\\text{XeF}_4$, xenon is in the $+4$ oxidation state, which is thermodynamically unstable towards self-oxidation to $+6$ (in $\\text{XeO}_3$) and reduction to $0$ (in $\\text{Xe}$).\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,'''

chem = chem.replace(old_chem_ar4, new_chem_ar4)

# Multi-statement conversions:
# M) Aromaticity (Topic 18)
old_chem_ms1 = '''        # 18. Organic Principles: Aromaticity
        ("Organic Chemistry - Some Basic Principles", "Hückel's Rule of Aromaticity in Cyclic Ions", "Direct MCQ",
         "Which of the following species is NON-AROMATIC according to Hückel's $(4n+2)\\pi$ rule due to non-planar tub-shaped conformation?",
         ["Cyclooctatetraene (COT, $\\text{C}_8\\text{H}_8$)",
          "Tropylium cation ($\\text{C}_7\\text{H}_7^+$)",
          "Cyclopentadienyl anion ($\\text{C}_5\\text{H}_5^-$)",
          "Benzene ($\\text{C}_6\\text{H}_6$)"], 0,'''

new_chem_ms1 = '''        # 18. Organic Principles: Aromaticity
        ("Organic Chemistry - Some Basic Principles", "Hückel's Rule of Aromaticity in Cyclic Systems", "Multi-Statement",
         "Which of the following chemical species are AROMATIC according to Hückel's $(4n+2)\\pi$ electron rule?\\n\\n"
         "A. Benzene ($\\text{C}_6\\text{H}_6$, $6\\pi$ electrons, planar cyclic conjugated ring)\\n"
         "B. Tropylium cation ($\\text{C}_7\\text{H}_7^+$, $6\\pi$ electrons, planar cycloheptatrienyl cation)\\n"
         "C. Cyclopentadienyl anion ($\\text{C}_5\\text{H}_5^-$, $6\\pi$ electrons, planar ring)\\n"
         "D. Cyclooctatetraene (COT, $\\text{C}_8\\text{H}_8$, adopting a non-planar tub conformation)\\n"
         "E. Pyridine (heterocyclic $6\\pi$ aromatic ring)\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A, B, C and E only",
          "A, B and C only",
          "B, C, D and E only",
          "A, C and D only"], 0,'''

chem = chem.replace(old_chem_ms1, new_chem_ms1)

# N) Saytzeff vs Hofmann (Topic 31)
old_chem_ms2 = '''        ("Haloalkanes and Haloarenes", "Saytzeff vs Hofmann Elimination", "Direct MCQ",
         "When 2-bromobutane is heated with alcoholic $\\text{KOH}$, the major alkene formed is but-2-ene according to Saytzeff's rule. But when heated with bulky potassium tert-butoxide ($(\\text{CH}_3)_3\\text{CO}^-\\text{K}^+$), the major product is:",
         ["But-1-ene (Hofmann product) due to steric hindrance of the bulky base",
          "trans-But-2-ene",
          "cis-But-2-ene",
          "Butan-2-ol"], 0,'''

new_chem_ms2 = '''        ("Haloalkanes and Haloarenes", "Saytzeff vs Hofmann Elimination Rules", "Multi-Statement",
         "Which of the following statements regarding dehydrohalogenation ($E_2$ elimination) of alkyl halides are correct?\\n\\n"
         "A. Dehydrohalogenation with small unhindered bases (e.g. $\\text{C}_2\\text{H}_5\\text{O}^- / \\text{C}_2\\text{H}_5\\text{OH}$) predominantly yields the more substituted, thermally stable alkene (Saytzeff product).\\n"
         "B. Dehydrohalogenation with bulky, sterically hindered bases (e.g. $(\\text{CH}_3)_3\\text{CO}^-\\text{K}^+$) yields the less substituted terminal alkene (Hofmann product) as the major product.\\n"
         "C. Dehydrohalogenation of alkyl fluorides predominantly yields the Hofmann alkene due to the strong $-I$ effect and poor leaving ability of fluoride.\\n"
         "D. $E_2$ elimination reactions proceed via a stable free carbocation intermediate that frequently undergoes rearrangement.\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A, B and C only",
          "A and B only",
          "B, C and D only",
          "A, B, C and D"], 0,'''

chem = chem.replace(old_chem_ms2, new_chem_ms2)

# O) Coloured ions in d-Block (Topic 28)
old_chem_ms3 = '''        ("The d- and f-Block Elements", "Coloured Ions in d-Block", "Direct MCQ",
         "Which of the following transition metal ions is COLOURLESS in aqueous solution due to the absence of $d-d$ electronic transitions?",
         ["$\\text{Sc}^{3+}$ ($3d^0$) and $\\text{Zn}^{2+}$ ($3d^{10}$)",
          "$\\text{Cu}^{2+}$ ($3d^9$)",
          "$\\text{Ti}^{3+}$ ($3d^1$)",
          "$\\text{Fe}^{3+}$ ($3d^5$)"], 0,'''

new_chem_ms3 = '''        ("The d- and f-Block Elements", "Electronic Transitions and Coloured Ions in d-Block", "Multi-Statement",
         "Which of the following statements regarding the colour and electronic properties of transition metal ions are correct?\\n\\n"
         "A. $\\text{Sc}^{3+}$ ($3d^0$) is colourless in aqueous solution because it possesses no $d$-electrons to undergo $d-d$ transitions.\\n"
         "B. $\\text{Zn}^{2+}$ ($3d^{10}$) is colourless in aqueous solution because its $d$-subshell is completely filled, leaving no vacant orbital for excitation.\\n"
         "C. $\\text{Cu}^{2+}$ ($3d^9$) ions impart a characteristic blue colour to aqueous solutions due to visible $d-d$ electronic transitions.\\n"
         "D. Permanganate ion ($\\text{MnO}_4^-$) exhibits an intense purple colour due to ligand-to-metal charge transfer (LMCT), not $d-d$ transition.\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A, B, C and D",
          "A, B and C only",
          "C and D only",
          "A and B only"], 0,'''

chem = chem.replace(old_chem_ms3, new_chem_ms3)

with open("engine/neet_engine/curriculum_chemistry_mod.py", "w", encoding="utf-8") as f:
    f.write(chem)

print("Chemistry calibrated successfully!")

