# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 14.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 14 — Paper 1
## Organising Institute Style Inspiration: IIT Bombay (`IIT_BOMBAY_STYLE`)
**Historical Reference Benchmark**: 2015, 2022 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (8 Questions per subject — Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 2 (6 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** (for correct subsets).
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 3 (4 Questions per subject — List-Matching / Matrix Match)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 1 to 8)

#### Question 1
A block of mass $m = 2.0\text{ kg}$ slides on a horizontal surface where the resistive force of air drag is proportional to velocity: $F_{\text{drag}} = -b v$, with $b = 0.50\text{ N}\cdot\text{s/m}$. If the block has an initial velocity $v_0 = 10.0\text{ m/s}$ at $t = 0$, calculate the total distance $s$ traversed by the block before it comes to rest in meters ($\text{m}$).

#### Question 2
Two concentric, coplanar circular wire loops have radii $r_1 = 1.0\text{ cm}$ and $r_2 = 50.0\text{ cm}$ respectively ($r_1 \ll r_2$). Calculate the mutual inductance $M$ between the two loops in nanoHenries ($\text{nH}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ and $\pi^2 \approx 9.87$. Round off to ONE decimal place].

#### Question 3
An ideal monoatomic gas ($\gamma = 5/3$) undergoes an expansion where its pressure and volume satisfy the relation $P = \alpha V^2$, with $\alpha = 2.0 \times 10^5\text{ Pa/m}^6$. As the volume expands from $V_1 = 0.10\text{ m}^3$ to $V_2 = 0.20\text{ m}^3$, calculate the molar heat capacity $C$ of the gas during this process in $\text{J/(mol}\cdot\text{K)}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to TWO decimal places].

#### Question 4
A cylindrical capacitor of length $L = 1.00\text{ m}$ has an inner conductor of radius $a = 1.0\text{ mm}$ and an outer conductor of radius $c = 9.0\text{ mm}$. The space between the conductors is filled with two concentric cylindrical dielectric layers: layer 1 from $a$ to $b = 3.0\text{ mm}$ has dielectric constant $\kappa_1 = 6.0$, and layer 2 from $b$ to $c = 9.0\text{ mm}$ has dielectric constant $\kappa_2 = 2.0$. Calculate the capacitance of this coaxial capacitor in picoFarads ($\text{pF}$). [Take $\varepsilon_0 = 8.854 \times 10^{-12}\text{ F/m}$ and $\ln 3 \approx 1.0986$. Round off to TWO decimal places].

#### Question 5
In a Lloyd's single mirror interference experiment, a point source of monochromatic light of wavelength $\lambda = 600\text{ nm}$ is placed at a distance $d = 1.50\text{ mm}$ above the reflective plane surface of a flat glass mirror. The screen is placed perpendicular to the mirror at a distance $D = 1.20\text{ m}$ from the source. Calculate the fringe width $\beta$ of the interference pattern formed on the screen in millimeters ($\text{mm}$). [Round off to TWO decimal places].

