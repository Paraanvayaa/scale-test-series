import os

MOCK_DIR = os.path.join("mock_tests", "Mock_09_IIT_Guwahati")

# ----------------------------------------------------
# PAPER 2
# ----------------------------------------------------
p2_content = """# JEE (Advanced) Mock Examination 09
### Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
### Paper 2 · Full Syllabus · Total Marks: 180 · Duration: 3 Hours

---

## Instructions
- This paper consists of **54 questions** across three subjects: **Physics (Qs 1–18)**, **Chemistry (Qs 19–36)**, and **Mathematics (Qs 37–54)**.
- Each subject contains three sections:
  - **Section 1**: 6 One or More Than One Correct Option Questions (+4, -2, 0; Partial marking: +3, +2, +1)
  - **Section 2**: 6 Numerical Value Questions (+3, 0; non-negative decimal/integer)
  - **Section 3**: 6 Single Digits Non-negative Integer Questions (+3, -1, 0)

---

# PART I: PHYSICS (54 Marks)

### SECTION 1: One or More Than One Correct Option (Qs 1–6)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q1.** A particle of mass $m$ moves along the x-axis under the influence of an attractive central force directed towards the origin with potential energy $U(x) = \\frac{1}{2} k x^2 + \\frac{1}{4} \\beta x^4$ (where $k > 0, \\beta > 0$):
(A) The origin $x = 0$ is a position of stable equilibrium.  
(B) The motion of the particle is periodic for any total mechanical energy $E > 0$.  
(C) For small oscillations ($x \\to 0$), the period approaches $2\\pi \\sqrt{m/k}$.  
(D) The restoring force is non-linear and satisfies $F(x) = -kx - \\beta x^3$.  

**Q2.** A cyclic process $1 \\rightarrow 2 \\rightarrow 3 \\rightarrow 1$ is performed on one mole of an ideal gas. Step $1 \\rightarrow 2$ is isothermal expansion at $T_0$ from volume $V_0$ to $2V_0$. Step $2 \\rightarrow 3$ is isochoric cooling to temperature $T_0/2$. Step $3 \\rightarrow 1$ is isobaric compression back to state 1:
(A) The work done in step $1 \\rightarrow 2$ is $R T_0 \\ln 2$.  
(B) The work done in step $2 \\rightarrow 3$ is zero.  
(C) The work done in step $3 \\rightarrow 1$ is $-\\frac{1}{2} R T_0$.  
(D) The net work done by the gas in one complete cycle is $R T_0 (\\ln 2 - 1/2)$.  

**Q3.** An isolated conducting spherical shell of inner radius $R_1$ and outer radius $R_2$ has a point charge $+q$ placed at its center:
(A) An induced charge $-q$ resides on the inner surface $r = R_1$.  
(B) An induced charge $+q$ resides on the outer surface $r = R_2$.  
(C) The electric field inside the conducting shell material ($R_1 < r < R_2$) is zero.  
(D) The potential at any point inside the cavity ($r < R_1$) is $\\frac{q}{4\\pi\\varepsilon_0}\\left(\\frac{1}{r} - \\frac{1}{R_1} + \\frac{1}{R_2}\\right)$.  

**Q4.** In a series $LCR$ circuit connected to an AC voltage $V(t) = V_0 \\sin(\\omega t)$:
(A) At resonance angular frequency $\\omega_0 = 1/\\sqrt{LC}$, current and applied voltage are in phase.  
(B) The impedance at resonance attains its minimum value $Z = R$.  
(C) The power factor at resonance is unity.  
(D) The bandwidth of the resonance curve is $\\Delta\\omega = R/L$.  

**Q5.** In an electron microscope, electrons are accelerated from rest by a high voltage $V$:
(A) The de Broglie wavelength is inversely proportional to $\\sqrt{V}$.  
(B) Using a higher accelerating potential improves the resolving power of the microscope.  
(C) For an accelerating voltage of $150\\text{ V}$, the electron de Broglie wavelength is approximately $0.1\\text{ nm}$.  
(D) The electron beam can be focused using non-uniform magnetic fields (magnetic lenses).  

**Q6.** A glass prism of refracting angle $A = 60^\\circ$ has refractive index $\\mu = \\sqrt{3}$. A ray of light is incident at the angle of minimum deviation $\\delta_m$:
(A) The angle of minimum deviation is $\\delta_m = 60^\\circ$.  
(B) The angle of incidence for minimum deviation is $i = 60^\\circ$.  
(C) The ray travels parallel to the base inside the prism at minimum deviation.  
(D) The angle of refraction at the first face is $r = 30^\\circ$.  

---

### SECTION 2: Numerical Value Questions (Qs 7–12)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q7.** A block of mass $M = 2.0\\text{ kg}$ is attached to a spring of force constant $k = 50\\text{ N/m}$. The block is pulled a distance $A = 0.2\\text{ m}$ from its equilibrium position and released from rest. The maximum speed of the block (in m/s) is:  

**Q8.** A heat engine operates between $127^\\circ\\text{C}$ and $27^\\circ\\text{C}$. Its actual efficiency is $50\\%$ of the maximum possible Carnot efficiency. The actual efficiency of this engine (as a percentage, %) is:  

**Q9.** Two long coaxial solenoids have radii $r_1 = 2\\text{ cm}$ and $r_2 = 4\\text{ cm}$ with turn densities $n_1 = 500\\text{ turns/m}$ and $n_2 = 1000\\text{ turns/m}$. The mutual inductance per unit length (in $\\text{mH/m}$) is (use $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ T}\\cdot\\text{m/A}$, $\\pi \\approx 3.14$, round to two decimal places):  

**Q10.** The work function of a metal is $\\Phi = 2.0\\text{ eV}$. Light of wavelength $\\lambda = 310\\text{ nm}$ is incident on the metal ($hc = 1240\\text{ eV}\\cdot\\text{nm}$). The maximum kinetic energy of the emitted photoelectrons (in eV) is:  

**Q11.** A thin converging lens of focal length $f = 20\\text{ cm}$ is placed in contact with a thin diverging lens of focal length $f = -30\\text{ cm}$. The focal length of the combination (in cm) is:  

**Q12.** A uniform wire of resistance $R = 12\\,\\Omega$ is bent into a circle. The effective resistance between two diametrically opposite points (in $\\Omega$) is:  

---

### SECTION 3: Non-Negative Integer Questions (Qs 13–18)
*Marking Scheme: +3 for correct integer, -1 for incorrect, 0 if unanswered.*

**Q13.** A body of mass $m$ is projected with speed $v$ from the surface of the earth. The minimum speed required for the body to escape the gravitational attraction of the earth (escape velocity) is $v_e = \\sqrt{k g R_e}$. The integer $k$ is:  

**Q14.** The number of beats heard per second when two tuning forks of frequencies $256\\text{ Hz}$ and $260\\text{ Hz}$ are sounded together is:  

**Q15.** The number of radioactive nuclei in a sample decreases to $1/8$ of its original value in $15\\text{ minutes}$. The half-life of the radioactive isotope (in minutes) is:  

**Q16.** The number of degrees of freedom of a rigid non-vibrating diatomic molecule (such as $\\text{O}_2$ or $\\text{N}_2$) at room temperature is:  

**Q17.** A car moves around a flat circular track of radius $R$ with speed $v$. If the speed is doubled and the radius is quadrupled, the centripetal acceleration remains the same. The ratio of the new centripetal acceleration to the old is:  

**Q18.** The number of spectral lines emitted when an electron in a hydrogen atom transitions from $n = 3$ to all lower energy states is:  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: One or More Than One Correct Option (Qs 19–24)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q19.** Which of the following statements is/are correct regarding the structure of sodium chloride ($\\text{NaCl}$)?
(A) $\\text{Cl}^-$ ions form an FCC (face-centered cubic) lattice.  
(B) $\\text{Na}^+$ ions occupy all octahedral voids.  
(C) The coordination number of both $\\text{Na}^+$ and $\\text{Cl}^-$ is 6.  
(D) Each unit cell contains 4 formula units of $\\text{NaCl}$.  

**Q20.** For a reversible chemical reaction at equilibrium:
(A) The forward reaction rate equals the reverse reaction rate.  
(B) $\\Delta G = 0$.  
(C) The equilibrium constant is related to standard Gibbs free energy by $\\Delta G^\\circ = -RT \\ln K$.  
(D) Catalysts increase the equilibrium constant $K$.  

**Q21.** Which of the following amines will react with nitrous acid ($\\text{HNO}_2$) at $0 - 5^\\circ\\text{C}$ to form a stable diazonium salt?
(A) Aniline (benzenamine)  
(B) Ethylamine  
(C) N-methylaniline  
(D) p-toluidine  

**Q22.** Which of the following octahedral complexes exhibits optical isomerism?
(A) $[\\text{Co}(\\text{en})_3]^{3+}$  
(B) $\\text{cis}-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$  
(C) $\\text{trans}-[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$  
(D) $[\\text{Cr}(\\text{ox})_3]^{3-}$  

**Q23.** In the Hall-Héroult electrolytic process for the extraction of aluminum:
(A) Pure alumina ($\\text{Al}_2\\text{O}_3$) is dissolved in molten cryolite ($\\text{Na}_3\\text{AlF}_6$) and fluorspar ($\\text{CaF}_2$).  
(B) Cryolite lowers the melting point of the mixture and increases its electrical conductivity.  
(C) Aluminum is discharged at the cathode as molten metal.  
(D) Carbon dioxide and carbon monoxide gases are evolved at the carbon anode.  

**Q24.** For a zero-order reaction $A \\rightarrow \\text{Products}$:
(A) The rate of reaction is independent of the reactant concentration.  
(B) The half-life is directly proportional to the initial concentration ($t_{1/2} = [A]_0 / (2k)$).  
(C) The plot of $[A]$ versus time $t$ is a straight line with slope $-k$.  
(D) The units of rate constant $k$ are $\\text{mol}\\cdot\\text{L}^{-1}\\cdot\\text{s}^{-1}$.  

---

### SECTION 2: Numerical Value Questions (Qs 25–30)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q25.** The standard reduction potential of $\\text{Ag}^+/\\text{Ag}$ is $+0.80\\text{ V}$. The potential of a silver electrode in a $0.10\\text{ M}\\text{ AgNO}_3$ solution at $298\\text{ K}$ (in Volts) is (use $2.303 RT/F = 0.06\\text{ V}$, round to two decimal places):  

**Q26.** The standard enthalpy of formation of liquid water is $-285.8\\text{ kJ/mol}$. The standard enthalpy of vaporization of water at $298\\text{ K}$ is $+44.0\\text{ kJ/mol}$. The standard enthalpy of formation of gaseous water $\\text{H}_2\\text{O}(g)$ (in kJ/mol) is (round to one decimal place):  

**Q27.** An organic compound has empirical formula $\\text{CH}_2\\text{O}$ and molecular mass $180\\text{ g/mol}$. The number of carbon atoms in one molecule of this compound is:  

**Q28.** The solubility product $K_{sp}$ of lead iodide ($\\text{PbI}_2$) is $7.1\\times 10^{-9}$ at $298\\text{ K}$. The molar solubility of $\\text{PbI}_2$ in pure water (in mmol/L) is (use $\\sqrt[3]{1.775\\times 10^{-9}} \\approx 1.21\\times 10^{-3}$, round to two decimal places):  

**Q29.** A first-order reaction is $50\\%$ complete in $20\\text{ minutes}$. The time (in minutes) required for $75\\%$ completion of the reaction is:  

**Q30.** The molality of a solution containing $18.0\\text{ g}$ of glucose (molar mass $180\\text{ g/mol}$) in $500\\text{ g}$ of water (in mol/kg) is:  

---

### SECTION 3: Non-Negative Integer Questions (Qs 31–36)
*Marking Scheme: +3 for correct integer, -1 for incorrect, 0 if unanswered.*

**Q31.** The oxidation state of sulfur in Caro's acid (peroxomonosulfuric acid, $\\text{H}_2\\text{SO}_5$) is:  

**Q32.** The total number of unpaired electrons in a free gaseous $\\text{Fe}^{3+}$ ion ($3d^5$) is:  

**Q33.** The number of bridging oxygen atoms in a molecule of pyrophosphate ion ($\\text{P}_2\\text{O}_7^{4-}$) is:  

**Q34.** The coordination number of cesium ion ($\\text{Cs}^+$) in the cesium chloride ($\\text{CsCl}$) crystal lattice is:  

**Q35.** The maximum number of isomers (structural + stereoisomers) for coordination compound $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$ is:  

**Q36.** The total number of $\\sigma$-bonds in a molecule of benzene ($\\text{C}_6\\text{H}_6$) is:  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: One or More Than One Correct Option (Qs 37–42)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q37.** Let $f(x) = \\frac{x}{1 + x^2}$ for all $x \\in \\mathbb{R}$:
(A) $f(x)$ is an odd function.  
(B) The range of $f(x)$ is $[-1/2, 1/2]$.  
(C) $f(x)$ attains its absolute maximum at $x = 1$.  
(D) $f(x)$ attains its absolute minimum at $x = -1$.  

**Q38.** For the circle $x^2 + y^2 = r^2$:
(A) The equation of the tangent at $(x_1, y_1)$ is $x x_1 + y y_1 = r^2$.  
(B) The condition for the line $y = m x + c$ to be tangent to the circle is $c^2 = r^2(1 + m^2)$.  
(C) Tangents drawn from any external point to the circle are equal in length.  
(D) The director circle is $x^2 + y^2 = 2r^2$.  

**Q39.** Let $A$ be a $3 \\times 3$ matrix such that $A^2 = A$ (idempotent matrix):
(A) The only possible eigenvalues of $A$ are 0 and 1.  
(B) $\\det(A)$ is either 0 or 1.  
(C) $\\text{tr}(A) = \\text{rank}(A)$.  
(D) $I - A$ is also an idempotent matrix.  

**Q40.** Let $I = \\int_{0}^{\\pi/2} \\ln(\\sin x)\\,dx$:
(A) $I = \\int_{0}^{\\pi/2} \\ln(\\cos x)\\,dx$.  
(B) $2I = \\int_{0}^{\\pi/2} \\ln(\\frac{1}{2}\\sin 2x)\\,dx$.  
(C) $I = -\\frac{\\pi}{2}\\ln 2$.  
(D) $\\int_{0}^{\\pi/2} \\ln(\\tan x)\\,dx = 0$.  

**Q41.** For two events $A$ and $B$:
(A) $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$.  
(B) $P(A \\cap B) = P(A) P(B|A)$.  
(C) $P(A' \\cap B') = 1 - P(A \\cup B)$.  
(D) If $P(A|B) = P(A)$, then $P(B|A) = P(B)$.  

**Q42.** Let $\\vec{a}, \\vec{b}, \\vec{c}$ be unit vectors such that $\\vec{a} + \\vec{b} + \\vec{c} = \\vec{0}$:
(A) $\\vec{a} \\cdot \\vec{b} = -1/2$.  
(B) The vectors form an equilateral triangle.  
(C) $\\vec{a} \\cdot \\vec{b} + \\vec{b} \\cdot \\vec{c} + \\vec{c} \\cdot \\vec{a} = -3/2$.  
(D) $\\vec{a} \\times \\vec{b} = \\vec{b} \\times \\vec{c} = \\vec{c} \\times \\vec{a}$.  

---

### SECTION 2: Numerical Value Questions (Qs 43–48)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q43.** The value of the integral
$$I = \\int_{0}^{1} x e^x\\,dx$$
is: (Round to two decimal places, $e \\approx 2.72$)  

**Q44.** The maximum value of $f(x) = \\cos x$ on $\\mathbb{R}$ is:  

**Q45.** The distance between the parallel lines $4x + 3y = 12$ and $4x + 3y = 2$ is:  

**Q46.** The length of the latus rectum of the parabola $y^2 = 12x$ is:  

**Q47.** The sum of the infinite series $\\sum_{n=0}^{\\infty} (1/2)^n$ is:  

**Q48.** If the vectors $\\vec{u} = \\hat{i} + \\hat{j}$ and $\\vec{v} = \\hat{i} + k\\hat{j}$ are perpendicular, the value of $k$ is:  

---

### SECTION 3: Non-Negative Integer Questions (Qs 49–54)
*Marking Scheme: +3 for correct integer, -1 for incorrect, 0 if unanswered.*

**Q49.** The number of ways to choose 2 items from a set of 5 distinct items ($\\binom{5}{2}$) is:  

**Q50.** The order of the differential equation $\\frac{d^2 y}{dx^2} + 5\\frac{dy}{dx} + 6y = 0$ is:  

**Q51.** The value of $\\lim_{x \\to 0} \\frac{\\sin 5x}{x}$ is:  

**Q52.** The number of real solutions of the equation $x^2 + 1 = 0$ is:  

**Q53.** The radius of the circle $x^2 + y^2 = 49$ is:  

**Q54.** The value of the sum of the roots of the equation $x^2 - 5x + 6 = 0$ is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_2.md"), "w", encoding="utf-8") as f:
    f.write(p2_content)
print("Generated mock_tests/Mock_09_IIT_Guwahati/Paper_2.md")

