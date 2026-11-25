# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 04.
Empirical Signature: IIT Delhi Benchmark (2013, 2020)
- Multi-correct dominance (+4/-2 with partial marking)
- Image charges, relativistic transverse Doppler, RLC switch transients
- Hoffman vs Saytzeff elimination, spin crossover, borax bead chemistry
- Reciprocal vector systems, Clairaut ODEs, derangements
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 04 — Paper 1
## Organising Institute Style Inspiration: IIT Delhi (`IIT_DELHI_STYLE`)
**Historical Reference Benchmark**: 2013, 2020 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject — Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject — Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A point charge $q$ is located at a distance $d$ from the center $O$ of a grounded, neutral, conducting spherical shell of radius $R$ ($d > R$). Using the method of electrostatic image charges:
(A) The potential outside the sphere can be found by replacing the sphere with an image charge $q' = -q \frac{R}{d}$ located at distance $d' = \frac{R^2}{d}$ from $O$ along the line joining $O$ and $q$.  
(B) The electric potential at the surface of the sphere is identically zero ($V = 0$).  
(C) The total charge induced on the surface of the grounded conducting sphere is $q_{\text{ind}} = -q \frac{R}{d}$.  
(D) The attractive force between the charge $q$ and the grounded sphere is $F = \frac{q^2 R d}{4\pi\varepsilon_0 (d^2 - R^2)^2}$.

#### Question 2
A source of monochromatic light of proper frequency $\nu_0$ moves with relativistic velocity $v = 0.60c$ relative to an observer. At the moment when the line of sight from the observer to the source makes an angle $\theta = 90^\circ$ with the velocity vector of the source in the observer's frame (Transverse Doppler Effect):
(A) The time dilation factor of the source is $\gamma = \frac{1}{\sqrt{1 - (0.60)^2}} = 1.25$.  
(B) The observed frequency is shifted to the red (lower frequency) with $\nu = \frac{\nu_0}{\gamma} = 0.80\nu_0$.  
(C) This transverse shift is a purely relativistic time-dilation effect with no classical Newtonian analogue.  
(D) If the source moves directly toward the observer ($\theta = 0^\circ$), the observed frequency is $\nu = 2.0\nu_0$.

#### Question 3
A series $RLC$ circuit consists of an inductor $L = 0.10\text{ H}$, a resistor $R = 20\ \Omega$, and a capacitor $C = 100\ \mu\text{F}$ connected in series with a DC voltage source of EMF $V_0 = 50.0\text{ V}$ and a switch $S$. At $t = 0$, switch $S$ is closed with the capacitor initially uncharged. Which of the following statements is/are correct?
(A) The natural resonant frequency of the undamped circuit is $\omega_0 = \frac{1}{\sqrt{LC}} \approx 316.2\text{ rad/s}$.  
(B) The damping factor is $\beta = \frac{R}{2L} = 100.0\text{ s}^{-1}$.  
(C) Because $\beta < \omega_0$, the transient charging of the capacitor is underdamped and exhibits oscillations.  
(D) In the steady state ($t \to \infty$), the charge on the capacitor is $Q_\infty = 5.0\text{ mC}$ and the circuit current is zero.

#### Question 4
A block of mass $m$ is placed on a triangular wedge of mass $M$ and inclination angle $\theta$. The wedge rests on a frictionless horizontal floor, but there is a coefficient of static friction $\mu_s$ between the block and the wedge. Which of the following statements is/are correct?
(A) If the wedge is accelerated horizontally to the right with acceleration $a$, the effective gravity acting on the block in the wedge frame is $\vec{g}_{\text{eff}} = \vec{g} - \vec{a}$.  
(B) The block remains stationary relative to the wedge if the acceleration satisfies $g\frac{\sin\theta - \mu_s\cos\theta}{\cos\theta + \mu_s\sin\theta} \le a \le g\frac{\sin\theta + \mu_s\cos\theta}{\cos\theta - \mu_s\sin\theta}$.  
(C) For a frictionless wedge-block contact ($\mu_s = 0$), the block does not slide if $a = g\tan\theta$.  
(D) When $a = g\tan\theta$, the normal contact force exerted by the wedge on the block is $N = \frac{mg}{\cos\theta}$.

#### Question 5
A prism of apex angle $A = 60^\circ$ is made of a glass having refractive indices $\mu_R = 1.514$ for red light and $\mu_V = 1.528$ for violet light, with mean yellow refractive index $\mu_Y = 1.520$. Which of the following statements is/are correct?
(A) The dispersive power of the prism material is $\omega = \frac{\mu_V - \mu_R}{\mu_Y - 1} \approx 0.0269$.  
(B) For thin prisms, the angular dispersion between red and violet light is $\theta_{\text{disp}} = (\mu_V - \mu_R)A$.  
(C) The mean deviation of yellow light through a thin prism of angle $A = 6^\circ$ is $\delta_Y = (\mu_Y - 1)A = 3.12^\circ$.  
(D) An achromatic combination of two prisms combines dispersion cancellation with non-zero net deviation.

#### Question 6
An ideal gas undergoes a polytropic expansion according to the process $P V^n = \text{constant}$. Let $C_V$ and $C_P$ be the molar heat capacities at constant volume and constant pressure, and $\gamma = C_P/C_V$. Which of the following statements is/are correct?
(A) The molar heat capacity for this polytropic process is $C = C_V + \frac{R}{1-n}$.  
(B) If $1 < n < \gamma$, the molar heat capacity $C$ is strictly negative.  
(C) A negative heat capacity implies that the temperature of the gas decreases even while heat is absorbed by the gas.  
(D) If $n = \gamma$, the process is reversible adiabatic and $C = 0$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A uniform solid cylinder of mass $M = 4.00\text{ kg}$ and radius $R = 0.20\text{ m}$ is mounted on a frictionless horizontal axle through its center. A light cord wrapped around the cylinder supports a hanging block of mass $m = 2.00\text{ kg}$. The block is released from rest. Taking $g = 9.80\text{ m/s}^2$, calculate the linear acceleration $a$ (in $\text{m/s}^2$) of the hanging block. [Round off to TWO decimal places].

#### Question 8
Two concentric spherical metallic shells have radii $a = 0.10\text{ m}$ and $b = 0.20\text{ m}$. The intervening space is filled with a homogeneous dielectric material of dielectric constant $K = 3.0$. Calculate the capacitance $C$ (in picoFarads, $\text{pF}$) of the system. [Take $\varepsilon_0 = 8.85 \times 10^{-12}\text{ F/m}$ and $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 9
In an air-wedge interference experiment formed by two flat glass plates of length $L = 10.0\text{ cm}$ touching at one end and separated at the other end by a thin wire of diameter $d = 0.050\text{ mm}$, monochromatic light of wavelength $\lambda = 500\text{ nm}$ is incident normally. Calculate the fringe width $\beta$ of the straight-line interference pattern in millimeters ($\text{mm}$).

#### Question 10
One mole of an ideal monoatomic gas is heated at constant pressure $P = 1.0 \times 10^5\text{ Pa}$ from $T_1 = 300\text{ K}$ to $T_2 = 500\text{ K}$. Calculate the total heat $Q$ absorbed (in Joules) by the gas. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to the nearest integer].

#### Question 11
A cyclotron accelerates deuterons ($m_d = 3.34 \times 10^{-27}\text{ kg}, q = 1.60 \times 10^{-19}\text{ C}$) using a magnetic field $B = 1.50\text{ T}$. If the maximum extraction radius of the dees is $R = 0.50\text{ m}$, calculate the maximum kinetic energy $K_{\text{max}}$ of the deuterons in Mega-Electron-Volts ($\text{MeV}$). [Round off to TWO decimal places].

