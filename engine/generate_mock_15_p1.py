import os

MOCK_DIR = os.path.join("mock_tests", "Mock_15_IIT_Madras")
os.makedirs(MOCK_DIR, exist_ok=True)

# ----------------------------------------------------
# PAPER 1
# ----------------------------------------------------
p1_content = """# JEE (Advanced) Mock Examination 15
### Organising Institute Style: IIT Madras (`IIT_MADRAS_STYLE` — 2017 Benchmark)
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

**Q1.** A non-conducting ring of radius $R$ carries a non-uniform linear charge density $\\lambda(\\theta) = \\lambda_0 \\cos\\theta$. The electric potential at the center of the ring and the net electric dipole moment of the ring are, respectively:
(A) $V = 0$, $p = \\pi R^2 \\lambda_0$  
(B) $V = \\frac{\\lambda_0}{2\\varepsilon_0}$, $p = \\pi R^2 \\lambda_0$  
(C) $V = 0$, $p = 2\\pi R^2 \\lambda_0$  
(D) $V = \\frac{\\lambda_0}{4\\pi\\varepsilon_0}$, $p = \\frac{1}{2}\\pi R^2 \\lambda_0$  

**Q2.** A circular loop of wire of radius $a$ carries a steady current $I$. A long straight wire carrying the same current $I$ lies in the plane of the loop at a distance $d$ ($d > a$) from its center. If the magnetic field at the center of the loop is zero, the direction of current in the straight wire relative to the loop is:
(A) Directed such that its field cancels that of the loop, requiring $d = a/\\pi$  
(B) Directed such that its field cancels that of the loop, requiring $d = a \\pi$  
(C) Directed such that its field cancels that of the loop, requiring $d = 2a/\\pi$  
(D) Directed such that its field cancels that of the loop, requiring $d = a/(2\\pi)$  

**Q3.** In an $RL$ series circuit connected to an ideal battery of EMF $\\mathcal{E}$ at $t = 0$, the rate of energy storage in the magnetic field of the inductor reaches its maximum value at time $t$ equal to:
(A) $\\frac{L}{R} \\ln 2$  
(B) $\\frac{2L}{R} \\ln 2$  
(C) $\\frac{L}{2R} \\ln 2$  
(D) $\\frac{L}{R}$  

**Q4.** A point charge $q$ is placed at a distance $d$ from the center of an uncharged grounded conducting sphere of radius $R$ ($d > R$). The total charge induced on the conducting sphere is:
(A) $-q \\frac{R}{d}$  
(B) $-q$  
(C) $-q \\frac{d}{R}$  
(D) $0$  

**Q5.** A thin biconvex lens of focal length $f = 20\\text{ cm}$ in air has refractive index $\\mu_g = 1.50$. When immersed completely in a transparent liquid of refractive index $\\mu_l = 1.25$, its new focal length is:
(A) $50\\text{ cm}$  
(B) $40\\text{ cm}$  
(C) $60\\text{ cm}$  
(D) $25\\text{ cm}$  

**Q6.** A particle of mass $m$ and charge $+q$ enters a region of crossed electric and magnetic fields $\\vec{E} = E_0 \\hat{j}$ and $\\vec{B} = B_0 \\hat{k}$ with initial velocity $\\vec{v} = v_0 \\hat{i}$. If the particle passes through undeflected, its speed must be:
(A) $v_0 = E_0 / B_0$  
(B) $v_0 = B_0 / E_0$  
(C) $v_0 = \\sqrt{E_0 / B_0}$  
(D) $v_0 = E_0 B_0$  

---

### SECTION 2: One or More Than One Correct Option (Qs 7–12)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q7.** A square conducting loop of side $L$ and resistance $R$ falls vertically under gravity in a region where a horizontal magnetic field $\\vec{B} = B_0 \\hat{k}$ exists for $y < 0$ (the upper half $y > 0$ has zero field):
(A) While entering the magnetic field, a counter-clockwise induced current flows in the loop.  
(B) The magnetic braking force on the loop during entry is directed vertically upward and has magnitude $\\frac{B_0^2 L^2 v}{R}$.  
(C) The terminal velocity achieved by the loop if it is still partially in the field is $v_t = \\frac{m g R}{B_0^2 L^2}$.  
(D) The rate of Joule heat dissipation at terminal speed equals the rate of loss of gravitational potential energy $m g v_t$.  

**Q8.** A spherical capacitor consists of two concentric conducting spherical shells of radii $a$ and $b$ ($b > a$). The inner shell carries charge $+Q$ and the outer shell carries charge $-Q$:
(A) The capacitance of the system is $C = 4\\pi\\varepsilon_0 \\frac{a b}{b - a}$.  
(B) The electrostatic energy stored in the electric field between the shells is $U = \\frac{Q^2(b - a)}{8\\pi\\varepsilon_0 a b}$.  
(C) If the outer shell is expanded to infinity ($b \\to \\infty$), the capacitance becomes $4\\pi\\varepsilon_0 a$.  
(D) The electric field in the region $r < a$ and $r > b$ is identically zero.  

**Q9.** An alternating voltage $v(t) = V_0 \\sin(\\omega t)$ is applied across a series combination of a resistor $R$, an inductor $L$, and a capacitor $C$:
(A) At resonance ($\\omega_0 = 1/\\sqrt{LC}$), the impedance of the circuit is purely resistive and has its minimum value $Z = R$.  
(B) The voltage across the inductor leads the current by $\\pi/2$ radians.  
(C) The voltage across the capacitor lags the current by $\\pi/2$ radians.  
(D) At resonance, the voltages across the inductor and capacitor cancel each other at every instant.  

**Q10.** In an electromagnetic wave propagating along the $+x$-direction in free space:
(A) The electric field $\\vec{E}$ and magnetic field $\\vec{B}$ oscillate in phase.  
(B) The ratio of the amplitudes is $E_0 / B_0 = c$, where $c = 1/\\sqrt{\\mu_0 \\varepsilon_0}$.  
(C) The instantaneous Poynting vector is $\\vec{S} = \\frac{1}{\\mu_0}(\\vec{E} \\times \\vec{B})$ and points in the $+x$-direction.  
(D) The average energy densities in the electric and magnetic fields are equal: $\\langle u_E \\rangle = \\langle u_B \\rangle = \\frac{1}{4}\\varepsilon_0 E_0^2$.  

**Q11.** A particle of mass $m$ moves in a circular orbit of radius $r_0$ under the action of a central attractive force $F(r) = -\\frac{k}{r^3}$:
(A) The orbital angular momentum $L$ is conserved.  
(B) The kinetic energy of the particle in the circular orbit is $\\frac{k}{2 r_0^2}$.  
(C) The total mechanical energy in the circular orbit is identically zero.  
(D) A small radial perturbation results in unbounded motion (unstable circular orbit).  

**Q12.** In a photoelectric experiment using a clean metal surface:
(A) The maximum kinetic energy of photoelectrons depends linearly on the frequency of incident radiation.  
(B) The photoelectric current is directly proportional to the intensity of incident radiation above the threshold frequency.  
(C) The stopping potential is independent of the intensity of incident radiation.  
(D) There is no detectable time lag between the incidence of radiation and the emission of photoelectrons.  

---

### SECTION 3: Numerical Value Questions (Qs 13–18)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q13.** A parallel plate capacitor of capacitance $C_0 = 10.0\\,\\mu\\text{F}$ is charged to potential $V_0 = 100\\text{ V}$ and then disconnected from the battery. A dielectric slab of dielectric constant $K = 5.0$ completely filling the space between the plates is then inserted. The work done by the external agent in inserting the slab (in milliJoules, mJ) is: (Take work done as positive if work is done on the system, or negative if the system does work; enter magnitude in mJ)  

**Q14.** A long solenoid of length $l = 1.0\\text{ m}$ and radius $r = 2.0\\text{ cm}$ has $N = 1000\\text{ turns}$ of wire carrying a current of $I = 2.0\\text{ A}$. The magnetic energy stored inside the solenoid (in milliJoules, mJ) is: (Take $\\pi = 3.14$, $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ T}\\cdot\\text{m/A}$, round to one decimal place)  

**Q15.** A uniform rod of length $L = 1.0\\text{ m}$ and mass $M = 3.0\\text{ kg}$ is free to rotate in a vertical plane about a smooth horizontal axis through its upper end. It is released from rest in the horizontal position. The angular velocity of the rod (in rad/s) when it reaches the vertical position is: ($g = 9.8\\text{ m/s}^2$, round to two decimal places)  

**Q16.** In a Young's double-slit experiment, the intensity at the central maximum is $I_0$. The intensity at a point on the screen where the path difference between the interfering waves is $\\lambda/6$ is $k I_0$. The value of $k$ is: (Round to two decimal places)  

**Q17.** A car sounding a horn of frequency $f = 400\\text{ Hz}$ travels at $20.0\\text{ m/s}$ towards a vertical wall. An observer standing stationary behind the car hears beats between the direct sound and the sound reflected from the wall. If the speed of sound is $340.0\\text{ m/s}$, the beat frequency heard (in Hz) is: (Round to one decimal place)  

**Q18.** A sample contains $1.0 \\times 10^{20}$ radioactive nuclei with a half-life of $10.0\\text{ days}$. The initial activity of the sample (in Curie, Ci) is: ($1\\text{ Ci} = 3.7 \\times 10^{10}\\text{ Bq}$, use $\\ln 2 = 0.693$, round to two decimal places)  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: Single Correct Option (Qs 19–24)
*Marking Scheme: +3 for correct, -1 for incorrect, 0 if unanswered.*

**Q19.** For the cell $\\text{Pt}|\\text{H}_2(g, 1\\text{ bar})|\\text{HCl}(aq, 0.01\\text{ M})||\\text{AgCl}(s)|\\text{Ag}(s)$ with $E^\\circ_{\\text{AgCl}/\\text{Ag}} = +0.222\\text{ V}$ at $298\\text{ K}$, the cell potential is: (Use $\\frac{2.303 RT}{F} = 0.0591\\text{ V}$)
(A) $0.340\\text{ V}$  
(B) $0.222\\text{ V}$  
(C) $0.104\\text{ V}$  
(D) $0.458\\text{ V}$  

**Q20.** According to crystal field theory, the crystal field stabilization energy (CFSE) for a high-spin octahedral $d^7$ complex (e.g., $[\\text{Co}(\\text{H}_2\\text{O})_6]^{2+}$) is:
(A) $-0.8 \\Delta_o$  
(B) $-1.2 \\Delta_o$  
(C) $-0.4 \\Delta_o$  
(D) $-1.8 \\Delta_o$  

**Q21.** Which of the following compounds reacts with alkaline iodine solution to give a yellow precipitate of iodoform?
(A) Butan-2-ol  
(B) Butan-1-ol  
(C) Pentan-3-one  
(D) 2-Methylpropan-2-ol  

**Q22.** The thermal stability of carbonates of alkaline earth metals increases down the group from $\\text{BeCO}_3$ to $\\text{BaCO}_3$. This trend is primarily due to:
(A) Decrease in polarizing power of the cation as its ionic radius increases  
(B) Increase in lattice energy of the carbonates down the group  
(C) Decrease in hydration enthalpy of the metal cation  
(D) Increase in electropositive character of the metal  

**Q23.** For the first-order decomposition of $\\text{N}_2\\text{O}_5(g) \\rightarrow 2\\text{NO}_2(g) + \\frac{1}{2}\\text{O}_2(g)$, the rate constant is $k = 6.93 \\times 10^{-3}\\text{ s}^{-1}$. The time required for the concentration of $\\text{N}_2\\text{O}_5$ to decrease from $0.40\\text{ M}$ to $0.05\\text{ M}$ is:
(A) $300\\text{ s}$  
(B) $200\\text{ s}$  
(C) $100\\text{ s}$  
(D) $400\\text{ s}$  

**Q24.** When excess potassium iodide solution is added to an acidified solution of potassium dichromate, the liberated iodine is titrated against standard sodium thiosulfate solution using starch as an indicator. The stoichiometric ratio of moles of $\\text{Cr}_2\\text{O}_7^{2-}$ to moles of $\\text{S}_2\\text{O}_3^{2-}$ reacted is:
(A) $1 : 6$  
(B) $1 : 3$  
(C) $1 : 2$  
(D) $1 : 1$  

---

### SECTION 2: One or More Than One Correct Option (Qs 25–30)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q25.** Regarding the Kohlrausch's law of independent migration of ions and electrolytic conductance:
(A) The molar conductivity at infinite dilution $\\Lambda_m^\\circ$ of a salt is the sum of the individual ionic contributions $\\lambda_+^\\circ$ and $\\lambda_-^\\circ$.  
(B) The degree of dissociation of a weak electrolyte at concentration $c$ is given by $\\alpha = \\Lambda_m / \\Lambda_m^\\circ$.  
(C) Specific conductance (conductivity $\\kappa$) decreases upon dilution because the number of current-carrying ions per unit volume decreases.  
(D) Molar conductance $\\Lambda_m$ increases upon dilution for both strong and weak electrolytes.  

**Q26.** For the coordination complexes $[\\text{Co}(\\text{en})_3]^{3+}$ and $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$:
(A) $[\\text{Co}(\\text{en})_3]^{3+}$ is an octahedral complex possessing a $D_3$ symmetry and is optically active.  
(B) $[\\text{Co}(\\text{en})_3]^{3+}$ exists as a pair of non-superimposable enantiomers ($\Delta$ and $\Lambda$).  
(C) $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$ is a square planar complex displaying cis and trans geometrical isomerism.  
(D) Neither the cis nor the trans isomer of $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$ exhibits optical isomerism due to internal planes of symmetry.  

**Q27.** For an organic compound undergoing the Cannizzaro reaction:
(A) The aldehyde must lack $\\alpha$-hydrogen atoms.  
(B) Benzaldehyde undergoes disproportionation in concentrated $\\text{NaOH}$ to give benzyl alcohol and sodium benzoate.  
(C) The hydride transfer from the dianion/monoanion tetrahedral intermediate to the second aldehyde molecule is the rate-determining step.  
(D) In a crossed Cannizzaro reaction between benzaldehyde and formaldehyde, formaldehyde is preferentially oxidized to sodium formate.  

**Q28.** Regarding the metallurgy of iron and the reactions in the blast furnace:
(A) In the reduction zone ($500–800\\text{ K}$), $\\text{Fe}_2\\text{O}_3$ is reduced to $\\text{Fe}_3\\text{O}_4$ and then to $\\text{FeO}$ by carbon monoxide.  
(B) Limestone ($\\text{CaCO}_3$) acts as a flux, decomposing to $\\text{CaO}$, which removes silica gangue as molten calcium silicate slag ($\\text{CaSiO}_3$).  
(C) The molten iron collected at the bottom of the blast furnace is pig iron, containing about $4\\%$ carbon and other impurities.  
(D) Cast iron is extremely hard and brittle due to its high carbon content.  

**Q29.** In the thermodynamics of phase equilibria and chemical reactions:
(A) At the boiling point of a liquid at $1\\text{ atm}$, the change in Gibbs free energy $\\Delta G$ is identically zero.  
(B) According to Trouton's rule, the standard entropy of vaporization $\\Delta S_{\\text{vap}}^\\circ$ for many non-associated liquids is approximately $88\\text{ J}/(\\text{mol}\\cdot\\text{K})$.  
(C) A reaction with $\\Delta H > 0$ and $\\Delta S > 0$ is non-spontaneous at low temperatures but becomes spontaneous above a threshold temperature $T = \\Delta H / \\Delta S$.  
(D) The equilibrium constant $K$ of an endothermic reaction increases as the temperature is raised.  

**Q30.** For the qualitative identification of inorganic anions:
(A) Sulfate ions ($\\text{SO}_4^{2-}$) form a white precipitate of $\\text{BaSO}_4$ with $\\text{BaCl}_2$ solution, insoluble in concentrated $\\text{HCl}$.  
(B) Nitrate ions ($\\text{NO}_3^-$) give a brown ring of $[\\text{Fe}(\\text{H}_2\\text{O})_5(\\text{NO})]^{2+}$ in the brown ring test with freshly prepared $\\text{FeSO}_4$ and concentrated $\\text{H}_2\\text{SO}_4$.  
(C) In the brown ring complex, the oxidation state of iron is $+1$ and $\\text{NO}$ acts as $\\text{NO}^+$.  
(D) Sulfide ions ($\\text{S}^{2-}$) produce a deep purple coloration with sodium nitroprusside solution due to the formation of $[\\text{Fe}(\\text{CN})_5(\\text{NOS})]^{4-}$.  

---

### SECTION 3: Numerical Value Questions (Qs 31–36)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q31.** The standard reduction potentials for $\\text{Fe}^{3+}/\\text{Fe}^{2+}$ and $\\text{Fe}^{2+}/\\text{Fe}$ couples are $+0.77\\text{ V}$ and $-0.44\\text{ V}$, respectively. The standard reduction potential for the $\\text{Fe}^{3+}/\\text{Fe}$ couple (in Volts) is: (Round to two decimal places)  

**Q32.** An aqueous solution contains $0.10\\text{ M } \\text{CH}_3\\text{COOH}$ and $0.10\\text{ M } \\text{CH}_3\\text{COONa}$. Given $K_a(\\text{CH}_3\\text{COOH}) = 1.8 \\times 10^{-5}$, the pH of the buffer solution is: (Use $\\log_{10} 1.8 = 0.255$, round to two decimal places)  

**Q33.** A metal crystallizes in a face-centered cubic (FCC) lattice with a unit cell edge length of $a = 400\\text{ pm}$. The density of the metal is $10.0\\text{ g/cm}^3$. The molar mass of the metal (in g/mol) is: ($N_A = 6.02 \\times 10^{23}\\text{ mol}^{-1}$, round to one decimal place)  

**Q34.** The decomposition of ozone follows the rate law $\\text{Rate} = k [\\text{O}_3]^2 [\\text{O}_2]^{-1}$. The overall order of this reaction is:  

**Q35.** A solution of a non-volatile non-electrolyte solute in water exhibits an osmotic pressure of $4.92\\text{ atm}$ at $300\\text{ K}$. Given $R = 0.0821\\text{ L}\\cdot\\text{atm}/(\\text{mol}\\cdot\\text{K})$, the molarity of the solution (in mol/L) is: (Round to two decimal places)  

**Q36.** The solubility of barium sulfate ($\\text{BaSO}_4$) in pure water is $1.0 \\times 10^{-5}\\text{ mol/L}$ at $298\\text{ K}$. The solubility of $\\text{BaSO}_4$ in a $0.010\\text{ M } \\text{BaCl}_2$ aqueous solution (in mol/L) is $k \\times 10^{-8}\\text{ mol/L}$. The value of $k$ is:  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 37–42)
*Marking Scheme: +3 for correct, -1 for incorrect, 0 if unanswered.*

**Q37.** Let $z$ be a complex number satisfying $|z - 2| + |z + 2| = 6$. The locus of $z$ in the complex plane is an ellipse with eccentricity:
(A) $\\frac{2}{3}$  
(B) $\\frac{1}{3}$  
(C) $\\frac{\\sqrt{5}}{3}$  
(D) $\\frac{1}{2}$  

**Q38.** The value of the definite integral
$$I = \\int_{0}^{\\pi/2} \\frac{\\cos x}{1 + \\sin x + \\cos x}\\,dx$$
is:
(A) $\\frac{\\pi}{4} - \\frac{1}{2}\\ln 2$  
(B) $\\frac{\\pi}{4} + \\frac{1}{2}\\ln 2$  
(C) $\\frac{\\pi}{2} - \\ln 2$  
(D) $\\frac{\\pi}{4}$  

**Q39.** The normal to the rectangular hyperbola $xy = c^2$ at the point $\\left(ct, \\frac{c}{t}\\right)$ intersects the curve again at point $\\left(ct', \\frac{c}{t'}\\right)$. The parameter $t'$ is given by:
(A) $t' = -\\frac{1}{t^3}$  
(B) $t' = -\\frac{1}{t}$  
(C) $t' = -t^3$  
(D) $t' = \\frac{1}{t^2}$  

**Q40.** The general solution of the differential equation
$$\\frac{dy}{dx} + y \\tan x = \\sec x$$
is:
(A) $y = \\sin x + C \\cos x$  
(B) $y = \\cos x + C \\sin x$  
(C) $y \\sec x = \\tan x + C$  
(D) $y = \\tan x + C \\cos x$  

**Q41.** The number of distinct arrangements of the letters of the word "PERMUTATION" in which all vowels occur together is:
(A) $5! \\times \\frac{7!}{2!}$  
(B) $\\frac{5! \\times 7!}{2!}$  
(C) $5! \\times 7!$  
(D) $\\frac{6! \\times 6!}{2!}$  

**Q42.** The angle between the two lines whose direction cosines satisfy the relations $l + m + n = 0$ and $l^2 + m^2 - n^2 = 0$ is:
(A) $\\frac{\\pi}{3}$  
(B) $\\frac{\\pi}{4}$  
(C) $\\frac{\\pi}{2}$  
(D) $\\frac{2\\pi}{3}$  

---

### SECTION 2: One or More Than One Correct Option (Qs 43–48)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q43.** Let $f(x) = x^3 - 6x^2 + 9x + 1$ defined on $\\mathbb{R}$:
(A) $f(x)$ has a local maximum at $x = 1$.  
(B) $f(x)$ has a local minimum at $x = 3$.  
(C) The point of inflection of $y = f(x)$ is $(2, 3)$.  
(D) The equation $f(x) = 0$ has exactly one real root.  

**Q44.** For the family of confocal conics $\\frac{x^2}{a^2 + \\lambda} + \\frac{y^2}{b^2 + \\lambda} = 1$ where $a > b > 0$:
(A) For $\\lambda > -b^2$, the curves are confocal ellipses.  
(B) For $-a^2 < \\lambda < -b^2$, the curves are confocal hyperbolas.  
(C) Every ellipse of the family intersects every hyperbola of the family orthogonally.  
(D) Through any point in the plane (not on the axes), there pass exactly one ellipse and one hyperbola of the family.  

**Q45.** Let $A$ be a $3 \\times 3$ invertible real symmetric matrix:
(A) All eigenvalues of $A$ are real numbers.  
(B) Eigenvectors corresponding to distinct eigenvalues of $A$ are mutually orthogonal.  
(C) There exists an orthogonal matrix $P$ such that $P^T A P$ is a diagonal matrix.  
(D) $\\det(A)$ is the product of its eigenvalues.  

**Q46.** Let $\\vec{a}, \\vec{b}, \\vec{c}$ be three non-coplanar vectors. The reciprocal system of vectors $\\vec{a}', \\vec{b}', \\vec{c}'$ is defined by $\\vec{a}' = \\frac{\\vec{b} \\times \\vec{c}}{[\\vec{a} \\; \\vec{b} \\; \\vec{c}]}$, $\\vec{b}' = \\frac{\\vec{c} \\times \\vec{a}}{[\\vec{a} \\; \\vec{b} \\; \\vec{c}]}$, and $\\vec{c}' = \\frac{\\vec{a} \\times \\vec{b}}{[\\vec{a} \\; \\vec{b} \\; \\vec{c}]}$:
(A) $\\vec{a} \\cdot \\vec{a}' = 1$, $\\vec{b} \\cdot \\vec{b}' = 1$, $\\vec{c} \\cdot \\vec{c}' = 1$.  
(B) $\\vec{a} \\cdot \\vec{b}' = 0$, $\\vec{a} \\cdot \\vec{c}' = 0$, $\\vec{b} \\cdot \\vec{a}' = 0$.  
(C) $[\\vec{a}' \\; \\vec{b}' \\; \\vec{c}'] = \\frac{1}{[\\vec{a} \\; \\vec{b} \\; \\vec{c}]}$.  
(D) $\\vec{a}' \\times \\vec{b}' + \\vec{b}' \\times \\vec{c}' + \\vec{c}' \\times \\vec{a}' = \\frac{\\vec{a} + \\vec{b} + \\vec{c}}{[\\vec{a} \\; \\vec{b} \\; \\vec{c}]}$.  

**Q47.** For any complex number $z = x + iy$:
(A) $|e^z| = e^x$.  
(B) $\\arg(e^z) = y + 2k\\pi$ ($k \\in \\mathbb{Z}$).  
(C) $e^z$ is a periodic function with fundamental period $2\\pi i$.  
(D) The equation $e^z = 1$ has solutions $z = 2k\\pi i$ ($k \\in \\mathbb{Z}$).  

**Q48.** Let $X$ be a binomial random variable with parameters $n$ and $p$ ($0 < p < 1$):
(A) The mean of $X$ is $E[X] = n p$.  
(B) The variance of $X$ is $\\text{Var}(X) = n p (1 - p)$.  
(C) The variance is strictly less than the mean: $\\text{Var}(X) < E[X]$.  
(D) The maximum possible variance for a fixed $n$ occurs at $p = 1/2$ and is $n/4$.  

---

### SECTION 3: Numerical Value Questions (Qs 49–54)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q49.** The value of the limit
$$L = \\lim_{x \\to 0} \\frac{x - \\sin x}{x^3}$$
is: (Round to three decimal places)  

**Q50.** The area of the region enclosed by the parabola $y^2 = 4x$ and the line $y = 2x$ is: (Round to two decimal places)  

**Q51.** The value of the definite integral
$$I = \\int_{0}^{1} \\frac{dx}{1 + x^2}$$
is $\\frac{\\pi}{k}$. The integer $k$ is:  

**Q52.** The radius of the circle passing through the vertices of a triangle with sides $3\\text{ cm}$, $4\\text{ cm}$, and $5\\text{ cm}$ (in cm) is:  

**Q53.** The number of solutions of the equation $2\\sin^2 x - 3\\sin x + 1 = 0$ in the interval $[0, 2\\pi]$ is:  

**Q54.** If $A = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}$, then $\\det(A^3)$ is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(p1_content)
print("Generated mock_tests/Mock_15_IIT_Madras/Paper_1.md")

# ----------------------------------------------------
# SOLUTIONS PAPER 1
# ----------------------------------------------------
sol_p1_content = """# Detailed Solutions and Pedagogical Analysis — Mock Examination 15 (Paper 1)
### Organising Institute Style: IIT Madras (`IIT_MADRAS_STYLE` — 2017 Benchmark)

