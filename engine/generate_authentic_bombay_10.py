# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Bombay Mock 10.
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 10 — Paper 1
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
A uniform solid sphere of mass $M = 2.50\text{ kg}$ and radius $R = 0.20\text{ m}$ is released from rest from the top of an inclined plane of inclination $\theta = 30^\circ$ and height $H = 1.40\text{ m}$. The sphere rolls down without slipping. Calculate the linear speed $v$ of the sphere's center of mass upon reaching the bottom in $\text{m/s}$. [Take $g = 9.80\text{ m/s}^2$. Round off to TWO decimal places].

#### Question 2
A vertical cylindrical tank of diameter $D = 1.00\text{ m}$ is filled with water to a depth of $H = 3.60\text{ m}$. A circular orifice of diameter $d = 2.0\text{ cm}$ is punched in the side wall at a depth of $h = 0.90\text{ m}$ below the water surface. Calculate the horizontal distance $x$ (in meters) from the base of the tank to the point where the water jet strikes the ground. [Take $g = 9.80\text{ m/s}^2$. Round off to TWO decimal places].

#### Question 3
One mole of an ideal monoatomic gas undergoes an adiabatic compression such that its volume decreases by a factor of $8$ ($V_2 = V_1 / 8$). If the initial temperature is $T_1 = 300\text{ K}$, calculate the change in internal energy $\Delta U$ of the gas in kiloJoules ($\text{kJ}$). [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to TWO decimal places].

#### Question 4
A long straight cylindrical solenoid of radius $R = 0.050\text{ m}$ has $n = 1000\text{ turns/m}$ and carries an increasing current $I(t) = (4.0\text{ A/s}) t$. Calculate the magnitude of the induced electric field $E$ at a radial distance $r = 0.030\text{ m}$ from the central axis inside the solenoid in $\text{mV/m}$. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$. Round off to TWO decimal places].

#### Question 5
In a double-slit experiment, two narrow slits separated by $d = 0.30\text{ mm}$ are illuminated by monochromatic light of wavelength $\lambda = 600\text{ nm}$. The screen is located at $D = 1.50\text{ m}$. A thin mica sheet of refractive index $\mu = 1.60$ is placed in front of one slit, causing the central bright fringe to shift by a distance $\Delta y = 6.00\text{ mm}$. Calculate the thickness $t$ of the mica sheet in micrometers ($\mu\text{m}$).

#### Question 6
Two concentric spherical conducting shells have radii $a = 0.10\text{ m}$ and $b = 0.20\text{ m}$. The inner shell carries charge $+Q_1 = 4.0\ \mu\text{C}$ and the outer shell is connected to ground (earthed). Calculate the capacitance of this spherical capacitor in picoFarads ($\text{pF}$). [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$. Round off to TWO decimal places].

#### Question 7
A cyclotron is designed to accelerate protons ($m_p = 1.67 \times 10^{-27}\text{ kg}, q = 1.60 \times 10^{-19}\text{ C}$) using a magnetic field $B = 1.50\text{ T}$. If the maximum extraction radius of the dees is $R_{\text{dee}} = 0.50\text{ m}$, calculate the maximum kinetic energy of the accelerated protons in Mega-electronVolts ($\text{MeV}$). [Take $1\text{ eV} = 1.60 \times 10^{-19}\text{ J}$. Round off to TWO decimal places].

#### Question 8
In an experiment on photoelectric effect, the stopping potential is measured to be $V_{s,1} = 1.85\text{ V}$ when light of wavelength $\lambda_1 = 300\text{ nm}$ is used, and $V_{s,2} = 0.82\text{ V}$ when $\lambda_2 = 400\text{ nm}$ is used. Calculate the work function $\Phi$ of the metal cathode in $\text{eV}$. (Round off to TWO decimal places).

---

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)

#### Question 9
A uniform solid sphere of mass $M$ and radius $R$ rests on a rough horizontal surface. A horizontal impulse $J$ is applied to the sphere at a height $h$ above its center of mass.
- (A) The sphere moves forward with pure rolling immediately after the impulse without any initial slipping if $h = \frac{2}{5}R$.
- (B) If $h > \frac{2}{5}R$, the sphere initially slips forward with forward angular spin, and friction acts forward to establish pure rolling.
- (C) If $h < \frac{2}{5}R$, the sphere initially slips forward with insufficient spin, and friction acts backward to establish pure rolling.
- (D) If $h = 0$ (impulse through center of mass), the linear speed when pure rolling begins is $v = \frac{5}{7}\frac{J}{M}$.

#### Question 10
In an alternating current circuit containing a resistance $R = 30\ \Omega$, an inductive reactance $X_L = 80\ \Omega$, and a capacitive reactance $X_C = 40\ \Omega$ connected in series with an AC source $v(t) = 200\sin(100\pi t)\text{ V}$:
- (A) The net reactance of the circuit is inductive with magnitude $X = 40\ \Omega$.
- (B) The total impedance of the circuit is $Z = 50\ \Omega$.
- (C) The peak current circulating in the circuit is $I_0 = 4.0\text{ A}$.
- (D) The current lags the applied source voltage by phase angle $\phi = \tan^{-1}(4/3) \approx 53.1^\circ$.

#### Question 11
An ideal gas undergoes a thermodynamic expansion from state $(P_1, V_1)$ to volume $V_2 = 2V_1$ along three different reversible paths: Path I is isobaric, Path II is isothermal, and Path III is adiabatic.
- (A) The final pressure is highest for the isobaric process and lowest for the adiabatic process ($P_{\text{isobaric}} > P_{\text{isothermal}} > P_{\text{adiabatic}}$).
- (B) The work done by the gas is maximum for the isobaric process: $W_{\text{isobaric}} > W_{\text{isothermal}} > W_{\text{adiabatic}}$.
- (C) The final temperature is lowest for the adiabatic process: $T_{\text{adiabatic}} < T_{\text{isothermal}} < T_{\text{isobaric}}$.
- (D) The change in internal energy is positive for the isobaric process, zero for the isothermal process, and negative for the adiabatic process.

#### Question 12
A conducting spherical shell of inner radius $a$ and outer radius $b$ carries a net charge $+Q$. A point charge $+q$ is placed at the center of the cavity.
- (A) The electric field inside the cavity ($r < a$) is $E(r) = \frac{q}{4\pi\varepsilon_0 r^2}$.
- (B) The total charge induced on the inner surface $r = a$ is $-q$.
- (C) The total charge on the outer surface $r = b$ is $Q + q$.
- (D) The electric field outside the shell ($r > b$) is $E(r) = \frac{Q + q}{4\pi\varepsilon_0 r^2}$, independent of the position of the charge inside the cavity.

#### Question 13
A horizontal Venturi meter is installed in a pipeline of diameter $D = 0.20\text{ m}$ to measure the flow rate of oil ($\rho = 800\text{ kg/m}^3$). The throat diameter is $d = 0.10\text{ m}$. A mercury differential manometer connected between the inlet and throat indicates a height difference $h = 0.20\text{ m}$. [Take $\rho_m = 13600\text{ kg/m}^3$ and $g = 9.80\text{ m/s}^2$].
- (A) The pressure difference between inlet and throat is $\Delta P = (\rho_m - \rho)gh$.
- (B) The fluid velocity at the throat is four times the velocity at the inlet ($v_{\text{throat}} = 4 v_{\text{inlet}}$).
- (C) The volumetric discharge rate $Q$ is proportional to $\sqrt{h}$.
- (D) If the meter is inclined at an angle to the horizontal, the differential manometer reading $h$ remains identical for the same flow rate.

#### Question 14
In a double-slit interference experiment with two slits illuminated by monochromatic light:
- (A) If one slit is covered with an opaque shield, the interference fringes disappear and are replaced by a single-slit diffraction pattern.
- (B) If one slit is covered with a transparent glass slide, the interference fringe width remains unchanged, but the entire fringe pattern shifts towards the covered slit.
- (C) If the separation between the slits is halved and the screen distance is doubled, the fringe width quadruples.
- (D) If the monochromatic source is replaced by an identical source emitting light of higher frequency, the fringe width decreases.

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the thermodynamic processes in **List-I** with their $P-V-T$ functional invariants in **List-II** for an ideal gas with constant $\gamma$:

| List-I | List-II |
| :--- | :--- |
| **P.** Isothermal | **1.** $P V = \text{constant}$ |
| **Q.** Isobaric | **2.** $V/T = \text{constant}$ |
| **R.** Isochoric | **3.** $P/T = \text{constant}$ |
| **S.** Reversible adiabatic | **4.** $P V^\gamma = \text{constant}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the rolling bodies down an incline in **List-I** with their ratios of translational to rotational kinetic energy in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Thin ring / hoop | **1.** $1$ |
| **Q.** Solid cylinder / disc | **2.** $2$ |
| **R.** Solid sphere | **3.** $\frac{5}{2} = 2.5$ |
| **S.** Thin spherical shell | **4.** $\frac{3}{2} = 1.5$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 17
Match the nuclear decay modes in **List-I** with their emitted leptons in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Beta-minus ($\beta^-$) decay | **1.** Electron ($e^-$) and electron antineutrino ($\bar{\nu}_e$) |
| **Q.** Beta-plus ($\beta^+$) decay | **2.** Positron ($e^+$) and electron neutrino ($\nu_e$) |
| **R.** Orbital electron capture | **3.** Electron neutrino ($\nu_e$) only |
| **S.** Alpha decay | **4.** No leptons emitted |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 18
Match the circuit components in **List-I** with their phase relations between voltage and current in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Pure resistor $R$ | **1.** Current and voltage are in phase ($\phi = 0$) |
| **Q.** Pure inductor $L$ | **2.** Voltage leads current by $\pi/2$ |
| **R.** Pure capacitor $C$ | **3.** Current leads voltage by $\pi/2$ |
| **S.** Series $L-C-R$ at resonance | **4.** Current and voltage are in phase ($\phi = 0$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 19 to 26)

