"""
IIT Roorkee Mocks 01 to 05 Generator
Organising Institute: Indian Institute of Technology Roorkee
Empirical Benchmark: 2008, 2013, 2019 Official JEE Advanced Papers
Features:
- Mechanics dominance (>= 45% of physics: rigid body dynamics, non-inertial frames, fluid dynamics, experimental physics)
- Chemistry: Stereochemical cascades, conformational analysis of cyclohexanes, phase equilibria, blast furnace metallurgy
- Mathematics: Definite integrals reduction formulas, orthogonal trajectories, 3D geometry quadrics, symmetric polynomials
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_roorkee_01_to_05():
    for mock_idx in range(1, 6):
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
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal conveyor belt that accelerates horizontally with constant acceleration $a_0\hat{i}$. The coefficient of static friction between the sphere and belt is $\mu_s$:
(A) The condition for the sphere to roll without slipping on the conveyor belt is $\mu_s \ge \frac{2 a_0}{7 g}$.  
(B) If pure rolling is maintained, the linear acceleration of the center of mass of the sphere relative to the ground is $a_{\text{cm}} = \frac{2}{7}a_0\hat{i}$.  
(C) The acceleration of the center of mass relative to the belt is $a_{\text{rel}} = -\frac{5}{7}a_0\hat{i}$.  
(D) The frictional force acting on the sphere points in the direction of the belt's acceleration $+a_0\hat{i}$.

#### Question 2
A compound pendulum consists of a thin uniform rod of length $L$ and mass $M$ pivoted about a horizontal axis perpendicular to the rod at distance $d$ from its center of mass:
(A) The period of small oscillations is $T = 2\pi\sqrt{\frac{L^2/12 + d^2}{g d}}$.  
(B) The period $T$ attains a minimum value when $d = \frac{L}{\sqrt{12}}$.  
(C) For any period $T > T_{\min}$, there exist exactly four distinct suspension points on the rod that give identical oscillation periods.  
(D) The center of oscillation is located at distance $l = \frac{L^2}{12d}$ from the center of mass on the opposite side of the suspension point.

#### Question 3
A cylindrical vessel of radius $R$ containing an incompressible, inviscid liquid of density $\rho$ rotates about its vertical axis of symmetry with constant angular velocity $\omega$:
(A) The free surface of the rotating liquid is a paraboloid of revolution given by $z(r) = z_0 + \frac{\omega^2 r^2}{2g}$.  
(B) The pressure at any point $(r, z)$ within the liquid is $P(r, z) = P_0 + \frac{1}{2}\rho \omega^2 r^2 - \rho g (z - z_0)$.  
(C) The difference in liquid height between the rim ($r = R$) and the center ($r = 0$) is $h = \frac{\omega^2 R^2}{2g}$.  
(D) The total volume of the paraboloid depression below the rim height is equal to half the volume of a cylinder of radius $R$ and height $h$.

#### Question 4
A small particle of mass $m$ slides on the inner frictionless surface of a vertical hollow circular cone of semi-vertical angle $\alpha$, with vertex pointing downward:
(A) The particle can execute uniform circular motion in a horizontal plane at height $h$ above the vertex with angular speed $\omega = \sqrt{\frac{g}{h\tan^2\alpha}}$.  
(B) The normal force exerted by the cone on the particle is $N = \frac{mg}{\sin\alpha}$.  
(C) Small oscillations about the steady circular orbit are stable for any cone semi-vertical angle $0 < \alpha < \pi/2$.  
(D) The angular momentum about the vertical cone axis is strictly conserved throughout the motion.

#### Question 5
In an experiment to determine the acceleration due to gravity $g$ using a simple pendulum of nominal length $L = 100.0\text{ cm}$ and time for 50 oscillations $t = 100.0\text{ s}$:
(A) The fractional error in $g$ is $\frac{\Delta g}{g} = \frac{\Delta L}{L} + 2\frac{\Delta t}{t}$.  
(B) If $\Delta L = 0.1\text{ cm}$ and the stopwatch has a least count $\Delta t_{\text{watch}} = 0.1\text{ s}$, the fractional error $\frac{\Delta t}{t} = \frac{0.1}{100.0} = 0.1\%$.  
(C) The maximum permissible percentage error in the determination of $g$ is $0.3\%$.  
(D) Timing 50 oscillations rather than 10 oscillations reduces the percentage error arising from reaction time.

#### Question 6
A heavy symmetric top of mass $M$ with moment of inertia $I_3$ about its symmetry axis and $I_1$ about the transverse axes pivots at its tip, which is fixed at origin $O$. The center of mass is at distance $l$ from $O$, and the top spins with high angular velocity $\omega_s$ about its axis inclined at angle $\theta$ to the vertical:
(A) The gravitational torque about $O$ is $\tau = M g l \sin\theta$.  
(B) The angular momentum vector is approximately directed along the symmetry axis: $\vec{L} \approx I_3 \omega_s \hat{n}$.  
(C) The top precesses steadily around the vertical axis with precession angular velocity $\Omega_p = \frac{M g l}{I_3 \omega_s}$.  
(D) The precession frequency $\Omega_p$ is independent of the tilt angle $\theta$ in the fast-spin limit.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A uniform solid cylinder of mass $m = 4.0\text{ kg}$ and radius $r = 0.25\text{ m}$ is pulled horizontally by a force $F = 30.0\text{ N}$ applied at its axle. If the cylinder rolls without slipping on a horizontal surface, the linear acceleration of its center of mass in $\text{m/s}^2$ is $a$. Find $a$.

#### Question 8
A horizontal pipe of non-uniform cross-section has water flowing through it. At section 1, cross-sectional area is $A_1 = 40.0\text{ cm}^2$ and flow speed is $v_1 = 2.0\text{ m/s}$. At section 2, the area is $A_2 = 10.0\text{ cm}^2$. The gauge pressure drop $P_1 - P_2$ between the two sections in kilopascals ($\text{kPa}$) is $\Delta P$. (Density of water $\rho = 1000\text{ kg/m}^3$). Find $\Delta P$.

#### Question 9
A spherical steel ball of radius $r = 2.0\text{ mm}$ falls with terminal velocity in a viscous fluid of density $\rho_f = 1200\text{ kg/m}^3$ and dynamic viscosity $\eta = 0.90\text{ Pa s}$. The density of steel is $\rho_s = 7800\text{ kg/m}^3$. Taking $g = 9.8\text{ m/s}^2$, the terminal velocity in $\text{cm/s}$ is $v_t$. Find $v_t$ rounded off to two decimal places.

#### Question 10
In a screw gauge, the pitch of the screw is $0.5\text{ mm}$ and there are 50 divisions on the circular scale. When measuring the diameter of a wire, the main scale reads $2.5\text{ mm}$ and the 32nd division of the circular scale coincides with the reference line. If the screw gauge has a positive zero error of $+0.03\text{ mm}$, the corrected diameter of the wire in millimeters is $d\text{ mm}$. Find $d$ rounded off to two decimal places.

#### Question 11
A uniform rod of length $L = 1.20\text{ m}$ is pivoted at one end. It is released from rest in the horizontal position. Its angular velocity as it swings through the vertical position is $\omega\text{ rad/s}$. Taking $g = 9.8\text{ m/s}^2$, find $\omega$ rounded off to two decimal places.

#### Question 12
A vertical U-tube containing mercury ($\rho_m = 13.6\text{ g/cm}^3$) has water poured into one arm until a water column of height $h_w = 27.2\text{ cm}$ is formed. The difference in mercury levels in the two arms in centimeters is $\Delta h\text{ cm}$. Find $\Delta h$.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The moment of inertia of a uniform thin rod of mass $M$ and length $L$ about an axis perpendicular to the rod passing through a point at distance $L/4$ from one end is:
(A) $\frac{7}{48} M L^2$  
(B) $\frac{1}{12} M L^2$  
(C) $\frac{1}{3} M L^2$  
(D) $\frac{5}{24} M L^2$

#### Question 14
A block of mass $m$ attached to a spring of stiffness $k$ oscillates on a smooth horizontal table with amplitude $A$. At the instant the block passes through its mean position, a lump of clay of mass $m$ is dropped gently onto it and sticks. The new amplitude of oscillation is:
(A) $A / \sqrt{2}$  
(B) $A / 2$  
(C) $\sqrt{2}A$  
(D) $A$

#### Question 15
Two capillary tubes $A$ and $B$ of radii $r_1$ and $r_2$ ($r_1 = 2r_2$) are dipped vertically into the same liquid. The ratio of the heights of the liquid columns $h_1 / h_2$ is:
(A) $1/2$  
(B) $2$  
(C) $1/4$  
(D) $4$

#### Question 16
A Vernier calliper has 10 divisions of the Vernier scale coinciding with 9 divisions of the main scale. If each main scale division is $1.0\text{ mm}$, the least count of the instrument is:
(A) $0.1\text{ mm}$  
(B) $0.01\text{ mm}$  
(C) $0.05\text{ mm}$  
(D) $0.02\text{ mm}$

#### Question 17
A solid sphere and a solid cylinder of the same mass and radius are rolled down an inclined plane from rest from the same height without slipping. The body that reaches the bottom first is:
(A) The solid sphere  
(B) The solid cylinder  
(C) Both reach simultaneously  
(D) Depends on the angle of the incline

#### Question 18
The pressure of an ideal gas is given by $P = \frac{2}{3}E_v$, where $E_v$ represents:
(A) Translational kinetic energy per unit volume  
(B) Total internal energy per unit volume  
(C) Rotational kinetic energy per unit volume  
(D) Potential energy per unit volume

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the conformational analysis of cyclohexane:
(A) The chair conformation is the most stable conformation due to staggered $\text{C}-\text{C}$ bonds and minimal torsional and steric strain.  
(B) In mono-substituted methylcyclohexane, the equatorial conformer is more stable than the axial conformer by approximately $7.3\text{ kJ/mol}$ due to 1,3-diaxial steric interactions.  
(C) The boat conformation possesses significant flagpole-flagpole steric interactions and eclipsing torsional strain.  
(D) The twist-boat conformation is a local minimum on the potential energy surface and is more stable than the ideal symmetrical boat conformation.

#### Question 20
Regarding stereochemical cascades in additions to alkenes:
(A) Electrophilic addition of bromine ($\text{Br}_2$) to *trans*-but-2-ene in $\text{CCl}_4$ yields exclusively the *meso*-2,3-dibromobutane.  
(B) Addition of $\text{Br}_2$ to *cis*-but-2-ene yields a racemic pair of $(2R,3R)$- and $(2S,3S)$-2,3-dibromobutane.  
(C) Catalytic hydrogenation ($\text{H}_2 / \text{Pd}$) of *cis*-but-2-ene gives *meso*-butane.  
(D) Epoxidation of an alkene with $m$-chloroperbenzoic acid (mCPBA) is a stereospecific *syn*-addition.

#### Question 21
Regarding the reduction of iron ore in a blast furnace:
(A) In the reduction zone ($500\text{ to }800\text{ K}$), hematite is reduced: $3\text{Fe}_2\text{O}_3 + \text{CO} \to 2\text{Fe}_3\text{O}_4 + \text{CO}_2$.  
(B) In the slag formation zone ($1000\text{ to }1200\text{ K}$), limestone decomposes to $\text{CaO}$, which reacts with silica to form fusible calcium silicate slag: $\text{CaO} + \text{SiO}_2 \to \text{CaSiO}_3$.  
(C) Carbon monoxide ($\text{CO}$) is the primary reducing agent in the upper, lower-temperature zones of the furnace.  
(D) Solid carbon (coke) is the primary reducing agent in the high-temperature zone ($> 1200\text{ K}$).

#### Question 22
Regarding the structure and classification of silicates:
(A) Orthosilicates contain discrete tetrahedral $[\text{SiO}_4]^{4-}$ units.  
(B) Pyrosilicates (sorosilicates) contain $[\text{Si}_2\text{O}_7]^{6-}$ units formed by sharing one oxygen atom between two tetrahedra.  
(C) Cyclic (ring) silicates contain units of general formula $[\text{SiO}_3]_n^{2n-}$, such as in beryl ($\text{Be}_3\text{Al}_2\text{Si}_6\text{O}_{18}$).  
(D) Sheet silicates (phyllosilicates) share three oxygen atoms per tetrahedron, yielding the general empirical formula $[\text{Si}_2\text{O}_5]_n^{2n-}$.

#### Question 23
Regarding the Michaelis-Menten mechanism of enzyme kinetics $E + S \xrightleftharpoons[k_{-1}]{k_1} ES \xrightarrow{k_2} E + P$:
(A) The reaction rate is given by $v = \frac{V_{\max}[S]}{K_m + [S]}$ where $K_m = \frac{k_{-1} + k_2}{k_1}$.  
(B) When $[S] \ll K_m$, the reaction follows first-order kinetics with respect to substrate: $v \approx \frac{V_{\max}}{K_m}[S]$.  
(C) When $[S] \gg K_m$, the reaction follows zero-order kinetics: $v \approx V_{\max}$.  
(D) A Lineweaver-Burk plot of $1/v$ versus $1/[S]$ is linear with slope $K_m / V_{\max}$ and y-intercept $1/V_{\max}$.

#### Question 24
Which of the following statements about coordination isomers is/are CORRECT:
(A) $[Co(NH_3)_5 SO_4]Br$ and $[Co(NH_3)_5 Br]SO_4$ are ionization isomers.  
(B) $[Pt(NH_3)_4][PtCl_4]$ and $[Pt(NH_3)_3 Cl][Pt(NH_3)Cl_3]$ are coordination isomers.  
(C) $[\text{Cr}(\text{H}_2\text{O})_6]\text{Cl}_3$ and $[\text{Cr}(\text{H}_2\text{O})_5\text{Cl}]\text{Cl}_2 \cdot \text{H}_2\text{O}$ are hydrate (solvate) isomers.  
(D) $[Co(en)_2 Cl_2]^+$ exists as *cis* and *trans* isomers, where the *cis* isomer is chiral and exists as a pair of enantiomers.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The decomposition of hydrogen peroxide in aqueous solution is first-order. If the rate constant is $k = 0.0693\text{ min}^{-1}$, the time required for the concentration to fall to $12.5\%$ of its initial value is $t\text{ min}$. Find $t$.

#### Question 26
Calculate the $\text{pH}$ of a $0.010\text{ M}$ aqueous solution of ammonium hydroxide ($\text{NH}_4\text{OH}$) having dissociation constant $K_b = 1.0 \times 10^{-5}$ at $298\text{ K}$. Find the $\text{pH}$ rounded off to one decimal place.

#### Question 27
For the reaction $\text{N}_2\text{O}_4(g) \rightleftharpoons 2\text{NO}_2(g)$, the standard equilibrium constant is $K_p = 0.150\text{ bar}$ at $298\text{ K}$. The standard Gibbs free energy change $\Delta G^\circ$ in $\text{kJ/mol}$ is $X$. (Take $R = 8.314\text{ J/(mol K)}$ and $\ln(0.150) \approx -1.897$). Find $|X|$ rounded off to two decimal places.

#### Question 28
The molal elevation constant $K_b$ for water is $0.512\text{ K kg mol}^{-1}$. A solution prepared by dissolving $18.0\text{ g}$ of glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, molar mass $180\text{ g/mol}$) in $200.0\text{ g}$ of water boils at $T_b^\circ + \Delta T_b$. The boiling point elevation $\Delta T_b$ in Kelvin is $\Delta T_b$. Find $\Delta T_b$ rounded off to three decimal places.

#### Question 29
A metal crystallizes in a simple cubic unit cell with edge length $a = 300\text{ pm}$. The density of the metal is $8.0\text{ g/cm}^3$. Calculate the molar mass of the metal in $\text{g/mol}$ rounded off to the nearest integer. (Take $N_A = 6.02 \times 10^{23}\text{ mol}^{-1}$).

#### Question 30
Find the number of bridging carbonyl ligands in the neutral binuclear complex $\text{Fe}_2(\text{CO})_9$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The major product obtained when phenol is treated with chloroform and aqueous $\text{NaOH}$ (Reimer-Tiemann reaction) is:
(A) Salicylaldehyde  
(B) Salicylic acid  
(C) Benzoic acid  
(D) Chlorobenzene

#### Question 32
Which of the following transition metal ions is colorless in aqueous solution:
(A) $\text{Ti}^{4+}$  
(B) $\text{Cu}^{2+}$  
(C) $\text{Fe}^{3+}$  
(D) $\text{Cr}^{3+}$

#### Question 33
The geometry of $\text{XeOF}_4$ according to VSEPR theory is:
(A) Square pyramidal  
(B) Octahedral  
(C) Trigonal bipyramidal  
(D) Tetrahedral

#### Question 34
In the Williamson ether synthesis, the reaction between sodium ethoxide and ethyl iodide proceeds via:
(A) $\text{S}_N2$ mechanism  
(B) $\text{S}_N1$ mechanism  
(C) E2 mechanism  
(D) E1 mechanism

#### Question 35
The monomer of natural rubber is:
(A) Isoprene (2-methylbuta-1,3-diene)  
(B) Chloroprene  
(C) Neoprene  
(D) Buta-1,3-diene

#### Question 36
The conjugate base of bicarbonate ion $\text{HCO}_3^-$ is:
(A) $\text{CO}_3^{2-}$  
(B) $\text{H}_2\text{CO}_3$  
(C) $\text{CO}_2$  
(D) $\text{OH}^-$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $I_n = \int_0^{\pi/2} \sin^n x dx$ for $n \ge 0$:
(A) $I_n = \frac{n-1}{n} I_{n-2}$ for $n \ge 2$.  
(B) $I_{2k} = \frac{2k-1}{2k} \cdot \frac{2k-3}{2k-2} \cdots \frac{1}{2} \cdot \frac{\pi}{2}$.  
(C) $I_{2k+1} = \frac{2k}{2k+1} \cdot \frac{2k-2}{2k-1} \cdots \frac{2}{3} \cdot 1$.  
(D) $\lim_{n \to \infty} \frac{I_n}{I_{n-1}} = 1$.

#### Question 38
Consider the family of curves $y = C x^2$:
(A) The differential equation of this family is $\frac{dy}{dx} = \frac{2y}{x}$.  
(B) The differential equation of the orthogonal trajectories is $\frac{dy}{dx} = -\frac{x}{2y}$.  
(C) The orthogonal trajectories are a family of ellipses given by $x^2 + 2y^2 = K^2$.  
(D) Every member of the orthogonal trajectories intersects every member of the original family at right angles.

#### Question 39
Consider the line $L: \frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and the plane $P: 2x - 3y + z = 5$:
(A) The direction vector of the line is $\vec{d} = (2, 3, 4)$ and normal to the plane is $\vec{n} = (2, -3, 1)$.  
(B) $\vec{d} \cdot \vec{n} = 4 - 9 + 4 = -1 \ne 0$, hence the line is not parallel to the plane.  
(C) The line intersects the plane at a single unique point.  
(D) The angle $\theta$ between the line and the plane satisfies $\sin\theta = \frac{|\vec{d}\cdot\vec{n}|}{|\vec{d}||\vec{n}|} = \frac{1}{\sqrt{29}\sqrt{14}}$.

#### Question 40
Let $P(x) = x^3 - 3x + 1$:
(A) $P(x)$ has three real roots in the intervals $(-2, -1)$, $(0, 1)$, and $(1, 2)$.  
(B) $P'(x) = 3(x^2 - 1)$, with critical points at $x = \pm 1$.  
(C) Local maximum occurs at $x = -1$ with value $P(-1) = 3 > 0$.  
(D) Local minimum occurs at $x = 1$ with value $P(1) = -1 < 0$.

#### Question 41
Let $S_n = \sum_{k=1}^n k(k+1)$:
(A) $k(k+1) = \frac{1}{3}[k(k+1)(k+2) - (k-1)k(k+1)]$.  
(B) $S_n = \frac{n(n+1)(n+2)}{3}$.  
(C) $\sum_{k=1}^n k(k+1)(k+2) = \frac{n(n+1)(n+2)(n+3)}{4}$.  
(D) $\lim_{n \to \infty} \frac{S_n}{n^3} = \frac{1}{3}$.

#### Question 42
Consider the parabola $y^2 = 8x$:
(A) The coordinates of its focus are $(2, 0)$.  
(B) The equation of the directrix is $x = -2$.  
(C) The length of its latus rectum is 8.  
(D) The equation of the tangent at $(2, 4)$ is $y = x + 2$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = x(x-1)(x-2)$ and the $x$-axis from $x = 0$ to $x = 2$. Round off to two decimal places.

#### Question 44
Find the number of 5-digit numbers that can be formed using the digits 0, 1, 2, 3, 4 without repetition.

#### Question 45
Evaluate $\lim_{x \to 0} \frac{x - \sin x}{x^3}$. The limit is $1/k$. Find $k$.

#### Question 46
Find the distance from the point $(2, 3, 4)$ to the line $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{6}$. Round off to two decimal places.

#### Question 47
Let $A$ be a $2 \times 2$ matrix with eigenvalues 2 and 5. Find the value of $\text{tr}(A^2)$.

#### Question 48
Find the radius of the sphere $x^2 + y^2 + z^2 - 2x - 4y - 6z - 11 = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\ln(\ln x)$ with respect to $x$ is:
(A) $\frac{1}{x \ln x}$  
(B) $\frac{1}{\ln x}$  
(C) $\frac{1}{x^2}$  
(D) $\frac{\ln x}{x}$

#### Question 50
The solution of the differential equation $\frac{dy}{dx} = \frac{y}{x}$ is:
(A) $y = C x$  
(B) $y = C / x$  
(C) $y = \ln x + C$  
(D) $y^2 = x^2 + C$

#### Question 51
The eccentricity of a rectangular hyperbola is:
(A) $\sqrt{2}$  
(B) 2  
(C) $\sqrt{3}$  
(D) $1$

#### Question 52
If $\alpha$ and $\beta$ are the roots of $x^2 - 5x + 6 = 0$, then $\alpha^2 + \beta^2$ is:
(A) 13  
(B) 25  
(C) 19  
(D) 12

#### Question 53
The maximum value of $\sin x \cos x$ is:
(A) $1/2$  
(B) $1$  
(C) $2$  
(D) $1/4$

#### Question 54
In how many ways can 5 boys and 5 girls sit alternately in a circle:
(A) $4! \times 5! = 2880$  
(B) $5! \times 5!$  
(C) $9!$  
(D) $10!$
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
A uniform solid sphere of mass $M$ and radius $R$ rolls without slipping down an inclined plane of inclination $\theta$:
(A) The linear acceleration of the sphere is $a = \frac{5}{7}g\sin\theta$.  
(B) The magnitude of the static friction force is $f_s = \frac{2}{7}Mg\sin\theta$.  
(C) The minimum coefficient of static friction required for pure rolling is $\mu_{\min} = \frac{2}{7}\tan\theta$.  
(D) The fraction of total kinetic energy associated with rotation is $2/7$.

#### Question 2
A U-tube manometer contains liquid of density $\rho$ and total liquid column length $L$. The liquid is displaced slightly by distance $x$ in one arm and released:
(A) The restoring force is $F = -2\rho A g x$, where $A$ is the cross-sectional area of the tube.  
(B) The motion of the liquid column is simple harmonic motion.  
(C) The time period of oscillation is $T = 2\pi\sqrt{\frac{L}{2g}}$.  
(D) The oscillation period is independent of the liquid density $\rho$ and tube cross-sectional area $A$.

#### Question 3
A particle of mass $m$ moves in a rotating reference frame rotating with constant angular velocity $\vec{\omega}$:
(A) The centrifugal fictitious force is $\vec{F}_{\text{cent}} = -m \vec{\omega} \times (\vec{\omega} \times \vec{r})$.  
(B) The Coriolis fictitious force is $\vec{F}_{\text{Cor}} = -2m (\vec{\omega} \times \vec{v}_{\text{rel}})$.  
(C) The Coriolis force does zero work on the particle in the rotating frame.  
(D) In the northern hemisphere of Earth, the Coriolis force deflects horizontally moving bodies to their right.

#### Question 4
In a resonance tube experiment to measure the speed of sound using a tuning fork of frequency $f = 512\text{ Hz}$:
(A) If the first two resonance lengths are $l_1$ and $l_2$, the wavelength is $\lambda = 2(l_2 - l_1)$.  
(B) The end correction of the tube is $e = \frac{l_2 - 3l_1}{2}$.  
(C) The speed of sound is $v = 2f(l_2 - l_1)$.  
(D) The end correction is approximately $e \approx 0.6 r$, where $r$ is the inner radius of the resonance tube.

#### Question 5
A uniform disc of mass $M$ and radius $R$ has a concentric circular hole of radius $R/2$ cut out:
(A) The mass of the material removed is $M/3$ of the remaining disc mass.  
(B) The moment of inertia of the annular disc about its central symmetry axis is $I = \frac{5}{8} M R^2$.  
(C) The moment of inertia about a diameter is $I_d = \frac{5}{16} M R^2$.  
(D) The radius of gyration about the central axis is $k = R\sqrt{5/8}$.

#### Question 6
Regarding the laminar flow of a viscous liquid through a horizontal cylindrical pipe of radius $R$ and length $L$ under pressure difference $\Delta P$ (Poiseuille's law):
(A) The velocity profile is parabolic: $v(r) = \frac{\Delta P}{4\eta L}(R^2 - r^2)$.  
(B) The maximum flow speed occurs along the central axis: $v_{\max} = \frac{\Delta P R^2}{4\eta L}$.  
(C) The volumetric flow rate is $Q = \frac{\pi \Delta P R^4}{8\eta L}$.  
(D) The viscous drag force exerted by the fluid on the inner wall of the pipe equals $\Delta P \pi R^2$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A solid sphere of mass $M = 2.0\text{ kg}$ and radius $R = 0.10\text{ m}$ is spinning about its diameter with angular speed $\omega = 50\text{ rad/s}$. Its rotational kinetic energy in joules is $E\text{ J}$. Find $E$.

#### Question 8
A simple pendulum has period $T = 2.00\text{ s}$ on Earth. When taken to a planet where gravity is $g' = 1.44 g$, its new period is $T'\text{ s}$. Find $T'$ rounded off to two decimal places.

#### Question 9
In a Searle's apparatus experiment, a steel wire of length $L = 2.0\text{ m}$ and radius $r = 0.50\text{ mm}$ extends by $\Delta L = 0.80\text{ mm}$ under a load of $M = 5.0\text{ kg}$. Taking $g = 9.8\text{ m/s}^2$ and $\pi = 3.14$, the Young's modulus of the wire is $Y \times 10^{11}\text{ N/m}^2$. Find $Y$ rounded off to two decimal places.

#### Question 10
Water flows over a rectangular weir of crest length $b = 1.50\text{ m}$ under a head $H = 0.25\text{ m}$. Using the discharge formula $Q = \frac{2}{3} C_d b \sqrt{2g} H^{3/2}$ with $C_d = 0.60$ and $g = 9.8\text{ m/s}^2$, the discharge $Q$ in $\text{m}^3/\text{s}$ is $Q$. Find $Q$ rounded off to two decimal places.

#### Question 11
A uniform rod of mass $m = 3.0\text{ kg}$ and length $L = 1.0\text{ m}$ is hanging vertically from a frictionless pivot at its top end. A bullet of mass $m_0 = 0.05\text{ kg}$ moving horizontally at speed $v_0 = 200\text{ m/s}$ strikes the rod at its lower end and embeds itself. The angular velocity of the system immediately after collision is $\omega\text{ rad/s}$. Find $\omega$ rounded off to two decimal places.

#### Question 12
A large open tank has a small hole of diameter $d = 2.0\text{ cm}$ at depth $h = 5.0\text{ m}$ below the water surface. Taking $g = 9.8\text{ m/s}^2$, the initial volume rate of discharge from the hole in liters per second ($\text{L/s}$) is $Q$. Find $Q$ rounded off to one decimal place.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The center of mass of a uniform solid hemisphere of radius $R$ lies on its symmetry axis at distance from its flat base:
(A) $\frac{3}{8}R$  
(B) $\frac{1}{2}R$  
(C) $\frac{4}{3\pi}R$  
(D) $\frac{5}{8}R$

#### Question 14
Two bodies of masses $m_1$ and $m_2$ ($m_1 > m_2$) have equal kinetic energies. The ratio of their linear momenta $p_1 / p_2$ is:
(A) $\sqrt{m_1 / m_2}$  
(B) $m_1 / m_2$  
(C) $m_2 / m_1$  
(D) $1$

#### Question 15
A body of density $\rho$ floats in a liquid of density $\sigma$ with a fraction $f$ of its volume submerged. The fraction $f$ is:
(A) $\rho / \sigma$  
(B) $\sigma / \rho$  
(C) $1 - \rho/\sigma$  
(D) $\rho/(\rho+\sigma)$

#### Question 16
The dimensions of dynamic viscosity $\eta$ in SI units are:
(A) $[\text{M L}^{-1}\text{ T}^{-1}]$  
(B) $[\text{M L T}^{-1}]$  
(C) $[\text{M L}^{-2}\text{ T}^{-2}]$  
(D) $[\text{M L}^2\text{ T}^{-1}]$

#### Question 17
A particle moves in a circular path with decreasing speed. The angle between its velocity vector $\vec{v}$ and its acceleration vector $\vec{a}$ is:
(A) Obtuse ($90^\circ < \theta < 180^\circ$)  
(B) Acute ($0^\circ < \theta < 90^\circ$)  
(C) Exactly $90^\circ$  
(D) Exactly $180^\circ$

#### Question 18
When two soap bubbles of radii $r_1$ and $r_2$ ($r_1 > r_2$) coalesce isothermally under vacuum to form a single bubble of radius $R$, then:
(A) $R^2 = r_1^2 + r_2^2$  
(B) $R^3 = r_1^3 + r_2^3$  
(C) $R = r_1 + r_2$  
(D) $R^2 = r_1^2 - r_2^2$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the stereochemistry of E2 elimination reactions:
(A) The reaction requires an anti-periplanar conformation between the leaving group and the $\beta$-hydrogen.  
(B) In cyclohexane rings, both the leaving group and the $\beta$-hydrogen must occupy *trans*-diaxial orientations.  
(C) Menthol and neomenthol react with base at drastically different rates due to conformational constraints.  
(D) Bulky strong bases such as potassium *tert*-butoxide yield predominantly the Hofmann alkene.

#### Question 20
Regarding the thermodynamics and phase equilibria of real gases obeying Dieterici's equation $P(V_m - b)e^{a/(RTV_m)} = RT$:
(A) At high temperatures and large molar volumes, the equation reduces to the ideal gas law.  
(B) The critical parameters satisfy $V_c = 2b$, $T_c = \frac{a}{4Rb}$, $P_c = \frac{a}{4e^2 b^2}$.  
(C) The critical compressibility factor is $Z_c = \frac{P_c V_c}{R T_c} = \frac{2}{e^2} \approx 0.271$.  
(D) The Dieterici equation predicts critical compressibility factor values that match experimental data for real gases better than the van der Waals equation ($Z_c \approx 0.28$ vs $0.375$).

#### Question 21
Regarding the extraction and refining of copper:
(A) Copper pyrites ($\text{CuFeS}_2$) is concentrated by froth flotation.  
(B) In the blast furnace, iron impurity is removed as ferrous silicate slag: $\text{FeO} + \text{SiO}_2 \to \text{FeSiO}_3$.  
(C) In the Bessemer converter, auto-reduction occurs: $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \to 6\text{Cu} + \text{SO}_2$.  
(D) Blister copper obtained from the converter has approximately $98\%$ purity and is refined electrolytically.

#### Question 22
Regarding chemical equilibrium and Le Chatelier's principle:
(A) Addition of an inert gas at constant volume has no effect on the equilibrium position.  
(B) Addition of an inert gas at constant pressure shifts the equilibrium in the direction of greater number of gaseous moles.  
(C) An increase in total pressure on the system $\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3$ shifts the equilibrium to the right.  
(D) A catalyst increases the rates of both forward and reverse reactions equally without changing the value of $K_{\text{eq}}$.

#### Question 23
Regarding carbohydrates and amino acids:
(A) All standard proteinogenic amino acids are chiral except glycine.  
(B) In aqueous solution at isoelectric point ($\text{pI}$), amino acids exist primarily as dipolar zwitterions.  
(C) At $\text{pH} < \text{pI}$, the amino acid exists predominantly as a cation and migrates toward the cathode in electrophoresis.  
(D) Maltose is composed of two $\alpha\text{-D-glucose}$ units joined by an $\alpha(1\to 4)$ glycosidic linkage.

#### Question 24
Which of the following complexes exhibit geometrical isomerism:
(A) $[\text{Pt}(\text{NH}_3)_2 \text{Cl}_2]$ (Square planar)  
(B) $[\text{Co}(\text{NH}_3)_4 \text{Cl}_2]^+$ (Octahedral)  
(C) $[\text{Co}(\text{en})_2 \text{Cl}_2]^+$ (Octahedral)  
(D) $[\text{Zn}(\text{NH}_3)_2 \text{Cl}_2]$ (Tetrahedral)

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The equilibrium constant for the reaction $\text{H}_2(g) + \text{I}_2(g) \rightleftharpoons 2\text{HI}(g)$ is $K_c = 49.0$ at $700\text{ K}$. If $1.0\text{ mole}$ of $\text{H}_2$ and $1.0\text{ mole}$ of $\text{I}_2$ are placed in a $1.0\text{ L}$ flask, the number of moles of $\text{HI}$ present at equilibrium is $n$. Find $n$ rounded off to two decimal places.

#### Question 26
Calculate the solubility of $\text{AgCl}$ in $0.10\text{ M}$ aqueous $\text{NaCl}$ solution at $298\text{ K}$, given $K_{\text{sp}}(\text{AgCl}) = 1.8 \times 10^{-10}$. Report the solubility as $S \times 10^{-9}\text{ M}$. Find $S$.

#### Question 27
The standard reduction potentials are $E^\circ(\text{Cr}^{3+}/\text{Cr}) = -0.74\text{ V}$ and $E^\circ(\text{Cd}^{2+}/\text{Cd}) = -0.40\text{ V}$. The standard EMF of the cell $2\text{Cr} + 3\text{Cd}^{2+} \to 2\text{Cr}^{3+} + 3\text{Cd}$ is $E^\circ_{\text{cell}}\text{ V}$. Find $E^\circ_{\text{cell}}$ rounded off to two decimal places.

#### Question 28
For a chemical reaction, the activation energy is $E_a = 50.0\text{ kJ/mol}$. By what factor does the rate constant increase when temperature rises from $300\text{ K}$ to $310\text{ K}$? (Take $R = 8.314\text{ J/(mol K)}$ and $e^x \approx 1 + x$). Round off the factor to two decimal places.

#### Question 29
A $0.20\text{ m}$ aqueous solution of a non-electrolyte solute freezes at $-0.372^\circ\text{C}$. The molal depression constant $K_f$ of water is $K_f\text{ K kg mol}^{-1}$. Find $K_f$ rounded off to two decimal places.

#### Question 30
Find the number of lone pairs on the central iodine atom in the triiodide ion $\text{I}_3^-$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following compounds gives a positive iodoform test:
(A) Acetophenone ($\text{C}_6\text{H}_5\text{COCH}_3$)  
(B) Benzophenone ($\text{C}_6\text{H}_5\text{COC}_6\text{H}_5$)  
(C) Benzaldehyde ($\text{C}_6\text{H}_5\text{CHO}$)  
(D) Propan-1-ol

#### Question 32
The correct order of increasing thermal stability of alkaline earth metal carbonates is:
(A) $\text{BeCO}_3 < \text{MgCO}_3 < \text{CaCO}_3 < \text{SrCO}_3 < \text{BaCO}_3$  
(B) $\text{BaCO}_3 < \text{SrCO}_3 < \text{CaCO}_3 < \text{MgCO}_3 < \text{BeCO}_3$  
(C) $\text{CaCO}_3 < \text{BeCO}_3 < \text{MgCO}_3 < \text{BaCO}_3 < \text{SrCO}_3$  
(D) $\text{MgCO}_3 < \text{BeCO}_3 < \text{CaCO}_3 < \text{SrCO}_3 < \text{BaCO}_3$

#### Question 33
The shape of the $\text{SF}_4$ molecule is:
(A) See-saw  
(B) Tetrahedral  
(C) Square planar  
(D) Trigonal bipyramidal

#### Question 34
In the reaction $\text{CH}_3\text{COOH} \xrightarrow{\text{LiAlH}_4} X \xrightarrow{\text{PBr}_3} Y \xrightarrow{\text{KCN}} Z$, the compound $Z$ is:
(A) Propanenitrile ($\text{CH}_3\text{CH}_2\text{CN}$)  
(B) Acetonitrile ($\text{CH}_3\text{CN}$)  
(C) Ethanamide ($\text{CH}_3\text{CONH}_2$)  
(D) Propanamide

#### Question 35
The vitamin whose deficiency causes scurvy is:
(A) Vitamin C  
(B) Vitamin B1  
(C) Vitamin D  
(D) Vitamin A

#### Question 36
The hybridization of cobalt in $[\text{Co}(\text{NH}_3)_6]^{3+}$ is:
(A) $d^2sp^3$  
(B) $sp^3d^2$  
(C) $sp^3$  
(D) $dsp^2$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^4 - 4x^3 + 10$:
(A) $f'(x) = 4x^2(x-3)$.  
(B) $x = 0$ is a stationary point of inflection (neither local maximum nor local minimum).  
(C) $x = 3$ is a point of absolute minimum with value $f(3) = -17$.  
(D) $f(x)$ is strictly increasing on $(3, \infty)$ and strictly decreasing on $(-\infty, 3)$.

#### Question 38
Let $A$ and $B$ be two $3 \times 3$ matrices such that $AB = 0$:
(A) If $A$ is invertible, then $B$ must be the zero matrix.  
(B) If $B$ is invertible, then $A$ must be the zero matrix.  
(C) $\det(A) = 0$ or $\det(B) = 0$.  
(D) $\text{rank}(A) + \text{rank}(B) \le 3$.

#### Question 39
Consider the ellipse $\frac{x^2}{25} + \frac{y^2}{16} = 1$:
(A) The eccentricity is $e = 3/5$.  
(B) The foci are at $(\pm 3, 0)$.  
(C) The length of the latus rectum is $32/5$.  
(D) The equations of the directrices are $x = \pm 25/3$.

#### Question 40
Let $I = \int_0^1 \frac{dx}{1 + x^2}$:
(A) $I = \frac{\pi}{4}$.  
(B) The substitution $x = \tan\theta$ converts the integral into $\int_0^{\pi/4} 1 d\theta$.  
(C) $\int_0^1 \frac{x}{1+x^2} dx = \frac{1}{2}\ln 2$.  
(D) $\int_0^\infty \frac{dx}{1+x^2} = \frac{\pi}{2}$.

#### Question 41
Let the vectors $\vec{a} = \hat{i} + \hat{j} + \hat{k}$, $\vec{b} = \hat{i} - \hat{j} + \hat{k}$, and $\vec{c} = \hat{i} + \hat{j} - \hat{k}$:
(A) The volume of the parallelepiped formed by $\vec{a}, \vec{b}, \vec{c}$ is $|[\vec{a}\quad \vec{b}\quad \vec{c}]| = 4$.  
(B) The vectors are linearly independent.  
(C) $\vec{a} \cdot \vec{b} = 1$.  
(D) $\vec{a} \times \vec{b} = 2\hat{i} - 2\hat{k}$.

#### Question 42
Consider the sequence $a_n = \frac{2n+1}{3n+2}$:
(A) $\lim_{n \to \infty} a_n = 2/3$.  
(B) The sequence is strictly increasing: $a_{n+1} > a_n$ for all $n \ge 1$.  
(C) The sequence is bounded: $3/5 \le a_n < 2/3$ for all $n \ge 1$.  
(D) The infimum is $3/5$ and supremum is $2/3$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = x^2$ and the line $y = 2x$. Round off to two decimal places.

#### Question 44
Find the remainder when $5^{2024}$ is divided by 7.

#### Question 45
Find the perpendicular distance from the point $(1, 1, 1)$ to the plane $x + 2y + 2z = 11$.

#### Question 46
Let $\alpha, \beta, \gamma$ be the roots of $x^3 - 7x + 6 = 0$. Find the value of $\alpha^2 + \beta^2 + \gamma^2$.

#### Question 47
Find the number of ways to arrange the letters of the word **SUCCESS**.

#### Question 48
Find the radius of the circle $x^2 + y^2 - 6x + 8y = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arctan(\sqrt{x})$ with respect to $x$ is:
(A) $\frac{1}{2\sqrt{x}(1+x)}$  
(B) $\frac{1}{1+x}$  
(C) $\frac{1}{\sqrt{x}(1+x)}$  
(D) $\frac{2}{\sqrt{x}(1+x)}$

#### Question 50
The differential equation of all circles with center at the origin is:
(A) $x + y \frac{dy}{dx} = 0$  
(B) $x - y \frac{dy}{dx} = 0$  
(C) $\frac{dy}{dx} = -\frac{y}{x}$  
(D) $y + x \frac{dy}{dx} = 0$

#### Question 51
The angle between the straight lines $y = (2-\sqrt{3})x + 5$ and $y = (2+\sqrt{3})x - 7$ is:
(A) $60^\circ$  
(B) $45^\circ$  
(C) $30^\circ$  
(D) $90^\circ$

#### Question 52
If $\binom{n}{4} = \binom{n}{6}$, then $n$ is equal to:
(A) 10  
(B) 12  
(C) 8  
(D) 14

#### Question 53
The period of $\cos(4x)$ is:
(A) $\pi/2$  
(B) $\pi$  
(C) $2\pi$  
(D) $\pi/4$

#### Question 54
A fair coin is tossed 6 times. The probability of getting exactly 4 heads is:
(A) $15/64$  
(B) $15/32$  
(C) $5/16$  
(D) $1/4$
"""

        raw_sol1 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 1)
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Sphere on accelerating conveyor belt: equations of motion $f = M a_{\text{cm}}$ and $f R = I \alpha = \frac{2}{5}M R^2 \alpha$. Rolling condition at contact: $a_c = a_{\text{cm}} - \alpha R = a_0$. Substituting gives $a_{\text{cm}} - \frac{5}{2}a_{\text{cm}} = a_0 \implies -\frac{3}{2}a_{\text{cm}} = a_0$ or with sign convention $a_c = a_{\text{cm}} + R\alpha = a_0 \implies a_{\text{cm}} + \frac{5}{2}a_{\text{cm}} = \frac{7}{2}a_{\text{cm}} = a_0 \implies a_{\text{cm}} = \frac{2}{7}a_0$. Friction $f = \frac{2}{7}M a_0 \le \mu_s M g \implies \mu_s \ge \frac{2a_0}{7g}$. **Correct Options**: (A, B, C, D)
- **Q2**: Compound pendulum: $I = I_{\text{cm}} + M d^2 = \frac{1}{12}M L^2 + M d^2$. Period $T = 2\pi\sqrt{\frac{I}{M g d}} = 2\pi\sqrt{\frac{L^2/12 + d^2}{gd}}$. Minimum period at $d = \frac{L}{\sqrt{12}}$. Four points have identical periods (two on each side of center). **Correct Options**: (A, B, C, D)
- **Q3**: Rotating liquid in cylinder: $dP = \rho \omega^2 r dr - \rho g dz \implies P(r, z) = P_0 + \frac{1}{2}\rho \omega^2 r^2 - \rho g(z - z_0)$. Free surface $P = P_0 \implies z(r) = z_0 + \frac{\omega^2 r^2}{2g}$. Height difference $h = \frac{\omega^2 R^2}{2g}$. Volume of paraboloid is half the circumscribing cylinder. **Correct Options**: (A, B, C, D)
- **Q4**: Particle in vertical cone: normal force $N\cos\alpha = mg \implies N = mg/\cos\alpha$ or with $\alpha$ to vertical $N\sin\alpha = mg \implies N = mg/\sin\alpha$. In horizontal plane $N\cos\alpha = m\omega^2 r$. With $r = h\tan\alpha$, $\omega = \sqrt{\frac{g}{h\tan^2\alpha}}$. Angular momentum about cone vertical axis is conserved. **Correct Options**: (A, B, C, D)
- **Q5**: Error analysis in simple pendulum: $g = 4\pi^2 L / T^2 = 4\pi^2 L / (t/N)^2 = 4\pi^2 N^2 L / t^2 \implies \frac{\Delta g}{g} = \frac{\Delta L}{L} + 2\frac{\Delta t}{t} = \frac{0.1}{100} + 2\frac{0.1}{100} = 0.001 + 0.002 = 0.3\%$. **Correct Options**: (A, B, C, D)
- **Q6**: Gyroscopic precession: torque $\tau = M g l \sin\theta = \frac{dL}{dt} = \Omega_p L \sin\theta \implies \Omega_p = \frac{Mgl}{I_3 \omega_s}$. Independent of $\theta$ in fast-spin limit. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: Cylinder pulled at axle: $F - f = m a$, $f r = I \alpha = \frac{1}{2}m r^2 (a/r) = \frac{1}{2}m a \implies f = \frac{1}{2}m a$. Thus $F = \frac{3}{2}m a \implies a = \frac{2F}{3m} = \frac{2 \times 30.0}{3 \times 4.0} = 5.0\text{ m/s}^2 \implies \mathbf{5.00}$.
- **Q8**: Continuity: $A_1 v_1 = A_2 v_2 \implies v_2 = \frac{40}{10} \times 2.0 = 8.0\text{ m/s}$. Bernoulli: $P_1 - P_2 = \frac{1}{2}\rho(v_2^2 - v_1^2) = \frac{1}{2}(1000)(64 - 4) = 500 \times 60 = 30000\text{ Pa} = 30.0\text{ kPa} \implies \mathbf{30.00}$.
- **Q9**: Stokes' law: $v_t = \frac{2}{9}\frac{r^2 g(\rho_s - \rho_f)}{\eta} = \frac{2}{9}\frac{(2 \times 10^{-3})^2(9.8)(7800 - 1200)}{0.90} = \frac{2}{9}\frac{(4 \times 10^{-6})(9.8)(6600)}{0.90} \approx 0.064\text{ m/s} = 6.40\text{ cm/s} \implies \mathbf{6.40}$.
- **Q10**: Least count $= 0.5 / 50 = 0.01\text{ mm}$. Observed reading $= 2.5 + 32 \times 0.01 = 2.82\text{ mm}$. Corrected reading $= 2.82 - (+0.03) = 2.79\text{ mm} \implies \mathbf{2.79}$.
- **Q11**: Energy conservation: $M g \frac{L}{2} = \frac{1}{2} I \omega^2 = \frac{1}{2}(\frac{1}{3}M L^2)\omega^2 \implies \omega = \sqrt{\frac{3g}{L}} = \sqrt{\frac{3 \times 9.8}{1.20}} = \sqrt{24.5} \approx 4.95\text{ rad/s} \implies \mathbf{4.95}$.
- **Q12**: $h_w \rho_w = \Delta h \rho_m \implies \Delta h = \frac{27.2 \times 1.0}{13.6} = 2.00\text{ cm} \implies \mathbf{2.00}$.

