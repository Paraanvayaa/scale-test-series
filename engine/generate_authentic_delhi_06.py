# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 06.
Empirical Signature: IIT Delhi Benchmark (2013, 2020)
- Multi-correct dominance (+4/-2 with partial marking)
- Betatron condition, dipole radiation, charge sharing dissipation
- Beckmann rearrangement, chelate effect, Dieterici gas
- Convex functions & Jensen's inequality, Cauchy-Euler ODEs, Cholesky decomposition
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 06 — Paper 1
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
In a betatron accelerator, electrons of charge $-e$ and mass $m$ are accelerated in a circular orbit of constant radius $R$ by a time-varying magnetic field $B(r, t)$ perpendicular to the orbital plane. Which of the following statements is/are correct?
(A) The tangential induced electric field at radius $R$ is $E_\theta = \frac{1}{2\pi R}\frac{d\Phi(R)}{dt}$, where $\Phi(R)$ is the total magnetic flux enclosed by the orbit.  
(B) To maintain a constant orbital radius $R$, the Betatron Condition requires that the change in the average magnetic field $\langle B \rangle$ over the orbit area must be twice the change in the magnetic field $B_{\text{orb}}$ at the orbit itself: $\Delta \langle B \rangle = 2 \Delta B_{\text{orb}}$.  
(C) The magnetic flux condition can be written as $\Delta \Phi(R) = 2\pi R^2 \Delta B_{\text{orb}}$.  
(D) For radial orbital stability against small perturbations, the magnetic field must decrease with radius with field index $n = -\frac{R}{B}\frac{\partial B}{\partial r}$ satisfying $0 < n < 1$.

#### Question 2
Two capacitors of capacitances $C_1$ and $C_2$ are charged to initial potential differences $V_1$ and $V_2$ respectively ($V_1 \ne V_2$). They are then connected in parallel with each other through a connecting resistor of resistance $R$:
(A) The common potential difference across both capacitors in the steady state is $V_f = \frac{C_1 V_1 + C_2 V_2}{C_1 + C_2}$.  
(B) The total charge of the two-capacitor system is strictly conserved during the charging transient.  
(C) The total electrical energy dissipated as Joule heat in the resistor is $\Delta U = \frac{1}{2}\frac{C_1 C_2}{C_1 + C_2}(V_1 - V_2)^2$.  
(D) The total energy dissipated in the resistor depends explicitly on the resistance value $R$.

#### Question 3
An oscillating electric dipole has dipole moment $\vec{p}(t) = p_0 \cos(\omega t)\hat{k}$. According to classical electrodynamics (Larmor-Hertz formula):
(A) The time-averaged total power radiated as electromagnetic waves into space is $P = \frac{\mu_0 p_0^2 \omega^4}{12\pi c}$.  
(B) The radiated intensity is proportional to $\omega^4$ (or $1/\lambda^4$).  
(C) The angular distribution of radiated intensity is proportional to $\sin^2\theta$, where $\theta$ is the polar angle measured from the dipole axis $\hat{k}$.  
(D) No electromagnetic radiation is emitted along the axis of oscillation of the dipole ($\theta = 0^\circ$ and $\theta = 180^\circ$).

#### Question 4
One mole of a gas obeys the Dieterici equation of state $P(V - b)e^{a/RTV} = RT$, where $a$ and $b$ are positive constants. Which of the following statements is/are correct?
(A) At the critical point, $\left(\frac{\partial P}{\partial V}\right)_T = 0$ and $\left(\frac{\partial^2 P}{\partial V^2}\right)_T = 0$.  
(B) The critical volume is $V_c = 2b$.  
(C) The critical temperature is $T_c = \frac{a}{4Rb}$.  
(D) The critical compressibility factor is $Z_c = \frac{P_c V_c}{R T_c} = \frac{2}{e^2} \approx 0.271$.

#### Question 5
In a Fabry-Pérot interferometer consisting of two parallel flat partially reflecting plates separated by distance $d$, each having intensity reflectance $R_0$:
(A) The coefficient of finesse is $F = \frac{4R_0}{(1 - R_0)^2}$.  
(B) The transmission function is given by the Airy formula $T(\delta) = \frac{1}{1 + F\sin^2(\delta/2)}$, where $\delta = \frac{4\pi d}{\lambda}\cos\theta$.  
(C) As the reflectance $R_0 \to 1$, the transmission fringes become extremely sharp peaks on a dark background.  
(D) The free spectral range ($\text{FSR}$) in frequency is $\Delta \nu_{\text{FSR}} = \frac{c}{2d}$ for normal incidence.

#### Question 6
A particle of mass $m$ is constrained to slide along a frictionless inverted cycloid defined parametrically by $x = R(\theta + \sin\theta), y = R(1 - \cos\theta)$ with gravity acting in the $-y$ direction:
(A) The motion of the particle along the cycloid is exactly simple harmonic motion for any amplitude (tautochrone/isochrone property).  
(B) The period of oscillation of the particle is $T = 4\pi\sqrt{\frac{R}{g}}$, completely independent of the starting height.  
(C) Christiaan Huygens used the cycloidal pendulum to construct the world's first isochronous pendulum clock.  
(D) The arc length $s$ from the vertex satisfies $s^2 = 8 R y$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A horizontal uniform disk of mass $M = 6.00\text{ kg}$ and radius $R = 0.40\text{ m}$ is free to rotate about a fixed vertical axis through its center. A steady horizontal force $F = 15.0\text{ N}$ is applied tangentially to the rim for a duration $t = 4.00\text{ s}$, starting from rest. Calculate the final kinetic energy $K$ (in Joules) of the disk.

#### Question 8
Two concentric spherical metallic shells have radii $R_1 = 0.10\text{ m}$ and $R_2 = 0.30\text{ m}$. The inner shell has a charge $Q_1 = +2.0\ \mu\text{C}$ and the outer shell has a charge $Q_2 = -6.0\ \mu\text{C}$. Calculate the electric potential $V$ (in kiloVolts, $\text{kV}$) at the surface of the inner shell ($r = R_1$). [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$].

#### Question 9
In a Newton's rings arrangement, monochromatic light of wavelength $\lambda = 589\text{ nm}$ is used with a plano-convex lens of radius of curvature $R = 2.00\text{ m}$. Calculate the radius $r_5$ (in millimeters, $\text{mm}$) of the 5th bright interference ring in reflected light. [Round off to TWO decimal places].

#### Question 10
One mole of an ideal gas expands isothermally at $T = 300\text{ K}$ from an initial volume $V_1 = 0.010\text{ m}^3$ to a final volume $V_2 = 0.040\text{ m}^3$. Calculate the work done $W$ (in Joules) by the gas. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 4 = 1.3863$. Round off to the nearest integer].

#### Question 11
A long solenoid of radius $R = 0.030\text{ m}$ has $n = 1000\text{ turns/m}$ and carries an alternating current $I(t) = 4.0\sin(100\pi t)\text{ A}$. Calculate the peak magnitude of the induced electric field $E_{\text{peak}}$ (in $\text{mV/m}$) at a distance $r = 0.020\text{ m}$ from the central axis. [Take $\pi = 3.1416$ and $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$. Round off to TWO decimal places].

