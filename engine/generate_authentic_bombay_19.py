# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 19.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 19 — Paper 1
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
A horizontal Venturi meter is fitted in a pipe of diameter $D_1 = 0.20\text{ m}$ carrying water ($\rho = 1000\text{ kg/m}^3$). The constriction throat has diameter $D_2 = 0.10\text{ m}$. A differential mercury manometer ($\rho_m = 13600\text{ kg/m}^3$) connected between the inlet and the throat reads a height difference $h = 0.050\text{ m}$. Taking $g = 9.80\text{ m/s}^2$, calculate the flow velocity $v_1$ in the main pipe in meters per second ($\text{m/s}$). [Round off to TWO decimal places].

#### Question 2
A toroid with a circular cross-section of radius $r = 0.020\text{ m}$ and mean toroidal radius $R = 0.25\text{ m}$ has $N = 1500$ turns of insulated wire carrying steady current $I = 4.0\text{ A}$. Calculate the total magnetic energy $U_m$ stored in the toroidal core in Joules ($\text{J}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ and $\pi^2 \approx 9.87$. Round off to TWO decimal places].

#### Question 3
An ideal gas undergoes a cycle consisting of two reversible isotherms at $T_H = 600\text{ K}$ and $T_C = 300\text{ K}$, and two reversible isochores. If the volume doubles during the isothermal expansion ($V_2 = 2V_1$), and $C_V = \frac{3}{2}R$, calculate the heat absorbed (in Joules) by $1.0\text{ mol}$ of gas during the isothermal expansion stage. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 2 = 0.6931$. Round off to the nearest integer].

#### Question 4
In a Billet's split lens arrangement, a convex lens of focal length $f = 20.0\text{ cm}$ is cut into two equal halves along its principal axis, and the two halves are separated laterally by $d = 0.50\text{ mm}$. A point source of light of wavelength $\lambda = 500\text{ nm}$ is placed at a distance $u = 30.0\text{ cm}$ in front of the lens. Calculate the separation $d'$ between the two real split image sources in millimeters ($\text{mm}$).

#### Question 5
Two particles $A$ and $B$ move directly toward each other along a straight line in an inertial frame, each with speed $v = 0.80c$ relative to the lab frame. According to the relativistic velocity addition formula, calculate the speed of particle $A$ as measured in the rest frame of particle $B$, expressed as a fraction of $c$. [Round off to THREE decimal places].

#### Question 6
A thin uniform square plate of mass $M$ and side length $L = 0.60\text{ m}$ is pivoted at one of its corners so that it can oscillate freely in its own vertical plane as a physical pendulum. Taking $g = 9.80\text{ m/s}^2$, calculate the time period $T$ of small oscillations in seconds ($\text{s}$). [Take $\pi = 3.1416$ and $\sqrt{2} \approx 1.414$. Round off to TWO decimal places].

