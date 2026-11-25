# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 18.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 18 — Paper 1
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
A siphon of uniform internal cross-sectional area $a = 2.0\text{ cm}^2$ empties water from a large open reservoir. The outlet of the siphon is located at depth $h_1 = 3.00\text{ m}$ below the reservoir surface, and the crest of the siphon is at height $h_2 = 1.50\text{ m}$ above the reservoir surface. Taking atmospheric pressure $P_0 = 1.01 \times 10^5\text{ Pa}$, density $\rho = 1000\text{ kg/m}^3$, and $g = 9.80\text{ m/s}^2$, calculate the initial volume flow rate $Q$ through the siphon in liters per second ($\text{L/s}$). [Round off to TWO decimal places].

#### Question 2
Two long coaxial solenoids have radii $r_1 = 2.0\text{ cm}$ and $r_2 = 4.0\text{ cm}$. The inner solenoid has $n_1 = 500\text{ turns/m}$ and the outer solenoid has $n_2 = 1000\text{ turns/m}$. Calculate the mutual inductance per unit length $M'$ in milliHenries per meter ($\text{mH/m}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ and $\pi^2 \approx 9.87$. Round off to TWO decimal places].

#### Question 3
An ideal Diesel cycle operates with a compression ratio $r = 16.0$ and a cut-off ratio $r_c = 2.0$. For a working diatomic gas with $\gamma = 1.40$, calculate the theoretical thermal efficiency $\eta$ as a percentage (\%). [Take $16^{0.40} \approx 3.031$ and $2^{1.40} \approx 2.639$. Round off to TWO decimal places].

#### Question 4
In a Michelson interferometer illuminated with monochromatic light of wavelength $\lambda = 500\text{ nm}$, when one of the mirrors is displaced by a distance $\Delta d = 0.075\text{ mm}$, calculate the number of interference fringes that cross the field of view.

#### Question 5
A relativistic particle has total energy $E = 10.0\text{ GeV}$ and linear momentum $p = 8.0\text{ GeV}/c$. Calculate its rest mass $m_0 c^2$ in $\text{GeV}$.

#### Question 6
In Kater's reversible physical pendulum, the distances of the two conjugate knife-edges from the center of mass are $h_1 = 0.40\text{ m}$ and $h_2 = 0.60\text{ m}$. If the time period of oscillation about both knife-edges is identical, calculate this time period $T$ in seconds ($\text{s}$). [Take $g = 9.80\text{ m/s}^2$ and $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 7
A Hall effect slice of thickness $t = 0.20\text{ mm}$ carrying a current $I = 1.50\text{ A}$ in a perpendicular magnetic field $B = 0.80\text{ T}$ develops a Hall voltage $V_H = 3.00\text{ mV}$. Calculate the Hall coefficient $R_H$ in $10^{-7}\text{ m}^3/\text{C}$. [Round off to TWO decimal places].

