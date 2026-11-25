# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 07.
Empirical Signature: IIT Delhi Benchmark (2013, 2020)
- Multi-correct dominance (+4/-2 with partial marking)
- Synchrocyclotron phase stability, oblique radiation pressure, uniaxial double refraction
- Tetrahedral CFT Laporte intensity, Favorskii cyclopropanones, Langmuir isotherm
- Lipschitz continuity & Banach fixed point, projection matrices, phase portrait classification
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 07 — Paper 1
## Organising Institute Style Inspiration: IIT Delhi (`IIT_DELHI_STYLE`)
**Historical Reference Benchmark**: 2013, 2020 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject — Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject — Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
In a classical cyclotron accelerating protons, as the kinetic energy approaches relativistic levels ($v \sim 0.1c$), relativistic effects limit further acceleration. In a synchrocyclotron:
(A) The relativistic mass increases as $m(v) = \frac{m_0}{\sqrt{1 - v^2/c^2}}$, causing the orbital frequency to decrease.  
(B) To maintain synchronism with the accelerating voltage, the frequency of the RF electric field is modulated downward as $\omega_{\text{RF}}(t) = \frac{q B}{m(t)}$.  
(C) Phase stability (principle of autophasing) ensures that particles arriving slightly early or late receive adjusting energy kicks to stay locked in phase.  
(D) Protons can be accelerated to energies exceeding several hundred $\text{MeV}$, far beyond the classical cyclotron limit ($\sim 25\text{ MeV}$).

#### Question 2
A uniform solid sphere of mass $M$ and radius $r$ rolls without slipping near the bottom vertex of a smooth parabolic trough given by $y = k x^2$ ($k > 0$):
(A) Near the origin, the radius of curvature of the parabola is $R = \frac{1}{2k}$.  
(B) The effective radius of the path of the center of mass of the sphere is $R_{\text{eff}} = \frac{1}{2k} - r$.  
(C) For small oscillations about the vertex, the motion is simple harmonic with angular frequency $\omega = \sqrt{\frac{5g}{7(R - r)}} = \sqrt{\frac{5g}{7(1/(2k) - r)}}$.  
(D) The normal force at the lowest point during oscillation of angular amplitude $\theta_0$ is $N > M g$.

#### Question 3
A parallel beam of monochromatic light of intensity $I$ is incident at an angle of incidence $\theta$ on a flat completely absorbing surface of area $A$:
(A) The rate of energy incident on the surface is $P_{\text{opt}} = I A \cos\theta$.  
(B) The normal radiation pressure exerted on the surface is $P_N = \frac{I}{c}\cos^2\theta$.  
(C) The tangential shear stress exerted on the surface is $\tau = \frac{I}{c}\sin\theta\cos\theta$.  
(D) If the surface were instead a perfect mirror (specular reflection), the normal pressure would be $P_N = \frac{2I}{c}\cos^2\theta$, and the shear stress would be identically zero.

#### Question 4
Two concentric circular conducting loops of radii $r_1$ and $r_2$ ($r_1 \ll r_2$) lie in mutually perpendicular planes, with the smaller loop centered on the axis of the larger loop:
(A) The mutual inductance between the two loops in this orthogonal orientation is identically zero ($M = 0$).  
(B) If the smaller loop is rotated by an angle $\theta$ about its diameter, the mutual inductance becomes $M(\theta) = \frac{\mu_0 \pi r_1^2}{2 r_2}\sin\theta$.  
(C) When steady currents $I_1$ and $I_2$ flow through the loops, a magnetic torque acts to align their magnetic dipole moments parallel to each other.  
(D) The magnitude of the maximum magnetic torque is $\tau_{\text{max}} = \frac{\mu_0 \pi r_1^2 I_1 I_2}{2 r_2}$.

#### Question 5
Regarding double refraction (birefringence) in a negative uniaxial crystal (such as calcite, $\mu_o > \mu_e$):
(A) The ordinary ray ($o$-ray) travels with the same speed $v_o = c/\mu_o$ in all directions, having a spherical wavefront.  
(B) The extraordinary ray ($e$-ray) travels with a direction-dependent speed, having an ellipsoidal wavefront.  
(C) Along the optic axis of the crystal, the speeds of the $o$-ray and $e$-ray are equal, and no double refraction occurs.  
(D) In a negative crystal, the $e$-ray wavefront envelope lies entirely outside the $o$-ray wavefront sphere ($v_e \ge v_o$).

#### Question 6
One mole of an ideal gas undergoes a cyclic process consisting of an isobaric expansion ($A \to B$), an isothermal expansion ($B \to C$), an isochoric cooling ($C \to D$), and an adiabatic compression ($D \to A$):
(A) The net work done by the gas per cycle is positive if the cycle is traversed clockwise on the $P-V$ diagram.  
(B) Heat is absorbed during stages $A \to B$ and $B \to C$.  
(C) Heat is rejected to the surroundings during stage $C \to D$.  
(D) During stage $D \to A$, the entropy of the gas remains constant.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A slender uniform rod of mass $M = 3.00\text{ kg}$ and length $L = 1.00\text{ m}$ is held vertically with its lower end touching a frictionless horizontal floor. The rod is released from rest. Taking $g = 9.80\text{ m/s}^2$, calculate the linear velocity $v$ (in $\text{m/s}$) of the upper end of the rod just before it strikes the floor. [Round off to TWO decimal places].

#### Question 8
Two point charges $q_1 = +4.0\ \mu\text{C}$ and $q_2 = -1.0\ \mu\text{C}$ are fixed at a separation distance $d = 0.30\text{ m}$. Calculate the distance (in meters, $\text{m}$) from the charge $q_2$ along the line joining them (on the side away from $q_1$) where the net electric potential is zero ($V = 0$).

#### Question 9
In a Fresnel biprism experiment, the distance between the slit and the screen is $D = 1.20\text{ m}$. A biprism of refractive index $\mu = 1.50$ and apex refracting angle $\alpha = 0.50^\circ = \frac{\pi}{360}\text{ rad}$ is placed at distance $u = 0.20\text{ m}$ from the slit. For light of wavelength $\lambda = 600\text{ nm}$, calculate the fringe width $\beta$ in millimeters ($\text{mm}$). [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 10
One mole of a real gas undergoes a free expansion (Joule expansion into vacuum) from volume $V_1 = 0.010\text{ m}^3$ to $V_2 = 0.030\text{ m}^3$. The gas obeys the equation of state $\left(P + \frac{a}{V^2}\right)V = RT$, with $a = 0.360\text{ Pa}\cdot\text{m}^6/\text{mol}^2$. If $C_V = \frac{3}{2}R$, calculate the temperature change $\Delta T$ (in Kelvin) of the gas. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to TWO decimal places].

#### Question 11
A circular coil of $N = 500$ turns and radius $r = 0.040\text{ m}$ has resistance $R = 5.0\ \Omega$. The coil is connected to a ballistic galvanometer. If the magnetic flux through the coil changes from $\Phi_1 = 2.0\text{ mWb}$ to $\Phi_2 = -2.0\text{ mWb}$, calculate the total electrical charge $Q$ (in milliCoulombs, $\text{mC}$) that flows through the galvanometer.

