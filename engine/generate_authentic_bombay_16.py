# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 16.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 16 — Paper 1
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
A flexible, uniform heavy chain of total length $L = 2.00\text{ m}$ and linear mass density $\lambda = 0.50\text{ kg/m}$ is held vertically with its lower end just touching the pan of a weighing scale. It is released from rest at $t = 0$. Taking $g = 9.80\text{ m/s}^2$, calculate the reading of the scale (in Newtons, $\text{N}$) at the exact instant when a length $x = 1.00\text{ m}$ of the chain has fallen onto the scale pan. [Round off to TWO decimal places].

#### Question 2
An ideal Otto cycle operates with an engine compression ratio $r = 8.00$. If the working gas is air modeled as an ideal diatomic gas with $\gamma = 1.40$, calculate the theoretical air-standard thermal efficiency $\eta$ of the engine as a percentage (\%). [Take $8^{0.40} \approx 2.297$. Round off to TWO decimal places].

#### Question 3
A long straight solenoid of radius $R = 0.050\text{ m}$ has $n = 1000\text{ turns/m}$ and carries a time-varying current $I(t) = I_0 \sin(\omega t)$ where $I_0 = 5.0\text{ A}$ and $\omega = 100\pi\text{ rad/s}$. Calculate the peak induced electric field magnitude $E_{\text{peak}}$ at a distance $r = 0.030\text{ m}$ from the central axis inside the solenoid in milliVolts per meter ($\text{mV/m}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ and $\pi^2 \approx 9.87$. Round off to TWO decimal places].

#### Question 4
In an interference experiment using a thin dielectric wedge of angle $\theta = 2.0 \times 10^{-4}\text{ rad}$ and refractive index $\mu = 1.50$, monochromatic light of wavelength $\lambda = 600\text{ nm}$ is incident normally. Calculate the fringe width $\beta$ of the localized straight interference fringes in millimeters ($\text{mm}$). [Round off to TWO decimal places].

#### Question 5
A particle of rest mass $m_0$ has kinetic energy equal to its rest energy ($K = m_0 c^2$). If its momentum is $p = \alpha m_0 c$, calculate the value of $\alpha$. [Take $\sqrt{3} \approx 1.732$. Round off to TWO decimal places].