---

## PART I: PHYSICS

### Q1. Charged Ring with Cosine Distribution
- **First Observation & Concept**: Linear charge density $\\lambda(\\theta) = \\lambda_0 \\cos\\theta$.
- **Derivation**:
  - Potential at center: $V = \\frac{1}{4\\pi\\varepsilon_0 R} \\int_0^{2\\pi} \\lambda(\\theta) R\\,d\\theta = \\frac{\\lambda_0}{4\\pi\\varepsilon_0} \\int_0^{2\\pi} \\cos\\theta\\,d\\theta = 0$.
  - Dipole moment: element $dq = \\lambda_0 \\cos\\theta R\\,d\\theta$ is at position $(R\\cos\\theta, R\\sin\\theta)$.
  - $p_x = \\int dq x = \\int_0^{2\\pi} (\\lambda_0 \\cos\\theta R\\,d\\theta)(R\\cos\\theta) = \\lambda_0 R^2 \\int_0^{2\\pi}\\cos^2\\theta\\,d\\theta = \\pi R^2 \\lambda_0$.
  - $p_y = \\int dq y = \\lambda_0 R^2 \\int_0^{2\\pi}\\cos\\theta\\sin\\theta\\,d\\theta = 0$.
  - Total dipole moment $p = \\pi R^2 \\lambda_0$.
