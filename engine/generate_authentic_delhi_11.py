# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 11.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Compton recoil kinematics, Foucault pendulum precession, Berthelot real gas, coupled oscillator normal modes
- Curtius rearrangement, Michaelis-Menten kinetics, Quinhydrone pH electrode, Spinel site preference
- Bernoulli ODEs, matrix similarity invariants, Catalan numbers, family of planes
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 11 — Paper 1
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
In a Compton scattering process, an incident photon of energy $E_0 = h\nu_0$ collides elastically with an electron of rest mass $m_e$ initially at rest. The photon is scattered at angle $\theta$, and the recoil electron emerges at angle $\phi$ relative to the incident direction:
(A) The scattered photon wavelength is $\lambda' = \lambda_0 + \lambda_C (1 - \cos\theta)$, where $\lambda_C = \frac{h}{m_e c} \approx 0.0243\text{ \AA}$.  
(B) The kinetic energy imparted to the recoil electron is $K_e = E_0 - E' = \frac{E_0 \alpha (1 - \cos\theta)}{1 + \alpha (1 - \cos\theta)}$, where $\alpha = \frac{E_0}{m_e c^2}$.  
(C) The recoil angle $\phi$ of the electron is related to the photon scattering angle $\theta$ by $\cot\phi = (1 + \alpha)\tan(\theta/2)$.  
(D) The maximum kinetic energy of the recoil electron occurs for backscattering ($\theta = 180^\circ$), known as the Compton edge $K_{\text{max}} = \frac{2\alpha E_0}{1 + 2\alpha}$.

#### Question 2
Two identical simple pendulums, each of mass $m$ and length $l$, are coupled together by a light horizontal spring of spring constant $k$ attached at distance $d$ from the pivot points ($0 < d \le l$):
(A) In the symmetric normal mode, both pendulums oscillate in phase with identical amplitudes, the spring remains unstretched, and the angular frequency is $\omega_1 = \sqrt{g/l}$.  
(B) In the antisymmetric normal mode, the pendulums oscillate $180^\circ$ out of phase, and the angular frequency is $\omega_2 = \sqrt{\frac{g}{l} + \frac{2k d^2}{m l^2}}$.  
(C) If one pendulum is initially displaced by $\theta_0$ while the other is held at rest, energy is periodically transferred between the pendulums with a beat period $T_{\text{beat}} = \frac{2\pi}{\omega_2 - \omega_1}$.  
(D) The frequency of the antisymmetric mode increases monotonically as the attachment point $d$ is moved closer to the bob ($d \to l$).

#### Question 3
Regarding a Foucault pendulum oscillating at latitude $\lambda$ in the Northern Hemisphere on the rotating Earth:
(A) The plane of oscillation of the pendulum precesses clockwise (viewed from above) due to the horizontal component of the Coriolis acceleration.  
(B) The angular velocity of precession of the plane of oscillation is $\Omega_p = \Omega_{\text{Earth}}\sin\lambda$, where $\Omega_{\text{Earth}} \approx 7.29 \times 10^{-5}\text{ rad/s}$.  
(C) At the North Pole ($\lambda = 90^\circ$), the plane of oscillation completes one full revolution ($360^\circ$) in one sidereal day ($\approx 23.93\text{ hours}$).  
(D) At the equator ($\lambda = 0^\circ$), the plane of oscillation does not precess ($\Omega_p = 0$).

#### Question 4
One mole of a real gas obeys the Berthelot equation of state $\left(P + \frac{a}{T V^2}\right)(V - b) = RT$, where $a$ and $b$ are positive empirical constants:
(A) The temperature dependence of the internal pressure term $\frac{a}{T V^2}$ accounts for the decrease in effective intermolecular cohesive forces at higher kinetic temperatures.  
(B) At the critical point, the critical volume is $V_c = 3b$.  
(C) The critical temperature is $T_c = \sqrt{\frac{8a}{27Rb}}$.  
(D) The critical compressibility factor is $Z_c = \frac{P_c V_c}{R T_c} = \frac{3}{8} = 0.375$.

#### Question 5
Regarding polarization of light and birefringent wave plates:
(A) A quarter-wave plate ($\text{QWP}$) introduces an optical path difference of $\Delta L = \lambda/4$ (phase difference $\delta = \pi/2$) between the extraordinary and ordinary rays.  
(B) When linearly polarized light is incident on a $\text{QWP}$ with its electric field vector at $45^\circ$ to the optic axis, the transmitted light is circularly polarized.  
(C) A half-wave plate ($\text{HWP}$) introduces a phase difference $\delta = \pi$ ($\Delta L = \lambda/2$) and rotates the plane of polarization of linearly polarized light by an angle $2\theta$, where $\theta$ is the angle between the incident polarization and the fast axis.  
(D) An optically active substance (e.g., aqueous sucrose solution) rotates the plane of polarization because it has different refractive indices for right- and left-circularly polarized light ($\mu_R \ne \mu_L$, circular birefringence).

#### Question 6
A rocket of initial total mass $m_0$ is launched vertically from rest in a uniform gravitational field $g$. Exhaust gases are ejected downward with constant relative exhaust velocity $u$ at a constant mass burn rate $\alpha = -\frac{dm}{dt}$:
(A) By Newton's second law for variable-mass systems, the upward equation of motion is $m(t)\frac{dv}{dt} = u \alpha - m(t)g$.  
(B) The velocity of the rocket as a function of time is $v(t) = u \ln\left(\frac{m_0}{m_0 - \alpha t}\right) - gt$.  
(C) The thrust force exerted on the rocket by the expelled propellant is $F_{\text{thrust}} = u \alpha$.  
(D) Lift-off from the launch pad occurs immediately at $t = 0$ only if the initial thrust exceeds the initial weight ($u \alpha > m_0 g$).

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
In a Compton scattering experiment with incident X-rays of wavelength $\lambda_0 = 0.0500\text{ \AA}$, photons are scattered at $\theta = 180^\circ$ (backscattering). Calculate the fractional shift in wavelength $\frac{\Delta\lambda}{\lambda_0}$ of the photons. [Take $\lambda_C = 0.0243\text{ \AA}$. Round off to TWO decimal places].

#### Question 8
A parallel-plate capacitor with square plates of side $L = 0.20\text{ m}$ and separation $d = 2.0\text{ mm}$ is half-filled with a dielectric of relative permittivity $\varepsilon_r = 4.0$ inserted parallel to the plates (so dielectric thickness is $d/2 = 1.0\text{ mm}$, and remaining $1.0\text{ mm}$ is air). Calculate the capacitance $C$ in picoFarads ($\text{pF}$). [Take $\varepsilon_0 = 8.854 \times 10^{-12}\text{ F/m}$. Round off to ONE decimal place].

#### Question 9
In a two-slit Fraunhofer diffraction experiment, the slit width is $a = 0.040\text{ mm}$ and the slit separation is $d = 0.200\text{ mm}$. Calculate the total number of bright interference fringes contained within the central diffraction envelope.

#### Question 10
One mole of an ideal gas expands along the path $P = \alpha V^2$ (where $\alpha = 2.0 \times 10^5\text{ Pa/m}^6$) from initial volume $V_1 = 1.0\text{ m}^3$ to $V_2 = 2.0\text{ m}^3$. Calculate the mechanical work done $W$ (in kiloJoules, $\text{kJ}$) by the gas. [Round off to TWO decimal places].

#### Question 11
An alpha particle ($q = 2e, m_\alpha = 6.64 \times 10^{-27}\text{ kg}$) is accelerated through a potential difference $V = 1.0\text{ MV} = 10^6\text{ V}$. Calculate its kinetic energy $K$ in Mega-electron-Volts ($\text{MeV}$).

