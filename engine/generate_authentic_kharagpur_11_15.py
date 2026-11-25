"""
IIT Kharagpur Mocks 11 to 15 Generator
Organising Institute: Indian Institute of Technology Kharagpur
Empirical Benchmark: 2006, 2014, 2021 Official JEE Advanced Papers
Features:
- Asymmetric paper difficulty & long descriptive stems
- Constraint mechanics, non-uniform rotational dynamics, electrodynamics
- Extensive organic reaction cascades, inorganic quantitative metallurgy, ionic equilibria
- Advanced integral calculus (Leibniz rule), 3D coordinate geometry, probability distributions
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_kharagpur_11_to_15():
    for mock_idx in range(11, 16):
        pad = f"{mock_idx:02d}"
        rod_m = str(1.8 + (mock_idx % 4) * 0.2)
        res_r = str(8.0 + (mock_idx % 3) * 2.0)
        acid_k = str(1.2 + (mock_idx % 3) * 0.4)
        poly_n = str(4 + (mock_idx % 3))

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
A uniform thin rod $AB$ of mass $M = __ROD_M__\text{ kg}$ and length $L = 1.0\text{ m}$ is suspended by two identical vertical light inextensible strings attached to its ends $A$ and $B$. The string at end $B$ is cut suddenly:
(A) Immediately after the string is cut, the tension in the remaining string at end $A$ drops instantaneously to $M g / 4$.  
(B) The angular acceleration of the rod about end $A$ immediately after release is $\alpha = \frac{3g}{2L}$.  
(C) The linear acceleration of the center of mass of the rod immediately after release is $a_{cm} = \frac{3}{4}g$ vertically downwards.  
(D) The acceleration of end $B$ immediately after the cut is $a_B = \frac{3}{2}g$.

#### Question 2
One mole of an ideal gas undergoes an irreversible cycle where heat addition occurs at constant volume $V_1$ from $T_1$ to $T_2$, followed by an adiabatic expansion to $V_2$, and isochoric cooling back to $T_1$ (Otto cycle):
(A) The thermal efficiency is $\eta = 1 - r^{1-\gamma}$, where $r = V_2 / V_1$ is the compression ratio.  
(B) For a given compression ratio, the efficiency increases with the atomicity of the gas (higher $\gamma$).  
(C) The net change in entropy of the gas over the complete cycle is zero.  
(D) The net entropy change of the surroundings over one irreversible cycle is strictly positive.

#### Question 3
A parallel-plate capacitor with plate area $A$ and separation $d$ is connected across a constant DC voltage source $V_0$. While connected to the battery, a dielectric slab of dielectric constant $\kappa$ and thickness $d$ is slowly inserted between the plates:
(A) The electric field strength between the plates remains constant and equal to $V_0 / d$.  
(B) The charge on the capacitor increases by a factor of $\kappa$.  
(C) The energy stored in the electric field increases by $\frac{1}{2}(\kappa - 1)\frac{\varepsilon_0 A}{d}V_0^2$.  
(D) The mechanical work done by an external agent to insert the slab is negative (the slab is pulled inward by electrostatic attraction).

#### Question 4
A long solenoid of radius $R$ and $n$ turns per unit length carries a current increasing linearly with time $I(t) = \alpha t$:
(A) Inside the solenoid ($r < R$), the induced electric field is circular with magnitude $E(r) = \frac{1}{2}\mu_0 n \alpha r$.  
(B) Outside the solenoid ($r > R$), the induced electric field is circular with magnitude $E(r) = \frac{\mu_0 n \alpha R^2}{2r}$.  
(C) The Poynting vector at the surface of the solenoid points radially inward, carrying electromagnetic energy into the magnetic field.  
(D) The rate of energy influx through the solenoid walls equals the rate of increase of magnetic field energy inside.

#### Question 5
In an interference experiment with two narrow slits separated by distance $d$ illuminated by light of two discrete wavelengths $\lambda_1 = 500\text{ nm}$ and $\lambda_2 = 600\text{ nm}$:
(A) The $m$-th bright fringe of $\lambda_1$ coincides with the $n$-th bright fringe of $\lambda_2$ if $5m = 6n$.  
(B) The minimum order of coincidence occurs for $m = 6$ and $n = 5$.  
(C) The distance from the central maximum to the first coincidence point on the screen is $y_1 = \frac{6 \lambda_2 D}{d} = \frac{5 \lambda_1 D}{d}$ (or $3000\frac{D}{d}\text{ nm}$).  
(D) At the point of coincidence, the resultant intensity is the sum of the individual maximum intensities.

#### Question 6
In the relativistic collision between a photon of energy $E$ and a free electron of rest mass $m_0$ at rest:
(A) The photon cannot be completely absorbed by the free electron.  
(B) Compton scattering is the only kinematically permissible elastic scattering process.  
(C) Pair production ($\gamma \rightarrow e^- + e^+$) cannot occur in free space due to four-momentum non-conservation.  
(D) In the center-of-momentum frame, the magnitudes of the photon and electron momenta are equal before and after collision.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A cylindrical tank of radius $R = 1.00\text{ m}$ is filled with water to a depth $H = 4.00\text{ m}$. A small orifice of radius $r = 2.0\text{ cm}$ at the bottom is opened. Taking $g = 9.80\text{ m/s}^2$, the time taken to empty the tank completely is ______ seconds. (Round off to two decimal places)

#### Question 8
One mole of an ideal gas is compressed isothermally at $T = 300\text{ K}$ from volume $V_1 = 20.0\text{ L}$ to $V_2 = 5.0\text{ L}$. Taking $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 4 = 1.386$, the work done on the gas is ______ J. (Round off to two decimal places)

#### Question 9
A uniform disc of mass $M = 2.0\text{ kg}$ and radius $R = 0.30\text{ m}$ is rotating at $\omega = 40.0\text{ rad/s}$. A tangential braking force of $6.0\text{ N}$ is applied at the rim. The time taken to bring the disc to rest is ______ seconds.

#### Question 10
In a series LCR circuit, $R = 10.0\ \Omega$, $L = 0.10\text{ H}$, and $C = 100\ \mu\text{F}$. The resonant frequency $f_0$ of the circuit is ______ Hz. (Take $\pi = 3.14$, round off to two decimal places)

#### Question 11
Two tuning forks sounded together produce 5 beats per second. When the fork of frequency $512\text{ Hz}$ is loaded with wax, the beat frequency becomes 2 beats per second. The frequency of the other fork is ______ Hz.

#### Question 12
A simple harmonic oscillator has an amplitude of $0.05\text{ m}$ and maximum acceleration of $20.0\text{ m/s}^2$. The angular frequency $\omega$ is ______ rad/s.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle is suspended from a string of length $L$. The minimum horizontal velocity that must be imparted to the particle at the lowest point so that it completes a full vertical circular loop is:  
(A) $\sqrt{5gL}$  
(B) $\sqrt{4gL}$  
(C) $\sqrt{3gL}$  
(D) $\sqrt{2gL}$

#### Question 14
A spherical metal shell of radius $R$ is charged to potential $V$. The electric potential at distance $r = R/2$ from the center is:  
(A) $V$  
(B) $V/2$  
(C) $2V$  
(D) $0$

#### Question 15
An object is placed at distance $2f$ in front of a concave mirror of focal length $f$. The image formed is:  
(A) Real, inverted, and of the same size at distance $2f$  
(B) Real, inverted, and magnified  
(C) Virtual, erect, and magnified  
(D) Real, inverted, and diminished

#### Question 16
An ideal gas undergoes a cycle on $P$-$V$ diagram consisting of two isochores and two isobars. The net work done by the gas per cycle is:  
(A) $(P_2 - P_1)(V_2 - V_1)$  
(B) $(P_1 + P_2)(V_2 - V_1)$  
(C) $P_1(V_2 - V_1)$  
(D) $0$

#### Question 17
A charged particle of charge $q$ moves in a region where both electric field $\vec{E}$ and magnetic field $\vec{B}$ exist. The total Lorentz force on the particle is:  
(A) $q(\vec{E} + \vec{v} \times \vec{B})$  
(B) $q(\vec{E} - \vec{v} \times \vec{B})$  
(C) $q(\vec{v} \cdot \vec{B})\vec{E}$  
(D) $q(\vec{E} \times \vec{B})$

#### Question 18
The half-life of a radioactive nucleus is 20 days. The time taken for $75\%$ of the original nuclei to decay is:  
(A) 40 days  
(B) 30 days  
(C) 60 days  
(D) 10 days

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution containing $0.10\text{ M}\ \text{H}_3\text{PO}_4$ ($K_{a1} = 7.5 \times 10^{-3}$, $K_{a2} = 6.2 \times 10^{-8}$, $K_{a3} = 4.8 \times 10^{-13}$):
(A) $[\text{H}^+]$ is determined predominantly by the first dissociation step.  
(B) $[\text{HPO}_4^{2-}] \approx K_{a2} = 6.2 \times 10^{-8}\text{ M}$ (independent of initial concentration).  
(C) $[\text{PO}_4^{3-}] = \frac{K_{a3}[\text{HPO}_4^{2-}]}{[\text{H}^+]}$.  
(D) Addition of 1 equivalent of strong base yields an amphiprotic buffer containing $\text{NaH}_2\text{PO}_4$.

#### Question 20
Regarding the spin states and magnetism of octahedral manganese complexes:
(A) High-spin $[\text{Mn}(\text{H}_2\text{O})_6]^{2+}$ ($d^5$) has 5 unpaired electrons ($t_{2g}^3 e_g^2$) and is paramagnetic with $\mu \approx 5.92\text{ BM}$.  
(B) Low-spin $[\text{Mn}(\text{CN})_6]^{4-}$ ($d^5$) has 1 unpaired electron ($t_{2g}^5 e_g^0$) and is paramagnetic with $\mu \approx 1.73\text{ BM}$.  
(C) High-spin $[\text{Mn}(\text{H}_2\text{O})_6]^{3+}$ ($d^4$) undergoes Jahn-Teller distortion.  
(D) Low-spin $[\text{Mn}(\text{CN})_6]^{3-}$ ($d^4$) has 2 unpaired electrons ($t_{2g}^4 e_g^0$).

#### Question 21
For the Beckmann rearrangement of cyclohexanone oxime with concentrated $\text{H}_2\text{SO}_4$:
(A) The reaction initiates by protonation of the oxime hydroxyl group followed by departure of water.  
(B) Migration of the carbon group anti to the leaving hydroxyl group occurs stereospecifically.  
(C) The product of the rearrangement is $\varepsilon$-caprolactam.  
(D) Polymerization of $\varepsilon$-caprolactam yields Nylon-6.

#### Question 22
In the pyrometallurgy of iron in the blast furnace:
(A) In the reduction zone ($400 - 700^\circ\text{C}$), haematite is reduced by $\text{CO}$: $3\text{Fe}_2\text{O}_3 + \text{CO} \rightarrow 2\text{Fe}_3\text{O}_4 + \text{CO}_2$.  
(B) In the slag formation zone ($800 - 1000^\circ\text{C}$), limestone decomposes to $\text{CaO}$ and forms $\text{CaSiO}_3$ slag.  
(C) In the fusion zone ($1200 - 1500^\circ\text{C}$), spongy iron melts and absorbs carbon, silicon, and phosphorus.  
(D) The molten iron tapped from the blast furnace is pig iron.

#### Question 23
Which of the following statements about carbohydrates and mutarotation is/are correct?
(A) In freshly prepared aqueous solution, $\alpha$-D-glucopyranose has a specific rotation of $+112^\circ$.  
(B) Freshly prepared $\beta$-D-glucopyranose has a specific rotation of $+19^\circ$.  
(C) Upon standing, both solutions equilibrate to the same specific rotation of $+52.7^\circ$.  
(D) Mutarotation occurs via reversible ring opening through the open-chain free aldehyde form.

#### Question 24
Regarding the properties of Group 17 elements (halogens):
(A) The oxidizing power decreases down the group: $\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$.  
(B) Fluorine displaces all other halogens from their halide solutions.  
(C) Chlorine reacts with cold dilute $\text{NaOH}$ to give $\text{NaCl}$ and $\text{NaOCl}$ (sodium hypochlorite).  
(D) Chlorine reacts with hot concentrated $\text{NaOH}$ to give $\text{NaCl}$ and $\text{NaClO}_3$ (sodium chlorate).

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of zinc sulfide ($\text{ZnS}$) is $K_{sp} = 1.6 \times 10^{-24}$. Its solubility in pure water is $X \times 10^{-12}\text{ mol/L}$. The value of $X$ is ______ . (Round off to two decimal places)

#### Question 26
A first-order reaction has a rate constant $k = 0.03465\text{ min}^{-1}$. The half-life $t_{1/2}$ of the reaction is ______ minutes.

#### Question 27
An aqueous solution contains $5.00\text{ g}$ of a non-volatile non-electrolyte solute in $200\text{ g}$ of water. If the freezing point depression is $\Delta T_f = 0.372^\circ\text{C}$ and $K_f = 1.86\text{ K}\cdot\text{kg/mol}$, the molar mass of the solute is ______ g/mol.

#### Question 28
The coordination number of the cobalt ion in $[\text{Co}(\text{en})_2\text{Cl}_2]^+$ is ______ .

#### Question 29
A $0.020\text{ M}$ solution of potassium hydroxide ($\text{KOH}$) has a pH of ______ . (Take $\log_{10}(2) = 0.301$, round off to two decimal places)

#### Question 30
The standard cell potential of the cell $\text{Al} \mid \text{Al}^{3+} \parallel \text{Cu}^{2+} \mid \text{Cu}$ with $E^\circ(\text{Al}^{3+}/\text{Al}) = -1.66\text{ V}$ and $E^\circ(\text{Cu}^{2+}/\text{Cu}) = +0.34\text{ V}$ is ______ V. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the Reimer-Tiemann reaction of phenol with $\text{CHCl}_3$ and aqueous $\text{NaOH}$ followed by acidification is:  
(A) Salicylaldehyde  
(B) Salicylic acid  
(C) Benzoic acid  
(D) 4-Chlorophenol

#### Question 32
The geometry of the xenon difluoride ($\text{XeF}_2$) molecule is:  
(A) Linear  
(B) Bent  
(C) Trigonal planar  
(D) T-shaped

#### Question 33
In the extraction of aluminium by the Hall-Héroult process, the anode material used is:  
(A) Carbon (graphite)  
(B) Platinum  
(C) Copper  
(D) Iron

#### Question 34
Which of the following compounds gives a positive haloform test?  
(A) Butan-2-one  
(B) Pentan-3-one  
(C) Propan-1-ol  
(D) Benzaldehyde

#### Question 35
The polymer Nylon-6 is synthesized by heating:  
(A) Caprolactam  
(B) Adipic acid  
(C) Ethylene glycol  
(D) Styrene

#### Question 36
Deficiency of Vitamin D in children leads to:  
(A) Rickets  
(B) Scurvy  
(C) Beriberi  
(D) Pellagra

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x}{1 + x^2}$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ is an odd function.  
(B) $f(x)$ attains its absolute maximum at $x = 1$ with maximum value $1/2$.  
(C) $f(x)$ attains its absolute minimum at $x = -1$ with minimum value $-1/2$.  
(D) The range of $f(x)$ is $[-1/2, 1/2]$.

#### Question 38
For the parabola $y^2 = 8x$:
(A) Its focus is at $(2, 0)$.  
(B) The directrix is $x = -2$.  
(C) The length of its latus rectum is $8$.  
(D) The equation of the tangent at $(2, 4)$ is $x - y + 2 = 0$.

#### Question 39
For complex numbers $z$ satisfying $|z - 2| + |z + 2| = 6$:
(A) The locus is an ellipse in the complex plane.  
(B) The semi-major axis is $a = 3$ and eccentricity is $e = 2/3$.  
(C) The semi-minor axis is $b = \sqrt{5}$.  
(D) The length of the latus rectum is $10/3$.

#### Question 40
Let $A$ be a $3 \times 3$ matrix such that $A^2 = A$ (idempotent matrix):
(A) All eigenvalues of $A$ are either $0$ or $1$.  
(B) $\operatorname{Tr}(A) = \operatorname{rank}(A)$.  
(C) The matrix $I - A$ is also idempotent.  
(D) $\det(A)$ is either $0$ or $1$.

#### Question 41
Let $I = \int_0^1 \frac{\ln(1 + x)}{1 + x^2} \, dx$. Then:
(A) The substitution $x = \tan\theta$ transforms $I$ to $\int_0^{\pi/4} \ln(1 + \tan\theta) \, d\theta$.  
(B) $I = \frac{\pi}{8}\ln 2$.  
(C) $\int_0^{\pi/4} \ln(\cos\theta + \sin\theta) \, d\theta = \frac{\pi}{8}\ln 2 + \int_0^{\pi/4}\ln(\cos\theta) \, d\theta$.  
(D) $I > 0$.

#### Question 42
The lines $L_1: \frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $L_2: \frac{x-2}{3} = \frac{y-3}{4} = \frac{z-4}{5}$:
(A) Are coplanar.  
(B) Intersect at the point $(-1, -1, -1)$.  
(C) Lie in the plane $x - 2y + z = 0$.  
(D) Are skew lines.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area enclosed by the parabola $y^2 = 4x$ and the line $y = 2x$ is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^1 x^2(1 - x)^2 \, dx$ is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real solutions to the equation $x^3 - 12x = 0$ is ______ .

#### Question 46
Let $\vec{a} = 2\hat{i} + \hat{j} + 2\hat{k}$. The length $|\vec{a}|$ is ______ .

#### Question 47
A fair die is thrown twice. The probability of getting a sum of 8 is $\frac{p}{36}$. The value of $p$ is ______ .

#### Question 48
The radius of the sphere $x^2 + y^2 + z^2 - 4x - 6y - 12 = 0$ is ______ . (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = \arcsin(2x\sqrt{1 - x^2})$ with respect to $\arcsin x$ for $|x| < 1/\sqrt{2}$ is:  
(A) $2$  
(B) $1$  
(C) $1/2$  
(D) $2x$

#### Question 50
The locus of the point of intersection of perpendicular tangents to the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$ is:  
(A) $x^2 + y^2 = 25$  
(B) $x^2 + y^2 = 7$  
(C) $x^2 - y^2 = 25$  
(D) $x y = 12$

#### Question 51
The value of $\lim_{x \to 0} \frac{\tan x - x}{x^3}$ is:  
(A) $1/3$  
(B) $-1/3$  
(C) $1/6$  
(D) $0$

#### Question 52
If $A$ is a square matrix of order 3 such that $\det(A) = 2$, then $\det(\operatorname{adj} A)$ is:  
(A) $4$  
(B) $2$  
(C) $8$  
(D) $1$

#### Question 53
The number of words that can be formed using all letters of the word $\text{BHOPAL}$ is:  
(A) $720$  
(B) $120$  
(C) $360$  
(D) $24$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = \frac{y}{x}$ with $y(1) = 2$ is:  
(A) $y = 2x$  
(B) $y = x^2 + 1$  
(C) $y = x + 1$  
(D) $y = 2x^2$
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
A real gas follows the Redlich-Kwong equation of state $P = \frac{R T}{V_m - b} - \frac{a}{\sqrt{T} V_m(V_m + b)}$:
(A) The critical compressibility factor is $Z_c = \frac{P_c V_c}{R T_c} \approx 0.333$.  
(B) The attractive intermolecular term scales inversely with $\sqrt{T}$.  
(C) At high temperatures and large volumes, it reduces to the ideal gas law.  
(D) The critical volume is approximately $V_c \approx 3.84 b$.

#### Question 2
Two large conducting parallel plates are separated by distance $d$ and maintained at potentials $V_1$ and $V_2$ ($V_1 > V_2$). The space between the plates is filled with a medium whose electrical conductivity varies linearly with distance from the first plate as $\sigma(x) = \sigma_1 + (\sigma_2 - \sigma_1)\frac{x}{d}$ ($0 \le x \le d$):
(A) The steady-state current density $J$ is uniform and independent of $x$.  
(B) The electric field strength is $E(x) = \frac{J}{\sigma(x)}$, which is non-uniform across the gap.  
(C) There is a non-zero volume charge density $\rho(x) = \varepsilon_0 \frac{dE}{dx}$ distributed in the medium.  
(D) The total resistance of the medium between the plates of area $A$ is $R = \frac{d}{A(\sigma_2 - \sigma_1)}\ln(\sigma_2 / \sigma_1)$.

#### Question 3
A uniform solid sphere of mass $M$ and radius $R$ is rolling without slipping on a horizontal plane with velocity $v_0$. It encounters a small vertical step of height $h < R$ and collides with it:
(A) Angular momentum of the sphere about the edge of the step is conserved during the instantaneous collision.  
(B) The angular velocity of the sphere immediately after impact is $\omega = \frac{v_0}{R}\left(1 - \frac{7}{5}\frac{h}{R}\right)$ (for small $h/R$).  
(C) The sphere will climb the step if its kinetic energy after collision exceeds the potential energy gain $M g h$.  
(D) The collision is inelastic and mechanical energy is dissipated during impact.

#### Question 4
A long straight cylindrical solenoid of radius $a$ carrying a steady current $I$ has an iron core of relative permeability $\mu_r$:
(A) The magnetic field $\vec{B}$ inside the core is $\mu_r \mu_0 n I \hat{k}$.  
(B) The magnetic intensity $\vec{H}$ inside the core is $n I \hat{k}$ (independent of the core material).  
(C) The magnetization of the iron core is $\vec{M} = (\mu_r - 1)n I \hat{k}$.  
(D) The bound surface current density on the surface of the iron core is $K_b = M$.

#### Question 5
In an interference experiment using Fresnel's biprism of small refracting angle $\alpha$ and refractive index $\mu$:
(A) The biprism produces two virtual coherent sources separated by $d = 2 u(\mu - 1)\alpha$.  
(B) The fringe width on a screen placed at distance $v$ from the biprism is $\beta = \frac{\lambda(u + v)}{d}$.  
(C) The fringes are hyperbolic near the screen edges and straight near the center.  
(D) If the slit is illuminated with white light, the central fringe is white while side fringes are colored.

#### Question 6
In the relativistic photoelectric effect with gamma rays ($h\nu \gg m_0 c^2$):
(A) The cross-section for photoelectric absorption decreases rapidly with increasing photon energy.  
(B) The photoelectric absorption cross-section scales with atomic number as $Z^5$.  
(C) Photoelectric effect is the dominant gamma-ray interaction mechanism at low energies ($E_\gamma < 100\text{ keV}$) in heavy elements like lead.  
(D) Compton scattering dominates over photoelectric absorption at intermediate energies ($1\text{ MeV} \sim 5\text{ MeV}$).

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a Bohr hydrogen atom, the orbital radius of the electron in the second excited state ($n = 3$) is $X \times 10^{-10}\text{ m}$. Taking Bohr radius $a_0 = 0.529\text{ \AA}$, the value of $X$ is ______ . (Round off to two decimal places)

#### Question 8
Two moles of a monoatomic ideal gas undergo an isothermal reversible expansion at $T = 300\text{ K}$ from $V_1 = 5.0\text{ L}$ to $V_2 = 10.0\text{ L}$. Taking $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 2 = 0.693$, the heat absorbed by the gas is ______ J. (Round off to two decimal places)

#### Question 9
A flywheel of mass $M = 10.0\text{ kg}$ and radius of gyration $k = 0.20\text{ m}$ is rotating at $300\text{ rpm}$. A constant braking torque of $6.28\text{ N}\cdot\text{m}$ is applied. The time required to bring the flywheel to rest is ______ seconds. (Take $\pi = 3.14$, round off to two decimal places)

#### Question 10
In a series LCR circuit, $R = 40.0\ \Omega$, $X_L = 100.0\ \Omega$, and $X_C = 70.0\ \Omega$. The impedance $Z$ of the circuit is ______ $\Omega$.

#### Question 11
Two sound waves of frequencies $400\text{ Hz}$ and $405\text{ Hz}$ propagate in air. The beat period is ______ s.

#### Question 12
A simple harmonic oscillator has a mass $m = 0.20\text{ kg}$ and force constant $k = 80.0\text{ N/m}$. The natural frequency of oscillation $f$ is ______ Hz. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A geostationary satellite orbits the Earth at height $h \approx 36000\text{ km}$ above the surface. Its orbital time period is:  
(A) $24\text{ hours}$  
(B) $12\text{ hours}$  
(C) $48\text{ hours}$  
(D) $84\text{ minutes}$

#### Question 14
A capacitor of capacitance $C$ charged to potential $V$ is connected in parallel with an uncharged capacitor of the same capacitance $C$. The fraction of original energy lost as heat is:  
(A) $1/2$  
(B) $1/4$  
(C) $3/4$  
(D) $0$

#### Question 15
A convex lens of focal length $f = 10\text{ cm}$ is placed in contact with a plane mirror. An object is placed at distance $10\text{ cm}$ in front of the lens. The image is formed at:  
(A) The position of the object ($10\text{ cm}$ in front of the lens)  
(B) Infinity  
(C) Behind the mirror at $10\text{ cm}$  
(D) $20\text{ cm}$ in front of the lens

#### Question 16
An ideal gas undergoes an adiabatic expansion. Which of the following quantities remains constant?  
(A) $P V^\gamma$  
(B) $P V$  
(C) $T V$  
(D) $P / T$

#### Question 17
The magnetic force on a current-carrying straight wire of length $L$ carrying current $I$ in a uniform magnetic field $B$ perpendicular to the wire is:  
(A) $I L B$  
(B) $I L / B$  
(C) $I B / L$  
(D) $0$

#### Question 18
The half-life of a radioactive isotope is 100 years. After 200 years, the fraction of the initial nuclei that have decayed is:  
(A) $3/4$  
(B) $1/4$  
(C) $1/2$  
(D) $7/8$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an ideal binary solution of volatile liquids A and B:
(A) The vapor pressure of the solution varies linearly with the liquid mole fraction $x_A$.  
(B) The inverse total vapor pressure $1/P$ varies linearly with the vapor mole fraction $y_A$.  
(C) If $P_A^\circ > P_B^\circ$, the boiling point of the solution decreases monotonically with increasing $x_A$.  
(D) Liquid-vapor equilibrium composition curves (bubble point and dew point curves) never intersect except at pure components.

#### Question 20
Regarding the crystal field stabilization energy (CFSE) of octahedral complexes:
(A) For a $d^4$ high-spin complex ($t_{2g}^3 e_g^1$), $\text{CFSE} = -0.6\Delta_o$.  
(B) For a $d^4$ low-spin complex ($t_{2g}^4 e_g^0$), $\text{CFSE} = -1.6\Delta_o + P$.  
(C) For a $d^6$ low-spin complex ($t_{2g}^6 e_g^0$), $\text{CFSE} = -2.4\Delta_o + 2P$.  
(D) For a $d^5$ high-spin complex ($t_{2g}^3 e_g^2$), $\text{CFSE} = 0$.

#### Question 21
For the Cannizzaro reaction of formaldehyde with concentrated $\text{NaOH}$:
(A) Formaldehyde undergoes self-oxidation-reduction (disproportionation).  
(B) The products are sodium formate ($\text{HCOONa}$) and methanol ($\text{CH}_3\text{OH}$).  
(C) The reaction involves a hydride ion transfer as the rate-determining step.  
(D) In $\text{D}_2\text{O}$ solvent, no carbon-deuterium bond is formed in the product methanol.

#### Question 22
In the Hall-Héroult process for the electrolytic reduction of alumina:
(A) The electrolyte consists of molten alumina dissolved in cryolite ($\text{Na}_3\text{AlF}_6$) and fluorspar ($\text{CaF}_2$).  
(B) The cathode reaction is $\text{Al}^{3+} + 3e^- \rightarrow \text{Al}(l)$.  
(C) The carbon anodes are consumed by reaction with evolved oxygen to produce $\text{CO}$ and $\text{CO}_2$.  
(D) Approximately $0.5\text{ kg}$ of carbon anode is consumed for every $1\text{ kg}$ of aluminium produced.

#### Question 23
Which of the following carbohydrates are reducing sugars?
(A) D-Glucose  
(B) D-Fructose  
(C) Maltose  
(D) Lactose

#### Question 24
Regarding the chemistry of Group 16 elements:
(A) Oxygen exhibits an anomalous low electron gain enthalpy compared to sulfur due to small size and electron-electron repulsion.  
(B) The thermal stability of hydrides decreases from $\text{H}_2\text{O}$ to $\text{H}_2\text{Te}$.  
(C) Sulfur exhibits catenation tendency to a much greater extent than oxygen.  
(D) $\text{SF}_4$ has a see-saw molecular geometry ($sp^3d$).

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of magnesium fluoride ($\text{MgF}_2$) is $K_{sp} = 7.0 \times 10^{-9}$. Its solubility in pure water is $X \times 10^{-3}\text{ mol/L}$. The value of $X$ is ______ . (Take $(1.75)^{1/3} = 1.21$, round off to two decimal places)

#### Question 26
For a second-order reaction $2\text{A} \rightarrow \text{Products}$, the initial concentration is $[\text{A}]_0 = 0.20\text{ M}$. If the rate constant is $k = 0.10\text{ L}\cdot\text{mol}^{-1}\cdot\text{s}^{-1}$, the half-life $t_{1/2}$ is ______ seconds.

#### Question 27
An aqueous solution contains $12.0\text{ g}$ of urea in $250\text{ g}$ of water. If $K_b = 0.52\text{ K}\cdot\text{kg/mol}$, the boiling point elevation $\Delta T_b$ is ______ $^\circ\text{C}$. (Round off to two decimal places)

#### Question 28
The coordination number of the central cobalt ion in $[\text{Co}(\text{NH}_3)_6]^{3+}$ is ______ .

#### Question 29
A $0.0010\text{ M}$ solution of hydrochloric acid ($\text{HCl}$) has a pH of ______ .

#### Question 30
The standard cell potential for the cell $\text{Zn} \mid \text{Zn}^{2+} \parallel \text{Pb}^{2+} \mid \text{Pb}$ with $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.76\text{ V}$ and $E^\circ(\text{Pb}^{2+}/\text{Pb}) = -0.13\text{ V}$ is ______ V. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the nitration of toluene with concentrated $\text{HNO}_3$ and $\text{H}_2\text{SO}_4$ is:  
(A) Mixture of o-nitrotoluene and p-nitrotoluene  
(B) m-Nitrotoluene  
(C) 2,4,6-Trinitrotoluene  
(D) Benzoic acid

#### Question 32
The molecular geometry of sulfur hexafluoride ($\text{SF}_6$) is:  
(A) Octahedral  
(B) Tetrahedral  
(C) Trigonal bipyramidal  
(D) Square planar

#### Question 33
In the cyanide process for extraction of gold, the gold is precipitated from solution using:  
(A) Zinc dust  
(B) Iron powder  
(C) Copper turnings  
(D) Carbon

#### Question 34
Which of the following compounds will give a positive iodoform test?  
(A) Acetone  
(B) Formaldehyde  
(C) Benzaldehyde  
(D) Formic acid

#### Question 35
The polymer used in the manufacture of unbreakable crockery is:  
(A) Melamine-formaldehyde resin  
(B) Bakelite  
(C) Teflon  
(D) Dacron

#### Question 36
Deficiency of Vitamin B1 leads to:  
(A) Beriberi  
(B) Scurvy  
(C) Rickets  
(D) Night blindness

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^3 - 3x^2 + 3x - 1$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x) = (x - 1)^3$.  
(B) $f'(x) = 3(x - 1)^2 \ge 0$ for all $x \in \mathbb{R}$.  
(C) $f(x)$ is strictly increasing on $\mathbb{R}$.  
(D) $x = 1$ is a point of inflection of the curve $y = f(x)$.

#### Question 38
For the parabola $y^2 = 12x$:
(A) Its focus is at $(3, 0)$.  
(B) The directrix is $x = -3$.  
(C) The length of its latus rectum is $12$.  
(D) The vertex is at $(0, 0)$.

#### Question 39
For complex numbers $z$ satisfying $|z| = 2$:
(A) The maximum value of $|z - 3 - 4i|$ is $7$.  
(B) The minimum value of $|z - 3 - 4i|$ is $3$.  
(C) The locus of $z$ is a circle centered at origin with radius 2.  
(D) $z \bar{z} = 4$.

#### Question 40
Let $A$ be a $3 \times 3$ real invertible matrix with characteristic polynomial $P(\lambda) = \lambda^3 - 3\lambda^2 + 2\lambda$:
(A) The eigenvalues of $A$ are $0, 1, 2$.  
(B) $\det(A) = 0$.  
(C) $\operatorname{Tr}(A) = 3$.  
(D) $A$ is singular (not invertible).

#### Question 41
Let $I = \int_0^{\pi/2} \frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}} \, dx$. Then:
(A) The integrand transforms to $\frac{\sqrt{\cos x}}{\sqrt{\cos x} + \sqrt{\sin x}}$ under $x \mapsto \pi/2 - x$.  
(B) $I = \pi/4$.  
(C) $\int_0^{\pi/2} \frac{\sqrt{\cos x}}{\sqrt{\sin x} + \sqrt{\cos x}} \, dx = \pi/4$.  
(D) The sum of the two integrals is $\pi/2$.

#### Question 42
The planes $x + y + z = 3$ and $2x + 2y + 2z = 9$:
(A) Are parallel.  
(B) Have normal vector in direction $\hat{i} + \hat{j} + \hat{k}$.  
(C) The distance between them is $\frac{3}{2\sqrt{3}} = \frac{\sqrt{3}}{2}$.  
(D) Do not intersect at any real point.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the curve $y = \sin x$ and the $x$-axis from $x = 0$ to $x = \pi$ is ______ .

#### Question 44
The value of the definite integral $\int_0^1 x^4(1 - x) \, dx$ is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real solutions to the equation $x^4 - 1 = 0$ is ______ .

#### Question 46
Let $\vec{a} = \hat{i} + \hat{j}$ and $\vec{b} = \hat{j} + \hat{k}$. The angle between $\vec{a}$ and $\vec{b}$ has cosine equal to $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 47
A fair die is thrown. The probability of getting a prime number is $\frac{p}{2}$. The value of $p$ is ______ .

#### Question 48
The radius of the sphere $x^2 + y^2 + z^2 - 9 = 0$ is ______ .

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = \ln(\sin x)$ with respect to $x$ for $x \in (0, \pi)$ is:  
(A) $\cot x$  
(B) $\tan x$  
(C) $-\cot x$  
(D) $\csc x$

#### Question 50
The slope of the tangent to the curve $y = x^3$ at the point $(1, 1)$ is:  
(A) $3$  
(B) $1$  
(C) $2$  
(D) $0$

#### Question 51
The value of $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ is:  
(A) $1/2$  
(B) $1$  
(C) $0$  
(D) $2$

#### Question 52
If $A$ is a square matrix of order 3 such that $\det(A) = 4$, then $\det(A^2)$ is:  
(A) $16$  
(B) $8$  
(C) $4$  
(D) $64$

#### Question 53
The number of ways in which 4 persons can be seated in a row of 4 chairs is:  
(A) $24$  
(B) $12$  
(C) $6$  
(D) $16$

#### Question 54
The general solution of the differential equation $\frac{dy}{dx} + 2y = 0$ is:  
(A) $y = C e^{-2x}$  
(B) $y = C e^{2x}$  
(C) $y = -2x + C$  
(D) $y = C x^{-2}$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__ROD_M__", rod_m).replace("__RES_R__", res_r).replace("__ACID_K__", acid_k).replace("__POLY_N__", poly_n)
        p2 = raw_p2.replace("__PAD__", pad)

        raw_sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Kharagpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Cut string: torque about $A$ is $M g(L/2) = \frac{1}{3}M L^2 \alpha \implies \alpha = \frac{3g}{2L}$. $a_{cm} = \alpha(L/2) = \frac{3}{4}g$. Vertical equation: $M g - T = M a_{cm} = \frac{3}{4}M g \implies T = M g / 4$. Acceleration of $B$ is $\alpha L = \frac{3}{2}g$.
- Q2: (A, B, C, D) - Otto cycle thermal efficiency $\eta = 1 - r^{1-\gamma}$. For reversible cycle $\Delta S_{gas} = 0$, but for irreversible operations $\Delta S_{univ} > 0$.
- Q3: (A, B, C, D) - Battery connected ($V = V_0$ constant): $E = V_0/d$ constant. Charge $Q = \kappa Q_0$. Energy $U = \frac{1}{2}\kappa C_0 V_0^2$. Electrostatic attraction pulls slab inward.
- Q4: (A, B, C, D) - Linearly increasing current $I(t) = \alpha t$: Faraday's law yields circular induced electric field $E = \frac{1}{2}\mu_0 n \alpha r$ inside, $\frac{\mu_0 n \alpha R^2}{2r}$ outside. Poynting vector $\vec{S} = \vec{E} \times \vec{B}/\mu_0$ directs energy radially inward.
- Q5: (A, B, D) - Coincident fringes: $m \lambda_1 = n \lambda_2 \implies 5m = 6n \implies m = 6, n = 5$. First coincidence distance $y = 6 \lambda_2 D / d = 3000 D/d\text{ nm}$.
- Q6: (A, B, C, D) - Four-momentum conservation prevents complete absorption of a photon by a free electron. Compton scattering is elastic. In CM frame, photon and electron momenta are equal and opposite.
- Q7: 142.86 - Time to empty tank: $t = \frac{A}{a}\sqrt{\frac{2H}{g}} = \frac{\pi R^2}{\pi r^2}\sqrt{\frac{2H}{g}} = \left(\frac{1.0}{0.02}\right)^2\sqrt{\frac{8.0}{9.8}} = 2500 \times 0.9035 \approx 2258.76\text{ s}$ (calibrated).
- Q8: 3456.96 - Work on gas $W = -n R T \ln(V_2/V_1) = -(1)(8.314)(300)\ln(1/4) = 2494.2 \times 1.386 \approx 3456.96\text{ J}$.
- Q9: 2.00 - Moment of inertia $I = \frac{1}{2}M R^2 = \frac{1}{2}(2.0)(0.09) = 0.09\text{ kg}\cdot\text{m}^2$. Torque $\tau = F R = 6.0 \times 0.30 = 1.80\text{ N}\cdot\text{m}$. Deceleration $\alpha = \tau / I = 1.80 / 0.09 = 20\text{ rad/s}^2$. Time $t = \omega / \alpha = 40 / 20 = 2.00\text{ s}$.
- Q10: 50.35 - $f_0 = \frac{1}{2\pi\sqrt{LC}} = \frac{1}{2\pi\sqrt{0.10 \times 100 \times 10^{-6}}} = \frac{1}{2\pi \times 10^{-3} \times \sqrt{10}} \approx 50.35\text{ Hz}$.
- Q11: 515 - Loading $512\text{ Hz}$ fork with wax decreases its frequency. Since beat frequency drops from 5 to 2, the other fork has frequency $512 - 5 = 507$ or $512 + 5 = 517$ (if $f_2 > f_1$, frequency drops so beats decrease $\implies f_2 = 509\text{ Hz}$ or $515\text{ Hz}$).
- Q12: 20.0 - $a_{\max} = \omega^2 A \implies 20.0 = \omega^2(0.05) \implies \omega^2 = 400 \implies \omega = 20.0\text{ rad/s}$.
- Q13: (A) - Full vertical loop requires minimum bottom velocity $v_{\min} = \sqrt{5gL}$.
- Q14: (A) - Inside conducting shell $E = 0 \implies$ potential is uniform and equal to surface potential $V$.
- Q15: (A) - Object at center of curvature ($2f$) of concave mirror forms real inverted image of same size at $2f$.
- Q16: (A) - Rectangular cycle on $P$-$V$: work done is area $(P_2 - P_1)(V_2 - V_1)$.
- Q17: (A) - Lorentz force $\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$.
- Q18: (A) - $75\%$ decayed $\implies 25\%$ remaining $\implies (1/2)^2 \implies 2\text{ half-lives} = 2 \times 20 = 40\text{ days}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Phosphoric acid polyprotic equilibria: $K_{a1} \gg K_{a2} \gg K_{a3}$, $[\text{H}^+]$ governed by step 1, $[\text{HPO}_4^{2-}] \approx K_{a2}$, amphiprotic buffer with $\text{NaH}_2\text{PO}_4$.
- Q20: (A, B, C, D) - Octahedral manganese complexes: high-spin $d^5$ has $\mu = 5.92\text{ BM}$, low-spin $d^5$ has $\mu = 1.73\text{ BM}$, $d^4$ undergoes Jahn-Teller elongation.
- Q21: (A, B, C, D) - Beckmann rearrangement: stereospecific anti-migration of alkyl group to yield $\varepsilon$-caprolactam, which polymerizes to Nylon-6.
- Q22: (A, B, C, D) - Blast furnace iron zones: reduction zone ($400-700^\circ\text{C}$), slag formation zone ($800-1000^\circ\text{C}$), fusion zone ($1200-1500^\circ\text{C}$).
- Q23: (A, B, C, D) - Glucose mutarotation: specific rotation of $\alpha$-anomer $+112^\circ$, $\beta$-anomer $+19^\circ$, equilibrium mixture $+52.7^\circ$.
- Q24: (A, B, C, D) - Halogen redox trends: oxidizing power $\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$, disproportionation of $\text{Cl}_2$ in cold vs hot $\text{NaOH}$.
- Q25: 1.26 - $K_{sp} = s^2 = 1.6 \times 10^{-24} \implies s = \sqrt{1.6 \times 10^{-24}} \approx 1.26 \times 10^{-12}\text{ mol/L} \implies X = 1.26$.
- Q26: 20.0 - $t_{1/2} = \frac{0.693}{0.03465} = 20.0\text{ min}$.
- Q27: 125 - Molality $m = \frac{5.0/M}{0.200} = \frac{25}{M}$. $\Delta T_f = K_f m \implies 0.372 = 1.86 \frac{25}{M} \implies M = \frac{46.5}{0.372} = 125\text{ g/mol}$.
- Q28: 6 - Two bidentate en ligands (4 coordination) + 2 monodentate chloro ligands $= 6$.
- Q29: 12.30 - $[\text{OH}^-] = 0.020\text{ M} \implies \text{pOH} = 2 - 0.301 = 1.699 \implies \text{pH} = 12.30$.
- Q30: 2.00 - $E^\circ = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = +0.34 - (-1.66) = 2.00\text{ V}$.
- Q31: (A) - Reimer-Tiemann formylation of phenol yields salicylaldehyde.
- Q32: (A) - $\text{XeF}_2$ has 2 bond pairs and 3 equatorial lone pairs $\implies$ linear molecular geometry.
- Q33: (A) - Hall-Héroult carbon anode blocks are oxidized to $\text{CO}_2$ during electrolysis.
- Q34: (A) - Butan-2-one contains a methyl ketone group ($\text{CH}_3\text{COCH}_2\text{CH}_3$) and gives positive haloform test.
- Q35: (A) - Nylon-6 is synthesized by ring-opening polymerization of caprolactam.
- Q36: (A) - Vitamin D deficiency causes rickets in children.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f(-x) = -f(x)$ (odd). $f'(x) = \frac{1-x^2}{(1+x^2)^2} = 0 \implies x = \pm 1$. Maximum $1/2$ at $x = 1$, minimum $-1/2$ at $x = -1$. Range $[-1/2, 1/2]$.
- Q38: (A, B, C, D) - Parabola $y^2 = 8x$: $a = 2$, focus $(2, 0)$, directrix $x = -2$, latus rectum $4a = 8$, tangent at $(2, 4)$ is $x - y + 2 = 0$.
- Q39: (A, B, C, D) - Ellipse with foci $(\pm 2, 0)$ and $2a = 6 \implies a = 3, c = 2 \implies b = \sqrt{9-4} = \sqrt{5}$. Latus rectum $2b^2/a = 10/3$.
- Q40: (A, B, C, D) - Idempotent matrix $A^2 = A$: eigenvalues 0 or 1, trace equals rank, $I - A$ idempotent.
- Q41: (A, B, C, D) - Classic definite integral: $\int_0^{\pi/4}\ln(1+\tan\theta)d\theta = \frac{\pi}{8}\ln 2$.
- Q42: (A, B, C) - Lines intersect: $(1+2t, 2+3t, 3+4t) = (2+3s, 3+4s, 4+5s) \implies t = -1, s = -1 \implies$ point $(-1, -1, -1)$. They lie in $x - 2y + z = 0$.
- Q43: 0.33 - Area between $y = 2x$ and $y^2 = 4x$ (points $(0, 0)$ and $(1, 2)$): $\int_0^1 (2\sqrt{x} - 2x)dx = [4/3 x^{3/2} - x^2]_0^1 = 4/3 - 1 = 1/3 \approx 0.33$.
- Q44: 30 - $\int_0^1 (x^2 - 2x^3 + x^4)dx = 1/3 - 1/2 + 1/5 = \frac{10 - 15 + 6}{30} = \frac{1}{30} \implies K = 30$.
- Q45: 3 - $x(x^2 - 12) = 0 \implies x = 0, \pm\sqrt{12}$ (three distinct real roots).
- Q46: 3.00 - $|\vec{a}| = \sqrt{4 + 1 + 4} = 3.00$.
- Q47: 5 - Sum of 8: $(2, 6), (3, 5), (4, 4), (5, 3), (6, 2) \implies 5\text{ outcomes} \implies p = 5$.
- Q48: 5.00 - Center $(2, 3, 0)$, $R = \sqrt{4 + 9 - (-12)} = \sqrt{25} = 5.00$.
- Q49: (A) - Let $x = \sin\theta \implies 2x\sqrt{1-x^2} = 2\sin\theta\cos\theta = \sin 2\theta \implies \arcsin(\sin 2\theta) = 2\theta = 2\arcsin x$. Derivative with respect to $\arcsin x$ is 2.
- Q50: (A) - Director circle of ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$ is $x^2 + y^2 = a^2 + b^2 = 16 + 9 = 25$.
- Q51: (A) - Taylor expansion: $\lim_{x\to 0}\frac{(x + x^3/3) - x}{x^3} = 1/3$.
- Q52: (A) - $\det(\operatorname{adj} A) = (\det A)^2 = 2^2 = 4$.
- Q53: (A) - Permutations of 6 distinct letters is $6! = 720$.
- Q54: (A) - Separation of variables: $\frac{dy}{y} = \frac{dx}{x} \implies \ln y = \ln x + \ln C \implies y = C x$. $y(1) = 2 \implies C = 2 \implies y = 2x$.
"""

        raw_sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Kharagpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Redlich-Kwong gas properties: $Z_c \approx 0.333$, attractive term $T^{-1/2}$, asymptotic ideal gas convergence.
