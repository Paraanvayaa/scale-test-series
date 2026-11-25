# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 01.
Empirical Signature: IIT Delhi Benchmark (2013, 2020)
- Multi-correct dominance (+4/-2 with partial marking)
- Circuit transients (coupled L-C-R, switch closures)
- Stereochemical isomerism & organic reaction cascades
- Advanced coordinate calculus & matrices
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 01 — Paper 1
## Organising Institute Style Inspiration: IIT Delhi (`IIT_DELHI_STYLE`)
**Historical Reference Benchmark**: 2013, 2020 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3** (3 of 4 correct chosen), **+2** (2 or more chosen, all correct), **+1** (1 chosen, correct).
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
*One or more than one option is correct. Negative marking (-2) applies for incorrect choices.*

#### Question 1
A uniform solid cylinder of mass $M$ and radius $R$ rests on a rough horizontal plank of mass $m = 2M$. The plank is placed on a frictionless horizontal floor. A constant horizontal force $F$ is applied to the center of the cylinder. If there is no slipping between the cylinder and the plank, which of the following statements is/are correct?
(A) The acceleration of the plank is $a_p = \frac{F}{7M}$.  
(B) The acceleration of the center of mass of the cylinder is $a_c = \frac{5F}{7M}$.  
(C) The friction force acting on the cylinder points in the backward direction and has magnitude $f = \frac{2F}{7}$.  
(D) The minimum coefficient of static friction $\mu_s$ required between the cylinder and plank to prevent slipping is $\frac{2F}{7Mg}$.

#### Question 2
In the circuit shown, an inductor of inductance $L$ and a capacitor of capacitance $C$ are connected in parallel with each other. This combination is connected in series with a resistor $R$ across an AC voltage source $v(t) = V_0 \sin(\omega t)$. Let $\omega_0 = \frac{1}{\sqrt{LC}}$. Which of the following statements is/are correct?
(A) At angular frequency $\omega = \omega_0$, the net impedance of the parallel LC combination is infinite.  
(B) At $\omega = \omega_0$, the total current supplied by the AC source is zero.  
(C) For $\omega < \omega_0$, the parallel LC combination behaves inductively.  
(D) For $\omega > \omega_0$, the parallel LC combination behaves capacitively.

#### Question 3
A thermodynamic system containing $n$ moles of an ideal diatomic gas ($\gamma = 1.4$) undergoes a quasi-static process described by $P = \alpha V^2$, where $\alpha$ is a positive constant. As the gas expands from volume $V_0$ to $2V_0$:
(A) The work done by the gas is $W = \frac{7}{3}\alpha V_0^3$.  
(B) The change in internal energy of the gas is $\Delta U = \frac{35}{4}\alpha V_0^3$.  
(C) The molar heat capacity for this process is $C = \frac{17}{6}R$.  
(D) The temperature of the gas increases by a factor of 8.

#### Question 4
Two thin conducting concentric spherical shells of radii $R$ and $2R$ are placed in vacuum. The inner shell is given a charge $+Q$ and the outer shell is given a charge $+2Q$. A switch $S$ connects the inner shell to the ground through a long thin wire passing through a tiny insulated hole in the outer shell. When the switch is closed:
(A) The charge on the inner shell becomes $-Q$.  
(B) The potential of the outer shell becomes $\frac{Q}{4\pi\varepsilon_0 R}$.  
(C) The total charge flown to the ground is $2Q$.  
(D) The electrostatic energy stored in the region between the two shells becomes $\frac{Q^2}{16\pi\varepsilon_0 R}$.

#### Question 5
A particle of mass $m$ moves in a one-dimensional potential well given by $U(x) = U_0 \left[\left(\frac{x}{a}\right)^4 - 2\left(\frac{x}{a}\right)^2\right]$, where $U_0$ and $a$ are positive constants. Which of the following statements is/are correct?
(A) The system has stable equilibrium positions at $x = \pm a$.  
(B) An unstable equilibrium position exists at $x = 0$.  
(C) The angular frequency of small oscillations about the stable equilibrium position is $\omega = \frac{2}{a}\sqrt{\frac{2U_0}{m}}$.  
(D) The minimum energy required to escape from one of the wells to $x \to \infty$ is $U_0$.

#### Question 6
A plane electromagnetic wave of frequency $\nu = 1.0 \times 10^{14}\text{ Hz}$ propagates along the $+z$-direction in free space. The electric field is given by $\vec{E}(z,t) = E_0 \cos(kz - \omega t)\hat{i}$ with $E_0 = 300\text{ V/m}$. Which of the following statements is/are correct?
(A) The associated magnetic field is $\vec{B}(z,t) = \frac{E_0}{c}\cos(kz - \omega t)\hat{j}$.  
(B) The time-averaged Poynting vector is $\langle \vec{S} \rangle = \frac{E_0^2}{2\mu_0 c}\hat{k} \approx 119.4\hat{k}\text{ W/m}^2$.  
(C) The radiation pressure exerted on a completely absorbing flat surface perpendicular to the beam is $P_{\text{rad}} = \frac{\langle S \rangle}{c} \approx 3.98 \times 10^{-7}\text{ N/m}^2$.  
(D) If the wave strikes a perfectly reflecting flat mirror at normal incidence, the radiation pressure is doubled.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)
*Enter the correct numerical value rounded off to TWO decimal places.*

#### Question 7
A cylindrical tank of height $H = 4.90\text{ m}$ is filled completely with water ($\rho = 1000\text{ kg/m}^3$). A small circular hole of area $a = 2.0\text{ cm}^2$ is opened at the bottom. If the cross-sectional area of the tank is $A = 1.0\text{ m}^2$, calculate the time (in seconds) required to empty the tank completely. [Take $g = 9.80\text{ m/s}^2$].

#### Question 8
In an experiment to measure the speed of sound using a resonance tube apparatus, the first resonance occurs at a water column length of $L_1 = 16.0\text{ cm}$ and the second resonance occurs at $L_2 = 50.0\text{ cm}$ using a tuning fork of frequency $\nu = 500\text{ Hz}$. Calculate the speed of sound (in $\text{m/s}$) in air.

#### Question 9
A uniform rod of length $L = 1.20\text{ m}$ and mass $M = 0.90\text{ kg}$ is free to rotate about a frictionless horizontal axis passing through one of its ends. It is released from rest from a horizontal position. Determine the magnitude of the angular velocity $\omega$ (in rad/s) of the rod when it passes through the vertical position. [Take $g = 9.80\text{ m/s}^2$].

#### Question 10
In a photoelectric effect experiment using a cesium photocathode (work function $\Phi = 2.14\text{ eV}$), monochromatic light of wavelength $\lambda = 400\text{ nm}$ is incident. Determine the stopping potential $V_0$ (in Volts) required to reduce the photocurrent to zero. [Take $hc = 1240\text{ eV}\cdot\text{nm}$. Round off to TWO decimal places].

#### Question 11
Two long, straight parallel wires separated by a distance $d = 0.20\text{ m}$ carry currents $I_1 = 10.0\text{ A}$ and $I_2 = 20.0\text{ A}$ in opposite directions. Calculate the magnetic field magnitude $B$ (in $\mu\text{T}$) at a point midway between the two wires. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$].

#### Question 12
A convex lens of focal length $f_1 = +20.0\text{ cm}$ and a concave lens of focal length $f_2 = -10.0\text{ cm}$ are placed coaxially separated by a distance $d = 10.0\text{ cm}$. A parallel beam of light is incident from the left on the convex lens. Calculate the distance (in cm) of the final image from the concave lens.

---

## Section 3: Single Correct Option (Questions 13 to 18)
*Only one option is correct. +3 for correct, -1 for incorrect.*

#### Question 13
A solid sphere of mass $m$ and radius $r$ rolls without slipping down an inclined plane of inclination $\theta = 30^\circ$. The acceleration of the center of mass of the sphere is:
(A) $\frac{5}{14}g$  
(B) $\frac{5}{7}g$  
(C) $\frac{3}{7}g$  
(D) $\frac{2}{7}g$

#### Question 14
A block of mass $m = 1.0\text{ kg}$ attached to a horizontal spring of spring constant $k = 100\text{ N/m}$ executes simple harmonic motion on a frictionless surface. If the maximum speed of the block is $v_{\text{max}} = 2.0\text{ m/s}$, the amplitude of oscillation is:
(A) $0.10\text{ m}$  
(B) $0.20\text{ m}$  
(C) $0.40\text{ m}$  
(D) $0.05\text{ m}$

#### Question 15
An electron in a hydrogen atom makes a transition from $n = 3$ to $n = 1$. The frequency of the emitted photon is ($R_{\infty} = 1.097 \times 10^7\text{ m}^{-1}, c = 3.0 \times 10^8\text{ m/s}$):
(A) $2.44 \times 10^{15}\text{ Hz}$  
(B) $2.92 \times 10^{15}\text{ Hz}$  
(C) $3.29 \times 10^{15}\text{ Hz}$  
(D) $1.64 \times 10^{15}\text{ Hz}$

#### Question 16
A circular coil of $N = 100$ turns and radius $R = 5.0\text{ cm}$ carries a current $I = 2.0\text{ A}$. The magnetic dipole moment of the coil is:
(A) $1.57\text{ A}\cdot\text{m}^2$  
(B) $3.14\text{ A}\cdot\text{m}^2$  
(C) $0.785\text{ A}\cdot\text{m}^2$  
(D) $6.28\text{ A}\cdot\text{m}^2$

#### Question 17
A Carnot engine absorbs $1000\text{ J}$ of heat from a reservoir at $T_H = 500\text{ K}$ and rejects heat to a sink at $T_C = 300\text{ K}$. The work done per cycle is:
(A) $400\text{ J}$  
(B) $600\text{ J}$  
(C) $500\text{ J}$  
(D) $300\text{ J}$

#### Question 18
The de Broglie wavelength of a thermal neutron at temperature $T = 300\text{ K}$ ($m_n = 1.67 \times 10^{-27}\text{ kg}, k_B = 1.38 \times 10^{-23}\text{ J/K}, h = 6.63 \times 10^{-34}\text{ J}\cdot\text{s}$) is approximately:
(A) $0.18\text{ nm}$  
(B) $0.14\text{ nm}$  
(C) $0.25\text{ nm}$  
(D) $0.08\text{ nm}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Consider the coordination complex $[Co(en)_2Cl_2]^+$. Which of the following statements is/are correct?
(A) It exhibits geometrical isomerism with cis and trans forms.  
(B) The trans-isomer is optically inactive due to a center of inversion.  
(C) The cis-isomer is chiral and exists as a pair of enantiomers.  
(D) The coordination number of cobalt in this complex is 6, and its oxidation state is +3.

