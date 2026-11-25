import os

MOCK_DIR = os.path.join("mock_tests", "Mock_16_IIT_Madras")
os.makedirs(MOCK_DIR, exist_ok=True)

# ----------------------------------------------------
# PAPER 1
# ----------------------------------------------------
p1_content = """# JEE (Advanced) Mock Examination 16
### Organising Institute Style: IIT Madras (`IIT_MADRAS_STYLE` — 2010 Benchmark)
### Paper 1 • Full Syllabus • Total Marks: 180 • Duration: 3 Hours

---

## Instructions
- This paper consists of **54 questions** across three subjects: **Physics (Qs 1–18)**, **Chemistry (Qs 19–36)**, and **Mathematics (Qs 37–54)**.
- Each subject contains three sections:
  - **Section 1**: 6 Single Correct Option Questions (+3, -1, 0)
  - **Section 2**: 6 One or More Than One Correct Option Questions (+4, -2, 0; Partial marking: +3, +2, +1)
  - **Section 3**: 6 Numerical Value Questions (+3, 0; decimal or integer)

---

# PART I: PHYSICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 1–6)
*Marking Scheme: +3 for correct, -1 for incorrect, 0 if unanswered.*

**Q1.** A solid metal sphere of radius $a$ is surrounded by a concentric dielectric spherical shell of inner radius $a$ and outer radius $b$, having dielectric constant $K$. If the metal sphere carries a charge $+Q$, the electric potential at its surface relative to infinity is:
(A) $\\frac{Q}{4\\pi\\varepsilon_0}\\left(\\frac{1}{K a} - \\frac{1}{K b} + \\frac{1}{b}\\right)$  
(B) $\\frac{Q}{4\\pi\\varepsilon_0}\\left(\\frac{1}{K a} + \\frac{1}{b}\\right)$  
(C) $\\frac{Q}{4\\pi\\varepsilon_0 K a}$  
(D) $\\frac{Q}{4\\pi\\varepsilon_0 b}\\left(1 + \\frac{1}{K}\\right)$  

**Q2.** A circular ring of radius $R$ and total charge $Q$ uniformly distributed rotates with constant angular speed $\\omega$ about an axis passing through its center and perpendicular to its plane. The magnetic dipole moment of the rotating ring is:
(A) $\\frac{1}{2} Q \\omega R^2$  
(B) $Q \\omega R^2$  
(C) $\\frac{1}{4} Q \\omega R^2$  
(D) $2 Q \\omega R^2$  

**Q3.** In an alternating current circuit, the instantaneous voltage and current are given by $v(t) = 200 \\sin(100\\pi t)\\text{ V}$ and $i(t) = 5.0 \\sin\\left(100\\pi t - \\frac{\\pi}{3}\\right)\\text{ A}$. The average power dissipated in the circuit over a complete cycle is:
(A) $250\\text{ W}$  
(B) $500\\text{ W}$  
(C) $1000\\text{ W}$  
(D) $125\\text{ W}$  

**Q4.** A rectangular loop of wire with dimensions $a \\times b$ carrying current $I$ is placed in a uniform magnetic field $\\vec{B} = B_0 \\hat{j}$. If the unit normal to the loop makes an angle $\\theta = 30^\\circ$ with the $+y$-axis, the magnitude of the torque acting on the loop is:
(A) $\\frac{1}{2} I a b B_0$  
(B) $\\frac{\\sqrt{3}}{2} I a b B_0$  
(C) $I a b B_0$  
(D) $\\frac{1}{4} I a b B_0$  

**Q5.** In an experiment with a compound pendulum, the period of oscillation is minimum when the distance $d$ of the knife-edge from the center of mass is equal to:
(A) The radius of gyration $k$ about the center of mass  
(B) $k/2$  
(C) $2k$  
(D) $k^2$  

**Q6.** A ray of unpolarized light is incident at Brewster's angle $\\theta_B$ on the surface of a glass plate of refractive index $\\mu = 1.732 \\approx \\sqrt{3}$. The angle of refraction inside the glass is:
(A) $30^\\circ$  
(B) $60^\\circ$  
(C) $45^\\circ$  
(D) $15^\\circ$  

---

### SECTION 2: One or More Than One Correct Option (Qs 7–12)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q7.** A uniform magnetic field $\\vec{B} = B_0 \\hat{k}$ is confined to a cylindrical region of radius $R$. The magnetic field is increasing at a constant rate $\\frac{dB}{dt} = \\alpha > 0$:
(A) The induced electric field lines form concentric circles centered on the cylinder's axis.  
(B) For $r \\le R$, the magnitude of the induced electric field is $E(r) = \\frac{1}{2} \\alpha r$.  
(C) For $r > R$, the magnitude of the induced electric field is $E(r) = \\frac{\\alpha R^2}{2 r}$.  
(D) A charged particle released from rest at any point inside the cylinder will experience a tangential acceleration.  

**Q8.** A parallel plate capacitor of capacitance $C_0$ is connected to a battery of EMF $V_0$. With the battery remaining connected, a dielectric slab of dielectric constant $K$ is introduced to completely fill the space between the plates:
(A) The potential difference across the plates remains unchanged at $V_0$.  
(B) The charge on the capacitor increases to $K C_0 V_0$.  
(C) The electrostatic energy stored in the capacitor increases by a factor of $K$.  
(D) The work done by the battery is $(K - 1) C_0 V_0^2$.  

**Q9.** For a particle executing simple harmonic motion (SHM) with amplitude $A$ and angular frequency $\\omega$:
(A) The velocity and displacement have a phase difference of $\\pi/2$.  
(B) The acceleration and displacement have a phase difference of $\\pi$.  
(C) The average kinetic energy over one full period equals the average potential energy: $\\langle K \\rangle = \\langle U \\rangle = \\frac{1}{4} m \\omega^2 A^2$.  
(D) The total mechanical energy $E = \\frac{1}{2} m \\omega^2 A^2$ is independent of time.  

**Q10.** In an ideal heat pump operating reversibly between an indoor temperature $T_H = 300\\text{ K}$ and an outdoor temperature $T_C = 250\\text{ K}$:
(A) The coefficient of performance (COP) for heating is $\\text{COP} = \\frac{T_H}{T_H - T_C} = 6.0$.  
(B) If the heat delivered to the room is $6000\\text{ J}$, the work input required is $1000\\text{ J}$.  
(C) The heat extracted from the cold outside reservoir is $5000\\text{ J}$.  
(D) The entropy of the universe remains constant during each cycle.  

**Q11.** In the Davisson-Germer experiment demonstrating electron wave nature:
(A) Electrons scattered from a nickel crystal show an intensity peak due to constructive interference.  
(B) The Bragg condition $2d \\sin\\theta = n\\lambda$ is satisfied for the lattice planes.  
(C) A peak in electron scattering intensity was observed at an accelerating potential of $54\\text{ V}$ and scattering angle $50^\\circ$.  
(D) The experiment provides direct experimental confirmation of de Broglie's wave hypothesis for matter.  

**Q12.** Two coherent sound sources $S_1$ and $S_2$ oscillate in phase:
(A) The condition for constructive interference at point $P$ is $|S_1 P - S_2 P| = n\\lambda$ ($n \\in \\mathbb{Z}$).  
(B) The condition for destructive interference at point $P$ is $|S_1 P - S_2 P| = \\left(n + \\frac{1}{2}\\right)\\lambda$.  
(C) If the amplitude of each source is $A_0$, the maximum resultant intensity is $4 I_0$.  
(D) Destructive interference produces zero intensity if the amplitudes are equal.  

---

### SECTION 3: Numerical Value Questions (Qs 13–18)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q13.** A parallel plate capacitor with plate area $A = 0.050\\text{ m}^2$ and separation $d = 1.0\\text{ mm}$ has a vacuum between the plates. It is charged to a potential difference $V = 200\\text{ V}$. The electrostatic attractive force between the plates (in milliNewtons, mN) is: (Take $\\varepsilon_0 = 8.85 \\times 10^{-12}\\text{ F/m}$, round to two decimal places)  

**Q14.** A circular coil of $N = 100\\text{ turns}$ and radius $r = 5.0\\text{ cm}$ carries a current of $I = 2.0\\text{ A}$. The magnetic field at its center (in milliTesla, mT) is: (Take $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ T}\\cdot\\text{m/A}$, $\\pi = 3.14$, round to two decimal places)  

**Q15.** A solid sphere of mass $M = 5.0\\text{ kg}$ and radius $R = 0.20\\text{ m}$ is rolling without slipping on a horizontal surface at a speed of $v = 4.0\\text{ m/s}$. The total kinetic energy of the rolling sphere (in Joules) is:  

**Q16.** In a Newton's rings experiment using light of wavelength $\\lambda = 600\\text{ nm}$, the diameter of the 4th dark ring is $4.0\\text{ mm}$. The radius of curvature of the plano-convex lens (in meters) is: (Round to two decimal places)  

**Q17.** A whistle emitting sound of frequency $500\\text{ Hz}$ is tied to a string of length $L = 1.0\\text{ m}$ and whirled in a horizontal circle at angular speed $\\omega = 20.0\\text{ rad/s}$. An observer stands far away in the plane of the circle. The difference between the maximum and minimum frequencies heard by the observer (in Hz) is: (Speed of sound $= 340.0\\text{ m/s}$, round to one decimal place)  

**Q18.** A radioactive nuclide has a decay constant $\\lambda = 0.050\\text{ s}^{-1}$. The mean lifetime $\\tau$ of this nuclide (in seconds) is:  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: Single Correct Option (Qs 19–24)
*Marking Scheme: +3 for correct, -1 for incorrect, 0 if unanswered.*

**Q19.** The molar conductance of a $0.010\\text{ M}$ aqueous solution of an electrolyte is $120.0\\text{ S}\\cdot\\text{cm}^2/\\text{mol}$. The specific conductance (conductivity $\\kappa$) of the solution (in $\\text{S/cm}$) is:
(A) $1.20 \\times 10^{-3}$  
(B) $1.20 \\times 10^{-2}$  
(C) $1.20 \\times 10^{-4}$  
(D) $1.20$  

**Q20.** Which of the following ligands is a bidentate monoanionic chelating ligand?
(A) Glycinate ion ($\\text{gly}^-$)  
(B) Ethylenediamine ($\\text{en}$)  
(C) Oxalate ion ($\\text{ox}^{2-}$)  
(D) $o$-Phenanthroline ($\\text{phen}$)  

**Q21.** An aromatic organic compound $A$ with molecular formula $\\text{C}_7\\text{H}_8\\text{O}$ is insoluble in aqueous $\\text{NaHCO}_3$ but soluble in aqueous $\\text{NaOH}$. It gives a violet coloration with neutral $\\text{FeCl}_3$ solution. On bromination with $\\text{Br}_2/\\text{FeBr}_3$, it forms a monobromo derivative. Compound $A$ is:
(A) $p$-Cresol (4-methylphenol)  
(B) $o$-Cresol (2-methylphenol)  
(C) $m$-Cresol (3-methylphenol)  
(D) Benzyl alcohol  

**Q22.** Among the alkali metal halides, the correct order of lattice enthalpy is:
(A) $\\text{LiF} > \\text{NaF} > \\text{KF} > \\text{RbF} > \\text{CsF}$  
(B) $\\text{CsF} > \\text{RbF} > \\text{KF} > \\text{NaF} > \\text{LiF}$  
(C) $\\text{LiF} > \\text{KF} > \\text{NaF} > \\text{RbF} > \\text{CsF}$  
(D) $\\text{NaF} > \\text{LiF} > \\text{KF} > \\text{RbF} > \\text{CsF}$  

**Q23.** For the reaction $2\\text{A} + \\text{B} \\rightarrow \\text{C}$, the rate law is found to be $\\text{Rate} = k [\\text{A}]^2 [\\text{B}]$. If the volume of the reaction vessel is halved at constant temperature, the rate of the reaction increases by a factor of:
(A) 8  
(B) 4  
(C) 6  
(D) 2  

**Q24.** When potassium permanganate ($\\text{KMnO}_4$) acts as an oxidizing agent in an acidic medium, the change in oxidation state of manganese is:
(A) From $+7$ to $+2$ (gain of $5e^-$)  
(B) From $+7$ to $+4$ (gain of $3e^-$)  
(C) From $+7$ to $+6$ (gain of $1e^-$)  
(D) From $+7$ to $0$ (gain of $7e^-$)  

---

### SECTION 2: One or More Than One Correct Option (Qs 25–30)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q25.** For an electrochemical cell operating reversibly at temperature $T$:
(A) $\\Delta G = -n F E_{\\text{cell}}$.  
(B) The temperature coefficient of the cell potential is $\\left(\\frac{\\partial E_{\\text{cell}}}{\\partial T}\\right)_P = \\frac{\\Delta S}{n F}$.  
(C) The enthalpy change of the cell reaction is $\\Delta H = n F \\left[T \\left(\\frac{\\partial E}{\\partial T}\\right)_P - E\\right]$.  
(D) If $\\left(\\frac{\\partial E}{\\partial T}\\right)_P > 0$, the cell absorbs heat from the surroundings during reversible discharge.  

**Q26.** Regarding the crystal field splitting in transition metal complexes:
(A) In an octahedral complex, the $d_{x^2-y^2}$ and $d_{z^2}$ orbitals are raised in energy by $+0.6 \\Delta_o$.  
(B) In a tetrahedral complex, the splitting energy satisfies $\\Delta_t \\approx \\frac{4}{9} \\Delta_o$.  
(C) Strong-field ligands (such as $\\text{CN}^-$, $\\text{CO}$) produce large splitting and favor low-spin configurations.  
(D) Weak-field ligands (such as $\\text{I}^-$, $\\text{Br}^-$, $\\text{F}^-$) produce high-spin configurations where electrons occupy $e_g$ orbitals before pairing in $t_{2g}$.  

**Q27.** Which of the following compounds will give a positive silver mirror test with Tollens' reagent?
(A) Glucose  
(B) Benzaldehyde  
(C) Fructose  
(D) Formic acid ($\\text{HCOOH}$)  

**Q28.** In the metallurgy of gold and silver using the MacArthur-Forrest cyanide process:
(A) The native ore is leached with dilute $\\text{NaCN}$ solution in the presence of air ($\\text{O}_2$).  
(B) Gold dissolves forming the soluble coordination complex $[\\text{Au}(\\text{CN})_2]^-$.  
(C) Gold is precipitated from the solution by displacement with zinc dust: $2[\\text{Au}(\\text{CN})_2]^- + \\text{Zn} \\rightarrow [\\text{Zn}(\\text{CN})_4]^{2-} + 2\\text{Au}$.  
(D) Zinc acts as a reducing agent in the displacement step.  

**Q29.** For an ideal gas expanding isothermally and reversibly from $(P_1, V_1)$ to $(P_2, V_2)$:
(A) The change in internal energy is $\\Delta U = 0$.  
(B) The work done by the gas is $W = n R T \\ln(V_2/V_1) = n R T \\ln(P_1/P_2)$.  
(C) The heat absorbed by the gas is $Q = W$.  
(D) The entropy change of the gas is $\\Delta S = n R \\ln(V_2/V_1)$.  

**Q30.** For the Group 14 elements (carbon family):
(A) Carbon exhibits maximum catenation ability due to its high $\\text{C}-\\text{C}$ bond enthalpy.  
(B) Lead shows stable $+2$ oxidation state rather than $+4$ due to the inert pair effect.  
(C) $\\text{CCl}_4$ is inert to hydrolysis at room temperature because carbon lacks vacant $d$-orbitals to accept a lone pair from water.  
(D) $\\text{SiCl}_4$ hydrolyzes rapidly in water to form silicic acid $\\text{Si(OH)}_4$.  

---

### SECTION 3: Numerical Value Questions (Qs 31–36)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q31.** The standard potential of the cell $\\text{Zn}|\\text{Zn}^{2+}||\\text{Ag}^+|\\text{Ag}$ is $E^\\circ = 1.56\\text{ V}$. Given $E^\\circ_{\\text{Zn}^{2+}/\\text{Zn}} = -0.76\\text{ V}$, the standard reduction potential of the $\\text{Ag}^+/\\text{Ag}$ electrode (in Volts) is: (Round to two decimal places)  

**Q32.** An aqueous solution of ammonium hydroxide ($\\text{NH}_4\\text{OH}$, $K_b = 1.8 \\times 10^{-5}$) has concentration $0.10\\text{ M}$. The pOH of the solution is: (Use $\\log_{10} 1.34 = 0.127$, round to two decimal places)  

**Q33.** A metal with atomic weight $108.0\\text{ g/mol}$ crystallizes in a simple cubic structure with unit cell edge length $a = 3.0 \\times 10^{-8}\\text{ cm}$. The density of the metal (in $\\text{g/cm}^3$) is: ($N_A = 6.02 \\times 10^{23}\\text{ mol}^{-1}$, round to one decimal place)  

**Q34.** The half-life of a radioactive isotope is $20.0\\text{ days}$. The time taken (in days) for $75.0\\%$ of the sample to decay is:  

**Q35.** A solution containing $6.0\\text{ g}$ of urea ($M = 60.0\\text{ g/mol}$) in $500\\text{ g}$ of water freezes at $-T_f^\\circ$. Given $K_f(\\text{H}_2\\text{O}) = 1.86\\text{ K}\\cdot\\text{kg/mol}$, the freezing point depression $\\Delta T_f$ (in Kelvin, K) is: (Round to two decimal places)  

**Q36.** The solubility product of lead(II) chloride ($\\text{PbCl}_2$) is $K_{sp} = 1.6 \\times 10^{-5}$ at $298\\text{ K}$. The molar solubility of $\\text{PbCl}_2$ in pure water (in mmol/L, $10^{-3}\\text{ M}$) is: (Take $(4.0)^{1/3} = 1.59$, round to one decimal place)  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 37–42)
*Marking Scheme: +3 for correct, -1 for incorrect, 0 if unanswered.*

**Q37.** Let $z = x + iy$ be a complex number satisfying $\\left|\\frac{z - i}{z + i}\\right| = 1$. The locus of $z$ in the complex plane is:
(A) The real axis ($y = 0$)  
(B) The imaginary axis ($x = 0$)  
(C) The circle $x^2 + y^2 = 1$  
(D) The line $y = 1$  

**Q38.** The value of the definite integral
$$I = \\int_{0}^{1} x (1 - x)^9\\,dx$$
is:
(A) $\\frac{1}{110}$  
(B) $\\frac{1}{90}$  
(C) $\\frac{1}{100}$  
(D) $\\frac{1}{120}$  

**Q39.** The condition that the line $y = mx + c$ is a tangent to the parabola $y^2 = 4ax$ is:
(A) $c = \\frac{a}{m}$  
(B) $c = a m$  
(C) $c = -a m^2$  
(D) $c = \\frac{a}{m^2}$  

**Q40.** The solution of the differential equation
$$x\\,dy - y\\,dx = 0$$
represents a family of:
(A) Straight lines passing through the origin  
(B) Circles centered at the origin  
(C) Parabolas with vertex at the origin  
(D) Hyperbolas with center at the origin  

**Q41.** The number of four-digit numbers greater than 5000 that can be formed using the digits $2, 4, 5, 7, 8$ without repetition is:
(A) 72  
(B) 48  
(C) 96  
(D) 120  

**Q42.** The perpendicular distance of the origin from the plane $2x - 3y + 6z - 14 = 0$ is:
(A) 2  
(B) 3  
(C) 1  
(D) 4  

---

### SECTION 2: One or More Than One Correct Option (Qs 43–48)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q43.** Let $f(x) = \\frac{x}{1 + x^2}$ for all $x \\in \\mathbb{R}$:
(A) $f(x)$ is an odd function.  
(B) The maximum value of $f(x)$ is $1/2$, attained at $x = 1$.  
(C) The minimum value of $f(x)$ is $-1/2$, attained at $x = -1$.  
(D) The range of $f(x)$ is $[-1/2, 1/2]$.  

**Q44.** For the ellipse $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ ($a > b$):
(A) The sum of the focal distances of any point on the ellipse is constant and equal to $2a$.  
(B) The locus of the foot of the perpendicular from either focus onto any tangent is the auxiliary circle $x^2 + y^2 = a^2$.  
(C) The product of the perpendicular distances from the two foci onto any tangent is constant and equal to $b^2$.  
(D) The director circle of the ellipse is $x^2 + y^2 = a^2 + b^2$.  

**Q45.** Let $A$ and $B$ be two $3 \\times 3$ matrices:
(A) $\\det(A^T) = \\det(A)$.  
(B) If $A$ is skew-symmetric, $\\det(A) = 0$.  
(C) $\\text{tr}(A B) = \\text{tr}(B A)$.  
(D) $\\det(k A) = k^3 \\det(A)$ for any scalar $k$.  

**Q46.** Let $\\vec{a}, \\vec{b}$ be two unit vectors making an angle $\\theta$ with each other:
(A) $|\\vec{a} + \\vec{b}| = 2\\cos(\\theta/2)$.  
(B) $|\\vec{a} - \\vec{b}| = 2\\sin(\\theta/2)$.  
(C) $(\\vec{a} + \\vec{b}) \\cdot (\\vec{a} - \\vec{b}) = 0$.  
(D) The vectors $\\vec{a} + \\vec{b}$ and $\\vec{a} - \\vec{b}$ are mutually orthogonal.  

**Q47.** For any two complex numbers $z_1$ and $z_2$:
(A) $|z_1 + z_2| \\le |z_1| + |z_2|$ (Triangle inequality).  
(B) $|z_1 - z_2| \\ge ||z_1| - |z_2||$.  
(C) $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2(|z_1|^2 + |z_2|^2)$ (Parallelogram law).  
(D) $\\arg(z_1 z_2) = \\arg(z_1) + \\arg(z_2) + 2k\\pi$ ($k \\in \\mathbb{Z}$).  

**Q48.** In rolling two fair six-faced dice:
(A) The probability of getting a sum of 7 is $\\frac{1}{6}$.  
(B) The probability of getting a sum of at least 10 is $\\frac{1}{6}$.  
(C) The probability of getting equal numbers on both dice (a doublet) is $\\frac{1}{6}$.  
(D) The conditional probability of getting a sum of 8 given that the first die shows 4 is $\\frac{1}{6}$.  

---

### SECTION 3: Numerical Value Questions (Qs 49–54)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q49.** The value of the limit
$$L = \\lim_{x \\to 0} \\frac{\\tan x - x}{x^3}$$
is: (Round to two decimal places)  

**Q50.** The area of the region enclosed between the curve $y = \\sqrt{x}$ and the line $y = x$ is: (Round to two decimal places)  

**Q51.** The value of the definite integral
$$I = \\int_{0}^{\\pi/2} \\sin^3 x\\,dx$$
is: (Round to two decimal places)  

**Q52.** The radius of the in-circle of a triangle with side lengths $5\\text{ cm}$, $12\\text{ cm}$, and $13\\text{ cm}$ (in cm) is:  

**Q53.** The number of distinct real roots of the equation $x^3 - 3x + 1 = 0$ is:  

**Q54.** The value of the determinant
$$\\begin{vmatrix} 1 & 1 & 1 \\\\ 1 & 2 & 3 \\\\ 1 & 4 & 9 \\end{vmatrix}$$
is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(p1_content)
print("Generated mock_tests/Mock_16_IIT_Madras/Paper_1.md")

# ----------------------------------------------------
# SOLUTIONS PAPER 1
# ----------------------------------------------------
sol_p1_content = """# Detailed Solutions and Pedagogical Analysis — Mock Examination 16 (Paper 1)
### Organising Institute Style: IIT Madras (`IIT_MADRAS_STYLE` — 2010 Benchmark)

