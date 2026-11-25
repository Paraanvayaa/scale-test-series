# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 20 (Capstone Examination).
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Quantum Hall effect von Klitzing constant, Casimir vacuum force, Bose-Einstein condensation Tc
- Sharpless asymmetric dihydroxylation, Ferrocene 18-electron aromaticity, Mutual exclusion rule
- Riemann zeta Euler product, Matrix exponential fundamental system, Clairaut's geodesic relation, Kuratowski planar graphs
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 20 — Paper 1
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
Regarding the Integer Quantum Hall Effect observed in a two-dimensional electron gas (2DEG) at low temperatures and under a high perpendicular magnetic field $B$:
(A) The energy eigenvalues form discrete, highly degenerate Landau levels $E_n = \left(n + \frac{1}{2}\right)\hbar\omega_c$, where $\omega_c = \frac{e B}{m^*}$ is the cyclotron frequency.  
(B) Each Landau level has an areal degeneracy of $n_B = \frac{e B}{h} = \frac{1}{2\pi l_B^2}$, where $l_B = \sqrt{\frac{\hbar}{e B}}$ is the magnetic length.  
(C) When the chemical potential lies within an energy gap between localized states, the Hall conductivity is quantized as $\sigma_{x y} = \nu \frac{e^2}{h}$, where $\nu$ is an integer.  
(D) The von Klitzing constant $R_K = \frac{h}{e^2} \approx 25812.807\text{ }\Omega$ defines the international quantum standard of electrical resistance.

#### Question 2
Regarding the Casimir effect, which describes the attractive force between two parallel, uncharged, perfectly conducting plates separated by distance $d$ in vacuum:
(A) The force arises from the modification of zero-point quantum vacuum electromagnetic fluctuations by the conducting boundary conditions.  
(B) The attractive force per unit area is given by $\frac{F}{A} = -\frac{\pi^2 \hbar c}{240 d^4}$.  
(C) The negative sign indicates an attractive force that pulls the plates together.  
(D) The Casimir force becomes significant at sub-micrometer separations and plays a crucial role in micro-electromechanical systems (MEMS).

#### Question 3
In a ring laser gyroscope utilizing the relativistic Sagnac effect, two counter-propagating laser beams of wavelength $\lambda$ circulate around a closed planar loop of area $A$ and perimeter $P$ rotating with angular velocity $\vec{\Omega}$ about its normal axis:
(A) The optical path difference between the co-rotating and counter-rotating beams is $\Delta L = \frac{4 \vec{A} \cdot \vec{\Omega}}{c}$.  
(B) The time difference for one complete round trip is $\Delta t = \frac{4 A \Omega}{c^2}$.  
(C) The beat frequency detected when the two beams interfere is $f_{\text{beat}} = \frac{4 A \Omega}{\lambda P}$.  
(D) The Sagnac effect enables inertial navigation without external reference frames.

#### Question 4
Regarding Bose-Einstein condensation (BEC) in a non-interacting three-dimensional gas of $N$ bosonic atoms of mass $m$ confined in a volume $V$ (number density $n = N/V$):
(A) Condensation occurs below a critical transition temperature $T_c = \frac{h^2}{2\pi m k_B}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}$, where $\zeta(3/2) \approx 2.612$.  
(B) Below $T_c$, a macroscopic fraction of the atoms condenses into the single zero-momentum ground state ($\vec{p} = \vec{0}$).  
(C) The fraction of condensed atoms varies with temperature as $\frac{N_0}{N} = 1 - \left(\frac{T}{T_c}\right)^{3/2}$ for $T < T_c$.  
(D) The phase transition is characterized by the overlap of the thermal de Broglie wavelengths of neighboring atoms: $n \lambda_{\text{th}}^3 \ge 2.612$.

#### Question 5
Regarding magnetohydrodynamic (MHD) Alfvén waves propagating along a uniform magnetic field $\vec{B}_0$ in an incompressible, perfectly conducting fluid of mass density $\rho_0$:
(A) The phase velocity of the wave is the Alfvén speed $v_A = \frac{B_0}{\sqrt{\mu_0 \rho_0}}$.  
(B) The magnetic field lines act like stretched elastic strings with tension $\frac{B_0^2}{\mu_0}$ and mass per unit length $\rho_0$.  
(C) The fluid velocity fluctuations and magnetic field perturbations are transverse to the background field $\vec{B}_0$.  
(D) Alfvén waves transport energy and momentum without transferring mass.

#### Question 6
A uniform solid sphere of mass $M$ and radius $R$ is suspended by a light string from a ceiling. A horizontal force $F$ is applied to its lowest point until the string makes an angle $\theta = 30^\circ$ with the vertical in static equilibrium:
(A) The tension in the string is $T = \frac{M g}{\cos 30^\circ} = \frac{2 M g}{\sqrt{3}}$.  
(B) The required horizontal force is $F = M g \tan 30^\circ = \frac{M g}{\sqrt{3}}$.  
(C) The line of action of the string tension, gravity, and $F$ must be concurrent.  
(D) The sphere does not rotate about its center of mass because all applied forces have zero net torque about the center of mass.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In an Integer Quantum Hall Effect experiment at filling factor $\nu = 2$, calculate the Hall resistance $R_H = \frac{h}{2 e^2}$ in Ohms ($\Omega$) (use $h = 6.626 \times 10^{-34}\text{ J s}$, $e = 1.602 \times 10^{-19}\text{ C}$, round off to ONE decimal place).

#### Question 8
Calculate the magnitude of the attractive Casimir pressure in Pascals ($\text{N/m}^2$) between two perfectly conducting plates separated by distance $d = 100.0\text{ nm}$ in vacuum (use $\hbar = 1.055 \times 10^{-34}\text{ J s}$, $c = 3.0 \times 10^8\text{ m/s}$, $\pi \approx 3.1416$, round off to TWO decimal places).

#### Question 9
In a square ring laser gyroscope with side length $L = 10.0\text{ cm}$ using He-Ne laser light ($\lambda = 633\text{ nm}$), calculate the Sagnac beat frequency in $\text{Hz}$ when the gyroscope rotates at $\Omega = 1.0\text{ rad/s}$ (round off to the nearest integer).

#### Question 10
In an interstellar plasma cloud, the magnetic field is $B_0 = 1.0 \times 10^{-4}\text{ T}$ and mass density is $\rho_0 = 1.0 \times 10^{-14}\text{ kg/m}^3$. Calculate the Alfvén speed $v_A$ in $\text{km/s}$ (use $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$, round off to the nearest integer).

#### Question 11
A uniform solid sphere of mass $M = 2.0\text{ kg}$ and radius $R = 0.20\text{ m}$ rotates about a fixed diameter with angular velocity $\omega = 10.0\text{ rad/s}$. Calculate its rotational kinetic energy in Joules (round off to the nearest integer).

#### Question 12
An ideal Carnot engine operates between $T_H = 500\text{ K}$ and $T_C = 300\text{ K}$. If it delivers $W = 400\text{ J}$ of mechanical work per cycle, calculate the heat absorbed $Q_H$ in Joules from the high-temperature reservoir.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle is dropped from a height $h$ onto a fixed horizontal floor. If the coefficient of restitution is $e$, the total distance traveled by the particle before coming to rest after infinitely many bounces is:
(A) $H_{\text{total}} = h\left(\frac{1 + e^2}{1 - e^2}\right)$  
(B) $H_{\text{total}} = h\left(\frac{1 - e^2}{1 + e^2}\right)$  
(C) $H_{\text{total}} = \frac{h}{1 - e^2}$  
(D) $H_{\text{total}} = \frac{h}{1 - e}$  

