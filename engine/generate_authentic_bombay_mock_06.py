# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 06 (Full Suite: P1, P2, Sol P1, Sol P2, Val).
"""
import os

mock_dir = os.path.join("mock_tests", "IIT_Bombay", "Mock_06")
os.makedirs(mock_dir, exist_ok=True)

paper_1_md = r"""# JEE Advanced Mock Examination 06 — Paper 1
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
A uniform semicircular thin wire of mass $M = 0.60\text{ kg}$ and radius $R = 0.40\text{ m}$ is freely hinged at one of its ends $P$ such that it can swing in a vertical plane. The wire is released from rest from a position where the line joining its ends is horizontal. When the line joining its ends becomes vertical, calculate the angular speed $\omega$ of the wire in $\text{rad/s}$. [Take $g = 9.80\text{ m/s}^2$ and $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 2
A vertical open cylindrical vessel of base radius $R = 0.20\text{ m}$ is filled with an ideal incompressible liquid of density $\rho = 1000\text{ kg/m}^3$ to a depth of $H = 1.00\text{ m}$. The container is rotated about its central vertical axis at a constant angular speed $\omega = 12.0\text{ rad/s}$. If a tiny circular hole of cross-sectional area $a = 1.0\text{ cm}^2$ is opened at the periphery of the bottom base, calculate the initial volume discharge rate of the liquid in $\text{liters/second}$ ($1\text{ L} = 10^{-3}\text{ m}^3$). [Take $g = 9.80\text{ m/s}^2$. Round off to TWO decimal places].

#### Question 3
Two moles of an ideal monoatomic gas undergo an adiabatic expansion such that its absolute temperature drops from $T_1 = 500\text{ K}$ to $T_2 = 300\text{ K}$. If the gas then undergoes an isobaric compression back to its initial volume, followed by an isochoric pressure rise back to initial state, calculate the total mechanical work done by the gas in the complete cycle in kiloJoules ($\text{kJ}$). [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to TWO decimal places].

#### Question 4
A long coaxial cable consists of an inner solid cylindrical conductor of radius $a = 2.0\text{ mm}$ carrying a uniformly distributed current $I = 10.0\text{ A}$ in the $+z$ direction, and an outer thin cylindrical shell of radius $b = 6.0\text{ mm}$ carrying the return current $I = 10.0\text{ A}$ in the $-z$ direction. Calculate the total magnetic energy stored per unit length of the cable in microJoules per meter ($\mu\text{J/m}$). [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$. Round off to TWO decimal places].

#### Question 5
In an interference experiment using Lloyd's mirror, a point source of light of wavelength $\lambda = 600\text{ nm}$ is placed at a distance $d = 1.50\text{ mm}$ above the horizontal plane of a flat glass mirror. The interference fringes are observed on a vertical screen placed at distance $D = 2.00\text{ m}$ from the source. Calculate the distance of the first bright fringe above the line of the mirror surface on the screen in millimeters ($\text{mm}$).

#### Question 6
A spherical capacitor consists of two concentric conducting spheres of radii $R_1 = 10.0\text{ cm}$ and $R_2 = 20.0\text{ cm}$. The intervening space is filled with two concentric layers of dielectric: from $r = R_1$ to $r = 15.0\text{ cm}$, the dielectric constant is $K_1 = 3.0$, and from $r = 15.0\text{ cm}$ to $r = R_2$, the dielectric constant is $K_2 = 6.0$. Determine the capacitance of the system in picoFarads ($\text{pF}$). [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$. Round off to TWO decimal places].

#### Question 7
A non-relativistic particle of mass $m$ and charge $q$ is projected into a region of crossed uniform fields: an electric field $\vec{E} = E_0 \hat{j}$ and a magnetic field $\vec{B} = B_0 \hat{k}$. The particle is released from rest at the origin $(0,0,0)$ at $t = 0$. If $E_0 = 1000\text{ V/m}$ and $B_0 = 0.50\text{ T}$, calculate the maximum speed $v_{\text{max}}$ attained by the particle in $\text{m/s}$.

#### Question 8
In a Coolidge X-ray tube operating at an accelerating voltage $V_0 = 40.0\text{ kV}$, electrons strike a target. The target emits $K_\alpha$ characteristic X-rays of wavelength $\lambda_{K_\alpha} = 0.154\text{ nm}$. If the cutoff minimum wavelength of continuous bremsstrahlung X-rays is $\lambda_{\text{min}}$, find the difference $(\lambda_{K_\alpha} - \lambda_{\text{min}})$ in picometers ($\text{pm}$). [Take $hc = 1240\text{ eV}\cdot\text{nm}$. Round off to ONE decimal place].

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal conveyor belt that is moving with a constant horizontal speed $u_0$ along the $+x$ direction. At $t = 0$, the sphere is placed gently on the belt with zero initial velocity ($v(0) = 0, \omega(0) = 0$). The coefficient of kinetic friction between the sphere and belt is $\mu_k$.
- (A) The sphere slips on the belt for a time duration $t_s = \frac{2u_0}{7\mu_k g}$.
- (B) At the instant slipping ceases, the linear speed of the center of mass of the sphere relative to the ground is $v_{\text{cm}} = \frac{2}{7}u_0$.
- (C) The total mechanical work done by friction on the sphere until slipping stops is positive and equal to $\frac{1}{7}M u_0^2$.
- (D) The total heat dissipated by friction between the sphere and the belt during the slipping phase is $Q = \frac{5}{14}M u_0^2$.

#### Question 10
In an $R-L-C$ series circuit driven by an alternating voltage source $v(t) = V_m \sin(\omega t)$, the parameters are $R = 100\ \Omega$, $L = 0.50\text{ H}$, and $C = 20.0\ \mu\text{F}$.
- (A) The resonant angular frequency of the circuit is $\omega_0 = 100\sqrt{10}\text{ rad/s} \approx 316.2\text{ rad/s}$.
- (B) The quality factor of the circuit at resonance is $Q = \frac{1}{R}\sqrt{\frac{L}{C}} \approx 1.58$.
- (C) At an operating frequency $\omega = 200\text{ rad/s}$, the circuit is capacitive and the current leads the source voltage.
- (D) At resonance, the peak voltage across the capacitor exceeds the peak voltage of the input source.

#### Question 11
An ideal gas with adiabatic index $\gamma = 1.40$ undergoes a process described by $P = \alpha V^2$, where $\alpha$ is a positive dimensional constant.
- (A) The molar heat capacity of the gas for this process is $C = C_V + \frac{R}{3} = \frac{17}{6}R$.
- (B) During expansion in this process, the temperature of the gas increases monotonically with volume as $T \propto V^3$.
- (C) The work done by the gas when expanding from volume $V_1$ to $2V_1$ is $W = \frac{7}{3}\alpha V_1^3$.
- (D) The ratio of the heat supplied to the gas to the work done by the gas is $\frac{\Delta Q}{W} = \frac{17}{6}$.

#### Question 12
A grounded conducting infinite plane coincides with the $xy$-plane ($z = 0$). A point charge $+q$ is held fixed at $(0, 0, d)$ where $d > 0$.
- (A) The electric potential at any point $(x, y, z)$ in the half-space $z > 0$ is identical to that produced by $+q$ at $(0, 0, d)$ and an image charge $-q$ at $(0, 0, -d)$.
- (B) The surface charge density induced on the conducting plane at distance $r = \sqrt{x^2 + y^2}$ from the origin is $\sigma(r) = -\frac{q d}{2\pi (r^2 + d^2)^{3/2}}$.
- (C) The total induced charge on the infinite conducting plane is $-q$.
- (D) The attractive force between the charge $+q$ and the conducting plane is $F = \frac{q^2}{16\pi\varepsilon_0 d^2}$.

#### Question 13
A horizontal Venturi tube has a main pipe diameter $D_1 = 0.15\text{ m}$ and a throat diameter $D_2 = 0.05\text{ m}$. Water ($\rho = 1000\text{ kg/m}^3$) flows through the tube. A mercury manometer connected between the inlet and throat shows a level difference $h = 0.10\text{ m}$. Take $\rho_{\text{Hg}} = 13600\text{ kg/m}^3$ and $g = 9.8\text{ m/s}^2$.
- (A) The static pressure at the throat is lower than that at the inlet.
- (B) The flow velocity at the throat is approximately 9 times the velocity at the inlet.
- (C) The volumetric discharge rate through the pipe is independent of the density of water.
- (D) If an air bubble enters the throat, it expands due to the lower static pressure.

#### Question 14
A parallel beam of unpolarized light of intensity $I_0$ passes through a sequence of three linear polarizers $P_1, P_2, P_3$. The transmission axis of $P_1$ is vertical ($\theta_1 = 0^\circ$), that of $P_3$ is horizontal ($\theta_3 = 90^\circ$), and the transmission axis of $P_2$ is oriented at angle $\theta$ with the vertical ($0 < \theta < 90^\circ$).
- (A) If polarizer $P_2$ is removed, the transmitted intensity through $P_3$ is zero.
- (B) With $P_2$ present, the transmitted intensity through $P_3$ is $I = \frac{I_0}{8}\sin^2(2\theta)$.
- (C) The transmitted intensity reaches its maximum value of $\frac{I_0}{8}$ when $\theta = 45^\circ$.
- (D) The light emerging from $P_2$ is linearly polarized at angle $\theta$ to the vertical with intensity $\frac{I_0}{2}\cos^2\theta$.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the physical thermodynamic cycles in **List-I** with their thermal efficiency expressions in **List-II** (all working substances are ideal gases with constant heat capacities):

| List-I | List-II |
| :--- | :--- |
| **P.** Carnot Cycle operating between $T_H$ and $T_C$ | **1.** $1 - \frac{T_C}{T_H}$ |
| **Q.** Otto Cycle with compression ratio $r = V_1/V_2$ | **2.** $1 - \frac{1}{r^{\gamma - 1}}$ |
| **R.** Brayton Cycle with pressure ratio $r_p = P_2/P_1$ | **3.** $1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}}$ |
| **S.** Stirling Cycle with ideal regenerator operating between $T_H$ and $T_C$ | **4.** $1 - \frac{T_C}{T_H}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the physical systems in **List-I** with their moment of inertia expressions in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Solid homogeneous sphere of mass $M$, radius $R$ about a tangent | **1.** $\frac{7}{5}M R^2$ |
| **Q.** Thin spherical shell of mass $M$, radius $R$ about a tangent | **2.** $\frac{5}{3}M R^2$ |
| **R.** Solid uniform cone of mass $M$, base radius $R$ about its central symmetry axis | **3.** $\frac{3}{10}M R^2$ |
| **S.** Thin uniform circular ring of mass $M$, radius $R$ about a tangential axis in its plane | **4.** $\frac{3}{2}M R^2$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2