---

## PART I: PHYSICS

### Q1. Dielectric Coated Charged Sphere
- **First Observation & Concept**: Gauss's law with concentric dielectric shell.
- **Derivation**:
  - For $r > b$: $E(r) = \\frac{Q}{4\\pi\\varepsilon_0 r^2}$.
  - For $a < r < b$: $E(r) = \\frac{Q}{4\\pi\\varepsilon_0 K r^2}$.
  - Potential at $r = a$:
    $$V(a) = \\int_a^b E_{\\text{in}}\\,dr + \\int_b^\\infty E_{\\text{out}}\\,dr = \\frac{Q}{4\\pi\\varepsilon_0 K}\\left(\\frac{1}{a} - \\frac{1}{b}\\right) + \\frac{Q}{4\\pi\\varepsilon_0}\\frac{1}{b} = \\frac{Q}{4\\pi\\varepsilon_0}\\left(\\frac{1}{Ka} - \\frac{1}{Kb} + \\frac{1}{b}\\right)$$
- **Correct Option**: **(A)**.

### Q2. Magnetic Moment of Rotating Ring
- **First Observation & Concept**: Magnetic moment $\\mu = I A$.
- **Derivation**:
  - Current $I = \\frac{Q}{T} = \\frac{Q \\omega}{2\\pi}$.
  - Area $A = \\pi R^2$.
  - $\\mu = I A = \\frac{Q \\omega}{2\\pi} (\\pi R^2) = \\frac{1}{2} Q \\omega R^2$.