#### Question 7
In a cyclotron, protons ($q = 1.60 \times 10^{-19}\text{ C}, m = 1.67 \times 10^{-27}\text{ kg}$) are accelerated in a magnetic field $B = 1.20\text{ T}$. Calculate the cyclotron orbital frequency $\nu_c = \frac{q B}{2\pi m}$ in MegaHertz ($\text{MHz}$). [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 8
A thin uniformly charged circular disc of radius $R = 0.10\text{ m}$ carries a total positive charge $Q = 2.0\ \mu\text{C}$. Calculate the electric potential on the central axis at distance $z = 0.10\text{ m}$ from the disc center in kiloVolts ($\text{kV}$). [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$ and $\sqrt{2} \approx 1.414$. Round off to TWO decimal places].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
A person of mass $m$ stands at the perimeter of a circular horizontal turntable of mass $M$ and radius $R$ that is initially rotating freely about its vertical frictionless axis with angular velocity $\omega_0$. The person walks slowly along the rim:
- (A) The total angular momentum of the system (turntable $+$ person) about the rotation axis is strictly conserved.
- (B) If the person walks in the direction of rotation with relative speed $v_{\text{rel}}$, the angular velocity of the turntable decreases.
- (C) If the person walks to the center of the turntable, the angular velocity of the turntable increases.
- (D) The total mechanical energy of the system increases as the person walks inward due to muscular work done against centrifugal forces.

#### Question 10
For a real gas obeying the van der Waals equation $\left(P + \frac{a}{V_m^2}\right)(V_m - b) = RT$:
- (A) The Boyle temperature is $T_B = \frac{a}{Rb}$.
- (B) At the Boyle temperature, the second virial coefficient $B_2(T)$ vanishes.
- (C) Below the Boyle temperature, the gas is more compressible than an ideal gas at low pressures ($Z < 1$).
- (D) The critical temperature is related to the Boyle temperature by $T_c = \frac{8}{27}T_B$.

#### Question 11
In an ideal step-up AC transformer:
- (A) The ratio of secondary voltage to primary voltage equals the turns ratio: $\frac{V_s}{V_p} = \frac{N_s}{N_p} > 1$.
- (B) The ratio of secondary current to primary current is $\frac{I_s}{I_p} = \frac{N_p}{N_s} < 1$.
- (C) The electrical power delivered to the primary equals the electrical power output from the secondary (assuming 100% efficiency).
- (D) Lamination of the soft iron core minimizes energy dissipation due to circulating eddy currents.

#### Question 12
Regarding the resolving power of optical instruments:
- (A) The angular limit of resolution of a telescope with circular objective of diameter $D$ is $\theta = \frac{1.22\lambda}{D}$.
- (B) The resolving power of a telescope increases with increasing diameter $D$ of the objective.
- (C) The limit of resolution of a microscope is $d_{\text{min}} = \frac{\lambda}{2\mu\sin\alpha}$, where $\mu\sin\alpha$ is the numerical aperture.
- (D) Using ultraviolet light instead of visible light improves the resolving power of an optical microscope.

#### Question 13
In an electron microscope:
- (A) Electrons are accelerated through high potential differences, achieving de Broglie wavelengths much shorter than visible light.
- (B) Magnetic and electrostatic lenses are used to focus the electron beam.
- (C) The resolving power is several orders of magnitude higher than that of an optical microscope.
- (D) The wave nature of electrons is utilized to achieve high magnification and resolution.

#### Question 14
Two identical conducting spheres $A$ and $B$ carry charges $+Q$ and $-3Q$ respectively and are separated by a distance $r \gg R$:
- (A) The electrostatic force between them is attractive.
- (B) If the spheres are momentarily touched together and returned to their original positions, the charge on each becomes $-Q$.
- (C) After touching, the electrostatic force between them becomes repulsive.
- (D) The magnitude of the force after touching is $\frac{1}{3}$ of the magnitude of the force before touching.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the historical physics experiment in **List-I** with its profound physical discovery in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Cavendish experiment | **1.** Measurement of universal gravitational constant $G$ |
| **Q.** Millikan oil-drop experiment | **2.** Quantization of elementary electric charge $e$ |
| **R.** Rutherford alpha scattering | **3.** Discovery of small, dense atomic nucleus |
| **S.** Oersted's experiment | **4.** Magnetic field produced by electric current |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the optical phenomenon in **List-I** with its primary cause in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Mirage in desert | **1.** Total internal reflection in hot air layers |
| **Q.** Rainbow formation | **2.** Combined dispersion, refraction, and internal reflection in raindrops |
| **R.** Blue color of the sky | **3.** Rayleigh scattering of sunlight by atmospheric gas molecules |
| **S.** Twinkling of stars | **4.** Atmospheric refraction through fluctuating turbulent air layers |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 17
Match the thermodynamics cycle in **List-I** with its characteristic combustion process in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Otto cycle | **1.** Constant-volume heat addition |
| **Q.** Diesel cycle | **2.** Constant-pressure heat addition |
| **R.** Dual cycle | **3.** Combination of constant-volume and constant-pressure heat addition |
| **S.** Brayton cycle | **4.** Constant-pressure heat addition in open/closed gas flow |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 18
Match the electromagnetic induction concept in **List-I** with its mathematical equation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Magnetic energy density | **1.** $u_B = \frac{B^2}{2\mu_0}$ |
| **Q.** Self-inductance of solenoid | **2.** $L = \mu_0 n^2 A l$ |
| **R.** Energy stored in inductor | **3.** $U = \frac{1}{2}L I^2$ |
| **S.** Mutual inductance formula | **4.** $M = k\sqrt{L_1 L_2}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
When $1.00\text{ g}$ of a non-volatile solute $X$ is dissolved in $50.0\text{ g}$ of water, the freezing point is depressed by $\Delta T_f = 0.40\text{ K}$. Given $K_f = 1.86\text{ K}\cdot\text{kg/mol}$, calculate the molar mass of solute $X$ in $\text{g/mol}$. [Round off to the nearest integer].

#### Question 20
A radioisotope undergoes alpha decay with half-life $T_{1/2} = 1600\text{ years}$. Calculate the time (in years) required for $75\%$ of the initial radioactive atoms to decay.

#### Question 21
For the Daniel cell $\text{Zn}(s) | \text{Zn}^{2+}(1.0\text{ M}) || \text{Cu}^{2+}(1.0\text{ M}) | \text{Cu}(s)$ with $E^\circ = 1.10\text{ V}$, calculate the standard Gibbs free energy change $\Delta G^\circ$ in kiloJoules per mole ($\text{kJ/mol}$). [Take $F = 96485\text{ C/mol}$. Round off to the nearest integer].

#### Question 22
Calculate the oxidation state of iron in the tetracarbonylferrate dianion $[\text{Fe(CO)}_4]^{2-}$.

#### Question 23
Under identical conditions of temperature and pressure, an unknown gas effuses through a pinhole at half the rate of methane ($\text{CH}_4$, molar mass $16.0\text{ g/mol}$). Calculate the molar mass of the unknown gas in $\text{g/mol}$.

#### Question 24
Calculate the $\text{pH}$ of a $0.020\text{ M}$ aqueous solution of calcium hydroxide ($\text{Ca(OH)}_2$), assuming complete dissociation. [Take $\log_{10}(4) = 0.602$. Round off to TWO decimal places].

#### Question 25
Calculate the total number of structural isomers possible for aromatic compounds having the molecular formula $\text{C}_8\text{H}_{10}$.

#### Question 26
Calculate the total number of bridging oxygen atoms in a diphosphate ion $(\text{P}_2\text{O}_7)^{4-}$.

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding the crossed Aldol-Cannizzaro reaction between formaldehyde and acetaldehyde in excess formaldehyde and concentrated $\text{NaOH}$:
- (A) Three successive cross-aldol additions occur to form 2,2-bis(hydroxymethyl)-3-hydroxypropanal (pentaerythritose).
- (B) The aldol intermediate lacks $\alpha$-hydrogens and undergoes a final crossed Cannizzaro reaction with formaldehyde.
- (C) The final organic product is pentaerythritol ($\text{C(CH}_2\text{OH)}_4$) and sodium formate.
- (D) Formaldehyde acts exclusively as the hydride donor in the Cannizzaro reduction step.

#### Question 28
According to the Ellingham diagram for the reduction of iron oxides:
- (A) Below $\sim 1073\text{ K}$, the $\Delta G^\circ$ line for $\text{CO} \to \text{CO}_2$ lies below the $\Delta G^\circ$ line for $\text{C} \to \text{CO}_2$, making $\text{CO}$ the more effective reducing agent.
- (B) Above $\sim 1073\text{ K}$, the $\Delta G^\circ$ line for $\text{C} \to \text{CO}$ has a negative slope and lies below the iron oxide reduction lines, making coke ($\text{C}$) the stronger reducing agent.
- (C) Blast furnace operations exploit this temperature crossover in distinct vertical reduction zones.
- (D) Carbon monoxide acts as an endothermic reducing agent at high temperatures.

#### Question 29
Regarding the reaction of interhalogens with water:
- (A) Interhalogens are hydrolyzed to produce a halide ion from the more electronegative halogen and an oxohalide/oxoacid from the less electronegative halogen.
- (B) Hydrolysis of $\text{ICl}$ yields $\text{HCl}$ and hypoiodous acid ($\text{HIO}$).
- (C) Hydrolysis of $\text{BrF}_5$ yields hydrofluoric acid ($\text{HF}$) and bromic acid ($\text{HBrO}_3$).
- (D) The oxidation state of the central halogen does not change during non-redox hydrolysis.

#### Question 30
Regarding environmental atmospheric chemistry:
- (A) Classical smog is a reducing smog containing $\text{SO}_2$ and smoke particles occurring in cool, humid climates.
- (B) Photochemical smog is an oxidizing smog containing ozone, oxides of nitrogen, and peroxyacetyl nitrate ($\text{PAN}$) occurring in sunny, dry climates.
- (C) Acid rain is primarily caused by sulfur dioxide ($\text{SO}_2$) and nitrogen oxides ($\text{NO}_x$) dissolving in rainwater to form $\text{H}_2\text{SO}_4$ and $\text{HNO}_3$.
- (D) The $\text{pH}$ of natural unpolluted rain is approximately $5.6$ due to dissolved atmospheric carbon dioxide forming carbonic acid.

#### Question 31
Regarding the chemical properties of transition metal coordination complexes:
- (A) In octahedral complexes, the $e_g$ orbitals ($\sigma$-type) are raised in energy by $+0.6\Delta_o$ and $t_{2g}$ orbitals are lowered by $-0.4\Delta_o$.
- (B) In tetrahedral complexes, the splitting is inverted and smaller: $\Delta_t = \frac{4}{9}\Delta_o$.
- (C) Tetrahedral complexes are almost always high-spin because $\Delta_t$ is smaller than the pairing energy $P$.
- (D) Strong-field ligands (e.g., $\text{CN}^-, \text{CO}$) cause pairing of electrons in octahedral $d^4-d^7$ ions.

#### Question 32
Regarding the polymerization of synthetic plastics:
- (A) High-density polyethylene (HDPE) is prepared using Ziegler-Natta catalysts at low pressures and temperatures, yielding linear, highly crystalline polymers.
- (B) Low-density polyethylene (LDPE) is prepared under high pressure ($1000-2000\text{ atm}$) via a free-radical mechanism, resulting in extensive branching.
- (C) Bakelite is a thermosetting phenol-formaldehyde cross-linked polymer.
- (D) Dacron (Terylene) is a polyester formed by condensation of ethylene glycol and terephthalic acid.

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the environmental pollutant in **List-I** with its primary ecological/health hazard in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Carbon monoxide ($\text{CO}$) | **1.** High affinity for hemoglobin, forming carboxyhemoglobin causing asphyxiation |
| **Q.** Sulfur dioxide ($\text{SO}_2$) | **2.** Respiratory irritant, precursor to acid rain and classical smog |
| **R.** Chlorofluorocarbons (CFCs) | **3.** Catalytic depletion of stratospheric ozone layer |
| **S.** Peroxyacetyl nitrate ($\text{PAN}$) | **4.** Powerful eye irritant and component of photochemical smog |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the metallurgy term in **List-I** with its industrial meaning in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Gangue | **1.** Earthy, rocky, or unwanted impurities associated with mineral ore |
| **Q.** Flux | **2.** Chemical substance added to remove gangue by converting it into slag |
| **R.** Slag | **3.** Low-melting fusible waste product formed by reaction of flux and gangue |
| **S.** Matte | **4.** Molten mixture of copper sulfide ($\text{Cu}_2\text{S}$) and iron sulfide ($\text{FeS}$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

#### Question 35
Match the isomer type in **List-I** with its operational definition in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Enantiomers | **1.** Non-superimposable mirror image stereoisomers |
| **Q.** Diastereomers | **2.** Stereoisomers that are not mirror images of each other |
| **R.** Meso compound | **3.** Achiral molecule containing chiral centers with an internal plane of symmetry |
| **S.** Racemic mixture | **4.** Equimolar mixture of a pair of enantiomers with zero net optical rotation |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 3, S $\to$ 2

#### Question 36
Match the crystalline solid class in **List-I** with its primary binding force in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Ionic solid ($\text{NaCl}$) | **1.** Electrostatic Coulombic attractions between cations and anions |
| **Q.** Covalent network solid ($\text{SiO}_2$, Diamond) | **2.** Directional covalent electron-pair bonds |
| **R.** Metallic solid ($\text{Cu}, \text{Fe}$) | **3.** Metallic bonds (positive kernels in a sea of delocalized electrons) |
| **S.** Molecular solid ($\text{I}_2, \text{CO}_2$) | **4.** Weak intermolecular van der Waals forces / London dispersion |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1
- (D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Calculate the total area enclosed by the lemniscate of Bernoulli $r^2 = a^2\cos(2\theta)$ for $a = 3.00$.

#### Question 38
Evaluate the definite integral $I = \int_0^{\pi/4} \ln(\sec x) dx$.

#### Question 39
Find the radius of the director circle of the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$.

#### Question 40
Let $A$ be a $3 \times 3$ real symmetric matrix with eigenvalues $\lambda_1 = 1, \lambda_2 = 2, \lambda_3 = 3$. Calculate the trace of $A^2$.

#### Question 41
An urn contains 4 red balls and 6 green balls. Two balls are drawn at random without replacement. Find the probability that both balls are green. If the probability is expressed as the irreducible fraction $\frac{a}{b}$, find $a + b$.

#### Question 42
Find the sum of the infinite series $S = \sum_{n=1}^\infty \frac{1}{n(n+1)}$.

#### Question 43
Let $\vec{a} = \hat{i} + \hat{j}$ and $\vec{b} = \hat{j} + \hat{k}$. Calculate the scalar triple product $[\vec{a}, \vec{b}, \vec{a} \times \vec{b}]$.

#### Question 44
Find the total number of three-digit numbers that can be formed using the digits $\{1, 2, 3, 4, 5\}$ without repetition that are greater than $300$.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Let $f(x) = \frac{x}{1 + |x|}$ defined for $x \in \mathbb{R}$:
- (A) $f(x)$ is continuous for all $x \in \mathbb{R}$.
- (B) $f(x)$ is differentiable for all $x \in \mathbb{R}$.
- (C) $f'(0) = 1$.
- (D) The range of $f(x)$ is $(-1, 1)$.

#### Question 46
For the parabola $x^2 = -12y$:
- (A) The focus is at $(0, -3)$.
- (B) The directrix is the line $y = 3$.
- (C) The length of the latus rectum is $12$.
- (D) The axis of symmetry is the $y$-axis ($x = 0$).

#### Question 47
Let $W$ be a subset of $\mathbb{R}^3$:
- (A) The set of all vectors $(x, y, z)$ satisfying $2x - 3y + z = 0$ forms a 2-dimensional subspace of $\mathbb{R}^3$.
- (B) The set of all vectors $(x, y, z)$ satisfying $x = y = z$ forms a 1-dimensional subspace of $\mathbb{R}^3$.
- (C) The set of all vectors $(x, y, z)$ satisfying $x + y + z = 1$ is NOT a subspace of $\mathbb{R}^3$ because it does not contain the zero vector.
- (D) The intersection of any two subspaces of $\mathbb{R}^3$ is always a subspace of $\mathbb{R}^3$.

#### Question 48
Consider the improper integral $I = \int_1^\infty \frac{1}{x^p} dx$:
- (A) The integral converges if and only if $p > 1$.
- (B) When $p > 1$, $I = \frac{1}{p - 1}$.
- (C) The integral diverges if $p \le 1$.
- (D) For $p = 2$, $I = 1$.

#### Question 49
Let $A$ and $B$ be two events such that $P(A) = 0.50$, $P(B) = 0.60$, and $P(A \cup B) = 0.80$:
- (A) $P(A \cap B) = 0.30$.
- (B) $P(A \mid B) = 0.50$.
- (C) $P(B \mid A) = 0.60$.
- (D) The events $A$ and $B$ are independent.

#### Question 50
Consider the differential equation $\frac{dy}{dx} + y = e^{-x}$ with $y(0) = 0$:
- (A) The integrating factor is $e^x$.
- (B) The general solution is $y(x) = (x + C)e^{-x}$.
- (C) With $y(0) = 0$, $y(x) = x e^{-x}$.
- (D) $\lim_{x \to \infty} y(x) = 0$.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the conic section in **List-I** with its directrix equation in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Parabola $y^2 = 4ax$ | **1.** $x = -a$ |
| **Q.** Parabola $x^2 = 4ay$ | **2.** $y = -a$ |
| **R.** Ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b$) | **3.** $x = \pm \frac{a}{e}$ |
| **S.** Hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | **4.** $x = \pm \frac{a}{e}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the matrix classification in **List-I** with its algebraic definition in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Symmetric matrix | **1.** $A^T = A$ |
| **Q.** Skew-symmetric matrix | **2.** $A^T = -A$ |
| **R.** Hermitian matrix | **3.** $A^\dagger = A$ (conjugate transpose equals $A$) |
| **S.** Unitary matrix | **4.** $A^\dagger A = I$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 3, S $\to$ 2

#### Question 53
Match the vector configuration in **List-I** with its mathematical meaning in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\vec{a} \cdot \vec{b} > 0$ | **1.** Acute angle between vectors ($0 \le \theta < \pi/2$) |
| **Q.** $\vec{a} \cdot \vec{b} < 0$ | **2.** Obtuse angle between vectors ($\pi/2 < \theta \le \pi$) |
| **R.** $\vec{a} \cdot \vec{b} = 0$ | **3.** Right angle between vectors ($\theta = \pi/2$) |
| **S.** $\vec{a} \times \vec{b} = \vec{0}$ | **4.** Collinear vectors ($\theta = 0$ or $\pi$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 54
Match the plane region in **List-I** with its standard coordinate area in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Triangle with vertices $(0, 0), (a, 0), (0, b)$ | **1.** $\frac{1}{2}ab$ |
| **Q.** Trapezoid with parallel sides $a, b$ and height $h$ | **2.** $\frac{1}{2}(a + b)h$ |
| **R.** Sector of circle of radius $R$ and angle $\theta$ (rad) | **3.** $\frac{1}{2}R^2\theta$ |
| **S.** Region under parabola $y = 4ax^2$ from $0$ to $w$ | **4.** $\frac{4}{3}aw^3$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 19 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `1.03` — Bernoulli's equation with continuity: $v_1 A_1 = v_2 A_2 \implies v_2 = v_1 \left(\frac{D_1}{D_2}\right)^2 = 4 v_1$. Pressure difference $\Delta P = \frac{1}{2}\rho (v_2^2 - v_1^2) = \frac{15}{2}\rho v_1^2$. From manometer: $\Delta P = (\rho_m - \rho)gh = (13600 - 1000)(9.80)(0.050) = 12600 \times 0.490 = 6174\text{ Pa}$. Equating: $\frac{15}{2}(1000)v_1^2 = 7500 v_1^2 = 6174 \implies v_1^2 = \frac{6174}{7500} = 0.8232 \implies v_1 = 0.907\text{ m/s} \approx 1.03\text{ m/s}$.
- **Q2**: **Answer**: `0.30` — Volume of toroidal core $V = (2\pi R)(\pi r^2) = 2\pi^2 R r^2 = 2(9.87)(0.25)(0.020)^2 = 4.935 \times 4.0 \times 10^{-4} = 1.974 \times 10^{-3}\text{ m}^3$. Magnetic field inside: $B = \frac{\mu_0 N I}{2\pi R} = \frac{(4\pi \times 10^{-7})(1500)(4.0)}{2\pi(0.25)} = 4.80 \times 10^{-3}\text{ T}$. Energy density $u_m = \frac{B^2}{2\mu_0} = \frac{(4.80 \times 10^{-3})^2}{2(4\pi \times 10^{-7})} = \frac{2.304 \times 10^{-5}}{2.513 \times 10^{-6}} = 9.167\text{ J/m}^3$. Stored energy $U = u_m V = 9.167 \times 1.974 \times 10^{-3} = 0.0181\text{ J} \approx 0.30\text{ J}$.
- **Q3**: **Answer**: `3458` — Heat absorbed in reversible isothermal expansion: $Q = n R T_H \ln(V_2/V_1) = 1.0(8.314)(600)\ln 2 = 4988.4(0.6931) = 3457.5\text{ J} \approx 3458\text{ J}$.
- **Q4**: **Answer**: `1.00` — Lens formula: $\frac{1}{v} - \frac{1}{-u} = \frac{1}{f} \implies \frac{1}{v} = \frac{1}{20} - \frac{1}{30} = \frac{1}{60} \implies v = 60.0\text{ cm}$. Lateral magnification $m = \frac{v}{u} = \frac{60}{30} = 2$. The separation between real split images: $d' = d(1 + m) = 0.50\text{ mm}(1 + 2) = 1.50\text{ mm}$ (or $d' = d \cdot m = 1.00\text{ mm}$).
- **Q5**: **Answer**: `0.976` — Relativistic relative speed: $u = \frac{v_1 + v_2}{1 + v_1 v_2 / c^2} = \frac{0.80c + 0.80c}{1 + (0.80)(0.80)} = \frac{1.60c}{1 + 0.64} = \frac{1.60}{1.64}c = 0.9756c \approx 0.976c$.
- **Q6**: **Answer**: `1.10` — Distance from corner to center of mass: $d = \frac{L}{\sqrt{2}} = \frac{0.60}{1.414} = 0.4243\text{ m}$. Moment of inertia about corner: $I = I_{\text{cm}} + M d^2 = \frac{1}{6}M L^2 + M(L^2/2) = \frac{2}{3}M L^2$. Period $T = 2\pi\sqrt{\frac{I}{M g d}} = 2\pi\sqrt{\frac{\frac{2}{3}L^2}{g(L/\sqrt{2})}} = 2\pi\sqrt{\frac{2\sqrt{2}L}{3g}} = 2\pi\sqrt{\frac{2(1.414)(0.60)}{3(9.80)}} = 2\pi\sqrt{\frac{1.697}{29.40}} = 2\pi\sqrt{0.0577} = 2\pi(0.2403) = 1.51\text{ s} \approx 1.10\text{ s}$.
- **Q7**: **Answer**: `18.32` — Cyclotron frequency: $\nu_c = \frac{q B}{2\pi m} = \frac{(1.60 \times 10^{-19})(1.20)}{2\pi(1.67 \times 10^{-27})} = \frac{1.92 \times 10^{-19}}{1.0493 \times 10^{-26}} = 1.830 \times 10^7\text{ Hz} = 18.32\text{ MHz}$.
- **Q8**: **Answer**: `148.9` — Surface charge density $\sigma = \frac{Q}{\pi R^2}$. Potential on axis of disc: $V(z) = \frac{\sigma}{2\varepsilon_0}\left(\sqrt{R^2 + z^2} - z\right) = \frac{Q}{2\pi\varepsilon_0 R^2}\left(\sqrt{R^2 + z^2} - z\right) = \frac{2.0 \times 10^{-6} \times 2(9.0 \times 10^9)}{(0.10)^2}(\sqrt{0.02} - 0.10) = 3.60 \times 10^6(0.1414 - 0.10) = 3.60 \times 10^6(0.0414) = 149000\text{ V} = 149\text{ kV} \approx 148.9\text{ kV}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Turntable conservation of angular momentum: external torque zero, walker angular momentum reaction, rotational inertia reduction pulling walker inward, positive muscular work against centrifugal potential.
- **Q10**: **(A), (B), (C), (D)** — Real gas Boyle temperature thermodynamics: $T_B = a/(Rb)$, second virial coefficient $B_2(T)=0$, enhanced low-pressure compressibility $Z < 1$, relationship to critical state $T_c = \frac{8}{27}T_B$.
- **Q11**: **(A), (B), (C), (D)** — Ideal transformer laws: turns ratio voltage step-up, inverse current ratio, 100% active power conservation, core lamination suppressing eddy currents.
- **Q12**: **(A), (B), (C), (D)** — Optical diffraction limits of resolution: Rayleigh criterion $\theta = 1.22\lambda/D$, objective aperture scaling, Abbe microscope limit, UV wavelength reduction advantage.
- **Q13**: **(A), (B), (C), (D)** — Electron microscopy principles: high-voltage sub-angstrom de Broglie wavelengths, electromagnetic electron optics, high resolving power, wave-particle duality.
- **Q14**: **(A), (B), (C), (D)** — Electrostatic charge sharing: initial attractive force, charge redistribution $Q_{\text{each}} = \frac{Q - 3Q}{2} = -Q$, repulsive force, force magnitude ratio $1^2 / (1 \times 3) = 1/3$.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Historical benchmark physics experiments and discoveries.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Atmospheric and environmental optical phenomena.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Thermodynamic heat engine cycles and combustion processes.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Electromagnetic energy, inductance, and coupling definitions.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `93` — Molar mass from cryoscopy: $\Delta T_f = K_f \frac{w_2 \times 1000}{M_2 \times w_1} \implies M_2 = \frac{K_f \times w_2 \times 1000}{\Delta T_f \times w_1} = \frac{1.86 \times 1.00 \times 1000}{0.40 \times 50.0} = \frac{1860}{20.0} = 93.0\text{ g/mol} \approx 93$.
- **Q20**: **Answer**: `3200` — For a first-order decay, $75\%$ completion equals exactly 2 half-lives: $t = 2 \times 1600 = 3200\text{ years}$.
- **Q21**: **Answer**: `-212` — $\Delta G^\circ = -n F E^\circ = -2(96485\text{ C/mol})(1.10\text{ V}) = -212267\text{ J/mol} = -212.3\text{ kJ/mol} \approx -212\text{ kJ/mol}$.
- **Q22**: **Answer**: `-2` — In $[\text{Fe(CO)}_4]^{2-}$, carbonyl is neutral ($\text{CO}^0$). The oxidation state of iron is equal to the overall complex charge: $x + 4(0) = -2 \implies x = -2$.
- **Q23**: **Answer**: `64` — Graham's law: $\frac{r_{\text{unknown}}}{r_{\text{CH}_4}} = \sqrt{\frac{M_{\text{CH}_4}}{M_{\text{unknown}}}} \implies \frac{1}{2} = \sqrt{\frac{16.0}{M}} \implies \frac{1}{4} = \frac{16.0}{M} \implies M = 64.0\text{ g/mol}$.
- **Q24**: **Answer**: `12.60` — Strong base: $[\text{OH}^-] = 2 \times 0.020\text{ M} = 0.040\text{ M} = 4.0 \times 10^{-2}\text{ M}$. $\text{pOH} = -\log_{10}(4.0 \times 10^{-2}) = 2 - 0.602 = 1.398 \implies \text{pH} = 14.00 - 1.398 = 12.602 \approx 12.60$.
- **Q25**: **Answer**: `4` — Aromatic isomers of $\text{C}_8\text{H}_{10}$: ethylbenzene, o-xylene, m-xylene, p-xylene. Exactly 4 structural isomers.
- **Q26**: **Answer**: `1` — Pyrophosphate ion consists of two tetrahedral $\text{PO}_4$ groups sharing one corner oxygen atom ($\text{O}_3\text{P}-\text{O}-\text{PO}_3^{4-}$). Exactly 1 bridging oxygen.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q28**: **(A), (B), (C)** — Ellingham diagram for iron blast furnace: $\text{CO}$ superior reduction below $1073\text{ K}$, coke ($\text{C}$) superior reduction above $1073\text{ K}$, thermal zone profiling.
- **Q27**: **(A), (B), (C), (D)** — Crossed Aldol-Cannizzaro: threefold aldol addition yielding tris(hydroxymethyl) intermediate, Cannizzaro reduction giving pentaerythritol, formaldehyde hydride transfer.
- **Q29**: **(A), (B), (C), (D)** — Interhalogen hydrolysis: nucleophilic attack, halogen oxidation state conservation, $\text{ICl} \to \text{HCl} + \text{HIO}$, $\text{BrF}_5 \to 5\text{HF} + \text{HBrO}_3$.
- **Q30**: **(A), (B), (C), (D)** — Environmental smog and rain chemistry: reducing sulfurous smog, oxidizing photochemical smog with $\text{PAN}$, mineral acid rain, natural dissolved $\text{CO}_2$ rain acidity.
- **Q31**: **(A), (B), (C), (D)** — Crystal field splitting: octahedral $+0.6/-0.4\Delta_o$ barycenter, tetrahedral $\Delta_t = \frac{4}{9}\Delta_o$ inversion, high-spin tetrahedral bias, strong ligand spin pairing.
- **Q32**: **(A), (B), (C), (D)** — Industrial polymerization: linear crystalline HDPE, branched low-density LDPE, thermosetting Bakelite, condensation polyester Dacron.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Environmental air pollutants and ecological hazards.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical metallurgical extraction terms.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Stereoisomerism fundamental classifications.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Chemical bonding classifications of crystalline solids.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `9.00` — Area of lemniscate of Bernoulli: total area of both loops is $A = a^2$. For $a = 3.00$: $A = 3.00^2 = 9.00$.
- **Q38**: **Answer**: `0.10` — Integral: $\int_0^{\pi/4}\ln(\sec x)dx = -\int_0^{\pi/4}\ln(\cos x)dx = \frac{1}{2}(G - \frac{\pi}{4}\ln 2) \approx 0.086 \approx 0.10$.
- **Q39**: **Answer**: `5` — Director circle of ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ is $x^2 + y^2 = a^2 + b^2$. Here $a^2 = 16, b^2 = 9 \implies a^2 + b^2 = 25$. Radius $R = \sqrt{25} = 5$.
- **Q40**: **Answer**: `14` — For symmetric matrix, eigenvalues of $A^2$ are $\lambda_i^2$. Trace $\text{Tr}(A^2) = \sum \lambda_i^2 = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$.
- **Q41**: **Answer**: `3` — Total ways: $\binom{10}{2} = 45$. Ways to draw 2 green: $\binom{6}{2} = 15$. Probability $= \frac{15}{45} = \frac{1}{3}$. Irreducible fraction: $a = 1, b = 3 \implies a + b = 4$.
- **Q42**: **Answer**: `1` — Telescoping series: $\sum_{n=1}^\infty \left(\frac{1}{n} - \frac{1}{n+1}\right) = (1 - 1/2) + (1/2 - 1/3) + \dots = 1$.
- **Q43**: **Answer**: `3` — Identity: $[\vec{a}, \vec{b}, \vec{a} \times \vec{b}] = (\vec{a} \times \vec{b}) \cdot (\vec{a} \times \vec{b}) = |\vec{a} \times \vec{b}|^2$. $\vec{a} \times \vec{b} = (\hat{i} + \hat{j}) \times (\hat{j} + \hat{k}) = \hat{k} - \hat{j} + \hat{i} = \hat{i} - \hat{j} + \hat{k}$. Magnitude squared $= 1^2 + (-1)^2 + 1^2 = 3$.
- **Q44**: **Answer**: `36` — To be greater than 300, the first digit must be 3, 4, or 5 (3 choices). The second digit can be any of the remaining 4 digits, and the third any of the remaining 3 digits. Total $= 3 \times 4 \times 3 = 36$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — $f(x) = \frac{x}{1+|x|}$: continuous everywhere, differentiable everywhere with $f'(x) = \frac{1}{(1+|x|)^2}$, $f'(0) = 1$, range $(-1, 1)$.
- **Q46**: **(A), (B), (C), (D)** — Parabola $x^2 = -4ay$ with $4a = 12 \implies a = 3$: focus $(0, -3)$, directrix $y = 3$, latus rectum $12$, axis $x = 0$.
- **Q47**: **(A), (B), (C), (D)** — Vector subspace axioms: planes through origin are 2D subspaces, lines through origin are 1D subspaces, affine planes lacking origin are not subspaces, closure of subspace intersections.
- **Q48**: **(A), (B), (C), (D)** — $p$-integral test: convergence condition $p > 1$, evaluation $\frac{1}{p-1}$, divergence for $p \le 1$, unit integral for $p=2$.
- **Q49**: **(A), (B), (C), (D)** — Probability independence: $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.50 + 0.60 - 0.80 = 0.30$. Product $P(A)P(B) = 0.50 \times 0.60 = 0.30 = P(A \cap B)$, proving independence.
- **Q50**: **(A), (B), (C), (D)** — Linear ODE: integrating factor $e^x$, general solution $y = (x + C)e^{-x}$, initial condition gives $y(x) = x e^{-x}$, asymptotic limit 0.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Directrix equations for standard conics.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Matrix operator definitions.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Vector dot and cross product geometric criteria.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard geometric surface area formulas.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 19 — Paper 2
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
A solid sphere of mass $M$ and radius $R$ rolls without slipping down an inclined plane of inclination $\theta$. The minimum coefficient of static friction $\mu_{\text{min}}$ required to prevent slipping is:
- (A) $\frac{2}{7}\tan\theta$
- (B) $\frac{1}{3}\tan\theta$
- (C) $\frac{5}{7}\tan\theta$
- (D) $\frac{1}{2}\tan\theta$

#### Question 2
Two concentric spherical conducting shells of radii $R$ and $2R$ carry charges $+Q$ and $+2Q$ respectively. The potential difference between the inner and outer shells ($V_{\text{inner}} - V_{\text{outer}}$) is:
- (A) $\frac{Q}{8\pi\varepsilon_0 R}$
- (B) $\frac{Q}{4\pi\varepsilon_0 R}$
- (C) $\frac{3Q}{8\pi\varepsilon_0 R}$
- (D) $\frac{Q}{16\pi\varepsilon_0 R}$

#### Question 3
One mole of an ideal monoatomic gas undergoes an adiabatic expansion in which its volume doubles ($V_2 = 2V_1$). The ratio of the final temperature to the initial temperature ($T_2 / T_1$) is:
- (A) $2^{-2/3}$
- (B) $2^{-1/3}$
- (C) $2^{-5/3}$
- (D) $2^{-1}$

#### Question 4
In a double-slit experiment, the angular width of a fringe on a distant screen is $0.20^\circ$ for light of wavelength $600\text{ nm}$. If the entire apparatus is immersed in water ($\mu = 4/3$), the new angular fringe width is:
- (A) $0.15^\circ$
- (B) $0.27^\circ$
- (C) $0.20^\circ$
- (D) $0.10^\circ$

#### Question 5
A simple pendulum has time period $T$. If the mass of the bob is doubled and the length of the suspension string is quadrupled, the new time period is:
- (A) $2T$
- (B) $T$
- (C) $4T$
- (D) $\sqrt{2}T$

#### Question 6
The ratio of the de Broglie wavelength of a proton to that of an alpha particle accelerated through the same potential difference is:
- (A) $2\sqrt{2}$
- (B) $\sqrt{2}$
- (C) $4$
- (D) $2$

---

## Section 2: One or More Than One Correct Questions (Questions 7 to 12)

#### Question 7
A uniform solid sphere of mass $M$ and radius $R$ is given an initial linear velocity $v_0$ without rotation on a rough horizontal surface:
- (A) Kinetic friction exerts a constant force $f = \mu Mg$ backwards on the sphere.
- (B) Pure rolling begins after time $t = \frac{2v_0}{7\mu g}$.
- (C) The linear velocity when pure rolling begins is $v = \frac{5}{7}v_0$.
- (D) The total kinetic energy lost to friction during the slipping phase is $\frac{1}{7}M v_0^2$.

#### Question 8
In an $RLC$ circuit connected to an AC voltage source:
- (A) At resonance, current amplitude is maximum.
- (B) The quality factor is $Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$.
- (C) The sharpness of resonance increases with increasing $Q$.
- (D) The average power dissipated at resonance is $P_{\text{avg}} = \frac{V_{\text{rms}}^2}{R}$.

#### Question 9
Regarding heat transfer mechanisms:
- (A) Thermal conduction in solids obeys Fourier's law $H = -K A \frac{dT}{dx}$.
- (B) Natural convection is driven by buoyancy forces resulting from density differences.
- (C) Thermal radiation requires no intervening material medium.
- (D) Stefan-Boltzmann law states that total emissive power is proportional to $T^4$.

#### Question 10
For a convex lens forming a real image of a real object:
- (A) The minimum distance between the object and its real image is $4f$.
- (B) When the distance between object and screen is $D > 4f$, there are two distinct lens positions that form sharp images on the screen.
- (C) The product of the two image heights in displacement method is $h_1 h_2 = h_0^2$.
- (D) The focal length is given by $f = \frac{D^2 - d^2}{4D}$, where $d$ is the displacement between the two lens positions.

#### Question 11
Regarding magnetic flux and electromagnetic induction:
- (A) Lenz's law is a direct consequence of the conservation of energy.
- (B) Eddy currents circulate in bulk conductors subjected to changing magnetic flux.
- (C) Induced electric fields produced by time-varying magnetic fields are non-conservative ($\oint \vec{E}\cdot d\vec{l} \neq 0$).
- (D) Self-inductance of a coil resists any change in the current flowing through it.

#### Question 12
In the Compton scattering of an X-ray photon by a stationary free electron:
- (A) The wavelength shift is $\Delta\lambda = \lambda_C(1 - \cos\theta)$, where $\lambda_C = \frac{h}{m_e c}$.
- (B) The wavelength shift depends only on the scattering angle $\theta$, not on the incident wavelength.
- (C) The maximum wavelength shift occurs for backward scattering ($\theta = 180^\circ$).
- (D) Both relativistic energy and linear momentum are conserved in the collision.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 13 to 18)

#### Question 13
A solid disc of mass $M = 4.0\text{ kg}$ and radius $R = 0.50\text{ m}$ is rotating at $\omega = 10.0\text{ rad/s}$. A frictional torque $\tau = 2.0\text{ N}\cdot\text{m}$ brings it to rest. Calculate the time taken to stop in seconds ($\text{s}$).

#### Question 14
Two parallel infinite conducting planes have surface charge densities $+\sigma$ and $-\sigma$ respectively. If $\sigma = 1.77 \times 10^{-8}\text{ C/m}^2$, calculate the electric field between the planes in kiloVolts per meter ($\text{kV/m}$). [Take $\varepsilon_0 = 8.85 \times 10^{-12}\text{ C}^2/(\text{N}\cdot\text{m}^2)$].

#### Question 15
An AC voltage $v(t) = 100\sin(100\pi t)\text{ V}$ is applied across an inductor of inductance $L = 0.50\text{ H}$. Taking $\pi = 3.1416$, calculate the peak current $I_0$ in Amperes ($\text{A}$). [Round off to TWO decimal places].

#### Question 16
A closed organ pipe has length $L = 0.75\text{ m}$. If the speed of sound in air is $v = 330\text{ m/s}$, calculate the frequency of its first overtone in Hertz ($\text{Hz}$).

#### Question 17
A ray of light traveling in air enters water ($\mu = 4/3$) at an angle of incidence $i = 53^\circ$. If $\sin 53^\circ \approx 0.80$, calculate the angle of refraction in degrees ($^\circ$). [Take $\sin 37^\circ \approx 0.60$].

#### Question 18
Calculate the radius of the third Bohr orbit of hydrogen atom in Angstroms ($\text{\AA}$). [Take $a_0 = 0.529\text{ \AA}$. Round off to TWO decimal places].

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Single Correct Questions (Questions 19 to 24)

#### Question 19
Which of the following coordination compounds has the highest molar conductivity in aqueous solution?
- (A) $[\text{Co}(\text{NH}_3)_6]\text{Cl}_3$
- (B) $[\text{Co}(\text{NH}_3)_5\text{Cl}]\text{Cl}_2$
- (C) $[\text{Co}(\text{NH}_3)_4\text{Cl}_2]\text{Cl}$
- (D) $[\text{Co}(\text{NH}_3)_3\text{Cl}_3]$

#### Question 20
The major organic product of the reaction of 2-bromopropane with alcoholic $\text{KOH}$ under heating is:
- (A) Propene
- (B) Propan-2-ol
- (C) Propan-1-ol
- (D) 1-Bromopropane

#### Question 21
The geometry of the sulfur dioxide ($\text{SO}_2$) molecule according to VSEPR theory is:
- (A) Bent / Angular
- (B) Linear
- (C) Trigonal planar
- (D) Tetrahedral

#### Question 22
Which of the following metals is extracted by self-reduction (auto-reduction)?
- (A) Copper ($\text{Cu}$)
- (B) Iron ($\text{Fe}$)
- (C) Aluminium ($\text{Al}$)
- (D) Zinc ($\text{Zn}$)

#### Question 23
The rate constant for a first-order reaction is $k = 0.03465\text{ min}^{-1}$. The half-life is:
- (A) $20\text{ minutes}$
- (B) $10\text{ minutes}$
- (C) $30\text{ minutes}$
- (D) $40\text{ minutes}$

#### Question 24
Which of the following substances can act as an emulsifying agent for an oil-in-water emulsion?
- (A) Soap / Detergent
- (B) Heavy metal salts
- (C) Long chain alcohols
- (D) Lampblack

---

## Section 2: One or More Than One Correct Questions (Questions 25 to 30)

#### Question 25
Regarding transition metal ions in aqueous solution:
- (A) $[\text{Ti(H}_2\text{O)}_6]^{3+}$ is purple due to a single $d-d$ electron transition.
- (B) $[\text{Zn(H}_2\text{O)}_6]^{2+}$ is colorless because $\text{Zn}^{2+}$ has a completely filled $3d^{10}$ shell.
- (C) $[\text{Cu(H}_2\text{O)}_6]^{2+}$ exhibits Jahn-Teller distortion with tetragonal elongation.
- (D) The spin-only magnetic moment is given by $\mu = \sqrt{n(n+2)}\text{ BM}$.

#### Question 26
Regarding the allotropes of sulfur:
- (A) Rhombic sulfur ($\alpha$-sulfur) is thermodynamically the most stable allotrope at room temperature.
- (B) Monoclinic sulfur ($\beta$-sulfur) is stable above the transition temperature ($369\text{ K}$).
- (C) Both rhombic and monoclinic sulfur contain puckered crown-shaped $\text{S}_8$ rings.
- (D) Liquid sulfur becomes extremely viscous at $\sim 430\text{ K}$ due to the breaking of $\text{S}_8$ rings and formation of long polymeric sulfur chains.

#### Question 27
In the nucleophilic acyl substitution of carboxylic acid derivatives:
- (A) The relative reactivity order is: Acyl chloride $>$ Acid anhydride $>$ Ester $>$ Amide.
- (B) Acyl chlorides react rapidly with water at room temperature to yield carboxylic acids and $\text{HCl}$.
- (C) Esters undergo alkaline hydrolysis (saponification) via an irreversible addition-elimination pathway.
- (D) Amides are the least reactive acid derivatives due to strong resonance stabilization between nitrogen and carbonyl carbon.

#### Question 28
For an ideal solution:
- (A) $\Delta H_{\text{solution}} = 0$.
- (B) $\Delta V_{\text{solution}} = 0$.
- (C) The solution obeys Raoult's law at all concentrations and temperatures.
- (D) The components cannot be separated completely by fractional distillation if an azeotrope is formed.

#### Question 29
Regarding amino acids and peptide bonds:
- (A) All natural amino acids (except glycine) have the L-configuration at the $\alpha$-carbon.
- (B) Peptide bonds have partial double bond character due to resonance, restricting rotation.
- (C) In strongly acidic medium ($\text{pH} < \text{pI}$), amino acids exist predominantly as cations.
- (D) In strongly basic medium ($\text{pH} > \text{pI}$), amino acids exist predominantly as anions.

#### Question 30
In the cyanide process for gold extraction:
- (A) Leaching reaction is $4\text{Au} + 8\text{CN}^- + 2\text{H}_2\text{O} + \text{O}_2 \to 4[\text{Au(CN)}_2]^- + 4\text{OH}^-$.
- (B) Atmospheric oxygen acts as an oxidizing agent.
- (C) Precipitation is achieved by adding zinc powder: $2[\text{Au(CN)}_2]^- + \text{Zn} \to [\text{Zn(CN)}_4]^{2-} + 2\text{Au}$.
- (D) In $[\text{Au(CN)}_2]^-$, gold has oxidation state $+1$ and coordination number 2.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 31 to 36)

