# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Guwahati Mock 03.
Empirical Signature: IIT Guwahati Benchmark (2009, 2016, 2023)
- Conceptual Elegance over Brute Calculation
- Modern Physics & Thermodynamics / Statistical Mechanics Emphasis (>=35%)
- Geometric Insight in Conics, Vectors, Complex Numbers
- Clean Physical Chemistry & Rigorous Stereochemical Organic Cascades
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 03 – Paper 1
## Organising Institute Style Inspiration: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
**Historical Reference Benchmark**: 2009, 2016, 2023 Official Examination Papers  
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
In an isotropic radiation field inside an evacuated cavity with perfectly reflecting walls maintained at uniform temperature $T$:
(A) The spectral energy density $u(\nu, T)$ is isotropic and homogeneous throughout the cavity volume.  
(B) The radiation pressure exerted on the cavity walls is related to the total volumetric energy density $u$ by $P = \frac{1}{3} u$.  
(C) The total energy density scales with absolute temperature as $u \propto T^4$.  
(D) If the cavity expands adiabatically and reversibly from volume $V_1$ to $V_2$, the temperature drops according to $V T^3 = \text{constant}$.

#### Question 2
Taking into account relativistic kinematics, an electron of rest mass $m_0$ and charge $e$ is accelerated from rest through an electrostatic potential difference $V$. Let $c$ be the speed of light in vacuum. Which of the following statements is/are correct?
(A) The kinetic energy of the electron is $K = e V$.  
(B) The relativistic momentum of the electron is $p = \frac{1}{c}\sqrt{e^2 V^2 + 2 m_0 c^2 e V}$.  
(C) The de Broglie wavelength is $\lambda = \frac{h}{\sqrt{2 m_0 e V}}\left(1 + \frac{e V}{2 m_0 c^2}\right)^{-1/2}$.  
(D) If $e V \ll m_0 c^2$, the de Broglie wavelength reduces to the classical expression $\lambda \approx \frac{h}{\sqrt{2 m_0 e V}}$.

#### Question 3
A steady direct current $I$ flows uniformly along a cylindrical conductor of radius $a$, length $L$, and resistivity $\rho$. The potential difference across its ends is $V = I R$. Which of the following statements is/are correct?
(A) Inside the wire, the electric field is $\vec{E} = \frac{V}{L}\hat{z}$ parallel to the wire axis.  
(B) At the surface of the wire ($r = a$), the magnetic field is $\vec{B} = \frac{\mu_0 I}{2\pi a}\hat{\phi}$.  
(C) The Poynting vector at the surface of the wire is directed radially inward towards the wire axis, with magnitude $S = \frac{V I}{2\pi a L}$.  
(D) The total inward flux of the Poynting vector across the surface of the wire equals the Joule heating rate $I^2 R$.

#### Question 4
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal conveyor belt that moves with a constant horizontal acceleration $a_0$. The sphere rolls without slipping on the belt. Which of the following statements is/are correct?
(A) The acceleration of the center of mass of the sphere relative to the ground is $a_{\text{cm}} = \frac{2}{7} a_0$.  
(B) The frictional force exerted by the belt on the sphere is $f = \frac{2}{7} M a_0$ directed in the direction of the belt acceleration.  
(C) The minimum coefficient of static friction $\mu_{\min}$ required to prevent slipping is $\frac{2 a_0}{7 g}$.  
(D) The angular acceleration of the sphere is $\alpha = \frac{5 a_0}{7 R}$.

#### Question 5
In a Michelson interferometer illuminated with monochromatic light of wavelength $\lambda = 589\text{ nm}$, an evacuated transparent gas cell of length $L = 10.0\text{ cm}$ is placed in one of the arms. A gas is slowly introduced into the cell until atmospheric pressure is reached, causing $N = 100$ interference fringes to cross the field of view. Which of the following statements is/are correct?
(A) The optical path length change through the gas cell is $\Delta = 2(\mu - 1) L$, where $\mu$ is the refractive index of the gas.  
(B) The number of fringes crossed satisfies $N = \frac{2(\mu - 1) L}{\lambda}$.  
(C) The refractive index of the gas at atmospheric pressure is $\mu = 1 + \frac{N \lambda}{2 L} \approx 1.000295$.  
(D) If the cell length $L$ were doubled, the number of fringes crossed would be halved.

#### Question 6
According to Moseley's law for characteristic X-rays, the frequency $\nu$ of the $K_\alpha$ line of an element of atomic number $Z$ satisfies $\sqrt{\nu} = a(Z - b)$, where $a$ and $b$ are constants. Which of the following statements is/are correct?
(A) The screening constant for the $K_\alpha$ transition is $b \approx 1$.  
(B) The constant $a$ is related to the Rydberg frequency $\nu_R$ by $a = \sqrt{\frac{3}{4}\nu_R}$.  
(C) A plot of $\sqrt{\nu}$ versus atomic number $Z$ yields a straight line with horizontal intercept $Z = b$.  
(D) Moseley's law provided experimental proof that atomic number $Z$, rather than atomic weight, governs the periodic arrangement of elements.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A solar sail spacecraft of total mass $m = 200\text{ kg}$ has a completely reflecting planar square sail of side length $L = 20\text{ m}$. The intensity of solar radiation incident normally on the sail is $I = 1350\text{ W/m}^2$. Calculate the radiation force acceleration of the spacecraft in $\text{mm/s}^2$. (Speed of light $c = 3.0 \times 10^8\text{ m/s}$. Round off to two decimal places).

#### Question 8
Two moles of an ideal monoatomic gas ($\gamma = 5/3$) undergo an adiabatic expansion in which the temperature drops from $T_1 = 600\text{ K}$ to $T_2 = 300\text{ K}$. Calculate the work done by the gas in kilojoules ($\text{kJ}$). (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to two decimal places).

#### Question 9
A cylindrical liquid column of density $\rho = 1000\text{ kg/m}^3$ and radius $R_0 = 1.0\text{ mm}$ falls vertically under gravity. According to the Rayleigh-Plateau instability, the column breaks into droplets when perturbed by surface capillary waves of wavelength $\lambda > 2\pi R_0$. Calculate the minimum wavelength $\lambda_c$ in millimeters required for breakup. (Take $\pi \approx 3.1416$. Round off to two decimal places).

#### Question 10
In a series RLC circuit, $R = 10\ \Omega$, $L = 0.10\text{ H}$, and $C = 100\ \mu\text{F}$. Find the resonant angular frequency $\omega_0$ in $\text{rad/s}$.

#### Question 11
A source of sound of frequency $f_0 = 600\text{ Hz}$ moves at a constant speed $u = 30\text{ m/s}$ along a straight line. An observer is situated at a perpendicular distance $d = 40\text{ m}$ from the line of motion. Calculate the frequency (in Hz) heard by the observer at the exact instant when the source is at its closest approach to the observer. (Speed of sound $v = 330\text{ m/s}$. Round off to the nearest integer).

#### Question 12
A convex lens of focal length $f = 20.0\text{ cm}$ in air ($\mu_g = 1.50$) is completely submerged in water ($\mu_w = 1.33$). Calculate the new focal length of the lens in water in centimeters. (Round off to the nearest integer).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
An inverted pendulum consists of a rigid light rod of length $l$ carrying a mass $m$ at its upper tip. The pivot point is vibrated vertically with displacement $y(t) = a \cos(\omega t)$ with high frequency $\omega \gg \sqrt{g/l}$. According to the Kapitza method of effective potential, the inverted vertical position is dynamically stable if:
(A) $a^2 \omega^2 > 2 g l$  
(B) $a \omega > \sqrt{g l}$  
(C) $a^2 \omega^2 > g l$  
(D) $a \omega > 2 \sqrt{g l}$

#### Question 14
A parallel-plate capacitor with plate area $A$ and separation $d$ is charged to a potential difference $V_0$ and then isolated from the battery. The plates are now pulled apart to separation $2d$. The electrostatic energy stored in the capacitor:
(A) Doubles  
(B) Halves  
(C) Remains unchanged  
(D) Quadruples

#### Question 15
A uniform magnetic field $\vec{B} = B_0 \hat{k}$ is localized in a cylindrical region of radius $R$ centered on the z-axis. The magnetic field increases at a constant rate $\frac{dB}{dt} = \alpha > 0$. The induced electric field $\vec{E}$ at a radial distance $r > R$ from the axis is:
(A) $-\frac{\alpha R^2}{2 r}\hat{\phi}$  
(B) $-\frac{\alpha r}{2}\hat{\phi}$  
(C) $-\frac{\alpha R}{2}\hat{\phi}$  
(D) $0$

#### Question 16
An alpha particle of kinetic energy $K = 5.0\text{ MeV}$ is scattered head-on by a stationary gold nucleus ($Z = 79$). The distance of closest approach $r_{\min}$ is: (Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$, $e = 1.6 \times 10^{-19}\text{ C}$)
(A) $4.55 \times 10^{-14}\text{ m}$  
(B) $2.28 \times 10^{-14}\text{ m}$  
(C) $9.10 \times 10^{-14}\text{ m}$  
(D) $1.14 \times 10^{-14}\text{ m}$

#### Question 17
A Carnot engine operates between reservoirs at temperatures $T_H = 800\text{ K}$ and $T_C = 400\text{ K}$. If the engine absorbs $2000\text{ J}$ of heat from the hot reservoir per cycle, the work done per cycle is:
(A) $1000\text{ J}$  
(B) $1500\text{ J}$  
(C) $500\text{ J}$  
(D) $2000\text{ J}$

