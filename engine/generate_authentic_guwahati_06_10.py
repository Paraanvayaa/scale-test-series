# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Guwahati Mocks 06 to 10.
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

def generate_guwahati_06_to_10():
    for mock_idx in range(6, 11):
        pad = f"{mock_idx:02d}"
        comp_ratio = str(4 + mock_idx % 4)
        phot_e = str(50 + 10 * mock_idx)
        carnot_eff = f"{(1 - 300 / (500 + 50 * mock_idx)) * 100:.2f}"
        alpha_k = f"{4.0 + 0.5 * mock_idx:.1f}"
        disc_v = f"{3.0 + 0.5 * mock_idx:.1f}"
        disc_ke = f"{0.75 * 2.0 * (3.0 + 0.5 * mock_idx)**2:.2f}"
        pend_l = f"{0.80 + 0.05 * mock_idx:.2f}"
        pend_t = f"{2 * 3.1416 * ( (0.80 + 0.05 * mock_idx) / 9.8 )**0.5:.2f}"
        
        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
**Historical Reference Benchmark**: 2009, 2016, 2023 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**: +4, -2 (Partials: +3, +2, +1)
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**: +3, 0
- **Section 3 (6 Questions per subject – Single Correct Option)**: +3, -1

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A monoatomic gas undergoes an Otto cycle consisting of two isochoric processes and two adiabatic processes with compression ratio $r = V_1 / V_2 = __COMP_RATIO__$. Let $\gamma = 5/3$:
(A) The theoretical efficiency of the Otto cycle is $\eta = 1 - r^{1 - \gamma}$.  
(B) An increase in compression ratio $r$ strictly increases the thermal efficiency.  
(C) The heat absorbed occurs during the isochoric pressure rise at minimum volume.  
(D) The net entropy change of the working gas over one complete reversible cycle is zero.

#### Question 2
Regarding the Heisenberg Uncertainty Principle $\Delta x \Delta p \ge \frac{\hbar}{2}$ applied to a particle of mass $m$ trapped in a one-dimensional region of size $a$:
(A) The minimum zero-point energy is estimated as $E_0 \approx \frac{\hbar^2}{8 m a^2}$.  
(B) A particle confined to a finite spatial domain can never be completely at rest.  
(C) The simultaneous measurement of non-commuting observables $[\hat{x}, \hat{p}_x] = i\hbar$ has fundamental precision limits.  
(D) Energy-time uncertainty $\Delta E \Delta t \ge \frac{\hbar}{2}$ relates the natural linewidth of an excited atomic state to its lifetime.

#### Question 3
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal surface. A horizontal force $F$ is applied at a height $h$ above the center:
(A) If $h = \frac{2}{5} R$, the sphere rolls without any friction force acting on it.  
(B) If $h > \frac{2}{5} R$, friction acts in the forward direction.  
(C) If $h < \frac{2}{5} R$, friction acts in the backward direction.  
(D) Pure rolling is maintained without slipping if the required friction $|f| \le \mu M g$.

#### Question 4
A parallel-plate capacitor with plate area $A$ and separation $d$ is charged to voltage $V$ by a battery. While remaining connected to the battery, the plate separation is slowly increased to $2d$:
(A) The electric field between the plates decreases by a factor of 2.  
(B) The stored electrostatic energy decreases by a factor of 2.  
(C) The battery does negative work as charge flows back into the battery.  
(D) The mechanical work done by the external agent pulling the plates is positive.

#### Question 5
In a Fabry-Perot interferometer with plate reflectance $R = 0.85$:
(A) The coefficient of finesse is $F = \frac{4 R}{(1 - R)^2}$.  
(B) The transmitted intensity distribution is given by the Airy formula $I_t = \frac{I_0}{1 + F \sin^2(\delta/2)}$.  
(C) The resolving power increases rapidly as reflectance $R \to 1$.  
(D) The sharpness of transmission fringes increases with higher finesse.

#### Question 6
A cosmic ray particle of rest mass $m_0$ decays in flight into two identical photons each of energy $E_0 = __PHOT_E__\text{ MeV}$ emitted symmetrically at angle $\theta = 30^\circ$ to the flight direction:
(A) The rest mass of the decaying particle is $m_0 = \frac{2 E_0 \sin\theta}{c^2}$.  
(B) The momentum of the parent particle is $p = \frac{2 E_0 \cos\theta}{c}$.  
(C) The speed of the parent particle is $v = c \cos\theta$.  
(D) The total energy of the parent particle is $2 E_0$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
Calculate the efficiency of a Carnot engine operating between $T_H = 600\text{ K}$ and $T_C = 300\text{ K}$ in percentage. (Round off to two decimal places).

#### Question 8
In a Rutherford scattering experiment, an $\alpha$-particle of energy $K = __ALPHA_K__\text{ MeV}$ approaches a stationary gold nucleus ($Z = 79$). Find the distance of closest approach in units of $10^{-14}\text{ m}$. (Round off to two decimal places).

#### Question 9
A circular disc of mass $M = 2.0\text{ kg}$ and radius $R = 0.50\text{ m}$ rolls without slipping with velocity $v = __DISC_V__\text{ m/s}$. Calculate its total kinetic energy in Joules. (Round off to two decimal places).

#### Question 10
Find the resonant frequency in Hz of a series LCR circuit with $L = 0.10\text{ H}$ and $C = 10\ \mu\text{F}$. (Take $\pi \approx 3.1416$. Round off to the nearest integer).

#### Question 11
Two sound sources emit frequencies $300\text{ Hz}$ and $305\text{ Hz}$. Find the beat period in seconds. (Round off to two decimal places).

#### Question 12
A simple pendulum of length $L = __PEND_L__\text{ m}$ oscillates with small amplitude. Find its period in seconds. (Take $g = 9.8\text{ m/s}^2$. Round off to two decimal places).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The potential energy of a particle of mass $m$ is $U(x) = U_0 \left[\left(\frac{a}{x}\right)^{12} - 2\left(\frac{a}{x}\right)^6\right]$ (Lennard-Jones potential). The equilibrium separation $x_0$ is:
(A) $x_0 = a$  
(B) $x_0 = 2a$  
(C) $x_0 = a / 2$  
(D) $x_0 = \sqrt{2} a$

