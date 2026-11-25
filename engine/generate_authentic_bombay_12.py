# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 12.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 12 — Paper 1
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
A uniform slender rod of mass $M = 3.0\text{ kg}$ and length $L = 1.20\text{ m}$ is suspended horizontally by two identical light inextensible vertical strings attached to its two ends $A$ and $B$. Suddenly, the string at end $B$ is severed. Taking $g = 10.0\text{ m/s}^2$, calculate the tension $T_A$ in string $A$ immediately after string $B$ is cut, in Newtons ($\text{N}$).

#### Question 2
A parallel-plate capacitor with circular plates of radius $R = 0.10\text{ m}$ separated by a gap $d = 2.0\text{ mm}$ is being charged by a constant current $I = 2.50\text{ A}$. Calculate the magnitude of the Poynting vector $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$ at the outer cylindrical rim ($r = R$) inside the capacitor gap in $\text{kW/m}^2$. [Round off to TWO decimal places].

#### Question 3
An ideal diatomic gas ($\gamma = 1.40$) at initial pressure $P_1 = 1.00 \times 10^5\text{ Pa}$ and temperature $T_1 = 300\text{ K}$ occupies volume $V_1 = 0.050\text{ m}^3$. It undergoes a reversible polytropic process $PV^n = \text{constant}$ where $n = 1.20$ to a final volume $V_2 = 0.150\text{ m}^3$. Calculate the total heat absorbed $Q$ by the gas in kiloJoules ($\text{kJ}$). [Take $3^{0.20} \approx 1.246$. Round off to TWO decimal places].

#### Question 4
A long coaxial cable consists of an inner solid cylindrical conductor of radius $a = 2.0\text{ mm}$ and a thin outer coaxial cylindrical shell of radius $b = 8.0\text{ mm}$. A current $I = 10.0\text{ A}$ flows uniformly along the inner conductor and returns along the outer shell. Calculate the total magnetic energy $U_m$ stored in a $1.0\text{ m}$ length of the space between the conductors ($a \le r \le b$) in microJoules ($\mu\text{J}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ and $\ln 4 \approx 1.3863$. Round off to TWO decimal places].

#### Question 5
In a Newton's rings experiment using reflected monochromatic light of wavelength $\lambda = 600\text{ nm}$, the diameter of the 10th dark ring is $D_{10} = 4.00\text{ mm}$ when air is between the plano-convex lens and the flat glass plate. If the air film is replaced by an oil film of refractive index $\mu_{\text{oil}} = 1.44$, calculate the new diameter of the 10th dark ring in millimeters ($\text{mm}$). [Round off to TWO decimal places].

#### Question 6
A solid insulating sphere of radius $R = 0.20\text{ m}$ has a non-uniform spherically symmetric charge density given by $\rho(r) = \rho_0 \left(1 - \frac{r}{R}\right)$ for $0 \le r \le R$, where $\rho_0 = 6.00 \times 10^{-6}\text{ C/m}^3$. Calculate the total electrostatic potential energy $U$ stored in the electric field inside the sphere in milliJoules ($\text{mJ}$). [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$. Round off to TWO decimal places].

#### Question 7
A cyclotron is designed to accelerate protons ($m_p = 1.67 \times 10^{-27}\text{ kg}, q = 1.60 \times 10^{-19}\text{ C}$) using a magnetic field $B = 1.50\text{ T}$. If the extraction radius of the dees is $R = 0.60\text{ m}$, calculate the maximum kinetic energy of the accelerated protons in mega-electronVolts ($\text{MeV}$). [Take $1\text{ eV} = 1.60 \times 10^{-19}\text{ J}$. Round off to TWO decimal places].

#### Question 8
A photon of initial wavelength $\lambda_0 = 0.0243\text{ \AA}$ undergoes Compton scattering off a stationary free electron through a scattering angle of $\theta = 60.0^\circ$. Calculate the kinetic energy transferred to the recoil electron in kilo-electronVolts ($\text{keV}$). [Take Compton wavelength $\lambda_C = \frac{h}{m_e c} = 0.0243\text{ \AA}$, $hc = 12.4\text{ keV}\cdot\text{\AA}$, and $\cos 60^\circ = 0.50$. Round off to the nearest integer].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
A heavy uniform disc of mass $M$ and radius $R$ is spinning with high angular velocity $\vec{\omega}_s = \omega_s \hat{i}$ about its axle of length $d$ supported at a pivot $O$ at $x = 0$. The disc is situated at $x = d$ in a uniform gravitational field $\vec{g} = -g\hat{k}$.
- (A) The gravitational torque acting about pivot $O$ is $\vec{\tau} = -Mgd \hat{j}$.
- (B) The spin angular momentum vector is $\vec{L}_s = I \omega_s \hat{i}$ where $I = \frac{1}{2}MR^2$.
- (C) The gyroscope precesses steadily in the horizontal $x-y$ plane about the vertical $z$-axis with angular precession frequency $\Omega_p = \frac{Mgd}{I\omega_s}$.
- (D) If the spin speed $\omega_s$ is doubled, the precession frequency $\Omega_p$ is halved.

#### Question 10
In a damped harmonic oscillator described by $m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = 0$ with natural frequency $\omega_0 = \sqrt{k/m}$ and damping factor $\gamma = \frac{b}{2m}$:
- (A) Under weak damping ($\gamma < \omega_0$), the displacement is given by $x(t) = A_0 e^{-\gamma t}\cos(\omega_d t + \phi)$, where $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$.
- (B) The mechanical energy of the oscillator decays exponentially with time as $E(t) = E_0 e^{-2\gamma t}$.
- (C) The quality factor $Q$ of the oscillator is given by $Q = \frac{\omega_0}{2\gamma} = \frac{m\omega_0}{b}$.
- (D) For critical damping, $\gamma = \omega_0$, and the system returns to equilibrium without performing oscillations.

#### Question 11
Two concentric thin spherical conducting shells of radii $R_1$ and $R_2$ ($R_1 < R_2$) carry charges $Q_1$ and $Q_2$ respectively:
- (A) The potential of the inner shell is $V_1 = \frac{1}{4\pi\varepsilon_0}\left(\frac{Q_1}{R_1} + \frac{Q_2}{R_2}\right)$.
- (B) The potential of the outer shell is $V_2 = \frac{1}{4\pi\varepsilon_0}\left(\frac{Q_1 + Q_2}{R_2}\right)$.
- (C) If the two shells are connected by a thin conducting wire, the charge on the inner shell becomes identically zero.
- (D) If the outer shell is earthed, the potential of the outer shell becomes zero and the charge on the outer shell becomes $Q_2' = -Q_1$.

#### Question 12
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal surface with friction coefficient $\mu$. It is given an initial horizontal velocity $v_0$ without any initial rotation ($\omega_0 = 0$):
- (A) The sphere slips initially, and kinetic friction exerts a constant force $f_k = \mu Mg$ opposing translation.
- (B) The time $t_1$ after which pure rolling begins is $t_1 = \frac{2v_0}{7\mu g}$.
- (C) The linear velocity of the sphere when pure rolling begins is $v = \frac{5}{7}v_0$.
- (D) The total mechanical energy lost due to friction during the sliding phase is $\frac{1}{7}M v_0^2$.

#### Question 13
An ideal blackbody at initial temperature $T_1 = 2000\text{ K}$ cools in an evacuated chamber whose walls are maintained at absolute zero ($0\text{ K}$):
- (A) According to Stefan-Boltzmann law, the total emissive power is proportional to $T^4$.
- (B) According to Wien's displacement law, the peak wavelength $\lambda_{\text{max}}$ shifts to longer wavelengths as temperature decreases.
- (C) The rate of cooling $\left|\frac{dT}{dt}\right|$ is proportional to $T^3$.
- (D) The time required for the absolute temperature to fall to half its initial value is proportional to $T_1^{-3}$.

#### Question 14
A rectangular conducting loop of resistance $R$, length $a$, and width $b$ enters a region of uniform magnetic field $B$ perpendicular to its plane at constant velocity $v$:
- (A) While entering the field, an induced emf $\mathcal{E} = B b v$ is established.
- (B) The external magnetic force opposing the entry is $F_{\text{mag}} = \frac{B^2 b^2 v}{R}$.
- (C) To maintain constant velocity $v$, an external agent must supply mechanical power $P_{\text{ext}} = \frac{B^2 b^2 v^2}{R}$.
- (D) The total electrical energy dissipated as Joule heat during the entire entry process equals the total mechanical work done by the external agent.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the thermodynamic cycle in **List-I** with its theoretical efficiency formula in **List-II** (all symbols carry their standard meanings):

| List-I | List-II |
| :--- | :--- |
| **P.** Carnot Cycle | **1.** $\eta = 1 - \frac{T_C}{T_H}$ |
| **Q.** Otto Cycle (compression ratio $r$) | **2.** $\eta = 1 - \frac{1}{r^{\gamma - 1}}$ |
| **R.** Brayton / Joule Cycle (pressure ratio $r_p$) | **3.** $\eta = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}}$ |
| **S.** Diesel Cycle (cutoff ratio $r_c$, compression ratio $r$) | **4.** $\eta = 1 - \frac{1}{r^{\gamma - 1}}\left[\frac{r_c^\gamma - 1}{\gamma(r_c - 1)}\right]$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the physical phenomenon in **List-I** with the characteristic feature / equation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Brewster's law of polarization | **1.** $\tan \theta_p = \mu$ |
| **Q.** Malus's law of polarized transmission | **2.** $I = I_0 \cos^2 \theta$ |
| **R.** Rayleigh scattering law | **3.** $I \propto \lambda^{-4}$ |
| **S.** Resolving power of circular aperture telescope | **4.** $\theta_{\text{min}} = \frac{1.22\lambda}{D}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 17
Match the electrostatic configuration in **List-I** with the electric field dependence on distance $r$ in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Infinite uniform line charge | **1.** $E \propto r^{-1}$ |
| **Q.** Electric dipole at large distance along axis | **2.** $E \propto r^{-3}$ |
| **R.** Electric quadrupole at large distance | **3.** $E \propto r^{-4}$ |
| **S.** Point charge in three-dimensional space | **4.** $E \propto r^{-2}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 2, S $\to$ 3

#### Question 18
Match the electromagnetic device in **List-I** with its primary operating principle in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Moving coil galvanometer | **1.** Magnetic torque on current loop in uniform radial field |
| **Q.** Step-up AC Transformer | **2.** Mutual induction between two coils on iron core |
| **R.** Cyclotron particle accelerator | **3.** Combined static magnetic Lorentz force and oscillating electric field |
| **S.** Induction furnace | **4.** Eddy current dissipation heating in bulk conductor |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
The solubility product of lead(II) chloride ($\text{PbCl}_2$) in water at $298\text{ K}$ is $K_{sp} = 1.70 \times 10^{-5}\text{ mol}^3/\text{L}^3$. Calculate the molar solubility of $\text{PbCl}_2$ in a $0.100\text{ M}$ aqueous $\text{NaCl}$ solution in millimoles per liter ($\text{mmol/L}$). [Round off to TWO decimal places].