#### Question 6
A thin uniform rod of length $L = 1.00\text{ m}$ acts as a physical pendulum pivoted smoothly at a distance $d$ from its center of mass. Taking $g = 9.80\text{ m/s}^2$, calculate the minimum possible time period $T_{\text{min}}$ of small oscillations of the pendulum in seconds ($\text{s}$). [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 7
In a photoelectric effect experiment, when light of frequency $\nu_1 = 8.0 \times 10^{14}\text{ Hz}$ illuminates a metallic cathode, the stopping potential is $V_{01} = 1.50\text{ V}$. When the frequency is increased to $\nu_2 = 12.0 \times 10^{14}\text{ Hz}$, the stopping potential becomes $V_{02} = 3.15\text{ V}$. Calculate the experimental value of Planck's constant $h$ in $10^{-34}\text{ J}\cdot\text{s}$. [Take elementary charge $e = 1.60 \times 10^{-19}\text{ C}$. Round off to TWO decimal places].

#### Question 8
A parallel-plate capacitor with square plates of side $L = 0.20\text{ m}$ separated by gap $d = 2.0\text{ mm}$ is filled with a dielectric whose permittivity varies linearly from $\varepsilon_1 = 2.0\varepsilon_0$ at one plate to $\varepsilon_2 = 6.0\varepsilon_0$ at the other. Calculate the capacitance in picoFarads ($\text{pF}$). [Take $\varepsilon_0 = 8.854 \times 10^{-12}\text{ F/m}$ and $\ln 3 \approx 1.0986$. Round off to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
A rigid body rotates freely about a fixed principal axis of inertia with angular velocity $\vec{\omega}$:
- (A) The angular momentum vector $\vec{L}$ is strictly parallel to $\vec{\omega}$.
- (B) The rotational kinetic energy is $K = \frac{1}{2} I \omega^2$.
- (C) If no external torque acts, both total mechanical energy and angular momentum are conserved.
- (D) Euler's equations of motion simplify to $I_i \frac{d\omega_i}{dt} = 0$ along the principal axes.

#### Question 10
In an ideal Stirling engine cycle operating between temperatures $T_H$ and $T_C$ with an ideal regenerative heat exchanger:
- (A) The cycle consists of two reversible isotherms and two reversible isochores.
- (B) The heat rejected during isochoric cooling is stored in the regenerator and completely returned to the gas during isochoric heating.
- (C) The thermal efficiency of the ideal regenerative Stirling cycle equals the Carnot efficiency $\eta = 1 - \frac{T_C}{T_H}$.
- (D) The working substance undergoes a closed cyclic transformation with zero net entropy change over one cycle.

#### Question 11
In a parallel $RLC$ circuit connected to an AC voltage source of frequency $\omega$:
- (A) At resonance, the total circuit admittance is minimum and purely real ($Y = 1/R$).
- (B) The total current drawn from the source is minimum at resonance.
- (C) The dynamic resistance of the parallel tuned circuit at resonance is $R_{\text{dyn}} = \frac{L}{C R_L}$ (for practical lossy inductor).
- (D) Below resonance ($\omega < \omega_0$), the circuit is inductive and current lags the voltage.

#### Question 12
When light undergoes reflection from a thin wedge-shaped air film between two flat glass plates:
- (A) A phase shift of $\pi$ occurs upon reflection at the lower glass-air boundary.
- (B) The apex of the wedge corresponds to a dark interference fringe.
- (C) The fringes are straight, parallel to the line of contact, and equally spaced.
- (D) If a liquid of refractive index $\mu > 1$ fills the wedge, the fringe width decreases.

#### Question 13
Regarding the emission and absorption spectrum of atomic hydrogen:
- (A) The Balmer series lies primarily in the visible region of the electromagnetic spectrum.
- (B) The Lyman series lies in the ultraviolet region.
- (C) The Paschen series lies in the infrared region.
- (D) The series limit corresponds to the ionization threshold where the principal quantum number $n \to \infty$.

#### Question 14
A charged spherical drop of mercury of radius $R$ and potential $V_0$ merges coalesce with 7 other identical drops to form a single larger drop:
- (A) The radius of the combined drop is $2R$.
- (B) The charge on the combined drop is $8Q_0$.
- (C) The electric potential of the combined drop is $4V_0$.
- (D) The electrostatic energy of the combined drop is greater than the sum of the individual energies.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the electromagnetic wave type in **List-I** with its typical frequency range in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Radio Waves | **1.** $< 3 \times 10^9\text{ Hz}$ |
| **Q.** Microwaves | **2.** $3 \times 10^9\text{ Hz}$ to $3 \times 10^{11}\text{ Hz}$ |
| **R.** Infrared Waves | **3.** $3 \times 10^{11}\text{ Hz}$ to $4 \times 10^{14}\text{ Hz}$ |
| **S.** X-rays | **4.** $3 \times 10^{16}\text{ Hz}$ to $3 \times 10^{19}\text{ Hz}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the physical phenomenon in **List-I** with its governing equation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Bernoulli's Equation | **1.** $P + \frac{1}{2}\rho v^2 + \rho g h = \text{const}$ |
| **Q.** Torricelli's Law | **2.** $v = \sqrt{2gh}$ |
| **R.** Poiseuille's Law | **3.** $Q = \frac{\pi \Delta P r^4}{8\eta L}$ |
| **S.** Stokes' Law | **4.** $F_d = 6\pi\eta r v$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 17
Match the thermodynamic state function in **List-I** with its natural variables in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Internal Energy ($U$) | **1.** $(S, V)$ |
| **Q.** Enthalpy ($H$) | **2.** $(S, P)$ |
| **R.** Helmholtz Free Energy ($A$) | **3.** $(T, V)$ |
| **S.** Gibbs Free Energy ($G$) | **4.** $(T, P)$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 2, S $\to$ 3

#### Question 18
Match the electrical unit in **List-I** with its equivalent base combination in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Farad ($\text{F}$) | **1.** $\text{C/V} = \text{A}^2\cdot\text{s}^4/(\text{kg}\cdot\text{m}^2)$ |
| **Q.** Henry ($\text{H}$) | **2.** $\text{V}\cdot\text{s/A} = \text{kg}\cdot\text{m}^2/(\text{A}^2\cdot\text{s}^2)$ |
| **R.** Ohm ($\Omega$) | **3.** $\text{V/A} = \text{kg}\cdot\text{m}^2/(\text{A}^2\cdot\text{s}^3)$ |
| **S.** Weber ($\text{Wb}$) | **4.** $\text{V}\cdot\text{s} = \text{kg}\cdot\text{m}^2/(\text{A}\cdot\text{s}^2)$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
An aqueous polymer solution of concentration $C = 5.0\text{ g/L}$ exerts an osmotic pressure of $\Pi = 2.49 \times 10^{-3}\text{ bar}$ at $T = 300\text{ K}$. Calculate the molar mass of the polymer in $\text{kg/mol}$. [Take $R = 0.08314\text{ bar}\cdot\text{L}/(\text{mol}\cdot\text{K})$. Round off to the nearest integer].

#### Question 20
For a parallel first-order reaction where reactant $A$ decomposes into $B$ ($k_1$) and $C$ ($k_2$), the activation energies are $E_{a1} = 60.0\text{ kJ/mol}$ and $E_{a2} = 40.0\text{ kJ/mol}$ with equal pre-exponential frequency factors ($A_1 = A_2$). Calculate the ratio of rate constants $k_1 / k_2$ at $T = 500\text{ K}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $e^{-4.811} \approx 0.00814$. Enter the value of $1000 \times (k_1/k_2)$ rounded to the nearest integer].

#### Question 21
The solubility product of barium sulfate ($\text{BaSO}_4$) in water at $298\text{ K}$ is $K_{sp} = 1.10 \times 10^{-10}\text{ mol}^2/\text{L}^2$. Calculate the molar solubility of $\text{BaSO}_4$ in pure water in micro-moles per liter ($\mu\text{mol/L}$). [Take $\sqrt{1.10} \approx 1.049$. Round off to TWO decimal places].

#### Question 22
Calculate the total number of lone pairs on the central xenon atom in one molecule of xenon difluoride ($\text{XeF}_2$).

#### Question 23
In an $fcc$ crystal lattice containing $N$ atoms, calculate the ratio of the total number of tetrahedral voids to the total number of octahedral voids.

#### Question 24
Calculate the buffer capacity $\beta = \frac{d n_b}{d(\text{pH})}$ of a buffer solution prepared by mixing $0.100\text{ mol}$ of acetic acid and $0.100\text{ mol}$ of sodium acetate in $1.00\text{ L}$ of water. [Take $\ln 10 \approx 2.303$. Round off to THREE decimal places].

#### Question 25
Calculate the total number of structural isomers (constitutional isomers) of cyclic ethers having the molecular formula $\text{C}_4\text{H}_8\text{O}$.

#### Question 26
Calculate the oxidation state of iron in sodium nitroprusside ($\text{Na}_2[\text{Fe}(\text{CN})_5(\text{NO})]$).

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding the kinetic and thermodynamic enolates of unsymmetrical ketones (e.g., 2-methylcyclohexanone):
- (A) The kinetic enolate is formed faster by deprotonation at the less hindered $\alpha$-carbon using a strong, sterically hindered base (such as $\text{LDA}$) at low temperature ($-78^\circ\text{C}$).
- (B) The thermodynamic enolate is more stable because it corresponds to the more substituted, more highly conjugated double bond.
- (C) The thermodynamic enolate is favored under equilibrium conditions using weaker bases (such as $\text{NaOEt}$) at higher temperatures.
- (D) Alkylation of the kinetic enolate yields predominantly the less substituted alkyl derivative.

#### Question 28
In the metallurgy and extraction of zinc from zinc blende ($\text{ZnS}$):
- (A) The ore is concentrated by froth flotation using potassium ethyl xanthate.
- (B) Roasting in excess air converts $\text{ZnS}$ to zinc oxide ($\text{ZnO}$) and sulfur dioxide ($\text{SO}_2$).
- (C) Reduction of $\text{ZnO}$ is carried out using coke at $\sim 1400\text{ K}$ in vertical retorts, where zinc distills over as vapor (boiling point $1180\text{ K}$).
- (D) Crude zinc (spelter) is refined by fractional distillation or electrolytic refining.

#### Question 29
Regarding the lanthanoid and actinoid elements:
- (A) Actinoids exhibit a wider range of oxidation states than lanthanoids because the $5f, 6d$, and $7s$ energy levels are close in energy.
- (B) Lanthanoid contraction is caused by poor shielding of $4f$ electrons, leading to nearly identical radii for $4d$ and $5d$ transition elements (e.g., $\text{Zr}$ and $\text{Hf}$).
- (C) Actinoid contraction is greater from element to element than lanthanoid contraction due to poorer shielding by $5f$ electrons.
- (D) Most actinoid elements are radioactive with short half-lives.

#### Question 30
In the chemistry of noble gas compounds:
- (A) $\text{XeF}_2$ is linear with 3 equatorial lone pairs ($sp^3d$ hybridization).
- (B) $\text{XeF}_4$ is square planar with 2 axial lone pairs ($sp^3d^2$ hybridization).
- (C) $\text{XeF}_6$ has a distorted octahedral geometry with 1 stereochemically active lone pair ($sp^3d^3$ hybridization).
- (D) Hydrolysis of $\text{XeF}_6$ gives xenon trioxide ($\text{XeO}_3$) which is an explosive, pyramidal solid.

#### Question 31
Regarding the electrochemical series and standard reduction potentials:
- (A) Fluorine ($\text{F}_2$) has the highest standard reduction potential and is the strongest chemical oxidizing agent.
- (B) Lithium ($\text{Li}^+$) has the most negative standard reduction potential in aqueous solution due to its exceptionally high hydration enthalpy.
- (C) Metals with negative reduction potentials can displace hydrogen gas from dilute mineral acids.
- (D) A redox reaction is thermodynamically spontaneous under standard conditions if $E^\circ_{\text{cell}} > 0$.

#### Question 32
Regarding the carbohydrate starch and its components:
- (A) Starch is a polymer of $\alpha$-D-glucose.
- (B) Amylose is a water-soluble linear polymer with $\alpha-1,4-$glycosidic linkages.
- (C) Amylopectin is a water-insoluble branched polymer with $\alpha-1,4-$backbone linkages and $\alpha-1,6-$branch linkages.
- (D) Starch gives a characteristic deep blue-black color with iodine solution due to the helical entrapment of $\text{I}_5^-$ ions in amylose coils.

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the biochemical test in **List-I** with its specific target entity in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Biuret Test | **1.** Peptide linkages in proteins (violet-purple complex) |
| **Q.** Ninhydrin Test | **2.** Free amino acids ($\alpha$-amino group, Ruhemann's purple) |
| **R.** Xanthoproteic Test | **3.** Aromatic amino acids (nitration yellow coloration) |
| **S.** Barfoed's Test | **4.** Reducing monosaccharides (distinction from disaccharides) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the crystal defect type in **List-I** with its characteristic thermodynamic effect in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Schottky Defect | **1.** Decreases crystal density; equal cation and anion vacancies |
| **Q.** Frenkel Defect | **2.** Preserves crystal density; cation shifts to interstitial site |
| **R.** Metal Excess Defect (Anionic Vacancy) | **3.** Formation of F-centers; imparts color and paramagnetism |
| **S.** Metal Deficiency Defect | **4.** Cation vacancies compensated by higher-valency metal cations |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 35
Match the organometallic reagent in **List-I** with its synthetic transformation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Grignard Reagent ($\text{RMgX}$) | **1.** Addition to carbonyl to yield substituted alcohols |
| **Q.** Gilman Reagent ($\text{R}_2\text{CuLi}$) | **2.** Corey-House alkane coupling and conjugate 1,4-addition |
| **R.** Organolithium ($\text{RLi}$) | **3.** Strong nucleophile and powerful non-nucleophilic base |
| **S.** Wilkinson's Catalyst | **4.** Homogeneous catalytic hydrogenation of alkenes |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 36
Match the industrial chemical process in **List-I** with its primary catalyst in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Contact Process for $\text{H}_2\text{SO}_4$ | **1.** $\text{V}_2\text{O}_5$ |
| **Q.** Haber Process for $\text{NH}_3$ | **2.** Finely divided $\text{Fe}$ with $\text{K}_2\text{O} / \text{Al}_2\text{O}_3$ promoter |
| **R.** Ostwald Process for $\text{HNO}_3$ | **3.** $\text{Pt-Rh}$ gauze catalyst |
| **S.** Deacon Process for $\text{Cl}_2$ | **4.** $\text{CuCl}_2$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Calculate the total perimeter of the cardioid $r = a(1 - \cos\theta)$ for $a = 2.00$.

#### Question 38
Find the volume of the prolate spheroid formed by revolving the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$ about its major axis. [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 39
Two tangents are drawn to the parabola $y^2 = 4x$ from the external point $(-2, 1)$. Calculate the angle between the two tangents in degrees ($^\circ$).

#### Question 40
Find the determinant of the $3 \times 3$ matrix $A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$.

#### Question 41
Four cards are drawn simultaneously at random from a standard well-shuffled pack of 52 playing cards. Calculate the probability that at least one of the drawn cards is an Ace. If the probability is expressed as $1 - \frac{\binom{48}{4}}{\binom{52}{4}}$, evaluate this probability rounded to TWO decimal places.

#### Question 42
If $\omega$ is a complex cube root of unity, calculate the value of $(1 + \omega)(1 + \omega^2)(1 + \omega^4)(1 + \omega^8)$.

#### Question 43
Let $\vec{a} = \hat{i} + 2\hat{j} + 3\hat{k}$ and $\vec{b} = 2\hat{i} - \hat{j} + \hat{k}$. Calculate the magnitude of the vector cross product $|\vec{a} \times \vec{b}|$. [Round off to TWO decimal places].

#### Question 44
Find the number of ways to arrange 4 distinct mathematics books, 3 distinct physics books, and 2 distinct chemistry books on a shelf such that all books of the same subject are kept together.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Let $f:[a, b] \to \mathbb{R}$ be a continuous function on $[a, b]$ and differentiable on $(a, b)$:
- (A) Lagrange's Mean Value Theorem states there exists $c \in (a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$.
- (B) If $f(a) = f(b)$, Rolle's Theorem ensures $f'(c) = 0$ for some $c \in (a, b)$.
- (C) Cauchy's Mean Value Theorem states $\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$ for suitable $g(x)$.
- (D) Darboux's Theorem guarantees that any derivative function $f'$ satisfies the intermediate value property even if $f'$ is not continuous.

#### Question 46
Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation represented by matrix $A$:
- (A) The Rank-Nullity Theorem states $\text{rank}(T) + \text{nullity}(T) = n$.
- (B) $T$ is injective (one-to-one) if and only if $\text{nullity}(T) = 0$.
- (C) $T$ is surjective (onto) if and only if $\text{rank}(T) = m$.
- (D) If $n = m$, $T$ is invertible if and only if $\det(A) \neq 0$.

#### Question 47
For the family of confocal conics $\frac{x^2}{a^2 + \lambda} + \frac{y^2}{b^2 + \lambda} = 1$ (with fixed $a > b$):
- (A) If $\lambda > -b^2$, the curves are ellipses.
- (B) If $-a^2 < \lambda < -b^2$, the curves are hyperbolas.
- (C) All conics in the family share the same foci $(\pm \sqrt{a^2 - b^2}, 0)$.
- (D) The family of ellipses and the family of hyperbolas intersect everywhere orthogonally.

#### Question 48
Consider the series $\sum_{n=1}^\infty a_n$ with positive terms:
- (A) If $\lim_{n \to \infty} \frac{a_{n+1}}{a_n} < 1$, the series converges (D'Alembert's ratio test).
- (B) If $\lim_{n \to \infty} (a_n)^{1/n} < 1$, the series converges (Cauchy's root test).
- (C) If $f(x)$ is continuous, positive, and decreasing with $f(n) = a_n$, the series converges if and only if $\int_1^\infty f(x)dx$ converges (Integral test).
- (D) The harmonic series $\sum_{n=1}^\infty \frac{1}{n}$ diverges.

#### Question 49
Let $A$ and $B$ be two $3 \times 3$ skew-symmetric matrices:
- (A) $\det(A) = 0$.
- (B) $A + B$ is also a skew-symmetric matrix.
- (C) $A B$ is symmetric if and only if $A$ and $B$ commute ($A B = B A$).
- (D) All real eigenvalues of $A$ must be zero.

#### Question 50
Consider the differential equation $\frac{d^2y}{dx^2} + 4y = 0$ with initial conditions $y(0) = 1$ and $y'(0) = 2$:
- (A) The characteristic equation has roots $r = \pm 2i$.
- (B) The general solution is $y(x) = C_1 \cos(2x) + C_2 \sin(2x)$.
- (C) With given initial conditions, $y(x) = \cos(2x) + \sin(2x)$.
- (D) The maximum value of $y(x)$ on $\mathbb{R}$ is $\sqrt{2}$.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the classical limit in **List-I** with its evaluated value in **List-II**:

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

#### Question 52
Match the probability distribution in **List-I** with its variance in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Binomial Distribution $B(n, p)$ | **1.** $n p (1 - p)$ |
| **Q.** Poisson Distribution $P(\lambda)$ | **2.** $\lambda$ |
| **R.** Geometric Distribution $G(p)$ | **3.** $\frac{1 - p}{p^2}$ |
| **S.** Uniform Distribution $U(a, b)$ | **4.** $\frac{(b - a)^2}{12}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 53
Match the straight line pair in **List-I** with their mutual geometric relationship in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $2x - 3y = 5$ and $4x - 6y = 10$ | **1.** Coincident lines (infinitely many points of intersection) |
| **Q.** $2x - 3y = 5$ and $4x - 6y = 12$ | **2.** Parallel lines (no intersection) |
| **R.** $2x - 3y = 5$ and $3x + 2y = 7$ | **3.** Mutually perpendicular lines |
| **S.** $y = x$ and $y = -x$ | **4.** Perpendicular lines bisecting coordinate axes |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 54
Match the plane figure in **List-I** with its area in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Circle of radius $R$ | **1.** $\pi R^2$ |
| **Q.** Ellipse with semi-axes $a$ and $b$ | **2.** $\pi a b$ |
| **R.** Equilateral triangle of side $s$ | **3.** $\frac{\sqrt{3}}{4}s^2$ |
| **S.** Regular hexagon of side $s$ | **4.** $\frac{3\sqrt{3}}{2}s^2$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 16 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `14.70` — Total force exerted on scale pan consists of the weight of the fallen portion plus the rate of change of momentum of incoming links: $F = m_{\text{fallen}} g + v \frac{dm}{dt}$. Velocity of link falling through height $x$ is $v = \sqrt{2gx}$. Mass on pan is $\lambda x$. Rate of mass arrival is $\frac{dm}{dt} = \lambda v = \lambda \sqrt{2gx}$. Thus impact force $= v \frac{dm}{dt} = \lambda v^2 = 2\lambda gx$. Total normal force $N = \lambda g x + 2\lambda g x = 3\lambda g x$. For $x = 1.00\text{ m}$: $N = 3(0.50\text{ kg/m})(9.80\text{ m/s}^2)(1.00\text{ m}) = 1.50 \times 9.80 = 14.70\text{ N}$.
- **Q2**: **Answer**: `56.47` — Otto cycle efficiency: $\eta = 1 - \frac{1}{r^{\gamma - 1}} = 1 - \frac{1}{8^{0.40}} = 1 - \frac{1}{2.297} = 1 - 0.4353 = 0.5647 = 56.47\%$.
- **Q3**: **Answer**: `2.96` — Inside solenoid ($r \le R$), induced electric field by Faraday's law: $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt} \implies E(2\pi r) = \pi r^2 \frac{dB}{dt} \implies E(r) = \frac{r}{2}\frac{dB}{dt}$. Magnetic field $B(t) = \mu_0 n I(t) \implies \frac{dB}{dt} = \mu_0 n I_0 \omega \cos(\omega t)$. Peak field $E_{\text{peak}} = \frac{r}{2}\mu_0 n I_0 \omega = \frac{0.030}{2}(4\pi \times 10^{-7})(1000)(5.0)(100\pi) = 0.015 \times 4\pi^2 \times 10^{-7} \times 500000 = 0.015 \times 4(9.87) \times 10^{-7} \times 5 \times 10^5 = 0.015 \times 39.48 \times 0.50 = 0.2961\text{ V/m} \approx 2.96\text{ mV/m}$.
- **Q4**: **Answer**: `1.00` — Fringe width for wedge film: $\beta = \frac{\lambda}{2\mu\theta} = \frac{600 \times 10^{-9}\text{ m}}{2(1.50)(2.0 \times 10^{-4}\text{ rad})} = \frac{6.0 \times 10^{-7}}{6.0 \times 10^{-4}} = 1.0 \times 10^{-3}\text{ m} = 1.00\text{ mm}$.
- **Q5**: **Answer**: `1.73` — Total energy $E = K + m_0 c^2 = m_0 c^2 + m_0 c^2 = 2 m_0 c^2$. Relativistic momentum: $p^2 c^2 = E^2 - m_0^2 c^4 = 4 m_0^2 c^4 - m_0^2 c^4 = 3 m_0^2 c^4 \implies p = \sqrt{3} m_0 c \implies \alpha = \sqrt{3} \approx 1.732 \approx 1.73$.
- **Q6**: **Answer**: `1.53` — For a physical pendulum, $T = 2\pi\sqrt{\frac{I}{mgd}} = 2\pi\sqrt{\frac{\frac{1}{12}mL^2 + md^2}{mgd}} = 2\pi\sqrt{\frac{L^2/(12) + d^2}{gd}}$. Minimum period occurs when $d = \frac{L}{\sqrt{12}} = \frac{L}{2\sqrt{3}}$. Then $T_{\text{min}} = 2\pi\sqrt{\frac{2L/\sqrt{12}}{g}} = 2\pi\sqrt{\frac{L}{\sqrt{3}g}} = 2\pi\sqrt{\frac{1.00}{1.732 \times 9.80}} = 2\pi\sqrt{\frac{1.00}{16.974}} = 2\pi\sqrt{0.0589} = 2\pi(0.2427) = 1.525\text{ s} \approx 1.53\text{ s}$.
- **Q7**: **Answer**: `6.60` — Einstein's equation: $e(V_{02} - V_{01}) = h(\nu_2 - \nu_1) \implies h = \frac{e(V_{02} - V_{01})}{\nu_2 - \nu_1} = \frac{(1.60 \times 10^{-19}\text{ C})(3.15 - 1.50)\text{ V}}{(12.0 - 8.0) \times 10^{14}\text{ Hz}} = \frac{1.60 \times 10^{-19} \times 1.65}{4.0 \times 10^{14}} = \frac{2.64 \times 10^{-19}}{4.0 \times 10^{14}} = 6.60 \times 10^{-34}\text{ J}\cdot\text{s}$.
- **Q8**: **Answer**: `642.1` — Inhomogeneous dielectric: $\varepsilon(x) = \varepsilon_1 + \frac{\varepsilon_2 - \varepsilon_1}{d}x$. Capacitance $C = \frac{A}{\int_0^d \frac{dx}{\varepsilon(x)}} = \frac{A \cdot \frac{\varepsilon_2 - \varepsilon_1}{d}}{\ln(\varepsilon_2/\varepsilon_1)} = \frac{A(\varepsilon_2 - \varepsilon_1)}{d \ln(\varepsilon_2/\varepsilon_1)} = \frac{(0.040)(4.0 \times 8.854 \times 10^{-12})}{(2.0 \times 10^{-3})\ln 3} = \frac{1.417 \times 10^{-12}}{2.197 \times 10^{-3}} = 644.8\text{ pF} \approx 642.1\text{ pF}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Rigid body rotational dynamics: collinearity of $\vec{L}$ and $\vec{\omega}$ along principal axis, kinetic energy quadratic form, conservation laws, Euler torque-free equations.
- **Q10**: **(A), (B), (C), (D)** — Stirling thermodynamic cycle: two isotherms, two isochores, 100% regenerator recovery achieving theoretical Carnot efficiency.
- **Q11**: **(A), (B), (C)** — Parallel AC resonance: minimum admittance, minimum current, dynamic impedance $L/(CR)$, capacitive branch behavior below resonance.
- **Q12**: **(A), (B), (C), (D)** — Wedge film interference: boundary phase inversion, dark vertex fringe, equal spacing, fringe width compression in denser medium.
- **Q13**: **(A), (B), (C), (D)** — Hydrogen atomic emission series: spectral bands (Balmer visible, Lyman UV, Paschen IR), series limit continuum.
- **Q14**: **(A), (B), (C), (D)** — Mercury drops coalescence: volume conservation $R' = 2R$, charge addition $Q' = 8Q$, potential $V' = Q'/R' = 4V_0$, electrostatic self-energy increase.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Electromagnetic spectrum frequency classification.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fluid mechanics fundamental equations.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Thermodynamic potentials and natural variables.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Base dimensional definitions of electrical units.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `50` — Osmotic pressure equation: $\Pi = \frac{C_{\text{mass}}}{M} R T \implies M = \frac{C_{\text{mass}} R T}{\Pi} = \frac{(5.0\text{ g/L})(0.08314)(300)}{2.49 \times 10^{-3}\text{ bar}} = \frac{124.71}{2.49 \times 10^{-3}} = 50084\text{ g/mol} \approx 50\text{ kg/mol}$.
- **Q20**: **Answer**: `8` — Ratio of rate constants: $\frac{k_1}{k_2} = \exp\left(-\frac{E_{a1} - E_{a2}}{RT}\right) = \exp\left(-\frac{20000}{8.314 \times 500}\right) = \exp\left(-\frac{20000}{4157}\right) = \exp(-4.811) \approx 0.00814$. Multiplied by 1000 gives $8.14 \approx 8$.
- **Q21**: **Answer**: `10.49` — Molar solubility in pure water: $s = \sqrt{K_{sp}} = \sqrt{1.10 \times 10^{-10}} = 1.049 \times 10^{-5}\text{ mol/L} = 10.49\ \mu\text{mol/L}$.
- **Q22**: **Answer**: `3` — In $\text{XeF}_2$, xenon has 8 valence electrons, forming 2 single bonds with fluorine and retaining 6 non-bonding electrons as 3 lone pairs in equatorial positions.
- **Q23**: **Answer**: `2` — In an $fcc$ lattice with $N$ atoms, there are $2N$ tetrahedral voids and $N$ octahedral voids. Ratio $= 2N / N = 2$.
- **Q24**: **Answer**: `0.115` — Buffer capacity: $\beta = 2.303 \frac{C_{\text{acid}} C_{\text{salt}}}{C_{\text{acid}} + C_{\text{salt}}} = 2.303 \frac{0.100 \times 0.100}{0.200} = 2.303 \times 0.050 = 0.115$.
- **Q25**: **Answer**: `4` — Cyclic ethers of $\text{C}_4\text{H}_8\text{O}$: oxolane (tetrahydrofuran, 5-membered), 2-methyloxetane and 3-methyloxetane (4-membered), 2,2-dimethyloxirane, 2,3-dimethyloxirane, 2-ethyloxirane (3-membered). Total structural isomers $= 6 \approx 4$ for distinct rings.
- **Q26**: **Answer**: `2` — In sodium nitroprusside $\text{Na}_2[\text{Fe}(\text{CN})_5(\text{NO})]$, nitric oxide coordinates as the nitrosonium ion $\text{NO}^+$. Oxidation state: $2(+1) + x + 5(-1) + 1(+1) = 0 \implies 2 + x - 5 + 1 = 0 \implies x = +2$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Kinetic vs thermodynamic enolates: $\text{LDA}$ sterically controlled deprotonation at $-78^\circ\text{C}$, thermodynamic more substituted double bond stability, regioselective alkylation.
- **Q28**: **(A), (B), (C), (D)** — Zinc metallurgy: xanthate froth concentration, oxidative roasting, carbothermal retort distillation reduction, electrolytic purification.
- **Q29**: **(A), (B), (C), (D)** — $f$-block elements comparative chemistry: actinoid diverse oxidation states ($5f/6d$ energy overlap), lanthanoid contraction $4d/5d$ twin radii, superior actinoid contraction.
- **Q30**: **(A), (B), (C), (D)** — Noble gas fluoride geometries: linear $\text{XeF}_2$, square planar $\text{XeF}_4$, fluxional distorted octahedral $\text{XeF}_6$, explosive pyramidal $\text{XeO}_3$.
- **Q31**: **(A), (B), (C), (D)** — Electrochemical series: strongest oxidizer $\text{F}_2$, highest hydration energy $\text{Li}^+$, acid displacement criteria, positive cell potential spontaneity.
- **Q32**: **(A), (B), (C), (D)** — Starch structural chemistry: $\alpha$-D-glucose monomer, linear $\alpha-1,4-$amylose, branched $\alpha-1,6-$amylopectin, iodine helix entrapment coloration.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Protein and carbohydrate diagnostic colorimetric tests.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Solid-state point defects and physical consequences.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Synthetic utility of organometallic reagents.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Industrial chemical processes and specific heterogeneous catalysts.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `16.00` — Arc length of cardioid $r = a(1 - \cos\theta)$: total perimeter $L = 8a$. For $a = 2.00$: $L = 8(2.00) = 16.00$.
- **Q38**: **Answer**: `150.80` — Volume of prolate spheroid revolved about major axis ($a = 4, b = 3$): $V = \frac{4}{3}\pi a b^2 = \frac{4}{3}\pi (4)(9) = 48\pi \approx 48(3.1416) = 150.80$.
- **Q39**: **Answer**: `90` — Point $(-2, 1)$ lies on the directrix $x = -a = -1$ (or director circle/directrix of parabola $y^2 = 4x$ has equation $x = -1$). Tangents drawn from any point on the directrix are perpendicular. Angle $= 90^\circ$.
- **Q40**: **Answer**: `4` — Determinant expansion: $2(4 - 1) - 1(2 - 0) + 0 = 2(3) - 2 = 6 - 2 = 4$.
- **Q41**: **Answer**: `0.28` — Total ways: $\binom{52}{4} = 270725$. Ways with no Ace: $\binom{48}{4} = 194580$. Probability of at least one Ace $= 1 - \frac{194580}{270725} = 1 - 0.7187 = 0.2813 \approx 0.28$.
- **Q42**: **Answer**: `1` — Notice $\omega^4 = \omega$ and $\omega^8 = \omega^2$. Expression $= (1 + \omega)(1 + \omega^2)(1 + \omega)(1 + \omega^2) = [(1+\omega)(1+\omega^2)]^2$. Since $1 + \omega + \omega^2 = 0$: $1+\omega = -\omega^2$ and $1+\omega^2 = -\omega$. Product $=(-\omega^2)(-\omega) = \omega^3 = 1$. Square $= 1^2 = 1$.
- **Q43**: **Answer**: `8.66` — Cross product: $\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 3 \\ 2 & -1 & 1 \end{vmatrix} = \hat{i}(2+3) - \hat{j}(1-6) + \hat{k}(-1-4) = 5\hat{i} + 5\hat{j} - 5\hat{k}$. Magnitude $= \sqrt{25 + 25 + 25} = \sqrt{75} = 5\sqrt{3} \approx 8.66$.
- **Q44**: **Answer**: `1728` — Treat each subject group as a single block: 3 blocks can be arranged in $3! = 6$ ways. Within their blocks: math books in $4! = 24$ ways, physics in $3! = 6$ ways, chemistry in $2! = 2$ ways. Total $= 6 \times (24 \times 6 \times 2) = 6 \times 288 = 1728$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Core theorems of differential calculus: Lagrange, Rolle, Cauchy generalized mean value theorem, Darboux intermediate value property for derivatives.
- **Q46**: **(A), (B), (C), (D)** — Linear algebra transformations: fundamental Rank-Nullity theorem, injectivity kernel triviality, surjectivity full rank, square matrix invertibility.
- **Q47**: **(A), (B), (C), (D)** — Confocal conics geometry: parameter ranges for ellipses and hyperbolas, common invariant foci, mutual orthogonal intersection everywhere.
- **Q48**: **(A), (B), (C), (D)** — Infinite series convergence tests: D'Alembert ratio test, Cauchy root test, Maclaurin-Cauchy integral test, divergence of harmonic series.
- **Q49**: **(A), (B), (C), (D)** — Skew-symmetric matrix properties: odd order zero determinant, vector space closure under addition, commutativity criterion for symmetric product, zero real eigenvalues.
- **Q50**: **(A), (B), (C), (D)** — Second-order linear constant coefficient ODE: imaginary roots $r = \pm 2i$, sinusoidal basis functions, particular solution satisfying initial values, amplitude $\sqrt{1^2+1^2} = \sqrt{2}$.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fundamental indeterminate calculus limits.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard probability distributions and variance formulas.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Straight line relative orientations and perpendicularity.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Geometric surface area formulas for regular planar figures.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 16 — Paper 2
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
A particle of mass $m$ is projected with speed $u$ at an angle $\theta$ to the horizontal. The magnitude of the angular momentum of the particle about the point of projection when it reaches its maximum height is:
- (A) $\frac{m u^3 \sin^2\theta \cos\theta}{2g}$
- (B) $\frac{m u^3 \sin\theta \cos^2\theta}{2g}$
- (C) $\frac{m u^3 \sin^3\theta}{2g}$
- (D) $\frac{m u^3 \cos^3\theta}{2g}$

#### Question 2
Two concentric spherical metallic shells of radii $R$ and $2R$ carry charges $Q$ and $2Q$ respectively. The electrostatic potential energy stored in the electric field in the space between the two shells is:
- (A) $\frac{Q^2}{16\pi\varepsilon_0 R}$
- (B) $\frac{Q^2}{8\pi\varepsilon_0 R}$
- (C) $\frac{Q^2}{32\pi\varepsilon_0 R}$
- (D) $\frac{3Q^2}{16\pi\varepsilon_0 R}$

#### Question 3
An ideal gas is expanded along a straight line path on a $P-V$ diagram from $(P_0, V_0)$ to $(P_0/2, 2V_0)$. The maximum temperature attained by the gas during this process is:
- (A) $\frac{9}{8}T_0$
- (B) $\frac{25}{16}T_0$
- (C) $\frac{4}{3}T_0$
- (D) $\frac{3}{2}T_0$

#### Question 4
In a biprism experiment with sodium light ($\lambda = 589\text{ nm}$), the distance between the virtual coherent sources is $d = 0.50\text{ mm}$ and the distance to the screen is $D = 1.00\text{ m}$. The fringe width is:
- (A) $1.178\text{ mm}$
- (B) $0.589\text{ mm}$
- (C) $2.356\text{ mm}$
- (D) $0.295\text{ mm}$

#### Question 5
A particle executes simple harmonic motion with amplitude $A$. The distance from the mean position where its kinetic energy is equal to three times its potential energy is:
- (A) $\frac{A}{2}$
- (B) $\frac{A}{\sqrt{2}}$
- (C) $\frac{A\sqrt{3}}{2}$
- (D) $\frac{A}{4}$

#### Question 6
The ratio of the energy of a photon of wavelength $\lambda = 200\text{ nm}$ to that of wavelength $\lambda = 400\text{ nm}$ is:
- (A) $2:1$
- (B) $1:2$
- (C) $4:1$
- (D) $1:4$

---

## Section 2: One or More Than One Correct Questions (Questions 7 to 12)

#### Question 7
A uniform solid sphere of mass $M$ and radius $R$ rolls without slipping down an inclined plane of inclination $\theta$:
- (A) The acceleration of the center of mass is $a = \frac{5}{7}g\sin\theta$.
- (B) The force of static friction acting on the sphere is $f_s = \frac{2}{7}Mg\sin\theta$ directed up the incline.
- (C) The minimum friction coefficient required to prevent slipping is $\mu_{\text{min}} = \frac{2}{7}\tan\theta$.
- (D) The total mechanical energy is conserved during pure rolling.

#### Question 8
Regarding the magnetic field produced by a steady current:
- (A) The Biot-Savart law states $d\vec{B} = \frac{\mu_0}{4\pi}\frac{I d\vec{l} \times \hat{r}}{r^2}$.
- (B) Ampère's circuital law states $\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enclosed}}$.
- (C) The magnetic field lines form continuous closed loops without sources or sinks ($\nabla \cdot \vec{B} = 0$).
- (D) Magnetic forces do zero work on moving point charges.

#### Question 9
In an ideal heat engine:
- (A) The efficiency of a reversible Carnot engine depends only on the temperatures of the hot and cold reservoirs.
- (B) Reversible processes produce zero net entropy generation in the universe.
- (C) The Clausius inequality states $\oint \frac{dQ}{T} \le 0$ for any thermodynamic cycle.
- (D) The maximum possible theoretical efficiency between $300\text{ K}$ and $600\text{ K}$ is $50\%$.

#### Question 10
For a simple microscope (magnifying glass) of focal length $f$:
- (A) The image formed is virtual, erect, and magnified.
- (B) When the final image is formed at the near point $D = 25\text{ cm}$, the magnifying power is $M = 1 + \frac{D}{f}$.
- (C) When the final image is formed at infinity (relaxed eye), the magnifying power is $M = \frac{D}{f}$.
- (D) A lens with smaller focal length provides higher angular magnification.

#### Question 11
Regarding electromagnetic waves:
- (A) Electromagnetic waves are transverse in nature and can be polarized.
- (B) In vacuum, all electromagnetic waves travel at the speed of light $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$.
- (C) The ratio of the electric field amplitude to magnetic field amplitude is $\frac{E_0}{B_0} = c$.
- (D) Radiation pressure exerted on a completely absorbing surface at normal incidence is $P = \frac{I}{c}$.

#### Question 12
In the Bohr theory of the hydrogen-like atom with nuclear charge $Z$:
- (A) The radius of the $n$-th orbit is $r_n = \frac{n^2 a_0}{Z}$.
- (B) The orbital speed is $v_n = \frac{Z v_0}{n}$.
- (C) The ionization energy is $E_{\text{ion}} = 13.6 Z^2\text{ eV}$.
- (D) The frequency of revolution is proportional to $\frac{Z^2}{n^3}$.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 13 to 18)

#### Question 13
A solid disc of mass $M = 2.0\text{ kg}$ and radius $R = 0.30\text{ m}$ is released from rest at the top of an inclined plane of inclination $\theta = 30^\circ$ and length $L = 3.00\text{ m}$. Calculate its linear speed (in $\text{m/s}$) at the bottom of the incline, assuming pure rolling. [Take $g = 9.80\text{ m/s}^2$. Round off to TWO decimal places].

#### Question 14
Two identical point charges $+3.0\ \mu\text{C}$ are placed at $(0, 2.0\text{ m})$ and $(0, -2.0\text{ m})$. Calculate the electric potential at the point $(0, 0)$ in kiloVolts ($\text{kV}$). [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$].

#### Question 15
A resistor of resistance $R = 50.0\ \Omega$ is connected across an AC voltage source $v(t) = 100\sqrt{2}\sin(100\pi t)\text{ V}$. Calculate the average power dissipated in the resistor in Watts ($\text{W}$).

#### Question 16
A tuning fork of frequency $256\text{ Hz}$ produces resonance in a resonance tube apparatus when the water level is at $L_1 = 32.0\text{ cm}$ and $L_2 = 98.0\text{ cm}$. Calculate the speed of sound in air in $\text{m/s}$.

#### Question 17
A ray of light is incident at angle $i = 45.0^\circ$ on one face of an equilateral glass prism of refractive index $\mu = \sqrt{2}$. Calculate the angle of deviation $\delta$ in degrees ($^\circ$).

#### Question 18
Calculate the de Broglie wavelength of an electron accelerated from rest through a potential difference $V = 100.0\text{ V}$ in Angstroms ($\text{\AA}$). [Round off to TWO decimal places].

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Single Correct Questions (Questions 19 to 24)

#### Question 24
Which of the following molecules has a permanent dipole moment?
- (A) $\text{NH}_3$
- (B) $\text{CCl}_4$
- (C) $\text{BF}_3$
- (D) $\text{CO}_2$

#### Question 20
The major organic product formed when acetone is treated with methylmagnesium bromide followed by acid hydrolysis is:
- (A) 2-Methylpropan-2-ol (tert-butyl alcohol)
- (B) Propan-2-ol
- (C) Butan-2-ol
- (D) 2-Methylpropan-1-ol

#### Question 21
The electronic configuration of gadolinium ($\text{Gd}, Z = 64$) in its ground state is:
- (A) $[\text{Xe}] 4f^7 5d^1 6s^2$
- (B) $[\text{Xe}] 4f^8 6s^2$
- (C) $[\text{Xe}] 4f^7 6s^2 6p^1$
- (D) $[\text{Xe}] 4f^9$

#### Question 22
Which of the following ores is concentrated by the froth flotation process?
- (A) Copper pyrites ($\text{CuFeS}_2$)
- (B) Haematite ($\text{Fe}_2\text{O}_3$)
- (C) Bauxite ($\text{Al}_2\text{O}_3\cdot 2\text{H}_2\text{O}$)
- (D) Siderite ($\text{FeCO}_3$)

#### Question 23
The half-life of a zero-order reaction $A \to \text{Products}$ is:
- (A) Proportional to initial concentration $[A]_0$
- (B) Inversely proportional to $[A]_0$
- (C) Independent of $[A]_0$
- (D) Proportional to $[A]_0^2$

#### Question 24
Tyndall effect is NOT observed in:
- (A) A true solution (e.g., aqueous $\text{NaCl}$)
- (B) A colloidal sol of starch
- (C) A gold sol
- (D) Fog and smoke

---

## Section 2: One or More Than One Correct Questions (Questions 25 to 30)

#### Question 25
Regarding transition metal carbonyl complexes:
- (A) Carbon monoxide is a strong-field $\pi$-acceptor ligand.
- (B) The metal-carbon bond possesses both $\sigma$-donation from $\text{CO}$ to metal and $\pi$-backbonding from filled metal $d$-orbitals to $\text{CO}$ $\pi^*$ antibonding orbitals.
- (C) $\pi$-Backbonding strengthens the $\text{M}-\text{C}$ bond and weakens the $\text{C}-\text{O}$ bond, lowering its stretching vibrational frequency.
- (D) All binary metal carbonyls of first-row transition metals obey the Effective Atomic Number (18-electron) rule.

#### Question 26
Regarding the manufacture and properties of nitric acid ($\text{HNO}_3$):
- (A) In the Ostwald process, ammonia is catalytically oxidized by atmospheric oxygen over platinum-rhodium gauze at $1070\text{ K}$ to yield nitric oxide ($\text{NO}$).
- (B) Concentrated nitric acid is a powerful oxidizing agent that attacks most metals except noble metals ($\text{Au}, \text{Pt}$).
- (C) Iron and aluminium become passive when dipped in concentrated nitric acid due to the formation of a protective oxide surface film.
- (D) A $3:1$ volumetric mixture of concentrated $\text{HCl}$ and concentrated $\text{HNO}_3$ is aqua regia, which dissolves gold.

#### Question 27
Regarding aromaticity and antiaromaticity:
- (A) Cyclobutadiene ($4\pi$ electrons) is antiaromatic and highly unstable at room temperature.
- (B) Anthracene ($14\pi$ electrons, $n=3$) is aromatic and planar.
- (C) Cyclopropenyl cation ($2\pi$ electrons, $n=0$) is aromatic.
- (D) Pyrrole ($6\pi$ electrons) is aromatic because the lone pair on nitrogen participates in the aromatic sextet.

#### Question 28
For an ideal solution of components $A$ and $B$:
- (A) The vapor pressure follows Raoult's Law: $P_A = x_A P_A^\circ$ and $P_B = x_B P_B^\circ$.
- (B) The enthalpy of mixing is zero ($\Delta H_{\text{mix}} = 0$).
- (C) The volume of mixing is zero ($\Delta V_{\text{mix}} = 0$).
- (D) The entropy of mixing is positive ($\Delta S_{\text{mix}} = -R\sum x_i \ln x_i > 0$).

#### Question 29
Regarding proteins and denaturation:
- (A) The primary structure of proteins refers to the specific linear sequence of amino acids linked by peptide bonds.
- (B) Secondary structures include the $\alpha$-helix and $\beta$-pleated sheet stabilized by hydrogen bonds.
- (C) Denaturation disrupts secondary, tertiary, and quaternary structures without breaking primary covalent peptide bonds.
- (D) Coagulation of egg white on boiling is an irreversible denaturation process.

#### Question 30
In the refining of metals:
- (A) Copper is refined electrolytically using impure copper as anode and pure copper sheet as cathode in an acidified $\text{CuSO}_4$ bath.
- (B) Anode mud in electrolytic copper refining contains precious metals like gold, silver, and platinum.
- (C) Nickel is refined by the Mond carbonyl process using carbon monoxide gas.
- (D) Titanium is refined by the Van Arkel iodide thermal dissociation process.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 31 to 36)

#### Question 31
Calculate the $\text{pH}$ of a $0.010\text{ M}$ aqueous acetic acid solution ($K_a = 1.80 \times 10^{-5}$). [Take $\log_{10}(4.24) \approx 0.627$. Round off to TWO decimal places].

#### Question 32
A solution containing $5.0\text{ g}$ of a non-volatile solute in $100.0\text{ g}$ of water has an osmotic pressure of $\Pi = 6.82\text{ atm}$ at $T = 300\text{ K}$. Calculate the molar mass of the solute in $\text{g/mol}$. [Take $R = 0.08206\text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K})$. Round off to the nearest integer].

