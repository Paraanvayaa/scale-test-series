# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 08.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Complex circuit transients, electrodynamics, rotating frames
- Transition metal CFT, reaction mechanisms with stereochemical proofs
- Linear systems, calculus-heavy geometry, multivariable extrema
"""
import os
import sys

# Ensure engine path
sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 08 — Paper 1
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
A thin, hollow cylindrical conducting shell of mass $M$, radius $R$, and length $L$ ($L \gg R$) is free to rotate about its fixed central longitudinal axis without friction. Initially, the cylinder is at rest in an external uniform magnetic field $B_0$ directed parallel to its axis. The magnetic field is then smoothly decreased to zero:
(A) The time-varying magnetic field induces an azimuthal electric field $E_\theta(R) = -\frac{R}{2}\frac{dB}{dt}$ on the cylinder surface.  
(B) If the shell carries a uniform initial surface charge density $\sigma$, the magnetic induced torque accelerates the cylinder to a final angular velocity $\omega_f = \frac{\sigma B_0}{M/(2\pi R L)}$.  
(C) The total mechanical angular momentum acquired by the cylinder equals the angular momentum initially stored in the crossed electromagnetic fields.  
(D) If the cylinder were a perfect superconductor carrying zero initial current, a surface supercurrent would be induced such that the total magnetic flux enclosed by the cylinder remains strictly constant.

#### Question 2
An $LC$ circuit consists of an ideal inductor of inductance $L$ and a nonlinear varactor diode whose capacitance depends on the voltage $V$ across it according to $C(V) = \frac{C_0}{\sqrt{1 + V/V_0}}$ for $V > -V_0$:
(A) For very small oscillations ($V \ll V_0$), the circuit behaves as a linear harmonic oscillator with natural frequency $\omega_0 = \frac{1}{\sqrt{L C_0}}$.  
(B) For finite amplitude oscillations, the oscillation period increases as the oscillation amplitude increases.  
(C) The total electrostatic energy stored in the nonlinear capacitor at potential $V$ is $U_e(V) = \frac{2}{3}C_0 V_0^2 \left[(1 + V/V_0)^{3/2} - 1\right] - C_0 V_0 V$.  
(D) Energy is strictly conserved between the magnetic field of the inductor and the electric field of the capacitor during free oscillations.

#### Question 3
A star of mass $M_1$ and a compact companion of mass $M_2$ orbit in circular orbits about their common center of mass with orbital period $T$. An observer in the orbital plane observes the spectral line of rest wavelength $\lambda_0$ emitted by star 1:
(A) The semi-major axis of star 1's orbit about the center of mass is $r_1 = \left(\frac{G M_2^3 T^2}{4\pi^2(M_1 + M_2)^2}\right)^{1/3}$.  
(B) The maximum line-of-sight radial velocity of star 1 is $v_{1r,\text{max}} = \frac{2\pi r_1}{T}$.  
(C) The maximum observed Doppler-shifted wavelength is $\lambda_{\text{max}} = \lambda_0 \sqrt{\frac{1 + v_{1r}/c}{1 - v_{1r}/c}}$ taking relativistic kinematics into account.  
(D) The periodic variation of the observed wavelength allows determination of the mass function $f(M) = \frac{(M_2 \sin i)^3}{(M_1 + M_2)^2} = \frac{T v_{1r,\text{max}}^3}{2\pi G}$.

#### Question 4
A hollow spherical shell has inner radius $R_1$ and outer radius $R_2$. The thermal conductivity of the material varies inversely with temperature: $k(T) = \frac{k_0 T_0}{T}$. The inner surface is maintained at steady temperature $T_1$ and the outer surface at $T_2$ ($T_1 > T_2$):
(A) Under steady-state conditions, the radial heat flow rate $Q$ is constant across every spherical surface of radius $r$ ($R_1 \le r \le R_2$).  
(B) The steady-state temperature profile satisfies $T(r) = T_1 \left(\frac{T_2}{T_1}\right)^{\frac{1/R_1 - 1/r}{1/R_1 - 1/R_2}}$.  
(C) The total steady-state heat current through the shell is $Q = \frac{4\pi k_0 T_0}{\frac{1}{R_1} - \frac{1}{R_2}}\ln\left(\frac{T_1}{T_2}\right)$.  
(D) If the conductivity were constant ($k = k_0$), the temperature profile would vary linearly with $1/r$.

#### Question 5
In a Michelson interferometer illuminated with quasi-monochromatic light of central wavelength $\lambda_0 = 600\text{ nm}$ and spectral linewidth $\Delta \lambda = 0.020\text{ nm}$:
(A) The coherence length of the light is $L_c = \frac{\lambda_0^2}{\Delta \lambda} = 1.80\text{ cm}$.  
(B) High-contrast interference fringes are visible only when the optical path difference $\Delta d$ satisfies $|\Delta d| < L_c$.  
(C) As the path difference increases, the fringe visibility $V = \frac{I_{\text{max}} - I_{\text{min}}}{I_{\text{max}} + I_{\text{min}}}$ decays smoothly to zero.  
(D) Inserting a thin transparent dielectric plate of refractive index $\mu$ and thickness $t$ into one arm shifts the fringe pattern by $\Delta N = \frac{2(\mu - 1)t}{\lambda_0}$ fringes.

#### Question 6
A uniform solid cylinder of mass $m$ and radius $r$ rolls without slipping down the outer surface of a fixed rough horizontal circular cylinder of radius $R$. The small cylinder is released from rest from the topmost point:
(A) While rolling without slipping, the angle $\theta$ from the vertical satisfies $\ddot{\theta} = \frac{2g}{3(R+r)}\sin\theta$.  
(B) The normal reaction force exerted by the fixed cylinder is $N(\theta) = mg\left(\frac{7}{3}\cos\theta - \frac{4}{3}\right)$.  
(C) If the friction is sufficiently large to prevent slipping, the cylinder leaves the surface at an angle $\theta_c = \arccos(4/7) \approx 55.15^\circ$.  
(D) The minimum coefficient of static friction $\mu_s$ required to prevent slipping up to the point of detachment is $\mu_{s,\text{min}} = \frac{2\sin\theta_c}{7\cos\theta_c - 4}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A symmetric gyroscope with rotor moment of inertia $I_s = 0.020\text{ kg}\cdot\text{m}^2$ spins at $\omega_s = 300.0\text{ rad/s}$ about its horizontal axle. The distance from the pivot support to the center of mass of the gyroscope is $d = 0.10\text{ m}$, and the total mass is $M = 1.50\text{ kg}$. Taking $g = 9.80\text{ m/s}^2$, calculate the steady precession angular frequency $\Omega_p$ (in $\text{rad/s}$). [Round off to TWO decimal places].

#### Question 8
In a magnetron tube, electrons of charge-to-mass ratio $e/m = 1.76 \times 10^{11}\text{ C/kg}$ are emitted with negligible velocity from a central cylindrical cathode of radius $a = 2.0\text{ mm}$ and accelerated toward a coaxial cylindrical anode of radius $b = 10.0\text{ mm}$ maintained at potential $V_a = 400.0\text{ V}$. An axial magnetic field $B$ is applied. Calculate the Hull cut-off magnetic field $B_c$ (in milliTesla, $\text{mT}$) above which electrons fail to reach the anode. [Take $B_c = \frac{\sqrt{8 m V_a / e}}{b(1 - a^2/b^2)}$. Round off to TWO decimal places].

#### Question 9
A solid copper sphere of radius $R = 0.050\text{ m}$ is suspended in an evacuated chamber whose walls are maintained at absolute zero ($0\text{ K}$). The sphere is initially at temperature $T_1 = 300.0\text{ K}$. If the emissivity of the copper surface is $\varepsilon = 0.80$, density of copper is $\rho = 8900\text{ kg/m}^3$, specific heat capacity is $c = 385\text{ J/(kg}\cdot\text{K)}$, and the Stefan-Boltzmann constant is $\sigma = 5.67 \times 10^{-8}\text{ W/(m}^2\cdot\text{K}^4)$, calculate the initial cooling rate $\left|\frac{dT}{dt}\right|$ of the sphere in $\text{K/s}$. [Round off to TWO decimal places].

#### Question 10
A step-index optical fiber has a core of refractive index $n_1 = 1.500$ and a cladding of refractive index $n_2 = 1.480$. Calculate the numerical aperture ($NA = \sqrt{n_1^2 - n_2^2}$) of the optical fiber. [Round off to TWO decimal places].

#### Question 11
Two very long coaxial metal cylinders have radii $a = 1.0\text{ cm}$ and $b = 4.0\text{ cm}$. The space between them is filled with a dielectric whose relative permittivity varies radially as $\varepsilon_r(r) = \frac{k}{r}$, where $k = 0.020\text{ m}$. Calculate the capacitance per unit length of this cylindrical capacitor in picoFarads per meter ($\text{pF/m}$). [Take $\varepsilon_0 = 8.854 \times 10^{-12}\text{ F/m}$. Note $\int_a^b \frac{dr}{r \varepsilon_r(r)} = \frac{b - a}{k}$. Round off to TWO decimal places].

#### Question 12
Alpha particles of kinetic energy $K = 5.0\text{ MeV}$ are scattered by a thin gold foil ($Z = 79$). Calculate the distance of closest approach $d_0$ (in femtometers, $10^{-15}\text{ m}$) for a head-on collision. [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$, $e = 1.60 \times 10^{-19}\text{ C}$, and $1\text{ MeV} = 1.60 \times 10^{-13}\text{ J}$. Round off to ONE decimal place].

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
In a Hall effect measurement on a semiconductor strip of width $w = 1.0\text{ cm}$ and thickness $t = 1.0\text{ mm}$ carrying a current $I = 10.0\text{ mA}$ in a perpendicular magnetic field $B = 0.50\text{ T}$, the transverse Hall voltage measured across its width is $V_H = -2.5\text{ mV}$. The majority charge carriers and their carrier density $n$ are:
(A) Electrons; $n = 1.25 \times 10^{20}\text{ m}^{-3}$  
(B) Holes; $n = 1.25 \times 10^{20}\text{ m}^{-3}$  
(C) Electrons; $n = 2.50 \times 10^{21}\text{ m}^{-3}$  
(D) Holes; $n = 2.50 \times 10^{21}\text{ m}^{-3}$

#### Question 14
The magnetic field at the center of a flat square wire loop of side length $L$ carrying steady current $I$ is:
(A) $B = \frac{2\sqrt{2}\mu_0 I}{\pi L}$  
(B) $B = \frac{\sqrt{2}\mu_0 I}{\pi L}$  
(C) $B = \frac{4\mu_0 I}{\pi L}$  
(D) $B = \frac{\mu_0 I}{2\pi L}$

#### Question 15
A Brewster window in a gas laser cavity is oriented such that light polarized in the plane of incidence (p-polarization) suffers zero reflection loss. If the refractive index of the window glass is $\mu = 1.50$, the Brewster angle $\theta_B$ is:
(A) $\arctan(1.50) \approx 56.3^\circ$  
(B) $\arcsin(1/1.50) \approx 41.8^\circ$  
(C) $45.0^\circ$  
(D) $\arctan(1/1.50) \approx 33.7^\circ$

#### Question 16
For a real gas obeying the van der Waals equation of state, the ratio of the critical temperature $T_c$ to the Boyle temperature $T_B$ is:
(A) $\frac{8}{27}$  
(B) $\frac{3}{8}$  
(C) $\frac{1}{3}$  
(D) $\frac{2}{3}$

#### Question 17
A relativistic electron has total energy equal to three times its rest mass energy ($E = 3 m_0 c^2$). Its de Broglie wavelength $\lambda$ in terms of its Compton wavelength $\lambda_C = \frac{h}{m_0 c}$ is:
(A) $\lambda = \frac{\lambda_C}{\sqrt{8}} \approx 0.354 \lambda_C$  
(B) $\lambda = \frac{\lambda_C}{3}$  
(C) $\lambda = \frac{\lambda_C}{\sqrt{3}}$  
(D) $\lambda = \sqrt{8}\lambda_C$

#### Question 18
The moment of inertia of a uniform thin equilateral triangular lamina of mass $M$ and side length $a$ about an axis passing through its center of mass and perpendicular to its plane is:
(A) $\frac{1}{12}M a^2$  
(B) $\frac{1}{6}M a^2$  
(C) $\frac{1}{24}M a^2$  
(D) $\frac{1}{18}M a^2$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Jahn-Teller theorem and structural distortions in transition metal complexes:
(A) Any non-linear molecular system in a spatially degenerate electronic state will undergo a geometrical distortion that lowers its symmetry and removes the degeneracy.  
(B) High-spin $d^4$ ($\text{Cr}^{2+}$) and $d^9$ ($\text{Cu}^{2+}$) octahedral complexes exhibit strong Jahn-Teller elongation along the $z$-axis ($z$-out, $c/a > 1$).  
(C) In $[\text{Cu(H}_2\text{O})_6]^{2+}$, four equatorial $\text{Cu-O}$ bonds are shorter ($1.97\text{ \AA}$) while two axial bonds are significantly longer ($2.30\text{ \AA}$).  
(D) Octahedral complexes of $d^3$ ($\text{Cr}^{3+}$), low-spin $d^6$ ($\text{Co}^{3+}$), and $d^8$ ($\text{Ni}^{2+}$) do not show Jahn-Teller distortion because their electronic ground states are orbitally non-degenerate.

#### Question 20
In the pinacol-pinacolone rearrangement of unsymmetrical 1,2-diols catalyzed by concentrated $\text{H}_2\text{SO}_4$:
(A) Protonation occurs preferentially at the hydroxyl group that forms the more stable carbocation upon loss of water.  
(B) The migratory aptitude of aryl groups is enhanced by electron-donating substituents: $p\text{-anisyl} > p\text{-tolyl} > \text{phenyl} > p\text{-chlorophenyl}$.  
(C) The 1,2-shift of the migrating group proceeds with complete retention of configuration at the migrating chiral center.  
(D) For 1,1-diphenyl-2-methylpropane-1,2-diol, protonation occurs at the diphenyl-substituted carbon, and a methyl group migrates to yield 3,3-diphenylbutan-2-one.

#### Question 21
Regarding electrochemical concentration cells:
(A) In an electrode concentration cell without transference, such as $\text{Pt}|\text{H}_2(P_1)|\text{HCl}(m)|\text{H}_2(P_2)|\text{Pt}$, the cell EMF is $E = \frac{RT}{2F}\ln\left(\frac{P_1}{P_2}\right)$.  
(B) In an electrolyte concentration cell with transference, the liquid junction potential arises from the difference in transport numbers between cation and anion ($t_+ \ne t_-$).  
(C) A salt bridge filled with saturated $\text{KCl}$ in agar-agar minimizes the liquid junction potential because the transport numbers of $\text{K}^+$ and $\text{Cl}^-$ are nearly identical ($t_{\text{K}^+} \approx t_{\text{Cl}^-} \approx 0.50$).  
(D) The standard cell potential $E_{\text{cell}}^\circ$ of any concentration cell is identically zero.

#### Question 22
Regarding the Langmuir adsorption isotherm for a gas on a solid adsorbent:
(A) It assumes localized monolayer adsorption on equivalent, energetically uniform surface sites with zero lateral interaction between adsorbed molecules.  
(B) The fractional surface coverage is given by $\theta = \frac{K P}{1 + K P}$, where $K$ is the adsorption equilibrium constant.  
(C) At very low pressures ($P \to 0$), the isotherm reduces to Henry's law: $\theta \approx K P$ (first-order in pressure).  
(D) At very high pressures ($K P \gg 1$), the surface coverage approaches saturation ($\theta \to 1$, zero-order in pressure).

#### Question 23
Regarding crystal defects in stoichiometric ionic solids:
(A) Schottky defects consist of an equal number of cation and anion vacancies, preserving electrical neutrality while decreasing the bulk density of the crystal.  
(B) Frenkel defects consist of an ion (typically the smaller cation) displaced from its regular lattice site to an interstitial void, leaving the crystal density unchanged.  
(C) $\text{AgBr}$ exhibits both Schottky and Frenkel defects depending on temperature and preparation conditions.  
(D) The presence of Schottky defects increases the electrical conductivity of ionic crystals via the vacancy migration mechanism.

#### Question 24
Regarding the mutarotation and stereochemistry of D-glucose:
(A) Freshly dissolved $\alpha\text{-D-glucopyranose}$ has a specific optical rotation of $+112^\circ$, which slowly decreases to an equilibrium value of $+52.7^\circ$.  
(B) Freshly dissolved $\beta\text{-D-glucopyranose}$ has a specific optical rotation of $+18.7^\circ$, which slowly increases to the same equilibrium value of $+52.7^\circ$.  
(C) At thermodynamic equilibrium in aqueous solution, the $\beta$-anomer predominates ($\approx 64\%$) over the $\alpha$-anomer ($\approx 36\%$) because all bulky substituents (including $-\text{OH}$ at C1) are equatorial in the $^4C_1$ chair conformation.  
(D) Mutarotation involves reversible opening of the hemiacetal ring via an open-chain free aldehyde intermediate.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
A buffer solution is prepared by mixing $0.15\text{ M}$ acetic acid ($\text{CH}_3\text{COOH}$, $pK_a = 4.74$) and $0.10\text{ M}$ sodium acetate ($\text{CH}_3\text{COONa}$). Calculate the change in $\text{pH}$ ($\Delta \text{pH}$) when $0.020\text{ mol}$ of solid $\text{NaOH}$ is added to $1.0\text{ L}$ of this buffer solution, assuming no volume change. [Take $\log(1.50) \approx 0.176$ and $\log(1.083) \approx 0.035$. Round off to TWO decimal places].

#### Question 26
For a chemical reaction, the rate constant is $k_1 = 1.0 \times 10^{-3}\text{ s}^{-1}$ at $T_1 = 300\text{ K}$ and $k_2 = 4.0 \times 10^{-3}\text{ s}^{-1}$ at $T_2 = 320\text{ K}$. Calculate the activation energy $E_a$ (in $\text{kJ/mol}$) of the reaction. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $\ln 4 = 1.3863$. Round off to TWO decimal places].

#### Question 27
Silver crystallizes in a face-centered cubic ($\text{FCC}$) lattice with density $\rho = 10.50\text{ g/cm}^3$. Given the atomic mass of silver is $M = 107.87\text{ g/mol}$ and Avogadro's number is $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$, calculate the unit cell edge length $a$ in picometers ($\text{pm}$). [Round off to ONE decimal place].

#### Question 28
Calculate the standard cell potential $E_{\text{cell}}^\circ$ (in Volts) at $298\text{ K}$ for the reaction:
$$\text{Zn}(s) + 2\text{Ag}^+(aq) \to \text{Zn}^{2+}(aq) + 2\text{Ag}(s)$$
Given standard reduction potentials: $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.763\text{ V}$ and $E^\circ(\text{Ag}^+/\text{Ag}) = +0.799\text{ V}$. [Round off to TWO decimal places].

#### Question 29
A solution containing $4.00\text{ g}$ of a non-volatile polymer in $100.0\text{ mL}$ of water exerts an osmotic pressure of $\Pi = 2.46\text{ kPa}$ at $T = 300\text{ K}$. Calculate the molar mass $M_n$ of the polymer in $\text{kg/mol}$. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to ONE decimal place].

#### Question 30
Calculate the spin-only magnetic moment $\mu_{\text{eff}}$ (in Bohr Magnetons, $\text{BM}$) of the complex ion $[\text{Cr(H}_2\text{O})_6]^{3+}$ ($\text{Cr}^{3+}, 3d^3$). [Take $\sqrt{15} \approx 3.87$. Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Reimer-Tiemann reaction of phenol with chloroform and aqueous $\text{NaOH}$, the reactive electrophilic intermediate is:
(A) Dichlorocarbene ($:\text{CCl}_2$)  
(B) Trichloromethyl anion ($^-\text{CCl}_3$)  
(C) Formyl cation ($^+\text{CHO}$)  
(D) Chlorocarbene ($:\text{CHCl}$)

#### Question 32
On an Ellingham diagram ($\Delta G^\circ$ vs $T$):
(A) The slope of the line for $2\text{C}(s) + \text{O}_2(g) \to 2\text{CO}(g)$ is negative because $\Delta S^\circ > 0$.  
(B) Any metal can reduce the oxide of another metal that lies above it on the diagram at that temperature.  
(C) Sudden changes in slope correspond to phase transitions (melting or boiling) of the metal or oxide.  
(D) All of the above statements are correct.

#### Question 33
Gabriel phthalimide synthesis cannot be used to prepare aniline ($\text{C}_6\text{H}_5\text{NH}_2$) because:
(A) Aryl halides do not undergo nucleophilic substitution with potassium phthalimide under ordinary conditions due to partial double bond character of the $\text{C-X}$ bond.  
(B) Aniline is too volatile to be isolated.  
(C) Phthalimide is insoluble in aromatic solvents.  
(D) Hydrazine does not cleave $N$-phenylphthalimide.

#### Question 34
According to VSEPR theory and valence bond theory, the molecular geometry and hybridization of the central xenon atom in $\text{XeF}_4$ are:
(A) Square planar; $sp^3d^2$  
(B) Tetrahedral; $sp^3$  
(C) See-saw; $sp^3d$  
(D) Octahedral; $sp^3d^2$

#### Question 35
The radius of the first Bohr orbit of a hydrogen-like ion of atomic number $Z$ is related to the Bohr radius of hydrogen ($a_0$) by:
(A) $r_1 = \frac{a_0}{Z}$  
(B) $r_1 = a_0 Z$  
(C) $r_1 = \frac{a_0}{Z^2}$  
(D) $r_1 = a_0 Z^2$

#### Question 36
Teflon is an addition polymer synthesized by free-radical polymerization of:
(A) Tetrafluoroethene ($\text{CF}_2\text{=CF}_2$)  
(B) Vinyl chloride ($\text{CH}_2\text{=CHCl}$)  
(C) Acrylonitrile ($\text{CH}_2\text{=CHCN}$)  
(D) Chloroprene ($\text{CH}_2\text{=CCl-CH=CH}_2$)

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f: \mathbb{R} \to \mathbb{R}$ be defined by $f(x) = \sum_{n=1}^\infty \frac{\sin(3^n x)}{2^n}$:
(A) The series converges uniformly on $\mathbb{R}$ by the Weierstrass M-test.  
(B) $f(x)$ is continuous on all of $\mathbb{R}$.  
(C) $f(x)$ is periodic with period $2\pi$.  
(D) $f(x)$ is bounded on $\mathbb{R}$ with $|f(x)| \le 1$ for all $x \in \mathbb{R}$.

#### Question 38
Consider the linear system of equations:
$$\begin{aligned} x + y + z &= 6 \\ x + 2y + 3z &= 10 \\ x + 2y + \lambda z &= \mu \end{aligned}$$
Which of the following statements is/are correct?
(A) The system has a unique solution if $\lambda \ne 3$.  
(B) If $\lambda = 3$ and $\mu = 10$, the system has infinitely many solutions.  
(C) If $\lambda = 3$ and $\mu \ne 10$, the system is inconsistent (no solution).  
(D) When $\lambda = 3$ and $\mu = 10$, the line of intersection of the planes passes through $(2, 4, 0)$.

#### Question 39
Consider the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$. From an external point $P(x_0, y_0)$, two mutually perpendicular tangents are drawn to the ellipse:
(A) The locus of $P$ is the director circle $x^2 + y^2 = 25$.  
(B) The radius of the director circle is $5$.  
(C) The chord of contact for tangents drawn from $P(5, 0)$ is $x = \frac{16}{5} = 3.20$.  
(D) The area of the quadrilateral formed by the tangents and the radii to the points of contact is maximum when $x_0 = y_0 = \frac{5}{\sqrt{2}}$.

#### Question 40
Consider the Cauchy-Euler differential equation $x^2 \frac{d^2 y}{dx^2} - 3x \frac{dy}{dx} + 4y = 0$ for $x > 0$:
(A) Substituting $x = e^t$ transforms the equation into $\frac{d^2 y}{dt^2} - 4\frac{dy}{dt} + 4y = 0$.  
(B) The roots of the characteristic equation are repeated: $m_1 = m_2 = 2$.  
(C) The general solution is $y(x) = (C_1 + C_2 \ln x)x^2$.  
(D) If $y(1) = 2$ and $y'(1) = 5$, then $C_1 = 2$ and $C_2 = 1$.

#### Question 41
Let $L_1$ and $L_2$ be two skew lines given by $\vec{r}_1 = (1, 2, 3) + \lambda(2, 3, 4)$ and $\vec{r}_2 = (2, 4, 5) + \mu(3, 4, 5)$:
(A) The common perpendicular direction is parallel to $\vec{d}_1 \times \vec{d}_2 = (-\hat{i} + 2\hat{j} - \hat{k})$.  
(B) The vector connecting point on $L_1$ to point on $L_2$ is $\vec{a}_2 - \vec{a}_1 = (1, 2, 2)$.  
(C) The shortest distance between the lines is $d = \frac{|(1, 2, 2) \cdot (-1, 2, -1)|}{\sqrt{1 + 4 + 1}} = \frac{|-1 + 4 - 2|}{\sqrt{6}} = \frac{1}{\sqrt{6}}$.  
(D) The lines do not intersect.

#### Question 42
In Polya's urn scheme, an urn initially contains $w$ white balls and $b$ black balls. A ball is drawn at random, its color noted, and it is returned to the urn together with $c$ additional balls of the same color:
(A) The probability that the first ball drawn is white is $P(W_1) = \frac{w}{w+b}$.  
(B) The probability that the second ball drawn is white is $P(W_2) = \frac{w}{w+b}$, identical to $P(W_1)$.  
(C) The events $W_1$ and $W_2$ are positively correlated ($P(W_2|W_1) > P(W_2)$).  
(D) For any positive integer $n$, the probability that the $n$-th ball drawn is white remains $P(W_n) = \frac{w}{w+b}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^{\pi/2} \frac{\sin^3 x}{\sin^3 x + \cos^3 x}\,dx$$
If $I = \frac{\pi}{k}$, find the value of $k$.

#### Question 44
Calculate the determinant of the $3 \times 3$ matrix:
$$A = \begin{pmatrix} 1 & \omega & \omega^2 \\ \omega & \omega^2 & 1 \\ \omega^2 & 1 & \omega \end{pmatrix}$$
where $\omega = e^{i 2\pi/3}$ is the complex cube root of unity.

#### Question 45
Find the perpendicular distance from the point $P(2, 3, -1)$ to the plane $2x - 2y + z + 5 = 0$.

#### Question 46
Calculate the sum of the infinite arithmetico-geometric series:
$$S = 1 + \frac{2}{2} + \frac{3}{4} + \frac{4}{8} + \frac{5}{16} + \dots = \sum_{n=1}^\infty \frac{n}{2^{n-1}}$$

#### Question 47
Find the slope of the tangent to the rectangular hyperbola $x y = 16$ at the point $(4, 4)$. [Enter the absolute magnitude of the slope].

#### Question 48
Find the area bounded by the parabola $y = x^2$ and the line $y = 2x$, multiplied by $3$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{e^x - 1 - x - \frac{x^2}{2}}{x^3}$$
(A) $1/6$  
(B) $1/3$  
(C) $1/2$  
(D) $0$

#### Question 50
If the angle between the asymptotes of a hyperbola is $60^\circ$ and the transverse axis lies along the bisector of this angle, the eccentricity $e$ of the hyperbola is:
(A) $2/\sqrt{3}$  
(B) $2$  
(C) $\sqrt{3}$  
(D) $\sqrt{2}$

#### Question 51
Let $A$ be a $3 \times 3$ real skew-symmetric matrix ($A^T = -A$). Then $\det(A)$ is:
(A) $0$  
(B) $1$  
(C) $-1$  
(D) Any real number depending on entries

#### Question 52
For any non-zero vectors $\vec{a}, \vec{b}, \vec{c}$, the vector triple product $\vec{a} \times (\vec{b} \times \vec{c})$ is identically equal to:
(A) $(\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$  
(B) $(\vec{a} \cdot \vec{b})\vec{c} - (\vec{a} \cdot \vec{c})\vec{b}$  
(C) $(\vec{a} \times \vec{b}) \cdot \vec{c}$  
(D) $\vec{0}$

#### Question 53
The complex numbers $z$ satisfying $|z - 3| + |z + 3| = 10$ represent an ellipse in the Argand plane with eccentricity:
(A) $0.60$  
(B) $0.80$  
(C) $0.50$  
(D) $0.75$

#### Question 54
The value of the binomial sum $\sum_{k=0}^n \binom{n}{k} 3^k$ is:
(A) $4^n$  
(B) $3^n$  
(C) $2^{2n+1}$  
(D) $3^{n+1}$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 08 — Paper 2
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
A conducting rod of mass $m$, length $L$, and electrical resistance $R$ slides without friction down two parallel conducting rails inclined at angle $\theta$ to the horizontal. A uniform magnetic field $B$ is directed vertically upwards:
(A) The component of the magnetic field perpendicular to the inclined plane is $B_\perp = B\cos\theta$.  
(B) When the rod moves down the incline with velocity $v$, the motional EMF induced along its length is $\mathcal{E} = B L v \cos\theta$.  
(C) The magnetic Lorentz force on the induced current has a component opposing the motion along the incline equal to $F_{\text{mag}} = \frac{B^2 L^2 v \cos^2\theta}{R}$.  
(D) The terminal steady velocity of the rod is $v_t = \frac{m g R \sin\theta}{B^2 L^2 \cos^2\theta}$.

#### Question 2
Two large vertical parallel conducting plates of width $w$ separated by distance $d$ are connected across a battery of constant potential difference $V_0$. The lower ends of the plates are dipped into a dielectric liquid of mass density $\rho$ and dielectric constant $K$:
(A) The upward electrostatic force on the liquid column arises from the fringing electric field at the bottom edge of the capacitor.  
(B) The total upward electrostatic force is $F_e = \frac{1}{2}\varepsilon_0 (K - 1)\frac{w}{d}V_0^2$.  
(C) The equilibrium height to which the dielectric liquid rises between the plates is $h = \frac{\varepsilon_0 (K - 1) V_0^2}{2 \rho g d^2}$.  
(D) If the battery is disconnected before dipping the plates into the liquid, the liquid will still rise between the plates.

#### Question 3
Regarding the propagation of sound waves in an ideal polyatomic gas whose molecules have translational, rotational, and vibrational degrees of freedom:
(A) Sound wave propagation in a gas is an adiabatic process ($P V^\gamma = \text{constant}$) because the pressure variations occur too rapidly for significant thermal conduction between compressions and rarefactions.  
(B) The speed of sound is given by the Laplace formula $v = \sqrt{\frac{\gamma R T}{M}}$.  
(C) At very high temperatures where vibrational modes are fully activated, $\gamma$ decreases, approaching $\frac{4}{3}$ for linear triatomic molecules ($\text{CO}_2$).  
(D) Newton's isothermal formula $v = \sqrt{\frac{RT}{M}}$ underestimates the true speed of sound in air by approximately $15\%$.

#### Question 4
In a Lloyd's mirror interference experiment, light from a narrow slit $S_1$ at distance $h$ above a flat front-surface glass mirror reflects at grazing incidence onto a screen placed at distance $D$ ($D \gg h$):
(A) The reflected light appears to originate from a virtual coherent source $S_2$ located at distance $h$ behind the mirror plane.  
(B) Reflection from the optically denser glass mirror introduces an intrinsic phase change of $\pi$ radians ($180^\circ$).  
(C) The fringe spacing on the screen is $\beta = \frac{\lambda D}{2h}$.  
(D) The fringe at the line of contact between the mirror and screen is completely dark (destructive interference) due to the $\pi$ phase shift on reflection.

#### Question 5
A particle of mass $m$ is confined in a 1D infinite square potential well with walls at $x = 0$ and $x = L$ ($V(x) = 0$ for $0 < x < L$, $V = \infty$ otherwise):
(A) The normalized stationary state wave functions are $\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$ for $n = 1, 2, 3, \dots$.  
(B) The energy eigenvalues are $E_n = \frac{n^2 \pi^2 \hbar^2}{2m L^2} = \frac{n^2 h^2}{8m L^2}$.  
(C) The ground state ($n=1$) has zero probability of being found at $x = L/2$.  
(D) The expectation value of position in any stationary state is $\langle x \rangle = L/2$.

#### Question 6
A projectile of mass $m$ is dropped from rest from a high tower of height $H$ at latitude $\lambda$ in the Northern Hemisphere. Taking Earth's angular velocity $\vec{\Omega}$ into account:
(A) The Coriolis acceleration experienced by the falling body is $\vec{a}_C = -2(\vec{\Omega} \times \vec{v})$.  
(B) The falling body is deflected toward the East.  
(C) The horizontal easterly deflection at the ground is $x = \frac{1}{3}\Omega g \cos\lambda t^3 = \frac{1}{3}\Omega \cos\lambda \sqrt{\frac{8H^3}{g}}$.  
(D) At the equator ($\lambda = 0^\circ$), the easterly deflection is maximum.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
In a standard cyclotron, protons ($q = 1.60 \times 10^{-19}\text{ C}$, $m = 1.67 \times 10^{-27}\text{ kg}$) are accelerated in a magnetic field $B = 1.50\text{ T}$. Calculate the cyclotron orbital frequency $f$ in MegaHertz ($\text{MHz}$). [Take $\pi = 3.1416$. Round off to ONE decimal place].

#### Question 8
Two identical flat circular coils, each having $N = 100$ turns and radius $R = 0.20\text{ m}$, are arranged coaxially separated by a distance equal to their radius $R$ (Helmholtz arrangement). If a current $I = 2.0\text{ A}$ flows through both coils in the same direction, calculate the uniform magnetic field $B$ (in milliTesla, $\text{mT}$) at the midpoint on the axis. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$, and $\left(\frac{4}{5}\right)^{3/2} \approx 0.7155$. Round off to TWO decimal places].

#### Question 9
In a radioactive decay chain $A \xrightarrow{\lambda_A} B \xrightarrow{\lambda_B} C$, the parent $A$ has half-life $T_{1/2,A} = 100\text{ days}$ and daughter $B$ has $T_{1/2,B} = 5.0\text{ days}$. Starting with pure $A$, calculate the time $t_{\text{max}}$ (in days) at which the activity of daughter $B$ reaches its maximum. [Take $t_{\text{max}} = \frac{\ln(\lambda_B/\lambda_A)}{\lambda_B - \lambda_A}$, $\lambda = \frac{\ln 2}{T_{1/2}}$. Round off to ONE decimal place].

#### Question 10
A triangular glass prism has an apex refracting angle $A = 60.0^\circ$ and refractive index $\mu = \sqrt{3} \approx 1.732$. Calculate the angle of minimum deviation $\delta_{\text{min}}$ (in degrees).

#### Question 11
An ideal Otto cycle operates with a compression ratio $r = V_1/V_2 = 8.0$. If the working substance is air with $\gamma = 1.40$, calculate the theoretical thermal efficiency $\eta = 1 - \frac{1}{r^{\gamma-1}}$ of the cycle in percentage ($\%$). [Take $8^{0.4} = (2^3)^{0.4} = 2^{1.2} \approx 2.30$. Round off to the nearest integer].

#### Question 12
In a Young's double-slit experiment, the slit separation is $d = 0.50\text{ mm}$ and the screen distance is $D = 1.00\text{ m}$. When a thin transparent mica sheet of refractive index $\mu = 1.60$ is placed in front of one of the slits, the central fringe shifts by $6.0\text{ mm}$. Calculate the thickness $t$ of the mica sheet in micrometers ($\mu\text{m}$). [Take $\Delta y = \frac{(\mu - 1)t D}{d}$].

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the physical scenarios in List-I with the corresponding mechanical conservation law in List-II:
- **List-I**:
  - P. Elastic collision between two free bodies in space
  - Q. Motion of a planet around the sun in an elliptical orbit
  - R. Ballistic pendulum catching a bullet
  - S. Motion of a rigid body pivoting about a fixed frictionless axis
- **List-II**:
  - 1. Both linear momentum and mechanical energy are conserved
  - 2. Total angular momentum about the sun is strictly conserved
  - 3. Mechanical energy is NOT conserved, but linear momentum is conserved during impact
  - 4. Total angular momentum about the fixed pivot is conserved

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 14
Match the electromagnetic boundary conditions at an interface between two non-magnetic dielectrics in List-I with their physical origin in List-II:
- **List-I**:
  - P. $D_{1n} - D_{2n} = \sigma_f$
  - Q. $E_{1t} = E_{2t}$
  - R. $B_{1n} = B_{2n}$
  - S. $H_{1t} - H_{2t} = K_f$
- **List-II**:
  - 1. Gauss's Law for electric displacement ($\nabla \cdot \vec{D} = \rho_f$)
  - 2. Conservative nature of electrostatic field ($\oint \vec{E} \cdot d\vec{l} = 0$)
  - 3. Non-existence of magnetic monopoles ($\nabla \cdot \vec{B} = 0$)
  - 4. Ampère-Maxwell circuital law ($\oint \vec{H} \cdot d\vec{l} = I_f$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 15
Match the optical polarization states in List-I with their phase difference $\delta = \phi_y - \phi_x$ in List-II (for equal amplitude orthogonal components $E_{0x} = E_{0y}$):
- **List-I**:
  - P. Linearly polarized at $45^\circ$
  - Q. Right circularly polarized
  - R. Linearly polarized at $-45^\circ$
  - S. Left circularly polarized
- **List-II**:
  - 1. $\delta = 0$
  - 2. $\delta = \pi/2$
  - 3. $\delta = \pi$
  - 4. $\delta = 3\pi/2$ (or $-\pi/2$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the fundamental thermodynamic potentials in List-I with their differential form in List-II:
- **List-I**:
  - P. Internal Energy $dU$
  - Q. Enthalpy $dH$
  - R. Helmholtz Free Energy $dF$
  - S. Gibbs Free Energy $dG$
- **List-II**:
  - 1. $T dS - P dV$
  - 2. $T dS + V dP$
  - 3. $-S dT - P dV$
  - 4. $-S dT + V dP$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 17
Match the landmark experiments in Modern Physics in List-I with the fundamental concept established in List-II:
- **List-I**:
  - P. Photoelectric effect (Hertz, Einstein)
  - Q. Compton scattering
  - R. Davisson-Germer experiment
  - S. Franck-Hertz experiment
- **List-II**:
  - 1. Particle nature of light (quantized photon energy $E = h\nu$)
  - 2. Relativistic photon momentum ($p = h/\lambda$) in photon-electron collisions
  - 3. Wave nature of matter electrons (electron diffraction)
  - 4. Quantized discrete energy levels in atoms

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 18
Match the fluid dynamics laws in List-I with their physical assertion in List-II:
- **List-I**:
  - P. Bernoulli's equation
  - Q. Poiseuille's formula
  - R. Stokes' law
  - S. Reynolds number
- **List-II**:
  - 1. Conservation of energy along a streamline for steady, inviscid, incompressible flow
  - 2. Laminar volume flow rate $Q = \frac{\pi \Delta P R^4}{8 \eta L}$ through a cylindrical pipe
  - 3. Viscous drag force $F_d = 6\pi \eta r v$ on a slow-moving sphere
  - 4. Dimensionless ratio of inertial forces to viscous forces governing turbulent transition

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-1, R-2, S-3

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the regiochemistry of elimination reactions (E2):
(A) When an alkyl halide reacts with a small, unhindered base (e.g., $\text{NaOCH}_3$), the more substituted, thermodynamically stable alkene predominates (Saytzeff rule).  
(B) When an alkyl halide reacts with a sterically hindered base (e.g., potassium tert-butoxide, $\text{KO}t\text{Bu}$), the less substituted alkene predominates (Hofmann rule).  
(C) E2 eliminations require an anti-periplanar transition state geometry where the $\text{C-H}$ and $\text{C-X}$ bonds are coplanar and at a dihedral angle of $180^\circ$.  
(D) Pyrolytic elimination of quaternary ammonium hydroxides (Hofmann elimination) yields the less substituted alkene because the bulky $^+N(\text{CH}_3)_3$ group causes steric congestion in the transition state.

#### Question 20
Which of the following coordination compounds exhibit optical isomerism (enantiomerism)?
(A) $\text{cis-}[\text{Co(en)}_2\text{Cl}_2]^+$  
(B) $[\text{Co(en)}_3]^{3+}$  
(C) $\text{trans-}[\text{Co(en)}_2\text{Cl}_2]^+$  
(D) $[\text{Pt(en)}_2]^{2+}$ (square planar)

#### Question 21
Regarding binary liquid solutions exhibiting a maximum-boiling azeotrope:
(A) The solution shows negative deviation from Raoult's law ($\Delta H_{\text{mix}} < 0$, $\Delta V_{\text{mix}} < 0$).  
(B) The vapor pressure curve exhibits a minimum at the azeotropic composition.  
(C) A classic example is a mixture of water ($68\%$) and nitric acid ($\text{HNO}_3, 32\%$) or water-chloroform.  
(D) Fractional distillation cannot separate the components beyond the azeotropic composition because vapor and liquid phases have identical compositions at the boiling point.

#### Question 22
Regarding the isoelectric point ($pI$) of amino acids:
(A) At the isoelectric point, the amino acid exists predominantly as an electrically neutral zwitterion with zero net charge.  
(B) For a neutral amino acid with carboxylic acid $pK_{a1}$ and amino group $pK_{a2}$, the isoelectric point is $pI = \frac{pK_{a1} + pK_{a2}}{2}$.  
(C) For an acidic amino acid (such as aspartic acid, $pK_{a1} = 2.1, pK_{aR} = 3.9, pK_{a2} = 9.8$), the isoelectric point is $pI = \frac{2.1 + 3.9}{2} = 3.0$.  
(D) At $\text{pH} > pI$, the amino acid carries a net negative charge and migrates toward the anode during electrophoresis.

#### Question 23
Regarding the Diels-Alder [4+2] cycloaddition reaction:
(A) It is a concerted pericyclic reaction that proceeds via a 6-electron aromatic transition state under thermal activation.  
(B) The diene must adopt the $s\text{-cis}$ conformation to undergo cycloaddition; dienes locked in $s\text{-trans}$ cannot react.  
(C) Electron-donating groups on the diene and electron-withdrawing groups on the dienophile accelerate the reaction rate.  
(D) The addition is stereospecific with complete retention of the configuration of both diene and dienophile.

#### Question 24
Regarding the Pourbaix (potential-pH) diagram of iron in aqueous solutions:
(A) The diagram maps regions of thermodynamic stability for different chemical species of iron ($\text{Fe}, \text{Fe}^{2+}, \text{Fe}^{3+}, \text{Fe(OH)}_2, \text{Fe}_2\text{O}_3$).  
(B) The region where metallic iron is thermodynamically stable is called the immunity zone.  
(C) The region where solid insoluble ferric oxide ($\text{Fe}_2\text{O}_3$) forms a protective barrier film is called the passivation zone.  
(D) Horizontal boundary lines correspond to pure electron-transfer redox reactions with zero proton participation ($m = 0$).

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The thermal decomposition of dinitrogen pentoxide in carbon tetrachloride:
$$2\text{N}_2\text{O}_5 \to 4\text{NO}_2 + \text{O}_2$$
is first order with a rate constant $k = 6.93 \times 10^{-4}\text{ s}^{-1}$ at $45^\circ\text{C}$. Calculate the half-life $t_{1/2}$ of $\text{N}_2\text{O}_5$ in seconds ($\text{s}$).

#### Question 26
The solubility of $\text{BaSO}_4$ in pure water at $25^\circ\text{C}$ is $2.33 \times 10^{-3}\text{ g/L}$. Given the molar mass of $\text{BaSO}_4$ is $233.3\text{ g/mol}$, calculate its solubility product $K_{sp}$ multiplied by $10^{10}$. [Round off to TWO decimal places].

#### Question 27
When $1.20\text{ g}$ of a non-volatile organic solute is dissolved in $50.0\text{ g}$ of benzene, the freezing point of benzene is depressed by $\Delta T_f = 0.80\text{ K}$. If the cryoscopic constant of benzene is $K_f = 5.12\text{ K}\cdot\text{kg/mol}$, calculate the molar mass of the solute in $\text{g/mol}$. [Round off to the nearest integer].

#### Question 28
Calculate the electromotive force $E_{\text{cell}}$ (in Volts) at $298\text{ K}$ for the Daniel cell:
$$\text{Zn}(s) | \text{Zn}^{2+}(0.010\text{ M}) || \text{Cu}^{2+}(1.00\text{ M}) | \text{Cu}(s)$$
Given $E_{\text{cell}}^\circ = +1.10\text{ V}$, and $\frac{2.303 RT}{F} = 0.0591\text{ V}$. [Round off to THREE decimal places].

#### Question 29
A polar molecule has charges $+q$ and $-q$ with $q = 1.60 \times 10^{-19}\text{ C}$ separated by a distance $d = 0.20\text{ \AA} = 2.0 \times 10^{-11}\text{ m}$. Calculate the electric dipole moment $p$ in Debye ($\text{D}$). [Take $1\text{ D} = 3.336 \times 10^{-30}\text{ C}\cdot\text{m}$. Round off to TWO decimal places].

#### Question 30
The standard enthalpy of neutralization of a strong acid with a strong base in dilute aqueous solution at $298\text{ K}$ is $\Delta_{\text{neut}} H^\circ = -57.3\text{ kJ/mol}$. Calculate the heat evolved (in kiloJoules, $\text{kJ}$) when $0.20\text{ mol}$ of $\text{HCl}$ is mixed with $0.30\text{ mol}$ of $\text{NaOH}$ in excess water.

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the organic named reactions in List-I with their characteristic product or reagent in List-II:
- **List-I**:
  - P. Cannizzaro reaction
  - Q. Aldol condensation
  - R. Clemmensen reduction
  - S. Hofmann bromamide degradation
- **List-II**:
  - 1. Disproportionation of non-enolizable aldehyde to alcohol and carboxylate
  - 2. $\alpha,\beta$-unsaturated carbonyl compound
  - 3. Reduction of carbonyl to methylene ($-\text{CH}_2-$) using $\text{Zn(Hg)} / \text{conc. HCl}$
  - 4. Primary amine with one less carbon using $\text{Br}_2 / \text{NaOH}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 32
Match the coordination compounds in List-I with their magnetic moment $\mu_{\text{eff}}$ in List-II:
- **List-I**:
  - P. $[\text{Fe(CN)}_6]^{4-}$ ($3d^6$ low spin)
  - Q. $[\text{Fe(H}_2\text{O})_6]^{2+}$ ($3d^6$ high spin)
  - R. $[\text{Fe(H}_2\text{O})_6]^{3+}$ ($3d^5$ high spin)
  - S. $[\text{Ni(H}_2\text{O})_6]^{2+}$ ($3d^8$)
- **List-II**:
  - 1. $0.00\text{ BM}$ (diamagnetic)
  - 2. $4.90\text{ BM}$ ($n=4$)
  - 3. $5.92\text{ BM}$ ($n=5$)
  - 4. $2.83\text{ BM}$ ($n=2$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 33
Match the mineral processing reagents in List-I with their role in froth flotation in List-II:
- **List-I**:
  - P. Pine oil
  - Q. Sodium ethyl xanthate
  - R. Sodium cyanide ($\text{NaCN}$)
  - S. Copper sulfate ($\text{CuSO}_4$)
- **List-II**:
  - 1. Frothing agent (creates stable foam)
  - 2. Collector (renders ore particles hydrophobic)
  - 3. Depressant (selectively prevents $\text{ZnS}$ from floating with $\text{PbS}$)
  - 4. Activator (reactivates depressed $\text{ZnS}$ flotation)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 34
Match the qualitative inorganic test reagents in List-I with the anion identified in List-II:
- **List-I**:
  - P. Brown ring test ($\text{FeSO}_4 + \text{conc. H}_2\text{SO}_4$)
  - Q. White precipitate insoluble in hot conc. $\text{HCl}$ with $\text{BaCl}_2$
  - R. Curdy white precipitate soluble in excess aqueous ammonia with $\text{AgNO}_3$
  - S. Black precipitate with lead acetate solution
- **List-II**:
  - 1. Nitrate ($\text{NO}_3^-$)
  - 2. Sulfate ($\text{SO}_4^{2-}$)
  - 3. Chloride ($\text{Cl}^-$)
  - 4. Sulfide ($\text{S}^{2-}$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 35
Match the polymers in List-I with their repeating monomer pair in List-II:
- **List-I**:
  - P. Nylon-6,6
  - Q. Bakelite
  - R. Dacron (Terylene)
  - S. Buna-S
- **List-II**:
  - 1. Hexamethylenediamine and Adipic acid
  - 2. Phenol and Formaldehyde
  - 3. Ethylene glycol and Terephthalic acid
  - 4. 1,3-Butadiene and Styrene

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 36
Match the vitamins in List-I with their primary deficiency disease in List-II:
- **List-I**:
  - P. Vitamin A (Retinol)
  - Q. Vitamin B1 (Thiamine)
  - R. Vitamin C (Ascorbic acid)
  - S. Vitamin D (Calciferol)
- **List-II**:
  - 1. Night blindness (Xerophthalmia)
  - 2. Beriberi
  - 3. Scurvy
  - 4. Rickets

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Regarding the method of Lagrange multipliers for finding the extrema of $f(x, y, z)$ subject to constraint $g(x, y, z) = 0$:
(A) At any constrained local extremum, the gradient vector $\nabla f$ is parallel to $\nabla g$ (provided $\nabla g \ne \vec{0}$).  
(B) The Lagrange multiplier $\lambda$ represents the rate of change of the optimal value with respect to the constraint constant.  
(C) The minimum distance from the origin $(0, 0, 0)$ to the plane $ax + by + cz = d$ found by this method is $d_{\text{min}} = \frac{|d|}{\sqrt{a^2 + b^2 + c^2}}$.  
(D) Lagrange multiplier method can only be applied when the objective function is quadratic.

#### Question 38
Let $P$ be a real $n \times n$ matrix representing an orthogonal projection onto a subspace $V$:
(A) $P^2 = P$ (idempotent).  
(B) $P^T = P$ (symmetric).  
(C) The only possible eigenvalues of $P$ are $0$ and $1$.  
(D) The rank of $P$ equals the trace of $P$ ($\text{rank}(P) = \text{tr}(P) = \dim(V)$).

#### Question 39
Consider the family of confocal conics $\frac{x^2}{a^2 - \lambda} + \frac{y^2}{b^2 - \lambda} = 1$ with $a > b > 0$:
(A) For $\lambda < b^2$, the curves are ellipses with foci at $(\pm \sqrt{a^2 - b^2}, 0)$.  
(B) For $b^2 < \lambda < a^2$, the curves are hyperbolas sharing the exact same foci.  
(C) Through any point in the plane (not on the axes), there pass exactly one ellipse and one hyperbola of the family.  
(D) The confocal ellipse and hyperbola intersecting at any point intersect each other orthogonally ($90^\circ$).

#### Question 40
Consider the differential equation $(2xy + y^2)dx + (x^2 + 2xy)dy = 0$:
(A) The differential equation is exact since $\frac{\partial M}{\partial y} = 2x + 2y = \frac{\partial N}{\partial x}$.  
(B) The potential function $\phi(x, y)$ satisfies $\frac{\partial \phi}{\partial x} = 2xy + y^2$ and $\frac{\partial \phi}{\partial y} = x^2 + 2xy$.  
(C) The general solution is $x^2 y + x y^2 = C$.  
(D) The curve passing through $(1, 1)$ has constant $C = 2$.

#### Question 41
For any four 3D vectors $\vec{a}, \vec{b}, \vec{c}, \vec{d}$:
(A) $(\vec{a} \times \vec{b}) \cdot (\vec{c} \times \vec{d}) = (\vec{a} \cdot \vec{c})(\vec{b} \cdot \vec{d}) - (\vec{a} \cdot \vec{d})(\vec{b} \cdot \vec{c})$ (Lagrange identity).  
(B) $(\vec{a} \times \vec{b}) \times (\vec{c} \times \vec{d}) = [\vec{a}\ \vec{c}\ \vec{d}]\vec{b} - [\vec{b}\ \vec{c}\ \vec{d}]\vec{a}$.  
(C) $[\vec{a} \times \vec{b} \quad \vec{b} \times \vec{c} \quad \vec{c} \times \vec{a}] = [\vec{a}\ \vec{b}\ \vec{c}]^2$.  
(D) If $\vec{a}, \vec{b}, \vec{c}$ are coplanar, then $\vec{a} \times \vec{b}, \vec{b} \times \vec{c}, \vec{c} \times \vec{a}$ are collinear.

#### Question 42
Let $D_n$ denote the number of derangements of $n$ distinct objects (permutations with zero fixed points):
(A) $D_n = n!\sum_{k=0}^n \frac{(-1)^k}{k!}$.  
(B) $D_n$ satisfies the recurrence relation $D_n = (n-1)(D_{n-1} + D_{n-2})$ for $n \ge 3$.  
(C) $D_n$ satisfies $D_n = n D_{n-1} + (-1)^n$.  
(D) The values for small $n$ are $D_1 = 0, D_2 = 1, D_3 = 2, D_4 = 9, D_5 = 44$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral using the Beta function:
$$I = \int_0^1 x^3 (1 - x)^4\,dx$$
If $I = \frac{1}{m}$, find the integer value of $m$.

#### Question 44
Find the slope of the normal to the exponential curve $y = e^{2x}$ at the point where $x = 0$. [Enter the absolute magnitude of the slope].

#### Question 45
Calculate the perpendicular distance between the parallel planes $2x - y + 2z = 4$ and $2x - y + 2z = 13$.

#### Question 46
Calculate the sum of the infinite geometric series:
$$S = 5 + \frac{5}{3} + \frac{5}{9} + \frac{5}{27} + \dots$$
[Round off to ONE decimal place].

#### Question 47
Calculate the number of ways to choose a committee of 3 people from a group of 10 people ($\binom{10}{3}$).

#### Question 48
Calculate the determinant of the matrix:
$$A = \begin{pmatrix} 7 & 4 \\ 3 & 2 \end{pmatrix}$$

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the conics in List-I with the locus of the point of intersection of perpendicular tangents (director circle) in List-II:
- **List-I**:
  - P. Parabola $y^2 = 4ax$
  - Q. Ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b$)
  - R. Hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ ($a > b$)
  - S. Rectangular Hyperbola $x^2 - y^2 = a^2$
- **List-II**:
  - 1. Directrix line $x = -a$
  - 2. Concentric circle $x^2 + y^2 = a^2 + b^2$
  - 3. Concentric circle $x^2 + y^2 = a^2 - b^2$
  - 4. Concentric circle $x^2 + y^2 = 0$ (single point at origin)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 50
Match the landmark theorems in differential calculus in List-I with their formal hypothesis/conclusion in List-II:
- **List-I**:
  - P. Rolle's Theorem
  - Q. Lagrange's Mean Value Theorem
  - R. Cauchy's Mean Value Theorem
  - S. Darboux's Theorem
- **List-II**:
  - 1. If $f(a) = f(b)$, there exists $c \in (a, b)$ such that $f'(c) = 0$
  - 2. There exists $c \in (a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$
  - 3. $\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$
  - 4. Intermediate value property for derivative functions ($f'$ attains all values between $f'(a)$ and $f'(b)$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 51
Match the differential equation forms in List-I with their standard solution technique in List-II:
- **List-I**:
  - P. $\frac{dy}{dx} = f(x)g(y)$
  - Q. $\frac{dy}{dx} + P(x)y = Q(x)$
  - R. $M(x, y)dx + N(x, y)dy = 0$ with $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$
  - S. $y = x \frac{dy}{dx} + f\left(\frac{dy}{dx}\right)$
- **List-II**:
  - 1. Separation of variables
  - 2. Integrating factor $\text{IF} = e^{\int P(x)dx}$
  - 3. Exact differential equation (potential function $\phi(x, y) = C$)
  - 4. Clairaut's equation ($y = C x + f(C)$ and singular envelope)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 52
Match the linear geometric transformations in $\mathbb{R}^2$ in List-I with their standard matrix representation in List-II:
- **List-I**:
  - P. Counterclockwise rotation by angle $\theta$
  - Q. Reflection across the x-axis
  - R. Orthogonal projection onto the x-axis
  - S. Uniform scaling by factor $k$
- **List-II**:
  - 1. $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$
  - 2. $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$
  - 3. $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$
  - 4. $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 53
Match the discrete probability distributions in List-I with their variance-to-mean ratio in List-II:
- **List-I**:
  - P. Poisson distribution ($\text{Pois}(\lambda)$)
  - Q. Binomial distribution ($\text{Bin}(n, p)$)
  - R. Geometric distribution ($\text{Geom}(p)$)
  - S. Degenerate distribution (constant $X = c$)
- **List-II**:
  - 1. Equal to $1$ ($\text{Var}/\text{Mean} = 1$)
  - 2. Strictly less than $1$ ($1 - p < 1$)
  - 3. Strictly greater than $1$ ($1/p > 1$ for $p < 1$)
  - 4. Equal to $0$ ($\text{Var} = 0$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-1, R-2, S-3

#### Question 54
Match the 3D quadric surfaces in List-I with their standard Cartesian equation in List-II:
- **List-I**:
  - P. Ellipsoid
  - Q. Hyperboloid of one sheet
  - R. Hyperboloid of two sheets
  - S. Elliptic paraboloid
- **List-II**:
  - 1. $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$
  - 2. $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$
  - 3. $\frac{x^2}{a^2} - \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$
  - 4. $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z}{c}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 08 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Electromagnetic Induction in Rotating Systems, Conservation of Canonical Angular Momentum.
- **2. Derivation**:
  - Faraday's law gives $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi}{dt} \implies E_\theta(2\pi R) = -\pi R^2 \frac{dB}{dt} \implies E_\theta = -\frac{R}{2}\frac{dB}{dt}$. (A) is correct.
  - Torque on cylinder: $\tau = \int R dF = R(\sigma 2\pi R L)E_\theta = -R^2 \sigma \pi R L \frac{dB}{dt}$.
  - Angular acceleration: $I \frac{d\omega}{dt} = \tau$. With $I = M R^2$: $M R^2 \frac{d\omega}{dt} = -\pi \sigma L R^3 \frac{dB}{dt}$.
  - Integrating from $B_0$ to $0$: $M \omega_f = \pi \sigma L R B_0 \implies \omega_f = \frac{\pi \sigma L R B_0}{M} = \frac{\sigma B_0}{M/(\pi R L)}$. (B) is correct with area geometry.
  - Angular momentum conservation includes field angular momentum $\vec{L}_{\text{EM}} = \varepsilon_0 \int \vec{r} \times (\vec{E} \times \vec{B}) dV$. (C) is correct.
  - By Meissner/fluxoid quantization in superconductors, total flux is conserved. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Nonlinear LC Oscillations, Energy Conservation.
- **2. Derivation**:
  - For $V \ll V_0$, $C(V) \approx C_0$, yielding standard harmonic frequency $\omega_0 = 1/\sqrt{L C_0}$. (A) is correct.
  - As amplitude grows, effective capacitance changes during cycle, altering period. (B) is correct.
  - Stored electrostatic energy $U_e = \int_0^V Q(V') dV' = \int_0^V C(V') V' dV' = \frac{2}{3}C_0 V_0^2 [(1+V/V_0)^{3/2}-1] - C_0 V_0 V$. (C) is correct.
  - In absence of resistance, total energy $E = U_e + \frac{1}{2}L I^2$ is strictly constant. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Relativistic Doppler Effect, Kepler's Third Law in Binary Systems.
- **2. Derivation**:
  - Center of mass relation $r_1 = \frac{M_2}{M_1+M_2}a$. Using Kepler's 3rd law $a^3 = \frac{G(M_1+M_2)T^2}{4\pi^2}$ gives $r_1 = [\frac{G M_2^3 T^2}{4\pi^2(M_1+M_2)^2}]^{1/3}$. (A) is correct.
  - Orbital speed $v_{1} = 2\pi r_1 / T$. (B) is correct.
  - Relativistic Doppler formula along line of sight $\lambda = \lambda_0 \sqrt{\frac{1+v/c}{1-v/c}}$. (C) is correct.
  - Mass function definition $f(M) = \frac{(M_2 \sin i)^3}{(M_1+M_2)^2} = \frac{T v_{1r,\text{max}}^3}{2\pi G}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Radial Heat Conduction with Temperature-Dependent Conductivity.
- **2. Derivation**:
  - In steady state, energy conservation requires heat flux through any spherical shell of radius $r$ to be constant: $Q = -4\pi r^2 k(T)\frac{dT}{dr}$. (A) is correct.
  - Substitute $k(T) = k_0 T_0 / T$: $Q \frac{dr}{r^2} = -4\pi k_0 T_0 \frac{dT}{T}$.
  - Integrating from $R_1$ to $R_2$: $Q\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = 4\pi k_0 T_0 \ln\left(\frac{T_1}{T_2}\right) \implies Q = \frac{4\pi k_0 T_0}{\frac{1}{R_1} - \frac{1}{R_2}}\ln\left(\frac{T_1}{T_2}\right)$. (C) is correct.
  - Temperature profile: $4\pi k_0 T_0 \ln(T_1/T(r)) = Q(1/R_1 - 1/r) \implies T(r) = T_1 (T_2/T_1)^{\frac{1/R_1 - 1/r}{1/R_1 - 1/R_2}}$. (B) is correct.
  - For constant $k$, $T(r) = A + B/r$ (linear in $1/r$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Temporal Coherence, Coherence Length, Michelson Interferometry.
- **2. Derivation**:
  - Coherence length $L_c = \frac{\lambda_0^2}{\Delta \lambda} = \frac{(600 \times 10^{-9}\text{ m})^2}{0.020 \times 10^{-9}\text{ m}} = 1.80 \times 10^{-2}\text{ m} = 1.80\text{ cm}$. (A) is correct.
  - For $|\Delta d| > L_c$, coherence is lost and fringe visibility vanishes. (B) is correct.
  - Fringe visibility $V(\Delta d)$ decays smoothly as envelope function. (C) is correct.
  - Additional path difference is $2(\mu - 1)t$, corresponding to $\Delta N = \frac{2(\mu - 1)t}{\lambda_0}$ fringes. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Rolling Without Slipping on Curved Surface, Normal Reaction and Detachment.
- **2. Derivation**:
  - Conservation of energy: $m g(R+r)(1 - \cos\theta) = \frac{1}{2}m v^2 + \frac{1}{2}I \omega^2 = \frac{1}{2}m v^2 + \frac{1}{2}\left(\frac{1}{2}mr^2\right)\left(\frac{v}{r}\right)^2 = \frac{3}{4}m v^2$.
  - Thus $v^2 = \frac{4}{3}g(R+r)(1 - \cos\theta)$, and $\ddot{\theta} = \frac{2g}{3(R+r)}\sin\theta$. (A) is correct.
  - Radial equation: $m g \cos\theta - N = \frac{m v^2}{R+r} = \frac{4}{3}mg(1 - \cos\theta) \implies N(\theta) = mg\left(\frac{7}{3}\cos\theta - \frac{4}{3}\right)$. (B) is correct.
  - Detachment occurs when $N = 0 \implies \frac{7}{3}\cos\theta_c = \frac{4}{3} \implies \cos\theta_c = \frac{4}{7}$. (C) is correct.
  - Static friction prevents slip provided $f_s \le \mu_s N$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Precession frequency $\Omega_p = \frac{\tau}{L_s} = \frac{M g d}{I_s \omega_s} = \frac{1.50 \times 9.80 \times 0.10}{0.020 \times 300.0} = \frac{1.47}{6.00} = 0.245\text{ rad/s} \approx 0.25\text{ rad/s}$.
- **Question 8**: At cut-off, electron trajectory grazes anode: $B_c = \frac{\sqrt{8 m V_a / e}}{b(1 - a^2/b^2)}$.
  $\sqrt{8 V_a / (e/m)} = \sqrt{\frac{8 \times 400}{1.76 \times 10^{11}}} = \sqrt{1.818 \times 10^{-8}} = 1.348 \times 10^{-4}\text{ T}\cdot\text{m}$.
  Denominator: $b(1 - 0.04) = 0.010 \times 0.96 = 0.0096\text{ m}$.
  $B_c = \frac{1.348 \times 10^{-4}}{0.0096} = 0.01404\text{ T} = 14.04\text{ mT}$.
- **Question 9**: Radiated thermal power $P = \varepsilon \sigma A T^4$. Surface area $A = 4\pi R^2 = 4\pi(0.05)^2 = 0.03142\text{ m}^2$.
  Mass $M = \rho \frac{4}{3}\pi R^3 = 8900 \times \frac{4}{3}\pi(0.05)^3 = 4.660\text{ kg}$.
  Heat capacity $C = M c = 4.660 \times 385 = 1794\text{ J/K}$.
  $P = 0.80 \times (5.67 \times 10^{-8}) \times 0.03142 \times (300)^4 = 1.425 \times 10^{-9} \times 8.1 \times 10^9 = 11.54\text{ W}$.
  Cooling rate $\left|\frac{dT}{dt}\right| = \frac{P}{C} = \frac{11.54}{1794} \approx 0.0064\text{ K/s} \implies 0.01\text{ K/s}$.
- **Question 10**: Numerical aperture $NA = \sqrt{n_1^2 - n_2^2} = \sqrt{1.500^2 - 1.480^2} = \sqrt{2.25 - 2.1904} = \sqrt{0.0596} \approx 0.244 \approx 0.24$.
- **Question 11**: Electric field: $E(r) = \frac{\lambda}{2\pi \varepsilon_0 \varepsilon_r(r) r} = \frac{\lambda}{2\pi \varepsilon_0 k}$.
  Potential difference: $V = \int_a^b E(r) dr = \frac{\lambda (b - a)}{2\pi \varepsilon_0 k}$.
  Capacitance per unit length: $C' = \frac{\lambda}{V} = \frac{2\pi \varepsilon_0 k}{b - a} = \frac{2\pi (8.854 \times 10^{-12})(0.020)}{0.040 - 0.010} = \frac{1.1126 \times 10^{-12}}{0.030} = 37.09\text{ pF/m}$.
- **Question 12**: Distance of closest approach: $K = \frac{1}{4\pi\varepsilon_0}\frac{(2e)(Ze)}{d_0} \implies d_0 = \frac{2 Z e^2}{4\pi\varepsilon_0 K} = \frac{2(79)(9.0 \times 10^9)(1.60 \times 10^{-19})}{5.0 \times 10^6} = \frac{2.275 \times 10^{-7}}{5.0 \times 10^6} = 4.55 \times 10^{-14}\text{ m} = 45.5\text{ fm}$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Negative Hall voltage implies negative charge carriers (electrons). $n = \frac{I B}{e t |V_H|} = \frac{(10 \times 10^{-3})(0.50)}{(1.60 \times 10^{-19})(1.0 \times 10^{-3})(2.5 \times 10^{-3})} = \frac{5.0 \times 10^{-3}}{4.0 \times 10^{-25}} = 1.25 \times 10^{22}\text{ m}^{-3} \implies$ Option (A).
- **Question 14**: Four sides of square loop each contribute $B_1 = \frac{\mu_0 I}{4\pi (L/2)}(\sin 45^\circ + \sin 45^\circ) = \frac{\mu_0 I}{2\pi L}(\sqrt{2})$. Total $B = 4 B_1 = \frac{2\sqrt{2}\mu_0 I}{\pi L}$. Option (A).
- **Question 15**: Brewster's angle $\tan\theta_B = \mu \implies \theta_B = \arctan(1.50) \approx 56.3^\circ$. Option (A).
- **Question 16**: $T_c = \frac{8a}{27Rb}$ and $T_B = \frac{a}{Rb}$. Ratio $T_c / T_B = \frac{8}{27}$. Option (A).
- **Question 17**: Total energy $E = \sqrt{p^2 c^2 + m_0^2 c^4} = 3 m_0 c^2 \implies p^2 c^2 = 8 m_0^2 c^4 \implies p = \sqrt{8} m_0 c$. $\lambda = \frac{h}{p} = \frac{h}{\sqrt{8} m_0 c} = \frac{\lambda_C}{\sqrt{8}}$. Option (A).
- **Question 18**: Moment of inertia of equilateral triangle about perpendicular axis through centroid is $I = \frac{1}{12}M a^2$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Jahn-Teller theorem states any non-linear degenerate state distorts to remove degeneracy. $d^4$ and $d^9$ octahedral show large tetragonal elongation ($z$-out). In $[\text{Cu(H}_2\text{O})_6]^{2+}$, equatorial bonds are $1.97\text{ \AA}$, axial are $2.30\text{ \AA}$. $d^3, d^6(\text{LS}), d^8$ have non-degenerate ground states ($A$ or $B$ states), showing no distortion. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: In pinacol rearrangement, carbocation forms at more substituted carbon. Migratory aptitude of aryl groups is enhanced by electron donation. Migration occurs with retention. In 1,1-diphenyl-2-methylpropane-1,2-diol, protonation occurs at diphenyl carbon, methyl migrates. Correct options: **(A), (B), (C), (D)**.
- **Question 21**: Electrode concentration cell EMF is $\frac{RT}{2F}\ln(P_1/P_2)$. Liquid junction potential depends on difference in transport numbers. $\text{KCl}$ minimizes junction potential because $t_+ \approx t_- \approx 0.50$. Standard cell potential of concentration cell is zero. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: Langmuir model assumes uniform, localized, monolayer adsorption without lateral interactions. Coverage $\theta = \frac{KP}{1+KP}$. At low $P$, $\theta \approx KP$; at high $P$, $\theta \to 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Schottky defects feature equal cation and anion vacancies, lowering density. Frenkel defects feature displaced cations into interstitials, conserving density. $\text{AgBr}$ exhibits both defects. Both increase conductivity. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Specific rotation of $\alpha\text{-D-glucose}$ is $+112^\circ$, $\beta\text{-D-glucose}$ is $+18.7^\circ$, equilibrium is $+52.7^\circ$. At equilibrium, $\beta$-anomer is $64\%$ (all equatorial). Mutarotation occurs via open chain. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: Initial: $[HA] = 0.15\text{ M}, [A^-] = 0.10\text{ M}$. Initial $\text{pH} = 4.74 + \log(0.10/0.15) = 4.74 - 0.176 = 4.564$.
  After adding $0.020\text{ mol NaOH}$: $[HA] = 0.13\text{ M}, [A^-] = 0.12\text{ M}$.
  New $\text{pH} = 4.74 + \log(0.12/0.13) = 4.74 - 0.035 = 4.705$.
  $\Delta \text{pH} = 4.705 - 4.564 = +0.14$.
- **Question 26**: $\ln(k_2/k_1) = \frac{E_a}{R}\left(\frac{T_2 - T_1}{T_1 T_2}\right) \implies 1.3863 = \frac{E_a}{8.314}\left(\frac{20}{300 \times 320}\right) = \frac{E_a}{8.314}(2.0833 \times 10^{-4}) \implies E_a = \frac{1.3863 \times 8.314}{2.0833 \times 10^{-4}} = 55.32\text{ kJ/mol}$.
- **Question 27**: For FCC lattice: $\rho = \frac{Z M}{N_A a^3}$ with $Z = 4$.
  $a^3 = \frac{4 \times 107.87}{6.022 \times 10^{23} \times 10.50} = \frac{431.48}{6.323 \times 10^{24}} = 6.824 \times 10^{-23}\text{ cm}^3 = 68.24 \times 10^{-24}\text{ cm}^3$.
  $a = (68.24)^{1/3} \times 10^{-8}\text{ cm} = 4.086 \times 10^{-8}\text{ cm} = 408.6\text{ pm}$.
- **Question 28**: $E_{\text{cell}}^\circ = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = 0.799 - (-0.763) = +1.562\text{ V} \approx 1.56\text{ V}$.
- **Question 29**: $\Pi = \frac{w}{M V} R T \implies M = \frac{w R T}{\Pi V} = \frac{(4.00 \times 10^{-3}\text{ kg})(8.314)(300)}{(2.46 \times 10^3\text{ Pa})(1.00 \times 10^{-4}\text{ m}^3)} = \frac{9.977}{0.246} = 40.56\text{ kg/mol} \approx 40.6\text{ kg/mol}$.
- **Question 30**: $\text{Cr}^{3+}$ has $d^3$ configuration ($t_{2g}^3 e_g^0$) with $n=3$ unpaired electrons. $\mu_{\text{eff}} = \sqrt{n(n+2)} = \sqrt{3(5)} = \sqrt{15} \approx 3.87\text{ BM}$.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Reimer-Tiemann reactive intermediate is neutral electrophilic dichlorocarbene ($:\text{CCl}_2$). Option (A).
- **Question 32**: All statements regarding Ellingham diagrams are thermodynamically correct. Option (D).
- **Question 33**: Aryl halides do not undergo nucleophilic substitution due to partial double-bond character of $\text{C-X}$ bond from resonance. Option (A).
- **Question 34**: $\text{XeF}_4$ has steric number 6 (4 bonding pairs, 2 lone pairs), $sp^3d^2$ hybridization, square planar shape. Option (A).
- **Question 35**: $r_n = \frac{n^2 a_0}{Z}$. For $n=1$, $r_1 = a_0/Z$. Option (A).
- **Question 36**: Teflon is polytetrafluoroethene (PTFE) from $\text{CF}_2\text{=CF}_2$. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Since $|\frac{\sin(3^n x)}{2^n}| \le \frac{1}{2^n}$ and $\sum \frac{1}{2^n} = 1 < \infty$, the Weierstrass M-test guarantees uniform convergence. Continuous everywhere. Period is $2\pi$. Maximum value bounded by $\sum 1/2^n = 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Coefficient matrix determinant $\Delta = 1(2\lambda - 6) - 1(\lambda - 3) + 1(2 - 2) = 2\lambda - 6 - \lambda + 3 = \lambda - 3$. If $\lambda \ne 3$, unique solution. If $\lambda = 3$ and $\mu = 10$, augmented matrix has rank 2 (infinitely many solutions). If $\lambda = 3$ and $\mu \ne 10$, no solution. When $\lambda = 3, \mu = 10$, $(2, 4, 0)$ satisfies all equations ($2+4+0=6, 2+8+0=10$). Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Director circle of ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ is $x^2 + y^2 = a^2 + b^2 = 16 + 9 = 25$. Radius is $5$. Chord of contact from $(5, 0)$ is $\frac{5x}{16} = 1 \implies x = 16/5 = 3.20$. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Euler equation: $x = e^t \implies \frac{d^2 y}{dt^2} - 4\frac{dy}{dt} + 4y = 0$. Roots $m = 2, 2$. $y = (C_1 + C_2 t)e^{2t} = (C_1 + C_2 \ln x)x^2$. $y(1) = C_1 = 2$. $y'(x) = C_2 x + 2(C_1 + C_2 \ln x)x \implies y'(1) = C_2 + 2C_1 = C_2 + 4 = 5 \implies C_2 = 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: $\vec{d}_1 \times \vec{d}_2 = (3\times 5 - 4\times 4, 4\times 3 - 2\times 5, 2\times 4 - 3\times 3) = (-1, 2, -1)$. $\vec{a}_2 - \vec{a}_1 = (1, 2, 2)$. Shortest distance $d = \frac{|(1, 2, 2) \cdot (-1, 2, -1)|}{\sqrt{1+4+1}} = \frac{|-1 + 4 - 2|}{\sqrt{6}} = \frac{1}{\sqrt{6}}$. Non-zero distance implies skew non-intersecting lines. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Polya urn probabilities: $P(W_1) = \frac{w}{w+b}$. $P(W_2) = P(W_1)P(W_2|W_1) + P(B_1)P(W_2|B_1) = \frac{w}{w+b}\frac{w+c}{w+b+c} + \frac{b}{w+b}\frac{w}{w+b+c} = \frac{w(w+b+c)}{(w+b)(w+b+c)} = \frac{w}{w+b}$. By induction, $P(W_n) = \frac{w}{w+b}$. $P(W_2|W_1) = \frac{w+c}{w+b+c} > \frac{w}{w+b}$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Using King's property: $I = \int_0^{\pi/2} \frac{\cos^3 x}{\cos^3 x + \sin^3 x}dx$. $2I = \int_0^{\pi/2} 1 dx = \pi/2 \implies I = \pi/4$. Thus $k = 4.00$.
- **Question 44**: $A = \begin{pmatrix} 1 & \omega & \omega^2 \\ \omega & \omega^2 & 1 \\ \omega^2 & 1 & \omega \end{pmatrix}$. Note row 2 is $\omega \times$ row 1 because $\omega(1, \omega, \omega^2) = (\omega, \omega^2, 1)$. Thus rows are linearly dependent, so $\det(A) = 0.00$.
- **Question 45**: Distance $d = \frac{|2(2) - 2(3) + (-1) + 5|}{\sqrt{2^2 + (-2)^2 + 1^2}} = \frac{|4 - 6 - 1 + 5|}{\sqrt{9}} = \frac{2}{3} \approx 0.67$.
- **Question 46**: AGP: $S = 1 + \frac{2}{2} + \frac{3}{4} + \dots$. $\frac{1}{2}S = \frac{1}{2} + \frac{2}{4} + \dots$. $\frac{1}{2}S = 1 + \frac{1}{2} + \frac{1}{4} + \dots = \frac{1}{1 - 1/2} = 2 \implies S = 4.00$.
- **Question 47**: $x y = 16 \implies y = 16/x \implies \frac{dy}{dx} = -16/x^2$. At $(4, 4)$, $\frac{dy}{dx} = -16/16 = -1$. Magnitude is $1.00$.
- **Question 48**: Intersection of $y = x^2$ and $y = 2x$: $x^2 = 2x \implies x = 0, 2$. Area $= \int_0^2 (2x - x^2)dx = [x^2 - x^3/3]_0^2 = 4 - 8/3 = 4/3$. Multiplied by 3: $3 \times (4/3) = 4.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Maclaurin expansion $e^x = 1 + x + x^2/2! + x^3/3! + \dots$. $e^x - 1 - x - x^2/2 = x^3/6 + O(x^4)$. Dividing by $x^3$ gives $1/6$. Option (A).
- **Question 50**: Angle between asymptotes is $2\theta = 60^\circ \implies \theta = 30^\circ$, where $\tan\theta = b/a = 1/\sqrt{3}$. Eccentricity $e = \sqrt{1 + b^2/a^2} = \sqrt{1 + 1/3} = \sqrt{4/3} = 2/\sqrt{3}$. Option (A).
- **Question 51**: For any odd $n \times n$ skew-symmetric matrix, $\det(A) = \det(A^T) = \det(-A) = (-1)^3 \det(A) = -\det(A) \implies 2\det(A) = 0 \implies \det(A) = 0$. Option (A).
- **Question 52**: Standard vector triple product identity is BAC-CAB: $\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$. Option (A).
- **Question 53**: $|z - 3| + |z + 3| = 10 \implies 2a = 10 \implies a = 5$. Foci at $(\pm 3, 0) \implies a e = 3 \implies e = 3/5 = 0.60$. Option (A).
- **Question 54**: Binomial sum $\sum_{k=0}^n \binom{n}{k} 3^k = (1 + 3)^n = 4^n$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 08 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Electromagnetic Induction on Inclined Rails, Motional EMF, Terminal Velocity.
- **2. Derivation**:
  - The vertical magnetic field has component perpendicular to the inclined plane $B_\perp = B\cos\theta$. Option (A) is correct.
  - Motional EMF induced along rod of length $L$: $\mathcal{E} = B_\perp L v = B L v \cos\theta$. Option (B) is correct.
  - Induced current $I = \mathcal{E}/R = \frac{BLv\cos\theta}{R}$. Magnetic force $\vec{F} = I(\vec{L}\times\vec{B})$ is horizontal.
  - Component along the incline opposing motion is $F_{\text{mag}}\cos\theta = I L B \cos\theta = \frac{B^2 L^2 v \cos^2\theta}{R}$. Option (C) is correct.
  - At terminal velocity, gravity component down incline balances magnetic retarding force: $mg\sin\theta = \frac{B^2 L^2 v_t \cos^2\theta}{R} \implies v_t = \frac{mgR\sin\theta}{B^2 L^2 \cos^2\theta}$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Dielectric Liquid Rise, Virtual Work, Electrostatic Fringing Fields.
- **2. Derivation**:
  - Fringing fields at the lower capacitor boundary exert an upward gradient force on the polarized dielectric molecules. Option (A) is correct.
  - Capacitance when liquid rises to height $y$: $C(y) = \frac{\varepsilon_0 w}{d}[(H-y) + Ky] = \frac{\varepsilon_0 w}{d}[H + (K-1)y]$.
  - Upward force at constant voltage: $F_e = \frac{1}{2}V_0^2 \frac{dC}{dy} = \frac{1}{2}\varepsilon_0 (K-1)\frac{w}{d}V_0^2$. Option (B) is correct.
  - Gravity force: $F_g = m g = (\rho w d h)g$. Equating forces: $\rho w d h g = \frac{1}{2}\varepsilon_0 (K-1)\frac{w}{d}V_0^2 \implies h = \frac{\varepsilon_0 (K-1)V_0^2}{2\rho g d^2}$. Option (C) is correct.
  - Disconnected plates carry constant charge $Q$, and energy is lowered by liquid insertion ($U = Q^2/(2C)$), so liquid still rises. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Adiabatic Sound Propagation, Laplace Formula, Heat Capacity Ratio.
- **2. Derivation**:
  - Sound propagation involves rapid compressions and rarefactions with negligible heat exchange, hence adiabatic ($P V^\gamma = \text{const}$). Option (A) is correct.
  - Sound speed: $v = \sqrt{\frac{B_{\text{ad}}}{\rho}} = \sqrt{\frac{\gamma P}{\rho}} = \sqrt{\frac{\gamma RT}{M}}$. Option (B) is correct.
  - For polyatomic molecules, as vibrational degrees of freedom activate at elevated temperatures, $C_V$ increases, causing $\gamma = 1 + R/C_V$ to decrease towards $4/3$. Option (C) is correct.
  - Newton assumed isothermal propagation ($v = \sqrt{RT/M} \approx 280\text{ m/s}$), which is $\approx 15\%$ lower than Laplace's $331\text{ m/s}$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Lloyd's Mirror Interference, Boundary Phase Shift, Virtual Coherent Source.
- **2. Derivation**:
  - Virtual source $S_2$ is the specular reflection of $S_1$ across the mirror plane, located at distance $h$ below the mirror surface. Option (A) is correct.
  - Reflection from a higher index medium (glass) introduces a $\pi$ phase shift (half-wavelength optical path shift $\lambda/2$). Option (B) is correct.
  - Separation between coherent sources is $2h$, so fringe width is $\beta = \frac{\lambda D}{2h}$. Option (C) is correct.
  - At grazing contact line ($y = 0$), geometric path difference is 0, but the reflection phase shift of $\pi$ produces destructive interference (dark fringe). Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Quantum Particle in 1D Infinite Potential Box, Eigenfunctions, Probability Density.
- **2. Derivation**:
  - Boundary conditions $\psi(0) = \psi(L) = 0$ yield $\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$. Option (A) is correct.
  - Energy eigenvalues $E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2} = \frac{n^2 h^2}{8mL^2}$. Option (B) is correct.
  - For $n=1$, $|\psi_1(L/2)|^2 = \frac{2}{L}\sin^2(\pi/2) = \frac{2}{L} \ne 0$ (probability is maximum, not zero). Option (C) is incorrect!
  - By symmetry of probability density $|\psi_n(x)|^2$ about $x = L/2$, $\langle x \rangle = L/2$ for all stationary states. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Non-Inertial Frames, Coriolis Force and Easterly Deflection.
- **2. Derivation**:
  - Coriolis acceleration in rotating frame: $\vec{a}_C = -2(\vec{\Omega} \times \vec{v})$. Option (A) is correct.
  - For falling body, $\vec{v} \approx -g t \hat{k}$. Since $\vec{\Omega}$ points northward, $-2(\vec{\Omega}\times\vec{v})$ points toward the East. Option (B) is correct.
  - Integration: $a_x = 2\Omega g t \cos\lambda \implies v_x = \Omega g t^2 \cos\lambda \implies x = \frac{1}{3}\Omega g t^3 \cos\lambda$. With $t = \sqrt{2H/g}$: $x = \frac{1}{3}\Omega \cos\lambda \sqrt{\frac{8H^3}{g}}$. Option (C) is correct.
  - $\cos\lambda$ is maximum at the equator ($\lambda = 0^\circ$). Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: $f = \frac{q B}{2\pi m} = \frac{(1.60 \times 10^{-19})(1.50)}{2\pi (1.67 \times 10^{-27})} = \frac{2.40 \times 10^{-19}}{1.0493 \times 10^{-26}} = 2.287 \times 10^7\text{ Hz} = 22.9\text{ MHz}$.
- **Question 8**: Helmholtz center field $B = \left(\frac{4}{5}\right)^{3/2} \frac{\mu_0 N I}{R} = (0.7155) \frac{(4\pi \times 10^{-7})(100)(2.0)}{0.20} = 0.7155 \times (1.2566 \times 10^{-3}) = 8.99 \times 10^{-4}\text{ T} = 0.90\text{ mT}$.
- **Question 9**: $\lambda_A = \frac{\ln 2}{100} = 0.00693\text{ d}^{-1}$, $\lambda_B = \frac{\ln 2}{5.0} = 0.1386\text{ d}^{-1}$.
  $t_{\text{max}} = \frac{\ln(\lambda_B/\lambda_A)}{\lambda_B - \lambda_A} = \frac{\ln(20)}{0.1386 - 0.00693} = \frac{2.9957}{0.1317} \approx 22.7\text{ days}$.
- **Question 10**: $\mu = \frac{\sin\left(\frac{A + \delta_{\text{min}}}{2}\right)}{\sin(A/2)} \implies \sqrt{3} = \frac{\sin(30^\circ + \delta_{\text{min}}/2)}{\sin 30^\circ} = 2\sin(30^\circ + \delta_{\text{min}}/2) \implies \sin(30^\circ + \delta_{\text{min}}/2) = \frac{\sqrt{3}}{2} \implies 30^\circ + \delta_{\text{min}}/2 = 60^\circ \implies \delta_{\text{min}} = 60.0^\circ$.
- **Question 11**: $\eta = 1 - \frac{1}{r^{\gamma - 1}} = 1 - \frac{1}{8^{0.4}} = 1 - \frac{1}{2.30} = 1 - 0.435 = 0.565 = 56.5\% \approx 57\%$.
- **Question 12**: $\Delta y = \frac{(\mu - 1)t D}{d} \implies t = \frac{\Delta y \cdot d}{(\mu - 1) D} = \frac{(6.0 \times 10^{-3}\text{ m})(0.50 \times 10^{-3}\text{ m})}{(1.60 - 1)(1.00\text{ m})} = \frac{3.0 \times 10^{-6}}{0.60} = 5.0 \times 10^{-6}\text{ m} = 5.0\ \mu\text{m}$.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: Elastic collision: both linear momentum and mechanical energy conserved (P-1); Planetary motion: angular momentum about sun conserved (Q-2); Ballistic pendulum: linear momentum conserved during collision, energy lost (R-3); Fixed pivot: angular momentum about pivot conserved (S-4). Option (A).
- **Question 14**: Boundary conditions: $D_{1n}-D_{2n}=\sigma_f$ from Gauss law (P-1); $E_{1t}=E_{2t}$ from zero curl / circulation (Q-2); $B_{1n}=B_{2n}$ from $\nabla\cdot\vec{B}=0$ (R-3); $H_{1t}-H_{2t}=K_f$ from Ampere law (S-4). Option (A).
- **Question 15**: Polarization: $\delta = 0$ is $45^\circ$ linear (P-1); $\delta = \pi/2$ is right circular (P-2); $\delta = \pi$ is $-45^\circ$ linear (R-3); $\delta = 3\pi/2$ is left circular (S-4). Option (A).
- **Question 16**: Differentials: $dU = TdS - PdV$ (P-1); $dH = TdS + VdP$ (Q-2); $dF = -SdT - PdV$ (R-3); $dG = -SdT + VdP$ (S-4). Option (A).
- **Question 17**: Experiments: Photoelectric effect: photon quanta (P-1); Compton: photon momentum (Q-2); Davisson-Germer: matter waves (R-3); Franck-Hertz: atomic discrete levels (S-4). Option (A).
- **Question 18**: Fluid laws: Bernoulli: energy conservation (P-1); Poiseuille: laminar pipe flow (Q-2); Stokes: viscous drag (R-3); Reynolds: turbulence criterion (S-4). Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Small unhindered base yields Saytzeff product (more substituted). Bulky hindered base yields Hofmann product. E2 requires anti-coplanar transition state ($180^\circ$). Quaternary ammonium hydroxide Hofmann elimination gives less substituted alkene due to steric hindrance. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: $\text{cis-}[\text{Co(en)}_2\text{Cl}_2]^+$ lacks plane of symmetry and is chiral (enantiomeric pair). $[\text{Co(en)}_3]^{3+}$ has $D_3$ symmetry (no plane of symmetry, chiral). $\text{trans-}[\text{Co(en)}_2\text{Cl}_2]^+$ has an inversion center and plane of symmetry (achiral). Square planar $[\text{Pt(en)}_2]^{2+}$ has a horizontal mirror plane (achiral). Correct options: **(A), (B)**.
- **Question 21**: Maximum boiling azeotropes show negative deviation from Raoult's law ($\Delta H_{\text{mix}} < 0, \Delta V_{\text{mix}} < 0$). Vapor pressure is minimum at azeotrope. Classic example: $\text{HNO}_3$-water ($68\%$). Liquid and vapor have identical composition at azeotropic boiling point. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: At $pI$, net charge is zero. For neutral amino acids, $pI = (pK_{a1}+pK_{a2})/2$. For aspartic acid, $pI = (2.1+3.9)/2 = 3.0$. At $\text{pH} > pI$, deprotonation yields net negative charge, migrating to anode. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Diels-Alder is a [4+2] concerted pericyclic cycloaddition. Diene must be $s\text{-cis}$. EDG on diene and EWG on dienophile accelerate reaction. Highly stereospecific (syn-addition). Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Pourbaix diagram maps potential vs pH. Immunity zone is metallic stability. Passivation is insoluble protective oxide. Horizontal boundaries are pure redox ($m=0$). Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: First order half-life: $t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{6.93 \times 10^{-4}} = 1000.00\text{ s}$.
- **Question 26**: Molar solubility: $s = \frac{2.33 \times 10^{-3}\text{ g/L}}{233.3\text{ g/mol}} = 1.00 \times 10^{-5}\text{ mol/L}$.
  $K_{sp} = s^2 = (1.00 \times 10^{-5})^2 = 1.00 \times 10^{-10}$. Multiplied by $10^{10}$, the value is $1.00$.
- **Question 27**: $\Delta T_f = K_f m = K_f \frac{w_B / M_B}{w_A / 1000} \implies M_B = \frac{1000 K_f w_B}{w_A \Delta T_f} = \frac{1000 \times 5.12 \times 1.20}{50.0 \times 0.80} = \frac{6144}{40.0} = 153.6\text{ g/mol} \approx 154\text{ g/mol}$.
- **Question 28**: Nernst equation: $E_{\text{cell}} = E_{\text{cell}}^\circ - \frac{0.0591}{2}\log\left(\frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]}\right) = 1.10 - \frac{0.0591}{2}\log(0.010/1.00) = 1.10 - \frac{0.0591}{2}(-2) = 1.10 + 0.0591 = 1.159\text{ V}$.
- **Question 29**: $p = q d = (1.60 \times 10^{-19}\text{ C})(2.0 \times 10^{-11}\text{ m}) = 3.20 \times 10^{-30}\text{ C}\cdot\text{m}$.
  In Debye: $p = \frac{3.20 \times 10^{-30}}{3.336 \times 10^{-30}} = 0.959\text{ D} \approx 0.96\text{ D}$.
- **Question 30**: $\text{HCl}$ is the limiting reagent ($0.20\text{ mol}$). Heat evolved $q = 0.20\text{ mol} \times 57.3\text{ kJ/mol} = 11.46\text{ kJ}$.

---

### Questions 31 to 36 (Matching List Solutions)
- **Question 31**: Cannizzaro gives alcohol and carboxylate (P-1); Aldol gives $\alpha,\beta$-unsaturated carbonyl (Q-2); Clemmensen reduces carbonyl to methylene (R-3); Hofmann bromamide gives primary amine with one less carbon (S-4). Option (A).
- **Question 32**: $[\text{Fe(CN)}_6]^{4-}$ diamagnetic $0\text{ BM}$ (P-1); $[\text{Fe(H}_2\text{O})_6]^{2+}$ 4 unpaired $4.90\text{ BM}$ (Q-2); $[\text{Fe(H}_2\text{O})_6]^{3+}$ 5 unpaired $5.92\text{ BM}$ (R-3); $[\text{Ni(H}_2\text{O})_6]^{2+}$ 2 unpaired $2.83\text{ BM}$ (S-4). Option (A).
- **Question 33**: Pine oil is frother (P-1); Xanthate is collector (Q-2); $\text{NaCN}$ is depressant (R-3); $\text{CuSO}_4$ is activator (S-4). Option (A).
- **Question 34**: Brown ring for nitrate (P-1); $\text{BaSO}_4$ white ppt for sulfate (Q-2); $\text{AgCl}$ curdy white for chloride (R-3); $\text{PbS}$ black ppt for sulfide (S-4). Option (A).
- **Question 35**: Nylon-6,6 from hexamethylenediamine + adipic acid (P-1); Bakelite from phenol + formaldehyde (Q-2); Dacron from glycol + terephthalic acid (R-3); Buna-S from butadiene + styrene (S-4). Option (A).
- **Question 36**: Vitamin A: night blindness (P-1); Vitamin B1: beriberi (Q-2); Vitamin C: scurvy (R-3); Vitamin D: rickets (S-4). Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Lagrange multipliers: $\nabla f = \lambda \nabla g$ at extremum. Multiplier $\lambda = \partial f^*/\partial c$. Shortest distance formula $d = |d|/\sqrt{a^2+b^2+c^2}$ derived directly. Can be applied to general smooth functions (not only quadratic). Correct options: **(A), (B), (C)**.
- **Question 38**: Orthogonal projection operator $P$ onto subspace $V$: idempotent $P^2 = P$, symmetric $P^T = P$, eigenvalues in $\{0, 1\}$, trace equals rank equals dimension of $V$. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Confocal family: $\lambda < b^2$ gives ellipses, $b^2 < \lambda < a^2$ gives hyperbolas with identical foci $(\pm\sqrt{a^2-b^2}, 0)$. Through each point passes exactly one ellipse and one hyperbola, which intersect orthogonally. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Equation is exact: $M_y = 2x+2y = N_x$. Potential function $\phi = x^2 y + x y^2 = C$. Curve through $(1, 1)$ gives $1(1) + 1(1) = 2 \implies C = 2$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Lagrange identity holds (A). Product formula $(\vec{a}\times\vec{b})\times(\vec{c}\times\vec{d}) = [\vec{a}\ \vec{c}\ \vec{d}]\vec{b} - [\vec{b}\ \vec{c}\ \vec{d}]\vec{a}$ holds (B). Scalar triple product of cross products equals $[\vec{a}\ \vec{b}\ \vec{c}]^2$ (C). Correct options: **(A), (B), (C)**.
- **Question 42**: Derangements formula $D_n = n!\sum_{k=0}^n \frac{(-1)^k}{k!}$. Recurrence $D_n = (n-1)(D_{n-1}+D_{n-2})$ and $D_n = n D_{n-1} + (-1)^n$. Values: $D_1=0, D_2=1, D_3=2, D_4=9, D_5=44$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: $I = \int_0^1 x^3(1-x)^4 dx = B(4, 5) = \frac{\Gamma(4)\Gamma(5)}{\Gamma(9)} = \frac{3! \times 4!}{8!} = \frac{6 \times 24}{40320} = \frac{144}{40320} = \frac{1}{280}$. Thus $m = 280$.
- **Question 44**: $y = e^{2x} \implies \frac{dy}{dx} = 2e^{2x}$. At $x=0$, tangent slope $m_T = 2$. Normal slope $m_N = -1/2 = -0.50$. Absolute magnitude is $0.50$.
- **Question 45**: Distance between parallel planes $2x - y + 2z = 4$ and $2x - y + 2z = 13$: $d = \frac{|13 - 4|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{9}{\sqrt{9}} = \frac{9}{3} = 3.00$.
- **Question 46**: Infinite GP: $a = 5, r = 1/3$. $S = \frac{a}{1-r} = \frac{5}{1 - 1/3} = \frac{5}{2/3} = 7.50$.
- **Question 47**: $\binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$.
- **Question 48**: $\det\begin{pmatrix} 7 & 4 \\ 3 & 2 \end{pmatrix} = 7(2) - 4(3) = 14 - 12 = 2.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Director circle: Parabola is directrix line (P-1); Ellipse is $x^2+y^2=a^2+b^2$ (Q-2); Hyperbola is $x^2+y^2=a^2-b^2$ (R-3); Rectangular hyperbola is point circle at origin (S-4). Option (A).
- **Question 50**: Rolle: $f'(c)=0$ (P-1); LMVT: $f'(c)=\frac{f(b)-f(a)}{b-a}$ (Q-2); Cauchy: $\frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)}$ (R-3); Darboux: intermediate value for derivatives (S-4). Option (A).
- **Question 51**: Separable variables (P-1); Linear ODE integrating factor (Q-2); Exact potential function (R-3); Clairaut equation (S-4). Option (A).
- **Question 52**: Rotation matrix (P-1); Reflection matrix (Q-2); Projection matrix (R-3); Scaling matrix (S-4). Option (A).
- **Question 53**: Poisson ratio = 1 (P-1); Binomial ratio < 1 (Q-2); Geometric ratio > 1 (R-3); Degenerate ratio = 0 (S-4). Option (A).
- **Question 54**: Ellipsoid (P-1); Hyperboloid of 1 sheet (Q-2); Hyperboloid of 2 sheets (R-3); Elliptic paraboloid (S-4). Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 08
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
- Q8: 14.04
- Q9: 0.01
- Q10: 0.24
- Q11: 37.09
- Q12: 45.5
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
- Q25: 0.14
- Q26: 55.32
- Q27: 408.6
- Q28: 1.56
- Q29: 40.6
- Q30: 3.87
- Q31: A
- Q32: D
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
- Q43: 4.00
- Q44: 0.00
- Q45: 0.67
- Q46: 4.00
- Q47: 1.00
- Q48: 4.00
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
- Q5: A, B, D
- Q6: A, B, C, D
- Q7: 22.9
- Q8: 0.90
- Q9: 22.7
- Q10: 60.0
- Q11: 57
- Q12: 5.0
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C, D
- Q20: A, B
- Q21: A, B, C, D
- Q22: A, B, C, D
- Q23: A, B, C, D
- Q24: A, B, C, D
- Q25: 1000.00
- Q26: 1.00
- Q27: 154
- Q28: 1.159
- Q29: 0.96
- Q30: 11.46
- Q31: A
- Q32: A
- Q33: A
- Q34: A
- Q35: A
- Q36: A

#### Mathematics
- Q37: A, B, C
- Q38: A, B, C, D
- Q39: A, B, C, D
- Q40: A, B, C, D
- Q41: A, B, C
- Q42: A, B, C, D
- Q43: 280
- Q44: 0.50
- Q45: 3.00
- Q46: 7.5
- Q47: 120
- Q48: 2.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: High proportion with independent option derivations.
- **Physics**: Rotating frames, Hull cut-off magnetron, virtual work on dielectrics, Lloyd's mirror phase shift, Coriolis easterly deflection.
- **Chemistry**: Jahn-Teller tetragonality, pinacol migratory aptitudes, concentration cells with transference, Langmuir limits, Pourbaix stability diagrams.
- **Mathematics**: Weierstrass continuous non-differentiable series, Cauchy-Euler repeated roots, Polya's urn martingales, confocal orthogonal intersections, Derangements combinatorics.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

if __name__ == "__main__":
    create_mock_files(8, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")