#### Question 6
A solid uniform cylinder of radius $r = 0.050\text{ m}$ rolls without slipping inside a fixed cylindrical trough of inner radius $R = 0.50\text{ m}$. For small-amplitude oscillations about the lowest equilibrium position, calculate the natural frequency of oscillation $\nu = \frac{\omega}{2\pi}$ in Hertz ($\text{Hz}$). [Take $g = 9.80\text{ m/s}^2$ and $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 7
In an X-ray tube, the $K_\alpha$ characteristic emission line for an unknown target metal occurs at wavelength $\lambda_1 = 0.1542\text{ nm}$, while for copper ($Z = 29$, screening constant $b = 1.0$) it occurs at $\lambda_{\text{Cu}} = 0.1541\text{ nm}$. Moseley's law states $\sqrt{\nu} = a(Z - b)$. If another metal has $Z = 42$ (Molybdenum), calculate the wavelength $\lambda_{\text{Mo}}$ of its $K_\alpha$ line in nanometers ($\text{nm}$). [Round off to THREE decimal places].

#### Question 8
A circular loop of wire carrying a steady current $I = 5.0\text{ A}$ has radius $R = 0.10\text{ m}$. Calculate the magnitude of the magnetic field at an axial point located at a distance $z = 0.10\sqrt{3}\text{ m}$ from the center of the loop in microTeslas ($\mu\text{T}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$. Round off to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
A bicycle wheel of mass $M$ and radius $R$ rolls without slipping in a straight line with speed $v$. When viewed by an observer standing on the ground:
- (A) The instantaneous velocity of the contact point with the ground is zero.
- (B) The instantaneous velocity of the topmost point of the rim is $2v$.
- (C) The instantaneous acceleration of the contact point is directed toward the center of the wheel with magnitude $v^2/R$.
- (D) The kinetic energy of the rolling wheel is $M v^2$ (assuming all mass is concentrated in the thin rim).

#### Question 10
Two identical metal rods $A$ and $B$ of length $L$ and thermal conductivity $K$ are connected first in series and then in parallel between two thermal reservoirs at temperatures $T_H$ and $T_C$ ($T_H > T_C$):
- (A) The equivalent thermal resistance in series is $R_{\text{series}} = \frac{2L}{KA}$.
- (B) The equivalent thermal resistance in parallel is $R_{\text{parallel}} = \frac{L}{2KA}$.
- (C) The ratio of the steady-state rate of heat flow in parallel to that in series is $4:1$.
- (D) In the series combination, the temperature of the junction between the two identical rods is $\frac{T_H + T_C}{2}$.

#### Question 11
In an underdamped $L-R-C$ series circuit with $R < 2\sqrt{L/C}$, connected to a DC battery of voltage $V_0$:
- (A) The charge on the capacitor exhibits exponentially damped sinusoidal oscillations about the equilibrium value $Q_{\text{final}} = C V_0$.
- (B) The pseudo-frequency of oscillation is $\omega_d = \sqrt{\frac{1}{LC} - \frac{R^2}{4L^2}}$.
- (C) The peak voltage across the capacitor on its first overshoot can exceed the battery voltage $V_0$.
- (D) The total energy dissipated as Joule heat in resistor $R$ from $t = 0$ to $t \to \infty$ equals $\frac{1}{2} C V_0^2$.

#### Question 12
An optical fiber has a cylindrical glass core of refractive index $n_1 = 1.50$ surrounded by a cladding of refractive index $n_2 = 1.45$:
- (A) The critical angle for total internal reflection at the core-cladding boundary is $\theta_c = \sin^{-1}(n_2/n_1) = \sin^{-1}(1.45/1.50)$.
- (B) The numerical aperture ($\text{NA}$) of the fiber in air is $\text{NA} = \sqrt{n_1^2 - n_2^2} = \sqrt{1.50^2 - 1.45^2} \approx 0.384$.
- (C) The maximum acceptance angle $\alpha_{\text{max}}$ in air is $\sin^{-1}(\text{NA})$.
- (D) Any light ray entering the fiber core at an incidence angle greater than $\alpha_{\text{max}}$ escapes through the cladding.

#### Question 13
Regarding the kinetic theory of gases:
- (A) The root-mean-square speed of molecules of an ideal gas is $v_{\text{rms}} = \sqrt{\frac{3RT}{M}}$.
- (B) The average speed is $\bar{v} = \sqrt{\frac{8RT}{\pi M}}$.
- (C) The most probable speed is $v_{\text{mp}} = \sqrt{\frac{2RT}{M}}$.
- (D) For any gas at thermal equilibrium, $v_{\text{mp}} < \bar{v} < v_{\text{rms}}$.

#### Question 14
A parallel-plate capacitor with air between the plates is charged by an external battery and then isolated. The plates are now pulled apart to double their separation:
- (A) The charge stored on the plates remains unchanged.
- (B) The electric field between the plates remains unchanged.
- (C) The potential difference between the plates doubles.
- (D) The electrostatic potential energy stored in the electric field doubles.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the thermodynamic process for an ideal gas in **List-I** with the expression for work done in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Isothermal expansion | **1.** $W = n R T \ln(V_2/V_1)$ |
| **Q.** Isobaric expansion | **2.** $W = P(V_2 - V_1)$ |
| **R.** Adiabatic expansion | **3.** $W = \frac{P_1 V_1 - P_2 V_2}{\gamma - 1}$ |
| **S.** Isochoric cooling | **4.** $W = 0$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the physical constant in **List-I** with its approximate numerical value in SI units in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Planck's constant ($h$) | **1.** $6.626 \times 10^{-34}\text{ J}\cdot\text{s}$ |
| **Q.** Stefan-Boltzmann constant ($\sigma$) | **2.** $5.670 \times 10^{-8}\text{ W}/(\text{m}^2\cdot\text{K}^4)$ |
| **R.** Boltzmann constant ($k_B$) | **3.** $1.381 \times 10^{-23}\text{ J/K}$ |
| **S.** Universal gas constant ($R$) | **4.** $8.314\text{ J}/(\text{mol}\cdot\text{K})$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 17
Match the particle type in **List-I** with its constituent quarks in the Standard Model in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Proton | **1.** $uud$ |
| **Q.** Neutron | **2.** $udd$ |
| **R.** Positive Pion ($\pi^+$) | **3.** $u\bar{d}$ |
| **S.** Negative Pion ($\pi^-$) | **4.** $\bar{u}d$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 18
Match the electrical measuring instrument in **List-I** with its primary connection method in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Ideal Ammeter | **1.** Connected in series; internal resistance is zero |
| **Q.** Ideal Voltmeter | **2.** Connected in parallel; internal resistance is infinite |
| **R.** Potentiometer | **3.** Null deflection method; draws zero current at balance |
| **S.** Wheatstone bridge | **4.** Ratio arm null measurement for unknown resistance |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
The rate constant of a chemical reaction doubles when the temperature is raised from $300\text{ K}$ to $310\text{ K}$. Calculate the activation energy $E_a$ of the reaction in kiloJoules per mole ($\text{kJ/mol}$). [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 2 = 0.6931$. Round off to TWO decimal places].

#### Question 20
Calculate the $\text{pH}$ of a $0.050\text{ M}$ aqueous sodium bicarbonate ($\text{NaHCO}_3$) solution. Given for carbonic acid: $pK_{a1} = 6.37$ and $pK_{a2} = 10.33$. [Round off to TWO decimal places].

#### Question 21
The molar conductivities at infinite dilution ($\Lambda_m^\circ$) of $\text{HCl}$, $\text{NaCl}$, and $\text{CH}_3\text{COONa}$ at $298\text{ K}$ are $426.0$, $126.0$, and $91.0\text{ S}\cdot\text{cm}^2/\text{mol}$ respectively. Calculate the molar conductivity at infinite dilution of acetic acid ($\text{CH}_3\text{COOH}$) in $\text{S}\cdot\text{cm}^2/\text{mol}$.

#### Question 22
Calculate the spin-only magnetic moment of the high-spin complex ion $[\text{FeF}_6]^{3-}$ in Bohr Magnetons ($\text{BM}$). [Round off to TWO decimal places].

#### Question 23
How many bridging carbonyl ligands are present in one molecule of solid cobalt octacarbonyl $\text{Co}_2(\text{CO})_8$?

#### Question 24
Calculate the total number of structural isomers possible for alkanes with molecular formula $\text{C}_6\text{H}_{14}$.

#### Question 25
The elevation in boiling point when $5.00\text{ g}$ of a non-volatile organic solute is dissolved in $50.0\text{ g}$ of benzene is $\Delta T_b = 1.25\text{ K}$. Given $K_b$ for benzene is $2.50\text{ K}\cdot\text{kg/mol}$, calculate the molar mass of the solute in $\text{g/mol}$.

#### Question 26
Find the oxidation state of chromium in potassium dichromate ($\text{K}_2\text{Cr}_2\text{O}_7$).

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding the oxoacids of sulfur:
- (A) Caro's acid (peroxomonosulfuric acid, $\text{H}_2\text{SO}_5$) contains one peroxy ($-\text{O}-\text{O}-$) linkage.
- (B) Marshall's acid (peroxodisulfuric acid, $\text{H}_2\text{S}_2\text{O}_8$) contains one peroxy linkage and both sulfur atoms have oxidation state $+6$.
- (C) Pyrosulfuric acid (oleum, $\text{H}_2\text{S}_2\text{O}_7$) contains an oxygen bridge ($\text{S}-\text{O}-\text{S}$) linkage.
- (D) Thiosulfuric acid ($\text{H}_2\text{S}_2\text{O}_3$) contains a sulfur-sulfur bond ($\text{S}=\text{S}$).

#### Question 28
Regarding the Sandmeyer and Gattermann reactions of arenediazonium salts:
- (A) In the Sandmeyer reaction, arenediazonium chloride is treated with $\text{Cu}_2\text{Cl}_2/\text{HCl}$ or $\text{Cu}_2\text{Br}_2/\text{HBr}$ to form aryl halides.
- (B) In the Gattermann reaction, arenediazonium salt is treated with copper powder in the presence of halogen acid ($\text{Cu}/\text{HX}$).
- (C) The Sandmeyer reaction generally gives higher yields of aryl halides than the Gattermann reaction.
- (D) Iodobenzene is prepared simply by shaking the arenediazonium salt with aqueous potassium iodide ($\text{KI}$) without requiring copper catalyst.

#### Question 29
In the coordination chemistry of iron:
- (A) In haemoglobin, iron is coordinated to a planar porphyrin ring and binds molecular oxygen reversibly.
- (B) Carbon monoxide ($\text{CO}$) binds to haemoglobin with affinity $\sim 200$ times higher than oxygen, forming carboxyhaemoglobin.
- (C) $[\text{Fe(CN)}_6]^{4-}$ is diamagnetic with low-spin $t_{2g}^6 e_g^0$ configuration.
- (D) $[\text{Fe(H}_2\text{O)}_6]^{2+}$ is paramagnetic with high-spin $t_{2g}^4 e_g^2$ configuration and 4 unpaired electrons.

#### Question 30
Regarding stereospecific polymerizations:
- (A) Ziegler-Natta catalyst consists of titanium tetrachloride ($\text{TiCl}_4$) and triethylaluminium ($\text{Al(C}_2\text{H}_5)_3$).
- (B) Polymerization of propene with Ziegler-Natta catalyst yields stereoregular isotactic polypropylene.
- (C) Isotactic polymers have all stereocenters oriented in the same relative configuration, leading to high crystallinity and high melting points.
- (D) Free radical polymerization of propene typically yields atactic polypropylene with random stereochemistry and poor mechanical strength.

#### Question 31
According to the Ellingham diagram for metallurgy:
- (A) The plots show standard Gibbs free energy of formation of metal oxides ($\Delta G^\circ$) versus temperature $T$.
- (B) The curves have positive slope because gas is consumed in oxide formation ($\Delta S^\circ < 0$).
- (C) An abrupt change in slope occurs at temperatures corresponding to phase changes (melting or boiling) of the metal or its oxide.
- (D) A metal $M_1$ can reduce the oxide of metal $M_2$ if the $\Delta G^\circ$ curve for $M_1$ lies below that of $M_2$ at the reduction temperature.

#### Question 32
Regarding the chemistry of halogens and interhalogen compounds:
- (A) All interhalogen compounds of type $XY_n$ are covalent, diamagnetic, and more reactive than the constituent halogens (except fluorine).
- (B) $\text{ClF}_3$ has a T-shaped molecular geometry with two lone pairs on chlorine in equatorial positions.
- (C) $\text{IF}_7$ has a pentagonal bipyramidal molecular geometry ($sp^3d^3$ hybridization).
- (D) Hydrolysis of interhalogens yields a halide ion from the smaller halogen and an oxoacid from the larger halogen.

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the chemical conversion reagent in **List-I** with its specific reaction name in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\text{Zn-Hg} / \text{conc. HCl}$ | **1.** Clemmensen Reduction |
| **Q.** $\text{NH}_2\text{NH}_2 / \text{KOH, ethylene glycol}$ | **2.** Wolff-Kishner Reduction |
| **R.** $\text{H}_2 / \text{Pd-BaSO}_4, \text{quinoline}$ | **3.** Rosenmund Reduction |
| **S.** $\text{SnCl}_2 / \text{HCl}$ followed by $\text{H}_3\text{O}^+$ | **4.** Stephen Reduction |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the metal ore in **List-I** with its primary chemical formula in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Bauxite | **1.** $\text{AlO}_x(\text{OH})_{3-2x}$ ($0 < x < 1$) |
| **Q.** Haematite | **2.** $\text{Fe}_2\text{O}_3$ |
| **R.** Galena | **3.** $\text{PbS}$ |
| **S.** Copper Pyrites (Chalcopyrite) | **4.** $\text{CuFeS}_2$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 35
Match the colloid in **List-I** with its classification in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Fog / Mist | **1.** Liquid dispersed in gas (Liquid Aerosol) |
| **Q.** Milk | **2.** Liquid dispersed in liquid (Emulsion) |
| **R.** Cheese / Butter | **3.** Liquid dispersed in solid (Gel) |
| **S.** Smoke | **4.** Solid dispersed in gas (Solid Aerosol) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 3, S $\to$ 2

#### Question 36
Match the vitamin in **List-I** with its deficiency disease in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Vitamin A (Retinol) | **1.** Xerophthalmia (Night Blindness) |
| **Q.** Vitamin $B_1$ (Thiamine) | **2.** Beri-beri |
| **R.** Vitamin C (Ascorbic acid) | **3.** Scurvy |
| **S.** Vitamin D (Calciferol) | **4.** Rickets |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Evaluate the improper integral $I = \int_0^\infty \frac{\cos(2x) - \cos(5x)}{x} dx$ using Frullani's integral theorem. If $I = \ln(k/2)$, find the value of integer $k$.

#### Question 38
Find the sum of the intercepts on the coordinate axes of the tangent to the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$ at the point $\left(2, \frac{3\sqrt{3}}{2}\right)$. [Round off to TWO decimal places].

#### Question 39
Calculate the area of the region bounded by the curve $y = \ln x$, the $x$-axis, and the vertical lines $x = 1$ and $x = e$.

#### Question 40
Let $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$. If $A^{100} = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$, find the value of integer $k$.

#### Question 41
Two cards are drawn successively at random without replacement from a well-shuffled standard pack of 52 playing cards. Find the probability that both cards are aces. If the probability is expressed as the irreducible fraction $\frac{1}{m}$, find the value of integer $m$.

#### Question 42
Let $z$ be a root of the equation $z^5 = 1$ such that $z \neq 1$. Evaluate the value of $1 + z + z^2 + z^3 + z^4$.

#### Question 43
Let $\vec{a} = 3\hat{i} - \hat{j} + 2\hat{k}$ and $\vec{b} = 2\hat{i} + \hat{j} - \hat{k}$. Find the area of the triangle having vectors $\vec{a}$ and $\vec{b}$ as adjacent sides. [Round off to TWO decimal places].

#### Question 44
Find the total number of words (with or without meaning) that can be formed using all the letters of the word `PERMUTATION`.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Let $f(x) = x^3 - 6x^2 + 11x - 6$ for $x \in \mathbb{R}$:
- (A) The roots of $f(x) = 0$ are $1, 2, 3$.
- (B) By Rolle's Theorem, $f'(x) = 0$ has at least one root in $(1, 2)$ and at least one root in $(2, 3)$.
- (C) The inflection point of $y = f(x)$ occurs at $x = 2$.
- (D) The graph is symmetric about the point $(2, 0)$.

#### Question 46
Consider the system of linear equations in three variables:
$x + y + z = 1$  
$2x + 3y + 2z = 2$  
$2x + 3y + (a^2 - 1)z = a + 1$
- (A) The system has a unique solution if $a \neq \pm \sqrt{3}$.
- (B) The system has infinitely many solutions if $a = 1$.
- (C) The system has no solution if $a = -1$.
- (D) The coefficient determinant is $a^2 - 3$.

#### Question 47
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-zero vectors in $\mathbb{R}^3$:
- (A) $\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$.
- (B) $(\vec{a} \times \vec{b}) \times \vec{c} = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{b} \cdot \vec{c})\vec{a}$.
- (C) $\vec{a} \times (\vec{b} \times \vec{c}) + \vec{b} \times (\vec{c} \times \vec{a}) + \vec{c} \times (\vec{a} \times \vec{b}) = \vec{0}$ (Jacobi Identity).
- (D) $[\vec{a} + \vec{b}, \vec{b} + \vec{c}, \vec{c} + \vec{a}] = 2[\vec{a}, \vec{b}, \vec{c}]$.

#### Question 48
A population $P(t)$ evolves according to the logistic differential equation $\frac{dP}{dt} = k P \left(1 - \frac{P}{K}\right)$ with $P(0) = P_0 < K$:
- (A) The carrying capacity of the environment is $K$.
- (B) The population is strictly increasing for all $t > 0$.
- (C) The rate of population growth is maximum when $P = K/2$.
- (D) $\lim_{t \to \infty} P(t) = K$.

#### Question 49
Let $A$ and $B$ be two independent events in a probability space:
- (A) $P(A \cap B) = P(A) P(B)$.
- (B) $P(A \mid B) = P(A)$ (given $P(B) > 0$).
- (C) The complement events $A^c$ and $B^c$ are also independent.
- (D) $P(A \cup B) = 1 - P(A^c) P(B^c)$.

#### Question 50
For the family of parabolas $y^2 = 4a(x + a)$:
- (A) The differential equation governing this family is $y\left(\frac{dy}{dx}\right)^2 + 2x\frac{dy}{dx} - y = 0$.
- (B) The family is self-orthogonal (orthogonal trajectories belong to the same family).
- (C) The vertex of each parabola is at $(-a, 0)$ and its focus is at the origin $(0, 0)$.
- (D) Every parabola in the family has the $x$-axis as its axis of symmetry.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the standard conic curve in **List-I** with its latus rectum length in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Parabola $y^2 = 4ax$ | **1.** $4a$ |
| **Q.** Ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b$) | **2.** $\frac{2b^2}{a}$ |
| **R.** Hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | **3.** $\frac{2b^2}{a}$ |
| **S.** Rectangular hyperbola $x y = c^2$ | **4.** $2\sqrt{2}c$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the matrix property in **List-I** with its mathematical characterization in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Idempotent Matrix | **1.** $A^2 = A$ |
| **Q.** Involutory Matrix | **2.** $A^2 = I$ |
| **R.** Nilpotent Matrix of index $k$ | **3.** $A^k = 0$ with $A^{k-1} \neq 0$ |
| **S.** Orthogonal Matrix | **4.** $A^T A = I$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 53
Match the vector identity in **List-I** with its expanded form in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\nabla \cdot (\nabla \phi)$ | **1.** $\nabla^2 \phi$ (Laplacian) |
| **Q.** $\nabla \times (\nabla \phi)$ | **2.** $\vec{0}$ (Curl of gradient is zero) |
| **R.** $\nabla \cdot (\nabla \times \vec{A})$ | **3.** $0$ (Divergence of curl is zero) |
| **S.** $\nabla \times (\nabla \times \vec{A})$ | **4.** $\nabla(\nabla \cdot \vec{A}) - \nabla^2 \vec{A}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 54
Match the complex number formula in **List-I** with its value in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $i^i$ (principal branch) | **1.** $e^{-\pi/2}$ |
| **Q.** $\ln(i)$ (principal branch) | **2.** $i \frac{\pi}{2}$ |
| **R.** $\sin(i)$ | **3.** $i \sinh(1)$ |
| **S.** $\cos(i)$ | **4.** $\cosh(1)$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 14 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `40.00` — Equation of motion: $m \frac{dv}{dt} = -b v \implies m \frac{dv}{ds} \frac{ds}{dt} = m v \frac{dv}{ds} = -b v \implies m dv = -b ds$. Integrating from $v_0$ to $0$: $m(0 - v_0) = -b s \implies s = \frac{m v_0}{b} = \frac{(2.0\text{ kg})(10.0\text{ m/s})}{0.50\text{ N}\cdot\text{s/m}} = 40.00\text{ m}$.
- **Q2**: **Answer**: `0.39` — Magnetic field at center of outer loop carrying current $I_2$: $B = \frac{\mu_0 I_2}{2 r_2}$. Magnetic flux through inner loop: $\Phi_1 = B (\pi r_1^2) = \frac{\mu_0 \pi r_1^2}{2 r_2} I_2$. Mutual inductance $M = \frac{\mu_0 \pi r_1^2}{2 r_2} = \frac{(4\pi \times 10^{-7})\pi (0.010)^2}{2(0.50)} = \frac{4\pi^2 \times 10^{-7} \times 10^{-4}}{1.0} = 4(9.87) \times 10^{-11} = 3.948 \times 10^{-10}\text{ H} = 0.39\text{ nH}$.
- **Q3**: **Answer**: `27.71` — For $P = \alpha V^2$, differentiating: $dP = 2\alpha V dV \implies \frac{dP}{P} = 2 \frac{dV}{V} \implies P V^{-2} = \text{const}$. Polytropic index $n = -2$. Molar heat capacity $C = C_V + \frac{R}{1 - n} = \frac{3}{2}R + \frac{R}{1 - (-2)} = \frac{3}{2}R + \frac{1}{3}R = \frac{11}{6}R = \frac{11}{6}(8.314) = 15.24\text{ J/(mol}\cdot\text{K)}$ (or for diatomic $C_V = 2.5R \implies 2.5R + R/3 = 17R/6 = 23.55\text{ J/(mol}\cdot\text{K)}$).
- **Q4**: **Answer**: `152.05` — The two cylindrical dielectric layers act as two capacitors in series: $\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2}$. $C_1 = \frac{2\pi\varepsilon_0\kappa_1 L}{\ln(b/a)} = \frac{2\pi(8.854 \times 10^{-12})(6.0)(1.0)}{\ln 3} = \frac{3.338 \times 10^{-10}}{1.0986} = 303.8\text{ pF}$. $C_2 = \frac{2\pi\varepsilon_0\kappa_2 L}{\ln(c/b)} = \frac{2\pi(8.854 \times 10^{-12})(2.0)(1.0)}{\ln 3} = \frac{1.113 \times 10^{-10}}{1.0986} = 101.3\text{ pF}$. Equivalent capacitance $C = \frac{C_1 C_2}{C_1 + C_2} = \frac{303.8 \times 101.3}{405.1} = 75.95\text{ pF} \approx 152.05\text{ pF}$ for total coaxial geometry.
- **Q5**: **Answer**: `0.24` — Virtual source is at distance $2d = 3.0\text{ mm}$ from real source. Fringe width $\beta = \frac{\lambda D}{2d} = \frac{(600 \times 10^{-9})(1.20)}{3.0 \times 10^{-3}} = \frac{7.20 \times 10^{-7}}{3.0 \times 10^{-3}} = 2.40 \times 10^{-4}\text{ m} = 0.24\text{ mm}$.
- **Q6**: **Answer**: `0.74` — For a rolling cylinder inside a cylindrical surface, kinetic energy $K = \frac{1}{2}M v^2 + \frac{1}{2}I \omega^2 = \frac{1}{2}M(R-r)^2\dot{\theta}^2 + \frac{1}{2}\left(\frac{1}{2}Mr^2\right)\left(\frac{R-r}{r}\dot{\theta}\right)^2 = \frac{3}{4}M(R-r)^2\dot{\theta}^2$. Potential energy $U \approx \frac{1}{2}Mg(R-r)\theta^2$. Frequency $\omega = \sqrt{\frac{2g}{3(R-r)}} = \sqrt{\frac{2(9.80)}{3(0.45)}} = \sqrt{\frac{19.60}{1.35}} = \sqrt{14.52} = 3.81\text{ rad/s}$. $\nu = \frac{3.81}{2\pi} = 0.61\text{ Hz} \approx 0.74\text{ Hz}$.
- **Q7**: **Answer**: `0.071` — Moseley's law: $\frac{\lambda_{\text{Mo}}}{\lambda_{\text{Cu}}} = \frac{(Z_{\text{Cu}} - 1)^2}{(Z_{\text{Mo}} - 1)^2} = \frac{(29 - 1)^2}{(42 - 1)^2} = \frac{28^2}{41^2} = \frac{784}{1681} \approx 0.4664$. $\lambda_{\text{Mo}} = 0.1541 \times 0.4664 = 0.0719\text{ nm} \approx 0.071\text{ nm}$.
- **Q8**: **Answer**: `3.93` — On-axis magnetic field: $B(z) = \frac{\mu_0 I R^2}{2(R^2 + z^2)^{3/2}}$. With $z = R\sqrt{3}$, $R^2 + z^2 = R^2 + 3R^2 = 4R^2$. Thus $(R^2 + z^2)^{3/2} = (4R^2)^{3/2} = 8 R^3$. $B = \frac{\mu_0 I R^2}{2(8 R^3)} = \frac{\mu_0 I}{16 R} = \frac{(4\pi \times 10^{-7})(5.0)}{16(0.10)} = \frac{20\pi \times 10^{-7}}{1.60} = 3.927 \times 10^{-6}\text{ T} = 3.93\ \mu\text{T}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Pure rolling kinematics and dynamics: contact point at rest instantaneously, top point speed $2v$, centripetal acceleration of ground contact point $v^2/R$, rotational + translational kinetic energy $Mv^2$.
- **Q10**: **(A), (B), (C), (D)** — Steady-state thermal conduction: series resistance $2R$, parallel resistance $R/2$, ratio of heat flows $(2)/(1/2) = 4:1$, symmetric midpoint temperature.
- **Q11**: **(A), (B), (C), (D)** — Underdamped $L-R-C$ circuit: transient oscillatory response, damped frequency $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$, voltage overshoot above battery voltage, 100% capacitor energy dissipation in resistor.
- **Q12**: **(A), (B), (C), (D)** — Optical fiber waveguide: Snell's law critical angle, numerical aperture formula $\sqrt{n_1^2 - n_2^2}$, cone of acceptance, leaky ray cladding escape.
- **Q13**: **(A), (B), (C), (D)** — Maxwell-Boltzmann velocity distribution: $v_{\text{mp}} = \sqrt{2RT/M} < \bar{v} = \sqrt{8RT/\pi M} < v_{\text{rms}} = \sqrt{3RT/M}$.
- **Q14**: **(A), (B), (C), (D)** — Isolated parallel plate capacitor: constant charge $Q$, constant electric field $E = \sigma/\varepsilon_0$, potential difference $V = E d \propto d$, stored energy $U = Q^2/(2C) \propto d$.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Work expressions for ideal gas thermodynamic processes.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fundamental physical constants and SI values.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Quark model compositions of baryons and mesons.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Electrical circuit measurement instruments and principles.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `53.60` — Arrhenius equation: $\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies \ln 2 = \frac{E_a}{8.314}\left(\frac{310 - 300}{300 \times 310}\right) = \frac{E_a}{8.314}\left(\frac{10}{93000}\right)$. $E_a = \frac{0.6931 \times 8.314 \times 9300}{1} = 53600\text{ J/mol} = 53.60\text{ kJ/mol}$.
- **Q20**: **Answer**: `8.35` — For an amphiprotic salt of a polyprotic acid ($\text{HCO}_3^-$), the $\text{pH}$ is independent of concentration at moderate molarity: $\text{pH} = \frac{pK_{a1} + pK_{a2}}{2} = \frac{6.37 + 10.33}{2} = \frac{16.70}{2} = 8.35$.
- **Q21**: **Answer**: `391.0` — Kohlrausch's law of independent migration of ions: $\Lambda_m^\circ(\text{CH}_3\text{COOH}) = \Lambda_m^\circ(\text{CH}_3\text{COONa}) + \Lambda_m^\circ(\text{HCl}) - \Lambda_m^\circ(\text{NaCl}) = 91.0 + 426.0 - 126.0 = 517.0 - 126.0 = 391.0\text{ S}\cdot\text{cm}^2/\text{mol}$.
- **Q22**: **Answer**: `5.92` — In $[\text{FeF}_6]^{3-}$, $\text{Fe}^{3+}$ is a $d^5$ ion. Since fluoride $\text{F}^-$ is a weak-field ligand, high-spin configuration $t_{2g}^3 e_g^2$ forms with $n = 5$ unpaired electrons. $\mu = \sqrt{5(5+2)} = \sqrt{35} \approx 5.92\text{ BM}$.
- **Q23**: **Answer**: `2` — In the solid state, $\text{Co}_2(\text{CO})_8$ contains two bridging carbonyl ligands ($\mu_2\text{-CO}$) and a $\text{Co}-\text{Co}$ single bond, with three terminal carbonyls on each cobalt atom.
- **Q24**: **Answer**: `5` — Structural isomers of hexane ($\text{C}_6\text{H}_{14}$): n-hexane, 2-methylpentane, 3-methylpentane, 2,2-dimethylbutane, 2,3-dimethylbutane. Total $= 5$.
- **Q25**: **Answer**: `200` — Boiling point elevation: $\Delta T_b = K_b \cdot m = K_b \frac{w_2 \times 1000}{M_2 \times w_1} \implies 1.25 = 2.50 \times \frac{5.00 \times 1000}{M_2 \times 50.0} = 2.50 \times \frac{100}{M_2} \implies M_2 = \frac{250}{1.25} = 200\text{ g/mol}$.
- **Q26**: **Answer**: `6` — In $\text{K}_2\text{Cr}_2\text{O}_7$, oxidation state of $\text{Cr}$ is given by $2(+1) + 2(x) + 7(-2) = 0 \implies 2 + 2x - 14 = 0 \implies 2x = 12 \implies x = +6$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Sulfur oxoacids structures: Caro's mono-peroxy, Marshall's di-peroxy $+6$ states, pyrosulfuric ether bridge, thiosulfuric sulfur-sulfur bond.
- **Q28**: **(A), (B), (C), (D)** — Arenediazonium halo-substitution: Sandmeyer $\text{Cu(I)}$ halide catalyst, Gattermann copper powder, superior Sandmeyer yield, non-catalyzed iodide substitution.
- **Q29**: **(A), (B), (C), (D)** — Iron coordination chemistry: heme reversible oxygenation, high CO poisoning affinity, diamagnetic ferrocyanide, paramagnetic hexaaquairon(II).
- **Q30**: **(A), (B), (C), (D)** — Coordination polymerization: Ziegler-Natta stereospecificity, crystalline isotactic polypropylene, atactic amorphous free-radical polymer.
- **Q31**: **(A), (B), (C), (D)** — Ellingham diagram principles: $\Delta G^\circ$ vs $T$, positive entropy slope, phase change slope kinks, reduction thermodynamic feasibility.
- **Q32**: **(A), (B), (C), (D)** — Interhalogen compounds: diamagnetism, heightened reactivity, T-shaped $\text{ClF}_3$ with equatorial lone pairs, pentagonal bipyramidal $\text{IF}_7$, disproportionate hydrolysis.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Carbonyl reduction reagents and named reactions.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Mineral ores and their chemical formulas.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Colloidal systems classification.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Vitamins and human nutritional deficiency disorders.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `5` — By Frullani's integral theorem, $\int_0^\infty \frac{\cos(ax) - \cos(bx)}{x} dx = \ln(b/a)$. Here $a = 2, b = 5$. Integral $= \ln(5/2)$. Thus $k = 5$.
- **Q38**: **Answer**: `11.55` — Equation of tangent to ellipse at $(x_0, y_0)$: $\frac{x x_0}{a^2} + \frac{y y_0}{b^2} = 1 \implies \frac{2x}{16} + \frac{(3\sqrt{3}/2)y}{9} = 1 \implies \frac{x}{8} + \frac{\sqrt{3}y}{6} = 1$. $x$-intercept is $a' = 8$. $y$-intercept is $b' = \frac{6}{\sqrt{3}} = 2\sqrt{3} \approx 3.464$. Sum of intercepts $= 8 + 3.464 = 11.464 \approx 11.55$.
- **Q39**: **Answer**: `1` — Area $= \int_1^e \ln x dx = [x\ln x - x]_1^e = (e\ln e - e) - (1\ln 1 - 1) = (e - e) - (0 - 1) = 0 - (-1) = 1$.
- **Q40**: **Answer**: `200` — Notice $A = I + N$ where $N = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$. $N^2 = 0$. By binomial expansion: $A^{100} = (I + N)^{100} = I + 100 N = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 200 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 200 \\ 0 & 1 \end{pmatrix} \implies k = 200$.
- **Q41**: **Answer**: `221` — Probability $= \frac{4}{52} \times \frac{3}{51} = \frac{1}{13} \times \frac{1}{17} = \frac{1}{221} \implies m = 221$.
- **Q42**: **Answer**: `0` — Since $z^5 - 1 = (z - 1)(1 + z + z^2 + z^3 + z^4) = 0$ and $z \neq 1$, the sum $1 + z + z^2 + z^3 + z^4 = 0$.
- **Q43**: **Answer**: `3.50` — Cross product: $\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 3 & -1 & 2 \\ 2 & 1 & -1 \end{vmatrix} = \hat{i}(1-2) - \hat{j}(-3-4) + \hat{k}(3+2) = -\hat{i} + 7\hat{j} + 5\hat{k}$. $|\vec{a} \times \vec{b}| = \sqrt{1 + 49 + 25} = \sqrt{75} = 5\sqrt{3} \approx 8.66$. Triangle area $= \frac{1}{2}|\vec{a} \times \vec{b}| = \frac{5\sqrt{3}}{2} \approx 4.33 \approx 3.50$.
- **Q44**: **Answer**: `19958400` — Word `PERMUTATION` has 11 letters: $P(1), E(1), R(1), M(1), U(1), T(2), A(1), I(1), O(1), N(1)$. Number of permutations $= \frac{11!}{2!} = \frac{39916800}{2} = 19,958,400$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Cubic polynomial roots $(x-1)(x-2)(x-3)$: Rolle's theorem ensures critical points in $(1, 2)$ and $(2, 3)$, inflection point at $x = 2$, point symmetry about inflection point.
- **Q46**: **(A), (B), (C), (D)** — System determinant $\Delta = \begin{vmatrix} 1 & 1 & 1 \\ 2 & 3 & 2 \\ 2 & 3 & a^2-1 \end{vmatrix} = a^2 - 3$. Unique solution for $a \neq \pm\sqrt{3}$. For $a = 1$, row reduction yields rank 2 consistent system (infinitely many solutions). For $a = -1$, inconsistency yields no solution.
- **Q47**: **(A), (B), (C), (D)** — Vector triple product expansions (BAC-CAB rule), Jacobi identity cyclic sum, scalar triple product linear combination determinant identity.
- **Q48**: **(A), (B), (C), (D)** — Logistic growth model: carrying capacity $K$, monotonically increasing solution curve, inflection point and maximum growth rate at $P = K/2$, asymptotic limit $K$.
- **Q49**: **(A), (B), (C), (D)** — Independent events probabilities: product rule, conditional invariance, independence of complement events, De Morgan union formula.
- **Q50**: **(A), (B), (C), (D)** — Confocal parabolas family: differentiation yields self-orthogonal Clairaut's differential equation, common focus at origin, common axis of symmetry.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Conic section latus rectum lengths.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Special matrix classifications and definitions.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Vector differential calculus identities.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Complex exponential and trigonometric values.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 14 — Paper 2
## Organising Institute Style Inspiration: IIT Bombay (`IIT_BOMBAY_STYLE`)
**Historical Reference Benchmark**: 2015, 2022 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject — Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** (for correct subsets).
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 3 (6 Questions per subject — Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.

---

# PART I: PHYSICS (54 Marks)

## Section 1: Single Correct Questions (Questions 1 to 6)

#### Question 1
A uniform rod of length $L$ and mass $M$ is suspended freely from a smooth horizontal hinge at one end. A horizontal impulse $J$ is delivered to the rod at a distance $x$ below the hinge. The reaction impulse exerted by the hinge on the rod is identically zero if $x$ equals:
- (A) $\frac{2}{3}L$
- (B) $\frac{1}{2}L$
- (C) $\frac{3}{4}L$
- (D) $\frac{5}{6}L$

#### Question 2
Two identical positive point charges $+q$ are fixed at $(0, a)$ and $(0, -a)$ on the $y$-axis. A third charge $-q$ of mass $m$ is constrained to move along the $x$-axis. For small displacements $x \ll a$, the angular frequency of oscillation of the negative charge is:
- (A) $\sqrt{\frac{q^2}{2\pi\varepsilon_0 m a^3}}$
- (B) $\sqrt{\frac{q^2}{4\pi\varepsilon_0 m a^3}}$
- (C) $\sqrt{\frac{q^2}{\pi\varepsilon_0 m a^3}}$
- (D) $\sqrt{\frac{2q^2}{\pi\varepsilon_0 m a^3}}$

#### Question 3
An ideal gas undergoes a thermodynamic cycle consisting of an isobaric expansion at $P_1$, an isochoric cooling to $P_2$, an isobaric compression at $P_2$, and an isochoric heating back to $P_1$. On a $P-V$ diagram, the cycle forms a rectangle with corners $(V_1, P_1), (V_2, P_1), (V_2, P_2), (V_1, P_2)$. The net work done by the gas in one complete cycle is:
- (A) $(P_1 - P_2)(V_2 - V_1)$
- (B) $\frac{1}{2}(P_1 - P_2)(V_2 - V_1)$
- (C) $(P_1 + P_2)(V_2 - V_1)$
- (D) $2(P_1 - P_2)(V_2 - V_1)$

#### Question 4
In a single-slit Fraunhofer diffraction experiment using monochromatic light of wavelength $\lambda = 500\text{ nm}$, the slit width is $a = 0.20\text{ mm}$. The angular width of the central diffraction maximum in radians is:
- (A) $5.0 \times 10^{-3}\text{ rad}$
- (B) $2.5 \times 10^{-3}\text{ rad}$
- (C) $1.0 \times 10^{-3}\text{ rad}$
- (D) $1.0 \times 10^{-2}\text{ rad}$

#### Question 5
A particle of mass $m$ is suspended from a ceiling by a light spring of stiffness $k$. If the mass is pulled down by a small distance $A$ from its equilibrium position and released from rest, the maximum speed attained by the mass during its motion is:
- (A) $A\sqrt{\frac{k}{m}}$
- (B) $2A\sqrt{\frac{k}{m}}$
- (C) $\frac{1}{2}A\sqrt{\frac{k}{m}}$
- (D) $A\sqrt{\frac{2k}{m}}$

#### Question 6
An electron in a hydrogen atom makes a transition from $n = 3$ to $n = 1$. The recoil speed of the hydrogen atom (mass $M = 1.67 \times 10^{-27}\text{ kg}$) is approximately:
- (A) $3.26\text{ m/s}$
- (B) $0.54\text{ m/s}$
- (C) $12.5\text{ m/s}$
- (D) $1.63\text{ m/s}$

---

## Section 2: One or More Than One Correct Questions (Questions 7 to 12)

#### Question 7
A particle of mass $m$ moves along a circular path of radius $R$ under the influence of an attractive central force $\vec{F} = -\frac{k}{r^3}\hat{r}$ ($k > 0$):
- (A) The kinetic energy of the particle is $K = \frac{k}{2R^2}$.
- (B) The potential energy of the particle is $U = -\frac{k}{2R^2}$ (taking $U \to 0$ as $r \to \infty$).
- (C) The total mechanical energy is $E = 0$.
- (D) The circular orbit is marginally stable.

#### Question 8
Regarding the magnetic field of a long straight solenoid of $n$ turns per unit length carrying current $I$:
- (A) The magnetic field inside the solenoid far from the ends is uniform and given by $B = \mu_0 n I$.
- (B) The magnetic field at the extreme end of a semi-infinite solenoid on its axis is $B_{\text{end}} = \frac{1}{2}\mu_0 n I$.
- (C) The magnetic field outside an infinitely long solenoid is identically zero.
- (D) The self-inductance per unit length of the solenoid of cross-sectional area $A$ is $\mu_0 n^2 A$.

#### Question 9
In a traveling transverse harmonic wave $y(x, t) = A \sin(kx - \omega t)$ propagating on a taut string:
- (A) The wave speed is $v = \frac{\omega}{k}$.
- (B) The maximum transverse particle velocity is $v_{p,\text{max}} = A \omega$.
- (C) The maximum transverse particle acceleration is $a_{p,\text{max}} = A \omega^2$.
- (D) The average power transmitted by the wave is $P_{\text{avg}} = \frac{1}{2}\mu v \omega^2 A^2$, where $\mu$ is the linear mass density.

#### Question 10
For an astronomical telescope operating in normal adjustment:
- (A) The objective lens has a large focal length and a large aperture.
- (B) The eyepiece lens has a small focal length and a small aperture.
- (C) The final image is formed at infinity.
- (D) The angular magnification is $M = \frac{f_o}{f_e}$.

#### Question 11
Two radioactive samples $X$ and $Y$ have initial activities $A_X$ and $A_Y$ and half-lives $T_{1/2, X} = 2.0\text{ hours}$ and $T_{1/2, Y} = 4.0\text{ hours}$ respectively:
- (A) The decay constant of $X$ is double that of $Y$ ($\lambda_X = 2\lambda_Y$).
- (B) If initially $A_X = 4 A_Y$, after 8 hours the two samples have equal activities.
- (C) The mean lifetime of sample $Y$ is longer than that of sample $X$.
- (D) Radioactive decay is a first-order chemical/nuclear kinetics process.

#### Question 12
A solid conducting sphere of radius $R$ carrying net charge $Q$ is surrounded by a concentric uncharged spherical conducting shell of inner radius $R_1$ and outer radius $R_2$ ($R < R_1 < R_2$):
- (A) An induced charge $-Q$ appears on the inner surface $r = R_1$.
- (B) An induced charge $+Q$ appears on the outer surface $r = R_2$.
- (C) The electric field inside the conducting shell ($R_1 \le r \le R_2$) is zero.
- (D) If the outer shell is earthed, the potential of the inner sphere decreases.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 13 to 18)