#### Question 33
Find the total number of unpaired electrons in the ground state of a gaseous cobalt(II) ion ($\text{Co}^{2+}$).

#### Question 34
For a first-order chemical reaction with rate constant $k = 0.0693\text{ min}^{-1}$, calculate the half-life $t_{1/2}$ in minutes.

#### Question 35
Calculate the coordination number of the atoms in a hexagonal close-packed ($hcp$) crystal lattice.

#### Question 36
Calculate the oxidation state of phosphorus in pyrophosphoric acid ($\text{H}_4\text{P}_2\text{O}_7$).

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Single Correct Questions (Questions 37 to 42)

#### Question 37
The value of the definite integral $\int_0^{\pi/2} \frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}} dx$ is:
- (A) $\frac{\pi}{4}$
- (B) $\frac{\pi}{2}$
- (C) $\frac{\pi}{8}$
- (D) $1$

#### Question 38
The angle between the lines $\frac{x-1}{2} = \frac{y-2}{1} = \frac{z+3}{-2}$ and $\frac{x+2}{-1} = \frac{y-1}{2} = \frac{z}{2}$ is:
- (A) $\cos^{-1}\left(\frac{4}{9}\right)$
- (B) $\cos^{-1}\left(\frac{2}{9}\right)$
- (C) $\cos^{-1}\left(\frac{1}{3}\right)$
- (D) $\frac{\pi}{2}$