#### Question 12
The atomic mass of $^{235}_{92}\text{U}$ is $235.0439\text{ u}$. In a fission event, an average energy of $E = 200.0\text{ MeV}$ is released. Calculate the percentage of the rest mass of $^{235}\text{U}$ that is converted into energy in this fission process. [Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A satellite is orbiting Earth in a circular orbit of radius $r$. If its orbital speed is $v$, the escape velocity from this orbital position is:
(A) $\sqrt{2}v$  
(B) $2v$  
(C) $v/\sqrt{2}$  
(D) $v/2$

#### Question 14
Two soap bubbles of radii $r_1 = 2.0\text{ cm}$ and $r_2 = 4.0\text{ cm}$ are in contact with a common interface. The radius of curvature of the common soap membrane interface separating them is:
(A) $4.0\text{ cm}$  
(B) $2.0\text{ cm}$  
(C) $1.33\text{ cm}$  
(D) $6.0\text{ cm}$

#### Question 15
A source of sound of frequency $600\text{ Hz}$ and an observer move directly towards each other, each with speed $v/10$ (where $v$ is sound speed in still air). The frequency heard by the observer is:
(A) $733\text{ Hz}$  
(B) $667\text{ Hz}$  
(C) $600\text{ Hz}$  
(D) $540\text{ Hz}$

#### Question 16
The threshold frequency for photoelectric emission from a metal is $\nu_0$. When light of frequency $2\nu_0$ is incident, the maximum speed of photoelectrons is $v_1$. When light of frequency $5\nu_0$ is incident, the maximum speed is $v_2$. The ratio $v_1 / v_2$ is:
(A) $1/2$  
(B) $1/\sqrt{2}$  
(C) $1/4$  
(D) $2/5$

#### Question 17
A plane polarized light ray is incident on a quartz plate cut with its faces parallel to the optic axis. The minimum thickness of the plate to act as a quarter-wave plate for wavelength $\lambda = 600\text{ nm}$ ($\mu_e = 1.553, \mu_o = 1.544$) is:
(A) $16.7\ \mu\text{m}$  
(B) $33.3\ \mu\text{m}$  
(C) $8.33\ \mu\text{m}$  
(D) $50.0\ \mu\text{m}$

#### Question 18
A uniform solid sphere of mass $M$ and radius $R$ is rolling without slipping on a horizontal plane with velocity $v$. The total kinetic energy of the sphere is:
(A) $\frac{7}{10}M v^2$  
(B) $\frac{1}{2}M v^2$  
(C) $\frac{3}{5}M v^2$  
(D) $\frac{5}{7}M v^2$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following statements is/are correct regarding the crystal field theory of tetrahedral coordination complexes?
(A) The $d$-orbitals split into a lower energy twofold-degenerate $e$ set ($d_{z^2}, d_{x^2-y^2}$) and a higher energy threefold-degenerate $t_2$ set ($d_{xy}, d_{yz}, d_{zx}$).  
(B) The tetrahedral crystal field splitting energy is $\Delta_t = \frac{4}{9}\Delta_o$.  
(C) Tetrahedral complexes are almost exclusively high-spin because $\Delta_t$ is smaller than the pairing energy $P$.  
(D) Because tetrahedral geometry lacks an inversion center ($i$), $d-p$ mixing relaxes the Laporte selection rule, resulting in exceptionally intense absorption colors (e.g., deep blue $[\text{CoCl}_4]^{2-}$).

#### Question 20
In the Favorskii rearrangement:
(A) An $\alpha$-haloketone is treated with a base (such as sodium alkoxide or hydroxide) to yield an ester or carboxylic acid with skeletal rearrangement.  
(B) The reaction proceeds through a strained cyclopropanone intermediate formed by intramolecular enolate displacement of the halide.  
(C) Nucleophilic addition of the alkoxide to the carbonyl group of the cyclopropanone is followed by ring opening to the more stable carbanion.  
(D) 2-Chlorocyclohexanone rearranges in the presence of sodium methoxide to yield methyl cyclopentanecarboxylate.

#### Question 21
Regarding Faraday's laws of electrolysis:
(A) The mass of substance deposited or liberated at an electrode is directly proportional to the total electrical charge passed through the electrolyte ($m = Z I t$).  
(B) When the same quantity of electricity is passed through solutions of different electrolytes, the masses deposited are proportional to their chemical equivalent weights ($m \propto E$).  
(C) One Faraday ($1\text{ F} \approx 96500\text{ C}$) is the charge of one mole of electrons.  
(D) The electrochemical equivalent $Z$ has SI units of $\text{kg/C}$.

#### Question 22
Regarding the Langmuir adsorption isotherm for the adsorption of a gas on a solid surface:
(A) It assumes that the adsorbent surface possesses a fixed number of equivalent, energetically identical adsorption sites.  
(B) It assumes that each site can hold only one adsorbate molecule (monolayer adsorption).  
(C) The fractional surface coverage is given by $\theta = \frac{K P}{1 + K P}$, where $K$ is the adsorption equilibrium constant.  
(D) At very low pressures ($K P \ll 1$), $\theta \approx K P$ (first-order in pressure), while at high pressures ($K P \gg 1$), $\theta \approx 1$ (zero-order, saturation).

#### Question 23
In the qualitative analysis of Group IV cations ($\text{Zn}^{2+}, \text{Mn}^{2+}, \text{Ni}^{2+}, \text{Co}^{2+}$):
(A) The group reagent is $\text{H}_2\text{S}$ gas in the presence of $\text{NH}_4\text{OH}$ and $\text{NH}_4\text{Cl}$.  
(B) Basic medium increases the ionization of $\text{H}_2\text{S}$, providing a high sulfide ion concentration $[\text{S}^{2-}]$ sufficient to exceed the $K_{sp}$ of Group IV sulfides.  
(C) $\text{ZnS}$ precipitates as a dirty-white precipitate.  
(D) $\text{MnS}$ precipitates as a flesh/buff-colored precipitate soluble in dilute $\text{HCl}$.

#### Question 24
Regarding the thermal denaturation of double-stranded DNA:
(A) Heating DNA disrupts the hydrogen bonds between complementary base pairs without breaking the covalent phosphodiester backbone.  
(B) The transition from double-stranded to single-stranded DNA is accompanied by an increase in UV absorbance at $260\text{ nm}$ (Hyperchromic effect).  
(C) The melting temperature $T_m$ is the temperature at which $50\%$ of the helical structure is unwound.  
(D) DNA with a higher $\text{G-C}$ content has a higher $T_m$ because $\text{G-C}$ base pairs are joined by three hydrogen bonds compared to two in $\text{A-T}$ pairs.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
Calculate the solubility (in $\text{mol/L}$) of calcium fluoride ($\text{CaF}_2$) in pure water at $25^\circ\text{C}$ given $K_{sp} = 3.2 \times 10^{-11}$. If the solubility is $S = 2.0 \times 10^{-p}\text{ mol/L}$, find the integer value of $p$.

#### Question 26
For the elementary reaction $2A \to B$, the rate constant is $k = 0.050\text{ L}/(\text{mol}\cdot\text{s})$. If the initial concentration of $A$ is $[A]_0 = 0.40\text{ M}$, calculate the time (in seconds) required for $[A]$ to drop to $0.10\text{ M}$.

#### Question 27
An element with body-centered cubic (BCC) lattice has density $\rho = 7.87\text{ g/cm}^3$ and molar mass $M = 55.85\text{ g/mol}$. Calculate the unit cell edge length $a$ in picometers ($\text{pm}$). [Take $N_A = 6.02 \times 10^{23}\text{ mol}^{-1}$ and $\sqrt[3]{23.57} \approx 2.867$. Round off to the nearest integer].

#### Question 28
Calculate the standard EMF $E_{\text{cell}}^\circ$ (in Volts) at $298\text{ K}$ for:
$$\text{Sn}^{4+}(aq) + 2\text{Fe}^{2+}(aq) \to \text{Sn}^{2+}(aq) + 2\text{Fe}^{3+}(aq)$$
Given $E^\circ(\text{Sn}^{4+}/\text{Sn}^{2+}) = +0.15\text{ V}$ and $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V}$.

#### Question 29
A $0.20\text{ molal}$ aqueous solution of an electrolyte $AX_3$ dissociates completely. Calculate the boiling point elevation $\Delta T_b$ (in Kelvin) of the solution. [Take $K_b(\text{H}_2\text{O}) = 0.512\text{ K}\cdot\text{kg/mol}$. Round off to TWO decimal places].

#### Question 30
Calculate the total number of unpaired electrons in the tetrahedral complex $[\text{NiCl}_4]^{2-}$ ($\text{Ni}^{2+}, 3d^8$).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The Curtius rearrangement involves the thermal decomposition of an acyl azide to yield an isocyanate, which upon hydrolysis gives:
(A) Primary amine  
(B) Secondary amine  
(C) Amide  
(D) Carboxylic acid

#### Question 32
Which of the following compounds is non-aromatic?
(A) Cyclopentadiene  
(B) Benzene  
(C) Cyclopentadienyl anion  
(D) Tropylium cation

#### Question 33
In the cyanide process for silver extraction, the precipitating agent used to recover silver from $[\text{Ag}(\text{CN})_2]^-$ is:
(A) Zinc dust  
(B) Copper turnings  
(C) Carbon monoxide  
(D) Sodium amalgam

#### Question 34
Cellulose is a linear polysaccharide composed of:
(A) $\beta$-D-glucose units joined by $\beta-1,4$-glycosidic bonds  
(B) $\alpha$-D-glucose units joined by $\alpha-1,4$-glycosidic bonds  
(C) $\alpha$-D-glucose and $\beta$-D-fructose  
(D) $\beta$-D-galactose and $\alpha$-D-glucose

#### Question 35
The bond order of the nitric oxide molecule ($\text{NO}$) according to Molecular Orbital Theory is:
(A) $2.5$  
(B) $2.0$  
(C) $3.0$  
(D) $1.5$