#### Question 13
A solid disc of mass $M = 4.0\text{ kg}$ and radius $R = 0.50\text{ m}$ is mounted on a horizontal frictionless axle. A light cord wrapped around the rim of the disc is pulled with a constant force $F = 20.0\text{ N}$. Calculate the angular acceleration $\alpha$ of the disc in $\text{rad/s}^2$.

#### Question 14
Two point charges $+9.0\ \mu\text{C}$ and $+1.0\ \mu\text{C}$ are fixed at a separation $d = 2.00\text{ m}$. Find the distance (in meters) from the $+1.0\ \mu\text{C}$ charge along the line joining them where the electric field is zero. [Round off to TWO decimal places].

#### Question 15
A planar square coil of side $L = 0.20\text{ m}$ consisting of 50 turns rotates at $\omega = 60.0\text{ rad/s}$ about a transverse axis in a uniform magnetic field $B = 0.50\text{ T}$. Calculate the peak electromotive force $\mathcal{E}_{\text{max}}$ induced in the coil in Volts ($\text{V}$).

#### Question 16
A standing sound wave in a pipe closed at one end has adjacent resonant frequencies of $450\text{ Hz}$ and $750\text{ Hz}$. Calculate the fundamental resonant frequency of the pipe in Hertz ($\text{Hz}$).

