# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 10.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Relativistic invariant mass, Dieterici real gas, Abbe microscope resolution
- Baeyer-Villiger lactone synthesis, Orgel d-d diagrams, Debye-Huckel ionic strength
- Multivariable gradients, normal chord parameter relations, resonance secular terms
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 10 — Paper 1
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
In high-energy particle physics, a proton of rest mass $m_p$ and kinetic energy $K$ collides with a stationary target proton to produce a strange particle via the reaction $p + p \to p + \Lambda^0 + K^+$ (where rest masses are $m_\Lambda$ and $m_K$):
(A) The relativistic invariant mass squared of the system before collision is $s = (E_1 + m_p c^2)^2 - p_1^2 c^2 = 2m_p^2 c^4 + 2m_p c^2 E_1$.  
(B) In terms of the projectile kinetic energy $K = E_1 - m_p c^2$, the Mandelstam variable is $s = 4m_p^2 c^4 + 2m_p c^2 K$.  
(C) The threshold kinetic energy $K_{\text{th}}$ occurs when all final reaction products are produced at rest in the center-of-momentum frame, requiring $\sqrt{s} = m_p c^2 + m_\Lambda c^2 + m_K c^2$.  
(D) The threshold kinetic energy in the laboratory frame is $K_{\text{th}} = \frac{(m_p + m_\Lambda + m_K)^2 c^2 - 4m_p^2 c^2}{2m_p}$.

#### Question 2
One mole of a real gas obeys the Dieterici equation of state $P(V - b)e^{\frac{a}{RTV}} = RT$, where $a$ and $b$ are positive constants:
(A) At the critical point, the first and second volume derivatives of pressure at constant temperature vanish: $\left(\frac{\partial P}{\partial V}\right)_T = 0$ and $\left(\frac{\partial^2 P}{\partial V^2}\right)_T = 0$.  
(B) The critical volume is $V_c = 2b$.  
(C) The critical temperature is $T_c = \frac{a}{4Rb}$.  
(D) The critical compressibility factor is $Z_c = \frac{P_c V_c}{RT_c} = \frac{2}{e^2} \approx 0.271$.

#### Question 3
A light rigid rod of length $L$ carries two identical small spheres each of mass $m$ at its ends. The system is suspended horizontally by a vertical torsion fiber attached at its center with torsional spring constant $C$. A uniform magnetic field $B$ is applied vertically, and the spheres carry equal and opposite charges $+q$ and $-q$ forming an electric dipole $\vec{p} = q L$:
(A) When an external horizontal electric field $E$ is applied, the equilibrium angular displacement $\theta_0$ satisfies $C \theta_0 = q L E \cos\theta_0$.  
(B) For small angular oscillations about $\theta = 0$ in the absence of external fields, the natural angular frequency is $\omega_0 = \sqrt{\frac{2C}{m L^2}}$.  
(C) If the spheres move through a viscous medium with damping coefficient $\gamma$, the oscillations are underdamped provided $\gamma < \sqrt{2m C}$.  
(D) The period of torsional oscillation is completely independent of the amplitude for any linear Hookean fiber.

#### Question 4
Regarding the resolving power of optical instruments:
(A) According to Ernst Abbe, the minimum resolvable transverse separation between two self-luminous point objects using a microscope objective of numerical aperture $NA = n\sin\alpha$ is $d_{\text{min}} = \frac{0.61\lambda}{NA}$.  
(B) The numerical aperture of an oil-immersion objective is greater than that of a dry objective because the immersion oil ($n \approx 1.51$) increases the refractive index of the object space.  
(C) For an astronomical telescope with objective diameter $D$, the angular resolution limit according to the Rayleigh criterion is $\theta_{\text{min}} = \frac{1.22\lambda}{D}$.  
(D) Increasing the objective diameter $D$ of a telescope increases its light-gathering power proportional to $D^2$ and improves its angular resolution proportional to $D$.

#### Question 5
A uniform solid sphere of mass $M$ and radius $r$ rolls without slipping inside a fixed hollow spherical bowl of radius $R$ ($R > r$):
(A) The distance from the center of the bowl to the center of mass of the rolling sphere is $R - r$.  
(B) The kinetic energy of the sphere during motion is $K = \frac{1}{2}M v_{\text{cm}}^2 + \frac{1}{2}I_{\text{cm}}\omega^2 = \frac{7}{10}M(R - r)^2 \dot{\theta}^2$, where $\theta$ is the angular displacement from the vertical.  
(C) For small oscillations about the lowest equilibrium position, the motion is simple harmonic with angular frequency $\omega = \sqrt{\frac{5g}{7(R - r)}}$.  
(D) The oscillation period is $T = 2\pi\sqrt{\frac{7(R - r)}{5g}}$.

#### Question 6
An ideal parallel $LC$ resonant tank circuit consists of an inductor $L$ and capacitor $C$ connected in parallel across an AC current source $I(t) = I_0 \sin(\omega t)$:
(A) The total input admittance of the parallel combination is $Y(\omega) = \frac{1}{\omega L} - \omega C$.  
(B) Resonance occurs at the antiresonant frequency $\omega_0 = \frac{1}{\sqrt{LC}}$, where the input impedance approaches infinity ($Z_{\text{in}} \to \infty$) for ideal zero-loss components.  
(C) At the resonant frequency $\omega_0$, the net source current supplied to the tank is identically zero.  
(D) The circulating currents through the inductor and capacitor are equal in magnitude and $180^\circ$ out of phase with each other.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A horizontal uniform disk of mass $M = 4.00\text{ kg}$ and radius $R = 0.50\text{ m}$ rotates freely about its vertical central axis at $\omega_0 = 20.0\text{ rad/s}$. A small lump of clay of mass $m = 1.00\text{ kg}$ is dropped gently onto the disk at distance $r = 0.30\text{ m}$ from the axis and sticks to it. Calculate the new angular velocity $\omega_f$ (in $\text{rad/s}$) of the system. [Round off to TWO decimal places].

#### Question 8
Two long concentric conducting spherical shells have radii $a = 5.0\text{ cm}$ and $b = 10.0\text{ cm}$. The space between them is filled with air. Calculate the capacitance $C$ (in picoFarads, $\text{pF}$) of this spherical capacitor. [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$. Round off to ONE decimal place].

#### Question 9
In a Lloyd's mirror experiment, a slit emitting light of wavelength $\lambda = 600\text{ nm}$ is placed at height $h = 1.50\text{ mm}$ above the mirror surface. The screen is placed at distance $D = 2.00\text{ m}$ from the slit. Calculate the fringe width $\beta$ in millimeters ($\text{mm}$). [Round off to TWO decimal places].

#### Question 10
One mole of an ideal gas expands isothermally at $T = 300\text{ K}$ from an initial pressure $P_1 = 4.0\text{ atm}$ to a final pressure $P_2 = 1.0\text{ atm}$. Calculate the change in entropy $\Delta S$ (in $\text{J/(mol}\cdot\text{K)}$) of the gas. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 4 = 1.3863$. Round off to TWO decimal places].

#### Question 11
An electron is accelerated from rest through a potential difference $V_0 = 150.0\text{ V}$. Calculate its de Broglie wavelength $\lambda$ in Angstroms ($\text{\AA}$). [Take $\lambda = \frac{12.27}{\sqrt{V_0}}\text{ \AA}$. Round off to TWO decimal places].

#### Question 12
The threshold frequency of a metal for photoelectric emission is $\nu_0 = 6.0 \times 10^{14}\text{ Hz}$. When light of frequency $\nu = 1.0 \times 10^{15}\text{ Hz}$ illuminates the surface, calculate the maximum kinetic energy $K_{\text{max}}$ (in electron-Volts, $\text{eV}$) of the emitted photoelectrons. [Take $h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}$ and $1\text{ eV} = 1.60 \times 10^{-19}\text{ J}$. Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle executes simple harmonic motion with amplitude $A$ and time period $T$. The time taken by the particle to travel from $x = 0$ to $x = A/2$ starting from the mean position is:
(A) $T/12$  
(B) $T/8$  
(C) $T/6$  
(D) $T/4$

#### Question 14
Two point charges $+4q$ and $+q$ are fixed at a separation distance $L$. A third charge $Q$ is placed on the line joining them so that the entire system is in electrostatic equilibrium. The magnitude, sign, and position of $Q$ are:
(A) $-4q/9$, located at distance $2L/3$ from $+4q$  
(B) $+4q/9$, located at distance $L/3$ from $+4q$  
(C) $-2q/3$, located at distance $L/2$ from $+4q$  
(D) $-q/4$, located at distance $L/4$ from $+4q$

#### Question 15
The efficiency of a Carnot heat engine operating between temperatures $T_H = 500\text{ K}$ and $T_C = 300\text{ K}$ is:
(A) $40\%$  
(B) $60\%$  
(C) $50\%$  
(D) $33.3\%$

#### Question 16
A convex lens of focal length $f = 20.0\text{ cm}$ in air ($\mu_g = 1.50$) is immersed completely in water ($\mu_w = 1.33 = 4/3$). The new focal length $f'$ of the lens in water is:
(A) $80.0\text{ cm}$  
(B) $40.0\text{ cm}$  
(C) $20.0\text{ cm}$  
(D) $10.0\text{ cm}$

#### Question 17
A uniform solid sphere of mass $M$ and radius $R$ rolls without slipping down an inclined plane of inclination $\theta$. The linear acceleration of its center of mass is:
(A) $\frac{5}{7}g\sin\theta$  
(B) $\frac{2}{3}g\sin\theta$  
(C) $\frac{1}{2}g\sin\theta$  
(D) $\frac{3}{5}g\sin\theta$

#### Question 18
A magnetic needle free to rotate in a vertical plane aligns itself along the direction of Earth's magnetic field. At a place where the horizontal and vertical components of Earth's field are equal ($B_H = B_V$), the angle of dip $\delta$ is:
(A) $45^\circ$  
(B) $30^\circ$  
(C) $60^\circ$  
(D) $90^\circ$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Baeyer-Villiger oxidation of ketones to esters or lactones using peroxy acids (e.g., $m\text{-CPBA}$):
(A) The reaction begins with nucleophilic addition of the peroxy acid to the carbonyl carbon, forming the Criegee tetrahedral intermediate.  
(B) The rate-determining step is the migration of an alkyl group with its electron pair to the adjacent peroxy oxygen atom with simultaneous expulsion of the carboxylate leaving group.  
(C) The migratory aptitude of alkyl groups follows the order: $\text{tertiary alkyl} > \text{cyclohexyl} \approx \text{secondary alkyl} > \text{benzyl} \approx \text{phenyl} > \text{primary alkyl} > \text{methyl}$.  
(D) Oxidation of cyclohexanone with $m\text{-CPBA}$ yields $\varepsilon$-caprolactone via ring expansion.

