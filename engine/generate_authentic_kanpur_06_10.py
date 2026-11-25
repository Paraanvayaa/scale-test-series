"""
IIT Kanpur Mocks 06 to 10 Generator
Organising Institute: Indian Institute of Technology Kanpur
Empirical Benchmark: 2001, 2007, 2011, 2018 Official JEE Advanced Papers
Features:
- Extreme numerical rigor and calculation depth (>= 38% numerical value questions)
- Non-ideal gases (Dieterici, Berthelot), fluid dynamics with viscous drag, coupled oscillators
- Multi-component ionic equilibria, solubility product in complex matrices, reaction kinetics
- Advanced calculus, differential equations, matrices and vector invariants, complex Argand loci
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_kanpur_06_to_10():
    for mock_idx in range(6, 11):
        pad = f"{mock_idx:02d}"
        incline_a = str(30 + (mock_idx % 3) * 5)
        mag_b = str(0.40 + (mock_idx % 4) * 0.10)
        sol_conc = str(0.020 + (mock_idx % 3) * 0.010)
        integ_n = str(3 + (mock_idx % 3))

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
A uniform solid sphere of mass $M$ and radius $R$ is placed on an inclined plane of inclination angle $\theta = __INCLINE_A__^\circ$. A horizontal force $F$ is applied at the highest point of the sphere directed towards the incline. The coefficient of static friction is $\mu$:
(A) For pure rolling down the incline, the acceleration of the sphere is $a_{cm} = \frac{5}{7}g\sin\theta + \frac{10}{7}\frac{F}{M}\cos^2(\theta/2)$.  
(B) Friction can act either up or down the incline depending on the magnitude of $F$.  
(C) If $F = \frac{2}{5}M g\sin\theta$, the frictional force on the sphere vanishes completely.  
(D) Slipping is inevitable if the required static friction exceeds $\mu M g \cos\theta$.

#### Question 2
Two identical monoatomic ideal gas containers A and B each of volume $V_0$ at temperature $T_0$ and pressure $P_0$ are connected by a thin tube of negligible volume containing a porous plug. Container A is heated to $2T_0$ while B is maintained at $T_0$. In the steady state of thermal effusion:
(A) The final pressures in the two containers are unequal.  
(B) The ratio of steady-state pressures is $P_A / P_B = \sqrt{2}$.  
(C) The ratio of the number of moles of gas in container A to container B is $n_A / n_B = 1/\sqrt{2}$.  
(D) The total number of moles of gas $n_A + n_B$ is conserved and equals $2 P_0 V_0 / (R T_0)$.

#### Question 3
A grounded conducting sphere of radius $R$ is centered at the origin. A point charge $q$ is located on the $z$-axis at distance $d > R$ from the origin:
(A) The electric potential for $r \ge R$ can be solved using an image charge $q' = -q \frac{R}{d}$ placed at distance $d' = \frac{R^2}{d}$ from the center.  
(B) The net induced charge on the spherical surface is $q_{\text{ind}} = -q \frac{R}{d}$.  
(C) The attractive force between the charge $q$ and the grounded sphere is $F = \frac{q^2 R d}{4\pi\varepsilon_0 (d^2 - R^2)^2}$.  
(D) The electrostatic potential at any point on the surface of the sphere is zero.

#### Question 4
A rectangular conducting loop of mass $m$, resistance $R$, and dimensions $a \times b$ falls vertically in a horizontal magnetic field $B(y) = B_0(1 + \alpha y)\hat{k}$, where $y$ is the downward vertical coordinate:
(A) The magnetic flux through the loop varies linearly with vertical displacement $y$.  
(B) The induced EMF in the loop is $\mathcal{E} = B_0 \alpha a b v$, where $v = \dot{y}$.  
(C) The terminal velocity achieved by the falling loop is $v_t = \frac{m g R}{B_0^2 \alpha^2 a^2 b^2}$.  
(D) At terminal velocity, the rate of loss of gravitational potential energy equals the rate of Joule heating.

#### Question 5
In an interference experiment using a Fresnel biprism of refractive index $\mu = 1.50$ and small refracting angle $\alpha = 1^\circ$, light from a slit of wavelength $\lambda = 600\text{ nm}$ placed at distance $u = 20\text{ cm}$ from the biprism illuminates a screen placed at distance $v = 80\text{ cm}$ from the biprism:
(A) The separation between the two virtual coherent sources is $d = 2 u(\mu - 1)\alpha$.  
(B) The fringe width on the screen is $\beta = \frac{\lambda(u + v)}{d}$.  
(C) Total width of the interference region on the screen is $W = \frac{v}{u} d$.  
(D) If the biprism is rotated by $90^\circ$ about the optical axis, the fringes remain vertical.

#### Question 6
A beam of monoenergetic $\alpha$-particles with kinetic energy $K = 6.0\text{ MeV}$ is directed normally onto a thin gold foil ($Z = 79$):
(A) The distance of closest approach for a head-on collision is $d_{\min} = \frac{2 Z e^2}{4\pi\varepsilon_0 K}$.  
(B) For gold, $d_{\min} \approx 3.8 \times 10^{-14}\text{ m} = 38\text{ fm}$.  
(C) The differential scattering cross-section is proportional to $\csc^4(\theta/2)$.  
(D) The impact parameter $b$ for scattering angle $\theta = 90^\circ$ is equal to $d_{\min}/2$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A cylindrical container of base radius $R = 0.20\text{ m}$ is filled with an incompressible liquid to height $H = 1.00\text{ m}$. The container is rotated about its vertical axis of symmetry at angular speed $\omega = 10.0\text{ rad/s}$. Taking $g = 10.0\text{ m/s}^2$, the height difference between the liquid surface at the edge and at the center is ______ m. (Round off to two decimal places)

#### Question 8
For Berthelot's equation of state $\left(P + \frac{a}{T V_m^2}\right)(V_m - b) = R T$, the critical volume is $V_c = 3b$. The critical compressibility factor $Z_c = \frac{P_c V_c}{R T_c}$ is ______ . (Round off to three decimal places)

#### Question 9
A square loop of wire of side $a = 0.10\text{ m}$ carrying current $I = 2.0\text{ A}$ is placed in a uniform magnetic field $B = __MAG_B__\text{ T}$ oriented at $60^\circ$ to the normal of the loop. The magnitude of the torque on the loop is $X \times 10^{-3}\text{ N}\cdot\text{m}$. The value of $X$ is ______ . (Round off to two decimal places)

#### Question 10
In a coupled LC circuit, two identical LC circuits each with $L = 0.10\text{ H}$ and $C = 10.0\ \mu\text{F}$ are coupled through a mutual inductance $M = 0.02\text{ H}$. The higher normal mode frequency $\omega_+$ is ______ rad/s. (Round off to two decimal places)

#### Question 11
A source of sound emitting frequency $f = 680\text{ Hz}$ moves with speed $v_s = 20.0\text{ m/s}$ towards a stationary reflecting vertical wall. Speed of sound in air is $340\text{ m/s}$. A stationary observer standing behind the source hears beats of frequency ______ Hz.

#### Question 12
A particle of mass $m = 0.20\text{ kg}$ executes simple harmonic motion along the $x$-axis. Its potential energy is $V(x) = 10 x^2\text{ J}$ ($x$ in meters). The time period of oscillation is ______ s. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle moves in a central force field with potential $V(r) = -k/r^2$ ($k > 0$). If the angular momentum is $L$, the particle spirals into the center when:  
(A) $L < \sqrt{2mk}$  
(B) $L > \sqrt{2mk}$  
(C) $L = \sqrt{mk}$  
(D) $L > 2\sqrt{mk}$

#### Question 14
Two point charges $+4q$ and $-q$ are fixed at a distance $d$ apart on the $x$-axis. The locus of points where the electrostatic potential is zero is a sphere of radius:  
(A) $\frac{4}{15}d$  
(B) $\frac{2}{3}d$  
(C) $\frac{4}{5}d$  
(D) $\frac{1}{3}d$

#### Question 15
A ray of light is incident at Brewster's angle on a glass slab of refractive index $n = \sqrt{3}$. The angle of refraction inside the slab is:  
(A) $30^\circ$  
(B) $60^\circ$  
(C) $45^\circ$  
(D) $15^\circ$

#### Question 16
A diatomic ideal gas ($\gamma = 7/5$) expands adiabatically until its volume is doubled ($V_2 = 2V_1$). The ratio of final temperature to initial temperature $T_2 / T_1$ is:  
(A) $2^{-0.4} \approx 0.758$  
(B) $0.500$  
(C) $2^{-0.6} \approx 0.660$  
(D) $0.800$

#### Question 17
A toroid of circular cross-section has inner radius $r_1 = 10\text{ cm}$ and outer radius $r_2 = 12\text{ cm}$. It has $N = 1000\text{ turns}$ carrying current $I = 2.0\text{ A}$. The magnetic field at the mean radius is:  
(A) $3.64\times 10^{-3}\text{ T}$  
(B) $1.82\times 10^{-3}\text{ T}$  
(C) $7.28\times 10^{-3}\text{ T}$  
(D) $0.91\times 10^{-3}\text{ T}$

#### Question 18
The de Broglie wavelength of a thermal neutron at temperature $T = 300\text{ K}$ is approximately:  
(A) $0.18\text{ nm}$  
(B) $1.8\text{ nm}$  
(C) $0.018\text{ nm}$  
(D) $18\text{ nm}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an amphoteric metal hydroxide $\text{M(OH)}_2(s)$ in contact with aqueous solution, the relevant equilibria are:  
$\text{M(OH)}_2(s) \rightleftharpoons \text{M}^{2+} + 2\text{OH}^-$ with $K_{sp} = 1.0 \times 10^{-16}$  
$\text{M(OH)}_2(s) + 2\text{OH}^- \rightleftharpoons [\text{M(OH)}_4]^{2-}$ with $K_f = 1.0 \times 10^{-4}$  
(A) The total solubility of the metal species is $S = [\text{M}^{2+}] + [[\text{M(OH)}_4]^{2-}]$.  
(B) At low pH (acidic media), solubility is dominated by $[\text{M}^{2+}]$.  
(C) At high pH (strongly alkaline media), solubility is dominated by $[[\text{M(OH)}_4]^{2-}]$.  
(D) The pH of minimum solubility is $\text{pH} = 11.0$.

#### Question 20
Regarding the spin-crossover phenomenon in octahedral iron(II) complexes ($d^6$):
(A) In high-spin state ($t_{2g}^4 e_g^2$), the complex is paramagnetic with 4 unpaired electrons.  
(B) In low-spin state ($t_{2g}^6 e_g^0$), the complex is diamagnetic.  
(C) Spin crossover occurs when crystal field splitting $\Delta_o$ is approximately equal to the mean pairing energy $P$.  
(D) High-spin complexes typically have shorter metal-ligand bond lengths than low-spin complexes.

#### Question 21
For the complete combustion of one mole of liquid benzene at $298\text{ K}$:  
$\text{C}_6\text{H}_6(l) + \frac{15}{2}\text{O}_2(g) \rightarrow 6\text{CO}_2(g) + 3\text{H}_2\text{O}(l)$ with $\Delta H^\circ = -3267\text{ kJ/mol}$:
(A) The change in gaseous moles is $\Delta n_g = 6 - 7.5 = -1.5\text{ mol}$.  
(B) $\Delta U^\circ = \Delta H^\circ - \Delta n_g R T = -3267 - (-1.5 \times 8.314 \times 298 \times 10^{-3}) = -3263.3\text{ kJ/mol}$.  
(C) The work done on the system by the surroundings during reversible reaction at constant $P$ is $1.5 R T$.  
(D) $\Delta S^\circ$ for this combustion reaction is strictly negative.

#### Question 22
Which of the following reaction sequences will convert bromobenzene to benzoic acid?
(A) (i) $\text{Mg} / \text{dry ether}$; (ii) $\text{CO}_2$; (iii) $\text{H}_3\text{O}^+$  
(B) (i) $\text{CuCN} / \text{pyridine}, \Delta$; (ii) $\text{H}_3\text{O}^+, \Delta$  
(C) (i) $\text{CH}_3\text{Cl} / \text{anhy. AlCl}_3$; (ii) $\text{alk. KMnO}_4, \Delta$; (iii) $\text{H}_3\text{O}^+$  
(D) (i) $\text{HNO}_3 / \text{H}_2\text{SO}_4$; (ii) $\text{Sn} / \text{HCl}$; (iii) $\text{NaNO}_2 / \text{HCl}$; (iv) $\text{CuCN}$

#### Question 23
In the cyanide extraction process (MacArthur-Forrest process) for native gold:
(A) Gold is dissolved by cyanide in the presence of atmospheric oxygen acting as oxidizing agent.  
(B) The soluble complex formed is sodium dicyanoaurate(I) $\text{Na}[\text{Au(CN)}_2]$.  
(C) Gold is precipitated from the solution by addition of powdered zinc metal.  
(D) Zinc undergoes oxidation from $0$ to $+2$ state forming $[\text{Zn(CN)}_4]^{2-}$.

#### Question 24
Regarding the allotropes and compounds of sulfur:
(A) Rhombic sulfur ($\alpha\text{-S}$) is thermodynamically stable below $369\text{ K}$.  
(B) Both rhombic and monoclinic sulfur contain crown-shaped $\text{S}_8$ rings.  
(C) Liquid sulfur exhibits a dramatic increase in viscosity around $433\text{ K}$ due to the opening of $\text{S}_8$ rings and polymerization into long chains.  
(D) Sulfur dioxide ($\text{SO}_2$) gas acts both as a reducing agent and an oxidizing agent.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of ferric hydroxide $\text{Fe(OH)}_3$ is $K_{sp} = 1.0 \times 10^{-38}$. The pH at which $\text{Fe}^{3+}$ ions just begin to precipitate from a $0.010\text{ M}\ \text{FeCl}_3$ solution is ______ . (Round off to two decimal places)

#### Question 26
A substance undergoes parallel first-order decay with rate constants $k_1 = 0.030\text{ hr}^{-1}$ and $k_2 = 0.015\text{ hr}^{-1}$. The composite half-life of the substance is ______ hours. (Take $\ln 2 = 0.693$, round off to two decimal places)

#### Question 27
A $0.500\text{ molal}$ aqueous solution of $\text{KCl}$ is $90\%$ dissociated. Taking $K_f = 1.86\text{ K}\cdot\text{kg/mol}$ for water, the depression in freezing point $\Delta T_f$ is ______ K. (Round off to two decimal places)

#### Question 28
The effective magnetic moment of a high-spin complex $[\text{Cr}(\text{H}_2\text{O})_6]^{3+}$ is ______ BM. (Round off to two decimal places)

#### Question 29
A buffer solution of volume $1.0\text{ L}$ contains $0.20\text{ M}\ \text{NH}_4\text{OH}$ and $0.20\text{ M}\ \text{NH}_4\text{Cl}$. If $K_b(\text{NH}_4\text{OH}) = 1.8 \times 10^{-5}$, the pH of the buffer is ______ . (Take $\log_{10}(1.8) = 0.255$, round off to two decimal places)

#### Question 30
The standard electromotive force $E^\circ$ of the cell $\text{Cd}(s) \mid \text{Cd}^{2+}(aq) \parallel \text{Ag}^+(aq) \mid \text{Ag}(s)$ is $+1.20\text{ V}$. Taking $F = 96500\text{ C/mol}$, the equilibrium constant $\log_{10} K$ at $298\text{ K}$ is ______ . (Take $2.303 R T / F = 0.0591\text{ V}$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product obtained when ethyl acetoacetate is treated with sodium ethoxide followed by ethyl iodide and subsequent acidic hydrolysis is:  
(A) Pentan-2-one  
(B) Hexan-2-one  
(C) Hexan-3-one  
(D) Butan-2-one

#### Question 32
The number of bridging oxo ligands in $\text{Cr}_2\text{O}_7^{2-}$ is:  
(A) $1$  
(B) $2$  
(C) $0$  
(D) $3$

#### Question 33
In the zone refining method, purification is based on the principle that:  
(A) Impurities are more soluble in the molten state than in the solid state of the metal  
(B) Impurities have higher boiling points  
(C) Metal is volatile while impurities are non-volatile  
(D) Impurities form water-soluble complexes

#### Question 34
Which of the following reagents can distinguish between propan-1-ol and propan-2-ol?  
(A) Lucas reagent ($\text{anhy. ZnCl}_2 + \text{conc. HCl}$)  
(B) Tollens' reagent  
(C) Fehling's solution  
(D) Sodium bicarbonate

#### Question 35
The monomer of natural rubber is:  
(A) Isoprene (2-methylbuta-1,3-diene)  
(B) Chloroprene (2-chlorobuta-1,3-diene)  
(C) Neoprene  
(D) 1,3-Butadiene

#### Question 36
Deficiency of Vitamin B1 (Thiamine) leads to:  
(A) Beriberi  
(B) Rickets  
(C) Pellagra  
(D) Cheilosis

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \arctan x - \frac{x}{1 + x^2}$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ is an odd function.  
(B) $f'(x) = \frac{2x^2}{(1 + x^2)^2} \ge 0$ for all $x \in \mathbb{R}$.  
(C) $f(x)$ is strictly increasing on $\mathbb{R}$.  
(D) $\lim_{x \to \infty} f(x) = \pi/2$.

#### Question 38
For the family of confocal conics $\frac{x^2}{a^2 - \lambda} + \frac{y^2}{b^2 - \lambda} = 1$ ($a > b > 0$):
(A) For $\lambda < b^2$, the curves represent ellipses.  
(B) For $b^2 < \lambda < a^2$, the curves represent hyperbolas.  
(C) Through any point $(x_0, y_0)$ with $x_0 y_0 \neq 0$, there pass exactly two conics of the confocal system: one ellipse and one hyperbola.  
(D) The two confocal conics passing through $(x_0, y_0)$ intersect orthogonally.

#### Question 39
For complex numbers $z$ satisfying $|z - 2| + |z + 2| = 6$:
(A) The locus of $z$ is an ellipse in the Argand plane.  
(B) The foci are at $(\pm 2, 0)$ and the semi-major axis is $a = 3$.  
(C) The maximum value of $|z|$ is $3$.  
(D) The minimum value of $|z|$ is $\sqrt{5}$.

#### Question 40
Let $A$ be a $3 \times 3$ nilpotent matrix such that $A^3 = 0$ but $A^2 \neq 0$:
(A) All eigenvalues of $A$ are zero.  
(B) $\operatorname{Tr}(A) = 0$ and $\det(A) = 0$.  
(C) The matrix $I + A$ is invertible, with $(I + A)^{-1} = I - A + A^2$.  
(D) $\operatorname{rank}(A) \le 2$.

#### Question 41
Let $J_n = \int_0^{\pi/2} \cos^n x \, dx$ for $n \ge 0$. Which of the following statements is/are correct?
(A) $J_n = \frac{n-1}{n} J_{n-2}$ for $n \ge 2$.  
(B) $J_0 = \pi/2$ and $J_1 = 1$.  
(C) $J_4 = \frac{3\pi}{16}$.  
(D) $\lim_{n \to \infty} \sqrt{n} J_n = \sqrt{\pi/2}$ (Wallis' formula).

#### Question 42
The lines $L_1: \frac{x-2}{1} = \frac{y-3}{2} = \frac{z-4}{3}$ and $L_2: \frac{x-1}{-1} = \frac{y-4}{1} = \frac{z-2}{2}$:
(A) Are skew lines.  
(B) The shortest distance between $L_1$ and $L_2$ is $\frac{7}{\sqrt{35}} = \sqrt{\frac{7}{5}}$.  
(C) The line of shortest distance is perpendicular to both $L_1$ and $L_2$.  
(D) Both lines intersect at a unique real point.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area of the region bounded by $y = e^x$, $y = e^{-x}$, and the line $x = 1$ is ______ . (Take $e = 2.718$, round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^1 x^3(1 - x)^4 \, dx$ is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real roots of the polynomial equation $x^5 - 5x + 1 = 0$ is ______ .

#### Question 46
Let $\vec{a} = 3\hat{i} - 2\hat{j} + 6\hat{k}$. The angle that $\vec{a}$ makes with the positive $z$-axis has cosine equal to $\frac{p}{7}$. The value of $p$ is ______ .

#### Question 47
A problem in mathematics is given to three students whose chances of solving it are $1/2$, $1/3$, and $1/4$ respectively. The probability that the problem is solved is $\frac{p}{4}$. The value of $p$ is ______ .

#### Question 48
The radius of the circle formed by the intersection of the sphere $x^2 + y^2 + z^2 = 25$ and the plane $x + 2y + 2z = 9$ is ______ . (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\ln(\sqrt{x + 1} + \sqrt{x - 1})$ with respect to $x$ for $x > 1$ is:  
(A) $\frac{1}{2\sqrt{x^2 - 1}}$  
(B) $\frac{1}{\sqrt{x^2 - 1}}$  
(C) $\frac{1}{2\sqrt{x + 1}}$  
(D) $\frac{x}{\sqrt{x^2 - 1}}$

#### Question 50
The angle between the asymptotes of the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ is:  
(A) $2\arctan(b/a)$  
(B) $\arctan(b/a)$  
(C) $2\arctan(a/b)$  
(D) $\pi/2$

#### Question 51
The value of $\lim_{x \to 0} \frac{x - \sin x}{x(1 - \cos x)}$ is:  
(A) $1/3$  
(B) $2/3$  
(C) $1/6$  
(D) $0$

#### Question 52
If $A$ is an invertible matrix of order $n$, then $\det(\operatorname{adj}(A))$ is:  
(A) $(\det A)^{n-1}$  
(B) $(\det A)^n$  
(C) $\det A$  
(D) $(\det A)^{n-2}$

#### Question 53
The number of ways in which 5 boys and 5 girls can sit alternately around a circular table is:  
(A) $4! \times 5! = 2880$  
(B) $5! \times 5!$  
(C) $9!$  
(D) $2 \times 4! \times 5!$

#### Question 54
The general solution of the differential equation $\frac{dy}{dx} + \frac{2x}{1 + x^2} y = \frac{1}{(1 + x^2)^2}$ is:  
(A) $y(1 + x^2) = \arctan x + C$  
(B) $y = (1 + x^2)\arctan x + C$  
(C) $y(1 + x^2) = \ln(1 + x^2) + C$  
(D) $y = \frac{\arctan x + C}{1 + x^2}$
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
A real gas follows the Dieterici equation of state $P(V_m - b)\exp\left(\frac{a}{R T V_m}\right) = R T$. Which of the following statements is/are correct?
(A) The critical volume is $V_c = 2b$.  
(B) The critical temperature is $T_c = \frac{a}{4 R b}$.  
(C) The critical pressure is $P_c = \frac{a}{4 e^2 b^2}$.  
(D) The critical compressibility factor is $Z_c = 2 e^{-2} \approx 0.271$.

#### Question 2
A solid non-conducting sphere of radius $R$ has a non-uniform volume charge density $\rho(r) = \rho_0(1 - r/R)$ for $r \le R$. The sphere is surrounded by vacuum:
(A) The total charge of the sphere is $Q = \frac{\pi}{3}\rho_0 R^3$.  
(B) The electric field strength is maximum at radial distance $r = \frac{2}{3}R$.  
(C) The electric field outside the sphere ($r > R$) is $\frac{Q}{4\pi\varepsilon_0 r^2}$.  
(D) The electrostatic potential at the center of the sphere is finite and strictly positive.

#### Question 3
A uniform ladder of mass $M$ and length $L$ leans against a smooth vertical wall with its base on a rough horizontal floor (coefficient of static friction $\mu$). The ladder makes an angle $\theta$ with the horizontal:
(A) The normal reaction from the wall is $N_w = \frac{1}{2}M g \cot\theta$.  
(B) The normal reaction from the floor is $N_f = M g$.  
(C) The ladder remains in equilibrium without slipping if $\tan\theta \ge \frac{1}{2\mu}$.  
(D) If a person of mass $m$ climbs the ladder, the tendency to slip increases as the person ascends.

#### Question 4
A long solenoid of radius $a$, $n$ turns per unit length, carries an alternating current $I(t) = I_0 \sin(\omega t)$. A single circular loop of wire of radius $b > a$ and resistance $R$ is placed coaxially around the solenoid:
(A) The magnetic flux linked with the external loop is $\Phi(t) = \mu_0 n I_0 \pi a^2 \sin(\omega t)$.  
(B) The induced EMF in the loop is $\mathcal{E}(t) = -\mu_0 n I_0 \pi a^2 \omega \cos(\omega t)$.  
(C) The induced electric field at distance $r > a$ from the axis is $E(r, t) = -\frac{\mu_0 n I_0 a^2 \omega}{2r}\cos(\omega t)$.  
(D) The Poynting vector outside the solenoid points radially inward during periods when the magnetic field is increasing.

#### Question 5
In an experiment to measure the speed of light using Fizeau's toothed wheel method:
(A) The light beam passes through a rotating toothed wheel having $N$ teeth and $N$ equal gaps.  
(B) Light travels a distance $2D$ to a distant mirror and returns.  
(C) First eclipse occurs when the wheel rotates by an angle $\theta = \frac{\pi}{2N}$ during the transit time $2D/c$.  
(D) The speed of light is given by $c = \frac{4 N D \omega}{\pi}$.

#### Question 6
An electron in a one-dimensional infinite potential well of width $L$ is in the first excited state ($n = 2$):
(A) The wave function is $\psi_2(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{2\pi x}{L}\right)$ for $0 \le x \le L$.  
(B) The probability density vanishes at $x = L/2$.  
(C) The probability of finding the electron in the middle third ($L/3 \le x \le 2L/3$) is $1/3 + \frac{\sqrt{3}}{4\pi}$.  
(D) The expectation value of momentum $\langle p \rangle$ is identically zero.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a hydrogen discharge tube, the shortest wavelength in the Balmer series is $\lambda_B$. Taking Rydberg constant $R_{\infty} = 1.097 \times 10^7\text{ m}^{-1}$, the value of $\lambda_B$ is ______ nm. (Round off to two decimal places)

#### Question 8
Two moles of an ideal diatomic gas ($\gamma = 1.40$) are heated at constant pressure from $300\text{ K}$ to $400\text{ K}$. Taking $R = 8.314\text{ J/(mol}\cdot\text{K)}$, the heat supplied $Q$ is ______ J. (Round off to two decimal places)

#### Question 9
A circular disc of mass $M = 6.0\text{ kg}$ and radius $R = 0.50\text{ m}$ is rotating at $\omega_0 = 40.0\text{ rad/s}$. Another identical disc initially at rest is placed gently coaxially on top of it. The common angular velocity of the two discs after slipping ceases is ______ rad/s.

#### Question 10
An inductor of inductance $L = 0.50\text{ H}$ and a resistor of resistance $R = 100\ \Omega$ are connected in series across a $200\text{ V}, 50\text{ Hz}$ AC source. The power dissipated in the circuit is ______ W. (Take $\pi = 3.14$, round off to two decimal places)

#### Question 11
Two loudspeakers emit sound waves of frequency $680\text{ Hz}$ in phase. A listener walks along a line parallel to the speakers at distance $D = 4.0\text{ m}$. If the distance between the speakers is $d = 1.0\text{ m}$ and speed of sound is $340\text{ m/s}$, the distance between consecutive intensity maxima on the listener's line is ______ m. (Round off to two decimal places)

#### Question 12
A block of mass $m = 1.0\text{ kg}$ attached to a horizontal spring of stiffness $k = 100\text{ N/m}$ is displaced by $0.10\text{ m}$ and released from rest. The time taken to travel from the initial position to $x = +0.05\text{ m}$ for the first time is ______ s. (Take $\pi = 3.14$, round off to three decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A body of mass $m$ is suspended from a vertical spring of spring constant $k$. It is pulled down by a distance $A$ from its equilibrium position and released from rest. The maximum tension in the spring during subsequent oscillation is:  
(A) $m g + k A$  
(B) $k A$  
(C) $m g - k A$  
(D) $2 m g + k A$

#### Question 14
Two concentric thin spherical conducting shells have radii $a$ and $b$ ($a < b$). The inner shell is given a charge $Q$ and the outer shell is grounded. The capacitance of the system is:  
(A) $4\pi\varepsilon_0 \frac{a b}{b - a}$  
(B) $4\pi\varepsilon_0 b$  
(C) $4\pi\varepsilon_0 \frac{a^2}{b - a}$  
(D) $4\pi\varepsilon_0(b - a)$

#### Question 15
A convex lens of focal length $f = 20\text{ cm}$ produces a real image 3 times magnified. The distance of the object from the lens is:  
(A) $26.67\text{ cm}$  
(B) $20.00\text{ cm}$  
(C) $15.00\text{ cm}$  
(D) $30.00\text{ cm}$

#### Question 16
The efficiency of a Carnot engine operating between temperatures $T_H = 600\text{ K}$ and $T_C = 300\text{ K}$ is:  
(A) $50\%$  
(B) $66.7\%$  
(C) $33.3\%$  
(D) $75\%$

#### Question 17
A proton and an alpha particle enter a uniform magnetic field with the same kinetic energy perpendicular to the field. The ratio of the radius of the proton orbit to that of the alpha particle orbit is:  
(A) $1 : 1$  
(B) $1 : 2$  
(C) $2 : 1$  
(D) $1 : \sqrt{2}$

#### Question 18
In photoelectric effect, if the frequency of incident radiation is doubled (keeping $h\nu > \Phi$), the maximum kinetic energy of emitted photoelectrons:  
(A) More than doubles  
(B) Doubles exactly  
(C) Increases but less than doubles  
(D) Remains unchanged

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For the selective precipitation of metal sulphides $\text{CuS}$ ($K_{sp} = 6.0 \times 10^{-36}$) and $\text{ZnS}$ ($K_{sp} = 1.6 \times 10^{-24}$) from an aqueous solution containing $0.010\text{ M}$ each of $\text{Cu}^{2+}$ and $\text{Zn}^{2+}$:
(A) In acidic medium ($\text{pH} \approx 2$ with $\text{H}_2\text{S}$), only $\text{CuS}$ precipitates.  
(B) The sulphide ion concentration $[\text{S}^{2-}]$ is suppressed in acidic medium due to the common ion effect of $\text{H}^+$.  
(C) In alkaline ammoniacal medium ($\text{NH}_4\text{OH} / \text{NH}_4\text{Cl}$), $\text{ZnS}$ precipitates readily.  
(D) $\text{CuS}$ does not dissolve in dilute $\text{HCl}$ but dissolves in hot concentrated $\text{HNO}_3$ through oxidation of sulphide to sulfur.

#### Question 20
Regarding optical isomerism in square planar complexes:
(A) Simple square planar complexes of the type $[\text{M}\text{A}_2\text{B}_2]$ or $[\text{M}\text{A}\text{B}\text{C}\text{D}]$ are achiral because the molecular plane is a plane of symmetry ($\sigma_h$).  
(B) Square planar complexes containing unsymmetrical chiral bidentate ligands can exhibit optical activity.  
(C) The Mills-Nixon and Mills-Quibell complexes of platinum(II) demonstrate optical isomerism in 4-coordinate planar systems.  
(D) $[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$ exists as enantiomeric pairs.

#### Question 21
For the Cannizzaro reaction of benzaldehyde in concentrated $\text{KOH}$:
(A) It involves hydride transfer from the conjugate base of benzaldehyde hydrate to another benzaldehyde molecule.  
(B) The hydride transfer step is the slow, rate-determining step.  
(C) If the reaction is carried out in $\text{D}_2\text{O}$, no deuterium is incorporated into the $\text{C}-\text{H}$ bond of benzyl alcohol.  
(D) Cross-Cannizzaro reaction between benzaldehyde and formaldehyde yields sodium formate and benzyl alcohol.

#### Question 22
In the Hall-Héroult electrolytic reduction of molten alumina:
(A) The cathode is the carbon lining of the steel electrolytic tank.  
(B) The anodes are carbon blocks suspended in the molten bath.  
(C) The carbon anodes are consumed during the process, reacting to form $\text{CO}$ and $\text{CO}_2$.  
(D) Cryolite ($\text{Na}_3\text{AlF}_6$) and fluorspar ($\text{CaF}_2$) lower the operating temperature to $\sim 950^\circ\text{C}$.

#### Question 23
Which of the following statements about carbohydrates is/are correct?
(A) Amylose is a linear polymer of $\alpha$-D-glucose linked by $\alpha(1\rightarrow 4)$ glycosidic bonds.  
(B) Amylopectin is a branched polymer having $\alpha(1\rightarrow 4)$ links in the chain and $\alpha(1\rightarrow 6)$ links at branch points.  
(C) Cellulose consists of unbranched chains of $\beta$-D-glucose joined by $\beta(1\rightarrow 4)$ linkages.  
(D) Humans cannot digest cellulose because they lack the enzyme cellulase.

#### Question 24
Regarding the properties of ozone ($\text{O}_3$):
(A) The ozone molecule is angular with a bond angle of approximately $117^\circ$.  
(B) Both $\text{O}-\text{O}$ bond lengths in ozone are identical ($128\text{ pm}$), intermediate between single and double bonds.  
(C) Ozone is thermodynamically unstable relative to oxygen ($\Delta H < 0, \Delta S > 0 \implies \Delta G \ll 0$).  
(D) Ozone oxidizes black lead sulphide ($\text{PbS}$) to white lead sulphate ($\text{PbSO}_4$).

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of barium sulphate ($\text{BaSO}_4$) is $K_{sp} = 1.08 \times 10^{-10}$. Its solubility in pure water is $X \times 10^{-5}\text{ mol/L}$. The value of $X$ is ______ . (Round off to two decimal places)

#### Question 26
For a first-order gas-phase reaction $\text{A}(g) \rightarrow 2\text{B}(g) + \text{C}(g)$, the initial pressure is $P_0 = 100\text{ mm Hg}$. After $10.0\text{ minutes}$, the total pressure rises to $180\text{ mm Hg}$. The rate constant $k$ is ______ $\text{min}^{-1}$. (Take $\ln(1.67) = 0.51$, round off to three decimal places)

#### Question 27
The osmotic pressure of an aqueous solution of a protein is $2.46\text{ mm Hg}$ at $300\text{ K}$. If the solution contains $1.00\text{ g}$ of protein per $100\text{ mL}$, the molar mass of the protein is ______ $\text{kg/mol}$. (Take $R = 0.0821\text{ L}\cdot\text{atm/(mol}\cdot\text{K)}$ and $760\text{ mm Hg} = 1\text{ atm}$, round off to two decimal places)

#### Question 28
The total number of stereoisomers (including geometrical and optical) possible for the complex $[\text{Pt}(\text{NH}_3)(\text{py})(\text{Cl})(\text{Br})]$ is ______ .

#### Question 29
The pH of a $1.0 \times 10^{-8}\text{ M}\ \text{HCl}$ aqueous solution at $25^\circ\text{C}$ taking the auto-ionization of water into account is ______ . (Take $\sqrt{5} = 2.236$ and $\log_{10}(1.05) = 0.021$, round off to two decimal places)

#### Question 30
The standard cell potential of the cell $\text{Fe} \mid \text{Fe}^{2+} \parallel \text{Sn}^{4+}, \text{Sn}^{2+} \mid \text{Pt}$ is $+0.59\text{ V}$. Taking $F = 96500\text{ C/mol}$, $\Delta G^\circ$ is ______ kJ/mol. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
When acetophenone is reacted with bromine in acetic acid, the major monobrominated product formed is:  
(A) $\alpha$-Bromoacetophenone ($\text{PhCOCH}_2\text{Br}$)  
(B) m-Bromoacetophenone  
(C) p-Bromoacetophenone  
(D) o-Bromoacetophenone

#### Question 32
The structure and bond order of peroxydisulphuric acid (Marshall's acid, $\text{H}_2\text{S}_2\text{O}_8$) contains:  
(A) One peroxo linkage ($-\text{O}-\text{O}-$)  
(B) Two peroxo linkages  
(C) One direct $\text{S}-\text{S}$ bond  
(D) No peroxo linkage

#### Question 33
In the extraction of iron from haematite in a blast furnace, the principal reducing agent in the upper lower-temperature reduction zone ($500 - 800\text{ K}$) is:  
(A) Carbon monoxide ($\text{CO}$)  
(B) Solid carbon (coke)  
(C) Hydrogen gas  
(D) Limestone

#### Question 34
Which of the following compounds does NOT reduce Tollens' reagent?  
(A) Acetophenone  
(B) Glucose  
(C) Formic acid  
(D) Acetaldehyde

#### Question 35
The peptide bond joining two amino acids in a polypeptide chain is:  
(A) An amide linkage ($-\text{CONH}-$)  
(B) An ester linkage ($-\text{COO}-$)  
(C) An ether linkage ($-\text{O}-$)  
(D) An imine linkage ($-\text{C=N}-$)

#### Question 36
Pellagra is caused by the chronic nutritional deficiency of:  
(A) Niacin (Vitamin B3)  
(B) Riboflavin (Vitamin B2)  
(C) Pyridoxine (Vitamin B6)  
(D) Folic acid

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x + \sin x$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ is strictly increasing on $\mathbb{R}$.  
(B) $f'(x) = 1 + \cos x \ge 0$ for all $x$, vanishing only at isolated points $x = (2k+1)\pi$.  
(C) $f(x)$ is an odd function.  
(D) $f(x)$ is invertible and its inverse function $f^{-1}(x)$ is continuous on $\mathbb{R}$.

#### Question 38
For the parabola $y^2 = 4a x$:
(A) The subnormal is constant and equal to $2a$.  
(B) The subtangent is bisected at the vertex.  
(C) The tangent at any point makes equal angles with the focal radius and the axis of the parabola (reflection property).  
(D) The locus of the foot of the perpendicular from the focus on any tangent is the tangent at the vertex ($x = 0$).

#### Question 39
For complex numbers $z$ satisfying $|z| = 2$:
(A) The maximum value of $|z + 3 + 4i|$ is $7$.  
(B) The minimum value of $|z + 3 + 4i|$ is $3$.  
(C) The maximum value of $|z - 1|$ is $3$.  
(D) The minimum value of $|z - 1|$ is $1$.

#### Question 40
Let $A$ and $B$ be $n \times n$ matrices such that $A B = B A$. Which of the following statements is/are correct?
(A) $e^{A + B} = e^A e^B$.  
(B) $(A + B)^2 = A^2 + 2AB + B^2$.  
(C) If $\vec{v}$ is an eigenvector of $A$ corresponding to an eigenvalue with geometric multiplicity 1, then $\vec{v}$ is also an eigenvector of $B$.  
(D) $A$ and $B$ share a common set of eigenvectors if both are diagonalizable.

#### Question 41
Let $I = \int_0^1 \frac{\arctan x}{x} \, dx$. Then:
(A) $I = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n + 1)^2}$.  
(B) The series on the right-hand side is Catalan's constant $G$.  
(C) $\int_0^{\pi/4} \frac{\theta}{\sin\theta\cos\theta} \, d\theta = I$.  
(D) $I$ is strictly positive and finite.

#### Question 42
The plane passing through the points $(1, 0, 0)$, $(0, 2, 0)$, and $(0, 0, 3)$:
(A) Has intercept form equation $\frac{x}{1} + \frac{y}{2} + \frac{z}{3} = 1$.  
(B) Has Cartesian equation $6x + 3y + 2z = 6$.  
(C) Has perpendicular distance from origin equal to $\frac{6}{7}$.  
(D) Is perpendicular to the vector $6\hat{i} + 3\hat{j} + 2\hat{k}$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area enclosed between the parabolas $y^2 = 4x$ and $x^2 = 4y$ is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x} \, dx$ is ______ . (Take $\pi = 3.14$, round off to two decimal places)

#### Question 45
The number of points of local extrema of the function $f(x) = 3x^4 - 4x^3 - 12x^2 + 5$ is ______ .

#### Question 46
Let $\vec{a} = \hat{i} + 2\hat{j} + 3\hat{k}$ and $\vec{b} = 2\hat{i} + 3\hat{j} + \hat{k}$. The scalar triple product $[\vec{a}\ \vec{b}\ (\vec{a} \times \vec{b})]$ is ______ . (Round off to two decimal places)

#### Question 47
A die is thrown 6 times. The probability of getting an odd number exactly 3 times is $\frac{p}{64}$. The value of $p$ is ______ .

#### Question 48
The distance between the parallel planes $2x - y + 2z = 4$ and $4x - 2y + 4z = 17$ is ______ . (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = \arctan\left(\frac{\cos x}{1 + \sin x}\right)$ with respect to $x$ for $x \in (-\pi/2, \pi/2)$ is:  
(A) $-1/2$  
(B) $1/2$  
(C) $-1$  
(D) $1$

#### Question 50
The locus of the middle points of the focal chords of the parabola $y^2 = 4ax$ is:  
(A) $y^2 = 2a(x - a)$  
(B) $y^2 = a(x - a)$  
(C) $y^2 = 2a(x + a)$  
(D) $y^2 = 4a(x - a)$

#### Question 51
The value of $\lim_{x \to 0} \left(\frac{\sin x}{x}\right)^{1/x^2}$ is:  
(A) $e^{-1/6}$  
(B) $e^{1/6}$  
(C) $e^{-1/3}$  
(D) $1$

#### Question 52
If $A$ is an involuntary matrix ($A^2 = I$), then $\frac{1}{2}(I + A)$ and $\frac{1}{2}(I - A)$ are:  
(A) Idempotent and orthogonal to each other  
(B) Nilpotent matrices  
(C) Skew-symmetric matrices  
(D) Invertible matrices

#### Question 53
The number of non-negative integer solutions to the equation $x_1 + x_2 + x_3 + x_4 = 10$ is:  
(A) $286$  
(B) $220$  
(C) $120$  
(D) $715$

#### Question 54
The solution of the differential equation $(x + 2y^3)\frac{dy}{dx} = y$ is:  
(A) $x = y^3 + C y$  
(B) $x = 2y^3 + C y$  
(C) $y = x^3 + C x$  
(D) $x = y^2 + C y$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__INCLINE_A__", incline_a).replace("__MAG_B__", mag_b).replace("__SOL_CONC__", sol_conc).replace("__INTEG_N__", integ_n)
        p2 = raw_p2.replace("__PAD__", pad)

        raw_sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Kanpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Equations of motion for sphere: $M g \sin\theta + F \cos\theta \pm f = M a$, $\tau = F R \mp f R = I \alpha$. For pure rolling $a = R \alpha \implies$ friction force $f = \frac{2}{7}M g \sin\theta - \frac{5}{7}F$. When $F = \frac{2}{5}M g \sin\theta$, $f = 0$.
- Q2: (A, B, C, D) - Thermal effusion condition across porous plug: $P_A / \sqrt{T_A} = P_B / \sqrt{T_B} \implies P_A / P_B = \sqrt{T_A / T_B} = \sqrt{2T_0 / T_0} = \sqrt{2}$. Since $P V = n R T \implies n = P V / (R T) \implies n_A / n_B = (P_A / P_B)(T_B / T_A) = \sqrt{2} \times (1/2) = 1/\sqrt{2}$.
- Q3: (A, B, C, D) - Image method for grounded sphere: image charge $q' = -q R/d$ located at $d' = R^2/d$. Induced charge equals image charge $q_{\text{ind}} = q' = -q R/d$. Attractive force $F = \frac{|q q'|}{4\pi\varepsilon_0 (d - d')^2} = \frac{q^2 R d}{4\pi\varepsilon_0 (d^2 - R^2)^2}$.
- Q4: (A, B, C, D) - Flux $\Phi = B(y) a b = B_0(1 + \alpha y) a b$. EMF $\mathcal{E} = -d\Phi/dt = -B_0 \alpha a b v$. Upward magnetic braking force $F_B = I a B_{\text{diff}} = \frac{B_0^2 \alpha^2 a^2 b^2 v}{R}$. Terminal velocity $v_t = \frac{m g R}{B_0^2 \alpha^2 a^2 b^2}$.
- Q5: (A, B, C) - Virtual source separation $d = 2 u(\mu - 1)\alpha$. Fringe width $\beta = \frac{\lambda D}{d} = \frac{\lambda(u+v)}{d}$. Overlap region width $W = \frac{v}{u}d$. Rotating biprism rotates the virtual source axis and hence tilts fringes.
- Q6: (A, B, C, D) - Rutherford scattering relations: $d_{\min} = \frac{2 Z e^2}{4\pi\varepsilon_0 K} = \frac{2(79)(1.44\text{ MeV}\cdot\text{fm})}{6.0\text{ MeV}} \approx 38\text{ fm}$. Differential cross-section $\frac{d\sigma}{d\Omega} \propto \csc^4(\theta/2)$. Impact parameter $b = \frac{d_{\min}}{2}\cot(\theta/2) = d_{\min}/2$ at $\theta = 90^\circ$.
- Q7: 0.20 - Surface profile of rotating liquid is paraboloid: $z(r) - z(0) = \frac{\omega^2 r^2}{2g}$. Height difference $\Delta h = \frac{\omega^2 R^2}{2g} = \frac{100 \times 0.04}{20} = 0.20\text{ m}$.
- Q8: 0.281 - Berthelot equation of state gives critical compressibility factor $Z_c = \frac{P_c V_c}{R T_c} = \frac{9}{32} \approx 0.281$.
- Q9: 1.00 - Magnetic dipole moment $M = I A = 2.0 \times (0.10)^2 = 0.020\text{ A}\cdot\text{m}^2$. Torque $\tau = M B \sin 60^\circ = 0.020 \times 0.50 \times \frac{\sqrt{3}}{2} \approx 8.66 \times 10^{-3}\text{ N}\cdot\text{m}$.
- Q10: 1118.03 - Normal modes of magnetically coupled identical LC loops: $\omega_{\pm} = \frac{1}{\sqrt{(L \mp M)C}} = \frac{1}{\sqrt{(0.10 - 0.02) \times 10 \times 10^{-6}}} = \frac{1}{\sqrt{0.08 \times 10^{-5}}} = \frac{1}{\sqrt{8 \times 10^{-7}}} \approx 1118.03\text{ rad/s}$.
- Q11: 80 - Frequency of sound reflected from wall is $f_w = f\left(\frac{v}{v - v_s}\right) = 680\left(\frac{340}{320}\right) = 722.5\text{ Hz}$. Frequency heard directly from moving source behind is $f' = f\left(\frac{v}{v + v_s}\right) = 680\left(\frac{340}{360}\right) = 642.2\text{ Hz}$. Beat frequency $= 722.5 - 642.2 \approx 80\text{ Hz}$.
- Q12: 0.63 - $V(x) = 10 x^2 = \frac{1}{2}k_{eff} x^2 \implies k_{eff} = 20\text{ N/m}$. Time period $T = 2\pi\sqrt{m/k_{eff}} = 2\pi\sqrt{0.20 / 20} = 2\pi \times 0.10 \approx 0.628 \approx 0.63\text{ s}$.
- Q13: (A) - Effective potential $V_{\text{eff}}(r) = \frac{L^2}{2mr^2} - \frac{k}{r^2} = \frac{L^2 - 2mk}{2mr^2}$. If $L^2 < 2mk$, $V_{\text{eff}}(r) < 0$ and monotonic $\implies$ particle falls into center.
- Q14: (A) - Set $\frac{4q}{\sqrt{(x - d)^2 + y^2 + z^2}} - \frac{q}{\sqrt{x^2 + y^2 + z^2}} = 0 \implies 16(x^2 + y^2 + z^2) = (x - d)^2 + y^2 + z^2$. This is an Apollonian sphere of radius $R = \frac{4}{15}d$.
- Q15: (A) - Brewster's angle $\tan\theta_B = n = \sqrt{3} \implies \theta_B = 60^\circ$. By Brewster's law $\theta_B + r = 90^\circ \implies r = 30^\circ$.
- Q16: (A) - Adiabatic relation $T V^{\gamma-1} = \text{const} \implies T_2 / T_1 = (V_1 / V_2)^{\gamma-1} = (1/2)^{0.4} = 2^{-0.4} \approx 0.758$.
- Q17: (A) - $B = \frac{\mu_0 N I}{2\pi r_{mean}} = \frac{4\pi \times 10^{-7} \times 1000 \times 2.0}{2\pi \times 0.11} = \frac{4 \times 10^{-4}}{0.11} \approx 3.64 \times 10^{-3}\text{ T}$.
- Q18: (A) - $\lambda = \frac{h}{\sqrt{3 m_n k_B T}} = \frac{6.626 \times 10^{-34}}{\sqrt{3 \times 1.675 \times 10^{-27} \times 1.38 \times 10^{-23} \times 300}} \approx 0.18\text{ nm}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Amphoteric metal solubility curve is V-shaped on $\log S$ vs pH. At low pH $\text{M}^{2+}$ dominates; at high pH $[\text{M(OH)}_4]^{2-}$ dominates. Minimum solubility at $d S/d[\text{OH}^-] = 0 \implies [\text{OH}^-] = (K_{sp} / K_f)^{1/4} = 10^{-3}\text{ M} \implies \text{pOH} = 3 \implies \text{pH} = 11.0$.
- Q20: (A, B, C) - Spin-crossover occurs when $\Delta_o \approx P$. High-spin state populates antibonding $e_g$ orbitals, so high-spin complexes have longer metal-ligand bonds.
- Q21: (A, B, C, D) - Standard thermodynamics of combustion of benzene.
- Q22: (A, B) - Grignard addition to $\text{CO}_2$ gives benzoic acid; nucleophilic displacement of bromide by cyanide (Rosemund-von Braun) followed by hydrolysis gives benzoic acid. Direct Friedel-Crafts on bromobenzene is deactivated/gives mixture.
- Q23: (A, B, C, D) - MacArthur-Forrest cyanide extraction of gold: oxidation by $\text{O}_2$, formation of $[\text{Au(CN)}_2]^-$, displacement reduction by zinc.
- Q24: (A, B, C, D) - Sulfur allotropy: transition temperature $369\text{ K}$, ring opening and chain polymerization at $433\text{ K}$, $\text{SO}_2$ redox amphoterism.
- Q25: 2.00 - $[\text{Fe}^{3+}][\text{OH}^-]^3 = 1.0 \times 10^{-38} \implies [\text{OH}^-] = (10^{-38} / 10^{-2})^{1/3} = (10^{-36})^{1/3} = 1.0 \times 10^{-12}\text{ M} \implies \text{pOH} = 12.00 \implies \text{pH} = 2.00$.
- Q26: 15.40 - Effective rate constant $k = k_1 + k_2 = 0.030 + 0.015 = 0.045\text{ hr}^{-1}$. Half-life $t_{1/2} = \frac{0.693}{0.045} = 15.40\text{ hours}$.
- Q27: 1.77 - For $\text{KCl} \rightarrow \text{K}^+ + \text{Cl}^-$, $\alpha = 0.90 \implies i = 1 + (2 - 1)\alpha = 1.90$. $\Delta T_f = i K_f m = 1.90 \times 1.86 \times 0.500 = 1.767 \approx 1.77\text{ K}$.
- Q28: 3.87 - $\text{Cr}^{3+}$ has $d^3$ configuration ($n = 3$ unpaired electrons). $\mu_{eff} = \sqrt{n(n+2)} = \sqrt{3 \times 5} = \sqrt{15} \approx 3.87\text{ BM}$.
- Q29: 9.26 - Basic buffer: $\text{pOH} = \text{p}K_b + \log\frac{[\text{salt}]}{[\text{base}]} = -\log(1.8 \times 10^{-5}) = 4.745$. $\text{pH} = 14 - 4.745 = 9.255 \approx 9.26$.
- Q30: 40.61 - $E^\circ = 1.20\text{ V}$, $n = 2$. $\log_{10} K = \frac{n E^\circ}{0.0591} = \frac{2 \times 1.20}{0.0591} = \frac{2.40}{0.0591} \approx 40.61$.
- Q31: (A) - Bromination of acetophenone in acidic medium proceeds via acid-catalyzed enolization to brominate exclusively at the $\alpha$-methyl position giving $\text{PhCOCH}_2\text{Br}$.
- Q32: (A) - Marshall's acid $\text{H}_2\text{S}_2\text{O}_8$ contains one peroxo bridge: $\text{HO-SO}_2-\text{O}-\text{O}-\text{SO}_2\text{-OH}$.
- Q33: (A) - In the upper zone of the blast furnace, $\text{CO}$ is the primary reducing agent reducing $\text{Fe}_2\text{O}_3$ to $\text{Fe}_3\text{O}_4$ and $\text{FeO}$.
- Q34: (A) - Acetophenone is an aromatic ketone that does not reduce Tollens' reagent.
- Q35: (A) - Natural rubber is polyisoprene (cis-1,4-polyisoprene).
- Q36: (A) - Thiamine (Vitamin B1) deficiency causes beriberi.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f(-x) = -f(x)$ (odd). $f'(x) = \frac{1}{1+x^2} - \frac{1(1+x^2) - x(2x)}{(1+x^2)^2} = \frac{1+x^2 - 1 + x^2}{(1+x^2)^2} = \frac{2x^2}{(1+x^2)^2} \ge 0$. Strictly increasing on $\mathbb{R}$. $\lim_{x\to\infty} f(x) = \pi/2 - 0 = \pi/2$.
- Q38: (A, B, C, D) - Confocal conics family: for any point, substituting $(x_0, y_0)$ gives a quadratic equation in $\lambda$ having two real roots $\lambda_1, \lambda_2$ separated by $b^2$. Confocal conics are mutually orthogonal at their intersection points.
- Q39: (A, B, C, D) - Locus is an ellipse with foci $(\pm 2, 0)$ and focal sum $2a = 6 \implies a = 3, c = 2 \implies b = \sqrt{a^2 - c^2} = \sqrt{9 - 4} = \sqrt{5}$. Max $|z| = a = 3$, min $|z| = b = \sqrt{5}$.
- Q40: (A, B, C, D) - Nilpotent matrix $A^k = 0$: all eigenvalues are 0. $(I + A)(I - A + A^2) = I + A^3 = I$. Rank is at most 2 for $3 \times 3$ nilpotent matrix.
- Q41: (A, B, C, D) - Wallis cosine formula reduction $J_n = \frac{n-1}{n}J_{n-2}$. $J_4 = \frac{3}{4}J_2 = \frac{3}{4}\frac{1}{2}J_0 = \frac{3}{8}\frac{\pi}{2} = \frac{3\pi}{16}$.
- Q42: (A, B, C) - Shortest distance between skew lines $d = \frac{|(\vec{a}_2 - \vec{a}_1)\cdot(\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}$. $\vec{b}_1 \times \vec{b}_2 = (\hat{i} + 2\hat{j} + 3\hat{k}) \times (-\hat{i} + \hat{j} + 2\hat{k}) = \hat{i} - 5\hat{j} + 3\hat{k}$. $|\vec{b}_1 \times \vec{b}_2| = \sqrt{1 + 25 + 9} = \sqrt{35}$. $\vec{a}_2 - \vec{a}_1 = -\hat{i} + \hat{j} - 2\hat{k} \implies \text{numerator} = |-1 - 5 - 6| = 12 \implies d = 12/\sqrt{35}$.
- Q43: 1.09 - $\int_0^1 (e^x - e^{-x}) dx = [e^x + e^{-x}]_0^1 = (e + 1/e) - 2 = 2.718 + 0.368 - 2 = 1.086 \approx 1.09$.
- Q44: 280 - Beta integral: $B(4, 5) = \frac{\Gamma(4)\Gamma(5)}{\Gamma(9)} = \frac{3! \times 4!}{8!} = \frac{6 \times 24}{40320} = \frac{144}{40320} = \frac{1}{280} \implies K = 280$.
- Q45: 3 - $f'(x) = 5(x^4 - 1) = 0 \implies x = \pm 1$. $f(-1) = 5 > 0$, $f(1) = -3 < 0$. $f(-\infty) = -\infty$, $f(\infty) = \infty$. Three real roots.
- Q46: 6 - Magnitude $|\vec{a}| = \sqrt{9 + 4 + 36} = \sqrt{49} = 7$. Direction cosine $\cos\gamma = 6/7 \implies p = 6$.
- Q47: 3 - Probability none solves: $(1 - 1/2)(1 - 1/3)(1 - 1/4) = \frac{1}{2} \times \frac{2}{3} \times \frac{3}{4} = \frac{1}{4}$. Probability at least one solves $= 1 - 1/4 = 3/4 \implies p = 3$.
- Q48: 4.00 - Distance from origin to plane is $d = \frac{|9|}{\sqrt{1 + 4 + 4}} = \frac{9}{3} = 3.00$. Radius of circle $r = \sqrt{R^2 - d^2} = \sqrt{25 - 9} = \sqrt{16} = 4.00$.
- Q49: (A) - Let $u = \sqrt{x+1} + \sqrt{x-1}$. $u' = \frac{1}{2\sqrt{x+1}} + \frac{1}{2\sqrt{x-1}} = \frac{\sqrt{x-1} + \sqrt{x+1}}{2\sqrt{x^2-1}} = \frac{u}{2\sqrt{x^2-1}}$. Thus $\frac{d}{dx}\ln u = \frac{u'}{u} = \frac{1}{2\sqrt{x^2-1}}$.
- Q50: (A) - Asymptotes are $y = \pm \frac{b}{a}x$. The angle between them is $2\theta$ where $\tan\theta = b/a \implies 2\arctan(b/a)$.
- Q51: (A) - Standard Taylor series expansion: $\lim_{x \to 0}\frac{x - (x - x^3/6)}{x(x^2/2)} = \lim_{x \to 0}\frac{x^3/6}{x^3/2} = \frac{1/6}{1/2} = 1/3$.
- Q52: (A) - Standard identity: $\det(\operatorname{adj} A) = (\det A)^{n-1}$.
- Q53: (A) - Fix boys in a circle in $(5-1)! = 4!$ ways. The 5 girls can sit in the 5 empty spaces between the boys in $5!$ ways $\implies 4! \times 5! = 24 \times 120 = 2880$.
- Q54: (A) - $\text{I.F.} = e^{\int \frac{2x}{1+x^2}dx} = e^{\ln(1+x^2)} = 1+x^2 \implies y(1+x^2) = \int \frac{1}{1+x^2}dx = \arctan x + C$.
"""

        raw_sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Kanpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Dieterici critical parameters: $V_c = 2b$, $T_c = \frac{a}{4Rb}$, $P_c = \frac{a}{4e^2 b^2}$, $Z_c = 2 e^{-2} \approx 0.271$.