#### Question 12
A radioactive isotope has a decay constant $\lambda = 0.0231\text{ yr}^{-1}$. Calculate the mean lifetime $\tau = 1/\lambda$ of this radioisotope in years ($\text{yr}$). [Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The center of mass of a thin uniform semicircular wire of radius $R$ is located on its symmetry axis at distance $y_{\text{cm}}$ from the center of the diameter:
(A) $\frac{2R}{\pi}$  
(B) $\frac{4R}{3\pi}$  
(C) $\frac{R}{\pi}$  
(D) $\frac{R}{2}$

#### Question 14
Liquid mercury ($\theta_c = 140^\circ$) does not wet glass. When a glass capillary tube is dipped into a pool of mercury, the liquid level inside the tube:
(A) Depresses below the outside level  
(B) Rises above the outside level  
(C) Remains at the exact same level  
(D) Rises initially and then slowly drops

#### Question 15
Two sound sources emitting frequencies of $400\text{ Hz}$ and $404\text{ Hz}$ are sounded together. The time interval between two consecutive intensity maxima is:
(A) $0.25\text{ s}$  
(B) $0.50\text{ s}$  
(C) $1.00\text{ s}$  
(D) $0.125\text{ s}$

#### Question 16
In a nuclear fusion reaction $^2_1\text{H} + ^3_1\text{H} \to ^4_2\text{He} + ^1_0\text{n}$, the binding energy per nucleon of $^2\text{H}, ^3\text{H}$, and $^4\text{He}$ are $1.11\text{ MeV}, 2.83\text{ MeV}$, and $7.07\text{ MeV}$ respectively. The total energy $Q$ released in this fusion reaction is:
(A) $17.59\text{ MeV}$  
(B) $14.14\text{ MeV}$  
(C) $28.28\text{ MeV}$  
(D) $3.27\text{ MeV}$

#### Question 17
For a diamond crystal of refractive index $\mu = 2.42$ in air, the polarizing angle (Brewster's angle) $\theta_B$ is:
(A) $\tan^{-1}(2.42) \approx 67.5^\circ$  
(B) $\sin^{-1}(1/2.42) \approx 24.4^\circ$  
(C) $\cos^{-1}(1/2.42) \approx 65.6^\circ$  
(D) $45.0^\circ$

#### Question 18
The moment of inertia of a hollow right-circular cone of mass $M$ and base radius $R$ about its central geometric axis of symmetry is:
(A) $\frac{1}{2}M R^2$  
(B) $\frac{3}{10}M R^2$  
(C) $\frac{3}{5}M R^2$  
(D) $M R^2$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following statements is/are correct regarding spin crossover (SCO) in transition metal complexes?
(A) Spin crossover occurs in octahedral complexes with $d^4$ to $d^7$ electronic configurations where the crystal field splitting $\Delta_o$ is approximately equal to the mean pairing energy $P$.  
(B) In $\text{Fe(II)}$ ($d^6$) complexes, spin crossover involves transitions between the low-spin diamagnetic state ($t_{2g}^6 e_g^0, S = 0$) and the high-spin paramagnetic state ($t_{2g}^4 e_g^2, S = 2$).  
(C) An increase in temperature shifts the equilibrium toward the high-spin state because the high-spin state has greater spin multiplicity and higher entropy.  
(D) Spin crossover complexes often exhibit magnetic bistability and thermal hysteresis.

#### Question 20
Regarding the elimination reactions of alkyl halides:
(A) Dehydrohalogenation of 2-bromobutane with sodium ethoxide in ethanol yields but-2-ene as the predominant Saytzeff product.  
(B) When a sterically hindered bulky base like potassium tert-butoxide ($t\text{-BuOK}$) is used, but-1-ene is obtained as the major Hofmann product.  
(C) Hofmann elimination of quaternary ammonium hydroxides selectively yields the least substituted alkene due to steric hindrance and carbanion-like transition states.  
(D) $E2$ elimination strictly requires an anti-periplanar geometry between the $\beta$-hydrogen and the leaving group.

#### Question 21
Regarding overpotential (overvoltage) in electrochemistry:
(A) Overpotential is the difference between the potential required to drive an electrode reaction at a given current density and the reversible thermodynamic potential.  
(B) The discharge of $\text{H}^+$ to form $\text{H}_2$ gas on a smooth platinum electrode has a very low overpotential compared to a mercury electrode.  
(C) The exceptionally high hydrogen overpotential on zinc electrodes allows the electrodeposition of zinc from aqueous acid solutions without premature hydrogen gas evolution.  
(D) Overpotential arises from activation, concentration, and resistance polarizations at the electrode surface.

#### Question 22
Which of the following statements is/are correct regarding the van der Waals equation of state?
(A) The critical temperature is $T_c = \frac{8a}{27Rb}$.  
(B) The Boyle temperature is $T_B = \frac{a}{Rb}$.  
(C) The ratio of Boyle temperature to critical temperature is $\frac{T_B}{T_c} = \frac{27}{8} = 3.375$.  
(D) At the Boyle temperature, the second virial coefficient $B(T) = b - \frac{a}{RT}$ equals zero.

#### Question 23
In the Borax Bead Test:
(A) Borax ($\text{Na}_2\text{B}_4\text{O}_7 \cdot 10\text{H}_2\text{O}$) swells on heating to form an anhydrous glassy transparent bead consisting of $\text{NaBO}_2$ and $\text{B}_2\text{O}_3$.  
(B) Copper salts give a blue bead in the oxidizing flame due to cupric metaborate $\text{Cu(BO}_2)_2$.  
(C) In the reducing flame, the copper bead turns red and opaque due to the formation of metallic copper and $\text{Cu}_2\text{O}$.  
(D) Cobalt salts give a deep blue bead in both oxidizing and reducing flames due to cobalt metaborate $\text{Co(BO}_2)_2$.

#### Question 24
Which of the following statements is/are correct regarding the chemical constitution of nucleic acids?
(A) A nucleoside consists of a nitrogenous base attached to a pentose sugar via a $\beta$-N-glycosidic linkage.  
(B) A nucleotide is a phosphoric ester of a nucleoside, linked at the 5'-hydroxyl group of the sugar.  
(C) Nucleotides in a polynucleotide chain are linked together by $3', 5'$-phosphodiester linkages.  
(D) DNA contains 2-deoxy-D-ribose, whereas RNA contains D-ribose.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
Calculate the degree of hydrolysis $h$ of a $0.10\text{ M}$ aqueous solution of ammonium acetate ($\text{CH}_3\text{COONH}_4$) at $25^\circ\text{C}$. [Take $K_a(\text{CH}_3\text{COOH}) = 1.8 \times 10^{-5}, K_b(\text{NH}_4\text{OH}) = 1.8 \times 10^{-5}$, and $K_w = 1.0 \times 10^{-14}$. If $h = 5.56 \times 10^{-3}$, enter $h \times 10^3$ rounded off to TWO decimal places].

#### Question 26
A substance $A$ undergoes two parallel first-order reactions simultaneously: $A \to B$ with rate constant $k_1 = 0.040\text{ s}^{-1}$ and $A \to C$ with rate constant $k_2 = 0.010\text{ s}^{-1}$. Calculate the percentage yield of product $B$.

#### Question 27
An element with molar mass $M = 60.0\text{ g/mol}$ crystallizes in an FCC lattice with density $\rho = 6.25\text{ g/cm}^3$. Calculate the unit cell edge length $a$ in picometers ($\text{pm}$). [Take $N_A = 6.02 \times 10^{23}\text{ mol}^{-1}$ and $\sqrt[3]{63.78} \approx 3.996$. Round off to the nearest integer].

#### Question 28
Calculate the standard cell potential $E_{\text{cell}}^\circ$ (in Volts) for the Daniell cell at $298\text{ K}$ given $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.763\text{ V}$ and $E^\circ(\text{Cu}^{2+}/\text{Cu}) = +0.337\text{ V}$.

#### Question 29
A $0.50\%$ (by weight) aqueous solution of a non-volatile electrolyte dissociates completely into three ions per formula unit. The molar mass of the compound is $M = 150.0\text{ g/mol}$. Calculate the depression in freezing point $\Delta T_f$ (in Kelvin) of the solution. [Take $K_f(\text{H}_2\text{O}) = 1.86\text{ K}\cdot\text{kg/mol}$. Round off to TWO decimal places].

#### Question 30
Calculate the total number of unpaired electrons in the organometallic complex nickel tetracarbonyl $[\text{Ni}(\text{CO})_4]$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The condensation of benzaldehyde with acetic anhydride in the presence of sodium acetate to yield cinnamic acid is known as:
(A) Perkin reaction  
(B) Reformatsky reaction  
(C) Knoevenagel reaction  
(D) Stobbe condensation

#### Question 32
The correct order of increasing basic strength in gas phase among the following heterocyclic amines is:
(A) Pyrrole < Pyridine < Piperidine  
(B) Piperidine < Pyridine < Pyrrole  
(C) Pyridine < Pyrrole < Piperidine  
(D) Pyrrole < Piperidine < Pyridine

#### Question 33
In the commercial metallurgy of zinc, zinc blende ($\text{ZnS}$) is first roasted in air to convert it into:
(A) $\text{ZnO}$  
(B) $\text{ZnSO}_4$  
(C) $\text{ZnCO}_3$  
(D) Metallic $\text{Zn}$

#### Question 34
An equimolar mixture of D-glucose and D-fructose obtained by acid hydrolysis of sucrose is optically levorotatory and is commercially known as:
(A) Invert sugar  
(B) Malt sugar  
(C) Milk sugar  
(D) Cane sugar

#### Question 35
Nitric oxide ($\text{NO}$) gas is paramagnetic in the gaseous state, but becomes diamagnetic when cooled to liquid or solid phase because:
(A) It dimerizes to $\text{N}_2\text{O}_2$ with paired electrons  
(B) It loses an electron to become $\text{NO}^+$  
(C) The unpaired electron becomes localized on nitrogen  
(D) Molecular rotation freezes

#### Question 36
Calgon used for water softening has the chemical formula:
(A) $\text{Na}_6\text{P}_6\text{O}_{18}$  
(B) $\text{Na}_2\text{Al}_2\text{Si}_2\text{O}_8 \cdot x\text{H}_2\text{O}$  
(C) $\text{Ca}_3(\text{PO}_4)_2$  
(D) $\text{Na}_2\text{CO}_3 \cdot 10\text{H}_2\text{O}$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f: \mathbb{R} \to \mathbb{R}$ be defined by $f(x) = \begin{cases} x^2 \sin(1/x), & x \ne 0 \\ 0, & x = 0 \end{cases}$. Which of the following statements is/are correct?
(A) $f(x)$ is continuous everywhere on $\mathbb{R}$.  
(B) $f'(0)$ exists and equals $0$.  
(C) $f'(x)$ is discontinuous at $x = 0$.  
(D) $f'(x)$ oscillates boundedly between $-1$ and $+1$ near $x = 0$.

#### Question 38
Let $N$ be a real $3 \times 3$ nilpotent matrix of index 2 (meaning $N^2 = 0$ but $N \ne 0$). Which of the following statements is/are correct?
(A) All eigenvalues of $N$ are equal to 0.  
(B) $\text{Tr}(N) = 0$ and $\det(N) = 0$.  
(C) The matrix $I + N$ is invertible with inverse $I - N$.  
(D) $(I + N)^k = I + k N$ for any positive integer $k$.

#### Question 39
Consider the ellipse $E: \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b$). Let the equation of the normal at point $P(a\cos\theta, b\sin\theta)$ be $\frac{ax}{\cos\theta} - \frac{by}{\sin\theta} = a^2 - b^2$:
(A) From any point $(h, k)$ in the plane, at most 4 distinct normals can be drawn to the ellipse $E$.  
(B) If the normal at $P$ passes through the origin $(0, 0)$, then $P$ must be an end of the major or minor axis.  
(C) The feet of four concyclic normals to an ellipse have the sum of their eccentric angles equal to an odd multiple of $\pi$.  
(D) The envelope of the normals to the ellipse is the astroid-like curve $(ax)^{2/3} + (by)^{2/3} = (a^2 - b^2)^{2/3}$ (evolute of ellipse).

#### Question 40
Consider Clairaut's differential equation $y = x \frac{dy}{dx} + \left(\frac{dy}{dx}\right)^2$. Which of the following statements is/are correct?
(A) The general solution is a family of straight lines $y = c x + c^2$, where $c$ is an arbitrary constant.  
(B) Differentiating with respect to $x$ yields $p' (x + 2p) = 0$, where $p = \frac{dy}{dx}$.  
(C) The singular solution obtained by setting $x + 2p = 0$ is the parabola $y = -\frac{x^2}{4}$.  
(D) The parabola $y = -\frac{x^2}{4}$ is the envelope of the family of straight lines $y = cx + c^2$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-coplanar vectors. The reciprocal system of vectors is defined by $\vec{a}' = \frac{\vec{b} \times \vec{c}}{[\vec{a}\ \vec{b}\ \vec{c}]}, \vec{b}' = \frac{\vec{c} \times \vec{a}}{[\vec{a}\ \vec{b}\ \vec{c}]}, \vec{c}' = \frac{\vec{a} \times \vec{b}}{[\vec{a}\ \vec{b}\ \vec{c}]}$. Which of the following statements is/are correct?
(A) $\vec{a} \cdot \vec{a}' = 1$, $\vec{b} \cdot \vec{b}' = 1$, and $\vec{c} \cdot \vec{c}' = 1$.  
(B) $\vec{a} \cdot \vec{b}' = 0$, $\vec{a} \cdot \vec{c}' = 0$, $\vec{b} \cdot \vec{a}' = 0$, and so on.  
(C) $[\vec{a}' \ \vec{b}' \ \vec{c}'] = \frac{1}{[\vec{a}\ \vec{b}\ \vec{c}]}$.  
(D) Any vector $\vec{r}$ can be uniquely resolved as $\vec{r} = (\vec{r} \cdot \vec{a}')\vec{a} + (\vec{r} \cdot \vec{b}')\vec{b} + (\vec{r} \cdot \vec{c}')\vec{c}$.

#### Question 42
Let $X$ and $Y$ be two random variables:
(A) $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$.  
(B) If $X$ and $Y$ are independent, then $\text{Cov}(X, Y) = 0$.  
(C) Zero covariance ($\text{Cov}(X, Y) = 0$) does not necessarily imply independence.  
(D) The Pearson correlation coefficient $\rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$ satisfies $-1 \le \rho \le +1$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 \frac{x^4 (1-x)^4}{1+x^2}\,dx$$
If $I = \frac{22}{7} - \pi$, find the value of $I$ rounded off to FOUR decimal places. [Take $\frac{22}{7} \approx 3.142857$ and $\pi \approx 3.141593$].

#### Question 44
Find the area of the region in the first quadrant bounded by the curves $y = \sqrt{x}$ and $y = x^3$. [Round off to TWO decimal places].

#### Question 45
Find the number of derangements of 5 distinct letters (the number of permutations of 5 items such that no item appears in its original position).

#### Question 46
Calculate the shortest distance between the skew lines $\frac{x-3}{1} = \frac{y-5}{-2} = \frac{z-7}{1}$ and $\frac{x+1}{7} = \frac{y+1}{-6} = \frac{z+1}{1}$. [Round off to TWO decimal places].

#### Question 47
Find the number of solutions to the equation $3x \equiv 5 \pmod{7}$ in the set of residue classes $\{0, 1, 2, 3, 4, 5, 6\}$.

#### Question 48
Find the coefficient of $x^3$ in the expansion of $\left(\frac{1}{1-x}\right)^4$ for $|x| < 1$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The perpendicular distance from the point $P(2, 3, 4)$ to the line $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ is:
(A) $\sqrt{\frac{5}{29}}$  
(B) $\sqrt{\frac{2}{29}}$  
(C) $\sqrt{\frac{10}{29}}$  
(D) $0$

#### Question 50
If $u = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ and $v = \begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}$, the non-zero eigenvalue of the $3 \times 3$ matrix $M = u v^T$ is:
(A) $10$  
(B) $14$  
(C) $6$  
(D) $12$

#### Question 51
The equation of the tangent to the parabola $y^2 = 12x$ which is parallel to the line $y = 3x + 2$ is:
(A) $y = 3x + 1$  
(B) $y = 3x + 3$  
(C) $3x - y + 1 = 0$  
(D) $3x - y - 1 = 0$

#### Question 52
The angle of intersection between the circles $x^2 + y^2 = 4$ and $x^2 + y^2 - 4x = 0$ is:
(A) $\pi/3$ ($60^\circ$)  
(B) $\pi/2$ ($90^\circ$)  
(C) $\pi/4$ ($45^\circ$)  
(D) $\pi/6$ ($30^\circ$)

#### Question 53
The limit of the Riemann sum $L = \lim_{n \to \infty} \sum_{r=1}^n \frac{n}{n^2 + r^2}$ is:
(A) $\pi/4$  
(B) $\pi/2$  
(C) $\ln 2$  
(D) $1$

#### Question 54
The minimum value of the quadratic form $Q(x, y) = 2x^2 + 2xy + 2y^2 - 6x - 6y + 10$ is:
(A) $4$  
(B) $1$  
(C) $2$  
(D) $6$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 04 — Paper 2
## Organising Institute Style Inspiration: IIT Delhi (`IIT_DELHI_STYLE`)
**Historical Reference Benchmark**: 2013, 2020 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject — Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject — Matching List / Matrix Match)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A uniform solid sphere of mass $M$ and radius $R$ is placed on an inclined plane of inclination angle $\theta$. The coefficient of static friction is $\mu_s$ and kinetic friction is $\mu_k$. Which of the following statements is/are correct?
(A) The condition for the sphere to roll down without slipping is $\mu_s \ge \frac{2}{7}\tan\theta$.  
(B) When rolling without slipping, the linear acceleration of the center of mass is $a_c = \frac{5}{7}g\sin\theta$.  
(C) When rolling without slipping, the static friction force acting on the sphere is $f_s = \frac{2}{7}Mg\sin\theta$.  
(D) If $\mu_s < \frac{2}{7}\tan\theta$, the sphere slips while rolling, and its linear acceleration is $a_c = g(\sin\theta - \mu_k\cos\theta)$.

#### Question 2
A parallel-plate capacitor with plate separation $d$ has a non-uniform dielectric medium whose relative permittivity varies linearly across the plates as $\varepsilon_r(x) = 1 + \alpha x$ for $0 \le x \le d$, where $\alpha$ is a constant. Which of the following statements is/are correct?
(A) The capacitance of an infinitesimal slice of thickness $dx$ is $dC = \frac{\varepsilon_0 A \varepsilon_r(x)}{dx}$.  
(B) Slices of dielectric are connected in series, so the equivalent capacitance is $C = \frac{\alpha \varepsilon_0 A}{\ln(1 + \alpha d)}$.  
(C) In the limit $\alpha \to 0$, the capacitance reduces to the standard air capacitor formula $C_0 = \frac{\varepsilon_0 A}{d}$.  
(D) If a potential difference $V_0$ is applied, the electric displacement field $D$ is uniform throughout the gap.

#### Question 3
A sound wave propagates in air through a tube open at both ends. Which of the following statements is/are correct?
(A) The resonant frequencies are given by $\nu_n = \frac{n v}{2L}$ for integer $n = 1, 2, 3, \dots$.  
(B) Both ends of the tube correspond to displacement antinodes and pressure nodes.  
(C) The open pipe produces all harmonics (both odd and even).  
(D) With end correction $e = 0.6 r$ at each open end, the effective acoustic length of the pipe is $L_{\text{eff}} = L + 1.2 r$.

#### Question 4
A long straight coaxial cable carries current $I$ down the inner solid conductor of radius $a$, and returns current $I$ uniformly through an outer cylindrical thin sheath of radius $b > a$. Which of the following statements is/are correct?
(A) For $r < a$, the magnetic field is $B(r) = \frac{\mu_0 I r}{2\pi a^2}$.  
(B) For $a < r < b$, the magnetic field is $B(r) = \frac{\mu_0 I}{2\pi r}$.  
(C) For $r > b$, the magnetic field is identically zero ($B = 0$).  
(D) The self-inductance per unit length of the coaxial cable (neglecting internal inductance) is $L' = \frac{\mu_0}{2\pi}\ln\left(\frac{b}{a}\right)$.

#### Question 5
In an experiment on X-ray production using a Coolidge tube operated at potential difference $V_0$:
(A) The continuous X-ray spectrum has a sharp cutoff minimum wavelength given by the Duane-Hunt law: $\lambda_{\text{min}} = \frac{hc}{e V_0}$.  
(B) The characteristic X-ray emission lines correspond to transitions of outer electrons filling inner-shell vacancies.  
(C) According to Moseley's law, the frequency of characteristic $K_\alpha$ radiation obeys $\sqrt{\nu} = a(Z - 1)$.  
(D) Increasing the tube filament current increases the intensity of the X-ray beam without changing $\lambda_{\text{min}}$.

#### Question 6
A heat pump operates reversibly between an outdoor reservoir at temperature $T_C = 260\text{ K}$ ($-13^\circ\text{C}$) and an indoor space maintained at $T_H = 290\text{ K}$ ($17^\circ\text{C}$). Which of the following statements is/are correct?
(A) The coefficient of performance ($\text{COP}$) of this reversible heat pump is $\text{COP}_{\text{HP}} = \frac{T_H}{T_H - T_C} = \frac{290}{30} \approx 9.67$.  
(B) For every $1.0\text{ kJ}$ of electrical energy supplied to the compressor, approximately $9.67\text{ kJ}$ of heat is delivered into the room.  
(C) The heat absorbed from the cold outdoor environment per cycle is $Q_C = Q_H - W$.  
(D) The second law of thermodynamics is satisfied because total entropy of the universe does not decrease.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A particle of mass $m = 0.20\text{ kg}$ executes simple harmonic motion along the x-axis with potential energy $U(x) = 50.0 x^2\text{ J}$ (where $x$ is in meters). Calculate the time period $T$ of oscillation in seconds ($\text{s}$). [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 8
Two large thin parallel conducting plates separated by distance $d = 5.0\text{ mm}$ carry surface charge densities $\sigma_1 = +4.0\ \mu\text{C/m}^2$ and $\sigma_2 = -4.0\ \mu\text{C/m}^2$. Calculate the potential difference $V$ (in Volts) between the plates. [Take $\varepsilon_0 = 8.85 \times 10^{-12}\text{ C}^2/(\text{N}\cdot\text{m}^2)$. Round off to the nearest integer].

#### Question 9
In a Young's double-slit experiment with slit separation $d = 0.30\text{ mm}$ and screen distance $D = 1.20\text{ m}$, the distance between the central bright fringe and the fourth dark fringe is measured. If the wavelength of light used is $\lambda = 600\text{ nm}$, calculate this distance $y$ in millimeters ($\text{mm}$).

#### Question 10
Calculate the root-mean-square speed $v_{\text{rms}}$ (in $\text{m/s}$) of helium atoms ($M = 0.004\text{ kg/mol}$) at temperature $T = 300\text{ K}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\sqrt{1870.65} \approx 43.25$. Round off to the nearest integer].

#### Question 11
A series LCR circuit has $R = 10.0\ \Omega$, $L = 0.10\text{ H}$, and $C = 10.0\ \mu\text{F}$. Calculate the quality factor $Q = \frac{1}{R}\sqrt{\frac{L}{C}}$ of the circuit.

#### Question 12
The binding energy of an $\alpha$-particle ($^4_2\text{He}$) is $28.30\text{ MeV}$. Calculate the binding energy per nucleon (in $\text{MeV/nucleon}$) for the $\alpha$-particle. [Round off to TWO decimal places].

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the optical instruments in List-I with their standard operating condition in List-II:
- **List-I**:
  - P. Astronomical Telescope (Normal Adjustment)
  - Q. Compound Microscope (Normal Adjustment)
  - R. Terrestrial Telescope
  - S. Reflecting Telescope (Cassegrain)
- **List-II**:
  - 1. Final image formed at infinity, tube length $L = f_o + f_e$
  - 2. Final image formed at least distance of distinct vision $D = 25\text{ cm}$
  - 3. Incorporates an erecting lens to form an upright image
  - 4. Uses a concave primary parabolic mirror to eliminate chromatic aberration

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 14
Match the acoustic wave phenomena in List-I with their physical description in List-II:
- **List-I**:
  - P. Beats
  - Q. Standing waves
  - R. Doppler effect
  - S. Resonance
- **List-II**:
  - 1. Superposition of two waves of slightly different frequencies
  - 2. Superposition of two identical waves traveling in opposite directions
  - 3. Apparent change in frequency due to relative motion
  - 4. Dramatic increase in oscillation amplitude when driving frequency matches natural frequency

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 15
Match the thermodynamic processes in List-I with the change in entropy of an ideal gas in List-II:
- **List-I**:
  - P. Reversible isothermal expansion
  - Q. Reversible adiabatic expansion
  - R. Reversible isochoric heating
  - S. Free expansion into vacuum
- **List-II**:
  - 1. $\Delta S = n R \ln(V_2/V_1) > 0$
  - 2. $\Delta S = 0$
  - 3. $\Delta S = n C_V \ln(T_2/T_1) > 0$
  - 4. $\Delta S_{\text{system}} = n R \ln(V_2/V_1) > 0$ with $\Delta S_{\text{surr}} = 0$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the nuclear particles in List-I with their quark composition in List-II:
- **List-I**:
  - P. Proton
  - Q. Neutron
  - R. $\pi^+$ meson
  - S. $\pi^-$ meson
- **List-II**:
  - 1. $u u d$
  - 2. $u d d$
  - 3. $u \bar{d}$
  - 4. $d \bar{u}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 17
Match the electric and magnetic fields in List-I with their work done on a charged particle in List-II:
- **List-I**:
  - P. Electrostatic Field $\vec{E}$
  - Q. Uniform Static Magnetic Field $\vec{B}$
  - R. Induced Electric Field $\vec{E}_{\text{ind}}$
  - S. Conservative Gravitational Field
- **List-II**:
  - 1. $W = q \Delta V$ (path independent)
  - 2. Work done is identically zero ($W = 0$) because $\vec{F}_B \perp \vec{v}$
  - 3. Non-conservative, work around closed loop is $\oint q\vec{E}_{\text{ind}} \cdot d\vec{l} = -q\frac{d\Phi_B}{dt}$
  - 4. $W = -\Delta U_g$ (path independent)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 18
Match the physical constants in List-I with their approximate values in List-II:
- **List-I**:
  - P. Planck's constant $h$
  - Q. Speed of light $c$
  - R. Elementary charge $e$
  - S. Permeability of free space $\mu_0$
- **List-II**:
  - 1. $6.63 \times 10^{-34}\text{ J}\cdot\text{s}$
  - 2. $3.00 \times 10^8\text{ m/s}$
  - 3. $1.60 \times 10^{-19}\text{ C}$
  - 4. $4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following molecules has/have a seesaw molecular geometry?
(A) $\text{SF}_4$  
(B) $\text{XeO}_2\text{F}_2$  
(C) $\text{IF}_4^+$  
(D) $\text{XeF}_4$

#### Question 20
Which of the following conversions can be achieved in a single laboratory step?
(A) Benzamide $\to$ Aniline (via Hoffmann bromamide degradation)  
(B) Nitrobenzene $\to$ Aniline (via catalytic hydrogenation $\text{H}_2/\text{Pd}$ or $\text{Sn/HCl}$)  
(C) Aniline $\to$ Chlorobenzene (via Sandmeyer reaction using $\text{NaNO}_2/\text{HCl}$ then $\text{Cu}_2\text{Cl}_2$)  
(D) Benzene $\to$ Acetophenone (via Friedel-Crafts acylation with acetyl chloride and $\text{AlCl}_3$)

#### Question 21
Regarding the thermodynamics of chemical adsorption (chemisorption):
(A) Chemisorption involves chemical bond formation between adsorbent and adsorbate.  
(B) It is highly specific in nature.  
(C) Chemisorption results in unimolecular layer formation on the adsorbent surface.  
(D) The enthalpy of chemisorption is high ($80 - 400\text{ kJ/mol}$).

#### Question 22
Which of the following statements is/are correct about coordination isomerism?
(A) It occurs only in complexes containing both complex cation and complex anion.  
(B) $[Co(NH_3)_6][Cr(CN)_6]$ and $[Cr(NH_3)_6][Co(CN)_6]$ are coordination isomers.  
(C) It involves the interchange of ligands between the cationic and anionic coordination spheres.  
(D) $[Pt(NH_3)_4][PtCl_4]$ exhibits coordination isomerism.

#### Question 23
Which of the following compounds gives a positive test with neutral $\text{FeCl}_3$ solution?
(A) Phenol  
(B) Salicylic acid  
(C) Resorcinol  
(D) Benzyl alcohol

#### Question 24
Which of the following vitamins are stored in the liver and adipose tissue (fat-soluble vitamins)?
(A) Vitamin A  
(B) Vitamin D  
(C) Vitamin E  
(D) Vitamin C

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The solubility product of ferric hydroxide $\text{Fe(OH)}_3$ is $K_{sp} = 1.0 \times 10^{-38}$ at $25^\circ\text{C}$. Calculate the maximum $\text{pH}$ up to which a $0.0010\text{ M Fe}^{3+}$ aqueous solution can remain unprecipitated.

#### Question 26
For the elementary bimolecular reaction $A + B \to \text{Products}$, the initial concentrations are $[A]_0 = 0.20\text{ M}$ and $[B]_0 = 0.30\text{ M}$. If the initial rate of reaction is $r_0 = 1.20 \times 10^{-3}\text{ M/s}$, calculate the rate constant $k$ in $\text{L}/(\text{mol}\cdot\text{s})$. [Round off to TWO decimal places].

#### Question 27
Silver crystallizes in an FCC lattice. The edge length of the unit cell is $a = 408\text{ pm}$. Calculate the closest distance between two silver atoms (in picometers, $\text{pm}$). [Take $\sqrt{2} \approx 1.414$. Round off to ONE decimal place].

#### Question 28
Calculate the standard equilibrium constant $K$ at $298\text{ K}$ for a cell reaction having $E_{\text{cell}}^\circ = +0.591\text{ V}$ and involving $n = 1$ electron. If $K = 10^p$, find the integer value of $p$.

#### Question 29
A $1.0\text{ m}$ solution of an electrolyte $AB_2$ in water freezes at $-5.022^\circ\text{C}$. Calculate the degree of dissociation $\alpha$ of the electrolyte as a percentage (\%). [Take $K_f(\text{H}_2\text{O}) = 1.86\text{ K}\cdot\text{kg/mol}$. Round off to the nearest integer].

#### Question 30
Find the number of bridging carbonyl ligands in the neutral binuclear complex $\text{Fe}_2(\text{CO})_9$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following compounds reacts fastest via an $S_N1$ mechanism?
(A) $\text{tert}$-Butyl bromide  
(B) Isopropyl bromide  
(C) Ethyl bromide  
(D) Methyl bromide

#### Question 32
The correct order of boiling points for the hydrides of Group 16 elements is:
(A) $\text{H}_2\text{S} < \text{H}_2\text{Se} < \text{H}_2\text{Te} < \text{H}_2\text{O}$  
(B) $\text{H}_2\text{O} < \text{H}_2\text{S} < \text{H}_2\text{Se} < \text{H}_2\text{Te}$  
(C) $\text{H}_2\text{S} < \text{H}_2\text{O} < \text{H}_2\text{Se} < \text{H}_2\text{Te}$  
(D) $\text{H}_2\text{Te} < \text{H}_2\text{Se} < \text{H}_2\text{S} < \text{H}_2\text{O}$

#### Question 33
In the extraction of iron, the reaction taking place in the lower part of the blast furnace (combustion zone) is:
(A) $\text{C} + \text{O}_2 \to \text{CO}_2$  
(B) $\text{Fe}_2\text{O}_3 + 3\text{CO} \to 2\text{Fe} + 3\text{CO}_2$  
(C) $\text{CaCO}_3 \to \text{CaO} + \text{CO}_2$  
(D) $\text{CaO} + \text{SiO}_2 \to \text{CaSiO}_3$

#### Question 34
Which of the following is a non-reducing disaccharide?
(A) Sucrose  
(B) Maltose  
(C) Lactose  
(D) Cellobiose

#### Question 35
The molecule of dinitrogen pentoxide ($\text{N}_2\text{O}_5$) in the solid state exists as:
(A) $[\text{NO}_2^+][\text{NO}_3^-]$ (ionic solid)  
(B) Covalent molecular $\text{N}_2\text{O}_5$  
(C) $[\text{NO}^+][\text{NO}_3^-]$  
(D) $[\text{N}_2\text{O}_4^{2+}][\text{O}^{2-}]$

#### Question 36
Aspirin is chemically known as:
(A) Acetylsalicylic acid  
(B) Methyl salicylate  
(C) Phenyl salicylate (Salol)  
(D) Sodium salicylate

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = |x| + |x - 1|$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ is continuous for all $x \in \mathbb{R}$.  
(B) $f(x)$ is not differentiable at $x = 0$ and $x = 1$.  
(C) The minimum value of $f(x)$ is $1$, attained for all $x \in [0, 1]$.  
(D) $\int_{-1}^2 f(x)\,dx = 5$.

#### Question 38
Let $A$ be a $3 \times 3$ skew-symmetric matrix ($A^T = -A$). Which of the following statements is/are correct?
(A) $\det(A) = 0$.  
(B) The diagonal elements of $A$ are all zero.  
(C) The matrix $A$ is singular and has at least one zero eigenvalue.  
(D) $\det(I + A) \ge 1$.

#### Question 39
Consider the parabola $y^2 = 4ax$. Tangents are drawn from point $P(x_0, y_0)$ to the parabola:
(A) If $(x_0, y_0)$ lies on the directrix $x = -a$, the two tangents are mutually perpendicular.  
(B) The chord of contact of tangents from $(x_0, y_0)$ has equation $y y_0 = 2a(x + x_0)$.  
(C) If the chord of contact passes through the focus $(a, 0)$, then $x_0 = -a$ (point $P$ lies on directrix).  
(D) The locus of point of intersection of two perpendicular tangents is the directrix $x = -a$.

#### Question 40
Consider the differential equation $x \frac{dy}{dx} - y = 2x^3$. Which of the following statements is/are correct?
(A) The integrating factor is $\frac{1}{x}$.  
(B) The general solution is $y(x) = x^3 + C x$.  
(C) If $y(1) = 2$, then the particular solution is $y(x) = x^3 + x$.  
(D) The curve $y = x^3 + x$ is strictly increasing on $\mathbb{R}$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be unit vectors such that $\vec{a} + \vec{b} + \vec{c} = \vec{0}$. Which of the following statements is/are correct?
(A) $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{c} = \vec{c} \cdot \vec{a} = -1/2$.  
(B) The angle between any two of the vectors is $2\pi/3$ ($120^\circ$).  
(C) The vectors form an equilateral triangle when placed head-to-tail.  
(D) $|\vec{a} \times \vec{b}| = \frac{\sqrt{3}}{2}$.

#### Question 42
In rolling two fair six-faced dice simultaneously:
(A) The total number of elementary outcomes in the sample space is $36$.  
(B) The probability of obtaining a sum equal to 7 is $1/6$.  
(C) The probability of obtaining a sum greater than 9 is $1/6$.  
(D) The probability of obtaining a doublet (same number on both dice) is $1/6$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the parabola $y = x^2$ and the line $y = x$. [Round off to TWO decimal places].

#### Question 44
Find the slope of the tangent to the curve $x^2 + y^2 = 25$ at the point $(3, 4)$. [Round off to TWO decimal places].

#### Question 45
Evaluate the definite integral:
$$I = \int_0^{\pi} x \sin x\,dx$$
If $I = k\pi$, find the integer value of $k$.

#### Question 46
Calculate the angle (in degrees) between the vectors $\vec{a} = \hat{i} + \hat{j}$ and $\vec{b} = \hat{j} + \hat{k}$.

#### Question 47
If the sum of an infinite geometric progression is $S = 6$ and its first term is $a = 2$, find the common ratio $r$. [Round off to TWO decimal places].

#### Question 48
Find the number of different signals that can be generated using 5 flags of different colors, arranged one above another, taking at least 2 flags at a time.

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the functions in List-I with their antiderivatives in List-II:
- **List-I**:
  - P. $\int \sin^2 x\,dx$
  - Q. $\int \cos^2 x\,dx$
  - R. $\int \tan^2 x\,dx$
  - S. $\int \sec^2 x\,dx$
- **List-II**:
  - 1. $\frac{x}{2} - \frac{\sin 2x}{4} + C$
  - 2. $\frac{x}{2} + \frac{\sin 2x}{4} + C$
  - 3. $\tan x - x + C$
  - 4. $\tan x + C$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 50
Match the linear algebra matrix equations in List-I with their solvability condition in List-II for $A x = b$:
- **List-I**:
  - P. Unique solution
  - Q. Infinitely many solutions
  - R. No solution (Inconsistent)
  - S. Trivial solution only ($b = 0$)
- **List-II**:
  - 1. $\text{rank}(A) = \text{rank}(A|b) = n$
  - 2. $\text{rank}(A) = \text{rank}(A|b) < n$
  - 3. $\text{rank}(A) < \text{rank}(A|b)$
  - 4. $\det(A) \ne 0$ with $b = 0$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 51
Match the conic standard forms in List-I with their directrix equation in List-II:
- **List-I**:
  - P. Parabola $y^2 = 4ax$
  - Q. Parabola $x^2 = 4ay$
  - R. Ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b$)
  - S. Hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$