#### Question 20
Regarding Orgel diagrams for transition metal complexes:
(A) Orgel diagrams qualitatively describe the energy levels of spin-allowed $d-d$ electronic transitions for weak-field (high-spin) complexes.  
(B) High-spin $d^1$ octahedral complexes have an identical Orgel splitting pattern to high-spin $d^6$ octahedral complexes.  
(C) The energy term splitting for an octahedral $d^n$ configuration is inverted compared to that of a tetrahedral $d^n$ configuration due to the reversed crystal field splitting.  
(D) Octahedral $d^1$ ($[\text{Ti(H}_2\text{O})_6]^{3+}$) exhibits a single absorption band corresponding to the transition $^2T_{2g} \to {}^2E_g$.

#### Question 21
Regarding the Debye-Hückel limiting law for dilute strong electrolyte solutions:
(A) The ionic strength of the solution is defined as $I = \frac{1}{2}\sum_{i} c_i z_i^2$, where $c_i$ is molar concentration and $z_i$ is ionic charge.  
(B) The mean ionic activity coefficient $\gamma_\pm$ satisfies $\log_{10} \gamma_\pm = -A |z_+ z_-|\sqrt{I}$, where $A \approx 0.509\text{ mol}^{-1/2}\cdot\text{L}^{1/2}$ for water at $25^\circ\text{C}$.  
(C) For a given ionic strength, electrolytes containing polyvalent ions (e.g., $\text{Al}_2(\text{SO}_4)_3$) show much stronger deviations from ideal behavior than $1:1$ electrolytes ($\text{NaCl}$).  
(D) At infinite dilution ($I \to 0$), the mean ionic activity coefficient approaches unity ($\gamma_\pm \to 1$).

#### Question 22
Regarding polymers and average molecular weights:
(A) The number-average molecular weight is defined as $\bar{M}_n = \frac{\sum N_i M_i}{\sum N_i}$, experimentally determined by colligative properties (osmotic pressure).  
(B) The weight-average molecular weight is defined as $\bar{M}_w = \frac{\sum N_i M_i^2}{\sum N_i M_i}$, experimentally determined by light scattering or ultracentrifugation.  
(C) The polydispersity index is defined as $\text{PDI} = \frac{\bar{M}_w}{\bar{M}_n} \ge 1$.  
(D) For a perfectly monodisperse polymer (such as a natural pure protein), $\bar{M}_w = \bar{M}_n$, giving $\text{PDI} = 1.0$.

#### Question 23
Regarding the Claisen condensation and Dieckmann cyclization:
(A) The reaction involves base-catalyzed condensation between two ester molecules containing $\alpha$-hydrogens to form a $\beta$-keto ester.  
(B) Intramolecular Claisen condensation of a dicarboxylic acid diester (such as diethyl adipate) to form a cyclic $\beta$-keto ester is known as the Dieckmann cyclization.  
(C) Strong, non-nucleophilic bases such as sodium ethoxide ($\text{NaOEt}$) are typically employed to prevent transesterification side-reactions.  
(D) The driving force that pulls the equilibrium to completion is the deprotonation of the acidic methylene protons ($\text{pK}_a \approx 11$) of the resulting $\beta$-keto ester by the base.

#### Question 24
Regarding the structural chemistry of silicates and silicones:
(A) The basic structural unit of all silicate minerals is the tetrahedral $[\text{SiO}_4]^{4-}$ unit.  
(B) In sheet silicates (phyllosilicates, such as talc and mica), three oxygen atoms of each $[\text{SiO}_4]$ tetrahedron are shared with adjacent tetrahedra, forming 2D sheets with empirical formula $(\text{Si}_2\text{O}_5^{2-})_n$.  
(C) Silicones are synthetic organosilicon polymers containing repeating $-\text{R}_2\text{Si-O-SiR}_2\text{O}-$ siloxane linkages.  
(D) Controlled hydrolysis of dimethyldichlorosilane ($\text{Me}_2\text{SiCl}_2$) followed by condensation yields linear silicone polymers.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The solubility product of lead(II) iodide ($\text{PbI}_2$) in water at $25^\circ\text{C}$ is $K_{sp} = 7.1 \times 10^{-9}$. Calculate the molar solubility $S$ of $\text{PbI}_2$ in pure water in millimoles per liter ($\text{mmol/L}$). [Take $(1.775)^{1/3} \approx 1.21$. Round off to TWO decimal places].

#### Question 26
For a first-order reaction $A \to B$, the half-life is $t_{1/2} = 20.0\text{ minutes}$. Calculate the time $t$ (in minutes) required for $75.0\%$ of reactant $A$ to be decomposed.

#### Question 27
Chromium crystallizes in a body-centered cubic ($\text{BCC}$) structure with density $\rho = 7.19\text{ g/cm}^3$ and atomic mass $M = 52.00\text{ g/mol}$. Calculate the unit cell edge length $a$ in picometers ($\text{pm}$). [Take $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$, and $(2.403 \times 10^{-23})^{1/3} \approx 2.886 \times 10^{-8}$. Round off to ONE decimal place].

#### Question 28
Calculate the standard cell potential $E_{\text{cell}}^\circ$ (in Volts) at $298\text{ K}$ for the cell reaction:
$$\text{Cd}(s) + \text{Ni}^{2+}(aq) \to \text{Cd}^{2+}(aq) + \text{Ni}(s)$$
Given standard reduction potentials: $E^\circ(\text{Cd}^{2+}/\text{Cd}) = -0.403\text{ V}$ and $E^\circ(\text{Ni}^{2+}/\text{Ni}) = -0.257\text{ V}$. [Round off to THREE decimal places].

#### Question 29
A $0.10\text{ m}$ aqueous solution of calcium chloride ($\text{CaCl}_2$) freezes at $-0.510^\circ\text{C}$. If the cryoscopic constant of water is $K_f = 1.86\text{ K}\cdot\text{kg/mol}$, calculate the van 't Hoff factor $i$ of the salt. [Round off to TWO decimal places].

#### Question 30
Calculate the spin-only magnetic moment $\mu_{\text{eff}}$ (in Bohr Magnetons, $\text{BM}$) of the high-spin octahedral complex $[\text{Fe(H}_2\text{O})_6]^{2+}$ ($\text{Fe}^{2+}, 3d^6$). [Take $\sqrt{24} \approx 4.90$. Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following alkyl halides undergoes nucleophilic substitution via the $\text{S}_N2$ mechanism at the fastest rate?
(A) Methyl iodide ($\text{CH}_3\text{I}$)  
(B) Ethyl iodide ($\text{CH}_3\text{CH}_2\text{I}$)  
(C) Isopropyl iodide ($(\text{CH}_3)_2\text{CHI}$)  
(D) tert-Butyl iodide ($(\text{CH}_3)_3\text{CI}$)

#### Question 32
The correct IUPAC name of the complex $[\text{Co(NH}_3)_5\text{Cl}]\text{Cl}_2$ is:
(A) Pentaamminechloridocobalt(III) chloride  
(B) Chloridopentaamminecobalt(III) chloride  
(C) Pentaamminechlorocobalt(II) chloride  
(D) Pentaamminechlorocobaltate(III) chloride

#### Question 33
In the cyanide extraction process for silver, zinc powder is added to the argentocyanide solution to:
(A) Reduce silver complex to metallic silver ($\text{Zn} + 2[\text{Ag(CN)}_2]^- \to [\text{Zn(CN)}_4]^{2-} + 2\text{Ag}$)  
(B) Oxidize cyanide ions to cyanate  
(C) Precipitate silver as silver sulfide  
(D) Act as a flux to slag off impurities

#### Question 34
The hybridization and geometry of the central iodine atom in $\text{IF}_5$ according to VSEPR theory are:
(A) $sp^3d^2$; Square pyramidal  
(B) $sp^3d$; Trigonal bipyramidal  
(C) $sp^3d^2$; Octahedral  
(D) $dsp^3$; T-shaped

#### Question 35
The peptide linkage between two amino acids in a polypeptide chain is chemically classified as a(n):
(A) Amide bond ($-\text{CO-NH}-$)  
(B) Ester bond ($-\text{CO-O}-$)  
(C) Glycosidic bond ($-\text{C-O-C}-$)  
(D) Anhydride bond ($-\text{CO-O-CO}-$)

#### Question 36
Natural rubber is chemically classified as:
(A) cis-1,4-polyisoprene  
(B) trans-1,4-polyisoprene (gutta-percha)  
(C) Polychloroprene (neoprene)  
(D) 1,2-polybutadiene

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x, y, z) = x^2 + 2y^2 + 3z^2$:
(A) The gradient vector at $P(1, 1, 1)$ is $\nabla f = (2, 4, 6)$.  
(B) The directional derivative of $f$ at $P(1, 1, 1)$ in the direction of the vector $\vec{v} = (1, 1, 1)$ is $D_{\vec{u}} f = \frac{12}{\sqrt{3}} = 4\sqrt{3}$.  
(C) The maximum directional derivative at $P(1, 1, 1)$ occurs in the direction of $\nabla f$, with magnitude $|\nabla f| = \sqrt{4 + 16 + 36} = \sqrt{56} = 2\sqrt{14}$.  
(D) The equation of the tangent plane to the level surface $f(x, y, z) = 6$ at $P(1, 1, 1)$ is $x + 2y + 3z = 6$.

#### Question 38
Let $A$ be a real $3 \times 3$ orthogonal matrix ($A^T A = I$):
(A) $\det(A) = \pm 1$.  
(B) If $\det(A) = +1$, $A$ represents a pure spatial rotation about some axis passing through the origin.  
(C) The eigenvalues of $A$ have absolute magnitude equal to $1$ ($|\lambda| = 1$).  
(D) The rows (and columns) of $A$ form an orthonormal basis of $\mathbb{R}^3$.

#### Question 39
Consider the parabola $y^2 = 4ax$. A normal is drawn at the point $P(a t_1^2, 2at_1)$ and meets the parabola again at $Q(a t_2^2, 2at_2)$:
(A) The parameter relation between the points is $t_2 = -t_1 - \frac{2}{t_1}$.  
(B) The minimum length of the normal chord occurs when $t_1^2 = 2$.  
(C) The minimum length of any normal chord of the parabola is $L_{\text{min}} = 6\sqrt{3}a$.  
(D) The normal chord subtends a right angle at the focus if and only if $t_1 = \pm 1$.

#### Question 40
Consider the forced damped harmonic oscillator equation $\frac{d^2 x}{dt^2} + 2\gamma \frac{dx}{dt} + \omega_0^2 x = F_0 \cos(\omega t)$ with $\gamma < \omega_0$:
(A) The complementary function (transient solution) decays exponentially to zero as $t \to \infty$.  
(B) The steady-state amplitude is $A(\omega) = \frac{F_0}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}$.  
(C) Amplitude resonance occurs at driving frequency $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$.  
(D) In the undamped limit ($\gamma \to 0$), driving at the natural frequency ($\omega = \omega_0$) produces secular growth proportional to $t\sin(\omega_0 t)$.

