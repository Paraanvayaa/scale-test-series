import os

MOCK_DIR = os.path.join("mock_tests", "Mock_11_IIT_Kanpur")
os.makedirs(MOCK_DIR, exist_ok=True)

# ----------------------------------------------------
# PAPER 1
# ----------------------------------------------------
p1_content = """# JEE (Advanced) Mock Examination 11
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

**Q1.** A particle of mass $m$ moves in one dimension under the potential $V(x) = V_0 \\left(\\frac{x^2}{a^2} - \\frac{x^4}{2a^4}\\right)$, where $V_0$ and $a$ are positive constants. The angular frequency of small oscillations about the stable equilibrium position $x = 0$ is:
(A) $\\sqrt{\\frac{2V_0}{m a^2}}$  
(B) $\\sqrt{\\frac{V_0}{m a^2}}$  
(C) $\\sqrt{\\frac{V_0}{2m a^2}}$  
(D) $2\\sqrt{\\frac{V_0}{m a^2}}$  

**Q2.** A spherical metal shell of inner radius $a$ and outer radius $b$ carries a net charge $+Q$. A point charge $+q$ is placed at the center of the cavity. The electric potential at a point $P$ at distance $r$ from the center ($a < r < b$) is:
(A) $\\frac{1}{4\\pi\\varepsilon_0}\\frac{Q + q}{b}$  
(B) $\\frac{1}{4\\pi\\varepsilon_0}\\frac{q}{a}$  
(C) $\\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{b}$  
(D) $0$  

**Q3.** An ideal gas undergoes an expansion wherein its pressure and volume are related by $P = \\alpha V$, where $\\alpha$ is a constant. The molar heat capacity of the gas for this process is ($C_v$ is the isochoric molar heat capacity):
(A) $C_v + \\frac{R}{2}$  
(B) $C_v + R$  
(C) $C_v + 2R$  
(D) $C_v - \\frac{R}{2}$  

**Q4.** A long coaxial cable consists of an inner solid cylindrical conductor of radius $a$ carrying a steady current $I$, and an outer thin cylindrical conducting shell of radius $b$ carrying return current $I$ uniformly distributed over its surface. The self-inductance per unit length of the cable (neglecting internal inductance of the conductors) is:
(A) $\\frac{\\mu_0}{2\\pi}\\ln(b/a)$  
(B) $\\frac{\\mu_0}{4\\pi}\\ln(b/a)$  
(C) $\\frac{\\mu_0}{2\\pi}(b - a)$  
(D) $\\frac{\\mu_0}{4\\pi}$  

**Q5.** In a double-slit experiment, one of the slits is covered by a thin glass plate of thickness $t_1$ and refractive index $\\mu_1 = 1.6$, while the other slit is covered by a glass plate of thickness $t_2$ and refractive index $\\mu_2 = 1.4$. If the central fringe remains at the center of the screen, the ratio of thicknesses $t_1 / t_2$ must be:
(A) $2/3$  
(B) $3/2$  
(C) $4/5$  
(D) $1/2$  

**Q6.** The binding energy per nucleon for a certain nucleus is $E_b$. If the mass number is $A$ and atomic number is $Z$, the actual mass of the nucleus is ($m_p$ and $m_n$ are proton and neutron masses, $c$ is speed of light):
(A) $Z m_p + (A - Z)m_n - \\frac{A E_b}{c^2}$  
(B) $Z m_p + (A - Z)m_n + \\frac{A E_b}{c^2}$  
(C) $A m_p - \\frac{E_b}{c^2}$  
(D) $Z m_p + (A - Z)m_n - \\frac{E_b}{c^2}$  

---

### SECTION 2: One or More Than One Correct Option (Qs 7–12)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q7.** A uniform rod of mass $M$ and length $L$ rests horizontally on two knife edges placed at its ends $A$ and $B$. The support at end $B$ is suddenly removed:
(A) The instantaneous angular acceleration of the rod about $A$ is $\\frac{3g}{2L}$.  
(B) The initial reaction force at support $A$ immediately after removing $B$ is $Mg/4$.  
(C) The downward acceleration of the center of mass immediately after release is $\\frac{3}{4}g$.  
(D) The reaction force at support $A$ remains $Mg/2$ at the instant of release.  

**Q8.** A cylindrical container of height $H$ and radius $R$ is half-filled with water. It is rotated about its central axis with angular velocity $\\omega$:
(A) The pressure at the bottom is maximum at the perimeter $r = R$.  
(B) The difference between the maximum and minimum pressure at the bottom of the container is $\\frac{1}{2}\\rho \\omega^2 R^2$.  
(C) If $\\omega$ exceeds $\\sqrt{2gH}/R$, the bottom of the container begins to be exposed at the center.  
(D) The total vertical downward force exerted by the water on the bottom of the container equals the weight of the water.  

**Q9.** A conducting circular loop of radius $r$ and resistance $R$ is placed in a spatially uniform but time-dependent magnetic field $\\vec{B}(t) = B_0 e^{-\\alpha t}\\hat{k}$:
(A) The induced electric field inside the loop wire has magnitude $E = \\frac{1}{2} r B_0 \\alpha e^{-\\alpha t}$.  
(B) The total charge that flows through the loop from $t = 0$ to $t = \\infty$ is $\\frac{\\pi r^2 B_0}{R}$.  
(C) The rate of Joule heating is maximum at $t = 0$.  
(D) The total energy dissipated as heat in the resistor from $t = 0$ to $t = \\infty$ is $\\frac{\\pi^2 r^4 B_0^2 \\alpha}{4R}$.  

**Q10.** For an ideal gas undergoing a polytropic process $P V^n = \\text{constant}$:
(A) The molar heat capacity is $C = C_v + \\frac{R}{1 - n}$.  
(B) If $1 < n < \\gamma$, the molar heat capacity is negative.  
(C) If $n = \\gamma$, the process is reversible adiabatic and $C = 0$.  
(D) If $n = 1$, the process is isothermal and $C = \\infty$.  

**Q11.** In the Davisson-Germer electron diffraction experiment:
(A) A beam of accelerated electrons strikes a nickel crystal target.  
(B) A strong diffraction peak is observed at an accelerating potential of $54\\text{ V}$ and scattering angle $50^\\circ$.  
(C) The wavelength calculated from de Broglie's relation agrees with that obtained from Bragg's law ($0.165\\text{ nm}$).  
(D) This experiment verified the de Broglie hypothesis of the wave nature of moving particles.  

**Q12.** An astronomical telescope has an objective lens of focal length $f_o = 100\\text{ cm}$ and an eyepiece of focal length $f_e = 5.0\\text{ cm}$. In normal adjustment (image at infinity):
(A) The angular magnification of the telescope is $20$.  
(B) The length of the telescope tube is $105\\text{ cm}$.  
(C) The intermediate image formed by the objective lens is real, inverted, and located at the focal point of the objective.  
(D) If the telescope is focused on an object at $20\\text{ m}$, the tube length must be increased.  

---

### SECTION 3: Numerical Value Questions (Qs 13–18)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q13.** A uniform thin disc of mass $M = 2.0\\text{ kg}$ and radius $R = 0.4\\text{ m}$ rolls without slipping on a horizontal plane with velocity $v = 6.0\\text{ m/s}$. The total kinetic energy of the disc (in Joules) is:  

**Q14.** In an RC charging circuit, a capacitor of capacitance $C = 50\\,\\mu\\text{F}$ is charged through a resistor $R = 20\\text{ k}\\Omega$ by a DC voltage source of $V = 10\\text{ V}$. The time taken (in seconds) for the charge on the capacitor to reach $63.2\\%$ of its steady-state value is:  

**Q15.** A capillary tube of radius $r = 0.5\\text{ mm}$ is dipped vertically in water ($T = 0.075\\text{ N/m}$, $\\rho = 1000\\text{ kg/m}^3$, $\\theta = 0^\\circ$). Taking $g = 10\\text{ m/s}^2$, the height of water rise in the capillary (in cm) is:  

**Q16.** A particle of mass $m = 0.1\\text{ kg}$ vibrates with simple harmonic motion of amplitude $A = 0.05\\text{ m}$ and frequency $f = 10\\text{ Hz}$. The maximum restoring force acting on the particle (in Newtons) is (take $\\pi^2 \\approx 9.87$, round to one decimal place):  

**Q17.** The de Broglie wavelength of a thermal neutron at temperature $T = 300\\text{ K}$ is (in nanometers, nm): (Use $m_n = 1.67\\times 10^{-27}\\text{ kg}$, $k_B = 1.38\\times 10^{-23}\\text{ J/K}$, $h = 6.63\\times 10^{-34}\\text{ J}\\cdot\\text{s}$, round to two decimal places):  

**Q18.** A circular coil of $N = 100$ turns and radius $r = 10\\text{ cm}$ carries a current of $I = 0.5\\text{ A}$. The magnetic dipole moment of the coil (in $\\text{A}\\cdot\\text{m}^2$) is (take $\\pi \\approx 3.14$, round to two decimal places):  

---

# PART II: CHEMISTRY (54 Marks)

### SECTION 1: Single Correct Option (Qs 19–24)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q19.** At $298\\text{ K}$, the solubility product of $\\text{Ag}_2\\text{CrO}_4$ is $K_{sp} = 1.1\\times 10^{-12}$. The solubility of $\\text{Ag}_2\\text{CrO}_4$ in pure water (in mol/L) is approximately:
(A) $6.5\\times 10^{-5}\\text{ M}$  
(B) $1.0\\times 10^{-4}\\text{ M}$  
(C) $5.2\\times 10^{-6}\\text{ M}$  
(D) $3.2\\times 10^{-4}\\text{ M}$  

**Q20.** For a second-order reaction $2A \\rightarrow \\text{Products}$, a plot of $1/[A]$ versus time $t$ gives a straight line with:
(A) Slope equal to $2k$ and intercept $1/[A]_0$  
(B) Slope equal to $k$ and intercept $[A]_0$  
(C) Slope equal to $-k$ and intercept $1/[A]_0$  
(D) Slope equal to $k/2$ and intercept $[A]_0$  

**Q21.** In qualitative salt analysis, when an aqueous solution of a cation is treated with potassium ferrocyanide ($\\text{K}_4[\\text{Fe}(\\text{CN})_6]$), a chocolate brown precipitate is formed. The cation present is:
(A) $\\text{Fe}^{3+}$  
(B) $\\text{Cu}^{2+}$  
(C) $\\text{Zn}^{2+}$  
(D) $\\text{Fe}^{2+}$  

**Q22.** The major product obtained when 2-methylbut-2-ene is treated with $\\text{B}_2\\text{H}_6$ in THF followed by alkaline $\\text{H}_2\\text{O}_2$ oxidation (hydroboration-oxidation) is:
(A) 2-methylbutan-2-ol  
(B) 3-methylbutan-2-ol  
(C) 2-methylbutan-1-ol  
(D) 3-methylbutan-1-ol  

**Q23.** The spin-only magnetic moment of $[\\text{NiCl}_4]^{2-}$ is $\\approx 2.83\\text{ BM}$, whereas that of $[\\text{Ni}(\\text{CN})_4]^{2-}$ is $0\\text{ BM}$. The geometries of these two complex ions are respectively:
(A) Tetrahedral and square planar  
(B) Square planar and tetrahedral  
(C) Both tetrahedral  
(D) Both square planar  

**Q24.** When excess sodium thiosulfate solution is added to a precipitate of silver bromide (fixing step in photography), the soluble complex formed is:
(A) $\\text{Na}_3[\\text{Ag}(\\text{S}_2\\text{O}_3)_2]$  
(B) $\\text{Na}[\\text{Ag}(\\text{S}_2\\text{O}_3)]$  
(C) $\\text{Na}_2[\\text{Ag}(\\text{SO}_3)_2]$  
(D) $\\text{Ag}_2\\text{S}_2\\text{O}_3$  

---

### SECTION 2: One or More Than One Correct Option (Qs 25–30)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q25.** For the Daniell cell $\\text{Zn}(s)|\\text{Zn}^{2+}(aq)||\\text{Cu}^{2+}(aq)|\\text{Cu}(s)$ with standard potential $E^\\circ = 1.10\\text{ V}$:
(A) The cell EMF increases if $[\\text{Cu}^{2+}]$ is increased at constant $[\\text{Zn}^{2+}]$.  
(B) The cell EMF decreases if $[\\text{Zn}^{2+}]$ is increased at constant $[\\text{Cu}^{2+}]$.  
(C) The equilibrium constant for the cell reaction is $K = 10^{2 E^\\circ / 0.06} \\approx 10^{36.7}$.  
(D) When the cell reaches electrical equilibrium, $E_{\\text{cell}} = 0$ and $\\Delta G = 0$.  

**Q26.** Regarding negative deviation from Raoult's law (e.g. chloroform + acetone):
(A) $\\Delta H_{\\text{mix}} < 0$ (exothermic mixing due to hydrogen bonding between unlike molecules).  
(B) $\\Delta V_{\\text{mix}} < 0$ (contraction on mixing).  
(C) The total vapor pressure is less than that predicted by Raoult's law.  
(D) The mixture forms a maximum boiling azeotrope.  

**Q27.** Which of the following statements is/are correct regarding potassium permanganate ($\\text{KMnO}_4$)?
(A) In acidic medium, $\\text{MnO}_4^-$ is reduced to $\\text{Mn}^{2+}$ (change in oxidation state $= 5$).  
(B) In neutral or faintly alkaline medium, $\\text{MnO}_4^-$ is reduced to $\\text{MnO}_2$ (change in oxidation state $= 3$).  
(C) In strongly alkaline medium, $\\text{MnO}_4^-$ is reduced to manganate $\\text{MnO}_4^{2-}$ (change in oxidation state $= 1$).  
(D) $\\text{KMnO}_4$ acts as a self-indicator in redox titrations.  

**Q28.** In the Kolbe-Schmitt reaction:
(A) Sodium phenoxide is heated with carbon dioxide under pressure ($4 - 7\\text{ atm}$) at $400\\text{ K}$.  
(B) The major product after acidification is salicylic acid (2-hydroxybenzoic acid).  
(C) Phenoxide ion is more reactive towards electrophilic aromatic substitution than neutral phenol.  
(D) Carbon dioxide acts as a weak electrophile attacking the ortho-position preferentially due to chelation with $\\text{Na}^+$.  

**Q29.** In a buffer solution composed of a weak base $BOH$ and its conjugate acid salt $BCl$:
(A) $\\text{pOH} = pK_b + \\log\\frac{[\\text{Salt}]}{[\\text{Base}]}$.  
(B) Buffer capacity is maximum when $[\\text{Salt}] = [\\text{Base}]$.  
(C) Diluting the buffer solution with pure water does not change the pH appreciably.  
(D) Adding a small amount of strong acid converts $\\text{BOH}$ to $B^+$, neutralizing the added $\\text{H}^+$.  

**Q30.** For the elimination reactions of alkyl halides:
(A) E2 elimination occurs in a single concerted step with anti-periplanar geometry.  
(B) E1 elimination involves a two-step mechanism via a carbocation intermediate.  
(C) With bulky strong bases like potassium tert-butoxide, the less substituted Hofmann alkene predominates.  
(D) With unhindered strong bases like ethoxide, the more substituted Saytzeff alkene predominates.  

---

### SECTION 3: Numerical Value Questions (Qs 31–36)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q31.** The solubility product of magnesium hydroxide $\\text{Mg(OH)}_2$ is $K_{sp} = 1.2\\times 10^{-11}$. The pH of a saturated aqueous solution of $\\text{Mg(OH)}_2$ is (round to two decimal places):  

**Q32.** An element crystallizes in an FCC lattice with unit cell edge length $a = 400\\text{ pm}$. The number of unit cells present in $1.0\\text{ cm}^3$ of this crystal, expressed as $A \\times 10^{22}$, has $A$ equal to (round to two decimal places):  

**Q33.** A first-order reaction has a rate constant $k = 4.62\\times 10^{-3}\\text{ s}^{-1}$. The time (in seconds) required for $50\\%$ of the reactant to react is:  

**Q34.** An organic compound has empirical formula $\\text{CH}_2$. Its molecular mass determined by Victor Meyer method is $70\\text{ g/mol}$. The number of hydrogen atoms present in one molecule of this hydrocarbon is:  

**Q35.** The standard electrode potential for $\\text{Fe}^{3+} + 3e^- \\rightarrow \\text{Fe}$ is $-0.036\\text{ V}$, and for $\\text{Fe}^{2+} + 2e^- \\rightarrow \\text{Fe}$ is $-0.440\\text{ V}$. The standard reduction potential $E^\\circ$ for $\\text{Fe}^{3+} + e^- \\rightarrow \\text{Fe}^{2+}$ (in Volts) is (round to three decimal places):  

**Q36.** The number of geometrical isomers possible for $[\\text{Pt}(\\text{NH}_3)(\\text{py})(\\text{Cl})(\\text{Br})]$ (square planar) is:  

---

# PART III: MATHEMATICS (54 Marks)

### SECTION 1: Single Correct Option (Qs 37–42)
*Marking Scheme: +3 for correct option, -1 for incorrect option, 0 if unanswered.*

**Q37.** The value of the definite integral
$$I = \\int_{0}^{\\pi} \\frac{x}{1 + \\sin x}\\,dx$$
is:
(A) $\\pi$  
(B) $\\frac{\\pi}{2}$  
(C) $2\\pi$  
(D) $\\frac{\\pi^2}{2}$  

**Q38.** The equation of the normal to the curve $y = x^3 - 2x + 1$ at the point $(1, 0)$ is:
(A) $x + y - 1 = 0$  
(B) $x - y - 1 = 0$  
(C) $2x + y - 2 = 0$  
(D) $x + 2y - 1 = 0$  

**Q39.** If the lines $\\frac{x - 1}{1} = \\frac{y - 2}{2} = \\frac{z - 3}{3}$ and $\\frac{x - 2}{2} = \\frac{y - 3}{3} = \\frac{z - 4}{4}$ are skew lines, the shortest distance between them is:
(A) $\\frac{1}{\\sqrt{6}}$  
(B) $\\frac{1}{\\sqrt{3}}$  
(C) $0$ (the lines intersect)  
(D) $\\frac{2}{\\sqrt{6}}$  

**Q40.** A box contains 3 white and 2 black balls. Two balls are drawn at random without replacement. The probability that both balls are white is:
(A) $3/10$  
(B) $1/5$  
(C) $3/5$  
(D) $1/10$  

**Q41.** The area bounded by the parabola $y^2 = 2x$ and the line $x - y = 4$ is:
(A) $18$  
(B) $9$  
(C) $36$  
(D) $27$  

**Q42.** The integrating factor for the differential equation $\\frac{dy}{dx} + \\frac{2}{x}y = x^2$ is:
(A) $x^2$  
(B) $x$  
(C) $1/x^2$  
(D) $e^{2x}$  

---

### SECTION 2: One or More Than One Correct Option (Qs 43–48)
*Marking Scheme: +4 if all correct, 0 if unanswered, -2 if incorrect. Partial marking applicable.*

**Q43.** Let $f(x) = x^4 - 2x^2 + 3$ for all $x \\in \\mathbb{R}$:
(A) $f(x)$ has local minima at $x = -1$ and $x = 1$.  
(B) $f(x)$ has a local maximum at $x = 0$.  
(C) The minimum value of $f(x)$ on $\\mathbb{R}$ is $2$.  
(D) $f(x)$ is an even function.  

**Q44.** For the circle $x^2 + y^2 - 4x - 6y + 9 = 0$:
(A) The center is $(2, 3)$.  
(B) The radius is $2$.  
(C) The circle touches the x-axis.  
(D) The circle touches the y-axis.  

**Q45.** Let $A$ and $B$ be two $3 \\times 3$ matrices such that $A B = 0$:
(A) If $\\det(A) \\ne 0$, then $B = 0$.  
(B) If $\\det(B) \\ne 0$, then $A = 0$.  
(C) It is possible for neither $A$ nor $B$ to be zero.  
(D) $\\det(A) \\det(B) = 0$.  

**Q46.** Let $z_1$ and $z_2$ be two complex numbers such that $|z_1 + z_2| = |z_1 - z_2|$:
(A) $\\arg(z_1) - \\arg(z_2) = \\pm \\pi/2$.  
(B) $z_1 / z_2$ is purely imaginary.  
(C) The vectors representing $z_1$ and $z_2$ in the Argand plane are orthogonal.  
(D) $|z_1 + z_2|^2 = |z_1|^2 + |z_2|^2$.  

**Q47.** Let $f(x) = x^3 - 3x^2 + 3x - 1$ for all $x \\in \\mathbb{R}$:
(A) $f(x) = (x - 1)^3$.  
(B) $f'(x) \\ge 0$ for all $x \\in \\mathbb{R}$.  
(C) $f(x)$ is strictly increasing on $\\mathbb{R}$.  
(D) $f(x) = 0$ has a triple root at $x = 1$.  

**Q48.** Let $\\vec{a}, \\vec{b}, \\vec{c}$ be three vectors such that $\\vec{a} + \\vec{b} + \\vec{c} = \\vec{0}$ and $|\\vec{a}| = 3, |\\vec{b}| = 5, |\\vec{c}| = 7$:
(A) The angle between $\\vec{a}$ and $\\vec{b}$ is $60^\\circ$.  
(B) $\\vec{a} \\cdot \\vec{b} = 15/2$.  
(C) $\\vec{b} \\cdot \\vec{c} = -35/2$.  
(D) $\\vec{a} \\cdot \\vec{c} = -33/2$.  

---

### SECTION 3: Numerical Value Questions (Qs 49–54)
*Marking Scheme: +3 for correct answer, 0 in all other cases.*

**Q49.** The value of the limit
$$L = \\lim_{x \\to 0} \\frac{\\tan x - \\sin x}{x^3}$$
is: (Round to one decimal place)  

**Q50.** The number of distinct real roots of the equation $x^4 - 4x + 3 = 0$ is:  

**Q51.** The slope of the normal to the parabola $y^2 = 4x$ at $(1, 2)$ is:  

**Q52.** The value of the definite integral $\\int_{0}^{\\pi/2} \\sin^2 x\\,dx$ is: (Round to two decimal places, $\\pi \\approx 3.14$)  

**Q53.** The distance between the parallel planes $x + 2y - 2z = 6$ and $x + 2y - 2z = -3$ is:  

**Q54.** The value of the determinant $\\begin{vmatrix} 2 & 1 & 0 \\\\ 1 & 2 & 1 \\\\ 0 & 1 & 2 \\end{vmatrix}$ is:  
"""

with open(os.path.join(MOCK_DIR, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(p1_content)
print("Generated mock_tests/Mock_11_IIT_Kanpur/Paper_1.md")