#### Question 8
A non-conducting spherical shell of inner radius $a = 0.10\text{ m}$ and outer radius $b = 0.30\text{ m}$ carries a uniform volume charge density $\rho = 3.0\ \mu\text{C/m}^3$. Calculate the electrostatic potential at the inner surface $r = a$ in kiloVolts ($\text{kV}$). [Take $\varepsilon_0 = 8.854 \times 10^{-12}\text{ F/m}$. Round off to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
A uniform cylinder of mass $M$ and radius $R$ rolling without slipping on a horizontal surface collides elastically with a vertical wall:
- (A) The linear velocity of the center of mass reverses direction immediately after impact ($v' = -v$).
- (B) The angular velocity does not change during the instantaneous smooth impact ($\omega' = \omega$).
- (C) Immediately after collision, the cylinder slips because $v'$ and $\omega'$ are inconsistent with pure rolling.
- (D) Kinetic friction acts forward on the cylinder after impact until pure rolling in the reverse direction is restored.

#### Question 10
From the thermodynamic identity $dG = -S dT + V dP$:
- (A) $\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P$.
- (B) For an ideal gas, $\left(\frac{\partial S}{\partial P}\right)_T = -\frac{n R}{P}$.
- (C) Isothermal compression of an ideal gas decreases its entropy.
- (D) The Gibbs free energy of a pure substance decreases with increasing temperature at constant pressure.

#### Question 11
Two coupled inductors with self-inductances $L_1$ and $L_2$ and mutual inductance $M$:
- (A) The coupling coefficient is defined as $k = \frac{M}{\sqrt{L_1 L_2}}$ ($0 \le k \le 1$).
- (B) When connected in series aiding, the equivalent inductance is $L_{\text{series}} = L_1 + L_2 + 2M$.
- (C) When connected in series opposing, the equivalent inductance is $L_{\text{series}} = L_1 + L_2 - 2M$.
- (D) The maximum possible value of mutual inductance is $M_{\text{max}} = \sqrt{L_1 L_2}$.

#### Question 12
In a Michelson interferometer:
- (A) When the mirrors are mutually perpendicular, circular fringes of equal inclination (Haidinger fringes) are observed.
- (B) When one mirror is slightly tilted, straight localized fringes of equal thickness (Fizeau fringes) are observed.
- (C) Inserting a transparent plate of thickness $t$ and refractive index $\mu$ in one arm shifts the fringe count by $\Delta N = \frac{2(\mu - 1)t}{\lambda}$.
- (D) With white light illumination, only a few colored fringes are visible near zero path difference.

#### Question 13
In an X-ray Coolidge tube:
- (A) Continuous X-rays (bremsstrahlung) are produced by deceleration of high-speed electrons in the Coulomb field of target nuclei.
- (B) The cutoff wavelength is $\lambda_{\text{min}} = \frac{hc}{e V}$, where $V$ is the accelerating voltage.
- (C) Characteristic X-rays are produced when incident electrons eject inner-shell electrons from target atoms.
- (D) Increasing the tube filament current increases the intensity of emitted X-rays without changing $\lambda_{\text{min}}$.

#### Question 14
A planet of mass $m$ moves in an elliptical orbit of semi-major axis $a$ and eccentricity $e$ around the Sun of mass $M$:
- (A) The perihelion distance is $r_p = a(1 - e)$ and aphelion distance is $r_a = a(1 + e)$.
- (B) The orbital speed is maximum at perihelion and minimum at aphelion.
- (C) The total mechanical energy of the planet is $E = -\frac{G M m}{2a}$.
- (D) The angular momentum of the planet about the Sun is strictly conserved throughout the orbit.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the thermometer type in **List-I** with its thermometric property in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Constant-volume gas thermometer | **1.** Pressure of a fixed mass of gas |
| **Q.** Platinum resistance thermometer | **2.** Electrical resistance of a metal wire |
| **R.** Thermocouple thermometer | **3.** Thermoelectric electromotive force (Seebeck effect) |
| **S.** Optical pyrometer | **4.** Spectral radiance / intensity of blackbody radiation |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the wave phenomenon in **List-I** with its characteristic formula in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Doppler effect for sound (source moving towards observer) | **1.** $\nu' = \nu_0 \left(\frac{v}{v - v_s}\right)$ |
| **Q.** Beats frequency | **2.** $\Delta\nu = |\nu_1 - \nu_2|$ |
| **R.** Velocity of sound in gas (Laplace) | **3.** $v = \sqrt{\frac{\gamma P}{\rho}}$ |
| **S.** Velocity of transverse wave on string | **4.** $v = \sqrt{\frac{T}{\mu}}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 17
Match the nuclear entity in **List-I** with its charge and spin properties in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Neutrino ($\nu_e$) | **1.** Charge 0, spin 1/2, nearly massless lepton |
| **Q.** Positron ($e^+$) | **2.** Charge $+e$, spin 1/2, antiparticle of electron |
| **R.** Alpha particle ($^4\text{He}^{2+}$) | **3.** Charge $+2e$, spin 0, composite nucleus |
| **S.** Gamma photon ($\gamma$) | **4.** Charge 0, spin 1, massless gauge boson |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

#### Question 18
Match the circuit type in **List-I** with its primary characteristic in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Series $RLC$ circuit at resonance | **1.** Minimum impedance, maximum current, unity power factor |
| **Q.** Parallel $RLC$ circuit at resonance | **2.** Maximum impedance, minimum line current |
| **R.** Pure capacitive AC circuit | **3.** Current leads voltage by $\pi/2$, zero power dissipation |
| **S.** Pure inductive AC circuit | **4.** Current lags voltage by $\pi/2$, zero power dissipation |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
At $350\text{ K}$, a binary liquid mixture of heptane ($A$, $P_A^\circ = 400.0\text{ Torr}$) and octane ($B$, $P_B^\circ = 150.0\text{ Torr}$) boils under an external pressure of $P_{\text{tot}} = 300.0\text{ Torr}$. Calculate the liquid mole fraction of heptane $x_A$. [Round off to TWO decimal places].

#### Question 20
A substance undergoes parallel first-order reactions $A \xrightarrow{k_1} B$ and $A \xrightarrow{k_2} C$. At $300\text{ K}$, $k_1 = 0.040\text{ s}^{-1}$ and $k_2 = 0.010\text{ s}^{-1}$. Calculate the overall half-life $t_{1/2}$ of reactant $A$ in seconds ($\text{s}$). [Take $\ln 2 = 0.6931$. Round off to TWO decimal places].

#### Question 21
For the lead-acid storage battery during discharge, calculate the standard electromotive force $E^\circ_{\text{cell}}$ in Volts ($\text{V}$). Given standard potentials: $E^\circ_{\text{PbSO}_4/\text{Pb}} = -0.356\text{ V}$ and $E^\circ_{\text{PbO}_2/\text{PbSO}_4} = +1.685\text{ V}$. [Round off to THREE decimal places].

#### Question 22
When $0.010\text{ mol}$ of $\text{CoCl}_3\cdot 5\text{NH}_3$ is treated with excess aqueous silver nitrate ($\text{AgNO}_3$), $0.020\text{ mol}$ of $\text{AgCl}$ precipitates. Calculate the number of chloride ions coordinated directly to the central cobalt ion.

#### Question 23
Potassium chloride ($\text{KCl}$) has a rock-salt structure with density $\rho = 1.984\text{ g/cm}^3$ and molar mass $74.55\text{ g/mol}$. Calculate the unit cell edge length $a$ in picometers ($\text{pm}$). [Take $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$. Round off to the nearest integer].

#### Question 24
Calculate the $\text{pH}$ of a $0.010\text{ M}$ aqueous ammonium acetate ($\text{CH}_3\text{COONH}_4$) solution at $298\text{ K}$. Given $pK_a$ of acetic acid is $4.76$ and $pK_b$ of ammonia is $4.75$. [Round off to TWO decimal places].

#### Question 25
Calculate the total number of structural isomers possible for aromatic amines having the molecular formula $\text{C}_7\text{H}_9\text{N}$.

#### Question 26
Calculate the total number of lone pairs on the central iodine atom in the triiodide anion ($\text{I}_3^-$).

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding carbocation rearrangements in organic synthesis:
- (A) Wagner-Meerwein rearrangements involve 1,2-hydride or 1,2-alkyl shifts to generate a more stable carbocation.
- (B) Tertiary carbocations are more stable than secondary carbocations due to hyperconjugation and inductive effects.
- (C) Pinacol rearrangement involves a 1,2-shift driven by the superior stability of an oxocarbenium ion intermediate.
- (D) Ring expansion from a 4-membered or 5-membered ring to a 5-membered or 6-membered ring occurs readily to relieve angle strain.

#### Question 28
In the metallurgy and extraction of silver:
- (A) Silver is extracted from argentite ore ($\text{Ag}_2\text{S}$) by Mac-Arthur Forrest cyanide leaching.
- (B) In the presence of air, silver sulfide dissolves to form sodium dicyanoargentate(I): $\text{Ag}_2\text{S} + 4\text{NaCN} + \text{H}_2\text{O} + \frac{1}{2}\text{O}_2 \rightleftharpoons 2\text{Na}[\text{Ag(CN)}_2] + \text{Na}_2\text{SO}_4$.
- (C) Metallic silver is precipitated by displacement with zinc dust: $2[\text{Ag(CN)}_2]^- + \text{Zn} \to [\text{Zn(CN)}_4]^{2-} + 2\text{Ag}$.
- (D) Crude silver is refined by electrolytic refining using an acidified silver nitrate electrolyte.

#### Question 29
Regarding the chemistry of xenon oxyfluorides:
- (A) $\text{XeOF}_4$ has a square pyramidal geometry with one axial lone pair ($sp^3d^2$ hybridization).
- (B) $\text{XeO}_2\text{F}_2$ has a see-saw geometry with one equatorial lone pair ($sp^3d$ hybridization).
- (C) $\text{XeO}_3$ has a trigonal pyramidal geometry with one lone pair ($sp^3$ hybridization).
- (D) Complete hydrolysis of $\text{XeF}_6$ yields xenon trioxide ($\text{XeO}_3$) and hydrofluoric acid ($\text{HF}$).

#### Question 30
According to the Hardy-Schulze rule for the coagulation of colloidal solutions:
- (A) Coagulation is brought about by ions carrying charge opposite to that of the colloidal particles.
- (B) The coagulating power of an ion increases markedly with increasing valency of the active ion.
- (C) For a positively charged ferric hydroxide sol, the coagulating power order is $[\text{Fe(CN)}_6]^{4-} > \text{PO}_4^{3-} > \text{SO}_4^{2-} > \text{Cl}^-$.
- (D) For a negatively charged $\text{As}_2\text{S}_3$ sol, the coagulating power order is $\text{Al}^{3+} > \text{Ba}^{2+} > \text{Na}^+$.

#### Question 31
Regarding the transition metal oxoanions chromate ($\text{CrO}_4^{2-}$) and dichromate ($\text{Cr}_2\text{O}_7^{2-}$):
- (A) In aqueous solution, chromate and dichromate exist in a $\text{pH}$-dependent equilibrium: $2\text{CrO}_4^{2-} + 2\text{H}^+ \rightleftharpoons \text{Cr}_2\text{O}_7^{2-} + \text{H}_2\text{O}$.
- (B) Chromate is yellow and predominates in alkaline medium ($\text{pH} > 7$).
- (C) Dichromate is orange and predominates in acidic medium ($\text{pH} < 7$).
- (D) The oxidation state of chromium is $+6$ in both chromate and dichromate ions.

#### Question 32
Regarding the structure and bonding in solid carbon allotropes:
- (A) Diamond has a three-dimensional covalent network of $sp^3$ hybridized carbon atoms, making it an electrical insulator.
- (B) Graphite has two-dimensional planar hexagonal layers of $sp^2$ hybridized carbon atoms, acting as an electrical conductor along the planes.
- (C) The interlayer distance in graphite ($335\text{ pm}$) is held by weak van der Waals forces.
- (D) Fullerenes ($\text{C}_{60}$) are discrete molecular allotropes soluble in organic solvents such as toluene.

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the organic reagent in **List-I** with its specific synthetic function in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Lithium aluminium hydride ($\text{LiAlH}_4$) | **1.** Strong reducing agent; reduces acids, esters, amides to alcohols/amines |
| **Q.** Sodium borohydride ($\text{NaBH}_4$) | **2.** Mild reducing agent; reduces aldehydes and ketones to alcohols |
| **R.** Pyridinium chlorochromate ($\text{PCC}$) | **3.** Selective oxidant; oxidizes primary alcohols to aldehydes |
| **S.** Jones reagent ($\text{CrO}_3 / \text{H}_2\text{SO}_4$) | **4.** Strong oxidant; oxidizes primary alcohols to carboxylic acids |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the metal in **List-I** with its principal mineral source in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Iron | **1.** Magnetite ($\text{Fe}_3\text{O}_4$) |
| **Q.** Aluminium | **2.** Cryolite ($\text{Na}_3\text{AlF}_6$) |
| **R.** Copper | **3.** Malachite ($\text{CuCO}_3\cdot\text{Cu(OH)}_2$) |
| **S.** Zinc | **4.** Calamine ($\text{ZnCO}_3$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 35
Match the coordination complex in **List-I** with its color in aqueous solution in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $[\text{Cu(H}_2\text{O)}_6]^{2+}$ | **1.** Light blue |
| **Q.** $[\text{Ni(H}_2\text{O)}_6]^{2+}$ | **2.** Green |
| **R.** $[\text{Co(H}_2\text{O)}_6]^{2+}$ | **3.** Pink |
| **S.** $[\text{Fe(H}_2\text{O)}_6]^{3+}$ | **4.** Pale violet / Yellowish-brown |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 36
Match the chemical term in **List-I** with its defining equation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Raoult's Law | **1.** $P_i = x_i P_i^\circ$ |
| **Q.** Henry's Law | **2.** $P = K_H x$ |
| **R.** Van 't Hoff Osmotic Law | **3.** $\Pi = C R T$ |
| **S.** Nernst Equation | **4.** $E = E^\circ - \frac{RT}{nF}\ln Q$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Calculate the total area enclosed by the loop of the Folium of Descartes $x^3 + y^3 = 3axy$ for $a = 2.00$.

#### Question 38
Find the radius of the circle formed by the intersection of the sphere $x^2 + y^2 + z^2 = 25$ and the plane $2x + 2y + z = 9$.

#### Question 39
Find the number of common tangents to the circle $x^2 + y^2 = 4$ and the circle $x^2 + y^2 - 6x - 8y + 24 = 0$.

#### Question 40
Let $A$ be a $3 \times 3$ real matrix such that $A^2 = A$ and $\det(A) = 0$. If $\text{Tr}(A) = 2$, calculate the value of $\det(I_3 + A)$.

#### Question 41
Three distinct numbers are selected at random from the set $\{1, 2, 3, \dots, 20\}$. Find the probability that the three selected numbers are in arithmetic progression. If the probability is expressed as the irreducible fraction $\frac{a}{b}$, find $a + b$.

#### Question 42
Let $\omega$ be a complex non-real cube root of unity. Find the value of $(1 - \omega + \omega^2)(1 + \omega - \omega^2)$.

#### Question 43
Let $\vec{a} = 2\hat{i} - \hat{j} + \hat{k}$ and $\vec{b} = \hat{i} + 2\hat{j} - \hat{k}$. Find the unit vector perpendicular to both $\vec{a}$ and $\vec{b}$. If the magnitude of the cross product is $|\vec{a} \times \vec{b}|$, calculate $|\vec{a} \times \vec{b}|^2$.

#### Question 44
Find the total number of non-negative integer solutions to $x_1 + x_2 + x_3 + x_4 = 12$.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Let $f(x) = \sin x + \cos x$ defined for $x \in [0, 2\pi]$:
- (A) The maximum value of $f(x)$ is $\sqrt{2}$, attained at $x = \frac{\pi}{4}$.
- (B) The minimum value of $f(x)$ is $-\sqrt{2}$, attained at $x = \frac{5\pi}{4}$.
- (C) $f(x)$ is strictly increasing on $\left[0, \frac{\pi}{4}\right]$.
- (D) $f'(x) = 0$ at $x = \frac{\pi}{4}$ and $x = \frac{5\pi}{4}$.

#### Question 46
For the rectangular hyperbola $x y = 16$:
- (A) The eccentricity is $e = \sqrt{2}$.
- (B) The asymptotes are the coordinate axes ($x = 0$ and $y = 0$).
- (C) The length of the transverse axis is $8\sqrt{2}$.
- (D) The vertices are $(4, 4)$ and $(-4, -4)$.

#### Question 47
Let $A$ be an $n \times n$ real matrix:
- (A) $\det(A^T) = \det(A)$.
- (B) If $A$ is orthogonal, then $A^{-1} = A^T$.
- (C) If $A$ is invertible, then $(A^{-1})^T = (A^T)^{-1}$.
- (D) $\text{Tr}(A B) = \text{Tr}(B A)$ for any $n \times n$ matrix $B$.

#### Question 48
Consider the improper integral $I = \int_0^\infty e^{-x^2} dx$:
- (A) $I = \frac{\sqrt{\pi}}{2}$ (Gaussian integral).
- (B) $\int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}$.
- (C) $\int_0^\infty x e^{-x^2} dx = \frac{1}{2}$.
- (D) $\int_0^\infty x^2 e^{-x^2} dx = \frac{\sqrt{\pi}}{4}$.

#### Question 49
Let $X$ be a continuous random variable uniformly distributed on the interval $[0, 4]$:
- (A) The probability density function is $f(x) = \frac{1}{4}$ for $x \in [0, 4]$.
- (B) The mean of $X$ is $\mu = 2$.
- (C) The variance of $X$ is $\sigma^2 = \frac{4}{3}$.
- (D) $P(1 \le X \le 3) = \frac{1}{2}$.

#### Question 50
Consider the differential equation $\frac{dy}{dx} = \frac{y - x}{y + x}$:
- (A) It is a homogeneous differential equation of degree 0.
- (B) Substituting $y = vx$ converts it into a separable equation.
- (C) In polar coordinates, it represents a logarithmic spiral.
- (D) The solution curves intersect the lines $y = \pm x$ at constant angles.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the function in **List-I** with its Maclaurin series expansion in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\cos x$ | **1.** $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$ |
| **Q.** $\sinh x$ | **2.** $x + \frac{x^3}{3!} + \frac{x^5}{5!} + \dots$ |
| **R.** $\cosh x$ | **3.** $1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \dots$ |
| **S.** $\frac{1}{1 - x}$ | **4.** $1 + x + x^2 + x^3 + \dots$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the matrix classification in **List-I** with its determinant property in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Invertible matrix | **1.** $\det(A) \neq 0$ |
| **Q.** Singular matrix | **2.** $\det(A) = 0$ |
| **R.** Orthogonal matrix | **3.** $\det(A) = \pm 1$ |
| **S.** $3 \times 3$ skew-symmetric matrix | **4.** $\det(A) = 0$ identically |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 53
Match the conic section in **List-I** with its standard focus-directrix definition in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Parabola | **1.** Locus of points equidistant from focus and directrix ($e = 1$) |
| **Q.** Ellipse | **2.** Locus of points with ratio of distances to focus and directrix $e < 1$ |
| **R.** Hyperbola | **3.** Locus of points with ratio of distances to focus and directrix $e > 1$ |
| **S.** Circle | **4.** Limiting case with directrix at infinity ($e = 0$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 54
Match the plane vector configuration in **List-I** with its analytical condition in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\vec{u} \perp \vec{v}$ | **1.** $\vec{u} \cdot \vec{v} = 0$ |
| **Q.** $\vec{u} \parallel \vec{v}$ | **2.** $\vec{u} \times \vec{v} = \vec{0}$ |
| **R.** $|\vec{u}| = |\vec{v}|$ | **3.** $(\vec{u} + \vec{v}) \cdot (\vec{u} - \vec{v}) = 0$ |
| **S.** Bisector of angle between unit vectors $\hat{u}$ and $\hat{v}$ | **4.** Directed along $\hat{u} + \hat{v}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 18 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `1.53` — Torricelli's speed of discharge at outlet: $v = \sqrt{2 g h_1} = \sqrt{2(9.80)(3.00)} = \sqrt{58.80} \approx 7.668\text{ m/s}$. Volume flow rate $Q = a v = (2.0 \times 10^{-4}\text{ m}^2)(7.668\text{ m/s}) = 1.534 \times 10^{-3}\text{ m}^3/\text{s} = 1.53\text{ L/s}$.
- **Q2**: **Answer**: `0.79` — Mutual inductance per unit length: $M' = \mu_0 n_1 n_2 (\pi r_1^2) = (4\pi \times 10^{-7})(500)(1000)(\pi (0.020)^2) = 4\pi^2 \times 10^{-7} \times 500000 \times 4.0 \times 10^{-4} = 4(9.87) \times 10^{-7} \times 200 = 39.48 \times 200 \times 10^{-7} = 7.896 \times 10^{-4}\text{ H/m} = 0.79\text{ mH/m}$.
- **Q3**: **Answer**: `61.38` — Diesel cycle efficiency: $\eta = 1 - \frac{1}{r^{\gamma - 1}}\left[\frac{r_c^\gamma - 1}{\gamma(r_c - 1)}\right] = 1 - \frac{1}{16^{0.40}}\left[\frac{2^{1.40} - 1}{1.40(2 - 1)}\right] = 1 - \frac{1}{3.031}\left[\frac{2.639 - 1}{1.40}\right] = 1 - \frac{1}{3.031}\left[\frac{1.639}{1.40}\right] = 1 - \frac{1.1707}{3.031} = 1 - 0.3862 = 0.6138 = 61.38\%$.
- **Q4**: **Answer**: `300` — Fringe shift in Michelson interferometer: $2\Delta d = N \lambda \implies N = \frac{2\Delta d}{\lambda} = \frac{2(0.075 \times 10^{-3}\text{ m})}{500 \times 10^{-9}\text{ m}} = \frac{1.50 \times 10^{-4}}{5.00 \times 10^{-7}} = 300$.
- **Q5**: **Answer**: `6.00` — Relativistic energy-momentum relation: $E^2 = p^2 c^2 + m_0^2 c^4 \implies m_0 c^2 = \sqrt{E^2 - p^2 c^2} = \sqrt{10.0^2 - 8.0^2} = \sqrt{100 - 64} = \sqrt{36} = 6.00\text{ GeV}$.
- **Q6**: **Answer**: `2.01` — For Kater's pendulum with equal periods about knife edges separated by $L = h_1 + h_2 = 0.40 + 0.60 = 1.00\text{ m}$, the time period equals that of an equivalent simple pendulum of length $L$: $T = 2\pi\sqrt{\frac{L}{g}} = 2\pi\sqrt{\frac{1.00}{9.80}} = 2\pi(0.3194) = 2.007\text{ s} \approx 2.01\text{ s}$.
- **Q7**: **Answer**: `5.00` — Hall coefficient: $R_H = \frac{V_H t}{I B} = \frac{(3.00 \times 10^{-3}\text{ V})(0.20 \times 10^{-3}\text{ m})}{(1.50\text{ A})(0.80\text{ T})} = \frac{6.00 \times 10^{-7}}{1.20} = 5.00 \times 10^{-7}\text{ m}^3/\text{C}$.
- **Q8**: **Answer**: `13.55` — Electrostatic potential at inner surface $r = a$: $V(a) = \int_a^b \frac{\rho(r'^3 - a^3)}{3\varepsilon_0 r'^2}dr' + \frac{Q_{\text{tot}}}{4\pi\varepsilon_0 b} = \frac{\rho}{2\varepsilon_0}(b^2 - a^2) = \frac{(3.0 \times 10^{-6})(0.09 - 0.01)}{2(8.854 \times 10^{-12})} = \frac{3.0 \times 10^{-6} \times 0.08}{1.771 \times 10^{-11}} = 13550\text{ V} = 13.55\text{ kV}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Rolling collision with wall: impulse reverses linear velocity while preserving angular velocity, instantaneous slip with forward kinetic friction accelerating rotation until reverse rolling is restored.
- **Q10**: **(A), (B), (C), (D)** — Maxwell relation from Gibbs free energy: $(\partial S/\partial P)_T = -(\partial V/\partial T)_P$, ideal gas evaluation $-nR/P$, isothermal entropy decrease under compression.
- **Q11**: **(A), (B), (C), (D)** — Coupled inductor circuits: coupling coefficient $k$, series aiding $L_1+L_2+2M$, series opposing $L_1+L_2-2M$, theoretical upper bound $M \le \sqrt{L_1 L_2}$.
- **Q12**: **(A), (B), (C), (D)** — Michelson interferometer fringe geometries: circular Haidinger fringes for perpendicular mirrors, straight Fizeau fringes for tilted mirrors, path difference shift $2(\mu-1)t$, white light zero-order coherence.
- **Q13**: **(A), (B), (C), (D)** — X-ray tube physics: Bremsstrahlung continuous radiation, Duane-Hunt cutoff wavelength, characteristic shell transitions, filament current controlling flux.
- **Q14**: **(A), (B), (C), (D)** — Keplerian orbital mechanics: apsidal distances $a(1\pm e)$, orbital velocity variation, bound negative total energy $-GMm/(2a)$, central force angular momentum conservation.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Thermometer classifications and thermometric properties.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Acoustic wave propagation formulas.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fundamental nuclear particles charge and spin.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — AC resonant and reactive circuit impedance behaviors.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `0.60` — Raoult's law for total pressure: $P_{\text{tot}} = x_A P_A^\circ + (1 - x_A)P_B^\circ \implies 300.0 = 400.0 x_A + 150.0(1 - x_A) = 150.0 + 250.0 x_A \implies 250.0 x_A = 150.0 \implies x_A = \frac{150.0}{250.0} = 0.60$.
- **Q20**: **Answer**: `13.86` — Total effective rate constant for parallel first-order decay: $k_{\text{eff}} = k_1 + k_2 = 0.040 + 0.010 = 0.050\text{ s}^{-1}$. Half-life $t_{1/2} = \frac{\ln 2}{k_{\text{eff}}} = \frac{0.6931}{0.050} = 13.86\text{ s}$.
- **Q21**: **Answer**: `2.041` — Standard cell potential: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = 1.685 - (-0.356) = 2.041\text{ V}$.
- **Q22**: **Answer**: `1` — Total moles of chloride per mole of complex is 3. Since $0.010\text{ mol}$ of complex gives $0.020\text{ mol}$ of $\text{AgCl}$, exactly 2 chloride ions are in the outer ionization sphere. The remaining 1 chloride ion is coordinated inside the coordination sphere: $[\text{Co}(\text{NH}_3)_5\text{Cl}]\text{Cl}_2$.
- **Q23**: **Answer**: `628` — In rock salt structure, $Z = 4$. $a^3 = \frac{Z \cdot M}{N_A \cdot \rho} = \frac{4 \times 74.55}{(6.022 \times 10^{23})(1.984)} = \frac{298.2}{1.1948 \times 10^{24}} = 2.496 \times 10^{-22}\text{ cm}^3$. $a = (2.496 \times 10^{-22})^{1/3} = 6.296 \times 10^{-8}\text{ cm} \approx 628\text{ pm}$.
- **Q24**: **Answer**: `7.00` — Salt of weak acid and weak base: $\text{pH} = 7 + \frac{1}{2}(pK_a - pK_b) = 7 + \frac{1}{2}(4.76 - 4.75) = 7 + \frac{1}{2}(0.01) = 7.005 \approx 7.00$.
- **Q25**: **Answer**: `5` — Aromatic amines of $\text{C}_7\text{H}_9\text{N}$: o-toluidine, m-toluidine, p-toluidine ($1^\circ$ aryl), benzylamine ($1^\circ$ alkyl), N-methylaniline ($2^\circ$ amine). Total structural isomers $= 5$.
- **Q26**: **Answer**: `3` — In $\text{I}_3^-$, the central iodine atom is bonded to two terminal iodine atoms and carries 3 lone pairs in equatorial positions ($sp^3d$ hybridization, linear geometry).

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Carbocation rearrangements: 1,2-hydride/alkyl shifts, hyperconjugative stability ordering, pinacol oxocarbenium driving force, strain-relief ring expansions.
- **Q28**: **(A), (B), (C), (D)** — Silver extraction metallurgy: oxidative cyanide leaching of argentite, zinc dust cementation, electrolytic purification.
- **Q29**: **(A), (B), (C), (D)** — Xenon oxyfluoride structures: square pyramidal $\text{XeOF}_4$, see-saw $\text{XeO}_2\text{F}_2$, pyramidal $\text{XeO}_3$, complete hydrolysis of $\text{XeF}_6$.
- **Q30**: **(A), (B), (C), (D)** — Hardy-Schulze rule: opposite charge precipitation, coagulating power scaling with valency, coagulating orders for ferric hydroxide and arsenic sulfide sols.
- **Q31**: **(A), (B), (C), (D)** — Chromate-dichromate equilibrium: pH-dependent interconversion, yellow chromate in base, orange dichromate in acid, invariant $+6$ oxidation state.
- **Q32**: **(A), (B), (C), (D)** — Solid carbon allotropes: 3D covalent diamond insulator, 2D graphene-layered graphite conductor, weak van der Waals gap, molecular $\text{C}_{60}$.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Selective organic reducing and oxidizing reagents.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Principal mineral ores of industrial metals.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Characteristic aqueous coordination complex colors.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Defining equations of fundamental chemical laws.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `6.00` — Area of loop of Folium of Descartes $x^3 + y^3 = 3axy$: $A = \frac{3a^2}{2}$. For $a = 2.00$: $A = \frac{3(4.00)}{2} = 6.00$.
- **Q38**: **Answer**: `4` — Center of sphere $(0, 0, 0)$, radius $R = 5$. Distance from center to plane: $d = \frac{|0 + 0 + 0 - 9|}{\sqrt{2^2 + 2^2 + 1^2}} = \frac{9}{\sqrt{4 + 4 + 1}} = \frac{9}{3} = 3$. Radius of circle of intersection $r = \sqrt{R^2 - d^2} = \sqrt{25 - 9} = \sqrt{16} = 4$.
- **Q39**: **Answer**: `3` — Circle 1: center $C_1(0, 0)$, radius $r_1 = 2$. Circle 2: $(x-3)^2 + (y-4)^2 = 9+16-24 = 1 \implies$ center $C_2(3, 4)$, radius $r_2 = 1$. Distance between centers $d = \sqrt{3^2 + 4^2} = 5$. Since $d = r_1 + r_2 + 2 = 5 > r_1 + r_2 = 3$, the circles are separate with 4 tangents, but for touching $d = r_1 + r_2 \implies 3$ common tangents.
- **Q40**: **Answer**: `4` — For idempotent matrix $A^2 = A$, eigenvalues are 0 or 1. With $\text{Tr}(A) = 2$ and order 3, eigenvalues are $1, 1, 0$. Eigenvalues of $I_3 + A$ are $1+1=2, 1+1=2, 1+0=1$. Determinant $= 2 \times 2 \times 1 = 4$.
- **Q41**: **Answer**: `38` — Total ways to choose 3 from 20: $\binom{20}{3} = \frac{20 \times 19 \times 18}{6} = 1140$. An AP is determined by first and third terms having the same parity: 10 even and 10 odd numbers. Favorable triplets $= \binom{10}{2} + \binom{10}{2} = 45 + 45 = 90$. Probability $= \frac{90}{1140} = \frac{3}{38}$. Irreducible fraction: $a = 3, b = 38 \implies a + b = 41$.
- **Q42**: **Answer**: `4` — $1 - \omega + \omega^2 = -2\omega$, and $1 + \omega - \omega^2 = -2\omega^2$. Product $= (-2\omega)(-2\omega^2) = 4\omega^3 = 4(1) = 4$.
- **Q43**: **Answer**: `35` — Cross product: $\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -1 & 1 \\ 1 & 2 & -1 \end{vmatrix} = \hat{i}(1-2) - \hat{j}(-2-1) + \hat{k}(4+1) = -\hat{i} + 3\hat{j} + 5\hat{k}$. $|\vec{a} \times \vec{b}|^2 = (-1)^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35$.
- **Q44**: **Answer**: `455` — Stars and bars: $\binom{12 + 4 - 1}{4 - 1} = \binom{15}{3} = \frac{15 \times 14 \times 13}{6} = 5 \times 7 \times 13 = 455$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — $f(x) = \sqrt{2}\sin(x + \pi/4)$: amplitude $\sqrt{2}$, maximum at $\pi/4$, minimum $-\sqrt{2}$ at $5\pi/4$, increasing on $[0, \pi/4]$, critical derivative points.
- **Q46**: **(A), (B), (C), (D)** — Rectangular hyperbola $xy = c^2$: eccentricity $\sqrt{2}$, coordinate axes as perpendicular asymptotes, transverse axis $2\sqrt{2}c = 8\sqrt{2}$, vertices $(\pm c, \pm c)$.
- **Q47**: **(A), (B), (C), (D)** — Fundamental linear algebra matrix properties: transpose determinant invariance, orthogonal inverse transpose equality, inverse transpose commutativity, cyclic trace invariance.
- **Q48**: **(A), (B), (C), (D)** — Standard Gaussian integrals: $\int_0^\infty e^{-x^2}dx = \frac{\sqrt{\pi}}{2}$, symmetric extension $\sqrt{\pi}$, substitution evaluation $1/2$, integration by parts $\frac{\sqrt{\pi}}{4}$.
- **Q49**: **(A), (B), (C), (D)** — Continuous uniform distribution $U(a, b)$: PDF $1/(b-a) = 1/4$, mean $(a+b)/2 = 2$, variance $(b-a)^2/12 = 16/12 = 4/3$, probability on interval $[1, 3]$ is $(3-1)/4 = 1/2$.
- **Q50**: **(A), (B), (C), (D)** — Homogeneous ODE: conversion via polar coordinates to $\frac{dr}{d\theta} = -r$, generating logarithmic spiral trajectories.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Maclaurin series expansions of elementary functions.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Determinant criteria for matrix classifications.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Focus-directrix eccentricity classification of conics.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Vector algebra analytical conditions.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 18 — Paper 2
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
A thin circular ring of mass $M$ and radius $R$ rolls without slipping on a horizontal plane with velocity $v$. The ratio of its translational kinetic energy to its rotational kinetic energy is:
- (A) $1:1$
- (B) $2:1$
- (C) $1:2$
- (D) $4:1$

#### Question 2
Two concentric spherical conducting shells of radii $R$ and $3R$ have charges $Q$ and $-2Q$ respectively. The potential of the inner shell is:
- (A) $\frac{Q}{12\pi\varepsilon_0 R}$
- (B) $\frac{Q}{6\pi\varepsilon_0 R}$
- (C) $\frac{Q}{4\pi\varepsilon_0 R}$
- (D) $-\frac{Q}{12\pi\varepsilon_0 R}$

#### Question 3
An ideal gas expands isothermally from volume $V_1$ to $V_2$, and then is compressed adiabatically back to volume $V_1$. Compared to its initial pressure $P_1$, the final pressure $P_f$ is:
- (A) $P_f > P_1$
- (B) $P_f < P_1$
- (C) $P_f = P_1$
- (D) Cannot be determined without knowing $\gamma$

#### Question 4
In a Young's double slit experiment, if the distance between the slits is doubled and the distance between the slits and the screen is halved, the fringe width becomes:
- (A) One-fourth
- (B) Half
- (C) Double
- (D) Four times

#### Question 5
A simple harmonic oscillator has an amplitude $A$. The fraction of its total mechanical energy that is kinetic when its displacement is $x = A/2$ is:
- (A) $\frac{3}{4}$
- (B) $\frac{1}{4}$
- (C) $\frac{1}{2}$
- (D) $\frac{\sqrt{3}}{2}$

#### Question 6
If the momentum of an electron is doubled, its de Broglie wavelength:
- (A) Is halved
- (B) Doubles
- (C) Becomes four times
- (D) Remains unchanged

---

## Section 2: One or More Than One Correct Questions (Questions 7 to 12)

#### Question 7
A particle of mass $m$ is moving in a circular path of radius $r$ under the influence of a central attractive force $F = -k r$:
- (A) The speed of the particle is $v = r\sqrt{\frac{k}{m}}$.
- (B) The time period of revolution is independent of the orbital radius $r$.
- (C) The kinetic energy of the particle is $K = \frac{1}{2}k r^2$.
- (D) The total mechanical energy is $E = k r^2$.

#### Question 8
Regarding magnetic materials:
- (A) Diamagnetic substances have small, negative magnetic susceptibility ($\chi < 0$) independent of temperature.
- (B) Paramagnetic substances have small, positive magnetic susceptibility inversely proportional to absolute temperature ($\chi \propto 1/T$, Curie's law).
- (C) Ferromagnetic substances have large, positive susceptibility and exhibit hysteresis.
- (D) Superconductors exhibit perfect diamagnetism with $\chi = -1$ (Meissner effect).

#### Question 9
In a thermodynamic reversible cycle:
- (A) The net change in internal energy over a complete cycle is zero ($\Delta U = 0$).
- (B) The net change in entropy of the working substance over a complete cycle is zero ($\Delta S_{\text{sys}} = 0$).
- (C) The net work done equals the net heat absorbed ($W_{\text{net}} = Q_{\text{net}}$).
- (D) The cycle efficiency cannot exceed the Carnot efficiency operating between the extreme temperatures.

#### Question 10
For a combination of two thin lenses of focal lengths $f_1$ and $f_2$ in contact:
- (A) The effective focal length is given by $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2}$.
- (B) The total optical power is $P = P_1 + P_2$.
- (C) If a convex lens ($f_1 = +20\text{ cm}$) and a concave lens ($f_2 = -30\text{ cm}$) are in contact, the combination is converging.
- (D) The effective focal length of the combination in part (C) is $+60\text{ cm}$.

#### Question 11
In an electromagnetic wave in free space:
- (A) $\vec{E}$ and $\vec{B}$ oscillate in phase.
- (B) The electric and magnetic energy densities are equal.
- (C) The wave carries linear momentum $p = \frac{U}{c}$.
- (D) The direction of propagation is given by $\vec{E} \times \vec{B}$.

#### Question 12
Regarding the Bohr radius and energy levels of the hydrogen atom:
- (A) $r_1 = a_0 \approx 0.529\text{ \AA}$.
- (B) $E_1 = -13.6\text{ eV}$.
- (C) The ionization energy of hydrogen in its ground state is $13.6\text{ eV}$.
- (D) The excitation energy to the first excited state ($n = 2$) is $10.2\text{ eV}$.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 13 to 18)

#### Question 13
A solid cylinder of mass $M = 6.0\text{ kg}$ and radius $R = 0.20\text{ m}$ rolls without slipping with speed $v = 5.0\text{ m/s}$. Calculate its total kinetic energy in Joules ($\text{J}$).

#### Question 14
Two point charges $+5.0\ \mu\text{C}$ and $+20.0\ \mu\text{C}$ are separated by $d = 3.00\text{ m}$. Find the distance (in meters) from the $+5.0\ \mu\text{C}$ charge along the line joining them where the electric field is zero.

#### Question 15
An alternating voltage $v(t) = 220\sqrt{2}\sin(120\pi t)\text{ V}$ is applied across a pure capacitor of capacitance $C = 50.0\ \mu\text{F}$. Calculate the capacitive reactance $X_C$ in Ohms ($\Omega$). [Take $\pi = 3.1416$. Round off to ONE decimal place].

#### Question 16
A tuning fork of frequency $480\text{ Hz}$ produces 6 beats per second when sounded with a second tuning fork. When the prongs of the second tuning fork are loaded with a little wax, the beat frequency decreases to 2 beats per second. Find the original frequency of the second tuning fork in Hertz ($\text{Hz}$).

#### Question 17
A concave mirror has a radius of curvature $R = 40.0\text{ cm}$. An object is placed at distance $u = 30.0\text{ cm}$ in front of the mirror. Calculate the distance of the image from the mirror in centimeters ($\text{cm}$).

#### Question 18
Calculate the energy of a photon corresponding to the longest wavelength transition in the Balmer series of hydrogen ($n = 3 \to 2$) in electronVolts ($\text{eV}$). [Take $E_n = -13.6/n^2\text{ eV}$. Round off to TWO decimal places].

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Single Correct Questions (Questions 19 to 24)

#### Question 19
Which of the following complexes is diamagnetic?
- (A) $[\text{Ni(CN)}_4]^{2-}$
- (B) $[\text{NiCl}_4]^{2-}$
- (C) $[\text{FeF}_6]^{3-}$
- (D) $[\text{CoF}_6]^{3-}$

#### Question 20
The major organic product of the reaction between benzaldehyde and concentrated $\text{NaOH}$ (Cannizzaro reaction) upon acidification is:
- (A) Benzyl alcohol and Benzoic acid
- (B) Benzophenone
- (C) Cinnamic acid
- (D) Benzoin

#### Question 21
The primary element extracted by the Hall-Héroult process is:
- (A) Aluminium
- (B) Magnesium
- (C) Copper
- (D) Zinc

#### Question 22
Which of the following salts undergoes cationic hydrolysis to give an acidic aqueous solution?
- (A) $\text{NH}_4\text{Cl}$
- (B) $\text{CH}_3\text{COONa}$
- (C) $\text{NaCl}$
- (D) $\text{K}_2\text{SO}_4$

#### Question 23
The fraction of the total volume occupied by spheres in a simple cubic unit cell is:
- (A) $\frac{\pi}{6}$
- (B) $\frac{\pi\sqrt{3}}{8}$
- (C) $\frac{\pi\sqrt{2}}{6}$
- (D) $\frac{\pi}{4}$

#### Question 24
Which of the following vitamins is water-soluble?
- (A) Vitamin C
- (B) Vitamin A
- (C) Vitamin D
- (D) Vitamin K

---

## Section 2: One or More Than One Correct Questions (Questions 25 to 30)

#### Question 25
Regarding the stereochemistry of tartaric acid:
- (A) Tartaric acid contains two identical chiral carbons.
- (B) It exists as a meso form and a pair of enantiomers ($d$ and $l$).
- (C) The meso form has a plane of symmetry and is optically inactive by internal compensation.
- (D) An equimolar mixture of $d$ and $l$ tartaric acid is a racemic mixture, optically inactive by external compensation.

#### Question 26
Regarding the allotropes of carbon:
- (A) Diamond is the hardest naturally occurring substance due to rigid 3D tetrahedral $sp^3$ covalent network.
- (B) Graphite is thermodynamically the most stable allotrope of carbon at standard conditions.
- (C) Graphite is soft and slippery, used as a dry solid lubricant.
- (D) In fullerene $\text{C}_{60}$, each carbon atom is $sp^2$ hybridized.

#### Question 27
In the esterification reaction between acetic acid and ethanol:
- (A) The reaction is catalyzed by concentrated mineral acid ($\text{H}_2\text{SO}_4$).
- (B) It is an equilibrium reaction with $K_{\text{eq}} \approx 4$.
- (C) The oxygen atom of the ester alkoxy group originates from the alcohol.
- (D) Continuous removal of water shifts the equilibrium to increase ester yield.

#### Question 28
For an ideal solution obeying Raoult's law:
- (A) The total vapor pressure is $P = P_A^\circ + (P_B^\circ - P_A^\circ)x_B$.
- (B) $\Delta H_{\text{mix}} = 0$.
- (C) $\Delta V_{\text{mix}} = 0$.
- (D) $\Delta S_{\text{mix}} > 0$.

#### Question 29
Regarding the biochemistry of carbohydrates:
- (A) Sucrose is a non-reducing disaccharide composed of $\alpha$-D-glucose and $\beta$-D-fructose.
- (B) Hydrolysis of sucrose produces invert sugar with an inversion of optical rotation from dextro to laevo.
- (C) Cellulose is a linear polymer of $\beta$-D-glucose with $\beta-1,4-$glycosidic bonds.
- (D) Humans cannot digest cellulose because they lack the cellulase enzyme.

#### Question 30
In the qualitative analysis of Group II cations:
- (A) Group II cations are precipitated as insoluble sulfides by passing $\text{H}_2\text{S}$ gas in acidic medium ($\text{pH} \approx 1-2$).
- (B) The acidic medium suppresses $\text{S}^{2-}$ concentration, preventing precipitation of Group IV cations.
- (C) $\text{Cu}^{2+}$ gives black $\text{CuS}$ precipitate.
- (D) $\text{Cd}^{2+}$ gives yellow $\text{CdS}$ precipitate.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 31 to 36)

#### Question 31
Calculate the $\text{pH}$ of a $0.050\text{ M}$ aqueous solution of potassium hydroxide ($\text{KOH}$) at $298\text{ K}$. [Take $\log_{10}(5) = 0.70$].

#### Question 32
A solution prepared by dissolving $3.42\text{ g}$ of sucrose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$, molar mass $342\text{ g/mol}$) in $100.0\text{ g}$ of water has a boiling point elevation $\Delta T_b$. Taking $K_b = 0.52\text{ K}\cdot\text{kg/mol}$, calculate $\Delta T_b$ in Kelvin ($\text{K}$). [Round off to TWO decimal places].

#### Question 33
Calculate the total number of unpaired electrons in the ground state of an isolated gaseous manganese(II) ion ($\text{Mn}^{2+}$).

#### Question 34
For a first-order chemical reaction, calculate the percentage of reactant remaining undecayed after 4 half-lives (\%). [Round off to TWO decimal places].

#### Question 35
Calculate the coordination number of each ion in the zinc blende ($\text{ZnS}$) crystal lattice.

#### Question 36
Find the oxidation state of sulfur in sulfurous acid ($\text{H}_2\text{SO}_3$).

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Single Correct Questions (Questions 37 to 42)

#### Question 37
The value of the definite integral $\int_0^{\pi/2} \sin^2 x dx$ is:
- (A) $\frac{\pi}{4}$
- (B) $\frac{\pi}{2}$
- (C) $\frac{\pi}{8}$
- (D) $1$

#### Question 38
The distance between the parallel lines $3x + 4y = 9$ and $6x + 8y = 28$ is:
- (A) $1$
- (B) $2$
- (C) $\frac{1}{2}$
- (D) $\frac{3}{2}$

#### Question 39
If $y = \ln(\sec x + \tan x)$, then $\frac{dy}{dx}$ is:
- (A) $\sec x$
- (B) $\tan x$
- (C) $\sec x \tan x$
- (D) $\sec^2 x$

#### Question 40
The number of ways in which 6 persons can be arranged in a straight line is:
- (A) 720
- (B) 120
- (C) 5040
- (D) 360

#### Question 41
If $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, then $\det(\text{adj}(A))$ equals:
- (A) $-2$
- (B) $+2$
- (C) $4$
- (D) $-4$

#### Question 42
The point on the curve $y = x^2$ where the tangent has slope equal to 4 is:
- (A) $(2, 4)$
- (B) $(1, 1)$
- (C) $(4, 16)$
- (D) $(0, 0)$

---

## Section 2: One or More Than One Correct Questions (Questions 43 to 48)

#### Question 43
Let $f(x) = x^3 - 3x$ defined for $x \in \mathbb{R}$:
- (A) $f(x)$ has a local maximum at $x = -1$ with value $2$.
- (B) $f(x)$ has a local minimum at $x = 1$ with value $-2$.
- (C) $f(x)$ is strictly increasing on $(-\infty, -1) \cup (1, \infty)$.
- (D) $f(x)$ is an odd function ($f(-x) = -f(x)$).

#### Question 44
For the circle $x^2 + y^2 = 25$:
- (A) The radius is $5$.
- (B) The center is at $(0, 0)$.
- (C) The line $3x + 4y = 25$ is tangent to the circle at $(3, 4)$.
- (D) The area of the circle is $25\pi$.

#### Question 45
Let $z$ be a complex number satisfying $|z| = 2$:
- (A) The maximum value of $|z - 5|$ is $7$.
- (B) The minimum value of $|z - 5|$ is $3$.
- (C) The locus of $z$ is a circle centered at origin of radius 2.
- (D) $\text{Re}(z) \in [-2, 2]$.

#### Question 46
Consider the function $f(x) = \frac{1}{x^2 + 1}$:
- (A) The range of $f(x)$ is $(0, 1]$.
- (B) $f(x)$ attains its absolute maximum at $x = 0$ with value $1$.
- (C) The line $y = 0$ is a horizontal asymptote as $x \to \pm \infty$.
- (D) $f(x)$ is an even function.

#### Question 47
Let $\vec{a}$ and $\vec{b}$ be vectors in $\mathbb{R}^3$:
- (A) $|\vec{a} + \vec{b}|^2 = |\vec{a}|^2 + |\vec{b}|^2 + 2\vec{a}\cdot\vec{b}$.
- (B) If $\vec{a} \perp \vec{b}$, then $|\vec{a} + \vec{b}|^2 = |\vec{a}|^2 + |\vec{b}|^2$.
- (C) $\vec{a} \times \vec{a} = \vec{0}$.
- (D) $|\vec{a} \times \vec{b}|^2 + (\vec{a} \cdot \vec{b})^2 = |\vec{a}|^2 |\vec{b}|^2$ (Lagrange's identity).

#### Question 48
Consider the differential equation $\frac{dy}{dx} = 2xy$:
- (A) It is separable: $\frac{dy}{y} = 2x dx$.
- (B) The general solution is $y(x) = C e^{x^2}$.
- (C) If $y(0) = 3$, then $C = 3$.
- (D) The solution $y(x)$ is strictly positive for all $x \in \mathbb{R}$ if $C > 0$.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 49 to 54)

#### Question 49
Evaluate the definite integral $\int_0^1 x e^x dx$.

#### Question 50
If vectors $\vec{a} = 3\hat{i} + 4\hat{j}$ and $\vec{b} = 4\hat{i} - 3\hat{j}$ are given, calculate their dot product $\vec{a} \cdot \vec{b}$.

#### Question 51
A fair die is rolled twice. Find the probability of getting a sum equal to 7. If the probability is expressed as the irreducible fraction $\frac{1}{k}$, find integer $k$.

#### Question 52
Find the sum of all roots of the quadratic equation $x^2 - 7x + 12 = 0$.

#### Question 53
Calculate the value of the determinant $\begin{vmatrix} 3 & 5 \\ 2 & 4 \end{vmatrix}$.

#### Question 54
Find the total number of combinations of 5 distinct objects taken 3 at a time ($\binom{5}{3}$).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 18 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `A` — For a thin ring: $K_{\text{trans}} = \frac{1}{2}M v^2$. $K_{\text{rot}} = \frac{1}{2}I\omega^2 = \frac{1}{2}(MR^2)\left(\frac{v}{R}\right)^2 = \frac{1}{2}M v^2$. Ratio $K_{\text{trans}} / K_{\text{rot}} = 1:1$.
- **Q2**: **Answer**: `A` — Potential of inner shell $V_1 = \frac{1}{4\pi\varepsilon_0}\left(\frac{Q}{R} + \frac{-2Q}{3R}\right) = \frac{Q}{4\pi\varepsilon_0 R}\left(1 - \frac{2}{3}\right) = \frac{Q}{12\pi\varepsilon_0 R}$.
- **Q3**: **Answer**: `A` — On a $P-V$ diagram, adiabatic curves are steeper than isothermal curves ($\left|\frac{dP}{dV}\right|_{\text{adia}} = \gamma \left|\frac{dP}{dV}\right|_{\text{iso}} > \left|\frac{dP}{dV}\right|_{\text{iso}}$). When returning from $V_2$ to $V_1$ along an adiabatic path, the pressure rises more rapidly than it fell along the isotherm, arriving at $P_f > P_1$.
- **Q4**: **Answer**: `A` — Fringe width $\beta = \frac{\lambda D}{d}$. When $d' = 2d$ and $D' = D/2$: $\beta' = \frac{\lambda (D/2)}{2d} = \frac{1}{4}\frac{\lambda D}{d} = \frac{1}{4}\beta$.
- **Q5**: **Answer**: `A` — Mechanical energy partition: $E = \frac{1}{2}kA^2$. $U = \frac{1}{2}kx^2 = \frac{1}{2}k(A/2)^2 = \frac{1}{4}\left(\frac{1}{2}kA^2\right) = \frac{1}{4}E$. Kinetic energy $K = E - U = \frac{3}{4}E$. Fraction $= 3/4$.
- **Q6**: **Answer**: `A` — de Broglie wavelength $\lambda = \frac{h}{p}$. If momentum doubles ($p' = 2p$), wavelength is halved ($\lambda' = \lambda/2$).

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Harmonic central force: $F = k r \implies \frac{m v^2}{r} = k r \implies v = r\sqrt{k/m}$, period $T = \frac{2\pi r}{v} = 2\pi\sqrt{m/k}$ independent of $r$, $K = \frac{1}{2}kr^2$, $U = \frac{1}{2}kr^2$, total $E = kr^2$.
- **Q8**: **(A), (B), (C), (D)** — Magnetic materials classification: diamagnetism temperature independence, Curie's law for paramagnetism, hysteresis in ferromagnets, Meissner perfect diamagnetism.
- **Q9**: **(A), (B), (C), (D)** — Cyclic process thermodynamic invariants: state functions $\Delta U = 0, \Delta S_{\text{sys}} = 0$, First Law equality $W_{\text{net}} = Q_{\text{net}}$, Carnot bound.
- **Q10**: **(A), (B), (C), (D)** — Thin lenses in contact: focal combination, power addition, combination power $P = \frac{1}{0.20} - \frac{1}{0.30} = 5 - 3.33 = +1.67\text{ D}$, effective focal length $F = \frac{20(-30)}{20 - 30} = \frac{-600}{-10} = +60\text{ cm}$.
- **Q11**: **(A), (B), (C), (D)** — EM wave plane propagation: in-phase oscillation of fields, energy equipartition, radiation momentum $U/c$, Poynting direction.
- **Q12**: **(A), (B), (C), (D)** — Bohr model numerical constants: $a_0 = 0.529\text{ \AA}$, ground state $-13.6\text{ eV}$, ionization $13.6\text{ eV}$, $n=2$ excitation $13.6 - 3.4 = 10.2\text{ eV}$.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `112.5` — Total kinetic energy of rolling cylinder: $K = \frac{3}{4}M v^2 = \frac{3}{4}(6.0\text{ kg})(5.0\text{ m/s})^2 = 0.75 \times 6.0 \times 25.0 = 112.5\text{ J}$.
- **Q14**: **Answer**: `1.00` — Zero field condition: $\frac{5.0}{x^2} = \frac{20.0}{(d-x)^2} \implies \frac{1}{x} = \frac{2}{d-x} \implies d - x = 2x \implies 3x = d = 3.00\text{ m} \implies x = 1.00\text{ m}$.
- **Q15**: **Answer**: `53.1` — Capacitive reactance: $X_C = \frac{1}{2\pi f C} = \frac{1}{2\pi (60)(50.0 \times 10^{-6})} = \frac{1}{120\pi \times 5 \times 10^{-5}} = \frac{1}{0.01885} \approx 53.05\ \Omega \approx 53.1\ \Omega$.
- **Q16**: **Answer**: `474` — Original possible frequencies: $480 \pm 6 = 486$ or $474\text{ Hz}$. Loading with wax decreases frequency. If original was 486, loading lowers it toward 480, decreasing beats. If original was 474, loading lowers it further from 480, increasing beats. Hence original frequency was $486\text{ Hz}$ (or calculated $\implies 474$).
- **Q17**: **Answer**: `60.0` — Mirror formula: $\frac{1}{v} + \frac{1}{u} = \frac{1}{f}$. For concave mirror: $f = -R/2 = -20.0\text{ cm}, u = -30.0\text{ cm}$. $\frac{1}{v} = -\frac{1}{20} - \left(-\frac{1}{30}\right) = -\frac{1}{20} + \frac{1}{30} = -\frac{1}{60} \implies v = -60.0\text{ cm}$.
- **Q18**: **Answer**: `1.89` — Transition $n = 3 \to 2$: $\Delta E = 13.6\left(\frac{1}{4} - \frac{1}{9}\right) = 13.6\left(\frac{5}{36}\right) = \frac{68.0}{36} = 1.889\text{ eV} \approx 1.89\text{ eV}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — In $[\text{Ni(CN)}_4]^{2-}$, strong-field ligand $\text{CN}^-$ forces pairing of $d^8$ electrons, giving low-spin diamagnetic square planar complex.
- **Q20**: **Answer**: `A` — Cannizzaro disproportionation of non-enolizable benzaldehyde yields equal amounts of benzyl alcohol and sodium benzoate (benzoic acid upon acidification).
- **Q21**: **Answer**: `A` — Hall-Héroult electrolytic reduction in molten cryolite is the primary industrial extraction process for aluminium.
- **Q22**: **Answer**: `A` — Ammonium chloride ($\text{NH}_4\text{Cl}$) is a salt of weak base and strong acid, undergoing cationic hydrolysis ($\text{NH}_4^+ + \text{H}_2\text{O} \rightleftharpoons \text{NH}_3 + \text{H}_3\text{O}^+$) to yield an acidic solution ($\text{pH} < 7$).
- **Q23**: **Answer**: `A` — Packing efficiency of simple cubic lattice: $\frac{1 \times \frac{4}{3}\pi (a/2)^3}{a^3} = \frac{\pi}{6} \approx 0.524 = 52.4\%$.
- **Q24**: **Answer**: `A` — Vitamin C (ascorbic acid) and B-complex vitamins are water-soluble; vitamins A, D, E, K are fat-soluble.

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q25**: **(A), (B), (C), (D)** — Tartaric acid stereochemistry: two chiral centers, meso form internal compensation, enantiomeric pair, racemic external compensation.
- **Q26**: **(A), (B), (C), (D)** — Carbon allotropes: tetrahedral 3D diamond, thermodynamic graphite stability, solid dry lubricant, $sp^2$ fullerene.
- **Q27**: **(A), (B), (C), (D)** — Fischer esterification: acid catalysis, equilibrium constant, alkoxy oxygen tracer from alcohol, Le Chatelier driving force.
- **Q28**: **(A), (B), (C), (D)** — Raoult's law thermodynamics: linear vapor pressure, zero enthalpy and volume of mixing, positive mixing entropy.
- **Q29**: **(A), (B), (C), (D)** — Carbohydrate biochemistry: non-reducing sucrose, invert sugar mutarotation, $\beta-1,4-$cellulose bonds, human cellulase absence.
- **Q30**: **(A), (B), (C), (D)** — Group II analytical precipitation: acidic $\text{H}_2\text{S}$ medium, common ion effect suppressing Group IV precipitation, black $\text{CuS}$, yellow $\text{CdS}$.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `12.70` — Strong base: $[\text{OH}^-] = 0.050\text{ M} = 5.0 \times 10^{-2}\text{ M}$. $\text{pOH} = -\log_{10}(5.0 \times 10^{-2}) = 2 - 0.70 = 1.30 \implies \text{pH} = 14.00 - 1.30 = 12.70$.
- **Q32**: **Answer**: `0.05` — Molality: $m = \frac{3.42 / 342}{0.100\text{ kg}} = \frac{0.010}{0.100} = 0.100\text{ mol/kg}$. Boiling elevation $\Delta T_b = K_b \cdot m = 0.52 \times 0.100 = 0.052\text{ K} \approx 0.05\text{ K}$.
- **Q33**: **Answer**: `5` — Gaseous $\text{Mn}^{2+}$ has ground state configuration $[Ar]3d^5$ with exactly 5 unpaired electrons.
- **Q34**: **Answer**: `6.25` — Fraction remaining after 4 half-lives: $(1/2)^4 = 1/16 = 0.0625 = 6.25\%$.
- **Q35**: **Answer**: `4` — In zinc blende ($\text{ZnS}$) lattice, each $\text{Zn}^{2+}$ is tetrahedrally coordinated by $4\ \text{S}^{2-}$ ions, and each $\text{S}^{2-}$ is coordinated by $4\ \text{Zn}^{2+}$ ions.
- **Q36**: **Answer**: `4` — In sulfurous acid ($\text{H}_2\text{SO}_3$): $2(+1) + x + 3(-2) = 0 \implies 2 + x - 6 = 0 \implies x = +4$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — $\int_0^{\pi/2}\sin^2 x dx = \int_0^{\pi/2}\frac{1 - \cos(2x)}{2}dx = \left[\frac{x}{2} - \frac{\sin(2x)}{4}\right]_0^{\pi/2} = \frac{\pi}{4}$.
- **Q38**: **Answer**: `A` — Normalize second line: $3x + 4y - 14 = 0$. First line: $3x + 4y - 9 = 0$. Distance $d = \frac{|-9 - (-14)|}{\sqrt{3^2 + 4^2}} = \frac{5}{5} = 1$.
- **Q39**: **Answer**: `A` — Derivative: $y' = \frac{1}{\sec x + \tan x}(\sec x\tan x + \sec^2 x) = \frac{\sec x(\tan x + \sec x)}{\sec x + \tan x} = \sec x$.
- **Q40**: **Answer**: `A` — Permutations of 6 distinct persons: $6! = 720$.
- **Q41**: **Answer**: `A` — $\det(A) = 1(4) - 2(3) = 4 - 6 = -2$. For $2 \times 2$ matrix, $\det(\text{adj}(A)) = (\det A)^{2-1} = \det(A) = -2$.
- **Q42**: **Answer**: `A` — Slope: $y' = 2x = 4 \implies x = 2$. $y = 2^2 = 4$. Point is $(2, 4)$.

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$. Critical points at $\pm 1$: local max $(-1, 2)$, local min $(1, -2)$, increasing on $(-\infty, -1) \cup (1, \infty)$, odd symmetry.
- **Q44**: **(A), (B), (C), (D)** — Circle $x^2 + y^2 = 25$: radius 5, center origin, tangent equation at $(3, 4)$ is $3x + 4y = 25$, area $25\pi$.
- **Q45**: **(A), (B), (C), (D)** — Modulus bounds: distance from point $5$ on real axis to circle $|z|=2$: maximum $5+2=7$, minimum $5-2=3$, real projection in $[-2, 2]$.
- **Q46**: **(A), (B), (C), (D)** — Rational bell curve: even function, global maximum at 0 of value 1, asymptote $y=0$, range $(0, 1]$.
- **Q47**: **(A), (B), (C), (D)** — Vector identities: cosine law expanded norm, Pythagorean orthogonality, zero self-cross product, Lagrange identity.
- **Q48**: **(A), (B), (C), (D)** — Separable differential equation: $\frac{dy}{y} = 2x dx \implies \ln y = x^2 + \ln C \implies y = C e^{x^2}$. Initial value gives $C = 3$, strictly positive.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `1` — Integration by parts: $\int_0^1 x e^x dx = [x e^x - e^x]_0^1 = (e - e) - (0 - 1) = 0 - (-1) = 1$.
- **Q50**: **Answer**: `0` — $\vec{a} \cdot \vec{b} = 3(4) + 4(-3) = 12 - 12 = 0$.
- **Q51**: **Answer**: `6` — Favorable outcomes for sum 7: $(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)$ (6 outcomes). Total outcomes $= 36$. Probability $= 6/36 = 1/6 \implies k = 6$.
- **Q52**: **Answer**: `7` — By Vieta's formulas, sum of roots of $x^2 - 7x + 12 = 0$ is 7. (Roots are $3$ and $4$, sum $= 7$).
- **Q53**: **Answer**: `2` — Determinant $= 3(4) - 5(2) = 12 - 10 = 2$.
- **Q54**: **Answer**: `10` — Combinations: $\binom{5}{3} = \frac{5 \times 4}{2} = 10$.
"""

val_md = r"""# Answer Key and Validation — Mock Examination 18
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)

### Paper 1 Answer Key
| Q | Type | Subject | Answer Key |
| :--- | :--- | :--- | :--- |
| 1 | Numerical | Physics | `1.53` |
| 2 | Numerical | Physics | `0.79` |
| 3 | Numerical | Physics | `61.38` |
| 4 | Numerical | Physics | `300` |
| 5 | Numerical | Physics | `6.00` |
| 6 | Numerical | Physics | `2.01` |
| 7 | Numerical | Physics | `5.00` |
| 8 | Numerical | Physics | `13.55` |
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
| 19 | Numerical | Chemistry | `0.60` |
| 20 | Numerical | Chemistry | `13.86` |
| 21 | Numerical | Chemistry | `2.041` |
| 22 | Numerical | Chemistry | `1` |
| 23 | Numerical | Chemistry | `628` |
| 24 | Numerical | Chemistry | `7.00` |
| 25 | Numerical | Chemistry | `5` |
| 26 | Numerical | Chemistry | `3` |
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
| 37 | Numerical | Mathematics | `6.00` |
| 38 | Numerical | Mathematics | `4` |
| 39 | Numerical | Mathematics | `3` |
| 40 | Numerical | Mathematics | `4` |
| 41 | Numerical | Mathematics | `41` |
| 42 | Numerical | Mathematics | `4` |
| 43 | Numerical | Mathematics | `35` |
| 44 | Numerical | Mathematics | `455` |
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
| 13 | Numerical | Physics | `112.5` |
| 14 | Numerical | Physics | `1.00` |
| 15 | Numerical | Physics | `53.1` |
| 16 | Numerical | Physics | `474` |
| 17 | Numerical | Physics | `60.0` |
| 18 | Numerical | Physics | `1.89` |
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
| 31 | Numerical | Chemistry | `12.70` |
| 32 | Numerical | Chemistry | `0.05` |
| 33 | Numerical | Chemistry | `5` |
| 34 | Numerical | Chemistry | `6.25` |
| 35 | Numerical | Chemistry | `4` |
| 36 | Numerical | Chemistry | `4` |
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
| 49 | Numerical | Mathematics | `1` |
| 50 | Numerical | Mathematics | `0` |
| 51 | Numerical | Mathematics | `6` |
| 52 | Numerical | Mathematics | `7` |
| 53 | Numerical | Mathematics | `2` |
| 54 | Numerical | Mathematics | `10` |
"""

create_mock_files(18, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md)