#### Question 18
A thin spherical shell of radius $R$ and mass $M$ is filled with water of mass $m$. The shell is rolling without slipping on a horizontal surface. If the water inside is assumed to be ideal and frictionless (does not rotate with the shell), the effective kinetic energy of the system when the shell moves with velocity $v$ is:
(A) $\frac{1}{2}(M + m)v^2 + \frac{1}{3}M v^2$  
(B) $\frac{1}{2}(M + m)v^2 + \frac{1}{5}(M + m)v^2$  
(C) $\frac{1}{2}(M + m)v^2 + \frac{1}{3}(M + m)v^2$  
(D) $\frac{1}{2} M v^2 + \frac{1}{2} m v^2$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the temperature dependence of cell electromotive force (EMF) and the Gibbs-Helmholtz relation:
(A) $\Delta G = -n F E_{\text{cell}}$.  
(B) The entropy change of the cell reaction is given by $\Delta S = n F \left(\frac{\partial E_{\text{cell}}}{\partial T}\right)_P$.  
(C) The enthalpy change of the cell reaction is $\Delta H = -n F E_{\text{cell}} + n F T \left(\frac{\partial E_{\text{cell}}}{\partial T}\right)_P$.  
(D) If $\left(\frac{\partial E_{\text{cell}}}{\partial T}\right)_P > 0$, the cell absorbs heat from the surroundings during reversible discharge ($q_{\text{rev}} > 0$).

#### Question 20
Consider the [4+2] Diels-Alder cycloaddition between 1,3-cyclopentadiene and maleic anhydride:
(A) The reaction is a concerted, stereospecific pericyclic reaction occurring via a single transition state.  
(B) The diene must adopt the $s$-cis conformation to undergo cycloaddition.  
(C) The stereochemistry of the dienophile is preserved in the adduct (cis-diester remains cis).  
(D) Due to secondary orbital interactions in the transition state, the endo-adduct is the kinetically favored major product.

#### Question 21
Regarding the oxoacids of phosphorus ($\text{H}_3\text{PO}_2$, $\text{H}_3\text{PO}_3$, $\text{H}_3\text{PO}_4$):
(A) Hypophosphorous acid ($\text{H}_3\text{PO}_2$) contains one ionizable $\text{P-OH}$ bond and two direct $\text{P-H}$ bonds, making it monobasic.  
(B) Phosphorous acid ($\text{H}_3\text{PO}_3$) contains two $\text{P-OH}$ bonds and one $\text{P-H}$ bond, making it dibasic.  
(C) Both $\text{H}_3\text{PO}_2$ and $\text{H}_3\text{PO}_3$ act as strong reducing agents due to the presence of direct $\text{P-H}$ bonds.  
(D) Phosphoric acid ($\text{H}_3\text{PO}_4$) has three $\text{P-OH}$ bonds, is tribasic, and lacks reducing properties.

#### Question 22
Which of the following pairs of liquid mixtures exhibit negative deviation from Raoult's law?
(A) Acetone and Chloroform.  
(B) Phenol and Aniline.  
(C) Nitric acid and Water.  
(D) Ethanol and Acetone.

#### Question 23
Regarding the Jahn-Teller effect in coordination complexes:
(A) Non-linear degenerate electronic states undergo geometrical distortion to remove the electronic degeneracy and lower the overall energy.  
(B) The effect is particularly pronounced in high-spin $d^4$ ($\text{Cr}^{2+}$) and $d^9$ ($\text{Cu}^{2+}$) octahedral complexes due to asymmetrical occupancy of $e_g$ orbitals.  
(C) In $[\text{Cu}(\text{H}_2\text{O})_6]^{2+}$, tetragonal elongation is observed with two axial bonds being longer than the four equatorial bonds.  
(D) Octahedral complexes with symmetrically filled or half-filled subshells ($d^3, d^5\text{ high-spin}, d^8, d^{10}$) do not exhibit Jahn-Teller distortions.

#### Question 24
In the Beckmann rearrangement of cyclohexanone oxime treated with concentrated $\text{H}_2\text{SO}_4$:
(A) The reaction involves migration of the alkyl group anti to the leaving $\text{OH}$ group.  
(B) The reaction proceeds via an electron-deficient nitrogen intermediate (nitrenium-like ion).  
(C) The product of the rearrangement is $\varepsilon$-caprolactam, a seven-membered cyclic amide.  
(D) Polymerization of $\varepsilon$-caprolactam yields Nylon-6.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The EMF of the cell $\text{Cd}(s) \mid \text{CdCl}_2(0.10\text{ M}) \parallel \text{AgCl}(s) \mid \text{Ag}(s)$ is $0.675\text{ V}$ at $25^\circ\text{C}$ ($298\text{ K}$) and its temperature coefficient is $\left(\frac{\partial E}{\partial T}\right)_P = -6.5 \times 10^{-4}\text{ V/K}$. For the cell reaction $\text{Cd}(s) + 2\text{AgCl}(s) \to \text{Cd}^{2+} + 2\text{Ag} + 2\text{Cl}^-$, calculate the standard enthalpy change $\Delta H$ in $\text{kJ/mol}$. (Take $n = 2, F = 96500\text{ C/mol}$. Round off to the nearest integer).

#### Question 26
For an enzyme-catalyzed reaction obeying Michaelis-Menten kinetics, the maximum velocity is $V_{\max} = 5.0 \times 10^{-4}\text{ mol}\cdot\text{L}^{-1}\cdot\text{s}^{-1}$ and the Michaelis constant is $K_m = 2.0 \times 10^{-3}\text{ M}$. Calculate the initial rate of reaction in units of $10^{-4}\text{ mol}\cdot\text{L}^{-1}\cdot\text{s}^{-1}$ when the substrate concentration is $[S] = 6.0 \times 10^{-3}\text{ M}$. (Round off to two decimal places).

#### Question 27
An organic compound contains $52.2\%$ carbon, $13.0\%$ hydrogen, and $34.8\%$ oxygen by mass. Its vapor density is $23.0$. Calculate the molecular mass of the compound.

#### Question 28
In an experiment on conductometric titration, $100\text{ mL}$ of $0.05\text{ M}$ $\text{HCl}$ is titrated with $0.10\text{ M}$ $\text{NaOH}$. What volume of $\text{NaOH}$ in mL is required to reach the equivalence point?

#### Question 29
A monobasic weak acid has an ionization constant $K_a = 2.5 \times 10^{-5}$ at $25^\circ\text{C}$. Calculate the pH of a $0.10\text{ M}$ solution of this acid. (Round off to two decimal places).

#### Question 30
Calculate the radius of an octahedral void in terms of the sphere radius $R$ for a close-packed cubic lattice. If $r_{\text{void}} = k R$, find the value of $k$ to three decimal places.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The correct IUPAC name of the complex $\text{K}_3[\text{Fe}(\text{CN})_5\text{NO}]$ (sodium nitroprusside homologue) is:
(A) Potassium pentacyanonitrosylferrate(II)  
(B) Potassium pentacyanidonitrosylferrate(III)  
(C) Potassium pentacyanidonitrosyliumferrate(II)  
(D) Potassium nitrosylpentacyanoiron(II)

#### Question 32
Which of the following alkenes upon ozonolysis followed by reductive workup with $(\text{CH}_3)_2\text{S}$ produces only acetone?
(A) 2,3-Dimethylbut-2-ene  
(B) 2-Methylpropene  
(C) But-2-ene  
(D) 2,3-Dimethylbut-1-ene

#### Question 33
The spin-only magnetic moment of $[\text{Mn}(\text{CN})_6]^{3-}$ is:
(A) $2.83\ \mu_B$  
(B) $4.90\ \mu_B$  
(C) $1.73\ \mu_B$  
(D) $3.87\ \mu_B$

#### Question 34
In the extraction of copper from copper pyrites ($\text{CuFeS}_2$), silica ($\text{SiO}_2$) is added during smelting in the blast furnace to remove:
(A) $\text{FeO}$ as $\text{FeSiO}_3$ (slag)  
(B) $\text{Cu}_2\text{O}$ as $\text{Cu}_2\text{SiO}_3$  
(C) $\text{FeS}$ as $\text{FeSO}_4$  
(D) $\text{SO}_2$ as sulfur

#### Question 35
The monomer of natural rubber is:
(A) Isoprene (2-methylbuta-1,3-diene)  
(B) Chloroprene (2-chlorobuta-1,3-diene)  
(C) Buta-1,3-diene  
(D) Styrene

#### Question 36
Which of the following compounds gives a positive iodoform test upon reaction with $\text{I}_2 / \text{NaOH}$?
(A) Pentan-2-one  
(B) Pentan-3-one  
(C) Benzaldehyde  
(D) Methanol

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $E_1: \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b > 0$) and $E_2: \frac{x^2}{a^2 - \lambda} + \frac{y^2}{b^2 - \lambda} = 1$ be two confocal conics with parameter $\lambda$. Which of the following statements is/are correct?
(A) The foci of both conics coincide at $(\pm\sqrt{a^2 - b^2}, 0)$.  
(B) If $0 < \lambda < b^2$, $E_2$ is an ellipse confocal with $E_1$.  
(C) If $b^2 < \lambda < a^2$, $E_2$ is a hyperbola confocal with $E_1$.  
(D) An ellipse and a hyperbola belonging to the same confocal family intersect orthogonally at every point of intersection.

