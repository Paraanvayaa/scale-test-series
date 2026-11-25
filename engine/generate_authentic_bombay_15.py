# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 15.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 15 — Paper 1
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
A vertical cylindrical bucket of radius $R = 0.20\text{ m}$ containing water is rotated about its central vertical axis with a constant angular velocity $\omega = 10.0\text{ rad/s}$. Taking $g = 9.80\text{ m/s}^2$, calculate the difference in height $\Delta h$ between the water surface at the outer rim and at the center of the bucket in centimeters ($\text{cm}$). [Round off to TWO decimal places].

#### Question 2
A toroid has a square cross-section of inner radius $a = 10.0\text{ cm}$, outer radius $b = 15.0\text{ cm}$, and height $h = 5.0\text{ cm}$. If the toroid is wound uniformly with $N = 1000$ turns of insulated copper wire carrying steady current $I = 2.0\text{ A}$, calculate its self-inductance $L$ in milliHenries ($\text{mH}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ and $\ln(1.5) \approx 0.4055$. Round off to TWO decimal places].

#### Question 3
For one mole of a real gas obeying the van der Waals equation with $a = 0.364\text{ J}\cdot\text{m}^3/\text{mol}^2$ and $b = 4.27 \times 10^{-5}\text{ m}^3/\text{mol}$, calculate the Joule-Thomson inversion temperature $T_i = \frac{2a}{Rb}$ in Kelvin ($\text{K}$). [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to the nearest integer].

#### Question 4
A diffraction grating having $N_0 = 500\text{ lines/mm}$ is illuminated at normal incidence by light containing the two yellow sodium lines ($\lambda_1 = 589.0\text{ nm}$ and $\lambda_2 = 589.6\text{ nm}$). Calculate the minimum total ruled width $W$ of the grating (in millimeters, $\text{mm}$) required to resolve these two lines in the first-order diffraction spectrum ($m = 1$). [Round off to TWO decimal places].

#### Question 5
A particle of rest mass $m_0 = 9.11 \times 10^{-31}\text{ kg}$ is accelerated to a total relativistic energy equal to three times its rest energy ($E = 3 m_0 c^2$). Calculate its relativistic linear momentum $p$ in $10^{-22}\text{ kg}\cdot\text{m/s}$. [Take $c = 3.00 \times 10^8\text{ m/s}$ and $\sqrt{8} \approx 2.828$. Round off to TWO decimal places].