- **Correct Option**: **(A)**.

### Q3. Average AC Power Dissipation
- **First Observation & Concept**: $P = V_{\\text{rms}} I_{\\text{rms}} \\cos\\phi$.
- **Derivation**:
  - $V_0 = 200\\text{ V} \\implies V_{\\text{rms}} = 200/\\sqrt{2}$.
  - $I_0 = 5.0\\text{ A} \\implies I_{\\text{rms}} = 5.0/\\sqrt{2}$.
  - Phase difference $\\phi = \\pi/3 \\implies \\cos\\phi = 1/2$.
  - $P = \\frac{200}{\\sqrt{2}} \\times \\frac{5.0}{\\sqrt{2}} \\times \\frac{1}{2} = \\frac{1000}{2} \\times \\frac{1}{2} = 250\\text{ W}$.
- **Correct Option**: **(A)**.

### Q4. Torque on Current Loop
- **First Observation & Concept**: $\\vec{\\tau} = \\vec{M} \\times \\vec{B} \\implies \\tau = M B \\sin\\theta$.
- **Derivation**:
  - $M = I a b$.
  - Angle between normal and field is $\\theta = 30^\\circ$.
  - $\\tau = I a b B_0 \\sin 30^\\circ = \\frac{1}{2} I a b B_0$.