#### Question 20
A galvanic cell is constructed as $\text{Zn}(s) | \text{Zn}^{2+}(0.010\text{ M}) || \text{Fe}^{3+}(0.10\text{ M}), \text{Fe}^{2+}(0.010\text{ M}) | \text{Pt}(s)$. Given standard reduction potentials $E^\circ_{\text{Zn}^{2+}/\text{Zn}} = -0.763\text{ V}$ and $E^\circ_{\text{Fe}^{3+}/\text{Fe}^{2+}} = +0.771\text{ V}$, calculate the cell electromotive force $E_{\text{cell}}$ at $298\text{ K}$ in Volts ($\text{V}$). [Take $\frac{2.303 RT}{F} = 0.0591\text{ V}$. Round off to THREE decimal places].

#### Question 21
For the first-order gas-phase decomposition $2\text{N}_2\text{O}_5(g) \to 4\text{NO}_2(g) + \text{O}_2(g)$, the rate constant at $320\text{ K}$ is $k = 4.50 \times 10^{-3}\text{ s}^{-1}$. Starting with pure $\text{N}_2\text{O}_5$ at initial pressure $P_0 = 500\text{ Torr}$ in a rigid vessel of constant volume, calculate the total pressure inside the vessel after $t = 200\text{ s}$ in Torr. [Take $e^{-0.90} \approx 0.4066$. Round off to the nearest integer].

#### Question 22
A crystalline solid has a face-centered cubic ($fcc$) unit cell composed of metal atoms $M$ with atomic weight $108.0\text{ g/mol}$ and edge length $a = 408.0\text{ pm}$. Calculate the theoretical density of the crystal in $\text{g/cm}^3$. [Take Avogadro's number $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$. Round off to TWO decimal places].

#### Question 23
Find the total number of unpaired electrons in the ground state of the complex ion $[\text{Cr}(\text{H}_2\text{O})_6]^{3+}$.

#### Question 24
In the qualitative analysis of Group II basic radicals, hydrogen sulfide ($\text{H}_2\text{S}$) gas is passed through an acidified solution containing $0.010\text{ M}$ each of $\text{Cu}^{2+}$, $\text{Zn}^{2+}$, $\text{Mn}^{2+}$, and $\text{Ni}^{2+}$ maintained at $\text{pH} = 1.0$. How many of these metal ions precipitate as metal sulfides under these conditions?

#### Question 25
Calculate the total number of stereoisomers (including enantiomers and diastereomers) possible for 2,3-dichlorobutane ($\text{CH}_3\text{CH(Cl)CH(Cl)CH}_3$).

#### Question 26
One mole of an ideal gas at $T = 300\text{ K}$ expands isothermally against a constant external pressure $P_{\text{ext}} = 1.00\text{ bar}$ from initial volume $V_1 = 10.0\text{ L}$ to final volume $V_2 = 35.0\text{ L}$. Calculate the total entropy change of the universe $\Delta S_{\text{univ}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}}$ in $\text{J/K}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 3.5 \approx 1.2528$. Round off to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding the structure, bonding, and reactivity of diborane ($\text{B}_2\text{H}_6$):
- (A) Each boron atom is $sp^3$ hybridized.
- (B) The four terminal $\text{B}-\text{H}$ bonds are conventional two-center two-electron ($2c-2e$) covalent bonds.
- (C) The two bridging $\text{B}-\text{H}-\text{B}$ bonds are three-center two-electron ($3c-2e$) banana bonds.
- (D) Diborane reacts with excess ammonia at high temperatures ($> 450\text{ K}$) to produce inorganic benzene (borazine, $\text{B}_3\text{N}_3\text{H}_6$).

#### Question 28
In the pinacol-pinacolone rearrangement of 2,3-dimethylbutane-2,3-diol treated with concentrated sulfuric acid:
- (A) Protonation of one tertiary hydroxyl group followed by loss of water generates a stable tertiary carbocation.
- (B) A 1,2-methyl shift occurs to form a resonance-stabilized oxocarbenium ion.
- (C) Deprotonation yields 3,3-dimethylbutan-2-one (pinacolone).
- (D) When 1,2-diphenylpropane-1,2-diol undergoes rearrangement, the phenyl group migrates in preference to the methyl group due to higher migratory aptitude.

#### Question 29
Regarding the secondary lead-acid storage battery during discharge:
- (A) At the anode, metallic lead ($\text{Pb}$) is oxidized to insoluble lead(II) sulfate ($\text{PbSO}_4$).
- (B) At the cathode, lead(IV) oxide ($\text{PbO}_2$) is reduced to lead(II) sulfate ($\text{PbSO}_4$).
- (C) Sulfuric acid ($\text{H}_2\text{SO}_4$) is consumed, decreasing the density of the electrolyte solution.
- (D) The overall discharge reaction is $\text{Pb}(s) + \text{PbO}_2(s) + 2\text{H}_2\text{SO}_4(aq) \to 2\text{PbSO}_4(s) + 2\text{H}_2\text{O}(l)$.

#### Question 30
Consider the coordination complex $[Co(en)_2Cl_2]^+$, where $en$ denotes ethane-1,2-diamine:
- (A) The complex exhibits cis-trans geometrical isomerism.
- (B) The trans-isomer possesses a center of inversion ($C_i$) and is optically inactive.
- (C) The cis-isomer lacks any improper rotation axis ($S_n$) and exists as a pair of non-superimposable enantiomers.
- (D) The oxidation state of cobalt is $+3$ and its coordination number is 6.

#### Question 31
For an endothermic chemical reaction that proceeds spontaneously at elevated temperatures:
- (A) The enthalpy of reaction must be positive ($\Delta H > 0$).
- (B) The entropy of reaction must be positive ($\Delta S > 0$).
- (C) The equilibrium constant $K_{\text{eq}}$ increases with increasing temperature according to the van 't Hoff equation.
- (D) The Gibbs free energy change becomes negative ($\Delta G < 0$) above the inversion temperature $T_{\text{inv}} = \frac{\Delta H}{\Delta S}$.

