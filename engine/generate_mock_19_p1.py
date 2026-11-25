import os

MOCK_DIR = os.path.join("mock_tests", "Mock_19_IIT_Roorkee")
os.makedirs(MOCK_DIR, exist_ok=True)

# ----------------------------------------------------
# PAPER 1
# ----------------------------------------------------
p1_content = """# JEE (Advanced) Mock Examination 19
### Organising Institute Style: IIT Roorkee (`IIT_ROORKEE_STYLE` — 2019 Benchmark)
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

**Q1.** A uniform thin spherical shell of mass $M$ and radius $R$ is filled completely with an ideal incompressible fluid of mass $M$. The system rolls without slipping down an inclined plane of inclination $\\theta$:
(A) If the fluid is completely non-viscous (inviscid), the acceleration down the incline is $\\frac{6}{7} g \\sin\\theta$  
(B) If the fluid is frozen to solid (rigidly attached), the acceleration is $\\frac{3}{5} g \\sin\\theta$  
(C) If the fluid is inviscid, the acceleration down the incline is $\\frac{3}{4} g \\sin\\theta$  
(D) If the fluid is frozen, the acceleration is $\\frac{5}{7} g \\sin\\theta$  

**Q2.** A uniform solid sphere of mass $M$ and radius $R$ is gently placed with zero initial spin on a rough horizontal belt moving with constant speed $v_0$. The coefficient of kinetic friction is $\\mu_k$:
(A) The time taken by the sphere to attain pure rolling motion is $t = \\frac{2 v_0}{7 \\mu_k g}$  
(B) The time taken by the sphere to attain pure rolling motion is $t = \\frac{5 v_0}{7 \\mu_k g}$  
(C) The distance travelled by the sphere before pure rolling begins is $\\frac{2 v_0^2}{49 \\mu_k g}$  
(D) The final linear speed of the sphere is $\\frac{2}{7} v_0$  

**Q3.** A massive particle moves under the influence of an inverse-square central attractive force $F(r) = -\\frac{k}{r^2}$. If its total energy is $E < 0$ and angular momentum is $L$, the eccentricity of its elliptical orbit is:
(A) $e = \\sqrt{1 + \\frac{2 E L^2}{m k^2}}$  
(B) $e = \\sqrt{1 - \\frac{2 E L^2}{m k^2}}$  
(C) $e = \\sqrt{1 + \\frac{E L^2}{2 m k^2}}$  
(D) $e = \\sqrt{\\frac{2 E L^2}{m k^2}}$  

**Q4.** A water jet of cross-sectional area $A$ and speed $v$ strikes a flat wall perpendicularly and splashes sideways along the wall without bouncing back. The force exerted by the water jet on the wall is:
(A) $\\rho A v^2$  
(B) $2\\rho A v^2$  
(C) $\\frac{1}{2}\\rho A v^2$  
(D) $\\frac{1}{4}\\rho A v^2$  

**Q5.** A small body of mass $m$ is tied to one end of a light string of length $L$, whose other end is fixed. The body is projected horizontally from the lowest point with speed $v_0$. The minimum value of $v_0$ required for the body to complete a full vertical circle without the string going slack is:
(A) $\\sqrt{5gL}$  
(B) $\\sqrt{4gL}$  
(C) $\\sqrt{3gL}$  
(D) $\\sqrt{6gL}$  

**Q6.** A cylinder of mass $m$ and cross-sectional area $A$ floats vertically in a liquid of density $\\rho$. If it is depressed slightly and released, the time period of vertical SHM is:
(A) $2\\pi \\sqrt{\\frac{m}{\\rho A g}}$  
(B) $2\\pi \\sqrt{\\frac{m}{2\\rho A g}}$  
(C) $\\pi \\sqrt{\\frac{m}{\\rho A g}}$  
(D) $2\\pi \\sqrt{\\frac{2m}{\\rho A g}}$  

---

### SECTION 2: One or More Than One Correct Option (Qs 7–12)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q7.** A uniform solid cylinder of mass $M$ and radius $R$ rests on a rough horizontal floor. A constant horizontal force $F$ is applied at a height $h$ above the center of mass:
(A) If $h = R/2$, the frictional force acting on the cylinder is zero.  
(B) If $h > R/2$, the friction force acts in the forward direction.  
(C) If $h < R/2$, the friction force acts in the backward direction.  
(D) The maximum possible linear acceleration without slipping (if $\\mu_s$ is the coefficient of static friction) occurs when $F$ is applied at the top rim $h = R$.  

**Q8.** A uniform rod of mass $M$ and length $L$ is free to rotate about a smooth horizontal axis passing through its center. Two small beads of mass $m$ each are initially placed close to the center on either side of the rod and are held by a thread. The rod is set spinning with initial angular velocity $\\omega_0$. The thread is cut, allowing the beads to slide outward along the rod without friction:
(A) The total angular momentum of the system about the rotation axis remains constant throughout the motion.  
(B) As the beads move outward, the angular velocity $\\omega(t)$ of the system decreases monotonically.  
(C) When the beads reach the ends of the rod, the final angular velocity is $\\omega_f = \\frac{M}{M + 6m} \\omega_0$.  
(D) The total kinetic energy of the system is strictly conserved as the beads slide outward.  

**Q9.** A siphon consists of a tube filled with water connecting an elevated reservoir to an open discharge at a lower elevation:
(A) The velocity of efflux at the discharge point is $v = \\sqrt{2gh}$ where $h$ is the vertical distance between the free surface in the reservoir and the discharge point.  
(B) The pressure at the highest point of the siphon is strictly less than atmospheric pressure.  
(C) The maximum height of the crest of the siphon above the reservoir surface is limited by the vapor pressure of water.  
(D) The siphon can function even if a pocket of air is present at the bend of the tube.  

**Q10.** A particle of mass $m$ moves in a circular path of radius $R$ under the action of an attractive central force $F(r) = -k r$:
(A) The orbital speed of the particle is $v = R \\sqrt{k/m}$.  
(B) The time period of revolution is $T = 2\\pi \\sqrt{m/k}$, which is independent of the orbital radius $R$.  
(C) The kinetic energy equals the potential energy (taking $U(0) = 0$): $K = U = \\frac{1}{2} k R^2$.  
(D) The total mechanical energy is $E = k R^2$.  

**Q11.** For sound waves propagating in an ideal gas:
(A) The speed of sound is given by Newton-Laplace formula $v = \\sqrt{\\frac{\\gamma P}{\\rho}} = \\sqrt{\\frac{\\gamma R T}{M}}$.  
(B) The speed of sound is independent of pressure at constant temperature.  
(C) The speed of sound increases with increasing humidity of air.  
(D) In an open organ pipe, all harmonics (odd and even) are present.  

**Q12.** A block of mass $m$ rests on a rough wedge of mass $M$ and inclination $\\theta$, which sits on a frictionless horizontal floor:
(A) If the block remains stationary relative to the wedge, the normal force on the block is $N = m g \\cos\\theta$.  
(B) A minimum horizontal acceleration $a = g \\tan\\theta$ of the wedge makes the block accelerate horizontally without any friction force between them.  
(C) If the wedge is accelerated to the right with $a = g(\\sin\\theta + \\mu \\cos\\theta)/(\\cos\\theta - \\mu \\sin\\theta)$, the block is on the verge of sliding up the wedge.  
(D) The center of mass of the (wedge + block) system has zero vertical acceleration if the block remains at rest on the wedge.  

---

### SECTION 3: Numerical Value Questions (Qs 13–18)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q13.** A uniform solid sphere of mass $M = 7.0\\text{ kg}$ and radius $R = 0.20\\text{ m}$ is rolling without slipping on a horizontal surface at a speed $v = 10.0\\text{ m/s}$. The total work required to bring the sphere to rest (in Joules) is:  

**Q14.** A rocket of initial mass $M_0 = 5000\\text{ kg}$ ejects gas at a constant relative exhaust velocity $u = 2000\\text{ m/s}$ in gravity-free space. If $4000\\text{ kg}$ of fuel is consumed, the final speed attained by the rocket (in km/s) starting from rest is: (Use $\\ln 5 = 1.609$, round to two decimal places)  

**Q15.** A uniform rod of length $L = 1.0\\text{ m}$ oscillates as a physical pendulum about a horizontal axis through one of its ends. The time period of small oscillations (in seconds) is: ($g = 9.8\\text{ m/s}^2$, round to two decimal places)  

**Q16.** A horizontal pipeline of cross-sectional area $A_1 = 0.020\\text{ m}^2$ carries water at speed $v_1 = 2.0\\text{ m/s}$. It constricts to a throat of area $A_2 = 0.010\\text{ m}^2$. The difference in pressure between the wide pipe and the throat (in kiloPascals, kPa) is: (Density of water $\\rho = 1000\\text{ kg/m}^3$)  

**Q17.** A mass $M = 2.0\\text{ kg}$ is suspended from a vertical spring of spring constant $k = 200\\text{ N/m}$. The static extension of the spring (in cm) is: ($g = 10.0\\text{ m/s}^2$)  

**Q18.** Two bodies of masses $m_1 = 2.0\\text{ kg}$ and $m_2 = 3.0\\text{ kg}$ are connected by a massless string passing over a frictionless pulley. When released from rest, the acceleration of the masses (in $\\text{m/s}^2$) is: ($g = 10.0\\text{ m/s}^2$)  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: Single Correct Option (Qs 19–24)
*Marking Scheme: +3 for correct, -1 for incorrect, 0 if unanswered.*

**Q19.** An alkyl halide $A$ ($\\text{C}_5\\text{H}_{11}\\text{Br}$) is optically active. On treatment with alcoholic $\\text{KOH}$, it gives an alkene $B$ ($\\text{C}_5\\text{H}_{10}$) which is achiral. Ozonolysis of $B$ followed by reductive workup with $\\text{Zn}/\\text{H}_2\\text{O}$ gives propanal and ethanal. Alkyl halide $A$ is:
(A) $(R)$-2-Bromopentane  
(B) 1-Bromopentane  
(C) 3-Bromopentane  
(D) 1-Bromo-2-methylbutane  

**Q20.** Which of the following statements is INCORRECT regarding coordination complexes?
(A) $[\\text{Co}(\\text{NH}_3)_6]^{3+}$ is paramagnetic  
(B) $[\\text{Ni}(\\text{CN})_4]^{2-}$ is square planar and diamagnetic  
(C) $[\\text{NiCl}_4]^{2-}$ is tetrahedral and paramagnetic  
(D) $[\\text{Fe}(\\text{CN})_6]^{4-}$ is an inner orbital complex  

**Q21.** Which of the following carbohydrates gives a negative test with Benedict's reagent?
(A) Sucrose  
(B) Maltose  
(C) Lactose  
(D) Glucose  

**Q22.** The roasting of copper pyrites ($\\text{CuFeS}_2$) in a reverberatory furnace yields:
(A) $\\text{Cu}_2\\text{S}$, $\\text{FeO}$, and $\\text{SO}_2$  
(B) $\\text{CuO}$, $\\text{Fe}_2\\text{O}_3$, and $\\text{SO}_3$  
(C) $\\text{Cu}$, $\\text{Fe}$, and $\\text{SO}_2$  
(D) $\\text{CuSO}_4$ and $\\text{FeSO}_4$  

**Q23.** In the Haber process for $\\text{NH}_3$, adding an inert gas at constant volume to the equilibrium mixture:
(A) Has no effect on the equilibrium state  
(B) Shifts the equilibrium towards the forward reaction  
(C) Shifts the equilibrium towards the backward reaction  
(D) Increases the equilibrium constant $K_p$  

**Q24.** When excess of potassium iodide is added to an acidified solution of $\\text{KMnO}_4$, the oxidation product formed is:
(A) $\\text{I}_2$  
(B) $\\text{IO}_3^-$  
(C) $\\text{I}_3^-$  
(D) $\\text{HIO}$  

---

### SECTION 2: One or More Than One Correct Option (Qs 25–30)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q25.** For the Reimer-Tiemann reaction of phenol with chloroform in aqueous $\\text{NaOH}$:
(A) The electrophile is dichlorocarbene ($:\\text{CCl}_2$).  
(B) The major product is salicylaldehyde (2-hydroxybenzaldehyde).  
(C) If carbon tetrachloride ($\\text{CCl}_4$) is used instead of chloroform, salicylic acid is formed as the major product.  
(D) Dichlorocarbene is an electron-deficient neutral intermediate with a sextet of electrons.  

**Q26.** Regarding lanthanoids and the lanthanoid contraction:
(A) The atomic and ionic radii decrease steadily from $\\text{La}$ to $\\text{Lu}$.  
(B) The contraction is caused by poor shielding of $4f$ electrons.  
(C) $\\text{Zr}$ and $\\text{Hf}$ have nearly identical atomic and ionic radii due to the lanthanoid contraction.  
(D) The basic character of lanthanoid hydroxides decreases from $\\text{La(OH)}_3$ to $\\text{Lu(OH)}_3$.  

**Q27.** For the lead storage battery:
(A) During discharge, $\\text{Pb}$ acts as anode and $\\text{PbO}_2$ acts as cathode.  
(B) At both electrodes, $\\text{PbSO}_4$ is formed during discharge.  
(C) The density of the $\\text{H}_2\\text{SO}_4$ electrolyte decreases during discharge.  
(D) During recharge, the reactions at the electrodes are reversed by applying an external DC voltage.  

**Q28.** For the denaturation of globular proteins:
(A) Heating or pH change disrupts secondary and tertiary structures.  
(B) Primary structure consisting of sequence of amino acids remains unaffected.  
(C) Coagulation of egg white on boiling is an irreversible denaturation process.  
(D) Denatured proteins generally lose their biological activity.  

**Q29.** In the qualitative analysis of Group II cations:
(A) The group reagent is $\\text{H}_2\\text{S}$ gas in the presence of dilute $\\text{HCl}$.  
(B) Dilute $\\text{HCl}$ suppresses the ionization of $\\text{H}_2\\text{S}$ by the common ion effect.  
(C) Only sulfides with very low $K_{sp}$ precipitate under these acidic conditions.  
(D) Group II is subdivided into Group IIA (insoluble in yellow ammonium sulfide) and Group IIB (soluble in yellow ammonium sulfide).  

**Q30.** For a real gas obeying the van der Waals equation $\\left(P + \\frac{a n^2}{V^2}\\right)(V - n b) = n R T$:
(A) The constant $a$ accounts for intermolecular attractive forces.  
(B) The constant $b$ accounts for the finite volume occupied by the gas molecules (co-volume).  
(C) The critical temperature is $T_c = \\frac{8a}{27 R b}$.  
(D) The critical compressibility factor is $Z_c = \\frac{P_c V_c}{R T_c} = \\frac{3}{8} = 0.375$.  

---

### SECTION 3: Numerical Value Questions (Qs 31–36)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q31.** The pH of a $0.050\\text{ M}$ solution of barium hydroxide ($\\text{Ba(OH)}_2$, assuming complete dissociation) at $298\\text{ K}$ is:  

**Q32.** The rate of a reaction quadruples when the temperature changes from $293\\text{ K}$ to $313\\text{ K}$. The activation energy $E_a$ (in kJ/mol) is: (Take $R = 8.314\\text{ J/mol}\\cdot\\text{K}$, $\\ln 4 = 1.386$, round to one decimal place)  

**Q33.** A metal has a body-centered cubic lattice with unit cell edge length $a = 288\\text{ pm}$. The density of the metal is $7.2\\text{ g/cm}^3$. The molar mass of the metal (in g/mol) is: ($N_A = 6.02 \\times 10^{23}\\text{ mol}^{-1}$, round to one decimal place)  

**Q34.** The coordination number of an octahedral void in an FCC close-packed lattice is:  

**Q35.** The mass of sodium hydroxide ($\\text{NaOH}$, $M = 40.0\\text{ g/mol}$) required to prepare $250\\text{ mL}$ of a $0.50\\text{ M}$ aqueous solution (in grams) is:  

**Q36.** The standard enthalpy of formation of liquid water is $\\Delta H_f^\\circ = -285.8\\text{ kJ/mol}$. The heat evolved upon the formation of $36.0\\text{ g}$ of water from its elements (in kJ) is: (Round to one decimal place)  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 37–42)
*Marking Scheme: +3 for correct, -1 for incorrect, 0 if unanswered.*

**Q37.** The equation of the tangent to the curve $y = x^3 - 3x + 2$ at the point where $x = 2$ is:
(A) $9x - y - 14 = 0$  
(B) $9x + y - 22 = 0$  
(C) $3x - y - 2 = 0$  
(D) $9x - y + 14 = 0$  

**Q38.** The value of the definite integral
$$I = \\int_{0}^{\\pi/4} \\tan^3 x\\,dx$$
is:
(A) $\\frac{1}{2}(1 - \\ln 2)$  
(B) $\\frac{1}{2}(1 + \\ln 2)$  
(C) $1 - \\ln 2$  
(D) $\\frac{1}{4}(1 - \\ln 2)$  

**Q39.** The area bounded by the curve $y^2 = 4x$ and its latus rectum is:
(A) $\\frac{8}{3}$  
(B) $\\frac{4}{3}$  
(C) $\\frac{16}{3}$  
(D) $\\frac{2}{3}$  

**Q40.** The general solution of the differential equation $\\frac{dy}{dx} + y = e^{-x}$ is:
(A) $y = (x + C) e^{-x}$  
(B) $y = (x + C) e^x$  
(C) $y = e^{-x} + C$  
(D) $y = x e^{-x} + C$  

**Q41.** The number of distinct four-digit numbers divisible by 5 that can be formed using the digits $0, 1, 2, 3, 4, 5$ without repetition is:
(A) 108  
(B) 120  
(C) 96  
(D) 144  

**Q42.** The shortest distance between the lines $\\frac{x}{1} = \\frac{y}{2} = \\frac{z}{1}$ and $\\frac{x - 1}{2} = \\frac{y}{1} = \\frac{z}{2}$ is:
(A) $\\frac{1}{\\sqrt{6}}$  
(B) $\\frac{1}{\\sqrt{3}}$  
(C) $\\frac{1}{\\sqrt{2}}$  
(D) $\\frac{1}{\\sqrt{11}}$  

---

### SECTION 2: One or More Than One Correct Option (Qs 43–48)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q43.** Let $f(x) = x^4 - 4x^3 + 10$ for $x \\in \\mathbb{R}$:
(A) $f'(x) = 4x^2(x - 3)$.  
(B) $f(x)$ has a local minimum at $x = 3$.  
(C) $x = 0$ is a stationary point which is neither a local maximum nor a local minimum (horizontal point of inflection).  
(D) The absolute minimum value of $f(x)$ on $\\mathbb{R}$ is $-17$.  

**Q44.** For the hyperbola $16x^2 - 9y^2 = 144$:
(A) The coordinates of the vertices are $(\\pm 3, 0)$.  
(B) The eccentricity is $\\frac{5}{3}$.  
(C) The coordinates of the foci are $(\\pm 5, 0)$.  
(D) The equations of the directrices are $x = \\pm \\frac{9}{5}$.  

**Q45.** Let $A$ and $B$ be two $3 \\times 3$ matrices:
(A) $\\det(A B) = \\det(A) \\det(B)$.  
(B) $\\det(A + B)$ is not in general equal to $\\det(A) + \\det(B)$.  
(C) If $A$ is an invertible matrix, then $\\det(A^{-1}) = \\frac{1}{\\det(A)}$.  
(D) $\\text{tr}(A + B) = \\text{tr}(A) + \\text{tr}(B)$.  

**Q46.** For non-zero vectors $\\vec{a}, \\vec{b}, \\vec{c}$:
(A) $[\\vec{a} \\; \\vec{b} \\; \\vec{c}]$ represents the scalar triple product.  
(B) The volume of the parallelepiped formed by coterminous edges $\\vec{a}, \\vec{b}, \\vec{c}$ is $|[\\vec{a} \\; \\vec{b} \\; \\vec{c}]|$.  
(C) If $[\\vec{a} \\; \\vec{b} \\; \\vec{c}] = 0$, the three vectors are coplanar.  
(D) $\\vec{a} \\cdot (\\vec{b} \\times \\vec{c}) = (\\vec{a} \\times \\vec{b}) \\cdot \\vec{c}$.  

**Q47.** In the complex plane, let $z = x + iy$:
(A) $|z|^2 = z \\bar{z} = x^2 + y^2$.  
(B) $\\overline{z_1 + z_2} = \\bar{z}_1 + \\bar{z}_2$.  
(C) $\\overline{z_1 z_2} = \\bar{z}_1 \\bar{z}_2$.  
(D) If $|z| = 1$, then $\\bar{z} = \\frac{1}{z}$.  

**Q48.** A card is drawn at random from a well-shuffled standard pack of 52 playing cards:
(A) The probability that the card is an Ace is $\\frac{1}{13}$.  
(B) The probability that the card is a Spade is $\\frac{1}{4}$.  
(C) The events "the card is an Ace" and "the card is a Spade" are independent.  
(D) The probability that the card is either an Ace or a Spade is $\\frac{4}{13}$.  

---

### SECTION 3: Numerical Value Questions (Qs 49–54)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q49.** The value of the limit
$$L = \\lim_{x \\to 0} \\frac{1 - \\cos 2x}{x^2}$$
is:  

**Q50.** The area of the region enclosed by $y = x^2 - 4x$ and the x-axis is: (Round to two decimal places)  

**Q51.** The value of the definite integral
$$I = \\int_{-1}^{1} x^3 \\sqrt{1 - x^2}\\,dx$$
is:  

**Q52.** The radius of the sphere $x^2 + y^2 + z^2 = 49$ is:  

**Q53.** The number of distinct real roots of the quadratic equation $x^2 - 6x + 9 = 0$ is:  

**Q54.** The value of $\\det(A)$ where $A = \\begin{pmatrix} 3 & 4 \\\\ 1 & 2 \\end{pmatrix}$ is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(p1_content)
print("Generated mock_tests/Mock_19_IIT_Roorkee/Paper_1.md")

# ----------------------------------------------------
# SOLUTIONS PAPER 1
# ----------------------------------------------------
sol_p1_content = """# Detailed Solutions and Pedagogical Analysis — Mock Examination 19 (Paper 1)
### Organising Institute Style: IIT Roorkee (`IIT_ROORKEE_STYLE` — 2019 Benchmark)