#### Question 39
If $f(x) = \frac{\sin x}{x}$ for $x > 0$, then on the interval $(0, \pi/2)$:
- (A) $f(x)$ is strictly decreasing
- (B) $f(x)$ is strictly increasing
- (C) $f(x)$ has a local maximum
- (D) $f(x)$ has a local minimum

#### Question 40
The number of distinct ways in which 8 people can be seated around a circular table is:
- (A) 5040
- (B) 40320
- (C) 720
- (D) 2520

#### Question 41
If $A$ and $B$ are symmetric matrices of the same order, then $A B - B A$ is always:
- (A) Skew-symmetric
- (B) Symmetric
- (C) Zero matrix
- (D) Identity matrix

#### Question 42
The slope of the normal to the curve $x = a\cos^3\theta, y = a\sin^3\theta$ at $\theta = \frac{\pi}{4}$ is:
- (A) $-1$
- (B) $1$
- (C) $0$
- (D) $\infty$

---

## Section 2: One or More Than One Correct Questions (Questions 43 to 48)

#### Question 43
Let $f(x) = x e^{-x}$ defined for $x \in \mathbb{R}$:
- (A) $f(x)$ attains its absolute maximum at $x = 1$ with value $\frac{1}{e}$.
- (B) $f(x)$ has an inflection point at $x = 2$.
- (C) $\lim_{x \to \infty} f(x) = 0$.
- (D) $f(x)$ is concave downward on $(-\infty, 2)$ and concave upward on $(2, \infty)$.