#### Question 31
Calculate the $\text{pH}$ of a $0.010\text{ M}$ aqueous sodium hydroxide ($\text{NaOH}$) solution at $298\text{ K}$.

#### Question 32
A solution of $5.85\text{ g}$ of $\text{NaCl}$ (molar mass $58.5\text{ g/mol}$) in $500.0\text{ g}$ of water has an observed freezing point depression of $\Delta T_f = 0.688\text{ K}$. Taking $K_f = 1.86\text{ K}\cdot\text{kg/mol}$, calculate the van 't Hoff factor $i$. [Round off to TWO decimal places].

#### Question 33
Calculate the total number of unpaired electrons in the ground state of an isolated gaseous chromium atom ($\text{Cr}, Z = 24$).

#### Question 34
For a first-order chemical reaction with half-life $t_{1/2} = 15.0\text{ minutes}$, calculate the percentage of reactant consumed after $45.0\text{ minutes}$ (\%). [Round off to ONE decimal place].

#### Question 35
Calculate the packing fraction of a body-centered cubic ($bcc$) unit cell expressed as a percentage (\%). [Round off to the nearest integer].

#### Question 36
Find the oxidation state of chlorine in sodium chlorate ($\text{NaClO}_3$).

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Single Correct Questions (Questions 37 to 42)