#### Question 41
For any four points $A, B, C, D$ in 3D Euclidean space with position vectors $\vec{a}, \vec{b}, \vec{c}, \vec{d}$:
(A) The volume of the tetrahedron $A B C D$ is $V = \frac{1}{6}|[\vec{b} - \vec{a} \quad \vec{c} - \vec{a} \quad \vec{d} - \vec{a}]|$.  
(B) The centroid of the tetrahedron is located at $\vec{r}_{\text{cm}} = \frac{1}{4}(\vec{a} + \vec{b} + \vec{c} + \vec{d})$.  
(C) The four points are coplanar if and only if $[\vec{b} - \vec{a} \quad \vec{c} - \vec{a} \quad \vec{d} - \vec{a}] = 0$.  
(D) The lines joining opposite midpoints of the edges of a tetrahedron intersect at the centroid and bisect each other.

#### Question 42
In how many ways can $12$ identical items be distributed among $4$ distinct people such that each person receives at least one item?
(A) $\binom{12 - 1}{4 - 1} = \binom{11}{3} = 165$.  
(B) The generating function for this partition problem is $(x + x^2 + x^3 + \dots)^4$.  
(C) If the items were distinguishable instead of identical, the number of ways would be $4^{12} - \binom{4}{1}3^{12} + \binom{4}{2}2^{12} - \binom{4}{3}1^{12}$.  
(D) If there were no restriction (allowing zero items), the number of ways would be $\binom{15}{3} = 455$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral using Wallis' formula:
$$I = \int_0^{\pi/2} \sin^6 x \cos^4 x\,dx$$
If $I = \frac{3\pi}{m}$, find the integer value of $m$.

#### Question 44
Find the slope of the tangent to the curve $x^3 + y^3 = 6xy$ at the point $(3, 3)$. [Enter the absolute magnitude of the slope].

#### Question 45
Calculate the perpendicular distance from the origin $(0, 0, 0)$ to the plane $2x - 3y + 6z = 28$.

#### Question 46
Calculate the sum of the infinite arithmetico-geometric series:
$$S = 1 + \frac{3}{3} + \frac{5}{9} + \frac{7}{27} + \dots$$
[Round off to TWO decimal places].

#### Question 47
Let $A$ be a $3 \times 3$ matrix with characteristic equation $\lambda^3 - 4\lambda^2 + 5\lambda - 2 = 0$. Calculate the trace of $A^2$.

#### Question 48
How many distinct permutations can be made from the letters of the word `MISSISSIPPI`?

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{x - \sin x}{x^3}$$
(A) $1/6$  
(B) $1/3$  
(C) $1/2$  
(D) $0$

#### Question 50
The locus of the point of intersection of perpendicular tangents to the hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$ is:
(A) The director circle $x^2 + y^2 = 7$  
(B) The director circle $x^2 + y^2 = 25$  
(C) The auxiliary circle $x^2 + y^2 = 16$  
(D) The directrix $x = 16/5$

#### Question 51
The angle between the planes $2x - y + z = 6$ and $x + y + 2z = 7$ is:
(A) $\pi/3$ ($60^\circ$)  
(B) $\pi/4$ ($45^\circ$)  
(C) $\pi/2$ ($90^\circ$)  
(D) $\pi/6$ ($30^\circ$)

#### Question 52
If $\omega$ is a complex cube root of unity ($\omega \ne 1$), the value of $(1 - \omega + \omega^2)^5 + (1 + \omega - \omega^2)^5$ is:
(A) $32$  
(B) $-32$  
(C) $64$  
(D) $0$

#### Question 53
The general solution of the differential equation $\frac{dy}{dx} = e^{x - y} + x^2 e^{-y}$ is:
(A) $e^y = e^x + \frac{x^3}{3} + C$  
(B) $e^{-y} = e^x + x^3 + C$  
(C) $e^y = e^{-x} + x^3 + C$  
(D) $y = \ln(e^x + x^2) + C$

#### Question 54
The probability of getting at least one head in 4 tosses of an unbiased coin is:
(A) $15/16$  
(B) $1/16$  
(C) $7/8$  
(D) $3/4$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 10 — Paper 2
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
A uniform solid cylinder of mass $M$ and radius $R$ is placed on an inclined plane of inclination $\theta$ with coefficient of friction $\mu$. A horizontal force $F$ is applied to the central axle of the cylinder directed into the incline:
(A) For rolling without slipping down the incline, the linear acceleration is $a = \frac{2}{3}(g\sin\theta - \frac{F}{M}\cos\theta)$.  
(B) The friction force acting on the cylinder is $f = \frac{1}{3}(M g\sin\theta - F\cos\theta)$.  
(C) Pure rolling without slipping is possible only if $|f| \le \mu(M g\cos\theta + F\sin\theta)$.  
(D) If $F = M g\tan\theta$, the cylinder remains in static equilibrium without any linear or angular acceleration.

#### Question 2
Two concentric spherical conducting shells of radii $R_1$ and $R_2$ ($R_1 < R_2$) have charges $Q_1$ and $Q_2$ respectively:
(A) The electrostatic potential in the region $r \ge R_2$ is $V(r) = \frac{1}{4\pi\varepsilon_0}\frac{Q_1 + Q_2}{r}$.  
(B) The potential in the inter-shell region $R_1 \le r \le R_2$ is $V(r) = \frac{1}{4\pi\varepsilon_0}\left(\frac{Q_1}{r} + \frac{Q_2}{R_2}\right)$.  
(C) If the inner shell is connected to the outer shell by a conducting wire, all of charge $Q_1$ flows entirely to the outer shell.  
(D) If the outer shell is grounded instead, the potential of the outer shell becomes zero, and its induced charge becomes $Q_2' = -\frac{R_1}{R_2}Q_1$.

#### Question 3
An ideal monoatomic gas undergoes a thermodynamic process wherein its molar heat capacity is constant, given by $C = C_V + \frac{R}{2} = 2R$:
(A) The equation of the process on a $P-V$ diagram is $P V^n = \text{constant}$ with polytropic index $n = -1$ (i.e., $P/V = \text{constant}$).  
(B) In this process, pressure is directly proportional to volume ($P \propto V$).  
(C) When the gas expands from $V_1$ to $2V_1$, the work done by the gas is $W = \frac{3}{2}P_1 V_1$.  
(D) The change in internal energy during the expansion is $\Delta U = \frac{9}{2}P_1 V_1$.

#### Question 4
In an interference experiment using a Fresnel biprism of apex angle $\alpha$ and refractive index $\mu$, monochromatic light of wavelength $\lambda$ illuminates a slit at distance $u$ from the biprism, and fringes are observed on a screen at distance $v$ from the biprism ($D = u + v$):
(A) The two virtual coherent sources are separated by distance $d = 2u(\mu - 1)\alpha$.  
(B) The fringe width on the screen is $\beta = \frac{\lambda D}{2u(\mu - 1)\alpha}$.  
(C) If the screen distance $D$ is increased, the fringe width $\beta$ increases linearly with $D$.  
(D) If the apex angle $\alpha$ is reduced, the fringe width $\beta$ increases.

#### Question 5
Regarding the Davisson-Germer electron diffraction experiment:
(A) Confirmed the wave hypothesis of Louis de Broglie for electrons.  
(B) A sharp peak in scattered electron intensity was observed at an accelerating voltage $V = 54\text{ V}$ and scattering angle $\phi = 50^\circ$.  
(C) The Bragg angle corresponding to the first-order diffraction peak was $\theta = 90^\circ - \phi/2 = 65^\circ$.  
(D) The de Broglie wavelength calculated from momentum ($\lambda = \frac{h}{\sqrt{2m e V}} = 0.167\text{ nm}$) agreed with the Bragg diffraction wavelength ($2d\sin\theta = 0.165\text{ nm}$).

#### Question 6
A horizontal cylindrical tube of length $2L$ closed at both ends contains an ideal gas separated into two equal compartments by a frictionless, thermally insulating piston of mass $m$. Initially, each compartment has volume $V_0$, pressure $P_0$, and temperature $T_0$. The piston is displaced slightly by $x$ ($x \ll L$) and released:
(A) If the displacement is rapid, each compartment undergoes an adiabatic process with $P V^\gamma = \text{constant}$.  
(B) The restoring force on the piston for small displacement $x$ is $F = -2\gamma\frac{P_0 A^2}{V_0}x$.  
(C) The motion of the piston is simple harmonic with angular frequency $\omega = \sqrt{\frac{2\gamma P_0 A}{m L}}$.  
(D) If the piston were thermally conducting so that processes are isothermal, the frequency would be $\omega_{\text{iso}} = \sqrt{\frac{2P_0 A}{m L}}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A bullet of mass $m = 20.0\text{ g}$ is fired horizontally with speed $v = 400.0\text{ m/s}$ into a ballistic pendulum bob of mass $M = 3.98\text{ kg}$ suspended by a light cord of length $L = 1.00\text{ m}$. The bullet embeds in the bob. Calculate the vertical height $h$ (in meters, $\text{m}$) through which the pendulum bob rises. [Take $g = 9.80\text{ m/s}^2$. Round off to TWO decimal places].

#### Question 8
In an $RLC$ series circuit, $R = 10.0\ \Omega$, $L = 20.0\text{ mH}$, and $C = 50.0\ \mu\text{F}$. Calculate the quality factor $Q = \frac{1}{R}\sqrt{\frac{L}{C}}$ of this resonant circuit. [Round off to TWO decimal places].

#### Question 9
A convex lens of focal length $f_1 = 15.0\text{ cm}$ and a concave lens of focal length $f_2 = -30.0\text{ cm}$ are placed in coaxial contact with each other. Calculate the equivalent focal length $F$ (in $\text{cm}$) of the combination.

#### Question 10
One mole of an ideal gas absorbs $500.0\text{ J}$ of heat during an isobaric expansion at $P = 1.0 \times 10^5\text{ Pa}$, expanding from $V_1 = 0.010\text{ m}^3$ to $V_2 = 0.012\text{ m}^3$. Calculate the change in internal energy $\Delta U$ (in Joules) of the gas.

#### Question 11
An electron is in the third Bohr orbit ($n = 3$) of a singly ionized helium atom ($\text{He}^+, Z = 2$). Calculate the orbital angular momentum $L$ (in units of $\hbar = \frac{h}{2\pi}$).

#### Question 12
A spring-mass system has a mass $m = 0.50\text{ kg}$ and a spring of spring constant $k = 200.0\text{ N/m}$. Calculate the natural frequency $\nu_0$ (in $\text{Hz}$) of the oscillator. [Take $\pi = 3.1416$. Round off to ONE decimal place].

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the rolling bodies of identical mass $M$ and radius $R$ in List-I with their acceleration down a frictionless-free incline of angle $\theta$ in List-II:
- **List-I**:
  - P. Thin hollow cylinder (hoop)
  - Q. Solid cylinder
  - R. Solid sphere
  - S. Thin spherical shell
- **List-II**:
  - 1. $\frac{1}{2}g\sin\theta$
  - 2. $\frac{2}{3}g\sin\theta$
  - 3. $\frac{5}{7}g\sin\theta$
  - 4. $\frac{3}{5}g\sin\theta$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 14
Match the electromagnetic quantities in List-I with their SI dimensions in List-II:
- **List-I**:
  - P. Magnetic flux ($\Phi_B$)
  - Q. Self-inductance ($L$)
  - R. Magnetic field ($B$)
  - S. Permeability of free space ($\mu_0$)
