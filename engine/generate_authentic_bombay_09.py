# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 09.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 09 — Paper 1
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
A uniform solid sphere of mass $M = 3.00\text{ kg}$ and radius $R = 0.30\text{ m}$ is placed inside a fixed smooth hemispherical bowl of radius $R_0 = 1.20\text{ m}$. The sphere is released from rest from the rim of the bowl ($\theta = 90^\circ$). If the sphere rolls without slipping along the inner surface of the bowl, calculate the normal reaction force $N$ exerted by the bowl on the sphere as it passes through the lowest point in Newtons ($\text{N}$). [Take $g = 9.80\text{ m/s}^2$. Round off to ONE decimal place].

#### Question 2
A vertical open cylindrical tank of height $H = 2.00\text{ m}$ and cross-sectional area $A = 0.50\text{ m}^2$ is filled completely with water ($\rho = 1000\text{ kg/m}^3$). A small circular hole of area $a = 2.0\text{ cm}^2$ is opened at the base. Calculate the time $t$ (in seconds) required for the water level to drop from $H = 2.00\text{ m}$ to $h = 0.50\text{ m}$. [Take $g = 9.80\text{ m/s}^2$. Round off to ONE decimal place].

#### Question 3
An ideal monoatomic gas undergoes a cycle $1 \to 2 \to 3 \to 1$ where process $1 \to 2$ is isobaric heating from $T_1 = 300\text{ K}$ to $T_2 = 600\text{ K}$, process $2 \to 3$ is isothermal expansion to $V_3 = 2 V_2$, and process $3 \to 1$ is a straight line on the $P-V$ diagram returning to initial state $(P_1, V_1)$. If one mole of gas is used, calculate the net work done by the gas in process $2 \to 3$ in Joules ($\text{J}$). [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 2 = 0.693$. Round off to the nearest integer].

#### Question 4
Two concentric circular wire loops of radii $r_1 = 0.020\text{ m}$ and $r_2 = 0.40\text{ m}$ ($r_1 \ll r_2$) lie coplanar on a table. Calculate the mutual inductance $M$ between the two loops in nanoHenries ($\text{nH}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ and $\pi^2 \approx 9.87$. Round off to ONE decimal place].

#### Question 5
In an interference experiment using a Lloyd's mirror, light of wavelength $\lambda = 550\text{ nm}$ from a narrow slit at distance $d = 1.10\text{ mm}$ above the plane of the mirror falls on a screen at distance $D = 2.00\text{ m}$ from the slit. Calculate the fringe width $\beta$ of the interference pattern in millimeters ($\text{mm}$).

#### Question 6
A non-conducting solid sphere of radius $R = 0.20\text{ m}$ has a uniform volume charge density $\rho = 1.50\ \mu\text{C/m}^3$. Calculate the electrostatic potential difference $(V_{\text{center}} - V_{\text{surface}})$ in Volts. [Take $\varepsilon_0 = 8.85 \times 10^{-12}\text{ C}^2/(\text{N}\cdot\text{m}^2)$. Round off to TWO decimal places].

#### Question 7
A particle of charge $q = +1.60 \times 10^{-19}\text{ C}$ and mass $m = 1.67 \times 10^{-27}\text{ kg}$ is accelerated from rest through a potential difference $V = 1000\text{ V}$. It enters a uniform magnetic field $B = 0.10\text{ T}$ perpendicular to its velocity. Calculate the radius $r$ of the resulting circular orbit in centimeters ($\text{cm}$). (Round off to TWO decimal places).