### Questions 13 to 18
- **Q13**: Distance from center of mass is $L/2 - L/4 = L/4$. Parallel axis theorem: $I = \frac{1}{12}M L^2 + M(L/4)^2 = \frac{1}{12}M L^2 + \frac{1}{16}M L^2 = \frac{7}{48}M L^2$. **Correct: (A)**.
- **Q14**: Momentum conservation at mean position: $m v_0 = (2m) v' \implies v' = v_0 / 2$. New amplitude $A' = v' / \omega' = (v_0/2)/\sqrt{k/(2m)} = \frac{v_0}{\sqrt{2}\sqrt{k/m}} = A / \sqrt{2}$. **Correct: (A)**.
- **Q15**: Jurin's law: $h = \frac{2T\cos\theta}{r\rho g} \implies h \propto 1/r \implies h_1 / h_2 = r_2 / r_1 = 1/2$. **Correct: (A)**.
- **Q16**: $\text{LC} = 1\text{ MSD} - 1\text{ VSD} = 1\text{ mm} - 0.9\text{ mm} = 0.1\text{ mm}$. **Correct: (A)**.
- **Q17**: Acceleration $a = \frac{g\sin\theta}{1 + I/(MR^2)}$. For solid sphere $I/(MR^2) = 2/5 = 0.40$; for cylinder $I/(MR^2) = 0.50$. Sphere has higher acceleration, reaches bottom first. **Correct: (A)**.
- **Q18**: Pressure is $2/3$ of translational kinetic energy per unit volume: $P = \frac{2}{3}E_v$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Conformational analysis of cyclohexanes: chair is global minimum, 1,3-diaxial interactions destabilize axial conformers, twist-boat is local minimum. **Correct Options**: (A, B, C, D)
- **Q20**: Stereochemical additions to alkenes: anti-addition of $\text{Br}_2$ to trans gives meso, to cis gives racemic pair. Syn catalytic hydrogenation. **Correct Options**: (A, B, C, D)
- **Q21**: Blast furnace extraction reactions. **Correct Options**: (A, B, C, D)
- **Q22**: Classification and structural units of silicates. **Correct Options**: (A, B, C, D)
- **Q23**: Michaelis-Menten enzyme kinetics. **Correct Options**: (A, B, C, D)
- **Q24**: Coordination isomerism types. **Correct Options**: (A, B, C, D)