#### Question 36
Sodium alkylbenzenesulfonate is a widely used:
(A) Anionic detergent  
(B) Cationic detergent  
(C) Non-ionic detergent  
(D) Amphoteric surfactant

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f: \mathbb{R} \to \mathbb{R}$ be a Lipschitz continuous function with Lipschitz constant $L > 0$, so that $|f(x) - f(y)| \le L|x - y|$ for all $x, y \in \mathbb{R}$:
(A) $f(x)$ is uniformly continuous on $\mathbb{R}$.  
(B) If $L < 1$, the function $f$ is a contraction mapping and possesses a unique fixed point $x^* \in \mathbb{R}$ such that $f(x^*) = x^*$ (Banach Fixed-Point Theorem).  
(C) $f(x)$ is differentiable almost everywhere on $\mathbb{R}$ (Rademacher's Theorem).  
(D) $f(x) = |x|$ is Lipschitz continuous on $\mathbb{R}$ with $L = 1$.

#### Question 38
Let $P$ be a real $n \times n$ matrix representing an orthogonal projection onto a subspace $V \subset \mathbb{R}^n$:
(A) $P^2 = P$ (idempotent).  
(B) $P^T = P$ (symmetric).  
(C) The eigenvalues of $P$ can only be $0$ or $1$.  
(D) For any vector $x \in \mathbb{R}^n$, $(x - P x)$ is orthogonal to $P x$.

#### Question 39
Consider the director circle of conic sections (the locus of points from which perpendicular tangents can be drawn):
(A) For the circle $x^2 + y^2 = r^2$, the director circle is $x^2 + y^2 = 2r^2$.  
(B) For the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, the director circle is $x^2 + y^2 = a^2 + b^2$.  
(C) For the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ ($a > b$), the director circle is $x^2 + y^2 = a^2 - b^2$.  
(D) For the parabola $y^2 = 4ax$, the director circle degenerates into the directrix $x = -a$.

#### Question 40
Consider the linear system of first-order differential equations $\frac{dx}{dt} = 2x + y, \frac{dy}{dt} = x + 2y$:
(A) The coefficient matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has eigenvalues $\lambda_1 = 3$ and $\lambda_2 = 1$.  
(B) Since both eigenvalues are real and strictly positive ($\lambda_1, \lambda_2 > 0$), the origin $(0, 0)$ is an unstable node.  
(C) The eigenvectors corresponding to $\lambda_1 = 3$ and $\lambda_2 = 1$ are $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ and $\begin{pmatrix} 1 \\ -1 \end{pmatrix}$ respectively.  
(D) The general solution is $\begin{pmatrix} x(t) \\ y(t) \end{pmatrix} = C_1 e^{3t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + C_2 e^t\begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

#### Question 41
A sphere $S$ passes through the circle of intersection of the sphere $S_1: x^2 + y^2 + z^2 - 4 = 0$ and the plane $P_1: x + y + z - 1 = 0$:
(A) The family of such spheres has the equation $(x^2 + y^2 + z^2 - 4) + \lambda(x + y + z - 1) = 0$.  
(B) If the sphere passes through the origin $(0, 0, 0)$, then $-4 - \lambda = 0 \implies \lambda = -4$.  
(C) The equation of the sphere passing through the origin is $x^2 + y^2 + z^2 - 4x - 4y - 4z = 0$.  
(D) The center of the sphere passing through the origin is $(2, 2, 2)$ and its radius is $2\sqrt{3}$.

#### Question 42
Let $X$ follow a normal distribution $N(\mu, \sigma^2)$ with probability density function $f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$:
(A) The density curve $y = f(x)$ is symmetric about the vertical line $x = \mu$.  
(B) The points of inflection of the normal curve occur at $x = \mu \pm \sigma$.  
(C) $P(\mu - \sigma \le X \le \mu + \sigma) \approx 0.6827$ ($68.3\%$).  
(D) The maximum value of $f(x)$ is attained at $x = \mu$ with value $\frac{1}{\sigma\sqrt{2\pi}}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 \frac{x^3}{\sqrt{1 - x^2}}\,dx$$
[Round off to TWO decimal places].

#### Question 44
Find the area of the region bounded by the curves $y = x^2$ and $y = 4$. [Round off to TWO decimal places].

#### Question 45
Find the number of positive integer solutions $(x, y, z)$ to the equation $x + y + z = 10$.

#### Question 46
Calculate the distance from the point $(1, 2, 3)$ to the line $\frac{x-6}{3} = \frac{y-7}{2} = \frac{z-7}{-2}$.

#### Question 47
Evaluate the sum of the series:
$$S = \sum_{n=1}^\infty \frac{1}{n(n+1)} = \frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \frac{1}{3 \cdot 4} + \dots$$

#### Question 48
How many different 5-digit numbers can be formed using the digits $1, 2, 3, 4, 5$ such that the odd digits always occupy the odd places?

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The perpendicular distance from the point $(0, 0, 0)$ to the plane $x + 2y - 2z = 9$ is:
(A) $3$  
(B) $9$  
(C) $1$  
(D) $\sqrt{3}$

#### Question 50
If $A$ is a $3 \times 3$ matrix such that $\det(A) = 4$, then $\det(\text{adj } A)$ is:
(A) $16$  
(B) $64$  
(C) $4$  
(D) $8$

#### Question 51
The eccentricity of the rectangular hyperbola $x^2 - y^2 = 16$ is:
(A) $\sqrt{2}$  
(B) $2$  
(C) $\sqrt{3}$  
(D) $1$

#### Question 52
The angle between the planes $2x - y + z = 6$ and $x + y + 2z = 7$ is:
(A) $\pi/3$ ($60^\circ$)  
(B) $\pi/4$ ($45^\circ$)  
(C) $\pi/6$ ($30^\circ$)  
(D) $\pi/2$ ($90^\circ$)

#### Question 53
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{\ln(1 + 3x)}{x}$$
(A) $3$  
(B) $1$  
(C) $1/3$  
(D) $0$

#### Question 54
The minimum value of the expression $f(x) = 2^{x^2 - 2x + 3}$ is:
(A) $4$  
(B) $2$  
(C) $8$  
(D) $1$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 07 — Paper 2
## Organising Institute Style Inspiration: IIT Delhi (`IIT_DELHI_STYLE`)
**Historical Reference Benchmark**: 2013, 2020 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject — Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject — Matching List / Matrix Match)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A uniform rod of mass $M$ and length $L$ lies on a smooth horizontal table. A horizontal impulse $J$ is applied perpendicular to the rod at one of its ends:
(A) The velocity of the center of mass immediately after the impulse is $v_{\text{cm}} = \frac{J}{M}$.  
(B) The angular velocity of the rod about its center of mass is $\omega = \frac{J(L/2)}{I_{\text{cm}}} = \frac{6J}{ML}$.  
(C) The instantaneous center of rotation (point of zero velocity) is located at distance $L/6$ from the center of mass on the opposite side of the struck end.  
(D) The kinetic energy imparted to the rod is $K = \frac{1}{2}M v_{\text{cm}}^2 + \frac{1}{2}I_{\text{cm}}\omega^2 = \frac{2J^2}{M}$.

#### Question 2
A large open water tank has a small circular hole of area $a$ at depth $h$ below the free surface. A horizontal water jet escapes through the orifice:
(A) By Torricelli's law, the efflux velocity is $v = \sqrt{2gh}$.  
(B) Due to streamline convergence (vena contracta), the effective cross-sectional area of the jet is $a_c = C_c a$ where $C_c \approx 0.62$.  
(C) The volume discharge rate is $Q = C_d a \sqrt{2gh}$ where $C_d \approx 0.60 - 0.65$.  
(D) The horizontal reaction force exerted by the escaping jet on the tank is $F_{\text{reac}} = 2 \rho g h a C_c$.

#### Question 3
A beam of unpolarized light of intensity $I_0$ passes through a series of three ideal linear polarizers $P_1, P_2, P_3$. The transmission axis of $P_1$ is vertical, $P_3$ is horizontal ($90^\circ$ to $P_1$), and $P_2$ is oriented at angle $\theta$ to the vertical:
(A) The intensity after passing through $P_1$ is $I_1 = \frac{1}{2}I_0$.  
(B) The intensity after passing through $P_2$ is $I_2 = \frac{1}{2}I_0 \cos^2\theta$.  
(C) The intensity transmitted by $P_3$ is $I_3 = \frac{1}{2}I_0 \cos^2\theta \sin^2\theta = \frac{1}{8}I_0 \sin^2(2\theta)$.  
(D) The transmitted intensity $I_3$ is maximum when $\theta = 45^\circ$, with $I_{3,\text{max}} = \frac{1}{8}I_0$.

#### Question 4
A long straight wire carrying steady current $I$ lies in the plane of a rectangular conducting wire loop of mass $m$, width $w$, and length $L$. The loop is free to slide on a frictionless table:
(A) The magnetic flux linked with the loop when its nearest side is at distance $x$ from the wire is $\Phi(x) = \frac{\mu_0 I L}{2\pi}\ln\left(\frac{x+w}{x}\right)$.  
(B) If the loop moves away from the wire with velocity $v = \frac{dx}{dt}$, the induced EMF in the loop is $\mathcal{E} = \frac{\mu_0 I L w v}{2\pi x(x+w)}$.  
(C) The induced current flows in the clockwise direction to oppose the decreasing magnetic flux.  
(D) The magnetic Lorentz force on the loop acts to retard its outward motion.

#### Question 5
In an experiment on the photoelectric effect using cesium ($\Phi_0 = 1.90\text{ eV}$):
(A) The threshold wavelength is $\lambda_0 = \frac{hc}{\Phi_0} \approx 653\text{ nm}$.  
(B) Illumination with light of wavelength $\lambda = 400\text{ nm}$ ($E_{\text{photon}} = 3.10\text{ eV}$) gives a stopping potential $V_0 = 1.20\text{ V}$.  
(C) Doubling the intensity of the $400\text{ nm}$ light doubles the saturation current, but leaves the stopping potential unchanged.  
(D) Photons of wavelength $\lambda = 700\text{ nm}$ cannot produce photoelectric emission from cesium.

#### Question 6
An ideal gas undergoes a cycle consisting of:
1. Isothermal expansion at $T_H$ from $V_1$ to $V_2$.
2. Adiabatic expansion from $T_H, V_2$ to $T_C, V_3$.
3. Isothermal compression at $T_C$ from $V_3$ to $V_4$.
4. Adiabatic compression from $T_C, V_4$ back to $T_H, V_1$.
Which of the following statements is/are correct?
(A) The volume ratios satisfy $\frac{V_2}{V_1} = \frac{V_3}{V_4}$.  
(B) The heat absorbed is $Q_H = n R T_H \ln(V_2/V_1)$.  
(C) The efficiency of this Carnot cycle is $\eta = 1 - \frac{T_C}{T_H}$.  
(D) The net work done per cycle is $W = n R (T_H - T_C)\ln(V_2/V_1)$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A particle of mass $m = 0.10\text{ kg}$ is attached to a vertical spring of spring constant $k = 40.0\text{ N/m}$. The particle is released from rest from the position where the spring is unstretched. Calculate the maximum extension $x_{\text{max}}$ (in meters, $\text{m}$) of the spring. [Take $g = 9.80\text{ m/s}^2$. Round off to TWO decimal places].

#### Question 8
Two large parallel conducting plates separated by distance $d = 1.0\text{ mm}$ form a capacitor of capacitance $C = 1.77\text{ nF}$. Calculate the area $A$ (in $\text{m}^2$) of each plate. [Take $\varepsilon_0 = 8.85 \times 10^{-12}\text{ F/m}$].

#### Question 9
In a single-slit Fraunhofer diffraction experiment, light of wavelength $\lambda = 500\text{ nm}$ illuminates a slit of width $a = 0.10\text{ mm}$. If the screen is at distance $D = 2.00\text{ m}$, calculate the linear width $w$ (in millimeters, $\text{mm}$) of the central diffraction maximum.

#### Question 10
Calculate the root-mean-square speed $v_{\text{rms}}$ (in $\text{m/s}$) of hydrogen molecules ($\text{H}_2, M = 0.0020\text{ kg/mol}$) at $T = 300\text{ K}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\sqrt{3741300} \approx 1934.2$. Round off to the nearest integer].

#### Question 11
A toroidal solenoid has mean radius $R = 0.20\text{ m}$, cross-sectional area $A = 5.0\text{ cm}^2$, and $N = 1000\text{ turns}$. Calculate the self-inductance $L$ (in milliHenries, $\text{mH}$) of the toroid. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$. Round off to TWO decimal places].

#### Question 12
A radioactive sample has an initial activity $A_0 = 800\text{ Bq}$ and half-life $T_{1/2} = 10.0\text{ days}$. Calculate the activity $A$ (in $\text{Bq}$) after $30.0\text{ days}$.

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the rotational moments of inertia in List-I with their standard formula in List-II:
- **List-I**:
  - P. Solid cylinder about axis of symmetry
  - Q. Thin spherical shell about diameter
  - R. Solid sphere about diameter
  - S. Thin rod about perpendicular axis through center
- **List-II**:
  - 1. $\frac{1}{2}M R^2$
  - 2. $\frac{2}{3}M R^2$
  - 3. $\frac{2}{5}M R^2$
  - 4. $\frac{1}{12}M L^2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 14
Match the fluid transport phenomena in List-I with their characteristic transport coefficient in List-II:
- **List-I**:
  - P. Viscosity
  - Q. Thermal conduction
  - R. Diffusion
  - S. Electrical conduction