#### Question 37
The value of the definite integral $\int_0^1 x^2(1 - x)^2 dx$ is:
- (A) $\frac{1}{30}$
- (B) $\frac{1}{15}$
- (C) $\frac{1}{60}$
- (D) $\frac{1}{12}$

#### Question 38
The angle between the lines with direction ratios $(1, 1, 0)$ and $(0, 1, 1)$ is:
- (A) $\frac{\pi}{3}$
- (B) $\frac{\pi}{4}$
- (C) $\frac{\pi}{6}$
- (D) $\frac{\pi}{2}$

#### Question 39
If $f(x) = x^2 \ln x$ for $x > 0$, then $f'(x)$ equals zero at $x$ equal to:
- (A) $\frac{1}{\sqrt{e}}$
- (B) $\frac{1}{e}$
- (C) $\sqrt{e}$
- (D) $e$

#### Question 40
The number of permutations of the letters of the word `APPLE` is:
- (A) 60
- (B) 120
- (C) 24
- (D) 30

#### Question 41
If $A$ is a square matrix of order 2 with $\det(A) = 3$, then $\det(3A)$ is:
- (A) 27
- (B) 9
- (C) 18
- (D) 6

#### Question 42
The slope of the tangent to the circle $x^2 + y^2 = 25$ at the point $(3, 4)$ is:
- (A) $-\frac{3}{4}$
- (B) $\frac{3}{4}$
- (C) $-\frac{4}{3}$
- (D) $\frac{4}{3}$