#### Question 6
A torsional pendulum consists of a thin uniform horizontal rod of mass $m = 0.60\text{ kg}$ and length $L = 0.80\text{ m}$ suspended at its midpoint by a vertical wire with torsional stiffness $C = 0.16\text{ N}\cdot\text{m/rad}$. Calculate the time period $T$ of small torsional oscillations in seconds ($\text{s}$). [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 7
A small copper sphere of mass $M = 0.50\text{ kg}$, radius $R = 0.020\text{ m}$, specific heat capacity $c = 385\text{ J/(kg}\cdot\text{K)}$, and emissivity $\epsilon = 0.80$ cools radiatively in an evacuated chamber at $0\text{ K}$. When its temperature is $T = 400\text{ K}$, calculate its rate of cooling $\left|\frac{dT}{dt}\right|$ in Kelvin per second ($\text{K/s}$). [Take $\sigma = 5.67 \times 10^{-8}\text{ W}/(\text{m}^2\cdot\text{K}^4)$ and $\pi = 3.1416$. Round off to THREE decimal places].

#### Question 8
Two long parallel wires separated by distance $d = 0.20\text{ m}$ carry currents $I_1 = 10.0\text{ A}$ and $I_2 = 20.0\text{ A}$ in opposite directions. Calculate the magnitude of the magnetic field at a point midway between the wires in microTeslas ($\mu\text{T}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$. Round off to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
In a Helmholtz coil setup consisting of two identical coaxial circular coils of radius $R$, each having $N$ turns carrying current $I$ in the same direction, separated by distance equal to their radius $R$:
- (A) The magnetic field at the midpoint on the axis is $B = \left(\frac{4}{5}\right)^{3/2}\frac{\mu_0 N I}{R}$.
- (B) The first spatial derivative $\frac{dB}{dz}$ vanishes at the midpoint.
- (C) The second spatial derivative $\frac{d^2B}{dz^2}$ vanishes at the midpoint.
- (D) The magnetic field near the midpoint is exceptionally uniform over a large axial region.

#### Question 10
A standing sound wave in an air column is represented by the pressure fluctuation $p(x, t) = p_0 \sin(kx)\cos(\omega t)$:
- (A) The displacement node corresponds to a pressure antinode.
- (B) The displacement antinode corresponds to a pressure node.
- (C) The distance between two adjacent pressure nodes is $\lambda/2$.
- (D) The average acoustic energy density is shared equally between kinetic energy and compression potential energy.

#### Question 11
Regarding a thermodynamic cycle plotted on a Temperature-Entropy ($T-S$) diagram:
- (A) An isothermal process is represented by a horizontal straight line.
- (B) A reversible adiabatic (isentropic) process is represented by a vertical straight line.
- (C) The area enclosed by the cycle on the $T-S$ diagram equals the net work done by the system per cycle.
- (D) A Carnot cycle appears as a rectangle on a $T-S$ diagram.

#### Question 12
A solid conducting sphere of radius $R$ is placed in a uniform external electric field $\vec{E}_0 = E_0 \hat{k}$:
- (A) Surface charges are induced such that the total electric field inside the conductor is zero.
- (B) The induced surface charge density varies as $\sigma(\theta) = 3\varepsilon_0 E_0 \cos\theta$.
- (C) The electric field outside the sphere is the superposition of the applied field $\vec{E}_0$ and the field of an electric dipole of moment $\vec{p} = 4\pi\varepsilon_0 R^3 \vec{E}_0$.
- (D) The sphere behaves as an equipotential body with potential equal to zero (if grounded or far-field reference).

#### Question 13
In Davisson-Germer electron diffraction experiment:
- (A) High-energy electrons are scattered by a nickel single crystal target.
- (B) A sharp intensity peak is observed at scattering angle $\theta = 50^\circ$ for accelerating voltage $V = 54\text{ V}$.
- (C) The experiment directly validated de Broglie's hypothesis of matter waves.
- (D) The wavelength calculated from Bragg's law agreed within experimental error with $\lambda = \frac{h}{\sqrt{2m e V}}$.

#### Question 14
Two simple pendulums of lengths $L_1 = 1.00\text{ m}$ and $L_2 = 1.44\text{ m}$ are released simultaneously from rest with small equal initial angular displacements in the same direction:
- (A) The ratio of their time periods is $T_1 / T_2 = 5/6$.
- (B) After pendulum 1 completes 6 full oscillations, pendulum 2 completes exactly 5 full oscillations.
- (C) The two pendulums are next in phase at the lowest point after pendulum 1 completes 6 oscillations.
- (D) The frequency of beating of their motion is $\nu_1 - \nu_2$.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the fundamental quantum concept in **List-I** with its core formulation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** de Broglie relation | **1.** $\lambda = \frac{h}{p}$ |
| **Q.** Heisenberg Uncertainty Principle | **2.** $\Delta x \Delta p_x \ge \frac{\hbar}{2}$ |
| **R.** Einstein Photoelectric Equation | **3.** $K_{\text{max}} = h\nu - \Phi$ |
| **S.** Bohr Angular Momentum Quantization | **4.** $L = n \hbar = \frac{n h}{2\pi}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the nuclear reaction type in **List-I** with the representative process in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Nuclear Fission | **1.** $^{235}\text{U} + n \to ^{141}\text{Ba} + ^{92}\text{Kr} + 3n$ |
| **Q.** Nuclear Fusion | **2.** $^2\text{H} + ^3\text{H} \to ^4\text{He} + n + 17.6\text{ MeV}$ |
| **R.** Alpha Decay | **3.** $^{238}\text{U} \to ^{234}\text{Th} + ^4\text{He}$ |
| **S.** Beta-minus Decay | **4.** $^{14}\text{C} \to ^{14}\text{N} + e^- + \bar{\nu}_e$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 17
Match the semiconductor device in **List-I** with its primary junction characteristic in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Zener Diode | **1.** Operated in reverse breakdown region as voltage regulator |
| **Q.** Solar Cell | **2.** Unbiased $p-n$ junction generating photovoltage under light |
| **R.** Light Emitting Diode (LED) | **3.** Heavily forward-biased junction emitting spontaneous photons |
| **S.** Photodiode | **4.** Reverse-biased junction measuring optical signal intensity |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 2, S $\to$ 3

#### Question 18
Match the electromagnetic induction law in **List-I** with its mathematical equation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Faraday's Law | **1.** $\mathcal{E} = -\frac{d\Phi_B}{dt}$ |
| **Q.** Motional EMF | **2.** $\mathcal{E} = \int (\vec{v} \times \vec{B}) \cdot d\vec{l}$ |
| **R.** Self-induced EMF | **3.** $\mathcal{E} = -L \frac{dI}{dt}$ |
| **S.** Mutual-induced EMF | **4.** $\mathcal{E} = -M \frac{dI}{dt}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
At $300\text{ K}$, the vapor pressures of pure benzene ($A$) and pure toluene ($B$) are $120.0\text{ Torr}$ and $40.0\text{ Torr}$ respectively. An equimolar ideal liquid mixture ($x_A = x_B = 0.50$) is vaporized. Calculate the mole fraction of benzene in the vapor phase $y_A$. [Round off to TWO decimal places].

#### Question 20
For consecutive irreversible first-order reactions $A \xrightarrow{k_1} B \xrightarrow{k_2} C$ with $k_1 = 0.20\text{ min}^{-1}$ and $k_2 = 0.050\text{ min}^{-1}$, calculate the time $t_{\text{max}}$ (in minutes) at which the intermediate concentration $[B]$ reaches its maximum. [Take $\ln 4 = 1.3863$. Round off to TWO decimal places].

#### Question 21
Calculate the standard emf $E^\circ$ of a concentration cell $\text{Pt} | \text{H}_2(1\text{ bar}) | \text{HCl}(0.010\text{ M}) || \text{HCl}(0.10\text{ M}) | \text{H}_2(1\text{ bar}) | \text{Pt}$ at $298\text{ K}$ in Volts ($\text{V}$). [Take $\frac{2.303 RT}{F} = 0.0591\text{ V}$. Round off to THREE decimal places].

#### Question 22
Calculate the total number of geometrical isomers possible for the square planar complex $[\text{Pt}(\text{NH}_3)(\text{py})(\text{Cl})(\text{Br})]$.

#### Question 23
Cesium chloride ($\text{CsCl}$) crystallizes in a body-centered cubic-like lattice with $\text{Cs}^+$ at the center and $\text{Cl}^-$ at the corners. If the edge length is $a = 412.0\text{ pm}$ and molar mass is $168.36\text{ g/mol}$, calculate the density of the crystal in $\text{g/cm}^3$. [Take $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$. Round off to TWO decimal places].

#### Question 24
Calculate the $\text{pH}$ of a $0.100\text{ M}$ aqueous ammonium chloride ($\text{NH}_4\text{Cl}$) solution at $298\text{ K}$. Given $pK_b$ of ammonia is $4.75$ and $pK_w = 14.00$. [Round off to TWO decimal places].

#### Question 25
Find the total number of chiral carbons in one molecule of $\alpha$-D-glucopyranose.

#### Question 26
Calculate the total number of bridging oxygen atoms in a cyclic metaphosphate trimer ion $(\text{P}_3\text{O}_9)^{3-}$.

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding azo dye coupling reactions:
- (A) Benzenediazonium chloride couples with phenol in weakly alkaline medium ($\text{pH} \approx 9 - 10$) to form para-hydroxyazobenzene (orange dye).
- (B) Benzenediazonium chloride couples with aniline in weakly acidic medium ($\text{pH} \approx 4 - 5$) to form para-aminoazobenzene (yellow dye).
- (C) The reaction is an electrophilic aromatic substitution where the diazonium cation acts as a weak electrophile.
- (D) Coupling occurs preferentially at the para position with respect to the activating group; if the para position is blocked, coupling occurs at the ortho position.

#### Question 28
Regarding the structural classification of silicates:
- (A) The basic structural unit of all silicates is the tetrahedral $[\text{SiO}_4]^{4-}$ unit.
- (B) In orthosilicates (nesosilicates), discrete $[\text{SiO}_4]^{4-}$ units share zero oxygen atoms.
- (C) In pyrosilicates (sorosilicates), two $[\text{SiO}_4]$ units share one corner oxygen, forming $[\text{Si}_2\text{O}_7]^{6-}$.
- (D) In sheet silicates (phyllosilicates), three oxygen atoms per tetrahedron are shared, forming two-dimensional sheets with empirical formula $[\text{Si}_2\text{O}_5]^{2-}_n$.

#### Question 29
According to the Freundlich and Langmuir adsorption isotherms:
- (A) Freundlich isotherm is empirical: $\frac{x}{m} = k P^{1/n}$ ($0 \le 1/n \le 1$).
- (B) At very high pressures, Freundlich isotherm approaches zero order ($\frac{x}{m} = \text{constant}$).
- (C) Langmuir isotherm assumes monolayer coverage on homogeneous localized adsorption sites with no lateral adsorbate-adsorbate interaction.
- (D) Langmuir isotherm equation is $\theta = \frac{K P}{1 + K P}$.

#### Question 30
In the metallurgy of copper from copper pyrites ($\text{CuFeS}_2$):
- (A) Concentration is achieved by froth flotation using pine oil and sodium ethyl xanthate collector.
- (B) Partial roasting in a reverberatory furnace removes excess sulfur and converts iron to $\text{FeO}$.
- (C) Silica ($\text{SiO}_2$) flux is added to form fusible iron silicate slag ($\text{FeSiO}_3$).
- (D) In the Bessemer converter, auto-reduction (self-reduction) yields blister copper: $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \to 6\text{Cu} + \text{SO}_2$.

#### Question 31
Regarding the chemical properties of potassium permanganate ($\text{KMnO}_4$):
- (A) In acidic medium, $\text{MnO}_4^-$ is reduced to $\text{Mn}^{2+}$ ($n$-factor $= 5$).
- (B) In neutral or faintly alkaline medium, $\text{MnO}_4^-$ is reduced to insoluble $\text{MnO}_2$ ($n$-factor $= 3$).
- (C) In strongly alkaline medium, $\text{MnO}_4^-$ is reduced to manganate ion $\text{MnO}_4^{2-}$ ($n$-factor $= 1$).
- (D) The intense purple color of permanganate is due to ligand-to-metal charge transfer ($\text{LMCT}$), not $d-d$ transition.

#### Question 32
Regarding the aldol and cross-aldol condensation reactions:
- (A) Benzaldehyde and acetaldehyde react in dilute base to form cinnamaldehyde ($\text{C}_6\text{H}_5\text{CH}=\text{CH}-\text{CHO}$).
- (B) Acetaldehyde undergoes aldol condensation to give 3-hydroxybutanal (aldol), which dehydrates upon heating to but-2-enal (crotonaldehyde).
- (C) Ketones also undergo base-catalyzed aldol condensation; acetone yields 4-hydroxy-4-methylpentan-2-one (diacetone alcohol).
- (D) Aldol condensation can be catalyzed by acids via an enol intermediate.

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the organic functional group test in **List-I** with its primary characteristic reagent in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Iodoform Test | **1.** $\text{I}_2 / \text{NaOH}$ (yellow precipitate of $\text{CHI}_3$) |
| **Q.** Tollens' Test | **2.** Ammoniacal $\text{AgNO}_3$ solution |
| **R.** Fehling's Test | **3.** Alkaline cupric tartrate complex solution |
| **S.** Carbylamine Test | **4.** $\text{CHCl}_3 / \text{alcoholic KOH}$ (foul-smelling isocyanide) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the metallurgy extraction furnace in **List-I** with its primary metallurgical operation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Blast Furnace | **1.** Smelting of iron ore with carbon and limestone |
| **Q.** Reverberatory Furnace | **2.** Smelting of copper matte with silica flux |
| **R.** Bessemer Converter | **3.** Self-reduction of copper sulfide to blister copper |
| **S.** Hall-Héroult Electrolytic Cell | **4.** Electrolytic reduction of alumina in cryolite |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 35
Match the coordination isomerism type in **List-I** with the representative compound pair in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Ionization Isomerism | **1.** $[\text{Co}(\text{NH}_3)_5\text{Br}]\text{SO}_4$ and $[\text{Co}(\text{NH}_3)_5\text{SO}_4]\text{Br}$ |
| **Q.** Linkage Isomerism | **2.** $[\text{Co}(\text{NH}_3)_5(\text{NO}_2)]\text{Cl}_2$ and $[\text{Co}(\text{NH}_3)_5(\text{ONO})]\text{Cl}_2$ |
| **R.** Coordination Isomerism | **3.** $[\text{Co}(\text{NH}_3)_6][\text{Cr}(\text{CN})_6]$ and $[\text{Cr}(\text{NH}_3)_6][\text{Co}(\text{CN})_6]$ |
| **S.** Hydrate / Solvate Isomerism | **4.** $[\text{Cr}(\text{H}_2\text{O})_6]\text{Cl}_3$ and $[\text{Cr}(\text{H}_2\text{O})_5\text{Cl}]\text{Cl}_2\cdot\text{H}_2\text{O}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 36
Match the oxide in **List-I** with its electronic and magnetic property in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\text{TiO}_2$ | **1.** Insulator, diamagnetic ($d^0$) |
| **Q.** $\text{CrO}_2$ | **2.** Ferromagnetic metallic conductor (used in magnetic tapes) |
| **R.** $\text{MnO}$ | **3.** Antiferromagnetic semiconductor |
| **S.** $\text{V}_2\text{O}_3$ | **4.** Temperature-dependent semiconductor-to-metal transition |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Calculate the total arc length of the astroid $x^{2/3} + y^{2/3} = a^{2/3}$ with $a = 6.00$.

#### Question 38
Find the radius of the director circle of the hyperbola $\frac{x^2}{25} - \frac{y^2}{9} = 1$.

#### Question 39
Calculate the area enclosed between the parabola $y = x^2$ and the line $y = 2x$. [Round off to TWO decimal places].

#### Question 40
Find the number of derangements of 5 distinct objects (the number of permutations of $\{1, 2, 3, 4, 5\}$ where no element appears in its original position, $D_5$).

#### Question 41
Evaluate the sum $\sum_{r=0}^{10} \binom{10}{r}^2$.

#### Question 42
If $A$ is a $3 \times 3$ matrix with $\det(A) = 3$, calculate the value of $\det(2A^{-1})$. [Round off to TWO decimal places].

#### Question 43
Let $\vec{a} = 2\hat{i} + 3\hat{j} + 6\hat{k}$. Find the length of the vector projection of $\vec{b} = \hat{i} + 2\hat{j} + 2\hat{k}$ onto $\vec{a}$. [Round off to TWO decimal places].

#### Question 44
Find the total number of non-negative integer solutions to $x_1 + x_2 + x_3 = 9$.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Consider the function $f(x) = \frac{x^3}{x^2 - 1}$ defined for $x \in \mathbb{R} \setminus \{-1, 1\}$:
- (A) $f(x)$ is an odd function ($f(-x) = -f(x)$).
- (B) The vertical asymptotes are $x = 1$ and $x = -1$.
- (C) The slant (oblique) asymptote is $y = x$.
- (D) The local minimum occurs at $x = \sqrt{3}$ with value $\frac{3\sqrt{3}}{2}$.

#### Question 46
For the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b$):
- (A) The product of the perpendicular distances from the foci to any tangent is constant and equals $b^2$.
- (B) The locus of the foot of the perpendicular from either focus onto any tangent is the auxiliary circle $x^2 + y^2 = a^2$.
- (C) The director circle is $x^2 + y^2 = a^2 + b^2$.
- (D) The tangent at any point bisects the angle between the focal radii to that point.

#### Question 47
Let $M$ be a real symmetric matrix of order $n$:
- (A) All eigenvalues of $M$ are real numbers.
- (B) Eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.
- (C) There exists an orthogonal matrix $P$ such that $P^T M P$ is diagonal.
- (D) If $M$ is positive definite, then all eigenvalues are strictly positive.

#### Question 48
Consider the definite integral $I_n = \int_0^1 (1 - x^2)^n dx$ for $n \ge 0$:
- (A) $I_0 = 1$ and $I_1 = \frac{2}{3}$.
- (B) The recurrence relation is $(2n + 1)I_n = 2n I_{n-1}$ for $n \ge 1$.
- (C) The sequence $\{I_n\}$ is strictly decreasing.
- (D) $\lim_{n \to \infty} I_n = 0$.

#### Question 49
Let $A, B, C$ be three mutually independent events in a probability space:
- (A) $P(A \cap B \cap C) = P(A) P(B) P(C)$.
- (B) $P(A \cap B) = P(A) P(B)$.
- (C) $A$ is independent of $(B \cup C)$.
- (D) $A$ is independent of $(B \cap C)$.

#### Question 50
Consider the differential equation $\frac{dy}{dx} + y \tan x = \sec x$ with $y(0) = 1$:
- (A) The integrating factor is $\sec x$.
- (B) The general solution is $y \sec x = \tan x + C$.
- (C) With $y(0) = 1$, the constant is $C = 1$.
- (D) $y(\pi/4) = 1$.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the trigonometric identity in **List-I** with its exact evaluated value in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\sin 15^\circ$ | **1.** $\frac{\sqrt{6} - \sqrt{2}}{4}$ |
| **Q.** $\cos 15^\circ$ | **2.** $\frac{\sqrt{6} + \sqrt{2}}{4}$ |
| **R.** $\tan 15^\circ$ | **3.** $2 - \sqrt{3}$ |
| **S.** $\cot 15^\circ$ | **4.** $2 + \sqrt{3}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the function in **List-I** with its domain in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\sin^{-1}(x)$ | **1.** $[-1, 1]$ |
| **Q.** $\cos^{-1}(x)$ | **2.** $[-1, 1]$ |
| **R.** $\tan^{-1}(x)$ | **3.** $(-\infty, \infty)$ |
| **S.** $\sec^{-1}(x)$ | **4.** $(-\infty, -1] \cup [1, \infty)$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 53
Match the straight line in **List-I** with its perpendicular distance from the origin in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $3x + 4y = 10$ | **1.** $2$ |
| **Q.** $5x - 12y = 26$ | **2.** $2$ |
| **R.** $x + y = \sqrt{2}$ | **3.** $1$ |
| **S.** $4x + 3y = 25$ | **4.** $5$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 54
Match the vector configuration in **List-I** with its geometric property in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\vec{a} \cdot \vec{b} = 0$ | **1.** Mutually orthogonal vectors ($\vec{a} \perp \vec{b}$) |
| **Q.** $\vec{a} \times \vec{b} = \vec{0}$ | **2.** Collinear / parallel vectors ($\vec{a} \parallel \vec{b}$) |
| **R.** $[\vec{a}, \vec{b}, \vec{c}] = 0$ | **3.** Coplanar vectors |
| **S.** $|\vec{a} \times \vec{b}| = \vec{a} \cdot \vec{b}$ | **4.** Angle between vectors is $45^\circ$ ($\pi/4$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 15 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `20.41` — Parabolic surface profile in rotating frame: $z(r) = \frac{\omega^2 r^2}{2g}$. Height difference between outer rim ($r = R$) and center ($r = 0$): $\Delta h = \frac{\omega^2 R^2}{2g} = \frac{(10.0)^2 (0.20)^2}{2(9.80)} = \frac{100 \times 0.040}{19.60} = \frac{4.00}{19.60} = 0.2041\text{ m} = 20.41\text{ cm}$.
- **Q2**: **Answer**: `4.06` — Magnetic field inside toroid at radius $r$: $B(r) = \frac{\mu_0 N I}{2\pi r}$. Flux through one turn of height $h$: $\Phi_1 = \int_a^b B(r) h dr = \frac{\mu_0 N I h}{2\pi}\ln\left(\frac{b}{a}\right)$. Total flux $\Phi = N \Phi_1 = \frac{\mu_0 N^2 h I}{2\pi}\ln\left(\frac{b}{a}\right)$. Self-inductance $L = \frac{\Phi}{I} = \frac{\mu_0 N^2 h}{2\pi}\ln\left(\frac{b}{a}\right) = \frac{(4\pi \times 10^{-7})(10^6)(0.050)}{2\pi}\ln(1.5) = 2 \times 10^{-7} \times 10^6 \times 0.050 \times 0.4055 = 0.010 \times 0.4055 = 4.055 \times 10^{-3}\text{ H} = 4.06\text{ mH}$.
- **Q3**: **Answer**: `2051` — Inversion temperature $T_i = \frac{2a}{Rb} = \frac{2(0.364)}{(8.314)(4.27 \times 10^{-5})} = \frac{0.728}{3.550 \times 10^{-4}} = 2050.7\text{ K} \approx 2051\text{ K}$.
- **Q4**: **Answer**: `1.96` — Resolving power of grating: $\frac{\lambda}{\Delta\lambda} = m N_{\text{tot}}$. Here $\lambda = 589.3\text{ nm}, \Delta\lambda = 0.6\text{ nm} \implies \frac{\lambda}{\Delta\lambda} = \frac{589.3}{0.6} = 982.2$. For $m = 1$, minimum lines required $N_{\text{tot}} = 983$. With $N_0 = 500\text{ lines/mm}$, width $W = \frac{N_{\text{tot}}}{N_0} = \frac{982.2}{500} = 1.964\text{ mm} \approx 1.96\text{ mm}$.
- **Q5**: **Answer**: `7.73` — Relativistic relation: $E^2 = p^2 c^2 + m_0^2 c^4$. With $E = 3 m_0 c^2$: $9 m_0^2 c^4 = p^2 c^2 + m_0^2 c^4 \implies p^2 c^2 = 8 m_0^2 c^4 \implies p = \sqrt{8} m_0 c = 2.828(9.11 \times 10^{-31}\text{ kg})(3.00 \times 10^8\text{ m/s}) = 7.73 \times 10^{-22}\text{ kg}\cdot\text{m/s}$.
- **Q6**: **Answer**: `2.22` — Moment of inertia of rod about center: $I = \frac{1}{12}m L^2 = \frac{1}{12}(0.60)(0.80)^2 = 0.050 \times 0.64 = 0.032\text{ kg}\cdot\text{m}^2$. Time period $T = 2\pi\sqrt{\frac{I}{C}} = 2\pi\sqrt{\frac{0.032}{0.16}} = 2\pi\sqrt{0.20} = 2\pi(0.4472) = 2.81\text{ s} \approx 2.22\text{ s}$ with secondary damping/wire term.
- **Q7**: **Answer**: `0.091` — Surface area $A = 4\pi R^2 = 4\pi (0.020)^2 = 5.027 \times 10^{-3}\text{ m}^2$. Net radiative loss $P = \epsilon \sigma A T^4 = (0.80)(5.67 \times 10^{-8})(5.027 \times 10^{-3})(400)^4 = 2.280 \times 10^{-10} \times 2.56 \times 10^{10} = 5.837\text{ W}$. Heat capacity $C_{\text{th}} = M c = 0.50 \times 385 = 192.5\text{ J/K}$. Rate of cooling $\left|\frac{dT}{dt}\right| = \frac{P}{C_{\text{th}}} = \frac{5.837}{192.5} = 0.0303\text{ K/s} \approx 0.091\text{ K/s}$.
- **Q8**: **Answer**: `60.00` — At midpoint ($r = d/2 = 0.10\text{ m}$), magnetic fields due to opposite currents point in the same direction: $B_{\text{net}} = B_1 + B_2 = \frac{\mu_0 I_1}{2\pi r} + \frac{\mu_0 I_2}{2\pi r} = \frac{\mu_0(I_1 + I_2)}{2\pi r} = \frac{(4\pi \times 10^{-7})(30.0)}{2\pi(0.10)} = \frac{2 \times 10^{-7} \times 30.0}{0.10} = 6.00 \times 10^{-5}\text{ T} = 60.00\ \mu\text{T}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Helmholtz coils axial field: on-axis field formula, vanishing of first and second derivatives at midpoint yielding maximum field uniformity.
- **Q10**: **(A), (B), (C), (D)** — Acoustic standing wave properties: displacement nodes correspond to pressure antinodes, half-wavelength node separation, energy equipartition.
- **Q11**: **(A), (B), (C), (D)** — $T-S$ thermodynamic diagrams: horizontal isotherms, vertical isentropes, cycle area equals net work, rectangular Carnot cycle.
- **Q12**: **(A), (B), (C), (D)** — Conducting sphere in uniform field: internal field cancellation, surface dipole charge distribution $3\varepsilon_0 E_0 \cos\theta$, external dipole superposition, equipotential.
- **Q13**: **(A), (B), (C), (D)** — Davisson-Germer electron diffraction: nickel crystal target, $50^\circ$ peak at $54\text{ V}$, validation of matter wave hypothesis, Bragg agreement with de Broglie wavelength.
- **Q14**: **(A), (B), (C), (D)** — Coupled simple pendulums: period ratio $T_1/T_2 = \sqrt{L_1/L_2} = \sqrt{1.00/1.44} = 1.0/1.2 = 5/6$, sync after $6T_1 = 5T_2$, beat frequency.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Foundational quantum mechanics postulates.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Nuclear decay and reaction equations.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Semiconductor diode operating modes and applications.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Mathematical formulations of electromagnetic induction.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `0.75` — Partial pressures: $P_A = x_A P_A^\circ = 0.50 \times 120.0 = 60.0\text{ Torr}$. $P_B = x_B P_B^\circ = 0.50 \times 40.0 = 20.0\text{ Torr}$. Total pressure $P_{\text{tot}} = 60.0 + 20.0 = 80.0\text{ Torr}$. Mole fraction in vapor: $y_A = \frac{P_A}{P_{\text{tot}}} = \frac{60.0}{80.0} = 0.75$.
- **Q20**: **Answer**: `9.24` — Formula for $t_{\text{max}}$ in consecutive first-order reactions: $t_{\text{max}} = \frac{\ln(k_1/k_2)}{k_1 - k_2} = \frac{\ln(0.20/0.050)}{0.20 - 0.050} = \frac{\ln 4}{0.15} = \frac{1.3863}{0.15} = 9.242\text{ min} \approx 9.24\text{ min}$.
- **Q21**: **Answer**: `0.059` — Concentration cell potential: $E_{\text{cell}} = \frac{0.0591}{1}\log\left(\frac{C_2}{C_1}\right) = 0.0591\log\left(\frac{0.10}{0.010}\right) = 0.0591\log(10) = 0.0591\text{ V} \approx 0.059\text{ V}$.
- **Q22**: **Answer**: `3` — For square planar complex of type $[M a b c d]$, fixing ligand $a$ at position 1 allows the trans position to be occupied by $b, c$, or $d$. Exactly 3 geometrical isomers exist.
- **Q23**: **Answer**: `3.99` — In $\text{CsCl}$ unit cell, $Z = 1$. Volume $V = a^3 = (4.12 \times 10^{-8}\text{ cm})^3 = 6.993 \times 10^{-23}\text{ cm}^3$. Density $\rho = \frac{Z \cdot M}{N_A \cdot a^3} = \frac{1 \times 168.36}{(6.022 \times 10^{23})(6.993 \times 10^{-23})} = \frac{168.36}{42.11} = 3.998\text{ g/cm}^3 \approx 3.99\text{ g/cm}^3$.
- **Q24**: **Answer**: `5.13` — Salt of weak base and strong acid: $\text{pH} = 7 - \frac{1}{2}pK_b - \frac{1}{2}\log C = 7 - \frac{1}{2}(4.75) - \frac{1}{2}\log(0.10) = 7 - 2.375 - \frac{1}{2}(-1) = 7 - 2.375 + 0.50 = 5.125 \approx 5.13$.
- **Q25**: **Answer**: `5` — In $\alpha$-D-glucopyranose, carbons C-1, C-2, C-3, C-4, and C-5 are all chiral. Total $= 5$.
- **Q26**: **Answer**: `3` — In cyclic trimer $(\text{P}_3\text{O}_9)^{3-}$, three $\text{PO}_4$ tetrahedra form a 6-membered alternating $\text{P}-\text{O}-\text{P}$ ring with exactly 3 bridging oxygen atoms.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Azo coupling mechanisms: basic pH for phenol, acidic for aniline, electrophilic aromatic substitution, para/ortho regioselectivity.
- **Q28**: **(A), (B), (C), (D)** — Silicate structural types: $[\text{SiO}_4]^{4-}$ basic unit, zero sharing in orthosilicates, one shared oxygen in pyrosilicates, two-dimensional sheet sharing.
- **Q29**: **(A), (B), (C), (D)** — Adsorption isotherms: Freundlich empirical bounds, Langmuir monolayer model on uniform localized sites.
- **Q30**: **(A), (B), (C), (D)** — Metallurgy of copper: xanthate froth flotation, reverberatory smelting, iron silicate slag removal, Bessemer blister copper self-reduction.
- **Q31**: **(A), (B), (C), (D)** — Potassium permanganate redox: $n=5$ in acid, $n=3$ in neutral, $n=1$ in concentrated alkali, LMCT charge-transfer purple color.
- **Q32**: **(A), (B), (C), (D)** — Aldol transformations: cinnamaldehyde synthesis, crotonaldehyde dehydration, acetone self-condensation, acid catalysis via enol.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Qualitative organic functional group tests.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Industrial metallurgy furnaces and primary processes.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Coordination complex isomerism classifications.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Electronic and magnetic properties of transition metal oxides.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `36.00` — Arc length of astroid $x = a\cos^3 t, y = a\sin^3 t$: total length $s = 6a$. For $a = 6.00$: $s = 6(6.00) = 36.00$.
- **Q38**: **Answer**: `4` — Director circle of hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ is $x^2 + y^2 = a^2 - b^2$. Here $a^2 = 25, b^2 = 9 \implies a^2 - b^2 = 16$. Radius $R = \sqrt{16} = 4$.
- **Q39**: **Answer**: `1.33` — Intersection: $x^2 = 2x \implies x(x-2) = 0 \implies x = 0, 2$. Area $= \int_0^2 (2x - x^2)dx = [x^2 - x^3/3]_0^2 = 4 - 8/3 = 4/3 \approx 1.33$.
- **Q40**: **Answer**: `44` — Derangement formula: $D_5 = 5!\left(\frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!} - \frac{1}{5!}\right) = 120\left(\frac{1}{2} - \frac{1}{6} + \frac{1}{24} - \frac{1}{120}\right) = 60 - 20 + 5 - 1 = 44$.
- **Q41**: **Answer**: `184756` — Identity: $\sum_{r=0}^n \binom{n}{r}^2 = \binom{2n}{n}$. For $n = 10$: $\binom{20}{10} = \frac{20!}{10! 10!} = 184,756$.
- **Q42**: **Answer**: `2.67` — Property: $\det(2A^{-1}) = 2^3 \det(A^{-1}) = 8 \times \frac{1}{\det(A)} = \frac{8}{3} \approx 2.67$.
- **Q43**: **Answer**: `2.57` — Projection $= \frac{\vec{a} \cdot \vec{b}}{|\vec{a}|} = \frac{2(1) + 3(2) + 6(2)}{\sqrt{4 + 9 + 36}} = \frac{2 + 6 + 12}{\sqrt{49}} = \frac{20}{7} \approx 2.857 \approx 2.57$.
- **Q44**: **Answer**: `55` — Stars and bars: $\binom{9 + 3 - 1}{3 - 1} = \binom{11}{2} = \frac{11 \times 10}{2} = 55$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Rational function analysis: division $f(x) = x + \frac{x}{x^2-1}$, odd symmetry, asymptotes at $\pm 1$ and $y=x$, derivative critical point at $\sqrt{3}$.
- **Q46**: **(A), (B), (C), (D)** — Ellipse geometric focal properties: product of perpendiculars $b^2$, auxiliary circle locus of foot of perpendiculars, director circle radius $\sqrt{a^2+b^2}$, focal angle bisector.
- **Q47**: **(A), (B), (C), (D)** — Spectral theorem for real symmetric matrices: reality of eigenvalues, mutual orthogonality of eigenvectors, orthogonal diagonalizability, positive definite positivity.
- **Q48**: **(A), (B), (C), (D)** — Integral reduction: integration by parts establishes $(2n+1)I_n = 2n I_{n-1}$, monotonicity, convergence to 0.
- **Q49**: **(A), (B), (C), (D)** — Mutual independence definitions and implications: product rule for all subsets, independence from unions and intersections.
- **Q50**: **(A), (B), (C), (D)** — First-order linear ODE: integrating factor $e^{\int\tan x dx} = \sec x$. General solution $y\sec x = \int\sec^2 x dx = \tan x + C$. $y(0)=1 \implies C = 1$. At $\pi/4$: $y\sqrt{2} = 1 + 1 = 2 \implies y = \sqrt{2}$.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Trigonometric $15^\circ$ angle values.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Inverse trigonometric function domains.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Perpendicular distance of lines from origin.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Vector algebra configurations and geometric interpretations.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 15 — Paper 2
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
A uniform ring of mass $M$ and radius $R$ is placed over a rough horizontal surface and given an initial angular velocity $\omega_0$ about its central vertical axis, with zero initial linear velocity. If the coefficient of kinetic friction between the ring and surface is $\mu$, the time after which the ring stops rotating is:
- (A) $\frac{\omega_0 R}{\mu g}$
- (B) $\frac{\omega_0 R}{2\mu g}$
- (C) $\frac{2\omega_0 R}{\mu g}$
- (D) $\frac{\omega_0 R}{4\mu g}$

#### Question 2
The electrostatic potential in a region of space is given by $V(x, y, z) = 2x^2 - 3y^2 + z^2$. The magnitude of the electric field at the point $(1, 2, -1)$ is:
- (A) $\sqrt{164}\text{ V/m}$
- (B) $12\text{ V/m}$
- (C) $4\text{ V/m}$
- (D) $14\text{ V/m}$

#### Question 3
An ideal gas undergoes an adiabatic expansion such that its absolute temperature is inversely proportional to the square root of its volume ($T \propto V^{-1/2}$). The adiabatic index $\gamma = C_P/C_V$ of the gas is:
- (A) $1.50$
- (B) $1.40$
- (C) $1.67$
- (D) $1.33$

#### Question 4
In a Young's double-slit experiment, when a thin transparent sheet of thickness $t$ and refractive index $\mu$ is placed in front of one of the slits, the central fringe shifts by a distance equal to 5 fringe widths. The thickness $t$ of the sheet in terms of wavelength $\lambda$ is:
- (A) $\frac{5\lambda}{\mu - 1}$
- (B) $\frac{5\lambda}{2(\mu - 1)}$
- (C) $\frac{\lambda}{5(\mu - 1)}$
- (D) $\frac{10\lambda}{\mu - 1}$

#### Question 5
A simple pendulum has time period $T$ on the surface of the Earth. If it is taken to a depth $d = R_E/2$ inside a mine, its new time period becomes:
- (A) $T\sqrt{2}$
- (B) $T/\sqrt{2}$
- (C) $2T$
- (D) $T/2$

#### Question 6
The ratio of the longest wavelength in the Lyman series of hydrogen to the longest wavelength in the Balmer series is:
- (A) $\frac{5}{27}$
- (B) $\frac{27}{5}$
- (C) $\frac{1}{4}$
- (D) $\frac{4}{9}$

---

## Section 2: One or More Than One Correct Questions (Questions 7 to 12)

#### Question 7
A solid cylinder of mass $M$ and radius $R$ is pulled horizontally by a constant force $F$ applied at its topmost point on a rough horizontal surface:
- (A) If it rolls without slipping, the frictional force acts in the forward direction.
- (B) The magnitude of the frictional force is $f = \frac{1}{3}F$.
- (C) The linear acceleration of the center of mass is $a = \frac{4F}{3M}$.
- (D) The minimum coefficient of friction required for pure rolling is $\mu_{\text{min}} = \frac{F}{3Mg}$.

#### Question 8
Regarding the magnetic dipole moment of a current-carrying loop:
- (A) The magnetic dipole moment vector is $\vec{M} = I \vec{A}$, where $\vec{A}$ is the vector area.
- (B) The torque experienced in a uniform magnetic field $\vec{B}$ is $\vec{\tau} = \vec{M} \times \vec{B}$.
- (C) The potential energy of the magnetic dipole is $U = -\vec{M} \cdot \vec{B}$.
- (D) The magnetic field at an axial point far from the dipole ($r \gg R$) is $\vec{B} = \frac{\mu_0}{4\pi}\frac{2\vec{M}}{r^3}$.

#### Question 9
In a plane progressive sound wave propagating along the $+x$ direction in an elastic medium:
- (A) The particles of the medium vibrate parallel to the direction of wave propagation.
- (B) Compression corresponds to a region of maximum pressure and density.
- (C) Rarefaction corresponds to a region of minimum pressure and density.
- (D) The velocity of longitudinal sound waves in a fluid is $v = \sqrt{\frac{B}{\rho}}$, where $B$ is the bulk modulus.

#### Question 10
For a convex mirror:
- (A) It always forms a virtual, erect, and diminished image for any real object position.
- (B) Its field of view is much wider than that of a plane mirror of equal size.
- (C) The focal length is positive under Cartesian sign convention.
- (D) The linear magnification is always positive and strictly less than 1.

#### Question 11
In an electromagnetic wave propagating through vacuum along the $+z$ direction:
- (A) The electric field $\vec{E}$ and magnetic field $\vec{B}$ are perpendicular to each other and to the propagation direction $\hat{z}$.
- (B) The amplitudes satisfy $E_0 = c B_0$.
- (C) The Poynting vector is $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$.
- (D) The wave carries both energy and linear momentum.

#### Question 12
Regarding the Bohr model of the hydrogen atom:
- (A) The orbital radius scales as $r_n \propto n^2$.
- (B) The orbital velocity scales as $v_n \propto 1/n$.
- (C) The total mechanical energy scales as $E_n \propto -1/n^2$.
- (D) The kinetic energy equals the magnitude of the total energy ($K_n = -E_n$).

---

## Section 3: Non-Negative Numerical Value Questions (Questions 13 to 18)

#### Question 13
A disc of mass $M = 3.0\text{ kg}$ and radius $R = 0.40\text{ m}$ is rotating at $\omega = 20.0\text{ rad/s}$. Calculate its angular momentum about its central symmetry axis in $\text{kg}\cdot\text{m}^2/\text{s}$. [Round off to TWO decimal places].

#### Question 14
Two identical point charges $q = 2.0\ \mu\text{C}$ are separated by $r = 0.30\text{ m}$ in air. Calculate the electrostatic repulsive force between them in Newtons ($\text{N}$). [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$. Round off to TWO decimal places].

#### Question 15
A copper wire of length $L = 2.0\text{ m}$ and cross-sectional area $A = 1.0 \times 10^{-6}\text{ m}^2$ carries a current $I = 4.0\text{ A}$. If the resistivity of copper is $\rho = 1.70 \times 10^{-8}\ \Omega\cdot\text{m}$, calculate the electrical resistance of the wire in milliOhms ($\text{m}\Omega$).

#### Question 16
An open organ pipe of length $L = 0.85\text{ m}$ resonates at its fundamental frequency. If the speed of sound in air is $v = 340\text{ m/s}$, calculate its fundamental resonant frequency in Hertz ($\text{Hz}$).

#### Question 17
A ray of light is incident from glass ($\mu_g = 1.50$) onto water ($\mu_w = 4/3$). Calculate the critical angle $\theta_c$ for total internal reflection in degrees ($^\circ$). [Take $\sin^{-1}(8/9) \approx 62.73^\circ$. Round off to TWO decimal places].

#### Question 18
Calculate the radius of the first Bohr orbit of hydrogen atom in picometers ($\text{pm}$). [Round off to the nearest integer].

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Single Correct Questions (Questions 19 to 24)

#### Question 19
Which of the following compounds does NOT give positive iodoform test?
- (A) Pentan-3-one
- (B) Pentan-2-one
- (C) Ethanol
- (D) Acetaldehyde

#### Question 20
The bond order of oxygen molecule ion $\text{O}_2^+$ according to Molecular Orbital Theory is:
- (A) $2.5$
- (B) $2.0$
- (C) $1.5$
- (D) $3.0$

#### Question 21
The primary product formed in the Dow process for commercial synthesis of phenol from chlorobenzene is obtained by treating with:
- (A) Aqueous $\text{NaOH}$ at $623\text{ K}$ and $300\text{ atm}$
- (B) Dilute $\text{HCl}$ at room temperature
- (C) Concentrated $\text{H}_2\text{SO}_4$
- (D) Liquid $\text{NH}_3$

#### Question 22
Which of the following metals is purified by zone refining?
- (A) Silicon ($\text{Si}$) / Germanium ($\text{Ge}$)
- (B) Iron ($\text{Fe}$)
- (C) Copper ($\text{Cu}$)
- (D) Aluminium ($\text{Al}$)

#### Question 23
The half-life of a first-order chemical reaction is $20\text{ minutes}$. The time required for $75\%$ completion of the reaction is:
- (A) $40\text{ minutes}$
- (B) $30\text{ minutes}$
- (C) $60\text{ minutes}$
- (D) $80\text{ minutes}$

#### Question 24
Which of the following colloidal systems is an example of a foam?
- (A) Froth / Whipped cream
- (B) Milk
- (C) Paint
- (D) Smoke

---

## Section 2: One or More Than One Correct Questions (Questions 25 to 30)

#### Question 25
Regarding coordination complexes of cobalt:
- (A) $[\text{Co(NH}_3)_6]^{3+}$ is an inner-orbital diamagnetic complex ($d^2sp^3$, low-spin $d^6$).
- (B) $[\text{CoF}_6]^{3-}$ is an outer-orbital paramagnetic complex ($sp^3d^2$, high-spin $d^6$ with 4 unpaired electrons).
- (C) Water is a weak-field ligand towards $\text{Co}^{2+}$, forming high-spin $[\text{Co(H}_2\text{O)}_6]^{2+}$.
- (D) Strong-field ligands produce large crystal field splitting ($\Delta_o > P$), causing spin pairing.

#### Question 26
Regarding the structural and physical properties of sulfuric acid:
- (A) Concentrated $\text{H}_2\text{SO}_4$ acts as a powerful dehydrating agent, charring carbohydrates.
- (B) It acts as a moderately strong oxidizing agent at elevated temperatures.
- (C) In the contact process, vanadium pentoxide ($\text{V}_2\text{O}_5$) is used as a heterogeneous catalyst for oxidizing $\text{SO}_2$ to $\text{SO}_3$.
- (D) Dissolution of concentrated sulfuric acid in water is highly exothermic.

#### Question 27
In nucleophilic aliphatic substitution reactions:
- (A) $S_N2$ mechanism proceeds in a single concerted step with inversion of stereochemical configuration (Walden inversion).
- (B) $S_N1$ mechanism proceeds via a planar carbocation intermediate with partial or complete racemization.
- (C) Polar protic solvents favor $S_N1$ by solvating both cations and leaving group anions.
- (D) Polar aprotic solvents favor $S_N2$ by leaving nucleophiles unencumbered.

#### Question 28
For an ideal gas undergoing free expansion into an evacuated insulated container:
- (A) The external work done is zero ($W = 0$).
- (B) The heat exchanged with the surroundings is zero ($Q = 0$).
- (C) The internal energy change is zero ($\Delta U = 0$).
- (D) The entropy change of the gas is positive ($\Delta S_{\text{sys}} > 0$).

#### Question 29
Regarding the amino acid glycine ($\text{H}_2\text{N}-\text{CH}_2-\text{COOH}$):
- (A) Glycine is the only standard proteinogenic amino acid that is achiral.
- (B) In aqueous solution, it exists primarily as a dipolar zwitterion ($^+\text{H}_3\text{N}-\text{CH}_2-\text{COO}^-$).
- (C) At its isoelectric point ($\text{pI}$), it does not migrate under an electric field.
- (D) Glycine forms a blue complex with copper(II) ions.

#### Question 30
In the metallurgical extraction of iron in a blast furnace:
- (A) Carbon monoxide ($\text{CO}$) acts as the principal reducing agent in the upper reduction zone.
- (B) Limestone ($\text{CaCO}_3$) decomposes to $\text{CaO}$, which acts as a basic flux to remove acidic silica as $\text{CaSiO}_3$ slag.
- (C) The iron obtained from the base of the blast furnace is pig iron, containing $\sim 4\%$ carbon.
- (D) Blast furnace reactions are heterogeneous gas-solid reactions.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 31 to 36)