#### Question 17
Match the nuclear decay processes in **List-I** with their physical characteristics in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Alpha ($\alpha$) decay | **1.** Discrete monoenergetic kinetic energy spectrum |
| **Q.** Beta-minus ($\beta^-$) decay | **2.** Continuous kinetic energy spectrum accompanied by antineutrino |
| **R.** Gamma ($\gamma$) emission | **3.** Nuclear de-excitation without change in atomic number $Z$ or mass number $A$ |
| **S.** Positron ($\beta^+$) emission | **4.** Accompanied by orbital electron capture as an alternative channel |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 18
Match the electromagnetic wave phenomena in **List-I** with their characteristic wave properties in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Total internal reflection | **1.** Occurs at interface from denser to rarer medium beyond critical angle |
| **Q.** Brewster's polarization | **2.** Reflected ray is completely linearly polarized perpendicular to plane of incidence |
| **R.** Chromatic dispersion | **3.** Phase velocity depends on frequency ($dn/d\lambda \neq 0$) |
| **S.** Optical activity | **4.** Rotation of plane of polarization due to circular birefringence |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
The solubility product of lead(II) iodate $\text{Pb(IO}_3)_2$ is $K_{\text{sp}} = 2.60 \times 10^{-13}$ at $298\text{ K}$. Calculate the molar solubility of $\text{Pb(IO}_3)_2$ in a $0.10\text{ M}$ aqueous solution of $\text{KIO}_3$ in units of $10^{-11}\text{ mol/L}$. (Round off to ONE decimal place).