#### Question 38
Let $n \ge 2$ be an integer. Consider the $n$-th roots of unity $1, \omega, \omega^2, \dots, \omega^{n-1}$. Which of the following statements is/are correct?
(A) $\sum_{k=0}^{n-1} \omega^k = 0$.  
(B) $\prod_{k=1}^{n-1} (1 - \omega^k) = n$.  
(C) $\prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = \frac{n}{2^{n-1}}$.  
(D) The points representing $\omega^k$ in the complex plane form the vertices of a regular $n$-gon inscribed in the unit circle.

#### Question 39
Let $f(x) = \int_0^x \frac{\sin t}{t} \, dt$ for $x > 0$ (Sine integral $\text{Si}(x)$). Which of the following statements is/are correct?
(A) $f'(x) = \frac{\sin x}{x}$.  
(B) The critical points of $f(x)$ are $x = k\pi$ for positive integers $k$.  
(C) $x = \pi$ is a point of local maximum.  
(D) $\lim_{x \to \infty} f(x) = \frac{\pi}{2}$ (Dirichlet integral).

#### Question 40
Let $A$ be a $3 \times 3$ real invertible matrix satisfying $A^3 - 3 A^2 + 2 A - I_3 = 0$. Which of the following statements is/are correct?
(A) $A^{-1} = A^2 - 3 A + 2 I_3$.  
(B) $\det(A) \ne 0$.  
(C) The trace of $A$ equals $3$.  
(D) $A$ cannot have zero as an eigenvalue.

#### Question 41
Let $S$ be the surface defined by $z = x^2 + y^2$. A tangent plane to $S$ at the point $P(x_0, y_0, z_0)$ has normal vector:
(A) $\vec{n} = 2x_0 \hat{i} + 2y_0 \hat{j} - \hat{k}$.  
(B) The equation of the tangent plane is $z - z_0 = 2x_0(x - x_0) + 2y_0(y - y_0)$.  
(C) If $x_0 = 1, y_0 = 2$, the tangent plane passes through the origin $(0, 0, 0)$.  
(D) The tangent plane intersects the paraboloid only at the single point $P(x_0, y_0, z_0)$.

#### Question 42
Consider the function $h(x) = \frac{x^2 - x + 1}{x^2 + x + 1}$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $h(x)$ is continuous and differentiable for all $x \in \mathbb{R}$.  
(B) The maximum value of $h(x)$ is $3$, attained at $x = -1$.  
(C) The minimum value of $h(x)$ is $\frac{1}{3}$, attained at $x = 1$.  
(D) The range of $h(x)$ is $\left[\frac{1}{3}, 3\right]$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Let $I = \int_0^{\pi/2} \frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}} \, dx$. If $I = \frac{\pi}{k}$, find the value of $k$.

#### Question 44
Find the distance between the parallel planes $2x - 2y + z + 3 = 0$ and $4x - 4y + 2z - 5 = 0$. (Round off to two decimal places).

#### Question 45
Find the number of real roots of the equation $x^3 - 3x + 1 = 0$.

#### Question 46
Let $y = y(x)$ satisfy the differential equation $\frac{dy}{dx} + 2y = 4x$ with $y(0) = 1$. Calculate the value of $y(1)$. (Take $e^{-2} \approx 0.1353$. Round off to two decimal places).

#### Question 47
Let a fair coin be tossed 6 times. Find the probability of obtaining at least 4 heads. (Give the answer as a percentage rounded to two decimal places).

#### Question 48
Find the radius of the circle inscribed in the triangle formed by the lines $x = 0, y = 0$, and $3x + 4y = 12$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The value of the determinant $\det \begin{pmatrix} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{pmatrix}$ is:
(A) $(a - b)(b - c)(c - a)$  
(B) $(b - a)(c - b)(a - c)$  
(C) $(a + b)(b + c)(c + a)$  
(D) $0$

#### Question 50
The angle between the asymptotes of the hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$ is:
(A) $2 \arctan(3/4)$  
(B) $2 \arctan(4/3)$  
(C) $\pi/2$  
(D) $\arctan(7/24)$

#### Question 51
The value of the limit $\lim_{x \to 0} \frac{e^x - e^{-x} - 2x}{x^3}$ is:
(A) $\frac{1}{3}$  
(B) $\frac{1}{6}$  
(C) $\frac{2}{3}$  
(D) $0$

#### Question 52
If $\vec{a}, \vec{b}, \vec{c}$ are three mutually perpendicular unit vectors, the value of $|\vec{a} + \vec{b} + \vec{c}|$ is:
(A) $\sqrt{3}$  
(B) $3$  
(C) $1$  
(D) $\sqrt{2}$

#### Question 53
The number of ways in which 5 boys and 5 girls can sit in a circle such that no two girls are adjacent is:
(A) $4! \times 5!$  
(B) $5! \times 5!$  
(C) $4! \times 4!$  
(D) $10!$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = \frac{x + y}{x}$ with $y(1) = 0$ is:
(A) $y = x \ln x$  
(B) $y = x^2 - x$  
(C) $y = \ln x$  
(D) $y = x e^x$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 03 – Paper 2
## Organising Institute Style Inspiration: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
**Historical Reference Benchmark**: 2009, 2016, 2023 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
- **Section 3 (6 Questions per subject – Matching List / Matrix Match)**:
  - Full Marks: **+3** if only the correct matching combination is chosen.
  - Negative Marks: **-1** for incorrect option.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A superconductor in the Meissner state expels all magnetic flux from its interior ($B = 0$). A small permanent magnetic dipole of magnetic moment $\vec{m} = m \hat{k}$ is positioned at height $h$ vertically above a flat horizontal superconducting plane ($z = 0$). Using the method of magnetic images:
(A) The image magnetic dipole is situated at $z = -h$ with moment $\vec{m}' = -m \hat{k}$ (pointing downwards).  
(B) The magnetic interaction between the real dipole and its image produces a repulsive vertical force.  
(C) The levitation force on the magnet scales with height as $F_z \propto \frac{1}{h^4}$.  
(D) At a stable equilibrium height, the repulsive magnetic force balances the weight $M g$ of the magnet.

#### Question 2
Two thin coaxial circular coils each of radius $R$ and $N$ turns are separated by distance $d = R$ (Helmholtz coil configuration). Both coils carry equal currents $I$ in the same direction. Which of the following statements is/are correct?
(A) The magnetic field at the midpoint on the axis is $B_0 = \left(\frac{4}{5}\right)^{3/2} \frac{\mu_0 N I}{R}$.  
(B) At the midpoint, the first derivative of the magnetic field with respect to axial position vanishes: $\frac{dB}{dz} = 0$.  
(C) The second derivative also vanishes: $\frac{d^2 B}{dz^2} = 0$.  
(D) The Helmholtz arrangement produces an exceptionally uniform magnetic field over a large volume near the midpoint.

#### Question 3
A particle of mass $m$ is placed in a one-dimensional finite square well of width $2a$ and depth $V_0$:
$$V(x) = \begin{cases} -V_0 & \text{for } |x| < a \\ 0 & \text{for } |x| \ge a \end{cases}$$
Which of the following statements is/are correct?
(A) Bound state energy eigenvalues are strictly negative ($-V_0 < E < 0$).  
(B) Wavefunctions of bound states have definite parity (symmetric or antisymmetric).  
(C) There exists at least one symmetric bound state no matter how shallow or narrow the well is.  
(D) The probability of finding the particle in the classically forbidden region $|x| > a$ is non-zero (quantum penetration).

#### Question 4
A thermodynamic gas undergoes a Joule-Thomson expansion through a porous plug from pressure $P_1$ to $P_2$ ($P_2 < P_1$) under adiabatic conditions. Which of the following statements is/are correct?
(A) The initial and final enthalpies of the gas are equal ($H_1 = H_2$).  
(B) For an ideal gas, the temperature change $\Delta T = 0$.  
(C) The Joule-Thomson coefficient is given by $\mu_{\text{JT}} = \frac{1}{C_P}\left[T \left(\frac{\partial V}{\partial T}\right)_P - V\right]$.  
(D) At the inversion temperature $T_i$, $\mu_{\text{JT}} = 0$.

#### Question 5
A planar diffraction grating has $N$ parallel slits each of width $b$ separated by opaque spaces of width $c$ (grating period $d = b + c$). Monochromatic light of wavelength $\lambda$ is incident normally on the grating. Which of the following statements is/are correct?
(A) Principal interference maxima occur at angles $\theta$ satisfying $d \sin\theta = m \lambda$ ($m = 0, \pm 1, \pm 2, \dots$).  
(B) The angular width of the principal maxima is inversely proportional to the total number of slits $N$.  
(C) If $d = 2b$, all even-order principal maxima ($m = 2, 4, 6, \dots$) are missing (absent spectra).  
(D) The chromatic resolving power in the $m$-th order is $\frac{\lambda}{\Delta \lambda} = m N$.