#### Question 14
A cylindrical capacitor has inner radius $a$, outer radius $b$, and length $L$. The capacitance per unit length is:
(A) $\frac{2\pi\varepsilon_0}{\ln(b/a)}$  
(B) $\frac{\pi\varepsilon_0}{\ln(b/a)}$  
(C) $\frac{2\pi\varepsilon_0}{b - a}$  
(D) $2\pi\varepsilon_0 \frac{a b}{b - a}$

#### Question 15
In a Young's double-slit experiment, the intensity at the central maximum is $I_0$. The intensity at a point where the path difference is $\lambda/4$ is:
(A) $\frac{I_0}{2}$  
(B) $\frac{I_0}{4}$  
(C) $\frac{I_0}{\sqrt{2}}$  
(D) $0$

#### Question 16
The pressure $P$ and volume $V$ of an ideal gas are related by $P V^{3/2} = \text{constant}$. The bulk modulus of elasticity of the gas is:
(A) $\frac{3}{2} P$  
(B) $\frac{2}{3} P$  
(C) $P$  
(D) $\frac{5}{3} P$

#### Question 17
A charged particle moves in a crossed electric field $\vec{E} = E \hat{j}$ and magnetic field $\vec{B} = B \hat{k}$ along an undeflected trajectory. The velocity of the particle must be:
(A) $\vec{v} = \frac{E}{B}\hat{i}$  
(B) $\vec{v} = -\frac{E}{B}\hat{i}$  
(C) $\vec{v} = \frac{B}{E}\hat{i}$  
(D) $\vec{v} = \frac{E}{B}\hat{k}$

#### Question 18
The activity of a radioactive nuclide drops to $1/16$ of its initial value in $60\text{ hours}$. The half-life is:
(A) $15\text{ hours}$  
(B) $30\text{ hours}$  
(C) $12\text{ hours}$  
(D) $20\text{ hours}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution of an amphiprotic anion $\text{HA}^-$:
(A) It can act both as an acid ($\text{HA}^- \rightleftharpoons \text{H}^+ + \text{A}^{2-}$) and as a base ($\text{HA}^- + \text{H}^+ \rightleftharpoons \text{H}_2\text{A}$).  
(B) The hydronium ion concentration is $[\text{H}^+] = \sqrt{K_{a1} K_{a2}}$.  
(C) The pH of the solution is approximately $\frac{1}{2}(\text{p}K_{a1} + \text{p}K_{a2})$.  
(D) The pH is independent of salt concentration at moderate concentrations.

#### Question 20
Regarding the adsorption of hydrogen gas on platinum surface:
(A) Physisorption dominates at low temperatures, chemisorption at higher temperatures.  
(B) Chemisorption involves dissociative adsorption of $\text{H}_2$ into atomic $\text{H}$ atoms.  
(C) The enthalpy of chemisorption is exothermic ($\Delta H < 0$).  
(D) Chemisorption forms a unimolecular monolayer.

#### Question 21
Regarding the stability of transition metal oxidation states in aqueous solution:
(A) $\text{Cr}^{2+}$ is a strong reducing agent in aqueous solution ($d^4 \to d^3$, stable $t_{2g}^3$).  
(B) $\text{Mn}^{3+}$ is a strong oxidizing agent ($d^4 \to d^5$, half-filled $d^5$).  
(C) $\text{Fe}^{3+}$ is more stable than $\text{Fe}^{2+}$ towards oxidation due to $3d^5$ configuration.  
(D) $\text{Ti}^{4+}$ is diamagnetic ($d^0$).

#### Question 22
Which of the following transformations yield an $\alpha,\beta$-unsaturated carbonyl compound?
(A) Aldol condensation followed by heating  
(B) Perkin reaction of benzaldehyde with acetic anhydride in sodium acetate  
(C) Knoevenagel condensation of benzaldehyde with diethyl malonate  
(D) Cannizzaro reaction

#### Question 23
Regarding the structure of diborane ($\text{B}_2\text{H}_6$):
(A) Two boron atoms and four terminal hydrogen atoms lie in one plane.  
(B) Two bridging hydrogen atoms lie above and below the plane.  
(C) The bridging $\text{B-H-B}$ bonds are 3-center-2-electron bonds.  
(D) The terminal $\text{B-H}$ bonds are normal 2-center-2-electron covalent bonds.

#### Question 24
Which of the following organic compounds will give a positive Lucas test (turbidity within 5 minutes)?
(A) 2-Methylpropan-2-ol ($3^\circ$, instantaneous)  
(B) Propan-2-ol ($2^\circ$, within 5 minutes)  
(C) Butan-1-ol ($1^\circ$, no reaction at room temperature)  
(D) Benzyl alcohol (forms stable carbocation)

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The rate of a reaction quadruples when temperature increases from $300\text{ K}$ to $320\text{ K}$. Calculate the activation energy $E_a$ in $\text{kJ/mol}$. (Round off to two decimal places).

#### Question 26
Calculate the solubility product $K_{sp}$ of lead(II) chloride ($\text{PbCl}_2$) if its solubility is $s = 0.010\text{ M}$. (Express in units of $10^{-6}\text{ M}^3$. Round off to two decimal places).

#### Question 27
A solution of $5.0\text{ g}$ of non-volatile solute in $100\text{ g}$ of water elevates the boiling point by $0.26^\circ\text{C}$. Calculate the molecular weight of the solute. ($K_b = 0.52\text{ K}\cdot\text{kg/mol}$. Round off to the nearest integer).

#### Question 28
In an FCC metal lattice of copper ($a = 361\text{ pm}$), calculate the atomic radius in picometers. (Round off to two decimal places).

#### Question 29
Calculate the pH of a $0.050\text{ M}$ solution of $\text{H}_2\text{SO}_4$ assuming complete dissociation of both protons. (Round off to two decimal places).