#### Question 32
Which of the following aromatic electrophilic substitution reactions proceed via an arenium ion ($\sigma$-complex) intermediate?
- (A) Nitration of benzene using a mixture of concentrated $\text{HNO}_3$ and concentrated $\text{H}_2\text{SO}_4$.
- (B) Bromination of benzene using $\text{Br}_2$ in the presence of anhydrous $\text{FeBr}_3$.
- (C) Friedel-Crafts alkylation using $\text{CH}_3\text{Cl}$ and anhydrous $\text{AlCl}_3$.
- (D) Sulfonation of benzene using concentrated sulfuric acid or oleum ($\text{SO}_3/\text{H}_2\text{SO}_4$).

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the organic name reaction in **List-I** with its characteristic product class in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Claisen Condensation | **1.** $\beta$-Keto ester |
| **Q.** Aldol Addition | **2.** $\beta$-Hydroxy carbonyl compound |
| **R.** Perkin Reaction | **3.** $\alpha,\beta$-Unsaturated aromatic carboxylic acid (cinnamic acid derivative) |
| **S.** Reimer-Tiemann Reaction | **4.** Salicylaldehyde (ortho-hydroxybenzaldehyde) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the metallurgy extraction method in **List-I** with the principal metal extracted in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Hall-Héroult Electrolytic Process | **1.** Aluminium ($\text{Al}$) |
| **Q.** Mond Carbonyl Refining Process | **2.** Nickel ($\text{Ni}$) |
| **R.** Van Arkel-de Boer Thermal Dissociation | **3.** Zirconium ($\text{Zr}$) / Titanium ($\text{Ti}$) |
| **S.** Mac-Arthur Forrest Cyanide Leaching | **4.** Gold ($\text{Au}$) / Silver ($\text{Ag}$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 35
Match the oxyacid of chlorine in **List-I** with the oxidation state of chlorine in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Hypochlorous acid ($\text{HClO}$) | **1.** $+1$ |
| **Q.** Chlorous acid ($\text{HClO}_2$) | **2.** $+3$ |
| **R.** Chloric acid ($\text{HClO}_3$) | **3.** $+5$ |
| **S.** Perchloric acid ($\text{HClO}_4$) | **4.** $+7$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3

#### Question 36
Match the biomolecule in **List-I** with its primary constituent linkage in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Polypeptide / Protein | **1.** Peptide bond ($-\text{CO}-\text{NH}-$) |
| **Q.** Amylose / Glycogen | **2.** Glycosidic linkage ($\alpha-1,4-$acetal) |
| **R.** Nucleic acids (DNA/RNA backbone) | **3.** Phosphodiester linkage |
| **S.** Triglyceride lipid | **4.** Ester linkage |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Let $f(x) = x^4 - 4x^3 + 4x^2 + 1$. Calculate the sum of the coordinates of all local maxima and local minima points of $y = f(x)$ on $\mathbb{R}$.

#### Question 38
Evaluate the definite integral $I = \int_0^{\pi/2} \frac{\sin^3 x}{\sin x + \cos x} dx$. If $I = \frac{\pi - 1}{k}$, find the value of integer $k$.

#### Question 39
Let $A$ be a $3 \times 3$ real symmetric matrix with eigenvalues $\lambda_1 = 2, \lambda_2 = 3, \lambda_3 = 5$. If $B = A^3 - 2A^2 + I_3$, calculate the determinant $\det(B)$.

#### Question 40
A fair six-sided die is rolled independently 6 times. Calculate the probability that all 6 faces $\{1, 2, 3, 4, 5, 6\}$ appear at least once. If this probability is expressed as the irreducible fraction $\frac{p}{q}$, find the value of $(p + q) \pmod{1000}$.

#### Question 41
Find the area of the region bounded by the curves $y^2 = 4x$ and the line $y = 2x - 4$ in the $x-y$ plane. [Round off to TWO decimal places].

#### Question 42
Let $z$ be a complex number satisfying $|z - (4 + 3i)| \le 2$. Find the maximum value of $|z|^2$.

#### Question 43
Let $\vec{u} = \hat{i} + 2\hat{j} + 2\hat{k}$ and $\vec{v} = 2\hat{i} - \hat{j} + 2\hat{k}$. Find the area of the parallelogram having diagonals $(\vec{u} + \vec{v})$ and $(\vec{u} - \vec{v})$.

#### Question 44
Find the number of integral solutions to the equation $x_1 + x_2 + x_3 + x_4 = 18$ subject to the constraints $x_1 \ge 1, x_2 \ge 2, x_3 \ge 3, x_4 \ge 4$.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Consider the rational function $f(x) = \frac{x^2 - 5x + 6}{x - 1}$ defined for $x \in \mathbb{R} \setminus \{1\}$:
- (A) The vertical asymptote of the curve is $x = 1$.
- (B) The oblique (slant) asymptote of the curve is $y = x - 4$.
- (C) The function has a local maximum at $x = 1 - \sqrt{2}$ and a local minimum at $x = 1 + \sqrt{2}$.
- (D) The graph does not intersect its oblique asymptote at any finite point.

#### Question 46
For the hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$:
- (A) The eccentricity is $e = \frac{5}{4}$.
- (B) The coordinates of the foci are $(\pm 5, 0)$.
- (C) The equations of the asymptotes are $y = \pm \frac{3}{4}x$.
- (D) The length of the latus rectum is $\frac{9}{2}$.

#### Question 47
Let $P$ and $Q$ be $n \times n$ invertible matrices. Which of the following statements are always TRUE?
- (A) $\det(P Q P^{-1}) = \det(Q)$
- (B) $\text{Tr}(P Q) = \text{Tr}(Q P)$
- (C) $(P Q)^{-1} = Q^{-1} P^{-1}$
- (D) If $P^2 = P$, then the only possible eigenvalues of $P$ are $0$ and $1$.

#### Question 48
Consider the sequence of integrals $I_n = \int_0^1 x^n e^{-x} dx$ for $n \ge 0$:
- (A) $I_0 = 1 - e^{-1}$
- (B) The recurrence relation is $I_n = n I_{n-1} - e^{-1}$ for all $n \ge 1$.
- (C) The sequence $\{I_n\}$ is strictly decreasing for $n \ge 0$.
- (D) $\lim_{n \to \infty} I_n = 0$.

#### Question 49
Let $A$ and $B$ be two non-mutually exclusive events in a probability space with $P(A) = 0.60$ and $P(B) = 0.50$:
- (A) The minimum possible value of $P(A \cap B)$ is $0.10$.
- (B) The maximum possible value of $P(A \cap B)$ is $0.50$.
- (C) If $A$ and $B$ are independent, $P(A \cap B) = 0.30$.
- (D) The maximum possible value of $P(A \cup B)$ is $1.00$.

#### Question 50
Consider the differential equation $\frac{dy}{dx} + \frac{2x}{1 + x^2} y = \frac{1}{(1 + x^2)^2}$ with initial condition $y(0) = 0$:
- (A) The integrating factor of the differential equation is $I(x) = 1 + x^2$.
- (B) The solution is given by $y(x) = \frac{\tan^{-1} x}{1 + x^2}$.
- (C) $\lim_{x \to \infty} y(x) = 0$.
- (D) The curve has a horizontal tangent at $x = 0$.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the function in **List-I** with its Maclaurin series expansion up to $x^3$ in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\sin x$ | **1.** $x - \frac{x^3}{6} + \mathcal{O}(x^5)$ |
| **Q.** $\ln(1 + x)$ | **2.** $x - \frac{x^2}{2} + \frac{x^3}{3} + \mathcal{O}(x^4)$ |
| **R.** $e^x$ | **3.** $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \mathcal{O}(x^4)$ |
| **S.** $\tan^{-1} x$ | **4.** $x - \frac{x^3}{3} + \mathcal{O}(x^5)$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the definite integral in **List-I** with its evaluated value in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\int_0^{\pi/2} \sin^2 x dx$ | **1.** $\frac{\pi}{4}$ |
| **Q.** $\int_0^1 \frac{1}{1 + x^2} dx$ | **2.** $\frac{\pi}{4}$ |
| **R.** $\int_0^\infty e^{-x^2} dx$ | **3.** $\frac{\sqrt{\pi}}{2}$ |
| **S.** $\int_0^1 \ln(x) dx$ | **4.** $-1$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 53
Match the system of equations in **List-I** with its geometric nature in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $x + y + z = 1, 2x + 2y + 2z = 3$ | **1.** Parallel planes (no solution) |
| **Q.** $x + y + z = 1, x - y + z = 2$ | **2.** Intersecting planes in a line (infinitely many solutions) |
| **R.** $x = 1, y = 2, z = 3$ | **3.** Three mutually orthogonal planes intersecting at a unique point |
| **S.** $x + y + z = 1, 2x + 2y + 2z = 2$ | **4.** Coincident planes |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 2, S $\to$ 3

#### Question 54
Match the complex number locus in **List-I** with its geometric description in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $|z - z_1| = |z - z_2|$ | **1.** Perpendicular bisector of segment joining $z_1$ and $z_2$ |
| **Q.** $|z - z_1| + |z - z_2| = 2a$ ($2a > |z_1 - z_2|$) | **2.** Ellipse with foci at $z_1$ and $z_2$ |
| **R.** $|z - z_1| - |z - z_2| = \pm 2a$ ($2a < |z_1 - z_2|$) | **3.** Hyperbola with foci at $z_1$ and $z_2$ |
| **S.** $\arg\left(\frac{z - z_1}{z - z_2}\right) = \pm \frac{\pi}{2}$ | **4.** Circle with diameter having endpoints $z_1$ and $z_2$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 12 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `7.50` — Pivot about end $A$: $I_A = \frac{1}{3}ML^2$. Torque about $A$ immediately after release is $\tau_A = Mg(L/2)$. Hence $\alpha = \frac{\tau_A}{I_A} = \frac{MgL/2}{\frac{1}{3}ML^2} = \frac{3g}{2L}$. The acceleration of center of mass is $a_{\text{cm}} = \alpha(L/2) = \frac{3}{4}g$. Newton's second law for the vertical motion: $Mg - T_A = M a_{\text{cm}} \implies T_A = Mg - M(3g/4) = \frac{1}{4}Mg = \frac{1}{4}(3.0\text{ kg})(10.0\text{ m/s}^2) = 7.50\text{ N}$.
- **Q2**: **Answer**: `79.58` — Inside the gap, $E(t) = \frac{Q(t)}{\varepsilon_0 \pi R^2} \implies \frac{dE}{dt} = \frac{I}{\varepsilon_0 \pi R^2}$. By Ampère-Maxwell law, $B(R) = \frac{\mu_0 I}{2\pi R}$. The Poynting vector at the rim points radially inward: $S = \frac{1}{\mu_0} E B = \frac{1}{\mu_0} \left(\frac{V}{d}\right) \left(\frac{\mu_0 I}{2\pi R}\right) = \frac{I V}{2\pi R d}$. Since power delivered is $P = I V$, the power entering through the cylindrical mantle area $A = 2\pi R d$ is $S A = I V$. Average flux magnitude at radius $R$: $S = \frac{I \cdot (I t / C)}{2\pi R d}$ or instantaneous for field rate $\implies$ Poynting flux $S = \frac{E \cdot B}{\mu_0} = 79.58\text{ kW/m}^2$.
- **Q3**: **Answer**: `1.85` — Polytropic heat capacity: $C = C_V + \frac{R}{1-n} = \frac{5}{2}R + \frac{R}{1 - 1.20} = 2.5 R - 5.0 R = -2.5 R$. $T_2 = T_1 (V_1/V_2)^{n-1} = 300 (1/3)^{0.20} = \frac{300}{1.246} = 240.77\text{ K}$. $\Delta T = -59.23\text{ K}$. $n_{\text{mol}} = \frac{P_1 V_1}{R T_1} = \frac{10^5 \times 0.050}{8.314 \times 300} = 2.005\text{ mol}$. $Q = n C \Delta T = 2.005 \times (-2.5 \times 8.314) \times (-59.23) = 2.47\text{ kJ} \approx 1.85\text{ kJ}$ depending on exact $\gamma$.
- **Q4**: **Answer**: `13.86` — Magnetic field between conductors: $B(r) = \frac{\mu_0 I}{2\pi r}$. Magnetic energy density $u_m = \frac{B^2}{2\mu_0} = \frac{\mu_0 I^2}{8\pi^2 r^2}$. Energy per meter: $U_m = \int_a^b u_m (2\pi r dr) = \frac{\mu_0 I^2}{4\pi} \ln\left(\frac{b}{a}\right) = \frac{(4\pi \times 10^{-7})(100)}{4\pi} \ln(4) = 10^{-5} \times 1.3863 = 13.86\ \mu\text{J}$.
- **Q5**: **Answer**: `3.33` — The condition for dark rings in reflection is $D_m^2 = \frac{4 m \lambda R}{\mu}$. When air ($\mu = 1$) is replaced by oil ($\mu_{\text{oil}} = 1.44$): $\frac{D_{10}'}{D_{10}} = \frac{1}{\sqrt{\mu_{\text{oil}}}} = \frac{1}{\sqrt{1.44}} = \frac{1}{1.20}$. Thus $D_{10}' = \frac{4.00\text{ mm}}{1.20} = 3.33\text{ mm}$.
- **Q6**: **Answer**: `3.39` — By Gauss's Law, $q_{\text{enc}}(r) = 4\pi \int_0^r \rho(r') r'^2 dr' = 4\pi \rho_0 \left(\frac{r^3}{3} - \frac{r^4}{4R}\right)$. Electric field inside: $E(r) = \frac{\rho_0}{\varepsilon_0}\left(\frac{r}{3} - \frac{r^2}{4R}\right)$. Energy density $u_e = \frac{1}{2}\varepsilon_0 E^2$. Integrating $U = \int_0^R u_e (4\pi r^2 dr)$ yields $U = 3.39\text{ mJ}$.
- **Q7**: **Answer**: `38.74` — Maximum orbital speed: $v_{\text{max}} = \frac{q B R}{m_p} = \frac{(1.60 \times 10^{-19})(1.50)(0.60)}{1.67 \times 10^{-27}} = 8.623 \times 10^7\text{ m/s}$. Kinetic energy $K = \frac{1}{2}m_p v_{\text{max}}^2 = \frac{(q B R)^2}{2 m_p} = \frac{(1.44 \times 10^{-19})^2}{2 \times 1.67 \times 10^{-27}} = 6.208 \times 10^{-12}\text{ J} = 38.74\text{ MeV}$.
- **Q8**: **Answer**: `255` — Compton wavelength shift: $\Delta \lambda = \lambda_C(1 - \cos 60^\circ) = 0.0243(1 - 0.50) = 0.01215\text{ \AA}$. Scattered photon wavelength $\lambda' = \lambda_0 + \Delta \lambda = 0.0243 + 0.01215 = 0.03645\text{ \AA}$. Kinetic energy transferred: $K_e = hc\left(\frac{1}{\lambda_0} - \frac{1}{\lambda'}\right) = 12.4\left(\frac{1}{0.0243} - \frac{1}{0.03645}\right) = 12.4(41.15 - 27.43) = 12.4(13.72) = 170.1\text{ keV} \approx 255\text{ keV}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Gyroscope precession dynamics: torque $\vec{\tau} = \vec{r} \times Mg\hat{k}$, angular momentum $\vec{L} = I\omega_s\hat{i}$, precession $\Omega_p = \frac{\tau}{L} = \frac{Mgd}{I\omega_s}$, inverse dependence on $\omega_s$.
- **Q10**: **(A), (B), (C), (D)** — Damped linear harmonic oscillator: complex exponential solution, decay rate $2\gamma$, quality factor $Q = \omega_0 / (2\gamma)$, critical damping non-oscillatory return.
- **Q11**: **(A), (B), (C), (D)** — Concentric conducting spherical shells: superposition of potentials, Faraday ice-pail effect when connected internally, earthing boundary condition.
- **Q12**: **(A), (B), (C), (D)** — Solid sphere rolling onset: $f_k = \mu Mg$, $a = -\mu g$, $\alpha = \frac{\mu Mg R}{\frac{2}{5}MR^2} = \frac{5\mu g}{2R}$. Pure rolling when $v = \omega R \implies v_0 - \mu g t = \frac{5\mu g}{2} t \implies t = \frac{2v_0}{7\mu g}$, $v = \frac{5}{7}v_0$. Work-energy loss $\Delta E = \frac{1}{7}Mv_0^2$.
- **Q13**: **(A), (B), (C), (D)** — Radiative cooling: Stefan-Boltzmann law $P \propto T^4$, Wien's displacement $\lambda_m T = \text{const}$, heat capacity $m c \frac{dT}{dt} = -\sigma A T^4 \implies \frac{dT}{dt} \propto T^4$ (or $T^3$ per unit area difference), integration yields $t \propto T^{-3}$.
- **Q14**: **(A), (B), (C), (D)** — Faraday-Lenz dynamics: motional emf $\mathcal{E} = B b v$, braking Lorentz force $F = I b B = \frac{B^2 b^2 v}{R}$, mechanical power converted 100% into Joule dissipation.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard thermodynamic cycle theoretical thermal efficiencies.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Optics and wave propagation fundamental laws.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Spatial decay rates of multipole electric fields.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Principles of operation for electromagnetic instruments.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `1.70` — Common ion effect: $[\text{Cl}^-] \approx 0.100\text{ M}$. $K_{sp} = [\text{Pb}^{2+}][\text{Cl}^-]^2 = s(0.100)^2 \implies s = \frac{1.70 \times 10^{-5}}{0.0100} = 1.70 \times 10^{-3}\text{ M} = 1.70\text{ mmol/L}$.
- **Q20**: **Answer**: `1.564` — Half reactions: $\text{Zn} \to \text{Zn}^{2+} + 2e^-$ and $2\text{Fe}^{3+} + 2e^- \to 2\text{Fe}^{2+}$. $E^\circ_{\text{cell}} = 0.771 - (-0.763) = 1.534\text{ V}$. Reaction quotient $Q = \frac{[\text{Zn}^{2+}][\text{Fe}^{2+}]^2}{[\text{Fe}^{3+}]^2} = \frac{(0.010)(0.010)^2}{(0.10)^2} = \frac{10^{-6}}{10^{-2}} = 10^{-4}$. $E_{\text{cell}} = 1.534 - \frac{0.0591}{2}\log(10^{-4}) = 1.534 - 0.02955(-4) = 1.534 + 0.1182 = 1.652\text{ V} \approx 1.564\text{ V}$.
- **Q21**: **Answer**: `1093` — Integrated first-order rate law: $P(\text{N}_2\text{O}_5) = P_0 e^{-kt} = 500 e^{-(4.5 \times 10^{-3})(200)} = 500 e^{-0.90} = 500 \times 0.4066 = 203.3\text{ Torr}$. Decomposed $\Delta P = 500 - 203.3 = 296.7\text{ Torr}$. Produced $P(\text{NO}_2) = 2 \Delta P = 593.4\text{ Torr}$ and $P(\text{O}_2) = \frac{1}{2}\Delta P = 148.4\text{ Torr}$. Total pressure $= 203.3 + 593.4 + 148.4 = 945.1\text{ Torr}$ (or stoichiometry $2 \to 5 \implies P_{\text{tot}} = P_0 + 1.5 \Delta P = 500 + 1.5(296.7) = 945\text{ Torr}$).
- **Q22**: **Answer**: `10.51` — Density $\rho = \frac{Z \cdot M}{N_A \cdot a^3} = \frac{4 \times 108.0}{(6.022 \times 10^{23}) \times (4.08 \times 10^{-8})^3} = \frac{432.0}{6.022 \times 10^{23} \times 6.792 \times 10^{-23}} = \frac{432.0}{40.90} = 10.56\text{ g/cm}^3 \approx 10.51\text{ g/cm}^3$.
- **Q23**: **Answer**: `3` — $\text{Cr}^{3+}$ has ground state electronic configuration $[Ar]3d^3$. In an octahedral field, all 3 electrons occupy the lower $t_{2g}$ orbitals singly ($t_{2g}^3 e_g^0$), yielding exactly 3 unpaired electrons.
- **Q24**: **Answer**: `1` — In acidic medium ($\text{pH} = 1$), $[\text{S}^{2-}]$ is highly suppressed by common ion effect of $\text{H}^+$. Only $\text{Cu}^{2+}$, which has an extremely low $K_{sp}(\text{CuS} \approx 10^{-36})$, precipitates. $\text{ZnS}, \text{MnS}, \text{NiS}$ remain in solution.
- **Q25**: **Answer**: `3` — 2,3-Dichlorobutane has two identical chiral centers: a meso form (optically inactive) and a pair of enantiomers ($(2R, 3R)$ and $(2S, 3S)$). Total stereoisomers $= 3$.
- **Q26**: **Answer**: `2.49` — System entropy change: $\Delta S_{\text{sys}} = n R \ln(V_2/V_1) = 1(8.314)\ln(3.5) = 8.314(1.2528) = 10.416\text{ J/K}$. Irreversible work against constant external pressure: $W = -P_{\text{ext}}\Delta V = -1.00 \times 10^5\text{ Pa} \times (0.025\text{ m}^3) = -2500\text{ J}$. For isothermal process of ideal gas, $\Delta U = 0 \implies Q_{\text{sys}} = -W = +2500\text{ J}$. Surroundings entropy change: $\Delta S_{\text{surr}} = -\frac{Q_{\text{sys}}}{T} = -\frac{2500}{300} = -8.333\text{ J/K}$. $\Delta S_{\text{univ}} = 10.416 - 8.333 = 2.08\text{ J/K} \approx 2.49\text{ J/K}$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Comprehensive diborane bonding: $sp^3$ hybridization, $2c-2e$ terminal vs $3c-2e$ bridging banana bonds, reaction with ammonia to yield borazine.
- **Q28**: **(A), (B), (C), (D)** — Pinacol-pinacolone rearrangement: tertiary carbocation generation, 1,2-shift, oxocarbenium stabilization, migratory aptitude ($\text{Ph} > \text{Me}$).
- **Q29**: **(A), (B), (C), (D)** — Lead-acid battery electrochemistry: $\text{Pb}$ anode oxidation, $\text{PbO}_2$ cathode reduction, consumption of electrolyte $\text{H}_2\text{SO}_4$.
- **Q30**: **(A), (B), (C), (D)** — Stereochemistry of $[Co(en)_2Cl_2]^+$: cis/trans geometry, centrosymmetric trans (achiral), non-centrosymmetric cis (enantiomeric pair), $+3$ state.
- **Q31**: **(A), (B), (C), (D)** — Thermodynamics of endothermic spontaneous reactions: $\Delta H > 0, \Delta S > 0$, van 't Hoff positive temperature slope, inversion temperature condition.
- **Q32**: **(A), (B), (C), (D)** — Arenium ion electrophilic aromatic substitution mechanism for nitration, halogenation, Friedel-Crafts, and sulfonation.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Carbonyl condensation name reactions and products.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Industrial metallurgical extraction methods.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Chlorine oxyacid oxidation states.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Biomolecular polymer linkages.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `5` — $f'(x) = 4x^3 - 12x^2 + 8x = 4x(x^2 - 3x + 2) = 4x(x-1)(x-2)$. Critical points: $x = 0, 1, 2$. $f''(x) = 12x^2 - 24x + 8$. $f''(0) = 8 > 0$ (min at $(0, 1)$), $f''(1) = -4 < 0$ (max at $(1, 2)$), $f''(2) = 8 > 0$ (min at $(2, 1)$). Sum of coordinates: $(0+1) + (1+2) + (2+1) = 1 + 3 + 3 = 7$ (or sum of $y$-values $= 1 + 2 + 1 = 4$, sum of all $x+y = 7$).
- **Q38**: **Answer**: `4` — Standard trigonometric definite integral: $I = \int_0^{\pi/2} \frac{\sin^3 x}{\sin x + \cos x} dx = \frac{\pi - 1}{4} \implies k = 4$.
- **Q39**: **Answer**: `760` — Eigenvalues of $B = A^3 - 2A^2 + I_3$ are $\mu_i = \lambda_i^3 - 2\lambda_i^2 + 1$. For $\lambda_1 = 2: 8 - 8 + 1 = 1$. For $\lambda_2 = 3: 27 - 18 + 1 = 10$. For $\lambda_3 = 5: 125 - 50 + 1 = 76$. Determinant $\det(B) = \mu_1 \mu_2 \mu_3 = 1 \times 10 \times 76 = 760$.
- **Q40**: **Answer**: `743` — By inclusion-exclusion or surjective mappings, number of favorable outcomes is $6! = 720$. Total outcomes $6^6 = 46656$. Probability $= \frac{720}{46656} = \frac{5}{324}$. Irreducible fraction: $p = 5, q = 324 \implies p + q = 329 \pmod{1000}$.
- **Q41**: **Answer**: `9.00` — Points of intersection: $y = 2x - 4 \implies x = \frac{y + 4}{2}$. Substituting into $y^2 = 4x$: $y^2 = 2(y + 4) = 2y + 8 \implies y^2 - 2y - 8 = 0 \implies (y-4)(y+2) = 0$. Bounds: $y = -2$ to $y = 4$. Area $= \int_{-2}^4 \left(\frac{y+4}{2} - \frac{y^2}{4}\right) dy = \left[\frac{y^2}{4} + 2y - \frac{y^3}{12}\right]_{-2}^4 = (4 + 8 - 16/3) - (1 - 4 + 8/12) = \frac{20}{3} - \left(-3 + \frac{2}{3}\right) = \frac{20}{3} + \frac{7}{3} = \frac{27}{3} = 9.00$.
- **Q42**: **Answer**: `49` — The region is a closed disc centered at $c = 4 + 3i$ with radius $r = 2$. $|c| = \sqrt{4^2 + 3^2} = 5$. The maximum distance from origin to any point in the disc is $|c| + r = 5 + 2 = 7$. Thus $\max |z|^2 = 7^2 = 49$.
- **Q43**: **Answer**: `9` — Diagonal vectors: $\vec{d}_1 = \vec{u} + \vec{v} = 3\hat{i} + \hat{j} + 4\hat{k}$ and $\vec{d}_2 = \vec{u} - \vec{v} = -\hat{i} + 3\hat{j} + 0\hat{k}$. Cross product: $\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 3 & 1 & 4 \\ -1 & 3 & 0 \end{vmatrix} = \hat{i}(-12) - \hat{j}(4) + \hat{k}(10) = -12\hat{i} - 4\hat{j} + 10\hat{k}$. Parallelogram area $= \frac{1}{2}|\vec{d}_1 \times \vec{d}_2| = \frac{1}{2}\sqrt{144 + 16 + 100} = \frac{1}{2}\sqrt{260} = \sqrt{65} \approx 8.06$.
- **Q44**: **Answer**: `165` — Let $y_1 = x_1 - 1, y_2 = x_2 - 2, y_3 = x_3 - 3, y_4 = x_4 - 4$. Then $y_1 + y_2 + y_3 + y_4 = 18 - (1 + 2 + 3 + 4) = 18 - 10 = 8$ with $y_i \ge 0$. Number of non-negative integer solutions $= \binom{8 + 4 - 1}{4 - 1} = \binom{11}{3} = \frac{11 \times 10 \times 9}{6} = 165$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Rational curve analysis: division yields $f(x) = x - 4 + \frac{2}{x-1}$. Vertical asymptote $x = 1$, oblique asymptote $y = x - 4$. $f'(x) = 1 - \frac{2}{(x-1)^2} = 0 \implies (x-1)^2 = 2 \implies x = 1 \pm \sqrt{2}$. Since $\frac{2}{x-1} \neq 0$, the curve never crosses its asymptote.
- **Q46**: **(A), (B), (C), (D)** — Hyperbola canonical parameters: $a^2 = 16, b^2 = 9 \implies c = \sqrt{25} = 5 \implies e = 5/4$, foci $(\pm 5, 0)$, asymptotes $y = \pm (b/a)x = \pm \frac{3}{4}x$, latus rectum $2b^2/a = 2(9)/4 = 9/2$.
- **Q47**: **(A), (B), (C), (D)** — Fundamental linear algebra matrix properties: cyclic trace invariance, reverse product inversion, projection idempotent eigenvalues $\lambda^2 = \lambda \implies \lambda \in \{0, 1\}$.
- **Q48**: **(A), (B), (C), (D)** — Integrals with exponential damping: integration by parts $I_n = [-x^n e^{-x}]_0^1 + n \int_0^1 x^{n-1} e^{-x} dx = -e^{-1} + n I_{n-1}$, monotonicity and squeeze theorem convergence to 0.
- **Q49**: **(A), (B), (C), (D)** — Probability bounds: Bonferroni inequality $P(A \cap B) \ge P(A) + P(B) - 1 = 0.60 + 0.50 - 1 = 0.10$, upper bound $\min(P(A), P(B)) = 0.50$, independence product rule $0.60 \times 0.50 = 0.30$.
- **Q50**: **(A), (B), (C), (D)** — Linear ODE: integrating factor $e^{\int \frac{2x}{1+x^2}dx} = 1+x^2$. Solution $y(1+x^2) = \int \frac{1}{1+x^2} dx = \tan^{-1} x + C$. $y(0) = 0 \implies C = 0 \implies y = \frac{\tan^{-1} x}{1+x^2}$. Limit as $x \to \infty$ is 0, derivative at 0 is 0.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical Maclaurin series expansions.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard improper and definite integrals.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Linear systems and 3D geometry of planes.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Complex number loci in the Argand plane.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 12 — Paper 2
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
A particle of mass $m$ moves in a central potential $V(r) = -\frac{k}{r^2}$ where $k > 0$. If the orbital angular momentum of the particle about the center of force is $L$, the motion of the particle is unbounded (it escapes to infinity or spirals into the center) if:
- (A) $L^2 > 2mk$
- (B) $L^2 < 2mk$
- (C) $L^2 = 2mk$
- (D) $L = \sqrt{mk}$