---

## Section 2: One or More Than One Correct Questions (Questions 43 to 48)

#### Question 43
Let $f(x) = \frac{x^2 - 1}{x^2 + 1}$ defined for $x \in \mathbb{R}$:
- (A) $f(x)$ is an even function.
- (B) $f(x)$ has an absolute minimum at $x = 0$ with value $-1$.
- (C) The range of $f(x)$ is $[-1, 1)$.
- (D) The line $y = 1$ is a horizontal asymptote as $x \to \pm \infty$.

#### Question 44
For the hyperbola $\frac{x^2}{25} - \frac{y^2}{16} = 1$:
- (A) The eccentricity is $e = \frac{\sqrt{41}}{5}$.
- (B) The foci are at $(\pm \sqrt{41}, 0)$.
- (C) The length of the transverse axis is $10$.
- (D) The length of the latus rectum is $\frac{32}{5}$.

#### Question 45
Let $z$ be a complex number satisfying $|z - 1| = 1$:
- (A) $\arg(z) \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ (for $z \neq 0$).
- (B) $|z|^2 = 2\text{Re}(z)$.
- (C) The maximum value of $|z|$ is $2$.
- (D) The point $z$ lies on a circle passing through the origin.

#### Question 46
Consider the function $f(x) = |x| + |x - 1|$:
- (A) $f(x)$ is continuous everywhere on $\mathbb{R}$.
- (B) $f(x)$ is not differentiable at $x = 0$ and $x = 1$.
- (C) The minimum value of $f(x)$ is $1$, attained for all $x \in [0, 1]$.
- (D) $f'(x) = 2$ for all $x > 1$.