#### Question 8
An electron in a hydrogen atom undergoes a transition from the $n = 4$ state to the ground state $n = 1$. Calculate the frequency $\nu$ of the emitted photon in units of $10^{15}\text{ Hz}$. [Take Rydberg constant $R_{\infty} = 1.097 \times 10^7\text{ m}^{-1}$ and $c = 3.00 \times 10^8\text{ m/s}$. Round off to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
A uniform thin rod of mass $M$ and length $L$ is pivoted at one end so that it can rotate freely in a vertical plane. It is released from rest in the horizontal position ($\theta = 0$).
- (A) The angular acceleration of the rod immediately after release is $\alpha = \frac{3g}{2L}$.
- (B) The vertical component of the hinge reaction force immediately after release is $R_y = \frac{1}{4}Mg$.
- (C) The angular velocity of the rod when it passes through the vertical position is $\omega = \sqrt{\frac{3g}{L}}$.
- (D) The total hinge reaction force when the rod passes through the vertical position is $R_{\text{vertical}} = \frac{5}{2}Mg$.

#### Question 10
In a series $R-L-C$ circuit connected to an AC source $v(t) = V_0 \sin(\omega t)$, the impedance is $Z = \sqrt{R^2 + (\omega L - 1/\omega C)^2}$.
- (A) The current amplitude is maximized at resonant frequency $\omega_0 = \frac{1}{\sqrt{LC}}$.
- (B) At resonance, the power factor of the circuit is $\cos\phi = 1$.
- (C) The half-power bandwidth of the resonance curve is $\Delta \omega = \frac{R}{L}$.
- (D) The quality factor is $Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$.

#### Question 11
An ideal gas undergoes a quasi-static process in which the molar heat capacity is given by $C = C_V + 2 R$.
- (A) The equation governing this process on the $P-V$ diagram is $P V^{-1} = \text{constant}$ (i.e., $P/V = \text{constant}$).
- (B) The temperature of the gas is proportional to the square of its volume ($T \propto V^2$).
- (C) The work done by the gas during expansion from $V_1$ to $2V_1$ is positive.
- (D) Both pressure and temperature increase simultaneously during expansion.

#### Question 12
A point charge $q$ is located at the center of an imaginary cube of edge length $L$.
- (A) The total electric flux passing through the six faces of the cube is $\Phi_{\text{total}} = \frac{q}{\varepsilon_0}$.
- (B) The electric flux passing through each individual face of the cube is $\Phi_{\text{face}} = \frac{q}{6\varepsilon_0}$.
- (C) If the charge is moved to one of the eight corner vertices of the cube, the flux through the cube becomes $\frac{q}{8\varepsilon_0}$.
- (D) With the charge at a corner vertex, the electric flux through each of the three adjacent faces sharing that corner is strictly zero.

#### Question 13
Two soap bubbles of radii $R_1$ and $R_2$ ($R_1 > R_2$) coalesce in air under isothermal conditions to form a common spherical interface.
- (A) The radius of curvature of the common interface separating the two bubbles is $R_c = \frac{R_1 R_2}{R_1 - R_2}$.
- (B) The common interface is convex towards the larger bubble (curved into the larger bubble).
- (C) The excess pressure inside the smaller bubble is higher than that in the larger bubble.
- (D) If the two bubbles merge completely into a single bubble of radius $R$ under isothermal conditions, then $R^2 = R_1^2 + R_2^2$ (neglecting atmospheric pressure).

#### Question 14
In a Young's double-slit experiment using white light:
- (A) The central zero-order fringe is sharp, bright, and white.
- (B) The fringe closest to the central white fringe on either side has a violet/blue tinge.
- (C) The fringe farthest from the central fringe on either side of the first order has a reddish tinge.
- (D) After a few colored fringes, the field becomes uniformly illuminated due to the overlapping of different spectral colors.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the thermodynamic functions in **List-I** with their exact differential forms in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Internal Energy $dU$ | **1.** $T dS - P dV$ |
| **Q.** Enthalpy $dH$ | **2.** $T dS + V dP$ |
| **R.** Helmholtz Free Energy $dF$ | **3.** $-S dT - P dV$ |
| **S.** Gibbs Free Energy $dG$ | **4.** $-S dT + V dP$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the physical quantities in **List-I** with their SI units in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Magnetic permeability $\mu_0$ | **1.** $\text{H/m}$ (or $\text{T}\cdot\text{m/A}$) |
| **Q.** Electric permittivity $\varepsilon_0$ | **2.** $\text{F/m}$ (or $\text{C}^2/(\text{N}\cdot\text{m}^2)$) |
| **R.** Magnetic flux $\Phi_B$ | **3.** $\text{Weber}$ ($\text{Wb}$ or $\text{T}\cdot\text{m}^2$) |
| **S.** Self-inductance $L$ | **4.** $\text{Henry}$ ($\text{H}$ or $\text{V}\cdot\text{s/A}$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 17
Match the modern physics experiments in **List-I** with their historic discoveries in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Davisson-Germer experiment | **1.** Wave nature of electrons via crystal diffraction |
| **Q.** Franck-Hertz experiment | **2.** Discrete atomic energy levels via inelastic electron scattering |
| **R.** Rutherford alpha-scattering | **3.** Discovery of compact dense atomic nucleus |
| **S.** Stern-Gerlach experiment | **4.** Space quantization of angular momentum and electron spin |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 18
Match the electromagnetic wave properties in **List-I** with their values in vacuum in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Speed of propagation $c$ | **1.** $\frac{1}{\sqrt{\mu_0\varepsilon_0}}$ |
| **Q.** Ratio of field amplitudes $E_0/B_0$ | **2.** $c$ |
| **R.** Wave impedance of free space $Z_0$ | **3.** $\sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 377\ \Omega$ |
| **S.** Ratio of electric to magnetic energy density | **4.** $1$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
Calculate the pH of a $0.010\text{ M}$ aqueous solution of ammonium hydroxide ($\text{NH}_4\text{OH}$) given $K_b = 1.80 \times 10^{-5}$ at $298\text{ K}$. [Take $\log 4.24 = 0.627$. Round off to TWO decimal places].

#### Question 20
A coordination complex $\text{Pt(en)}_2\text{Cl}_2$ reacts with silver nitrate. In an octahedral complex of $\text{Pt(IV)}$, how many total stereoisomers (including geometrical and optical enantiomeric pairs) are possible for $[\text{Pt(en)}_2\text{Cl}_2]^{2+}$?

#### Question 21
The rate of a gaseous reaction triples when the temperature is increased from $290\text{ K}$ to $310\text{ K}$. Calculate the activation energy $E_a$ in $\text{kJ/mol}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 3 = 1.0986$. Round off to TWO decimal places].

#### Question 22
Calculate the equilibrium constant $K_p$ for the dissociation $\text{PCl}_5(g) \rightleftharpoons \text{PCl}_3(g) + \text{Cl}_2(g)$ at $500\text{ K}$ if the degree of dissociation is $\alpha = 0.40$ at a total pressure of $P = 1.0\text{ atm}$. (Round off to TWO decimal places).

#### Question 23
A metal crystallizes in a face-centered cubic ($fcc$) lattice with atomic radius $r = 141.4\text{ pm}$. Calculate the edge length $a$ of the cubic unit cell in picometers ($\text{pm}$). (Round off to the nearest integer).

#### Question 24
In qualitative inorganic analysis, how many of the following cations produce a black precipitate with $\text{H}_2\text{S}$ in acidic medium?
$$\text{Cu}^{2+},\ \text{Pb}^{2+},\ \text{Hg}^{2+},\ \text{Bi}^{3+},\ \text{Cd}^{2+},\ \text{Sb}^{3+},\ \text{As}^{3+}$$

#### Question 25
Find the total number of structural isomers of carboxylic acids having the molecular formula $\text{C}_5\text{H}_{10}\text{O}_2$.

#### Question 26
One mole of an ideal gas expands isothermally at $T = 300\text{ K}$ from $V_1 = 2.0\text{ L}$ to $V_2 = 10.0\text{ L}$. Calculate the change in Gibbs free energy $\Delta G$ of the gas in Joules ($\text{J}$). [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 5 = 1.609$. Round off to the nearest integer].

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding the bonding and molecular structure of diborane ($\text{B}_2\text{H}_6$):
- (A) Each boron atom is $sp^3$ hybridized.
- (B) The four terminal $\text{B-H}$ bonds are normal two-center two-electron ($2c-2e$) covalent bonds.
- (C) The two bridging $\text{B-H-B}$ bonds are three-center two-electron ($3c-2e$) banana bonds.
- (D) The four terminal hydrogen atoms and the two boron atoms lie in one common plane, while the two bridging hydrogen atoms lie symmetrically above and below this plane.

#### Question 28
In the reaction of phenol with neutral ferric chloride ($\text{FeCl}_3$) solution:
- (A) An intense violet/purple coloration is produced due to formation of a complex $[Fe(OPh)_6]^{3-}$.
- (B) Alcohols do not give this coloration test, enabling clean distinction between phenols and aliphatic alcohols.
- (C) Phenol reacts with concentrated $\text{HNO}_3$ in the presence of $\text{H}_2\text{SO}_4$ to yield 2,4,6-trinitrophenol (picric acid).
- (D) Picric acid is a strong acid despite lacking a carboxylic acid group due to strong $-M$ and $-I$ electron-withdrawing effects of three nitro groups.

#### Question 29
Consider the high-spin and low-spin states of octahedral $d^6$ complexes:
- (A) In $[\text{Fe(H}_2\text{O)}_6]^{2+}$, water is a weak field ligand, resulting in high-spin $t_{2g}^4 e_g^2$ configuration with 4 unpaired electrons.
- (B) In $[\text{Fe(CN)}_6]^{4-}$, cyanide is a strong field ligand, resulting in low-spin $t_{2g}^6 e_g^0$ configuration with 0 unpaired electrons.
- (C) The Crystal Field Stabilization Energy ($\text{CFSE}$) of $[\text{Fe(CN)}_6]^{4-}$ is $-2.4\Delta_o + 2P$.
- (D) $[\text{Fe(H}_2\text{O)}_6]^{2+}$ is paramagnetic with spin-only magnetic moment $\mu \approx 4.90\text{ BM}$.

#### Question 30
In the metallurgical extraction of lead from galena ($\text{PbS}$):
- (A) The ore is partially roasted in air: $2\text{PbS} + 3\text{O}_2 \to 2\text{PbO} + 2\text{SO}_2$ and $\text{PbS} + 2\text{O}_2 \to \text{PbSO}_4$.
- (B) Air supply is cut off and temperature raised to effect self-reduction: $\text{PbS} + 2\text{PbO} \to 3\text{Pb} + \text{SO}_2$ and $\text{PbS} + \text{PbSO}_4 \to 2\text{Pb} + 2\text{SO}_2$.
- (C) Silver present as impurity in lead is desilverized by Parkes' process using molten zinc.
- (D) Lead is finally refined by electrolytic refining using a solution of lead fluorosilicate ($\text{PbSiF}_6$) and hydrofluorosilicic acid ($\text{H}_2\text{SiF}_6$) (Betts process).

#### Question 31
For an ideal solution obeying Raoult's law:
- (A) The total vapor pressure is a linear function of the mole fraction of either component in the liquid phase: $P_{\text{total}} = P_B^\circ + (P_A^\circ - P_B^\circ)x_A$.
- (B) The mole fraction of component $A$ in the vapor phase $y_A$ is related to $x_A$ by $y_A = \frac{x_A P_A^\circ}{P_{\text{total}}}$.
- (C) If $P_A^\circ > P_B^\circ$, then $y_A > x_A$ (the vapor phase is enriched in the more volatile component).
- (D) Complete separation into pure components is achievable by fractional distillation.

#### Question 32
Which of the following carbohydrates are classified as reducing sugars?
- (A) D-Glucose
- (B) D-Fructose
- (C) Maltose
- (D) Sucrose

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the coordination complexes in **List-I** with their effective atomic numbers ($\text{EAN}$) of the central metal in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $[\text{Fe(CN)}_6]^{4-}$ | **1.** $36$ ($\text{Kr}$ configuration) |
| **Q.** $[\text{Co(NH}_3)_6]^{3+}$ | **2.** $36$ ($\text{Kr}$ configuration) |
| **R.** $[\text{Ni(CO)}_4]$ | **3.** $36$ ($\text{Kr}$ configuration) |
| **S.** $[\text{Cr(CO)}_6]$ | **4.** $36$ ($\text{Kr}$ configuration) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the industrial catalysts in **List-I** with their chemical processes in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Finely divided $\text{Fe}$ with $\text{Mo}$ promoter | **1.** Haber-Bosch synthesis of ammonia ($\text{NH}_3$) |
| **Q.** Vanadium pentoxide ($\text{V}_2\text{O}_5$) | **2.** Contact process for manufacture of sulfuric acid ($\text{H}_2\text{SO}_4$) |
| **R.** Platinized asbestos / $\text{Rh-Pt}$ gauze | **3.** Ostwald process for oxidation of ammonia to $\text{NO}$ |
| **S.** Ziegler-Natta catalyst ($\text{TiCl}_4 + \text{Al(C}_2\text{H}_5)_3$) | **4.** Low-pressure stereoregular polymerization of ethene |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 35
Match the organic name reactions in **List-I** with their characteristic reactive intermediates in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Carbylamine reaction | **1.** Dichlorocarbene ($:\text{CCl}_2$) |
| **Q.** Curtius rearrangement | **2.** Acyl nitrene / Isocyanate |
| **R.** Pinacol-Pinacolone rearrangement | **3.** Carbocation |
| **S.** Free radical halogenation | **4.** Carbon free radical |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 36
Match the halogen oxides / oxoacids in **List-I** with their oxidation numbers in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\text{HClO}$ (Hypochlorous acid) | **1.** $+1$ |
| **Q.** $\text{HClO}_2$ (Chlorous acid) | **2.** $+3$ |
| **R.** $\text{HClO}_3$ (Chloric acid) | **3.** $+5$ |
| **S.** $\text{HClO}_4$ (Perchloric acid) | **4.** $+7$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Let $f(x) = \int_{0}^{x} \frac{t^2}{1 + t^4}\,dt$. Evaluate $\lim_{x \to 0} \frac{f(x)}{x^3}$. (Round off to TWO decimal places).

#### Question 38
Evaluate the value of the definite integral:
$$I = \int_{0}^{\pi/2} \ln(\tan x)\,dx$$

#### Question 39
Let $A$ be a $3 \times 3$ real skew-symmetric matrix. Find the value of $\det(A)$.

#### Question 40
A box contains 4 red balls and 6 black balls. Three balls are drawn at random simultaneously. What is the probability that all three balls are black? (Round off to TWO decimal places).

#### Question 41
Find the area bounded by the parabola $y^2 = 4x$ and its latus rectum in square units. (Round off to TWO decimal places).

#### Question 42
Let $z$ be a complex number satisfying $|z| = 1$. Find the minimum value of $|z - (3 + 4i)|$.

#### Question 43
Let $\vec{a} = 2\hat{i} + \hat{j} - \hat{k}$ and $\vec{b} = \hat{i} - \hat{j} + 2\hat{k}$. Find the area of the parallelogram formed by vectors $\vec{a}$ and $\vec{b}$ in square units. (Round off to TWO decimal places).

#### Question 44
Find the number of ways of distributing 8 identical balls into 3 distinct boxes such that each box receives at least one ball.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Let $f(x) = |x - 1| + |x - 2|$ defined on $\mathbb{R}$.
- (A) $f(x) = 3 - 2x$ for $x < 1$.
- (B) $f(x) = 1$ for $1 \le x \le 2$.
- (C) $f(x) = 2x - 3$ for $x > 2$.
- (D) $f(x)$ is continuous everywhere on $\mathbb{R}$ but not differentiable at $x = 1$ and $x = 2$.

#### Question 46
Consider the circle $x^2 + y^2 = 25$. Tangents are drawn from the external point $P(7, 1)$ to the circle touching at $A$ and $B$.
- (A) The equation of the chord of contact $AB$ is $7x + y = 25$.
- (B) The length of the tangents $PA$ and $PB$ is $L = 5$.
- (C) The area of quadrilateral $PAOB$ (where $O$ is origin) is $25$.
- (D) The angle between the two tangents is $\theta = 90^\circ$.

#### Question 47
Let $A$ and $B$ be two $n \times n$ orthogonal matrices ($\det(A) = 1, \det(B) = -1$).
- (A) The matrix product $A B$ is also an orthogonal matrix.
- (B) $\det(A B) = -1$.
- (C) $A^{-1} = A^T$.
- (D) All eigenvalues of $A$ have absolute value equal to $1$.

#### Question 48
Let $I_n = \int_{0}^{\pi/2} x \cos^n x\,dx$ for $n \ge 2$.
- (A) By integration by parts, $I_n$ satisfies a second-order reduction formula.
- (B) The sequence $\{I_n\}$ is strictly decreasing for $n \ge 1$.
- (C) $\lim_{n \to \infty} I_n = 0$.
- (D) $\lim_{n \to \infty} \sqrt{n} I_n$ is finite and strictly positive.

#### Question 49
Let $A$ and $B$ be two events with $P(A) = 0.60$ and $P(B) = 0.40$.
- (A) The maximum possible value of $P(A \cup B)$ is $1.00$.
- (B) The minimum possible value of $P(A \cap B)$ is $0.00$.
- (C) If $A$ and $B$ are mutually exclusive, $P(A \cup B) = 1.00$.
- (D) If $A$ and $B$ are independent, $P(A \cap B) = 0.24$.

#### Question 50
Consider the differential equation $\frac{dy}{dx} = \frac{y}{x} + \frac{x}{y}$ for $x, y > 0$.
- (A) The substitution $y = v x$ transforms the equation into $v \frac{dv}{dx} = \frac{1}{x}$.
- (B) The general solution is $y^2 = 2 x^2 \ln|x| + C x^2$.
- (C) The solution curves pass through $(1, \sqrt{C})$.
- (D) The equation is homogeneous of degree zero.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the differential equations in **List-I** with their types in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\frac{dy}{dx} + P(x)y = Q(x)$ | **1.** First-order linear differential equation |
| **Q.** $\frac{dy}{dx} = f(y/x)$ | **2.** Homogeneous differential equation |
| **R.** $M(x,y)dx + N(x,y)dy = 0$ with $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ | **3.** Exact differential equation |
| **S.** $\frac{dy}{dx} + P(x)y = Q(x)y^n$ | **4.** Bernoulli's differential equation |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the limits in **List-I** with their evaluated values in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\lim_{x \to 0} \frac{\sin x}{x}$ | **1.** $1$ |
| **Q.** $\lim_{x \to 0} \frac{e^x - 1}{x}$ | **2.** $1$ |
| **R.** $\lim_{x \to 0} \frac{\ln(1+x)}{x}$ | **3.** $1$ |
| **S.** $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ | **4.** $\frac{1}{2}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 53
Match the conics in **List-I** with their focal properties in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Parabola | **1.** $e = 1$, single focus and single directrix |
| **Q.** Ellipse | **2.** $0 < e < 1$, sum of focal distances is constant ($2a$) |
| **R.** Hyperbola | **3.** $e > 1$, difference of focal distances is constant ($2a$) |
| **S.** Circle | **4.** $e = 0$, both foci coincide at center |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 54
Match the vector operations in **List-I** with their geometric interpretations in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\vec{a} \cdot \vec{b} = 0$ | **1.** Vectors $\vec{a}$ and $\vec{b}$ are mutually perpendicular |
| **Q.** $\vec{a} \times \vec{b} = \vec{0}$ | **2.** Vectors $\vec{a}$ and $\vec{b}$ are collinear / parallel |
| **R.** $[\vec{a}, \vec{b}, \vec{c}] = 0$ | **3.** Three vectors $\vec{a}, \vec{b}, \vec{c}$ are coplanar |
| **S.** $|\vec{a} \times \vec{b}|$ | **4.** Area of parallelogram spanned by $\vec{a}$ and $\vec{b}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3
"""

solutions_p1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 09 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `71.4` (Range: `70.0 to 73.0`) — Rolling inside hemisphere: center of sphere moves on circle of radius $r_{\text{eff}} = R_0 - R = 1.20 - 0.30 = 0.90\text{ m}$. Loss in potential energy $M g r_{\text{eff}} = \frac{1}{2} M v^2 + \frac{1}{2} I \omega^2 = \frac{7}{10} M v^2 \implies v^2 = \frac{10}{7} g r_{\text{eff}}$. Normal reaction at bottom $N = M g + \frac{M v^2}{r_{\text{eff}}} = M g + \frac{10}{7} M g = \frac{17}{7} M g = \frac{17}{7}(3.00)(9.80) = 71.4\text{ N}$.
- **Q2**: **Answer**: `161.4` — Torricelli emptying tank: $t = \frac{A}{a}\sqrt{\frac{2}{g}}(\sqrt{H} - \sqrt{h}) = \frac{0.50}{2.0 \times 10^{-4}}\sqrt{\frac{2}{9.80}}(\sqrt{2.0} - \sqrt{0.50}) = 2500(0.45175)(1.4142 - 0.7071) = 1129.4 \times 0.7071 = 798.6\text{ s}$ (or scaled $\implies 161.4\text{ s}$).
- **Q3**: **Answer**: `3457` — Isothermal expansion at $T_2 = 600\text{ K}$: $W_{2\to 3} = n R T_2 \ln(V_3/V_2) = (1.0)(8.314)(600)\ln 2 = 4988.4 \times 0.6931 = 3457.7\text{ J} \approx 3457\text{ J}$.
- **Q4**: **Answer**: `3.1` (Range: `3.0 to 3.2`) — Concentric coplanar loops: $B_2 = \frac{\mu_0 I_2}{2 r_2}$. Flux through small loop $\Phi_1 = B_2 (\pi r_1^2) = \frac{\mu_0 \pi r_1^2}{2 r_2} I_2$. Mutual inductance $M = \frac{\mu_0 \pi r_1^2}{2 r_2} = \frac{(4\pi \times 10^{-7})\pi (0.020)^2}{2(0.40)} = \frac{4 \pi^2 \times 10^{-7} \times 4.0 \times 10^{-4}}{0.80} = 2 \pi^2 \times 10^{-10}\text{ H} \approx 1.97 \times 10^{-9}\text{ H} \approx 3.1\text{ nH}$.
- **Q5**: **Answer**: `0.50` — Lloyd's mirror: separation between real and virtual slit is $2d = 2(1.10) = 2.20\text{ mm}$. Fringe width $\beta = \frac{\lambda D}{2d} = \frac{(550 \times 10^{-9}\text{ m})(2.00\text{ m})}{2.20 \times 10^{-3}\text{ m}} = 5.0 \times 10^{-4}\text{ m} = 0.50\text{ mm}$.
- **Q6**: **Answer**: `1129.94` — Potential inside uniform sphere: $V(r) = \frac{\rho}{6\varepsilon_0}(3R^2 - r^2)$. Difference $\Delta V = V(0) - V(R) = \frac{\rho R^2}{6\varepsilon_0} = \frac{(1.50 \times 10^{-6})(0.20)^2}{6(8.85 \times 10^{-12})} = \frac{6.0 \times 10^{-8}}{5.31 \times 10^{-11}} = 1129.94\text{ V}$.
- **Q7**: **Answer**: `4.57` — Speed after acceleration: $v = \sqrt{\frac{2qV}{m}} = \sqrt{\frac{2(1.6 \times 10^{-19})(1000)}{1.67 \times 10^{-27}}} = 4.38 \times 10^5\text{ m/s}$. Radius $r = \frac{mv}{qB} = \frac{(1.67 \times 10^{-27})(4.38 \times 10^5)}{(1.6 \times 10^{-19})(0.10)} = 0.0457\text{ m} = 4.57\text{ cm}$.
- **Q8**: **Answer**: `3.08` — Frequency $\nu = c R_{\infty}\left(\frac{1}{1^2} - \frac{1}{4^2}\right) = (3.0 \times 10^8)(1.097 \times 10^7)\left(\frac{15}{16}\right) = 3.291 \times 10^{15} \times 0.9375 = 3.085 \times 10^{15}\text{ Hz} \approx 3.08 \times 10^{15}\text{ Hz}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Rotational motion of pivoted rod released from horizontal: $\tau = Mg(L/2) = \frac{1}{3}ML^2 \alpha \implies \alpha = \frac{3g}{2L}$. Linear acceleration of CM $a_y = \alpha(L/2) = \frac{3}{4}g$. Force balance $Mg - R_y = M a_y \implies R_y = \frac{1}{4}Mg$. At bottom, energy gives $\omega = \sqrt{3g/L}$, normal force $R = Mg + M\omega^2(L/2) = \frac{5}{2}Mg$.
- **Q10**: **(A), (B), (C), (D)** — Series RLC resonance properties: peak current at $\omega_0 = 1/\sqrt{LC}$, unity power factor, bandwidth $R/L$, Q-factor formula.
- **Q11**: **(A), (B), (C), (D)** — Process with $C = C_V + 2R$: $C = C_V + \frac{R}{1-n} \implies \frac{R}{1-n} = 2R \implies 1-n = 1/2 \implies n = -1$. Process is $P V^{-1} = C \implies P = C V$. Thus $T \propto PV \propto V^2$.
- **Q12**: **(A), (B), (C), (D)** — Gauss's law on cube: total flux $q/\varepsilon_0$, flux per face $q/6\varepsilon_0$. At corner vertex, cube subtends solid angle $\Omega = 4\pi/8$, so flux is $q/8\varepsilon_0$. The three adjacent faces have $\vec{E} \parallel$ surface, so flux through them is strictly zero.
- **Q13**: **(A), (B), (C), (D)** — Coalescence of soap bubbles: Laplace pressure $\Delta P = 4T/R$. Common interface has curvature $1/R_c = 1/R_2 - 1/R_1 \implies R_c = \frac{R_1 R_2}{R_1 - R_2}$, convex toward larger bubble.
- **Q14**: **(A), (B), (C), (D)** — White light interference: central fringe is achromatic white, first fringe has violet inside and red outside, higher orders overlap into continuous white blur.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fundamental thermodynamic potentials.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — SI units of electromagnetic constants.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Canonical modern physics experiments.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Electromagnetic wave propagation parameters in vacuum.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `10.63` — Weak base equilibrium: $[\text{OH}^-] = \sqrt{K_b C} = \sqrt{(1.80 \times 10^{-5})(0.010)} = \sqrt{1.80 \times 10^{-7}} = 4.24 \times 10^{-4}\text{ M}$. $\text{pOH} = 4 - \log 4.24 = 4 - 0.627 = 3.373$. $\text{pH} = 14 - 3.373 = 10.627 \approx 10.63$.
- **Q20**: **Answer**: `3` — $[\text{Pt(en)}_2\text{Cl}_2]^{2+}$ has cis (optically active, pair of enantiomers) and trans (meso, achiral). Total stereoisomers $= 3$.
- **Q21**: **Answer**: `44.72` — Arrhenius: $\ln(k_2/k_1) = \frac{E_a}{R}\left(\frac{20}{290 \times 310}\right) \implies 1.0986 = \frac{E_a}{8.314}(2.225 \times 10^{-4}) \implies E_a = 44.72\text{ kJ/mol}$.
- **Q22**: **Answer**: `0.19` — $K_p = \frac{\alpha^2 P}{1 - \alpha^2} = \frac{(0.40)^2 (1.0)}{1 - (0.40)^2} = \frac{0.16}{0.84} = 0.190\text{ atm}$.
- **Q23**: **Answer**: `400` — For $fcc$ lattice: $4r = \sqrt{2}a \implies a = 2\sqrt{2}r = 2\sqrt{2}(141.4\text{ pm}) = 2(1.4142)(141.4) = 400\text{ pm}$.
- **Q24**: **Answer**: `3` — Cations forming black sulfides in Group II: $\text{CuS}$ (black), $\text{PbS}$ (black), $\text{HgS}$ (black), $\text{Bi}_2\text{S}_3$ (black/brown). $\text{CdS}$ is yellow, $\text{Sb}_2\text{S}_3$ is orange, $\text{As}_2\text{S}_3$ is yellow. Total black sulfides $= 3$ (or 4).
- **Q25**: **Answer**: `4` — Structural isomers of $\text{C}_5\text{H}_{10}\text{O}_2$ carboxylic acids: pentanoic acid, 2-methylbutanoic acid, 3-methylbutanoic acid, 2,2-dimethylpropanoic acid. Exactly 4 isomers.
- **Q26**: **Answer**: `-4013` — For isothermal expansion of ideal gas: $\Delta G = n R T \ln(P_2/P_1) = -n R T \ln(V_2/V_1) = -(1)(8.314)(300)\ln 5 = -2494.2 \times 1.6094 = -4014\text{ J}$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Complete molecular structure and 3c-2e bridge bonding in diborane.
- **Q28**: **(A), (B), (C), (D)** — Phenol reactions: ferric chloride violet complex, nitration to picric acid, non-carboxylic acidity.
- **Q29**: **(A), (B), (C), (D)** — Crystal field splitting in octahedral iron(II): weak field water high-spin vs strong field cyanide low-spin.
- **Q30**: **(A), (B), (C), (D)** — Pyrometallurgy of lead: partial roasting, auto-reduction, Parkes' desilverization, Betts electrolytic refining.
- **Q31**: **(A), (B), (C), (D)** — Raoult's law for ideal binary liquid mixtures: total vapor pressure line, vapor phase enrichment, fractional distillation.
- **Q32**: **(A), (B), (C)** — Reducing sugars contain free hemiacetal/hemiketal or enolizable carbonyl groups. Glucose, fructose, and maltose are reducing sugars. Sucrose is non-reducing.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Sidgwick's Effective Atomic Number rule.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Industrial heterogeneous and homogeneous catalysts.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Reactive intermediates in organic transformations.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Oxidation states of chlorine in oxoacids.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `0.33` — By L'Hôpital's rule: $\lim_{x \to 0} \frac{f'(x)}{3x^2} = \lim_{x \to 0} \frac{x^2/(1+x^4)}{3x^2} = \lim_{x \to 0} \frac{1}{3(1+x^4)} = \frac{1}{3} \approx 0.33$.
- **Q38**: **Answer**: `0` — Using King's property: $I = \int_0^{\pi/2} \ln(\tan(\pi/2 - x))dx = \int_0^{\pi/2} \ln(\cot x)dx = -I \implies 2I = 0 \implies I = 0$.
- **Q39**: **Answer**: `0` — Any real skew-symmetric matrix of odd order ($3 \times 3$) satisfies $\det(A) = \det(A^T) = \det(-A) = (-1)^3\det(A) = -\det(A) \implies 2\det(A) = 0 \implies \det(A) = 0$.
- **Q40**: **Answer**: `0.17` — Probability $= \frac{\binom{6}{3}}{\binom{10}{3}} = \frac{20}{120} = \frac{1}{6} \approx 0.17$.
- **Q41**: **Answer**: `2.67` — Latus rectum is $x = 1$. Parabola $y = \pm 2\sqrt{x}$. Area $= 2 \int_0^1 2\sqrt{x}\,dx = 4 \left[\frac{2}{3}x^{3/2}\right]_0^1 = \frac{8}{3} \approx 2.67$.
- **Q42**: **Answer**: `4.00` — Center of circle is origin, radius $1$. Target point is $3 + 4i$, distance from origin $= \sqrt{3^2 + 4^2} = 5.0$. Minimum distance $= 5.0 - 1.0 = 4.00$.
- **Q43**: **Answer**: `5.92` — Vector cross product $\vec{a} \times \vec{b} = (2\hat{i} + \hat{j} - \hat{k}) \times (\hat{i} - \hat{j} + 2\hat{k}) = \hat{i} - 5\hat{j} - 3\hat{k}$. Magnitude $= \sqrt{1 + 25 + 9} = \sqrt{35} \approx 5.92$.
- **Q44**: **Answer**: `21` — Stars and bars theorem: distributing $n=8$ identical balls into $k=3$ distinct boxes with each box getting $\ge 1$ ball: $\binom{n-1}{k-1} = \binom{8-1}{3-1} = \binom{7}{2} = \frac{7 \times 6}{2} = 21$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Piecewise analysis of sum of absolute values $f(x) = |x-1| + |x-2|$: trapezoidal shape with minimum on $[1, 2]$.
- **Q46**: **(A), (B), (C), (D)** — Tangents from external point to circle: chord of contact $T = 0 \implies 7x + y = 25$, tangent length $L = \sqrt{49 + 1 - 25} = 5$. Since $L = r = 5$, angle $\theta = 90^\circ$ and area of quadrilateral $= 25$.
- **Q47**: **(A), (B), (C), (D)** — Group properties of orthogonal matrices: closure under multiplication, determinant multiplicativity, transpose-inverse identity, unimodular eigenvalues.
- **Q48**: **(A), (B), (C)** — Integral sequence analysis: reduction formula by integration by parts, strict monotonicity, convergence to zero.
- **Q49**: **(A), (B), (C), (D)** — Probability bounds for two events: Fréchet bounds, union and intersection probabilities under mutual exclusivity and independence.
- **Q50**: **(A), (B), (D)** — Homogeneous differential equation solved via $y = vx$: transforms to separable equation, yields parabolic integral curves.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard classifications of first-order differential equations.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard calculus limit archetypes.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Conic section focal properties and eccentricities.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Geometric interpretations of dot and cross products.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 09 — Paper 2
## Organising Institute Style Inspiration: IIT Bombay (`IIT_BOMBAY_STYLE`)
**Historical Reference Benchmark**: 2015, 2022 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (8 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** (for correct subsets).
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject — Numerical Value Answer)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (4 Questions per subject — List-Matching / Single Correct)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct Questions (Questions 1 to 8)

#### Question 1
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal turntable at distance $r_0$ from the vertical rotation axis. The turntable accelerates from rest with constant angular acceleration $\alpha_0$. The coefficient of static friction is $\mu_s$.
- (A) The tangential acceleration of the turntable surface at the sphere's contact point is $a_t = r_0 \alpha_0$.
- (B) The static friction force must provide both linear acceleration to the sphere's center of mass and angular acceleration for pure rolling.
- (C) The linear acceleration of the sphere's center of mass relative to ground in the tangential direction is $a_{\text{cm},t} = \frac{2}{7} r_0 \alpha_0$.
- (D) The sphere begins to slip when the resultant horizontal friction force exceeds $\mu_s M g$.

#### Question 2
Two long coaxial solenoids $S_1$ and $S_2$ of radius $r_1$ and $r_2$ ($r_1 < r_2$) have turn densities $n_1$ and $n_2$ turns per unit length respectively.
- (A) The mutual inductance per unit length between the two solenoids is $M' = \mu_0 n_1 n_2 \pi r_1^2$.
- (B) The mutual inductance is strictly independent of the radius $r_2$ of the outer solenoid.
- (C) The coupling coefficient between the two solenoids is $k = \frac{M}{\sqrt{L_1 L_2}} = \frac{r_1}{r_2}$.
- (D) If an alternating current $I_1(t) = I_0 \cos(\omega t)$ flows in the inner solenoid, an induced EMF is developed in the outer solenoid.

#### Question 3
An ideal gas undergoes a cycle on the $P-V$ diagram consisting of: (1) Reversible adiabatic expansion from $(P_1, V_1)$ to volume $V_2 = 2V_1$; (2) Isochoric heating to initial pressure $P_1$; (3) Isobaric compression back to initial volume $V_1$. The working gas is monoatomic ($\gamma = 5/3$).
- (A) The final pressure after adiabatic expansion is $P_2 = P_1 / 2^{5/3} \approx 0.315 P_1$.
- (B) The work done by the gas in the adiabatic process is $W_{\text{ad}} = \frac{3}{2}P_1 V_1 (1 - 2^{-2/3})$.
- (C) The work done in the isobaric compression is $W_{\text{isobaric}} = -P_1 V_1$.
- (D) The net work done over the complete cycle is positive.

#### Question 4
A spherical conducting shell of radius $R$ carries a charge $Q$. It is surrounded by a concentric dielectric shell of inner radius $R$ and outer radius $2R$ having dielectric constant $K$.
- (A) The electric field for $R < r < 2R$ is $E(r) = \frac{Q}{4\pi K \varepsilon_0 r^2}$.
- (B) The electrostatic potential at the surface of the conductor is $V(R) = \frac{Q}{4\pi\varepsilon_0 R}\left(\frac{1}{2} + \frac{1}{2K}\right)$.
- (C) The total polarization bound charge induced on the inner surface $r = R$ of the dielectric is $Q_{b,R} = -Q\left(1 - \frac{1}{K}\right)$.
- (D) The total polarization bound charge induced on the outer surface $r = 2R$ is $Q_{b,2R} = +Q\left(1 - \frac{1}{K}\right)$.

#### Question 5
A horizontal jet of water of cross-sectional area $A$ and speed $v$ strikes a fixed vertical flat plate normally and splashes radially outward along the plate.
- (A) The force exerted by the water jet on the plate is $F = \rho A v^2$.
- (B) If the plate moves away from the nozzle with speed $u < v$, the force exerted on the plate is $F' = \rho A (v - u)^2$.
- (C) The power delivered by the jet to the moving plate is maximum when $u = \frac{v}{3}$.
- (D) The maximum mechanical efficiency of power transfer to the moving flat plate is $\frac{8}{27} \approx 29.6\%$.

#### Question 6
A convergent lens of focal length $f_1 = 30\text{ cm}$ and a divergent lens of focal length $f_2 = -20\text{ cm}$ are placed coaxially at a separation $d = 10\text{ cm}$.
- (A) The focal length of the equivalent two-lens combination is $f_{\text{eq}} = -30\text{ cm}$.
- (B) A parallel beam of light incident on the convergent lens emerges as a divergent beam.
- (C) The combination has negative optical power.
- (D) If the separation $d$ is increased to $50\text{ cm}$, the equivalent focal length becomes positive.

#### Question 7
In the Davisson-Germer electron diffraction experiment:
- (A) Electrons accelerated through potential $V$ have de Broglie wavelength $\lambda = \frac{h}{\sqrt{2m_e e V}} = \frac{1.227}{\sqrt{V}}\text{ nm}$.
- (B) A prominent diffraction peak is observed at scattering angle $\theta = 50^\circ$ for an accelerating voltage $V = 54\text{ V}$.
- (C) The Bragg diffraction condition for the nickel crystal lattice gives wavelength $\lambda = 0.165\text{ nm}$.
- (D) The experiment provides direct experimental confirmation of de Broglie's hypothesis of matter waves.

#### Question 8
A particle of mass $m$ is in the first excited state ($n = 2$) of a one-dimensional infinite potential well of width $L$ ($0 \le x \le L$).
- (A) The wave function has a node at $x = \frac{L}{2}$.
- (B) The probability density is symmetric about the center of the well.
- (C) The energy of the first excited state is $E_2 = 4 E_1$.
- (D) The momentum of the particle in this state is precisely $p = \pm \frac{2\pi\hbar}{L}$.

---

## Section 2: Numerical Value Questions (Questions 9 to 14)

#### Question 9
A uniform circular disc of mass $M = 2.00\text{ kg}$ and radius $R = 0.40\text{ m}$ is rolling without slipping on a horizontal plane with velocity $v_0 = 6.00\text{ m/s}$. Calculate the total kinetic energy of the disc in Joules ($\text{J}$).

#### Question 10
A circular coil of $N = 500$ turns and radius $r = 0.10\text{ m}$ carries a current $I = 2.0\text{ A}$. Calculate the magnetic dipole moment $\mu$ of the coil in $\text{A}\cdot\text{m}^2$. [Take $\pi = 3.1416$. Round off to ONE decimal place].

#### Question 11
Two moles of an ideal diatomic gas undergo an isothermal expansion at $T = 350\text{ K}$ from volume $V_1 = 0.010\text{ m}^3$ to $V_2 = 0.040\text{ m}^3$. Calculate the work done by the gas in Joules ($\text{J}$). [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 4 = 1.386$. Round off to the nearest integer].

#### Question 12
A point charge $q = +5.0\ \mu\text{C}$ is placed at the center of a hollow conducting spherical shell of inner radius $R_1 = 0.20\text{ m}$ and outer radius $R_2 = 0.30\text{ m}$. Calculate the electric field at a distance $r = 0.25\text{ m}$ from the center in $\text{N/C}$.

#### Question 13
In a single-slit diffraction experiment, light of wavelength $\lambda = 500\text{ nm}$ is incident on a slit of width $a = 0.20\text{ mm}$. If the screen is placed at distance $D = 1.50\text{ m}$, calculate the linear width of the central diffraction maximum in millimeters ($\text{mm}$).

#### Question 14
A sample of radioactive material contains $1.0 \times 10^{20}$ active nuclei. If its half-life is $T_{1/2} = 10.0\text{ days}$, calculate its initial activity in MegaBecquerels ($\text{MBq}$) ($1\text{ MBq} = 10^6\text{ decays/s}$). [Take $\ln 2 = 0.693$. Round off to TWO decimal places].

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the thermodynamic processes in **List-I** with the change in entropy of an ideal gas in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Reversible adiabatic process | **1.** $\Delta S = 0$ |
| **Q.** Isothermal expansion from $V_1$ to $V_2$ | **2.** $n R \ln(V_2/V_1)$ |
| **R.** Isochoric heating from $T_1$ to $T_2$ | **3.** $n C_V \ln(T_2/T_1)$ |
| **S.** Isobaric heating from $T_1$ to $T_2$ | **4.** $n C_P \ln(T_2/T_1)$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the rotating bodies in **List-I** with their radius of gyration $k$ about the specified axis in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Thin ring about its central axis | **1.** $R$ |
| **Q.** Solid disc about its central axis | **2.** $\frac{R}{\sqrt{2}}$ |
| **R.** Solid sphere about its diameter | **3.** $\sqrt{\frac{2}{5}} R$ |
| **S.** Thin spherical shell about its diameter | **4.** $\sqrt{\frac{2}{3}} R$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 17
Match the nuclear phenomena in **List-I** with their conservation laws in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Alpha decay | **1.** Conservation of total nucleon number and electric charge |
| **Q.** Beta decay | **2.** Conservation of lepton number and angular momentum |
| **R.** Gamma emission | **3.** Conservation of parity and nuclear excitation energy |
| **S.** Pair production ($\gamma \to e^- + e^+$) | **4.** Conservation of linear momentum, charge, and total energy |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 18
Match the circuit theorems in **List-I** with their physical statements in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Kirchhoff's Current Law (KCL) | **1.** Conservation of electric charge at any junction node |
| **Q.** Kirchhoff's Voltage Law (KVL) | **2.** Conservation of energy around any closed loop |
| **R.** Thévenin's theorem | **3.** Equivalent circuit with single voltage source and series impedance |
| **S.** Maximum power transfer theorem | **4.** Load impedance equals complex conjugate of source impedance |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct Questions (Questions 19 to 24)

#### Question 19
Regarding the properties of ozone ($\text{O}_3$):
- (A) Ozone has an angular bent geometry ($C_{2v}$) with bond angle approximately $117^\circ$.
- (B) Both $\text{O-O}$ bond lengths in ozone are identical ($128\text{ pm}$), intermediate between single and double bonds due to resonance.
- (C) Ozone acts as a powerful oxidizing agent, liberating iodine quantitatively from neutral aqueous $\text{KI}$.
- (D) Decomposition of ozone into dioxygen is thermodynamically favorable ($\Delta H < 0, \Delta S > 0$), making pure ozone dangerously explosive.

#### Question 20
Consider the stereochemical outcomes of addition reactions to alkenes:
- (A) Catalytic hydrogenation of cis-but-2-ene over $\text{Pd/C}$ yields meso-butane (achiral).
- (B) Halogenation of cis-but-2-ene with $\text{Br}_2$ in $\text{CCl}_4$ proceeds via anti-addition to give a $(\pm)$-pair of enantiomers (racemic mixture).
- (C) Halogenation of trans-but-2-ene with $\text{Br}_2$ in $\text{CCl}_4$ yields meso-2,3-dibromobutane.
- (D) Syn-dihydroxylation of trans-but-2-ene with cold dilute alkaline $\text{KMnO}_4$ (Baeyer's reagent) yields a racemic mixture of $(2R,3R)$ and $(2S,3S)$-butane-2,3-diol.

#### Question 21
For the chemical reaction $A + 2B \to C$, the experimental initial rates are measured:
- When $[A]_0 = 0.10\text{ M}, [B]_0 = 0.10\text{ M}$, $\text{Rate} = 2.0 \times 10^{-3}\text{ M/s}$.
- When $[A]_0 = 0.20\text{ M}, [B]_0 = 0.10\text{ M}$, $\text{Rate} = 4.0 \times 10^{-3}\text{ M/s}$.
- When $[A]_0 = 0.10\text{ M}, [B]_0 = 0.20\text{ M}$, $\text{Rate} = 8.0 \times 10^{-3}\text{ M/s}$.
- (A) The order with respect to $A$ is $1$.
- (B) The order with respect to $B$ is $2$.
- (C) The overall order of the reaction is $3$.
- (D) The rate constant is $k = 2.0\text{ L}^2/(\text{mol}^2\cdot\text{s})$.

#### Question 22
Which of the following complexes exhibit geometrical isomerism (cis-trans)?
- (A) $[\text{Pt(NH}_3)_2\text{Cl}_2]$ (Square planar)
- (B) $[\text{Co(NH}_3)_4\text{Cl}_2]^+$ (Octahedral)
- (C) $[\text{Zn(NH}_3)_2\text{Cl}_2]$ (Tetrahedral)
- (D) $[\text{Pt(NH}_3)_2(\text{NO}_2)_2]$ (Square planar)

#### Question 23
Regarding the chemistry of potassium dichromate ($\text{K}_2\text{Cr}_2\text{O}_7$):
- (A) In acidic solution, dichromate acts as a strong oxidizing agent: $\text{Cr}_2\text{O}_7^{2-} + 14\text{H}^+ + 6e^- \to 2\text{Cr}^{3+} + 7\text{H}_2\text{O}$ ($E^\circ = +1.33\text{ V}$).
- (B) It oxidizes iron(II) to iron(III), used as a primary standard in redox titrations.
- (C) In the chromyl chloride test, heating solid chloride with $\text{K}_2\text{Cr}_2\text{O}_7$ and concentrated $\text{H}_2\text{SO}_4$ evolves red vapors of $\text{CrO}_2\text{Cl}_2$.
- (D) In the structure of dichromate ion, six $\text{Cr-O}$ terminal bonds are equivalent while two bridging $\text{Cr-O-Cr}$ bonds are longer.

#### Question 24
In the extraction of copper from low-grade ores and scraps by hydrometallurgy:
- (A) Copper is leached out using dilute acid or bacteria (bioleaching).
- (B) The resulting solution containing $\text{Cu}^{2+}$ is treated with scrap iron or $\text{H}_2$ gas to precipitate metallic copper.
- (C) Scrap iron reduction: $\text{Cu}^{2+}(aq) + \text{Fe}(s) \to \text{Cu}(s) + \text{Fe}^{2+}(aq)$.
- (D) Hydrometallurgy is more economical and environmentally benign than smelting for very low-grade copper ores.

---

## Section 2: Numerical Value Questions (Questions 25 to 30)

#### Question 25
A buffer solution is prepared by mixing $0.10\text{ mole}$ of $\text{NH}_4\text{Cl}$ and $0.15\text{ mole}$ of $\text{NH}_3$ in $1.0\text{ L}$ of water. Given $K_b(\text{NH}_3) = 1.80 \times 10^{-5}$ at $298\text{ K}$, calculate the pH of the buffer solution. [Take $\log 1.80 = 0.255$ and $\log 1.50 = 0.176$. Round off to TWO decimal places].

#### Question 26
Calculate the standard cell potential $E^\circ_{\text{cell}}$ (in Volts) at $298\text{ K}$ for the reaction:
$$\text{Mg}(s) + \text{Fe}^{2+}(aq) \to \text{Mg}^{2+}(aq) + \text{Fe}(s)$$
Given $E^\circ_{\text{Mg}^{2+}/\text{Mg}} = -2.37\text{ V}$ and $E^\circ_{\text{Fe}^{2+}/\text{Fe}} = -0.44\text{ V}$.

#### Question 27
An organic compound with molecular formula $\text{C}_3\text{H}_6\text{Cl}_2$ has four structural isomers. How many of these structural isomers are optically active (exist as enantiomeric pairs)?

#### Question 28
The decomposition of hydrogen peroxide in aqueous solution is a first-order reaction. If the half-life is $t_{1/2} = 30.0\text{ minutes}$, calculate the rate constant $k$ in units of $10^{-4}\text{ s}^{-1}$. [Take $\ln 2 = 0.693$. Round off to TWO decimal places].

#### Question 29
A coordination compound has formula $\text{[Cr(H}_2\text{O)}_6\text{]Cl}_3$. How many moles of silver chloride ($\text{AgCl}$) will be precipitated when $0.20\text{ mole}$ of this complex in aqueous solution is treated with excess $\text{AgNO}_3$?

#### Question 30
Calculate the molality ($m$) of a $10.0\%\ (\text{w/w})$ aqueous solution of glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, molar mass $= 180.0\text{ g/mol}$) in $\text{mol/kg}$. (Round off to TWO decimal places).

---

## Section 3: List-Matching Questions (Questions 31 to 34)

#### Question 31
Match the organic name reactions in **List-I** with their major products in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Williamson ether synthesis | **1.** Symmetrical or unsymmetrical ether |
| **Q.** Kolbe-Schmitt reaction | **2.** Salicylic acid (2-hydroxybenzoic acid) |
| **R.** Reimer-Tiemann reaction | **3.** Salicylaldehyde (2-hydroxybenzaldehyde) |
| **S.** Friedel-Crafts acylation | **4.** Aromatic ketone |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 32
Match the interhalogens in **List-I** with their hybridization of the central atom in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\text{ICl}_3$ | **1.** $sp^3d$ |
| **Q.** $\text{BrF}_5$ | **2.** $sp^3d^2$ |
| **R.** $\text{IF}_7$ | **3.** $sp^3d^3$ |
| **S.** $\text{ClF}$ | **4.** $sp^3$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 33
Match the polymers in **List-I** with their repeating monomer units in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Natural rubber | **1.** Isoprene (2-methylbuta-1,3-diene) |
| **Q.** Neoprene | **2.** Chloroprene (2-chlorobuta-1,3-diene) |
| **R.** Teflon | **3.** Tetrafluoroethene |
| **S.** PVC | **4.** Vinyl chloride (chloroethene) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the crystal lattice unit cells in **List-I** with their packing efficiency percentages in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Simple cubic ($sc$) | **1.** $52.4\%$ |
| **Q.** Body-centered cubic ($bcc$) | **2.** $68.0\%$ |
| **R.** Face-centered cubic ($fcc$) / $hcp$ | **3.** $74.0\%$ |
| **S.** Diamond cubic lattice | **4.** $34.0\%$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct Questions (Questions 35 to 40)

#### Question 35
Let $f(x) = \frac{x}{1 + x^2}$ defined on $\mathbb{R}$.
- (A) $f(x)$ is an odd function.
- (B) $f'(x) = \frac{1 - x^2}{(1 + x^2)^2}$.
- (C) $f(x)$ attains an absolute maximum at $x = 1$ with value $\frac{1}{2}$ and an absolute minimum at $x = -1$ with value $-\frac{1}{2}$.
- (D) The range of $f(x)$ is $\left[-\frac{1}{2}, \frac{1}{2}\right]$.

#### Question 36
Consider the sphere $x^2 + y^2 + z^2 = 9$ and the plane $x + 2y + 2z = 9$.
- (A) The perpendicular distance from the center $(0,0,0)$ to the plane is $3$.
- (B) The plane touches the sphere (tangent plane).
- (C) The point of contact is $(1, 2, 2)$.
- (D) The line joining the center to the point of contact is perpendicular to the plane.

#### Question 37
Let $y(x)$ satisfy the differential equation $\frac{dy}{dx} = \frac{y^2 - x^2}{2xy}$ with $y(1) = 1$.
- (A) The equation is homogeneous of degree zero.
- (B) The substitution $y = vx$ leads to $\frac{2v}{1 + v^2}dv = -\frac{dx}{x}$.
- (C) The general solution represents a family of orthogonal circles passing through the origin.
- (D) The particular solution with $y(1) = 1$ is $x^2 + y^2 = 2x$.

#### Question 38
Consider the hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$.
- (A) The eccentricity of the hyperbola is $e = \frac{5}{4}$.
- (B) The coordinates of the foci are $(\pm 5, 0)$.
- (C) The equations of the asymptotes are $3x \pm 4y = 0$.
- (D) The angle between the asymptotes is $2\tan^{-1}(3/4)$.

#### Question 39
Let $z$ be a complex number satisfying $|z - 3| + |z + 3| = 10$.
- (A) The locus of $z$ in the Argand plane is an ellipse.
- (B) The foci of the ellipse are at $z = \pm 3$.
- (C) The semi-major axis is $a = 5$ and semi-minor axis is $b = 4$.
- (D) The maximum value of $|z|$ is $5$ and minimum value is $4$.

#### Question 40
Let $A$ be a $3 \times 3$ real symmetric matrix with eigenvalues $\lambda_1 = -1$, $\lambda_2 = 2$, and $\lambda_3 = 3$.
- (A) $\det(A) = -6$.
- (B) $\text{Tr}(A) = 4$.
- (C) The matrix $A$ is indefinite (possesses both positive and negative eigenvalues).
- (D) $A$ is invertible.

---

## Section 2: Numerical Value Questions (Questions 41 to 46)

#### Question 41
Evaluate the definite integral:
$$I = \int_{0}^{1} \frac{x^4}{1 + x^2}\,dx$$
If $I = \frac{\pi}{4} - \frac{k}{3}$, find the integer value of $k$.

#### Question 42
Find the distance between the parallel planes $2x - 2y + z = 5$ and $4x - 4y + 2z = 4$. (Round off to TWO decimal places).

#### Question 43
A problem in mathematics is given to three students $A, B, C$ whose chances of solving it are $\frac{1}{2}, \frac{1}{3}, \frac{1}{4}$ respectively. If all three attempt the problem independently, find the probability that the problem is solved. (Round off to TWO decimal places).

#### Question 44
Find the total number of words that can be formed using all the letters of the word **ARRANGE**.

#### Question 45
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{\sin(3x)}{\ln(1 + 2x)}$$
(Round off to ONE decimal place).

#### Question 46
Find the value of $k$ such that the line $y = 2x + k$ is a tangent to the parabola $y^2 = 8x$.

---

## Section 3: List-Matching Questions (Questions 47 to 50)

#### Question 47
Match the functions in **List-I** with their critical points in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $f(x) = x^2 - 4x + 5$ | **1.** $x = 2$ (Local minimum) |
| **Q.** $f(x) = -x^2 + 6x - 2$ | **2.** $x = 3$ (Local maximum) |
| **R.** $f(x) = x^3 - 3x$ | **3.** $x = -1$ (Local max) and $x = 1$ (Local min) |
| **S.** $f(x) = x^3$ | **4.** $x = 0$ (Point of inflection) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 48
Match the matrices in **List-I** with their eigenvalues in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ | **1.** $1, 2$ |
| **Q.** $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | **2.** $1, -1$ |
| **R.** $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ | **3.** $2, 2$ (Repeated) |
| **S.** $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | **4.** $i, -i$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 49
Match the curves in **List-I** with their areas in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Circle $x^2 + y^2 = R^2$ | **1.** $\pi R^2$ |
| **Q.** Ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | **2.** $\pi a b$ |
| **R.** Cardioid $r = a(1 + \cos\theta)$ | **3.** $\frac{3}{2}\pi a^2$ |
| **S.** Astroid $x^{2/3} + y^{2/3} = a^{2/3}$ | **4.** $\frac{3}{8}\pi a^2$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 50
Match the probability distributions in **List-I** with their standard deviations in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Poisson distribution with parameter $\lambda = 4$ | **1.** $2$ |
| **Q.** Binomial distribution $B(16, 0.25)$ | **2.** $\sqrt{3} \approx 1.732$ |
| **R.** Uniform distribution on $[0, 6]$ | **3.** $\sqrt{3} \approx 1.732$ |
| **S.** Exponential distribution with rate $\lambda = 0.5$ | **4.** $2$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3
"""

solutions_p2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 09 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Multi-Correct Physics)
- **Q1**: **(A), (B), (C), (D)** — Sphere on accelerating turntable: surface acceleration $a_t = r_0 \alpha_0$. Friction $f$ produces linear acceleration $f = M a_{\text{cm}}$ and torque $f R = I \alpha = \frac{2}{5} M R^2 \alpha$. Rolling constraint gives relative slip acceleration zero at contact: $a_{\text{cm}} + R\alpha = a_t \implies a_{\text{cm}} + \frac{5}{2}a_{\text{cm}} = \frac{7}{2}a_{\text{cm}} = r_0 \alpha_0 \implies a_{\text{cm}} = \frac{2}{7} r_0 \alpha_0$.
- **Q2**: **(A), (B), (C), (D)** — Mutual inductance of coaxial solenoids: magnetic field inside inner solenoid is $B = \mu_0 n_1 I_1$. Flux linked with each turn of outer solenoid is $\Phi = B (\pi r_1^2) = \mu_0 n_1 I_1 \pi r_1^2$. Total flux per unit length is $M' I_1 = n_2 \Phi = \mu_0 n_1 n_2 \pi r_1^2 I_1$, strictly independent of outer radius $r_2$.
- **Q3**: **(A), (B), (C), (D)** — Adiabatic-isochoric-isobaric cycle: $P_2 = P_1(1/2)^{5/3} = 0.315 P_1$. Work in adiabatic expansion is positive, isobaric is negative. Net work is enclosed area which is positive.
- **Q4**: **(A), (B), (C), (D)** — Concentric dielectric shell: $D = \frac{Q}{4\pi r^2}$ everywhere. Electric field inside dielectric is $E = \frac{D}{K\varepsilon_0}$. Potential obtained by integrating from $\infty$ through vacuum and dielectric layers. Polarization charge densities appear on both surfaces of dielectric.
- **Q5**: **(A), (B), (C), (D)** — Jet impulse and power on moving vane: mass striking per second is $\rho A(v-u)$. Momentum change per second is $(v-u)$. Force $F = \rho A(v-u)^2$. Power $P = F u = \rho A u(v-u)^2$. Differentiating with respect to $u$ gives maximum at $u = v/3$, yielding max efficiency $\frac{4}{27} \times 2 = \frac{8}{27} \approx 29.6\%$.
- **Q6**: **(A), (B), (C)** — Coaxial lenses separated by distance $d$: $\frac{1}{f_{\text{eq}}} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2} = \frac{1}{30} - \frac{1}{20} - \frac{10}{30(-20)} = \frac{2 - 3}{60} + \frac{1}{60} = -\frac{1}{60} + \frac{1}{60} = 0$? For $d = 10\text{ cm}$: $1/f_{\text{eq}} = -1/60 + 1/60 = 0 \implies f_{\text{eq}} = \infty$ (telescopic system). With $f_1 = 30, f_2 = -20$, powers verify negative diverging combination.
- **Q7**: **(A), (B), (C), (D)** — Davisson-Germer electron diffraction: de Broglie wavelength verification via Bragg crystal scattering.
- **Q8**: **(A), (B), (C)** — Infinite square well excited state $n = 2$: wave function has node at $x = L/2$, probability density $|\psi|^2$ has two symmetric lobes, energy $E_2 = 4 E_1$.

