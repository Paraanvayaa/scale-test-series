"""
IIT Madras Mocks 06 to 10 Generator
Organising Institute: Indian Institute of Technology Madras
Empirical Benchmark: 2010, 2017, 2024 Official JEE Advanced Papers
Features:
- Electromagnetism dominance (>= 37% of physics: induction, radiation, Poynting vectors, coupled inductors)
- Single-correct traps and speed/precision tests
- Physical chemistry dominance: phase equilibria, electrochemistry, ionic equilibria, thermodynamics
- Mathematics: Argand plane loci, conics invariants, vector triple products, definite integrals
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_madras_06_to_10():
    for mock_idx in range(6, 11):
        pad = f"{mock_idx:02d}"
        ind_l = str(0.15 + (mock_idx % 4) * 0.03)
        mag_b = str(0.60 + (mock_idx % 3) * 0.12)
        volt_v = str(24.0 + mock_idx * 2.0)
        ang_w = str(70 + mock_idx * 10)

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
A coaxial transmission line of length $L$ consists of an inner solid cylinder of radius $a$ carrying uniform axial current $I_0(t) = I_0 \sin(\omega t)$ and a thin concentric outer cylindrical shell of radius $b$ carrying the return current $-I_0(t)$:
(A) The magnetic field in the region $a < r < b$ is $B(r, t) = \frac{\mu_0 I_0 \sin(\omega t)}{2\pi r}$.  
(B) The induced electric field tangential to the cylinders in $a < r < b$ satisfies $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi}{dt}$.  
(C) The self-inductance per unit length of this coaxial cable is $\frac{\mu_0}{2\pi}\ln\left(\frac{b}{a}\right) + \frac{\mu_0}{8\pi}$ (including internal inductance).  
(D) The Poynting vector in the dielectric gap $a < r < b$ points parallel to the cable axis in the direction of energy propagation.

#### Question 2
A square conducting loop of side $w$ and total mass $M$ with electrical resistance $R$ enters a region of uniform magnetic field $B_0\hat{k}$ oriented perpendicular to the loop plane with initial velocity $v_0\hat{i}$:
(A) While entering the field, the magnetic retarding force on the loop is $F = -\frac{B_0^2 w^2 v}{R}$.  
(B) The velocity of the loop decreases exponentially as $v(t) = v_0 e^{-\alpha t}$ where $\alpha = \frac{B_0^2 w^2}{MR}$.  
(C) The total distance traversed by the loop before coming to rest (assuming the field region is sufficiently wide) is $x_{\max} = \frac{M v_0 R}{B_0^2 w^2}$.  
(D) The total electrical energy dissipated in the loop during deceleration is precisely equal to the initial kinetic energy $\frac{1}{2}M v_0^2$.

#### Question 3
A plane electromagnetic wave propagates in free space with electric field $\vec{E} = E_0 \cos(kz - \omega t)\hat{i}$. It reflects normally from an ideal plane mirror located at $z = 0$:
(A) The reflected electric field is $\vec{E}_r = -E_0 \cos(kz + \omega t)\hat{i}$.  
(B) A standing wave is formed with nodes of electric field at $z = -n\frac{\lambda}{2}$ ($n = 0, 1, 2, \dots$).  
(C) Antinodes of magnetic field occur at the positions of electric field nodes.  
(D) The time-averaged Poynting vector of the resulting standing wave is identically zero everywhere.

#### Question 4
Two mutually coupled inductors have self-inductances $L_1$ and $L_2$, with mutual inductance $M = k\sqrt{L_1 L_2}$ where $0 < k \le 1$. They are connected in parallel such that their magnetic fluxes aid each other:
(A) The equivalent inductance of the parallel combination is $L_{\text{eq}} = \frac{L_1 L_2 - M^2}{L_1 + L_2 - 2M}$.  
(B) If $k = 1$ and $L_1 = L_2 = L$, the equivalent inductance is $L_{\text{eq}} = L$.  
(C) The energy stored in the magnetic field at any instant is $U = \frac{1}{2}L_1 i_1^2 + \frac{1}{2}L_2 i_2^2 + M i_1 i_2$.  
(D) If the windings are reversed to oppose each other, $L_{\text{eq}} = \frac{L_1 L_2 - M^2}{L_1 + L_2 + 2M}$.

#### Question 5
In an experiment with a cylindrical laser beam of power $P_0$ and radius $r_0$ striking a perfectly reflecting cone of half-angle $\alpha$ along its axis of symmetry:
(A) The momentum delivered per unit time to the cone depends on the half-angle $\alpha$.  
(B) The net force exerted on the cone along its axis is $F = \frac{2P_0}{c}\sin^2\alpha$.  
(C) If the cone is replaced by a flat disc perpendicular to the beam, the force is $F = \frac{2P_0}{c}$.  
(D) The radiation pressure is uniform over the conical surface.

#### Question 6
An ideal gas undergoes a cycle on the $T-S$ (Temperature-Entropy) plane consisting of two isothermal processes at temperatures $T_H$ and $T_C$ ($T_H > T_C$) and two isentropic (reversible adiabatic) processes between entropies $S_1$ and $S_2$ ($S_2 > S_1$):
(A) The cycle represents a reversible Carnot engine operating between $T_H$ and $T_C$.  
(B) The net work done per cycle is equal to the area of the rectangle in the $T-S$ plane: $W = (T_H - T_C)(S_2 - S_1)$.  
(C) The efficiency of this heat engine is $\eta = 1 - \frac{T_C}{T_H}$.  
(D) The heat absorbed from the high-temperature reservoir is $Q_H = T_H (S_2 - S_1)$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A long straight solenoid of radius $R = 0.10\text{ m}$ has $n = 1000\text{ turns/m}$ and carries a time-dependent current $I(t) = 4.0 t\text{ A}$. The induced electric field at a radial distance $r = 0.05\text{ m}$ from the central axis at $t = 2.0\text{ s}$ is $E \times 10^{-4}\text{ V/m}$. Taking $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$, evaluate $E$ rounded off to two decimal places.

#### Question 8
A parallel-plate capacitor of capacitance $C_0 = 10.0\text{ }\mu\text{F}$ is charged to voltage $V_0 = 100.0\text{ V}$ and disconnected from the battery. A dielectric slab of dielectric constant $\kappa = 4.0$ filling half the plate area is inserted. The work done by the electrostatic force on the slab during insertion is $W\text{ mJ}$. Find $W$.

#### Question 9
In a series $RLC$ circuit driven by an AC voltage source of amplitude $V_0 = 220\text{ V}$ at resonance frequency $\omega_0 = 1000\text{ rad/s}$, the values are $R = 10\text{ }\Omega$, $L = 0.10\text{ H}$, and $C = 10\text{ }\mu\text{F}$. The voltage amplitude across the inductor at resonance is $V_L\text{ V}$. Find $V_L$.

#### Question 10
A circular ring of mass $m = 0.50\text{ kg}$ and radius $r = 0.20\text{ m}$ having total charge $Q = 2.0\text{ C}$ is placed in a horizontal plane. A uniform magnetic field perpendicular to the ring plane increases at a constant rate $\frac{dB}{dt} = 5.0\text{ T/s}$. The angular acceleration of the ring is $\alpha\text{ rad/s}^2$. Find $\alpha$.

#### Question 11
A light ray is incident at Brewster's angle on a glass slab of refractive index $n = \sqrt{3}$. The angle of refraction inside the glass slab is $\theta_r$ in degrees. Find $\theta_r$.

#### Question 12
A thermodynamic system containing $1\text{ mole}$ of a monoatomic ideal gas expands quasi-statically such that its molar heat capacity varies as $C = C_V + 2RT$. The gas temperature rises from $T_1 = 300\text{ K}$ to $T_2 = 400\text{ K}$. If the total heat supplied to the gas is $Q = k R$, find the value of $k$.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
An infinite flat sheet lying in the $xy$-plane carries a uniform surface current density $\vec{K} = K_0 \hat{i}$. The magnetic field $\vec{B}$ at a point $(0, 0, z)$ with $z > 0$ is:
(A) $\frac{\mu_0 K_0}{2}\hat{j}$  
(B) $-\frac{\mu_0 K_0}{2}\hat{j}$  
(C) $\frac{\mu_0 K_0}{2}\hat{k}$  
(D) $-\frac{\mu_0 K_0}{2}\hat{i}$

#### Question 14
A spherical conducting shell of inner radius $R_1$ and outer radius $R_2$ contains a point charge $q$ placed at an eccentric point at distance $d < R_1$ from the center $O$:
(A) The surface charge density on the inner surface of the shell is uniform.  
(B) The surface charge density on the outer surface of the shell is uniform.  
(C) The electric field at any point outside the shell ($r > R_2$) depends on $d$.  
(D) The potential at the center $O$ is $\frac{q}{4\pi\varepsilon_0}\left(\frac{1}{d} - \frac{1}{R_1} + \frac{1}{R_2}\right)$.

#### Question 15
Two inductors of inductances $L_1 = 4\text{ H}$ and $L_2 = 9\text{ H}$ are perfectly coupled ($k = 1$). The mutual inductance $M$ between them is:
(A) $4\text{ H}$  
(B) $6\text{ H}$  
(C) $9\text{ H}$  
(D) $13\text{ H}$

#### Question 16
A particle of mass $m$ and charge $q$ is launched with velocity $\vec{v} = v_0 \hat{i}$ into a region with crossed fields $\vec{E} = E_0 \hat{j}$ and $\vec{B} = B_0 \hat{k}$. If $v_0 = E_0 / B_0$, the trajectory of the particle is:
(A) A straight line along the $x$-axis  
(B) A cycloid in the $xy$-plane  
(C) A helix along the $z$-axis  
(D) A parabola in the $xy$-plane

#### Question 17
A Carnot refrigerator operates between reservoirs at $T_C = 250\text{ K}$ and $T_H = 300\text{ K}$. Its coefficient of performance ($\beta$) is:
(A) $5.0$  
(B) $6.0$  
(C) $0.83$  
(D) $1.2$

#### Question 18
A parallel beam of unpolarized light passes successively through two ideal polarizers whose transmission axes are oriented at an angle of $60^\circ$ with respect to each other. If the incident beam has intensity $I_0$, the transmitted intensity is:
(A) $I_0 / 2$  
(B) $I_0 / 4$  
(C) $I_0 / 8$  
(D) $3I_0 / 8$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an electrochemical cell: $\text{Pt}(s) \mid \text{H}_2(g, 1\text{ bar}) \mid \text{H}^+(aq, 1\text{ M}) \parallel \text{Fe}^{3+}(aq), \text{Fe}^{2+}(aq) \mid \text{Pt}(s)$ with standard reduction potentials $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V}$:
(A) The cell reaction is $\frac{1}{2}\text{H}_2(g) + \text{Fe}^{3+}(aq) \rightleftharpoons \text{H}^+(aq) + \text{Fe}^{2+}(aq)$.  
(B) The standard cell EMF is $E^\circ_{\text{cell}} = +0.77\text{ V}$.  
(C) Increasing the concentration of $\text{Fe}^{2+}$ decreases the cell potential $E_{\text{cell}}$.  
(D) At $298\text{ K}$, $\Delta G^\circ = -nFE^\circ_{\text{cell}} = -74.3\text{ kJ/mol}$.

#### Question 20
Regarding the thermodynamics of ideal and non-ideal liquid solutions:
(A) For an ideal solution, $\Delta_{\text{mix}}H = 0$ and $\Delta_{\text{mix}}V = 0$.  
(B) For an ideal solution, $\Delta_{\text{mix}}S = -R\sum x_i \ln x_i > 0$.  
(C) A solution showing positive deviation from Raoult's law forms a minimum boiling azeotrope.  
(D) For an azeotropic mixture, the vapor phase and liquid phase compositions are identical at the boiling point.

#### Question 21
Consider the coordination complex $[Co(NH_3)_4 Cl_2]^+$; which of the following statements is(are) TRUE:
(A) It exhibits geometrical isomerism: *cis* and *trans* forms.  
(B) The *cis* isomer is optically active because it lacks an inversion center and plane of symmetry.  
(C) The *trans* isomer is optically inactive with a center of symmetry.  
(D) Both isomers are low-spin diamagnetic complexes ($d^6, t_{2g}^6$).

#### Question 22
Regarding the chemistry of transition metals and coordination compounds:
(A) $\text{KMnO}_4$ acts as a self-indicator in redox titrations in acidic medium.  
(B) The intense purple color of $\text{MnO}_4^-$ arises from ligand-to-metal charge transfer (LMCT).  
(C) In $\text{Cr}_2\text{O}_7^{2-}$, the two chromium atoms are linked by a bridging oxygen atom with $\text{Cr}-\text{O}-\text{Cr}$ bond angle of approximately $126^\circ$.  
(D) $\text{MnO}_4^{2-}$ (manganate) is paramagnetic with one unpaired electron.

#### Question 23
In the aldol condensation of acetaldehyde ($\text{CH}_3\text{CHO}$) in dilute aqueous $\text{NaOH}$:
(A) The rate-determining step in base-catalyzed enolization is the abstraction of an $\alpha$-proton.  
(B) The intermediate is an enolate resonance-stabilized carbanion.  
(C) Dehydration of 3-hydroxybutanal gives but-2-enal via an E1cB mechanism.  
(D) The reaction is reversible and the position of equilibrium favors the aldol addition product at low temperatures.

#### Question 24
Which of the following statements about nucleic acids and amino acids is/are CORRECT:
(A) DNA contains 2-deoxy-D-ribose, whereas RNA contains D-ribose.  
(B) Adenine pairs with thymine via two hydrogen bonds in double-stranded DNA.  
(C) Guanine pairs with cytosine via three hydrogen bonds.  
(D) All standard proteinogenic amino acids except glycine possess a chiral $\alpha$-carbon atom with L-configuration.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{Ag}_2\text{CrO}_4$ in pure water at $298\text{ K}$ is $K_{\text{sp}} = 1.08 \times 10^{-12}$. The molar solubility of $\text{Ag}_2\text{CrO}_4$ in pure water is $S \times 10^{-4}\text{ M}$. Find the value of $S$ rounded off to two decimal places.

#### Question 26
For the first-order reaction $A \to \text{Products}$, the half-life is $t_{1/2} = 30.0\text{ min}$. The time required for $87.5\%$ of reactant $A$ to decompose is $t\text{ min}$. Find $t$.

#### Question 27
The standard reduction potential of the Daniel cell is $E^\circ = 1.10\text{ V}$ at $298\text{ K}$. The equilibrium constant for the reaction $\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightleftharpoons \text{Zn}^{2+}(aq) + \text{Cu}(s)$ is written as $10^K$ where $K = \frac{2 \times 1.10}{0.0591}$. Find $K$ rounded off to two decimal places.

#### Question 28
The freezing point of a $0.10\text{ m}$ aqueous solution of a weak monobasic acid $\text{HA}$ is $-0.2046^\circ\text{C}$. Given $K_f(\text{H}_2\text{O}) = 1.86\text{ K kg mol}^{-1}$, the degree of dissociation $\alpha$ of the acid is $\alpha\%$. Find $\alpha$ as a percentage.

#### Question 29
A coordination compound has the empirical formula $\text{CoCl}_3 \cdot 5\text{NH}_3$. When $1\text{ mole}$ of this complex is treated with excess $\text{AgNO}_3(aq)$, $2\text{ moles}$ of $\text{AgCl}$ are precipitated immediately. The coordination number of cobalt in this complex is $N$. Find $N$.

#### Question 30
In the complete combustion of $1\text{ mole}$ of liquid benzene ($\text{C}_6\text{H}_6$) at $298\text{ K}$, the change in the number of moles of gas, $\Delta n_g$, is $x$. Find $|x|$ rounded off to one decimal place.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The IUPAC name of the complex $[\text{Pt}(\text{NH}_3)_2 \text{Cl}(\text{NO}_2)]$ is:
(A) Diamminechloridonitrito-N-platinum(II)  
(B) Diamminechloronitroplatinum(II)  
(C) Diamminedichloridoplatinum(II)  
(D) Platinum(II) diamminechloronitrite

#### Question 32
Which of the following pairs represents functional isomers:
(A) Ethanol and Dimethyl ether  
(B) Propan-1-ol and Propan-2-ol  
(C) Pentan-2-one and Pentan-3-one  
(D) But-1-ene and But-2-ene

#### Question 33
In the extraction of silver from its ore using the cyanide process (MacArthur-Forrest process), the oxidizing agent used to oxidize native silver is:
(A) Atmospheric oxygen $\text{O}_2$  
(B) Zinc dust  
(C) Sodium cyanide  
(D) Carbon monoxide

#### Question 34
The molar conductivity of a $0.01\text{ M}$ solution of an electrolyte is $\Lambda_m = 120\text{ S cm}^2\text{mol}^{-1}$. The specific conductivity $\kappa$ in $\text{S cm}^{-1}$ is:
(A) $1.2 \times 10^{-3}$  
(B) $1.2 \times 10^{-2}$  
(C) $1.2 \times 10^{-4}$  
(D) $1.20$

#### Question 35
Which of the following carbocations is the MOST stable:
(A) Tropylium cation ($\text{C}_7\text{H}_7^+$)  
(B) Benzyl cation ($\text{C}_6\text{H}_5\text{CH}_2^+$)  
(C) Allyl cation ($\text{CH}_2=\text{CH}-\text{CH}_2^+$)  
(D) *tert*-Butyl cation ($(\text{CH}_3)_3\text{C}^+$)

#### Question 36
The enthalpy of atomization of $\text{CH}_4(g)$ is $1665\text{ kJ/mol}$. The average $\text{C}-\text{H}$ bond enthalpy in methane is:
(A) $416.25\text{ kJ/mol}$  
(B) $555.0\text{ kJ/mol}$  
(C) $832.5\text{ kJ/mol}$  
(D) $1665.0\text{ kJ/mol}$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{\ln x}{x}$ defined on $(0, \infty)$:
(A) $f(x)$ is strictly increasing on $(0, e)$ and strictly decreasing on $(e, \infty)$.  
(B) The absolute maximum value of $f(x)$ is $\frac{1}{e}$ attained at $x = e$.  
(C) $e^\pi > \pi^e$.  
(D) The equation $f(x) = c$ has exactly two distinct positive solutions for all $c \in (0, 1/e)$.

#### Question 38
Let $A$ be a $3 \times 3$ real skew-symmetric matrix:
(A) $\det(A) = 0$.  
(B) All non-zero eigenvalues of $A$ are purely imaginary.  
(C) $I_3 + A$ is invertible.  
(D) $(I_3 - A)(I_3 + A)^{-1}$ is an orthogonal matrix (Cayley transform).

#### Question 39
Consider the system of vectors $\vec{a}, \vec{b}, \vec{c}$ in $\mathbb{R}^3$ such that $|\vec{a}| = 1, |\vec{b}| = 2, |\vec{c}| = 3$, and $\vec{a} \times (\vec{b} \times \vec{c}) = \frac{1}{2}\vec{b}$:
(A) $\vec{a} \cdot \vec{c} = \frac{1}{2}$ and $\vec{a} \cdot \vec{b} = 0$.  
(B) The angle between $\vec{a}$ and $\vec{c}$ is $\arccos\left(\frac{1}{6}\right)$.  
(C) $\vec{a}$ is perpendicular to $\vec{b}$.  
(D) The scalar triple product $[\vec{a}\text{ }\vec{b}\text{ }\vec{c}]$ can be evaluated once the angle between $\vec{b}$ and $\vec{c}$ is known.

#### Question 40
Let $I_n = \int_0^1 (1 - x^2)^n dx$ for $n \ge 0$:
(A) $I_n = \frac{2n}{2n+1} I_{n-1}$ for $n \ge 1$.  
(B) $I_0 = 1$.  
(C) $I_1 = 2/3$.  
(D) $\lim_{n \to \infty} \sqrt{n} I_n = \frac{\sqrt{\pi}}{2}$.

#### Question 41
Let $z$ be a complex number satisfying $|z - 3 - 4i| \le 2$:
(A) The maximum value of $|z|$ is $7$.  
(B) The minimum value of $|z|$ is $3$.  
(C) The maximum value of $\arg(z)$ corresponds to the tangent drawn from the origin to the circle.  
(D) The locus of $z$ represents a closed disc in the complex plane centered at $(3, 4)$ with radius $2$.

#### Question 42
Consider the parabola $y^2 = 4ax$ and a chord $AB$ passing through its focus $S(a, 0)$:
(A) If the focal chord makes an angle $\theta$ with the axis of the parabola, its length is $4a\csc^2\theta$.  
(B) The circle described on $AB$ as diameter touches the directrix $x = -a$.  
(C) The tangents to the parabola at $A$ and $B$ intersect at right angles on the directrix.  
(D) The semi-latus rectum $2a$ is the harmonic mean of the focal segments $SA$ and $SB$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral $I = \int_0^{\pi/2} \frac{\sin^3 x}{\sin^3 x + \cos^3 x} dx$. If $I = \frac{\pi}{k}$, find the value of $k$.

#### Question 44
Find the number of integral values of $k$ for which the quadratic equation $(k-2)x^2 + 8x + (k+4) = 0$ has real and distinct roots of opposite signs.

#### Question 45
Let $S$ be the sum of the series $\sum_{n=1}^\infty \frac{n}{2^n}$. Find the value of $S$.

#### Question 46
Let the line $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ intersect the plane $2x + 3y - z = 5$ at point $P(x_0, y_0, z_0)$. Find the value of $x_0 + y_0 + z_0$.

#### Question 47
A bag contains 4 red balls and 6 black balls. Three balls are drawn at random without replacement. If the probability that all three drawn balls are of the same color is $P = \frac{m}{n}$ in lowest terms, find $m + n$.

#### Question 48
Find the radius of the sphere passing through the four points $(0,0,0), (2,0,0), (0,4,0),$ and $(0,0,6)$. Round off the squared radius $R^2$ to the nearest integer.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The value of $\lim_{x \to 0} \frac{e^{x^2} - \cos x}{x^2}$ is:
(A) $1/2$  
(B) $1$  
(C) $3/2$  
(D) $2$

#### Question 50
If $y = y(x)$ satisfies the differential equation $\frac{dy}{dx} + y\tan x = \sec x$ with initial condition $y(0) = 0$, then $y(\pi/4)$ is:
(A) $1$  
(B) $\sqrt{2} - 1$  
(C) $\frac{1}{\sqrt{2}}$  
(D) $\sqrt{2}$

#### Question 51
The eccentricity of the hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$ is:
(A) $4/3$  
(B) $5/4$  
(C) $5/3$  
(D) $\sqrt{7}/4$

#### Question 52
The number of distinct arrangements of the letters of the word **MATHEMATICS** in which vowels always appear together is:
(A) 120960  
(B) 60480  
(C) 30240  
(D) 15120

#### Question 53
If $\sin\alpha + \sin\beta = a$ and $\cos\alpha + \cos\beta = b$, then $\cos(\alpha - \beta)$ is:
(A) $\frac{a^2 + b^2 - 2}{2}$  
(B) $\frac{a^2 + b^2 + 2}{2}$  
(C) $\frac{a^2 - b^2}{2}$  
(D) $\frac{a^2 + b^2}{2}$

#### Question 54
Let $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$. Then $A^{10}$ is equal to:
(A) $\begin{pmatrix} 1 & 20 \\ 0 & 1 \end{pmatrix}$  
(B) $\begin{pmatrix} 1 & 1024 \\ 0 & 1 \end{pmatrix}$  
(C) $\begin{pmatrix} 1 & 2^{10} \\ 0 & 1 \end{pmatrix}$  
(D) $\begin{pmatrix} 10 & 20 \\ 0 & 10 \end{pmatrix}$
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
A charged particle of mass $m$ and charge $q$ moves in a region of space where both a uniform electric field $\vec{E} = E_0\hat{k}$ and a uniform magnetic field $\vec{B} = B_0\hat{k}$ exist parallel to each other:
(A) The motion along the $z$-axis is uniformly accelerated with acceleration $a_z = qE_0/m$.  
(B) The motion projected onto the $xy$-plane is uniform circular motion with cyclotron angular frequency $\omega_c = qB_0/m$.  
(C) The pitch of the helical trajectory increases linearly with time: $p(t) = \frac{2\pi m}{qB_0}(v_{0z} + a_z t)$.  
(D) The total kinetic energy of the particle increases monotonically with time if $v_{0z} \ge 0$.

#### Question 2
A dielectric sphere of radius $R$ carries a frozen-in uniform polarization $\vec{P} = P_0\hat{k}$:
(A) The bound surface charge density is $\sigma_b = P_0 \cos\theta$.  
(B) The bound volume charge density is $\rho_b = 0$ everywhere inside the sphere.  
(C) The electric field inside the sphere is uniform and given by $\vec{E}_{\text{in}} = -\frac{\vec{P}}{3\varepsilon_0}$.  
(D) The total dipole moment of the sphere is $\vec{p} = \frac{4}{3}\pi R^3 P_0 \hat{k}$.

#### Question 3
An AC source of EMF $\mathcal{E}(t) = V_0 \cos(\omega t)$ drives a circuit containing a series combination of resistance $R$ and inductor $L$ connected in parallel with a capacitor $C$:
(A) The admittance of the parallel combination is $Y = \frac{1}{R + j\omega L} + j\omega C$.  
(B) Resonance (unity power factor) occurs when $\omega = \sqrt{\frac{1}{LC} - \frac{R^2}{L^2}}$.  
(C) At resonance, the dynamic impedance of this parallel circuit is $Z_{\text{dyn}} = \frac{L}{CR}$.  
(D) The total current supplied by the source at anti-resonance is at a local minimum.

#### Question 4
A thin uniform metallic bar of mass $m$, length $L$, and electrical resistance $R$ slides without friction down two parallel inclined conducting rails separated by distance $L$, inclined at angle $\theta$ to the horizontal. A uniform magnetic field $B$ acts vertically upward:
(A) The component of magnetic field perpendicular to the inclined plane is $B\cos\theta$.  
(B) The induced EMF in the bar when moving at speed $v$ is $\mathcal{E} = B L v \cos\theta$.  
(C) The magnetic retarding force along the incline is $F_{\text{mag}} = \frac{B^2 L^2 v \cos^2\theta}{R}$.  
(D) The terminal velocity of the bar is $v_t = \frac{m g R \sin\theta}{B^2 L^2 \cos^2\theta}$.

#### Question 5
In an optical Young's double-slit apparatus with slit separation $d$ and screen distance $D$, a thin transparent mica sheet of thickness $t$ and refractive index $\mu$ is placed in front of the upper slit:
(A) The optical path through the upper slit increases by $(\mu - 1)t$.  
(B) The entire fringe pattern shifts upward by $\Delta y = \frac{D}{d}(\mu - 1)t$.  
(C) The fringe width $\beta = \frac{\lambda D}{d}$ remains completely unchanged.  
(D) If $\Delta y$ equals 5 fringe widths, the optical path difference introduced is $5\lambda$.

#### Question 6
One mole of an ideal diatomic gas undergoes an adiabatic expansion from volume $V_1$ and temperature $T_1$ to volume $V_2 = 32 V_1$:
(A) The final temperature of the gas is $T_2 = T_1 / 4$ (taking $\gamma = 7/5$).  
(B) The work done by the gas is $W = \frac{5}{2}R(T_1 - T_2) = \frac{15}{8}R T_1$.  
(C) The change in internal energy is $\Delta U = -W$.  
(D) The change in entropy of the gas is $\Delta S = 0$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A circular coil of 200 turns and radius $r = 0.10\text{ m}$ rotates at $\omega = 50\text{ rad/s}$ about a diameter perpendicular to a uniform magnetic field $B = 0.20\text{ T}$. The peak induced EMF in the coil is $V_0\text{ V}$. Taking $\pi = 3.14$, find $V_0$ rounded off to two decimal places.

#### Question 8
Two spherical raindrops of equal radii $r_1 = r_2 = 1.0\text{ mm}$ coalesce into a single spherical drop. If the surface tension of water is $T = 0.072\text{ N/m}$, the energy released during coalescence is $\Delta U \times 10^{-7}\text{ J}$. Find $\Delta U$ rounded off to two decimal places.

#### Question 9
In an RC discharge circuit, a capacitor of $C = 20\text{ }\mu\text{F}$ charged to $V_0 = 50\text{ V}$ discharges through a resistor $R = 50\text{ k}\Omega$. The time taken for the capacitor charge to drop to half its initial value is $t\text{ s}$. Given $\ln 2 \approx 0.693$, find $t$ rounded off to two decimal places.

#### Question 10
A mass $m = 2.0\text{ kg}$ is attached to a spring of spring constant $k = 200\text{ N/m}$ on a frictionless horizontal surface. The mass is pulled to $x = 0.10\text{ m}$ and released from rest. The maximum speed of the mass during oscillation is $v_{\max}\text{ m/s}$. Find $v_{\max}$.

#### Question 11
An electron is accelerated from rest through a potential difference $V = 150\text{ V}$. Its de Broglie wavelength is $\lambda\text{ \AA}$. Using $\lambda = \sqrt{150/V}\text{ \AA}$, find $\lambda$.

#### Question 12
The speed of sound in an ideal diatomic gas ($\gamma = 1.40$) of molar mass $M = 28\text{ g/mol}$ at temperature $T = 300\text{ K}$ is $v\text{ m/s}$. Given $R = 8.314\text{ J/(mol K)}$, find $v$ rounded off to the nearest integer.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The magnetic dipole moment of a thin flat circular coil of $N$ turns, radius $R$, carrying steady current $I$ is:
(A) $N I \pi R^2$  
(B) $2\pi N I R$  
(C) $\frac{N I R^2}{2}$  
(D) $N I R$

#### Question 14
A parallel plate capacitor with plate area $A$ and separation $d$ has a dielectric slab of thickness $d/2$ and dielectric constant $\kappa = 3$ inserted between the plates. The ratio of new capacitance to initial capacitance $C/C_0$ is:
(A) $3/2$  
(B) $4/3$  
(C) $2$  
(D) $5/3$

#### Question 15
A uniform solid sphere of mass $M$ and radius $R$ rolls without slipping down an incline of angle $\theta$. The linear acceleration of the sphere is:
(A) $\frac{5}{7}g\sin\theta$  
(B) $\frac{2}{3}g\sin\theta$  
(C) $\frac{1}{2}g\sin\theta$  
(D) $\frac{3}{5}g\sin\theta$

#### Question 16
The focal length of a thin convex lens of glass ($n = 1.50$) in air is $20\text{ cm}$. When immersed in water ($n = 4/3$), its focal length becomes:
(A) $40\text{ cm}$  
(B) $60\text{ cm}$  
(C) $80\text{ cm}$  
(D) $100\text{ cm}$

#### Question 17
In a radioactive decay series, the half-life of a radioisotope is $T_{1/2} = 10\text{ days}$. The fraction of original nuclei remaining after 30 days is:
(A) $1/4$  
(B) $1/8$  
(C) $1/16$  
(D) $1/32$

#### Question 18
Two identical simple pendulums of length $L$ have their bobs connected by a light weak spring. This system exhibits normal modes of oscillation with frequencies:
(A) $\omega_1 = \sqrt{g/L}$ and $\omega_2 = \sqrt{g/L + 2k/m}$  
(B) $\omega_1 = \sqrt{g/L}$ and $\omega_2 = \sqrt{2g/L}$  
(C) $\omega_1 = \omega_2 = \sqrt{g/L}$  
(D) $\omega_1 = \sqrt{k/m}$ and $\omega_2 = \sqrt{g/L}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an ideal gas undergoing a reversible adiabatic process:
(A) $P V^\gamma = \text{constant}$.  
(B) $T V^{\gamma-1} = \text{constant}$.  
(C) $T^\gamma P^{1-\gamma} = \text{constant}$.  
(D) The entropy change of the surroundings is $\Delta S_{\text{surr}} = 0$.

#### Question 20
Regarding coordination isomerism and linkage isomerism:
(A) $[Co(NH_3)_6][Cr(CN)_6]$ and $[Cr(NH_3)_6][Co(CN)_6]$ are coordination isomers.  
(B) $[Co(NH_3)_5(NO_2)]Cl_2$ and $[Co(NH_3)_5(ONO)]Cl_2$ are linkage isomers.  
(C) The nitro ($-\text{NO}_2$) isomer binds via nitrogen, whereas the nitrito ($-\text{ONO}$) isomer binds via oxygen.  
(D) Both linkage isomers exhibit identical UV-Vis absorption spectra.

#### Question 21
Which of the following organic transformations yield benzaldehyde ($\text{C}_6\text{H}_5\text{CHO}$):
(A) Rosenmund reduction of benzoyl chloride ($\text{C}_6\text{H}_5\text{COCl}$) using $\text{H}_2 / \text{Pd-BaSO}_4$.  
(B) Etard reaction of toluene with $\text{CrO}_2\text{Cl}_2$ followed by hydrolysis.  
(C) Gattermann-Koch reaction of benzene with $\text{CO} + \text{HCl}$ in the presence of anhydrous $\text{AlCl}_3 / \text{CuCl}$.  
(D) Ozonolysis of trans-stilbene followed by reductive workup with $\text{Zn}/\text{H}_2\text{O}$.

#### Question 22
Regarding chemical kinetics and the Arrhenius equation $k = A e^{-E_a/RT}$:
(A) The pre-exponential factor $A$ has the same units as the rate constant $k$.  
(B) A plot of $\ln k$ versus $1/T$ is linear with slope $-E_a/R$.  
(C) A catalyst lowers the activation energy $E_a$ without changing the enthalpy of reaction $\Delta H$.  
(D) The fraction of collisions having energy $\ge E_a$ is given by the Boltzmann factor $e^{-E_a/RT}$.

#### Question 23
Regarding the chemistry of halogens and interhalogen compounds:
(A) $\text{ClF}_3$ has a T-shaped geometry with two lone pairs in equatorial positions of a trigonal bipyramid.  
(B) $\text{IF}_7$ has a pentagonal bipyramidal molecular geometry.  
(C) Interhalogen compounds are generally more reactive than pure halogens (except $\text{F}_2$).  
(D) The oxidizing power of halogens decreases in the order $\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$.

#### Question 24
In qualitative inorganic analysis of Group II and Group IV cations:
(A) Group II cations are precipitated as sulfides using $\text{H}_2\text{S}$ in acidic medium ($\text{dil. HCl}$).  
(B) The common ion effect of $\text{H}^+$ suppresses the ionization of $\text{H}_2\text{S}$, keeping $[S^{2-}]$ low.  
(C) Group IV cations require alkaline medium ($\text{NH}_4\text{OH} + \text{NH}_4\text{Cl}$) to precipitate their sulfides.  
(D) $\text{CuS}$ precipitates in Group II, whereas $\text{ZnS}$ precipitates in Group IV.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The equilibrium constant for the water-gas shift reaction $\text{CO}(g) + \text{H}_2\text{O}(g) \rightleftharpoons \text{CO}_2(g) + \text{H}_2(g)$ is $K_c = 4.0$ at $1000\text{ K}$. If equimolar quantities of $\text{CO}$ and $\text{H}_2\text{O}$ are mixed, the percentage of $\text{CO}$ converted at equilibrium is $x\%$. Find $x$ rounded off to two decimal places.

#### Question 26
Calculate the $\text{pH}$ of a buffer solution prepared by mixing $0.20\text{ M}$ acetic acid ($\text{p}K_a = 4.74$) and $0.20\text{ M}$ sodium acetate. Find the $\text{pH}$ rounded off to two decimal places.

#### Question 27
For the cell $\text{Zn} \mid \text{Zn}^{2+}(1\text{ M}) \parallel \text{Ag}^+(1\text{ M}) \mid \text{Ag}$, given $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.76\text{ V}$ and $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$. The standard cell EMF is $E^\circ_{\text{cell}}\text{ V}$. Find $E^\circ_{\text{cell}}$.

#### Question 28
The half-life of radioactive $^{14}\text{C}$ is 5730 years. An ancient wooden artifact shows a $^{14}\text{C}$ activity that is $25\%$ of the activity of modern living wood. The age of the artifact is $t$ years. Find $t$.

#### Question 29
A $0.50\text{ molal}$ aqueous solution of $\text{NaCl}$ freezes at $-1.86^\circ\text{C}$. Given $K_f(\text{H}_2\text{O}) = 1.86\text{ K kg mol}^{-1}$, the van 't Hoff factor $i$ for this solution is $i$. Find $i$.

#### Question 30
The spin-only magnetic moment of $[\text{Fe}(\text{H}_2\text{O})_6]^{2+}$ is $\mu = \sqrt{n(n+2)}\text{ BM}$ where $n = 4$. Find $\mu$ rounded off to two decimal places.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following compounds will undergo nucleophilic addition with $\text{HCN}$ at the FASTEST rate:
(A) $\text{HCHO}$  
(B) $\text{CH}_3\text{CHO}$  
(C) $\text{CH}_3\text{COCH}_3$  
(D) $\text{C}_6\text{H}_5\text{CHO}$

#### Question 32
The geometry and hybridization of xenon in $\text{XeF}_4$ are:
(A) Square planar, $sp^3d^2$  
(B) Tetrahedral, $sp^3$  
(C) Octahedral, $sp^3d^2$  
(D) See-saw, $sp^3d$

#### Question 33
In a body-centered cubic (BCC) unit cell, the coordination number of each atom is:
(A) 6  
(B) 8  
(C) 12  
(D) 4

#### Question 34
Which of the following species is aromatic:
(A) Cyclopentadienyl anion ($\text{C}_5\text{H}_5^-$)  
(B) Cyclooctatetraene  
(C) Cyclopentadienyl cation  
(D) Cycloheptatriene

#### Question 35
The primary structure of a protein is held together by:
(A) Peptide bonds  
(B) Hydrogen bonds  
(C) Disulfide bridges  
(D) Ionic interactions

#### Question 36
The conjugate acid of $\text{HSO}_4^-$ is:
(A) $\text{SO}_4^{2-}$  
(B) $\text{H}_2\text{SO}_4$  
(C) $\text{H}_3\text{SO}_4^+$  
(D) $\text{HSO}_3^-$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f: \mathbb{R} \to \mathbb{R}$ be defined by $f(x) = x^3 - 3x^2 + 3x - 1$:
(A) $f(x) = (x-1)^3$.  
(B) $f'(x) \ge 0$ for all $x \in \mathbb{R}$, hence $f(x)$ is strictly increasing on $\mathbb{R}$.  
(C) $x = 1$ is a point of inflection of $f(x)$.  
(D) $f(x)$ has no local extrema on $\mathbb{R}$.

#### Question 38
Let $A$ and $B$ be two $n \times n$ invertible matrices:
(A) $(AB)^{-1} = B^{-1} A^{-1}$.  
(B) $\det(AB) = \det(A)\det(B)$.  
(C) $(A + B)^{-1} = A^{-1} + B^{-1}$ is generally false.  
(D) $\text{adj}(AB) = \text{adj}(B)\text{adj}(A)$.

#### Question 39
For any two non-zero vectors $\vec{u}$ and $\vec{v}$:
(A) $|\vec{u} + \vec{v}|^2 + |\vec{u} - \vec{v}|^2 = 2(|\vec{u}|^2 + |\vec{v}|^2)$ (Parallelogram law).  
(B) $|\vec{u} \times \vec{v}|^2 + (\vec{u} \cdot \vec{v})^2 = |\vec{u}|^2 |\vec{v}|^2$ (Lagrange's identity).  
(C) $\vec{u} \times \vec{v} = -\vec{v} \times \vec{u}$.  
(D) $\vec{u} \cdot (\vec{u} \times \vec{v}) = 0$.

#### Question 40
Let $I = \int_0^\pi x f(\sin x) dx$:
(A) $I = \frac{\pi}{2} \int_0^\pi f(\sin x) dx$.  
(B) If $f(\sin x) = \sin x$, then $I = \pi$.  
(C) The substitution $x = \pi - t$ leaves the limits transformed to $[0, \pi]$.  
(D) $\int_0^{\pi/2} \ln(\sin x) dx = -\frac{\pi}{2}\ln 2$.

#### Question 41
The ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b$) has eccentricity $e$:
(A) The distance between its foci is $2ae$.  
(B) The distance between its directrices is $2a/e$.  
(C) The length of its latus rectum is $2b^2/a$.  
(D) The sum of focal distances of any point on the ellipse is constant and equal to $2a$.

#### Question 42
Let events $A$ and $B$ satisfy $P(A) > 0, P(B) > 0$:
(A) If $A$ and $B$ are independent, $P(A \cap B) = P(A)P(B)$.  
(B) If $A$ and $B$ are mutually exclusive, $P(A \cap B) = 0$.  
(C) Independent events with non-zero probabilities cannot be mutually exclusive.  
(D) $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the area enclosed between the parabolas $y^2 = 4x$ and $x^2 = 4y$. Round off to two decimal places if needed.

#### Question 44
Find the remainder when $2^{2024}$ is divided by 7.

#### Question 45
Evaluate $\lim_{n \to \infty} \sum_{r=1}^n \frac{1}{n + r}$. The limit is $\ln k$. Find $k$.

#### Question 46
Find the distance between the parallel planes $2x - y + 2z = 4$ and $2x - y + 2z = -5$.

#### Question 47
If the sum of the coefficients in the expansion of $(1 + 2x)^n$ is 6561, find the value of $n$.

#### Question 48
Find the number of positive integers less than or equal to 100 that are divisible by either 3 or 5.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arctan\left(\frac{2x}{1-x^2}\right)$ with respect to $\arcsin\left(\frac{2x}{1+x^2}\right)$ for $x \in (-1, 1)$ is:
(A) $1$  
(B) $1/2$  
(C) $2$  
(D) $-1$

#### Question 50
The solution of the differential equation $\frac{dy}{dx} = \frac{x+y}{x}$ is:
(A) $y = x\ln|x| + Cx$  
(B) $y = x^2 + C$  
(C) $y = Cx e^x$  
(D) $y = \ln|x| + C$

#### Question 51
The angle between the asymptotes of the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ is:
(A) $2\arctan(b/a)$  
(B) $\arctan(b/a)$  
(C) $2\arctan(a/b)$  
(D) $\pi/2$

#### Question 52
The value of $\sum_{k=1}^{10} k^3$ is:
(A) 3025  
(B) 2025  
(C) 385  
(D) 55

#### Question 53
If $\tan\theta = 3/4$, then $\sin(2\theta)$ is:
(A) $24/25$  
(B) $7/25$  
(C) $12/25$  
(D) $16/25$

#### Question 54
The probability of getting a sum of 9 in a single throw of two fair six-sided dice is:
(A) $1/9$  
(B) $1/6$  
(C) $1/12$  
(D) $5/36$
"""

        raw_sol1 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 1)
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)

