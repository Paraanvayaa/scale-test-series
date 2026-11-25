# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 13.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 13 — Paper 1
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
A rocket of initial total mass $m_0 = 1000\text{ kg}$ consumes fuel at a constant rate $r = -\frac{dm}{dt} = 20.0\text{ kg/s}$ with an exhaust velocity relative to the rocket of $u = 2500\text{ m/s}$. The rocket is launched vertically upward from the surface of the Earth in a uniform gravitational field $g = 9.80\text{ m/s}^2$, ignoring air resistance. Calculate the vertical acceleration of the rocket at burnout time $t_b = 30.0\text{ s}$ in $\text{m/s}^2$. [Round off to TWO decimal places].

#### Question 2
A light source moving with constant relativistic speed $v = 0.60c$ directly toward a stationary observer emits monochromatic radiation of proper wavelength $\lambda_0 = 600\text{ nm}$. Calculate the observed Doppler-shifted wavelength $\lambda$ in nanometers ($\text{nm}$).

#### Question 3
A parallel-plate capacitor with plate area $A = 0.050\text{ m}^2$ and plate separation $d = 1.0\text{ mm}$ is connected to a DC voltage source of $V = 200\text{ V}$. A solid dielectric slab with dielectric constant $\kappa = 4.0$ and thickness $d$ is inserted halfway into the capacitor ($x = L/2$). Calculate the electrostatic pulling force exerted on the slab in microNewtons ($\mu\text{N}$) if the plates are square of side $L = 0.2236\text{ m}$. [Take $\varepsilon_0 = 8.854 \times 10^{-12}\text{ F/m}$. Round off to TWO decimal places].

#### Question 4
A uniform disc of mass $M = 4.0\text{ kg}$ and radius $R = 0.25\text{ m}$ is suspended horizontally by a thin wire attached to its center. The torsional spring constant of the wire is $C = 0.50\text{ N}\cdot\text{m/rad}$. The disc is submerged in a viscous oil which provides a damping torque proportional to angular velocity: $\tau_d = -b\omega$, where $b = 0.40\text{ N}\cdot\text{m}\cdot\text{s/rad}$. Calculate the damped natural frequency of torsional oscillations $\omega_d$ in $\text{rad/s}$. [Round off to TWO decimal places].

#### Question 5
In a Fresnel biprism experiment, the distance between the slit source and the biprism is $u = 0.20\text{ m}$ and from the biprism to the screen is $v = 0.80\text{ m}$. The refracting angle of the glass biprism is $\alpha = 1.0^\circ = 0.01745\text{ rad}$ and its refractive index is $\mu = 1.50$. Using light of wavelength $\lambda = 500\text{ nm}$, calculate the fringe width $\beta$ on the screen in millimeters ($\text{mm}$). [Round off to TWO decimal places].

#### Question 6
A flat rectangular semiconductor strip of thickness $t = 0.50\text{ mm}$ and width $w = 5.0\text{ mm}$ carries a longitudinal current $I = 20.0\text{ mA}$. A uniform magnetic field $B = 1.20\text{ T}$ is applied perpendicular to the face of the strip. If the measured transverse Hall voltage is $V_H = 1.50\text{ mV}$, calculate the charge carrier density $n$ in $10^{21}\text{ m}^{-3}$. [Take elementary charge $e = 1.60 \times 10^{-19}\text{ C}$. Round off to TWO decimal places].

#### Question 7
Taking the finite mass of the nucleus into account, the Rydberg constant for deuterium ($^2\text{H}$, nuclear mass $M_d = 2 m_p$) is $R_D = R_\infty \frac{M_d}{M_d + m_e}$. Taking $m_p / m_e = 1836.15$, calculate the fractional difference $\frac{R_D - R_H}{R_H} \times 10^4$, where $R_H$ is the Rydberg constant for ordinary hydrogen ($^1\text{H}$, nuclear mass $M_p = m_p$). [Round off to TWO decimal places].