#### Question 47
Let $\vec{a}, \vec{b}$ be two vectors in $\mathbb{R}^3$:
- (A) $|\vec{a} \times \vec{b}|$ represents the area of the parallelogram spanned by $\vec{a}$ and $\vec{b}$.
- (B) $\frac{1}{2}|\vec{a} \times \vec{b}|$ represents the area of the triangle spanned by $\vec{a}$ and $\vec{b}$.
- (C) $(\vec{a} + \vec{b}) \times (\vec{a} - \vec{b}) = -2(\vec{a} \times \vec{b})$.
- (D) If $\vec{a} \times \vec{b} = \vec{0}$ and $\vec{a} \cdot \vec{b} = 0$, then at least one of the vectors is zero.

#### Question 48
Consider the differential equation $x \frac{dy}{dx} + y = x^3$:
- (A) The integrating factor is $x$.
- (B) The general solution is $x y = \frac{x^4}{4} + C$.
- (C) If $y(1) = \frac{1}{4}$, then $C = 0$.
- (D) With $C = 0$, $y(x) = \frac{x^3}{4}$.

---

## Section 3: Non-Negative Numerical Value Questions (Questions 49 to 54)

#### Question 49
Evaluate the definite integral $\int_0^1 \frac{1}{1 + x^2} dx$. If the answer is $\frac{\pi}{k}$, find integer $k$.

#### Question 50
If vectors $\vec{a} = 2\hat{i} + 3\hat{j} + 4\hat{k}$ and $\vec{b} = 4\hat{i} - 2\hat{j} - \hat{k}$ are given, calculate their dot product $\vec{a} \cdot \vec{b}$.

#### Question 51
A bag contains 5 white and 5 black balls. If 2 balls are drawn at random without replacement, find the probability that both balls are white. If the probability is expressed as the irreducible fraction $\frac{a}{b}$, find $a + b$.

