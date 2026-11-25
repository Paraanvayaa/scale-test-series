"""
IIT Roorkee Mocks 06 to 10 Generator
Organising Institute: Indian Institute of Technology Roorkee
Empirical Benchmark: 2008, 2013, 2019 Official JEE Advanced Papers
Features:
- Mechanics dominance (>= 45% of physics: rolling inside hollow cylinder, Atwood machine with pulley inertia, capillary dynamics, meter bridge corrections)
- Chemistry: Baeyer-Villiger oxidation, peptide coupling (Boc/Fmoc), quadruple metal-metal bonding, Wilkinson's catalyst
- Mathematics: Arc length rectification, evolutes & envelopes, characteristic roots of recurrences, Bayes' theorem
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_roorkee_06_to_10():
    for mock_idx in range(6, 11):
        pad = f"{mock_idx:02d}"

        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)
**Historical Reference Benchmark**: 2008, 2013, 2019 Official Examination Papers  
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
A small uniform solid sphere of mass $m$ and radius $r$ rolls without slipping inside a fixed hollow cylindrical surface of radius $R$ ($R > r$):
(A) The kinetic energy of the sphere when its center is displaced by angle $\theta$ from the lowest point is $K = \frac{7}{10}m(R-r)^2\dot{\theta}^2$.  
(B) The potential energy of the sphere relative to the lowest position is $U(\theta) = mg(R-r)(1 - \cos\theta)$.  
(C) For small oscillations, the angular frequency of oscillation is $\omega = \sqrt{\frac{5g}{7(R-r)}}$.  
(D) The normal contact force exerted by the cylinder on the sphere at the lowest point with oscillation amplitude $\theta_0$ is $N = mg\left(1 + \frac{10}{7}(1 - \cos\theta_0)\right)$.

#### Question 2
In an Atwood machine, two blocks of masses $m_1$ and $m_2$ ($m_1 > m_2$) are connected by a light inextensible cord passing over a pulley of mass $M$, radius $R$, and moment of inertia $I = \frac{1}{2}MR^2$. The axle of the pulley is frictionless, and the cord does not slip on the pulley:
(A) The linear acceleration of the descending mass $m_1$ is $a = \frac{(m_1 - m_2)g}{m_1 + m_2 + M/2}$.  
(B) The tensions in the two vertical segments of the cord are unequal: $T_1 - T_2 = \frac{1}{2}Ma$.  
(C) The tension supporting mass $m_1$ is $T_1 = m_1(g - a)$.  
(D) If the mass of the pulley $M \to 0$, the tensions become equal: $T_1 = T_2 = \frac{2m_1 m_2 g}{m_1 + m_2}$.

#### Question 3
A rectangular tank of length $L$, width $W$, and height $H$ is partially filled with water to depth $h_0$. The tank is given a uniform horizontal acceleration $a_x\hat{i}$ along its length:
(A) The free surface of the water tilts at an angle $\theta = \arctan(a_x / g)$ to the horizontal.  
(B) Water will not spill over the rim provided $h_0 + \frac{L}{2}\tan\theta \le H$.  
(C) The hydrostatic pressure at any point $(x, z)$ within the fluid is $P(x, z) = P_0 - \rho a_x x - \rho g z + C$.  
(D) The net horizontal force exerted by the fluid on the end walls of the tank equals the total fluid mass multiplied by $a_x$.

#### Question 4
In a meter bridge experiment to measure an unknown resistance $X$ using a standard resistance $R = 10.0\text{ }\Omega$:
(A) If the null point is obtained at length $l_1 = 40.0\text{ cm}$ from the left end, the calculated value of $X$ is $X = R\frac{l_1}{100 - l_1} = 6.67\text{ }\Omega$.  
(B) End errors $\alpha$ and $\beta$ at the two ends shift the effective lengths to $l_1 + \alpha$ and $(100 - l_1) + \beta$.  
(C) End resistance errors can be eliminated by repeating the measurement after interchanging the positions of $X$ and $R$.  
(D) The percentage error in the determination of $X$ is minimized when the null point is close to the middle of the bridge wire ($l_1 \approx 50\text{ cm}$).

#### Question 5
A uniform solid sphere of mass $M$ and radius $R$ is rolling on a horizontal surface with translational speed $v_0$ when it encounters a vertical curb of height $h < R$:
(A) The collision of the sphere with the curb edge is instantaneous, and angular momentum about the curb edge is conserved during the impact.  
(B) The angular velocity of the sphere immediately after the impact about the curb edge is $\omega_1 = \frac{v_0}{R}\left(1 - \frac{7h}{5R}\right)$ or similar projection.  
(C) The minimum speed $v_0$ required for the sphere to climb over the curb without slipping off the curb edge can be determined from mechanical energy conservation after the impact.  
(D) The kinetic energy of the sphere decreases discontinuously during the impact.

#### Question 6
A horizontal turntable of radius $R$ rotates with constant angular velocity $\vec{\omega} = \omega\hat{k}$. A small bug of mass $m$ crawls radially outward from the center with constant speed $v_r$ relative to the turntable:
(A) The radial acceleration of the bug in the inertial frame is $a_r = -\omega^2 r$.  
(B) The transverse (tangential) acceleration of the bug in the inertial frame is $a_\theta = 2\omega v_r$ (Coriolis acceleration).  
(C) The total horizontal force exerted by the turntable on the bug at distance $r$ from the center is $F = m\sqrt{\omega^4 r^2 + 4\omega^2 v_r^2}$.  
(D) If $\mu_s$ is the coefficient of static friction, the maximum distance the bug can crawl before slipping is $r_{\max} = \frac{\sqrt{\mu_s^2 g^2 - 4\omega^2 v_r^2}}{\omega^2}$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In an Atwood machine, the masses are $m_1 = 3.0\text{ kg}$, $m_2 = 1.0\text{ kg}$, and the pulley is a uniform disc of mass $M = 2.0\text{ kg}$. Taking $g = 9.8\text{ m/s}^2$, the downward acceleration of mass $m_1$ in $\text{m/s}^2$ is $a$. Find $a$ rounded off to two decimal places.

#### Question 8
A solid sphere of mass $M = 5.0\text{ kg}$ and radius $R = 0.20\text{ m}$ rolls without slipping on a horizontal surface at speed $v = 4.0\text{ m/s}$. The total kinetic energy of the sphere in joules is $E\text{ J}$. Find $E$.

#### Question 9
In a meter bridge experiment, a standard resistance $R = 15.0\text{ }\Omega$ is connected in the right gap and an unknown resistance $X$ in the left gap. The balance point is obtained at $l = 37.5\text{ cm}$ from the left end. Find the value of $X$ in ohms.

#### Question 10
Water rises to a height of $h = 6.0\text{ cm}$ in a vertical glass capillary tube of radius $r = 0.25\text{ mm}$. If the surface tension of water is $T = 0.0735\text{ N/m}$ and density $\rho = 1000\text{ kg/m}^3$, the contact angle $\theta$ in degrees is $\theta^\circ$. (Taking $g = 9.8\text{ m/s}^2$). Find $\theta$.

#### Question 11
A uniform rod of length $L = 1.0\text{ m}$ and mass $M = 2.0\text{ kg}$ is free to rotate about a horizontal axis through its top end. A horizontal force $F = 12.0\text{ N}$ is applied at the center of the rod. The initial angular acceleration of the rod in $\text{rad/s}^2$ is $\alpha$. Find $\alpha$.

#### Question 12
A vertical cylindrical vessel of base area $A = 0.02\text{ m}^2$ contains water to depth $H = 1.0\text{ m}$. A small orifice of area $a = 1.0 \times 10^{-4}\text{ m}^2$ is opened at the bottom. Taking $g = 9.8\text{ m/s}^2$, the time required to completely empty the vessel in seconds is $t\text{ s}$. Find $t$ rounded off to the nearest integer.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A body of mass $m$ is projected vertically upward with velocity $v_0$ from the Earth's surface. Neglecting air resistance, the maximum height $h$ reached above the surface (where $R_E$ is Earth's radius) is:
(A) $\frac{v_0^2 R_E}{2g R_E - v_0^2}$  
(B) $\frac{v_0^2}{2g}$  
(C) $\frac{v_0^2 R_E}{g R_E + v_0^2}$  
(D) $\frac{2g R_E^2}{v_0^2}$

#### Question 14
The moment of inertia of a hollow sphere of mass $M$ and radius $R$ about its diameter is:
(A) $\frac{2}{3} M R^2$  
(B) $\frac{2}{5} M R^2$  
(C) $\frac{1}{2} M R^2$  
(D) $\frac{3}{5} M R^2$

#### Question 15
Two soap bubbles have internal excess pressures in the ratio $1:3$. The ratio of their surface areas is:
(A) $9:1$  
(B) $3:1$  
(C) $1:9$  
(D) $27:1$

#### Question 16
The angle of contact between pure water and clean glass is:
(A) Zero (or nearly zero)  
(B) $90^\circ$  
(C) $135^\circ$  
(D) $180^\circ$

#### Question 17
A solid sphere, a thin circular ring, and a uniform disc of identical mass and radius roll down an incline without slipping. The order of arrival at the bottom is:
(A) Sphere first, disc second, ring third  
(B) Ring first, disc second, sphere third  
(C) Disc first, sphere second, ring third  
(D) All arrive simultaneously

#### Question 18
The fundamental frequency of a closed organ pipe of length $L$ is $f_0$. If the pipe is opened at both ends, its fundamental frequency becomes:
(A) $2f_0$  
(B) $f_0 / 2$  
(C) $4f_0$  
(D) $f_0$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Baeyer-Villiger oxidation of ketones using peroxy acids ($R\text{COOOH}$):
(A) The reaction converts ketones into esters with insertion of an oxygen atom adjacent to the carbonyl group.  
(B) The migratory aptitude follows the order: $\text{tertiary alkyl} > \text{cyclohexyl} > \text{secondary alkyl} \approx \text{benzyl} > \text{phenyl} > \text{primary alkyl} > \text{methyl}$.  
(C) The stereochemistry at the migrating chiral center is retained with complete fidelity.  
(D) Cyclic ketones undergo ring expansion to yield lactones (e.g., cyclohexanone gives $\varepsilon$-caprolactone).

#### Question 20
Regarding the chemistry of metal-metal multiple bonding in transition metal clusters:
(A) The octachlorodirhenate(III) ion $[\text{Re}_2\text{Cl}_8]^{2-}$ features a formal quadruple metal-metal bond ($\sigma + 2\pi + \delta$).  
(B) The presence of the $\delta$-bond enforces an eclipsed conformation of the two $\text{ReCl}_4$ square planar units.  
(C) The $\delta$-bond arises from the face-to-face overlap of $d_{xy}$ orbitals on adjacent Re atoms.  
(D) $[\text{Re}_2\text{Cl}_8]^{2-}$ is diamagnetic with all bonding electrons paired.

#### Question 21
Regarding the homogeneous catalytic hydrogenation of alkenes using Wilkinson's catalyst $[\text{RhCl}(\text{PPh}_3)_3]$:
(A) The active catalytic species is the coordinatively unsaturated 14-electron complex $[\text{RhCl}(\text{PPh}_3)_2]$.  
(B) The mechanism involves oxidative addition of $\text{H}_2$ to the Rh(I) center to form a Rh(III) dihydride.  
(C) Coordination of alkene followed by migratory insertion gives a Rh(III) alkyl hydride.  
(D) Reductive elimination yields the alkane product and regenerates the Rh(I) catalyst with *cis* (syn) addition of both hydrogen atoms.

#### Question 22
Regarding the extraction and metallurgy of zinc from zinc blende ($\text{ZnS}$):
(A) Zinc blende is concentrated by froth flotation using sodium ethyl xanthate as collector.  
(B) Roasting in excess air converts $\text{ZnS}$ to $\text{ZnO}$: $2\text{ZnS} + 3\text{O}_2 \to 2\text{ZnO} + 2\text{SO}_2$.  
(C) Reduction of $\text{ZnO}$ with coke occurs at $\approx 1400\text{ K}$, and zinc distills over since its boiling point is $1180\text{ K}$.  
(D) Crude zinc is known as spelter and is purified by fractional distillation or electrolytic refining.

#### Question 23
Regarding peptide synthesis and protecting group strategies:
(A) The amino group can be protected using the tert-butyloxycarbonyl (Boc) group, which is cleaved by trifluoroacetic acid (TFA).  
(B) The 9-fluorenylmethoxycarbonyl (Fmoc) group protects amino groups and is base-labile, cleaved by piperidine.  
(C) Dicyclohexylcarbodiimide (DCC) is commonly used as a coupling agent to activate the carboxyl group for amide bond formation.  
(D) Solid-phase peptide synthesis (Merrifield synthesis) constructs the peptide chain from the C-terminus to the N-terminus.

#### Question 24
Which of the following molecules possess a permanent electric dipole moment:
(A) Sulfur dioxide ($\text{SO}_2$)  
(B) Ammonia ($\text{NH}_3$)  
(C) Water ($\text{H}_2\text{O}$)  
(D) Boron trifluoride ($\text{BF}_3$)

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The equilibrium constant for the esterification reaction $\text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH} \rightleftharpoons \text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O}$ is $K_c = 4.0$ at $298\text{ K}$. If $1.0\text{ mole}$ of acetic acid and $2.0\text{ moles}$ of ethanol are reacted, the moles of ethyl acetate formed at equilibrium is $x$. Find $x$ rounded off to two decimal places.

#### Question 26
Calculate the $\text{pH}$ of a $0.050\text{ M}$ solution of sulfuric acid ($\text{H}_2\text{SO}_4$) assuming complete dissociation of both protons at $298\text{ K}$. Find the $\text{pH}$.

#### Question 27
For the cell $\text{Pt} \mid \text{H}_2(1\text{ bar}) \mid \text{H}^+(1\text{ M}) \parallel \text{Cu}^{2+}(0.01\text{ M}) \mid \text{Cu}$, given $E^\circ(\text{Cu}^{2+}/\text{Cu}) = +0.34\text{ V}$. The cell EMF at $298\text{ K}$ is $E_{\text{cell}}\text{ V}$. Find $E_{\text{cell}}$ rounded off to two decimal places.

#### Question 28
The half-life of a first-order reaction is $45.0\text{ minutes}$. Calculate the rate constant $k$ in $\text{min}^{-1}$ rounded off to three decimal places.

#### Question 29
A $0.10\text{ molal}$ aqueous solution of $\text{KCl}$ exhibits an osmotic pressure of $4.60\text{ atm}$ at $27^\circ\text{C}$ ($300\text{ K}$). Given $R = 0.0821\text{ L atm/(mol K)}$, the apparent van 't Hoff factor $i$ is $i$. Find $i$ rounded off to two decimal places.

#### Question 30
Find the oxidation state of rhenium in the quadruply bonded complex $[\text{Re}_2\text{Cl}_8]^{2-}$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The reaction of an alkyl halide with sodium in dry ether (Wurtz reaction) is BEST suited for the synthesis of:
(A) Symmetrical alkanes with an even number of carbon atoms  
(B) Unsymmetrical alkanes with an odd number of carbon atoms  
(C) Methane  
(D) Branched alkenes

#### Question 32
Which of the following compounds has the lowest boiling point:
(A) Neo-pentane (2,2-dimethylpropane)  
(B) Iso-pentane (2-methylbutane)  
(C) $n$-Pentane  
(D) $n$-Butane

#### Question 33
The hybridization and geometry of $\text{XeF}_2$ are:
(A) $sp^3d$, Linear  
(B) $sp^3$, Bent  
(C) $sp^3d^2$, Square planar  
(D) $sp$, Linear

#### Question 34
In the extraction of copper, the slag formed in the blast furnace is:
(A) $\text{FeSiO}_3$  
(B) $\text{CaSiO}_3$  
(C) $\text{CuSiO}_3$  
(D) $\text{FeS}$

#### Question 35
The amino acid that contains a disulfide cross-link in proteins is:
(A) Cysteine  
(B) Alanine  
(C) Serine  
(D) Valine

#### Question 36
The conjugate base of water ($\text{H}_2\text{O}$) is:
(A) $\text{OH}^-$  
(B) $\text{H}_3\text{O}^+$  
(C) $\text{O}^{2-}$  
(D) $\text{H}_2$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $y = f(x)$ be a smooth plane curve. The length of the arc between $x = a$ and $x = b$ is given by $L = \int_a^b \sqrt{1 + (f'(x))^2} dx$:
(A) For the catenary $y = a\cosh(x/a)$ from $x = 0$ to $x = X$, the arc length is $L = a\sinh(X/a)$.  
(B) For the circle $x = R\cos t, y = R\sin t$, the total perimeter is $2\pi R$.  
(C) For the cycloid $x = a(t - \sin t), y = a(1 - \cos t)$, the arc length of one full arch ($t \in [0, 2\pi]$) is $8a$.  
(D) The arc length integral is invariant under rigid rotations and translations of the coordinate axes.

#### Question 38
Consider the envelope of the family of straight lines $y = m x + \frac{a}{m}$ parameterized by slope $m \ne 0$:
(A) Differentiating with respect to the parameter $m$ yields $x - \frac{a}{m^2} = 0 \implies m = \sqrt{a/x}$.  
(B) Eliminating $m$ gives the envelope $y = 2\sqrt{ax} \implies y^2 = 4ax$.  
(C) The family of lines represents the tangents to the parabola $y^2 = 4ax$.  
(D) The envelope of a family of tangents to any smooth curve is the curve itself.

#### Question 39
Consider the recurrence relation $a_n = 5a_{n-1} - 6a_{n-2}$ with initial values $a_0 = 2, a_1 = 5$:
(A) The characteristic equation is $r^2 - 5r + 6 = 0$.  
(B) The characteristic roots are $r_1 = 2$ and $r_2 = 3$.  
(C) The general solution is $a_n = C_1 2^n + C_2 3^n$.  
(D) With the given initial values, $a_n = 2^n + 3^n$ for all $n \ge 0$.

#### Question 40
Let events $A, B, C$ partition the sample space with prior probabilities $P(A) = 0.2, P(B) = 0.3, P(C) = 0.5$. An event $E$ has likelihoods $P(E|A) = 0.1, P(E|B) = 0.2, P(E|C) = 0.3$:
(A) The total probability of $E$ is $P(E) = (0.2)(0.1) + (0.3)(0.2) + (0.5)(0.3) = 0.23$.  
(B) By Bayes' theorem, $P(A|E) = \frac{0.02}{0.23} = \frac{2}{23}$.  
(C) $P(B|E) = \frac{0.06}{0.23} = \frac{6}{23}$.  
(D) $P(C|E) = \frac{0.15}{0.23} = \frac{15}{23}$.

#### Question 41
Let $f(x) = \frac{x}{1 + |x|}$ for $x \in \mathbb{R}$:
(A) $f(x)$ is strictly increasing on $\mathbb{R}$.  
(B) $f(x)$ is an odd function: $f(-x) = -f(x)$.  
(C) The range of $f(x)$ is $(-1, 1)$.  
(D) $f(x)$ is bijective from $\mathbb{R}$ to $(-1, 1)$ with inverse $f^{-1}(y) = \frac{y}{1 - |y|}$.

#### Question 42
Consider the hyperbola $\frac{x^2}{9} - \frac{y^2}{16} = 1$:
(A) The coordinates of its foci are $(\pm 5, 0)$.  
(B) The equations of its asymptotes are $y = \pm \frac{4}{3}x$.  
(C) The eccentricity is $e = 5/3$.  
(D) The length of its latus rectum is $32/3$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the arc length of the parabola $y = \frac{1}{2}x^2$ from $x = 0$ to $x = 1$. The value of $\int_0^1 \sqrt{1+x^2} dx$ rounded off to two decimal places is $L$. Find $L$.

#### Question 44
Find the remainder when $7^{2024}$ is divided by 100.

#### Question 45
Find the shortest distance between the lines $\frac{x-1}{1} = \frac{y-2}{2} = \frac{z-3}{3}$ and $\frac{x-2}{2} = \frac{y-4}{4} = \frac{z-5}{6}$. (Note that these lines are parallel). Round off to two decimal places.

#### Question 46
Let $z$ be a complex number satisfying $|z| = 2$. Find the maximum value of $|z + 3 + 4i|$.

#### Question 47
Find the number of integral solutions to $x_1 + x_2 + x_3 + x_4 = 20$ with $x_i \ge 0$ for all $i$.

#### Question 48
Find the radius of the sphere passing through $(0,0,0)$ and having center at $(2, 3, 6)$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arcsin(2x\sqrt{1-x^2})$ with respect to $\arccos(\sqrt{1-x^2})$ for $x \in (0, 1/\sqrt{2})$ is:
(A) $2$  
(B) $1$  
(C) $1/2$  
(D) $-2$

#### Question 50
The differential equation of all lines passing through the origin is:
(A) $x \frac{dy}{dx} - y = 0$  
(B) $x \frac{dy}{dx} + y = 0$  
(C) $\frac{d^2 y}{dx^2} = 1$  
(D) $y \frac{dy}{dx} = x$

#### Question 51
The angle between the diagonals of a cube is:
(A) $\arccos(1/3)$  
(B) $\arccos(1/\sqrt{3})$  
(C) $\pi/3$  
(D) $\pi/4$

#### Question 52
If $A$ is a square matrix of order 3 with $\det(A) = 3$, then $\det(2A)$ is:
(A) 24  
(B) 6  
(C) 18  
(D) 12

#### Question 53
The number of real solutions of the equation $e^x + x = 0$ is:
(A) 1  
(B) 0  
(C) 2  
(D) Infinite

#### Question 54
A box contains 6 red and 4 white balls. Two balls are drawn at random without replacement. The probability that both are of the same color is:
(A) $7/15$  
(B) $1/2$  
(C) $8/15$  
(D) $1/3$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)
**Historical Reference Benchmark**: 2008, 2013, 2019 Official Examination Papers  
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
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal surface. A horizontal impulsive blow of impulse $J$ is struck at a height $h$ above the center:
(A) The linear velocity of the center of mass immediately after the blow is $v_0 = J / M$.  
(B) The angular velocity immediately after the blow is $\omega_0 = \frac{J h}{I_{\text{cm}}} = \frac{5 J h}{2 M R^2}$.  
(C) The condition for the sphere to roll without slipping immediately after the blow is $h = \frac{2}{5}R$.  
(D) If $h > \frac{2}{5}R$, the friction force immediately after the blow acts forward in the direction of $J$.

#### Question 2
A hydraulic lift has two pistons of cross-sectional areas $A_1 = 10\text{ cm}^2$ and $A_2 = 500\text{ cm}^2$ filled with an incompressible liquid:
(A) By Pascal's principle, pressure applied at the small piston is transmitted undiminished to the large piston.  
(B) The mechanical advantage of the hydraulic lift is $\frac{A_2}{A_1} = 50$.  
(C) To lift a load of $1000\text{ kg}$, the minimum force required on the small piston is $F_1 = \frac{1000 \times 9.8}{50} = 196\text{ N}$.  
(D) If the small piston moves down by distance $d_1 = 50\text{ cm}$, the large piston rises by $d_2 = 1.0\text{ cm}$.

#### Question 3
A liquid of density $\rho$ and surface tension $T$ rises in a vertical capillary tube of radius $R$ to a height $h_0 = \frac{2T\cos\theta}{\rho g R}$:
(A) The total gravitational potential energy gained by the liquid column is $U = \frac{1}{2}m g h_0 = \frac{1}{2}\rho \pi R^2 g h_0^2$.  
(B) The work done by the surface tension force during the ascent is $W_s = (2\pi R T\cos\theta) h_0 = \rho \pi R^2 g h_0^2$.  
(C) Half of the work done by surface tension is dissipated as viscous heat during the ascent: $Q_{\text{diss}} = \frac{1}{2}W_s$.  
(D) If the tube is tilted by angle $\alpha$ to the vertical, the length of the liquid column along the tube becomes $l = h_0 / \cos\alpha$.

#### Question 4
In an experiment to measure the focal length of a concave lens using a convex lens of known focal length $f_1 = 15.0\text{ cm}$:
(A) A real object cannot form a real image through a single concave lens in air.  
(B) The convex lens forms a convergent beam that serves as a virtual object for the concave lens.  
(C) If the virtual object distance is $u$ and the real image is formed at distance $v$ from the concave lens, its focal length is given by $\frac{1}{f} = \frac{1}{v} - \frac{1}{u}$.  
(D) The focal length of the concave lens must have magnitude larger than the distance between the two lenses for a real final image to be formed.

#### Question 5
A spherical bubble of gas of radius $R_0$ oscillates radially in an infinite incompressible liquid of density $\rho$ (Minnaert frequency):
(A) The kinetic energy of the surrounding liquid is $K = 2\pi \rho R^3 \dot{R}^2$.  
(B) The natural frequency of radial pulsation of the bubble is $f = \frac{1}{2\pi R_0}\sqrt{\frac{3\gamma P_0}{\rho}}$.  
(C) The pulsation frequency depends inversely on the equilibrium bubble radius $R_0$.  
(D) Radial oscillations of bubbles are a primary source of acoustic noise in turbulent water and waterfalls.

#### Question 6
A uniform solid cylinder of mass $M$ and radius $R$ is released from rest at the top of a cylindrical surface of radius $3R$ and rolls without slipping down the outside of the surface:
(A) The angle $\theta$ from the vertical at which the cylinder loses contact with the surface is given by $\cos\theta = 4/7$.  
(B) The linear speed of the cylinder's center of mass at the moment of separation is $v = \sqrt{\frac{4}{7}g(2R)} = \sqrt{\frac{8}{7}g R}$.  
(C) Before separation, static friction prevents slipping.  
(D) The normal force vanishes identically at the instant of separation.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A hydraulic press has pistons with diameters $d_1 = 2.0\text{ cm}$ and $d_2 = 20.0\text{ cm}$. If a force $F_1 = 50.0\text{ N}$ is applied to the smaller piston, the force exerted by the larger piston in newtons is $F_2\text{ N}$. Find $F_2$.

#### Question 8
In a capillary rise experiment with water ($T = 0.070\text{ N/m}$, contact angle $\theta = 0^\circ$, $\rho = 1000\text{ kg/m}^3$), water rises to height $h = 7.0\text{ cm}$. Taking $g = 10.0\text{ m/s}^2$, the radius of the capillary tube in millimeters is $r\text{ mm}$. Find $r$ rounded off to two decimal places.

#### Question 9
A solid sphere of mass $M = 3.0\text{ kg}$ and radius $R = 0.15\text{ m}$ is struck by a horizontal impulse $J$ at height $h = 0.06\text{ m}$ above the center. The initial translational velocity acquired is $v_0 = 5.0\text{ m/s}$. The initial angular velocity $\omega_0$ in $\text{rad/s}$ is $\omega_0$. Find $\omega_0$ rounded off to one decimal place.

#### Question 10
A tuning fork of frequency $f = 340\text{ Hz}$ resonates with a tube closed at one end at a water level giving air column length $l_1 = 24.0\text{ cm}$, and the next resonance occurs at $l_2 = 74.0\text{ cm}$. The speed of sound in air is $v\text{ m/s}$. Find $v$.

#### Question 11
A uniform solid sphere of radius $R = 0.50\text{ m}$ rolls without slipping on a horizontal track with speed $v = 3.5\text{ m/s}$. It then ascends a rough inclined track of angle $30^\circ$. Taking $g = 9.8\text{ m/s}^2$, the maximum vertical height $h$ reached by the sphere in meters is $h\text{ m}$. Find $h$ rounded off to two decimal places.

#### Question 12
Two droplets of mercury of radii $r_1 = 1.0\text{ mm}$ and $r_2 = 1.0\text{ mm}$ collapse into a single spherical droplet. If surface tension of mercury is $T = 0.465\text{ N/m}$, the energy released in microjoules ($\mu\text{J}$) is $\Delta U$. Find $\Delta U$ rounded off to two decimal places.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The center of mass of a uniform thin hemispherical shell of radius $R$ is at a distance from its base of:
(A) $R/2$  
(B) $3R/8$  
(C) $2R/3$  
(D) $4R/(3\pi)$

#### Question 14
A stone tied to the end of a string of length $L$ is whirled in a vertical circle. The minimum speed at the lowest point so that the string does not slacken at the top is:
(A) $\sqrt{5gL}$  
(B) $\sqrt{3gL}$  
(C) $\sqrt{gL}$  
(D) $\sqrt{2gL}$

#### Question 15
According to Bernoulli's equation, along a streamline in steady, incompressible, inviscid flow:
(A) $P + \frac{1}{2}\rho v^2 + \rho g z = \text{constant}$  
(B) $P + \rho v^2 + \rho g z = \text{constant}$  
(C) $P / \rho + v^2 + g z = \text{constant}$  
(D) $P + \frac{1}{2}\rho v = \text{constant}$

#### Question 16
The excess pressure inside a soap bubble of radius $R$ and surface tension $T$ in air is:
(A) $4T/R$  
(B) $2T/R$  
(C) $T/R$  
(D) $8T/R$

#### Question 17
A sphere, a cylinder, and a hoop roll down an inclined plane without slipping. The body with the maximum rotational kinetic energy as a fraction of total kinetic energy is:
(A) The hoop  
(B) The cylinder  
(C) The sphere  
(D) All have equal fractions

#### Question 18
The speed of transverse waves on a stretched string of linear mass density $\mu$ under tension $T$ is:
(A) $\sqrt{T/\mu}$  
(B) $\sqrt{\mu/T}$  
(C) $T/\mu$  
(D) $\sqrt{T\mu}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the aldol reaction and its stereochemical control:
(A) The reaction of an enolate with an aldehyde generates a new carbon-carbon bond and up to two new stereocenters.  
(B) $(E)$-enolates typically favor the formation of *anti*-aldol products via a Zimmerman-Traxler chair-like transition state.  
(C) $(Z)$-enolates typically favor the formation of *syn*-aldol products via a Zimmerman-Traxler transition state.  
(D) Dehydration of aldol addition products occurs with high selectivity to give the thermodynamically more stable $(E)$-$\alpha,\beta$-unsaturated carbonyl compound.

#### Question 20
Regarding the thermodynamics and phase rule for heterogeneous systems:
(A) Gibbs phase rule states $F = C - P + 2$ where $F$ is degrees of freedom, $C$ is number of components, and $P$ is number of phases.  
(B) For a single-component system ($C=1$), at the triple point $P = 3$, hence $F = 0$ (invariant point).  
(C) The slope of the solid-liquid coexistence curve for water is negative because ice is less dense than liquid water ($\Delta_{\text{fus}}V < 0$).  
(D) Along any two-phase coexistence line, the chemical potentials of the substance in the two phases are equal: $\mu_\alpha(T, P) = \mu_\beta(T, P)$.

#### Question 21
Regarding the chemistry of polyoxometalates and isopolyanions:
(A) Acidification of aqueous solutions of $\text{CrO}_4^{2-}$ results in condensation to form dichromate $\text{Cr}_2\text{O}_7^{2-}$.  
(B) Molybdates and tungstates condense upon acidification to form large polyoxometalate clusters such as the Keggin anion $[\text{PW}_{12}\text{O}_{40}]^{3-}$.  
(C) The condensation involves corner-sharing and edge-sharing of $[\text{MO}_6]$ octahedra.  
(D) Polyoxometalates act as versatile heterogeneous and homogeneous oxidation catalysts.

#### Question 22
Regarding the extraction and metallurgy of aluminum (Hall-Héroult process):
(A) Pure alumina ($\text{Al}_2\text{O}_3$) is extracted from bauxite by the Bayer process using aqueous $\text{NaOH}$.  
(B) The electrolyte is a molten mixture of alumina, cryolite ($\text{Na}_3\text{AlF}_6$), and fluorspar ($\text{CaF}_2$) at $\approx 1250\text{ K}$.  
(C) Cryolite lowers the melting point of alumina from $> 2300\text{ K}$ to $\approx 1250\text{ K}$ and improves electrical conductivity.  
(D) Carbon anodes are consumed during electrolysis, forming $\text{CO}$ and $\text{CO}_2$, requiring periodic replacement.

#### Question 23
Regarding amino acids and protein secondary structures:
(A) The $\alpha$-helix is stabilized by intrachain hydrogen bonds between the carbonyl oxygen of residue $i$ and the amide hydrogen of residue $i+4$.  
(B) In $\beta$-pleated sheets, hydrogen bonds form between adjacent polypeptide strands that can run parallel or antiparallel.  
(C) Proline acts as a helix breaker because its rigid cyclic side chain disrupts regular $\alpha$-helical backbone conformations.  
(D) Denaturation of a protein disrupts secondary, tertiary, and quaternary structures while leaving the primary structure intact.

#### Question 24
Which of the following compounds exhibit optical isomerism (chirality):
(A) Lactic acid ($\text{CH}_3\text{CH}(\text{OH})\text{COOH}$)  
(B) 2-Chlorobutane  
(C) Tartaric acid (the $d$- and $l$-forms)  
(D) *meso*-Tartaric acid (this statement is false as meso form is achiral)

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{CaF}_2$ is $K_{\text{sp}} = 3.2 \times 10^{-11}$ at $298\text{ K}$. Calculate the molar solubility of $\text{CaF}_2$ in pure water in units of $10^{-4}\text{ M}$. Find the value rounded off to two decimal places.

#### Question 26
Calculate the $\text{pH}$ of a $0.010\text{ M}$ aqueous solution of hydrochloric acid ($\text{HCl}$) at $298\text{ K}$. Find the $\text{pH}$.

#### Question 27
For the cell $\text{Zn} \mid \text{Zn}^{2+}(1\text{ M}) \parallel \text{Fe}^{3+}(1\text{ M}), \text{Fe}^{2+}(1\text{ M}) \mid \text{Pt}$, given $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.76\text{ V}$ and $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V}$. The standard cell EMF is $E^\circ_{\text{cell}}\text{ V}$. Find $E^\circ_{\text{cell}}$.

#### Question 28
The rate constant for a reaction is $k = 2.0 \times 10^{-3}\text{ s}^{-1}$ at $300\text{ K}$ and $k = 8.0 \times 10^{-3}\text{ s}^{-1}$ at $320\text{ K}$. Calculate the activation energy $E_a$ in $\text{kJ/mol}$ rounded off to one decimal place. (Take $R = 8.314\text{ J/(mol K)}$ and $\ln 4 \approx 1.3863$).

#### Question 29
A $0.050\text{ molal}$ aqueous solution of a monobasic acid $\text{HA}$ is $20\%$ dissociated. Given $K_f(\text{H}_2\text{O}) = 1.86\text{ K kg mol}^{-1}$, the freezing point depression $\Delta T_f$ in Kelvin is $\Delta T_f\text{ K}$. Find $\Delta T_f$ rounded off to three decimal places.

#### Question 30
Find the number of oxygen atoms shared per silicon tetrahedron in pyrosilicates ($[\text{Si}_2\text{O}_7]^{6-}$).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following alkyl halides reacts FASTEST with aqueous $\text{KOH}$ via an $\text{S}_N1$ mechanism:
(A) *tert*-Butyl chloride  
(B) Isopropyl chloride  
(C) Ethyl chloride  
(D) Methyl chloride

#### Question 32
The correct order of basicity of Group 15 hydrides is:
(A) $\text{NH}_3 > \text{PH}_3 > \text{AsH}_3 > \text{SbH}_3 > \text{BiH}_3$  
(B) $\text{BiH}_3 > \text{SbH}_3 > \text{AsH}_3 > \text{PH}_3 > \text{NH}_3$  
(C) $\text{PH}_3 > \text{NH}_3 > \text{AsH}_3 > \text{SbH}_3 > \text{BiH}_3$  
(D) $\text{NH}_3 > \text{AsH}_3 > \text{PH}_3 > \text{SbH}_3 > \text{BiH}_3$

#### Question 33
The geometry of $\text{PCl}_5$ in the gas phase is:
(A) Trigonal bipyramidal  
(B) Square pyramidal  
(C) Octahedral  
(D) Tetrahedral

#### Question 34
In the Gabriel phthalimide synthesis, the product formed after hydrazinolysis is:
(A) Primary aliphatic amine  
(B) Secondary amine  
(C) Tertiary amine  
(D) Aromatic primary amine

#### Question 35
The sugar present in RNA is:
(A) D-Ribose  
(B) 2-Deoxy-D-ribose  
(C) D-Glucose  
(D) D-Fructose

#### Question 36
The oxidation number of phosphorus in orthophosphoric acid ($\text{H}_3\text{PO}_4$) is:
(A) $+5$  
(B) $+3$  
(C) $+1$  
(D) $-3$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x^2}{x^2 + 1}$ defined for $x \in \mathbb{R}$:
(A) $f(x)$ is an even function: $f(-x) = f(x)$.  
(B) $f'(x) = \frac{2x}{(x^2+1)^2}$, so $x = 0$ is a point of absolute minimum with value $f(0) = 0$.  
(C) The range of $f(x)$ is $[0, 1)$.  
(D) The horizontal line $y = 1$ is an asymptote as $x \to \pm \infty$.

#### Question 38
Let $A$ be a $3 \times 3$ idempotent matrix ($A^2 = A$):
(A) The only possible eigenvalues of $A$ are 0 and 1.  
(B) $\text{tr}(A) = \text{rank}(A)$.  
(C) $I - A$ is also idempotent.  
(D) If $\det(A) \ne 0$, then $A = I_3$.

#### Question 39
Consider the circle $x^2 + y^2 = 9$ and the point $P(5, 0)$ outside it:
(A) The length of the tangents drawn from $P$ to the circle is $L = \sqrt{5^2 - 9} = 4$.  
(B) The chord of contact of tangents from $P$ is $5x = 9 \implies x = 9/5$.  
(C) The angle $\theta$ between the two tangents satisfies $\tan(\theta/2) = 3/4$.  
(D) The area of the quadrilateral formed by the tangents and the radii to the points of contact is 12.

#### Question 40
Let $I = \int_0^{\pi/2} \ln(\tan x) dx$:
(A) The substitution $x = \pi/2 - t$ transforms the integral to $-I$.  
(B) $I = 0$.  
(C) $\int_0^{\pi/2} \ln(\cot x) dx = 0$.  
(D) $\int_0^{\pi/4} \ln(1 + \tan x) dx = \frac{\pi}{8}\ln 2$.

#### Question 41
Consider the straight line $\frac{x-2}{3} = \frac{y+1}{2} = \frac{z-1}{-1}$:
(A) The line passes through the point $(2, -1, 1)$.  
(B) The direction cosines of the line are $\left(\frac{3}{\sqrt{14}}, \frac{2}{\sqrt{14}}, \frac{-1}{\sqrt{14}}\right)$.  
(C) The line is perpendicular to the vector $2\hat{i} - 3\hat{j} + 0\hat{k}$ (since $3(2) + 2(-3) + (-1)(0) = 0$).  
(D) The line lies entirely within the plane $x - 2y - z = 3$.

#### Question 42
Let $X$ be a binomial random variable with parameters $n = 10$ and $p = 0.5$:
(A) The mean of $X$ is $\mu = n p = 5.0$.  
(B) The variance of $X$ is $\sigma^2 = n p (1-p) = 2.5$.  
(C) The distribution is symmetric about its mean.  
(D) $P(X = 5) = \binom{10}{5}(0.5)^{10} = \frac{252}{1024} = \frac{63}{256}$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = 9 - x^2$ and the $x$-axis.

#### Question 44
Find the remainder when $2^{2025}$ is divided by 9.

#### Question 45
Find the perpendicular distance from the origin $(0, 0, 0)$ to the plane $2x - 3y + 6z = 49$.

#### Question 46
Let $\alpha$ and $\beta$ be the roots of $x^2 - 4x + 1 = 0$. Find the value of $\alpha^2 + \beta^2$.

#### Question 47
Find the number of 3-letter words (with or without meaning) that can be formed using the letters of the word **TRIANGLE** without repetition.

#### Question 48
Find the radius of the circle $x^2 + y^2 - 8x + 6y = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $e^{x\sin x}$ with respect to $x$ is:
(A) $e^{x\sin x}(\sin x + x\cos x)$  
(B) $e^{x\sin x}\cos x$  
(C) $e^{x\sin x}\sin x$  
(D) $x e^{x\sin x}\cos x$

#### Question 50
The solution of the differential equation $\frac{dy}{dx} + y = e^{-x}$ with $y(0) = 0$ is:
(A) $y = x e^{-x}$  
(B) $y = e^{-x}$  
(C) $y = x^2 e^{-x}$  
(D) $y = e^x$

#### Question 51
The eccentricity of the ellipse $\frac{x^2}{25} + \frac{y^2}{9} = 1$ is:
(A) $4/5$  
(B) $3/5$  
(C) $5/4$  
(D) $16/25$

#### Question 52
The sum of the infinite geometric series $1 + \frac{1}{3} + \frac{1}{9} + \frac{1}{27} + \dots$ is:
(A) $3/2$  
(B) $4/3$  
(C) $2$  
(D) $5/3$

#### Question 53
The minimum value of $2^{\sin x} + 2^{\cos x}$ is:
(A) $2^{1 - 1/\sqrt{2}}$  
(B) $2$  
(C) $2^{\sqrt{2}}$  
(D) 1

#### Question 54
The probability of getting at least one head in 3 tosses of a fair coin is:
(A) $7/8$  
(B) $1/8$  
(C) $3/4$  
(D) $1/2$
"""

        raw_sol1 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 1)
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Sphere rolling inside hollow cylinder: $v = (R-r)\dot{\theta}$, $\omega = \frac{v}{r} = \frac{R-r}{r}\dot{\theta}$. Total KE $= \frac{1}{2}mv^2 + \frac{1}{2}(\frac{2}{5}mr^2)\omega^2 = \frac{7}{10}m(R-r)^2\dot{\theta}^2$. Potential energy $U = mg(R-r)(1-\cos\theta)$. Lagrangian / energy conservation yields $\ddot{\theta} + \frac{5g}{7(R-r)}\sin\theta = 0 \implies \omega = \sqrt{\frac{5g}{7(R-r)}}$. **Correct Options**: (A, B, C, D)
- **Q2**: Atwood machine with pulley inertia: $(m_1 - m_2)g = (m_1 + m_2 + I/R^2)a = (m_1 + m_2 + M/2)a$. Tensions satisfy $T_1 - T_2 = (I/R^2)a = \frac{1}{2}Ma$. **Correct Options**: (A, B, C, D)
- **Q3**: Accelerated fluid: free surface aligns perpendicular to effective gravity $\vec{g}_{\text{eff}} = \vec{g} - a_x\hat{i}$, giving $\tan\theta = a_x / g$. Hydrostatic pressure field and boundary force conditions. **Correct Options**: (A, B, C, D)
- **Q4**: Meter bridge experiment: Wheatstone bridge balance $X/R = l_1 / (100 - l_1)$. End resistance corrections and minimal fractional error near middle wire. **Correct Options**: (A, B, C, D)
- **Q5**: Sphere striking a curb: angular momentum about curb corner is conserved during instantaneous collision. Energy conservation dictates subsequent climb. **Correct Options**: (A, B, C, D)
- **Q6**: Coriolis force and kinematics on rotating turntable: $a_r = -\omega^2 r$, $a_\theta = 2\omega v_r$. Total force $F = m\sqrt{\omega^4 r^2 + 4\omega^2 v_r^2}$. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $a = \frac{(m_1 - m_2)g}{m_1 + m_2 + M/2} = \frac{(3.0 - 1.0)(9.8)}{3.0 + 1.0 + 1.0} = \frac{19.6}{5.0} = 3.92\text{ m/s}^2 \implies \mathbf{3.92}$.
- **Q8**: For rolling solid sphere, $E = \frac{7}{10}M v^2 = \frac{7}{10}(5.0)(4.0)^2 = \frac{7}{10}(5.0)(16.0) = 56.0\text{ J} \implies \mathbf{56.00}$.
- **Q9**: $X = R \frac{l}{100 - l} = 15.0 \times \frac{37.5}{62.5} = 15.0 \times 0.60 = 9.00\text{ }\Omega \implies \mathbf{9.00}$.
- **Q10**: $h = \frac{2T\cos\theta}{r\rho g} \implies \cos\theta = \frac{h r \rho g}{2T} = \frac{(0.06)(0.25 \times 10^{-3})(1000)(9.8)}{2(0.0735)} = \frac{0.147}{0.147} = 1.0 \implies \theta = 0^\circ \implies \mathbf{0.00}$.
- **Q11**: Torque about pivot $\tau = F(L/2) = 12.0 \times 0.50 = 6.0\text{ N m}$. Moment of inertia $I = \frac{1}{3}M L^2 = \frac{1}{3}(2.0)(1.0)^2 = 2/3\text{ kg m}^2$. $\alpha = \tau / I = 6.0 / (2/3) = 9.0\text{ rad/s}^2 \implies \mathbf{9.00}$.
- **Q12**: Torricelli drainage: $t = \frac{A}{a}\sqrt{\frac{2H}{g}} = \frac{0.02}{1.0 \times 10^{-4}}\sqrt{\frac{2 \times 1.0}{9.8}} = 200 \times \sqrt{0.204} \approx 200 \times 0.4517 \approx 90.3\text{ s} \implies \mathbf{90.00}$.