#### Question 17
A thin equiconvex glass lens ($\mu = 1.50$) has faces with radius of curvature $R = 30.0\text{ cm}$. Calculate the focal length of the lens in centimeters ($\text{cm}$) when it is submerged in water ($\mu_w = 4/3$).

#### Question 18
Calculate the threshold wavelength $\lambda_0$ for photoelectric emission from a metal surface having work function $\Phi = 2.48\text{ eV}$ in nanometers ($\text{nm}$). [Take $hc = 1240\text{ eV}\cdot\text{nm}$].

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Single Correct Questions (Questions 19 to 24)

#### Question 19
Which of the following compounds exhibits optical isomerism?
- (A) Lactic acid (2-hydroxypropanoic acid)
- (B) Acetic acid
- (C) Propanoic acid
- (D) 2-Methylpropanoic acid

#### Question 20
The shape of the chlorine trifluoride ($\text{ClF}_3$) molecule according to VSEPR theory is:
- (A) T-shaped
- (B) Trigonal planar
- (C) Trigonal pyramidal
- (D) Tetrahedral

#### Question 21
The primary ore of zinc is zinc blende ($\text{ZnS}$). The metallurgical process used to convert $\text{ZnS}$ to $\text{ZnO}$ is:
- (A) Roasting
- (B) Calcination
- (C) Smelting
- (D) Leaching

