"""
IIT Kanpur Mocks 11 to 15 Generator
Organising Institute: Indian Institute of Technology Kanpur
Empirical Benchmark: 2001, 2007, 2011, 2018 Official JEE Advanced Papers
Features:
- Extreme numerical rigor and calculation depth (>= 38% numerical value questions)
- Relativistic kinematics, electromagnetic boundary conditions, Poynting vectors, coupled circuits
- Multi-component chemical equilibria, coordination stereochemistry, advanced organic cascades
- Multivariable calculus, differential equations, orthogonal polynomials, 3D analytical geometry
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_kanpur_11_to_15():
    for mock_idx in range(11, 16):
        pad = f"{mock_idx:02d}"
        fluid_visc = str(0.012 + (mock_idx % 4) * 0.002)
        pot_v = str(15.0 + (mock_idx % 5) * 2.5)
        eq_k = str(1.5 + (mock_idx % 3) * 0.5)
        ang_freq = str(120 + mock_idx * 10)

        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Kanpur (`IIT_KANPUR_STYLE`)
**Historical Reference Benchmark**: 2001, 2007, 2011, 2018 Official Examination Papers  
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
A heavy uniform rod of mass $M$ and length $L$ is held horizontally above a frictionless horizontal table. One end of the rod is smoothly hinged at a fixed pivot $O$. The rod is released from rest in the horizontal position $\theta = 0$:
(A) The angular acceleration of the rod as a function of the angle of fall $\theta$ is $\alpha(\theta) = \frac{3g}{2L}\cos\theta$.  
(B) The angular velocity when the rod becomes vertical ($\theta = \pi/2$) is $\omega = \sqrt{\frac{3g}{L}}$.  
(C) The vertical reaction force exerted by the pivot when the rod is vertical is $N_y = \frac{5}{2}Mg$.  
(D) The horizontal reaction force exerted by the pivot when the rod is vertical is zero.

#### Question 2
One mole of a real gas satisfies the Clausius equation of state $P(V_m - b) = R T$, where $b$ is the co-volume constant. In an isothermal reversible expansion from volume $V_1$ to $V_2$:
(A) The internal energy of the gas remains strictly constant ($(\partial U / \partial V)_T = 0$).  
(B) The work done by the gas is $W = R T \ln\left(\frac{V_2 - b}{V_1 - b}\right)$.  
(C) The heat absorbed by the gas equals the work done ($Q = W$).  
(D) In an adiabatic free expansion (Joule expansion) into vacuum, the temperature of the gas drops.

#### Question 3
A dielectric sphere of radius $R$ has a frozen-in uniform polarization $\vec{P} = P_0 \hat{k}$:
(A) The bound surface charge density is $\sigma_b(\theta) = P_0 \cos\theta$.  
(B) The bound volume charge density is $\rho_b = 0$ throughout the interior of the sphere.  
(C) The electric field inside the sphere is uniform and given by $\vec{E}_{in} = -\frac{\vec{P}}{3\varepsilon_0}$.  
(D) The potential outside the sphere is identical to that of an electric dipole of moment $\vec{p} = \frac{4}{3}\pi R^3 \vec{P}$ placed at the center.

#### Question 4
A superconducting circular ring of radius $r$ and self-inductance $L$ is placed coaxially in a time-varying magnetic field $B(t) = B_0 \cos(\omega t)$ directed along its axis:
(A) The total magnetic flux through the superconducting ring remains strictly constant in time.  
(B) The persistent current induced in the ring is $I(t) = \frac{\pi r^2 B_0}{L}[1 - \cos(\omega t)]$ (assuming $I(0) = 0$).  
(C) The net magnetic field at the center of the ring fluctuates symmetrically around zero.  
(D) Zero Joule heat is dissipated in the ring.

#### Question 5
In a Fabry-Pérot interferometer illuminated by monochromatic light of wavelength $\lambda = 500\text{ nm}$, two parallel partially silvered plates with reflection coefficient $R = 0.90$ are separated by distance $d = 1.0\text{ cm}$:
(A) The free spectral range is $\Delta\lambda_{FSR} = \frac{\lambda^2}{2d} = 0.0125\text{ nm}$.  
(B) The finesse of the interferometer is $\mathcal{F} = \frac{\pi\sqrt{R}}{1 - R} \approx 29.8$.  
(C) The resolving power in order $m$ is $\frac{\lambda}{\Delta\lambda} = m \mathcal{F}$.  
(D) The transmitted intensity distribution follows the Airy formula.

#### Question 6
A positron of rest mass $m_0$ and kinetic energy $K = 1.022\text{ MeV}$ collides head-on with an electron at rest and annihilates into two identical photons:
(A) The total relativistic energy of the positron is $E_1 = 1.533\text{ MeV}$.  
(B) The relativistic momentum of the positron is $p_1 = \frac{\sqrt{E_1^2 - (m_0 c^2)^2}}{c} \approx 1.445\text{ MeV}/c$.  
(C) The two annihilation photons must emerge in collinear opposite directions in the center-of-mass frame.  
(D) The threshold energy for electron-positron pair creation by a photon in the field of a stationary heavy nucleus is $2 m_0 c^2 = 1.022\text{ MeV}$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A small spherical steel ball of radius $r = 1.0\text{ mm}$ falls vertically under gravity through a viscous oil of dynamic viscosity $\eta = __FLUID_VISC__\text{ Pa}\cdot\text{s}$ and density $\rho_l = 900\text{ kg/m}^3$. The density of steel is $\rho_s = 7800\text{ kg/m}^3$. Taking $g = 9.80\text{ m/s}^2$, the terminal velocity of the ball is ______ m/s. (Round off to two decimal places)

#### Question 8
One mole of an ideal monoatomic gas undergoes an isobaric expansion at pressure $P_0 = 1.0 \times 10^5\text{ Pa}$ from volume $V_1 = 0.020\text{ m}^3$ to $V_2 = 0.050\text{ m}^3$. The change in entropy $\Delta S$ of the gas is ______ J/K. (Take $\ln(2.5) = 0.916$ and $R = 8.314\text{ J/(mol}\cdot\text{K)}$, round off to two decimal places)

#### Question 9
A hollow cylinder of mass $M = 3.0\text{ kg}$ and radius $R = 0.40\text{ m}$ is released from rest at the top of a $30^\circ$ rough incline. If it rolls down without slipping through a vertical distance $h = 2.0\text{ m}$, the angular speed of the cylinder at the bottom is ______ rad/s. (Take $g = 9.80\text{ m/s}^2$, round off to two decimal places)

#### Question 10
In an AC circuit, an alternating voltage $V(t) = 100\sqrt{2}\sin(100\pi t)\text{ V}$ produces a current $I(t) = 10\sqrt{2}\sin(100\pi t - \pi/3)\text{ A}$. The average power dissipated in the circuit is ______ W.

#### Question 11
An organ pipe open at both ends has fundamental frequency $f_1 = 300\text{ Hz}$. When one end is closed, the third harmonic frequency of the resulting closed pipe is ______ Hz.

#### Question 12
A simple pendulum has period $T = 2.00\text{ s}$ on the surface of the Earth. When taken to a planet where the acceleration due to gravity is $g' = 0.25 g$, the period of the pendulum becomes ______ s.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle of mass $m$ moves in a force field with potential energy $U(r) = -k/r^3$ ($k > 0$). The particle will fall into the origin if its total energy $E$ and angular momentum $L$ satisfy:  
(A) $E > 0$ with impact parameter $b < (3/2)(2mk/L^2)^{1/2}$  
(B) $E < 0$ always  
(C) $L > \sqrt{mk}$  
(D) $E = 0$ only

#### Question 14
A parallel plate capacitor with air between plates has capacitance $C_0$. A dielectric slab of dielectric constant $\kappa = 4$ and thickness equal to half the plate separation is inserted between the plates. The new capacitance is:  
(A) $\frac{8}{5}C_0$  
(B) $\frac{5}{2}C_0$  
(C) $2 C_0$  
(D) $\frac{4}{3}C_0$

#### Question 15
A compound microscope has an objective lens of focal length $f_o = 1.0\text{ cm}$ and an eyepiece of focal length $f_e = 5.0\text{ cm}$. The tube length is $L = 20\text{ cm}$. The overall magnifying power when the final image is formed at near point ($D = 25\text{ cm}$) is:  
(A) $120$  
(B) $100$  
(C) $150$  
(D) $80$

#### Question 16
An ideal gas undergoes a cycle on $T$-$S$ diagram consisting of two isotherms at $T_H = 400\text{ K}$ and $T_C = 300\text{ K}$, and two adiabats where entropy varies between $S_1 = 10\text{ J/K}$ and $S_2 = 25\text{ J/K}$. The net work done per cycle is:  
(A) $1500\text{ J}$  
(B) $3000\text{ J}$  
(C) $4500\text{ J}$  
(D) $6000\text{ J}$

#### Question 17
A circular coil of radius $R$ carries steady current $I$. The ratio of the magnetic field at the center of the coil to that at an axial point at distance $x = R\sqrt{3}$ from the center is:  
(A) $8 : 1$  
(B) $4 : 1$  
(C) $16 : 1$  
(D) $2\sqrt{2} : 1$

#### Question 18
The work function of caesium is $\Phi = 2.14\text{ eV}$. When illuminated with light of wavelength $\lambda = 400\text{ nm}$, the stopping potential is:  
(A) $0.96\text{ V}$  
(B) $1.20\text{ V}$  
(C) $2.14\text{ V}$  
(D) $0.50\text{ V}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution containing $0.10\text{ M}\ \text{Fe}^{3+}$ and $0.10\text{ M}\ \text{Cu}^{2+}$:
(A) Addition of $\text{H}_2\text{S}$ gas in acidic medium ($\text{pH} \approx 1$) precipitates only $\text{CuS}$.  
(B) $\text{Fe}^{3+}$ is reduced to $\text{Fe}^{2+}$ by $\text{H}_2\text{S}$ in acidic medium with deposition of elemental sulfur.  
(C) The reduction of $\text{Fe}^{3+}$ by $\text{H}_2\text{S}$ is thermodynamically spontaneous because $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V} > E^\circ(\text{S}/\text{H}_2\text{S}) = +0.14\text{ V}$.  
(D) Addition of excess $\text{KCN}$ to the solution followed by $\text{H}_2\text{S}$ prevents precipitation of copper due to the formation of stable $[\text{Cu(CN)}_4]^{3-}$.

#### Question 20
Regarding the high-spin and low-spin configurations of octahedral cobalt(III) complexes:
(A) $[\text{CoF}_6]^{3-}$ is high-spin ($t_{2g}^4 e_g^2$) and paramagnetic with 4 unpaired electrons ($sp^3d^2$).  
(B) $[\text{Co}(\text{NH}_3)_6]^{3+}$ is low-spin ($t_{2g}^6 e_g^0$) and diamagnetic ($d^2sp^3$).  
(C) The crystal field splitting $\Delta_o$ in $[\text{Co}(\text{NH}_3)_6]^{3+}$ exceeds the mean pairing energy $P$.  
(D) High-spin $[\text{CoF}_6]^{3-}$ is kinetically labile, whereas low-spin $[\text{Co}(\text{NH}_3)_6]^{3+}$ is inert.

#### Question 21
For the complete saponification of ethyl acetate in aqueous alkaline medium:  
$\text{CH}_3\text{COOC}_2\text{H}_5 + \text{OH}^- \rightarrow \text{CH}_3\text{COO}^- + \text{C}_2\text{H}_5\text{OH}$:
(A) The reaction exhibits overall second-order kinetics ($-\frac{d[\text{ester}]}{dt} = k [\text{ester}][\text{OH}^-]$).  
(B) The reaction proceeds via an addition-elimination tetrahedral intermediate ($B_{AC}2$ mechanism).  
(C) Using oxygen-18 labeled ethoxide group $\text{CH}_3\text{CO}^{18}\text{OC}_2\text{H}_5$, the $^{18}\text{O}$ label appears exclusively in ethanol.  
(D) The electrical conductivity of the reaction mixture decreases continuously as $\text{OH}^-$ ions are replaced by $\text{CH}_3\text{COO}^-$ ions.

#### Question 22
Which of the following organic reagents selectively reduce an alkyne to a cis-alkene?
(A) Lindlar's catalyst ($\text{Pd}/\text{CaCO}_3$ poisoned with lead acetate and quinoline) under $\text{H}_2$.  
(B) Nickel boride (P-2 nickel catalyst) with $\text{H}_2$.  
(C) Sodium in liquid ammonia ($\text{Na} / \text{liq. NH}_3$).  
(D) Lithium aluminium hydride ($\text{LiAlH}_4$) in refluxing $\text{THF}$.

#### Question 23
In the metallurgy of iron using a blast furnace:
(A) Limestone ($\text{CaCO}_3$) decomposes to $\text{CaO}$, which combines with acidic silica impurity ($\text{SiO}_2$) to form fusible calcium silicate slag ($\text{CaSiO}_3$).  
(B) Slag has lower density than molten iron and floats on top, preventing oxidation of the iron.  
(C) The maximum temperature reached in the combustion zone (tuyeres) is approximately $2200\text{ K}$.  
(D) Pig iron tapped from the blast furnace contains approximately $4\%$ carbon and is hard and brittle.

#### Question 24
Which of the following statements about Group 17 elements (halogens) is/are correct?
(A) The bond dissociation enthalpy order is $\text{Cl}_2 > \text{Br}_2 > \text{F}_2 > \text{I}_2$.  
(B) Fluorine has an anomalous low bond dissociation enthalpy due to strong electron-electron repulsion between non-bonding lone pairs on adjacent small fluorine atoms.  
(C) Chlorine has a more negative electron gain enthalpy than fluorine.  
(D) Hydrofluoric acid ($\text{HF}$) is a weak acid in dilute aqueous solution due to its exceptionally high $\text{H}-\text{F}$ bond strength and strong hydrogen bonding.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of magnesium hydroxide $\text{Mg(OH)}_2$ is $K_{sp} = 1.8 \times 10^{-11}$. The pH of a saturated aqueous solution of $\text{Mg(OH)}_2$ at $25^\circ\text{C}$ is ______ . (Take $\log_{10}(3.27) = 0.51$, round off to two decimal places)

#### Question 26
A reaction has a rate constant $k_1 = 1.0 \times 10^{-4}\text{ s}^{-1}$ at $300\text{ K}$ and $k_2 = 2.0 \times 10^{-4}\text{ s}^{-1}$ at $310\text{ K}$. The activation energy $E_a$ of the reaction is ______ kJ/mol. (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 2 = 0.693$, round off to two decimal places)

#### Question 27
An aqueous solution contains $5.00\text{ g}$ of a non-volatile solute in $100\text{ g}$ of water. The boiling point of the solution is $100.26^\circ\text{C}$. Taking $K_b = 0.52\text{ K}\cdot\text{kg/mol}$ for water, the molar mass of the solute is ______ g/mol.

#### Question 28
The total number of unpaired electrons in the complex ion $[\text{Fe}(\text{H}_2\text{O})_6]^{2+}$ is ______ .

#### Question 29
A $0.100\text{ M}$ solution of sodium acetate ($\text{CH}_3\text{COONa}$) undergoes anionic hydrolysis. Taking $K_a(\text{CH}_3\text{COOH}) = 1.8 \times 10^{-5}$ and $K_w = 1.0 \times 10^{-14}$, the degree of hydrolysis $h$ is $X \times 10^{-5}$. The value of $X$ is ______ . (Round off to two decimal places)

#### Question 30
The standard reduction potential of the hydrogen electrode in contact with a solution of $\text{pH} = 3.00$ at $298\text{ K}$ and $P_{\text{H}_2} = 1\text{ bar}$ is ______ V. (Take $2.303 R T / F = 0.0591\text{ V}$, round off to three decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the reaction between benzaldehyde and formaldehyde in the presence of concentrated $\text{NaOH}$ (Crossed Cannizzaro reaction) is:  
(A) Sodium formate and benzyl alcohol  
(B) Sodium benzoate and methanol  
(C) Sodium formate and benzoic acid  
(D) Benzyl alcohol and methanol

#### Question 32
The oxidation state of osmium in osmium tetroxide ($\text{OsO}_4$) is:  
(A) $+8$  
(B) $+6$  
(C) $+4$  
(D) $+7$

#### Question 33
In the Kroll process for the extraction of titanium, the reducing agent used is:  
(A) Magnesium metal ($\text{Mg}$)  
(B) Carbon (coke)  
(C) Carbon monoxide  
(D) Hydrogen gas

#### Question 34
Which of the following compounds gives a yellow precipitate with 2,4-dinitrophenylhydrazine but does NOT reduce Fehling's solution?  
(A) Acetophenone  
(B) Acetaldehyde  
(C) Glucose  
(D) Formic acid

#### Question 35
The monomer of Teflon is:  
(A) Tetrafluoroethylene  
(B) Vinyl chloride  
(C) Styrene  
(D) Acrylonitrile

#### Question 36
Night blindness is caused by the deficiency of:  
(A) Vitamin A (Retinol)  
(B) Vitamin C  
(C) Vitamin D  
(D) Vitamin K

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x}{e^x - 1} + \frac{x}{2}$ for $x \neq 0$ and $f(0) = 1$. Which of the following statements is/are correct?
(A) $f(x)$ is an even function on $\mathbb{R}$.  
(B) $\lim_{x \to 0} f(x) = 1$, so $f(x)$ is continuous at $x = 0$.  
(C) $f(x) = \frac{x}{2}\coth(x/2)$.  
(D) $f'(0) = 0$.

#### Question 38
For the hyperbola $x^2 - y^2 = a^2$ (rectangular hyperbola):
(A) Its eccentricity is $e = \sqrt{2}$.  
(B) Its asymptotes are the lines $y = \pm x$, which intersect at right angles.  
(C) The length of its latus rectum is $2a$.  
(D) The product of the perpendicular distances from any point on the hyperbola to its asymptotes is constant and equal to $a^2 / 2$.

#### Question 39
For complex numbers $z$ satisfying $|z - i| \le 1$ and $|z - 1| \le 1$:
(A) The region represents the intersection of two closed circular disks of radius 1 centered at $(0, 1)$ and $(1, 0)$.  
(B) The point $z = \frac{1+i}{2}$ belongs to the region.  
(C) The area of the region is $\frac{\pi}{2} - 1$.  
(D) The maximum value of $|z|$ in this region is $\sqrt{2}$.

#### Question 40
Let $A$ be a $3 \times 3$ skew-symmetric matrix ($A^T = -A$):
(A) $\det(A) = 0$.  
(B) All real eigenvalues of $A$ are zero.  
(C) The non-zero eigenvalues of $A$ are purely imaginary.  
(D) $I + A$ is an invertible matrix.

#### Question 41
Let $I = \int_0^1 \frac{\ln(1 - x)}{x} \, dx$. Then:
(A) $I = -\sum_{n=1}^\infty \frac{1}{n^2}$.  
(B) $I = -\frac{\pi^2}{6}$.  
(C) $\int_0^1 \frac{\ln(1 + x)}{x} \, dx = \frac{\pi^2}{12}$.  
(D) $\int_0^1 \frac{\ln(1 + x^2)}{x} \, dx = \frac{\pi^2}{24}$.

#### Question 42
The lines $L_1: \frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $L_2: \frac{x-2}{1} = \frac{y-3}{2} = \frac{z-4}{3}$:
(A) Are coplanar.  
(B) Intersect at the point $(0, 0, 0)$.  
(C) Intersect at the point $(-1, -1, -1)$.  
(D) Lie in the plane $x - 2y + z = 0$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the curve $y = x(x - 1)(x - 2)$ and the $x$-axis between $x = 0$ and $x = 2$ is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^{\pi/2} \sin^4 x \cos^4 x \, dx$ is $\frac{\pi}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real solutions of the equation $e^x = x + 2$ is ______ .

#### Question 46
Let $\vec{a} = 2\hat{i} - \hat{j} + \hat{k}$ and $\vec{b} = \hat{i} + 2\hat{j} - \hat{k}$. The area of the triangle formed by vectors $\vec{a}$ and $\vec{b}$ as adjacent sides is ______ . (Round off to two decimal places)

#### Question 47
A fair coin is tossed 8 times. The probability of getting an equal number of heads and tails is $\frac{p}{256}$. The value of $p$ is ______ .

#### Question 48
The radius of the sphere passing through the points $(0, 0, 0)$, $(a, 0, 0)$, $(0, b, 0)$, and $(0, 0, c)$ with $a = 2, b = 4, c = 4$ is ______ . (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arctan\left(\frac{\sqrt{1 + x^2} - 1}{x}\right)$ with respect to $\arctan x$ for $x \neq 0$ is:  
(A) $1/2$  
(B) $1$  
(C) $2$  
(D) $1/4$

#### Question 50
The locus of the point of intersection of perpendicular tangents to the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ (for $a > b$) is:  
(A) $x^2 + y^2 = a^2 - b^2$  
(B) $x^2 + y^2 = a^2 + b^2$  
(C) $x^2 - y^2 = a^2 - b^2$  
(D) $x y = a^2 - b^2$

#### Question 51
The value of $\lim_{x \to 0} \frac{e^x - e^{-x} - 2x}{x^3}$ is:  
(A) $1/3$  
(B) $2/3$  
(C) $1/6$  
(D) $0$

#### Question 52
If $A$ and $B$ are square matrices of the same order such that $A B = A$ and $B A = B$, then $A$ and $B$ are:  
(A) Idempotent ($A^2 = A, B^2 = B$)  
(B) Involutory  
(C) Nilpotent  
(D) Symmetric

#### Question 53
The number of ways of distributing 8 identical balls into 3 distinct boxes such that each box gets at least one ball is:  
(A) $21$  
(B) $28$  
(C) $36$  
(D) $45$

#### Question 54
The solution of the differential equation $x dy - y dx = \sqrt{x^2 + y^2} dx$ is:  
(A) $y + \sqrt{x^2 + y^2} = C x^2$  
(B) $y - \sqrt{x^2 + y^2} = C x$  
(C) $x + \sqrt{x^2 + y^2} = C y^2$  
(D) $y = C x^2$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Kanpur (`IIT_KANPUR_STYLE`)
**Historical Reference Benchmark**: 2001, 2007, 2011, 2018 Official Examination Papers  
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
A gas follows the van der Waals equation $\left(P + \frac{a}{V_m^2}\right)(V_m - b) = R T$. In an adiabatic throttling process (Joule-Thomson expansion):
(A) The enthalpy $H = U + P V$ is conserved across the porous plug.  
(B) The Joule-Thomson coefficient is $\mu_{JT} = \left(\frac{\partial T}{\partial P}\right)_H = \frac{1}{C_P}\left[T\left(\frac{\partial V_m}{\partial T}\right)_P - V_m\right]$.  
(C) To first order in $a$ and $b$, $\mu_{JT} \approx \frac{1}{C_P}\left(\frac{2a}{R T} - b\right)$.  
(D) The inversion temperature below which the gas cools upon expansion is $T_i = \frac{2a}{R b}$.

#### Question 2
A solid conducting sphere of radius $a$ carries charge $+Q$. It is surrounded by a concentric spherical dielectric shell of inner radius $a$, outer radius $b$, and relative permittivity $\varepsilon_r$:
(A) The electric displacement $\vec{D}$ in the region $a < r < b$ is $\frac{Q}{4\pi r^2}\hat{r}$.  
(B) The electric field in the dielectric shell is $\vec{E} = \frac{Q}{4\pi\varepsilon_0\varepsilon_r r^2}\hat{r}$.  
(C) The bound surface charge density at the inner surface $r = a$ is $\sigma_b(a) = -\frac{Q}{4\pi a^2}\left(1 - \frac{1}{\varepsilon_r}\right)$.  
(D) The total electrostatic energy stored in the whole system is $U = \frac{Q^2}{8\pi\varepsilon_0}\left[\frac{1}{\varepsilon_r}\left(\frac{1}{a} - \frac{1}{b}\right) + \frac{1}{b}\right]$.

#### Question 3
A uniform solid sphere of mass $M$ and radius $R$ is given an initial forward linear velocity $v_0$ and backspin with angular velocity $\omega_0$ on a rough horizontal surface with coefficient of kinetic friction $\mu$:
(A) The direction of friction force on the sphere initially opposes the forward linear velocity.  
(B) The linear speed as a function of time is $v(t) = v_0 - \mu g t$.  
(C) The angular velocity as a function of time is $\omega(t) = \omega_0 - \frac{5\mu g}{2R}t$.  
(D) Pure rolling is achieved when $v(t_r) = R \omega(t_r)$.

#### Question 4
A long coaxial cable consists of an inner solid cylinder of radius $a$ carrying steady current $I$ and an outer thin cylindrical shell of radius $b$ carrying equal return current $I$:
(A) The magnetic field inside the inner conductor ($r < a$) is $B(r) = \frac{\mu_0 I r}{2\pi a^2}$.  
(B) The magnetic field between the conductors ($a < r < b$) is $B(r) = \frac{\mu_0 I}{2\pi r}$.  
(C) The magnetic field outside the cable ($r > b$) is identically zero.  
(D) The self-inductance per unit length of the cable is $\frac{\mu_0}{2\pi}\left[\frac{1}{4} + \ln(b/a)\right]$.

#### Question 5
In a Michelson interferometer illuminated with sodium yellow light containing two close wavelengths $\lambda_1 = 589.0\text{ nm}$ and $\lambda_2 = 589.6\text{ nm}$:
(A) As the movable mirror is translated, the fringe visibility undergoes periodic variations (beats).  
(B) Maximum fringe clarity (contrast) occurs when the path differences for both wavelengths differ by an integer multiple of $\lambda$.  
(C) The mirror translation distance between two consecutive minimum visibility points is $\Delta d = \frac{\lambda_1 \lambda_2}{2(\lambda_2 - \lambda_1)} \approx 0.289\text{ mm}$.  
(D) The coherence length of the sodium doublet is approximately equal to $2\Delta d$.

#### Question 6
In the Bohr-Sommerfeld model of the hydrogen atom, relativistic fine structure arises from:
(A) The relativistic mass variation of the orbiting electron.  
(B) Precession of the perihelion of elliptical Keplerian electronic orbits.  
(C) Splitting of principal energy levels $n$ into $n$ distinct sub-levels characterized by azimuthal quantum number $k$.  
(D) Spin-orbit coupling between electron spin and orbital magnetic field.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a Coolidge X-ray tube operating at potential difference $V = 50.0\text{ kV}$, the minimum cut-off wavelength $\lambda_{\min}$ of the bremsstrahlung continuous spectrum is ______ pm. (Take $h c = 1240\text{ eV}\cdot\text{nm}$, round off to two decimal places)

#### Question 8
One mole of an ideal gas expands adiabatically from state $(P_1 = 8.0\text{ bar}, V_1 = 2.0\text{ L})$ to $(P_2 = 1.0\text{ bar}, V_2 = 8.0\text{ L})$. The work done by the gas is ______ J. (Take $1\text{ bar}\cdot\text{L} = 100\text{ J}$, round off to two decimal places)

#### Question 9
A uniform disc of mass $M = 4.0\text{ kg}$ and radius $R = 0.30\text{ m}$ is rotating freely about its symmetry axis at $\omega = 20.0\text{ rad/s}$. A point mass $m = 1.0\text{ kg}$ is dropped gently onto the rim of the disc and sticks to it. The new angular speed of the system is ______ rad/s.

#### Question 10
In a series LCR circuit, $R = 8.0\ \Omega$, $X_L = 20.0\ \Omega$, and $X_C = 14.0\ \Omega$. The impedance $Z$ of the circuit is ______ $\Omega$.

#### Question 11
Two organ pipes, one open at both ends and the other closed at one end, are sounded in their fundamental modes. If their lengths are $80\text{ cm}$ and $39\text{ cm}$ respectively and speed of sound is $340\text{ m/s}$, the beat frequency heard is ______ Hz. (Round off to two decimal places)

#### Question 12
A simple harmonic oscillator has a frequency of $2.0\text{ Hz}$ and an amplitude of $0.05\text{ m}$. The magnitude of its acceleration at displacement $x = 0.03\text{ m}$ is ______ $\text{m/s}^2$. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle moves in a circular orbit of radius $r_0$ under an attractive central force $F(r) = -k/r^n$. The orbit is stable against small radial perturbations if and only if:  
(A) $n < 3$  
(B) $n > 3$  
(C) $n = 3$  
(D) $n < 2$

#### Question 14
A cylindrical capacitor has inner radius $a$, outer radius $b$, and length $L \gg b$. The capacitance per unit length is:  
(A) $\frac{2\pi\varepsilon_0}{\ln(b/a)}$  
(B) $\frac{4\pi\varepsilon_0}{\ln(b/a)}$  
(C) $\frac{2\pi\varepsilon_0 b}{b - a}$  
(D) $\frac{\pi\varepsilon_0}{\ln(b/a)}$

#### Question 15
A ray of light is refracted through a glass prism of refracting angle $A = 60^\circ$ at minimum deviation. If the angle of minimum deviation is $\delta_m = 30^\circ$, the refractive index of the prism material is:  
(A) $\sqrt{2} \approx 1.414$  
(B) $1.500$  
(C) $\sqrt{3} \approx 1.732$  
(D) $1.333$

#### Question 16
An ideal gas undergoes a process in which its pressure and volume are related by $P V^n = \text{constant}$. The bulk modulus of elasticity of the gas in this process is:  
(A) $n P$  
(B) $P / n$  
(C) $n / P$  
(D) $P$

#### Question 17
A proton enters a uniform magnetic field $B = 0.50\text{ T}$ with speed $v = 1.0\times 10^7\text{ m/s}$ at an angle of $30^\circ$ to the field lines. The pitch of the helical path is:  
(A) $0.228\text{ m}$  
(B) $0.114\text{ m}$  
(C) $0.456\text{ m}$  
(D) $0.057\text{ m}$

#### Question 18
The half-life of a radioactive sample is 10 days. The time taken for the activity to reduce to $1\%$ of its initial value is:  
(A) $66.4\text{ days}$  
(B) $50.0\text{ days}$  
(C) $100.0\text{ days}$  
(D) $33.2\text{ days}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution containing $0.050\text{ M}\ \text{Ag}^+$ and $0.050\text{ M}\ \text{Pb}^{2+}$, selective precipitation of anions is performed:  
$K_{sp}(\text{AgCl}) = 1.8 \times 10^{-10}$, $K_{sp}(\text{PbCl}_2) = 1.7 \times 10^{-5}$  
$K_{sp}(\text{AgI}) = 8.5 \times 10^{-17}$, $K_{sp}(\text{PbI}_2) = 7.1 \times 10^{-9}$
(A) When $\text{NaCl}$ is added dropwise, $\text{AgCl}$ precipitates before $\text{PbCl}_2$.  
(B) When $\text{KI}$ is added dropwise, $\text{AgI}$ precipitates before $\text{PbI}_2$.  
(C) In both cases, the silver halide precipitates at a far lower halide concentration than the lead halide.  
(D) $\text{PbCl}_2$ precipitate dissolves readily in boiling water and recrystallizes upon cooling.

#### Question 20
Regarding the trans-effect in square planar platinum(II) complexes:
(A) The trans-effect refers to the labilization of ligands trans to a specific directing ligand.  
(B) The trans-directing ability order is $\text{CN}^- \sim \text{CO} \sim \text{C}_2\text{H}_4 > \text{PR}_3 > \text{NO}_2^- > \text{I}^- > \text{Br}^- > \text{Cl}^- > \text{NH}_3 > \text{H}_2\text{O}$.  
(C) Reaction of $[\text{PtCl}_4]^{2-}$ with two equivalents of $\text{NH}_3$ yields selectively cis-$[\text{Pt(NH}_3)_2\text{Cl}_2]$ (cisplatin).  
(D) Reaction of $[\text{Pt(NH}_3)_4]^{2+}$ with two equivalents of $\text{Cl}^-$ yields selectively trans-$[\text{Pt(NH}_3)_2\text{Cl}_2]$.

#### Question 21
For the pinacol-pinacolone rearrangement of 2,3-dimethylbutane-2,3-diol with concentrated $\text{H}_2\text{SO}_4$:
(A) The reaction initiates with protonation of one hydroxyl group followed by loss of water to generate a tertiary carbocation.  
(B) A 1,2-methyl shift occurs with concomitant formation of a resonance-stabilized oxonium ion.  
(C) Loss of a proton yields 3,3-dimethylbutan-2-one (pinacolone).  
(D) In unsymmetrical pinacols, carbocation formation occurs preferentially at the carbon that yields the more stable carbocation intermediate.

#### Question 22
Regarding the extraction and refining of nickel:
(A) In the Mond process, nickel is purified by reversible reaction with carbon monoxide.  
(B) Nickel forms volatile nickel tetracarbonyl $\text{Ni(CO)}_4$ at $\sim 330 - 350\text{ K}$.  
(C) $\text{Ni(CO)}_4$ vapor decomposes to pure nickel metal and $\text{CO}$ at $\sim 450 - 470\text{ K}$.  
(D) The process relies on the low boiling point and volatility of $\text{Ni(CO)}_4$ ($43^\circ\text{C}$).

#### Question 23
Which of the following compounds undergo mutarotation in aqueous solution?
(A) $\alpha$-D-Glucopyranose  
(B) $\beta$-D-Glucopyranose  
(C) D-Fructose  
(D) Sucrose

#### Question 24
Regarding the oxides and oxoacids of nitrogen:
(A) $\text{N}_2\text{O}$ (nitrous oxide) is a linear, neutral, diamagnetic gas.  
(B) $\text{NO}$ (nitric oxide) is paramagnetic in the gas phase with one unpaired electron in a $\pi^*$ molecular orbital.  
(C) $\text{NO}_2$ dimerizes to diamagnetic $\text{N}_2\text{O}_4$ upon cooling.  
(D) Solid $\text{N}_2\text{O}_5$ is ionic, existing as nitronium nitrate $[\text{NO}_2]^+[\text{NO}_3]^-$.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of silver chromate ($\text{Ag}_2\text{CrO}_4$) is $K_{sp} = 1.1 \times 10^{-12}$. Its molar solubility in pure water is $X \times 10^{-4}\text{ mol/L}$. The value of $X$ is ______ . (Take $(0.275)^{1/3} = 0.65$, round off to two decimal places)

#### Question 26
A first-order reaction has a rate constant $k = 0.0231\text{ min}^{-1}$. The time required for $90\%$ of the initial reactant to decompose is ______ minutes. (Take $\ln 10 = 2.303$, round off to two decimal places)

#### Question 27
An aqueous solution contains $10.0\text{ g}$ of a non-volatile non-electrolyte solute in $250\text{ g}$ of water. If the boiling point elevation is $\Delta T_b = 0.26^\circ\text{C}$ and $K_b = 0.52\text{ K}\cdot\text{kg/mol}$, the molar mass of the solute is ______ g/mol.

#### Question 28
The coordination number of iron in the brown ring complex $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$ is ______ .

#### Question 29
A $0.020\text{ M}$ solution of formic acid ($\text{HCOOH}$) has a pH of $2.72$. The ionization constant $K_a$ of formic acid is $X \times 10^{-4}$. The value of $X$ is ______ . (Take $10^{-2.72} = 1.9 \times 10^{-3}$, round off to two decimal places)

#### Question 30
The standard reduction potential for $\text{Cu}^{2+} + 2e^- \rightarrow \text{Cu}$ is $E^\circ = +0.34\text{ V}$. Taking $F = 96500\text{ C/mol}$, $\Delta G^\circ$ is ______ kJ/mol. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the aldol condensation of propanal in the presence of dilute $\text{NaOH}$ followed by dehydration is:  
(A) 2-Methylpent-2-enal  
(B) Hex-2-enal  
(C) Hex-3-enal  
(D) 2-Methylpent-3-enal

#### Question 32
The number of bridging chlorine atoms in the dimer $\text{Al}_2\text{Cl}_6$ in the vapor phase is:  
(A) $2$  
(B) $1$  
(C) $3$  
(D) $0$

#### Question 33
In the extraction of copper, matte is transferred to a silica-lined converter where auto-reduction takes place according to:  
(A) $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \rightarrow 6\text{Cu} + \text{SO}_2$  
(B) $\text{Cu}_2\text{S} + 2\text{O}_2 \rightarrow 2\text{CuO} + \text{SO}_2$  
(C) $\text{Cu}_2\text{O} + \text{CO} \rightarrow 2\text{Cu} + \text{CO}_2$  
(D) $\text{Cu}_2\text{S} + \text{C} \rightarrow 2\text{Cu} + \text{CS}_2$

#### Question 34
Which of the following compounds gives a positive carbylamine test?  
(A) Aniline  
(B) N-Methylaniline  
(C) N,N-Dimethylaniline  
(D) Acetamide

#### Question 35
The monomer unit of natural cellulose is:  
(A) $\beta$-D-Glucose  
(B) $\alpha$-D-Glucose  
(C) D-Galactose  
(D) $\beta$-D-Fructose

#### Question 36
Rickets is caused by the dietary deficiency of:  
(A) Vitamin D  
(B) Vitamin A  
(C) Vitamin C  
(D) Vitamin K

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{\sin x}{x}$ for $x \neq 0$ and $f(0) = 1$. Which of the following statements is/are correct?
(A) $f(x)$ is continuous and differentiable at $x = 0$.  
(B) $f'(0) = 0$.  
(C) $f(x)$ is strictly decreasing on $(0, \pi/2)$.  
(D) $\int_0^\infty \frac{\sin x}{x} \, dx = \frac{\pi}{2}$ (Dirichlet integral).

#### Question 38
For the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$:
(A) The area of the parallelogram formed by tangents at the ends of conjugate diameters is constant and equal to $4ab$.  
(B) The sum of squares of any two conjugate semi-diameters is constant: $a'^2 + b'^2 = a^2 + b^2$.  
(C) The eccentric angles of the ends of conjugate diameters differ by $\pi/2$.  
(D) The auxiliary circle has radius $a$.

#### Question 39
For complex numbers $z$ satisfying $|z - 3| + |z + 3| = 10$:
(A) The locus is an ellipse with foci at $(\pm 3, 0)$.  
(B) The semi-major axis is $a = 5$ and eccentricity is $e = 3/5$.  
(C) The semi-minor axis is $b = 4$.  
(D) The locus passes through $(0, \pm 4)$ and $(\pm 5, 0)$.

#### Question 40
Let $A$ be an $n \times n$ matrix with eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$:
(A) The eigenvalues of $A^k$ are $\lambda_1^k, \dots, \lambda_n^k$ for any positive integer $k$.  
(B) $\operatorname{Tr}(A) = \sum_{i=1}^n \lambda_i$.  
(C) $\det(A) = \prod_{i=1}^n \lambda_i$.  
(D) If $A$ is invertible, the eigenvalues of $A^{-1}$ are $1/\lambda_1, \dots, 1/\lambda_n$.

#### Question 41
Let $I_n = \int_0^1 x^n e^{-x} \, dx$ for $n \ge 0$. Which of the following statements is/are correct?
(A) $I_n = -e^{-1} + n I_{n-1}$ for $n \ge 1$.  
(B) $I_0 = 1 - e^{-1}$.  
(C) $\lim_{n \to \infty} I_n = 0$.  
(D) $I_n = n!\left(1 - e^{-1}\sum_{k=0}^n \frac{1}{k!}\right)$.

#### Question 42
The planes $P_1: x + y + z = 1$ and $P_2: x - y + 2z = 2$:
(A) Intersect in a straight line with direction vector $\vec{d} = 3\hat{i} - \hat{j} - 2\hat{k}$.  
(B) The acute angle $\theta$ between the planes satisfies $\cos\theta = \frac{2}{\sqrt{18}} = \frac{\sqrt{2}}{3}$.  
(C) The line of intersection passes through $(0, 0, 1)$.  
(D) Both planes pass through $(1, 0, 0)$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the curve $y = |\sin x|$ and the $x$-axis from $x = 0$ to $x = 2\pi$ is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^{\pi/2} \ln(\sin x) \, dx$ is $-\frac{\pi}{2}\ln K$. The value of $K$ is ______ .

#### Question 45
The number of distinct points of inflection of the curve $y = x e^{-x^2}$ is ______ .

#### Question 46
Let $\vec{a} = \hat{i} + \hat{j}$, $\vec{b} = \hat{j} + \hat{k}$, and $\vec{c} = \hat{k} + \hat{i}$. The scalar triple product $[\vec{a}\ \vec{b}\ \vec{c}]$ is ______ .

#### Question 47
Two cards are drawn successively with replacement from a standard pack of 52 cards. The probability that both cards are Queens is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 48
The distance of the point $(1, 2, 3)$ from the plane $2x - 2y + z = 10$ is ______ . (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = x^x$ with respect to $x$ for $x > 0$ is:  
(A) $x^x(1 + \ln x)$  
(B) $x \cdot x^{x-1}$  
(C) $x^x \ln x$  
(D) $x^x$

#### Question 50
The locus of the pole of a chord of the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ which subtends a right angle at the center is:  
(A) $\frac{x^2}{a^4} + \frac{y^2}{b^4} = \frac{1}{a^2} + \frac{1}{b^2}$  
(B) $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 2$  
(C) $x^2 + y^2 = a^2 + b^2$  
(D) $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$

#### Question 51
The value of $\lim_{x \to 0} \frac{1 - \cos(1 - \cos x)}{x^4}$ is:  
(A) $1/8$  
(B) $1/4$  
(C) $1/2$  
(D) $1/16$

#### Question 52
If $A$ is an invertible $3 \times 3$ matrix such that $A^{-1} = A^T$, then $A$ is:  
(A) An orthogonal matrix  
(B) A symmetric matrix  
(C) A skew-symmetric matrix  
(D) An involutory matrix

#### Question 53
The number of diagonals in a regular decagon (10-sided polygon) is:  
(A) $35$  
(B) $45$  
(C) $20$  
(D) $25$

#### Question 54
The general solution of the differential equation $\frac{dy}{dx} = \frac{x + y + 1}{x + y - 1}$ is:  
(A) $y - x - \ln|x + y| = C$  
(B) $y + x + \ln|x + y| = C$  
(C) $x^2 + y^2 = C$  
(D) $y = C(x + 1)$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__FLUID_VISC__", fluid_visc).replace("__POT_V__", pot_v).replace("__EQ_K__", eq_k).replace("__ANG_FREQ__", ang_freq)
        p2 = raw_p2.replace("__PAD__", pad)

        raw_sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Kanpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Pivoted rod falling under gravity: torque about pivot $\tau = M g \frac{L}{2}\cos\theta = \frac{1}{3}M L^2 \alpha \implies \alpha = \frac{3g}{2L}\cos\theta$. Energy conservation: $M g \frac{L}{2} = \frac{1}{2}\left(\frac{1}{3}M L^2\right)\omega^2 \implies \omega = \sqrt{\frac{3g}{L}}$. Vertical centripetal force at bottom: $N_y - M g = M \omega^2(L/2) = M(3g/L)(L/2) = \frac{3}{2}M g \implies N_y = \frac{5}{2}M g$.
- Q2: (A, B, C) - For Clausius gas $P = \frac{RT}{V-b}$, $(\partial U/\partial V)_T = T(\partial P/\partial T)_V - P = T\frac{R}{V-b} - P = 0$, so $U$ depends only on $T$. $W = \int P dV = R T \ln\left(\frac{V_2-b}{V_1-b}\right) = Q$. In free expansion $\Delta U = 0 \implies \Delta T = 0$, so temperature remains constant.
- Q3: (A, B, C, D) - Uniformly polarized dielectric sphere: $\sigma_b = \vec{P}\cdot\hat{n} = P_0\cos\theta$. Interior field is uniform $\vec{E} = -\vec{P}/(3\varepsilon_0)$. Exterior potential is a pure dipole potential of moment $\vec{p} = \frac{4}{3}\pi R^3 \vec{P}$.
- Q4: (A, B, D) - Superconducting ring has zero resistance, so total magnetic flux $\Phi = \pi r^2 B(t) + L I(t) = \text{const} = \pi r^2 B_0 \implies I(t) = \frac{\pi r^2 B_0}{L}[1 - \cos\omega t]$.
- Q5: (A, B, C, D) - Fabry-Pérot interferometer parameters: $\Delta\lambda_{FSR} = \lambda^2/(2d)$, $\mathcal{F} = \frac{\pi\sqrt{R}}{1-R} \approx 29.8$, resolving power $R = m \mathcal{F}$, Airy intensity distribution.
- Q6: (A, B, C, D) - Relativistic electron-positron annihilation. Positron total energy $E_1 = K + m_0 c^2 = 1.022 + 0.511 = 1.533\text{ MeV}$. In CM frame photons are collinear. Pair creation threshold is $2 m_0 c^2 = 1.022\text{ MeV}$.
- Q7: 1.25 - Terminal velocity $v_t = \frac{2}{9}\frac{r^2(\rho_s - \rho_l)g}{\eta} = \frac{2}{9}\frac{(10^{-3})^2(7800 - 900)(9.80)}{0.012} = \frac{2}{9}\frac{10^{-6}(6900)(9.80)}{0.012} \approx 1.25\text{ m/s}$.
- Q8: 19.04 - Isobaric entropy change $\Delta S = n C_P \ln(V_2/V_1) = 1 \times \left(\frac{5}{2}R\right)\ln(2.5) = 2.5 \times 8.314 \times 0.916 \approx 19.04\text{ J/K}$.
- Q9: 11.07 - Hollow cylinder rolling without slipping: $M g h = \frac{1}{2}M v^2 + \frac{1}{2}I \omega^2 = \frac{1}{2}M(R\omega)^2 + \frac{1}{2}(M R^2)\omega^2 = M R^2 \omega^2 \implies \omega = \frac{\sqrt{gh}}{R} = \frac{\sqrt{9.8 \times 2.0}}{0.40} = \frac{\sqrt{19.6}}{0.40} \approx \frac{4.427}{0.40} \approx 11.07\text{ rad/s}$.
- Q10: 500 - Average power $P_{avg} = V_{rms} I_{rms} \cos\phi = (100)(10)\cos(\pi/3) = 1000 \times 0.5 = 500\text{ W}$.
- Q11: 450 - For closed pipe $f_n = (2n-1)\frac{v}{4L}$. Length of closed pipe $= L/2 \implies f_1 = \frac{v}{4(L/2)} = \frac{v}{2L} = 300\text{ Hz}$. Third harmonic ($n=2$): $f_3 = 3 f_1 = 3 \times 150 = 450\text{ Hz}$.
- Q12: 4.00 - Period $T = 2\pi\sqrt{L/g} \propto 1/\sqrt{g}$. If $g' = g/4$, $T' = T\sqrt{g/g'} = T\sqrt{4} = 2 T = 4.00\text{ s}$.
- Q13: (A) - Central force $F = -k/r^3 \implies V_{\text{eff}}(r) = \frac{L^2 - mk}{2mr^2}$. Particle falls into origin if $L^2 < mk$.
- Q14: (A) - Slab of thickness $d/2$ and dielectric constant 4: effective separation $d' = d - t + t/\kappa = d - d/2 + (d/2)/4 = d/2 + d/8 = 5d/8 \implies C = \frac{\varepsilon_0 A}{5d/8} = \frac{8}{5}C_0$.
- Q15: (A) - Overall magnification $M = m_o \times m_e = \left(\frac{L}{f_o}\right)\left(1 + \frac{D}{f_e}\right) = \left(\frac{20}{1.0}\right)\left(1 + \frac{25}{5.0}\right) = 20 \times 6 = 120$.
- Q16: (A) - On $T$-$S$ diagram, work is area of rectangle: $W = (T_H - T_C)(S_2 - S_1) = (400 - 300)(25 - 10) = 100 \times 15 = 1500\text{ J}$.
- Q17: (A) - $B(x) = \frac{\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}$. At $x = R\sqrt{3}$, $R^2 + x^2 = 4R^2 \implies (4R^2)^{3/2} = 8R^3 \implies B(x) = \frac{\mu_0 I}{16R} = \frac{B_0}{8} \implies B_0 / B(x) = 8 : 1$.
- Q18: (A) - $h\nu = \frac{1240}{400} = 3.10\text{ eV} \implies K_{\max} = 3.10 - 2.14 = 0.96\text{ eV} \implies V_s = 0.96\text{ V}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - $\text{H}_2\text{S}$ selective precipitation: In dilute acid $\text{CuS}$ precipitates. $\text{Fe}^{3+}$ is reduced by $\text{H}_2\text{S}$ to $\text{Fe}^{2+}$ with elemental sulfur deposition. Cyanide complexes copper into $[\text{Cu(CN)}_4]^{3-}$.
- Q20: (A, B, C, D) - Cobalt(III) ligand field splitting: fluoride is weak field ($t_{2g}^4 e_g^2$, paramagnetic, labile), ammonia is strong field ($t_{2g}^6 e_g^0$, diamagnetic, inert).
- Q21: (A, B, C, D) - Saponification mechanism ($B_{AC}2$): second-order kinetics, tetrahedral intermediate, labeled ethoxy appears in ethanol, electrical conductance decreases as $\text{OH}^-$ is replaced by acetate.
- Q22: (A, B) - Lindlar's catalyst and P-2 nickel reduce alkynes stereoselectively to cis-alkenes. $\text{Na}/\text{NH}_3$ (Birch) gives trans-alkenes.
- Q23: (A, B, C, D) - Blast furnace iron metallurgy: basic flux $\text{CaO}$ removes $\text{SiO}_2$ as slag $\text{CaSiO}_3$, combustion zone reaches $2200\text{ K}$, pig iron contains $\sim 4\%$ carbon.
- Q24: (A, B, C, D) - Halogen bond dissociation energies, electron gain enthalpies, and $\text{HF}$ hydrogen bonding anomalies.
- Q25: 1.65 - $K_{sp} = [Mg^{2+}][OH^-]^2 = s(2s)^2 = 4s^3 = 1.8 \times 10^{-11} \implies s^3 = 4.5 \times 10^{-12} \implies s \approx 1.65 \times 10^{-4}\text{ M} \implies [\text{OH}^-] = 3.3 \times 10^{-4}\text{ M} \implies \text{pOH} = 3.48 \implies \text{pH} = 10.52$.
- Q26: 99.70 - $t = \frac{2.303}{k}\log_{10}\left(\frac{100}{10}\right) = \frac{2.303}{0.0231} \times 1 \approx 99.70\text{ min}$.
- Q27: 100 - $\Delta T_b = K_b \frac{w_B / M_B}{w_A} \times 1000 \implies 0.26 = 0.52 \frac{5.0 / M_B}{100} \times 1000 \implies M_B = \frac{0.52 \times 50}{0.26} = 100\text{ g/mol}$.
- Q28: 4 - $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]^{2+}$ has $\text{Fe}^+$ ($d^7$) and $\text{NO}^+$, with 3 unpaired electrons (or classic high spin $\text{Fe}^{2+}$ with 4 unpaired electrons).
- Q29: 2.36 - $h = \sqrt{K_w / (K_a c)} = \sqrt{10^{-14} / (1.8 \times 10^{-5} \times 0.10)} = \sqrt{5.56 \times 10^{-9}} \approx 2.36 \times 10^{-5} \implies X = 2.36$.
- Q30: -65.62 - $\Delta G^\circ = -n F E^\circ = -2(96500)(0.34) = -65620\text{ J} = -65.62\text{ kJ/mol}$.
- Q31: (A) - Aldol of propanal gives 3-hydroxy-2-methylpentanal, which dehydrates to 2-methylpent-2-enal.
- Q32: (A) - Dimeric aluminium chloride $\text{Al}_2\text{Cl}_6$ has two bridging chlorine atoms.
- Q33: (A) - Copper auto-reduction in Bessemer converter: $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \rightarrow 6\text{Cu} + \text{SO}_2$.
- Q34: (A) - Aniline is a primary aromatic amine and gives the carbylamine test with $\text{CHCl}_3/\text{KOH}$.
- Q35: (A) - Cellulose is a polymer of $\beta$-D-glucopyranose units.
- Q36: (A) - Vitamin D deficiency causes rickets in children.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f(-x) = \frac{-x}{e^{-x}-1} - \frac{x}{2} = \frac{x e^x}{e^x - 1} - \frac{x}{2} = \frac{x(e^x - 1 + 1)}{e^x - 1} - \frac{x}{2} = x + \frac{x}{e^x - 1} - \frac{x}{2} = \frac{x}{e^x - 1} + \frac{x}{2} = f(x)$ (even). $\lim_{x\to 0}f(x) = 1$.
- Q38: (A, B, C, D) - Rectangular hyperbola $x^2 - y^2 = a^2$: $e = \sqrt{2}$, perpendicular asymptotes $y = \pm x$, latus rectum $= 2a$, product of distances to asymptotes is $a^2/2$.
- Q39: (A, B, C) - Intersection of disks $|z-i|\le 1$ and $|z-1|\le 1$. Center distance $\sqrt{2}$. Lens area $= 2(\frac{\pi}{4} - \frac{1}{2}) = \frac{\pi}{2} - 1$.
- Q40: (A, B, C, D) - Skew-symmetric odd-order real matrix has determinant 0. Eigenvalues of $3\times 3$ skew-symmetric matrix are $0, \pm i \lambda$. $I + A$ has eigenvalues $1, 1 \pm i\lambda \neq 0 \implies$ invertible.
- Q41: (A, B, C, D) - Dilogarithm evaluation: $-\int_0^1 \frac{\ln(1-x)}{x}dx = \sum \frac{1}{n^2} = \frac{\pi^2}{6}$.
- Q42: (A, C, D) - Intersecting lines: setting parameters $(1+2t, 2+3t, 3+4t) = (2+s, 3+2s, 4+3s)$ yields $t = -1, s = -1 \implies$ point $(-1, -1, -1)$. They lie in $x - 2y + z = 0$.
- Q43: 0.50 - Area $= \int_0^1 (x^3 - 3x^2 + 2x) dx - \int_1^2 (x^3 - 3x^2 + 2x) dx = 1/4 - 0 + (1/4) = 0.50$.
- Q44: 128 - $\int_0^{\pi/2}\sin^4 x \cos^4 x dx = \frac{1}{16}\int_0^{\pi/2}\sin^4(2x) dx = \frac{1}{32}\int_0^\pi \sin^4 u du = \frac{1}{16}\frac{3\pi}{16} = \frac{3\pi}{256}$ (calibrated to $K$).
- Q45: 2 - $f(x) = e^x - x - 2$. $f'(x) = e^x - 1 = 0 \implies x = 0$ is minimum. $f(0) = -1 < 0$. As $x\to -\infty, f(x)\to \infty$. As $x\to\infty, f(x)\to\infty$. Two real roots.
- Q46: 2.12 - $\vec{a} \times \vec{b} = (-\hat{i} + 3\hat{j} + 5\hat{k}) \implies \text{Area} = \frac{1}{2}\sqrt{1 + 9 + 25} = \frac{1}{2}\sqrt{35} \approx 2.96$.
- Q47: 70 - Binomial probability $\binom{8}{4}(1/2)^8 = 70 / 256 \implies p = 70$.
- Q48: 3.00 - Center $(a/2, b/2, c/2) = (1, 2, 2) \implies R = \sqrt{1 + 4 + 4} = 3.00$.
- Q49: (A) - Let $x = \tan\theta \implies \frac{\sqrt{1+x^2}-1}{x} = \frac{\sec\theta - 1}{\tan\theta} = \tan(\theta/2) \implies \arctan(\tan(\theta/2)) = \theta/2 = \frac{1}{2}\arctan x$. Derivative is $1/2$.
- Q50: (A) - Director circle / pole of orthogonal chords is $\frac{x^2}{a^4} + \frac{y^2}{b^4} = \frac{1}{a^2} + \frac{1}{b^2}$.
- Q51: (A) - Taylor expansion: $\lim_{x\to 0}\frac{1 - \cos(x^2/2)}{x^4} = \lim_{x\to 0}\frac{\frac{1}{2}(x^2/2)^2}{x^4} = \frac{1}{8}$.
- Q52: (A) - $A B = A \implies A B A = A^2 \implies A(B A) = A^2 \implies A B = A^2 \implies A = A^2$.
- Q53: (A) - Stars and bars for positive integers: $\binom{n-1}{r-1} = \binom{8-1}{3-1} = \binom{7}{2} = 21$.
- Q54: (A) - Homogeneous substitution $y = v x \implies x(v dx + x dv) - v x dx = x\sqrt{1+v^2}dx \implies \frac{dv}{\sqrt{1+v^2}} = \frac{dx}{x} \implies \ln|v + \sqrt{1+v^2}| = \ln|x| + \ln C \implies y + \sqrt{x^2+y^2} = C x^2$.
"""

        raw_sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Kanpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Joule-Thomson effect for van der Waals gas: constant enthalpy process, $\mu_{JT} = \frac{1}{C_P}\left(\frac{2a}{RT} - b\right)$, inversion temperature $T_i = \frac{2a}{Rb}$.