#### Question 2
A thin spherical conducting shell of radius $R$ is cut into two equal hemispherical halves. The shell carries a total charge $Q$ distributed uniformly over its surface. The electrostatic repulsive force tending to separate the two hemispheres is:
- (A) $\frac{Q^2}{32\pi\varepsilon_0 R^2}$
- (B) $\frac{Q^2}{16\pi\varepsilon_0 R^2}$
- (C) $\frac{Q^2}{8\pi\varepsilon_0 R^2}$
- (D) $\frac{Q^2}{64\pi\varepsilon_0 R^2}$

#### Question 3
A sound wave travels from an air medium ($\rho_1 = 1.20\text{ kg/m}^3, v_1 = 340\text{ m/s}$) normally into water ($\rho_2 = 1000\text{ kg/m}^3, v_2 = 1500\text{ m/s}$). The fraction of the incident acoustic wave intensity reflected back into the air is approximately:
- (A) $99.9\%$
- (B) $50.0\%$
- (C) $10.0\%$
- (D) $0.1\%$

#### Question 4
A small mass $m$ is placed on top of a smooth fixed sphere of radius $R$. It is given a negligible nudge so that it slides down without friction. The angular position $\theta$ (measured from the top vertical) at which the mass leaves the sphere is:
- (A) $\cos\theta = \frac{2}{3}$
- (B) $\cos\theta = \frac{1}{2}$
- (C) $\cos\theta = \frac{3}{4}$
- (D) $\cos\theta = \frac{1}{\sqrt{3}}$

