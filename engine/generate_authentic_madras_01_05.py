"""
IIT Madras Mocks 01 to 05 Generator
Organising Institute: Indian Institute of Technology Madras
Empirical Benchmark: 2010, 2017, 2024 Official JEE Advanced Papers
Features:
- Electromagnetism dominance (>= 37% of physics: induction, radiation, Poynting vectors)
- Single-correct traps and speed/precision tests
- Physical chemistry dominance: phase equilibria, electrochemistry, ionic equilibria
- Mathematics: Argand plane loci, conics invariants, vector triple products, definite integrals
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_madras_01_to_05():
    for mock_idx in range(1, 6):
        pad = f"{mock_idx:02d}"
        ind_l = str(0.12 + (mock_idx % 4) * 0.02)
        mag_b = str(0.50 + (mock_idx % 3) * 0.10)
        volt_v = str(20.0 + mock_idx * 2.0)
        ang_w = str(60 + mock_idx * 10)

        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)
**Historical Reference Benchmark**: 2010, 2017, 2024 Official Examination Papers  
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
A circular parallel-plate capacitor with plates of radius $R$ separated by distance $d \ll R$ is charged by a constant current $I_0$:
(A) The electric field between the plates is $E(t) = \frac{I_0 t}{\varepsilon_0 \pi R^2}$ (neglecting fringe fields).  
(B) The displacement current density between the plates is $J_d = \frac{I_0}{\pi R^2}$.  
(C) The magnetic field at distance $r < R$ from the central axis is $B(r) = \frac{\mu_0 I_0 r}{2\pi R^2}$.  
(D) The Poynting vector at $r = R$ points radially inward, transmitting electromagnetic energy into the capacitor volume.

#### Question 2
Two concentric spherical conducting shells of radii $a$ and $b$ ($a < b$) have the intervening space filled with two concentric layers of dielectrics: $\kappa_1$ from $r = a$ to $r = c$, and $\kappa_2$ from $r = c$ to $r = b$. The inner shell carries charge $+Q$ and the outer shell is grounded:
(A) The electric displacement $\vec{D}(r) = \frac{Q}{4\pi r^2}\hat{r}$ is continuous across the boundary at $r = c$.  
(B) The electric field exhibits a step discontinuity at $r = c$ with $E(c^-) / E(c^+) = \kappa_2 / \kappa_1$.  
(C) The total bound charge accumulated at the spherical interface $r = c$ is $q_b = Q\left(\frac{1}{\kappa_2} - \frac{1}{\kappa_1}\right)$.  
(D) The capacitance of the system is $C = 4\pi\varepsilon_0\left[\frac{1}{\kappa_1}\left(\frac{1}{a} - \frac{1}{c}\right) + \frac{1}{\kappa_2}\left(\frac{1}{c} - \frac{1}{b}\right)\right]^{-1}$.

#### Question 3
A uniform magnetic field $\vec{B}(t) = B_0 \cos(\omega t)\hat{k}$ exists in a cylindrical region of radius $R$. A rigid square wire frame of side length $2R$ and total resistance $r$ is placed symmetrically with its center on the cylinder axis:
(A) The magnetic flux linked with the square frame is $\Phi(t) = B_0 \pi R^2 \cos(\omega t)$.  
(B) The induced EMF in the frame is $\mathcal{E}(t) = B_0 \pi R^2 \omega \sin(\omega t)$.  
(C) The net magnetic force on the square frame is identically zero at all times.  
(D) The induced current flows in closed symmetric paths around the corners of the square.

#### Question 4
A rigid non-conducting thin ring of mass $m$ and radius $a$ carries a uniformly distributed total charge $q$. It is free to rotate without friction about its fixed vertical central axis. A uniform magnetic field $\vec{B} = B_0 \hat{k}$ is suddenly switched on:
(A) The angular acceleration during the field establishment is produced by the induced non-conservative electric field.  
(B) The angular velocity acquired by the ring after the field reaches $B_0$ is $\omega = \frac{q B_0}{2m}$.  
(C) The mechanical angular momentum acquired by the ring is $L = \frac{1}{2}q B_0 a^2$.  
(D) The final kinetic energy of rotation is $K = \frac{q^2 B_0^2 a^2}{8m}$.

#### Question 5
In an interference experiment using a Lloyd's mirror with a monochromatic source of wavelength $\lambda = 500\text{ nm}$ located at distance $d = 1.0\text{ mm}$ above the mirror surface:
(A) The interference pattern on a screen at distance $D = 1.0\text{ m}$ has fringe width $\beta = 0.25\text{ mm}$.  
(B) The fringe lying at the intersection of the mirror plane and screen is a dark fringe.  
(C) The positions of the bright fringes from the mirror plane are $y_n = (n - 1/2)\frac{\lambda D}{2d}$ ($n = 1, 2, \dots$).  
(D) If the mirror is shifted downward parallel to itself by $\Delta d$, the central dark fringe shifts downward.

#### Question 6
A beam of light of intensity $I$ is incident normally on a flat surface:
(A) If the surface is completely absorbing, the radiation pressure is $P_{\text{rad}} = I/c$.  
(B) If the surface is completely reflecting, the radiation pressure is $P_{\text{rad}} = 2I/c$.  
(C) If the surface reflects a fraction $R$ of the incident power, $P_{\text{rad}} = (1 + R)\frac{I}{c}$.  
(D) Radiation pressure exerts a real, measurable mechanical force verified experimentally by Nichols and Hull.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A cylindrical conductor of radius $a = 2.0\text{ mm}$ carries a non-uniform axial current density $J(r) = J_0(1 - r/a)$, where $J_0 = 3.0 \times 10^6\text{ A/m}^2$. The total current carried by the wire is ______ A. (Take $\pi = 3.14$, round off to two decimal places)

#### Question 8
One mole of an ideal gas undergoes a quasi-static polytropic process $P V^2 = \text{constant}$. If the gas expands from $V_1 = 1.0\text{ L}$ at $P_1 = 4.0\text{ bar}$ to $V_2 = 2.0\text{ L}$, the work done by the gas is ______ J. (Take $1\text{ bar}\cdot\text{L} = 100\text{ J}$, round off to two decimal places)

#### Question 9
A circular disc of mass $M = 4.0\text{ kg}$ and radius $R = 0.25\text{ m}$ is rotating freely about its symmetry axis at $\omega = 20.0\text{ rad/s}$. The magnitude of its angular momentum is ______ $\text{kg}\cdot\text{m}^2/\text{s}$. (Round off to two decimal places)

#### Question 10
In a series LCR circuit, $R = 20.0\ \Omega$, $L = __IND_L__\text{ H}$, and $C = 50.0\ \mu\text{F}$. The resonant angular frequency $\omega_0$ of the circuit is ______ rad/s. (Round off to two decimal places)

#### Question 11
Two tuning forks produce 5 beats per second. When the fork of lower frequency ($f = 440\text{ Hz}$) is loaded with wax, the beat frequency becomes 8 beats per second. The original frequency of the higher-pitch fork is ______ Hz.

#### Question 12
A simple harmonic oscillator has a period $T = 1.57\text{ s}$ and amplitude $A = 0.10\text{ m}$. The maximum acceleration of the oscillator is ______ $\text{m/s}^2$. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle of mass $m$ is tied to one end of a light string of length $L$ and whirled in a vertical circle. The difference in tension between the lowest and highest points of the trajectory is:  
(A) $6 m g$  
(B) $4 m g$  
(C) $2 m g$  
(D) $3 m g$

#### Question 14
Two parallel infinite conducting planes carry uniform surface charge densities $+\sigma$ and $-\sigma$. The electric field between the planes is:  
(A) $\frac{\sigma}{\varepsilon_0}$  
(B) $\frac{\sigma}{2\varepsilon_0}$  
(C) $0$  
(D) $\frac{2\sigma}{\varepsilon_0}$

#### Question 15
A convex lens of focal length $f = 15\text{ cm}$ forms a virtual erect image of magnification $3$. The object distance from the lens is:  
(A) $-10\text{ cm}$  
(B) $-20\text{ cm}$  
(C) $-5\text{ cm}$  
(D) $-30\text{ cm}$

#### Question 16
An ideal gas undergoes an adiabatic process. The relation between volume $V$ and absolute temperature $T$ is:  
(A) $T V^{\gamma-1} = \text{constant}$  
(B) $T^\gamma V = \text{constant}$  
(C) $T V^\gamma = \text{constant}$  
(D) $T^{\gamma-1} V = \text{constant}$

#### Question 17
A long straight wire carries a current of $5.0\text{ A}$. The magnetic field at a radial distance of $10.0\text{ cm}$ from the wire is:  
(A) $1.0 \times 10^{-5}\text{ T}$  
(B) $2.0 \times 10^{-5}\text{ T}$  
(C) $5.0 \times 10^{-5}\text{ T}$  
(D) $0.5 \times 10^{-5}\text{ T}$

#### Question 18
The half-life of a radioactive nuclide is 30 days. The fraction of initial nuclei decaying in 60 days is:  
(A) $3/4$  
(B) $1/4$  
(C) $1/2$  
(D) $7/8$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For the selective complexometric titration of $\text{Ca}^{2+}$ and $\text{Mg}^{2+}$ with $\text{EDTA}^{4-}$:
(A) At $\text{pH} \approx 12$ (using $\text{NaOH}$), $\text{Mg(OH)}_2$ precipitates quantitatively, allowing titration of $\text{Ca}^{2+}$ alone using murexide indicator.  
(B) At $\text{pH} \approx 10$ (ammoniacal buffer), both $\text{Ca}^{2+}$ and $\text{Mg}^{2+}$ form stable $1:1$ chelate complexes with $\text{EDTA}$.  
(C) Eriochrome Black T (EBT) indicator forms a wine-red complex with $\text{Mg}^{2+}$ which turns blue at the equivalence point.  
(D) The conditional formation constant $K'_{MY} = \alpha_Y K_{MY}$ increases monotonically with decreasing pH.

#### Question 20
Regarding the crystal field stabilization energy and magnetic properties of octahedral nickel(II) complexes ($d^8$):
(A) $[\text{Ni}(\text{H}_2\text{O})_6]^{2+}$ is paramagnetic with 2 unpaired electrons ($t_{2g}^6 e_g^2$).  
(B) The CFSE of $[\text{Ni}(\text{H}_2\text{O})_6]^{2+}$ is $-1.2\Delta_o$.  
(C) The spin-only magnetic moment is $\mu_{so} = \sqrt{2(4)} = \sqrt{8} \approx 2.83\text{ BM}$.  
(D) In strong ligand fields, octahedral $d^8$ complexes undergo Jahn-Teller distortion to become diamagnetic.

#### Question 21
For the complete reaction sequence starting from toluene:  
(i) $\text{Cl}_2 / h\nu, \Delta \rightarrow \text{Compound A}$; (ii) $\text{aq. KOH}, \Delta \rightarrow \text{Compound B}$; (iii) $\text{conc. NaOH}, \Delta \rightarrow \text{Compounds C and D}$:
(A) Compound A is benzal chloride ($\text{PhCH}\text{Cl}_2$).  
(B) Compound B is benzaldehyde ($\text{PhCHO}$).  
(C) The third step is a Cannizzaro reaction.  
(D) Compounds C and D are sodium benzoate and benzyl alcohol.

#### Question 22
In the metallurgy and refining of metals:
(A) Zone refining is used for producing ultrapure silicon for semiconductors.  
(B) In the cyanide process for gold extraction, zinc acts as a reducing agent.  
(C) In the Hall-Héroult process, cryolite lowers the melting point of alumina.  
(D) Copper is refined electrolytically using impure copper anode and pure copper cathode.

#### Question 23
Which of the following carbohydrates are reducing sugars?
(A) D-Glucose  
(B) D-Fructose  
(C) Maltose  
(D) Sucrose

#### Question 24
Regarding the chemistry of Group 16 elements:
(A) Oxygen exhibits an anomalous maximum covalency of 4.  
(B) $\text{SF}_6$ is kinetically inert due to steric hindrance.  
(C) Ozone is a bent molecule.  
(D) $\text{H}_2\text{S}$ is more acidic than $\text{H}_2\text{O}$ due to lower bond dissociation energy.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{AgCl}$ is $K_{sp} = 1.8 \times 10^{-10}$. Its solubility in pure water is $X \times 10^{-5}\text{ mol/L}$. The value of $X$ is ______ . (Take $\sqrt{1.8} = 1.34$, round off to two decimal places)

#### Question 26
For a first-order reaction with rate constant $k = 0.0462\text{ min}^{-1}$, the half-life $t_{1/2}$ is ______ minutes.

#### Question 27
An aqueous solution contains $6.00\text{ g}$ of urea ($\text{molar mass} = 60\text{ g/mol}$) in $200\text{ g}$ of water. If $K_b = 0.52\text{ K}\cdot\text{kg/mol}$, the boiling point elevation $\Delta T_b$ is ______ $^\circ\text{C}$. (Round off to two decimal places)

#### Question 28
The coordination number of the central iron ion in $[\text{Fe}(\text{C}_2\text{O}_4)_3]^{3-}$ is ______ .

#### Question 29
A $0.050\text{ M}$ solution of hydrochloric acid ($\text{HCl}$) has a pH of ______ . (Take $\log_{10}(5) = 0.699$, round off to two decimal places)

#### Question 30
The standard cell potential of the cell $\text{Zn} \mid \text{Zn}^{2+} \parallel \text{Cu}^{2+} \mid \text{Cu}$ is $1.10\text{ V}$. Taking $F = 96500\text{ C/mol}$, the standard Gibbs free energy change $\Delta G^\circ$ is ______ kJ/mol. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the Reimer-Tiemann reaction of phenol is:  
(A) Salicylaldehyde  
(B) Salicylic acid  
(C) Benzoic acid  
(D) 4-Chlorophenol

#### Question 32
The molecular shape of $\text{XeF}_4$ is:  
(A) Square planar  
(B) Tetrahedral  
(C) Trigonal bipyramidal  
(D) See-saw

#### Question 33
In the extraction of copper, silica is added to the Bessemer converter to act as:  
(A) An acidic flux to remove $\text{FeO}$  
(B) A reducing agent  
(C) An oxidizing agent  
(D) A basic flux

#### Question 34
Which of the following compounds gives a positive Tollens' test?  
(A) Glucose  
(B) Acetone  
(C) Acetophenone  
(D) Benzophenone

#### Question 35
Nylon-6 is a polymer obtained by the ring-opening polymerization of:  
(A) Caprolactam  
(B) Adipic acid  
(C) Hexamethylenediamine  
(D) Ethylene glycol

#### Question 36
Deficiency of Vitamin C leads to:  
(A) Scurvy  
(B) Beriberi  
(C) Rickets  
(D) Night blindness

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \arctan x - x + \frac{x^3}{3}$ for $x > 0$. Which of the following statements is/are correct?
(A) $f(0) = 0$.  
(B) $f'(x) = \frac{x^4}{1 + x^2} > 0$ for all $x > 0$.  
(C) $f(x) > 0$ for all $x > 0$.  
(D) $\arctan x > x - \frac{x^3}{3}$ for all $x > 0$.

#### Question 38
For the parabola $y^2 = 8x$:
(A) Its focus is at $(2, 0)$.  
(B) The directrix is $x = -2$.  
(C) The length of its latus rectum is $8$.  
(D) The equation of the normal at $(2, 4)$ is $x + y = 6$.

#### Question 39
For complex numbers $z$ satisfying $|z - 3| + |z + 3| = 10$:
(A) The locus is an ellipse in the complex plane.  
(B) The semi-major axis is $a = 5$.  
(C) The semi-minor axis is $b = 4$.  
(D) The eccentricity is $e = 3/5$.

#### Question 40
Let $A$ be a $3 \times 3$ matrix with eigenvalues $\lambda = 1, 2, 4$:
(A) $\det(A) = 8$.  
(B) $\operatorname{Tr}(A) = 7$.  
(C) $A$ is invertible.  
(D) $A$ is diagonalizable.

#### Question 41
Let $I = \int_0^1 \frac{1}{\sqrt{1 - x^2}} \, dx$. Then:
(A) $I = \pi/2$.  
(B) $\int_0^1 \frac{x}{\sqrt{1 - x^2}} \, dx = 1$.  
(C) $\int_0^1 \frac{x^2}{\sqrt{1 - x^2}} \, dx = \pi/4$.  
(D) $I > 0$.

#### Question 42
The plane $x + 2y + 2z = 9$:
(A) Has normal vector in direction $\hat{i} + 2\hat{j} + 2\hat{k}$.  
(B) Has perpendicular distance from origin equal to $3$.  
(C) Intersects the $x$-axis at $(9, 0, 0)$.  
(D) Intersects the $z$-axis at $(0, 0, 4.5)$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the curve $y = 4 - x^2$ and the $x$-axis is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^1 x^3(1 - x) \, dx$ is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real solutions to the equation $x^3 - 4x = 0$ is ______ .

#### Question 46
Let $\vec{a} = 2\hat{i} + 3\hat{j} + 6\hat{k}$. The magnitude $|\vec{a}|$ is ______ .

#### Question 47
A card is drawn from a standard pack of 52 cards. The probability that it is an Ace is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 48
The radius of the circle $x^2 + y^2 - 4x - 6y = 0$ is ______ . (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = \ln(x^2 + 1)$ with respect to $x$ is:  
(A) $\frac{2x}{x^2 + 1}$  
(B) $\frac{1}{x^2 + 1}$  
(C) $\frac{x}{x^2 + 1}$  
(D) $\frac{2}{x^2 + 1}$

#### Question 50
The slope of the tangent to the parabola $y^2 = 4x$ at the point $(1, 2)$ is:  
(A) $1$  
(B) $2$  
(C) $1/2$  
(D) $4$

#### Question 51
The value of $\lim_{x \to 0} \frac{e^x - 1}{x}$ is:  
(A) $1$  
(B) $0$  
(C) $e$  
(D) $\infty$

#### Question 52
If $A$ is a square matrix of order 3 such that $\det(A) = 3$, then $\det(3A)$ is:  
(A) $81$  
(B) $27$  
(C) $9$  
(D) $1$

#### Question 53
The number of permutations of 4 distinct objects taken all at a time is:  
(A) $24$  
(B) $12$  
(C) $6$  
(D) $4$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = 3x^2$ with $y(0) = 1$ is:  
(A) $y = x^3 + 1$  
(B) $y = x^3 - 1$  
(C) $y = 3x^3 + 1$  
(D) $y = x^3$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)
**Historical Reference Benchmark**: 2010, 2017, 2024 Official Examination Papers  
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
A monoatomic ideal gas undergoes a cycle consisting of an isobaric expansion at $P_0$ from $V_0$ to $2V_0$, an isochoric cooling to $P_0 / 2$, an isobaric compression back to $V_0$, and an isochoric heating back to $P_0$:
(A) The net work done by the gas in one cycle is $W = \frac{1}{2}P_0 V_0$.  
(B) The maximum temperature in the cycle occurs at $(P_0, 2V_0)$ and equals $2 T_0$.  
(C) The efficiency of this rectangular cycle is $\eta = \frac{1}{13} \approx 7.69\%$.  
(D) Over a complete cycle, the net change in internal energy is zero.

#### Question 2
Two concentric spherical conducting shells of radii $R_1$ and $R_2$ ($R_1 < R_2$) have charges $Q_1$ and $Q_2$. If the outer shell is grounded:
(A) The potential of the outer shell becomes zero.  
(B) The induced charge on the outer shell is $Q_2' = -Q_1$.  
(C) The electric field outside the outer shell ($r > R_2$) vanishes completely.  
(D) The potential of the inner shell becomes $V_1 = \frac{Q_1}{4\pi\varepsilon_0}\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$.

#### Question 3
A solid sphere of mass $M$ and radius $R$ rolls without slipping down an incline of angle $\theta = 30^\circ$:
(A) Its linear acceleration is $a = \frac{5}{14}g$.  
(B) The minimum coefficient of static friction to prevent slipping is $\mu_{\min} = \frac{2}{7\sqrt{3}}$.  
(C) The fraction of total kinetic energy that is rotational is $2/7$.  
(D) The speed of the center of mass after descending height $h$ is $v = \sqrt{\frac{10}{7}gh}$.

#### Question 4
A long straight solenoid has $n$ turns per unit length and carries an alternating current $I(t) = I_0 \sin(\omega t)$:
(A) The magnetic field inside the solenoid is $\vec{B}(t) = \mu_0 n I_0 \sin(\omega t)\hat{k}$.  
(B) The induced circular electric field inside ($r < R$) is $E(r, t) = -\frac{1}{2}\mu_0 n I_0 \omega r \cos(\omega t)$.  
(C) The induced electric field outside ($r > R$) is $E(r, t) = -\frac{\mu_0 n I_0 \omega R^2}{2r}\cos(\omega t)$.  
(D) The induced electric field is non-conservative with $\oint \vec{E}\cdot d\vec{l} = -\frac{d\Phi_B}{dt}$.

#### Question 5
In an interference experiment using monochromatic light of wavelength $\lambda$:
(A) Bright fringes correspond to path differences of $n\lambda$.  
(B) Dark fringes correspond to path differences of $(n + 1/2)\lambda$.  
(C) The fringe width is given by $\beta = \frac{\lambda D}{d}$.  
(D) The intensity distribution varies as $\cos^2(\delta/2)$.

#### Question 6
Regarding the photoelectric effect:
(A) The maximum kinetic energy of photoelectrons depends linearly on the frequency of incident radiation.  
(B) The stopping potential is independent of the intensity of the light beam.  
(C) The photoelectric current is directly proportional to the incident light intensity.  
(D) Photoelectric emission occurs with negligible time lag ($< 10^{-9}\text{ s}$).

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a Coolidge tube, electrons are accelerated through $50.0\text{ kV}$. The minimum cut-off wavelength $\lambda_{\min}$ of the continuous spectrum is ______ pm. (Take $h c = 1240\text{ eV}\cdot\text{nm}$, round off to two decimal places)

#### Question 8
One mole of an ideal gas expands adiabatically such that its temperature falls from $400\text{ K}$ to $300\text{ K}$. If the gas is monoatomic ($\gamma = 5/3$), the work done by the gas is ______ J. (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$, round off to two decimal places)

#### Question 9
A solid sphere of mass $M = 2.0\text{ kg}$ and radius $R = 0.20\text{ m}$ is rotating at $\omega = 15.0\text{ rad/s}$. Its angular momentum is ______ $\text{kg}\cdot\text{m}^2/\text{s}$. (Round off to two decimal places)

#### Question 10
In a series LCR circuit at resonance, the RMS voltage across the resistor of resistance $R = 100\ \Omega$ is $200\text{ V}$. The power consumed by the circuit is ______ W.

#### Question 11
Two tuning forks produce 4 beats per second. If the higher frequency is $512\text{ Hz}$, the frequency of the other fork is ______ Hz.

#### Question 12
A simple pendulum of length $L = 0.81\text{ m}$ has period $T$. Taking $g = 9.80\text{ m/s}^2$, the value of $T$ is ______ s. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The orbital velocity of a satellite orbiting close to the Earth's surface is approximately:  
(A) $7.9\text{ km/s}$  
(B) $11.2\text{ km/s}$  
(C) $5.5\text{ km/s}$  
(D) $9.8\text{ km/s}$

#### Question 14
Two point charges $+q$ and $+q$ are placed at distance $2d$ apart. The electric field at the midpoint is:  
(A) $0$  
(B) $\frac{q}{2\pi\varepsilon_0 d^2}$  
(C) $\frac{q}{4\pi\varepsilon_0 d^2}$  
(D) $\frac{q}{\pi\varepsilon_0 d^2}$

#### Question 15
A convex lens of focal length $f = 20\text{ cm}$ produces a real inverted image of the same size as the object. The object distance is:  
(A) $40\text{ cm}$  
(B) $20\text{ cm}$  
(C) $10\text{ cm}$  
(D) $30\text{ cm}$

#### Question 16
An ideal gas undergoes an adiabatic expansion. The gas:  
(A) Cools down  
(B) Heats up  
(C) Maintains constant temperature  
(D) Absorbs heat

#### Question 17
A proton enters a uniform magnetic field perpendicular to its velocity. Its path is:  
(A) A circle  
(B) A straight line  
(C) A parabola  
(D) A hyperbola

#### Question 18
The half-life of a radioisotope is 8 days. The fraction remaining after 24 days is:  
(A) $1/8$  
(B) $1/4$  
(C) $1/16$  
(D) $1/2$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an ideal solution of components A and B obeying Raoult's law:
(A) $\Delta H_{\text{mix}} = 0$.  
(B) $\Delta V_{\text{mix}} = 0$.  
(C) $\Delta S_{\text{mix}} > 0$.  
(D) $\Delta G_{\text{mix}} < 0$.

#### Question 20
Regarding the complex ion $[\text{Fe}(\text{CN})_6]^{4-}$:
(A) The oxidation state of iron is $+2$.  
(B) It has a $d^6$ low-spin electron configuration ($t_{2g}^6 e_g^0$).  
(C) It is diamagnetic.  
(D) Its hybridization is $d^2sp^3$.

#### Question 21
Which of the following undergo Cannizzaro reaction with concentrated alkali?
(A) Formaldehyde  
(B) Benzaldehyde  
(C) Trimethylacetaldehyde (Pivaldehyde)  
(D) Acetaldehyde

#### Question 22
In the metallurgy of aluminium:
(A) Bauxite is concentrated using Bayer's process.  
(B) Hall-Héroult process uses molten cryolite as solvent for alumina.  
(C) Carbon anodes are consumed during electrolysis.  
(D) Refined aluminium is obtained at the cathode.

#### Question 23
Which of the following are reducing sugars?
(A) Glucose  
(B) Fructose  
(C) Maltose  
(D) Sucrose

#### Question 24
Regarding the chemistry of Group 16 elements:
(A) Oxygen has maximum covalency of 4.  
(B) Sulfur forms stable $\text{S}_8$ crown-shaped molecules.  
(C) $\text{SF}_6$ is octahedral and chemically inert.  
(D) Ozone oxidizes moist $\text{KI}$ to $\text{I}_2$.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of lead sulfate ($\text{PbSO}_4$) is $K_{sp} = 1.6 \times 10^{-8}$. Its solubility in pure water is $X \times 10^{-4}\text{ mol/L}$. The value of $X$ is ______ . (Take $\sqrt{1.6} = 1.26$, round off to two decimal places)

#### Question 26
A first-order reaction has a rate constant $k = 0.0231\text{ min}^{-1}$. The half-life $t_{1/2}$ of the reaction is ______ minutes.

#### Question 27
An aqueous solution contains $18.0\text{ g}$ of glucose in $100\text{ g}$ of water. If $K_b = 0.52\text{ K}\cdot\text{kg/mol}$, the boiling point elevation $\Delta T_b$ is ______ $^\circ\text{C}$. (Round off to two decimal places)

#### Question 28
The coordination number of copper in $[\text{Cu}(\text{NH}_3)_4]^{2+}$ is ______ .

#### Question 29
A $0.050\text{ M}$ solution of barium hydroxide ($\text{Ba(OH)}_2$) is completely dissociated. The pOH of the solution is ______ .

#### Question 30
The standard cell potential of the cell $\text{Zn} \mid \text{Zn}^{2+} \parallel \text{Ag}^+ \mid \text{Ag}$ with $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.76\text{ V}$ and $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$ is ______ V. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the reaction between phenol and concentrated $\text{HNO}_3$ in the presence of concentrated $\text{H}_2\text{SO}_4$ is:  
(A) 2,4,6-Trinitrophenol (Picric acid)  
(B) o-Nitrophenol  
(C) p-Nitrophenol  
(D) Benzoic acid

#### Question 32
The molecular geometry of ammonia ($\text{NH}_3$) is:  
(A) Trigonal pyramidal  
(B) Tetrahedral  
(C) Trigonal planar  
(D) T-shaped

#### Question 33
In the extraction of iron, haematite is reduced in a blast furnace mainly by:  
(A) Carbon monoxide ($\text{CO}$)  
(B) Carbon dioxide ($\text{CO}_2$)  
(C) Hydrogen ($\text{H}_2$)  
(D) Limestone

#### Question 34
Which of the following compounds reduces Fehling's solution?  
(A) Acetaldehyde  
(B) Acetone  
(C) Benzaldehyde  
(D) Acetophenone

#### Question 35
Bakelite is a polymer of:  
(A) Phenol and Formaldehyde  
(B) Adipic acid and Hexamethylenediamine  
(C) Urea and Formaldehyde  
(D) Ethylene glycol and Terephthalic acid

#### Question 36
Rickets is caused by deficiency of:  
(A) Vitamin D  
(B) Vitamin A  
(C) Vitamin C  
(D) Vitamin B1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^3 - 6x^2 + 9x + 1$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f'(x) = 3(x - 1)(x - 3)$.  
(B) $f(x)$ has a local maximum at $x = 1$ with maximum value $5$.  
(C) $f(x)$ has a local minimum at $x = 3$ with minimum value $1$.  
(D) The point of inflection is $(2, 3)$.

#### Question 38
For the parabola $y^2 = 16x$:
(A) The focus is at $(4, 0)$.  
(B) The directrix has equation $x = -4$.  
(C) The length of its latus rectum is $16$.  
(D) The tangent at $(4, 8)$ has equation $x - y + 4 = 0$.

#### Question 39
For complex numbers $z$ satisfying $|z| = 1$:
(A) $\operatorname{Re}(z) \in [-1, 1]$.  
(B) $|z + 1| \le 2$.  
(C) $z \bar{z} = 1$.  
(D) $\frac{z - 1}{z + 1}$ is purely imaginary for $z \neq -1$.

#### Question 40
Let $A$ and $B$ be $n \times n$ invertible matrices:
(A) $(A B)^{-1} = B^{-1} A^{-1}$.  
(B) $\det(A B) = \det(A)\det(B)$.  
(C) $\operatorname{Tr}(A B) = \operatorname{Tr}(B A)$.  
(D) $(A B)^T = B^T A^T$.

#### Question 41
Let $I = \int_0^{\pi/2} \frac{\sin^2 x}{\sin^2 x + \cos^2 x} \, dx$. Then:
(A) $I = \int_0^{\pi/2} \sin^2 x \, dx$.  
(B) $I = \pi/4$.  
(C) $\int_0^{\pi/2} \cos^2 x \, dx = \pi/4$.  
(D) The sum of the two integrals is $\pi/2$.

#### Question 42
The plane $2x - 2y + z = 6$:
(A) Has normal vector $2\hat{i} - 2\hat{j} + \hat{k}$.  
(B) Has perpendicular distance from origin equal to $2$.  
(C) Intersects the $x$-axis at $(3, 0, 0)$.  
(D) Intersects the $z$-axis at $(0, 0, 6)$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by $y = x^2$ and $y = 4$ is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^1 x^3 \, dx$ is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real solutions to the equation $x^2 - 16 = 0$ is ______ .

#### Question 46
Let $\vec{a} = \hat{i} + 2\hat{j} + 2\hat{k}$. The length $|\vec{a}|$ is ______ .

#### Question 47
A card is drawn from a pack of 52 cards. The probability of getting a red card is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 48
The radius of the sphere $x^2 + y^2 + z^2 = 36$ is ______ .

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = \sin(2x)$ with respect to $x$ is:  
(A) $2\cos(2x)$  
(B) $\cos(2x)$  
(C) $-2\cos(2x)$  
(D) $2\sin(2x)$

#### Question 50
The slope of the line $3x - 4y = 12$ is:  
(A) $3/4$  
(B) $-3/4$  
(C) $4/3$  
(D) $-4/3$

#### Question 51
The value of $\lim_{x \to 0} \frac{\sin(4x)}{x}$ is:  
(A) $4$  
(B) $1$  
(C) $1/4$  
(D) $0$

#### Question 52
If $A$ is a square matrix of order 3 such that $\det(A) = 2$, then $\det(2A)$ is:  
(A) $16$  
(B) $8$  
(C) $4$  
(D) $32$

#### Question 53
The number of permutations of 5 distinct items taken all at a time is:  
(A) $120$  
(B) $24$  
(C) $60$  
(D) $720$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = 2x$ with $y(0) = 0$ is:  
(A) $y = x^2$  
(B) $y = x^2 + 1$  
(C) $y = 2x^2$  
(D) $y = x$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__IND_L__", ind_l).replace("__MAG_B__", mag_b).replace("__VOLT_V__", volt_v).replace("__ANG_W__", ang_w)
        p2 = raw_p2.replace("__PAD__", pad)

        raw_sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Madras Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Circular capacitor charging: displacement current density $J_d = I_0 / (\pi R^2)$. Magnetic field inside $B = \frac{\mu_0 I_0 r}{2\pi R^2}$. Poynting vector directed radially inward carries energy influx.
- Q2: (A, B, C, D) - Concentric spheres with two radial dielectric shells: $\vec{D} = \frac{Q}{4\pi r^2}\hat{r}$ is continuous. Bound surface charge at interface $q_b = Q(1/\kappa_2 - 1/\kappa_1)$. Capacitance in series.
- Q3: (A, B, C) - Time-varying magnetic field in circular zone: flux through square frame of side $2R$ covers entire circular area $\pi R^2$. Induced EMF $\mathcal{E} = B_0 \pi R^2 \omega \sin\omega t$. Net magnetic force is zero by symmetry.
- Q4: (A, B, C, D) - Charged non-conducting ring in switching field: induced electric field exerts torque $\tau = q a E = q a(\frac{a}{2}\frac{dB}{dt}) = \frac{1}{2}q a^2 \frac{dB}{dt}$. Final angular momentum $L = \frac{1}{2}q B_0 a^2 = I \omega = m a^2 \omega \implies \omega = \frac{q B_0}{2m}$.
- Q5: (A, B, C) - Lloyd's mirror: $\beta = \lambda D / (2d) = 500\text{ nm} \times 1.0 / (2 \times 1.0\text{ mm}) = 0.25\text{ mm}$. Contact line is dark fringe due to $\pi$ phase reflection.
- Q6: (A, B, C, D) - Radiation pressure: absorbing surface $I/c$, reflecting surface $2I/c$, general $(1+R)I/c$. Experimental verification by Nichols-Hull.
- Q7: 6.28 - Total current: $I = \int_0^a 2\pi r J(r) dr = 2\pi J_0 \int_0^a (r - r^2/a) dr = 2\pi J_0 [a^2/2 - a^2/3] = \frac{\pi J_0 a^2}{3} = \frac{3.14 \times (3.0 \times 10^6) \times (2.0 \times 10^{-3})^2}{3} = 3.14 \times 10^6 \times 4.0 \times 10^{-6} \approx 12.56\text{ A}$ (or calibrated).
- Q8: 200.00 - Polytropic work: $W = \frac{P_1 V_1 - P_2 V_2}{n - 1} = \frac{P_1 V_1 - P_1(V_1/V_2)^2 V_2}{2 - 1} = P_1 V_1(1 - V_1/V_2) = (4.0 \times 1.0 \times 100)(1 - 1/2) = 400 \times 0.5 = 200.00\text{ J}$.
- Q9: 0.25 - $I = \frac{1}{2}M R^2 = \frac{1}{2}(4.0)(0.0625) = 0.125\text{ kg}\cdot\text{m}^2$. Angular momentum $L = I \omega = 0.125 \times 20.0 = 2.50\text{ kg}\cdot\text{m}^2/\text{s}$.
- Q10: 408.25 - $\omega_0 = 1/\sqrt{LC} = 1/\sqrt{0.12 \times 50 \times 10^{-6}} = 1/\sqrt{6.0 \times 10^{-6}} = 1000/\sqrt{6} \approx 408.25\text{ rad/s}$.
- Q11: 445 - Loaded fork decreases from 440, so beat frequency increases to 8 means higher frequency is $440 + 5 = 445\text{ Hz}$.
- Q12: 1.60 - $\omega = 2\pi / T = 2(3.14) / 1.57 = 4.0\text{ rad/s}$. $a_{\max} = \omega^2 A = 16 \times 0.10 = 1.60\text{ m/s}^2$.
- Q13: (A) - Tension difference between bottom and top of vertical circle is always $6mg$.
- Q14: (A) - Field between oppositely charged conducting planes is $\sigma/\varepsilon_0$.
- Q15: (A) - Virtual erect image: $m = +3 = v/u \implies v = 3u$. $\frac{1}{3u} - \frac{1}{u} = \frac{1}{15} \implies -\frac{2}{3u} = \frac{1}{15} \implies u = -10\text{ cm}$.
- Q16: (A) - Adiabatic relation $T V^{\gamma-1} = \text{const}$.
- Q17: (A) - $B = \frac{\mu_0 I}{2\pi r} = \frac{4\pi \times 10^{-7} \times 5.0}{2\pi \times 0.10} = 1.0 \times 10^{-5}\text{ T}$.
- Q18: (A) - 60 days is 2 half-lives $\implies$ fraction remaining is $1/4 \implies$ fraction decaying is $3/4$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C) - Complexometric EDTA titration: $\text{Mg(OH)}_2$ precipitates at $\text{pH} \approx 12$ allowing calcium titration. At $\text{pH} \approx 10$ both form stable chelates with wine-red to blue EBT transition. Conditional constant increases with increasing pH.
- Q20: (A, B, C) - Octahedral $[\text{Ni}(\text{H}_2\text{O})_6]^{2+}$ is $d^8$ ($t_{2g}^6 e_g^2$) with 2 unpaired electrons, $\mu = 2.83\text{ BM}$, $\text{CFSE} = 6(-0.4) + 2(0.6) = -1.2\Delta_o$.
- Q21: (A, B, C, D) - Toluene chlorination gives benzal chloride, hydrolysis gives benzaldehyde, Cannizzaro gives sodium benzoate and benzyl alcohol.
- Q22: (A, B, C, D) - Metallurgical refining principles: zone refining (semiconductors), cyanide displacement (gold), Hall-Héroult cryolite (aluminium), electrorefining (copper).
- Q23: (A, B, C) - Glucose, fructose, maltose are reducing sugars; sucrose is non-reducing.
- Q24: (A, B, C, D) - Group 16 elements: oxygen covalency limit, $\text{SF}_6$ steric inertness, bent ozone, $\text{H}_2\text{S}$ acidity.
- Q25: 1.34 - Solubility $s = \sqrt{K_{sp}} = \sqrt{1.8 \times 10^{-10}} \approx 1.34 \times 10^{-5}\text{ mol/L} \implies X = 1.34$.
- Q26: 15.0 - $t_{1/2} = \frac{0.693}{0.0462} = 15.0\text{ min}$.
- Q27: 0.26 - Molality $m = \frac{6.0/60}{0.200} = 0.50\text{ m} \implies \Delta T_b = 0.52 \times 0.50 = 0.26^\circ\text{C}$.
- Q28: 6 - Oxalate is bidentate $\implies 3 \times 2 = 6$.
- Q29: 1.30 - $[\text{H}^+] = 0.050\text{ M} \implies \text{pH} = -\log_{10}(0.050) = 2 - 0.699 = 1.30$.
- Q30: -212.30 - $\Delta G^\circ = -n F E^\circ = -2(96500)(1.10) = -212.30\text{ kJ/mol}$.
- Q31: (A) - Reimer-Tiemann gives salicylaldehyde.
- Q32: (A) - $\text{XeF}_4$ has 4 bond pairs and 2 lone pairs $\implies$ square planar.
- Q33: (A) - Silica flux removes $\text{FeO}$ as $\text{FeSiO}_3$ slag.
- Q34: (A) - Reducing sugars like glucose reduce Tollens' reagent.
- Q35: (A) - Nylon-6 is polymerized caprolactam.
- Q36: (A) - Vitamin C deficiency causes scurvy.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Taylor expansion inequality: $\arctan x > x - x^3/3$ for $x > 0$.
- Q38: (A, B, C, D) - Parabola $y^2 = 8x$: focus $(2, 0)$, directrix $x = -2$, latus rectum $8$, normal $x + y = 6$.
- Q39: (A, B, C, D) - Ellipse with foci $(\pm 3, 0)$ and $2a = 10 \implies a = 5, c = 3 \implies b = 4$.
- Q40: (A, B, C, D) - Distinct eigenvalues 1, 2, 4: determinant is product $= 8$, trace is sum $= 7$, invertible, diagonalizable.
- Q41: (A, B, C, D) - Beta-gamma definite integral: $\int_0^1 \frac{dx}{\sqrt{1-x^2}} = [\arcsin x]_0^1 = \pi/2$.
- Q42: (A, B, C, D) - Plane $x + 2y + 2z = 9$: distance from origin is $9 / \sqrt{1 + 4 + 4} = 9/3 = 3$.
- Q43: 10.67 - Area between $y = 4 - x^2$ and $x$-axis from $x = -2$ to $2$ is $32/3 \approx 10.67$.
- Q44: 20 - $\int_0^1 (x^3 - x^4)dx = 1/4 - 1/5 = 1/20 \implies K = 20$.
- Q45: 3 - $x(x^2 - 4) = 0 \implies x = 0, \pm 2$ (three real roots).
- Q46: 7.00 - $|\vec{a}| = \sqrt{4 + 9 + 36} = 7.00$.
- Q47: 13 - Probability of Ace is $4/52 = 1/13 \implies K = 13$.
- Q48: 3.61 - Center $(2, 3)$, radius $R = \sqrt{4 + 9} = \sqrt{13} \approx 3.61$.
- Q49: (A) - $\frac{d}{dx}\ln(x^2 + 1) = \frac{2x}{x^2 + 1}$.
- Q50: (A) - $2y y' = 4 \implies y' = 2/y = 2/2 = 1$.
- Q51: (A) - Standard limit $\lim_{x\to 0}\frac{e^x - 1}{x} = 1$.
- Q52: (A) - $\det(3A) = 3^3 \det(A) = 27 \times 3 = 81$.
- Q53: (A) - $4! = 24$.
- Q54: (A) - $y' = 3x^2 \implies y = x^3 + C$. $y(0) = 1 \implies y = x^3 + 1$.
"""

        raw_sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Madras Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Rectangular thermodynamic cycle: work done is area $\frac{1}{2}P_0 V_0$. Internal energy returns to initial value over closed cycle.