---

# PART I: PHYSICS

### Question 1
- **Concept**: Maxwell's Equations and Displacement Current in a circular capacitor.
- **Step 1**: Charge $Q(t) = I_0 t$. The electric field is $E = \frac{Q}{\varepsilon_0 A} = \frac{I_0 t}{\varepsilon_0 \pi R^2}$. Thus (A) is correct.
- **Step 2**: Displacement current density $J_d = \varepsilon_0 \frac{\partial E}{\partial t} = \varepsilon_0 \frac{I_0}{\varepsilon_0 \pi R^2} = \frac{I_0}{\pi R^2}$. Thus (B) is correct.
- **Step 3**: Ampère-Maxwell law: $\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enclosed}} = \mu_0 J_d (\pi r^2) \implies B(2\pi r) = \mu_0 \frac{I_0}{\pi R^2} \pi r^2 \implies B = \frac{\mu_0 I_0 r}{2\pi R^2}$. (C) is correct.
- **Step 4**: Poynting vector $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$. $\vec{E}$ is along $+\hat{k}$ and $\vec{B}$ is along $+\hat{\phi}$, so $\vec{E} \times \vec{B}$ points in $-\hat{r}$ (inward). Thus (D) is correct.
- **Correct Options**: (A, B, C, D)

### Question 2
- **Concept**: Electrostatics of layered dielectrics.
- **Step 1**: Gauss's law for displacement $\oint \vec{D} \cdot d\vec{A} = Q \implies D(r) = \frac{Q}{4\pi r^2}$ everywhere, which is continuous across $r = c$. Thus (A) is correct.
- **Step 2**: $E(r) = D(r)/(\varepsilon_0 \kappa)$. Ratio $E(c^-)/E(c^+) = \kappa_2 / \kappa_1$. Thus (B) is correct.
- **Step 3**: Polarization $\vec{P} = \varepsilon_0 (\kappa - 1)\vec{E}$. Bound surface charge $\sigma_b = (\vec{P}_1 - \vec{P}_2)\cdot \hat{r} \implies q_b = Q\left(\frac{1}{\kappa_2} - \frac{1}{\kappa_1}\right)$. (C) is correct.
- **Step 4**: Capacitance formula represents two spherical capacitors in series: $1/C = 1/C_1 + 1/C_2$. Thus (D) is correct.
- **Correct Options**: (A, B, C, D)

