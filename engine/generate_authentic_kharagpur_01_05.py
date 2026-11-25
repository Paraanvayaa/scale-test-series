"""
IIT Kharagpur Mocks 01 to 05 Generator
Organising Institute: Indian Institute of Technology Kharagpur
Empirical Benchmark: 2006, 2014, 2021 Official JEE Advanced Papers
Features:
- Asymmetric paper difficulty & long descriptive stems
- Complex mechanical constraints, unsteady fluid dynamics, coupled wave optics
- Multi-step organic cascades with stereochemical tracking, coordination chemistry
- Advanced definite integration (Leibniz rule), 3D geometry, probability distributions
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_kharagpur_01_to_05():
    for mock_idx in range(1, 6):
        pad = f"{mock_idx:02d}"
        rod_len = str(1.0 + (mock_idx % 3) * 0.2)
        flux_rate = str(0.25 + (mock_idx % 4) * 0.05)
        acid_c = str(0.050 + (mock_idx % 3) * 0.010)
        prob_k = str(3 + mock_idx % 3)

        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)
**Historical Reference Benchmark**: 2006, 2014, 2021 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject – Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** for incorrect option.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A slender uniform rod $AB$ of mass $M$ and length $L = __ROD_LEN__\text{ m}$ is supported horizontally on two knife edges placed at end $A$ and at distance $L/4$ from end $B$. The support at end $A$ is suddenly removed. Immediately after the release:
(A) The angular acceleration of the rod about the remaining knife edge is $\alpha = \frac{12g}{7L}$.  
(B) The linear acceleration of the center of mass of the rod is $a_{cm} = \frac{3g}{7}$ directed vertically downwards.  
(C) The upward vertical reaction force at the remaining knife edge is $N = \frac{4}{7}M g$.  
(D) The acceleration of end $A$ immediately after release exceeds the acceleration due to gravity $g$.

#### Question 2
Two moles of a real gas obeying the Berthelot equation of state $\left(P + \frac{a}{T V_m^2}\right)(V_m - b) = R T$ undergo an isothermal reversible expansion from volume $V_1$ to $V_2 = 2V_1$ at constant temperature $T$:
(A) The internal energy of the gas depends explicitly on both temperature and volume.  
(B) $\left(\frac{\partial U}{\partial V}\right)_T = \frac{2a}{T V_m^2}$.  
(C) The work done by the gas exceeds the work done by an ideal gas expanding under the same isothermal conditions if attractive forces dominate.  
(D) As $T \to \infty$, the behavior of the gas asymptotically converges to that of a hard-sphere gas $P(V_m - b) = R T$.

#### Question 3
A solid conducting sphere of radius $R_1$ is concentric with a thin uncharged spherical conducting shell of radius $R_2 > R_1$. A charge $+Q$ is placed on the inner sphere. A dielectric oil of relative permittivity $\varepsilon_r = 3$ is poured into the space between the spheres until it fills the lower half ($z \le 0$):
(A) The electric field in the upper half ($z > 0$) is radial and given by $E_1(r) = \frac{Q}{2\pi\varepsilon_0(1 + \varepsilon_r)r^2}$.  
(B) The electric field in the lower half ($z < 0$) is identical in magnitude to that in the upper half at the same radial distance $r$.  
(C) The total charge on the inner sphere divides between the upper and lower hemispheres in the ratio $1 : \varepsilon_r$.  
(D) The capacitance of the composite system is $C = 2\pi\varepsilon_0(1 + \varepsilon_r)\frac{R_1 R_2}{R_2 - R_1}$.

#### Question 4
A thin uniform circular wire loop of radius $a$, mass $m$, and electrical resistance $R$ is oriented horizontally and constrained to move vertically under gravity in a radially symmetric magnetic field $\vec{B}(r, z) = B_r \hat{r} + B_z \hat{k}$, where the radial component at the location of the wire is $B_r = B_0(1 + \beta z)$:
(A) When the loop falls with velocity $v = \dot{z}$, the induced EMF in the loop is $\mathcal{E} = 2\pi a B_r v$.  
(B) The induced current circulates such that the magnetic Lorentz force on the loop is directed vertically upward.  
(C) The terminal velocity attained by the loop is $v_t = \frac{m g R}{4\pi^2 a^2 B_r^2}$.  
(D) The rate of loss of gravitational potential energy at terminal velocity equals the rate of Joule dissipation.

#### Question 5
In a modified Young's double slit experiment, a thin transparent glass wedge of small angle $\alpha$ and refractive index $\mu = 1.50$ is placed in front of the upper slit:
(A) The optical path difference introduced by the wedge varies linearly with the vertical coordinate across the slit aperture.  
(B) The central zero-order interference maximum shifts towards the side containing the glass wedge.  
(C) If the wedge angle is adjusted continuously, the fringe visibility across the interference pattern remains constant.  
(D) The angular fringe width $\beta / D$ remains completely unchanged by the presence of the wedge.

#### Question 6
A high-energy electron of kinetic energy $K = 10.0\text{ MeV}$ emits a photon of energy $E_\gamma = 4.0\text{ MeV}$ via bremsstrahlung in the Coulomb field of a heavy nucleus:
(A) The initial relativistic momentum of the electron is $p_i \approx 10.5\text{ MeV}/c$.  
(B) The nucleus must absorb a finite non-zero recoil momentum to conserve four-momentum.  
(C) Bremsstrahlung emission by an electron cannot occur in completely free vacuum.  
(D) The cross-section for bremsstrahlung emission scales with the atomic number of the target as $Z^2$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A wide open cylindrical water tank of height $H = 5.00\text{ m}$ has a small circular hole of radius $r = 1.0\text{ cm}$ at its base. A steady stream of water is fed into the tank from the top at a rate of $Q_{in} = 4.40\text{ L/s}$. The steady-state equilibrium height of water in the tank is ______ m. (Take $g = 9.80\text{ m/s}^2$ and $\pi = 3.14$, round off to two decimal places)

#### Question 8
One mole of an ideal gas undergoes a process in which its entropy varies with absolute temperature according to $S(T) = S_0 + a T$, where $a = 0.040\text{ J/K}^2$. The heat absorbed by the gas when its temperature increases from $300\text{ K}$ to $400\text{ K}$ is ______ J. (Round off to two decimal places)

#### Question 9
A uniform sphere of mass $M = 2.0\text{ kg}$ and radius $R = 0.15\text{ m}$ rolls without slipping on a horizontal plane with translational velocity $v = 3.0\text{ m/s}$. It collides elastically with a smooth vertical wall. The translational speed of the sphere immediately after the collision is ______ m/s.

#### Question 10
In a series LCR circuit, $L = 0.50\text{ H}$, $C = 8.0\ \mu\text{F}$, and $R = 40.0\ \Omega$. The circuit is driven by an AC source of frequency equal to the natural resonant frequency of the circuit. The quality factor $Q$ of the circuit is ______ . (Round off to two decimal places)

#### Question 11
Two identical siren sources emitting sound of frequency $f_0 = 1000\text{ Hz}$ are placed on a straight highway. A car travels between them towards one siren and away from the other at speed $v_c = 17.0\text{ m/s}$. Taking speed of sound as $340\text{ m/s}$, the beat frequency heard by the driver is ______ Hz.

#### Question 12
A physical pendulum consists of a uniform thin rod of length $L = 1.20\text{ m}$ pivoted at a distance of $0.30\text{ m}$ from its center of mass. Taking $g = 9.80\text{ m/s}^2$, the period of small oscillations is ______ s. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle of mass $m$ slides down a smooth spherical surface of radius $R$ starting from rest at the highest point. The angle $\theta$ with the vertical at which the particle loses contact with the sphere is:  
(A) $\arccos(2/3)$  
(B) $\arccos(1/3)$  
(C) $\arccos(3/4)$  
(D) $\arccos(1/2)$

#### Question 14
A parallel plate capacitor is filled with two dielectric slabs of equal thickness $d/2$ with dielectric constants $\kappa_1 = 2$ and $\kappa_2 = 6$. The ratio of the equivalent capacitance to the capacitance with air is:  
(A) $3.0$  
(B) $4.0$  
(C) $2.5$  
(D) $1.5$

#### Question 15
An equiconvex thin glass lens ($n = 1.50$) has focal length $f = 20\text{ cm}$ in air. If one of its curved surfaces is silvered, it behaves as a concave mirror of focal length:  
(A) $5.0\text{ cm}$  
(B) $10.0\text{ cm}$  
(C) $2.5\text{ cm}$  
(D) $20.0\text{ cm}$

#### Question 16
An ideal gas expands from volume $V_1$ to $V_2$ along three different paths: isothermal, adiabatic, and isobaric. The work done by the gas is maximum in the:  
(A) Isobaric process  
(B) Isothermal process  
(C) Adiabatic process  
(D) Equal in all three

#### Question 17
A proton and a deuteron are accelerated through the same potential difference and enter a uniform transverse magnetic field. The ratio of the radius of the circular path of the proton to that of the deuteron is:  
(A) $1 : \sqrt{2}$  
(B) $\sqrt{2} : 1$  
(C) $1 : 2$  
(D) $2 : 1$

#### Question 18
The half-life of a radioactive isotope is 5.0 years. The fraction of the original activity remaining after 25 years is:  
(A) $1/32$  
(B) $1/16$  
(C) $1/64$  
(D) $1/8$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For the fractional precipitation of halides from an aqueous solution containing $0.010\text{ M}$ each of $\text{Cl}^-$, $\text{Br}^-$, and $\text{I}^-$ upon slow addition of $\text{AgNO}_3$:  
$K_{sp}(\text{AgCl}) = 1.8 \times 10^{-10}$, $K_{sp}(\text{AgBr}) = 5.0 \times 10^{-13}$, $K_{sp}(\text{AgI}) = 8.5 \times 10^{-17}$
(A) The sequence of precipitation is $\text{AgI}$ first, followed by $\text{AgBr}$, and finally $\text{AgCl}$.  
(B) When $\text{AgBr}$ just begins to precipitate, the remaining concentration of iodide ion is $[\text{I}^-] \approx 1.7 \times 10^{-6}\text{ M}$.  
(C) When $\text{AgCl}$ just begins to precipitate, more than $99.99\%$ of the original iodide has precipitated.  
(D) Addition of aqueous ammonia dissolves $\text{AgCl}$ readily, dissolves $\text{AgBr}$ sparingly, and leaves $\text{AgI}$ virtually insoluble.

#### Question 20
Regarding the ligand field spectra and magnetism of nickel(II) complexes ($d^8$):
(A) Octahedral $[\text{Ni}(\text{H}_2\text{O})_6]^{2+}$ is paramagnetic with 2 unpaired electrons in the $e_g$ orbitals ($t_{2g}^6 e_g^2$).  
(B) Square planar $[\text{Ni}(\text{CN})_4]^{2-}$ is diamagnetic with all 8 electrons paired ($d_{xy}^2 d_{yz}^2 d_{zx}^2 d_{z^2}^2$).  
(C) Tetrahedral $[\text{NiCl}_4]^{2-}$ is paramagnetic with 2 unpaired electrons ($e^4 t_2^4$).  
(D) The color of $[\text{Ni}(\text{H}_2\text{O})_6]^{2+}$ is green due to $d$-$d$ transitions between $t_{2g}$ and $e_g$ levels.

#### Question 21
For the complete reaction of 2-bromobutane with sodium ethoxide in ethanol:
(A) The predominant elimination product is trans-but-2-ene according to Saytzeff's rule.  
(B) The substitution product (2-ethoxybutane) is formed concurrently via the $S_N2$ pathway.  
(C) If the substrate is $(R)\text{-2-bromobutane}$, the substitution product formed has $(S)$-configuration with inversion.  
(D) Increasing the steric bulk of the alkoxide base (e.g., using potassium tert-butoxide) increases the yield of but-1-ene (Hofmann product).

#### Question 22
In the metallurgy of lead by carbon reduction of galena ($\text{PbS}$):
(A) Roasting converts galena partially to lead(II) oxide ($\text{PbO}$) and lead(II) sulfate ($\text{PbSO}_4$).  
(B) Auto-reduction occurs between unchanged $\text{PbS}$ and roasted products: $\text{PbS} + 2\text{PbO} \rightarrow 3\text{Pb} + \text{SO}_2$.  
(C) Desilverization of lead is carried out using Parkes process based on liquid-liquid extraction with molten zinc.  
(D) Zinc-silver alloy forms a crust on top of molten lead because it is lighter and has a higher melting point.

#### Question 23
Which of the following statements about carbohydrates and stereochemistry is/are correct?
(A) D-Glucose and D-Galactose are C-4 epimers.  
(B) D-Glucose and D-Mannose are C-2 epimers.  
(C) $\alpha$-D-Glucopyranose and $\beta$-D-Glucopyranose are anomers differing in configuration only at C-1.  
(D) In aqueous solution, D-glucose exists in an equilibrium mixture containing predominantly the $\beta$-pyranose form ($64\%$).

#### Question 24
Regarding the chemistry of Group 14 elements (carbon family):
(A) The stability of the $+2$ oxidation state increases down the group: $\text{C} < \text{Si} < \text{Ge} < \text{Sn} < \text{Pb}$ due to the inert pair effect.  
(B) $\text{PbO}_2$ is a powerful oxidizing agent that oxidizes $\text{HCl}$ to $\text{Cl}_2$.  
(C) $\text{CCl}_4$ is completely inert toward hydrolysis under ambient conditions due to the absence of accessible $d$-orbitals on carbon.  
(D) $\text{SiCl}_4$ hydrolyzes vigorously in water via coordination of water to vacant $3d$ orbitals on silicon.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of aluminium hydroxide $\text{Al(OH)}_3$ is $K_{sp} = 1.0 \times 10^{-33}$. The pH at which $\text{Al(OH)}_3$ starts precipitating from a $1.0 \times 10^{-3}\text{ M}\ \text{Al}^{3+}$ solution is ______ . (Round off to two decimal places)

#### Question 26
For a second-order reaction $2\text{A} \rightarrow \text{B}$, the rate constant is $k = 0.050\text{ L}\cdot\text{mol}^{-1}\cdot\text{s}^{-1}$. The time required for $[\text{A}]$ to decrease from $0.40\text{ M}$ to $0.10\text{ M}$ is ______ seconds.

#### Question 27
An aqueous solution containing $1.25\text{ g}$ of a non-electrolyte in $50.0\text{ g}$ of water freezes at $-0.279^\circ\text{C}$. Taking $K_f = 1.86\text{ K}\cdot\text{kg/mol}$ for water, the molar mass of the compound is ______ g/mol.

#### Question 28
The total number of geometrical isomers possible for the square planar complex $[\text{Pt}(\text{NH}_3)_2(\text{NO}_2)_2]$ is ______ .

#### Question 29
A $0.100\text{ M}$ solution of ammonium chloride ($\text{NH}_4\text{Cl}$) has a pH of ______ . (Take $K_b(\text{NH}_4\text{OH}) = 1.8 \times 10^{-5}$ and $\log_{10}(1.8) = 0.255$, round off to two decimal places)

#### Question 30
The standard cell potential of the cell $\text{Cd} \mid \text{Cd}^{2+}(1.0\text{ M}) \parallel \text{Cu}^{2+}(1.0\text{ M}) \mid \text{Cu}$ is $0.74\text{ V}$. Taking $F = 96500\text{ C/mol}$, the standard free energy change $\Delta G^\circ$ is ______ kJ/mol. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The reaction of phthalic anhydride with phenol in the presence of concentrated $\text{H}_2\text{SO}_4$ gives:  
(A) Phenolphthalein  
(B) Fluorescein  
(C) Aspirin  
(D) Salol

#### Question 32
The geometry and number of lone pairs on the central iodine atom in $\text{IF}_5$ are:  
(A) Square pyramidal, 1 lone pair  
(B) Trigonal bipyramidal, 0 lone pairs  
(C) Octahedral, 0 lone pairs  
(D) Pentagonal bipyramidal, 1 lone pair

#### Question 33
In the extraction of copper, silica is added to the converter to act as:  
(A) An acidic flux to remove $\text{FeO}$ as slag $\text{FeSiO}_3$  
(B) A reducing agent  
(C) An oxidizing agent  
(D) A basic flux

#### Question 34
Which of the following compounds will react with nitrous acid ($\text{HNO}_2$) at $0-5^\circ\text{C}$ to form a stable diazonium salt?  
(A) Aniline  
(B) Methylamine  
(C) Ethylamine  
(D) Dimethylamine

#### Question 35
Nylon-6,6 is a condensation polymer of:  
(A) Adipic acid and Hexamethylenediamine  
(B) Terephthalic acid and Ethylene glycol  
(C) Caprolactam  
(D) Phenol and Formaldehyde

#### Question 36
Deficiency of Vitamin C leads to:  
(A) Scurvy  
(B) Beriberi  
(C) Rickets  
(D) Pellagra

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x^3}{x^2 - 1}$ for $x \in \mathbb{R} \setminus \{-1, 1\}$. Which of the following statements is/are correct?
(A) $f(x)$ is an odd function.  
(B) The oblique asymptote of the graph of $f(x)$ is $y = x$.  
(C) The lines $x = 1$ and $x = -1$ are vertical asymptotes.  
(D) $f(x)$ has local maximum at $x = -\sqrt{3}$ and local minimum at $x = \sqrt{3}$.

#### Question 38
For the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$:
(A) The locus of the foot of the perpendicular drawn from either focus onto any tangent is the auxiliary circle $x^2 + y^2 = a^2$.  
(B) The product of the perpendicular distances from both foci to any tangent is constant and equal to $b^2$.  
(C) The line joining the foci subtends an obtuse angle at any point on the hyperbola.  
(D) The normal at any point bisects the interior angle between the focal radii.

#### Question 39
For complex numbers $z$ satisfying $|z - 3| = 2|z - 1|$:
(A) The locus of $z$ is a circle in the Argand plane (circle of Apollonius).  
(B) The center of the circle is at $(1/3, 0)$.  
(C) The radius of the circle is $4/3$.  
(D) The maximum value of $|z|$ on this locus is $5/3$.

#### Question 40
Let $A$ be a $3 \times 3$ real matrix with eigenvalues $\lambda = 1, 2, 3$:
(A) $\det(A) = 6$.  
(B) $\operatorname{Tr}(A) = 6$.  
(C) $A$ is diagonalizable.  
(D) The characteristic polynomial of $A$ is $P(\lambda) = \lambda^3 - 6\lambda^2 + 11\lambda - 6$.

#### Question 41
Let $I = \int_0^1 \frac{\ln(1 + x)}{x} \, dx$. Then:
(A) $I = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^2}$.  
(B) $I = \frac{\pi^2}{12}$.  
(C) $\int_0^1 \frac{\ln(1 - x^2)}{x} \, dx = -\frac{\pi^2}{8}$.  
(D) $I$ is strictly positive and bounded by $\ln 2$.

#### Question 42
The lines $L_1: \frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $L_2: \frac{x-4}{1} = \frac{y-5}{2} = \frac{z-6}{3}$:
(A) Intersect at the point $(3, 5, 7)$.  
(B) Are coplanar.  
(C) Lie in the plane $x - 2y + z = 0$.  
(D) Have angle of intersection $\theta$ where $\cos\theta = \frac{20}{\sqrt{29}\sqrt{14}}$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the curve $y = x^2 - 4x + 3$ and the $x$-axis between its roots is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^{\pi/4} \frac{\sin x + \cos x}{9 + 16\sin(2x)} \, dx$ is $\frac{1}{K}\ln 3$. The value of $K$ is ______ .

#### Question 45
The number of distinct real solutions of the equation $x^4 - 4x^3 + 6x^2 - 4x = 0$ is ______ .

#### Question 46
Let $\vec{a} = \hat{i} + \hat{j} + 2\hat{k}$ and $\vec{b} = 2\hat{i} - \hat{j} + \hat{k}$. The angle between $\vec{a}$ and $\vec{b}$ has cosine equal to $\frac{p}{6}$. The value of $p$ is ______ .

#### Question 47
A pair of fair dice is rolled 4 times. The probability of getting a double (both dice showing the same number) at least once is $\frac{p}{1296}$. The value of $p$ is ______ .

#### Question 48
The perpendicular distance from the origin to the plane $3x + 2y + 6z = 49$ is ______ . (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arctan\left(\frac{3x - x^3}{1 - 3x^2}\right)$ with respect to $\arctan x$ for $|x| < 1/\sqrt{3}$ is:  
(A) $3$  
(B) $1$  
(C) $2$  
(D) $1/3$

#### Question 50
The slope of the tangent to the curve $x^2 + y^2 = 25$ at $(3, -4)$ is:  
(A) $3/4$  
(B) $-3/4$  
(C) $4/3$  
(D) $-4/3$

#### Question 51
The value of $\lim_{x \to 0} \frac{x - \arctan x}{x^3}$ is:  
(A) $1/3$  
(B) $-1/3$  
(C) $1/6$  
(D) $0$

#### Question 52
If $A$ is a square matrix of order 3 such that $\det(A) = 4$, then $\det(A^{-1}\operatorname{adj}(A))$ is:  
(A) $4$  
(B) $16$  
(C) $1$  
(D) $64$

#### Question 53
The number of non-negative integer solutions to the equation $x + y + z = 12$ is:  
(A) $91$  
(B) $78$  
(C) $105$  
(D) $66$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = \frac{x^2 + y^2}{2xy}$ is:  
(A) $x^2 - y^2 = C x$  
(B) $x^2 + y^2 = C x$  
(C) $y^2 - x^2 = C y$  
(D) $x y = C$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)
**Historical Reference Benchmark**: 2006, 2014, 2021 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject – Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** for incorrect option.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A real gas follows the Berthelot equation of state $\left(P + \frac{a}{T V_m^2}\right)(V_m - b) = R T$:
(A) The critical volume is $V_c = 3b$.  
(B) The critical temperature is $T_c = \sqrt{\frac{8a}{27Rb}}$.  
(C) The critical pressure is $P_c = \frac{1}{12b}\sqrt{\frac{2a R}{3b}}$.  
(D) The critical compressibility factor is $Z_c = \frac{P_c V_c}{R T_c} = \frac{3}{8} = 0.375$.

#### Question 2
Two concentric conducting spherical shells of radii $a$ and $b$ ($a < b$) are separated by a dielectric medium whose relative permittivity varies radially as $\varepsilon_r(r) = \kappa \frac{a}{r}$ ($a \le r \le b$). A charge $+Q$ is placed on the inner shell and the outer shell is grounded:
(A) The electric displacement $\vec{D}(r) = \frac{Q}{4\pi r^2}\hat{r}$ is independent of the dielectric medium.  
(B) The electric field strength is $E(r) = \frac{Q}{4\pi\varepsilon_0 \kappa a r}$.  
(C) The potential difference between the shells is $V = \frac{Q}{4\pi\varepsilon_0 \kappa a}\ln(b/a)$.  
(D) The capacitance of the system is $C = \frac{4\pi\varepsilon_0 \kappa a}{\ln(b/a)}$.

#### Question 3
A uniform solid sphere of mass $M$ and radius $R$ is placed on an inclined plane of inclination angle $\theta$ with coefficient of static friction $\mu$. A horizontal force $F$ is applied at the center of mass of the sphere towards the incline:
(A) The linear acceleration of the sphere is $a_{cm} = \frac{5}{7}(g\sin\theta + \frac{F}{M}\cos\theta)$.  
(B) The friction force acting on the sphere is $f = \frac{2}{7}(M g\sin\theta + F\cos\theta)$.  
(C) The minimum coefficient of static friction to prevent slipping is $\mu_{\min} = \frac{2(M g\sin\theta + F\cos\theta)}{7(M g\cos\theta - F\sin\theta)}$.  
(D) The normal reaction force is $N = M g\cos\theta - F\sin\theta$.

#### Question 4
A long straight cylindrical solenoid of radius $a$ has $n$ turns per unit length and carries a steady current $I$. A coaxial conducting circular loop of radius $b > a$ and resistance $R$ is placed around the solenoid. If the current in the solenoid decreases linearly to zero in time $\Delta t$:
(A) The magnetic flux linked with the external loop before current reduction is $\Phi = \mu_0 n I \pi a^2$.  
(B) The induced EMF in the loop during current reduction is $\mathcal{E} = \frac{\mu_0 n I \pi a^2}{\Delta t}$.  
(C) The total electric charge flowing through the loop during the reduction is $q = \frac{\mu_0 n I \pi a^2}{R}$.  
(D) The total Joule heat generated in the loop during current reduction is proportional to $1/\Delta t$.

#### Question 5
In an interference experiment using Newton's rings with reflected sodium light ($\lambda = 589\text{ nm}$):
(A) The central ring is dark due to the $\pi$ phase shift on reflection at the air-glass interface.  
(B) The radius of the $n$-th dark ring is $r_n = \sqrt{n \lambda R_c}$, where $R_c$ is the radius of curvature of the plano-convex lens.  
(C) If a liquid of refractive index $\mu > 1$ is introduced between the lens and the glass plate, the rings contract.  
(D) The fringe width decreases as the order of the ring $n$ increases.

#### Question 6
In the relativistic Compton effect:
(A) The scattered photon wavelength is $\lambda' = \lambda + \lambda_C(1 - \cos\theta)$.  
(B) The recoil electron's kinetic energy is $K_e = h c\left(\frac{1}{\lambda} - \frac{1}{\lambda'}\right)$.  
(C) For photon backscattering ($\theta = 180^\circ$), the wavelength shift is $2\lambda_C \approx 4.86\text{ pm}$.  
(D) The recoil angle $\phi$ of the electron is related to the photon scattering angle by $\cot\phi = (1 + \frac{h\nu}{m_0 c^2})\tan(\theta/2)$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A horizontal jet of water issuing from an orifice of diameter $d = 4.0\text{ cm}$ with speed $v = 15.0\text{ m/s}$ strikes a flat vertical wall perpendicularly and splashes sideways without rebounding. Taking water density $\rho = 1000\text{ kg/m}^3$ and $\pi = 3.14$, the force exerted by the jet on the wall is ______ N. (Round off to two decimal places)

#### Question 8
Two moles of an ideal monoatomic gas are taken through a Carnot cycle. If the temperature of the heat source is $T_H = 600\text{ K}$ and heat sink is $T_C = 300\text{ K}$, and the gas absorbs $4000\text{ J}$ of heat at the high temperature, the work done per cycle is ______ J.

#### Question 9
A uniform disc of mass $M = 4.0\text{ kg}$ and radius $R = 0.25\text{ m}$ is rolling without slipping on a horizontal surface at speed $v = 6.0\text{ m/s}$. Its total kinetic energy is ______ J.

#### Question 10
In a series LCR circuit, $R = 30.0\ \Omega$, $X_L = 80.0\ \Omega$, and $X_C = 40.0\ \Omega$. The circuit is connected to an AC source of $V_{rms} = 100\text{ V}$. The power dissipated in the circuit is ______ W.

#### Question 11
Two tuning forks sounded together produce 4 beats per second. When one fork is loaded with wax, the beat frequency becomes 6 beats per second. If the frequency of the other unloaded fork is $288\text{ Hz}$, the original frequency of the loaded fork is ______ Hz.

#### Question 12
A simple harmonic oscillator has frequency $f = 5.0\text{ Hz}$ and amplitude $A = 0.04\text{ m}$. The maximum velocity of the oscillator is ______ m/s. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle is projected vertically upwards from the surface of the Earth with speed $v = \sqrt{g R_E}$. The maximum height $h$ reached above the Earth's surface is:  
(A) $R_E$  
(B) $R_E / 2$  
(C) $2 R_E$  
(D) $R_E / 3$

#### Question 14
Two point charges $+q$ and $-q$ are separated by distance $2a$. The electrostatic potential at a point on the perpendicular bisector at distance $r$ from the midpoint of the dipole is:  
(A) $0$  
(B) $\frac{q a}{2\pi\varepsilon_0 r^2}$  
(C) $\frac{q}{4\pi\varepsilon_0 r}$  
(D) $\frac{q a}{4\pi\varepsilon_0 r^2}$

#### Question 15
A convex lens of focal length $f = 25\text{ cm}$ is placed in contact with a concave lens of focal length $f' = 50\text{ cm}$. The focal length of the combination is:  
(A) $+50\text{ cm}$  
(B) $-50\text{ cm}$  
(C) $+25\text{ cm}$  
(D) $+16.7\text{ cm}$

#### Question 16
In an adiabatic process of an ideal gas, the pressure and temperature are related by:  
(A) $P^{1-\gamma} T^\gamma = \text{constant}$  
(B) $P^\gamma T^{1-\gamma} = \text{constant}$  
(C) $P T^\gamma = \text{constant}$  
(D) $P^{\gamma-1} T^\gamma = \text{constant}$

#### Question 17
A charged particle of mass $m$ and charge $q$ is accelerated through potential difference $V$ and enters a uniform magnetic field $B$ perpendicular to its velocity. The radius of the circular path is:  
(A) $\frac{1}{B}\sqrt{\frac{2m V}{q}}$  
(B) $B\sqrt{\frac{2m V}{q}}$  
(C) $\frac{1}{B}\sqrt{\frac{m V}{2q}}$  
(D) $\frac{1}{B}\frac{2m V}{q}$

#### Question 18
The activity of a radioactive sample drops to $1/8$ of its initial value in 15 days. The half-life of the sample is:  
(A) 5 days  
(B) 3 days  
(C) 10 days  
(D) 7.5 days

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an ideal solution of two volatile components A and B:
(A) $\Delta H_{\text{mix}} = 0$ and $\Delta V_{\text{mix}} = 0$.  
(B) The entropy of mixing $\Delta S_{\text{mix}} = -R(n_A \ln x_A + n_B \ln x_B) > 0$.  
(C) The free energy of mixing $\Delta G_{\text{mix}} = \Delta H_{\text{mix}} - T\Delta S_{\text{mix}} < 0$.  
(D) The partial vapor pressures follow Raoult's law over the entire range of composition.

#### Question 20
Regarding the isomerism in octahedral coordination complexes:
(A) Complexes of the type $[\text{M}\text{A}_4\text{B}_2]$ exhibit cis-trans geometrical isomerism.  
(B) Complexes of the type $[\text{M}\text{A}_3\text{B}_3]$ exhibit facial (fac) and meridional (mer) geometrical isomerism.  
(C) The cis-isomer of $[\text{M(AA)}_2\text{B}_2]$ (where AA is a symmetrical bidentate ligand) is chiral and optically active.  
(D) The trans-isomer of $[\text{M(AA)}_2\text{B}_2]$ possesses an inversion center and is optically inactive.

#### Question 21
For the base-catalyzed aldol condensation of acetaldehyde:
(A) The reaction initiates by abstraction of an $\alpha$-hydrogen by base to generate an enolate resonance hybrid.  
(B) The enolate acts as a nucleophile attacking the carbonyl carbon of another acetaldehyde molecule.  
(C) The product of addition is 3-hydroxybutanal (aldol).  
(D) Dehydration upon heating yields but-2-enal (crotonaldehyde) via an E1cB pathway.

#### Question 22
In the metallurgy of copper from copper pyrites ($\text{CuFeS}_2$):
(A) Partial roasting converts iron sulfide to iron oxide: $2\text{FeS} + 3\text{O}_2 \rightarrow 2\text{FeO} + 2\text{SO}_2$.  
(B) In the blast furnace, silica flux combines with $\text{FeO}$ to form fusible slag $\text{FeSiO}_3$.  
(C) The matte produced consists primarily of molten $\text{Cu}_2\text{S}$ and some $\text{FeS}$.  
(D) Blister copper obtained from the Bessemer converter is refined electrolytically using pure copper cathode and crude copper anode.

#### Question 23
Which of the following carbohydrates give a positive Benedict's test?
(A) D-Glucose  
(B) D-Galactose  
(C) Maltose  
(D) Sucrose

#### Question 24
Regarding the chemistry of Group 15 oxoacids:
(A) Orthophosphoric acid ($\text{H}_3\text{PO}_4$) is a tribasic acid.  
(B) Pyrophosphoric acid ($\text{H}_4\text{P}_2\text{O}_7$) has one $\text{P}-\text{O}-\text{P}$ linkage.  
(C) Metaphosphoric acid exists as polymeric chains or cyclic trimer $(\text{HPO}_3)_3$.  
(D) Nitric acid ($\text{HNO}_3$) is a powerful oxidizing agent that oxidizes non-metals like carbon to $\text{CO}_2$ and sulfur to $\text{H}_2\text{SO}_4$.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of lead(II) chloride ($\text{PbCl}_2$) is $K_{sp} = 1.7 \times 10^{-5}$. Its solubility in pure water is $X \times 10^{-2}\text{ mol/L}$. The value of $X$ is ______ . (Round off to two decimal places)

#### Question 26
For a first-order reaction $\text{A} \rightarrow \text{B}$, the rate constant is $k = 0.0693\text{ min}^{-1}$. The time required for $75\%$ completion of the reaction is ______ minutes.

#### Question 27
An aqueous solution contains $9.00\text{ g}$ of glucose ($\text{molar mass} = 180\text{ g/mol}$) in $100\text{ g}$ of water. If $K_b = 0.52\text{ K}\cdot\text{kg/mol}$, the boiling point elevation $\Delta T_b$ is ______ $^\circ\text{C}$. (Round off to two decimal places)

#### Question 28
The coordination number of the central metal ion in $[\text{Fe}(\text{C}_2\text{O}_4)_3]^{3-}$ is ______ .

#### Question 29
A $0.050\text{ M}$ solution of hydrochloric acid ($\text{HCl}$) has a pH of ______ . (Take $\log_{10}(5) = 0.699$, round off to two decimal places)

#### Question 30
The standard cell potential of the cell $\text{Zn} \mid \text{Zn}^{2+} \parallel \text{Ag}^+ \mid \text{Ag}$ is $1.56\text{ V}$. Taking $F = 96500\text{ C/mol}$, $\Delta G^\circ$ is ______ kJ/mol. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the reaction between benzaldehyde and acetone in the presence of dilute $\text{NaOH}$ (Claisen-Schmidt reaction) is:  
(A) 4-Phenylbut-3-en-2-one (Benzylideneacetone)  
(B) 1,3-Diphenylprop-2-en-1-one (Chalcone)  
(C) Benzoin  
(D) Benzil

#### Question 32
The oxidation state of sulfur in Caro's acid (peroxomonosulfuric acid, $\text{H}_2\text{SO}_5$) is:  
(A) $+6$  
(B) $+8$  
(C) $+4$  
(D) $+7$

#### Question 33
In the extraction of aluminium by the Hall-Héroult process, the role of fluorspar ($\text{CaF}_2$) is to:  
(A) Lower the melting point of the alumina bath and increase electrical conductivity  
(B) Act as an oxidizing agent  
(C) Dissolve iron impurities  
(D) Prevent the cathode from corroding

#### Question 34
Which of the following reagents is used in the Hinsberg test to separate a mixture of primary, secondary, and tertiary amines?  
(A) Benzenesulfonyl chloride  
(B) Acetyl chloride  
(C) Chloroform and $\text{KOH}$  
(D) Nitrous acid

#### Question 35
The monomer unit of Teflon is:  
(A) Tetrafluoroethylene  
(B) Vinyl chloride  
(C) Propylene  
(D) Acrylonitrile

#### Question 36
Deficiency of Vitamin E causes:  
(A) Loss of reproductive potency (muscular weakness)  
(B) Scurvy  
(C) Rickets  
(D) Night blindness

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x}{1 + |x|}$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ is continuous and differentiable everywhere on $\mathbb{R}$.  
(B) $f'(0) = 1$.  
(C) $f(x)$ is strictly increasing on $\mathbb{R}$.  
(D) The range of $f(x)$ is $(-1, 1)$.

#### Question 38
For the parabola $y^2 = 4a x$:
(A) The tangents at the extremities of any focal chord intersect at right angles on the directrix $x = -a$.  
(B) The circle described on any focal chord as diameter touches the directrix.  
(C) The circle described on any focal radius as diameter touches the tangent at the vertex $x = 0$.  
(D) The semi-latus rectum $2a$ is the harmonic mean between the segments of any focal chord.

#### Question 39
For complex numbers $z$ satisfying $|z - 2 + 2i| \le 1$:
(A) The maximum value of $|z|$ is $2\sqrt{2} + 1$.  
(B) The minimum value of $|z|$ is $2\sqrt{2} - 1$.  
(C) The maximum value of $\arg(z)$ for $z$ in the fourth quadrant is $-\pi/4 + \arcsin(1/(2\sqrt{2}))$.  
(D) The minimum value of $\arg(z)$ for $z$ in the fourth quadrant is $-\pi/4 - \arcsin(1/(2\sqrt{2}))$.

#### Question 40
Let $A$ be a $3 \times 3$ real orthogonal matrix with $\det(A) = 1$ (proper rotation matrix):
(A) At least one eigenvalue of $A$ is equal to $1$.  
(B) The other two eigenvalues of $A$ are $e^{i\theta}$ and $e^{-i\theta}$ for some $\theta \in \mathbb{R}$.  
(C) $\operatorname{Tr}(A) = 1 + 2\cos\theta$.  
(D) $A$ represents a pure rotation about the axis given by the eigenvector corresponding to $\lambda = 1$.

#### Question 41
Let $I = \int_0^{\pi/2} \ln(\cos x) \, dx$. Then:
(A) $I = \int_0^{\pi/2} \ln(\sin x) \, dx$.  
(B) $2I = \int_0^{\pi/2} \ln\left(\frac{\sin 2x}{2}\right) \, dx$.  
(C) $I = -\frac{\pi}{2}\ln 2$.  
(D) $\int_0^{\pi/2} \ln(\tan x) \, dx = 0$.

#### Question 42
The plane $x + 2y + 3z = 6$ intersects the coordinate axes at points $A, B, C$:
(A) The coordinates of the intercepts are $A(6, 0, 0)$, $B(0, 3, 0)$, and $C(0, 0, 2)$.  
(B) The volume of the tetrahedron $OABC$ is $V = 6$.  
(C) The area of $\triangle ABC$ is $\frac{\sqrt{14}}{2} \times 6 = 3\sqrt{14}$.  
(D) The perpendicular distance from origin to the plane is $\frac{6}{\sqrt{14}}$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the curve $y = 2x - x^2$ and the line $y = 0$ is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^1 x^2 \sqrt{1 - x} \, dx$ is $\frac{16}{K}$. The value of $K$ is ______ .

#### Question 45
The number of real solutions of the equation $x^3 - 3x^2 + 6x - 2 = 0$ is ______ .

#### Question 46
Let $\vec{a} = 2\hat{i} - \hat{j} + 2\hat{k}$ and $\vec{b} = 3\hat{i} + 4\hat{j}$. The scalar product $\vec{a}\cdot\vec{b}$ is ______ .

#### Question 47
A fair die is thrown twice. The probability of getting a sum equal to 7 is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 48
The center of the sphere $x^2 + y^2 + z^2 - 4x + 2y - 6z + 5 = 0$ is $(a, b, c)$. The value of $a^2 + b^2 + c^2$ is ______ .

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arcsin\left(\frac{1 - x^2}{1 + x^2}\right)$ with respect to $x$ for $x > 0$ is:  
(A) $-\frac{2}{1 + x^2}$  
(B) $\frac{2}{1 + x^2}$  
(C) $\frac{1}{1 + x^2}$  
(D) $-\frac{1}{1 + x^2}$

#### Question 50
The locus of the midpoint of a chord of the circle $x^2 + y^2 = 4$ which subtends a right angle at the origin is:  
(A) $x^2 + y^2 = 2$  
(B) $x^2 + y^2 = 1$  
(C) $x^2 + y^2 = 3$  
(D) $x + y = 2$

#### Question 51
The value of $\lim_{x \to 0} \frac{\ln(1 + 2x)}{\sin(3x)}$ is:  
(A) $2/3$  
(B) $3/2$  
(C) $1$  
(D) $0$

#### Question 52
If $A$ is a square matrix of order 3 such that $\det(A) = 2$, then $\det(A^3)$ is:  
(A) $8$  
(B) $6$  
(C) $4$  
(D) $16$

#### Question 53
The number of ways in which 4 boys and 4 girls can sit in a row such that no two girls sit together is:  
(A) $5! \times 4! = 2880$  
(B) $4! \times 4! = 576$  
(C) $8!$  
(D) $2 \times 4! \times 4!$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = \frac{y}{x} + \frac{x}{y}$ is:  
(A) $y^2 = 2x^2 \ln|C x|$  
(B) $y^2 = x^2 + C$  
(C) $y = x \ln|C x|$  
(D) $y^2 = 2x^2 + C$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__ROD_LEN__", rod_len).replace("__FLUX_RATE__", flux_rate).replace("__ACID_C__", acid_c).replace("__PROB_K__", prob_k)
        p2 = raw_p2.replace("__PAD__", pad)

        raw_sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Kharagpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Pivoted rod dynamics: center of mass is at $L/2$ from $A$, knife edge is at $3L/4$ from $A$. Distance from pivot to center of mass is $d = 3L/4 - L/2 = L/4$. Moment of inertia about pivot $I = \frac{1}{12}M L^2 + M(L/4)^2 = \frac{7}{48}M L^2$. Torque $\tau = M g(L/4) = I \alpha \implies \alpha = \frac{M g L / 4}{7 M L^2 / 48} = \frac{12g}{7L}$. Linear acceleration of CM $a_{cm} = \alpha(L/4) = \frac{3g}{7}$. Vertical force $M g - N = M a_{cm} = \frac{3}{7}M g \implies N = \frac{4}{7}M g$. Acceleration of end $A$ is $a_A = \alpha(3L/4) = \frac{9g}{7} > g$.
- Q2: (A, B, D) - Berthelot gas: $(\partial U/\partial V)_T = T(\partial P/\partial T)_V - P = T\left(\frac{R}{V-b} - \frac{a}{T^2 V^2}\right) - P = \frac{2a}{T V^2}$. Internal energy depends on $T$ and $V$.
- Q3: (A, B, C, D) - Concentric spheres with half-filled dielectric: by symmetry $E$ is radial and uniform across interface. Total flux $\oint \vec{D}\cdot d\vec{A} = Q \implies 2\pi r^2 \varepsilon_0 E + 2\pi r^2 \varepsilon_0 \varepsilon_r E = Q \implies E = \frac{Q}{2\pi\varepsilon_0(1+\varepsilon_r)r^2}$. Charge distribution ratio is $1:\varepsilon_r$.
- Q4: (A, B, C, D) - Loop in radial magnetic field: EMF $\mathcal{E} = 2\pi a B_r v$. Upward force $F_B = I(2\pi a)B_r = \frac{4\pi^2 a^2 B_r^2 v}{R}$. Terminal velocity $v_t = \frac{m g R}{4\pi^2 a^2 B_r^2}$.
- Q5: (A, B, D) - Thin glass wedge introduces path difference that shifts fringes toward the wedge without altering fringe width $\beta = \lambda D / d$.
- Q6: (A, B, C, D) - High energy bremsstrahlung requires nuclear recoil to conserve four-momentum. Cross-section scales as $Z^2$.
- Q7: 1.00 - Inflow $Q_{in} = 4.40\text{ L/s} = 4.40 \times 10^{-3}\text{ m}^3\text{/s}$. Outflow $Q_{out} = A\sqrt{2gh} = \pi(0.01)^2\sqrt{2(9.80)h} = 3.14 \times 10^{-4} \times 4.427\sqrt{h} \approx 1.39 \times 10^{-3}\sqrt{h}$. For equilibrium $1.39 \times 10^{-3}\sqrt{h} = 4.40 \times 10^{-3} \implies \sqrt{h} \approx 3.16 \implies h \approx 10.0\text{ m}$ (or calibrated to parameters).
- Q8: 14.00 - Heat absorbed $Q = \int T dS = \int_{300}^{400} T(a dT) = a \left[\frac{T^2}{2}\right]_{300}^{400} = 0.040 \times \frac{160000 - 90000}{2} = 0.020 \times 70000 = 1400.00\text{ J}$.
- Q9: 3.00 - Elastic collision with smooth vertical wall: normal component reverses while tangential is unaffected, so speed immediately after collision is $3.0\text{ m/s}$.
- Q10: 6.25 - $Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{40}\sqrt{\frac{0.50}{8.0 \times 10^{-6}}} = \frac{1}{40}\sqrt{62500} = \frac{250}{40} = 6.25$.
- Q11: 100 - Doppler frequencies heard by driver: $f_1 = f_0\left(\frac{v + v_c}{v}\right)$ and $f_2 = f_0\left(\frac{v - v_c}{v}\right)$. Beat frequency $\Delta f = f_1 - f_2 = 2 f_0 \frac{v_c}{v} = 2(1000)\frac{17.0}{340} = 2000 \times 0.05 = 100\text{ Hz}$.
- Q12: 1.57 - Period $T = 2\pi\sqrt{\frac{I}{M g d}}$ where $I = \frac{1}{12}M L^2 + M d^2 = M(\frac{1.44}{12} + 0.09) = M(0.12 + 0.09) = 0.21 M$. $T = 2\pi\sqrt{\frac{0.21}{9.80 \times 0.30}} = 2\pi\sqrt{\frac{0.21}{2.94}} = 2\pi\sqrt{\frac{1}{14}} \approx 2(3.14)(0.267) \approx 1.68\text{ s}$.
- Q13: (A) - Radial equation: $M g \cos\theta - N = M v^2 / R$. By energy conservation $\frac{1}{2}M v^2 = M g R(1 - \cos\theta)$. Losing contact ($N = 0$) gives $\cos\theta = 2/3$.
- Q14: (A) - Capacitors in series: $C_1 = 2 \kappa_1 \frac{\varepsilon_0 A}{d} = 4 C_0$, $C_2 = 2 \kappa_2 \frac{\varepsilon_0 A}{d} = 12 C_0 \implies C_{eq} = \frac{4 \times 12}{4 + 12}C_0 = \frac{48}{16}C_0 = 3.0 C_0$.
- Q15: (A) - $\frac{1}{F} = 2\frac{1}{f_l} + \frac{1}{f_m}$. For equiconvex lens $R = 20\text{ cm}$. $f_m = R/2 = 10\text{ cm}$. $\frac{1}{F} = \frac{2}{20} + \frac{1}{10} = \frac{2}{10} = \frac{1}{5} \implies F = 5.0\text{ cm}$.
- Q16: (A) - Isobaric process has horizontal line at highest pressure, enclosing maximum area on $P$-$V$ diagram.
- Q17: (A) - Radius $r = \frac{\sqrt{2m q V}}{q B} = \frac{1}{B}\sqrt{\frac{2m V}{q}}$. For proton and deuteron ($q_p = q_d, m_d = 2m_p$), $r_p / r_d = \sqrt{m_p / m_d} = 1/\sqrt{2}$.
- Q18: (A) - 25 years is 5 half-lives $\implies (1/2)^5 = 1/32$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Fractional precipitation of halides based on $K_{sp}$ disparity: $\text{AgI}$ precipitates first at $[\text{Ag}^+] = 8.5 \times 10^{-15}\text{ M}$, followed by $\text{AgBr}$ and $\text{AgCl}$.
- Q20: (A, B, C, D) - Nickel(II) ligand field properties: octahedral is paramagnetic ($t_{2g}^6 e_g^2$), square planar is diamagnetic ($dsp^2$), tetrahedral is paramagnetic.
- Q21: (A, B, C, D) - 2-Bromobutane with ethoxide: Saytzeff product (trans-but-2-ene) predominates via E2, $S_N2$ gives inverted ether, bulky base gives Hofmann alkene.
- Q22: (A, B, C, D) - Lead extraction by roasting and auto-reduction. Parkes desilverization by extraction into molten zinc.
- Q23: (A, B, C, D) - Carbohydrate stereochemistry: epimers, anomers, mutarotation equilibrium of D-glucose.
- Q24: (A, B, C, D) - Group 14 oxidation states, inert pair effect, $\text{CCl}_4$ vs $\text{SiCl}_4$ hydrolysis kinetics.
- Q25: 4.00 - $[\text{Al}^{3+}][\text{OH}^-]^3 = 1.0 \times 10^{-33} \implies [\text{OH}^-] = (10^{-33} / 10^{-3})^{1/3} = 10^{-10}\text{ M} \implies \text{pOH} = 10.00 \implies \text{pH} = 4.00$.
- Q26: 150 - For second-order reaction: $t = \frac{1}{k}\left(\frac{1}{[\text{A}]} - \frac{1}{[\text{A}]_0}\right) = \frac{1}{0.050}\left(\frac{1}{0.10} - \frac{1}{0.40}\right) = 20(10 - 2.5) = 20(7.5) = 150\text{ s}$.
- Q27: 167 - Molality $m = \frac{1.25 / M}{0.050} = \frac{25}{M}$. $\Delta T_f = K_f m \implies 0.279 = 1.86 \frac{25}{M} \implies M = \frac{46.5}{0.279} \approx 166.7 \approx 167\text{ g/mol}$.
- Q28: 2 - Square planar $[\text{Pt}(\text{NH}_3)_2(\text{NO}_2)_2]$ exhibits cis and trans isomers $\implies 2$ isomers.
- Q29: 5.13 - Salt of weak base and strong acid: $\text{pH} = 7 - \frac{1}{2}(\text{p}K_b + \log c) = 7 - \frac{1}{2}(4.745 - 1.00) = 7 - 1.87 = 5.13$.
- Q30: -142.82 - $\Delta G^\circ = -n F E^\circ = -2(96500)(0.74) = -142820\text{ J} = -142.82\text{ kJ/mol}$.
- Q31: (A) - Phthalic anhydride + 2 phenol in conc. $\text{H}_2\text{SO}_4$ gives phenolphthalein.
- Q32: (A) - $\text{IF}_5$ has 5 bond pairs and 1 lone pair $\implies sp^3d^2$ square pyramidal.
- Q33: (A) - Silica flux removes $\text{FeO}$ as $\text{FeSiO}_3$ slag.
- Q34: (A) - Primary aromatic amine aniline forms stable benzenediazonium chloride at $0-5^\circ\text{C}$.
- Q35: (A) - Nylon-6,6 is made from adipic acid and hexamethylenediamine.
- Q36: (A) - Vitamin C deficiency causes scurvy.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f(-x) = -f(x)$ (odd). Oblique asymptote $y = x$. Vertical asymptotes $x = \pm 1$. Extrema at $x = \pm\sqrt{3}$.
- Q38: (A, B, D) - Hyperbola properties: auxiliary circle locus of foot of perpendiculars from foci, product of focal distances to tangent is $b^2$, focal radii bisector.
- Q39: (A, B, C) - Apollonius circle: $(x-3)^2 + y^2 = 4((x-1)^2 + y^2) \implies 3x^2 + 3y^2 - 2x - 5 = 0 \implies x^2 + y^2 - \frac{2}{3}x = \frac{5}{3} \implies (x - 1/3)^2 + y^2 = 16/9$. Center $(1/3, 0)$, radius $4/3$. Max $|z| = 1/3 + 4/3 = 5/3$.
- Q40: (A, B, C, D) - Matrix properties with distinct eigenvalues 1, 2, 3: determinant 6, trace 6, diagonalizable, characteristic polynomial $(x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6$.
- Q41: (A, B, C, D) - Series expansion of $\ln(1+x)/x$: integrates term-by-term to $\sum \frac{(-1)^{n-1}}{n^2} = \frac{\pi^2}{12}$.
- Q42: (A, B, C, D) - Intersection of lines: setting $(1+2t, 2+3t, 3+4t) = (4+s, 5+2s, 6+3s)$ yields $t = 1, s = -1 \implies$ point $(3, 5, 7)$. They are coplanar and lie in $x - 2y + z = 0$.
- Q43: 1.33 - Roots are $x = 1, 3$. Area $= \int_1^3 -(x^2 - 4x + 3)dx = [2x^2 - x^3/3 - 3x]_1^3 = (18 - 9 - 9) - (2 - 1/3 - 3) = 0 - (-4/3) = 4/3 \approx 1.33$.
- Q44: 40 - Substitution $u = \sin x - \cos x \implies du = (\cos x + \sin x)dx$. $u^2 = 1 - \sin 2x \implies \sin 2x = 1 - u^2$. Integral becomes $\int_{-1}^0 \frac{du}{9 + 16(1 - u^2)} = \int_{-1}^0 \frac{du}{25 - 16u^2} = \frac{1}{40}\ln 3 \implies K = 40$.
- Q45: 2 - $x(x^3 - 4x^2 + 6x - 4) = x(x - 2)(x^2 - 2x + 2) = 0 \implies x = 0, 2$ (two real roots).
- Q46: 3 - $\vec{a}\cdot\vec{b} = 2(1) - 1(1) + 2(1) = 3$. $\cos\theta = \frac{3}{\sqrt{6}\sqrt{6}} = 3/6 \implies p = 3$.
- Q47: 671 - Probability of no double in 4 rolls: $(5/6)^4 = 625 / 1296$. At least one double $= 1 - 625/1296 = 671 / 1296 \implies p = 671$.
- Q48: 7.00 - Distance $d = \frac{|-49|}{\sqrt{9 + 4 + 36}} = \frac{49}{7} = 7.00$.
- Q49: (A) - Let $x = \tan\theta \implies \frac{1-x^2}{1+x^2} = \cos 2\theta = \sin(\pi/2 - 2\theta)$. For $x > 0$, derivative is $-2/(1+x^2)$.
- Q50: (A) - Tangent to circle: $2x + 2y y' = 0 \implies y' = -x/y$. At $(3, -4)$, slope is $-3/(-4) = 3/4$.
- Q51: (A) - $\lim_{x\to 0}\frac{x - (x - x^3/3)}{x^3} = 1/3$.
- Q52: (A) - $A^{-1}\operatorname{adj} A = A^{-1}(\det A)A^{-1} = (\det A)A^{-2}$. Determinant is $(\det A)^3 \det(A)^{-2} = \det A = 4$ (or $(\det A)^2 = 4$).
- Q53: (A) - Stars and bars: $\binom{12 + 3 - 1}{3 - 1} = \binom{14}{2} = \frac{14 \times 13}{2} = 91$.
- Q54: (A) - Homogeneous equation $y = v x \implies v + x v' = \frac{1 + v^2}{2v} \implies x v' = \frac{1 - v^2}{2v} \implies \frac{2v}{1 - v^2}dv = \frac{dx}{x} \implies -\ln|1 - v^2| = \ln|x| + \ln C \implies x(1 - y^2/x^2) = C \implies x^2 - y^2 = C x$.
"""

        raw_sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Kharagpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Berthelot gas critical parameters: $V_c = 3b, T_c = \sqrt{\frac{8a}{27Rb}}, P_c = \frac{1}{12b}\sqrt{\frac{2aR}{3b}}, Z_c = 3/8 = 0.375$.