#### Question 20
A coordination complex has the formula $\text{[Co(en)}_2(\text{NO}_2)\text{Cl]}^+$. Let $N_g$ be the number of geometrical isomers and let $N_o$ be the number of optically active isomers. Calculate the value of $(N_g \times N_o)$.

#### Question 21
The rate constant for a first-order chemical reaction increases by a factor of $4.0$ when the temperature is raised from $300\text{ K}$ to $320\text{ K}$. Determine the activation energy $E_a$ of the reaction in $\text{kJ/mol}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 4 = 1.386$. Round off to TWO decimal places].

#### Question 22
For the Daniel cell:
$$\text{Zn}(s) \mid \text{Zn}^{2+}(aq, 0.010\text{ M}) \parallel \text{Cu}^{2+}(aq, 1.00\text{ M}) \mid \text{Cu}(s)$$
Given standard reduction potentials $E^\circ_{\text{Zn}^{2+}/\text{Zn}} = -0.763\text{ V}$ and $E^\circ_{\text{Cu}^{2+}/\text{Cu}} = +0.340\text{ V}$. Calculate the cell electromotive force $E_{\text{cell}}$ at $298\text{ K}$ in Volts. [Take $\frac{2.303 RT}{F} = 0.0591\text{ V}$. Round off to THREE decimal places].