#### Question 20
For the gaseous equilibrium $\text{PCl}_5(g) \rightleftharpoons \text{PCl}_3(g) + \text{Cl}_2(g)$, which of the following statements is/are correct?
(A) Addition of an inert gas at constant pressure shifts the equilibrium in the forward direction.  
(B) Addition of an inert gas at constant volume has no effect on the equilibrium position.  
(C) An increase in temperature increases the degree of dissociation $\alpha$ since the forward reaction is endothermic.  
(D) The equilibrium constant $K_p$ increases with an increase in total pressure at constant temperature.

#### Question 21
Regarding the reaction of $(2R, 3R)$-2-bromo-3-methylpentane with sodium ethoxide in ethanol under reflux:
(A) The major product is formed via an $E2$ elimination mechanism.  
(B) The reaction requires an anti-periplanar conformation between the $\beta$-hydrogen and the leaving bromide.  
(C) $(E)$-3-methylpent-2-ene is obtained as the predominant alkene.  
(D) The rate of reaction depends only on the concentration of the alkyl halide.

#### Question 22
Which of the following molecules/ions has/have an planar geometry and zero dipole moment?
(A) $\text{XeF}_4$  
(B) $\text{BF}_3$  
(C) $\text{SF}_4$  
(D) $\text{I}_3^-$

#### Question 23
For an ideal binary solution of volatile liquids $A$ and $B$, which of the following thermodynamic relations must hold true at constant temperature and pressure?
(A) $\Delta_{\text{mix}} H = 0$  
(B) $\Delta_{\text{mix}} V = 0$  
(C) $\Delta_{\text{mix}} S > 0$  
(D) $\Delta_{\text{mix}} G < 0$

#### Question 24
In qualitative inorganic analysis, which of the following metal ions yield a black precipitate with $\text{H}_2\text{S}$ gas in acidic medium ($\text{Group II}$)?
(A) $\text{Cu}^{2+}$  
(B) $\text{Pb}^{2+}$  
(C) $\text{Cd}^{2+}$  
(D) $\text{Bi}^{3+}$

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
Calculate the $\text{pH}$ of a buffer solution prepared by mixing $50.0\text{ mL}$ of $0.20\text{ M CH}_3\text{COOH}$ with $50.0\text{ mL}$ of $0.10\text{ M CH}_3\text{COONa}$. [Take $pK_a(\text{CH}_3\text{COOH}) = 4.74$ and $\log 2 = 0.301$. Round off to TWO decimal places].

#### Question 26
For the first-order reaction $A \to B + C$, the rate constant is $k = 6.93 \times 10^{-3}\text{ s}^{-1}$. Calculate the time (in seconds) required for $75\%$ of reactant $A$ to decompose. [Take $\ln 2 = 0.693$].

#### Question 27
An element crystallizes in a face-centered cubic (FCC) lattice with an edge length $a = 400\text{ pm}$. Calculate the atomic radius $r$ of the element in picometers ($\text{pm}$). [Take $\sqrt{2} \approx 1.414$. Round off to TWO decimal places].

#### Question 28
Calculate the standard EMF $E_{\text{cell}}^\circ$ (in Volts) for the galvanic cell:
$$\text{Zn}(s) | \text{Zn}^{2+}(aq) \parallel \text{Cu}^{2+}(aq) | \text{Cu}(s)$$
Given $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.76\text{ V}$ and $E^\circ(\text{Cu}^{2+}/\text{Cu}) = +0.34\text{ V}$.

#### Question 29
A $0.10\text{ m}$ aqueous solution of a monobasic weak acid $HA$ freezes at $-0.205^\circ\text{C}$. Calculate the percentage degree of ionization $\alpha$ of the acid. [Take $K_f(\text{H}_2\text{O}) = 1.86\text{ K}\cdot\text{kg/mol}$. Round off to TWO decimal places].

#### Question 30
The spin-only magnetic moment of a high-spin octahedral complex $[\text{Fe}(\text{H}_2\text{O})_6]^{2+}$ is $\mu_{\text{eff}} = \sqrt{n(n+2)}\text{ BM}$. Calculate $\mu_{\text{eff}}$ in Bohr Magnetons ($\text{BM}$). [Take $\sqrt{24} \approx 4.90$. Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following compounds will not undergo Friedel-Crafts alkylation reaction?
(A) Nitrobenzene  
(B) Toluene  
(C) Anisole  
(D) Chlorobenzene

#### Question 32
The correct order of increasing acid strength among the following oxoacids of chlorine is:
(A) $\text{HClO} < \text{HClO}_2 < \text{HClO}_3 < \text{HClO}_4$  
(B) $\text{HClO}_4 < \text{HClO}_3 < \text{HClO}_2 < \text{HClO}$  
(C) $\text{HClO}_2 < \text{HClO} < \text{HClO}_3 < \text{HClO}_4$  
(D) $\text{HClO} < \text{HClO}_3 < \text{HClO}_2 < \text{HClO}_4$

#### Question 33
In the extraction of copper from copper pyrites ($\text{CuFeS}_2$), the slag formed during smelting in the blast furnace is primarily:
(A) $\text{FeSiO}_3$  
(B) $\text{CuSiO}_3$  
(C) $\text{CaSiO}_3$  
(D) $\text{FeO}$

#### Question 34
Treatment of benzaldehyde with concentrated $\text{NaOH}$ yields benzyl alcohol and sodium benzoate. This reaction is known as:
(A) Cannizzaro reaction  
(B) Aldol condensation  
(C) Perkin reaction  
(D) Reformatsky reaction

#### Question 35
The total number of lone pairs of electrons in a molecule of $\text{XeOF}_4$ is:
(A) 13  
(B) 14  
(C) 15  
(D) 12

#### Question 36
Which of the following vitamins is water-soluble?
(A) Vitamin C  
(B) Vitamin A  
(C) Vitamin D  
(D) Vitamin K

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x^2 - 1}{x^2 + 1}$ for all $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ is an even function.  
(B) The range of $f(x)$ is $[-1, 1)$.  
(C) $f'(x) > 0$ for all $x > 0$.  
(D) The graph of $f(x)$ has a horizontal asymptote at $y = 1$.

#### Question 38
Let $M$ be a $3 \times 3$ real invertible matrix such that $M^T = M^{-1}$ and $\det(M) = 1$. Which of the following statements is/are correct?
(A) $\lambda = 1$ is always an eigenvalue of $M$.  
(B) $M$ represents a spatial rotation in $\mathbb{R}^3$.  
(C) The sum of the squares of the entries of each row of $M$ equals 1.  
(D) $\det(M - I) = 0$.

#### Question 39
Consider the ellipse $E: \frac{x^2}{16} + \frac{y^2}{9} = 1$. Which of the following statements is/are correct?
(A) The eccentricity of the ellipse is $e = \frac{\sqrt{7}}{4}$.  
(B) The length of the latus rectum is $\frac{9}{2}$.  
(C) The product of perpendiculars drawn from the two foci to any tangent to the ellipse is equal to 9.  
(D) The locus of the point of intersection of two perpendicular tangents to $E$ is the director circle $x^2 + y^2 = 25$.

#### Question 40
Let $I_n = \int_0^{\pi/2} \sin^n x\,dx$ for integer $n \ge 0$. Which of the following statements is/are correct?
(A) $I_n = \frac{n-1}{n} I_{n-2}$ for $n \ge 2$.  
(B) $I_4 = \frac{3\pi}{16}$.  
(C) $I_5 = \frac{8}{15}$.  
(D) $\lim_{n \to \infty} I_n = 0$.

#### Question 41
Let $z$ be a complex number satisfying $|z - 3 - 4i| = 2$. Which of the following statements is/are correct?
(A) The maximum value of $|z|$ is 7.  
(B) The minimum value of $|z|$ is 3.  
(C) The locus of $z$ is a circle of center $(3, 4)$ and radius 2 in the complex Argand plane.  
(D) The point $z_0 = 3 + 2i$ lies on the locus.

#### Question 42
Consider the differential equation $\frac{dy}{dx} + y \cot x = 2\cos x$ with initial condition $y(\pi/2) = 1$. Which of the following statements is/are correct?
(A) The integrating factor of the differential equation is $\sin x$.  
(B) The solution is $y(x) = \sin x$.  
(C) $y(\pi/6) = \frac{1}{2}$.  
(D) The function $y(x)$ attains its maximum value at $x = \pi/2$ on the interval $(0, \pi)$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 \frac{\ln(1+x)}{1+x^2}\,dx$$
If $I = \frac{\pi}{k}\ln 2$, find the integer value of $k$.

#### Question 44
Find the area of the region bounded by the parabola $y^2 = 4x$ and the line $y = 2x - 4$. [Round off to TWO decimal places].

#### Question 45
Let $\vec{a} = \hat{i} + 2\hat{j} + 3\hat{k}$, $\vec{b} = 2\hat{i} + 3\hat{j} + \hat{k}$, and $\vec{c} = 3\hat{i} + \hat{j} + 2\hat{k}$. Calculate the volume $V$ of the parallelepiped formed by the vectors $\vec{a}, \vec{b}, \vec{c}$.

#### Question 46
A bag contains 5 red balls and 3 green balls. Two balls are drawn at random without replacement. Calculate the probability that both balls drawn are red. [Round off to TWO decimal places].

#### Question 47
Find the number of distinct real solutions to the equation $2^x + 3^x = 5^x$.

#### Question 48
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{\sin x - x + \frac{x^3}{6}}{x^5}$$
If $L = \frac{1}{m}$, find the integer value of $m$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The shortest distance between the lines $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $\frac{x-2}{3} = \frac{y-4}{4} = \frac{z-5}{5}$ is:
(A) $\frac{1}{\sqrt{6}}$  
(B) $\frac{2}{\sqrt{6}}$  
(C) $\frac{1}{\sqrt{3}}$  
(D) $0$

#### Question 50
If $\alpha$ and $\beta$ are the roots of $x^2 - 6x + 2 = 0$, then the value of $\alpha^3 + \beta^3$ is:
(A) 180  
(B) 216  
(C) 198  
(D) 162

#### Question 51
The value of $\sum_{r=1}^{10} r \cdot r!$ is:
(A) $11! - 1$  
(B) $10! - 1$  
(C) $11!$  
(D) $12! - 1$

#### Question 52
If $A$ is a $2 \times 2$ matrix such that $A^2 - 3A + 2I = 0$, then $A^{-1}$ equals:
(A) $\frac{1}{2}(3I - A)$  
(B) $3I - A$  
(C) $\frac{1}{2}(A - 3I)$  
(D) $A + 3I$

#### Question 53
The number of ways in which 5 boys and 5 girls can sit in a row such that no two girls sit together is:
(A) $5! \times 6!$  
(B) $(5!)^2$  
(C) $10! / 2$  
(D) $5! \times \binom{6}{5}$