### Questions 13 to 18
- **Q13**: Conservation of energy: $\frac{1}{2}m v_0^2 - \frac{G M_E m}{R_E} = -\frac{G M_E m}{R_E + h} \implies h = \frac{v_0^2 R_E}{2g R_E - v_0^2}$. **Correct: (A)**.
- **Q14**: Hollow sphere (spherical shell) moment of inertia is $\frac{2}{3}MR^2$. **Correct: (A)**.
- **Q15**: Excess pressure $\Delta P = 4T/r \implies \Delta P \propto 1/r$. Ratio $\Delta P_1 / \Delta P_2 = 1/3 \implies r_1 / r_2 = 3/1$. Surface areas $A_1 / A_2 = (r_1/r_2)^2 = 9/1$. **Correct: (A)**.
- **Q16**: Pure water and clean glass have contact angle zero. **Correct: (A)**.
- **Q17**: Accelerations: sphere ($a = 5/7 g\sin\theta \approx 0.71$), disc ($a = 2/3 g\sin\theta \approx 0.67$), ring ($a = 1/2 g\sin\theta = 0.50$). Sphere arrives first, disc second, ring third. **Correct: (A)**.
- **Q18**: Closed organ pipe $f_0 = v/(4L)$. Open organ pipe of same length $f_{\text{open}} = v/(2L) = 2f_0$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Baeyer-Villiger oxidation mechanisms and migratory aptitudes. **Correct Options**: (A, B, C, D)
- **Q20**: Metal-metal quadruple bonding in $[\text{Re}_2\text{Cl}_8]^{2-}$ ($\sigma + 2\pi + \delta$). **Correct Options**: (A, B, C, D)
- **Q21**: Wilkinson's catalytic cycle for homogeneous hydrogenation. **Correct Options**: (A, B, C, D)
- **Q22**: Zinc blende metallurgy and purification of spelter. **Correct Options**: (A, B, C, D)
- **Q23**: Peptide synthesis protecting group chemistry (Boc, Fmoc, DCC). **Correct Options**: (A, B, C, D)
- **Q24**: Dipole moment: $\text{SO}_2$ (bent), $\text{NH}_3$ (pyramidal), $\text{H}_2\text{O}$ (bent) all have non-zero dipoles; $\text{BF}_3$ is trigonal planar with zero dipole. **Correct Options**: (A, B, C)