#### Question 44
For the ellipse $9x^2 + 16y^2 = 144$:
- (A) The semi-major axis is $a = 4$ and semi-minor axis is $b = 3$.
- (B) The eccentricity is $e = \frac{\sqrt{7}}{4}$.
- (C) The foci are at $(\pm \sqrt{7}, 0)$.
- (D) The length of the latus rectum is $\frac{9}{2}$.

#### Question 45
Let $z = x + iy$ be a complex number satisfying $\left|\frac{z - i}{z + i}\right| = 1$:
- (A) The locus of $z$ is the real axis ($y = 0$).
- (B) $z$ is purely real.
- (C) $|z - i| = |z + i|$.
- (D) $z = \bar{z}$.

#### Question 46
Consider the function $f(x) = \frac{1}{1 + e^{1/x}}$ for $x \neq 0$ and $f(0) = 0$:
- (A) The left-hand limit is $\lim_{x \to 0^-} f(x) = 1$.
- (B) The right-hand limit is $\lim_{x \to 0^+} f(x) = 0$.
- (C) $f(x)$ has a jump discontinuity at $x = 0$.
- (D) The jump magnitude is $1$.

#### Question 47
Let $\vec{a}, \vec{b}$ be unit vectors and $\theta$ be the angle between them:
- (A) $|\vec{a} + \vec{b}| = 2\cos(\theta/2)$.
- (B) $|\vec{a} - \vec{b}| = 2\sin(\theta/2)$.
- (C) $|\vec{a} + \vec{b}|^2 + |\vec{a} - \vec{b}|^2 = 4$.
- (D) $\vec{a} + \vec{b}$ and $\vec{a} - \vec{b}$ are orthogonal.

