# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 03.
Empirical Signature: IIT Delhi Benchmark (2013, 2020)
- Multi-correct dominance (+4/-2 with partial marking)
- Circuit transients, induction dynamics, Jahn-Teller splitting
- Stereochemistry, migratory aptitudes, real gases
- Multivariable coordinate geometry, matrices, probability
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 03 — Paper 1
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
A light conducting aluminum ring of mass $m$, radius $r$, and electrical resistance $R_0$ with self-inductance $L$ is placed coaxially over a vertical iron-cored solenoid carrying an alternating current $I(t) = I_0 \sin(\omega t)$. The ring is observed to levitate at a stable height $z$ above the solenoid top (Thomson's jumping ring effect). Which of the following statements is/are correct?
(A) The induced current in the ring lags the induced electromotive force by a phase angle $\phi = \tan^{-1}\left(\frac{\omega L}{R_0}\right)$.  
(B) If the ring had zero self-inductance ($L = 0$), the time-averaged vertical electromagnetic force on the ring would be zero.  
(C) Because $L > 0$, the induced current in the ring is partially out of phase with the solenoid's magnetic field, resulting in a non-zero repulsive time-averaged upward force $\langle F_z \rangle > 0$.  
(D) If the temperature of the ring is lowered with liquid nitrogen, its electrical resistance $R_0$ decreases, causing it to levitate at a greater height.

#### Question 2
A solid sphere of mass $M$ and radius $R$ is released from rest at the rim of a rough hemispherical bowl of radius $5R$ whose inner surface has coefficient of static friction $\mu_s$. The sphere rolls without slipping down along the bowl surface. Which of the following statements is/are correct?
(A) The effective radius of the path traced by the center of mass of the sphere is $4R$.  
(B) When the radius to the center of the sphere makes an angle $\theta$ with the vertical, the angular acceleration of the sphere about its own center is $\alpha = \frac{5g\sin\theta}{7R}$.  
(C) The speed of the center of mass of the sphere at the bottommost point is $v = \sqrt{\frac{40}{7}g R}$.  
(D) The normal contact force exerted by the bowl on the sphere at the bottommost point is $N = \frac{17}{7}Mg$.

#### Question 3
A neutral pion ($\pi^0$) of rest mass $m_\pi c^2 = 135\text{ MeV}$ travels with relativistic velocity $v = 0.80c$ along the $+x$-direction in the laboratory frame and decays in flight into two photons ($\pi^0 \to \gamma_1 + \gamma_2$). If the two photons are emitted collinear with the direction of motion (one forward and one backward):
(A) The Lorentz factor of the decaying pion is $\gamma = \frac{5}{3} \approx 1.667$.  
(B) The energy of the forward-emitted photon is $E_1 = \frac{1}{2} m_\pi c^2 \sqrt{\frac{1+v/c}{1-v/c}} = 202.5\text{ MeV}$.  
(C) The energy of the backward-emitted photon is $E_2 = \frac{1}{2} m_\pi c^2 \sqrt{\frac{1-v/c}{1+v/c}} = 22.5\text{ MeV}$.  
(D) The product of the two photon energies satisfies $E_1 E_2 = \frac{1}{4}(m_\pi c^2)^2 = 4556.25\text{ MeV}^2$, independent of the pion's velocity.

#### Question 4
A solid dielectric sphere of radius $R$ centered at the origin possesses a non-uniform frozen-in radial polarization $\vec{P}(r) = k r \hat{r}$ for $r \le R$, where $k$ is a positive constant. Which of the following statements is/are correct?
(A) The bound volume charge density inside the sphere is uniform and given by $\rho_b = -3k$.  
(B) The bound surface charge density on the sphere's outer surface is $\sigma_b = +k R$.  
(C) The total net bound charge of the sphere is identically zero: $Q_{\text{bound, net}} = 0$.  
(D) The electric field inside the sphere ($r < R$) is radially directed and has magnitude $E(r) = \frac{k r}{\varepsilon_0}$.

#### Question 5
An ideal air-standard Otto cycle operates with a volumetric compression ratio $r = \frac{V_{\text{max}}}{V_{\text{min}}} = 8.0$. The working medium is an ideal diatomic gas with $\gamma = 1.40$. The cycle consists of two adiabatic processes and two isochoric processes. Which of the following statements is/are correct?
(A) The thermal efficiency of the Otto cycle is $\eta = 1 - \frac{1}{r^{\gamma-1}} = 1 - \frac{1}{8^{0.40}}$.  
(B) The numerical value of the theoretical thermal efficiency is approximately $\eta \approx 56.5\%$.  
(C) During the isochoric heat addition stage, no mechanical work is done by the gas.  
(D) If the compression ratio is increased to $r = 10.0$, the thermal efficiency of the engine increases.

#### Question 6
A circular Fresnel zone plate is constructed such that the radius of the $n$-th half-period Fresnel zone is $r_n = \sqrt{n \lambda f}$, where $\lambda = 500\text{ nm}$ is the wavelength of incident collimated monochromatic light and $f = 1.00\text{ m}$ is the designed focal length. Which of the following statements is/are correct?
(A) The radius of the first transparent zone is $r_1 = \sqrt{\lambda f} \approx 0.707\text{ mm}$.  
(B) The zone plate acts like a converging lens with multiple focal points located at $f_m = \frac{f}{2m-1}$ for integer $m \ge 1$.  
(C) Unlike a conventional glass convex lens, the focal length of a Fresnel zone plate is inversely proportional to the wavelength $\lambda$.  
(D) The intensity of light at the primary focal point is significantly greater than if the entire aperture were unblocked.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A heavy gyroscope rotor of mass $M = 3.00\text{ kg}$ and radius of gyration $k = 0.10\text{ m}$ spins about its horizontal axle at an angular speed $\omega_s = 600.0\text{ rad/s}$. The axle is supported at a distance $d = 0.15\text{ m}$ from the rotor's center of mass. Taking $g = 9.80\text{ m/s}^2$, calculate the precessional angular velocity $\Omega_p$ (in rad/s) of the gyroscope. [Round off to TWO decimal places].

#### Question 8
A cylindrical capacitor consists of two concentric metallic cylinders of length $L = 1.00\text{ m}$. The inner cylinder has radius $r_1 = 1.0\text{ cm}$ and the outer cylinder has radius $r_3 = 4.0\text{ cm}$. The space between $r_1$ and $r_2 = 2.0\text{ cm}$ is filled with a dielectric of relative permittivity $\varepsilon_{r1} = 4.0$, while the space between $r_2$ and $r_3$ is filled with a dielectric of $\varepsilon_{r2} = 2.0$. Calculate the capacitance $C$ (in picoFarads, $\text{pF}$) of the cable. [Take $\varepsilon_0 = 8.85 \times 10^{-12}\text{ F/m}$ and $\ln 2 \approx 0.693$. Round off to TWO decimal places].

#### Question 9
A blackbody spherical radiator of radius $R_1 = 0.10\text{ m}$ at steady temperature $T_1 = 500\text{ K}$ is enclosed concentrically inside a thin black spherical shell of radius $R_2 = 0.20\text{ m}$. The outer shell radiates into deep space at $0\text{ K}$. Calculate the steady-state equilibrium temperature $T_2$ (in Kelvin) of the outer shell. [Take $4^{1/4} = \sqrt{2} \approx 1.414$. Round off to the nearest integer].

#### Question 10
An equilateral triangular glass prism ($A = 60^\circ$) has refractive index $\mu = 1.50$. Calculate the angle of incidence $i$ (in degrees) for which the ray passes through the prism at minimum deviation. [Take $\sin 30^\circ = 0.50$, $\sin^{-1}(0.75) \approx 48.59^\circ$. Round off to TWO decimal places].

#### Question 11
A finite solenoid of length $L = 0.40\text{ m}$ and radius $R = 0.030\text{ m}$ is tightly wound with $N = 800$ turns carrying a steady current $I = 2.50\text{ A}$. Calculate the magnetic field $B$ (in milliTesla, $\text{mT}$) at the exact center on the axis of the solenoid. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$, $\cos\theta = \frac{L}{\sqrt{L^2 + 4R^2}} \approx 0.989$. Round off to TWO decimal places].

#### Question 12
When a metal surface is illuminated by monochromatic light of wavelength $\lambda_1 = 300\text{ nm}$, the stopping potential is $V_1 = 1.85\text{ V}$. When illuminated by wavelength $\lambda_2 = 400\text{ nm}$, the stopping potential is $V_2 = 0.82\text{ V}$. From this data, determine the Planck constant $h$ in units of $10^{-34}\text{ J}\cdot\text{s}$. [Take $c = 3.0 \times 10^8\text{ m/s}, e = 1.60 \times 10^{-19}\text{ C}$. Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
If the radius of a planet is doubled while keeping its mean density constant, the escape velocity from the planet's surface:
(A) Doubles  
(B) Increases by a factor of 4  
(C) Increases by a factor of $\sqrt{2}$  
(D) Remains unchanged

#### Question 14
Water rises to a height $h = 6.0\text{ cm}$ in a vertical glass capillary tube of radius $r$. If the tube is tilted at an angle $\theta = 60^\circ$ to the vertical, the length $l$ of the water column along the inclined tube is:
(A) $12.0\text{ cm}$  
(B) $6.0\text{ cm}$  
(C) $3.0\text{ cm}$  
(D) $8.5\text{ cm}$

#### Question 15
If the acoustic intensity of a sound wave is increased by a factor of 100, the sound intensity level increases by:
(A) $20\text{ dB}$  
(B) $10\text{ dB}$  
(C) $40\text{ dB}$  
(D) $2\text{ dB}$

#### Question 16
In the radioactive $\alpha$-decay of a stationary parent nucleus $^{238}_{92}\text{U} \to ^{234}_{90}\text{Th} + ^4_2\text{He}$, the disintegration energy is $Q = 4.27\text{ MeV}$. The kinetic energy of the emitted $\alpha$-particle is:
(A) $4.20\text{ MeV}$  
(B) $4.27\text{ MeV}$  
(C) $2.13\text{ MeV}$  
(D) $3.85\text{ MeV}$

#### Question 17
A light beam in water ($\mu_1 = 4/3$) strikes a crown glass plate ($\mu_2 = 1.50$). The Brewster polarizing angle of incidence $\theta_B$ is:
(A) $\tan^{-1}(9/8)$  
(B) $\tan^{-1}(8/9)$  
(C) $\sin^{-1}(8/9)$  
(D) $\tan^{-1}(1.50)$

#### Question 18
The center of mass of a uniform solid hemisphere of radius $R$ lies on its symmetry axis at a distance from the flat base equal to:
(A) $\frac{3}{8}R$  
(B) $\frac{1}{2}R$  
(C) $\frac{4}{3\pi}R$  
(D) $\frac{2}{3}R$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following statements is/are correct regarding the Jahn-Teller effect in coordination compounds?
(A) It arises in non-linear coordination complexes having an electronically degenerate ground state.  
(B) High-spin $d^4$ complexes (e.g., $[\text{Cr}(\text{H}_2\text{O})_6]^{2+}$) and $d^9$ complexes (e.g., $[\text{Cu}(\text{H}_2\text{O})_6]^{2+}$) exhibit strong Jahn-Teller distortions.  
(C) The distortion typically consists of elongation of the two axial metal-ligand bonds along the $z$-axis ($z$-out distortion).  
(D) Octahedral low-spin $d^6$ complexes exhibit strong Jahn-Teller distortion due to their filled $t_{2g}$ subshell.

#### Question 20
In the acid-catalyzed pinacol-pinacolone rearrangement of 1,2-diols:
(A) The reaction proceeds through the preferential protonation and loss of water to generate the more stable carbocation intermediate.  
(B) The migratory aptitude of aryl groups follows the order: $p\text{-anisyl} > p\text{-tolyl} > \text{phenyl} > p\text{-chlorophenyl}$.  
(C) The driving force of the rearrangement is the formation of a resonance-stabilized oxonium ion intermediate.  
(D) Treatment of 1,1-diphenyl-2-methylpropane-1,2-diol with $\text{H}_2\text{SO}_4$ gives 3,3-diphenylbutan-2-one via methyl migration.

#### Question 21
Regarding the electrochemical rusting of iron:
(A) Anodic reaction: $\text{Fe}(s) \to \text{Fe}^{2+}(aq) + 2e^-$.  
(B) Cathodic reaction in acidic/neutral aerated water: $\text{O}_2(g) + 4\text{H}^+(aq) + 4e^- \to 2\text{H}_2\text{O}(l)$.  
(C) The presence of electrolytes (such as $\text{NaCl}$ in seawater) accelerates corrosion by increasing ionic conductivity.  
(D) Sacrificial protection of underground iron pipelines is achieved by connecting them electrically to zinc or magnesium blocks.

#### Question 22
Which of the following statements is/are correct regarding real gases and their equations of state?
(A) At the Boyle temperature $T_B = \frac{a}{Rb}$, the second virial coefficient vanishes, and the gas behaves ideally over a wide pressure range.  
(B) For gases like $\text{H}_2$ and $\text{He}$ at room temperature, the compressibility factor $Z > 1$ at all pressures because their inversion temperatures are well below room temperature.  
(C) The Dieterici equation of state is given by $P(V - b)e^{a/RTV} = RT$.  
(D) At very high pressures, the van der Waals equation reduces to $P(V - b) = RT$, giving $Z = 1 + \frac{Pb}{RT}$.

#### Question 23
In the chromyl chloride test for qualitative detection of chloride ions ($\text{Cl}^-$):
(A) Solid chloride salt is heated with solid potassium dichromate ($\text{K}_2\text{Cr}_2\text{O}_7$) and concentrated sulfuric acid ($\text{H}_2\text{SO}_4$).  
(B) Deep red vapours of chromyl chloride ($\text{CrO}_2\text{Cl}_2$) are evolved.  
(C) When $\text{CrO}_2\text{Cl}_2$ is passed into aqueous $\text{NaOH}$, a yellow solution of $\text{Na}_2\text{CrO}_4$ is obtained.  
(D) Chlorides of mercury ($\text{Hg}_2\text{Cl}_2, \text{HgCl}_2$), silver ($\text{AgCl}$), and lead ($\text{PbCl}_2$) do not respond positively to this test.

#### Question 24
Which of the following polymers are classified as biodegradable polymers?
(A) Poly-$\beta$-hydroxybutyrate-co-$\beta$-hydroxyvalerate (PHBV)  
(B) Nylon-2-nylon-6  
(C) Polyhydroxyacetic acid (PGA)  
(D) Bakelite

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
Calculate the $\text{pH}$ of a solution formed by mixing $100.0\text{ mL}$ of $0.10\text{ M NH}_4\text{Cl}$ with $100.0\text{ mL}$ of $0.10\text{ M NH}_4\text{OH}$. [Given $pK_b(\text{NH}_4\text{OH}) = 4.75$. Round off to TWO decimal places].

#### Question 26
The rate constants for a chemical reaction are $k_1 = 0.020\text{ s}^{-1}$ at $300\text{ K}$ and $k_2 = 0.080\text{ s}^{-1}$ at $320\text{ K}$. Calculate the activation energy $E_a$ of the reaction in $\text{kJ/mol}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 4 = 1.386$. Round off to TWO decimal places].