### Question 3
- **Concept**: Faraday's Law in a cylindrical field region.
- **Step 1**: Flux $\Phi = B(t) \cdot (\pi R^2) = B_0 \pi R^2 \cos(\omega t)$. Thus (A) is correct.
- **Step 2**: Induced EMF $\mathcal{E} = -d\Phi/dt = B_0 \pi R^2 \omega \sin(\omega t)$. Thus (B) is correct.
- **Step 3**: Due to four-fold symmetry, the forces on opposite sides cancel identically: $F_{\text{net}} = 0$. Thus (C) is correct.
- **Step 4**: The frame has 4 straight sides, current flows uniformly along the perimeter, not around corners individually. Thus (D) is incorrect.
- **Correct Options**: (A, B, C)

### Question 4
- **Concept**: Induced electric field accelerating a charged ring.
- **Step 1**: Induced electric field along the circumference satisfies $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi}{dt} \implies E(2\pi a) = \pi a^2 \frac{dB}{dt} \implies E = \frac{a}{2}\frac{dB}{dt}$.
- **Step 2**: Torque $\tau = q E a = \frac{q a^2}{2}\frac{dB}{dt}$.
- **Step 3**: $\int \tau dt = I_{\text{ring}} \omega \implies \frac{q a^2 B_0}{2} = (m a^2) \omega \implies \omega = \frac{q B_0}{2m}$. Thus (A), (B), (C), (D) are all correct.
- **Correct Options**: (A, B, C, D)

