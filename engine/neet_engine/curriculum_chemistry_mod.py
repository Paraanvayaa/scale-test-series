# -*- coding: utf-8 -*-
"""
Moderate Rigor Full Curriculum Chemistry Generator for NEET (UG) - Mocks 21 to 40
Calibrated to 2026 NEET-UG pattern:
- Direct MCQ: 29
- Statement I & II: 7
- Match List: 7
- Assertion & Reason: 4
- Multi-Statement: 3
Total: 50
"""
from neet_models import NeetQuestion

def get_chemistry_questions_mod(mock_num):
    questions = []

    topics_data = [
        # 1. Solutions - Dimerization
        ("Solutions", "van 't Hoff Factor with Association in Benzene", "Direct MCQ",
         "Benzoic acid ($\\text{C}_6\\text{H}_5\\text{COOH}$) dissolves in benzene and undergoes $80\\%$ dimerization ($2\\text{C}_6\\text{H}_5\\text{COOH} \\rightleftharpoons (\\text{C}_6\\text{H}_5\\text{COOH})_2$). The van 't Hoff factor $i$ of benzoic acid in this solution is:",
         ["0.60", "0.80", "1.60", "0.20"], 0,
         "1. Association equilibrium: $2A \\rightleftharpoons A_2$.\n2. For association into $n$ molecules ($n=2$ for dimer):\n   $$i = 1 - \\alpha\\left(1 - \\frac{1}{n}\\right) = 1 - \\alpha\\left(1 - \\frac{1}{2}\\right) = 1 - \\frac{\\alpha}{2}$$.\n3. Given degree of association $\\alpha = 0.80$ ($80\\%$):\n   $$i = 1 - \\frac{0.80}{2} = 1 - 0.40 = 0.60$$.\n4. Because molecules associate, $i < 1$.",
         "0.80 confuses degree of association with $i$; 1.60 calculates dissociation ($1+\\alpha$).",
         "For dimerization, the van 't Hoff factor is $i = 1 - \\alpha/2$. For $80\\%$ association, $i = 0.60$."),

        # 2. Solutions - Coordination Complexes Match List
        ("Solutions", "Coordination Complexes and Ionization in Aqueous Solution", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Werner Complex Formula) | List-II (Total Number of Ions Produced per Formula Unit) |\n"
         "| :--- | :--- |\n"
         "| **A.** $[\\text{Co}(\\text{NH}_3)_6]\\text{Cl}_3$ | **I.** 4 ions (van 't Hoff factor $i = 4$) |\n"
         "| **B.** $[\\text{Co}(\\text{NH}_3)_5\\text{Cl}]\\text{Cl}_2$ | **II.** 3 ions (van 't Hoff factor $i = 3$) |\n"
         "| **C.** $[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]\\text{Cl}$ | **III.** 2 ions (van 't Hoff factor $i = 2$) |\n"
         "| **D.** $[\\text{Co}(\\text{NH}_3)_3\\text{Cl}_3]$ | **IV.** 0 ions (non-electrolyte, $i = 1$) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-IV, B-III, C-II, D-I"], 0,
         "$[\\text{Co}(\\text{NH}_3)_6]\\text{Cl}_3$ dissociates into $[\\text{Co}(\\text{NH}_3)_6]^{3+} + 3\\text{Cl}^-$ (4 ions, A-I). $[\\text{Co}(\\text{NH}_3)_5\\text{Cl}]\\text{Cl}_2$ yields 3 ions (B-II). $[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]\\text{Cl}$ yields 2 ions (C-III). $[\\text{Co}(\\text{NH}_3)_3\\text{Cl}_3]$ does not ionize (D-IV).",
         "Distractors swap ion counts or count coordinated inner-sphere ligands as free ions.",
         "Werner complexes: only counter-ions outside the coordination sphere ionize in water."),

        # 3. Solutions - Negative Deviation Statement Pair
        ("Solutions", "Negative Deviation from Raoult's Law and Intermolecular H-Bonding", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** A liquid mixture of acetone and chloroform exhibits negative deviation from Raoult's law and forms a maximum boiling azeotrope.\n\n"
         "**Statement II:** Mixing acetone and chloroform leads to intermolecular hydrogen bonding between chloroform hydrogen and acetone carbonyl oxygen ($A-B$ attraction), which is stronger than the attractive interactions between like molecules ($A-A$ and $B-B$).\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Chloroform has an acidic hydrogen due to $-I$ effect of three chlorine atoms; acetone has basic carbonyl oxygen. H-bonding forms upon mixing: $\\text{Cl}_3\\text{C}-\\text{H}\\cdots\\text{O}=\\text{C}(\\text{CH}_3)_2$.\n2. Because $A-B$ forces are stronger than $A-A$ and $B-B$, vapour pressure decreases ($\\Delta P < 0, \\Delta H_{\\text{mix}} < 0, \\Delta V_{\\text{mix}} < 0$), forming a maximum boiling azeotrope. Both statements are correct.",
         "Positive deviation forms minimum boiling azeotrope; negative deviation forms maximum boiling azeotrope.",
         "Acetone + chloroform forms intermolecular H-bonds, yielding negative deviation from Raoult's law."),

        # 4. Electrochemistry - Nernst Concentration Cell
        ("Electrochemistry", "EMF of Concentration Cell and Nernst Equation", "Direct MCQ",
         "For the copper concentration cell $\\text{Cu}(s)|\\text{Cu}^{2+}(aq, 0.001\\text{ M})||\\text{Cu}^{2+}(aq, 0.1\\text{ M})|\\text{Cu}(s)$ at $298\\text{ K}$, the cell EMF $E_{\\text{cell}}$ is (take $\\frac{2.303 RT}{F} = 0.059\\text{ V}$):",
         ["0.059 V", "0.0295 V", "0.118 V", "0.000 V"], 0,
         "1. Standard potential of identical electrodes: $E^\\circ_{\\text{cell}} = 0\\text{ V}$.\n2. Cell reaction: $\\text{Cu}^{2+}_{\\text{cathode}}(0.1\\text{ M}) \\to \\text{Cu}^{2+}_{\\text{anode}}(0.001\\text{ M})$ with $n = 2$.\n3. Nernst equation:\n   $$E_{\\text{cell}} = E^\\circ - \\frac{0.059}{n}\\log\\frac{[\\text{Cu}^{2+}]_{\\text{anode}}}{[\\text{Cu}^{2+}]_{\\text{cathode}}} = 0 - \\frac{0.059}{2}\\log\\left(\\frac{10^{-3}}{10^{-1}}\\right) = -\\frac{0.059}{2}\\log(10^{-2})$$.\n4. $E_{\\text{cell}} = -\\frac{0.059}{2}(-2) = +0.059\\text{ V}$.",
         "0.0295 V forgets the factor of 2 from $\\log(10^{-2})$; 0.000 V is standard potential.",
         "Concentration cell EMF: $E_{\\text{cell}} = -\\frac{0.059}{n}\\log(c_1/c_2) = +0.059\\text{ V}$."),

        # 5. Electrochemistry - Lead Storage Battery Statement Pair
        ("Electrochemistry", "Reactions in Lead Storage Battery During Discharge", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** During the discharge of a lead storage battery, insoluble lead sulphate ($\\text{PbSO}_4$) is deposited on both the lead anode and the lead dioxide cathode.\n\n"
         "**Statement II:** During discharge, sulphuric acid ($\\text{H}_2\\text{SO}_4$) is consumed, causing the specific gravity and density of the battery electrolyte to decrease.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Overall discharge reaction: $\\text{Pb}(s) + \\text{PbO}_2(s) + 2\\text{H}_2\\text{SO}_4(aq) \\to 2\\text{PbSO}_4(s) + 2\\text{H}_2\\text{O}(l)$.\n2. Lead sulphate precipitates on both electrodes, and sulfuric acid is consumed as water is produced, dropping the density from $1.30\\text{ g/cm}^3$ to below $1.20\\text{ g/cm}^3$. Both statements are accurate.",
         "During recharging, the reverse reaction occurs: $\\text{PbSO}_4$ converts back to $\\text{Pb}$ and $\\text{PbO}_2$.",
         "Discharging a lead storage battery consumes $\\text{H}_2\\text{SO}_4$ and deposits $\\text{PbSO}_4$ on both electrodes."),

        # 6. Chemical Kinetics - Arrhenius Two Temperatures
        ("Chemical Kinetics", "Activation Energy from Rate Constants at Two Temperatures", "Direct MCQ",
         "The rate constant of a reaction triples when the temperature is raised from $300\\text{ K}$ to $310\\text{ K}$. The activation energy $E_a$ of the reaction is ($R = 8.314\\text{ J K}^{-1}\\text{ mol}^{-1}, \\log_{10} 3 = 0.477$):",
         ["84.3 kJ/mol", "42.1 kJ/mol", "28.1 kJ/mol", "126.5 kJ/mol"], 0,
         "1. Arrhenius two-temperature relation:\n   $$\\log_{10}\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{2.303 R}\\left(\\frac{T_2 - T_1}{T_1 T_2}\\right)$$.\n2. Given $\\frac{k_2}{k_1} = 3$, $T_1 = 300\\text{ K}$, $T_2 = 310\\text{ K}$:\n   $$0.477 = \\frac{E_a}{2.303 \\times 8.314}\\left(\\frac{10}{300 \\times 310}\\right) = \\frac{E_a}{19.147}\\left(\\frac{10}{93000}\\right)$$.\n3. $E_a = \\frac{0.477 \\times 19.147 \\times 93000}{10} = 84938\\text{ J/mol} \\approx 84.3\\text{ kJ/mol}$.",
         "42.1 kJ/mol divides by 2; 28.1 kJ/mol divides by 3.",
         "Arrhenius equation: $\\log(k_2/k_1) = \\frac{E_a}{2.303 R}\\frac{\\Delta T}{T_1 T_2}$."),

        # 7. Chemical Kinetics - Pseudo First Order
        ("Chemical Kinetics", "Pseudo-First Order Acid-Catalyzed Ester Hydrolysis", "Direct MCQ",
         "The acid-catalysed hydrolysis of ethyl acetate: $\\text{CH}_3\\text{COOC}_2\\text{H}_5 + \\text{H}_2\\text{O} \\xrightarrow{\\text{H}^+} \\text{CH}_3\\text{COOH} + \\text{C}_2\\text{H}_5\\text{OH}$ is classified as a pseudo-first-order reaction because:",
         ["Water is present in large stoichiometric excess, so its concentration remains essentially constant during the reaction",
          "The reaction is elementary and unimolecular",
          "Ethyl acetate acts as a catalyst",
          "Activation energy of the forward reaction is zero"], 0,
         "1. The true rate law is second-order overall: $\\text{Rate} = k' [\\text{CH}_3\\text{COOC}_2\\text{H}_5][\\text{H}_2\\text{O}]$.\n2. Because water is the solvent present in large excess ($[\\text{H}_2\\text{O}] \\approx 55.5\\text{ M}$), its concentration does not change noticeably.\n3. Therefore, $k' [\\text{H}_2\\text{O}]$ merges into an effective pseudo-first-order rate constant $k = k' [\\text{H}_2\\text{O}]$.\n4. Rate $= k [\\text{CH}_3\\text{COOC}_2\\text{H}_5]$, mimicking first-order kinetics.",
         "Distractors call the reaction unimolecular or claim zero activation energy.",
         "Ester hydrolysis is pseudo-first-order because solvent water is in large excess: Rate $= k[\\text{ester}]$."),

        # 8. Equilibrium - Common Ion Effect on Ksp
        ("Equilibrium", "Common Ion Effect on Sparingly Soluble Salt", "Direct MCQ",
         "The solubility product constant of silver chloride ($\\text{AgCl}$) in water is $K_{sp} = 1.6 \\times 10^{-10}$ at $298\\text{ K}$. Its molar solubility in $0.1\\text{ M }\\text{NaCl}$ aqueous solution is:",
         ["1.6 x 10^-9 M", "1.26 x 10^-5 M", "1.6 x 10^-10 M", "3.2 x 10^-9 M"], 0,
         "1. $\\text{NaCl}$ is a strong electrolyte dissociating completely: $[\\text{Cl}^-] = 0.1\\text{ M}$.\n2. Dissociation of $\\text{AgCl}$: $\\text{AgCl}(s) \\rightleftharpoons \\text{Ag}^+(aq) + \\text{Cl}^-(aq)$.\n3. Let solubility be $S$. Then $[\\text{Ag}^+] = S$, and total $[\\text{Cl}^-] = 0.1 + S \\approx 0.1\\text{ M}$ (since $S \\ll 0.1$).\n4. $K_{sp} = [\\text{Ag}^+][\\text{Cl}^-] = S \\times 0.1 = 1.6 \\times 10^{-10}$.\n5. $S = \\frac{1.6 \\times 10^{-10}}{0.1} = 1.6 \\times 10^{-9}\\text{ M}$.\n6. Notice that common ion $\\text{Cl}^-$ suppresses solubility from $1.26 \\times 10^{-5}\\text{ M}$ in pure water down to $1.6 \\times 10^{-9}\\text{ M}$.",
         "1.26 x 10^-5 M is solubility in pure water without common ion effect.",
         "Common ion presence suppresses solubility of sparingly soluble salt: $S = K_{sp}/[\\text{common ion}]$."),

        # 9. Equilibrium - Salt Hydrolysis pH
        ("Equilibrium", "pH of Salt of Weak Acid and Weak Base", "Direct MCQ",
         "For ammonium acetate ($\\text{CH}_3\\text{COONH}_4$), the dissociation constants of acetic acid and ammonium hydroxide are equal: $pK_a = pK_b = 4.76$ at $298\\text{ K}$. The $pH$ of a $0.05\\text{ M}$ aqueous solution of ammonium acetate is:",
         ["7.00 (neutral and independent of salt concentration)",
          "4.76",
          "9.24",
          "8.88"], 0,
         "1. Ammonium acetate is a salt derived from weak acid ($\\text{CH}_3\\text{COOH}$) and weak base ($\\text{NH}_4\\text{OH}$).\n2. Hydrolysis formula for weak acid-weak base salt:\n   $$pH = 7 + \\frac{1}{2}pK_a - \\frac{1}{2}pK_b$$.\n3. Since $pK_a = pK_b = 4.76$:\n   $$pH = 7 + \\frac{1}{2}(4.76) - \\frac{1}{2}(4.76) = 7.00$$.\n4. Crucially, the $pH$ of a weak acid-weak base salt is completely independent of the concentration of the salt solution.",
         "Distractors depend on salt concentration or equate $pH$ to $pK_a$.",
         "For weak acid + weak base salts, $pH = 7 + \\frac{1}{2}(pK_a - pK_b)$, independent of concentration."),

        # 10. Structure of Atom - Nodes
        ("Structure of Atom", "Radial and Angular Nodes of 4d Orbitals", "Direct MCQ",
         "For a $4d$ orbital ($n = 4, l = 2$), the number of radial nodes, angular nodes, and total nodes are respectively:",
         ["1 radial node, 2 angular nodes, 3 total nodes",
          "2 radial nodes, 1 angular node, 3 total nodes",
          "0 radial nodes, 2 angular nodes, 2 total nodes",
          "1 radial node, 1 angular node, 2 total nodes"], 0,
         "1. Radial nodes formula: $N_{\\text{radial}} = n - l - 1$.\n2. For $4d$ orbital, principal quantum number $n = 4$, azimuthal quantum number $l = 2$.\n3. Radial nodes: $4 - 2 - 1 = 1$.\n4. Angular nodes formula: $N_{\\text{angular}} = l = 2$.\n5. Total nodes: $N_{\\text{total}} = N_{\\text{radial}} + N_{\\text{angular}} = (n - l - 1) + l = n - 1 = 4 - 1 = 3$.",
         "Distractors swap radial and angular counts or forget the $-1$ offset.",
         "Radial nodes $= n - l - 1$; Angular nodes $= l$; Total nodes $= n - 1$. For $4d$, nodes are $1, 2, 3$."),

        # 11. Chemical Bonding - Back Bonding Assertion-Reason
        ("Chemical Bonding and Molecular Structure", "Lewis Acid Strength of Boron Trihalides", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** The Lewis acid strength of boron trihalides follows the unexpected order: $\\text{BF}_3 < \\text{BCl}_3 < \\text{BBr}_3 < \\text{BI}_3$, despite fluorine being the most electronegative halogen.\n\n"
         "**Reason (R):** Strong $p\\pi-p\\pi$ back-bonding occurs between the filled $2p$ orbital of fluorine and the vacant $2p$ orbital of boron due to effective size and energy match, which significantly reduces electron deficiency at the boron atom in $\\text{BF}_3$.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "Based purely on electronegativity, BF3 would be expected to be the strongest Lewis acid. However, effective 2p-2p orbital overlap allows strong back-donation from F to B in BF3, satisfying boron's electron deficiency. In BCl3 (2p-3p) and BBr3 (2p-4p), orbital mismatch weakens back-bonding, making BI3 the strongest Lewis acid. Reason directly explains Assertion.",
         "Electronegativity predicts the opposite order; back-bonding explains the real trend.",
         "Lewis acidity of boron halides is governed by $p\\pi-p\\pi$ back bonding: $\\text{BF}_3 < \\text{BCl}_3 < \\text{BBr}_3 < \\text{BI}_3$."),

        # 12. Coordination - Optical Isomerism
        ("Coordination Compounds", "Optical Activity in Octahedral Complexes", "Direct MCQ",
         "Which of the following coordination complexes is chiral and exhibits optical activity (existence of non-superimposable d- and l-enantiomers)?",
         ["$cis-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$",
          "$trans-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$",
          "$[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]^+$",
          "$[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$"], 0,
         "1. In $trans-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$, there is a plane of symmetry ($\\sigma$) and centre of inversion ($i$); it is superimposable on its mirror image and optically inactive.\n2. In $cis-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$, the two bidentate ethylenediamine (en) rings lie perpendicular to each other, lacking any plane or centre of symmetry.\n3. The cis isomer is non-superimposable on its mirror image, resolving into dextro ($d$) and laevo ($l$) enantiomers.",
         "trans isomer has a centre of symmetry making it achiral; square planar platinum is achiral.",
         "$cis-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$ lacks symmetry planes and is optically active; trans isomer is achiral."),

        # 13. Coordination - CFSE Calculation
        ("Coordination Compounds", "Crystal Field Stabilization Energy (CFSE) of d6 Complex", "Direct MCQ",
         "The crystal field stabilization energy (CFSE) for a high-spin octahedral complex of a $d^6$ metal ion (such as $[\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+}$) is:",
         ["-0.4 Δ_o", "-2.4 Δ_o + 2P", "-0.8 Δ_o", "-1.2 Δ_o"], 0,
         "1. High-spin $d^6$ complex with weak field ligand ($\\Delta_o < P$): pairing does not occur initially.\n2. Electronic configuration: $t_{2g}^4 e_g^2$.\n3. CFSE formula: $\\text{CFSE} = (-0.4 n_{t_{2g}} + 0.6 n_{e_g}) \\Delta_o$.\n4. Calculation: $\\text{CFSE} = (-0.4 \\times 4 + 0.6 \\times 2)\\Delta_o = (-1.6 + 1.2)\\Delta_o = -0.4\\Delta_o$.\n5. (For low spin $t_{2g}^6 e_g^0$, CFSE would be $-2.4\\Delta_o + 2P$).",
         "-2.4 Δ_o + 2P applies to low-spin configuration ($t_{2g}^6$); -0.8 Δ_o applies to $d^7$.",
         "High-spin $d^6$ ($t_{2g}^4 e_g^2$) has $\\text{CFSE} = -0.4\\Delta_o$."),

        # 14. Coordination - Synergic Bonding
        ("Coordination Compounds", "Synergic Bonding in Metal Carbonyls", "Direct MCQ",
         "In metal carbonyls such as $[\\text{Ni}(\\text{CO})_4]$ and $[\\text{Fe}(\\text{CO})_5]$, the metal-carbon bond possesses both $\\sigma$ and $\\pi$ character. The $\\pi$-bond is formed by the:",
         ["Donation of a pair of electrons from a filled metal d-orbital into the vacant antibonding π* orbital of carbon monoxide",
          "Donation of lone pair from carbon into vacant metal d-orbital",
          "Overlap of metal s-orbital with carbon p-orbital",
          "Back-donation from metal into bonding $\\sigma$ orbital of oxygen"], 0,
         "1. $\\text{M}-\\text{C}$ $\\sigma$-bond forms by donation of lone pair on carbonyl carbon into vacant hybrid orbital of metal.\n2. $\\text{M}-\\text{C}$ $\\pi$-bond forms by back-donation of electron density from filled $d$-orbitals of transition metal into vacant antibonding $\\pi^*$ molecular orbitals of $\\text{CO}$.\n3. This synergic interaction strengthens the $\\text{M}-\\text{C}$ bond while simultaneously weakening the $\\text{C}-\\text{O}$ bond (lengthening $\\text{C}-\\text{O}$ and lowering stretching frequency).",
         "Option (2) describes the $\\sigma$-bond, not the $\\pi$-backbond.",
         "Synergic bonding involves metal $d \\to \\pi^*(\\text{CO})$ back-donation, strengthening $\\text{M}-\\text{C}$ and weakening $\\text{C}-\\text{O}$."),

        # 15. d-Block - Manganate Statement Pair
        ("The d- and f-Block Elements", "Disproportionation of Manganate(VI) in Acidic Medium", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** In acidic or neutral aqueous solution, dark green manganate ions ($\\text{MnO}_4^{2-}$) are thermodynamically unstable and disproportionate into purple permanganate ($\\text{MnO}_4^-$) and brown manganese dioxide ($\\text{MnO}_2$).\n\n"
         "**Statement II:** In strongly alkaline solutions, manganate ion ($\\text{MnO}_4^{2-}$) is stable and does not undergo disproportionation.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. In acid: $3\\text{MnO}_4^{2-} + 4\\text{H}^+ \\to 2\\text{MnO}_4^- + \\text{MnO}_2(s) + 2\\text{H}_2\\text{O}$. Manganese(+6) simultaneously oxidizes to +7 and reduces to +4.\n2. In high alkaline pH, the equilibrium shifts strongly to the left, stabilizing green manganate(VI). Both statements are accurate.",
         "Permanganate is purple (+7), manganate is green (+6), and manganese dioxide is brown (+4).",
         "Manganate(VI) disproportionates in acid: $3\\text{MnO}_4^{2-} + 4\\text{H}^+ \\to 2\\text{MnO}_4^- + \\text{MnO}_2 + 2\\text{H}_2\\text{O}$."),

        # 16. p-Block - XeF4 Hydrolysis Assertion-Reason
        ("p-Block Elements", "Disproportionation Hydrolysis of Xenon Tetrafluoride", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** The complete hydrolysis of xenon tetrafluoride ($\\text{XeF}_4$) at room temperature is a redox disproportionation reaction yielding both elemental xenon ($\\text{Xe}$) and xenon trioxide ($\\text{XeO}_3$).\n\n"
         "**Reason (R):** In $\\text{XeF}_4$, xenon is in the $+4$ oxidation state, which is thermodynamically unstable towards self-oxidation to $+6$ (in $\\text{XeO}_3$) and reduction to $0$ (in $\\text{Xe}$).\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "Reaction: $6\\text{XeF}_4 + 12\\text{H}_2\\text{O} \\to 4\\text{Xe} + 2\\text{XeO}_3 + 24\\text{HF} + 3\\text{O}_2$. Xenon(+4) is both reduced to Xe(0) and oxidized to Xe(+6). By contrast, XeF6 hydrolyzes non-redox to XeO3 and HF. Both statements are true and Reason directly explains Assertion.",
         "XeF6 hydrolysis is NOT redox, but XeF4 hydrolysis IS redox disproportionation.",
         "Hydrolysis of $\\text{XeF}_4$ yields $\\text{Xe} + \\text{XeO}_3 + \\text{HF} + \\text{O}_2$ via disproportionation."),

        # 17. Organic Principles - Ortho Effect Assertion-Reason
        ("Organic Chemistry - Some Basic Principles", "Ortho Effect on Acid Strength of Benzoic Acids", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** 2-Methylbenzoic acid (o-toluic acid) is a stronger acid than benzoic acid, despite the methyl group having an electron-donating ($+I$ and hyperconjugative) effect.\n\n"
         "**Reason (R):** Due to steric hindrance (ortho-effect), the bulky ortho substituent twists the carboxyl group out of the benzene ring plane, inhibiting resonance with the ring and facilitating resonance stabilization of the carboxylate anion.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "Steric inhibition of resonance (ortho effect) causes the -COOH group to twist out of coplanarity with the phenyl ring. As a result, the benzene ring cannot donate electrons into the carboxylate by resonance, allowing the negative charge to be stabilized exclusively by the two oxygen atoms. Both statements are true and Reason directly explains Assertion.",
         "Normal $+I$ effect weakens acidity, but ortho steric effect overrides it.",
         "Ortho-substituted benzoic acids are stronger acids than benzoic acid due to steric inhibition of resonance (ortho-effect)."),

        # 18. Organic Principles - Aromaticity Multi-Statement
        ("Organic Chemistry - Some Basic Principles", "Hückel's Rule of Aromaticity in Cyclic Systems", "Multi-Statement",
         "Which of the following chemical species are AROMATIC according to Hückel's $(4n+2)\\pi$ electron rule?\n\n"
         "A. Benzene ($\\text{C}_6\\text{H}_6$, $6\\pi$ electrons, planar cyclic conjugated ring)\n"
         "B. Tropylium cation ($\\text{C}_7\\text{H}_7^+$, $6\\pi$ electrons, planar cycloheptatrienyl cation)\n"
         "C. Cyclopentadienyl anion ($\\text{C}_5\\text{H}_5^-$, $6\\pi$ electrons, planar ring)\n"
         "D. Cyclooctatetraene (COT, $\\text{C}_8\\text{H}_8$, adopting a non-planar tub conformation)\n"
         "E. Pyridine (heterocyclic $6\\pi$ aromatic ring)\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, C and E only",
          "A, B and C only",
          "B, C, D and E only",
          "A, C and D only"], 0,
         "Benzene, Tropylium cation, Cyclopentadienyl anion, and Pyridine are all planar conjugated systems containing $(4n+2) = 6\\pi$ electrons ($n=1$), satisfying Hückel's rule. Cyclooctatetraene ($8\\pi$ electrons) is non-planar (tub-shaped) to avoid anti-aromaticity, making it non-aromatic.",
         "COT adopts non-planar tub conformation to avoid being anti-aromatic.",
         "Hückel rule requires planarity, complete conjugation, and $(4n+2)\\pi$ electrons."),

        # 19. Hydrocarbons - Birch Reduction
        ("Hydrocarbons", "Stereoselective Birch Reduction of Non-Terminal Alkynes", "Direct MCQ",
         "The reduction of but-2-yne ($\\text{CH}_3-\\text{C}\\equiv\\text{C}-\\text{CH}_3$) with sodium in liquid ammonia (Birch reduction) yields:",
         ["trans-But-2-ene selectively via radical-anion intermediate",
          "cis-But-2-ene selectively",
          "Butane",
          "1-Bromobutane"], 0,
         "1. Reduction of non-terminal internal alkynes with $\\text{Na} / \\text{liquid }\\text{NH}_3$ proceeds via radical anion intermediate where bulky methyl groups adopt anti-periplanar orientation to minimize steric repulsion.\n2. This stereoselectively produces the trans-alkene (trans-but-2-ene).\n3. By contrast, catalytic hydrogenation with Lindlar's catalyst ($\text{H}_2 / \text{Pd}-\text{CaCO}_3$) poisoned with quinoline) gives the cis-alkene (cis-but-2-ene).",
         "Lindlar's catalyst gives cis-alkene; Birch reduction gives trans-alkene.",
         "$\\text{Na} / \\text{liquid }\\text{NH}_3$ reduces internal alkynes stereoselectively to trans-alkenes."),

        # 20. Haloalkanes - SN1 Stereochemistry Statement Pair
        ("Haloalkanes and Haloarenes", "Stereochemical Fate of Chiral Substrates in SN1", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** An $S_N1$ reaction of an optically active haloalkane at an asymmetric chiral carbon always results in partial racemization accompanied by net excess of inversion of configuration.\n\n"
         "**Statement II:** The departing halide leaving group momentarily blocks the front side of the carbocation as an intimate ion-pair, forcing the incoming nucleophile to attack more frequently from the opposite (rear) side.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Pure planar carbocation would lead to 50:50 racemization only in idealized isolated gas phase.\n2. In solution, the departing halide ion forms a front-side intimate ion pair (shielding effect), hindering front attack.\n3. Backside attack occurs with higher probability, yielding ~70% inversion and ~30% retention (partial racemization with excess inversion). Both statements are accurate.",
         "SN2 gives 100% inversion; SN1 in practice yields partial racemization with net inversion.",
         "$S_N1$ on chiral secondary halides yields partial racemization with net excess of inversion due to ion pairing."),

        # 21. Alcohols - Phenol Acidity Statement Pair
        ("Alcohols, Phenols and Ethers", "Acidic Strength Comparison of Substituted Phenols", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** 2,4,6-Trinitrophenol (picric acid) is a much stronger acid than phenol and even stronger than acetic acid ($pK_a = 0.38$).\n\n"
         "**Statement II:** The presence of three strongly electron-withdrawing nitro groups ($-\\text{NO}_2$) at ortho and para positions powerfully stabilizes the conjugate phenoxide anion via strong $-M$ and $-I$ resonance delocalization.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Picric acid contains three -NO2 groups at ortho and para positions (2, 4, 6).\n2. Both -I and -M effects disperse the negative charge across all three oxygens of the nitro groups.\n3. Its pKa of 0.38 makes it strongly acidic, reacting with aqueous sodium bicarbonate to effervesce CO2. Both statements are accurate.",
         "Phenol does not react with sodium bicarbonate; picric acid dissolves with vigorous CO2 effervescence.",
         "Picric acid is exceptionally acidic ($pK_a = 0.38$) due to three $-M, -I$ ortho/para nitro groups."),

        # 22. Aldehydes - Functional Tests Match List
        ("Aldehydes, Ketones and Carboxylic Acids", "Organic Functional Group Diagnostic Reagents", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Diagnostic Chemical Test) | List-II (Specific Functional Group Detected) |\n"
         "| :--- | :--- |\n"
         "| **A.** Lucas test (anhydrous $\\text{ZnCl}_2 + \\text{conc. HCl}$) | **I.** Distinction among $1^\\circ, 2^\\circ,$ and $3^\\circ$ alcohols |\n"
         "| **B.** Iodoform test ($\\text{I}_2 + \\text{NaOH}$) | **II.** Methyl ketones ($\\text{CH}_3\\text{CO}-$) and $\\text{CH}_3\\text{CH(OH)}-$ groups |\n"
         "| **C.** Tollens' test (Ammoniacal $\\text{AgNO}_3$) | **III.** Aldehydes (produces silver mirror) |\n"
         "| **D.** Carbylamine test ($\\text{CHCl}_3 + \\text{alc. KOH}$) | **IV.** Primary amines ($1^\\circ$ aliphatic and aromatic) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-II, C-I, D-IV"], 0,
         "Lucas test distinguishes alcohols: $3^\\circ$ turbid immediately, $2^\\circ$ in 5 min, $1^\\circ$ on heating (A-I). Iodoform gives yellow $\\text{CHI}_3$ precipitate for methyl ketones (B-II). Tollens' gives silver mirror with aldehydes (C-III). Carbylamine gives foul-smelling isocyanide with $1^\\circ$ amines (D-IV).",
         "Lucas test fails for primary alcohols at room temperature.",
         "Functional tests: Lucas ($1^\circ / 2^\circ / 3^\circ$ alcohols), Iodoform (methyl ketones), Tollens' (aldehydes), Carbylamine ($1^\circ$ amines)."),

        # 23. Amines - Hoffmann Bromamide
        ("Amines", "Hoffmann Bromamide Degradation Mechanism and Migration", "Direct MCQ",
         "In the Hoffmann bromamide degradation reaction: $\\text{R}-\\text{CONH}_2 + \\text{Br}_2 + 4\\text{NaOH} \\to \\text{R}-\\text{NH}_2 + \\text{Na}_2\\text{CO}_3 + 2\\text{NaBr} + 2\\text{H}_2\\text{O}$, the alkyl or aryl group $R$ migrates from carbonyl carbon to nitrogen atom with:",
         ["Complete retention of stereochemical configuration",
          "Complete inversion of configuration",
          "Racemization yielding 50:50 enantiomers",
          "Carbocation rearrangement to a more stable skeletal isomer"], 0,
         "1. Intermediate in Hoffmann degradation is an acyl nitrene / isocyanate ($\\text{R}-\\text{N}=\\text{C}=\\text{O}$).\n2. The migration of group $\\text{R}$ from carbonyl carbon to the electron-deficient nitrogen is an intramolecular 1,2-shift.\n3. Because it is concerted and intramolecular without ever detaching as a free ion, the migrating group retains its spatial configuration completely (retention of configuration).",
         "Distractors invoke carbocation rearrangement or inversion.",
         "In Hoffmann bromamide degradation, alkyl migration to nitrogen proceeds with complete retention of configuration."),

        # 24. Biomolecules - Mutarotation
        ("Biomolecules", "Mutarotation of D-Glucose", "Direct MCQ",
         "The spontaneous change in the specific optical rotation of freshly prepared $\\alpha$-D-glucopyranose ($+112^\\circ$) or $\\beta$-D-glucopyranose ($+19^\\circ$) in aqueous solution until an equilibrium value of $+52.7^\\circ$ is reached is known as:",
         ["Mutarotation, caused by dynamic equilibrium between cyclic anomers through the open-chain aldehyde form",
          "Inversion of cane sugar",
          "Enantiomerization",
          "Denaturation"], 0,
         "1. $\\alpha$-D-glucose and $\\beta$-D-glucose are cyclic hemiacetal anomers differing only at the C-1 anomeric carbon.\n2. In aqueous solution, the pyranose ring opens reversibly into the trace open-chain aldehyde form ($< 0.1\\%$) and recloses into either $\\alpha$ or $\\beta$ form.\n3. This interconversion establishes an equilibrium mixture ($36\\%\\ \\alpha$ and $64\\%\\ \\beta$) with net specific rotation $+52.7^\\circ$.\n4. This phenomenon is termed mutarotation.",
         "Inversion applies to sucrose hydrolysis; denaturation applies to proteins.",
         "Mutarotation is the spontaneous optical rotation change of anomers equilibrating via the open-chain form."),

        # 25. Practical Chemistry - Group Cations Match List
        ("Practical Chemistry", "Qualitative Cation Analysis Group Reagents", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Analytical Cation Group) | List-II (Specific Group Precipitation Reagent) |\n"
         "| :--- | :--- |\n"
         "| **A.** Group I ($\\text{Pb}^{2+}, \\text{Ag}^+$) | **I.** Dilute $\\text{HCl}$ (precipitated as chlorides) |\n"
         "| **B.** Group II ($\\text{Cu}^{2+}, \\text{Pb}^{2+}, \\text{Cd}^{2+}$) | **II.** $\\text{H}_2\\text{S}$ gas in presence of dilute $\\text{HCl}$ |\n"
         "| **C.** Group III ($\\text{Fe}^{3+}, \\text{Al}^{3+}, \\text{Cr}^{3+}$) | **III.** $\\text{NH}_4\\text{OH}$ in presence of excess $\\text{NH}_4\\text{Cl}$ |\n"
         "| **D.** Group IV ($\\text{Zn}^{2+}, \\text{Ni}^{2+}, \\text{Mn}^{2+}$) | **IV.** $\\text{H}_2\\text{S}$ gas in presence of $\\text{NH}_4\\text{OH}$ and $\\text{NH}_4\\text{Cl}$ |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-III, C-II, D-IV",
          "A-IV, B-II, C-III, D-I"], 0,
         "Group I: dilute HCl forms insoluble chlorides (A-I). Group II: H2S in acidic medium selectively precipitates low-Ksp sulphides (B-II). Group III: NH4OH with NH4Cl precipitates hydroxides (C-III). Group IV: H2S in basic medium precipitates higher-Ksp sulphides (D-IV).",
         "In Group II, acidic medium keeps sulphide ion concentration low via common ion effect.",
         "Inorganic group separation relies on selective control of ion products exceeding $K_{sp}$."),

        # 26. Solutions - Relative Lowering
        ("Solutions", "Relative Lowering of Vapour Pressure", "Direct MCQ",
         "The vapour pressure of pure water at $298\\text{ K}$ is $23.8\\text{ mm Hg}$. When $18\\text{ g}$ of glucose is dissolved in $178.2\\text{ g}$ of water, the relative lowering of vapour pressure is:",
         ["0.010", "0.018", "0.005", "0.025"], 0,
         "1. Moles of glucose: $n_1 = 18/180 = 0.1\\text{ mol}$.\n2. Moles of water: $n_2 = 178.2/18 = 9.9\\text{ mol}$.\n3. Total moles: $n_1 + n_2 = 0.1 + 9.9 = 10.0\\text{ mol}$.\n4. Relative lowering of vapour pressure equals mole fraction of solute:\n   $$\\frac{P^\\circ - P}{P^\\circ} = x_{\\text{solute}} = \\frac{0.1}{10.0} = 0.010$$.",
         "0.018 uses mass ratio; 0.005 divides by 20.",
         "Relative lowering of vapour pressure: $\\frac{\\Delta P}{P^\\circ} = x_{\\text{solute}} = 0.010$."),

        # 27. Electrochemistry - Gibbs Energy
        ("Electrochemistry", "Standard Gibbs Energy and Equilibrium Constant", "Direct MCQ",
         "For the cell reaction $2\\text{Fe}^{3+}(aq) + 2\\text{I}^-(aq) \\to 2\\text{Fe}^{2+}(aq) + \\text{I}_2(s)$, the standard cell potential is $E^\\circ_{\\text{cell}} = 0.236\\text{ V}$ at $298\\text{ K}$. The standard Gibbs energy change $\\Delta G^\\circ$ is ($F = 96500\\text{ C/mol}$):",
         ["-45.54 kJ/mol", "-22.77 kJ/mol", "-91.08 kJ/mol", "+45.54 kJ/mol"], 0,
         "1. Number of electrons transferred in balanced equation: $n = 2$.\n2. Formula: $\\Delta G^\\circ = -n F E^\\circ_{\\text{cell}}$.\n3. Calculation:\n   $$\\Delta G^\\circ = -(2) \\times (96500) \\times (0.236) = -45548\\text{ J/mol} \\approx -45.54\\text{ kJ/mol}$$.",
         "-22.77 kJ/mol uses $n=1$; +45.54 kJ/mol has incorrect sign for spontaneous reaction.",
         "Standard Gibbs energy: $\\Delta G^\\circ = -nFE^\\circ = -45.54\\text{ kJ/mol}$."),

        # 28. Kinetics - Graphical
        ("Chemical Kinetics", "First Order Reaction Graphical Representation", "Direct MCQ",
         "For a first-order reaction $A \\to \\text{Products}$, which of the following graphical plots is a straight line passing through the origin?",
         ["Rate versus $[A]$", "$\\ln[A]$ versus time $t$", "$t_{1/2}$ versus initial concentration $[A]_0$", "$[A]$ versus time $t$"], 0,
         "1. Rate law for first order: $\\text{Rate} = k [A]^1$.\n2. This is a direct proportionality of the form $y = mx$ with zero intercept ($c = 0$).\n3. Hence a plot of Rate versus $[A]$ is a straight line passing directly through the origin with slope equal to rate constant $k$.\n4. $\\ln[A]$ vs $t$ has a negative slope with y-intercept $\\ln[A]_0$.",
         "$\\ln[A]$ vs $t$ does not pass through origin; $t_{1/2}$ is horizontal constant line.",
         "Plot of reaction Rate versus reactant concentration $[A]$ is a straight line through the origin for first-order kinetics."),

        # 29. Thermodynamics - Hess's Law
        ("Thermodynamics", "Hess's Law Application to Enthalpy of Formation", "Direct MCQ",
         "Given the enthalpies of combustion: $\\text{C}(s) + \\text{O}_2(g) \\to \\text{CO}_2(g)$ ($\\Delta H = -393.5\\text{ kJ}$), $\\text{H}_2(g) + \\frac{1}{2}\\text{O}_2(g) \\to \\text{H}_2\\text{O}(l)$ ($\\Delta H = -285.8\\text{ kJ}$), and $\\text{CH}_4(g) + 2\\text{O}_2(g) \\to \\text{CO}_2(g) + 2\\text{H}_2\\text{O}(l)$ ($\\Delta H = -890.3\\text{ kJ}$). The standard enthalpy of formation of methane ($\\text{CH}_4$) is:",
         ["-74.8 kJ/mol", "-128.2 kJ/mol", "+74.8 kJ/mol", "-211.0 kJ/mol"], 0,
         "1. Target reaction: $\\text{C}(s) + 2\\text{H}_2(g) \\to \\text{CH}_4(g)$.\n2. Using Hess's law:\n   $$\\Delta_f H^\\circ = \\Delta_c H(\\text{C}) + 2\\Delta_c H(\\text{H}_2) - \\Delta_c H(\\text{CH}_4)$$.\n3. Calculation:\n   $$\\Delta_f H^\\circ = (-393.5) + 2(-285.8) - (-890.3) = -393.5 - 571.6 + 890.3 = -965.1 + 890.3 = -74.8\\text{ kJ/mol}$$.",
         "+74.8 kJ/mol inverts signs; -128.2 kJ/mol forgets to multiply hydrogen by 2.",
         "Standard enthalpy of formation from combustion enthalpies: $\\Delta_f H = \\sum \\Delta_c H(\\text{reactants}) - \\sum \\Delta_c H(\\text{products})$."),

        # 30. Equilibrium - Vapour Density
        ("Equilibrium", "Degree of Dissociation and Vapour Density", "Direct MCQ",
         "The vapour density of phosphorus pentachloride ($\\text{PCl}_5$, molar mass $208.5\\text{ g/mol}$) dissociating according to $\\text{PCl}_5(g) \\rightleftharpoons \\text{PCl}_3(g) + \\text{Cl}_2(g)$ is found to be $70$ at a certain temperature. The degree of dissociation $\\alpha$ is:",
         ["0.49 (49%)", "0.33 (33%)", "0.67 (67%)", "0.25 (25%)"], 0,
         "1. Theoretical vapour density: $D = M/2 = 208.5 / 2 = 104.25$.\n2. Observed vapour density: $d = 70$.\n3. Formula for dissociation $A \\rightleftharpoons B + C$ ($n=2$):\n   $$\\alpha = \\frac{D - d}{d (n - 1)} = \\frac{104.25 - 70}{70(2 - 1)} = \\frac{34.25}{70} \\approx 0.489 \\approx 0.49\\text{ (or } 49\\%\\text{)}$$.",
         "0.33 uses $D$ in denominator; 0.67 is $1-\\alpha$.",
         "Degree of dissociation from vapour density: $\\alpha = \\frac{D - d}{(n - 1)d}$."),

        # 31. Chemical Bonding - Interhalogen Match List
        ("Chemical Bonding and Molecular Structure", "Hybridisation of Interhalogen Compounds", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Interhalogen / Xenon Compound) | List-II (Hybridisation and Molecular Geometry) |\n"
         "| :--- | :--- |\n"
         "| **A.** $\\text{IF}_7$ | **I.** $sp^3d^3$ / Pentagonal bipyramidal |\n"
         "| **B.** $\\text{BrF}_3$ | **II.** $sp^3d$ / T-shaped |\n"
         "| **C.** $\\text{XeF}_6$ | **III.** $sp^3d^3$ / Distorted octahedral (7 electron pairs) |\n"
         "| **D.** $\\text{XeO}_3$ | **IV.** $sp^3$ / Pyramidal (3 bond pairs + 1 lone pair) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. $\\text{IF}_7$: 7 bond pairs, $sp^3d^3$, pentagonal bipyramidal $\\to$ I.\n2. $\\text{BrF}_3$: 3 bond pairs + 2 lone pairs, $sp^3d$, T-shaped $\\to$ II.\n3. $\\text{XeF}_6$: 6 bond pairs + 1 lone pair, $sp^3d^3$, distorted octahedral $\\to$ III.\n4. $\\text{XeO}_3$: 3 bond pairs + 1 lone pair, $sp^3$, pyramidal $\\to$ IV.",
         "Distractors confuse distorted octahedral $\\text{XeF}_6$ with regular octahedral.",
         "$\\text{IF}_7$ is pentagonal bipyramidal ($sp^3d^3$); $\\text{XeF}_6$ has 1 lone pair ($sp^3d^3$, distorted octahedral)."),

        # 32. d-Block - Lanthanoid vs Actinoid Statement Pair
        ("The d- and f-Block Elements", "Lanthanoid vs Actinoid Oxidation States", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Actinoids exhibit a greater range of oxidation states (up to $+7$) compared to lanthanoids whose predominant oxidation state is $+3$.\n\n"
         "**Statement II:** The $5f, 6d,$ and $7s$ energy levels in actinoids are comparable in energy, allowing electrons from all three subshells to participate in bonding, whereas $4f$ electrons in lanthanoids are buried deep inside.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Lanthanoids exhibit mainly $+3$ (with occasional $+2$ or $+4$ for empty, half-filled, or full $4f$ subshells) because $4f$ orbitals are deeply buried.\n2. Actinoids show wider oxidation states ($+3, +4, +5, +6, +7$ in Np, Pu) because energy gap between $5f, 6d,$ and $7s$ is very small.\n3. Both statements are accurate and Statement II explains Statement I.",
         "Distractors falsely claim lanthanoids show higher oxidation states.",
         "Actinoids show greater range of oxidation states because $5f, 6d,$ and $7s$ levels are close in energy."),

        # 33. d-Block - Coloured Ions Multi-Statement
        ("The d- and f-Block Elements", "Electronic Transitions and Coloured Ions in d-Block", "Multi-Statement",
         "Which of the following statements regarding the colour and electronic properties of transition metal ions are correct?\n\n"
         "A. $\\text{Sc}^{3+}$ ($3d^0$) is colourless in aqueous solution because it possesses no $d$-electrons to undergo $d-d$ transitions.\n"
         "B. $\\text{Zn}^{2+}$ ($3d^{10}$) is colourless in aqueous solution because its $d$-subshell is completely filled, leaving no vacant orbital for excitation.\n"
         "C. $\\text{Cu}^{2+}$ ($3d^9$) ions impart a characteristic blue colour to aqueous solutions due to visible $d-d$ electronic transitions.\n"
         "D. Permanganate ion ($\\text{MnO}_4^-$) exhibits an intense purple colour due to ligand-to-metal charge transfer (LMCT), not $d-d$ transition.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, C and D",
          "A, B and C only",
          "C and D only",
          "A and B only"], 0,
         "All four statements are accurate NCERT facts: Sc3+ (3d0) and Zn2+ (3d10) are colourless due to lack of d-d transitions; Cu2+ (3d9) has an unpaired electron in eg and is blue; MnO4- has Mn(+7, 3d0) and its intense purple colour arises from LMCT.",
         "MnO4- is coloured by charge transfer, not d-d transition.",
         "d0 and d10 ions are colourless; MnO4- colour is caused by LMCT charge transfer."),

        # 34. Organic Principles - Geometrical Isomerism
        ("Organic Chemistry - Some Basic Principles", "Geometrical Isomerism in Oximes", "Direct MCQ",
         "Geometrical isomerism (syn- and anti-isomers) can be exhibited by which class of organic nitrogen derivatives?",
         ["Oximes derived from unsymmetrical aldehydes and ketones",
          "Primary aliphatic amines",
          "Quaternary ammonium salts",
          "Aliphatic amides"], 0,
         "1. In oximes ($>\\text{C}=\\text{N}-\\text{OH}$), the nitrogen atom is $sp^2$ hybridised and possesses a lone pair.\n2. Restricted rotation around the $C=N$ double bond and two different substituents on carbon produce syn- and anti-isomers.\n3. For benzaldoxime: when $-H$ and $-OH$ are on the same side, it is syn; when opposite, it is anti.",
         "Distractors name amines or amides which have free rotation or identical groups.",
         "Oximes exhibit geometrical isomerism (syn/anti) due to restricted rotation around the $C=N$ bond."),

        # 35. Hydrocarbons - Kucherov Reaction
        ("Hydrocarbons", "Acidic Hydration of Alkynes (Kucherov Reaction)", "Direct MCQ",
         "The reaction of propyne ($\\text{CH}_3-\\text{C}\\equiv\\text{CH}$) with dilute $\\text{H}_2\\text{SO}_4$ in the presence of $\\text{HgSO}_4$ catalyst at $333\\text{ K}$ yields:",
         ["Propan-2-one (Acetone) via Markownikoff enol tautomerization",
          "Propanal",
          "Propanoic acid",
          "Propan-1-ol"], 0,
         "1. Propyne undergoes electrophilic addition of water according to Markownikoff's rule.\n2. In the presence of $\\text{Hg}^{2+}$, $\\text{OH}^-$ adds to the internal carbon C-2:\n   $$\\text{CH}_3-\\text{C}\\equiv\\text{CH} + \\text{H}_2\\text{O} \\xrightarrow{\\text{Hg}^{2+}/\\text{H}^+} [\\text{CH}_3-\\text{C}(\\text{OH})=\\text{CH}_2]$$.\n3. The unstable enol immediately undergoes keto-enol tautomerism to form propan-2-one (acetone):\n   $$[\\text{CH}_3-\\text{C}(\\text{OH})=\\text{CH}_2] \\rightleftharpoons \\text{CH}_3-\\text{CO}-\\text{CH}_3$$.",
         "Propanal would require anti-Markownikoff addition (hydroboration-oxidation).",
         "Kucherov reaction of propyne yields propan-2-one via Markownikoff addition and enol tautomerization."),

        # 36. Haloalkanes - Saytzeff vs Hofmann Multi-Statement
        ("Haloalkanes and Haloarenes", "Saytzeff vs Hofmann Elimination Rules", "Multi-Statement",
         "Which of the following statements regarding dehydrohalogenation ($E_2$ elimination) of alkyl halides are correct?\n\n"
         "A. Dehydrohalogenation with small unhindered bases (e.g. $\\text{C}_2\\text{H}_5\\text{O}^- / \\text{C}_2\\text{H}_5\\text{OH}$) predominantly yields the more substituted, thermally stable alkene (Saytzeff product).\n"
         "B. Dehydrohalogenation with bulky, sterically hindered bases (e.g. $(\\text{CH}_3)_3\\text{CO}^-\\text{K}^+$) yields the less substituted terminal alkene (Hofmann product) as the major product.\n"
         "C. Dehydrohalogenation of alkyl fluorides predominantly yields the Hofmann alkene due to the strong $-I$ effect and poor leaving ability of fluoride.\n"
         "D. $E_2$ elimination reactions proceed via a stable free carbocation intermediate that frequently undergoes rearrangement.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B and C only",
          "A and B only",
          "B, C and D only",
          "A, B, C and D"], 0,
         "Statements A, B, and C are authentic NCERT facts. Statement D is false because E2 is a concerted bimolecular elimination occurring in a single step via an anti-coplanar transition state without any carbocation intermediate (no rearrangement).",
         "E2 has no carbocation intermediate; E1 has a carbocation intermediate.",
         "E2 elimination: Small base gives Saytzeff; bulky base gives Hofmann; no carbocation intermediate."),

        # 37. Ethers - Anisole Cleavage Assertion-Reason
        ("Alcohols, Phenols and Ethers", "Ether Cleavage with Excess Hot Concentrated HI", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** Heating anisole (methoxybenzene) with concentrated hydroiodic acid ($\\text{HI}$) yields phenol and iodomethane ($\\text{CH}_3\\text{I}$), but never iodobenzene and methanol.\n\n"
         "**Reason (R):** The phenyl-oxygen bond ($\\text{C}_{sp^2}-\\text{O}$) possesses partial double-bond character due to resonance with the benzene ring and is much stronger than the aliphatic methyl-oxygen single bond ($\\text{C}_{sp^3}-\\text{O}$).\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "In protonated anisole, iodide attacks the sp3 methyl carbon via SN2 to form methyl iodide. The aromatic C-O bond resists cleavage due to partial double bond character and high resonance energy. Both statements are true and Reason directly explains Assertion.",
         "Iodobenzene cannot form because the aromatic C-O bond resists cleavage.",
         "Anisole cleavage with $\\text{HI}$ produces phenol and $\\text{CH}_3\\text{I}$ because the aromatic $\\text{C}_{sp^2}-\\text{O}$ bond resists cleavage."),

        # 38. Aldehydes - Semicarbazide
        ("Aldehydes, Ketones and Carboxylic Acids", "Reactivity towards Semicarbazide", "Direct MCQ",
         "Semicarbazide ($\\text{H}_2\\text{N}-\\text{CO}-\\text{NH}-\\text{NH}_2$) contains two $-\\text{NH}_2$ groups. Only one of the amino groups acts as a nucleophile in forming semicarbazones with carbonyl compounds. This active nucleophilic amino group is:",
         ["The terminal hydrazine $-\\text{NH}_2$ group attached to $-\\text{NH}-$, because its lone pair is not delocalized into the carbonyl group",
          "The amide $-\\text{NH}_2$ attached to $C=O$",
          "Both amino groups with equal reactivity",
          "The central $-\\text{NH}-$ group"], 0,
         "1. Structure: $\\text{H}_2\\text{N}^1-\\text{C}(=\\text{O})-\\text{NH}-\\text{NH}_2^2$.\n2. The lone pair of electrons on the amide nitrogen ($\text{N}^1$) is delocalized into the adjacent carbonyl group via resonance:\n   $$\\text{H}_2\\text{N}-\\text{C}(=\\text{O})- \\longleftrightarrow \\text{H}_2\\text{N}^+=\\text{C}(\\text{O}^-)-$$.\n3. This resonance decreases electron density on $\\text{N}^1$, rendering it non-nucleophilic.\n4. The hydrazine amino group ($\text{N}^2$) is insulated from resonance; its lone pair remains localized and freely available for nucleophilic addition.",
         "Distractors choose the amide nitrogen directly attached to carbonyl.",
         "In semicarbazide, only the hydrazine $-\\text{NH}_2$ is nucleophilic; the amide lone pair is delocalized into $C=O$."),

        # 39. Aldehydes - HVZ Reaction
        ("Aldehydes, Ketones and Carboxylic Acids", "Hell-Volhard-Zelinsky (HVZ) Reaction", "Direct MCQ",
         "The Hell-Volhard-Zelinsky (HVZ) reaction involves the treatment of carboxylic acids possessing $\\alpha$-hydrogens with bromine in the presence of red phosphorus to yield:",
         ["$\\alpha$-Bromocarboxylic acids", "$\beta$-Bromocarboxylic acids", "Acyl bromides", "Alkanes"], 0,
         "1. Reagents: $\\text{R}-\\text{CH}_2\\text{COOH} + \\text{Br}_2 \\xrightarrow{\\text{Red P}} \\text{R}-\\text{CH}(\\text{Br})\\text{COOH}$.\n2. The reaction specifically halogenates the $\\alpha$-position of carboxylic acids.\n3. Acids lacking $\\alpha$-hydrogens (e.g. formic acid, benzoic acid, trimethylacetic acid) do NOT undergo the HVZ reaction.\n4. The product is an $\\alpha$-halo carboxylic acid.",
         "$\beta$-position is unreactive; acyl bromides hydrolyse back to carboxylic acid during workup.",
         "HVZ reaction halogenates exclusively the $\\alpha$-position of aliphatic carboxylic acids with $\\alpha$-hydrogens."),

        # 40. Amines - Hinsberg Match List
        ("Amines", "Separation of Amines via Hinsberg Method", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Class of Amine) | List-II (Reaction with Benzenesulphonyl Chloride) |\n"
         "| :--- | :--- |\n"
         "| **A.** Primary amine ($1^\\circ$) | **I.** Forms sulphonamide containing acidic $\\text{N}-\\text{H}$, soluble in aqueous $\\text{KOH}$ |\n"
         "| **B.** Secondary amine ($2^\\circ$) | **II.** Forms sulphonamide lacking acidic $\\text{N}-\\text{H}$, insoluble in aqueous $\\text{KOH}$ |\n"
         "| **C.** Tertiary amine ($3^\\circ$) | **III.** Does not react with Hinsberg's reagent (no replaceable hydrogen) |\n"
         "| **D.** Quaternary ammonium salt | **IV.** Ionic salt, non-reactive with sulphonyl halides |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. $1^\\circ$ amine forms N-alkylbenzenesulphonamide, soluble in $\\text{KOH}$ due to acidic proton $\\to$ I.\n2. $2^\\circ$ amine forms N,N-dialkylbenzenesulphonamide, insoluble in $\\text{KOH}$ $\\to$ II.\n3. $3^\\circ$ amine has no hydrogen on nitrogen and does not react $\\to$ III.\n4. Quaternary salts are unreactive ionic compounds $\\to$ IV.",
         "Distractors swap solubility between primary and secondary amine products.",
         "Hinsberg method: $1^\\circ$ amine product dissolves in alkali; $2^\\circ$ amine product is insoluble; $3^\\circ$ does not react."),

        # 41. Biomolecules - Vitamins Match List
        ("Biomolecules", "Vitamins and Deficiency Diseases", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Vitamin) | List-II (Characteristic Deficiency Disease) |\n"
         "| :--- | :--- |\n"
         "| **A.** Vitamin $B_1$ (Thiamine) | **I.** Beri-beri (loss of appetite, retarded growth) |\n"
         "| **B.** Vitamin $B_{12}$ (Cobalamin) | **II.** Pernicious anaemia (RBC deficiency in haemoglobin) |\n"
         "| **C.** Vitamin C (Ascorbic acid) | **III.** Scurvy (bleeding gums) |\n"
         "| **D.** Vitamin D (Calciferol) | **IV.** Rickets in children and osteomalacia in adults |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. Vitamin $B_1$ (Thiamine) deficiency causes Beri-beri $\\to$ I.\n2. Vitamin $B_{12}$ (Cyanocobalamin) deficiency causes Pernicious anaemia $\\to$ II.\n3. Vitamin C (Ascorbic acid) deficiency causes Scurvy $\\to$ III.\n4. Vitamin D deficiency causes Rickets in children and osteomalacia in adults $\\to$ IV.",
         "Distractors swap Beri-beri and Scurvy or Pernicious anaemia.",
         "Vitamins: $B_1$ (Beri-beri), $B_{12}$ (Pernicious anaemia), C (Scurvy), D (Rickets)."),

        # 42. Biomolecules - Essential Amino Acids
        ("Biomolecules", "Essential Amino Acids", "Direct MCQ",
         "Which of the following sets contains exclusively ESSENTIAL amino acids that cannot be synthesized in the human body and must be supplied in diet?",
         ["Valine, Leucine, Isoleucine, Lysine, Phenylalanine",
          "Glycine, Alanine, Serine, Glutamic acid",
          "Aspartic acid, Proline, Tyrosine, Cysteine",
          "Alanine, Glutamine, Asparagine, Glycine"], 0,
         "1. Ten essential amino acids: Valine, Leucine, Isoleucine, Phenylalanine, Methionine, Tryptophan, Threonine, Lysine, Histidine, Arginine.\n2. Non-essential amino acids are synthesized by human metabolic pathways (Glycine, Alanine, Serine, Aspartic acid, Glutamic acid, etc.).\n3. Set (1) consists entirely of essential amino acids.",
         "Sets (2), (3), and (4) consist of non-essential amino acids synthesized in the liver.",
         "Essential amino acids include Valine, Leucine, Isoleucine, Lysine, and Phenylalanine."),

        # 43. Organic Principles - Carbocation Rearrangement
        ("Organic Chemistry - Some Basic Principles", "Carbocation Rearrangement in Alcohol Dehydration", "Direct MCQ",
         "The acid-catalysed dehydration of 3,3-dimethylbutan-2-ol ($\\text{CH}_3-\\text{C}(\\text{CH}_3)_2-\\text{CH}(\\text{OH})-\\text{CH}_3$) with concentrated $\\text{H}_2\\text{SO}_4$ yields 2,3-dimethylbut-2-ene as the major product. This occurs via:",
         ["A 1,2-methyl shift converting a secondary carbocation into a more stable tertiary carbocation",
          "Direct E2 elimination without intermediate",
          "A 1,2-hydride shift",
          "Anti-Markownikoff free radical addition"], 0,
         "1. Protonation of $-OH$ followed by loss of water yields a secondary carbocation: $\\text{CH}_3-\\text{C}(\\text{CH}_3)_2-\\text{CH}^+-\\text{CH}_3$.\n2. A 1,2-methyl shift occurs:\n   $$\\text{CH}_3-\\text{C}^+(\\text{CH}_3)-\\text{CH}(\\text{CH}_3)-\\text{CH}_3$$, generating a stable tertiary carbocation.\n3. Loss of proton gives the most substituted, tetra-alkylated alkene: 2,3-dimethylbut-2-ene (major product).",
         "1,2-hydride shift is impossible because the adjacent carbon has no hydrogen.",
         "Alcohol dehydration with rearrangement proceeds via 1,2-methyl shift to form a more stable $3^\\circ$ carbocation."),

        # 44. Haloalkanes - Picryl Chloride
        ("Haloalkanes and Haloarenes", "Nucleophilic Aromatic Substitution in Nitrochlorobenzenes", "Direct MCQ",
         "The presence of nitro groups ($-\\text{NO}_2$) at ortho and para positions facilitates nucleophilic substitution of chlorine in chlorobenzene. Which compound undergoes hydrolysis with aqueous $\\text{NaOH}$ under the mildest conditions ($warm\\ water$ at $40^\\circ\\text{C}$)?",
         ["2,4,6-Trinitrochlorobenzene (Picryl chloride)",
          "2,4-Dinitrochlorobenzene",
          "4-Nitrochlorobenzene",
          "Chlorobenzene"], 0,
         "1. Nucleophilic aromatic substitution ($S_N\\text{Ar}$) proceeds via a Meisenheimer carbanion complex.\n2. Negative charge generated in the transition state is strongly stabilized by resonance with $-\\text{NO}_2$ groups at ortho and para positions.\n3. Chlorobenzene requires drastic conditions ($300^\\circ\\text{C}, 300\\text{ atm}$).\n4. 4-Nitrochlorobenzene requires $15\\%\\text{ NaOH}$ at $170^\\circ\\text{C}$; 2,4-dinitrochlorobenzene requires $95^\\circ\\text{C}$.\n5. Picryl chloride has three $-\\text{NO}_2$ groups stabilizing the intermediate so strongly that warm water alone ($40^\\circ\\text{C}$) hydrolyses it into picric acid.",
         "Distractors name compounds with fewer nitro groups requiring higher temperatures.",
         "Picryl chloride hydrolyses rapidly in warm water due to 3 ortho/para $-\\text{NO}_2$ groups stabilizing the Meisenheimer intermediate."),

        # 45. Aldehydes - Cannizzaro Statement Pair
        ("Aldehydes, Ketones and Carboxylic Acids", "Cannizzaro Disproportionation Mechanism", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Benzaldehyde ($\\text{C}_6\\text{H}_5\\text{CHO}$) undergoes Cannizzaro reaction when heated with concentrated ($50\\%$) $\\text{NaOH}$ solution.\n\n"
         "**Statement II:** In the Cannizzaro reaction, one molecule of aldehyde is reduced to alcohol while another is oxidised to carboxylic acid salt via hydride ion ($\\text{H}^-$) transfer.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Benzaldehyde lacks an $\\alpha$-hydrogen atom, so it cannot form an enolate or undergo aldol condensation.\n2. In concentrated alkali, hydroxide attacks the carbonyl carbon, forming a tetrahedral dianion.\n3. The hydride ion ($\\text{H}^-$) is transferred directly from this intermediate to a second aldehyde molecule $\\to$ Rate-determining step.\n4. One molecule reduces to benzyl alcohol, while the other oxidises to sodium benzoate.\n5. Both statements are accurate NCERT textbook principles.",
         "Distractors falsely claim proton transfer instead of hydride transfer.",
         "Cannizzaro reaction is a redox disproportionation of aldehydes lacking $\\alpha$-H mediated by hydride ion transfer."),

        # 46. Coordination - Spectrochemical Series
        ("Coordination Compounds", "Spectrochemical Series Order of Ligands", "Direct MCQ",
         "According to the spectrochemical series based on experimental crystal field splitting parameters ($\\Delta_o$), the correct increasing order of field strength of ligands is:",
         ["$\\text{I}^- < \\text{Br}^- < \\text{Cl}^- < \\text{F}^- < \\text{H}_2\\text{O} < \\text{NH}_3 < \\text{en} < \\text{CN}^- < \\text{CO}$",
          "$\\text{CO} < \\text{CN}^- < \\text{en} < \\text{NH}_3 < \\text{H}_2\\text{O} < \\text{F}^- < \\text{Cl}^- < \\text{Br}^- < \\text{I}^-$",
          "$\\text{F}^- < \\text{Cl}^- < \\text{Br}^- < \\text{I}^- < \\text{H}_2\\text{O} < \\text{NH}_3 < \\text{en} < \\text{CO}$",
          "$\\text{I}^- < \\text{Cl}^- < \\text{F}^- < \\text{NH}_3 < \\text{H}_2\\text{O} < \\text{en} < \\text{CN}^- < \\text{CO}$"], 0,
         "1. Spectrochemical series arranges ligands in order of increasing crystal field splitting energy ($\\Delta_o$):\n   $$\\text{I}^- < \\text{Br}^- < \\text{S}^{2-} < \\text{SCN}^- < \\text{Cl}^- < \\text{NO}_3^- < \\text{F}^- < \\text{OH}^- < \\text{C}_2\\text{O}_4^{2-} < \\text{H}_2\\text{O} < \\text{NCS}^- < \\text{EDTA}^{4-} < \\text{NH}_3 < \\text{en} < \\text{CN}^- < \\text{CO}$$.\n2. Halides are weak field ligands ($\\Delta_o < P$), while cyanide and carbon monoxide are strongest field ligands ($\\Delta_o > P$).",
         "Option (2) is inverted; Option (3) inverts halide trend.",
         "Spectrochemical series: $\\text{I}^- < \\text{Br}^- < \\text{Cl}^- < \\text{F}^- < \\text{H}_2\\text{O} < \\text{NH}_3 < \\text{en} < \\text{CN}^- < \\text{CO}$."),

        # 47. Practical Chemistry - Flame Test Match List
        ("Practical Chemistry", "Characteristic Flame Test Colors of s-Block Cations", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Metal Ion) | List-II (Characteristic Flame Coloration) |\n"
         "| :--- | :--- |\n"
         "| **A.** Lithium ($\\text{Li}^+$) | **I.** Crimson red |\n"
         "| **B.** Sodium ($\\text{Na}^+$) | **II.** Golden yellow |\n"
         "| **C.** Potassium ($\\text{K}^+$) | **III.** Violet / Lilac |\n"
         "| **D.** Barium ($\\text{Ba}^{2+}$) | **IV.** Apple green |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. Lithium salts impart crimson red colour to bunsen flame $\\to$ I.\n2. Sodium imparts intense golden yellow colour $\\to$ II.\n3. Potassium imparts violet / lilac colour $\\to$ III.\n4. Barium imparts characteristic apple green colour $\\to$ IV (Calcium is brick red; Strontium is crimson).",
         "Distractors swap crimson red (Li) with golden yellow (Na).",
         "Flame test colours: $\\text{Li}^+$ (crimson), $\\text{Na}^+$ (golden yellow), $\\text{K}^+$ (violet), $\\text{Ba}^{2+}$ (apple green)."),

        # 48. Hydrocarbons - Hydroboration
        ("Hydrocarbons", "Hydroboration-Oxidation of Terminal Alkynes", "Direct MCQ",
         "When propyne ($\\text{CH}_3-\\text{C}\\equiv\\text{CH}$) is treated with diborane ($\\text{B}_2\\text{H}_6$) followed by alkaline hydrogen peroxide ($\\text{H}_2\\text{O}_2 / \\text{NaOH}$), the major organic product obtained is:",
         ["Propanal (Propionaldehyde) via anti-Markownikoff hydration",
          "Propan-2-one (Acetone)",
          "Propanoic acid",
          "Propan-1-ol"], 0,
         "1. Hydroboration-oxidation adds water across the triple bond with anti-Markownikoff regioselectivity.\n2. Boron attaches to the less hindered terminal carbon: $\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{B}<$.\n3. Alkaline $\\text{H}_2\\text{O}_2$ oxidises the organoborane to an enol: $\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{OH}$.\n4. Tautomerization of the terminal enol yields the aldehyde propanal ($\\text{CH}_3\\text{CH}_2\\text{CHO}$).\n5. (Note: Acidic $\\text{Hg}^{2+}/\\text{H}_2\\text{SO}_4$ gives Markownikoff ketone acetone).",
         "Acetone is obtained from oxymercuration; hydroboration gives aldehyde.",
         "Hydroboration-oxidation of terminal alkynes gives aldehydes via anti-Markownikoff hydration."),

        # 49. Carboxylic Acids - Inductive Acidity
        ("Aldehydes, Ketones and Carboxylic Acids", "Inductive Effect on Carboxylic Acid Strength", "Direct MCQ",
         "The correct decreasing order of acidic strength among $\\alpha$-halosubstituted acetic acids is:",
         ["$\\text{F}-\\text{CH}_2\\text{COOH} > \\text{Cl}-\\text{CH}_2\\text{COOH} > \\text{Br}-\\text{CH}_2\\text{COOH} > \\text{I}-\\text{CH}_2\\text{COOH} > \\text{CH}_3\\text{COOH}$",
          "$\\text{I}-\\text{CH}_2\\text{COOH} > \\text{Br}-\\text{CH}_2\\text{COOH} > \\text{Cl}-\\text{CH}_2\\text{COOH} > \\text{F}-\\text{CH}_2\\text{COOH} > \\text{CH}_3\\text{COOH}$",
          "$\\text{Cl}-\\text{CH}_2\\text{COOH} > \\text{F}-\\text{CH}_2\\text{COOH} > \\text{Br}-\\text{CH}_2\\text{COOH} > \\text{I}-\\text{CH}_2\\text{COOH} > \\text{CH}_3\\text{COOH}$",
          "$\\text{CH}_3\\text{COOH} > \\text{F}-\\text{CH}_2\\text{COOH} > \\text{Cl}-\\text{CH}_2\\text{COOH} > \\text{Br}-\\text{CH}_2\\text{COOH} > \\text{I}-\\text{CH}_2\\text{COOH}$"], 0,
         "1. Halogens exert electron-withdrawing inductive effect ($-I$), which disperses negative charge on the carboxylate anion, stabilizing the conjugate base.\n2. The magnitude of the $-I$ effect is directly proportional to electronegativity: $\\text{F} > \\text{Cl} > \\text{Br} > \\text{I}$.\n3. Consequently, fluoroacetic acid is the strongest acid ($pK_a = 2.57$), and acetic acid is the weakest ($pK_a = 4.76$).",
         "Option (2) reflects atomic size instead of electronegativity.",
         "Carboxylic acid acidity follows halogen electronegativity $-I$ magnitude: $\\text{F} > \\text{Cl} > \\text{Br} > \\text{I}$."),

        # 50. Electrochemistry - Fuel Cell
        ("Electrochemistry", "Efficiency and Reactions in Hydrogen-Oxygen Fuel Cell", "Direct MCQ",
         "In the hydrogen-oxygen ($\\text{H}_2-\\text{O}_2$) fuel cell used in the Apollo space program, the overall cell reaction and theoretical thermodynamic efficiency are:",
         ["$2\\text{H}_2(g) + \\text{O}_2(g) \\to 2\\text{H}_2\\text{O}(l)$, with efficiency $\\eta = \\frac{\\Delta G}{\\Delta H} \\approx 70\\%$ (producing non-polluting drinking water)",
          "$2\\text{H}_2\\text{O}(l) \\to 2\\text{H}_2(g) + \\text{O}_2(g)$, with efficiency $40\\%$",
          "$\\text{H}_2(g) + \\text{O}_2(g) \\to \\text{H}_2\\text{O}_2(l)$, with efficiency $90\\%$",
          "$2\\text{H}_2(g) + \\text{O}_2(g) \\to 2\\text{H}_2\\text{O}(g)$, consuming external electric power"], 0,
         "1. Anode reaction: $2\\text{H}_2(g) + 4\\text{OH}^-(aq) \\to 4\\text{H}_2\\text{O}(l) + 4e^-$.\n2. Cathode reaction: $\\text{O}_2(g) + 2\\text{H}_2\\text{O}(l) + 4e^- \\to 4\\text{OH}^-(aq)$.\n3. Net reaction: $2\\text{H}_2(g) + \\text{O}_2(g) \\to 2\\text{H}_2\\text{O}(l)$.\n4. Efficiency $\\eta = \\frac{\\Delta G}{\\Delta H} \\approx 70\\%$, far higher than conventional thermal power plants ($~40\\%$). Water produced was used by astronauts.",
         "Option (2) is electrolytic decomposition, not fuel cell generation.",
         "$\\text{H}_2-\\text{O}_2$ fuel cell converts chemical energy into electrical energy at $~70\\%$ efficiency, producing water.")
    ]

    assert len(topics_data) == 50, f"Expected 50 Chemistry topics, got {len(topics_data)}"

    for i, item in enumerate(topics_data):
        chapter, topic, q_type, text, options, correct_idx, solution_steps, distractor_analysis, takeaway = item
        q_num = i + 51  # 51 to 100
        sec = "Section A" if (q_num - 50) <= 35 else "Section B"
        q = NeetQuestion(
            q_num=q_num,
            subject="Chemistry",
            section=sec,
            chapter=chapter,
            topic=topic,
            q_type=q_type,
            text=text,
            options=options,
            correct_idx=correct_idx,
            solution_steps=solution_steps,
            distractor_analysis=distractor_analysis,
            takeaway=takeaway
        )
        questions.append(q)

    return questions