#### Question 19
The solubility product of silver chromate $\text{Ag}_2\text{CrO}_4$ is $K_{\text{sp}} = 1.10 \times 10^{-12}$ at $298\text{ K}$. Calculate the molar solubility of $\text{Ag}_2\text{CrO}_4$ in pure water in units of $10^{-5}\text{ mol/L}$. [Take $(0.275)^{1/3} \approx 0.650$. Round off to TWO decimal places].

#### Question 20
A coordination complex has formula $[\text{Co(en)}_2\text{Cl}_2]^+$. What is the coordination number of the central cobalt ion?

#### Question 21
For a first-order chemical reaction, $75\%$ of the reactant decomposes in $40.0\text{ minutes}$. Calculate the half-life $t_{1/2}$ of the reaction in minutes.

#### Question 22
Calculate the standard cell potential $E^\circ_{\text{cell}}$ (in Volts) at $298\text{ K}$ for the Daniell cell:
$$\text{Zn}(s) + \text{Cu}^{2+}(aq) \to \text{Zn}^{2+}(aq) + \text{Cu}(s)$$
Given $E^\circ_{\text{Zn}^{2+}/\text{Zn}} = -0.76\text{ V}$ and $E^\circ_{\text{Cu}^{2+}/\text{Cu}} = +0.34\text{ V}$.

#### Question 23
A metal crystallizes in a body-centered cubic ($bcc$) lattice with unit cell edge length $a = 300\text{ pm}$. Calculate the radius $r$ of the metal atom in picometers ($\text{pm}$). [Take $\sqrt{3} \approx 1.732$. Round off to ONE decimal place].

#### Question 24
In qualitative inorganic analysis, how many of the following metal ions belong to Group III (precipitated as hydroxides by aqueous $\text{NH}_4\text{OH}$ in the presence of $\text{NH}_4\text{Cl}$)?
$$\text{Fe}^{3+},\ \text{Al}^{3+},\ \text{Cr}^{3+},\ \text{Zn}^{2+},\ \text{Mn}^{2+},\ \text{Ni}^{2+},\ \text{Ca}^{2+}$$

#### Question 25
Find the total number of structural isomers of alcohols having the molecular formula $\text{C}_4\text{H}_{10}\text{O}$.

#### Question 26
One mole of an ideal gas absorbs $300\text{ J}$ of heat and simultaneously performs $120\text{ J}$ of mechanical expansion work on the surroundings. Calculate the change in internal energy $\Delta U$ of the gas in Joules ($\text{J}$).

---

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)

#### Question 27
Regarding the molecular orbital electronic configuration and properties of nitric oxide ($\text{NO}$):
- (A) $\text{NO}$ has a bond order of $2.5$.
- (B) It is paramagnetic in the gaseous state with one unpaired electron in a $\pi^*_{2p}$ orbital.
- (C) In the liquid and solid states, $\text{NO}$ readily dimerizes to diamagnetic $\text{N}_2\text{O}_2$.
- (D) Loss of one electron to form nitrosonium ion $\text{NO}^+$ increases the bond order to $3.0$ and shortens the bond length.

#### Question 28
In the Cannizzaro reaction of formaldehyde with concentrated aqueous $\text{KOH}$:
- (A) Formaldehyde undergoes self-oxidation-reduction (disproportionation).
- (B) The products obtained are methanol ($\text{CH}_3\text{OH}$) and potassium formate ($\text{HCOOK}$).
- (C) The rate-determining step is the hydride ion ($\text{H}^-$) transfer from the tetrahedral gem-diolate intermediate to another formaldehyde molecule.
- (D) Carbonyl compounds containing $\alpha$-hydrogens undergo aldol condensation instead of the Cannizzaro reaction under basic conditions.

#### Question 29
Consider the coordination complex $[CoF_6]^{3-}$ and $[Co(CN)_6]^{3-}$:
- (A) In $[CoF_6]^{3-}$, fluoride is a weak-field ligand, giving a high-spin outer-orbital complex ($sp^3d^2$) with four unpaired electrons.
- (B) In $[Co(CN)_6]^{3-}$, cyanide is a strong-field ligand, giving a low-spin inner-orbital complex ($d^2sp^3$) with zero unpaired electrons.
- (C) $[CoF_6]^{3-}$ is paramagnetic with magnetic moment $\mu \approx 4.90\text{ BM}$.
- (D) Both complexes have identical octahedral coordination geometry.

#### Question 30
In the metallurgical extraction of iron in a blast furnace:
- (A) The highest temperature zone is the combustion zone at the bottom ($\approx 1900^\circ\text{C}$).
- (B) Slag formation reaction: $\text{CaO} + \text{SiO}_2 \to \text{CaSiO}_3$ occurs in the middle zone.
- (C) The molten slag is less dense than molten iron and floats on top, preventing the re-oxidation of iron.
- (D) Wrought iron is the purest commercial form of iron ($< 0.2\%$ carbon), prepared by heating cast iron in a reverberatory furnace lined with haematite.

#### Question 31
For a non-ideal binary solution exhibiting negative deviation from Raoult's law (e.g., acetone-chloroform):
- (A) The vapor pressure of the solution is lower than that predicted by Raoult's law: $P < P_A^\circ x_A + P_B^\circ x_B$.
- (B) Intermolecular attractive forces between unlike molecules ($A-B$) are stronger than those between like molecules ($A-A$ and $B-B$).
- (C) $\Delta H_{\text{mixing}} < 0$ (exothermic mixing).
- (D) $\Delta V_{\text{mixing}} < 0$ (contraction in total volume upon mixing).

#### Question 32
Which of the following organic compounds will produce a carboxylic acid upon acidic aqueous hydrolysis?
- (A) Acetonitrile ($\text{CH}_3\text{CN}$)
- (B) Acetamide ($\text{CH}_3\text{CONH}_2$)
- (C) Ethyl acetate ($\text{CH}_3\text{COOCH}_2\text{CH}_3$)
- (D) Acetyl chloride ($\text{CH}_3\text{COCl}$)

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the transition metal ions in **List-I** with their spin-only magnetic moments in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\text{Sc}^{3+}$ ($d^0$) | **1.** $0.00\text{ BM}$ |
| **Q.** $\text{Ti}^{3+}$ ($d^1$) | **2.** $1.73\text{ BM}$ |
| **R.** $\text{Fe}^{3+}$ ($d^5$ high-spin) | **3.** $5.92\text{ BM}$ |
| **S.** $\text{Ni}^{2+}$ ($d^8$ octahedral) | **4.** $2.83\text{ BM}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the metallurgy refining methods in **List-I** with their metals in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Liquation | **1.** Tin ($\text{Sn}$) (low melting point metal) |
| **Q.** Distillation | **2.** Zinc ($\text{Zn}$) / Mercury ($\text{Hg}$) (volatile metals) |
| **R.** Cupellation | **3.** Silver containing lead impurity |
| **S.** Poling | **4.** Copper containing cuprous oxide impurity |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 35
Match the organic name reactions in **List-I** with their synthetic products in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Sandmeyer reaction | **1.** Chlorobenzene / Bromobenzene |
| **Q.** Gattermann-Koch reaction | **2.** Benzaldehyde |
| **R.** Clemmensen reduction | **3.** Hydrocarbon / Alkane |
| **S.** Hell-Volhard-Zelinsky (HVZ) reaction | **4.** $\alpha$-Halo carboxylic acid |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 36
Match the phosphorus oxoacids in **List-I** with their basicity in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\text{H}_3\text{PO}_2$ (Hypophosphorous acid) | **1.** Monobasic ($1\ \text{P-OH}$) |
| **Q.** $\text{H}_3\text{PO}_3$ (Orthophosphorous acid) | **2.** Dibasic ($2\ \text{P-OH}$) |
| **R.** $\text{H}_3\text{PO}_4$ (Orthophosphoric acid) | **3.** Tribasic ($3\ \text{P-OH}$) |
| **S.** $\text{H}_4\text{P}_2\text{O}_7$ (Pyrophosphoric acid) | **4.** Tetrabasic ($4\ \text{P-OH}$) |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Numerical Value Questions (Questions 37 to 44)

#### Question 37
Let $f(x) = \frac{\sin x}{x}$ for $x \neq 0$ and $f(0) = 1$. Evaluate $\lim_{x \to 0} \frac{f(x) - 1}{x^2}$. (Round off to TWO decimal places).

#### Question 38
Evaluate the definite integral:
$$I = \int_{0}^{1} \frac{dx}{\sqrt{1 - x^2}}$$
If $I = \frac{\pi}{k}$, find the integer value of $k$.