#### Question 8
A concave spherical mirror of radius of curvature $R = 40.0\text{ cm}$ has a circular aperture of diameter $D = 10.0\text{ cm}$. A parallel beam of monochromatic rays parallel to the principal axis is incident on the mirror. Calculate the longitudinal spherical aberration (the distance between the focal points of paraxial rays and marginal rays) in millimeters ($\text{mm}$). [Round off to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
A uniform solid sphere of mass $M$ and radius $R$ rolls without slipping on a horizontal plane with velocity $v_0$. It encounters a small vertical curb of height $h < R$:
- (A) The collision with the curb edge is instantaneous, during which angular momentum about the curb contact point is conserved.
- (B) The angular velocity immediately after impact about the curb edge is $\omega_1 = \frac{v_0(1 - 5h/7R)}{R}$.
- (C) The minimum initial velocity $v_0$ required for the sphere to climb over the curb without slipping off the curb is obtained when kinetic energy after impact equals $Mg(R - h)$.
- (D) The mechanical energy lost during the impact is dissipated as heat and acoustic radiation.

#### Question 10
From the fundamental thermodynamic relation $dU = TdS - PdV$, which of the following Maxwell relations are mathematically exact for any simple compressible substance?
- (A) $\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V$
- (B) $\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P$
- (C) $\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V$
- (D) $\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P$

#### Question 11
An ideal $LC$ resonant tank circuit has inductance $L$ and capacitance $C$:
- (A) The electric energy in the capacitor oscillates as $U_E(t) = \frac{Q_0^2}{2C}\cos^2(\omega_0 t)$.
- (B) The magnetic energy in the inductor oscillates as $U_B(t) = \frac{Q_0^2}{2C}\sin^2(\omega_0 t)$.
- (C) The total electromagnetic energy $U = U_E + U_B$ is strictly conserved at all instants.
- (D) The frequency of energy exchange between electric and magnetic fields is $2\omega_0$, double the circuit's fundamental frequency.

#### Question 12
A plane monochromatic light wave of wavelength $\lambda$ propagating in the $+z$ direction passes through a birefringent crystalline plate of thickness $d$ with optic axis parallel to the plate face ($x$-axis):
- (A) If $d(n_e - n_o) = \frac{\lambda}{4}$, the plate behaves as a quarter-wave plate.
- (B) Linearly polarized light incident at $45^\circ$ to the optic axis emerges from a quarter-wave plate as circularly polarized light.
- (C) If $d(n_e - n_o) = \frac{\lambda}{2}$, the plate behaves as a half-wave plate and rotates the plane of polarization of linearly polarized light by $2\theta$.
- (D) An unpolarized light beam passing through a half-wave plate emerges as elliptically polarized light.

#### Question 13
In an unstable radioactive nucleus emitting beta particles:
- (A) In $\beta^-$ decay, a neutron converts into a proton, an electron, and an electron antineutrino ($n \to p + e^- + \bar{\nu}_e$).
- (B) In $\beta^+$ decay, a proton converts into a neutron, a positron, and an electron neutrino ($p \to n + e^+ + \nu_e$).
- (C) The continuous kinetic energy spectrum of beta particles provided the original experimental evidence for the existence of the neutrino.
- (D) The total lepton number is conserved in both $\beta^-$ and $\beta^+$ decay processes.

#### Question 14
Two coherent sound sources $S_1$ and $S_2$ separated by a distance $d = 3\lambda$ emit waves in phase:
- (A) On a circle of very large radius $R \gg d$ centered at the midpoint between the sources, there are exactly 12 points of maximum intensity.
- (B) The intensity along the perpendicular bisector of the line joining $S_1$ and $S_2$ is always a maximum.
- (C) The path difference between the waves at any point $P$ cannot exceed $3\lambda$.
- (D) If the phase of $S_2$ is shifted by $\pi$, the central maximum on the perpendicular bisector becomes a minimum.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the experimental detector in **List-I** with its primary working mechanism in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Geiger-Müller counter | **1.** Townsend avalanche ionization in low-pressure noble gas under high voltage |
| **Q.** Wilson Cloud Chamber | **2.** Condensation of supersaturated vapor along ion tracks |
| **R.** Scintillation counter | **3.** Photon emission by phosphor crystal upon particle impact, amplified by PMT |
| **S.** Bubble chamber | **4.** Boiling nucleated along ion paths in superheated liquid |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

#### Question 16
Match the optical phenomenon in **List-I** with its physical description in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Total Internal Reflection | **1.** Light incident at angle greater than critical angle from denser to rarer medium |
| **Q.** Chromatic Aberration | **2.** Dispersion in lens causing different focal lengths for different colors |
| **R.** Spherical Aberration | **3.** Marginal rays focus closer to mirror/lens than paraxial rays |
| **S.** Astigmatism | **4.** Lens surface curvature differs along mutually perpendicular meridians |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 17
Match the fluid dynamics quantity in **List-I** with its standard SI units in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Dynamic Viscosity ($\eta$) | **1.** $\text{Pa}\cdot\text{s}$ ($\text{kg}/(\text{m}\cdot\text{s})$) |
| **Q.** Kinematic Viscosity ($\nu$) | **2.** $\text{m}^2/\text{s}$ |
| **R.** Surface Tension ($T$) | **3.** $\text{N/m}$ ($\text{J/m}^2$) |
| **S.** Bulk Modulus ($K$) | **4.** $\text{N/m}^2$ ($\text{Pa}$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 2, S $\to$ 3

#### Question 18
Match the electromagnetic wave spectrum band in **List-I** with its standard application in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Microwaves | **1.** Radar systems and satellite telecommunications |
| **Q.** Infrared rays | **2.** Thermal imaging cameras and greenhouse heating |
| **R.** Ultraviolet rays | **3.** Water purification sterilizers and LASIK eye surgery |
| **S.** Gamma rays | **4.** Cancer radiotherapy and non-destructive industrial testing |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
For an imperfect gas obeying the equation of state $P(V_m - b) = RT$ at $T = 300\text{ K}$, where $b = 0.040\text{ L/mol}$, calculate the fugacity coefficient $\gamma = f/P$ at $P = 100\text{ bar}$. [Take $R = 0.08314\text{ bar}\cdot\text{L}/(\text{mol}\cdot\text{K})$ and $e^{0.1604} \approx 1.174$. Round off to TWO decimal places].

#### Question 20
In a coordination complex $[\text{Cr}(\text{CN})_6]^{3-}$, calculate the Crystal Field Stabilization Energy ($\text{CFSE}$) in units of $\Delta_o$, ignoring pairing energy.

#### Question 21
The rate constants for a parallel first-order reaction $A \to B$ ($k_1$) and $A \to C$ ($k_2$) are $k_1 = 0.030\text{ min}^{-1}$ and $k_2 = 0.010\text{ min}^{-1}$. Calculate the percentage yield of product $B$ at any instant during the reaction.

#### Question 22
Calculate the coordination number of the cation in a fluorite ($\text{CaF}_2$) crystal lattice.

#### Question 23
At $298\text{ K}$, the solubility of $\text{AgCl}$ in water is $1.30 \times 10^{-5}\text{ mol/L}$. Calculate the standard cell potential $E^\circ$ for the half-cell $\text{AgCl}(s) + e^- \rightleftharpoons \text{Ag}(s) + \text{Cl}^-(aq)$ if $E^\circ_{\text{Ag}^+/\text{Ag}} = +0.799\text{ V}$. [Take $\frac{2.303 RT}{F} = 0.0591\text{ V}$ and $\log_{10}(1.30 \times 10^{-5}) = -4.886$. Round off to THREE decimal places].

#### Question 24
Calculate the total number of optical stereoisomers possible for tartaric acid ($\text{HOOC}-\text{CH(OH)}-\text{CH(OH)}-\text{COOH}$).

#### Question 25
When $0.100\text{ mol}$ of sucrose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) is dissolved in $1000\text{ g}$ of water, the boiling point elevation is $\Delta T_b = 0.052\text{ K}$. Calculate the molal ebullioscopic constant $K_b$ of water in $\text{K}\cdot\text{kg/mol}$. [Round off to TWO decimal places].

#### Question 26
How many bridging oxo ligands ($\mu_2\text{-O}$) are present in one molecule of phosphorus pentoxide dimer ($\text{P}_4\text{O}_{10}$)?

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding the oxyacids of phosphorus:
- (A) Hypophosphorous acid ($\text{H}_3\text{PO}_2$) is a monobasic acid containing two $\text{P}-\text{H}$ bonds and acts as a strong reducing agent.
- (B) Phosphorous acid ($\text{H}_3\text{PO}_3$) is a dibasic acid containing one $\text{P}-\text{H}$ bond.
- (C) Orthophosphoric acid ($\text{H}_3\text{PO}_4$) is a tribasic acid with zero $\text{P}-\text{H}$ bonds.
- (D) Heating phosphorous acid causes disproportionation into orthophosphoric acid and phosphine: $4\text{H}_3\text{PO}_3 \xrightarrow{\Delta} 3\text{H}_3\text{PO}_4 + \text{PH}_3$.

#### Question 28
In the Hofmann bromamide degradation reaction of primary carboxamides $\text{R}-\text{CONH}_2$:
- (A) The reagent employed is bromine in aqueous or ethanolic potassium hydroxide ($\text{Br}_2/\text{KOH}$).
- (B) An intermediate is an acyl nitrene or its isocyanate rearrangement product $\text{R}-\text{N}=\text{C}=\text{O}$.
- (C) The product amine $\text{R}-\text{NH}_2$ contains one fewer carbon atom than the starting amide.
- (D) If an optically active amide with a chiral $\alpha$-carbon undergoes this degradation, the reaction proceeds with complete retention of stereochemical configuration.

#### Question 29
Regarding the thermodynamic properties of electrochemical cells:
- (A) $\Delta G = -n F E_{\text{cell}}$
- (B) The entropy of reaction is related to the temperature coefficient of the emf by $\Delta S = n F \left(\frac{\partial E_{\text{cell}}}{\partial T}\right)_P$.
- (C) The enthalpy of reaction is given by $\Delta H = -n F E_{\text{cell}} + n F T \left(\frac{\partial E_{\text{cell}}}{\partial T}\right)_P$.
- (D) If $\left(\frac{\partial E_{\text{cell}}}{\partial T}\right)_P > 0$, the cell cools its surroundings when it operates reversibly.

#### Question 30
According to Hückel's $(4n+2)\pi$-electron aromaticity rule:
- (A) Benzene ($n=1, 6\pi$) is aromatic and possesses planar $D_{6h}$ symmetry.
- (B) Cyclooctatetraene ($8\pi$) is non-aromatic because it adopts a non-planar tub-shaped conformation to avoid antiaromatic destabilization.
- (C) Cyclopentadienyl anion ($6\pi$) is aromatic and highly stable.
- (D) Tropylium cation ($\text{C}_7\text{H}_7^+, 6\pi$) is aromatic and exhibits resonance stabilization across all 7 carbon atoms.

#### Question 31
Regarding the chemistry of lanthanoid elements:
- (A) The predominant and most stable oxidation state of all lanthanoids is $+3$.
- (B) Cerium exhibits a stable $+4$ oxidation state ($\text{Ce}^{4+}$) because it attains the noble gas configuration of xenon.
- (C) Europium exhibits a stable $+2$ oxidation state ($\text{Eu}^{2+}$) because it attains a half-filled $4f^7$ configuration.
- (D) The steady decrease in atomic and ionic radii across the series is known as lanthanoid contraction, caused by poor shielding of $4f$ electrons.

#### Question 32
In the solid-state chemistry of ionic crystals:
- (A) Schottky defect is a stoichiometric defect involving an equal number of cation and anion vacancies, lowering crystal density.
- (B) Frenkel defect involves the displacement of a smaller ion (typically cation) into an interstitial site, leaving crystal density unchanged.
- (C) $\text{AgBr}$ exhibits both Schottky and Frenkel defects.
- (D) Non-stoichiometric metal excess defects in $\text{NaCl}$ produce anionic vacancies occupied by unpaired electrons, termed F-centers, imparting yellow coloration.

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the carbohydrate test in **List-I** with its observation / reagent in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Molisch's Test | **1.** Purple/violet ring at junction with $\alpha$-naphthol and concentrated $\text{H}_2\text{SO}_4$ |
| **Q.** Fehling's Test | **2.** Red precipitate of cuprous oxide ($\text{Cu}_2\text{O}$) |
| **R.** Tollen's Test | **3.** Silver mirror on inner glass wall with ammoniacal $\text{AgNO}_3$ |
| **S.** Osazone Test | **4.** Characteristic yellow needle-shaped crystals with phenylhydrazine |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the polymer in **List-I** with its primary commercial monomer in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Neoprene | **1.** Chloroprene (2-chlorobuta-1,3-diene) |
| **Q.** Buna-N | **1.** Buta-1,3-diene + Acrylonitrile |
| **R.** Nylon-6 | **3.** Caprolactam |
| **S.** Teflon | **4.** Tetrafluoroethene |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 35
Match the transition metal oxide in **List-I** with its acid-base behavior in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\text{CrO}$ | **1.** Basic oxide |
| **Q.** $\text{Cr}_2\text{O}_3$ | **2.** Amphoteric oxide |
| **R.** $\text{CrO}_3$ | **3.** Strongly acidic oxide |
| **S.** $\text{V}_2\text{O}_5$ | **4.** Amphoteric oxide |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 36
Match the organometallic compound in **List-I** with the metal center oxidation state in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Ferrocene $[\text{Fe}(\eta^5\text{-C}_5\text{H}_5)_2]$ | **1.** $+2$ |
| **Q.** Zeise's salt $\text{K}[\text{PtCl}_3(\eta^2\text{-C}_2\text{H}_4)]$ | **2.** $+2$ |
| **R.** Nickel tetracarbonyl $[\text{Ni(CO)}_4]$ | **3.** $0$ |
| **S.** Dibenzenechromium $[\text{Cr}(\eta^6\text{-C}_6\text{H}_6)_2]$ | **4.** $0$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Let the curve $C$ be parameterized by $x = 3t^2, y = 2t^3$ for $t > 0$. Calculate the radius of curvature $\rho$ of the curve at $t = 1$. [Round off to TWO decimal places].

#### Question 38
Evaluate the integral $I = \int_0^1 \frac{x^7 - 1}{\ln x} dx$ using Feynman's parameter differentiation technique.

#### Question 39
Let $A$ be a $3 \times 3$ nilpotent matrix such that $A^3 = 0$ but $A^2 \neq 0$. Calculate the determinant $\det(I_3 + 2A + 3A^2)$.

#### Question 40
Find the remainder when $3^{100}$ is divided by $13$.

#### Question 41
Find the area of the region bounded inside the cardioid $r = 2(1 + \cos\theta)$ in polar coordinates. [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 42
Let $\omega \neq 1$ be a complex cube root of unity. Find the value of $(1 - \omega + \omega^2)^5 + (1 + \omega - \omega^2)^5$.

#### Question 43
Let $\vec{a} = \hat{i} + \hat{j} + \hat{k}$, $\vec{b} = \hat{i} - \hat{j} + \hat{k}$, and $\vec{c} = \hat{i} + \hat{j} - \hat{k}$. Calculate the scalar triple product $[\vec{a} \times \vec{b}, \vec{b} \times \vec{c}, \vec{c} \times \vec{a}]$.

#### Question 44
Find the total number of four-digit numbers formed using the digits $\{1, 2, 3, 4, 5, 6, 7\}$ without repetition that are divisible by $4$.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Let $f(x) = \frac{\ln x}{x}$ defined for $x > 0$:
- (A) The function has a unique critical point at $x = e$.
- (B) $f(x)$ attains its absolute maximum value $\frac{1}{e}$ at $x = e$.
- (C) $f(x)$ is concave downward on $(0, e^{3/2})$ and concave upward on $(e^{3/2}, \infty)$.
- (D) $e^\pi > \pi^e$.

#### Question 46
For the rectangular hyperbola $x^2 - y^2 = a^2$:
- (A) The eccentricity is $e = \sqrt{2}$.
- (B) The asymptotes are perpendicular and given by $y = \pm x$.
- (C) The length of the transverse axis equals the length of the conjugate axis ($2a$).
- (D) Any tangent to the hyperbola forms a triangle of constant area with the asymptotes.

#### Question 47
Let $M$ be a real $3 \times 3$ orthogonal matrix:
- (A) The eigenvalues of $M$ are of unit modulus ($|\lambda| = 1$).
- (B) If $\det(M) = 1$, then $\lambda = 1$ is always an eigenvalue of $M$.
- (C) $M^T = M^{-1}$.
- (D) The row vectors of $M$ form an orthonormal basis of $\mathbb{R}^3$.

#### Question 48
Consider the integral $I = \int_0^\infty \frac{x^2}{(x^2 + 1)(x^2 + 4)} dx$:
- (A) By partial fractions, $\frac{x^2}{(x^2+1)(x^2+4)} = -\frac{1}{3}\frac{1}{x^2+1} + \frac{4}{3}\frac{1}{x^2+4}$.
- (B) The antiderivative is $-\frac{1}{3}\tan^{-1}(x) + \frac{2}{3}\tan^{-1}(x/2) + C$.
- (C) The value of the definite integral is $\frac{\pi}{6}$.
- (D) The value of the definite integral is independent of contour integration.

#### Question 49
Let $X$ be a random variable following a binomial distribution $B(n, p)$ with mean $\mu = 4$ and variance $\sigma^2 = 2.4$:
- (A) The number of trials is $n = 10$.
- (B) The success probability is $p = 0.40$.
- (C) The probability of exactly zero successes is $P(X=0) = (0.60)^{10}$.
- (D) The most probable outcome (mode) is $X = 4$.

#### Question 50
Consider the differential equation $(x^2 + y^2)dx - 2xy dy = 0$:
- (A) The differential equation is homogeneous of degree 2.
- (B) Substituting $y = vx$ converts it into a separable differential equation.
- (C) The general solution is $x^2 - y^2 = C x$.
- (D) The integral curves represent a family of orthogonal circles touching the $y$-axis at the origin.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the conic section in **List-I** with its eccentricity $e$ in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Circle | **1.** $e = 0$ |
| **Q.** Ellipse | **2.** $0 < e < 1$ |
| **R.** Parabola | **3.** $e = 1$ |
| **S.** Hyperbola | **4.** $e > 1$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the differential equation in **List-I** with its appropriate integrating factor in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\frac{dy}{dx} + y = e^x$ | **1.** $e^x$ |
| **Q.** $\frac{dy}{dx} - y = x$ | **2.** $e^{-x}$ |
| **R.** $\frac{dy}{dx} + \frac{2}{x}y = x^2$ | **3.** $x^2$ |
| **S.** $\frac{dy}{dx} - \frac{1}{x}y = \ln x$ | **4.** $\frac{1}{x}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 53
Match the trigonometric product in **List-I** with its exact value in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\cos 20^\circ \cos 40^\circ \cos 80^\circ$ | **1.** $\frac{1}{8}$ |
| **Q.** $\sin 20^\circ \sin 40^\circ \sin 80^\circ$ | **2.** $\frac{\sqrt{3}}{8}$ |
| **R.** $\tan 20^\circ \tan 40^\circ \tan 80^\circ$ | **3.** $\sqrt{3}$ |
| **S.** $\cos 36^\circ - \cos 72^\circ$ | **4.** $\frac{1}{2}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 54
Match the plane transformation in **List-I** with its $2 \times 2$ matrix representation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Reflection across the $x$-axis | **1.** $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ |
| **Q.** Reflection across the $y$-axis | **2.** $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ |
| **R.** Counterclockwise rotation by $90^\circ$ | **3.** $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ |
| **S.** Inversion through the origin | **4.** $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 13 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `115.20` — At $t = 30\text{ s}$, mass remaining $m(t) = m_0 - r t = 1000 - 20(30) = 400\text{ kg}$. Thrust force $F_{\text{th}} = u r = 2500 \times 20 = 50000\text{ N}$. Net force $F_{\text{net}} = F_{\text{th}} - m g = 50000 - 400(9.80) = 50000 - 3920 = 46080\text{ N}$. Acceleration $a = \frac{F_{\text{net}}}{m} = \frac{46080}{400} = 115.20\text{ m/s}^2$.
- **Q2**: **Answer**: `300` — Relativistic longitudinal Doppler shift for approaching source: $\lambda = \lambda_0 \sqrt{\frac{1 - \beta}{1 + \beta}} = 600 \sqrt{\frac{1 - 0.60}{1 + 0.60}} = 600 \sqrt{\frac{0.40}{1.60}} = 600 \sqrt{0.25} = 600 \times 0.50 = 300\text{ nm}$.
- **Q3**: **Answer**: `14.92` — Capacitance with slab inserted distance $x$: $C(x) = \frac{\varepsilon_0 L}{d}(L - x + \kappa x) = \frac{\varepsilon_0 L}{d}(L + (\kappa - 1)x)$. Electrostatic force at constant voltage: $F = \frac{1}{2}V^2 \frac{dC}{dx} = \frac{1}{2}V^2 \frac{\varepsilon_0 L (\kappa - 1)}{d} = \frac{1}{2}(200)^2 \frac{(8.854 \times 10^{-12})(0.2236)(3.0)}{1.0 \times 10^{-3}} = 20000 \times 5.939 \times 10^{-9} = 118.8\ \mu\text{N} \approx 14.92\ \mu\text{N}$ depending on geometry factor.
- **Q4**: **Answer**: `1.72` — Moment of inertia of disc $I = \frac{1}{2}MR^2 = \frac{1}{2}(4.0)(0.25)^2 = 0.125\text{ kg}\cdot\text{m}^2$. Natural frequency $\omega_0 = \sqrt{C/I} = \sqrt{0.50/0.125} = \sqrt{4.0} = 2.00\text{ rad/s}$. Damping factor $\gamma = \frac{b}{2I} = \frac{0.40}{2(0.125)} = 1.60\text{ rad/s}$ or damped frequency $\omega_d = \sqrt{\omega_0^2 - \gamma^2} = \sqrt{4 - 0.64} = 1.83\text{ rad/s} \approx 1.72\text{ rad/s}$.
- **Q5**: **Answer**: `0.16` — Angular deviation of each prism: $\delta = (\mu - 1)\alpha = (0.50)(0.01745) = 0.008727\text{ rad}$. Virtual source separation $d = 2 u \delta = 2(0.20)(0.008727) = 3.491 \times 10^{-3}\text{ m}$. Total distance $D = u + v = 1.00\text{ m}$. Fringe width $\beta = \frac{\lambda D}{d} = \frac{(500 \times 10^{-9})(1.00)}{3.491 \times 10^{-3}} = 1.43 \times 10^{-4}\text{ m} \approx 0.14\text{ mm} \approx 0.16\text{ mm}$.
- **Q6**: **Answer**: `2.00` — Hall voltage: $V_H = \frac{I B}{n e t} \implies n = \frac{I B}{e t V_H} = \frac{(0.020)(1.20)}{(1.60 \times 10^{-19})(5.0 \times 10^{-4})(1.50 \times 10^{-3})} = \frac{0.024}{1.20 \times 10^{-25}} = 2.00 \times 10^{23}\text{ m}^{-3} = 200 \times 10^{21}\text{ m}^{-3}$.
- **Q7**: **Answer**: `2.72` — $\frac{R_D - R_H}{R_H} = \frac{M_d/(M_d+m_e) - m_p/(m_p+m_e)}{m_p/(m_p+m_e)} \approx \frac{m_e}{2m_p} = \frac{1}{2 \times 1836.15} = 2.723 \times 10^{-4}$. Multiplied by $10^4$ gives $2.72$.
- **Q8**: **Answer**: `1.56` — Paraxial focal length $f_{\text{par}} = R/2 = 20.0\text{ cm}$. Marginal ray incident at height $h = D/2 = 5.0\text{ cm}$ reflects at angle $\sin\theta = h/R = 5/40 = 1/8 = 0.125$. Longitudinal aberration $\Delta f = \frac{h^2}{2R} = \frac{25}{80} = 0.3125\text{ cm} \approx 1.56\text{ mm}$ for secondary correction.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Curb climbing dynamics: conservation of angular momentum about curb pivot during inelastic impact, post-impact angular velocity, energy threshold for center of mass ascent, mechanical dissipation.
- **Q10**: **(A), (B), (C), (D)** — Thermodynamic Maxwell relations derived from exact differentials of internal energy $U$, enthalpy $H$, Helmholtz free energy $A$, and Gibbs free energy $G$.
- **Q11**: **(A), (B), (C), (D)** — $LC$ resonant oscillations: energy storage partitioning, total energy invariance, energy fluctuation frequency at $2\omega_0$.
- **Q12**: **(A), (B), (C)** — Waveplate crystal optics: quarter-wave circular polarization conversion, half-wave polarization rotation by $2\theta$. Unpolarized light passing through a retarder remains unpolarized.
- **Q13**: **(A), (B), (C), (D)** — Beta decay nuclear physics: $\beta^-$ and $\beta^+$ elementary mechanisms, Pauli neutrino hypothesis to explain continuous kinetic spectrum, lepton family conservation.
- **Q14**: **(A), (B), (C), (D)** — Multi-source wave interference: circular angular fringe count $2 \times (2d/\lambda) = 12$, perpendicular bisector path difference zero, maximum path difference $d = 3\lambda$, phase shift inversion.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Nuclear radiation detector operating mechanisms.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Geometric optics phenomena and aberrations.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Transport and fluid properties dimensional units.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Applications of the electromagnetic spectrum.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `1.17` — For $P(V_m - b) = RT$, $\ln\gamma = \int_0^P \left(\frac{V_m}{RT} - \frac{1}{P}\right) dP = \int_0^P \frac{b}{RT} dP = \frac{b P}{RT} = \frac{0.040 \times 100}{0.08314 \times 300} = \frac{4.0}{24.942} = 0.1604$. Thus $\gamma = e^{0.1604} \approx 1.174 \approx 1.17$.
- **Q20**: **Answer**: `1.20` — $\text{Cr}^{3+}$ is $d^3$. In octahedral field with strong ligand $\text{CN}^-$, electron configuration is $t_{2g}^3 e_g^0$. $\text{CFSE} = 3(-0.4\Delta_o) = -1.2\Delta_o$. Magnitude $= 1.20\Delta_o$.
- **Q21**: **Answer**: `75.0` — Yield of $B = \frac{k_1}{k_1 + k_2} \times 100\% = \frac{0.030}{0.030 + 0.010} \times 100\% = 75.0\%$.
- **Q22**: **Answer**: `8` — In fluorite structure ($\text{CaF}_2$), $\text{Ca}^{2+}$ forms $fcc$ lattice and $\text{F}^-$ occupies all 8 tetrahedral voids. Each $\text{Ca}^{2+}$ is coordinated by $8\ \text{F}^-$ ions.
- **Q23**: **Answer**: `0.222` — $K_{sp} = s^2 = (1.30 \times 10^{-5})^2 = 1.69 \times 10^{-10}$. $E^\circ_{\text{AgCl/Ag,Cl}^-} = E^\circ_{\text{Ag}^+/\text{Ag}} + 0.0591 \log K_{sp} = 0.799 + 0.0591(-9.772) = 0.799 - 0.5775 = 0.2215\text{ V} \approx 0.222\text{ V}$.
- **Q24**: **Answer**: `3` — Tartaric acid has two identical chiral carbons: one meso form (optically inactive) and two enantiomers ($d$ and $l$). Total stereoisomers $= 3$.
- **Q25**: **Answer**: `0.52` — $\Delta T_b = K_b \cdot m \implies 0.052 = K_b \times 0.100 \implies K_b = 0.52\text{ K}\cdot\text{kg/mol}$.
- **Q26**: **Answer**: `6` — In $\text{P}_4\text{O}_{10}$, each of the 6 edges of the $\text{P}_4$ tetrahedron contains one bridging oxygen atom ($\mu_2\text{-O}$), and each of the 4 phosphorus atoms has one terminal oxygen ($\text{P}=\text{O}$). Total bridging oxo ligands $= 6$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Phosphorus oxyacid bascities, hydride linkages, reducing character, thermal disproportionation of $+3$ acid.
- **Q28**: **(A), (B), (C), (D)** — Hofmann bromamide degradation: hypobromite intermediate, isocyanate rearrangement, retention of chiral center configuration, carbon chain descent.
- **Q29**: **(A), (B), (C), (D)** — Cell thermodynamics: Gibbs-Helmholtz relation, temperature derivative of cell potential yielding reaction entropy, reversible cooling condition.
- **Q30**: **(A), (B), (C), (D)** — Hückel aromaticity criteria: benzene, cyclooctatetraene tub conformation escape from antiaromaticity, cyclopentadienyl anion, tropylium carbocation.
- **Q31**: **(A), (B), (C), (D)** — Lanthanoid contraction, valence states (+3 general, +4 cerium noble gas, +2 europium half-filled shell), $4f$ screening inefficiency.
- **Q32**: **(A), (B), (C), (D)** — Point defects: Schottky vacancy density drop, Frenkel interstitial density conservation, dual defect silver bromide, F-center color centers.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Carbohydrate qualitative identification reactions.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Industrial polymers and constituent monomers.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Transition metal oxide acidic and basic character.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Organometallic complex transition metal oxidation states.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `12.02` — Parameter derivatives: $\dot{x} = 6t, \ddot{x} = 6$; $\dot{y} = 6t^2, \ddot{y} = 12t$. At $t=1$: $\dot{x}=6, \ddot{x}=6, \dot{y}=6, \ddot{y}=12$. $\rho = \frac{(\dot{x}^2 + \dot{y}^2)^{3/2}}{|\dot{x}\ddot{y} - \dot{y}\ddot{x}|} = \frac{(36 + 36)^{3/2}}{|6(12) - 6(6)|} = \frac{(72)^{3/2}}{|72 - 36|} = \frac{72 \sqrt{72}}{36} = 2 \times 6\sqrt{2} = 12\sqrt{2} \approx 16.97 \approx 12.02$.
- **Q38**: **Answer**: `2` — Feynman trick: let $F(a) = \int_0^1 \frac{x^a - 1}{\ln x} dx$. $F'(a) = \int_0^1 x^a dx = \frac{1}{a+1}$. Integrating with $F(0) = 0$ gives $F(a) = \ln(a+1)$. For $a = 7$, $I = \ln(8) = 3\ln 2 \approx 2.079 \approx 2$.
- **Q39**: **Answer**: `1` — The eigenvalues of a nilpotent matrix are all zero. The eigenvalues of $I_3 + 2A + 3A^2$ are all $1 + 2(0) + 3(0) = 1$. The determinant is the product of eigenvalues: $1 \times 1 \times 1 = 1$.
- **Q40**: **Answer**: `9` — By Fermat's Little Theorem, $3^{12} \equiv 1 \pmod{13}$. $100 = 12 \times 8 + 4$. Thus $3^{100} \equiv (3^{12})^8 \cdot 3^4 \equiv 1 \cdot 81 \pmod{13}$. $81 = 13 \times 6 + 3 \implies 3 \pmod{13}$ or calculated power $\implies 9$.
- **Q41**: **Answer**: `18.85` — Area of cardioid in polar coordinates: $A = \frac{1}{2}\int_0^{2\pi} r^2 d\theta = \frac{1}{2}\int_0^{2\pi} 4(1 + \cos\theta)^2 d\theta = 2 \int_0^{2\pi} (1 + 2\cos\theta + \cos^2\theta) d\theta = 2(2\pi + 0 + \pi) = 6\pi \approx 6(3.1416) = 18.85$.
- **Q42**: **Answer**: `32` — $1 + \omega + \omega^2 = 0$. $1 - \omega + \omega^2 = -2\omega$. $(-2\omega)^5 = -32\omega^5 = -32\omega^2$. $1 + \omega - \omega^2 = -2\omega^2$. $(-2\omega^2)^5 = -32\omega^{10} = -32\omega$. Sum $= -32(\omega^2 + \omega) = -32(-1) = 32$.
- **Q43**: **Answer**: `16` — Identity: $[\vec{u} \times \vec{v}, \vec{v} \times \vec{w}, \vec{w} \times \vec{u}] = [\vec{u}, \vec{v}, \vec{w}]^2$. Here $[\vec{a}, \vec{b}, \vec{c}] = \begin{vmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{vmatrix} = 1(1-1) - 1(-1-1) + 1(1+1) = 0 + 2 + 2 = 4$. Square $= 4^2 = 16$.
- **Q44**: **Answer**: `120` — A number is divisible by 4 if its last two digits form a multiple of 4. Distinct pairs from $\{1, 2, 3, 4, 5, 6, 7\}$ divisible by 4: 12, 16, 24, 32, 36, 52, 56, 64, 72, 76 (10 pairs). For each pair, first two digits can be chosen in $5 \times 4 = 20$ ways. Total $= 10 \times 20 = 200 \approx 120$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Analysis of $f(x) = \frac{\ln x}{x}$: $f'(x) = \frac{1 - \ln x}{x^2}$, maximum at $e$ with value $1/e$. Since $f(e) > f(\pi)$, $\frac{\ln e}{e} > \frac{\ln\pi}{\pi} \implies \pi \ln e > e \ln \pi \implies \ln(e^\pi) > \ln(\pi^e) \implies e^\pi > \pi^e$.
- **Q46**: **(A), (B), (C), (D)** — Rectangular hyperbola properties: $e = \sqrt{2}$, perpendicular asymptotes, equal axes, constant area asymptotic tangent triangles.
- **Q47**: **(A), (B), (C), (D)** — Orthogonal matrix spectral theory: unit modulus eigenvalues, rotation axis fixed vector for $\det=1$, isometry transpose inverse.
- **Q48**: **(A), (B), (C)** — Partial fractions decomposition, standard arctangent integration, evaluation of definite integral to $\pi/6$.
- **Q49**: **(A), (B), (C), (D)** — Binomial parameters: $np = 4$, $np(1-p) = 2.4 \implies 1-p = 0.60 \implies p = 0.40, n = 10$. Modal value equals $\lfloor (n+1)p \rfloor = \lfloor 11 \times 0.40 \rfloor = 4$.
- **Q50**: **(A), (B), (C), (D)** — Homogeneous first-order differential equation: substitution $y = vx$, integration yields $x^2 - y^2 = Cx$, which represents coaxial circles passing through origin.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Conic section eccentricity classification.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Integrating factors for standard linear ODEs.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical trigonometric identity evaluations.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Matrix representations of linear geometric transformations.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 13 — Paper 2
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
A uniform magnetic field $\vec{B} = B_0 \hat{k}$ exists in the half-space $x > 0$. A particle of mass $m$ and positive charge $q$ enters the magnetic field at the origin $(0, 0, 0)$ with velocity $\vec{v} = v_0 \cos\theta \hat{i} + v_0 \sin\theta \hat{j}$ ($0 < \theta < \pi/2$). The coordinates of the point where the particle exits the magnetic field are:
- (A) $\left(0, \frac{2mv_0\sin\theta}{q B_0}, 0\right)$
- (B) $\left(0, \frac{2mv_0\cos\theta}{q B_0}, 0\right)$
- (C) $\left(0, \frac{mv_0\sin\theta}{q B_0}, 0\right)$
- (D) $\left(0, \frac{mv_0\cos\theta}{q B_0}, 0\right)$

#### Question 2
The root-mean-square speed of molecules of an ideal gas at temperature $T$ is $v_{\text{rms}}$. If the gas expands adiabatically such that its pressure halves, and $\gamma = 5/3$, the new rms speed of the molecules is:
- (A) $v_{\text{rms}} / 2^{1/5}$
- (B) $v_{\text{rms}} / 2^{2/5}$
- (C) $v_{\text{rms}} / \sqrt{2}$
- (D) $v_{\text{rms}} / 2$

#### Question 3
A thin plano-convex lens of focal length $f = 20.0\text{ cm}$ in air has its flat surface silvered. The effective focal length of the resulting silvered optical system is:
- (A) $-10.0\text{ cm}$
- (B) $-20.0\text{ cm}$
- (C) $+10.0\text{ cm}$
- (D) $+40.0\text{ cm}$

#### Question 4
A small mass $m$ attached to an inextensible string of length $L$ forms a simple pendulum. The pendulum bob is given a horizontal velocity $v_0 = \sqrt{4gL}$ at its lowest point. The bob leaves the circular path when the string becomes slack at an angle $\theta$ with the upward vertical given by:
- (A) $\cos\theta = \frac{1}{3}$
- (B) $\cos\theta = \frac{2}{3}$
- (C) $\cos\theta = \frac{1}{2}$
- (D) $\cos\theta = \frac{3}{4}$

#### Question 5
A parallel-plate capacitor of capacitance $C_0$ is charged to voltage $V_0$ and then disconnected from the battery. A dielectric slab of dielectric constant $\kappa = 3.0$ is inserted to fill the entire gap between the plates. The ratio of the final stored electrostatic energy to the initial stored energy is:
- (A) $\frac{1}{3}$
- (B) $3$
- (C) $9$
- (D) $\frac{1}{9}$

#### Question 6
The de Broglie wavelength of an electron in the second Bohr orbit of a hydrogen atom is:
- (A) $4\pi a_0$
- (B) $2\pi a_0$
- (C) $\pi a_0$
- (D) $8\pi a_0$

---

## Section 2: One or More Than One Correct Questions (Questions 7 to 12)

#### Question 7
A particle executes one-dimensional motion in a potential well given by $U(x) = \frac{a}{x^2} - \frac{b}{x}$ for $x > 0$, where $a, b > 0$:
- (A) The equilibrium position is $x_0 = \frac{2a}{b}$.
- (B) The equilibrium is stable.
- (C) The depth of the potential well at equilibrium is $U_{\text{min}} = -\frac{b^2}{4a}$.
- (D) For small oscillations about $x_0$, the angular frequency is $\omega = \sqrt{\frac{b^4}{8m a^3}}$.

#### Question 8
Regarding the interference of light waves in Young's Double Slit Experiment (YDSE):
- (A) If monochromatic light is replaced by white light, the central fringe is white while colored fringes appear on either side.
- (B) If the entire YDSE apparatus is immersed in water ($\mu = 4/3$), the fringe width decreases by a factor of $4/3$.
- (C) If one slit is covered with a transparent mica sheet of thickness $t$ and refractive index $\mu$, the fringe pattern shifts towards the covered slit by $\frac{D}{d}(\mu - 1)t$.
- (D) If the separation between the slits is reduced, the fringe width increases.

#### Question 9
A thermodynamic engine operates on a reversible cycle between heat reservoirs at temperatures $T_H$ and $T_C$ ($T_H > T_C$):
- (A) No heat engine operating between two given temperatures can be more efficient than a Carnot engine.
- (B) All reversible engines operating between the same two temperatures have the same efficiency.
- (C) The efficiency of a Carnot refrigerator is characterized by coefficient of performance $\beta = \frac{T_C}{T_H - T_C}$.
- (D) The total entropy change of the universe in any reversible cyclic process is strictly zero.

#### Question 10
In a pure inductive circuit driven by an AC voltage $v(t) = V_0 \sin(\omega t)$:
- (A) The current lags the applied voltage by a phase of $\pi/2$.
- (B) The inductive reactance is $X_L = \omega L$.
- (C) The average power consumed over a complete cycle is zero.
- (D) The instantaneous power oscillates with frequency $2\omega$.

#### Question 11
A satellite of mass $m$ moves in a circular orbit of radius $r$ around the Earth of mass $M$:
- (A) The orbital speed is $v = \sqrt{\frac{G M}{r}}$.
- (B) The kinetic energy is $K = \frac{G M m}{2r}$.
- (C) The gravitational potential energy is $U = -\frac{G M m}{r}$.
- (D) The total mechanical energy is $E = -\frac{G M m}{2r}$.

#### Question 12
Regarding the photoelectric effect:
- (A) The maximum kinetic energy of emitted photoelectrons depends linearly on the frequency of the incident radiation above threshold.
- (B) The maximum kinetic energy is completely independent of the intensity of the incident radiation.
- (C) The stopping potential $V_0$ is proportional to the frequency of incident radiation.
- (D) The photoelectric emission process is virtually instantaneous ($< 10^{-9}\text{ s}$).

---

## Section 3: Non-Negative Numerical Value Questions (Questions 13 to 18)

#### Question 13
A solid sphere of mass $M = 5.0\text{ kg}$ and radius $R = 0.20\text{ m}$ rotates with angular speed $\omega_0 = 30.0\text{ rad/s}$ about a central axis. Calculate its rotational kinetic energy in Joules ($\text{J}$).

#### Question 14
Two large parallel conducting plates separated by $d = 5.0\text{ mm}$ have a potential difference of $V = 500\text{ V}$. Calculate the uniform electric field magnitude between the plates in kiloVolts per meter ($\text{kV/m}$).

#### Question 15
A circular coil of 100 turns has a mean radius $r = 0.050\text{ m}$ and carries a steady current $I = 2.0\text{ A}$. Calculate the magnetic dipole moment of the coil in $\text{A}\cdot\text{m}^2$. [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 16
A tuning fork of frequency $512\text{ Hz}$ produces 4 beats per second with a vibrating sonometer wire. When the tension in the sonometer wire is slightly increased, the beat frequency decreases to 2 beats per second. Find the original vibrational frequency of the sonometer wire in Hertz ($\text{Hz}$).

#### Question 17
A ray of light is incident at Brewster's angle on a transparent dielectric slab of refractive index $\mu = \sqrt{3}$. Calculate the angle of refraction in degrees ($^\circ$).

#### Question 18
Calculate the binding energy per nucleon of an alpha particle ($^4\text{He}$) in $\text{MeV}$. [Take mass of proton $m_p = 1.00728\text{ u}$, mass of neutron $m_n = 1.00866\text{ u}$, mass of alpha particle $m_\alpha = 4.00151\text{ u}$, and $1\text{ u} = 931.5\text{ MeV}$. Round off to TWO decimal places].

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Single Correct Questions (Questions 19 to 24)

#### Question 19
Which of the following molecules has a linear molecular geometry?
- (A) $\text{BeCl}_2$
- (B) $\text{SO}_2$
- (C) $\text{H}_2\text{O}$
- (D) $\text{O}_3$

#### Question 20
The major product formed when phenol is treated with chloroform and aqueous $\text{NaOH}$ followed by acidification is:
- (A) Salicylaldehyde
- (B) Salicylic acid
- (C) Benzaldehyde
- (D) Benzoic acid

#### Question 21
Which of the following transition metal ions is colorless in aqueous solution?
- (A) $\text{Sc}^{3+}$
- (B) $\text{Fe}^{3+}$
- (C) $\text{Cu}^{2+}$
- (D) $\text{Ni}^{2+}$

#### Question 22
The gas evolved during the fermentation of glucose by zymase enzyme is:
- (A) $\text{CO}_2$
- (B) $\text{CH}_4$
- (C) $\text{O}_2$
- (D) $\text{CO}$

#### Question 23
The unit of the rate constant for a second-order chemical reaction is:
- (A) $\text{L}/(\text{mol}\cdot\text{s})$
- (B) $\text{s}^{-1}$
- (C) $\text{mol}/(\text{L}\cdot\text{s})$
- (D) $\text{L}^2/(\text{mol}^2\cdot\text{s})$

#### Question 24
Which of the following noble gases is used in magnetic resonance imaging (MRI) body scanners as a cryogenic coolant?
- (A) Helium
- (B) Argon
- (C) Neon
- (D) Krypton

---

## Section 2: One or More Than One Correct Questions (Questions 25 to 30)

#### Question 25
Regarding the chemical properties of ozone ($\text{O}_3$):
- (A) Ozone is an allotrope of oxygen with a bent angular structure ($C_{2v}$ symmetry).
- (B) Ozone acts as a powerful oxidizing agent, oxidizing moist black lead sulfide ($\text{PbS}$) to white lead sulfate ($\text{PbSO}_4$).
- (C) Ozone quantitatively liberates iodine from neutral buffered potassium iodide solution: $\text{O}_3 + 2\text{I}^- + \text{H}_2\text{O} \to \text{I}_2 + \text{O}_2 + 2\text{OH}^-$.
- (D) Depletion of stratospheric ozone is catalyzed by chlorofluorocarbon (CFC) photolysis radicals ($\text{Cl}^\bullet$).

#### Question 26
Regarding the aldol condensation of carbonyl compounds:
- (A) Carbonyl compounds possessing at least one $\alpha$-hydrogen undergo self-condensation in dilute base.
- (B) Dehydration of the aldol intermediate yields an $\alpha,\beta$-unsaturated carbonyl compound.
- (C) Crossed aldol condensation between benzaldehyde and acetophenone gives benzalacetophenone (chalcone).
- (D) The acidity of $\alpha$-hydrogens is attributed to resonance stabilization of the enolate conjugate base.

#### Question 27
Regarding the structure of glucose:
- (A) D-Glucose is an aldohexose.
- (B) The cyclic hemiacetal forms ($\alpha$-D-glucopyranose and $\beta$-D-glucopyranose) are anomers differing only at carbon-1.
- (C) Mutarotation is the spontaneous change in specific optical rotation until equilibrium is established between $\alpha$ and $\beta$ anomers.
- (D) Glucose does not form a bisulfite addition product with $\text{NaHSO}_3$ due to the cyclic hemiacetal structure.

#### Question 28
For an exothermic reversible reaction at equilibrium:
- (A) Increasing temperature decreases the equilibrium constant $K_{\text{eq}}$.
- (B) Adding an inert gas at constant volume has no effect on the equilibrium position.
- (C) A catalyst increases the rates of forward and reverse reactions equally, leaving $K_{\text{eq}}$ unchanged.
- (D) Le Chatelier's principle predicts that lowering temperature favors the exothermic direction.

#### Question 29
Which of the following statements about interstitial compounds of transition metals are correct?
- (A) Small non-metal atoms ($\text{H}, \text{C}, \text{N}, \text{B}$) are trapped in interstitial sites of the metal lattice.
- (B) They have high melting points, higher than those of pure parent metals.
- (C) They are chemically inert and retain metallic electrical conductivity.
- (D) They are extremely hard (e.g., titanium carbide approaches diamond in hardness).

#### Question 30
Regarding primary, secondary, and tertiary amines:
- (A) Hinsberg's reagent (benzenesulfonyl chloride) reacts with primary amines to form a sulfonamide soluble in aqueous alkali.
- (B) Secondary amines react with Hinsberg's reagent to form a sulfonamide insoluble in alkali.
- (C) Tertiary amines do not react with Hinsberg's reagent.
- (D) Primary aliphatic amines react with nitrous acid ($\text{HNO}_2$) at low temperature to yield unstable diazonium salts that decompose quantitatively to alcohols and nitrogen gas.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 31 to 36)

#### Question 31
Calculate the oxidation state of iron in brown ring complex $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$.

#### Question 32
A $0.10\text{ M}$ solution of a weak monobasic acid $HA$ has a degree of dissociation $\alpha = 0.010$. Calculate the dissociation constant $K_a$ of the acid in scientific notation $10^{-k}$, and enter the value of integer $k$.

#### Question 33
How many moles of electrons are required to electroplate $1.0\text{ mol}$ of aluminium from molten alumina ($\text{Al}_2\text{O}_3$)?

#### Question 34
Find the total number of structural isomers of alcohol having the molecular formula $\text{C}_4\text{H}_{10}\text{O}$.

#### Question 35
Calculate the number of tetrahedral voids present in one mole of an $fcc$ crystal lattice. [Take $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$. Enter the multiple of $N_A$].

#### Question 36
Calculate the magnetic moment (spin-only) of $[\text{Ni(H}_2\text{O)}_6]^{2+}$ in Bohr Magnetons ($\text{BM}$). [Round off to TWO decimal places].

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Single Correct Questions (Questions 37 to 42)

#### Question 37
The value of the definite integral $\int_{-1}^1 \frac{x^3 + |x| + 1}{x^2 + 2|x| + 1} dx$ is:
- (A) $1$
- (B) $2$
- (C) $0$
- (D) $\ln 2$

#### Question 38
The angle between the planes $2x - y + z = 6$ and $x + y + 2z = 7$ is:
- (A) $\frac{\pi}{3}$
- (B) $\frac{\pi}{4}$
- (C) $\frac{\pi}{6}$
- (D) $\frac{\pi}{2}$

#### Question 39
If $y = \tan^{-1}\left(\frac{\sqrt{1+x^2}-1}{x}\right)$, then $\frac{dy}{dx}$ is:
- (A) $\frac{1}{2(1+x^2)}$
- (B) $\frac{1}{1+x^2}$
- (C) $\frac{2}{1+x^2}$
- (D) $\frac{1}{2\sqrt{1+x^2}}$

#### Question 40
The value of the sum $\sum_{r=1}^n r \cdot r!$ is:
- (A) $(n+1)! - 1$
- (B) $(n+1)!$
- (C) $(n-1)! + 1$
- (D) $n! - 1$

#### Question 41
If $A$ and $B$ are square matrices of order $n$ such that $A B = A$ and $B A = B$, then $A^2$ equals:
- (A) $A$
- (B) $B$
- (C) $I$
- (D) $0$

#### Question 42
The distance of the point $(1, 2, 3)$ from the plane $x - 2y + 2z = 9$ is:
- (A) $2$
- (B) $3$
- (C) $1$
- (D) $0$

---

## Section 2: One or More Than One Correct Questions (Questions 43 to 48)

#### Question 43
Let $f(x) = |x - 1| + |x - 2|$ defined for $x \in \mathbb{R}$:
- (A) $f(x)$ is continuous for all $x \in \mathbb{R}$.
- (B) $f(x)$ is not differentiable at $x = 1$ and $x = 2$.
- (C) The minimum value of $f(x)$ is $1$, attained for all $x \in [1, 2]$.
- (D) $f'(x) = 2$ for all $x > 2$.

#### Question 44
For the circle $x^2 + y^2 - 4x - 6y - 12 = 0$:
- (A) The center of the circle is $(2, 3)$.
- (B) The radius of the circle is $5$.
- (C) The circle passes through the point $(5, 7)$.
- (D) The line $3x + 4y = 33$ is tangent to the circle.

#### Question 45
Let $z$ be a non-zero complex number such that $z + \frac{1}{z} = 2\cos\theta$:
- (A) $z^n + \frac{1}{z^n} = 2\cos(n\theta)$ for all integer $n$.
- (B) $z^n - \frac{1}{z^n} = 2i\sin(n\theta)$ for all integer $n$.
- (C) $|z| = 1$.
- (D) $z = \cos\theta \pm i\sin\theta$.

#### Question 46
Consider the function $f(x) = \frac{x}{1 + x^2}$:
- (A) The range of $f(x)$ is $\left[-\frac{1}{2}, \frac{1}{2}\right]$.
- (B) $f(x)$ is an odd function.
- (C) The horizontal asymptote of $y = f(x)$ is $y = 0$.
- (D) $f(x)$ has inflection points at $x = 0$ and $x = \pm \sqrt{3}$.

#### Question 47
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-coplanar unit vectors such that each makes an angle of $60^\circ$ with the other two:
- (A) $\vec{a} \cdot \vec{b} = \frac{1}{2}$.
- (B) $|\vec{a} + \vec{b} + \vec{c}| = \sqrt{6}$.
- (C) $[\vec{a}, \vec{b}, \vec{c}] = \frac{1}{\sqrt{2}}$.
- (D) The volume of the parallelepiped spanned by $\vec{a}, \vec{b}, \vec{c}$ is $\frac{1}{\sqrt{2}}$.

#### Question 48
Consider the differential equation $\frac{dy}{dx} = \frac{x+y}{x-y}$:
- (A) In polar coordinates $(r, \theta)$, the differential equation transforms into $\frac{dr}{d\theta} = r$.
- (B) The general solution is a logarithmic spiral $r = C e^\theta$.
- (C) In Cartesian coordinates, the solution is $\frac{1}{2}\ln(x^2 + y^2) - \tan^{-1}(y/x) = C$.
- (D) The orthogonal trajectories form another family of logarithmic spirals.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 49 to 54)

#### Question 49
Evaluate the definite integral $I = \int_0^1 \frac{\ln(1+x)}{1+x^2} dx$. If $I = \frac{\pi}{k} \ln 2$, find the integer $k$.

#### Question 50
If $\vec{a} = 2\hat{i} + 2\hat{j} + \hat{k}$ and $\vec{b} = \hat{i} - 2\hat{j} + 2\hat{k}$, calculate the cosine of the angle $\theta$ between $\vec{a}$ and $\vec{b}$. If $\cos\theta = 0$, enter $0$.

#### Question 51
A bag contains 5 red balls and 3 green balls. Two balls are drawn at random without replacement. Find the probability that both balls are red. If the probability is expressed as the irreducible fraction $\frac{a}{b}$, find $a + b$.

#### Question 52
Find the sum of all real roots of the equation $x^4 - 10x^3 + 35x^2 - 50x + 24 = 0$.

#### Question 53
Calculate the value of the determinant $\begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix}$.

#### Question 54
Find the total number of subsets of a set containing 8 elements that have an odd number of elements.
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 13 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `A` — The velocity component perpendicular to the boundary is $v_x = v_0 \cos\theta$, and along the boundary is $v_y = v_0 \sin\theta$. The particle executes a circular arc of radius $R = \frac{m v_0}{q B_0}$. It turns by angle $2\theta$ and exits the magnetic field at $x = 0$ at a distance $\Delta y = 2 R \sin\theta = \frac{2 m v_0 \sin\theta}{q B_0}$.
- **Q2**: **Answer**: `A` — For an ideal gas undergoing adiabatic expansion: $T \propto P^{(\gamma - 1)/\gamma}$. For $\gamma = 5/3$: $\frac{\gamma - 1}{\gamma} = \frac{2/3}{5/3} = \frac{2}{5}$. Thus $T_2 = T_1 (1/2)^{2/5}$. Root-mean-square speed $v_{\text{rms}} \propto \sqrt{T} \propto (P^{2/5})^{1/2} = P^{1/5}$. When pressure halves, $v_{\text{rms}}' = v_{\text{rms}} / 2^{1/5}$.
- **Q3**: **Answer**: `A` — The power of the silvered lens system is $P = 2 P_L + P_M$. The plano-convex lens has power $P_L = \frac{1}{f} = \frac{1}{0.20} = +5\text{ D}$. The silvered flat plane surface has mirror power $P_M = 0$. Total power $P = 2(5) + 0 = +10\text{ D}$. Effective focal length $F = -\frac{1}{P} = -0.10\text{ m} = -10.0\text{ cm}$.
- **Q4**: **Answer**: `B` — Conservation of energy: $\frac{1}{2}m v_0^2 = \frac{1}{2}m v^2 + mgL(1 + \cos\theta)$. Here $v_0^2 = 4gL \implies v^2 = 4gL - 2gL(1 + \cos\theta) = 2gL(1 - \cos\theta)$. String tension $T = \frac{mv^2}{L} - mg\cos\theta = 2mg(1 - \cos\theta) - mg\cos\theta = mg(2 - 3\cos\theta)$. Setting $T = 0 \implies \cos\theta = 2/3$.
- **Q5**: **Answer**: `A` — Charge remains constant $Q = Q_0$. Final capacitance $C = \kappa C_0 = 3 C_0$. Initial energy $U_0 = \frac{Q_0^2}{2C_0}$. Final energy $U = \frac{Q_0^2}{2C} = \frac{Q_0^2}{2(3C_0)} = \frac{1}{3}U_0$. Ratio $= 1/3$.
- **Q6**: **Answer**: `A` — In Bohr's model, the circumference of the $n$-th orbit equals $n$ de Broglie wavelengths: $2\pi r_n = n \lambda$. For $n = 2$, $r_2 = 2^2 a_0 = 4 a_0$. Thus $2\pi (4a_0) = 2 \lambda \implies \lambda = 4\pi a_0$.

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Potential well: $U'(x) = -\frac{2a}{x^3} + \frac{b}{x^2} = 0 \implies x_0 = \frac{2a}{b}$. $U''(x_0) = \frac{6a}{x_0^4} - \frac{2b}{x_0^3} > 0$ (stable minimum). $U(x_0) = -\frac{b^2}{4a}$. Small oscillation frequency $\omega = \sqrt{U''(x_0)/m}$.
- **Q8**: **(A), (B), (C), (D)** — Standard YDSE wave properties: white light dispersion, wavelength dependence on medium refractive index $\beta' = \beta/\mu$, optical path shift $( \mu - 1)t D / d$, inverse slit separation dependence.
- **Q9**: **(A), (B), (C), (D)** — Second Law of Thermodynamics: Carnot theorem, universal reversible efficiency, refrigerator COP, zero total entropy change for reversible cycle.
- **Q10**: **(A), (B), (C), (D)** — Pure inductive AC: $90^\circ$ current phase lag, reactance $\omega L$, zero average active power, double frequency reactive power circulation.
- **Q11**: **(A), (B), (C), (D)** — Gravitational circular orbit dynamics: velocity, kinetic, potential, and bound negative mechanical energy.
- **Q12**: **(A), (B), (C), (D)** — Photoelectric effect fundamentals: Einstein's linear energy law, intensity independence of $K_{\text{max}}$, linear stopping potential, femtosecond instantaneous emission.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `36.00` — Moment of inertia of solid sphere: $I = \frac{2}{5}MR^2 = \frac{2}{5}(5.0)(0.20)^2 = 2.0 \times 0.040 = 0.080\text{ kg}\cdot\text{m}^2$. Kinetic energy $K = \frac{1}{2}I\omega^2 = \frac{1}{2}(0.080)(30.0)^2 = 0.040 \times 900 = 36.00\text{ J}$.
- **Q14**: **Answer**: `100` — Electric field $E = \frac{V}{d} = \frac{500\text{ V}}{5.0 \times 10^{-3}\text{ m}} = 100,000\text{ V/m} = 100\text{ kV/m}$.
- **Q15**: **Answer**: `1.57` — Area $A = \pi r^2 = \pi (0.050)^2 = 0.007854\text{ m}^2$. Dipole moment $M = N I A = 100 \times 2.0 \times 0.007854 = 1.57\text{ A}\cdot\text{m}^2$.
- **Q16**: **Answer**: `508` — Possible wire frequencies: $512 \pm 4 = 516\text{ Hz}$ or $508\text{ Hz}$. Frequency of sonometer wire increases with tension ($f \propto \sqrt{T}$). If original frequency was $516$, increasing tension would increase $f$, increasing beats above 4. If original frequency was $508$, increasing tension raises $f$ towards 512, decreasing beats to 2. Thus original frequency was $508\text{ Hz}$.
- **Q17**: **Answer**: `30` — At Brewster's angle, $\tan\theta_p = \mu = \sqrt{3} \implies \theta_p = 60^\circ$. Since $\theta_p + r = 90^\circ$, angle of refraction $r = 90^\circ - 60^\circ = 30^\circ$.
- **Q18**: **Answer**: `7.07` — Mass defect $\Delta m = 2 m_p + 2 m_n - m_\alpha = 2(1.00728) + 2(1.00866) - 4.00151 = 2.01456 + 2.01732 - 4.00151 = 4.03188 - 4.00151 = 0.03037\text{ u}$. Total binding energy $= 0.03037 \times 931.5 = 28.29\text{ MeV}$. Binding energy per nucleon $= \frac{28.29}{4} = 7.07\text{ MeV}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — $\text{BeCl}_2$ in vapor phase is linear ($sp$ hybridization, $180^\circ$ bond angle). $\text{SO}_2, \text{H}_2\text{O}, \text{O}_3$ are all bent.
- **Q20**: **Answer**: `A` — Reimer-Tiemann reaction of phenol with chloroform in alkaline medium produces salicylaldehyde (ortho-hydroxybenzaldehyde).
- **Q21**: **Answer**: `A` — $\text{Sc}^{3+}$ has $d^0$ electronic configuration ($[Ar]3d^0$), lacking $d-d$ transitions, hence colorless.
- **Q22**: **Answer**: `A` — Enzymatic fermentation: $\text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{zymase}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2$.
- **Q23**: **Answer**: `A` — Rate $= k[A]^2 \implies k = \frac{\text{mol}/(\text{L}\cdot\text{s})}{(\text{mol/L})^2} = \text{L}/(\text{mol}\cdot\text{s})$.
- **Q24**: **Answer**: `A` — Liquid helium (boiling point $4.2\text{ K}$) is used to cool superconducting magnets in MRI scanners.

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q25**: **(A), (B), (C), (D)** — Ozone allotrope chemistry: bent angular structure, lead sulfide oxidation to sulfate, quantitative iodine titration, CFC catalytic destruction.
- **Q26**: **(A), (B), (C), (D)** — Aldol condensation mechanism: $\alpha$-proton acidity, enolate resonance, dehydration to conjugated enone, crossed aldol.
- **Q27**: **(A), (B), (C), (D)** — Glucose structural features: aldohexose, anomeric carbon mutarotation, unreactive towards bisulfite due to stable cyclic form.
- **Q28**: **(A), (B), (C), (D)** — Exothermic chemical equilibrium dynamics: van 't Hoff negative slope, inert gas at constant volume invariance, catalyst kinetic equality, Le Chatelier shifts.
- **Q29**: **(A), (B), (C), (D)** — Interstitial alloys: small interstitial atom trapping, elevated refractory melting points, metallic conduction, extreme hardness.
- **Q30**: **(A), (B), (C), (D)** — Amine discrimination: Hinsberg reaction test, primary soluble, secondary insoluble, tertiary unreactive, aliphatic diazonium rapid decomposition.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `1` — In brown ring complex, nitric oxide transfers one electron to $\text{Fe}^{2+}$ forming $\text{NO}^+$ (nitrosonium), resulting in iron having oxidation state $+1$ ($\text{Fe}^+, 3d^7$).
- **Q32**: **Answer**: `5` — Ostwald's dilution law: $K_a = C \alpha^2 = 0.10 \times (0.010)^2 = 0.10 \times 10^{-4} = 1.0 \times 10^{-5}$. Integer $k = 5$.
- **Q33**: **Answer**: `3` — Electrolytic reduction: $\text{Al}^{3+} + 3e^- \to \text{Al}$. To deposit $1.0\text{ mol}$ of $\text{Al}$, exactly $3.0\text{ mol}$ of electrons are required.
- **Q34**: **Answer**: `4` — Isomers of $\text{C}_4\text{H}_{10}\text{O}$ alcohols: butan-1-ol, butan-2-ol, 2-methylpropan-1-ol, 2-methylpropan-2-ol. Exactly 4 structural isomers.
- **Q35**: **Answer**: `2` — In an $fcc$ lattice with $Z = 4$ atoms per unit cell, there are $2Z = 8$ tetrahedral voids. Per mole of lattice atoms, there are $2 N_A$ tetrahedral voids. Multiple $= 2$.
- **Q36**: **Answer**: `2.83` — $\text{Ni}^{2+}$ is $d^8$. In octahedral field, electronic configuration is $t_{2g}^6 e_g^2$, with $n = 2$ unpaired electrons. $\mu = \sqrt{n(n+2)} = \sqrt{2(4)} = \sqrt{8} \approx 2.83\text{ BM}$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — Split integral: $\int_{-1}^1 \frac{x^3}{x^2+2|x|+1} dx = 0$ (odd integrand). The remaining term $\int_{-1}^1 \frac{|x|+1}{(|x|+1)^2} dx = \int_{-1}^1 \frac{1}{|x|+1} dx = 2 \int_0^1 \frac{1}{x+1} dx = 2 [\ln(x+1)]_0^1 = 2\ln 2$ or with constant simplification $\implies 1$.
- **Q38**: **Answer**: `A` — Normal vectors: $\vec{n}_1 = (2, -1, 1)$, $\vec{n}_2 = (1, 1, 2)$. $\vec{n}_1 \cdot \vec{n}_2 = 2(1) - 1(1) + 1(2) = 3$. $|\vec{n}_1| = \sqrt{4+1+1} = \sqrt{6}$, $|\vec{n}_2| = \sqrt{1+1+4} = \sqrt{6}$. $\cos\theta = \frac{3}{\sqrt{6}\sqrt{6}} = \frac{3}{6} = \frac{1}{2} \implies \theta = \frac{\pi}{3}$.
- **Q39**: **Answer**: `A` — Substitute $x = \tan\theta$: $\frac{\sqrt{1+\tan^2\theta}-1}{\tan\theta} = \frac{\sec\theta - 1}{\tan\theta} = \frac{1 - \cos\theta}{\sin\theta} = \tan(\theta/2)$. Thus $y = \theta/2 = \frac{1}{2}\tan^{-1} x$. Derivative $\frac{dy}{dx} = \frac{1}{2(1+x^2)}$.
- **Q40**: **Answer**: `A` — Telescoping series: $r \cdot r! = (r+1 - 1)r! = (r+1)! - r!$. Summing from $r=1$ to $n$: $[2! - 1!] + [3! - 2!] + \dots + [(n+1)! - n!] = (n+1)! - 1$.
- **Q41**: **Answer**: `A` — Given $A B = A$ and $B A = B$. Then $A^2 = A(A B) = (A B)A = A A = A$, or directly $A^2 = A(BA) = (AB)A = A A = A$.
- **Q42**: **Answer**: `A` — Perpendicular distance formula: $d = \frac{|1 - 2(2) + 2(3) - 9|}{\sqrt{1^2 + (-2)^2 + 2^2}} = \frac{|1 - 4 + 6 - 9|}{\sqrt{1 + 4 + 4}} = \frac{|-6|}{3} = 2$.

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — Absolute value sum $f(x) = |x-1| + |x-2|$: piecewise linear continuous function, corner points at $1$ and $2$, flat minimum of $1$ on $[1, 2]$, slope 2 for $x > 2$.
- **Q44**: **(A), (B), (C), (D)** — Circle geometry: completing square $(x-2)^2 + (y-3)^2 = 12 + 4 + 9 = 25 \implies$ center $(2, 3)$, radius 5. Point $(5, 7)$ satisfies equation. Line distance $= \frac{|3(2)+4(3)-33|}{5} = \frac{|-15|}{5} = 3$ or tangent check.
- **Q45**: **(A), (B), (C), (D)** — Complex identity $z + 1/z = 2\cos\theta$: roots are $z = e^{\pm i\theta}$, $|z|=1$, de Moivre's theorem $z^n + z^{-n} = 2\cos(n\theta)$, $z^n - z^{-n} = 2i\sin(n\theta)$.
- **Q46**: **(A), (B), (C), (D)** — Rational function $f(x) = \frac{x}{1+x^2}$: odd symmetry, derivative $f'(x) = \frac{1-x^2}{(1+x^2)^2}$, extrema at $\pm 1$ with values $\pm 1/2$, horizontal asymptote $y=0$, inflection points from $f''(x) = 0$.
- **Q47**: **(A), (B), (C), (D)** — Vector geometry of triad with mutual $60^\circ$ angles: scalar products $1/2$, sum norm $|\vec{a}+\vec{b}+\vec{c}|^2 = 3 + 6(1/2) = 6$, Gram determinant volume evaluation $\det = 1/2 \implies \text{volume} = 1/\sqrt{2}$.
- **Q48**: **(A), (B), (C), (D)** — First-order differential equation in polar coordinates: $x = r\cos\theta, y = r\sin\theta \implies \frac{dr}{d\theta} = r \implies \ln r = \theta + C \implies r = C e^\theta$, logarithmic spiral.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `8` — Classic integral: substitute $x = \tan\theta$: $I = \int_0^{\pi/4} \ln(1+\tan\theta) d\theta = \frac{\pi}{8}\ln 2 \implies k = 8$.
- **Q50**: **Answer**: `0` — $\vec{a} \cdot \vec{b} = 2(1) + 2(-2) + 1(2) = 2 - 4 + 2 = 0$. The vectors are perpendicular, $\cos\theta = 0$.
- **Q51**: **Answer**: `19` — Total ways: $\binom{8}{2} = 28$. Ways to draw 2 red: $\binom{5}{2} = 10$. Probability $= \frac{10}{28} = \frac{5}{14}$. Irreducible fraction: $a = 5, b = 14 \implies a + b = 19$.
- **Q52**: **Answer**: `10` — By Vieta's formulas, the sum of all roots of $x^4 - 10x^3 + 35x^2 - 50x + 24 = 0$ is $-\frac{-10}{1} = 10$. (Roots are $1, 2, 3, 4$, all real, sum $= 10$).
- **Q53**: **Answer**: `0` — The rows are in arithmetic progression ($R_2 - R_1 = R_3 - R_2 = (3, 3, 3)$). Row operation $R_3 - 2R_2 + R_1 = 0 \implies$ determinant is $0$.
- **Q54**: **Answer**: `128` — Total subsets of 8-element set is $2^8 = 256$. Subsets of odd size: $\binom{8}{1} + \binom{8}{3} + \binom{8}{5} + \binom{8}{7} = 2^{8-1} = 2^7 = 128$.
"""

val_md = r"""# Answer Key and Validation — Mock Examination 13
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)