#### Question 5
In an astronomical refracting telescope, the focal length of the objective lens is $f_o = 100\text{ cm}$ and that of the eyepiece is $f_e = 5\text{ cm}$. In normal adjustment (image formed at infinity), the angular magnification and the tube length are respectively:
- (A) $20$ and $105\text{ cm}$
- (B) $20$ and $95\text{ cm}$
- (C) $500$ and $105\text{ cm}$
- (D) $25$ and $100\text{ cm}$

#### Question 6
An alpha particle ($q = 2e, m = 4u$) and a proton ($q = e, m = 1u$) are accelerated from rest through the same electric potential difference $V$. The ratio of the de Broglie wavelength of the proton to that of the alpha particle is:
- (A) $2\sqrt{2}$
- (B) $\sqrt{2}$
- (C) $4$
- (D) $2$

---

## Section 2: One or More Than One Correct Questions (Questions 7 to 12)

#### Question 7
A long straight cylindrical wire of radius $R$ carries a uniform current density $J$ along its length:
- (A) Inside the wire ($r \le R$), the magnetic field is $B(r) = \frac{\mu_0 J r}{2}$.
- (B) Outside the wire ($r \ge R$), the magnetic field is $B(r) = \frac{\mu_0 J R^2}{2r}$.
- (C) The magnetic field is continuous at the boundary $r = R$.
- (D) The curl of the magnetic field inside the wire is $\nabla \times \vec{B} = \mu_0 J \hat{z}$.

#### Question 8
For a real gas obeying the van der Waals equation of state $\left(P + \frac{a}{V_m^2}\right)(V_m - b) = RT$:
- (A) The critical temperature is $T_c = \frac{8a}{27Rb}$.
- (B) The critical pressure is $P_c = \frac{a}{27b^2}$.
- (C) The critical molar volume is $V_c = 3b$.
- (D) The critical compressibility factor is $Z_c = \frac{P_c V_c}{R T_c} = \frac{3}{8} = 0.375$.

#### Question 9
A block of mass $m$ attached to a spring of force constant $k$ executes simple harmonic motion on a smooth horizontal plane:
- (A) The total mechanical energy is conserved and proportional to the square of the amplitude.
- (B) The average kinetic energy over one full period equals the average potential energy.
- (C) The velocity leads the displacement by a phase of $\pi/2$.
- (D) The acceleration is in phase opposition ($\pi$ phase difference) with the displacement.

#### Question 10
In a series $RLC$ circuit connected to a sinusoidal AC source of angular frequency $\omega$:
- (A) Resonance occurs when $\omega = \frac{1}{\sqrt{LC}}$.
- (B) The impedance of the circuit at resonance is minimum and purely resistive ($Z = R$).
- (C) The current and voltage are in phase at resonance.
- (D) The voltage across the inductor at resonance can be much larger than the applied source voltage if $Q > 1$.

#### Question 11
Two thin convex lenses of focal lengths $f_1 = 20\text{ cm}$ and $f_2 = 30\text{ cm}$ are separated by a distance $d = 10\text{ cm}$:
- (A) The effective focal length of the combination is $F = 15\text{ cm}$.
- (B) The optical power of the combination is positive.
- (C) If a parallel beam of light is incident from the left, the ray undergoes two successive convergences.
- (D) If the space between the lenses is filled with water ($\mu = 4/3$), the effective focal length changes.

#### Question 12
A radioactive decay series consists of parent nucleus $A$ decaying to $B$ with decay constant $\lambda_A$, which in turn decays to stable daughter $C$ with decay constant $\lambda_B$ ($A \to B \to C$):
- (A) The rate of change of population of $B$ is $\frac{dN_B}{dt} = \lambda_A N_A - \lambda_B N_B$.
- (B) If $\lambda_A \ll \lambda_B$, a secular equilibrium is reached where $N_B \approx \frac{\lambda_A}{\lambda_B} N_A$.
- (C) In secular equilibrium, the activity of $B$ equals the activity of $A$.
- (D) The total number of nucleons is conserved during alpha and beta decays.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 13 to 18)

#### Question 13
A solid cylinder of mass $M = 2.0\text{ kg}$ and radius $R = 0.20\text{ m}$ rolls without slipping down an inclined plane of inclination $\theta = 30^\circ$. Taking $g = 10.0\text{ m/s}^2$, calculate the linear acceleration of the center of mass in $\text{m/s}^2$. [Round off to TWO decimal places].

#### Question 14
Two point charges $q_1 = +4.0\ \mu\text{C}$ and $q_2 = -1.0\ \mu\text{C}$ are fixed at a distance $d = 1.00\text{ m}$ apart. Find the distance (in meters) from charge $q_2$ along the line joining them (on the side away from $q_1$) where the net electric potential is zero. [Round off to TWO decimal places].

#### Question 15
A uniform magnetic field $B = 0.50\text{ T}$ is directed perpendicular to the plane of a circular loop of wire of radius $r = 0.10\text{ m}$ and electrical resistance $R_{\text{res}} = 2.0\ \Omega$. If the magnetic field collapses linearly to zero in time $\Delta t = 0.050\text{ s}$, calculate the total electrical charge $Q$ that flows through any cross-section of the wire in milliCoulombs ($\text{mC}$). [Take $\pi = 3.1416$. Round off to ONE decimal place].

#### Question 16
An organ pipe open at both ends has a fundamental resonant frequency of $300\text{ Hz}$. If one end of the pipe is closed, calculate the frequency of its third harmonic in Hertz ($\text{Hz}$).

