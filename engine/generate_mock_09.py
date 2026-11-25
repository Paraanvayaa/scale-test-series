import os

MOCK_DIR = os.path.join("mock_tests", "Mock_09_IIT_Guwahati")
os.makedirs(MOCK_DIR, exist_ok=True)

# ----------------------------------------------------
# PAPER 1
# ----------------------------------------------------
p1_content = """# JEE (Advanced) Mock Examination 09
### Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
### Paper 1 · Full Syllabus · Total Marks: 180 · Duration: 3 Hours

---

## Instructions
- This paper consists of **54 questions** across three subjects: **Physics (Qs 1–18)**, **Chemistry (Qs 19–36)**, and **Mathematics (Qs 37–54)**.
- Each subject contains three sections:
  - **Section 1**: 6 Single Correct Option Questions (+3, -1, 0)
  - **Section 2**: 6 One or More Than One Correct Option Questions (+4, -2, 0; Partial marking: +3, +2, +1)
  - **Section 3**: 6 Numerical Value Questions (+3, 0; rounded to two decimal places or exact integer)

---

# PART I: PHYSICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 1–6)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q1.** A conducting bar of mass $m$ and length $L$ slides without friction down two parallel inclined conducting rails separated by distance $L$. The rails make an angle $\\theta$ with the horizontal and have negligible resistance. A uniform vertical magnetic field $\\vec{B} = B \\hat{k}$ is applied everywhere. The rails are connected at the bottom through a resistor $R$. The terminal velocity $v_t$ of the bar is:
(A) $\\frac{m g R \\sin\\theta}{B^2 L^2 \\cos^2\\theta}$  
(B) $\\frac{m g R \\sin\\theta}{B^2 L^2}$  
(C) $\\frac{m g R \\cos\\theta}{B^2 L^2 \\sin^2\\theta}$  
(D) $\\frac{m g R \\tan\\theta}{B^2 L^2}$  

**Q2.** An ideal monoatomic gas undergoes an adiabatic process in which its pressure is proportional to the cube of its absolute temperature ($P \\propto T^3$). The value of $\\gamma = C_p/C_v$ for this gas process corresponds to:
(A) $4/3$  
(B) $3/2$  
(C) $5/3$  
(D) $7/5$  

**Q3.** A small block of mass $m$ is released from rest at the top of a smooth hemispherical bowl of radius $R$ fixed on a horizontal table. The angle $\\theta$ with the vertical at which the block loses contact with the bowl is:
(A) $\\arccos(1/3)$  
(B) $\\arccos(2/3)$  
(C) $\\arccos(1/2)$  
(D) $\\arccos(3/4)$  

**Q4.** In a three-slit interference experiment, the three narrow slits are parallel and equidistant with separation $d$. Light of wavelength $\\lambda$ is incident normally. The ratio of the intensity at the principal maximum to the intensity at the first secondary maximum is:
(A) $3 : 1$  
(B) $9 : 1$  
(C) $4 : 1$  
(D) $9 : 4$  

**Q5.** In a nuclear fusion reaction, two deuterons $^{2}_{1}\\text{H}$ fuse to form a $^{3}_{2}\\text{He}$ nucleus and a neutron $^{1}_{0}\\text{n}$. The masses of $^{2}_{1}\\text{H}$, $^{3}_{2}\\text{He}$, and $^{1}_{0}\\text{n}$ are $2.0141\\text{ u}$, $3.0160\\text{ u}$, and $1.0087\\text{ u}$ respectively ($1\\text{ u} = 931.5\\text{ MeV}$). The $Q$-value of the reaction is approximately:
(A) $3.26\\text{ MeV}$  
(B) $4.03\\text{ MeV}$  
(C) $17.6\\text{ MeV}$  
(D) $0.82\\text{ MeV}$  

**Q6.** A cylindrical pipe of length $L$ open at both ends has fundamental frequency $f_0$. If the pipe is dipped vertically into water up to half its length, the new fundamental frequency of the remaining air column is:
(A) $f_0 / 2$  
(B) $f_0$  
(C) $2 f_0$  
(D) $4 f_0$  

---

### SECTION 2: One or More Than One Correct Option (Qs 7–12)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q7.** A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal surface and given a purely translational velocity $v_0$ without initial rotation:
(A) Kinetic friction does negative work on the center of mass translation.  
(B) Kinetic friction does positive work on the rotational motion about the center of mass.  
(C) The total mechanical energy is conserved during the transition to pure rolling.  
(D) The final steady rolling speed of the center of mass is $\\frac{5}{7}v_0$.  

**Q8.** Two identical containers $A$ and $B$ are connected by a thin tube of negligible volume fitted with a closed valve. Container $A$ holds an ideal gas at pressure $P_1$ and temperature $T_1$, while $B$ holds the same gas at pressure $P_2$ and temperature $T_2$. The valve is opened and the system reaches thermal and mechanical equilibrium at temperature $T$:
(A) The final equilibrium pressure is $P = \\frac{1}{2}\\left(\\frac{P_1 T}{T_1} + \\frac{P_2 T}{T_2}\\right)$.  
(B) The total number of moles of gas is conserved.  
(C) If the containers are thermally insulated from the surroundings, the final temperature is $T = \\frac{2 T_1 T_2}{T_1 + T_2}$.  
(D) The entropy of the universe increases during this process.  

**Q9.** A non-conducting thin ring of radius $R$ carries a non-uniform linear charge density $\\lambda(\\theta) = \\lambda_0 \\cos\\theta$, where $\\theta$ is the azimuthal angle in the plane of the ring:
(A) The total electric charge on the ring is zero.  
(B) The electric potential at the center of the ring is zero.  
(C) The electric field at the center of the ring is $\\frac{\\lambda_0}{4\\varepsilon_0 R}$ directed along $\\theta = \\pi$.  
(D) The electric dipole moment of the ring has magnitude $\\pi R^2 \\lambda_0$.  

**Q10.** An electron moves in a circular orbit of radius $r$ in a uniform magnetic field $B$ perpendicular to its plane of motion:
(A) The magnetic flux enclosed by the orbit is proportional to the kinetic energy of the electron.  
(B) The magnetic dipole moment associated with the orbital motion is directly proportional to its orbital angular momentum.  
(C) The ratio of magnetic dipole moment to orbital angular momentum (gyromagnetic ratio) is $e / (2m_e)$.  
(D) The orbital frequency is independent of the orbital radius $r$ (cyclotron frequency).  

**Q11.** For an electromagnetic wave propagating in a linear non-magnetic dielectric medium of relative permittivity $\\varepsilon_r$:
(A) The phase velocity is $v = c / \\sqrt{\\varepsilon_r}$.  
(B) The refractive index is $n = \\sqrt{\\varepsilon_r}$.  
(C) The ratio of the electric field amplitude to magnetic field amplitude is $E_0 / B_0 = v$.  
(D) The energy density of the electric field equals the energy density of the magnetic field at every point.  

**Q12.** In a photoelectric experiment, when light of frequency $\\nu$ is incident on a metal surface, photoelectrons with maximum kinetic energy $K_1$ are emitted. When light of frequency $2\\nu$ is used, the maximum kinetic energy becomes $K_2$:
(A) $K_2 > 2 K_1$.  
(B) $K_2 = 2 K_1 + \\Phi$ (where $\\Phi$ is the work function).  
(C) The threshold frequency is $\\nu_0 = \\frac{2K_1 - K_2}{h}$ (if $K_2 < 2K_1$, impossible).  
(D) The work function is $\\Phi = K_2 - 2K_1$.  

---

### SECTION 3: Numerical Value Questions (Qs 13–18)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q13.** A heat engine working in a Carnot cycle absorbs $500\\text{ J}$ of heat from a source at $400\\text{ K}$ and rejects heat to a sink at $300\\text{ K}$. The net work produced per cycle (in Joules) is:  

**Q14.** In a Young's double-slit experiment, the distance between the two slits is $d = 0.2\\text{ mm}$ and the distance to the screen is $D = 1.0\\text{ m}$. The wavelength of light used is $\\lambda = 500\\text{ nm}$. The fringe width $\\beta$ (in mm) is:  

**Q15.** A uniform rod of mass $M = 3\\text{ kg}$ and length $L = 1.0\\text{ m}$ is pivoted at one end. Its moment of inertia about the pivot (in $\\text{kg}\\cdot\\text{m}^2$) is:  

**Q16.** A particle of mass $m = 1.0\\times 10^{-20}\\text{ kg}$ has a de Broglie wavelength of $\\lambda = 0.663\\text{ nm}$. The speed of the particle (in m/s) is ($h = 6.63\\times 10^{-34}\\text{ J}\\cdot\\text{s}$):  

**Q17.** A parallel plate capacitor of capacitance $C = 10\\,\\mu\\text{F}$ is charged to $100\\text{ V}$. The energy stored in the capacitor (in Joules) is:  

**Q18.** A small sphere of mass $m = 0.1\\text{ kg}$ is attached to a string of length $l = 1.0\\text{ m}$ and whirled in a horizontal circle at constant angular velocity $\\omega = 10\\text{ rad/s}$. The tension in the string (in Newtons) is:  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: Single Correct Option (Qs 19–24)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q19.** An element crystallizes in a body-centered cubic (BCC) lattice with edge length $a = 300\\text{ pm}$. The radius of the constituent atom (in pm) is:
(A) $150.0\\text{ pm}$  
(B) $129.9\\text{ pm}$  
(C) $106.1\\text{ pm}$  
(D) $86.6\\text{ pm}$  

**Q20.** For the reaction $\\text{A}(g) + 2\\text{B}(g) \\rightleftharpoons 3\\text{C}(g)$, the relation between $K_p$ and $K_c$ is:
(A) $K_p = K_c (RT)$  
(B) $K_p = K_c / (RT)$  
(C) $K_p = K_c$  
(D) $K_p = K_c (RT)^2$  

**Q21.** Which of the following complexes is paramagnetic with spin-only magnetic moment $\\approx 1.73\\text{ BM}$?
(A) $[\\text{Ni}(\\text{CN})_4]^{2-}$  
(B) $[\\text{Cu}(\\text{NH}_3)_4]^{2+}$  
(C) $[\\text{Zn}(\\text{NH}_3)_4]^{2+}$  
(D) $[\\text{Co}(\\text{NH}_3)_6]^{3+}$  

**Q22.** The major product obtained when anisole (methoxybenzene) is heated with excess concentrated hydroiodic acid ($\\text{HI}$) at $373\\text{ K}$ is:
(A) Iodobenzene and methanol  
(B) Phenol and iodomethane  
(C) Phenol and methanol  
(D) Iodobenzene and iodomethane  

**Q23.** The standard reduction potential of $\\text{Cu}^{2+}/\\text{Cu}$ is $+0.34\\text{ V}$ and that of $\\text{Ag}^+/\\text{Ag}$ is $+0.80\\text{ V}$. For the cell reaction $\\text{Cu}(s) + 2\\text{Ag}^+(aq) \\rightleftharpoons \\text{Cu}^{2+}(aq) + 2\\text{Ag}(s)$, the standard EMF $E^\\circ_{\\text{cell}}$ is:
(A) $+1.14\\text{ V}$  
(B) $+0.46\\text{ V}$  
(C) $+0.12\\text{ V}$  
(D) $-0.46\\text{ V}$  

**Q24.** The shape and hybridization of the central atom in xenon trioxide ($\\text{XeO}_3$) are respectively:
(A) Trigonal planar, $sp^2$  
(B) Pyramidal, $sp^3$  
(C) T-shaped, $sp^3d$  
(D) Tetrahedral, $sp^3$  

---

### SECTION 2: One or More Than One Correct Option (Qs 25–30)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q25.** For an ideal gas undergoing a reversible isothermal expansion:
(A) $\\Delta U = 0$.  
(B) $\\Delta H = 0$.  
(C) $q = -W = n R T \\ln(V_2/V_1)$.  
(D) $\\Delta S_{\\text{univ}} = 0$.  

**Q26.** Which of the following compounds will give a positive Tollens' test (silver mirror)?
(A) Glucose  
(B) Fructose  
(C) Formic acid ($\\text{HCOOH}$)  
(D) Benzaldehyde  

**Q27.** Consider the coordination compound $[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]\\text{Cl}$:
(A) It exhibits geometrical isomerism (cis and trans isomers).  
(B) The cis-isomer is optically active.  
(C) The trans-isomer has a center of inversion and is optically inactive.  
(D) Addition of aqueous $\\text{AgNO}_3$ precipitates 1 mole of $\\text{AgCl}$ per mole of complex.  

**Q28.** Which of the following statements is/are correct regarding the p-block hydrides?
(A) Ammonia ($\\text{NH}_3$) acts as a Lewis base due to a lone pair on the nitrogen atom.  
(B) Phosphine ($\\text{PH}_3$) is less basic than ammonia because the lone pair resides in an almost pure s-orbital (Drago's rule).  
(C) Silane ($\\text{SiH}_4$) is a stronger reducing agent than methane ($\\text{CH}_4$).  
(D) Hydrogen fluoride ($\\text{HF}$) is a weaker acid than $\\text{HCl}$ due to the higher bond dissociation enthalpy of the $\\text{H-F}$ bond.  

**Q29.** In the qualitative analysis of Group III cations ($\\text{Fe}^{3+}, \\text{Al}^{3+}, \\text{Cr}^{3+}$):
(A) Ammonium chloride ($\\text{NH}_4\\text{Cl}$) is added before ammonium hydroxide ($\\text{NH}_4\\text{OH}$).  
(B) $\\text{NH}_4\\text{Cl}$ suppresses the ionization of $\\text{NH}_4\\text{OH}$ by common ion effect.  
(C) The suppressed $[\\text{OH}^-]$ is sufficient to exceed the $K_{sp}$ of Group III hydroxides but not of subsequent groups ($\\text{Zn}^{2+}, \\text{Mg}^{2+}$).  
(D) $\\text{Al(OH)}_3$ dissolves in excess $\\text{NaOH}$ forming soluble sodium aluminate.  

**Q30.** For the nucleophilic addition-elimination reactions of carboxylic acid derivatives, the reactivity order towards nucleophiles is:
(A) Acyl chloride > Acid anhydride > Ester > Amide.  
(B) The leaving group ability decreases in the order $\\text{Cl}^- > \\text{RCOO}^- > \\text{RO}^- > \\text{NH}_2^-$.  
(C) The basicity of the leaving group increases in the order $\\text{Cl}^- < \\text{RCOO}^- < \\text{RO}^- < \\text{NH}_2^-$.  
(D) Esters are more reactive than acyl chlorides towards nucleophilic attack.  

---

### SECTION 3: Numerical Value Questions (Qs 31–36)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q31.** The number of atoms present in a single unit cell of a body-centered cubic (BCC) crystal lattice is:  

**Q32.** At $298\\text{ K}$, the pH of a $1.0\\times 10^{-3}\\text{ M}$ solution of strong monoprotic acid $\\text{HCl}$ is:  

**Q33.** The rate of a chemical reaction doubles when the concentration of reactant $A$ is quadrupled. The order of the reaction with respect to $A$ is:  

**Q34.** The boiling point elevation constant $K_b$ of water is $0.52\\text{ K}\\cdot\\text{kg/mol}$. The boiling point elevation $\\Delta T_b$ (in K) for a $0.50\\text{ m}$ solution of non-volatile solute glucose in water is (round to two decimal places):  

**Q35.** The spin-only magnetic moment of $[\\text{CoF}_6]^{3-}$ (high-spin, 4 unpaired electrons) in Bohr Magnetons (BM) is (round to two decimal places, $\\sqrt{24} \\approx 4.90$):  

**Q36.** The total number of structural isomers possible for an alkane with molecular formula $\\text{C}_5\\text{H}_{12}$ is:  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 37–42)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q37.** The value of the definite integral
$$I = \\int_{0}^{1} \\frac{dx}{1 + x^2}$$
is:
(A) $\\frac{\\pi}{4}$  
(B) $\\frac{\\pi}{2}$  
(C) $1$  
(D) $\\ln 2$  

**Q38.** The eccentricity of the ellipse $25x^2 + 16y^2 = 400$ is:
(A) $3/5$  
(B) $4/5$  
(C) $9/25$  
(D) $16/25$  

**Q39.** If $\\vec{a} = 2\\hat{i} + 3\\hat{j} + 6\\hat{k}$, the unit vector in the direction of $\\vec{a}$ is:
(A) $\\frac{1}{7}(2\\hat{i} + 3\\hat{j} + 6\\hat{k})$  
(B) $\\frac{1}{49}(2\\hat{i} + 3\\hat{j} + 6\\hat{k})$  
(C) $\\frac{1}{\\sqrt{11}}(2\\hat{i} + 3\\hat{j} + 6\\hat{k})$  
(D) $\\frac{1}{13}(2\\hat{i} + 3\\hat{j} + 6\\hat{k})$  

**Q40.** The probability of rolling a sum of 7 with two standard fair six-sided dice is:
(A) $1/6$  
(B) $5/36$  
(C) $7/36$  
(D) $1/12$  

**Q41.** The area bounded by the curve $y = x^3$, the x-axis, and the ordinates $x = 0$ and $x = 2$ is:
(A) $2$  
(B) $4$  
(C) $8$  
(D) $16$  

**Q42.** The solution of the differential equation $\\frac{dy}{dx} = \\frac{y}{x}$ with $y(1) = 2$ is:
(A) $y = 2x$  
(B) $y = x^2 + 1$  
(C) $y = 2/x$  
(D) $y = x + 1$  

---

### SECTION 2: One or More Than One Correct Option (Qs 43–48)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q43.** Let $f(x) = x^3 - 6x^2 + 9x + 1$ for all $x \\in \\mathbb{R}$:
(A) $f(x)$ has a local maximum at $x = 1$.  
(B) $f(x)$ has a local minimum at $x = 3$.  
(C) $f(x)$ is strictly increasing on $(-\\infty, 1)$ and $(3, \\infty)$.  
(D) $f(x)$ has an inflection point at $x = 2$.  

**Q44.** For the rectangular hyperbola $x^2 - y^2 = a^2$:
(A) The eccentricity is $\\sqrt{2}$.  
(B) The asymptotes are mutually perpendicular lines $y = \\pm x$.  
(C) The length of the transverse axis equals the length of the conjugate axis ($2a$).  
(D) The distance between the foci is $2a\\sqrt{2}$.  

**Q45.** Let $A$ and $B$ be two $n \\times n$ invertible matrices:
(A) $(A B)^{-1} = B^{-1} A^{-1}$.  
(B) $\\det(A B) = \\det(A) \\det(B)$.  
(C) $(A B)^T = B^T A^T$.  
(D) $\\text{tr}(A B) = \\text{tr}(B A)$.  

**Q46.** For any complex number $z = x + i y$:
(A) $|z|^2 = z \\bar{z} = x^2 + y^2$.  
(B) $\\text{Re}(z) = \\frac{z + \\bar{z}}{2}$.  
(C) $\\text{Im}(z) = \\frac{z - \\bar{z}}{2i}$.  
(D) $|z_1 + z_2| \\le |z_1| + |z_2|$ (Triangle inequality).  

**Q47.** Let $f(x) = e^x - 1 - x$ for all $x \\in \\mathbb{R}$:
(A) $f'(x) = e^x - 1$.  
(B) $f(x) \\ge 0$ for all $x \\in \\mathbb{R}$.  
(C) $e^x \\ge 1 + x$ for all $x \\in \\mathbb{R}$.  
(D) $f(x)$ attains its minimum value of $0$ at $x = 0$.  

**Q48.** Let $\\vec{u}, \\vec{v}, \\vec{w}$ be vectors in $\\mathbb{R}^3$:
(A) $\\vec{u} \\cdot (\\vec{v} \\times \\vec{w}) = \\vec{v} \\cdot (\\vec{w} \\times \\vec{u}) = \\vec{w} \\cdot (\\vec{u} \\times \\vec{v})$.  
(B) $\\vec{u} \\times \\vec{v} = -\\vec{v} \\times \\vec{u}$.  
(C) $|\\vec{u} \\times \\vec{v}|$ represents the area of the parallelogram formed by $\\vec{u}$ and $\\vec{v}$.  
(D) If $\\vec{u} \\cdot \\vec{v} = 0$ and $\\vec{u} \\times \\vec{v} = \\vec{0}$, then at least one of the vectors is zero.  

---

### SECTION 3: Numerical Value Questions (Qs 49–54)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q49.** The value of the limit
$$L = \\lim_{x \\to 0} \\frac{\\ln(1 + x)}{x}$$
is:  

**Q50.** The number of solutions of $\\sin x = 0$ in the closed interval $[0, 2\\pi]$ is:  

**Q51.** The slope of the normal to the curve $y = x^2$ at the point $(1, 1)$ is:  

**Q52.** The value of $\\int_{0}^{2} (3x^2 - 2x + 1)\\,dx$ is:  

**Q53.** The distance of the point $(0, 0, 0)$ from the plane $x + 2y + 2z = 9$ is:  

**Q54.** The value of the determinant $\\begin{vmatrix} 1 & 0 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 3 \\end{vmatrix}$ is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(p1_content)
print("Generated mock_tests/Mock_09_IIT_Guwahati/Paper_1.md")