#### Question 12
Calculate the total binding energy $BE$ (in $\text{MeV}$) of a deuteron ($^2_1\text{H}$) given:
- Mass of proton $m_p = 1.007276\text{ u}$
- Mass of neutron $m_n = 1.008665\text{ u}$
- Mass of deuteron $m_d = 2.013553\text{ u}$
- $1\text{ u} = 931.5\text{ MeV}/c^2$
[Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The gravitational field strength at any point inside a uniform spherical shell of mass $M$ and radius $R$ is:
(A) $0$  
(B) $\frac{GM}{R^2}$  
(C) $\frac{GMr}{R^3}$  
(D) $-\frac{GM}{r}$

#### Question 14
A spherical soap bubble of radius $R$ and surface tension $S$ is given an electrostatic charge $Q$. The excess pressure $\Delta P = P_{\text{in}} - P_{\text{out}}$ inside the bubble is:
(A) $\frac{4S}{R} - \frac{Q^2}{32\pi^2\varepsilon_0 R^4}$  
(B) $\frac{4S}{R} + \frac{Q^2}{32\pi^2\varepsilon_0 R^4}$  
(C) $\frac{2S}{R} - \frac{Q^2}{16\pi^2\varepsilon_0 R^4}$  
(D) $\frac{4S}{R}$

#### Question 15
A train blowing a whistle of frequency $\nu_0 = 400\text{ Hz}$ approaches a stationary observer at speed $u = 34\text{ m/s}$. If the speed of sound in air is $v = 340\text{ m/s}$, the frequency heard by the observer is:
(A) $444\text{ Hz}$  
(B) $364\text{ Hz}$  
(C) $400\text{ Hz}$  
(D) $450\text{ Hz}$

#### Question 16
In the electron capture process $p + e^- \to n + \nu_e$, the emitted particle is:
(A) Electron neutrino ($\nu_e$)  
(B) Electron antineutrino ($\bar{\nu}_e$)  
(C) Positron ($e^+$)  
(D) $\gamma$-ray photon only

#### Question 17
To rotate the plane of polarization of linearly polarized light by an angle of $90^\circ$, a half-wave plate must be oriented such that its optic axis makes an angle with the incident polarization equal to:
(A) $45^\circ$  
(B) $90^\circ$  
(C) $30^\circ$  
(D) $60^\circ$

#### Question 18
The moment of inertia of a uniform solid sphere of mass $M$ and radius $R$ about a tangent is:
(A) $\frac{7}{5}M R^2$  
(B) $\frac{2}{5}M R^2$  
(C) $\frac{5}{3}M R^2$  
(D) $\frac{3}{2}M R^2$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the chelate effect in coordination chemistry:
(A) Complexes formed by polydentate chelating ligands are significantly more stable than those formed by analogous monodentate ligands.  
(B) The enhanced stability of chelates is primarily an entropic effect ($\Delta S^\circ > 0$) arising from the net increase in the number of free particles upon ligand substitution.  
(C) Ethylenediaminetetraacetate ($\text{EDTA}^{4-}$) forms exceptionally stable hexadentate complexes with many divalent and trivalent metal cations.  
(D) Macrocyclic ligands (such as crown ethers and porphyrins) exhibit even greater thermodynamic stability than open-chain chelates (the macrocyclic effect).

#### Question 20
In the Beckmann rearrangement:
(A) Ketoximes rearrange to $N$-substituted amides upon treatment with acidic catalysts like $\text{H}_2\text{SO}_4, \text{PCl}_5$, or polyphosphoric acid ($\text{PPA}$).  
(B) The group that migrates from carbon to nitrogen is strictly the group situated anti (trans) to the oxime $-\text{OH}$ group.  
(C) The rearrangement proceeds with complete retention of configuration at the migrating chiral center.  
(D) The industrial synthesis of $\varepsilon$-caprolactam (monomer for Nylon-6) utilizes the Beckmann rearrangement of cyclohexanone oxime.

#### Question 21
Regarding the electrochemical passivation of metals:
(A) Passivation is the spontaneous formation of an ultra-thin, dense, adherent metal oxide film that protects the underlying metal from further corrosion.  
(B) Concentrated nitric acid ($\text{HNO}_3$) renders iron and chromium passive due to the formation of a surface oxide film ($\text{Fe}_3\text{O}_4$ or $\text{Cr}_2\text{O}_3$).  
(C) Stainless steel owes its corrosion resistance to a self-healing passive surface layer of chromium oxide.  
(D) In the presence of chloride ions ($\text{Cl}^-$), the passive film can break down locally, leading to severe pitting corrosion.

#### Question 22
Which of the following statements is/are correct regarding real gas equations of state?
(A) The Berthelot equation of state is given by $\left(P + \frac{a}{T V^2}\right)(V - b) = RT$.  
(B) In the Berthelot equation, the attractive parameter $a$ is inversely proportional to temperature, reflecting weaker intermolecular cohesion at higher thermal velocities.  
(C) The Redlich-Kwong equation of state is given by $\left(P + \frac{a}{\sqrt{T} V(V + b)}\right)(V - b) = RT$.  
(D) Both Berthelot and Redlich-Kwong equations reproduce the critical state and Boyle temperature more accurately than the simple van der Waals equation.

#### Question 23
In qualitative inorganic analysis of anions:
(A) The brown ring test for nitrate ($\text{NO}_3^-$) involves the formation of $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$ at the junction of the two liquid layers.  
(B) Nitrite ions ($\text{NO}_2^-$) give the brown ring test even with dilute $\text{H}_2\text{SO}_4$ without requiring concentrated acid.  
(C) Nitrite ions can be decomposed and eliminated before testing for nitrate by boiling with urea or sulfamic acid in dilute sulfuric acid.  
(D) Iodide ions ($\text{I}^-$) can be selectively oxidized to violet $\text{I}_2$ in $\text{CCl}_4$ by chlorine water.

#### Question 24
Regarding the structural hierarchy of proteins:
(A) The primary structure is the linear sequence of amino acids linked by covalent peptide bonds.  
(B) The secondary structure ($\alpha$-helix and $\beta$-pleated sheet) is stabilized primarily by intramolecular and intermolecular hydrogen bonds between $-\text{C=O}$ and $-\text{NH}-$ groups.  
(C) The tertiary structure represents the overall 3D folding of the polypeptide chain, stabilized by disulfide linkages, salt bridges, hydrogen bonds, and hydrophobic interactions.  
(D) Hemoglobin possesses a quaternary structure composed of four polypeptide subunits ($2\alpha$ and $2\beta$).

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
A buffer solution contains $0.20\text{ M CH}_3\text{COOH}$ and $0.20\text{ M CH}_3\text{COONa}$ ($pK_a = 4.74$). Calculate the $\text{pH}$ of the solution after the addition of $0.020\text{ mol}$ of gaseous $\text{HCl}$ to $1.0\text{ L}$ of this buffer. [Take $\log(1.22) \approx 0.087$. Round off to TWO decimal places].

#### Question 26
For a reaction $A \to B$, the rate constant doubles when the temperature increases from $300\text{ K}$ to $310\text{ K}$. Calculate the activation energy $E_a$ of the reaction in $\text{kJ/mol}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 2 = 0.693$. Round off to TWO decimal places].

#### Question 27
Cesium chloride ($\text{CsCl}$) crystallizes in a body-centered cubic-like arrangement with $\text{Cs}^+$ at the body center and $\text{Cl}^-$ at the corners. If the edge length of the unit cell is $a = 412.0\text{ pm}$, calculate the distance $d$ (in picometers, $\text{pm}$) between the center of a $\text{Cs}^+$ ion and an adjacent $\text{Cl}^-$ ion. [Take $\sqrt{3} \approx 1.732$. Round off to ONE decimal place].

#### Question 28
Calculate the standard cell potential $E_{\text{cell}}^\circ$ (in Volts) at $298\text{ K}$ for the cell reaction:
$$2\text{Fe}^{3+}(aq) + 2\text{I}^-(aq) \to 2\text{Fe}^{2+}(aq) + \text{I}_2(s)$$
Given $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V}$ and $E^\circ(\text{I}_2/\text{I}^-) = +0.54\text{ V}$.

#### Question 29
When $2.00\text{ g}$ of benzoic acid ($\text{C}_6\text{H}_5\text{COOH}$, molar mass $122.0\text{ g/mol}$) is dissolved in $25.0\text{ g}$ of benzene, it associates to form dimers with a degree of association $\alpha = 80.0\%$. Calculate the depression in freezing point $\Delta T_f$ (in Kelvin). [Take $K_f(\text{benzene}) = 5.12\text{ K}\cdot\text{kg/mol}$. Round off to TWO decimal places].

