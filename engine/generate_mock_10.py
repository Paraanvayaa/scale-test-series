import os

MOCK_DIR = os.path.join("mock_tests", "Mock_10_IIT_Kanpur")
os.makedirs(MOCK_DIR, exist_ok=True)

# ----------------------------------------------------
# PAPER 1
# ----------------------------------------------------
p1_content = """# JEE (Advanced) Mock Examination 10
### Organising Institute Style: IIT Kanpur (`IIT_KANPUR_STYLE`)
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

**Q1.** A particle of mass $m = 0.5\\text{ kg}$ moves in a medium where the retarding drag force is proportional to the square of its speed: $F_d = -b v^2$, where $b = 0.2\\text{ kg/m}$. If the particle starts with an initial speed $v_0 = 20\\text{ m/s}$ at $t = 0$, the distance $x$ (in meters) traversed by the particle by the time its speed drops to $5\\text{ m/s}$ is:
(A) $3.47\\text{ m}$  
(B) $4.25\\text{ m}$  
(C) $5.12\\text{ m}$  
(D) $6.84\\text{ m}$  

**Q2.** A non-uniform thin rod of length $L = 1.0\\text{ m}$ lies along the x-axis from $x = 0$ to $x = L$. Its linear mass density varies as $\\lambda(x) = \\lambda_0 (1 + x/L)$. The distance of the center of mass of the rod from the end $x = 0$ is:
(A) $\\frac{5}{9}L$  
(B) $\\frac{7}{12}L$  
(C) $\\frac{3}{5}L$  
(D) $\\frac{2}{3}L$  

**Q3.** An electric dipole with dipole moment $\\vec{p} = p_0 \\hat{i}$ is placed at the origin. A point charge $+q$ is located at a distance $r$ on the y-axis (broadside-on position). The magnitude and direction of the electrostatic force exerted on the point charge $+q$ are:
(A) $\\frac{1}{4\\pi\\varepsilon_0}\\frac{p_0 q}{r^3} (-\\hat{i})$  
(B) $\\frac{1}{4\\pi\\varepsilon_0}\\frac{2 p_0 q}{r^3} (+\\hat{i})$  
(C) $\\frac{1}{4\\pi\\varepsilon_0}\\frac{p_0 q}{r^3} (+\\hat{j})$  
(D) $\\frac{1}{4\\pi\\varepsilon_0}\\frac{p_0 q}{r^2} (-\\hat{i})$  

**Q4.** A long solenoid of radius $R = 5.0\\text{ cm}$ has $n = 1000\\text{ turns/m}$ and carries a time-varying current $I(t) = I_0 \\alpha t$, where $I_0 = 2.0\\text{ A}$ and $\\alpha = 50\\text{ s}^{-1}$. The induced electric field $E$ at a radial distance $r = 10.0\\text{ cm}$ from the central axis of the solenoid is:
(A) $1.57\\times 10^{-4}\\text{ V/m}$  
(B) $3.14\\times 10^{-4}\\text{ V/m}$  
(C) $6.28\\times 10^{-4}\\text{ V/m}$  
(D) $7.85\\times 10^{-4}\\text{ V/m}$  

**Q5.** In a heat transfer experiment, a metal sphere of radius $r$ cools in ambient air at temperature $T_0$ according to Newton's law of cooling: $\\frac{dT}{dt} = -k (T - T_0)$. The cooling constant $k$ is inversely proportional to:
(A) $r$  
(B) $r^2$  
(C) $\\sqrt{r}$  
(D) $r^3$  

**Q6.** In a hydrogen atom, the electron is in a state described by the principal quantum number $n = 4$. If relativistic corrections are neglected, the maximum orbital angular momentum of the electron (in units of $\\hbar$) is:
(A) $\\sqrt{6}$  
(B) $\\sqrt{12}$  
(C) $3$  
(D) $4$  

---

### SECTION 2: One or More Than One Correct Option (Qs 7–12)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q7.** A block of mass $M$ rests on a frictionless horizontal floor. A small block of mass $m$ is placed on top of $M$. The coefficient of static and kinetic friction between the blocks is $\\mu$. A horizontal force $F$ is applied to the upper block $m$:
(A) The two blocks move together without slipping if $F \\le \\mu m g \\left(1 + \\frac{m}{M}\\right)$.  
(B) When the blocks move together with common acceleration $a$, the static friction force acting on $M$ is $\\frac{M F}{m + M}$.  
(C) If $F > \\mu m g \\left(1 + \\frac{m}{M}\\right)$, the acceleration of $M$ is strictly $\\frac{\\mu m g}{M}$.  
(D) The work done by friction on the two-block system is negative whenever slipping occurs.  

**Q8.** A cylindrical container of radius $R$ filled with an incompressible liquid of density $\\rho$ to a height $H$ is rotated about its central vertical axis with constant angular velocity $\\omega$:
(A) The free surface of the liquid assumes the shape of a paraboloid of revolution given by $z(r) = z_0 + \\frac{\\omega^2 r^2}{2g}$.  
(B) The difference in height between the liquid at the perimeter and at the center is $\\frac{\\omega^2 R^2}{2g}$.  
(C) The pressure at the bottom of the container at radius $r$ is $P(r) = P_0 + \\rho g z_0 + \\frac{1}{2}\\rho \\omega^2 r^2$.  
(D) The total volume of the liquid remains conserved, so $z_0 = H - \\frac{\\omega^2 R^2}{4g}$.  

**Q9.** Two identical planar circular coils, each of radius $R$ and carrying steady current $I$ in the same direction, are arranged coaxially separated by a distance equal to their radius $R$ (Helmholtz coil configuration):
(A) The magnetic field at the midpoint on the common axis is $B = \\left(\\frac{4}{5}\\right)^{3/2} \\frac{\\mu_0 I}{R}$.  
(B) The first derivative of the magnetic field with respect to axial coordinate $z$ vanishes at the midpoint ($dB/dz = 0$).  
(C) The second derivative of the magnetic field with respect to axial coordinate $z$ vanishes at the midpoint ($d^2B/dz^2 = 0$).  
(D) The magnetic field in the vicinity of the midpoint is extraordinarily uniform.  

**Q10.** A sample of an ideal monoatomic gas undergoes a thermodynamic process wherein its molar heat capacity varies with absolute temperature as $C = C_v + \\alpha T$, where $\\alpha$ is a positive constant:
(A) The heat absorbed by $n$ moles of gas when temperature increases from $T_1$ to $T_2$ is $n C_v (T_2 - T_1) + \\frac{1}{2} n \\alpha (T_2^2 - T_1^2)$.  
(B) The equation of the process in terms of $T$ and $V$ is $T e^{\\alpha T / R} V^{2/3} = \\text{constant}$.  
(C) The work done by the gas in this process is strictly less than the heat supplied.  
(D) The change in entropy of the gas between temperatures $T_1$ and $T_2$ is $n C_v \\ln(T_2/T_1) + n \\alpha (T_2 - T_1)$.  

**Q11.** In an interference pattern formed by two coherent monochromatic slit sources with unequal field amplitudes $E_1$ and $E_2$ ($E_1 > E_2$):
(A) The visibility of the interference fringes is $\\mathcal{V} = \\frac{2 E_1 E_2}{E_1^2 + E_2^2}$.  
(B) The minimum intensity in the pattern is strictly greater than zero.  
(C) If $E_1 = 3 E_2$, the fringe visibility is $\\mathcal{V} = 0.60$.  
(D) The ratio of maximum intensity to minimum intensity is $\\left(\\frac{E_1 + E_2}{E_1 - E_2}\\right)^2$.  

**Q12.** An alpha particle of kinetic energy $K_\\alpha = 5.0\\text{ MeV}$ is scattered head-on by a heavy gold nucleus ($Z = 79$):
(A) The distance of closest approach is $r_0 = \\frac{1}{4\\pi\\varepsilon_0}\\frac{2 Z e^2}{K_\\alpha}$.  
(B) The distance of closest approach is approximately $4.55\\times 10^{-14}\\text{ m}$.  
(C) At the point of closest approach, the electrostatic potential energy equals the initial kinetic energy.  
(D) If the kinetic energy of the alpha particle is doubled, the distance of closest approach is halved.  

---

### SECTION 3: Numerical Value Questions (Qs 13–18)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q13.** A uniform thin disc of mass $M = 4.0\\text{ kg}$ and radius $R = 0.5\\text{ m}$ is rotating freely about its fixed central axis with angular velocity $\\omega_0 = 12.0\\text{ rad/s}$. A small lump of sticky clay of mass $m = 1.0\\text{ kg}$ is dropped gently onto the rim of the disc and sticks to it. The new angular velocity of the disc (in rad/s) is:  

**Q14.** In an RC discharging circuit, a capacitor of capacitance $C = 20\\,\\mu\\text{F}$ charged to $V_0 = 50\\text{ V}$ is discharged through a resistor $R = 50\\text{ k}\\Omega$. The time taken (in seconds) for the potential difference across the capacitor to decrease to $18.4\\text{ V}$ (which is $V_0/e$) is:  

**Q15.** A capillary tube of internal radius $r = 0.25\\text{ mm}$ is dipped vertically in mercury (density $\\rho = 13600\\text{ kg/m}^3$, surface tension $T = 0.544\\text{ N/m}$, contact angle $\\theta = 135^\\circ$). Taking $g = 9.8\\text{ m/s}^2$ and $\\cos 135^\\circ = -1/\\sqrt{2} \\approx -0.707$, the depression of mercury inside the capillary (in cm) is (round to two decimal places):  

**Q16.** A particle executes simple harmonic motion with time period $T = 12.0\\text{ s}$ and amplitude $A = 10.0\\text{ cm}$. The time taken (in seconds) by the particle to travel from the equilibrium position $x = 0$ to $x = 5.0\\text{ cm}$ is:  

**Q17.** A potential difference of $V = 100\\text{ V}$ is applied across an X-ray tube. The minimum wavelength (cutoff wavelength) of the continuous X-rays produced (in picometers, pm) is ($hc/e = 1240\\text{ V}\\cdot\\text{nm}$, $1\\text{ nm} = 1000\\text{ pm}$):  

**Q18.** A circular wire loop of radius $r = 5.0\\text{ cm}$ and resistance $R = 0.2\\,\\Omega$ is placed perpendicular to a magnetic field that collapses from $B_0 = 2.0\\text{ T}$ to $0$ uniformly in $\\Delta t = 0.05\\text{ s}$. The total thermal energy dissipated in the loop (in milliJoules, mJ) is (take $\\pi \\approx 3.14$, round to nearest integer):  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: Single Correct Option (Qs 19–24)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q19.** An amphiprotic salt $\\text{NaHA}$ dissolves in water to form a $0.10\\text{ M}$ solution. If $K_{a1} = 1.0\\times 10^{-4}$ and $K_{a2} = 1.0\\times 10^{-9}$ for the diprotic acid $\\text{H}_2\\text{A}$, the pH of the $\\text{NaHA}$ solution is:
(A) $4.00$  
(B) $5.50$  
(C) $6.50$  
(D) $9.00$  

**Q20.** For the second-order gas-phase dimerization $2A(g) \\rightarrow A_2(g)$, the initial pressure is $P_0 = 1.0\\text{ bar}$. If the half-life of the reaction is $100\\text{ seconds}$, the total pressure of the reaction mixture at $t = 100\\text{ seconds}$ is:
(A) $0.50\\text{ bar}$  
(B) $0.75\\text{ bar}$  
(C) $0.67\\text{ bar}$  
(D) $0.25\\text{ bar}$  

**Q21.** In the qualitative analysis of acidic radicals, when a salt is heated with concentrated $\\text{H}_2\\text{SO}_4$ and copper turnings, reddish-brown fumes are evolved that turn starch-iodide paper blue. The acidic radical present is:
(A) $\\text{Br}^-$  
(B) $\\text{NO}_3^-$  
(C) $\\text{NO}_2^-$  
(D) $\\text{CH}_3\\text{COO}^-$  

**Q22.** Treatment of $(R)$-butan-2-ol with p-toluenesulfonyl chloride ($\\text{TsCl}$) in pyridine produces compound $X$. Subsequent reaction of $X$ with potassium cyanide ($\\text{KCN}$) in DMF gives compound $Y$. The absolute configuration of compound $Y$ is:
(A) $(R)$  
(B) $(S)$  
(C) Racemic mixture  
(D) Optically inactive meso  

**Q23.** The spin-only magnetic moment of $[\\text{Co}(\\text{H}_2\\text{O})_6]^{2+}$ is $3.87\\text{ BM}$, whereas that of $[\\text{Co}(\\text{CN})_6]^{4-}$ is $1.73\\text{ BM}$. The numbers of unpaired electrons in these two complexes are respectively:
(A) $3$ and $1$  
(B) $3$ and $3$  
(C) $1$ and $1$  
(D) $4$ and $2$  

**Q24.** When excess potassium iodide solution is added to a solution of copper sulfate, a white precipitate $P$ is formed along with a brown solution $Q$. The white precipitate $P$ and brown solution $Q$ are:
(A) $\\text{CuI}_2$ and $\\text{I}_2$  
(B) $\\text{Cu}_2\\text{I}_2$ (or $\\text{CuI}$) and $\\text{I}_3^-$  
(C) $\\text{CuSO}_4$ and $\\text{K}_2\\text{SO}_4$  
(D) $\\text{Cu(OH)}_2$ and $\\text{KIO}_3$  

---

### SECTION 2: One or More Than One Correct Option (Qs 25–30)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q25.** A galvanic cell consists of a hydrogen electrode and a standard calomel electrode ($E_{\\text{calomel}} = +0.28\\text{ V}$). If the cell EMF is $E_{\\text{cell}} = 0.58\\text{ V}$ at $298\\text{ K}$ with $P_{\\text{H}_2} = 1\\text{ bar}$:
(A) The potential of the hydrogen electrode is $-0.30\\text{ V}$.  
(B) The pH of the acidic solution at the hydrogen electrode is $5.0$.  
(C) If the $\\text{H}^+$ concentration is increased, the cell EMF decreases.  
(D) The hydrogen electrode acts as the anode.  

**Q26.** Regarding the thermodynamics of mixing of non-ideal liquid solutions showing positive deviation from Raoult's law (e.g. ethanol + cyclohexane):
(A) $\\Delta H_{\\text{mix}} > 0$ (endothermic mixing).  
(B) $\\Delta V_{\\text{mix}} > 0$ (expansion on mixing).  
(C) The intermolecular attractive forces between unlike molecules ($A-B$) are weaker than those between like molecules ($A-A$ and $B-B$).  
(D) The mixture forms a minimum boiling azeotrope.  

**Q27.** Which of the following statements is/are correct concerning the chemistry of lanthanoids?
(A) The general oxidation state of lanthanoids is $+3$.  
(B) $\\text{Eu}^{2+}$ is a strong reducing agent because it achieves the stable half-filled $4f^7$ configuration.  
(C) $\\text{Ce}^{4+}$ is a good analytical oxidizing agent, converting to the stable $+3$ state.  
(D) Due to lanthanoid contraction, the atomic and ionic radii of zirconium ($\\text{Zr}$) and hafnium ($\\text{Hf}$) are almost identical.  

**Q28.** In the aldol reaction of acetone with benzaldehyde in the presence of dilute $\\text{NaOH}$ (Claisen-Schmidt condensation):
(A) Benzaldehyde has no $\\alpha$-hydrogens, so it acts exclusively as the electrophile.  
(B) Acetone forms the enolate nucleophile.  
(C) The major dehydration product is 4-phenylbut-3-en-2-one (benzalacetone).  
(D) Further reaction with another molecule of benzaldehyde yields dibenzalacetone.  

**Q29.** In the simultaneous equilibrium of two sparingly soluble salts $AgCl$ ($K_{sp1} = 1.6\\times 10^{-10}$) and $AgBr$ ($K_{sp2} = 5.0\\times 10^{-13}$) in water:
(A) $[\\text{Cl}^-] / [\\text{Br}^-] = K_{sp1} / K_{sp2} = 320$.  
(B) The solubility of $\\text{AgCl}$ is suppressed by the presence of $\\text{AgBr}$.  
(C) $[\\text{Ag}^+] = \\sqrt{K_{sp1} + K_{sp2}}$.  
(D) The precipitation of $\\text{AgBr}$ occurs at a lower silver ion concentration than $\\text{AgCl}$.  

**Q30.** For the conversion of an alkyne into a trans-alkene:
(A) Birch reduction using $\\text{Na} / \\text{liquid } \\text{NH}_3$ at $-33^\\circ\\text{C}$ gives the trans-alkene stereoselectively.  
(B) Catalytic hydrogenation over Lindlar's catalyst gives the cis-alkene.  
(C) Birch reduction proceeds via radical anion and radical intermediates with anti-addition of hydrogen.  
(D) Terminal alkynes cannot be reduced to trans-alkenes by Birch reduction due to acetylide salt formation.  

---

### SECTION 3: Numerical Value Questions (Qs 31–36)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q31.** At $298\\text{ K}$, the solubility product of $\\text{Fe(OH)}_3$ is $K_{sp} = 1.0\\times 10^{-38}$. The minimum pH required to initiate the precipitation of $\\text{Fe(OH)}_3$ from a $1.0\\times 10^{-2}\\text{ M}$ solution of $\\text{FeCl}_3$ is:  

**Q32.** In a face-centered cubic lattice of an alloy containing atoms $A$ and $B$, atoms $A$ occupy all the corners and atoms $B$ occupy all the face centers. If one atom of $B$ is missing from one of the face centers, the stoichiometric formula of the alloy is $A B_x$. The numerical value of $x$ is:  

**Q33.** For a first-order parallel reaction where reactant $A$ decomposes simultaneously to $B$ (rate constant $k_1 = 1.2\\times 10^{-3}\\text{ s}^{-1}$) and $C$ (rate constant $k_2 = 3.6\\times 10^{-3}\\text{ s}^{-1}$), the percentage yield of product $C$ is:  

**Q34.** An organic compound has molecular mass $122\\text{ g/mol}$. Combustion analysis shows $78.7\\%\\text{ C}, 8.2\\%\\text{ H}$, and $13.1\\%\\text{ O}$ by mass. The number of $\\pi$-bonds present in one molecule of this aromatic compound is:  

**Q35.** The standard reduction potentials are $E^\\circ(\\text{MnO}_4^-/\\text{Mn}^{2+}) = +1.51\\text{ V}$ and $E^\\circ(\\text{Cl}_2/\\text{Cl}^-) = +1.36\\text{ V}$. The standard EMF $E^\\circ$ (in Volts) for the reaction $2\\text{MnO}_4^- + 10\\text{Cl}^- + 16\\text{H}^+ \\rightarrow 2\\text{Mn}^{2+} + 5\\text{Cl}_2 + 8\\text{H}_2\\text{O}$ is:  

**Q36.** The total number of unpaired electrons in $[\\text{FeF}_6]^{3-}$ according to crystal field theory is:  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 37–42)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q37.** The value of the definite integral
$$I = \\int_{0}^{1} x (1 - x)^5\\,dx$$
is:
(A) $\\frac{1}{42}$  
(B) $\\frac{1}{30}$  
(C) $\\frac{1}{56}$  
(D) $\\frac{1}{20}$  

**Q38.** The number of distinct real roots of the equation $x^3 - 3x + 1 = 0$ is:
(A) $1$  
(B) $2$  
(C) $3$  
(D) $0$  

**Q39.** If the lines $\\frac{x - 1}{2} = \\frac{y + 1}{3} = \\frac{z - 1}{4}$ and $\\frac{x - 3}{1} = \\frac{y - k}{2} = \\frac{z}{1}$ intersect, then the value of $k$ is:
(A) $9/2$  
(B) $3/2$  
(C) $-3/2$  
(D) $-9/2$  

**Q40.** An urn contains 5 red and 5 black balls. A ball is drawn at random, its color is noted, and it is replaced along with 2 additional balls of the same color. A second ball is now drawn. The probability that the second ball drawn is red is:
(A) $1/2$  
(B) $5/12$  
(C) $7/12$  
(D) $1/3$  

**Q41.** The area bounded by the curve $y = 4 - x^2$ and the x-axis is:
(A) $\\frac{16}{3}$  
(B) $\\frac{32}{3}$  
(C) $\\frac{8}{3}$  
(D) $16$  

**Q42.** The general solution of the differential equation $\\frac{dy}{dx} + 2y = e^{-x}$ is:
(A) $y = e^{-x} + C e^{-2x}$  
(B) $y = e^{-2x} + C e^{-x}$  
(C) $y = x e^{-x} + C$  
(D) $y = e^{-x} + C$  

---

### SECTION 2: One or More Than One Correct Option (Qs 43–48)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q43.** Let $f(x) = x^3 - 3x + 2$. Which of the following statements is/are correct?
(A) $f(x)$ has a local maximum at $x = -1$.  
(B) $f(x)$ has a local minimum at $x = 1$.  
(C) The equation $f(x) = 0$ has a double root at $x = 1$.  
(D) $f(x) \\ge 0$ for all $x \\ge -2$.  

**Q44.** For the hyperbola $\\frac{x^2}{9} - \\frac{y^2}{16} = 1$:
(A) The eccentricity is $5/3$.  
(B) The coordinates of the foci are $(\\pm 5, 0)$.  
(C) The equations of the directrices are $x = \\pm 9/5$.  
(D) The length of the latus rectum is $32/3$.  

**Q45.** Let $A$ be a $3 \\times 3$ real symmetric matrix whose characteristic equation is $\\lambda^3 - 6\\lambda^2 + 11\\lambda - 6 = 0$:
(A) $\\det(A) = 6$.  
(B) $\\text{tr}(A) = 6$.  
(C) $A$ is invertible.  
(D) $A$ has three distinct positive eigenvalues $\\lambda = 1, 2, 3$.  

**Q46.** Let $z$ be a complex number satisfying $|z - 1| = 1$:
(A) The locus of $z$ is a circle passing through the origin.  
(B) $\\arg(z) \\in (-\\pi/2, \\pi/2)$ for $z \\ne 0$.  
(C) $|z|^2 = 2\\text{Re}(z)$.  
(D) $|z| \\le 2$.  

**Q47.** Let $f(x)$ be twice differentiable on $[a, b]$ such that $f(a) = f(b) = 0$ and $f''(x) < 0$ for all $x \\in (a, b)$:
(A) $f(x) > 0$ for all $x \\in (a, b)$.  
(B) $f(x)$ attains its absolute maximum at a unique point in $(a, b)$.  
(C) There exists a unique point $c \\in (a, b)$ such that $f'(c) = 0$.  
(D) The graph of $y = f(x)$ is strictly concave downward on $(a, b)$.  

**Q48.** Let $\\vec{a}, \\vec{b}, \\vec{c}$ be three vectors such that $\\vec{a} \\times \\vec{b} = \\vec{c}$ and $\\vec{b} \\times \\vec{c} = \\vec{a}$:
(A) $\\vec{a}, \\vec{b}, \\vec{c}$ are mutually perpendicular.  
(B) $|\\vec{a}| = |\\vec{c}|$.  
(C) If $\\vec{a} \\ne \\vec{0}$, then $|\\vec{b}| = 1$.  
(D) $[\\vec{a} \\; \\vec{b} \\; \\vec{c}] = |\\vec{a}|^2$.  

---

### SECTION 3: Numerical Value Questions (Qs 49–54)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q49.** The value of the limit
$$L = \\lim_{x \\to 0} \\frac{e^{x^2} - \\cos x}{x^2}$$
is: (Round to one decimal place)  

**Q50.** The number of distinct real roots of the equation $2x^3 - 3x^2 - 12x + 20 = 0$ is:  

**Q51.** The slope of the tangent to the curve $x^2 + y^2 = 25$ at the point $(3, 4)$ is:  

**Q52.** The value of the definite integral $\\int_{0}^{2} |x - 1|\\,dx$ is:  

**Q53.** The perpendicular distance from the origin to the plane $2x + 3y + 6z = 14$ is:  

**Q54.** The value of the determinant $\\begin{vmatrix} 1 & 2 & 3 \\\\ 0 & 4 & 5 \\\\ 0 & 0 & 6 \\end{vmatrix}$ is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(p1_content)
print("Generated mock_tests/Mock_10_IIT_Kanpur/Paper_1.md")