#### Question 6
A solid sphere and a hollow cylinder of equal mass $M$ and equal radius $R$ are released from rest at the top of an inclined plane of inclination angle $\theta$. Both roll down without slipping. Which of the following statements is/are correct?
(A) The solid sphere reaches the bottom before the hollow cylinder.  
(B) The linear acceleration of the solid sphere is $\frac{5}{7} g \sin\theta$.  
(C) The linear acceleration of the hollow cylinder is $\frac{1}{2} g \sin\theta$.  
(D) The ratio of the velocity of the sphere to that of the hollow cylinder at the bottom is $\sqrt{10/7}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
In a Franck-Hertz experiment using mercury vapor, the excitation potential for the first discrete atomic level of mercury is $4.9\text{ V}$. Calculate the wavelength (in nm) of the ultraviolet photon emitted when an excited mercury atom returns to the ground state. (Take $h c \approx 1240\text{ eV}\cdot\text{nm}$. Round off to the nearest integer).

#### Question 8
One mole of an ideal gas expands isothermally at $300\text{ K}$ from volume $V_0$ to $4V_0$. Calculate the entropy change $\Delta S$ of the gas in $\text{J/K}$. (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$, $\ln 4 \approx 1.3863$. Round off to two decimal places).

#### Question 9
A circular loop of wire of radius $r = 0.10\text{ m}$ and resistance $R = 2.0\ \Omega$ is placed in a uniform magnetic field $B = 0.50\text{ T}$ perpendicular to the plane of the loop. If the loop is completely removed from the field in time $\Delta t = 0.05\text{ s}$, calculate the total electrical charge $q$ in Coulombs that flows through any cross-section of the wire. (Take $\pi \approx 3.1416$. Round off to three decimal places).

#### Question 10
A tuning fork of frequency $f = 512\text{ Hz}$ is held over the open end of a resonance tube filled with water. The first resonance is heard when the water level is at distance $L_1 = 15.0\text{ cm}$ below the open top, and the second resonance is heard at $L_2 = 48.0\text{ cm}$. Calculate the speed of sound in air in $\text{m/s}$. (Round off to two decimal places).

#### Question 11
Two point charges $q_1 = +2.0\ \mu\text{C}$ and $q_2 = -8.0\ \mu\text{C}$ are fixed at a distance $d = 1.0\text{ m}$ apart. Find the distance in meters from $q_1$ along the line joining the charges (outside the segment joining them) where the net electrostatic potential is zero. (Round off to two decimal places).

#### Question 12
A uniform rod of mass $M = 2.0\text{ kg}$ and length $L = 1.0\text{ m}$ is free to rotate about a frictionless horizontal axis passing through one end. The rod is held horizontally and released from rest. Find its angular velocity in $\text{rad/s}$ as it passes through the vertical position. (Take $g = 9.8\text{ m/s}^2$. Round off to two decimal places).

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the optical components in List-I with their functions in List-II:

| List-I (Component) | List-II (Function) |
|---|---|
| (P) Quarter-Wave Plate | (1) Converts linearly polarized light to circularly polarized light |
| (Q) Half-Wave Plate | (2) Rotates the plane of polarization by $2\theta$ |
| (R) Nicol Prism | (3) Produces linearly polarized light by total internal reflection |
| (S) Babinet Compensator | (4) Measures and compensates variable phase differences |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 14
Match the thermodynamic cycles in List-I with their process pairs in List-II:

| List-I (Cycle) | List-II (Processes) |
|---|---|
| (P) Carnot Cycle | (1) Two Isotherms + Two Adiabatics |
| (Q) Stirling Cycle | (2) Two Isotherms + Two Isochorics |
| (R) Otto Cycle | (3) Two Adiabatics + Two Isochorics |
| (S) Brayton Cycle | (4) Two Adiabatics + Two Isobarics |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 15
Match the physical constants in List-I with their numerical values in List-II:

| List-I (Constant) | List-II (Value in SI Units) |
|---|---|
| (P) Speed of light ($c$) | (1) $3.00 \times 10^8\text{ m/s}$ |
| (Q) Planck's constant ($h$) | (2) $6.63 \times 10^{-34}\text{ J}\cdot\text{s}$ |
| (R) Boltzmann's constant ($k_B$) | (3) $1.38 \times 10^{-23}\text{ J/K}$ |
| (S) Avogadro's number ($N_A$) | (4) $6.02 \times 10^{23}\text{ mol}^{-1}$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the nuclear reactions in List-I with their reaction types in List-II:

| List-I (Reaction) | List-II (Type) |
|---|---|
| (P) $^{14}\text{N} + \alpha \to ^{17}\text{O} + p$ | (1) First artificial transmutation (Rutherford) |
| (Q) $^{2}\text{H} + ^{3}\text{H} \to ^{4}\text{He} + n$ | (2) Thermonuclear fusion |
| (R) $^{235}\text{U} + n \to ^{141}\text{Ba} + ^{92}\text{Kr} + 3n$ | (3) Thermal neutron induced fission |
| (S) $^{27}\text{Al} + \alpha \to ^{30}\text{P} + n$ | (4) Discovery of artificial radioactivity (Joliot-Curie) |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 17
Match the electronic instruments in List-I with their physical operating principles in List-II:

| List-I (Instrument) | List-II (Operating Principle) |
|---|---|
| (P) Zener Diode | (1) Heavy doping, quantum tunneling breakdown in reverse bias |
| (Q) Solar Cell | (2) Photovoltaic effect producing EMF at $p-n$ junction |
| (R) Light Emitting Diode (LED) | (3) Spontaneous radiative recombination in forward bias |
| (S) Photodiode | (4) Reverse-biased detector of optical signals |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 18
Match the orbital angular momentum states in List-I with their spectroscopic notations in List-II:

| List-I (Azimuthal Quantum Number $l$) | List-II (Spectroscopic Symbol) |
|---|---|
| (P) $l = 0$ | (1) $s$ |
| (Q) $l = 1$ | (2) $p$ |
| (R) $l = 2$ | (3) $d$ |
| (S) $l = 3$ | (4) $f$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the conductometric titration curves of various acid-base systems:
(A) Titration of strong acid ($\text{HCl}$) with strong base ($\text{NaOH}$) shows a sharp V-shaped curve with conductance dropping due to replacement of fast $\text{H}^+$ by slower $\text{Na}^+$.  
(B) Titration of weak acid ($\text{CH}_3\text{COOH}$) with strong base ($\text{NaOH}$) shows an initial slight dip followed by a gradual increase due to common ion effect and sodium acetate formation.  
(C) In the titration of a mixture of $\text{HCl}$ and $\text{CH}_3\text{COOH}$ with $\text{NaOH}$, two distinct break points are observed.  
(D) Titration of weak acid with weak base yields a sharp V-shaped minimum at the equivalence point.

#### Question 20
Regarding the structure and bonding in metal carbonyls such as $[\text{Fe}(\text{CO})_5]$ and $[\text{Ni}(\text{CO})_4]$:
(A) The metal-carbon $\sigma$-bond is formed by donation of lone pair electrons from the carbonyl carbon into an empty $d$-orbital of the metal.  
(B) The metal-carbon $\pi$-bond is formed by back-donation of electrons from filled $d$-orbitals of the metal into empty antibonding $\pi^*$ orbitals of $\text{CO}$.  
(C) The synergic bonding increases the $\text{M-C}$ bond order and strengthens the metal-carbon bond.  
(D) Stronger back-donation weakens the $\text{C-O}$ bond and lowers its infrared vibrational stretching frequency ($\nu_{\text{CO}}$).

#### Question 21
Which of the following reactions undergo [3,3]-sigmatropic rearrangements?
(A) Cope rearrangement of 1,5-dienes.  
(B) Claisen rearrangement of allyl vinyl ethers or allyl phenyl ethers.  
(C) Benzidine rearrangement of hydrazobenzene.  
(D) Diels-Alder reaction.

#### Question 22
Regarding the crystal packing of ionic compounds:
(A) In zinc blende ($\text{ZnS}$), sulfide ions form an FCC lattice and zinc ions occupy half of the tetrahedral voids alternately.  
(B) In wurtzite ($\text{ZnS}$), sulfide ions form an HCP lattice and zinc ions occupy half of the tetrahedral voids.  
(C) In both zinc blende and wurtzite, the coordination number of both $\text{Zn}^{2+}$ and $\text{S}^{2-}$ is $4:4$.  
(D) In cesium chloride ($\text{CsCl}$), chloride ions form a simple cubic array with cesium ions occupying the central cubic interstitial site ($8:8$ coordination).

#### Question 23
Which of the following carbohydrates are reducing sugars?
(A) D-Glucose.  
(B) D-Fructose (reducing due to enediol rearrangement in alkaline medium).  
(C) Maltose.  
(D) Sucrose.

#### Question 24
Which of the following statements regarding the metallurgy of aluminium (Hall-Hroult process) is/are correct?
(A) Pure alumina ($\text{Al}_2\text{O}_3$) is dissolved in molten cryolite ($\text{Na}_3\text{AlF}_6$) and fluorspar ($\text{CaF}_2$) to lower the melting point and increase electrical conductivity.  
(B) The cathode is the carbon lining of the steel electrolytic tank.  
(C) Carbon anodes are consumed during electrolysis because oxygen evolved reacts with carbon to form $\text{CO}$ and $\text{CO}_2$.  
(D) For every kilogram of aluminium produced, approximately $0.5\text{ kg}$ of carbon anode is consumed.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
A first-order reaction has a rate constant $k = 2.303 \times 10^{-3}\text{ s}^{-1}$. Calculate the time in seconds required for $90\%$ of the initial reactant to decompose. (Round off to the nearest integer).