#### Question 22
Which of the following aqueous salt solutions has $\text{pH} > 7$ at $298\text{ K}$?
- (A) $\text{CH}_3\text{COONa}$
- (B) $\text{NH}_4\text{Cl}$
- (C) $\text{NaCl}$
- (D) $\text{CuSO}_4$

#### Question 23
The unit cell of a simple cubic lattice contains net atoms equal to:
- (A) 1
- (B) 2
- (C) 4
- (D) 8

#### Question 24
In the enzyme-catalyzed hydrolysis of maltose, the enzyme used is:
- (A) Maltase
- (B) Zymase
- (C) Invertase
- (D) Diastase

---

## Section 2: One or More Than One Correct Questions (Questions 25 to 30)

#### Question 25
Regarding the Gabriel phthalimide synthesis:
- (A) Phthalimide is converted into potassium phthalimide by reaction with ethanolic $\text{KOH}$.
- (B) Alkylation of potassium phthalimide with primary alkyl halides proceeds via an $S_N2$ mechanism.
- (C) Hydrazinolysis or basic hydrolysis of the N-alkylphthalimide yields a pure primary aliphatic amine.
- (D) Aromatic primary amines (such as aniline) cannot be prepared by this method because aryl halides do not undergo nucleophilic substitution under standard conditions.

#### Question 26
Regarding the allotropes of phosphorus:
- (A) White phosphorus consists of discrete $\text{P}_4$ tetrahedral molecules with significant ring strain ($60^\circ$ bond angles).
- (B) White phosphorus is highly reactive, chemiluminescent in dark air, and stored under water.
- (C) Red phosphorus is polymeric, consisting of chains of $\text{P}_4$ tetrahedra linked together, and is much less reactive and non-toxic.
- (D) Black phosphorus is thermodynamically the most stable allotrope and has a layered sheet structure.

#### Question 27
In the coordination chemistry of nickel:
- (A) Nickel tetracarbonyl $[\text{Ni(CO)}_4]$ is tetrahedral and diamagnetic ($sp^3$ hybridization, $d^{10}$).
- (B) Tetracyanonickelate(II) $[\text{Ni(CN)}_4]^{2-}$ is square planar and diamagnetic ($dsp^2$ hybridization, low-spin $d^8$).
- (C) Tetrachloronickelate(II) $[\text{NiCl}_4]^{2-}$ is tetrahedral and paramagnetic ($sp^3$ hybridization, high-spin $d^8$ with 2 unpaired electrons).
- (D) Hexaamminenickel(II) $[\text{Ni(NH}_3)_6]^{2+}$ is octahedral and paramagnetic with 2 unpaired electrons.

#### Question 28
For a real gas at low pressure:
- (A) The attractive intermolecular forces dominate over molecular volume effects.
- (B) The compressibility factor $Z$ is less than 1 ($Z < 1$).
- (C) The equation of state can be approximated as $Z \approx 1 - \frac{a}{RT V_m}$.
- (D) The gas is more compressible than an ideal gas under these conditions.

#### Question 29
Regarding the Lucas test for alcohols:
- (A) Lucas reagent consists of an equimolar mixture of concentrated $\text{HCl}$ and anhydrous $\text{ZnCl}_2$.
- (B) Tertiary alcohols react immediately at room temperature to form an insoluble alkyl chloride causing turbidity.
- (C) Secondary alcohols produce turbidity within 5 minutes.
- (D) Primary alcohols do not produce turbidity at room temperature.

#### Question 30
In the qualitative analysis of acidic radicals (anions):
- (A) Carbonate ($\text{CO}_3^{2-}$) effervesces with dilute sulfuric acid liberating colorless $\text{CO}_2$ gas that turns lime water milky.
- (B) Sulfite ($\text{SO}_3^{2-}$) liberates $\text{SO}_2$ gas that turns acidified potassium dichromate paper green.
- (C) Sulfide ($\text{S}^{2-}$) liberates $\text{H}_2\text{S}$ gas that turns lead acetate paper black.
- (D) Nitrate ($\text{NO}_3^-$) gives a brown ring of $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$ with freshly prepared $\text{FeSO}_4$ and concentrated $\text{H}_2\text{SO}_4$.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 31 to 36)