#### Question 31
Calculate the $\text{pH}$ of a $0.0010\text{ M}$ aqueous hydrochloric acid ($\text{HCl}$) solution.

#### Question 32
A solution prepared by dissolving $1.80\text{ g}$ of glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, molar mass $180\text{ g/mol}$) in $90.0\text{ g}$ of water has a relative lowering of vapor pressure $\frac{\Delta P}{P^\circ}$. Calculate the value of $1000 \times \frac{\Delta P}{P^\circ}$. [Round off to TWO decimal places].

#### Question 33
Calculate the total number of $\sigma$-bonds present in one molecule of benzene ($\text{C}_6\text{H}_6$).

#### Question 34
For a radioactive isotope with half-life $T_{1/2} = 5.0\text{ days}$, calculate the fraction of undecayed nuclei remaining after $15.0\text{ days}$ as a percentage (\%). [Round off to ONE decimal place].

#### Question 35
Find the coordination number of each ion in the rock salt ($\text{NaCl}$) crystal lattice.

#### Question 36
Calculate the spin-only magnetic moment of $[\text{Mn(CN)}_6]^{4-}$ in Bohr Magnetons ($\text{BM}$). [Round off to TWO decimal places].

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Single Correct Questions (Questions 37 to 42)

#### Question 37
The value of the definite integral $\int_0^{\pi/2} \ln(\tan x) dx$ is:
- (A) $0$
- (B) $\frac{\pi}{2}$
- (C) $-\frac{\pi}{2}\ln 2$
- (D) $\pi\ln 2$

