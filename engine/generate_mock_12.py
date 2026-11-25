import os

MOCK_DIR = os.path.join("mock_tests", "Mock_12_IIT_Kanpur")
os.makedirs(MOCK_DIR, exist_ok=True)

# ----------------------------------------------------
# PAPER 1
# ----------------------------------------------------
p1_content = """# JEE (Advanced) Mock Examination 12
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

**Q1.** A heavy block of mass $m$ is pushed against a rough vertical wall by applying a horizontal force $F$. The coefficient of static friction between the block and the wall is $\\mu = 0.4$. The minimum force $F$ required to prevent the block from sliding down is ($m = 2.0\\text{ kg}$, $g = 10\\text{ m/s}^2$):
(A) $50\\text{ N}$  
(B) $20\\text{ N}$  
(C) $8\\text{ N}$  
(D) $100\\text{ N}$  

**Q2.** A spherical cavity of radius $R$ is scooped out from the center of a uniform solid sphere of radius $2R$ and total initial mass $M_0$. The gravitational field intensity at a distance $3R$ from the center of the sphere is:
(A) $\\frac{7}{72}\\frac{G M_0}{R^2}$  
(B) $\\frac{1}{9}\\frac{G M_0}{R^2}$  
(C) $\\frac{7}{81}\\frac{G M_0}{R^2}$  
(D) $\\frac{1}{12}\\frac{G M_0}{R^2}$  

**Q3.** An ideal monoatomic gas is taken through an adiabatic process where its volume is reduced to $1/8$ of its initial value. The ratio of final pressure to initial pressure $P_f / P_i$ is:
(A) $16$  
(B) $32$  
(C) $64$  
(D) $8$  

**Q4.** A parallel-plate capacitor of capacitance $C_0$ is connected across a battery of voltage $V_0$. While remaining connected to the battery, a dielectric slab of dielectric constant $\\kappa = 3$ is inserted, completely filling the space between the plates. The ratio of the final electrostatic energy stored to the initial stored energy is:
(A) $3$  
(B) $9$  
(C) $1/3$  
(D) $1$  

**Q5.** In an electron transition from $n = 3$ to $n = 1$ in a hydrogen atom, the recoil speed of the hydrogen atom (mass $M = 1.67\\times 10^{-27}\\text{ kg}$) is approximately (energy emitted $= 12.1\\text{ eV}$, $c = 3.0\\times 10^8\\text{ m/s}$):
(A) $3.9\\text{ m/s}$  
(B) $1.2\\text{ m/s}$  
(C) $0.8\\text{ m/s}$  
(D) $7.8\\text{ m/s}$  

**Q6.** A glass prism of refracting angle $A = 60^\\circ$ has refractive index $\\mu = 1.50$. The angle of minimum deviation $\\delta_m$ is:
(A) $37.2^\\circ$  
(B) $45.0^\\circ$  
(C) $30.0^\\circ$  
(D) $60.0^\\circ$  

---

### SECTION 2: One or More Than One Correct Option (Qs 7–12)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q7.** A uniform solid cylinder of mass $M$ and radius $R$ is placed on a rough horizontal surface. A horizontal force $F$ is applied at the level of the center of mass:
(A) The acceleration of the center of mass is $\\frac{2F}{3M}$.  
(B) The friction force acting on the cylinder is $\\frac{F}{3}$ directed opposite to $F$.  
(C) The minimum coefficient of static friction required for rolling without slipping is $\\frac{F}{3Mg}$.  
(D) If the surface is frictionless, the cylinder translates without rotation.  

**Q8.** An ideal gas undergoes a thermodynamic process whose equation is $P T = \\text{constant}$:
(A) The process can be written as $P^2 V = \\text{constant}$.  
(B) The work done by the gas when temperature changes from $T_1$ to $T_2$ is $2 n R (T_2 - T_1)$.  
(C) The molar heat capacity for this process is $C = C_v + 2R$.  
(D) During expansion, the temperature of the gas increases.  

**Q9.** A long straight wire along the z-axis carries a steady current $I$ in the $+z$ direction. A rectangular loop in the xz-plane has sides of length $a$ (parallel to z-axis) and $b$ (parallel to x-axis). The closer edge is at distance $d$ from the wire:
(A) The magnetic flux linked with the loop is $\\frac{\\mu_0 I a}{2\\pi}\\ln\\left(1 + \\frac{b}{d}\\right)$.  
(B) If the loop moves away from the wire with constant velocity $v\\hat{i}$, the induced EMF in the loop is $\\frac{\\mu_0 I a b v}{2\\pi d (d + b)}$.  
(C) The induced current flows clockwise when viewed from the $+y$ direction.  
(D) The net magnetic force on the loop opposes its motion away from the wire.  

**Q10.** In a photoelectric experiment using light of frequency $\\nu$ greater than threshold frequency $\\nu_0$:
(A) The stopping potential is independent of the light intensity.  
(B) The saturation current is directly proportional to the light intensity.  
(C) The maximum kinetic energy of photoelectrons increases linearly with frequency $\\nu$.  
(D) Photoelectric emission occurs even if the intensity is extremely low, provided $\\nu > \\nu_0$.  

**Q11.** A convex lens of focal length $f_1 = 30\\text{ cm}$ is placed in contact with a concave lens of focal length $f_2 = -20\\text{ cm}$:
(A) The combination acts as a diverging lens of focal length $F = -60\\text{ cm}$.  
(B) The power of the combination is $-1.67\\text{ D}$.  
(C) A parallel beam incident on the combination emerges as a divergent beam.  
(D) The combination produces a real image of a real object placed at any distance.  

**Q12.** A particle of mass $m$ is executing undamped simple harmonic motion with amplitude $A$ and angular frequency $\\omega$:
(A) The total mechanical energy is $E = \\frac{1}{2} m \\omega^2 A^2$.  
(B) The average kinetic energy over one complete cycle is $\\frac{1}{4} m \\omega^2 A^2$.  
(C) The average potential energy over one complete cycle is $\\frac{1}{4} m \\omega^2 A^2$.  
(D) The potential energy equals the kinetic energy when displacement is $x = \\pm A/\\sqrt{2}$.  

---

### SECTION 3: Numerical Value Questions (Qs 13–18)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q13.** A uniform thin rod of mass $M = 3.0\\text{ kg}$ and length $L = 2.0\\text{ m}$ is free to rotate about a horizontal axis passing through its center. Two small balls, each of mass $m = 0.5\\text{ kg}$, are attached to the two ends of the rod. The moment of inertia of the system about the rotation axis (in $\\text{kg}\\cdot\\text{m}^2$) is:  

**Q14.** In an AC circuit, an alternating voltage $v(t) = 200\\sin(100\\pi t)\\text{ V}$ is applied across a pure resistor $R = 50\\,\\Omega$. The average power consumed in the resistor (in Watts) is:  

**Q15.** A capillary tube of radius $r = 0.2\\text{ mm}$ is dipped in water ($T = 0.07\\text{ N/m}$, $\\rho = 1000\\text{ kg/m}^3$, $g = 10\\text{ m/s}^2$). The height of water rise (in cm) is:  

**Q16.** A particle of mass $m = 0.2\\text{ kg}$ is attached to a spring of stiffness $k = 80\\text{ N/m}$. The natural frequency of oscillation (in Hz) is (take $\\pi \\approx 3.14$, round to two decimal places):  

**Q17.** A photon has energy $E = 3.1\\text{ eV}$. The wavelength of the photon (in nanometers, nm) is ($hc = 1240\\text{ eV}\\cdot\\text{nm}$):  

**Q18.** A circular coil of $N = 200$ turns and radius $r = 5.0\\text{ cm}$ carries a current $I = 1.0\\text{ A}$. The magnetic field at its center (in milliTesla, mT) is (take $\\pi \\approx 3.14$, round to two decimal places):  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: Single Correct Option (Qs 19–24)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q19.** At $298\\text{ K}$, the solubility product of a salt $M_2 X$ is $K_{sp} = 3.2\\times 10^{-11}$. The molar solubility of $M_2 X$ in pure water (in mol/L) is:
(A) $2.0\\times 10^{-4}\\text{ M}$  
(B) $4.0\\times 10^{-4}\\text{ M}$  
(C) $1.0\\times 10^{-4}\\text{ M}$  
(D) $5.6\\times 10^{-6}\\text{ M}$  

**Q20.** For a first-order reaction, the time required for $99.9\\%$ completion is related to its half-life $t_{1/2}$ by:
(A) $t_{99.9\\%} = 10 t_{1/2}$  
(B) $t_{99.9\\%} = 3 t_{1/2}$  
(C) $t_{99.9\\%} = 5 t_{1/2}$  
(D) $t_{99.9\\%} = 20 t_{1/2}$  

**Q21.** In the qualitative analysis of Group IV cations ($\\text{Co}^{2+}, \\text{Ni}^{2+}, \\text{Mn}^{2+}, \\text{Zn}^{2+}$), $\\text{H}_2\\text{S}$ is passed in:
(A) Ammoniacal medium ($\\text{NH}_4\\text{OH} + \\text{NH}_4\\text{Cl}$)  
(B) Acidic medium (dilute $\\text{HCl}$)  
(C) Neutral water  
(D) Concentrated $\\text{HNO}_3$  

**Q22.** The major product obtained when 2-bromopentane is heated with alcoholic potassium hydroxide ($\\text{alc. KOH}$) is:
(A) Pent-2-ene (major, Saytzeff product)  
(B) Pent-1-ene  
(C) Pentan-2-ol  
(D) 2-ethoxypentane  

**Q23.** According to crystal field theory, the number of unpaired electrons in $[\\text{Fe}(\\text{CN})_6]^{3-}$ (low-spin $d^5$) is:
(A) $1$  
(B) $3$  
(C) $5$  
(D) $0$  

**Q24.** When excess potassium iodide solution is added to an aqueous solution of mercuric chloride ($\\text{HgCl}_2$), the red precipitate formed initially dissolves to form:
(A) Nessler's reagent cation $[\\text{Hg}(\\text{NH}_3)_2]^+$  
(B) Soluble complex ion $[\\text{HgI}_4]^{2-}$  
(C) $\\text{Hg}_2\\text{I}_2$  
(D) $\\text{K}_2\\text{HgCl}_4$  

---

### SECTION 2: One or More Than One Correct Option (Qs 25–30)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q25.** In an electrochemical cell at $298\\text{ K}$: $\\text{Zn}(s)|\\text{Zn}^{2+}(0.01\\text{ M})||\\text{Cu}^{2+}(0.1\\text{ M})|\\text{Cu}(s)$ with $E^\\circ_{\\text{cell}} = 1.10\\text{ V}$:
(A) The reaction quotient is $Q = 0.10$.  
(B) The cell EMF is $E_{\\text{cell}} = 1.10 - \\frac{0.06}{2}\\log(0.10) = 1.13\\text{ V}$.  
(C) Diluting the anode compartment increases the cell EMF.  
(D) Diluting the cathode compartment decreases the cell EMF.  

**Q26.** Regarding an ideal binary solution of liquids $A$ and $B$:
(A) $\\Delta H_{\\text{mix}} = 0$.  
(B) $\\Delta V_{\\text{mix}} = 0$.  
(C) $\\Delta S_{\\text{mix}} > 0$.  
(D) $\\Delta G_{\\text{mix}} < 0$.  

**Q27.** Which of the following compounds will give a positive carbylamine test (isocyanide test)?
(A) Aniline  
(B) Methylamine  
(C) N-methylaniline  
(D) Triethylamine  

**Q28.** Which of the following statements is/are correct regarding the structure of diborane ($\\text{B}_2\\text{H}_6$)?
(A) Each boron atom is $sp^3$ hybridized.  
(B) There are two 3-center-2-electron ($\\text{3c-2e}$) banana bonds.  
(C) There are four terminal 2-center-2-electron ($\\text{2c-2e}$) $\\text{B-H}$ bonds.  
(D) All six hydrogen atoms lie in the same plane.  

**Q29.** In a solution containing weak acid $\\text{CH}_3\\text{COOH}$ and its conjugate base $\\text{CH}_3\\text{COONa}$:
(A) $\\text{pH} = pK_a + \\log\\frac{[\\text{CH}_3\\text{COO}^-]}{[\\text{CH}_3\\text{COOH}]}$.  
(B) If $[\\text{Salt}] = [\\text{Acid}]$, then $\\text{pH} = pK_a$.  
(C) The buffer resists changes in pH upon addition of small amounts of strong acid or base.  
(D) The buffer solution has maximum buffering capacity when $\\text{pH} = pK_a$.  

**Q30.** For the nucleophilic substitution reactions of alkyl halides:
(A) The $S_N 2$ mechanism proceeds with complete inversion of configuration (Walden inversion).  
(B) The $S_N 1$ mechanism proceeds via a planar carbocation intermediate leading to racemization.  
(C) Tertiary alkyl halides react predominantly via $S_N 1$.  
(D) Primary alkyl halides react predominantly via $S_N 2$.  

---

### SECTION 3: Numerical Value Questions (Qs 31–36)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q31.** At $298\\text{ K}$, the pH of a $0.01\\text{ M}$ solution of strong base $\\text{NaOH}$ is:  

**Q32.** An element crystallizes in a simple cubic (SC) crystal lattice with edge length $a = 200\\text{ pm}$. The packing efficiency of the simple cubic unit cell (as a percentage, %) is (use $\\pi \\approx 3.14$, round to two decimal places):  

**Q33.** A first-order reaction has a rate constant $k = 6.93\\times 10^{-3}\\text{ s}^{-1}$. The half-life of the reaction (in seconds) is:  

**Q34.** An alkene on reductive ozonolysis produces only acetone (propan-2-one). The number of carbon atoms in one molecule of this symmetric alkene is:  

**Q35.** The standard reduction potentials are $E^\\circ(\\text{Zn}^{2+}/\\text{Zn}) = -0.76\\text{ V}$ and $E^\\circ(\\text{Ag}^+/\\text{Ag}) = +0.80\\text{ V}$. The standard EMF $E^\\circ_{\\text{cell}}$ (in Volts) of the cell $\\text{Zn}|\\text{Zn}^{2+}||\\text{Ag}^+|\\text{Ag}$ is:  

**Q36.** The total number of stereoisomers (optical isomers) of lactic acid ($\\text{CH}_3\\text{-CH(OH)-COOH}$) is:  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 37–42)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q37.** The value of the definite integral
$$I = \\int_{0}^{\\pi/2} \\frac{\\sin x}{\\sin x + \\cos x}\\,dx$$
is:
(A) $\\frac{\\pi}{4}$  
(B) $\\frac{\\pi}{2}$  
(C) $1$  
(D) $0$  

**Q38.** The slope of the tangent to the curve $y = x^2 - 4x + 3$ at the point where it cuts the y-axis is:
(A) $-4$  
(B) $3$  
(C) $2$  
(D) $0$  

**Q39.** The distance between the parallel lines $y = 2x + 3$ and $y = 2x - 7$ is:
(A) $2\\sqrt{5}$  
(B) $\\sqrt{5}$  
(C) $10$  
(D) $4\\sqrt{5}$  

**Q40.** An unbiased die is thrown twice. The probability of getting a doublet (same number on both dice) is:
(A) $1/6$  
(B) $1/36$  
(C) $1/12$  
(D) $5/36$  

**Q41.** The area bounded by the curve $y = x^2$ and the line $y = 4$ is:
(A) $\\frac{32}{3}$  
(B) $\\frac{16}{3}$  
(C) $16$  
(D) $8$  

**Q42.** The integrating factor of the linear differential equation $\\frac{dy}{dx} + y = e^{-x}$ is:
(A) $e^x$  
(B) $e^{-x}$  
(C) $x$  
(D) $1/x$  

---

### SECTION 2: One or More Than One Correct Option (Qs 43–48)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q43.** Let $f(x) = x^3 - 3x^2 + 2$ for all $x \\in \\mathbb{R}$:
(A) $f(x)$ has a local maximum at $x = 0$.  
(B) $f(x)$ has a local minimum at $x = 2$.  
(C) $f(x)$ has an inflection point at $x = 1$.  
(D) $f(x) = 0$ has three distinct real roots.  

**Q44.** For the circle $x^2 + y^2 = 25$:
(A) The equation of the tangent at $(3, 4)$ is $3x + 4y = 25$.  
(B) The equation of the normal at $(3, 4)$ is $4x - 3y = 0$.  
(C) The length of the tangent drawn from $(10, 0)$ is $5\\sqrt{3}$.  
(D) The director circle is $x^2 + y^2 = 50$.  

**Q45.** Let $A$ be a $3 \\times 3$ matrix such that $A^T = A$ (symmetric matrix):
(A) All eigenvalues of $A$ are real numbers.  
(B) Eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.  
(C) $A$ is orthogonally diagonalizable.  
(D) $\\det(A)$ is the product of its eigenvalues.  

**Q46.** Let $z$ be a complex number satisfying $|z| = 2$:
(A) The locus of $z$ is a circle of radius 2 centered at the origin.  
(B) The maximum value of $|z - 3|$ is 5.  
(C) The minimum value of $|z - 3|$ is 1.  
(D) $z \\bar{z} = 4$.  

**Q47.** Let $f(x) = |x - 1| + |x - 3|$ for all $x \\in \\mathbb{R}$:
(A) $f(x) = 2$ for all $x \\in [1, 3]$.  
(B) The minimum value of $f(x)$ on $\\mathbb{R}$ is 2.  
(C) $f(x)$ is continuous everywhere on $\\mathbb{R}$.  
(D) $f(x)$ is not differentiable at $x = 1$ and $x = 3$.  

**Q48.** Let $\\vec{u}, \\vec{v}, \\vec{w}$ be three vectors such that $\\vec{u} \\cdot (\\vec{v} \\times \\vec{w}) \\ne 0$:
(A) The three vectors are linearly independent.  
(B) The three vectors are non-coplanar.  
(C) The volume of the parallelepiped formed by these vectors is $|\\vec{u} \\cdot (\\vec{v} \\times \\vec{w})|$.  
(D) Any vector $\\vec{r} \\in \\mathbb{R}^3$ can be expressed as a linear combination of $\\vec{u}, \\vec{v}, \\vec{w}$.  

---

### SECTION 3: Numerical Value Questions (Qs 49–54)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q49.** The value of the limit
$$L = \\lim_{x \\to 0} \\frac{e^{2x} - 1}{x}$$
is:  

**Q50.** The number of distinct real roots of the equation $x^3 - x = 0$ is:  

**Q51.** The slope of the tangent to the curve $y = x^3$ at the point $(1, 1)$ is:  

**Q52.** The value of the definite integral $\\int_{0}^{3} (2x + 1)\\,dx$ is:  

**Q53.** The distance of the point $(1, 1, 1)$ from the origin is: (Round to two decimal places, $\\sqrt{3} \\approx 1.73$)  

**Q54.** The value of the determinant $\\begin{vmatrix} 3 & 0 & 0 \\\\ 0 & 3 & 0 \\\\ 0 & 0 & 3 \\end{vmatrix}$ is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(p1_content)
print("Generated mock_tests/Mock_12_IIT_Kanpur/Paper_1.md")