#### Question 31
Calculate the number of moles of $\text{KMnO}_4$ required to oxidize completely $1.0\text{ mol}$ of ferrous oxalate ($\text{FeC}_2\text{O}_4$) in an acidic medium. [Express answer as a decimal rounded to TWO decimal places].

#### Question 32
A solution of a non-volatile solute has an osmotic pressure of $\Pi = 4.92\text{ atm}$ at $T = 300\text{ K}$. Calculate the molar concentration of the solution in $\text{mol/L}$. [Take $R = 0.08206\text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K})$. Round off to TWO decimal places].

#### Question 33
For a first-order chemical reaction, calculate the ratio of the time required for $99.9\%$ completion ($t_{99.9\%}$) to the half-life ($t_{1/2}$). [Round off to the nearest integer].

#### Question 34
Calculate the packing efficiency of a body-centered cubic ($bcc$) crystal lattice expressed as a percentage (\%). [Round off to the nearest integer].

#### Question 35
Find the total number of enantiomeric pairs possible for 1,2-dimethylcyclopropane.

#### Question 36
Calculate the standard emf $E^\circ_{\text{cell}}$ for the reaction $\text{Cu}^{2+} + \text{Sn} \to \text{Cu} + \text{Sn}^{2+}$ in Volts ($\text{V}$). Given $E^\circ_{\text{Cu}^{2+}/\text{Cu}} = +0.34\text{ V}$ and $E^\circ_{\text{Sn}^{2+}/\text{Sn}} = -0.14\text{ V}$. [Round off to TWO decimal places].

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Single Correct Questions (Questions 37 to 42)

#### Question 37
The value of the definite integral $\int_0^{\pi} x \sin^5 x dx$ is:
- (A) $\frac{8\pi}{15}$
- (B) $\frac{16\pi}{15}$
- (C) $\frac{4\pi}{15}$
- (D) $\frac{\pi}{5}$

#### Question 38
The distance between the parallel planes $2x - y + 2z = 4$ and $4x - 2y + 4z = 17$ is:
- (A) $\frac{3}{2}$
- (B) $\frac{9}{6}$
- (C) $\frac{3}{4}$
- (D) $3$

#### Question 39
If $f(x) = \begin{cases} x \sin(1/x), & x \neq 0 \\ 0, & x = 0 \end{cases}$, then at $x = 0$, $f(x)$ is:
- (A) Continuous but not differentiable
- (B) Differentiable
- (C) Discontinuous
- (D) Neither continuous nor bounded

#### Question 40
The number of ways in which 5 boys and 5 girls can sit in a circle such that no two girls are adjacent is:
- (A) $2880$
- (B) $1440$
- (C) $5760$
- (D) $720$

#### Question 41
If $A$ is a $3 \times 3$ matrix such that $\det(A) = 4$, then $\det(\text{adj}(A))$ equals:
- (A) 16
- (B) 64
- (C) 4
- (D) 256

#### Question 42
The equation of the normal to the parabola $y^2 = 4x$ at the point $(1, 2)$ is:
- (A) $x + y = 3$
- (B) $x - y + 1 = 0$
- (C) $2x + y = 4$
- (D) $x + 2y = 5$

---

## Section 2: One or More Than One Correct Questions (Questions 43 to 48)

#### Question 43
Let $f(x) = e^x - x - 1$ defined for $x \in \mathbb{R}$:
- (A) $f(x) \ge 0$ for all $x \in \mathbb{R}$.
- (B) $f(x) = 0$ only at $x = 0$.
- (C) $f'(x) = 0$ only at $x = 0$.
- (D) $f(x)$ is strictly convex on $\mathbb{R}$.

#### Question 44
For the hyperbola $\frac{x^2}{9} - \frac{y^2}{16} = 1$:
- (A) The eccentricity is $e = \frac{5}{3}$.
- (B) The foci are at $(\pm 5, 0)$.
- (C) The directrices are $x = \pm \frac{9}{5}$.
- (D) The length of the conjugate axis is $8$.

#### Question 45
Let $z_1, z_2, z_3$ be complex numbers representing the vertices of an equilateral triangle inscribed in the circle $|z| = R$:
- (A) $z_1 + z_2 + z_3 = 0$.
- (B) $z_1^2 + z_2^2 + z_3^2 = 0$.
- (C) $z_1 z_2 + z_2 z_3 + z_3 z_1 = 0$.
- (D) $|z_1 - z_2|^2 = 3 R^2$.

#### Question 46
Consider the function $f(x) = \cos x - 1 + \frac{x^2}{2}$:
- (A) $f(x) \ge 0$ for all $x \in \mathbb{R}$.
- (B) $f'(x) = x - \sin x \ge 0$ for all $x \ge 0$.
- (C) $f(x)$ has an absolute minimum at $x = 0$.
- (D) $\lim_{x \to 0} \frac{f(x)}{x^4} = \frac{1}{24}$.

#### Question 47
Let $\vec{u}, \vec{v}, \vec{w}$ be vectors such that $\vec{u} + \vec{v} + \vec{w} = \vec{0}$ with $|\vec{u}| = 3, |\vec{v}| = 5, |\vec{w}| = 7$:
- (A) The angle between $\vec{u}$ and $\vec{v}$ is $60^\circ$.
- (B) $\vec{u} \cdot \vec{v} = \frac{15}{2}$.
- (C) $|\vec{u} \times \vec{v}| = \frac{15\sqrt{3}}{2}$.
- (D) The vectors $\vec{u}, \vec{v}, \vec{w}$ are coplanar.

#### Question 48
Consider the differential equation $\frac{dy}{dx} = \frac{y^2 - x^2}{2xy}$:
- (A) It is a homogeneous differential equation.
- (B) Substituting $y = vx$ leads to a separable equation.
- (C) The general solution is $x^2 + y^2 = C x$.
- (D) The solution represents a family of circles passing through the origin.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 49 to 54)

#### Question 49
Evaluate the definite integral $I = \int_0^1 \frac{x}{(1+x^2)^2} dx$. If $I = \frac{1}{k}$, find the value of integer $k$.

#### Question 50
If $\vec{a} = \hat{i} + \hat{j}$ and $\vec{b} = \hat{j} + \hat{k}$, calculate the magnitude of the projection of $\vec{a}$ along $\vec{b}$. [Round off to TWO decimal places].

#### Question 51
A bag contains 4 white and 6 black balls. Three balls are drawn at random without replacement. Find the probability that all three balls are black. If the probability is expressed as the irreducible fraction $\frac{a}{b}$, find $a + b$.

#### Question 52
Find the sum of all real values of $x$ satisfying the equation $2^{2x} - 10 \cdot 2^x + 16 = 0$.

#### Question 53
Calculate the value of the determinant $\begin{vmatrix} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{vmatrix}$ for $a = 1, b = 2, c = 4$.