- **Correct Option**: **(A)**.

### Q5. Minimum Period of Compound Pendulum
- **First Observation & Concept**: $T = 2\\pi \\sqrt{\\frac{k^2 + d^2}{g d}}$.
- **Derivation**:
  - $\\frac{d}{dd}\\left(\\frac{k^2}{d} + d\\right) = -\\frac{k^2}{d^2} + 1 = 0 \\implies d = k$.
  - Distance of knife-edge equals radius of gyration $k$ about CM.
- **Correct Option**: **(A)**.

### Q6. Brewster's Law and Snell's Law
- **First Observation & Concept**: $\\tan\\theta_B = \\mu = \\sqrt{3} \\implies \\theta_B = 60^\\circ$.
- **Derivation**:
  - At Brewster angle, reflected and refracted rays are perpendicular: $\\theta_B + r = 90^\\circ$.
  - $r = 90^\\circ - 60^\\circ = 30^\\circ$.
- **Correct Option**: **(A)**.

### Q7. Induced Electric Field from Changing B
- **Analysis**:
  - Symmetry gives circular field lines. (A is True)
  - For $r \\le R$: $E(2\\pi r) = \\pi r^2 \\alpha \\implies E = \\frac{1}{2} \\alpha r$. (B is True)
  - For $r > R$: $E(2\\pi r) = \\pi R^2 \\alpha \\implies E = \\frac{\\alpha R^2}{2r}$. (C is True)
  - $F = q E(r)$ is tangential $\\implies$ tangential acceleration. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q8. Dielectric Insertion at Constant Voltage