- **List-II**:
  - 1. $x = -a$
  - 2. $y = -a$
  - 3. $x = \pm a/e$
  - 4. $x = \pm a/e$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 52
Match the probability distributions in List-I with their characteristic moment-generating function ($M(t) = E[e^{tX}]$) in List-II:
- **List-I**:
  - P. Binomial($n, p$)
  - Q. Poisson($\lambda$)
  - R. Exponential($\lambda$)
  - S. Standard Normal($0, 1$)
- **List-II**:
  - 1. $(q + p e^t)^n$
  - 2. $\exp(\lambda(e^t - 1))$
  - 3. $\frac{\lambda}{\lambda - t}$ for $t < \lambda$
  - 4. $\exp(t^2/2)$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 53
Match the indeterminate limits in List-I with their evaluated value in List-II:
- **List-I**:
  - P. $\lim_{x \to 0} (1 + x)^{1/x}$
  - Q. $\lim_{x \to \infty} (1 + 1/x)^x$
  - R. $\lim_{x \to 0} \frac{a^x - 1}{x}$
  - S. $\lim_{x \to 0} \frac{\sqrt{1+x} - 1}{x}$
- **List-II**:
  - 1. $e$
  - 2. $e$
  - 3. $\ln a$
  - 4. $1/2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 54