### Question 5
- **Concept**: Lloyd's mirror interference.
- **Step 1**: The real source and virtual image form two coherent sources separated by $2d$.
- **Step 2**: Fringe width $\beta = \frac{\lambda D}{2d} = \frac{500 \times 10^{-9} \times 1.0}{2 \times 1.0 \times 10^{-3}} = 0.25\text{ mm}$. (A) is correct.
- **Step 3**: Reflection at the mirror introduces a $\pi$ phase change (path difference $\lambda/2$), so the central fringe is dark. (B) is correct.
- **Step 4**: Bright fringes occur at $y_n = (n - 1/2)\beta$. (C) is correct.
- **Correct Options**: (A, B, C)

### Question 6
- **Concept**: Radiation pressure.
- **Step 1**: Absorbing: $P = I/c$. Reflecting: $P = 2I/c$. Fraction $R$: $P = (1+R)I/c$.
- **Step 2**: Verified by Nichols and Hull (1901).
- **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $E(2\pi r) = \pi r^2 \mu_0 n \frac{dI}{dt} \implies E = \frac{1}{2} r \mu_0 n \frac{dI}{dt} = \frac{1}{2}(0.05)(4\pi \times 10^{-7})(1000)(4.0) = 1.26 \times 10^{-4}\text{ V/m} \implies \mathbf{1.26}$.
- **Q8**: Initial energy $U_i = \frac{1}{2} C_0 V_0^2 = \frac{1}{2}(10 \times 10^{-6})(100)^2 = 50\text{ mJ}$. Half slab inserted: $C_f = \frac{1}{2}C_0 + \frac{1}{2}\kappa C_0 = 2.5 C_0$. Disconnected $\implies Q = C_0 V_0$ constant. $U_f = Q^2/(2C_f) = U_i / 2.5 = 20\text{ mJ}$. $W = U_i - U_f = 30\text{ mJ} \implies \mathbf{30.00}$.
- **Q9**: At resonance, $I_0 = V_0 / R = 220 / 10 = 22\text{ A}$. $X_L = \omega_0 L = 1000 \times 0.10 = 100\text{ }\Omega$. $V_L = I_0 X_L = 22 \times 100 = 2200\text{ V} \implies \mathbf{2200.00}$.
- **Q10**: $\tau = q E r = q (\frac{r}{2}\frac{dB}{dt}) r = \frac{1}{2} q r^2 \frac{dB}{dt} = \frac{1}{2}(2.0)(0.20)^2(5.0) = 0.20\text{ N m}$. $I = m r^2 = 0.50 \times 0.04 = 0.02\text{ kg m}^2$. $\alpha = \tau / I = 0.20 / 0.02 = 10.00\text{ rad/s}^2 \implies \mathbf{10.00}$.
- **Q11**: $\tan\theta_p = \sqrt{3} \implies \theta_p = 60^\circ$. $\theta_r = 90^\circ - \theta_p = 30^\circ \implies \mathbf{30.00}$.
- **Q12**: $Q = \int C dT = \int_{300}^{400} (\frac{3}{2}R + 2RT) dT = \frac{3}{2}R(100) + R(400^2 - 300^2) = 150R + 70000R = 70150 R \implies \mathbf{70150.00}$.