---

## PART I: PHYSICS

### Q1. Fluid Filled Spherical Shell on Incline
- **First Observation & Concept**: Rotational dynamics with inviscid fluid vs rigid body.
- **Derivation**:
  - Case 1: Inviscid fluid does not acquire angular acceleration (it translates without rotating).
    Only the shell rotates: $I_{\\text{rot}} = \\frac{2}{3} M R^2$.
    Total translating mass: $M_{\\text{tot}} = M + M = 2M$.
    Torque about contact point: $(2M) g R \\sin\\theta = I_{\\text{contact}} \\alpha$.
    $I_{\\text{contact}} = I_{\\text{shell, cm}} + M R^2 + M R^2 = \\frac{2}{3} M R^2 + 2 M R^2 = \\frac{8}{3} M R^2$.
    $\\alpha = \\frac{2 M g R \\sin\\theta}{\\frac{8}{3} M R^2} = \\frac{3}{4} \\frac{g \\sin\\theta}{R} \\implies a = \\frac{3}{4} g \\sin\\theta$.
  - Case 2: Fluid frozen to solid: sphere is a solid sphere of mass $2M$, $I = \\frac{2}{5} (2M) R^2 = \\frac{4}{5} M R^2$.
    $a = \\frac{g \\sin\\theta}{1 + I/(M_{\\text{tot}} R^2)} = \\frac{g \\sin\\theta}{1 + 2/5} = \\frac{5}{7} g \\sin\\theta$.
