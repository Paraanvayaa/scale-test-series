# -*- coding: utf-8 -*-
"""
NEET Mock Generation Engine - Difficult Curriculum (Chemistry)
Strictly calibrated to NTA NEET-UG standards (2023-2027 Predictive Rigor).
Difficult conceptual and analytical depth: multi-step equilibria,
abnormal colligative properties, CFSE calculation, salt analysis tests,
regioselective organic mechanisms, stereoisomer counts, and anomalous periodic trends.
Strictly NCERT-aligned.

Proportions for 50 Questions:
- Direct MCQ: 29
- Statement I & II: 7
- Match List: 7
- Assertion & Reason: 4
- Multi-Statement: 3
Total: 50
"""
from neet_models import NeetQuestion

def get_chemistry_questions_diff(mock_num):
    questions = []
    shift = (mock_num - 41) * 3

    topics_data = [
        # 1. Solutions - van 't Hoff Factor & Colligative
        ("Solutions and Colligative Properties", "Degree of Dissociation and Abnormal Freezing Point", "Direct MCQ",
         "A $0.1\\text{ m}$ aqueous solution of potassium ferrocyanide, $\\text{K}_4[\\text{Fe}(\\text{CN})_6]$, is $60%$ ionized at $273\\text{ K}$. If the cryoscopic constant of water is $K_f = 1.86\\text{ K kg mol}^{-1}$, the depression in freezing point $\\Delta T_f$ of this solution is:",
         ["$0.632\\text{ K}$", "$0.186\\text{ K}$", "$0.930\\text{ K}$", "$0.558\\text{ K}$"], 0,
         "1. Dissociation equation: $\\text{K}_4[\\text{Fe}(\\text{CN})_6] \\rightleftharpoons 4\\text{K}^+ + [\\text{Fe}(\\text{CN})_6]^{4-}$. Total ions produced per molecule $n = 4 + 1 = 5$.\n2. Degree of dissociation $\\alpha = 0.60$.\n3. van \'t Hoff factor: $i = 1 + (n - 1)\\alpha = 1 + (5 - 1)(0.60) = 1 + 4(0.60) = 1 + 2.40 = 3.40$.\n4. Depression in freezing point: $\\Delta T_f = i K_f m = 3.40 \\times 1.86 \\times 0.1 = 0.6324\\text{ K} \\approx 0.632\\text{ K}$.",
         "Assuming 100% dissociation ($i=5$) gives $0.930\\text{ K}$; neglecting dissociation ($i=1$) gives $0.186\\text{ K}$.",
         "van \'t Hoff factor for electrolyte with degree of dissociation $\\alpha$: $i = 1 + (n - 1)\\alpha$."),

        # 2. Electrochemistry - Concentration Cell
        ("Electrochemistry", "Hydrogen Concentration Cell EMF with Different Pressures", "Direct MCQ",
         "Consider a concentration cell with two hydrogen gas electrodes dipped in identical $0.1\\text{ M }\\text{HCl}$ solutions at $298\\text{ K}$:\n"
         "$$\\text{Pt}|\\text{H}_2(p_1 = 4\\text{ atm})|\\text{HCl}(0.1\\text{ M})||\\text{HCl}(0.1\\text{ M})|\\text{H}_2(p_2 = 1\\text{ atm})|\\text{Pt}$$\n"
         "The electromotive force ($E_{\\text{cell}}$) of this concentration cell is: (take $\\frac{2.303 R T}{F} = 0.0591\\text{ V}$)",
         ["$+0.0178\\text{ V}$", "$-0.0178\\text{ V}$", "$+0.0356\\text{ V}$", "$0\\text{ V}$"], 0,
         "1. Anode half-reaction (oxidation): $\\text{H}_2(p_1) \\to 2\\text{H}^+ + 2e^-$.\n2. Cathode half-reaction (reduction): $2\\text{H}^+ + 2e^- \\to \\text{H}_2(p_2)$.\n3. Overall cell reaction: $\\text{H}_2(p_1) \\to \\text{H}_2(p_2)$ with $n = 2$ electrons transferred.\n4. Reaction quotient: $Q = \\frac{p_2}{p_1} = \\frac{1}{4}$.\n5. Nernst equation at $298\\text{ K}$ ($E^\\circ_{\\text{cell}} = 0$ for concentration cell):\n   $$E_{\\text{cell}} = -\\frac{0.0591}{2} \\log\\left(\\frac{p_2}{p_1}\\right) = -0.02955 \\log\\left(\\frac{1}{4}\\right) = -0.02955(-2 \\log 2) = +0.02955 \\times 0.602 = +0.0178\\text{ V}$$.",
         "Negative emf results from inverting the ratio $p_2/p_1$; zero assumes gas pressure has no effect.",
         "Concentration cell emf with pressure difference: $E_{\\text{cell}} = \\frac{0.0591}{2}\\log\\left(\\frac{p_1}{p_2}\\right)$."),

        # 3. Electrochemistry - Kohlrausch's Law (Match List)
        ("Electrochemistry", "Limiting Molar Conductivity and Dissociation Constant", "Match List",
         "Match List-I with List-II for molar conductivity relationships and their physical interpretations:\n\n"
         "| List-I (Equation / Parameter) | List-II (Physical Application) |\n"
         "| :--- | :--- |\n"
         "| **A.** $\\Lambda_m^\\circ = \\nu_+ \\lambda_+^\\circ + \\nu_- \\lambda_-^\\circ$ | **I.** Kohlrausch\'s law of independent migration |\n"
         "| **B.** $\\alpha = \\frac{\\Lambda_m}{\\Lambda_m^\\circ}$ | **II.** Degree of dissociation of weak electrolyte |\n"
         "| **C.** $K_a = \\frac{c \\alpha^2}{1 - \\alpha}$ | **III.** Ostwald\'s dilution law for weak acid |\n"
         "| **D.** $\\Lambda_m = \\Lambda_m^\\circ - A \\sqrt{c}$ | **IV.** Debye-Huckel-Onsager equation for strong electrolytes |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Independent migration of ions is Kohlrausch\'s law $\\to$ I.\n2. Ratio of molar conductivity at concentration $c$ to limiting molar conductivity is degree of dissociation $\\alpha \\to$ II.\n3. Acid dissociation constant from Ostwald dilution law $\\to$ III.\n4. Linear decrease of $\\Lambda_m$ with $\\sqrt{c}$ is Debye-Huckel-Onsager equation $\\to$ IV.",
         "Distractors confuse Debye-Huckel equation (strong electrolytes) with Ostwald dilution law (weak electrolytes).",
         "Limiting molar conductivity $\\Lambda_m^\\circ$ of weak electrolytes is determined indirectly via Kohlrausch\'s law."),

        # 4. Chemical Kinetics - Arrhenius Temperature Coefficient
        ("Chemical Kinetics", "Activation Energy Calculation from Two Temperatures", "Direct MCQ",
         "The rate constant of a chemical reaction triples ($k_2 / k_1 = 3$) when the temperature increases from $300\\text{ K}$ to $310\\text{ K}$. The activation energy $E_a$ of this reaction is: (Given: $R = 8.314\\text{ J K}^{-1}\\text{ mol}^{-1}$, $\\log 3 = 0.4771$)",
         ["$84.8\\text{ kJ/mol}$", "$42.4\\text{ kJ/mol}$", "$28.3\\text{ kJ/mol}$", "$120.5\\text{ kJ/mol}$"], 0,
         "1. Integrated Arrhenius equation:\n   $$\\log\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{2.303 R}\\left(\\frac{T_2 - T_1}{T_1 T_2}\\right)$$.\n2. Substituting given values: $\\log 3 = \\frac{E_a}{2.303 \\times 8.314}\\left(\\frac{310 - 300}{300 \\times 310}\\right)$.\n3. $0.4771 = \\frac{E_a}{19.147}\\left(\\frac{10}{93000}\\right) = \\frac{E_a \\times 10}{1.7806 \\times 10^6}$.\n4. $E_a = \\frac{0.4771 \\times 1.7806 \\times 10^6}{10} = 8.495 \\times 10^4\\text{ J/mol} \\approx 84.8\\text{ kJ/mol}$.",
         "42.4 kJ/mol results from using natural log without 2.303; 28.3 kJ/mol uses temperature in Celsius.",
         "Arrhenius equation: $\\log\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{2.303 R}\\left(\\frac{\\Delta T}{T_1 T_2}\\right)$."),

        # 5. Chemical Kinetics - Multi-Step Mechanism (Statement I & II)
        ("Chemical Kinetics", "Steady-State and Rate-Determining Step Kinetics", "Statement I & II",
         "Given below are two statements regarding the reaction $2\\text{NO}(g) + \\text{O}_2(g) \\to 2\\text{NO}_2(g)$:\n\n"
         "Statement I: The reaction follows termolecular third-order kinetics with rate law $\\text{Rate} = k[\\text{NO}]^2[\\text{O}_2]$, proceeding via a fast pre-equilibrium formation of dimer $\\text{N}_2\\text{O}_2$ followed by a slow reaction with $\\text{O}_2$.\n\n"
         "Statement II: The overall rate of this reaction decreases with increasing temperature, exhibiting an apparent negative activation energy.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Mechanism:\n   Step 1 (fast): $2\\text{NO} \\rightleftharpoons \\text{N}_2\\text{O}_2$ ($K_c = [\\text{N}_2\\text{O}_2]/[\\text{NO}]^2$).\n   Step 2 (slow, r.d.s.): $\\text{N}_2\\text{O}_2 + \\text{O}_2 \\to 2\\text{NO}_2$ ($r = k\' [\\text{N}_2\\text{O}_2][\\text{O}_2]$).\n2. Substituting $[\\text{N}_2\\text{O}_2] = K_c [\\text{NO}]^2$ gives $r = k\' K_c [\\text{NO}]^2[\\text{O}_2] = k [\\text{NO}]^2[\\text{O}_2]$. Statement I is correct.\n3. The dimerization $2\\text{NO} \\rightleftharpoons \\text{N}_2\\text{O}_2$ is exothermic ($\\Delta H < 0$). With rising temperature, equilibrium shifts backward ($K_c$ decreases rapidly), exceeding the modest increase in $k\'$. Thus overall rate constant $k = k\' K_c$ decreases with temperature (apparent negative $E_a$). Statement II is correct.",
         "Students usually assume reaction rate always increases with temperature; $2\\text{NO} + \\text{O}_2$ is the famous NCERT exception.",
         "Reactions involving exothermic pre-equilibria can exhibit negative overall temperature coefficients."),

        # 6. Thermodynamics - Ellingham Diagram (Assertion & Reason)
        ("Thermodynamics", "Ellingham Diagram Slopes and Reducing Power Feasibility", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "Assertion (A): In the Ellingham diagram, carbon monoxide (CO) is a more effective reducing agent than carbon (C) for iron oxides at temperatures below $983\\text{ K}$ ($710^\\circ\\text{C}$).\n"
         "Reason (R): Below $983\\text{ K}$, the $\\Delta G^\\circ$ line for the oxidation of $\\text{CO}$ to $\\text{CO}_2$ ($2\\text{CO} + \\text{O}_2 \\to 2\\text{CO}_2$) lies below the $\\Delta G^\\circ$ line for $2\\text{C} + \\text{O}_2 \\to 2\\text{CO}$.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. In the blast furnace, reduction of iron oxides by $\\text{CO}$ occurs predominantly in the upper, cooler region ($T < 983\\text{ K}$). Assertion is TRUE.\n2. In the Ellingham diagram, a lower line can reduce the oxide of a higher line. Below $983\\text{ K}$, the line for $2\\text{CO} + \\text{O}_2 \\to 2\\text{CO}_2$ has a positive slope but lies lower in $\\Delta G^\\circ$ than the line for $2\\text{C} + \\text{O}_2 \\to 2\\text{CO}$ (which has negative slope). Reason is TRUE and explains Assertion.",
         "Above 983 K, carbon (coke) becomes the stronger reducing agent because $2\\text{C} + \\text{O}_2 \\to 2\\text{CO}$ has positive $\\Delta S^\\circ$ and drops with $T$.",
         "Below 983 K, CO reduces iron oxides; above 983 K, solid carbon (coke) is the active reducing agent."),

        # 7. Chemical Equilibrium - Simultaneous Equilibrium
        ("Chemical Equilibrium", "Simultaneous Dissociation of Solid Salt in Common Gas", "Direct MCQ",
         "Solid ammonium hydrogen sulfide decomposes according to:\n"
         "$$\\text{NH}_4\\text{HS}(s) \\rightleftharpoons \\text{NH}_3(g) + \\text{H}_2\\text{S}(g)$$\n"
         "At a certain temperature, $K_p = 64\\text{ atm}^2$. If excess $\\text{NH}_4\\text{HS}(s)$ is placed in an evacuated vessel which already contains ammonia gas at a pressure of $12\\text{ atm}$, the total pressure in the vessel at equilibrium will be:",
         ["$20\\text{ atm}$", "$16\\text{ atm}$", "$24\\text{ atm}$", "$18\\text{ atm}$"], 0,
         "1. Initial pressure of $\\text{NH}_3 = 12\\text{ atm}$, initial $p_{\\text{H}_2\\text{S}} = 0$.\n2. Let additional pressure of $\\text{H}_2\\text{S}$ produced by decomposition be $p$.\n3. At equilibrium:\n   $$p_{\\text{NH}_3} = 12 + p$$,\n   $$p_{\\text{H}_2\\text{S}} = p$$.\n4. Equilibrium constant expression:\n   $$K_p = p_{\\text{NH}_3} \\times p_{\\text{H}_2\\text{S}} = (12 + p)p = 64 \\implies p^2 + 12p - 64 = 0$$.\n5. Factoring the quadratic:\n   $$(p + 16)(p - 4) = 0 \\implies p = 4\\text{ atm}$$.\n6. Equilibrium partial pressures: $p_{\\text{NH}_3} = 12 + 4 = 16\\text{ atm}$, $p_{\\text{H}_2\\text{S}} = 4\\text{ atm}$.\n7. Total equilibrium pressure: $P_{\\text{total}} = p_{\\text{NH}_3} + p_{\\text{H}_2\\text{S}} = 16 + 4 = 20\\text{ atm}$.",
         "16 atm is the partial pressure of ammonia alone; 24 atm forgets to solve the quadratic.",
         "For solid decomposition in presence of common gaseous product, use $(p_0 + p)p = K_p$."),

        # 8. Ionic Equilibrium - Buffer Action
        ("Ionic Equilibrium", "Henderson-Hasselbalch Buffer Capacity and pH Shift", "Direct MCQ",
         "To prepare an acidic buffer solution of $pH = 5.0$, what volume ratio of $0.1\\text{ M }\\text{CH}_3\\text{COONa}$ to $0.1\\text{ M }\\text{CH}_3\\text{COOH}$ must be mixed? (Given: $pK_a(\\text{CH}_3\\text{COOH}) = 4.74$, $\\log 1.82 = 0.26$)",
         ["$1.82 : 1$", "$1 : 1.82$", "$1 : 1$", "$2.5 : 1$"], 0,
         "1. By Henderson-Hasselbalch equation for acidic buffer:\n   $$pH = pK_a + \\log\\left(\\frac{[\\text{Conjugate Base}]}{[\\text{Acid}]}\\right)$$.\n2. Substituting values: $5.0 = 4.74 + \\log\\left(\\frac{[\\text{Salt}]}{[\\text{Acid}]}\\right)$.\n3. $\\log\\left(\\frac{[\\text{Salt}]}{[\\text{Acid}]}\\right) = 5.0 - 4.74 = +0.26$.\n4. Taking antilog: $\\frac{[\\text{Salt}]}{[\\text{Acid}]} = 10^{0.26} = 1.82$.\n5. Since both stock solutions have identical concentration ($0.1\\text{ M}$), the molar ratio equals the volume ratio: $\\frac{V_{\\text{salt}}}{V_{\\text{acid}}} = \\frac{1.82}{1}$.",
         "1 : 1.82 inverts acid and salt; 1 : 1 gives pH = pKa = 4.74.",
         "Henderson-Hasselbalch equation: $pH = pK_a + \\log\\left(\\frac{[\\text{Salt}]}{[\\text{Acid}]}\\right)$."),

        # 9. Ionic Equilibrium - Solubility Product with Common Ion
        ("Ionic Equilibrium", "Sparingly Soluble Salt Common Ion Suppression", "Direct MCQ",
         "The solubility product of silver chromate ($\\text{Ag}_2\\text{CrO}_4$) is $K_{sp} = 1.1 \\times 10^{-12}$. The molar solubility of $\\text{Ag}_2\\text{CrO}_4$ in a $0.1\\text{ M }\\text{AgNO}_3$ solution is:",
         ["$1.1 \\times 10^{-10}\\text{ M}$", "$6.5 \\times 10^{-5}\\text{ M}$", "$1.1 \\times 10^{-11}\\text{ M}$", "$3.3 \\times 10^{-6}\\text{ M}$"], 0,
         "1. Dissociation: $\\text{Ag}_2\\text{CrO}_4(s) \\rightleftharpoons 2\\text{Ag}^+ + \\text{CrO}_4^{2-}$. Let solubility be $s$.\n2. In $0.1\\text{ M }\\text{AgNO}_3$, $[\\text{Ag}^+] = 0.1 + 2s \\approx 0.1\\text{ M}$ (since $s \\ll 0.1$).\n3. Concentration of chromate: $[\\text{CrO}_4^{2-}] = s$.\n4. $K_{sp} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (0.1)^2 \\times s = 10^{-2} s$.\n5. $s = \\frac{K_{sp}}{10^{-2}} = \\frac{1.1 \\times 10^{-12}}{10^{-2}} = 1.1 \\times 10^{-10}\\text{ M}$.",
         "$6.5 \\times 10^{-5}\\text{ M}$ is the solubility in pure water ($s = \\sqrt[3]{K_{sp}/4}$).",
         "Common ion effect dramatically suppresses solubility: for $A_2 B$ salt, $s = \\frac{K_{sp}}{[A^+]^2}$."),

        # 10. Atomic Structure - Quantum Numbers & Radial Nodes (Match List)
        ("Atomic Structure", "Radial and Angular Nodes of Hydrogenic Orbitals", "Match List",
         "Match List-I with List-II for atomic orbitals and their total node counts:\n\n"
         "| List-I (Atomic Orbital) | List-II (Radial Nodes, Angular Nodes) |\n"
         "| :--- | :--- |\n"
         "| **A.** $3p$ orbital | **I.** Radial $= 1$, Angular $= 1$ |\n"
         "| **B.** $4d$ orbital | **II.** Radial $= 1$, Angular $= 2$ |\n"
         "| **C.** $4s$ orbital | **III.** Radial $= 3$, Angular $= 0$ |\n"
         "| **D.** $2p$ orbital | **IV.** Radial $= 0$, Angular $= 1$ |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Radial nodes $= n - l - 1$; Angular nodes $= l$.\n2. For $3p$: $n = 3, l = 1 \\implies$ Radial $= 3 - 1 - 1 = 1$, Angular $= 1 \\to$ I.\n3. For $4d$: $n = 4, l = 2 \\implies$ Radial $= 4 - 2 - 1 = 1$, Angular $= 2 \\to$ II.\n4. For $4s$: $n = 4, l = 0 \\implies$ Radial $= 4 - 0 - 1 = 3$, Angular $= 0 \\to$ III.\n5. For $2p$: $n = 2, l = 1 \\implies$ Radial $= 2 - 1 - 1 = 0$, Angular $= 1 \\to$ IV.",
         "Confusing radial nodes ($n-l-1$) with total nodes ($n-1$).",
         "Total nodes in any orbital $= n - 1 = (n - l - 1)_{\\text{radial}} + l_{\\text{angular}}$."),

        # 11. Periodic Table - Anomalous Ionization Enthalpy (Statement I & II)
        ("Classification of Elements and Periodicity", "Group 13 Ionization Enthalpy Anomalies and Inert Pair Effect", "Statement I & II",
         "Given below are two statements regarding Group 13 elements:\n\n"
         "Statement I: The first ionization enthalpy of Gallium ($579\\text{ kJ/mol}$) is slightly higher than that of Aluminium ($577\\text{ kJ/mol}$).\n\n"
         "Statement II: Gallium has poor shielding provided by the intervening ten $3d$ electrons, resulting in a higher effective nuclear charge ($Z_{\\text{eff}}$) and contracted atomic radius compared to Aluminium.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Expected trend down a group is a monotonic decrease in ionization enthalpy, but $\\text{Ga}$ has higher first ionization enthalpy than $\\text{Al}$. Statement I is correct.\n2. Gallium follows the first transition series; its $3d^{10}$ electrons exhibit poor shielding of valence electrons. The outer electrons feel a stronger nuclear pull (d-block contraction), making atomic radius of $\\text{Ga}$ ($135\\text{ pm}$) smaller than $\\text{Al}$ ($143\\text{ pm}$) and raising ionization enthalpy. Statement II is correct and accurately explains Statement I.",
         "Assuming atomic radius always increases down Group 13 is a classic NEET trap.",
         "Group 13 radius anomaly: $r(\\text{Ga}) < r(\\text{Al})$ due to poor shielding of $3d^{10}$ electrons (d-block contraction)."),

        # 12. Chemical Bonding - MOT Magnetism (Match List)
        ("Chemical Bonding and Molecular Structure", "Molecular Orbital Theory Bond Order and Paramagnetism", "Match List",
         "Match List-I with List-II for diatomic species and their MOT characteristics according to Molecular Orbital Theory:\n\n"
         "| List-I (Molecular Species) | List-II (Bond Order & Magnetic Nature) |\n"
         "| :--- | :--- |\n"
         "| **A.** $\\text{O}_2^+$ ($15$ electrons) | **I.** Bond order $= 2.5$, Paramagnetic ($1$ unpaired electron) |\n"
         "| **B.** $\\text{O}_2^{2-}$ ($18$ electrons) | **II.** Bond order $= 1.0$, Diamagnetic ($0$ unpaired electrons) |\n"
         "| **C.** $\\text{N}_2^+$ ($13$ electrons) | **III.** Bond order $= 2.5$, Paramagnetic ($1$ unpaired electron) |\n"
         "| **D.** $\\text{C}_2$ ($12$ electrons) | **IV.** Bond order $= 2.0$, Diamagnetic (contains only $\\pi$-bonds) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. $\\text{O}_2^+$: $15e^-$, configuration $\\sigma_{1s}^2 \\sigma_{1s}^{*2} \\dots \\pi_{2p_x}^{*1}$. $\\text{BO} = (10-5)/2 = 2.5$, paramagnetic $\\to$ I.\n2. $\\text{O}_2^{2-}$: $18e^-$, peroxide ion. $\\text{BO} = (10-8)/2 = 1.0$, all paired, diamagnetic $\\to$ II.\n3. $\\text{N}_2^+$: $13e^-$, $\\text{BO} = (9-4)/2 = 2.5$, one unpaired electron, paramagnetic $\\to$ III.\n4. $\\text{C}_2$: $12e^-$, configuration ends in $(\\pi_{2p_x}^2 = \\pi_{2p_y}^2)$. $\\text{BO} = (8-4)/2 = 2.0$. Diamagnetic, and both bonds are $\\pi$-bonds because the last 4 electrons reside in $\\pi$ MOs $\\to$ IV.",
         "Remember: $\\text{C}_2$ has NO $\\sigma$-bond in its double bond; both bonds are $\\pi$-bonds!",
         "In $\\text{C}_2$ molecule, both bonds in the double bond are $\\pi$-bonds due to filling of $\\pi_{2p}$ orbitals."),

        # 13. Chemical Bonding - VSEPR Shapes (Multi-Statement)
        ("Chemical Bonding and Molecular Structure", "VSEPR Geometry and Lone Pair Repulsion", "Multi-Statement",
         "Consider the molecules $\\text{XeF}_4$, $\\text{SF}_4$, $\\text{XeO}_3$, and $\\text{ClF}_3$:\n\n"
         "A. $\\text{XeF}_4$ has $sp^3d^2$ hybridization with a square planar geometry and two axial lone pairs.\n"
         "B. $\\text{SF}_4$ has $sp^3d$ hybridization with a see-saw geometry where the single lone pair occupies an equatorial position.\n"
         "C. $\\text{ClF}_3$ has $sp^3d$ hybridization with a T-shaped geometry where both lone pairs occupy equatorial positions.\n"
         "D. $\\text{XeO}_3$ has $sp^3d$ hybridization with a trigonal planar geometry.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and C only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. $\\text{XeF}_4$: 4 bond pairs + 2 lone pairs $= 6$ steric number $\\implies sp^3d^2$. Lone pairs take trans axial positions to minimize $90^\\circ$ repulsions $\\implies$ Square planar. Statement A is TRUE.\n2. $\\text{SF}_4$: 4 bond pairs + 1 lone pair $= 5$ steric number $\\implies sp^3d$. Lone pair occupies equatorial position to minimize repulsions $\\implies$ See-saw shape. Statement B is TRUE.\n3. $\\text{ClF}_3$: 3 bond pairs + 2 lone pairs $= 5$ steric number $\\implies sp^3d$. Both lone pairs take equatorial positions $\\implies$ T-shaped. Statement C is TRUE.\n4. $\\text{XeO}_3$: 3 bond pairs + 1 lone pair $= 4$ steric number $\\implies sp^3$ hybridization with pyramidal geometry (not $sp^3d$ trigonal planar). Statement D is FALSE.",
         "Placing lone pairs axially in $sp^3d$ geometry creates too many $90^\\circ$ repulsions; they ALWAYS occupy equatorial positions in $sp^3d$.",
         "In $sp^3d$ hybridization, lone pairs always prefer equatorial positions to minimize $90^\\circ$ repulsions."),

        # 14. Coordination Compounds - CFSE Calculation
        ("Coordination Compounds", "Crystal Field Stabilization Energy for d6 Octahedral Complex", "Direct MCQ",
         "The crystal field stabilization energy (CFSE) for a high-spin octahedral complex of $\\text{Co}^{3+}$ ($d^6$) and a low-spin octahedral complex of $\\text{Co}^{3+}$ ($d^6$) are respectively: (where $\\Delta_o$ is octahedral splitting and $P$ is pairing energy)",
         ["$-0.4\\Delta_o$ and $-2.4\\Delta_o + 2P$", "$-2.4\\Delta_o + 2P$ and $-0.4\\Delta_o$", "$-0.8\\Delta_o$ and $-2.4\\Delta_o$", "$-0.4\\Delta_o + P$ and $-2.4\\Delta_o + 3P$"], 0,
         "1. For $d^6$ configuration in octahedral field:\n   $\\text{CFSE} = \\left(-0.4 n_{t_{2g}} + 0.6 n_{e_g}\\right)\\Delta_o + m P$, where $m$ is the net number of additional electron pairs compared to free ion.\n2. Free ion $d^6$ has 1 pair and 4 unpaired electrons.\n3. High-spin complex (weak field, $\\Delta_o < P$): configuration is $t_{2g}^4 e_g^2$.\n   $$\\text{CFSE} = \\left[-0.4(4) + 0.6(2)\\right]\\Delta_o = (-1.6 + 1.2)\\Delta_o = -0.4\\Delta_o$$. (No extra pairs, $m = 0$).\n4. Low-spin complex (strong field, $\\Delta_o > P$): configuration is $t_{2g}^6 e_g^0$.\n   $$\\text{CFSE} = \\left[-0.4(6) + 0.6(0)\\right]\\Delta_o + (3 - 1)P = -2.4\\Delta_o + 2P$$.",
         "Forgetting that the free ion already had 1 pair leads to calculating $3P$ instead of $2P$.",
         "CFSE calculation: $t_{2g}$ electrons stabilize by $-0.4\\Delta_o$; $e_g$ electrons destabilize by $+0.6\\Delta_o$."),

        # 15. Coordination Compounds - Isomerism Count (Match List)
        ("Coordination Compounds", "Geometrical Optical and Linkage Isomer Counts", "Match List",
         "Match List-I with List-II for coordination complexes and the total number of stereoisomers (geometrical + optical) they can exhibit:\n\n"
         "| List-I (Coordination Complex) | List-II (Number of Stereoisomers) |\n"
         "| :--- | :--- |\n"
         "| **A.** $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$ (Square planar) | **I.** $2$ (cis and trans, none optically active) |\n"
         "| **B.** $[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$ (Octahedral) | **II.** $3$ (trans is inactive, cis has d- and l-forms) |\n"
         "| **C.** $[\\text{Co}(\\text{en})_3]^{3+}$ (Octahedral) | **III.** $2$ (d- and l-enantiomers) |\n"
         "| **D.** $[\\text{Co}(\\text{NH}_3)_3(\\text{NO}_2)_3]$ | **IV.** $2$ (fac- and mer-isomers) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$ is $Ma_2 b_2$ square planar: 2 geometrical isomers (cis and trans); square planar complexes have a plane of symmetry so optical activity is zero $\\to$ I.\n2. $[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$ is $M(AA)_2 b_2$: trans-isomer is optically inactive (has inversion center); cis-isomer lacks symmetry and exists as a pair of enantiomers ($d$ and $l$). Total stereoisomers $= 1 + 2 = 3 \\to$ II.\n3. $[\\text{Co}(\\text{en})_3]^{3+}$ is $M(AA)_3$: has no geometrical isomers, but exists as a pair of non-superimposable mirror images ($d$ and $l$) $\\to$ III.\n4. $[\\text{Co}(\\text{NH}_3)_3(\\text{NO}_2)_3]$ is $Ma_3 b_3$: forms facial (fac) and meridional (mer) geometrical isomers $\\to$ IV.",
         "Counting cis and trans as only 2 isomers for $[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$ forgets that cis is chiral and resolves into enantiomers.",
         "In $[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$, the trans isomer has a center of inversion (inactive), while the cis isomer is chiral (2 enantiomers)."),

        # 16. Coordination Compounds - Colour and d-d Transition (Statement I & II)
        ("Coordination Compounds", "Crystal Field Colour and Electronic Transition Conditions", "Statement I & II",
         "Given below are two statements:\n\n"
         "Statement I: An aqueous solution of $[\\text{Ti}(\\text{H}_2\\text{O})_6]^{3+}$ is violet, but it turns colourless upon heating.\n\n"
         "Statement II: On heating, the water ligands are expelled, destroying the octahedral crystal field splitting $\\Delta_o$; in the absence of a ligand field, $d-d$ transitions cannot occur.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. $[\\text{Ti}(\\text{H}_2\\text{O})_6]^{3+}$ has $Ti^{3+}$ ($3d^1$). Light absorption excites the single electron from $t_{2g}$ to $e_g$, absorbing yellow-green light and transmitting complementary violet light. When heated, hydrated water molecules are driven off, making the complex anhydrous $\\text{TiCl}_3$, which is colourless. Statement I is correct.\n2. The colour of coordination complexes originates from $d-d$ electronic transitions. In the absence of ligands, the five $d$-orbitals remain degenerate, so no $d-d$ splitting exists and no visible transition can occur. Statement II is correct and explains Statement I.",
         "Complexes with $d^0$ (like $Sc^{3+}, Ti^{4+}$) or $d^{10}$ (like $Zn^{2+}, Cu^+$) are colourless due to absence of possible $d-d$ transitions.",
         "Ligand field is essential for $d$-orbital splitting; uncomplexed ions with degenerate $d$-orbitals cannot show $d-d$ transition colours."),

        # 17. d-Block - E° Anomaly of Copper (Assertion & Reason)
        ("d- and f-Block Elements", "Positive Standard Electrode Potential of Cu2+/Cu Couple", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "Assertion (A): Copper is the only transition metal of the $3d$-series with a positive standard reduction potential ($E^\\circ_{\\text{Cu}^{2+}/\\text{Cu}} = +0.34\\text{ V}$), and it does not liberate $\\text{H}_2$ gas from dilute mineral acids.\n"
         "Reason (R): The high sum of enthalpy of atomization and ionization enthalpies ($\\Delta_a H^\\circ + \\Delta_i H_1^\\circ + \\Delta_i H_2^\\circ$) of copper is not compensated by its hydration enthalpy ($\\Delta_{\\text{hyd}} H^\\circ$).\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. All $3d$ metals from $\\text{Sc}$ to $\\text{Zn}$ have negative $E^\\circ(M^{2+}/M)$ except copper ($E^\\circ = +0.34\\text{ V}$). Copper cannot reduce $H^+$ to $H_2$ in dilute non-oxidizing acids ($\\text{HCl}, \\text{dil. }\\text{H}_2\\text{SO}_4$). Assertion is TRUE.\n2. The transformation $\\text{Cu}(s) \\to \\text{Cu}^{2+}(aq) + 2e^-$ involves:\n   Sublimation: $\\text{Cu}(s) \\to \\text{Cu}(g)$ ($\\Delta_a H^\\circ > 0$, very high),\n   Ionization: $\\text{Cu}(g) \\to \\text{Cu}^{2+}(g) + 2e^-$ ($\\Delta_i H_1 + \\Delta_i H_2 > 0$),\n   Hydration: $\\text{Cu}^{2+}(g) \\to \\text{Cu}^{2+}(aq)$ ($\\Delta_{\\text{hyd}} H < 0$).\n   Because copper has a very high enthalpy of atomization and high second ionization enthalpy, the hydration energy cannot balance this energy deficit, making $\\Delta G^\\circ > 0$ and $E^\\circ > 0$. Reason is TRUE and explains Assertion.",
         "Nitric acid oxidizes copper not by hydrogen displacement, but because nitrate acts as a strong oxidizing agent.",
         "Copper\'s positive $E^\\circ$ is due to high enthalpy of atomization and ionization not compensated by hydration enthalpy."),

        # 18. d-Block - KMnO4 Redox Titration
        ("d- and f-Block Elements", "Potassium Permanganate Oxidation in Acidic vs Neutral Medium", "Direct MCQ",
         "The number of moles of potassium permanganate ($\\text{KMnO}_4$) required to completely oxidize $1\\text{ mole}$ of ferrous oxalate ($\\text{FeC}_2\\text{O}_4$) in acidic aqueous medium is:",
         ["$0.6\\text{ moles}$ ($3/5$)", "$0.4\\text{ moles}$ ($2/5$)", "$1.0\\text{ mole}$", "$0.2\\text{ moles}$ ($1/5$)"], 0,
         "1. In acidic medium, permanganate is reduced: $\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}$ (change in oxidation state $= +7 \\to +2$, so $n$-factor of $\\text{KMnO}_4 = 5$).\n2. In ferrous oxalate ($\\text{FeC}_2\\text{O}_4$):\n   $\\text{Fe}^{2+} \\to \\text{Fe}^{3+} + 1e^-$ (1 electron lost),\n   $\\text{C}_2\\text{O}_4^{2-} \\to 2\\text{CO}_2 + 2e^-$ (2 electrons lost).\n3. Total electrons lost per molecule of $\\text{FeC}_2\\text{O}_4 = 1 + 2 = 3e^-$ ($n$-factor of $\\text{FeC}_2\\text{O}_4 = 3$).\n4. Equating equivalents: $n_{\\text{KMnO}_4} \\times 5 = n_{\\text{FeC}_2\\text{O}_4} \\times 3 = 1 \\times 3 = 3$.\n5. $n_{\\text{KMnO}_4} = \\frac{3}{5} = 0.6\\text{ moles}$.",
         "Considering only oxalate oxidation gives 2/5 (0.4 mol); considering only iron gives 1/5 (0.2 mol). BOTH parts oxidize!",
         "Both $\\text{Fe}^{2+}$ and $\\text{C}_2\\text{O}_4^{2-}$ are oxidized by $\\text{KMnO}_4$, giving total $n$-factor $= 1 + 2 = 3$."),

        # 19. p-Block - Oxoacids of Phosphorus
        ("p-Block Elements", "Reducing Property and Basicity of Phosphorus Oxoacids", "Direct MCQ",
         "Hypophosphorous acid ($\\text{H}_3\\text{PO}_2$) is a very strong reducing agent capable of reducing $\\text{AgNO}_3$ to metallic silver. The basicity of $\\text{H}_3\\text{PO}_2$ and the number of $P-H$ bonds in its molecule are respectively:",
         ["Basicity $= 1$, number of $P-H$ bonds $= 2$",
          "Basicity $= 3$, number of $P-H$ bonds $= 0$",
          "Basicity $= 2$, number of $P-H$ bonds $= 1$",
          "Basicity $= 1$, number of $P-H$ bonds $= 1$"], 0,
         "1. Structure of $\\text{H}_3\\text{PO}_2$: Phosphorus is bonded to one $=O$, one $-OH$ group, and two $-H$ atoms directly ($P-H$ bonds).\n2. Only the hydrogen atom bonded to oxygen ($-OH$) is ionizable as $H^+$. Therefore, basicity $= 1$ (monobasic acid).\n3. The two hydrogen atoms bonded directly to phosphorus ($P-H$ bonds) are non-ionizable and impart powerful reducing character to the acid.\n4. Hence: Basicity $= 1$, $P-H$ bonds $= 2$.",
         "Assuming all 3 hydrogen atoms are ionizable gives basicity 3, which is incorrect.",
         "Reducing power of phosphorus oxoacids is directly proportional to number of $P-H$ bonds ($\\text{H}_3\\text{PO}_2 > \\text{H}_3\\text{PO}_3 > \\text{H}_3\\text{PO}_4$)."),

        # 20. Salt Analysis - Cation Confirmation Tests (Statement I & II)
        ("Practical Chemistry and Qualitative Salt Analysis", "Prussian Blue and Turnbull Blue Complex Formations", "Statement I & II",
         "Given below are two statements:\n\n"
         "Statement I: Ferric ion ($\\text{Fe}^{3+}$) produces an intense Prussian blue precipitate with potassium ferrocyanide, $\\text{K}_4[\\text{Fe}(\\text{CN})_6]$.\n\n"
         "Statement II: Ferrous ion ($\\text{Fe}^{2+}$) produces an identical blue precipitate (Turnbull\'s blue) with potassium ferricyanide, $\\text{K}_3[\\text{Fe}(\\text{CN})_6]$, and both compounds are chemically identical to $\\text{Fe}_4[\\text{Fe}(\\text{CN})_6]_3 \\cdot x\\text{H}_2\\text{O}$.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Reaction: $4\\text{Fe}^{3+} + 3[\\text{Fe}(\\text{CN})_6]^{4-} \\to \\text{Fe}_4[\\text{Fe}(\\text{CN})_6]_3$ (Prussian blue). Statement I is correct.\n2. For ferrous: $3\\text{Fe}^{2+} + 2[\\text{Fe}(\\text{CN})_6]^{3-} \\to \\text{Fe}_3[\\text{Fe}(\\text{CN})_6]_2$. Electronic charge-transfer between iron centers makes Prussian blue and Turnbull\'s blue chemically equivalent: iron(III) hexacyanoferrate(II). Statement II is correct.",
         "Confusing potassium ferrocyanide with ferricyanide reagents.",
         "Prussian blue and Turnbull\'s blue are structurally identical charge-transfer complexes: $\\text{Fe}_4[\\text{Fe}(\\text{CN})_6]_3$."),

        # 21. Salt Analysis - Anion Identification (Match List)
        ("Practical Chemistry and Qualitative Salt Analysis", "Confirmatory Tests for Inorganic Acid Radicals", "Match List",
         "Match List-I with List-II for confirmatory chemical tests of inorganic anions:\n\n"
         "| List-I (Anion Under Test) | List-II (Observation in Confirmatory Test) |\n"
         "| :--- | :--- |\n"
         "| **A.** Chloride ($\\text{Cl}^-$) | **I.** Reddish-brown vapours of chromyl chloride ($\\text{CrO}_2\\text{Cl}_2$) |\n"
         "| **B.** Nitrate ($\\text{NO}_3^-$) | **II.** Brown ring at junction due to $[\\text{Fe}(\\text{H}_2\\text{O})_5(\\text{NO})]^{2+}$ |\n"
         "| **C.** Sulphide ($\\text{S}^{2-}$) | **III.** Purple/violet coloration with sodium nitroprusside |\n"
         "| **D.** Sulphate ($\\text{SO}_4^{2-}$) | **IV.** White precipitate of $\\text{BaSO}_4$ insoluble in concentrated $\\text{HCl}$ |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Chloride heated with $\\text{K}_2\\text{Cr}_2\\text{O}_7$ and conc. $\\text{H}_2\\text{SO}_4$ yields deep red chromyl chloride vapours $\\to$ I.\n2. Nitrate gives brown ring test: $[\\text{Fe}(\\text{H}_2\\text{O})_5(\\text{NO})]^{2+}$ where iron has $+1$ oxidation state and $\\text{NO}$ is $+1$ $\\to$ II.\n3. Sulphide with sodium nitroprusside gives violet complex $[\\text{Fe}(\\text{CN})_5(\\text{NOS})]^{4-} \\to$ III.\n4. Sulphate forms insoluble barium sulphate precipitate $\\to$ IV.",
         "Distractors swap chromyl chloride test with brown ring test.",
         "Chromyl chloride test is specific to ionic chlorides; covalent halides like $\\text{HgCl}_2$ do not respond!"),

        # 22. GOC - Carbocation Rearrangement & Ring Expansion
        ("General Organic Chemistry", "Carbocation Ring Expansion and Major Product", "Direct MCQ",
         "When cyclobutylmethanol is treated with concentrated hydrochloric acid ($1\\text{ M }\\text{HCl}$), the major organic product obtained is:",
         ["1-Chlorocyclopentane", "1-Chloro-1-cyclobutylmethane", "1-Chloro-2-methylcyclobutane", "Cyclopentene"], 0,
         "1. Protonation of $-OH$ on cyclobutylmethanol gives $-OH_2^+$, which departs as a leaving group forming primary carbocation: $\\text{Cyclobutyl}-\\text{CH}_2^+$.\n2. Four-membered cyclobutane ring has severe angle strain ($90^\\circ$ vs tetrahedral $109.5^\\circ$).\n3. The adjacent $C-C$ ring bond migrates to the exocyclic $\\text{CH}_2^+$, causing ring expansion into a five-membered cyclopentyl secondary carbocation.\n4. This cyclopentyl carbocation is thermodynamically much more stable due to relieved ring strain.\n5. Chloride ion ($\\text{Cl}^-$) attacks the cyclopentyl cation, yielding 1-chlorocyclopentane as the exclusive major product.",
         "Direct attack without rearrangement gives (chloromethyl)cyclobutane, ignoring ring strain relief.",
         "Four-membered and five-membered rings adjacent to carbocations undergo spontaneous ring expansion to relieve angle strain."),

        # 23. GOC - Basicity of Amines in Aqueous Phase
        ("Organic Compounds Containing Nitrogen", "Basicity Order of Alkylamines in Aqueous Medium", "Direct MCQ",
         "The correct order of basic strength of methyl-substituted amines and ammonia in aqueous solution is:",
         ["$(\\text{CH}_3)_2\\text{NH} > \\text{CH}_3\\text{NH}_2 > (\\text{CH}_3)_3\\text{N} > \\text{NH}_3$",
          "$(\\text{CH}_3)_3\\text{N} > (\\text{CH}_3)_2\\text{NH} > \\text{CH}_3\\text{NH}_2 > \\text{NH}_3$",
          "$(\\text{CH}_3)_2\\text{NH} > (\\text{CH}_3)_3\\text{N} > \\text{CH}_3\\text{NH}_2 > \\text{NH}_3$",
          "\\text{CH}_3\\text{NH}_2 > (\\text{CH}_3)_2\\text{NH} > (\\text{CH}_3)_3\\text{N} > \\text{NH}_3$"], 0,
         "1. In gas phase, basicity follows purely inductive $+I$ effect: $3^\\circ > 2^\\circ > 1^\\circ > \\text{NH}_3$.\n2. In aqueous medium, basicity is governed by three competing factors: inductive effect ($+I$), hydration stabilization of ammonium cation via H-bonding, and steric hindrance.\n3. For methyl group (smaller size): inductive and hydration effects combine to give maximum stability to $2^\\circ$, followed by $1^\\circ$, and then $3^\\circ$ (where steric hindrance suppresses hydration).\n4. Order for methyl: $2^\\circ > 1^\\circ > 3^\\circ > \\text{NH}_3$ (i.e. $(\\text{CH}_3)_2\\text{NH} > \\text{CH}_3\\text{NH}_2 > (\\text{CH}_3)_3\\text{N} > \\text{NH}_3$).\n5. Note: for ethyl groups, steric relief makes $2^\\circ > 3^\\circ > 1^\\circ > \\text{NH}_3$.",
         "Assuming the 213 order applies to ethyl or 231 to methyl is the most common confusion in NEET.",
         "Aqueous amine basicity: Methyl follows 2 > 1 > 3; Ethyl follows 2 > 3 > 1."),

        # 24. GOC - Aromaticity Hückel's Rule (Multi-Statement)
        ("General Organic Chemistry", "Aromaticity Non-Aromaticity and Anti-Aromaticity", "Multi-Statement",
         "Consider the following cyclic species: (I) Cyclooctatetraene, (II) Cyclopentadienyl anion, (III) Cycloheptatrienyl cation (Tropylium ion), and (IV) Cyclopropenyl cation:\n\n"
         "A. Cyclopentadienyl anion contains $6\\pi$ electrons in a planar conjugated ring and is aromatic.\n"
         "B. Tropylium ion contains $6\\pi$ electrons delocalized over 7 carbon atoms and is aromatic.\n"
         "C. Cyclooctatetraene adopts a non-planar tub-shaped conformation to avoid anti-aromaticity, making it non-aromatic.\n"
         "D. Cyclopropenyl cation has $4\\pi$ electrons and is anti-aromatic.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and C only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. Cyclopentadienyl anion has 2 double bonds ($4\\pi$) + 1 carbanion lone pair ($2\\pi$) $= 6\\pi$ electrons ($4n+2, n=1$). Planar and aromatic. Statement A is TRUE.\n2. Tropylium ion has 3 double bonds $= 6\\pi$ electrons ($4n+2, n=1$). Planar, aromatic, exceptionally stable. Statement B is TRUE.\n3. Cyclooctatetraene has $8\\pi$ electrons. If planar, it would be anti-aromatic ($4n$). It puckers into a tub conformation, breaking planarity and conjugation, rendering it non-aromatic. Statement C is TRUE.\n4. Cyclopropenyl cation has 1 double bond $= 2\\pi$ electrons ($4n+2$ with $n=0$). It is aromatic, NOT anti-aromatic. Statement D is FALSE.",
         "Cyclopropenyl cation has $2\\pi$ electrons ($4n+2$ where $n=0$), which makes it the smallest aromatic ring system!",
         "Hückel\'s rule: $(4n+2)\\pi$ electrons in planar conjugated ring $\\implies$ aromatic; $4n\\pi$ in planar ring $\\implies$ anti-aromatic."),

        # 25. Hydrocarbons - Ozonolysis Structure Elucidation
        ("Hydrocarbons", "Reductive Ozonolysis Identification of Alkene Structure", "Direct MCQ",
         "An alkene $X$ on reductive ozonolysis with $\\text{O}_3 / \\text{Zn}-\\text{H}_2\\text{O}$ gives an equimolar mixture of acetone ($\\text{CH}_3\\text{COCH}_3$) and glyoxal ($\\text{OHC}-\\text{CHO}$). The IUPAC name of alkene $X$ is:",
         ["2,5-Dimethylhexa-2,4-diene", "2-Methylpenta-2,4-diene", "2,3-Dimethylbuta-1,3-diene", "Hexa-1,5-diene"], 0,
         "1. Ozonolysis cleaves $C=C$ double bonds and replaces each with $=O$.\n2. Products: 2 molecules of acetone ($\\text{CH}_3-\\text{C}(\\text{CH}_3)=\\text{O}$) and 1 molecule of glyoxal ($\\text{O}=\\text{CH}-\\text{CH}=\\text{O}$).\n3. Reconstructing the reactant by removing oxygens and forming double bonds:\n   $$(\\text{CH}_3)_2\\text{C}=\\text{CH}-\\text{CH}=\\text{C}(\\text{CH}_3)_2$$.\n4. Numbering the 6-carbon chain: $1, 2, 3, 4, 5, 6$. Double bonds are at $C_2$ and $C_4$; methyl substituents are at $C_2$ and $C_5$.\n5. IUPAC name: 2,5-Dimethylhexa-2,4-diene.",
         "2-Methylpenta-2,4-diene would yield acetaldehyde rather than a second acetone molecule.",
         "To deduce original alkene from ozonolysis products, align carbonyl groups face-to-face and remove oxygen atoms."),

        # 26. Haloalkanes - SN1 vs SN2 Stereochemistry (Statement I & II)
        ("Haloalkanes and Haloarenes", "Stereochemical Traps in SN1 vs SN2 Reactions", "Statement I & II",
         "Given below are two statements regarding nucleophilic substitution reactions:\n\n"
         "Statement I: An $S_N2$ reaction at a chiral carbon center proceeds with complete stereochemical inversion of configuration (Walden inversion).\n\n"
         "Statement II: An $S_N1$ reaction at an optically active chiral alkyl halide generally gives complete $50:50$ racemization with zero optical rotation.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Statement I is correct but Statement II is incorrect",
          "Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. In $S_N2$, nucleophile attacks strictly from backside opposite to the leaving group, causing $100%$ inversion of configuration (Walden inversion). Statement I is correct.\n2. In $S_N1$, departure of leaving group forms a planar carbocation. However, the departing leaving group shields the front face for a brief moment (intimate ion pair). As a result, backside attack is slightly favoured over frontside attack, leading to partial racemization with a net excess of inversion (rarely exactly 50:50). Statement II is incorrect.",
         "Textbooks state SN1 gives racemization, but at advanced NEET level, NCERT specifically notes net excess of inversion occurs.",
         "$S_N2$ gives 100% inversion; $S_N1$ produces racemization accompanied by net inversion due to ion-pair shielding."),

        # 27. Haloalkanes - Elimination Regiochemistry
        ("Haloalkanes and Haloarenes", "Saytzeff vs Hofmann Elimination with Steric Bases", "Direct MCQ",
         "When 2-bromo-2-methylbutane is treated with potassium tert-butoxide (($\\text{CH}_3)_3\\text{CO}^- \\text{K}^+$) in tert-butanol, the major elimination product is:",
         ["2-Methylbut-1-ene (Hofmann product)",
          "2-Methylbut-2-ene (Saytzeff product)",
          "2-Methylbutan-2-ol",
          "3-Methylbut-1-ene"], 0,
         "1. 2-Bromo-2-methylbutane has two types of $\\beta$-hydrogens:\n   $C_1$ has 3 primary hydrogens (less hindered, on methyl),\n   $C_3$ has 2 secondary hydrogens (more hindered, on methylene).\n2. Potassium tert-butoxide is an exceptionally bulky, sterically hindered strong base.\n3. Because of its large steric bulk, it cannot easily access the hindered internal $C_3$ secondary hydrogens.\n4. It selectively abstracts the readily accessible, unhindered primary hydrogen from the terminal $C_1$ methyl group.\n5. This yields the less substituted, less stable terminal alkene: 2-Methylbut-1-ene (Hofmann product) as the major product ($>70%$).",
         "Using standard small base like $KOH$ yields 2-Methylbut-2-ene (Saytzeff product).",
         "Bulky bases (t-BuOK) selectively produce Hofmann (least substituted) elimination products."),

        # 28. Alcohols - Lucas Test Kinetics
        ("Alcohols, Phenols and Ethers", "Lucas Reagent Turbidity and Reaction Mechanism", "Direct MCQ",
         "An unknown organic liquid of molecular formula $\\text{C}_4\\text{H}_{10}\\text{O}$ gives immediate cloudiness (turbidity) at room temperature upon addition of Lucas reagent ($\\text{anhydrous ZnCl}_2 + \\text{conc. HCl}$). The structure of the compound is:",
         ["2-Methylpropan-2-ol (tert-butyl alcohol)",
          "Butan-1-ol",
          "Butan-2-ol",
          "2-Methylpropan-1-ol"], 0,
         "1. Lucas reagent test works by conversion of alcohol into insoluble alkyl chloride: $\\text{R-OH} + \\text{HCl} \\xrightarrow{\\text{ZnCl}_2} \\text{R-Cl}\\downarrow + \\text{H}_2\\text{O}$.\n2. The reaction proceeds via a carbocation intermediate ($S_N1$).\n3. Turbidity rate depends on carbocation stability:\n   $3^\\circ$ alcohol $\\to 3^\\circ$ carbocation (most stable) $\\implies$ Immediate turbidity (within seconds),\n   $2^\\circ$ alcohol $\\to 2^\\circ$ carbocation $\\implies$ Turbidity appears in $5\\text{ minutes}$,\n   $1^\\circ$ alcohol $\\to 1^\\circ$ carbocation $\\implies$ No turbidity at room temperature without heating.\n4. Immediate turbidity confirms a tertiary alcohol: 2-Methylpropan-2-ol.",
         "Butan-2-ol is a secondary alcohol and takes 5 minutes to show turbidity.",
         "Lucas test turbidity: Tertiary = Immediate; Secondary = 5 minutes; Primary = Only on heating."),

        # 29. Phenols - Reimer-Tiemann Electrophile (Assertion & Reason)
        ("Alcohols, Phenols and Ethers", "Dichlorocarbene Intermediates in Reimer-Tiemann Reaction", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "Assertion (A): In the Reimer-Tiemann reaction of phenol with chloroform and aqueous $\\text{NaOH}$, the active electrophilic species attacking the phenoxide ring is dichlorocarbene ($:\\text{CCl}_2$).\n"
         "Reason (R): Dichlorocarbene has a sextet of electrons around carbon, rendering it an electron-deficient neutral electrophile.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Chloroform reacts with base: $\\text{CHCl}_3 + \\text{OH}^- \\rightleftharpoons :\\text{CCl}_3^- + \\text{H}_2\\text{O} \\to :\\text{CCl}_2 + \\text{Cl}^-$. The active intermediate is dichlorocarbene ($:\\text{CCl}_2$). Assertion is TRUE.\n2. Dichlorocarbene has two single covalent $C-Cl$ bonds (4 electrons) and one lone pair (2 electrons), giving total 6 valence electrons (an incomplete octet). Hence it acts as a powerful neutral electrophile attacking electron-rich ortho-phenoxide position. Reason is TRUE and explains Assertion.",
         "Assuming the attacking electrophile is $CHCl_2^+$ or carbonium ion is a common error.",
         "Dichlorocarbene ($:\\text{CCl}_2$) is an electron-deficient carbene with a sextet of valence electrons."),

        # 30. Ethers - HI Cleavage Regiochemistry
        ("Alcohols, Phenols and Ethers", "Cleavage of Unsymmetrical Ethers with Hydrogen Iodide", "Direct MCQ",
         "When tert-butyl methyl ether is heated with excess concentrated hydroiodic acid ($\\text{HI}$), the major products formed are:",
         ["tert-Butyl iodide and Methanol",
          "tert-Butyl alcohol and Methyl iodide",
          "Isobutylene and Methyl iodide",
          "tert-Butyl iodide and Methyl iodide"], 0,
         "1. Ether oxygen gets protonated: $(\\text{CH}_3)_3\\text{C}-\\text{O}^+(\\text{H})-\\text{CH}_3$.\n2. Since one group is tertiary ($tert$-butyl), the reaction proceeds via an $S_N1$ pathway rather than $S_N2$.\n3. Cleavage of the $C-O$ bond generates the highly stable $3^\\circ$ carbocation: $(\\text{CH}_3)_3\\text{C}^+$, while leaving methanol ($\\text{CH}_3\\text{OH}$) as neutral departing group.\n4. The iodide ion ($\\text{I}^-$) attacks the $tert$-butyl carbocation, yielding $tert$-butyl iodide.\n5. Thus, the cleavage products are $tert$-butyl iodide and methanol (which with cold/stoichiometric HI does not convert further, or gives both iodides with hot excess HI; standard textbook question tests initial cleavage selectivity).",
         "Primary/secondary ethers follow SN2 (iodide attacks smaller alkyl group); tertiary ethers follow SN1 (iodide goes to tertiary carbon).",
         "Tertiary ethers cleave via $S_N1$ mechanism with iodide attaching to the tertiary carbon."),

        # 31. Aldehydes & Ketones - Crossed Cannizzaro Reaction
        ("Aldehydes, Ketones and Carboxylic Acids", "Crossed Cannizzaro Reaction with Formaldehyde", "Direct MCQ",
         "When an equimolar mixture of benzaldehyde ($\\text{C}_6\\text{H}_5\\text{CHO}$) and formaldehyde ($\\text{HCHO}$) is heated with concentrated $\\text{NaOH}$ solution (Crossed Cannizzaro reaction), the products obtained are:",
         ["Sodium formate and Benzyl alcohol",
          "Sodium benzoate and Methanol",
          "Benzyl alcohol and Methanol",
          "Sodium benzoate and Sodium formate"], 0,
         "1. Crossed Cannizzaro reaction occurs between two different aldehydes neither having $\\alpha$-hydrogens.\n2. Formaldehyde ($\\text{HCHO}$) has no electron-donating alkyl/aryl groups and is far less sterically hindered than benzaldehyde.\n3. Consequently, nucleophilic attack of hydroxide ion ($\\text{OH}^-$) occurs much faster at the carbonyl carbon of formaldehyde.\n4. Formaldehyde forms the dianion intermediate and transfers hydride ($\\text{H}^-$) to the less reactive benzaldehyde.\n5. Formaldehyde is oxidized to sodium formate ($\\text{HCOONa}$), and benzaldehyde is reduced to benzyl alcohol ($\\text{C}_6\\text{H}_5\\text{CH}_2\\text{OH}$).",
         "Sodium benzoate and methanol is the exact reverse of the true reaction selectivity.",
         "In crossed Cannizzaro with formaldehyde, formaldehyde is ALWAYS oxidized to formate."),

        # 32. Aldehydes & Ketones - Semicarbazide Reaction Site
        ("Aldehydes, Ketones and Carboxylic Acids", "Nucleophilic Addition of Semicarbazide Regioselectivity", "Direct MCQ",
         "Semicarbazide ($\\text{H}_2\\text{N}-\\text{CO}-\\text{NH}-\\text{NH}_2$) reacts with aldehydes and ketones through only one of its two amino groups. The non-reactive amino group is inactive because:",
         ["Its lone pair of electrons is delocalized into the carbonyl group by resonance",
          "It is sterically hindered by the adjacent carbonyl oxygen",
          "It is protonated by acid catalyst forming an ammonium ion",
          "It undergoes rapid tautomerization into an enol form"], 0,
         "1. Structure of semicarbazide: $\\text{H}_2\\text{N}_{(a)}-\\text{C}(=\\text{O})-\\text{NH}-\\text{NH}_{2(b)}$.\n2. The nitrogen $(a)$ is an amide nitrogen attached directly to the carbonyl group: $\\text{H}_2\\text{N}-\\text{C}(=\\text{O})- \\leftrightarrow \\text{H}_2\\text{N}^+=\\text{C}(\\text{O}^-)-$.\n3. Resonance delocalization into the carbonyl group drastically reduces electron density on nitrogen $(a)$, making it non-nucleophilic.\n4. The hydrazine terminal nitrogen $(b)$ is not conjugated with the carbonyl group; its lone pair remains fully localized and available for nucleophilic attack.\n5. Only the hydrazine terminal $-\\text{NH}_2$ participates in semicarbazone formation.",
         "Steric hindrance is minor; resonance conjugation is the fundamental electronic cause.",
         "Only the hydrazine terminal $-\\text{NH}_2$ of semicarbazide acts as nucleophile; amide $-\\text{NH}_2$ is resonance-deactivated."),

        # 33. Carboxylic Acids - Acidic Strength Ortho Effect (Statement I & II)
        ("Aldehydes, Ketones and Carboxylic Acids", "Ortho Effect on Acidic Strength of Benzoic Acid", "Statement I & II",
         "Given below are two statements regarding substituted benzoic acids:\n\n"
         "Statement I: Ortho-toluic acid (2-methylbenzoic acid) is a stronger acid than benzoic acid, even though the methyl group is an electron-donating ($+I$ and hyperconjugative) group.\n\n"
         "Statement II: Ortho-substituents cause steric inhibition of resonance (ortho-effect), twisting the carboxyl group ($-COOH$) out of the benzene ring plane, which prevents resonance destabilization of the carboxylate anion by the aromatic ring.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Ortho-substituted benzoic acids are stronger than benzoic acid, almost irrespective of the electronic nature of the substituent ($+I$ or $-I$). Ortho-toluic acid has $pK_a = 3.91$ compared to benzoic acid $pK_a = 4.20$. Statement I is correct.\n2. Bulky ortho substituents force the $-COOH$ group to twist perpendicular to the benzene ring. In this non-planar geometry, the benzene ring cannot donate electrons into the carboxyl group. The carboxylate anion can delocalize its negative charge symmetrically over its two oxygen atoms without ring interference, dramatically increasing stability and acidity. Statement II is correct and explains Statement I.",
         "Assuming electron-donating groups always decrease acidity overlooks the steric ortho-effect.",
         "Ortho-effect: steric twisting removes ring conjugation, making ortho-substituted benzoic acids stronger acids."),

        # 34. Amines - Gabriel Phthalimide Synthesis (Assertion & Reason)
        ("Organic Compounds Containing Nitrogen", "Gabriel Phthalimide Inability to Synthesize Aniline", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "Assertion (A): Aniline cannot be prepared by Gabriel phthalimide synthesis.\n"
         "Reason (R): Aryl halides do not undergo nucleophilic aromatic substitution ($S_N2$) with potassium phthalimide under ordinary conditions due to partial double bond character of the $C-\\text{halogen}$ bond.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Gabriel phthalimide synthesis is exclusively used for preparing aliphatic primary amines. Aniline (aromatic primary amine) cannot be synthesized by this method. Assertion is TRUE.\n2. The key step involves nucleophilic attack of phthalimide anion on an alkyl halide ($S_N2$). Aryl halides have resonance resonance partial double bond character in $C-\\text{Cl}$ / $C-\\text{Br}$, $sp^2$ hybridized carbon, and electrostatic repulsion from benzene $\\pi$-cloud, making them completely unreactive towards nucleophilic substitution with phthalimide anion. Reason is TRUE and explains Assertion.",
         "Students often confuse phthalimide synthesis with Hoffmann bromamide degradation (which CAN prepare aniline).",
         "Gabriel phthalimide cannot produce aromatic amines because aryl halides do not undergo $S_N2$ displacement."),

        # 35. Amines - Diazonium Salt Coupling (Match List)
        ("Organic Compounds Containing Nitrogen", "Diazonium Salt Azo Coupling pH Conditions and Dyes", "Match List",
         "Match List-I with List-II for diazonium coupling reactions and their optimal reaction conditions:\n\n"
         "| List-I (Coupling Partner) | List-II (Optimal pH and Product Dye) |\n"
         "| :--- | :--- |\n"
         "| **A.** Phenol | **I.** Mildly alkaline medium ($pH = 9-10$), Orange dye |\n"
         "| **B.** Aniline | **II.** Mildly acidic medium ($pH = 4-5$), Yellow dye |\n"
         "| **C.** $\\beta$-Naphthol | **I.** Alkaline medium, Scarlet red dye |\n"
         "| **D.** Fluoroboric acid ($\\text{HBF}_4$) heating | **IV.** Balz-Schiemann reaction yielding fluorobenzene |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Phenol coupling requires mildly alkaline pH (9-10) to convert phenol into more reactive phenoxide ion, yielding $p$-hydroxyazobenzene (orange dye) $\\to$ I.\n2. Aniline coupling requires mildly acidic pH (4-5) to prevent protonation of aniline while maintaining uncomplexed amine nucleophile, yielding $p$-aminoazobenzene (yellow dye) $\\to$ II.\n3. $\\beta$-naphthol in alkaline medium yields an intense red azo dye $\\to$ III.\n4. Decomposition of diazonium fluoroborate to fluorobenzene is Balz-Schiemann reaction $\\to$ IV.",
         "Strongly acidic pH protonates aniline into non-nucleophilic anilinium ion; strongly basic pH converts diazonium into inactive diazotate.",
         "Diazonium coupling: Phenol needs basic pH (9-10); Aniline needs mildly acidic pH (4-5)."),

        # 36. Biomolecules - Glucose Anomers and Mutarotation (Multi-Statement)
        ("Biomolecules", "Glucose Cyclic Hemiacetal Anomers and Mutarotation", "Multi-Statement",
         "Consider the structural characteristics of D-glucose:\n\n"
         "A. $\\alpha$-D-glucopyranose and $\\beta$-D-glucopyranose are anomers differing in configuration only at $C_1$.\n"
         "B. The spontaneous change in specific optical rotation of an optically active carbohydrate solution until reaching equilibrium is called mutarotation.\n"
         "C. Glucose pentaacetate does not react with hydroxylamine ($\\text{NH}_2\\text{OH}$), proving the absence of a free $-CHO$ group in the cyclic form.\n"
         "D. $\\beta$-D-glucopyranose is thermodynamically more stable than $\\alpha$-D-glucopyranose because all its non-hydrogen substituents ($-OH$ and $-\\text{CH}_2\\text{OH}$) occupy equatorial positions.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, C, and D", "A, B, and C only", "A and C only", "B and D only"], 0,
         "1. $\\alpha$ and $\\beta$ forms are epimers at the anomeric hemiacetal carbon $C_1$. Statement A is TRUE.\n2. Mutarotation is the equilibrium equilibration between $\\alpha$ ($+112^\\circ$) and $\\beta$ ($+19^\\circ$) forms to $+52.7^\\circ$. Statement B is TRUE.\n3. Glucose pentaacetate locks the hemiacetal ring into an acetal; it cannot open into free aldehyde and thus fails to form an oxime with $\\text{NH}_2\\text{OH}$. Statement C is TRUE.\n4. In $\\beta$-D-glucopyranose, every hydroxyl group and the bulky $-\\text{CH}_2\\text{OH}$ group are in equatorial positions in the chair conformation, minimizing 1,3-diaxial steric strain. Statement D is TRUE.",
         "All four statements are direct NCERT facts regarding glucose chemistry.",
         "$\\beta$-D-glucose is more stable because all bulky groups are equatorial; pentaacetate lacks free $-CHO$."),

        # 37. Biomolecules - Protein Structure and Denaturation (Statement I & II)
        ("Biomolecules", "Protein Denaturation Levels of Structural Disruption", "Statement I & II",
         "Given below are two statements:\n\n"
         "Statement I: Denaturation of proteins causes coagulation, disrupting the secondary and tertiary structures while leaving the primary covalent polypeptide structure intact.\n\n"
         "Statement II: During denaturation, hydrogen bonds and ionic interactions are broken, causing globular proteins to unfold and lose their biological activity.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Denaturation (by heat, acids, heavy metals) does not hydrolyze covalent peptide bonds. The sequence of amino acids (primary structure) remains completely preserved. Statement I is correct.\n2. Non-covalent stabilizing forces (hydrogen bonding, hydrophobic interactions, disulfide bonds, salt bridges) that hold $\\alpha$-helices and $\\beta$-sheets foldings are ruptured, leading to unfolding and loss of native biological function. Statement II is correct and explains Statement I.",
         "Students often think denaturation breaks all bonds; covalent peptide bonds remain unaffected.",
         "Denaturation destroys $2^\\circ$ and $3^\\circ$ protein structures; $1^\\circ$ (primary sequence) remains intact."),

        # 38. Biomolecules - Nucleic Acid Nucleotide Linkages
        ("Biomolecules", "DNA Double Helix Phosphodiester and Glycosidic Bonds", "Direct MCQ",
         "In a double-stranded DNA molecule, adenine constitutes $31%$ of the total nitrogenous bases. According to Chargaff\'s rules, the percentage of cytosine in this DNA sample is:",
         ["$19%$", "$31%$", "$38%$", "$62%$"], 0,
         "1. By Chargaff\'s equivalence rules for double-stranded DNA:\n   $$\\text{Amount of Adenine (A)} = \\text{Amount of Thymine (T)}$$,\n   $$\\text{Amount of Guanine (G)} = \\text{Amount of Cytosine (C)}$$.\n2. Given: $\\text{A} = 31% \\implies \\text{T} = 31%$.\n3. Total percentage of $\\text{A} + \\text{T} = 31 + 31 = 62%$.\n4. Remaining percentage corresponds to $\\text{G} + \\text{C}$:\n   $$\\text{G} + \\text{C} = 100% - 62% = 38%$$.\n5. Since $\\text{G} = \\text{C}$, the percentage of cytosine is:\n   $$\\text{Cytosine} = \\frac{38%}{2} = 19%$$.",
         "38% is the sum of G and C combined; 31% is thymine.",
         "Chargaff\'s rule: $\\text{A} = \\text{T}$ and $\\text{G} = \\text{C}$. Therefore $%\\text{C} = (100 - 2%\\text{A})/2$."),

        # 39. Polymers & Everyday Chemistry - Enzyme Inhibition
        ("Chemistry in Everyday Life and Biomolecules", "Competitive vs Non-Competitive Enzyme Inhibition", "Direct MCQ",
         "In competitive enzyme inhibition, the inhibitor closely resembles the substrate in molecular structure. How do the Michaelis-Menten parameters $K_m$ (Michaelis constant) and $V_{\\max}$ (maximum velocity) change in competitive inhibition?",
         ["$K_m$ increases, $V_{\\max}$ remains unchanged",
          "$K_m$ decreases, $V_{\\max}$ decreases",
          "$K_m$ remains unchanged, $V_{\\max}$ decreases",
          "Both $K_m$ and $V_{\\max}$ decrease"], 0,
         "1. A competitive inhibitor binds reversibly to the active catalytic site of the enzyme, competing directly with the natural substrate.\n2. Because substrate must compete with the inhibitor, a higher substrate concentration is required to achieve half-maximal velocity, meaning apparent $K_m$ increases.\n3. At sufficiently high substrate concentrations, the substrate outcompetes the inhibitor completely, reaching the true maximum velocity $V_{\\max}$. Thus $V_{\\max}$ remains unchanged.\n4. Classic example: Malonate competitively inhibits succinate dehydrogenase because of its structural similarity to succinate.",
         "Non-competitive inhibitors decrease $V_{\\max}$ without altering $K_m$.",
         "Competitive inhibition: $K_m$ increases, $V_{\\max}$ unchanged; overcome by increasing substrate concentration."),

        # 40. Solutions - Raoult's Law Positive vs Negative Deviations
        ("Solutions and Colligative Properties", "Non-Ideal Solutions Azeotropic Mixtures", "Direct MCQ",
         "A mixture of concentrated nitric acid ($68%$) and water ($32%$) forms a maximum boiling azeotrope that boils at $393.5\\text{ K}$. This mixture exhibits:",
         ["Negative deviation from Raoult\'s law with $\\Delta H_{\\text{mix}} < 0$ and $\\Delta V_{\\text{mix}} < 0$",
          "Positive deviation from Raoult\'s law with $\\Delta H_{\\text{mix}} > 0$ and $\\Delta V_{\\text{mix}} > 0$",
          "Ideal behavior with $\\Delta H_{\\text{mix}} = 0$",
          "Positive deviation with minimum boiling azeotrope"], 0,
         "1. Nitric acid and water molecules form strong intermolecular hydrogen bonds with each other: $A-B$ interactions are stronger than $A-A$ and $B-B$ interactions.\n2. Stronger attraction lowers vapor pressure below Raoult\'s law prediction $\\implies$ Negative deviation.\n3. Lower vapor pressure requires a higher temperature to boil $\\implies$ Maximum boiling azeotrope.\n4. Enthalpy and volume changes for negative deviation: $\\Delta H_{\\text{mix}} < 0$ (exothermic) and $\\Delta V_{\\text{mix}} < 0$ (contraction).",
         "Positive deviation forms minimum boiling azeotropes (e.g. ethanol-water).",
         "Negative deviation $\\implies$ lower vapor pressure $\\implies$ maximum boiling azeotrope, $\\Delta H < 0, \\Delta V < 0$."),

        # 41. Environmental Chemistry - Photochemical Smog (Match List)
        ("Environmental Chemistry", "Components of Classical vs Photochemical Smog", "Match List",
         "Match List-I with List-II for atmospheric pollution phenomena and their characteristic chemicals:\n\n"
         "| List-I (Pollution Phenomenon) | List-II (Chemical Characteristic / Component) |\n"
         "| :--- | :--- |\n"
         "| **A.** Photochemical smog | **I.** Peroxyacetyl nitrate (PAN), ozone, acrolein (oxidizing) |\n"
         "| **B.** Classical smog | **II.** Smoke, fog, and sulphur dioxide (reducing smog) |\n"
         "| **C.** Acid rain | **III.** $pH < 5.6$, caused by $\\text{SO}_2$ and $\\text{NO}_2$ emissions |\n"
         "| **D.** Ozone hole catalyst | **IV.** Chlorine free radicals ($\\text{Cl}^\\bullet$) from chlorofluorocarbons |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Photochemical smog is oxidizing, formed by action of sunlight on hydrocarbons and nitrogen oxides, producing PAN and ozone $\\to$ I.\n2. Classical smog occurs in cool humid climates, contains $\\text{SO}_2$ and is reducing in nature $\\to$ II.\n3. Clean rain has $pH \\approx 5.6$ due to dissolved $\\text{CO}_2$; rain with $pH < 5.6$ is acid rain $\\to$ III.\n4. CFC breakdown releases $\\text{Cl}^\\bullet$ free radicals that catalytically destroy ozone $\\to$ IV.",
         "Photochemical smog is oxidizing; classical smog is reducing.",
         "Photochemical smog: PAN + $O_3$ + $NO_2$ (oxidizing); Classical smog: $SO_2$ + smoke (reducing)."),

        # 42. Practical Chemistry - Kjeldahl Nitrogen Estimation
        ("Practical Chemistry and Qualitative Salt Analysis", "Kjeldahl Method Percentage of Nitrogen Formula", "Direct MCQ",
         "During estimation of nitrogen present in an organic compound by Kjeldahl\'s method, the ammonia evolved from $0.5\\text{ g}$ of the compound neutralized $20\\text{ mL}$ of $0.1\\text{ M }\\text{H}_2\\text{SO}_4$. The percentage of nitrogen in the compound is:",
         ["$11.2%$", "$5.6%$", "$22.4%$", "$14.0%$"], 0,
         "1. $0.1\\text{ M }\\text{H}_2\\text{SO}_4$ is dibasic ($n$-factor $= 2$), so its normality is $N = 0.1 \\times 2 = 0.2\\text{ N}$.\n2. Milliequivalents of acid neutralized by ammonia:\n   $$\\text{meq} = N \\times V(\\text{mL}) = 0.2 \\times 20 = 4\\text{ meq}$$.\n3. Formula for Kjeldahl\'s estimation of nitrogen:\n   $$%\\text{N} = \\frac{1.4 \\times N \\times V}{W} = \\frac{1.4 \\times \\text{meq of acid}}{W}$$.\n4. Substituting values: $%\\text{N} = \\frac{1.4 \\times 4}{0.5} = \\frac{5.6}{0.5} = 11.2%$.",
         "Forgetting the basicity of sulfuric acid ($n=2$) gives half the percentage: 5.6%.",
         "Kjeldahl\'s method: $%\\text{N} = \\frac{1.4 \\times N_{\\text{acid}} \\times V_{\\text{acid}}}{W_{\\text{sample}}}$. Use normality, not molarity!"),

        # 43. Organic Synthesis Reagents - DIBAL-H and Lindlar
        ("Hydrocarbons and Carbonyl Compounds", "Selective Reduction by DIBAL-H and Lindlar Catalyst", "Direct MCQ",
         "The reagents $X$ and $Y$ in the following transformations are:\n"
         "1. $\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CN} \\xrightarrow{X} \\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CHO}$\n"
         "2. $\\text{CH}_3-\\text{C}\\equiv\\text{C}-\\text{CH}_3 \\xrightarrow{Y} \\text{cis-but-2-ene}$",
         ["$X = \\text{DIBAL-H}$, $Y = \\text{H}_2 / \\text{Pd-BaSO}_4$ (Lindlar catalyst)",
          "$X = \\text{LiAlH}_4$, $Y = \\text{Na} / \\text{liq. }\\text{NH}_3$",
          "$X = \\text{NaBH}_4$, $Y = \\text{H}_2 / \\text{Pd-BaSO}_4$",
          "$X = \\text{DIBAL-H}$, $Y = \\text{Na} / \\text{liq. }\\text{NH}_3$"], 0,
         "1. $\\text{DIBAL-H}$ (Diisobutylaluminium hydride) at $-78^\\circ\\text{C}$ selectively reduces nitriles and esters to aldehydes without reducing $C=C$ double bonds.\n2. Hydrogenation of alkynes over Lindlar catalyst ($\\text{Pd}/\\text{BaSO}_4$ poisoned with quinoline) performs stereoselective syn-addition yielding cis-alkenes.\n3. Reduction with $\\text{Na}/\\text{liq. }\\text{NH}_3$ (Birch reduction) performs anti-addition yielding trans-alkenes.",
         "LiAlH4 reduces the nitrile all the way to primary amine and can also reduce double bonds conjugated with nitriles.",
         "DIBAL-H selectively yields aldehydes from nitriles/esters; Lindlar catalyst yields cis-alkenes."),

        # 44. Coordination Chemistry - Nickel Complex Hybridizations
        ("Coordination Compounds", "Valence Bond Hybridization and Magnetism of Nickel Complexes", "Direct MCQ",
         "The hybridization and magnetic behavior of $[\\text{Ni}(\\text{CO})_4]$, $[\\text{Ni}(\\text{CN})_4]^{2-}$, and $[\\text{NiCl}_4]^{2-}$ are respectively:",
         ["$[\\text{Ni}(\\text{CO})_4]$: $sp^3$, diamagnetic; $[\\text{Ni}(\\text{CN})_4]^{2-}$: $dsp^2$, diamagnetic; $[\\text{NiCl}_4]^{2-}$: $sp^3$, paramagnetic",
          "$[\\text{Ni}(\\text{CO})_4]$: $dsp^2$, diamagnetic; $[\\text{Ni}(\\text{CN})_4]^{2-}$: $sp^3$, diamagnetic; $[\\text{NiCl}_4]^{2-}$: $sp^3$, paramagnetic",
          "$[\\text{Ni}(\\text{CO})_4]$: $sp^3$, paramagnetic; $[\\text{Ni}(\\text{CN})_4]^{2-}$: $dsp^2$, paramagnetic; $[\\text{NiCl}_4]^{2-}$: $dsp^2$, diamagnetic",
          "$[\\text{Ni}(\\text{CO})_4]$: $sp^3$, diamagnetic; $[\\text{Ni}(\\text{CN})_4]^{2-}$: $sp^3$, diamagnetic; $[\\text{NiCl}_4]^{2-}$: $dsp^2$, paramagnetic"], 0,
         "1. $[\\text{Ni}(\\text{CO})_4]$: $Ni(0)$ is $3d^8 4s^2$. Strong ligand $\\text{CO}$ forces $4s$ electrons into $3d$, pairing all electrons to $3d^{10}$. Empty $4s$ and $4p$ hybridize as $sp^3$ (tetrahedral). Zero unpaired electrons $\\implies$ Diamagnetic.\n2. $[\\text{Ni}(\\text{CN})_4]^{2-}$: $Ni^{2+}$ is $3d^8$. Strong ligand $\\text{CN}^-$ forces pairing into four $3d$ orbitals, leaving one empty $3d$. Hybridization is $dsp^2$ (square planar). Diamagnetic.\n3. $[\\text{NiCl}_4]^{2-}$: $Ni^{2+}$ is $3d^8$. Weak field ligand $\\text{Cl}^-$ cannot pair electrons ($3d^8$ has 2 unpaired electrons). Hybridization uses $4s 4p^3 \\implies sp^3$ (tetrahedral). Paramagnetic ($2$ unpaired electrons).",
         "Assuming $[\\text{Ni}(\\text{CO})_4]$ is $dsp^2$ overlooks that $Ni(0)$ has 10 valence electrons which completely fill the $3d$ subshell.",
         "$[\\text{Ni}(\\text{CO})_4]$ is $sp^3$ diamagnetic; $[\\text{Ni}(\\text{CN})_4]^{2-}$ is $dsp^2$ diamagnetic; $[\\text{NiCl}_4]^{2-}$ is $sp^3$ paramagnetic."),

        # 45. Thermodynamics - Kirchhoff's Enthalpy Variation
        ("Thermodynamics", "Kirchhoff Law Temperature Dependence of Enthalpy", "Direct MCQ",
         "For the reaction $\\text{N}_2(g) + 3\\text{H}_2(g) \\to 2\\text{NH}_3(g)$, the standard enthalpy of reaction at $300\\text{ K}$ is $\\Delta H_1 = -92.4\\text{ kJ/mol}$. Given molar heat capacities: $C_p(\\text{N}_2) = 29.1\\text{ J K}^{-1}\\text{ mol}^{-1}$, $C_p(\\text{H}_2) = 28.8\\text{ J K}^{-1}\\text{ mol}^{-1}$, and $C_p(\\text{NH}_3) = 35.1\\text{ J K}^{-1}\\text{ mol}^{-1}$. The value of $\\Delta C_p$ for this reaction is:",
         ["$-45.3\\text{ J K}^{-1}\\text{ mol}^{-1}$", "$+45.3\\text{ J K}^{-1}\\text{ mol}^{-1}$", "$-22.8\\text{ J K}^{-1}\\text{ mol}^{-1}$", "$+22.8\\text{ J K}^{-1}\\text{ mol}^{-1}$"], 0,
         "1. By definition of $\\Delta C_p$ for a balanced chemical reaction:\n   $$\\Delta C_p = \\sum C_p(\\text{products}) - \\sum C_p(\\text{reactants})$$.\n2. For the reaction $\\text{N}_2 + 3\\text{H}_2 \\to 2\\text{NH}_3$:\n   $$\\Delta C_p = 2 \\times C_p(\\text{NH}_3) - \\left[C_p(\\text{N}_2) + 3 \\times C_p(\\text{H}_2)\\right]$$.\n3. Substituting values:\n   $$\\Delta C_p = 2(35.1) - [29.1 + 3(28.8)] = 70.2 - [29.1 + 86.4] = 70.2 - 115.5 = -45.3\\text{ J K}^{-1}\\text{ mol}^{-1}$$.",
         "Forgetting stoichiometric coefficients (2 for ammonia and 3 for hydrogen) yields incorrect heat capacity difference.",
         "Kirchhoff\'s law: $\\Delta H_{T_2} - \\Delta H_{T_1} = \\Delta C_p (T_2 - T_1)$."),

        # 46. Electrochemistry - Nernst Cell Potential
        ("Electrochemistry", "Standard Gibbs Energy and Equilibrium Constant Relationship", "Direct MCQ",
         "The standard cell potential of the Daniel cell is $E^\\circ_{\\text{cell}} = 1.10\\text{ V}$ at $298\\text{ K}$ for $\\text{Zn}(s) + \\text{Cu}^{2+}(aq) \\rightleftharpoons \\text{Zn}^{2+}(aq) + \\text{Cu}(s)$. The standard Gibbs free energy change $\\Delta G^\\circ$ for this cell reaction is: (take Faraday constant $F = 96500\\text{ C/mol}$)",
         ["$-212.3\\text{ kJ/mol}$", "$+212.3\\text{ kJ/mol}$", "$-106.15\\text{ kJ/mol}$", "$-424.6\\text{ kJ/mol}$"], 0,
         "1. Number of electrons transferred in Daniel cell: $n = 2$.\n2. Relationship between Gibbs free energy and cell potential: $\\Delta G^\\circ = -n F E^\\circ_{\\text{cell}}$.\n3. Substituting values:\n   $$\\Delta G^\\circ = -2 \\times 96500\\text{ C/mol} \\times 1.10\\text{ V} = -212300\\text{ J/mol} = -212.3\\text{ kJ/mol}$$.",
         "Forgetting $n=2$ gives -106.15 kJ/mol; positive sign contradicts thermodynamic spontaneity.",
         "Spontaneous galvanic cell has positive $E^\\circ$ and negative $\\Delta G^\\circ = -nFE^\\circ$."),

        # 47. Periodic Table - Lanthanoid Contraction Consequences
        ("d- and f-Block Elements", "Lanthanoid Contraction and Similarities of 4d and 5d Elements", "Direct MCQ",
         "The almost identical atomic and ionic radii of Zirconium ($\\text{Zr}$, $4d$) and Hafnium ($\\text{Hf}$, $5d$) is a direct consequence of:",
         ["Lanthanoid contraction caused by poor shielding of $4f$ electrons",
          "Diagonal relationship between Period 5 and Period 6",
          "Shielding effect of $d$-electrons",
          "Inert pair effect in heavy transition elements"], 0,
         "1. Normally, down any group in the periodic table, atomic size increases due to addition of extra electron shells.\n2. However, between $\\text{La}$ ($Z=57$) and $\\text{Hf}$ ($Z=72$) lie the 14 lanthanoid elements ($4f^{1-14}$).\n3. The $4f$ subshell has a highly diffused spatial shape, resulting in exceptionally poor shielding of the outer electrons from the nuclear charge.\n4. As atomic number increases by 14 units, the effective nuclear charge rises steadily, pulling outer electrons closer.\n5. This cumulative contraction (Lanthanoid Contraction) exactly offsets the expected size increase, making radii of $\\text{Zr}$ ($160\\text{ pm}$) and $\\text{Hf}$ ($159\\text{ pm}$) almost identical.",
         "Diagonal relationship occurs between second and third period elements (Li-Mg, Be-Al, B-Si), not 4d and 5d.",
         "Lanthanoid contraction makes $4d$ and $5d$ members of the same group exhibit nearly identical physical and chemical properties."),

        # 48. Hydrocarbons - Terminal Alkyne Acidity
        ("Hydrocarbons", "Acidity of Terminal Alkynes and Heavy Metal Acetylide Precipitants", "Direct MCQ",
         "Which one of the following hydrocarbons forms a red precipitate when treated with ammoniacal cuprous chloride ($\\text{Cu}_2\\text{Cl}_2 + \\text{NH}_4\\text{OH}$) solution?",
         ["Propyne ($\\text{CH}_3-\\text{C}\\equiv\\text{CH}$)",
          "But-2-yne ($\\text{CH}_3-\\text{C}\\equiv\\text{C}-\\text{CH}_3$)",
          "Propene ($\\text{CH}_3-\\text{CH}=\\text{CH}_2$)",
          "Benzene ($\\text{C}_6\\text{H}_6$)"], 0,
         "1. Terminal alkynes (alkynes with a hydrogen directly attached to a triply bonded carbon, $\\equiv\\text{C}-\\text{H}$) possess acidic hydrogen.\n2. The $sp$-hybridized carbon has $50%$ $s$-character, providing high electronegativity that stabilizes the conjugate acetylide carbanion.\n3. When treated with ammoniacal cuprous chloride, the acidic hydrogen is replaced by copper, forming a red precipitate of cuprous acetylide: $\\text{CH}_3-\\text{C}\\equiv\\text{CH} + \\text{Cu}^+ \\to \\text{CH}_3-\\text{C}\\equiv\\text{C}-\\text{Cu}\\downarrow (\\text{red}) + \\text{H}^+$.\n4. But-2-yne is an internal alkyne lacking acidic terminal hydrogen, so it does not react.",
         "Internal alkynes like but-2-yne have no terminal acidic hydrogen and give no precipitate.",
         "Ammoniacal cuprous chloride forms a red precipitate exclusively with terminal alkynes ($R-\\text{C}\\equiv\\text{CH}$)."),

        # 49. Haloalkanes - Freons and Environmental Degradation
        ("Haloalkanes and Haloarenes", "Freon-12 Nomenclature and Stratospheric Catalytic Destruction", "Direct MCQ",
         "Freon-12 (Dichlorodifluoromethane, $\\text{CCl}_2\\text{F}_2$) is manufactured industrially from carbon tetrachloride ($\\text{CCl}_4$) by Swarts reaction using which fluorinating reagent?",
         ["$\\text{SbF}_3$ in the presence of $\\text{SbCl}_5$",
          "$\\text{NaF}$ in water",
          "$\\text{HF}$ gas alone",
          "$\\text{CaF}_2$ at room temperature"], 0,
         "1. Swarts reaction is used to synthesize alkyl fluorides and chlorofluorocarbons by halogen exchange.\n2. $\\text{CCl}_4$ is heated with antimony trifluoride ($\\text{SbF}_3$) in the presence of antimony pentachloride ($\\text{SbCl}_5$) catalyst:\n   $$3\\text{CCl}_4 + 2\\text{SbF}_3 \\xrightarrow{\\text{SbCl}_5} 3\\text{CCl}_2\\text{F}_2 + 2\\text{SbCl}_3$$.\n3. Freon-12 ($\\text{CCl}_2\\text{F}_2$) is extremely stable in the troposphere, but in the stratosphere UV radiation cleaves the $C-Cl$ bond releasing chlorine free radicals that catalytically destroy the protective ozone layer.",
         "NaF in water cannot replace chlorines in carbon tetrachloride.",
         "Freons are prepared by Swarts reaction using inorganic fluorides like $\\text{SbF}_3$, $\\text{AgF}$, or $\\text{Hg}_2\\text{F}_2$."),

        # 50. Coordination Compounds - Optical Inactivity of Trans Isomers
        ("Coordination Compounds", "Symmetry Elements and Optical Inactivity in Complexes", "Direct MCQ",
         "Which of the following coordination complexes is optically active and can be resolved into enantiomeric pairs?",
         ["$\\text{cis}-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$",
          "$\\text{trans}-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$",
          "$[\\text{Pt}(\\text{NH}_3)_3\\text{Cl}]^+$",
          "$\\text{trans}-[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]^+$"], 0,
         "1. A molecule or complex is optically active if it is chiral, meaning it lacks an improper axis of rotation ($S_n$), which practically means it has neither a plane of symmetry ($\\sigma$) nor a center of inversion ($i$).\n2. $\\text{trans}-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$ has a center of inversion and multiple planes of symmetry; it is superimposable on its mirror image and strictly achiral (optically inactive).\n3. $\\text{cis}-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$ has $C_2$ rotational symmetry only and possesses neither a plane of symmetry nor a center of inversion. It is chiral and exists as non-superimposable $d$- and $l$-enantiomers.\n4. Square planar complexes like $[\\text{Pt}(\\text{NH}_3)_3\\text{Cl}]^+$ have the molecular plane as a plane of symmetry and are achiral.",
         "Assuming trans-isomers are chiral because they contain bidentate ligands overlooks their inversion center.",
         "$\\text{cis}-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$ is chiral and optically active; the trans isomer is achiral due to a center of inversion.")
    ]

    assert len(topics_data) == 50, f"Expected 50 Chemistry topics, got {len(topics_data)}"

    # Dynamic rotation across Mocks 41 to 60 so each mock starts with a distinct chapter sequence
    rotated = topics_data[shift % 50:] + topics_data[:shift % 50]

    for i, item in enumerate(rotated):
        chapter, topic, q_type, text, options, correct_idx, solution_steps, distractor_analysis, takeaway = item
        q_num = i + 1  # 1 to 50
        sec = "Section A" if q_num <= 35 else "Section B"
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