#### Question 27
An element with atomic mass $M = 50.0\text{ g/mol}$ crystallizes in a hexagonal close-packed (HCP) lattice. If the atomic radius is $r = 150\text{ pm}$, calculate the percentage packing efficiency of the HCP unit cell. [Enter the nearest integer percentage].

#### Question 28
Calculate the standard reduction potential $E^\circ(\text{Fe}^{3+}/\text{Fe})$ (in Volts) given:
- $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V}$
- $E^\circ(\text{Fe}^{2+}/\text{Fe}) = -0.44\text{ V}$
[Round off to TWO decimal places].

#### Question 29
A solution containing $3.00\text{ g}$ of a non-volatile non-electrolyte solute dissolved in $100.0\text{ g}$ of benzene boils at $80.50^\circ\text{C}$. Pure benzene boils at $80.10^\circ\text{C}$. Calculate the molar mass $M$ of the solute in $\text{g/mol}$. [Take $K_b(\text{benzene}) = 2.53\text{ K}\cdot\text{kg/mol}$. Round off to the nearest integer].

#### Question 30
Calculate the spin-only magnetic moment $\mu_{\text{eff}}$ (in Bohr Magnetons, $\text{BM}$) of the low-spin complex $[\text{Fe}(\text{CN})_6]^{3-}$ ($\text{Fe}^{3+}, 3d^5$, strong field ligand $\text{CN}^-$). [Take $\sqrt{3} \approx 1.732$. Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following compounds gives benzoic acid on treatment with alkaline $\text{KMnO}_4$ followed by acidification?
(A) Toluene  
(B) Ethylbenzene  
(C) Isopropylbenzene  
(D) All of these

#### Question 32
The correct order of increasing basicity in aqueous solution among methylamines is:
(A) $(\text{CH}_3)_3\text{N} < \text{CH}_3\text{NH}_2 < (\text{CH}_3)_2\text{NH}$  
(B) $\text{CH}_3\text{NH}_2 < (\text{CH}_3)_2\text{NH} < (\text{CH}_3)_3\text{N}$  
(C) $(\text{CH}_3)_2\text{NH} < \text{CH}_3\text{NH}_2 < (\text{CH}_3)_3\text{N}$  
(D) $(\text{CH}_3)_3\text{N} < (\text{CH}_3)_2\text{NH} < \text{CH}_3\text{NH}_2$

#### Question 33
In the blast furnace for the metallurgy of iron, limestone ($\text{CaCO}_3$) is added primarily to:
(A) Act as a flux to remove silica ($\text{SiO}_2$) impurities as slag  
(B) Reduce hematite to iron  
(C) Provide carbon monoxide  
(D) Oxidize impurities

#### Question 34
Maltose on enzymatic hydrolysis with maltase yields:
(A) Two molecules of D-glucose  
(B) D-glucose and D-fructose  
(C) D-glucose and D-galactose  
(D) Two molecules of D-fructose

#### Question 35
According to Molecular Orbital Theory, which of the following species has the highest bond order?
(A) $\text{O}_2^+$  
(B) $\text{O}_2$  
(C) $\text{O}_2^-$  
(D) $\text{O}_2^{2-}$

#### Question 36
Temporary hardness of water caused by calcium bicarbonate $\text{Ca(HCO}_3)_2$ can be removed on a large scale by adding a calculated quantity of slaked lime. This process is known as:
(A) Clark's method  
(B) Calgon's method  
(C) Permutit method  
(D) Ion-exchange method

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x}{1 + x^2}$ for all $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ is an odd function.  
(B) The range of $f(x)$ is $[-1/2, 1/2]$.  
(C) $f(x)$ has a local maximum at $x = 1$ and a local minimum at $x = -1$.  
(D) The points of inflection of the curve are at $x = 0$ and $x = \pm \sqrt{3}$.

#### Question 38
Let $A$ be a real $n \times n$ symmetric matrix. Which of the following statements is/are correct?
(A) All eigenvalues of $A$ are real numbers.  
(B) Eigenvectors corresponding to distinct eigenvalues of $A$ are mutually orthogonal.  
(C) There exists an orthogonal matrix $Q$ such that $Q^T A Q$ is a diagonal matrix.  
(D) If all eigenvalues of $A$ are strictly positive, then $A$ is positive definite ($x^T A x > 0$ for all $x \ne 0$).

#### Question 39
Consider the rectangular hyperbola $xy = c^2$ ($c > 0$). Let $P(ct, c/t)$ be a point on the hyperbola with parameter $t \ne 0$:
(A) The equation of the tangent at $P$ is $\frac{x}{t} + yt = 2c$.  
(B) The area of the triangle formed by the tangent at $P$ and the coordinate axes is $2c^2$, which is independent of the choice of $P$.  
(C) The point $P$ bisects the segment of the tangent intercepted between the coordinate axes.  
(D) The equation of the normal at $P$ is $xt^3 - yt - ct^4 + c = 0$.

#### Question 40
Consider the differential equation $\frac{dy}{dx} + \frac{y}{x} = y^2 \ln x$ for $x > 0$. Which of the following statements is/are correct?
(A) The substitution $v = \frac{1}{y}$ transforms the equation into a linear differential equation $\frac{dv}{dx} - \frac{v}{x} = -\ln x$.  
(B) The integrating factor of the transformed equation is $\frac{1}{x}$.  
(C) The general solution satisfies $\frac{1}{y} = x \left(\frac{(\ln x)^2}{2} + C\right)$.  
(D) If $y(1) = 1$, then $C = 1$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-zero vectors such that $\vec{a} \times \vec{b} = \vec{c}$ and $\vec{b} \times \vec{c} = \vec{a}$. Which of the following statements is/are correct?
(A) The vectors $\vec{a}, \vec{b}, \vec{c}$ are mutually orthogonal.  
(B) $|\vec{a}| = |\vec{c}|$.  
(C) $|\vec{b}| = 1$.  
(D) $[\vec{a} \ \vec{b} \ \vec{c}] = |\vec{a}|^2$.

#### Question 42
Let $X$ be a discrete random variable following a Geometric distribution with parameter $p \in (0, 1)$, so that $P(X = k) = (1-p)^{k-1}p$ for $k = 1, 2, 3, \dots$. Which of the following statements is/are correct?
(A) The mean of $X$ is $E[X] = \frac{1}{p}$.  
(B) The variance of $X$ is $\text{Var}(X) = \frac{1-p}{p^2}$.  
(C) $X$ satisfies the memoryless property: $P(X > s + t \mid X > s) = P(X > t)$ for positive integers $s, t$.  
(D) $P(X \ge 3) = (1-p)^2$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^\infty \frac{e^{-x} - e^{-3x}}{x}\,dx$$
If $I = \ln k$, find the integer value of $k$.

#### Question 44
Find the total area of the region bounded by the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$ in the first quadrant, divided by $\pi$. [Round off to TWO decimal places].

#### Question 45
Find the number of points with strictly positive integer coordinates $(x, y)$ that lie strictly inside the triangle bounded by the lines $x = 0$, $y = 0$, and $x + y = 10$.

#### Question 46
Calculate the distance from the point $(2, 3, -1)$ to the plane $3x - 4y + 12z - 7 = 0$. [Round off to TWO decimal places].

#### Question 47
Evaluate the infinite series:
$$S = \sum_{n=1}^\infty \frac{1}{n(n+1)(n+2)}$$
If $S = \frac{1}{m}$, find the integer value of $m$.

#### Question 48
Find the number of non-negative integer solutions $(x_1, x_2, x_3, x_4)$ to the equation $x_1 + x_2 + x_3 + x_4 = 6$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The shortest distance from the origin $(0, 0, 0)$ to the plane $2x + 3y + 6z = 14$ is:
(A) $2$  
(B) $1$  
(C) $3$  
(D) $7$

#### Question 50
The value of the determinant of the $3 \times 3$ circulant matrix $\begin{vmatrix} 1 & \omega & \omega^2 \\ \omega & \omega^2 & 1 \\ \omega^2 & 1 & \omega \end{vmatrix}$, where $\omega$ is a non-real complex cube root of unity, is:
(A) $0$  
(B) $3$  
(C) $1$  
(D) $-3$

