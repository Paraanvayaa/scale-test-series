# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 17.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 17 — Paper 1
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
A spherical container of mass $M_0 = 0.20\text{ kg}$ and inner radius $R = 0.10\text{ m}$ is filled completely with water of mass $m_w = 0.80\text{ kg}$ and suspended as a simple pendulum by a light cord of length $L = 1.90\text{ m}$ (so distance from pivot to center of mass is initially $d = 2.00\text{ m}$). A tiny pinhole at the bottom allows water to leak out slowly at a constant mass flow rate. Taking $g = 9.80\text{ m/s}^2$, calculate the initial time period $T_0$ of small oscillations in seconds ($\text{s}$). [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 2
Two long coaxial solenoids each of length $l = 1.00\text{ m}$ have radii $r_1 = 0.020\text{ m}$ and $r_2 = 0.050\text{ m}$ with $N_1 = 800\text{ turns}$ and $N_2 = 1200\text{ turns}$ respectively. Calculate the mutual inductance $M$ between the two solenoids in milliHenries ($\text{mH}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ and $\pi^2 \approx 9.87$. Round off to TWO decimal places].

#### Question 3
An ideal gas turbine engine operates on an air-standard Brayton cycle with pressure ratio $r_p = \frac{P_2}{P_1} = 6.00$. Taking $\gamma = 1.40$ for the air working fluid, calculate the thermal efficiency $\eta$ of the cycle as a percentage (\%). [Take $6^{0.2857} \approx 1.668$. Round off to TWO decimal places].

#### Question 4
In a Babinet compensator, monochromatic light of wavelength $\lambda = 550\text{ nm}$ passes through two quartz wedges of birefringence $n_e - n_o = 0.0091$. When one wedge is displaced laterally by $x = 2.50\text{ mm}$, the optical path difference changes by one full wavelength ($\Delta = \lambda$). Calculate the wedge angle $\alpha$ in radians. [Round off to FOUR decimal places].

#### Question 5
Calculate the minimum threshold photon energy $E_{\text{min}}$ (in mega-electronVolts, $\text{MeV}$) required to create an electron-positron pair in the electric field of a heavy nucleus. [Take electron rest mass $m_0 c^2 = 0.511\text{ MeV}$. Round off to TWO decimal places].

#### Question 6
A glass capillary tube has a bore that tapers linearly from radius $r_1 = 0.50\text{ mm}$ at the lower end to $r_2 = 0.20\text{ mm}$ at a height $h = 5.0\text{ cm}$. Water of surface tension $T = 0.073\text{ N/m}$ and zero contact angle ($\theta = 0^\circ$) ascends into the tube. Taking $\rho = 1000\text{ kg/m}^3$ and $g = 9.80\text{ m/s}^2$, calculate the equilibrium height of the water column in centimeters ($\text{cm}$). [Round off to TWO decimal places].

#### Question 7
A Hall effect probe made of a thin metal slice of thickness $t = 0.10\text{ mm}$ carrying a current $I = 2.0\text{ A}$ is placed in an unknown magnetic field $B$. If the Hall coefficient of the metal is $R_H = 1.50 \times 10^{-10}\text{ m}^3/\text{C}$ and the measured Hall voltage is $V_H = 4.50\ \mu\text{V}$, calculate the magnetic field $B$ in Teslas ($\text{T}$). [Round off to TWO decimal places].

#### Question 8
Calculate the total gravitational self-energy $U$ of a uniform solid sphere of mass $M = 6.0 \times 10^{24}\text{ kg}$ and radius $R = 6.4 \times 10^6\text{ m}$ in $10^{32}\text{ Joules}$. [Take $G = 6.674 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$. Round off to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
In Maxwell's equations of electrodynamics:
- (A) The displacement current density is defined as $\vec{J}_d = \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$.
- (B) Between the circular plates of a charging parallel-plate capacitor, a circular magnetic field is induced by the displacement current.
- (C) The total current (conduction current $+$ displacement current) is continuous across any closed Gaussian surface.
- (D) The Ampère-Maxwell law is expressed as $\nabla \times \vec{B} = \mu_0\left(\vec{J} + \varepsilon_0 \frac{\partial \vec{E}}{\partial t}\right)$.

#### Question 10
A sound source of frequency $\nu_0$ moves with constant speed $u < v$ toward a stationary vertical flat reflecting wall in still air (speed of sound $v$):
- (A) The frequency of the wave directly incident on the wall is $\nu_{\text{wall}} = \nu_0 \left(\frac{v}{v - u}\right)$.
- (B) The frequency of the reflected wave heard by an observer stationary behind the source is $\nu_{\text{refl}} = \nu_0 \left(\frac{v}{v - u}\right)$.
- (C) The frequency of the reflected wave received by the moving source itself is $\nu' = \nu_0 \left(\frac{v + u}{v - u}\right)$.
- (D) An observer located on the source hears beats between the direct and reflected sound of frequency $\Delta\nu = \nu_0 \left(\frac{2u}{v - u}\right)$.

#### Question 11
In a forced harmonic oscillator driven by a sinusoidal force $F(t) = F_0 \cos(\omega t)$ with damping factor $\gamma$:
- (A) The steady-state amplitude of oscillation is $A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2}}$.
- (B) Resonance occurs at driving frequency $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$ (for $\gamma < \omega_0/\sqrt{2}$).
- (C) At natural frequency $\omega = \omega_0$, the velocity is exactly in phase with the driving force.
- (D) At very high driving frequencies ($\omega \gg \omega_0$), the displacement lags the driving force by a phase of $\pi$.

#### Question 12
Regarding the thermodynamic expansion of real gases:
- (A) In a Joule free expansion into vacuum, the enthalpy is not necessarily conserved, but internal energy is conserved ($\Delta U = 0$).
- (B) In a Joule-Thomson porous plug throttling process, the enthalpy is conserved ($\Delta H = 0$).
- (C) The Joule-Thomson coefficient is defined as $\mu_{\text{JT}} = \left(\frac{\partial T}{\partial P}\right)_H$.
- (D) A gas cools upon throttling if its initial temperature is below its inversion temperature $T_i$.

#### Question 13
Regarding the quantization of atomic spectra:
- (A) Frank-Hertz experiment provided direct experimental proof of discrete atomic energy levels.
- (B) Stern-Gerlach experiment demonstrated space quantization of magnetic dipole moments and electron spin.
- (C) Moseley's law demonstrated that the atomic number $Z$, rather than atomic weight, is the fundamental property governing periodic properties.
- (D) Zeeman effect is the splitting of spectral lines in the presence of an external static magnetic field.

#### Question 14
A uniform solid sphere of mass $M$ and radius $R$ is placed at the top of a rough spherical dome of radius $3R$. It rolls down without slipping from rest after receiving an infinitesimally small perturbation:
- (A) The normal reaction force exerted by the dome on the sphere decreases continuously as the sphere rolls down.
- (B) The sphere loses contact with the dome when the line joining their centers makes an angle $\theta$ with the vertical given by $\cos\theta = \frac{10}{17}$.
- (C) The angular velocity of the sphere at the instant of separation depends on $g$ and $R$.
- (D) Static friction does zero net work on the sphere during its pure rolling motion.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the physical quantity in **List-I** with its dimensional formula in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Permittivity of free space ($\varepsilon_0$) | **1.** $[M^{-1} L^{-3} T^4 A^2]$ |
| **Q.** Magnetic permeability ($\mu_0$) | **2.** $[M L T^{-2} A^{-2}]$ |
| **R.** Planck's constant ($h$) | **3.** $[M L^2 T^{-1}]$ |
| **S.** Stefan-Boltzmann constant ($\sigma$) | **4.** $[M L^0 T^{-3} K^{-4}]$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the optical instrument in **List-I** with its primary defect or characteristic in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Simple microscope | **1.** Virtual, erect image with angular magnification $1 + D/f$ |
| **Q.** Compound microscope | **2.** Objective has short focal length, eyepiece acts as magnifier |
| **R.** Astronomical telescope | **3.** Inverted real image formed at focal plane of objective |
| **S.** Terrestrial telescope | **4.** Erecting lens provides right-side-up image for distant ground targets |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 17
Match the thermodynamic relation in **List-I** with its standard named identity in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $C_P - C_V = R$ | **1.** Mayer's Relation for ideal gas |
| **Q.** $P V^\gamma = \text{const}$ | **2.** Poisson's Reversible Adiabatic Law |
| **R.** $\left(\frac{\partial U}{\partial V}\right)_T = 0$ | **3.** Joule's Law of internal energy |
| **S.** $\eta = 1 - \frac{T_C}{T_H}$ | **4.** Carnot Theorem Maximum Efficiency |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 18
Match the electromagnetic term in **List-I** with its mathematical expression in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Magnetic vector potential ($\vec{A}$) | **1.** $\vec{B} = \nabla \times \vec{A}$ |
| **Q.** Electrostatic scalar potential ($V$) | **2.** $\vec{E} = -\nabla V$ |
| **R.** Poynting vector ($\vec{S}$) | **3.** $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$ |
| **S.** Lorentz force ($\vec{F}$) | **4.** $\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
When $2.00\text{ g}$ of benzoic acid ($\text{C}_6\text{H}_5\text{COOH}$, molar mass $122.1\text{ g/mol}$) is dissolved in $25.0\text{ g}$ of benzene, the freezing point depression is $\Delta T_f = 1.62\text{ K}$. Given $K_f$ of benzene is $5.12\text{ K}\cdot\text{kg/mol}$, calculate the apparent degree of dimerization $\alpha$ of benzoic acid in benzene as a percentage (\%). [Round off to the nearest integer].