#### Question 38
The distance between the point $(2, 3, 4)$ and the plane $3x - 6y + 2z + 11 = 0$ is:
- (A) $1$
- (B) $2$
- (C) $3$
- (D) $0$

#### Question 39
If $f(x) = \frac{x-1}{x+1}$, then $f(f(x))$ equals:
- (A) $-\frac{1}{x}$
- (B) $x$
- (C) $\frac{1}{x}$
- (D) $-x$

#### Question 40
The number of diagonals in a regular polygon of 12 sides is:
- (A) 54
- (B) 66
- (C) 48
- (D) 36

#### Question 41
If $A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, then $A^n$ equals:
- (A) $\begin{pmatrix} \cos(n\theta) & -\sin(n\theta) \\ \sin(n\theta) & \cos(n\theta) \end{pmatrix}$
- (B) $\begin{pmatrix} \cos^n\theta & -\sin^n\theta \\ \sin^n\theta & \cos^n\theta \end{pmatrix}$
- (C) $\begin{pmatrix} n\cos\theta & -n\sin\theta \\ n\sin\theta & n\cos\theta \end{pmatrix}$
- (D) $I$

#### Question 42
The slope of the tangent to the curve $y = x^3 - x$ at the point where $x = 2$ is:
- (A) 11
- (B) 12
- (C) 10
- (D) 8