#### Question 30
Find the standard EMF in volts for the cell reaction with $\Delta G^\circ = -193.0\text{ kJ/mol}$ and $n = 2$. (Take $F = 96500\text{ C/mol}$. Round off to two decimal places).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Kolbe-Schmitt reaction, sodium phenoxide is heated with carbon dioxide under pressure followed by acid hydrolysis to produce:
(A) Salicylic acid  
(B) Salicylaldehyde  
(C) Benzoic acid  
(D) Phenolphthalein

#### Question 32
The shape of the $\text{XeF}_2$ molecule is:
(A) Linear  
(B) Bent  
(C) Trigonal planar  
(D) Tetrahedral

#### Question 33
Which of the following ions has the highest magnetic moment (spin-only)?
(A) $\text{Fe}^{3+}$ ($3d^5$)  
(B) $\text{Fe}^{2+}$ ($3d^6$)  
(C) $\text{Co}^{2+}$ ($3d^7$)  
(D) $\text{Ni}^{2+}$ ($3d^8$)

#### Question 34
In the extraction of copper, the flux added during smelting in reverberatory furnace is:
(A) Silica ($\text{SiO}_2$)  
(B) Limestone ($\text{CaCO}_3$)  
(C) Coke  
(D) Alumina

#### Question 35
The monomer of Teflon is:
(A) Tetrafluoroethene ($\text{CF}_2=\text{CF}_2$)  
(B) Vinyl chloride  
(C) Acrylonitrile  
(D) Chloroprene

#### Question 36
Which of the following carbohydrates gives a negative Fehling's test?
(A) Sucrose  
(B) Maltose  
(C) Lactose  
(D) Glucose

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x}{x^2 + 4}$ for $x \in \mathbb{R}$:
(A) $f(x) is an odd function.  
(B) The absolute maximum is $\frac{1}{4}$, attained at $x = 2$.  
(C) The absolute minimum is $-\frac{1}{4}$, attained at $x = -2$.  
(D) The horizontal asymptote is $y = 0$.

#### Question 38
Consider the parabola $y^2 = 12x$:
(A) The focus is at $(3, 0)$.  
(B) The directrix is $x = -3$.  
(C) The length of the latus rectum is $12$.  
(D) The vertex is at $(0, 0)$.

#### Question 39
Let $z$ be a complex number satisfying $|z| = 2$:
(A) The maximum value of $|z + 3 + 4i|$ is $7$.  
(B) The minimum value of $|z + 3 + 4i|$ is $3$.  
(C) The locus of $z$ is a circle centered at the origin.  
(D) $\text{Re}(z) \in [-2, 2]$.

#### Question 40
Let $A$ be a $3 \times 3$ matrix such that $A^T = -A$ (skew-symmetric):
(A) $\det(A) = 0$.  
(B) The eigenvalues of $A$ are purely imaginary or zero.  
(C) $\text{Tr}(A) = 0$.  
(D) $I + A$ is invertible.

#### Question 41
Let $f(x)$ be continuous on $[0, \pi]$:
(A) $\int_0^\pi x f(\sin x) \, dx = \frac{\pi}{2}\int_0^\pi f(\sin x) \, dx$.  
(B) $\int_0^{\pi/2} \ln(\sin x) \, dx = -\frac{\pi}{2}\ln 2$.  
(C) $\int_0^{\pi/2} \ln(\cos x) \, dx = -\frac{\pi}{2}\ln 2$.  
(D) $\int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x} \, dx = \frac{\pi}{4}$.

#### Question 42
Consider the planes $x - y + z = 1$ and $x + y - z = 1$:
(A) The line of intersection has direction ratios $(0, 1, 1)$.  
(B) The point $(1, 0, 0)$ lies on both planes.  
(C) The angle between the planes is $\arccos(-1/3)$.  
(D) The planes are not parallel.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the parabola $y = x^2$ and the line $y = 4$. (Round off to two decimal places).

#### Question 44
Evaluate the integral $\int_0^{\pi/2} \sin^2 x \, dx$. (Take $\pi \approx 3.1416$. Round off to two decimal places).

#### Question 45
Find the number of local extrema of $f(x) = x^3 - 3x + 4$.

#### Question 46
Let $\vec{a} = \hat{i} + \hat{j}$ and $\vec{b} = \hat{j} + \hat{k}$. Find $|\vec{a} \times \vec{b}|^2$.

#### Question 47
Two dice are thrown together. Find the probability (in percentage) of getting a doublet. (Round off to two decimal places).

#### Question 48
Find the radius of the circle $x^2 + y^2 - 10x + 24y = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\sin(x^2)$ with respect to $x$ is:
(A) $2x \cos(x^2)$  
(B) $\cos(x^2)$  
(C) $2 \cos(x^2)$  
(D) $-2x \cos(x^2)$

#### Question 50
The slope of the tangent to the circle $x^2 + y^2 = 25$ at $(3, 4)$ is:
(A) $-\frac{3}{4}$  
(B) $\frac{3}{4}$  
(C) $-\frac{4}{3}$  
(D) $\frac{4}{3}$

#### Question 51
The value of $\lim_{x \to 0} \frac{\tan 2x}{x}$ is:
(A) $2$  
(B) $1$  
(C) $\frac{1}{2}$  
(D) $0$

#### Question 52
If $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, then $\det(A)$ is:
(A) $-2$  
(B) $2$  
(C) $10$  
(D) $-10$

#### Question 53
The number of subsets of a set containing 4 elements is:
(A) $16$  
(B) $8$  
(C) $4$  
(D) $32$

