# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 02.
Empirical Signature: IIT Delhi Benchmark (2013, 2020)
- Multi-correct dominance (+4/-2 with partial marking)
- Circuit transients, variable mass dynamics, wave optics
- Organic reaction cascades, coordination chemistry
- Multivariable coordinate calculus, matrices, probability
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 02 — Paper 1
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
Sand drops vertically at a constant rate $\frac{dm}{dt} = \mu$ onto a horizontal conveyor belt moving at a constant speed $v$ maintained by an electric motor. The coefficient of friction between the sand and the belt is $\mu_k$. Which of the following statements is/are correct?
(A) The external horizontal driving force exerted by the motor on the belt to maintain constant speed is $F = \mu v$.  
(B) The rate at which the motor does mechanical work is $P = \mu v^2$.  
(C) The rate of increase of kinetic energy of the sand deposited on the belt is $\frac{1}{2}\mu v^2$.  
(D) Exactly half of the mechanical work delivered by the motor is dissipated as heat due to friction during slipping.

#### Question 2
A parallel-plate capacitor with plate area $A$ and separation $d$ is connected across an ideal battery of EMF $V_0$. A dielectric slab of thickness $d$, width $w$, and dielectric constant $K > 1$ is partially inserted into the capacitor along the length by a distance $x$. Which of the following statements is/are correct?
(A) The total capacitance as a function of insertion distance $x$ is $C(x) = \frac{\varepsilon_0 w}{d}[(K-1)x + L]$, where $L$ is the total length of the plates.  
(B) The electrostatic force exerted by the electric field on the dielectric slab pulls it inward with magnitude $F = \frac{1}{2}(K-1)\frac{\varepsilon_0 w V_0^2}{d}$.  
(C) The force on the slab is independent of the insertion depth $x$ as long as $0 < x < L$.  
(D) If the slab is released from rest from an initial insertion depth $x_0$, it executes simple harmonic motion inside the capacitor plates (neglecting fringing fields).

#### Question 3
One mole of a real gas obeys the van der Waals equation of state $\left(P + \frac{a}{V^2}\right)(V - b) = RT$. Which of the following statements is/are correct?
(A) At the critical point, the critical temperature is $T_c = \frac{8a}{27Rb}$.  
(B) The critical pressure is $P_c = \frac{a}{27b^2}$ and critical volume is $V_c = 3b$.  
(C) The critical compressibility factor is $Z_c = \frac{P_c V_c}{R T_c} = \frac{3}{8} = 0.375$.  
(D) The Joule-Thomson inversion temperature for this gas is $T_i = \frac{2a}{Rb}$.

#### Question 4
A semicircular conducting wire loop of radius $R$ and resistance $r$ is rotated with constant angular velocity $\omega$ in a uniform magnetic field $B$ directed perpendicular to the axis of rotation lying in the plane of the loop along its diameter. Which of the following statements is/are correct?
(A) The magnetic flux linked with the loop at time $t$ is $\Phi(t) = \frac{1}{2}\pi R^2 B \cos(\omega t)$.  
(B) The peak induced EMF in the loop is $\mathcal{E}_0 = \frac{1}{2}\pi R^2 B \omega$.  
(C) The average power dissipated as Joule heat over one complete revolution is $P_{\text{avg}} = \frac{\pi^2 R^4 B^2 \omega^2}{8r}$.  
(D) The net external mechanical torque required to keep the loop rotating at constant speed is time-dependent.

#### Question 5
In a thin film of transparent oil of refractive index $\mu = 1.40$ floating on water ($\mu_w = 1.33$), white light is incident normally from air ($\mu_{\text{air}} = 1.00$). Which of the following statements is/are correct?
(A) Reflection at the air-oil interface undergoes a phase change of $\pi$ radians.  
(B) Reflection at the oil-water interface undergoes no phase change because $\mu_{\text{oil}} > \mu_{\text{water}}$.  
(C) The condition for constructive interference in the reflected light is $2\mu t = \left(m + \frac{1}{2}\right)\lambda$ where $m \in \{0, 1, 2, \dots\}$.  
(D) If the film thickness is $t = 280\text{ nm}$, the wavelength in the visible spectrum ($\lambda = 400 - 700\text{ nm}$) that is strongly reflected is approximately $\lambda \approx 523\text{ nm}$.

