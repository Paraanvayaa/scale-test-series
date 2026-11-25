import os

MOCK_DIR = os.path.join("mock_tests", "Mock_08_IIT_Guwahati")
os.makedirs(MOCK_DIR, exist_ok=True)

# ----------------------------------------------------
# PAPER 1
# ----------------------------------------------------
p1_content = """# JEE (Advanced) Mock Examination 08
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

**Q1.** A solid insulating sphere of radius $R$ carries a uniform volume charge density $\\rho$. A spherical cavity of radius $R/2$ is scooped out such that the center of the cavity is at distance $R/2$ from the center of the sphere. The electric field inside the cavity is:
(A) Non-uniform and radially outward from the cavity center  
(B) Uniform in magnitude and parallel to the line connecting the centers  
(C) Zero everywhere inside the cavity  
(D) Non-uniform and proportional to $1/r^2$ from the sphere center  

**Q2.** Two identical moles of an ideal diatomic gas undergo a reversible cyclic process $A \\rightarrow B \\rightarrow C \\rightarrow A$. Process $A \\rightarrow B$ is isothermal expansion at $T_1 = 400\\text{ K}$ from volume $V_0$ to $2V_0$. Process $B \\rightarrow C$ is isochoric cooling to temperature $T_2 = 300\\text{ K}$. Process $C \\rightarrow A$ returns the gas to state $A$ along a straight line in the PV diagram. The net work done by the gas per cycle is:
(A) $2R [400\\ln 2 - 50]$  
(B) $R [400\\ln 2 - 25]$  
(C) $2R [400\\ln 2 - 100]$  
(D) $800 R \\ln 2$  

**Q3.** A particle of mass $m$ is suspended from a ceiling by a light inextensible string of length $L$. It is given a horizontal velocity $u$ at its lowest point. The minimum value of $u$ such that the string remains taut throughout the complete vertical circular motion is:
(A) $\\sqrt{3gL}$  
(B) $\\sqrt{4gL}$  
(C) $\\sqrt{5gL}$  
(D) $\\sqrt{6gL}$  

**Q4.** A beam of unpolarized light passes through three successive linear polarizers $P_1, P_2, P_3$. The transmission axes of $P_1$ and $P_3$ are crossed (perpendicular to each other). The transmission axis of $P_2$ is oriented at $45^\\circ$ relative to $P_1$. If the incident intensity is $I_0$, the transmitted intensity emerging from $P_3$ is:
(A) $I_0 / 4$  
(B) $I_0 / 8$  
(C) $I_0 / 16$  
(D) $0$  

**Q5.** In the Compton scattering of an X-ray photon of wavelength $\\lambda = 0.050\\text{ nm}$ by a stationary electron, the maximum kinetic energy transferred to the recoiling electron occurs when the scattering angle of the photon is:
(A) $0^\\circ$  
(B) $45^\\circ$  
(C) $90^\\circ$  
(D) $180^\\circ$  

**Q6.** A cylindrical vessel of base area $A$ contains water up to height $H$. A small hole of area $a$ ($a \\ll A$) is opened at the bottom. The horizontal distance from the base of the cylinder to the point where the emerging water jet hits the ground is maximum when the hole is drilled at depth $h$ below the free surface equal to:
(A) $H/4$  
(B) $H/3$  
(C) $H/2$  
(D) $H$  

---

### SECTION 2: One or More Than One Correct Option (Qs 7–12)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q7.** A uniform disc of mass $M$ and radius $R$ rolls without slipping on a horizontal track with constant velocity $v_0 \\hat{i}$:
(A) The instantaneous axis of rotation passes through the contact point with the track.  
(B) The kinetic energy of the disc is $\\frac{3}{4} M v_0^2$.  
(C) The acceleration of the lowest point of the disc is $v_0^2 / R$ directed vertically upwards towards the center.  
(D) The angular momentum of the disc about the contact point is $\\frac{3}{2} M R v_0$.  

**Q8.** A monoatomic ideal gas is taken through an isobaric process $1 \\rightarrow 2$ in which heat $Q$ is supplied to the gas:
(A) The increase in internal energy of the gas is $\\Delta U = \\frac{3}{5} Q$.  
(B) The work done by the gas is $W = \\frac{2}{5} Q$.  
(C) The ratio of work done to heat absorbed is $W/Q = 2/5$.  
(D) The molar heat capacity for this process is $C_p = \\frac{5}{2}R$.  

**Q9.** Two identical coherent point sources $S_1$ and $S_2$ emitting light of wavelength $\\lambda$ are separated by distance $d = 3\\lambda$ along the x-axis. A large circular detector of radius $R$ ($R \\gg d$) is placed in the xy-plane concentric with the midpoint of the sources:
(A) The total number of intensity maxima detected along the entire circumference of the circle is 12.  
(B) Along the perpendicular bisector (y-axis), constructive interference occurs at the intersection points with the circle.  
(C) The path difference between the two waves at an angle $\\theta$ with the x-axis is $d \\cos\\theta$.  
(D) Minima occur at angles where $\\cos\\theta = \\pm 1/6, \\pm 1/2, \\pm 5/6$.  

**Q10.** An electron in a hydrogen atom makes a transition from an excited state with principal quantum number $n$ to the ground state ($n = 1$). Let $r_n, v_n, L_n, E_n$ denote orbital radius, speed, angular momentum, and total energy in the $n$-th Bohr orbit:
(A) $r_n \\propto n^2$.  
(B) $v_n \\propto 1/n$.  
(C) $L_n = n \\hbar$.  
(D) $E_n \\propto -1/n^2$.  

**Q11.** A thin spherical shell of radius $R$ carries a uniform surface charge density $\\sigma$:
(A) The electrostatic potential at the center is $\\frac{\\sigma R}{\\varepsilon_0}$.  
(B) The electric field intensity at any point inside the shell is zero.  
(C) The electrostatic energy stored in the field of the charged shell is $\\frac{2\\pi \\sigma^2 R^3}{\\varepsilon_0}$.  
(D) The outward electrostatic pressure acting on the surface of the shell is $\\frac{\\sigma^2}{2\\varepsilon_0}$.  

**Q12.** A circular coil of $N$ turns, radius $r$, and resistance $R$ is rotated with constant angular velocity $\\omega$ about a diameter perpendicular to a uniform magnetic field $B$:
(A) The maximum induced EMF in the coil is $N B \\pi r^2 \\omega$.  
(B) The average power dissipated as heat in the coil is $\\frac{(N B \\pi r^2 \\omega)^2}{2R}$.  
(C) The average torque required to maintain the steady rotation is $\\frac{(N B \\pi r^2)^2 \\omega}{2R}$.  
(D) The total magnetic flux linked with the coil varies sinusoidally with time.  

---

### SECTION 3: Numerical Value Questions (Qs 13–18)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q13.** A heat engine operates between temperatures $T_1 = 500\\text{ K}$ and $T_2 = 300\\text{ K}$. It takes in $1000\\text{ J}$ of heat from the high temperature reservoir and exhausts $700\\text{ J}$ to the cold reservoir. The efficiency of this actual engine divided by the maximum possible Carnot efficiency between these reservoirs is:  

**Q14.** In a photoelectric effect experiment, stopping potentials for light of wavelengths $300\\text{ nm}$ and $400\\text{ nm}$ are $V_1$ and $V_2$ respectively. The difference $(V_1 - V_2)$ in Volts is ($hc/e = 1240\\text{ V}\\cdot\\text{nm}$, round to two decimal places):  

**Q15.** A uniform solid sphere of radius $R = 20\\text{ cm}$ oscillates as a physical pendulum about a horizontal axis tangent to its surface. The period of small oscillations (in seconds) is ($g = 9.8\\text{ m/s}^2$, use $\\pi \\approx 3.14$, round to two decimal places):  

**Q16.** Two long parallel wires separated by distance $d = 10\\text{ cm}$ carry equal currents of $I = 5.0\\text{ A}$ in opposite directions. The magnitude of the magnetic field at the midpoint between the two wires (in $\\mu\\text{T}$) is:  

**Q17.** A mass $m = 0.5\\text{ kg}$ is attached to a vertical spring of force constant $k = 200\\text{ N/m}$. The mass is released from rest when the spring is in its unstretched condition. The maximum downward displacement of the mass (in cm) is ($g = 10\\text{ m/s}^2$):  

**Q18.** A convex lens of focal length $f = 15\\text{ cm}$ forms a real image on a screen that is 4 times the size of the object. The distance of the screen from the lens (in cm) is:  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: Single Correct Option (Qs 19–24)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q19.** An ionic compound $AB$ crystallizes in the zinc blende (sphalerite) crystal structure. The sulfide ions ($B^{2-}$) form a face-centered cubic lattice, and the zinc cations ($A^{2+}$) occupy:
(A) All octahedral voids  
(B) All tetrahedral voids  
(C) Alternate tetrahedral voids (50% of tetrahedral voids)  
(D) Half of the octahedral voids  

**Q20.** For the reaction $\\text{PCl}_5(g) \\rightleftharpoons \\text{PCl}_3(g) + \\text{Cl}_2(g)$, the degree of dissociation $\\alpha$ is small compared to 1. The relationship between $\\alpha$, equilibrium constant $K_p$, and total pressure $P$ is:
(A) $\\alpha \\propto P$  
(B) $\\alpha \\propto 1/P$  
(C) $\\alpha \\propto 1/\\sqrt{P}$  
(D) $\\alpha \\propto \\sqrt{P}$  

**Q21.** Which of the following high-spin octahedral complexes is expected to exhibit dynamic Jahn-Teller distortion?
(A) $[\\text{Cr}(\\text{H}_2\\text{O})_6]^{3+}$ ($d^3$)  
(B) $[\\text{Mn}(\\text{H}_2\\text{O})_6]^{2+}$ ($d^5$)  
(C) $[\\text{Cu}(\\text{H}_2\\text{O})_6]^{2+}$ ($d^9$)  
(D) $[\\text{Ni}(\\text{H}_2\\text{O})_6]^{2+}$ ($d^8$)  

**Q22.** The major product formed when phenol is treated with chloroform and aqueous $\\text{NaOH}$ at $340\\text{ K}$ followed by acidification (Reimer-Tiemann reaction) is:
(A) Benzoic acid  
(B) Salicylaldehyde (2-hydroxybenzaldehyde)  
(C) Salicylic acid  
(D) 4-chlorophenol  

**Q23.** At $298\\text{ K}$, the molar conductivities at infinite dilution ($\\Lambda_m^\\circ$) for $\\text{HCl}, \\text{NaCl}$, and $\\text{CH}_3\\text{COONa}$ are $426.1, 126.5$, and $91.0\\text{ S}\\cdot\\text{cm}^2/\\text{mol}$ respectively. According to Kohlrausch's law, $\\Lambda_m^\\circ$ for acetic acid ($\\text{CH}_3\\text{COOH}$) is:
(A) $390.6\\text{ S}\\cdot\\text{cm}^2/\\text{mol}$  
(B) $517.1\\text{ S}\\cdot\\text{cm}^2/\\text{mol}$  
(C) $208.6\\text{ S}\\cdot\\text{cm}^2/\\text{mol}$  
(D) $300.0\\text{ S}\\cdot\\text{cm}^2/\\text{mol}$  

**Q24.** Which of the following xenon fluorides acts as a fluoride ion acceptor when reacted with alkali metal fluorides like $\\text{CsF}$?
(A) $\\text{XeF}_2$  
(B) $\\text{XeF}_4$  
(C) $\\text{XeF}_6$  
(D) None of these  

---

### SECTION 2: One or More Than One Correct Option (Qs 25–30)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q25.** For the spontaneous expansion of an ideal gas into vacuum (free expansion) in an insulated container:
(A) $W = 0$.  
(B) $q = 0$.  
(C) $\\Delta U = 0$ and $\\Delta T = 0$.  
(D) $\\Delta S_{\\text{sys}} > 0$ and $\\Delta S_{\\text{univ}} > 0$.  

**Q26.** Which of the following statements is/are correct regarding the Cannizzaro reaction?
(A) It is undergone by aldehydes lacking $\\alpha$-hydrogen atoms upon treatment with concentrated alkali.  
(B) It is a disproportionation (redox) reaction where one molecule is reduced to an alcohol and another is oxidized to a carboxylate salt.  
(C) Cross-Cannizzaro reaction between benzaldehyde and formaldehyde yields benzyl alcohol and sodium formate.  
(D) The hydride transfer from the dianion intermediate to the carbonyl group is the rate-determining step.  

**Q27.** Consider the complex $[\\text{Fe}(\\text{CN})_6]^{3-}$:
(A) The iron center has $+3$ oxidation state ($d^5$).  
(B) $\\text{CN}^-$ is a strong field ligand, producing a low-spin $t_{2g}^5 e_g^0$ configuration.  
(C) It has one unpaired electron and is paramagnetic with spin-only magnetic moment $\\approx 1.73\\text{ BM}$.  
(D) It undergoes $d^2sp^3$ inner orbital hybridization with octahedral geometry.  

**Q28.** Which of the following statements is/are correct regarding the extraction of iron in a blast furnace?
(A) Limestone ($\\text{CaCO}_3$) acts as a basic flux to remove acidic silica impurity ($\text{SiO}_2$) as calcium silicate slag ($\text{CaSiO}_3$).  
(B) In the lower reduction zone, the main reducing agent is carbon monoxide ($\text{CO}$).  
(C) The iron obtained directly from the blast furnace contains about $4\\%$ carbon and is known as pig iron.  
(D) Hematite ($\\text{Fe}_2\\text{O}_3$) is reduced through the sequence $\\text{Fe}_2\\text{O}_3 \\rightarrow \\text{Fe}_3\\text{O}_4 \\rightarrow \\text{FeO} \\rightarrow \\text{Fe}$.  

**Q29.** In an aqueous solution of a weak acid $HA$ of concentration $C$ and ionization constant $K_a$:
(A) The degree of dissociation is $\\alpha = \\sqrt{K_a / C}$ when $\\alpha \\ll 1$.  
(B) Dilution increases the degree of dissociation $\\alpha$ (Ostwald's dilution law).  
(C) Addition of a strong acid suppressing the dissociation of $HA$ is an example of the common ion effect.  
(D) $[\\text{H}^+] = \\sqrt{K_a C}$ when $\\alpha \\ll 1$.  

**Q30.** Which of the following reagents can be used to convert toluene into benzaldehyde?
(A) $\\text{CrO}_2\\text{Cl}_2$ in $\\text{CS}_2$ followed by $\\text{H}_3\\text{O}^+$ (Etard reaction)  
(B) $\\text{CrO}_3$ in acetic anhydride followed by hydrolysis  
(C) $\\text{Cl}_2 / h\\nu$ to give benzal chloride followed by hydrolysis at $373\\text{ K}$  
(D) Acidified $\\text{KMnO}_4$ with vigorous heating  

---

### SECTION 3: Numerical Value Questions (Qs 31–36)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q31.** The density of a face-centered cubic crystal is $10.0\\text{ g/cm}^3$ and its edge length is $200\\text{ pm}$. The molar mass of the element (in g/mol) is ($N_A = 6.02\\times 10^{23}\\text{ mol}^{-1}$, round to one decimal place):  

**Q32.** At $300\\text{ K}$, the equilibrium constant for the reaction $A(g) \\rightleftharpoons B(g) + C(g)$ is $K_p = 0.16\\text{ bar}$. If pure $A$ is introduced at an initial pressure of $1.0\\text{ bar}$, the total equilibrium pressure (in bar) is (round to two decimal places):  

**Q33.** A first-order reaction has activation energy $E_a = 50\\text{ kJ/mol}$. If the rate constant at $300\\text{ K}$ is $1.0\\times 10^{-3}\\text{ s}^{-1}$, the rate constant at $310\\text{ K}$ expressed as $k_2 / k_1$ is (use $R = 8.314\\text{ J/mol}\\cdot\\text{K}$, round to two decimal places):  

**Q34.** The depression in freezing point for a $1.0\\text{ m}$ aqueous solution of $\\text{CaCl}_2$ (assuming complete dissociation into 3 ions) is (given $K_f = 1.86\\text{ K}\\cdot\\text{kg/mol}$, in K, round to two decimal places):  

**Q35.** The number of geometrical isomers possible for the square planar complex $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$ is:  

**Q36.** The total number of optical stereoisomers (enantiomers + diastereomers) for 2,3-dichlorobutane is:  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 37–42)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q37.** The value of the definite integral
$$I = \\int_{0}^{\\pi/2} \\frac{\\sqrt{\\sin x}}{\\sqrt{\\sin x} + \\sqrt{\\cos x}}\\,dx$$
is:
(A) $\\frac{\\pi}{4}$  
(B) $\\frac{\\pi}{2}$  
(C) $\\pi$  
(D) $0$  

**Q38.** The equation of the tangent to the parabola $y^2 = 8x$ which is parallel to the line $2x - y + 5 = 0$ is:
(A) $2x - y + 1 = 0$  
(B) $2x - y + 2 = 0$  
(C) $x - 2y + 1 = 0$  
(D) $2x + y + 1 = 0$  

**Q39.** If $\\vec{a}$ and $\\vec{b}$ are two unit vectors inclined at an angle $\\theta$, then $\\sin(\\theta/2)$ is equal to:
(A) $\\frac{1}{2}|\\vec{a} - \\vec{b}|$  
(B) $\\frac{1}{2}|\\vec{a} + \\vec{b}|$  
(C) $|\\vec{a} \\times \\vec{b}|$  
(D) $\\frac{1}{2}(\\vec{a} \\cdot \\vec{b})$  

**Q40.** An unbiased coin is tossed 10 times. The probability of getting at least 2 heads is:
(A) $\\frac{1013}{1024}$  
(B) $\\frac{1014}{1024}$  
(C) $\\frac{11}{1024}$  
(D) $\\frac{1}{1024}$  

**Q41.** The area bounded by the curves $y = x^2$ and $y = x$ is:
(A) $\\frac{1}{2}$  
(B) $\\frac{1}{3}$  
(C) $\\frac{1}{6}$  
(D) $\\frac{1}{12}$  

**Q42.** The integrating factor of the differential equation $(x + 2y^3)\\frac{dy}{dx} = y$ is:
(A) $1/y$  
(B) $e^{-y}$  
(C) $y$  
(D) $1/y^2$  

---

### SECTION 2: One or More Than One Correct Option (Qs 43–48)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q43.** Let $f(x) = x^4 - 4x^3 + 4x^2 + 1$ for all $x \\in \\mathbb{R}$:
(A) $f(x)$ has local minima at $x = 0$ and $x = 2$.  
(B) $f(x)$ has a local maximum at $x = 1$.  
(C) The minimum value of $f(x)$ on $\\mathbb{R}$ is $1$.  
(D) $f(x) \\ge 1$ for all $x \\in \\mathbb{R}$.  

**Q44.** For the ellipse $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ ($a > b$):
(A) The length of the latus rectum is $\\frac{2b^2}{a}$.  
(B) The sum of focal distances of any point on the ellipse is $2a$.  
(C) The tangents at the ends of any focal chord intersect on the directrix.  
(D) The foot of perpendicular from either focus on any tangent lies on the auxiliary circle $x^2 + y^2 = a^2$.  

**Q45.** Let $A$ be a non-singular $3 \\times 3$ matrix. Which of the following statements is/are always true?
(A) $\\det(\\text{adj } A) = (\\det A)^2$.  
(B) $\\text{adj}(\\text{adj } A) = (\\det A) A$.  
(C) $\\det(A^{-1}) = \\frac{1}{\\det A}$.  
(D) $(A^T)^{-1} = (A^{-1})^T$.  

**Q46.** Let $z$ be a complex number satisfying $|z| = 1$. Which of the following is/are correct?
(A) $\\frac{1 + z}{1 + \\bar{z}} = z$.  
(B) $\\text{Re}\\left(\\frac{z - 1}{z + 1}\\right) = 0$ for $z \\ne -1$.  
(C) $|z - 2|$ attains its minimum value of $1$ at $z = 1$.  
(D) $|z^n| = 1$ for all $n \\in \\mathbb{N}$.  

**Q47.** Consider the function $f(x) = \\frac{\\sin x}{x}$ for $x > 0$:
(A) $f(x)$ is strictly decreasing on $(0, \\pi/2)$.  
(B) $\\lim_{x \\to 0} \\frac{\\sin x}{x} = 1$.  
(C) $\\frac{2}{\\pi} x < \\sin x < x$ for all $x \\in (0, \\pi/2)$ (Jordan's inequality).  
(D) $\\int_{0}^{\\infty} \\frac{\\sin x}{x}\\,dx = \\frac{\\pi}{2}$ (Dirichlet integral).  

**Q48.** For any three vectors $\\vec{a}, \\vec{b}, \\vec{c}$ in $\\mathbb{R}^3$:
(A) $\\vec{a} \\times (\\vec{b} \\times \\vec{c}) = (\\vec{a} \\cdot \\vec{c})\\vec{b} - (\\vec{a} \\cdot \\vec{b})\\vec{c}$.  
(B) $(\\vec{a} \\times \\vec{b}) \\cdot \\vec{c} = \\vec{a} \\cdot (\\vec{b} \\times \\vec{c})$.  
(C) If $\\vec{a} \\times \\vec{b} = \\vec{a} \\times \\vec{c}$ and $\\vec{a} \\ne \\vec{0}$, then $\\vec{b} = \\vec{c} + \\lambda \\vec{a}$ for some scalar $\\lambda$.  
(D) $[\\vec{a} \\; \\vec{b} \\; \\vec{c}] = 0$ if and only if the three vectors are coplanar.  

---

### SECTION 3: Numerical Value Questions (Qs 49–54)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q49.** The value of the limit
$$L = \\lim_{x \\to 0} \\frac{x - \\sin x}{x^3}$$
expressed as $1/N$, has integer $N$ equal to:  

**Q50.** The number of solutions of $\\cos^2 x + \\cos x - 2 = 0$ in the interval $[0, 4\\pi]$ is:  

**Q51.** The slope of the tangent to the curve $y = x^3 - 3x + 2$ at the point where it crosses the y-axis is:  

**Q52.** The maximum value of $f(x) = 2x^3 - 9x^2 + 12x + 5$ on the closed interval $[0, 3]$ is:  

**Q53.** The perpendicular distance of the point $(1, 2, 3)$ from the plane $2x - 2y + z + 5 = 0$ is:  

**Q54.** The value of the determinant $\\begin{vmatrix} 2 & 3 & 4 \\\\ 3 & 4 & 5 \\\\ 4 & 5 & 6 \\end{vmatrix}$ is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(p1_content)
print("Generated mock_tests/Mock_08_IIT_Guwahati/Paper_1.md")