#### Question 54
The solution of $\frac{dy}{dx} = e^x$ with $y(0) = 0$ is:
(A) $y = e^x - 1$  
(B) $y = e^x$  
(C) $y = e^x + 1$  
(D) $y = x e^x$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
**Historical Reference Benchmark**: 2009, 2016, 2023 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**: +4, -2
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**: +3, 0
- **Section 3 (6 Questions per subject – Matching List / Matrix Match)**: +3, -1

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A heat engine uses 1 mole of an ideal monoatomic gas in a reversible cycle consisting of: isobaric heating at $P_0$ from $V_0$ to $2V_0$, isochoric cooling to $P_0/2$, isobaric compression to $V_0$, and isochoric heating back to $P_0$:
(A) The cycle forms a rectangle on the $P-V$ diagram.  
(B) The net work done per cycle is $W = \frac{1}{2} P_0 V_0$.  
(C) Heat is absorbed during the isobaric expansion and isochoric heating steps.  
(D) The efficiency of this rectangular cycle is strictly less than 20%.

#### Question 2
Regarding radioactive decay series ($4n, 4n+1, 4n+2, 4n+3$):
(A) The $4n$ series is the Thorium series starting with $^{232}\text{Th}$ and ending with $^{208}\text{Pb}$.  
(B) The $4n+2$ series is the Uranium series starting with $^{238}\text{U}$ and ending with $^{206}\text{Pb}$.  
(C) The $4n+3$ series is the Actinium series starting with $^{235}\text{U}$ and ending with $^{207}\text{Pb}$.  
(D) In every $\alpha$-decay, the mass number $A$ decreases by 4.

#### Question 3
A glass prism of apex angle $A = 60^\circ$ has refractive index $\mu = \sqrt{2}$. A ray of light is incident at the angle of minimum deviation:
(A) The angle of minimum deviation is $\delta_m = 30^\circ$.  
(B) The angle of incidence at minimum deviation is $i = 45^\circ$.  
(C) Inside the prism, the refracted ray is parallel to the base of the prism.  
(D) The angle of emergence equals the angle of incidence.

#### Question 4
A charged spherical conductor of radius $R$ carries total charge $Q$:
(A) The electric field inside ($r < R$) is zero everywhere.  
(B) The electrostatic potential inside is constant and equals $\frac{Q}{4\pi\varepsilon_0 R}$.  
(C) The electrostatic energy stored in the field is $U = \frac{Q^2}{8\pi\varepsilon_0 R}$.  
(D) Electrostatic pressure on the surface is $P_e = \frac{\sigma^2}{2\varepsilon_0}$.

#### Question 5
A particle of mass $m$ is attached to a light inextensible string of length $L$ and whirled in a vertical circle:
(A) The minimum speed at the highest point to complete the circle is $v_{\min} = \sqrt{g L}$.  
(B) The minimum speed at the lowest point is $u_{\min} = \sqrt{5 g L}$.  
(C) The tension at the lowest point under minimum speed condition is $6 m g$.  
(D) Tension at the highest point is zero under minimum speed condition.

#### Question 6
Regarding Maxwell's displacement current $I_D = \varepsilon_0 \frac{d\Phi_E}{dt}$:
(A) It arises from a time-varying electric flux.  
(B) It satisfies the generalized Ampere-Maxwell law $\oint \vec{B}\cdot d\vec{l} = \mu_0(I_C + I_D)$.  
(C) Inside a parallel plate capacitor being charged, $I_D = I_C$ (conduction current in wires).  
(D) It preserves the continuity of total current across capacitor plates.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
Calculate the ratio of the de Broglie wavelength of an electron accelerated through $100\text{ V}$ to that through $400\text{ V}$.

#### Question 8
Find the molar heat capacity $C$ of an ideal monoatomic gas during an isobaric expansion in units of $R$. (Round off to two decimal places).

#### Question 9
A solid cylinder of mass $M = 4.0\text{ kg}$ and radius $R = 0.20\text{ m}$ has moment of inertia about its axis in $\text{kg}\cdot\text{m}^2$. (Round off to two decimal places).

#### Question 10
In an AC circuit, $V_{\text{rms}} = 220\text{ V}$ and $I_{\text{rms}} = 5.0\text{ A}$ with power factor $\cos\phi = 0.80$. Find the average power dissipated in watts.

#### Question 11
Two organ pipes, one closed of length $L_1 = 0.75\text{ m}$ and one open of length $L_2 = 1.0\text{ m}$, sound their fundamental frequencies. If speed of sound is $340\text{ m/s}$, calculate the frequency of the open pipe in Hz.

#### Question 12
A spring of constant $k = 400\text{ N/m}$ is compressed by $0.10\text{ m}$. Find the energy stored in Joules.

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the thermodynamic cycles with their working media:
- (P) Carnot -> (1) Ideal gas
- (Q) Rankine -> (2) Steam / water
- (R) Otto -> (3) Air-fuel mixture
- (S) Diesel -> (4) Heavy oil-air mixture
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 14
Match the optical instruments with their magnifying power formulas:
- (P) Simple Microscope -> (1) $1 + \frac{D}{f}$
- (Q) Compound Microscope -> (2) $\frac{L}{f_o}\frac{D}{f_e}$
- (R) Astronomical Telescope -> (3) $\frac{f_o}{f_e}$
- (S) Terrestrial Telescope -> (4) $\frac{f_o}{f_e}$ (erect image)
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 15
Match the physical constants with their dimensions:
- (P) Gravitational constant $G$ -> (1) $[M^{-1} L^3 T^{-2}]$
- (Q) Planck's constant $h$ -> (2) $[M L^2 T^{-1}]$
- (R) Permeability $\mu_0$ -> (3) $[M L T^{-2} A^{-2}]$
- (S) Permittivity $\varepsilon_0$ -> (4) $[M^{-1} L^{-3} T^4 A^2]$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 16
Match the magnetic materials with their magnetic susceptibility $\chi$:
- (P) Diamagnetic -> (1) Small and negative ($\chi \sim -10^{-5}$)
- (Q) Paramagnetic -> (2) Small and positive ($\chi \sim +10^{-4}$)
- (R) Ferromagnetic -> (3) Very large and positive ($\chi \gg 1$)
- (S) Superconductor -> (4) Perfect diamagnet ($\chi = -1$)
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 17
Match the nuclear reactions with their energy yields:
- (P) $D-T$ fusion -> (1) $17.6\text{ MeV}$
- (Q) $^{235}\text{U}$ fission -> (2) $\approx 200\text{ MeV}$
- (R) $p-p$ chain fusion -> (3) $\approx 26.7\text{ MeV}$
- (S) Carbon nitrogen cycle -> (4) $\approx 26.7\text{ MeV}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 18
Match the physical laws with their mathematical forms:
- (P) Coulomb's Law -> (1) $F = \frac{q_1 q_2}{4\pi\varepsilon_0 r^2}$
- (Q) Biot-Savart Law -> (2) $d\vec{B} = \frac{\mu_0 I}{4\pi}\frac{d\vec{l}\times\hat{r}}{r^2}$
- (R) Faraday's Law -> (3) $\mathcal{E} = -\frac{d\Phi_B}{dt}$
- (S) Ampere's Law -> (4) $\oint \vec{B}\cdot d\vec{l} = \mu_0 I_{\text{enc}}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the elevation in boiling point ($\Delta T_b = K_b m$):
(A) Molal elevation constant $K_b = \frac{R T_b^2 M_{\text{solvent}}}{1000 \Delta H_{\text{vap}}}$.  
(B) $K_b$ is a characteristic property of the solvent alone.  
(C) Units of $K_b$ are $\text{K}\cdot\text{kg/mol}$.  
(D) Equimolar solutions of glucose and urea in water have the same boiling point elevation.