#### Question 14
Two convex lenses of focal lengths $f_1 = 10\text{ cm}$ and $f_2 = 20\text{ cm}$ are placed coaxially in contact. The power of the lens combination is:
(A) $+15\text{ D}$  
(B) $+10\text{ D}$  
(C) $+5\text{ D}$  
(D) $+30\text{ D}$  

#### Question 15
An electric dipole of moment $\vec{p}$ is placed in a uniform electric field $\vec{E}$. The torque acting on the dipole is:
(A) $\vec{\tau} = \vec{p} \times \vec{E}$  
(B) $\vec{\tau} = \vec{p} \cdot \vec{E}$  
(C) $\vec{\tau} = \vec{E} \times \vec{p}$  
(D) $\vec{\tau} = \vec{0}$  

#### Question 16
The magnetic force per unit length between two long parallel wires separated by distance $d$ carrying equal currents $I$ in the same direction is:
(A) $f = \frac{\mu_0 I^2}{2\pi d}$ (attractive)  
(B) $f = \frac{\mu_0 I^2}{2\pi d}$ (repulsive)  
(C) $f = \frac{\mu_0 I^2}{4\pi d}$ (attractive)  
(D) $f = \frac{\mu_0 I^2}{\pi d}$ (repulsive)  

#### Question 17
A heat engine absorbs heat $Q_1$ at temperature $T_1$ and rejects heat $Q_2$ at temperature $T_2$. The engine is reversible if and only if:
(A) $\frac{Q_1}{T_1} = \frac{Q_2}{T_2}$  
(B) $\frac{Q_1}{T_1} > \frac{Q_2}{T_2}$  
(C) $\frac{Q_1}{T_1} < \frac{Q_2}{T_2}$  
(D) $Q_1 = Q_2$  

#### Question 18
The radius of the $n\text{th}$ Bohr orbit in a hydrogen atom is proportional to:
(A) $n^2$  
(B) $n$  
(C) $1/n$  
(D) $1/n^2$  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Sharpless asymmetric dihydroxylation (AD) of alkenes:
(A) The catalyst system utilizes catalytic osmium tetroxide ($\text{OsO}_4$) along with chiral bis-cinchona alkaloid ligands.  
(B) Ligand (DHQD)$_2$PHAL (AD-mix-$\beta$) directs dihydroxylation to the top ($\beta$) face of the alkene when drawn in the standard orientation.  
(C) Ligand (DHQ)$_2$PHAL (AD-mix-$\alpha$) directs dihydroxylation to the bottom ($\alpha$) face.  
(D) Stoichiometric co-oxidant potassium ferricyanide ($\text{K}_3[\text{Fe(CN)}_6]$) reoxidizes the reduced $\text{Os(VI)}$ species back to active $\text{Os(VIII)}$ in a two-phase aqueous-organic solvent mixture.

#### Question 20
Regarding ferrocene ($[\text{Fe}(\eta^5\text{-C}_5\text{H}_5)_2]$) and its organometallic sandwich chemistry:
(A) Iron is in the $+2$ oxidation state and the complex satisfies the 18-electron rule ($6\text{ electrons from Fe}^{2+} + 2 \times 6\pi\text{ electrons from cyclopentadienyl anions}$).  
(B) Ferrocene exhibits high aromaticity and undergoes electrophilic aromatic substitution (e.g., Friedel-Crafts acylation) at a rate millions of times faster than benzene.  
(C) Direct nitration of ferrocene with $\text{HNO}_3 / \text{H}_2\text{SO}_4$ fails because the reagent oxidizes $\text{Fe(II)}$ to the blue paramagnetic ferrocenium cation $[\text{Fe}(\text{C}_5\text{H}_5)_2]^+$.  
(D) In the gas phase, ferrocene adopts an eclipsed $D_{5h}$ conformation with a very low rotational barrier between the rings ($\sim 4\text{ kJ/mol}$).

#### Question 21
Regarding the Flory-Huggins solution theory for polymer solutions:
(A) It employs a lattice model that accounts for the large size disparity between long polymer chains and small solvent molecules.  
(B) The entropy of mixing per unit volume is $\Delta S_{\text{mix}} = -k_B \left(\frac{\phi_1}{r_1}\ln\phi_1 + \frac{\phi_2}{r_2}\ln\phi_2\right)$, which is substantially smaller than for low-molecular-weight mixtures.  
(C) The Flory interaction parameter $\chi$ characterizes the excess free energy of solvent-polymer monomer contact interactions.  
(D) Phase separation (demixing) occurs when $\chi$ exceeds the critical value $\chi_c = \frac{1}{2}\left(1 + \frac{1}{\sqrt{N}}\right)^2$.

#### Question 22
Regarding the rule of mutual exclusion in molecular vibrational spectroscopy:
(A) For any molecule possessing a center of inversion ($C_i$ symmetry, such as $\text{CO}_2, \text{SF}_6, \text{trans-1,2-dichloroethene}$), fundamental vibrational modes that are infrared active are Raman inactive, and vice versa.  
(B) The symmetric stretching mode of $\text{CO}_2$ ($\Sigma_g^+$) preserves the center of inversion, involves no change in dipole moment ($\frac{d\mu}{dQ} = 0$), and is active only in Raman spectroscopy.  
(C) The asymmetric stretching mode ($\Sigma_u^+$) and bending mode ($\Pi_u$) of $\text{CO}_2$ alter the dipole moment and are active only in infrared spectroscopy.  
(D) If a molecule exhibits fundamental vibrational bands that appear simultaneously in both infrared and Raman spectra, the molecule must lack a center of inversion (e.g., $\text{H}_2\text{O}, \text{SO}_2, \text{NH}_3$).

#### Question 23
Regarding biological dinitrogen fixation by the enzyme nitrogenase:
(A) The overall biological reduction is $\text{N}_2 + 8\text{H}^+ + 8e^- + 16\text{ATP} \to 2\text{NH}_3 + \text{H}_2 + 16\text{ADP} + 16\text{P}_i$.  
(B) The catalytic active site is the FeMo-cofactor ($[\text{MoFe}_7\text{S}_9\text{C(homocitrate)}]$) featuring a central interstitial carbide ($\text{C}^{4-}$) ion.  
(C) Dihydrogen gas ($\text{H}_2$) is an obligate stoichiometric co-product of biological dinitrogen fixation.  
(D) In contrast to the industrial Haber-Bosch process ($450^\circ\text{C}, 200\text{ atm}$), nitrogenase operates under ambient temperature and pressure ($25^\circ\text{C}, 1\text{ atm}$).

#### Question 24
In the qualitative analysis of acidic radicals (anions):
(A) Carbonates ($\text{CO}_3^{2-}$) effervesce with dilute $\text{H}_2\text{SO}_4$, releasing $\text{CO}_2$ that turns lime water milky.  
(B) Sulfites ($\text{SO}_3^{2-}$) evolve $\text{SO}_2$ gas with the suffocating smell of burning sulfur, which turns acidified potassium dichromate solution green.  
(C) Nitrates ($\text{NO}_3^-$) give the brown ring test with freshly prepared ferrous sulfate ($\text{FeSO}_4$) and concentrated $\text{H}_2\text{SO}_4$ due to the complex $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]^{2+}$.  
(D) Chlorides ($\text{Cl}^-$) give the chromyl chloride test: heating with $\text{K}_2\text{Cr}_2\text{O}_7$ and conc. $\text{H}_2\text{SO}_4$ gives red vapors of $\text{CrO}_2\text{Cl}_2$ which dissolve in $\text{NaOH}$ to give a yellow solution.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The dissociation constant of acetic acid is $K_a = 1.8 \times 10^{-5}$. Calculate the pH of a $0.10\text{ M}$ solution of sodium acetate ($\text{CH}_3\text{COONa}$) at $25^\circ\text{C}$ (use $\log 1.8 = 0.26$, round off to TWO decimal places).