### Questions 13 to 18
- **Q13**: By right-hand rule and Ampère's law, $\vec{B} = -\frac{\mu_0 K_0}{2}\hat{j}$. **Correct: (B)**.
- **Q14**: The outer charge redistributes uniformly to shield the interior: outer surface density is uniform. **Correct: (B)**.
- **Q15**: $M = \sqrt{L_1 L_2} = \sqrt{4 \times 9} = 6\text{ H}$. **Correct: (B)**.
- **Q16**: $q(\vec{E} + \vec{v} \times \vec{B}) = q(E_0 \hat{j} + v_0 \hat{i} \times B_0 \hat{k}) = q(E_0 \hat{j} - v_0 B_0 \hat{j}) = 0$. Particle moves undeflected in a straight line. **Correct: (A)**.
- **Q17**: $\beta = \frac{T_C}{T_H - T_C} = \frac{250}{300 - 250} = 5.0$. **Correct: (A)**.
- **Q18**: Unpolarized through first polarizer gives $I_0/2$. Through second gives $(I_0/2)\cos^2(60^\circ) = (I_0/2)(1/4) = I_0/8$. **Correct: (C)**.

---

# PART II: CHEMISTRY

### Question 19 to 24
- **Q19**: Standard hydrogen electrode combined with $\text{Fe}^{3+}/\text{Fe}^{2+}$. All listed thermodynamic and electrochemical properties are correct. **Correct Options**: (A, B, C, D)
- **Q20**: Thermodynamic definitions of ideal and non-ideal solutions. **Correct Options**: (A, B, C, D)
- **Q21**: $[Co(NH_3)_4 Cl_2]^+$ has *cis* and *trans* forms. *trans* has inversion center (achiral), *cis* has $C_{2v}$ symmetry without inversion center, but has planes of symmetry, making it optically inactive as well. Thus (B) is false. Correct are (A, C, D).
- **Q22**: Chemistry of permanganate and dichromate. LMCT gives deep color. **Correct Options**: (A, B, C, D)
- **Q23**: Mechanism of aldol condensation: $\alpha$-deprotonation, enolate attack, E1cB dehydration. **Correct Options**: (A, B, C, D)
- **Q24**: Nucleic acids and amino acids fundamentals. **Correct Options**: (A, B, C, D)