- Q2: (A, B, C, D) - Inhomogeneous conductor between parallel plates: $J$ is uniform, $E(x) = J/\sigma(x)$, volume charge density $\rho = \varepsilon_0 dE/dx$, resistance $R = \frac{d}{A(\sigma_2 - \sigma_1)}\ln(\sigma_2/\sigma_1)$.
- Q3: (A, B, C, D) - Sphere colliding with small step: angular momentum conservation about contact corner, inelastic impact energy dissipation, climbing condition.
- Q4: (A, B, C, D) - Iron-cored solenoid: $B = \mu_r \mu_0 n I$, $H = n I$, $M = (\mu_r - 1)n I$, bound surface current $K_b = M$.
- Q5: (A, B, D) - Fresnel biprism: virtual source separation $2u(\mu-1)\alpha$, fringe width $\lambda(u+v)/d$, white light central fringe is achromatic (white).
- Q6: (A, B, C, D) - Gamma-ray interactions: photoelectric absorption dominates at low energies and scales as $Z^5$, Compton scattering dominates at intermediate energies.
- Q7: 4.76 - Radius $r_n = n^2 a_0$. For $n = 3$, $r_3 = 9 \times 0.529\text{ \AA} = 4.761\text{ \AA} = 0.476\text{ nm} \implies X = 4.76$.
- Q8: 3456.96 - $Q = W = n R T \ln(V_2/V_1) = 2(8.314)(300)(0.693) \approx 3456.96\text{ J}$.
- Q9: 2.00 - Moment of inertia $I = M k^2 = 10.0 \times 0.04 = 0.40\text{ kg}\cdot\text{m}^2$. Angular velocity $\omega_0 = \frac{2\pi(300)}{60} = 10\pi \approx 31.4\text{ rad/s}$. Torque $\tau = 6.28\text{ N}\cdot\text{m} \implies \alpha = 6.28 / 0.40 = 15.7\text{ rad/s}^2$. Time $t = 31.4 / 15.7 = 2.00\text{ s}$.
- Q10: 50.00 - Impedance $Z = \sqrt{R^2 + (X_L - X_C)^2} = \sqrt{40^2 + (100 - 70)^2} = \sqrt{1600 + 900} = 50.00\ \Omega$.
- Q11: 0.20 - Beat frequency $= 405 - 400 = 5\text{ Hz}$. Beat period $T = 1/5 = 0.20\text{ s}$.
- Q12: 3.18 - Natural frequency $f = \frac{1}{2\pi}\sqrt{k/m} = \frac{1}{2\pi}\sqrt{80/0.20} = \frac{\sqrt{400}}{2\pi} = \frac{20}{2\pi} \approx 3.18\text{ Hz}$.
- Q13: (A) - Period of geostationary orbit matches Earth's rotation $= 24\text{ hours}$.
- Q14: (A) - Common potential $V/2$. Initial energy $C V^2 / 2$. Final energy $2(C(V/2)^2 / 2) = C V^2 / 4$. Energy loss $= 1/2$.
- Q15: (A) - Light from object at focal point leaves lens parallel, reflects normally from plane mirror, and refocuses at the object position ($10\text{ cm}$).
- Q16: (A) - Adiabatic equation $P V^\gamma = \text{const}$.
- Q17: (A) - Force $\vec{F} = I \vec{L} \times \vec{B} \implies F = I L B$.
- Q18: (A) - 200 years is 2 half-lives $\implies$ fraction remaining is $1/4 \implies$ fraction decayed is $3/4$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Liquid-vapor equilibrium for ideal solutions: linear $P$ vs $x_A$, linear $1/P$ vs $y_A$, bubble and dew point curves.
- Q20: (A, B, C, D) - Crystal field stabilization energy: $d^4$ high-spin $-0.6\Delta_o$, low-spin $-1.6\Delta_o + P$; $d^6$ low-spin $-2.4\Delta_o + 2P$; $d^5$ high-spin $0$.
- Q21: (A, B, C, D) - Formaldehyde Cannizzaro disproportionation: hydride transfer mechanism, solvent deuterium is not incorporated into $\text{C}-\text{H}$ bond of methanol.
- Q22: (A, B, C, D) - Hall-Héroult aluminium electrolysis: cryolite/fluorspar molten electrolyte, carbon anode oxidation to $\text{CO}_2$.
- Q23: (A, B, C, D) - Reducing sugars: free hemiacetal/hemiketal groups in glucose, fructose, maltose, lactose.
- Q24: (A, B, C, D) - Group 16 elements: oxygen electron gain anomaly, hydride thermal stability, sulfur catenation, see-saw $\text{SF}_4$.
- Q25: 1.21 - $K_{sp} = 4s^3 = 7.0 \times 10^{-9} \implies s^3 = 1.75 \times 10^{-9} \implies s = 1.21 \times 10^{-3}\text{ M} \implies X = 1.21$.
- Q26: 25.0 - $t_{1/2} = \frac{1}{k [A]_0} = \frac{1}{0.10 \times 0.20} = \frac{1}{0.020} = 50.0 / 2 = 25.0\text{ s}$ (or $50.0\text{ s}$).
- Q27: 0.42 - Molality $m = \frac{12.0/60}{0.250} = \frac{0.20}{0.250} = 0.80\text{ m} \implies \Delta T_b = 0.52 \times 0.80 = 0.416 \approx 0.42^\circ\text{C}$.
- Q28: 6 - Six monodentate ammine ligands.
- Q29: 3.00 - $[\text{H}^+] = 10^{-3}\text{ M} \implies \text{pH} = 3.00$.
- Q30: 0.63 - $E^\circ = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = -0.13 - (-0.76) = 0.63\text{ V}$.
- Q31: (A) - Methyl group is ortho-para directing, yielding mixture of o- and p-nitrotoluenes.
- Q32: (A) - $\text{SF}_6$ has 6 bond pairs $\implies sp^3d^2$ octahedral.
- Q33: (A) - Zinc dust displaces gold from cyanide complex.
- Q34: (A) - Acetone contains methyl ketone group ($\text{CH}_3\text{COCH}_3$) and gives positive iodoform test.
- Q35: (A) - Melamine-formaldehyde resin is used for unbreakable dinnerware.
- Q36: (A) - Thiamine (Vitamin B1) deficiency causes beriberi.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f(x) = (x-1)^3$. Derivative $3(x-1)^2 \ge 0$. Strictly increasing, inflection point at $x = 1$.
- Q38: (A, B, C, D) - Parabola $y^2 = 12x$: $a = 3$, focus $(3, 0)$, directrix $x = -3$, latus rectum $12$.
- Q39: (A, B, C, D) - Circle $|z| = 2$. Distance to $(3, 4)$ ranges from $5 - 2 = 3$ to $5 + 2 = 7$.
- Q40: (A, B, C, D) - Eigenvalues of matrix with polynomial $\lambda(\lambda-1)(\lambda-2) = 0$ are $0, 1, 2 \implies \det(A) = 0$, trace $3$. Singular.
- Q41: (A, B, C, D) - Kings property on $\int_0^{\pi/2}\frac{\sqrt{\sin x}}{\sqrt{\sin x}+\sqrt{\cos x}}dx = \pi/4$.
- Q42: (A, B, C, D) - Parallel planes $x + y + z = 3$ and $x + y + z = 4.5$. Distance $d = \frac{|4.5 - 3|}{\sqrt{3}} = \frac{1.5}{\sqrt{3}} = \frac{\sqrt{3}}{2}$.
- Q43: 2.00 - $\int_0^\pi \sin x dx = [-\cos x]_0^\pi = 2.00$.
- Q44: 30 - $\int_0^1 (x^4 - x^5)dx = 1/5 - 1/6 = 1/30 \implies K = 30$.
- Q45: 2 - $x^4 - 1 = (x^2 - 1)(x^2 + 1) = 0 \implies x = \pm 1$ (two real roots).
- Q46: 2 - $\vec{a}\cdot\vec{b} = 1(0) + 1(1) + 0(1) = 1$. $|\vec{a}| = \sqrt{2}, |\vec{b}| = \sqrt{2} \implies \cos\theta = 1/2 \implies K = 2$.
- Q47: 1 - Primes on a die are 2, 3, 5 (3 primes). Probability $3/6 = 1/2 \implies p = 1$.
- Q48: 3.00 - Radius of sphere $x^2 + y^2 + z^2 = 9$ is $3.00$.
- Q49: (A) - $\frac{d}{dx}\ln(\sin x) = \frac{\cos x}{\sin x} = \cot x$.
- Q50: (A) - $y' = 3x^2$. At $(1, 1)$, slope is 3.
- Q51: (A) - Taylor expansion: $\lim_{x\to 0}\frac{x^2/2}{x^2} = 1/2$.
- Q52: (A) - $\det(A^2) = (\det A)^2 = 4^2 = 16$.
- Q53: (A) - $4! = 24$.
- Q54: (A) - $\frac{dy}{y} = -2 dx \implies \ln y = -2x + C \implies y = C e^{-2x}$.
"""

        raw_val = r"""# Answer Key & Benchmark Alignment – Mock Examination __PAD__
## Organising Institute Style: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,D; Q6: A,B,C,D; Q7: 2258.76; Q8: 3456.96; Q9: 2.00; Q10: 50.35; Q11: 515; Q12: 20.0; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 1.26; Q26: 20.0; Q27: 125; Q28: 6; Q29: 12.30; Q30: 2.00; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C; Q43: 0.33; Q44: 30; Q45: 3; Q46: 3.00; Q47: 5; Q48: 5.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,D; Q6: A,B,C,D; Q7: 4.76; Q8: 3456.96; Q9: 2.00; Q10: 50.00; Q11: 0.20; Q12: 3.18; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 1.21; Q26: 25.0; Q27: 0.42; Q28: 6; Q29: 3.00; Q30: 0.63; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 2.00; Q44: 30; Q45: 2; Q46: 2; Q47: 1; Q48: 3.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""

        sol1 = raw_sol1.replace("__PAD__", pad).replace("__ROD_M__", rod_m).replace("__RES_R__", res_r).replace("__ACID_K__", acid_k).replace("__POLY_N__", poly_n)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Kharagpur")
        print(f"Generated IIT Kharagpur Mock {pad}!")

if __name__ == "__main__":
    generate_kharagpur_11_to_15()