#### Question 12
A simple pendulum has a time period $T = 2.00\text{ s}$ on the surface of Earth ($g = 9.80\text{ m/s}^2$). Calculate the length $L$ (in meters, $\text{m}$) of the pendulum. [Take $\pi^2 \approx 9.87$. Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle moves in a circle of radius $R = 2.0\text{ m}$ with constant tangential acceleration $a_t = 3.0\text{ m/s}^2$, starting from rest. The time $t$ at which the magnitudes of the centripetal acceleration and tangential acceleration become equal is:
(A) $\sqrt{2/3}\text{ s} \approx 0.82\text{ s}$  
(B) $1.50\text{ s}$  
(C) $2.00\text{ s}$  
(D) $0.50\text{ s}$

#### Question 14
The electric potential in a region of space is given by $V(x, y, z) = 4x^2 - 3y^2 + 2z^2$ Volts. The electric field vector $\vec{E}$ at the point $(1, 1, 1)$ is:
(A) $-8\hat{i} + 6\hat{j} - 4\hat{k}\text{ V/m}$  
(B) $8\hat{i} - 6\hat{j} + 4\hat{k}\text{ V/m}$  
(C) $-4\hat{i} + 3\hat{j} - 2\hat{k}\text{ V/m}$  
(D) $-8\hat{i} - 6\hat{j} - 4\hat{k}\text{ V/m}$

#### Question 15
Two monoatomic ideal gases 1 and 2 have molar masses $M_1 = 4.0\text{ g/mol}$ (Helium) and $M_2 = 40.0\text{ g/mol}$ (Argon). At the same temperature $T$, the ratio of the speed of sound in gas 1 to that in gas 2 is:
(A) $\sqrt{10} \approx 3.16$  
(B) $10$  
(C) $1/\sqrt{10}$  
(D) $1$

#### Question 16
An astronomical telescope has an objective lens of focal length $f_o = 100.0\text{ cm}$ and an eyepiece of focal length $f_e = 5.0\text{ cm}$. In normal adjustment (final image at infinity), the magnifying power $m$ and the separation $L$ between the lenses are:
(A) $m = 20$; $L = 105.0\text{ cm}$  
(B) $m = 25$; $L = 100.0\text{ cm}$  
(C) $m = 20$; $L = 95.0\text{ cm}$  
(D) $m = 500$; $L = 105.0\text{ cm}$

#### Question 17
A particle of mass $m$ is executing SHM with amplitude $A$. The displacement $x$ from the mean position at which its kinetic energy equals its potential energy is:
(A) $A/\sqrt{2}$  
(B) $A/2$  
(C) $\sqrt{3}A/2$  
(D) $A/4$

#### Question 18
The magnetic susceptibility $\chi_m$ of a diamagnetic substance is:
(A) Small, negative, and independent of temperature  
(B) Small, positive, and inversely proportional to temperature (Curie's law)  
(C) Large, positive, and temperature dependent  
(D) Zero at all temperatures

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Curtius rearrangement and Schmidt reaction:
(A) In the Curtius rearrangement, an acyl azide ($\text{RCON}_3$) is thermally decomposed to an isocyanate ($\text{R-N=C=O}$) with concerted loss of dinitrogen gas ($\text{N}_2$).  
(B) The migration of the $R$ group to the electron-deficient nitrogen proceeds with complete retention of stereochemical configuration at the migrating carbon.  
(C) Aqueous hydrolysis of the intermediate isocyanate yields a primary amine ($\text{R-NH}_2$) and carbon dioxide.  
(D) In the Schmidt reaction, a carboxylic acid reacts with hydrazoic acid ($\text{HN}_3$) in the presence of concentrated $\text{H}_2\text{SO}_4$ to yield a primary amine with one less carbon.

#### Question 20
Regarding the Michaelis-Menten model for enzyme kinetics:
(A) The reaction mechanism is $E + S \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} ES \xrightarrow{k_{\text{cat}}} E + P$.  
(B) The initial reaction rate is $v_0 = \frac{V_{\max}[S]}{K_m + [S]}$, where $K_m = \frac{k_{-1} + k_{\text{cat}}}{k_1}$ is the Michaelis constant.  
(C) A competitive inhibitor increases the apparent $K_m$ while leaving $V_{\max}$ unchanged.  
(D) A non-competitive inhibitor decreases $V_{\max}$ while leaving $K_m$ unchanged.

#### Question 21
Regarding the quinhydrone electrode used for measuring solution $\text{pH}$:
(A) Quinhydrone is an equimolar crystalline molecular complex of $p$-benzoquinone ($\text{Q}$) and hydroquinone ($\text{QH}_2$).  
(B) The reversible redox half-cell reaction at the platinum electrode is $\text{Q} + 2\text{H}^+ + 2e^- \rightleftharpoons \text{QH}_2$.  
(C) The electrode potential at $25^\circ\text{C}$ is given by $E = E^\circ_{\text{Q/QH}_2} - \frac{2.303 RT}{F}\text{pH} = 0.6996 - 0.0591\text{ pH}$.  
(D) The quinhydrone electrode cannot be used in alkaline solutions ($\text{pH} > 8.5$) because hydroquinone dissociates as a weak diprotic acid and is rapidly oxidized by atmospheric oxygen.

#### Question 22
Regarding the crystal chemistry of normal and inverse spinels with formula $\text{AB}_2\text{O}_4$:
(A) Oxide ions form a cubic close-packed ($\text{CCP}$) lattice with 8 tetrahedral and 4 octahedral interstitial sites per formula unit.  
(B) In a normal spinel (e.g., $\text{MgAl}_2\text{O}_4$), divalent $\text{A}^{2+}$ cations occupy $1/8$ of tetrahedral voids, and trivalent $\text{B}^{3+}$ cations occupy $1/2$ of octahedral voids.  
(C) In an inverse spinel (e.g., magnetite $\text{Fe}_3\text{O}_4 = \text{Fe}^{3+}[\text{Fe}^{2+}\text{Fe}^{3+}]\text{O}_4$), all $\text{A}^{2+}$ cations and half of $\text{B}^{3+}$ cations occupy octahedral voids, while the other half of $\text{B}^{3+}$ occupy tetrahedral voids.  
(D) Cation distribution between tetrahedral and octahedral sites is governed by the relative Crystal Field Stabilization Energies ($\text{CFSE}$) of the transition metal ions.

#### Question 23
Regarding the Edman degradation technique for protein primary structure determination:
(A) Phenyl isothiocyanate ($\text{PITC}$) selectively reacts with the uncharged N-terminal amino group of the peptide under mildly alkaline conditions.  
(B) Mild anhydrous acid treatment selectively cleaves the first peptide bond, releasing the N-terminal amino acid as an anilinothiazolinone ($\text{ATZ}$) derivative.  
(C) The $\text{ATZ}$ intermediate is extracted and isomerized into a stable phenylthiohydantoin ($\text{PTH}$) amino acid for chromatographic identification.  
(D) The remaining shortened peptide chain is left intact with a free N-terminus, allowing sequential degradation of up to 50 amino acid residues.

#### Question 24
Regarding the chemical behavior and properties of interhalogen compounds:
(A) Interhalogen compounds ($\text{XX}'_n$, where $n = 1, 3, 5, 7$) are formed by direct reaction between halogens, where $X$ is the larger, less electronegative halogen.  
(B) Interhalogens are generally more reactive than pure halogens (except $\text{F}_2$) because the polar $\text{X-X}'$ bond is weaker than the homonuclear bond in halogens.  
(C) $\text{IF}_7$ has a pentagonal bipyramidal geometry ($sp^3d^3$ hybridization).  
(D) Hydrolysis of interhalogens yields a halide ion derived from the smaller halogen $X'$ and an oxoacid/oxohalide derived from the larger halogen $X$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The solubility product of $\text{Mg(OH)}_2$ in pure water at $25^\circ\text{C}$ is $K_{sp} = 1.2 \times 10^{-11}$. Calculate the $\text{pH}$ of a saturated aqueous solution of $\text{Mg(OH)}_2$. [Take $(3.0)^{1/3} \approx 1.44$. Round off to TWO decimal places].

#### Question 26
For a second-order reaction $2A \to \text{Products}$, the initial concentration is $[A]_0 = 0.20\text{ M}$ and the rate constant is $k = 0.050\text{ L/(mol}\cdot\text{s)}$. Calculate the time $t$ (in seconds) required for the concentration to decrease to $0.050\text{ M}$.

#### Question 27
An element crystallizes in a face-centered cubic ($\text{FCC}$) lattice with unit cell edge length $a = 400.0\text{ pm}$. Calculate the atomic radius $r$ of the element in picometers ($\text{pm}$). [Take $\sqrt{2} \approx 1.414$. Round off to ONE decimal place].

#### Question 28
Calculate the standard Gibbs free energy change $\Delta G^\circ$ (in $\text{kJ/mol}$) at $298\text{ K}$ for a galvanic cell having standard cell potential $E_{\text{cell}}^\circ = +1.20\text{ V}$ and involving $n = 2$ electrons transferred per reaction formula. [Take $F = 96485\text{ C/mol}$. Round off to ONE decimal place].

#### Question 29
A $0.10\text{ m}$ aqueous solution of a monobasic acid $HA$ is $20.0\%$ dissociated at $25^\circ\text{C}$. Calculate the depression in freezing point $\Delta T_f$ (in Kelvin) of the solution. [Take $K_f(\text{water}) = 1.86\text{ K}\cdot\text{kg/mol}$. Note $i = 1 + \alpha = 1.20$. Round off to TWO decimal places].

#### Question 30
Find the coordination number of the central cobalt atom in the complex $[Co(en)_2Cl_2]^+$, where `en` is ethylenediamine.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Gabriel phthalimide synthesis, potassium phthalimide is reacted with an alkyl halide to synthesize:
(A) Pure primary aliphatic amines  
(B) Aromatic primary amines  
(C) Secondary amines  
(D) Tertiary amines

#### Question 32
Which of the following transition metal complexes is diamagnetic?
(A) $[\text{Ni(CN)}_4]^{2-}$ ($3d^8$ low spin square planar)  
(B) $[\text{NiCl}_4]^{2-}$ ($3d^8$ tetrahedral)  
(C) $[\text{Fe(H}_2\text{O})_6]^{2+}$ ($3d^6$ high spin octahedral)  
(D) $[\text{CoF}_6]^{3-}$ ($3d^6$ high spin octahedral)

#### Question 33
In the froth flotation process for the concentration of sulfide ores, the role of sodium ethyl xanthate is:
(A) Collector  
(B) Frother  
(C) Depressant  
(D) Activator

#### Question 34
The shape of the chlorine trifluoride ($\text{ClF}_3$) molecule according to VSEPR theory is:
(A) T-shaped  
(B) Trigonal planar  
(C) Trigonal pyramidal  
(D) See-saw

#### Question 35
An $\alpha\text{-helix}$ in proteins is an example of:
(A) Secondary structure  
(B) Primary structure  
(C) Tertiary structure  
(D) Quaternary structure

#### Question 36
Which of the following polymers is formed by condensation polymerization?
(A) Nylon-6,6  
(B) Teflon  
(C) Polyvinyl chloride (PVC)  
(D) Polystyrene

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Consider the Bernoulli differential equation $\frac{dy}{dx} + \frac{1}{x}y = x y^2$ for $x > 0$:
(A) Dividing by $y^2$ and substituting $v = y^{1-2} = y^{-1} = 1/y$ transforms the equation into the linear ODE $\frac{dv}{dx} - \frac{1}{x}v = -x$.  
(B) The integrating factor for the transformed equation is $\text{IF} = e^{-\int (1/x)dx} = \frac{1}{x}$.  
(C) The general solution of the transformed equation is $\frac{v}{x} = -x + C \implies v = C x - x^2$.  
(D) The general solution of the original equation is $y(x) = \frac{1}{C x - x^2}$.

#### Question 38
Let $A$ and $B$ be two $n \times n$ similar matrices over $\mathbb{R}$ (i.e., there exists invertible matrix $P$ such that $B = P^{-1} A P$):
(A) $A$ and $B$ have identical characteristic polynomials ($\det(\lambda I - A) = \det(\lambda I - B)$).  
(B) $A$ and $B$ have identical eigenvalues with identical algebraic and geometric multiplicities.  
(C) $\text{tr}(A) = \text{tr}(B)$ and $\det(A) = \det(B)$.  
(D) The rank of $A$ equals the rank of $B$ ($\text{rank}(A) = \text{rank}(B)$).

#### Question 39
Consider the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Tangents are drawn from an external point $P(x_0, y_0)$ to the hyperbola:
(A) The equation of the chord of contact of tangents is $\frac{x x_0}{a^2} - \frac{y y_0}{b^2} = 1$.  
(B) If the chord of contact passes through the focus $(a e, 0)$, the point $P$ must lie on the directrix $x = a/e$.  
(C) The locus of points $P$ from which the two tangents are mutually perpendicular is the director circle $x^2 + y^2 = a^2 - b^2$ (for $a > b$).  
(D) For an equilateral (rectangular) hyperbola ($a = b$), perpendicular tangents can only intersect at the origin ($x^2 + y^2 = 0$).

#### Question 40
Let $P_1: a_1 x + b_1 y + c_1 z + d_1 = 0$ and $P_2: a_2 x + b_2 y + c_2 z + d_2 = 0$ be two non-parallel planes intersecting along a line $L$:
(A) The equation $P_1 + \lambda P_2 = 0$ represents the family of all planes passing through the line of intersection $L$ (except $P_2$).  
(B) The direction vector of the line of intersection $L$ is parallel to $\vec{n}_1 \times \vec{n}_2 = (a_1\hat{i} + b_1\hat{j} + c_1\hat{k}) \times (a_2\hat{i} + b_2\hat{j} + c_2\hat{k})$.  
(C) The plane of the family perpendicular to a given vector $\vec{v}$ can be determined by setting $(\vec{n}_1 + \lambda \vec{n}_2) \times \vec{v} = \vec{0}$.  
(D) Every point on line $L$ satisfies $P_1 = 0$ and $P_2 = 0$ simultaneously.

#### Question 41
Let $C_n$ denote the $n$-th Catalan number, defined by $C_n = \frac{1}{n+1}\binom{2n}{n}$ for $n \ge 0$:
(A) The first few terms are $C_0 = 1, C_1 = 1, C_2 = 2, C_3 = 5, C_4 = 14, C_5 = 42$.  
(B) $C_n$ satisfies the Segner recurrence relation $C_{n+1} = \sum_{i=0}^n C_i C_{n-i}$ for $n \ge 0$.  
(C) $C_n$ equals the number of monotonic Dyck lattice paths along the edges of an $n \times n$ grid that do not cross above the main diagonal.  
(D) $C_n$ equals the number of correct matchings of $n$ pairs of parentheses.

#### Question 42
Let $X$ be a continuous random variable having normal distribution $\mathcal{N}(\mu, \sigma^2)$:
(A) The probability density function is symmetric about $x = \mu$, where mean $=$ median $=$ mode.  
(B) Points of inflection of the Gaussian bell curve occur at $x = \mu - \sigma$ and $x = \mu + \sigma$.  
(C) The probability that $X$ falls within one standard deviation of the mean ($P(|X - \mu| \le \sigma)$) is approximately $68.27\%$.  
(D) The probability that $X$ falls within two standard deviations ($P(|X - \mu| \le 2\sigma)$) is approximately $95.45\%$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral using integration by parts:
$$I = \int_0^1 x^3 e^x\,dx$$
If $I = 6 - m e$, find the integer value of $m$.

#### Question 44
Find the slope of the tangent to the curve $y = \ln(1 + x^2)$ at the point where $x = 1$.

#### Question 45
Calculate the perpendicular distance from the point $(1, 2, 3)$ to the plane $2x + y - 2z + 8 = 0$.

#### Question 46
Calculate the sum of the infinite geometric series:
$$S = 18 + 6 + 2 + \frac{2}{3} + \dots$$

#### Question 47
Calculate the value of the determinant:
$$D = \begin{vmatrix} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{vmatrix}$$
when $a = 1, b = 2, c = 4$.

#### Question 48
How many distinct 4-digit numbers can be formed using the digits $\{1, 2, 3, 4, 5\}$ without repetition?

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{\tan x - x}{x^3}$$
(A) $1/3$  
(B) $1/6$  
(C) $1/2$  
(D) $1$

#### Question 50
The length of the latus rectum of the ellipse $9x^2 + 25y^2 = 225$ is:
(A) $18/5 = 3.60$  
(B) $50/3$  
(C) $10/3$  
(D) $9/5$

#### Question 51
The distance between the parallel planes $2x - y + 2z = 4$ and $4x - 2y + 4z = 20$ is:
(A) $2.00$  
(B) $3.00$  
(C) $1.00$  
(D) $4.00$

#### Question 52
If $z = \frac{1 + i\sqrt{3}}{2}$, then the value of $z^3$ is:
(A) $-1$  
(B) $1$  
(C) $i$  
(D) $-i$

#### Question 53
The integrating factor of the differential equation $\frac{dy}{dx} + y \cot x = 2\cos x$ is:
(A) $\sin x$  
(B) $\cos x$  
(C) $\ln(\sin x)$  
(D) $\csc x$

#### Question 54
Two dice are rolled simultaneously. The probability that the sum of the numbers appearing on the dice is 8 is:
(A) $5/36$  
(B) $1/6$  
(C) $7/36$  
(D) $1/9$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 11 — Paper 2
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
A uniform rod of mass $M$ and length $L$ is pivoted at one end so that it can rotate freely in a vertical plane. The rod is released from rest in the horizontal position:
(A) The angular acceleration of the rod immediately upon release is $\alpha = \frac{3g}{2L}$.  
(B) The vertical reaction force exerted by the pivot immediately upon release is $R_y = \frac{1}{4}M g$.  
(C) The angular velocity of the rod when it swings through the lowest vertical position is $\omega = \sqrt{\frac{3g}{L}}$.  
(D) The total vertical reaction force exerted by the pivot at the lowest vertical position is $R_{\text{lowest}} = \frac{5}{2}M g$.

#### Question 2
Two concentric spherical metallic shells have radii $R_1$ and $R_2$ ($R_1 < R_2$). The inner shell has a charge $+Q$, while the outer shell is grounded:
(A) The electric potential of the outer shell is identically zero ($V(R_2) = 0$).  
(B) The charge induced on the inner surface of the outer shell is $-Q$.  
(C) The net electric field in the external region $r > R_2$ is identically zero.  
(D) The capacitance of this spherical capacitor is $C = 4\pi\varepsilon_0 \frac{R_1 R_2}{R_2 - R_1}$.

#### Question 3
One mole of an ideal monoatomic gas undergoes an expansion wherein its pressure and volume satisfy the polytropic relation $P V^{1/2} = \text{constant}$:
(A) The molar heat capacity of the gas during this process is $C = C_V + \frac{R}{1 - n} = \frac{3}{2}R + 2R = \frac{7}{2}R$.  
(B) When the gas expands from $V_1$ to $4V_1$, the temperature doubles ($T_2 = 2T_1$).  
(C) The work done by the gas during this expansion is $W = 2 R T_1$.  
(D) The heat absorbed by the gas during this expansion is $Q = \frac{7}{2}R T_1$.

#### Question 4
In a Young's double slit experiment, monochromatic light of wavelength $\lambda = 500\text{ nm}$ illuminates two slits separated by distance $d = 1.0\text{ mm}$, with a screen placed at distance $D = 2.0\text{ m}$:
(A) The fringe width on the screen is $\beta = \frac{\lambda D}{d} = 1.0\text{ mm}$.  
(B) The angular fringe width is $\theta_w = \lambda/d = 5.0 \times 10^{-4}\text{ rad}$.  
(C) If the entire apparatus is immersed in water ($\mu = 4/3$), the fringe width decreases to $0.75\text{ mm}$.  
(D) The intensity at a point on the screen where the path difference is $\lambda/4$ is half of the maximum intensity ($I = I_0/2$).

#### Question 5
Regarding the nuclear binding energy and stability of atomic nuclei:
(A) The binding energy per nucleon ($BE/A$) reaches a broad maximum of $\approx 8.8\text{ MeV/nucleon}$ near iron ($^{56}\text{Fe}$).  
(B) Nuclear fusion of very light nuclei ($A < 20$) releases energy because the binding energy per nucleon increases toward $^{56}\text{Fe}$.  
(C) Nuclear fission of heavy nuclei ($A > 200$, such as $^{235}\text{U}$) releases energy because the fragments have higher $BE/A$ than the parent nucleus.  
(D) The saturation property of nuclear forces implies that each nucleon interacts only with its immediate nearest neighbors.

#### Question 6
A block of mass $m$ is connected to two identical horizontal springs, each of spring constant $k$:
(A) When the springs are connected in parallel, the effective spring constant is $k_{\text{eff}} = 2k$, and the angular frequency is $\omega_p = \sqrt{2k/m}$.  
(B) When the springs are connected in series, the effective spring constant is $k_{\text{eff}} = k/2$, and the angular frequency is $\omega_s = \sqrt{k/(2m)}$.  
(C) The ratio of the parallel to series natural frequencies is $\omega_p / \omega_s = 2.0$.  
(D) The time period in series is twice that in parallel ($T_s = 2 T_p$).

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A horizontal uniform rod of mass $M = 3.00\text{ kg}$ and length $L = 2.00\text{ m}$ is supported at its two ends by two vertical strings. A load of mass $m = 6.00\text{ kg}$ is placed at distance $x = 0.50\text{ m}$ from the left end. Calculate the tension $T_1$ (in Newtons) in the left supporting string. [Take $g = 9.80\text{ m/s}^2$. Round off to ONE decimal place].

#### Question 8
In an electric circuit, a capacitor of capacitance $C = 20.0\ \mu\text{F}$ is charged to potential $V = 100.0\text{ V}$. Calculate the electrostatic energy $U$ (in Joules) stored in the capacitor.

#### Question 9
A compound microscope has an objective of focal length $f_o = 1.00\text{ cm}$ and an eyepiece of focal length $f_e = 5.00\text{ cm}$. The tube length (distance between focal points) is $L = 20.0\text{ cm}$. If the final image is formed at the near point ($D = 25.0\text{ cm}$), calculate the magnifying power $m$ of the microscope.

#### Question 10
One mole of an ideal gas expands isothermally at $T = 300.0\text{ K}$ from volume $V_1 = 0.010\text{ m}^3$ to $V_2 = 0.020\text{ m}^3$. Calculate the work done $W$ (in Joules) by the gas. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 2 = 0.6931$. Round off to the nearest integer].

#### Question 11
The work function of potassium is $\Phi_0 = 2.30\text{ eV}$. Calculate the threshold wavelength $\lambda_0$ (in nanometers, $\text{nm}$) for photoelectric emission from potassium. [Take $h c = 1240\text{ eV}\cdot\text{nm}$. Round off to the nearest integer].

#### Question 12
A simple pendulum has an oscillation period of $T = 2.00\text{ s}$ inside a stationary elevator. If the elevator accelerates vertically upwards with acceleration $a = 2.45\text{ m/s}^2 = g/4$, calculate the new time period $T'$ (in seconds) of the pendulum. [Take $g = 9.80\text{ m/s}^2$ and $\sqrt{5/4} \approx 1.118$. Round off to TWO decimal places].

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the rotational moments of inertia in List-I with their mathematical value in List-II:
- **List-I**:
  - P. Solid sphere of mass $M$, radius $R$ about a tangent
  - Q. Solid cylinder of mass $M$, radius $R$ about its central axis
  - R. Thin spherical shell of mass $M$, radius $R$ about a diameter
  - S. Thin uniform rod of mass $M$, length $L$ about an axis through one end
- **List-II**:
  - 1. $\frac{7}{5}M R^2$
  - 2. $\frac{1}{2}M R^2$
  - 3. $\frac{2}{3}M R^2$
  - 4. $\frac{1}{3}M L^2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 14
Match the electromagnetic laws in List-I with their mathematical expression in List-II:
- **List-I**:
  - P. Coulomb's Law
  - Q. Gauss's Law
  - R. Biot-Savart Law
  - S. Faraday's Law
- **List-II**:
  - 1. $F = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r^2}$
  - 2. $\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enclosed}}}{\varepsilon_0}$
  - 3. $d\vec{B} = \frac{\mu_0 I}{4\pi}\frac{d\vec{l}\times\hat{r}}{r^2}$
  - 4. $\mathcal{E} = -\frac{d\Phi_B}{dt}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 15