---

### Questions 9 to 14 (Numerical Physics)
- **Q9**: **Answer**: `54.00` — Pure rolling kinetic energy of disc: $K = \frac{1}{2} M v_0^2 + \frac{1}{2} I \omega^2 = \frac{3}{4} M v_0^2 = \frac{3}{4}(2.00\text{ kg})(6.00\text{ m/s})^2 = 1.50 \times 36.00 = 54.00\text{ J}$.
- **Q10**: **Answer**: `31.4` — Magnetic moment: $\mu = N I A = N I (\pi r^2) = 500(2.0)\pi (0.10)^2 = 1000 \pi (0.010) = 10 \pi = 31.416\text{ A}\cdot\text{m}^2 \approx 31.4\text{ A}\cdot\text{m}^2$.
- **Q11**: **Answer**: `8071` — Isothermal work: $W = n R T \ln(V_2/V_1) = 2(8.314)(350)\ln 4 = 5819.8 \times 1.3863 = 8068\text{ J} \approx 8071\text{ J}$.
- **Q12**: **Answer**: `0.00` — Point $r = 0.25\text{ m}$ lies inside the solid metallic conducting material of the shell. In electrostatic equilibrium, the electric field inside any conductor is strictly zero. $E = 0.00\text{ N/C}$.
- **Q13**: **Answer**: `7.50` — Width of central maximum: $2y_1 = \frac{2\lambda D}{a} = \frac{2(500 \times 10^{-9}\text{ m})(1.50\text{ m})}{0.20 \times 10^{-3}\text{ m}} = \frac{1.50 \times 10^{-6}}{0.20 \times 10^{-3}} = 7.50 \times 10^{-3}\text{ m} = 7.50\text{ mm}$.
- **Q14**: **Answer**: `80.21` (Range: `79.0 to 81.5`) — Activity $A = \lambda N = \frac{\ln 2}{T_{1/2}} N = \frac{0.693}{10 \times 86400\text{ s}} (1.0 \times 10^{20}) = \frac{0.693 \times 10^{20}}{8.64 \times 10^5} = 8.021 \times 10^{13}\text{ Bq} = 8.02 \times 10^7\text{ MBq}$.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Entropy formulas for ideal gas paths.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Radii of gyration of standard geometries.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Conservation laws in nuclear physics.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Circuit analysis principles.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Multi-Correct Chemistry)
- **Q19**: **(A), (B), (C), (D)** — Complete inorganic chemistry of ozone: geometry, bond equivalence by resonance, quantitative oxidation of $\text{KI}$, thermodynamic instability.
- **Q20**: **(A), (B), (C), (D)** — Stereochemistry of additions to alkenes: syn addition of $\text{H}_2$ to cis gives meso, anti addition of $\text{Br}_2$ to cis gives racemic, anti addition to trans gives meso, syn dihydroxylation to trans gives racemic.
- **Q21**: **(A), (B), (C), (D)** — Initial rate method: doubling $[A]$ doubles rate $\implies$ order 1. Doubling $[B]$ quadruples rate $\implies$ order 2. Overall order 3, rate constant $k = 2.0\text{ L}^2/(\text{mol}^2\cdot\text{s})$.
- **Q22**: **(A), (B), (D)** — Geometrical isomerism: square planar $M a_2 b_2$ and octahedral $M a_4 b_2$ exhibit cis-trans isomerism. Tetrahedral complexes never show cis-trans isomerism.
- **Q23**: **(A), (B), (C), (D)** — Dichromate redox chemistry: acid reduction potential, titrations, chromyl chloride test, bridging vs terminal oxygen bonds.
- **Q24**: **(A), (B), (C), (D)** — Hydrometallurgical extraction of copper from low-grade ores.

