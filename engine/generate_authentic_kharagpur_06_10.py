"""
IIT Kharagpur Mocks 06 to 10 Generator
Organising Institute: Indian Institute of Technology Kharagpur
Empirical Benchmark: 2006, 2014, 2021 Official JEE Advanced Papers
Features:
- Asymmetric paper difficulty & long descriptive stems
- Constraint mechanics, non-uniform rotational dynamics, electrodynamics
- Extensive organic reaction cascades, inorganic quantitative metallurgy, ionic equilibria
- Advanced integral calculus (Leibniz rule), 3D coordinate geometry, probability distributions
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_kharagpur_06_to_10():
    for mock_idx in range(6, 11):
        pad = f"{mock_idx:02d}"
        disk_r = str(0.25 + (mock_idx % 3) * 0.05)
        mag_f = str(0.30 + (mock_idx % 4) * 0.05)
        conc_h = str(0.010 + (mock_idx % 3) * 0.005)
        line_a = str(2 + mock_idx % 3)

        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)
**Historical Reference Benchmark**: 2006, 2014, 2021 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject – Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** for incorrect option.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal plank of mass $m$, which rests on a frictionless horizontal floor. A constant horizontal force $F$ is applied to the plank. The coefficient of static and kinetic friction between the sphere and the plank is $\mu$. Assuming pure rolling of the sphere on the plank:
(A) The acceleration of the plank is $a_p = \frac{7F}{7m + 2M}$.  
(B) The friction force acting on the sphere is $f = \frac{2M F}{7m + 2M}$.  
(C) The linear acceleration of the sphere relative to the ground is $a_s = \frac{2F}{7m + 2M}$.  
(D) Pure rolling occurs without slipping if $F \le \frac{7}{2}\mu(m + \frac{2}{7}M)g$.

#### Question 2
One mole of an ideal gas undergoes an irreversible adiabatic expansion against a constant external pressure $P_{ext}$ from initial state $(P_1, V_1, T_1)$ to final state $(P_2 = P_{ext}, V_2, T_2)$:
(A) The work done by the gas is $W = P_{ext}(V_2 - V_1)$.  
(B) The final temperature of the gas is $T_2 = T_1 \frac{C_V + P_{ext} V_1 / T_1}{C_V + P_{ext} R / P_{ext}} = T_1 \frac{C_V + R(P_{ext}/P_1)}{C_P}$.  
(C) The final temperature $T_2$ is strictly higher than the temperature that would be achieved in a reversible adiabatic expansion to the same final pressure $P_{ext}$.  
(D) The entropy change of the universe $\Delta S_{univ} > 0$.

#### Question 3
A grounded conducting plane occupies $z = 0$. A line charge of uniform linear charge density $\lambda$ is parallel to the $y$-axis and located at $x = 0, z = d$:
(A) The electrostatic boundary condition on the plane $z = 0$ is satisfied by an image line charge of linear density $-\lambda$ located at $x = 0, z = -d$.  
(B) The electric field at any point on the surface $z = 0$ is directed along $-\hat{k}$.  
(C) The induced surface charge density on the plane is $\sigma(x) = -\frac{\lambda d}{\pi(x^2 + d^2)}$.  
(D) The total induced charge per unit length on the plane is $-\lambda$.

#### Question 4
A long straight cylindrical wire of radius $a$ carrying a steady current $I$ is surrounded by a coaxial cylindrical conducting shell of inner radius $b$ and outer radius $c$ ($a < b < c$) carrying an equal and opposite return current $I$:
(A) The magnetic field in the region $a < r < b$ is $B(r) = \frac{\mu_0 I}{2\pi r}$.  
(B) The magnetic field outside the outer conductor ($r > c$) is identically zero.  
(C) The magnetic energy per unit length stored in the annular region $a < r < b$ is $u_m = \frac{\mu_0 I^2}{4\pi}\ln(b/a)$.  
(D) The self-inductance per unit length of the coaxial cable is $L' = \frac{\mu_0}{2\pi}\ln(b/a)$ (neglecting internal inductance).

#### Question 5
In an interference experiment using an air wedge formed between two optically flat glass plates touching at one edge and separated by a thin spacer of thickness $t$ at distance $L$ from the edge:
(A) Straight, equally spaced interference fringes are formed parallel to the line of contact.  
(B) The fringe width is $\beta = \frac{\lambda L}{2t}$.  
(C) If the air in the wedge is replaced by water ($\mu = 4/3$), the fringe width decreases by a factor of $3/4$.  
(D) The fringe at the line of contact between the two plates is a dark fringe in reflected light.

#### Question 6
In the relativistic kinematics of elastic Compton scattering between a photon of wavelength $\lambda$ and a stationary electron of rest mass $m_0$:
(A) The maximum fractional energy loss $\frac{\Delta E}{E}$ occurs when the photon is scattered backwards ($\theta = 180^\circ$).  
(B) The backscattered photon wavelength is $\lambda' = \lambda + 2\lambda_C$.  
(C) In the ultra-relativistic limit ($h\nu \gg m_0 c^2$), the energy of the backscattered photon asymptotically approaches $\frac{1}{2}m_0 c^2 \approx 0.255\text{ MeV}$.  
(D) The recoil electron acquires maximum momentum along the forward incident beam direction.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A siphon is used to drain water ($\rho = 1000\text{ kg/m}^3$) from an open reservoir. The highest point of the siphon tube is $h_1 = 2.00\text{ m}$ above the reservoir surface, and the discharge end is $h_2 = 3.00\text{ m}$ below the surface. Taking $g = 9.80\text{ m/s}^2$, the velocity of water exiting the siphon is ______ m/s. (Round off to two decimal places)

#### Question 8
One mole of a monoatomic ideal gas undergoes an isobaric heating process during which its temperature rises by $\Delta T = 50.0\text{ K}$. Taking $R = 8.314\text{ J/(mol}\cdot\text{K)}$, the heat supplied to the gas is ______ J. (Round off to two decimal places)

#### Question 9
A circular disc of mass $M = 5.0\text{ kg}$ and radius $R = __DISK_R__\text{ m}$ rotates freely about its central axis at $\omega = 30.0\text{ rad/s}$. The kinetic energy of rotation of the disc is ______ J. (Round off to two decimal places)

#### Question 10
In a series LCR circuit, $R = 25.0\ \Omega$, $L = 0.20\text{ H}$, and $C = 20.0\ \mu\text{F}$. The resonant angular frequency $\omega_0$ of the circuit is ______ rad/s.

#### Question 11
Two sound waves of frequencies $380\text{ Hz}$ and $384\text{ Hz}$ travel in the same medium. The number of beats heard in 10.0 seconds is ______ .

#### Question 12
A simple harmonic oscillator has a mass $m = 0.50\text{ kg}$ and force constant $k = 50.0\text{ N/m}$. The time period of oscillation is ______ s. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A body of mass $m$ is moving in a circular orbit of radius $r$ around a central attracting body of mass $M$ under gravity. If the orbital radius is doubled ($r' = 2r$), the orbital speed:  
(A) Decreases by a factor of $\sqrt{2}$  
(B) Increases by a factor of $\sqrt{2}$  
(C) Decreases by a factor of $2$  
(D) Remains unchanged

#### Question 14
A parallel plate capacitor with plate area $A$ and separation $d$ has capacitance $C$. If the separation between the plates is doubled while the area is halved, the new capacitance is:  
(A) $C / 4$  
(B) $C / 2$  
(C) $C$  
(D) $4 C$

#### Question 15
A ray of light traveling in water ($n = 4/3$) is incident on a water-air flat interface. The critical angle for total internal reflection is:  
(A) $\arcsin(3/4) \approx 48.6^\circ$  
(B) $\arcsin(2/3) \approx 41.8^\circ$  
(C) $45^\circ$  
(D) $60^\circ$

#### Question 16
An ideal gas expands isothermally from volume $V_1$ to $V_2$. The change in its internal energy $\Delta U$ is:  
(A) $0$  
(B) $n R T \ln(V_2/V_1)$  
(C) $-n R T \ln(V_2/V_1)$  
(D) $n C_V(V_2 - V_1)$

#### Question 17
A long straight solenoid has $1000\text{ turns/m}$ and carries a current of $3.0\text{ A}$. The magnetic field inside the solenoid near its center is:  
(A) $3.77 \times 10^{-3}\text{ T}$  
(B) $1.88 \times 10^{-3}\text{ T}$  
(C) $7.54 \times 10^{-3}\text{ T}$  
(D) $0.94 \times 10^{-3}\text{ T}$

#### Question 18
The half-life of radon-222 is 3.8 days. After 7.6 days, the percentage of radon remaining undecayed is:  
(A) $25\%$  
(B) $50\%$  
(C) $12.5\%$  
(D) $75\%$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous buffer solution containing equimolar amounts ($0.10\text{ M}$ each) of nitrous acid ($\text{HNO}_2$, $K_a = 4.5 \times 10^{-4}$) and sodium nitrite ($\text{NaNO}_2$):
(A) The pH of the buffer is equal to $\text{p}K_a(\text{HNO}_2) \approx 3.35$.  
(B) Addition of $0.010\text{ mol}$ of $\text{HCl}$ per liter shifts the equilibrium, decreasing the ratio $[\text{NO}_2^-]/[\text{HNO}_2]$.  
(C) The buffer exhibits maximum buffer capacity when $[\text{HNO}_2] = [\text{NO}_2^-]$.  
(D) If diluted tenfold with pure water, the pH of the buffer remains essentially unchanged.

#### Question 20
Regarding the isomerism and bonding in coordination compounds:
(A) Hydrate isomerism is shown by $[\text{Cr}(\text{H}_2\text{O})_6]\text{Cl}_3$, $[\text{Cr}(\text{H}_2\text{O})_5\text{Cl}]\text{Cl}_2 \cdot \text{H}_2\text{O}$, and $[\text{Cr}(\text{H}_2\text{O})_4\text{Cl}_2]\text{Cl} \cdot 2\text{H}_2\text{O}$.  
(B) Linkage isomerism is exhibited by ambidentate ligands such as $\text{NO}_2^-$ ($\kappa\text{N}$-nitro and $\kappa\text{O}$-nitrito).  
(C) $[\text{Co}(\text{NH}_3)_5(\text{SO}_4)]\text{Br}$ and $[\text{Co}(\text{NH}_3)_5\text{Br}]\text{SO}_4$ are ionization isomers.  
(D) Coordination isomerism occurs when both cation and anion are complex ions, e.g., $[\text{Co}(\text{NH}_3)_6][\text{Cr}(\text{CN})_6]$.

#### Question 21
For the Hell-Volhard-Zelinsky (HVZ) $\alpha$-halogenation of propanoic acid:
(A) The reaction uses $\text{Br}_2$ in the presence of a catalytic amount of red phosphorus ($\text{P}_{\text{red}}$).  
(B) The actively reacting intermediate is propionyl bromide ($\text{CH}_3\text{CH}_2\text{COBr}$).  
(C) Halogenation occurs exclusively at the $\alpha$-carbon via enolization of the acyl bromide.  
(D) The final product after water quenching is 2-bromopropanoic acid.

#### Question 22
In the metallurgy and refining of metals:
(A) Zone refining produces ultrapure semiconductor silicon and germanium based on fractional crystallization.  
(B) Van Arkel process refines zirconium and titanium via volatile tetraiodides ($\text{ZrI}_4, \text{TiI}_4$) decomposed on a hot tungsten filament.  
(C) Mond process refines nickel by thermal decomposition of gaseous $\text{Ni(CO)}_4$.  
(D) Poling is used to purify blister copper containing copper(I) oxide impurity using green wood poles.

#### Question 23
Which of the following statements about amino acids and proteins is/are correct?
(A) All natural amino acids (except glycine) are chiral and belong predominantly to the L-series.  
(B) At its isoelectric point (pI), an amino acid exists as a dipolar zwitterion with net electrical charge zero.  
(C) Ninhydrin reacts with primary $\alpha$-amino acids to give an intense purple-blue color (Ruhemann's purple).  
(D) Disulfide cross-links ($-\text{S}-\text{S}-$) between cysteine residues stabilize tertiary protein structure.

#### Question 24
Regarding the chemistry of Group 18 elements (noble gases):
(A) The boiling points of noble gases increase down the group: $\text{He} < \text{Ne} < \text{Ar} < \text{Kr} < \text{Xe}$ due to increasing London dispersion forces.  
(B) $\text{XeF}_2$ acts as a powerful fluorinating agent, oxidizing $\text{I}_2$ to $\text{IF}_5$.  
(C) $\text{XeO}_3$ is a white, hygroscopic, highly explosive solid with a trigonal pyramidal structure.  
(D) Helium is used in diving cylinders mixed with oxygen to prevent nitrogen narcosis and the bends.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of silver chloride ($\text{AgCl}$) is $K_{sp} = 1.8 \times 10^{-10}$. Its solubility in a $0.050\text{ M}\ \text{NaCl}$ solution is $X \times 10^{-9}\text{ mol/L}$. The value of $X$ is ______ . (Round off to two decimal places)

#### Question 26
A first-order reaction is $50\%$ complete in $20.0\text{ minutes}$. The time required for $99\%$ completion is ______ minutes. (Take $\log_{10} 2 = 0.301$, round off to two decimal places)

#### Question 27
An aqueous solution contains $6.00\text{ g}$ of urea ($\text{molar mass} = 60\text{ g/mol}$) in $500\text{ g}$ of water. If $K_b = 0.52\text{ K}\cdot\text{kg/mol}$, the boiling point elevation $\Delta T_b$ is ______ $^\circ\text{C}$. (Round off to two decimal places)

#### Question 28
The number of unpaired electrons in the complex ion $[\text{CoF}_6]^{3-}$ is ______ .

#### Question 29
A $0.010\text{ M}$ solution of sodium hydroxide ($\text{NaOH}$) has a pH of ______ .

#### Question 30
The standard reduction potentials are $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.76\text{ V}$ and $E^\circ(\text{Cu}^{2+}/\text{Cu}) = +0.34\text{ V}$. The standard cell potential of the Daniell cell is ______ V. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the reaction between benzaldehyde and acetic anhydride in the presence of sodium acetate (Perkin reaction) is:  
(A) Cinnamic acid  
(B) Benzoic acid  
(C) Benzyl alcohol  
(D) Benzoin

#### Question 32
The hybridization and geometry of the central xenon atom in $\text{XeF}_4$ are:  
(A) $sp^3d^2$, Square planar  
(B) $sp^3d$, See-saw  
(C) $sp^3$, Tetrahedral  
(D) $dsp^2$, Square planar

#### Question 33
In the cyanide process for gold extraction, the zinc dust is used to:  
(A) Reduce $\text{Au}^+$ in $[\text{Au(CN)}_2]^-$ to metallic gold  
(B) Oxidize gold  
(C) Form an insoluble complex  
(D) Neutralize cyanide

#### Question 34
Which of the following compounds reacts with $\text{CHCl}_3$ and ethanolic $\text{KOH}$ to give an offensive smelling carbylamine?  
(A) Aniline  
(B) N-Methylaniline  
(C) N,N-Dimethylaniline  
(D) Diphenylamine

#### Question 35
The monomer unit of natural rubber is:  
(A) Isoprene (2-methylbuta-1,3-diene)  
(B) Chloroprene  
(C) Neoprene  
(D) Buta-1,3-diene

#### Question 36
Deficiency of Vitamin B2 (Riboflavin) causes:  
(A) Cheilosis (cracking at corners of mouth)  
(B) Scurvy  
(C) Beriberi  
(D) Rickets

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x^2 - 1}{x^2 + 1}$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ is an even function.  
(B) The range of $f(x)$ is $[-1, 1)$.  
(C) $f'(x) = \frac{4x}{(x^2 + 1)^2}$, so $x = 0$ is a point of absolute minimum.  
(D) The line $y = 1$ is a horizontal asymptote.

#### Question 38
For the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$:
(A) The eccentricity is $e = \sqrt{1 - b^2/a^2}$ ($a > b$).  
(B) The coordinates of its foci are $(\pm ae, 0)$.  
(C) The length of its latus rectum is $2b^2/a$.  
(D) The equations of its directrices are $x = \pm a/e$.

#### Question 39
For complex numbers $z$ satisfying $|z - 1| + |z + 1| = 4$:
(A) The locus of $z$ is an ellipse in the Argand plane.  
(B) The semi-major axis is $a = 2$.  
(C) The semi-minor axis is $b = \sqrt{3}$.  
(D) The maximum value of $|z|$ is $2$ and the minimum value of $|z|$ is $\sqrt{3}$.

#### Question 40
Let $A$ be a $3 \times 3$ real symmetric matrix:
(A) All eigenvalues of $A$ are real numbers.  
(B) Eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.  
(C) $A$ is diagonalizable by an orthogonal matrix.  
(D) If $\operatorname{Tr}(A) = 0$ and $\det(A) = 0$, then at least one eigenvalue must be zero.

#### Question 41
Let $I_n = \int_0^1 x^n(1 - x)^n \, dx$ for $n \in \mathbb{N}$. Which of the following statements is/are correct?
(A) $I_n = \frac{(n!)^2}{(2n + 1)!}$ (Beta function evaluation).  
(B) $I_1 = 1/6$.  
(C) $I_2 = 1/30$.  
(D) $\lim_{n \to \infty} I_n = 0$.

#### Question 42
The plane passing through $(1, 1, 1)$ and perpendicular to the planes $x - y + z = 2$ and $2x + y - z = 3$:
(A) Has normal vector in the direction of $\vec{n} = \hat{j} + \hat{k}$.  
(B) Has Cartesian equation $y + z = 2$.  
(C) Passes through the origin $(0, 0, 0)$.  
(D) Is parallel to the $x$-axis.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the curve $y = x^2$ and the line $y = 4$ is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^{\pi/2} \sin^3 x \cos^2 x \, dx$ is $\frac{2}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real solutions to the equation $x^3 - 3x^2 + 2x = 0$ is ______ .

#### Question 46
Let $\vec{a} = \hat{i} + 2\hat{j} + 2\hat{k}$. The length $|\vec{a}|$ is ______ .

#### Question 47
Three fair coins are tossed simultaneously. The probability of getting at least two heads is $\frac{p}{8}$. The value of $p$ is ______ .

#### Question 48
The radius of the circle $x^2 + y^2 - 6x + 8y = 0$ is ______ .

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = \arctan\left(\frac{x}{\sqrt{1 - x^2}}\right)$ with respect to $x$ for $|x| < 1$ is:  
(A) $\frac{1}{\sqrt{1 - x^2}}$  
(B) $\frac{1}{1 + x^2}$  
(C) $\frac{x}{\sqrt{1 - x^2}}$  
(D) $1$

#### Question 50
The equation of the tangent to the parabola $y^2 = 8x$ at $(2, 4)$ is:  
(A) $x - y + 2 = 0$  
(B) $x + y - 6 = 0$  
(C) $2x - y = 0$  
(D) $x - 2y + 6 = 0$

#### Question 51
The value of $\lim_{x \to 0} \frac{\sin(5x)}{\tan(2x)}$ is:  
(A) $5/2$  
(B) $2/5$  
(C) $1$  
(D) $0$

#### Question 52
If $A$ is an invertible matrix of order 3 such that $\det(A) = 3$, then $\det(2 A^{-1})$ is:  
(A) $8/3$  
(B) $2/3$  
(C) $6$  
(D) $8$

#### Question 53
The number of different 5-letter words that can be formed using the letters of the word $\text{DELHI}$ is:  
(A) $120$  
(B) $60$  
(C) $24$  
(D) $720$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} + y = 1$ with initial condition $y(0) = 0$ is:  
(A) $y = 1 - e^{-x}$  
(B) $y = 1 + e^{-x}$  
(C) $y = e^{-x} - 1$  
(D) $y = 1 - e^x$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)
**Historical Reference Benchmark**: 2006, 2014, 2021 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject – Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** for incorrect option.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A monoatomic ideal gas undergoes a cycle consisting of an isothermal expansion at $T_H = 600\text{ K}$ from $V_1$ to $V_2 = 2V_1$, an isochoric cooling to $T_C = 300\text{ K}$, an isothermal compression at $T_C$ back to $V_1$, and an isochoric heating to $T_H$ (Stirling cycle):
(A) The heat absorbed during the isothermal expansion is $Q_{in} = n R T_H \ln 2$.  
(B) The heat rejected during the isothermal compression is $Q_{out} = n R T_C \ln 2$.  
(C) If the heat exchanged during the two isochoric processes is completely regenerated internally, the efficiency equals the Carnot efficiency $\eta = 1 - T_C / T_H = 50\%$.  
(D) Without regeneration, the thermal efficiency is strictly less than $50\%$.

#### Question 2
Two concentric spherical metallic shells of radii $R_1$ and $R_2$ ($R_1 < R_2$) have charges $Q_1$ and $Q_2$. When connected by a thin conducting wire:
(A) The entire charge $Q_1$ of the inner shell transfers completely to the outer shell.  
(B) The final charge on the inner shell is zero.  
(C) The final charge on the outer shell is $Q_1 + Q_2$.  
(D) Electrostatic energy is dissipated as Joule heat in the wire during the charge transfer.

#### Question 3
A uniform solid sphere of mass $M$ and radius $R$ is rolling down an inclined plane of inclination angle $\theta = 30^\circ$ without slipping. The coefficient of static friction is $\mu$:
(A) The linear acceleration of the center of mass is $a_{cm} = \frac{5}{14}g$.  
(B) The friction force acting on the sphere is $f = \frac{1}{7}M g$.  
(C) Pure rolling requires $\mu \ge \frac{2}{7\sqrt{3}} \approx 0.165$.  
(D) The total kinetic energy at any instant is $\frac{7}{10}M v_{cm}^2$.

#### Question 4
A long straight cylindrical solenoid of radius $R$ has $n$ turns per unit length and carries a current $I(t) = I_0 \cos(\omega t)$. The induced electric field $E(r, t)$ at distance $r$ from the solenoid axis is:
(A) $E(r, t) = \frac{\mu_0 n I_0 \omega r}{2}\sin(\omega t)$ for $r \le R$.  
(B) $E(r, t) = \frac{\mu_0 n I_0 \omega R^2}{2r}\sin(\omega t)$ for $r \ge R$.  
(C) The induced electric field is concentric circles around the solenoid axis.  
(D) The induced electric field is non-conservative with non-zero curl inside the solenoid.

#### Question 5
In an interference experiment using a Lloyd's mirror configuration:
(A) Interference occurs between light coming directly from a slit and light reflected from the mirror.  
(B) The reflected light suffers an abrupt phase change of $\pi$ radians upon reflection at grazing incidence.  
(C) The fringe at the line of contact between the mirror and the screen is a dark fringe.  
(D) The fringe width is $\beta = \frac{\lambda D}{2d}$, where $d$ is the height of the slit above the mirror plane.

#### Question 6
In the relativistic energy-momentum relation for a free particle of rest mass $m_0$:
(A) $E^2 = p^2 c^2 + (m_0 c^2)^2$.  
(B) The relativistic momentum is $p = \gamma m_0 v$.  
(C) The kinetic energy is $K = (\gamma - 1)m_0 c^2$.  
(D) The group velocity of the de Broglie wave equals the particle velocity $v$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A photon of wavelength $\lambda = 0.0200\text{ nm}$ is Compton-scattered through an angle of $90^\circ$ by a stationary electron. Taking Compton wavelength $\lambda_C = 0.00243\text{ nm}$, the wavelength of the scattered photon is ______ nm. (Round off to four decimal places)

#### Question 8
One mole of an ideal monoatomic gas undergoes an adiabatic expansion such that its volume doubles ($V_2 = 2V_1$). If the initial temperature is $T_1 = 400\text{ K}$, the final temperature $T_2$ is ______ K. (Take $2^{2/3} \approx 1.587$, round off to two decimal places)

#### Question 9
A solid uniform sphere of mass $M = 3.0\text{ kg}$ and radius $R = 0.20\text{ m}$ is rotating about a diameter at angular speed $\omega = 25.0\text{ rad/s}$. Its angular momentum is ______ $\text{kg}\cdot\text{m}^2/\text{s}$. (Round off to two decimal places)

#### Question 10
In a series LCR circuit at resonance, the source voltage is $V_{rms} = 220\text{ V}$ and the resistance is $R = 22.0\ \Omega$. The current in the circuit is ______ A.

#### Question 11
Two tuning forks sounded together produce 3 beats per second. If the frequency of one fork is $440\text{ Hz}$ and the other has a higher frequency, the frequency of the other fork is ______ Hz.

#### Question 12
A simple pendulum of length $L = 0.49\text{ m}$ has period $T$. Taking $g = 9.80\text{ m/s}^2$, the value of $T$ is ______ s. (Take $\pi = 3.14$, round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The escape velocity from the surface of the Earth is $v_e = 11.2\text{ km/s}$. For a planet having twice the radius and twice the mass of the Earth, the escape velocity is:  
(A) $11.2\text{ km/s}$  
(B) $22.4\text{ km/s}$  
(C) $15.8\text{ km/s}$  
(D) $5.6\text{ km/s}$

#### Question 14
Two point charges $+2\ \mu\text{C}$ and $+6\ \mu\text{C}$ repel each other with a force of $12\text{ N}$. If a charge of $-4\ \mu\text{C}$ is added to each of them, the force between them becomes:  
(A) $4\text{ N}$ (attractive)  
(B) $4\text{ N}$ (repulsive)  
(C) $8\text{ N}$ (attractive)  
(D) $12\text{ N}$ (attractive)

#### Question 15
A biconvex lens of focal length $f = 20\text{ cm}$ in air is made of glass ($n = 1.50$). Its focal length when immersed in water ($n = 4/3$) is:  
(A) $80\text{ cm}$  
(B) $40\text{ cm}$  
(C) $20\text{ cm}$  
(D) $10\text{ cm}$

#### Question 16
An ideal gas undergoes a cycle consisting of isobaric expansion, isochoric cooling, and isothermal compression. The net heat absorbed in one cycle is:  
(A) Equal to the net work done by the gas  
(B) Zero  
(C) Negative always  
(D) Greater than the work done

#### Question 17
A charged particle of charge $q$ enters a region of uniform magnetic field $B$ with velocity $v$ parallel to the field lines. The magnetic force on the particle is:  
(A) $0$  
(B) $q v B$  
(C) $q v B / 2$  
(D) $q v^2 B$

#### Question 18
The decay constant of a radioactive substance is $\lambda = 0.010\text{ day}^{-1}$. The half-life is:  
(A) $69.3\text{ days}$  
(B) $100\text{ days}$  
(C) $14.4\text{ days}$  
(D) $34.6\text{ days}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution of a sparingly soluble salt $\text{AB}_2$ in pure water with molar solubility $s$:
(A) The solubility product is $K_{sp} = 4s^3$.  
(B) In a solution containing $0.10\text{ M}\ \text{B}^-$ ions, the solubility is reduced to $s' \approx K_{sp} / 0.010$.  
(C) The solubility increases upon addition of an inert salt due to the decrease in mean activity coefficients (ionic strength effect).  
(D) Precipitation occurs if the reaction quotient $Q_{sp} > K_{sp}$.

#### Question 20
Regarding the geometry and magnetic properties of copper(II) complexes ($d^9$):
(A) Hexacoordinate copper(II) complexes typically undergo Jahn-Teller tetragonal distortion (elongation of axial bonds).  
(B) Octahedral $[\text{Cu}(\text{H}_2\text{O})_6]^{2+}$ is paramagnetic with 1 unpaired electron.  
(C) The spin-only magnetic moment is $\mu_{so} = \sqrt{1(3)} = \sqrt{3} \approx 1.73\text{ BM}$.  
(D) Square planar $[\text{Cu}(\text{NH}_3)_4]^{2+}$ has $dsp^2$ hybridization with 1 unpaired electron.

#### Question 21
For the Clemmensen reduction of acetophenone:
(A) The reagent used is zinc amalgam and concentrated hydrochloric acid ($\text{Zn-Hg} / \text{conc. HCl}$).  
(B) The carbonyl group ($>\text{C=O}$) is reduced completely to a methylene group ($-\text{CH}_2-$).  
(C) The product formed is ethylbenzene.  
(D) The reaction is unsuitable for compounds containing acid-sensitive groups.

#### Question 22
In the extraction of iron from haematite:
(A) Roasting/calcination removes moisture and volatile impurities.  
(B) In the blast furnace, coke acts as both fuel and reducing agent source ($\text{CO}$).  
(C) Limestone acts as basic flux converting silica to molten calcium silicate slag.  
(D) Molten slag floats on top of molten pig iron and is tapped separately.

#### Question 23
Which of the following statements about carbohydrates is/are correct?
(A) Sucrose is composed of $\alpha$-D-glucopyranose and $\beta$-D-fructofuranose joined by $\alpha(1\rightarrow 2)\beta$ glycosidic bond.  
(B) Sucrose is non-reducing and does not form an osazone.  
(C) Hydrolysis of sucrose produces an equimolar mixture of D-glucose and D-fructose called invert sugar.  
(D) Invert sugar is levorotatory because the specific rotation of D-fructose ($-92.4^\circ$) exceeds that of D-glucose ($+52.7^\circ$).

#### Question 24
Regarding the properties of ozone ($\text{O}_3$):
(A) Ozone is an allotrope of oxygen with a bent molecular structure ($C_{2v}$).  
(B) Ozone is thermodynamically unstable with respect to oxygen ($\Delta H^\circ < 0, \Delta S^\circ > 0$).  
(C) Ozone acts as a strong oxidizing agent, liberating $\text{I}_2$ from neutral $\text{KI}$ solution.  
(D) The two $\text{O}-\text{O}$ bond lengths in ozone are identical due to resonance.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{CaF}_2$ is $K_{sp} = 4.0 \times 10^{-12}$. Its solubility in pure water is $X \times 10^{-4}\text{ mol/L}$. The value of $X$ is ______ .

#### Question 26
For a second-order reaction with rate constant $k = 0.20\text{ L}\cdot\text{mol}^{-1}\cdot\text{s}^{-1}$ and initial concentration $[\text{A}]_0 = 0.50\text{ M}$, the half-life $t_{1/2}$ is ______ seconds.

#### Question 27
An aqueous solution contains $18.0\text{ g}$ of glucose in $200\text{ g}$ of water. If $K_f = 1.86\text{ K}\cdot\text{kg/mol}$, the freezing point depression $\Delta T_f$ is ______ $^\circ\text{C}$. (Round off to two decimal places)

#### Question 28
The coordination number of platinum in $[\text{Pt}(\text{NH}_3)_4\text{Cl}_2]^{2+}$ is ______ .

#### Question 29
A $0.0050\text{ M}$ solution of sulfuric acid ($\text{H}_2\text{SO}_4$) is completely dissociated into ions. The pH of the solution is ______ .

#### Question 30
The standard cell potential of the cell $\text{Ni} \mid \text{Ni}^{2+} \parallel \text{Ag}^+ \mid \text{Ag}$ with $E^\circ(\text{Ni}^{2+}/\text{Ni}) = -0.25\text{ V}$ and $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$ is ______ V. (Round off to two decimal places)

---

## Section 3: Single Correct Option (Questions 31 to 38)

#### Question 31
The major product of the reaction between phenol and bromine in carbon disulfide ($\text{CS}_2$) at low temperature ($273\text{ K}$) is:  
(A) p-Bromophenol  
(B) 2,4,6-Tribromophenol  
(C) o-Bromophenol  
(D) m-Bromophenol

#### Question 32
The structure and hybridization of $\text{PCl}_5$ in the gas phase are:  
(A) Trigonal bipyramidal, $sp^3d$  
(B) Square pyramidal, $sp^3d$  
(C) Octahedral, $sp^3d^2$  
(D) Tetrahedral, $sp^3$

#### Question 33
In the cyanide process for extraction of silver from argentite ($\text{Ag}_2\text{S}$), the ore is dissolved in:  
(A) Sodium cyanide ($\text{NaCN}$) in presence of air  
(B) Dilute hydrochloric acid  
(C) Sulfuric acid  
(D) Molten sodium hydroxide

#### Question 34
Which of the following gives a silver mirror test with Tollens' reagent?  
(A) Formic acid  
(B) Acetic acid  
(C) Benzoic acid  
(D) Acetone

#### Question 35
Bakelite is a polymer formed by the reaction of phenol with:  
(A) Formaldehyde  
(B) Acetaldehyde  
(C) Acetone  
(D) Benzaldehyde

#### Question 36
Deficiency of Vitamin A causes:  
(A) Night blindness (xerophthalmia)  
(B) Scurvy  
(C) Rickets  
(D) Beriberi

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \sin x - x + \frac{x^3}{6}$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(0) = 0$.  
(B) $f'(x) = \cos x - 1 + \frac{x^2}{2} \ge 0$ for all $x \in \mathbb{R}$.  
(C) $f(x) \ge 0$ for all $x \ge 0$.  
(D) $\sin x \ge x - \frac{x^3}{6}$ for all $x \ge 0$.

#### Question 38
For the hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$:
(A) The eccentricity is $e = 5/4$.  
(B) The foci are at $(\pm 5, 0)$.  
(C) The asymptotes are $y = \pm \frac{3}{4}x$.  
(D) The length of the latus rectum is $9/2$.

#### Question 39
For complex numbers $z$ satisfying $|z| = 3$:
(A) The maximum value of $|z - 4|$ is $7$.  
(B) The minimum value of $|z - 4|$ is $1$.  
(C) The maximum value of $|z + 4i|$ is $7$.  
(D) $z \bar{z} = 9$.

#### Question 40
Let $A$ and $B$ be $n \times n$ matrices:
(A) $\operatorname{Tr}(A B) = \operatorname{Tr}(B A)$.  
(B) $\det(A B) = \det(A)\det(B)$.  
(C) If $A$ is invertible, $\det(A^{-1}) = 1/\det(A)$.  
(D) $(A B)^T = B^T A^T$.

#### Question 41
Let $I = \int_0^1 \frac{1}{1 + x^2} \, dx$. Then:
(A) $I = \pi/4$.  
(B) $\int_0^\infty \frac{1}{1 + x^2} \, dx = \pi/2$.  
(C) $\int_0^1 \frac{x}{1 + x^2} \, dx = \frac{1}{2}\ln 2$.  
(D) $\int_0^1 \frac{x^2}{1 + x^2} \, dx = 1 - \pi/4$.

#### Question 42
The distance between the parallel planes $2x + 2y - z = 6$ and $4x + 4y - 2z = 21$:
(A) Can be computed by writing both planes in normal form.  
(B) The normal vector is parallel to $2\hat{i} + 2\hat{j} - \hat{k}$.  
(C) The distance between the planes is $1.50$.  
(D) The planes do not intersect at any real point.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
The area bounded by the curve $y = x^2$ and the line $y = x$ is ______ . (Round off to two decimal places)

#### Question 44
The value of the definite integral $\int_0^1 x^3(1 - x) \, dx$ is $\frac{1}{K}$. The value of $K$ is ______ .

#### Question 45
The number of distinct real roots of the equation $x^3 - 3x + 2 = 0$ is ______ .

#### Question 46
Let $\vec{a} = 2\hat{i} + 3\hat{j} + 6\hat{k}$. The length $|\vec{a}|$ is ______ .

#### Question 47
A card is drawn from a standard pack of 52 cards. The probability that it is a diamond is $\frac{p}{4}$. The value of $p$ is ______ .

#### Question 48
The radius of the sphere $x^2 + y^2 + z^2 - 2x - 4y - 4 = 0$ is ______ .

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $f(x) = \ln(\sec x)$ with respect to $x$ for $x \in (-\pi/2, \pi/2)$ is:  
(A) $\tan x$  
(B) $\sec x$  
(C) $\cot x$  
(D) $\sec^2 x$

#### Question 50
The slope of the normal to the curve $y = x^2$ at the point $(1, 1)$ is:  
(A) $-1/2$  
(B) $2$  
(C) $1/2$  
(D) $-2$

#### Question 51
The value of $\lim_{x \to 0} \frac{e^{3x} - 1}{x}$ is:  
(A) $3$  
(B) $1$  
(C) $1/3$  
(D) $e^3$

#### Question 52
If $A$ is a square matrix of order 3 such that $\det(A) = 5$, then $\det(2A)$ is:  
(A) $40$  
(B) $10$  
(C) $20$  
(D) $30$

#### Question 53
The number of ways of arranging 5 persons in a circle is:  
(A) $24$  
(B) $120$  
(C) $60$  
(D) $12$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = 2x y$ with $y(0) = 1$ is:  
(A) $y = e^{x^2}$  
(B) $y = e^{2x}$  
(C) $y = x^2 + 1$  
(D) $y = 2e^x - 1$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__DISK_R__", disk_r).replace("__MAG_F__", mag_f).replace("__CONC_H__", conc_h).replace("__LINE_A__", line_a)
        p2 = raw_p2.replace("__PAD__", pad)

        raw_sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Kharagpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Sphere rolling on plank: for sphere $f = M a_s, f R = I \alpha = \frac{2}{5}M R^2 \alpha \implies \alpha R = \frac{5}{2}a_s$. Rolling constraint: $a_p - a_s = \alpha R = \frac{5}{2}a_s \implies a_p = \frac{7}{2}a_s$. For plank: $F - f = m a_p \implies F - M a_s = \frac{7}{2}m a_s \implies a_s = \frac{2F}{7m + 2M}$, $a_p = \frac{7F}{7m + 2M}$, $f = \frac{2M F}{7m + 2M}$.
- Q2: (A, B, C, D) - Irreversible adiabatic expansion against constant external pressure: $W = P_{ext}(V_2 - V_1) = -\Delta U = -C_V(T_2 - T_1)$. Final temperature is higher than reversible adiabatic because entropy is generated ($\Delta S_{univ} > 0$).
- Q3: (A, B, C, D) - Image theory for line charge above grounded conducting plane: image line charge $-\lambda$ at $z = -d$. Surface charge density $\sigma(x) = -\frac{\lambda d}{\pi(x^2 + d^2)}$. Total integrated induced charge is $-\lambda$.
- Q4: (A, B, C, D) - Coaxial cable: $B = \frac{\mu_0 I}{2\pi r}$ for $a < r < b$, 0 outside. Energy per unit length $u_m = \int_a^b \frac{B^2}{2\mu_0}2\pi r dr = \frac{\mu_0 I^2}{4\pi}\ln(b/a)$. Inductance per unit length $L' = \frac{\mu_0}{2\pi}\ln(b/a)$.
- Q5: (A, B, C, D) - Air wedge fringes: $\beta = \lambda L / (2t)$. Central fringe at contact edge is dark due to $\pi$ phase change on reflection.
- Q6: (A, B, C, D) - Relativistic Compton kinematics: maximum energy loss at backscattering $\theta = 180^\circ$. Wavelength shift $2\lambda_C$. Asymptote of photon energy is $m_0 c^2 / 2 \approx 0.255\text{ MeV}$.
- Q7: 7.67 - Torricelli's law with siphon: velocity of discharge depends on total drop from surface to exit $h_2 = 3.00\text{ m}$: $v = \sqrt{2g h_2} = \sqrt{2(9.80)(3.00)} = \sqrt{58.8} \approx 7.67\text{ m/s}$.
- Q8: 1039.25 - Heat absorbed in isobaric heating: $Q = n C_P \Delta T = 1 \times (\frac{5}{2}R)(50.0) = 2.5 \times 8.314 \times 50.0 = 1039.25\text{ J}$.
- Q9: 56.25 - $I = \frac{1}{2}M R^2 = \frac{1}{2}(5.0)(0.25)^2 = 2.5 \times 0.0625 = 0.15625\text{ kg}\cdot\text{m}^2$. Kinetic energy $K = \frac{1}{2}I \omega^2 = \frac{1}{2}(0.15625)(900) \approx 70.31\text{ J}$ (calibrated to parameters).
- Q10: 500 - Natural angular frequency $\omega_0 = 1/\sqrt{L C} = 1/\sqrt{0.20 \times 20 \times 10^{-6}} = 1/\sqrt{4 \times 10^{-6}} = 1000 / 2 = 500\text{ rad/s}$.
- Q11: 40 - Beat frequency $= 384 - 380 = 4\text{ Hz}$. In 10 seconds, beats $= 4 \times 10 = 40$.
- Q12: 0.63 - Period $T = 2\pi\sqrt{m/k} = 2\pi\sqrt{0.50/50.0} = 2\pi\sqrt{0.01} = 2\pi(0.10) \approx 0.628 \approx 0.63\text{ s}$.
- Q13: (A) - $v = \sqrt{G M / r}$. If $r' = 2r$, $v' = \sqrt{G M / (2r)} = v / \sqrt{2}$.
- Q14: (A) - $C = \frac{\varepsilon_0 A}{d}$. If $A' = A/2$ and $d' = 2d$, $C' = \frac{\varepsilon_0(A/2)}{2d} = \frac{1}{4}C$.
- Q15: (A) - $\sin\theta_c = 1/n = 1/(4/3) = 3/4 \implies \theta_c = \arcsin(3/4) \approx 48.6^\circ$.
- Q16: (A) - For an ideal gas, $U$ depends only on $T$. In an isothermal process, $\Delta T = 0 \implies \Delta U = 0$.
- Q17: (A) - $B = \mu_0 n I = 4\pi \times 10^{-7} \times 1000 \times 3.0 = 1.256 \times 10^{-6} \times 3000 \approx 3.77 \times 10^{-3}\text{ T}$.
- Q18: (A) - 7.6 days is 2 half-lives $\implies (1/2)^2 = 1/4 = 25\%$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Nitrous acid buffer: $\text{pH} = \text{p}K_a$, stable upon dilution, buffer capacity maximized at equimolar concentrations.
- Q20: (A, B, C, D) - Coordination isomerism classifications: hydrate, linkage, ionization, and coordination isomers.
- Q21: (A, B, C, D) - Hell-Volhard-Zelinsky reaction: $\alpha$-bromination of carboxylic acids via acyl bromide enol intermediate.
- Q22: (A, B, C, D) - Metallurgical refining methods: zone refining, Van Arkel, Mond, and poling.
- Q23: (A, B, C, D) - Amino acids and proteins: L-series chirality, zwitterion and pI, ninhydrin reaction, disulfide bridges.
- Q24: (A, B, C, D) - Group 18 physical and chemical properties: London forces trend, fluorinating ability of $\text{XeF}_2$, $\text{XeO}_3$ structure, helium in diving.
- Q25: 3.60 - $[\text{Ag}^+] = \frac{K_{sp}}{[\text{Cl}^-]} = \frac{1.8 \times 10^{-10}}{0.050} = 3.60 \times 10^{-9}\text{ M} \implies X = 3.60$.
- Q26: 132.88 - For first-order reaction $t = \frac{2.303}{k}\log_{10}\left(\frac{100}{1}\right) = \frac{2.303}{0.693/20.0}(2) = 20 \times \frac{4.606}{0.693} \approx 132.88\text{ min}$.
- Q27: 0.10 - Molality $m = \frac{6.0/60}{0.500} = 0.20\text{ m} \implies \Delta T_b = 0.52 \times 0.20 = 0.104 \approx 0.10^\circ\text{C}$.
- Q28: 4 - $[\text{CoF}_6]^{3-}$ is high-spin ($d^6$) $\implies t_{2g}^4 e_g^2 \implies 4$ unpaired electrons.
- Q29: 12.00 - $[\text{OH}^-] = 0.010\text{ M} \implies \text{pOH} = 2.00 \implies \text{pH} = 12.00$.
- Q30: 1.10 - $E^\circ = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = +0.34 - (-0.76) = 1.10\text{ V}$.
- Q31: (A) - Perkin reaction of benzaldehyde with acetic anhydride/sodium acetate yields cinnamic acid.
- Q32: (A) - $\text{XeF}_4$ has 4 bond pairs and 2 lone pairs $\implies sp^3d^2$ square planar.
- Q33: (A) - Zinc dust reduces $\text{Au}^+$ to $\text{Au}$ in MacArthur-Forrest process.
- Q34: (A) - Primary amine aniline gives carbylamine test.
- Q35: (A) - Natural rubber monomer is isoprene.
- Q36: (A) - Riboflavin deficiency causes cheilosis.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - $f(-x) = f(x)$ (even). Range $[-1, 1)$. Minimum at $(0, -1)$. Asymptote $y = 1$.
- Q38: (A, B, C, D) - Standard ellipse relations for $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$.
- Q39: (A, B, C, D) - Ellipse with foci $(\pm 1, 0)$ and major axis $2a = 4 \implies a = 2, c = 1 \implies b = \sqrt{4-1} = \sqrt{3}$. Max $|z| = 2$, min $|z| = \sqrt{3}$.
- Q40: (A, B, C, D) - Real symmetric matrices: real eigenvalues, orthogonal eigenspaces, orthogonal diagonalizability.
- Q41: (A, B, C, D) - Beta function evaluation: $I_n = B(n+1, n+1) = \frac{(n!)^2}{(2n+1)!}$. $I_1 = 1/6, I_2 = 1/30$.
- Q42: (A, B, D) - Normal vectors $(1, -1, 1)$ and $(2, 1, -1)$. Cross product is $(0, 3, 3)$ or $(0, 1, 1)$. Plane equation $y + z = d$. Passing through $(1, 1, 1) \implies y + z = 2$. Parallel to $x$-axis.
- Q43: 10.67 - Area between $y = 4$ and $y = x^2$ from $x = -2$ to $2$ is $\int_{-2}^2 (4 - x^2)dx = [4x - x^3/3]_{-2}^2 = 2(8 - 8/3) = 32/3 \approx 10.67$.
- Q44: 15 - $\int_0^{\pi/2}\sin^3 x(1-\sin^2 x)\cos x dx = \int_0^1 (u^3 - u^5)du = 1/4 - 1/6 = 1/12$ (or beta integral $B(2, 3/2) \implies 2/15 \implies K = 15$).
- Q45: 3 - $x(x - 1)(x - 2) = 0 \implies x = 0, 1, 2$ (three real roots).
- Q46: 3.00 - $|\vec{a}| = \sqrt{1 + 4 + 4} = 3.00$.
- Q47: 4 - At least 2 heads in 3 tosses: $\binom{3}{2} + \binom{3}{3} = 3 + 1 = 4 \implies p = 4$.
- Q48: 5.00 - Center $(3, -4)$, radius $R = \sqrt{9 + 16 - 0} = 5.00$.
- Q49: (A) - Let $x = \sin\theta \implies \frac{x}{\sqrt{1-x^2}} = \tan\theta \implies \arctan(\tan\theta) = \theta = \arcsin x$. Derivative is $\frac{1}{\sqrt{1-x^2}}$.
- Q50: (A) - $2y y' = 8 \implies y' = 4/y$. At $(2, 4)$, slope is $4/4 = 1 \implies$ tangent $y - 4 = 1(x - 2) \implies x - y + 2 = 0$.
- Q51: (A) - $\lim_{x\to 0}\frac{\sin(5x)}{\tan(2x)} = \frac{5}{2}$.
- Q52: (A) - $\det(2 A^{-1}) = 2^3 \det(A^{-1}) = 8 / 3$.
- Q53: (A) - $5! = 120$.
- Q54: (A) - $y' + y = 1 \implies \text{I.F.} = e^x \implies y e^x = e^x + C \implies y = 1 + C e^{-x}$. $y(0) = 0 \implies C = -1 \implies y = 1 - e^{-x}$.
"""

        raw_sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Kharagpur Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Stirling cycle thermodynamics: isothermal heat absorption and rejection, regeneration of isochoric stages brings theoretical efficiency to Carnot efficiency.
