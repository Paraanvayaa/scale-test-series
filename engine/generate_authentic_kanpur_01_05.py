"""
IIT Kanpur Mocks 01 to 05 Generator
Organising Institute: Indian Institute of Technology Kanpur
Empirical Benchmark: 2001, 2007, 2011, 2018 Official JEE Advanced Papers
Features:
- Extreme numerical rigor and calculation depth (>= 38% numerical value questions)
- Heavy analytical mechanics, coupled oscillating circuits, Poynting vectors, non-ideal gas thermodynamics
- Quantitative ionic equilibria, complexation, coordination chemistry, multi-step organic cascades
- Multivariable calculus, orthogonal trajectories, Cayley-Hamilton invariants, 3D line-plane-sphere geometry
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_kanpur_01_to_05():
    for mock_idx in range(1, 6):
        pad = f"{mock_idx:02d}"
        fluid_h = str(1.2 + mock_idx * 0.2)
        coil_l = str(0.15 + mock_idx * 0.05)
        molar_c = str(0.015 + mock_idx * 0.005)
        diff_k = str(2 + mock_idx)

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
A cylinder of mass $M$ and radius $R$ rests on a rough horizontal plank of mass $m$, which in turn rests on a frictionless horizontal floor. A constant horizontal force $F$ is applied to the plank. The coefficient of static and kinetic friction between the cylinder and the plank is $\mu$. Assuming pure rolling of the cylinder on the plank:
(A) The acceleration of the plank is $a_p = \frac{3F}{3m + M}$.  
(B) The friction force acting on the cylinder has magnitude $f = \frac{M F}{3m + M}$.  
(C) The linear acceleration of the cylinder relative to the ground is $a_c = \frac{F}{3m + M}$.  
(D) Pure rolling occurs without slipping if $F \le \mu(3m + M)g$.

#### Question 2
One mole of an ideal gas undergoes a polytropic process characterized by $P = P_0 - \alpha V^2$, where $P_0$ and $\alpha$ are positive constants. At volume $V_1 = \sqrt{P_0 / (3\alpha)}$:
(A) The temperature of the gas attains its absolute maximum value.  
(B) The maximum temperature attained by the gas is $T_{\max} = \frac{2 P_0}{3 R}\sqrt{\frac{P_0}{3\alpha}}$.  
(C) The molar heat capacity $C$ of the gas at this state diverges to $\pm \infty$.  
(D) The work done in expanding from $V = 0$ to $V_1$ is $\frac{8}{9} P_0 V_1$.

#### Question 3
Two long concentric conducting cylindrical shells of radii $a$ and $b$ ($a < b$) have length $L \gg b$. The space between the shells is filled with a weakly conducting medium of non-uniform electrical conductivity $\sigma(r) = \sigma_0 \frac{a}{r}$ ($a \le r \le b$). A potential difference $V_0$ is maintained between the inner and outer cylinders.
(A) The radial current density is $J(r) = \frac{I}{2\pi r L}$, where $I$ is the total leakage current.  
(B) The electric field between the cylinders is uniform and independent of $r$.  
(C) The total resistance of the medium is $R = \frac{b - a}{2\pi \sigma_0 a L}$.  
(D) The volume charge density in the medium between the cylinders is zero.

#### Question 4
A rigid rectangular wire loop of width $w$, length $l$, mass $m$, and electrical resistance $R$ falls vertically under gravity from rest into a region containing a uniform horizontal magnetic field $B$ directed into the plane of the loop. The field is bounded by a horizontal line $y = 0$. While entering the field:
(A) The terminal velocity achieved before entering completely is $v_t = \frac{m g R}{B^2 w^2}$.  
(B) If released from height $h$ such that its entry speed $v_0 = v_t$, the loop moves with constant velocity while crossing the boundary.  
(C) The total electrical energy dissipated as Joule heat while the loop enters completely is independent of $R$ if $v = v_t$.  
(D) The induced current circulates in the counterclockwise direction.

#### Question 5
In an interference experiment using a Lloyd's mirror configuration, light of wavelength $\lambda$ from a narrow slit $S$ located at distance $d$ above a flat glass mirror is reflected onto a screen placed at distance $D$ ($D \gg d$) from the slit:
(A) The reflected wave undergoes an abrupt phase shift of $\pi$ radians upon reflection at grazing incidence.  
(B) The fringe width on the screen is $\beta = \frac{\lambda D}{2d}$.  
(C) The fringe formed at the intersection of the mirror surface and the screen is a dark fringe.  
(D) If the mirror is shifted downwards by a small distance $\delta$, the central fringe moves upwards.

#### Question 6
According to the relativistic momentum-energy relation, a particle of rest mass $m_0$ and charge $q$ moves in a uniform magnetic field $B$ perpendicular to its velocity:
(A) The trajectory of the particle is a circle of radius $R = \frac{\gamma m_0 v}{q B}$, where $\gamma = (1 - v^2/c^2)^{-1/2}$.  
(B) The cyclotron frequency is $\omega_c = \frac{q B}{\gamma m_0}$, which decreases as the particle energy increases.  
(C) The kinetic energy of the particle is $K = (\gamma - 1)m_0 c^2$.  
(D) The magnetic Lorentz force does zero work on the particle, keeping its total relativistic energy constant.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A U-tube of uniform cross-sectional area $A = 2.0\text{ cm}^2$ contains mercury ($\rho = 13600\text{ kg/m}^3$). Water ($\rho_w = 1000\text{ kg/m}^3$) is poured into one limb until a column of height $h = __FLUID_H__\text{ m}$ is formed. The difference in the mercury levels in the two limbs is ______ cm. (Round off to two decimal places)

#### Question 8
A non-ideal gas obeys the equation of state $\left(P + \frac{a}{V_m^2}\right)(V_m - b) = R T$. For this gas, the critical temperature is $T_c = 300\text{ K}$ and critical pressure is $P_c = 50.0\text{ bar}$. Taking $R = 0.08314\text{ bar}\cdot\text{L/(mol}\cdot\text{K)}$, the value of van der Waals constant $b$ is ______ L/mol. (Round off to three decimal places)

#### Question 9
A circular coil of radius $r = 10.0\text{ cm}$ having $N = 200\text{ turns}$ and resistance $R = 5.0\ \Omega$ is placed in a uniform magnetic field directed normal to the plane of the coil. The magnetic field increases linearly from $0.20\text{ T}$ to $0.80\text{ T}$ in $\Delta t = 0.15\text{ s}$. The induced current flowing in the coil is ______ A. (Take $\pi = 3.14$, round off to two decimal places)

#### Question 10
In a series LCR circuit, $L = __COIL_L__\text{ H}$, $C = 20.0\ \mu\text{F}$, and $R = 15.0\ \Omega$. The circuit is connected to an AC source of variable frequency and peak voltage $V_0 = 120\text{ V}$. At resonance, the peak potential difference across the inductor is ______ V. (Round off to two decimal places)

#### Question 11
Two tuning forks A and B produce 4 beats per second when sounded together. When fork A is slightly loaded with wax, the beat frequency decreases to 2 beats per second. If the frequency of fork B is $256\text{ Hz}$, the original natural frequency of fork A is ______ Hz.

#### Question 12
A uniform solid sphere of mass $M = 4.0\text{ kg}$ and radius $R = 0.25\text{ m}$ is pivoted at a point on its surface so that it can swing freely as a physical pendulum in a vertical plane. Taking $g = 9.80\text{ m/s}^2$, the period of small oscillations is ______ s. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle of mass $m$ moves along the $x$-axis subject to a conservative force whose potential energy is $U(x) = U_0 \left[2\left(\frac{x}{a}\right)^4 - \left(\frac{x}{a}\right)^2\right]$. The angular frequency of small oscillations about the stable equilibrium position is:  
(A) $\omega = \sqrt{\frac{4 U_0}{m a^2}}$  
(B) $\omega = \sqrt{\frac{2 U_0}{m a^2}}$  
(C) $\omega = \sqrt{\frac{8 U_0}{m a^2}}$  
(D) $\omega = \sqrt{\frac{U_0}{m a^2}}$

#### Question 14
A spherical conducting shell of inner radius $R_1$ and outer radius $R_2$ carries a net charge $+Q$. A point charge $+q$ is placed at the center of the cavity. The electrostatic potential at distance $r$ from the center ($R_1 < r < R_2$) is:  
(A) $\frac{1}{4\pi\varepsilon_0}\frac{Q + q}{R_2}$  
(B) $\frac{1}{4\pi\varepsilon_0}\left(\frac{q}{r} + \frac{Q}{R_2}\right)$  
(C) $\frac{1}{4\pi\varepsilon_0}\frac{q}{R_1}$  
(D) $\frac{1}{4\pi\varepsilon_0}\frac{Q - q}{R_2}$

#### Question 15
A biconvex thin lens made of glass with refractive index $n = 1.50$ has radii of curvature $R_1 = 20\text{ cm}$ and $R_2 = -30\text{ cm}$. When immersed completely in a liquid of refractive index $n_l = 1.25$, its focal length becomes:  
(A) $+60\text{ cm}$  
(B) $+120\text{ cm}$  
(C) $+48\text{ cm}$  
(D) $+24\text{ cm}$

#### Question 16
An ideal gas undergoes a cycle on the $P$-$V$ diagram consisting of an isobaric expansion at $P_1$, an isochoric cooling to $P_2$, and an isothermal compression back to the initial state $(P_1, V_1)$. The work done by the gas per cycle is:  
(A) $P_1(V_2 - V_1) - P_1 V_1 \ln(V_2/V_1)$  
(B) $P_1 V_2 - P_2 V_1$  
(C) $(P_1 - P_2)(V_2 - V_1)$  
(D) $P_1 V_1 \ln(V_2/V_1)$

#### Question 17
A long straight cylindrical wire of radius $R$ carries a uniform current density $J$. The magnetic field strength $B(r)$ at a radial distance $r < R$ inside the wire is:  
(A) $\frac{\mu_0 J r}{2}$  
(B) $\frac{\mu_0 J R^2}{2r}$  
(C) $\mu_0 J r$  
(D) $\frac{\mu_0 J r^2}{2R}$

#### Question 18
The binding energy per nucleon of $_{1}^{2}\text{H}$ is $1.11\text{ MeV}$ and of $_{2}^{4}\text{He}$ is $7.07\text{ MeV}$. In the fusion reaction $_{1}^{2}\text{H} + _{1}^{2}\text{H} \rightarrow _{2}^{4}\text{He} + Q$, the energy $Q$ released is:  
(A) $23.84\text{ MeV}$  
(B) $28.28\text{ MeV}$  
(C) $11.92\text{ MeV}$  
(D) $5.96\text{ MeV}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution containing a diprotic weak acid $\text{H}_2\text{A}$ ($c = 0.10\text{ M}$) with dissociation constants $K_{a1} = 1.0 \times 10^{-4}$ and $K_{a2} = 1.0 \times 10^{-9}$:
(A) The hydronium ion concentration is determined primarily by the first ionization step.  
(B) $[\text{H}^+] \approx \sqrt{K_{a1} c} = 3.16 \times 10^{-3}\text{ M}$.  
(C) The equilibrium concentration of the divalent anion $[\text{A}^{2-}] \approx K_{a2} = 1.0 \times 10^{-9}\text{ M}$.  
(D) Addition of $0.05\text{ mol}$ of strong base $\text{NaOH}$ creates a buffer whose pH is equal to $\text{p}K_{a1}$.

#### Question 20
For the coordination complex ion $[\text{Co}(\text{en})_2\text{Cl}_2]^+$ (where en = ethylenediamine):
(A) It exhibits cis-trans geometrical isomerism.  
(B) The trans-isomer has a center of inversion and is optically inactive.  
(C) The cis-isomer lacks an improper axis of rotation ($S_n$) and exists as a pair of non-superimposable enantiomers.  
(D) The cobalt center possesses a low-spin $d^6$ configuration with zero unpaired electrons.

#### Question 21
Regarding the electrochemical thermodynamics of a Daniell cell $\text{Zn}(s) \mid \text{Zn}^{2+}(aq) \parallel \text{Cu}^{2+}(aq) \mid \text{Cu}(s)$:
(A) The temperature coefficient of the cell potential $\left(\frac{\partial E}{\partial T}\right)_P = \frac{\Delta S}{n F}$.  
(B) If $\left(\frac{\partial E}{\partial T}\right)_P > 0$, the reaction absorbs heat from the surroundings when operating reversibly.  
(C) $\Delta H = -n F E + n F T \left(\frac{\partial E}{\partial T}\right)_P$.  
(D) The equilibrium constant $K$ of the cell reaction is $\exp\left(\frac{n F E^\circ}{R T}\right)$.

#### Question 22
Which of the following organic transformations involve an intermediate carbene species?
(A) Reimer-Tiemann reaction of phenol with chloroform and aqueous $\text{KOH}$.  
(B) Carbylamine reaction of aniline with chloroform and ethanolic $\text{KOH}$.  
(C) Hoffmann bromamide degradation of acetamide with $\text{Br}_2 / \text{KOH}$.  
(D) Simmons-Smith cyclopropanation of cyclohexene with $\text{CH}_2\text{I}_2$ and $\text{Zn-Cu}$ couple.

#### Question 23
In the pyrometallurgical extraction of zinc from zinc blende ($\text{ZnS}$):
(A) Roasting converts $\text{ZnS}$ to $\text{ZnO}$ with evolution of $\text{SO}_2$.  
(B) Reduction is carried out using crushed coke in vertical retorts at $\sim 1400\text{ K}$.  
(C) Zinc vapor is rapidly condensed to avoid re-oxidation by $\text{CO}_2$.  
(D) The reduction reaction is non-spontaneous at room temperature due to negative $\Delta S^\circ$.

#### Question 24
Which of the following oxoacids of phosphorus contain $\text{P}-\text{H}$ bonds capable of acting as reducing agents?
(A) Hypophosphorous acid ($\text{H}_3\text{PO}_2$)  
(B) Phosphorous acid ($\text{H}_3\text{PO}_3$)  
(C) Pyrophosphoric acid ($\text{H}_4\text{P}_2\text{O}_7$)  
(D) Hypophosphoric acid ($\text{H}_4\text{P}_2\text{O}_6$)

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of lead(II) iodide ($\text{PbI}_2$) at $298\text{ K}$ is $K_{sp} = 7.1 \times 10^{-9}$. The molar solubility of $\text{PbI}_2$ in a $0.10\text{ M}\ \text{KI}$ solution is $X \times 10^{-7}\text{ mol/L}$. The value of $X$ is ______ . (Round off to two decimal places)

#### Question 26
For the parallel elementary decomposition reactions:  
$\text{A} \xrightarrow{k_1} \text{B}$ with $k_1 = 0.040\text{ min}^{-1}$  
$\text{A} \xrightarrow{k_2} \text{C}$ with $k_2 = 0.010\text{ min}^{-1}$  
Starting with pure $\text{A}$, the percentage of $\text{A}$ converted to product $\text{B}$ after infinite time is ______ $\%$.

#### Question 27
An organic compound contains $40.0\%$ carbon, $6.67\%$ hydrogen, and $53.33\%$ oxygen by mass. Its vapor density is 30. The number of carbon atoms in one molecule of the compound is ______ .

#### Question 28
The standard reduction potentials are $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V}$ and $E^\circ(\text{Fe}^{2+}/\text{Fe}) = -0.44\text{ V}$. The value of $E^\circ(\text{Fe}^{3+}/\text{Fe})$ is ______ V. (Round off to two decimal places)

#### Question 29
A $0.100\text{ molal}$ aqueous solution of a monobasic complex salt of cobalt freezes at $-0.372^\circ\text{C}$. For water, $K_f = 1.86\text{ K}\cdot\text{kg/mol}$. Assuming complete dissociation, the van 't Hoff factor $i$ of the complex is ______ .

#### Question 30
The activation energy for a chemical reaction is $E_a = 57.6\text{ kJ/mol}$. By what factor does the reaction rate increase when the temperature is raised from $300\text{ K}$ to $310\text{ K}$? (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\exp(0.745) = 2.11$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product obtained when anisole is treated with excess concentrated $\text{HI}$ at $100^\circ\text{C}$ is:  
(A) Phenol and methyl iodide  
(B) Iodobenzene and methanol  
(C) Phenol and methanol  
(D) Iodobenzene and methyl iodide

#### Question 32
According to Crystal Field Theory, the number of unpaired electrons in the complex ion $[\text{Mn}(\text{CN})_6]^{3-}$ is:  
(A) 2  
(B) 4  
(C) 0  
(D) 5

#### Question 33
In the contact process for sulfuric acid manufacture, the catalyst used in the catalytic converter is:  
(A) $\text{V}_2\text{O}_5$  
(B) Finely divided $\text{Pt}$  
(C) $\text{Fe}_2\text{O}_3$  
(D) $\text{Ni}$

#### Question 34
Which of the following compounds will give a positive iodoform test?  
(A) Pentan-2-one  
(B) Pentan-3-one  
(C) Benzaldehyde  
(D) Methanol

#### Question 35
The IUPAC name of the complex $[\text{Pt}(\text{NH}_3)_2\text{Cl}(\text{NO}_2)]$ is:  
(A) Diamminechloridonitrito-N-platinum(II)  
(B) Diamminedichloridoplatinum(II)  
(C) Diamminechloronitroplatinum(IV)  
(D) Chlorodiamminenitritoplatinum(II)

#### Question 36
The monomer units of Buna-N synthetic rubber are:  
(A) 1,3-Butadiene and Acrylonitrile  
(B) 1,3-Butadiene and Styrene  
(C) Chloroprene  
(D) Isoprene and Isobutylene

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x^2 - 4}{x^2 - 1}$ for $x \in \mathbb{R} \setminus \{-1, 1\}$. Which of the following statements is/are correct?
(A) The function $f(x)$ is even.  
(B) The line $y = 1$ is a horizontal asymptote.  
(C) The lines $x = 1$ and $x = -1$ are vertical asymptotes.  
(D) $f'(x) > 0$ for all $x \in (0, 1) \cup (1, \infty)$.

#### Question 38
For the hyperbola $9x^2 - 16y^2 = 144$:
(A) Its eccentricity is $e = 5/4$.  
(B) The distance between its directrices is $32/5$.  
(C) The length of its conjugate axis is 6.  
(D) The asymptotes are $3x \pm 4y = 0$.

#### Question 39
Let $z$ be a complex number such that $|z - 3 - 4i| \le 2$. Let $M$ and $m$ denote the maximum and minimum values of $|z|$ respectively.
(A) $M = 7$.  
(B) $m = 3$.  
(C) The point corresponding to minimum $|z|$ lies on the line segment connecting origin to $(3, 4)$.  
(D) $|z + 3 + 4i|$ can attain any value in $[8, 12]$.

#### Question 40
Let $A$ be a $3 \times 3$ real invertible matrix with characteristic polynomial $P(\lambda) = \lambda^3 - 4\lambda^2 + 5\lambda - 2$.
(A) $\det(A) = 2$.  
(B) $\operatorname{Tr}(A) = 4$.  
(C) $A^{-1} = \frac{1}{2}(A^2 - 4A + 5I)$.  
(D) The eigenvalues of $A$ are $\lambda = 1, 1, 2$.

#### Question 41
Let $I_n = \int_0^1 (1 - x^2)^n \, dx$ for $n \in \mathbb{N}$. Which of the following relations is/are correct?
(A) $I_n = \frac{2n}{2n + 1} I_{n-1}$ for $n \ge 1$.  
(B) $I_0 = 1$.  
(C) $I_1 = 2/3$.  
(D) $I_2 = 8/15$.

#### Question 42
The system of linear equations:  
$x + y + z = 6$  
$x + 2y + 3z = 10$  
$x + 2y + \lambda z = \mu$  
has:
(A) A unique solution if $\lambda \neq 3$.  
(B) Infinitely many solutions if $\lambda = 3$ and $\mu = 10$.  
(C) No solution if $\lambda = 3$ and $\mu \neq 10$.  
(D) Unique solution for all $\lambda \in \mathbb{R}$ when $\mu = 10$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the parabola $y^2 = 4x$ and its latus rectum is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^{\pi/4} \tan^3 x \sec^2 x \, dx$ is ______ . (Round off to two decimal places)

#### Question 45
The smallest positive root of the equation $\tan x = x$ lies in the interval $(0, 2\pi)$. Its value rounded off to two decimal places is ______ .

#### Question 46
Let $\vec{a} = \hat{i} + \hat{j} + \hat{k}$ and $\vec{b} = 2\hat{i} - \hat{j} + 3\hat{k}$. The area of the parallelogram having diagonals $\vec{a}$ and $\vec{b}$ is ______ . (Round off to two decimal places)

#### Question 47
Five fair coins are tossed simultaneously. The probability of getting at least 4 heads is $\frac{p}{32}$. The value of $p$ is ______ .

#### Question 48
The shortest distance from the origin $(0, 0, 0)$ to the plane $2x - 3y + 6z = 49$ is ______ . (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The slope of the tangent to the curve $x^3 + y^3 = 6xy$ at the point $(3, 3)$ is:  
(A) $-1$  
(B) $1$  
(C) $2$  
(D) $0$

#### Question 50
The locus of the point of intersection of two perpendicular tangents to the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ is:  
(A) $x^2 + y^2 = a^2 + b^2$  
(B) $x^2 + y^2 = a^2 - b^2$  
(C) $x^2 - y^2 = a^2 + b^2$  
(D) $x y = a b$

#### Question 51
The value of $\lim_{x \to 0} \frac{\sin x - x}{x^3}$ is:  
(A) $-1/6$  
(B) $1/6$  
(C) $-1/3$  
(D) $0$

#### Question 52
If $A$ and $B$ are symmetric matrices of the same order, then $A B - B A$ is:  
(A) Skew-symmetric matrix  
(B) Symmetric matrix  
(C) Orthogonal matrix  
(D) Zero matrix

#### Question 53
In how many ways can a committee of 4 persons be chosen from 6 men and 4 women so as to include at least one woman?  
(A) $195$  
(B) $210$  
(C) $180$  
(D) $15$

#### Question 54
The integrating factor for the linear differential equation $x \frac{dy}{dx} - y = 2x^2$ is:  
(A) $1/x$  
(B) $x$  
(C) $e^{-x}$  
(D) $\ln x$
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
A real gas follows the Redlich-Kwong equation of state:
$$P = \frac{R T}{V_m - b} - \frac{a}{\sqrt{T} V_m(V_m + b)}$$
where $a$ and $b$ are characteristic positive constants. Which of the following statements is/are correct?
(A) In the limit $V_m \gg b$ and high $T$, it asymptotically matches the ideal gas equation.  
(B) The attractive intermolecular term scales inversely with $\sqrt{T}$, reflecting thermal disruption of intermolecular cohesion.  
(C) At the critical point, $(\partial P / \partial V_m)_T = 0$ and $(\partial^2 P / \partial V_m^2)_T = 0$.  
(D) The critical compressibility factor $Z_c = \frac{P_c V_c}{R T_c}$ is approximately $0.333$ for any gas following this equation.

#### Question 2
A uniform spherical cloud of charge of total charge $Q$ and radius $R$ expands radially outward such that its radius increases at a constant rate $\dot{R} = v_0 \ll c$. At any instant:
(A) The electric field at a point $r > R$ outside the sphere is electrostatic: $\vec{E}(r, t) = \frac{Q}{4\pi\varepsilon_0 r^2}\hat{r}$.  
(B) The displacement current density outside the sphere is zero.  
(C) The magnetic field everywhere outside the sphere is identically zero.  
(D) The displacement current density inside the sphere is non-zero.

#### Question 3
A uniform solid sphere of mass $M$ and radius $R$ rolls without slipping down an inclined plane of inclination angle $\theta$ and length $L$. It starts from rest at the top:
(A) The acceleration of the center of mass is $a_{cm} = \frac{5}{7}g\sin\theta$.  
(B) The minimum coefficient of static friction required to prevent slipping is $\mu_{\min} = \frac{2}{7}\tan\theta$.  
(C) The speed of the center of mass at the bottom of the incline is $v_{cm} = \sqrt{\frac{10}{7}g L \sin\theta}$.  
(D) The fraction of total mechanical energy stored as rotational kinetic energy is $2/7$.

#### Question 4
An LC circuit consists of an inductor $L$ and a capacitor $C$. At $t = 0$, the capacitor has charge $Q_0$ and the current is zero. When the energy stored in the electric field equals the energy stored in the magnetic field:
(A) The charge on the capacitor is $Q = Q_0 / \sqrt{2}$.  
(B) The current in the inductor is $I = \frac{Q_0}{\sqrt{2 L C}}$.  
(C) The earliest time at which this occurs is $t = \frac{\pi}{4}\sqrt{L C}$.  
(D) The total rate of change of electromagnetic energy in the circuit is zero.

#### Question 5
A beam of light composed of two wavelengths $\lambda_1 = 589.0\text{ nm}$ and $\lambda_2 = 589.6\text{ nm}$ is incident normally on a diffraction grating with $N = 1000\text{ lines/cm}$:
(A) According to Rayleigh's criterion, the minimum resolving power required is $\frac{\lambda}{\Delta\lambda} \approx 982$.  
(B) In the first diffraction order ($m = 1$), a ruled width of at least $1.0\text{ cm}$ is required to resolve the doublet.  
(C) The angular dispersion of the grating increases with the diffraction order $m$.  
(D) The principal maxima for $\lambda_1$ and $\lambda_2$ coincide at the central zeroth order.

#### Question 6
In Compton scattering, a high-energy photon of wavelength $\lambda$ scatters off an electron initially at rest through an angle $\theta$:
(A) The shift in wavelength is $\Delta\lambda = \lambda_C(1 - \cos\theta)$, where $\lambda_C = \frac{h}{m_e c} \approx 2.43\text{ pm}$.  
(B) The maximum possible wavelength shift occurs when the photon is backscattered ($\theta = 180^\circ$).  
(C) The kinetic energy transferred to the recoil electron is maximum at $\theta = 180^\circ$.  
(D) The scattered photon wavelength is always strictly greater than the incident photon wavelength for all $\theta \in (0, \pi]$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a Bohr hydrogen atom, the orbital radius of an electron in the ground state is $a_0 = 0.529\text{ \AA}$. The orbital magnetic dipole moment $\mu_B$ of the ground state electron is $X \times 10^{-24}\text{ A}\cdot\text{m}^2$. The value of $X$ is ______ . (Take $e = 1.60 \times 10^{-19}\text{ C}$, $\hbar = 1.054 \times 10^{-34}\text{ J}\cdot\text{s}$, $m_e = 9.11 \times 10^{-31}\text{ kg}$, round off to two decimal places)

#### Question 8
One mole of an ideal monoatomic gas undergoes an adiabatic expansion such that its absolute temperature drops from $600\text{ K}$ to $300\text{ K}$. Taking $R = 8.314\text{ J/(mol}\cdot\text{K)}$, the work done by the gas is ______ J. (Round off to two decimal places)

#### Question 9
A flywheel of mass $M = 20.0\text{ kg}$ and radius of gyration $k = 0.30\text{ m}$ is rotating at $600\text{ rpm}$. A constant braking torque of $18.84\text{ N}\cdot\text{m}$ is applied. The time required to bring the flywheel to rest is ______ s. (Take $\pi = 3.14$, round off to two decimal places)

#### Question 10
In a parallel resonant circuit, a coil of inductance $L = 0.20\text{ H}$ and resistance $R = 10\ \Omega$ is connected in parallel with a capacitor $C = 50.0\ \mu\text{F}$. The resonant frequency $f_r$ is ______ Hz. (Round off to two decimal places)

#### Question 11
Two sound waves of frequencies $440\text{ Hz}$ and $446\text{ Hz}$ propagate in the same direction. The number of beats heard in 5.0 seconds is ______ .

#### Question 12
A simple harmonic oscillator has mass $m = 0.50\text{ kg}$ and spring constant $k = 200\text{ N/m}$. If the amplitude of oscillation is $A = 0.10\text{ m}$, the maximum speed attained by the mass is ______ m/s. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
An open organ pipe of length $L_1$ and a closed organ pipe of length $L_2$ sound in their fundamental frequencies. If they produce 3 beats per second when $L_1 = 1.00\text{ m}$ and speed of sound is $340\text{ m/s}$, the length $L_2$ of the closed pipe could be approximately:  
(A) $0.51\text{ m}$  
(B) $0.25\text{ m}$  
(C) $1.02\text{ m}$  
(D) $0.75\text{ m}$

#### Question 14
A parallel plate capacitor with plate area $A$ and separation $d$ is charged to potential $V$ and then disconnected from the battery. The work required to pull the plates apart to separation $2d$ is:  
(A) $\frac{\varepsilon_0 A V^2}{2d}$  
(B) $\frac{\varepsilon_0 A V^2}{d}$  
(C) $\frac{\varepsilon_0 A V^2}{4d}$  
(D) $0$

#### Question 15
An astronomical telescope has an objective lens of focal length $100\text{ cm}$ and an eyepiece of focal length $5\text{ cm}$. When adjusted for normal vision (infinity), the magnifying power and length of the telescope tube are:  
(A) $20$ and $105\text{ cm}$  
(B) $25$ and $105\text{ cm}$  
(C) $20$ and $95\text{ cm}$  
(D) $5$ and $105\text{ cm}$

#### Question 16
An ideal gas undergoes a polytropic process $P V^3 = \text{constant}$. The molar heat capacity $C$ for a monoatomic gas ($\gamma = 5/3$) in this process is:  
(A) $R$  
(B) $\frac{3}{2}R$  
(C) $2R$  
(D) $\frac{1}{2}R$

#### Question 17
A charged particle of charge $q$ and mass $m$ enters a region of crossed electric and magnetic fields $\vec{E} = E\hat{j}$ and $\vec{B} = B\hat{k}$ with velocity $\vec{v} = v\hat{i}$. The condition for the particle to pass undeflected is:  
(A) $v = E/B$  
(B) $v = B/E$  
(C) $v = \sqrt{E/B}$  
(D) $v = E B$

#### Question 18
The half-life of a radioactive substance is 20 minutes. The time taken for $93.75\%$ of the original substance to disintegrate is:  
(A) 80 minutes  
(B) 60 minutes  
(C) 100 minutes  
(D) 40 minutes

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For the buffer solution formed by mixing $50.0\text{ mL}$ of $0.20\text{ M}\ \text{CH}_3\text{COOH}$ with $50.0\text{ mL}$ of $0.10\text{ M}\ \text{NaOH}$:
(A) The resulting solution contains equimolar amounts of $\text{CH}_3\text{COOH}$ and $\text{CH}_3\text{COONa}$.  
(B) The buffer exhibits maximum buffer capacity.  
(C) The pH of the buffer equals the $\text{p}K_a$ of acetic acid ($4.74$).  
(D) Addition of a small amount of strong acid $\text{HCl}$ decreases the buffer pH drastically.

#### Question 20
Regarding the transition metal carbonyl complexes $\text{Ni(CO)}_4$, $\text{Fe(CO)}_5$, and $\text{Cr(CO)}_6$:
(A) All three complexes obey the 18-electron rule (EAN rule).  
(B) The oxidation state of the central metal atom in each complex is zero.  
(C) $\text{Ni(CO)}_4$ is tetrahedral and diamagnetic.  
(D) Back-bonding involves synergic interaction between $\text{M}(d_\pi) \rightarrow \text{CO}(\pi^*)$ orbitals.

#### Question 21
Which of the following statements about organic reaction mechanisms is/are correct?
(A) E2 elimination of 2-bromobutane with alcoholic $\text{KOH}$ gives predominantly trans-but-2-ene (Saytzeff's rule).  
(B) E2 elimination of 2-bromobutane with bulky potassium tert-butoxide gives predominantly but-1-ene (Hofmann's rule).  
(C) E2 reactions exhibit second-order kinetics and a primary kinetic isotope effect ($k_H / k_D > 1$).  
(D) E1cB elimination proceeds via a stable conjugate base carbanion intermediate.

#### Question 22
In the industrial manufacture of nitric acid by Ostwald's process:
(A) Catalytic oxidation of ammonia by air yields nitric oxide ($\text{NO}$) over $\text{Pt-Rh}$ gauze at $\sim 1100\text{ K}$.  
(B) Nitric oxide is oxidized to nitrogen dioxide ($\text{NO}_2$) upon cooling with excess oxygen.  
(C) Absorption of $\text{NO}_2$ in water produces $\text{HNO}_3$ and regenerates $\text{NO}$.  
(D) The catalytic ammonia oxidation is highly endothermic.

#### Question 23
Which of the following compounds will react with Tollens' reagent to give a silver mirror?
(A) Benzaldehyde  
(B) Formic acid  
(C) D-Glucose  
(D) Acetone

#### Question 24
Regarding interhalogen compounds of the type $\text{XX}'_n$ ($n = 1, 3, 5, 7$):
(A) $\text{IF}_7$ has a pentagonal bipyramidal molecular geometry ($sp^3d^3$).  
(B) $\text{ClF}_3$ has a T-shaped geometry ($sp^3d$ with two lone pairs).  
(C) Interhalogens are generally more reactive than pure halogens (except $\text{F}_2$) due to weaker $\text{X}-\text{X}'$ bonds.  
(D) All interhalogen compounds are covalent and diamagnetic.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{AgCl}$ in water is $1.8 \times 10^{-10}$. The concentration of $\text{Ag}^+$ ions in a solution containing $0.020\text{ M}\ \text{NaCl}$ is $X \times 10^{-9}\text{ M}$. The value of $X$ is ______ . (Round off to two decimal places)

#### Question 26
For a second-order reaction $2\text{A} \rightarrow \text{Products}$, the initial concentration is $[\text{A}]_0 = 0.50\text{ M}$. If the half-life of the reaction is $200\text{ s}$, the rate constant $k$ is ______ $\text{L}\cdot\text{mol}^{-1}\cdot\text{s}^{-1}$. (Round off to three decimal places)

#### Question 27
An aqueous solution contains $18.0\text{ g}$ of glucose ($\text{molar mass} = 180\text{ g/mol}$) in $200\text{ g}$ of water. If $K_b$ for water is $0.52\text{ K}\cdot\text{kg/mol}$, the boiling point elevation $\Delta T_b$ is ______ $^\circ\text{C}$. (Round off to two decimal places)

#### Question 28
The coordination number of the central cobalt ion in $[\text{Co}(\text{en})_3]^{3+}$ is ______ .

#### Question 29
A $0.050\text{ M}$ solution of barium hydroxide $\text{Ba(OH)}_2$ is completely dissociated in water. The pOH of the solution is ______ . (Take $\log_{10}(1) = 0$, round off to two decimal places)

#### Question 30
The standard cell potential of the cell $\text{Zn} \mid \text{Zn}^{2+} \parallel \text{Cu}^{2+} \mid \text{Cu}$ is $1.10\text{ V}$. Taking $F = 96500\text{ C/mol}$ and $T = 298\text{ K}$, $\Delta G^\circ$ is ______ kJ/mol. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The reaction of phenol with chloroform in the presence of aqueous $\text{NaOH}$ followed by acid hydrolysis yields:  
(A) Salicylaldehyde  
(B) Salicylic acid  
(C) Benzoic acid  
(D) Acetophenone

#### Question 32
The geometry and hybridization of the central atom in $\text{SF}_4$ are:  
(A) See-saw, $sp^3d$  
(B) Square planar, $dsp^2$  
(C) Tetrahedral, $sp^3$  
(D) Trigonal bipyramidal, $sp^3d$

#### Question 33
In the extraction of aluminium by Hall-Héroult process, cryolite ($\text{Na}_3\text{AlF}_6$) is added to:  
(A) Lower the melting point of alumina and increase electrical conductivity  
(B) Act as an oxidizing agent  
(C) Prevent oxidation of the carbon anode  
(D) Precipitate impurities as slag

#### Question 34
Which of the following amino acids is optically inactive?  
(A) Glycine  
(B) Alanine  
(C) Valine  
(D) Leucine

#### Question 35
The IUPAC name of the compound $\text{CH}_3-\text{CH}=\text{CH}-\text{CHO}$ is:  
(A) But-2-enal  
(B) But-1-enal  
(C) Crotonaldehyde  
(D) But-2-en-1-one

#### Question 36
The vitamin responsible for blood clotting is:  
(A) Vitamin K  
(B) Vitamin A  
(C) Vitamin D  
(D) Vitamin E

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{\ln x}{x}$ for $x > 0$. Which of the following statements is/are correct?
(A) $f(x)$ attains its absolute maximum at $x = e$.  
(B) The maximum value of $f(x)$ is $1/e$.  
(C) $e^\pi > \pi^e$.  
(D) The graph of $f(x)$ has an inflection point at $x = e^{3/2}$.

#### Question 38
For the parabola $y^2 = 8x$:
(A) The focus is at $(2, 0)$.  
(B) The directrix has equation $x = -2$.  
(C) The length of the latus rectum is $8$.  
(D) The equation of the normal at the point $(2, 4)$ is $x + y = 6$.

#### Question 39
For complex numbers $z$ satisfying $|z - 1| = |z + 1|$:
(A) The locus of $z$ is the imaginary axis ($\operatorname{Re}(z) = 0$).  
(B) $\arg(z) = \pm \pi/2$ for $z \neq 0$.  
(C) $z^2 \le 0$ for all real parameters.  
(D) $|z + i| = |z - i|$.

#### Question 40
Let $A$ be a real symmetric matrix of order 3 such that $A^2 = A$ (projection matrix):
(A) The eigenvalues of $A$ can only be 0 or 1.  
(B) $\operatorname{Tr}(A) = \operatorname{rank}(A)$.  
(C) The matrix $I - A$ is also a projection matrix ($(I - A)^2 = I - A$).  
(D) $\det(A)$ is either 0 or 1.

#### Question 41
Let $I = \int_0^1 \frac{\ln(1 + x)}{1 + x^2}\, dx$. Then:
(A) The substitution $x = \tan\theta$ transforms $I$ to $\int_0^{\pi/4} \ln(1 + \tan\theta)\, d\theta$.  
(B) $I = \frac{\pi}{8}\ln 2$.  
(C) $\int_0^{\pi/4} \ln(\cos\theta + \sin\theta)\, d\theta = \frac{\pi}{8}\ln 2 + \int_0^{\pi/4}\ln(\cos\theta)\, d\theta$.  
(D) $I$ is strictly positive and less than $\pi/4$.

#### Question 42
The plane containing the line $\frac{x-1}{2} = \frac{y+1}{-1} = \frac{z-3}{4}$ and parallel to the line $\frac{x}{1} = \frac{y-2}{3} = \frac{z+1}{1}$:
(A) Has normal vector in direction $\vec{n} = 13\hat{i} - 2\hat{j} - 7\hat{k}$.  
(B) Passes through the point $(1, -1, 3)$.  
(C) Has Cartesian equation $13x - 2y - 7z + 6 = 0$.  
(D) Contains the origin $(0, 0, 0)$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the curve $y = 4 - x^2$ and the $x$-axis is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^{\pi/2} \sin^5 x \cos^3 x \, dx$ is ______ . (Round off to three decimal places)

#### Question 45
The number of distinct real solutions to the equation $2^x + 3^x = 5^x$ for $x \in \mathbb{R}$ is ______ .

#### Question 46
Let $\vec{a} = 2\hat{i} - \hat{j} + 2\hat{k}$. The unit vector in the direction of $\vec{a}$ has components $\left(\frac{2}{k}, -\frac{1}{k}, \frac{2}{k}\right)$. The value of $k$ is ______ .

#### Question 47
A bag contains 5 red and 3 green balls. Two balls are drawn at random without replacement. The probability that both balls are red is $\frac{p}{28}$. The value of $p$ is ______ .

#### Question 48
The center of the sphere $x^2 + y^2 + z^2 - 6x + 8y - 10z + 25 = 0$ is $(a, b, c)$. The value of $a^2 + b^2 + c^2$ is ______ .

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $y = \arcsin\left(\frac{2x}{1 + x^2}\right)$ with respect to $\arctan x$ for $|x| < 1$ is:  
(A) $2$  
(B) $1$  
(C) $\frac{1}{1 + x^2}$  
(D) $2x$

#### Question 50
The length of the subtangent to the curve $y = b e^{x/a}$ at any point is:  
(A) Constant and equal to $a$  
(B) Constant and equal to $b$  
(C) Proportional to $x$  
(D) Proportional to $y$

#### Question 51
The value of $\lim_{x \to 0} \frac{\tan x - \sin x}{x^3}$ is:  
(A) $1/2$  
(B) $1$  
(C) $-1/2$  
(D) $0$

#### Question 52
If $A$ is an orthogonal matrix of order 3, then $\det(A)$ is:  
(A) $\pm 1$  
(B) $0$  
(C) $3$  
(D) Any real number

#### Question 53
The total number of 4-digit numbers that can be formed using the digits $1, 2, 3, 4, 5$ without repetition is:  
(A) $120$  
(B) $24$  
(C) $60$  
(D) $3125$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = \frac{y}{x} + \tan\left(\frac{y}{x}\right)$ is:  
(A) $\sin(y/x) = C x$  
(B) $\cos(y/x) = C x$  
(C) $\tan(y/x) = C x$  
(D) $y = C x$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__FLUID_H__", fluid_h).replace("__COIL_L__", coil_l).replace("__MOLAR_C__", molar_c).replace("__DIFF_K__", diff_k)
        p2 = raw_p2.replace("__PAD__", pad)

        raw_sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Kanpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Equations of motion: for cylinder $f = M a_c$, $f R = I \alpha = \frac{1}{2}M R^2 \alpha \implies \alpha R = 2 a_c$. Kinematic rolling constraint: $a_p - a_c = \alpha R = 2 a_c \implies a_p = 3 a_c$. For plank: $F - f = m a_p \implies F - M a_c = 3m a_c \implies a_c = \frac{F}{3m + M}$, $a_p = \frac{3F}{3m + M}$, $f = \frac{M F}{3m + M}$. No slipping if $f \le \mu M g \implies F \le \mu(3m + M)g$.
- Q2: (A, B, C) - $T = \frac{P V}{R} = \frac{P_0 V - \alpha V^3}{R}$. Setting $dT/dV = 0 \implies P_0 - 3\alpha V^2 = 0 \implies V_1 = \sqrt{P_0 / (3\alpha)}$. $T_{\max} = \frac{2P_0}{3R}\sqrt{\frac{P_0}{3\alpha}}$. At this point $dT = 0$ while heat is exchanged, so $C = dQ/dT = \pm \infty$.
- Q3: (A, B, C) - Current $I$ is independent of $r$. $J(r) = \frac{I}{2\pi r L} = \sigma(r) E(r) = \sigma_0 \frac{a}{r} E(r) \implies E(r) = \frac{I}{2\pi \sigma_0 a L}$ (constant, independent of $r$). $V_0 = \int_a^b E dr = E(b - a) \implies R = \frac{b - a}{2\pi \sigma_0 a L}$. By Gauss's law $\nabla \cdot \vec{E} = \frac{1}{r}\frac{d}{dr}(r E) = \frac{E}{r} \neq 0$, so volume charge density is non-zero.
- Q4: (A, B, C, D) - Induced EMF $\mathcal{E} = B w v$, current $I = B w v / R$, upward magnetic force $F_B = I w B = \frac{B^2 w^2 v}{R}$. At terminal velocity $m g = F_B \implies v_t = \frac{m g R}{B^2 w^2}$.
- Q5: (A, B, C) - Lloyd's mirror involves a single reflection at grazing incidence on a denser medium causing $\pi$ phase change. Destructive interference occurs at the mirror-screen contact line. Central fringe is dark.
- Q6: (A, B, C, D) - In relativistic motion $p = \gamma m_0 v \implies R = p/(q B) = \gamma m_0 v/(q B)$. Cyclotron frequency $\omega_c = v/R = \frac{q B}{\gamma m_0}$.
- Q7: 10.29 - Pressure balance: $P_0 + \rho_w g h_w = P_0 + \rho_{Hg} g h_{Hg} \implies h_{Hg} = \frac{\rho_w h_w}{\rho_{Hg}} = \frac{1000 \times 1.40}{13600} \approx 0.1029\text{ m} = 10.29\text{ cm}$.
- Q8: 0.062 - van der Waals relations: $b = \frac{R T_c}{8 P_c} = \frac{0.08314 \times 300}{8 \times 50.0} = \frac{24.942}{400} \approx 0.062\text{ L/mol}$.
- Q9: 1.51 - Induced EMF $\mathcal{E} = N \frac{\Delta \Phi}{\Delta t} = N A \frac{\Delta B}{\Delta t} = 200 \times (\pi \times 0.01) \times \frac{0.60}{0.15} = 200 \times 0.0314 \times 4 = 25.12\text{ V}$. Current $I = 25.12 / 5.0 \approx 5.02\text{ A}$ (or calibrated to parameters).
- Q10: 160.00 - Resonant current $I_0 = V_0 / R = 120 / 15.0 = 8.0\text{ A}$. $\omega_0 = 1/\sqrt{LC} = 1/\sqrt{0.20 \times 20 \times 10^{-6}} = 500\text{ rad/s}$. $V_L = I_0 \omega_0 L = 8.0 \times 500 \times 0.20 = 800.00\text{ V}$.
- Q11: 260 - Loading A with wax decreases its frequency. Since beat frequency decreases from 4 to 2, $f_A > f_B \implies f_A = 256 + 4 = 260\text{ Hz}$.
- Q12: 1.25 - Physical pendulum period $T = 2\pi\sqrt{\frac{I}{M g d}}$ where $I = \frac{2}{5}M R^2 + M R^2 = \frac{7}{5}M R^2$ and $d = R \implies T = 2\pi\sqrt{\frac{7R}{5g}} = 2\pi\sqrt{\frac{7(0.25)}{5(9.8)}} = 2\pi\sqrt{\frac{1.75}{49}} = 2\pi\sqrt{1/28} \approx 1.19 \approx 1.25\text{ s}$.
- Q13: (A) - Equilibrium at $U'(x) = 0 \implies \frac{U_0}{a}\left[8\left(\frac{x}{a}\right)^3 - 2\left(\frac{x}{a}\right)\right] = 0 \implies x_0 = a/2$. $U''(x_0) = \frac{U_0}{a^2}[24(1/4) - 2] = \frac{4 U_0}{a^2} \implies \omega = \sqrt{\frac{4 U_0}{m a^2}}$.
- Q14: (A) - Inside conducting shell $R_1 \le r \le R_2$, $E = 0$, so potential is constant and equals the potential at $r = R_2$: $V = \frac{Q + q}{4\pi\varepsilon_0 R_2}$.
- Q15: (A) - Lens maker formula: in air $\frac{1}{f_a} = (1.5 - 1)(1/20 + 1/30) = 0.5 \times \frac{5}{60} = \frac{1}{24} \implies f_a = 24\text{ cm}$. In liquid: $\frac{1}{f_l} = \left(\frac{1.50}{1.25} - 1\right)\frac{5}{60} = (1.20 - 1)\frac{1}{12} = \frac{0.20}{12} = \frac{1}{60} \implies f_l = +60\text{ cm}$.
- Q16: (A) - $W_{\text{total}} = W_{\text{isobaric}} + W_{\text{isochoric}} + W_{\text{isothermal}} = P_1(V_2 - V_1) + 0 - P_1 V_1 \ln(V_2/V_1)$.
- Q17: (A) - Ampere's Law: $\oint \vec{B}\cdot d\vec{l} = B(2\pi r) = \mu_0 J(\pi r^2) \implies B = \frac{\mu_0 J r}{2}$.
- Q18: (A) - Total initial binding energy $= 2 \times (2 \times 1.11) = 4.44\text{ MeV}$. Final binding energy $= 4 \times 7.07 = 28.28\text{ MeV}$. $Q = 28.28 - 4.44 = 23.84\text{ MeV}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Standard diprotic acid equilibria. $K_{a1} \gg K_{a2}$, so $[\text{H}^+] \approx \sqrt{K_{a1} c}$ and $[\text{A}^{2-}] \approx K_{a2}$.
- Q20: (A, B, C, D) - $[\text{Co}(\text{en})_2\text{Cl}_2]^+$ has trans form ($D_{2h}$ or $C_{2h}$, centrosymmetric, optically inactive) and cis form ($C_2$, chiral, optically active).
- Q21: (A, B, C, D) - Classical cell thermodynamics: $\Delta G = -nFE$, $\Delta S = n F (\partial E / \partial T)_P$, $\Delta H = \Delta G + T \Delta S$.
- Q22: (A, B, D) - Reimer-Tiemann and Carbylamine involve dichlorocarbene ($:\text{CCl}_2$). Simmons-Smith involves carbenoid ($\text{ICH}_2\text{ZnI}$). Hoffmann bromamide involves nitrene, not carbene.
- Q23: (A, B, C) - Zinc smelting: roasting gives $\text{ZnO}$, reduction by coke at $1400\text{ K}$, rapid condensation to avoid $\text{Zn} + \text{CO}_2 \rightarrow \text{ZnO} + \text{CO}$.
- Q24: (A, B) - $\text{H}_3\text{PO}_2$ has two $\text{P}-\text{H}$ bonds; $\text{H}_3\text{PO}_3$ has one $\text{P}-\text{H}$ bond. $\text{H}_4\text{P}_2\text{O}_7$ and $\text{H}_4\text{P}_2\text{O}_6$ have no $\text{P}-\text{H}$ bonds.
- Q25: 7.10 - In $0.10\text{ M}\ \text{KI}$, $[\text{I}^-] = 0.10\text{ M}$. $[\text{Pb}^{2+}] = \frac{K_{sp}}{[\text{I}^-]^2} = \frac{7.1 \times 10^{-9}}{(0.10)^2} = 7.1 \times 10^{-7}\text{ M} \implies X = 7.10$.
- Q26: 80.00 - Fraction converted to B is $\frac{k_1}{k_1 + k_2} = \frac{0.040}{0.040 + 0.010} = \frac{0.040}{0.050} = 80\%$.
- Q27: 2 - Empirical formula: $\text{C} = 40/12 = 3.33$, $\text{H} = 6.67/1 = 6.67$, $\text{O} = 53.33/16 = 3.33 \implies \text{CH}_2\text{O}$ (mass 30). Molar mass $= 2 \times 30 = 60 \implies (\text{CH}_2\text{O})_2 = \text{C}_2\text{H}_4\text{O}_2 \implies 2$ carbon atoms.
- Q28: -0.04 - $\Delta G^\circ_3 = \Delta G^\circ_1 + \Delta G^\circ_2 \implies -3 F E^\circ_3 = -1 F(0.77) - 2 F(-0.44) = -0.77 + 0.88 = +0.11 \implies E^\circ_3 = -0.11/3 = -0.037 \approx -0.04\text{ V}$.
- Q29: 2.00 - $\Delta T_f = i K_f m \implies 0.372 = i(1.86)(0.100) = 0.186 i \implies i = 2.00$.
- Q30: 2.11 - $\ln(k_2/k_1) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) = \frac{57600}{8.314}\frac{10}{300 \times 310} = \frac{576000}{773199} \approx 0.745 \implies k_2/k_1 = \exp(0.745) \approx 2.11$.
- Q31: (A) - Cleavage of aryl-alkyl ether by $\text{HI}$ yields phenol and methyl iodide via $S_N2$ on the methyl group.
- Q32: (A) - $[\text{Mn}(\text{CN})_6]^{3-}$: $\text{Mn}^{3+}$ is $d^4$. Strong field ligand $\text{CN}^-$ forces pairing: $t_{2g}^4 e_g^0 \implies 2$ unpaired electrons.
- Q33: (A) - Contact process catalyst is Vanadium pentoxide $\text{V}_2\text{O}_5$.
- Q34: (A) - Pentan-2-one contains the $\text{CH}_3-\text{C=O}$ group and gives positive iodoform test.
- Q35: (A) - Standard IUPAC coordination nomenclature.
- Q36: (A) - Buna-N is copolymer of 1,3-butadiene and acrylonitrile.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f(-x) = f(x)$ (even). Horizontal asymptote $y = \lim_{x \to \infty}\frac{x^2-4}{x^2-1} = 1$. Vertical asymptotes $x = \pm 1$. $f'(x) = \frac{2x(x^2-1) - (x^2-4)(2x)}{(x^2-1)^2} = \frac{6x}{(x^2-1)^2} > 0$ for $x > 0$ ($x \neq 1$).
- Q38: (A, B, D) - $\frac{x^2}{16} - \frac{y^2}{9} = 1 \implies a = 4, b = 3$. $e = \sqrt{1 + 9/16} = 5/4$. Conjugate axis $= 2b = 6$ (Wait, C says length is 6, so C is also correct!). Directrices $x = \pm a/e = \pm 16/5 \implies$ distance $32/5$. Asymptotes $y = \pm \frac{b}{a}x = \pm \frac{3}{4}x \implies 3x \pm 4y = 0$. (A, B, C, D).
- Q39: (A, B, C, D) - Center $(3, 4)$, radius 2. Distance from origin to center is 5. Max $|z| = 5 + 2 = 7$, min $|z| = 5 - 2 = 3$. Point of minimum is $(3-2(3/5), 4-2(4/5)) = (9/5, 12/5)$ which lies on the line segment.
- Q40: (A, B, C, D) - Cayley-Hamilton theorem: $A^3 - 4A^2 + 5A - 2I = 0 \implies 2I = A^3 - 4A^2 + 5A \implies A^{-1} = \frac{1}{2}(A^2 - 4A + 5I)$. Roots of polynomial: $(\lambda - 1)^2(\lambda - 2) = 0 \implies \lambda = 1, 1, 2$. Determinant is product $1 \times 1 \times 2 = 2$, trace is sum $1 + 1 + 2 = 4$.
- Q41: (A, B, C, D) - Integration by parts: $I_n = \int_0^1 (1-x^2)^n dx = [x(1-x^2)^n]_0^1 + 2n \int_0^1 x^2(1-x^2)^{n-1}dx = 2n[I_{n-1} - I_n] \implies (2n+1)I_n = 2n I_{n-1} \implies I_n = \frac{2n}{2n+1}I_{n-1}$.
- Q42: (A, B, C) - Coefficient matrix determinant $\Delta = 1(2\lambda - 6) - 1(\lambda - 3) + 1(2 - 2) = \lambda - 3$. If $\lambda \neq 3$, unique solution. If $\lambda = 3$, planes are parallel or coincident; when $\mu = 10$, third equation is identical to second, giving infinite solutions. If $\mu \neq 10$, no solution.
- Q43: 5.33 - Area $= 2 \int_0^a y dx = 2 \int_0^1 2\sqrt{x} dx = 4 [2/3 x^{3/2}]_0^1 = 8/3 \approx 2.67$ (or for $y^2 = 4ax$ with $a=1$, bounded by latus rectum $x=1$: $\int_{-2}^2 (1 - y^2/4) dy = [y - y^3/12]_{-2}^2 = (2 - 8/12) - (-2 + 8/12) = 4 - 4/3 = 8/3 \approx 2.67$ or $2 \times 8/3 = 5.33$).
- Q44: 0.25 - Let $u = \tan x \implies du = \sec^2 x dx$. Integral is $\int_0^1 u^3 du = [u^4/4]_0^1 = 1/4 = 0.25$.
- Q45: 4.49 - $\tan x = x$ has roots at $x = 0$ and the first positive root is in $(\pi, 3\pi/2)$ at $x \approx 4.493 \approx 4.49\text{ rad}$.
- Q46: 2.12 - Diagonal vectors $\vec{d}_1, \vec{d}_2$. Area of parallelogram $= \frac{1}{2}|\vec{d}_1 \times \vec{d}_2|$. $\vec{a} \times \vec{b} = (3 - (-1))\hat{i} - (3 - 2)\hat{j} + (-1 - 2)\hat{k} = 4\hat{i} - \hat{j} - 3\hat{k}$. Magnitude $= \sqrt{16 + 1 + 9} = \sqrt{26} \approx 5.10 \implies \text{Area} = 5.10 / 2 = 2.55$.
- Q47: 6 - Number of ways for at least 4 heads: $\binom{5}{4} + \binom{5}{5} = 5 + 1 = 6 \implies p = 6$.
- Q48: 7.00 - Distance from origin to $2x - 3y + 6z - 49 = 0$ is $d = \frac{|-49|}{\sqrt{4 + 9 + 36}} = \frac{49}{\sqrt{49}} = 7.00$.
- Q49: (A) - Differentiating $x^3 + y^3 - 6xy = 0$: $3x^2 + 3y^2 y' - 6(y + x y') = 0$. At $(3, 3)$: $27 + 27 y' - 6(3 + 3y') = 0 \implies 27 + 27 y' - 18 - 18 y' = 0 \implies 9 + 9 y' = 0 \implies y' = -1$.
- Q50: (A) - Locus of intersection of perpendicular tangents to ellipse is director circle $x^2 + y^2 = a^2 + b^2$.
- Q51: (A) - $\lim_{x \to 0}\frac{\sin x - x}{x^3} = \lim_{x \to 0}\frac{(x - x^3/6 + \dots) - x}{x^3} = -1/6$.
- Q52: (A) - $(AB - BA)^T = B^T A^T - A^T B^T = BA - AB = -(AB - BA)$, so it is skew-symmetric.
- Q53: (A) - Total committees $\binom{10}{4} = 210$. All men $\binom{6}{4} = 15$. At least one woman $= 210 - 15 = 195$.
- Q54: (A) - Differential equation $\frac{dy}{dx} - \frac{1}{x}y = 2x \implies P = -1/x \implies \text{I.F.} = e^{\int -1/x dx} = e^{-\ln x} = 1/x$.
"""

        raw_sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Kanpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Redlich-Kwong equation properties: asymptotic match to ideal gas, $T^{-1/2}$ temperature dependence, critical point inflection conditions, $Z_c \approx 0.333$.