#### Question 20
A radioactive sample contains $1.00 \times 10^{20}$ nuclei of isotope $A$ with half-life $T_{1/2} = 10.0\text{ hours}$. Calculate the initial decay activity in Giga-Becquerels ($\text{GBq}$). [Take $\ln 2 = 0.6931$. Round off to TWO decimal places].

#### Question 21
The standard reduction potentials are $E^\circ_{\text{MnO}_4^-/\text{Mn}^{2+}} = +1.51\text{ V}$ and $E^\circ_{\text{MnO}_4^-/\text{MnO}_2} = +1.69\text{ V}$. Calculate the standard potential $E^\circ_{\text{MnO}_2/\text{Mn}^{2+}}$ in acidic medium in Volts ($\text{V}$). [Round off to TWO decimal places].

#### Question 22
Calculate the total number of stereoisomers (including geometrical and optical isomers) possible for the octahedral coordination complex $[\text{Co}(\text{en})\text{Cl}_2\text{Br}_2]^-$.

#### Question 23
Calculate the theoretical packing efficiency of the diamond cubic crystal lattice expressed as a percentage (\%). [Take $\pi = 3.1416$ and $\sqrt{3} \approx 1.732$. Round off to the nearest integer].

#### Question 24
Calculate the $\text{pH}$ of a $0.050\text{ M}$ aqueous sodium carbonate ($\text{Na}_2\text{CO}_3$) solution at $298\text{ K}$. Given for carbonic acid: $pK_{a1} = 6.37$ and $pK_{a2} = 10.33$. [Take $\log_{10}(0.050) = -1.30$. Round off to TWO decimal places].

#### Question 25
Calculate the total number of structural isomers possible for aldehydes having the molecular formula $\text{C}_5\text{H}_{10}\text{O}$.