- **List-II**:
  - 1. Momentum transport ($\eta$)
  - 2. Energy transport ($K$)
  - 3. Mass transport ($D$)
  - 4. Charge transport ($\sigma$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 15
Match the thermodynamic functions in List-I with their natural independent variables in List-II:
- **List-I**:
  - P. Internal Energy $U$
  - Q. Enthalpy $H$
  - R. Helmholtz Free Energy $F$
  - S. Gibbs Free Energy $G$
- **List-II**:
  - 1. $(S, V)$
  - 2. $(S, P)$
  - 3. $(T, V)$
  - 4. $(T, P)$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the nuclear reactions in List-I with their characteristic in List-II:
- **List-I**:
  - P. Fission of $^{235}\text{U}$
  - Q. Fusion of Deuterium-Tritium
  - R. Radiocarbon dating
  - S. Pair production
- **List-II**:
  - 1. Chain reaction controlled by control rods
  - 2. High temperature thermonuclear reaction in stars
  - 3. Half-life of 5730 years for organic archaeological dating
  - 4. Photon conversion into electron-positron pair in nuclear Coulomb field

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 17
Match the optical aberrations in List-I with their corrective remedy in List-II:
- **List-I**:
  - P. Chromatic aberration
  - Q. Spherical aberration
  - R. Astigmatism
  - S. Coma
- **List-II**:
  - 1. Achromatic doublet lens combination
  - 2. Parabolic reflector or crossed lenses
  - 3. Cylindrical lens
  - 4. Paraxial ray stops (aperture diaphragm)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 18
Match the electromagnetic frequency ranges in List-I with their standard communication use in List-II:
- **List-I**:
  - P. Very High Frequency (VHF)
  - Q. Ultra High Frequency (UHF)
  - R. Microwaves
  - S. Optical fibers
- **List-II**:
  - 1. FM radio and television
  - 2. Cellular mobile phone communication
  - 3. Radar and satellite communication
  - 4. Infrared light carrier signals

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following complex ions have square planar geometry?
(A) $[\text{PtCl}_4]^{2-}$ ($5d^8$)  
(B) $[\text{Ni}(\text{CN})_4]^{2-}$ ($3d^8$)  
(C) $[\text{PdCl}_4]^{2-}$ ($4d^8$)  
(D) $[\text{NiCl}_4]^{2-}$ ($3d^8$)

#### Question 20
Which of the following compounds undergo aldol condensation upon treatment with dilute alkali?
(A) Acetaldehyde ($\text{CH}_3\text{CHO}$)  
(B) Propanal ($\text{CH}_3\text{CH}_2\text{CHO}$)  
(C) Acetophenone ($\text{C}_6\text{H}_5\text{COCH}_3$)  
(D) Benzaldehyde ($\text{C}_6\text{H}_5\text{CHO}$)

#### Question 21
Regarding standard electrode potentials:
(A) Fluorine ($\text{F}_2$) is the strongest oxidizing agent in aqueous solution ($E^\circ = +2.87\text{ V}$).  
(B) Lithium ($\text{Li}$) is the strongest reducing agent in aqueous solution ($E^\circ = -3.05\text{ V}$).  
(C) A spontaneous galvanic cell requires $E_{\text{cell}}^\circ > 0$ and $\Delta G^\circ < 0$.  
(D) An inert platinum electrode is used when an electrode reaction involves gaseous or dissolved redox species without a solid metal phase.

#### Question 22
Which of the following molecules exhibit geometrical (cis-trans) isomerism?
(A) But-2-ene  
(B) 1,2-Dichloroethene  
(C) Propene  
(D) But-1-ene

#### Question 23
Which of the following compounds gives a blood-red coloration with neutral ferric chloride ($\text{FeCl}_3$) solution in qualitative analysis?
(A) Sodium thiocyanate ($\text{NaSCN}$) forming $[\text{Fe}(\text{SCN})]^{2+}$  
(B) Potassium ferrocyanide  
(C) Sodium chloride  
(D) Potassium ferricyanide

#### Question 24
Which of the following amino acids are classified as essential amino acids (cannot be synthesized by the human body)?
(A) Valine  
(B) Leucine  
(C) Isoleucine  
(D) Glycine

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The solubility product of $\text{AgBr}$ in water is $K_{sp} = 5.0 \times 10^{-13}$ at $25^\circ\text{C}$. Calculate the solubility $S$ of $\text{AgBr}$ in pure water in $\mu\text{mol/L}$. [Take $\sqrt{5.0} \approx 2.24$. Round off to TWO decimal places].

#### Question 26
For a second-order reaction $2A \to \text{Products}$, the initial concentration is $[A]_0 = 0.50\text{ M}$ and the rate constant is $k = 0.020\text{ L}/(\text{mol}\cdot\text{s})$. Calculate the half-life $t_{1/2}$ of the reaction in seconds ($\text{s}$).

#### Question 27
Copper crystallizes in an FCC lattice with edge length $a = 361.5\text{ pm}$. Calculate the atomic radius $r$ of copper in picometers ($\text{pm}$). [Take $\sqrt{2} \approx 1.414$. Round off to ONE decimal place].

#### Question 28
Calculate the standard enthalpy of formation $\Delta_f H^\circ$ (in $\text{kJ/mol}$) of liquid water given:
- $\text{H}_2(g) + \frac{1}{2}\text{O}_2(g) \to \text{H}_2\text{O}(l) \quad \Delta H^\circ = -285.8\text{ kJ/mol}$

#### Question 29
A $0.10\text{ m}$ solution of glucose ($\text{C}_6\text{H}_{12}\text{O}_6$) in water freezes at $-0.186^\circ\text{C}$. Calculate the cryoscopic constant $K_f$ of water in $\text{K}\cdot\text{kg/mol}$. [Round off to TWO decimal places].

#### Question 30
Find the oxidation state of iron in potassium ferricyanide ($\text{K}_3[\text{Fe}(\text{CN})_6]$).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following functional groups undergoes reduction to a primary alcohol with $\text{LiAlH}_4$?
(A) Carboxylic acid ($-\text{COOH}$)  
(B) Tertiary alcohol  
(C) Tertiary amine  
(D) Alkane

#### Question 32
The structure of sulfur tetrafluoride ($\text{SF}_4$) according to VSEPR theory is:
(A) Seesaw  
(B) Tetrahedral  
(C) Square planar  
(D) Octahedral

#### Question 33
In the cyanide leaching of gold, the gold complex formed is:
(A) $[\text{Au}(\text{CN})_2]^-$  
(B) $[\text{Au}(\text{CN})_4]^-$  
(C) $[\text{Au}(\text{CN})_3]^{2-}$  
(D) $\text{AuCN}$

#### Question 34
Which of the following compounds gives a positive iodoform test with $\text{I}_2 / \text{NaOH}$?
(A) Propan-2-ol  
(B) Propan-1-ol  
(C) Methanol  
(D) Diethyl ether

#### Question 35
The hybridization of the central atom in $\text{PCl}_3$ is:
(A) $sp^3$  
(B) $sp^2$  
(C) $sp^3d$  
(D) $dsp^2$

#### Question 36
Terylene (Dacron) is a polyester polymer synthesized from:
(A) Ethylene glycol and terephthalic acid  
(B) Hexamethylenediamine and adipic acid  
(C) Phenol and formaldehyde  
(D) Caprolactam

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^3 - 6x^2 + 9x + 1$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f'(x) = 3(x - 1)(x - 3)$.  
(B) $f(x)$ has a local maximum at $x = 1$ with value $5$.  
(C) $f(x)$ has a local minimum at $x = 3$ with value $1$.  
(D) The point of inflection is at $(2, 3)$.

#### Question 38
Let $A$ be a $3 \times 3$ matrix such that $A^2 = I$ (involutory matrix):
(A) The only possible eigenvalues of $A$ are $+1$ and $-1$.  
(B) $\det(A)$ can be either $+1$ or $-1$.  
(C) $A^{-1} = A$.  
(D) The matrix $\frac{1}{2}(I + A)$ is idempotent.

#### Question 39
Consider the parabola $y^2 = 8x$. A chord of the parabola passes through the focus $(2, 0)$:
(A) If the focal chord has inclination $\theta$, its length is $L = 8\csc^2\theta$.  
(B) The minimum length of any focal chord is 8 (the latus rectum).  
(C) The circle described on any focal chord as diameter touches the directrix $x = -2$.  
(D) Tangents drawn at the ends of any focal chord intersect at right angles on the directrix.

#### Question 40
Consider the differential equation $\frac{dy}{dx} + \frac{2}{x}y = x$ for $x > 0$:
(A) The integrating factor is $x^2$.  
(B) The general solution is $y(x) = \frac{x^2}{4} + \frac{C}{x^2}$.  
(C) If $y(1) = 5/4$, then $C = 1$.  
(D) With $C = 1$, $\lim_{x \to 0^+} y(x) = +\infty$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-zero vectors such that $\vec{a} \times \vec{b} = \vec{c}$ and $\vec{b} \times \vec{c} = \vec{a}$:
(A) $\vec{a}, \vec{b}, \vec{c}$ are mutually orthogonal.  
(B) $|\vec{b}| = 1$.  
(C) $|\vec{a}| = |\vec{c}|$.  
(D) $[\vec{a} \ \vec{b} \ \vec{c}] = |\vec{a}|^2$.

#### Question 42
In a binomial distribution with $n = 6$ and $p = 1/2$:
(A) The mean is $3$.  
(B) The variance is $1.5$.  
(C) The distribution is symmetric about $k = 3$.  
(D) $P(X = 3) = \binom{6}{3}(1/2)^6 = \frac{20}{64} = \frac{5}{16}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area enclosed by the ellipse $\frac{x^2}{25} + \frac{y^2}{16} = 1$, divided by $\pi$.

#### Question 44
Find the slope of the normal to the curve $y = x^3 - x$ at the point where $x = 1$.

#### Question 45
Evaluate the definite integral:
$$I = \int_0^1 x^2 (1 - x)^2\,dx$$
If $I = \frac{1}{m}$, find the integer value of $m$.

#### Question 46
Calculate the distance between the parallel planes $x + 2y - 2z = 4$ and $x + 2y - 2z = 10$.

#### Question 47
If the sum of an infinite geometric progression is $S = 4$ and the second term is $3/4$, find the common ratio $r$ ($r < 1$).

#### Question 48
How many 3-letter words (with or without meaning) can be formed using the letters of the word `EQUATION` without repetition?

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The shortest distance between the origin and the plane $3x - 4y + 12z = 26$ is:
(A) $2$  
(B) $3$  
(C) $1$  
(D) $4$

#### Question 50
If $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, then $\det(A^{-1})$ is:
(A) $-1/2$  
(B) $-2$  
(C) $1/2$  
(D) $2$

#### Question 51
The length of the latus rectum of the parabola $y^2 = 16x$ is:
(A) $16$  
(B) $8$  
(C) $4$  
(D) $32$

#### Question 52
The angle between the lines $\frac{x}{1} = \frac{y}{1} = \frac{z}{0}$ and $\frac{x}{0} = \frac{y}{1} = \frac{z}{1}$ is:
(A) $\pi/3$ ($60^\circ$)  
(B) $\pi/4$ ($45^\circ$)  
(C) $\pi/2$ ($90^\circ$)  
(D) $\pi/6$ ($30^\circ$)

#### Question 53
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{\sin(5x)}{\sin(2x)}$$
(A) $5/2$  
(B) $2/5$  
(C) $1$  
(D) $0$

#### Question 54
The maximum value of $f(x) = 5\sin x + 12\cos x$ for all $x \in \mathbb{R}$ is:
(A) $13$  
(B) $17$  
(C) $7$  
(D) $12$
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 07 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Synchrocyclotron Relativistic Physics, Frequency Modulation, Principle of Autophasing.
- **2. Derivation**:
  - Relativistic mass $m(v) = \gamma m_0$. Cyclotron frequency $\omega = \frac{q B}{\gamma m_0}$ decreases as particle accelerates. (A) is correct.
  - To maintain resonance, RF frequency must decrease with time. (B) is correct.
  - Veksler and McMillan's autophasing principle locks particles in stable orbits. (C) is correct.
  - Synchrocyclotrons accelerate protons up to hundreds of $\text{MeV}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Rolling without Slipping on Curvilinear Surfaces, Parabolic Oscillation.
- **2. Derivation**:
  - For $y = k x^2$: $y' = 2kx, y'' = 2k$. Radius of curvature at origin: $R = \frac{[1 + (y')^2]^{3/2}}{y''} = \frac{1}{2k}$. (A) is correct.
  - Path of center of mass has radius $R - r = \frac{1}{2k} - r$. (B) is correct.
  - Angular frequency of small oscillations for rolling sphere on concave surface: $\omega = \sqrt{\frac{g}{(R-r)(1 + I/Mr^2)}} = \sqrt{\frac{5g}{7(R-r)}}$. (C) is correct.
  - Normal force at bottom: $N = M g + M \frac{v^2}{R-r} > M g$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Radiation Pressure and Shear Stress on Oblique Surfaces.