#### Question 23
Iron crystallizes at room temperature in a body-centered cubic ($bcc$) crystal structure with lattice parameter $a = 286.6\text{ pm}$. The atomic weight of iron is $55.85\text{ g/mol}$. Taking Avogadro's number $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$, calculate the theoretical density of iron in $\text{g/cm}^3$. (Round off to TWO decimal places).

#### Question 24
In qualitative inorganic analysis, a salt containing Group III cation $\text{Fe}^{3+}$ is treated with excess aqueous potassium ferrocyanide $\text{K}_4[\text{Fe(CN)}_6]$. A deep Prussian blue precipitate of $\text{Fe}_4[\text{Fe(CN)}_6]_3$ is formed. What is the total number of unpaired electrons per formula unit contributed by the high-spin iron centers in this Prussian blue complex?

#### Question 25
Find the total number of cyclic stereoisomers (including enantiomers and diastereomers) possible for 1,2-dimethylcyclopropane.

#### Question 26
For one mole of a van der Waals gas at its critical state, the critical volume is $V_c = 0.120\text{ L/mol}$ and the critical pressure is $P_c = 45.0\text{ atm}$. Calculate the value of the van der Waals parameter $b$ in $\text{L/mol}$. (Round off to THREE decimal places).

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding the molecular orbitals and magnetic behaviors of homonuclear diatomic molecules:
- (A) $\text{O}_2^-$ (superoxide ion) has a bond order of $1.5$ and is paramagnetic with one unpaired electron.
- (B) In $\text{N}_2$, the Highest Occupied Molecular Orbital ($\text{HOMO}$) is $\sigma_{2p_z}$, whereas in $\text{O}_2$ it is $\pi^*_{2p}$.
- (C) The bond dissociation energy of $\text{N}_2^+$ is lower than that of neutral $\text{N}_2$.
- (D) $\text{Ne}_2$ does not exist as a stable chemical species because its bond order is zero.

#### Question 28
An organic compound $A$ ($\text{C}_8\text{H}_{10}\text{O}$) gives a positive iodoform test and undergoes dehydration with concentrated $\text{H}_2\text{SO}_4$ to form alkene $B$. Alkene $B$ on reductive ozonolysis ($\text{O}_3, \text{Zn/H}_2\text{O}$) yields benzaldehyde and formaldehyde.
- (A) Compound $A$ is 1-phenylethanol.
- (B) Compound $B$ is styrene (phenylethene).
- (C) Compound $A$ can be resolved into two optically active enantiomers.
- (D) Reaction of compound $B$ with $\text{HBr}$ in the presence of benzoyl peroxide gives 1-bromo-2-phenylethane as the major product.