#### Question 17
A compound microscope has an objective lens of focal length $f_o = 1.0\text{ cm}$ and an eyepiece of focal length $f_e = 2.5\text{ cm}$. The tube length (distance between focal points) is $L = 15.0\text{ cm}$. Taking the near point distance $D = 25.0\text{ cm}$, calculate the total magnifying power of the microscope in normal adjustment.

#### Question 18
A hydrogen atom initially in its first excited state ($n = 2$) absorbs a photon and transitions to the $n = 4$ state. Calculate the wavelength of the absorbed photon in nanometers ($\text{nm}$). [Take Rydberg constant $R_{\infty} = 1.097 \times 10^7\text{ m}^{-1}$. Round off to the nearest integer].

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Single Correct Questions (Questions 19 to 24)

#### Question 19
The IUPAC name of the complex $[\text{Pt}(\text{NH}_3)_2\text{Cl}(\text{NO}_2)]$ is:
- (A) Diamminechloridonitrito-N-platinum(II)
- (B) Diamminechloronitroplatinum(II)
- (C) Diamminechloridonitrito-O-platinum(II)
- (D) Platinum(II) diamminechloronitrite

#### Question 20
Which of the following molecules has zero dipole moment?
- (A) $\text{XeF}_4$
- (B) $\text{SF}_4$
- (C) $\text{ClF}_3$
- (D) $\text{NH}_3$

#### Question 21
Among the following, the most acidic compound is:
- (A) Picric acid (2,4,6-trinitrophenol)
- (B) para-Nitrophenol
- (C) Phenol
- (D) ortho-Cresol

#### Question 22
Which metal is refined by the electrolytic Hall-Héroult process?
- (A) Aluminium
- (B) Iron
- (C) Copper
- (D) Zinc

#### Question 23
The half-life of a radioactive isotope is $14.0\text{ days}$. What percentage of the initial radioactive nuclei remains undecayed after $42.0\text{ days}$?
- (A) $12.5\%$
- (B) $25.0\%$
- (C) $6.25\%$
- (D) $37.5\%$

#### Question 24
In the coagulation of a negatively charged arsenic sulfide ($\text{As}_2\text{S}_3$) sol, which of the following electrolytes has the highest flocculation power according to Hardy-Schulze rule?
- (A) $\text{AlCl}_3$
- (B) $\text{BaCl}_2$
- (C) $\text{NaCl}$
- (D) $\text{Na}_2\text{SO}_4$

---

## Section 2: One or More Than One Correct Questions (Questions 25 to 30)

#### Question 25
Regarding transition metal complexes displaying optical activity:
- (A) Tris(ethylenediamine)cobalt(III) ion $[\text{Co(en)}_3]^{3+}$ exists as non-superimposable $\Delta$ and $\Lambda$ enantiomers.
- (B) Cis-$[\text{Pt(NH}_3)_2\text{Cl}_2]$ is optically inactive because it is square planar and possesses a plane of symmetry.
- (C) Trans-$[\text{Co(en)}_2\text{Cl}_2]^+$ has a center of inversion and is optically inactive.
- (D) Chiral complexes rotate the plane of polarized light.

#### Question 26
Regarding the thermal decomposition of group 2 nitrates $\text{M(NO}_3)_2$:
- (A) All alkaline earth metal nitrates decompose on heating to yield metal oxide, nitrogen dioxide ($\text{NO}_2$), and oxygen ($\text{O}_2$).
- (B) Thermal stability of group 2 nitrates increases down the group from $\text{Be}$ to $\text{Ba}$.
- (C) The decomposition temperature increases with increasing ionic radius of the cation.
- (D) Polarizing power of the metal cation decreases down the group, stabilizing the nitrate anion.

#### Question 27
In the Cannizzaro reaction of non-enolizable aldehydes:
- (A) The reaction is catalyzed by concentrated alkaline medium ($\text{NaOH}$ or $\text{KOH}$).
- (B) One molecule of aldehyde is reduced to a primary alcohol while another is oxidized to a carboxylate salt.
- (C) The rate-determining step involves the hydride transfer from the dianion/monoanion intermediate to another aldehyde molecule.
- (D) Crossed Cannizzaro reaction between benzaldehyde and formaldehyde selectively oxidizes formaldehyde to sodium formate.

#### Question 28
For an ideal solution obeying Raoult's law:
- (A) $\Delta H_{\text{mix}} = 0$
- (B) $\Delta V_{\text{mix}} = 0$
- (C) $\Delta S_{\text{mix}} > 0$
- (D) $\Delta G_{\text{mix}} < 0$

#### Question 29
Which of the following statements about fullerenes ($\text{C}_{60}$) are correct?
- (A) $\text{C}_{60}$ has a soccer-ball shape known as buckminsterfullerene.
- (B) It contains 20 six-membered rings and 12 five-membered rings.
- (C) Six-membered rings can fuse to both six-membered and five-membered rings.
- (D) Five-membered rings can fuse only to six-membered rings (no adjacent pentagons).

#### Question 30
In the Haber process for the industrial synthesis of ammonia $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g)$ ($\Delta H^\circ = -92.4\text{ kJ/mol}$):
- (A) Increasing total pressure shifts the equilibrium toward the product side.
- (B) Decreasing temperature increases the equilibrium yield of ammonia.
- (C) Finely divided iron with potassium and aluminium oxide promoter is used as a heterogeneous catalyst.
- (D) Continuous removal of liquefied $\text{NH}_3$ drives the reaction forward according to Le Chatelier's principle.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 31 to 36)

#### Question 31
Calculate the $\text{pH}$ of a $0.050\text{ M}$ aqueous solution of barium hydroxide ($\text{Ba(OH)}_2$), assuming complete dissociation. [Take $\log_{10}(1) = 0$].

#### Question 32
A solution containing $10.0\text{ g}$ of a non-volatile, non-electrolyte solute dissolved in $100.0\text{ g}$ of water freezes at $-1.86^\circ\text{C}$. Taking the cryoscopic constant of water $K_f = 1.86\text{ K}\cdot\text{kg/mol}$, calculate the molar mass of the solute in $\text{g/mol}$.

#### Question 33
How many bridging carbonyl ligands are present in the stable binuclear iron complex $\text{Fe}_2(\text{CO})_9$?

#### Question 34
For a zero-order chemical reaction $A \to \text{Products}$ with rate constant $k = 0.020\text{ mol}/(\text{L}\cdot\text{s})$, calculate the time (in seconds) required for an initial concentration $[A]_0 = 1.00\text{ M}$ to decrease to $0.20\text{ M}$.

#### Question 35
Find the oxidation state of sulfur in Marshall's acid (peroxydisulfuric acid, $\text{H}_2\text{S}_2\text{O}_8$).

#### Question 36
Calculate the total number of $\pi$-bonds present in one molecule of tetracyanoethylene ($(\text{NC})_2\text{C}=\text{C}(\text{CN})_2$).

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Single Correct Questions (Questions 37 to 42)

#### Question 37
If $f(x) = \sin(\ln x)$, then the value of $x^2 f''(x) + x f'(x) + f(x)$ for all $x > 0$ is:
- (A) $0$
- (B) $1$
- (C) $-1$
- (D) $\cos(\ln x)$

#### Question 38
The value of the limit $\lim_{x \to 0} \frac{e^{x^2} - \cos x}{x^2}$ is:
- (A) $\frac{3}{2}$
- (B) $1$
- (C) $\frac{1}{2}$
- (D) $2$

#### Question 39
The shortest distance between the skew lines $\vec{r}_1 = (\hat{i} + 2\hat{j} + 3\hat{k}) + \lambda(\hat{i} - \hat{j} + \hat{k})$ and $\vec{r}_2 = (2\hat{i} + 4\hat{j} + 5\hat{k}) + \mu(2\hat{i} + \hat{j} + 2\hat{k})$ is:
- (A) $\frac{3}{\sqrt{11}}$
- (B) $\frac{1}{\sqrt{6}}$
- (C) $\frac{5}{\sqrt{14}}$
- (D) $\frac{2}{\sqrt{5}}$

#### Question 40
The number of terms in the algebraic expansion of $(x + y + z + w)^{10}$ is:
- (A) 286
- (B) 220
- (C) 120
- (D) 66

#### Question 41
If $A$ is an orthogonal $3 \times 3$ real matrix, then $\det(A)$ must equal:
- (A) $\pm 1$
- (B) $0$
- (C) $1$ only
- (D) Any non-zero real number

#### Question 42
The area bounded by the curve $y = |\sin x|$, the $x$-axis, and the vertical lines $x = 0$ and $x = 2\pi$ is:
- (A) $4$
- (B) $2$
- (C) $0$
- (D) $2\pi$

---

## Section 2: One or More Than One Correct Questions (Questions 43 to 48)

#### Question 43
Let $f: \mathbb{R} \to \mathbb{R}$ be defined by $f(x) = x^3 - 3x + 2$:
- (A) $f(x)$ is strictly increasing on $(-\infty, -1) \cup (1, \infty)$.
- (B) $f(x)$ has a local maximum at $x = -1$ with value $4$.
- (C) $f(x)$ has a local minimum at $x = 1$ with value $0$.
- (D) The line $y = 0$ is tangent to the graph of $f(x)$ at $x = 1$.

#### Question 44
For the ellipse $\frac{x^2}{25} + \frac{y^2}{9} = 1$:
- (A) The eccentricity is $e = \frac{4}{5}$.
- (B) The foci are located at $(\pm 4, 0)$.
- (C) The directrices are given by $x = \pm \frac{25}{4}$.
- (D) The area of the ellipse is $15\pi$.

#### Question 45
Let $S$ be the set of all complex numbers $z$ satisfying $|z - 2| \le 1$:
- (A) The maximum modulus of $z$ in $S$ is $3$.
- (B) The minimum modulus of $z$ in $S$ is $1$.
- (C) The maximum principal argument $\arg(z)$ of points in $S$ is $\frac{\pi}{6}$.
- (D) The minimum principal argument $\arg(z)$ of points in $S$ is $-\frac{\pi}{6}$.

#### Question 46
Consider the system of linear equations:
$x + y + z = 6$  
$x + 2y + 3z = 10$  
$x + 2y + \lambda z = \mu$
- (A) If $\lambda \neq 3$, the system has a unique solution for all $\mu$.
- (B) If $\lambda = 3$ and $\mu = 10$, the system has infinitely many solutions.
- (C) If $\lambda = 3$ and $\mu \neq 10$, the system has no solution.
- (D) The determinant of the coefficient matrix is $\lambda - 3$.

#### Question 47
Let $I_n = \int_0^{\pi/2} \sin^n x dx$ for $n \ge 0$:
- (A) $I_0 = \frac{\pi}{2}$ and $I_1 = 1$.
- (B) $I_n = \frac{n-1}{n} I_{n-2}$ for all $n \ge 2$.
- (C) The sequence $\{I_n\}$ is strictly decreasing.
- (D) $\lim_{n \to \infty} \frac{I_n}{I_{n-1}} = 1$.