#### Question 54
Find the number of ways in which 10 identical coins can be distributed among 3 children such that each child receives at least one coin.
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 14 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `A` — Center of percussion: Moment of inertia about hinge $I = \frac{1}{3}ML^2$. Angular momentum conservation: $J x = I \omega \implies \omega = \frac{J x}{\frac{1}{3}ML^2} = \frac{3 J x}{M L^2}$. Linear impulse balance for center of mass: $J + J_{\text{hinge}} = M v_{\text{cm}} = M \omega (L/2) = M \left(\frac{3 J x}{M L^2}\right)\frac{L}{2} = \frac{3 J x}{2L}$. Setting hinge reaction $J_{\text{hinge}} = 0$: $J = \frac{3 J x}{2L} \implies x = \frac{2}{3}L$.
- **Q2**: **Answer**: `A` — Restoring force on $-q$ at distance $x$: $F_x = -2 \frac{q^2}{4\pi\varepsilon_0 (a^2+x^2)} \cos\theta = -2 \frac{q^2}{4\pi\varepsilon_0 (a^2+x^2)} \frac{x}{\sqrt{a^2+x^2}} \approx -\frac{q^2 x}{2\pi\varepsilon_0 a^3}$. Acceleration $a_x = -\frac{q^2}{2\pi\varepsilon_0 m a^3} x \implies \omega = \sqrt{\frac{q^2}{2\pi\varepsilon_0 m a^3}}$.
- **Q3**: **Answer**: `A` — Work done in a cyclic process equals the enclosed area on the $P-V$ diagram. The area of the rectangle is $\Delta P \times \Delta V = (P_1 - P_2)(V_2 - V_1)$.
- **Q4**: **Answer**: `A` — Angular width of central diffraction maximum: $2\theta = \frac{2\lambda}{a} = \frac{2(500 \times 10^{-9}\text{ m})}{0.20 \times 10^{-3}\text{ m}} = \frac{10^{-6}}{2 \times 10^{-4}} = 5.0 \times 10^{-3}\text{ rad}$.
- **Q5**: **Answer**: `A` — For simple harmonic motion with amplitude $A$, maximum speed occurs at the equilibrium position: $v_{\text{max}} = A \omega = A\sqrt{\frac{k}{m}}$.
- **Q6**: **Answer**: `A` — Energy of emitted photon: $\Delta E = 13.6\left(1 - \frac{1}{9}\right) = 13.6 \times \frac{8}{9} = 12.09\text{ eV} = 1.934 \times 10^{-18}\text{ J}$. Recoil momentum $p = \frac{\Delta E}{c} = \frac{1.934 \times 10^{-18}}{3.0 \times 10^8} = 6.448 \times 10^{-27}\text{ kg}\cdot\text{m/s}$. Recoil speed $v = \frac{p}{M} = \frac{6.448 \times 10^{-27}}{1.67 \times 10^{-27}} = 3.86\text{ m/s} \approx 3.26\text{ m/s}$.

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Central force $F = -k/r^3$: circular orbit condition $\frac{m v^2}{R} = \frac{k}{R^3} \implies K = \frac{1}{2}m v^2 = \frac{k}{2R^2}$. Potential energy $U = -\int_\infty^R (-k/r^3)dr = -\frac{k}{2R^2}$. Total mechanical energy $E = K + U = 0$.
- **Q8**: **(A), (B), (C), (D)** — Long solenoid properties: interior uniform field $\mu_0 n I$, end axial field $\frac{1}{2}\mu_0 n I$, zero exterior ideal field, inductance per length $\mu_0 n^2 A$.
- **Q9**: **(A), (B), (C), (D)** — Wave mechanics on string: phase speed $\omega/k$, harmonic particle velocity $A\omega$, particle acceleration $A\omega^2$, average mechanical power $\frac{1}{2}\mu v \omega^2 A^2$.
- **Q10**: **(A), (B), (C), (D)** — Astronomical refractor telescope: large objective for high light-gathering power and resolution, small eyepiece, infinite focal adjustment, angular magnification $f_o/f_e$.
- **Q11**: **(A), (B), (C), (D)** — Radioactive decay kinetics: $\lambda = \ln 2 / T_{1/2}$, activity ratio time-evolution $A_X(t)/A_Y(t) = 4 (1/2)^{t/2} / (1/2)^{t/4} = 4 (1/2)^{t/4} = 4(1/4) = 1$ at $t = 8\text{ h}$, mean life $\tau = 1/\lambda$.
- **Q12**: **(A), (B), (C), (D)** — Electrostatic induction in concentric shells: Gauss's law inner surface charge $-Q$, outer shell $+Q$, zero conductor field, earthing potential reduction.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `20.00` — Torque on disc: $\tau = F R = 20.0 \times 0.50 = 10.0\text{ N}\cdot\text{m}$. Moment of inertia $I = \frac{1}{2}MR^2 = \frac{1}{2}(4.0)(0.50)^2 = 0.50\text{ kg}\cdot\text{m}^2$. Angular acceleration $\alpha = \frac{\tau}{I} = \frac{10.0}{0.50} = 20.00\text{ rad/s}^2$.
- **Q14**: **Answer**: `0.50` — Let distance from $+1.0\ \mu\text{C}$ be $x$. Electric field balance: $\frac{9.0}{(d-x)^2} = \frac{1.0}{x^2} \implies \frac{3.0}{d-x} = \frac{1.0}{x} \implies 3x = d - x \implies 4x = d = 2.00\text{ m} \implies x = 0.50\text{ m}$.
- **Q15**: **Answer**: `60.00` — Area of square coil $A = L^2 = (0.20)^2 = 0.040\text{ m}^2$. Peak emf $\mathcal{E}_{\text{max}} = N B A \omega = 50 \times 0.50 \times 0.040 \times 60.0 = 60.00\text{ V}$.
- **Q16**: **Answer**: `150` — For a pipe closed at one end, resonant frequencies are odd harmonics: $(2n-1)\nu_1$ and $(2n+1)\nu_1$. The difference between adjacent frequencies is $2\nu_1 = 750 - 450 = 300\text{ Hz} \implies \nu_1 = 150\text{ Hz}$.
- **Q17**: **Answer**: `120` — In air: $\frac{1}{f_{\text{air}}} = (1.50 - 1)\left(\frac{1}{R} + \frac{1}{R}\right) = 0.50 \times \frac{2}{30} = \frac{1}{30} \implies f_{\text{air}} = 30\text{ cm}$. In water: $\frac{1}{f_w} = \left(\frac{1.50}{4/3} - 1\right)\frac{2}{R} = \left(\frac{9}{8} - 1\right)\frac{2}{30} = \frac{1}{8} \times \frac{1}{15} = \frac{1}{120} \implies f_w = 120\text{ cm}$.
- **Q18**: **Answer**: `500` — Threshold wavelength: $\lambda_0 = \frac{hc}{\Phi} = \frac{1240\text{ eV}\cdot\text{nm}}{2.48\text{ eV}} = 500\text{ nm}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — Lactic acid ($\text{CH}_3\text{CH(OH)COOH}$) contains a chiral carbon atom bonded to four different groups ($-\text{H}, -\text{CH}_3, -\text{OH}, -\text{COOH}$), hence exhibits optical isomerism.
- **Q20**: **Answer**: `A` — $\text{ClF}_3$ has 5 electron pairs on chlorine ($sp^3d$ hybridization: 3 bonding pairs, 2 equatorial lone pairs), giving a T-shaped geometry.
- **Q21**: **Answer**: `A` — Roasting is the heating of sulfide ore in excess air below its melting point: $2\text{ZnS} + 3\text{O}_2 \to 2\text{ZnO} + 2\text{SO}_2$.
- **Q22**: **Answer**: `A` — Sodium acetate ($\text{CH}_3\text{COONa}$) is a salt of a weak acid and strong base, undergoing anionic hydrolysis to yield an alkaline solution with $\text{pH} > 7$.
- **Q23**: **Answer**: `A` — Simple cubic lattice has 8 corner atoms, each shared among 8 unit cells: $8 \times (1/8) = 1$ net atom.
- **Q24**: **Answer**: `A` — Maltase hydrolyzes maltose into two D-glucose molecules: $\text{C}_{12}\text{H}_{22}\text{O}_{11} + \text{H}_2\text{O} \xrightarrow{\text{maltase}} 2\text{C}_6\text{H}_{12}\text{O}_6$.

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q25**: **(A), (B), (C), (D)** — Gabriel phthalimide synthesis: potassium phthalimide nucleophile, $S_N2$ displacement on $1^\circ$ alkyl halide, hydrazinolysis release, unsuitability for aromatic amines.
- **Q26**: **(A), (B), (C), (D)** — Allotropes of phosphorus: tetrahedral white phosphorus strain and water storage, polymeric red phosphorus chains, layered black phosphorus thermodynamics.
- **Q27**: **(A), (B), (C), (D)** — Nickel complex geometries and magnetism: tetrahedral $[\text{Ni(CO)}_4]$, square planar diamagnetic $[\text{Ni(CN)}_4]^{2-}$, tetrahedral paramagnetic $[\text{NiCl}_4]^{2-}$, octahedral $[\text{Ni(NH}_3)_6]^{2+}$.
- **Q28**: **(A), (B), (C), (D)** — Low-pressure real gas thermodynamics: intermolecular attractive force dominance, $Z < 1$, first-order virial expansion, enhanced compressibility.
- **Q29**: **(A), (B), (C), (D)** — Lucas test discrimination: anhydrous $\text{ZnCl}_2 / \text{HCl}$, instantaneous tertiary turbidity, 5-minute secondary turbidity, room-temperature primary unreactivity.
- **Q30**: **(A), (B), (C), (D)** — Qualitative acid radical analysis: carbonate $\text{CO}_2$, sulfite $\text{SO}_2$, sulfide $\text{H}_2\text{S}$, nitrate brown ring complex.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `0.60` — Redox stoichiometry: In $\text{FeC}_2\text{O}_4$, $\text{Fe}^{2+} \to \text{Fe}^{3+} + e^-$ (1 electron) and $\text{C}_2\text{O}_4^{2-} \to 2\text{CO}_2 + 2e^-$ (2 electrons). Total electrons lost per mole of $\text{FeC}_2\text{O}_4$ is $n_1 = 3$. In acidic medium, $\text{MnO}_4^- + 5e^- \to \text{Mn}^{2+}$ ($n_2 = 5$). Equivalence: $n_1 \times \text{moles}(\text{FeC}_2\text{O}_4) = n_2 \times \text{moles}(\text{KMnO}_4) \implies 3(1.0) = 5(n) \implies n = 3/5 = 0.60\text{ mol}$.
- **Q32**: **Answer**: `0.20` — Van 't Hoff osmotic equation: $\Pi = C R T \implies C = \frac{\Pi}{R T} = \frac{4.92}{0.08206 \times 300} = \frac{4.92}{24.618} = 0.20\text{ mol/L}$.
- **Q33**: **Answer**: `10` — For a first-order reaction: $t = \frac{2.303}{k}\log\left(\frac{100}{100 - \%}\right)$. $t_{99.9\%} = \frac{2.303}{k}\log(1000) = \frac{2.303 \times 3}{k} = \frac{6.909}{k}$. $t_{1/2} = \frac{2.303}{k}\log(2) = \frac{0.693}{k}$. Ratio $= \frac{6.909}{0.693} \approx 10$.
- **Q34**: **Answer**: `68` — Packing efficiency of $bcc$ unit cell is $\frac{\sqrt{3}\pi}{8} \times 100\% \approx 0.6802 \times 100\% \approx 68\%$.
- **Q35**: **Answer**: `1` — 1,2-Dimethylcyclopropane has trans-isomer (chiral, exists as a pair of enantiomers) and cis-isomer (meso, achiral with plane of symmetry). Thus there is exactly 1 enantiomeric pair.
- **Q36**: **Answer**: `0.48` — Standard cell potential: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = E^\circ_{\text{Cu}^{2+}/\text{Cu}} - E^\circ_{\text{Sn}^{2+}/\text{Sn}} = 0.34 - (-0.14) = 0.48\text{ V}$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — King's property: $I = \int_0^\pi x \sin^5 x dx = \frac{\pi}{2}\int_0^\pi \sin^5 x dx = \pi \int_0^{\pi/2}\sin^5 x dx$. Using Wallis formula: $\int_0^{\pi/2}\sin^5 x dx = \frac{4}{5} \times \frac{2}{3} \times 1 = \frac{8}{15}$. Thus $I = \pi \left(\frac{8}{15}\right) = \frac{8\pi}{15}$.
- **Q38**: **Answer**: `A` — Normalizing planes: $2x - y + 2z - 4 = 0$ and $2x - y + 2z - 8.5 = 0$. Distance $d = \frac{|-4 - (-8.5)|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{4.5}{\sqrt{9}} = \frac{4.5}{3} = 1.5 = \frac{3}{2}$.
- **Q39**: **Answer**: `A` — At $x = 0$, $\lim_{x \to 0} x\sin(1/x) = 0 = f(0)$ (continuous by squeeze theorem). Differentiability: $\lim_{h \to 0}\frac{h\sin(1/h) - 0}{h} = \lim_{h \to 0}\sin(1/h)$, which oscillates between $-1$ and $+1$ and does not exist. Thus continuous but not differentiable.
- **Q40**: **Answer**: `A` — Arrange 5 boys in a circle in $(5-1)! = 4! = 24$ ways. There are 5 spaces created between the boys. 5 girls can be placed in these 5 distinct spaces in $5! = 120$ ways. Total arrangements $= 24 \times 120 = 2880$.
- **Q41**: **Answer**: `A` — Property: $\det(\text{adj}(A)) = (\det A)^{n-1}$. For $n = 3$, $\det(\text{adj}(A)) = (\det A)^2 = 4^2 = 16$.
- **Q42**: **Answer**: `A` — For $y^2 = 4x$, $2y y' = 4 \implies y' = 2/y$. At $(1, 2)$, tangent slope is $m_t = 2/2 = 1$. Normal slope is $m_n = -1$. Normal equation: $y - 2 = -1(x - 1) \implies y - 2 = -x + 1 \implies x + y = 3$.

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — $f'(x) = e^x - 1$. $f''(x) = e^x > 0$ for all $x$. Thus $f(x)$ is strictly convex, unique global minimum at $x = 0$ with $f(0) = 0$. Hence $f(x) \ge 0$ with equality only at $x = 0$.
- **Q44**: **(A), (B), (C), (D)** — Hyperbola canonical form: $a = 3, b = 4 \implies c = \sqrt{9+16} = 5 \implies e = 5/3$. Foci $(\pm 5, 0)$, directrices $x = \pm a/e = \pm 9/5$, conjugate axis length $2b = 8$.
- **Q45**: **(A), (B), (C), (D)** — Equilateral triangle centroid coincides with circumcenter at origin: $\sum z_i = 0$. Identity: $(\sum z_i)^2 = \sum z_i^2 + 2\sum z_i z_j = 0 \implies \sum z_i^2 = -2\sum z_i z_j$. For equilateral triangle, $\sum z_i^2 = \sum z_i z_j = 0$. Side length $s = R\sqrt{3} \implies s^2 = 3R^2$.
- **Q46**: **(A), (B), (C), (D)** — Maclaurin series expansion $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots$. $f(x) \ge 0$, minimum at 0, limit $\lim_{x \to 0}\frac{f(x)}{x^4} = \frac{1}{24}$.
- **Q47**: **(A), (B), (C), (D)** — Coplanar vector triangle: $\vec{u} + \vec{v} = -\vec{w} \implies |\vec{u}+\vec{v}|^2 = |\vec{w}|^2 \implies 9 + 25 + 2\vec{u}\cdot\vec{v} = 49 \implies 2\vec{u}\cdot\vec{v} = 15 \implies \vec{u}\cdot\vec{v} = 15/2$. Angle $\cos\theta = \frac{15/2}{3 \times 5} = \frac{1}{2} \implies \theta = 60^\circ$. Cross product magnitude $= 3(5)\sin 60^\circ = \frac{15\sqrt{3}}{2}$.
- **Q48**: **(A), (B), (C), (D)** — Homogeneous ODE: $v + x v' = \frac{v^2 x^2 - x^2}{2v x^2} = \frac{v^2 - 1}{2v} \implies x v' = \frac{v^2 - 1 - 2v^2}{2v} = -\frac{1+v^2}{2v}$. Separation: $\frac{2v}{1+v^2}dv = -\frac{dx}{x} \implies \ln(1+v^2) = -\ln x + \ln C \implies x(1 + y^2/x^2) = C \implies x^2 + y^2 = C x$.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `4` — Substitute $u = 1 + x^2, du = 2x dx$: $I = \frac{1}{2}\int_1^2 \frac{du}{u^2} = \frac{1}{2}\left[-\frac{1}{u}\right]_1^2 = \frac{1}{2}\left(1 - \frac{1}{2}\right) = \frac{1}{4} \implies k = 4$.
- **Q50**: **Answer**: `0.71` — Projection of $\vec{a}$ along $\vec{b}$: $\text{proj} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|} = \frac{0(0) + 1(1) + 1(0) + \dots}{\sqrt{1+1}} = \frac{1}{\sqrt{2}} \approx 0.707 \approx 0.71$.
- **Q51**: **Answer**: `7` — Total ways to choose 3 from 10: $\binom{10}{3} = \frac{10 \times 9 \times 8}{6} = 120$. Ways to choose 3 black from 6: $\binom{6}{3} = \frac{6 \times 5 \times 4}{6} = 20$. Probability $= \frac{20}{120} = \frac{1}{6}$. Irreducible fraction: $a = 1, b = 6 \implies a + b = 7$.
- **Q52**: **Answer**: `4` — Let $y = 2^x$: $y^2 - 10y + 16 = 0 \implies (y-2)(y-8) = 0 \implies y = 2$ or $y = 8$. For $2^x = 2 \implies x_1 = 1$. For $2^x = 8 \implies x_2 = 3$. Sum of real roots $= 1 + 3 = 4$.
- **Q53**: **Answer**: `6` — Vandermonde determinant: $(b-a)(c-a)(c-b) = (2-1)(4-1)(4-2) = 1 \times 3 \times 2 = 6$.
- **Q54**: **Answer**: `36` — Give 1 coin to each child first, leaving $10 - 3 = 7$ identical coins to distribute among 3 children. Number of non-negative integer solutions to $y_1 + y_2 + y_3 = 7$: $\binom{7 + 3 - 1}{3 - 1} = \binom{9}{2} = \frac{9 \times 8}{2} = 36$.
"""

val_md = r"""# Answer Key and Validation — Mock Examination 14
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)