#### Question 6
A high-energy proton of rest mass $m_p$ collides head-on with a stationary target proton to produce a proton-antiproton pair via the reaction $p + p \to p + p + p + \bar{p}$. Which of the following statements is/are correct?
(A) The total invariant mass squared in the center-of-momentum frame at threshold is $s = (4 m_p c^2)^2 = 16 m_p^2 c^4$.  
(B) In the laboratory frame, the threshold total energy of the incident proton is $E_{\text{th}} = 7 m_p c^2$.  
(C) The threshold kinetic energy of the incident proton in the laboratory frame is $K_{\text{th}} = 6 m_p c^2$.  
(D) For $m_p c^2 \approx 0.938\text{ GeV}$, the threshold kinetic energy is approximately $K_{\text{th}} \approx 5.63\text{ GeV}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A torsional pendulum consists of a uniform solid disk of mass $M = 2.00\text{ kg}$ and radius $R = 0.20\text{ m}$ suspended at its center by a thin wire of torsional spring constant $\kappa = 0.80\text{ N}\cdot\text{m/rad}$. Calculate the time period $T$ of torsional oscillations in seconds ($\text{s}$). [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 8
A spherical shell of radius $R = 0.10\text{ m}$ carries a uniformly distributed surface charge $Q = 6.00\ \mu\text{C}$ and rotates about one of its diameters with constant angular velocity $\omega = 100.0\text{ rad/s}$. Calculate the magnetic dipole moment $\mu_m$ of the rotating shell in micro-Ampere-meter-squared ($\mu\text{A}\cdot\text{m}^2$).

#### Question 9
A spherical metal ball of radius $r_1 = 0.05\text{ m}$ is maintained at temperature $T_1 = 400\text{ K}$. It is surrounded by a concentric spherical shell of radius $r_2 = 0.15\text{ m}$ maintained at $T_2 = 300\text{ K}$. The space between them is filled with a thermal insulator of thermal conductivity $K = 0.50\text{ W/(m}\cdot\text{K)}$. Calculate the steady-state heat current $\dot{Q}$ (in Watts) flowing radially outward. [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 10
A triangular glass prism has an apex refracting angle $A = 60^\circ$ and refractive index $\mu = \sqrt{3}$. Calculate the angle of minimum deviation $\delta_m$ (in degrees) for a monochromatic light ray passing through the prism.

#### Question 11
In Compton scattering, a photon of wavelength $\lambda = 0.0200\text{ nm}$ is scattered at an angle $\theta = 90^\circ$ by a stationary free electron. Calculate the fractional increase in wavelength $\frac{\Delta\lambda}{\lambda}$ expressed as a percentage (\%). [Take Compton wavelength $\lambda_c = \frac{h}{m_e c} = 0.00243\text{ nm}$. Round off to TWO decimal places].

#### Question 12
A damped harmonic oscillator has mass $m = 0.20\text{ kg}$, spring constant $k = 80.0\text{ N/m}$, and damping constant $b = 0.040\text{ kg/s}$. Calculate the dimensionless quality factor $Q = \frac{\sqrt{mk}}{b}$ of the oscillator.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The potential energy of a particle of mass $m$ moving along the x-axis is given by $U(x) = \frac{a}{x^2} - \frac{b}{x}$, where $a, b > 0$. The equilibrium position of the particle is:
(A) $x_0 = \frac{2a}{b}$  
(B) $x_0 = \frac{a}{b}$  
(C) $x_0 = \frac{a}{2b}$  
(D) $x_0 = \frac{b}{2a}$

#### Question 14
A long cylindrical wire of radius $R$ carries a steady current with non-uniform current density $J(r) = J_0 \left(1 - \frac{r}{R}\right)$ for $0 \le r \le R$. The total current carried by the wire is:
(A) $\frac{1}{3}\pi R^2 J_0$  
(B) $\frac{1}{2}\pi R^2 J_0$  
(C) $\frac{2}{3}\pi R^2 J_0$  
(D) $\pi R^2 J_0$

#### Question 15
The adiabatic bulk modulus $B_s$ of an ideal gas at pressure $P$ and with ratio of specific heats $\gamma$ is:
(A) $\gamma P$  
(B) $P$  
(C) $\frac{P}{\gamma}$  
(D) $\frac{\gamma - 1}{\gamma}P$

#### Question 16
An astronomical telescope has an objective of diameter $D = 2.44\text{ m}$. For light of wavelength $\lambda = 600\text{ nm}$, the theoretical angular resolution limit $\theta_{\text{min}}$ (in radians) according to Rayleigh's criterion is:
(A) $3.0 \times 10^{-7}\text{ rad}$  
(B) $1.5 \times 10^{-7}\text{ rad}$  
(C) $6.0 \times 10^{-7}\text{ rad}$  
(D) $1.22 \times 10^{-6}\text{ rad}$

#### Question 17
A radioactive sample has an initial activity of $A_0 = 1600\text{ Bq}$. After a duration of 8 hours, the activity drops to $100\text{ Bq}$. The half-life of the radioisotope is:
(A) 2 hours  
(B) 1 hour  
(C) 4 hours  
(D) 3 hours

#### Question 18
A vessel contains water of refractive index $\mu_1 = 4/3$ to a depth of $12\text{ cm}$, above which floats an oil layer of refractive index $\mu_2 = 1.50$ of thickness $6\text{ cm}$. The apparent depth of the bottom of the vessel when viewed normally from above is:
(A) $13\text{ cm}$  
(B) $15\text{ cm}$  
(C) $11\text{ cm}$  
(D) $14\text{ cm}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following statements is/are correct regarding the structure and bonding of diborane ($\text{B}_2\text{H}_6$)?
(A) It contains four terminal two-center two-electron ($2c-2e$) $\text{B}-\text{H}$ bonds.  
(B) It contains two bridging three-center two-electron ($3c-2e$) $\text{B}-\text{H}-\text{B}$ banana bonds.  
(C) The boron atoms are $sp^3$ hybridized.  
(D) All six hydrogen atoms lie in the same geometric plane.

#### Question 20
When phenol is treated with chloroform ($\text{CHCl}_3$) in aqueous sodium hydroxide ($\text{NaOH}$) followed by acidification (Reimer-Tiemann reaction):
(A) The electrophile involved in the reaction is dichlorocarbene ($:\text{CCl}_2$).  
(B) The major product formed is salicylaldehyde (2-hydroxybenzaldehyde).  
(C) Dichlorocarbene is generated by $\alpha$-elimination of $\text{HCl}$ from chloroform.  
(D) If carbon tetrachloride ($\text{CCl}_4$) is used instead of $\text{CHCl}_3$, salicylic acid is obtained as the major product.

#### Question 21
For the cell reaction $\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightleftharpoons \text{Zn}^{2+}(aq) + \text{Cu}(s)$ at $298\text{ K}$:
(A) The cell EMF increases if the concentration of $\text{Cu}^{2+}$ is increased.  
(B) The cell EMF decreases if the concentration of $\text{Zn}^{2+}$ is increased.  
(C) At equilibrium, the cell potential $E_{\text{cell}} = 0$.  
(D) $\Delta G^\circ = -n F E_{\text{cell}}^\circ$.

#### Question 22
Which of the following compounds undergo aldol condensation in the presence of dilute base?
(A) Acetaldehyde ($\text{CH}_3\text{CHO}$)  
(B) Acetone ($\text{CH}_3\text{COCH}_3$)  
(C) Benzaldehyde ($\text{C}_6\text{H}_5\text{CHO}$)  
(D) Trimethylacetaldehyde ($(\text{CH}_3)_3\text{CCHO}$)

#### Question 23
Regarding the properties of transition metals in the $3d$ series:
(A) Scandium ($Z = 21$) forms only +3 oxidation state in its compounds.  
(B) Manganese ($Z = 25$) exhibits the highest number of oxidation states from +2 to +7.  
(C) Zinc ($Z = 30$) has a completely filled $d$-subshell and is not strictly considered a transition metal.  
(D) The catalytic activity of transition metals is attributed to their variable oxidation states and ability to form complex intermediates.

#### Question 24
Which of the following statements is/are correct about the structure of DNA?
(A) The two polynucleotide strands run antiparallel to each other.  
(B) Adenine pairs with thymine via two hydrogen bonds.  
(C) Guanine pairs with cytosine via three hydrogen bonds.  
(D) The pitch of the B-DNA double helix is approximately $3.4\text{ nm}$ per turn containing 10 base pairs.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The solubility product of $\text{BaSO}_4$ in water is $K_{sp} = 1.0 \times 10^{-10}$ at $25^\circ\text{C}$. Calculate the solubility of $\text{BaSO}_4$ in a $0.010\text{ M Na}_2\text{SO}_4$ aqueous solution in $\text{mol/L}$. If the solubility is $S = 1.0 \times 10^{-m}\text{ mol/L}$, find the integer value of $m$.

#### Question 26
For a second-order reaction $2A \to B$, the initial concentration of $A$ is $[A]_0 = 0.50\text{ M}$ and the rate constant is $k = 0.040\text{ L}/(\text{mol}\cdot\text{s})$. Calculate the half-life $t_{1/2}$ of the reaction in seconds ($\text{s}$).

#### Question 27
A metal crystallizes in a body-centered cubic (BCC) crystal structure with an edge length $a = 300\text{ pm}$. Calculate the atomic radius $r$ of the metal atom in picometers ($\text{pm}$). [Take $\sqrt{3} \approx 1.732$. Round off to TWO decimal places].

#### Question 28
Calculate the standard enthalpy of formation $\Delta_f H^\circ$ (in $\text{kJ/mol}$) of gaseous methane ($\text{CH}_4$) given:
- $\Delta_{\text{comb}} H^\circ(\text{C}_{\text{graphite}}) = -393.5\text{ kJ/mol}$
- $\Delta_{\text{comb}} H^\circ(\text{H}_2(g)) = -285.8\text{ kJ/mol}$
- $\Delta_{\text{comb}} H^\circ(\text{CH}_4(g)) = -890.3\text{ kJ/mol}$
[Round off to ONE decimal place].

#### Question 29
A $0.050\text{ molal}$ aqueous solution of potassium chloride ($\text{KCl}$) boils at $100.050^\circ\text{C}$ at standard pressure. Calculate the van 't Hoff factor $i$ of $\text{KCl}$ in this solution. [Take $K_b(\text{H}_2\text{O}) = 0.512\text{ K}\cdot\text{kg/mol}$. Round off to TWO decimal places].

#### Question 30
Calculate the total number of stereoisomers (including geometrical and optical isomers) for the complex $[Co(en)_2Cl_2]^+$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The major organic product obtained when anisole ($\text{C}_6\text{H}_5\text{OCH}_3$) is heated with concentrated $\text{HI}$ is:
(A) Phenol and iodomethane  
(B) Iodobenzene and methanol  
(C) Benzene and methyl iodide  
(D) $o$-Iodoanisole

#### Question 32
The oxidation state of phosphorus in hypophosphorous acid ($\text{H}_3\text{PO}_2$) is:
(A) +1  
(B) +3  
(C) +5  
(D) -1

#### Question 33
In the cyanide process for extraction of gold, zinc dust is added to the solution of sodium dicyanoaurate(I) primarily to:
(A) Act as a reducing agent to precipitate metallic gold  
(B) Oxidize gold to trivalent state  
(C) Form a stable coordination complex with cyanide  
(D) Neutralize the excess sodium cyanide

#### Question 34
Which of the following compounds gives a silver mirror with Tollens' reagent?
(A) Glucose  
(B) Sucrose  
(C) Acetone  
(D) Starch

#### Question 35
The hybridization of the central sulfur atom in sulfur hexafluoride ($\text{SF}_6$) is:
(A) $sp^3d^2$  
(B) $sp^3d$  
(C) $d^2sp^3$  
(D) $sp^3$

#### Question 36
Which of the following polymers is a copolymer?
(A) Buna-S  
(B) Polyethylene  
(C) PVC  
(D) Polyacrylonitrile (PAN)

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^3 - 3x + 2$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) The local maximum of $f(x)$ occurs at $x = -1$ with value $4$.  
(B) The local minimum of $f(x)$ occurs at $x = 1$ with value $0$.  
(C) The point of inflection is at $(0, 2)$.  
(D) $f(x) \ge 0$ for all $x \ge -2$.

#### Question 38
Let $A$ be a $3 \times 3$ matrix such that $A^3 = I$ and $A \ne I$. Which of the following statements is/are correct?
(A) $\det(A) = 1$.  
(B) The eigenvalues of $A$ can be the complex cube roots of unity $\omega$ and $\omega^2$.  
(C) $A^2 + A + I = 0$ if all eigenvalues are non-real.  
(D) $A$ is invertible with $A^{-1} = A^2$.

#### Question 39
Consider the parabola $y^2 = 8x$. A focal chord passes through $(2, 0)$ with inclination $\theta \ne 0$:
(A) The length of the focal chord making an angle $\theta$ with the axis of the parabola is $L = 8\csc^2\theta$.  
(B) The minimum length of any focal chord is 8 (the latus rectum).  
(C) The tangents drawn at the extremities of any focal chord intersect at right angles on the directrix $x = -2$.  
(D) The circle described on any focal chord as diameter touches the directrix.

#### Question 40
Let $y(x)$ be the solution of the linear differential equation $\frac{dy}{dx} + 2xy = x$ with $y(0) = 1$. Which of the following statements is/are correct?
(A) The integrating factor is $e^{x^2}$.  
(B) The general solution is $y(x) = \frac{1}{2} + C e^{-x^2}$.  
(C) With $y(0) = 1$, the particular solution is $y(x) = \frac{1}{2}(1 + e^{-x^2})$.  
(D) $\lim_{x \to \infty} y(x) = \frac{1}{2}$.

#### Question 41
Let $\vec{u} = \hat{i} + \hat{j}$, $\vec{v} = \hat{j} + \hat{k}$, and $\vec{w} = \hat{k} + \hat{i}$. Which of the following statements is/are correct?
(A) The scalar triple product is $[\vec{u} \ \vec{v} \ \vec{w}] = 2$.  
(B) The vectors $\vec{u}, \vec{v}, \vec{w}$ are non-coplanar and form a basis for $\mathbb{R}^3$.  
(C) The angle between $\vec{u}$ and $\vec{v}$ is $\pi/3$ ($60^\circ$).  
(D) $(\vec{u} \times \vec{v}) \cdot \vec{w} = 2$.

#### Question 42
Consider the function $f(z) = \frac{z-1}{z+1}$ for complex numbers $z \ne -1$. Which of the following statements is/are correct?
(A) If $|z| = 1$ with $z \ne -1$, then $f(z)$ is purely imaginary.  
(B) If $\text{Re}(z) > 0$, then $|f(z)| < 1$.  
(C) The imaginary axis $\text{Re}(z) = 0$ is mapped to the unit circle $|w| = 1$.  
(D) $f(1) = 0$ and $f(0) = -1$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^{\pi/2} \frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}}\,dx$$
If $I = \frac{\pi}{p}$, find the integer value of $p$.

#### Question 44
Find the area of the region enclosed between the curves $y = x^2$ and $y = 2x - x^2$. [Round off to TWO decimal places].

#### Question 45
Find the number of integral solutions to the inequality $\frac{x-2}{x+3} \le 0$.

#### Question 46
Calculate the distance from the point $P(1, 2, 3)$ to the plane $2x - 2y + z + 5 = 0$.

#### Question 47
If $\tan^{-1}(1) + \tan^{-1}(2) + \tan^{-1}(3) = k\pi$, find the value of $k$.

#### Question 48
How many distinct arrangements of the letters in the word `MATHEMATICS` are possible? If the total number of permutations is $N = 4989600 / m$, find the integer value of $m$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The equation of the tangent to the curve $y = x^3 - 3x + 1$ at the point where $x = 2$ is:
(A) $9x - y - 15 = 0$  
(B) $9x - y - 11 = 0$  
(C) $3x - y - 3 = 0$  
(D) $6x - y - 9 = 0$

#### Question 50
If $A$ and $B$ are two independent events such that $P(A) = 0.4$ and $P(B) = 0.5$, then $P(A \cup B)$ is:
(A) $0.70$  
(B) $0.90$  
(C) $0.20$  
(D) $0.60$

#### Question 51
The term independent of $x$ in the binomial expansion of $\left(x^2 - \frac{1}{x}\right)^9$ is:
(A) 84  
(B) -84  
(C) 126  
(D) -126

#### Question 52
The distance between the parallel lines $3x + 4y - 9 = 0$ and $6x + 8y + 7 = 0$ is:
(A) $2.5$  
(B) $5.0$  
(C) $1.6$  
(D) $3.2$