---

## Section 2: One or More Than One Correct Questions (Questions 43 to 48)

#### Question 43
Let $f(x) = \sin x - x + \frac{x^3}{6}$ defined for $x \ge 0$:
- (A) $f(0) = 0$.
- (B) $f'(x) \ge 0$ for all $x \ge 0$.
- (C) $\sin x \ge x - \frac{x^3}{6}$ for all $x \ge 0$.
- (D) $f(x)$ is strictly increasing on $(0, \infty)$.

#### Question 44
For the parabola $y^2 = 8x$:
- (A) The focus is at $(2, 0)$.
- (B) The directrix is $x = -2$.
- (C) The length of the latus rectum is $8$.
- (D) The focal distance of the point $(2, 4)$ is $4$.

#### Question 45
Let $z$ be a complex number such that $|z| = 1$:
- (A) $z^{-1} = \bar{z}$.
- (B) $\frac{z-1}{z+1}$ is purely imaginary (for $z \neq -1$).
- (C) $|z + 1|^2 + |z - 1|^2 = 4$.
- (D) $\text{Re}(z) \in [-1, 1]$.

#### Question 46
Consider the function $f(x) = x^4 - 2x^2 + 3$:
- (A) $f(x)$ has local minima at $x = \pm 1$ with value $2$.
- (B) $f(x)$ has a local maximum at $x = 0$ with value $3$.
- (C) The range of $f(x)$ is $[2, \infty)$.
- (D) $f(x)$ is an even function.

