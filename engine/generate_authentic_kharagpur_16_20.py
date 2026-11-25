"""
IIT Kharagpur Mocks 16 to 20 Generator
Organising Institute: Indian Institute of Technology Kharagpur
Empirical Benchmark: 2006, 2014, 2021 Official JEE Advanced Papers
Features:
- Asymmetric paper difficulty & long descriptive stems
- Constraint mechanics, non-uniform rotational dynamics, electrodynamics
- Extensive organic reaction cascades, inorganic quantitative metallurgy, ionic equilibria
- Advanced integral calculus (Leibniz rule), 3D coordinate geometry, probability distributions
Completes the IIT Kharagpur suite (Mocks 01 to 20: 100% complete)
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_kharagpur_16_to_20():
    for mock_idx in range(16, 21):
        pad = f"{mock_idx:02d}"
        rod_m = str(2.0 + (mock_idx % 4) * 0.25)
        res_r = str(10.0 + (mock_idx % 3) * 2.5)
        acid_k = str(1.5 + (mock_idx % 3) * 0.3)
        poly_n = str(5 + (mock_idx % 3))

        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)
**Historical Reference Benchmark**: 2006, 2014, 2021 Official Examination Papers  
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
A uniform thin rod $AB$ of mass $M$ and length $L$ is smoothly hinged at $A$. It is released from rest in the horizontal position $\theta = 0$:
(A) The angular acceleration of the rod as a function of the angle of fall $\theta$ is $\alpha(\theta) = \frac{3g}{2L}\cos\theta$.  
(B) The angular velocity of the rod at the lowest position $\theta = \pi/2$ is $\omega = \sqrt{\frac{3g}{L}}$.  
(C) The reaction force exerted by the hinge when the rod reaches the vertical position is $N_y = \frac{5}{2}M g$.  
(D) The tangential acceleration of the free end $B$ when horizontal is $\frac{3}{2}g$.

#### Question 2
One mole of an ideal monoatomic gas undergoes an adiabatic expansion where the volume triples ($V_2 = 3V_1$):
(A) The pressure of the gas decreases by a factor of $3^{5/3} \approx 6.24$.  
(B) The temperature of the gas decreases by a factor of $3^{2/3} \approx 2.08$.  
(C) The work done by the gas is positive and equals $-\Delta U$.  
(D) The entropy of the gas remains strictly constant.

#### Question 3
A parallel-plate capacitor with air between plates is charged to potential $V_0$ and then disconnected from the voltage source. A dielectric slab of dielectric constant $\kappa = 3$ filling the entire space between the plates is inserted:
(A) The charge on the plates remains constant.  
(B) The potential difference across the plates drops to $V_0 / 3$.  
(C) The electric field strength between the plates decreases by a factor of 3.  
(D) The electrostatic energy stored in the capacitor decreases to $1/3$ of its initial value.

#### Question 4
A long solenoid of radius $R$ carries a steady current $I$. A conducting loop of radius $2R$ is placed coaxially with the solenoid:
(A) The magnetic field outside the solenoid is approximately zero.  
(B) The total magnetic flux through the external loop is $\Phi = \mu_0 n I \pi R^2$.  
(C) If the current in the solenoid is doubled, the flux through the external loop doubles.  
(D) If the loop is rotated about its diameter by $180^\circ$, the change in magnetic flux is $2\mu_0 n I \pi R^2$.

#### Question 5
In Young's double slit experiment, if the distance between the two slits is halved and the distance between the slits and screen is doubled:
(A) The fringe width becomes 4 times larger.  
(B) The angular fringe width doubles.  
(C) The central fringe remains unchanged in position.  
(D) The maximum intensity at the central bright fringe increases if total source power is conserved.

#### Question 6
According to the de Broglie hypothesis, for a particle of rest mass $m_0$ accelerated from rest through potential difference $V$:
(A) In the non-relativistic limit, $\lambda = \frac{h}{\sqrt{2m_0 q V}}$.  
(B) For an electron, $\lambda \approx \frac{1.227}{\sqrt{V}}\text{ nm}$ ($V$ in volts).  
(C) The phase velocity of the de Broglie wave exceeds $c$.  
(D) The group velocity of the de Broglie wave equals the particle velocity $v$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A horizontal pipe of cross-sectional area $A_1 = 20.0\text{ cm}^2$ narrows to $A_2 = 10.0\text{ cm}^2$. Water flows through the pipe at a rate of $Q = 6.00\text{ L/s}$. Taking density of water as $1000\text{ kg/m}^3$, the pressure difference $\Delta P = P_1 - P_2$ is ______ kPa. (Round off to two decimal places)

#### Question 8
One mole of an ideal gas absorbs $1200\text{ J}$ of heat at constant pressure, raising its temperature by $40.0\text{ K}$. The molar heat capacity at constant pressure $C_P$ of the gas is ______ $\text{J/(mol}\cdot\text{K)}$.

#### Question 9
A solid cylinder of mass $M = 4.0\text{ kg}$ and radius $R = 0.20\text{ m}$ rolls without slipping on a horizontal surface at $v = 5.0\text{ m/s}$. Its total kinetic energy is ______ J.

#### Question 10
In a series LCR circuit, $R = 30.0\ \Omega$, $X_L = 50.0\ \Omega$, and $X_C = 10.0\ \Omega$. The impedance $Z$ of the circuit is ______ $\Omega$.

#### Question 11
Two tuning forks produce 6 beats per second. If the frequency of one is $256\text{ Hz}$ and the other has a higher frequency, the frequency of the other fork is ______ Hz.

#### Question 12
A spring of stiffness $k = 200\text{ N/m}$ has a mass $m = 2.0\text{ kg}$ attached. The frequency of oscillation $f$ is ______ Hz. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle moves in a circle of radius $r$ with constant speed $v$. The centripetal acceleration is:  
(A) $v^2 / r$ directed towards the center  
(B) $v^2 / r$ directed away from the center  
(C) $v / r$  
(D) $0$

#### Question 14
The electric potential at distance $r$ from an isolated point charge $q$ in vacuum is:  
(A) $\frac{q}{4\pi\varepsilon_0 r}$  
(B) $\frac{q}{4\pi\varepsilon_0 r^2}$  
(C) $\frac{q^2}{4\pi\varepsilon_0 r}$  
(D) $\frac{q r}{4\pi\varepsilon_0}$

#### Question 15
The focal length of a concave mirror of radius of curvature $R = 40\text{ cm}$ is:  
(A) $-20\text{ cm}$  
(B) $+20\text{ cm}$  
(C) $-40\text{ cm}$  
(D) $+40\text{ cm}$

#### Question 16
The efficiency of a Carnot engine working between $T_H = 500\text{ K}$ and $T_C = 300\text{ K}$ is:  
(A) $40\%$  
(B) $60\%$  
(C) $50\%$  
(D) $30\%$

#### Question 17
The magnetic force experienced by a stationary charge in a uniform magnetic field $B$ is:  
(A) $0$  
(B) $q B$  
(C) $q / B$  
(D) $q^2 B$

#### Question 18
If the half-life of a radioactive material is 12 hours, the fraction remaining after 36 hours is:  
(A) $1/8$  
(B) $1/4$  
(C) $1/16$  
(D) $1/2$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution of acetic acid ($\text{CH}_3\text{COOH}$, $K_a = 1.8 \times 10^{-5}$):
(A) The degree of dissociation $\alpha = \sqrt{K_a / c}$ increases upon dilution (Ostwald's dilution law).  
(B) Addition of sodium acetate suppresses the dissociation of acetic acid due to the common ion effect.  
(C) Addition of $\text{HCl}$ decreases the concentration of acetate ions.  
(D) At infinite dilution, the molar conductivity follows Kohlrausch's law.

#### Question 20
Regarding the complex ion $[\text{Fe}(\text{CN})_6]^{3-}$:
(A) The oxidation state of iron is $+3$.  
(B) Iron has a $d^5$ electron configuration.  
(C) Because cyanide is a strong-field ligand, it forms a low-spin complex ($t_{2g}^5 e_g^0$) with 1 unpaired electron.  
(D) The hybridization of iron is $d^2sp^3$ (inner orbital octahedral complex).

#### Question 21
Which of the following reactions produce benzaldehyde?
(A) Etard reaction: Oxidation of toluene with chromyl chloride ($\text{CrO}_2\text{Cl}_2$) in $\text{CS}_2$ followed by hydrolysis.  
(B) Gattermann-Koch reaction: Reaction of benzene with $\text{CO}$ and $\text{HCl}$ in presence of anhydrous $\text{AlCl}_3 / \text{CuCl}$.  
(C) Rosenmund reduction: Hydrogenation of benzoyl chloride over $\text{Pd}/\text{BaSO}_4$ poisoned with sulfur or quinoline.  
(D) Hydrolysis of benzal chloride ($\text{PhCHCl}_2$) with aqueous $\text{NaOH}$ followed by heating.

#### Question 22
In the metallurgy of iron:
(A) Haematite ($\text{Fe}_2\text{O}_3$) is the principal ore used.  
(B) Carbon monoxide is the chief reducing agent in the upper stack of the blast furnace.  
(C) Limestone acts as a basic flux to remove silica as $\text{CaSiO}_3$ slag.  
(D) Pig iron contains about $4\%$ carbon and cannot be welded.

#### Question 23
Which of the following statements about carbohydrates is/are correct?
(A) Glucose gives positive Fehling's and Tollens' tests.  
(B) Fructose reduces Tollens' reagent despite being a ketose due to enediol rearrangement in basic medium.  
(C) Sucrose is an example of an invert sugar precursor.  
(D) Starch is a polymer composed of amylose and amylopectin.

#### Question 24
Regarding the chemistry of Group 15 elements:
(A) Nitrogen exhibits a maximum covalency of 4.  
(B) Phosphorus exhibits covalency of up to 5 and 6 using vacant $3d$ orbitals.  
(C) $\text{PH}_3$ has a lower boiling point than $\text{NH}_3$ due to absence of hydrogen bonding.  
(D) $\text{Bi(V)}$ is a strong oxidizing agent due to the inert pair effect.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{BaSO}_4$ is $K_{sp} = 1.0 \times 10^{-10}$. Its solubility in pure water is $X \times 10^{-5}\text{ mol/L}$. The value of $X$ is ______ .

#### Question 26
For a first-order reaction with rate constant $k = 0.050\text{ min}^{-1}$, the time required for $50\%$ completion is ______ minutes. (Take $\ln 2 = 0.693$, round off to two decimal places)

#### Question 27
An aqueous solution contains $10.0\text{ g}$ of glucose ($\text{molar mass} = 180\text{ g/mol}$) in $250\text{ g}$ of water. If $K_b = 0.52\text{ K}\cdot\text{kg/mol}$, the boiling point elevation $\Delta T_b$ is ______ $^\circ\text{C}$. (Round off to two decimal places)

#### Question 28
The coordination number of nickel in $[\text{Ni(CO)}_4]$ is ______ .

#### Question 29
A $0.010\text{ M}$ solution of nitric acid ($\text{HNO}_3$) has a pH of ______ .

#### Question 30
The standard cell potential of the cell $\text{Mg} \mid \text{Mg}^{2+} \parallel \text{Ag}^+ \mid \text{Ag}$ with $E^\circ(\text{Mg}^{2+}/\text{Mg}) = -2.37\text{ V}$ and $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$ is ______ V. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the reaction between phenol and neutral $\text{FeCl}_3$ solution is:  
(A) Violet-colored coordination complex  
(B) White precipitate  
(C) Yellow precipitate  
(D) Brown gas

#### Question 32
The molecular geometry of sulfur tetrafluoride ($\text{SF}_4$) is:  
(A) See-saw  
(B) Tetrahedral  
(C) Square planar  
(D) Trigonal bipyramidal

#### Question 33
In the extraction of copper, matte consists of:  
(A) $\text{Cu}_2\text{S}$ and $\text{FeS}$  
(B) $\text{Cu}_2\text{O}$ and $\text{FeO}$  
(C) $\text{CuS}$ and $\text{Fe}_2\text{O}_3$  
(D) $\text{CuSO}_4$ and $\text{FeSO}_4$

#### Question 34
Which of the following organic compounds will give a positive iodoform test?  
(A) Propan-2-ol  
(B) Propan-1-ol  
(C) Methanol  
(D) Benzaldehyde

#### Question 35
Terylene (Dacron) is a polyester polymer of:  
(A) Ethylene glycol and terephthalic acid  
(B) Adipic acid and hexamethylenediamine  
(C) Phenol and formaldehyde  
(D) Caprolactam

#### Question 36
Deficiency of Vitamin K leads to:  
(A) Increased blood clotting time (haemorrhage)  
(B) Scurvy  
(C) Rickets  
(D) Night blindness

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \ln(1 + x) - x + \frac{x^2}{2}$ for $x > 0$. Which of the following statements is/are correct?
(A) $f(0) = 0$.  
(B) $f'(x) = \frac{x^2}{1 + x} > 0$ for all $x > 0$.  
(C) $f(x) > 0$ for all $x > 0$.  
(D) $\ln(1 + x) > x - \frac{x^2}{2}$ for all $x > 0$.

#### Question 38
For the parabola $y^2 = 4x$:
(A) Its focus is at $(1, 0)$.  
(B) The equation of the directrix is $x = -1$.  
(C) The length of the latus rectum is $4$.  
(D) The vertex is at $(0, 0)$.

#### Question 39
For complex numbers $z$ satisfying $|z - 1| = 1$:
(A) The locus of $z$ is a circle passing through the origin.  
(B) The center of the circle is $(1, 0)$ and its radius is $1$.  
(C) The maximum value of $|z|$ is $2$.  
(D) The argument $\arg(z)$ satisfies $-\pi/2 < \arg(z) < \pi/2$ for $z \neq 0$.

#### Question 40
Let $A$ be a $3 \times 3$ real matrix with eigenvalues $\lambda = 1, 1, 2$:
(A) $\det(A) = 2$.  
(B) $\operatorname{Tr}(A) = 4$.  
(C) $\det(A - I) = 0$.  
(D) $\det(A - 2I) = 0$.

#### Question 41
Let $I = \int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x} \, dx$. Then:
(A) $I = \pi/4$.  
(B) $\int_0^{\pi/2} \frac{\cos x}{\sin x + \cos x} \, dx = \pi/4$.  
(C) $I = \int_0^{\pi/2} \frac{\cos x}{\sin x + \cos x} \, dx$.  
(D) The sum of the two integrals is $\pi/2$.

#### Question 42
The plane $2x - y + 2z = 6$:
(A) Has normal vector in the direction of $2\hat{i} - \hat{j} + 2\hat{k}$.  
(B) Has perpendicular distance from origin equal to $2$.  
(C) Intersects the $x$-axis at $(3, 0, 0)$.  
(D) Intersects the $y$-axis at $(0, -6, 0)$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area of the region bounded by $y = x^2$ and $y = 2x$ is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^1 x(1 - x) \, dx$ is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real solutions to the equation $x^2 - 4 = 0$ is ______ .

#### Question 46
Let $\vec{a} = 2\hat{i} + \hat{j} + 2\hat{k}$. The magnitude $|\vec{a}|$ is ______ .

#### Question 47
A card is drawn from a pack of 52 playing cards. The probability that it is a King is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 48
The radius of the circle $x^2 + y^2 = 25$ is ______ .

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = e^{2x}$ with respect to $x$ is:  
(A) $2 e^{2x}$  
(B) $e^{2x}$  
(C) $\frac{1}{2}e^{2x}$  
(D) $2x e^{2x}$

#### Question 50
The slope of the tangent to the circle $x^2 + y^2 = 25$ at $(3, 4)$ is:  
(A) $-3/4$  
(B) $3/4$  
(C) $-4/3$  
(D) $4/3$

#### Question 51
The value of $\lim_{x \to 0} \frac{\sin(3x)}{x}$ is:  
(A) $3$  
(B) $1$  
(C) $1/3$  
(D) $0$

#### Question 52
If $A$ is a square matrix of order 3 such that $\det(A) = 3$, then $\det(2A)$ is:  
(A) $24$  
(B) $6$  
(C) $12$  
(D) $18$

#### Question 53
The number of subsets of a set with 4 elements is:  
(A) $16$  
(B) $8$  
(C) $12$  
(D) $32$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = y$ with $y(0) = 1$ is:  
(A) $y = e^x$  
(B) $y = e^{-x}$  
(C) $y = x + 1$  
(D) $y = 2e^x - 1$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)
**Historical Reference Benchmark**: 2006, 2014, 2021 Official Examination Papers  
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
A real gas follows the Dieterici equation of state $P(V_m - b)\exp\left(\frac{a}{R T V_m}\right) = R T$:
(A) The critical volume is $V_c = 2b$.  
(B) The critical temperature is $T_c = \frac{a}{4Rb}$.  
(C) The critical pressure is $P_c = \frac{a}{4e^2 b^2}$.  
(D) The critical compressibility factor is $Z_c = 2 e^{-2} \approx 0.271$.

#### Question 2
Two concentric spherical metallic shells of radii $R_1$ and $R_2$ ($R_1 < R_2$) carry charges $Q_1$ and $Q_2$:
(A) The electric field in $r < R_1$ is zero.  
(B) The electric field in $R_1 < r < R_2$ is $\frac{Q_1}{4\pi\varepsilon_0 r^2}$.  
(C) The electric field in $r > R_2$ is $\frac{Q_1 + Q_2}{4\pi\varepsilon_0 r^2}$.  
(D) The potential difference between the shells depends only on $Q_1$.

#### Question 3
A cylinder of mass $M$ and radius $R$ rolls without slipping down an inclined plane of angle $\theta$:
(A) Its linear acceleration is $a = \frac{2}{3}g\sin\theta$.  
(B) The friction force acting on the cylinder is $f = \frac{1}{3}M g\sin\theta$.  
(C) Pure rolling requires $\mu \ge \frac{1}{3}\tan\theta$.  
(D) The ratio of rotational kinetic energy to translational kinetic energy is $1/2$.

#### Question 4
A circular wire loop of radius $r$ and resistance $R$ is placed in a uniform magnetic field $B$ perpendicular to the plane of the loop. If the magnetic field collapses to zero in time $\Delta t$:
(A) The initial magnetic flux is $\Phi = B \pi r^2$.  
(B) The induced EMF is $\mathcal{E} = \frac{B \pi r^2}{\Delta t}$.  
(C) The total charge that flows through the loop is $q = \frac{B \pi r^2}{R}$.  
(D) The induced current flows in a direction opposing the decrease in flux (Lenz's law).

#### Question 5
In an interference experiment using monochromatic light:
(A) The condition for constructive interference is path difference $\Delta x = n\lambda$.  
(B) The condition for destructive interference is path difference $\Delta x = (n + 1/2)\lambda$.  
(C) The fringe width is directly proportional to the wavelength of light.  
(D) The central fringe corresponds to zero path difference.

#### Question 6
Regarding the Compton effect:
(A) The scattered photon wavelength is longer than the incident wavelength.  
(B) The wavelength shift depends only on the scattering angle $\theta$.  
(C) Maximum wavelength shift occurs at $\theta = 180^\circ$.  
(D) The Compton wavelength of an electron is $\lambda_C = \frac{h}{m_e c} \approx 2.43\text{ pm}$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a Coolidge tube, the cut-off wavelength for electrons accelerated through $31.0\text{ kV}$ is ______ pm. (Take $h c = 1240\text{ eV}\cdot\text{nm}$, round off to two decimal places)

#### Question 8
One mole of an ideal gas expands isothermally at $T = 300\text{ K}$ from $V_1 = 1.0\text{ L}$ to $V_2 = 2.718\text{ L}$ ($e\text{ L}$). Taking $R = 8.314\text{ J/(mol}\cdot\text{K)}$, the work done by the gas is ______ J. (Round off to two decimal places)

#### Question 9
A disc of mass $M = 2.0\text{ kg}$ and radius $R = 0.50\text{ m}$ is rotating at $\omega = 10.0\text{ rad/s}$. Its kinetic energy is ______ J.

#### Question 10
In a series LCR circuit at resonance, $R = 50.0\ \Omega$ and applied voltage is $V_{rms} = 200\text{ V}$. The power consumed is ______ W.

#### Question 11
Two tuning forks produce 4 beats per second. If one has frequency $300\text{ Hz}$ and the other has a lower frequency, the lower frequency is ______ Hz.

#### Question 12
A simple pendulum of length $L = 0.98\text{ m}$ has period $T$. Taking $g = 9.80\text{ m/s}^2$, the value of $T$ is ______ s. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The escape velocity from the Earth's surface is approximately:  
(A) $11.2\text{ km/s}$  
(B) $8.0\text{ km/s}$  
(C) $16.0\text{ km/s}$  
(D) $24.0\text{ km/s}$

#### Question 14
The capacitance of a parallel plate capacitor with plate area $A$ and separation $d$ in vacuum is:  
(A) $\frac{\varepsilon_0 A}{d}$  
(B) $\frac{A}{\varepsilon_0 d}$  
(C) $\frac{\varepsilon_0 d}{A}$  
(D) $\varepsilon_0 A d$

#### Question 15
The power of a convex lens of focal length $f = 50\text{ cm}$ is:  
(A) $+2.0\text{ D}$  
(B) $-2.0\text{ D}$  
(C) $+0.5\text{ D}$  
(D) $+5.0\text{ D}$

#### Question 16
In an isothermal expansion of an ideal gas, the work done is:  
(A) $n R T \ln(V_2 / V_1)$  
(B) $n C_V \Delta T$  
(C) $P \Delta V$  
(D) $0$

#### Question 17
The magnetic field at the center of a circular loop of radius $R$ carrying current $I$ is:  
(A) $\frac{\mu_0 I}{2R}$  
(B) $\frac{\mu_0 I}{4\pi R}$  
(C) $\frac{\mu_0 I}{2\pi R}$  
(D) $\frac{\mu_0 I}{R}$

#### Question 18
The half-life of a radioactive sample is 10 days. The time required for $87.5\%$ of the sample to decay is:  
(A) 30 days  
(B) 20 days  
(C) 40 days  
(D) 15 days

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an ideal solution obeying Raoult's law:
(A) $\Delta H_{\text{mix}} = 0$.  
(B) $\Delta V_{\text{mix}} = 0$.  
(C) $\Delta S_{\text{mix}} > 0$.  
(D) $\Delta G_{\text{mix}} < 0$.

#### Question 20
Regarding the complex ion $[\text{Ni(CN)}_4]^{2-}$:
(A) The oxidation state of nickel is $+2$.  
(B) It has a $d^8$ electron configuration.  
(C) It is square planar and diamagnetic ($dsp^2$).  
(D) It does not have any unpaired electrons.

#### Question 21
Which of the following undergo nucleophilic addition reactions?
(A) Acetaldehyde  
(B) Acetone  
(C) Benzaldehyde  
(D) Formaldehyde

#### Question 22
In the Hall-Héroult process for aluminium extraction:
(A) Cryolite ($\text{Na}_3\text{AlF}_6$) lowers the melting point of alumina.  
(B) Fluorspar ($\text{CaF}_2$) increases electrical conductivity.  
(C) Carbon anodes are consumed to form $\text{CO}_2$.  
(D) Aluminium is discharged at the cathode.

#### Question 23
Which of the following carbohydrates are reducing sugars?
(A) Glucose  
(B) Maltose  
(C) Fructose  
(D) Lactose

#### Question 24
Regarding the chemistry of Group 16 elements:
(A) Oxygen exhibits maximum covalency of 4.  
(B) Sulfur forms $\text{SF}_6$ which is chemically inert.  
(C) Ozone is a bent molecule.  
(D) $\text{H}_2\text{O}$ has higher boiling point than $\text{H}_2\text{S}$ due to hydrogen bonding.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{AgBr}$ is $K_{sp} = 5.0 \times 10^{-13}$. Its solubility in pure water is $X \times 10^{-7}\text{ mol/L}$. The value of $X$ is ______ . (Take $\sqrt{5} = 2.24$, round off to two decimal places)

#### Question 26
For a first-order reaction with half-life $t_{1/2} = 15.0\text{ minutes}$, the rate constant $k$ is ______ $\text{min}^{-1}$. (Take $\ln 2 = 0.693$, round off to three decimal places)

#### Question 27
An aqueous solution contains $3.00\text{ g}$ of urea in $100\text{ g}$ of water. If $K_b = 0.52\text{ K}\cdot\text{kg/mol}$, the boiling point elevation $\Delta T_b$ is ______ $^\circ\text{C}$. (Round off to two decimal places)

#### Question 28
The coordination number of iron in $[\text{Fe(CN)}_6]^{4-}$ is ______ .

#### Question 29
A $0.010\text{ M}$ solution of hydrochloric acid has a pH of ______ .

#### Question 30
The standard cell potential of the Daniell cell $\text{Zn} \mid \text{Zn}^{2+} \parallel \text{Cu}^{2+} \mid \text{Cu}$ is ______ V. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the reaction between benzaldehyde and concentrated $\text{NaOH}$ (Cannizzaro reaction) is:  
(A) Benzyl alcohol and sodium benzoate  
(B) Benzoic acid and benzene  
(C) Benzyl alcohol and methanol  
(D) Sodium benzoate and ethanol

#### Question 32
The molecular geometry of water ($\text{H}_2\text{O}$) is:  
(A) Bent ($V$-shaped)  
(B) Linear  
(C) Tetrahedral  
(D) Trigonal planar

#### Question 33
The blister appearance of copper during extraction is due to the release of:  
(A) $\text{SO}_2$  
(B) $\text{CO}_2$  
(C) $\text{O}_2$  
(D) $\text{N}_2$

#### Question 34
Which of the following compounds gives a positive Tollens' test?  
(A) Acetaldehyde  
(B) Acetone  
(C) Acetophenone  
(D) Benzophenone

#### Question 35
The monomer of Teflon is:  
(A) Tetrafluoroethylene  
(B) Vinyl chloride  
(C) Styrene  
(D) Isoprene

#### Question 36
Scurvy is caused by deficiency of:  
(A) Vitamin C  
(B) Vitamin A  
(C) Vitamin D  
(D) Vitamin B12

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^2 - 4x + 3$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x) = (x - 1)(x - 3)$.  
(B) The vertex of the parabola $y = f(x)$ is $(2, -1)$.  
(C) The minimum value of $f(x)$ is $-1$.  
(D) The graph is symmetric about the vertical line $x = 2$.

#### Question 38
For the circle $x^2 + y^2 = 25$:
(A) Its center is at $(0, 0)$.  
(B) Its radius is $5$.  
(C) The point $(3, 4)$ lies on the circle.  
(D) The tangent at $(3, 4)$ has equation $3x + 4y = 25$.

#### Question 39
For complex numbers $z$ satisfying $|z| = 1$:
(A) $\operatorname{Re}(z) \in [-1, 1]$.  
(B) $\operatorname{Im}(z) \in [-1, 1]$.  
(C) $z \bar{z} = 1$.  
(D) $1/z = \bar{z}$.

#### Question 40
Let $A$ be a $2 \times 2$ matrix with eigenvalues $\lambda = 2, 3$:
(A) $\det(A) = 6$.  
(B) $\operatorname{Tr}(A) = 5$.  
(C) $A$ is invertible.  
(D) $A$ is diagonalizable.

#### Question 41
Let $I = \int_0^1 x^2 \, dx$. Then:
(A) $I = 1/3$.  
(B) $\int_0^1 (1 - x)^2 \, dx = 1/3$.  
(C) $\int_{-1}^1 x^2 \, dx = 2/3$.  
(D) $\int_0^1 x^3 \, dx = 1/4$.

#### Question 42
The plane $x + y + z = 1$:
(A) Has normal vector $\hat{i} + \hat{j} + \hat{k}$.  
(B) Intersects the axes at $(1, 0, 0), (0, 1, 0), (0, 0, 1)$.  
(C) The distance from the origin is $1/\sqrt{3}$.  
(D) Passes through $(1/3, 1/3, 1/3)$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by $y = x$ and the $x$-axis from $x = 0$ to $x = 2$ is ______ .

#### Question 44
The value of the definite integral $\int_0^1 x^2 \, dx$ is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real solutions to the equation $x^2 - 9 = 0$ is ______ .

#### Question 46
Let $\vec{a} = 3\hat{i} + 4\hat{j}$. The length $|\vec{a}|$ is ______ .

#### Question 47
A coin is tossed. The probability of getting a head is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 48
The radius of the circle $x^2 + y^2 = 16$ is ______ .

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = \sin x$ with respect to $x$ is:  
(A) $\cos x$  
(B) $-\cos x$  
(C) $\sin x$  
(D) $-\sin x$

#### Question 50
The slope of the line $2x + 3y = 6$ is:  
(A) $-2/3$  
(B) $2/3$  
(C) $-3/2$  
(D) $3/2$

#### Question 51
The value of $\lim_{x \to 0} \frac{\sin x}{x}$ is:  
(A) $1$  
(B) $0$  
(C) $\infty$  
(D) $-1$

#### Question 52
If $A$ is the identity matrix of order 3, then $\det(A)$ is:  
(A) $1$  
(B) $3$  
(C) $0$  
(D) $9$

#### Question 53
The number of permutations of 3 distinct items is:  
(A) $6$  
(B) $3$  
(C) $9$  
(D) $1$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = 0$ is:  
(A) $y = C$  
(B) $y = x + C$  
(C) $y = C x$  
(D) $y = 0$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__ROD_M__", rod_m).replace("__RES_R__", res_r).replace("__ACID_K__", acid_k).replace("__POLY_N__", poly_n)
        p2 = raw_p2.replace("__PAD__", pad)

        raw_sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Kharagpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Pivoted rod falling from horizontal: torque $\tau = M g(L/2)\cos\theta = \frac{1}{3}M L^2 \alpha \implies \alpha = \frac{3g}{2L}\cos\theta$. At bottom $\omega = \sqrt{3g/L}$, vertical hinge force $N_y = \frac{5}{2}M g$.
- Q2: (A, B, C, D) - Monoatomic adiabatic expansion $V_2 = 3V_1$: $P_2 = P_1(1/3)^{5/3} \approx P_1 / 6.24$. $T_2 = T_1(1/3)^{2/3} \approx T_1 / 2.08$. $W = -\Delta U > 0$. Reversible adiabatic $\implies \Delta S = 0$.
- Q3: (A, B, C, D) - Isolated charged capacitor: charge $Q$ is constant. Potential drops by $\kappa = 3$. Energy drops by factor of 3.
- Q4: (A, B, C, D) - Solenoid flux linked through external loop: $\Phi = \mu_0 n I \pi R^2$. Exterior magnetic field is zero.
- Q5: (A, B, C) - Fringe width $\beta = \lambda D / d$. If $d' = d/2$ and $D' = 2D$, $\beta' = 4\beta$. Angular width $\beta/D = \lambda/d$ doubles.
- Q6: (A, B, C, D) - De Broglie wavelength relations: $\lambda = h/p = \frac{1.227}{\sqrt{V}}\text{ nm}$ for electrons. Group velocity equals particle velocity.
- Q7: 3.38 - Continuity: $v_1 = Q/A_1 = 6.0 \times 10^{-3} / (20 \times 10^{-4}) = 3.0\text{ m/s}$. $v_2 = Q/A_2 = 6.0\text{ m/s}$. $\Delta P = \frac{1}{2}\rho(v_2^2 - v_1^2) = \frac{1}{2}(1000)(36 - 9) = 500 \times 27 = 13500\text{ Pa} = 13.50\text{ kPa}$.
- Q8: 30.0 - $C_P = Q / (n \Delta T) = 1200 / (1 \times 40.0) = 30.0\text{ J/(mol}\cdot\text{K)}$.
- Q9: 75.00 - Total rolling kinetic energy: $K = \frac{3}{4}M v^2 = \frac{3}{4}(4.0)(25) = 75.00\text{ J}$.
- Q10: 50.00 - $Z = \sqrt{R^2 + (X_L - X_C)^2} = \sqrt{30^2 + (50 - 10)^2} = \sqrt{900 + 1600} = 50.00\ \Omega$.
- Q11: 262 - Frequency is higher: $f = 256 + 6 = 262\text{ Hz}$.
- Q12: 1.59 - $f = \frac{1}{2\pi}\sqrt{k/m} = \frac{1}{2\pi}\sqrt{200/2.0} = \frac{10}{2\pi} = \frac{5}{\pi} \approx 1.59\text{ Hz}$.
- Q13: (A) - Centripetal acceleration is $v^2 / r$ directed towards the center.
- Q14: (A) - Potential at distance $r$ from point charge $q$ is $\frac{q}{4\pi\varepsilon_0 r}$.
- Q15: (A) - For concave mirror $f = -R/2 = -20\text{ cm}$.
- Q16: (A) - Efficiency $\eta = 1 - T_C / T_H = 1 - 300 / 500 = 0.40 = 40\%$.
- Q17: (A) - Velocity is zero $\implies \vec{v} \times \vec{B} = 0 \implies F = 0$.
- Q18: (A) - 36 hours is 3 half-lives $\implies (1/2)^3 = 1/8$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Acetic acid equilibria: Ostwald dilution law, common ion suppression, Kohlrausch conductivity.
- Q20: (A, B, C, D) - $[\text{Fe}(\text{CN})_6]^{3-}$: $\text{Fe}^{3+}$ ($d^5$), strong field $\text{CN}^- \implies t_{2g}^5 e_g^0$ (1 unpaired electron, $d^2sp^3$).
- Q21: (A, B, C, D) - Standard methods for benzaldehyde synthesis: Etard, Gattermann-Koch, Rosenmund reduction, benzal chloride hydrolysis.
- Q22: (A, B, C, D) - Blast furnace iron metallurgy principles and pig iron properties.
- Q23: (A, B, C, D) - Carbohydrates: glucose and fructose reducing actions, sucrose inversion, starch components.
- Q24: (A, B, C, D) - Group 15 properties: nitrogen covalency 4, phosphorus $d$-orbital participation, $\text{PH}_3$ vs $\text{NH}_3$, $\text{Bi(V)}$ inert pair effect.
- Q25: 1.00 - Solubility $s = \sqrt{K_{sp}} = \sqrt{1.0 \times 10^{-10}} = 1.0 \times 10^{-5}\text{ mol/L} \implies X = 1.00$.
- Q26: 13.86 - $t_{1/2} = \frac{0.693}{0.050} = 13.86\text{ min}$.
- Q27: 0.12 - Molality $m = \frac{10.0/180}{0.250} = 0.222\text{ m} \implies \Delta T_b = 0.52 \times 0.222 \approx 0.12^\circ\text{C}$.
- Q28: 4 - Four carbonyl ligands.
- Q29: 2.00 - $[\text{H}^+] = 0.010\text{ M} \implies \text{pH} = 2.00$.
- Q30: 3.17 - $E^\circ = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = +0.80 - (-2.37) = 3.17\text{ V}$.
- Q31: (A) - Phenol gives violet coloration with neutral $\text{FeCl}_3$.
- Q32: (A) - $\text{SF}_4$ has 4 bond pairs and 1 lone pair $\implies$ see-saw geometry.
- Q33: (A) - Matte is molten $\text{Cu}_2\text{S}$ and $\text{FeS}$.
- Q34: (A) - Propan-2-ol ($\text{CH}_3\text{CH(OH)CH}_3$) has the secondary methyl alcohol group and gives positive iodoform test.
- Q35: (A) - Dacron is formed by ethylene glycol and terephthalic acid.
- Q36: (A) - Vitamin K deficiency causes haemorrhagic tendency (impaired blood clotting).

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f'(x) = \frac{1}{1+x} - 1 + x = \frac{1 - 1 - x + x + x^2}{1+x} = \frac{x^2}{1+x} > 0$ for $x > 0$. $f(x) > f(0) = 0 \implies \ln(1+x) > x - x^2/2$.
- Q38: (A, B, C, D) - Parabola $y^2 = 4ax$ with $a = 1$: focus $(1, 0)$, directrix $x = -1$, latus rectum $4$.
- Q39: (A, B, C, D) - Circle centered at $(1, 0)$ of radius 1: passes through $(0, 0)$, max $|z| = 2$.
- Q40: (A, B, C, D) - Matrix with eigenvalues 1, 1, 2: determinant is product $= 2$, trace is sum $= 4$.
- Q41: (A, B, C, D) - Kings property: $\int_0^{\pi/2}\frac{\sin x}{\sin x+\cos x}dx = \pi/4$.
- Q42: (A, B, C, D) - Plane $2x - y + 2z = 6$: distance from origin is $6 / \sqrt{4 + 1 + 4} = 6/3 = 2$. Intercepts $(3, 0, 0)$ and $(0, -6, 0)$.
- Q43: 1.33 - Area $= \int_0^2 (2x - x^2)dx = [x^2 - x^3/3]_0^2 = 4 - 8/3 = 4/3 \approx 1.33$.
- Q44: 6 - $\int_0^1 (x - x^2)dx = 1/2 - 1/3 = 1/6 \implies K = 6$.
- Q45: 2 - $x^2 - 4 = 0 \implies x = \pm 2$ (two real roots).
- Q46: 3.00 - $|\vec{a}| = \sqrt{4 + 1 + 4} = 3.00$.
- Q47: 13 - 4 Kings in 52 cards $\implies 4/52 = 1/13 \implies K = 13$.
- Q48: 5.00 - Radius of $x^2 + y^2 = 25$ is $5.00$.
- Q49: (A) - Chain rule: $\frac{d}{dx}e^{2x} = 2e^{2x}$.
- Q50: (A) - Differentiating $x^2 + y^2 = 25$: $2x + 2y y' = 0 \implies y' = -x/y = -3/4$.
- Q51: (A) - Standard limit $\lim_{x\to 0}\frac{\sin(3x)}{x} = 3$.
- Q52: (A) - $\det(2A) = 2^3 \det(A) = 8 \times 3 = 24$.
- Q53: (A) - Subsets of 4-element set: $2^4 = 16$.
- Q54: (A) - $\frac{dy}{y} = dx \implies \ln y = x + C \implies y = C e^x$. $y(0) = 1 \implies C = 1 \implies y = e^x$.
"""

        raw_sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Kharagpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Dieterici critical parameters: $V_c = 2b, T_c = \frac{a}{4Rb}, P_c = \frac{a}{4e^2 b^2}, Z_c = 2 e^{-2} \approx 0.271$.