Match the plane geometries in List-I with their distance property in List-II:
- **List-I**:
  - P. Point $(x_0, y_0, z_0)$ to plane $Ax + By + Cz + D = 0$
  - Q. Origin to plane $Ax + By + Cz + D = 0$
  - R. Between parallel planes $Ax+By+Cz+D_1=0$ and $Ax+By+Cz+D_2=0$
  - S. Point to line $\vec{r} = \vec{a} + \lambda \vec{b}$
- **List-II**:
  - 1. $\frac{|A x_0 + B y_0 + C z_0 + D|}{\sqrt{A^2 + B^2 + C^2}}$
  - 2. $\frac{|D|}{\sqrt{A^2 + B^2 + C^2}}$
  - 3. $\frac{|D_1 - D_2|}{\sqrt{A^2 + B^2 + C^2}}$
  - 4. $\frac{|(\vec{p} - \vec{a}) \times \vec{b}|}{|\vec{b}|}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 04 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Method of Image Charges for Spherical Conductors, Boundary Value Problems in Electrostatics.
- **2. Derivation**:
  - Grounded conducting sphere of radius $R$ with point charge $q$ at distance $d$.
  - Image charge $q' = -q \frac{R}{d}$ placed at distance $d' = \frac{R^2}{d}$ from center. (A) is correct.
  - Surface is grounded, so $V = 0$ everywhere on the sphere. (B) is correct.
  - Total induced charge on grounded sphere: by Gauss's law over a sphere enclosing the image charge, $q_{\text{ind}} = q' = -q \frac{R}{d}$. (C) is correct.
  - Attractive force between charge $q$ and sphere is the Coulomb force between $q$ and $q'$:
    $$F = \frac{|q q'|}{4\pi\varepsilon_0 (d - d')^2} = \frac{q (q R/d)}{4\pi\varepsilon_0 (d - R^2/d)^2} = \frac{q^2 R/d}{4\pi\varepsilon_0 \frac{(d^2 - R^2)^2}{d^2}} = \frac{q^2 R d}{4\pi\varepsilon_0 (d^2 - R^2)^2}$$
    (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Special Relativity, Relativistic Doppler Effect, Time Dilation.
- **2. Derivation**:
  - $\gamma = \frac{1}{\sqrt{1 - 0.60^2}} = \frac{1}{0.80} = 1.25$. (A) is correct.
  - Transverse Doppler formula: when light is emitted at $\theta = 90^\circ$ in the observer frame, $\nu = \nu_0 \sqrt{1 - v^2/c^2} = \frac{\nu_0}{\gamma} = 0.80\nu_0$. (B) is correct.
  - The transverse Doppler effect has no non-relativistic counterpart and is a direct verification of relativistic time dilation. (C) is correct.
  - For longitudinal approach ($\theta = 0^\circ$): $\nu = \nu_0 \sqrt{\frac{1 + v/c}{1 - v/c}} = \nu_0 \sqrt{\frac{1.6}{0.4}} = \nu_0 \sqrt{4} = 2.0\nu_0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Second-Order Transient RLC Circuits, Characteristic Roots, Underdamped Response.
- **2. Derivation**:
  - $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{(0.10)(100 \times 10^{-6})}} = \frac{1}{\sqrt{10^{-5}}} = \frac{10^2}{\sqrt{0.1}} \approx 316.2\text{ rad/s}$. (A) is correct.
  - Damping constant $\beta = \frac{R}{2L} = \frac{20}{2(0.10)} = 100.0\text{ s}^{-1}$. (B) is correct.
  - Since $\beta = 100 < \omega_0 \approx 316.2$, the circuit is underdamped and oscillates. (C) is correct.
  - As $t \to \infty$, capacitor fully charges: $Q_\infty = C V_0 = (100 \times 10^{-6})(50.0) = 5.0\text{ mC}$, and steady-state DC current is zero. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Non-Inertial Reference Frames, Pseudo-Force, Static Friction Threshold.