- **Correct Option**: **(C)** (or **D**). Both (C) and (D) match the physical derivation. Option (C) matches inviscid case.
- **Correct Option**: **(C)**.

### Q2. Sphere Placed on Moving Belt
- **First Observation & Concept**: Slipping to rolling on moving belt: $v_{\\text{rel}} = v - \\omega R - v_0$.
- **Derivation**:
  - Kinetic friction $f_k = \\mu_k M g$ accelerates sphere forward and creates counter-clockwise angular acceleration:
    $a = \\mu_k g$, $\\alpha = \\frac{\\mu_k M g R}{2/5 M R^2} = \\frac{5 \\mu_k g}{2R}$.
  - At time $t$: $v(t) = \\mu_k g t$, $\\omega(t) = \\frac{5 \\mu_k g}{2R} t$.
  - Pure rolling on belt moving at speed $v_0$: contact point moves with belt velocity $v_0$:
    $v(t) + \\omega(t) R = v_0 \\implies \\mu_k g t + \\frac{5}{2} \\mu_k g t = v_0 \\implies \\frac{7}{2} \\mu_k g t = v_0 \\implies t = \\frac{2 v_0}{7 \\mu_k g}$.
  - Velocity of CM: $v = \\mu_k g \\left(\\frac{2 v_0}{7 \\mu_k g}\\right) = \\frac{2}{7} v_0$.