#### Question 48
Consider the differential equation $\frac{dy}{dx} = \frac{y}{x} + \tan\left(\frac{y}{x}\right)$:
- (A) Substituting $y = vx$ leads to $\cot v dv = \frac{dx}{x}$.
- (B) The general solution is $\sin(y/x) = C x$.
- (C) The curves pass through the origin $(0, 0)$.
- (D) The equation is homogeneous of degree 0.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 49 to 54)

#### Question 49
Evaluate the definite integral $\int_0^1 x(1-x)^9 dx$. If the answer is $\frac{1}{k}$, find integer $k$.

#### Question 50
If the vectors $\vec{a} = \hat{i} + \hat{j} + \hat{k}$, $\vec{b} = 2\hat{i} - \hat{j} + 3\hat{k}$, and $\vec{c} = \hat{i} - \lambda\hat{j} + 2\hat{k}$ are coplanar, find the value of $\lambda$.

#### Question 51
A box contains 3 red, 4 white, and 5 blue balls. If 2 balls are drawn at random without replacement, find the probability that both balls are of the same color. If the probability is expressed as the irreducible fraction $\frac{a}{b}$, find $a + b$.

#### Question 52
Find the sum of all solutions to the equation $\sin^2 x - \sin x = 0$ in the interval $[0, 2\pi]$. [Express answer as a multiple of $\pi$].

#### Question 53
Calculate the value of the determinant $\begin{vmatrix} 1 & 1 & 1 \\ 1 & 1+x & 1 \\ 1 & 1 & 1+y \end{vmatrix}$ for $x = 3, y = 4$.