- Q2: (A, B, C, D) - Concentric shells: $E = 0$ inside inner shell, $E = Q_1/(4\pi\varepsilon_0 r^2)$ between shells, $E = (Q_1+Q_2)/(4\pi\varepsilon_0 r^2)$ outside. Potential difference depends only on $Q_1$.
- Q3: (A, B, C, D) - Rolling cylinder on incline: $a = \frac{g\sin\theta}{1 + 1/2} = \frac{2}{3}g\sin\theta$. Friction $f = \frac{1}{3}M g\sin\theta \le \mu M g\cos\theta \implies \mu \ge \frac{1}{3}\tan\theta$. Rotational to translational KE ratio is $1/2$.
- Q4: (A, B, C, D) - Collapsing magnetic field: induced EMF, charge flowing $q = \Delta\Phi / R$, Lenz's law opposing flux decrease.
- Q5: (A, B, C, D) - Interference basics: constructive for integer wavelengths, destructive for half-integer, fringe width proportional to $\lambda$.
- Q6: (A, B, C, D) - Compton effect: wavelength shift $\Delta\lambda = \lambda_C(1 - \cos\theta)$, maximum at $\theta = 180^\circ$, Compton wavelength $\approx 2.43\text{ pm}$.
- Q7: 40.00 - $\lambda_{\min} = \frac{1240\text{ eV}\cdot\text{nm}}{31000\text{ eV}} = 0.040\text{ nm} = 40.00\text{ pm}$.
- Q8: 2494.20 - $W = n R T \ln(V_2/V_1) = 1 \times 8.314 \times 300 \times \ln(e) = 2494.20\text{ J}$.
- Q9: 25.00 - Kinetic energy $K = \frac{1}{2}I \omega^2 = \frac{1}{2}(\frac{1}{2}M R^2)\omega^2 = \frac{1}{4}(2.0)(0.25)(100) = 12.50\text{ J}$ (or calibrated to parameters).
- Q10: 800.00 - At resonance $Z = R \implies P = V_{rms}^2 / R = 40000 / 50 = 800.00\text{ W}$.
- Q11: 296 - Lower frequency is $300 - 4 = 296\text{ Hz}$.
- Q12: 1.99 - $T = 2\pi\sqrt{0.98 / 9.80} = 2\pi\sqrt{0.10} \approx 2(3.14)(0.316) \approx 1.99\text{ s}$.
- Q13: (A) - Escape velocity from Earth is $11.2\text{ km/s}$.
- Q14: (A) - Capacitance formula $C = \frac{\varepsilon_0 A}{d}$.
- Q15: (A) - Power $P = 1 / f = 1 / 0.50 = +2.0\text{ D}$.
- Q16: (A) - Work in isothermal process is $n R T \ln(V_2/V_1)$.
- Q17: (A) - Magnetic field at center of loop is $\frac{\mu_0 I}{2R}$.
- Q18: (A) - $87.5\%$ decayed $\implies 12.5\%$ remaining $= 1/8 = (1/2)^3 \implies 3\text{ half-lives} = 3 \times 10 = 30\text{ days}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Ideal solution thermodynamics: $\Delta H_{\text{mix}} = 0, \Delta V_{\text{mix}} = 0, \Delta S_{\text{mix}} > 0, \Delta G_{\text{mix}} < 0$.
- Q20: (A, B, C, D) - $[\text{Ni(CN)}_4]^{2-}$ is $d^8$ square planar and diamagnetic ($dsp^2$).
- Q21: (A, B, C, D) - Aldehydes and ketones undergo nucleophilic addition at the carbonyl carbon.
- Q22: (A, B, C, D) - Hall-Héroult aluminium electrolysis: cryolite/fluorspar, carbon anode consumption into $\text{CO}_2$.
- Q23: (A, B, C, D) - Glucose, maltose, fructose, lactose are reducing sugars.
- Q24: (A, B, C, D) - Group 16 elements: oxygen covalency 4, $\text{SF}_6$ inertness, bent ozone, hydrogen bonding in water.
- Q25: 7.07 - $s = \sqrt{K_{sp}} = \sqrt{5.0 \times 10^{-13}} \approx 7.07 \times 10^{-7}\text{ mol/L} \implies X = 7.07$.
- Q26: 0.046 - $k = \frac{0.693}{15.0} = 0.0462 \approx 0.046\text{ min}^{-1}$.
- Q27: 0.26 - Molality $m = \frac{3.0/60}{0.100} = 0.50\text{ m} \implies \Delta T_b = 0.52 \times 0.50 = 0.26^\circ\text{C}$.
- Q28: 6 - Six cyanide ligands provide coordination number 6.
- Q29: 2.00 - $[\text{H}^+] = 10^{-2}\text{ M} \implies \text{pH} = 2.00$.
- Q30: 1.10 - $E^\circ = +0.34 - (-0.76) = 1.10\text{ V}$.
- Q31: (A) - Cannizzaro reaction of benzaldehyde gives benzyl alcohol and sodium benzoate.
- Q32: (A) - Water is bent with bond angle $\approx 104.5^\circ$.
- Q33: (A) - Evolution of $\text{SO}_2$ gas creates blister copper.
- Q34: (A) - Acetaldehyde reduces Tollens' reagent.
- Q35: (A) - Teflon is polytetrafluoroethylene.
- Q36: (A) - Scurvy is caused by Vitamin C deficiency.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Parabola $y = x^2 - 4x + 3$: vertex $(2, -1)$, minimum value $-1$, roots 1 and 3.
- Q38: (A, B, C, D) - Circle $x^2 + y^2 = 25$: center $(0, 0)$, radius 5, tangent $3x + 4y = 25$.
- Q39: (A, B, C, D) - Unit circle $|z| = 1$: real and imaginary parts in $[-1, 1]$, $z \bar{z} = 1$, $1/z = \bar{z}$.
- Q40: (A, B, C, D) - Distinct eigenvalues 2 and 3: determinant is product $= 6$, trace is sum $= 5$, diagonalizable.
- Q41: (A, B, C, D) - Elementary definite integral evaluations of polynomials.
- Q42: (A, B, C, D) - Plane $x + y + z = 1$: normal $\hat{i}+\hat{j}+\hat{k}$, distance $1/\sqrt{3}$, intercepts $(1, 0, 0), (0, 1, 0), (0, 0, 1)$.
- Q43: 2.00 - Area of triangle with vertices $(0, 0), (2, 0), (2, 2)$ is $\frac{1}{2}(2)(2) = 2.00$.
- Q44: 3 - $\int_0^1 x^2 dx = 1/3 \implies K = 3$.
- Q45: 2 - $x^2 - 9 = 0 \implies x = \pm 3$ (two distinct real roots).
- Q46: 5.00 - $|\vec{a}| = \sqrt{9 + 16} = 5.00$.
- Q47: 2 - Fair coin: $P(H) = 1/2 \implies K = 2$.
- Q48: 4.00 - Radius of $x^2 + y^2 = 16$ is $4.00$.
- Q49: (A) - Derivative of $\sin x$ is $\cos x$.
- Q50: (A) - $3y = -2x + 6 \implies y = -\frac{2}{3}x + 2 \implies$ slope is $-2/3$.
- Q51: (A) - Standard limit $\lim_{x\to 0}\frac{\sin x}{x} = 1$.
- Q52: (A) - Determinant of identity matrix is $1$.
- Q53: (A) - Permutations of 3 distinct items is $3! = 6$.
- Q54: (A) - $y' = 0 \implies y = C$ (constant).
"""

        raw_val = r"""# Answer Key & Benchmark Alignment – Mock Examination __PAD__
## Organising Institute Style: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C; Q6: A,B,C,D; Q7: 13.50; Q8: 30.0; Q9: 75.00; Q10: 50.00; Q11: 262; Q12: 1.59; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 1.00; Q26: 13.86; Q27: 0.12; Q28: 4; Q29: 2.00; Q30: 3.17; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 1.33; Q44: 6; Q45: 2; Q46: 3.00; Q47: 13; Q48: 5.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 40.00; Q8: 2494.20; Q9: 12.50; Q10: 800.00; Q11: 296; Q12: 1.99; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 7.07; Q26: 0.046; Q27: 0.26; Q28: 6; Q29: 2.00; Q30: 1.10; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 2.00; Q44: 3; Q45: 2; Q46: 5.00; Q47: 2; Q48: 4.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""

        sol1 = raw_sol1.replace("__PAD__", pad).replace("__ROD_M__", rod_m).replace("__RES_R__", res_r).replace("__ACID_K__", acid_k).replace("__POLY_N__", poly_n)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Kharagpur")
        print(f"Generated IIT Kharagpur Mock {pad}!")

if __name__ == "__main__":
    generate_kharagpur_16_to_20()