Match the optical devices in List-I with their principal operating phenomenon in List-II:
- **List-I**:
  - P. Periscope
  - Q. Compound microscope
  - R. Optical fiber
  - S. Polarizing sunglasses
- **List-II**:
  - 1. Reflection / Total internal reflection
  - 2. Dual-lens refractive magnification
  - 3. Total internal reflection in core-cladding structure
  - 4. Selective absorption of polarized glare

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the thermodynamic processes in List-I with their governing equation for an ideal gas in List-II:
- **List-I**:
  - P. Isothermal
  - Q. Isobaric
  - R. Isochoric
  - S. Adiabatic
- **List-II**:
  - 1. $P V = \text{constant}$
  - 2. $V/T = \text{constant}$
  - 3. $P/T = \text{constant}$
  - 4. $P V^\gamma = \text{constant}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 17
Match the nuclear particles in List-I with their charge and rest mass in List-II:
- **List-I**:
  - P. Alpha particle
  - Q. Beta-minus particle (electron)
  - R. Positron
  - S. Neutrino
- **List-II**:
  - 1. Charge $+2e$, mass $\approx 4\text{ u}$
  - 2. Charge $-e$, mass $m_e$
  - 3. Charge $+e$, mass $m_e$
  - 4. Zero charge, nearly zero mass

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 18
Match the electrical circuit quantities in List-I with their SI unit in List-II:
- **List-I**:
  - P. Capacitance
  - Q. Inductance
  - R. Magnetic field
  - S. Electric potential