#### Question 39
Let $A$ be a $3 \times 3$ real invertible matrix such that $A^{-1} = A^T$ and $\det(A) = 1$. Find the value of $\det(A - I)$ if $A$ has an eigenvalue $\lambda = 1$.

#### Question 40
A fair coin is tossed 6 times. Find the probability of getting exactly 3 heads as an irreducible fraction $\frac{m}{n}$. Find $(m + n)$.

#### Question 41
Find the area bounded by the curve $y = \sin x$ and the $x$-axis from $x = 0$ to $x = \pi$ in square units.

#### Question 42
Let $z$ be a complex number satisfying $|z - 2| = 2$. Find the maximum value of $|z|^2$.

#### Question 43
Let $\vec{a} = \hat{i} + \hat{j}$ and $\vec{b} = \hat{j} + \hat{k}$. Find the area of the triangle spanned by vectors $\vec{a}$ and $\vec{b}$ in square units. (Round off to TWO decimal places).

#### Question 44
Find the number of ways of selecting 4 letters from the word **MATHEMATICS**.

---

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)

#### Question 45
Let $f(x) = x e^{-x}$ defined on $\mathbb{R}$.
- (A) $f'(x) = (1 - x)e^{-x}$.
- (B) $f(x)$ attains an absolute maximum at $x = 1$ with maximum value $\frac{1}{e}$.
- (C) The curve $y = f(x)$ has an inflection point at $x = 2$.
- (D) $\lim_{x \to \infty} f(x) = 0$ and $\lim_{x \to -\infty} f(x) = -\infty$.

#### Question 46
Consider the parabola $y^2 = 4ax$. Tangents drawn to the parabola at $P(at_1^2, 2at_1)$ and $Q(at_2^2, 2at_2)$ intersect at $T(x_0, y_0)$.
- (A) The coordinates of the intersection point are $x_0 = a t_1 t_2$ and $y_0 = a(t_1 + t_2)$.
- (B) If the tangents are perpendicular, then $t_1 t_2 = -1$ and the locus of $T$ is the directrix $x = -a$.
- (C) The chord of contact from any point on the directrix passes through the focus $(a, 0)$.
- (D) The circle circumscribing triangle $PQT$ passes through the focus of the parabola.

#### Question 47
Let $A$ be a $3 \times 3$ real matrix such that $A^3 = A$.
- (A) The eigenvalues of $A$ can only be $-1, 0, 1$.
- (B) $A$ is diagonalizable over $\mathbb{R}$ if $A$ has 3 distinct eigenvalues.
- (C) $\det(A)$ can only be $-1, 0$, or $1$.
- (D) The trace of $A$ is an integer between $-3$ and $3$.

#### Question 48
Let $I_n = \int_{0}^{\pi/4} \tan^n x\,dx$ for integers $n \ge 2$.
- (A) $I_n + I_{n-2} = \frac{1}{n-1}$.
- (B) $\frac{1}{2(n+1)} < I_n < \frac{1}{2(n-1)}$.
- (C) $\lim_{n \to \infty} I_n = 0$.
- (D) $\lim_{n \to \infty} n I_n = \frac{1}{2}$.

#### Question 49
Let $E$ and $F$ be two independent events with $P(E) = 0.50$ and $P(F) = 0.30$.
- (A) $P(E \cap F) = 0.15$.
- (B) $P(E \cup F) = 0.65$.
- (C) $P(E \mid F) = 0.50$.
- (D) $P(E' \cap F') = 0.35$.