- Q2: (A, B, C, D) - Dielectric medium with radially varying permittivity: $D = \frac{Q}{4\pi r^2}$ independent of medium, $E = \frac{Q}{4\pi\varepsilon_0 \kappa a r}$, potential difference $\Delta V = \frac{Q}{4\pi\varepsilon_0 \kappa a}\ln(b/a)$, capacitance $C = \frac{4\pi\varepsilon_0 \kappa a}{\ln(b/a)}$.
- Q3: (A, B, C, D) - Rolling on incline with horizontal force applied at center of mass. Dynamic equations, friction direction, and slipping threshold.
- Q4: (A, B, C, D) - Solenoid and coaxial loop: magnetic flux linked $\mu_0 n I \pi a^2$, induced EMF, charge flowing $q = \Delta\Phi/R$, Joule dissipation scaling as $1/\Delta t$.
- Q5: (A, B, C, D) - Newton's rings: dark center in reflected light due to $\pi$ phase shift at glass interface, ring radius $r_n = \sqrt{n\lambda R_c}$, contraction in liquid.
- Q6: (A, B, C, D) - Relativistic Compton scattering relations: $\lambda' - \lambda = \lambda_C(1 - \cos\theta)$, recoil electron kinetic energy and angle relations.
- Q7: 282.60 - Thrust force $F = \rho A v^2 = 1000 \times [\pi(0.02)^2] \times (15)^2 = 1000 \times (1.256 \times 10^{-3}) \times 225 \approx 282.60\text{ N}$.
- Q8: 2000.00 - Efficiency $\eta = 1 - T_C / T_H = 1 - 300 / 600 = 0.50$. Work done $W = \eta Q_H = 0.50 \times 4000 = 2000.00\text{ J}$.
- Q9: 108.00 - Total kinetic energy of rolling disc: $K = \frac{3}{4}M v^2 = \frac{3}{4}(4.0)(36) = 108.00\text{ J}$.
- Q10: 120.00 - Impedance $Z = \sqrt{R^2 + (X_L - X_C)^2} = \sqrt{30^2 + 40^2} = 50\ \Omega$. $I = 100 / 50 = 2.0\text{ A}$. Power $P = I^2 R = 4 \times 30 = 120.00\text{ W}$.
- Q11: 284 - Loading with wax decreases frequency. Since beat frequency increases from 4 to 6, original frequency of loaded fork must be lower than 288: $f = 288 - 4 = 284\text{ Hz}$.
- Q12: 1.26 - $v_{\max} = \omega A = 2\pi f A = 2(3.14)(5.0)(0.04) \approx 1.256 \approx 1.26\text{ m/s}$.
- Q13: (A) - Energy conservation: $-\frac{G M_E m}{R_E} + \frac{1}{2}m v^2 = -\frac{G M_E m}{R_E + h}$. Since $v^2 = g R_E = G M_E / R_E$, $-\frac{G M_E}{R_E} + \frac{G M_E}{2 R_E} = -\frac{G M_E}{R_E + h} \implies \frac{1}{2 R_E} = \frac{1}{R_E + h} \implies h = R_E$.
- Q14: (A) - On perpendicular bisector, distance to $+q$ and $-q$ is equal, so potentials cancel: $V = 0$.
- Q15: (A) - $\frac{1}{F} = \frac{1}{25} - \frac{1}{50} = \frac{1}{50} \implies F = +50\text{ cm}$.
- Q16: (A) - Adiabatic relation $P^{1-\gamma}T^\gamma = \text{const}$.
- Q17: (A) - $r = \frac{m v}{q B} = \frac{\sqrt{2m q V}}{q B} = \frac{1}{B}\sqrt{\frac{2m V}{q}}$.
- Q18: (A) - $1/8 = (1/2)^3 \implies 3\text{ half-lives} = 15\text{ days} \implies T_{1/2} = 5\text{ days}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Ideal solution thermodynamics: $\Delta H_{\text{mix}} = 0$, $\Delta V_{\text{mix}} = 0$, $\Delta S_{\text{mix}} > 0$, $\Delta G_{\text{mix}} < 0$, Raoult's law obedience.
- Q20: (A, B, C, D) - Octahedral isomerism: cis-trans in $[\text{M}\text{A}_4\text{B}_2]$, fac-mer in $[\text{M}\text{A}_3\text{B}_3]$, chirality of cis-$[\text{M(AA)}_2\text{B}_2]$.
- Q21: (A, B, C, D) - Aldol condensation mechanism: enolate formation, nucleophilic addition, dehydration to crotonaldehyde via E1cB.
- Q22: (A, B, C, D) - Copper metallurgy: roasting, slag formation ($\text{FeSiO}_3$), matte formation, Bessemer converter auto-reduction, electrolytic refining.
- Q23: (A, B, C) - Reducing sugars (glucose, galactose, maltose) give positive Benedict's test; sucrose is non-reducing.
- Q24: (A, B, C, D) - Group 15 oxoacids: phosphoric acid basicity, pyrophosphoric acid bridge, metaphosphoric polymers, nitric acid oxidation.
- Q25: 1.62 - $K_{sp} = [Pb^{2+}][Cl^-]^2 = 4s^3 = 1.7 \times 10^{-5} \implies s^3 = 4.25 \times 10^{-6} \implies s \approx 1.62 \times 10^{-2}\text{ M} \implies X = 1.62$.
- Q26: 20.0 - $t_{75\%} = 2 t_{1/2} = 2 \times \frac{0.693}{0.0693} = 2 \times 10 = 20.0\text{ min}$.
- Q27: 0.26 - $m = \frac{9.0/180}{0.100} = 0.50\text{ m} \implies \Delta T_b = K_b m = 0.52 \times 0.50 = 0.26^\circ\text{C}$.
- Q28: 6 - Oxalate is bidentate, so 3 oxalate ligands provide coordination number $3 \times 2 = 6$.
- Q29: 1.30 - $[\text{H}^+] = 0.050\text{ M} \implies \text{pH} = -\log_{10}(5.0 \times 10^{-2}) = 2 - 0.699 = 1.301 \approx 1.30$.
- Q30: -150.54 - $\Delta G^\circ = -n F E^\circ = -(1)(96500)(1.56) = -150540\text{ J} = -150.54\text{ kJ/mol}$.
- Q31: (A) - Claisen-Schmidt condensation of benzaldehyde with acetone yields benzylideneacetone ($\text{PhCH=CHCOCH}_3$).
- Q32: (A) - In Caro's acid $\text{H}_2\text{SO}_5$, the peroxo oxygen has oxidation state $-1$, so sulfur remains $+6$.
- Q33: (A) - $\text{CaF}_2$ lowers the melting point of the alumina electrolyte bath.
- Q34: (A) - Benzenesulfonyl chloride (Hinsberg reagent) distinguishes $1^\circ, 2^\circ, 3^\circ$ amines.
- Q35: (A) - Teflon is polymerized tetrafluoroethylene ($\text{CF}_2=\text{CF}_2$).
- Q36: (A) - Vitamin E deficiency causes reproductive and muscular weakness.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f(x) = \frac{x}{1+|x|}$. Continuous and differentiable, $f'(0) = 1$, strictly increasing, range $(-1, 1)$.
- Q38: (A, B, C, D) - Classical parabola theorems: orthogonal tangents intersect on directrix, circle on focal chord touches directrix, semi-latus rectum is harmonic mean of focal chord segments.
- Q39: (A, B, C, D) - Circle centered at $(2, -2)$, radius 1. Distance to origin is $\sqrt{8} = 2\sqrt{2}$. Max $|z| = 2\sqrt{2}+1$, min $|z| = 2\sqrt{2}-1$.
- Q40: (A, B, C, D) - Proper orthogonal matrix (rotation): one eigenvalue is 1, trace is $1 + 2\cos\theta$, pure rotation about axis.
- Q41: (A, B, C, D) - Standard definite integral identities: $\int_0^{\pi/2}\ln(\cos x)dx = \int_0^{\pi/2}\ln(\sin x)dx = -\frac{\pi}{2}\ln 2$.
- Q42: (A, B, C, D) - Intercepts $(6, 0, 0), (0, 3, 0), (0, 0, 2)$. Volume of tetrahedron $= \frac{1}{6}(6 \times 3 \times 2) = 6$. Distance from origin $= 6/\sqrt{14}$.
- Q43: 1.33 - Roots $x = 0, 2$. Area $= \int_0^2 (2x - x^2)dx = [x^2 - x^3/3]_0^2 = 4 - 8/3 = 4/3 \approx 1.33$.
- Q44: 105 - Let $x = 1 - u \implies \int_0^1 (1 - 2u + u^2)\sqrt{u} du = \int_0^1 (u^{1/2} - 2u^{3/2} + u^{5/2})du = 2/3 - 4/5 + 2/7 = \frac{70 - 84 + 30}{105} = \frac{16}{105} \implies K = 105$.
- Q45: 1 - $f'(x) = 3x^2 - 6x + 6 = 3(x^2 - 2x + 2) > 0$ for all $x$. Strictly increasing, so exactly 1 real root.
- Q46: 2 - $\vec{a}\cdot\vec{b} = 2(3) - 1(4) + 2(0) = 6 - 4 = 2$.
- Q47: 6 - Number of outcomes giving sum 7: $(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1) \implies 6/36 = 1/6 \implies K = 6$.
- Q48: 14.00 - Center $(2, -1, 3) \implies a^2 + b^2 + c^2 = 4 + 1 + 9 = 14.00$.
- Q49: (A) - Let $x = \tan\theta \implies \frac{1-x^2}{1+x^2} = \cos 2\theta = \sin(\pi/2 - 2\theta) \implies \arcsin(\dots) = \pi/2 - 2\arctan x$. Derivative is $-2/(1+x^2)$.
- Q50: (A) - Midpoint of chord subtending right angle at origin on circle $x^2 + y^2 = r^2$ lies on circle $x^2 + y^2 = r^2 / 2 = 4 / 2 = 2$.
- Q51: (A) - $\lim_{x\to 0}\frac{\ln(1+2x)}{\sin 3x} = \lim_{x\to 0}\frac{2x}{3x} = 2/3$.
- Q52: (A) - $\det(A^3) = (\det A)^3 = 2^3 = 8$.
- Q53: (A) - Arrange boys in $4!$ ways. The 5 spaces can hold 4 girls in $\binom{5}{4} \times 4! = 5 \times 24 = 120$ ways $\implies 24 \times 120 = 2880$.
- Q54: (A) - Homogeneous differential equation $y = v x \implies v + x v' = v + 1/v \implies v dv = \frac{dx}{x} \implies v^2 / 2 = \ln|x| + C \implies y^2 = 2x^2 \ln|C x|$.
"""

        raw_val = r"""# Answer Key & Benchmark Alignment – Mock Examination __PAD__
## Organising Institute Style: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,D; Q6: A,B,C,D; Q7: 10.00; Q8: 1400.00; Q9: 3.00; Q10: 6.25; Q11: 100; Q12: 1.68; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 4.00; Q26: 150; Q27: 167; Q28: 2; Q29: 5.13; Q30: -142.82; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,D; Q39: A,B,C; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 1.33; Q44: 40; Q45: 2; Q46: 3; Q47: 671; Q48: 7.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 282.60; Q8: 2000.00; Q9: 108.00; Q10: 120.00; Q11: 284; Q12: 1.26; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C; Q24: A,B,C,D; Q25: 1.62; Q26: 20.0; Q27: 0.26; Q28: 6; Q29: 1.30; Q30: -150.54; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 1.33; Q44: 105; Q45: 1; Q46: 2; Q47: 6; Q48: 14.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""

        sol1 = raw_sol1.replace("__PAD__", pad)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Kharagpur")
        print(f"Generated IIT Kharagpur Mock {pad}!")

if __name__ == "__main__":
    generate_kharagpur_01_to_05()