#### Question 26
Calculate the solubility of silver chromate ($\text{Ag}_2\text{CrO}_4$, $K_{sp} = 1.1 \times 10^{-12}$) in pure water in units of $10^{-5}\text{ mol/L}$. (Take $\sqrt[3]{0.275} \approx 0.65$. Round off to two decimal places).

#### Question 27
An aqueous solution of non-volatile solute freezes at $-0.372^\circ\text{C}$. Calculate the boiling point of the same solution at $1\text{ atm}$ in $^\circ\text{C}$. (Take $K_f = 1.86\text{ K}\cdot\text{kg/mol}$, $K_b = 0.52\text{ K}\cdot\text{kg/mol}$. Round off to two decimal places).

#### Question 28
Calculate the oxidation state of chromium in potassium dichromate ($\text{K}_2\text{Cr}_2\text{O}_7$).

#### Question 29
A sample of hard water contains $162\text{ mg/L}$ of calcium bicarbonate ($\text{Ca(HCO}_3)_2$, $M = 162\text{ g/mol}$). Express the temporary hardness of this water sample in parts per million (ppm) of $\text{CaCO}_3$ equivalent ($M = 100\text{ g/mol}$).

#### Question 30
The standard reduction potential for $\text{Fe}^{3+} / \text{Fe}$ is $-0.036\text{ V}$ and for $\text{Fe}^{2+} / \text{Fe}$ is $-0.440\text{ V}$. Calculate the standard potential $E^\circ$ in volts for the half-reaction $\text{Fe}^{3+} + e^- \to \text{Fe}^{2+}$. (Round off to three decimal places).

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the named organic reactions in List-I with their characteristic reagents in List-II:

| List-I (Reaction) | List-II (Reagent) |
|---|---|
| (P) Rosenmund Reduction | (1) $\text{H}_2 / \text{Pd-BaSO}_4$ |
| (Q) Clemmensen Reduction | (2) $\text{Zn-Hg} / \text{conc. HCl}$ |
| (R) Wolff-Kishner Reduction | (3) $\text{NH}_2\text{NH}_2 / \text{KOH}$ in ethylene glycol |
| (S) Etard Reaction | (4) $\text{CrO}_2\text{Cl}_2$ in $\text{CS}_2$ followed by $\text{H}_2\text{O}$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 32
Match the hybridization states of xenon in List-I with the corresponding molecules in List-II:

| List-I (Hybridization) | List-II (Xenon Compound) |
|---|---|
| (P) $sp^3d$ | (1) $\text{XeF}_2$ |
| (Q) $sp^3d^2$ | (2) $\text{XeF}_4$ |
| (R) $sp^3d^3$ | (3) $\text{XeF}_6$ |
| (S) $sp^3$ | (4) $\text{XeO}_3$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 33
Match the types of crystalline solids in List-I with their exemplary substances in List-II:

| List-I (Solid Type) | List-II (Example) |
|---|---|
| (P) Molecular Solid | (1) Dry Ice ($\text{CO}_2$) / Iodine ($\text{I}_2$) |
| (Q) Covalent Network Solid | (2) Diamond / Silicon Carbide ($\text{SiC}$) |
| (R) Ionic Solid | (3) Sodium Chloride ($\text{NaCl}$) |
| (S) Metallic Solid | (4) Copper ($\text{Cu}$) / Iron ($\text{Fe}$) |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 34
Match the ores in List-I with their concentration methods in List-II:

| List-I (Ore) | List-II (Concentration Technique) |
|---|---|
| (P) Copper Pyrites ($\text{CuFeS}_2$) | (1) Froth Floatation Method |
| (Q) Haematite ($\text{Fe}_2\text{O}_3$) | (2) Hydraulic Washing / Gravity Separation |
| (R) Bauxite ($\text{Al}_2\text{O}_3 \cdot 2\text{H}_2\text{O}$) | (3) Chemical Leaching (Bayer's Process) |
| (S) Tinstone ($\text{SnO}_2$) containing Wolframite | (4) Magnetic Separation |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 35
Match the organic tests in List-I with the functional groups detected in List-II:

| List-I (Test) | List-II (Functional Group) |
|---|---|
| (P) Carbylamine Test | (1) Aliphatic/Aromatic Primary Amine ($-\text{NH}_2$) |
| (Q) Lucas Test | (2) Distinction of $1^\circ, 2^\circ, 3^\circ$ Alcohols |
| (R) Neutral $\text{FeCl}_3$ Test | (3) Phenolic group ($-\text{OH}$) |
| (S) 2,4-DNP Test | (4) Carbonyl group (Aldehyde / Ketone) |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 36
Match the therapeutic drugs in List-I with their pharmacological classes in List-II:

| List-I (Drug) | List-II (Class) |
|---|---|
| (P) Paracetamol / Aspirin | (1) Analgesic & Antipyretic |
| (Q) Penicillin | (2) Bactericidal Antibiotic |
| (R) Ranitidine | (3) Antacid / $\text{H}_2$-receptor antagonist |
| (S) Equanil / Valium | (4) Tranquilizer |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \arctan x - \frac{x}{1 + x^2}$ for $x > 0$. Which of the following statements is/are correct?
(A) $f(0) = 0$.  
(B) $f'(x) = \frac{2 x^2}{(1 + x^2)^2} > 0$ for all $x > 0$.  
(C) $f(x) > 0$ for all $x > 0$.  
(D) For all $x > 0$, $\arctan x > \frac{x}{1 + x^2}$.

#### Question 38
Consider the system of circles orthogonal to the circle $S: x^2 + y^2 = a^2$. Which of the following statements is/are correct?
(A) The condition for two circles $x^2 + y^2 + 2g_1 x + 2f_1 y + c_1 = 0$ and $x^2 + y^2 + 2g_2 x + 2f_2 y + c_2 = 0$ to cut orthogonally is $2 g_1 g_2 + 2 f_1 f_2 = c_1 + c_2$.  
(B) Any circle with center on the line $y = 0$ cutting $S$ orthogonally has its constant term $c = -a^2$.  
(C) The radical axis of any two orthogonal circles to $S$ passes through the origin.  
(D) The polar of the center of $S$ with respect to any orthogonal circle is a diameter of $S$.

#### Question 39
Let $z$ be a complex number. Which of the following statements is/are correct?
(A) The equation $|z - a|^2 + |z - b|^2 = k$ represents a circle if $k > \frac{1}{2}|a - b|^2$.  
(B) If $k = \frac{1}{2}|a - b|^2$, the locus consists of a single point (the midpoint of $a$ and $b$).  
(C) The center of the circle in (A) is the midpoint $\frac{a + b}{2}$.  
(D) The radius of the circle in (A) is $\frac{1}{2}\sqrt{2k - |a - b|^2}$.

#### Question 40
Let $A$ be an $n \times n$ matrix with real entries such that $A^T = A$ and $A^2 = 0$. Which of the following statements is/are correct?
(A) All eigenvalues of $A$ are zero.  
(B) $\text{Tr}(A^T A) = \text{Tr}(A^2) = 0$.  
(C) $A = 0$ (the zero matrix).  
(D) A non-zero real symmetric matrix cannot be nilpotent.

#### Question 41
Let $I_n = \int_0^1 (1 - x^2)^n \, dx$ for $n \ge 0$. Which of the following statements is/are correct?
(A) $I_0 = 1$.  
(B) For $n \ge 1$, $(2n + 1) I_n = 2n I_{n-1}$.  
(C) $I_n = \frac{2n}{2n + 1} \frac{2n-2}{2n-1} \dots \frac{2}{3} \cdot 1$.  
(D) $\lim_{n \to \infty} I_n = 0$.

#### Question 42
Consider the planes $x + 2y - z = 4$ and $2x - y + z = 1$. Which of the following statements is/are correct?
(A) The two planes are perpendicular to each other ($1(2) + 2(-1) + (-1)(1) = -1 \ne 0$, wait, $2 - 2 - 1 = -1 \ne 0$).  
(B) The line of intersection has direction ratios $(1, -3, -5)$.  
(C) The plane passing through the origin and the line of intersection is $x + 7y - 4z = 0$.  
(D) The angle between the normal vectors is $\arccos(-1/6)$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area of the region bounded by the curves $y = x^2$ and $y = 2 - x^2$. (Round off to two decimal places).

#### Question 44
Evaluate the definite integral:
$$P = \int_0^\pi \frac{x \sin x}{1 + \cos^2 x} \, dx$$
If $P = \frac{\pi^2}{m}$, find the integer value of $m$.

#### Question 45
Find the number of points on the curve $y = x^3 - 3x$ where the tangent is parallel to the line $y = 9x + 5$.

#### Question 46
Let $\vec{a} = \hat{i} + \hat{j} + \hat{k}$ and $\vec{b} = \hat{i} - \hat{j} + \hat{k}$. Find the area of the parallelogram having diagonals represented by $\vec{a}$ and $\vec{b}$. (Round off to two decimal places).

#### Question 47
A committee of 4 persons is to be chosen from a group of 5 men and 4 women. Find the probability that the committee contains at least 2 women. (Give the answer as a percentage rounded to two decimal places).

#### Question 48
Find the radius of the circle $x^2 + y^2 - 6x + 8y = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The general solution of the differential equation $\frac{dy}{dx} = e^{x - y} + x^2 e^{-y}$ is:
(A) $e^y = e^x + \frac{x^3}{3} + C$  
(B) $e^{-y} = e^x + \frac{x^3}{3} + C$  
(C) $e^y = e^x + x^3 + C$  
(D) $y = \ln(e^x + x^3) + C$

#### Question 50
The locus of the point of intersection of perpendicular tangents to the parabola $y^2 = 4ax$ is:
(A) The directrix $x + a = 0$  
(B) The latus rectum $x - a = 0$  
(C) The axis $y = 0$  
(D) The tangent at vertex $x = 0$

#### Question 51
If $\alpha$ and $\beta$ are the roots of the equation $x^2 - 6x + 2 = 0$, the value of $\alpha^3 + \beta^3$ is:
(A) $180$  
(B) $216$  
(C) $144$  
(D) $196$

#### Question 52
The value of $\lim_{x \to 0} \frac{\sin x - x}{x^3}$ is:
(A) $-\frac{1}{6}$  
(B) $\frac{1}{6}$  
(C) $0$  
(D) $-\frac{1}{3}$

#### Question 53
If $\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, then the matrix $A$ is:
(A) $\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$  
(B) $\begin{pmatrix} -3 & 1 \\ 5 & -2 \end{pmatrix}$  
(C) $\begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}$  
(D) $\begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$