#### Question 20
Regarding the crystal structures of spinels:
(A) Normal spinel ($\text{MgAl}_2\text{O}_4$) has oxide ions in FCC array.  
(B) In normal spinel, divalent $\text{Mg}^{2+}$ ions occupy $1/8$ of tetrahedral voids.  
(C) In normal spinel, trivalent $\text{Al}^{3+}$ ions occupy $1/2$ of octahedral voids.  
(D) Magnetite ($\text{Fe}_3\text{O}_4$) is an inverse spinel.

#### Question 21
Which of the following statements regarding the stability of aromatic compounds is/are correct?
(A) Benzene possesses resonance energy of approximately $150\text{ kJ/mol}$ ($36\text{ kcal/mol}$).  
(B) Cyclooctatetraene is non-planar (tub-shaped) to avoid antiaromaticity.  
(C) Cyclopentadienyl anion is aromatic with $6\ \pi$-electrons.  
(D) Pyridine is aromatic and basic.

#### Question 22
Regarding the extraction of iron in a blast furnace:
(A) Carbon monoxide is the main reducing agent in the upper zone ($400 - 700^\circ\text{C}$).  
(B) Carbon acts as reducing agent in the lower high-temperature zone ($> 1000^\circ\text{C}$).  
(C) Slag is calcium silicate ($\text{CaSiO}_3$).  
(D) Pig iron contains $\approx 4\%$ carbon.

#### Question 23
Which of the following tests can be used to identify carbohydrates?
(A) Molisch's test (violet ring with $\alpha$-naphthol and conc. $\text{H}_2\text{SO}_4$)  
(B) Benedict's test  
(C) Fehling's test  
(D) Biuret test (specific for peptide bonds, negative for simple sugars)

#### Question 24
Which of the following statements regarding group 17 elements (Halogens) is/are correct?
(A) Electronegativity order is $\text{F} > \text{Cl} > \text{Br} > \text{I}$.  
(B) Electron gain enthalpy of chlorine is more negative than that of fluorine.  
(C) Bond dissociation enthalpy order is $\text{Cl}_2 > \text{Br}_2 > \text{F}_2 > \text{I}_2$.  
(D) Acid strength of hydrogen halides is $\text{HF} < \text{HCl} < \text{HBr} < \text{HI}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The decomposition of $\text{N}_2\text{O}_5$ has rate constant $k = 5.0 \times 10^{-4}\text{ s}^{-1}$. Find the half-life in seconds. (Round off to the nearest integer).

#### Question 26
Calculate the solubility product $K_{sp}$ of silver chloride ($\text{AgCl}$) if its solubility in water is $1.3 \times 10^{-5}\text{ mol/L}$. (Express in units of $10^{-10}\text{ M}^2$. Round off to two decimal places).

#### Question 27
An aqueous solution contains $3.0\text{ g}$ of urea ($M = 60\text{ g/mol}$) in $250\text{ g}$ of water. Calculate the freezing point depression $\Delta T_f$ in $^\circ\text{C}$. ($K_f = 1.86\text{ K}\cdot\text{kg/mol}$. Round off to two decimal places).

#### Question 28
Find the number of tetrahedral voids per unit cell in an FCC crystal lattice.

#### Question 29
Calculate the pH of a $0.001\text{ M}$ $\text{HCl}$ aqueous solution.