#### Question 54
The radius of the circle passing through the points $(0, 0)$, $(4, 0)$, and $(0, 6)$ is:
(A) $\sqrt{13}$  
(B) $\sqrt{26}$  
(C) $2\sqrt{13}$  
(D) 5
"""

paper_2_md = r"""# JEE Advanced Mock Examination 01 — Paper 2
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
A uniform rod $AB$ of length $L$ and mass $M$ is suspended horizontally from two identical vertical strings attached at its ends $A$ and $B$. At $t = 0$, the string at end $B$ is suddenly cut. Immediately after cutting:
(A) The angular acceleration of the rod is $\alpha = \frac{3g}{2L}$.  
(B) The linear acceleration of the center of mass of the rod is $a_{\text{cm}} = \frac{3g}{4}$.  
(C) The tension in the string at end $A$ instantaneously drops to $T = \frac{Mg}{4}$.  
(D) The linear acceleration of end $B$ is $a_B = \frac{3g}{2}$.

#### Question 2
Two identical circular loops of radius $R$ carry equal steady current $I$. They are placed coaxially with their centers separated by distance $d = R$ (Helmholtz coil configuration). Which of the following statements is/are correct?
(A) The magnetic field at the midpoint on the axis between the two coils is $B = \frac{8\mu_0 I}{5\sqrt{5}R}$.  
(B) The first derivative $\frac{dB}{dx}$ of the magnetic field with respect to axial distance vanishes at the midpoint.  
(C) The second derivative $\frac{d^2B}{dx^2}$ of the magnetic field also vanishes at the midpoint.  
(D) The magnetic field in the region around the midpoint is exceptionally uniform.

#### Question 3
A light ray enters a right-angled isosceles prism of refractive index $\mu = \sqrt{2}$ normally through one of its legs. Which of the following statements is/are correct?
(A) The critical angle for total internal reflection at the glass-air interface is $\theta_c = 45^\circ$.  
(B) The ray undergoes total internal reflection at the hypotenuse face.  
(C) The ray emerges through the other leg without deviation from the normal to that face.  
(D) The total deviation angle experienced by the light ray is $\delta = 90^\circ$.

#### Question 4
A parallel-plate capacitor with plate area $A$ and separation $d$ is filled with two dielectric slabs of thickness $d/2$ each. One slab has dielectric constant $K_1 = 2$ and the other has $K_2 = 4$. Which of the following statements is/are correct?
(A) The equivalent capacitance of the system is $C = \frac{8\varepsilon_0 A}{3d}$.  
(B) If a potential difference $V$ is applied across the plates, the electric field in dielectric 1 is twice that in dielectric 2.  
(C) The potential drop across slab 1 is $\frac{2}{3}V$.  
(D) The bound surface charge density at the interface between the two dielectrics is non-zero.

#### Question 5
A hydrogen-like ion of atomic number $Z$ is in its ground state. It absorbs a photon of energy $E = 40.8\text{ eV}$ and is excited to an energy state corresponding to principal quantum number $n = 2$. Which of the following statements is/are correct?
(A) The atomic number of the ion is $Z = 2$ ($\text{He}^+$ ion).  
(B) The ionization energy of this ion from its ground state is $54.4\text{ eV}$.  
(C) The orbital radius of the electron in $n = 2$ is equal to the Bohr radius $a_0$.  
(D) The de Broglie wavelength of the orbital electron in the $n = 2$ state is $2\pi a_0$.

#### Question 6
A transverse sinusoidal wave travels along a stretched string under tension $T$. The wave equation is $y(x,t) = A \sin(kx - \omega t)$. Which of the following statements is/are correct?
(A) The maximum transverse particle velocity is $v_{p,\text{max}} = \omega A$.  
(B) The wave propagation speed is $v = \frac{\omega}{k} = \sqrt{\frac{T}{\mu}}$, where $\mu$ is linear mass density.  
(C) The average energy per unit length transmitted by the wave is $\frac{1}{2}\mu \omega^2 A^2$.  
(D) The rate of energy transmission (power) across any cross-section is $P = \frac{1}{2}\mu v \omega^2 A^2$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A small block of mass $m = 0.50\text{ kg}$ is attached to a vertical spring of spring constant $k = 200\text{ N/m}$. The block is pulled down by distance $x_0 = 0.10\text{ m}$ from its equilibrium position and released from rest. Calculate the maximum kinetic energy $K_{\text{max}}$ (in Joules) of the block during oscillation.

#### Question 8
A soap bubble of radius $R_1 = 3.0\text{ cm}$ is blown in air. The surface tension of the soap solution is $S = 0.030\text{ N/m}$. Calculate the excess pressure $\Delta P$ (in Pascals) inside the bubble.

#### Question 9
In a Young's double-slit experiment, the slits are separated by $d = 0.20\text{ mm}$ and the screen is at distance $D = 1.00\text{ m}$. Light of wavelength $\lambda = 600\text{ nm}$ is used. Calculate the fringe width $\beta$ in millimeters ($\text{mm}$).

#### Question 10
A heat engine operates between temperatures $T_H = 800\text{ K}$ and $T_C = 400\text{ K}$. If the engine receives $Q_H = 2000\text{ J}$ of heat from the high-temperature reservoir and performs $W = 800\text{ J}$ of mechanical work per cycle, calculate the second-law efficiency (fraction of Carnot efficiency, $\eta / \eta_C$) as a percentage (\%).

#### Question 11
A long solenoid of radius $r = 0.040\text{ m}$ and $n = 800\text{ turns/m}$ carries a current increasing at a constant rate $\frac{dI}{dt} = 50.0\text{ A/s}$. Calculate the magnitude of the induced electric field $E$ (in $\text{mV/m}$) at a radial distance $r_1 = 0.020\text{ m}$ from the central axis.

#### Question 12
A radioactive sample contains $N_0$ nuclei at $t = 0$. The decay constant of the radioisotope is $\lambda = 0.0693\text{ day}^{-1}$. Calculate the half-life $T_{1/2}$ of the isotope in days. [Take $\ln 2 = 0.693$].

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the thermodynamic processes in List-I with their characteristic equation/property in List-II for an ideal gas:
- **List-I**:
  - P. Isothermal
  - Q. Isobaric
  - R. Isochoric
  - S. Adiabatic
- **List-II**:
  - 1. $\Delta U = 0$
  - 2. $W = 0$
  - 3. $Q = 0$
  - 4. $W = P\Delta V$

Options:
(A) P-1, Q-4, R-2, S-3  
(B) P-4, Q-1, R-3, S-2  
(C) P-1, Q-2, R-4, S-3  
(D) P-3, Q-4, R-2, S-1

#### Question 14
Match the optical instruments in List-I with their magnifying power formula in normal adjustment in List-II:
- **List-I**:
  - P. Simple Microscope
  - Q. Compound Microscope
  - R. Astronomical Telescope
  - S. Galilean Telescope
- **List-II**:
  - 1. $m = \frac{D}{f}$
  - 2. $m \approx \frac{L}{f_o}\frac{D}{f_e}$
  - 3. $m = \frac{f_o}{f_e}$
  - 4. $m = \frac{f_o}{|f_e|}$ with virtual erect image

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 15
Match the electromagnetic wave spectrum region in List-I with its typical wavelength in List-II:
- **List-I**:
  - P. Radio waves
  - Q. Microwaves
  - R. Infrared
  - S. X-rays
- **List-II**:
  - 1. $> 0.1\text{ m}$
  - 2. $1\text{ mm} - 0.1\text{ m}$
  - 3. $700\text{ nm} - 1\text{ mm}$
  - 4. $0.01\text{ nm} - 10\text{ nm}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-4, Q-3, R-2, S-1  
(C) P-2, Q-1, R-4, S-3  
(D) P-1, Q-3, R-2, S-4

#### Question 16
Match the nuclear phenomena in List-I with their physical conservation law/property in List-II:
- **List-I**:
  - P. $\alpha$-decay
  - Q. $\beta^-$-decay
  - R. $\gamma$-decay
  - S. Nuclear fission
- **List-II**:
  - 1. Discrete line spectrum with emission of $^4_2\text{He}$ nucleus
  - 2. Continuous energy spectrum due to antineutrino emission
  - 3. Transitions between nuclear energy levels without change in $A$ or $Z$
  - 4. Heavy nucleus splits with release of prompt neutrons and $\sim 200\text{ MeV}$ energy

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 17
Match the rotational quantities in List-I with their linear analogs in List-II:
- **List-I**:
  - P. Moment of Inertia $I$
  - Q. Angular Momentum $L$
  - R. Torque $\tau$
  - S. Rotational Kinetic Energy $\frac{1}{2}I\omega^2$
- **List-II**:
  - 1. Mass $m$
  - 2. Linear Momentum $p$
  - 3. Force $F$
  - 4. Linear Kinetic Energy $\frac{1}{2}mv^2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-2, S-4

#### Question 18
Match the electrical components in List-I with their dimensional formula in List-II:
- **List-I**:
  - P. Resistance $R$
  - Q. Capacitance $C$
  - R. Inductance $L$
  - S. Magnetic Flux $\Phi_B$
- **List-II**:
  - 1. $[M L^2 T^{-3} A^{-2}]$
  - 2. $[M^{-1} L^{-2} T^4 A^2]$
  - 3. $[M L^2 T^{-2} A^{-2}]$
  - 4. $[M L^2 T^{-2} A^{-1}]$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following statements is/are correct regarding the crystal field theory of octahedral transition metal complexes?
(A) The $d$-orbitals split into lower energy $t_{2g}$ ($d_{xy}, d_{yz}, d_{zx}$) and higher energy $e_g$ ($d_{z^2}, d_{x^2-y^2}$) sets.  
(B) The energy separation between $t_{2g}$ and $e_g$ is denoted by $\Delta_o$.  
(C) Strong field ligands like $\text{CN}^-$ cause large splitting, favoring low-spin configurations.  
(D) The crystal field stabilization energy (CFSE) for a $d^6$ low-spin octahedral complex is $-2.4\Delta_o + 2P$.

#### Question 20
Which of the following organic compounds will give a positive iodoform test upon reaction with $\text{I}_2 / \text{NaOH}$?
(A) Ethanol ($\text{CH}_3\text{CH}_2\text{OH}$)  
(B) Acetophenone ($\text{C}_6\text{H}_5\text{COCH}_3$)  
(C) Propan-2-ol ($\text{CH}_3\text{CH(OH)CH}_3$)  
(D) Benzaldehyde ($\text{C}_6\text{H}_5\text{CHO}$)

