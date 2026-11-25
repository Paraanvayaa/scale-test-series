import os

MOCK_DIR = os.path.join("mock_tests", "Mock_13_IIT_Kharagpur")
os.makedirs(MOCK_DIR, exist_ok=True)

# ----------------------------------------------------
# PAPER 1
# ----------------------------------------------------
p1_content = """# JEE (Advanced) Mock Examination 13
### Organising Institute Style: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)
### Paper 1 · Full Syllabus · Total Marks: 180 · Duration: 3 Hours

---

## Instructions
- This paper consists of **54 questions** across three subjects: **Physics (Qs 1–18)**, **Chemistry (Qs 19–36)**, and **Mathematics (Qs 37–54)**.
- Each subject contains three sections:
  - **Section 1**: 6 Single Correct Option Questions (+3, -1, 0)
  - **Section 2**: 6 One or More Than One Correct Option Questions (+4, -2, 0; Partial marking: +3, +2, +1)
  - **Section 3**: 6 Numerical Value Questions (+3, 0; exact decimal or rounded to two decimal places)

---

# PART I: PHYSICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 1–6)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q1.** A particle of mass $m$ is confined to move in a central potential $V(r) = \\frac{1}{2} k r^2$. According to the Bohr-Sommerfeld quantization rule $\\oint p_r\\,dr + \\oint p_\\theta\\,d\\theta = n h$, the allowed energy levels $E_n$ ($n = 1, 2, 3, \\dots$) scale with quantum number $n$ as:
(A) $E_n \\propto n$  
(B) $E_n \\propto n^2$  
(C) $E_n \\propto \\sqrt{n}$  
(D) $E_n \\propto n^{-1}$  

**Q2.** A solid insulating sphere of radius $R$ has a non-uniform charge density $\\rho(r) = \\rho_0 \\frac{r}{R}$ for $r \\le R$, and zero outside. The electric field intensity at distance $r = R/2$ from the center is:
(A) $\\frac{\\rho_0 R}{16\\varepsilon_0}$  
(B) $\\frac{\\rho_0 R}{8\\varepsilon_0}$  
(C) $\\frac{\\rho_0 R}{32\\varepsilon_0}$  
(D) $\\frac{\\rho_0 R}{4\\varepsilon_0}$  

**Q3.** A light damping force $F_d = -b v$ acts on an oscillator of mass $m$ and spring constant $k$. The time taken for the amplitude of oscillations to decay to $1/e$ of its initial value is:
(A) $\\frac{2m}{b}$  
(B) $\\frac{m}{b}$  
(C) $\\frac{m}{2b}$  
(D) $\\frac{4m}{b}$  

**Q4.** A long cylindrical conductor of radius $R$ carries a non-uniform current density $J(r) = J_0 (r/R)$ parallel to its axis. The magnetic field at a distance $r < R$ from the axis is:
(A) $\\frac{\\mu_0 J_0 r^2}{3R}$  
(B) $\\frac{\\mu_0 J_0 r^2}{2R}$  
(C) $\\frac{\\mu_0 J_0 r}{3}$  
(D) $\\frac{\\mu_0 J_0 R}{3}$  

**Q5.** In an experiment with a sonometer wire of length $L$, mass $m$, and tension $T$, the wire resonates in its second harmonic with a tuning fork of frequency $f$. If the tension is increased by $44\\%$, the length of the wire must be changed to $L'$ so that it resonates in the fundamental mode with the same tuning fork. The ratio $L' / L$ is:
(A) $0.60$  
(B) $1.20$  
(C) $0.50$  
(D) $1.44$  

**Q6.** A glass hemisphere of radius $R$ and refractive index $\\mu = 1.50$ is placed with its flat surface horizontal on a table. A small object is placed at the center of the flat surface. When viewed from vertically above through the curved surface, the apparent depth of the object is:
(A) $R$  
(B) $R / 1.5$  
(C) $1.5 R$  
(D) $2R$  

---

### SECTION 2: One or More Than One Correct Option (Qs 7–12)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q7.** A uniform rod of mass $M$ and length $L$ lies on a smooth horizontal table. An insect of mass $m = M/3$ crawls along the rod from one end $A$ to the other end $B$ with constant speed $u$ relative to the rod:
(A) The center of mass of the (rod + insect) system remains stationary.  
(B) The total displacement of the rod relative to the table during the insect's crawl is $L/4$ in the opposite direction.  
(C) The speed of the rod relative to the table while the insect crawls is $u/4$.  
(D) No external horizontal force acts on the system.  

**Q8.** A monoatomic ideal gas undergoes a cycle $1 \\rightarrow 2 \\rightarrow 3 \\rightarrow 1$. Process $1 \\rightarrow 2$ is isothermal expansion at $T_0$ from $V_0$ to $3V_0$. Process $2 \\rightarrow 3$ is isochoric cooling. Process $3 \\rightarrow 1$ is adiabatic compression back to the initial state $(P_0, V_0, T_0)$:
(A) The work done in process $1 \\rightarrow 2$ is $n R T_0 \\ln 3$.  
(B) The temperature at state 3 is $T_3 = T_0 (1/3)^{2/3}$.  
(C) The net work done in the cycle is positive.  
(D) The efficiency of this cycle is strictly less than the Carnot efficiency between $T_0$ and $T_3$.  

**Q9.** Two thin coaxial metallic spherical shells of radii $R_1$ and $R_2$ ($R_1 < R_2$) carry charges $Q_1$ and $Q_2$:
(A) The electric field in the region $r < R_1$ is zero.  
(B) The electric field in the region $R_1 < r < R_2$ depends only on $Q_1$.  
(C) The potential difference between the two shells is $V_1 - V_2 = \\frac{Q_1}{4\\pi\\varepsilon_0}\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$.  
(D) Connecting the two shells with a conducting wire causes charge $Q_1$ to transfer completely to the outer shell.  

**Q10.** A series $LCR$ circuit with $L = 0.5\\text{ H}$, $C = 20\\,\\mu\\text{F}$, and $R = 50\\,\\Omega$ is driven by an AC voltage $V(t) = 100\\sin(\\omega t)$:
(A) The resonance angular frequency is $\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{10^{-5}}} = 100\\sqrt{10}\\text{ rad/s}$.  
(B) At resonance, the current amplitude is $I_0 = 2.0\\text{ A}$.  
(C) The average power dissipated at resonance is $100\\text{ W}$.  
(D) If $\\omega < \\omega_0$, the current leads the source voltage.  

**Q11.** In an interference pattern formed by thin film reflection of monochromatic light of wavelength $\\lambda$:
(A) If the film is surrounded on both sides by a medium of lower refractive index, the condition for constructive interference is $2\\mu t \\cos r = (m + 1/2)\\lambda$.  
(B) If the film has a thickness $t \\ll \\lambda$, the reflected intensity approaches zero (dark film).  
(C) The colors of soap bubbles viewed in sunlight arise from thin-film interference.  
(D) The transmitted and reflected interference patterns are complementary.  

**Q12.** In a radioactive decay series $A \\xrightarrow{\\lambda_1} B \\xrightarrow{\\lambda_2} C$ (with $C$ stable):
(A) If $\\lambda_1 \\ll \\lambda_2$, secular equilibrium is achieved and $N_B / N_A \\approx \\lambda_1 / \\lambda_2$.  
(B) The activity of $B$ eventually equals the activity of $A$ in secular equilibrium.  
(C) The total number of nuclei $N_A(t) + N_B(t) + N_C(t)$ is constant in time.  
(D) The rate of formation of $C$ is $\\lambda_2 N_B$.  

---

### SECTION 3: Numerical Value Questions (Qs 13–18)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q13.** A uniform thin disc of mass $M = 2.0\\text{ kg}$ and radius $R = 0.5\\text{ m}$ is free to rotate about a fixed vertical axis passing through its center. A constant tangential force $F = 4.0\\text{ N}$ is applied to the rim for $\\Delta t = 3.0\\text{ seconds}$ starting from rest. The final angular momentum of the disc (in $\\text{J}\\cdot\\text{s}$) is:  

**Q14.** In a circuit containing an inductor $L = 2.0\\text{ H}$ and resistor $R = 10\\,\\Omega$, a steady current is established by a $20\\text{ V}$ battery. The battery is suddenly short-circuited at $t = 0$. The time taken (in seconds) for the current to drop to $1/e$ of its steady-state value is:  

**Q15.** A U-tube of uniform cross-section contains water. When oil of density $\\rho = 800\\text{ kg/m}^3$ is poured into one limb to a height of $h_{\\text{oil}} = 10.0\\text{ cm}$, the difference in height between the water levels in the two limbs (in cm) is:  

**Q16.** A block of mass $m = 1.0\\text{ kg}$ is attached to a horizontal spring of stiffness $k = 100\\text{ N/m}$. The block is pulled $x = 0.10\\text{ m}$ from equilibrium and released. The maximum acceleration of the block (in $\\text{m/s}^2$) is:  

**Q17.** A beam of light of wavelength $\\lambda = 400\\text{ nm}$ is incident on a metal with work function $\\Phi = 2.1\\text{ eV}$ ($hc = 1240\\text{ eV}\\cdot\\text{nm}$). The maximum kinetic energy of the emitted photoelectrons (in eV) is:  

**Q18.** A circular wire loop of radius $r = 10\\text{ cm}$ carrying a current $I = 2.0\\text{ A}$ is placed in a uniform magnetic field $B = 0.50\\text{ T}$ such that the plane of the loop makes an angle of $30^\\circ$ with the field. The torque acting on the loop (in $\\text{N}\\cdot\\text{m}$) is (use $\\pi \\approx 3.14$, round to two decimal places):  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: Single Correct Option (Qs 19–24)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q19.** An organic compound $P$ ($\\text{C}_7\\text{H}_8\\text{O}$) is insoluble in aqueous $\\text{NaHCO}_3$ but dissolves readily in aqueous $\\text{NaOH}$. When treated with bromine water, it rapidly gives a tribromo derivative $\\text{C}_7\\text{H}_5\\text{Br}_3\\text{O}$. The structure of compound $P$ is:
(A) o-cresol  
(B) m-cresol  
(C) p-cresol  
(D) Anisole  

**Q20.** For the gaseous equilibrium $\\text{N}_2\\text{O}_4(g) \\rightleftharpoons 2\\text{NO}_2(g)$, the degree of dissociation is $\\alpha = 0.20$ at a total pressure of $1.0\\text{ bar}$. The value of $K_p$ (in bar) is:
(A) $0.17$  
(B) $0.25$  
(C) $0.04$  
(D) $0.50$  

**Q21.** In qualitative inorganic analysis, addition of sodium nitroprusside ($\\text{Na}_2[\\text{Fe}(\\text{CN})_5\\text{NO}]$) to an alkaline solution containing sulfide ions produces a brilliant purple coloration due to the formation of:
(A) $[\\text{Fe}(\\text{CN})_5(\\text{NOS})]^{4-}$  
(B) $[\\text{Fe}(\\text{CN})_5(\\text{NO}_2)]^{4-}$  
(C) $[\\text{Fe}(\\text{CN})_6]^{3-}$  
(D) $[\\text{Fe}(\\text{H}_2\\text{O})_5(\\text{NO})]^{2+}$  

**Q22.** In the multi-step synthesis:
$$\\text{Benzaldehyde} \\xrightarrow{\\text{KCN / EtOH / } \\Delta} A \\xrightarrow{\\text{conc. HNO}_3} B \\xrightarrow{\\text{KOH / } \\Delta \\text{ then } \\text{H}_3\\text{O}^+} C$$
The final product $C$ is:
(A) Benzilic acid  
(B) Benzoin  
(C) Benzil  
(D) Mandelic acid  

**Q23.** The electronic absorption spectrum of $[\\text{Ti}(\\text{H}_2\\text{O})_6]^{3+}$ exhibits a single broad absorption peak at $20300\\text{ cm}^{-1}$. The crystal field stabilization energy (CFSE) of this complex in $\\text{kJ/mol}$ is ($1\\text{ cm}^{-1} \\approx 0.01196\\text{ kJ/mol}$):
(A) $97.1\\text{ kJ/mol}$  
(B) $242.8\\text{ kJ/mol}$  
(C) $145.7\\text{ kJ/mol}$  
(D) $48.6\\text{ kJ/mol}$  

**Q24.** When excess potassium iodide solution is added to a solution of bismuth nitrate acidified with dilute nitric acid, a black precipitate is formed which dissolves in excess $\\text{KI}$ to form an orange-red solution of:
(A) $[\\text{BiI}_4]^-$  
(B) $\\text{BiI}_3$  
(C) $[\\text{Bi}(\\text{NO}_3)_4]^-$  
(D) $\\text{BiOI}$  

---

### SECTION 2: One or More Than One Correct Option (Qs 25–30)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q25.** A concentration cell without liquid junction is constructed as: $\\text{Pt}|\\text{H}_2(g, 1\\text{ bar})|\\text{HCl}(m_1)||\\text{HCl}(m_2)|\\text{H}_2(g, 1\\text{ bar})|\\text{Pt}$:
(A) The cell EMF is given by $E_{\\text{cell}} = \\frac{2.303 RT}{F}\\log\\frac{m_2}{m_1}$.  
(B) The standard potential of any concentration cell is strictly $E^\\circ = 0$.  
(C) The process is spontaneous if $m_2 > m_1$.  
(D) Transfer of solute from higher to lower concentration drives the electrical current.  

**Q26.** Regarding the thermodynamics of rubber elasticity:
(A) Stretching a rubber band aligns polymer chains, decreasing its conformational entropy ($\\Delta S < 0$).  
(B) The process of stretching rubber is exothermic (heat is released, $\\Delta H < 0$).  
(C) When a stretched rubber band contracts spontaneously, its entropy increases.  
(D) Heating a stretched rubber band causes it to contract.  

**Q27.** Which of the following statements is/are correct regarding the extraction of aluminum by the Hall-Héroult process?
(A) Bauxite is purified to pure alumina ($\\text{Al}_2\\text{O}_3$) by the Bayer process using aqueous $\\text{NaOH}$.  
(B) Cryolite ($\\text{Na}_3\\text{AlF}_6$) lowers the melting point of alumina from $2320\\text{ K}$ to about $1220\\text{ K}$.  
(C) The carbon anodes are consumed during electrolysis, forming $\\text{CO}$ and $\\text{CO}_2$.  
(D) Aluminum metal is produced at the cathode.  

**Q28.** In the acid-catalyzed pinacol-pinacolone rearrangement of 1,1,2-triphenylethane-1,2-diol:
(A) The reaction proceeds via the more stable benzylic carbocation intermediate.  
(B) The migrating group is phenyl rather than hydrogen or methyl.  
(C) The product obtained is triphenylacetaldehyde or a phenyl ketone.  
(D) The thermodynamic driving force is the formation of a very stable carbonyl $\\text{C=O}$ double bond.  

**Q29.** In a solution containing equal concentrations of $\\text{Cl}^-, \\text{Br}^-$, and $\\text{I}^-$, aqueous $\\text{AgNO}_3$ solution is added dropwise:
(A) $\\text{AgI}$ precipitates first because its $K_{sp}$ is the smallest ($8.5\\times 10^{-17}$).  
(B) $\\text{AgBr}$ precipitates second ($K_{sp} = 5.0\\times 10^{-13}$).  
(C) $\\text{AgCl}$ precipitates last ($K_{sp} = 1.8\\times 10^{-10}$).  
(D) Fractional precipitation cleanly separates iodide from chloride.  

**Q30.** For the reactions of monosaccharides:
(A) D-glucose and D-mannose are C-2 epimers.  
(B) D-glucose reacts with excess phenylhydrazine to form a glucosazone identical to that from D-fructose.  
(C) $\\alpha$-D-glucopyranose and $\\beta$-D-glucopyranose are anomers.  
(D) Mutarotation involves spontaneous interconversion between $\\alpha$ and $\\beta$ anomers via the open-chain form.  

---

### SECTION 3: Numerical Value Questions (Qs 31–36)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q31.** The solubility product of lead sulfate $\\text{PbSO}_4$ is $K_{sp} = 1.6\\times 10^{-8}$. The solubility of $\\text{PbSO}_4$ in pure water (in mmol/L) is (round to two decimal places):  

**Q32.** An element has a body-centered cubic (BCC) lattice with edge length $a = 300\\text{ pm}$ and density $\\rho = 8.0\\text{ g/cm}^3$. The molar mass of the element (in g/mol) is ($N_A = 6.02\\times 10^{23}\\text{ mol}^{-1}$, round to one decimal place):  

**Q33.** A first-order reaction has a rate constant $k = 3.0\\times 10^{-3}\\text{ s}^{-1}$. The time (in seconds) required for $80\\%$ of the reactant to decompose is (use $\\ln 5 \\approx 1.609$, round to nearest integer):  

**Q34.** An aromatic ester has molecular formula $\\text{C}_8\\text{H}_8\\text{O}_2$. Alkaline hydrolysis followed by acidification yields benzoic acid and an alcohol. The number of carbon atoms in the alcohol is:  

**Q35.** The standard electrode potential for $\\text{Cu}^{2+} + 2e^- \\rightarrow \\text{Cu}$ is $+0.34\\text{ V}$ and for $\\text{Cu}^+ + e^- \\rightarrow \\text{Cu}$ is $+0.52\\text{ V}$. The standard reduction potential $E^\\circ$ for $\\text{Cu}^{2+} + e^- \\rightarrow \\text{Cu}^+$ (in Volts) is:  

**Q36.** The total number of stereoisomers (optical + geometrical) possible for the complex $[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$ is:  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 37–42)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q37.** The value of the definite integral
$$I = \\int_{0}^{\\pi/2} \\frac{\\cos x}{1 + \\sin x + \\cos x}\\,dx$$
is:
(A) $\\frac{\\pi}{4} - \\frac{1}{2}\\ln 2$  
(B) $\\frac{\\pi}{4} + \\frac{1}{2}\\ln 2$  
(C) $\\frac{\\pi}{2}$  
(D) $\\frac{\\pi}{4}$  

**Q38.** The equation of the normal to the ellipse $\\frac{x^2}{16} + \\frac{y^2}{9} = 1$ at the point $(4\\cos\\theta, 3\\sin\\theta)$ with $\\theta = \\pi/4$ is:
(A) $4x - 3y = 7\\sqrt{2}$  
(B) $4x - 3y = 7/\\sqrt{2}$  
(C) $3x - 4y = 7$  
(D) $4x + 3y = 7\\sqrt{2}$  

**Q39.** If the vectors $\\vec{a} = \\hat{i} + \\hat{j} + \\hat{k}$, $\\vec{b} = \\hat{i} - \\hat{j} + 2\\hat{k}$, and $\\vec{c} = 2\\hat{i} + 3\\hat{j} + \\lambda\\hat{k}$ are coplanar, the value of $\\lambda$ is:
(A) $1$  
(B) $2$  
(C) $3$  
(D) $4$  

**Q40.** An urn contains 4 red and 6 black balls. Three balls are drawn at random without replacement. The probability that exactly two of the balls drawn are red is:
(A) $3/10$  
(B) $1/2$  
(C) $3/8$  
(D) $1/3$  

**Q41.** The area bounded by the curve $y = \\sqrt{x}$, the line $y = x - 2$, and the x-axis in the first quadrant is:
(A) $\\frac{10}{3}$  
(B) $\\frac{16}{3}$  
(C) $\\frac{8}{3}$  
(D) $4$  

**Q42.** The general solution of the differential equation $\\frac{dy}{dx} = \\frac{y}{x} + \\tan\\left(\\frac{y}{x}\\right)$ is:
(A) $\\sin(y/x) = C x$  
(B) $\\cos(y/x) = C x$  
(C) $\\tan(y/x) = C x$  
(D) $\\sin(y/x) = C / x$  

---

### SECTION 2: One or More Than One Correct Option (Qs 43–48)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q43.** Let $f(x) = x^3 - 3x^2 - 9x + 5$ for all $x \\in \\mathbb{R}$:
(A) $f(x)$ has a local maximum at $x = -1$.  
(B) $f(x)$ has a local minimum at $x = 3$.  
(C) $f(x)$ has an inflection point at $x = 1$.  
(D) The local maximum value is $10$ and local minimum value is $-22$.  

**Q44.** For the hyperbola $9x^2 - 16y^2 = 144$:
(A) The coordinates of the foci are $(\\pm 5, 0)$.  
(B) The eccentricity is $5/4$.  
(C) The length of the latus rectum is $9/2$.  
(D) The asymptotes are $y = \\pm \\frac{3}{4}x$.  

**Q45.** Let $A$ be a $3 \\times 3$ orthogonal matrix ($A A^T = I$):
(A) $\\det(A) = \\pm 1$.  
(B) $A^{-1} = A^T$.  
(C) The rows of $A$ form an orthonormal basis of $\\mathbb{R}^3$.  
(D) The columns of $A$ form an orthonormal basis of $\\mathbb{R}^3$.  

**Q46.** Let $z$ be a complex number satisfying $|z - 3| + |z + 3| = 10$:
(A) The locus of $z$ in the complex plane is an ellipse.  
(B) The foci of the ellipse are at $z = \\pm 3$.  
(C) The length of the major axis is $10$.  
(D) The length of the minor axis is $8$.  

**Q47.** Let $f(x) = \\int_{0}^{x} \\frac{\\sin t}{t}\\,dt$ for $x > 0$:
(A) $f'(x) = \\frac{\\sin x}{x}$.  
(B) $f(x)$ has local extrema at $x = n\\pi$ ($n = 1, 2, 3, \\dots$).  
(C) $f(x)$ has local maxima at $x = \\pi, 3\\pi, 5\\pi, \\dots$.  
(D) $f(x)$ has local minima at $x = 2\\pi, 4\\pi, 6\\pi, \\dots$.  

**Q48.** For any three vectors $\\vec{a}, \\vec{b}, \\vec{c}$ in $\\mathbb{R}^3$:
(A) $[\\vec{a} \\; \\vec{b} \\; \\vec{c}] = \\vec{a} \\cdot (\\vec{b} \\times \\vec{c})$.  
(B) $\\vec{a} \\times (\\vec{b} \\times \\vec{c}) = (\\vec{a} \\cdot \\vec{c})\\vec{b} - (\\vec{a} \\cdot \\vec{b})\\vec{c}$.  
(C) $[\\vec{a} + \\vec{b} \\quad \\vec{b} + \\vec{c} \\quad \\vec{c} + \\vec{a}] = 2 [\\vec{a} \\; \\vec{b} \\; \\vec{c}]$.  
(D) $[\\vec{a} - \\vec{b} \\quad \\vec{b} - \\vec{c} \\quad \\vec{c} - \\vec{a}] = 0$.  

---

### SECTION 3: Numerical Value Questions (Qs 49–54)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q49.** The value of the limit
$$L = \\lim_{x \\to 0} \\frac{\\ln(1 + 3x)}{\\sin 2x}$$
is:  

**Q50.** The number of distinct real roots of the equation $x^3 - 3x^2 + 3x - 2 = 0$ is:  

**Q51.** The slope of the tangent to the curve $y = e^{2x}$ at $x = 0$ is:  

**Q52.** The value of the definite integral $\\int_{0}^{1} \\frac{2x}{1 + x^2}\\,dx$ is: (Round to two decimal places, $\\ln 2 \\approx 0.693$)  

**Q53.** The distance between the parallel planes $2x - y + 2z = 4$ and $2x - y + 2z = 10$ is:  

**Q54.** The value of the determinant $\\begin{vmatrix} 1 & 1 & 1 \\\\ 1 & 2 & 3 \\\\ 1 & 3 & 6 \\end{vmatrix}$ is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(p1_content)
print("Generated mock_tests/Mock_13_IIT_Kharagpur/Paper_1.md")