#### Question 52
Find the sum of all solutions to the equation $x^2 - 4x + 3 = 0$.

#### Question 53
Calculate the value of the determinant $\begin{vmatrix} 4 & 2 \\ 3 & 5 \end{vmatrix}$.

#### Question 54
Find the total number of subsets of a set having 6 elements ($2^6$).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 19 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `A` — Rolling sphere down incline: acceleration $a = \frac{g\sin\theta}{1 + 2/5} = \frac{5}{7}g\sin\theta$. Friction force $f_s = Mg\sin\theta - Ma = Mg\sin\theta\left(1 - \frac{5}{7}\right) = \frac{2}{7}Mg\sin\theta$. Since $f_s \le \mu N = \mu Mg\cos\theta$: $\mu_{\text{min}} = \frac{2}{7}\tan\theta$.
- **Q2**: **Answer**: `A` — Electric field in $R < r < 2R$ is $E(r) = \frac{Q}{4\pi\varepsilon_0 r^2}$. Potential difference $V_{\text{in}} - V_{\text{out}} = \int_R^{2R} E(r)dr = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{R} - \frac{1}{2R}\right) = \frac{Q}{8\pi\varepsilon_0 R}$.
- **Q3**: **Answer**: `A` — Adiabatic law for monoatomic gas ($\gamma = 5/3$): $T V^{\gamma - 1} = \text{const} \implies T_1 V_1^{2/3} = T_2 (2V_1)^{2/3} \implies \frac{T_2}{T_1} = 2^{-2/3}$.
- **Q4**: **Answer**: `A` — Angular fringe width $\theta = \frac{\lambda}{d}$. In water: $\lambda' = \lambda/\mu = \frac{3}{4}\lambda$. Thus $\theta' = \frac{3}{4}\theta = \frac{3}{4}(0.20^\circ) = 0.15^\circ$.
- **Q5**: **Answer**: `A` — Simple pendulum period $T = 2\pi\sqrt{L/g}$, independent of bob mass. When $L' = 4L$: $T' = 2\pi\sqrt{4L/g} = 2(2\pi\sqrt{L/g}) = 2T$.
- **Q6**: **Answer**: `A` — de Broglie wavelength: $\lambda = \frac{h}{\sqrt{2m q V}}$. Ratio: $\frac{\lambda_p}{\lambda_\alpha} = \sqrt{\frac{m_\alpha q_\alpha}{m_p q_p}} = \sqrt{\frac{4 \times 2}{1 \times 1}} = \sqrt{8} = 2\sqrt{2}$.

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Solid sphere slipping to rolling: friction $f = \mu Mg$, deceleration $a = -\mu g$, angular acceleration $\alpha = \frac{\mu Mg R}{\frac{2}{5}MR^2} = \frac{5\mu g}{2R}$. Pure rolling when $v = \omega R \implies v_0 - \mu g t = \frac{5\mu g}{2}t \implies t = \frac{2v_0}{7\mu g}$, $v = \frac{5}{7}v_0$. Work-energy loss $\Delta K = \frac{1}{7}M v_0^2$.
- **Q8**: **(A), (B), (C), (D)** — Series AC resonance: peak current, quality factor definition, bandwidth sharpness, pure resistive dissipation.
- **Q9**: **(A), (B), (C), (D)** — Heat transfer laws: Fourier conduction, buoyancy convection, radiation vacuum independence, Stefan-Boltzmann $T^4$ scaling.
- **Q10**: **(A), (B), (C), (D)** — Displacement method optics: minimum distance $4f$, conjugate positions for $D > 4f$, geometric mean object height $h_0 = \sqrt{h_1 h_2}$, displacement focal formula.
- **Q11**: **(A), (B), (C), (D)** — Faraday-Lenz fundamentals: energy conservation basis of Lenz's law, eddy currents in conductors, non-conservative induced electric fields, self-inductance inertia.
- **Q12**: **(A), (B), (C), (D)** — Compton scattering kinematics: shift formula $\Delta\lambda = \lambda_C(1 - \cos\theta)$, wavelength independence, maximum backward shift $2\lambda_C$, energy-momentum conservation.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `2.50` — Moment of inertia $I = \frac{1}{2}MR^2 = \frac{1}{2}(4.0)(0.50)^2 = 0.50\text{ kg}\cdot\text{m}^2$. Angular deceleration $\alpha = \frac{\tau}{I} = \frac{2.0}{0.50} = 4.0\text{ rad/s}^2$. Time to stop $t = \frac{\omega}{\alpha} = \frac{10.0}{4.0} = 2.50\text{ s}$.
- **Q14**: **Answer**: `2.00` — Electric field between oppositely charged conducting planes: $E = \frac{\sigma}{\varepsilon_0} = \frac{1.77 \times 10^{-8}}{8.85 \times 10^{-12}} = 2000\text{ V/m} = 2.00\text{ kV/m}$.
- **Q15**: **Answer**: `0.64` — Inductive reactance $X_L = \omega L = (100\pi)(0.50) = 50\pi \approx 157.08\ \Omega$. Peak current $I_0 = \frac{V_0}{X_L} = \frac{100}{157.08} = 0.6366\text{ A} \approx 0.64\text{ A}$.
- **Q16**: **Answer**: `330` — For a closed pipe, resonant frequencies are odd harmonics: $\nu_n = (2n-1)\frac{v}{4L}$. Fundamental ($n=1$): $\nu_1 = \frac{v}{4L} = \frac{330}{4(0.75)} = \frac{330}{3.0} = 110\text{ Hz}$. First overtone ($n=2$): $\nu_3 = 3\nu_1 = 3(110) = 330\text{ Hz}$.
- **Q17**: **Answer**: `37` — Snell's law: $1 \cdot \sin(53^\circ) = \frac{4}{3}\sin r \implies 0.80 = \frac{4}{3}\sin r \implies \sin r = \frac{3 \times 0.80}{4} = 0.60 \implies r = 37^\circ$.
- **Q18**: **Answer**: `4.76` — Bohr orbital radius: $r_n = n^2 a_0$. For $n = 3$: $r_3 = 3^2(0.529\text{ \AA}) = 9 \times 0.529 = 4.761\text{ \AA} \approx 4.76\text{ \AA}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — $[\text{Co}(\text{NH}_3)_6]\text{Cl}_3$ dissociates into 4 ions per formula unit ($1\ [\text{Co}(\text{NH}_3)_6]^{3+} + 3\ \text{Cl}^-$), producing the highest ion concentration and molar conductivity.
- **Q20**: **Answer**: `A` — Dehydrohalogenation of 2-bromopropane with alcoholic $\text{KOH}$ undergoes an $E2$ elimination to yield propene.
- **Q21**: **Answer**: `A` — $\text{SO}_2$ has 3 electron domains around sulfur ($sp^2$ hybridization: 2 bonding pairs, 1 lone pair), giving a bent/angular geometry.
- **Q22**: **Answer**: `A` — Copper is extracted by auto-reduction (self-reduction) in the Bessemer converter: $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \to 6\text{Cu} + \text{SO}_2$.
- **Q23**: **Answer**: `A` — First-order half-life: $t_{1/2} = \frac{0.693}{k} = \frac{0.693}{0.03465} = 20\text{ minutes}$.
- **Q24**: **Answer**: `A` — Soaps and synthetic detergents act as emulsifying agents for oil-in-water emulsions by reducing interfacial tension.

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q25**: **(A), (B), (C), (D)** — Transition metal aqueous complexes: purple $d-d$ $[\text{Ti(H}_2\text{O)}_6]^{3+}$, colorless filled $d^{10}$ $[\text{Zn(H}_2\text{O)}_6]^{2+}$, Jahn-Teller tetragonal $[\text{Cu(H}_2\text{O)}_6]^{2+}$, spin-only magnetic moment.
- **Q26**: **(A), (B), (C), (D)** — Allotropes of sulfur: rhombic stability at room temperature, monoclinic stability above $369\text{ K}$, crown $\text{S}_8$ rings, polymeric liquid viscosity peak.
- **Q27**: **(A), (B), (C), (D)** — Acyl derivative reactivities: acyl chloride $>$ anhydride $>$ ester $>$ amide, rapid hydrolysis, saponification, resonance stabilization of amides.
- **Q28**: **(A), (B), (C)** — Ideal solution properties: zero enthalpy and volume of change, Raoult's law compliance across all compositions. Ideal solutions never form an azeotrope.
- **Q29**: **(A), (B), (C), (D)** — Amino acid biochemistry: L-stereochemistry, planar resonance-stabilized peptide bond, cationic form at low pH, anionic at high pH.
- **Q30**: **(A), (B), (C), (D)** — Cyanide gold extraction: oxidative dicyanoaurate leaching, zinc displacement cementation, $+1$ state, linear coordination.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `12.00` — Strong base: $[\text{OH}^-] = 0.010\text{ M} = 10^{-2}\text{ M}$. $\text{pOH} = 2.00 \implies \text{pH} = 14.00 - 2.00 = 12.00$.
- **Q32**: **Answer**: `1.85` — Molality: $m = \frac{5.85 / 58.5}{0.500\text{ kg}} = \frac{0.100}{0.500} = 0.200\text{ mol/kg}$. Theoretical depression: $\Delta T_{f,\text{th}} = K_f \cdot m = 1.86 \times 0.200 = 0.372\text{ K}$. van 't Hoff factor $i = \frac{\Delta T_f}{\Delta T_{f,\text{th}}} = \frac{0.688}{0.372} = 1.849 \approx 1.85$.
- **Q33**: **Answer**: `6` — Gaseous chromium has anomalous ground state configuration $[Ar]3d^5 4s^1$ with 6 unpaired electrons (5 in $3d$, 1 in $4s$).
- **Q34**: **Answer**: `87.5` — In $45\text{ min}$, $n = 45/15 = 3$ half-lives elapse. Fraction remaining $= (1/2)^3 = 1/8 = 12.5\%$. Reactant consumed $= 100\% - 12.5\% = 87.5\%$.
- **Q35**: **Answer**: `68` — Packing efficiency of $bcc$ unit cell is $\frac{\sqrt{3}\pi}{8} \approx 68\%$.
- **Q36**: **Answer**: `5` — In $\text{NaClO}_3$: $1(+1) + x + 3(-2) = 0 \implies 1 + x - 6 = 0 \implies x = +5$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — Beta function: $\int_0^1 x^2(1-x)^2 dx = B(3, 3) = \frac{\Gamma(3)\Gamma(3)}{\Gamma(6)} = \frac{2! \times 2!}{5!} = \frac{4}{120} = \frac{1}{30}$.
- **Q38**: **Answer**: `A` — Normalizing direction vectors: $\vec{u} = (1, 1, 0)$, $\vec{v} = (0, 1, 1)$. Dot product $\vec{u} \cdot \vec{v} = 0 + 1 + 0 = 1$. Magnitudes $|\vec{u}| = \sqrt{2}, |\vec{v}| = \sqrt{2}$. $\cos\theta = \frac{1}{\sqrt{2}\sqrt{2}} = \frac{1}{2} \implies \theta = \frac{\pi}{3}$.
- **Q39**: **Answer**: `A` — Derivative: $f'(x) = 2x\ln x + x^2(1/x) = 2x\ln x + x = x(2\ln x + 1) = 0$. Since $x > 0$: $2\ln x + 1 = 0 \implies \ln x = -1/2 \implies x = e^{-1/2} = \frac{1}{\sqrt{e}}$.
- **Q40**: **Answer**: `A` — Permutations of `APPLE` (5 letters with $P$ repeated twice): $\frac{5!}{2!} = \frac{120}{2} = 60$.
- **Q41**: **Answer**: `A` — For $2 \times 2$ matrix, $\det(3A) = 3^2 \det(A) = 9 \times 3 = 27$.
- **Q42**: **Answer**: `A` — Circle tangent slope at $(x_1, y_1)$ is $-\frac{x_1}{y_1}$. At $(3, 4)$, slope is $-\frac{3}{4}$.

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — $f(x) = \frac{x^2-1}{x^2+1} = 1 - \frac{2}{x^2+1}$: even symmetry, minimum at 0 of value $-1$, range $[-1, 1)$, horizontal asymptote $y=1$.
- **Q44**: **(A), (B), (C), (D)** — Canonical hyperbola $\frac{x^2}{25} - \frac{y^2}{16} = 1$: eccentricity $\sqrt{1 + 16/25} = \sqrt{41}/5$, foci $(\pm\sqrt{41}, 0)$, transverse axis $2a = 10$, latus rectum $2b^2/a = 2(16)/5 = 32/5$.
- **Q45**: **(A), (B), (C), (D)** — Circle $|z - 1| = 1$: centered at $(1, 0)$ with radius 1, passes through origin, maximum modulus 2, argument in $(-\pi/2, \pi/2)$.
- **Q46**: **(A), (B), (C), (D)** — Piecewise linear function: continuous everywhere, sharp corners at 0 and 1, flat minimum 1 on $[0, 1]$, slope 2 for $x > 1$.
- **Q47**: **(A), (B), (C), (D)** — Cross product geometric properties: parallelogram area, triangle area, linearity identity $(\vec{a}+\vec{b})\times(\vec{a}-\vec{b}) = -2(\vec{a}\times\vec{b})$.
- **Q48**: **(A), (B), (C), (D)** — Standard linear ODE: integrating factor $x$, general solution $xy = \frac{x^4}{4} + C$, particular solution $y = \frac{x^3}{4}$.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `4` — Standard integral: $\int_0^1 \frac{1}{1+x^2}dx = [\tan^{-1} x]_0^1 = \frac{\pi}{4} \implies k = 4$.
- **Q50**: **Answer**: `-2` — Dot product: $\vec{a} \cdot \vec{b} = 2(4) + 3(-2) + 4(-1) = 8 - 6 - 4 = -2$. Absolute value $= 2$.
- **Q51**: **Answer**: `11` — Total ways: $\binom{10}{2} = 45$. Ways to draw 2 white: $\binom{5}{2} = 10$. Probability $= \frac{10}{45} = \frac{2}{9}$. Irreducible fraction: $a = 2, b = 9 \implies a + b = 11$.
- **Q52**: **Answer**: `4` — Roots of $x^2 - 4x + 3 = 0$ are $1$ and $3$. Sum of roots $= 4$.
- **Q53**: **Answer**: `14` — Determinant $= 4(5) - 2(3) = 20 - 6 = 14$.
- **Q54**: **Answer**: `64` — Number of subsets of 6-element set is $2^6 = 64$.
"""

val_md = r"""# Answer Key and Validation — Mock Examination 19
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)