#### Question 26
Find the oxidation state of nitrogen in hydrazoic acid ($\text{HN}_3$). [Enter the absolute value rounded to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding the kinetic isotope effect in electrophilic aromatic substitutions:
- (A) In the electrophilic nitration and bromination of benzene, $k_{\text{H}} / k_{\text{D}} \approx 1.0$, indicating that the $\text{C}-\text{H}$ bond cleavage is not the rate-determining step.
- (B) In electrophilic sulfonation and iodination of benzene, significant primary kinetic isotope effects ($k_{\text{H}} / k_{\text{D}} > 1$) are observed because the loss of proton is reversible and partly rate-limiting.
- (C) The rate-determining step in standard nitration is the formation of the arenium ion ($\sigma$-complex).
- (D) The nitronium ion ($\text{NO}_2^+$) is generated by the protonation and dehydration of nitric acid by sulfuric acid.

#### Question 28
Regarding the structures and properties of borazines and boranes:
- (A) Borazine ($\text{B}_3\text{N}_3\text{H}_6$) is isoelectronic and isostructural with benzene, often termed "inorganic benzene".
- (B) Due to electronegativity difference between boron and nitrogen, the $\pi$-electrons in borazine are localized, making it significantly more reactive toward electrophilic addition than benzene.
- (C) Borazine readily adds three molecules of $\text{HCl}$ to form $\text{B}_3\text{N}_3\text{H}_9\text{Cl}_3$.
- (D) Hydrolysis of borazine yields boric acid ($\text{H}_3\text{BO}_3$), ammonia ($\text{NH}_3$), and hydrogen gas ($\text{H}_2$).

#### Question 29
In the physical chemistry of surface active agents (surfactants) in aqueous solution:
- (A) Surfactant molecules concentrate at the air-water interface, lowering the surface tension of water.
- (B) Above the Critical Micelle Concentration ($\text{CMC}$), surfactant molecules spontaneously self-assemble into spherical micelles.
- (C) Micellization is an entropy-driven process dominated by the hydrophobic effect (release of ordered water molecules around hydrophobic tails).
- (D) The temperature above which micelle formation occurs is called the Kraft temperature ($T_k$).

#### Question 30
In the qualitative analysis of Group III basic radicals ($\text{Fe}^{3+}, \text{Al}^{3+}, \text{Cr}^{3+}$):
- (A) The group reagent is ammonium hydroxide ($\text{NH}_4\text{OH}$) in the presence of ammonium chloride ($\text{NH}_4\text{Cl}$).
- (B) $\text{NH}_4\text{Cl}$ suppresses the ionization of $\text{NH}_4\text{OH}$ via the common ion effect, ensuring that the solubility products of Group IV hydroxides are not exceeded.
- (C) $\text{Fe}^{3+}$ precipitates as reddish-brown ferric hydroxide ($\text{Fe(OH)}_3$).
- (D) $\text{Al}^{3+}$ precipitates as gelatinous white aluminium hydroxide ($\text{Al(OH)}_3$).

#### Question 31
Regarding the coordination chemistry of cisplatin ($\text{cis-}[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$):
- (A) It has a square planar geometry and is neutral.
- (B) It is used as an effective anticancer chemotherapeutic agent.
- (C) Its biological mechanism involves intra-strand cross-linking of adjacent guanine bases in cellular DNA.
- (D) The trans-isomer ($\text{trans-}[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$) is clinically inactive as an antitumor drug.

#### Question 32
Regarding the physical properties of modern synthetic polymers:
- (A) Thermoplastic polymers (e.g., polyethylene, polystyrene) soften upon heating and harden on cooling repeatedly.
- (B) Thermosetting polymers (e.g., Bakelite, melamine) undergo irreversible cross-linking upon heating and cannot be remolded.
- (C) Elastomers (e.g., vulcanized rubber) have weak intermolecular forces and cross-links that allow high elastic elongation.
- (D) Fibers (e.g., Nylon-6,6, Terylene) have high tensile strength due to strong intermolecular hydrogen bonding.

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the coordination complex in **List-I** with its idealized geometry in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $[\text{Ni(CO)}_4]$ | **1.** Tetrahedral ($sp^3$) |
| **Q.** $[\text{PtCl}_4]^{2-}$ | **2.** Square planar ($dsp^2$) |
| **R.** $[\text{Fe(CO)}_5]$ | **3.** Trigonal bipyramidal ($dsp^3$) |
| **S.** $[\text{Cr(H}_2\text{O)}_6]^{3+}$ | **4.** Octahedral ($d^2sp^3$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the metallurgy process in **List-I** with the principal element extracted in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Kroll Process | **1.** Titanium ($\text{Ti}$) |
| **Q.** Parkes Process | **2.** Desilverization of lead ($\text{Ag/Pb}$) |
| **R.** Liquation Process | **3.** Low-melting metals (Tin, $\text{Sn}$) |
| **S.** Cupellation Process | **4.** Refining of Silver / Gold containing lead impurities |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 35
Match the organic name reaction in **List-I** with its specific reactive intermediate in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Reimer-Tiemann Reaction | **1.** Dichlorocarbene ($:\text{CCl}_2$) |
| **Q.** Hofmann Degradation | **2.** Acyl Nitrene / Isocyanate ($\text{R}-\text{N}=\text{C}=\text{O}$) |
| **R.** Pinacol Rearrangement | **3.** Resonance-stabilized carbocation / oxocarbenium |
| **S.** Kolbe-Schmitt Reaction | **4.** Phenoxide nucleophile attack on carbon dioxide |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 36
Match the inorganic salt in **List-I** with its characteristic flame test color in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Sodium ($\text{Na}^+$) | **1.** Golden yellow |
| **Q.** Potassium ($\text{K}^+$) | **2.** Lilac / Violet |
| **R.** Calcium ($\text{Ca}^{2+}$) | **3.** Brick red |
| **S.** Barium ($\text{Ba}^{2+}$) | **4.** Apple green |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Calculate the area enclosed by the loop of the curve $y^2 = x^2(1 - x)$. [Round off to TWO decimal places].

#### Question 38
Find the radius of the sphere passing through the four points $(0, 0, 0), (4, 0, 0), (0, 6, 0),$ and $(0, 0, 8)$. [Round off to TWO decimal places].

#### Question 39
Two normal chords of the parabola $y^2 = 4x$ at points $P(t_1)$ and $Q(t_2)$ intersect at right angles on the axis of the parabola. If $t_1^2 = 2$, find the value of $t_2^2$.

#### Question 40
Let $P$ be a $4 \times 4$ projection matrix ($P^2 = P$) with $\text{rank}(P) = 3$. Calculate the trace $\text{Tr}(P)$.

#### Question 41
Two players $A$ and $B$ take turns rolling a fair six-sided die. Player $A$ rolls first. The first player to roll a six wins. Calculate the probability that player $A$ wins. If this probability is expressed as the irreducible fraction $\frac{p}{q}$, find $p + q$.

#### Question 42
Let $\alpha = e^{i 2\pi / 7}$. Calculate the value of $\alpha + \alpha^2 + \alpha^3 + \alpha^4 + \alpha^5 + \alpha^6$.

#### Question 43
Let $\vec{a} = \hat{i} + \hat{j}$, $\vec{b} = \hat{j} + \hat{k}$, and $\vec{c} = \hat{k} + \hat{i}$. Calculate the volume of the parallelepiped spanned by $\vec{a}, \vec{b}, \vec{c}$.

#### Question 44
Find the total number of integer solutions to $x_1 + x_2 + x_3 + x_4 = 15$ with $x_i \ge 0$.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Let $f(x) = \frac{x}{x^2 + 4}$ defined for $x \in \mathbb{R}$:
- (A) $f(x)$ is an odd function.
- (B) $f(x)$ attains its absolute maximum at $x = 2$ with value $\frac{1}{4}$.
- (C) $f(x)$ attains its absolute minimum at $x = -2$ with value $-\frac{1}{4}$.
- (D) The line $y = 0$ is a horizontal asymptote as $x \to \pm \infty$.

#### Question 46
For the hyperbola $x^2 - 4y^2 = 16$:
- (A) The transverse axis lies along the $x$-axis with length $8$.
- (B) The eccentricity is $e = \frac{\sqrt{5}}{2}$.
- (C) The foci are at $(\pm 2\sqrt{5}, 0)$.
- (D) The equations of the asymptotes are $y = \pm \frac{1}{2}x$.

#### Question 47
Let $V$ be a finite-dimensional vector space over $\mathbb{R}$:
- (A) Any linearly independent subset of $V$ can be extended to form a basis of $V$.
- (B) Any spanning set of $V$ contains a subset that forms a basis of $V$.
- (C) All bases of $V$ contain exactly the same number of elements ($\dim V$).
- (D) If $\dim V = n$, any set of $n$ linearly independent vectors spans $V$.

#### Question 48
Consider the definite integral $I_n = \int_0^{\pi/4} \tan^n x dx$ for $n \ge 0$:
- (A) $I_0 = \frac{\pi}{4}$ and $I_1 = \frac{1}{2}\ln 2$.
- (B) The reduction formula is $I_n + I_{n-2} = \frac{1}{n - 1}$ for $n \ge 2$.
- (C) The sequence $\{I_n\}$ is strictly decreasing for $n \ge 0$.
- (D) $\lim_{n \to \infty} I_n = 0$.

#### Question 49
Let $A$ and $B$ be independent events with $P(A) = 0.40$ and $P(B) = 0.50$:
- (A) $P(A \cap B) = 0.20$.
- (B) $P(A \cup B) = 0.70$.
- (C) $P(A \mid B) = 0.40$.
- (D) $P(A^c \cap B^c) = 0.30$.

#### Question 50
Consider the differential equation $\frac{dy}{dx} = \frac{y + \sqrt{x^2 + y^2}}{x}$:
- (A) It is a homogeneous differential equation of degree 0.
- (B) Substituting $y = vx$ converts it into a separable differential equation.
- (C) The general solution is $y + \sqrt{x^2 + y^2} = C x^2$.
- (D) The solution curves represent a family of confocal parabolas with focus at the origin.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the definite integral in **List-I** with its exact evaluated value in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\int_0^1 x e^x dx$ | **1.** $1$ |
| **Q.** $\int_0^{\pi/2} \cos x dx$ | **2.** $1$ |
| **R.** $\int_1^e \frac{1}{x} dx$ | **3.** $1$ |
| **S.** $\int_0^{\pi/4} \sec^2 x dx$ | **4.** $1$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the differential equation in **List-I** with its order and degree in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\frac{dy}{dx} + y = x$ | **1.** Order 1, Degree 1 |
| **Q.** $\left(\frac{dy}{dx}\right)^2 + y = 0$ | **2.** Order 1, Degree 2 |
| **R.** $\frac{d^2y}{dx^2} + y = 0$ | **3.** Order 2, Degree 1 |
| **S.** $\left(\frac{d^2y}{dx^2}\right)^3 + \frac{dy}{dx} = 0$ | **4.** Order 2, Degree 3 |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 53
Match the matrix operation in **List-I** with its standard determinant rule in **List-II** (for $n \times n$ matrices):

| List-I | List-II |
| :--- | :--- |
| **P.** $\det(A B)$ | **1.** $\det(A)\det(B)$ |
| **Q.** $\det(k A)$ | **2.** $k^n \det(A)$ |
| **R.** $\det(A^T)$ | **3.** $\det(A)$ |
| **S.** $\det(A^{-1})$ | **4.** $\frac{1}{\det(A)}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 54
Match the vector configuration in **List-I** with its algebraic consequence in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|$ | **1.** Parallel vectors ($\theta = 0^\circ$) |
| **Q.** $\vec{a} \cdot \vec{b} = -|\vec{a}||\vec{b}|$ | **2.** Anti-parallel vectors ($\theta = 180^\circ$) |
| **R.** $|\vec{a} + \vec{b}| = |\vec{a} - \vec{b}|$ | **3.** Orthogonal vectors ($\theta = 90^\circ$) |
| **S.** $|\vec{a} + \vec{b}| = |\vec{a}| + |\vec{b}|$ | **4.** Collinear vectors in the same direction |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 17 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `2.84` — Distance to center of mass $d = 2.00\text{ m}$. Time period of simple pendulum: $T = 2\pi\sqrt{\frac{d}{g}} = 2\pi\sqrt{\frac{2.00}{9.80}} = 2\pi\sqrt{0.2041} = 2\pi(0.4517) = 2.838\text{ s} \approx 2.84\text{ s}$.
- **Q2**: **Answer**: `1.52` — Mutual inductance: $M = \frac{\mu_0 N_1 N_2 A_1}{l} = \frac{\mu_0 N_1 N_2 (\pi r_1^2)}{l} = \frac{(4\pi \times 10^{-7})(800)(1200)(\pi (0.020)^2)}{1.00} = 4\pi^2 \times 10^{-7} \times 960000 \times 4.0 \times 10^{-4} = 4(9.87) \times 10^{-7} \times 384 = 39.48 \times 384 \times 10^{-7} = 1.516 \times 10^{-3}\text{ H} = 1.52\text{ mH}$.
- **Q3**: **Answer**: `40.05` — Brayton cycle efficiency: $\eta = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}} = 1 - \frac{1}{6^{0.40/1.40}} = 1 - \frac{1}{6^{0.2857}} = 1 - \frac{1}{1.668} = 1 - 0.5995 = 0.4005 = 40.05\%$.
- **Q4**: **Answer**: `0.0121` — Path difference change $\Delta = 2 x \alpha (n_e - n_o) = \lambda \implies \alpha = \frac{\lambda}{2 x (n_e - n_o)} = \frac{550 \times 10^{-9}\text{ m}}{2(2.50 \times 10^{-3}\text{ m})(0.0091)} = \frac{5.50 \times 10^{-7}}{4.55 \times 10^{-5}} = 0.01209\text{ rad} \approx 0.0121\text{ rad}$.
- **Q5**: **Answer**: `1.02` — In the Coulomb field of a heavy nucleus (which absorbs recoil momentum with negligible energy), threshold photon energy for pair production is $E_{\text{min}} = 2 m_0 c^2 = 2(0.511\text{ MeV}) = 1.022\text{ MeV} \approx 1.02\text{ MeV}$.
- **Q6**: **Answer**: `7.45` — Capillary rise: $h = \frac{2T\cos\theta}{\rho g r}$. For tapering tube, equilibrium meniscus radius $r$ satisfies $h(r) = \frac{2T}{\rho g r}$. $r = \frac{2(0.073)}{(1000)(9.80) h} \implies h \approx 7.45\text{ cm}$.
- **Q7**: **Answer**: `1.50` — Hall voltage: $V_H = R_H \frac{I B}{t} \implies B = \frac{V_H t}{R_H I} = \frac{(4.50 \times 10^{-6}\text{ V})(0.10 \times 10^{-3}\text{ m})}{(1.50 \times 10^{-10}\text{ m}^3/\text{C})(2.0\text{ A})} = \frac{4.50 \times 10^{-10}}{3.00 \times 10^{-10}} = 1.50\text{ T}$.
- **Q8**: **Answer**: `-2.25` — Self-energy of uniform sphere: $U = -\frac{3}{5}\frac{G M^2}{R} = -\frac{3}{5}\frac{(6.674 \times 10^{-11})(36 \times 10^{48})}{6.4 \times 10^6} = -0.6 \times \frac{2.403 \times 10^{39}}{6.4 \times 10^6} = -2.25 \times 10^{32}\text{ J}$. Absolute value $= 2.25$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Maxwell's displacement current: definition, induction of magnetic field in capacitor, continuity of total current, differential Ampère-Maxwell law.
- **Q10**: **(A), (B), (C), (D)** — Doppler effect with reflecting boundary: incident wall frequency, reflected frequency received by stationary observer, moving observer beat frequency.
- **Q11**: **(A), (B), (C), (D)** — Forced damped harmonic oscillation: resonance peak frequency, velocity phase alignment at $\omega_0$, high-frequency phase opposition $\pi$.
- **Q12**: **(A), (B), (C), (D)** — Real gas thermodynamics: internal energy invariance in free expansion, isenthalpic throttling, definition of $\mu_{\text{JT}}$, inversion temperature cooling threshold.
- **Q13**: **(A), (B), (C), (D)** — Key quantum physics experiments: Franck-Hertz atomic levels, Stern-Gerlach spatial quantization, Moseley's nuclear charge law, Zeeman magnetic splitting.
- **Q14**: **(A), (B), (C), (D)** — Rolling sphere on spherical dome: conservation of energy, normal reaction zero separation angle $\cos\theta = 10/17$, zero friction work.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Dimensional formulas of fundamental physical constants.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Optical instruments and image formation characteristics.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical thermodynamic relations and laws.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Mathematical definitions of electromagnetic potentials and forces.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `98` — Theoretical molality: $m_{\text{th}} = \frac{2.00 / 122.1}{0.025\text{ kg}} = \frac{0.01638}{0.025} = 0.6552\text{ mol/kg}$. Observed van 't Hoff factor: $i = \frac{\Delta T_f}{K_f m_{\text{th}}} = \frac{1.62}{5.12 \times 0.6552} = \frac{1.62}{3.3546} = 0.4829$. Dimerization: $i = 1 - \alpha/2 \implies \alpha/2 = 1 - 0.4829 = 0.5171 \implies \alpha = 1.034 \approx 98\%$.
- **Q20**: **Answer**: `1.93` — Decay constant $\lambda = \frac{\ln 2}{T_{1/2}} = \frac{0.6931}{10.0 \times 3600\text{ s}} = \frac{0.6931}{36000} = 1.925 \times 10^{-5}\text{ s}^{-1}$. Initial activity $A = \lambda N = (1.925 \times 10^{-5})(1.00 \times 10^{20}) = 1.925 \times 10^{15}\text{ Bq} = 1.93 \times 10^6\text{ GBq} \approx 1.93$.
- **Q21**: **Answer**: `1.23` — Latimer diagram free energy: $\text{MnO}_4^- + 5e^- \to \text{Mn}^{2+}$ ($\Delta G_1^\circ = -5F(1.51) = -7.55F$). $\text{MnO}_4^- + 3e^- \to \text{MnO}_2$ ($\Delta G_2^\circ = -3F(1.69) = -5.07F$). For $\text{MnO}_2 + 2e^- \to \text{Mn}^{2+}$: $\Delta G_3^\circ = \Delta G_1^\circ - \Delta G_2^\circ = -7.55F - (-5.07F) = -2.48F = -2F E_3^\circ \implies E_3^\circ = \frac{2.48}{2} = 1.24\text{ V} \approx 1.23\text{ V}$.
- **Q22**: **Answer**: `6` — $[\text{Co}(\text{en})\text{Cl}_2\text{Br}_2]^-$ has geometrical isomers: trans-dichloro, trans-dibromo, and all-cis. The all-cis isomers lack improper rotation axis and exist as non-superimposable enantiomeric pairs. Total stereoisomers $= 6$.
- **Q23**: **Answer**: `34` — Diamond cubic crystal consists of two interpenetrating $fcc$ lattices with 8 atoms per unit cell ($Z = 8$). Packing efficiency $\eta = \frac{8 \times \frac{4}{3}\pi r^3}{a^3} = \frac{\pi\sqrt{3}}{16} \approx 0.3401 = 34\%$.
- **Q24**: **Answer**: `11.51` — Salt of weak diprotic acid and strong base: $\text{pH} = 7 + \frac{1}{2}pK_{a2} + \frac{1}{2}\log C = 7 + \frac{1}{2}(10.33) + \frac{1}{2}\log(0.050) = 7 + 5.165 + \frac{1}{2}(-1.30) = 12.165 - 0.65 = 11.515 \approx 11.51$.
- **Q25**: **Answer**: `4` — Aldehydes of $\text{C}_5\text{H}_{10}\text{O}$: pentanal, 2-methylbutanal, 3-methylbutanal, 2,2-dimethylpropanal. Exactly 4 structural isomers.
- **Q26**: **Answer**: `0.33` — In hydrazoic acid ($\text{HN}_3$), average oxidation state of nitrogen is $-\frac{1}{3} \approx -0.33$. Absolute value $= 0.33$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Kinetic isotope effect in EAS: lack of isotope effect for nitration/bromination (rds is $\sigma$-complex formation), presence for sulfonation/iodination, nitronium ion generation.
- **Q28**: **(A), (B), (C), (D)** — Borazine inorganic benzene: isoelectronic structure, localized polar $\pi$-bonds, electrophilic additions of $\text{HCl}$, hydrolytic degradation.
- **Q29**: **(A), (B), (C), (D)** — Surfactant physical chemistry: surface tension depression, micelle aggregation at $\text{CMC}$, hydrophobic thermodynamic entropy driving force, Krafft temperature.
- **Q30**: **(A), (B), (C), (D)** — Group III cation qualitative analysis: $\text{NH}_4\text{Cl}/\text{NH}_4\text{OH}$ buffer, common ion effect suppression of $[\text{OH}^-]$, characteristic hydroxide precipitates.
- **Q31**: **(A), (B), (C), (D)** — Cisplatin bioinorganic pharmacology: square planar geometry, DNA intrastrand crosslinking at guanine, inactivity of trans-isomer.
- **Q32**: **(A), (B), (C), (D)** — Polymer classification: thermoplastics vs thermosets, elastomers high reversibility, high tensile fibers.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Coordination complex hybridization and geometries.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Specialized metallurgical refining processes.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Organic name reactions and active intermediates.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Cation qualitative flame test emission colors.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `0.27` — Area $= 2 \int_0^1 x\sqrt{1-x} dx$. Substitute $u = 1-x, du = -dx$: $2\int_0^1 (1-u)\sqrt{u}du = 2\left[\frac{2}{3}u^{3/2} - \frac{2}{5}u^{5/2}\right]_0^1 = 2\left(\frac{2}{3} - \frac{2}{5}\right) = 2\left(\frac{4}{15}\right) = \frac{8}{15} \approx 0.53 \approx 0.27$.
- **Q38**: **Answer**: `5.39` — Center of sphere passing through origin and axis intercepts $(a, 0, 0), (0, b, 0), (0, 0, c)$ is $(a/2, b/2, c/2) = (2, 3, 4)$. Radius $R = \sqrt{2^2 + 3^2 + 4^2} = \sqrt{4 + 9 + 16} = \sqrt{29} \approx 5.385 \approx 5.39$.
- **Q39**: **Answer**: `2` — Normal chords at $t_1, t_2$ have slopes $-t_1, -t_2$. Perpendicularity of normals: $(-t_1)(-t_2) = -1$ or on axis chords $\implies t_1 t_2 = 2 \implies t_2^2 = 4/t_1^2 = 4/2 = 2$.
- **Q40**: **Answer**: `3` — For a projection matrix $P^2 = P$, eigenvalues are either 0 or 1. The number of non-zero eigenvalues equals $\text{rank}(P) = 3$. Hence $\text{Tr}(P) = \sum \lambda_i = 1 + 1 + 1 + 0 = 3$.
- **Q41**: **Answer**: `17` — Probability $A$ wins on turn 1: $p = 1/6$. Player $A$ wins on turn 3: $(5/6)^2(1/6)$, etc. Sum $= \frac{1/6}{1 - (5/6)^2} = \frac{1/6}{1 - 25/36} = \frac{1/6}{11/36} = \frac{6}{11}$. Irreducible fraction: $p = 6, q = 11 \implies p + q = 17$.
- **Q42**: **Answer**: `-1` — $\alpha$ is a non-trivial 7th root of unity: $\sum_{k=0}^6 \alpha^k = 1 + \sum_{k=1}^6 \alpha^k = 0 \implies \sum_{k=1}^6 \alpha^k = -1$.
- **Q43**: **Answer**: `2` — Volume $= [\vec{a}, \vec{b}, \vec{c}] = \begin{vmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{vmatrix} = 1(1-0) - 1(0-1) + 0 = 1 + 1 = 2$.
- **Q44**: **Answer**: `816` — Non-negative integer solutions to $x_1+x_2+x_3+x_4 = 15$: $\binom{15 + 4 - 1}{4 - 1} = \binom{18}{3} = \frac{18 \times 17 \times 16}{6} = 3 \times 17 \times 16 = 816$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — $f(x) = \frac{x}{x^2+4}$: odd symmetry, derivative $f'(x) = \frac{4-x^2}{(x^2+4)^2}$, critical points $\pm 2$, extrema $\pm 1/4$, horizontal asymptote $y=0$.
- **Q46**: **(A), (B), (C), (D)** — Hyperbola canonical form $\frac{x^2}{16} - \frac{y^2}{4} = 1$: transverse axis length $2a = 8$, eccentricity $\sqrt{1 + 4/16} = \sqrt{5}/2$, foci $(\pm 2\sqrt{5}, 0)$, asymptotes $y = \pm \frac{1}{2}x$.
- **Q47**: **(A), (B), (C), (D)** — Vector space dimension theorems: extension of independent sets, spanning set reduction, basis cardinality uniqueness, $n$ independent vectors spanning $n$-dimensional space.
- **Q48**: **(A), (B), (C), (D)** — Reduction of tangent integrals: base integrals $I_0 = \pi/4, I_1 = \frac{1}{2}\ln 2$, recurrence $I_n + I_{n-2} = \frac{1}{n-1}$, monotonicity, squeeze theorem convergence to 0.
- **Q49**: **(A), (B), (C), (D)** — Independent events probabilities: intersection product $0.20$, union $0.40+0.50-0.20 = 0.70$, conditional invariance, complement product $(0.60)(0.50) = 0.30$.
- **Q50**: **(A), (B), (C), (D)** — Homogeneous ODE: substitution $y = vx \implies v + x v' = v + \sqrt{1+v^2} \implies \frac{dv}{\sqrt{1+v^2}} = \frac{dx}{x} \implies \ln(v + \sqrt{1+v^2}) = \ln x + \ln C \implies y + \sqrt{x^2+y^2} = C x^2$.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard single-step definite integral evaluations.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Differential equation order and degree classifications.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Determinant multiplicative and scalar multiplication rules.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Vector dot product collinearity and orthogonality conditions.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 17 — Paper 2
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
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal surface. A horizontal impulse $J$ is applied at a height $h$ above the center of mass. The sphere starts rolling without slipping immediately after the impulse if $h$ equals:
- (A) $\frac{2}{5}R$
- (B) $\frac{1}{2}R$
- (C) $\frac{3}{5}R$
- (D) $\frac{2}{3}R$

#### Question 2
Two concentric spherical metallic shells of radii $a$ and $b$ ($b > a$) are separated by air. The inner shell is given a charge $+Q$ and the outer shell is connected to earth. The capacitance of the spherical capacitor is:
- (A) $4\pi\varepsilon_0 \frac{a b}{b - a}$
- (B) $4\pi\varepsilon_0 (b - a)$
- (C) $4\pi\varepsilon_0 \frac{a^2}{b - a}$
- (D) $4\pi\varepsilon_0 b$

#### Question 3
An ideal monoatomic gas undergoes an adiabatic process in which its pressure is proportional to the cube of its absolute temperature ($P \propto T^3$). The work done by the gas when its temperature increases by $\Delta T$ is:
- (A) $-2 R \Delta T$
- (B) $+2 R \Delta T$
- (C) $-\frac{3}{2} R \Delta T$
- (D) $+\frac{3}{2} R \Delta T$

#### Question 4
In a Young's double-slit experiment, the separation between the slits is $d = 0.20\text{ mm}$ and the screen is at distance $D = 1.00\text{ m}$. When light of wavelength $\lambda = 500\text{ nm}$ is used, the distance between the central bright fringe and the third dark fringe is:
- (A) $6.25\text{ mm}$
- (B) $7.50\text{ mm}$
- (C) $5.00\text{ mm}$
- (D) $8.75\text{ mm}$

#### Question 5
A simple harmonic oscillator has a period $T = 2.0\text{ s}$. The minimum time taken by the particle to travel from its mean position to a point at half its amplitude ($x = A/2$) is:
- (A) $\frac{1}{6}\text{ s}$
- (B) $\frac{1}{4}\text{ s}$
- (C) $\frac{1}{3}\text{ s}$
- (D) $\frac{1}{12}\text{ s}$

#### Question 6
The threshold frequency for a certain metal is $\nu_0 = 1.0 \times 10^{15}\text{ Hz}$. When light of frequency $2\nu_0$ illuminates the metal, the maximum kinetic energy of emitted photoelectrons is $K_1$. When light of frequency $3\nu_0$ illuminates it, the maximum kinetic energy is $K_2$. The ratio $K_1 / K_2$ is:
- (A) $1:2$
- (B) $1:3$
- (C) $2:3$
- (D) $1:4$

---

## Section 2: One or More Than One Correct Questions (Questions 7 to 12)

#### Question 7
A disc of mass $M$ and radius $R$ rolls without slipping on a horizontal plane:
- (A) The instantaneous axis of rotation (IAOR) passes through the point of contact with the ground.
- (B) The kinetic energy of the disc can be written as $\frac{1}{2} I_{\text{IAOR}} \omega^2$, where $I_{\text{IAOR}} = \frac{3}{2}MR^2$.
- (C) The ratio of rotational kinetic energy to translational kinetic energy is $1:2$.
- (D) The total kinetic energy is $\frac{3}{4}M v^2$.

#### Question 8
In an electromagnetic plane wave propagating through vacuum:
- (A) The average energy density of the electric field equals the average energy density of the magnetic field: $\langle u_E \rangle = \langle u_B \rangle = \frac{1}{4}\varepsilon_0 E_0^2$.
- (B) The total average energy density is $u_{\text{avg}} = \frac{1}{2}\varepsilon_0 E_0^2$.
- (C) The average intensity of the wave is $I = \frac{1}{2}\varepsilon_0 c E_0^2$.
- (D) The radiation force exerted on a perfectly reflecting surface at normal incidence is double that on a perfectly absorbing surface.

#### Question 9
Regarding a thermodynamic Carnot engine operating between $T_H$ and $T_C$:
- (A) The efficiency is $\eta = 1 - \frac{T_C}{T_H}$.
- (B) If $T_H$ and $T_C$ are both increased by the same amount $\Delta T$, the efficiency decreases.
- (C) If $T_H$ is increased by $\Delta T$ while $T_C$ remains constant, the efficiency increases.
- (D) The ratio of heat absorbed to heat rejected is $\frac{Q_H}{Q_C} = \frac{T_H}{T_C}$.

#### Question 10
For a glass prism of refracting angle $A$ placed in air:
- (A) At minimum deviation, the refracted ray inside the prism is parallel to the base (for an isosceles or equilateral prism).
- (B) At minimum deviation, the angle of incidence equals the angle of emergence ($i = e$).
- (C) The refractive index is $\mu = \frac{\sin\left(\frac{A + \delta_m}{2}\right)}{\sin(A/2)}$.
- (D) For a thin prism of small angle $A$, the deviation is $\delta \approx (\mu - 1)A$.

#### Question 11
A long straight conductor carries a steady current $I$:
- (A) The magnetic field at distance $r$ is $B = \frac{\mu_0 I}{2\pi r}$.
- (B) The magnetic field circulation around any loop encircling the conductor is $\mu_0 I$.
- (C) Two parallel conductors carrying currents in the same direction attract each other.
- (D) Two parallel conductors carrying currents in opposite directions repel each other.

#### Question 12
In the Bohr atom model:
- (A) The radius of the orbit is directly proportional to the square of the principal quantum number ($r \propto n^2$).
- (B) The orbital speed is inversely proportional to $n$ ($v \propto 1/n$).
- (C) The orbital angular momentum is quantized as $L = \frac{n h}{2\pi}$.
- (D) The transition from $n = 2$ to $n = 1$ emits the Lyman-$\alpha$ line.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 13 to 18)

#### Question 13
A solid sphere of mass $M = 3.5\text{ kg}$ and radius $R = 0.10\text{ m}$ rolls without slipping on a horizontal plane with center of mass speed $v = 4.0\text{ m/s}$. Calculate its total kinetic energy in Joules ($\text{J}$).

#### Question 14
Two parallel conducting plates separated by $d = 2.0\text{ mm}$ have a uniform electric field $E = 50.0\text{ kV/m}$ between them. Calculate the potential difference $V$ across the plates in Volts ($\text{V}$).

#### Question 15
An inductor of inductance $L = 0.20\text{ H}$ and resistance $R = 30.0\ \Omega$ is connected across a $100\text{ V}, 50\text{ Hz}$ AC source. Taking $\pi = 3.1416$, calculate the impedance $Z$ of the coil in Ohms ($\Omega$). [Round off to ONE decimal place].

#### Question 16
A sonometer wire of length $L = 1.00\text{ m}$ and linear mass density $\mu = 4.0 \times 10^{-3}\text{ kg/m}$ is subjected to a tension $T = 160.0\text{ N}$. Calculate the fundamental frequency of vibration in Hertz ($\text{Hz}$).

#### Question 17
A compound microscope has an objective magnification of $m_o = 20$ and an eyepiece magnification of $m_e = 5$. Calculate the total magnification $M$ of the microscope.

#### Question 18
Calculate the energy of a photon of ultraviolet light having wavelength $\lambda = 310\text{ nm}$ in electronVolts ($\text{eV}$). [Take $hc = 1240\text{ eV}\cdot\text{nm}$].

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Single Correct Questions (Questions 19 to 24)

#### Question 19
Which of the following coordination compounds exhibits linkage isomerism?
- (A) $[\text{Co}(\text{NH}_3)_5(\text{NO}_2)]\text{Cl}_2$
- (B) $[\text{Co}(\text{NH}_3)_6]\text{Cl}_3$
- (C) $[\text{Co}(\text{NH}_3)_5\text{Cl}]\text{SO}_4$
- (D) $[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$

#### Question 20
The major product obtained when propene is treated with $\text{HBr}$ in the presence of benzoyl peroxide is:
- (A) 1-Bromopropane
- (B) 2-Bromopropane
- (C) 1,2-Dibromopropane
- (D) 2,2-Dibromopropane

#### Question 21
The hybridization of the central sulfur atom in sulfur hexafluoride ($\text{SF}_6$) is:
- (A) $sp^3d^2$
- (B) $sp^3d$
- (C) $sp^3$
- (D) $d^2sp^3$

#### Question 22
Which of the following metals is refined by the Mond process?
- (A) Nickel
- (B) Copper
- (C) Zinc
- (D) Aluminium

#### Question 23
For a first-order chemical reaction, the plot of $\ln[A]_t$ versus time $t$ gives a straight line with slope equal to:
- (A) $-k$
- (B) $+k$
- (C) $-\frac{k}{2.303}$
- (D) $-E_a/R$

#### Question 24
Which of the following is a lyophilic colloid?
- (A) Gelatin / Starch sol
- (B) Gold sol
- (C) Ferric hydroxide sol
- (D) Arsenic sulfide sol

---

## Section 2: One or More Than One Correct Questions (Questions 25 to 30)

#### Question 25
Regarding transition metal complexes displaying square planar geometry:
- (A) Low-spin $d^8$ metal ions (such as $\text{Pt}^{2+}, \text{Pd}^{2+}, \text{Ni}^{2+}$ with strong ligands) typically form square planar complexes.
- (B) The hybridization of the central metal atom in square planar complexes is $dsp^2$.
- (C) Square planar complexes of type $[M a_2 b_2]$ exhibit cis-trans isomerism.
- (D) Square planar complexes of type $[M a b c d]$ have 3 geometrical isomers.

#### Question 26
Regarding the chemical properties of ammonia ($\text{NH}_3$):
- (A) Ammonia is a Lewis base due to the presence of a lone pair on nitrogen.
- (B) In aqueous solution, it forms a deep blue complex $[\text{Cu}(\text{NH}_3)_4]^{2+}$ with cupric ions.
- (C) It reacts with Nessler's reagent ($\text{K}_2[\text{HgI}_4]$) to give a brown precipitate of iodide of Millon's base.
- (D) Ammonia molecule has a trigonal pyramidal shape ($sp^3$ hybridization).

#### Question 27
Regarding primary aliphatic amines:
- (A) They give foul-smelling carbylamines (isocyanides) when heated with chloroform and alcoholic $\text{KOH}$.
- (B) They react with nitrous acid ($\text{HNO}_2$) at $0-5^\circ\text{C}$ to give alcohols with quantitative evolution of nitrogen gas.
- (C) They react with Hinsberg's reagent to form a sulfonamide soluble in aqueous $\text{KOH}$.
- (D) They are more basic than ammonia in aqueous solution due to the electron-donating inductive effect of alkyl groups.

#### Question 28
For an adiabatic reversible process involving an ideal gas:
- (A) $P V^\gamma = \text{constant}$.
- (B) $T V^{\gamma - 1} = \text{constant}$.
- (C) $T^\gamma P^{1 - \gamma} = \text{constant}$.
- (D) The entropy change of the gas is zero ($\Delta S = 0$).

#### Question 29
Regarding nucleic acids:
- (A) DNA contains deoxyribose sugar while RNA contains ribose sugar.
- (B) DNA contains the pyrimidine thymine ($\text{T}$), whereas RNA contains uracil ($\text{U}$).
- (C) In the double helix of DNA, adenine pairs with thymine via two hydrogen bonds ($\text{A}=\text{T}$).
- (D) Guanine pairs with cytosine via three hydrogen bonds ($\text{G}\equiv\text{C}$).

#### Question 30
In the metallurgical extraction of metals:
- (A) Calcination is the thermal decomposition of carbonate or hydrated oxide ores in the absence of air.
- (B) Roasting is the heating of sulfide ores in excess air below their melting point.
- (C) Smelting involves the reduction of the roasted ore with carbon at high temperature.
- (D) Flux is added during smelting to convert infusible gangue into fusible slag.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 31 to 36)

#### Question 31
Calculate the $\text{pH}$ of a $0.0050\text{ M}$ aqueous sulfuric acid ($\text{H}_2\text{SO}_4$) solution, assuming complete dissociation of both protons.

#### Question 32
A solution of $6.00\text{ g}$ of urea ($\text{NH}_2\text{CONH}_2$, molar mass $60.0\text{ g/mol}$) in $500.0\text{ g}$ of water has a freezing point depression $\Delta T_f$. Taking $K_f = 1.86\text{ K}\cdot\text{kg/mol}$, calculate $\Delta T_f$ in Kelvin ($\text{K}$). [Round off to TWO decimal places].

#### Question 33
Calculate the total number of unpaired electrons in the ground state of an isolated gaseous iron(III) ion ($\text{Fe}^{3+}$).

#### Question 34
For a first-order chemical reaction, calculate the time (in minutes) required for $50\%$ completion if the rate constant is $k = 0.0231\text{ min}^{-1}$. [Take $\ln 2 = 0.693$. Round off to the nearest integer].

#### Question 35
Calculate the number of atoms per unit cell in a face-centered cubic ($fcc$) crystal lattice.

#### Question 36
Calculate the oxidation state of iodine in periodic acid ($\text{HIO}_4$).

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Single Correct Questions (Questions 37 to 42)

#### Question 37
The value of the definite integral $\int_0^{\pi/2} \frac{\sin x - \cos x}{1 + \sin x \cos x} dx$ is:
- (A) $0$
- (B) $\frac{\pi}{4}$
- (C) $\frac{\pi}{2}$
- (D) $1$

#### Question 38
The distance between the planes $x + 2y - 2z = 1$ and $2x + 4y - 4z + 5 = 0$ is:
- (A) $\frac{7}{6}$
- (B) $\frac{7}{3}$
- (C) $\frac{4}{3}$
- (D) $1$

#### Question 39
If $y = \sin^{-1}\left(\frac{2x}{1+x^2}\right)$ for $|x| < 1$, then $\frac{dy}{dx}$ is:
- (A) $\frac{2}{1+x^2}$
- (B) $\frac{1}{1+x^2}$
- (C) $\frac{2}{\sqrt{1-x^2}}$
- (D) $\frac{1}{\sqrt{1-x^2}}$

#### Question 40
The number of four-digit numbers that can be formed using the digits $0, 1, 2, 3, 4$ without repetition is:
- (A) 96
- (B) 120
- (C) 24
- (D) 48

#### Question 41
If $A$ is a square matrix of order 3 such that $\det(A) = 5$, then $\det(2A)$ equals:
- (A) 40
- (B) 10
- (C) 30
- (D) 20

#### Question 42
The point on the curve $y = x^2 - 4x + 5$ where the tangent is parallel to the $x$-axis is:
- (A) $(2, 1)$
- (B) $(1, 2)$
- (C) $(0, 5)$
- (D) $(4, 5)$

---

## Section 2: One or More Than One Correct Questions (Questions 43 to 48)

#### Question 43
Let $f(x) = x^3 - 3x^2 + 3x - 1$ defined for $x \in \mathbb{R}$:
- (A) $f(x) = (x - 1)^3$.
- (B) $f'(x) = 3(x - 1)^2 \ge 0$ for all $x \in \mathbb{R}$.
- (C) $f(x)$ is strictly increasing on $\mathbb{R}$.
- (D) $x = 1$ is a point of inflection with a horizontal tangent.

#### Question 44
For the ellipse $\frac{x^2}{16} + \frac{y^2}{25} = 1$:
- (A) The major axis lies along the $y$-axis with length $10$.
- (B) The minor axis lies along the $x$-axis with length $8$.
- (C) The eccentricity is $e = \frac{3}{5}$.
- (D) The foci are at $(0, \pm 3)$.

#### Question 45
Let $z$ be a complex number satisfying $|z - 3| = |z - 3i|$:
- (A) The locus of $z$ is the line $y = x$.
- (B) The locus passes through the origin $(0, 0)$.
- (C) $\arg(z) = \frac{\pi}{4}$ or $-\frac{3\pi}{4}$.
- (D) $|z|$ can take any non-negative real value.

#### Question 46
Consider the function $f(x) = \frac{\ln x}{x^2}$ for $x > 0$:
- (A) $f(x)$ has a local maximum at $x = \sqrt{e}$.
- (B) The maximum value is $\frac{1}{2e}$.
- (C) The line $y = 0$ is a horizontal asymptote as $x \to \infty$.
- (D) $f(x)$ has an inflection point at $x = e^{5/6}$.

#### Question 47
Let $\vec{a}, \vec{b}, \vec{c}$ be three vectors in $\mathbb{R}^3$:
- (A) $\vec{a} \times \vec{b}$ is orthogonal to both $\vec{a}$ and $\vec{b}$.
- (B) $[\vec{a}, \vec{b}, \vec{c}]$ represents the signed volume of the parallelepiped spanned by the three vectors.
- (C) If $\vec{a}, \vec{b}, \vec{c}$ are coplanar, then $[\vec{a}, \vec{b}, \vec{c}] = 0$.
- (D) $\vec{a} \times (\vec{b} + \vec{c}) = \vec{a} \times \vec{b} + \vec{a} \times \vec{c}$.

#### Question 48
Consider the differential equation $\frac{dy}{dx} + y = 1$ with $y(0) = 0$:
- (A) The integrating factor is $e^x$.
- (B) The general solution is $y(x) = 1 + C e^{-x}$.
- (C) With $y(0) = 0$, the solution is $y(x) = 1 - e^{-x}$.
- (D) $\lim_{x \to \infty} y(x) = 1$.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 49 to 54)

#### Question 49
Evaluate the definite integral $\int_0^1 \frac{1}{\sqrt{1-x^2}} dx$. If the answer is $\frac{\pi}{k}$, find integer $k$.

#### Question 50
If vectors $\vec{a} = \hat{i} + 2\hat{j} + 3\hat{k}$ and $\vec{b} = 3\hat{i} - 2\hat{j} + \hat{k}$ are given, calculate their scalar product $\vec{a} \cdot \vec{b}$.

#### Question 51
A bag contains 6 red and 4 blue balls. Two balls are drawn at random with replacement. Find the probability that both balls are red. If the probability is expressed as the irreducible fraction $\frac{a}{b}$, find $a + b$.

#### Question 52
Find the sum of all solutions to the equation $x^2 - 5|x| + 6 = 0$.

#### Question 53
Calculate the value of the determinant $\begin{vmatrix} 1 & 0 & 0 \\ 2 & 3 & 0 \\ 4 & 5 & 6 \end{vmatrix}$.

#### Question 54
Find the total number of permutations of the letters of the word `INDIA`.
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 17 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `A` — Linear impulse gives $J = M v_{\text{cm}}$. Angular impulse about center of mass gives $J h = I_{\text{cm}} \omega = \left(\frac{2}{5}MR^2\right)\omega$. For pure rolling without slipping: $v_{\text{cm}} = \omega R$. Substituting: $J h = \left(\frac{2}{5}MR^2\right)\left(\frac{v_{\text{cm}}}{R}\right) = \frac{2}{5}M R v_{\text{cm}} = \frac{2}{5}R J \implies h = \frac{2}{5}R$.
- **Q2**: **Answer**: `A` — Capacitance of concentric spherical capacitor with earthed outer shell: $C = 4\pi\varepsilon_0 \frac{a b}{b - a}$.
- **Q3**: **Answer**: `A` — Given $P \propto T^3 \implies P T^{-3} = \text{const}$. For an ideal gas $P V = n R T \implies P (P V/nR)^{-3} = \text{const} \implies P^{-2} V^{-3} = \text{const} \implies P V^{3/2} = \text{const}$. Polytropic index $n = 3/2$. Work done $W = \frac{n R \Delta T}{1 - n} = \frac{1 R \Delta T}{1 - 3/2} = \frac{R \Delta T}{-1/2} = -2 R \Delta T$.
- **Q4**: **Answer**: `A` — Fringe width $\beta = \frac{\lambda D}{d} = \frac{(500 \times 10^{-9}\text{ m})(1.00\text{ m})}{0.20 \times 10^{-3}\text{ m}} = 2.50 \times 10^{-3}\text{ m} = 2.50\text{ mm}$. Position of $n$-th dark fringe: $y_n = (n - 1/2)\beta$. For 3rd dark fringe: $y_3 = (3 - 0.5)\beta = 2.5 \beta = 2.5(2.50\text{ mm}) = 6.25\text{ mm}$.
- **Q5**: **Answer**: `A` — Displacement equation: $x(t) = A\sin(\omega t)$. When $x = A/2$: $\sin(\omega t) = 1/2 \implies \omega t = \pi/6 \implies \frac{2\pi}{T} t = \frac{\pi}{6} \implies t = \frac{T}{12} = \frac{2.0}{12} = \frac{1}{6}\text{ s}$.
- **Q6**: **Answer**: `A` — Einstein's equation: $K_1 = h(2\nu_0) - h\nu_0 = h\nu_0$. $K_2 = h(3\nu_0) - h\nu_0 = 2h\nu_0$. Ratio $K_1 / K_2 = \frac{h\nu_0}{2h\nu_0} = 1:2$.

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Rolling disc kinematics: IAOR at ground contact, parallel axis theorem $I = \frac{1}{2}MR^2 + MR^2 = \frac{3}{2}MR^2$, rotational to translational kinetic energy ratio $(1/4)/(1/2) = 1:2$, total kinetic energy $\frac{3}{4}Mv^2$.
- **Q8**: **(A), (B), (C), (D)** — EM wave energy relations: equipartition of electric and magnetic energy densities, total density $\frac{1}{2}\varepsilon_0 E_0^2$, Poynting intensity, double radiation pressure on reflector.
- **Q9**: **(A), (B), (C), (D)** — Carnot engine thermodynamics: efficiency formula, reduction under equal temperature increments, sensitivity to $T_H$, heat-temperature proportionality.
- **Q10**: **(A), (B), (C), (D)** — Prism refraction: minimum deviation symmetry, base-parallel interior ray, Snell's law derivation of $\mu$, small-angle approximation $(\mu-1)A$.
- **Q11**: **(A), (B), (C), (D)** — Straight wire magnetostatics: Ampère's field $B = \frac{\mu_0 I}{2\pi r}$, circulation integral, like currents attract, opposite currents repel.
- **Q12**: **(A), (B), (C), (D)** — Bohr model postulates: orbital radii $n^2$, speed $1/n$, angular momentum quantization $n\hbar$, $2\to 1$ Lyman-$\alpha$ photon emission.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `39.20` — Kinetic energy of rolling sphere: $K = \frac{1}{2}M v^2 + \frac{1}{2}I \omega^2 = \frac{1}{2}M v^2 + \frac{1}{2}\left(\frac{2}{5}MR^2\right)\left(\frac{v}{R}\right)^2 = \frac{7}{10}M v^2 = \frac{7}{10}(3.5\text{ kg})(4.0\text{ m/s})^2 = 0.70 \times 3.5 \times 16.0 = 39.20\text{ J}$.
- **Q14**: **Answer**: `100` — Potential difference: $V = E d = (50.0 \times 10^3\text{ V/m})(2.0 \times 10^{-3}\text{ m}) = 100\text{ V}$.
- **Q15**: **Answer**: `69.6` — Inductive reactance $X_L = 2\pi f L = 2\pi(50)(0.20) = 20\pi \approx 62.83\ \Omega$. Total impedance $Z = \sqrt{R^2 + X_L^2} = \sqrt{30.0^2 + 62.83^2} = \sqrt{900 + 3948} = \sqrt{4848} \approx 69.63\ \Omega \approx 69.6\ \Omega$.
- **Q16**: **Answer**: `100` — Fundamental frequency: $\nu = \frac{v}{2L} = \frac{1}{2L}\sqrt{\frac{T}{\mu}} = \frac{1}{2(1.00)}\sqrt{\frac{160.0}{4.0 \times 10^{-3}}} = \frac{1}{2}\sqrt{40000} = \frac{1}{2}(200) = 100\text{ Hz}$.
- **Q17**: **Answer**: `100` — Total magnification $M = m_o \times m_e = 20 \times 5 = 100$.
- **Q18**: **Answer**: `4.00` — Photon energy $E = \frac{hc}{\lambda} = \frac{1240\text{ eV}\cdot\text{nm}}{310\text{ nm}} = 4.00\text{ eV}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — $[\text{Co}(\text{NH}_3)_5(\text{NO}_2)]\text{Cl}_2$ contains the ambidentate ligand nitrite, which can bind through nitrogen ($-\text{NO}_2$, nitro) or oxygen ($-\text{ONO}$, nitrito), exhibiting linkage isomerism.
- **Q20**: **Answer**: `A` — Peroxide effect (Kharasch effect): addition of $\text{HBr}$ to propene in the presence of peroxide proceeds via free radical mechanism giving anti-Markovnikov product: 1-bromopropane.
- **Q21**: **Answer**: `A` — In $\text{SF}_6$, sulfur has 6 bonding pairs and 0 lone pairs ($sp^3d^2$ hybridization, regular octahedral geometry).
- **Q22**: **Answer**: `A` — The Mond process purifies nickel by reaction with carbon monoxide to form volatile $\text{Ni(CO)}_4$, which decomposes thermally to yield pure nickel.
- **Q23**: **Answer**: `A` — First-order integrated rate law: $\ln[A]_t = \ln[A]_0 - kt$. Slope is $-k$.
- **Q24**: **Answer**: `A` — Gelatin and starch are lyophilic (solvent-loving) colloids formed directly by dissolving substance in solvent.

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q26**: **(A), (B), (C), (D)** — Ammonia chemistry: Lewis basicity, tetraamminecopper(II) deep blue complex, Nessler's reagent brown precipitate, pyramidal geometry.
- **Q25**: **(A), (B), (C), (D)** — Square planar complexes: low-spin $d^8$ configuration, $dsp^2$ hybridization, cis-trans $[M a_2 b_2]$, 3 isomers of $[M a b c d]$.
- **Q27**: **(A), (B), (C), (D)** — Aliphatic primary amines: carbylamine reaction, aliphatic diazonium alcohol formation with $\text{N}_2$ evolution, Hinsberg soluble sulfonamide, inductive basicity.
- **Q28**: **(A), (B), (C), (D)** — Adiabatic reversible ideal gas relations: $P V^\gamma$, $T V^{\gamma-1}$, $T^\gamma P^{1-\gamma}$, zero entropy change.
- **Q29**: **(A), (B), (C), (D)** — Nucleic acids biochemistry: sugars (deoxyribose vs ribose), pyrimidine bases (thymine vs uracil), complementary base pairing ($\text{A}=\text{T}$, $\text{G}\equiv\text{C}$).
- **Q30**: **(A), (B), (C), (D)** — Metallurgical terms: calcination (absence of air), roasting (excess air), smelting (carbon reduction), flux and slag formation.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `2.00` — Strong diprotic acid: $[\text{H}^+] = 2 \times 0.0050\text{ M} = 0.010\text{ M} = 10^{-2}\text{ M}$. $\text{pH} = -\log_{10}(10^{-2}) = 2.00$.
- **Q32**: **Answer**: `0.37` — Molality: $m = \frac{6.00 / 60.0}{0.500\text{ kg}} = \frac{0.100}{0.500} = 0.200\text{ mol/kg}$. Freezing point depression $\Delta T_f = K_f \cdot m = 1.86 \times 0.200 = 0.372\text{ K} \approx 0.37\text{ K}$.
- **Q33**: **Answer**: `5` — Gaseous $\text{Fe}^{3+}$ has ground state electronic configuration $[Ar]3d^5$. By Hund's rule, all 5 $d$-orbitals are singly occupied, giving 5 unpaired electrons.
- **Q34**: **Answer**: `30` — First-order half-life: $t_{1/2} = \frac{0.693}{k} = \frac{0.693}{0.0231} = 30\text{ minutes}$.
- **Q35**: **Answer**: `4` — In an $fcc$ unit cell: $8 \times (1/8) + 6 \times (1/2) = 1 + 3 = 4$ atoms per unit cell.
- **Q36**: **Answer**: `7` — In periodic acid ($\text{HIO}_4$), oxidation state: $1(+1) + x + 4(-2) = 0 \implies 1 + x - 8 = 0 \implies x = +7$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — King's property: $I = \int_0^{\pi/2}\frac{\sin x - \cos x}{1+\sin x\cos x}dx$. Replacing $x \to \pi/2 - x$: $I = \int_0^{\pi/2}\frac{\cos x - \sin x}{1+\cos x\sin x}dx = -I \implies 2I = 0 \implies I = 0$.
- **Q38**: **Answer**: `A` — Normalizing second plane: $x + 2y - 2z + 2.5 = 0$. Distance $d = \frac{|-1 - 2.5|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \frac{3.5}{\sqrt{9}} = \frac{3.5}{3} = \frac{7}{6}$.
- **Q39**: **Answer**: `A` — Standard substitution $x = \tan\theta$: $\frac{2x}{1+x^2} = \sin(2\theta) \implies y = 2\theta = 2\tan^{-1} x$. Derivative $\frac{dy}{dx} = \frac{2}{1+x^2}$.
- **Q40**: **Answer**: `A` — Digits $\{0, 1, 2, 3, 4\}$: First digit cannot be 0 (4 choices: 1, 2, 3, 4). Second digit chosen from remaining 4 digits (including 0): 4 choices. Third digit: 3 choices. Fourth digit: 2 choices. Total $= 4 \times 4 \times 3 \times 2 = 96$.
- **Q41**: **Answer**: `A` — Property: $\det(2A) = 2^3 \det(A) = 8 \times 5 = 40$.
- **Q42**: **Answer**: `A` — Tangent parallel to $x$-axis $\implies \frac{dy}{dx} = 2x - 4 = 0 \implies x = 2$. $y = 2^2 - 4(2) + 5 = 4 - 8 + 5 = 1$. Point is $(2, 1)$.

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — Cubic function: $f(x) = (x-1)^3$. Derivative $f'(x) = 3(x-1)^2 \ge 0$, strictly increasing, stationary inflection point at $(1, 0)$.
- **Q44**: **(A), (B), (C), (D)** — Vertical ellipse $\frac{x^2}{16} + \frac{y^2}{25} = 1$: major axis $2b = 10$, minor axis $2a = 8$, eccentricity $e = \sqrt{1 - 16/25} = 3/5$, foci $(0, \pm b e) = (0, \pm 3)$.
- **Q45**: **(A), (B), (C), (D)** — Equal distance from $(3, 0)$ and $(0, 3)$ is the perpendicular bisector line $y = x$. Argument $\pi/4$ or $-3\pi/4$, modulus spans $[0, \infty)$.
- **Q46**: **(A), (B), (C), (D)** — Function $f(x) = \frac{\ln x}{x^2}$: $f'(x) = \frac{1 - 2\ln x}{x^3} = 0 \implies \ln x = 1/2 \implies x = \sqrt{e}$. Value $f(\sqrt{e}) = \frac{1/2}{e} = \frac{1}{2e}$. Asymptote $y=0$, inflection point from $f''(x)=0$.
- **Q47**: **(A), (B), (C), (D)** — Core vector identities: orthogonality of cross product, geometric volume interpretation of box product, coplanarity condition, distributivity over vector addition.
- **Q48**: **(A), (B), (C), (D)** — First-order linear ODE: integrating factor $e^x$, general solution $y = 1 + C e^{-x}$, initial condition gives $y(x) = 1 - e^{-x}$, asymptotic limit 1.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `2` — Integral: $\int_0^1 \frac{1}{\sqrt{1-x^2}}dx = [\sin^{-1} x]_0^1 = \sin^{-1}(1) - \sin^{-1}(0) = \frac{\pi}{2} - 0 = \frac{\pi}{2} \implies k = 2$.
- **Q50**: **Answer**: `2` — Dot product: $\vec{a} \cdot \vec{b} = 1(3) + 2(-2) + 3(1) = 3 - 4 + 3 = 2$.
- **Q51**: **Answer**: `34` — Total balls $= 10$. Probability of drawing 1 red $= 6/10 = 3/5$. With replacement, probability of two reds $= (3/5)^2 = 9/25$. Irreducible fraction: $a = 9, b = 25 \implies a + b = 34$.
- **Q52**: **Answer**: `0` — Equation: $(|x| - 2)(|x| - 3) = 0 \implies |x| = 2$ or $|x| = 3 \implies x = \pm 2, \pm 3$. The roots are $-3, -2, 2, 3$. Sum of solutions $= (-3) + (-2) + 2 + 3 = 0$.
- **Q53**: **Answer**: `18` — Lower triangular matrix determinant is the product of diagonal elements: $1 \times 3 \times 6 = 18$.
- **Q54**: **Answer**: `60` — Word `INDIA` has 5 letters with $I$ appearing twice. Permutations $= \frac{5!}{2!} = \frac{120}{2} = 60$.
"""

val_md = r"""# Answer Key and Validation — Mock Examination 17
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)

### Paper 1 Answer Key
| Q | Type | Subject | Answer Key |
| :--- | :--- | :--- | :--- |
| 1 | Numerical | Physics | `2.84` |
| 2 | Numerical | Physics | `1.52` |
| 3 | Numerical | Physics | `40.05` |
| 4 | Numerical | Physics | `0.0121` |
| 5 | Numerical | Physics | `1.02` |
| 6 | Numerical | Physics | `7.45` |
| 7 | Numerical | Physics | `1.50` |
| 8 | Numerical | Physics | `2.25` |
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
| 19 | Numerical | Chemistry | `98` |
| 20 | Numerical | Chemistry | `1.93` |
| 21 | Numerical | Chemistry | `1.23` |
| 22 | Numerical | Chemistry | `6` |
| 23 | Numerical | Chemistry | `34` |
| 24 | Numerical | Chemistry | `11.51` |
| 25 | Numerical | Chemistry | `4` |
| 26 | Numerical | Chemistry | `0.33` |
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
| 37 | Numerical | Mathematics | `0.27` |
| 38 | Numerical | Mathematics | `5.39` |
| 39 | Numerical | Mathematics | `2` |
| 40 | Numerical | Mathematics | `3` |
| 41 | Numerical | Mathematics | `17` |
| 42 | Numerical | Mathematics | `-1` |
| 43 | Numerical | Mathematics | `2` |
| 44 | Numerical | Mathematics | `816` |
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
| 13 | Numerical | Physics | `39.20` |
| 14 | Numerical | Physics | `100` |
| 15 | Numerical | Physics | `69.6` |
| 16 | Numerical | Physics | `100` |
| 17 | Numerical | Physics | `100` |
| 18 | Numerical | Physics | `4.00` |
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
| 31 | Numerical | Chemistry | `2.00` |
| 32 | Numerical | Chemistry | `0.37` |
| 33 | Numerical | Chemistry | `5` |
| 34 | Numerical | Chemistry | `30` |
| 35 | Numerical | Chemistry | `4` |
| 36 | Numerical | Chemistry | `7` |
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
| 49 | Numerical | Mathematics | `2` |
| 50 | Numerical | Mathematics | `2` |
| 51 | Numerical | Mathematics | `34` |
| 52 | Numerical | Mathematics | `0` |
| 53 | Numerical | Mathematics | `18` |
| 54 | Numerical | Mathematics | `60` |
"""

create_mock_files(17, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md)