### Questions 25 to 30
- **Q25**: $\text{Ag}_2\text{CrO}_4 \rightleftharpoons 2\text{Ag}^+ + \text{CrO}_4^{2-} \implies K_{\text{sp}} = 4S^3 = 1.08 \times 10^{-12} \implies S^3 = 0.27 \times 10^{-12} = 2.7 \times 10^{-13} \implies S = 0.646 \times 10^{-4}\text{ M} \implies \mathbf{0.65}$.
- **Q26**: $87.5\%$ decomposition means $12.5\% = (1/2)^3$ remains $\implies t = 3 t_{1/2} = 90.0\text{ min} \implies \mathbf{90.00}$.
- **Q27**: $K = \frac{2 \times 1.10}{0.0591} = \frac{2.20}{0.0591} \approx 37.23 \implies \mathbf{37.23}$.
- **Q28**: $\Delta T_f = i K_f m \implies 0.2046 = (1+\alpha)(1.86)(0.10) \implies 1+\alpha = 1.10 \implies \alpha = 0.10 = 10\% \implies \mathbf{10.00}$.
- **Q29**: $[\text{Co}(\text{NH}_3)_5 \text{Cl}]\text{Cl}_2 \implies$ coordination number of Co is $5 + 1 = 6 \implies \mathbf{6.00}$.
- **Q30**: $\text{C}_6\text{H}_6(l) + \frac{15}{2}\text{O}_2(g) \to 6\text{CO}_2(g) + 3\text{H}_2\text{O}(l) \implies \Delta n_g = 6 - 7.5 = -1.5 \implies |\Delta n_g| = \mathbf{1.50}$.

### Questions 31 to 36
- **Q31**: Diamminechloridonitrito-N-platinum(II). **Correct: (A)**.
- **Q32**: Ethanol ($\text{C}_2\text{H}_5\text{OH}$) and Dimethyl ether ($\text{CH}_3\text{OCH}_3$) are functional isomers. **Correct: (A)**.
- **Q33**: $\text{O}_2$ oxidizes silver to cyanide complex. **Correct: (A)**.
- **Q34**: $\Lambda_m = \frac{1000 \kappa}{M} \implies \kappa = \frac{120 \times 0.01}{1000} = 1.2 \times 10^{-3}\text{ S cm}^{-1}$. **Correct: (A)**.
- **Q35**: Tropylium cation has $6\pi$ aromatic stabilization. **Correct: (A)**.
- **Q36**: $1665 / 4 = 416.25\text{ kJ/mol}$. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: $f'(x) = \frac{1 - \ln x}{x^2}$. Maximum at $x=e$ with value $1/e$. Since $f(e) > f(\pi)$, $\frac{\ln e}{e} > \frac{\ln \pi}{\pi} \implies e^\pi > \pi^e$. **Correct Options**: (A, B, C, D)
- **Q38**: Properties of skew-symmetric matrices. In odd dimensions $\det(A) = 0$. Cayley transform produces an orthogonal matrix. **Correct Options**: (A, B, C, D)
- **Q39**: $\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c} = \frac{1}{2}\vec{b} \implies \vec{a} \cdot \vec{c} = 1/2, \vec{a} \cdot \vec{b} = 0$. **Correct Options**: (A, B, C, D)
- **Q40**: Walli's-type integral reduction. **Correct Options**: (A, B, C, D)
- **Q41**: Disc centered at $(3, 4)$ with radius $2$. Distance from origin is $5$. Max $|z| = 5 + 2 = 7$, min $|z| = 5 - 2 = 3$. **Correct Options**: (A, B, C, D)
- **Q42**: Standard theorems of focal chords for a parabola. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: King's property: $2I = \int_0^{\pi/2} 1 dx = \pi/2 \implies I = \pi/4 \implies k = \mathbf{4.00}$.
- **Q44**: Real distinct roots of opposite signs $\implies \Delta > 0$ and product of roots $< 0 \implies \frac{k+4}{k-2} < 0 \implies k \in (-4, 2)$. Integers: $-3, -2, -1, 0, 1 \implies 5$ values. $\mathbf{5.00}$.
- **Q45**: Arithmetico-geometric series: $S = 1/2 + 2/4 + 3/8 + \dots = 2 \implies \mathbf{2.00}$.
- **Q46**: Parametric point $P(2t+1, 3t+2, 4t+3)$. Substitute in plane: $2(2t+1) + 3(3t+2) - (4t+3) = 5 \implies 9t + 5 = 5 \implies t = 0$. $P = (1, 2, 3) \implies x_0 + y_0 + z_0 = 1 + 2 + 3 = \mathbf{6.00}$.
- **Q47**: Total ways $\binom{10}{3} = 120$. Favorable: 3 red $\binom{4}{3} = 4$, 3 black $\binom{6}{3} = 20$. Total favorable $= 24$. $P = 24/120 = 1/5$. $m + n = 1 + 5 = \mathbf{6.00}$.
- **Q48**: Sphere equation: $x^2 + y^2 + z^2 - 2x - 4y - 6z = 0$. Center $(1, 2, 3)$, radius $R = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14} \implies R^2 = \mathbf{14.00}$.