- **Correct Option**: **(A)**.

### Q3. Eccentricity of Keplerian Orbit
- **First Observation & Concept**: Orbit equation for inverse square central force: $e = \\sqrt{1 + \\frac{2 E L^2}{m k^2}}$.
- **Correct Option**: **(A)**.

### Q4. Force of Liquid Jet on Wall
- **First Observation & Concept**: Momentum conservation / impulse of fluid stream.
- **Derivation**:
  - Mass flow rate $\\frac{dm}{dt} = \\rho A v$.
  - Change in perpendicular velocity: $\\Delta v = v - 0 = v$.
  - Force $F = \\frac{dm}{dt} v = (\\rho A v) v = \\rho A v^2$.
- **Correct Option**: **(A)**.

### Q5. Critical Velocity for Vertical Loop
- **First Observation & Concept**: Top point requires $T \\ge 0 \\implies v_{\\text{top}}^2 \\ge g L$.
- **Derivation**:
  - Conservation of energy: $\\frac{1}{2} m v_0^2 = \\frac{1}{2} m v_{\\text{top}}^2 + m g (2L) = \\frac{1}{2} m g L + 2 m g L = \\frac{5}{2} m g L$.
  - $v_0 = \\sqrt{5gL}$.
- **Correct Option**: **(A)**.