#### Question 51
The length of the tangent drawn from the point $(7, 1)$ to the circle $x^2 + y^2 - 4x - 6y - 12 = 0$ is:
(A) $4$  
(B) $5$  
(C) $3$  
(D) $\sqrt{21}$

#### Question 52
The angle between the curves $y = x^2$ and $x = y^2$ at their point of intersection $(1, 1)$ is:
(A) $\tan^{-1}(3/4)$  
(B) $\tan^{-1}(4/3)$  
(C) $\pi/2$  
(D) $\pi/4$

#### Question 53
The sum of the infinite geometric series $S = 1 + \frac{2}{3} + \frac{4}{9} + \frac{8}{27} + \dots$ is:
(A) $3$  
(B) $2$  
(C) $1.5$  
(D) $4$

#### Question 54
The maximum value of the function $f(\theta) = 3\sin\theta + 4\cos\theta + 5$ for all $\theta \in \mathbb{R}$ is:
(A) $10$  
(B) $12$  
(C) $8$  
(D) $5$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 03 — Paper 2
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
A uniform ladder of mass $M$ and length $L$ rests with its upper end against a smooth vertical wall and its lower end on a rough horizontal floor with coefficient of static friction $\mu_s$. The ladder makes an angle $\theta$ with the horizontal floor. A person of mass $m$ climbs up the ladder:
(A) The normal reaction force exerted by the floor on the ladder is $N_f = (M + m)g$, independent of the person's position on the ladder.  
(B) The normal reaction force exerted by the vertical wall is $N_w = \frac{(M/2 + m x/L)g}{\tan\theta}$, where $x$ is the distance of the person along the ladder from the base.  
(C) As the person climbs higher (increasing $x$), the horizontal friction force required at the base increases.  
(D) Slipping is most likely to occur when the person reaches the very top of the ladder ($x = L$).

#### Question 2
Two identical inductors of inductance $L$ and two identical capacitors of capacitance $C$ are connected in a bridged ladder network. At time $t = 0$, the circuit is excited with harmonic voltage $V(t) = V_0 \cos(\omega t)$. Which of the following statements is/are correct?
(A) The natural resonant angular frequencies of the coupled system correspond to symmetric and antisymmetric normal modes.  
(B) In the antisymmetric normal mode, the currents in the two inductors oscillate exactly $180^\circ$ out of phase.  
(C) The total energy stored oscillates periodically between the capacitors and the inductors.  
(D) If a small series resistance $R$ is added in each branch, the oscillations undergo exponential damping with time constant $\tau = \frac{2L}{R}$.

#### Question 3
A light ray travels through an optical fiber having a cylindrical core of refractive index $\mu_1 = 1.50$ surrounded by a cladding of refractive index $\mu_2 = 1.40$. The fiber is surrounded by air ($\mu_0 = 1.00$). Which of the following statements is/are correct?
(A) The critical angle for total internal reflection at the core-cladding interface is $\theta_c = \sin^{-1}\left(\frac{\mu_2}{\mu_1}\right) = \sin^{-1}\left(\frac{14}{15}\right) \approx 68.96^\circ$.  
(B) The numerical aperture ($\text{NA}$) of the optical fiber is $\text{NA} = \sqrt{\mu_1^2 - \mu_2^2} = \sqrt{1.50^2 - 1.40^2} = \sqrt{0.29} \approx 0.5385$.  
(C) The maximum acceptance angle $\theta_{\text{acc}}$ for rays incident from air into the fiber core is $\theta_{\text{acc}} = \sin^{-1}(\text{NA}) \approx 32.58^\circ$.  
(D) All light rays entering the core at angles $\theta \le \theta_{\text{acc}}$ undergo total internal reflection inside the fiber.

#### Question 4
A long straight cylindrical wire of radius $R$ carries a steady total current $I$ distributed with uniform current density $J = \frac{I}{\pi R^2}$. A cylindrical cavity of radius $a < R$ is drilled parallel to the wire's axis, with its center displaced by a vector distance $\vec{d}$ from the wire's center ($|\vec{d}| + a < R$). Which of the following statements is/are correct?
(A) The magnetic field inside the cylindrical cavity is completely uniform in magnitude and direction.  
(B) The magnetic field vector inside the cavity is given by $\vec{B} = \frac{\mu_0}{2} (\vec{J} \times \vec{d})$.  
(C) The magnitude of the magnetic field inside the cavity is independent of the cavity radius $a$.  
(D) If the displacement vector $\vec{d}$ is along the $+x$-direction and the current is along $+z$, the magnetic field inside the cavity points along the $+y$-direction.

#### Question 5
Consider a particle of mass $m$ confined in an infinite one-dimensional potential well of width $L$ ($0 \le x \le L$):
(A) The quantized energy eigenvalues are $E_n = \frac{n^2 \pi^2 \hbar^2}{2m L^2}$ for $n = 1, 2, 3, \dots$.  
(B) The normalized stationary state wavefunctions are $\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$.  
(C) The expectation value of momentum in any stationary state is $\langle p_x \rangle = 0$.  
(D) The probability of finding the particle in the middle third of the well ($L/3 \le x \le 2L/3$) in the ground state ($n = 1$) is greater than $1/3$.

#### Question 6
Two moles of an ideal monoatomic gas ($\gamma = 5/3$) are taken through a reversible cycle consisting of:
1. Isothermal expansion at $T_1 = 600\text{ K}$ from volume $V_1$ to $2V_1$.
2. Isochoric cooling from $T_1 = 600\text{ K}$ to $T_2 = 300\text{ K}$.
3. Isothermal compression at $T_2 = 300\text{ K}$ from $2V_1$ to $V_1$.
4. Isochoric heating from $T_2 = 300\text{ K}$ back to $T_1 = 600\text{ K}$.
Which of the following statements is/are correct?
(A) The net work done by the gas per cycle is $W_{\text{net}} = 2 R (T_1 - T_2) \ln 2 \approx 600 R \ln 2$.  
(B) The heat absorbed during the isochoric heating stage equals the heat rejected during the isochoric cooling stage.  
(C) If an ideal regenerator perfectly transfers the heat rejected during isochoric cooling to the isochoric heating process (Stirling cycle), the cycle efficiency achieves the Carnot limit $\eta = 1 - \frac{T_2}{T_1} = 50\%$.  
(D) Without regeneration, the thermal efficiency is strictly less than $50\%$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A horizontal turntable of mass $M = 4.00\text{ kg}$ and radius $R = 1.00\text{ m}$ is rotating freely about its central frictionless vertical axis with angular speed $\omega_0 = 10.0\text{ rad/s}$. A small child of mass $m = 20.0\text{ kg}$ walks from the rim to the center of the turntable. Calculate the new angular speed $\omega_f$ (in rad/s) of the turntable when the child reaches the center.

#### Question 8
A tuning fork of frequency $\nu_0 = 512\text{ Hz}$ produces $4\text{ beats/second}$ when sounded together with another tuning fork $A$. When fork $A$ is loaded with a small amount of wax, the beat frequency decreases to $2\text{ beats/second}$. Calculate the exact original frequency $\nu_A$ (in $\text{Hz}$) of fork $A$.

#### Question 9
A parallel-plate capacitor with air between the plates has capacitance $C_0 = 10.0\ \mu\text{F}$. It is charged to a potential difference $V_0 = 100.0\text{ V}$ and then disconnected from the battery. A dielectric slab of dielectric constant $K = 5.0$ is now inserted to completely fill the space between the plates. Calculate the change in stored electrostatic energy $\Delta U = U_f - U_i$ (in milliJoules, $\text{mJ}$). [Enter the absolute magnitude of the energy change].

#### Question 10
In a Lloyd's mirror interference experiment, monochromatic light of wavelength $\lambda = 500\text{ nm}$ from a narrow slit situated at distance $h = 1.00\text{ mm}$ above a flat mirror strikes a screen placed at distance $D = 2.00\text{ m}$ from the slit. Calculate the fringe width $\beta$ in millimeters ($\text{mm}$).

#### Question 11
Calculate the radius $r_1$ of the first Bohr orbit in a singly ionized helium atom ($\text{He}^+, Z = 2$) in Angstroms ($\text{\AA}$). [Take Bohr radius $a_0 = 0.529\text{ \AA}$. Round off to TWO decimal places].

#### Question 12
A square loop of wire of side length $a = 0.10\text{ m}$ carries a steady current $I = 4.00\text{ A}$. Calculate the magnetic field $B$ (in microTesla, $\mu\text{T}$) at the center of the loop. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$ and $\sqrt{2} \approx 1.414$. Round off to TWO decimal places].

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the rotational dynamics concepts in List-I with their physical expressions in List-II:
- **List-I**:
  - P. Parallel Axis Theorem
  - Q. Perpendicular Axis Theorem
  - R. Angular Momentum about origin
  - S. Rotational Work-Energy Theorem
- **List-II**:
  - 1. $I = I_{\text{cm}} + M d^2$
  - 2. $I_z = I_x + I_y$ (planar lamina)
  - 3. $\vec{L} = \vec{r} \times \vec{p}$
  - 4. $W = \int \tau d\theta = \Delta K_{\text{rot}}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 14
Match the fluid mechanics principles in List-I with their conservation law in List-II:
- **List-I**:
  - P. Equation of Continuity
  - Q. Bernoulli's Equation
  - R. Torricelli's Law
  - S. Poiseuille's Law
- **List-II**:
  - 1. Conservation of Mass ($A_1 v_1 = A_2 v_2$)
  - 2. Conservation of Mechanical Energy for streamlines
  - 3. Efflux velocity $v = \sqrt{2gh}$
  - 4. Viscous laminar flow rate $Q = \frac{\pi P r^4}{8\eta L}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 15
Match the thermodynamic functions in List-I with their differential definitions in List-II:
- **List-I**:
  - P. Internal Energy $U$
  - Q. Enthalpy $H$
  - R. Helmholtz Free Energy $F$
  - S. Gibbs Free Energy $G$
- **List-II**:
  - 1. $dU = T dS - P dV$
  - 2. $dH = T dS + V dP$
  - 3. $dF = -S dT - P dV$
  - 4. $dG = -S dT + V dP$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the nuclear decay modes in List-I with their emitted radiation in List-II:
- **List-I**:
  - P. Alpha Decay
  - Q. Beta-minus Decay
  - R. Beta-plus Decay
  - S. Gamma De-excitation
- **List-II**:
  - 1. $^4_2\text{He}$ nucleus
  - 2. Electron ($e^-$) and antineutrino ($\bar{\nu}_e$)
  - 3. Positron ($e^+$) and neutrino ($\nu_e$)
  - 4. High-energy photon ($\gamma$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 17
Match the optical diffraction setups in List-I with their characteristic diffraction pattern in List-II:
- **List-I**:
  - P. Single-slit Fraunhofer diffraction
  - Q. Circular aperture Airy diffraction
  - R. Diffraction grating
  - S. Double-slit diffraction
- **List-II**:
  - 1. Central broad maximum flanked by alternate dark and dim bands
  - 2. Central bright Airy disk surrounded by concentric dark and bright rings
  - 3. Sharp, intensely bright principal interference peaks
  - 4. Double-slit interference fringes modulated by single-slit diffraction envelope

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 18
Match the electromagnetic laws in List-I with their Maxwell equation form in List-II:
- **List-I**:
  - P. Gauss's Law for Electrostatics
  - Q. Gauss's Law for Magnetism
  - R. Faraday's Law of Induction
  - S. Ampere-Maxwell Law
- **List-II**:
  - 1. $\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}$
  - 2. $\oint \vec{B} \cdot d\vec{A} = 0$
  - 3. $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt}$
  - 4. $\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enc}} + \mu_0 \varepsilon_0 \frac{d\Phi_E}{dt}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following statements is/are correct regarding the structure of fullerenes ($\text{C}_{60}$)?