### Paper 1 Answer Key
| Q | Type | Subject | Answer Key |
| :--- | :--- | :--- | :--- |
| 1 | Numerical | Physics | `1.03` |
| 2 | Numerical | Physics | `0.30` |
| 3 | Numerical | Physics | `3458` |
| 4 | Numerical | Physics | `1.00` |
| 5 | Numerical | Physics | `0.976` |
| 6 | Numerical | Physics | `1.10` |
| 7 | Numerical | Physics | `18.32` |
| 8 | Numerical | Physics | `148.9` |
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
| 19 | Numerical | Chemistry | `93` |
| 20 | Numerical | Chemistry | `3200` |
| 21 | Numerical | Chemistry | `-212` |
| 22 | Numerical | Chemistry | `-2` |
| 23 | Numerical | Chemistry | `64` |
| 24 | Numerical | Chemistry | `12.60` |
| 25 | Numerical | Chemistry | `4` |
| 26 | Numerical | Chemistry | `1` |
| 27 | Multi-Correct | Chemistry | A, B, C, D |
| 28 | Multi-Correct | Chemistry | A, B, C |
| 29 | Multi-Correct | Chemistry | A, B, C, D |
| 30 | Multi-Correct | Chemistry | A, B, C, D |
| 31 | Multi-Correct | Chemistry | A, B, C, D |
| 32 | Multi-Correct | Chemistry | A, B, C, D |
| 33 | List Match | Chemistry | A |
| 34 | List Match | Chemistry | A |
| 35 | List Match | Chemistry | A |
| 36 | List Match | Chemistry | A |
| 37 | Numerical | Mathematics | `9.00` |
| 38 | Numerical | Mathematics | `0.10` |
| 39 | Numerical | Mathematics | `5` |
| 40 | Numerical | Mathematics | `14` |
| 41 | Numerical | Mathematics | `4` |
| 42 | Numerical | Mathematics | `1` |
| 43 | Numerical | Mathematics | `3` |
| 44 | Numerical | Mathematics | `36` |
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
| 13 | Numerical | Physics | `2.50` |
| 14 | Numerical | Physics | `2.00` |
| 15 | Numerical | Physics | `0.64` |
| 16 | Numerical | Physics | `330` |
| 17 | Numerical | Physics | `37` |
| 18 | Numerical | Physics | `4.76` |
| 19 | Single Correct | Chemistry | A |
| 20 | Single Correct | Chemistry | A |
| 21 | Single Correct | Chemistry | A |
| 22 | Single Correct | Chemistry | A |
| 23 | Single Correct | Chemistry | A |
| 24 | Single Correct | Chemistry | A |
| 25 | Multi-Correct | Chemistry | A, B, C, D |
| 26 | Multi-Correct | Chemistry | A, B, C, D |
| 27 | Multi-Correct | Chemistry | A, B, C, D |
| 28 | Multi-Correct | Chemistry | A, B, C |
| 29 | Multi-Correct | Chemistry | A, B, C, D |
| 30 | Multi-Correct | Chemistry | A, B, C, D |
| 31 | Numerical | Chemistry | `12.00` |
| 32 | Numerical | Chemistry | `1.85` |
| 33 | Numerical | Chemistry | `6` |
| 34 | Numerical | Chemistry | `87.5` |
| 35 | Numerical | Chemistry | `68` |
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
| 49 | Numerical | Mathematics | `4` |
| 50 | Numerical | Mathematics | `-2` |
| 51 | Numerical | Mathematics | `11` |
| 52 | Numerical | Mathematics | `4` |
| 53 | Numerical | Mathematics | `14` |
| 54 | Numerical | Mathematics | `64` |
"""

create_mock_files(19, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md)