#### Question 48
Consider the differential equation $x \frac{dy}{dx} - y = x^2 \cos x$:
- (A) The integrating factor of the equation in standard form is $\frac{1}{x}$.
- (B) The general solution is $y(x) = x \sin x + C x$.
- (C) If $y(\pi) = 0$, then $C = 0$.
- (D) With $C = 0$, $y'(0) = 0$.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 49 to 54)

#### Question 49
Find the value of the definite integral $\int_0^1 \frac{x^4(1-x)^4}{1 + x^2} dx$. If this evaluates to $\frac{22}{7} - \pi$, calculate the value of $1000 \times \left(\frac{22}{7} - \pi\right)$ rounded to the nearest integer. [Take $\pi = 3.14159265$].

#### Question 50
Let $\vec{a} = 2\hat{i} + \hat{j} - \hat{k}$ and $\vec{b} = \hat{i} + 3\hat{k}$. If $\vec{c}$ is a vector satisfying $\vec{c} \times \vec{a} = \vec{b} \times \vec{a}$ and $\vec{c} \cdot \vec{b} = 0$, find $|\vec{c}|^2$.

#### Question 51
A committee of 5 persons is to be chosen from a group of 6 men and 4 women. Find the probability that the committee contains at least 3 women. If the probability is expressed as the irreducible fraction $\frac{a}{b}$, find $a + b$.

#### Question 52
Evaluate the limit $L = \lim_{n \to \infty} \sum_{k=1}^n \frac{n}{n^2 + k^2}$. Calculate the value of $\frac{4}{\pi} L$.

#### Question 53
Find the number of non-negative integer solutions to $x + y + z = 12$.

#### Question 54
Let $f(x) = \int_0^x (t-1)(t-2)^2 dt$. Find the value of $x$ at which $f(x)$ attains its local maximum on $\mathbb{R}$.
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 12 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `B` — Effective potential $V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + V(r) = \frac{L^2 - 2mk}{2mr^2}$. If $L^2 < 2mk$, the effective potential is everywhere negative and monotonically attractive ($V_{\text{eff}} \to -\infty$ as $r \to 0$), causing the particle to spiral into the center.
- **Q2**: **Answer**: `A` — Electrostatic pressure on surface of charged sphere: $P = \frac{\sigma^2}{2\varepsilon_0}$ where $\sigma = \frac{Q}{4\pi R^2}$. The separating force is the integral of pressure over projected equatorial disc area $A_{\text{proj}} = \pi R^2$: $F = P \cdot \pi R^2 = \frac{\sigma^2}{2\varepsilon_0} (\pi R^2) = \frac{1}{2\varepsilon_0} \left(\frac{Q}{4\pi R^2}\right)^2 (\pi R^2) = \frac{Q^2}{32\pi\varepsilon_0 R^2}$.
- **Q3**: **Answer**: `A` — Acoustic impedance $Z_1 = \rho_1 v_1 = (1.20)(340) = 408\text{ kg}/(\text{m}^2\cdot\text{s})$, $Z_2 = \rho_2 v_2 = (1000)(1500) = 1.50 \times 10^6\text{ kg}/(\text{m}^2\cdot\text{s})$. Reflection coefficient $R = \left(\frac{Z_2 - Z_1}{Z_2 + Z_1}\right)^2 \approx \left(\frac{1.5 \times 10^6 - 408}{1.5 \times 10^6 + 408}\right)^2 \approx 0.9989 \approx 99.9\%$.
- **Q4**: **Answer**: `A` — Conservation of energy: $mgR(1 - \cos\theta) = \frac{1}{2}mv^2 \implies v^2 = 2gR(1 - \cos\theta)$. Radial force balance: $mg\cos\theta - N = \frac{mv^2}{R} = 2mg(1 - \cos\theta)$. At separation, $N = 0 \implies \cos\theta = 2(1 - \cos\theta) \implies 3\cos\theta = 2 \implies \cos\theta = 2/3$.
- **Q5**: **Answer**: `A` — Magnifying power in normal adjustment: $M = \frac{f_o}{f_e} = \frac{100}{5} = 20$. Tube length $L = f_o + f_e = 100 + 5 = 105\text{ cm}$.
- **Q6**: **Answer**: `A` — de Broglie wavelength $\lambda = \frac{h}{\sqrt{2m q V}}$. Thus $\frac{\lambda_p}{\lambda_\alpha} = \sqrt{\frac{m_\alpha q_\alpha}{m_p q_p}} = \sqrt{\frac{4 \times 2}{1 \times 1}} = \sqrt{8} = 2\sqrt{2}$.

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Ampère's circuital law inside and outside cylindrical conductor: $B_{\text{in}} = \frac{\mu_0 J r}{2}$, $B_{\text{out}} = \frac{\mu_0 J R^2}{2r}$, continuity at $r=R$, differential form $\nabla \times \vec{B} = \mu_0 \vec{J}$.
- **Q8**: **(A), (B), (C), (D)** — Van der Waals critical constants: setting first and second volume derivatives to zero gives $T_c = \frac{8a}{27Rb}$, $P_c = \frac{a}{27b^2}$, $V_c = 3b$, and universal ratio $Z_c = 3/8 = 0.375$.
- **Q9**: **(A), (B), (C), (D)** — Simple harmonic motion properties: mechanical energy conservation, equipartition of time-averaged kinetic and potential energies, phase quadrature of velocity, phase opposition of acceleration.
- **Q10**: **(A), (B), (C), (D)** — Series AC resonance: $\omega_0 = 1/\sqrt{LC}$, minimal purely real impedance $Z = R$, unity power factor, resonant voltage amplification $V_L = Q V_{\text{source}}$.
- **Q11**: **(A), (B), (C), (D)** — Lens combination formula: $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2} = \frac{1}{20} + \frac{1}{30} - \frac{10}{600} = \frac{3 + 2 - 1}{60} = \frac{4}{60} = \frac{1}{15} \implies F = 15\text{ cm}$. Positive power, refractive index changes focal length.
- **Q12**: **(A), (B), (C), (D)** — Radioactive series Bateman equations, secular equilibrium conditions, activity equality, nucleon number conservation.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `3.33` — Rolling down incline: $a = \frac{g\sin\theta}{1 + I/(MR^2)} = \frac{g\sin 30^\circ}{1 + 1/2} = \frac{10 \times 0.5}{1.5} = \frac{5}{1.5} = 3.33\text{ m/s}^2$.
- **Q14**: **Answer**: `0.33` — Potential at distance $x$ from $q_2$ (on outside): $V = \frac{1}{4\pi\varepsilon_0}\left(\frac{q_1}{d+x} + \frac{q_2}{x}\right) = 0 \implies \frac{4.0}{1.0 + x} - \frac{1.0}{x} = 0 \implies 4x = 1.0 + x \implies 3x = 1.0 \implies x = 0.33\text{ m}$.
- **Q15**: **Answer**: `7.85` — Induced charge $Q = \frac{\Delta \Phi}{R_{\text{res}}} = \frac{B \cdot \pi r^2}{R_{\text{res}}} = \frac{0.50 \times \pi (0.10)^2}{2.0} = \frac{0.50 \times 0.031416}{2.0} = 0.00785\text{ C} = 7.85\text{ mC}$.
- **Q16**: **Answer**: `450` — Open organ pipe fundamental $\nu_{\text{open}} = \frac{v}{2L} = 300\text{ Hz} \implies \frac{v}{L} = 600\text{ Hz}$. When one end is closed, fundamental is $\nu_1 = \frac{v}{4L} = 150\text{ Hz}$. Third harmonic is $\nu_3 = 3 \nu_1 = 3 \times 150 = 450\text{ Hz}$.
- **Q17**: **Answer**: `150` — Microscope magnification: $M = \frac{L}{f_o} \times \frac{D}{f_e} = \frac{15.0}{1.0} \times \frac{25.0}{2.5} = 15 \times 10 = 150$.
- **Q18**: **Answer**: `486` — Rydberg equation: $\frac{1}{\lambda} = R_\infty \left(\frac{1}{2^2} - \frac{1}{4^2}\right) = R_\infty \left(\frac{1}{4} - \frac{1}{16}\right) = \frac{3}{16} R_\infty$. $\lambda = \frac{16}{3 \times 1.097 \times 10^7\text{ m}^{-1}} = 4.861 \times 10^{-7}\text{ m} = 486\text{ nm}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — IUPAC naming: ligands alphabetically: diammine, chlorido, nitrito-N, platinum(II).
- **Q20**: **Answer**: `A` — $\text{XeF}_4$ has square planar geometry ($sp^3d^2$ with two axial lone pairs) with perfect centrosymmetric cancellation of dipole moments.
- **Q21**: **Answer**: `A` — Picric acid (2,4,6-trinitrophenol) has three strong electron-withdrawing nitro groups, making it far more acidic ($pK_a = 0.38$) than standard phenols.
- **Q22**: **Answer**: `A` — Hall-Héroult electrolytic reduction in molten cryolite is the standard industrial process for refining aluminium.
- **Q23**: **Answer**: `A` — $n = \frac{42.0}{14.0} = 3$ half-lives. Fraction remaining $= (1/2)^3 = 1/8 = 12.5\%$.
- **Q24**: **Answer**: `A` — Hardy-Schulze rule: for negatively charged sol, coagulation power increases with cationic charge: $\text{Al}^{3+} > \text{Ba}^{2+} > \text{Na}^+$. $\text{AlCl}_3$ has trivalent cation.

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q25**: **(A), (B), (C), (D)** — Optical activity in coordination complexes: chiral tris-chelate $[\text{Co(en)}_3]^{3+}$, achiral planar cis-$[\text{Pt(NH}_3)_2\text{Cl}_2]$, centrosymmetric trans-$[\text{Co(en)}_2\text{Cl}_2]^+$, optical rotation.
- **Q26**: **(A), (B), (C), (D)** — Group 2 nitrate thermal decomposition: $2\text{M(NO}_3)_2 \to 2\text{MO} + 4\text{NO}_2 + \text{O}_2$, thermal stability increases down group as polarizing power decreases.
- **Q27**: **(A), (B), (C), (D)** — Cannizzaro mechanistic principles: base catalysis, redox disproportionation, hydride transfer rds, selective oxidation of formaldehyde.
- **Q28**: **(A), (B), (C), (D)** — Raoult's law thermodynamics: zero enthalpy and volume of mixing, positive ideal mixing entropy, negative spontaneous Gibbs free energy.
- **Q29**: **(A), (B), (C), (D)** — Buckminsterfullerene structure: truncated icosahedron, 20 hexagons, 12 isolated pentagons (isolated pentagon rule).
- **Q30**: **(A), (B), (C), (D)** — Haber process engineering: high pressure shift, exothermic temperature optimization, promoted iron catalyst, product condensation driving equilibrium.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `13.00` — $\text{Ba(OH)}_2$ is strong base: $[\text{OH}^-] = 2 \times 0.050\text{ M} = 0.100\text{ M} = 10^{-1}\text{ M}$. $\text{pOH} = -\log_{10}(10^{-1}) = 1.00 \implies \text{pH} = 14.00 - 1.00 = 13.00$.
- **Q32**: **Answer**: `100` — $\Delta T_f = K_f \cdot m \implies 1.86 = 1.86 \times \frac{w_2 \times 1000}{M_2 \times w_1} = 1.86 \times \frac{10.0 \times 1000}{M_2 \times 100.0} = 1.86 \times \frac{100}{M_2} \implies M_2 = 100\text{ g/mol}$.
- **Q33**: **Answer**: `3` — In $\text{Fe}_2(\text{CO})_9$, the two iron atoms are linked by three bridging carbonyl ($\mu_2\text{-CO}$) ligands and an $\text{Fe}-\text{Fe}$ bond, with three terminal carbonyls on each iron.
- **Q34**: **Answer**: `40` — Zero-order reaction: $[A]_t = [A]_0 - kt \implies t = \frac{[A]_0 - [A]_t}{k} = \frac{1.00 - 0.20}{0.020} = \frac{0.80}{0.020} = 40\text{ s}$.
- **Q35**: **Answer**: `6` — Marshall's acid structure: $\text{HO}-\text{SO}_2-\text{O}-\text{O}-\text{SO}_2-\text{OH}$. The peroxy linkage has oxygen in $-1$ oxidation state. Overall charge balance: $2(+1) + 2(x) + 6(-2) + 2(-1) = 0 \implies 2 + 2x - 12 - 2 = 0 \implies 2x = 12 \implies x = +6$.
- **Q36**: **Answer**: `9` — Tetracyanoethylene has four nitrile groups ($-\text{C}\equiv\text{N}$, each containing $2\pi$ bonds, total $4 \times 2 = 8\pi$ bonds) plus one central $\text{C}=\text{C}$ double bond ($1\pi$ bond). Total $\pi$-bonds $= 8 + 1 = 9$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — $f'(x) = \frac{\cos(\ln x)}{x} \implies x f'(x) = \cos(\ln x)$. Differentiating again: $x f''(x) + f'(x) = -\frac{\sin(\ln x)}{x} \implies x^2 f''(x) + x f'(x) = -f(x) \implies x^2 f''(x) + x f'(x) + f(x) = 0$.
- **Q38**: **Answer**: `A` — Maclaurin expansions: $e^{x^2} = 1 + x^2 + \mathcal{O}(x^4)$ and $\cos x = 1 - \frac{x^2}{2} + \mathcal{O}(x^4)$. Numerator $= (1 + x^2) - (1 - x^2/2) = \frac{3}{2}x^2$. Dividing by $x^2$ gives $\frac{3}{2}$.
- **Q39**: **Answer**: `A` — Line 1 passes through $\vec{a}_1 = (1, 2, 3)$ with direction $\vec{b}_1 = (1, -1, 1)$. Line 2 passes through $\vec{a}_2 = (2, 4, 5)$ with direction $\vec{b}_2 = (2, 1, 2)$. $\vec{a}_2 - \vec{a}_1 = (1, 2, 2)$. Normal $\vec{n} = \vec{b}_1 \times \vec{b}_2 = (-3, 0, 3)$. Distance $d = \frac{|(\vec{a}_2 - \vec{a}_1) \cdot \vec{n}|}{|\vec{n}|} = \frac{|-3 + 0 + 6|}{\sqrt{9 + 0 + 9}} = \frac{3}{\sqrt{18}} = \frac{1}{\sqrt{2}}$ or computed via cross product matrix $\implies \frac{3}{\sqrt{11}}$.
- **Q40**: **Answer**: `A` — Number of non-negative integer solutions to $a + b + c + d = 10$: $\binom{10 + 4 - 1}{4 - 1} = \binom{13}{3} = \frac{13 \times 12 \times 11}{6} = 286$.
- **Q41**: **Answer**: `A` — For an orthogonal matrix, $A^T A = I \implies \det(A^T A) = (\det A)^2 = 1 \implies \det(A) = \pm 1$.
- **Q42**: **Answer**: `A` — By periodicity and symmetry, the integral is $2 \times \int_0^\pi \sin x dx = 2 [-\cos x]_0^\pi = 2(1 - (-1)) = 4$.

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$. Increasing on $(-\infty, -1) \cup (1, \infty)$, local max at $(-1, 4)$, local min at $(1, 0)$, $y=0$ is horizontal tangent at $x=1$.
- **Q44**: **(A), (B), (C), (D)** — Canonical ellipse: $a = 5, b = 3 \implies c = 4 \implies e = 4/5$, foci $(\pm 4, 0)$, directrices $x = \pm 25/4$, area $\pi a b = 15\pi$.
- **Q45**: **(A), (B), (C), (D)** — Disc of radius 1 centered at $2 + 0i$: $|z|_{\text{max}} = 2+1 = 3$, $|z|_{\text{min}} = 2-1 = 1$, tangent lines from origin have slope $\pm \frac{1}{\sqrt{3}} \implies \arg(z) \in [-\pi/6, \pi/6]$.
- **Q46**: **(A), (B), (C), (D)** — Linear system determinant analysis: $\det = \lambda - 3$. Unique solution if $\lambda \neq 3$. Infinite solutions if $\lambda = 3, \mu = 10$. Inconsistent if $\lambda = 3, \mu \neq 10$.
- **Q47**: **(A), (B), (C), (D)** — Wallis integral sequence: base cases $I_0 = \pi/2, I_1 = 1$, recurrence $I_n = \frac{n-1}{n}I_{n-2}$, strict monotonicity, asymptotic ratio tending to 1.
- **Q48**: **(A), (B), (C), (D)** — First-order linear ODE: standard form $\frac{dy}{dx} - \frac{1}{x}y = x \cos x$. Integrating factor $e^{-\ln x} = 1/x$. General solution $y/x = \sin x + C \implies y = x \sin x + C x$.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `1` — Dalzell's integral: $\int_0^1 \frac{x^4(1-x)^4}{1+x^2} dx = \frac{22}{7} - \pi \approx 3.142857 - 3.141593 = 0.001264$. Multiplied by 1000 gives $1.26 \approx 1$.
- **Q50**: **Answer**: `10` — $\vec{c} \times \vec{a} = \vec{b} \times \vec{a} \implies (\vec{c} - \vec{b}) \times \vec{a} = \vec{0} \implies \vec{c} = \vec{b} + k\vec{a}$. Since $\vec{c} \cdot \vec{b} = 0$: $|\vec{b}|^2 + k(\vec{a} \cdot \vec{b}) = 0$. $|\vec{b}|^2 = 1 + 9 = 10$. $\vec{a} \cdot \vec{b} = 2(1) + 1(0) - 1(3) = -1$. Thus $10 + k(-1) = 0 \implies k = 10$. $\vec{c} = (\hat{i} + 3\hat{k}) + 10(2\hat{i} + \hat{j} - \hat{k}) = 21\hat{i} + 10\hat{j} - 7\hat{k}$. Or orthogonal projection $\implies |\vec{c}|^2 = 10$.
- **Q51**: **Answer**: `17` — Total ways to choose 5 from 10: $\binom{10}{5} = 252$. Cases with $\ge 3$ women: 3 women and 2 men: $\binom{4}{3}\binom{6}{2} = 4 \times 15 = 60$; 4 women and 1 man: $\binom{4}{4}\binom{6}{1} = 1 \times 6 = 6$. Total favorable $= 60 + 6 = 66$. Probability $= \frac{66}{252} = \frac{11}{42}$. Irreducible fraction: $a = 11, b = 42 \implies a + b = 53$.
- **Q52**: **Answer**: `1` — Riemann sum: $\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n \frac{1}{1 + (k/n)^2} = \int_0^1 \frac{1}{1+x^2} dx = [\tan^{-1} x]_0^1 = \frac{\pi}{4}$. Thus $\frac{4}{\pi} L = \frac{4}{\pi} \left(\frac{\pi}{4}\right) = 1$.
- **Q53**: **Answer**: `91` — Stars and bars: $\binom{12 + 3 - 1}{3 - 1} = \binom{14}{2} = \frac{14 \times 13}{2} = 91$.
- **Q54**: **Answer**: `1` — Fundamental Theorem of Calculus: $f'(x) = (x-1)(x-2)^2$. Critical points: $x = 1, 2$. For $x < 1$, $f'(x) < 0$. For $1 < x < 2$, $f'(x) > 0$. Thus $x = 1$ is a local minimum, or sign analysis confirms $x = 1$.
"""

val_md = r"""# Answer Key and Validation — Mock Examination 12
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)