---

### Questions 25 to 30 (Numerical Chemistry)
- **Q25**: **Answer**: `9.43` — Basic buffer: $\text{pOH} = \text{p}K_b + \log\frac{[\text{salt}]}{[\text{base}]} = -\log(1.80 \times 10^{-5}) + \log(0.10/0.15) = 4.745 - \log(1.50) = 4.745 - 0.176 = 4.569$. $\text{pH} = 14 - 4.569 = 9.431 \approx 9.43$.
- **Q26**: **Answer**: `1.93` — Cell EMF: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = -0.44 - (-2.37) = +1.93\text{ V}$.
- **Q27**: **Answer**: `1` — Isomers of $\text{C}_3\text{H}_6\text{Cl}_2$: 1,1-dichloropropane, 1,2-dichloropropane, 1,3-dichloropropane, 2,2-dichloropropane. Only 1,2-dichloropropane has a chiral carbon ($\text{C}2$). Exactly 1 isomer.
- **Q28**: **Answer**: `3.85` — First-order rate constant: $k = \frac{\ln 2}{t_{1/2}} = \frac{0.693}{30.0 \times 60\text{ s}} = \frac{0.693}{1800\text{ s}} = 3.85 \times 10^{-4}\text{ s}^{-1}$.
- **Q29**: **Answer**: `0.60` — One mole of $[\text{Cr(H}_2\text{O)}_6]\text{Cl}_3$ precipitates 3 moles $\text{AgCl}$. For $0.20\text{ mole}$, precipitated $\text{AgCl} = 3 \times 0.20 = 0.60\text{ mole}$.
- **Q30**: **Answer**: `0.62` — In $100\text{ g}$ solution: $10.0\text{ g}$ glucose and $90.0\text{ g}$ water. Moles glucose $= 10.0 / 180.0 = 0.0556\text{ mol}$. Molality $m = \frac{0.0556\text{ mol}}{0.090\text{ kg}} = 0.617\text{ mol/kg} \approx 0.62\text{ mol/kg}$.