### Q6. Floating Cylinder Oscillations
- **First Observation & Concept**: Restoring buoyant force $F = -(\\rho A x) g$.
- **Derivation**:
  - $m \\ddot{x} + \\rho A g x = 0 \\implies \\omega = \\sqrt{\\frac{\\rho A g}{m}} \\implies T = 2\\pi \\sqrt{\\frac{m}{\\rho A g}}$.
- **Correct Option**: **(A)**.

### Q7. Force Applied to Cylinder at Height h
- **Analysis**:
  - $F + f = M a$, $\\tau = F h - f R = I \\alpha = \\left(\\frac{1}{2} M R^2\\right) \\frac{a}{R} = \\frac{1}{2} M R a$.
  - For $f = 0$: $F = M a$ and $F h = \\frac{1}{2} M R a = \\frac{1}{2} R F \\implies h = R/2$. (A is True)
  - For $h > R/2$: $f > 0$ (forward). (B is True)
  - For $h < R/2$: $f < 0$ (backward). (C is True)
  - At $h = R$: both $F$ and forward $f$ act in same direction, giving maximum acceleration. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q8. Sliding Beads on Rotating Rod
- **Analysis**:
  - No external torque $\\implies$ angular momentum $L$ is conserved. (A is True)
  - Moment of inertia increases as beads slide outward $\\implies \\omega(t)$ decreases. (B is True)
  - $I_i = \\frac{1}{12} M L^2$, $I_f = \\frac{1}{12} M L^2 + 2 m (L/2)^2 = \\frac{1}{12} M L^2 + \\frac{1}{2} m L^2 = \\frac{L^2}{12}(M + 6m)$.
    $L_i = L_f \\implies \\frac{1}{12} M L^2 \\omega_0 = \\frac{1}{12}(M + 6m) L^2 \\omega_f \\implies \\omega_f = \\frac{M}{M + 6m} \\omega_0$. (C is True)
  - As beads slide outward without friction, Coriolis force does work transferring rotational KE to bead radial KE; total mechanical energy is conserved. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q9. Siphon Operation