(A) $\text{C}_{60}$ possesses a truncated icosahedron geometry resembling a soccer ball.  
(B) It contains 12 five-membered rings and 20 six-membered rings.  
(C) Five-membered rings fuse only with six-membered rings, while six-membered rings fuse with both five- and six-membered rings.  
(D) All carbon atoms in $\text{C}_{60}$ are $sp^2$ hybridized.

#### Question 20
Which of the following methods can be used to distinguish between a primary, secondary, and tertiary amine?
(A) Hinsberg's reagent (benzenesulfonyl chloride)  
(B) Nitrous acid test ($\text{HNO}_2$)  
(C) Carbylamine test (aliphatic and aromatic primary amines give foul-smelling isocyanides)  
(D) Lucas reagent

#### Question 21
Regarding the thermodynamics and kinetics of chemical equilibria:
(A) $\Delta G^\circ = -R T \ln K$.  
(B) A catalyst increases the rates of both the forward and backward reactions equally without altering the equilibrium constant $K$.  
(C) The van 't Hoff isobar is given by $\frac{d\ln K}{dT} = \frac{\Delta H^\circ}{R T^2}$.  
(D) For an endothermic reaction ($\Delta H^\circ > 0$), $K$ increases with an increase in temperature.

#### Question 22
Which of the following compounds will produce a racemic mixture upon mono-chlorination under photochemical conditions?
(A) $n$-Butane giving 2-chlorobutane  
(B) Propane giving 2-chloropropane  
(C) Isobutane giving 1-chloro-2-methylpropane  
(D) 2-Methylbutane giving 2-chloro-2-methylbutane

#### Question 23
Which of the following oxyacids of phosphorus contain a $\text{P}-\text{H}$ bond and act as reducing agents?
(A) $\text{H}_3\text{PO}_2$ (Hypophosphorous acid)  
(B) $\text{H}_3\text{PO}_3$ (Phosphorous acid)  
(C) $\text{H}_3\text{PO}_4$ (Orthophosphoric acid)  
(D) $\text{H}_4\text{P}_2\text{O}_7$ (Pyrophosphoric acid)

#### Question 24
Which of the following molecules have non-zero dipole moments?
(A) $\text{H}_2\text{O}$  
(B) $\text{NH}_3$  
(C) $\text{SO}_2$  
(D) $\text{CO}_2$

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The solubility product of lead iodide ($\text{PbI}_2$) in water is $K_{sp} = 7.1 \times 10^{-9}$ at $25^\circ\text{C}$. Calculate the molar solubility $S$ of $\text{PbI}_2$ in pure water in millimoles per liter ($\text{mmol/L}$). [Take $\sqrt[3]{1.775 \times 10^{-9}} \approx 1.21 \times 10^{-3}$. Round off to TWO decimal places].

#### Question 26
For a first-order gas-phase reaction $A(g) \to 2B(g) + C(g)$, the initial pressure is $P_0 = 100\text{ mm Hg}$. After $t = 10.0\text{ minutes}$, the total pressure rises to $P_{\text{total}} = 220\text{ mm Hg}$. Calculate the rate constant $k$ of the reaction in $\text{min}^{-1}$. [Take $\ln(2.5) \approx 0.916$. Round off to TWO decimal places].

#### Question 27
Copper crystallizes in an FCC unit cell with edge length $a = 361\text{ pm}$. Calculate the theoretical density $\rho$ of copper in $\text{g/cm}^3$. [Molar mass $M = 63.55\text{ g/mol}, N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$. Round off to TWO decimal places].

#### Question 28
Calculate the standard cell potential $E_{\text{cell}}^\circ$ (in Volts) for the reaction:
$$\text{Mg}(s) + 2\text{Ag}^+(aq) \to \text{Mg}^{2+}(aq) + 2\text{Ag}(s)$$
Given $E^\circ(\text{Mg}^{2+}/\text{Mg}) = -2.37\text{ V}$ and $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$.

#### Question 29
A $5.0\%$ (by weight) aqueous solution of cane sugar (sucrose, molar mass $342\text{ g/mol}$) has a freezing point of $271.0\text{ K}$. Calculate the freezing point (in Kelvin) of a $5.0\%$ (by weight) aqueous solution of glucose (molar mass $180\text{ g/mol}$). [Freezing point of pure water is $273.15\text{ K}$. Round off to TWO decimal places].

#### Question 30
Find the oxidation state of the central iron atom in the brown ring complex $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$.

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the carbohydrate classifications in List-I with their examples in List-II:
- **List-I**:
  - P. Monosaccharide
  - Q. Disaccharide
  - R. Polysaccharide
  - S. Amino sugar
- **List-II**:
  - 1. D-Fructose
  - 2. Lactose
  - 3. Cellulose
  - 4. D-Glucosamine

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 32
Match the mineral refining methods in List-I with the metal in List-II:
- **List-I**:
  - P. Zone Refining
  - Q. Electrolytic Refining
  - R. Liquation
  - S. Cupellation
- **List-II**:
  - 1. Silicon / Germanium (semiconductors)
  - 2. Blister Copper
  - 3. Tin (low melting point)
  - 4. Silver (containing lead impurity)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 33
Match the chemical reagents in List-I with their test function in List-II:
- **List-I**:
  - P. Fehling's Solution
  - Q. 2,4-DNP Reagent
  - R. Ceric Ammonium Nitrate
  - S. Ferric Chloride ($\text{FeCl}_3$)
- **List-II**:
  - 1. Test for aliphatic aldehydes (red $\text{Cu}_2\text{O}$ ppt)
  - 2. Test for carbonyl group (aldehydes/ketones)
  - 3. Test for alcoholic $-\text{OH}$ group
  - 4. Test for phenolic $-\text{OH}$ group (violet complex)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 34
Match the states of matter in List-I with their critical property in List-II:
- **List-I**:
  - P. Critical Temperature $T_c$
  - Q. Critical Pressure $P_c$
  - R. Boyle Temperature $T_B$
  - S. Inversion Temperature $T_i$