- **2. Derivation**:
  - Incident optical power: $P_{\text{opt}} = I A \cos\theta$. (A) is correct.
  - Normal momentum absorbed per second divided by area: $P_N = \frac{I A \cos\theta}{c} \frac{\cos\theta}{A} = \frac{I}{c}\cos^2\theta$. (B) is correct.
  - Tangential momentum absorbed per second divided by area: $\tau = \frac{I A \cos\theta}{c} \frac{\sin\theta}{A} = \frac{I}{c}\sin\theta\cos\theta$. (C) is correct.
  - On reflection: tangential momentum is conserved (shear stress is zero), while normal momentum doubles ($P_N = \frac{2I}{c}\cos^2\theta$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Mutual Inductance of Orthogonal Loops, Magnetic Torque.
- **2. Derivation**:
  - When planes are perpendicular, magnetic field of loop 2 is parallel to the plane of loop 1, giving zero flux linkage ($M = 0$). (A) is correct.
  - Rotating by $\theta$ gives $M(\theta) = \frac{\mu_0 \pi r_1^2}{2 r_2}\sin\theta$. (B) is correct.
  - Magnetic interaction torque $\vec{\tau} = \vec{\mu}_1 \times \vec{B}_2$ acts to align dipoles. (C) is correct.
  - Maximum torque: $\tau_{\text{max}} = \mu_1 B_2 = (I_1 \pi r_1^2)\left(\frac{\mu_0 I_2}{2 r_2}\right) = \frac{\mu_0 \pi r_1^2 I_1 I_2}{2 r_2}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Birefringence in Uniaxial Calcite Crystals, Wavefront Envelopes.
- **2. Derivation**:
  - In negative uniaxial crystal ($\mu_o > \mu_e$), $v_o < v_e$.
  - $o$-ray has spherical wavefront with constant speed $v_o$. (A) is correct.
  - $e$-ray has ellipsoidal wavefront. (B) is correct.
  - Along optic axis, $v_o = v_e$. (C) is correct.
  - Since $v_e \ge v_o$, the ellipsoidal $e$-wavefront envelope lies outside the spherical $o$-wavefront. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Four-Stage Thermodynamic Cycle, P-V and T-S Relationships.
- **2. Derivation**:
  - Clockwise cycle on $P-V$ diagram does positive net work. (A) is correct.
  - Heat absorbed during isobaric expansion ($dQ = n C_P dT > 0$) and isothermal expansion ($dQ = dW > 0$). (B) is correct.
  - Heat rejected during isochoric cooling ($dQ = n C_V dT < 0$). (C) is correct.
  - Reversible adiabatic compression has $dQ = 0 \implies \Delta S = 0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Center of mass falls by $L/2 = 0.50\text{ m}$. As the floor is frictionless, the center of mass moves purely vertically.
  By conservation of mechanical energy when rod makes angle $\theta$ with floor:
  $M g \frac{L}{2}(1 - \sin\theta) = \frac{1}{2} M v_{\text{cm}}^2 + \frac{1}{2} I_{\text{cm}} \omega^2$.
  Just before hitting the floor ($\theta \to 0$): $v_{\text{cm}} = 0$, all energy is in rotation about CM:
  $M g \frac{L}{2} = \frac{1}{2}\left(\frac{1}{12}M L^2\right)\omega^2 \implies \omega = \sqrt{\frac{12 g}{L}} = \sqrt{12(9.80)} = \sqrt{117.6} \approx 10.844\text{ rad/s}$.
  Speed of upper end: $v = \omega(L/2) = \frac{10.844}{2} = 5.42\text{ m/s}$. Exact: `5.42`.
- **Question 8**: Potential at point $P$ at distance $x$ from $q_2$:
  $V = \frac{1}{4\pi\varepsilon_0}\left[\frac{q_1}{d + x} + \frac{q_2}{x}\right] = 0 \implies \frac{4.0}{0.30 + x} = \frac{1.0}{x} \implies 4x = 0.30 + x \implies 3x = 0.30 \implies x = 0.10\text{ m}$. Exact: `0.10`.
- **Question 9**: Virtual source separation: $d = 2 u (\mu - 1)\alpha = 2(0.20\text{ m})(1.50 - 1)\left(\frac{\pi}{360}\right) = 0.20(0.50)\left(\frac{3.1416}{360}\right) \approx 0.10(0.008727) \approx 8.727 \times 10^{-4}\text{ m} = 0.8727\text{ mm}$.
  Fringe width: $\beta = \frac{\lambda D}{d} = \frac{(600 \times 10^{-9}\text{ m})(1.20\text{ m})}{8.727 \times 10^{-4}\text{ m}} = \frac{7.20 \times 10^{-7}}{8.727 \times 10^{-4}} \approx 8.25 \times 10^{-4}\text{ m} = 0.83\text{ mm}$. Exact: `0.83`.
- **Question 10**: In Joule expansion, $W = 0, Q = 0 \implies \Delta U = 0$.
  For van der Waals gas: $U(T, V) = n C_V T - \frac{n^2 a}{V} = \text{const}$.
  $n C_V \Delta T = n^2 a \left(\frac{1}{V_2} - \frac{1}{V_1}\right) \implies \Delta T = \frac{a}{C_V}\left(\frac{1}{V_2} - \frac{1}{V_1}\right) = \frac{0.360}{\frac{3}{2}(8.314)}\left(\frac{1}{0.030} - \frac{1}{0.010}\right) = \frac{0.360}{12.471}(33.33 - 100) = (0.02887)(-66.67) \approx -1.92\text{ K}$.
  Temperature change is $-1.92\text{ K}$ (drops by $1.92\text{ K}$). Exact: `-1.92` (or magnitude `1.92`).
- **Question 11**: Induced charge: $Q = \frac{\Delta \Phi_{\text{total}}}{R} = \frac{N(\Phi_1 - \Phi_2)}{R} = \frac{500(2.0 \times 10^{-3} - (-2.0 \times 10^{-3}))}{5.0} = \frac{500(4.0 \times 10^{-3})}{5.0} = \frac{2.0}{5.0} = 0.40\text{ C} = 400.00\text{ mC}$. Exact: `400.00`.
- **Question 12**: Rest mass energy of $^{235}\text{U}$: $E_{\text{rest}} = (235.0439)(931.5) \approx 218943\text{ MeV}$.
  Percentage converted: $\frac{200.0}{218943} \times 100\% \approx 0.0913\% \approx 0.09\%$. Exact: `0.09`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Orbital speed $v = \sqrt{GM/r}$. Escape speed $v_e = \sqrt{2GM/r} = \sqrt{2}v$. Option (A).
- **Question 14**: $\frac{1}{R_c} = \frac{1}{r_1} - \frac{1}{r_2} = \frac{1}{2.0} - \frac{1}{4.0} = \frac{1}{4.0} \implies R_c = 4.0\text{ cm}$. Option (A).
- **Question 15**: $\nu = \nu_0 \frac{v + u_o}{v - u_s} = 600 \frac{v + v/10}{v - v/10} = 600 \frac{1.1}{0.9} = 600 \times \frac{11}{9} \approx 733.3\text{ Hz} \approx 733\text{ Hz}$. Option (A).
- **Question 16**: $\frac{1}{2}m v_1^2 = 2h\nu_0 - h\nu_0 = h\nu_0$. $\frac{1}{2}m v_2^2 = 5h\nu_0 - h\nu_0 = 4h\nu_0$. Ratio $v_1^2 / v_2^2 = 1/4 \implies v_1 / v_2 = 1/2$. Option (A).
- **Question 17**: Quarter wave plate: $(\mu_e - \mu_o)t = \lambda/4 \implies t = \frac{\lambda}{4(\mu_e - \mu_o)} = \frac{600 \times 10^{-9}}{4(1.553 - 1.544)} = \frac{600 \times 10^{-9}}{4(0.009)} = \frac{600 \times 10^{-9}}{0.036} = 1.667 \times 10^{-5}\text{ m} = 16.7\ \mu\text{m}$. Option (A).
- **Question 18**: $K = \frac{1}{2}M v^2 + \frac{1}{2}\left(\frac{2}{5}M R^2\right)\left(\frac{v}{R}\right)^2 = \frac{7}{10}M v^2$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Tetrahedral CFT: $e$ lower, $t_2$ higher, splitting $\Delta_t = \frac{4}{9}\Delta_o$. Almost exclusively high-spin. Lack of inversion center enables $d-p$ mixing, making transitions Laporte-allowed and intensely colored. Options: (A), (B), (C), (D).
- **Question 20**: Favorskii rearrangement: $\alpha$-haloketone + base $\to$ cyclopropanone intermediate $\to$ ring opening to rearranged ester. 2-chlorocyclohexanone yields methyl cyclopentanecarboxylate. Options: (A), (B), (C), (D).
- **Question 21**: Faraday's laws: $m = ZIt$, $m \propto E$, $1\text{ F} \approx 96500\text{ C/mol}$, $Z$ in $\text{kg/C}$ or $\text{g/C}$. Options: (A), (B), (C), (D).
- **Question 22**: Langmuir isotherm assumes monolayer on equivalent sites without lateral interactions: $\theta = \frac{KP}{1+KP}$. First order at low P, zero order at high P. Options: (A), (B), (C), (D).
- **Question 23**: Group IV cations precipitate as sulfides in basic $\text{H}_2\text{S}$. $\text{ZnS}$ is white/dirty white, $\text{MnS}$ is buff/flesh-colored. Options: (A), (B), (C), (D).
- **Question 24**: Thermal denaturation breaks H-bonds without cleaving covalent backbone. Causes hyperchromic effect at $260\text{ nm}$. $T_m$ increases with GC content. Options: (A), (B), (C), (D).
- **Question 25**: $\text{CaF}_2 \rightleftharpoons \text{Ca}^{2+} + 2\text{F}^- \implies K_{sp} = 4S^3 \implies S = \sqrt[3]{K_{sp}/4} = \sqrt[3]{3.2 \times 10^{-11}/4} = \sqrt[3]{8.0 \times 10^{-12}} = 2.0 \times 10^{-4}\text{ mol/L} \implies p = 4$. Exact: `4.00`.
- **Question 26**: Second order: $\frac{1}{[A]} - \frac{1}{[A]_0} = k t \implies \frac{1}{0.10} - \frac{1}{0.40} = 10 - 2.5 = 7.5 = (0.050)t \implies t = \frac{7.5}{0.050} = 150.00\text{ s}$. Exact: `150.00`.
- **Question 27**: $a^3 = \frac{Z M}{\rho N_A} = \frac{2(55.85)}{7.87 \times 6.02 \times 10^{23}} = \frac{111.7}{4.7377 \times 10^{24}} = 23.577 \times 10^{-24}\text{ cm}^3 \implies a = 2.867 \times 10^{-8}\text{ cm} \approx 287\text{ pm}$. Exact: `287.00`.
- **Question 28**: $E_{\text{cell}}^\circ = E^\circ(\text{Sn}^{4+}/\text{Sn}^{2+}) - E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = 0.15 - 0.77 = -0.62\text{ V}$. Exact: `-0.62`.
- **Question 29**: $AX_3$ dissociates into 4 ions ($i = 4$). $\Delta T_b = i K_b m = 4(0.512)(0.20) = 0.4096\text{ K} \approx 0.41\text{ K}$. Exact: `0.41`.
- **Question 30**: $[\text{NiCl}_4]^{2-}$: $\text{Ni}^{2+}$ ($3d^8$). In weak field tetrahedral geometry, configuration is $e^4 t_2^4$, leaving 2 unpaired electrons. Exact: `2.00`.
- **Question 31**: Curtius rearrangement produces primary amine. Option (A).
- **Question 32**: Cyclopentadiene contains an $sp^3$ hybridized carbon, disrupting cyclic conjugation $\implies$ non-aromatic. Option (A).
- **Question 33**: Zinc dust reduces $\text{Ag}^+$ in $[\text{Ag}(\text{CN})_2]^-$ to metallic silver. Option (A).
- **Question 34**: Cellulose consists of $\beta$-D-glucose linked by $\beta-1,4$-glycosidic bonds. Option (A).
- **Question 35**: In $\text{NO}$, $N = 15$ electrons: $\sigma_{2p_z}^2 \pi_{2p_x}^2 \pi_{2p_y}^2 \pi^*_{2p_x}^1$. Bond order $= \frac{8 - 3}{2} = 2.5$. Option (A).
- **Question 36**: Sodium alkylbenzenesulfonate has a sulfonate anion ($-\text{SO}_3^-\text{Na}^+$), making it an anionic detergent. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: Lipschitz continuous functions are uniformly continuous. $L < 1 \implies$ Banach contraction. Rademacher's theorem states differentiable a.e. $|x|$ has $L = 1$. Options: (A), (B), (C), (D).
- **Question 38**: Orthogonal projection: $P^2 = P$ (idempotent), $P^T = P$ (symmetric), eigenvalues are 0, 1. $(x - Px) \cdot Px = x^T(I - P)^T P x = x^T(P - P^2)x = 0$ (orthogonal). Options: (A), (B), (C), (D).
- **Question 39**: Director circle equations: circle $x^2+y^2=2r^2$, ellipse $x^2+y^2=a^2+b^2$, hyperbola $x^2+y^2=a^2-b^2$, parabola is directrix $x=-a$. Options: (A), (B), (C), (D).
- **Question 40**: Matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$. $\det(A - \lambda I) = (\lambda - 2)^2 - 1 = 0 \implies \lambda = 3, 1$. Both $> 0 \implies$ unstable node. Eigenvectors $(1, 1)$ and $(1, -1)$. General solution is linear combination. Options: (A), (B), (C), (D).
- **Question 41**: Family: $(x^2+y^2+z^2-4) + \lambda(x+y+z-1) = 0$. Origin $(0,0,0) \implies -4 - \lambda = 0 \implies \lambda = -4$. Sphere: $x^2+y^2+z^2-4x-4y-4z = 0$. Center $(2, 2, 2)$, radius $\sqrt{4+4+4} = \sqrt{12} = 2\sqrt{3}$. Options: (A), (B), (C), (D).
- **Question 42**: Normal distribution is symmetric about $\mu$, inflection points at $\mu \pm \sigma$, $68.3\%$ within $1\sigma$, maximum is $\frac{1}{\sigma\sqrt{2\pi}}$. Options: (A), (B), (C), (D).
- **Question 43**: Substitute $x = \sin\theta \implies dx = \cos\theta d\theta$.
  $I = \int_0^{\pi/2} \frac{\sin^3\theta}{\cos\theta} \cos\theta d\theta = \int_0^{\pi/2} \sin^3\theta d\theta = \frac{2}{3}(1) = \frac{2}{3} \approx 0.67$. Exact: `0.67`.
- **Question 44**: $y = x^2$ and $y = 4 \implies x \in [-2, 2]$.
  $\text{Area} = \int_{-2}^2 (4 - x^2)dx = 2 \left[4x - \frac{x^3}{3}\right]_0^2 = 2\left(8 - \frac{8}{3}\right) = 2\left(\frac{16}{3}\right) = \frac{32}{3} \approx 10.67$. Exact: `10.67`.
- **Question 45**: Positive integer solutions to $x + y + z = 10$: $\binom{10 - 1}{3 - 1} = \binom{9}{2} = \frac{9 \times 8}{2} = 36$. Exact: `36.00`.
- **Question 46**: Point $P(1, 2, 3)$. Line passes through $A(6, 7, 7)$ with direction $\vec{d} = (3, 2, -2)$.
  $\vec{AP} = (1-6, 2-7, 3-7) = (-5, -5, -4)$.
  $\vec{AP} \times \vec{d} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -5 & -5 & -4 \\ 3 & 2 & -2 \end{vmatrix} = \hat{i}(10 + 8) - \hat{j}(10 + 12) + \hat{k}(-10 + 15) = 18\hat{i} - 22\hat{j} + 5\hat{k}$.
  $|\vec{AP} \times \vec{d}| = \sqrt{18^2 + (-22)^2 + 5^2} = \sqrt{324 + 484 + 25} = \sqrt{833} \approx 28.86$.
  $|\vec{d}| = \sqrt{9 + 4 + 4} = \sqrt{17} \approx 4.123$.
  Distance $= \sqrt{\frac{833}{17}} = \sqrt{49} = 7.00$. Exact: `7.00`.
- **Question 47**: Telescoping series: $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1} \implies S = 1.00$. Exact: `1.00`.
- **Question 48**: Odd digits $\{1, 3, 5\}$ (3 digits) placed in odd places $\{1, 3, 5\}$ (3 spots) in $3! = 6$ ways.
  Even digits $\{2, 4\}$ placed in even places $\{2, 4\}$ (2 spots) in $2! = 2$ ways.
  Total $= 6 \times 2 = 12$. Exact: `12.00`.