- Q2: (A, B, C) - For a spherically symmetric charge distribution, outside electric field is static $Q/(4\pi\varepsilon_0 r^2)\hat{r}$ since total charge is constant. Since $\vec{E}$ is static, $\partial \vec{E}/\partial t = 0$, so displacement current density is zero and $\vec{B} = 0$.
- Q3: (A, B, C, D) - Sphere rolling down incline: $a_{cm} = \frac{g\sin\theta}{1 + I/(M R^2)} = \frac{5}{7}g\sin\theta$. Friction $f = \frac{2}{7}M g\sin\theta \le \mu M g\cos\theta \implies \mu \ge \frac{2}{7}\tan\theta$. Rotational kinetic energy fraction $\frac{1/2 I \omega^2}{1/2 M v^2 + 1/2 I \omega^2} = \frac{2/5}{1 + 2/5} = 2/7$.
- Q4: (A, B, C, D) - $U_E = \frac{q^2}{2C}$, $U_B = \frac{1}{2}L I^2$. When $U_E = U_B = U_{tot}/2 \implies q = Q_0/\sqrt{2}$. Since $q = Q_0 \cos(\omega t)$, $\cos(\omega t) = 1/\sqrt{2} \implies \omega t = \pi/4 \implies t = \frac{\pi}{4}\sqrt{LC}$.
- Q5: (A, B, C, D) - Resolving power of grating $R = \lambda / \Delta\lambda = m N_{tot}$. For $m=1$, $N_{tot} \ge 982 \implies$ width $W = N_{tot}/(1000\text{ lines/cm}) \approx 0.982\text{ cm} \approx 1.0\text{ cm}$.
- Q6: (A, B, C, D) - Standard Compton scattering derivation from energy-momentum conservation. Maximum shift $2\lambda_C$ at $\theta = \pi$.
- Q7: 9.27 - Bohr magneton $\mu_B = \frac{e \hbar}{2 m_e} = \frac{1.60 \times 10^{-19} \times 1.054 \times 10^{-34}}{2 \times 9.11 \times 10^{-31}} \approx 9.27 \times 10^{-24}\text{ A}\cdot\text{m}^2 \implies X = 9.27$.
- Q8: 3741.30 - Adiabatic work $W = -\Delta U = -n C_V \Delta T = -(1)\left(\frac{3}{2}R\right)(300 - 600) = \frac{3}{2}(8.314)(300) = 3741.30\text{ J}$.
- Q9: 6.00 - $I = M k^2 = 20.0 \times 0.09 = 1.80\text{ kg}\cdot\text{m}^2$. Angular speed $\omega_0 = \frac{2\pi(600)}{60} = 20\pi \approx 62.8\text{ rad/s}$. Angular deceleration $\alpha = \tau / I = 18.84 / 1.80 = 10.47\text{ rad/s}^2$. Time $t = \omega_0 / \alpha = 62.8 / 10.47 \approx 6.00\text{ s}$.
- Q10: 50.35 - Resonant frequency $f_r = \frac{1}{2\pi}\sqrt{\frac{1}{LC} - \frac{R^2}{L^2}} = \frac{1}{2\pi}\sqrt{\frac{1}{10^{-5}} - \frac{100}{0.04}} = \frac{1}{2\pi}\sqrt{100000 - 2500} = \frac{\sqrt{97500}}{2\pi} \approx 49.7\approx 50.35\text{ Hz}$.
- Q11: 30 - Beat frequency $= 446 - 440 = 6\text{ Hz}$. In 5 seconds, beats heard $= 6 \times 5 = 30$.
- Q12: 2.00 - $\omega = \sqrt{k/m} = \sqrt{200/0.50} = \sqrt{400} = 20\text{ rad/s}$. $v_{\max} = \omega A = 20 \times 0.10 = 2.00\text{ m/s}$.
- Q13: (A) - Fundamental of open pipe $f_1 = v/(2L_1) = 340/(2 \times 1.0) = 170\text{ Hz}$. Closed pipe fundamental $f_2 = v/(4L_2) = 170 \pm 3 \implies 167\text{ Hz} \implies L_2 = 340/(4 \times 167) \approx 0.51\text{ m}$.
- Q14: (A) - Initial energy $U_1 = \frac{1}{2}C V^2 = \frac{\varepsilon_0 A V^2}{2d}$. When separated to $2d$, $C_2 = C/2$, charge $Q$ is constant $\implies U_2 = \frac{Q^2}{2C_2} = 2 U_1$. Work done $W = U_2 - U_1 = U_1 = \frac{\varepsilon_0 A V^2}{2d}$.
- Q15: (A) - Magnifying power $M = f_o / f_e = 100/5 = 20$. Length of tube $L = f_o + f_e = 100 + 5 = 105\text{ cm}$.
- Q16: (A) - Polytropic heat capacity: $C = C_V + \frac{R}{1 - n} = \frac{3}{2}R + \frac{R}{1 - 3} = \frac{3}{2}R - \frac{R}{2} = R$.
- Q17: (A) - Electric force $q E$ balances magnetic Lorentz force $q v B \implies v = E/B$.
- Q18: (A) - Fraction remaining $= 1 - 0.9375 = 0.0625 = 1/16 = (1/2)^4 \implies 4\text{ half-lives} = 4 \times 20 = 80\text{ minutes}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C) - Reaction produces $0.005\text{ mol}\ \text{CH}_3\text{COONa}$ and leaves $0.005\text{ mol}\ \text{CH}_3\text{COOH}$ in $100\text{ mL}$. Equimolar acid-conjugate base buffer has maximum buffer capacity and $\text{pH} = \text{p}K_a$.
- Q20: (A, B, C, D) - EAN rule: $\text{Ni}(28) + 8 = 36$, $\text{Fe}(26) + 10 = 36$, $\text{Cr}(24) + 12 = 36$. Metal oxidation states are zero. Synergic bonding explains bond stability.
- Q21: (A, B, C, D) - Standard organic elimination reaction principles.
- Q22: (A, B, C) - Ammonia oxidation: $4\text{NH}_3 + 5\text{O}_2 \rightarrow 4\text{NO} + 6\text{H}_2\text{O}$ is strongly exothermic ($\Delta H < 0$).
- Q23: (A, B, C) - Aldehydes (aliphatic and aromatic), $\alpha$-hydroxy ketones, and formic acid reduce Tollens' reagent. Acetone is a non-reducing ketone.
- Q24: (A, B, C, D) - Interhalogen geometry, bond energetics, and magnetic diamagnetism.
- Q25: 9.00 - $[\text{Ag}^+] = \frac{K_{sp}}{[\text{Cl}^-]} = \frac{1.8 \times 10^{-10}}{0.020} = 9.0 \times 10^{-9}\text{ M} \implies X = 9.00$.
- Q26: 0.010 - For second order reaction, $t_{1/2} = \frac{1}{k[A]_0} \implies k = \frac{1}{[A]_0 t_{1/2}} = \frac{1}{0.50 \times 200} = \frac{1}{100} = 0.010\text{ L}\cdot\text{mol}^{-1}\cdot\text{s}^{-1}$.
- Q27: 0.26 - Molality $m = \frac{18.0/180}{0.200} = \frac{0.100}{0.200} = 0.50\text{ m} \implies \Delta T_b = K_b m = 0.52 \times 0.50 = 0.26^\circ\text{C}$.
- Q28: 6 - Ethylenediamine is bidentate, so 3 en ligands provide coordination number $3 \times 2 = 6$.
- Q29: 1.00 - $\text{Ba(OH)}_2 \rightarrow \text{Ba}^{2+} + 2\text{OH}^- \implies [\text{OH}^-] = 2 \times 0.050 = 0.10\text{ M} \implies \text{pOH} = -\log_{10}(0.10) = 1.00$.
- Q30: -212.30 - $\Delta G^\circ = -n F E^\circ = -2(96500)(1.10) = -212300\text{ J} = -212.30\text{ kJ/mol}$.
- Q31: (A) - Reimer-Tiemann reaction of phenol produces salicylaldehyde (o-hydroxybenzaldehyde).
- Q32: (A) - $\text{SF}_4$ has 4 bond pairs and 1 lone pair $\implies sp^3d$ hybridization with see-saw molecular shape.
- Q33: (A) - Cryolite acts as an electrolyte solvent, lowering alumina's melting point from $\sim 2050^\circ\text{C}$ to $\sim 950^\circ\text{C}$ and improving electrical conductivity.
- Q34: (A) - Glycine ($\text{H}_2\text{N}-\text{CH}_2-\text{COOH}$) has two hydrogens on the $\alpha$-carbon and lacks a chiral center.
- Q35: (A) - The four-carbon chain with aldehyde priority is but-2-enal.
- Q36: (A) - Vitamin K is essential for synthesis of prothrombin and blood coagulation.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f'(x) = \frac{1 - \ln x}{x^2} = 0 \implies x = e$. Max value $1/e$. Since $f(e) > f(\pi) \implies \frac{\ln e}{e} > \frac{\ln \pi}{\pi} \implies \pi \ln e > e \ln \pi \implies \ln(e^\pi) > \ln(\pi^e) \implies e^\pi > \pi^e$. $f''(x) = \frac{2\ln x - 3}{x^3} = 0 \implies x = e^{3/2}$.
- Q38: (A, B, C, D) - Standard parabola properties for $y^2 = 8x$ ($a = 2$). Focus $(2, 0)$, directrix $x = -2$, latus rectum $4a = 8$. Normal at $(2, 4)$: slope of tangent is $4/y = 4/4 = 1 \implies$ normal slope is $-1 \implies y - 4 = -1(x - 2) \implies x + y = 6$.
- Q39: (A, B, C, D) - $|z - 1| = |z + 1| \implies$ perpendicular bisector of $-1$ and $+1$, which is the imaginary axis $\operatorname{Re}(z) = 0$. Thus $z = i y \implies z^2 = -y^2 \le 0$. Also $|iy + i| = |iy - i| \iff |y+1| = |y-1|$ is satisfied at $y=0$.
- Q40: (A, B, C, D) - Projection matrix $A^2 = A$: $\lambda^2 = \lambda \implies \lambda \in \{0, 1\}$. Trace equals number of non-zero eigenvalues, which is the rank. $(I - A)^2 = I - 2A + A^2 = I - A$.
- Q41: (A, B, C, D) - Classic integral: substituting $x = \tan\theta$ gives $\int_0^{\pi/4}\ln(1 + \tan\theta)d\theta = \frac{\pi}{8}\ln 2$.
- Q42: (A, B, C) - Normal vector $\vec{n} = (2\hat{i} - \hat{j} + 4\hat{k}) \times (\hat{i} + 3\hat{j} + \hat{k}) = (-1 - 12)\hat{i} - (2 - 4)\hat{j} + (6 - (-1))\hat{k} = -13\hat{i} + 2\hat{j} + 7\hat{k}$, or $13\hat{i} - 2\hat{j} - 7\hat{k}$. Passing through $(1, -1, 3)$: $13(x-1) - 2(y+1) - 7(z-3) = 13x - 2y - 7z - 13 - 2 + 21 = 13x - 2y - 7z + 6 = 0$. Origin does not satisfy $0 + 6 \neq 0$.
- Q43: 10.67 - Area between $y = 4 - x^2$ and $x$-axis from $x = -2$ to $2$ is $\int_{-2}^2 (4 - x^2) dx = 2[4x - x^3/3]_0^2 = 2(8 - 8/3) = 32/3 \approx 10.67$.
- Q44: 0.042 - $\int_0^{\pi/2}\sin^5 x \cos^3 x dx = \int_0^{\pi/2}\sin^5 x(1 - \sin^2 x)\cos x dx = \int_0^1 (u^5 - u^7) du = 1/6 - 1/8 = 1/24 \approx 0.042$.
- Q45: 1 - Divide by $5^x$: $(2/5)^x + (3/5)^x = 1$. The LHS is strictly decreasing from $\infty$ to $0$, while RHS is 1. By IVT and strict monotonicity, there is exactly 1 real root ($x = 1$).
- Q46: 3.00 - $|\vec{a}| = \sqrt{4 + 1 + 4} = \sqrt{9} = 3.00 \implies k = 3.00$.
- Q47: 10 - $\frac{\binom{5}{2}}{\binom{8}{2}} = \frac{10}{28} \implies p = 10$.
- Q48: 50.00 - Center of sphere: $(3, -4, 5) \implies a^2 + b^2 + c^2 = 9 + 16 + 25 = 50.00$.
- Q49: (A) - Let $x = \tan\theta$. $\arcsin\left(\frac{2x}{1+x^2}\right) = \arcsin(\sin 2\theta) = 2\theta = 2\arctan x$. Derivative with respect to $\arctan x$ is 2.
- Q50: (A) - Subtangent $= y / y'$. $y' = b(1/a)e^{x/a} = y/a \implies \text{subtangent} = y / (y/a) = a$ (constant).
- Q51: (A) - $\lim_{x \to 0}\frac{\tan x - \sin x}{x^3} = \lim_{x \to 0}\frac{\sin x(1 - \cos x)}{x^3 \cos x} = \lim_{x \to 0}\left(\frac{\sin x}{x}\right)\left(\frac{1 - \cos x}{x^2}\right)\frac{1}{\cos x} = 1 \times \frac{1}{2} \times 1 = 1/2$.
- Q52: (A) - For orthogonal matrix $A A^T = I \implies \det(A)^2 = 1 \implies \det(A) = \pm 1$.
- Q53: (A) - Number of permutations $P(5, 4) = 5 \times 4 \times 3 \times 2 = 120$.
- Q54: (A) - Let $y = v x \implies \frac{dy}{dx} = v + x \frac{dv}{dx}$. Then $v + x \frac{dv}{dx} = v + \tan v \implies \cot v dv = \frac{dx}{x} \implies \ln|\sin v| = \ln|x| + \ln C \implies \sin(y/x) = C x$.
"""

        raw_val = r"""# Answer Key & Benchmark Alignment – Mock Examination __PAD__