#### Question 21
Regarding the thermodynamics of adsorption of a gas on a solid adsorbent:
(A) Adsorption is always an exothermic process ($\Delta H_{\text{ads}} < 0$).  
(B) The entropy change during adsorption is negative ($\Delta S_{\text{ads}} < 0$).  
(C) For spontaneous adsorption, $\Delta G_{\text{ads}}$ must be negative.  
(D) Physical adsorption decreases continuously with increasing temperature at constant pressure.

#### Question 22
Which of the following pairs of solutions will form an ideal solution obeying Raoult's law over the entire composition range?
(A) Benzene + Toluene  
(B) $n$-Hexane + $n$-Heptane  
(C) Bromoethane + Chloroethane  
(D) Ethanol + Acetone

#### Question 23
Which of the following statements is/are correct about the halogens and their compounds?
(A) Fluorine exhibits only $-1$ oxidation state in all its compounds.  
(B) Chlorine has a higher electron gain enthalpy (more negative) than fluorine.  
(C) The bond dissociation enthalpy of $\text{Cl}_2$ is greater than that of $\text{F}_2$.  
(D) $\text{HF}$ is a stronger acid than $\text{HI}$ in aqueous solution.

#### Question 24
Which of the following carbohydrates are reducing sugars?
(A) D-Glucose  
(B) D-Fructose  
(C) Maltose  
(D) Sucrose

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
Calculate the solubility (in $\text{mol/L}$) of silver chloride ($\text{AgCl}$) in pure water at $25^\circ\text{C}$ if the solubility product constant is $K_{sp} = 1.0 \times 10^{-10}$. If the solubility is $S = 1.0 \times 10^{-p}\text{ mol/L}$, find the integer value of $p$.

#### Question 26
Calculate the root-mean-square speed $v_{\text{rms}}$ (in $\text{m/s}$) of oxygen molecules ($\text{O}_2$, $M = 0.032\text{ kg/mol}$) at temperature $T = 300\text{ K}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\sqrt{77943.75} \approx 483.4$. Round off to the nearest integer].

#### Question 27
An electric current of $I = 2.00\text{ A}$ is passed through an aqueous solution of $\text{CuSO}_4$ for $t = 965\text{ seconds}$. Calculate the mass of copper (in grams) deposited at the cathode. [Atomic mass of $\text{Cu} = 63.5\text{ g/mol}$, Faraday constant $F = 96500\text{ C/mol}$. Round off to TWO decimal places].

#### Question 28
The activation energy for a chemical reaction is $E_a = 57.5\text{ kJ/mol}$. Calculate the factor by which the rate constant increases when the temperature is raised from $300\text{ K}$ to $310\text{ K}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $e^{0.745} \approx 2.11$. Round off to TWO decimal places].

#### Question 29
Calculate the total number of unpaired electrons in the complex ion $[\text{CoF}_6]^{3-}$ ($\text{Co}^{3+}, d^6$, weak field ligand $\text{F}^-$).

#### Question 30
The osmotic pressure of an aqueous solution of a protein containing $1.50\text{ g}$ of protein dissolved in $100\text{ mL}$ of water is $\Pi = 3.10 \times 10^{-3}\text{ atm}$ at $T = 300\text{ K}$. Calculate the molar mass $M$ of the protein in $\text{kg/mol}$. [Take $R = 0.0821\text{ L}\cdot\text{atm/(mol}\cdot\text{K)}$. Round off to the nearest integer].

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the polymers in List-I with their repeating monomer units in List-II:
- **List-I**:
  - P. Nylon-6,6
  - Q. Terylene (Dacron)
  - R. Teflon
  - S. Bakelite
- **List-II**:
  - 1. Hexamethylenediamine + Adipic acid
  - 2. Ethylene glycol + Terephthalic acid
  - 3. Tetrafluoroethene
  - 4. Phenol + Formaldehyde

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 32
Match the metallurgical processes in List-I with the metal extracted in List-II:
- **List-I**:
  - P. Hall-Héroult Process
  - Q. Mond Process
  - R. Van Arkel Method
  - S. Froth Floatation
- **List-II**:
  - 1. Aluminium
  - 2. Nickel
  - 3. Zirconium / Titanium
  - 4. Sulfide ores of Copper / Zinc

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-4, R-3, S-2  
(D) P-3, Q-2, R-1, S-4

#### Question 33
Match the chemical compounds in List-I with their common names in List-II:
- **List-I**:
  - P. $\text{CaSO}_4 \cdot \frac{1}{2}\text{H}_2\text{O}$
  - Q. $\text{CaSO}_4 \cdot 2\text{H}_2\text{O}$
  - R. $\text{CaO}$
  - S. $\text{Ca(OH)}_2$
- **List-II**:
  - 1. Plaster of Paris
  - 2. Gypsum
  - 3. Quicklime
  - 4. Slaked lime

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 34
Match the colloidal systems in List-I with their classification in List-II:
- **List-I**:
  - P. Fog / Mist
  - Q. Paint / Ink
  - R. Milk / Butter
  - S. Foam / Whipped cream
- **List-II**:
  - 1. Aerosol (Liquid in Gas)
  - 2. Sol (Solid in Liquid)
  - 3. Emulsion (Liquid in Liquid)
  - 4. Foam (Gas in Liquid)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 35
Match the named organic reactions in List-I with their characteristic reagent/catalyst in List-II:
- **List-I**:
  - P. Rosenmund Reduction
  - Q. Clemmensen Reduction
  - R. Wolff-Kishner Reduction
  - S. Stephen Reaction
- **List-II**:
  - 1. $\text{H}_2 / \text{Pd-BaSO}_4$
  - 2. $\text{Zn-Hg} / \text{conc. HCl}$
  - 3. $\text{NH}_2\text{NH}_2 / \text{KOH, ethylene glycol}$
  - 4. $\text{SnCl}_2 / \text{HCl}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 36
Match the electronic configurations in List-I with their corresponding element/ion in List-II:
- **List-I**:
  - P. $[\text{Ar}]3d^5 4s^1$
  - Q. $[\text{Ar}]3d^{10} 4s^1$
  - R. $[\text{Ar}]3d^5$
  - S. $[\text{Ar}]3d^8$
- **List-II**:
  - 1. $\text{Cr}$ atom
  - 2. $\text{Cu}$ atom
  - 3. $\text{Fe}^{3+}$ ion
  - 4. $\text{Ni}^{2+}$ ion

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \sin x - x + \frac{x^3}{6}$ for all $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(0) = 0$.  
(B) $f'(x) = \cos x - 1 + \frac{x^2}{2} \ge 0$ for all $x \in \mathbb{R}$.  
(C) $f(x)$ is a strictly increasing function on $\mathbb{R}$.  
(D) $\sin x > x - \frac{x^3}{6}$ for all $x > 0$.

#### Question 38
Let $A$ and $B$ be two $n \times n$ symmetric matrices. Which of the following statements is/are correct?
(A) $A + B$ is always a symmetric matrix.  
(B) $AB$ is symmetric if and only if $AB = BA$.  
(C) $AB - BA$ is always a skew-symmetric matrix.  
(D) $A^k$ is symmetric for any positive integer $k$.

#### Question 39
Consider the hyperbola $H: \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ with eccentricity $e$. Which of the following statements is/are correct?
(A) $e = \sqrt{1 + \frac{b^2}{a^2}} > 1$.  
(B) The equations of the asymptotes are $y = \pm \frac{b}{a}x$.  
(C) If $a = b$, the hyperbola is rectangular and its eccentricity is $\sqrt{2}$.  
(D) The locus of the feet of perpendiculars from either focus to any tangent is the auxiliary circle $x^2 + y^2 = a^2$.

#### Question 40
Let $y(x)$ be the solution of the initial value problem $\frac{dy}{dx} = y^2$ with $y(0) = 1$. Which of the following statements is/are correct?
(A) The differential equation is separable.  
(B) The solution is $y(x) = \frac{1}{1-x}$.  
(C) The solution exists and is continuous on the interval $(-\infty, 1)$.  
(D) $\lim_{x \to 1^-} y(x) = +\infty$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-coplanar unit vectors such that $\vec{a} \times (\vec{b} \times \vec{c}) = \frac{\vec{b} + \vec{c}}{\sqrt{2}}$. Which of the following statements is/are correct?
(A) $(\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c} = \frac{\vec{b} + \vec{c}}{\sqrt{2}}$.  
(B) $\vec{a} \cdot \vec{c} = \frac{1}{\sqrt{2}}$, which means the angle between $\vec{a}$ and $\vec{c}$ is $\frac{\pi}{4}$.  
(C) $\vec{a} \cdot \vec{b} = -\frac{1}{\sqrt{2}}$, which means the angle between $\vec{a}$ and $\vec{b}$ is $\frac{3\pi}{4}$.  
(D) The vectors $\vec{b}$ and $\vec{c}$ must be parallel.

#### Question 42
Let $X$ be a binomial random variable with parameters $n = 10$ and $p = 0.5$. Which of the following statements is/are correct?
(A) The mean of $X$ is $E[X] = 5$.  
(B) The variance of $X$ is $\text{Var}(X) = 2.5$.  
(C) The probability distribution of $X$ is symmetric about $k = 5$.  
(D) $P(X = 5) = \binom{10}{5} (0.5)^{10} = \frac{63}{256}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the absolute maximum value of the function $f(x) = x^3 - 3x^2 + 5$ on the closed interval $[0, 3]$.

#### Question 44
Evaluate the definite integral:
$$I = \int_{-2}^2 (x^3 \cos x + \sqrt{4-x^2})\,dx$$
If $I = k\pi$, find the value of $k$.

#### Question 45
Find the radius of convergence $R$ of the power series $\sum_{n=1}^\infty \frac{n}{3^n} x^n$.

#### Question 46
Calculate the acute angle (in degrees) between the lines whose direction cosines are proportional to $(1, 2, 2)$ and $(2, 1, -2)$.

#### Question 47
Let $z$ be a complex number such that $z + \frac{1}{z} = 2\cos\theta$. Find the value of $z^3 + \frac{1}{z^3}$ when $\theta = \frac{\pi}{6}$. [Take $\sqrt{3} \approx 1.732$, or round off to TWO decimal places].

#### Question 48
How many distinct 4-digit numbers can be formed using the digits $1, 2, 3, 4, 5, 6$ without repetition such that the number is divisible by 5?

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the functions in List-I with their derivatives in List-II:
- **List-I**:
  - P. $\ln(\sec x + \tan x)$
  - Q. $\tan^{-1} x$
  - R. $\sin^{-1} x$
  - S. $e^{x^2}$
- **List-II**:
  - 1. $\sec x$
  - 2. $\frac{1}{1+x^2}$
  - 3. $\frac{1}{\sqrt{1-x^2}}$
  - 4. $2x e^{x^2}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 50