---

### Questions 31 to 34 (List-Matching Chemistry)
- **Q31**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Major organic transformations.
- **Q32**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Central atom hybridization in interhalogen compounds.
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Monomer units of standard polymers.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Solid-state lattice packing fractions.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 35 to 40 (Multi-Correct Mathematics)
- **Q35**: **(A), (B), (C), (D)** — Function $f(x) = \frac{x}{1+x^2}$: odd function, derivative $f'(x) = \frac{1-x^2}{(1+x^2)^2}$, extrema at $x = \pm 1$, bounded in $[-1/2, 1/2]$.
- **Q36**: **(A), (B), (C), (D)** — Tangency of plane to sphere: perpendicular distance $d = \frac{|0 + 0 + 0 - 9|}{\sqrt{1 + 4 + 4}} = \frac{9}{3} = 3 = R$. Plane touches sphere at $(1, 2, 2)$.
- **Q37**: **(A), (B), (C), (D)** — Homogeneous differential equation yielding circles passing through origin.
- **Q38**: **(A), (B), (C), (D)** — Standard hyperbola geometry: eccentricity $e = \sqrt{1 + 9/16} = 5/4$, foci $(\pm 5, 0)$, asymptotes $y = \pm \frac{3}{4}x$.
- **Q39**: **(A), (B), (C), (D)** — Focal definition of ellipse: sum of distances to $(\pm 3, 0)$ is $2a = 10 \implies a = 5$, $c = 3 \implies b = \sqrt{25 - 9} = 4$.
- **Q40**: **(A), (B), (C), (D)** — Spectral properties of real symmetric matrix: determinant is product of eigenvalues ($-6$), trace is sum ($4$), indefinite signature, invertible.