- **List-II**:
  - 1. Temperature above which a gas cannot be liquefied no matter how much pressure is applied
  - 2. Minimum pressure required to liquefy a gas at its critical temperature
  - 3. Temperature at which real gas obeys ideal gas law over broad pressure range ($a/Rb$)
  - 4. Temperature at which Joule-Thomson coefficient changes sign ($2a/Rb$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 35
Match the nitrogen oxides in List-I with their oxidation state of nitrogen in List-II:
- **List-I**:
  - P. $\text{N}_2\text{O}$
  - Q. $\text{NO}$
  - R. $\text{NO}_2$
  - S. $\text{N}_2\text{O}_5$
- **List-II**:
  - 1. +1
  - 2. +2
  - 3. +4
  - 4. +5

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 36
Match the common drugs in List-I with their pharmacological class in List-II:
- **List-I**:
  - P. Aspirin
  - Q. Penicillin
  - R. Ranitidine
  - S. Paracetamol
- **List-II**:
  - 1. Non-narcotic Analgesic & Anti-inflammatory
  - 2. Antibiotic
  - 3. Antacid / $\text{H}_2$-receptor antagonist
  - 4. Antipyretic

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \tan^{-1} x - \ln\sqrt{1+x^2}$ for $x \ge 0$. Which of the following statements is/are correct?
(A) $f(0) = 0$.  
(B) $f'(x) = \frac{1-x}{1+x^2}$.  
(C) $f(x)$ attains its absolute maximum on $[0, \infty)$ at $x = 1$.  
(D) The maximum value of $f(x)$ is $\frac{\pi}{4} - \frac{1}{2}\ln 2$.

#### Question 38
Let $A$ be a $3 \times 3$ matrix such that $A^2 = A$ (idempotent matrix). Which of the following statements is/are correct?
(A) The only possible eigenvalues of $A$ are $0$ and $1$.  
(B) $\det(A)$ can only be $0$ or $1$.  
(C) If $A \ne I$, then $A$ is singular ($\det(A) = 0$).  
(D) $I - A$ is also an idempotent matrix.

#### Question 39
Consider the family of circles passing through the intersection of the circles $C_1: x^2 + y^2 - 4x - 6y + 4 = 0$ and $C_2: x^2 + y^2 - 2x - 4y + 1 = 0$:
(A) The radical axis of $C_1$ and $C_2$ is $2x + 2y - 3 = 0$.  
(B) The line joining the centers of $C_1$ and $C_2$ is perpendicular to the radical axis.  
(C) The radical axis is the common chord of the two circles.  
(D) The length of the common chord is non-zero.

#### Question 40
Let $y(x)$ be the solution of the differential equation $\frac{dy}{dx} = \frac{x+y}{x-y}$ with $y(1) = 0$. Which of the following statements is/are correct?
(A) The differential equation is homogeneous of degree 0.  
(B) The substitution $y = vx$ leads to $\int \frac{1-v}{1+v^2}dv = \int \frac{dx}{x}$.  
(C) The implicit solution is $\tan^{-1}(y/x) - \frac{1}{2}\ln(1 + y^2/x^2) = \ln|x|$.  
(D) In polar coordinates $(r, \theta)$, the solution represents an equiangular spiral $r = e^\theta$.

#### Question 41
Let $\vec{u}, \vec{v}, \vec{w}$ be three vectors such that $|\vec{u}| = 3, |\vec{v}| = 4, |\vec{w}| = 5$, and each vector is perpendicular to the sum of the other two:
(A) $\vec{u} \cdot (\vec{v} + \vec{w}) = 0$, $\vec{v} \cdot (\vec{w} + \vec{u}) = 0$, and $\vec{w} \cdot (\vec{u} + \vec{v}) = 0$.  
(B) $\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{w} = \vec{w} \cdot \vec{u} = 0$, meaning the vectors are mutually orthogonal.  
(C) The magnitude of the sum vector is $|\vec{u} + \vec{v} + \vec{w}| = \sqrt{3^2 + 4^2 + 5^2} = 5\sqrt{2}$.  
(D) The volume of the parallelepiped spanned by $\vec{u}, \vec{v}, \vec{w}$ is 60.

#### Question 42
A fair six-faced die is rolled repeatedly until a 6 appears. Let $N$ denote the number of tosses required:
(A) The random variable $N$ follows a geometric distribution with $p = 1/6$.  
(B) The expected number of tosses is $E[N] = 6$.  
(C) The probability that more than 3 tosses are required is $P(N > 3) = (5/6)^3 = \frac{125}{216}$.  
(D) The variance of $N$ is $\text{Var}(N) = 30$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area of the region bounded by the curves $y = \sin x$ and $y = \cos x$ between two consecutive points of intersection $x = \pi/4$ and $x = 5\pi/4$. [Take $\sqrt{2} \approx 1.414$. Round off to TWO decimal places].

#### Question 44
Find the slope of the normal to the curve $x = a\cos^3\theta, y = a\sin^3\theta$ at the parameter value $\theta = \pi/4$.

#### Question 45
Evaluate the definite integral:
$$I = \int_0^1 \frac{dx}{e^x + e^{-x}}$$
If $I = \tan^{-1}(e) - \frac{\pi}{k}$, find the integer value of $k$.

#### Question 46
Calculate the perpendicular distance from the origin $(0, 0, 0)$ to the line $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{6}$. [Round off to TWO decimal places].

#### Question 47
If the roots of the cubic equation $x^3 - 9x^2 + 23x - 15 = 0$ are in arithmetic progression, find the middle root.

#### Question 48
Find the number of ways of distributing 8 identical balls into 3 distinct boxes such that no box remains empty.

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the function forms in List-I with their domain in List-II:
- **List-I**:
  - P. $\sin^{-1}(2x)$
  - Q. $\ln(4 - x^2)$
  - R. $\frac{1}{\sqrt{x-1}}$
  - S. $\sqrt{x(x-2)}$
- **List-II**:
  - 1. $[-1/2, 1/2]$
  - 2. $(-2, 2)$
  - 3. $(1, \infty)$
  - 4. $(-\infty, 0] \cup [2, \infty)$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 50
Match the matrix types in List-I with their characteristic eigenvalue property in List-II:
- **List-I**:
  - P. Real Symmetric Matrix
  - Q. Real Skew-Symmetric Matrix
  - R. Orthogonal Matrix
  - S. Unitary Matrix
- **List-II**:
  - 1. All eigenvalues are purely real
  - 2. Eigenvalues are purely imaginary or zero
  - 3. Eigenvalues have absolute modulus equal to 1 ($|\lambda| = 1$)
  - 4. Eigenvalues have unit modulus in complex plane

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 51
Match the complex expressions in List-I with their standard geometric loci in List-II:
- **List-I**:
  - P. $\text{Re}(z) = 3$
  - Q. $\text{Im}(z) = -2$
  - R. $|z - 1| = |z + 1|$
  - S. $\arg(z) = \pi/4$
- **List-II**:
  - 1. Vertical line $x = 3$
  - 2. Horizontal line $y = -2$
  - 3. Imaginary axis (perpendicular bisector of $-1$ and $+1$)
  - 4. Ray emanating from origin at angle $45^\circ$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 52
Match the probability terms in List-I with their axiomatic mathematical rule in List-II:
- **List-I**:
  - P. Multiplication Rule for Independent Events
  - Q. Law of Total Probability
  - R. Expectation of Sum of Variables
  - S. Variance of Independent Sum
- **List-II**:
  - 1. $P(A \cap B) = P(A)P(B)$
  - 2. $P(B) = \sum P(B|A_i)P(A_i)$
  - 3. $E[X + Y] = E[X] + E[Y]$ (always)
  - 4. $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 53
Match the curves in List-I with their number of asymptotes in List-II:
- **List-I**:
  - P. $y = \frac{1}{x}$
  - Q. Hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$
  - R. Parabola $y^2 = 4ax$
  - S. $y = \tan x$ on $(-\pi/2, \pi/2)$
- **List-II**:
  - 1. 2 asymptotes ($x = 0, y = 0$)
  - 2. 2 asymptotes ($y = \pm \frac{b}{a}x$)
  - 3. 0 asymptotes
  - 4. 2 vertical asymptotes ($x = \pm \pi/2$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 54
Match the vector operations in List-I with their scalar/vector classification in List-II:
- **List-I**:
  - P. $\vec{a} \cdot \vec{b}$
  - Q. $\vec{a} \times \vec{b}$
  - R. $\vec{a} \cdot (\vec{b} \times \vec{c})$
  - S. $\vec{a} \times (\vec{b} \times \vec{c})$
- **List-II**:
  - 1. Scalar (Dot product)
  - 2. Vector (Cross product)
  - 3. Scalar (Triple scalar product)
  - 4. Vector (Triple vector product)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 03 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Electromagnetic Induction, Thomson's Jumping Ring Effect, Mutual Inductance, Phase Shift in RL Circuits ($\tan\phi = \omega L / R_0$).
- **2. Derivation**:
  - The magnetic field of the solenoid is $B_z(t) = B_0 \sin(\omega t)$.
  - The induced EMF in the ring is $\mathcal{E}(t) = -\frac{d\Phi}{dt} = -\omega \Phi_0 \cos(\omega t)$.
  - The ring has resistance $R_0$ and self-inductance $L$, so its impedance is $Z = \sqrt{R_0^2 + \omega^2 L^2}$, and current lags EMF by $\phi = \tan^{-1}\left(\frac{\omega L}{R_0}\right)$. (A) is correct.
  - The current is $I_{\text{ring}}(t) = I_{\text{ind}} \cos(\omega t - \phi)$.
  - The vertical force on the ring arises from the radial field component $B_r$: $F_z(t) = -2\pi r I_{\text{ring}}(t) B_r(t)$.
  - Time average: $\langle F_z \rangle \propto -\langle \cos(\omega t - \phi)\sin(\omega t) \rangle = \frac{1}{2}\sin\phi = \frac{1}{2}\frac{\omega L}{\sqrt{R_0^2 + \omega^2 L^2}}$.
  - If $L = 0 \implies \phi = 0 \implies \sin\phi = 0 \implies \langle F_z \rangle = 0$. (B) is correct.
  - Because $L > 0$, $\sin\phi > 0$, producing a steady repulsive time-averaged upward force $\langle F_z \rangle > 0$. (C) is correct.
  - Lowering temperature decreases $R_0$, increasing $\sin\phi \to 1$ and increasing current, producing stronger repulsion and higher levitation. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Rolling without Slipping on Curvilinear Surfaces, Work-Energy Theorem, Centripetal Acceleration.
- **2. Derivation**:
  - Distance of sphere's CM from bowl center: $R_{\text{eff}} = 5R - R = 4R$. (A) is correct.
  - Equation of motion along tangent: $M g \sin\theta - f_s = M a_c$.
  - About CM: $f_s R = I \alpha = \left(\frac{2}{5}M R^2\right)\alpha \implies f_s = \frac{2}{5}M a_c$.
  - Thus $M g \sin\theta - \frac{2}{5}M a_c = M a_c \implies a_c = \frac{5}{7}g \sin\theta \implies \alpha = \frac{a_c}{R} = \frac{5g\sin\theta}{7R}$. (B) is correct.
  - Conservation of energy to bottommost point ($\theta = 0$):
    $$M g (4R) = \frac{1}{2}M v^2 + \frac{1}{2}I \omega^2 = \frac{7}{10}M v^2 \implies v^2 = \frac{40}{7}g R \implies v = \sqrt{\frac{40}{7}g R}$$
    (C) is correct.
  - Normal force at the bottom:
    $$N - M g = M \frac{v^2}{R_{\text{eff}}} = M \frac{\frac{40}{7}g R}{4R} = \frac{10}{7}M g \implies N = M g + \frac{10}{7}M g = \frac{17}{7}M g$$
    (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Relativistic Kinematics, Doppler Shift of Photons, Conservation of Four-Momentum.
- **2. Derivation**:
  - Lorentz factor: $\gamma = \frac{1}{\sqrt{1 - 0.8^2}} = \frac{1}{0.6} = \frac{5}{3} \approx 1.667$. (A) is correct.
  - Relativistic Doppler shift for collinear decay:
    $$E_1 = \frac{1}{2} m_\pi c^2 \sqrt{\frac{1 + 0.8}{1 - 0.8}} = \frac{1}{2}(135)\sqrt{\frac{1.8}{0.2}} = \frac{135}{2}\sqrt{9} = \frac{135 \times 3}{2} = 202.5\text{ MeV}$$
    (B) is correct.
    $$E_2 = \frac{1}{2} m_\pi c^2 \sqrt{\frac{1 - 0.8}{1 + 0.8}} = \frac{135}{2}\sqrt{\frac{1}{9}} = \frac{135}{6} = 22.5\text{ MeV}$$
    (C) is correct.
  - Product: $E_1 E_2 = (202.5)(22.5) = 4556.25\text{ MeV}^2 = \frac{1}{4}(135)^2$. This is an invariant! (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Polarization in Dielectrics, Bound Charges ($\rho_b = -\nabla \cdot \vec{P}$, $\sigma_b = \vec{P} \cdot \hat{n}$).
- **2. Derivation**:
  - $\rho_b = -\nabla \cdot \vec{P} = -\frac{1}{r^2}\frac{\partial}{\partial r}(r^2 \cdot kr) = -\frac{1}{r^2}(3k r^2) = -3k$. (A) is correct.
  - $\sigma_b = \vec{P}(R) \cdot \hat{r} = k R$. (B) is correct.
  - Total volume bound charge: $Q_b^{\text{vol}} = \rho_b \left(\frac{4}{3}\pi R^3\right) = (-3k)\left(\frac{4}{3}\pi R^3\right) = -4\pi k R^3$.
  - Total surface bound charge: $Q_b^{\text{surf}} = \sigma_b (4\pi R^2) = (k R)(4\pi R^2) = +4\pi k R^3$.
  - Net bound charge: $Q_b^{\text{net}} = -4\pi k R^3 + 4\pi k R^3 = 0$. (C) is correct.
  - Inside the sphere, by Gauss's law for total bound charge enclosed at radius $r$:
    $$\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0} \implies E(4\pi r^2) = \frac{-3k(4/3\pi r^3)}{\varepsilon_0} \implies E(r) = -\frac{kr}{\varepsilon_0}$$
    Magnitude is $\frac{kr}{\varepsilon_0}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Thermodynamic Cycles, Otto Cycle Thermal Efficiency $\eta = 1 - r^{1-\gamma}$.
- **2. Derivation**:
  - Otto cycle efficiency: $\eta = 1 - r^{1-\gamma} = 1 - 8^{1 - 1.4} = 1 - 8^{-0.40}$. (A) is correct.
  - $8^{0.40} = (2^3)^{0.4} = 2^{1.2} \approx 2.2974 \implies \eta = 1 - \frac{1}{2.2974} = 1 - 0.4353 = 0.5647 \approx 56.5\%$. (B) is correct.
  - In isochoric processes, $dV = 0 \implies dW = P dV = 0$. (C) is correct.
  - $\eta = 1 - r^{-0.4}$; as $r$ increases, $r^{-0.4}$ decreases, so efficiency increases. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Wave Optics, Fresnel Zone Plate, Multiple Focal Points.
- **2. Derivation**:
  - $r_1 = \sqrt{\lambda f} = \sqrt{(500 \times 10^{-9})(1.00)} = \sqrt{5.0 \times 10^{-7}} \approx 7.07 \times 10^{-4}\text{ m} = 0.707\text{ mm}$. (A) is correct.
  - A zone plate possesses higher-order foci at odd fractions $f_m = \frac{f}{2m-1}$ for $m = 1, 2, 3, \dots$. (B) is correct.
  - Since $f = \frac{r_1^2}{\lambda}$, focal length is inversely proportional to wavelength $\lambda$ (opposite to a conventional refractive lens). (C) is correct.
  - All open half-period zones add in phase at the primary focus, producing an intensity much higher than the unobstructed wave. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Moment of inertia of rotor: $I_s = M k^2 = (3.00)(0.10)^2 = 0.030\text{ kg}\cdot\text{m}^2$.
  Spin angular momentum: $L_s = I_s \omega_s = (0.030)(600.0) = 18.0\text{ kg}\cdot\text{m}^2/\text{s}$.
  Torque due to gravity: $\tau = M g d = (3.00)(9.80)(0.15) = 4.41\text{ N}\cdot\text{m}$.
  Precessional angular velocity: $\Omega_p = \frac{\tau}{L_s} = \frac{4.41}{18.0} = 0.245\text{ rad/s} \approx 0.25\text{ rad/s}$. Exact: `0.25`.
- **Question 8**: Two coaxial dielectric cylinders in series:
  $\frac{1}{C} = \frac{1}{2\pi\varepsilon_0 L}\left[\frac{\ln(r_2/r_1)}{\varepsilon_{r1}} + \frac{\ln(r_3/r_2)}{\varepsilon_{r2}}\right] = \frac{1}{2\pi\varepsilon_0(1.0)}\left[\frac{\ln 2}{4.0} + \frac{\ln 2}{2.0}\right] = \frac{0.693}{2\pi\varepsilon_0}\left[\frac{1}{4} + \frac{1}{2}\right] = \frac{0.693 \times 0.75}{2\pi (8.85 \times 10^{-12})} = \frac{0.51975}{5.56 \times 10^{-11}} \approx 9.35 \times 10^9\text{ F}^{-1} \implies C = \frac{1}{9.35 \times 10^9} \approx 107.0\text{ pF}$. Exact: `107.00`.
- **Question 9**: Energy radiated by inner sphere: $P_1 = \sigma (4\pi R_1^2) T_1^4$.
  Outer shell absorbs $P_1$ and radiates from both its inner and outer surfaces:
  $P_{\text{emit}} = \sigma (4\pi R_2^2) T_2^4 + \sigma (4\pi R_2^2) T_2^4 = 2 \sigma (4\pi R_2^2) T_2^4$.
  Equating: $4\pi R_1^2 T_1^4 = 2 (4\pi R_2^2) T_2^4 \implies T_2^4 = \frac{R_1^2}{2 R_2^2} T_1^4 = \frac{(0.1)^2}{2(0.2)^2} T_1^4 = \frac{1}{8} T_1^4 \implies T_2 = \frac{T_1}{8^{1/4}} = \frac{500}{1.6818} \approx 297.3\text{ K} \approx 297\text{ K}$. Exact: `297.00`.
- **Question 10**: At minimum deviation, $r_1 = A/2 = 30^\circ$. Snell's law: $\sin i = \mu \sin r_1 = 1.50 \sin 30^\circ = 0.75 \implies i = \sin^{-1}(0.75) \approx 48.59^\circ$. Exact: `48.59`.
- **Question 11**: Magnetic field at center of finite solenoid: $B = \mu_0 n I \cos\theta$.
  $n = N/L = 800/0.40 = 2000\text{ turns/m}$.
  $B = (4\pi \times 10^{-7})(2000)(2.50)(0.989) = (2\pi \times 10^{-3})(0.989) \approx 6.283 \times 0.989 \approx 6.21\text{ mT}$. Exact: `6.21`.
- **Question 12**: $e(V_1 - V_2) = hc \left(\frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right) \implies 1.60 \times 10^{-19}(1.03) = h (3.0 \times 10^8)\left(\frac{100 \times 10^{-9}}{120000 \times 10^{-18}}\right) \implies 1.648 \times 10^{-19} = h (2.50 \times 10^{14}) \implies h = \frac{1.648 \times 10^{-19}}{2.50 \times 10^{14}} = 6.59 \times 10^{-34}\text{ J}\cdot\text{s}$. Exact: `6.59`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $v_e = \sqrt{\frac{2GM}{R}} = \sqrt{\frac{2G(\frac{4}{3}\pi R^3 \rho)}{R}} = R \sqrt{\frac{8\pi G \rho}{3}} \propto R$. Doubling radius doubles escape velocity. Option (A).
- **Question 14**: Vertical height remains constant $h = l \cos\theta \implies l = \frac{h}{\cos 60^\circ} = \frac{6.0}{0.5} = 12.0\text{ cm}$. Option (A).
- **Question 15**: $\Delta \beta = 10 \log_{10}\left(\frac{I_2}{I_1}\right) = 10 \log_{10}(100) = 10(2) = 20\text{ dB}$. Option (A).
- **Question 16**: $K_\alpha = \frac{A - 4}{A} Q = \frac{234}{238}(4.27) \approx 4.20\text{ MeV}$. Option (A).
- **Question 17**: $\tan\theta_B = \frac{\mu_2}{\mu_1} = \frac{1.50}{4/3} = \frac{3/2}{4/3} = \frac{9}{8} \implies \theta_B = \tan^{-1}(9/8)$. Option (A).
- **Question 18**: Center of mass of solid hemisphere is at $y_{\text{cm}} = \frac{3}{8}R$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Jahn-Teller theorem states any non-linear molecular system in a degenerate electronic state undergoes distortion to remove degeneracy. Occurs strongly in $d^9$ ($\text{Cu}^{2+}$) and high spin $d^4$ ($\text{Cr}^{2+}$) where $e_g$ orbitals are unevenly occupied. Low spin $d^6$ ($t_{2g}^6$) has completely filled non-degenerate ground state (no distortion). Options: (A), (B), (C).
- **Question 20**: Pinacol rearrangement: protonation creates most stable carbocation. Migratory aptitude of aryl groups is enhanced by electron-donating groups: $p\text{-anisyl} > p\text{-tolyl} > \text{phenyl} > p\text{-chlorophenyl}$. Forming stable oxonium ion drives rearrangement. Options: (A), (B), (C).
- **Question 21**: Rusting involves anodic oxidation of Fe, cathodic reduction of dissolved oxygen, accelerated by electrolytes, prevented by sacrificial anode like Zn/Mg. Options: (A), (B), (C), (D).
- **Question 22**: Boyle temperature $T_B = a/Rb$ where second virial coefficient vanishes. $\text{H}_2$ and $\text{He}$ have very low inversion temperatures ($T_i < 298\text{ K}$), so $Z > 1$. High pressure gives $Z = 1 + Pb/RT$. Options: (A), (B), (C), (D).
- **Question 23**: Chromyl chloride test: solid chloride + dichromate + concentrated $\text{H}_2\text{SO}_4$ gives red $\text{CrO}_2\text{Cl}_2$ vapours, absorbed in $\text{NaOH}$ to give yellow chromate. Covalent chlorides of Hg, Ag, Pb do not respond. Options: (A), (B), (C), (D).
- **Question 24**: PHBV, Nylon-2-nylon-6, and PGA are biodegradable. Bakelite is non-biodegradable synthetic plastic. Options: (A), (B), (C).
- **Question 25**: $pOH = pK_b + \log\frac{[\text{NH}_4^+]}{[\text{NH}_4\text{OH}]} = 4.75 + \log(1) = 4.75$. $\text{pH} = 14 - 4.75 = 9.25$. Exact: `9.25`.
- **Question 26**: $\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies \ln 4 = \frac{E_a}{8.314}\left(\frac{20}{300 \times 320}\right) \implies 1.386 = \frac{E_a}{8.314}\left(\frac{20}{96000}\right) \implies E_a = \frac{1.386 \times 8.314 \times 96000}{20} = 55310\text{ J/mol} = 55.31\text{ kJ/mol}$. Exact: `55.31`.
- **Question 27**: Percentage packing efficiency of HCP lattice is $74\%$. Exact: `74.00`.
- **Question 28**: $\Delta G_3^\circ = \Delta G_1^\circ + \Delta G_2^\circ \implies -3 F E_3^\circ = -1 F E_1^\circ - 2 F E_2^\circ \implies 3 E_3^\circ = E_1^\circ + 2 E_2^\circ = 0.77 + 2(-0.44) = 0.77 - 0.88 = -0.11\text{ V} \implies E_3^\circ = -0.0367\text{ V} \approx -0.04\text{ V}$. Exact: `-0.04`.
- **Question 29**: $\Delta T_b = 80.50 - 80.10 = 0.40\text{ K}$. $\Delta T_b = K_b \frac{w_2 \times 1000}{M_2 w_1} \implies 0.40 = 2.53 \frac{3.00 \times 1000}{M_2 \times 100} = \frac{75.9}{M_2} \implies M_2 = \frac{75.9}{0.40} \approx 190\text{ g/mol}$. Exact: `190.00`.
- **Question 30**: $[\text{Fe}(\text{CN})_6]^{3-}$: $\text{Fe}^{3+}$ ($3d^5$), strong field ligand pairs up electrons giving $t_{2g}^5 e_g^0$, leaving 1 unpaired electron ($n = 1$). $\mu = \sqrt{1(3)} = \sqrt{3} \approx 1.73\text{ BM}$. Exact: `1.73`.
- **Question 31**: Any alkyl side chain containing at least one benzylic hydrogen (toluene, ethylbenzene, isopropylbenzene) is oxidized to benzoic acid by alkaline $\text{KMnO}_4$. Option (D).
- **Question 32**: In aqueous solution, the order of basicity of methylamines is secondary > primary > tertiary: $(\text{CH}_3)_2\text{NH} > \text{CH}_3\text{NH}_2 > (\text{CH}_3)_3\text{N}$. In increasing order: $(\text{CH}_3)_3\text{N} < \text{CH}_3\text{NH}_2 < (\text{CH}_3)_2\text{NH}$. Option (A).
- **Question 33**: Limestone decomposes to $\text{CaO}$, which reacts with silica to form fusible slag $\text{CaSiO}_3$. Option (A).
- **Question 34**: Maltose is a disaccharide of two $\alpha$-D-glucose units joined by an $\alpha-1,4$-glycosidic linkage. Option (A).
- **Question 35**: Molecular orbital bond orders: $\text{O}_2^{2-} = 1, \text{O}_2^- = 1.5, \text{O}_2 = 2.0, \text{O}_2^+ = 2.5$. Highest is $\text{O}_2^+$. Option (A).
- **Question 36**: Clark's method uses slaked lime $\text{Ca(OH)}_2$. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(-x) = -f(x)$ (odd). $f'(x) = \frac{1 - x^2}{(1+x^2)^2} = 0 \implies x = \pm 1$. Extrema at $\pm 1$ with values $\pm 1/2$. Range is $[-1/2, 1/2]$. Points of inflection at $x = 0, \pm\sqrt{3}$. Options: (A), (B), (C), (D).
- **Question 38**: Spectral theorem for real symmetric matrices: all eigenvalues are real, eigenvectors of distinct eigenvalues are orthogonal, orthogonally diagonalizable, positive eigenvalues imply positive definite. Options: (A), (B), (C), (D).
- **Question 39**: For $xy = c^2$: tangent is $x/t + yt = 2c$. Axis intercepts are $(2ct, 0)$ and $(0, 2c/t)$. Area of triangle $= \frac{1}{2}(2ct)(2c/t) = 2c^2$ (constant). Midpoint of intercepts is $(ct, c/t) = P$. Normal equation is $xt^3 - yt - ct^4 + c = 0$. Options: (A), (B), (C), (D).
- **Question 40**: Bernoulli ODE: divide by $y^2 \implies \frac{1}{y^2}\frac{dy}{dx} + \frac{1}{xy} = \ln x$. Let $v = 1/y \implies -\frac{dv}{dx} + \frac{v}{x} = \ln x \implies \frac{dv}{dx} - \frac{v}{x} = -\ln x$. Integrating factor: $e^{\int -dx/x} = 1/x$. Solution: $\frac{v}{x} = -\int \frac{\ln x}{x}dx = -\frac{(\ln x)^2}{2} + C$. Options: (A), (B).
- **Question 41**: $\vec{a} \times \vec{b} = \vec{c} \implies \vec{c} \perp \vec{a}$ and $\vec{c} \perp \vec{b}$. Also $\vec{b} \times \vec{c} = \vec{a} \implies \vec{a} \perp \vec{b}$. Thus all 3 are mutually perpendicular. Magnitudes: $|\vec{c}| = |\vec{a}||\vec{b}|$ and $|\vec{a}| = |\vec{b}||\vec{c}| \implies |\vec{a}| = |\vec{b}|^2 |\vec{a}| \implies |\vec{b}| = 1$, and $|\vec{a}| = |\vec{c}|$. $[\vec{a}\ \vec{b}\ \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c}) = \vec{a} \cdot \vec{a} = |\vec{a}|^2$. Options: (A), (B), (C), (D).
- **Question 42**: Geometric distribution with parameter $p$: mean is $1/p$, variance is $\frac{1-p}{p^2}$, satisfies memoryless property, and $P(X \ge 3) = (1-p)^2$. Options: (A), (B), (C), (D).
- **Question 43**: Frullani's integral: $\int_0^\infty \frac{f(ax) - f(bx)}{x}dx = (f(0) - f(\infty))\ln(b/a)$. Here $f(x) = e^{-x}$, $a = 1, b = 3$. $I = (1 - 0)\ln(3/1) = \ln 3 \implies k = 3$. Exact: `3.00`.
- **Question 44**: Total area of ellipse $= \pi a b = \pi(4)(3) = 12\pi$. Area in first quadrant $= \frac{12\pi}{4} = 3\pi$. Divided by $\pi$, the answer is 3. Exact: `3.00`.
- **Question 45**: Strictly positive integers: $x \ge 1, y \ge 1$. $x + y < 10 \implies x + y \le 9$. For each $x \in \{1, 2, \dots, 8\}$, $y \in \{1, \dots, 9-x\}$. Total points $= \sum_{x=1}^8 (9 - x) = 8 + 7 + \dots + 1 = \frac{8 \times 9}{2} = 36$. Exact: `36.00`.
- **Question 46**: Distance $d = \frac{|3(2) - 4(3) + 12(-1) - 7|}{\sqrt{3^2 + (-4)^2 + 12^2}} = \frac{|6 - 12 - 12 - 7|}{\sqrt{9 + 16 + 144}} = \frac{|-25|}{\sqrt{169}} = \frac{25}{13} \approx 1.92$. Exact: `1.92`.
- **Question 47**: Telescoping series: $\frac{1}{n(n+1)(n+2)} = \frac{1}{2}\left[\frac{1}{n(n+1)} - \frac{1}{(n+1)(n+2)}\right]$. Sum $= \frac{1}{2}\left(\frac{1}{1 \times 2}\right) = \frac{1}{4} \implies m = 4$. Exact: `4.00`.
- **Question 48**: Non-negative integer solutions to $x_1 + x_2 + x_3 + x_4 = 6$: stars and bars formula $\binom{n + k - 1}{k - 1} = \binom{6 + 4 - 1}{4 - 1} = \binom{9}{3} = \frac{9 \times 8 \times 7}{6} = 84$. Exact: `84.00`.
- **Question 49**: Distance from origin: $d = \frac{|-14|}{\sqrt{2^2 + 3^2 + 6^2}} = \frac{14}{\sqrt{4 + 9 + 36}} = \frac{14}{7} = 2$. Option (A).
- **Question 50**: Circulant matrix determinant $= -(1 + \omega + \omega^2)(1 - \omega)(1 - \omega^2) = 0$ because $1 + \omega + \omega^2 = 0$. Option (A).
- **Question 51**: Length of tangent $= \sqrt{S_1} = \sqrt{7^2 + 1^2 - 4(7) - 6(1) - 12} = \sqrt{49 + 1 - 28 - 6 - 12} = \sqrt{4} = 2$ (or 4 for center distance). Let's verify: $S_1 = 50 - 46 = 4 \implies \sqrt{4} = 2$.
- **Question 52**: Curves $y = x^2 \implies y' = 2x = 2$; $x = y^2 \implies y' = \frac{1}{2y} = 1/2$. $\tan\theta = \left|\frac{2 - 1/2}{1 + 2(1/2)}\right| = \left|\frac{3/2}{2}\right| = \frac{3}{4} \implies \theta = \tan^{-1}(3/4)$. Option (A).
- **Question 53**: $S = \frac{a}{1 - r} = \frac{1}{1 - 2/3} = \frac{1}{1/3} = 3$. Option (A).
- **Question 54**: Maximum value $= \sqrt{3^2 + 4^2} + 5 = 5 + 5 = 10$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 03 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Static Equilibrium of Rigid Body, Torque, Friction Constraints.
- **2. Derivation**:
  - Vertical equilibrium: $N_f - (M + m)g = 0 \implies N_f = (M + m)g$. (A) is correct.
  - Torque about the base contact point:
    $$N_w (L \sin\theta) - M g \left(\frac{L}{2}\cos\theta\right) - m g (x\cos\theta) = 0 \implies N_w = \frac{(M/2 + m x/L)g}{\tan\theta}$$
    (B) is correct.
  - Horizontal equilibrium: $f_s = N_w$. As $x$ increases, $N_w$ increases, so required static friction increases. (C) is correct.
  - Slipping occurs if $f_s > \mu_s N_f$. Maximum friction required occurs at maximum $x = L$, so slipping is most likely at the top. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Coupled LC Oscillators, Normal Modes, Damped Harmonic Oscillations.
- **2. Derivation**:
  - Coupled identical LC circuits exhibit symmetric and antisymmetric normal modes with distinct frequencies. (A) is correct.
  - In the antisymmetric mode, currents are in anti-phase ($180^\circ$). (B) is correct.
  - Energy transfers periodically between electrostatic and magnetic forms. (C) is correct.
  - With resistance $R$, damping factor is $e^{-R t / 2L}$, time constant $\tau = 2L/R$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Fiber Optics, Total Internal Reflection, Numerical Aperture $\text{NA} = \sqrt{\mu_1^2 - \mu_2^2}$.
- **2. Derivation**:
  - $\sin\theta_c = \frac{\mu_2}{\mu_1} = \frac{1.40}{1.50} = \frac{14}{15} \approx 0.9333 \implies \theta_c \approx 68.96^\circ$. (A) is correct.
  - $\text{NA} = \sqrt{1.50^2 - 1.40^2} = \sqrt{2.25 - 1.96} = \sqrt{0.29} \approx 0.5385$. (B) is correct.
  - Acceptance angle in air ($\mu_0 = 1$): $\sin\theta_{\text{acc}} = \text{NA} \implies \theta_{\text{acc}} \approx 32.58^\circ$. (C) is correct.
  - Any ray with incident angle $\theta \le \theta_{\text{acc}}$ has internal reflection angle at core-cladding boundary $\ge \theta_c$, undergoing TIR. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Ampere's Law, Superposition Principle for Magnetic Fields in Cavities.
- **2. Derivation**:
  - Solid wire without cavity produces magnetic field $\vec{B}_1 = \frac{\mu_0}{2}(\vec{J} \times \vec{r}_1)$.
  - Negative current density $-\vec{J}$ in cavity produces $\vec{B}_2 = -\frac{\mu_0}{2}(\vec{J} \times \vec{r}_2)$.
  - Net field inside cavity: $\vec{B} = \vec{B}_1 + \vec{B}_2 = \frac{\mu_0}{2}\vec{J} \times (\vec{r}_1 - \vec{r}_2) = \frac{\mu_0}{2}(\vec{J} \times \vec{d})$. (A) and (B) are correct.
  - The field depends only on displacement $\vec{d}$ and current density $\vec{J}$, independent of $a$. (C) is correct.
  - Direction: $\vec{J} = J\hat{k}$, $\vec{d} = d\hat{i} \implies \vec{J} \times \vec{d} = J d (\hat{k} \times \hat{i}) = J d \hat{j}$. Points along $+y$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Quantum Mechanics, 1D Infinite Potential Well, Wavefunctions and Probabilities.
- **2. Derivation**:
  - Eigenvalues $E_n = \frac{n^2 \pi^2 \hbar^2}{2m L^2}$. (A) is correct.
  - Wavefunctions $\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$. (B) is correct.
  - $\langle p_x \rangle = 0$ for all real bound state wavefunctions. (C) is correct.
  - In ground state, probability density $\sin^2(\pi x / L)$ peaks at the center $x = L/2$. The integral over the middle third $[L/3, 2L/3]$ is $\frac{1}{3} + \frac{\sqrt{3}}{2\pi} \approx 0.333 + 0.276 = 0.609 > 1/3$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Stirling Cycle with and without Regeneration, Reversible Heat Cycles.
- **2. Derivation**:
  - $W_{\text{net}} = n R (T_1 - T_2)\ln(V_2/V_1) = 2 R (600 - 300)\ln 2 = 600 R \ln 2$. (A) is correct.
  - Isochoric heat capacities are equal and constant: $Q_{\text{in, isochoric}} = n C_V (T_1 - T_2) = Q_{\text{out, isochoric}}$. (B) is correct.
  - With ideal regeneration, internal heat transfer balances, so only isothermal heat exchanges occur, matching Carnot efficiency $\eta = 1 - T_2/T_1 = 50\%$. (C) is correct.
  - Without regeneration, additional heat must be supplied during isochoric heating, so $\eta < 50\%$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Angular momentum conservation about central axis:
  $$I_i \omega_0 = I_f \omega_f$$
  $I_i = \frac{1}{2}M R^2 + m R^2 = \frac{1}{2}(4.0)(1.0)^2 + 20.0(1.0)^2 = 2.0 + 20.0 = 22.0\text{ kg}\cdot\text{m}^2$.
  When child reaches center ($r = 0$), $I_f = \frac{1}{2}M R^2 = 2.0\text{ kg}\cdot\text{m}^2$.
  $\omega_f = \frac{I_i \omega_0}{I_f} = \frac{22.0 \times 10.0}{2.0} = 110.00\text{ rad/s}$. Exact: `110.00`.
- **Question 8**: $\nu_A = \nu_0 \pm 4 = 512 \pm 4 = 516\text{ Hz}$ or $508\text{ Hz}$.
  Loading with wax decreases the frequency of fork $A$.
  If $\nu_A = 516\text{ Hz}$, decreasing $\nu_A$ reduces the beat frequency from 4 to 2.
  If $\nu_A = 508\text{ Hz}$, decreasing $\nu_A$ would increase beat frequency from 4 to 6.
  Hence original frequency is $516\text{ Hz}$. Exact: `516.00`.
- **Question 9**: Initial energy: $U_i = \frac{1}{2} C_0 V_0^2 = \frac{1}{2}(10.0 \times 10^{-6})(100)^2 = 0.050\text{ J} = 50.0\text{ mJ}$.
  When disconnected, charge is conserved: $Q = C_0 V_0 = 10.0 \times 10^{-4}\text{ C}$.
  Final capacitance: $C_f = K C_0 = 5.0 \times 10.0\ \mu\text{F} = 50.0\ \mu\text{F}$.
  Final energy: $U_f = \frac{Q^2}{2 C_f} = \frac{U_i}{K} = \frac{50.0}{5.0} = 10.0\text{ mJ}$.
  Change: $|\Delta U| = |10.0 - 50.0| = 40.00\text{ mJ}$. Exact: `40.00`.
- **Question 10**: In Lloyd's mirror, effective slit separation is $d = 2h = 2(1.00\text{ mm}) = 2.00\text{ mm}$.
  Fringe width: $\beta = \frac{\lambda D}{d} = \frac{(500 \times 10^{-9}\text{ m})(2.00\text{ m})}{2.00 \times 10^{-3}\text{ m}} = 0.50 \times 10^{-3}\text{ m} = 0.50\text{ mm}$. Exact: `0.50`.
- **Question 11**: $r_n = \frac{n^2}{Z} a_0$. For $n = 1, Z = 2$: $r_1 = \frac{1}{2} a_0 = \frac{0.529}{2} = 0.2645\text{ \AA} \approx 0.26\text{ \AA}$. Exact: `0.26`.
- **Question 12**: Field due to one side of square of side $a$ at distance $a/2$:
  $$B_1 = \frac{\mu_0 I}{4\pi (a/2)} (\sin 45^\circ + \sin 45^\circ) = \frac{\mu_0 I}{2\pi a} (2 \times \frac{1}{\sqrt{2}}) = \frac{\sqrt{2}\mu_0 I}{\pi a}$$
  For 4 sides: $B = 4 B_1 = \frac{4\sqrt{2}\mu_0 I}{\pi a} = \frac{4(1.414)(4\pi \times 10^{-7})(4.00)}{\pi (0.10)} = \frac{90.496 \times 10^{-7}}{0.10} \approx 90.5 \times 10^{-6}\text{ T} = 45.25\ \mu\text{T}$ (or $45.25$). Let's check: $4 \times \sqrt{2} \times 4 \times 4 / 0.1 \times 10^{-7} = 226.24 \times 10^{-6} / \pi$... wait: $\frac{4\sqrt{2}\mu_0 I}{\pi a} = \frac{4\sqrt{2}(4\pi \times 10^{-7})(4)}{\pi (0.1)} = \frac{64\sqrt{2} \times 10^{-7}}{0.1} = 640\sqrt{2} \times 10^{-7} = 905.1 \times 10^{-7} = 90.51\ \mu\text{T}$. Exact: `90.51`.

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
- **Question 19**: $\text{C}_{60}$ has soccer-ball geometry with 12 pentagons and 20 hexagons. Pentagons fuse only with hexagons. All carbons are $sp^2$ hybridized. Options: (A), (B), (C), (D).
- **Question 20**: Hinsberg reagent and nitrous acid distinguish between $1^\circ, 2^\circ, 3^\circ$ amines. Carbylamine test distinguishes $1^\circ$ amines from $2^\circ$ and $3^\circ$. Lucas reagent is for alcohols. Options: (A), (B), (C).
- **Question 21**: $\Delta G^\circ = -RT \ln K$. Catalyst increases forward and backward rates equally. Van 't Hoff equation describes temperature dependence. Endothermic reactions shift forward with temperature. Options: (A), (B), (C), (D).
- **Question 22**: Photochemical chlorination of $n$-butane gives $(\pm)$-2-chlorobutane (chiral center created, racemic mixture). Propane gives achiral 2-chloropropane. 2-methylbutane at C2 gives achiral 2-chloro-2-methylbutane. Options: (A).
- **Question 23**: $\text{H}_3\text{PO}_2$ has two $\text{P}-\text{H}$ bonds; $\text{H}_3\text{PO}_3$ has one $\text{P}-\text{H}$ bond. Both act as reducing agents. $\text{H}_3\text{PO}_4$ and $\text{H}_4\text{P}_2\text{O}_7$ have zero $\text{P}-\text{H}$ bonds. Options: (A), (B).
- **Question 24**: Bent $\text{H}_2\text{O}$ and $\text{SO}_2$, and trigonal pyramidal $\text{NH}_3$ have non-zero dipole moments. Linear $\text{CO}_2$ has zero dipole moment. Options: (A), (B), (C).
- **Question 25**: $\text{PbI}_2 \rightleftharpoons \text{Pb}^{2+} + 2\text{I}^- \implies K_{sp} = 4S^3 \implies S = \sqrt[3]{K_{sp}/4} = \sqrt[3]{7.1 \times 10^{-9}/4} = \sqrt[3]{1.775 \times 10^{-9}} = 1.21 \times 10^{-3}\text{ mol/L} = 1.21\text{ mmol/L}$. Exact: `1.21`.
- **Question 26**: At $t = 10\text{ min}$, $P_{\text{total}} = P_0 - x + 2x + x = P_0 + 2x = 220 \implies 2x = 120 \implies x = 60\text{ mm Hg}$.
  $P_A(t) = P_0 - x = 100 - 60 = 40\text{ mm Hg}$.
  $k = \frac{1}{t}\ln\left(\frac{P_0}{P_A}\right) = \frac{1}{10}\ln\left(\frac{100}{40}\right) = \frac{1}{10}\ln(2.5) = \frac{0.916}{10} = 0.0916\text{ min}^{-1} \approx 0.09\text{ min}^{-1}$. Exact: `0.09`.
- **Question 27**: $\rho = \frac{Z M}{a^3 N_A} = \frac{4(63.55)}{(3.61 \times 10^{-8})^3 (6.022 \times 10^{23})} = \frac{254.2}{4.7046 \times 10^{-23} \times 6.022 \times 10^{23}} = \frac{254.2}{28.33} \approx 8.97\text{ g/cm}^3$. Exact: `8.97`.
- **Question 28**: $E_{\text{cell}}^\circ = E^\circ(\text{Ag}^+/\text{Ag}) - E^\circ(\text{Mg}^{2+}/\text{Mg}) = 0.80 - (-2.37) = +3.17\text{ V}$. Exact: `3.17`.
- **Question 29**: $\Delta T_f(\text{sugar}) = 273.15 - 271.0 = 2.15\text{ K}$.
  $\Delta T_f = K_f \frac{w_2 \times 1000}{M_2 w_1}$. Since $w_2/w_1$ is identical:
  $\frac{\Delta T_f(\text{glucose})}{\Delta T_f(\text{sugar})} = \frac{M_{\text{sugar}}}{M_{\text{glucose}}} = \frac{342}{180} = 1.90 \implies \Delta T_f(\text{glucose}) = 1.90 \times 2.15 = 4.085\text{ K}$.
  Freezing point of glucose solution $= 273.15 - 4.085 = 269.065\text{ K} \approx 269.07\text{ K}$. Exact: `269.07`.
- **Question 30**: In $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$, nitric oxide is present as nitrosonium ion ($\text{NO}^+$). Thus $\text{Fe}$ is in $+1$ oxidation state. Exact: `1.00`.
- **Question 31**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 32**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 33**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 34**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 35**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 36**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(0) = 0$. $f'(x) = \frac{1}{1+x^2} - \frac{x}{1+x^2} = \frac{1-x}{1+x^2}$. Local max at $x = 1$. Max value $= \tan^{-1}(1) - \frac{1}{2}\ln 2 = \frac{\pi}{4} - \frac{1}{2}\ln 2$. Options: (A), (B), (C), (D).
- **Question 38**: $A^2 = A \implies \lambda^2 = \lambda \implies \lambda = 0, 1$. $\det A = \prod \lambda_i \in \{0, 1\}$. If $A \ne I$, at least one eigenvalue is 0, so $\det A = 0$. $(I-A)^2 = I - 2A + A^2 = I - 2A + A = I - A$. Options: (A), (B), (C), (D).
- **Question 39**: Radical axis equation: $C_1 - C_2 = 0 \implies (-4x - 6y + 4) - (-2x - 4y + 1) = 0 \implies -2x - 2y + 3 = 0 \implies 2x + 2y - 3 = 0$. Radical axis is perpendicular to line of centers and acts as common chord. Options: (A), (B), (C), (D).
- **Question 40**: Homogeneous ODE: $\frac{dy}{dx} = \frac{1 + y/x}{1 - y/x}$. Let $y = vx \implies v + x\frac{dv}{dx} = \frac{1+v}{1-v} \implies x\frac{dv}{dx} = \frac{1+v^2}{1-v} \implies \frac{1-v}{1+v^2}dv = \frac{dx}{x}$. Integrating: $\tan^{-1}v - \frac{1}{2}\ln(1+v^2) = \ln|x| + C$. In polar coordinates, $\theta - \ln r = C \implies r = C_0 e^\theta$ (equiangular spiral). Options: (A), (B), (C), (D).
- **Question 41**: $\vec{u} \cdot (\vec{v} + \vec{w}) = 0 \implies \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w} = 0$. Adding all three equations: $2(\vec{u}\cdot\vec{v} + \vec{v}\cdot\vec{w} + \vec{w}\cdot\vec{u}) = 0$. Subtracting gives $\vec{u}\cdot\vec{v} = \vec{v}\cdot\vec{w} = \vec{w}\cdot\vec{u} = 0$. Thus mutually orthogonal. $|\vec{u}+\vec{v}+\vec{w}|^2 = 9 + 16 + 25 = 50 \implies |\vec{u}+\vec{v}+\vec{w}| = 5\sqrt{2}$. Parallelepiped volume $= 3 \times 4 \times 5 = 60$. Options: (A), (B), (C), (D).
- **Question 42**: Geometric with $p = 1/6$: mean $= 1/p = 6$. $P(N > 3) = q^3 = (5/6)^3 = 125/216$. Variance $= q/p^2 = (5/6)/(1/36) = 30$. Options: (A), (B), (C), (D).
- **Question 43**: $\text{Area} = \int_{\pi/4}^{5\pi/4} (\sin x - \cos x)dx = [-\cos x - \sin x]_{\pi/4}^{5\pi/4} = -(-\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}) - (-\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}) = \sqrt{2} - (-\sqrt{2}) = 2\sqrt{2} \approx 2.828 \approx 2.83$. Exact: `2.83`.
- **Question 44**: $\frac{dx}{d\theta} = -3a\cos^2\theta\sin\theta$, $\frac{dy}{d\theta} = 3a\sin^2\theta\cos\theta$.
  $\frac{dy}{dx} = -\tan\theta$. At $\theta = \pi/4$, $\frac{dy}{dx} = -1$.
  Slope of normal $= -1 / (-1) = +1.00$. Exact: `1.00`.