### Questions 49 to 54
- **Q49**: $\lim_{x \to 0} \frac{(1 + x^2 + \dots) - (1 - x^2/2 + \dots)}{x^2} = 1 + 1/2 = 3/2$. **Correct: (C)**.
- **Q50**: Integrating factor $e^{\int \tan x dx} = \sec x$. $y\sec x = \int \sec^2 x dx = \tan x + C$. $y(0) = 0 \implies C = 0$. $y = \sin x$. $y(\pi/4) = 1/\sqrt{2}$. **Correct: (C)**.
- **Q51**: $e = \sqrt{1 + b^2/a^2} = \sqrt{1 + 9/16} = 5/4$. **Correct: (B)**.
- **Q52**: Vowels: A, E, A, I (4 vowels with two A's). Consonants: M, T, H, M, T, C, S (7 consonants with two M's and two T's). Number of ways: $\frac{8!}{2! 2!} \times \frac{4!}{2!} = 10080 \times 12 = 120960$. **Correct: (A)**.
- **Q53**: $(a^2 + b^2) = (\sin\alpha + \sin\beta)^2 + (\cos\alpha + \cos\beta)^2 = 2 + 2\cos(\alpha - \beta) \implies \cos(\alpha - \beta) = \frac{a^2 + b^2 - 2}{2}$. **Correct: (A)**.
- **Q54**: By induction, $A^n = \begin{pmatrix} 1 & 2n \\ 0 & 1 \end{pmatrix} \implies A^{10} = \begin{pmatrix} 1 & 20 \\ 0 & 1 \end{pmatrix}$. **Correct: (A)**.
"""

        raw_sol2 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 2)
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Parallel $\vec{E}$ and $\vec{B}$ fields decouple: along $z$, $F_z = qE_0$ gives constant acceleration; in $xy$-plane, $F_{\perp} = q v_{\perp} B_0$ gives circular motion at $\omega_c = qB_0/m$. Pitch increases linearly with time. Kinetic energy increases monotonically. **Correct Options**: (A, B, C, D)
- **Q2**: Uniformly polarized sphere: $\sigma_b = \vec{P} \cdot \hat{n} = P_0 \cos\theta$. Volume charge $\rho_b = -\nabla \cdot \vec{P} = 0$. Interior field is $\vec{E} = -\vec{P}/(3\varepsilon_0)$. Dipole moment $\vec{p} = \frac{4}{3}\pi R^3 P_0 \hat{k}$. **Correct Options**: (A, B, C, D)
- **Q3**: Parallel resonance circuit. Dynamic impedance $Z_{\text{dyn}} = L/(CR)$, anti-resonance minimizes current. **Correct Options**: (A, B, C, D)
- **Q4**: Bar sliding on rails with vertical field. Induced EMF $\mathcal{E} = B L v \cos\theta$, retarding force along incline balances gravity component $mg\sin\theta$. Terminal velocity $v_t = \frac{mgR\sin\theta}{B^2 L^2 \cos^2\theta}$. **Correct Options**: (A, B, C, D)
- **Q5**: Introduction of mica sheet in YDSE shifts entire pattern without changing fringe width. **Correct Options**: (A, B, C, D)
- **Q6**: Adiabatic expansion with $\gamma = 7/5$: $T_2 = T_1 (V_1/V_2)^{\gamma-1} = T_1 (1/32)^{2/5} = T_1 / 4$. $W = -\Delta U = n C_V (T_1 - T_2) = \frac{5}{2}R(3T_1/4) = \frac{15}{8}RT_1$. Reversible adiabatic $\implies \Delta S = 0$. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $V_0 = N B A \omega = 200 \times 0.20 \times (\pi \times 0.01) \times 50 = 200 \times 0.20 \times 0.0314 \times 50 = 62.83\text{ V} \implies \mathbf{62.83}$.
- **Q8**: Coalescence: $V = 2 \times \frac{4}{3}\pi r^3 \implies R = 2^{1/3} r$. Surface area change $\Delta A = 4\pi (2 r^2 - R^2) = 4\pi r^2 (2 - 2^{2/3}) \approx 4\pi (10^{-6})(2 - 1.5874) \approx 5.18 \times 10^{-6}\text{ m}^2$. Energy released $\Delta U = T \Delta A = 0.072 \times 5.18 \times 10^{-6} \approx 3.73 \times 10^{-7}\text{ J} \implies \mathbf{3.73}$.
- **Q9**: $q(t) = Q_0 e^{-t/RC} \implies t = RC\ln 2 = (50 \times 10^3)(20 \times 10^{-6})(0.693) = 1.0 \times 0.693 = 0.69\text{ s} \implies \mathbf{0.69}$.
- **Q10**: $\omega = \sqrt{k/m} = \sqrt{200/2} = 10\text{ rad/s}$. $v_{\max} = A \omega = 0.10 \times 10 = 1.00\text{ m/s} \implies \mathbf{1.00}$.
- **Q11**: $\lambda = \sqrt{150/150} = 1.00\text{ \AA} \implies \mathbf{1.00}$.
- **Q12**: $v = \sqrt{\frac{\gamma R T}{M}} = \sqrt{\frac{1.40 \times 8.314 \times 300}{0.028}} = \sqrt{124710} \approx 353\text{ m/s} \implies \mathbf{353.00}$.

### Questions 13 to 18
- **Q13**: $M = N I A = N I \pi R^2$. **Correct: (A)**.
- **Q14**: $C = \frac{\varepsilon_0 A}{d/2 + (d/2)/\kappa} = \frac{\varepsilon_0 A}{\frac{d}{2}(1 + 1/3)} = \frac{\varepsilon_0 A}{\frac{2}{3}d} = \frac{3}{2}C_0$. **Correct: (A)**.
- **Q15**: $a = \frac{g\sin\theta}{1 + I/(MR^2)} = \frac{g\sin\theta}{1 + 2/5} = \frac{5}{7}g\sin\theta$. **Correct: (A)**.
- **Q16**: Lens maker formula: $1/f_w = \left(\frac{1.5}{4/3} - 1\right)\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = \left(\frac{9}{8} - 1\right) \frac{1}{R} = \frac{1}{8R}$. In air: $1/f_a = (1.5 - 1)\frac{1}{R} = \frac{1}{2R} = \frac{1}{20} \implies R = 10\text{ cm}$. Then $f_w = 8R = 80\text{ cm}$. **Correct: (C)**.
- **Q17**: 3 half-lives: $(1/2)^3 = 1/8$. **Correct: (B)**.
- **Q18**: Symmetric mode: bobs in phase, spring unstretched $\implies \omega_1 = \sqrt{g/L}$. Anti-symmetric mode: bobs out of phase, spring stretched $\implies \omega_2 = \sqrt{g/L + 2k/m}$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Reversible adiabatic equations for ideal gas. **Correct Options**: (A, B, C, D)
- **Q20**: Coordination vs linkage isomers. Linkage isomers have different ligands attached, differing in crystal field splitting, hence different UV-Vis spectra (D is false). Correct are (A, B, C).
- **Q21**: All four reactions are classic, robust synthetic routes to benzaldehyde. **Correct Options**: (A, B, C, D)
- **Q22**: Kinetic principles and Arrhenius equation. **Correct Options**: (A, B, C, D)
- **Q23**: Interhalogen geometries via VSEPR and halogen reactivity trends. **Correct Options**: (A, B, C, D)
- **Q24**: Qualitative analysis principles for Group II and IV. **Correct Options**: (A, B, C, D)

### Questions 25 to 30
- **Q25**: $\text{CO} + \text{H}_2\text{O} \rightleftharpoons \text{CO}_2 + \text{H}_2$. Let initial moles be 1, converted be $x$. $\frac{x^2}{(1-x)^2} = 4 \implies \frac{x}{1-x} = 2 \implies x = 2/3 \approx 66.67\% \implies \mathbf{66.67}$.
- **Q26**: Buffer $\text{pH} = \text{p}K_a + \log\left(\frac{[\text{salt}]}{[\text{acid}]}\right) = 4.74 + \log(1) = 4.74 \implies \mathbf{4.74}$.
- **Q27**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = 0.80 - (-0.76) = 1.56\text{ V} \implies \mathbf{1.56}$.
- **Q28**: Activity drops to $25\% = (1/2)^2 \implies t = 2 \times 5730 = 11460\text{ years} \implies \mathbf{11460.00}$.
- **Q29**: $\Delta T_f = i K_f m \implies 1.86 = i (1.86)(0.50) \implies i = 2.00 \implies \mathbf{2.00}$.
- **Q30**: For $n=4$, $\mu = \sqrt{4 \times 6} = \sqrt{24} \approx 4.90\text{ BM} \implies \mathbf{4.90}$.

### Questions 31 to 36
- **Q31**: Formaldehyde ($\text{HCHO}$) has least steric hindrance and most electrophilic carbonyl carbon. **Correct: (A)**.
- **Q32**: $\text{XeF}_4$ has 4 bond pairs and 2 lone pairs $\implies sp^3d^2$ square planar. **Correct: (A)**.
- **Q33**: BCC coordination number is 8. **Correct: (B)**.
- **Q34**: Cyclopentadienyl anion has $6\pi$ electrons ($4n+2$ with $n=1$), planar, cyclic conjugated $\implies$ aromatic. **Correct: (A)**.
- **Q35**: Primary structure is defined by covalent peptide bonds. **Correct: (A)**.
- **Q36**: Conjugate acid of $\text{HSO}_4^-$ is formed by adding $\text{H}^+$, giving $\text{H}_2\text{SO}_4$. **Correct: (B)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: $f(x) = (x-1)^3$. $f'(x) = 3(x-1)^2 \ge 0$, strictly increasing, inflection point at $x=1$, no extrema. **Correct Options**: (A, B, C, D)
- **Q38**: Invertible matrix properties. **Correct Options**: (A, B, C, D)
- **Q39**: Vector identities and properties. **Correct Options**: (A, B, C, D)
- **Q40**: Definite integral King's rule and Dirichlet integral $\int_0^{\pi/2}\ln(\sin x)dx = -\frac{\pi}{2}\ln 2$. **Correct Options**: (A, B, C, D)
- **Q41**: Standard parameters of an ellipse. **Correct Options**: (A, B, C, D)
- **Q42**: Probability theory fundamental theorems. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Intersection of $y^2 = 4x$ and $x^2 = 4y$: $(x^2/4)^2 = 4x \implies x^4 = 64x \implies x = 4$. Area $= \int_0^4 (2\sqrt{x} - x^2/4)dx = [ \frac{4}{3}x^{3/2} - \frac{x^3}{12} ]_0^4 = \frac{32}{3} - \frac{16}{3} = \frac{16}{3} \approx 5.33 \implies \mathbf{5.33}$.
- **Q44**: $2^3 \equiv 1 \pmod 7$. $2024 = 3 \times 674 + 2$. $2^{2024} \equiv (2^3)^{674} \times 2^2 \equiv 1 \times 4 \equiv 4 \pmod 7 \implies \mathbf{4.00}$.
- **Q45**: Riemann sum $\lim_{n \to \infty} \frac{1}{n}\sum_{r=1}^n \frac{1}{1 + r/n} = \int_0^1 \frac{dx}{1+x} = \ln 2 \implies k = \mathbf{2.00}$.
- **Q46**: $d = \frac{|4 - (-5)|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{9}{3} = 3.00 \implies \mathbf{3.00}$.
- **Q47**: Sum of coefficients $= (1+2)^n = 3^n = 6561 = 3^8 \implies n = \mathbf{8.00}$.
- **Q48**: Multiples of 3: $\lfloor 100/3 \rfloor = 33$. Multiples of 5: $\lfloor 100/5 \rfloor = 20$. Multiples of 15: $\lfloor 100/15 \rfloor = 6$. Total $= 33 + 20 - 6 = 47 \implies \mathbf{47.00}$.

### Questions 49 to 54
- **Q49**: For $x \in (-1, 1)$, $\arctan\left(\frac{2x}{1-x^2}\right) = 2\arctan x$, and $\arcsin\left(\frac{2x}{1+x^2}\right) = 2\arctan x$. The derivative of a function with respect to itself is 1. **Correct: (A)**.
- **Q50**: Homogeneous ODE: $y = vx \implies v + x\frac{dv}{dx} = 1 + v \implies \frac{dv}{dx} = \frac{1}{x} \implies v = \ln|x| + C \implies y = x\ln|x| + Cx$. **Correct: (A)**.
- **Q51**: Slopes of asymptotes are $\pm b/a$. Angle between them is $2\arctan(b/a)$. **Correct: (A)**.
- **Q52**: $\sum_{k=1}^{10} k^3 = \left(\frac{10 \times 11}{2}\right)^2 = 55^2 = 3025$. **Correct: (A)**.
- **Q53**: $\sin(2\theta) = \frac{2\tan\theta}{1+\tan^2\theta} = \frac{2(3/4)}{1 + 9/16} = \frac{3/2}{25/16} = \frac{24}{25}$. **Correct: (A)**.
- **Q54**: Sum of 9 pairs: $(3,6), (4,5), (5,4), (6,3) \implies 4$ outcomes out of 36 $\implies 4/36 = 1/9$. **Correct: (A)**.
"""

        raw_val = r"""# Comprehensive Answer Key & Academic Alignment Validation – JEE Advanced Mock Examination __PAD__
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)

---

### Master Answer Key – Paper 1
| Q# | Subject | Section | Question Type | Key |
|---|---|---|---|---|
| 1 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 2 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 3 | Physics | Sec 1 | One or More Than One Correct | A, B, C |
| 4 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 5 | Physics | Sec 1 | One or More Than One Correct | A, B, C |
| 6 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 7 | Physics | Sec 2 | Numerical | 1.26 |
| 8 | Physics | Sec 2 | Numerical | 30.00 |
| 9 | Physics | Sec 2 | Numerical | 2200.00 |
| 10 | Physics | Sec 2 | Numerical | 10.00 |
| 11 | Physics | Sec 2 | Numerical | 30.00 |
| 12 | Physics | Sec 2 | Numerical | 70150.00 |
| 13 | Physics | Sec 3 | Single Correct | B |
| 14 | Physics | Sec 3 | Single Correct | B |
| 15 | Physics | Sec 3 | Single Correct | B |
| 16 | Physics | Sec 3 | Single Correct | A |
| 17 | Physics | Sec 3 | Single Correct | A |
| 18 | Physics | Sec 3 | Single Correct | C |
| 19 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 20 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 21 | Chemistry | Sec 1 | One or More Than One Correct | A, C, D |
| 22 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 23 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 25 | Chemistry | Sec 2 | Numerical | 0.65 |
| 26 | Chemistry | Sec 2 | Numerical | 90.00 |
| 27 | Chemistry | Sec 2 | Numerical | 37.23 |
| 28 | Chemistry | Sec 2 | Numerical | 10.00 |
| 29 | Chemistry | Sec 2 | Numerical | 6.00 |
| 30 | Chemistry | Sec 2 | Numerical | 1.50 |
| 31 | Chemistry | Sec 3 | Single Correct | A |
| 32 | Chemistry | Sec 3 | Single Correct | A |
| 33 | Chemistry | Sec 3 | Single Correct | A |
| 34 | Chemistry | Sec 3 | Single Correct | A |
| 35 | Chemistry | Sec 3 | Single Correct | A |
| 36 | Chemistry | Sec 3 | Single Correct | A |
| 37 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 38 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 39 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 40 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 41 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 42 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 43 | Mathematics | Sec 2 | Numerical | 4.00 |
| 44 | Mathematics | Sec 2 | Numerical | 5.00 |
| 45 | Mathematics | Sec 2 | Numerical | 2.00 |
| 46 | Mathematics | Sec 2 | Numerical | 6.00 |
| 47 | Mathematics | Sec 2 | Numerical | 6.00 |
| 48 | Mathematics | Sec 2 | Numerical | 14.00 |
| 49 | Mathematics | Sec 3 | Single Correct | C |
| 50 | Mathematics | Sec 3 | Single Correct | C |
| 51 | Mathematics | Sec 3 | Single Correct | B |
| 52 | Mathematics | Sec 3 | Single Correct | A |
| 53 | Mathematics | Sec 3 | Single Correct | A |
| 54 | Mathematics | Sec 3 | Single Correct | A |

---

### Master Answer Key – Paper 2
| Q# | Subject | Section | Question Type | Key |
|---|---|---|---|---|
| 1 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 2 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 3 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 4 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 5 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 6 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 7 | Physics | Sec 2 | Numerical | 62.83 |
| 8 | Physics | Sec 2 | Numerical | 3.73 |
| 9 | Physics | Sec 2 | Numerical | 0.69 |
| 10 | Physics | Sec 2 | Numerical | 1.00 |
| 11 | Physics | Sec 2 | Numerical | 1.00 |
| 12 | Physics | Sec 2 | Numerical | 353.00 |
| 13 | Physics | Sec 3 | Single Correct | A |
| 14 | Physics | Sec 3 | Single Correct | A |
| 15 | Physics | Sec 3 | Single Correct | A |
| 16 | Physics | Sec 3 | Single Correct | C |
| 17 | Physics | Sec 3 | Single Correct | B |
| 18 | Physics | Sec 3 | Single Correct | A |
| 19 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 20 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C |
| 21 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 22 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 23 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 25 | Chemistry | Sec 2 | Numerical | 66.67 |
| 26 | Chemistry | Sec 2 | Numerical | 4.74 |
| 27 | Chemistry | Sec 2 | Numerical | 1.56 |
| 28 | Chemistry | Sec 2 | Numerical | 11460.00 |
| 29 | Chemistry | Sec 2 | Numerical | 2.00 |
| 30 | Chemistry | Sec 2 | Numerical | 4.90 |
| 31 | Chemistry | Sec 3 | Single Correct | A |
| 32 | Chemistry | Sec 3 | Single Correct | A |
| 33 | Chemistry | Sec 3 | Single Correct | B |
| 34 | Chemistry | Sec 3 | Single Correct | A |
| 35 | Chemistry | Sec 3 | Single Correct | A |
| 36 | Chemistry | Sec 3 | Single Correct | B |
| 37 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 38 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 39 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 40 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 41 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 42 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 43 | Mathematics | Sec 2 | Numerical | 5.33 |
| 44 | Mathematics | Sec 2 | Numerical | 4.00 |
| 45 | Mathematics | Sec 2 | Numerical | 2.00 |
| 46 | Mathematics | Sec 2 | Numerical | 3.00 |
| 47 | Mathematics | Sec 2 | Numerical | 8.00 |
| 48 | Mathematics | Sec 2 | Numerical | 47.00 |
| 49 | Mathematics | Sec 3 | Single Correct | A |
| 50 | Mathematics | Sec 3 | Single Correct | A |
| 51 | Mathematics | Sec 3 | Single Correct | A |
| 52 | Mathematics | Sec 3 | Single Correct | A |
| 53 | Mathematics | Sec 3 | Single Correct | A |
| 54 | Mathematics | Sec 3 | Single Correct | A |
"""

        p1 = raw_p1.replace("__PAD__", pad)
        p2 = raw_p2.replace("__PAD__", pad)
        sol1 = raw_sol1.replace("__PAD__", pad)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, "IIT_Madras")
        print(f"Generated IIT Madras Mock {pad}!")

if __name__ == "__main__":
    generate_madras_06_to_10()