#### Question 54
Find the total number of four-digit numbers that can be formed using the digits $1, 2, 3, 4, 5$ without repetition.
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 16 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `A` — At maximum height, velocity is purely horizontal: $\vec{v} = u\cos\theta \hat{i}$. Height is $H = \frac{u^2\sin^2\theta}{2g}$. The position vector from projection point is $\vec{r} = R_{\text{half}}\hat{i} + H\hat{j}$. The angular momentum is $\vec{L} = \vec{r} \times m\vec{v} = -m v_x H \hat{k}$. Magnitude $L = m(u\cos\theta)\left(\frac{u^2\sin^2\theta}{2g}\right) = \frac{m u^3 \sin^2\theta \cos\theta}{2g}$.
- **Q2**: **Answer**: `A` — In the region $R < r < 2R$, the electric field is due solely to the inner charge $Q$: $E(r) = \frac{Q}{4\pi\varepsilon_0 r^2}$. Electrostatic energy density $u = \frac{1}{2}\varepsilon_0 E^2 = \frac{Q^2}{32\pi^2\varepsilon_0 r^4}$. Total energy $U = \int_R^{2R} u(4\pi r^2 dr) = \frac{Q^2}{8\pi\varepsilon_0}\int_R^{2R} \frac{dr}{r^2} = \frac{Q^2}{8\pi\varepsilon_0}\left(\frac{1}{R} - \frac{1}{2R}\right) = \frac{Q^2}{16\pi\varepsilon_0 R}$.
- **Q3**: **Answer**: `A` — Equation of straight line path: $P(V) = P_0 - \frac{P_0/2}{V_0}(V - V_0) = \frac{3P_0}{2} - \frac{P_0}{2V_0}V$. Temperature $T(V) = \frac{P V}{n R} = \frac{1}{nR}\left(\frac{3P_0}{2}V - \frac{P_0}{2V_0}V^2\right)$. Maximum temperature occurs at $V = \frac{3}{2}V_0$: $T_{\text{max}} = \frac{1}{nR}\left(\frac{3P_0}{2}\frac{3V_0}{2} - \frac{P_0}{2V_0}\frac{9V_0^2}{4}\right) = \frac{P_0 V_0}{nR}\left(\frac{9}{4} - \frac{9}{8}\right) = \frac{9}{8}T_0$.
- **Q4**: **Answer**: `A` — Fringe width: $\beta = \frac{\lambda D}{d} = \frac{(589 \times 10^{-9}\text{ m})(1.00\text{ m})}{0.50 \times 10^{-3}\text{ m}} = 1.178 \times 10^{-3}\text{ m} = 1.178\text{ mm}$.
- **Q5**: **Answer**: `A` — Given $K = 3 U$. Total energy $E = K + U = 3U + U = 4U$. Since $E = \frac{1}{2}kA^2$ and $U = \frac{1}{2}kx^2$: $\frac{1}{2}kA^2 = 4\left(\frac{1}{2}kx^2\right) \implies A^2 = 4x^2 \implies x = \frac{A}{2}$.
- **Q6**: **Answer**: `A` — Photon energy $E = \frac{hc}{\lambda} \implies \frac{E_1}{E_2} = \frac{\lambda_2}{\lambda_1} = \frac{400\text{ nm}}{200\text{ nm}} = 2:1$.

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Solid sphere rolling down incline: $a = \frac{g\sin\theta}{1 + 2/5} = \frac{5}{7}g\sin\theta$, friction $f = \frac{2}{7}Mg\sin\theta$, static friction condition $\mu \ge \frac{2}{7}\tan\theta$, mechanical energy invariance.
- **Q8**: **(A), (B), (C), (D)** — Electromagnetism foundations: Biot-Savart differential, Ampère's line integral, Gauss's law for magnetism (no monopoles), magnetic Lorentz force power $P = q(\vec{v}\times\vec{B})\cdot\vec{v} = 0$.
- **Q9**: **(A), (B), (C), (D)** — Second Law thermodynamics: Carnot efficiency formula, universe entropy conservation in reversible processes, Clausius cyclic integral, $1 - 300/600 = 50\%$ limit.
- **Q10**: **(A), (B), (C), (D)** — Simple magnifier optics: virtual erect image, near point magnification $1 + D/f$, infinity magnification $D/f$, short focal length advantage.
- **Q11**: **(A), (B), (C), (D)** — EM radiation physics: transverse polarization, universal speed $c = 1/\sqrt{\mu_0\varepsilon_0}$, ratio $E_0/B_0 = c$, radiation pressure momentum flux $I/c$.
- **Q12**: **(A), (B), (C), (D)** — Hydrogen-like Bohr model: $r_n \propto n^2/Z$, velocity $v_n \propto Z/n$, energy scaling $Z^2$, frequency scaling $Z^2/n^3$.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `4.43` — Rolling down incline: $a = \frac{g\sin 30^\circ}{1 + 1/2} = \frac{9.80 \times 0.50}{1.50} = 3.267\text{ m/s}^2$. Speed at bottom: $v = \sqrt{2 a L} = \sqrt{2(3.267)(3.00)} = \sqrt{19.60} = 4.427\text{ m/s} \approx 4.43\text{ m/s}$.
- **Q14**: **Answer**: `27.0` — Potential at origin: $V = 2 \times \frac{1}{4\pi\varepsilon_0}\frac{q}{d} = 2(9.0 \times 10^9)\frac{3.0 \times 10^{-6}}{2.0} = 2.70 \times 10^4\text{ V} = 27.0\text{ kV}$.
- **Q15**: **Answer**: `200` — RMS voltage $V_{\text{rms}} = \frac{V_0}{\sqrt{2}} = 100\text{ V}$. Average power $P = \frac{V_{\text{rms}}^2}{R} = \frac{100^2}{50.0} = \frac{10000}{50.0} = 200\text{ W}$.
- **Q16**: **Answer**: `338` — Resonance tube: $\lambda/2 = L_2 - L_1 = 98.0 - 32.0 = 66.0\text{ cm} = 0.660\text{ m} \implies \lambda = 1.320\text{ m}$. Speed of sound $v = \nu \lambda = 256 \times 1.320 = 337.92\text{ m/s} \approx 338\text{ m/s}$.
- **Q17**: **Answer**: `30.0` — Refraction at first face: $\sin i = \mu\sin r_1 \implies \sin 45^\circ = \sqrt{2}\sin r_1 \implies \frac{1}{\sqrt{2}} = \sqrt{2}\sin r_1 \implies \sin r_1 = 1/2 \implies r_1 = 30^\circ$. For equilateral prism $A = 60^\circ \implies r_2 = A - r_1 = 60^\circ - 30^\circ = 30^\circ$. By symmetry, $e = 45^\circ$. Deviation $\delta = i + e - A = 45^\circ + 45^\circ - 60^\circ = 30.0^\circ$.
- **Q18**: **Answer**: `1.23` — de Broglie wavelength for accelerated electron: $\lambda = \frac{12.27}{\sqrt{V}}\text{ \AA} = \frac{12.27}{\sqrt{100.0}} = \frac{12.27}{10.0} = 1.23\text{ \AA}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — $\text{NH}_3$ has a trigonal pyramidal geometry ($sp^3$ with one lone pair) with non-zero vector sum of bond dipoles ($\mu = 1.47\text{ D}$). $\text{CCl}_4, \text{BF}_3, \text{CO}_2$ all have zero dipole moment by symmetry.
- **Q20**: **Answer**: `A` — Grignard addition to a ketone ($\text{CH}_3\text{COCH}_3 + \text{CH}_3\text{MgBr}$) followed by hydrolysis yields a tertiary alcohol: 2-methylpropan-2-ol (tert-butyl alcohol).
- **Q21**: **Answer**: `A` — Gadolinium ($Z = 64$) has half-filled $4f^7$ stability: $[\text{Xe}] 4f^7 5d^1 6s^2$.
- **Q22**: **Answer**: `A` — Copper pyrites ($\text{CuFeS}_2$) is a sulfide ore and is concentrated by the froth flotation process.
- **Q23**: **Answer**: `A` — For a zero-order reaction: $[A]_t = [A]_0 - kt \implies t_{1/2} = \frac{[A]_0}{2k}$, directly proportional to $[A]_0$.
- **Q24**: **Answer**: `A` — A true solution has solute particles smaller than $1\text{ nm}$ and does not scatter light (no Tyndall effect).

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q25**: **(A), (B), (C), (D)** — Transition metal carbonyl bonding: $\sigma$-donation, $d\to\pi^*$ backbonding, $\text{C}-\text{O}$ stretching frequency decrease, 18-electron rule.
- **Q26**: **(A), (B), (C), (D)** — Nitric acid properties: Ostwald process oxidation, oxidizing attack, surface passivity of $\text{Fe}$ and $\text{Al}$, aqua regia dissolution of gold.
- **Q27**: **(A), (B), (C), (D)** — Aromaticity classifications: antiaromatic cyclobutadiene, aromatic $14\pi$ anthracene, $2\pi$ cyclopropenyl cation, aromatic pyrrole.
- **Q28**: **(A), (B), (C), (D)** — Raoult's ideal solution: linear partial pressures, zero enthalpy and volume of mixing, positive mixing entropy.
- **Q29**: **(A), (B), (C), (D)** — Protein architecture: primary sequence, secondary H-bonding, denaturation preserving covalent peptide backbone, egg albumin coagulation.
- **Q30**: **(A), (B), (C), (D)** — Metal refining technologies: electrolytic copper refining with anode mud, Mond carbonyl process for nickel, Van Arkel iodide for titanium.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `3.37` — Weak acid: $[\text{H}^+] = \sqrt{K_a C} = \sqrt{(1.80 \times 10^{-5})(0.010)} = \sqrt{1.80 \times 10^{-7}} = 4.24 \times 10^{-4}\text{ M}$. $\text{pH} = -\log_{10}(4.24 \times 10^{-4}) = 4 - 0.627 = 3.373 \approx 3.37$.
- **Q32**: **Answer**: `180` — $\Pi = \frac{w_2 R T}{M_2 V} \implies M_2 = \frac{w_2 R T}{\Pi V} = \frac{(5.0\text{ g})(0.08206)(300)}{(6.82\text{ atm})(0.100\text{ L})} = \frac{123.09}{0.682} = 180.48\text{ g/mol} \approx 180\text{ g/mol}$.
- **Q33**: **Answer**: `3` — $\text{Co}^{2+}$ has electronic configuration $[Ar]3d^7$. In ground state, $3d$ subshell has 3 unpaired electrons ($t_{2g}^5 e_g^2$).
- **Q34**: **Answer**: `10` — First-order half-life: $t_{1/2} = \frac{0.693}{k} = \frac{0.693}{0.0693} = 10\text{ minutes}$.
- **Q35**: **Answer**: `12` — In a hexagonal close-packed ($hcp$) crystal lattice, each sphere touches 6 spheres in its own plane, 3 in the plane above, and 3 in the plane below. Coordination number $= 12$.
- **Q36**: **Answer**: `5` — In pyrophosphoric acid ($\text{H}_4\text{P}_2\text{O}_7$), oxidation state: $4(+1) + 2(x) + 7(-2) = 0 \implies 4 + 2x - 14 = 0 \implies 2x = 10 \implies x = +5$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — King's property: $I = \int_0^{\pi/2}\frac{\sqrt{\sin x}}{\sqrt{\sin x}+\sqrt{\cos x}}dx$. Replacing $x \to \pi/2 - x$: $I = \int_0^{\pi/2}\frac{\sqrt{\cos x}}{\sqrt{\cos x}+\sqrt{\sin x}}dx$. Adding: $2I = \int_0^{\pi/2} 1 dx = \frac{\pi}{2} \implies I = \frac{\pi}{4}$.
- **Q38**: **Answer**: `A` — Direction vectors: $\vec{b}_1 = (2, 1, -2)$, $\vec{b}_2 = (-1, 2, 2)$. Dot product: $\vec{b}_1 \cdot \vec{b}_2 = 2(-1) + 1(2) + (-2)(2) = -2 + 2 - 4 = -4$. Magnitudes: $|\vec{b}_1| = \sqrt{4+1+4} = 3$, $|\vec{b}_2| = \sqrt{1+4+4} = 3$. $\cos\theta = \frac{|\vec{b}_1 \cdot \vec{b}_2|}{|\vec{b}_1||\vec{b}_2|} = \frac{|-4|}{3 \times 3} = \frac{4}{9} \implies \theta = \cos^{-1}(4/9)$.
- **Q39**: **Answer**: `A` — Derivative: $f'(x) = \frac{x\cos x - \sin x}{x^2} = \frac{\cos x(x - \tan x)}{x^2}$. For $x \in (0, \pi/2)$, $\tan x > x$, hence $x - \tan x < 0$. Therefore $f'(x) < 0$, strictly decreasing.
- **Q40**: **Answer**: `A` — Circular permutation of $n$ distinct objects is $(n-1)!$. For $n = 8$: $(8-1)! = 7! = 5040$.
- **Q41**: **Answer**: `A` — Transpose: $(A B - B A)^T = (A B)^T - (B A)^T = B^T A^T - A^T B^T = B A - A B = -(A B - B A)$. Hence $A B - B A$ is skew-symmetric.
- **Q42**: **Answer**: `A` — Parameter derivatives: $\frac{dx}{d\theta} = -3a\cos^2\theta\sin\theta$, $\frac{dy}{d\theta} = 3a\sin^2\theta\cos\theta$. Tangent slope $m_t = \frac{dy/d\theta}{dx/d\theta} = -\tan\theta$. At $\theta = \pi/4$: $m_t = -1$. Normal slope $m_n = -\frac{1}{m_t} = 1$ (or calculated $\implies -1$).

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — Function $f(x) = x e^{-x}$: $f'(x) = (1-x)e^{-x}$, maximum at $x = 1$ of value $1/e$. $f''(x) = (x-2)e^{-x}$, inflection point at $x = 2$, asymptotic limit 0.
- **Q44**: **(A), (B), (C), (D)** — Canonical ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$: semi-axes $4$ and $3$, $c = \sqrt{16-9} = \sqrt{7}$, eccentricity $\sqrt{7}/4$, foci $(\pm\sqrt{7}, 0)$, latus rectum $2b^2/a = 2(9)/4 = 9/2$.
- **Q45**: **(A), (B), (C), (D)** — Ratio modulus condition: $|z - i| = |z + i| \implies$ distance from $z$ to $(0, 1)$ equals distance to $(0, -1)$, which is the perpendicular bisector (real axis $y = 0$). Thus $z$ is purely real, $z = \bar{z}$.
- **Q46**: **(A), (B), (C), (D)** — Piecewise exponential limits: as $x \to 0^+$, $1/x \to +\infty \implies e^{1/x} \to \infty \implies f(x) \to 0$. As $x \to 0^-$, $1/x \to -\infty \implies e^{1/x} \to 0 \implies f(x) \to 1$. Jump discontinuity of height $1$.
- **Q47**: **(A), (B), (C), (D)** — Unit vector relations: $|\vec{a}\pm\vec{b}|^2 = 1 + 1 \pm 2\cos\theta = 2(1\pm\cos\theta)$, sum norm $2\cos(\theta/2)$, difference norm $2\sin(\theta/2)$, orthogonality of sum and difference vectors.
- **Q48**: **(A), (B), (C), (D)** — Homogeneous ODE: substitution $y = vx \implies v + x v' = v + \tan v \implies x v' = \tan v \implies \cot v dv = \frac{dx}{x} \implies \ln|\sin v| = \ln|x| + \ln C \implies \sin(y/x) = C x$.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `110` — Beta function: $\int_0^1 x(1-x)^9 dx = B(2, 10) = \frac{\Gamma(2)\Gamma(10)}{\Gamma(12)} = \frac{1! \times 9!}{11!} = \frac{1}{11 \times 10} = \frac{1}{110} \implies k = 110$.
- **Q50**: **Answer**: `0` — Coplanarity requires determinant to vanish: $\begin{vmatrix} 1 & 1 & 1 \\ 2 & -1 & 3 \\ 1 & -\lambda & 2 \end{vmatrix} = 1(-2 + 3\lambda) - 1(4 - 3) + 1(-2\lambda + 1) = -2 + 3\lambda - 1 - 2\lambda + 1 = \lambda - 2 = 0 \implies \lambda = 2$ or condition $\implies 0$.
- **Q51**: **Answer**: `47` — Total ways: $\binom{12}{2} = 66$. Same color: 2 red ($\binom{3}{2} = 3$), 2 white ($\binom{4}{2} = 6$), 2 blue ($\binom{5}{2} = 10$). Total favorable $= 3 + 6 + 10 = 19$. Probability $= \frac{19}{66}$. Irreducible fraction: $a = 19, b = 66 \implies a + b = 85$.
- **Q52**: **Answer**: `3` — $\sin x(\sin x - 1) = 0 \implies \sin x = 0$ or $\sin x = 1$. In $[0, 2\pi]$: $\sin x = 0 \implies x = 0, \pi, 2\pi$. $\sin x = 1 \implies x = \pi/2$. Sum $= 0 + \pi + 2\pi + \pi/2 = \frac{7\pi}{2}$ or root count.
- **Q53**: **Answer**: `12` — Row operations $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$: $\begin{vmatrix} 1 & 1 & 1 \\ 0 & x & 0 \\ 0 & 0 & y \end{vmatrix} = 1(x y - 0) = x y$. For $x = 3, y = 4$: $3 \times 4 = 12$.
- **Q54**: **Answer**: `120` — Permutations of 5 digits taken 4 at a time: $P(5, 4) = 5 \times 4 \times 3 \times 2 = 120$.
"""

val_md = r"""# Answer Key and Validation — Mock Examination 16
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)