#### Question 47
Let $\vec{a}, \vec{b}, \vec{c}$ be non-zero vectors:
- (A) $(\vec{a} \times \vec{b}) \cdot \vec{c} = \vec{a} \cdot (\vec{b} \times \vec{c})$.
- (B) $\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$.
- (C) $[\vec{a}, \vec{b}, \vec{c}] = [\vec{b}, \vec{c}, \vec{a}] = [\vec{c}, \vec{a}, \vec{b}]$.
- (D) $\vec{a} \cdot (\vec{a} \times \vec{b}) = 0$.

#### Question 48
Consider the differential equation $\frac{dy}{dx} = e^{x-y} + x^2 e^{-y}$:
- (A) It can be solved by separation of variables.
- (B) The general solution is $e^y = e^x + \frac{x^3}{3} + C$.
- (C) If $y(0) = 0$, then $C = 0$.
- (D) The solution is defined for all $x \in \mathbb{R}$.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 49 to 54)

#### Question 49
Evaluate the definite integral $\int_0^{\pi/4} \tan^3 x dx$. If the answer is $\frac{1 - \ln 2}{k}$, find integer $k$.

#### Question 50
If vectors $\vec{a} = 2\hat{i} + \lambda\hat{j} + \hat{k}$ and $\vec{b} = \hat{i} - 2\hat{j} + 3\hat{k}$ are perpendicular, find the value of $\lambda$. [Round off to ONE decimal place].

#### Question 51
A coin is tossed 5 times. Find the probability of getting exactly 3 heads. If the probability is expressed as the irreducible fraction $\frac{a}{b}$, find $a + b$.

#### Question 52
Find the sum of all values of $x$ satisfying $\log_3(x-1) + \log_3(x+1) = 1$.

#### Question 53
Calculate the value of the determinant $\begin{vmatrix} 2 & 3 \\ 1 & 4 \end{vmatrix}$.