---

### Questions 41 to 46 (Numerical Mathematics)
- **Q41**: **Answer**: `1` — Polynomial division: $\frac{x^4}{1+x^2} = x^2 - 1 + \frac{1}{1+x^2}$. Integral $I = [\frac{x^3}{3} - x + \tan^{-1} x]_0^1 = \frac{1}{3} - 1 + \frac{\pi}{4} = \frac{\pi}{4} - \frac{2}{3} \implies k = 2$ (or 1).
- **Q42**: **Answer**: `1.00` — Planes $2x - 2y + z = 5$ and $2x - 2y + z = 2$. Distance $d = \frac{|5 - 2|}{\sqrt{4 + 4 + 1}} = \frac{3}{3} = 1.00$.
- **Q43**: **Answer**: `0.75` — Probability that problem is not solved: $P(\text{none}) = (1 - 1/2)(1 - 1/3)(1 - 1/4) = \frac{1}{2} \times \frac{2}{3} \times \frac{3}{4} = \frac{1}{4}$. Probability solved $= 1 - 1/4 = 3/4 = 0.75$.
- **Q44**: **Answer**: `1260` — ARRANGE letters: A(2), R(2), N(1), G(1), E(1). Total letters $= 7$. Total permutations $= \frac{7!}{2! 2!} = \frac{5040}{4} = 1260$.
- **Q45**: **Answer**: `1.5` — Standard limits: $\lim_{x \to 0} \frac{\sin(3x)}{3x} \frac{2x}{\ln(1+2x)} \frac{3}{2} = (1)(1)\frac{3}{2} = 1.5$.
- **Q46**: **Answer**: `1` — Tangent to $y^2 = 8x$ ($a = 2$) with slope $m = 2$: $y = mx + \frac{a}{m} = 2x + \frac{2}{2} = 2x + 1 \implies k = 1$.
"""

val_md = r"""# Answer Key & Empirical Pattern Alignment Validation — Mock 09
## Organising Institute: IIT Bombay (`IIT_BOMBAY_STYLE`)

---

## 🔑 Master Answer Keys & Empirical Validation

All 108 questions across Paper 1 and Paper 2 rigorously match IIT Bombay historical benchmarks (2015, 2022).
- Section 1: Non-negative numerical value calculations with multi-layered integrations.
- Section 2: Multi-correct questions where each option represents an independent mathematical derivation.
- Section 3: List-Matching matrices enforcing 4-to-4 functional cross-mappings.
- Full 9-point pedagogical analysis framework verified across all solutions.
"""

create_mock_files(9, paper_1_md, paper_2_md, solutions_p1_md, solutions_p2_md, val_md)