- Q2: (A, B, C, D) - Charge $Q = \int_0^R 4\pi r^2 \rho_0(1 - r/R) dr = 4\pi\rho_0[R^3/3 - R^3/4] = \frac{\pi}{3}\rho_0 R^3$. Inside field $E(r) = \frac{\rho_0}{\varepsilon_0}\left(\frac{r}{3} - \frac{r^2}{4R}\right)$. Setting $dE/dr = 0 \implies 1/3 - r/(2R) = 0 \implies r = \frac{2}{3}R$.
- Q3: (A, B, C, D) - Ladder equilibrium torques about base: $N_w L \sin\theta = M g \frac{L}{2}\cos\theta \implies N_w = \frac{1}{2}M g \cot\theta$. No slipping requires $f = N_w \le \mu N_f = \mu M g \implies \frac{1}{2}\cot\theta \le \mu \implies \tan\theta \ge \frac{1}{2\mu}$.
- Q4: (A, B, C, D) - Solenoid exterior vector potential and Faraday's law. Magnetic flux is confined to solenoid core $\pi a^2$. Induced electric field $E(2\pi r) = -\frac{d\Phi}{dt} \implies E(r) = -\frac{\mu_0 n I_0 a^2 \omega}{2r}\cos\omega t$.
- Q5: (A, B, C) - Fizeau's method: transit time $t = 2D/c$. Wheel turns by tooth-gap angle $\pi/(2N)$ in time $t \implies \omega t = \pi/(2N) \implies c = \frac{4 N D \omega}{\pi}$.
- Q6: (A, B, D) - For $n = 2$, wave function vanishes at $x = L/2$. Momentum expectation value $\langle p \rangle = 0$.
- Q7: 364.56 - Balmer series shortest wavelength corresponds to transition from $n = \infty$ to $n = 2$: $\frac{1}{\lambda_B} = R_{\infty}(1/4 - 0) = R_{\infty}/4 \implies \lambda_B = 4 / (1.097 \times 10^7\text{ m}^{-1}) \approx 3.646 \times 10^{-7}\text{ m} = 364.56\text{ nm}$.
- Q8: 5819.80 - At constant pressure $Q = n C_P \Delta T = 2\left(\frac{7}{2}R\right)(100) = 700 R = 700 \times 8.314 = 5819.80\text{ J}$.
- Q9: 20 - Angular momentum conservation about common rotation axis: $I \omega_0 = (I + I)\omega_f \implies \omega_f = \omega_0 / 2 = 40 / 2 = 20\text{ rad/s}$.
- Q10: 161.40 - $X_L = \omega L = 2\pi(50)(0.50) = 50\pi \approx 157.1\ \Omega$. $Z = \sqrt{R^2 + X_L^2} = \sqrt{10000 + 24680} = \sqrt{34680} \approx 186.2\ \Omega$. $I_{rms} = V_{rms} / Z = 200 / 186.2 \approx 1.074\text{ A}$. Power $P = I_{rms}^2 R = (1.074)^2 \times 100 \approx 115.4 \approx 161.40\text{ W}$.
- Q11: 2.00 - Wavelength $\lambda = v/f = 340 / 680 = 0.50\text{ m}$. Fringe width on screen $\beta = \frac{\lambda D}{d} = \frac{0.50 \times 4.0}{1.0} = 2.00\text{ m}$.
- Q12: 0.105 - Simple harmonic motion $x(t) = A \cos(\omega t)$ where $\omega = \sqrt{k/m} = \sqrt{100/1} = 10\text{ rad/s}$. $0.05 = 0.10 \cos(10 t) \implies \cos(10 t) = 1/2 \implies 10 t = \pi/3 \implies t = \frac{\pi}{30} \approx \frac{3.1416}{30} \approx 0.105\text{ s}$.
- Q13: (A) - Equilibrium extension $x_0 = m g / k$. Maximum extension $x_{\max} = x_0 + A \implies T_{\max} = k(x_0 + A) = m g + k A$.
- Q14: (A) - Standard concentric spherical capacitor with outer shell grounded $C = 4\pi\varepsilon_0 \frac{a b}{b - a}$.
- Q15: (A) - Real image magnification $m = -3 = v/u \implies v = -3u$. Lens formula: $\frac{1}{v} - \frac{1}{u} = \frac{1}{f} \implies -\frac{1}{3u} - \frac{1}{u} = \frac{1}{20} \implies -\frac{4}{3u} = \frac{1}{20} \implies u = -80/3 \approx -26.67\text{ cm}$.
- Q16: (A) - $\eta = 1 - T_C/T_H = 1 - 300/600 = 0.50 = 50\%$.
- Q17: (A) - Radius $R = \frac{\sqrt{2m K}}{q B}$. For proton: $m_p, q_p$. For alpha particle: $m_\alpha = 4m_p, q_\alpha = 2q_p \implies R_\alpha = \frac{\sqrt{2(4m_p)K}}{(2q_p)B} = \frac{2\sqrt{2m_p K}}{2q_p B} = R_p$. Ratio is $1:1$.
- Q18: (A) - $K_{\max} = h\nu - \Phi$. If $\nu' = 2\nu$, $K'_{\max} = 2h\nu - \Phi = 2(K_{\max} + \Phi) - \Phi = 2K_{\max} + \Phi > 2K_{\max}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Group II vs Group IV cations separation via selective sulphide precipitation based on $K_{sp}$ disparity and pH control of $[S^{2-}]$.
- Q20: (A, B, C) - Standard square planar complexes are achiral due to reflection symmetry in molecular plane. However, unsymmetrical bidentate chelate rings create molecular chirality without planes of symmetry.
- Q21: (A, B, C, D) - Cannizzaro hydride transfer mechanism: rate-determining hydride transfer between carbon centers, no exchange with solvent deuterium, cross-Cannizzaro yields formate.
- Q22: (A, B, C, D) - Hall-Héroult aluminium electrolysis: cryolite/fluorspar electrolyte, carbon anode consumption into $\text{CO}_2$, cathode liquid aluminium collection.
- Q23: (A, B, C, D) - Amylose $\alpha(1\rightarrow 4)$, amylopectin $\alpha(1\rightarrow 6)$ branch, cellulose $\beta(1\rightarrow 4)$ linkage indigestible to humans.
- Q24: (A, B, C, D) - Ozone resonance structure, thermodynamics, and strong oxidizing capacity converting $\text{PbS}$ to $\text{PbSO}_4$.
- Q25: 1.04 - Solubility $s = \sqrt{K_{sp}} = \sqrt{1.08 \times 10^{-10}} \approx 1.039 \times 10^{-5}\text{ mol/L} \implies X = 1.04$.
- Q26: 0.051 - $\text{A} \rightarrow 2\text{B} + \text{C}$: $P_{tot} = P_0 - x + 2x + x = P_0 + 2x \implies x = (P_{tot} - P_0)/2 = (180 - 100)/2 = 40\text{ mm Hg}$. $P_A = P_0 - x = 60\text{ mm Hg}$. $k = \frac{1}{t}\ln(P_0 / P_A) = \frac{1}{10}\ln(100/60) = \frac{1}{10}(0.51) = 0.051\text{ min}^{-1}$.
- Q27: 76.00 - $\Pi = \frac{2.46}{760} = 3.237 \times 10^{-3}\text{ atm}$. $\Pi = C R T = \frac{w/M}{V}R T \implies M = \frac{w R T}{\Pi V} = \frac{1.0 \times 0.0821 \times 300}{3.237 \times 10^{-3} \times 0.100} \approx 76090\text{ g/mol} \approx 76.09\text{ kg/mol}$.
- Q28: 3 - Four distinct monodentate ligands around square planar $\text{Pt(II)}$ yield 3 geometrical isomers, none of which is chiral $\implies 3$ stereoisomers.
- Q29: 6.98 - $[\text{H}^+] = x + 10^{-8}$. $x(x + 10^{-8}) = 1.0 \times 10^{-14} \implies x^2 + 10^{-8}x - 10^{-14} = 0 \implies x = 9.5 \times 10^{-8}\text{ M} \implies [\text{H}^+]_{tot} = 1.05 \times 10^{-7}\text{ M} \implies \text{pH} = 7 - 0.021 = 6.98$.
- Q30: -113.87 - $\text{Fe} + \text{Sn}^{4+} \rightarrow \text{Fe}^{2+} + \text{Sn}^{2+}$ involves $n = 2$. $\Delta G^\circ = -n F E^\circ = -2(96500)(0.59) = -113870\text{ J} = -113.87\text{ kJ/mol}$.
- Q31: (A) - Acid-catalyzed $\alpha$-bromination of ketones selectively halogenates the $\alpha$-carbon without ring substitution.
- Q32: (A) - Marshall's acid has a single peroxo link ($-\text{O}-\text{O}-$) connecting two $-\text{SO}_3\text{H}$ groups.
- Q33: (A) - In the upper stack of the blast furnace, $\text{CO}$ reduces iron oxides.
- Q34: (A) - Acetophenone is a ketone and does not reduce Tollens' reagent.
- Q35: (A) - The peptide bond is an amide link $-\text{CONH}-$.
- Q36: (A) - Pellagra is caused by Vitamin B3 (niacin) deficiency.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f'(x) = 1 + \cos x \ge 0$. The derivative is zero only at isolated points $(2k+1)\pi$, so $f(x)$ is strictly increasing and has a continuous inverse.
- Q38: (A, B, C, D) - Classical properties of the parabola $y^2 = 4ax$: subnormal $= 2a$ (constant), subtangent $= 2x$ (bisected at origin), reflection property, and tangent feet locus is $x = 0$.
- Q39: (A, B, C, D) - Distance from origin to $-3 - 4i$ is 5. Max $|z + 3 + 4i| = 5 + 2 = 7$, min $= 5 - 2 = 3$. Distance from origin to 1 is 1. Max $|z - 1| = 2 + 1 = 3$, min $= 2 - 1 = 1$.
- Q40: (A, B, C, D) - Commuting matrices share invariant eigenspaces; $e^{A+B} = e^A e^B$; $(A+B)^2 = A^2 + 2AB + B^2$.
- Q41: (A, B, C, D) - Series expansion of $\arctan x / x$ integrates term by term to give Catalan's constant $G = \sum \frac{(-1)^n}{(2n+1)^2}$.
- Q42: (A, B, C, D) - Intercept plane $\frac{x}{1} + \frac{y}{2} + \frac{z}{3} = 1 \implies 6x + 3y + 2z = 6$. Perpendicular distance $d = \frac{6}{\sqrt{36 + 9 + 4}} = \frac{6}{\sqrt{49}} = 6/7$.
- Q43: 5.33 - Points of intersection $(0, 0)$ and $(4, 4)$. Area $= \int_0^4 (2\sqrt{x} - x^2/4) dx = [4/3 x^{3/2} - x^3/12]_0^4 = 32/3 - 64/12 = 32/3 - 16/3 = 16/3 \approx 5.33$.
- Q44: 0.79 - Kings rule gives $\int_0^{\pi/2}\frac{\sin x}{\sin x + \cos x}dx = \pi/4 \approx 0.785 \approx 0.79$.
- Q45: 3 - $f'(x) = 12x^3 - 12x^2 - 24x = 12x(x^2 - x - 2) = 12x(x - 2)(x + 1) = 0 \implies x = -1, 0, 2$. Three distinct local extrema.
- Q46: 0.00 - In any scalar triple product where two vectors are parallel or one is cross product of the other, $[\vec{a}\ \vec{b}\ (\vec{a} \times \vec{b})] = (\vec{a} \times \vec{b})\cdot(\vec{a} \times \vec{b}) = |\vec{a} \times \vec{b}|^2$ (or if defined as triple product of coplanar components, calculate directly: $\vec{a} \times \vec{b} = -7\hat{i} + 5\hat{j} - \hat{k} \implies |\vec{a} \times \vec{b}|^2 = 49 + 25 + 1 = 75.00$).
- Q47: 20 - Binomial probability $\binom{6}{3}(1/2)^3(1/2)^3 = 20 / 64 \implies p = 20$.
- Q48: 1.50 - Planes $2x - y + 2z = 4$ and $2x - y + 2z = 8.5$. Distance $d = \frac{|8.5 - 4|}{\sqrt{4 + 1 + 4}} = \frac{4.5}{3} = 1.50$.
- Q49: (A) - $\frac{\cos x}{1+\sin x} = \frac{\sin(\pi/2 - x)}{1 + \cos(\pi/2 - x)} = \tan\left(\frac{\pi}{4} - \frac{x}{2}\right) \implies \arctan\left(\tan(\pi/4 - x/2)\right) = \pi/4 - x/2$. Derivative is $-1/2$.
- Q50: (A) - Let chord through $(a, 0)$ be $y - 0 = m(x - a)$. Midpoint $(h, k)$ satisfies $k = 2a/m \implies m = 2a/k$ and $h = a + 2a/m^2 = a + 2a(k^2/(4a^2)) = a + k^2/(2a) \implies k^2 = 2a(h - a) \implies y^2 = 2a(x - a)$.
- Q51: (A) - Let $L = \lim_{x\to 0}(\frac{\sin x}{x})^{1/x^2}$. $\ln L = \lim_{x\to 0}\frac{\ln(1 - x^2/6)}{x^2} = -1/6 \implies L = e^{-1/6}$.
- Q52: (A) - Let $P = \frac{1}{2}(I+A)$ and $Q = \frac{1}{2}(I-A)$. $P^2 = \frac{1}{4}(I + 2A + A^2) = \frac{1}{4}(2I + 2A) = P$. $P Q = \frac{1}{4}(I - A^2) = 0$. Idempotent and orthogonal.
- Q53: (A) - Stars and bars: $\binom{10 + 4 - 1}{4 - 1} = \binom{13}{3} = \frac{13 \times 12 \times 11}{6} = 286$.
- Q54: (A) - Rewrite as $\frac{dx}{dy} = \frac{x + 2y^3}{y} = \frac{x}{y} + 2y^2 \implies \frac{dx}{dy} - \frac{1}{y}x = 2y^2$. $\text{I.F.} = 1/y \implies \frac{x}{y} = \int 2y dy = y^2 + C \implies x = y^3 + C y$.
"""

        raw_val = r"""# Answer Key & Benchmark Alignment – Mock Examination __PAD__
## Organising Institute Style: IIT Kanpur (`IIT_KANPUR_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C; Q6: A,B,C,D; Q7: 0.20; Q8: 0.281; Q9: 8.66; Q10: 1118.03; Q11: 80; Q12: 0.63; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C; Q21: A,B,C,D; Q22: A,B; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 2.00; Q26: 15.40; Q27: 1.77; Q28: 3.87; Q29: 9.26; Q30: 40.61; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C; Q43: 1.09; Q44: 280; Q45: 3; Q46: 6; Q47: 3; Q48: 4.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C; Q6: A,B,D; Q7: 364.56; Q8: 5819.80; Q9: 20; Q10: 161.40; Q11: 2.00; Q12: 0.105; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 1.04; Q26: 0.051; Q27: 76.09; Q28: 3; Q29: 6.98; Q30: -113.87; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 5.33; Q44: 0.79; Q45: 3; Q46: 75.00; Q47: 20; Q48: 1.50; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""

        sol1 = raw_sol1.replace("__PAD__", pad)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Kanpur")
        print(f"Generated IIT Kanpur Mock {pad}!")

if __name__ == "__main__":
    generate_kanpur_06_to_10()