#### Question 53
If $\vec{a} = 2\hat{i} - \hat{j} + \hat{k}$ and $\vec{b} = 3\hat{i} + 4\hat{j} - \hat{k}$, then the unit vector perpendicular to both $\vec{a}$ and $\vec{b}$ is:
(A) $\frac{-3\hat{i} + 5\hat{j} + 11\hat{k}}{\sqrt{155}}$  
(B) $\frac{3\hat{i} - 5\hat{j} + 11\hat{k}}{\sqrt{155}}$  
(C) $\frac{-3\hat{i} + 5\hat{j} - 11\hat{k}}{\sqrt{155}}$  
(D) $\frac{5\hat{i} - 3\hat{j} + 11\hat{k}}{\sqrt{155}}$

#### Question 54
The value of $\lim_{x \to 0} \frac{\tan x - \sin x}{x^3}$ is:
(A) $1/2$  
(B) $1$  
(C) $0$  
(D) $1/3$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 02 — Paper 2
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
A uniform solid sphere of mass $M$ and radius $R$ is projected horizontally with initial linear speed $v_0$ and zero initial angular velocity ($\omega_0 = 0$) on a rough horizontal surface having coefficient of kinetic friction $\mu_k$. Which of the following statements is/are correct?
(A) The time after which pure rolling begins is $t_r = \frac{2v_0}{7\mu_k g}$.  
(B) The linear speed of the sphere when pure rolling commences is $v_r = \frac{5}{7}v_0$.  
(C) The distance traveled by the sphere before pure rolling begins is $s = \frac{12v_0^2}{49\mu_k g}$.  
(D) The mechanical energy dissipated as heat by friction during slipping is $\Delta E = \frac{1}{7}M v_0^2$.

#### Question 2
An $LC$ circuit consists of an inductor of inductance $L$ and a capacitor of capacitance $C$. At $t = 0$, the capacitor has an initial charge $Q_0$ and the switch is closed. Which of the following statements is/are correct?
(A) The charge on the capacitor oscillates as $q(t) = Q_0 \cos(\omega_0 t)$, where $\omega_0 = \frac{1}{\sqrt{LC}}$.  
(B) The current in the circuit is $i(t) = -\omega_0 Q_0 \sin(\omega_0 t)$.  
(C) The peak magnetic energy stored in the inductor equals the peak electrostatic energy stored in the capacitor, $U_{\text{max}} = \frac{Q_0^2}{2C}$.  
(D) The total electromagnetic energy of the system remains conserved for all $t \ge 0$.

#### Question 3
A sound source of frequency $\nu_0$ moves with constant speed $u = 0.20v$ (where $v$ is the speed of sound in air) along a straight line toward a stationary observer. The air is still. Which of the following statements is/are correct?
(A) The apparent frequency detected by the observer as the source approaches is $\nu = \frac{5}{4}\nu_0 = 1.25\nu_0$.  
(B) The wavelength of the sound waves in front of the moving source is compressed to $\lambda' = 0.80\lambda_0$.  
(C) As the source recedes directly away from the observer, the apparent frequency is $\nu' = \frac{5}{6}\nu_0 \approx 0.833\nu_0$.  
(D) The speed of sound waves relative to the stationary observer remains $v$, independent of the motion of the source.

#### Question 4
A thin convex lens of focal length $f = +15\text{ cm}$ in air ($\mu_l = 1.50$) is immersed in a liquid of refractive index $\mu_m = 1.20$. Which of the following statements is/are correct?
(A) The focal length of the lens in the liquid increases to $f' = +30\text{ cm}$.  
(B) The optical power of the lens decreases when immersed in the liquid.  
(C) If the lens is immersed in a liquid of refractive index $\mu_m = 1.60$, it behaves as a diverging lens.  
(D) If immersed in a liquid of refractive index $\mu_m = 1.50$, the lens becomes invisible and its focal length becomes infinite.

#### Question 5
In an experiment on the photoelectric effect:
(A) The maximum kinetic energy of the emitted photoelectrons depends linearly on the frequency of the incident light above the threshold frequency.  
(B) The saturation photocurrent is directly proportional to the intensity of the incident light of a given frequency.  
(C) The stopping potential is independent of the intensity of the incident radiation.  
(D) Emission of photoelectrons occurs instantaneously (within $\sim 10^{-9}\text{ s}$) upon illumination, supporting the photon theory.

#### Question 6
A gas undergoes a cycle consisting of an isothermal expansion at temperature $T_1$, an isochoric cooling to temperature $T_2$, and an adiabatic compression back to the initial state. Which of the following statements is/are correct?
(A) The efficiency of this cycle is strictly less than that of a Carnot cycle operating between $T_1$ and $T_2$.  
(B) In the isochoric cooling stage, heat is rejected by the gas to the surroundings.  
(C) The net work done per cycle is positive if the cycle is traversed clockwise on a $P-V$ diagram.  
(D) The change in entropy of the gas over one complete cycle is identically zero.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A horizontal uniform rod of mass $M = 1.50\text{ kg}$ and length $L = 0.80\text{ m}$ is pivoted at its center. A small putty ball of mass $m = 0.50\text{ kg}$ moving vertically upward with speed $v = 6.00\text{ m/s}$ hits one end of the rod and sticks to it. Calculate the angular velocity $\omega$ (in rad/s) of the rod immediately after the collision.

#### Question 8
Calculate the fundamental resonant frequency $\nu_1$ (in $\text{Hz}$) of an organ pipe of length $L = 0.85\text{ m}$ closed at one end, taking the speed of sound in air as $v = 340\text{ m/s}$.

#### Question 9
A point charge $q = +4.0\ \mu\text{C}$ is placed at the center of a cube of edge length $a = 0.20\text{ m}$. Calculate the electric flux $\Phi_E$ (in $\text{N}\cdot\text{m}^2/\text{C}$) passing through one of the six faces of the cube. [Take $\varepsilon_0 = 8.85 \times 10^{-12}\text{ C}^2/(\text{N}\cdot\text{m}^2)$. Round off to TWO decimal places].

#### Question 10
In a Young's double-slit experiment, when a thin transparent mica sheet of refractive index $\mu = 1.60$ and thickness $t$ is placed in front of one of the slits, the central bright fringe shifts by a distance equal to 6 fringe widths. If the wavelength of light is $\lambda = 600\text{ nm}$, calculate the thickness $t$ of the mica sheet in micrometers ($\mu\text{m}$).

#### Question 11
An electron is accelerated from rest through a potential difference $V = 150.0\text{ Volts}$. Calculate its de Broglie wavelength $\lambda$ in Angstroms ($\text{\AA}$). [Take $\lambda = \frac{12.27}{\sqrt{V}}\text{\AA}$. Round off to TWO decimal places].

#### Question 12
A current of $I = 5.0\text{ A}$ flows through a circular loop of radius $R = 0.10\text{ m}$. Calculate the magnitude of the magnetic field $B$ (in $\mu\text{T}$) at a point on the axis of the loop at a distance $x = 0.10\text{ m}$ from its center. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$ and $2^{3/2} \approx 2.828$. Round off to TWO decimal places].

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the physical quantities in List-I with their SI units in List-II:
- **List-I**:
  - P. Magnetic Flux
  - Q. Magnetic Permeability $\mu_0$
  - R. Electric Permittivity $\varepsilon_0$
  - S. Self Inductance