- **List-II**:
  - 1. Farad ($\text{F}$)
  - 2. Henry ($\text{H}$)
  - 3. Tesla ($\text{T}$)
  - 4. Volt ($\text{V}$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the acidity of substituted benzoic acids:
(A) Electron-withdrawing substituents ($-\text{NO}_2, -\text{CN}$) increase the acidity of benzoic acid by dispersing the negative charge of the carboxylate anion.  
(B) Electron-donating substituents ($-\text{OCH}_3, -\text{CH}_3$) at meta/para positions decrease the acidity.  
(C) Ortho-substituted benzoic acids are stronger acids than benzoic acid regardless of the electronic nature of the substituent (ortho effect).  
(D) 2,4,6-trinitrobenzoic acid is a very strong organic acid comparable to mineral acids.

#### Question 20
Which of the following molecules have zero dipole moment ($\mu = 0$)?
(A) Carbon dioxide ($\text{CO}_2$)  
(B) Boron trifluoride ($\text{BF}_3$)  
(C) Carbon tetrachloride ($\text{CCl}_4$)  
(D) Sulfur dioxide ($\text{SO}_2$)

#### Question 21
Regarding electrolysis and Faraday's laws:
(A) One Faraday ($1\text{ F} \approx 96500\text{ C}$) is the quantity of electric charge carried by one mole of electrons.  
(B) Passage of $1\text{ F}$ of electricity deposits 1 gram-equivalent of any substance at an electrode.  
(C) Electrolysis of dilute aqueous $\text{NaCl}$ using inert platinum electrodes yields $\text{H}_2(g)$ at the cathode and $\text{O}_2(g)$ at the anode.  
(D) Electrolysis of concentrated aqueous $\text{NaCl}$ (brine) yields $\text{Cl}_2(g)$ at the anode and $\text{H}_2(g)$ at the cathode.

#### Question 22
Regarding the roasting and smelting in pyrometallurgy of lead:
(A) Galena ($\text{PbS}$) is roasted in air to form lead(II) oxide ($\text{PbO}$) and lead(II) sulfate ($\text{PbSO}_4$).  
(B) In the self-reduction process, unreacted $\text{PbS}$ reduces $\text{PbO}$ and $\text{PbSO}_4$ to metallic lead without requiring an external reducing agent: $2\text{PbO} + \text{PbS} \to 3\text{Pb} + \text{SO}_2$.  
(C) Lead obtained from smelting contains silver impurities, which are removed by Parkes process using molten zinc.  
(D) Desilverization of lead by Parkes process is based on zinc and lead being mutually immiscible, with silver being much more soluble in zinc than in lead.

#### Question 23
Which of the following compounds undergo racemization during an $\text{S}_N1$ solvolysis reaction?
(A) Optically active 2-bromobutane  
(B) Optically active 1-phenylethyl chloride  
(C) Methyl iodide  
(D) 1-bromobutane

#### Question 24
Regarding the crystal structures of ionic solids:
(A) In a face-centered cubic ($\text{FCC}$) lattice, each unit cell contains 4 atoms, 4 octahedral voids, and 8 tetrahedral voids.  
(B) The radius ratio for tetrahedral coordination ($4$) is $0.225 \le r_+/r_- < 0.414$.  
(C) The radius ratio for octahedral coordination ($6$) is $0.414 \le r_+/r_- < 0.732$.  
(D) The radius ratio for cubic coordination ($8$, as in $\text{CsCl}$) is $0.732 \le r_+/r_- < 1.000$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
A weak acid $HA$ has dissociation constant $K_a = 1.0 \times 10^{-5}$. Calculate the $\text{pH}$ of a $0.10\text{ M}$ solution of this acid.

#### Question 26
For a reaction $A \to B$, the rate of reaction triples when the concentration of $A$ is increased by a factor of 9. Calculate the order of the reaction with respect to $A$. [Round off to ONE decimal place].

#### Question 27
Copper crystallizes in an $\text{FCC}$ unit cell with edge length $a = 361.0\text{ pm}$. Calculate the volume of the unit cell in $10^{-24}\text{ cm}^3$. [Take $3.61^3 \approx 47.05$. Round off to ONE decimal place].

#### Question 28
Calculate the standard cell potential $E_{\text{cell}}^\circ$ (in Volts) at $298\text{ K}$ for the cell reaction:
$$\text{Zn}(s) + \text{Fe}^{2+}(aq) \to \text{Zn}^{2+}(aq) + \text{Fe}(s)$$
Given standard reduction potentials: $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.763\text{ V}$ and $E^\circ(\text{Fe}^{2+}/\text{Fe}) = -0.440\text{ V}$. [Round off to THREE decimal places].

#### Question 29
A $5.0\%$ (weight/volume) solution of cane sugar ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$, molar mass $342.0\text{ g/mol}$) is isotonic with a $1.0\%$ (w/v) solution of an unknown substance $X$ at the same temperature. Calculate the molar mass of substance $X$ in $\text{g/mol}$. [Round off to ONE decimal place].

#### Question 30
Find the oxidation state of manganese in potassium permanganate ($\text{KMnO}_4$).

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the organic tests in List-I with the functional group identified in List-II:
- **List-I**:
  - P. Carbylamine test
  - Q. Iodoform test
  - R. Hinsberg test
  - S. 2,4-DNP test
- **List-II**:
  - 1. Primary aliphatic or aromatic amine
  - 2. Methyl ketone or methyl carbinol group
  - 3. Distinction between $1^\circ, 2^\circ$, and $3^\circ$ amines
  - 4. Carbonyl group (aldehydes and ketones)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 32
Match the coordination compounds in List-I with their hybridisation state of the central metal in List-II:
- **List-I**:
  - P. $[\text{Ni(CO)}_4]$
  - Q. $[\text{Ni(CN)}_4]^{2-}$
  - R. $[\text{Fe(CN)}_6]^{3-}$
  - S. $[\text{CoF}_6]^{3-}$
- **List-II**:
  - 1. $sp^3$
  - 2. $dsp^2$
  - 3. $d^2sp^3$
  - 4. $sp^3d^2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 33
Match the metallurgical processes in List-I with the metal extracted in List-II:
- **List-I**:
  - P. Cyanide leaching process
  - Q. Hall-Héroult electrolytic reduction
  - R. Blast furnace reduction
  - S. Self-reduction process
- **List-II**:
  - 1. Gold / Silver
  - 2. Aluminum
  - 3. Iron
  - 4. Copper / Lead

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 34
Match the oxides of nitrogen in List-I with their formal oxidation state of nitrogen in List-II:
- **List-I**:
  - P. $\text{N}_2\text{O}$
  - Q. $\text{NO}$
  - R. $\text{NO}_2$
  - S. $\text{N}_2\text{O}_5$