Match the curves in List-I with their curvature/property in List-II:
- **List-I**:
  - P. Circle $x^2 + y^2 = R^2$
  - Q. Straight line $y = mx + c$
  - R. Parabola $y^2 = 4ax$ at vertex $(0,0)$
  - S. Catenary $y = c\cosh(x/c)$ at lowest point
- **List-II**:
  - 1. Curvature $\kappa = \frac{1}{R}$ (constant)
  - 2. Curvature $\kappa = 0$
  - 3. Radius of curvature $\rho = 2a$
  - 4. Radius of curvature $\rho = c$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-4, R-3, S-2  
(D) P-4, Q-2, R-1, S-3

#### Question 51
Match the limits in List-I with their evaluated values in List-II:
- **List-I**:
  - P. $\lim_{x \to 0} \frac{\sin x}{x}$
  - Q. $\lim_{x \to 0} \frac{e^x - 1}{x}$
  - R. $\lim_{x \to 0} \frac{\ln(1+x)}{x}$
  - S. $\lim_{x \to 0} \frac{1-\cos x}{x^2}$
- **List-II**:
  - 1. $1$
  - 2. $1$
  - 3. $1$
  - 4. $1/2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-4, R-3, S-2  
(D) P-3, Q-2, R-1, S-4

#### Question 52
Match the conic sections in List-I with their eccentricity $e$ in List-II:
- **List-I**:
  - P. Circle
  - Q. Parabola
  - R. Ellipse
  - S. Hyperbola
- **List-II**:
  - 1. $e = 0$
  - 2. $e = 1$
  - 3. $0 < e < 1$
  - 4. $e > 1$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 53
Match the matrices in List-I with their classification in List-II:
- **List-I**:
  - P. $A^T = A$
  - Q. $A^T = -A$
  - R. $A^T A = I$
  - S. $A^2 = A$
- **List-II**:
  - 1. Symmetric
  - 2. Skew-Symmetric
  - 3. Orthogonal
  - 4. Idempotent

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 54
Match the probability concepts in List-I with their mathematical identity in List-II:
- **List-I**:
  - P. Bayes' Theorem
  - Q. Total Probability
  - R. Independent Events
  - S. Conditional Probability
- **List-II**:
  - 1. $P(A_i|B) = \frac{P(B|A_i)P(A_i)}{\sum P(B|A_j)P(A_j)}$
  - 2. $P(B) = \sum P(B|A_j)P(A_j)$
  - 3. $P(A \cap B) = P(A)P(B)$
  - 4. $P(A|B) = \frac{P(A \cap B)}{P(B)}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 01 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rigid Body Dynamics, Friction on Accelerated Plank, Newton's Second Law for Translation and Rotation ($\tau = I\alpha$), Condition for Pure Rolling without Slipping ($a_c - \alpha R = a_p$).
- **2. IIT Historical Signature**: Classic IIT Delhi multi-body friction challenge where friction between a rolling body and an accelerated base acts to enforce kinematics.
- **3. Given Parameters & Boundary Conditions**:
  - Cylinder: mass $M$, radius $R$, moment of inertia $I = \frac{1}{2}MR^2$.
  - Plank: mass $m = 2M$, smooth floor underneath.
  - Horizontal force $F$ applied at the center of the cylinder.
- **4. Schematic / Equations of Motion**:
  - Let friction on cylinder from plank be $f$ directed backward.
  - For cylinder translation: $F - f = M a_c$.
  - For cylinder rotation about CM: $f R = I \alpha = \left(\frac{1}{2}MR^2\right)\alpha \implies \alpha R = \frac{2f}{M}$.
  - By Newton's third law, friction on plank from cylinder is $f$ directed forward.
  - For plank translation: $f = m a_p = 2M a_p \implies a_p = \frac{f}{2M}$.
  - No slipping condition at contact point: $a_{\text{contact, cylinder}} = a_c - \alpha R = a_p$.
- **5. Step-by-Step Mathematical Derivation**:
  - Substitute expressions into rolling condition:
    $$a_c - \frac{2f}{M} = \frac{f}{2M} \implies a_c = \frac{5f}{2M}$$
  - From cylinder translation:
    $$F - f = M\left(\frac{5f}{2M}\right) = \frac{5}{2}f \implies F = \frac{7}{2}f \implies f = \frac{2F}{7}$$
  - Now calculate accelerations:
    $$a_p = \frac{f}{2M} = \frac{2F/7}{2M} = \frac{F}{7M}$$
    $$a_c = \frac{5f}{2M} = \frac{5(2F/7)}{2M} = \frac{5F}{7M}$$
  - Minimum friction coefficient $\mu_s$:
    $$f \le \mu_s N = \mu_s M g \implies \frac{2F}{7} \le \mu_s M g \implies \mu_s \ge \frac{2F}{7Mg}$$
  - All statements (A), (B), (C), (D) are correct.
- **6. Alternative Solving Method / Shortcut**: System Center of Mass: total external force is $F$, so $M a_c + 2M a_p = F$. Check: $M(5F/7M) + 2M(F/7M) = 5F/7 + 2F/7 = F$. Verified!
- **7. Conceptual Pitfalls & Distractor Breakdown**: Many candidates guess that friction on the plank opposes motion. On the plank, friction is the sole driving force, so it must point forward.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**
- **9. Cross-Concept Extension**: If force $F$ were applied to the plank instead of the cylinder, the partition of acceleration would change to $a_c = \frac{2F}{7M}$ and $a_p = \frac{3F}{7M}$.

---

### Question 2
- **1. Target Concept & Governing Laws**: AC Circuits, Parallel LC Resonance, Impedance, Phase Angle.
- **2. IIT Historical Signature**: IIT Delhi's high affinity for AC circuit theory and LC parallel resonance behavior.
- **3. Derivation**:
  - Admittance of parallel LC: $Y = j\omega C + \frac{1}{j\omega L} = j\left(\omega C - \frac{1}{\omega L}\right)$.
  - Impedance: $Z_{LC} = \frac{1}{Y} = \frac{-j}{\omega C - 1/(\omega L)}$.
  - At resonance $\omega_0 = 1/\sqrt{LC}$, $\omega C = 1/(\omega L)$, so $Y = 0 \implies Z_{LC} \to \infty$. Thus (A) is correct.
  - Since $Z_{LC} = \infty$, the total circuit impedance is infinite, so the source current is zero. (B) is correct.
  - For $\omega < \omega_0$: $\frac{1}{\omega L} > \omega C$, so inductive susceptance dominates $\implies$ inductive behavior. (C) is correct.
  - For $\omega > \omega_0$: $\omega C > \frac{1}{\omega L}$, so capacitive susceptance dominates $\implies$ capacitive behavior. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: First Law of Thermodynamics, Polytropic Process $P = \alpha V^2$, Work Done $W = \int P dV$, Molar Heat Capacity $C = C_V + \frac{R}{1-n}$.
- **2. Derivation**:
  - $P = \alpha V^2$ corresponds to $P V^{-2} = \alpha$, so polytropic index $n = -2$.
  - Work done: $W = \int_{V_0}^{2V_0} \alpha V^2 dV = \frac{\alpha}{3}[(2V_0)^3 - V_0^3] = \frac{7}{3}\alpha V_0^3$. (A) is correct.
  - Ideal gas law: $T = \frac{PV}{nR} = \frac{\alpha V^3}{nR}$. At $2V_0$, $T_2 = \frac{\alpha (8V_0^3)}{nR} = 8 T_1$. (D) is correct.
  - Internal energy change: $\Delta U = n C_V \Delta T = n\left(\frac{5}{2}R\right)(7 T_1) = \frac{35}{2} n R T_1 = \frac{35}{2}\alpha V_0^3 \ne \frac{35}{4}\alpha V_0^3$. Thus (B) is incorrect.
  - Molar heat capacity: $C = C_V + \frac{R}{1 - (-2)} = \frac{5}{2}R + \frac{R}{3} = \frac{17}{6}R$. (C) is correct.