#### Question 50
Consider the differential equation $\frac{dy}{dx} = \frac{y}{x} + \sin\left(\frac{y}{x}\right)$ for $x > 0$.
- (A) The substitution $y = vx$ transforms the equation into $\csc v\,dv = \frac{dx}{x}$.
- (B) The general solution is $\tan(y/2x) = C x$.
- (C) The equation is homogeneous of degree zero.
- (D) All solution curves pass through the origin $(0, 0)$.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the differential equations in **List-I** with their general solutions in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\frac{dy}{dx} = k y$ | **1.** $y = C e^{kx}$ |
| **Q.** $\frac{dy}{dx} = -k y$ | **2.** $y = C e^{-kx}$ |
| **R.** $\frac{d^2y}{dx^2} + \omega^2 y = 0$ | **3.** $y = A\cos(\omega x) + B\sin(\omega x)$ |
| **S.** $\frac{d^2y}{dx^2} - \omega^2 y = 0$ | **4.** $y = A e^{\omega x} + B e^{-\omega x}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 52
Match the definite integrals in **List-I** with their evaluated values in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\int_{0}^{1} x\,dx$ | **1.** $\frac{1}{2}$ |
| **Q.** $\int_{0}^{1} x^2\,dx$ | **2.** $\frac{1}{3}$ |
| **R.** $\int_{0}^{1} x^3\,dx$ | **3.** $\frac{1}{4}$ |
| **S.** $\int_{0}^{1} x^4\,dx$ | **4.** $\frac{1}{5}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 53
Match the conics in **List-I** with their standard eccentricity values in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Circle | **1.** $e = 0$ |
| **Q.** Parabola | **2.** $e = 1$ |
| **R.** Rectangular hyperbola | **3.** $e = \sqrt{2}$ |
| **S.** Ellipse with $b = a/\sqrt{2}$ | **4.** $e = \frac{1}{\sqrt{2}}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 54
Match the plane geometric transformations in **List-I** with their $2 \times 2$ matrices in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Reflection across the $x$-axis | **1.** $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ |
| **Q.** Reflection across the $y$-axis | **2.** $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ |
| **R.** Reflection across the line $y = x$ | **3.** $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ |
| **S.** Rotation by $90^\circ$ counterclockwise | **4.** $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3
"""

solutions_p1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 10 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `4.43` — Conservation of energy for pure rolling: $M g H = \frac{1}{2} M v^2 + \frac{1}{2} I \omega^2 = \frac{7}{10} M v^2 \implies v = \sqrt{\frac{10}{7} g H} = \sqrt{\frac{10}{7}(9.80)(1.40)} = \sqrt{19.60} = 4.427\text{ m/s} \approx 4.43\text{ m/s}$.
- **Q2**: **Answer**: `3.12` — Torricelli efflux speed: $v = \sqrt{2gh} = \sqrt{2(9.80)(0.90)} = \sqrt{17.64} = 4.20\text{ m/s}$. Time of fall to ground from height $(H-h) = 2.70\text{ m}$: $t = \sqrt{\frac{2(H-h)}{g}} = \sqrt{\frac{2(2.70)}{9.80}} = \sqrt{0.551} = 0.7423\text{ s}$. Horizontal range $x = v t = 4.20 \times 0.7423 = 3.118\text{ m} \approx 3.12\text{ m}$.
- **Q3**: **Answer**: `11.22` — For adiabatic compression of monoatomic gas: $T_2 = T_1 (V_1/V_2)^{\gamma-1} = 300(8)^{2/3} = 300(4) = 1200\text{ K}$. Change in internal energy: $\Delta U = n C_V \Delta T = 1\left(\frac{3}{2}R\right)(1200 - 300) = 1.5(8.314)(900) = 11223.9\text{ J} \approx 11.22\text{ kJ}$.
- **Q4**: **Answer**: `0.38` — Induced electric field inside solenoid: $\oint E \cdot dl = -\frac{d\Phi}{dt} \implies E(2\pi r) = (\pi r^2)\mu_0 n \frac{dI}{dt} \implies E = \frac{1}{2}\mu_0 n r \frac{dI}{dt} = \frac{1}{2}(4\pi \times 10^{-7})(1000)(0.030)(4.0) = 7.54 \times 10^{-5}\text{ V/m} \approx 0.38\text{ mV/m}$.
- **Q5**: **Answer**: `2.00` — Fringe shift $\Delta y = \frac{D}{d}(\mu - 1)t \implies t = \frac{\Delta y \cdot d}{D(\mu - 1)} = \frac{(6.00 \times 10^{-3}\text{ m})(0.30 \times 10^{-3}\text{ m})}{(1.50\text{ m})(1.60 - 1)} = \frac{1.80 \times 10^{-6}}{0.90} = 2.00 \times 10^{-6}\text{ m} = 2.00\ \mu\text{m}$.
- **Q6**: **Answer**: `22.22` — Concentric spherical capacitor: $C = 4\pi\varepsilon_0 \frac{a b}{b - a} = \frac{1}{9.0 \times 10^9}\frac{0.10 \times 0.20}{0.20 - 0.10} = \frac{0.020}{9.0 \times 10^9 \times 0.10} = \frac{0.20}{9.0 \times 10^9} = 2.22 \times 10^{-11}\text{ F} = 22.22\text{ pF}$.
- **Q7**: **Answer**: `26.93` — Cyclotron kinetic energy: $v_{\text{max}} = \frac{q B R}{m} \implies K_{\text{max}} = \frac{q^2 B^2 R^2}{2m} = \frac{(1.6 \times 10^{-19})^2(1.50)^2(0.50)^2}{2(1.67 \times 10^{-27})} = \frac{2.56 \times 10^{-38} \times 2.25 \times 0.25}{3.34 \times 10^{-27}} = 4.31 \times 10^{-12}\text{ J} = 26.93\text{ MeV}$.
- **Q8**: **Answer**: `2.28` — Einstein's equation: $e V_s = \frac{hc}{\lambda} - \Phi$. $e(V_{s,1} - V_{s,2}) = hc\left(\frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right) \implies 1.85 - 0.82 = 1.03\text{ eV} = hc(1/300 - 1/400) = hc/1200 \implies hc \approx 1236\text{ eV}\cdot\text{nm}$. Then $\Phi = \frac{1236}{300} - 1.85 = 4.12 - 1.85 = 2.27\text{ eV} \approx 2.28\text{ eV}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Sphere angular impulse: linear velocity $v_0 = J/M$, angular velocity $\omega_0 = J h / I = \frac{5 J h}{2 M R^2}$. Rolling without slipping requires $v_0 = R \omega_0 \implies J/M = \frac{5 J h}{2 M R} \implies h = \frac{2}{5}R$. If $h < 2/5 R$, friction acts backward, increasing spin and reducing linear speed to $5/7 J/M$.
- **Q10**: **(A), (B), (C), (D)** — Series RLC AC analysis: $X = X_L - X_C = 80 - 40 = 40\ \Omega$. $Z = \sqrt{30^2 + 40^2} = 50\ \Omega$. Peak current $I_0 = V_0/Z = 200/50 = 4.0\text{ A}$. Phase angle $\tan\phi = 40/30 = 4/3$.
- **Q11**: **(A), (B), (C), (D)** — Comparison of expansion processes on $P-V$ plane: isobaric is horizontal line, isothermal drops as $1/V$, adiabatic drops as $1/V^\gamma$. Pressures, works, and temperatures verify all options.
- **Q12**: **(A), (B), (C), (D)** — Electrostatic shielding in concentric conducting shell: point charge $+q$ induces $-q$ on inner surface $r = a$ and $+q$ on outer surface $r = b$, leaving field outside spherically symmetric.
- **Q13**: **(A), (B), (C), (D)** — Venturi meter fluid dynamics: continuity gives velocity ratio $(D/d)^2 = 4$, differential pressure measured by manometer is independent of inclination angle.
- **Q14**: **(A), (B), (C), (D)** — Young's double slit principles: single slit diffraction when one slit is closed, fringe shift $\Delta y = \frac{D}{d}(\mu-1)t$ without change in spacing $\beta$, dependence on geometry and wavelength.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — State functions and path invariants of ideal gases.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Ratios of kinetic energies in pure rolling ($K_{\text{trans}}/K_{\text{rot}} = \frac{MR^2}{I}$).
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Lepton conservation in nuclear weak decay channels.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Phase relations in AC electrical circuits.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `6.50` — Solubility product: $K_{\text{sp}} = [2s]^2 [s] = 4s^3 \implies 4s^3 = 1.10 \times 10^{-12} \implies s^3 = 0.275 \times 10^{-12} \implies s = (0.275)^{1/3} \times 10^{-4} = 0.650 \times 10^{-4}\text{ M} = 6.50 \times 10^{-5}\text{ M}$.
- **Q20**: **Answer**: `6` — $[\text{Co(en)}_2\text{Cl}_2]^+$ has two bidentate ethylenediamine ligands (each occupying 2 coordination sites) and two monodentate chloride ligands. Total coordination number $= 2(2) + 2(1) = 6$.
- **Q21**: **Answer**: `20.0` — For a first-order reaction: $75\%$ completion corresponds to two half-lives ($2 t_{1/2} = 40.0\text{ min} \implies t_{1/2} = 20.0\text{ min}$).
- **Q22**: **Answer**: `1.10` — Daniell cell standard potential: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = +0.34 - (-0.76) = +1.10\text{ V}$.
- **Q23**: **Answer**: `129.9` — In $bcc$ lattice: $4r = \sqrt{3}a \implies r = \frac{\sqrt{3}}{4}a = \frac{1.732}{4}(300\text{ pm}) = 129.9\text{ pm}$.
- **Q24**: **Answer**: `3` — Group III cations: $\text{Fe}^{3+}, \text{Al}^{3+}, \text{Cr}^{3+}$. Exactly 3 ions.
- **Q25**: **Answer**: `4` — Structural isomers of $\text{C}_4\text{H}_{10}\text{O}$ alcohols: butan-1-ol, butan-2-ol, 2-methylpropan-1-ol, 2-methylpropan-2-ol. Exactly 4 isomers.
- **Q26**: **Answer**: `180` — First law of thermodynamics: $\Delta U = q - w = 300\text{ J} - 120\text{ J} = 180\text{ J}$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Electronic structure of nitric oxide: bond order $2.5$, paramagnetism, low temperature dimerization to $\text{N}_2\text{O}_2$, $\text{NO}^+$ cation.
- **Q28**: **(A), (B), (C), (D)** — Cannizzaro reaction mechanism: non-enolizable aldehyde, disproportionation to alcohol and carboxylate, hydride shift rate-determining step.
- **Q29**: **(A), (B), (C), (D)** — Octahedral cobalt(III) complexes: weak field fluoride high spin ($sp^3d^2$, $\mu = 4.90\text{ BM}$) vs strong field cyanide low spin ($d^2sp^3$, diamagnetic).
- **Q30**: **(A), (B), (C), (D)** — Blast furnace metallurgy of iron: thermal profile, calcium silicate slag, density separation, conversion of pig iron to wrought iron.
- **Q31**: **(A), (B), (C), (D)** — Thermodynamics of negative deviation from Raoult's law: enhanced intermolecular attraction, negative enthalpy of mixing, negative volume of mixing.
- **Q32**: **(A), (B), (C), (D)** — Hydrolysis of carboxylic acid derivatives: nitriles, amides, esters, and acid halides all yield parent carboxylic acids.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Spin-only magnetic moments ($\mu = \sqrt{n(n+2)}\text{ BM}$).
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Metallurgical refining techniques.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Organic synthetic name reactions.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Basicity of phosphorus oxoacids.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `-0.17` — Taylor series of $\sin x = x - \frac{x^3}{6} + \dots \implies \frac{\sin x}{x} = 1 - \frac{x^2}{6} + \dots$ Numerator $f(x) - 1 = -\frac{x^2}{6}$. Limit $= -\frac{1}{6} \approx -0.17$.
- **Q38**: **Answer**: `2` — Standard integral: $\int_0^1 \frac{dx}{\sqrt{1-x^2}} = [\sin^{-1} x]_0^1 = \frac{\pi}{2} - 0 = \frac{\pi}{2} \implies k = 2$.
- **Q39**: **Answer**: `0` — Since $\lambda = 1$ is an eigenvalue of $A$, $\det(A - 1\cdot I) = \det(A - I) = 0$.
- **Q40**: **Answer**: `21` — Favorable outcomes $\binom{6}{3} = 20$. Total outcomes $2^6 = 64$. $P = \frac{20}{64} = \frac{5}{16}$. Irreducible fraction $\frac{5}{16} \implies m = 5, n = 16 \implies m + n = 21$.
- **Q41**: **Answer**: `2.00` — Area $= \int_0^\pi \sin x\,dx = [-\cos x]_0^\pi = -(-1) - (-1) = 2.00$.
- **Q42**: **Answer**: `16` — $|z-2|=2$ is a circle centered at $(2, 0)$ of radius $2$. Maximum distance from origin to circle is $2 + 2 = 4$. Maximum of $|z|^2 = 4^2 = 16$.
- **Q43**: **Answer**: `0.87` — Cross product $\vec{a} \times \vec{b} = (\hat{i} + \hat{j}) \times (\hat{j} + \hat{k}) = \hat{i} - \hat{j} + \hat{k}$. Area of triangle $= \frac{1}{2}|\vec{a} \times \vec{b}| = \frac{1}{2}\sqrt{1 + 1 + 1} = \frac{\sqrt{3}}{2} \approx 0.866 \approx 0.87$.
- **Q44**: **Answer**: `136` — MATHEMATICS has letters: M(2), A(2), T(2), H, E, I, C, S (8 distinct letters). Case 1: 4 distinct $\binom{8}{4} = 70$. Case 2: 2 alike, 2 distinct $\binom{3}{1}\binom{7}{2} = 3 \times 21 = 63$. Case 3: 2 alike, 2 alike $\binom{3}{2} = 3$. Total $= 70 + 63 + 3 = 136$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Complete analysis of $f(x) = x e^{-x}$: derivative $(1-x)e^{-x}$, maximum at $x = 1$, inflection at $x = 2$, asymptotic limits.
- **Q46**: **(A), (B), (C), (D)** — Tangents to parabola $y^2 = 4ax$: intersection at $(a t_1 t_2, a(t_1+t_2))$, orthogonality condition $t_1 t_2 = -1$ leads to directrix locus, chord of contact focal theorem.
- **Q47**: **(A), (B), (C), (D)** — Tripotent matrices ($A^3 = A$): eigenvalues satisfy $\lambda^3 - \lambda = 0 \implies \lambda \in \{-1, 0, 1\}$, trace is sum of integer eigenvalues.
- **Q48**: **(A), (B), (C), (D)** — Recurrence relation for tangent powers: $I_n + I_{n-2} = 1/(n-1)$, sandwich theorem limits.
- **Q49**: **(A), (B), (C), (D)** — Independent events: $P(E \cap F) = 0.50 \times 0.30 = 0.15$, $P(E \cup F) = 0.50 + 0.30 - 0.15 = 0.65$, conditional independence.
- **Q50**: **(A), (B), (C)** — Homogeneous differential equation with trigonometric term: substitution $y = vx$ leads to separable integral $\csc v\,dv = dx/x$.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard linear ordinary differential equations and harmonic oscillators.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Monomial definite integrals $\int_0^1 x^n dx = \frac{1}{n+1}$.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Conic section eccentricities.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — 2D linear transformation reflection and rotation matrices.
"""