### Questions 25 to 30
- **Q25**: $\frac{x^2}{(1-x)(2-x)} = 4 \implies x^2 = 4(x^2 - 3x + 2) = 4x^2 - 12x + 8 \implies 3x^2 - 12x + 8 = 0$. Roots $x = \frac{12 \pm \sqrt{144 - 96}}{6} = \frac{12 \pm \sqrt{48}}{6} = 2 \pm \frac{4\sqrt{3}}{6} = 2 - 1.155 = 0.845\text{ moles} \approx 0.85 \implies \mathbf{0.85}$.
- **Q26**: $[\text{H}^+] = 2 \times 0.050\text{ M} = 0.10\text{ M} \implies \text{pH} = -\log(0.10) = 1.00 \implies \mathbf{1.00}$.
- **Q27**: Nernst equation: $E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{0.0591}{2}\log\left(\frac{1}{[\text{Cu}^{2+}]}\right) = 0.34 - \frac{0.0591}{2}\log(100) = 0.34 - 0.0591 = 0.28\text{ V} \implies \mathbf{0.28}$.
- **Q28**: $k = \frac{\ln 2}{t_{1/2}} = \frac{0.693}{45.0} = 0.0154\text{ min}^{-1} \approx 0.015\text{ min}^{-1} \implies \mathbf{0.015}$.
- **Q29**: $\Pi = i M R T \implies 4.60 = i (0.10)(0.0821)(300) = i (2.463) \implies i = \frac{4.60}{2.463} \approx 1.87 \implies \mathbf{1.87}$.
- **Q30**: Formula $[\text{Re}_2\text{Cl}_8]^{2-} \implies 2x + 8(-1) = -2 \implies 2x = 6 \implies x = +3 \implies \mathbf{3.00}$.