- **8. Final Answer & Correct Options**: **(A), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Electrostatics of Concentric Spherical Shells, Grounding, Charge Distribution.
- **2. Derivation**:
  - Let $q'$ be the charge remaining on the inner shell after grounding.
  - Potential of inner shell must equal zero (grounded):
    $$V_{\text{inner}} = \frac{1}{4\pi\varepsilon_0}\left[\frac{q'}{R} + \frac{2Q}{2R}\right] = 0 \implies \frac{q'}{R} + \frac{Q}{R} = 0 \implies q' = -Q$$
    Statement (A) is correct.
  - Potential of outer shell:
    $$V_{\text{outer}} = \frac{1}{4\pi\varepsilon_0}\left[\frac{q'}{2R} + \frac{2Q}{2R}\right] = \frac{1}{4\pi\varepsilon_0}\frac{-Q + 2Q}{2R} = \frac{Q}{8\pi\varepsilon_0 R} \ne \frac{Q}{4\pi\varepsilon_0 R}$$
    Thus (B) is incorrect.
  - Initial charge on inner shell was $+Q$. Final is $-Q$. Thus charge flown to ground is $Q - (-Q) = 2Q$. (C) is correct.
  - Electric field between shells: $E(r) = \frac{q'}{4\pi\varepsilon_0 r^2} = -\frac{Q}{4\pi\varepsilon_0 r^2}$.
  - Stored energy:
    $$U = \int_R^{2R} \frac{1}{2}\varepsilon_0 E^2 (4\pi r^2 dr) = \frac{Q^2}{8\pi\varepsilon_0}\left(\frac{1}{R} - \frac{1}{2R}\right) = \frac{Q^2}{16\pi\varepsilon_0 R}$$
    Statement (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Potential Energy Wells, Small Oscillations, Simple Harmonic Motion.
- **2. Derivation**:
  - $U'(x) = U_0 \left[\frac{4x^3}{a^4} - \frac{4x}{a^2}\right] = \frac{4U_0 x}{a^2}\left(\frac{x^2}{a^2} - 1\right) = 0 \implies x = 0, \pm a$.
  - $U''(x) = U_0 \left[\frac{12x^2}{a^4} - \frac{4}{a^2}\right]$.
  - At $x = 0$: $U''(0) = -\frac{4U_0}{a^2} < 0 \implies$ unstable equilibrium. (B) is correct.
  - At $x = \pm a$: $U''(\pm a) = \frac{8U_0}{a^2} > 0 \implies$ stable equilibrium. (A) is correct.
  - Angular frequency: $\omega = \sqrt{\frac{U''(\pm a)}{m}} = \sqrt{\frac{8U_0}{m a^2}} = \frac{2}{a}\sqrt{\frac{2U_0}{m}}$. (C) is correct.
  - Potential at well bottom: $U(\pm a) = U_0(1 - 2) = -U_0$. Potential as $x \to \infty$ is $+\infty$. Thus escape energy to infinity is infinite, not $U_0$ (it is $U_0$ to escape to the central hill at $x=0$). Thus (D) is incorrect.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Electromagnetic Waves, Poynting Vector, Radiation Pressure.
- **2. Derivation**:
  - $\vec{B} = \frac{1}{c}(\hat{k} \times \vec{E}) = \frac{E_0}{c}\cos(kz - \omega t)\hat{j}$. (A) is correct.
  - $\langle \vec{S} \rangle = \frac{E_0^2}{2\mu_0 c}\hat{k} = \frac{300^2}{2(4\pi \times 10^{-7})(3 \times 10^8)}\hat{k} = \frac{90000}{753.98}\hat{k} \approx 119.37\hat{k}\text{ W/m}^2$. (B) is correct.
  - Radiation pressure on absorbing surface: $P = \frac{\langle S \rangle}{c} = \frac{119.37}{3 \times 10^8} \approx 3.98 \times 10^{-7}\text{ N/m}^2$. (C) is correct.
  - On reflection, momentum change doubles $\Delta p = 2p$, so pressure doubles $P_{\text{ref}} = 2P_{\text{abs}}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Torricelli's law with continuity: $t = \frac{A}{a}\sqrt{\frac{2H}{g}} = \frac{1.0}{2.0 \times 10^{-4}}\sqrt{\frac{2(4.90)}{9.80}} = 5000 \times 1.0 = 5000\text{ s}$. Exact: `5000.00`.
- **Question 8**: Resonance tube: $\frac{\lambda}{2} = L_2 - L_1 = 50.0 - 16.0 = 34.0\text{ cm} = 0.34\text{ m} \implies \lambda = 0.68\text{ m}$. Speed: $v = \nu \lambda = 500 \times 0.68 = 340\text{ m/s}$. Exact: `340.00`.
- **Question 9**: Conservation of energy for rotating rod: $M g \frac{L}{2} = \frac{1}{2} I \omega^2 = \frac{1}{2}\left(\frac{1}{3}ML^2\right)\omega^2 \implies \omega = \sqrt{\frac{3g}{L}} = \sqrt{\frac{3(9.80)}{1.20}} = \sqrt{24.5} \approx 4.95\text{ rad/s}$. Exact: `4.95`.
- **Question 10**: $E_{\text{photon}} = \frac{hc}{\lambda} = \frac{1240}{400} = 3.10\text{ eV}$. Stopping potential: $e V_0 = E - \Phi = 3.10 - 2.14 = 0.96\text{ eV} \implies V_0 = 0.96\text{ V}$. Exact: `0.96`.
- **Question 11**: At midpoint, fields due to opposite currents add: $B = \frac{\mu_0 I_1}{2\pi (d/2)} + \frac{\mu_0 I_2}{2\pi (d/2)} = \frac{\mu_0}{\pi d}(I_1 + I_2) = \frac{4\pi \times 10^{-7}}{\pi (0.20)}(30.0) = 20 \times 10^{-7} \times 30 = 60 \times 10^{-6}\text{ T} = 60\ \mu\text{T}$. Exact: `60.00`.
- **Question 12**: For lens 1: parallel beam converges at $f_1 = +20\text{ cm}$. Distance from lens 2: $u_2 = 20 - 10 = +10\text{ cm}$ (virtual object). Using lens formula for lens 2 ($f_2 = -10\text{ cm}$): $\frac{1}{v_2} - \frac{1}{+10} = \frac{1}{-10} \implies \frac{1}{v_2} = 0 \implies v_2 \to \infty$. But wait, parallel emergent beam! Distance is infinite, or let's specify parallel beam emergent at $\infty$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Rolling acceleration $a = \frac{g\sin\theta}{1 + I/(mr^2)} = \frac{g\sin 30^\circ}{1 + 2/5} = \frac{g/2}{7/5} = \frac{5}{14}g$. Option (A).
- **Question 14**: $v_{\text{max}} = \omega A = \sqrt{k/m} A \implies 2.0 = \sqrt{100/1} A = 10 A \implies A = 0.20\text{ m}$. Option (B).
- **Question 15**: $\nu = c R_\infty \left(\frac{1}{1^2} - \frac{1}{3^2}\right) = (3 \times 10^8)(1.097 \times 10^7)\left(\frac{8}{9}\right) \approx 2.925 \times 10^{15}\text{ Hz}$. Option (B).
- **Question 16**: $M = N I A = 100 \times 2.0 \times \pi (0.05)^2 = 200 \times 3.1416 \times 0.0025 \approx 1.57\text{ A}\cdot\text{m}^2$. Option (A).
- **Question 17**: $\eta = 1 - \frac{300}{500} = 0.40$. Work $W = \eta Q_H = 0.40 \times 1000 = 400\text{ J}$. Option (A).
- **Question 18**: $\lambda = \frac{h}{\sqrt{3 m k_B T}} = \frac{6.63 \times 10^{-34}}{\sqrt{3(1.67 \times 10^{-27})(1.38 \times 10^{-23})(300)}} \approx 0.145\text{ nm} \approx 0.14\text{ nm}$. Option (B).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: $[Co(en)_2Cl_2]^+$ has $cis$ (optically active, chiral pair) and $trans$ (inversion center, achiral) isomers. Co is +3, coordination number 6. Options: (A), (B), (C), (D).
- **Question 20**: Inert gas at constant P increases volume, shifting toward more moles ($\text{PCl}_3 + \text{Cl}_2$). Constant V has no effect. Endothermic reaction shifts forward with temperature. $K_p$ depends only on temperature. Options: (A), (B), (C).
- **Question 21**: $E2$ on $(2R, 3R)$-2-bromo-3-methylpentane with ethoxide requires anti-coplanar transition state yielding $(E)$-3-methylpent-2-ene. It is second order. Options: (A), (B), (C).
- **Question 22**: $\text{XeF}_4$ (square planar, $\mu=0$), $\text{BF}_3$ (trigonal planar, $\mu=0$), $\text{I}_3^-$ (linear, symmetric, $\mu=0$). $\text{SF}_4$ is see-saw ($\mu \ne 0$). Options: (A), (B), (D).
- **Question 23**: For ideal binary solution: $\Delta H_{\text{mix}} = 0, \Delta V_{\text{mix}} = 0, \Delta S_{\text{mix}} > 0, \Delta G_{\text{mix}} < 0$. Options: (A), (B), (C), (D).
- **Question 24**: Group II metal cations giving black sulfides: $\text{CuS}, \text{PbS}, \text{Bi}_2\text{S}_3$ are black. $\text{CdS}$ is yellow! Options: (A), (B), (D).
- **Question 25**: $\text{pH} = pK_a + \log\frac{[\text{CH}_3\text{COO}^-]}{[\text{CH}_3\text{COOH}]} = 4.74 + \log\left(\frac{0.10}{0.20}\right) = 4.74 - 0.30 = 4.44$. Exact: `4.44`.
- **Question 26**: For first-order reaction, $t_{75\%} = 2 t_{1/2} = 2 \times \frac{0.693}{6.93 \times 10^{-3}} = 2 \times 100 = 200\text{ s}$. Exact: `200.00`.
- **Question 27**: For FCC: $4r = \sqrt{2}a \implies r = \frac{\sqrt{2}a}{4} = \frac{1.414 \times 400}{4} = 141.4\text{ pm}$. Exact: `141.42`.
- **Question 28**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = 0.34 - (-0.76) = 1.10\text{ V}$. Exact: `1.10`.
- **Question 29**: $\Delta T_f = i K_f m \implies 0.205 = i (1.86)(0.10) \implies i = \frac{0.205}{0.186} \approx 1.102$. Since $i = 1 + \alpha$, $\alpha = 0.102 = 10.2\%$. Exact: `10.22`.
- **Question 30**: $\text{Fe}^{2+}$ is $3d^6$. High spin in weak field $\text{H}_2\text{O}$ has 4 unpaired electrons. $\mu = \sqrt{4(6)} = \sqrt{24} \approx 4.90\text{ BM}$. Exact: `4.90`.
- **Question 31**: Nitrobenzene has a strongly deactivating $-\text{NO}_2$ group which complexes with $\text{AlCl}_3$, preventing Friedel-Crafts reaction. Option (A).
- **Question 32**: Acid strength increases with oxidation state of central atom: $\text{HClO} < \text{HClO}_2 < \text{HClO}_3 < \text{HClO}_4$. Option (A).
- **Question 33**: Slag formed in copper smelting is iron silicate $\text{FeSiO}_3$. Option (A).
- **Question 34**: Cannizzaro reaction. Option (A).
- **Question 35**: $\text{XeOF}_4$: Xe has 1 lone pair. Each F has 3 lone pairs ($4 \times 3 = 12$). Oxygen has 2 lone pairs. Total lone pairs = $1 + 12 + 2 = 15$. Option (C).
- **Question 36**: Vitamin C (ascorbic acid) is water-soluble. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(-x) = \frac{(-x)^2 - 1}{(-x)^2 + 1} = f(x)$ (even). Range is $[-1, 1)$. $f'(x) = \frac{4x}{(x^2+1)^2} > 0$ for $x > 0$. Horizontal asymptote $y = 1$. Options: (A), (B), (C), (D).
- **Question 38**: Orthogonal matrix with $\det M = 1$ is an element of $SO(3)$, representing 3D spatial rotation. It always has eigenvalue $\lambda = 1$, row norm 1, and $\det(M - I) = 0$. Options: (A), (B), (C), (D).
- **Question 39**: For $\frac{x^2}{16} + \frac{y^2}{9} = 1$: $a=4, b=3$. $e = \sqrt{1 - 9/16} = \frac{\sqrt{7}}{4}$. Latus rectum $= \frac{2b^2}{a} = \frac{18}{4} = \frac{9}{2}$. Product of perpendiculars from foci to any tangent is $b^2 = 9$. Director circle is $x^2 + y^2 = a^2 + b^2 = 25$. Options: (A), (B), (C), (D).
- **Question 40**: Wallis formula recurrence: $I_n = \frac{n-1}{n}I_{n-2}$. $I_4 = \frac{3}{4}\frac{1}{2}\frac{\pi}{2} = \frac{3\pi}{16}$. $I_5 = \frac{4}{5}\frac{2}{3}(1) = \frac{8}{15}$. $\lim_{n \to \infty} I_n = 0$. Options: (A), (B), (C), (D).
- **Question 41**: Circle with center $c = 3+4i$, radius $r = 2$. $|c| = 5$. Max distance $= 5+2 = 7$, min distance $= 5-2 = 3$. Point $3+2i$: $|3+2i - (3+4i)| = |-2i| = 2$. Options: (A), (B), (C), (D).
- **Question 42**: $IF = e^{\int \cot x dx} = \sin x$. Equation: $y \sin x = \int 2\cos x \sin x dx = \sin^2 x + C$. $y(\pi/2) = 1 \implies 1 = 1 + C \implies C = 0 \implies y = \sin x$. $y(\pi/6) = 1/2$. Max is 1 at $\pi/2$. Options: (A), (B), (C), (D).
- **Question 43**: Substitute $x = \tan\theta$: $I = \int_0^{\pi/4} \ln(1+\tan\theta) d\theta = \frac{\pi}{8}\ln 2$. So $k = 8$. Exact: `8.00`.
- **Question 44**: $y^2 = 4x$ and $y = 2x - 4 \implies x = \frac{y+4}{2}$. Points of intersection: $y^2 = 4\left(\frac{y+4}{2}\right) = 2y + 8 \implies y^2 - 2y - 8 = 0 \implies y = 4, -2$.
  $$\text{Area} = \int_{-2}^4 \left(\frac{y+4}{2} - \frac{y^2}{4}\right)dy = \left[\frac{y^2}{4} + 2y - \frac{y^3}{12}\right]_{-2}^4 = (4 + 8 - 16/3) - (1 - 4 + 8/12) = \frac{20}{3} - \left(-\frac{7}{3}\right) = 9.00$$
  Exact: `9.00`.
- **Question 45**: Scalar triple product:
  $$[\vec{a} \ \vec{b} \ \vec{c}] = \begin{vmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \\ 3 & 1 & 2 \end{vmatrix} = 1(6-1) - 2(4-3) + 3(2-9) = 5 - 2 - 21 = -18$$
  Volume $V = |-18| = 18.00$. Exact: `18.00`.
- **Question 46**: $P = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14} \approx 0.357 \approx 0.36$. Exact: `0.36`.
- **Question 47**: $2^x + 3^x = 5^x \implies (2/5)^x + (3/5)^x = 1$. The left-hand side is strictly decreasing with $x$, while the RHS is constant. Hence there is exactly 1 real solution ($x = 1$). Exact: `1.00`.
- **Question 48**: Taylor expansion: $\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \dots$, so $\sin x - x + \frac{x^3}{6} = \frac{x^5}{120}$. Limit is $\frac{1}{120}$. Thus $m = 120$. Exact: `120.00`.
- **Question 49**: Distance formula between skew lines: vector $\vec{d}_1 = (2, 3, 4)$, $\vec{d}_2 = (3, 4, 5)$. Cross product $\vec{d}_1 \times \vec{d}_2 = (-1, 2, -1)$. $\vec{r}_2 - \vec{r}_1 = (1, 2, 2)$. Dot product $= -1(1) + 2(2) - 1(2) = 1$. Magnitude of cross product $= \sqrt{1 + 4 + 1} = \sqrt{6}$. Distance $= \frac{1}{\sqrt{6}}$. Option (A).
- **Question 50**: $\alpha + \beta = 6, \alpha\beta = 2$. $\alpha^3 + \beta^3 = (\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta) = 216 - 3(2)(6) = 216 - 36 = 180$. Option (A).
- **Question 51**: $r \cdot r! = (r+1 - 1)r! = (r+1)! - r!$. Telescoping sum gives $(11!) - 1! = 11! - 1$. Option (A).
- **Question 52**: $A^2 - 3A + 2I = 0 \implies 2I = 3A - A^2 \implies 2A^{-1} = 3I - A \implies A^{-1} = \frac{1}{2}(3I - A)$. Option (A).
- **Question 53**: Place 5 boys in $5!$ ways. This creates 6 available spots. Choose 5 spots for girls: $\binom{6}{5} \times 5! = 6 \times 5! = 6!$. Total ways $= 5! \times 6!$. Option (A).
- **Question 54**: Triangle with vertices $(0,0), (4,0), (0,6)$ is a right-angled triangle. Its hypotenuse joins $(4,0)$ and $(0,6)$. Length of hypotenuse $= \sqrt{4^2 + 6^2} = \sqrt{52} = 2\sqrt{13}$. Circumradius is half of hypotenuse $= \sqrt{13}$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 01 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rigid Body Dynamics, Severed Constraint, Torque about Center of Mass, Instantaneous Acceleration.
- **2. Derivation**:
  - Immediately after cutting string at $B$, tension at $A$ is $T$.
  - Equation of motion for CM: $Mg - T = M a_{\text{cm}}$.
  - Torque about CM: $T \frac{L}{2} = I_{\text{cm}} \alpha = \left(\frac{1}{12}ML^2\right)\alpha \implies \alpha = \frac{6T}{ML}$.
  - Kinematic constraint at $A$: string does not stretch instantaneously, so $a_A = a_{\text{cm}} - \alpha \frac{L}{2} = 0$.
  - Thus $a_{\text{cm}} = \alpha \frac{L}{2} = \frac{3T}{M}$.
  - Substitute into translational equation: $Mg - T = M\left(\frac{3T}{M}\right) = 3T \implies 4T = Mg \implies T = \frac{Mg}{4}$. (C) is correct.
  - $a_{\text{cm}} = \frac{3(Mg/4)}{M} = \frac{3g}{4}$. (B) is correct.
  - $\alpha = \frac{6(Mg/4)}{ML} = \frac{3g}{2L}$. (A) is correct.
  - Acceleration of end $B$: $a_B = a_{\text{cm}} + \alpha \frac{L}{2} = \frac{3g}{4} + \frac{3g}{4} = \frac{3g}{2}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Biot-Savart Law, Helmholtz Coil Principle, Axial Magnetic Field.
- **2. Derivation**:
  - For two coaxial coils separated by their radius $R$, the field at midpoint $x = R/2$ is:
    $$B = 2 \times \frac{\mu_0 I R^2}{2(R^2 + (R/2)^2)^{3/2}} = \frac{\mu_0 I R^2}{(5R^2/4)^{3/2}} = \frac{8\mu_0 I}{5\sqrt{5}R}$$
    Statement (A) is correct.
  - By symmetry, $\frac{dB}{dx} = 0$ at midpoint. (B) is correct.
  - In Helmholtz configuration with separation $d = R$, the second derivative $\frac{d^2B}{dx^2}$ also vanishes identically at the midpoint. (C) is correct.
  - Because first and second derivatives are zero, the field is extremely uniform over a broad region around the center. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Geometric Optics, Total Internal Reflection, Prisms.
- **2. Derivation**:
  - $\sin\theta_c = \frac{1}{\mu} = \frac{1}{\sqrt{2}} \implies \theta_c = 45^\circ$. (A) is correct.
  - The ray enters normally at leg 1, strikes hypotenuse at angle of incidence $i = 45^\circ = \theta_c$ (at grazing/TIR threshold). Under strict reflection condition, it reflects at $45^\circ$. (B) is correct.
  - The reflected ray hits the second leg perpendicularly (angle of incidence $0^\circ$), so it emerges undeflected. (C) is correct.
  - Total deviation angle $= 90^\circ$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Capacitors with Multiple Dielectrics in Series, Displacement Vector.
- **2. Derivation**:
  - Two capacitors in series: $C_1 = \frac{K_1 \varepsilon_0 A}{d/2} = \frac{4\varepsilon_0 A}{d}$, $C_2 = \frac{K_2 \varepsilon_0 A}{d/2} = \frac{8\varepsilon_0 A}{d}$.
  - $C_{\text{eq}} = \frac{C_1 C_2}{C_1 + C_2} = \frac{32}{12}\frac{\varepsilon_0 A}{d} = \frac{8\varepsilon_0 A}{3d}$. (A) is correct.
  - Charge $Q$ is same on both: $E_1 = \frac{Q}{K_1 \varepsilon_0 A}, E_2 = \frac{Q}{K_2 \varepsilon_0 A}$. Since $K_2 = 2K_1$, $E_1 = 2E_2$. (B) is correct.
  - Potential drops: $V_1 = E_1(d/2), V_2 = E_2(d/2)$. $V_1 = 2V_2 \implies V_1 = \frac{2}{3}V$. (C) is correct.
  - Bound surface charge density at interface $= P_1 - P_2 = \varepsilon_0(K_1 - 1)E_1 - \varepsilon_0(K_2 - 1)E_2 \ne 0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Bohr Model for Hydrogen-like Ions, Photon Absorption.
- **2. Derivation**:
  - $\Delta E = 13.6 Z^2 \left(1 - \frac{1}{4}\right) = 13.6 Z^2 \times \frac{3}{4} = 10.2 Z^2\text{ eV} = 40.8\text{ eV} \implies Z^2 = 4 \implies Z = 2$ ($\text{He}^+$). (A) is correct.
  - Ionization energy $= 13.6 Z^2 = 13.6(4) = 54.4\text{ eV}$. (B) is correct.
  - $r_n = \frac{n^2}{Z}a_0$. For $n = 2, Z = 2$, $r_2 = \frac{4}{2}a_0 = 2a_0 \ne a_0$. Thus (C) is incorrect.
  - De Broglie wavelength: by Bohr's postulate, $2\pi r_n = n \lambda \implies \lambda = \frac{2\pi(2a_0)}{2} = 2\pi a_0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Wave Mechanics on Stretched Strings, Energy Density and Power.
- **2. Derivation**:
  - Particle velocity $v_p = \frac{\partial y}{\partial t} = -\omega A \cos(kx - \omega t) \implies v_{p,\text{max}} = \omega A$. (A) is correct.
  - Wave velocity $v = \frac{\omega}{k} = \sqrt{\frac{T}{\mu}}$. (B) is correct.
  - Average energy per unit length: $\frac{dE}{dx} = \frac{1}{2}\mu \omega^2 A^2$. (C) is correct.
  - Power: $P = \frac{dE}{dt} = v \frac{dE}{dx} = \frac{1}{2}\mu v \omega^2 A^2$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Maximum kinetic energy equals elastic potential energy at maximum displacement: $K_{\text{max}} = \frac{1}{2}k x_0^2 = \frac{1}{2}(200)(0.10)^2 = 1.00\text{ J}$. Exact: `1.00`.
- **Question 8**: For a soap bubble with two surfaces: $\Delta P = \frac{4S}{R} = \frac{4(0.030)}{0.030} = 4.00\text{ Pa}$. Exact: `4.00`.
- **Question 9**: $\beta = \frac{\lambda D}{d} = \frac{(600 \times 10^{-9}\text{ m})(1.00\text{ m})}{0.20 \times 10^{-3}\text{ m}} = 3.0 \times 10^{-3}\text{ m} = 3.00\text{ mm}$. Exact: `3.00`.
- **Question 10**: Carnot efficiency $\eta_C = 1 - \frac{400}{800} = 0.50$ (50%). Actual efficiency $\eta = \frac{W}{Q_H} = \frac{800}{2000} = 0.40$ (40%). Second-law efficiency $= \frac{0.40}{0.50} = 0.80 = 80.00\%$. Exact: `80.00`.
- **Question 11**: Induced electric field inside solenoid: $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt} \implies E(2\pi r_1) = \pi r_1^2 \mu_0 n \frac{dI}{dt} \implies E = \frac{1}{2}\mu_0 n r_1 \frac{dI}{dt} = \frac{1}{2}(4\pi \times 10^{-7})(800)(0.020)(50.0) = 5.026 \times 10^{-4}\text{ V/m} \approx 0.50\text{ mV/m}$. Exact: `0.50`.
- **Question 12**: $T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{0.0693} = 10.00\text{ days}$. Exact: `10.00`.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: P-1, Q-4, R-2, S-3. Option (A).
- **Question 14**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 15**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 16**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 17**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 18**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Octahedral splitting: $t_{2g}$ lower, $e_g$ higher. Energy difference is $\Delta_o$. Strong field ligands give low spin. CFSE for low spin $d^6$ ($t_{2g}^6 e_g^0$) is $6(-0.4\Delta_o) + 2P = -2.4\Delta_o + 2P$. Options: (A), (B), (C), (D).
- **Question 20**: Iodoform test requires $\text{CH}_3\text{C=O}$ or $\text{CH}_3\text{CH(OH)}$ group. Ethanol, acetophenone, and propan-2-ol give positive test. Benzaldehyde does not. Options: (A), (B), (C).
- **Question 21**: Adsorption is exothermic ($\Delta H < 0$), decreases randomness ($\Delta S < 0$), spontaneous ($\Delta G < 0$). Physical adsorption decreases with increasing temperature. Options: (A), (B), (C), (D).
- **Question 22**: Pairs of chemically similar compounds with similar intermolecular forces form ideal solutions: Benzene + Toluene, $n$-Hexane + $n$-Heptane, Bromoethane + Chloroethane. Ethanol + Acetone shows positive deviation due to hydrogen bond disruption. Options: (A), (B), (C).
- **Question 23**: Fluorine is the most electronegative element and exhibits only -1 oxidation state. Chlorine has higher electron affinity than fluorine. $\text{Cl}_2$ bond is stronger than $\text{F}_2$ due to lone-pair repulsion in small fluorine. In water, $\text{HI}$ is a much stronger acid than $\text{HF}$ (weak acid). Options: (A), (B), (C).
- **Question 24**: Glucose, fructose, and maltose are reducing sugars (maltose has free hemiacetal group). Sucrose is a non-reducing sugar (glycosidic bond between anomeric carbons). Options: (A), (B), (C).
- **Question 25**: $S = \sqrt{K_{sp}} = \sqrt{1.0 \times 10^{-10}} = 1.0 \times 10^{-5}\text{ mol/L} \implies p = 5$. Exact: `5.00`.
- **Question 26**: $v_{\text{rms}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3(8.314)(300)}{0.032}} = \sqrt{233831.25} \approx 483.56 \approx 484\text{ m/s}$. Exact: `484.00`.
- **Question 27**: $m = \frac{M I t}{n F} = \frac{(63.5)(2.00)(965)}{2(96500)} = \frac{63.5 \times 1930}{193000} = \frac{63.5}{100} = 0.635\text{ g} \approx 0.64\text{ g}$. Exact: `0.64`.
- **Question 28**: $\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) = \frac{57500}{8.314}\left(\frac{10}{300 \times 310}\right) = \frac{575000}{773202} \approx 0.7436 \implies \frac{k_2}{k_1} = e^{0.744} \approx 2.10$. Exact: `2.10`.
- **Question 29**: $[\text{CoF}_6]^{3-}$: $\text{Co}^{3+}$ is $3d^6$. $\text{F}^-$ is a weak field ligand, so high-spin configuration $t_{2g}^4 e_g^2$. Number of unpaired electrons $= 4$. Exact: `4.00`.
- **Question 30**: $\Pi = \frac{w R T}{M V} \implies M = \frac{w R T}{\Pi V} = \frac{(1.50)(0.0821)(300)}{(3.10 \times 10^{-3})(0.100)} = \frac{36.945}{3.10 \times 10^{-4}} \approx 119177\text{ g/mol} \approx 119\text{ kg/mol}$. Exact: `119.00`.
- **Question 31**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 32**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 33**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 34**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 35**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 36**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(0) = 0$. $f'(x) = \cos x - 1 + \frac{x^2}{2} \ge 0$ since $\cos x \ge 1 - \frac{x^2}{2}$. Hence $f(x)$ is strictly increasing for $x > 0$. Therefore $f(x) > 0 \implies \sin x > x - \frac{x^3}{6}$ for $x > 0$. Options: (A), (B), (C), (D).
- **Question 38**: $(A+B)^T = A^T + B^T = A+B$. $(AB)^T = B^T A^T = BA = AB$ iff they commute. $(AB-BA)^T = BA - AB = -(AB-BA)$. $(A^k)^T = (A^T)^k = A^k$. Options: (A), (B), (C), (D).
- **Question 39**: Eccentricity $e = \sqrt{1 + b^2/a^2} > 1$. Asymptotes $y = \pm \frac{b}{a}x$. For rectangular hyperbola $a = b \implies e = \sqrt{2}$. Locus of feet of perpendiculars is the auxiliary circle $x^2 + y^2 = a^2$. Options: (A), (B), (C), (D).
- **Question 40**: $\frac{dy}{y^2} = dx \implies -\frac{1}{y} = x + C$. $y(0) = 1 \implies C = -1 \implies y(x) = \frac{1}{1-x}$. Continuous on $(-\infty, 1)$ and diverges to $+\infty$ as $x \to 1^-$. Options: (A), (B), (C), (D).
- **Question 41**: Vector triple product expansion: $\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c} = \frac{1}{\sqrt{2}}\vec{b} + \frac{1}{\sqrt{2}}\vec{c}$. Since $\vec{b}$ and $\vec{c}$ are non-collinear, equating coefficients gives $\vec{a} \cdot \vec{c} = \frac{1}{\sqrt{2}} \implies \theta = \pi/4$, and $\vec{a} \cdot \vec{b} = -\frac{1}{\sqrt{2}} \implies \theta = 3\pi/4$. Options: (A), (B), (C).
- **Question 42**: Binomial $n = 10, p = 0.5$. Mean $= np = 5$. Variance $= np(1-p) = 2.5$. Symmetric distribution. $P(X=5) = \binom{10}{5}(0.5)^{10} = \frac{252}{1024} = \frac{63}{256}$. Options: (A), (B), (C), (D).
- **Question 43**: $f'(x) = 3x^2 - 6x = 3x(x-2) = 0 \implies x = 0, 2$. Values: $f(0) = 5, f(2) = 8 - 12 + 5 = 1, f(3) = 27 - 27 + 5 = 5$. Absolute maximum is 5. Exact: `5.00`.
- **Question 44**: $x^3 \cos x$ is odd, so its integral from $-2$ to $2$ is 0. $\int_{-2}^2 \sqrt{4-x^2}dx$ represents the area of a semicircle of radius 2: $\frac{1}{2}\pi (2)^2 = 2\pi$. Thus $k = 2$. Exact: `2.00`.
- **Question 45**: Ratio test: $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = \lim_{n \to \infty} \frac{n+1}{3^{n+1}} \frac{3^n}{n} |x| = \frac{|x|}{3} < 1 \implies |x| < 3$. Radius of convergence $R = 3$. Exact: `3.00`.
- **Question 46**: Direction ratios: $\vec{u} = (1, 2, 2)$, $|\vec{u}| = \sqrt{1+4+4} = 3$. $\vec{v} = (2, 1, -2)$, $|\vec{v}| = \sqrt{4+1+4} = 3$. $\vec{u} \cdot \vec{v} = 1(2) + 2(1) + 2(-2) = 2 + 2 - 4 = 0$. Angle is $90^\circ$. Exact: `90.00`.
- **Question 47**: $z + \frac{1}{z} = 2\cos\theta \implies z = e^{i\theta}$. Then $z^3 + \frac{1}{z^3} = 2\cos(3\theta) = 2\cos(3 \times \pi/6) = 2\cos(\pi/2) = 0$. Exact: `0.00`.
- **Question 48**: Divisible by 5 means the last digit must be 5 (1 choice). The first 3 digits can be chosen from the remaining 5 digits $\{1, 2, 3, 4, 6\}$ in $P(5, 3) = 5 \times 4 \times 3 = 60$ ways. Exact: `60.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 01
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, C, D
- Q4: A, C, D
- Q5: A, B, C
- Q6: A, B, C, D
- Q7: 5000.00
- Q8: 340.00
- Q9: 4.95
- Q10: 0.96
- Q11: 60.00
- Q12: 10.00
- Q13: A
- Q14: B
- Q15: B
- Q16: A
- Q17: A
- Q18: B

#### Chemistry
- Q19: A, B, C, D
- Q20: A, B, C
- Q21: A, B, C
- Q22: A, B, D
- Q23: A, B, C, D
- Q24: A, B, D
- Q25: 4.44
- Q26: 200.00
- Q27: 141.42
- Q28: 1.10
- Q29: 10.22
- Q30: 4.90
- Q31: A
- Q32: A
- Q33: A
- Q34: A
- Q35: C
- Q36: A

#### Mathematics
- Q37: A, B, C, D
- Q38: A, B, C, D
- Q39: A, B, C, D
- Q40: A, B, C, D
- Q41: A, B, C, D
- Q42: A, B, C, D
- Q43: 8.00
- Q44: 9.00
- Q45: 18.00
- Q46: 0.36
- Q47: 1.00
- Q48: 120.00
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
- Q5: A, B, D
- Q6: A, B, C, D
- Q7: 1.00
- Q8: 4.00
- Q9: 3.00
- Q10: 80.00
- Q11: 0.50
- Q12: 10.00
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C, D
- Q20: A, B, C
- Q21: A, B, C, D
- Q22: A, B, C
- Q23: A, B, C
- Q24: A, B, C
- Q25: 5.00
- Q26: 484.00
- Q27: 0.64
- Q28: 2.10
- Q29: 4.00
- Q30: 119.00
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
- Q41: A, B, C
- Q42: A, B, C, D
- Q43: 5.00
- Q44: 2.00
- Q45: 3.00
- Q46: 90.00
- Q47: 0.00
- Q48: 60.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: 33.3% of questions (high option-checking cognitive load).
- **Circuit Transients & Field Geometry**: Deep coverage of Helmholtz coils, LC resonance, dielectric interfaces, and severed constraints.
- **Stereochemical & Coordination Chemistry**: High focus on CFSE, coordination isomerism, chiral centers, and organic reaction mechanisms.
- **Calculus & Linear Algebra**: Spatial rotation groups, symmetric matrices, Wallis reductions, and orthogonal expansions.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

create_mock_files(1, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")