- **Analysis**:
  - Voltage held constant by battery: $V = V_0$. (A is True)
  - $C = K C_0 \\implies Q = C V_0 = K C_0 V_0$. (B is True)
  - $U = \\frac{1}{2} C V_0^2 = K \\left(\\frac{1}{2} C_0 V_0^2\\right)$. (C is True)
  - Work done by battery: $W_b = \\Delta Q V_0 = (K - 1) C_0 V_0^2$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q9. Simple Harmonic Motion Dynamics
- **Analysis**: All four statements correctly state phase relations and energy equipartition in SHM.
- **Correct Options**: **(A, B, C, D)**.

### Q10. Heat Pump Thermodynamics
- **Analysis**: $\\text{COP} = 300 / 50 = 6.0$; $W = Q_H / 6 = 1000\\text{ J}$; $Q_C = 5000\\text{ J}$; reversible cycle has $\\Delta S_{\\text{univ}} = 0$.
- **Correct Options**: **(A, B, C, D)**.

### Q11. Davisson-Germer Experiment
- **Analysis**: All four statements are standard historical and theoretical facts of the Davisson-Germer experiment.
- **Correct Options**: **(A, B, C, D)**.

### Q12. Sound Interference
- **Analysis**: Constructive and destructive conditions, maximum intensity $4I_0$, zero minimum intensity.
- **Correct Options**: **(A, B, C, D)**.