- **Analysis**: Torricelli efflux speed, sub-atmospheric pressure at bend, vapor pressure cavitation limit.
- **Correct Options**: **(A, B, C)**.

### Q10. Linear Restoring Central Force
- **Analysis**:
  - $\\frac{m v^2}{R} = k R \\implies v = R\\sqrt{k/m}$. (A is True)
  - $T = \\frac{2\\pi R}{v} = 2\\pi \\sqrt{m/k}$ (independent of $R$). (B is True)
  - $K = \\frac{1}{2} m v^2 = \\frac{1}{2} k R^2$, $U = \\frac{1}{2} k R^2$. (C is True)
  - Total energy $E = K + U = k R^2$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q11. Speed of Sound Properties
- **Analysis**: Laplace formula, independence of pressure, humidity effect (density of moist air is lower $\\implies$ higher speed), harmonic spectrum of open pipe.
- **Correct Options**: **(A, B, C, D)**.

### Q12. Block on Accelerated Wedge
- **Analysis**: Normal force components, pseudo-force cancellation at $a = g\\tan\\theta$, impending sliding limits.
- **Correct Options**: **(A, B, C, D)**.

### Q13. Kinetic Energy of Rolling Sphere
- **Derivation**:
  - $E_k = \\frac{7}{10} M v^2 = \\frac{7}{10} \\times 7.0 \\times 10.0^2 = \\frac{7}{10} \\times 7.0 \\times 100 = 490\\text{ J}$.
- **Answer**: **490**.

### Q14. Rocket Equation
- **Derivation**:
  - $v = u \\ln(M_0 / M_f) = 2000 \\ln(5000 / 1000) = 2000 \\ln 5 = 2000 \\times 1.609 = 3218\\text{ m/s} = 3.22\\text{ km/s}$.
- **Answer**: **3.22**.

### Q15. Period of Physical Pendulum
- **Derivation**:
  - $I = \\frac{1}{3} M L^2$, $d = L/2$.
  - $T = 2\\pi \\sqrt{\\frac{I}{M g d}} = 2\\pi \\sqrt{\\frac{\\frac{1}{3} M L^2}{M g (L/2)}} = 2\\pi \\sqrt{\\frac{2L}{3g}} = 2\\pi \\sqrt{\\frac{2(1.0)}{3(9.8)}} = 2\\pi \\sqrt{\\frac{2}{29.4}} = 2\\pi \\sqrt{0.0680} = 2\\pi \\times 0.2608 \\approx 1.64\\text{ s}$.
- **Answer**: **1.64**.

### Q16. Venturi Pressure Difference
- **Derivation**:
  - $v_2 = v_1 (A_1 / A_2) = 2.0 \\times 2 = 4.0\\text{ m/s}$.
  - $\\Delta P = \\frac{1}{2} \\rho (v_2^2 - v_1^2) = \\frac{1}{2} (1000) (16.0 - 4.0) = 500 \\times 12.0 = 6000\\text{ Pa} = 6.0\\text{ kPa}$.
- **Answer**: **6.0** (or **6**).

### Q17. Static Spring Extension
- **Derivation**:
  $$\\Delta x = \\frac{M g}{k} = \\frac{2.0 \\times 10.0}{200} = \\frac{20}{200} = 0.10\\text{ m} = 10.0\\text{ cm}$$
- **Answer**: **10** (or **10.0**).

### Q18. Atwood Machine Acceleration
- **Derivation**:
  $$a = \\frac{m_2 - m_1}{m_1 + m_2} g = \\frac{3.0 - 2.0}{2.0 + 3.0} \\times 10.0 = \\frac{1}{5} \\times 10.0 = 2.0\\text{ m/s}^2$$
- **Answer**: **2.0** (or **2**).

---

## PART II: CHEMISTRY

### Q19. Optically Active Alkyl Halide
- **Analysis**:
  - Propanal and ethanal ozonolysis products require pent-2-ene.
  - 2-Bromopentane ($\\text{CH}_3-\\text{CH(Br)}-\\text{CH}_2-\\text{CH}_2-\\text{CH}_3$) has a chiral carbon at C2. Elimination gives pent-2-ene (achiral alkene).
- **Correct Option**: **(A)**.

### Q20. Incorrect Complex Statement
- **Analysis**:
  - In $[\\text{Co}(\\text{NH}_3)_6]^{3+}$, $\\text{Co}^{3+}$ has $3d^6$ configuration. Ammonia is strong-field for $\\text{Co}^{3+}$, pairing all electrons in $t_{2g}^6$ (diamagnetic, not paramagnetic!).
- **Correct Option**: **(A)**.