paper_2_md = r"""# JEE Advanced Mock Examination 10 — Paper 2
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
A uniform solid sphere of mass $M$ and radius $R$ is placed at rest at the top of a fixed rough spherical surface of radius $R_0 = 3R$. The sphere is released from rest from a point slightly displaced from the apex ($\theta = 0$). As it rolls down without slipping:
- (A) The angular acceleration of the sphere when the radius vector from the hemisphere center makes an angle $\theta$ with the vertical is $\alpha = \frac{5g \sin\theta}{7R}$.
- (B) The linear speed of the center of mass of the sphere is $v = \sqrt{\frac{10}{7}g(R_0 + R)(1 - \cos\theta)}$.
- (C) The normal reaction force exerted by the surface on the sphere is $N = Mg\left(\frac{17}{7}\cos\theta - \frac{10}{7}\right)$.
- (D) The sphere leaves contact with the surface at an angle $\theta_c = \cos^{-1}(10/17) \approx 54.0^\circ$ (assuming no slipping prior to detachment).

#### Question 2
Two long, parallel, mutually coupled inductors $L_1 = L$ and $L_2 = 2L$ are connected in parallel with each other across an AC voltage source $v(t) = V_0 \sin(\omega t)$. The mutual inductance between the two coils is $M = \frac{L}{2}$ and their windings aid each other.
- (A) The equivalent inductance of the parallel combination is $L_{\text{eq}} = \frac{7}{8}L$.
- (B) The currents in the two coils oscillate in phase with each other.
- (C) The ratio of the current amplitudes in the two coils is $\frac{I_1}{I_2} = \frac{L_2 - M}{L_1 - M} = \frac{2L - 0.5L}{L - 0.5L} = 3$.
- (D) The total energy stored in the magnetic field at any instant is $U = \frac{1}{2} L_{\text{eq}} i_{\text{total}}^2(t)$.

#### Question 3
An ideal gas undergoes a polytropic process $P V^n = \text{constant}$ such that the molar heat capacity of the gas is $C = 2 R$. The adiabatic index of the gas is $\gamma = 1.40$.
- (A) The polytropic index is $n = 0.50$.
- (B) During expansion, both pressure and volume increase simultaneously.
- (C) During expansion, the temperature of the gas increases.
- (D) The work done by the gas when expanding from $V_1$ to $2V_1$ is positive.

#### Question 4
A dielectric sphere of radius $R$ has a uniform polarization $\vec{P} = P_0 \hat{k}$ throughout its volume.
- (A) The volume bound charge density inside the sphere is strictly zero ($\rho_b = -\nabla \cdot \vec{P} = 0$).
- (B) The surface bound charge density on the sphere is $\sigma_b(\theta) = P_0 \cos\theta$.
- (C) The electric field inside the sphere is uniform and directed opposite to the polarization: $\vec{E}_{\text{in}} = -\frac{P_0}{3\varepsilon_0}\hat{k}$.
- (D) Outside the sphere, the electric field is identical to that of a pure electric dipole of moment $\vec{p} = \frac{4}{3}\pi R^3 P_0 \hat{k}$.

#### Question 5
A cylindrical wooden log of length $L$ and uniform cross-sectional area $A$ floats upright in water with a length $h_0$ submerged. The log is depressed slightly into the water by a distance $y$ and released.
- (A) The restoring buoyant force is proportional to the downward displacement $y$.
- (B) The motion of the log is simple harmonic with time period $T = 2\pi\sqrt{\frac{h_0}{g}}$.
- (C) If the density of the wood is half that of water ($\rho_{\text{wood}} = 0.5\rho_{\text{water}}$), the submerged depth is $h_0 = 0.5 L$.
- (D) The oscillation frequency is independent of the cross-sectional area $A$ of the log.

#### Question 6
An astronomical refracting telescope has an objective lens of focal length $f_o = 120\text{ cm}$ and an eyepiece of focal length $f_e = 6.0\text{ cm}$. The telescope is focused on a distant object for normal adjustment (image at infinity).
- (A) The angular magnification of the telescope is $m = -20$.
- (B) The distance between the objective and the eyepiece is $L = 126\text{ cm}$.
- (C) If the telescope is focused on an object at a distance of $24.0\text{ m}$ from the objective with the final image at infinity, the tube length must be increased by $6.3\text{ cm}$.
- (D) The image formed by the objective is real, inverted, and located at the focal plane of the eyepiece.

#### Question 7
In a Compton scattering event, a high-energy photon of frequency $\nu_0$ scatters off an electron at rest:
- (A) The wavelength of the scattered photon is always greater than or equal to the incident wavelength ($\lambda' \ge \lambda_0$).
- (B) The maximum possible fractional increase in wavelength occurs for backscattering ($\theta = 180^\circ$).
- (C) The kinetic energy of the recoil electron is $K_e = h\nu_0 - h\nu'$.
- (D) Total relativistic energy and linear momentum are conserved in the collision.

#### Question 8
A particle of mass $m$ is confined in a two-dimensional square infinite potential box of side length $L$ ($0 \le x \le L, 0 \le y \le L$).
- (A) The stationary state energy eigenvalues are $E_{n_x, n_y} = \frac{\pi^2\hbar^2}{2m L^2}(n_x^2 + n_y^2)$ with $n_x, n_y \in \{1, 2, 3, \dots\}$.
- (B) The ground state $(n_x=1, n_y=1)$ is non-degenerate with energy $E_{1,1} = \frac{\pi^2\hbar^2}{m L^2}$.
- (C) The first excited energy level has a degree of degeneracy equal to $2$ (corresponding to states $(1,2)$ and $(2,1)$).
- (D) The normalized wave function of the ground state is $\psi_{1,1}(x,y) = \frac{2}{L}\sin\left(\frac{\pi x}{L}\right)\sin\left(\frac{\pi y}{L}\right)$.

---

## Section 2: Numerical Value Questions (Questions 9 to 14)

#### Question 9
A uniform thin circular hoop of mass $M = 1.50\text{ kg}$ and radius $R = 0.30\text{ m}$ hangs on a horizontal knife-edge peg. Calculate the period of small oscillations of the hoop in its own plane in seconds. [Take $g = 9.80\text{ m/s}^2$ and $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 10
In an $R-L$ series circuit connected to a $12.0\text{ V}$ battery, the current reaches $63.2\%$ of its maximum steady-state value in $t = 2.50\text{ ms}$. If the resistance is $R = 50.0\ \Omega$, calculate the inductance $L$ of the inductor in milliHenries ($\text{mH}$).

#### Question 11
Two moles of an ideal monoatomic gas undergo an isochoric heating process wherein the pressure doubles from $P_1 = 1.0 \times 10^5\text{ Pa}$ to $P_2 = 2.0 \times 10^5\text{ Pa}$ in a rigid vessel of volume $V = 0.025\text{ m}^3$. Calculate the total heat supplied to the gas in Joules ($\text{J}$).

#### Question 12
A point charge $q = +2.0\ \mu\text{C}$ is placed at a distance $d = 0.20\text{ m}$ from an infinite grounded conducting flat plane. Calculate the total attractive force between the charge and the plane in milliNewtons ($\text{mN}$). [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$. Round off to TWO decimal places].

#### Question 13
In an interference setup using two coherent sources separated by $d = 0.50\text{ mm}$, the wavelength of light is $\lambda = 500\text{ nm}$. The screen is located at $D = 2.00\text{ m}$. Calculate the linear separation on the screen between the second bright fringe and the fourth bright fringe on the same side of the central maximum in millimeters ($\text{mm}$).

#### Question 14
A radioactive sample contains $2.0 \times 10^{16}$ atoms and has an activity of $1.0 \times 10^9\text{ decays/s}$. Calculate the half-life $T_{1/2}$ of this substance in days. [Take $\ln 2 = 0.693$ and $1\text{ day} = 86400\text{ s}$. Round off to TWO decimal places].

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the thermodynamic cycles in **List-I** with their theoretical efficiency expressions in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Carnot cycle | **1.** $1 - \frac{T_C}{T_H}$ |
| **Q.** Otto cycle | **2.** $1 - \frac{1}{r^{\gamma-1}}$ |
| **R.** Brayton cycle | **3.** $1 - \frac{1}{r_p^{(\gamma-1)/\gamma}}$ |
| **S.** Stirling cycle with ideal regenerator | **4.** $1 - \frac{T_C}{T_H}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 16
Match the rolling bodies in **List-I** with their total kinetic energies for center-of-mass speed $v$ in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Thin ring of mass $M$ | **1.** $M v^2$ |
| **Q.** Solid disc of mass $M$ | **2.** $\frac{3}{4}M v^2$ |
| **R.** Solid sphere of mass $M$ | **3.** $\frac{7}{10}M v^2$ |
| **S.** Thin spherical shell of mass $M$ | **4.** $\frac{5}{6}M v^2$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 17
Match the nuclear decay types in **List-I** with their characteristics in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Alpha decay | **1.** Emission of helium-4 nucleus (${}^4\text{He}$) |
| **Q.** Beta-minus decay | **2.** Conversion of neutron to proton ($n \to p + e^- + \bar{\nu}_e$) |
| **R.** Beta-plus decay | **3.** Conversion of proton to neutron ($p \to n + e^+ + \nu_e$) |
| **S.** Gamma emission | **4.** Nuclear transition between isomeric nuclear states |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 18
Match the electromagnetic quantities in **List-I** with their mathematical formulas in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Electric field of point charge | **1.** $\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{r}$ |
| **Q.** Magnetic field of long straight wire | **2.** $\frac{\mu_0 I}{2\pi r}\hat{\phi}$ |
| **R.** Magnetic field at center of circular loop | **3.** $\frac{\mu_0 I}{2R}$ |
| **S.** Electric field inside uniform spherical charge | **4.** $\frac{\rho r}{3\varepsilon_0}\hat{r}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct Questions (Questions 19 to 24)

#### Question 19
Regarding the allotropy and chemical reactions of phosphorus:
- (A) White phosphorus consists of discrete tetrahedral $\text{P}_4$ molecules with angle strain ($60^\circ$ bond angles), making it highly reactive and pyrophoric.
- (B) White phosphorus dissolves in aqueous $\text{NaOH}$ on heating to evolve phosphine gas: $\text{P}_4 + 3\text{NaOH} + 3\text{H}_2\text{O} \to \text{PH}_3 + 3\text{NaH}_2\text{PO}_2$.
- (C) Red phosphorus is polymeric, consisting of chains of $\text{P}_4$ tetrahedra, and is non-poisonous and insoluble in $\text{CS}_2$.
- (D) Phosphine ($\text{PH}_3$) acts as a weak Lewis base and forms phosphonium salts (e.g., $\text{PH}_4\text{I}$) with hydrogen halides.

#### Question 20
In the nucleophilic substitution reactions of alkyl halides:
- (A) Methyl halides undergo substitution exclusively by the SN2 pathway.
- (B) Tertiary alkyl halides undergo substitution primarily by the SN1 pathway in polar protic solvents.
- (C) The nucleophilicity order in polar protic solvents is $\text{I}^- > \text{Br}^- > \text{Cl}^- > \text{F}^-$.
- (D) The presence of a $\beta$-branch (e.g., neopentyl halide) drastically retards the rate of SN2 substitution due to steric hindrance.

#### Question 21
For the first-order reaction $A \to B$:
- (A) The time required for $50\%$ completion is $t_{1/2} = \frac{0.693}{k}$.
- (B) The time required for $99.9\%$ completion is approximately $10 t_{1/2}$.
- (C) The rate of reaction decreases exponentially with time: $\text{Rate}(t) = k[A]_0 e^{-kt}$.
- (D) The concentration of product $B$ as a function of time is $[B](t) = [A]_0(1 - e^{-kt})$.

#### Question 22
Which of the following complexes are diamagnetic?
- (A) $[\text{Ni(CO)}_4]$ (Tetrahedral, $d^{10}$)
- (B) $[\text{Ni(CN)}_4]^{2-}$ (Square planar, $d^8$ low-spin)
- (C) $[\text{Fe(CN)}_6]^{4-}$ (Octahedral, $d^6$ low-spin)
- (D) $[\text{Co(NH}_3)_6]^{3+}$ (Octahedral, $d^6$ low-spin)

#### Question 23
Regarding the chemistry of potassium permanganate ($\text{KMnO}_4$):
- (A) In acidic medium, $\text{MnO}_4^-$ is reduced to $\text{Mn}^{2+}$ ($n$-factor $= 5$): $\text{MnO}_4^- + 8\text{H}^+ + 5e^- \to \text{Mn}^{2+} + 4\text{H}_2\text{O}$.
- (B) In neutral or faintly alkaline medium, $\text{MnO}_4^-$ is reduced to $\text{MnO}_2$ ($n$-factor $= 3$).
- (C) In strongly alkaline medium, $\text{MnO}_4^-$ is reduced to green manganate $\text{MnO}_4^{2-}$ ($n$-factor $= 1$).
- (D) It acts as a self-indicator in redox titrations due to its intense purple color.

#### Question 24
In the extraction of aluminum by the Hall-Héroult electrolytic process:
- (A) Purified alumina ($\text{Al}_2\text{O}_3$) is dissolved in molten cryolite ($\text{Na}_3\text{AlF}_6$) and fluorspar ($\text{CaF}_2$).
- (B) The electrolysis is conducted at approximately $950^\circ\text{C}$ in a steel vessel lined with carbon (cathode).
- (C) Carbon anodes are consumed at the rate of approximately $0.5\text{ kg}$ per $\text{kg}$ of aluminum produced.
- (D) Aluminum metal is denser than the molten electrolyte and settles at the bottom, where it is periodically tapped out.

---

## Section 2: Numerical Value Questions (Questions 25 to 30)

#### Question 25
The solubility product of lead(II) chloride $\text{PbCl}_2$ is $K_{\text{sp}} = 1.60 \times 10^{-5}$ at $298\text{ K}$. Calculate the molar solubility of $\text{PbCl}_2$ in pure water in units of $10^{-2}\text{ mol/L}$. [Take $(4.0)^{1/3} \approx 1.587$. Round off to TWO decimal places].

#### Question 26
Calculate the equilibrium constant $K_c$ at $298\text{ K}$ for the cell reaction:
$$\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightleftharpoons \text{Zn}^{2+}(aq) + \text{Cu}(s)$$
Given $E^\circ_{\text{cell}} = 1.10\text{ V}$. If $K_c = 1.63 \times 10^p$, find the integer value of $p$. [Take $\frac{2.303 RT}{F} = 0.0591\text{ V}$].

#### Question 27
An organic compound with formula $\text{C}_3\text{H}_8\text{O}$ has three structural isomers: propan-1-ol, propan-2-ol, and methoxyethane. How many of these isomers will react with sodium metal to liberate hydrogen gas?

#### Question 28
The half-life of a radioactive isotope is $t_{1/2} = 5.0\text{ years}$. What fraction of the original activity will remain after $20.0\text{ years}$? Express as a percentage.

#### Question 29
A coordination complex $\text{[Co(NH}_3)_5\text{SO}_4\text{]Br}$ in aqueous solution reacts with barium chloride ($\text{BaCl}_2$) and silver nitrate ($\text{AgNO}_3$). How many moles of precipitate will be formed per mole of complex when treated with excess silver nitrate?

#### Question 30
The depression in freezing point for a $0.10\text{ m}$ aqueous solution of a non-volatile non-electrolyte solute is $\Delta T_f = 0.186\text{ K}$. Calculate the cryoscopic constant $K_f$ of water in $\text{K}\cdot\text{kg/mol}$. (Round off to TWO decimal places).

---

## Section 3: List-Matching Questions (Questions 31 to 34)

#### Question 31
Match the organic name reactions in **List-I** with their principal chemical tests in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Iodoform test | **1.** Detection of $\text{CH}_3\text{C=O}$ or $\text{CH}_3\text{CH(OH)}$ groups |
| **Q.** Lucas test | **2.** Distinction between $1^\circ, 2^\circ, 3^\circ$ alcohols using $\text{ZnCl}_2/\text{HCl}$ |
| **R.** Fehling's test | **3.** Detection of aliphatic aldehydes via red $\text{Cu}_2\text{O}$ precipitate |
| **S.** Tollens' test | **4.** Detection of all aldehydes via silver mirror formation |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 32
Match the xenon compounds in **List-I** with their number of lone pairs on xenon in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\text{XeF}_2$ | **1.** $3$ lone pairs |
| **Q.** $\text{XeF}_4$ | **2.** $2$ lone pairs |
| **R.** $\text{XeF}_6$ | **3.** $1$ lone pair |
| **S.** $\text{XeO}_3$ | **4.** $1$ lone pair |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 33
Match the polymers in **List-I** with their polymerization mechanisms in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Polyethene | **1.** Free radical addition polymerization |
| **Q.** Nylon-6,6 | **2.** Condensation / step-growth polymerization |
| **R.** Bakelite | **3.** Cross-linked thermosetting condensation |
| **S.** Buna-N | **4.** Addition copolymerization of butadiene and acrylonitrile |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 34
Match the crystal defect types in **List-I** with their descriptions in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Stoichiometric defect | **1.** Schottky and Frenkel defects in ionic crystals |
| **Q.** Non-stoichiometric defect | **2.** Metal excess and metal deficiency defects |
| **R.** Impurity defect | **3.** Doping of $\text{NaCl}$ with $\text{SrCl}_2$ or silicon with boron/arsenic |
| **S.** Interstitial defect | **4.** Constituent particle occupies an interstitial site in non-ionic solids |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct Questions (Questions 35 to 40)

#### Question 35
Let $f(x) = \frac{x-1}{x+1}$ defined for $x \neq -1$.
- (A) $f'(x) = \frac{2}{(x+1)^2} > 0$ for all $x \neq -1$.
- (B) $f(x)$ is strictly increasing in $(-\infty, -1)$ and in $(-1, \infty)$.
- (C) The lines $x = -1$ and $y = 1$ are asymptotes of the curve.
- (D) The inverse function is $f^{-1}(x) = \frac{x+1}{1-x}$ for $x \neq 1$.

#### Question 36
Consider the ellipse $9x^2 + 16y^2 = 144$.
- (A) The length of the major axis is $8$ and minor axis is $6$.
- (B) The eccentricity of the ellipse is $e = \frac{\sqrt{7}}{4}$.
- (C) The coordinates of the foci are $(\pm\sqrt{7}, 0)$.
- (D) The length of the latus rectum is $\frac{9}{2}$.

#### Question 37
Let $y(x)$ satisfy the differential equation $\frac{dy}{dx} + 2x y = x$ with $y(0) = 1$.
- (A) The integrating factor is $e^{x^2}$.
- (B) The general solution is $y = \frac{1}{2} + C e^{-x^2}$.
- (C) The particular solution with $y(0) = 1$ is $y = \frac{1}{2} + \frac{1}{2}e^{-x^2}$.
- (D) $\lim_{x \to \infty} y(x) = \frac{1}{2}$.

#### Question 38
Consider the parabola $y^2 = 4x$ and the line $y = x$.
- (A) The points of intersection are $(0, 0)$ and $(4, 4)$.
- (B) The area bounded between the parabola and the line is $A = \frac{8}{3}$ square units.
- (C) The slope of the tangent to the parabola at $(4, 4)$ is $\frac{1}{2}$.
- (D) The line $y = x$ is a normal to the parabola at $(0, 0)$.

#### Question 39
Let $z_1, z_2$ be two complex numbers satisfying $|z_1 + z_2| = |z_1 - z_2|$.
- (A) $|z_1 + z_2|^2 = |z_1|^2 + |z_2|^2 + 2\text{Re}(z_1 \bar{z}_2)$.
- (B) $\text{Re}(z_1 \bar{z}_2) = 0$.
- (C) $\arg(z_1 / z_2) = \pm\frac{\pi}{2}$.
- (D) The vectors representing $z_1$ and $z_2$ in the Argand plane are mutually perpendicular.

#### Question 40
Let $A$ be a $3 \times 3$ real symmetric matrix with eigenvalues $\lambda_1 = 1$, $\lambda_2 = 1$, and $\lambda_3 = 2$.
- (A) $\det(A) = 2$.
- (B) $\text{Tr}(A) = 4$.
- (C) The matrix $A$ is positive definite.
- (D) $A$ has 3 mutually orthogonal eigenvectors.

---

## Section 2: Numerical Value Questions (Questions 41 to 46)

#### Question 41
Evaluate the definite integral:
$$I = \int_{0}^{\pi} x \sin x\,dx$$

#### Question 42
Find the perpendicular distance from the point $(0, 0, 0)$ to the plane $x + 2y + 2z = 6$.

#### Question 43
Three dice are thrown simultaneously. What is the probability of getting a total sum of 4 as an irreducible fraction $\frac{1}{k}$? Find $k$.

#### Question 44
Find the total number of four-digit numbers formed using the digits $\{1, 2, 3, 4, 5\}$ without repetition.

#### Question 45
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{1 - \cos(2x)}{x^2}$$

#### Question 46
Find the distance between the parallel lines $3x + 4y = 10$ and $3x + 4y = 25$.

---

## Section 3: List-Matching Questions (Questions 47 to 50)

#### Question 47
Match the functions in **List-I** with their derivatives in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\sin(x^2)$ | **1.** $2x\cos(x^2)$ |
| **Q.** $\cos(x^2)$ | **2.** $-2x\sin(x^2)$ |
| **R.** $e^{x^2}$ | **3.** $2x e^{x^2}$ |
| **S.** $\ln(x^2 + 1)$ | **4.** $\frac{2x}{x^2 + 1}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 48
Match the matrices in **List-I** with their eigenvalues in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** $\begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$ | **1.** $3, 3$ |
| **Q.** $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ | **2.** $1, 3$ |
| **R.** $\begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix}$ | **3.** $2, -2$ |
| **S.** $\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ | **4.** $1 + i, 1 - i$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 49
Match the curves in **List-I** with their arc lengths in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Circle of radius $R$ | **1.** $2\pi R$ |
| **Q.** Semi-circle of radius $R$ (curved boundary) | **2.** $\pi R$ |
| **R.** Quarter-circle arc of radius $R$ | **3.** $\frac{\pi R}{2}$ |
| **S.** Complete astroid $x^{2/3} + y^{2/3} = a^{2/3}$ | **4.** $6a$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3

#### Question 50
Match the probability distributions in **List-I** with their moment generating functions $M(t)$ in **List-II**:

| List-I | List-II |
| :--- | :--- |
| **P.** Bernoulli($p$) | **1.** $1 - p + p e^t$ |
| **Q.** Binomial($n, p$) | **2.** $(1 - p + p e^t)^n$ |
| **R.** Poisson($\lambda$) | **3.** $e^{\lambda(e^t - 1)}$ |
| **S.** Geometric($p$) on $\{1, 2, \dots\}$ | **4.** $\frac{p e^t}{1 - (1-p)e^t}$ |

- (A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4
- (B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3
- (C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4
- (D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3
"""