- **Correct Option**: **(A)**.

### Q2. Magnetic Field Cancellation
- **First Observation & Concept**: Superposition of magnetic fields at the center of circular loop.
- **Derivation**:
  - $B_{\\text{loop}} = \\frac{\\mu_0 I}{2a}$ (perpendicular to plane).
  - Straight wire is in the plane of the loop. A wire in the same plane produces a magnetic field perpendicular to the plane at the center: $B_{\\text{wire}} = \\frac{\\mu_0 I}{2\\pi d}$.
  - For total cancellation: $\\frac{\\mu_0 I}{2a} = \\frac{\\mu_0 I}{2\\pi d} \\implies d = \\frac{a}{\\pi}$.
- **Correct Option**: **(A)**.

### Q3. Maximum Rate of Magnetic Energy Storage
- **First Observation & Concept**: Magnetic energy $U = \\frac{1}{2} L i^2$. Rate of energy storage $P_L = \\frac{dU}{dt} = L i \\frac{di}{dt}$.
- **Derivation**:
  - In $RL$ circuit: $i(t) = \\frac{\\mathcal{E}}{R}(1 - e^{-t/\\tau})$ where $\\tau = L/R$.
  - $\\frac{di}{dt} = \\frac{\\mathcal{E}}{L} e^{-t/\\tau}$.
  - $P_L(t) = L \\left[\\frac{\\mathcal{E}}{R}(1 - e^{-t/\\tau})\\right] \\left[\\frac{\\mathcal{E}}{L} e^{-t/\\tau}\\right] = \\frac{\\mathcal{E}^2}{R} (e^{-t/\\tau} - e^{-2t/\\tau})$.
  - Maximize $f(u) = u - u^2$ where $u = e^{-t/\\tau}$: maximum occurs when $u = 1/2$.
  - $e^{-t/\\tau} = 1/2 \\implies t = \\tau \\ln 2 = \\frac{L}{R} \\ln 2$.