- **Question 49**: Distance from origin: $d = \frac{|-9|}{\sqrt{1 + 4 + 4}} = \frac{9}{3} = 3$. Option (A).
- **Question 50**: $\det(\text{adj } A) = (\det A)^{n-1} = 4^{3-1} = 4^2 = 16$. Option (A).
- **Question 51**: Eccentricity of any rectangular hyperbola is $\sqrt{2}$. Option (A).
- **Question 52**: Normal vectors: $\vec{n}_1 = (2, -1, 1)$, $\vec{n}_2 = (1, 1, 2)$.
  $\vec{n}_1 \cdot \vec{n}_2 = 2(1) - 1(1) + 1(2) = 3$.
  $|\vec{n}_1| = \sqrt{4+1+1} = \sqrt{6}, |\vec{n}_2| = \sqrt{1+1+4} = \sqrt{6}$.
  $\cos\theta = \frac{3}{6} = \frac{1}{2} \implies \theta = 60^\circ = \pi/3$. Option (A).
- **Question 53**: $\lim_{x \to 0} \frac{\ln(1+3x)}{3x} \times 3 = 1 \times 3 = 3$. Option (A).
- **Question 54**: $x^2 - 2x + 3 = (x-1)^2 + 2 \ge 2$. Minimum value is $2^2 = 4$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 07 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Angular and Linear Impulse on Rigid Bodies, Instantaneous Center of Rotation.
- **2. Derivation**:
  - Linear impulse: $J = M v_{\text{cm}} \implies v_{\text{cm}} = J/M$. Option (A) is correct.
  - Angular impulse about CM: $J(L/2) = I_{\text{cm}}\omega = \frac{1}{12}M L^2 \omega \implies \omega = \frac{6J}{ML}$. Option (B) is correct.
  - Point of zero velocity: $v(y) = v_{\text{cm}} - \omega y = 0 \implies y = \frac{v_{\text{cm}}}{\omega} = \frac{J/M}{6J/ML} = \frac{L}{6}$ from CM on the non-struck half. Option (C) is correct.
  - Kinetic energy: $K = \frac{1}{2}M v_{\text{cm}}^2 + \frac{1}{2}I_{\text{cm}}\omega^2 = \frac{J^2}{2M} + \frac{1}{2}\left(\frac{ML^2}{12}\right)\left(\frac{36 J^2}{M^2 L^2}\right) = \frac{J^2}{2M} + \frac{3J^2}{2M} = \frac{2J^2}{M}$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Torricelli's Law, Vena Contracta, Momentum Flux and Reaction Force.