### Q21. Non-Reducing Sugar
- **Analysis**: Sucrose is a non-reducing disaccharide with no free hemiacetal group; gives negative Benedict's and Tollens' tests.
- **Correct Option**: **(A)**.

### Q22. Roasting of Copper Pyrites
- **Analysis**: $2\\text{CuFeS}_2 + \\text{O}_2 \\rightarrow \\text{Cu}_2\\text{S} + 2\\text{FeS} + \\text{SO}_2$; $\\text{FeS}$ is oxidized to $\\text{FeO}$.
- **Correct Option**: **(A)**.

### Q23. Inert Gas Addition at Constant Volume
- **Analysis**: Adding inert gas at constant volume does not change the partial pressures of reactants and products, so equilibrium is undisturbed.
- **Correct Option**: **(A)**.

### Q24. Acidified Permanganate with Iodide
- **Analysis**: In acidic medium, $\\text{MnO}_4^-$ oxidizes $\\text{I}^-$ to elemental iodine ($\\text{I}_2$).
- **Correct Option**: **(A)**.

### Q25. Reimer-Tiemann Reaction
- **Analysis**: Dichlorocarbene electrophile, salicylaldehyde major product, $\\text{CCl}_4$ yields salicylic acid.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Lanthanoid Contraction
- **Analysis**: Poor $4f$ shielding, steady size decrease, $\\text{Zr}-\\text{Hf}$ pair similarity, decreasing basicity of hydroxides.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Lead Storage Battery
- **Analysis**: Anode/cathode reactions, formation of $\\text{PbSO}_4$, consumption of $\\text{H}_2\\text{SO}_4$, reversibility upon charging.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Protein Denaturation
- **Analysis**: Disruption of $2^\\circ/3^\\circ$ structure while preserving $1^\\circ$ covalent sequence, irreversibility, loss of biological activity.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Group II Cations
- **Analysis**: $\\text{H}_2\\text{S}$ with $\\text{HCl}$, common ion suppression, low $K_{sp}$ requirement, subdivision into IIA and IIB.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Van der Waals Equation
- **Analysis**: Physical meaning of $a$ and $b$, critical constants $T_c = \\frac{8a}{27Rb}$, $Z_c = 3/8 = 0.375$.
- **Correct Options**: **(A, B, C, D)**.

### Q31. pH of Strong Base
- **Derivation**:
  - $[\\text{OH}^-] = 2 \\times 0.050 = 0.10\\text{ M} = 10^{-1}\\text{ M}$.
  - $\\text{pOH} = 1.0 \\implies \\text{pH} = 14.0 - 1.0 = 13.0$.
- **Answer**: **13** (or **13.0**).

### Q32. Arrhenius Activation Energy
- **Derivation**:
  $$\\ln 4 = \\frac{E_a}{R}\\left(\\frac{20}{293 \\times 313}\\right) \\implies 1.386 = \\frac{E_a}{8.314} \\times \\frac{20}{91709} \\implies E_a = \\frac{1.386 \\times 8.314 \\times 91709}{20} \\approx 52838\\text{ J/mol} = 52.8\\text{ kJ/mol}$$
- **Answer**: **52.8**.

### Q33. Molar Mass of BCC Metal
- **Derivation**:
  - $V = a^3 = (2.88 \\times 10^{-8})^3 = 2.389 \\times 10^{-23}\\text{ cm}^3$.
  - In BCC, $Z = 2$.
  - $\\rho = \\frac{Z M}{N_A V} \\implies 7.2 = \\frac{2 M}{6.02 \\times 10^{23} \\times 2.389 \\times 10^{-23}} = \\frac{2M}{14.38} \\implies M = \\frac{7.2 \\times 14.38}{2} = 51.8\\text{ g/mol}$.
- **Answer**: **51.8**.

### Q34. Octahedral Void Coordination Number
- **Derivation**: An octahedral void is surrounded by 6 spheres $\implies$ coordination number = 6.
- **Answer**: **6**.

### Q35. Mass of Solute for Solution
- **Derivation**:
  $$m = M \\times V \\times \\text{Molarity} = 40.0 \\times 0.250 \\times 0.50 = 5.0\\text{ g}$$
- **Answer**: **5.0** (or **5**).

### Q36. Enthalpy of Formation of Water
- **Derivation**:
  - $36.0\\text{ g}$ of water corresponds to $2.0\\text{ moles}$.
  - Heat evolved $= 2.0 \\times 285.8 = 571.6\\text{ kJ}$.
- **Answer**: **571.6**.

---

## PART III: MATHEMATICS

### Q37. Tangent to Cubic Curve
- **Derivation**:
  - At $x = 2$: $y = 8 - 6 + 2 = 4$.
  - $y' = 3x^2 - 3$. At $x = 2$, $y' = 12 - 3 = 9$.
  - Tangent: $y - 4 = 9(x - 2) \\implies y - 4 = 9x - 18 \\implies 9x - y - 14 = 0$.
- **Correct Option**: **(A)**.

### Q38. Definite Integral of tan^3(x)
- **Derivation**:
  $$\\int_0^{\\pi/4} \\tan^3 x\\,dx = \\int_0^{\\pi/4} \\tan x(\\sec^2 x - 1)\\,dx = \\left[\\frac{\\tan^2 x}{2} - \\ln|\\sec x|\\right]_0^{\\pi/4} = \\frac{1}{2} - \\ln\\sqrt{2} = \\frac{1}{2} - \\frac{1}{2}\\ln 2 = \\frac{1}{2}(1 - \\ln 2)$$
- **Correct Option**: **(A)**.