- **Correct Option**: **(A)**.

### Q4. Induced Charge on Grounded Sphere
- **First Observation & Concept**: Method of image charges for grounded conducting sphere.
- **Derivation**:
  - Image charge $q' = -q \\frac{R}{d}$ placed at distance $d' = \\frac{R^2}{d}$ from center.
  - The total charge induced on the grounded sphere equals the magnitude of the image charge: $q_{\\text{ind}} = q' = -q \\frac{R}{d}$.
- **Correct Option**: **(A)**.

### Q5. Lens in Liquid Medium
- **First Observation & Concept**: Lens maker's formula $\\frac{1}{f} = \\left(\\frac{\\mu}{\\mu_m} - 1\\right)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$.
- **Derivation**:
  - In air: $\\frac{1}{20} = (1.50 - 1) K = 0.50 K \\implies K = \\frac{1}{10}$.
  - In liquid: $\\frac{1}{f'} = \\left(\\frac{1.50}{1.25} - 1\\right) K = (1.20 - 1) \\times \\frac{1}{10} = 0.20 \\times \\frac{1}{10} = \\frac{1}{50}$.
  - $f' = 50\\text{ cm}$.
- **Correct Option**: **(A)**.

### Q6. Velocity Selector
- **First Observation & Concept**: Lorentz force $\\vec{F} = q(\\vec{E} + \\vec{v} \\times \\vec{B}) = \\vec{0}$.
- **Derivation**:
  - $\\vec{v} \\times \\vec{B} = (v_0 \\hat{i}) \\times (B_0 \\hat{k}) = -v_0 B_0 \\hat{j}$.
  - Total force: $q (E_0 \\hat{j} - v_0 B_0 \\hat{j}) = \\vec{0} \\implies v_0 = E_0 / B_0$.
- **Correct Option**: **(A)**.

### Q7. Falling Loop in Magnetic Field
- **Analysis**:
  - Flux into page increases downwards, induced current creates field out of page $\\implies$ counter-clockwise. (A is True)
  - Upward magnetic force: $F = I L B_0 = \\left(\\frac{B_0 L v}{R}\\right) L B_0 = \\frac{B_0^2 L^2 v}{R}$. (B is True)
  - Terminal velocity: $m g = \\frac{B_0^2 L^2 v_t}{R} \\implies v_t = \\frac{m g R}{B_0^2 L^2}$. (C is True)
  - Energy conservation at terminal velocity: $P_{\\text{Joule}} = I^2 R = \\frac{B_0^2 L^2 v_t^2}{R} = (m g) v_t$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q8. Spherical Capacitor
- **Analysis**:
  - $V = \\frac{Q}{4\\pi\\varepsilon_0}\\left(\\frac{1}{a} - \\frac{1}{b}\\right) \\implies C = 4\\pi\\varepsilon_0 \\frac{ab}{b-a}$. (A is True)
  - $U = \\frac{Q^2}{2C} = \\frac{Q^2(b - a)}{8\\pi\\varepsilon_0 ab}$. (B is True)
  - When $b \\to \\infty$, $C \\to 4\\pi\\varepsilon_0 a$. (C is True)
  - Gauss's law shows $E = 0$ for $r < a$ and $r > b$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q9. LCR Series AC Resonance
- **Analysis**:
  - At resonance $X_L = X_C$, $Z = R$. (A is True)
  - Inductor voltage leads current by $\\pi/2$. (B is True)
  - Capacitor voltage lags current by $\\pi/2$. (C is True)
  - Since $v_L(t)$ and $v_C(t)$ are $\\pi$ out of phase and have equal amplitudes at resonance, $v_L(t) + v_C(t) = 0$ at all times. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q10. Electromagnetic Wave Properties
- **Analysis**:
  - In free space, $\\vec{E}$ and $\\vec{B}$ are in phase. (A is True)
  - $E_0 / B_0 = c = 1/\\sqrt{\\mu_0 \\varepsilon_0}$. (B is True)
  - $\\vec{S} = \\frac{1}{\\mu_0}(\\vec{E} \\times \\vec{B})$ along $+x$. (C is True)
  - Equipartition of energy: $\\langle u_E \\rangle = \\langle u_B \\rangle = \\frac{1}{4}\\varepsilon_0 E_0^2$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q11. Inverse-Cube Force
- **Analysis**:
  - Central force $\\implies$ angular momentum $L$ conserved. (A is True)
  - For circular orbit: $\\frac{m v^2}{r_0} = \\frac{k}{r_0^3} \\implies m v^2 = \\frac{k}{r_0^2} \\implies E_k = \\frac{1}{2} m v^2 = \\frac{k}{2 r_0^2}$. (B is True)
  - Potential energy: $V(r) = -\\int F\\,dr = -\\int (-\\frac{k}{r^3})\\,dr = -\\frac{k}{2r^2}$.
    Total energy $E = E_k + V = \\frac{k}{2r_0^2} - \\frac{k}{2r_0^2} = 0$. (C is True)
  - Effective potential $V_{\\text{eff}}(r) = \\frac{L^2}{2m r^2} - \\frac{k}{2r^2} = \\frac{L^2 - mk}{2m r^2}$, which has no local minimum, orbit is unstable. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q12. Photoelectric Fundamentals
- **Analysis**: All four statements are core experimental facts of the photoelectric effect.
- **Correct Options**: **(A, B, C, D)**.

### Q13. Work Done in Inserting Dielectric
- **Derivation**:
  - Initial energy: $U_i = \\frac{1}{2} C_0 V_0^2 = \\frac{1}{2} (10.0 \\times 10^{-6}) (100)^2 = 0.050\\text{ J} = 50.0\\text{ mJ}$.
  - Charge $Q = C_0 V_0 = 10.0 \\times 10^{-6} \\times 100 = 1.0 \\times 10^{-3}\\text{ C}$.
  - After dielectric insertion: $C = K C_0 = 50.0\\,\\mu\\text{F}$.
  - Final energy: $U_f = \\frac{Q^2}{2C} = \\frac{U_i}{K} = \\frac{50.0}{5} = 10.0\\text{ mJ}$.
  - Energy released / work done magnitude $= U_i - U_f = 40.0\\text{ mJ}$.
- **Answer**: **40.0** (or **40**).

### Q14. Stored Magnetic Energy in Solenoid
- **Derivation**:
  - Inductance $L = \\mu_0 n^2 A l = \\mu_0 \\left(\\frac{N}{l}\\right)^2 (\\pi r^2) l = \\mu_0 \\frac{N^2}{l} \\pi r^2$.
  - $L = (4\\pi \\times 10^{-7}) \\times \\frac{10^6}{1.0} \\times 3.14 \\times (0.02)^2 = 4\\pi \\times 10^{-1} \\times 3.14 \\times 4 \\times 10^{-4} = 1.256 \\times 1.256 \\times 10^{-3} = 1.579 \\times 10^{-3}\\text{ H} = 1.58\\text{ mH}$.
  - Energy $U = \\frac{1}{2} L I^2 = \\frac{1}{2} \\times 1.579 \\times 10^{-3} \\times (2.0)^2 = 2 \\times 1.579 \\approx 3.16 \\approx 3.2\\text{ mJ}$.
- **Answer**: **3.2**.

### Q15. Rotating Rod
- **Derivation**:
  - Loss in PE $= M g \\frac{L}{2}$.
  - Gain in rotational KE $= \\frac{1}{2} I \\omega^2 = \\frac{1}{2} \\left(\\frac{1}{3} M L^2\\right) \\omega^2 = \\frac{1}{6} M L^2 \\omega^2$.
  - $\\frac{1}{6} M L^2 \\omega^2 = M g \\frac{L}{2} \\implies \\omega = \\sqrt{\\frac{3g}{L}} = \\sqrt{\\frac{3 \\times 9.8}{1.0}} = \\sqrt{29.4} \\approx 5.42\\text{ rad/s}$.
- **Answer**: **5.42**.

### Q16. Intensity in YDSE
- **Derivation**:
  - Phase difference $\\phi = \\frac{2\\pi}{\\lambda} \\Delta x = \\frac{2\\pi}{\\lambda} \\frac{\\lambda}{6} = \\frac{\\pi}{3}$.
  - $I = I_0 \\cos^2(\\phi/2) = I_0 \\cos^2(\\pi/6) = I_0 \\left(\\frac{\\sqrt{3}}{2}\\right)^2 = \\frac{3}{4} I_0 = 0.75 I_0$.
  - $k = 0.75$.
- **Answer**: **0.75**.

### Q17. Doppler Beat Frequency
- **Derivation**:
  - Direct sound heard by observer behind receding car:
    $$f_1 = f \\frac{v}{v + u} = 400 \\times \\frac{340}{340 + 20} = 400 \\times \\frac{340}{360} = 377.78\\text{ Hz}$$
  - Reflected sound from stationary wall: wall receives $f_{\\text{wall}} = f \\frac{v}{v - u} = 400 \\times \\frac{340}{340 - 20} = 400 \\times \\frac{340}{320} = 425.0\\text{ Hz}$.
  - Reflected back to stationary observer: $f_2 = f_{\\text{wall}} = 425.0\\text{ Hz}$.
  - Beat frequency $\\Delta f = f_2 - f_1 = 425.0 - 377.78 = 47.22 \\approx 47.2\\text{ Hz}$.
- **Answer**: **47.2**.

### Q18. Radioactive Activity in Curies
- **Derivation**:
  - Decay constant $\\lambda = \\frac{\\ln 2}{T_{1/2}} = \\frac{0.693}{10.0 \\times 86400\\text{ s}} = \\frac{0.693}{8.64 \\times 10^5} = 8.021 \\times 10^{-7}\\text{ s}^{-1}$.
  - $A_0 = \\lambda N_0 = 8.021 \\times 10^{-7} \\times 1.0 \\times 10^{20} = 8.021 \\times 10^{13}\\text{ Bq}$.
  - In Curies: $A_0 = \\frac{8.021 \\times 10^{13}}{3.7 \\times 10^{10}} \\approx 2167.8$ Ci.
  - Wait, let's check: $N_0 = 10^{20} \\implies 2167.84$ Ci.
- **Answer**: **2167.84** (or **2168**).

---

## PART II: CHEMISTRY

### Q19. Cell Potential Calculation
- **Analysis**:
  - Cell reaction: $\\frac{1}{2}\\text{H}_2(g) + \\text{AgCl}(s) \\rightarrow \\text{H}^+(aq) + \\text{Cl}^-(aq) + \\text{Ag}(s)$.
  - $Q = [\\text{H}^+][\\text{Cl}^-] = (0.01)(0.01) = 10^{-4}$.
  - $E = E^\\circ - \\frac{0.0591}{1}\\log_{10}(10^{-4}) = 0.222 - 0.0591(-4) = 0.222 + 0.2364 = 0.458\\text{ V}$.
- **Correct Option**: **(D)** (Wait, in question options (A) 0.340, (B) 0.222, (C) 0.104, (D) 0.458 $\\implies$ D).

### Q20. CFSE of High-Spin d7 Octahedral
- **Analysis**:
  - Electron configuration: $t_{2g}^5 e_g^2$.
  - $\\text{CFSE} = 5(-0.4\\Delta_o) + 2(+0.6\\Delta_o) = -2.0\\Delta_o + 1.2\\Delta_o = -0.8\\Delta_o$.
- **Correct Option**: **(A)**.

### Q21. Iodoform Reaction
- **Analysis**:
  - Iodoform requires $\\text{CH}_3\\text{CH(OH)}-$ or $\\text{CH}_3\\text{C}(=\\text{O})-$.
  - Butan-2-ol has $\\text{CH}_3\\text{CH(OH)}-\\text{CH}_2\\text{CH}_3$, so it gives a positive iodoform test.
- **Correct Option**: **(A)**.

### Q22. Thermal Stability of Alkaline Earth Carbonates
- **Analysis**:
  - Smaller cations have high charge density and strongly polarize the large $\\text{CO}_3^{2-}$ anion, weakening the $\\text{C}-\\text{O}$ bond. Down the group, ionic radius increases, polarizing power decreases, stability increases.
- **Correct Option**: **(A)**.

### Q23. Time for First-Order Decomposition
- **Analysis**:
  - Fraction remaining: $\\frac{0.05}{0.40} = \\frac{1}{8} = \\left(\\frac{1}{2}\\right)^3 \\implies 3$ half-lives.
  - $t_{1/2} = \\frac{0.693}{k} = \\frac{0.693}{6.93 \\times 10^{-3}} = 100\\text{ s}$.
  - Total time $= 3 \\times 100 = 300\\text{ s}$.
- **Correct Option**: **(A)**.

### Q24. Stoichiometry of Iodometric Titration
- **Analysis**:
  - $\\text{Cr}_2\\text{O}_7^{2-} + 14\\text{H}^+ + 6\\text{I}^- \\rightarrow 2\\text{Cr}^{3+} + 3\\text{I}_2 + 7\\text{H}_2\\text{O}$.
  - $3\\text{I}_2 + 6\\text{S}_2\\text{O}_3^{2-} \\rightarrow 6\\text{I}^- + 3\\text{S}_4\\text{O}_6^{2-}$.
  - 1 mole of $\\text{Cr}_2\\text{O}_7^{2-}$ produces 3 moles of $\\text{I}_2$, which reacts with 6 moles of $\\text{S}_2\\text{O}_3^{2-}$.
  - Ratio is $1 : 6$.
- **Correct Option**: **(A)**.

### Q25. Kohlrausch Law and Conductance
- **Analysis**: All four statements correctly state electrochemical principles of ionic conductivity.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Stereoisomerism in Complexes
- **Analysis**: All four statements accurately describe chiral octahedral vs square planar isomers.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Cannizzaro Reaction
- **Analysis**: Mechanism, hydride transfer as RDS, and crossed Cannizzaro selectivity are all correctly presented.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Metallurgy of Iron
- **Analysis**: Blast furnace chemistry, zones, flux/slag reactions, pig iron and cast iron characteristics are correct.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Thermodynamics of Equilibrium
- **Analysis**: Equilibrium conditions ($\\Delta G = 0$), Trouton's rule, temperature dependence of spontaneity and equilibrium constant are standard laws.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Qualitative Anion Analysis
- **Analysis**: $\\text{BaSO}_4$ precipitate, brown ring complex $[\\text{Fe}(\\text{H}_2\\text{O})_5(\\text{NO})]^{2+}$ ($+1$ oxidation state of Fe), and purple nitroprusside sulfide complex are exact qualitative tests.
- **Correct Options**: **(A, B, C, D)**.

### Q31. Standard Reduction Potential Fe3+/Fe
- **Derivation**:
  - $\\text{Fe}^{3+} + e^- \\rightarrow \\text{Fe}^{2+}\\quad (\\Delta G_1^\\circ = -1 F E_1^\\circ = -0.77 F)$
  - $\\text{Fe}^{2+} + 2e^- \\rightarrow \\text{Fe}\\quad (\\Delta G_2^\\circ = -2 F E_2^\\circ = -2(-0.44)F = +0.88 F)$
  - $\\text{Fe}^{3+} + 3e^- \\rightarrow \\text{Fe}\\quad (\\Delta G_3^\\circ = \\Delta G_1^\\circ + \\Delta G_2^\\circ = -0.77 F + 0.88 F = +0.11 F)$
  - $-3 F E_3^\\circ = +0.11 F \\implies E_3^\\circ = -\\frac{0.11}{3} = -0.037 \\approx -0.04\\text{ V}$.
- **Answer**: **-0.04**.

### Q32. Acetate Buffer pH
- **Derivation**:
  $$\\text{pH} = \\text{p}K_a + \\log_{10}\\left(\\frac{[\\text{Salt}]}{[\\text{Acid}]}\\right) = (5 - \\log_{10} 1.8) + \\log_{10}(1) = 5 - 0.255 = 4.745 \\approx 4.75$$
- **Answer**: **4.75**.

### Q33. Molar Mass of FCC Metal
- **Derivation**:
  - $a = 400\\text{ pm} = 4.0 \\times 10^{-8}\\text{ cm}$.
  - $V = a^3 = 6.4 \\times 10^{-23}\\text{ cm}^3$.
  - In FCC, $Z = 4$.
  - $\\rho = \\frac{Z M}{N_A V} \\implies 10.0 = \\frac{4 M}{6.02 \\times 10^{23} \\times 6.4 \\times 10^{-23}} = \\frac{4 M}{38.53} \\implies M = \\frac{385.3}{4} \\approx 96.3\\text{ g/mol}$.
- **Answer**: **96.3**.

### Q34. Overall Order of Reaction
- **Derivation**:
  - Exponents in rate law: $2 + (-1) = 1$.
  - Overall order = 1.
- **Answer**: **1**.

### Q35. Molarity from Osmotic Pressure
- **Derivation**:
  $$\\Pi = C R T \\implies C = \\frac{4.92}{0.0821 \\times 300} = \\frac{4.92}{24.63} = 0.20\\text{ M}$$
- **Answer**: **0.20** (or **0.2**).

### Q36. Common Ion Solubility
- **Derivation**:
  - $K_{sp} = (1.0 \\times 10^{-5})^2 = 1.0 \\times 10^{-10}$.
  - In $0.010\\text{ M } \\text{BaCl}_2$, $[\\text{Ba}^{2+}] = 0.010\\text{ M}$.
  - $s = \\frac{K_{sp}}{[\\text{Ba}^{2+}]} = \\frac{1.0 \\times 10^{-10}}{0.010} = 1.0 \\times 10^{-8}\\text{ M}$.
  - $k = 1.0$.
- **Answer**: **1** (or **1.0**).

---

## PART III: MATHEMATICS

### Q37. Locus of Complex Number
- **Derivation**:
  - $|z - 2| + |z + 2| = 6$ represents an ellipse with foci at $(\\pm 2, 0)$ and major axis $2a = 6 \\implies a = 3$.
  - Foci distance $2c = 4 \\implies c = 2$.
  - Eccentricity $e = c/a = 2/3$.
- **Correct Option**: **(A)**.

### Q38. Definite Integral
- **Derivation**:
  - Let $I = \\int_0^{\\pi/2} \\frac{\\cos x}{1 + \\sin x + \\cos x}\\,dx$.
  - By King's property: $I = \\int_0^{\\pi/2} \\frac{\\sin x}{1 + \\cos x + \\sin x}\\,dx$.
  - $2I = \\int_0^{\\pi/2} \\frac{\\sin x + \\cos x}{1 + \\sin x + \\cos x}\\,dx = \\int_0^{\\pi/2} \\left(1 - \\frac{1}{1 + \\sin x + \\cos x}\\right)\\,dx = \\frac{\\pi}{2} - \\int_0^{\\pi/2}\\frac{dx}{1+\\sin x+\\cos x}$.
  - For $J = \\int_0^{\\pi/2}\\frac{dx}{1+\\sin x+\\cos x}$: substitute $t = \\tan(x/2)$:
    $$J = \\int_0^1 \\frac{\\frac{2\\,dt}{1+t^2}}{1 + \\frac{2t}{1+t^2} + \\frac{1-t^2}{1+t^2}} = \\int_0^1 \\frac{2\\,dt}{2 + 2t} = \\int_0^1 \\frac{dt}{1+t} = \\ln 2$$
  - $2I = \\frac{\\pi}{2} - \\ln 2 \\implies I = \\frac{\\pi}{4} - \\frac{1}{2}\\ln 2$.
- **Correct Option**: **(A)**.

### Q39. Normal to Rectangular Hyperbola
- **Derivation**:
  - Equation: $y = c^2/x \\implies \\frac{dy}{dx} = -\\frac{c^2}{x^2} = -\\frac{1}{t^2}$.
  - Normal slope $m = t^2$.
  - Equation of normal at $(ct, c/t)$: $y - \\frac{c}{t} = t^2 (x - ct) \\implies y = t^2 x - c t^3 + \\frac{c}{t}$.
  - Intersection with curve $xy = c^2$: substitute $x = ct', y = c/t'$:
    $$\\frac{c}{t'} = t^2 (ct') - c t^3 + \\frac{c}{t} \\implies \\frac{1}{t'} - \\frac{1}{t} = t^2(t' - t) \\implies \\frac{t - t'}{t t'} = t^2(t' - t)$$
  - Since $t' \\ne t$: $-\\frac{1}{t t'} = t^2 \\implies t' = -\\frac{1}{t^3}$.
- **Correct Option**: **(A)**.

### Q40. Linear Differential Equation
- **Derivation**:
  - Integrating factor: $\\text{IF} = e^{\\int \\tan x\\,dx} = e^{\\ln|\\sec x|} = \\sec x$.
  - Solution: $y \\sec x = \\int \\sec x \\sec x\\,dx = \\int \\sec^2 x\\,dx = \\tan x + C$.
  - $y = \\sin x + C \\cos x$.
- **Correct Option**: **(A)**.

### Q41. Permutation with Grouping
- **Derivation**:
  - "PERMUTATION": 11 letters: P, E, R, M, U, T, A, T, I, O, N.
  - Vowels: E, U, A, I, O (5 vowels, all distinct).
  - Consonants: P, R, M, T, T, N (6 consonants, with two T's).
  - Treat the 5 vowels as a single block: total items $= 6 + 1 = 7$ items.
  - Number of arrangements of items $= \\frac{7!}{2!}$.
  - Number of arrangements of vowels within block $= 5!$.
  - Total $= 5! \\times \\frac{7!}{2!}$.
- **Correct Option**: **(A)**.

### Q42. Direction Cosines
- **Derivation**:
  - $n = -(l + m) \\implies n^2 = (l + m)^2 = l^2 + 2lm + m^2$.
  - Given $l^2 + m^2 - n^2 = 0 \\implies l^2 + m^2 - (l^2 + 2lm + m^2) = -2lm = 0 \\implies lm = 0$.
  - Case 1: $l = 0 \\implies n = -m$. Direction cosines: $(0, 1, -1) / \\sqrt{2}$.
  - Case 2: $m = 0 \\implies n = -l$. Direction cosines: $(1, 0, -1) / \\sqrt{2}$.
  - Angle: $\\cos\\theta = 0(1) + 1(0) + (-1)(-1) / (\\sqrt{2} \\times \\sqrt{2}) = 1/2 \\implies \\theta = \\pi/3$.
- **Correct Option**: **(A)**.

### Q43. Cubic Function Analysis
- **Analysis**:
  - $f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3)$. Local max at $x = 1$, local min at $x = 3$. (A, B are True)
  - $f''(x) = 6x - 12 = 0 \\implies x = 2$. $f(2) = 8 - 24 + 18 + 1 = 3$. Point of inflection is $(2, 3)$. (C is True)
  - $f(1) = 1 - 6 + 9 + 1 = 5 > 0$, $f(3) = 27 - 54 + 27 + 1 = 1 > 0$. Since local minimum is positive, curve crosses x-axis only once $\\implies$ exactly one real root. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q44. Confocal Conics
- **Analysis**: All four properties are classic theorems of confocal conics.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Real Symmetric Matrices
- **Analysis**: Spectral theorem for real symmetric matrices: real eigenvalues, orthogonal eigenvectors, orthogonal diagonalizability, determinant is product of eigenvalues.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Reciprocal Vector System
- **Analysis**: Fundamental identities of reciprocal basis vectors in $\\mathbb{R}^3$.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Complex Exponential Function
- **Analysis**: Standard analytic properties of $e^z = e^x(\\cos y + i\\sin y)$.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Binomial Distribution
- **Analysis**: Mean $np$, variance $np(1-p)$, variance $< np$ since $0 < p < 1$, maximum variance at $p = 1/2$.
- **Correct Options**: **(A, B, C, D)**.

### Q49. Standard Limit
- **Derivation**:
  $$\\lim_{x \\to 0} \\frac{x - (x - x^3/6 + \\dots)}{x^3} = \\frac{1}{6} \\approx 0.167$$
- **Answer**: **0.167**.

### Q50. Area Between Parabola and Line
- **Derivation**:
  - Intersections: $(2x)^2 = 4x \\implies 4x^2 - 4x = 0 \\implies x = 0, 1$.
  - Area $= \\int_0^1 (\\sqrt{4x} - 2x)\\,dx = \\left[2 \\frac{x^{3/2}}{3/2} - x^2\\right]_0^1 = \\frac{4}{3} - 1 = \\frac{1}{3} \\approx 0.33$.
- **Answer**: **0.33**.

### Q51. Standard Integral
- **Derivation**:
  $$\\int_0^1 \\frac{dx}{1 + x^2} = [\\arctan x]_0^1 = \\frac{\\pi}{4} \\implies k = 4$$
- **Answer**: **4**.

### Q52. Circumradius of Right-Angled Triangle
- **Derivation**:
  - $3-4-5$ triangle is right-angled. The hypotenuse is the diameter of the circumcircle: $2R = 5 \\implies R = 2.5\\text{ cm}$.
- **Answer**: **2.5** (or **2.50**).

### Q53. Number of Solutions
- **Derivation**:
  - $2\\sin^2 x - 3\\sin x + 1 = 0 \\implies (2\\sin x - 1)(\\sin x - 1) = 0$.
  - $\\sin x = 1/2 \\implies x = \\pi/6, 5\\pi/6$ (2 solutions).
  - $\\sin x = 1 \\implies x = \\pi/2$ (1 solution).
  - Total solutions in $[0, 2\\pi]$ is $2 + 1 = 3$.
- **Answer**: **3**.

### Q54. Determinant of Matrix Power
- **Derivation**:
  - $\\det(A) = 2(2) - 1(1) = 4 - 1 = 3$.
  - $\\det(A^3) = (\\det A)^3 = 3^3 = 27$.
- **Answer**: **27**.
"""

with open(os.path.join(MOCK_DIR, "Solutions_Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(sol_p1_content)
print("Generated mock_tests/Mock_15_IIT_Madras/Solutions_Paper_1.md")