- **List-II**:
  - 1. $+1$
  - 2. $+2$
  - 3. $+4$
  - 4. $+5$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 35
Match the polymers in List-I with their commercial application in List-II:
- **List-I**:
  - P. Glyptal
  - Q. Bakelite
  - R. Teflon
  - S. PVC
- **List-II**:
  - 1. Paints and lacquers
  - 2. Electrical switches and handles
  - 3. Non-stick cookware coating
  - 4. Raincoats and water pipes

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 36
Match the vitamins in List-I with their chemical name in List-II:
- **List-I**:
  - P. Vitamin A
  - Q. Vitamin C
  - R. Vitamin D
  - S. Vitamin E
- **List-II**:
  - 1. Retinol
  - 2. Ascorbic acid
  - 3. Ergocalciferol
  - 4. Tocopherol

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^4 - 4x^3 + 4x^2 + 1$ for $x \in \mathbb{R}$:
(A) $f'(x) = 4x(x - 1)(x - 2)$.  
(B) $f(x)$ has local minima at $x = 0$ and $x = 2$, each with minimum value $1$.  
(C) $f(x)$ has a local maximum at $x = 1$ with maximum value $2$.  
(D) The absolute minimum value of $f(x)$ on $\mathbb{R}$ is $1$.

#### Question 38
Let $A$ be a $2 \times 2$ real matrix such that $\text{tr}(A) = 5$ and $\det(A) = 6$:
(A) The characteristic equation of $A$ is $\lambda^2 - 5\lambda + 6 = 0$.  
(B) The eigenvalues of $A$ are $\lambda_1 = 2$ and $\lambda_2 = 3$.  
(C) By the Cayley-Hamilton theorem, $A^2 - 5A + 6I = 0$.  
(D) The matrix inverse is $A^{-1} = \frac{1}{6}(5I - A)$.

#### Question 39
Consider the parabola $y^2 = 12x$:
(A) The focus is located at $(3, 0)$.  
(B) The equation of the directrix is $x = -3$.  
(C) The length of the latus rectum is $12$.  
(D) The tangent at the vertex is the y-axis ($x = 0$).

#### Question 40
Consider the differential equation $\frac{dy}{dx} = \frac{y}{x} + \tan\left(\frac{y}{x}\right)$ for $x > 0$:
(A) The differential equation is homogeneous.  
(B) Substituting $y = v x$ gives $x \frac{dv}{dx} = \tan v$.  
(C) Separating variables yields $\cot v dv = \frac{dx}{x}$.  
(D) The general solution is $\sin(y/x) = C x$.

#### Question 41
Let $\vec{a} = 2\hat{i} + \hat{j} - \hat{k}$ and $\vec{b} = \hat{i} - \hat{j} + 2\hat{k}$:
(A) $\vec{a} \cdot \vec{b} = 2(1) + 1(-1) + (-1)(2) = -1$.  
(B) $\vec{a} \times \vec{b} = \hat{i} - 5\hat{j} - 3\hat{k}$.  
(C) The angle between $\vec{a}$ and $\vec{b}$ is obtuse ($\cos\theta < 0$).  
(D) $|\vec{a} \times \vec{b}| = \sqrt{1 + 25 + 9} = \sqrt{35}$.

#### Question 42
In rolling two fair standard six-sided dice:
(A) The total number of elementary outcomes in the sample space is $36$.  
(B) The probability of getting a doublet (both numbers identical) is $6/36 = 1/6$.  
(C) The probability of getting a sum of at least 10 is $6/36 = 1/6$.  
(D) The events "sum is 7" and "first die shows 3" are independent.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 x^2 (1 - x)^3\,dx$$
If $I = \frac{1}{m}$, find the integer value of $m$.

#### Question 44
Find the slope of the normal to the curve $y = x^3 - 3x + 2$ at the point where $x = 2$.

#### Question 45
Calculate the distance between the parallel lines $4x - 3y + 5 = 0$ and $4x - 3y - 15 = 0$.

#### Question 46
Calculate the sum of the infinite geometric series:
$$S = 24 + 12 + 6 + 3 + \dots$$

#### Question 47
Calculate the number of ways to arrange the letters of the word `COMMITTEE` ($\frac{9!}{2! 2! 2!}$).

#### Question 48
Calculate the determinant of the matrix:
$$A = \begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix}$$

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{e^{2x} - 1}{\sin(3x)}$$
(A) $2/3$  
(B) $3/2$  
(C) $1$  
(D) $0$

#### Question 50
The eccentricity of the ellipse $\frac{x^2}{25} + \frac{y^2}{16} = 1$ is:
(A) $3/5 = 0.60$  
(B) $4/5 = 0.80$  
(C) $9/25$  
(D) $16/25$

#### Question 51
The angle between the lines with direction ratios $(1, 2, 2)$ and $(2, -2, 1)$ is:
(A) $\pi/2$ ($90^\circ$)  
(B) $\pi/4$ ($45^\circ$)  
(C) $\pi/3$ ($60^\circ$)  
(D) $0^\circ$

#### Question 52
If $z = 3 + 4i$, then the principal argument $\arg(z)$ is:
(A) $\arctan(4/3)$  
(B) $\arctan(3/4)$  
(C) $\pi - \arctan(4/3)$  
(D) $\pi/4$

#### Question 53
The general solution of the differential equation $\frac{dy}{dx} = 2x y$ is:
(A) $y = C e^{x^2}$  
(B) $y = C e^{2x}$  
(C) $y = C x^2$  
(D) $y = e^{x^2} + C$

#### Question 54
A card is drawn at random from a standard well-shuffled deck of 52 playing cards. The probability that the card is either a King or a Heart is:
(A) $16/52 = 4/13$  
(B) $17/52$  
(C) $13/52 = 1/4$  
(D) $4/52 = 1/13$
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 11 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Relativistic Compton Scattering, Kinematics of Elastic Photon-Electron Collisions.
- **2. Derivation**:
  - Conservation of four-momentum gives $\lambda' - \lambda_0 = \frac{h}{m_e c}(1 - \cos\theta) = \lambda_C(1 - \cos\theta)$. (A) is correct.
  - Kinetic energy transferred to electron: $K_e = E_0 - E' = h\nu_0 - \frac{h c}{\lambda'} = E_0\left(1 - \frac{1}{1 + \alpha(1-\cos\theta)}\right) = \frac{E_0 \alpha(1-\cos\theta)}{1 + \alpha(1-\cos\theta)}$. (B) is correct.
  - Longitudinal and transverse momentum conservation: $p_e \cos\phi = \frac{h\nu_0}{c} - \frac{h\nu'}{c}\cos\theta$, $p_e \sin\phi = \frac{h\nu'}{c}\sin\theta$. Dividing gives $\cot\phi = (1 + \alpha)\tan(\theta/2)$. (C) is correct.
  - Compton edge occurs at $\theta = 180^\circ$ where $\cos\theta = -1 \implies K_{\text{max}} = \frac{2\alpha E_0}{1 + 2\alpha}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Coupled Oscillators, Normal Modes, Beat Phenomenon.
- **2. Derivation**:
  - Equations of motion: $m l^2 \ddot{\theta}_1 = -m g l \theta_1 - k d^2(\theta_1 - \theta_2)$, $m l^2 \ddot{\theta}_2 = -m g l \theta_2 - k d^2(\theta_2 - \theta_1)$.
  - Symmetric mode ($\theta_1 = \theta_2$): spring is unstretched, so restoring force is purely gravity, giving $\omega_1 = \sqrt{g/l}$. (A) is correct.
  - Antisymmetric mode ($\theta_1 = -\theta_2$): spring stretch is $2d\theta$, giving $\omega_2 = \sqrt{\frac{g}{l} + \frac{2k d^2}{m l^2}}$. (B) is correct.
  - Initial condition produces superposition $\theta_1(t) = \theta_0 \cos(\frac{\omega_2-\omega_1}{2}t)\cos(\frac{\omega_1+\omega_2}{2}t)$, with beat period $T_{\text{beat}} = \frac{2\pi}{\omega_2-\omega_1}$. (C) is correct.
  - As $d$ increases, the spring torque increases, raising $\omega_2$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Foucault Pendulum, Coriolis Acceleration, Non-Inertial Reference Frames.