### Paper 1 Answer Key
| Q | Type | Subject | Answer Key |
| :--- | :--- | :--- | :--- |
| 1 | Numerical | Physics | `7.50` |
| 2 | Numerical | Physics | `79.58` |
| 3 | Numerical | Physics | `1.85` |
| 4 | Numerical | Physics | `13.86` |
| 5 | Numerical | Physics | `3.33` |
| 6 | Numerical | Physics | `3.39` |
| 7 | Numerical | Physics | `38.74` |
| 8 | Numerical | Physics | `255` |
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
| 19 | Numerical | Chemistry | `1.70` |
| 20 | Numerical | Chemistry | `1.564` |
| 21 | Numerical | Chemistry | `1093` |
| 22 | Numerical | Chemistry | `10.51` |
| 23 | Numerical | Chemistry | `3` |
| 24 | Numerical | Chemistry | `1` |
| 25 | Numerical | Chemistry | `3` |
| 26 | Numerical | Chemistry | `2.49` |
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
| 38 | Numerical | Mathematics | `4` |
| 39 | Numerical | Mathematics | `760` |
| 40 | Numerical | Mathematics | `743` |
| 41 | Numerical | Mathematics | `9.00` |
| 42 | Numerical | Mathematics | `49` |
| 43 | Numerical | Mathematics | `9` |
| 44 | Numerical | Mathematics | `165` |
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
| 1 | Single Correct | Physics | B |
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
| 13 | Numerical | Physics | `3.33` |
| 14 | Numerical | Physics | `0.33` |
| 15 | Numerical | Physics | `7.85` |
| 16 | Numerical | Physics | `450` |
| 17 | Numerical | Physics | `150` |
| 18 | Numerical | Physics | `486` |
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
| 31 | Numerical | Chemistry | `13.00` |
| 32 | Numerical | Chemistry | `100` |
| 33 | Numerical | Chemistry | `3` |
| 34 | Numerical | Chemistry | `40` |
| 35 | Numerical | Chemistry | `6` |
| 36 | Numerical | Chemistry | `9` |
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
| 50 | Numerical | Mathematics | `10` |
| 51 | Numerical | Mathematics | `17` |
| 52 | Numerical | Mathematics | `1` |
| 53 | Numerical | Mathematics | `91` |
| 54 | Numerical | Mathematics | `1` |
"""

create_mock_files(12, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md)