#### Question 29
Consider the high-spin octahedral complex $[\text{Cr(H}_2\text{O)}_6]^{3+}$ and the low-spin octahedral complex $[\text{Co(NH}_3)_6]^{3+}$:
- (A) $[\text{Cr(H}_2\text{O)}_6]^{3+}$ has three unpaired electrons with magnetic moment $\mu \approx 3.87\text{ BM}$.
- (B) $[\text{Co(NH}_3)_6]^{3+}$ is diamagnetic with $t_{2g}^6 e_g^0$ electronic configuration.
- (C) The Crystal Field Stabilization Energy ($\text{CFSE}$) of $[\text{Cr(H}_2\text{O)}_6]^{3+}$ is $-1.2\Delta_o$.
- (D) Both complexes undergo rapid associative ligand exchange kinetics and are thermodynamically unstable.

#### Question 30
In the metallurgical extraction of copper from copper pyrites ($\text{CuFeS}_2$):
- (A) Smelting is carried out in a blast furnace where silica ($\text{SiO}_2$) is added as an acidic flux to remove $\text{FeO}$ as fusible slag $\text{FeSiO}_3$.
- (B) The molten matte obtained consists primarily of $\text{Cu}_2\text{S}$ and $\text{FeS}$.
- (C) In the Bessemer converter, auto-reduction occurs via $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \to 6\text{Cu} + \text{SO}_2$.
- (D) The solidified metal is known as blister copper due to the evolution of escaping $\text{SO}_2$ gas bubbles.

#### Question 31
For a non-ideal liquid mixture of chloroform and acetone:
- (A) It shows negative deviation from Raoult's law due to intermolecular hydrogen bonding between chloroform and acetone.
- (B) $\Delta H_{\text{mixing}} < 0$ (exothermic mixing) and $\Delta V_{\text{mixing}} < 0$ (volume contraction).
- (C) The mixture forms a maximum-boiling azeotrope at a specific composition.
- (D) The vapor pressure of the solution is higher than that predicted by Raoult's law.

#### Question 32
Which of the following reaction sequences correctly produce a carboxylic acid?
- (A) Alkaline hydrolysis of an alkyl nitrile ($R-\text{CN}$) followed by acidification.
- (B) Reaction of a Grignard reagent ($R\text{MgBr}$) with solid dry ice ($\text{CO}_2$) followed by aqueous acid workup.
- (C) Vigorous oxidation of an alkylbenzene with alkaline $\text{KMnO}_4$ followed by acidification, provided the benzylic carbon has at least one hydrogen.
- (D) Hydrolysis of an acyl chloride ($R\text{COCl}$) with water.

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the coordination complexes in **List-I** with their total number of stereoisomers in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $[\text{Pt(NH}_3)_2\text{Cl}_2]$ | **1.** $2$ (cis, trans) |
| **Q.** $[\text{Co(en)}_2\text{Cl}_2]^+$ | **2.** $3$ (trans-meso, cis-enantiomeric pair) |
| **R.** $[\text{Co(en)}_3]^{3+}$ | **3.** $2$ (enantiomeric pair: $\Delta, \Lambda$) |
| **S.** $[\text{Pt(NH}_3)(\text{py})(\text{Cl})(\text{Br})]$ | **4.** $3$ (three planar geometrical isomers) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the polymer types in **List-I** with their commercial polymer examples in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Polyamide condensation polymer | **1.** Nylon-6,6 |
| **Q.** Polyester condensation polymer | **2.** Dacron (Terylene) |
| **R.** Thermosetting cross-linked polymer | **3.** Bakelite (phenol-formaldehyde) |
| **S.** Elastomer addition copolymer | **4.** Buna-S (SBR) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 35
Match the organic reagents in **List-I** with their specific selective transformations in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Lindlar's catalyst ($\text{Pd/CaCO}_3 + \text{quinoline} + \text{H}_2$) | **1.** Alkyne $\to$ cis-alkene |
| **Q.** Birch reduction ($\text{Na} / \text{liquid NH}_3$) | **2.** Alkyne $\to$ trans-alkene |
| **R.** PCC (Pyridinium chlorochromate) | **3.** Primary alcohol $\to$ Aldehyde |
| **S.** DIBAL-H at $-78^\circ\text{C}$ followed by $\text{H}_2\text{O}$ | **4.** Ester / Nitrile $\to$ Aldehyde |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4