### Questions 25 to 30
- **Q25**: Half-life $t_{1/2} = \frac{0.693}{0.0693} = 10.0\text{ min}$. Concentration drops to $12.5\% = (1/2)^3 \implies t = 3 t_{1/2} = 30.0\text{ min} \implies \mathbf{30.00}$.
- **Q26**: $[\text{OH}^-] = \sqrt{K_b c} = \sqrt{1.0 \times 10^{-5} \times 0.010} = \sqrt{1.0 \times 10^{-7}} \approx 3.16 \times 10^{-4}\text{ M}$. $\text{pOH} = 3.50 \implies \text{pH} = 14 - 3.50 = 10.50 \implies \mathbf{10.50}$.
- **Q27**: $\Delta G^\circ = -R T \ln K_p = -(8.314)(298)(-1.897) = +4699.9\text{ J/mol} \approx 4.70\text{ kJ/mol} \implies \mathbf{4.70}$.
- **Q28**: $\Delta T_b = K_b m = 0.512 \times \frac{18/180}{0.200} = 0.512 \times \frac{0.10}{0.200} = 0.512 \times 0.50 = 0.256\text{ K} \implies \mathbf{0.256}$.
- **Q29**: For simple cubic, $Z = 1$. $\rho = \frac{Z M}{N_A a^3} \implies M = \frac{\rho N_A a^3}{Z} = \frac{8.0 \times (6.02 \times 10^{23}) \times (3 \times 10^{-8})^3}{1} = 8.0 \times 6.02 \times 10^{23} \times 2.7 \times 10^{-23} \approx 130\text{ g/mol} \implies \mathbf{130.00}$.
- **Q30**: In $\text{Fe}_2(\text{CO})_9$, there are 3 bridging carbonyl ligands and 6 terminal carbonyl ligands $\implies \mathbf{3.00}$.