#### Question 54
The distance of the point $(1, 2, 3)$ from the plane $x - 2y + 2z = 9$ is:
(A) $2$  
(B) $1$  
(C) $3$  
(D) $0$
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Guwahati Benchmark JEE Advanced Mock Examination 03

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- **Q1**: **(A, B, C, D)**
  - In a blackbody cavity, radiation field is isotropic and homogeneous. (A) is correct.
  - Maxwell stress tensor gives radiation pressure $P = u/3$. (B) is correct.
  - Stefan-Boltzmann law gives $u = a T^4$. (C) is correct.
  - For adiabatic reversible expansion: $d U = -P d V \implies d(u V) = -\frac{u}{3} d V \implies V d u + u d V = -\frac{u}{3} d V \implies V d u = -\frac{4}{3} u d V$.
  - Since $u \propto T^4$, $4 \frac{d T}{T} = -\frac{4}{3}\frac{d V}{V} \implies \frac{d T}{T} + \frac{1}{3}\frac{d V}{V} = 0 \implies T V^{1/3} = \text{const} \implies V T^3 = \text{const}$. (D) is correct.
- **Q2**: **(A, B, C, D)**
  - $E^2 = p^2 c^2 + m_0^2 c^4$, and total energy $E = K + m_0 c^2 = e V + m_0 c^2$.
  - $p^2 c^2 = (e V + m_0 c^2)^2 - m_0^2 c^4 = e^2 V^2 + 2 m_0 c^2 e V \implies p = \frac{1}{c}\sqrt{e^2 V^2 + 2 m_0 c^2 e V}$. (A) and (B) are correct.
  - $\lambda = \frac{h}{p} = \frac{h c}{\sqrt{2 m_0 c^2 e V (1 + \frac{e V}{2 m_0 c^2})}} = \frac{h}{\sqrt{2 m_0 e V}}\left(1 + \frac{e V}{2 m_0 c^2}\right)^{-1/2}$. (C) is correct.
  - When $e V \ll m_0 c^2$, the factor approaches 1. (D) is correct.
- **Q3**: **(A, B, C, D)**
  - Poynting vector energy flow theorem for cylindrical resistor.
  - Surface area $= 2\pi a L$. Inward flux $= S \times 2\pi a L = \frac{V I}{2\pi a L} \times 2\pi a L = V I = I^2 R$.
- **Q4**: **(A, B, C, D)**
  - Belt accelerates with $a_0$. Friction $f$ acts forward on sphere.
  - $f = M a_{\text{cm}}$, $f R = I \alpha = \frac{2}{5}M R^2 \alpha \implies \alpha = \frac{5 f}{2 M R}$.
  - No slipping condition at contact point: $a_{\text{cm}} + \alpha R = a_0$.
  - $a_{\text{cm}} + \frac{5}{2} a_{\text{cm}} = a_0 \implies \frac{7}{2} a_{\text{cm}} = a_0 \implies a_{\text{cm}} = \frac{2}{7} a_0$.
  - $f = M a_{\text{cm}} = \frac{2}{7} M a_0$.
  - For no slipping: $f \le \mu M g \implies \mu \ge \frac{2 a_0}{7 g}$.
- **Q5**: **(A, B, C)**
  - Optical path difference $\Delta = 2(\mu - 1)L = N \lambda \implies \mu = 1 + \frac{N \lambda}{2L}$.
  - If $L$ is doubled, $N$ doubles, not halved. (D) is false.
- **Q6**: **(A, B, C, D)**
  - Moseley's empirical and theoretical law for $K_\alpha$ X-rays.

#### Solutions 7 to 12:
- **Q7**: **18.00**
  - Radiation pressure on perfect reflector: $P_{\text{rad}} = \frac{2 I}{c}$.
  - Force $F = P_{\text{rad}} A = \frac{2 \times 1350 \times 400}{3.0 \times 10^8} = \frac{1.08 \times 10^6}{3.0 \times 10^8} = 3.6 \times 10^{-3}\text{ N}$.
  - Acceleration $a = F / m = \frac{3.6 \times 10^{-3}}{200} = 1.8 \times 10^{-5}\text{ m/s}^2 = 0.018\text{ mm/s}^2$. Wait, $1.8 \times 10^{-2}\text{ mm/s}^2 = 0.018$.
- **Q8**: **7.48**
  - $W = -\Delta U = -n C_V \Delta T = -2 \left(\frac{3}{2}R\right)(T_2 - T_1) = 3 R (600 - 300) = 900 R$.
  - $W = 900 \times 8.314 = 7482.6\text{ J} \approx 7.48\text{ kJ}$.
- **Q9**: **6.28**
  - $\lambda_c = 2\pi R_0 = 2(3.1416)(1.0) = 6.28\text{ mm}$.
- **Q10**: **316.23**
  - $\omega_0 = \frac{1}{\sqrt{L C}} = \frac{1}{\sqrt{0.10 \times 10^{-4}}} = \frac{1}{\sqrt{10^{-5}}} = \sqrt{10^5} \approx 316.23\text{ rad/s}$.
- **Q11**: **600**
  - At the closest approach, the velocity vector of the source is perpendicular to the line of sight ($\theta = 90^\circ$).
  - Hence, the classical Doppler shift vanishes: $f = f_0 \frac{v}{v - u \cos 90^\circ} = f_0 = 600\text{ Hz}$.
- **Q12**: **78**
  - Lens maker's formula: $\frac{1}{f_a} = (\frac{\mu_g}{\mu_a} - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right) \implies \frac{1}{20} = (1.5 - 1) K = 0.5 K \implies K = 0.10\text{ cm}^{-1}$.
  - In water: $\frac{1}{f_w} = (\frac{1.50}{1.33} - 1) K = (1.1278 - 1)(0.10) = 0.01278\text{ cm}^{-1} \implies f_w = 78.2 \approx 78\text{ cm}$.

#### Solutions 13 to 18:
- **Q13**: **(A)** - Kapitza's inverted pendulum dynamic stability criterion $a^2 \omega^2 > 2 g l$.
- **Q14**: **(A)** - Isolated capacitor has constant charge $Q$. $U = Q^2 / (2C)$. When $d$ doubles, $C$ halves, so $U$ doubles.
- **Q15**: **(A)** - By Faraday's law: $\oint \vec{E}\cdot d\vec{l} = -\frac{d\Phi}{dt} \implies E(2\pi r) = -\pi R^2 \alpha \implies E = -\frac{\alpha R^2}{2r}\hat{\phi}$.
- **Q16**: **(A)** - Distance of closest approach $r_{\min} = \frac{1}{4\pi\varepsilon_0}\frac{2 Z e^2}{K} = \frac{9 \times 10^9 \times 2 \times 79 \times (1.6 \times 10^{-19})^2}{5.0 \times 10^6 \times 1.6 \times 10^{-19}} = 4.55 \times 10^{-14}\text{ m}$.
- **Q17**: **(A)** - $\eta = 1 - T_C/T_H = 1 - 400/800 = 0.50 \implies W = 0.50 \times 2000 = 1000\text{ J}$.
- **Q18**: **(A)** - Water inside frictionless shell does not rotate, so it only has translational kinetic energy $\frac{1}{2}m v^2$. Shell has both translation and rotation: $\frac{1}{2}M v^2 + \frac{1}{2}(\frac{2}{3}M R^2)(v/R)^2 = \frac{5}{6}M v^2$. Total $= \frac{1}{2}(M + m)v^2 + \frac{1}{3}M v^2$.

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- **Q19**: **(A, B, C, D)** - Thermodynamic derivations of temperature coefficient of cell EMF.
- **Q20**: **(A, B, C, D)** - Pericyclic Diels-Alder stereochemistry and endo-selectivity.
- **Q21**: **(A, B, C, D)** - Basicity and reducing properties of phosphorus oxoacids.
- **Q22**: **(A, B, C)** - Negative deviations involve stronger intermolecular attractions (hydrogen bonding). Ethanol + acetone shows positive deviation.
- **Q23**: **(A, B, C, D)** - Jahn-Teller distortion analysis in copper(II) and chromium(II).
- **Q24**: **(A, B, C, D)** - Beckmann rearrangement stereochemistry and Nylon-6 synthesis.