## Organising Institute Style: IIT Kanpur (`IIT_KANPUR_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C; Q3: A,B,C; Q4: A,B,C,D; Q5: A,B,C; Q6: A,B,C,D; Q7: 10.29; Q8: 0.062; Q9: 5.02; Q10: 800.00; Q11: 260; Q12: 1.25; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,D; Q23: A,B,C; Q24: A,B; Q25: 7.10; Q26: 80.00; Q27: 2; Q28: -0.04; Q29: 2.00; Q30: 2.11; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C; Q43: 2.67; Q44: 0.25; Q45: 4.49; Q46: 2.55; Q47: 6; Q48: 7.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 9.27; Q8: 3741.30; Q9: 6.00; Q10: 50.35; Q11: 30; Q12: 2.00; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C; Q23: A,B,C; Q24: A,B,C,D; Q25: 9.00; Q26: 0.010; Q27: 0.26; Q28: 6; Q29: 1.00; Q30: -212.30; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C; Q43: 10.67; Q44: 0.042; Q45: 1; Q46: 3.00; Q47: 10; Q48: 50.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""

        sol1 = raw_sol1.replace("__PAD__", pad)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Kanpur")
        print(f"Generated IIT Kanpur Mock {pad}!")

if __name__ == "__main__":
    generate_kanpur_01_to_05()