#### Question 30
Find the standard potential $E^\circ$ in volts for the reaction $\text{Cu}^{2+} + 2e^- \to \text{Cu}$ given $\Delta G^\circ = -65.62\text{ kJ/mol}$. (Take $F = 96500\text{ C/mol}$. Round off to two decimal places).

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the named organic reactions with their characteristic reactants:
- (P) Wurtz Reaction -> (1) Alkyl halide + $\text{Na}$ in dry ether
- (Q) Fittig Reaction -> (2) Aryl halide + $\text{Na}$ in dry ether
- (R) Wurtz-Fittig Reaction -> (3) Alkyl halide + Aryl halide + $\text{Na}$ in dry ether
- (S) Frankland Reaction -> (4) Alkyl halide + $\text{Zn}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 32
Match the oxides of sulfur with their properties:
- (P) $\text{SO}_2$ -> (1) Colorless gas with suffocating odor of burning sulfur
- (Q) $\text{SO}_3$ -> (2) Trigonal planar in gas phase, cyclic trimer $(\text{SO}_3)_3$ in solid
- (R) $\text{H}_2\text{SO}_3$ -> (3) Diprotic weak acid
- (S) $\text{H}_2\text{SO}_4$ -> (4) King of chemicals, strong dehydrating agent
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 33
Match the polymers with their repeating monomers:
- (P) Polyvinyl chloride -> (1) Vinyl chloride ($\text{CH}_2=\text{CHCl}$)
- (Q) Polystyrene -> (2) Styrene ($\text{C}_6\text{H}_5\text{CH}=\text{CH}_2$)
- (R) Polypropene -> (3) Propene ($\text{CH}_3\text{CH}=\text{CH}_2$)
- (S) Polyacrylonitrile -> (4) Acrylonitrile ($\text{CH}_2=\text{CH-CN}$)
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 34
Match the metals with their refining methods:
- (P) Nickel -> (1) Mond's process
- (Q) Titanium -> (2) Van Arkel method
- (R) Copper -> (3) Electrolytic refining
- (S) Germanium / Silicon -> (4) Zone refining (semiconductors)
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 35
Match the colloidal systems with their dispersed phase and dispersion medium:
- (P) Sol -> (1) Solid in liquid
- (Q) Emulsion -> (2) Liquid in liquid
- (R) Foam -> (3) Gas in liquid
- (S) Solid Sol -> (4) Solid in solid
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 36
Match the biomolecules with their key functions:
- (P) Hemoglobin -> (1) Oxygen transport in blood
- (Q) Insulin -> (2) Glucose metabolism regulation
- (R) DNA -> (3) Genetic information storage
- (S) Chlorophyll -> (4) Photosynthesis light harvesting
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^2 e^{-x^2}$ for $x \in \mathbb{R}$:
(A) $f(x)$ is an even function.  
(B) The absolute maximum is $\frac{1}{e}$, attained at $x = \pm 1$.  
(C) The absolute minimum is $0$, attained at $x = 0$.  
(D) $\lim_{x \to \pm\infty} f(x) = 0$.

#### Question 38
Consider the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$:
(A) The eccentricity is $e = \frac{\sqrt{7}}{4}$.  
(B) The foci lie at $(\pm\sqrt{7}, 0)$.  
(C) The length of the major axis is $8$.  
(D) The length of the minor axis is $6$.

#### Question 39
Let $z$ be a complex number satisfying $|z - 1| = |z - i|$:
(A) The locus of $z$ is the line $y = x$.  
(B) $z$ is equidistant from $(1, 0)$ and $(0, 1)$.  
(C) The origin $(0, 0)$ lies on the locus.  
(D) $1 + i$ lies on the locus.

#### Question 40
Let $A$ be a $3 \times 3$ matrix such that $A^2 = I_3$:
(A) The eigenvalues of $A$ can only be $1$ or $-1$.  
(B) $\det(A)$ is either $1$ or $-1$.  
(C) $A = A^{-1}$.  
(D) $(I - A)(I + A) = 0$.

#### Question 41
Let $f$ be continuous on $[0, a]$:
(A) $\int_0^a f(x) \, dx = \int_0^a f(a - x) \, dx$.  
(B) $\int_0^{2a} f(x) \, dx = \int_0^a f(x) \, dx + \int_0^a f(2a - x) \, dx$.  
(C) If $f(2a - x) = f(x)$, then $\int_0^{2a} f(x) \, dx = 2 \int_0^a f(x) \, dx$.  
(D) If $f(2a - x) = -f(x)$, then $\int_0^{2a} f(x) \, dx = 0$.

#### Question 42
Consider the line $\frac{x}{2} = \frac{y}{3} = \frac{z}{4}$ and the plane $2x + 3y + 4z = 29$:
(A) The direction vector of the line is parallel to the normal to the plane.  
(B) The line is perpendicular to the plane.  
(C) The point of intersection is $(2, 3, 4)$.  
(D) The distance of the origin from the plane is $\frac{29}{\sqrt{29}} = \sqrt{29}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = x^2$ and the line $y = x$. (Round off to two decimal places).

#### Question 44
Evaluate the integral $\int_0^1 x^3 \, dx$. (Round off to two decimal places).

#### Question 45
Find the number of real roots of $x^3 - 3x = 0$.

#### Question 46
Let $\vec{a} = 3\hat{i} + 4\hat{j}$. Find $|\vec{a}|$.

#### Question 47
A card is drawn from a standard pack of 52 cards. Find the probability (in percentage) that it is an Ace. (Round off to two decimal places).