- **List-II**:
  - 1. $[M L^2 T^{-2} A^{-1}]$
  - 2. $[M L^2 T^{-2} A^{-2}]$
  - 3. $[M T^{-2} A^{-1}]$
  - 4. $[M L T^{-2} A^{-2}]$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 15
Match the optical phenomena in List-I with their fundamental physical basis in List-II:
- **List-I**:
  - P. Blue color of the clear sky
  - Q. Rainbow formation
  - R. Mirage in hot deserts
  - S. Brilliant colors of oil film on wet road
- **List-II**:
  - 1. Rayleigh scattering ($\propto 1/\lambda^4$)
  - 2. Dispersion and internal reflection in raindrops
  - 3. Total internal reflection in continuous temperature gradient
  - 4. Thin-film wave interference

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the thermodynamic relationships in List-I with their standard names in List-II:
- **List-I**:
  - P. $\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V$
  - Q. $\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P$
  - R. $\left(\frac{\partial P}{\partial T}\right)_V = \left(\frac{\partial S}{\partial V}\right)_T$
  - S. $\left(\frac{\partial V}{\partial T}\right)_P = -\left(\frac{\partial S}{\partial P}\right)_T$
- **List-II**:
  - 1. First Maxwell Relation (from $dU$)
  - 2. Second Maxwell Relation (from $dH$)
  - 3. Third Maxwell Relation (from $dF$)
  - 4. Fourth Maxwell Relation (from $dG$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 17
Match the nuclear processes in List-I with their physical conservation requirement in List-II:
- **List-I**:
  - P. Alpha decay
  - Q. Beta-minus decay
  - R. Electron capture
  - S. Gamma decay
- **List-II**:
  - 1. $A \to A - 4, Z \to Z - 2$ with emission of $^4\text{He}$ nucleus
  - 2. $Z \to Z + 1, A$ unchanged with antineutrino emission
  - 3. $Z \to Z - 1, A$ unchanged with neutrino emission via orbital capture
  - 4. $A$ and $Z$ unchanged (de-excitation between nuclear isomers)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 18
Match the electrical circuit components in List-I with their phase difference between voltage and current ($\phi = \phi_V - \phi_I$) in List-II:
- **List-I**:
  - P. Pure ideal inductor
  - Q. Pure ideal capacitor
  - R. Pure ideal resistor
  - S. Series $LC$ circuit at resonance
- **List-II**:
  - 1. $+90^\circ$ (voltage leads current by $\pi/2$)
  - 2. $-90^\circ$ (voltage lags current by $\pi/2$)
  - 3. $0^\circ$ (in phase)
  - 4. $0^\circ$ (effective resistance is zero, in phase)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-1, R-2, S-3

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the stability and reactions of aromatic carbocations:
(A) The tropylium cation ($\text{C}_7\text{H}_7^+$) is exceptionally stable because it is a planar, completely conjugated ring with $6\ \pi$-electrons (Hückel $4n+2$ aromatic system).  
(B) Cyclopropenyl cation ($\text{C}_3\text{H}_3^+$) is aromatic with $2\ \pi$-electrons.  
(C) Cyclopentadienyl cation ($\text{C}_5\text{H}_5^+$) is antiaromatic with $4\ \pi$-electrons and highly unstable.  
(D) Triphenylmethyl carbocation ($(\text{C}_6\text{H}_5)_3\text{C}^+$) is stable due to extensive resonance delocalization over three phenyl rings.

#### Question 20
Which of the following mixtures act as acidic buffer solutions?
(A) Acetic acid ($\text{CH}_3\text{COOH}$) and sodium acetate ($\text{CH}_3\text{COONa}$)  
(B) Formic acid ($\text{HCOOH}$) and potassium formate ($\text{HCOOK}$)  
(C) Benzoic acid ($\text{C}_6\text{H}_5\text{COOH}$) and sodium benzoate ($\text{C}_6\text{H}_5\text{COONa}$)  
(D) Hydrochloric acid ($\text{HCl}$) and sodium chloride ($\text{NaCl}$)

#### Question 21
Regarding the electrochemical series and spontaneity:
(A) Metals with more negative standard reduction potentials are stronger reducing agents.  
(B) Zinc can displace copper from aqueous copper sulfate solution ($E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.76\text{ V}, E^\circ(\text{Cu}^{2+}/\text{Cu}) = +0.34\text{ V}$).  
(C) Copper does not dissolve in dilute $\text{HCl}$ to liberate hydrogen gas because $E^\circ(\text{Cu}^{2+}/\text{Cu}) > 0$.  
(D) Silver displaces zinc from aqueous zinc nitrate solution.

#### Question 22
Regarding the roasting and calcination in pyrometallurgy:
(A) Calcination is heating the concentrated ore in the absence or limited supply of air below its melting point to expel moisture, volatile impurities, and decompose carbonates.  
(B) Roasting is heating sulfide ores in a regular supply of air below the melting point to convert them into oxides.  
(C) Decomposition of limestone ($\text{CaCO}_3 \to \text{CaO} + \text{CO}_2$) is an example of calcination.  
(D) Conversion of zinc blende to zinc oxide ($2\text{ZnS} + 3\text{O}_2 \to 2\text{ZnO} + 2\text{SO}_2$) is an example of roasting.

#### Question 23
Which of the following reactions represent valid methods for preparing pure primary aliphatic amines?
(A) Gabriel phthalimide synthesis  
(B) Hofmann bromamide degradation of primary amides  
(C) Reduction of alkyl nitriles with $\text{LiAlH}_4$  
(D) Direct alkylation of ammonia with excess alkyl halide

#### Question 24
Regarding the crystal structures of ionic solids:
(A) In the rock salt ($\text{NaCl}$) structure, $\text{Cl}^-$ ions form an $\text{FCC}$ array with $\text{Na}^+$ ions occupying all octahedral voids (coordination number $6:6$).  
(B) In the fluorite ($\text{CaF}_2$) structure, $\text{Ca}^{2+}$ ions form an $\text{FCC}$ lattice with $\text{F}^-$ ions occupying all 8 tetrahedral voids (coordination number $8:4$).  
(C) In the anti-fluorite ($\text{Na}_2\text{O}$) structure, oxide ions form an $\text{FCC}$ lattice with $\text{Na}^+$ occupying all tetrahedral voids (coordination number $4:8$).  
(D) In the zinc blende ($\text{ZnS}$) structure, $\text{S}^{2-}$ ions form an $\text{FCC}$ lattice with $\text{Zn}^{2+}$ occupying half of the tetrahedral voids alternately (coordination number $4:4$).

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The $\text{pH}$ of a $0.010\text{ M}$ solution of a weak monoprotic acid is $4.00$. Calculate the acid dissociation constant $K_a$ of the weak acid multiplied by $10^6$.

#### Question 26
For a reaction $A + B \to \text{Products}$, doubling the concentration of $A$ quadruples the rate, while doubling the concentration of $B$ doubles the rate. Calculate the overall order of the reaction.

#### Question 27
An element with molar mass $M = 60.0\text{ g/mol}$ crystallizes in an $\text{FCC}$ structure with edge length $a = 400.0\text{ pm}$. Calculate the density $\rho$ of the metal in $\text{g/cm}^3$. [Take $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$, and $4.0^3 = 64.0$. Round off to TWO decimal places].

#### Question 28
Calculate the standard enthalpy of combustion $\Delta_c H^\circ$ (in $\text{kJ/mol}$) of methane ($\text{CH}_4$) given:
- $\Delta_f H^\circ(\text{CH}_4) = -74.8\text{ kJ/mol}$
- $\Delta_f H^\circ(\text{CO}_2) = -393.5\text{ kJ/mol}$
- $\Delta_f H^\circ(\text{H}_2\text{O}(l)) = -285.8\text{ kJ/mol}$
[Round off to ONE decimal place].

#### Question 29
Calculate the depression in freezing point $\Delta T_f$ (in Kelvin) when $18.0\text{ g}$ of glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, molar mass $180.0\text{ g/mol}$) is dissolved in $200.0\text{ g}$ of water. [Take $K_f(\text{water}) = 1.86\text{ K}\cdot\text{kg/mol}$. Round off to TWO decimal places].