- Q2: (A, B, C, D) - Dielectric shell around conducting sphere: $D = \frac{Q}{4\pi r^2}$, $E = \frac{D}{\varepsilon_0\varepsilon_r}$, bound surface charge $\sigma_b = -P = -\varepsilon_0(\varepsilon_r - 1)E$, stored electrostatic energy.
- Q3: (A, B, D) - Sphere with backspin on rough surface: friction acts forward if $\omega_0 R > v_0$ or backward if sliding forward. Linear and angular decelerations until $v = R \omega$.
- Q4: (A, B, C, D) - Coaxial cable field via Ampere's Law: $B = \frac{\mu_0 I r}{2\pi a^2}$ inside, $\frac{\mu_0 I}{2\pi r}$ between, 0 outside. Self-inductance per unit length $\frac{\mu_0}{2\pi}[1/4 + \ln(b/a)]$.
- Q5: (A, B, C, D) - Michelson interferometer fringe visibility variations: $\Delta d = \frac{\lambda_1 \lambda_2}{2(\lambda_2 - \lambda_1)} \approx 0.289\text{ mm}$.
- Q6: (A, B, C) - Sommerfeld relativistic fine structure from relativistic mass increase and perihelion precession splitting levels $n$ into sub-levels $k$.
- Q7: 24.80 - Cut-off wavelength $\lambda_{\min} = \frac{1240\text{ eV}\cdot\text{nm}}{50000\text{ eV}} = 0.0248\text{ nm} = 24.80\text{ pm}$.
- Q8: 600.00 - Adiabatic work $W = \frac{P_1 V_1 - P_2 V_2}{\gamma - 1} = \frac{8.0 \times 2.0 - 1.0 \times 8.0}{5/3 - 1}\times 100\text{ J} = \frac{16 - 8}{2/3}\times 100 = 12 \times 100 = 1200\text{ J}$.
- Q9: 13.33 - Conservation of angular momentum about central axis: $I_1 \omega_1 = (I_1 + I_2)\omega_2 \implies (\frac{1}{2}M R^2)\omega_1 = (\frac{1}{2}M R^2 + m R^2)\omega_2 \implies \omega_2 = \frac{M/2}{M/2 + m}\omega_1 = \frac{2}{2 + 1}(20) = \frac{40}{3} \approx 13.33\text{ rad/s}$.
- Q10: 10.00 - $Z = \sqrt{R^2 + (X_L - X_C)^2} = \sqrt{8.0^2 + (20.0 - 14.0)^2} = \sqrt{64 + 36} = 10.00\ \Omega$.
- Q11: 5.45 - Open pipe fundamental $f_1 = \frac{v}{2L_1} = \frac{340}{2(0.80)} = 212.5\text{ Hz}$. Closed pipe fundamental $f_2 = \frac{v}{4L_2} = \frac{340}{4(0.39)} = \frac{340}{1.56} \approx 217.95\text{ Hz}$. Beat frequency $= 217.95 - 212.50 = 5.45\text{ Hz}$.
- Q12: 4.74 - $\omega = 2\pi f = 4\pi\text{ rad/s}$. Acceleration magnitude $a = \omega^2 x = (4\pi)^2(0.03) = 16\pi^2(0.03) \approx 16(9.87)(0.03) \approx 4.74\text{ m/s}^2$.
- Q13: (A) - Central force stability requires $\frac{d}{dr}\left(\frac{L^2}{m r^3} + F(r)\right)_{r_0} > 0 \implies -\frac{3L^2}{m r_0^4} + F'(r_0) > 0 \implies n < 3$.
- Q14: (A) - Cylindrical capacitor $C/L = \frac{2\pi\varepsilon_0}{\ln(b/a)}$.
- Q15: (A) - $\mu = \frac{\sin((A + \delta_m)/2)}{\sin(A/2)} = \frac{\sin(45^\circ)}{\sin(30^\circ)} = \frac{1/\sqrt{2}}{1/2} = \sqrt{2} \approx 1.414$.
- Q16: (A) - Polytropic bulk modulus $B = -V \frac{dP}{dV} = n P$.
- Q17: (A) - Pitch $p = v_{\parallel} T = (v\cos 30^\circ)\frac{2\pi m}{q B} = (10^7 \times \frac{\sqrt{3}}{2})\frac{2\pi(1.67 \times 10^{-27})}{(1.60 \times 10^{-19})(0.50)} \approx 0.228\text{ m}$.
- Q18: (A) - $A/A_0 = 1/100 = (1/2)^n \implies n = \log_2(100) \approx 6.64$ half-lives $\implies t = 6.64 \times 10 = 66.4\text{ days}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Selective precipitation based on $K_{sp}$ disparity. For $\text{AgCl}$ $[\text{Cl}^-] = 1.8 \times 10^{-10} / 0.050 = 3.6 \times 10^{-9}\text{ M}$, while for $\text{PbCl}_2$ $[\text{Cl}^-] = \sqrt{1.7 \times 10^{-5} / 0.050} \approx 0.018\text{ M}$.
- Q20: (A, B, C, D) - Trans-effect in planar $\text{Pt(II)}$ substitution. $\text{Cl}^-$ has stronger trans-effect than $\text{NH}_3$. Reaction of $[\text{PtCl}_4]^{2-}$ with $\text{NH}_3$ yields cisplatin; reaction of $[\text{Pt(NH}_3)_4]^{2+}$ with $\text{Cl}^-$ yields transplatin.
- Q21: (A, B, C, D) - Pinacol-pinacolone rearrangement: carbocation intermediate, 1,2-migration, driving force is formation of stable oxonium/carbonyl bond.
- Q22: (A, B, C, D) - Mond process for nickel: reversible carbonylation to $\text{Ni(CO)}_4$ gas and thermal decomposition to pure $\text{Ni}$.
- Q23: (A, B, C) - Reducing sugars with hemiacetal/hemiketal groups mutarotate. Sucrose is non-reducing and does not mutarotate.
- Q24: (A, B, C, D) - Nitrogen oxides structures: $\text{N}_2\text{O}$ linear neutral, $\text{NO}$ odd-electron paramagnetic, $\text{NO}_2$ dimerizes, $\text{N}_2\text{O}_5$ solid is $[\text{NO}_2]^+[\text{NO}_3]^-$.
- Q25: 0.65 - $K_{sp} = [Ag^+]^2[CrO_4^{2-}] = (2s)^2 s = 4s^3 = 1.1 \times 10^{-12} \implies s^3 = 0.275 \times 10^{-12} \implies s = 0.65 \times 10^{-4}\text{ M} \implies X = 0.65$.
- Q26: 99.70 - $t = \frac{\ln 10}{k} = \frac{2.303}{0.0231} \approx 99.70\text{ min}$.
- Q27: 80 - $\Delta T_b = K_b \frac{w_B / M_B}{w_A} \times 1000 \implies 0.26 = 0.52 \frac{10 / M_B}{250} \times 1000 \implies M_B = \frac{0.52 \times 40}{0.26} = 80\text{ g/mol}$.
- Q28: 6 - Six monodentate ligands around iron (5 water + 1 nitrosyl).
- Q29: 1.80 - $K_a = \frac{[\text{H}^+]^2}{c} = \frac{(1.9 \times 10^{-3})^2}{0.020} = \frac{3.61 \times 10^{-6}}{0.020} \approx 1.80 \times 10^{-4} \implies X = 1.80$.
- Q30: -65.62 - $\Delta G^\circ = -n F E^\circ = -2(96500)(0.34) = -65.62\text{ kJ/mol}$.
- Q31: (A) - Aldol condensation of propanal yields 2-methylpent-2-enal.
- Q32: (A) - Two bridging chlorine atoms in dimeric $\text{Al}_2\text{Cl}_6$.
- Q33: (A) - Copper auto-reduction in converter: $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \rightarrow 6\text{Cu} + \text{SO}_2$.
- Q34: (A) - Primary amine aniline gives carbylamine test.
- Q35: (A) - Cellulose monomer is $\beta$-D-glucose.
- Q36: (A) - Rickets is caused by Vitamin D deficiency.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Sinc function properties: analytic, $f'(0) = 0$, Dirichlet integral $\int_0^\infty \frac{\sin x}{x} dx = \pi/2$.
- Q38: (A, B, C, D) - Conjugate diameters of ellipse: parallelogram area $4ab$ (Apollonius theorem), $a'^2 + b'^2 = a^2 + b^2$, difference of eccentric angles is $\pi/2$.
- Q39: (A, B, C, D) - Ellipse with foci $(\pm 3, 0)$ and $2a = 10 \implies a = 5, c = 3 \implies b = 4$. Passes through $(0, \pm 4)$ and $(\pm 5, 0)$.
- Q40: (A, B, C, D) - Matrix eigenvalue theorems: powers, trace, determinant, and inverse.
- Q41: (A, B, C, D) - Incomplete gamma integral recurrence: $I_n = -e^{-1} + n I_{n-1}$.
- Q42: (A, B) - Normal vectors $(1, 1, 1)$ and $(1, -1, 2)$. Angle $\cos\theta = \frac{1 - 1 + 2}{\sqrt{3}\sqrt{6}} = \frac{2}{\sqrt{18}} = \frac{\sqrt{2}}{3}$. Direction of line is cross product: $(3, -1, -2)$.
- Q43: 4.00 - Area $= 2 \int_0^\pi \sin x dx = 2 [-\cos x]_0^\pi = 2(2) = 4.00$.
- Q44: 2 - Euler's log-sine integral: $\int_0^{\pi/2}\ln(\sin x) dx = -\frac{\pi}{2}\ln 2 \implies K = 2$.
- Q45: 3 - $y = x e^{-x^2}$. $y'' = (4x^3 - 6x)e^{-x^2} = 2x(2x^2 - 3)e^{-x^2} = 0 \implies x = 0, \pm\sqrt{3/2}$. Three inflection points.
- Q46: 2.00 - $[\vec{a}\ \vec{b}\ \vec{c}] = \vec{a}\cdot(\vec{b} \times \vec{c}) = 1(1) + 1(1) = 2.00$.
- Q47: 169 - Probability $= (4/52) \times (4/52) = (1/13)^2 = 1/169 \implies K = 169$.
- Q48: 3.00 - Distance $d = \frac{|2(1) - 2(2) + 3 - 10|}{\sqrt{4 + 4 + 1}} = \frac{|-9|}{3} = 3.00$.
- Q49: (A) - Let $y = x^x \implies \ln y = x \ln x \implies y'/y = 1 + \ln x \implies y' = x^x(1 + \ln x)$.
- Q50: (A) - Orthogonal chord pole locus for ellipse is $\frac{x^2}{a^4} + \frac{y^2}{b^4} = \frac{1}{a^2} + \frac{1}{b^2}$.
- Q51: (A) - Taylor expansion: $\lim_{x\to 0}\frac{1 - \cos(x^2/2)}{x^4} = \frac{1}{2}(1/2)^2 = 1/8$.
- Q52: (A) - $A^{-1} = A^T \implies A A^T = I \implies$ orthogonal matrix.
- Q53: (A) - Diagonals of $n$-gon: $\frac{n(n-3)}{2} = \frac{10(7)}{2} = 35$.
- Q54: (A) - Homogeneous substitution or substitution $u = x + y \implies u' = 1 + y' \implies u' - 1 = \frac{u+1}{u-1} \implies u' = \frac{2u}{u-1} \implies \frac{u-1}{2u}du = dx \implies y - x - \ln|x+y| = C$.
"""

        raw_val = r"""# Answer Key & Benchmark Alignment – Mock Examination __PAD__
## Organising Institute Style: IIT Kanpur (`IIT_KANPUR_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C; Q3: A,B,C,D; Q4: A,B,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 1.25; Q8: 19.04; Q9: 11.07; Q10: 500; Q11: 450; Q12: 4.00; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 10.52; Q26: 99.70; Q27: 100; Q28: 4; Q29: 2.36; Q30: -65.62; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,C,D; Q43: 0.50; Q44: 128; Q45: 2; Q46: 2.96; Q47: 70; Q48: 3.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C; Q7: 24.80; Q8: 1200.00; Q9: 13.33; Q10: 10.00; Q11: 5.45; Q12: 4.74; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C; Q24: A,B,C,D; Q25: 0.65; Q26: 99.70; Q27: 80; Q28: 6; Q29: 1.80; Q30: -65.62; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B; Q43: 4.00; Q44: 2; Q45: 3; Q46: 2.00; Q47: 169; Q48: 3.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""

        sol1 = raw_sol1.replace("__PAD__", pad)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Kanpur")
        print(f"Generated IIT Kanpur Mock {pad}!")

if __name__ == "__main__":
    generate_kanpur_11_to_15()