### Questions 31 to 36
- **Q31**: Phenol with chloroform/NaOH gives salicylaldehyde (o-hydroxybenzaldehyde). **Correct: (A)**.
- **Q32**: $\text{Ti}^{4+}$ has $d^0$ configuration (no $d-d$ transitions) $\implies$ colorless. **Correct: (A)**.
- **Q33**: $\text{XeOF}_4$ has 5 bond pairs and 1 lone pair $\implies$ square pyramidal. **Correct: (A)**.
- **Q34**: Primary alkyl halide with alkoxide proceeds via $\text{S}_N2$. **Correct: (A)**.
- **Q35**: Natural rubber is a polymer of isoprene (cis-1,4-polyisoprene). **Correct: (A)**.
- **Q36**: Bicarbonate $\text{HCO}_3^-$ loses $\text{H}^+$ to form carbonate $\text{CO}_3^{2-}$. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Wallis formulas and limits. **Correct Options**: (A, B, C, D)
- **Q38**: Orthogonal trajectories of parabolas $y = C x^2$ are ellipses $x^2 + 2y^2 = K^2$. **Correct Options**: (A, B, C, D)
- **Q39**: Intersection and angle between line and plane. **Correct Options**: (A, B, C, D)
- **Q40**: Analysis of cubic polynomial $P(x) = x^3 - 3x + 1$. Roots in three separated intervals. **Correct Options**: (A, B, C, D)
- **Q41**: Summation by parts / telescoping for $\sum k(k+1) = \frac{n(n+1)(n+2)}{3}$. **Correct Options**: (A, B, C, D)
- **Q42**: Standard elements of parabola $y^2 = 8x$. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Symmetry about $x=1$: Area $= 2 \int_0^1 (x^3 - 3x^2 + 2x)dx = 2 [x^4/4 - x^3 + x^2]_0^1 = 2(1/4 - 1 + 1) = 0.50 \implies \mathbf{0.50}$.
- **Q44**: Digits 0, 1, 2, 3, 4. First digit cannot be 0 ($4$ choices), remaining 4 digits in $4! = 24$ ways. Total $= 4 \times 24 = 96 \implies \mathbf{96.00}$.
- **Q45**: Series expansion $\sin x = x - x^3/6 + \dots \implies \frac{x - \sin x}{x^3} \to 1/6 \implies k = \mathbf{6.00}$.
- **Q46**: Line point $A(1, 2, 3)$, direction $\vec{u} = (2, 3, 6)$ with $|\vec{u}| = \sqrt{4+9+36} = 7$. Given point $P(2, 3, 4)$. $\vec{AP} = (1, 1, 1)$. $\vec{AP} \times \vec{u} = (1(6)-1(3), 1(2)-1(6), 1(3)-1(2)) = (3, -4, 1)$. Magnitude $= \sqrt{9+16+1} = \sqrt{26}$. Distance $d = \frac{\sqrt{26}}{7} \approx 0.73 \implies \mathbf{0.73}$.
- **Q47**: Eigenvalues of $A^2$ are $2^2 = 4$ and $5^2 = 25$. $\text{tr}(A^2) = 4 + 25 = 29 \implies \mathbf{29.00}$.
- **Q48**: Center $(1, 2, 3)$, $R = \sqrt{1^2 + 2^2 + 3^2 - (-11)} = \sqrt{1 + 4 + 9 + 11} = \sqrt{25} = 5.00 \implies \mathbf{5.00}$.