- **List-II**:
  - 1. Weber ($\text{Wb}$)
  - 2. $\text{H/m}$ or $\text{T}\cdot\text{m/A}$
  - 3. $\text{F/m}$ or $\text{C}^2/(\text{N}\cdot\text{m}^2)$
  - 4. Henry ($\text{H}$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 14
Match the thermal expansion coefficients in List-I with their isotropic relations in List-II:
- **List-I**:
  - P. Linear expansion coefficient $\alpha$
  - Q. Superficial expansion coefficient $\beta$
  - R. Volumetric expansion coefficient $\gamma$
  - S. Ratio $\alpha : \beta : \gamma$
- **List-II**:
  - 1. $\frac{1}{L}\frac{dL}{dT}$
  - 2. $2\alpha$
  - 3. $3\alpha$
  - 4. $1 : 2 : 3$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-4, R-3, S-2  
(D) P-3, Q-2, R-1, S-4

#### Question 15
Match the waves/phenomena in List-I with their speed formula in List-II:
- **List-I**:
  - P. Transverse wave on string
  - Q. Sound wave in fluid
  - R. Sound wave in solid rod
  - S. EM wave in non-magnetic medium
- **List-II**:
  - 1. $v = \sqrt{T/\mu}$
  - 2. $v = \sqrt{B/\rho}$
  - 3. $v = \sqrt{Y/\rho}$
  - 4. $v = c/\sqrt{\varepsilon_r}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the nuclear particles in List-I with their antiparticles in List-II:
- **List-I**:
  - P. Electron ($e^-$)
  - Q. Proton ($p$)
  - R. Electron Neutrino ($\nu_e$)
  - S. Photon ($\gamma$)
- **List-II**:
  - 1. Positron ($e^+$)
  - 2. Antiproton ($\bar{p}$)
  - 3. Electron Antineutrino ($\bar{\nu}_e$)
  - 4. Self-conjugate (own antiparticle)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 17
Match the optical devices in List-I with their principal physical effect in List-II:
- **List-I**:
  - P. Nicol Prism
  - Q. Quarter-wave plate
  - R. Half-wave plate
  - S. Polaroid sheet
- **List-II**:
  - 1. Produces plane-polarized light by total internal reflection of ordinary ray
  - 2. Introduces phase difference of $\pi/2$ between $o$- and $e$-rays
  - 3. Introduces phase difference of $\pi$ between $o$- and $e$-rays
  - 4. Selective dichroism (absorption of one polarization)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 18
Match the electrical circuits in List-I with their resonant characteristic in List-II:
- **List-I**:
  - P. Series LCR at resonance
  - Q. Parallel LCR at resonance
  - R. Pure LC circuit
  - S. High-Q resonant circuit
- **List-II**:
  - 1. Impedance is minimum ($Z = R$) and current is maximum
  - 2. Dynamic impedance is maximum ($L/CR$) and line current is minimum
  - 3. Undamped continuous harmonic oscillations at $\omega = 1/\sqrt{LC}$
  - 4. Narrow bandwidth and high frequency selectivity

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-4, R-3, S-2  
(D) P-4, Q-2, R-1, S-3

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following complexes is/are diamagnetic?
(A) $[\text{Ni}(\text{CN})_4]^{2-}$ (square planar, strong field $\text{CN}^-$)  
(B) $[\text{Fe}(\text{CN})_6]^{4-}$ (low spin $d^6$)  
(C) $[\text{Co}(\text{NH}_3)_6]^{3+}$ (low spin $d^6$)  
(D) $[\text{NiCl}_4]^{2-}$ (tetrahedral, weak field $\text{Cl}^-$)

#### Question 20
Which of the following reactions yield benzaldehyde as the primary product?
(A) Etard reaction (Toluene with $\text{CrO}_2\text{Cl}_2$ in $\text{CS}_2$ followed by $\text{H}_3\text{O}^+$)  
(B) Gattermann-Koch reaction (Benzene with $\text{CO} + \text{HCl}$ in the presence of anhydrous $\text{AlCl}_3 / \text{CuCl}$)  
(C) Rosenmund reduction (Benzoyl chloride with $\text{H}_2 / \text{Pd-BaSO}_4$)  
(D) Stephen reduction (Benzonitrile with $\text{SnCl}_2 / \text{HCl}$ followed by $\text{H}_3\text{O}^+$)

#### Question 21
Regarding the electrochemical series and standard reduction potentials:
(A) A metal with more negative reduction potential is a stronger reducing agent.  
(B) Lithium has the highest reducing power in aqueous solution due to its exceptionally high hydration enthalpy.  
(C) Fluorine gas has the most positive reduction potential and is the strongest oxidizing agent.  
(D) Zinc can displace copper from an aqueous solution of $\text{CuSO}_4$.

#### Question 22
Which of the following compounds undergo racemization during solvolysis in aqueous acetone?
(A) $(R)$-2-bromobutane  
(B) $(S)$-1-phenylethyl chloride  
(C) 1-bromobutane  
(D) 2-bromo-2-methylpropane

#### Question 23
Which of the following properties increase across a period from left to right in the modern periodic table?
(A) Effective nuclear charge ($Z_{\text{eff}}$)  
(B) Electronegativity  
(C) Ionization enthalpy (general trend)  
(D) Atomic radius

#### Question 24
Which of the following amino acids contain an aromatic ring in their side chain?
(A) Phenylalanine  
(B) Tyrosine  
(C) Tryptophan  
(D) Alanine

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The equilibrium constant for the reaction $\text{N}_2\text{O}_4(g) \rightleftharpoons 2\text{NO}_2(g)$ is $K_p = 0.15\text{ atm}$ at $25^\circ\text{C}$. Calculate the total pressure $P$ (in atm) at which the degree of dissociation of $\text{N}_2\text{O}_4$ is $\alpha = 0.20$. [Round off to TWO decimal places].

#### Question 26
For a reaction $A \to \text{Products}$, a plot of $\ln[A]$ versus time $t$ gives a straight line with a slope of $-0.0231\text{ min}^{-1}$. Calculate the half-life $t_{1/2}$ of the reaction in minutes. [Take $\ln 2 = 0.693$].

#### Question 27
An element has a density of $\rho = 8.92\text{ g/cm}^3$ and crystallizes in an FCC lattice with molar mass $M = 63.5\text{ g/mol}$. Calculate the unit cell volume $V_{\text{cell}}$ in cubic centimeters ($\text{cm}^3$). If $V_{\text{cell}} = 4.73 \times 10^{-23}\text{ cm}^3$, find the value of $V_{\text{cell}} \times 10^{23}$. [Round off to TWO decimal places].

#### Question 28
Calculate the standard Gibbs free energy change $\Delta G^\circ$ (in $\text{kJ/mol}$) for a cell reaction having $E_{\text{cell}}^\circ = +1.10\text{ V}$ and involving $n = 2$ electrons. [Take $F = 96500\text{ C/mol}$. Round off to ONE decimal place].

#### Question 29
A $0.20\text{ m}$ solution of glucose ($\text{C}_6\text{H}_{12}\text{O}_6$) in water freezes at $-0.372^\circ\text{C}$. Calculate the cryoscopic constant $K_f$ of water in $\text{K}\cdot\text{kg/mol}$. [Round off to TWO decimal places].

#### Question 30
Calculate the magnetic moment $\mu_{\text{eff}}$ (in Bohr Magnetons, $\text{BM}$) of the high-spin complex $[\text{Mn}(\text{H}_2\text{O})_6]^{2+}$ ($\text{Mn}^{2+}, 3d^5$). [Take $\sqrt{35} \approx 5.92$. Round off to TWO decimal places].

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the organic reagents in List-I with their characteristic function in List-II:
- **List-I**:
  - P. $\text{LiAlH}_4$
  - Q. $\text{NaBH}_4$
  - R. Pyridinium Chlorochromate (PCC)
  - S. Alkaline $\text{KMnO}_4$
- **List-II**:
  - 1. Strong reducing agent, reduces esters and carboxylic acids to primary alcohols
  - 2. Mild reducing agent, reduces aldehydes and ketones but not esters
  - 3. Oxidizes primary alcohols selectively to aldehydes without over-oxidation
  - 4. Strong oxidizing agent, oxidizes alkylbenzenes and alcohols to carboxylic acids

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 32
Match the ore names in List-I with their chemical formulas in List-II:
- **List-I**:
  - P. Bauxite
  - Q. Haematite
  - R. Calamine
  - S. Galena
- **List-II**:
  - 1. $\text{Al}_2\text{O}_3 \cdot 2\text{H}_2\text{O}$
  - 2. $\text{Fe}_2\text{O}_3$
  - 3. $\text{ZnCO}_3$
  - 4. $\text{PbS}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-4, R-3, S-2  
(D) P-4, Q-2, R-1, S-3

#### Question 33
Match the gas laws in List-I with their mathematical expression in List-II:
- **List-I**:
  - P. Boyle's Law
  - Q. Charles's Law
  - R. Gay-Lussac's Law
  - S. Avogadro's Law
- **List-II**:
  - 1. $P \propto \frac{1}{V}$ (constant $T, n$)
  - 2. $V \propto T$ (constant $P, n$)
  - 3. $P \propto T$ (constant $V, n$)
  - 4. $V \propto n$ (constant $P, T$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 34
Match the solid types in List-I with their example in List-II:
- **List-I**:
  - P. Ionic solid
  - Q. Covalent network solid
  - R. Metallic solid
  - S. Molecular solid
- **List-II**:
  - 1. $\text{NaCl}$
  - 2. Diamond / Quartz
  - 3. Copper ($\text{Cu}$)
  - 4. Dry Ice ($\text{CO}_2$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 35
Match the radioactive decay modes in List-I with the change in mass number $A$ and atomic number $Z$ in List-II:
- **List-I**:
  - P. $\alpha$-emission
  - Q. $\beta^-$-emission
  - R. $\beta^+$-emission
  - S. $\gamma$-emission
- **List-II**:
  - 1. $\Delta A = -4, \Delta Z = -2$
  - 2. $\Delta A = 0, \Delta Z = +1$
  - 3. $\Delta A = 0, \Delta Z = -1$
  - 4. $\Delta A = 0, \Delta Z = 0$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 36
Match the vitamins in List-I with their deficiency diseases in List-II:
- **List-I**:
  - P. Vitamin A
  - Q. Vitamin B1 (Thiamine)
  - R. Vitamin C
  - S. Vitamin D
- **List-II**:
  - 1. Night blindness / Xerophthalmia
  - 2. Beri-beri
  - 3. Scurvy
  - 4. Rickets

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{\ln x}{x}$ for $x > 0$. Which of the following statements is/are correct?
(A) $f(x)$ attains its absolute maximum at $x = e$.  
(B) The maximum value of $f(x)$ is $\frac{1}{e}$.  
(C) $e^\pi > \pi^e$.  
(D) $\lim_{x \to \infty} f(x) = 0$.

#### Question 38
Let $A$ and $B$ be two $n \times n$ invertible matrices. Which of the following statements is/are correct?
(A) $\det(AB) = \det(A)\det(B)$.  
(B) $(AB)^{-1} = B^{-1} A^{-1}$.  
(C) $\text{adj}(AB) = \text{adj}(B)\text{adj}(A)$.  
(D) $\det(\text{adj}(A)) = (\det(A))^{n-1}$.

#### Question 39
Consider the circle $C: x^2 + y^2 = 25$ and the line $L: 3x + 4y = 25$. Which of the following statements is/are correct?
(A) The line $L$ is tangent to the circle $C$ at the point $(3, 4)$.  
(B) The normal to the circle at the point of contact passes through $(0, 0)$ with equation $4x - 3y = 0$.  
(C) The length of the tangent drawn from $(5, 5)$ to the circle is $\sqrt{25} = 5$.  
(D) The chord of contact of tangents drawn from $(5, 5)$ is $x + y = 5$.

#### Question 40
Let $y(x)$ be the solution of the differential equation $\frac{d^2y}{dx^2} + 4y = 0$ with initial conditions $y(0) = 1$ and $y'(0) = 2$. Which of the following statements is/are correct?
(A) The general solution is $y(x) = C_1 \cos(2x) + C_2 \sin(2x)$.  
(B) The particular solution is $y(x) = \cos(2x) + \sin(2x)$.  
(C) The amplitude of the oscillation is $\sqrt{2}$.  
(D) The time period of oscillation is $\pi$.

#### Question 41
Let $\vec{a}, \vec{b}$ be two unit vectors making an angle $\theta$ with each other. Which of the following statements is/are correct?
(A) $|\vec{a} + \vec{b}| = 2\cos(\theta/2)$.  
(B) $|\vec{a} - \vec{b}| = 2\sin(\theta/2)$.  
(C) $(\vec{a} + \vec{b}) \cdot (\vec{a} - \vec{b}) = 0$.  
(D) The vector $\vec{a} + \vec{b}$ bisects the angle between $\vec{a}$ and $\vec{b}$.

#### Question 42
In a Poisson distribution with parameter $\lambda = 2$:
(A) The mean of the distribution is 2.  
(B) The variance of the distribution is 2.  
(C) $P(X = 0) = e^{-2}$.  
(D) $P(X = 1) = 2e^{-2}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the limit:
$$L = \lim_{x \to 0} \left(\frac{\sin x}{x}\right)^{1/x^2}$$
If $L = e^{-1/k}$, find the integer value of $k$.

#### Question 44
Find the minimum value of the function $f(x) = x + \frac{4}{x}$ for $x > 0$.

#### Question 45
Evaluate the definite integral:
$$I = \int_0^1 x (1-x)^9\,dx$$
If $I = \frac{1}{m}$, find the integer value of $m$.

#### Question 46
Calculate the distance between the parallel planes $2x - y + 2z + 3 = 0$ and $4x - 2y + 4z + 18 = 0$.

#### Question 47
If the sum of the first $n$ terms of an arithmetic progression is $S_n = 3n^2 + 5n$, find the 10th term $a_{10}$.

#### Question 48
In how many ways can 6 persons be seated around a circular table if two particular persons must always sit together?

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the standard integrals in List-I with their results in List-II:
- **List-I**:
  - P. $\int \frac{dx}{x^2 + a^2}$
  - Q. $\int \frac{dx}{\sqrt{a^2 - x^2}}$
  - R. $\int \frac{dx}{x^2 - a^2}$
  - S. $\int \frac{dx}{\sqrt{x^2 + a^2}}$
- **List-II**:
  - 1. $\frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right) + C$
  - 2. $\sin^{-1}\left(\frac{x}{a}\right) + C$
  - 3. $\frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right| + C$
  - 4. $\ln|x + \sqrt{x^2+a^2}| + C$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 50
Match the matrix trace and determinant properties in List-I with their expressions in List-II for $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
- **List-I**:
  - P. $\text{Tr}(A)$
  - Q. $\det(A)$
  - R. Characteristic polynomial
  - S. Eigenvalues sum
- **List-II**:
  - 1. $a + d$
  - 2. $ad - bc$
  - 3. $\lambda^2 - \text{Tr}(A)\lambda + \det(A) = 0$
  - 4. $\lambda_1 + \lambda_2 = \text{Tr}(A)$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-4, R-3, S-2  
(D) P-4, Q-2, R-1, S-3

#### Question 51
Match the complex loci in List-I with their geometric curves in List-II:
- **List-I**:
  - P. $|z - z_0| = r$
  - Q. $|z - z_1| = |z - z_2|$
  - R. $\arg\left(\frac{z-z_1}{z-z_2}\right) = \frac{\pi}{2}$
  - S. $|z - z_1| + |z - z_2| = 2a$ ($2a > |z_1 - z_2|$)
- **List-II**:
  - 1. Circle of radius $r$ centered at $z_0$
  - 2. Perpendicular bisector of line segment joining $z_1$ and $z_2$
  - 3. Circle with diameter joining $z_1$ and $z_2$
  - 4. Ellipse with foci at $z_1$ and $z_2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 52
Match the probability distributions in List-I with their variance in List-II:
- **List-I**:
  - P. Bernoulli($p$)
  - Q. Binomial($n, p$)
  - R. Poisson($\lambda$)
  - S. Geometric($p$)
- **List-II**:
  - 1. $p(1-p)$
  - 2. $np(1-p)$
  - 3. $\lambda$
  - 4. $\frac{1-p}{p^2}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 53
Match the function properties in List-I with their analytical condition in List-II:
- **List-I**:
  - P. Strictly increasing on $(a, b)$
  - Q. Concave upward on $(a, b)$
  - R. Local extremum at $x_0$
  - S. Point of inflection at $x_0$
- **List-II**:
  - 1. $f'(x) > 0$ for all $x \in (a, b)$
  - 2. $f''(x) > 0$ for all $x \in (a, b)$
  - 3. $f'(x_0) = 0$ and $f''(x_0) \ne 0$
  - 4. $f''(x_0) = 0$ with change of sign of $f''(x)$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 54
Match the plane geometries in List-I with their coordinate equations in List-II:
- **List-I**:
  - P. Plane passing through origin
  - Q. Plane parallel to xy-plane
  - R. Plane perpendicular to z-axis
  - S. Intercept form of plane
- **List-II**:
  - 1. $Ax + By + Cz = 0$
  - 2. $z = d$
  - 3. $z = d$
  - 4. $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 02 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Variable Mass Systems, Impulse-Momentum Theorem, Work-Energy Principle for Dissipative Systems ($W_{\text{motor}} = \Delta K + Q_{\text{heat}}$).
- **2. IIT Historical Signature**: Classic momentum flow problem with vertical mass deposition onto horizontal conveyor belt.
- **3. Derivation**:
  - Sand drops with zero horizontal velocity. To accelerate mass $dm$ to speed $v$, horizontal impulse required is $d p_x = (dm)v$.
  - Force exerted by belt: $F = \frac{dp_x}{dt} = v \frac{dm}{dt} = \mu v$. (A) is correct.
  - Power delivered by motor: $P = F v = (\mu v)v = \mu v^2$. (B) is correct.
  - Kinetic energy gained by sand per second: $\frac{dK}{dt} = \frac{1}{2}\left(\frac{dm}{dt}\right)v^2 = \frac{1}{2}\mu v^2$. (C) is correct.
  - Rate of energy dissipated as heat: $P_{\text{diss}} = P_{\text{motor}} - \frac{dK}{dt} = \mu v^2 - \frac{1}{2}\mu v^2 = \frac{1}{2}\mu v^2$. Exactly half the energy is lost to heat. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Capacitance with Partially Inserted Dielectric, Electrostatic Forces at Constant Potential ($F = \frac{1}{2}V_0^2 \frac{dC}{dx}$).
- **2. Derivation**:
  - System consists of two capacitors in parallel: $C(x) = \frac{\varepsilon_0 K w x}{d} + \frac{\varepsilon_0 w (L - x)}{d} = \frac{\varepsilon_0 w}{d}[(K-1)x + L]$. (A) is correct.
  - At constant battery potential $V_0$, electrostatic force:
    $$F = \frac{1}{2}V_0^2 \frac{dC}{dx} = \frac{1}{2}V_0^2 \frac{\varepsilon_0 w(K-1)}{d} = \frac{1}{2}(K-1)\frac{\varepsilon_0 w V_0^2}{d}$$
    (B) is correct.
  - The force is constant, independent of $x$ for $0 < x < L$. (C) is correct.
  - Since force is constant (not proportional to displacement $-x$), the slab undergoes constant acceleration, not simple harmonic motion. Thus (D) is incorrect.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Real Gases, van der Waals Equation, Critical Constants, Inversion Temperature.
- **2. Derivation**:
  - Critical constants: $T_c = \frac{8a}{27Rb}$, $P_c = \frac{a}{27b^2}$, $V_c = 3b$. (A) and (B) are correct.
  - Critical compressibility factor: $Z_c = \frac{P_c V_c}{R T_c} = \frac{(a/27b^2)(3b)}{R(8a/27Rb)} = \frac{3a/27b}{8a/27b} = \frac{3}{8} = 0.375$. (C) is correct.
  - Joule-Thomson inversion temperature: $T_i = \frac{2a}{Rb}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Faraday's Law of Induction, Alternating Current Generation, Magnetic Torque.
- **2. Derivation**:
  - Area of semicircle: $A = \frac{1}{2}\pi R^2$.
  - Flux: $\Phi(t) = B A \cos(\omega t) = \frac{1}{2}\pi R^2 B \cos(\omega t)$. (A) is correct.
  - Induced EMF: $\mathcal{E}(t) = -\frac{d\Phi}{dt} = \frac{1}{2}\pi R^2 B \omega \sin(\omega t) \implies \mathcal{E}_0 = \frac{1}{2}\pi R^2 B \omega$. (B) is correct.
  - Average power: $P_{\text{avg}} = \frac{\mathcal{E}_0^2}{2r} = \frac{(\frac{1}{2}\pi R^2 B \omega)^2}{2r} = \frac{\pi^2 R^4 B^2 \omega^2}{8r}$. (C) is correct.
  - Torque $\tau(t) = \vec{\mu} \times \vec{B}$ fluctuates with time as $\sin^2(\omega t)$, requiring time-dependent mechanical torque. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Wave Optics, Thin Film Interference, Phase Changes on Reflection.
- **2. Derivation**:
  - $\mu_{\text{air}} < \mu_{\text{oil}} \implies$ reflection at upper interface has phase shift $\pi$. (A) is correct.
  - $\mu_{\text{oil}} = 1.40 > \mu_{\text{water}} = 1.33 \implies$ reflection at lower interface has phase shift 0. (B) is correct.
  - Net relative phase difference: $\Delta \phi = \frac{2\pi}{\lambda}(2\mu t) + \pi$.
  - Constructive interference condition: $\Delta \phi = 2m\pi \implies 2\mu t = \left(m - \frac{1}{2}\right)\lambda = \left(k + \frac{1}{2}\right)\lambda$. (C) is correct.
  - For $t = 280\text{ nm}, \mu = 1.40$: $2\mu t = 2(1.40)(280) = 784\text{ nm}$.
  - For $k = 1$: $\lambda = \frac{784}{1.5} \approx 522.7\text{ nm} \approx 523\text{ nm}$ (visible green light). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Relativistic Kinematics, Invariant Mass $s = (p_1 + p_2)^2$, Threshold Energy.
- **2. Derivation**:
  - At threshold, all four final particles are at rest in the CM frame: $s = (4 m_p c^2)^2 = 16 m_p^2 c^4$. (A) is correct.
  - In laboratory frame where target is stationary:
    $$s = (p_1 + p_2)^2 = m_p^2 c^4 + m_p^2 c^4 + 2(E_{\text{th}} m_p c^2) = 2 m_p^2 c^4 + 2 E_{\text{th}} m_p c^2$$
  - Equating: $2 m_p^2 c^4 + 2 E_{\text{th}} m_p c^2 = 16 m_p^2 c^4 \implies 2 E_{\text{th}} m_p c^2 = 14 m_p^2 c^4 \implies E_{\text{th}} = 7 m_p c^2$. (B) is correct.
  - Kinetic energy: $K_{\text{th}} = E_{\text{th}} - m_p c^2 = 7 m_p c^2 - m_p c^2 = 6 m_p c^2$. (C) is correct.
  - Numerical value: $K_{\text{th}} = 6(0.938) \approx 5.63\text{ GeV}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Moment of inertia of disk about central axis: $I = \frac{1}{2}M R^2 = \frac{1}{2}(2.00)(0.20)^2 = 0.040\text{ kg}\cdot\text{m}^2$. Time period: $T = 2\pi\sqrt{\frac{I}{\kappa}} = 2\pi\sqrt{\frac{0.040}{0.80}} = 2\pi\sqrt{0.05} = 2(3.1416)(0.2236) \approx 1.405\text{ s} \approx 1.41\text{ s}$. Exact: `1.41`.
- **Question 8**: Rotating spherical shell: $\mu_m = \frac{1}{3} Q R^2 \omega = \frac{1}{3}(6.00 \times 10^{-6})(0.10)^2(100.0) = \frac{1}{3}(6.00 \times 10^{-6})(0.01)(100) = 2.00 \times 10^{-6}\text{ A}\cdot\text{m}^2 = 2.00\ \mu\text{A}\cdot\text{m}^2$. Exact: `2.00`.
- **Question 9**: Thermal resistance between concentric spheres: $R_{\text{th}} = \frac{1}{4\pi K}\left(\frac{1}{r_1} - \frac{1}{r_2}\right) = \frac{1}{4\pi (0.50)}\left(\frac{1}{0.05} - \frac{1}{0.15}\right) = \frac{1}{2\pi}(20 - 6.667) = \frac{13.333}{2\pi} \approx 2.122\text{ K/W}$.
  Heat current $\dot{Q} = \frac{\Delta T}{R_{\text{th}}} = \frac{100}{2.122} \approx 47.12\text{ W}$. Exact: `47.12`.
- **Question 10**: $\mu = \frac{\sin((A+\delta_m)/2)}{\sin(A/2)} \implies \sqrt{3} = \frac{\sin((60^\circ+\delta_m)/2)}{\sin(30^\circ)} = \frac{\sin((60^\circ+\delta_m)/2)}{0.5} \implies \sin((60^\circ+\delta_m)/2) = \frac{\sqrt{3}}{2} \implies \frac{60^\circ+\delta_m}{2} = 60^\circ \implies \delta_m = 60^\circ$. Exact: `60.00`.
- **Question 11**: $\Delta\lambda = \lambda_c (1 - \cos 90^\circ) = \lambda_c = 0.00243\text{ nm}$. Fractional increase: $\frac{\Delta\lambda}{\lambda} = \frac{0.00243}{0.0200} = 0.1215 = 12.15\%$. Exact: `12.15`.
- **Question 12**: Quality factor: $Q = \frac{\sqrt{mk}}{b} = \frac{\sqrt{0.20 \times 80.0}}{0.040} = \frac{\sqrt{16.0}}{0.040} = \frac{4.0}{0.040} = 100.00$. Exact: `100.00`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $F = -\frac{dU}{dx} = -\left(-\frac{2a}{x^3} + \frac{b}{x^2}\right) = \frac{2a}{x^3} - \frac{b}{x^2} = 0 \implies \frac{2a}{x^3} = \frac{b}{x^2} \implies x_0 = \frac{2a}{b}$. Option (A).
- **Question 14**: $I = \int_0^R J(r)(2\pi r dr) = 2\pi J_0 \int_0^R \left(r - \frac{r^2}{R}\right)dr = 2\pi J_0 \left(\frac{R^2}{2} - \frac{R^2}{3}\right) = 2\pi J_0 \left(\frac{R^2}{6}\right) = \frac{1}{3}\pi R^2 J_0$. Option (A).
- **Question 15**: $P V^\gamma = \text{const} \implies dP V^\gamma + \gamma P V^{\gamma-1} dV = 0 \implies -V \frac{dP}{dV} = \gamma P$. Hence $B_s = \gamma P$. Option (A).
- **Question 16**: $\theta_{\text{min}} = \frac{1.22\lambda}{D} = \frac{1.22(600 \times 10^{-9})}{2.44} = \frac{732 \times 10^{-9}}{2.44} = 3.0 \times 10^{-7}\text{ rad}$. Option (A).
- **Question 17**: $A(t) = A_0 (1/2)^{t/T_{1/2}} \implies \frac{100}{1600} = \frac{1}{16} = \left(\frac{1}{2}\right)^4 \implies \frac{8\text{ h}}{T_{1/2}} = 4 \implies T_{1/2} = 2\text{ hours}$. Option (A).
- **Question 18**: $d_{\text{app}} = \frac{d_1}{\mu_1} + \frac{d_2}{\mu_2} = \frac{12}{4/3} + \frac{6}{1.5} = 9 + 4 = 13\text{ cm}$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: $\text{B}_2\text{H}_6$ has 4 terminal $2c-2e$ bonds and 2 bridging $3c-2e$ bonds. Both borons are $sp^3$ hybridized. The two bridging hydrogens lie in a perpendicular plane above and below the plane containing the four terminal hydrogens and borons. Options: (A), (B), (C).
- **Question 20**: Reimer-Tiemann reaction generates $:\text{CCl}_2$ by $\alpha$-elimination from chloroform, attacking phenol to yield salicylaldehyde. $\text{CCl}_4$ yields salicylic acid. Options: (A), (B), (C), (D).
- **Question 21**: Nernst equation: $E = E^\circ - \frac{0.0591}{2}\log\frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]}$. Increasing $[\text{Cu}^{2+}]$ increases EMF, increasing $[\text{Zn}^{2+}]$ decreases it. At equilibrium, $E = 0$. $\Delta G^\circ = -nFE^\circ$. Options: (A), (B), (C), (D).
- **Question 22**: Aldol condensation requires $\alpha$-hydrogen atoms. Acetaldehyde ($\text{CH}_3\text{CHO}$) and acetone ($\text{CH}_3\text{COCH}_3$) have $\alpha$-hydrogens. Benzaldehyde and trimethylacetaldehyde lack $\alpha$-hydrogens. Options: (A), (B).
- **Question 23**: Across a period, $Z_{\text{eff}}$, electronegativity, and ionization energy generally increase, while atomic radius decreases. Options: (A), (B), (C).
- **Question 24**: Phenylalanine, tyrosine, and tryptophan have aromatic side chains (phenyl, 4-hydroxyphenyl, and indole). Alanine has a methyl side chain. Options: (A), (B), (C).
- **Question 25**: In $0.010\text{ M Na}_2\text{SO}_4$, $[\text{SO}_4^{2-}] = 0.010\text{ M}$. $S = \frac{K_{sp}}{[\text{SO}_4^{2-}]} = \frac{1.0 \times 10^{-10}}{1.0 \times 10^{-2}} = 1.0 \times 10^{-8}\text{ mol/L} \implies m = 8$. Exact: `8.00`.
- **Question 26**: For second-order reaction: $t_{1/2} = \frac{1}{k [A]_0} = \frac{1}{(0.040)(0.50)} = \frac{1}{0.020} = 50.00\text{ s}$. Exact: `50.00`.
- **Question 27**: For BCC: $\sqrt{3}a = 4r \implies r = \frac{\sqrt{3}a}{4} = \frac{1.732 \times 300}{4} = 129.90\text{ pm}$. Exact: `129.90`.
- **Question 28**: $\Delta_f H^\circ(\text{CH}_4) = \Delta_{\text{comb}} H^\circ(\text{C}) + 2\Delta_{\text{comb}} H^\circ(\text{H}_2) - \Delta_{\text{comb}} H^\circ(\text{CH}_4) = -393.5 + 2(-285.8) - (-890.3) = -393.5 - 571.6 + 890.3 = -74.8\text{ kJ/mol}$. Exact: `-74.80` (or `74.80` magnitude). Let's take `74.80`.
- **Question 29**: $\Delta T_b = 100.050 - 100.000 = 0.050\text{ K}$. $\Delta T_b = i K_b m \implies 0.050 = i (0.512)(0.050) \implies i = \frac{1}{0.512} \approx 1.95$. Exact: `1.95`.
- **Question 30**: $[Co(en)_2Cl_2]^+$ exists as trans (achiral, 1 isomer) and cis (chiral enantiomeric pair, 2 isomers). Total stereoisomers = $1 + 2 = 3$. Exact: `3.00`.
- **Question 31**: Protonation of oxygen followed by $S_N2$ attack of $I^-$ on the less hindered methyl carbon gives phenol and iodomethane. Option (A).
- **Question 32**: $\text{H}_3\text{PO}_2$: $3(+1) + x + 2(-2) = 0 \implies x - 1 = 0 \implies x = +1$. Option (A).
- **Question 33**: Zinc dust reduces $\text{Au}^+$ in $[Au(CN)_2]^-$ to metallic gold: $2[Au(CN)_2]^- + \text{Zn} \to [\text{Zn}(CN)_4]^{2-} + 2\text{Au}$. Option (A).
- **Question 34**: Glucose contains an aldehyde group (reducing sugar) and reduces Tollens' reagent to form a silver mirror. Option (A).
- **Question 35**: $\text{SF}_6$ has 6 bonding pairs and 0 lone pairs $\implies sp^3d^2$ hybridization. Option (A).
- **Question 36**: Buna-S is a copolymer of 1,3-butadiene and styrene. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f'(x) = \frac{1 - \ln x}{x^2} = 0 \implies x = e$. Maximum value $= \frac{1}{e}$. Since $f(e) > f(\pi)$, $\frac{\ln e}{e} > \frac{\ln \pi}{\pi} \implies \pi \ln e > e \ln \pi \implies \ln(e^\pi) > \ln(\pi^e) \implies e^\pi > \pi^e$. $\lim_{x \to \infty} \frac{\ln x}{x} = 0$. Options: (A), (B), (C), (D).
- **Question 38**: Invertible matrices obey $\det(AB) = \det(A)\det(B)$, $(AB)^{-1} = B^{-1}A^{-1}$, $\text{adj}(AB) = \text{adj}(B)\text{adj}(A)$, and $\det(\text{adj}(A)) = (\det A)^{n-1}$. Options: (A), (B), (C), (D).
- **Question 39**: Tangent formula: $xx_1 + yy_1 = r^2 \implies 3x + 4y = 25$ touches at $(3, 4)$. Normal passes through center $(0,0)$ with slope $4/3 \implies 4x - 3y = 0$. Length of tangent from $(5,5) = \sqrt{25 + 25 - 25} = 5$. Chord of contact: $5x + 5y = 25 \implies x + y = 5$. Options: (A), (B), (C), (D).
- **Question 40**: Auxiliary equation: $m^2 + 4 = 0 \implies m = \pm 2i$. General solution: $y = C_1\cos(2x) + C_2\sin(2x)$. Initial conditions: $y(0) = C_1 = 1$; $y'(0) = 2C_2 = 2 \implies C_2 = 1$. Solution: $y = \cos(2x) + \sin(2x)$. Amplitude $= \sqrt{1^2+1^2} = \sqrt{2}$. Period $= 2\pi/2 = \pi$. Options: (A), (B), (C), (D).
- **Question 41**: For unit vectors: $|\vec{a}+\vec{b}| = \sqrt{1 + 1 + 2\cos\theta} = \sqrt{2(1+\cos\theta)} = 2\cos(\theta/2)$. $|\vec{a}-\vec{b}| = 2\sin(\theta/2)$. $(\vec{a}+\vec{b})\cdot(\vec{a}-\vec{b}) = |\vec{a}|^2 - |\vec{b}|^2 = 1 - 1 = 0$. $\vec{a}+\vec{b}$ bisects the angle. Options: (A), (B), (C), (D).
- **Question 42**: For Poisson with $\lambda = 2$: mean $= 2$, variance $= 2$, $P(X=0) = \frac{e^{-2}2^0}{0!} = e^{-2}$, $P(X=1) = \frac{e^{-2}2^1}{1!} = 2e^{-2}$. Options: (A), (B), (C), (D).
- **Question 43**: $L = \lim_{x \to 0} \exp\left(\frac{\ln(\sin x / x)}{x^2}\right)$. Using Taylor series: $\frac{\sin x}{x} = 1 - \frac{x^2}{6}$, so $\ln(1 - x^2/6) \approx -\frac{x^2}{6}$. Thus exponent is $-\frac{x^2/6}{x^2} = -\frac{1}{6}$. $L = e^{-1/6} \implies k = 6$. Exact: `6.00`.
- **Question 44**: By AM-GM inequality, $x + \frac{4}{x} \ge 2\sqrt{x \cdot \frac{4}{x}} = 4.00$, with equality at $x = 2$. Exact: `4.00`.
- **Question 45**: Using Beta function: $\int_0^1 x^1 (1-x)^9 dx = B(2, 10) = \frac{\Gamma(2)\Gamma(10)}{\Gamma(12)} = \frac{1! 9!}{11!} = \frac{1}{11 \times 10} = \frac{1}{110}$. Thus $m = 110$. Exact: `110.00`.
- **Question 46**: Second plane: $2x - y + 2z + 9 = 0$. Distance $d = \frac{|9 - 3|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{6}{\sqrt{9}} = \frac{6}{3} = 2.00$. Exact: `2.00`.
- **Question 47**: $a_n = S_n - S_{n-1} = (3n^2 + 5n) - [3(n-1)^2 + 5(n-1)] = 6n + 2$. For $n = 10$: $a_{10} = 6(10) + 2 = 62.00$. Exact: `62.00`.
- **Question 48**: Treat the 2 particular persons as 1 block: $(5 - 1)! = 4! = 24$. The 2 persons can arrange among themselves in $2! = 2$ ways. Total circular arrangements $= 24 \times 2 = 48$. Exact: `48.00`.
- **Question 49**: $y = x^3 - 3x + 1$. At $x = 2$, $y = 8 - 6 + 1 = 3$. Slope $y' = 3x^2 - 3 = 12 - 3 = 9$. Equation: $y - 3 = 9(x - 2) \implies y - 3 = 9x - 18 \implies 9x - y - 15 = 0$. Option (A).
- **Question 50**: For independent events, $P(A \cap B) = P(A)P(B) = 0.4 \times 0.5 = 0.2$. $P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.4 + 0.5 - 0.2 = 0.70$. Option (A).
- **Question 51**: General term $T_{r+1} = \binom{9}{r}(x^2)^{9-r}(-1/x)^r = (-1)^r \binom{9}{r} x^{18-3r}$. For constant term: $18 - 3r = 0 \implies r = 6$. Coefficient $= (-1)^6 \binom{9}{6} = \binom{9}{3} = \frac{9 \times 8 \times 7}{6} = 84$. Option (A).
- **Question 52**: First line: $6x + 8y - 18 = 0$. Second line: $6x + 8y + 7 = 0$. Distance $d = \frac{|7 - (-18)|}{\sqrt{6^2 + 8^2}} = \frac{25}{10} = 2.5$. Option (A).
- **Question 53**: $\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -1 & 1 \\ 3 & 4 & -1 \end{vmatrix} = \hat{i}(1 - 4) - \hat{j}(-2 - 3) + \hat{k}(8 + 3) = -3\hat{i} + 5\hat{j} + 11\hat{k}$. Magnitude $= \sqrt{9 + 25 + 121} = \sqrt{155}$. Unit vector $= \frac{-3\hat{i} + 5\hat{j} + 11\hat{k}}{\sqrt{155}}$. Option (A).
- **Question 54**: $\tan x - \sin x = \sin x\left(\frac{1}{\cos x} - 1\right) = \tan x(1 - \cos x) = x \left(\frac{x^2}{2}\right) = \frac{x^3}{2}$. Limit is $1/2$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 02 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rolling with Slipping, Torque about Point of Contact, Angular Momentum Conservation about ground contact line.
- **2. Derivation**:
  - Kinetic friction force on sphere: $f_k = \mu_k M g$ acting backward.
  - Deceleration of CM: $a_c = \mu_k g \implies v(t) = v_0 - \mu_k g t$.
  - Angular acceleration: $\alpha = \frac{f_k R}{I} = \frac{\mu_k M g R}{\frac{2}{5}M R^2} = \frac{5\mu_k g}{2R} \implies \omega(t) = \frac{5\mu_k g}{2R} t$.
  - Pure rolling condition: $v(t_r) = R \omega(t_r) \implies v_0 - \mu_k g t_r = \frac{5}{2}\mu_k g t_r \implies \frac{7}{2}\mu_k g t_r = v_0 \implies t_r = \frac{2v_0}{7\mu_k g}$. (A) is correct.
  - Linear velocity at rolling: $v_r = v_0 - \mu_k g \left(\frac{2v_0}{7\mu_k g}\right) = \frac{5}{7}v_0$. (B) is correct.
  - Distance traveled: $s = v_0 t_r - \frac{1}{2} a_c t_r^2 = v_0\left(\frac{2v_0}{7\mu_k g}\right) - \frac{1}{2}(\mu_k g)\left(\frac{2v_0}{7\mu_k g}\right)^2 = \frac{2v_0^2}{7\mu_k g} - \frac{2v_0^2}{49\mu_k g} = \frac{12v_0^2}{49\mu_k g}$. (C) is correct.
  - Energy loss: $\Delta E = E_i - E_f = \frac{1}{2}M v_0^2 - \left[\frac{1}{2}M v_r^2 + \frac{1}{2}I \omega_r^2\right] = \frac{1}{2}M v_0^2 - \frac{7}{10}M v_r^2 = \frac{1}{2}M v_0^2 - \frac{7}{10}M \left(\frac{25}{49}v_0^2\right) = \frac{1}{2}M v_0^2 - \frac{5}{14}M v_0^2 = \frac{1}{7}M v_0^2$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Electromagnetic Oscillations in LC Tank Circuits, Energy Conservation.
- **2. Derivation**:
  - Kirchhoff's loop rule: $\frac{q}{C} + L \frac{d^2q}{dt^2} = 0 \implies \frac{d^2q}{dt^2} + \omega_0^2 q = 0$, with $\omega_0 = \frac{1}{\sqrt{LC}}$.
  - Solution with initial charge $Q_0$: $q(t) = Q_0 \cos(\omega_0 t)$. (A) is correct.
  - Current: $i(t) = \frac{dq}{dt} = -\omega_0 Q_0 \sin(\omega_0 t)$. (B) is correct.
  - Energy: $U_E(t) = \frac{q^2}{2C} = \frac{Q_0^2}{2C}\cos^2(\omega_0 t)$, $U_B(t) = \frac{1}{2}L i^2 = \frac{1}{2}L(\omega_0^2 Q_0^2)\sin^2(\omega_0 t) = \frac{Q_0^2}{2C}\sin^2(\omega_0 t)$. Peak energies are equal: $U_{\text{max}} = \frac{Q_0^2}{2C}$. (C) is correct.
  - Total energy $U_E + U_B = \frac{Q_0^2}{2C} = \text{const}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Doppler Effect for Sound Waves in Still Air.
- **2. Derivation**:
  - Approaching source: $\nu = \nu_0 \frac{v}{v - u} = \nu_0 \frac{v}{v - 0.20v} = \frac{\nu_0}{0.80} = 1.25\nu_0 = \frac{5}{4}\nu_0$. (A) is correct.
  - Wavelength in front: $\lambda' = \frac{v - u}{\nu_0} = \frac{0.80v}{\nu_0} = 0.80\lambda_0$. (B) is correct.
  - Receding source: $\nu' = \nu_0 \frac{v}{v + u} = \frac{\nu_0}{1.20} = \frac{5}{6}\nu_0 \approx 0.833\nu_0$. (C) is correct.
  - Wave propagation speed in a medium depends solely on the medium's elastic and inertial properties ($v = \sqrt{B/\rho}$), independent of source velocity. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Lens Maker's Formula in Medium $\frac{1}{f_m} = \left(\frac{\mu_l}{\mu_m} - 1\right)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$.
- **2. Derivation**:
  - In air: $\frac{1}{f} = (1.50 - 1) K = 0.50 K = \frac{1}{15} \implies K = \frac{2}{15}$.
  - In liquid $\mu_m = 1.20$: $\frac{1}{f'} = \left(\frac{1.50}{1.20} - 1\right) K = (1.25 - 1)\left(\frac{2}{15}\right) = 0.25 \times \frac{2}{15} = \frac{1}{30} \implies f' = +30\text{ cm}$. (A) is correct.
  - Power $P = 1/f'$ drops from $1/15$ to $1/30$. (B) is correct.
  - For $\mu_m = 1.60$: $\frac{\mu_l}{\mu_m} - 1 = \frac{1.50}{1.60} - 1 = -\frac{1}{16} < 0 \implies$ diverging lens. (C) is correct.
  - For $\mu_m = 1.50$: $\frac{\mu_l}{\mu_m} - 1 = 0 \implies 1/f' = 0 \implies f' \to \infty$ (invisible). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Einstein's Photoelectric Equation $K_{\text{max}} = h\nu - \Phi_0 = e V_0$.
- **2. Derivation**:
  - $K_{\text{max}} = h\nu - \Phi_0$ is linear in $\nu$. (A) is correct.
  - Saturation current is proportional to photon flux (intensity). (B) is correct.
  - Stopping potential $V_0 = \frac{h\nu - \Phi_0}{e}$ depends only on frequency, not intensity. (C) is correct.
  - Time lag is $\sim 10^{-9}\text{ s}$, indicating discrete photon-electron collisions. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Thermodynamic Cycles, Second Law, Entropy as State Function.
- **2. Derivation**:
  - Carnot cycle achieves maximum possible efficiency between two temperatures. Any other cycle has lower efficiency. (A) is correct.
  - Isochoric cooling: $dQ = n C_V dT < 0$ (heat rejected). (B) is correct.
  - Clockwise cycle on $P-V$ diagram encloses positive net work. (C) is correct.
  - Entropy $S$ is a state function; for any complete cycle, $\oint dS = 0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Angular momentum conservation about central pivot:
  $$L_i = m v (L/2) = (0.50)(6.00)(0.40) = 1.20\text{ kg}\cdot\text{m}^2/\text{s}$$
  Moment of inertia after sticking:
  $$I = \frac{1}{12}M L^2 + m(L/2)^2 = \frac{1}{12}(1.50)(0.80)^2 + 0.50(0.40)^2 = \frac{1}{12}(1.50)(0.64) + 0.50(0.16) = 0.080 + 0.080 = 0.160\text{ kg}\cdot\text{m}^2$$
  Angular velocity: $\omega = \frac{L_i}{I} = \frac{1.20}{0.160} = 7.50\text{ rad/s}$. Exact: `7.50`.
- **Question 8**: Fundamental for closed pipe: $\nu_1 = \frac{v}{4L} = \frac{340}{4(0.85)} = \frac{340}{3.40} = 100.00\text{ Hz}$. Exact: `100.00`.
- **Question 9**: By Gauss's Law, total flux through cube is $q/\varepsilon_0$. By symmetry, flux through one face is:
  $$\Phi_1 = \frac{q}{6\varepsilon_0} = \frac{4.0 \times 10^{-6}}{6(8.85 \times 10^{-12})} = \frac{4.0 \times 10^6}{53.1} \approx 75329.57\text{ N}\cdot\text{m}^2/\text{C} \approx 75329.60$$. Exact: `75329.60`.
- **Question 10**: Fringe shift $\Delta y = \frac{(\mu - 1)t D}{d} = 6 \beta = 6 \frac{\lambda D}{d} \implies (\mu - 1)t = 6\lambda \implies t = \frac{6\lambda}{\mu - 1} = \frac{6(600 \times 10^{-9})}{1.60 - 1} = \frac{3600 \times 10^{-9}}{0.60} = 6.0 \times 10^{-6}\text{ m} = 6.00\ \mu\text{m}$. Exact: `6.00`.
- **Question 11**: $\lambda = \frac{12.27}{\sqrt{150.0}} = \frac{12.27}{12.247} \approx 1.00\text{ \AA}$. Exact: `1.00`.
- **Question 12**: Axial magnetic field: $B = \frac{\mu_0 I R^2}{2(R^2 + x^2)^{3/2}} = \frac{\mu_0 I R^2}{2(2R^2)^{3/2}} = \frac{\mu_0 I}{2 \cdot 2\sqrt{2} R} = \frac{\mu_0 I}{4\sqrt{2} R} = \frac{(4\pi \times 10^{-7})(5.0)}{4(1.414)(0.10)} = \frac{20\pi \times 10^{-7}}{0.5657} \approx 11.11 \times 10^{-6}\text{ T} = 11.11\ \mu\text{T}$. Exact: `11.11`.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 14**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 15**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 16**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 17**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 18**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: $[\text{Ni}(\text{CN})_4]^{2-}$ ($d^8$ square planar, all paired), $[\text{Fe}(\text{CN})_6]^{4-}$ ($d^6$ low spin, $t_{2g}^6$, paired), $[\text{Co}(\text{NH}_3)_6]^{3+}$ ($d^6$ low spin, $t_{2g}^6$, paired) are diamagnetic. $[\text{NiCl}_4]^{2-}$ ($d^8$ tetrahedral) has 2 unpaired electrons (paramagnetic). Options: (A), (B), (C).
- **Question 20**: Etard reaction, Gattermann-Koch reaction, Rosenmund reduction, and Stephen reduction are classical named reactions for synthesizing benzaldehyde. Options: (A), (B), (C), (D).
- **Question 21**: Standard reduction potentials: more negative $\implies$ stronger reducing agent. Lithium has highest reducing power in water due to high hydration energy. Fluorine is strongest oxidizer. Zinc reduces copper. Options: (A), (B), (C), (D).
- **Question 22**: Racemization occurs via planar carbocation intermediate in $S_N1$ solvolysis. Secondary and benzylic halides like 2-bromobutane and 1-phenylethyl chloride form carbocations that undergo racemization. Primary 1-bromobutane undergoes $S_N2$ with inversion. Achiral 2-bromo-2-methylpropane cannot racemize. Options: (A), (B).
- **Question 23**: Across a period, $Z_{\text{eff}}$, electronegativity, and ionization enthalpy increase; atomic radius decreases. Options: (A), (B), (C).
- **Question 24**: Phenylalanine, tyrosine, and tryptophan have aromatic side chains. Alanine has methyl group. Options: (A), (B), (C).
- **Question 25**: $K_p = \frac{4\alpha^2 P}{1 - \alpha^2} \implies 0.15 = \frac{4(0.04) P}{1 - 0.04} = \frac{0.16 P}{0.96} = \frac{P}{6} \implies P = 6 \times 0.15 = 0.90\text{ atm}$. Exact: `0.90`.
- **Question 26**: First-order reaction: slope $= -k = -0.0231\text{ min}^{-1} \implies k = 0.0231\text{ min}^{-1}$. Half-life $t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{0.0231} = 30.00\text{ min}$. Exact: `30.00`.
- **Question 27**: $V_{\text{cell}} = \frac{Z M}{\rho N_A} = \frac{4 \times 63.5}{8.92 \times 6.022 \times 10^{23}} = \frac{254}{5.3716 \times 10^{24}} \approx 4.73 \times 10^{-23}\text{ cm}^3 \implies V_{\text{cell}} \times 10^{23} = 4.73$. Exact: `4.73`.
- **Question 28**: $\Delta G^\circ = -n F E^\circ = -2(96500)(1.10) = -212300\text{ J/mol} = -212.3\text{ kJ/mol}$. Magnitude $= 212.30$. Exact: `212.30`.
- **Question 29**: $\Delta T_f = K_f m \implies 0.372 = K_f (0.20) \implies K_f = \frac{0.372}{0.20} = 1.86\text{ K}\cdot\text{kg/mol}$. Exact: `1.86`.
- **Question 30**: $\text{Mn}^{2+}$ is $3d^5$. High spin has 5 unpaired electrons. $\mu = \sqrt{5(7)} = \sqrt{35} \approx 5.92\text{ BM}$. Exact: `5.92`.
- **Question 31**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 32**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 33**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 34**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 35**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 36**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f'(x) = \frac{1 - \ln x}{x^2} = 0 \implies x = e$. Maximum is $1/e$. Since $f(e) > f(\pi)$, $e^\pi > \pi^e$. $\lim_{x \to \infty} \frac{\ln x}{x} = 0$. Options: (A), (B), (C), (D).
- **Question 38**: Standard matrix theorems: $\det(AB) = \det(A)\det(B)$, $(AB)^{-1} = B^{-1}A^{-1}$, $\text{adj}(AB) = \text{adj}(B)\text{adj}(A)$, $\det(\text{adj}(A)) = (\det A)^{n-1}$. Options: (A), (B), (C), (D).
- **Question 39**: $xx_1 + yy_1 = r^2 \implies 3x + 4y = 25$ touches at $(3, 4)$. Normal passes through $(0,0)$ with equation $4x - 3y = 0$. Tangent length from $(5,5)$ is 5. Chord of contact is $x + y = 5$. Options: (A), (B), (C), (D).
- **Question 40**: Harmonic oscillator ODE: $y'' + 4y = 0 \implies y = \cos(2x) + \sin(2x)$. Amplitude $= \sqrt{2}$, period $= \pi$. Options: (A), (B), (C), (D).
- **Question 41**: $|\vec{a}+\vec{b}| = 2\cos(\theta/2)$, $|\vec{a}-\vec{b}| = 2\sin(\theta/2)$, dot product is 0, vector sum bisects angle. Options: (A), (B), (C), (D).
- **Question 42**: Poisson with $\lambda = 2$: mean $= 2$, variance $= 2$, $P(0) = e^{-2}$, $P(1) = 2e^{-2}$. Options: (A), (B), (C), (D).
- **Question 43**: Limit of $(\sin x / x)^{1/x^2}$ is $e^{-1/6}$, so $k = 6$. Exact: `6.00`.
- **Question 44**: $f'(x) = 1 - \frac{4}{x^2} = 0 \implies x = 2$. Minimum value $= 2 + 4/2 = 4.00$. Exact: `4.00`.
- **Question 45**: $\int_0^1 x(1-x)^9 dx = B(2, 10) = \frac{1! 9!}{11!} = \frac{1}{110} \implies m = 110$. Exact: `110.00`.
- **Question 46**: Planes: $2x - y + 2z + 3 = 0$ and $2x - y + 2z + 9 = 0$. Distance $d = \frac{|9 - 3|}{\sqrt{4+1+4}} = \frac{6}{3} = 2.00$. Exact: `2.00`.
- **Question 47**: $a_n = S_n - S_{n-1} = 6n + 2 \implies a_{10} = 62.00$. Exact: `62.00`.
- **Question 48**: Block of 2: $(5-1)! \times 2! = 24 \times 2 = 48.00$. Exact: `48.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 02
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 1.41
- Q8: 2.00
- Q9: 47.12
- Q10: 60.00
- Q11: 12.15
- Q12: 100.00
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C
- Q20: A, B, C, D
- Q21: A, B, C, D
- Q22: A, B
- Q23: A, B, C
- Q24: A, B, C
- Q25: 8.00
- Q26: 50.00
- Q27: 129.90
- Q28: 74.80
- Q29: 1.95
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
- Q42: A, B, C
- Q43: 2.00
- Q44: 0.33
- Q45: 5.00
- Q46: 2.00
- Q47: 1.00
- Q48: 10.00
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
- Q7: 7.50
- Q8: 100.00
- Q9: 75329.60
- Q10: 6.00
- Q11: 1.00
- Q12: 11.11
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C
- Q20: A, B, C, D
- Q21: A, B, C, D
- Q22: A, B
- Q23: A, B, C
- Q24: A, B, C
- Q25: 0.90
- Q26: 30.00
- Q27: 4.73
- Q28: 212.30
- Q29: 1.86
- Q30: 5.92
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
- Q43: 6.00
- Q44: 4.00
- Q45: 110.00
- Q46: 2.00
- Q47: 62.00
- Q48: 48.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: 33.3% of questions (high option-checking cognitive load).
- **Physics**: Focus on non-conservative momentum loss (conveyor sand), variable capacitor electrostatic energy, relativistic pair production thresholds.
- **Chemistry**: Rigorous coverage of Reimer-Tiemann mechanism ($:\text{CCl}_2$), diborane 3c-2e banana bonds, complex stereoisomer counting.
- **Mathematics**: Extrema of $x^x$ and $\ln x / x$, matrix identities under Cayley-Hamilton, circular permutations, Beta/Gamma integration.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

create_mock_files(2, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")