#### Question 36
Match the phosphorus compounds in **List-I** with their structural traits in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** White phosphorus ($\text{P}_4$) | **1.** Discrete tetrahedral molecules with bond angle $60^\circ$ |
| **Q.** Red phosphorus | **2.** Polymeric chains of $\text{P}_4$ tetrahedra linked covalently |
| **R.** Phosphorus pentachloride in solid state | **3.** Ionic lattice: $[\text{PCl}}_4]^+ [\text{PCl}}_6]^-$ |
| **S.** Phosphorus tribromide in solid state | **4.** Ionic lattice: $[\text{PBr}}_4]^+ \text{Br}^-$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Let $f(x)$ be a differentiable function on $\mathbb{R}$ satisfying $f'(x) = 2 f(x) + 4$ with $f(0) = 1$. Evaluate $\lim_{x \to 0} \frac{f(x) - e^{2x}}{x^2}$. (Round off to TWO decimal places).

#### Question 38
Evaluate the value of the definite integral:
$$I = \int_{0}^{\pi} \frac{x \sin^3 x}{1 + \cos^2 x}\,dx$$
If $I = \pi \left(\frac{\pi}{a} - b\right)$, where $a$ and $b$ are positive integers, find the value of $(a + b)$.

#### Question 39
Let $A$ be a $3 \times 3$ invertible real matrix such that $A^3 - 4A^2 + 5A - 2I = 0$. If $\det(A) = 2$ and $\text{Tr}(A) = 4$, determine the trace of $A^{-1}$. (Round off to TWO decimal places).

#### Question 40
A fair six-faced die is tossed repeatedly until a $6$ appears. Let $X$ be the number of tosses required. Calculate the conditional expectation $E[X \mid X > 2]$.

#### Question 41
Find the area enclosed between the parabola $y = x^2 - 4x + 3$ and the straight line $y = x - 1$ in square units. (Round off to TWO decimal places).

#### Question 42
Let $z$ be a complex number satisfying $|z - 2 - 2i| \le 1$. Find the minimum value of $|z - 5 - 6i|$.

#### Question 43
Let $\vec{a} = 2\hat{i} - \hat{j} + \hat{k}$, $\vec{b} = \hat{i} + 2\hat{j} - \hat{k}$, and $\vec{c} = \hat{i} + \hat{j} - 2\hat{k}$. A vector $\vec{d}$ is coplanar with $\vec{a}$ and $\vec{b}$ and its projection on $\vec{c}$ is $\frac{1}{\sqrt{6}}$. If $\vec{d} \cdot \vec{a} = 7$, find $|\vec{d}|^2$.

#### Question 44
Find the total number of four-digit numbers formed using the digits $\{0, 1, 2, 3, 4, 5\}$ without repetition that are divisible by $6$.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Let $f(x) = \frac{\ln x}{x}$ defined on $(0, \infty)$.
- (A) $f(x)$ is strictly increasing in $(0, e)$ and strictly decreasing in $(e, \infty)$.
- (B) $f(x)$ attains an absolute maximum at $x = e$ with maximum value $\frac{1}{e}$.
- (C) $e^\pi > \pi^e$.
- (D) The graph of $f(x)$ has an inflection point at $x = e^{3/2}$.

#### Question 46
Consider the parabola $y^2 = 4ax$ ($a > 0$). Let $P(at_1^2, 2at_1)$ and $Q(at_2^2, 2at_2)$ be the endpoints of a focal chord passing through the focus $S(a, 0)$.
- (A) $t_1 t_2 = -1$.
- (B) The tangents drawn at points $P$ and $Q$ intersect at right angles on the directrix $x = -a$.
- (C) The circle described on focal chord $PQ$ as diameter touches the directrix.
- (D) The length of the focal chord is $L = a\left(t_1 - \frac{1}{t_1}\right)^2$.