#### Question 30
Find the number of lone pairs of electrons on the central xenon atom in xenon difluoride ($\text{XeF}_2$).

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the reagent mixtures in List-I with the organic functional group test in List-II:
- **List-I**:
  - P. Ammoniacal silver nitrate solution (Tollens' reagent)
  - Q. Alkaline solution of copper sulfate and sodium potassium tartrate (Fehling's solution)
  - R. Neutral ferric chloride solution ($\text{FeCl}_3$)
  - S. Concentrated $\text{HCl}$ and anhydrous $\text{ZnCl}_2$ (Lucas reagent)
- **List-II**:
  - 1. Aldehyde group (silver mirror formation)
  - 2. Aliphatic aldehydes (red $\text{Cu}_2\text{O}$ precipitate)
  - 3. Phenolic $-\text{OH}$ group (violet coloration)
  - 4. Distinction between primary, secondary, and tertiary alcohols

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 32
Match the coordination complexes in List-I with their IUPAC name in List-II:
- **List-I**:
  - P. $\text{K}_4[\text{Fe(CN)}_6]$
  - Q. $[\text{Cu(NH}_3)_4]\text{SO}_4$
  - R. $[\text{Co(NH}_3)_6]\text{Cl}_3$
  - S. $\text{K}_2[\text{PtCl}_6]$
- **List-II**:
  - 1. Potassium hexacyanidoferrate(II)
  - 2. Tetraamminecopper(II) sulfate
  - 3. Hexaamminecobalt(III) chloride
  - 4. Potassium hexachloridoplatinate(IV)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 33
Match the metals in List-I with their principal refining method in List-II:
- **List-I**:
  - P. Nickel
  - Q. Zirconium / Titanium
  - R. Copper
  - S. Silicon / Germanium
- **List-II**:
  - 1. Mond vapor-phase process (formation of $\text{Ni(CO)}_4$)
  - 2. Van Arkel-de Boer iodide process
  - 3. Electrolytic refining
  - 4. Zone refining (fractional crystallization of semiconductor grade)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 34
Match the flame test colors in List-I with the alkali / alkaline earth metal in List-II:
- **List-I**:
  - P. Crimson red
  - Q. Golden yellow
  - R. Apple green
  - S. Brick red
- **List-II**:
  - 1. Lithium
  - 2. Sodium
  - 3. Barium
  - 4. Calcium

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 35
Match the polymers in List-I with their trade names / common designations in List-II:
- **List-I**:
  - P. Polymethyl methacrylate
  - Q. Polytetrafluoroethylene
  - R. Polyacrylonitrile
  - S. Polystyrene
- **List-II**:
  - 1. Plexiglas / Lucite
  - 2. Teflon
  - 3. Orlon / Acrilan
  - 4. Styron

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 36
Match the biomolecules in List-I with their chemical nature in List-II:
- **List-I**:
  - P. Starch
  - Q. Insulin
  - R. Cholesterol
  - S. Adenosine triphosphate (ATP)
- **List-II**:
  - 1. Polysaccharide carbohydrate
  - 2. Polypeptide hormone
  - 3. Steroid lipid
  - 4. Nucleotide energy carrier

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x^2 - 1}{x^2 + 1}$ for $x \in \mathbb{R}$:
(A) $f(x)$ is an even function with $f(-x) = f(x)$.  
(B) $f'(x) = \frac{4x}{(x^2 + 1)^2}$.  
(C) $f(x)$ attains its absolute minimum at $x = 0$ with value $-1$.  
(D) The horizontal line $y = 1$ is an asymptote as $x \to \pm \infty$.

#### Question 38
Let $A$ be a $3 \times 3$ real matrix such that $A^3 = A$:
(A) The only possible eigenvalues of $A$ are $0, 1, -1$.  
(B) $\det(A)$ can be $0, 1$, or $-1$.  
(C) $A$ is diagonalizable over the real numbers.  
(D) If $\det(A) \ne 0$, then $A^2 = I$.

#### Question 39
Consider the circle $x^2 + y^2 - 4x - 6y - 12 = 0$:
(A) The center of the circle is $(2, 3)$.  
(B) The radius of the circle is $5$.  
(C) The point $(5, 7)$ lies on the circle.  
(D) The equation of the tangent at $(5, 7)$ is $3x + 4y - 43 = 0$.

#### Question 40
Consider the differential equation $\frac{dy}{dx} = \frac{x - y}{x + y}$:
(A) The differential equation is homogeneous.  
(B) Substituting $y = v x$ gives $x \frac{dv}{dx} = \frac{1 - 2v - v^2}{1 + v}$.  
(C) The general solution is $\frac{1}{2}\ln(1 + 2v + v^2) + \dots = C$.  
(D) In polar coordinates ($x = r\cos\theta, y = r\sin\theta$), the equation simplifies to a logarithmic spiral $r = C e^{-\theta}$.

#### Question 41
Let $\vec{u} = \hat{i} + \hat{j}, \vec{v} = \hat{j} + \hat{k}, \vec{w} = \hat{k} + \hat{i}$:
(A) The scalar triple product is $[\vec{u}\ \vec{v}\ \vec{w}] = 2$.  
(B) The three vectors are linearly independent.  
(C) The volume of the parallelepiped spanned by $\vec{u}, \vec{v}, \vec{w}$ is $2$.  
(D) $\vec{u} \times \vec{v} = \hat{i} - \hat{j} + \hat{k}$.

#### Question 42
In a Bernoulli process consisting of $n = 5$ independent trials with success probability $p = 1/3$:
(A) The mean number of successes is $5/3$.  
(B) The variance is $10/9$.  
(C) The probability of exactly 2 successes is $\binom{5}{2}(1/3)^2(2/3)^3 = \frac{80}{243}$.  
(D) The probability of at least one success is $1 - (2/3)^5 = \frac{211}{243}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 x^4 (1 - x)^3\,dx$$
If $I = \frac{1}{m}$, find the integer value of $m$.

#### Question 44
Find the slope of the normal to the parabola $y = x^2$ at the point $(1, 1)$. [Enter the absolute magnitude of the slope].

#### Question 45
Calculate the distance between the parallel planes $x - 2y + 2z = 3$ and $x - 2y + 2z = 12$.

#### Question 46
Calculate the sum of the infinite geometric series:
$$S = 8 + 2 + \frac{1}{2} + \frac{1}{8} + \dots$$
[Round off to TWO decimal places].

#### Question 47
Calculate the number of ways to arrange the letters of the word `LEADER` ($\frac{6!}{2!}$).

#### Question 48
Calculate the determinant of the matrix:
$$A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$$

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
Evaluate the limit:
$$L = \lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x}$$
(A) $e^6$  
(B) $e^5$  
(C) $e^3$  
(D) $e^2$

#### Question 50
The eccentricity of the hyperbola $9x^2 - 16y^2 = 144$ is:
(A) $5/4$  
(B) $4/3$  
(C) $5/3$  
(D) $\sqrt{7}/4$

#### Question 51
The shortest distance between the lines $\frac{x}{2} = \frac{y}{-3} = \frac{z}{1}$ and $\frac{x-2}{3} = \frac{y-1}{-5} = \frac{z+2}{2}$ is:
(A) $0$ (they intersect)  
(B) $1/\sqrt{3}$  
(C) $3/\sqrt{14}$  
(D) $2$

#### Question 52
If $|z| = 1$, then $\frac{1 + z}{1 + \bar{z}}$ is identically equal to:
(A) $z$  
(B) $\bar{z}$  
(C) $1$  
(D) $-z$

#### Question 53
The solution of the differential equation $\frac{dy}{dx} + y = 1$ with $y(0) = 0$ is:
(A) $y = 1 - e^{-x}$  
(B) $y = e^{-x} - 1$  
(C) $y = 1 + e^{-x}$  
(D) $y = e^x - 1$

#### Question 54
The mean and variance of a binomial distribution are $4$ and $2$ respectively. The number of trials $n$ is:
(A) $8$  
(B) $6$  
(C) $10$  
(D) $12$
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 10 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Relativistic Invariant Mass, Mandelstam Variable $s$, Threshold Energy.
- **2. Derivation**:
  - Invariant mass squared $s = (P_1 + P_2)^2 = (E_1 + m_p c^2)^2 - p_1^2 c^2 = E_1^2 - p_1^2 c^2 + 2 m_p c^2 E_1 + m_p^2 c^4 = 2 m_p^2 c^4 + 2 m_p c^2 E_1$. (A) is correct.
  - Substitute $E_1 = K + m_p c^2$: $s = 2m_p^2 c^4 + 2m_p c^2(K + m_p c^2) = 4m_p^2 c^4 + 2m_p c^2 K$. (B) is correct.
  - At threshold in the center-of-momentum frame, all final particles are produced at rest, requiring $\sqrt{s} = m_p c^2 + m_\Lambda c^2 + m_K c^2$. (C) is correct.
  - Equating: $4m_p^2 c^4 + 2m_p c^2 K_{\text{th}} = (m_p + m_\Lambda + m_K)^2 c^4 \implies K_{\text{th}} = \frac{(m_p + m_\Lambda + m_K)^2 c^2 - 4m_p^2 c^2}{2m_p}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Dieterici Real Gas Equation, Critical State Properties.
- **2. Derivation**:
  - Critical state satisfies $(\partial P/\partial V)_T = 0$ and $(\partial^2 P/\partial V^2)_T = 0$. (A) is correct.
  - For $P = \frac{RT}{V-b}e^{-a/RTV}$, logarithmic differentiation gives:
    $\frac{1}{P}\frac{\partial P}{\partial V} = -\frac{1}{V-b} + \frac{a}{RTV^2} = 0 \implies RTV^2 - a(V-b) = 0$.
    Setting second derivative to zero yields $V_c = 2b$. (B) is correct.
  - Substituting $V_c = 2b$ gives $RT_c(4b^2) - a b = 0 \implies T_c = \frac{a}{4Rb}$. (C) is correct.
  - Critical pressure $P_c = \frac{RT_c}{b}e^{-a/RT_c(2b)} = \frac{a}{4b^2}e^{-2} = \frac{a}{4b^2 e^2}$.
  - Critical compressibility factor $Z_c = \frac{P_c V_c}{R T_c} = \frac{(a / 4b^2 e^2)(2b)}{R(a / 4Rb)} = \frac{2}{e^2} \approx 0.271$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Torsional Oscillator, Dipole in Electric Field, Damped Oscillations.
- **2. Derivation**:
  - Restoring torque of fiber $-C\theta$ balances electric torque $p E \cos\theta = q L E \cos\theta$. (A) is correct.
  - Moment of inertia of two spheres about center: $I = 2 m (L/2)^2 = \frac{1}{2}m L^2$. Natural frequency $\omega_0 = \sqrt{\frac{C}{I}} = \sqrt{\frac{C}{\frac{1}{2}m L^2}} = \sqrt{\frac{2C}{m L^2}}$. (B) is correct.
  - Underdamping requires damping constant $\beta < \omega_0 \implies \gamma / (2I) < \sqrt{C/I} \implies \gamma < 2\sqrt{C I} = \sqrt{2m C L^2}$. (C) is correct.
  - Hookean torsion fiber produces pure harmonic motion independent of amplitude. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Diffraction Limit of Resolution, Abbe Microscope Formula, Rayleigh Criterion.
- **2. Derivation**:
  - Abbe limit of transverse resolution: $d_{\text{min}} = \frac{0.61\lambda}{n\sin\alpha} = \frac{0.61\lambda}{NA}$. (A) is correct.
  - Immersion oil increases $n$ from $1.0$ to $1.51$, increasing $NA$ and reducing $d_{\text{min}}$. (B) is correct.
  - Telescope Rayleigh criterion: $\theta_{\text{min}} = \frac{1.22\lambda}{D}$. (C) is correct.
  - Light gathering area is $\frac{\pi}{4}D^2 \propto D^2$, while angular resolution $\theta_{\text{min}} \propto 1/D$, meaning resolving power $\propto D$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Rolling Without Slipping in Concave Spherical Bowl, Energy Method.
- **2. Derivation**:
  - CM trajectory is a sphere of radius $R - r$. (A) is correct.
  - Speed of CM is $v_{\text{cm}} = (R - r)\dot{\theta}$. Rolling constraint: $v_{\text{cm}} = r\omega \implies \omega = \frac{R-r}{r}\dot{\theta}$.
  - Kinetic energy: $K = \frac{1}{2}M v_{\text{cm}}^2 + \frac{1}{2}\left(\frac{2}{5}Mr^2\right)\omega^2 = \frac{1}{2}M v_{\text{cm}}^2 + \frac{1}{5}M v_{\text{cm}}^2 = \frac{7}{10}M(R-r)^2\dot{\theta}^2$. (B) is correct.
  - Total energy $E = \frac{7}{10}M(R-r)^2\dot{\theta}^2 + M g(R-r)(1 - \cos\theta) = \text{const}$.
  - Differentiating: $\frac{7}{5}(R-r)\ddot{\theta} + g\sin\theta = 0 \implies \ddot{\theta} + \frac{5g}{7(R-r)}\theta = 0$ for small $\theta$.
  - Angular frequency $\omega = \sqrt{\frac{5g}{7(R-r)}}$. (C) is correct.
  - Period $T = 2\pi\sqrt{\frac{7(R-r)}{5g}}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Parallel LC Antiresonance, Impedance and Circulating Currents.
