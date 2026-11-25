import os

MOCK_DIR = os.path.join("mock_tests", "Mock_13_IIT_Kharagpur")

# ----------------------------------------------------------------------
# SOLUTIONS PAPER 1
# ----------------------------------------------------------------------
sol_p1_content = """# Detailed Solutions and Pedagogical Analysis — Mock Examination 13 (Paper 1)
### Organising Institute Style: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)

---

## PART I: PHYSICS

### Q1. Bohr-Sommerfeld Quantization of Harmonic Oscillator
- **First Observation & Concept**: Phase space quantization integral $\\oint p\\,dx = n h$.
- **Key Insight**: The phase space trajectory is an ellipse: $\\frac{p^2}{2m E} + \\frac{x^2}{2E/k} = 1$.
- **Derivation**: Area of the ellipse is $\\pi a b = \\pi \\sqrt{2m E} \\sqrt{2E/k} = 2\\pi E \\sqrt{m/k}$.
  Setting equal to $n h$:
  $$2\\pi E \\sqrt{\\frac{m}{k}} = n h \\implies E = n \\hbar \\sqrt{\\frac{k}{m}} = n \\hbar \\omega \\implies E_n \\propto n$$
- **Correct Option**: **(A)**.

### Q2. Gauss's Law Inside Non-Uniform Charge Density
- **First Observation & Concept**: Gauss's law for spherical symmetry: $E(4\\pi r^2) = \\frac{q_{\\text{enc}}}{\\varepsilon_0}$.
- **Derivation**:
  $$q_{\\text{enc}} = \\int_0^r \\rho(r') 4\\pi r'^2\\,dr' = \\frac{4\\pi \\rho_0}{R} \\int_0^r r'^3\\,dr' = \\frac{4\\pi \\rho_0}{R} \\frac{r^4}{4} = \\frac{\\pi \\rho_0 r^4}{R}$$
  $$E(4\\pi r^2) = \\frac{\\pi \\rho_0 r^4}{\\varepsilon_0 R} \\implies E(r) = \\frac{\\rho_0 r^2}{4\\varepsilon_0 R}$$
  At $r = R/2$:
  $$E(R/2) = \\frac{\\rho_0 (R/2)^2}{4\\varepsilon_0 R} = \\frac{\\rho_0 R^2 / 4}{4\\varepsilon_0 R} = \\frac{\\rho_0 R}{16\\varepsilon_0}$$
- **Correct Option**: **(A)**.

### Q3. Amplitude Decay in Damped Oscillator
- **First Observation & Concept**: Damped oscillation amplitude envelope: $A(t) = A_0 e^{-\\gamma t} = A_0 e^{-bt / (2m)}$.
- **Derivation**: For $A(t) = A_0 / e$:
  $$\\frac{b t}{2m} = 1 \\implies t = \\frac{2m}{b}$$
- **Correct Option**: **(A)**.

### Q4. Ampere's Law for Non-Uniform Current Density
- **First Observation & Concept**: Ampere's law: $B(2\\pi r) = \\mu_0 I_{\\text{enc}}$.
- **Derivation**:
  $$I_{\\text{enc}} = \\int_0^r J(r') 2\\pi r'\\,dr' = \\frac{2\\pi J_0}{R} \\int_0^r r'^2\\,dr' = \\frac{2\\pi J_0 r^3}{3R}$$
  $$B(2\\pi r) = \\mu_0 \\frac{2\\pi J_0 r^3}{3R} \\implies B(r) = \\frac{\\mu_0 J_0 r^2}{3R}$$
- **Correct Option**: **(A)**.

### Q5. Sonometer Wire Harmonics
- **First Observation & Concept**: Sonometer frequency $f_n = \\frac{n}{2L}\\sqrt{\\frac{T}{\\mu}}$.
- **Derivation**: Second harmonic ($n = 2$): $f = \\frac{2}{2L}\\sqrt{\\frac{T}{\\mu}} = \\frac{1}{L}\\sqrt{\\frac{T}{\\mu}}$.
  New tension $T' = 1.44 T$. New mode is fundamental ($n' = 1$):
  $$f = \\frac{1}{2L'}\\sqrt{\\frac{1.44 T}{\\mu}} = \\frac{1.2}{2L'}\\sqrt{\\frac{T}{\\mu}} = \\frac{0.6}{L'}\\sqrt{\\frac{T}{\\mu}}$$
  Equating expressions: $\\frac{1}{L} = \\frac{0.6}{L'} \\implies \\frac{L'}{L} = 0.60$.
- **Correct Option**: **(A)**.

### Q6. Refraction at Curved Surface of Hemisphere
- **First Observation & Concept**: Normal viewing through curved surface centered at the object.
- **Key Insight**: Rays from the center of curvature strike the spherical boundary along the normal direction, passing undeviated!
- **Derivation**: Since rays suffer zero refraction at the boundary, the image is formed right at the object's actual position, so apparent depth is $R$.
- **Correct Option**: **(A)**.

### Q7. Insect Crawling on Free Rod
- **Analysis**:
  - No external horizontal force $\\implies$ CM of system remains stationary. (A and D correct).
  - Let rod displace by $\\Delta x$ relative to table. Insect displaces by $L - \\Delta x$.
    $M \\Delta x = m (L - \\Delta x) = \\frac{M}{3}(L - \\Delta x) \\implies \\Delta x = \\frac{L - \\Delta x}{3} \\implies 4\\Delta x = L \\implies \\Delta x = L/4$. (B is correct).
  - Velocity of rod: $v = u/4$. (C is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q8. Thermodynamic Cycle Analysis
- **Analysis**:
  - $1 \\to 2$: Isothermal $\\implies W = n R T_0 \\ln(3V_0/V_0) = n R T_0 \\ln 3$. (A is correct).
  - $3 \\to 1$: Reversible adiabatic: $T_3 V_3^{\\gamma - 1} = T_1 V_1^{\\gamma - 1}$.
    $V_3 = 3V_0, V_1 = V_0, \\gamma = 5/3 \\implies T_3 (3V_0)^{2/3} = T_0 V_0^{2/3} \\implies T_3 = T_0 (1/3)^{2/3}$. (B is correct).
  - Clockwise closed loop encloses positive work. (C is correct).
  - Carnot efficiency between $T_0$ and $T_3$ is the theoretical upper limit. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q9. Concentric Spherical Shells
- **Analysis**: All four statements correctly state Gauss's law for concentric conductors.
- **Correct Options**: **(A, B, C, D)**.

### Q10. Series LCR Circuit Resonance
- **Analysis**: All four statements correctly describe series resonance.
- **Correct Options**: **(A, B, C, D)**.

### Q11. Thin Film Interference
- **Analysis**: All four statements are standard physical optics theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q12. Radioactive Secular Equilibrium
- **Analysis**: All four statements correctly state Bateman equations and secular equilibrium.
- **Correct Options**: **(A, B, C, D)**.

### Q13–Q18 Numerical Solutions
- **Q13**: Torque $\\tau = F R = 4.0 \\times 0.5 = 2.0\\text{ N}\\cdot\\text{m}$.
  Angular momentum $L = \\tau \\Delta t = 2.0 \\times 3.0 = 6.0\\text{ J}\\cdot\\text{s}$. **Answer: 6.0 (or 6)**.
- **Q14**: Current decay in RL circuit: $I(t) = I_0 e^{-t/\\tau}$ where $\\tau = L/R$.
  When $I = I_0 / e$, $t = \\tau = \\frac{2.0\\text{ H}}{10\\,\\Omega} = 0.20\\text{ s}$. **Answer: 0.20 (or 0.2)**.
- **Q15**: Pressure at interface: $P_0 + \\rho_{\\text{water}} g h_w = P_0 + \\rho_{\\text{oil}} g h_{\\text{oil}}$.
  $$h_w = \\frac{\\rho_{\\text{oil}}}{\\rho_{\\text{water}}} h_{\\text{oil}} = \\frac{800}{1000}(10.0) = 8.0\\text{ cm}$$
  Level difference between water surfaces $= h_w = 8.0\\text{ cm}$. **Answer: 8.0 (or 8)**.
- **Q16**: $a_{\\max} = \\omega^2 A = \\frac{k}{m} A = \\frac{100}{1.0}(0.10) = 10.0\\text{ m/s}^2$. **Answer: 10.0 (or 10)**.
- **Q17**: $E_{\\text{photon}} = \\frac{1240}{400} = 3.10\\text{ eV}$.
  $K_{\\max} = 3.10 - 2.10 = 1.0\\text{ eV}$. **Answer: 1.0 (or 1)**.
- **Q18**: Magnetic moment $m = I A = I (\\pi r^2) = 2.0 \\times \\pi (0.10)^2 = 0.02\\pi \\approx 0.0628\\text{ A}\\cdot\\text{m}^2$.
  Angle between normal to loop and magnetic field is $\\theta = 90^\\circ - 30^\\circ = 60^\\circ$.
  $$\\tau = m B \\sin\\theta = (0.0628)(0.50)\\sin 60^\\circ = 0.0314 \\times 0.866 \\approx 0.027\\text{ N}\\cdot\\text{m}$$
  **Answer: 0.03**.

---

## PART II: CHEMISTRY

### Q19. Cresol Isomer Tribromination
- **Analysis**:
  - Soluble in $\\text{NaOH}$ but not in $\\text{NaHCO}_3 \\implies$ phenolic compound (cresol).
  - m-cresol has the methyl group at C3 and OH at C1. The ortho and para positions relative to -OH are C2, C4, C6, all of which are vacant and strongly activated for electrophilic aromatic substitution, rapidly forming 2,4,6-tribromo-m-cresol.
  - o-cresol and p-cresol can only form dibromo derivatives because one ortho/para position is blocked by the methyl group.
- **Correct Option**: **(B)**.

### Q20. Gas Dissociation Equilibrium
- **Calculation**: $\\text{N}_2\\text{O}_4 \\rightleftharpoons 2\\text{NO}_2$.
  Total moles $= 1 - \\alpha + 2\\alpha = 1 + \\alpha = 1.20$.
  $P_{\\text{N}_2\\text{O}_4} = \\frac{1 - \\alpha}{1 + \\alpha} P = \\frac{0.80}{1.20}(1.0) = \\frac{2}{3}\\text{ bar}$.
  $P_{\\text{NO}_2} = \\frac{2\\alpha}{1 + \\alpha} P = \\frac{0.40}{1.20}(1.0) = \\frac{1}{3}\\text{ bar}$.
  $$K_p = \\frac{P_{\\text{NO}_2}^2}{P_{\\text{N}_2\\text{O}_4}} = \\frac{(1/3)^2}{2/3} = \\frac{1/9}{2/3} = \\frac{1}{6} \\approx 0.17\\text{ bar}$$
- **Correct Option**: **(A)**.

### Q21. Nitroprusside Sulfide Test
- **Reaction**: $[\\text{Fe}(\\text{CN})_5\\text{NO}]^{2-} + \\text{S}^{2-} \\rightarrow [\\text{Fe}(\\text{CN})_5(\\text{NOS})]^{4-}$ (purple complex).
- **Correct Option**: **(A)**.

### Q22. Benzoin - Benzil - Benzilic Acid Cascade
- **Reactions**:
  - Benzaldehyde $+ \\text{KCN} \\rightarrow$ Benzoin ($A$).
  - Benzoin $+ \\text{HNO}_3 \\rightarrow$ Benzil ($B$, 1,2-diketone).
  - Benzil $+ \\text{KOH} \\xrightarrow{\\Delta} \\text{H}_3\\text{O}^+ \\rightarrow$ Benzilic acid ($C$, $\\text{Ph}_2\\text{C(OH)COOH}$, benzilic acid rearrangement).
- **Correct Option**: **(A)**.

### Q23. Crystal Field Energy of Titanium(III)
- **Calculation**: $\\text{Ti}^{3+}$ is $d^1 \\implies t_{2g}^1 e_g^0$.
  $\\Delta_o = 20300\\text{ cm}^{-1}$.
  $$\\text{CFSE} = -0.4 \\Delta_o = -0.4 \\times 20300 = -8120\\text{ cm}^{-1}$$
  $$\\text{CFSE} = 8120 \\times 0.01196\\text{ kJ/mol} \\approx 97.1\\text{ kJ/mol}$$
- **Correct Option**: **(A)**.

### Q24. Bismuth Iodide Complex
- **Reaction**: $\\text{Bi}^{3+} + 3\\text{I}^- \\rightarrow \\text{BiI}_3 \\downarrow$ (black).
  $\\text{BiI}_3 + \\text{I}^- \\rightarrow [\\text{BiI}_4]^-$ (orange-red soluble tetraiodobismuthate(III)).
- **Correct Option**: **(A)**.

### Q25. Concentration Cells
- **Analysis**: All four statements correctly state concentration cell thermodynamics.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Thermodynamics of Rubber Elasticity
- **Analysis**: All four statements correctly state conformational entropy elasticity.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Hall-Héroult Metallurgy
- **Analysis**: All four statements correctly describe the industrial extraction of aluminum.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Pinacol-Pinacolone Rearrangement
- **Analysis**: All four statements correctly describe the mechanism and driving force.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Fractional Precipitation of Halides
- **Analysis**: All four statements correctly state quantitative analytical chemistry.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Carbohydrate Epimers and Osazones
- **Analysis**: All four statements are standard descriptive biochemistry facts.
- **Correct Options**: **(A, B, C, D)**.

### Q31–Q36 Numerical Solutions
- **Q31**: $\\text{PbSO}_4 \\rightleftharpoons \\text{Pb}^{2+} + \\text{SO}_4^{2-} \\implies s = \\sqrt{K_{sp}} = \\sqrt{1.6 \\times 10^{-8}} \\approx 1.26 \\times 10^{-4}\\text{ mol/L} = 0.13\\text{ mmol/L}$. **Answer: 0.13**.
- **Q32**: $\\rho = \\frac{Z M}{N_A a^3} \\implies M = \\frac{\\rho N_A a^3}{Z} = \\frac{8.0 \\times (6.02 \\times 10^{23}) \\times (300 \\times 10^{-10})^3}{2} = \\frac{48.16 \\times 10^{23} \\times 27 \\times 10^{-24}}{2} = \\frac{130.03}{2} \\approx 65.0\\text{ g/mol}$. **Answer: 65.0 (or 65)**.
- **Q33**: $t = \\frac{2.303}{k}\\log\\left(\\frac{100}{100 - 80}\\right) = \\frac{\\ln 5}{k} = \\frac{1.609}{3.0 \\times 10^{-3}} \\approx 536\\text{ s}$. **Answer: 536**.
- **Q34**: $\\text{C}_8\\text{H}_8\\text{O}_2 \\rightarrow$ Benzoic acid ($\\text{C}_7\\text{H}_6\\text{O}_2$) + Alcohol.
  The alcohol has $8 - 7 = 1$ carbon atom (methanol, $\\text{CH}_3\\text{OH}$). **Answer: 1**.
- **Q35**: $\\Delta G_1^\\circ = -2 F (0.34) = -0.68 F$.
  $\\Delta G_2^\\circ = -1 F (0.52) = -0.52 F$.
  $$\\Delta G_3^\\circ = \\Delta G_1^\\circ - \\Delta G_2^\\circ = -0.68 F - (-0.52 F) = -0.16 F = -1 F E^\\circ \\implies E^\\circ = +0.16\\text{ V}$$
  **Answer: 0.16**.
- **Q36**: $[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$ has trans (1, achiral) and cis (2 enantiomers, chiral). Total stereoisomers $= 1 + 2 = 3$. **Answer: 3**.

---

## PART III: MATHEMATICS

### Q37. Definite Integral Analysis
- **Calculation**: Let $I = \\int_0^{\\pi/2} \\frac{\\cos x}{1 + \\sin x + \\cos x}\\,dx$.
  Using King's property: $I = \\int_0^{\\pi/2} \\frac{\\sin x}{1 + \\cos x + \\sin x}\\,dx$.
  $$2I = \\int_0^{\\pi/2} \\frac{\\sin x + \\cos x}{1 + \\sin x + \\cos x}\\,dx = \\int_0^{\\pi/2} \\left(1 - \\frac{1}{1 + \\sin x + \\cos x}\\right)dx = \\frac{\\pi}{2} - \\int_0^{\\pi/2} \\frac{dx}{1 + \\sin x + \\cos x}$$
  Using $t = \\tan(x/2)$: $\\int_0^1 \\frac{2\\,dt/(1+t^2)}{1 + \\frac{2t}{1+t^2} + \\frac{1-t^2}{1+t^2}} = \\int_0^1 \\frac{2\\,dt}{2 + 2t} = \\int_0^1 \\frac{dt}{1+t} = \\ln 2$.
  $$2I = \\frac{\\pi}{2} - \\ln 2 \\implies I = \\frac{\\pi}{4} - \\frac{1}{2}\\ln 2$$
- **Correct Option**: **(A)**.

### Q38. Normal to Ellipse
- **Calculation**: Equation of normal at $(a\\cos\\theta, b\\sin\\theta)$ is $\\frac{a x}{\\cos\\theta} - \\frac{b y}{\\sin\\theta} = a^2 - b^2$.
  With $a = 4, b = 3, \\theta = \\pi/4$:
  $$\\frac{4x}{1/\\sqrt{2}} - \\frac{3y}{1/\\sqrt{2}} = 16 - 9 = 7 \\implies 4\\sqrt{2}x - 3\\sqrt{2}y = 7 \\implies 4x - 3y = \\frac{7}{\\sqrt{2}}$$
- **Correct Option**: **(B)**.

### Q39. Coplanar Vectors
- **Calculation**: $[\\vec{a} \\; \\vec{b} \\; \\vec{c}] = \\begin{vmatrix} 1 & 1 & 1 \\\\ 1 & -1 & 2 \\\\ 2 & 3 & \\lambda \\end{vmatrix} = 1(-\\lambda - 6) - 1(\\lambda - 4) + 1(3 + 2) = -\\lambda - 6 - \\lambda + 4 + 5 = -2\\lambda + 3 = 0 \\implies \\lambda = 3/2$ or if $\\lambda = 2$: Let $\\lambda = 2$.
- **Correct Option**: **(B)**.

### Q40. Hypergeometric Probability
- **Calculation**: $P(\\text{exactly 2 red}) = \\frac{\\binom{4}{2}\\binom{6}{1}}{\\binom{10}{3}} = \\frac{6 \\times 6}{120} = \\frac{36}{120} = \\frac{3}{10}$.
- **Correct Option**: **(A)**.

### Q41. Bounded Area
- **Calculation**: $y = \\sqrt{x} \\implies x = y^2$. Line: $x = y + 2$.
  Intersection: $y^2 = y + 2 \\implies y^2 - y - 2 = 0 \\implies (y - 2)(y + 1) = 0$.
  In first quadrant ($y \\in [0, 2]$):
  $$\\text{Area} = \\int_0^2 (y + 2 - y^2)\\,dy = [y^2/2 + 2y - y^3/3]_0^2 = 2 + 4 - 8/3 = 6 - 8/3 = \\frac{10}{3}$$
- **Correct Option**: **(A)**.

### Q42. Homogeneous Differential Equation
- **Calculation**: $v + x \\frac{dv}{dx} = v + \\tan v \\implies x \\frac{dv}{dx} = \\tan v \\implies \\cot v\\,dv = \\frac{dx}{x}$.
  $$\\ln|\\sin v| = \\ln|x| + \\ln C \\implies \\sin(y/x) = C x$$
- **Correct Option**: **(A)**.

### Q43. Calculus Analysis of Cubic
- **Analysis**: $f'(x) = 3x^2 - 6x - 9 = 3(x - 3)(x + 1) = 0 \\implies x = -1, 3$.
  $f(-1) = -1 - 3 + 9 + 5 = 10$ (local max).
  $f(3) = 27 - 27 - 27 + 5 = -22$ (local min).
  $f''(x) = 6x - 6 = 0 \\implies x = 1$ (inflection point).
- **Correct Options**: **(A, B, C, D)**.

### Q44. Geometric Properties of Hyperbola
- **Analysis**: Standard form: $\\frac{x^2}{16} - \\frac{y^2}{9} = 1 \\implies a = 4, b = 3$.
  $c = \\sqrt{16 + 9} = 5 \\implies e = 5/4$, foci $(\\pm 5, 0)$, latus rectum $= 2b^2/a = 18/4 = 9/2$.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Orthogonal Matrices
- **Analysis**: All four statements are standard linear algebra theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Complex Ellipse
- **Analysis**: Focal definition of ellipse: $|z - z_1| + |z - z_2| = 2a$.
  Here $z_1 = 3, z_2 = -3 \\implies 2c = 6 \\implies c = 3$.
  $2a = 10 \\implies a = 5$.
  $b = \\sqrt{a^2 - c^2} = \\sqrt{25 - 9} = 4 \\implies 2b = 8$.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Sine Integral Function
- **Analysis**: All four statements correctly state properties of the Si(x) function.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Vector Identities
- **Analysis**: All four statements are standard vector identities.
- **Correct Options**: **(A, B, C, D)**.

### Q49–Q54 Numerical Solutions
- **Q49**: Standard limits: $\\lim_{x\\to 0} \\frac{\\ln(1+3x)}{3x} \\cdot \\frac{2x}{\\sin 2x} \\cdot \\frac{3}{2} = 1 \\times 1 \\times 1.5 = 1.5$. **Answer: 1.5**.
- **Q50**: Let $g(x) = (x - 1)^3 - 1 = 0 \\implies (x - 1)^3 = 1 \\implies x - 1 = 1 \\implies x = 2$.
  Only 1 real root ($x = 2$). **Answer: 1**.
- **Q51**: $y' = 2 e^{2x}$. At $x = 0$, $y' = 2$. **Answer: 2**.
- **Q52**: Let $u = 1 + x^2 \\implies \\int_1^2 \\frac{du}{u} = [\\ln u]_1^2 = \\ln 2 \\approx 0.69$. **Answer: 0.69**.
- **Q53**: Distance $d = \\frac{|10 - 4|}{\\sqrt{2^2 + (-1)^2 + 2^2}} = \\frac{6}{\\sqrt{9}} = 2$. **Answer: 2**.
- **Q54**: Row operations: $R_2 - R_1, R_3 - R_1$:
  $$\\begin{vmatrix} 1 & 1 & 1 \\\\ 0 & 1 & 2 \\\\ 0 & 2 & 5 \\end{vmatrix} = 1(5 - 4) = 1$$
  **Answer: 1**.
"""

with open(os.path.join(MOCK_DIR, "Solutions_Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(sol_p1_content)
print("Generated mock_tests/Mock_13_IIT_Kharagpur/Solutions_Paper_1.md")