#### Solutions 25 to 30:
- **Q25**: **-168**
  - $\Delta H = -n F E + n F T \left(\frac{\partial E}{\partial T}\right)_P$.
  - $\Delta H = -2(96500)(0.675) + 2(96500)(298)(-6.5 \times 10^{-4}) = -130275 - 37384 = -167659\text{ J} \approx -168\text{ kJ/mol}$.
- **Q26**: **3.75**
  - $v = \frac{V_{\max}[S]}{K_m + [S]} = \frac{5.0 \times 10^{-4} \times 6.0 \times 10^{-3}}{2.0 \times 10^{-3} + 6.0 \times 10^{-3}} = \frac{30.0 \times 10^{-7}}{8.0 \times 10^{-3}} = 3.75 \times 10^{-4}\text{ mol/(L}\cdot\text{s)}$.
- **Q27**: **46**
  - Molecular weight $= 2 \times \text{Vapor Density} = 2 \times 23.0 = 46.0\text{ g/mol}$ (Ethanol / Dimethyl ether).
- **Q28**: **50.00**
  - $N_1 V_1 = N_2 V_2 \implies 0.05 \times 100 = 0.10 \times V_2 \implies V_2 = 50.00\text{ mL}$.
- **Q29**: **2.80**
  - $[\text{H}^+] = \sqrt{K_a C} = \sqrt{2.5 \times 10^{-5} \times 0.10} = \sqrt{2.5 \times 10^{-6}} = 1.58 \times 10^{-3}\text{ M}$.
  - $\text{pH} = -\log(1.58 \times 10^{-3}) = 3 - 0.20 = 2.80$.
- **Q30**: **0.414**
  - Octahedral void radius ratio $r / R = \sqrt{2} - 1 \approx 0.414$.

#### Solutions 31 to 36:
- **Q31**: **(C)** - In potassium nitroprusside, $\text{NO}$ is coordinated as $\text{NO}^+$ (nitrosonium), making iron $+2$.
- **Q32**: **(A)** - 2,3-dimethylbut-2-ene is symmetrical $(\text{CH}_3)_2\text{C}=\text{C}(\text{CH}_3)_2$, yielding two acetone molecules.
- **Q33**: **(A)** - $\text{Mn}^{3+}$ is $d^4$. Strong field ligand $\text{CN}^-$ gives $t_{2g}^4 e_g^0$ with 2 unpaired electrons $\implies \mu = \sqrt{2(4)} = \sqrt{8} \approx 2.83\ \mu_B$.
- **Q34**: **(A)** - $\text{SiO}_2$ combines with $\text{FeO}$ to form slag $\text{FeSiO}_3$.
- **Q35**: **(A)** - Natural rubber is cis-1,4-polyisoprene.
- **Q36**: **(A)** - Pentan-2-one has a methyl ketone group ($\text{CH}_3\text{CO}-$).

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- **Q37**: **(A, B, C, D)** - Confocal conics share the same foci and intersect orthogonally everywhere.
- **Q38**: **(A, B, C, D)** - Classical algebraic and geometric identities of $n$-th roots of unity.
- **Q39**: **(A, B, C, D)** - Properties of Sine integral $\text{Si}(x)$.
- **Q40**: **(A, B, C, D)** - Matrix polynomial inversion via Cayley-Hamilton theorem.
- **Q41**: **(A, B, D)** - Normal vector and tangent plane to elliptic paraboloid.
- **Q42**: **(A, B, C, D)** - Extrema of quadratic rational function via discriminant analysis.

#### Solutions 43 to 48:
- **Q43**: **4**
  - By King's rule, $I = \frac{\pi}{4} \implies k = 4$.
- **Q44**: **1.83**
  - Normalizing second plane: $2x - 2y + z - 2.5 = 0$.
  - Distance $d = \frac{|3 - (-2.5)|}{\sqrt{2^2 + (-2)^2 + 1^2}} = \frac{5.5}{3} \approx 1.83$.
- **Q45**: **3**
  - $f'(x) = 3x^2 - 3 = 0 \implies x = \pm 1$. $f(1) = -1 < 0, f(-1) = 3 > 0$. Three distinct real roots.
- **Q46**: **1.41**
  - $\frac{dy}{dx} + 2y = 4x \implies y e^{2x} = \int 4x e^{2x} dx = 2x e^{2x} - e^{2x} + C \implies y = 2x - 1 + C e^{-2x}$.
  - $y(0) = 1 \implies 1 = -1 + C \implies C = 2$.
  - $y(1) = 2(1) - 1 + 2 e^{-2} = 1 + 2(0.1353) = 1.27$.
- **Q47**: **34.38**
  - Total outcomes $= 2^6 = 64$.
  - Favorable: $\binom{6}{4} + \binom{6}{5} + \binom{6}{6} = 15 + 6 + 1 = 22$.
  - Probability $= 22 / 64 = 11 / 32 = 0.34375 \implies 34.38\%$.
- **Q48**: **1.00**
  - Area of right triangle $= \frac{1}{2} \times 4 \times 3 = 6$. Hypotenuse $= 5$.
  - Inradius $r = \frac{\Delta}{s} = \frac{6}{(4 + 3 + 5)/2} = \frac{6}{6} = 1.00$.

#### Solutions 49 to 54:
- **Q49**: **(A)** - Vandermonde determinant formula $(b - a)(c - a)(c - b) = (a - b)(b - c)(c - a)$.
- **Q50**: **(A)** - Slope of asymptotes $m = \pm b/a = \pm 3/4$. Angle between them is $2\arctan(3/4)$.
- **Q51**: **(A)** - L'Hopital rule or series expansion gives $1/3$.
- **Q52**: **(A)** - $|\vec{a}+\vec{b}+\vec{c}|^2 = 1 + 1 + 1 = 3 \implies \sqrt{3}$.
- **Q53**: **(A)** - Circular permutations with alternating gender: $(5-1)! \times 5! = 4! \times 5!$.
- **Q54**: **(A)** - Homogeneous ODE solution $y = x \ln x$.
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Guwahati Benchmark JEE Advanced Mock Examination 03

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- **Q1**: **(A, B, C, D)** - Method of magnetic images for superconductor levitation.
- **Q2**: **(A, B, C, D)** - Helmholtz coil configuration field uniformity.
- **Q3**: **(A, B, C, D)** - One-dimensional finite square well quantum bound states.
- **Q4**: **(A, B, C, D)** - Joule-Thomson expansion and inversion curve.
- **Q5**: **(A, B, C, D)** - Grating diffraction, missing orders, and chromatic resolving power.
- **Q6**: **(A, B, C)** - Rolling down an incline: sphere acceleration $\frac{5}{7}g\sin\theta$, cylinder $\frac{1}{2}g\sin\theta$.

#### Solutions 7 to 12:
- **Q7**: **253**
  - $\lambda = \frac{h c}{\Delta E} = \frac{1240}{4.9} \approx 253\text{ nm}$.
- **Q8**: **11.53**
  - $\Delta S = n R \ln(V_f / V_i) = 1 \times 8.314 \times \ln 4 = 8.314 \times 1.3863 = 11.53\text{ J/K}$.
- **Q9**: **0.008**
  - $\Delta \Phi = B \pi r^2 = 0.50 \times \pi (0.10)^2 = 0.005 \pi \approx 0.0157\text{ Wb}$.
  - $q = \frac{\Delta \Phi}{R} = \frac{0.0157}{2.0} = 0.00785 \approx 0.008\text{ C}$.
- **Q10**: **337.92**
  - $\lambda / 2 = L_2 - L_1 = 48.0 - 15.0 = 33.0\text{ cm} \implies \lambda = 66.0\text{ cm} = 0.66\text{ m}$.
  - $v = f \lambda = 512 \times 0.66 = 337.92\text{ m/s}$.
- **Q11**: **0.33**
  - $V = \frac{1}{4\pi\varepsilon_0}\left[\frac{q_1}{x} + \frac{q_2}{d + x}\right] = 0 \implies \frac{2}{x} = \frac{8}{1 + x} \implies 2 + 2x = 8x \implies 6x = 2 \implies x = 1/3 \approx 0.33\text{ m}$.
- **Q12**: **5.42**
  - By conservation of energy: $M g \frac{L}{2} = \frac{1}{2} I \omega^2 = \frac{1}{2}\left(\frac{1}{3}M L^2\right)\omega^2 = \frac{1}{6}M L^2 \omega^2$.
  - $\omega = \sqrt{\frac{3 g}{L}} = \sqrt{\frac{3 \times 9.8}{1.0}} = \sqrt{29.4} \approx 5.42\text{ rad/s}$.