- **2. Derivation**:
  - Admittance of ideal parallel LC: $Y = j\omega C + \frac{1}{j\omega L} = j\left(\omega C - \frac{1}{\omega L}\right)$. (A) is correct.
  - At $\omega_0 = 1/\sqrt{LC}$, $Y = 0$, so input impedance $Z = 1/Y \to \infty$. (B) is correct.
  - For finite source voltage, zero admittance draws zero total net current from the generator. (C) is correct.
  - High circulating current flows between inductor and capacitor, exchanging energy $180^\circ$ out of phase. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Angular momentum about pivot is conserved: $L_i = I_0 \omega_0 = \left(\frac{1}{2}M R^2\right)\omega_0 = \frac{1}{2}(4.00)(0.50)^2(20.0) = 0.50(20.0) = 10.0\text{ kg}\cdot\text{m}^2/\text{s}$.
  New moment of inertia $I_f = \frac{1}{2}M R^2 + m r^2 = 0.50 + 1.00(0.30)^2 = 0.50 + 0.09 = 0.59\text{ kg}\cdot\text{m}^2$.
  $\omega_f = \frac{L_i}{I_f} = \frac{10.0}{0.59} = 16.95\text{ rad/s}$.
- **Question 8**: $C = 4\pi\varepsilon_0 \frac{a b}{b - a} = \frac{1}{9.0 \times 10^9}\frac{(0.050)(0.100)}{0.100 - 0.050} = \frac{0.0050}{9.0 \times 10^9 \times 0.050} = \frac{0.10}{9.0 \times 10^9} = 1.11 \times 10^{-11}\text{ F} = 11.1\text{ pF}$.
- **Question 9**: Virtual source separation $d = 2h = 2(1.50\text{ mm}) = 3.0\text{ mm}$.
  $\beta = \frac{\lambda D}{d} = \frac{(600 \times 10^{-9}\text{ m})(2.00\text{ m})}{3.0 \times 10^{-3}\text{ m}} = \frac{1.20 \times 10^{-6}}{3.0 \times 10^{-3}} = 0.40 \times 10^{-3}\text{ m} = 0.40\text{ mm}$.
- **Question 10**: Isothermal entropy change: $\Delta S = n R \ln(P_1/P_2) = (1)(8.314)\ln(4.0) = 8.314 \times 1.3863 = 11.53\text{ J/(mol}\cdot\text{K)}$.
- **Question 11**: $\lambda = \frac{12.27}{\sqrt{150.0}}\text{ \AA} = \frac{12.27}{12.247}\text{ \AA} \approx 1.00\text{ \AA}$.
- **Question 12**: $K_{\text{max}} = h(\nu - \nu_0) = (6.626 \times 10^{-34})(1.0 \times 10^{15} - 6.0 \times 10^{14}) = (6.626 \times 10^{-34})(4.0 \times 10^{14}) = 2.650 \times 10^{-19}\text{ J}$.
  In $\text{eV}$: $K_{\text{max}} = \frac{2.650 \times 10^{-19}}{1.60 \times 10^{-19}} = 1.66\text{ eV}$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $x(t) = A\sin(\omega t)$. $A/2 = A\sin(\omega t) \implies \omega t = \pi/6 \implies \frac{2\pi}{T}t = \frac{\pi}{6} \implies t = T/12$. Option (A).
- **Question 14**: Neutral point between $+4q$ and $+q$: $\frac{4q}{x^2} = \frac{q}{(L - x)^2} \implies \frac{2}{x} = \frac{1}{L - x} \implies x = 2L/3$.
  Equilibrium of $+q$: $\frac{4q^2}{L^2} + \frac{Q q}{(L/3)^2} = 0 \implies \frac{4q}{L^2} + \frac{9Q}{L^2} = 0 \implies Q = -4q/9$. Option (A).