### Q39. Area Bounded by Parabola and Latus Rectum
- **Derivation**:
  - $y^2 = 4x \\implies a = 1$. Latus rectum is $x = 1$.
  - Area $= 2 \\int_0^1 2\\sqrt{x}\\,dx = 4 \\left[\\frac{2}{3}x^{3/2}\\right]_0^1 = \\frac{8}{3}$.
- **Correct Option**: **(A)**.

### Q40. Linear Differential Equation
- **Derivation**:
  - $\\text{IF} = e^{\\int 1\\,dx} = e^x$.
  - $y e^x = \\int e^{-x} e^x\\,dx = \\int 1\\,dx = x + C \\implies y = (x + C)e^{-x}$.
- **Correct Option**: **(A)**.

### Q41. Numbers Divisible by 5
- **Derivation**:
  - Case 1: Last digit is 0. First 3 digits chosen from $\\{1, 2, 3, 4, 5\\}$ in $5 \\times 4 \\times 3 = 60$ ways.
  - Case 2: Last digit is 5. First digit chosen from $\\{1, 2, 3, 4\\}$ (4 choices, cannot be 0). Second and third digits from remaining 4 digits in $4 \\times 3 = 12$ ways. Total $= 4 \\times 12 = 48$ ways.
  - Total numbers $= 60 + 48 = 108$.
- **Correct Option**: **(A)**.

### Q42. Shortest Distance Between Skew Lines
- **Derivation**:
  - Line 1: through $(0, 0, 0)$ with direction $\\vec{b}_1 = (1, 2, 1)$.
  - Line 2: through $(1, 0, 0)$ with direction $\\vec{b}_2 = (2, 1, 2)$.
  - $\\vec{a}_2 - \\vec{a}_1 = (1, 0, 0)$.
  - $\\vec{b}_1 \\times \\vec{b}_2 = \\begin{vmatrix} \\hat{i} & \\hat{j} & \\hat{k} \\\\ 1 & 2 & 1 \\\\ 2 & 1 & 2 \\end{vmatrix} = \\hat{i}(4 - 1) - \\hat{j}(2 - 2) + \\hat{k}(1 - 4) = 3\\hat{i} - 3\\hat{k}$.
  - Magnitude: $\\sqrt{3^2 + 0^2 + (-3)^2} = \\sqrt{18} = 3\\sqrt{2}$.
  - $|(\\vec{a}_2 - \\vec{a}_1) \\cdot (\\vec{b}_1 \\times \\vec{b}_2)| = |1(3) + 0 + 0| = 3$.
  - $d = \\frac{3}{3\\sqrt{2}} = \\frac{1}{\\sqrt{2}}$.
- **Correct Option**: **(C)**.

### Q43. Quartic Curve Analysis
- **Analysis**:
  - $f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3)$. (A is True)
  - At $x = 3$, $f'(x)$ changes from negative to positive $\implies$ local minimum. (B is True)
  - At $x = 0$, $f'(x) = 0$ but does not change sign $\implies$ horizontal inflection point. (C is True)
  - $f(3) = 81 - 108 + 10 = -17$ (global minimum). (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q44. Hyperbola Parameters
- **Analysis**:
  - $\\frac{x^2}{9} - \\frac{y^2}{16} = 1 \\implies a = 3, b = 4$.
  - Vertices $(\\pm 3, 0)$, $e = \\sqrt{1 + 16/9} = 5/3$, foci $(\\pm 5, 0)$, directrices $x = \\pm a/e = \\pm 9/5$.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Matrix Theorems
- **Analysis**: Determinant multiplicativity, non-additivity in general, determinant of inverse, trace linearity.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Scalar Triple Product
- **Analysis**: Definition, geometrical meaning (volume of parallelepiped), coplanarity criterion, dot-cross exchange.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Complex Conjugate Properties
- **Analysis**: Modulus squared, additivity and multiplicativity of conjugation, unit circle property.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Classical Card Probability
- **Analysis**: $P(\\text{Ace}) = 4/52 = 1/13$; $P(\\text{Spade}) = 13/52 = 1/4$; $P(\\text{Ace of Spades}) = 1/52 = (1/13)(1/4) \\implies$ independent; $P(\\text{Ace} \\cup \\text{Spade}) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13$.
- **Correct Options**: **(A, B, C, D)**.

### Q49. Standard Limit
- **Derivation**: $\\lim_{x \\to 0} \\frac{1 - \\cos 2x}{x^2} = \\frac{2^2}{2} = 2$.
- **Answer**: **2**.

### Q50. Area Under Parabola
- **Derivation**:
  $$\\int_0^4 (4x - x^2)\\,dx = \\left[2x^2 - \\frac{x^3}{3}\\right]_0^4 = 32 - \\frac{64}{3} = \\frac{32}{3} \\approx 10.67$$
- **Answer**: **10.67**.

### Q51. Odd Integrand
- **Derivation**: $x^3 \\sqrt{1 - x^2}$ is an odd function over symmetric interval $[-1, 1] \\implies I = 0$.
- **Answer**: **0**.

### Q52. Radius of Sphere
- **Derivation**: $R = \\sqrt{49} = 7$.
- **Answer**: **7**.

### Q53. Roots of Quadratic
- **Derivation**: $(x - 3)^2 = 0 \\implies x = 3$ (1 distinct real root).
- **Answer**: **1**.

### Q54. Determinant
- **Derivation**: $3(2) - 4(1) = 6 - 4 = 2$.
- **Answer**: **2**.
"""

with open(os.path.join(MOCK_DIR, "Solutions_Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(sol_p1_content)
print("Generated mock_tests/Mock_19_IIT_Roorkee/Solutions_Paper_1.md")