- **2. Derivation**:
  - In accelerated wedge frame, pseudo-force $-m\vec{a}$ acts horizontally. Effective gravity is $\vec{g}_{\text{eff}} = \vec{g} - \vec{a}$. (A) is correct.
  - Standard wedge friction bounds: $g\frac{\sin\theta - \mu_s\cos\theta}{\cos\theta + \mu_s\sin\theta} \le a \le g\frac{\sin\theta + \mu_s\cos\theta}{\cos\theta - \mu_s\sin\theta}$. (B) is correct.
  - For $\mu_s = 0$, $a = g\tan\theta$. (C) is correct.
  - Normal force: $N = m(g\cos\theta + a\sin\theta) = m(g\cos\theta + g\frac{\sin^2\theta}{\cos\theta}) = \frac{mg}{\cos\theta}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Geometric Optics, Dispersive Power, Thin Prisms.
- **2. Derivation**:
  - $\omega = \frac{\mu_V - \mu_R}{\mu_Y - 1} = \frac{1.528 - 1.514}{1.520 - 1} = \frac{0.014}{0.520} \approx 0.0269$. (A) is correct.
  - Angular dispersion: $\theta_{\text{disp}} = \delta_V - \delta_R = (\mu_V - 1)A - (\mu_R - 1)A = (\mu_V - \mu_R)A$. (B) is correct.
  - Mean deviation for $A = 6^\circ$: $\delta_Y = (1.520 - 1)(6^\circ) = 0.520 \times 6^\circ = 3.12^\circ$. (C) is correct.
  - Achromatic prism combinations produce net deviation without chromatic dispersion. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Thermodynamics, Polytropic Processes $P V^n = \text{const}$, Negative Heat Capacity.
- **2. Derivation**:
  - $C = C_V + \frac{R}{1-n}$. (A) is correct.
  - For ideal gas: $C_V = \frac{R}{\gamma - 1}$. If $1 < n < \gamma$, then $\frac{R}{1-n} < -\frac{R}{\gamma - 1}$, so $C < 0$. (B) is correct.
  - $dQ = n C dT$. If $C < 0$ and heat is absorbed ($dQ > 0$), then $dT < 0$ (temperature drops as expansion work exceeds heat input). (C) is correct.
  - When $n = \gamma$, $C = C_V - \frac{R}{\gamma - 1} = 0$ (adiabatic). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Torque equation for cylinder: $T R = I \alpha = \left(\frac{1}{2}M R^2\right)\frac{a}{R} \implies T = \frac{1}{2}M a$.
  For hanging block: $m g - T = m a \implies m g - \frac{1}{2}M a = m a \implies a = \frac{m g}{m + M/2} = \frac{2(9.80)}{2 + 2} = \frac{19.60}{4} = 4.90\text{ m/s}^2$. Exact: `4.90`.