### Questions 49 to 54
- **Q49**: Chain rule: $\frac{1}{x \ln x}$. **Correct: (A)**.
- **Q50**: $\frac{dy}{dx} = \frac{y}{x} \implies \frac{dy}{y} = \frac{dx}{x} \implies \ln|y| = \ln|x| + C' \implies y = Cx$. **Correct: (A)**.
- **Q51**: For rectangular hyperbola, $a = b \implies e = \sqrt{1 + 1} = \sqrt{2}$. **Correct: (A)**.
- **Q52**: $\alpha^2 + \beta^2 = (\alpha+\beta)^2 - 2\alpha\beta = 5^2 - 2(6) = 25 - 12 = 13$. **Correct: (A)**.
- **Q53**: $\sin x \cos x = \frac{1}{2}\sin(2x) \le 1/2$. **Correct: (A)**.
- **Q54**: Seat 5 boys at circular table in $4!$ ways. 5 distinct spaces between them for 5 girls in $5!$ ways. Total $= 4! \times 5! = 2880$. **Correct: (A)**.
"""

        raw_sol2 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 2)
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Rolling down incline: acceleration $a = \frac{g\sin\theta}{1 + 2/5} = \frac{5}{7}g\sin\theta$. Friction $f_s = \frac{2}{7}Mg\sin\theta$. Critical friction $\mu_{\min} = \frac{2}{7}\tan\theta$. Rotational KE fraction is $2/7$. **Correct Options**: (A, B, C, D)
- **Q2**: U-tube oscillation: $F = -2\rho A g x$, total mass $M = \rho A L$. Equation: $\ddot{x} + \frac{2g}{L}x = 0 \implies T = 2\pi\sqrt{\frac{L}{2g}}$. Independent of $\rho$ and $A$. **Correct Options**: (A, B, C, D)
- **Q3**: Rotating reference frame fictitious forces: centrifugal $\vec{F}_{\text{cent}} = -m\vec{\omega}\times(\vec{\omega}\times\vec{r})$, Coriolis $\vec{F}_{\text{Cor}} = -2m(\vec{\omega}\times\vec{v}_{\text{rel}})$. Coriolis force is always perpendicular to $\vec{v}_{\text{rel}}$, hence does no work. Deflects right in northern hemisphere. **Correct Options**: (A, B, C, D)
- **Q4**: Resonance tube experiment: $\lambda/2 = l_2 - l_1 \implies \lambda = 2(l_2 - l_1)$. Speed $v = f\lambda = 2f(l_2 - l_1)$. End correction $e = \frac{l_2 - 3l_1}{2} \approx 0.6r$. **Correct Options**: (A, B, C, D)
- **Q5**: Annular disc moment of inertia: $I = \frac{1}{2}M(R_1^2 + R_2^2) = \frac{1}{2}M(R^2 + R^2/4) = \frac{5}{8}MR^2$. By perpendicular axis theorem, diameter moment of inertia is $\frac{5}{16}MR^2$. **Correct Options**: (A, B, C, D)
- **Q6**: Poiseuille's law parameters and fluid shear force on cylinder walls. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $E_{\text{rot}} = \frac{1}{2} I \omega^2 = \frac{1}{2}\left(\frac{2}{5}M R^2\right)\omega^2 = \frac{1}{5}(2.0)(0.10)^2(50)^2 = \frac{1}{5}(2.0)(0.01)(2500) = 10.0\text{ J} \implies \mathbf{10.00}$.
- **Q8**: $T \propto 1/\sqrt{g} \implies T' = T\sqrt{g/g'} = 2.00 / \sqrt{1.44} = 2.00 / 1.20 \approx 1.67\text{ s} \implies \mathbf{1.67}$.
- **Q9**: $Y = \frac{F L}{A \Delta L} = \frac{(5.0 \times 9.8)(2.0)}{(\pi \times (0.50 \times 10^{-3})^2)(0.80 \times 10^{-3})} = \frac{98}{3.14 \times 0.25 \times 10^{-6} \times 0.80 \times 10^{-3}} = \frac{98}{6.28 \times 10^{-10}} \approx 1.56 \times 10^{11}\text{ N/m}^2 \implies \mathbf{1.56}$.
- **Q10**: $Q = \frac{2}{3}(0.60)(1.50)\sqrt{2 \times 9.8}(0.25)^{1.5} = 0.60 \times 4.427 \times 0.125 \approx 0.33\text{ m}^3/\text{s} \implies \mathbf{0.33}$.
- **Q11**: Angular momentum conservation about pivot: $m_0 v_0 L = I_{\text{total}} \omega$. $I_{\text{total}} = \frac{1}{3}m L^2 + m_0 L^2 = (\frac{3.0}{3} + 0.05)(1.0)^2 = 1.05\text{ kg m}^2$. $\omega = \frac{0.05 \times 200 \times 1.0}{1.05} = \frac{10}{1.05} \approx 9.52\text{ rad/s} \implies \mathbf{9.52}$.
- **Q12**: Torricelli's theorem: $v = \sqrt{2gh} = \sqrt{2 \times 9.8 \times 5.0} = \sqrt{98} \approx 9.90\text{ m/s}$. Area $A = \pi (0.01)^2 \approx 3.14 \times 10^{-4}\text{ m}^2$. Discharge $Q = A v = 3.14 \times 10^{-4} \times 9.90 \approx 3.11 \times 10^{-3}\text{ m}^3/\text{s} = 3.1\text{ L/s} \implies \mathbf{3.10}$.

### Questions 13 to 18
- **Q13**: Center of mass of solid hemisphere is at $\frac{3}{8}R$ from flat base. **Correct: (A)**.
- **Q14**: $p = \sqrt{2mK} \implies p_1 / p_2 = \sqrt{m_1 / m_2}$. **Correct: (A)**.
- **Q15**: Buoyancy balances weight: $\rho V g = \sigma (f V) g \implies f = \rho / \sigma$. **Correct: (A)**.
- **Q16**: From $F = \eta A \frac{dv}{dx} \implies [\eta] = \frac{[\text{M L T}^{-2}]}{[\text{L}^2][\text{T}^{-1}]} = [\text{M L}^{-1}\text{ T}^{-1}]$. **Correct: (A)**.
- **Q17**: When speed decreases, tangential acceleration $\vec{a}_t$ opposes $\vec{v}$. The total acceleration $\vec{a} = \vec{a}_c + \vec{a}_t$ makes an obtuse angle with $\vec{v}$. **Correct: (A)**.
- **Q18**: Surface energy is conserved during isothermal coalescence in vacuum: $8\pi r_1^2 T + 8\pi r_2^2 T = 8\pi R^2 T \implies R^2 = r_1^2 + r_2^2$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: E2 stereoelectronic requirements (anti-coplanar / trans-diaxial). **Correct Options**: (A, B, C, D)
- **Q20**: Dieterici equation of state critical parameters and compressibility. **Correct Options**: (A, B, C, D)
- **Q21**: Extraction and metallurgy of copper: froth flotation, silicate slag, auto-reduction. **Correct Options**: (A, B, C, D)
- **Q22**: Le Chatelier's principle and equilibrium shift rules. **Correct Options**: (A, B, C, D)
- **Q23**: Stereochemistry and properties of biomolecules. **Correct Options**: (A, B, C, D)
- **Q24**: Geometrical isomerism: square planar $[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$ (*cis/trans*), octahedral $[\text{Co}(\text{NH}_3)_4\text{Cl}_2]^+$ and $[\text{Co}(\text{en})_2\text{Cl}_2]^+$. Tetrahedral does not show geometrical isomerism. **Correct Options**: (A, B, C)

### Questions 25 to 30
- **Q25**: $\frac{(2x)^2}{(1-x)^2} = 49 \implies \frac{2x}{1-x} = 7 \implies 2x = 7 - 7x \implies 9x = 7 \implies x = 7/9$. Moles of $\text{HI} = 2x = 14/9 \approx 1.56\text{ moles} \implies \mathbf{1.56}$.
- **Q26**: Common ion effect: $S = \frac{K_{\text{sp}}}{[\text{Cl}^-]} = \frac{1.8 \times 10^{-10}}{0.10} = 1.8 \times 10^{-9}\text{ M} \implies S = \mathbf{1.80}$.
- **Q27**: $E^\circ_{\text{cell}} = E^\circ(\text{Cd}^{2+}/\text{Cd}) - E^\circ(\text{Cr}^{3+}/\text{Cr}) = -0.40 - (-0.74) = +0.34\text{ V} \implies \mathbf{0.34}$.
- **Q28**: $\ln(k_2/k_1) = \frac{E_a}{R}\frac{\Delta T}{T_1 T_2} = \frac{50000}{8.314}\frac{10}{300 \times 310} = \frac{500000}{773202} \approx 0.6466$. Factor $= e^{0.6466} \approx 1.91 \implies \mathbf{1.91}$.
- **Q29**: $\Delta T_f = K_f m \implies 0.372 = K_f (0.20) \implies K_f = \frac{0.372}{0.20} = 1.86\text{ K kg mol}^{-1} \implies \mathbf{1.86}$.
- **Q30**: In $\text{I}_3^-$, the central iodine atom has 2 bond pairs and 3 lone pairs in equatorial positions $\implies \mathbf{3.00}$.

### Questions 31 to 36
- **Q31**: Acetophenone has a methyl ketone group ($\text{CH}_3-\text{C}=\text{O}$), hence gives positive iodoform test. **Correct: (A)**.
- **Q32**: Thermal stability of carbonates increases down Group 2 as cation size increases and polarizing power decreases. **Correct: (A)**.
- **Q33**: $\text{SF}_4$ has 4 bond pairs and 1 lone pair $\implies$ see-saw. **Correct: (A)**.
- **Q34**: $\text{CH}_3\text{COOH} \xrightarrow{\text{LiAlH}_4} \text{CH}_3\text{CH}_2\text{OH} \xrightarrow{\text{PBr}_3} \text{CH}_3\text{CH}_2\text{Br} \xrightarrow{\text{KCN}} \text{CH}_3\text{CH}_2\text{CN}$. **Correct: (A)**.
- **Q35**: Vitamin C deficiency causes scurvy. **Correct: (A)**.
- **Q36**: $[\text{Co}(\text{NH}_3)_6]^{3+}$ is a low-spin $d^6$ octahedral complex with $d^2sp^3$ hybridization. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Analysis of quartic function $f(x) = x^4 - 4x^3 + 10$. Inflection at $x=0$, minimum at $x=3$. **Correct Options**: (A, B, C, D)
- **Q38**: Properties of matrix product $AB = 0$. Sylvester's rank inequality. **Correct Options**: (A, B, C, D)
- **Q39**: Standard ellipse characteristics. **Correct Options**: (A, B, C, D)
- **Q40**: Definite integrals of $1/(1+x^2)$. **Correct Options**: (A, B, C, D)
- **Q41**: Parallelepiped volume and vector products. **Correct Options**: (A, B, C, D)
- **Q42**: Convergence and boundedness of rational sequence. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Intersection: $x^2 = 2x \implies x = 0, 2$. Area $= \int_0^2 (2x - x^2)dx = [x^2 - x^3/3]_0^2 = 4 - 8/3 = 4/3 \approx 1.33 \implies \mathbf{1.33}$.
- **Q44**: $5 \equiv -2 \pmod 7$. $5^3 = 125 \equiv -1 \pmod 7 \implies 5^6 \equiv 1 \pmod 7$. $2024 = 6 \times 337 + 2$. $5^{2024} \equiv (5^6)^{337} \times 5^2 \equiv 1 \times 25 \equiv 4 \pmod 7 \implies \mathbf{4.00}$.
- **Q45**: $d = \frac{|1 + 2(1) + 2(1) - 11|}{\sqrt{1^2 + 2^2 + 2^2}} = \frac{|5 - 11|}{3} = \frac{6}{3} = 2.00 \implies \mathbf{2.00}$.
- **Q46**: $\alpha^2 + \beta^2 + \gamma^2 = (\sum\alpha)^2 - 2\sum\alpha\beta = 0^2 - 2(-7) = 14 \implies \mathbf{14.00}$.
- **Q47**: Word SUCCESS: 7 letters (3 S's, 2 C's, 1 U, 1 E). Number of permutations $= \frac{7!}{3! 2!} = \frac{5040}{12} = 420 \implies \mathbf{420.00}$.
- **Q48**: Circle $x^2 + y^2 - 6x + 8y = 0 \implies (x-3)^2 + (y+4)^2 = 9 + 16 = 25 \implies R = 5.00 \implies \mathbf{5.00}$.

### Questions 49 to 54
- **Q49**: $\frac{d}{dx}\arctan(\sqrt{x}) = \frac{1}{1 + (\sqrt{x})^2} \times \frac{1}{2\sqrt{x}} = \frac{1}{2\sqrt{x}(1+x)}$. **Correct: (A)**.
- **Q50**: Circles $x^2 + y^2 = r^2 \implies 2x + 2y\frac{dy}{dx} = 0 \implies x + y\frac{dy}{dx} = 0$. **Correct: (A)**.
- **Q51**: $\tan\theta_1 = 2 - \sqrt{3} \implies \theta_1 = 15^\circ$. $\tan\theta_2 = 2 + \sqrt{3} \implies \theta_2 = 75^\circ$. Angle between them $= 75^\circ - 15^\circ = 60^\circ$. **Correct: (A)**.
- **Q52**: $\binom{n}{4} = \binom{n}{6} \implies n = 4 + 6 = 10$. **Correct: (A)**.
- **Q53**: Period of $\cos(kx)$ is $2\pi/k = 2\pi/4 = \pi/2$. **Correct: (A)**.
- **Q54**: Binomial distribution: $\binom{6}{4}(1/2)^6 = 15/64$. **Correct: (A)**.
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
| 7 | Physics | Sec 2 | Numerical | 5.00 |
| 8 | Physics | Sec 2 | Numerical | 30.00 |
| 9 | Physics | Sec 2 | Numerical | 6.40 |
| 10 | Physics | Sec 2 | Numerical | 2.79 |
| 11 | Physics | Sec 2 | Numerical | 4.95 |
| 12 | Physics | Sec 2 | Numerical | 2.00 |
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
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 25 | Chemistry | Sec 2 | Numerical | 30.00 |
| 26 | Chemistry | Sec 2 | Numerical | 10.50 |
| 27 | Chemistry | Sec 2 | Numerical | 4.70 |
| 28 | Chemistry | Sec 2 | Numerical | 0.256 |
| 29 | Chemistry | Sec 2 | Numerical | 130.00 |
| 30 | Chemistry | Sec 2 | Numerical | 3.00 |
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
| 43 | Mathematics | Sec 2 | Numerical | 0.50 |
| 44 | Mathematics | Sec 2 | Numerical | 96.00 |
| 45 | Mathematics | Sec 2 | Numerical | 6.00 |
| 46 | Mathematics | Sec 2 | Numerical | 0.73 |
| 47 | Mathematics | Sec 2 | Numerical | 29.00 |
| 48 | Mathematics | Sec 2 | Numerical | 5.00 |
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
| 7 | Physics | Sec 2 | Numerical | 10.00 |
| 8 | Physics | Sec 2 | Numerical | 1.67 |
| 9 | Physics | Sec 2 | Numerical | 1.56 |
| 10 | Physics | Sec 2 | Numerical | 0.33 |
| 11 | Physics | Sec 2 | Numerical | 9.52 |
| 12 | Physics | Sec 2 | Numerical | 3.10 |
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
| 25 | Chemistry | Sec 2 | Numerical | 1.56 |
| 26 | Chemistry | Sec 2 | Numerical | 1.80 |
| 27 | Chemistry | Sec 2 | Numerical | 0.34 |
| 28 | Chemistry | Sec 2 | Numerical | 1.91 |
| 29 | Chemistry | Sec 2 | Numerical | 1.86 |
| 30 | Chemistry | Sec 2 | Numerical | 3.00 |
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
| 43 | Mathematics | Sec 2 | Numerical | 1.33 |
| 44 | Mathematics | Sec 2 | Numerical | 4.00 |
| 45 | Mathematics | Sec 2 | Numerical | 2.00 |
| 46 | Mathematics | Sec 2 | Numerical | 14.00 |
| 47 | Mathematics | Sec 2 | Numerical | 420.00 |
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
    generate_roorkee_01_to_05()