- Q2: (A, B, C, D) - Concentric shells with outer grounded: $V_2 = 0$, induced outer charge $-Q_1$, electric field outside vanishes.
- Q3: (A, B, C, D) - Solid sphere rolling down $30^\circ$ incline: $a = \frac{5}{14}g$, $\mu_{\min} = \frac{2}{7\sqrt{3}}$, rotational KE fraction $2/7$.
- Q4: (A, B, C, D) - Solenoid time-varying field: induced electric field is circular non-conservative with non-zero line integral.
- Q5: (A, B, C, D) - Interference basics: constructive and destructive conditions, fringe width $\beta = \lambda D / d$, cosine-squared intensity.
- Q6: (A, B, C, D) - Photoelectric effect: linear frequency dependence of $K_{\max}$, intensity independence of stopping potential, instantaneous emission.
- Q7: 24.80 - Cut-off wavelength $\lambda_{\min} = \frac{1240\text{ eV}\cdot\text{nm}}{50000\text{ eV}} = 0.0248\text{ nm} = 24.80\text{ pm}$.
- Q8: 1247.10 - Adiabatic work $W = -n C_V \Delta T = -(1)(\frac{3}{2}R)(300 - 400) = \frac{3}{2}(8.314)(100) = 1247.10\text{ J}$.
- Q9: 0.24 - $I = \frac{2}{5}M R^2 = \frac{2}{5}(2.0)(0.04) = 0.032\text{ kg}\cdot\text{m}^2$. $L = I \omega = 0.032 \times 15.0 = 0.48\text{ kg}\cdot\text{m}^2/\text{s}$.
- Q10: 400.00 - At resonance $P = V_{rms}^2 / R = 40000 / 100 = 400.00\text{ W}$.
- Q11: 508 - Lower frequency is $512 - 4 = 508\text{ Hz}$.
- Q12: 1.81 - $T = 2\pi\sqrt{0.81 / 9.80} \approx 2(3.14)(0.287) \approx 1.81\text{ s}$.
- Q13: (A) - Close orbital speed $v = \sqrt{g R_E} \approx 7.9\text{ km/s}$.
- Q14: (A) - Opposite field vectors from identical charges cancel at midpoint $\implies E = 0$.
- Q15: (A) - Real image of same size at center of curvature ($2f = 40\text{ cm}$).
- Q16: (A) - In adiabatic expansion, work is done at the expense of internal energy, so gas cools down.
- Q17: (A) - Velocity perpendicular to uniform magnetic field gives circular path.
- Q18: (A) - 24 days is 3 half-lives $\implies (1/2)^3 = 1/8$ remaining.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Ideal solution thermodynamics: $\Delta H_{\text{mix}} = 0, \Delta V_{\text{mix}} = 0, \Delta S_{\text{mix}} > 0, \Delta G_{\text{mix}} < 0$.
- Q20: (A, B, C, D) - $[\text{Fe(CN)}_6]^{4-}$ is $d^6$ low-spin ($t_{2g}^6 e_g^0$) diamagnetic ($d^2sp^3$).
- Q21: (A, B, C) - Formaldehyde, benzaldehyde, pivaldehyde lack $\alpha$-hydrogens and undergo Cannizzaro reaction. Acetaldehyde undergoes aldol.
- Q22: (A, B, C, D) - Aluminium metallurgy: Bayer's process, Hall-Héroult molten cryolite, carbon anode consumption into $\text{CO}_2$.
- Q23: (A, B, C) - Glucose, fructose, maltose are reducing; sucrose is non-reducing.
- Q24: (A, B, C, D) - Group 16 elements: oxygen covalency 4, crown $\text{S}_8$, octahedral $\text{SF}_6$, ozone oxidizes $\text{KI}$ to $\text{I}_2$.
- Q25: 1.26 - $s = \sqrt{K_{sp}} = \sqrt{1.6 \times 10^{-8}} \approx 1.26 \times 10^{-4}\text{ M} \implies X = 1.26$.
- Q26: 30.0 - $t_{1/2} = \frac{0.693}{0.0231} = 30.0\text{ min}$.
- Q27: 0.52 - Molality $m = \frac{18.0/180}{0.100} = 1.00\text{ m} \implies \Delta T_b = 0.52 \times 1.00 = 0.52^\circ\text{C}$.
- Q28: 4 - Four ammine ligands.
- Q29: 1.00 - $[\text{OH}^-] = 2(0.050) = 0.10\text{ M} \implies \text{pOH} = 1.00$.
- Q30: 1.56 - $E^\circ = +0.80 - (-0.76) = 1.56\text{ V}$.
- Q31: (A) - Concentrated nitration of phenol produces picric acid (2,4,6-trinitrophenol).
- Q32: (A) - Ammonia has 3 bond pairs and 1 lone pair $\implies$ trigonal pyramidal.
- Q33: (A) - Carbon monoxide reduces iron oxide in blast furnace.
- Q34: (A) - Acetaldehyde reduces Fehling's solution.
- Q35: (A) - Bakelite is phenol-formaldehyde resin.
- Q36: (A) - Vitamin D deficiency causes rickets.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Cubic polynomial $f(x) = x^3 - 6x^2 + 9x + 1$: $f'(x) = 3(x-1)(x-3)$. Maximum at $x=1$ ($y=5$), minimum at $x=3$ ($y=1$), inflection at $(2, 3)$.
- Q38: (A, B, C, D) - Parabola $y^2 = 16x$: focus $(4, 0)$, directrix $x = -4$, latus rectum $16$, tangent $x - y + 4 = 0$.
- Q39: (A, B, C, D) - Unit circle $|z| = 1$: real part in $[-1, 1]$, $|z+1| \le 2$, $z\bar{z} = 1$, $\frac{z-1}{z+1}$ is imaginary.
- Q40: (A, B, C, D) - Standard matrix algebra properties.
- Q41: (A, B, C, D) - $\int_0^{\pi/2}\frac{\sin^2 x}{1}dx = \pi/4$.
- Q42: (A, B, C, D) - Plane $2x - 2y + z = 6$: distance from origin $6/3 = 2$, intercepts $(3, 0, 0)$ and $(0, 0, 6)$.
- Q43: 10.67 - Area between $y = x^2$ and $y = 4$ is $\int_{-2}^2 (4 - x^2)dx = 32/3 \approx 10.67$.
- Q44: 4 - $\int_0^1 x^3 dx = 1/4 \implies K = 4$.
- Q45: 2 - $x^2 - 16 = 0 \implies x = \pm 4$ (two real roots).
- Q46: 3.00 - $|\vec{a}| = \sqrt{1 + 4 + 4} = 3.00$.
- Q47: 2 - Red cards probability is $26/52 = 1/2 \implies K = 2$.
- Q48: 6.00 - Radius of sphere $x^2 + y^2 + z^2 = 36$ is $6.00$.
- Q49: (A) - $\frac{d}{dx}\sin(2x) = 2\cos(2x)$.
- Q50: (A) - $4y = 3x - 12 \implies y = \frac{3}{4}x - 3 \implies$ slope is $3/4$.
- Q51: (A) - $\lim_{x\to 0}\frac{\sin(4x)}{x} = 4$.
- Q52: (A) - $\det(2A) = 2^3 \det(A) = 8 \times 2 = 16$.
- Q53: (A) - $5! = 120$.
- Q54: (A) - $y' = 2x \implies y = x^2 + C$. $y(0) = 0 \implies y = x^2$.
"""

        raw_val = r"""# Answer Key & Benchmark Alignment – Mock Examination __PAD__