### Q13. Attractive Force Between Capacitor Plates
- **Derivation**:
  - $F = \\frac{1}{2} Q E = \\frac{\\varepsilon_0 A V^2}{2 d^2}$.
  - $F = \\frac{8.85 \\times 10^{-12} \\times 0.050 \\times 200^2}{2 \\times (1.0 \\times 10^{-3})^2} = \\frac{8.85 \\times 10^{-12} \\times 0.050 \\times 40000}{2 \\times 10^{-6}} = \\frac{1.77 \\times 10^{-8}}{2 \\times 10^{-6}} = 8.85 \\times 10^{-3}\\text{ N} = 8.85\\text{ mN}$.
- **Answer**: **8.85**.

### Q14. Magnetic Field at Center of Coil
- **Derivation**:
  $$B = \\frac{\\mu_0 N I}{2 r} = \\frac{4\\pi \\times 10^{-7} \\times 100 \\times 2.0}{2 \\times 0.050} = \\frac{8\\pi \\times 10^{-5}}{0.10} = 8\\pi \\times 10^{-4}\\text{ T} = 2.51 \\times 10^{-3}\\text{ T} = 2.51\\text{ mT}$$
- **Answer**: **2.51**.

### Q15. Rolling Sphere Kinetic Energy
- **Derivation**:
  - $E_k = \\frac{7}{10} M v^2 = \\frac{7}{10} \\times 5.0 \\times 4.0^2 = \\frac{7}{10} \\times 5.0 \\times 16 = 56.0\\text{ J}$.
- **Answer**: **56** (or **56.0**).

### Q16. Radius of Curvature from Newton's Rings
- **Derivation**:
  - For $n$-th dark ring: $D_n^2 = 4 n \\lambda R$.
  - $(4.0 \\times 10^{-3})^2 = 4 \\times 4 \\times (600 \\times 10^{-9}) \\times R$.
  - $16.0 \\times 10^{-6} = 16 \\times 600 \\times 10^{-9} R = 9.6 \\times 10^{-6} R$.
  - $R = \\frac{16.0 \\times 10^{-6}}{9.6 \\times 10^{-6}} = \\frac{16}{9.6} = 1.67\\text{ m}$.
- **Answer**: **1.67**.

### Q17. Doppler Effect in Whirled Whistle
- **Derivation**:
  - Speed of whistle $u = \\omega L = 20.0 \\times 1.0 = 20.0\\text{ m/s}$.
  - $f_{\\max} = f \\frac{v}{v - u} = 500 \\times \\frac{340}{340 - 20} = 500 \\times \\frac{340}{320} = 531.25\\text{ Hz}$.
  - $f_{\\min} = f \\frac{v}{v + u} = 500 \\times \\frac{340}{340 + 20} = 500 \\times \\frac{340}{360} = 472.22\\text{ Hz}$.
  - Difference $\\Delta f = 531.25 - 472.22 = 59.03 \\approx 59.0\\text{ Hz}$.
- **Answer**: **59.0**.

### Q18. Mean Lifetime of Radioactive Nuclide
- **Derivation**:
  $$\\tau = \\frac{1}{\\lambda} = \\frac{1}{0.050} = 20.0\\text{ s}$$
- **Answer**: **20** (or **20.0**).

---

## PART II: CHEMISTRY

### Q19. Specific Conductance
- **Analysis**:
  $$\\Lambda_m = \\frac{1000 \\kappa}{M} \\implies \\kappa = \\frac{\\Lambda_m M}{1000} = \\frac{120.0 \\times 0.010}{1000} = 1.20 \\times 10^{-3}\\text{ S/cm}$$
- **Correct Option**: **(A)**.

### Q20. Chelating Ligands
- **Analysis**:
  - Glycinate ($\\text{H}_2\\text{N}-\\text{CH}_2-\\text{COO}^-$) is bidentate with charge $-1$ (monoanionic).
  - $\\text{en}$ and $\\text{phen}$ are neutral bidentate; oxalate is dianionic ($-2$).
- **Correct Option**: **(A)**.

### Q21. Cresol Isomer Identification
- **Analysis**:
  - $p$-Cresol has the para position occupied; upon bromination, the two positions ortho to $-\\text{OH}$ are equivalent due to symmetry, yielding a single monobromo derivative (2-bromo-4-methylphenol).
- **Correct Option**: **(A)**.

### Q22. Alkali Metal Halide Lattice Enthalpy
- **Analysis**:
  - Lattice energy $\\propto \\frac{1}{r_+ + r_-}$. Down the group from $\\text{Li}^+$ to $\\text{Cs}^+$, ionic radius increases, so lattice enthalpy decreases: $\\text{LiF} > \\text{NaF} > \\text{KF} > \\text{RbF} > \\text{CsF}$.