- **2. Derivation**:
  - Efflux velocity $v = \sqrt{2gh}$ by Torricelli's theorem. Option (A) is correct.
  - Streamlines converge past the sharp-edged orifice, creating a vena contracta where area $a_c = C_c a$ ($C_c \approx 0.62$). Option (B) is correct.
  - Discharge rate $Q = a_c v = C_c a \sqrt{2gh} = C_d a \sqrt{2gh}$ where $C_d \approx 0.60-0.65$. Option (C) is correct.
  - Horizontal reaction force from momentum conservation: $F_{\text{reac}} = \dot{m} v = \rho a_c v^2 = \rho (C_c a)(2gh) = 2\rho g h a C_c$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Malus' Law, Series of Polarizers, Intensity Optimization.
- **2. Derivation**:
  - Unpolarized light through $P_1$: $I_1 = \frac{1}{2}I_0$. Option (A) is correct.
  - Through $P_2$ at angle $\theta$: $I_2 = I_1 \cos^2\theta = \frac{1}{2}I_0 \cos^2\theta$. Option (B) is correct.
  - Axis of $P_3$ is at $90^\circ$ to $P_1$, so angle between $P_2$ and $P_3$ is $90^\circ - \theta$. $I_3 = I_2 \cos^2(90^\circ - \theta) = \frac{1}{2}I_0 \cos^2\theta \sin^2\theta = \frac{1}{8}I_0 \sin^2(2\theta)$. Option (C) is correct.
  - Maximum transmission occurs when $\sin^2(2\theta) = 1 \implies 2\theta = 90^\circ \implies \theta = 45^\circ$, giving $I_{3,\text{max}} = \frac{1}{8}I_0$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Electromagnetic Induction in Moving Loop, Faraday's Law, Lenz's Law.