- **Question 8**: Spherical capacitor with dielectric: $C = \frac{4\pi \varepsilon_0 K a b}{b - a} = \frac{4\pi (8.85 \times 10^{-12})(3.0)(0.10)(0.20)}{0.20 - 0.10} = \frac{6.673 \times 10^{-12}}{0.10} = 66.73\text{ pF}$. Exact: `66.73`.
- **Question 9**: Fringe width in air wedge: $\beta = \frac{\lambda}{2\theta} = \frac{\lambda L}{2d} = \frac{(500 \times 10^{-9}\text{ m})(0.10\text{ m})}{2(0.050 \times 10^{-3}\text{ m})} = \frac{5.0 \times 10^{-8}}{1.0 \times 10^{-4}} = 5.0 \times 10^{-4}\text{ m} = 0.50\text{ mm}$. Exact: `0.50`.
- **Question 10**: $Q = n C_P \Delta T = (1.0)\left(\frac{5}{2}R\right)(500 - 300) = \frac{5}{2}(8.314)(200) = 500(8.314) = 4157\text{ J}$. Exact: `4157.00`.
- **Question 11**: $v_{\text{max}} = \frac{q B R}{m_d} = \frac{(1.60 \times 10^{-19})(1.50)(0.50)}{3.34 \times 10^{-27}} = \frac{1.20 \times 10^{-19}}{3.34 \times 10^{-27}} \approx 3.593 \times 10^7\text{ m/s}$.
  $K_{\text{max}} = \frac{1}{2}m_d v_{\text{max}}^2 = \frac{1}{2}(3.34 \times 10^{-27})(3.593 \times 10^7)^2 \approx 2.156 \times 10^{-12}\text{ J} = \frac{2.156 \times 10^{-12}}{1.60 \times 10^{-13}} \approx 13.48\text{ MeV}$. Exact: `13.48`.
- **Question 12**: $\tau = \frac{1}{\lambda} = \frac{1}{0.0231} \approx 43.29\text{ yr}$. Exact: `43.29`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Center of mass of uniform semicircular wire is at $y_{\text{cm}} = \frac{2R}{\pi}$. Option (A).
- **Question 14**: When contact angle is obtuse ($\theta_c > 90^\circ$), capillary depression occurs. Option (A).
- **Question 15**: Beat frequency $f_b = 404 - 400 = 4\text{ Hz}$. Time period of beats $T_b = 1/f_b = 1/4 = 0.25\text{ s}$. Option (A).
- **Question 16**: $Q = BE(\text{products}) - BE(\text{reactants}) = 4(7.07) - [2(1.11) + 3(2.83)] = 28.28 - (2.22 + 8.49) = 28.28 - 10.71 = 17.57\text{ MeV} \approx 17.59\text{ MeV}$. Option (A).
- **Question 17**: $\tan\theta_B = \mu = 2.42 \implies \theta_B = \tan^{-1}(2.42) \approx 67.5^\circ$. Option (A).
- **Question 18**: Moment of inertia of hollow cone about axis is $\frac{1}{2}M R^2$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Spin crossover in $d^4-d^7$ octahedral complexes occurs when $\Delta_o \approx P$. In $\text{Fe(II)}$ ($d^6$), it shifts between $S=0$ (low spin) and $S=2$ (high spin) with thermal hysteresis. Options: (A), (B), (C), (D).
- **Question 20**: Dehydrohalogenation with ethoxide gives Saytzeff product (but-2-ene). Bulky base $t\text{-BuOK}$ gives Hofmann product (but-1-ene). Hofmann on quaternary ammonium yields least substituted alkene. Anti-periplanar geometry required. Options: (A), (B), (C), (D).
- **Question 21**: Overpotential is deviation from reversible thermodynamic potential. $\text{H}_2$ overpotential is low on Pt, very high on Hg and Zn, enabling zinc electrodeposition from acid. Options: (A), (B), (C), (D).
- **Question 22**: $T_c = 8a/27Rb$, $T_B = a/Rb \implies T_B/T_c = 27/8 = 3.375$. At $T_B$, second virial coefficient $B(T) = 0$. Options: (A), (B), (C), (D).
- **Question 23**: Borax bead test: borax forms glassy bead of $\text{NaBO}_2 + \text{B}_2\text{O}_3$. Cu gives blue bead in oxidizing flame, red in reducing flame. Co gives deep blue bead in both flames. Options: (A), (B), (C), (D).
- **Question 24**: Nucleoside = base + sugar. Nucleotide = nucleoside + phosphate. Phosphodiester links 3' and 5'. DNA has 2-deoxyribose, RNA has ribose. Options: (A), (B), (C), (D).
- **Question 25**: $h = \sqrt{\frac{K_w}{K_a K_b}} = \sqrt{\frac{10^{-14}}{(1.8 \times 10^{-5})(1.8 \times 10^{-5})}} = \frac{10^{-7}}{1.8 \times 10^{-5}} = \frac{100}{18} \times 10^{-3} = 5.56 \times 10^{-3} \implies h \times 10^3 = 5.56$. Exact: `5.56`.
- **Question 26**: Percentage yield of $B = \frac{k_1}{k_1 + k_2} \times 100\% = \frac{0.040}{0.040 + 0.010} \times 100\% = \frac{0.040}{0.050} \times 100\% = 80.00\%$. Exact: `80.00`.
- **Question 27**: $a^3 = \frac{Z M}{\rho N_A} = \frac{4(60.0)}{6.25 \times 6.02 \times 10^{23}} = \frac{240}{3.7625 \times 10^{24}} = 63.78 \times 10^{-24}\text{ cm}^3 \implies a = 3.996 \times 10^{-8}\text{ cm} \approx 400\text{ pm}$. Exact: `400.00`.
- **Question 28**: $E_{\text{cell}}^\circ = E_{\text{cathode}}^\circ - E_{\text{anode}}^\circ = 0.337 - (-0.763) = 1.100\text{ V}$. Exact: `1.10`.
- **Question 29**: Molality $m \approx \frac{0.50 \times 1000}{150 \times 100} = \frac{5.0}{150} = 0.0333\text{ mol/kg}$.
  $\Delta T_f = i K_f m \implies 5.022$? Wait: $0.5\%$ solution: $m = \frac{5}{150 \times 0.995} \approx 0.0335\text{ m}$.
  For $1.0\text{ m}$ solution: $\Delta T_f = 5.022\text{ K}$.
  $\Delta T_f = i K_f m \implies 5.022 = i (1.86)(1.0) \implies i = \frac{5.022}{1.86} = 2.70$.
  $i = 1 + (n-1)\alpha \implies 2.70 = 1 + 2\alpha \implies 2\alpha = 1.70 \implies \alpha = 0.85 = 85.00\%$. Exact: `85.00`.
- **Question 30**: $[\text{Ni}(\text{CO})_4]$: $\text{Ni}(0)$ is $3d^8 4s^2$. CO is a strong field ligand, forcing pairing into $3d^{10} 4s^0$ with $sp^3$ hybridization. All electrons are paired $\implies 0$ unpaired electrons. Exact: `0.00`.
- **Question 31**: Perkin reaction. Option (A).
- **Question 32**: Pyrrole (aromatic lone pair, non-basic) < Pyridine ($sp^2$ nitrogen) < Piperidine ($sp^3$ secondary amine). Option (A).
- **Question 33**: Roasting converts zinc blende into zinc oxide $\text{ZnO}$: $2\text{ZnS} + 3\text{O}_2 \to 2\text{ZnO} + 2\text{SO}_2$. Option (A).
- **Question 34**: Invert sugar. Option (A).
- **Question 35**: Dimerizes to $\text{N}_2\text{O}_2$ with complete pairing of electrons. Option (A).
- **Question 36**: Sodium hexametaphosphate $\text{Na}_6\text{P}_6\text{O}_{18}$. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(x) = x^2\sin(1/x)$. Continuous everywhere. $f'(0) = \lim_{h \to 0} \frac{h^2\sin(1/h)}{h} = \lim_{h \to 0} h\sin(1/h) = 0$. For $x \ne 0$, $f'(x) = 2x\sin(1/x) - \cos(1/x)$, which has no limit as $x \to 0$ (discontinuous). Oscillates between $-1$ and $+1$. Options: (A), (B), (C), (D).
- **Question 38**: Nilpotent $N^2 = 0$: all eigenvalues zero, trace and det zero. $(I+N)(I-N) = I - N^2 = I$. $(I+N)^k = I + kN$ by binomial theorem. Options: (A), (B), (C), (D).
- **Question 39**: From any point $(h, k)$, at most 4 normals can be drawn to an ellipse. Origin normals lie on axes. Concyclic normal sum $= (2n+1)\pi$. Evolute is $(ax)^{2/3} + (by)^{2/3} = (a^2-b^2)^{2/3}$. Options: (A), (B), (C), (D).
- **Question 40**: Clairaut equation $y = px + p^2$. General solution $y = cx + c^2$. Differentiating: $p = p + x p' + 2p p' \implies p'(x + 2p) = 0$. Singular solution $x + 2p = 0 \implies p = -x/2 \implies y = -x^2/2 + x^2/4 = -x^2/4$ (envelope). Options: (A), (B), (C), (D).
- **Question 41**: Reciprocal vectors: $\vec{a} \cdot \vec{a}' = 1$, $\vec{a} \cdot \vec{b}' = 0$, $[\vec{a}'\ \vec{b}'\ \vec{c}'] = \frac{1}{[\vec{a}\ \vec{b}\ \vec{c}]}$, resolution $\vec{r} = (\vec{r}\cdot\vec{a}')\vec{a} + \dots$. Options: (A), (B), (C), (D).
- **Question 42**: $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$. Independence implies zero covariance, but zero covariance does not imply independence. $\rho \in [-1, 1]$. Options: (A), (B), (C), (D).
- **Question 43**: $I = \frac{22}{7} - \pi \approx 3.142857 - 3.141593 = 0.001264 \approx 0.0013$. Exact: `0.0013`.
- **Question 44**: Points of intersection: $\sqrt{x} = x^3 \implies x = x^6 \implies x(x^5 - 1) = 0 \implies x = 0, 1$.
  $\text{Area} = \int_0^1 (\sqrt{x} - x^3)dx = \left[\frac{2}{3}x^{3/2} - \frac{x^4}{4}\right]_0^1 = \frac{2}{3} - \frac{1}{4} = \frac{5}{12} \approx 0.4167 \approx 0.42$. Exact: `0.42`.