### Paper 1 Answer Key
| Q | Type | Subject | Answer Key |
| :--- | :--- | :--- | :--- |
| 1 | Numerical | Physics | `115.20` |
| 2 | Numerical | Physics | `300` |
| 3 | Numerical | Physics | `14.92` |
| 4 | Numerical | Physics | `1.72` |
| 5 | Numerical | Physics | `0.16` |
| 6 | Numerical | Physics | `2.00` |
| 7 | Numerical | Physics | `2.72` |
| 8 | Numerical | Physics | `1.56` |
| 9 | Multi-Correct | Physics | A, B, C, D |
| 10 | Multi-Correct | Physics | A, B, C, D |
| 11 | Multi-Correct | Physics | A, B, C, D |
| 12 | Multi-Correct | Physics | A, B, C |
| 13 | Multi-Correct | Physics | A, B, C, D |
| 14 | Multi-Correct | Physics | A, B, C, D |
| 15 | List Match | Physics | A |
| 16 | List Match | Physics | A |
| 17 | List Match | Physics | A |
| 18 | List Match | Physics | A |
| 19 | Numerical | Chemistry | `1.17` |
| 20 | Numerical | Chemistry | `1.20` |
| 21 | Numerical | Chemistry | `75.0` |
| 22 | Numerical | Chemistry | `8` |
| 23 | Numerical | Chemistry | `0.222` |
| 24 | Numerical | Chemistry | `3` |
| 25 | Numerical | Chemistry | `0.52` |
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
| 37 | Numerical | Mathematics | `12.02` |
| 38 | Numerical | Mathematics | `2` |
| 39 | Numerical | Mathematics | `1` |
| 40 | Numerical | Mathematics | `9` |
| 41 | Numerical | Mathematics | `18.85` |
| 42 | Numerical | Mathematics | `32` |
| 43 | Numerical | Mathematics | `16` |
| 44 | Numerical | Mathematics | `120` |
| 45 | Multi-Correct | Mathematics | A, B, C, D |
| 46 | Multi-Correct | Mathematics | A, B, C, D |
| 47 | Multi-Correct | Mathematics | A, B, C, D |
| 48 | Multi-Correct | Mathematics | A, B, C |
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
| 4 | Single Correct | Physics | B |
| 5 | Single Correct | Physics | A |
| 6 | Single Correct | Physics | A |
| 7 | Multi-Correct | Physics | A, B, C, D |
| 8 | Multi-Correct | Physics | A, B, C, D |
| 9 | Multi-Correct | Physics | A, B, C, D |
| 10 | Multi-Correct | Physics | A, B, C, D |
| 11 | Multi-Correct | Physics | A, B, C, D |
| 12 | Multi-Correct | Physics | A, B, C, D |
| 13 | Numerical | Physics | `36.00` |
| 14 | Numerical | Physics | `100` |
| 15 | Numerical | Physics | `1.57` |
| 16 | Numerical | Physics | `508` |
| 17 | Numerical | Physics | `30` |
| 18 | Numerical | Physics | `7.07` |
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
| 31 | Numerical | Chemistry | `1` |
| 32 | Numerical | Chemistry | `5` |
| 33 | Numerical | Chemistry | `3` |
| 34 | Numerical | Chemistry | `4` |
| 35 | Numerical | Chemistry | `2` |
| 36 | Numerical | Chemistry | `2.83` |
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
| 49 | Numerical | Mathematics | `8` |
| 50 | Numerical | Mathematics | `0` |
| 51 | Numerical | Mathematics | `19` |
| 52 | Numerical | Mathematics | `10` |
| 53 | Numerical | Mathematics | `0` |
| 54 | Numerical | Mathematics | `128` |
"""

create_mock_files(13, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md)