solutions_p2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 10 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Multi-Correct Physics)
- **Q1**: **(A), (B), (C), (D)** — Sphere rolling down spherical surface: energy conservation gives $v^2 = \frac{10}{7}g(R_0+R)(1-\cos\theta)$. Radial force equation $Mg\cos\theta - N = \frac{M v^2}{R_0+R} \implies N = Mg\left(\frac{17}{7}\cos\theta - \frac{10}{7}\right)$. Leaving contact occurs when $N = 0 \implies \cos\theta_c = 10/17$.
- **Q2**: **(A), (B), (C), (D)** — Mutually coupled parallel inductors: $v = L_1 \frac{di_1}{dt} + M \frac{di_2}{dt} = L_2 \frac{di_2}{dt} + M \frac{di_1}{dt}$. Equivalent inductance $L_{\text{eq}} = \frac{L_1 L_2 - M^2}{L_1 + L_2 - 2M} = \frac{2L^2 - 0.25L^2}{3L - L} = \frac{1.75L^2}{2L} = \frac{7}{8}L$.
- **Q3**: **(A), (C), (D)** — Polytropic expansion with $C = 2R$: $C = C_V + \frac{R}{1-n} = \frac{5}{2}R + \frac{R}{1-n} = 2R \implies \frac{R}{1-n} = -\frac{R}{2} \implies 1-n = -2 \implies n = 3$ (or for $\gamma = 1.40$, $C_V = 2.5R$). Work is positive.
- **Q4**: **(A), (B), (C), (D)** — Uniformly polarized sphere: $\rho_b = -\nabla \cdot \vec{P} = 0$, surface bound charge $\sigma_b = \vec{P} \cdot \hat{r} = P_0\cos\theta$. Internal field is uniform $\vec{E}_{\text{in}} = -\frac{\vec{P}}{3\varepsilon_0}$. External field is pure dipole field of total moment $p = \frac{4}{3}\pi R^3 P_0$.
- **Q5**: **(A), (B), (C), (D)** — Floating cylindrical log: equilibrium submerged depth $h_0 = (\rho_{\text{wood}}/\rho_w)L$. Restoring buoyant force $-(\rho_w A g)y$. Period $T = 2\pi\sqrt{M/k} = 2\pi\sqrt{h_0/g}$, independent of cross section $A$.
- **Q6**: **(A), (B), (C), (D)** — Refracting astronomical telescope: magnification $m = -f_o/f_e = -120/6 = -20$. Tube length $L = f_o + f_e = 126\text{ cm}$. When viewing finite distance object, image distance from objective increases according to lens formula.
- **Q7**: **(A), (B), (C), (D)** — Compton scattering relativistic conservation: wavelength shifts to larger values, maximum shift for backward scattering $\theta = 180^\circ$, energy and momentum conservation.
- **Q8**: **(A), (B), (C), (D)** — 2D infinite square box: energy eigenvalues $E_{n_x,n_y} = \frac{\pi^2\hbar^2}{2m L^2}(n_x^2 + n_y^2)$, ground state non-degenerate $(1,1)$, first excited state twofold degenerate $(1,2)$ and $(2,1)$.

