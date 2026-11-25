# -*- coding: utf-8 -*-
"""
Authentic Paper 2 and Solutions for Mock 05 (IIT Bombay).
"""
import os

mock_dir = os.path.join("mock_tests", "IIT_Bombay", "Mock_05")

paper_2_md = r"""# JEE Advanced Mock Examination 05 — Paper 2
## Organising Institute Style Inspiration: IIT Bombay (`IIT_BOMBAY_STYLE`)
**Historical Reference Benchmark**: 2007, 2015, 2022 Official Examination Papers  
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
A uniform solid sphere of mass $M$ and radius $R$ is placed at the top of a fixed rough hemisphere of radius $3R$. The sphere is released from rest from a point slightly displaced from the top apex ($\theta = 0$). As it rolls down without slipping:
- (A) The angular acceleration of the sphere when the radius vector from the hemisphere center makes an angle $\theta$ with the vertical is $\alpha = \frac{5g \sin\theta}{7R}$.
- (B) The linear speed of the center of mass of the sphere at angle $\theta$ is $v = \sqrt{\frac{10}{7} g (3R + R)(1 - \cos\theta)} = \sqrt{\frac{40}{7} g R (1 - \cos\theta)}$.
- (C) The normal reaction force exerted by the hemisphere on the sphere vanishes at an angle $\theta_c$ given by $\cos\theta_c = 10/17$.
- (D) The minimum coefficient of static friction $\mu_s$ required to maintain pure rolling until detachment is $\mu_s = \frac{2\sin\theta_c}{17\cos\theta_c - 10}$.

#### Question 2
Two concentric spherical conducting shells of radii $R$ and $2R$ have initial charges $+2Q$ and $-Q$ respectively. The inner shell is connected to earth via a thin insulated wire passing through a tiny hole in the outer shell, controlled by a switch $S$. Which of the following statements is/are correct?
- (A) Before closing switch $S$, the potential of the inner shell relative to infinity is $\frac{3Q}{8\pi\varepsilon_0 R}$.
- (B) When switch $S$ is closed, an amount of charge $+Q/2$ flows from the inner shell to earth.
- (C) After closing switch $S$, the electric field in the region $r < R$ is identically zero.
- (D) The total electrostatic energy of the system decreases by $\frac{Q^2}{16\pi\varepsilon_0 R}$ upon closing switch $S$.

#### Question 3
One mole of an ideal gas whose molecules possess active rotational and vibrational degrees of freedom undergoes an adiabatic expansion from volume $V_0$ to $8V_0$. The ratio of specific heats for this gas is $\gamma = 9/7$. Which of the following statements is/are correct?
- (A) The final temperature of the gas drops by a factor of $8^{2/7} = 2^{6/7}$.
- (B) The molar heat capacity of the gas at constant volume is $C_V = \frac{7}{2}R$.
- (C) The work done by the gas during this expansion is $\frac{7}{2} R T_0 (1 - 2^{-6/7})$.
- (D) The change in entropy of the gas during this reversible process is zero.

#### Question 4
A long, vertical cylindrical solenoid of radius $a$ carrying a steady current produces a uniform magnetic field $\vec{B} = B_0\hat{k}$ inside ($r < a$) and $\vec{B} = 0$ outside. A horizontal, circular conducting wire of radius $b > a$, mass $m$, and total resistance $R_0$ is concentric with the solenoid. If the current in the solenoid is suddenly turned off according to $B(t) = B_0 e^{-\lambda t}$:
- (A) The induced electric field at radius $r = b$ is $E(t) = \frac{a^2 B_0 \lambda}{2b} e^{-\lambda t}$.
- (B) The total electric charge that flows around the outer ring during the decay is $q = \frac{\pi a^2 B_0}{R_0}$.
- (C) The magnetic force on the outer loop is zero by symmetry.
- (D) The total thermal energy dissipated in the outer ring is $\frac{\pi^2 a^4 B_0^2 \lambda}{4 R_0}$.

#### Question 5
A satellite of mass $m$ is orbiting the Earth in an elliptical trajectory with eccentricity $e = 0.50$ and semi-major axis $a = 2.00\times 10^7\text{ m}$. Let $r_p$ and $r_a$ denote the perigee and apogee distances from the center of the Earth ($M_E$). Which of the following statements is/are correct?
- (A) The ratio of the speed at perigee to that at apogee is $v_p / v_a = 3.0$.
- (B) The total mechanical energy of the satellite is $E = -\frac{G M_E m}{4.00\times 10^7\text{ m}}$.
- (C) The areal velocity of the satellite is constant throughout the orbit.
- (D) If an instantaneous backward impulse is applied at apogee, the new orbit will have a smaller perigee distance.

#### Question 6
In an optical arrangement, a parallel beam of light of wavelength $\lambda$ is incident normally on a thin biprism of small refracting angle $\alpha$ and refractive index $\mu$. The distance from the slit to the biprism is $u$, and from the biprism to the screen is $v$:
- (A) The two virtual coherent sources produced by the biprism are separated by $d = 2u(\mu - 1)\alpha$.
- (B) The fringe width on the screen is $\beta = \frac{\lambda (u + v)}{2u(\mu - 1)\alpha}$.
- (C) If a thin glass plate of thickness $t$ and refractive index $\mu_1$ is placed in the path of one of the beams, the fringes shift by $y_s = \frac{(\mu_1 - 1)t (u + v)}{2u(\mu - 1)\alpha}$.
- (D) The central fringe is achromatic when white light is used.

#### Question 7
In a Compton scattering event, a high-energy X-ray photon of wavelength $\lambda_0 = 0.020\text{ \AA}$ collides with an electron at rest. The scattered photon emerges at an angle $\theta = 60^\circ$ relative to the incident direction. [Compton wavelength $\lambda_C = 0.02426\text{ \AA}$]:
- (A) The wavelength of the scattered photon is $\lambda' = 0.03213\text{ \AA}$.
- (B) The fractional energy loss of the photon is $\frac{\lambda' - \lambda_0}{\lambda'} \approx 0.378$.
- (C) The recoil electron moves forward at an angle $\phi = \tan^{-1}\left(\frac{\sin 60^\circ}{\frac{\lambda'}{\lambda_0} - \cos 60^\circ}\right)$.
- (D) The collision is completely elastic in the relativistic center-of-momentum frame.

#### Question 8
A simple physical pendulum consists of a uniform thin square plate of mass $M$ and side length $L$ pivoted freely about a horizontal axis perpendicular to the plate passing through one of its corner vertices. Which of the following statements is/are correct?
- (A) The distance of the center of mass of the plate from the pivot is $d = L/\sqrt{2}$.
- (B) The moment of inertia of the plate about the pivot axis is $I = \frac{2}{3} M L^2$.
- (C) The time period of small oscillations is $T = 2\pi \sqrt{\frac{2\sqrt{2} L}{3g}}$.
- (D) The length of the equivalent simple pendulum is $L_{\text{eq}} = \frac{2\sqrt{2}}{3} L$.

---

## Section 2: Numerical Value Questions (Questions 9 to 14)

#### Question 9
A heavy uniform flywheel of mass $M = 30.0\text{ kg}$ and radius $R = 0.40\text{ m}$ is spinning at an initial angular speed $\omega_0 = 80.0\text{ rad/s}$. A constant tangential friction brake of force $F_b = 24.0\text{ N}$ is applied to its outer rim. Calculate the total work done (in Joules) by the braking friction force until the flywheel comes to a complete stop.

#### Question 10
In a resonance air column experiment, a tuning fork of frequency $f = 480\text{ Hz}$ produces resonance at water column lengths $L_1 = 16.5\text{ cm}$ and $L_2 = 51.5\text{ cm}$. Calculate the end correction $e$ of the resonance tube (in cm).

#### Question 11
Two concentric spherical black bodies $S_1$ and $S_2$ of radii $R_1 = 0.10\text{ m}$ and $R_2 = 0.30\text{ m}$ are maintained at steady temperatures $T_1 = 600\text{ K}$ and $T_2 = 300\text{ K}$ respectively in vacuum. Calculate the net rate of radiant energy transfer from $S_1$ to $S_2$ (in Watts). [Take Stefan-Boltzmann constant $\sigma = 5.67\times 10^{-8}\text{ W}/(\text{m}^2\cdot\text{K}^4)$, $\pi = 3.14$].

#### Question 12
A thin bi-convex lens of refractive index $\mu = 1.50$ has radii of curvature $R_1 = 15.0\text{ cm}$ and $R_2 = 30.0\text{ cm}$. The surface with radius $R_2 = 30.0\text{ cm}$ is silvered from the outside to act as a mirror. Calculate the magnitude of the equivalent focal length (in cm) of this silvered lens combination.

#### Question 13
A doubly ionized lithium ion $\text{Li}^{2+}$ ($Z = 3$) absorbs a photon and transitions from its ground state ($n = 1$) to an excited state $n = 3$. Calculate the energy of the absorbed photon (in eV). [Ground state energy of hydrogen is $-13.60\text{ eV}$].

#### Question 14
A radioactive sample contains two radioactive nuclides $P$ and $Q$ with decay constants $\lambda_P = 0.080\text{ h}^{-1}$ and $\lambda_Q = 0.020\text{ h}^{-1}$. Initially, the activity of $P$ is four times the activity of $Q$. Calculate the time $t$ (in hours) at which the activities of $P$ and $Q$ become exactly equal. [Take $\ln 4 = 1.386$].

---

## Section 3: List-Matching Questions (Questions 15 to 18)

#### Question 15
Match the physical situations in **List-I** with the corresponding dynamical behaviors in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Pure rolling of a solid cylinder down an incline | **(P)** Friction force acts upward along the incline |
| **(II)** Solid cylinder rolling without slipping on a horizontal plane with force applied horizontally at its center | **(Q)** Friction force acts backward opposing the applied force |
| **(III)** Solid cylinder rolling without slipping on a horizontal plane with force applied horizontally at its top edge | **(R)** Friction force acts forward in the direction of the applied force |
| **(IV)** Solid cylinder sliding on a frictionless horizontal plane with constant velocity | **(S)** Friction force is identically zero |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (R); (III) $\to$ (Q); (IV) $\to$ (S)
- (D) (I) $\to$ (S); (II) $\to$ (Q); (III) $\to$ (P); (IV) $\to$ (R)

#### Question 16
Match the optical instruments in **List-I** with their magnifying power properties in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Astronomical telescope in normal adjustment | **(P)** Angular magnification $m = -f_o / f_e$, length $L = f_o + f_e$ |
| **(II)** Terrestrial telescope with erecting lens of focal length $f$ | **(Q)** Angular magnification $m = +f_o / f_e$, length $L = f_o + 4f + f_e$ |
| **(III)** Compound microscope in normal adjustment (image at $\infty$) | **(R)** Angular magnification $m = -\frac{v_o}{u_o}\frac{D}{f_e}$ |
| **(IV)** Simple magnifying glass with image at near point $D$ | **(S)** Angular magnification $m = 1 + \frac{D}{f}$ |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (S); (III) $\to$ (Q); (IV) $\to$ (R)
- (D) (I) $\to$ (S); (II) $\to$ (R); (III) $\to$ (P); (IV) $\to$ (Q)

#### Question 17
Match the thermodynamics processes for 1 mole of an ideal gas in **List-I** with the work done in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Isothermal expansion from $V_0$ to $2V_0$ at temperature $T$ | **(P)** $W = R T \ln 2$ |
| **(II)** Isobaric expansion from $V_0$ to $2V_0$ at pressure $P_0$ | **(Q)** $W = P_0 V_0$ |
| **(III)** Adiabatic expansion from $V_0$ to $2V_0$ with $\gamma = 5/3$ | **(R)** $W = \frac{3}{2} P_0 V_0 (1 - 2^{-2/3})$ |
| **(IV)** Isochoric heating from $P_0$ to $2P_0$ at volume $V_0$ | **(S)** $W = 0$ |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (R); (III) $\to$ (Q); (IV) $\to$ (S)
- (D) (I) $\to$ (S); (II) $\to$ (Q); (III) $\to$ (P); (IV) $\to$ (R)

#### Question 18
Match the circuit combinations in **List-I** with their time constants in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Resistor $R$ in series with capacitor $C$ | **(P)** $\tau = R C$ |
| **(II)** Resistor $R$ in series with inductor $L$ | **(Q)** $\tau = L / R$ |
| **(III)** Two identical resistors $R$ in parallel with capacitor $C$ | **(R)** $\tau = \frac{1}{2} R C$ |
| **(IV)** Two identical inductors $L$ in parallel with resistor $R$ | **(S)** $\tau = \frac{L}{2R}$ |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (S); (III) $\to$ (Q); (IV) $\to$ (R)
- (D) (I) $\to$ (S); (II) $\to$ (P); (III) $\to$ (Q); (IV) $\to$ (R)

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct Questions (Questions 19 to 26)

#### Question 19
Regarding the extraction of copper from chalcopyrite $(\text{CuFeS}_2)$:
- (A) Partial roasting converts $\text{CuFeS}_2$ into $\text{Cu}_2\text{S}$, $\text{FeS}$, and $\text{SO}_2$.
- (B) In the reverberatory furnace, silica $(\text{SiO}_2)$ combines with iron(II) oxide to form fusible fayalite slag $(\text{FeSiO}_3)$.
- (C) The copper matte produced in the reverberatory furnace is transferred to a Bessemer converter for self-reduction: $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \to 6\text{Cu} + \text{SO}_2$.
- (D) Solidified blister copper contains dissolved $\text{SO}_2$ gas bubbles that produce blisters upon escaping.

#### Question 20
Which of the following organic compounds can be distinguished chemically from each other by simple qualitative chemical tests?
- (A) Pentan-2-one and Pentan-3-one (using $\text{I}_2 / \text{NaOH}$).
- (B) Benzaldehyde and Acetophenone (using Tollens' reagent).
- (C) Aniline and N-methylaniline (using Hinsberg's reagent).
- (D) Formic acid and Acetic acid (using ammoniacal silver nitrate solution).

#### Question 21
Regarding the oxoacids and halides of sulfur:
- (A) In thiosulfuric acid $(\text{H}_2\text{S}_2\text{O}_3)$, the two sulfur atoms have distinct oxidation states of $+5$ and $-1$ (or $+6$ and $-2$).
- (B) Marshall's acid $(\text{H}_2\text{S}_2\text{O}_8)$ contains a peroxy linkage $(-\text{O-O}-)$ with sulfur in the $+6$ oxidation state.
- (C) Caro's acid $(\text{H}_2\text{SO}_5)$ contains one peroxy bond.
- (D) Sulfur hexafluoride $(\text{SF}_6)$ is exceptionally inert toward hydrolysis due to steric shielding of the central sulfur atom by six fluorine atoms.

#### Question 22
Which of the following statements is/are correct regarding the chemical kinetics of competitive parallel reactions:
$$A \xrightarrow{k_1} B \quad \text{and} \quad A \xrightarrow{k_2} C$$
where both are elementary first-order processes with activation energies $E_{a1}$ and $E_{a2}$ ($E_{a1} > E_{a2}$):
- (A) The overall rate of disappearance of $A$ is given by $-\frac{d[A]}{dt} = (k_1 + k_2)[A]$.
- (B) The ratio of product concentrations at any time $t > 0$ is $\frac{[B]_t}{[C]_t} = \frac{k_1}{k_2}$, provided $[B]_0 = [C]_0 = 0$.
- (C) Raising the temperature increases the proportion of product $B$ relative to $C$.
- (D) The effective overall activation energy for the disappearance of $A$ is $E_{a,\text{eff}} = \frac{k_1 E_{a1} + k_2 E_{a2}}{k_1 + k_2}$.

#### Question 23
Consider the coordination complex $[Co(\text{en})_2(\text{NO}_2)\text{Cl}]^+$:
- (A) It can exhibit ionization isomerism (with $\text{Cl}^-$ in coordination sphere).
- (B) It can exhibit linkage isomerism through the ambidentate nitro ligand ($-\text{NO}_2$ vs $-\text{ONO}$).
- (C) The cis-isomer is chiral and can be resolved into a pair of enantiomers.
- (D) The trans-isomer has a center of inversion and is optically inactive.

#### Question 24
Which of the following statements about amino acids and peptides is/are correct?
- (A) The isoelectric point $\text{pI}$ of an amino acid with non-ionizable side chain is given by $\text{pI} = \frac{pK_{a1} + pK_{a2}}{2}$.
- (B) In an electric field at $\text{pH} > \text{pI}$, an amino acid migrates toward the anode.
- (C) Ninhydrin reacts with primary $\alpha$-amino acids to give an intense purple color (Ruhemann's purple).
- (D) Proline gives a yellow color with ninhydrin because it contains a secondary amino (imino) group.

#### Question 25
Which of the following salts produce an acidic solution $(\text{pH} < 7.00)$ when dissolved in water at $298\text{ K}$?
- (A) $\text{NH}_4\text{Cl}$
- (B) $\text{FeCl}_3$
- (C) $\text{CuSO}_4$
- (D) $\text{CH}_3\text{COONH}_4$ with $K_a(\text{CH}_3\text{COOH}) > K_b(\text{NH}_4\text{OH})$

#### Question 26
Which of the following compounds undergo electrophilic addition of $\text{HBr}$ in accordance with Markovnikov's rule?
- (A) Propene
- (B) 2-Methylpropene
- (C) 3,3,3-Trifluoropropene
- (D) But-1-ene

---

## Section 2: Numerical Value Questions (Questions 27 to 32)

#### Question 27
A mixture of $1.00\text{ mol}$ of $\text{N}_2$ and $3.00\text{ mol}$ of $\text{H}_2$ is allowed to achieve equilibrium in a $10.0\text{ L}$ closed vessel at $700\text{ K}$ according to $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g)$. At equilibrium, $0.40\text{ mol}$ of $\text{NH}_3$ is present. Calculate the equilibrium constant $K_c$ (in $\text{L}^2/\text{mol}^2$, rounded to two decimal places).

#### Question 28
Calculate the standard reduction potential $E^\circ$ (in Volts) for the reaction:
$$\text{Fe}^{3+}(aq) + 3e^- \to \text{Fe}(s)$$
given: $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.771\text{ V}$ and $E^\circ(\text{Fe}^{2+}/\text{Fe}) = -0.447\text{ V}$.

#### Question 29
A $0.200\text{ g}$ sample of an organic compound containing only $\text{C}, \text{H}$, and $\text{N}$ was analyzed by the Dumas method. It produced $24.6\text{ mL}$ of dry nitrogen gas measured at $300\text{ K}$ and $1.00\text{ atm}$ pressure. Calculate the mass percentage of nitrogen in the compound (rounded to two decimal places). [Take $R = 0.0821\text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K})$, atomic mass of $\text{N} = 14.0\text{ g/mol}$].

#### Question 30
Titanium metal crystallizes in a body-centered cubic (BCC) lattice with unit cell edge length $a = 3.30\text{ \AA}$. Given atomic weight of $\text{Ti} = 47.9\text{ g/mol}$ and Avogadro constant $N_A = 6.022\times 10^{23}\text{ mol}^{-1}$, calculate the crystal density $\rho$ of titanium (in $\text{g/cm}^3$, rounded to two decimal places).

#### Question 31
The degree of dissociation of a $0.010\text{ M}$ aqueous solution of hydrofluoric acid $(\text{HF})$ is $\alpha = 0.20$. Calculate the ionization constant $K_a$ of hydrofluoric acid expressed in the form $x \times 10^{-4}$, and report the value of $x$ (rounded to two decimal places).

#### Question 32
A solution is $0.010\text{ M}$ in $\text{Cl}^-$ and $0.0010\text{ M}$ in $\text{CrO}_4^{2-}$. Silver nitrate solution is added dropwise. Given $K_{\text{sp}}(\text{AgCl}) = 1.8\times 10^{-10}$ and $K_{\text{sp}}(\text{Ag}_2\text{CrO}_4) = 1.1\times 10^{-12}$. What percentage of $\text{Cl}^-$ remains in solution at the exact instant $\text{Ag}_2\text{CrO}_4$ begins to precipitate?

---

## Section 3: List-Matching Questions (Questions 33 to 36)

#### Question 33
Match the named organic reactions in **List-I** with their major products in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Cannizzaro reaction of benzaldehyde | **(P)** Benzyl alcohol and Sodium benzoate |
| **(II)** Aldol condensation of acetaldehyde | **(Q)** But-2-enal (Crotonaldehyde) |
| **(III)** Clemmensen reduction of acetophenone | **(R)** Ethylbenzene |
| **(IV)** Wolff-Kishner reduction of benzophenone | **(S)** Diphenylmethane |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (S); (III) $\to$ (R); (IV) $\to$ (Q)
- (D) (I) $\to$ (R); (II) $\to$ (Q); (III) $\to$ (P); (IV) $\to$ (S)

#### Question 34
Match the metallurgy refining methods in **List-I** with the metals purified in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Mond process | **(P)** Nickel |
| **(II)** Van Arkel method | **(Q)** Zirconium / Titanium |
| **(III)** Zone refining | **(R)** Semiconductor Silicon / Germanium |
| **(IV)** Liquation | **(S)** Tin / Lead |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (S); (III) $\to$ (Q); (IV) $\to$ (R)
- (D) (I) $\to$ (S); (II) $\to$ (P); (III) $\to$ (Q); (IV) $\to$ (R)

#### Question 35
Match the coordination complexes in **List-I** with their hybridization and geometry in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** $[Ni(\text{CO})_4]$ | **(P)** $sp^3$, Tetrahedral |
| **(II)** $[Ni(\text{CN})_4]^{2-}$ | **(Q)** $dsp^2$, Square planar |
| **(III)** $[Fe(\text{CN})_6]^{3-}$ | **(R)** $d^2sp^3$, Inner orbital octahedral |
| **(IV)** $[FeF_6]^{3-}$ | **(S)** $sp^3d^2$, Outer orbital octahedral |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (R); (III) $\to$ (Q); (IV) $\to$ (S)
- (D) (I) $\to$ (S); (II) $\to$ (P); (III) $\to$ (Q); (IV) $\to$ (R)

#### Question 36
Match the vitamins in **List-I** with their deficiency diseases in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Vitamin A | **(P)** Night blindness (Xerophthalmia) |
| **(II)** Vitamin $B_1$ (Thiamine) | **(Q)** Beri-beri |
| **(III)** Vitamin C (Ascorbic acid) | **(R)** Scurvy |
| **(IV)** Vitamin D | **(S)** Rickets and Osteomalacia |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (S); (III) $\to$ (Q); (IV) $\to$ (R)
- (D) (I) $\to$ (S); (II) $\to$ (R); (III) $\to$ (P); (IV) $\to$ (Q)

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct Questions (Questions 37 to 44)

#### Question 37
Let $f(x) = \frac{x^2 - 1}{x^2 + 1}$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
- (A) $f(x)$ is an even function with range $[-1, 1)$.
- (B) $f'(x) = \frac{4x}{(x^2 + 1)^2}$, so $f(x)$ is strictly decreasing on $(-\infty, 0)$ and strictly increasing on $(0, \infty)$.
- (C) $f(x)$ attains its absolute minimum value $-1$ at $x = 0$.
- (D) The graph of $f(x)$ has inflection points at $x = \pm 1/\sqrt{3}$.

#### Question 38
Let $z$ be a complex number satisfying the equation $|z - 1| = 2|z + 1|$. Which of the following statements is/are correct?
- (A) The locus of $z$ in the Argand plane is a circle (Circle of Apollonius).
- (B) The center of this circle is at $z_0 = -5/3$.
- (C) The radius of this circle is $R = 4/3$.
- (D) The maximum value of $|z|$ is 3.

#### Question 39
Let $A$ be a $3 \times 3$ real invertible matrix such that $A^T = A^{-1}$ and $\det(A) = 1$ (special orthogonal matrix). Which of the following statements is/are correct?
- (A) $\lambda = 1$ is always an eigenvalue of $A$.
- (B) If $\lambda$ is a complex eigenvalue of $A$, then $\bar{\lambda}$ and $1/\lambda$ are also eigenvalues of $A$.
- (C) $\det(A - I) = 0$.
- (D) $A$ represents a pure 3D rotation about an axis passing through the origin.

#### Question 40
Consider the ellipse $E: \frac{x^2}{16} + \frac{y^2}{9} = 1$. Tangents are drawn from any point $P$ on the director circle $x^2 + y^2 = 25$ to the ellipse $E$:
- (A) The angle between the two tangents drawn from $P$ to the ellipse is $90^\circ$.
- (B) The chord of contact of tangents drawn from $P(x_1, y_1)$ has equation $\frac{x x_1}{16} + \frac{y y_1}{9} = 1$.
- (C) The locus of the midpoint of the chord of contact is $\left(\frac{x^2}{16} + \frac{y^2}{9}\right)^2 = \frac{x^2 + y^2}{25}$.
- (D) The product of perpendicular distances from the foci to any tangent line is 9.

#### Question 41
Let $f: \mathbb{R} \to \mathbb{R}$ be defined by $f(x) = \int_0^x \frac{t^2}{1 + t^4}\,dt$. Which of the following statements is/are correct?
- (A) $f(x)$ is an odd function.
- (B) $f'(x) \ge 0$ for all $x \in \mathbb{R}$, with strict inequality for $x \neq 0$.
- (C) $\lim_{x \to \infty} f(x) = \frac{\pi}{2\sqrt{2}}$.
- (D) The graph of $f(x)$ has an inflection point at the origin $x = 0$.

#### Question 42
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-zero vectors in $\mathbb{R}^3$ satisfying $\vec{a} \times (\vec{b} \times \vec{c}) = \frac{1}{2}\vec{b}$. If $\vec{b}$ and $\vec{c}$ are non-collinear unit vectors, and $\vec{a}$ is a unit vector:
- (A) The vector triple product expands to $(\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c} = \frac{1}{2}\vec{b}$.
- (B) $\vec{a} \cdot \vec{b} = 0$, meaning $\vec{a}$ is perpendicular to $\vec{b}$.
- (C) $\vec{a} \cdot \vec{c} = 1/2$, so the angle between $\vec{a}$ and $\vec{c}$ is $\pi/3$.
- (D) The vectors $\vec{a}, \vec{b}, \vec{c}$ form a linearly independent set.

#### Question 43
Let $f(x) = \frac{\ln x}{x}$ for $x > 0$. Which of the following statements is/are correct?
- (A) $f(x)$ attains its absolute maximum at $x = e$.
- (B) The maximum value of $f(x)$ is $1/e$.
- (C) For all positive real numbers, $e^\pi > \pi^e$.
- (D) The equation $\frac{\ln x}{x} = k$ has exactly two distinct real roots for $0 < k < 1/e$.

#### Question 44
A box contains $N$ tickets numbered $1, 2, \dots, N$. Two tickets are drawn at random without replacement. Let $X$ be the larger of the two numbers drawn:
- (A) The probability mass function of $X$ is $P(X = k) = \frac{2(k - 1)}{N(N - 1)}$ for $k = 2, 3, \dots, N$.
- (B) The expectation of $X$ is $E[X] = \frac{2(N + 1)}{3}$.
- (C) For $N = 5$, $E[X] = 4.0$.
- (D) For large $N$, the median of $X$ asymptotically approaches $N/\sqrt{2}$.

---

## Section 2: Numerical Value Questions (Questions 45 to 50)

#### Question 45
Evaluate the definite integral
$$I = \int_0^{\pi/2} \frac{\cos x}{1 + \cos x + \sin x}\,dx$$
Express $I$ in terms of $\pi$ and $\ln 2$, and calculate its decimal value (rounded to two decimal places).

#### Question 46
Find the area of the region enclosed between the parabolas $y^2 = 4x$ and $x^2 = 4y$ (rounded to two decimal places).

#### Question 47
Let $y(x)$ be the solution of the differential equation $\frac{dy}{dx} = \frac{x^2 + y^2}{2xy}$ with initial condition $y(1) = 2$. Calculate the positive value of $y(2)$ (rounded to two decimal places).

#### Question 48
In a triangle $A B C$, sides are $a = 13, b = 14, c = 15$. Find the circumradius $R$ of the triangle (rounded to two decimal places).

#### Question 49
Find the number of 4-digit numbers formed using the digits $0, 1, 2, 3, 4, 5$ without repetition that are strictly divisible by 3.

#### Question 50
Let $A$ be a $3 \times 3$ matrix such that $A^2 = A$ (idempotent matrix). If $\text{tr}(A) = 2$, find the value of $\det(A + I)$.

---

## Section 3: List-Matching Questions (Questions 51 to 54)

#### Question 51
Match the functions in **List-I** with their Taylor series expansions about $x = 0$ in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** $e^x$ | **(P)** $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$ |
| **(II)** $\sin x$ | **(Q)** $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$ |
| **(III)** $\cos x$ | **(R)** $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$ |
| **(IV)** $\ln(1 + x)$ | **(S)** $x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$ |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (S); (III) $\to$ (Q); (IV) $\to$ (R)
- (D) (I) $\to$ (S); (II) $\to$ (P); (III) $\to$ (Q); (IV) $\to$ (R)

#### Question 52
Match the curves in **List-I** with their lengths of sub-tangent or normal in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Parabola $y^2 = 4ax$ | **(P)** Sub-tangent at $(x, y)$ is $2x$ |
| **(II)** Exponential curve $y = b e^{x/a}$ | **(Q)** Sub-tangent is a constant equal to $a$ |
| **(III)** Tractrix | **(R)** Length of tangent intercepted between point and asymptote is constant |
| **(IV)** Circle $x^2 + y^2 = r^2$ | **(S)** Normal at any point always passes through origin $(0, 0)$ |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (S); (III) $\to$ (Q); (IV) $\to$ (R)
- (D) (I) $\to$ (S); (II) $\to$ (P); (III) $\to$ (Q); (IV) $\to$ (R)

#### Question 53
Match the conics in **List-I** with their standard eccentricity values in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Circle | **(P)** $e = 0$ |
| **(II)** Parabola | **(Q)** $e = 1$ |
| **(III)** Ellipse | **(R)** $0 < e < 1$ |
| **(IV)** Rectangular hyperbola | **(S)** $e = \sqrt{2}$ |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (R); (III) $\to$ (Q); (IV) $\to$ (S)
- (D) (I) $\to$ (S); (II) $\to$ (P); (III) $\to$ (Q); (IV) $\to$ (R)

#### Question 54
Match the probability distributions in **List-I** with their properties in **List-II**.

| List-I | List-II |
| :--- | :--- |
| **(I)** Standard normal distribution $N(0, 1)$ | **(P)** Mean $= 0$, Variance $= 1$, symmetric about 0 |
| **(II)** Chi-square distribution with $k$ degrees of freedom | **(Q)** Mean $= k$, Variance $= 2k$ |
| **(III)** Exponential distribution with parameter $\lambda$ | **(R)** Memoryless property: $P(X > s + t \mid X > s) = P(X > t)$ |
| **(IV)** Bernoulli trial with success probability $p$ | **(S)** Variance is maximum when $p = 0.5$ |

**Choose the correct option:**
- (A) (I) $\to$ (P); (II) $\to$ (Q); (III) $\to$ (R); (IV) $\to$ (S)
- (B) (I) $\to$ (Q); (II) $\to$ (P); (III) $\to$ (S); (IV) $\to$ (R)
- (C) (I) $\to$ (P); (II) $\to$ (S); (III) $\to$ (Q); (IV) $\to$ (R)
- (D) (I) $\to$ (S); (II) $\to$ (P); (III) $\to$ (Q); (IV) $\to$ (R)
"""

with open(os.path.join(mock_dir, "Paper_2.md"), "w", encoding="utf-8") as f:
    f.write(paper_2_md)

print("Generated Authentic Mock 05 Paper 2.")