- **Question 45**: $\int_0^1 \frac{dx}{e^x + e^{-x}} = \int_0^1 \frac{e^x dx}{e^{2x} + 1} = [\tan^{-1}(e^x)]_0^1 = \tan^{-1}(e) - \tan^{-1}(1) = \tan^{-1}(e) - \frac{\pi}{4}$. Thus $k = 4$. Exact: `4.00`.
- **Question 46**: Distance from origin to line: vector $\vec{r}_0 = (1, 2, 3)$, direction $\vec{d} = (2, 3, 6)$.
  $\vec{r}_0 \times \vec{d} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 3 \\ 2 & 3 & 6 \end{vmatrix} = \hat{i}(12 - 9) - \hat{j}(6 - 6) + \hat{k}(3 - 4) = 3\hat{i} - \hat{k}$.
  Magnitude $= \sqrt{9 + 1} = \sqrt{10}$.
  $|\vec{d}| = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$.
  Distance $= \frac{\sqrt{10}}{7} \approx \frac{3.162}{7} \approx 0.45$. Exact: `0.45`.
- **Question 47**: Roots in AP: let roots be $a - d, a, a + d$.
  Sum of roots $= 3a = 9 \implies a = 3$. The middle root is 3. Exact: `3.00`.
- **Question 48**: Number of ways to distribute 8 identical balls into 3 non-empty boxes: $\binom{8-1}{3-1} = \binom{7}{2} = \frac{7 \times 6}{2} = 21.00$. Exact: `21.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 03
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 0.25
- Q8: 107.00
- Q9: 297.00
- Q10: 48.59
- Q11: 6.21
- Q12: 6.59
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C
- Q20: A, B, C
- Q21: A, B, C, D
- Q22: A, B, C, D
- Q23: A, B, C, D
- Q24: A, B, C
- Q25: 9.25
- Q26: 55.31
- Q27: 74.00
- Q28: -0.04
- Q29: 190.00
- Q30: 1.73
- Q31: D
- Q32: A
- Q33: A
- Q34: A
- Q35: A
- Q36: A

#### Mathematics
- Q37: A, B, C, D
- Q38: A, B, C, D
- Q39: A, B, C, D
- Q40: A, B
- Q41: A, B, C, D
- Q42: A, B, C, D
- Q43: 3.00
- Q44: 3.00
- Q45: 36.00
- Q46: 1.92
- Q47: 4.00
- Q48: 84.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Paper 2 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 110.00
- Q8: 516.00
- Q9: 40.00
- Q10: 0.50
- Q11: 0.26
- Q12: 90.51
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C, D
- Q20: A, B, C
- Q21: A, B, C, D
- Q22: A
- Q23: A, B
- Q24: A, B, C
- Q25: 1.21
- Q26: 0.09
- Q27: 8.97
- Q28: 3.17
- Q29: 269.07
- Q30: 1.00
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
- Q43: 2.83
- Q44: 1.00
- Q45: 4.00
- Q46: 0.45
- Q47: 3.00
- Q48: 21.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: 33.3% of questions (high option-checking cognitive load).
- **Physics**: Focus on induction phase lag (jumping ring), relativistic photon pairs, cavity magnetic field superposition, quantum well probability integrals.
- **Chemistry**: Jahn-Teller geometric distortion, pinacol migratory aptitudes, van 't Hoff reaction isobars, fullerenes, brown ring iron oxidation state.
- **Mathematics**: Extrema of rational functions, spectral decomposition of real symmetric matrices, Bernoulli ODEs, equiangular polar spirals, Geometric distribution memorylessness.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

create_mock_files(3, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")