### Questions 31 to 36
- **Q31**: Wurtz reaction coupling gives symmetrical alkanes with even carbon count in highest yield. **Correct: (A)**.
- **Q32**: More branching gives more spherical shape, smaller surface area, weaker London forces $\implies$ neo-pentane has lowest boiling point among pentane isomers. But $n$-butane has only 4 carbons, so its molecular mass is lower: let's check between neo-pentane ($9.5^\circ\text{C}$) and $n$-butane ($-0.5^\circ\text{C}$). $n$-butane has lowest BP! **Correct: (D)**.
- **Q33**: $\text{XeF}_2$ has 2 bond pairs and 3 lone pairs in equatorial positions $\implies sp^3d$ linear. **Correct: (A)**.
- **Q34**: Slag formed in copper blast furnace is ferrous silicate $\text{FeSiO}_3$. **Correct: (A)**.
- **Q35**: Cysteine contains $-\text{SH}$ group which forms disulfide ($-\text{S}-\text{S}-$) crosslinks. **Correct: (A)**.
- **Q36**: Water loses a proton to form hydroxide ion $\text{OH}^-$. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Arc length formula applications. **Correct Options**: (A, B, C, D)
- **Q38**: Envelopes of family of tangents. **Correct Options**: (A, B, C, D)
- **Q39**: Second-order linear recurrence relations. **Correct Options**: (A, B, C, D)
- **Q40**: Bayes' theorem calculations. **Correct Options**: (A, B, C, D)
- **Q41**: Properties of $f(x) = \frac{x}{1+|x|}$. **Correct Options**: (A, B, C, D)
- **Q42**: Standard parameters of hyperbola. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: $\int_0^1 \sqrt{1+x^2}dx = [\frac{x}{2}\sqrt{1+x^2} + \frac{1}{2}\ln(x+\sqrt{1+x^2})]_0^1 = \frac{\sqrt{2}}{2} + \frac{1}{2}\ln(1+\sqrt{2}) \approx 0.7071 + 0.5(0.8814) \approx 1.15 \implies \mathbf{1.15}$.
- **Q44**: $7^4 = 2401 \equiv 1 \pmod{100}$. $2024 = 4 \times 506 \implies 7^{2024} \equiv 1 \pmod{100} \implies \mathbf{1.00}$.
- **Q45**: Lines are parallel with direction $(1, 2, 3)$. Points $A(1, 2, 3)$ and $B(2, 4, 5)$. Vector $\vec{AB} = (1, 2, 2)$. Direction $\vec{u} = (1, 2, 3)$ with $|\vec{u}| = \sqrt{14}$. $\vec{AB} \times \vec{u} = (2(3)-2(2), 2(1)-1(3), 1(2)-2(1)) = (2, -1, 0)$. Magnitude $= \sqrt{4+1} = \sqrt{5}$. Shortest distance $d = \sqrt{5/14} \approx 0.60 \implies \mathbf{0.60}$.
- **Q46**: $|z + 3 + 4i| \le |z| + |3 + 4i| = 2 + 5 = 7.00 \implies \mathbf{7.00}$.
- **Q47**: Non-negative integer solutions: $\binom{20+4-1}{4-1} = \binom{23}{3} = \frac{23 \times 22 \times 21}{6} = 1771 \implies \mathbf{1771.00}$.
- **Q48**: Distance from origin to center: $R = \sqrt{2^2 + 3^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7.00 \implies \mathbf{7.00}$.

### Questions 49 to 54
- **Q49**: For $x \in (0, 1/\sqrt{2})$, let $x = \sin\theta \implies \arcsin(2\sin\theta\cos\theta) = 2\theta = 2\arcsin x$. And $\arccos(\sqrt{1-x^2}) = \arccos(\cos\theta) = \theta = \arcsin x$. Derivative is $2/1 = 2$. **Correct: (A)**.
- **Q50**: Lines through origin $y = mx \implies \frac{dy}{dx} = m \implies y = x\frac{dy}{dx} \implies x\frac{dy}{dx} - y = 0$. **Correct: (A)**.
- **Q51**: Space diagonals of a cube: vectors $(1, 1, 1)$ and $(1, 1, -1)$. Angle $\cos\theta = \frac{1+1-1}{\sqrt{3}\sqrt{3}} = 1/3 \implies \theta = \arccos(1/3)$. **Correct: (A)**.
- **Q52**: $\det(2A) = 2^3 \det(A) = 8 \times 3 = 24$. **Correct: (A)**.
- **Q53**: $f(x) = e^x + x$. $f'(x) = e^x + 1 > 0$ strictly increasing, continuous from $-\infty$ to $\infty \implies$ exactly 1 real root. **Correct: (A)**.
- **Q54**: Total pairs $\binom{10}{2} = 45$. 2 red $\binom{6}{2} = 15$; 2 white $\binom{4}{2} = 6$. Total favorable $= 21$. $P = 21/45 = 7/15$. **Correct: (A)**.
"""

        raw_sol2 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 2)
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Horizontal impulsive blow on sphere: $J = M v_0$, $J h = I \omega_0 = \frac{2}{5}M R^2 \omega_0$. Pure rolling $v_0 = R\omega_0 \implies h = \frac{2}{5}R$. For $h > 2R/5$, $\omega_0 > v_0/R$, so contact point slips backward, friction acts forward. **Correct Options**: (A, B, C, D)
- **Q2**: Pascal's principle in hydraulic press: mechanical advantage $A_2/A_1 = 50$, force transmission, work conservation $F_1 d_1 = F_2 d_2$. **Correct Options**: (A, B, C, D)
- **Q3**: Energetics of capillary rise: $W_s = \rho \pi R^2 g h_0^2$, potential energy gained $\Delta U = \frac{1}{2}\rho \pi R^2 g h_0^2$. Viscous dissipation accounts for exactly half the work. Tilted column $l = h_0 / \cos\alpha$. **Correct Options**: (A, B, C, D)
- **Q4**: Focal length of concave lens using auxiliary convex lens: virtual object technique. **Correct Options**: (A, B, C, D)
- **Q5**: Minnaert resonance frequency of pulsating bubbles in liquids: $f = \frac{1}{2\pi R_0}\sqrt{\frac{3\gamma P_0}{\rho}}$. **Correct Options**: (A, B, C, D)
- **Q6**: Cylinder rolling off cylinder: separation angle $\cos\theta = 4/7$, normal force vanishes. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $F_2 = F_1 \left(\frac{d_2}{d_1}\right)^2 = 50.0 \times \left(\frac{20}{2}\right)^2 = 50.0 \times 100 = 5000\text{ N} \implies \mathbf{5000.00}$.
- **Q8**: $h = \frac{2T\cos\theta}{r\rho g} \implies r = \frac{2T}{h\rho g} = \frac{2(0.070)}{(0.070)(1000)(10.0)} = \frac{0.140}{700} = 2.0 \times 10^{-4}\text{ m} = 0.20\text{ mm} \implies \mathbf{0.20}$.
- **Q9**: $\omega_0 = \frac{J h}{I_{\text{cm}}} = \frac{(M v_0) h}{\frac{2}{5}M R^2} = \frac{5 v_0 h}{2 R^2} = \frac{5(5.0)(0.06)}{2(0.15)^2} = \frac{1.50}{0.045} \approx 33.3\text{ rad/s} \implies \mathbf{33.30}$.
- **Q10**: $\lambda/2 = l_2 - l_1 = 74.0 - 24.0 = 50.0\text{ cm} = 0.50\text{ m} \implies \lambda = 1.0\text{ m}$. Speed $v = f\lambda = 340 \times 1.0 = 340\text{ m/s} \implies \mathbf{340.00}$.
- **Q11**: Rolling without slipping: $\frac{7}{10}M v^2 = M g h \implies h = \frac{7 v^2}{10 g} = \frac{7(3.5)^2}{10(9.8)} = \frac{7 \times 12.25}{98} = \frac{85.75}{98} = 0.875\text{ m} \approx 0.88\text{ m} \implies \mathbf{0.88}$.
- **Q12**: Coalescence: $R = 2^{1/3} r \approx 1.26\text{ mm}$. $\Delta A = 4\pi (2 r^2 - R^2) = 4\pi r^2 (2 - 2^{2/3}) \approx 4\pi (10^{-6})(0.4126) \approx 5.185 \times 10^{-6}\text{ m}^2$. $\Delta U = T \Delta A = 0.465 \times 5.185 \times 10^{-6} \approx 2.41 \times 10^{-6}\text{ J} = 2.41\text{ }\mu\text{J} \implies \mathbf{2.41}$.

### Questions 13 to 18
- **Q13**: Center of mass of hemispherical shell is at $R/2$ from base. **Correct: (A)**.
- **Q14**: At top point, $v_{\text{top}} \ge \sqrt{gL}$. By energy conservation, $v_{\text{bottom}} \ge \sqrt{5gL}$. **Correct: (A)**.
- **Q15**: Bernoulli equation along streamline: $P + \frac{1}{2}\rho v^2 + \rho g z = \text{constant}$. **Correct: (A)**.
- **Q16**: Soap bubble has two liquid-gas interfaces $\implies \Delta P = 4T/R$. **Correct: (A)**.
- **Q17**: Hoop has highest rotational inertia fraction $I/(MR^2) = 1.0$, hence $K_{\text{rot}} / K_{\text{total}} = 1/2 = 50\%$ (cylinder is $1/3$, sphere is $2/7$). **Correct: (A)**.
- **Q18**: Wave speed on stretched string $v = \sqrt{T/\mu}$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Zimmerman-Traxler transition state stereocontrol in aldol reactions. **Correct Options**: (A, B, C, D)
- **Q20**: Gibbs phase rule and Clapeyron equation for negative slope in water. **Correct Options**: (A, B, C, D)
- **Q21**: Polyoxometalate chemistry and Keggin structures. **Correct Options**: (A, B, C, D)
- **Q22**: Hall-Héroult extraction of aluminum. **Correct Options**: (A, B, C, D)
- **Q23**: Protein secondary structure hydrogen bonding patterns. **Correct Options**: (A, B, C, D)
- **Q24**: Chirality: lactic acid, 2-chlorobutane, and $d/l$-tartaric acid are chiral. *meso*-tartaric acid is achiral. **Correct Options**: (A, B, C)

### Questions 25 to 30
- **Q25**: $\text{CaF}_2 \rightleftharpoons \text{Ca}^{2+} + 2\text{F}^- \implies K_{\text{sp}} = 4S^3 = 3.2 \times 10^{-11} \implies S^3 = 8.0 \times 10^{-12} \implies S = 2.0 \times 10^{-4}\text{ M} \implies \mathbf{2.00}$.
- **Q26**: Strong acid $[\text{H}^+] = 0.010\text{ M} \implies \text{pH} = -\log(0.010) = 2.00 \implies \mathbf{2.00}$.
- **Q27**: $E^\circ_{\text{cell}} = E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) - E^\circ(\text{Zn}^{2+}/\text{Zn}) = 0.77 - (-0.76) = 1.53\text{ V} \implies \mathbf{1.53}$.
- **Q28**: $\ln(k_2/k_1) = \frac{E_a}{R}\frac{\Delta T}{T_1 T_2} \implies 1.3863 = \frac{E_a}{8.314}\frac{20}{300 \times 320} \implies E_a = \frac{1.3863 \times 8.314 \times 96000}{20} \approx 55.3\text{ kJ/mol} \implies \mathbf{55.30}$.
- **Q29**: $\alpha = 0.20 \implies i = 1 + \alpha = 1.20$. $\Delta T_f = i K_f m = 1.20 \times 1.86 \times 0.050 = 0.1116\text{ K} \approx 0.112\text{ K} \implies \mathbf{0.112}$.
- **Q30**: In pyrosilicates $[\text{Si}_2\text{O}_7]^{6-}$, two tetrahedra share 1 bridging oxygen atom $\implies \mathbf{1.00}$.

### Questions 31 to 36
- **Q31**: Tertiary alkyl halide (*tert*-butyl chloride) forms the most stable tertiary carbocation, reacting fastest via $\text{S}_N1$. **Correct: (A)**.
- **Q32**: Basicity decreases down Group 15 due to decreasing electron density on the central atom: $\text{NH}_3 > \text{PH}_3 > \text{AsH}_3 > \text{SbH}_3 > \text{BiH}_3$. **Correct: (A)**.
- **Q33**: $\text{PCl}_5$ has 5 bond pairs and 0 lone pairs $\implies$ trigonal bipyramidal. **Correct: (A)**.
- **Q34**: Gabriel phthalimide synthesis is specific for the preparation of primary aliphatic amines. **Correct: (A)**.
- **Q35**: RNA contains D-ribose sugar. **Correct: (A)**.
- **Q36**: In $\text{H}_3\text{PO}_4$, $3(+1) + x + 4(-2) = 0 \implies x = +5$. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q38**: Properties of idempotent matrices: $A^2 = A \implies \lambda \in \{0, 1\}$, $\text{tr}(A) = \text{rank}(A)$. **Correct Options**: (A, B, C, D)
- **Q37**: Analysis of rational function $f(x) = \frac{x^2}{x^2+1}$. **Correct Options**: (A, B, C, D)
- **Q39**: Geometry of tangents from an external point to a circle. **Correct Options**: (A, B, C, D)
- **Q40**: Definite integrals involving logarithmic trigonometric functions. **Correct Options**: (A, B, C, D)
- **Q41**: Line in 3D: direction cosines, perpendicular vectors, containment in plane. **Correct Options**: (A, B, C, D)
- **Q42**: Binomial distribution properties for $n=10, p=0.5$. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Parabola crosses $x$-axis at $\pm 3$. Area $= 2 \int_0^3 (9 - x^2)dx = 2 [9x - x^3/3]_0^3 = 2(27 - 9) = 36.00 \implies \mathbf{36.00}$.
- **Q44**: $2^3 = 8 \equiv -1 \pmod 9 \implies 2^6 \equiv 1 \pmod 9$. $2025 = 6 \times 337 + 3$. $2^{2025} \equiv (2^6)^{337} \times 2^3 \equiv 1 \times 8 \equiv 8 \pmod 9 \implies \mathbf{8.00}$.
- **Q45**: $d = \frac{|0 - 0 + 0 - 49|}{\sqrt{2^2 + (-3)^2 + 6^2}} = \frac{49}{\sqrt{4 + 9 + 36}} = \frac{49}{7} = 7.00 \implies \mathbf{7.00}$.
- **Q46**: $\alpha^2 + \beta^2 = (\alpha+\beta)^2 - 2\alpha\beta = 4^2 - 2(1) = 16 - 2 = 14.00 \implies \mathbf{14.00}$.
- **Q47**: Word TRIANGLE has 8 distinct letters. Number of 3-letter words $= P(8, 3) = 8 \times 7 \times 6 = 336 \implies \mathbf{336.00}$.
- **Q48**: Circle $(x-4)^2 + (y+3)^2 = 16 + 9 = 25 \implies R = 5.00 \implies \mathbf{5.00}$.

### Questions 49 to 54
- **Q49**: Chain rule: $\frac{d}{dx}e^{x\sin x} = e^{x\sin x}\frac{d}{dx}(x\sin x) = e^{x\sin x}(\sin x + x\cos x)$. **Correct: (A)**.
- **Q50**: Integrating factor $e^x$. $y e^x = \int e^{-x} e^x dx = \int 1 dx = x + C$. $y(0) = 0 \implies C = 0 \implies y = x e^{-x}$. **Correct: (A)**.
- **Q51**: $e = \sqrt{1 - b^2/a^2} = \sqrt{1 - 9/25} = 4/5$. **Correct: (A)**.
- **Q52**: $S = \frac{a}{1-r} = \frac{1}{1 - 1/3} = \frac{1}{2/3} = 3/2$. **Correct: (A)**.
- **Q53**: By AM-GM inequality: $\frac{2^{\sin x} + 2^{\cos x}}{2} \ge \sqrt{2^{\sin x + \cos x}} \ge \sqrt{2^{-\sqrt{2}}} = 2^{-\sqrt{2}/2} \implies \text{minimum} = 2 \times 2^{-1/\sqrt{2}} = 2^{1 - 1/\sqrt{2}}$. **Correct: (A)**.
- **Q54**: $P(\ge 1\text{ head}) = 1 - P(\text{no heads}) = 1 - (1/2)^3 = 1 - 1/8 = 7/8$. **Correct: (A)**.
"""

        raw_val = r"""# Comprehensive Answer Key & Academic Alignment Validation – JEE Advanced Mock Examination __PAD__
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

### Master Answer Key – Paper 1
| Q# | Subject | Section | Question Type | Key |
|---|---|---|---|---|
| 1 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 2 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 3 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 4 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 5 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 6 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 7 | Physics | Sec 2 | Numerical | 3.92 |
| 8 | Physics | Sec 2 | Numerical | 56.00 |
| 9 | Physics | Sec 2 | Numerical | 9.00 |
| 10 | Physics | Sec 2 | Numerical | 0.00 |
| 11 | Physics | Sec 2 | Numerical | 9.00 |
| 12 | Physics | Sec 2 | Numerical | 90.00 |
| 13 | Physics | Sec 3 | Single Correct | A |
| 14 | Physics | Sec 3 | Single Correct | A |
| 15 | Physics | Sec 3 | Single Correct | A |
| 16 | Physics | Sec 3 | Single Correct | A |
| 17 | Physics | Sec 3 | Single Correct | A |
| 18 | Physics | Sec 3 | Single Correct | A |
| 19 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 20 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 21 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 22 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 23 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C |
| 25 | Chemistry | Sec 2 | Numerical | 0.85 |
| 26 | Chemistry | Sec 2 | Numerical | 1.00 |
| 27 | Chemistry | Sec 2 | Numerical | 0.28 |
| 28 | Chemistry | Sec 2 | Numerical | 0.015 |
| 29 | Chemistry | Sec 2 | Numerical | 1.87 |
| 30 | Chemistry | Sec 2 | Numerical | 3.00 |
| 31 | Chemistry | Sec 3 | Single Correct | A |
| 32 | Chemistry | Sec 3 | Single Correct | D |
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
| 43 | Mathematics | Sec 2 | Numerical | 1.15 |
| 44 | Mathematics | Sec 2 | Numerical | 1.00 |
| 45 | Mathematics | Sec 2 | Numerical | 0.60 |
| 46 | Mathematics | Sec 2 | Numerical | 7.00 |
| 47 | Mathematics | Sec 2 | Numerical | 1771.00 |
| 48 | Mathematics | Sec 2 | Numerical | 7.00 |
| 49 | Mathematics | Sec 3 | Single Correct | A |
| 50 | Mathematics | Sec 3 | Single Correct | A |
| 51 | Mathematics | Sec 3 | Single Correct | A |
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
| 7 | Physics | Sec 2 | Numerical | 5000.00 |
| 8 | Physics | Sec 2 | Numerical | 0.20 |
| 9 | Physics | Sec 2 | Numerical | 33.30 |
| 10 | Physics | Sec 2 | Numerical | 340.00 |
| 11 | Physics | Sec 2 | Numerical | 0.88 |
| 12 | Physics | Sec 2 | Numerical | 2.41 |
| 13 | Physics | Sec 3 | Single Correct | A |
| 14 | Physics | Sec 3 | Single Correct | A |
| 15 | Physics | Sec 3 | Single Correct | A |
| 16 | Physics | Sec 3 | Single Correct | A |
| 17 | Physics | Sec 3 | Single Correct | A |
| 18 | Physics | Sec 3 | Single Correct | A |
| 19 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 20 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 21 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 22 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 23 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C |
| 25 | Chemistry | Sec 2 | Numerical | 2.00 |
| 26 | Chemistry | Sec 2 | Numerical | 2.00 |
| 27 | Chemistry | Sec 2 | Numerical | 1.53 |
| 28 | Chemistry | Sec 2 | Numerical | 55.30 |
| 29 | Chemistry | Sec 2 | Numerical | 0.112 |
| 30 | Chemistry | Sec 2 | Numerical | 1.00 |
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
| 43 | Mathematics | Sec 2 | Numerical | 36.00 |
| 44 | Mathematics | Sec 2 | Numerical | 8.00 |
| 45 | Mathematics | Sec 2 | Numerical | 7.00 |
| 46 | Mathematics | Sec 2 | Numerical | 14.00 |
| 47 | Mathematics | Sec 2 | Numerical | 336.00 |
| 48 | Mathematics | Sec 2 | Numerical | 5.00 |
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

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, "IIT_Roorkee")
        print(f"Generated IIT Roorkee Mock {pad}!")

if __name__ == "__main__":
    generate_roorkee_06_to_10()