## Organising Institute Style: IIT Madras (`IIT_MADRAS_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C; Q4: A,B,C,D; Q5: A,B,C; Q6: A,B,C,D; Q7: 12.56; Q8: 200.00; Q9: 2.50; Q10: 408.25; Q11: 445; Q12: 1.60; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C; Q20: A,B,C; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C; Q24: A,B,C,D; Q25: 1.34; Q26: 15.0; Q27: 0.26; Q28: 6; Q29: 1.30; Q30: -212.30; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 10.67; Q44: 20; Q45: 3; Q46: 7.00; Q47: 13; Q48: 3.61; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 24.80; Q8: 1247.10; Q9: 0.48; Q10: 400.00; Q11: 508; Q12: 1.81; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C; Q22: A,B,C,D; Q23: A,B,C; Q24: A,B,C,D; Q25: 1.26; Q26: 30.0; Q27: 0.52; Q28: 4; Q29: 1.00; Q30: 1.56; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 10.67; Q44: 4; Q45: 2; Q46: 3.00; Q47: 2; Q48: 6.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""

        sol1 = raw_sol1.replace("__PAD__", pad).replace("__IND_L__", ind_l).replace("__MAG_B__", mag_b).replace("__VOLT_V__", volt_v).replace("__ANG_W__", ang_w)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Madras")
        print(f"Generated IIT Madras Mock {pad}!")

if __name__ == "__main__":
    generate_madras_01_to_05()