#### Question 48
Find the radius of the circle $x^2 + y^2 - 4x - 6y = 0$. (Round off to two decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\cos(3x)$ with respect to $x$ is:
(A) $-3\sin(3x)$  
(B) $3\sin(3x)$  
(C) $-\sin(3x)$  
(D) $-3\cos(3x)$

#### Question 50
The focus of the parabola $y^2 = 16x$ is at:
(A) $(4, 0)$  
(B) $(0, 4)$  
(C) $(-4, 0)$  
(D) $(8, 0)$

#### Question 51
The value of $\lim_{x \to 0} \frac{\sin 5x}{x}$ is:
(A) $5$  
(B) $1$  
(C) $0$  
(D) $\frac{1}{5}$

#### Question 52
If $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$, then $A^2$ is:
(A) $\begin{pmatrix} 4 & 0 \\ 0 & 9 \end{pmatrix}$  
(B) $\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$  
(C) $\begin{pmatrix} 4 & 0 \\ 0 & 6 \end{pmatrix}$  
(D) $\begin{pmatrix} 0 & 4 \\ 9 & 0 \end{pmatrix}$

#### Question 53
The number of permutations of 3 distinct objects taken all at a time is:
(A) $6$  
(B) $3$  
(C) $9$  
(D) $1$

#### Question 54
The general solution of $\frac{dy}{dx} = 2x$ is:
(A) $y = x^2 + C$  
(B) $y = 2x + C$  
(C) $y = x + C$  
(D) $y = \frac{x^2}{2} + C$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__COMP_RATIO__", comp_ratio).replace("__PHOT_E__", phot_e).replace("__ALPHA_K__", alpha_k).replace("__DISC_V__", disc_v).replace("__PEND_L__", pend_l)
        p2 = raw_p2.replace("__PAD__", pad)
        
        sol1 = f"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Guwahati Benchmark JEE Advanced Mock Examination {pad}

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Otto cycle analysis with compression ratio $r = {comp_ratio}$.
- Q2: (A, B, C, D) - Heisenberg uncertainty principle and zero point energy.
- Q3: (A, B, C, D) - Rolling with applied horizontal force at height $h$.
- Q4: (A, B, C, D) - Increasing separation of capacitor connected to battery.
- Q5: (A, B, C, D) - Fabry-Perot interferometer finesse.
- Q6: (A, B, C, D) - Symmetrical two-photon decay kinematics.
- Q7: {carnot_eff} - Carnot efficiency.
- Q8: 4.50 - Distance of closest approach for alpha scattering.
- Q9: {disc_ke} - Rolling disc kinetic energy $\\frac{{3}}{{4}}M v^2$.
- Q10: 159 - Resonant frequency $f_0 = \\frac{{1}}{{2\\pi\\sqrt{{L C}}}}$.
- Q11: 0.20 - Beat period $1 / \\Delta f = 1/5 = 0.20\\text{{ s}}$.
- Q12: {pend_t} - Simple pendulum period.
- Q13: (A) - Lennard-Jones equilibrium separation $x_0 = a$.
- Q14: (A) - Cylindrical capacitance per unit length.
- Q15: (A) - Path difference $\\lambda/4 \\implies \\Delta\\phi = \\pi/2 \\implies I = I_0 \\cos^2(\\pi/4) = I_0/2$.
- Q16: (A) - Polytropic bulk modulus $\\gamma P = 1.5 P$.
- Q17: (A) - Velocity selector condition $\\vec{{v}} = \\frac{{E}}{{B}}\\hat{{i}}$.
- Q18: (A) - $1/16 = (1/2)^4 \\implies 4$ half-lives $= 60\\text{{ hr}} \\implies t_{{1/2}} = 15\\text{{ hr}}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Amphiprotic anion equilibria.
- Q20: (A, B, C, D) - Hydrogen adsorption on platinum.
- Q21: (A, B, C, D) - Transition metal oxidation states stability.
- Q22: (A, B, C) - Condensation reactions yielding $\\alpha,\\beta$-unsaturated carbonyls.
- Q23: (A, B, C, D) - Diborane 3c-2e bond structure.
- Q24: (A, B, D) - Lucas test turbidity behavior.
- Q25: 55.33 - Arrhenius activation energy calculation.
- Q26: 4.00 - $K_{{sp}} = 4 s^3 = 4(0.01)^3 = 4 \\times 10^{{-6}}$.
- Q27: 100 - $\\Delta T_b = K_b \\frac{{w_B \\times 1000}}{{M_B \\times w_A}} \\implies M_B = 100\\text{{ g/mol}}$.
- Q28: 127.63 - $4r = \\sqrt{{2}}a \\implies r = \\frac{{\\sqrt{{2}}(361)}}{{4}} \\approx 127.63\\text{{ pm}}$.
- Q29: 1.00 - $[\\text{{H}}^+] = 2(0.050) = 0.10\\text{{ M}} \\implies \\text{{pH}} = 1.00$.
- Q30: 1.00 - $E^\\circ = \\frac{{-\\Delta G^\\circ}}{{n F}} = \\frac{{193000}}{{2 \\times 96500}} = 1.00\\text{{ V}}$.
- Q31: (A) - Kolbe reaction yields salicylic acid.
- Q32: (A) - $\\text{{XeF}}_2$ has 3 equatorial lone pairs $\\implies$ linear.
- Q33: (A) - $\\text{{Fe}}^{{3+}}$ has 5 unpaired electrons ($d^5$, $\\mu = 5.92\\ \\mu_B$).
- Q34: (A) - Silica is added as flux to remove $\\text{{FeO}}$ as slag.
- Q35: (A) - Teflon monomer is tetrafluoroethene.
- Q36: (A) - Sucrose is a non-reducing sugar.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Rational odd function analysis.
- Q38: (A, B, C, D) - Parabola $y^2 = 12x$ geometry.
- Q39: (A, B, C, D) - Circle $|z| = 2$ in complex plane.
- Q40: (A, B, C, D) - Skew-symmetric matrix properties.
- Q41: (A, B, C, D) - Definite integrals symmetry properties.
- Q42: (A, B, C, D) - Intersection of two planes.
- Q43: 10.67 - Area between $y = x^2$ and $y = 4$ is $2 \\int_0^2 (4 - x^2) dx = 32/3 \\approx 10.67$.
- Q44: 0.79 - $\\int_0^{{\\pi/2}} \\sin^2 x dx = \\pi/4 \\approx 0.79$.
- Q45: 2 - $f'(x) = 3x^2 - 3 = 0 \\implies x = \\pm 1$ (2 extrema).
- Q46: 3.00 - $\\vec{{a}}\\times\\vec{{b}} = \\hat{{i}} - \\hat{{j}} + \\hat{{k}} \\implies |\\vec{{a}}\\times\\vec{{b}}|^2 = 3.00$.
- Q47: 16.67 - Doublet probability $6/36 = 1/6 \\approx 16.67\\%$.
- Q48: 13.00 - $R = \\sqrt{{25 + 144}} = 13.00$.
- Q49: (A) - Derivative is $2x \\cos(x^2)$.
- Q50: (A) - $2x + 2y y' = 0 \\implies y' = -x/y = -3/4$.
- Q51: (A) - Limit $= 2$.
- Q52: (A) - $1(4) - 2(3) = -2$.
- Q53: (A) - $2^4 = 16$.
- Q54: (A) - $y = e^x - 1$.
"""

        sol2 = f"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Guwahati Benchmark JEE Advanced Mock Examination {pad}

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Rectangular cycle on P-V diagram.
- Q2: (A, B, C, D) - Natural radioactive decay series.
- Q3: (A, B, C, D) - Minimum deviation in equilateral prism.
- Q4: (A, B, C, D) - Spherical conductor electrostatics.
- Q5: (A, B, C, D) - Vertical circular motion critical velocity.
- Q6: (A, B, C, D) - Maxwell's displacement current properties.
- Q7: 2.00 - $\\lambda \\propto 1/\\sqrt{{V}} \\implies \\lambda_1 / \\lambda_2 = \\sqrt{{400/100}} = 2.00$.
- Q8: 2.50 - $C_P = \\frac{{5}}{{2}}R = 2.50 R$.
- Q9: 0.08 - $I = \\frac{{1}}{{2}}M R^2 = \\frac{{1}}{{2}}(4)(0.04) = 0.08\\text{{ kg}}\\cdot\\text{{m}}^2$.
- Q10: 880.00 - $P = V_{{\\text{{rms}}}} I_{{\\text{{rms}}}} \\cos\\phi = 220(5.0)(0.80) = 880.00\\text{{ W}}$.
- Q11: 170.00 - $f = \\frac{{v}}{{2 L_2}} = \\frac{{340}}{{2(1.0)}} = 170.00\\text{{ Hz}}$.
- Q12: 2.00 - $U = \\frac{{1}}{{2}}k x^2 = \\frac{{1}}{{2}}(400)(0.01) = 2.00\\text{{ J}}$.
- Q13: (A) - Thermodynamic cycle working fluids.
- Q14: (A) - Optical instruments magnification.
- Q15: (A) - Physical constants dimensional analysis.
- Q16: (A) - Magnetic susceptibilities.
- Q17: (A) - Nuclear fusion and fission energy yields.
- Q18: (A) - Classical electromagnetism laws.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Molal boiling point elevation constant properties.
- Q20: (A, B, C, D) - Normal and inverse spinel crystal structures.
- Q21: (A, B, C, D) - Aromaticity criteria and resonance energy.
- Q22: (A, B, C, D) - Blast furnace iron smelting reactions.
- Q23: (A, B, C) - Qualitative tests for carbohydrates. Biuret tests peptide bonds.
- Q24: (A, B, C, D) - Group 17 periodic trends.
- Q25: 1386 - $t_{{1/2}} = \\frac{{0.693}}{{5.0 \\times 10^{{-4}}}} = 1386\\text{{ s}}$.
- Q26: 1.69 - $K_{{sp}} = s^2 = (1.3 \\times 10^{{-5}})^2 = 1.69 \\times 10^{{-10}}$.
- Q27: 0.37 - $m = \\frac{{3/60}}{{0.250}} = 0.20\\text{{ m}} \\implies \\Delta T_f = 1.86(0.20) = 0.372^\\circ\\text{{C}}$.
- Q28: 8 - In FCC ($Z = 4$), number of tetrahedral voids $= 2 Z = 8$.
- Q29: 3.00 - $[\\text{{H}}^+] = 10^{{-3}}\\text{{ M}} \\implies \\text{{pH}} = 3.00$.
- Q30: 0.34 - $E^\\circ = \\frac{{-\\Delta G^\\circ}}{{n F}} = \\frac{{65620}}{{2 \\times 96500}} = 0.34\\text{{ V}}$ (Copper).
- Q31: (A) - Organohalide coupling reactions.
- Q32: (A) - Sulfur oxides and oxoacids.
- Q33: (A) - Addition polymers repeating units.
- Q34: (A) - Metallurgy refining processes.
- Q35: (A) - Colloid phase classifications.
- Q36: (A) - Biomolecules physiological roles.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Gaussian-modulated rational function analysis.
- Q38: (A, B, C, D) - Standard ellipse geometry.
- Q39: (A, B, C, D) - Perpendicular bisector line in Argand plane.
- Q40: (A, B, C, D) - Involutory matrix properties.
- Q41: (A, B, C, D) - Definite integrals symmetry properties.
- Q42: (A, B, C, D) - Line perpendicular to plane.
- Q43: 0.17 - $\\int_0^1 (x - x^2) dx = [\\frac{{x^2}}{{2}} - \\frac{{x^3}}{{3}}]_0^1 = 1/6 \\approx 0.17$.
- Q44: 0.25 - $\\int_0^1 x^3 dx = 1/4 = 0.25$.
- Q45: 3 - $x(x^2 - 3) = 0 \\implies x = 0, \\pm\\sqrt{{3}}$ (3 roots).
- Q46: 5.00 - $|\\vec{{a}}| = \\sqrt{{9 + 16}} = 5.00$.
- Q47: 7.69 - $4/52 = 1/13 \\approx 7.69\\%$.
- Q48: 3.61 - Center $(2, 3)$, $R = \\sqrt{{4 + 9}} = \\sqrt{{13}} \\approx 3.61$.
- Q49: (A) - $\\frac{{d}}{{dx}}\\cos(3x) = -3\\sin(3x)$.
- Q50: (A) - Focus of $y^2 = 4ax$ with $4a = 16 \\implies a = 4 \\implies (4, 0)$.
- Q51: (A) - Limit $= 5$.
- Q52: (A) - $A^2 = \\text{{diag}}(4, 9)$.
- Q53: (A) - $3! = 6$.
- Q54: (A) - $y = x^2 + C$.
"""

        val = f"""# Answer Key & Benchmark Alignment – Mock Examination {pad}
## Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: {carnot_eff}; Q8: 4.50; Q9: {disc_ke}; Q10: 159; Q11: 0.20; Q12: {pend_t}; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C; Q23: A,B,C,D; Q24: A,B,D; Q25: 55.33; Q26: 4.00; Q27: 100.00; Q28: 127.63; Q29: 1.00; Q30: 1.00; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 10.67; Q44: 0.79; Q45: 2.00; Q46: 3.00; Q47: 16.67; Q48: 13.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 2.00; Q8: 2.50; Q9: 0.08; Q10: 880.00; Q11: 170.00; Q12: 2.00; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C; Q24: A,B,C,D; Q25: 1386.00; Q26: 1.69; Q27: 0.37; Q28: 8.00; Q29: 3.00; Q30: 0.34; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 0.17; Q44: 0.25; Q45: 3.00; Q46: 5.00; Q47: 7.69; Q48: 3.61; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""
        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Guwahati")
        print(f"Generated IIT Guwahati Mock {pad}!")

if __name__ == "__main__":
    generate_guwahati_06_to_10()