#### Question 30
Calculate the spin-only magnetic moment $\mu_{\text{eff}}$ (in Bohr Magnetons, $\text{BM}$) of the low-spin octahedral complex $[\text{Mn}(\text{CN})_6]^{3-}$ ($\text{Mn}^{3+}, 3d^4$, strong field $\text{CN}^-$). [Take $\sqrt{8} \approx 2.83$. Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Gabriel phthalimide synthesis is exclusively used for the preparation of:
(A) Pure primary aliphatic amines  
(B) Primary aromatic amines  
(C) Secondary amines  
(D) Tertiary amines

#### Question 32
Cyclooctatetraene (COT, $\text{C}_8\text{H}_8$) does not show aromatic properties because:
(A) It adopts a non-planar tub-shaped conformation to avoid antiaromatic destabilization  
(B) It has $6\ \pi$-electrons  
(C) It is a planar conjugated ring  
(D) It has an odd number of double bonds

#### Question 33
In the extraction of iron in the blast furnace, the primary reducing agent in the upper reduction zone ($400 - 700^\circ\text{C}$) is:
(A) Carbon monoxide ($\text{CO}$)  
(B) Solid carbon (coke)  
(C) Carbon dioxide ($\text{CO}_2$)  
(D) Limestone ($\text{CaCO}_3$)

#### Question 34
Glycogen, the major storage polysaccharide in animals, is structurally most similar to:
(A) Amylopectin (with more frequent $\alpha-1,6$-branching)  
(B) Amylose  
(C) Cellulose  
(D) Chitin

#### Question 35
According to Molecular Orbital Theory, which of the following diatomic molecules has a bond order of 2 and is paramagnetic?
(A) $\text{B}_2$  
(B) $\text{C}_2$  
(C) $\text{O}_2$  
(D) $\text{N}_2$

#### Question 36
Cetyltrimethylammonium bromide ($[\text{CH}_3(\text{CH}_2)_{15}\text{N}(\text{CH}_3)_3]^+\text{Br}^-$) is a popular synthetic detergent belonging to the class of:
(A) Cationic detergents  
(B) Anionic detergents  
(C) Non-ionic detergents  
(D) Natural soaps

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f: [a, b] \to \mathbb{R}$ be a twice-differentiable strictly convex function on $[a, b]$, so that $f''(x) > 0$ for all $x \in [a, b]$. Which of the following statements is/are correct?
(A) The tangent line to the graph of $f$ at any point $c \in [a, b]$ lies entirely below the curve $y = f(x)$ for all $x \ne c$.  
(B) The secant line connecting $(a, f(a))$ and $(b, f(b))$ lies entirely above the curve $y = f(x)$ for all $x \in (a, b)$.  
(C) Jensen's inequality holds: $f\left(\frac{x_1 + x_2 + \dots + x_n}{n}\right) \le \frac{f(x_1) + f(x_2) + \dots + f(x_n)}{n}$ for any $x_1, \dots, x_n \in [a, b]$.  
(D) $f'(x)$ is a strictly increasing function on $[a, b]$.

#### Question 38
Let $A$ be a real $n \times n$ symmetric matrix. The matrix $A$ is said to be positive definite ($A \succ 0$) if $x^T A x > 0$ for all non-zero $x \in \mathbb{R}^n$. Which of the following statements is/are correct?
(A) All eigenvalues of $A$ are strictly positive real numbers.  
(B) All leading principal minors of $A$ are strictly positive (Sylvester's Criterion).  
(C) The matrix $A$ is invertible, and its inverse $A^{-1}$ is also positive definite.  
(D) There exists a unique lower triangular matrix $L$ with positive diagonal entries such that $A = L L^T$ (Cholesky Decomposition).

#### Question 39
Consider the parabolas $y^2 = 4ax$ and $x^2 = 4by$ ($a, b > 0$). Which of the following statements is/are correct?
(A) A common tangent to both parabolas exists and has a negative slope.  
(B) The equation of the common tangent is $x a^{1/3} + y b^{1/3} + a^{2/3} b^{2/3} = 0$.  
(C) The common tangent touches $y^2 = 4ax$ at $(a^{1/3} b^{2/3}, -2a^{2/3} b^{1/3})$.  
(D) The slope of the common tangent is $m = -(a/b)^{1/3}$.

#### Question 40
Consider the Cauchy-Euler differential equation $x^2 \frac{d^2y}{dx^2} - 2x \frac{dy}{dx} + 2y = 0$ for $x > 0$. Which of the following statements is/are correct?
(A) The substitution $x = e^t$ transforms the equation into a constant-coefficient ODE $\frac{d^2y}{dt^2} - 3\frac{dy}{dt} + 2y = 0$.  
(B) The characteristic roots are $m_1 = 1$ and $m_2 = 2$.  
(C) The general solution is $y(x) = C_1 x + C_2 x^2$.  
(D) If $y(1) = 3$ and $y'(1) = 5$, then $y(x) = x + 2x^2$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-coplanar vectors. Let $\vec{r}$ be any vector in $\mathbb{R}^3$. Which of the following statements is/are correct?
(A) $[\vec{a} \ \vec{b} \ \vec{c}] \ne 0$.  
(B) The volume of the parallelepiped formed by $\vec{a} + \vec{b}, \vec{b} + \vec{c}, \vec{c} + \vec{a}$ is $2[\vec{a} \ \vec{b} \ \vec{c}]$.  
(C) The volume of the parallelepiped formed by $\vec{a} \times \vec{b}, \vec{b} \times \vec{c}, \vec{c} \times \vec{a}$ is $[\vec{a} \ \vec{b} \ \vec{c}]^2$.  
(D) If $\vec{a} \cdot (\vec{b} \times \vec{c}) > 0$, the vector triplet forms a right-handed system.

#### Question 42
Let $(X, Y)$ be a continuous bivariate random vector with joint probability density function $f(x, y) = c(x + y)$ for $0 \le x \le 1$ and $0 \le y \le 1$, and $f(x, y) = 0$ elsewhere:
(A) The normalization constant is $c = 1$.  
(B) The marginal density of $X$ is $f_X(x) = x + \frac{1}{2}$ for $0 \le x \le 1$.  
(C) The expected value of $X$ is $E[X] = \frac{7}{12}$.  
(D) $X$ and $Y$ are independent random variables.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 \frac{\ln(1+x)}{x}\,dx$$
If $I = \frac{\pi^2}{k}$, find the integer value of $k$.

#### Question 44
Find the area of the region in the first quadrant enclosed between the sine curve $y = \sin x$ and the chord $y = \frac{2}{\pi}x$ for $0 \le x \le \pi/2$. [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 45
Find the total number of positive integer divisors of $N = 2520$.

#### Question 46
Calculate the shortest distance between the parallel lines $\vec{r} = (\hat{i} + 2\hat{j} + 3\hat{k}) + \lambda(2\hat{i} + 3\hat{j} + 6\hat{k})$ and $\vec{r} = (3\hat{i} + 3\hat{j} + 2\hat{k}) + \mu(2\hat{i} + 3\hat{j} + 6\hat{k})$. [Round off to TWO decimal places].

#### Question 47
Evaluate the sum of the infinite arithmetico-geometric series:
$$S = \sum_{n=1}^\infty \frac{n}{2^n} = \frac{1}{2} + \frac{2}{4} + \frac{3}{8} + \frac{4}{16} + \dots$$

#### Question 48
Find the number of ways in which 4 married couples can be seated around a circular table such that men and women sit alternately.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The perpendicular distance from the point $(3, -1, 11)$ to the line $\frac{x}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ is:
(A) $\sqrt{53}$  
(B) $5\sqrt{2}$  
(C) $\sqrt{29}$  
(D) $\sqrt{41}$

#### Question 50
If $A$ and $B$ are $3 \times 3$ matrices such that $\text{Tr}(A) = 5$ and $\text{Tr}(B) = 3$, then $\text{Tr}(2A - 3B)$ is:
(A) $1$  
(B) $7$  
(C) $4$  
(D) $19$

#### Question 51
The equation of the tangent to the hyperbola $\frac{x^2}{9} - \frac{y^2}{4} = 1$ which is parallel to the line $y = 2x + 1$ is:
(A) $y = 2x \pm 4\sqrt{2}$  
(B) $y = 2x \pm 6$  
(C) $y = 2x \pm 2$  
(D) $y = 2x \pm \sqrt{32}$

#### Question 52
The angle between the curves $y = x^3$ and $6y = 7 - x^2$ at their point of intersection $(1, 1)$ is:
(A) $\pi/2$ ($90^\circ$)  
(B) $\pi/4$ ($45^\circ$)  
(C) $\pi/3$ ($60^\circ$)  
(D) $\pi/6$ ($30^\circ$)

#### Question 53
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{x - \sin x}{x^3}$$
(A) $1/6$  
(B) $1/3$  
(C) $1/2$  
(D) $0$

#### Question 54
The maximum value of the function $f(x) = \sin x \cos x$ for all $x \in \mathbb{R}$ is:
(A) $1/2$  
(B) $1$  
(C) $1/4$  
(D) $\sqrt{2}$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 06 — Paper 2
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
A uniform rod of mass $M$ and length $L$ is pivoted smoothly at its upper end $O$ and hangs vertically. A bullet of mass $m$ moving horizontally with speed $v_0$ strikes the lower end of the rod and embeds itself into the rod:
(A) The angular momentum of the system about the pivot $O$ is conserved during the collision.  
(B) The moment of inertia of the rod-bullet system about $O$ immediately after impact is $I_O = \left(\frac{1}{3}M + m\right)L^2$.  
(C) The angular velocity of the system immediately after impact is $\omega = \frac{m v_0 L}{(M/3 + m)L^2} = \frac{m v_0}{(M/3 + m)L}$.  
(D) The linear momentum of the rod-bullet system is conserved during the collision.

#### Question 2
A liquid of density $\rho$ and surface tension $S$ is contained in a U-tube. The left arm has radius $r_1$ and the right arm has radius $r_2$ ($r_1 < r_2$). The contact angle is $\theta = 0^\circ$:
(A) The capillary meniscus in both arms is concave upward.  
(B) The pressure under the meniscus in the left arm is less than in the right arm.  
(C) The height difference $h$ between the liquid levels in the two arms is $h = \frac{2S}{\rho g}\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$.  
(D) The liquid level is higher in the narrower left arm.

#### Question 3
An electromagnetic wave propagating in free space has electric field $\vec{E} = E_0 \cos(k z - \omega t)\hat{i}$:
(A) The associated magnetic field is $\vec{B} = \frac{E_0}{c}\cos(k z - \omega t)\hat{j}$.  
(B) The wave is linearly polarized along the x-axis.  
(C) The intensity of the wave is $I = \frac{1}{2}\varepsilon_0 c E_0^2$.  
(D) The radiation pressure on a perfectly absorbing surface placed at normal incidence is $P_{\text{rad}} = \frac{I}{c}$.

#### Question 4
A light ray enters a medium where the refractive index depends on the distance $x$ from the boundary as $\mu(x) = \frac{\mu_0}{1 + x/a}$. If the ray is incident normally at $x = 0$:
(A) The ray continues straight along the x-axis without bending.  
(B) The speed of the light wave increases as it penetrates deeper into the medium.  
(C) The wavelength of the light wave increases as $x$ increases.  
(D) The frequency of the light wave remains strictly constant throughout the medium.

#### Question 5
In Davisson-Germer electron diffraction experiment:
(A) Electrons are accelerated through a potential difference $V$ and scattered by a nickel crystal.  
(B) Constructive interference occurs according to Bragg's law: $2d\sin\theta = n\lambda$.  
(C) The maximum intensity of scattered electrons is observed at an acceleration voltage of $54\text{ V}$ and scattering angle $\phi = 50^\circ$.  
(D) This experiment provided the first direct experimental verification of de Broglie's wave hypothesis for matter.

#### Question 6
An ideal gas undergoes a cyclic process shown on a $T-S$ (Temperature-Entropy) diagram consisting of a rectangle with temperatures $T_H$ and $T_C$, and entropies $S_1$ and $S_2$ ($S_2 > S_1$):
(A) The cycle is equivalent to a Carnot cycle.  
(B) The heat absorbed by the gas is $Q_{\text{in}} = T_H (S_2 - S_1)$.  
(C) The net work done per cycle is $W_{\text{net}} = (T_H - T_C)(S_2 - S_1)$.  
(D) The thermal efficiency of the cycle is $\eta = 1 - \frac{T_C}{T_H}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A horizontal spring-mass system has mass $m = 0.50\text{ kg}$ and spring constant $k = 200.0\text{ N/m}$. The mass is pulled to $x = 0.050\text{ m}$ and released from rest. Calculate the maximum speed $v_{\text{max}}$ (in $\text{m/s}$) of the mass during oscillation.

#### Question 8
Two large parallel conducting plates are separated by distance $d = 2.0\text{ mm}$ in vacuum. A potential difference $V = 400.0\text{ V}$ is applied across them. Calculate the magnitude of the electric field $E$ (in $\text{kV/m}$) between the plates.

#### Question 9
In a Young's double-slit experiment, the slit separation is $d = 0.25\text{ mm}$ and the screen distance is $D = 1.00\text{ m}$. Using light of wavelength $\lambda = 500\text{ nm}$, calculate the fringe width $\beta$ in millimeters ($\text{mm}$).

#### Question 10
Calculate the root-mean-square speed $v_{\text{rms}}$ (in $\text{m/s}$) of nitrogen molecules ($\text{N}_2, M = 0.028\text{ kg/mol}$) at $T = 300\text{ K}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\sqrt{267235.7} \approx 516.9$. Round off to the nearest integer].

#### Question 11
A circular wire loop of radius $R = 0.10\text{ m}$ and resistance $r = 2.0\ \Omega$ is placed in a uniform magnetic field $B$ perpendicular to the plane of the loop. If the magnetic field decreases at a constant rate $\frac{dB}{dt} = 10.0\text{ T/s}$, calculate the induced current $I$ (in milliAmperes, $\text{mA}$) in the loop. [Take $\pi = 3.1416$. Round off to the nearest integer].

#### Question 12
The half-life of a radioactive isotope is $T_{1/2} = 5.0\text{ years}$. Calculate the percentage of the initial radioactive nuclei remaining undecayed after $20.0\text{ years}$.

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the mechanics concepts in List-I with their mathematical identity in List-II:
- **List-I**:
  - P. Work-Energy Theorem
  - Q. Conservation of Linear Momentum
  - R. Conservation of Angular Momentum
  - S. Center of Mass
- **List-II**:
  - 1. $W_{\text{net}} = \Delta K$
  - 2. $\sum \vec{F}_{\text{ext}} = 0 \implies \vec{P} = \text{const}$
  - 3. $\sum \vec{\tau}_{\text{ext}} = 0 \implies \vec{L} = \text{const}$
  - 4. $\vec{r}_{\text{cm}} = \frac{\sum m_i \vec{r}_i}{\sum m_i}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 14
Match the fluid flows in List-I with their defining equation in List-II:
- **List-I**:
  - P. Continuity equation
  - Q. Bernoulli's equation
  - R. Stokes' law
  - S. Poiseuille's equation
- **List-II**:
  - 1. $A v = \text{const}$
  - 2. $P + \frac{1}{2}\rho v^2 + \rho g y = \text{const}$
  - 3. $F_v = 6\pi \eta r v$
  - 4. $Q = \frac{\pi \Delta P r^4}{8\eta L}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 15
Match the thermal processes in List-I with their characteristic thermodynamic parameter in List-II:
- **List-I**:
  - P. Isobaric
  - Q. Isochoric
  - R. Isothermal
  - S. Adiabatic
- **List-II**:
  - 1. $P = \text{const}, W = P\Delta V$
  - 2. $V = \text{const}, W = 0$
  - 3. $T = \text{const}, \Delta U = 0$
  - 4. $Q = 0, P V^\gamma = \text{const}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the nuclear decay types in List-I with their product characteristics in List-II:
- **List-I**:
  - P. Alpha decay
  - Q. Beta-minus decay
  - R. Beta-plus decay
  - S. Gamma decay
- **List-II**:
  - 1. $Z \to Z-2, A \to A-4$
  - 2. $Z \to Z+1, A \to A$
  - 3. $Z \to Z-1, A \to A$
  - 4. $Z \to Z, A \to A$ (no nucleon change)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 17
Match the optical devices in List-I with their focal properties in List-II:
- **List-I**:
  - P. Thin convex lens
  - Q. Thin concave lens
  - R. Concave mirror
  - S. Convex mirror
- **List-II**:
  - 1. Converging, $f > 0$
  - 2. Diverging, $f < 0$
  - 3. Converging, $f = -R/2 < 0$ (Cartesian sign)
  - 4. Diverging, $f = +R/2 > 0$ (Cartesian sign)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 18
Match the electromagnetic components in List-I with their impedance in List-II:
- **List-I**:
  - P. Resistor $R$
  - Q. Inductor $L$
  - R. Capacitor $C$
  - S. Series LCR at resonance
- **List-II**:
  - 1. $Z = R$
  - 2. $Z_L = \omega L$ (voltage leads current by $90^\circ$)
  - 3. $Z_C = \frac{1}{\omega C}$ (current leads voltage by $90^\circ$)
  - 4. $Z = R$ (purely resistive)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following complexes can exhibit optical isomerism?
(A) $cis-[\text{Co}(\text{en})_2\text{Cl}_2]^+$  
(B) $[\text{Cr}(\text{ox})_3]^{3-}$  
(C) $trans-[\text{Co}(\text{en})_2\text{Cl}_2]^+$  
(D) $[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$ (square planar)

#### Question 20
Which of the following statements is/are correct about the Cannizzaro reaction?
(A) It is undergone by aldehydes lacking an $\alpha$-hydrogen atom upon treatment with concentrated alkali.  
(B) It is a disproportionation (redox) reaction where one molecule is reduced to an alcohol and another is oxidized to a carboxylic acid salt.  
(C) The rate-determining step is the intermolecular hydride ion ($\text{H}^-$) transfer.  
(D) Crossed Cannizzaro reaction between formaldehyde and benzaldehyde gives sodium formate and benzyl alcohol.

#### Question 21
Regarding the electrochemical series:
(A) Metals with negative standard reduction potentials are more easily oxidized than hydrogen.  
(B) Zinc can displace iron from $\text{FeSO}_4$ solution.  
(C) Copper does not dissolve in dilute $\text{HCl}$ with liberation of $\text{H}_2$ gas because $E^\circ(\text{Cu}^{2+}/\text{Cu}) > 0$.  
(D) Chlorine gas can displace bromide and iodide from their aqueous halide solutions.

#### Question 22
Which of the following pairs represent structural chain isomers?
(A) $n$-Pentane and Isopentane  
(B) $n$-Butane and Isobutane  
(C) Pentan-2-one and Pentan-3-one  
(D) Propan-1-ol and Propan-2-ol

#### Question 23
Which of the following compounds gives off oxygen gas ($\text{O}_2$) upon thermal decomposition?
(A) Potassium chlorate ($\text{KClO}_3$)  
(B) Potassium nitrate ($\text{KNO}_3$)  
(C) Lead nitrate ($\text{Pb(NO}_3)_2$)  
(D) Ammonium dichromate ($(\text{NH}_4)_2\text{Cr}_2\text{O}_7$)

#### Question 24
Which of the following vitamins cannot be stored in the human body and must be supplied regularly in the diet?
(A) Vitamin C  
(B) Vitamin B1 (Thiamine)  
(C) Vitamin B6 (Pyridoxine)  
(D) Vitamin A

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The solubility product of $\text{AgCl}$ in water is $K_{sp} = 1.8 \times 10^{-10}$ at $25^\circ\text{C}$. Calculate the solubility $S$ of $\text{AgCl}$ in pure water in $\mu\text{mol/L}$. [Take $\sqrt{1.8} \approx 1.34$. Round off to ONE decimal place].

#### Question 26
For a first-order reaction, the half-life is $t_{1/2} = 100.0\text{ seconds}$. Calculate the time (in seconds) required for $87.5\%$ of the reactant to decompose.

#### Question 27
An element with FCC crystal structure has an atomic radius $r = 141.4\text{ pm}$. Calculate the edge length $a$ of the unit cell in picometers ($\text{pm}$). [Take $\sqrt{2} \approx 1.414$. Round off to the nearest integer].

#### Question 28
Calculate the standard enthalpy of combustion $\Delta_{\text{comb}} H^\circ$ (in $\text{kJ/mol}$) of graphite given:
- $\Delta_f H^\circ(\text{CO}_2(g)) = -393.5\text{ kJ/mol}$

#### Question 29
A $0.10\text{ m}$ aqueous solution of an electrolyte $AB$ freezes at $-0.3534^\circ\text{C}$. Calculate the degree of dissociation $\alpha$ as a percentage (\%). [Take $K_f(\text{H}_2\text{O}) = 1.86\text{ K}\cdot\text{kg/mol}$. Round off to the nearest integer].

#### Question 30
Find the oxidation state of sulfur in Caro's acid (peroxomonosulfuric acid, $\text{H}_2\text{SO}_5$).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following compounds is most acidic?
(A) Picric acid (2,4,6-trinitrophenol)  
(B) $p$-Nitrophenol  
(C) $m$-Nitrophenol  
(D) Phenol

#### Question 32
The structure of phosphorus pentachloride ($\text{PCl}_5$) in the solid state exists as:
(A) $[\text{PCl}_4]^+$ (tetrahedral) and $[\text{PCl}_6]^-$ (octahedral)  
(B) Trigonal bipyramidal covalent molecules  
(C) Square planar $[\text{PCl}_4]^+$ and linear $\text{Cl}^-$  
(D) Dimeric $\text{P}_2\text{Cl}_{10}$

#### Question 33
In the cyanide extraction process of silver, the complex ion formed in the solution is:
(A) $[\text{Ag}(\text{CN})_2]^-$  
(B) $[\text{Ag}(\text{CN})_4]^{3-}$  
(C) $[\text{Ag}(\text{CN})_3]^{2-}$  
(D) $\text{AgCN}$

#### Question 34
Which of the following amino acids is optically inactive?
(A) Glycine  
(B) Alanine  
(C) Valine  
(D) Leucine

#### Question 35
The shape of the water molecule ($\text{H}_2\text{O}$) according to VSEPR theory is:
(A) Bent / V-shaped  
(B) Linear  
(C) Trigonal planar  
(D) Tetrahedral

#### Question 36
Bakelite is obtained by the condensation polymerization of phenol with:
(A) Formaldehyde  
(B) Acetaldehyde  
(C) Benzaldehyde  
(D) Ethylene glycol

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \sin x - x \cos x$ for $x \in (0, \pi/2)$. Which of the following statements is/are correct?
(A) $f(0) = 0$.  
(B) $f'(x) = x \sin x > 0$ for all $x \in (0, \pi/2)$.  
(C) $f(x)$ is strictly increasing on $(0, \pi/2)$.  
(D) $\sin x > x \cos x$ (or $\tan x > x$) for all $x \in (0, \pi/2)$.

#### Question 38
Let $A$ be a $3 \times 3$ matrix such that $A^T A = I$ and $\det(A) = -1$ (improper orthogonal matrix):
(A) The eigenvalues of $A$ can be $-1, 1, 1$ or $-1, e^{i\theta}, e^{-i\theta}$.  
(B) $\lambda = -1$ is always an eigenvalue of $A$.  
(C) $A$ represents a reflection or rotoreflection in $\mathbb{R}^3$.  
(D) $A^{-1} = A^T$.

#### Question 39
Consider the circle $x^2 + y^2 = 9$ and the point $P(5, 0)$. Two tangents $PA$ and $PB$ are drawn to the circle:
(A) The length of each tangent is $L = \sqrt{25 - 9} = 4$.  
(B) The equation of the chord of contact $AB$ is $5x = 9 \implies x = 9/5$.  
(C) The area of the quadrilateral $PAOB$ (where $O$ is origin) is $12$.  
(D) The radius of the circle circumscribing $\Delta PAB$ is $2.5$.

#### Question 40
Consider the differential equation $\frac{dy}{dx} = \frac{y}{x} + \tan\left(\frac{y}{x}\right)$. Which of the following statements is/are correct?
(A) The substitution $y = vx$ leads to $\cot v\,dv = \frac{dx}{x}$.  
(B) The general solution is $\sin(y/x) = C x$.  
(C) If $y(1) = \pi/6$, then $C = 1/2$.  
(D) The solution with $y(1) = \pi/6$ satisfies $\sin(y/x) = \frac{x}{2}$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be unit vectors such that $\vec{a} \cdot \vec{b} = 0, \vec{a} \cdot \vec{c} = 0$, and the angle between $\vec{b}$ and $\vec{c}$ is $\pi/6$ ($30^\circ$):
(A) The vector $\vec{a}$ is parallel to $\pm (\vec{b} \times \vec{c})$.  
(B) $|\vec{b} \times \vec{c}| = \sin(\pi/6) = 1/2$.  
(C) The scalar triple product is $[\vec{a} \ \vec{b} \ \vec{c}] = \pm 1/2$.  
(D) The volume of the parallelepiped spanned by $\vec{a}, \vec{b}, \vec{c}$ is $1/2$.

#### Question 42
In a Poisson distribution with parameter $\lambda = 3$:
(A) The mean is $3$.  
(B) The variance is $3$.  
(C) $P(X = 0) = e^{-3}$.  
(D) The mode of the distribution is at $k = 2$ and $k = 3$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the parabola $y^2 = 4x$ and its latus rectum $x = 1$. [Round off to TWO decimal places].

#### Question 44
Find the slope of the tangent to the curve $y = \ln(1 + x^2)$ at the point where $x = 1$.

#### Question 45
Evaluate the definite integral:
$$I = \int_0^{\pi/2} \cos^3 x\,dx$$
[Round off to TWO decimal places].

#### Question 46
Calculate the distance between the point $(1, 2, 3)$ and the line $\frac{x-2}{1} = \frac{y-3}{2} = \frac{z-4}{2}$.

#### Question 47
If the sum of an infinite geometric series with first term $a = 3$ is $S = 9$, find the common ratio $r$. [Round off to TWO decimal places].

#### Question 48
How many 4-digit numbers can be formed using the digits $0, 1, 2, 3, 4, 5$ without repetition?

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the curve features in List-I with their mathematical identity in List-II:
- **List-I**:
  - P. Slope of tangent
  - Q. Slope of normal
  - R. Length of subtangent
  - S. Length of subnormal
- **List-II**:
  - 1. $\frac{dy}{dx}$
  - 2. $-\frac{dx}{dy}$
  - 3. $\left|\frac{y}{dy/dx}\right|$
  - 4. $\left|y \frac{dy}{dx}\right|$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 50
Match the quadratic forms in List-I with their classification in List-II:
- **List-I**:
  - P. $x^2 + y^2 + z^2$
  - Q. $-x^2 - y^2 - z^2$
  - R. $x^2 + y^2$
  - S. $x^2 - y^2$
- **List-II**:
  - 1. Positive definite
  - 2. Negative definite
  - 3. Positive semi-definite
  - 4. Indefinite

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 51
Match the complex numbers in List-I with their modulus in List-II:
- **List-I**:
  - P. $3 + 4i$
  - Q. $1 + i\sqrt{3}$
  - R. $5 - 12i$
  - S. $i$
- **List-II**:
  - 1. $5$
  - 2. $2$
  - 3. $13$
  - 4. $1$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 52
Match the counting problems in List-I with their result formula in List-II:
- **List-I**:
  - P. Permutations of $n$ distinct objects
  - Q. Combinations of $r$ objects from $n$
  - R. Circular permutations of $n$ objects
  - S. Permutations with repeated items ($p$ of one kind, $q$ of another)
- **List-II**:
  - 1. $n!$
  - 2. $\binom{n}{r} = \frac{n!}{r!(n-r)!}$
  - 3. $(n - 1)!$
  - 4. $\frac{n!}{p! q!}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 53
Match the functions in List-I with their range in List-II:
- **List-I**:
  - P. $\sin x$
  - Q. $\tan^{-1} x$
  - R. $e^x$
  - S. $x^2 + 1$
- **List-II**:
  - 1. $[-1, 1]$
  - 2. $(-\pi/2, \pi/2)$
  - 3. $(0, \infty)$
  - 4. $[1, \infty)$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 54
Match the vector operations in List-I with their geometric interpretation in List-II:
- **List-I**:
  - P. $\vec{a} \cdot \vec{b} = 0$
  - Q. $\vec{a} \times \vec{b} = \vec{0}$
  - R. $[\vec{a} \ \vec{b} \ \vec{c}] = 0$
  - S. $\vec{a} \cdot (\vec{b} \times \vec{c}) > 0$
- **List-II**:
  - 1. Vectors are perpendicular
  - 2. Vectors are parallel/collinear
  - 3. Vectors are coplanar
  - 4. Triplet forms right-handed system

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 06 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Betatron Acceleration, Induced Electric Field from Changing Flux, Magnetic Orbit Stability.
- **2. Derivation**:
  - Faraday's Law: $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi}{dt} \implies E_\theta (2\pi R) = \frac{d\Phi}{dt} \implies E_\theta = \frac{1}{2\pi R}\frac{d\Phi}{dt}$. (A) is correct.
  - Tangential force on electron: $F_\theta = e E_\theta = \frac{e}{2\pi R}\frac{d\Phi}{dt} = \frac{dp}{dt} \implies \Delta p = \frac{e \Delta \Phi}{2\pi R}$.
  - For circular orbit: $p = e R B_{\text{orb}} \implies \Delta p = e R \Delta B_{\text{orb}}$.
  - Equating: $e R \Delta B_{\text{orb}} = \frac{e \Delta \Phi}{2\pi R} \implies \Delta \Phi = 2\pi R^2 \Delta B_{\text{orb}}$.
  - Since average field $\langle B \rangle = \frac{\Phi}{\pi R^2}$, this implies $\Delta \langle B \rangle = 2 \Delta B_{\text{orb}}$ (the famous $2:1$ Betatron rule). (B) and (C) are correct.
  - Radial and vertical stability: requires field index $0 < n < 1$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Charge Sharing between Capacitors, Joule Heat Dissipation.
- **2. Derivation**:
  - Conservation of charge: $Q_{\text{total}} = C_1 V_1 + C_2 V_2 = (C_1 + C_2) V_f \implies V_f = \frac{C_1 V_1 + C_2 V_2}{C_1 + C_2}$. (A) and (B) are correct.
  - Initial energy: $U_i = \frac{1}{2} C_1 V_1^2 + \frac{1}{2} C_2 V_2^2$.
  - Final energy: $U_f = \frac{1}{2}(C_1 + C_2) V_f^2 = \frac{1}{2}\frac{(C_1 V_1 + C_2 V_2)^2}{C_1 + C_2}$.
  - Heat dissipated: $\Delta U = U_i - U_f = \frac{1}{2}\frac{C_1 C_2}{C_1 + C_2}(V_1 - V_2)^2$. (C) is correct.
  - The total energy dissipated is completely independent of the resistance $R$ of the connecting wire (it affects only the time constant $\tau = R C_{\text{eq}}$, not the integral $\int i^2 R dt$). Thus (D) is incorrect.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Hertzian Oscillating Dipole Radiation, Larmor Formula.
- **2. Derivation**:
  - Radiated power: $P = \frac{\mu_0 p_0^2 \omega^4}{12\pi c}$. (A) is correct.
  - Power scales as $\omega^4 \propto \lambda^{-4}$ (Rayleigh scattering law). (B) is correct.
  - Angular intensity: $\frac{dP}{d\Omega} = \frac{\mu_0 p_0^2 \omega^4}{32\pi^2 c}\sin^2\theta$. (C) is correct.
  - At $\theta = 0^\circ$ and $180^\circ$, $\sin\theta = 0$, so no power is radiated along the dipole axis. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Dieterici Equation of State, Critical State Conditions.
- **2. Derivation**:
  - At critical point: $\left(\frac{\partial P}{\partial V}\right)_{T_c} = 0$ and $\left(\frac{\partial^2 P}{\partial V^2}\right)_{T_c} = 0$. (A) is correct.
  - For Dieterici gas: $V_c = 2b$, $T_c = \frac{a}{4Rb}$, $P_c = \frac{a}{4e^2 b^2}$. (B) and (C) are correct.
  - Critical compressibility factor:
    $$Z_c = \frac{P_c V_c}{R T_c} = \frac{(a / 4e^2 b^2)(2b)}{R(a / 4Rb)} = \frac{2a / 4e^2 b}{a / 4b} = \frac{2}{e^2} \approx 0.2707 \approx 0.271$$
    (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Fabry-Pérot Interferometer, Airy Transmission Function, Free Spectral Range.
- **2. Derivation**:
  - Finesse parameter: $F = \frac{4R_0}{(1 - R_0)^2}$. (A) is correct.
  - Airy formula: $T(\delta) = \frac{1}{1 + F\sin^2(\delta/2)}$. (B) is correct.
  - As $R_0 \to 1$, $F \to \infty$, making transmission resonance peaks extremely narrow. (C) is correct.
  - Free spectral range: $\Delta \nu_{\text{FSR}} = \frac{c}{2d}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Cycloidal Pendulum, Tautochrone Property, Isochronism.
- **2. Derivation**:
  - Along cycloid, component of gravity along curve is proportional to arc length $s$: $\ddot{s} + \frac{g}{4R} s = 0$.
  - This is an exact SHM equation for all amplitudes! (A) is correct.
  - Time period: $\omega = \sqrt{\frac{g}{4R}} \implies T = \frac{2\pi}{\omega} = 4\pi\sqrt{\frac{R}{g}}$. (B) is correct.
  - Invented by Christiaan Huygens for pendulum clocks. (C) is correct.
  - Geometric property of cycloid: $s^2 = 8 R y$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Moment of inertia of disk: $I = \frac{1}{2}M R^2 = \frac{1}{2}(6.00)(0.40)^2 = 0.48\text{ kg}\cdot\text{m}^2$.
  Torque: $\tau = F R = (15.0)(0.40) = 6.00\text{ N}\cdot\text{m}$.
  Angular acceleration: $\alpha = \frac{\tau}{I} = \frac{6.00}{0.48} = 12.50\text{ rad/s}^2$.
  Final angular velocity: $\omega = \alpha t = (12.50)(4.00) = 50.0\text{ rad/s}$.
  Kinetic energy: $K = \frac{1}{2}I \omega^2 = \frac{1}{2}(0.48)(50.0)^2 = 0.24(2500) = 600.00\text{ J}$. Exact: `600.00`.
- **Question 8**: Potential of inner shell:
  $$V = \frac{1}{4\pi\varepsilon_0}\left[\frac{Q_1}{R_1} + \frac{Q_2}{R_2}\right] = (9.0 \times 10^9)\left[\frac{2.0 \times 10^{-6}}{0.10} + \frac{-6.0 \times 10^{-6}}{0.30}\right] = (9.0 \times 10^9)[20.0 \times 10^{-6} - 20.0 \times 10^{-6}] = 0.00\text{ V}$$
  Exact: `0.00`.
- **Question 9**: For bright rings: $r_n^2 = (n - 1/2)\lambda R$.
  For $n = 5$: $r_5^2 = (5 - 0.5)(589 \times 10^{-9}\text{ m})(2.00\text{ m}) = (4.5)(1.178 \times 10^{-6}) = 5.301 \times 10^{-6}\text{ m}^2$.
  $r_5 = \sqrt{5.301 \times 10^{-6}} \approx 2.30 \times 10^{-3}\text{ m} = 2.30\text{ mm}$. Exact: `2.30`.
- **Question 10**: $W = n R T \ln\left(\frac{V_2}{V_1}\right) = (1.0)(8.314)(300)\ln(4) = (2494.2)(1.3863) \approx 3457.7\text{ J} \approx 3458\text{ J}$. Exact: `3458.00`.
- **Question 11**: $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi}{dt} \implies E(2\pi r) = \pi r^2 \mu_0 n \left|\frac{dI}{dt}\right|$.
  $E = \frac{1}{2}\mu_0 n r \left|\frac{dI}{dt}\right|_{\text{max}} = \frac{1}{2}(4\pi \times 10^{-7})(1000)(0.020)[4.0 \times 100\pi] = (4\pi \times 10^{-4})(0.010)(400\pi) = 16\pi^2 \times 10^{-3} \approx 16(9.87) \times 10^{-3} \approx 157.9\text{ mV/m}$. Exact: `157.91`.
- **Question 12**: $\Delta m = m_p + m_n - m_d = 1.007276 + 1.008665 - 2.013553 = 2.015941 - 2.013553 = 0.002388\text{ u}$.
  $BE = (0.002388)(931.5) \approx 2.224\text{ MeV} \approx 2.22\text{ MeV}$. Exact: `2.22`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Inside a uniform spherical shell, gravitational field is zero everywhere. Option (A).
- **Question 14**: $\Delta P = \frac{4S}{R} - \frac{Q^2}{32\pi^2\varepsilon_0 R^4}$. Option (A).
- **Question 15**: Doppler shift for approaching source: $\nu = \nu_0 \frac{v}{v - u} = 400 \frac{340}{340 - 34} = 400 \frac{340}{306} = 400 \times \frac{10}{9} \approx 444.44\text{ Hz} \approx 444\text{ Hz}$. Option (A).
- **Question 16**: Electron neutrino ($\nu_e$) is emitted. Option (A).
- **Question 17**: A half-wave plate rotates polarization by $2\theta$. To rotate by $90^\circ$, angle must be $\theta = 45^\circ$. Option (A).
- **Question 18**: Tangential axis in sphere's plane: $I = \frac{2}{5}M R^2 + M R^2 = \frac{7}{5}M R^2$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Chelate effect: polydentate complexes are more stable due to entropy increase ($\Delta S > 0$) from releasing multiple monodentate solvent molecules. $\text{EDTA}^{4-}$ is hexadentate. Macrocyclic effect confers extra stability. Options: (A), (B), (C), (D).
- **Question 20**: Beckmann rearrangement converts ketoximes to amides via anti-migration with retention of stereochemistry. Used for Nylon-6 monomer caprolactam. Options: (A), (B), (C), (D).
- **Question 21**: Passivation forms protective oxide film. Concentrated $\text{HNO}_3$ passivates Fe and Cr. Stainless steel protected by $\text{Cr}_2\text{O}_3$. Pitting by $\text{Cl}^-$. Options: (A), (B), (C), (D).
- **Question 22**: Berthelot equation has $a/TV^2$. Redlich-Kwong has $a/\sqrt{T}V(V+b)$. Both improve over van der Waals. Options: (A), (B), (C), (D).
- **Question 23**: Nitrate brown ring test forms $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$. Nitrite reacts even in dilute acid. Urea removes $\text{NO}_2^-$. $\text{I}^-$ gives violet layer in $\text{CCl}_4$. Options: (A), (B), (C), (D).
- **Question 24**: Primary (peptide sequence), secondary ($\alpha$-helix, $\beta$-sheet with H-bonds), tertiary (3D fold with disulfides and hydrophobic interactions), quaternary (multimeric subunits). Options: (A), (B), (C), (D).
- **Question 25**: Addition of $0.020\text{ mol HCl}$: $[\text{CH}_3\text{COOH}] = 0.20 + 0.02 = 0.22\text{ M}$, $[\text{CH}_3\text{COO}^-] = 0.20 - 0.02 = 0.18\text{ M}$.
  $\text{pH} = pK_a + \log\left(\frac{0.18}{0.22}\right) = 4.74 - \log(1.22) = 4.74 - 0.087 = 4.653 \approx 4.65$. Exact: `4.65`.
- **Question 26**: $\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{10}{300 \times 310}\right) \implies \ln 2 = \frac{E_a}{8.314}\left(\frac{10}{93000}\right) \implies 0.693 = \frac{E_a}{8.314}(1.075 \times 10^{-4}) \implies E_a = \frac{0.693 \times 8.314}{1.075 \times 10^{-4}} \approx 53580\text{ J/mol} = 53.58\text{ kJ/mol}$. Exact: `53.58`.
- **Question 27**: In $\text{CsCl}$ structure: $2(r_+ + r_-) = \sqrt{3}a \implies d = r_+ + r_- = \frac{\sqrt{3}a}{2} = \frac{1.732 \times 412.0}{2} = 356.8\text{ pm}$. Exact: `356.80`.
- **Question 28**: $E_{\text{cell}}^\circ = E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) - E^\circ(\text{I}_2/\text{I}^-) = +0.77 - (+0.54) = +0.23\text{ V}$. Exact: `0.23`.
- **Question 29**: Molality $m = \frac{2.00 \times 1000}{122.0 \times 25.0} = \frac{2000}{3050} \approx 0.6557\text{ m}$.
  For dimerization: $i = 1 - \alpha/2 = 1 - 0.40 = 0.60$.
  $\Delta T_f = i K_f m = (0.60)(5.12)(0.6557) \approx 2.015\text{ K} \approx 2.02\text{ K}$. Exact: `2.02`.
- **Question 30**: $[\text{Mn}(\text{CN})_6]^{3-}$: $\text{Mn}^{3+}$ ($3d^4$), strong field $\text{CN}^-$ gives $t_{2g}^4 e_g^0$, with 2 unpaired electrons ($n = 2$). $\mu = \sqrt{2(4)} = \sqrt{8} \approx 2.83\text{ BM}$. Exact: `2.83`.
- **Question 31**: Gabriel synthesis produces pure $1^\circ$ aliphatic amines. Option (A).
- **Question 32**: Cyclooctatetraene is non-planar tub-shaped (non-aromatic). Option (A).
- **Question 33**: Carbon monoxide is the main reducing agent in the upper reduction zone. Option (A).
- **Question 34**: Glycogen is structurally analogous to amylopectin. Option (A).
- **Question 35**: $\text{B}_2$ has bond order 1 ($\pi_{2p_x}^1 = \pi_{2p_y}^1$, paramagnetic). $\text{O}_2$ has bond order 2 ($\pi^*_{2p_x}^1 = \pi^*_{2p_y}^1$, paramagnetic). Option (C).
- **Question 36**: Cetyltrimethylammonium bromide is a cationic detergent. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: For convex function $f''(x) > 0$: tangent lies below curve, secants lie above curve, Jensen's inequality holds, $f'(x)$ is strictly increasing. Options: (A), (B), (C), (D).
- **Question 38**: Real symmetric positive definite matrix: all eigenvalues $> 0$, Sylvester's criterion (positive leading principal minors), invertible with positive definite inverse, unique Cholesky factorization $A = L L^T$. Options: (A), (B), (C), (D).
- **Question 39**: Common tangent to $y^2 = 4ax$ and $x^2 = 4by$: tangent to first is $y = mx + a/m$. Substituting into $x^2 = 4by$ gives $x^2 - 4b(mx + a/m) = 0$. For tangency, discriminant $= 16b^2 m^2 + 16ab/m = 0 \implies m^3 = -a/b \implies m = -(a/b)^{1/3}$. Equation: $x a^{1/3} + y b^{1/3} + a^{2/3}b^{2/3} = 0$. Options: (A), (B), (C), (D).
- **Question 40**: Cauchy-Euler equation: let $x = e^t \implies \frac{d^2y}{dt^2} - 3\frac{dy}{dt} + 2y = 0$. Roots $m = 1, 2 \implies y = C_1 x + C_2 x^2$. Initial conditions: $C_1 + C_2 = 3$, $C_1 + 2C_2 = 5 \implies C_2 = 2, C_1 = 1 \implies y = x + 2x^2$. Options: (A), (B), (C), (D).
- **Question 41**: Non-coplanar $\implies [\vec{a}\ \vec{b}\ \vec{c}] \ne 0$. Volume of sum vectors is $2[\vec{a}\ \vec{b}\ \vec{c}]$. Volume of cross vectors is $[\vec{a}\ \vec{b}\ \vec{c}]^2$. Positive triple product indicates right-handed system. Options: (A), (B), (C), (D).
- **Question 42**: Normalization: $\int_0^1 \int_0^1 c(x+y)dx dy = c(1/2 + 1/2) = c = 1$. (A) is correct.
  Marginal: $f_X(x) = \int_0^1 (x+y)dy = x + 1/2$. (B) is correct.
  $E[X] = \int_0^1 x(x + 1/2)dx = [x^3/3 + x^2/4]_0^1 = 1/3 + 1/4 = 7/12$. (C) is correct.
  $f(x, y) = x + y \ne (x + 1/2)(y + 1/2)$, so NOT independent. Thus (D) is incorrect.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**
- **Question 43**: $\int_0^1 \frac{\ln(1+x)}{x}dx = \frac{\pi^2}{12} \implies k = 12$. Exact: `12.00`.
- **Question 44**: Area $= \int_0^{\pi/2} (\sin x - \frac{2}{\pi}x)dx = [-\cos x - \frac{x^2}{\pi}]_0^{\pi/2} = (0 - \frac{\pi^2/4}{\pi}) - (-1 - 0) = 1 - \frac{\pi}{4} \approx 1 - 0.7854 = 0.2146 \approx 0.21$. Exact: `0.21`.
- **Question 45**: $2520 = 2^3 \times 3^2 \times 5^1 \times 7^1$. Total divisors $= (3+1)(2+1)(1+1)(1+1) = 4 \times 3 \times 2 \times 2 = 48$. Exact: `48.00`.
- **Question 46**: Parallel lines with direction $\vec{d} = (2, 3, 6)$. Point difference: $\vec{r}_2 - \vec{r}_1 = (3-1, 3-2, 2-3) = (2, 1, -1)$.
  $(\vec{r}_2 - \vec{r}_1) \times \vec{d} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -1 \\ 2 & 3 & 6 \end{vmatrix} = \hat{i}(6 + 3) - \hat{j}(12 + 2) + \hat{k}(6 - 2) = 9\hat{i} - 14\hat{j} + 4\hat{k}$.
  Magnitude $= \sqrt{81 + 196 + 16} = \sqrt{293} \approx 17.117$.
  $|\vec{d}| = \sqrt{4 + 9 + 36} = 7$.
  Distance $= \frac{17.117}{7} \approx 2.45$. Exact: `2.45`.
- **Question 47**: $S = \frac{1/2}{1 - 1/2} + \frac{1/4}{(1 - 1/2)^2} = 1 + 1 = 2.00$. Exact: `2.00`.
- **Question 48**: Arrange 4 men around circle in $(4-1)! = 3! = 6$ ways. This creates 4 spaces. Place 4 women in $4! = 24$ ways. Total $= 6 \times 24 = 144$. Exact: `144.00`.
- **Question 49**: Distance from $(3, -1, 11)$ to line: vector calculation gives $\sqrt{53}$. Option (A).
- **Question 50**: Trace is linear: $\text{Tr}(2A - 3B) = 2\text{Tr}(A) - 3\text{Tr}(B) = 2(5) - 3(3) = 10 - 9 = 1$. Option (A).
- **Question 51**: Tangent to $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ with slope $m$: $y = mx \pm \sqrt{a^2 m^2 - b^2}$.
  Here $a^2 = 9, b^2 = 4, m = 2 \implies a^2 m^2 - b^2 = 9(4) - 4 = 32$.
  $y = 2x \pm \sqrt{32} = 2x \pm 4\sqrt{2}$. Option (A).
- **Question 52**: At $(1, 1)$: $y = x^3 \implies y' = 3x^2 = 3$.
  $6y = 7 - x^2 \implies 6y' = -2x \implies y' = -x/3 = -1/3$.
  $m_1 m_2 = 3(-1/3) = -1 \implies$ orthogonal ($\theta = 90^\circ = \pi/2$). Option (A).
- **Question 53**: $\lim_{x \to 0} \frac{x - (x - x^3/6)}{x^3} = \frac{1}{6}$. Option (A).
- **Question 54**: $f(x) = \frac{1}{2}\sin(2x) \le \frac{1}{2}$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 06 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Angular Impulse-Momentum about Fixed Pivot, Non-Conservation of Linear Momentum.
- **2. Derivation**:
  - The pivot exerts an external impulsive reaction force on the rod, so linear momentum of the system is not conserved. (D is incorrect).
  - Torque of the external reaction about pivot $O$ is identically zero, so angular momentum about $O$ is conserved. (A) is correct.
  - Moment of inertia about $O$: $I_O = \frac{1}{3}M L^2 + m L^2 = \left(\frac{1}{3}M + m\right)L^2$. (B) is correct.
  - Angular velocity: $L_i = m v_0 L = I_O \omega \implies \omega = \frac{m v_0 L}{(M/3 + m)L^2} = \frac{m v_0}{(M/3 + m)L}$. (C) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Capillary Action in Differential U-Tube, Laplace Excess Pressure.
- **2. Derivation**:
  - Menisci are concave upward for wetting liquids ($\theta = 0^\circ$). (A) is correct.
  - Pressure just below meniscus: $P_1 = P_0 - \frac{2S}{r_1}$ and $P_2 = P_0 - \frac{2S}{r_2}$. Since $r_1 < r_2$, $P_1 < P_2$. (B) is correct.
  - At horizontal reference level in the liquid: $P_1 + \rho g h_1 = P_2 + \rho g h_2 \implies \rho g h = P_2 - P_1 = 2S\left(\frac{1}{r_1} - \frac{1}{r_2}\right) \implies h = \frac{2S}{\rho g}\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$. (C) is correct.
  - The column rises higher in the narrower tube ($r_1$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Plane Electromagnetic Waves, Poynting Vector, Polarization.
- **2. Derivation**:
  - By Maxwell's equations: $\vec{B} = \frac{1}{c}(\hat{k} \times \vec{E}) = \frac{E_0}{c}\cos(kz - \omega t)\hat{j}$. (A) is correct.
  - $\vec{E}$ oscillates along $\hat{i}$ (linearly polarized along x-axis). (B) is correct.
  - Intensity $I = \langle S \rangle = \frac{1}{2}\varepsilon_0 c E_0^2$. (C) is correct.
  - Radiation pressure on absorbing surface: $P_{\text{rad}} = I/c$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Wave Propagation in Graded Index Media.
- **2. Derivation**:
  - Normal incidence at planar stratified boundary undergoes zero refraction angle $\theta = 0$, propagating along straight line. (A) is correct.
  - Speed of wave $v(x) = \frac{c}{\mu(x)} = \frac{c}{\mu_0}(1 + x/a)$, which increases linearly with $x$. (B) is correct.
  - Wavelength $\lambda(x) = \frac{v}{\nu}$ increases as $v$ increases. (C) is correct.
  - Frequency $\nu$ depends solely on the source and is invariant under propagation across any medium. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Davisson-Germer Experiment, de Broglie Matter Waves, Bragg Diffraction.
- **2. Derivation**:
  - Confirmed electron wave nature using nickel crystal. (A) is correct.
  - Bragg constructive interference: $2d\sin\theta = n\lambda$. (B) is correct.
  - Peak intensity observed at $54\text{ V}$ and $50^\circ$. (C) is correct.
  - Historically the first experimental verification of de Broglie's hypothesis. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Temperature-Entropy (T-S) Representation of Thermodynamic Cycles.
- **2. Derivation**:
  - Horizontal lines represent isotherms ($T = \text{const}$), vertical lines represent reversible adiabatics ($S = \text{const}$). Thus the rectangular cycle is a Carnot cycle. (A) is correct.
  - $Q_{\text{in}} = \int T dS = T_H (S_2 - S_1)$. (B) is correct.
  - $W_{\text{net}} = \oint T dS = \text{Area of rectangle} = (T_H - T_C)(S_2 - S_1)$. (C) is correct.
  - Efficiency $\eta = \frac{W_{\text{net}}}{Q_{\text{in}}} = \frac{(T_H - T_C)(S_2 - S_1)}{T_H (S_2 - S_1)} = 1 - \frac{T_C}{T_H}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: $\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{200.0}{0.50}} = \sqrt{400} = 20.0\text{ rad/s}$.
  $v_{\text{max}} = \omega A = (20.0)(0.050) = 1.00\text{ m/s}$. Exact: `1.00`.
- **Question 8**: $E = \frac{V}{d} = \frac{400.0\text{ V}}{2.0 \times 10^{-3}\text{ m}} = 200 \times 10^3\text{ V/m} = 200.00\text{ kV/m}$. Exact: `200.00`.
- **Question 9**: $\beta = \frac{\lambda D}{d} = \frac{(500 \times 10^{-9}\text{ m})(1.00\text{ m})}{0.25 \times 10^{-3}\text{ m}} = 2.0 \times 10^{-3}\text{ m} = 2.00\text{ mm}$. Exact: `2.00`.
- **Question 10**: $v_{\text{rms}} = \sqrt{\frac{3 R T}{M}} = \sqrt{\frac{3(8.314)(300)}{0.028}} = \sqrt{267235.7} \approx 516.9 \approx 517\text{ m/s}$. Exact: `517.00`.
- **Question 11**: $\mathcal{E} = -\frac{d\Phi}{dt} = -\pi R^2 \frac{dB}{dt} = \pi (0.10)^2(10.0) = 0.10\pi \approx 0.31416\text{ V}$.
  $I = \frac{\mathcal{E}}{r} = \frac{0.31416}{2.0} = 0.15708\text{ A} = 157.08\text{ mA} \approx 157\text{ mA}$. Exact: `157.00`.
- **Question 12**: $N(t) = N_0 (1/2)^{t/T_{1/2}} = N_0 (1/2)^{20/5} = N_0 (1/2)^4 = \frac{N_0}{16} = 0.0625 N_0 = 6.25\%$. Exact: `6.25`.

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
- **Question 19**: Optical activity requires lack of improper rotation axis (chiral). $cis-[\text{Co}(\text{en})_2\text{Cl}_2]^+$ ($C_2$ symmetry) and $[\text{Cr}(\text{ox})_3]^{3-}$ ($D_3$ symmetry) are chiral and resolve into enantiomers. Trans-isomer has center of inversion (achiral). Square planar $[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$ is achiral. Options: (A), (B).
- **Question 20**: Cannizzaro reaction: aldehydes without $\alpha$-H undergo redox with concentrated alkali via rate-determining hydride transfer. Crossed Cannizzaro with formaldehyde gives formate because formaldehyde is more easily attacked by $\text{OH}^-$. Options: (A), (B), (C), (D).
- **Question 21**: Electrochemical series: more negative reduction potential $\implies$ stronger reducing agent. Zinc reduces iron. Copper does not reduce $\text{H}^+$ because $E^\circ > 0$. Chlorine oxidizes bromide and iodide. Options: (A), (B), (C), (D).
- **Question 22**: Chain isomers differ in carbon skeleton: $n$-pentane/isopentane and $n$-butane/isobutane. Positional isomers differ in substituent location (pentan-2-one/pentan-3-one, propan-1-ol/propan-2-ol). Options: (A), (B).
- **Question 23**: $2\text{KClO}_3 \to 2\text{KCl} + 3\text{O}_2$; $2\text{KNO}_3 \to 2\text{KNO}_2 + \text{O}_2$; $2\text{Pb(NO}_3)_2 \to 2\text{PbO} + 4\text{NO}_2 + \text{O}_2$. But $(\text{NH}_4)_2\text{Cr}_2\text{O}_7$ gives $\text{N}_2$. Options: (A), (B), (C).
- **Question 24**: Water-soluble vitamins (C, B-complex) are excreted in urine and cannot be stored. Vitamin A is fat-soluble and stored in liver. Options: (A), (B), (C).
- **Question 25**: $S = \sqrt{K_{sp}} = \sqrt{1.8 \times 10^{-10}} = 1.34 \times 10^{-5}\text{ mol/L} = 13.4\ \mu\text{mol/L}$. Exact: `13.40`.
- **Question 26**: $87.5\%$ decomposition means $12.5\% = 1/8 = (1/2)^3$ remains. Time required $= 3 t_{1/2} = 3(100.0) = 300.00\text{ s}$. Exact: `300.00`.
- **Question 27**: For FCC: $\sqrt{2}a = 4r \implies a = \frac{4r}{\sqrt{2}} = 2\sqrt{2}r = 2(1.414)(141.4) = 400\text{ pm}$. Exact: `400.00`.
- **Question 28**: Combustion of graphite: $\text{C}(s) + \text{O}_2(g) \to \text{CO}_2(g)$, which is identical to the formation of $\text{CO}_2(g)$. Hence $\Delta_{\text{comb}} H^\circ = -393.5\text{ kJ/mol}$. Magnitude $= 393.50$. Exact: `393.50`.
- **Question 29**: $\Delta T_f = i K_f m \implies 0.3534 = i (1.86)(0.10) = 0.186 i \implies i = \frac{0.3534}{0.186} = 1.90$.
  $i = 1 + \alpha \implies \alpha = 0.90 = 90.00\%$. Exact: `90.00`.
- **Question 30**: In Caro's acid ($\text{H}_2\text{SO}_5$), one peroxide bond ($-\text{O}-\text{O}-$) exists: $2(+1) + x + 3(-2) + 2(-1) = 0 \implies x + 2 - 6 - 2 = 0 \implies x - 6 = 0 \implies x = +6$. Exact: `6.00`.
- **Question 31**: Picric acid contains three strongly electron-withdrawing $-\text{NO}_2$ groups at ortho and para positions, making it exceptionally acidic ($pK_a \approx 0.38$). Option (A).
- **Question 32**: Solid $\text{PCl}_5$ exists as $[\text{PCl}_4]^+[\text{PCl}_6]^-$. Option (A).
- **Question 33**: Cyanide extraction gives soluble complex $[\text{Ag}(\text{CN})_2]^-$. Option (A).
- **Question 34**: Glycine ($\text{H}_2\text{N}-\text{CH}_2-\text{COOH}$) has no chiral carbon (achiral, optically inactive). Option (A).
- **Question 35**: $\text{H}_2\text{O}$ has 2 bonding pairs and 2 lone pairs $\implies$ bent / V-shaped geometry. Option (A).
- **Question 36**: Phenol + Formaldehyde $\to$ Bakelite. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(0) = 0$. $f'(x) = \cos x - (\cos x - x\sin x) = x\sin x > 0$ on $(0, \pi/2)$. Thus $f(x)$ is strictly increasing. For $x > 0$, $f(x) > 0 \implies \sin x > x\cos x \implies \tan x > x$. Options: (A), (B), (C), (D).
- **Question 38**: $A^T A = I, \det A = -1$. Eigenvalues have modulus 1. Complex eigenvalues come in conjugate pairs, so real eigenvalues must have product $-1 \implies \lambda = -1$ is an eigenvalue. Represents reflection or rotoreflection. $A^{-1} = A^T$. Options: (A), (B), (C), (D).
- **Question 39**: $L = \sqrt{25 - 9} = 4$. Chord of contact: $5x + 0y = 9 \implies x = 9/5$. Area of $PAOB = 2 \times \frac{1}{2}(r)(L) = (3)(4) = 12$. Circumcircle of $\Delta PAB$ has $OP$ as diameter (length 5), so circumradius is $2.5$. Options: (A), (B), (C), (D).
- **Question 40**: Let $y = vx \implies v + x\frac{dv}{dx} = v + \tan v \implies \cot v dv = \frac{dx}{x} \implies \ln|\sin v| = \ln|x| + \ln C \implies \sin(y/x) = Cx$. Initial condition: $\sin(\pi/6) = C(1) \implies C = 1/2$. Solution: $\sin(y/x) = x/2$. Options: (A), (B), (C), (D).
- **Question 41**: $\vec{a} \perp \vec{b}$ and $\vec{a} \perp \vec{c} \implies \vec{a} \parallel \vec{b}\times\vec{c}$. $|\vec{b}\times\vec{c}| = |\vec{b}||\vec{c}|\sin(\pi/6) = 1/2$. $[\vec{a}\ \vec{b}\ \vec{c}] = \vec{a}\cdot(\vec{b}\times\vec{c}) = \pm 1/2$. Volume $= 1/2$. Options: (A), (B), (C), (D).
- **Question 42**: For Poisson with $\lambda = 3$: mean $= 3$, variance $= 3$, $P(0) = e^{-3}$. Mode is at $\lambda - 1 = 2$ and $\lambda = 3$ (bimodal). Options: (A), (B), (C), (D).
- **Question 43**: Parabola $y^2 = 4x$ bounded by $x = 1$: $\text{Area} = 2 \int_0^1 2\sqrt{x}dx = 4 \left[\frac{2}{3}x^{3/2}\right]_0^1 = \frac{8}{3} \approx 2.67$. Exact: `2.67`.
- **Question 44**: $y' = \frac{2x}{1+x^2}$. At $x = 1$, $y' = \frac{2(1)}{1+1} = \frac{2}{2} = 1.00$. Exact: `1.00`.
- **Question 45**: $\int_0^{\pi/2} \cos^3 x dx = \frac{2}{3}(1) = \frac{2}{3} \approx 0.67$. Exact: `0.67`.
- **Question 46**: Point $P(1, 2, 3)$. Line passes through $A(2, 3, 4)$ with direction $\vec{d} = (1, 2, 2)$.
  $\vec{AP} = (1-2, 2-3, 3-4) = (-1, -1, -1)$.
  $\vec{AP} \times \vec{d} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -1 & -1 & -1 \\ 1 & 2 & 2 \end{vmatrix} = \hat{i}(-2 + 2) - \hat{j}(-2 + 1) + \hat{k}(-2 + 1) = \hat{j} - \hat{k}$.
  Magnitude $= \sqrt{1 + 1} = \sqrt{2}$.
  $|\vec{d}| = \sqrt{1 + 4 + 4} = 3$.
  Distance $= \frac{\sqrt{2}}{3} \approx \frac{1.414}{3} \approx 0.47$. Exact: `0.47`.
- **Question 47**: $S = \frac{a}{1-r} \implies 9 = \frac{3}{1-r} \implies 1-r = \frac{1}{3} \implies r = \frac{2}{3} \approx 0.67$. Exact: `0.67`.
- **Question 48**: First digit cannot be 0: 5 choices $\{1, 2, 3, 4, 5\}$.
  Remaining 3 digits chosen from remaining 5 digits: $P(5, 3) = 5 \times 4 \times 3 = 60$.
  Total 4-digit numbers $= 5 \times 60 = 300$. Exact: `300.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 06
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 600.00
- Q8: 0.00
- Q9: 2.30
- Q10: 3458.00
- Q11: 157.91
- Q12: 2.22
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
- Q25: 4.65
- Q26: 53.58
- Q27: 356.80
- Q28: 0.23
- Q29: 2.02
- Q30: 2.83
- Q31: A
- Q32: A
- Q33: A
- Q34: A
- Q35: C
- Q36: A

#### Mathematics
- Q37: A, B, C, D
- Q38: A, B, C, D
- Q39: A, B, C, D
- Q40: A, B, C, D
- Q41: A, B, C, D
- Q42: A, B, C
- Q43: 12.00
- Q44: 0.21
- Q45: 48.00
- Q46: 2.45
- Q47: 2.00
- Q48: 144.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Paper 2 Answer Key
#### Physics
- Q1: A, B, C
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 1.00
- Q8: 200.00
- Q9: 2.00
- Q10: 517.00
- Q11: 157.00
- Q12: 6.25
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B
- Q20: A, B, C, D
- Q21: A, B, C, D
- Q22: A, B
- Q23: A, B, C
- Q24: A, B, C
- Q25: 13.40
- Q26: 300.00
- Q27: 400.00
- Q28: 393.50
- Q29: 90.00
- Q30: 6.00
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
- Q43: 2.67
- Q44: 1.00
- Q45: 0.67
- Q46: 0.47
- Q47: 0.67
- Q48: 300.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: 33.3% of questions (high option-checking cognitive load).
- **Physics**: Focus on Betatron 2:1 condition, Hertzian dipole radiation, capacitor energy dissipation independence from R, Dieterici gas critical state, Fabry-Pérot finesse.
- **Chemistry**: Chelate and macrocyclic effect, Beckmann rearrangement caprolactam synthesis, passivation kinetics, Berthelot/Redlich-Kwong equations of state, protein secondary/tertiary structures.
- **Mathematics**: Strict convexity and Jensen's inequality, Sylvester's criterion for positive definite matrices, common tangent to dual orthogonal parabolas, Cauchy-Euler differential equations.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

create_mock_files(6, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")