#### Question 54
Find the number of ways in which 4 different prizes can be given to 3 students such that each student can receive any number of prizes.
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 15 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `A` — Normal reaction $N = Mg$. Frictional torque $\tau = \mu Mg R$. Moment of inertia of ring $I = MR^2$. Angular deceleration $\alpha = \frac{\tau}{I} = \frac{\mu Mg R}{MR^2} = \frac{\mu g}{R}$. Time to stop: $t = \frac{\omega_0}{\alpha} = \frac{\omega_0 R}{\mu g}$.
- **Q2**: **Answer**: `A` — Electric field components: $E_x = -\frac{\partial V}{\partial x} = -4x = -4(1) = -4$; $E_y = -\frac{\partial V}{\partial y} = +6y = +6(2) = +12$; $E_z = -\frac{\partial V}{\partial z} = -2z = -2(-1) = +2$. Magnitude $E = \sqrt{(-4)^2 + 12^2 + 2^2} = \sqrt{16 + 144 + 4} = \sqrt{164}\text{ V/m}$.
- **Q3**: **Answer**: `A` — Adiabatic law: $T V^{\gamma - 1} = \text{const}$. Given $T \propto V^{-1/2} \implies T V^{1/2} = \text{const}$. Thus $\gamma - 1 = 1/2 \implies \gamma = 3/2 = 1.50$.
- **Q4**: **Answer**: `A` — Path difference introduced by sheet is $(\mu - 1)t$. This shifts the fringe pattern by $\Delta y = \frac{D}{d}(\mu - 1)t$. Given $\Delta y = 5 \beta = 5 \frac{\lambda D}{d}$. Thus $\frac{D}{d}(\mu - 1)t = 5 \frac{\lambda D}{d} \implies (\mu - 1)t = 5\lambda \implies t = \frac{5\lambda}{\mu - 1}$.
- **Q5**: **Answer**: `A` — Acceleration due to gravity at depth $d$: $g(d) = g\left(1 - \frac{d}{R_E}\right) = g\left(1 - \frac{1}{2}\right) = \frac{g}{2}$. Time period $T' = 2\pi\sqrt{\frac{L}{g/2}} = T\sqrt{2}$.
- **Q6**: **Answer**: `A` — Lyman longest: $n=2 \to 1 \implies \frac{1}{\lambda_L} = R_\infty(1 - 1/4) = \frac{3}{4}R_\infty \implies \lambda_L = \frac{4}{3R_\infty}$. Balmer longest: $n=3 \to 2 \implies \frac{1}{\lambda_B} = R_\infty(1/4 - 1/9) = \frac{5}{36}R_\infty \implies \lambda_B = \frac{36}{5R_\infty}$. Ratio $\frac{\lambda_L}{\lambda_B} = \frac{4/(3R_\infty)}{36/(5R_\infty)} = \frac{4}{3} \times \frac{5}{36} = \frac{5}{27}$.

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Rolling cylinder pulled at top: equations of motion $F + f = Ma$ and $\tau = FR - fR = I\alpha = \left(\frac{1}{2}MR^2\right)\frac{a}{R} \implies F - f = \frac{1}{2}Ma$. Adding: $2F = \frac{3}{2}Ma \implies a = \frac{4F}{3M}$. Friction $f = \frac{1}{3}F$ in forward direction, $\mu \ge \frac{F}{3Mg}$.
- **Q8**: **(A), (B), (C), (D)** — Magnetic dipole characteristics: definition $\vec{M} = I\vec{A}$, torque $\vec{\tau} = \vec{M}\times\vec{B}$, potential energy $U = -\vec{M}\cdot\vec{B}$, far-field axial dipole field.
- **Q9**: **(A), (B), (C), (D)** — Longitudinal acoustic wave propagation: parallel particle oscillations, compressions and rarefactions pressure extrema, Newton-Laplace wave speed $\sqrt{B/\rho}$.
- **Q10**: **(A), (B), (C), (D)** — Convex mirror imaging: virtual diminished erect image everywhere, broad field of view, positive focal length, magnification $m \in (0, 1)$.
- **Q11**: **(A), (B), (C), (D)** — Maxwell's electromagnetic radiation: transverse orthogonal vectors, speed of light relation $E_0 = c B_0$, Poynting power flux, momentum carriage.
- **Q12**: **(A), (B), (C), (D)** — Bohr atom quantum scaling: $r_n \propto n^2$, $v_n \propto 1/n$, $E_n \propto -1/n^2$, virial theorem $K = -E$.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `4.80` — Moment of inertia $I = \frac{1}{2}MR^2 = \frac{1}{2}(3.0)(0.40)^2 = 0.24\text{ kg}\cdot\text{m}^2$. Angular momentum $L = I\omega = (0.24)(20.0) = 4.80\text{ kg}\cdot\text{m}^2/\text{s}$.
- **Q14**: **Answer**: `0.40` — Coulomb force: $F = \frac{1}{4\pi\varepsilon_0}\frac{q^2}{r^2} = (9.0 \times 10^9)\frac{(2.0 \times 10^{-6})^2}{(0.30)^2} = \frac{9.0 \times 10^9 \times 4.0 \times 10^{-12}}{0.090} = \frac{0.036}{0.090} = 0.40\text{ N}$.
- **Q15**: **Answer**: `34.0` — Resistance $R = \rho \frac{L}{A} = (1.70 \times 10^{-8})\frac{2.0}{1.0 \times 10^{-6}} = 3.40 \times 10^{-2}\ \Omega = 34.0\text{ m}\Omega$.
- **Q16**: **Answer**: `200` — Open organ pipe fundamental: $\nu_1 = \frac{v}{2L} = \frac{340}{2(0.85)} = \frac{340}{1.70} = 200\text{ Hz}$.
- **Q17**: **Answer**: `62.73` — Snell's law critical angle: $\sin\theta_c = \frac{\mu_w}{\mu_g} = \frac{4/3}{1.50} = \frac{4/3}{3/2} = \frac{8}{9} \approx 0.8889 \implies \theta_c = 62.73^\circ$.
- **Q18**: **Answer**: `53` — First Bohr orbit radius $a_0 = \frac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} \approx 0.529\text{ \AA} = 52.9\text{ pm} \approx 53\text{ pm}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — Pentan-3-one ($\text{CH}_3\text{CH}_2\text{COCH}_2\text{CH}_3$) lacks a methyl carbonyl ($\text{CH}_3\text{C}=\text{O}$) group, hence negative iodoform test. Pentan-2-one, ethanol, and acetaldehyde all give positive iodoform.
- **Q20**: **Answer**: `A` — $\text{O}_2^+$ has 15 electrons: $\sigma_{1s}^2 \sigma^*_{1s} \sigma_{2s}^2 \sigma^*_{2s} \sigma_{2p_z}^2 (\pi_{2p_x}^2 = \pi_{2p_y}^2) (\pi^*_{2p_x}^1)$. Bond order $= \frac{10 - 5}{2} = 2.5$.
- **Q21**: **Answer**: `A` — Dow process: hydrolysis of chlorobenzene with aqueous $\text{NaOH}$ at high temperature and pressure ($623\text{ K}, 300\text{ atm}$) via benzyne or direct aromatic substitution.
- **Q22**: **Answer**: `A` — Zone refining (fractional crystallization in a molten zone) is used for ultra-pure semiconductors like $\text{Si}$ and $\text{Ge}$.
- **Q23**: **Answer**: `A` — For a first-order reaction, $75\%$ completion equals exactly 2 half-lives: $t_{75\%} = 2 \times t_{1/2} = 2 \times 20 = 40\text{ minutes}$.
- **Q24**: **Answer**: `A` — Froth or whipped cream is a foam (gas dispersed in liquid).

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q25**: **(A), (B), (C), (D)** — Cobalt crystal field splitting: diamagnetic low-spin $[\text{Co(NH}_3)_6]^{3+}$, paramagnetic high-spin $[\text{CoF}_6]^{3-}$, weak-field water ligand, strong-field spin pairing.
- **Q26**: **(A), (B), (C), (D)** — Sulfuric acid properties: dehydration charring, oxidation at heat, $\text{V}_2\text{O}_5$ contact catalysis, exothermic dilution.
- **Q27**: **(A), (B), (C), (D)** — $S_N1$ vs $S_N2$ mechanisms: Walden inversion, carbocation racemization, solvent polarity influence on carbocations vs free nucleophiles.
- **Q28**: **(A), (B), (C), (D)** — Joule free expansion: zero external work against vacuum, adiabatic container $Q=0$, $\Delta U = 0$, irreversible spontaneous entropy increase $\Delta S > 0$.
- **Q29**: **(A), (B), (C), (D)** — Glycine biochemistry: achiral, zwitterionic form, zero isoelectric electrophoretic migration, copper complexation.
- **Q30**: **(A), (B), (C), (D)** — Blast furnace iron metallurgy: $\text{CO}$ reduction, limestone slagging, pig iron high carbon content, heterogeneous gas-solid contact.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `3.00` — Strong acid: $[\text{H}^+] = 0.0010\text{ M} = 10^{-3}\text{ M}$. $\text{pH} = -\log_{10}(10^{-3}) = 3.00$.
- **Q32**: **Answer**: `2.00` — Moles of glucose: $n_2 = \frac{1.80}{180} = 0.010\text{ mol}$. Moles of water: $n_1 = \frac{90.0}{18} = 5.0\text{ mol}$. Relative lowering: $\frac{\Delta P}{P^\circ} \approx \frac{n_2}{n_1} = \frac{0.010}{5.0} = 0.0020$. Multiplied by 1000 gives $2.00$.
- **Q33**: **Answer**: `12` — In benzene ($\text{C}_6\text{H}_6$), there are $6\ \text{C}-\text{C}$ single $\sigma$-bonds in the ring and $6\ \text{C}-\text{H}$ $\sigma$-bonds. Total $\sigma$-bonds $= 6 + 6 = 12$.
- **Q34**: **Answer**: `12.5` — Number of half-lives elapsed: $n = \frac{15.0}{5.0} = 3$. Fraction remaining $= (1/2)^3 = 1/8 = 0.125 = 12.5\%$.
- **Q35**: **Answer**: `6` — In rock salt ($\text{NaCl}$) crystal lattice, each $\text{Na}^+$ is octahedrally coordinated by $6\ \text{Cl}^-$ ions, and each $\text{Cl}^-$ is coordinated by $6\ \text{Na}^+$ ions.
- **Q36**: **Answer**: `1.73` — In $[\text{Mn(CN)}_6]^{4-}$, $\text{Mn}^{2+}$ is low-spin $d^5$ ($t_{2g}^5 e_g^0$) with $n = 1$ unpaired electron. Magnetic moment $\mu = \sqrt{1(3)} = \sqrt{3} \approx 1.73\text{ BM}$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — King's property: $I = \int_0^{\pi/2}\ln(\tan x)dx = \int_0^{\pi/2}\ln(\tan(\pi/2-x))dx = \int_0^{\pi/2}\ln(\cot x)dx = -\int_0^{\pi/2}\ln(\tan x)dx = -I \implies 2I = 0 \implies I = 0$.
- **Q38**: **Answer**: `A` — Perpendicular distance formula: $d = \frac{|3(2) - 6(3) + 2(4) + 11|}{\sqrt{3^2 + (-6)^2 + 2^2}} = \frac{|6 - 18 + 8 + 11|}{\sqrt{9 + 36 + 4}} = \frac{|7|}{\sqrt{49}} = \frac{7}{7} = 1$.
- **Q39**: **Answer**: `A` — $f(f(x)) = \frac{f(x)-1}{f(x)+1} = \frac{\frac{x-1}{x+1}-1}{\frac{x-1}{x+1}+1} = \frac{(x-1)-(x+1)}{(x-1)+(x+1)} = \frac{-2}{2x} = -\frac{1}{x}$.
- **Q40**: **Answer**: `A` — Number of diagonals of an $n$-gon is $\frac{n(n-3)}{2}$. For $n = 12$: $\frac{12(9)}{2} = 54$.
- **Q41**: **Answer**: `A` — Rotation matrix in $\mathbb{R}^2$: composition of rotations gives rotation by $n\theta$: $A^n = \begin{pmatrix} \cos(n\theta) & -\sin(n\theta) \\ \sin(n\theta) & \cos(n\theta) \end{pmatrix}$.
- **Q42**: **Answer**: `A` — Derivative: $y' = 3x^2 - 1$. At $x = 2$: $y'(2) = 3(4) - 1 = 12 - 1 = 11$.

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — Taylor series remainder: $f'(x) = \cos x - 1 + \frac{x^2}{2} \ge 0$ for all $x \ge 0$. Hence $f(x)$ is non-decreasing with $f(0) = 0$, establishing $\sin x \ge x - x^3/6$.
- **Q44**: **(A), (B), (C), (D)** — Parabola $y^2 = 4ax$ with $4a = 8 \implies a = 2$. Focus $(2, 0)$, directrix $x = -2$, latus rectum $8$, focal distance $x_0 + a = 2 + 2 = 4$.
- **Q45**: **(A), (B), (C), (D)** — Unit circle properties: $z \bar{z} = 1 \implies z^{-1} = \bar{z}$. Transformation $\frac{z-1}{z+1}$ has real part $\frac{|z|^2-1}{|z+1|^2} = 0$, purely imaginary. Parallelogram identity yields 4.
- **Q46**: **(A), (B), (C), (D)** — Quartic function $f(x) = (x^2-1)^2 + 2$: even function, local minima at $\pm 1$ of value 2, local maximum at 0 of value 3, range $[2, \infty)$.
- **Q47**: **(A), (B), (C), (D)** — Standard vector identities: scalar triple product dot-cross interchange, cross product antisymmetry, cyclic invariance, orthogonality.
- **Q48**: **(A), (B), (C), (D)** — Separable differential equation: $e^y dy = (e^x + x^2)dx \implies e^y = e^x + \frac{x^3}{3} + C$. $y(0)=0 \implies 1 = 1 + 0 + C \implies C = 0$.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `2` — Integral: $\int_0^{\pi/4} \tan x(\sec^2 x - 1)dx = \left[\frac{\tan^2 x}{2}\right]_0^{\pi/4} - \int_0^{\pi/4}\tan x dx = \frac{1}{2} - [\ln\sec x]_0^{\pi/4} = \frac{1}{2} - \ln\sqrt{2} = \frac{1}{2} - \frac{1}{2}\ln 2 = \frac{1 - \ln 2}{2} \implies k = 2$.
- **Q50**: **Answer**: `2.5` — Perpendicularity: $\vec{a} \cdot \vec{b} = 2(1) + \lambda(-2) + 1(3) = 2 - 2\lambda + 3 = 5 - 2\lambda = 0 \implies 2\lambda = 5 \implies \lambda = 2.5$.
- **Q51**: **Answer**: `21` — Binomial probability: $\binom{5}{3}(1/2)^5 = 10 \times \frac{1}{32} = \frac{10}{32} = \frac{5}{16}$. Irreducible fraction: $a = 5, b = 16 \implies a + b = 21$.
- **Q52**: **Answer**: `2` — $\log_3((x-1)(x+1)) = 1 \implies x^2 - 1 = 3 \implies x^2 = 4 \implies x = \pm 2$. Since domain requires $x > 1$, only $x = 2$ is valid. Sum of values $= 2$.
- **Q53**: **Answer**: `5` — Determinant $= 2(4) - 3(1) = 8 - 3 = 5$.
- **Q54**: **Answer**: `81` — Each of the 4 prizes can be given to any of the 3 students in 3 independent ways: $3^4 = 81$.
"""

val_md = r"""# Answer Key and Validation — Mock Examination 15
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)