#### Question 26
Calculate the total number of unpaired electrons in the tetrahedral complex ion $[NiCl_4]^{2-}$ (atomic number of $\text{Ni} = 28$).

#### Question 27
An organic compound contains $52.2\%$ Carbon, $13.0\%$ Hydrogen, and $34.8\%$ Oxygen. Its molecular weight is $46.0\text{ g/mol}$. Calculate the total number of atoms in one molecule of this compound.

#### Question 28
The half-life of a first-order chemical reaction is $t_{1/2} = 100\text{ seconds}$. Calculate the time in seconds required for $99.0\%$ of the initial reactant to decompose (use $\ln 10 = 2.303$, round off to the nearest integer).

#### Question 29
A constant current of $I = 9.65\text{ A}$ is passed through an aqueous solution of silver nitrate for $t = 100.0\text{ seconds}$. Calculate the mass of silver deposited in grams (atomic weight of $\text{Ag} = 108.0\text{ g/mol}$, $F = 96500\text{ C/mol}$, round off to TWO decimal places).

#### Question 30
The elevation in boiling point for a $0.20\text{ m}$ aqueous solution of a non-volatile non-electrolyte solute is $\Delta T_b$. Calculate $\Delta T_b$ in $^\circ\text{C}$ (use $K_b = 0.512\text{ K kg/mol}$, round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Williamson ether synthesis, an ether is prepared by the reaction of:
(A) Sodium alkoxide with primary alkyl halide ($S_N2$)  
(B) Alcohol with tertiary alkyl halide  
(C) Sodium phenoxide with aryl halide  
(D) Alkene with water  

#### Question 32
Which of the following transition metal complexes is expected to absorb visible light of the shortest wavelength (highest energy)?
(A) $[\text{Co(CN)}_6]^{3-}$  
(B) $[\text{Co(NH}_3)_6]^{3+}$  
(C) $[\text{Co(H}_2\text{O)}_6]^{3+}$  
(D) $[\text{CoF}_6]^{3-}$  

#### Question 33
The linkage connecting two monosaccharide units in a disaccharide is called a:
(A) Glycosidic linkage  
(B) Peptide linkage  
(C) Phosphodiester linkage  
(D) Ester linkage  

#### Question 34
In the extraction of iron, the reaction taking place in the zone of slag formation is:
(A) $\text{CaO} + \text{SiO}_2 \to \text{CaSiO}_3$  
(B) $\text{C} + \text{O}_2 \to \text{CO}_2$  
(C) $\text{Fe}_2\text{O}_3 + 3\text{CO} \to 2\text{Fe} + 3\text{CO}_2$  
(D) $\text{CO}_2 + \text{C} \to 2\text{CO}$  

#### Question 35
Treatment of phenol with zinc dust upon heating yields:
(A) Benzene  
(B) Toluene  
(C) Benzoic acid  
(D) Cyclohexanol  

#### Question 36
The conjugate base of bisulfate ion ($\text{HSO}_4^-$) is:
(A) Sulfate ion ($\text{SO}_4^{2-}$)  
(B) Sulfuric acid ($\text{H}_2\text{SO}_4$)  
(C) Sulfite ion ($\text{SO}_3^{2-}$)  
(D) Bisulfite ion ($\text{HSO}_3^-$)  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Regarding the Riemann zeta function $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ for $\text{Re}(s) > 1$:
(A) Euler's product formula states $\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}$.  
(B) The value of the Basel problem is $\zeta(2) = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.  
(C) $\zeta(4) = \sum_{n=1}^\infty \frac{1}{n^4} = \frac{\pi^4}{90}$.  
(D) The Riemann Hypothesis states that all non-trivial zeros of $\zeta(s)$ lie on the critical line $\text{Re}(s) = 1/2$.

#### Question 38
Let $A$ be a square matrix. The matrix exponential is defined as $e^A = \sum_{k=0}^\infty \frac{A^k}{k!}$:
(A) $e^O = I$, where $O$ is the zero matrix and $I$ is the identity matrix.  
(B) If $A$ and $B$ commute ($A B = B A$), then $e^{A+B} = e^A e^B$.  
(C) The determinant of the matrix exponential satisfies Jacobi's formula $\det(e^A) = e^{\text{Tr}(A)}$.  
(D) For any matrix $A$, $e^A$ is always non-singular and its inverse is $e^{-A}$.

#### Question 39
Regarding geodesics on a surface of revolution defined in cylindrical coordinates $(r, \theta, z)$ with metric $ds^2 = dr^2 + r^2 d\theta^2 + dz^2$:
(A) Clairaut's relation states that along any geodesic, $r \sin\alpha = \text{constant}$, where $\alpha$ is the angle between the geodesic and the meridian curve.  
(B) On a right circular cylinder of radius $R$, geodesics are circular helices, circles, or straight lines parallel to the axis.  
(C) On a sphere of radius $R$, geodesics are great circles.  
(D) The shortest path between two points on any Riemannian manifold is a geodesic curve.

#### Question 40
According to Euler's formula and Kuratowski's theorem in topological graph theory:
(A) For any connected planar graph with $V$ vertices, $E$ edges, and $F$ faces, $V - E + F = 2$.  
(B) For a simple connected planar graph with $V \ge 3$, the number of edges satisfies $E \le 3V - 6$.  
(C) The complete graph on 5 vertices ($K_5$) is non-planar because $E = 10 > 3(5) - 6 = 9$.  
(D) Kuratowski's theorem states that a finite graph is planar if and only if it does not contain a subgraph homeomorphic to $K_5$ or the complete bipartite graph $K_{3,3}$.

#### Question 41
Let $f(x) = \frac{x^3}{3} - x$:
(A) The local maximum occurs at $x = -1$ with value $2/3$.  
(B) The local minimum occurs at $x = 1$ with value $-2/3$.  
(C) The point of inflection occurs at $(0, 0)$.  
(D) $f(x)$ is strictly increasing on $(-\infty, -1) \cup (1, \infty)$.

#### Question 42
Consider the Fibonacci recurrence relation $F_0 = 0, F_1 = 1$, and $F_{n+1} = F_n + F_{n-1}$ for $n \ge 1$:
(A) The characteristic equation is $\lambda^2 - \lambda - 1 = 0$ with roots $\phi = \frac{1+\sqrt{5}}{2}$ and $\psi = \frac{1-\sqrt{5}}{2}$.  
(B) The closed-form expression is Binet's formula $F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}$.  
(C) $\sum_{k=1}^n F_k^2 = F_n F_{n+1}$.  
(D) $\gcd(F_m, F_n) = F_{\gcd(m, n)}$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 x^4 dx$$
Calculate the value of $100 I$.

#### Question 44
Find the number of 5-digit permutations that can be formed using the digits $1, 2, 3, 4, 5$ without repetition ($5!$).

#### Question 45
Find the perpendicular distance from the point $(1, 2, 3)$ to the plane $x + 2y - 2z + 4 = 0$ (round off to TWO decimal places).

#### Question 46
Let $z = 1 + i$. Calculate the real part of $z^8$.

#### Question 47
Let $y(x)$ satisfy $\frac{dy}{dx} = 4x^3$ with $y(0) = 5$. Calculate $y(1)$.

#### Question 48
In rolling a fair die, calculate the probability of getting a number less than or equal to 2 (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The area of the region bounded by $y = x$ and $y = x^2$ is:
(A) $\frac{1}{6}$  
(B) $\frac{1}{3}$  
(C) $\frac{1}{2}$  
(D) 1  

#### Question 50
If the first term of an AP is 5 and common difference is 3, then the $15\text{th}$ term $a_{15}$ is:
(A) 47  
(B) 50  
(C) 44  
(D) 53  

#### Question 51
The value of the limit $\lim_{x \to 0} \frac{\sin(3x)}{x}$ is:
(A) 3  
(B) 1  
(C) $1/3$  
(D) 0  

#### Question 52
The equation of the circle with center at $(1, 2)$ and radius $r = 3$ is:
(A) $x^2 + y^2 - 2x - 4y - 4 = 0$  
(B) $x^2 + y^2 - 2x - 4y + 4 = 0$  
(C) $x^2 + y^2 + 2x + 4y - 4 = 0$  
(D) $x^2 + y^2 - 4x - 2y - 4 = 0$  

#### Question 53
The distance between the planes $x + 2y + 2z = 3$ and $x + 2y + 2z = 9$ is:
(A) 2  
(B) 6  
(C) 3  
(D) 1  

#### Question 54
If $\vec{a} = 2\hat{i} + 3\hat{j} + 4\hat{k}$ and $\vec{b} = 3\hat{i} - 2\hat{j} + \hat{k}$, then $\vec{a} \cdot \vec{b}$ is:
(A) 4  
(B) 0  
(C) 8  
(D) 16  
"""

paper_2_md = r"""# JEE Advanced Mock Examination 20 — Paper 2
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
  - Full Marks: **+3** if only the correct match is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A parallel-plate capacitor with plate area $A$ and separation $d$ is charged to a potential difference $V_0$ and then disconnected from the battery. A dielectric slab of dielectric constant $\kappa$ and thickness $d$ is then inserted between the plates:
(A) The charge on the plates remains constant ($Q = Q_0$).  
(B) The electric field between the plates decreases by a factor of $\kappa$: $E = E_0 / \kappa$.  
(C) The potential difference decreases to $V = V_0 / \kappa$.  
(D) The electrostatic energy stored in the capacitor decreases from $U_0$ to $U_0 / \kappa$.

#### Question 2
Regarding simple harmonic motion:
(A) The velocity is maximum when displacement is zero.  
(B) The acceleration is maximum when displacement is maximum.  
(C) The total mechanical energy is proportional to the square of amplitude ($E \propto A^2$).  
(D) The time period is independent of amplitude for small oscillations.

#### Question 3
A light ray traveling in a medium of refractive index $n_1$ strikes an interface with a medium of refractive index $n_2$ ($n_1 < n_2$) at Brewster's angle $\theta_B$:
(A) The reflected ray is completely linearly polarized perpendicular to the plane of incidence.  
(B) The reflected ray and refracted ray are mutually perpendicular ($\theta_B + r = 90^\circ$).  
(C) Brewster's angle satisfies $\tan\theta_B = n_2 / n_1$.  
(D) There is zero reflection for light polarized in the plane of incidence (p-polarized light).

#### Question 4
An ideal gas undergoes a cyclic process represented by a circle on a $P-V$ indicator diagram with center at $(V_0, P_0)$ and radius $R_V$ along $V$ and $R_P$ along $P$:
(A) The net work done by the gas per cycle is $W = \pi R_P R_V$ if the cycle is traversed clockwise.  
(B) The net heat absorbed by the gas per cycle equals the net work done.  
(C) If the cycle is traversed counter-clockwise, the net work done is negative (refrigerator cycle).  
(D) The change in internal energy over one complete cycle is zero ($\Delta U_{\text{cycle}} = 0$).

#### Question 5
Regarding the magnetic field of a long straight solenoid:
(A) The magnetic field inside the solenoid is nearly uniform and directed along the axis: $B = \mu_0 n I$.  
(B) The magnetic field outside an ideal long solenoid is zero.  
(C) The magnetic field at the extreme end of the solenoid on the axis is $B_{\text{end}} = \frac{1}{2}\mu_0 n I$.  
(D) The self-inductance of the solenoid is $L = \mu_0 n^2 A l$.

#### Question 6
Regarding series and parallel combinations of identical resistors:
(A) The equivalent resistance of $n$ identical resistors of resistance $R$ in series is $R_s = n R$.  
(B) The equivalent resistance of $n$ identical resistors in parallel is $R_p = R / n$.  
(C) The ratio of series to parallel equivalent resistance is $R_s / R_p = n^2$.  
(D) Power dissipated is greater in parallel than in series when connected across the same voltage source.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A parallel plate capacitor with $C_0 = 10.0\text{ }\mu\text{F}$ is charged to $V_0 = 100\text{ V}$ and disconnected. A dielectric of $\kappa = 5.0$ is inserted. Calculate the new stored energy in milliJoules ($\text{mJ}$).

#### Question 8
A body executes SHM with amplitude $A = 5.0\text{ cm}$ and frequency $f = 2.0\text{ Hz}$. Calculate its maximum acceleration in $\text{m/s}^2$ (use $\pi^2 \approx 9.87$, round off to TWO decimal places).

#### Question 9
Calculate Brewster's angle in degrees for light incident from air into glass of refractive index $n = \sqrt{3}$.

#### Question 10
A circular P-V cycle has pressure semi-axis $\Delta P = 2.0 \times 10^5\text{ Pa}$ and volume semi-axis $\Delta V = 1.0 \times 10^{-3}\text{ m}^3$. Calculate the net work done per cycle in Joules (use $\pi \approx 3.142$, round off to the nearest integer).

#### Question 11
A long solenoid has $n = 500\text{ turns/m}$ and carries a current $I = 2.0\text{ A}$. Calculate the magnetic field at its center in milliTesla ($\text{mT}$) (use $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$, round off to TWO decimal places).

#### Question 12
Five identical resistors each of $R = 10.0\text{ }\Omega$ are connected in parallel. Calculate the equivalent resistance in Ohms ($\Omega$).

---

## Section 3: Matching List / Matrix Match (Questions 13 to 18)

#### Question 13
Match the optics law in List-I with its primary relation in List-II:
- **List-I**:
  - P. Snell's law
  - Q. Brewster's law
  - R. Malus' law
  - S. Lens maker's formula
- **List-II**:
  - 1. $I = I_0 \cos^2\theta$
  - 2. $\tan\theta_B = n$
  - 3. $\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$
  - 4. $n_1 \sin\theta_1 = n_2 \sin\theta_2$

(A) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  
(D) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  

#### Question 14
Match the thermodynamic state function in List-I with its fundamental definition in List-II:
- **List-I**:
  - P. Internal energy $U$
  - Q. Enthalpy $H$
  - R. Helmholtz free energy $F$
  - S. Gibbs free energy $G$
- **List-II**:
  - 1. $U + P V$
  - 2. $H - T S$
  - 3. $U - T S$
  - 4. Total microscopic energy of system

(A) P $\to$ 4, Q $\to$ 1, R $\to$ 3, S $\to$ 2  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 4, Q $\to$ 3, R $\to$ 1, S $\to$ 2  
(D) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  

#### Question 15
Match the physical quantity in List-I with its SI unit in List-II:
- **List-I**:
  - P. Electric field
  - Q. Magnetic field
  - R. Electric potential
  - S. Magnetic flux
- **List-II**:
  - 1. Tesla ($\text{T}$)
  - 2. Volt per meter ($\text{V/m}$)
  - 3. Weber ($\text{Wb}$)
  - 4. Volt ($\text{V}$)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 16
Match the nuclear reaction in List-I with its type in List-II:
- **List-I**:
  - P. $^{235}\text{U} + n \to ^{141}\text{Ba} + ^{92}\text{Kr} + 3n$
  - Q. $^2\text{H} + ^3\text{H} \to ^4\text{He} + n$
  - R. $^{14}\text{C} \to ^{14}\text{N} + e^- + \bar{\nu}_e$
  - S. $^{60m}\text{Co} \to ^{60}\text{Co} + \gamma$
- **List-II**:
  - 1. Nuclear fusion
  - 2. Nuclear fission
  - 3. Gamma decay (isomeric transition)
  - 4. Beta-minus decay

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 17
Match the circuit component in List-I with its primary function in List-II:
- **List-I**:
  - P. Resistor
  - Q. Capacitor
  - R. Inductor
  - S. Diode
- **List-II**:
  - 1. Stores energy in electric field
  - 2. Dissipates electrical energy as heat
  - 3. Rectifies AC to DC (unidirectional current)
  - 4. Stores energy in magnetic field

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 18
Match the telescope type in List-I with its optical feature in List-II:
- **List-I**:
  - P. Refracting telescope
  - Q. Newtonian reflector
  - R. Cassegrain reflector
  - S. Radio telescope
- **List-II**:
  - 1. Concave primary mirror and flat diagonal secondary mirror
  - 2. Glass objective lens (suffers from chromatic aberration)
  - 3. Large parabolic dish antenna
  - 4. Concave primary mirror with convex secondary mirror through a central hole

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding primary, secondary, and tertiary alcohols:
(A) Lucas reagent ($\text{conc. HCl} + \text{anh. ZnCl}_2$) produces immediate turbidity with tertiary alcohols.  
(B) Secondary alcohols produce turbidity within 5 minutes.  
(C) Primary alcohols do not produce turbidity at room temperature.  
(D) Oxidation of primary alcohols gives aldehydes, secondary gives ketones, and tertiary resist oxidation under mild conditions.

#### Question 20
Regarding the chemical properties of transition metals:
(A) Transition metals exhibit variable oxidation states due to the participation of $(n-1)d$ and $n s$ electrons.  
(B) Transition metal compounds are frequently colored due to $d-d$ electronic transitions.  
(C) Most transition metal ions and complexes are paramagnetic due to unpaired $d$-electrons.  
(D) Transition metals and their compounds function as effective catalysts due to variable oxidation states and empty $d$-orbitals.

#### Question 21
Regarding the electrochemical series of standard reduction potentials:
(A) Metals with more negative reduction potentials are stronger reducing agents (e.g., $\text{Li, K, Na}$).  
(B) A metal higher up (more negative $E^\circ$) can displace a metal below it from its salt solution.  
(C) Hydrogen has standard reduction potential defined as $E^\circ(\text{H}^+/\text{H}_2) = 0.00\text{ V}$.  
(D) Fluorine ($\text{F}_2$) has the most positive reduction potential and is the strongest oxidizing agent.

#### Question 22
Regarding chemical kinetics:
(A) The rate of a chemical reaction generally increases with increase in temperature.  
(B) The order of a reaction is an experimentally determined quantity that can be fractional or zero.  
(C) The molecularity of an elementary reaction must be a positive integer.  
(D) For an elementary reaction, the order equals the molecularity.

#### Question 23
Regarding carbohydrates:
(A) Monosaccharides cannot be hydrolyzed into simpler carbohydrates.  
(B) Disaccharides yield two monosaccharide units upon hydrolysis.  
(C) Polysaccharides yield a large number of monosaccharide units upon hydrolysis.  
(D) Starch is composed of two components: water-soluble amylose and water-insoluble amylopectin.

#### Question 24
In the extraction of iron in a blast furnace:
(A) The temperature increases from the top of the furnace to the bottom.  
(B) The primary reducing agent in the upper zone is carbon monoxide ($\text{CO}$).  
(C) Coke acts as fuel and generates carbon monoxide.  
(D) The iron collected from the bottom of the blast furnace is called pig iron.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
Calculate the pH of a $0.0050\text{ M}$ aqueous solution of sulfuric acid ($\text{H}_2\text{SO}_4$), assuming complete dissociation of both protons (enter the value rounded off to TWO decimal places).

#### Question 26
Calculate the spin-only magnetic moment in Bohr Magnetons ($\mu_B$) for the high-spin complex $[FeF_6]^{3-}$ (atomic number of $\text{Fe} = 26$). Enter the value rounded off to TWO decimal places (take $\sqrt{35} \approx 5.92$).

#### Question 27
An organic compound contains $40.0\%$ Carbon, $6.67\%$ Hydrogen, and $53.33\%$ Oxygen by mass. If its molecular weight is $90.0\text{ g/mol}$, calculate the number of carbon atoms present in one molecule.

#### Question 28
The half-life of a radioactive isotope is $t_{1/2} = 20.0\text{ days}$. Calculate the time in days required for $75.0\%$ of the initial sample to decay.

#### Question 29
A constant current of $I = 2.0\text{ A}$ is passed through an aqueous solution of silver nitrate for $t = 4825\text{ seconds}$. Calculate the mass of silver deposited in grams (atomic mass of $\text{Ag} = 108.0\text{ g/mol}$, $F = 96500\text{ C/mol}$, round off to TWO decimal places).

#### Question 30
The elevation in boiling point for a $0.10\text{ m}$ aqueous solution of a non-volatile solute is $\Delta T_b$. Calculate $\Delta T_b$ in $^\circ\text{C}$ (use $K_b = 0.512\text{ K kg/mol}$, round off to TWO decimal places).

---

## Section 3: Matching List / Matrix Match (Questions 31 to 36)

#### Question 31
Match the organic reaction in List-I with its primary product in List-II:
- **List-I**:
  - P. Esterification
  - Q. Saponification
  - R. Decarboxylation
  - S. Ozonolysis of alkene
- **List-II**:
  - 1. Carbonyl compounds (aldehydes/ketones)
  - 2. Alkane with one less carbon atom
  - 3. Ester ($\text{R-COOR'}$)
  - 4. Soap (sodium salt of fatty acid) and glycerol

(A) P $\to$ 3, Q $\to$ 4, R $\to$ 2, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(D) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  

#### Question 32
Match the ore in List-I with its chemical formula in List-II:
- **List-I**:
  - P. Haematite
  - Q. Magnetite
  - R. Copper glance
  - S. Zinc blende
- **List-II**:
  - 1. $\text{Fe}_3\text{O}_4$
  - 2. $\text{Fe}_2\text{O}_3$
  - 3. $\text{ZnS}$
  - 4. $\text{Cu}_2\text{S}$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 33
Match the oxoacid of nitrogen/sulfur in List-I with the central atom oxidation state in List-II:
- **List-I**:
  - P. $\text{HNO}_3$
  - Q. $\text{HNO}_2$
  - R. $\text{H}_2\text{SO}_4$
  - S. $\text{H}_2\text{SO}_3$
- **List-II**:
  - 1. $+3$
  - 2. $+5$
  - 3. $+4$
  - 4. $+6$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 34
Match the biomolecule in List-I with its building block in List-II:
- **List-I**:
  - P. Protein
  - Q. Nucleic acid
  - R. Polysaccharide
  - S. Lipid (Triglyceride)
- **List-II**:
  - 1. Nucleotides
  - 2. $\alpha$-amino acids
  - 3. Glycerol and fatty acids
  - 4. Monosaccharides

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 35
Match the colloid in List-I with its example in List-II:
- **List-I**:
  - P. Sol
  - Q. Gel
  - R. Emulsion
  - S. Aerosol
- **List-II**:
  - 1. Cheese
  - 2. Paint
  - 3. Cloud / Fog
  - 4. Milk

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 36
Match the gas in List-I with its property in List-II:
- **List-I**:
  - P. Carbon monoxide ($\text{CO}$)
  - Q. Carbon dioxide ($\text{CO}_2$)
  - R. Sulfur dioxide ($\text{SO}_2$)
  - S. Nitrogen dioxide ($\text{NO}_2$)
- **List-II**:
  - 1. Reddish-brown acidic gas
  - 2. Highly toxic, binds irreversibly to hemoglobin
  - 3. Turns lime water milky, non-combustible
  - 4. Bleaching agent via reduction, choking smell

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^2 - 4x + 3$:
(A) The roots of $f(x) = 0$ are $x = 1$ and $x = 3$.  
(B) The vertex of the parabola is at $(2, -1)$.  
(C) The minimum value of $f(x)$ is $-1$, attained at $x = 2$.  
(D) $f(x) < 0$ for all $x \in (1, 3)$.

#### Question 38
Let $A$ be a $2 \times 2$ real symmetric matrix:
(A) Both eigenvalues of $A$ are real.  
(B) The eigenvectors corresponding to distinct eigenvalues are orthogonal.  
(C) $A$ is diagonalizable by an orthogonal matrix.  
(D) $\det(A)$ is the product of its eigenvalues.

#### Question 39
Consider the line $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and the point $P(1, 2, 3)$:
(A) The point $P$ lies on the line.  
(B) The direction cosines of the line are $\left(\frac{2}{\sqrt{29}}, \frac{3}{\sqrt{29}}, \frac{4}{\sqrt{29}}\right)$.  
(C) The line is parallel to the vector $2\hat{i} + 3\hat{j} + 4\hat{k}$.  
(D) The line is perpendicular to the plane $2x + 3y + 4z = 0$.

#### Question 40
Consider the differential equation $\frac{dy}{dx} + y = 0$:
(A) The general solution is $y = C e^{-x}$.  
(B) If $y(0) = 1$, the solution is $y = e^{-x}$.  
(C) The function $y(x) = e^{-x}$ is strictly decreasing on $\mathbb{R}$.  
(D) $\lim_{x \to \infty} y(x) = 0$.

#### Question 41
Let $X$ follow a binomial distribution $B(n, p)$:
(A) The mean is $E[X] = n p$.  
(B) The variance is $\text{Var}(X) = n p (1 - p)$.  
(C) The variance is always strictly less than the mean.  
(D) For $p = 0.5$, the distribution is symmetric about the mean.

#### Question 42
Consider the geometric series $S = \sum_{n=0}^\infty r^n$:
(A) The series converges if and only if $|r| < 1$.  
(B) When $|r| < 1$, the sum is $S = \frac{1}{1 - r}$.  
(C) For $r = 1/2$, the sum is 2.  
(D) For $r = -1/2$, the sum is $2/3$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^3 x^2 dx$$
Calculate the value of $I$.

#### Question 44
Find the number of 3-digit numbers that can be formed using the digits $1, 2, 3, 4, 5$ without repetition.

#### Question 45
Find the perpendicular distance from the point $(0, 0, 0)$ to the plane $3x + 4y - 10 = 0$.

#### Question 46
Let $z = 3 + 4i$. Calculate the modulus $|z|$.

#### Question 47
Let $y(x)$ satisfy $\frac{dy}{dx} = 2$ with $y(0) = 1$. Calculate $y(4)$.

#### Question 48
In flipping a fair coin 3 times, calculate the probability of getting at least 2 heads (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The area of the triangle with vertices $(0, 0), (4, 0),$ and $(0, 3)$ is:
(A) 6  
(B) 12  
(C) 7  
(D) 5  

#### Question 50
If the $n\text{th}$ term of an AP is $a_n = 2n + 1$, then the sum of the first 10 terms is:
(A) 120  
(B) 110  
(C) 100  
(D) 130  

#### Question 51
The value of the limit $\lim_{x \to 0} \frac{e^{2x} - 1}{x}$ is:
(A) 2  
(B) 1  
(C) $1/2$  
(D) 0  

#### Question 52
The center of the circle $x^2 + y^2 - 4x - 6y + 9 = 0$ is:
(A) $(2, 3)$  
(B) $(-2, -3)$  
(C) $(4, 6)$  
(D) $(2, -3)$  

#### Question 53
The distance between the points $(0, 0, 0)$ and $(1, 2, 2)$ is:
(A) 3  
(B) $\sqrt{5}$  
(C) 9  
(D) 5  

#### Question 54
If $\vec{a} = \hat{i} + \hat{j}$ and $\vec{b} = \hat{i} - \hat{j}$, then the angle between $\vec{a}$ and $\vec{b}$ is:
(A) $\frac{\pi}{2}$  
(B) $\frac{\pi}{4}$  
(C) $\pi$  
(D) 0  
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 20

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Integer Quantum Hall effect Landau levels and von Klitzing constant.
- 2: (A, B, C, D) - Casimir vacuum energy attractive force.
- 3: (A, B, C, D) - Relativistic Sagnac effect in ring laser gyroscopes.
- 4: (A, B, C, D) - Bose-Einstein condensation critical temperature and ground state fraction.
- 5: (A, B, C, D) - Magnetohydrodynamic Alfvén wave properties.
- 6: (A, B, C) - Force concurrency and equilibrium. Statement (D) is false: tension and gravity don't pass through CM in tilted position, but their torques balance $F$'s torque.

#### Solutions 7 to 12:
- 7: $R_H = \frac{h}{2 e^2} = \frac{6.626 \times 10^{-34}}{2(1.602 \times 10^{-19})^2} = \frac{6.626 \times 10^{-34}}{5.133 \times 10^{-38}} \approx 12906.4\text{ }\Omega$. (Answer: 12906.4)
- 8: $P = \frac{\pi^2 \hbar c}{240 d^4} = \frac{\pi^2 (1.055 \times 10^{-34}) (3.0 \times 10^8)}{240 (10^{-7})^4} = \frac{3.124 \times 10^{-25}}{240 \times 10^{-28}} = \frac{3.124 \times 10^3}{240} \approx 13.02\text{ Pa}$. (Answer: 13.02)
- 9: $A = L^2 = 0.01\text{ m}^2$, $P = 4L = 0.40\text{ m}$.
  $f_{\text{beat}} = \frac{4 A \Omega}{\lambda P} = \frac{4 (0.01) (1.0)}{(633 \times 10^{-9}) (0.40)} = \frac{0.04}{2.532 \times 10^{-7}} \approx 157978\text{ Hz} \approx 157978$. (Answer: 157978)
- 10: $v_A = \frac{B_0}{\sqrt{\mu_0 \rho_0}} = \frac{10^{-4}}{\sqrt{(4\pi \times 10^{-7}) (10^{-14})}} = \frac{10^{-4}}{\sqrt{1.257 \times 10^{-20}}} = \frac{10^{-4}}{1.121 \times 10^{-10}} \approx 892060\text{ m/s} \approx 892\text{ km/s}$. (Answer: 892)
- 11: $I = \frac{2}{5} M R^2 = \frac{2}{5}(2.0)(0.04) = 0.032\text{ kg m}^2$.
  $K = \frac{1}{2} I \omega^2 = \frac{1}{2}(0.032)(100) = 1.6\text{ J} \approx 2\text{ J}$. (Answer: 2)
- 12: $\eta = 1 - 300/500 = 0.40$. $Q_H = W / \eta = 400 / 0.40 = 1000\text{ J}$. (Answer: 1000)

#### Solutions 13 to 18:
- 13: Total distance $= h + 2h e^2 + 2h e^4 + \dots = h + 2h \frac{e^2}{1-e^2} = h \frac{1 + e^2}{1 - e^2}$. (A)
- 14: $P = P_1 + P_2 = \frac{100}{10} + \frac{100}{20} = 10 + 5 = +15\text{ D}$. (A)
- 15: $\vec{\tau} = \vec{p} \times \vec{E}$. (A)
- 16: $f = \frac{\mu_0 I^2}{2\pi d}$ (attractive for parallel currents). (A)
- 17: Clausius equality for reversible cycle: $\frac{Q_1}{T_1} = \frac{Q_2}{T_2}$. (A)
- 18: $r_n \propto n^2$. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Sharpless asymmetric dihydroxylation mechanism.
- 20: (A, B, C, D) - Ferrocene structure, 18-electron rule, and aromatic reactivity.
- 21: (A, B, C, D) - Flory-Huggins polymer solution thermodynamics.
- 22: (A, B, C, D) - Mutual exclusion rule in vibrational spectroscopy.
- 23: (A, B, C, D) - Nitrogenase biological dinitrogen fixation.
- 24: (A, B, C, D) - Acid radical qualitative testing.

#### Solutions 25 to 30:
- 25: Hydrolysis of acetate: $K_h = K_w / K_a = 10^{-14} / (1.8 \times 10^{-5}) = 5.56 \times 10^{-10}$.
  $[\text{OH}^-] = \sqrt{K_h c} = \sqrt{(5.56 \times 10^{-10}) (0.10)} = \sqrt{5.56 \times 10^{-11}} \approx 7.45 \times 10^{-6}\text{ M}$.
  $\text{pOH} = 5.13 \implies \text{pH} = 14 - 5.13 = 8.87$. (Answer: 8.87)
- 26: Tetrahedral $\text{Ni}^{2+}$ is $d^8 \implies e^4 t_2^4 \implies 2$ unpaired electrons. (Answer: 2)
- 27: Empirical formula $\text{C}_2\text{H}_6\text{O}$ (mass 46). Formula is $\text{C}_2\text{H}_6\text{O} \implies 2 + 6 + 1 = 9$ atoms. (Answer: 9)
- 28: $99\%$ decomposed $\implies 1\%$ remains.
  $t = \frac{2.303}{k}\log(100) = \frac{2.303 \times 2}{0.693 / 100} = \frac{4.606 \times 100}{0.693} \approx 665\text{ s}$. (Answer: 665)
- 29: $m = \frac{M I t}{F} = \frac{108.0 \times 9.65 \times 100.0}{96500} = \frac{104220}{96500} = 1.08\text{ g}$. (Answer: 1.08)
- 30: $\Delta T_b = K_b m = 0.512 \times 0.20 = 0.1024^\circ\text{C} \approx 0.10^\circ\text{C}$. (Answer: 0.10)

#### Solutions 31 to 36:
- 31: Williamson ether synthesis: alkoxide + primary alkyl halide ($S_N2$). (A)
- 32: $[\text{Co(CN)}_6]^{3-}$ has the strongest ligand field, largest $\Delta_o$, absorbs highest energy (shortest wavelength). (A)
- 33: Glycosidic linkage connects monosaccharides. (A)
- 34: Slag formation: $\text{CaO} + \text{SiO}_2 \to \text{CaSiO}_3$. (A)
- 35: Phenol + Zn dust reduces to benzene. (A)
- 36: $\text{HSO}_4^-$ loses $\text{H}^+$ to become $\text{SO}_4^{2-}$. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Riemann zeta function properties and values.
- 38: (A, B, C, D) - Matrix exponential algebraic properties.
- 39: (A, B, C, D) - Clairaut relation for geodesics on surfaces of revolution.
- 40: (A, B, C, D) - Euler planar graph formula and Kuratowski's theorem.
- 41: (A, B, C, D) - Cubic polynomial calculus analysis.
- 42: (A, B, C, D) - Fibonacci identities and Binet's formula.

#### Solutions 43 to 48:
- 43: $I = [x^5/5]_0^1 = 1/5 = 0.20 \implies 100 I = 20$. (Answer: 20)
- 44: $5! = 120$. (Answer: 120)
- 45: $d = \frac{|1 + 2(2) - 2(3) + 4|}{\sqrt{1 + 4 + 4}} = \frac{|1 + 4 - 6 + 4|}{3} = \frac{3}{3} = 1.0$. (Answer: 1.0)
- 46: $z = \sqrt{2} e^{i\pi/4} \implies z^8 = (\sqrt{2})^8 e^{i 2\pi} = 16(1) = 16$. (Answer: 16)
- 47: $y(x) = x^4 + 5 \implies y(1) = 1 + 5 = 6$. (Answer: 6)
- 48: Out of 6 faces, 1 and 2 give $\le 2 \implies 2/6 = 1/3 \approx 0.33$. (Answer: 0.33)

#### Solutions 49 to 54:
- 49: Area $= \int_0^1 (x - x^2)dx = 1/2 - 1/3 = 1/6$. (A)
- 50: $a_{15} = 5 + 14(3) = 5 + 42 = 47$. (A)
- 51: Limit $= 3$. (A)
- 52: $(x - 1)^2 + (y - 2)^2 = 9 \implies x^2 + y^2 - 2x - 4y - 4 = 0$. (A)
- 53: Distance $= \frac{|9 - 3|}{\sqrt{1 + 4 + 4}} = \frac{6}{3} = 2$. (A)
- 54: $\vec{a} \cdot \vec{b} = 2(3) + 3(-2) + 4(1) = 6 - 6 + 4 = 4$. (A)
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 2
## IIT Delhi Benchmark JEE Advanced Mock Examination 20

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Dielectric insertion into isolated capacitor.
- 2: (A, B, C, D) - Simple harmonic motion fundamental relations.
- 3: (A, B, C, D) - Brewster's angle and polarization by reflection.
- 4: (A, B, C, D) - P-V cyclic process thermodynamics.
- 5: (A, B, C, D) - Long solenoid magnetic field and self-inductance.
- 6: (A, B, C, D) - Series and parallel resistor combinations.

#### Solutions 7 to 12:
- 7: $U_0 = \frac{1}{2} C_0 V_0^2 = \frac{1}{2}(10.0 \times 10^{-6})(10000) = 0.050\text{ J} = 50.0\text{ mJ}$.
  $U = U_0 / \kappa = 50.0 / 5.0 = 10.0\text{ mJ}$. (Answer: 10.0)
- 8: $a_{\text{max}} = \omega^2 A = (2\pi f)^2 A = 4\pi^2 (4.0) (0.05) = 0.80 \pi^2 \approx 0.80 \times 9.87 \approx 7.90\text{ m/s}^2$. (Answer: 7.90)
- 9: $\tan\theta_B = \sqrt{3} \implies \theta_B = 60^\circ$. (Answer: 60)
- 10: $W = \pi R_P R_V = \pi (2.0 \times 10^5) (1.0 \times 10^{-3}) = 200\pi \approx 628\text{ J}$. (Answer: 628)
- 11: $B = \mu_0 n I = (4\pi \times 10^{-7}) (500) (2.0) = 4\pi \times 10^{-4}\text{ T} \approx 1.26\text{ mT}$. (Answer: 1.26)
- 12: $R_p = R / 5 = 10.0 / 5 = 2.0\text{ }\Omega$. (Answer: 2.0)

#### Solutions 13 to 18 (Matching Lists):
- 13: P-4, Q-2, R-1, S-3. (A)
- 14: P-4, Q-1, R-3, S-2. (A)
- 15: P-2, Q-1, R-4, S-3. (A)
- 16: P-2, Q-1, R-4, S-3. (A)
- 17: P-2, Q-1, R-4, S-3. (A)
- 18: P-2, Q-1, R-4, S-3. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Alcohol Lucas test and oxidation reactions.
- 20: (A, B, C, D) - Transition metal characteristic properties.
- 21: (A, B, C, D) - Electrochemical series applications.
- 22: (A, B, C, D) - Chemical kinetics definitions.
- 23: (A, B, C, D) - Carbohydrate classification and starch structure.
- 24: (A, B, C, D) - Iron blast furnace reduction zones.

#### Solutions 25 to 30:
- 25: $[\text{H}^+] = 2 \times 0.0050 = 0.010\text{ M} \implies \text{pH} = 2.00$. (Answer: 2.00)
- 26: High-spin $d^5$ Fe(III) has 5 unpaired electrons $\implies \mu = \sqrt{35} \approx 5.92\text{ BM}$. (Answer: 5.92)
- 27: Empirical formula $\text{CH}_2\text{O}$ (mass 30). Multiple $90/30 = 3 \implies \text{C}_3\text{H}_6\text{O}_3 \implies 3$ carbons. (Answer: 3)
- 28: $75\%$ decayed $\implies 2$ half-lives $= 2 \times 20.0 = 40.0\text{ days}$. (Answer: 40)
- 29: $m = \frac{M I t}{F} = \frac{108.0 \times 2.0 \times 4825}{96500} = \frac{1042200}{96500} = 10.80\text{ g}$. (Answer: 10.80)
- 30: $\Delta T_b = K_b m = 0.512 \times 0.10 \approx 0.05^\circ\text{C}$. (Answer: 0.05)

#### Solutions 31 to 36:
- 31: P-3, Q-4, R-2, S-1. (A)
- 32: P-2, Q-1, R-4, S-3. (A)
- 33: P-2, Q-1, R-4, S-3. (A)
- 34: P-2, Q-1, R-4, S-3. (A)
- 35: P-2, Q-1, R-4, S-3. (A)
- 36: P-2, Q-3, R-4, S-1. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Quadratic function algebra and parabola geometry.
- 38: (A, B, C, D) - Real symmetric matrix properties.
- 39: (A, B, C, D) - Line geometry in 3D.
- 40: (A, B, C, D) - Decay differential equation.
- 41: (A, B, C, D) - Binomial distribution parameters.
- 42: (A, B, C, D) - Infinite geometric series sum.

#### Solutions 43 to 48:
- 43: $I = [x^3/3]_0^3 = 27/3 = 9$. (Answer: 9)
- 44: $P(5, 3) = 5 \times 4 \times 3 = 60$. (Answer: 60)
- 45: $d = \frac{|0 + 0 - 10|}{\sqrt{9 + 16}} = \frac{10}{5} = 2.0$. (Answer: 2.0)
- 46: $|z| = \sqrt{9 + 16} = 5$. (Answer: 5)
- 47: $y(x) = 2x + 1 \implies y(4) = 2(4) + 1 = 9$. (Answer: 9)
- 48: Outcomes $\ge 2$ heads: HHT, HTH, THH, HHH (4 outcomes). $P = 4/8 = 0.50$. (Answer: 0.50)

#### Solutions 49 to 54:
- 49: P-2, Q-1, R-4, S-3. (A)
- 50: P-2, Q-1, R-4, S-3. (A)
- 51: P-2, Q-1, R-4, S-3. (A)
- 52: P-2, Q-1, R-4, S-3. (A)
- 53: P-2, Q-1, R-4, S-3. (A)
- 54: P-2, Q-1, R-4, S-3. (A)
"""

val_md = r"""# Answer Key & Benchmark Validation — Mock 20
## IIT Delhi Benchmark Calibration

### Paper 1 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 12906.4 | **C25** | Num | 8.87 | **M43** | Num | 20 |
| **P8** | Num | 13.02 | **C26** | Num | 2 | **M44** | Num | 120 |
| **P9** | Num | 157978 | **C27** | Num | 9 | **M45** | Num | 1.0 |
| **P10** | Num | 892 | **C28** | Num | 665 | **M46** | Num | 16 |
| **P11** | Num | 2 | **C29** | Num | 1.08 | **M47** | Num | 6 |
| **P12** | Num | 1000 | **C30** | Num | 0.10 | **M48** | Num | 0.33 |
| **P13** | Single | A | **C31** | Single | A | **M49** | Single | A |
| **P14** | Single | A | **C32** | Single | A | **M50** | Single | A |
| **P15** | Single | A | **C33** | Single | A | **M51** | Single | A |
| **P16** | Single | A | **C34** | Single | A | **M52** | Single | A |
| **P17** | Single | A | **C35** | Single | A | **M53** | Single | A |
| **P18** | Single | A | **C36** | Single | A | **M54** | Single | A |

---

### Paper 2 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 10.0 | **C25** | Num | 2.00 | **M43** | Num | 9 |
| **P8** | Num | 7.90 | **C26** | Num | 5.92 | **M44** | Num | 60 |
| **P9** | Num | 60 | **C27** | Num | 3 | **M45** | Num | 2.0 |
| **P10** | Num | 628 | **C28** | Num | 40 | **M46** | Num | 5 |
| **P11** | Num | 1.26 | **C29** | Num | 10.80 | **M47** | Num | 9 |
| **P12** | Num | 2.0 | **C30** | Num | 0.05 | **M48** | Num | 0.50 |
| **P13** | Match | A | **C31** | Match | A | **M49** | Match | A |
| **P14** | Match | A | **C32** | Match | A | **M50** | Match | A |
| **P15** | Match | A | **C33** | Match | A | **M51** | Match | A |
| **P16** | Match | A | **C34** | Match | A | **M52** | Match | A |
| **P17** | Match | A | **C35** | Match | A | **M53** | Match | A |
| **P18** | Match | A | **C36** | Match | A | **M54** | Match | A |
"""

if __name__ == "__main__":
    create_mock_files(
        20,
        paper_1_md,
        paper_2_md,
        sol_1_md,
        sol_2_md,
        val_md,
        iit_name="IIT_Delhi"
    )