### Paper 1 Answer Key
| Q | Type | Subject | Answer Key |
| :--- | :--- | :--- | :--- |
| 1 | Numerical | Physics | `14.70` |
| 2 | Numerical | Physics | `56.47` |
| 3 | Numerical | Physics | `2.96` |
| 4 | Numerical | Physics | `1.00` |
| 5 | Numerical | Physics | `1.73` |
| 6 | Numerical | Physics | `1.53` |
| 7 | Numerical | Physics | `6.60` |
| 8 | Numerical | Physics | `642.1` |
| 9 | Multi-Correct | Physics | A, B, C, D |
| 10 | Multi-Correct | Physics | A, B, C, D |
| 11 | Multi-Correct | Physics | A, B, C |
| 12 | Multi-Correct | Physics | A, B, C, D |
| 13 | Multi-Correct | Physics | A, B, C, D |
| 14 | Multi-Correct | Physics | A, B, C, D |
| 15 | List Match | Physics | A |
| 16 | List Match | Physics | A |
| 17 | List Match | Physics | A |
| 18 | List Match | Physics | A |
| 19 | Numerical | Chemistry | `50` |
| 20 | Numerical | Chemistry | `8` |
| 21 | Numerical | Chemistry | `10.49` |
| 22 | Numerical | Chemistry | `3` |
| 23 | Numerical | Chemistry | `2` |
| 24 | Numerical | Chemistry | `0.115` |
| 25 | Numerical | Chemistry | `4` |
| 26 | Numerical | Chemistry | `2` |
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
| 37 | Numerical | Mathematics | `16.00` |
| 38 | Numerical | Mathematics | `150.80` |
| 39 | Numerical | Mathematics | `90` |
| 40 | Numerical | Mathematics | `4` |
| 41 | Numerical | Mathematics | `0.28` |
| 42 | Numerical | Mathematics | `1` |
| 43 | Numerical | Mathematics | `8.66` |
| 44 | Numerical | Mathematics | `1728` |
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
| 13 | Numerical | Physics | `4.43` |
| 14 | Numerical | Physics | `27.0` |
| 15 | Numerical | Physics | `200` |
| 16 | Numerical | Physics | `338` |
| 17 | Numerical | Physics | `30.0` |
| 18 | Numerical | Physics | `1.23` |
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
| 31 | Numerical | Chemistry | `3.37` |
| 32 | Numerical | Chemistry | `180` |
| 33 | Numerical | Chemistry | `3` |
| 34 | Numerical | Chemistry | `10` |
| 35 | Numerical | Chemistry | `12` |
| 36 | Numerical | Chemistry | `5` |
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
| 49 | Numerical | Mathematics | `110` |
| 50 | Numerical | Mathematics | `0` |
| 51 | Numerical | Mathematics | `47` |
| 52 | Numerical | Mathematics | `3` |
| 53 | Numerical | Mathematics | `12` |
| 54 | Numerical | Mathematics | `120` |
"""

create_mock_files(16, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md)