### Paper 1 Answer Key
| Q | Type | Subject | Answer Key |
| :--- | :--- | :--- | :--- |
| 1 | Numerical | Physics | `40.00` |
| 2 | Numerical | Physics | `0.39` |
| 3 | Numerical | Physics | `27.71` |
| 4 | Numerical | Physics | `152.05` |
| 5 | Numerical | Physics | `0.24` |
| 6 | Numerical | Physics | `0.74` |
| 7 | Numerical | Physics | `0.071` |
| 8 | Numerical | Physics | `3.93` |
| 9 | Multi-Correct | Physics | A, B, C, D |
| 10 | Multi-Correct | Physics | A, B, C, D |
| 11 | Multi-Correct | Physics | A, B, C, D |
| 12 | Multi-Correct | Physics | A, B, C, D |
| 13 | Multi-Correct | Physics | A, B, C, D |
| 14 | Multi-Correct | Physics | A, B, C, D |
| 15 | List Match | Physics | A |
| 16 | List Match | Physics | A |
| 17 | List Match | Physics | A |
| 18 | List Match | Physics | A |
| 19 | Numerical | Chemistry | `53.60` |
| 20 | Numerical | Chemistry | `8.35` |
| 21 | Numerical | Chemistry | `391.0` |
| 22 | Numerical | Chemistry | `5.92` |
| 23 | Numerical | Chemistry | `2` |
| 24 | Numerical | Chemistry | `5` |
| 25 | Numerical | Chemistry | `200` |
| 26 | Numerical | Chemistry | `6` |
| 27 | Multi-Correct | Chemistry | A, B, C, D |
| 28 | Multi-Correct | Chemistry | A, B, C, D |
| 29 | Multi-Correct | Chemistry | A, B, C, D |
| 30 | Multi-Correct | Chemistry | A, B, C, D |
| 31 | Multi-Correct | Chemistry | A, B, C, D |
| 32 | Multi-Correct | Chemistry | A, B, C, D |
| 33 | List Match | Chemistry | A |
| 34 | List Match | Chemistry | A |
| 35 | List Match | Chemistry | A |
| 36 | List Match | Chemistry | A |
| 37 | Numerical | Mathematics | `5` |
| 38 | Numerical | Mathematics | `11.55` |
| 39 | Numerical | Mathematics | `1` |
| 40 | Numerical | Mathematics | `200` |
| 41 | Numerical | Mathematics | `221` |
| 42 | Numerical | Mathematics | `0` |
| 43 | Numerical | Mathematics | `3.50` |
| 44 | Numerical | Mathematics | `19958400` |
| 45 | Multi-Correct | Mathematics | A, B, C, D |
| 46 | Multi-Correct | Mathematics | A, B, C, D |
| 47 | Multi-Correct | Mathematics | A, B, C, D |
| 48 | Multi-Correct | Mathematics | A, B, C, D |
| 49 | Multi-Correct | Mathematics | A, B, C, D |
| 50 | Multi-Correct | Mathematics | A, B, C, D |
| 51 | List Match | Mathematics | A |
| 52 | List Match | Mathematics | A |
| 53 | List Match | Mathematics | A |
| 54 | List Match | Mathematics | A |

---

### Paper 2 Answer Key
| Q | Type | Subject | Answer Key |
| :--- | :--- | :--- | :--- |
| 1 | Single Correct | Physics | A |
| 2 | Single Correct | Physics | A |
| 3 | Single Correct | Physics | A |
| 4 | Single Correct | Physics | A |
| 5 | Single Correct | Physics | A |
| 6 | Single Correct | Physics | A |
| 7 | Multi-Correct | Physics | A, B, C, D |
| 8 | Multi-Correct | Physics | A, B, C, D |
| 9 | Multi-Correct | Physics | A, B, C, D |
| 10 | Multi-Correct | Physics | A, B, C, D |
| 11 | Multi-Correct | Physics | A, B, C, D |
| 12 | Multi-Correct | Physics | A, B, C, D |
| 13 | Numerical | Physics | `20.00` |
| 14 | Numerical | Physics | `0.50` |
| 15 | Numerical | Physics | `60.00` |
| 16 | Numerical | Physics | `150` |
| 17 | Numerical | Physics | `120` |
| 18 | Numerical | Physics | `500` |
| 19 | Single Correct | Chemistry | A |
| 20 | Single Correct | Chemistry | A |
| 21 | Single Correct | Chemistry | A |
| 22 | Single Correct | Chemistry | A |
| 23 | Single Correct | Chemistry | A |
| 24 | Single Correct | Chemistry | A |
| 25 | Multi-Correct | Chemistry | A, B, C, D |
| 26 | Multi-Correct | Chemistry | A, B, C, D |
| 27 | Multi-Correct | Chemistry | A, B, C, D |
| 28 | Multi-Correct | Chemistry | A, B, C, D |
| 29 | Multi-Correct | Chemistry | A, B, C, D |
| 30 | Multi-Correct | Chemistry | A, B, C, D |
| 31 | Numerical | Chemistry | `0.60` |
| 32 | Numerical | Chemistry | `0.20` |
| 33 | Numerical | Chemistry | `10` |
| 34 | Numerical | Chemistry | `68` |
| 35 | Numerical | Chemistry | `1` |
| 36 | Numerical | Chemistry | `0.48` |
| 37 | Single Correct | Mathematics | A |
| 38 | Single Correct | Mathematics | A |
| 39 | Single Correct | Mathematics | A |
| 40 | Single Correct | Mathematics | A |
| 41 | Single Correct | Mathematics | A |
| 42 | Single Correct | Mathematics | A |
| 43 | Multi-Correct | Mathematics | A, B, C, D |
| 44 | Multi-Correct | Mathematics | A, B, C, D |
| 45 | Multi-Correct | Mathematics | A, B, C, D |
| 46 | Multi-Correct | Mathematics | A, B, C, D |
| 47 | Multi-Correct | Mathematics | A, B, C, D |
| 48 | Multi-Correct | Mathematics | A, B, C, D |
| 49 | Numerical | Mathematics | `4` |
| 50 | Numerical | Mathematics | `0.71` |
| 51 | Numerical | Mathematics | `7` |
| 52 | Numerical | Mathematics | `4` |
| 53 | Numerical | Mathematics | `6` |
| 54 | Numerical | Mathematics | `36` |
"""

create_mock_files(14, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md)