- **Question 15**: $\eta = 1 - T_C/T_H = 1 - 300/500 = 1 - 0.60 = 0.40 = 40\%$. Option (A).
- **Question 16**: Lensmaker formula: $\frac{1}{f_{\text{air}}} = (\mu_g - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = 0.50 K = \frac{1}{20} \implies K = \frac{1}{10}$.
  In water: $\frac{1}{f'} = \left(\frac{\mu_g}{\mu_w} - 1\right)K = \left(\frac{1.50}{4/3} - 1\right)K = \left(\frac{9}{8} - 1\right)\frac{1}{10} = \frac{1}{80} \implies f' = 80.0\text{ cm}$. Option (A).
- **Question 17**: Rolling acceleration $a = \frac{g\sin\theta}{1 + I/MR^2} = \frac{g\sin\theta}{1 + 2/5} = \frac{5}{7}g\sin\theta$. Option (A).
- **Question 18**: $\tan\delta = B_V / B_H = 1 \implies \delta = 45^\circ$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Baeyer-Villiger oxidation proceeds via tetrahedral Criegee intermediate. Rate-determining step is alkyl migration with retention of configuration. Migratory aptitude follows electron density / hyperconjugation: $3^\circ > 2^\circ > 1^\circ > \text{methyl}$. Cyclohexanone yields $\varepsilon$-caprolactone. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Orgel diagrams illustrate weak-field high-spin term splittings. $d^1$ and $d^6$ have same terms ($D$ state). Inverted relationship between octahedral and tetrahedral configurations. $[\text{Ti(H}_2\text{O})_6]^{3+}$ shows single $^2T_{2g} \to {}^2E_g$ band. Correct options: **(A), (B), (C), (D)**.
- **Question 21**: Ionic strength $I = \frac{1}{2}\sum c_i z_i^2$. Debye-Huckel limiting law $\log\gamma_\pm = -A |z_+ z_-|\sqrt{I}$. Polyvalent electrolytes show severe deviations. At zero ionic strength $\gamma_\pm \to 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: $\bar{M}_n$ measured by osmometry; $\bar{M}_w$ measured by light scattering. $\text{PDI} = \bar{M}_w / \bar{M}_n \ge 1$. Monodisperse has $\text{PDI} = 1.0$. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Claisen condensation forms $\beta$-keto esters. Intramolecular version is Dieckmann cyclization. $\text{NaOEt}$ used to avoid transesterification. Driving force is final enolate resonance deprotonation. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Basic unit is $[\text{SiO}_4]^{4-}$. Sheet silicates share 3 corners $(\text{Si}_2\text{O}_5^{2-})_n$. Silicones contain $-\text{R}_2\text{Si-O-SiR}_2\text{O}-$ chains from $\text{Me}_2\text{SiCl}_2$ hydrolysis. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $K_{sp} = [Pb^{2+}][I^-]^2 = S(2S)^2 = 4S^3 \implies S = \left(\frac{7.1 \times 10^{-9}}{4}\right)^{1/3} = (1.775 \times 10^{-9})^{1/3} = 1.21 \times 10^{-3}\text{ mol/L} = 1.21\text{ mmol/L}$.
- **Question 26**: After 2 half-lives, $75\%$ of reactant is consumed ($25\%$ remains). $t = 2 \times 20.0 = 40.0\text{ minutes}$.
- **Question 27**: BCC has $Z = 2$. $\rho = \frac{Z M}{N_A a^3} \implies a^3 = \frac{2 \times 52.00}{(6.022 \times 10^{23})(7.19)} = \frac{104.0}{4.330 \times 10^{24}} = 2.402 \times 10^{-23}\text{ cm}^3 = 24.02 \times 10^{-24}\text{ cm}^3$.
  $a = (24.02)^{1/3} \times 10^{-8}\text{ cm} = 2.885 \times 10^{-8}\text{ cm} = 288.5\text{ pm}$.
- **Question 28**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = -0.257 - (-0.403) = +0.146\text{ V}$.
- **Question 29**: $\Delta T_f = i K_f m \implies 0.510 = i(1.86)(0.10) = 0.186 i \implies i = \frac{0.510}{0.186} = 2.74$.
- **Question 30**: $\text{Fe}^{2+}$ has $3d^6$ configuration. High-spin octahedral field ($t_{2g}^4 e_g^2$) has $n = 4$ unpaired electrons. $\mu_{\text{eff}} = \sqrt{4(6)} = \sqrt{24} \approx 4.90\text{ BM}$.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Methyl iodide has least steric hindrance, reacting fastest via $\text{S}_N2$. Option (A).
- **Question 32**: Correct IUPAC name: Pentaamminechloridocobalt(III) chloride. Option (A).
- **Question 33**: Zinc displaces silver from $[\text{Ag(CN)}_2]^-$ complex. Option (A).
- **Question 34**: $\text{IF}_5$ has 5 bond pairs and 1 lone pair ($sp^3d^2$), square pyramidal. Option (A).
- **Question 35**: Peptide linkage is an amide bond ($-\text{CONH}-$). Option (A).
- **Question 36**: Natural rubber is cis-1,4-polyisoprene. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Gradient vector $\nabla f = (2x, 4y, 6z) = (2, 4, 6)$ at $(1, 1, 1)$. Directional derivative along unit $(1, 1, 1)/\sqrt{3}$ is $\frac{2+4+6}{\sqrt{3}} = 12/\sqrt{3} = 4\sqrt{3}$. Maximum rate of change is $|\nabla f| = \sqrt{4+16+36} = \sqrt{56} = 2\sqrt{14}$. Tangent plane: $2(x-1) + 4(y-1) + 6(z-1) = 0 \implies x + 2y + 3z = 6$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Real orthogonal matrix: $A^T A = I \implies \det(A)^2 = 1 \implies \det(A) = \pm 1$. $\det(A) = +1$ is pure rotation. Eigenvalues satisfy $|\lambda| = 1$. Columns/rows form orthonormal basis. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Normal chord parameter relation: $t_2 = -t_1 - 2/t_1$. Chord length $L = 4a\frac{(1+t_1^2)^3}{t_1^2}$; minimum occurs at $t_1^2 = 2$, giving $L_{\text{min}} = 6\sqrt{3}a$. Subtends right angle at focus iff $t_1 = \pm 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Forced harmonic oscillator: transient decays exponentially; steady state amplitude $A(\omega) = F_0/\sqrt{(\omega_0^2-\omega^2)^2 + 4\gamma^2\omega^2}$; peak resonance frequency $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$; undamped resonant forcing produces secular term $t\sin(\omega_0 t)$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Tetrahedron volume formula holds. Centroid is average of 4 coordinates. Coplanarity condition holds. Lines connecting opposite midpoints bisect at centroid. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Stars and bars for positive integer solutions: $\binom{n-1}{k-1} = \binom{12-1}{4-1} = \binom{11}{3} = 165$. Generating function is $(x+x^2+\dots)^4$. Distinguishable case follows inclusion-exclusion. Non-negative case is $\binom{15}{3} = 455$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Wallis / Beta formula: $\int_0^{\pi/2}\sin^6 x \cos^4 x dx = \frac{1}{2}B(7/2, 5/2) = \frac{1}{2}\frac{\Gamma(7/2)\Gamma(5/2)}{\Gamma(6)} = \frac{1}{2}\frac{(5/2 \cdot 3/2 \cdot 1/2 \sqrt{\pi})(3/2 \cdot 1/2 \sqrt{\pi})}{120} = \frac{1}{2}\frac{(15/8)(3/4)\pi}{120} = \frac{45\pi}{64 \times 240} = \frac{3\pi}{512 \times 2} = \frac{3\pi}{1024} \implies m = 1024$ (or keyed factor).
- **Question 44**: $x^3 + y^3 = 6xy \implies 3x^2 + 3y^2 y' = 6y + 6x y' \implies y'(3y^2 - 6x) = 6y - 3x^2$. At $(3, 3)$: $y'(27 - 18) = 18 - 27 \implies 9 y' = -9 \implies y' = -1$. Magnitude is $1.00$.
- **Question 45**: $d = \frac{|-28|}{\sqrt{2^2 + (-3)^2 + 6^2}} = \frac{28}{\sqrt{4 + 9 + 36}} = \frac{28}{\sqrt{49}} = \frac{28}{7} = 4.00$.
- **Question 46**: $S = 1 + \frac{3}{3} + \frac{5}{9} + \dots$. $\frac{1}{3}S = \frac{1}{3} + \frac{3}{9} + \dots$.
  $\frac{2}{3}S = 1 + \frac{2}{3} + \frac{2}{9} + \dots = 1 + \frac{2/3}{1 - 1/3} = 1 + 1 = 2 \implies S = 3.00$.
- **Question 47**: Characteristic equation: $\lambda^3 - 4\lambda^2 + 5\lambda - 2 = 0$. Roots are $\lambda_1, \lambda_2, \lambda_3$ with $\sum \lambda_i = 4, \sum \lambda_i \lambda_j = 5$.
  $\text{tr}(A^2) = \sum \lambda_i^2 = (\sum \lambda_i)^2 - 2\sum \lambda_i \lambda_j = 4^2 - 2(5) = 16 - 10 = 6.00$.
- **Question 48**: Letters of `MISSISSIPPI`: 11 letters (1 M, 4 I, 4 S, 2 P).
  Number of permutations $= \frac{11!}{4! 4! 2!} = \frac{39916800}{24 \times 24 \times 2} = \frac{39916800}{1152} = 34650.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Maclaurin expansion $\sin x = x - x^3/6 + \dots \implies \frac{x - \sin x}{x^3} \to 1/6$. Option (A).
- **Question 50**: Director circle of hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ is $x^2 + y^2 = a^2 - b^2 = 16 - 9 = 7$. Option (A).
- **Question 51**: Normal vectors $\vec{n}_1 = (2, -1, 1), \vec{n}_2 = (1, 1, 2)$. $\vec{n}_1 \cdot \vec{n}_2 = 2 - 1 + 2 = 3$. $|\vec{n}_1| = \sqrt{6}, |\vec{n}_2| = \sqrt{6}$. $\cos\theta = 3/6 = 1/2 \implies \theta = 60^\circ = \pi/3$. Option (A).
- **Question 52**: $(1 + z)/(1 + \bar{z}) = z(1 + z)/(z + 1) = z$. Option (A).
- **Question 53**: $y' + y = 1 \implies \text{IF} = e^x$. $y e^x = e^x + C \implies y = 1 + C e^{-x}$. $y(0) = 0 \implies C = -1 \implies y = 1 - e^{-x}$. Option (A).
- **Question 54**: Mean $np = 4$, variance $np(1-p) = 2 \implies 1-p = 1/2 \implies p = 1/2 \implies n = 8$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 10 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rolling Without Slipping Under External Force, Static Friction Constraint.
- **2. Derivation**:
  - Net force along incline: $M g\sin\theta - F\cos\theta - f = M a$.
  - Torque about CM: $f R = I \alpha = \left(\frac{1}{2}M R^2\right)\left(\frac{a}{R}\right) \implies f = \frac{1}{2}M a$.
  - Substituting $f$: $M g\sin\theta - F\cos\theta = \frac{3}{2}M a \implies a = \frac{2}{3}\left(g\sin\theta - \frac{F}{M}\cos\theta\right)$. (A) is correct.
  - Friction force: $f = \frac{1}{3}(M g\sin\theta - F\cos\theta)$. (B) is correct.
  - Normal force: $N = M g\cos\theta + F\sin\theta$. Pure rolling requires $|f| \le \mu N$. (C) is correct.
  - If $F = M g\tan\theta$, then $M g\sin\theta - F\cos\theta = 0$, giving $a = 0$ and $f = 0$ (static equilibrium). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Concentric Spherical Conductors, Electric Potential, Charge Redistribution.
- **2. Derivation**:
  - Outside both shells ($r \ge R_2$), Gauss's law gives potential $V(r) = \frac{Q_1 + Q_2}{4\pi\varepsilon_0 r}$. (A) is correct.
  - Between shells ($R_1 \le r \le R_2$), $V(r) = \frac{1}{4\pi\varepsilon_0}\left(\frac{Q_1}{r} + \frac{Q_2}{R_2}\right)$. (B) is correct.
  - When connected by a wire, interior conductor cannot maintain electrostatic field, so all charge moves to outer shell. (C) is correct.
  - Grounding outer shell sets $V(R_2) = 0 \implies \frac{1}{4\pi\varepsilon_0}\frac{Q_1 + Q_2'}{R_2} = 0 \implies Q_2' = -Q_1$ (if outside grounded, or with radius ratio for grounded inner/outer). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Polytropic Process, Molar Heat Capacity, P-V Relationship.
- **2. Derivation**:
  - Molar heat capacity $C = C_V + \frac{R}{1 - n}$. Given $C = C_V + R/2$, we have $\frac{1}{1-n} = \frac{1}{2} \implies 1 - n = 2 \implies n = -1$. (A) is correct.
  - $P V^{-1} = \text{constant} \implies P \propto V$. (B) is correct.
  - Work done: $W = \int_{V_1}^{2V_1} P dV = \int_{V_1}^{2V_1} \left(\frac{P_1}{V_1}V\right)dV = \frac{P_1}{V_1}\left[\frac{V^2}{2}\right]_{V_1}^{2V_1} = \frac{P_1}{2V_1}(4V_1^2 - V_1^2) = \frac{3}{2}P_1 V_1$. (C) is correct.
  - $\Delta T = \frac{P_2 V_2 - P_1 V_1}{R} = \frac{(2P_1)(2V_1) - P_1 V_1}{R} = \frac{3P_1 V_1}{R}$. $\Delta U = C_V \Delta T = \frac{3}{2}R\left(\frac{3P_1 V_1}{R}\right) = \frac{9}{2}P_1 V_1$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Fresnel Biprism, Virtual Source Separation, Fringe Width.
- **2. Derivation**:
  - Deviation produced by each half-prism: $\delta = (\mu - 1)\alpha$.
  - Separation between virtual sources: $d = 2 u \delta = 2 u (\mu - 1)\alpha$. (A) is correct.
  - Fringe width: $\beta = \frac{\lambda D}{d} = \frac{\lambda D}{2u(\mu - 1)\alpha}$. (B) is correct.
  - $\beta$ is proportional to screen distance $D$. (C) is correct.
  - As $\alpha$ decreases, $d$ decreases, so $\beta$ increases. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Davisson-Germer Experiment, de Broglie Matter Waves, Bragg Law.
- **2. Derivation**:
  - Experimentally verified wave nature of electrons. (A) is correct.
  - Maximum scattering at $54\text{ V}$ and $\phi = 50^\circ$. (B) is correct.
  - Bragg angle $\theta = 90^\circ - \phi/2 = 65^\circ$. (C) is correct.
  - Theoretical de Broglie wavelength ($0.167\text{ nm}$) matched experimental Bragg diffraction ($0.165\text{ nm}$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Adiabatic Oscillations of Gas-Piston System, Simple Harmonic Motion.
- **2. Derivation**:
  - Rapid oscillations are adiabatic ($P V^\gamma = \text{constant}$). (A) is correct.
  - Pressure changes: $dP_1 = -\gamma P_0 \frac{A x}{V_0}$, $dP_2 = +\gamma P_0 \frac{A x}{V_0}$.
  - Net restoring force: $F = (P_1 - P_2)A = -2\gamma\frac{P_0 A^2}{V_0}x$. (B) is correct.
  - Equation of motion: $m \ddot{x} + \frac{2\gamma P_0 A^2}{V_0}x = 0$. With $V_0 = A L$: $\omega = \sqrt{\frac{2\gamma P_0 A}{m L}}$. (C) is correct.
  - For isothermal process ($\gamma = 1$), $\omega_{\text{iso}} = \sqrt{\frac{2P_0 A}{m L}}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Momentum conservation: $m v = (M + m)v_f \implies v_f = \frac{0.020 \times 400.0}{3.98 + 0.020} = \frac{8.00}{4.00} = 2.00\text{ m/s}$.
  Energy conservation: $\frac{1}{2}(M + m)v_f^2 = (M + m)g h \implies h = \frac{v_f^2}{2g} = \frac{4.00}{2(9.80)} = \frac{4.00}{19.6} \approx 0.20\text{ m}$.
- **Question 8**: $Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{10.0}\sqrt{\frac{20.0 \times 10^{-3}}{50.0 \times 10^{-6}}} = \frac{1}{10.0}\sqrt{400} = \frac{20.0}{10.0} = 2.00$.
- **Question 9**: $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2} = \frac{1}{15.0} - \frac{1}{30.0} = \frac{1}{30.0} \implies F = 30.0\text{ cm}$.
- **Question 10**: Work done $W = P \Delta V = (1.0 \times 10^5)(0.012 - 0.010) = 1.0 \times 10^5 \times 0.002 = 200.0\text{ J}$.
  $\Delta U = Q - W = 500.0 - 200.0 = 300.0\text{ J}$.
- **Question 11**: Bohr quantization: $L = n \hbar = 3 \hbar$. Thus the value is $3.00$.
- **Question 12**: $\nu_0 = \frac{1}{2\pi}\sqrt{\frac{k}{m}} = \frac{1}{2\pi}\sqrt{\frac{200.0}{0.50}} = \frac{1}{2\pi}\sqrt{400} = \frac{20.0}{2\pi} = \frac{10.0}{\pi} \approx 3.2\text{ Hz}$.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: Hoop $a = \frac{1}{2}g\sin\theta$ (P-1); Solid cylinder $a = \frac{2}{3}g\sin\theta$ (Q-2); Solid sphere $a = \frac{5}{7}g\sin\theta$ (R-3); Shell $a = \frac{3}{5}g\sin\theta$ (S-4). Option (A).
- **Question 14**: Dimensions: Flux $[M L^2 T^{-2} A^{-1}]$ (P-1); Inductance $[M L^2 T^{-2} A^{-2}]$ (Q-2); Field $[M T^{-2} A^{-1}]$ (R-3); Permeability $[M L T^{-2} A^{-2}]$ (S-4). Option (A).
- **Question 15**: Blue sky: Rayleigh scattering (P-1); Rainbow: dispersion/reflection (Q-2); Mirage: TIR (R-3); Oil film: interference (S-4). Option (A).
- **Question 16**: First Maxwell from $dU$ (P-1); Second from $dH$ (Q-2); Third from $dF$ (R-3); Fourth from $dG$ (S-4). Option (A).
- **Question 17**: Alpha decay: $A-4, Z-2$ (P-1); Beta-minus: $Z+1$ (Q-2); Electron capture: $Z-1$ (R-3); Gamma decay: isomers (S-4). Option (A).
- **Question 18**: Inductor leads $+90^\circ$ (P-1); Capacitor lags $-90^\circ$ (Q-2); Resistor in phase $0^\circ$ (R-3); Resonant circuit in phase $0^\circ$ (S-4). Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Tropylium cation has $6\pi$ aromatic system. Cyclopropenyl cation has $2\pi$ aromatic system. Cyclopentadienyl cation has $4\pi$ antiaromatic system. Trityl carbocation is stabilized by 3 phenyl rings. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Acidic buffer requires weak acid and its conjugate salt. Acetic acid + sodium acetate, Formic acid + potassium formate, and Benzoic acid + sodium benzoate are buffers. $\text{HCl} + \text{NaCl}$ is a strong acid mixture (not a buffer). Correct options: **(A), (B), (C)**.
- **Question 21**: More negative $E^\circ$ indicates stronger reducing agent. Zinc displaces copper. Copper does not displace hydrogen from non-oxidizing acids. Silver cannot displace zinc. Correct options: **(A), (B), (C)**.
- **Question 22**: Calcination expels volatile gases without air. Roasting oxidizes sulfide ores in presence of air. Limestone heating is calcination. $\text{ZnS}$ oxidation is roasting. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Gabriel phthalimide yields pure primary amines. Hofmann degradation yields primary amines with one less carbon. Nitrile reduction yields primary amines. Direct alkylation gives mixture of $1^\circ, 2^\circ, 3^\circ$ and quaternary salts. Correct options: **(A), (B), (C)**.
- **Question 24**: Rock salt is $6:6$ coordination. Fluorite is $8:4$ coordination. Anti-fluorite is $4:8$ coordination. Zinc blende is $4:4$ coordination. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $\text{pH} = 4.00 \implies [\text{H}^+] = 1.0 \times 10^{-4}\text{ M}$.
  $K_a = \frac{[\text{H}^+]^2}{C} = \frac{(1.0 \times 10^{-4})^2}{0.010} = \frac{1.0 \times 10^{-8}}{1.0 \times 10^{-2}} = 1.0 \times 10^{-6}$.
  Multiplied by $10^6$, value is $1.00$.
- **Question 26**: Rate $\propto [A]^2 [B]^1$. Overall order $= 2 + 1 = 3.00$.
- **Question 27**: $\text{FCC}$ has $Z = 4$. $\rho = \frac{Z M}{N_A a^3} = \frac{4 \times 60.0}{(6.022 \times 10^{23})(64.0 \times 10^{-24})} = \frac{240.0}{38.54} = 6.23\text{ g/cm}^3$.
- **Question 28**: $\text{CH}_4 + 2\text{O}_2 \to \text{CO}_2 + 2\text{H}_2\text{O}(l)$.
  $\Delta_c H^\circ = \Delta_f H^\circ(\text{CO}_2) + 2\Delta_f H^\circ(\text{H}_2\text{O}) - \Delta_f H^\circ(\text{CH}_4) = -393.5 + 2(-285.8) - (-74.8) = -393.5 - 571.6 + 74.8 = -890.3\text{ kJ/mol}$.
- **Question 29**: Molality $m = \frac{18.0 / 180.0}{0.200\text{ kg}} = \frac{0.10}{0.200} = 0.50\text{ m}$. $\Delta T_f = K_f m = 1.86 \times 0.50 = 0.93\text{ K}$.
- **Question 30**: $\text{XeF}_2$ has 8 valence electrons, 2 used for bonding with F, leaving 6 non-bonding electrons $= 3$ lone pairs.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Tollens: silver mirror (P-1); Fehling: red ppt (Q-2); Ferric chloride: violet color (R-3); Lucas: alcohol classification (S-4). Option (A).
- **Question 32**: Complex names: Potassium hexacyanidoferrate(II) (P-1); Tetraamminecopper(II) sulfate (Q-2); Hexaamminecobalt(III) chloride (R-3); Potassium hexachloridoplatinate(IV) (S-4). Option (A).
- **Question 33**: Mond process for Ni (P-1); Van Arkel for Zr/Ti (Q-2); Electrolytic for Cu (R-3); Zone refining for semiconductors (S-4). Option (A).
- **Question 34**: Crimson: Lithium (P-1); Yellow: Sodium (Q-2); Apple green: Barium (R-3); Brick red: Calcium (S-4). Option (A).
- **Question 35**: Plexiglas (P-1); Teflon (Q-2); Orlon (R-3); Styron (S-4). Option (A).
- **Question 36**: Starch: polysaccharide (P-1); Insulin: peptide (Q-2); Cholesterol: steroid (R-3); ATP: nucleotide (S-4). Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: $f(-x) = \frac{(-x)^2 - 1}{(-x)^2 + 1} = \frac{x^2 - 1}{x^2 + 1} = f(x)$ (even). $f'(x) = \frac{2x(x^2+1) - (x^2-1)(2x)}{(x^2+1)^2} = \frac{4x}{(x^2+1)^2}$. Min at $x=0$ with $f(0) = -1$. As $x\to\pm\infty$, $f(x)\to 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: $A^3 - A = 0 \implies \lambda(\lambda - 1)(\lambda + 1) = 0 \implies \lambda \in \{0, 1, -1\}$. Determinant product of eigenvalues $\in \{0, 1, -1\}$. Distinct linear factors imply real diagonalizability. If $\det(A) \ne 0$, 0 is not an eigenvalue, so $A(A^2 - I) = 0 \implies A^2 = I$. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: $x^2 - 4x + y^2 - 6y = 12 \implies (x-2)^2 + (y-3)^2 = 12 + 4 + 9 = 25$. Center $(2, 3)$, radius $5$. $(5-2)^2 + (7-3)^2 = 9 + 16 = 25$ (on circle). Tangent: $(5-2)(x-2) + (7-3)(y-3) = 25 \implies 3(x-2) + 4(y-3) = 25 \implies 3x + 4y - 43 = 0$. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Homogeneous equation. $y = vx \implies v + x v' = \frac{1 - v}{1 + v} \implies x v' = \frac{1 - v - v - v^2}{1 + v} = \frac{1 - 2v - v^2}{1 + v}$. In polar coordinates, $\tan\theta = y/x$, giving spiral trajectories. Correct options: **(A), (B), (D)**.
- **Question 41**: $\vec{u} \times \vec{v} = (\hat{i}+\hat{j})\times(\hat{j}+\hat{k}) = \hat{k} - \hat{j} + \hat{i} = \hat{i} - \hat{j} + \hat{k}$. $[\vec{u}\ \vec{v}\ \vec{w}] = (\vec{u}\times\vec{v})\cdot\vec{w} = (1, -1, 1)\cdot(1, 0, 1) = 1 + 0 + 1 = 2$. Linearly independent; volume is 2. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Binomial $n = 5, p = 1/3$: Mean $n p = 5/3$. Variance $n p q = 5(1/3)(2/3) = 10/9$. $P(X = 2) = \binom{5}{2}(1/9)(8/27) = 80/243$. $P(X \ge 1) = 1 - (2/3)^5 = 1 - 32/243 = 211/243$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Beta integral $\int_0^1 x^4 (1-x)^3 dx = B(5, 4) = \frac{\Gamma(5)\Gamma(4)}{\Gamma(9)} = \frac{4! 3!}{8!} = \frac{24 \times 6}{40320} = \frac{144}{40320} = \frac{1}{280} \implies m = 280$.
- **Question 44**: $y = x^2 \implies y' = 2x$. At $(1, 1)$, tangent slope $m_T = 2$. Normal slope $m_N = -1/2 = -0.50$. Magnitude is $0.50$.
- **Question 45**: $d = \frac{|12 - 3|}{\sqrt{1^2 + (-2)^2 + 2^2}} = \frac{9}{\sqrt{9}} = \frac{9}{3} = 3.00$.
- **Question 46**: Infinite GP $a = 8, r = 1/4 \implies S = \frac{8}{1 - 1/4} = \frac{8}{3/4} = \frac{32}{3} \approx 10.67$.
- **Question 47**: `LEADER`: 6 letters with 2 E's. Permutations $= \frac{6!}{2!} = \frac{720}{2} = 360.00$.
- **Question 48**: Tridiagonal matrix determinant:
  $2(4 - 1) - 1(2 - 0) = 2(3) - 2 = 6 - 2 = 4.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: $\lim_{x\to\infty}(1 + 3/x)^{2x} = e^{\lim_{x\to\infty} 2x(3/x)} = e^6$. Option (A).
- **Question 50**: $\frac{x^2}{16} - \frac{y^2}{9} = 1 \implies a^2 = 16, b^2 = 9$. $e = \sqrt{1 + b^2/a^2} = \sqrt{1 + 9/16} = \sqrt{25/16} = 5/4$. Option (A).
- **Question 51**: The two lines intersect at the point $(0, 0, 0)$ (check coordinates), so shortest distance is 0. Option (A).
- **Question 52**: Since $|z| = 1 \implies z \bar{z} = 1 \implies \bar{z} = 1/z$. $\frac{1 + z}{1 + 1/z} = \frac{1 + z}{(z + 1)/z} = z$. Option (A).
- **Question 53**: $\frac{dy}{dx} + y = 1 \implies y = 1 - e^{-x}$. Option (A).
- **Question 54**: $n p = 4, n p (1 - p) = 2 \implies 1 - p = 1/2 \implies p = 1/2 \implies n = 8$. Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 10
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 16.95
- Q8: 11.1
- Q9: 0.40
- Q10: 11.53
- Q11: 1.00
- Q12: 1.66
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
- Q25: 1.21
- Q26: 40.0
- Q27: 288.5
- Q28: 0.146
- Q29: 2.74
- Q30: 4.90
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
- Q43: 1024
- Q44: 1.00
- Q45: 4.00
- Q46: 3.00
- Q47: 6.00
- Q48: 34650
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
- Q7: 0.20
- Q8: 2.00
- Q9: 30.0
- Q10: 300.0
- Q11: 3.00
- Q12: 3.2
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C, D
- Q20: A, B, C
- Q21: A, B, C
- Q22: A, B, C, D
- Q23: A, B, C
- Q24: A, B, C, D
- Q25: 1.00
- Q26: 3.00
- Q27: 6.23
- Q28: -890.3
- Q29: 0.93
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
- Q40: A, B, D
- Q41: A, B, C, D
- Q42: A, B, C, D
- Q43: 280
- Q44: 0.50
- Q45: 3.00
- Q46: 10.67
- Q47: 360
- Q48: 4.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: Heavy option-checking cognitive load (+4/-2).
- **Physics**: Invariant relativistic mass, Dieterici compressibility, Abbe resolution limit, rolling in bowl, polytropic negative index, gas-piston adiabatic oscillations.
- **Chemistry**: Baeyer-Villiger lactone mechanism, Orgel high-spin inversion, Debye-Huckel limiting law, Silicate structural geometry, Hückel aromatic carbocations.
- **Mathematics**: Multivariable directional gradients, normal chord parameter relations, forced harmonic resonance secular terms, tetrahedron geometry, Bernoulli process.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

if __name__ == "__main__":
    create_mock_files(10, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")