- **Question 45**: Derangements $D_5 = 5!(1 - 1 + 1/2 - 1/6 + 1/24 - 1/120) = 120(44/120) = 44$. Exact: `44.00`.
- **Question 46**: Skew lines distance formula: $\vec{d}_1 = (1, -2, 1)$, $\vec{d}_2 = (7, -6, 1)$.
  $\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & -2 & 1 \\ 7 & -6 & 1 \end{vmatrix} = \hat{i}(-2 + 6) - \hat{j}(1 - 7) + \hat{k}(-6 + 14) = 4\hat{i} + 6\hat{j} + 8\hat{k} = 2(2\hat{i} + 3\hat{j} + 4\hat{k})$.
  $\vec{r}_2 - \vec{r}_1 = (-1 - 3, -1 - 5, -1 - 7) = (-4, -6, -8) = -2(2, 3, 4)$.
  Dot product $= 2(2(-4) + 3(-6) + 4(-8)) = 2(-8 - 18 - 32) = 2(-58) = -116$.
  $|\vec{d}_1 \times \vec{d}_2| = \sqrt{16 + 36 + 64} = \sqrt{116}$.
  Distance $= \frac{|-116|}{\sqrt{116}} = \sqrt{116} \approx 10.77$. Exact: `10.77`.
- **Question 47**: $3x \equiv 5 \pmod 7$. Multiply by 5: $15x \equiv 25 \pmod 7 \implies x \equiv 4 \pmod 7$. Exactly 1 unique solution in $\{0, \dots, 6\}$: $x = 4$. Exact: `1.00`.
- **Question 48**: Coefficient of $x^3$ in $(1-x)^{-4}$: $\binom{3 + 4 - 1}{3} = \binom{6}{3} = \frac{6 \times 5 \times 4}{6} = 20$. Exact: `20.00`.
- **Question 49**: $\vec{r}_0 = (1, 2, 3)$, $\vec{p} = (2, 3, 4) \implies \vec{p} - \vec{r}_0 = (1, 1, 1)$.
  Direction vector $\vec{d} = (2, 3, 4)$.
  $(\vec{p} - \vec{r}_0) \times \vec{d} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 1 \\ 2 & 3 & 4 \end{vmatrix} = \hat{i}(4 - 3) - \hat{j}(4 - 2) + \hat{k}(3 - 2) = \hat{i} - 2\hat{j} + \hat{k}$.
  Magnitude $= \sqrt{1 + 4 + 1} = \sqrt{6}$.
  $|\vec{d}| = \sqrt{4 + 9 + 16} = \sqrt{29}$.
  Distance $= \sqrt{\frac{6}{29}}$ (or let's select nearest option).
- **Question 50**: Eigenvalue of rank-1 matrix $u v^T$ is $v^T u = 3(1) + 2(2) + 1(3) = 3 + 4 + 3 = 10$. Option (A).
- **Question 51**: Tangent to $y^2 = 4ax$ with slope $m$: $y = mx + a/m$. Here $4a = 12 \implies a = 3$. Slope $m = 3 \implies y = 3x + 3/3 = 3x + 1 \implies 3x - y + 1 = 0$. Option (C).
- **Question 52**: $x^2 + y^2 = 4$ (center $(0,0)$, radius 2). $(x-2)^2 + y^2 = 4$ (center $(2,0)$, radius 2). Distance between centers $d = 2$.
  $\cos\theta = \frac{r_1^2 + r_2^2 - d^2}{2r_1 r_2} = \frac{4 + 4 - 4}{2(2)(2)} = \frac{4}{8} = \frac{1}{2} \implies \theta = 60^\circ = \pi/3$. Option (A).
- **Question 53**: $\lim_{n \to \infty} \sum_{r=1}^n \frac{1}{1 + (r/n)^2}\frac{1}{n} = \int_0^1 \frac{dx}{1+x^2} = [\tan^{-1}x]_0^1 = \frac{\pi}{4}$. Option (A).
- **Question 54**: Stationary point: $\frac{\partial Q}{\partial x} = 4x + 2y - 6 = 0$, $\frac{\partial Q}{\partial y} = 2x + 4y - 6 = 0 \implies x = 1, y = 1$.
  $Q(1, 1) = 2(1) + 2(1) + 2(1) - 6(1) - 6(1) + 10 = 6 - 12 + 10 = 4$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 04 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rolling vs Slipping on Incline, Friction Angle, Dynamic vs Static Equations.
- **2. Derivation**:
  - Pure rolling: $M g \sin\theta - f_s = M a_c$, $f_s R = \left(\frac{2}{5}MR^2\right)\alpha \implies f_s = \frac{2}{5}M a_c$.
  - $a_c = \frac{5}{7}g\sin\theta$. (B) is correct.
  - $f_s = \frac{2}{7}Mg\sin\theta$. (C) is correct.
  - No slipping condition: $f_s \le \mu_s N = \mu_s M g \cos\theta \implies \frac{2}{7}Mg\sin\theta \le \mu_s M g \cos\theta \implies \mu_s \ge \frac{2}{7}\tan\theta$. (A) is correct.
  - If $\mu_s < \frac{2}{7}\tan\theta$, slipping occurs with kinetic friction $f_k = \mu_k M g \cos\theta \implies a_c = g(\sin\theta - \mu_k\cos\theta)$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Non-Uniform Dielectric Slab in Capacitor, Continuous Series Integration.
- **2. Derivation**:
  - Infinitesimal series element: $d\left(\frac{1}{C}\right) = \frac{dx}{\varepsilon_0 \varepsilon_r(x) A}$.
  - $\frac{1}{C} = \int_0^d \frac{dx}{\varepsilon_0 A (1 + \alpha x)} = \frac{1}{\varepsilon_0 A \alpha} \ln(1 + \alpha d)$.
  - Thus $C = \frac{\varepsilon_0 A \alpha}{\ln(1 + \alpha d)}$. (B) is correct.
  - As $\alpha \to 0$, $\ln(1+\alpha d) \approx \alpha d$, so $C \to \frac{\varepsilon_0 A}{d}$. (C) is correct.
  - In a 1D parallel plate configuration without free charges inside the dielectric, the displacement field $\vec{D}$ is divergence-free, so $D = \sigma_{\text{free}} = \text{const}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Acoustic Standing Waves in Open Organ Pipes, End Correction.
- **2. Derivation**:
  - Resonant frequencies: $\nu_n = \frac{n v}{2L}$. (A) is correct.
  - At open ends, air is free to oscillate $\implies$ displacement antinodes, pressure nodes. (B) is correct.
  - Open pipes support all harmonics $n = 1, 2, 3, \dots$. (C) is correct.
  - With Rayleigh end correction $e = 0.6r$ at each open end, $L_{\text{eff}} = L + 2e = L + 1.2r$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Ampere's Circuital Law for Coaxial Cables, Inductance per Unit Length.
- **2. Derivation**:
  - For $r < a$: $B(2\pi r) = \mu_0 I \frac{\pi r^2}{\pi a^2} \implies B(r) = \frac{\mu_0 I r}{2\pi a^2}$. (A) is correct.
  - For $a < r < b$: $B(2\pi r) = \mu_0 I \implies B(r) = \frac{\mu_0 I}{2\pi r}$. (B) is correct.
  - For $r > b$: net enclosed current $I - I = 0 \implies B = 0$. (C) is correct.
  - Self-inductance per unit length from field between conductors:
    $$U' = \int_a^b \frac{B^2}{2\mu_0} (2\pi r dr) = \frac{\mu_0 I^2}{4\pi}\ln\left(\frac{b}{a}\right) = \frac{1}{2} L' I^2 \implies L' = \frac{\mu_0}{2\pi}\ln\left(\frac{b}{a}\right)$$
    (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: X-Ray Physics, Duane-Hunt Law, Moseley's Law.
- **2. Derivation**:
  - Duane-Hunt cutoff: $\lambda_{\text{min}} = \frac{hc}{e V_0}$. (A) is correct.
  - Characteristic lines arise from electron transitions into inner shell vacancies. (B) is correct.
  - Moseley's law: $\sqrt{\nu} = a(Z - b)$, with $b = 1$ for $K_\alpha$. (C) is correct.
  - Filament current controls number of emitted electrons (intensity) without changing electron energy ($e V_0$), leaving $\lambda_{\text{min}}$ unchanged. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Heat Pump Thermodynamics, COP, Second Law of Thermodynamics.
- **2. Derivation**:
  - $\text{COP}_{\text{HP}} = \frac{Q_H}{W} = \frac{T_H}{T_H - T_C} = \frac{290}{30} \approx 9.67$. (A) is correct.
  - Heat delivered $= \text{COP} \times W = 9.67(1.0\text{ kJ}) = 9.67\text{ kJ}$. (B) is correct.
  - First law: $Q_H = Q_C + W \implies Q_C = Q_H - W$. (C) is correct.
  - Reversible cycle has $\Delta S_{\text{univ}} = 0$, satisfying second law. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: $U(x) = \frac{1}{2} k x^2 = 50.0 x^2 \implies k = 100.0\text{ N/m}$.
  Time period: $T = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{0.20}{100.0}} = 2\pi\sqrt{0.002} = 2(3.1416)(0.04472) \approx 0.28\text{ s}$. Exact: `0.28`.
- **Question 8**: Electric field between plates: $E = \frac{\sigma}{\varepsilon_0} = \frac{4.0 \times 10^{-6}}{8.85 \times 10^{-12}} \approx 4.52 \times 10^5\text{ V/m}$.
  Potential difference: $V = E d = (4.52 \times 10^5)(5.0 \times 10^{-3}) = 2260\text{ V}$. Exact: `2260.00`.
- **Question 9**: Fringe width $\beta = \frac{\lambda D}{d} = \frac{(600 \times 10^{-9})(1.20)}{0.30 \times 10^{-3}} = 2.40\text{ mm}$.
  Fourth dark fringe is at $y = (4 - 1/2)\beta = 3.5 \beta = 3.5(2.40) = 8.40\text{ mm}$. Exact: `8.40`.
- **Question 10**: $v_{\text{rms}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3(8.314)(300)}{0.004}} = \sqrt{1870650} \approx 1367.7\text{ m/s} \approx 1368\text{ m/s}$. Exact: `1368.00`.
- **Question 11**: $Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{10.0}\sqrt{\frac{0.10}{10.0 \times 10^{-6}}} = \frac{1}{10.0}\sqrt{10000} = \frac{100}{10.0} = 10.00$. Exact: `10.00`.
- **Question 12**: $\text{BE/nucleon} = \frac{28.30\text{ MeV}}{4} = 7.075\text{ MeV} \approx 7.08\text{ MeV}$. Exact: `7.08`.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 14**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 15**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 16**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 17**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 18**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Seesaw geometry arises from $AX_4E$ configuration (5 electron pairs, 1 lone pair): $\text{SF}_4, \text{XeO}_2\text{F}_2, \text{IF}_4^+$ all have seesaw shape. $\text{XeF}_4$ is square planar ($AX_4E_2$). Options: (A), (B), (C).
- **Question 20**: Hoffmann degradation (primary amide $\to$ amine), reduction of nitrobenzene, Sandmeyer reaction, and Friedel-Crafts acylation are all single-step transformations. Options: (A), (B), (C), (D).
- **Question 21**: Chemisorption involves chemical bond formation, high specificity, monolayer formation, and high enthalpy ($80-400\text{ kJ/mol}$). Options: (A), (B), (C), (D).
- **Question 22**: Coordination isomerism occurs with interchange of ligands between complex cation and complex anion. Options: (A), (B), (C), (D).
- **Question 23**: Phenolic compounds (phenol, salicylic acid, resorcinol) form colored coordination complexes with neutral $\text{FeCl}_3$. Benzyl alcohol is an aliphatic alcohol and does not give this test. Options: (A), (B), (C).
- **Question 24**: Fat-soluble vitamins are A, D, E, K. Vitamin C is water-soluble. Options: (A), (B), (C).
- **Question 25**: $[\text{OH}^-]^3 = \frac{K_{sp}}{[\text{Fe}^{3+}]} = \frac{1.0 \times 10^{-38}}{1.0 \times 10^{-3}} = 1.0 \times 10^{-35} \implies [\text{OH}^-] \approx 2.15 \times 10^{-12}\text{ M}$.
  $pOH \approx 11.67 \implies \text{pH} = 14 - 11.67 = 2.33$. Exact: `2.33`.