#### Question 47
Let $M$ be a $3 \times 3$ skew-symmetric real matrix ($M^T = -M$).
- (A) $\det(M) = 0$.
- (B) All eigenvalues of $M$ are purely imaginary or zero.
- (C) The matrix $(I + M)$ is invertible for any real skew-symmetric matrix $M$.
- (D) The matrix $(I - M)(I + M)^{-1}$ is an orthogonal matrix (Cayley transform).

#### Question 48
Let $I_n = \int_{0}^{1} x^n e^{-x}\,dx$ for non-negative integers $n$.
- (A) $I_n = n I_{n-1} - \frac{1}{e}$ for $n \ge 1$.
- (B) $I_0 = 1 - \frac{1}{e}$.
- (C) $\lim_{n \to \infty} I_n = 0$.
- (D) $\lim_{n \to \infty} n I_n = \frac{1}{e}$.

#### Question 49
Let $A$ and $B$ be two independent events with probabilities $P(A) = 0.40$ and $P(B) = 0.50$.
- (A) The probability that at least one of the events occurs is $P(A \cup B) = 0.70$.
- (B) The probability that exactly one of the events occurs is $0.50$.
- (C) $P(A \mid A \cup B) = \frac{4}{7}$.
- (D) $P(A \cap B') = 0.20$.

#### Question 50
Consider the differential equation $(x^2 + y^2)dx - 2xy\,dy = 0$.
- (A) The equation is homogeneous of degree 2.
- (B) The substitution $y = vx$ transforms the equation into a separable variable form.
- (C) The general solution represents a family of circles passing through the origin with centers on the $x$-axis: $x^2 - y^2 = C x$.
- (D) The orthogonal trajectories of this family of curves are circles passing through the origin with centers on the $y$-axis.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the differential equations in **List-I** with their general solution types in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\frac{dy}{dx} = \frac{y}{x} + \tan\left(\frac{y}{x}\right)$ | **1.** $\sin(y/x) = C x$ |
| **Q.** $\frac{dy}{dx} + \frac{y}{x} = x^2$ | **2.** $y = \frac{x^3}{4} + \frac{C}{x}$ |
| **R.** $y\,dx - x\,dy + \ln x\,dx = 0$ | **3.** $\frac{y}{x} = \frac{\ln x + 1}{x} + C$ |
| **S.** $\frac{dy}{dx} + 2x y = 2x$ | **4.** $y = 1 + C e^{-x^2}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the limits in **List-I** with their values in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\lim_{x \to 0} \frac{\sin x - x}{x^3}$ | **1.** $-\frac{1}{6}$ |
| **Q.** $\lim_{x \to 0} \frac{e^x - e^{-x} - 2x}{x^3}$ | **2.** $\frac{1}{3}$ |
| **R.** $\lim_{x \to 0} \frac{\ln(1+x) - x}{x^2}$ | **3.** $-\frac{1}{2}$ |
| **S.** $\lim_{x \to 0} \left(\frac{1}{x} - \frac{1}{\sin x}\right)$ | **4.** $0$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4

#### Question 53
Match the conic section equations in **List-I** with their eccentricities $e$ in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $x^2 + 2y^2 = 2$ | **1.** $\frac{1}{\sqrt{2}}$ |
| **Q.** $x^2 - y^2 = 4$ | **2.** $\sqrt{2}$ |
| **R.** $y^2 = 4x$ | **3.** $1$ |
| **S.** $3x^2 + 4y^2 = 12$ | **4.** $\frac{1}{2}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 54
Match the plane geometric configurations in **List-I** with their angles in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Angle between asymptotes of rectangular hyperbola $x^2 - y^2 = a^2$ | **1.** $90^\circ$ |
| **Q.** Angle between lines represented by $x^2 - 3y^2 = 0$ | **2.** $60^\circ$ |
| **R.** Angle between diagonals of a square | **3.** $90^\circ$ |
| **S.** Acute angle between planes $x + y = 0$ and $y + z = 0$ | **4.** $60^\circ$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4
"""

with open(os.path.join(mock_dir, "Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(paper_1_md)

print("Mock 06 Paper 1 written successfully.")