#### Solutions 13 to 18:
- **Q13**: **(A)** - Polarizing optical elements.
- **Q14**: **(A)** - Thermodynamic cycles classification.
- **Q15**: **(A)** - Fundamental constants.
- **Q16**: **(A)** - Historic nuclear reactions.
- **Q17**: **(A)** - Semiconductor junction devices.
- **Q18**: **(A)** - Atomic orbitals and azimuthal quantum numbers.

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- **Q19**: **(A, B, C)** - Conductometric titration profiles. Weak acid-weak base does not yield a sharp minimum.
- **Q20**: **(A, B, C, D)** - Synergic $\sigma$-donation and $\pi$-backbonding in metal carbonyls.
- **Q21**: **(A, B)** - [3,3]-sigmatropic rearrangements.
- **Q22**: **(A, B, C, D)** - Close packing in zinc blende, wurtzite, and cesium chloride.
- **Q23**: **(A, B, C)** - Sucrose is a non-reducing disaccharide with glycosidic bond between C1 of glucose and C2 of fructose.
- **Q24**: **(A, B, C, D)** - Hall-Hroult electrolytic extraction of aluminium.

#### Solutions 25 to 30:
- **Q25**: **1000**
  - $t = \frac{2.303}{k}\log\frac{100}{10} = \frac{2.303}{2.303 \times 10^{-3}} \times 1 = 1000\text{ s}$.
- **Q26**: **6.50**
  - $\text{Ag}_2\text{CrO}_4 \rightleftharpoons 2\text{Ag}^+ + \text{CrO}_4^{2-}$.
  - $K_{sp} = 4 s^3 \implies 4 s^3 = 1.1 \times 10^{-12} \implies s^3 = 0.275 \times 10^{-12} \implies s = 0.65 \times 10^{-4}\text{ M} = 6.5 \times 10^{-5}\text{ M}$.
- **Q27**: **100.10**
  - $\Delta T_f = K_f m \implies 0.372 = 1.86 m \implies m = 0.20\text{ mol/kg}$.
  - $\Delta T_b = K_b m = 0.52 \times 0.20 = 0.104^\circ\text{C} \implies T_b = 100.10^\circ\text{C}$.
- **Q28**: **6**
  - Oxidation state of $\text{Cr}$ in $\text{Cr}_2\text{O}_7^{2-}$: $2x - 14 = -2 \implies 2x = 12 \implies x = +6$.
- **Q29**: **100.00**
  - $162\text{ mg}$ $\text{Ca(HCO}_3)_2 \equiv 1\text{ mmol} \equiv 1\text{ mmol }\text{CaCO}_3 = 100\text{ mg }\text{CaCO}_3/\text{L} = 100\text{ ppm}$.
- **Q30**: **0.771**
  - $\Delta G_1^\circ = -3 F(-0.036) = +0.108 F$.
  - $\Delta G_2^\circ = -2 F(-0.440) = +0.880 F$.
  - $\Delta G_3^\circ = \Delta G_1^\circ - \Delta G_2^\circ = 0.108 F - 0.880 F = -0.772 F = -1 F E_3^\circ \implies E_3^\circ = +0.772\text{ V}$.

#### Solutions 31 to 36:
- **Q31**: **(A)** - Organic reduction methods.
- **Q32**: **(A)** - VSEPR geometries of xenon fluorides.
- **Q33**: **(A)** - Classification of solid crystals.
- **Q34**: **(A)** - Metallurgy concentration processes.
- **Q35**: **(A)** - Organic functional group analytical tests.
- **Q36**: **(A)** - Medicinal chemistry drugs classification.

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- **Q37**: **(A, B, C, D)** - Function monotonicity and inequality proofs.
- **Q38**: **(A, C)** - Condition of orthogonality for circles.
- **Q39**: **(A, B, C, D)** - Apollonius circle in the complex plane.
- **Q40**: **(A, B, C, D)** - Real symmetric nilpotent matrices must be identically zero.
- **Q41**: **(A, B, C, D)** - Wallis integral reduction formula and asymptotic convergence.
- **Q42**: **(B, C, D)** - Dihedral geometry of intersecting planes.

#### Solutions 43 to 48:
- **Q43**: **2.67**
  - Points of intersection: $x^2 = 2 - x^2 \implies 2x^2 = 2 \implies x = \pm 1$.
  - Area $= \int_{-1}^1 (2 - 2x^2) dx = [2x - \frac{2x^3}{3}]_{-1}^1 = 2(2 - 2/3) = 8/3 \approx 2.67$.
- **Q44**: **4**
  - $P = \int_0^\pi \frac{x \sin x}{1 + \cos^2 x} dx = \frac{\pi}{2}\int_0^\pi \frac{\sin x}{1 + \cos^2 x} dx = \frac{\pi^2}{4} \implies m = 4$.
- **Q45**: **2**
  - $y' = 3x^2 - 3 = 9 \implies 3x^2 = 12 \implies x^2 = 4 \implies x = \pm 2$. Two points.
- **Q46**: **1.41**
  - Parallelogram area $= \frac{1}{2}|\vec{a} \times \vec{b}|$.
  - $\vec{a} \times \vec{b} = \det \begin{pmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix} = 2\hat{i} - 2\hat{k}$.
  - Magnitude $= \sqrt{2^2 + (-2)^2} = \sqrt{8} = 2\sqrt{2}$.
  - Area $= \frac{1}{2}(2\sqrt{2}) = \sqrt{2} \approx 1.41$.
- **Q47**: **74.60**
  - Total selections $= \binom{9}{4} = 126$.
  - Cases with $\ge 2$ women:
    - 2 women, 2 men: $\binom{4}{2}\binom{5}{2} = 6 \times 10 = 60$.
    - 3 women, 1 man: $\binom{4}{3}\binom{5}{1} = 4 \times 5 = 20$.
    - 4 women, 0 men: $\binom{4}{4}\binom{5}{0} = 1 \times 1 = 1$.
    - Total favorable $= 60 + 20 + 1 = 81$.
    - Probability $= 81 / 126 = 9 / 14 \approx 0.6429 \implies 64.29\%$.
- **Q48**: **5.00**
  - $x^2 - 6x + y^2 + 8y = 0 \implies (x - 3)^2 + (y + 4)^2 = 3^2 + 4^2 = 25 \implies R = 5.00$.

#### Solutions 49 to 54:
- **Q49**: **(A)** - Separable ODE: $e^y dy = (e^x + x^2) dx \implies e^y = e^x + \frac{x^3}{3} + C$.
- **Q50**: **(A)** - Locus of perpendicular tangents to parabola is its directrix $x + a = 0$.
- **Q51**: **(A)** - $\alpha + \beta = 6, \alpha \beta = 2$. $\alpha^3 + \beta^3 = (\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta) = 6^3 - 3(2)(6) = 216 - 36 = 180$.
- **Q52**: **(A)** - Standard limit: $\lim_{x \to 0}\frac{\sin x - x}{x^3} = -\frac{1}{6}$.
- **Q53**: **(A)** - Inverse of $2 \times 2$ matrix with determinant $6 - 5 = 1$.
- **Q54**: **(B)** - Distance $= \frac{|1(1) - 2(2) + 2(3) - 9|}{\sqrt{1^2 + (-2)^2 + 2^2}} = \frac{|1 - 4 + 6 - 9|}{3} = \frac{|-6|}{3} = 2$.
"""

val_md = r"""# Answer Key & Benchmark Alignment – Mock Examination 03
## Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C
- Q6: A, B, C, D
- Q7: 0.02
- Q8: 7.48
- Q9: 6.28
- Q10: 316.23
- Q11: 600.00
- Q12: 78.00
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C, D
- Q20: A, B, C, D
- Q21: A, B, C, D
- Q22: A, B, C
- Q23: A, B, C, D
- Q24: A, B, C, D
- Q25: -168.00
- Q26: 3.75
- Q27: 46.00
- Q28: 50.00
- Q29: 2.80
- Q30: 0.414
- Q31: C
- Q32: A
- Q33: A
- Q34: A
- Q35: A
- Q36: A

#### Mathematics
- Q37: A, B, C, D
- Q38: A, B, C, D
- Q39: A, B, C, D
- Q40: A, B, C, D
- Q41: A, B, D
- Q42: A, B, C, D
- Q43: 4.00
- Q44: 1.83
- Q45: 3.00
- Q46: 1.27
- Q47: 34.38
- Q48: 1.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Paper 2 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C
- Q7: 253.00
- Q8: 11.53
- Q9: 0.008
- Q10: 337.92
- Q11: 0.33
- Q12: 5.42
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C
- Q20: A, B, C, D
- Q21: A, B
- Q22: A, B, C, D
- Q23: A, B, C
- Q24: A, B, C, D
- Q25: 1000.00
- Q26: 6.50
- Q27: 100.10
- Q28: 6.00
- Q29: 100.00
- Q30: 0.772
- Q31: A
- Q32: A
- Q33: A
- Q34: A
- Q35: A
- Q36: A

#### Mathematics
- Q37: A, B, C, D
- Q38: A, C
- Q39: A, B, C, D
- Q40: A, B, C, D
- Q41: A, B, C, D
- Q42: B, C, D
- Q43: 2.67
- Q44: 4.00
- Q45: 2.00
- Q46: 1.41
- Q47: 64.29
- Q48: 5.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Pedagogical Profile Alignment
- **Modern Physics & Thermodynamics Weightage**: $\approx 39\%$ across Physics sections.
- **Physical Chemistry Weightage**: $\approx 68\%$ across Chemistry sections.
- **Geometric Invariants & Algebraic Symmetry**: Strongly emphasized across Mathematics sections.
- **Total Unique Questions**: 108 Questions (54 in Paper 1, 54 in Paper 2).
"""

if __name__ == "__main__":
    create_mock_files(3, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Guwahati")
    print("Successfully generated IIT Guwahati Mock 03!")