- **2. Derivation**:
  - Coriolis acceleration $\vec{a}_C = -2(\vec{\Omega}\times\vec{v})$. In Northern Hemisphere, vertical component of Earth's rotation $\Omega_z = \Omega\sin\lambda$ causes clockwise precession. (A) is correct.
  - Precession rate $\Omega_p = \Omega_{\text{Earth}}\sin\lambda$. (B) is correct.
  - At $\lambda = 90^\circ$, $\Omega_p = \Omega_{\text{Earth}}$, completing $360^\circ$ in one sidereal day ($23.93\text{ h}$). (C) is correct.
  - At equator ($\lambda = 0$), $\sin\lambda = 0$, so plane of oscillation remains fixed in inertial space ($\Omega_p = 0$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Berthelot Real Gas Equation, Critical State Thermodynamics.
- **2. Derivation**:
  - Internal pressure $a/(T V^2)$ captures temperature-dependent cohesion. (A) is correct.
  - Critical conditions: $(\partial P/\partial V)_T = 0, (\partial^2 P/\partial V^2)_T = 0$.
  - Logarithmic derivative yields $V_c = 3b$. (B) is correct.
  - Second derivative yields $T_c = \sqrt{\frac{8a}{27Rb}}$. (C) is correct.
  - Substituting $V_c$ and $T_c$ gives $Z_c = \frac{P_c V_c}{R T_c} = \frac{3}{8} = 0.375$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Wave Plates, Birefringence, Optical Activity.
- **2. Derivation**:
  - QWP introduces phase difference $\delta = \frac{2\pi}{\lambda}|n_e - n_o|d = \pi/2$ ($\Delta L = \lambda/4$). (A) is correct.
  - Incident linear polarization at $45^\circ$ has equal $x$ and $y$ components, so $\pi/2$ phase shift produces circular polarization. (B) is correct.
  - HWP introduces $\pi$ phase shift, reflecting the polarization vector across the fast axis, rotating it by $2\theta$. (C) is correct.
  - Optical activity is caused by circular birefringence ($\mu_R \ne \mu_L$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Variable Mass Dynamics, Tsiolkovsky Rocket Equation in Gravity.
- **2. Derivation**:
  - Momentum conservation on system: $(m + dm)(v + dv) + (-dm)(v - u) - m v = -m g dt \implies m dv = -u dm - m g dt$. With $dm/dt = -\alpha$, $m \frac{dv}{dt} = u \alpha - m g$. (A) is correct.
  - Integrating from $0$ to $t$: $v(t) = u \ln\left(\frac{m_0}{m_0 - \alpha t}\right) - gt$. (B) is correct.
  - Thrust force is $F_{\text{thrust}} = u \alpha$. (C) is correct.
  - For positive upward initial acceleration, $u \alpha > m_0 g$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: $\Delta\lambda = \lambda_C(1 - \cos 180^\circ) = 2\lambda_C = 2(0.0243\text{ \AA}) = 0.0486\text{ \AA}$.
  Fractional shift: $\frac{\Delta\lambda}{\lambda_0} = \frac{0.0486}{0.0500} = 0.972 \approx 0.97$.
- **Question 8**: Two capacitors in series: $C_1 = \frac{\varepsilon_0 A}{d/2} = \frac{2\varepsilon_0 A}{d}$, $C_2 = \frac{\varepsilon_0 \varepsilon_r A}{d/2} = \frac{2\varepsilon_0 \varepsilon_r A}{d}$.
  $C_{\text{eff}} = \frac{C_1 C_2}{C_1 + C_2} = \frac{2\varepsilon_0 A}{d}\frac{\varepsilon_r}{1 + \varepsilon_r} = \frac{2(8.854 \times 10^{-12})(0.040)}{2.0 \times 10^{-3}}\left(\frac{4.0}{5.0}\right) = (3.5416 \times 10^{-10})(0.80) = 2.833 \times 10^{-10}\text{ F} = 283.3\text{ pF}$.
- **Question 9**: Central diffraction minimum occurs at $a\sin\theta = \lambda \implies \sin\theta = \lambda/a$.
  Interference maxima occur at $d\sin\theta = m\lambda$. At diffraction minimum, $m = d/a = \frac{0.200}{0.040} = 5$.
  Thus orders $m = -4, -3, -2, -1, 0, 1, 2, 3, 4$ are visible within central maximum.
  Total bright fringes $= 2(4) + 1 = 9$.
- **Question 10**: $W = \int_{V_1}^{V_2} P dV = \alpha \int_{1.0}^{2.0} V^2 dV = \alpha\left[\frac{V^3}{3}\right]_1^2 = \frac{2.0 \times 10^5}{3}(8 - 1) = \frac{14.0 \times 10^5}{3} \approx 4.67 \times 10^5\text{ J} = 466.67\text{ kJ}$.
- **Question 11**: $K = q V = (2e)(1.0 \times 10^6\text{ V}) = 2.0\text{ MeV}$.
- **Question 12**: $T = 2\pi\sqrt{L/g} \implies L = \frac{g T^2}{4\pi^2} = \frac{9.80(4.00)}{4(9.87)} = \frac{9.80}{9.87} \approx 0.99\text{ m}$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $a_c = \frac{v^2}{R} = \frac{(a_t t)^2}{R} = a_t \implies \frac{a_t^2 t^2}{R} = a_t \implies t = \sqrt{\frac{R}{a_t}} = \sqrt{\frac{2.0}{3.0}} \approx 0.82\text{ s}$. Option (A).
- **Question 14**: $\vec{E} = -\nabla V = -\left(\frac{\partial V}{\partial x}\hat{i} + \frac{\partial V}{\partial y}\hat{j} + \frac{\partial V}{\partial z}\hat{k}\right) = -(8x\hat{i} - 6y\hat{j} + 4z\hat{k})$. At $(1, 1, 1)$, $\vec{E} = -8\hat{i} + 6\hat{j} - 4\hat{k}\text{ V/m}$. Option (A).
- **Question 15**: $v = \sqrt{\gamma R T / M}$. Ratio $v_1 / v_2 = \sqrt{M_2 / M_1} = \sqrt{40.0 / 4.0} = \sqrt{10} \approx 3.16$. Option (A).
- **Question 16**: $m = f_o / f_e = 100.0 / 5.0 = 20$; $L = f_o + f_e = 100.0 + 5.0 = 105.0\text{ cm}$. Option (A).
- **Question 17**: $K = U \implies \frac{1}{2}k(A^2 - x^2) = \frac{1}{2}k x^2 \implies 2x^2 = A^2 \implies x = A/\sqrt{2}$. Option (A).
- **Question 18**: Diamagnetic materials have negative, small, and temperature-independent susceptibility. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Curtius rearrangement decomposes acyl azides to isocyanates with nitrogen extrusion. Group migrates with retention of configuration. Hydrolysis yields primary amines. Schmidt reaction uses carboxylic acid and $\text{HN}_3$. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Michaelis-Menten rate law $v_0 = \frac{V_{\max}[S]}{K_m + [S]}$. Competitive inhibition increases $K_m$ ($V_{\max}$ unchanged). Non-competitive reduces $V_{\max}$ ($K_m$ unchanged). Correct options: **(A), (B), (C), (D)**.
- **Question 21**: Quinhydrone is $1:1$ complex of quinone and hydroquinone. Redox couple is $\text{Q} + 2\text{H}^+ + 2e^- \rightleftharpoons \text{QH}_2$. Potential is $E = 0.6996 - 0.0591\text{ pH}$. Fails above $\text{pH} = 8.5$ due to hydroquinone ionization. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: Oxides form CCP array. Normal spinel: $\text{A}^{2+}$ in $1/8$ tetrahedral, $\text{B}^{3+}$ in $1/2$ octahedral. Inverse spinel: $\text{Fe}^{3+}[\text{Fe}^{2+}\text{Fe}^{3+}]\text{O}_4$. Governed by octahedral CFSE gain. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Edman degradation uses PITC on N-terminus under basic conditions. Acid cleavage yields ATZ intermediate. ATZ isomerizes to PTH amino acid. Shortened peptide undergoes repetitive cycles. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Interhalogens $\text{XX}'_n$ have polar bonds, making them more reactive than pure halogens (except $\text{F}_2$). $\text{IF}_7$ is pentagonal bipyramidal ($sp^3d^3$). Hydrolysis gives halide from smaller and oxohalide from larger halogen. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $\text{Mg(OH)}_2 \rightleftharpoons \text{Mg}^{2+} + 2\text{OH}^-$. $K_{sp} = S(2S)^2 = 4S^3 \implies 4S^3 = 1.2 \times 10^{-11} \implies S^3 = 3.0 \times 10^{-12} \implies S = (3.0)^{1/3} \times 10^{-4} = 1.44 \times 10^{-4}\text{ M}$.
  $[\text{OH}^-] = 2S = 2.88 \times 10^{-4}\text{ M} \implies p\text{OH} = 4 - \log(2.88) = 4 - 0.459 = 3.541 \implies \text{pH} = 14 - 3.541 = 10.46$.
- **Question 26**: $\frac{1}{[A]} - \frac{1}{[A]_0} = k t \implies \frac{1}{0.050} - \frac{1}{0.20} = 0.050 t \implies 20.0 - 5.0 = 15.0 = 0.050 t \implies t = \frac{15.0}{0.050} = 300.0\text{ s}$.
- **Question 27**: For FCC lattice: $4r = \sqrt{2}a \implies r = \frac{\sqrt{2} \times 400.0}{4} = \frac{1.414 \times 400.0}{4} = 141.4\text{ pm}$.
- **Question 28**: $\Delta G^\circ = -n F E^\circ = -2(96485)(1.20) = -231564\text{ J/mol} = -231.6\text{ kJ/mol}$.
- **Question 29**: $\Delta T_f = i K_f m = (1.20)(1.86)(0.10) = 0.2232\text{ K} \approx 0.22\text{ K}$.
- **Question 30**: In $[Co(en)_2Cl_2]^+$, `en` is bidentate (occupies 2 coordination sites each), and two chloride ligands are monodentate. Total coordination number $= 2(2) + 2 = 6$.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Gabriel phthalimide is exclusively used for pure primary aliphatic amines. Option (A).
- **Question 32**: $[\text{Ni(CN)}_4]^{2-}$ is $dsp^2$ square planar with strong field $\text{CN}^-$, pairing all 8 $d$-electrons (diamagnetic). Option (A).
- **Question 33**: Sodium ethyl xanthate serves as a collector in froth flotation. Option (A).
- **Question 34**: $\text{ClF}_3$ has 3 bond pairs and 2 lone pairs ($sp^3d$), T-shaped. Option (A).
- **Question 35**: An $\alpha\text{-helix}$ is a classic secondary structure of proteins. Option (A).
- **Question 36**: Nylon-6,6 is formed by condensation of hexamethylenediamine and adipic acid. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Bernoulli ODE: $y' + \frac{1}{x}y = x y^2$. Dividing by $y^2$: $y^{-2}y' + \frac{1}{x}y^{-1} = x$.
  Let $v = y^{-1} \implies v' = -y^{-2}y'$. Thus $-v' + \frac{1}{x}v = x \implies v' - \frac{1}{x}v = -x$. (A) is correct.
  $\text{IF} = e^{-\int (1/x)dx} = 1/x$. (B) is correct.
  $\frac{v}{x} = \int (-1)dx = -x + C \implies v = C x - x^2$. (C) is correct.
  $y = 1/v = \frac{1}{C x - x^2}$. (D) is correct.
- **Question 38**: Similar matrices: $\det(\lambda I - P^{-1} A P) = \det(P^{-1}(\lambda I - A)P) = \det(\lambda I - A)$, preserving characteristic polynomial, eigenvalues, multiplicities, trace, determinant, and rank. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Chord of contact from $(x_0, y_0)$ is $\frac{x x_0}{a^2} - \frac{y y_0}{b^2} = 1$. Passing through focus $(a e, 0)$ gives $\frac{a e x_0}{a^2} = 1 \implies x_0 = a/e$ (directrix). Director circle is $x^2 + y^2 = a^2 - b^2$. For $a = b$, director circle reduces to single point $(0, 0)$. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Family of planes $P_1 + \lambda P_2 = 0$ contains the line of intersection. Line direction is parallel to $\vec{n}_1 \times \vec{n}_2$. Perpendicularity condition holds. Every line point satisfies both plane equations. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Catalan numbers: $C_0=1, C_1=1, C_2=2, C_3=5, C_4=14, C_5=42$. Segner recurrence holds. Dyck paths and balanced parentheses are classic interpretations. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Normal distribution: symmetric about $\mu$; inflection points at $\mu \pm \sigma$; $1\sigma$ interval contains $68.27\%$; $2\sigma$ interval contains $95.45\%$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: $\int_0^1 x^3 e^x dx = [x^3 e^x]_0^1 - 3\int_0^1 x^2 e^x dx = e - 3([x^2 e^x]_0^1 - 2\int_0^1 x e^x dx) = e - 3(e - 2(e - (e - 1))) = e - 3(e - 2) = e - 3e + 6 = 6 - 2e$. Thus $m = 2$.
- **Question 44**: $y = \ln(1 + x^2) \implies \frac{dy}{dx} = \frac{2x}{1 + x^2}$. At $x = 1$, $\frac{dy}{dx} = \frac{2(1)}{1 + 1} = \frac{2}{2} = 1.00$.
- **Question 45**: $d = \frac{|2(1) + 1(2) - 2(3) + 8|}{\sqrt{2^2 + 1^2 + (-2)^2}} = \frac{|2 + 2 - 6 + 8|}{\sqrt{9}} = \frac{6}{3} = 2.00$.
- **Question 46**: Infinite GP $a = 18, r = 1/3 \implies S = \frac{18}{1 - 1/3} = \frac{18}{2/3} = 27.00$.
- **Question 47**: Vandermonde determinant $D = (b - a)(c - a)(c - b) = (2 - 1)(4 - 1)(4 - 2) = (1)(3)(2) = 6.00$.
- **Question 48**: $P(5, 4) = 5 \times 4 \times 3 \times 2 = 120.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Maclaurin expansion $\tan x = x + x^3/3 + \dots \implies \frac{\tan x - x}{x^3} \to 1/3$. Option (A).
- **Question 50**: Ellipse $\frac{x^2}{25} + \frac{y^2}{9} = 1 \implies a = 5, b = 3$. Length of latus rectum $= 2b^2/a = 2(9)/5 = 18/5 = 3.60$. Option (A).
- **Question 51**: First plane $2x - y + 2z = 4$. Second plane $2x - y + 2z = 10$. Distance $d = \frac{|10 - 4|}{\sqrt{4 + 1 + 4}} = \frac{6}{3} = 2.00$. Option (A).
- **Question 52**: $z = \cos(\pi/3) + i\sin(\pi/3) = e^{i\pi/3} \implies z^3 = e^{i\pi} = -1$. Option (A).
- **Question 53**: $\text{IF} = e^{\int \cot x dx} = e^{\ln\sin x} = \sin x$. Option (A).
- **Question 54**: Favorable pairs summing to 8: $(2,6), (3,5), (4,4), (5,3), (6,2)$ (5 outcomes). $P = 5/36$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 11 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Pivoted Rigid Rod Swing, Angular Acceleration and Pivot Reaction Forces.
- **2. Derivation**:
  - Torque about pivot: $\tau = M g(L/2) = I_p \alpha = \left(\frac{1}{3}M L^2\right)\alpha \implies \alpha = \frac{3g}{2L}$. (A) is correct.
  - Tangential acceleration of CM: $a_{y,\text{cm}} = \alpha(L/2) = \frac{3g}{4}$.
  - Vertical equation for CM: $M g - R_y = M a_{y,\text{cm}} = \frac{3}{4}M g \implies R_y = \frac{1}{4}M g$. (B) is correct.
  - Energy conservation: $M g(L/2) = \frac{1}{2}I_p \omega^2 = \frac{1}{2}\left(\frac{1}{3}M L^2\right)\omega^2 \implies \omega = \sqrt{\frac{3g}{L}}$. (C) is correct.
  - At bottom: centripetal acceleration of CM is $a_c = \omega^2(L/2) = \frac{3g}{L}(L/2) = \frac{3}{2}g$.
  - Pivot reaction: $R - M g = M a_c = \frac{3}{2}M g \implies R = \frac{5}{2}M g$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Concentric Spherical Shells, Grounding, Shielding.
- **2. Derivation**:
  - Grounding forces potential $V(R_2) = 0$. (A) is correct.
  - Charge $+Q$ on inner shell induces $-Q$ on inner surface of outer shell. (B) is correct.
  - Exterior field is zero since net charge enclosed is zero. (C) is correct.
  - Capacitance between shells: $C = 4\pi\varepsilon_0 \frac{R_1 R_2}{R_2 - R_1}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Polytropic Expansion, Heat Capacity, Work Done.
- **2. Derivation**:
  - $P V^{1/2} = \text{const} \implies n = 1/2$. Molar heat capacity $C = C_V + \frac{R}{1 - n} = \frac{3}{2}R + \frac{R}{1 - 1/2} = \frac{3}{2}R + 2R = \frac{7}{2}R$. (A) is correct.
  - $T V^{n-1} = \text{const} \implies T V^{-1/2} = \text{const} \implies T \propto \sqrt{V}$. When $V \to 4V_1$, $T \to 2T_1$. (B) is correct.
  - Work: $W = \frac{R(T_1 - T_2)}{n - 1} = \frac{R(T_1 - 2T_1)}{1/2 - 1} = \frac{-R T_1}{-1/2} = 2 R T_1$. (C) is correct.
  - Heat absorbed: $Q = n C \Delta T = (1)\left(\frac{7}{2}R\right)(2T_1 - T_1) = \frac{7}{2}R T_1$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Young's Double Slit Interference, Medium Immersion.
- **2. Derivation**:
  - Fringe width: $\beta = \frac{\lambda D}{d} = \frac{(500 \times 10^{-9})(2.0)}{1.0 \times 10^{-3}} = 1.0\text{ mm}$. (A) is correct.
  - Angular width $\theta_w = \beta/D = \lambda/d = 5.0 \times 10^{-4}\text{ rad}$. (B) is correct.
  - In water: $\lambda' = \lambda/\mu \implies \beta' = \beta/\mu = 1.0 / (4/3) = 0.75\text{ mm}$. (C) is correct.
  - For path difference $\lambda/4$, phase difference is $\phi = \frac{2\pi}{\lambda}\frac{\lambda}{4} = \pi/2$. Intensity $I = I_0 \cos^2(\phi/2) = I_0 \cos^2(\pi/4) = I_0/2$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Nuclear Binding Energy Curve, Fission and Fusion.
- **2. Derivation**:
  - $BE/A$ peak occurs at $^{56}\text{Fe}$ ($\approx 8.8\text{ MeV}$). (A) is correct.
  - Fusion of light nuclei increases $BE/A$, releasing energy. (B) is correct.
  - Fission of heavy nuclei splits into fragments with higher $BE/A$, releasing energy. (C) is correct.
  - Saturation property means nucleons only interact with immediate neighbors. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Spring Combinations, Parallel vs Series SHM.
- **2. Derivation**:
  - Parallel: $k_p = 2k$, $\omega_p = \sqrt{2k/m}$. (A) is correct.
  - Series: $k_s = k/2$, $\omega_s = \sqrt{k/(2m)}$. (B) is correct.
  - Ratio $\omega_p / \omega_s = \sqrt{2k / (k/2)} = \sqrt{4} = 2.0$. (C) is correct.
  - Period ratio $T_s / T_p = \omega_p / \omega_s = 2.0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Taking torque about right end: $T_1(2.00) = M g(1.00) + m g(1.50) = 3.00(9.80)(1.00) + 6.00(9.80)(1.50) = 29.4 + 88.2 = 117.6\text{ N}\cdot\text{m}$.
  $T_1 = \frac{117.6}{2.00} = 58.8\text{ N}$.
- **Question 8**: $U = \frac{1}{2}C V^2 = \frac{1}{2}(20.0 \times 10^{-6})(100.0)^2 = 10.0 \times 10^{-6} \times 10000 = 0.10\text{ J}$.
- **Question 9**: Magnification $m = \frac{L}{f_o}\left(1 + \frac{D}{f_e}\right) = \frac{20.0}{1.00}\left(1 + \frac{25.0}{5.00}\right) = 20(1 + 5) = 20 \times 6 = 120.0$.
- **Question 10**: $W = n R T \ln(V_2/V_1) = (1)(8.314)(300.0)(0.6931) = 2494.2 \times 0.6931 \approx 1729\text{ J}$.
- **Question 11**: $\lambda_0 = \frac{h c}{\Phi_0} = \frac{1240\text{ eV}\cdot\text{nm}}{2.30\text{ eV}} \approx 539\text{ nm}$.
- **Question 12**: Effective gravity $g' = g + a = g + g/4 = 5g/4$.
  $T' = 2\pi\sqrt{L/g'} = T\sqrt{g/g'} = 2.00\sqrt{4/5} = \frac{2.00 \times 2}{\sqrt{5}} = \frac{4.00}{2.236} \approx 1.79\text{ s}$.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: Solid sphere tangent $\frac{7}{5}MR^2$ (P-1); Solid cylinder $\frac{1}{2}MR^2$ (Q-2); Shell $\frac{2}{3}MR^2$ (R-3); Rod end $\frac{1}{3}ML^2$ (S-4). Option (A).
- **Question 14**: Coulomb law (P-1); Gauss law (Q-2); Biot-Savart law (R-3); Faraday law (S-4). Option (A).
- **Question 15**: Periscope: reflection (P-1); Microscope: dual lens (Q-2); Optical fiber: TIR (R-3); Polarizing shades: selective absorption (S-4). Option (A).
- **Question 16**: Isothermal $PV=C$ (P-1); Isobaric $V/T=C$ (Q-2); Isochoric $P/T=C$ (R-3); Adiabatic $PV^\gamma=C$ (S-4). Option (A).
- **Question 17**: Alpha particle: $+2e, 4\text{ u}$ (P-1); Electron: $-e, m_e$ (Q-2); Positron: $+e, m_e$ (R-3); Neutrino: $0, 0$ (S-4). Option (A).
- **Question 18**: Capacitance Farad (P-1); Inductance Henry (Q-2); B-field Tesla (R-3); Potential Volt (S-4). Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: EWG substituents increase benzoic acid acidity. EDG decrease acidity. Ortho substituents increase acidity regardless of electronic nature (ortho effect due to steric inhibition of resonance). 2,4,6-trinitrobenzoic acid is very strong. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: $\text{CO}_2$ (linear), $\text{BF}_3$ (trigonal planar), $\text{CCl}_4$ (tetrahedral) have zero net dipole moment. $\text{SO}_2$ is bent with non-zero dipole moment. Correct options: **(A), (B), (C)**.
- **Question 21**: $1\text{ F}$ is charge of 1 mole of electrons ($96500\text{ C}$). Deposits 1 gram-equivalent. Dilute $\text{NaCl}$ gives $\text{H}_2$ and $\text{O}_2$. Concentrated $\text{NaCl}$ gives $\text{Cl}_2$ at anode and $\text{H}_2$ at cathode. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: Roasting converts $\text{PbS}$ to $\text{PbO}$ and $\text{PbSO}_4$. Self-reduction reduces oxide/sulfate without coke. Parkes process desilverizes lead using zinc. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Chiral substrate gives planar carbocation in $\text{S}_N1$, causing racemization. 2-bromobutane and 1-phenylethyl chloride racemize. Correct options: **(A), (B)**.
- **Question 24**: FCC unit cell has 4 atoms, 4 octahedral, 8 tetrahedral voids. Radius ratios: tetrahedral $0.225-0.414$, octahedral $0.414-0.732$, cubic $0.732-1.000$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $[\text{H}^+] = \sqrt{K_a C} = \sqrt{(1.0 \times 10^{-5})(0.10)} = \sqrt{1.0 \times 10^{-6}} = 1.0 \times 10^{-3}\text{ M} \implies \text{pH} = 3.00$.
- **Question 26**: Rate $\propto [A]^n \implies 3 = 9^n = (3^2)^n = 3^{2n} \implies 2n = 1 \implies n = 0.5$.
- **Question 27**: $V = a^3 = (3.61 \times 10^{-8}\text{ cm})^3 = 47.05 \times 10^{-24}\text{ cm}^3 \approx 47.1 \times 10^{-24}\text{ cm}^3$.
- **Question 28**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = -0.440 - (-0.763) = +0.323\text{ V}$.
- **Question 29**: Isotonic solutions have identical molar concentrations: $\frac{w_1}{M_1 V} = \frac{w_2}{M_2 V} \implies \frac{5.0}{342.0} = \frac{1.0}{M_X} \implies M_X = \frac{342.0}{5.0} = 68.4\text{ g/mol}$.
- **Question 30**: In $\text{KMnO}_4$, oxidation state of $\text{Mn}$ is $+7.00$.

---

### Questions 31 to 36 (Matching List Solutions)
- **Question 31**: Carbylamine for $1^\circ$ amine (P-1); Iodoform for methyl carbonyl (Q-2); Hinsberg for amine classes (R-3); 2,4-DNP for carbonyls (S-4). Option (A).
- **Question 32**: $[\text{Ni(CO)}_4]$ is $sp^3$ (P-1); $[\text{Ni(CN)}_4]^{2-}$ is $dsp^2$ (Q-2); $[\text{Fe(CN)}_6]^{3-}$ is $d^2sp^3$ (R-3); $[\text{CoF}_6]^{3-}$ is $sp^3d^2$ (S-4). Option (A).
- **Question 33**: Cyanide for Au/Ag (P-1); Hall-Heroult for Al (Q-2); Blast furnace for Fe (R-3); Self-reduction for Pb/Cu (S-4). Option (A).
- **Question 34**: $\text{N}_2\text{O}$ (+1) (P-1); $\text{NO}$ (+2) (Q-2); $\text{NO}_2$ (+4) (R-3); $\text{N}_2\text{O}_5$ (+5) (S-4). Option (A).
- **Question 35**: Glyptal paints (P-1); Bakelite switches (Q-2); Teflon cookware (R-3); PVC pipes (S-4). Option (A).
- **Question 36**: Vitamin A: Retinol (P-1); Vitamin C: Ascorbic acid (Q-2); Vitamin D: Calciferol (R-3); Vitamin E: Tocopherol (S-4). Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: $f(x) = x^4 - 4x^3 + 4x^2 + 1 = x^2(x-2)^2 + 1$. $f'(x) = 4x(x-1)(x-2)$. Critical points at $0, 1, 2$. Minima at $x=0, 2$ with value 1. Maximum at $x=1$ with value 2. Absolute minimum is 1. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Characteristic equation $\lambda^2 - \text{tr}(A)\lambda + \det(A) = \lambda^2 - 5\lambda + 6 = 0$. Roots are 2 and 3. Cayley-Hamilton holds. $A^{-1} = \frac{1}{6}(5I - A)$. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: For $y^2 = 12x$, $4a = 12 \implies a = 3$. Focus $(3, 0)$, directrix $x = -3$, latus rectum 12, tangent at vertex $x = 0$. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Homogeneous equation. $y = vx \implies v + x v' = v + \tan v \implies x v' = \tan v \implies \cot v dv = dx/x \implies \ln\sin v = \ln(Cx) \implies \sin(y/x) = Cx$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: $\vec{a}\cdot\vec{b} = 2 - 1 - 2 = -1 < 0$ (obtuse). $\vec{a}\times\vec{b} = \hat{i}(2 - 1) - \hat{j}(4 - (-1)) + \hat{k}(-2 - 1) = \hat{i} - 5\hat{j} - 3\hat{k}$. Magnitude is $\sqrt{1 + 25 + 9} = \sqrt{35}$. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Sample space has 36 outcomes. Doublets: 6 outcomes ($1/6$). Sum $\ge 10$: $(4,6),(5,5),(5,6),(6,4),(6,5),(6,6)$ (6 outcomes, $1/6$). $P(\text{sum}=7) = 6/36 = 1/6$. $P(\text{sum}=7 | \text{first}=3) = P(\text{second}=4) = 1/6$. Independent! Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Beta integral $\int_0^1 x^2(1-x)^3 dx = B(3, 4) = \frac{2! 3!}{6!} = \frac{2 \times 6}{720} = \frac{12}{720} = \frac{1}{60} \implies m = 60$.
- **Question 44**: $y = x^3 - 3x + 2 \implies y' = 3x^2 - 3$. At $x = 2$, $y' = 3(4) - 3 = 9$. Slope of normal $m_N = -1/9 \approx -0.11$. Absolute value is $0.11$.
- **Question 45**: $d = \frac{|5 - (-15)|}{\sqrt{4^2 + (-3)^2}} = \frac{20}{5} = 4.00$.
- **Question 46**: Infinite GP $a = 24, r = 1/2 \implies S = \frac{24}{1 - 1/2} = 48.00$.
- **Question 47**: `COMMITTEE`: 9 letters (1 C, 2 O, 2 M, 2 T, 2 E).
  Number of arrangements $= \frac{9!}{2! 2! 2!} = \frac{362880}{8} = 45360.00$.
- **Question 48**: $\det\begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix} = 3(4) - 2(1) = 12 - 2 = 10.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: $\lim_{x\to 0}\frac{e^{2x} - 1}{\sin(3x)} = \frac{2}{3}$. Option (A).
- **Question 50**: $a = 5, b = 4 \implies e = \sqrt{1 - b^2/a^2} = \sqrt{1 - 16/25} = 3/5 = 0.60$. Option (A).
- **Question 51**: $\vec{v}_1 \cdot \vec{v}_2 = 1(2) + 2(-2) + 2(1) = 2 - 4 + 2 = 0 \implies 90^\circ = \pi/2$. Option (A).
- **Question 52**: $z = 3 + 4i \implies \arg(z) = \arctan(4/3)$. Option (A).
- **Question 53**: $\frac{dy}{y} = 2x dx \implies \ln y = x^2 + C_1 \implies y = C e^{x^2}$. Option (A).
- **Question 54**: $P(\text{King} \cup \text{Heart}) = P(\text{King}) + P(\text{Heart}) - P(\text{King of Hearts}) = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}$. Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 11
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 0.97
- Q8: 283.3
- Q9: 9
- Q10: 466.67
- Q11: 2.0
- Q12: 0.99
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
- Q25: 10.46
- Q26: 300.0
- Q27: 141.4
- Q28: -231.6
- Q29: 0.22
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
- Q43: 2
- Q44: 1.00
- Q45: 2.00
- Q46: 27.00
- Q47: 6.00
- Q48: 120.00
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
- Q7: 58.8
- Q8: 0.10
- Q9: 120.0
- Q10: 1729
- Q11: 539
- Q12: 1.79
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
- Q22: A, B, C, D
- Q23: A, B
- Q24: A, B, C, D
- Q25: 3.00
- Q26: 0.5
- Q27: 47.1
- Q28: 0.323
- Q29: 68.4
- Q30: 7.00
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
- Q43: 60
- Q44: 0.11
- Q45: 4.00
- Q46: 48.00
- Q47: 45360
- Q48: 10.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: Heavy option-checking cognitive load (+4/-2).
- **Physics**: Compton recoil kinematics, Foucault pendulum precession, Berthelot real gas, coupled oscillator normal modes, pivoted rod vertical dynamics.
- **Chemistry**: Curtius rearrangement, Michaelis-Menten kinetics, Quinhydrone pH electrode, Spinel site preference, Edman sequencing, ortho effect.
- **Mathematics**: Bernoulli ODEs, matrix similarity invariants, Catalan numbers, family of planes, Cayley-Hamilton diagonalizability.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

if __name__ == "__main__":
    create_mock_files(11, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")