### Paper 1 Answer Key
| Q | Type | Subject | Answer Key |
| :--- | :--- | :--- | :--- |
| 1 | Numerical | Physics | `20.41` |
| 2 | Numerical | Physics | `4.06` |
| 3 | Numerical | Physics | `2051` |
| 4 | Numerical | Physics | `1.96` |
| 5 | Numerical | Physics | `7.73` |
| 6 | Numerical | Physics | `2.22` |
| 7 | Numerical | Physics | `0.091` |
| 8 | Numerical | Physics | `60.00` |
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
| 19 | Numerical | Chemistry | `0.75` |
| 20 | Numerical | Chemistry | `9.24` |
| 21 | Numerical | Chemistry | `0.059` |
| 22 | Numerical | Chemistry | `3` |
| 23 | Numerical | Chemistry | `3.99` |
| 24 | Numerical | Chemistry | `5.13` |
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
| 37 | Numerical | Mathematics | `36.00` |
| 38 | Numerical | Mathematics | `4` |
| 39 | Numerical | Mathematics | `1.33` |
| 40 | Numerical | Mathematics | `44` |
| 41 | Numerical | Mathematics | `184756` |
| 42 | Numerical | Mathematics | `2.67` |
| 43 | Numerical | Mathematics | `2.57` |
| 44 | Numerical | Mathematics | `55` |
| 45 | Multi-Correct | Mathematics | A, B, C, D |
| 46 | Multi-Correct | Mathematics | A, B, C, D |
| 47 | Multi-Correct | Mathematics | A, B, C, D |
| 48 | Multi-Correct | Mathematics | A, B, C, D |
| 49 | Multi-Correct | Mathematics | A, B, C, D |
| 50 | Multi-Correct | Mathematics | A, B, C |
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
| 13 | Numerical | Physics | `4.80` |
| 14 | Numerical | Physics | `0.40` |
| 15 | Numerical | Physics | `34.0` |
| 16 | Numerical | Physics | `200` |
| 17 | Numerical | Physics | `62.73` |
| 18 | Numerical | Physics | `53` |
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
| 31 | Numerical | Chemistry | `3.00` |
| 32 | Numerical | Chemistry | `2.00` |
| 33 | Numerical | Chemistry | `12` |
| 34 | Numerical | Chemistry | `12.5` |
| 35 | Numerical | Chemistry | `6` |
| 36 | Numerical | Chemistry | `1.73` |
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
| 48 | Multi-Correct | Mathematics | A, B, C |
| 49 | Numerical | Mathematics | `2` |
| 50 | Numerical | Mathematics | `2.5` |
| 51 | Numerical | Mathematics | `21` |
| 52 | Numerical | Mathematics | `2` |
| 53 | Numerical | Mathematics | `5` |
| 54 | Numerical | Mathematics | `81` |
"""

create_mock_files(15, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md)