- **Correct Option**: **(A)**.

### Q23. Effect of Volume on Rate
- **Analysis**:
  - Halving volume doubles all concentrations: $[\\text{A}]' = 2[\\text{A}]$, $[\\text{B}]' = 2[\\text{B}]$.
  - $\\text{Rate}' = k (2[\\text{A}])^2 (2[\\text{B}]) = 8 k [\\text{A}]^2 [\\text{B}] = 8 \\times \\text{Rate}$.
- **Correct Option**: **(A)**.

### Q24. KMnO4 in Acidic Medium
- **Analysis**:
  - $\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\rightarrow \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}$ ($+7 \\rightarrow +2$, gain of $5e^-$).
- **Correct Option**: **(A)**.

### Q25. Thermodynamic Relations of Electrochemical Cells
- **Analysis**: All four relations are rigorous consequences of the Gibbs-Helmholtz equation applied to reversible cells.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Crystal Field Splitting Parameters
- **Analysis**: $e_g$ destabilization $+0.6\\Delta_o$, $\\Delta_t = \\frac{4}{9}\\Delta_o$, spectrochemical series high-spin/low-spin criteria.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Tollens' Reagent Reduction
- **Analysis**:
  - Aldehydes (glucose, benzaldehyde, formic acid) reduce Tollens' reagent.
  - Fructose (an $\\alpha$-hydroxy ketone) isomerizes to glucose/mannose in alkaline Tollens' reagent (Lobry de Bruyn-van Ekenstein transformation) and gives a positive test.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Cyanide Leaching of Gold
- **Analysis**: MacArthur-Forrest process chemistry: oxidative leaching, complexation, zinc cementation reduction.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Reversible Isothermal Expansion
- **Analysis**: $\\Delta U = 0$, $W = nRT\\ln(V_2/V_1)$, $Q = W$, $\\Delta S = nR\\ln(V_2/V_1)$.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Group 14 Characteristics
- **Analysis**: Catenation of C, inert pair effect of Pb, $\\text{CCl}_4$ resistance to hydrolysis vs $\\text{SiCl}_4$ rapid hydrolysis.
- **Correct Options**: **(A, B, C, D)**.

### Q31. Standard Reduction Potential
- **Derivation**:
  $$E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}} \\implies 1.56 = E^\\circ_{\\text{Ag}^+/\\text{Ag}} - (-0.76) \\implies E^\\circ_{\\text{Ag}^+/\\text{Ag}} = 1.56 - 0.76 = +0.80\\text{ V}$$
- **Answer**: **0.80** (or **0.8**).

### Q32. pOH of Weak Base
- **Derivation**:
  $$[\\text{OH}^-] = \\sqrt{K_b c} = \\sqrt{1.8 \\times 10^{-5} \\times 0.10} = \\sqrt{1.8 \\times 10^{-6}} = 1.34 \\times 10^{-3}\\text{ M}$$
  $$\\text{pOH} = -\\log_{10}(1.34 \\times 10^{-3}) = 3 - 0.127 = 2.873 \\approx 2.87$$
- **Answer**: **2.87**.

### Q33. Density of Simple Cubic Metal
- **Derivation**:
  - Simple cubic: $Z = 1$ atom per unit cell.
  - $V = a^3 = (3.0 \\times 10^{-8})^3 = 27.0 \\times 10^{-24}\\text{ cm}^3$.
  - $\\rho = \\frac{Z M}{N_A V} = \\frac{1 \\times 108.0}{6.02 \\times 10^{23} \\times 27.0 \\times 10^{-24}} = \\frac{108.0}{16.25} \\approx 6.6\\text{ g/cm}^3$.
- **Answer**: **6.6**.

### Q34. Time for 75% Decay
- **Derivation**:
  - $75\\%$ decay means $25\\% = 1/4 = (1/2)^2$ remains $\\implies 2$ half-lives.
  - Total time $= 2 \\times 20.0 = 40.0\\text{ days}$.
- **Answer**: **40** (or **40.0**).

### Q35. Freezing Point Depression of Urea Solution
- **Derivation**:
  - Moles of urea $= 6.0 / 60.0 = 0.10\\text{ mol}$.
  - Mass of solvent $= 0.500\\text{ kg} \\implies m = 0.10 / 0.500 = 0.20\\text{ m}$.
  - $\\Delta T_f = K_f m = 1.86 \\times 0.20 = 0.372\\text{ K} \\approx 0.37\\text{ K}$.
- **Answer**: **0.37**.

### Q36. Molar Solubility of PbCl2
- **Derivation**:
  - $K_{sp} = 4s^3 \\implies 1.6 \\times 10^{-5} = 4s^3 \\implies s^3 = 4.0 \\times 10^{-6}$.
  - $s = (4.0)^{1/3} \\times 10^{-2} = 1.59 \\times 10^{-2}\\text{ M} = 15.9\\text{ mmol/L}$.
- **Answer**: **15.9**.

---

## PART III: MATHEMATICS

### Q37. Locus in Complex Plane
- **Derivation**:
  - $\\left|\\frac{z - i}{z + i}\\right| = 1 \\iff |z - i| = |z + i|$.
  - This is the locus of points equidistant from $(0, 1)$ and $(0, -1)$, which is the perpendicular bisector: the real axis ($y = 0$).
- **Correct Option**: **(A)**.

### Q38. Beta Function Integral
- **Derivation**:
  - Using $\\int_0^1 x (1 - x)^9\\,dx$: let $u = 1 - x \\implies \\int_0^1 (1 - u) u^9\\,du = \\int_0^1 (u^9 - u^{10})\\,du = \\frac{1}{10} - \\frac{1}{11} = \\frac{1}{110}$.
- **Correct Option**: **(A)**.