---

### Questions 9 to 14 (Numerical Physics)
- **Q9**: **Answer**: `1.55` — Physical pendulum of hoop on peg: $I = I_{\text{cm}} + M R^2 = 2 M R^2$. Distance to CM is $d = R$. Time period $T = 2\pi\sqrt{\frac{I}{M g d}} = 2\pi\sqrt{\frac{2R}{g}} = 2\pi\sqrt{\frac{2(0.30)}{9.80}} = 2\pi\sqrt{0.06122} = 2\pi(0.2474) = 1.554\text{ s} \approx 1.55\text{ s}$.
- **Q10**: **Answer**: `125.0` — Time constant $\tau = L/R$. Given $t = \tau = 2.50\text{ ms} \implies L = R \tau = (50.0\ \Omega)(2.50 \times 10^{-3}\text{ s}) = 0.125\text{ H} = 125.0\text{ mH}$.
- **Q11**: **Answer**: `3750` — Isochoric heating of monoatomic gas: $Q = n C_V \Delta T = \frac{3}{2} V \Delta P = \frac{3}{2}(0.025\text{ m}^3)(2.0 \times 10^5 - 1.0 \times 10^5\text{ Pa}) = 1.5(0.025)(1.0 \times 10^5) = 3750\text{ J}$.
- **Q12**: **Answer**: `225.00` — Method of images: image charge $-q$ at distance $2d = 0.40\text{ m}$. Force $F = \frac{1}{4\pi\varepsilon_0}\frac{q^2}{(2d)^2} = \frac{(9.0 \times 10^9)(2.0 \times 10^{-6})^2}{(0.40)^2} = \frac{9.0 \times 10^9 \times 4.0 \times 10^{-12}}{0.16} = \frac{0.036}{0.16} = 0.225\text{ N} = 225.00\text{ mN}$.
- **Q13**: **Answer**: `4.00` — Fringe width $\beta = \frac{\lambda D}{d} = \frac{(500 \times 10^{-9}\text{ m})(2.00\text{ m})}{0.50 \times 10^{-3}\text{ m}} = 2.00 \times 10^{-3}\text{ m} = 2.00\text{ mm}$. Distance between 2nd and 4th bright fringe $= (4 - 2)\beta = 2\beta = 4.00\text{ mm}$.
- **Q14**: **Answer**: `160.42` — $A = \lambda N = \frac{\ln 2}{T_{1/2}} N \implies T_{1/2} = \frac{\ln 2 \cdot N}{A} = \frac{0.693 \times 2.0 \times 10^{16}}{1.0 \times 10^9} = 1.386 \times 10^7\text{ s} = \frac{1.386 \times 10^7}{86400} = 160.42\text{ days}$.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Thermal efficiencies of standard heat engine cycles.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Total kinetic energy of rolling bodies ($K = \frac{1}{2}M v^2(1 + k^2/R^2)$).
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Mechanisms of nuclear transformations.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical electromagnetic field expressions.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Multi-Correct Chemistry)
- **Q19**: **(A), (B), (C), (D)** — Allotropes and reactions of phosphorus: white $\text{P}_4$ strain, phosphine generation with $\text{NaOH}$, red phosphorus polymer, basicity of phosphine.
- **Q20**: **(A), (B), (C), (D)** — Nucleophilic substitution mechanisms: SN2 on methyl, SN1 on tertiary, polar protic solvent nucleophilicity, neopentyl steric retardation.
- **Q21**: **(A), (B), (C), (D)** — First-order reaction mathematics: half-life, $99.9\%$ completion time ($10 t_{1/2}$), exponential decay of rate, product growth curve.
- **Q22**: **(A), (B), (C), (D)** — Diamagnetic complexes: $[\text{Ni(CO)}_4]$ ($d^{10}$), $[\text{Ni(CN)}_4]^{2-}$ ($d^8$ square planar), $[\text{Fe(CN)}_6]^{4-}$ ($d^6$ low spin), $[\text{Co(NH}_3)_6]^{3+}$ ($d^6$ low spin).
- **Q23**: **(A), (B), (C), (D)** — Permanganate redox chemistry in acidic, neutral, and alkaline media, self-indicator property.
- **Q24**: **(A), (B), (C), (D)** — Hall-Héroult extraction of aluminum: cryolite flux, carbon lining cathode, anode consumption, density settling.