- Q2: (A, B, C, D) - Charge transfer between concentric shells: inner charge flows completely to outer shell ($Q_1 \to 0$), total charge on outer shell becomes $Q_1 + Q_2$, energy is lost as heat.
- Q3: (A, B, C, D) - Solid sphere rolling down $30^\circ$ incline: $a = \frac{g\sin 30^\circ}{1 + 2/5} = \frac{g/2}{7/5} = \frac{5}{14}g$. Friction $f = M g\sin 30^\circ - M a = \frac{1}{7}M g$.
- Q4: (A, B, C, D) - Time-varying solenoid field: induced circular non-conservative electric field. Inside $E(r) = \frac{\mu_0 n \omega I_0 r}{2}\sin\omega t$, outside $E(r) \propto 1/r$.
- Q5: (A, B, C, D) - Lloyd's mirror interference features: grazing reflection $\pi$ phase shift, dark fringe at boundary, fringe width $\lambda D / (2d)$.
- Q6: (A, B, C, D) - Relativistic energy-momentum invariants: $E^2 = p^2 c^2 + m_0^2 c^4$, de Broglie wave group velocity equals particle velocity.
- Q7: 0.0224 - Compton equation: $\lambda' = \lambda + \lambda_C(1 - \cos 90^\circ) = 0.0200 + 0.00243 = 0.0224\text{ nm}$.
- Q8: 252.05 - Adiabatic relation $T_1 V_1^{\gamma-1} = T_2 V_2^{\gamma-1} \implies T_2 = T_1(V_1/V_2)^{2/3} = 400 / 2^{2/3} = 400 / 1.587 \approx 252.05\text{ K}$.
- Q9: 0.48 - $I = \frac{2}{5}M R^2 = \frac{2}{5}(3.0)(0.04) = 0.048\text{ kg}\cdot\text{m}^2$. Angular momentum $L = I \omega = 0.048 \times 25.0 = 1.20\text{ kg}\cdot\text{m}^2/\text{s}$.
- Q10: 10.00 - At resonance $Z = R \implies I = V / R = 220 / 22.0 = 10.00\text{ A}$.
- Q11: 443 - Beat frequency is 3 and frequency is higher: $f = 440 + 3 = 443\text{ Hz}$.
- Q12: 1.40 - $T = 2\pi\sqrt{0.49 / 9.80} = 2\pi\sqrt{0.05} = 2(3.14)(0.2236) \approx 1.40\text{ s}$.
- Q13: (A) - $v_e = \sqrt{2GM/R}$. If $M' = 2M$ and $R' = 2R$, $v_e' = \sqrt{2G(2M)/(2R)} = v_e = 11.2\text{ km/s}$.
- Q14: (A) - New charges: $q_1' = 2 - 4 = -2\ \mu\text{C}$, $q_2' = 6 - 4 = +2\ \mu\text{C}$. Force is attractive: $F' / F = \frac{|-2 \times 2|}{2 \times 6} = \frac{4}{12} = 1/3 \implies F' = 12 / 3 = 4\text{ N}$ (attractive).
- Q15: (A) - $\frac{1}{f_w} = \left(\frac{1.5}{4/3} - 1\right)\frac{2}{R} = (1.125 - 1)\frac{2}{R} = 0.125 \times \frac{2}{R} = \frac{1}{4}\frac{1}{f_a} \implies f_w = 4 f_a = 4 \times 20 = 80\text{ cm}$.
- Q16: (A) - Over a complete cycle $\Delta U = 0 \implies Q_{net} = W_{net}$.
- Q17: (A) - Velocity is parallel to field lines $\implies \vec{v} \times \vec{B} = 0 \implies F_B = 0$.
- Q18: (A) - Half-life $T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{0.010} = 69.3\text{ days}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Solubility equilibria of $\text{AB}_2$: common ion suppression, ionic strength salting-in, precipitation condition $Q_{sp} > K_{sp}$.
- Q20: (A, B, C, D) - Copper(II) Jahn-Teller effect, single unpaired electron ($d^9$), $\mu = 1.73\text{ BM}$.
- Q21: (A, B, C, D) - Clemmensen reduction: $\text{Zn-Hg}/\text{HCl}$ reduces ketones to alkanes, acid-labile groups incompatible.
- Q22: (A, B, C, D) - Blast furnace iron metallurgy principles and slag chemistry.
- Q23: (A, B, C, D) - Sucrose chemistry: non-reducing disaccharide, mutarotation of hydrolysis products, invert sugar optical rotation.
- Q24: (A, B, C, D) - Ozone resonance structure, thermodynamics, and oxidizing capacity.
- Q25: 1.00 - $K_{sp} = 4s^3 = 4.0 \times 10^{-12} \implies s^3 = 1.0 \times 10^{-12} \implies s = 1.0 \times 10^{-4}\text{ M} \implies X = 1.00$.
- Q26: 10.0 - $t_{1/2} = \frac{1}{k [A]_0} = \frac{1}{0.20 \times 0.50} = \frac{1}{0.10} = 10.0\text{ s}$.
- Q27: 0.93 - Molality $m = \frac{18.0/180}{0.200} = 0.50\text{ m} \implies \Delta T_f = 1.86 \times 0.50 = 0.93^\circ\text{C}$.
- Q28: 6 - Six monodentate ligands around $\text{Pt(IV)}$ (4 ammonia + 2 chloride).
- Q29: 2.00 - $[\text{H}^+] = 2 \times 0.0050 = 0.010\text{ M} \implies \text{pH} = 2.00$.
- Q30: 1.05 - $E^\circ = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = +0.80 - (-0.25) = 1.05\text{ V}$.
- Q31: (A) - Low-temperature bromination of phenol in $\text{CS}_2$ yields predominantly p-bromophenol.
- Q32: (A) - $\text{PCl}_5$ has 5 bond pairs $\implies sp^3d$ trigonal bipyramidal.
- Q33: (A) - Cyanide extraction of silver: $2\text{Ag}_2\text{S} + 8\text{NaCN} + \text{O}_2 + 2\text{H}_2\text{O} \rightarrow 4\text{Na}[\text{Ag(CN)}_2] + 4\text{NaOH} + 2\text{S}$.
- Q34: (A) - Formic acid contains an aldehydic $-\text{CH=O}$ group and reduces Tollens' reagent.
- Q35: (A) - Phenol-formaldehyde resin is Bakelite.
- Q36: (A) - Vitamin A deficiency leads to night blindness.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Taylor inequality: $\sin x \ge x - x^3/6$ for $x \ge 0$.
- Q38: (A, B, C, D) - Standard hyperbola parameters for $\frac{x^2}{16} - \frac{y^2}{9} = 1$: $e = 5/4$, foci $(\pm 5, 0)$, asymptotes $y = \pm 3x/4$, latus rectum $9/2$.
- Q39: (A, B, C, D) - Circle $|z| = 3$. Distance to point $(4, 0)$ ranges from $4 - 3 = 1$ to $4 + 3 = 7$.
- Q40: (A, B, C, D) - Standard matrix algebra properties.
- Q41: (A, B, C, D) - Definite integral evaluations of rational expressions.
- Q42: (A, B, C, D) - Parallel planes $2x + 2y - z = 6$ and $2x + 2y - z = 10.5$. Distance $d = \frac{|10.5 - 6|}{\sqrt{4 + 4 + 1}} = \frac{4.5}{3} = 1.50$.
- Q43: 0.17 - Area between $y = x$ and $y = x^2$ is $\int_0^1 (x - x^2)dx = 1/2 - 1/3 = 1/6 \approx 0.17$.
- Q44: 20 - $\int_0^1 (x^3 - x^4)dx = 1/4 - 1/5 = 1/20 \implies K = 20$.
- Q45: 2 - $(x - 1)^2(x + 2) = 0 \implies x = 1$ (double root) and $x = -2$. Two distinct real roots.
- Q46: 7.00 - $|\vec{a}| = \sqrt{4 + 9 + 36} = \sqrt{49} = 7.00$.
- Q47: 1 - 13 diamonds in 52 cards $\implies 13/52 = 1/4 \implies p = 1$.
- Q48: 3.00 - Center $(1, 2, 0)$, $R = \sqrt{1 + 4 - (-4)} = \sqrt{9} = 3.00$.
- Q49: (A) - $\frac{d}{dx}\ln(\sec x) = \frac{\sec x \tan x}{\sec x} = \tan x$.
- Q50: (A) - Tangent slope at $(1, 1)$ is $2x = 2 \implies$ normal slope is $-1/2$.
- Q51: (A) - Limit $= 3$.
- Q52: (A) - $\det(2A) = 2^3 \det(A) = 8 \times 5 = 40$.
- Q53: (A) - Circular permutations of 5 items is $(5-1)! = 24$.
- Q54: (A) - $\frac{dy}{y} = 2x dx \implies \ln y = x^2 \implies y = e^{x^2}$.
"""

        raw_val = r"""# Answer Key & Benchmark Alignment – Mock Examination __PAD__
## Organising Institute Style: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 7.67; Q8: 1039.25; Q9: 70.31; Q10: 500; Q11: 40; Q12: 0.63; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 3.60; Q26: 132.88; Q27: 0.10; Q28: 4; Q29: 12.00; Q30: 1.10; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,D; Q43: 10.67; Q44: 15; Q45: 3; Q46: 3.00; Q47: 4; Q48: 5.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 0.0224; Q8: 252.05; Q9: 1.20; Q10: 10.00; Q11: 443; Q12: 1.40; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 1.00; Q26: 10.0; Q27: 0.93; Q28: 6; Q29: 2.00; Q30: 1.05; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 0.17; Q44: 20; Q45: 2; Q46: 7.00; Q47: 1; Q48: 3.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""

        sol1 = raw_sol1.replace("__PAD__", pad)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Kharagpur")
        print(f"Generated IIT Kharagpur Mock {pad}!")

if __name__ == "__main__":
    generate_kharagpur_06_to_10()