### Q39. Tangent to Parabola
- **Derivation**: Standard condition of tangency for $y = mx + c$ to $y^2 = 4ax$ is $c = a/m$.
- **Correct Option**: **(A)**.

### Q40. Differential Equation Family
- **Derivation**:
  $$\\frac{dy}{y} = \\frac{dx}{x} \\implies \\ln|y| = \\ln|x| + \\ln|k| \\implies y = kx$$
  This represents a family of straight lines passing through the origin.
- **Correct Option**: **(A)**.

### Q41. Permutations with Restriction
- **Derivation**:
  - Digits: $2, 4, 5, 7, 8$ (5 digits).
  - To be $> 5000$, the first digit must be $5, 7,$ or $8$ (3 choices).
  - The remaining 3 positions can be filled by the remaining 4 digits in $P(4, 3) = 4 \\times 3 \\times 2 = 24$ ways.
  - Total numbers $= 3 \\times 24 = 72$.
- **Correct Option**: **(A)**.

### Q42. Distance from Origin to Plane
- **Derivation**:
  $$d = \\frac{|-14|}{\\sqrt{2^2 + (-3)^2 + 6^2}} = \\frac{14}{\\sqrt{4 + 9 + 36}} = \\frac{14}{\\sqrt{49}} = \\frac{14}{7} = 2$$
- **Correct Option**: **(A)**.

### Q43. Rational Function Analysis
- **Analysis**:
  - $f(-x) = -f(x)$ (odd). (A is True)
  - $f'(x) = \\frac{1 - x^2}{(1+x^2)^2} = 0 \\implies x = \\pm 1$. Local max $f(1) = 1/2$, local min $f(-1) = -1/2$. (B, C are True)
  - Range is $[-1/2, 1/2]$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q44. Geometric Properties of Ellipse
- **Analysis**: Focal property, auxiliary circle foot of perpendicular, product of focal perpendiculars $= b^2$, director circle $= a^2 + b^2$.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Matrix Determinant and Trace Properties
- **Analysis**: Standard matrix algebra theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Unit Vector Identities
- **Analysis**:
  - $|\\vec{a} + \\vec{b}|^2 = 1 + 1 + 2\\cos\\theta = 2(1 + \\cos\\theta) = 4\\cos^2(\\theta/2) \\implies |\\vec{a} + \\vec{b}| = 2\\cos(\\theta/2)$.
  - $|\\vec{a} - \\vec{b}|^2 = 2(1 - \\cos\\theta) = 4\\sin^2(\\theta/2) \\implies |\\vec{a} - \\vec{b}| = 2\\sin(\\theta/2)$.
  - $(\\vec{a} + \\vec{b}) \\cdot (\\vec{a} - \\vec{b}) = |\\vec{a}|^2 - |\\vec{b}|^2 = 1 - 1 = 0 \\implies$ orthogonal.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Complex Number Properties
- **Analysis**: Triangle inequalities, parallelogram identity, argument additivity.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Dice Probability
- **Analysis**:
  - Sum of 7: 6 outcomes out of 36 $= 1/6$. (A is True)
  - Sum $\\ge 10$: $(4,6), (5,5), (5,6), (6,4), (6,5), (6,6) = 6$ outcomes $= 1/6$. (B is True)
  - Doublet: 6 outcomes $= 1/6$. (C is True)
  - Given first die is 4, sum is 8 requires second die to be 4 $\\implies 1/6$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q49. Standard Limit
- **Derivation**:
  $$\\lim_{x \\to 0} \\frac{\\tan x - x}{x^3} = \\frac{1}{3} \\approx 0.33$$
- **Answer**: **0.33**.

### Q50. Area Enclosed by Curves
- **Derivation**:
  - $\\sqrt{x} = x \\implies x = x^2 \\implies x(x - 1) = 0 \\implies x = 0, 1$.
  - Area $= \\int_0^1 (\\sqrt{x} - x)\\,dx = [\\frac{2}{3}x^{3/2} - \\frac{x^2}{2}]_0^1 = \\frac{2}{3} - \\frac{1}{2} = \\frac{1}{6} \\approx 0.17$.
- **Answer**: **0.17**.

### Q51. Walli's Definite Integral
- **Derivation**:
  $$\\int_0^{\\pi/2} \\sin^3 x\\,dx = \\frac{2}{3} \\times 1 = \\frac{2}{3} \\approx 0.67$$
- **Answer**: **0.67**.

### Q52. In-Radius of Right Triangle
- **Derivation**:
  $$r = \\frac{a + b - c}{2} = \\frac{5 + 12 - 13}{2} = \\frac{4}{2} = 2.0\\text{ cm}$$
- **Answer**: **2** (or **2.0**).

### Q53. Real Roots of Cubic
- **Derivation**:
  - $f(x) = x^3 - 3x + 1$.
  - $f'(x) = 3x^2 - 3 = 3(x - 1)(x + 1) = 0 \\implies x = \\pm 1$.
  - $f(-1) = -1 + 3 + 1 = 3 > 0$.
  - $f(1) = 1 - 3 + 1 = -1 < 0$.
  - Since local max is positive and local min is negative, the graph crosses the x-axis 3 times $\\implies 3$ real roots.
- **Answer**: **3**.

### Q54. Vandermonde Determinant
- **Derivation**:
  $$\\begin{vmatrix} 1 & 1 & 1 \\\\ 1 & 2 & 3 \\\\ 1 & 4 & 9 \\end{vmatrix} = (2 - 1)(3 - 1)(3 - 2) = 1 \\times 2 \\times 1 = 2$$
- **Answer**: **2**.
"""

with open(os.path.join(MOCK_DIR, "Solutions_Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(sol_p1_content)
print("Generated mock_tests/Mock_16_IIT_Madras/Solutions_Paper_1.md")