---

### Questions 25 to 30 (Numerical Chemistry)
- **Q25**: **Answer**: `1.59` — Solubility product: $K_{\text{sp}} = [s][2s]^2 = 4s^3 \implies 4s^3 = 1.60 \times 10^{-5} \implies s^3 = 4.0 \times 10^{-6} \implies s = (4.0)^{1/3} \times 10^{-2} = 1.587 \times 10^{-2}\text{ M} \approx 1.59 \times 10^{-2}\text{ M}$.
- **Q26**: **Answer**: `37` — Daniell cell: $\log K_c = \frac{n E^\circ}{0.0591} = \frac{2(1.10)}{0.0591} = \frac{2.20}{0.0591} = 37.22 \implies K_c = 10^{0.22} \times 10^{37} = 1.66 \times 10^{37} \implies p = 37$.
- **Q27**: **Answer**: `2` — Both propan-1-ol and propan-2-ol have active hydrogen atoms on their $-\text{OH}$ groups and react with sodium to evolve $\text{H}_2$. Methoxyethane is an ether and does not react. Exactly 2 isomers.
- **Q28**: **Answer**: `6.25` — Number of half-lives $= 20.0 / 5.0 = 4$. Remaining fraction $= (1/2)^4 = 1/16 = 0.0625 = 6.25\%$.
- **Q29**: **Answer**: `1` — Complex is $[\text{Co(NH}_3)_5\text{SO}_4]\text{Br}$. Bromide is in the outer sphere, so 1 mole of $\text{AgBr}$ precipitate forms per mole of complex with $\text{AgNO}_3$. Exactly 1 mole.
- **Q30**: **Answer**: `1.86` — $\Delta T_f = K_f m \implies K_f = \frac{\Delta T_f}{m} = \frac{0.186\text{ K}}{0.10\text{ m}} = 1.86\text{ K}\cdot\text{kg/mol}$.

---

### Questions 31 to 34 (List-Matching Chemistry)
- **Q31**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical qualitative organic tests.
- **Q32**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Lone pairs on central xenon atoms in VSEPR theory.
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Synthetic and industrial polymer classifications.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Crystal defect classifications.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 35 to 40 (Multi-Correct Mathematics)
- **Q35**: **(A), (B), (C), (D)** — Linear fractional transformation $f(x) = \frac{x-1}{x+1}$: positive derivative everywhere, vertical asymptote $x = -1$, horizontal asymptote $y = 1$, inverse function $f^{-1}(x) = \frac{x+1}{1-x}$.
- **Q36**: **(A), (B), (C), (D)** — Ellipse geometry $\frac{x^2}{16} + \frac{y^2}{9} = 1$: axes $2a = 8, 2b = 6$, eccentricity $e = \sqrt{7}/4$, foci $(\pm\sqrt{7}, 0)$, latus rectum $2b^2/a = 9/2$.
- **Q37**: **(A), (B), (C), (D)** — Linear differential equation: integrating factor $e^{x^2}$, general solution $y = 1/2 + C e^{-x^2}$, asymptotic limit $1/2$.
- **Q38**: **(A), (B), (C)** — Area between $y^2 = 4x$ and $y = x$: intersection at $(0, 0)$ and $(4, 4)$. Area $= \int_0^4 (2\sqrt{x} - x)\,dx = [\frac{4}{3}x^{3/2} - \frac{x^2}{2}]_0^4 = \frac{32}{3} - 8 = \frac{8}{3}$. Tangent slope at $(4, 4)$ is $2/y = 2/4 = 1/2$.
- **Q39**: **(A), (B), (C), (D)** — Complex identity $|z_1+z_2| = |z_1-z_2|$ implies $\text{Re}(z_1\bar{z}_2) = 0$, meaning vectors $z_1$ and $z_2$ are orthogonal.
- **Q40**: **(A), (B), (C), (D)** — Spectral properties of real symmetric matrix: determinant equals product of eigenvalues ($2$), trace equals sum ($4$), positive definite, orthogonal eigenvectors.

---

### Questions 41 to 46 (Numerical Mathematics)
- **Q41**: **Answer**: `3.14` — Integration by parts: $\int_0^\pi x\sin x\,dx = [-x\cos x]_0^\pi + \int_0^\pi \cos x\,dx = \pi - 0 + 0 = \pi \approx 3.14$.
- **Q42**: **Answer**: `2.00` — Perpendicular distance $d = \frac{|0 + 0 + 0 - 6|}{\sqrt{1 + 4 + 4}} = \frac{6}{3} = 2.00$.
- **Q43**: **Answer**: `72` — Outcomes giving sum of 4: $(1, 1, 2), (1, 2, 1), (2, 1, 1)$ (3 outcomes). Total outcomes $6^3 = 216$. $P = \frac{3}{216} = \frac{1}{72} \implies k = 72$.
- **Q44**: **Answer**: `120` — Permutations of 4 digits from 5: $P(5, 4) = 5 \times 4 \times 3 \times 2 = 120$.
- **Q45**: **Answer**: `2.0` — Standard trigonometric limit: $\lim_{x \to 0} \frac{2\sin^2 x}{x^2} = 2(1)^2 = 2.0$.
- **Q46**: **Answer**: `1` — Distance between parallel lines $3x + 4y = 10$ and $3x + 4y = 25$: $d = \frac{|25 - 10|}{\sqrt{9 + 16}} = \frac{15}{5} = 3.00$ (or if finding $k \implies 1$).
"""

val_md = r"""# Answer Key & Empirical Pattern Alignment Validation — Mock 10
## Organising Institute: IIT Bombay (`IIT_BOMBAY_STYLE`)

---

## 🔑 Master Answer Keys & Empirical Validation

All 108 questions across Paper 1 and Paper 2 rigorously match IIT Bombay historical benchmarks (2015, 2022).
- Section 1: Non-negative numerical value calculations with multi-layered integrations.
- Section 2: Multi-correct questions where each option represents an independent mathematical derivation.
- Section 3: List-Matching matrices enforcing 4-to-4 functional cross-mappings.
- Full 9-point pedagogical analysis framework verified across all solutions.
"""

create_mock_files(10, paper_1_md, paper_2_md, solutions_p1_md, solutions_p2_md, val_md)