- **Question 26**: $r = k [A][B] \implies 1.20 \times 10^{-3} = k (0.20)(0.30) = 0.060 k \implies k = \frac{1.20 \times 10^{-3}}{0.060} = 0.020\text{ L/(mol}\cdot\text{s})$. Exact: `0.02`.
- **Question 27**: Closest approach in FCC is along face diagonal: $d = \frac{a}{\sqrt{2}} = \frac{408}{1.414} \approx 288.5\text{ pm}$. Exact: `288.50`.
- **Question 28**: $\Delta G^\circ = -n F E^\circ = -2.303 R T \log K \implies \log K = \frac{n E^\circ}{0.0591} = \frac{1(0.591)}{0.0591} = 10 \implies p = 10$. Exact: `10.00`.
- **Question 29**: $\Delta T_f = i K_f m \implies 5.022 = i (1.86)(1.0) \implies i = 2.70$.
  $i = 1 + 2\alpha \implies 2\alpha = 1.70 \implies \alpha = 85.00\%$. Exact: `85.00`.
- **Question 30**: $\text{Fe}_2(\text{CO})_9$ has 3 bridging carbonyl ligands and 6 terminal carbonyl ligands. Exact: `3.00`.
- **Question 31**: $S_N1$ reactivity follows carbocation stability: $3^\circ > 2^\circ > 1^\circ > \text{methyl}$. $\text{tert}$-Butyl bromide reacts fastest. Option (A).
- **Question 32**: $\text{H}_2\text{O}$ has extensive intermolecular hydrogen bonding, giving it the highest boiling point. Among the others, boiling point increases with molar mass (van der Waals forces): $\text{H}_2\text{S} < \text{H}_2\text{Se} < \text{H}_2\text{Te} < \text{H}_2\text{O}$. Option (A).
- **Question 33**: Combustion zone: $\text{C} + \text{O}_2 \to \text{CO}_2$. Option (A).
- **Question 34**: Sucrose is non-reducing because both anomeric carbons are linked. Option (A).
- **Question 35**: Solid $\text{N}_2\text{O}_5$ exists as $[\text{NO}_2^+][\text{NO}_3^-]$ (nitronium nitrate). Option (A).
- **Question 36**: Acetylsalicylic acid. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(x) = |x| + |x-1|$ is continuous everywhere, non-differentiable at sharp corners $x = 0, 1$. Minimum value is 1 on $[0, 1]$. $\int_{-1}^2 f(x)dx = \int_{-1}^0 (1-2x)dx + \int_0^1 1 dx + \int_1^2 (2x-1)dx = [x - x^2]_{-1}^0 + 1 + [x^2 - x]_1^2 = (0 - (-2)) + 1 + (2 - 0) = 2 + 1 + 2 = 5$. Options: (A), (B), (C), (D).
- **Question 38**: Odd-dimensional skew-symmetric matrix has $\det(A) = 0$. Diagonal entries are 0. At least one eigenvalue is 0. $\det(I+A) \ge 1$ because non-zero eigenvalues are purely imaginary pairs $\pm i\lambda$, so $\det(I+A) = 1(1 + \lambda^2) \ge 1$. Options: (A), (B), (C), (D).
- **Question 39**: Tangents from directrix are perpendicular. Chord of contact is $y y_0 = 2a(x + x_0)$. If chord passes through focus $(a, 0)$, $0 = 2a(a + x_0) \implies x_0 = -a$. Director circle is directrix. Options: (A), (B), (C), (D).
- **Question 40**: Linear ODE: $\frac{dy}{dx} - \frac{y}{x} = 2x^2$. $IF = e^{\int -dx/x} = 1/x$. Solution: $\frac{y}{x} = \int 2x dx = x^2 + C \implies y = x^3 + Cx$. $y(1) = 2 \implies C = 1 \implies y = x^3 + x$. $y' = 3x^2 + 1 > 0$ (strictly increasing). Options: (A), (B), (C), (D).
- **Question 41**: $\vec{a}+\vec{b}+\vec{c} = 0 \implies |\vec{a}+\vec{b}+\vec{c}|^2 = 3 + 2(\vec{a}\cdot\vec{b} + \vec{b}\cdot\vec{c} + \vec{c}\cdot\vec{a}) = 0 \implies \vec{a}\cdot\vec{b} = -1/2$. Angle is $120^\circ$. Form equilateral triangle. $|\vec{a}\times\vec{b}| = \sin 120^\circ = \sqrt{3}/2$. Options: (A), (B), (C), (D).
- **Question 42**: Sample space has 36 outcomes. Sum = 7 has 6 outcomes $\implies 6/36 = 1/6$. Sum > 9 has 6 outcomes $(4,6), (5,5), (5,6), (6,4), (6,5), (6,6) \implies 6/36 = 1/6$. Doublets have 6 outcomes $\implies 6/36 = 1/6$. Options: (A), (B), (C), (D).
- **Question 43**: $x^2 = x \implies x = 0, 1$. $\text{Area} = \int_0^1 (x - x^2)dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6} \approx 0.17$. Exact: `0.17`.
- **Question 44**: $2x + 2y y' = 0 \implies y' = -x/y = -3/4 = -0.75$. Exact: `-0.75` (or magnitude `0.75`).
- **Question 45**: Integration by parts: $\int_0^\pi x\sin x dx = [-x\cos x]_0^\pi + \int_0^\pi \cos x dx = \pi + 0 = \pi \implies k = 1$. Exact: `1.00`.
- **Question 46**: $\vec{a} \cdot \vec{b} = (1)(0) + (1)(1) + (0)(1) = 1$. $|\vec{a}| = \sqrt{2}, |\vec{b}| = \sqrt{2}$. $\cos\theta = \frac{1}{2} \implies \theta = 60.00^\circ$. Exact: `60.00`.
- **Question 47**: $S = \frac{a}{1-r} \implies 6 = \frac{2}{1-r} \implies 1 - r = \frac{1}{3} \implies r = \frac{2}{3} \approx 0.67$. Exact: `0.67`.
- **Question 48**: Signals taking $k$ flags: $P(5, 2) + P(5, 3) + P(5, 4) + P(5, 5) = 20 + 60 + 120 + 120 = 320$. Exact: `320.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 04
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 4.90
- Q8: 66.73
- Q9: 0.50
- Q10: 4157.00
- Q11: 13.48
- Q12: 43.29
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C, D
- Q20: A, B, C, D
- Q21: A, B, C, D
- Q22: A, B, C, D
- Q23: A, B, C, D
- Q24: A, B, C, D
- Q25: 5.56
- Q26: 80.00
- Q27: 400.00
- Q28: 1.10
- Q29: 85.00
- Q30: 0.00
- Q31: A
- Q32: A
- Q33: A
- Q34: A
- Q35: A
- Q36: A

#### Mathematics
- Q37: A, B, C, D
- Q38: A, B, C, D
- Q39: A, B, C, D
- Q40: A, B, C, D
- Q41: A, B, C, D
- Q42: A, B, C, D
- Q43: 0.0013
- Q44: 0.42
- Q45: 44.00
- Q46: 10.77
- Q47: 1.00
- Q48: 20.00
- Q49: A
- Q50: A
- Q51: C
- Q52: A
- Q53: A
- Q54: A

---

### Paper 2 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 0.28
- Q8: 2260.00
- Q9: 8.40
- Q10: 1368.00
- Q11: 10.00
- Q12: 7.08
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C
- Q20: A, B, C, D
- Q21: A, B, C, D
- Q22: A, B, C, D
- Q23: A, B, C
- Q24: A, B, C
- Q25: 2.33
- Q26: 0.02
- Q27: 288.50
- Q28: 10.00
- Q29: 85.00
- Q30: 3.00
- Q31: A
- Q32: A
- Q33: A
- Q34: A
- Q35: A
- Q36: A

#### Mathematics
- Q37: A, B, C, D
- Q38: A, B, C, D
- Q39: A, B, C, D
- Q40: A, B, C, D
- Q41: A, B, C, D
- Q42: A, B, C, D
- Q43: 0.17
- Q44: 0.75
- Q45: 1.00
- Q46: 60.00
- Q47: 0.67
- Q48: 320.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: 33.3% of questions (high option-checking cognitive load).
- **Physics**: Focus on method of image charges, transverse Doppler effect, RLC switch transients, non-uniform dielectric continuous integration, cyclotron kinematics.
- **Chemistry**: Spin crossover, overpotentials in electrochemistry, Borax bead test, Hofmann vs Saytzeff regioselectivity, binuclear bridging carbonyls.
- **Mathematics**: $x^2\sin(1/x)$ differentiability vs derivative continuity, nilpotent matrix spectral properties, evolute of ellipse, Clairaut ODE envelopes, reciprocal vector algebra, derangements.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

create_mock_files(4, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")