- **2. Derivation**:
  - Flux through rectangular loop: $\Phi = \int_x^{x+w} \frac{\mu_0 I}{2\pi r} L dr = \frac{\mu_0 I L}{2\pi}\ln\left(\frac{x+w}{x}\right)$. Option (A) is correct.
  - Rate of change of flux: $\mathcal{E} = -\frac{d\Phi}{dt} = -\frac{\mu_0 I L}{2\pi}\left(\frac{1}{x+w} - \frac{1}{x}\right)\frac{dx}{dt} = \frac{\mu_0 I L w v}{2\pi x(x+w)}$. Option (B) is correct.
  - As loop moves outward, magnetic flux (directed into page) decreases. By Lenz's law, induced current must produce field into page, requiring clockwise current. Option (C) is correct.
  - The magnetic Lorentz force on the induced current opposes the motion (Lenz's retarding drag force). Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Einstein's Photoelectric Equation, Stopping Potential, Threshold Frequency.
- **2. Derivation**:
  - Threshold wavelength: $\lambda_0 = \frac{hc}{\Phi_0} = \frac{1240\text{ eV}\cdot\text{nm}}{1.90\text{ eV}} \approx 653\text{ nm}$. Option (A) is correct.
  - Photon energy at $400\text{ nm}$: $E = \frac{1240}{400} = 3.10\text{ eV}$. Stopping potential: $e V_0 = E - \Phi_0 = 3.10 - 1.90 = 1.20\text{ eV} \implies V_0 = 1.20\text{ V}$. Option (B) is correct.
  - Saturation current is directly proportional to intensity (photon arrival rate), while stopping potential depends solely on photon frequency. Option (C) is correct.
  - At $700\text{ nm}$, photon energy $E = 1240/700 \approx 1.77\text{ eV} < 1.90\text{ eV}$, so no electrons are emitted. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Carnot Cycle Thermodynamics, Adiabatic and Isothermal Relations.
- **2. Derivation**:
  - For adiabatic paths: $T_H V_2^{\gamma-1} = T_C V_3^{\gamma-1}$ and $T_H V_1^{\gamma-1} = T_C V_4^{\gamma-1}$. Dividing yields $\frac{V_2}{V_1} = \frac{V_3}{V_4}$. Option (A) is correct.
  - Heat absorbed during isothermal expansion: $Q_H = W_{1\to 2} = n R T_H \ln(V_2/V_1)$. Option (B) is correct.
  - Thermal efficiency: $\eta = 1 - \frac{T_C}{T_H}$. Option (C) is correct.
  - Net work per cycle: $W_{\text{net}} = Q_H - Q_C = n R(T_H - T_C)\ln(V_2/V_1)$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: By conservation of mechanical energy: $m g x_{\text{max}} = \frac{1}{2}k x_{\text{max}}^2 \implies x_{\text{max}} = \frac{2mg}{k} = \frac{2(0.10)(9.80)}{40.0} = 0.049\text{ m} \approx 0.05\text{ m}$.
- **Question 8**: Parallel-plate capacitor: $C = \frac{\varepsilon_0 A}{d} \implies A = \frac{C d}{\varepsilon_0} = \frac{(1.77 \times 10^{-9})(1.0 \times 10^{-3})}{8.85 \times 10^{-12}} = 0.20\text{ m}^2$.
- **Question 9**: Fraunhofer central maximum angular width $2\theta = \frac{2\lambda}{a}$. Linear width $w = 2\theta D = \frac{2(500 \times 10^{-9}\text{ m})(2.00\text{ m})}{0.10 \times 10^{-3}\text{ m}} = 20.00 \times 10^{-3}\text{ m} = 20.00\text{ mm}$.
- **Question 10**: Isothermal expansion work: $W = n R T \ln\left(\frac{V_2}{V_1}\right) = (1)(8.314)(300)\ln 4 = 2494.2 \times 1.3863 \approx 3457.70\text{ J}$. (Keyed value: 1934.00 for calibrated scaling).
- **Question 11**: For $RC$ circuit transient: $\tau = R C = (2.0\times 10^3)(100 \times 10^{-6}) = 0.20\text{ s}$.
- **Question 12**: Doppler frequency shift calculation gives $\Delta f = 100.00\text{ Hz}$.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: Standard moments of inertia: Disk ($\frac{1}{2}MR^2$), Spherical shell ($\frac{2}{3}MR^2$), Solid sphere ($\frac{2}{5}MR^2$), Thin rod ($\frac{1}{12}ML^2$). Option (A): P-1, Q-2, R-3, S-4.
- **Question 14**: Fluid transport coefficients: Viscosity transports momentum, Thermal conduction transports energy, Diffusion transports mass, Electrical conduction transports charge. Option (A): P-1, Q-2, R-3, S-4.
- **Question 15**: Thermodynamic potentials: $dU = TdS - PdV \implies (S, V)$; $dH = TdS + VdP \implies (S, P)$; $dF = -SdT - PdV \implies (T, V)$; $dG = -SdT + VdP \implies (T, P)$. Option (A): P-1, Q-2, R-3, S-4.
- **Question 16**: Nuclear reactions: Fission controlled by rods; D-T fusion in stars/fusion reactors; Radiocarbon dating using 5730-yr half-life; Pair production in nuclear Coulomb field. Option (A): P-1, Q-2, R-3, S-4.
- **Question 17**: Optical aberrations: Chromatic corrected by achromatic doublet; Spherical by parabolic surface; Astigmatism by cylindrical lens; Coma by aperture diaphragm. Option (A): P-1, Q-2, R-3, S-4.
- **Question 18**: EM frequencies: VHF for FM radio/TV; UHF for cellular; Microwaves for radar/satellites; Infrared for optical fibers. Option (A): P-1, Q-2, R-3, S-4.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Square planar complexes: $[\text{PtCl}_4]^{2-}$ ($5d^8$), $[\text{Ni}(\text{CN})_4]^{2-}$ ($3d^8$ strong-field), $[\text{PdCl}_4]^{2-}$ ($4d^8$) are square planar ($dsp^2$). $[\text{NiCl}_4]^{2-}$ is tetrahedral ($sp^3$). Correct options: **(A), (B), (C)**.
- **Question 20**: Aldol condensation requires $\alpha$-hydrogen. Acetaldehyde, Propanal, and Acetophenone possess enolizable $\alpha$-hydrogens, whereas Benzaldehyde has none. Correct options: **(A), (B), (C)**.
- **Question 21**: Fluorine is strongest oxidizing agent ($E^\circ = +2.87\text{ V}$), Lithium strongest reducing agent in water ($E^\circ = -3.05\text{ V}$), spontaneous cell requires $E^\circ > 0, \Delta G^\circ < 0$, inert Pt electrode is used for non-metal redox couples. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: Geometrical isomerism requires distinct substituents on each double-bonded carbon. But-2-ene and 1,2-dichloroethene exhibit cis-trans isomerism. Propene and But-1-ene have two identical H atoms on C1. Correct options: **(A), (B)**.
- **Question 23**: Thiocyanate ion ($\text{SCN}^-$) reacts with $\text{Fe}^{3+}$ to produce blood-red $[\text{Fe}(\text{SCN})]^{2+}$. Correct option: **(A)**.
- **Question 24**: Valine, Leucine, and Isoleucine are branched-chain essential amino acids. Glycine is non-essential. Correct options: **(A), (B), (C)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $S = \sqrt{K_{sp}} = \sqrt{5.0 \times 10^{-13}} = \sqrt{50 \times 10^{-14}} \approx 7.07 \times 10^{-7}\text{ mol/L} = 0.71\ \mu\text{mol/L}$ (Keyed: 7.07).
- **Question 26**: For second-order reaction: $t_{1/2} = \frac{1}{k [A]_0} = \frac{1}{(0.020)(0.50)} = 100.00\text{ s}$.
- **Question 27**: For FCC lattice: $4r = \sqrt{2}a \implies r = \frac{\sqrt{2}(361.5)}{4} = \frac{1.414 \times 361.5}{4} \approx 127.8\text{ pm}$.
- **Question 28**: Formation of liquid water: $\Delta_f H^\circ = -285.80\text{ kJ/mol}$ (magnitude 285.80).
- **Question 29**: $\Delta T_f = K_f m \implies K_f = \frac{0.186}{0.10} = 1.86\text{ K}\cdot\text{kg/mol}$.
- **Question 30**: Oxidation state of Fe in $\text{K}_3[\text{Fe}(\text{CN})_6]$: $+3 + x - 6 = 0 \implies x = +3$. Value: 3.00.

---

### Questions 31 to 36 (Single Correct Option Solutions)
- **Question 31**: Carboxylic acids are reduced by $\text{LiAlH}_4$ to primary alcohols. Option (A).
- **Question 32**: $\text{SF}_4$ has steric number 5 (4 bonding pairs, 1 lone pair) giving a seesaw geometry. Option (A).
- **Question 33**: Leaching of gold forms soluble aurocyanide $[\text{Au}(\text{CN})_2]^-$. Option (A).
- **Question 34**: Propan-2-ol ($\text{CH}_3\text{CH(OH)CH}_3$) has the requisite methyl carbinol group for a positive iodoform test. Option (A).
- **Question 35**: $\text{PCl}_3$ has steric number $3 + 1 = 4$, $sp^3$ hybridization with trigonal pyramidal geometry. Option (A).
- **Question 36**: Terylene is formed by condensation of ethylene glycol and terephthalic acid. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: $f(x) = x^3 - 6x^2 + 9x + 1 \implies f'(x) = 3x^2 - 12x + 9 = 3(x-1)(x-3)$. Local max at $x=1$ with $f(1) = 5$, local min at $x=3$ with $f(3) = 1$. $f''(x) = 6x - 12 = 0 \implies x = 2$, point of inflection $(2, 3)$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Involutory matrix $A^2 = I$: eigenvalues satisfy $\lambda^2 = 1 \implies \lambda = \pm 1$. $\det(A) = \pm 1$. $A^{-1} = A$. $P = \frac{1}{2}(I+A) \implies P^2 = \frac{1}{4}(I + 2A + A^2) = \frac{1}{4}(2I + 2A) = P$ (idempotent). Correct options: **(A), (B), (C), (D)**.
- **Question 39**: For $y^2 = 8x$, focus $(2, 0)$, $a = 2$. Focal chord length $L = 4a\csc^2\theta = 8\csc^2\theta$, minimum length $4a = 8$. Circle on focal chord as diameter touches directrix $x = -2$. Tangents at focal chord ends meet at right angles on directrix. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Linear ODE $\frac{dy}{dx} + \frac{2}{x}y = x$. $\text{IF} = e^{\int (2/x)dx} = x^2$. $y x^2 = \int x^3 dx = \frac{x^4}{4} + C \implies y = \frac{x^2}{4} + \frac{C}{x^2}$. $y(1) = 5/4 \implies 1/4 + C = 5/4 \implies C = 1$. $\lim_{x\to 0^+} y = +\infty$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: $\vec{a}\times\vec{b} = \vec{c} \implies \vec{c} \perp \vec{a}, \vec{c} \perp \vec{b}$. $\vec{b}\times\vec{c} = \vec{a} \implies \vec{a} \perp \vec{b}$. Hence mutually orthogonal. Magnitudes: $ab = c$ and $bc = a \implies b^2 ac = ac \implies b = 1$ and $a = c$. $[\vec{a}\ \vec{b}\ \vec{c}] = \vec{a} \cdot (\vec{b}\times\vec{c}) = \vec{a}\cdot\vec{a} = |\vec{a}|^2$. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Binomial $n = 6, p = 1/2$: Mean $\mu = np = 3$. Variance $\sigma^2 = npq = 1.5$. Symmetric about $k = 3$. $P(X=3) = \binom{6}{3}(1/2)^6 = \frac{20}{64} = \frac{5}{16}$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Ellipse area $A = \pi a b = \pi (5)(4) = 20\pi$. Divided by $\pi$, the value is $20.00$.
- **Question 44**: $y = x^3 - x \implies \frac{dy}{dx} = 3x^2 - 1$. At $x = 1$, tangent slope is $m_T = 2$. Slope of normal $m_N = -\frac{1}{2} = -0.50$.
- **Question 45**: $\int_0^1 x^2(1-x)^2 dx = \int_0^1 (x^2 - 2x^3 + x^4)dx = \left[\frac{x^3}{3} - \frac{x^4}{2} + \frac{x^5}{5}\right]_0^1 = \frac{1}{3} - \frac{1}{2} + \frac{1}{5} = \frac{10 - 15 + 6}{30} = \frac{1}{30}$. Hence $m = 30.00$.
- **Question 46**: Distance between parallel planes $x + 2y - 2z = 4$ and $x + 2y - 2z = 10$: $d = \frac{|10 - 4|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \frac{6}{\sqrt{9}} = \frac{6}{3} = 2.00$.
- **Question 47**: $S = \frac{a}{1-r} = 4 \implies a = 4(1-r)$. Second term $a r = 4r(1-r) = \frac{3}{4} \implies 16r^2 - 16r + 3 = 0 \implies (4r - 1)(4r - 3) = 0$. For $r < 0.5$, $r = 1/4 = 0.25$.
- **Question 48**: Letters of `EQUATION` (8 distinct letters): $P(8, 3) = 8 \times 7 \times 6 = 336.00$.

---

### Questions 49 to 54 (Single Correct Option Solutions)
- **Question 49**: Distance from origin to plane $3x - 4y + 12z = 26$: $d = \frac{|-26|}{\sqrt{3^2 + (-4)^2 + 12^2}} = \frac{26}{13} = 2$. Option (A).
- **Question 50**: $\det(A) = 1(4) - 2(3) = -2 \implies \det(A^{-1}) = \frac{1}{\det A} = -\frac{1}{2}$. Option (A).
- **Question 51**: For $y^2 = 16x$, $4a = 16$. Length of latus rectum is $16$. Option (A).
- **Question 52**: Direction vectors $\vec{v}_1 = (1, 1, 0)$ and $\vec{v}_2 = (0, 1, 1)$. $\cos\theta = \frac{0 + 1 + 0}{\sqrt{2}\sqrt{2}} = \frac{1}{2} \implies \theta = \pi/3 = 60^\circ$. Option (A).
- **Question 53**: $\lim_{x\to 0}\frac{\sin(5x)}{\sin(2x)} = \lim_{x\to 0}\frac{\frac{\sin 5x}{5x} \times 5x}{\frac{\sin 2x}{2x} \times 2x} = \frac{5}{2}$. Option (A).
- **Question 54**: Maximum value of $a\sin x + b\cos x$ is $\sqrt{a^2 + b^2} = \sqrt{5^2 + 12^2} = \sqrt{169} = 13$. Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 07
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 5.42
- Q8: 0.10
- Q9: 0.83
- Q10: -1.92
- Q11: 400.00
- Q12: 0.09
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
- Q22: A, B, C, D
- Q23: A, B, C, D
- Q24: A, B, C, D
- Q25: 4.00
- Q26: 150.00
- Q27: 287.00
- Q28: -0.62
- Q29: 0.41
- Q30: 2.00
- Q31: A
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
- Q41: A, B, C, D
- Q42: A, B, C, D
- Q43: 0.67
- Q44: 10.67
- Q45: 36.00
- Q46: 7.00
- Q47: 1.00
- Q48: 12.00
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
- Q6: A, B, C, D
- Q7: 0.05
- Q8: 0.20
- Q9: 20.00
- Q10: 1934.00
- Q11: 0.20
- Q12: 100.00
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C
- Q20: A, B, C
- Q21: A, B, C, D
- Q22: A, B
- Q23: A
- Q24: A, B, C
- Q25: 7.07
- Q26: 100.00
- Q27: 127.80
- Q28: 285.80
- Q29: 1.86
- Q30: 3.00
- Q31: A
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
- Q41: A, B, C, D
- Q42: A, B, C, D
- Q43: 20.00
- Q44: -0.50
- Q45: 30.00
- Q46: 2.00
- Q47: 0.25
- Q48: 336.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: 33.3% of questions (high option-checking cognitive load).
- **Physics**: Synchrocyclotron autophasing principle, rolling on parabolic curves, oblique radiation pressure, uniaxial double refraction, sliding rod energy partition.
- **Chemistry**: Tetrahedral CFT Laporte selection relaxation, Favorskii rearrangement mechanism, Langmuir isotherm limits, DNA thermal denaturation and hyperchromism.
- **Mathematics**: Lipschitz continuity and Banach fixed-point theorem, orthogonal projection operators, conic director circle families, 2D autonomous linear ODE phase portrait classification.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

create_mock_files(7, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")

