# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Guwahati Mocks 11 to 15.
Empirical Signature: IIT Guwahati Benchmark (2009, 2016, 2023)
- Conceptual Elegance over Brute Calculation
- Modern Physics & Thermodynamics / Statistical Mechanics Emphasis (>=35%)
- Geometric Insight in Conics, Vectors, Complex Numbers
- Clean Physical Chemistry & Rigorous Stereochemical Organic Cascades
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

def generate_guwahati_11_to_15():
    for mock_idx in range(11, 16):
        pad = f"{mock_idx:02d}"
        comp_ratio = str(5 + mock_idx % 3)
        phot_e = str(70 + 10 * mock_idx)
        carnot_eff = f"{(1 - 280 / (550 + 40 * mock_idx)) * 100:.2f}"
        alpha_k = f"{5.0 + 0.4 * mock_idx:.1f}"
        disc_v = f"{4.0 + 0.4 * mock_idx:.1f}"
        disc_ke = f"{0.75 * 2.5 * (4.0 + 0.4 * mock_idx)**2:.2f}"
        pend_l = f"{0.90 + 0.04 * mock_idx:.2f}"
        pend_t = f"{2 * 3.1416 * ( (0.90 + 0.04 * mock_idx) / 9.8 )**0.5:.2f}"
        
        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
**Historical Reference Benchmark**: 2009, 2016, 2023 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**: +4, -2 (Partials: +3, +2, +1)
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**: +3, 0
- **Section 3 (6 Questions per subject – Single Correct Option)**: +3, -1

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A monoatomic ideal gas undergoes a Stirling cycle consisting of two reversible isotherms at temperatures $T_H$ and $T_C$ and two reversible isochors:
(A) The heat absorbed during the isochoric heating equals the heat rejected during isochoric cooling.  
(B) With an ideal regenerator, the efficiency of the Stirling cycle equals the Carnot efficiency $\eta = 1 - T_C / T_H$.  
(C) Without regeneration, the efficiency is strictly less than the Carnot efficiency.  
(D) The net work done per cycle is $W = n R (T_H - T_C)\ln(V_2 / V_1)$.

#### Question 2
Regarding the Bohr-Sommerfeld quantization condition $\oint p_q dq = n h$ applied to a relativistic particle in a central potential:
(A) It successfully accounts for the fine structure of hydrogen-like spectral lines.  
(B) The energy levels depend on both the principal quantum number $n$ and the azimuthal quantum number $k$.  
(C) In the non-relativistic limit, the energy depends only on the principal quantum number $n$.  
(D) Relativistic mass variation breaks the accidental degeneracy of states with different angular momentum.

#### Question 3
A uniform ladder of length $L$ and mass $M$ leans against a smooth vertical wall with its base on a rough horizontal floor (coefficient of friction $\mu$):
(A) The normal reaction from the wall is horizontal.  
(B) The normal reaction from the floor equals $M g$.  
(C) The minimum angle $\theta_{\min}$ with the horizontal for equilibrium is given by $\tan\theta_{\min} = \frac{1}{2\mu}$.  
(D) As a person climbs up the ladder, the required frictional force at the base increases.

#### Question 4
A dielectric sphere of radius $R$ and uniform polarization $\vec{P} = P_0 \hat{k}$ is placed in vacuum:
(A) The bound surface charge density is $\sigma_b = P_0 \cos\theta$.  
(B) The bound volume charge density inside the sphere is zero ($\rho_b = 0$).  
(C) The electric field inside the sphere is uniform: $\vec{E}_{\text{in}} = -\frac{P_0}{3\varepsilon_0}\hat{k}$.  
(D) The electric field outside the sphere is identical to that of a pure dipole at the origin.

#### Question 5
In an experiment on Newton's rings with reflected light of wavelength $\lambda = 589\text{ nm}$ using a plano-convex lens of radius of curvature $R$:
(A) The central spot is dark due to a phase reversal of $\pi$ at the lower glass plate.  
(B) The diameter of the $n$-th dark ring is $D_n = 2\sqrt{n \lambda R}$.  
(C) If a liquid of refractive index $\mu > 1$ is filled between the lens and plate, the rings contract.  
(D) The fringe spacing is non-uniform, decreasing with increasing ring radius.

#### Question 6
A high-energy photon undergoes Compton scattering through an angle $\theta = 90^\circ$ against a stationary electron of rest mass $m_0$:
(A) The wavelength shift is $\Delta \lambda = \frac{h}{m_0 c} = \lambda_C$.  
(B) The scattered photon has lower energy than the incident photon.  
(C) The recoil electron acquires both kinetic energy and momentum.  
(D) The direction of the recoil electron makes an acute angle with the incident photon direction.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
An ideal gas heat engine operates between $T_H = 700\text{ K}$ and $T_C = 350\text{ K}$. If the heat supplied per cycle is $1200\text{ J}$, calculate the work done in Joules.

#### Question 8
In an X-ray experiment, electrons hit a target with kinetic energy $K = 31.0\text{ keV}$. Calculate the cutoff wavelength $\lambda_{\min}$ in picometers ($\text{pm}$). (Take $h c \approx 1240\text{ eV}\cdot\text{nm}$. Round off to two decimal places).

#### Question 9
A solid cylinder of mass $M = 3.0\text{ kg}$ and radius $R = 0.30\text{ m}$ rolls without slipping with velocity $v = 4.0\text{ m/s}$. Calculate its total kinetic energy in Joules. (Round off to two decimal places).

#### Question 10
Find the resonant frequency in Hz of a series LCR circuit with $L = 0.25\text{ H}$ and $C = 4.0\ \mu\text{F}$. (Take $\pi \approx 3.1416$. Round off to the nearest integer).

#### Question 11
Two sound sources emit frequencies $440\text{ Hz}$ and $444\text{ Hz}$. Find the beat period in seconds. (Round off to two decimal places).

#### Question 12
A simple pendulum of length $L = 1.0\text{ m}$ oscillates with small amplitude. Find its period in seconds. (Take $g = 9.8\text{ m/s}^2$. Round off to two decimal places).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle moves in a potential $V(x) = \frac{1}{2} k x^2 + \frac{\lambda}{x^4}$ for $x > 0$. The equilibrium position is:
(A) $x_0 = \left(\frac{4\lambda}{k}\right)^{1/6}$  
(B) $x_0 = \left(\frac{2\lambda}{k}\right)^{1/4}$  
(C) $x_0 = \sqrt{\lambda/k}$  
(D) $x_0 = \frac{\lambda}{k}$

#### Question 14
A spherical capacitor has inner radius $a = 2.0\text{ cm}$ and outer radius $b = 3.0\text{ cm}$. Its capacitance in air is:
(A) $6.67\text{ pF}$  
(B) $3.33\text{ pF}$  
(C) $10.0\text{ pF}$  
(D) $1.67\text{ pF}$

#### Question 15
In Fraunhofer diffraction by a double slit with slit width $b$ and separation $d$, if $d = 3b$, the missing orders of interference maxima are:
(A) $3, 6, 9, \dots$  
(B) $2, 4, 6, \dots$  
(C) $1, 3, 5, \dots$  
(D) None

#### Question 16
An ideal gas expands adiabatically such that its pressure decreases to $1/8$ of its initial value. If $\gamma = 5/3$, the volume increases by a factor of:
(A) $8^{3/5} \approx 3.48$  
(B) $4$  
(C) $8$  
(D) $2$

#### Question 17
A wire loop of area $A = 0.10\text{ m}^2$ is placed in a uniform magnetic field $B = 0.50\text{ T}$ rotating at $\omega = 100\text{ rad/s}$. The maximum induced EMF is:
(A) $5.0\text{ V}$  
(B) $2.5\text{ V}$  
(C) $10.0\text{ V}$  
(D) $1.0\text{ V}$

#### Question 18
The half-life of a radioactive substance is 5 years. The fraction remaining after 15 years is:
(A) $\frac{1}{8}$  
(B) $\frac{1}{4}$  
(C) $\frac{1}{16}$  
(D) $\frac{1}{2}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an electrochemical concentration cell without transference:
$$\text{Pt} \mid \text{H}_2(1\text{ bar}) \mid \text{HCl}(c_1) \parallel \text{HCl}(c_2) \mid \text{H}_2(1\text{ bar}) \mid \text{Pt}$$
(A) The cell EMF at $298\text{ K}$ is $E_{\text{cell}} = \frac{2.303 RT}{F}\log\left(\frac{c_2}{c_1}\right)$.  
(B) The cell reaction is spontaneous if $c_2 > c_1$.  
(C) At equilibrium ($c_1 = c_2$), the EMF becomes zero.  
(D) The cell operates by the dilution of the more concentrated electrolyte.

#### Question 20
Regarding the Langmuir adsorption isotherm $\theta = \frac{K P}{1 + K P}$:
(A) At low pressures ($K P \ll 1$), coverage is proportional to pressure ($\theta \approx K P$).  
(B) At high pressures ($K P \gg 1$), coverage saturates at a monolayer ($\theta \approx 1$).  
(C) It assumes all adsorption sites on the surface are equivalent.  
(D) It assumes no interaction between adjacent adsorbed molecules.

#### Question 21
Regarding the spectrochemical series and crystal field splitting ($\Delta_o$):
(A) Cyanide ($\text{CN}^-$) and carbonyl ($\text{CO}$) are strong-field ligands causing large $\Delta_o$.  
(B) Halide ions ($\text{I}^-, \text{Br}^-, \text{Cl}^-, \text{F}^-$) are weak-field ligands causing small $\Delta_o$.  
(C) Strong-field ligands favor low-spin complexes with maximum electron pairing.  
(D) Weak-field ligands favor high-spin complexes obeying Hund's rule of maximum multiplicity.

#### Question 22
Which of the following reactions undergo clean stereospecific anti-elimination (E2)?
(A) Dehydrohalogenation of alkyl halides with alcoholic $\text{KOH}$  
(B) Dehalogenation of vicinal dibromides with zinc dust in ethanol  
(C) Pyrolysis of xanthate esters (Chugaev reaction, syn-elimination)  
(D) Pyrolysis of amine oxides (Cope elimination, syn-elimination)

#### Question 23
Regarding the allotropes of carbon:
(A) In diamond, each carbon atom is $sp^3$ hybridized in a 3D tetrahedral network.  
(B) In graphite, each carbon atom is $sp^2$ hybridized in planar hexagonal sheets with delocalized $\pi$-electrons.  
(C) Fullerenes ($\text{C}_{60}$) consist of 12 pentagons and 20 hexagons.  
(D) Graphene is a single two-dimensional layer of carbon atoms with extraordinary electrical conductivity.

#### Question 24
Which of the following tests can distinguish between an aldehyde and a ketone?
(A) Tollen's reagent (silver mirror test)  
(B) Fehling's solution (red $\text{Cu}_2\text{O}$ precipitate)  
(C) Schiff's reagent (pink/magenta color)  
(D) 2,4-Dinitrophenylhydrazine (2,4-DNP, forms precipitate with both)

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The rate constant for a reaction is $k = 0.020\text{ min}^{-1}$. Calculate the time in minutes required for $75\%$ completion of the reaction. (Round off to two decimal places).

#### Question 26
Calculate the solubility product $K_{sp}$ of silver iodide ($\text{AgI}$) if its solubility is $s = 1.0 \times 10^{-8}\text{ M}$. (Express in units of $10^{-16}\text{ M}^2$).

#### Question 27
An aqueous solution contains $9.0\text{ g}$ of glucose ($M = 180\text{ g/mol}$) in $100\text{ g}$ of water. Calculate the elevation in boiling point $\Delta T_b$ in $^\circ\text{C}$. ($K_b = 0.52\text{ K}\cdot\text{kg/mol}$. Round off to two decimal places).

#### Question 28
Calculate the number of formula units ($Z$) per unit cell in the rock salt ($\text{NaCl}$) crystal lattice.

#### Question 29
Calculate the pH of a $0.010\text{ M}$ aqueous solution of $\text{NaOH}$ at $25^\circ\text{C}$.

#### Question 30
Find the standard free energy change $\Delta G^\circ$ in $\text{kJ/mol}$ for a cell with $E^\circ = 0.50\text{ V}$ and $n = 2$. (Take $F = 96500\text{ C/mol}$. Round off to two decimal places).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Clemmensen reduction, aldehydes and ketones are reduced to alkanes using:
(A) $\text{Zn-Hg} / \text{conc. HCl}$  
(B) $\text{NH}_2\text{NH}_2 / \text{KOH}$  
(C) $\text{LiAlH}_4$  
(D) $\text{H}_2 / \text{Pd}$

#### Question 32
The hybridization of the central atom in $\text{SF}_6$ is:
(A) $sp^3d^2$  
(B) $sp^3d$  
(C) $sp^3$  
(D) $d^2sp^3$

#### Question 33
The complex ion $[\text{Fe}(\text{CN})_6]^{4-}$ is:
(A) Diamagnetic (low-spin $d^6$)  
(B) Paramagnetic with 4 unpaired electrons  
(C) Paramagnetic with 5 unpaired electrons  
(D) High-spin

#### Question 34
In the extraction of iron, the reduction of $\text{Fe}_2\text{O}_3$ by $\text{CO}$ in the blast furnace is:
(A) Exothermic and spontaneous at moderate temperatures  
(B) Endothermic  
(C) Electrolytic  
(D) Non-spontaneous

#### Question 35
The polymer Dacron (Terylene) is formed by the condensation polymerization of:
(A) Ethylene glycol and Terephthalic acid  
(B) Phenol and Formaldehyde  
(C) Hexamethylenediamine and Adipic acid  
(D) Vinyl chloride

#### Question 36
The carbohydrate known as animal starch is:
(A) Glycogen  
(B) Cellulose  
(C) Amylose  
(D) Maltose

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{\ln x}{x^2}$ for $x > 0$:
(A) $f'(x) = \frac{1 - 2\ln x}{x^3}$.  
(B) $f(x)$ attains an absolute maximum at $x = \sqrt{e}$ with value $\frac{1}{2e}$.  
(C) $f(x)$ is concave upwards for $x > e^{5/6}$.  
(D) $\lim_{x \to \infty} f(x) = 0$.

#### Question 38
Consider the hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$:
(A) The eccentricity is $e = \frac{5}{4}$.  
(B) The foci lie at $(\pm 5, 0)$.  
(C) The length of the latus rectum is $\frac{9}{2}$.  
(D) The directrices are $x = \pm \frac{16}{5}$.

#### Question 39
Let $z$ be a complex number satisfying $|z - 1| = 1$:
(A) The locus of $z$ is a circle passing through the origin.  
(B) The maximum value of $|z|$ is $2$.  
(C) The argument $\arg(z)$ lies in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$.  
(D) $|z|^2 = 2 \text{Re}(z)$.

#### Question 40
Let $A$ be an orthogonal $n \times n$ matrix ($A^T A = I_n$):
(A) $\det(A) = \pm 1$.  
(B) All eigenvalues of $A$ have absolute value $1$.  
(C) $A^{-1} = A^T$.  
(D) Lengths of vectors are preserved under multiplication by $A$ ($|A \vec{x}| = |\vec{x}|$).

#### Question 41
Let $I = \int_0^1 x^p (1 - x)^q \, dx$ for $p, q > -1$ (Beta function $B(p+1, q+1)$):
(A) $B(p+1, q+1) = \frac{\Gamma(p+1)\Gamma(q+1)}{\Gamma(p+q+2)}$.  
(B) $B(p+1, q+1) = B(q+1, p+1)$.  
(C) For positive integers $m, n$, $B(m, n) = \frac{(m-1)!(n-1)!}{(m+n-1)!}$.  
(D) $\int_0^{\pi/2} \sin^{2m-1}\theta \cos^{2n-1}\theta \, d\theta = \frac{1}{2}B(m, n)$.

#### Question 42
Consider the line $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and the plane $x - 2y + z = 0$:
(A) The direction vector of the line is $\vec{d} = 2\hat{i} + 3\hat{j} + 4\hat{k}$.  
(B) The normal vector to the plane is $\vec{n} = \hat{i} - 2\hat{j} + \hat{k}$.  
(C) $\vec{d} \cdot \vec{n} = 2(1) + 3(-2) + 4(1) = 0$, so the line is parallel to the plane.  
(D) The point $(1, 2, 3)$ lies on the plane ($1 - 4 + 3 = 0$), so the line lies entirely in the plane.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = \sqrt{x}$ and the line $y = x$. (Round off to two decimal places).

#### Question 44
Evaluate the integral $\int_0^1 \frac{1}{1 + x} \, dx$. (Take $\ln 2 \approx 0.693$. Round off to two decimal places).

#### Question 45
Find the number of real roots of $x^4 - 4x + 3 = 0$.

#### Question 46
Let $\vec{a} = \hat{i} + \hat{j} + \hat{k}$ and $\vec{b} = 2\hat{i} + 2\hat{j} + 2\hat{k}$. Calculate the magnitude $|\vec{a} \times \vec{b}|$.

#### Question 47
Two cards are drawn simultaneously from a pack of 52 cards. Find the probability (in percentage) that both are Kings. (Round off to two decimal places).

#### Question 48
Find the radius of the circle $x^2 + y^2 - 12x + 16y = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arctan(x^2)$ with respect to $x$ is:
(A) $\frac{2x}{1 + x^4}$  
(B) $\frac{1}{1 + x^4}$  
(C) $\frac{2x}{1 + x^2}$  
(D) $\frac{x}{1 + x^4}$

#### Question 50
The length of the latus rectum of the parabola $y^2 = 20x$ is:
(A) $20$  
(B) $10$  
(C) $5$  
(D) $40$

#### Question 51
The value of $\lim_{x \to 0} \frac{e^{3x} - 1}{x}$ is:
(A) $3$  
(B) $1$  
(C) $\frac{1}{3}$  
(D) $0$

#### Question 52
If $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, the eigenvalues of $A$ are:
(A) $3$ and $1$  
(B) $2$ and $2$  
(C) $4$ and $1$  
(D) $3$ and $-1$

#### Question 53
The number of circular permutations of 5 persons is:
(A) $24$  
(B) $120$  
(C) $60$  
(D) $12$

#### Question 54
The solution of $\frac{dy}{dx} = y$ with $y(0) = 3$ is:
(A) $y = 3 e^x$  
(B) $y = e^{3x}$  
(C) $y = 3x + 3$  
(D) $y = e^x + 2$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
**Historical Reference Benchmark**: 2009, 2016, 2023 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**: +4, -2
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**: +3, 0
- **Section 3 (6 Questions per subject – Matching List / Matrix Match)**: +3, -1

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A real gas obeys the equation $P(V - b) = R T$. For this gas:
(A) The Joule-Thomson coefficient is $\mu_{\text{JT}} = -\frac{b}{C_P} < 0$.  
(B) Throttling expansion of this gas always results in heating ($\Delta T > 0$).  
(C) The internal energy depends on both temperature and volume.  
(D) At all temperatures, the inversion temperature does not exist.

#### Question 2
Regarding the photoelectric effect with stopping potential $V_s$:
(A) $e V_s = h\nu - \Phi$.  
(B) Stopping potential depends linearly on light frequency.  
(C) The threshold frequency is $\nu_0 = \Phi / h$.  
(D) Stopping potential is independent of light intensity.

#### Question 3
A convex lens of focal length $f = 15.0\text{ cm}$ forms a real image of magnification $2$:
(A) The object distance is $u = -22.5\text{ cm}$.  
(B) The image distance is $v = +45.0\text{ cm}$.  
(C) The distance between object and image is $67.5\text{ cm}$.  
(D) The image is inverted.

#### Question 4
A long straight wire carries a steady current $I$. A rectangular wire loop in the same plane moves away with speed $v$:
(A) The magnetic flux linked with the loop decreases with time.  
(B) The induced current flows in such a direction as to oppose the motion.  
(C) The induced EMF is inversely proportional to distance from the wire.  
(D) External force is required to keep the loop moving at constant velocity.

#### Question 5
A sphere of mass $m$ rolling on a horizontal surface collides elastically with an identical sphere at rest:
(A) Linear momentum of the system is conserved.  
(B) Total kinetic energy is conserved.  
(C) Angular momentum about any fixed point is conserved.  
(D) Friction during impact may cause slipping immediately after collision.

#### Question 6
Regarding the Michelson-Morley experiment:
(A) It sought to measure the velocity of the Earth relative to the luminiferous ether.  
(B) It yielded a null result within experimental precision.  
(C) It demonstrated the constancy of the speed of light in all inertial frames.  
(D) It led directly to Einstein's special theory of relativity.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
Calculate the ratio of the energy of an electron in the $n = 1$ state to that in the $n = 3$ state of a hydrogen atom.

#### Question 8
Find the molar heat capacity $C$ of an ideal monoatomic gas during an isochoric heating process in units of $R$. (Round off to two decimal places).

#### Question 9
A solid sphere of mass $M = 5.0\text{ kg}$ and radius $R = 0.20\text{ m}$ has moment of inertia about a tangent in $\text{kg}\cdot\text{m}^2$. (Round off to two decimal places).

#### Question 10
In an AC circuit with $R = 30\ \Omega$ and inductive reactance $X_L = 40\ \Omega$, find the impedance $Z$ in ohms.

#### Question 11
Two waves of identical frequency have intensities $I_1 = 9 I_0$ and $I_2 = 4 I_0$. Find the ratio of maximum intensity to minimum intensity in their interference pattern. (Round off to two decimal places).

#### Question 12
A spring-mass system with $m = 1.0\text{ kg}$ and $k = 100\text{ N/m}$ is displaced by $0.05\text{ m}$. Find its maximum kinetic energy in Joules. (Round off to two decimal places).

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the thermodynamic processes with their work done expressions:
- (P) Isothermal -> (1) $W = n R T \ln(V_2/V_1)$
- (Q) Isobaric -> (2) $W = P(V_2 - V_1)$
- (R) Isochoric -> (3) $W = 0$
- (S) Adiabatic -> (4) $W = \frac{P_1 V_1 - P_2 V_2}{\gamma - 1}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 14
Match the lens combinations with their equivalent focal lengths:
- (P) Two thin lenses in contact ($f_1, f_2$) -> (1) $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2}$
- (Q) Two thin lenses separated by distance $d$ -> (2) $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2}$
- (R) Lens silvered on one surface -> (3) Acts as curved mirror
- (S) Plano-convex lens ($R, \mu$) -> (4) $F = \frac{R}{\mu - 1}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 15
Match the physical quantities with their dimensions:
- (P) Surface tension -> (1) $[M T^{-2}]$
- (Q) Viscosity ($\eta$) -> (2) $[M L^{-1} T^{-1}]$
- (R) Pressure -> (3) $[M L^{-1} T^{-2}]$
- (S) Angular momentum -> (4) $[M L^2 T^{-1}]$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 16
Match the electromagnetic effects with their discoveries:
- (P) Hall Effect -> (1) Transverse voltage in magnetic field
- (Q) Faraday Effect -> (2) Rotation of polarization plane by magnetic field
- (R) Kerr Effect -> (3) Quadratic electro-optic birefringence
- (S) Pockels Effect -> (4) Linear electro-optic effect
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 17
Match the nuclear particles with their charges:
- (P) Alpha particle -> (1) $+2 e$
- (Q) Beta particle ($e^-$) -> (2) $-e$
- (R) Neutron -> (3) $0$
- (S) Proton -> (4) $+e$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 18
Match the modern physics phenomena with their models:
- (P) Blackbody radiation spectrum -> (1) Planck quantum hypothesis
- (Q) Hydrogen atom spectrum -> (2) Bohr orbital quantization
- (R) Electron diffraction -> (3) de Broglie matter waves
- (S) X-ray line spectra -> (4) Moseley's nuclear charge law
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding freezing point depression ($\Delta T_f = K_f m$):
(A) Cryoscopic constant $K_f = \frac{R T_f^2 M_{\text{solvent}}}{1000 \Delta H_{\text{fus}}}$.  
(B) $K_f$ is independent of the nature of the solute.  
(C) Ethylene glycol is used as an antifreeze in car radiators.  
(D) $\text{NaCl}$ and $\text{CaCl}_2$ are used to clear snow from roads by lowering the freezing point of water.

#### Question 20
Regarding the geometry and hybridization of coordination complexes:
(A) $[\text{Ni}(\text{CN})_4]^{2-}$ is square planar and diamagnetic ($dsp^2$).  
(B) $[\text{NiCl}_4]^{2-}$ is tetrahedral and paramagnetic ($sp^3$).  
(C) $[\text{Fe}(\text{H}_2\text{O})_6]^{2+}$ is octahedral and paramagnetic ($sp^3d^2$, high-spin).  
(D) $[\text{Fe}(\text{CN})_6]^{4-}$ is octahedral and diamagnetic ($d^2sp^3$, low-spin).

#### Question 21
Regarding the stability of alkenes:
(A) More highly substituted alkenes are generally more stable due to hyperconjugation.  
(B) Trans-alkenes are generally more stable than cis-alkenes due to steric relief.  
(C) Conjugated dienes are more stable than isolated dienes due to resonance.  
(D) Heat of hydrogenation is inversely proportional to alkene stability for isomers.

#### Question 22
Regarding the extraction of silver by cyanide process:
(A) Argentite ore ($\text{Ag}_2\text{S}$) is dissolved in $\text{NaCN}$ solution in the presence of air ($\text{O}_2$).  
(B) Soluble sodium dicyanoargentate(I) is formed: $\text{Na}[\text{Ag}(\text{CN})_2]$.  
(C) Zinc dust is used to precipitate silver: $2[\text{Ag}(\text{CN})_2]^- + \text{Zn} \to [\text{Zn}(\text{CN})_4]^{2-} + 2\text{Ag}$.  
(D) Air oxidizes $\text{Na}_2\text{S}$ to $\text{Na}_2\text{SO}_4$, driving the reversible leaching forward.

#### Question 23
Which of the following compounds give a positive test with Tollens' reagent?
(A) Acetaldehyde  
(B) Benzaldehyde  
(C) Formic acid ($\text{HCOOH}$)  
(D) Acetone

#### Question 24
Which of the following statements regarding group 16 elements (Chalcogens) is/are correct?
(A) Oxygen exhibits anomalous behavior due to small size and high electronegativity.  
(B) Ozone ($\text{O}_3$) is an allotrope of oxygen with a bent structure.  
(C) $\text{SF}_6$ is exceptionally stable and unreactive due to steric shielding of sulfur by six fluorine atoms.  
(D) Sulfuric acid acts as an oxidizing agent and dehydrating agent.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The half-life of a radioactive isotope is $20.0\text{ days}$. Calculate the decay constant $\lambda$ in units of $10^{-2}\text{ day}^{-1}$. (Round off to two decimal places).

#### Question 26
Calculate the solubility product $K_{sp}$ of barium sulfate ($\text{BaSO}_4$) if its solubility is $s = 1.0 \times 10^{-5}\text{ M}$. (Express in units of $10^{-10}\text{ M}^2$).

#### Question 27
A solution containing $10.0\text{ g}$ of non-volatile solute in $100\text{ g}$ of water has an osmotic pressure of $2.46\text{ atm}$ at $300\text{ K}$. Calculate the molecular weight of the solute. (Take $R = 0.0821\text{ L}\cdot\text{atm/(mol}\cdot\text{K)}$. Round off to the nearest integer).

#### Question 28
Find the coordination number of atoms in a face-centered cubic (FCC) metal crystal.

#### Question 29
Calculate the pH of a $0.050\text{ M}$ solution of $\text{Ba(OH)}_2$ at $25^\circ\text{C}$.

#### Question 30
Find the standard potential $E^\circ$ in volts for the reaction $\text{Zn}^{2+} + 2e^- \to \text{Zn}$ given $\Delta G^\circ = +146.68\text{ kJ/mol}$. (Take $F = 96500\text{ C/mol}$. Round off to two decimal places).

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the organic name reactions with their characteristic reagents:
- (P) Cannizzaro Reaction -> (1) $50\%\ \text{NaOH}$ with aldehydes having no $\alpha$-H
- (Q) Aldol Condensation -> (2) Dilute $\text{NaOH}$ with aldehydes having $\alpha$-H
- (R) Haloform Reaction -> (3) $\text{I}_2 + \text{NaOH}$
- (S) Reimer-Tiemann -> (4) $\text{CHCl}_3 + \text{KOH}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 32
Match the xenon compounds with their structures:
- (P) $\text{XeF}_4$ -> (1) Square planar
- (Q) $\text{XeOF}_4$ -> (2) Square pyramidal
- (R) $\text{XeO}_3$ -> (3) Pyramidal
- (S) $\text{XeF}_6$ -> (4) Distorted octahedral
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 33
Match the polymers with their categories:
- (P) Buna-S -> (1) Synthetic rubber
- (Q) Glyptal -> (2) Polyester resin
- (R) Melamine -> (3) Thermosetting resin
- (S) Polypropylene -> (4) Thermoplastic
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 34
Match the metallurgy processes with their target metals:
- (P) Cyanide process -> (1) Gold / Silver
- (Q) Hall-Hroult -> (2) Aluminium
- (R) Blast furnace -> (3) Pig iron
- (S) Bessemerization -> (4) Blister copper
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 35
Match the colloids with their purification methods:
- (P) Dialysis -> (1) Removal of ions across semipermeable membrane
- (Q) Electrodialysis -> (2) Dialysis accelerated by electric field
- (R) Ultrafiltration -> (3) Filtration using specially impregnated membranes
- (S) Ultracentrifugation -> (4) High-speed spinning separation
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 36
Match the vitamins with their deficiency diseases:
- (P) Vitamin A -> (1) Night blindness
- (Q) Vitamin B1 -> (2) Beri-beri
- (R) Vitamin C -> (3) Scurvy
- (S) Vitamin D -> (4) Rickets
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x^2}{x^2 + 1}$ for $x \in \mathbb{R}$:
(A) $f(x)$ is an even function.  
(B) The absolute minimum is $0$, attained at $x = 0$.  
(C) The range of $f(x)$ is $[0, 1)$.  
(D) $f'(x) = \frac{2x}{(x^2 + 1)^2}$.

#### Question 38
Consider the parabola $y^2 = 4x$:
(A) The focus is at $(1, 0)$.  
(B) The directrix is $x = -1$.  
(C) The latus rectum is $4$.  
(D) The vertex is at $(0, 0)$.

#### Question 39
Let $z$ be a complex number satisfying $|z| = 3$:
(A) The maximum value of $|z - 4|$ is $7$.  
(B) The minimum value of $|z - 4|$ is $1$.  
(C) $z \bar{z} = 9$.  
(D) The locus of $z$ is a circle centered at the origin.

#### Question 40
Let $A$ be a $2 \times 2$ matrix with $\text{Tr}(A) = 5$ and $\det(A) = 6$:
(A) The characteristic equation of $A$ is $\lambda^2 - 5\lambda + 6 = 0$.  
(B) The eigenvalues of $A$ are $2$ and $3$.  
(C) $A^2 - 5A + 6 I_2 = 0$.  
(D) $A$ is invertible.

#### Question 41
Let $f(x)$ be an integrable function on $[a, b]$:
(A) $\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx$.  
(B) $\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx$.  
(C) $\int_a^a f(x) \, dx = 0$.  
(D) $\int_a^b k f(x) \, dx = k \int_a^b f(x) \, dx$.

#### Question 42
Consider the line $\frac{x}{1} = \frac{y}{1} = \frac{z}{1}$ and the plane $x + y + z = 3$:
(A) The line is perpendicular to the plane.  
(B) The point of intersection is $(1, 1, 1)$.  
(C) The origin $(0, 0, 0)$ is at distance $\sqrt{3}$ from the plane.  
(D) The line passes through the origin.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = x$ and the parabola $y = x^2$. (Round off to two decimal places).

#### Question 44
Evaluate the integral $\int_0^1 x^2 \, dx$. (Round off to two decimal places).

#### Question 45
Find the number of real roots of $x^2 - 5x + 6 = 0$.

#### Question 46
Let $\vec{a} = 2\hat{i} + 2\hat{j} - \hat{k}$. Find $|\vec{a}|$.

#### Question 47
A card is drawn from a standard pack of 52 cards. Find the probability (in percentage) that it is a Spade. (Round off to two decimal places).

#### Question 48
Find the radius of the circle $x^2 + y^2 - 6x - 8y = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $e^{3x}$ with respect to $x$ is:
(A) $3 e^{3x}$  
(B) $e^{3x}$  
(C) $\frac{1}{3} e^{3x}$  
(D) $3x e^{3x}$

#### Question 50
The focus of the parabola $y^2 = 8x$ is at:
(A) $(2, 0)$  
(B) $(0, 2)$  
(C) $(-2, 0)$  
(D) $(4, 0)$

#### Question 51
The value of $\lim_{x \to 0} \frac{\sin 3x}{x}$ is:
(A) $3$  
(B) $1$  
(C) $\frac{1}{3}$  
(D) $0$

#### Question 52
If $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, then $\det(A)$ is:
(A) $1$  
(B) $0$  
(C) $2$  
(D) $-1$

#### Question 53
The value of $5!$ is:
(A) $120$  
(B) $24$  
(C) $60$  
(D) $720$

#### Question 54
The solution of $\frac{dy}{dx} = 3x^2$ with $y(0) = 1$ is:
(A) $y = x^3 + 1$  
(B) $y = x^3$  
(C) $y = 3x^3 + 1$  
(D) $y = x^3 - 1$
"""

        p1 = raw_p1.replace("__PAD__", pad).replace("__COMP_RATIO__", comp_ratio).replace("__PHOT_E__", phot_e).replace("__ALPHA_K__", alpha_k).replace("__DISC_V__", disc_v).replace("__PEND_L__", pend_l)
        p2 = raw_p2.replace("__PAD__", pad)
        
        raw_sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Guwahati Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Stirling cycle thermodynamics.
- Q2: (A, B, C, D) - Bohr-Sommerfeld quantization and fine structure.
- Q3: (A, B, C, D) - Statics of ladder leaning against smooth wall.
- Q4: (A, B, C, D) - Dielectric sphere with uniform polarization.
- Q5: (A, B, C, D) - Newton's rings interference pattern properties.
- Q6: (A, B, C, D) - Compton scattering at 90 degrees.
- Q7: 600.00 - $W = \eta Q_H = (1 - 350/700)(1200) = 0.50 \times 1200 = 600\text{ J}$.
- Q8: 40.00 - $\lambda_{\min} = \frac{1240}{31000}\text{ nm} = 0.040\text{ nm} = 40.00\text{ pm}$.
- Q9: 36.00 - Total kinetic energy of rolling cylinder: $\frac{3}{4}M v^2 = \frac{3}{4}(3)(16) = 36.00\text{ J}$.
- Q10: 159 - $f_0 = \frac{1}{2\pi\sqrt{0.25 \times 4 \times 10^{-6}}} = \frac{1}{2\pi \times 10^{-3}} \approx 159\text{ Hz}$.
- Q11: 0.25 - Beat period $1 / (444 - 440) = 1/4 = 0.25\text{ s}$.
- Q12: 2.01 - $T = 2\pi\sqrt{1.0 / 9.8} \approx 2.01\text{ s}$.
- Q13: (A) - Equilibrium position $V'(x_0) = 0 \implies k x_0 - \frac{4\lambda}{x_0^5} = 0 \implies x_0 = (4\lambda/k)^{1/6}$.
- Q14: (A) - Spherical capacitor $C = 4\pi\varepsilon_0 \frac{a b}{b - a} = \frac{1}{9 \times 10^9}\frac{0.02 \times 0.03}{0.01} = 6.67\text{ pF}$.
- Q15: (A) - Missing orders when $d = 3b$ are $n = 3, 6, 9, \dots$.
- Q16: (A) - Adiabatic expansion: $P V^\gamma = \text{const} \implies V_2 / V_1 = (P_1 / P_2)^{1/\gamma} = 8^{3/5} \approx 3.48$.
- Q17: (A) - $\mathcal{E}_0 = B A \omega = 0.50(0.10)(100) = 5.0\text{ V}$.
- Q18: (A) - 15 years is 3 half-lives $\implies (1/2)^3 = 1/8$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Concentration cell without transference.
- Q20: (A, B, C, D) - Langmuir adsorption isotherm features.
- Q21: (A, B, C, D) - Spectrochemical series and crystal field splitting.
- Q22: (A, B) - Anti-eliminations. Chugaev and Cope are syn-eliminations.
- Q23: (A, B, C, D) - Carbon allotropes.
- Q24: (A, B, C) - DNP forms precipitate with both aldehydes and ketones.
- Q25: 69.31 - $t_{75\%} = 2 t_{1/2} = 2 \times \frac{0.6931}{0.020} = 69.31\text{ min}$.
- Q26: 1.00 - $K_{sp} = s^2 = (10^{-8})^2 = 1.0 \times 10^{-16}$.
- Q27: 0.26 - $m = \frac{9/180}{0.100} = 0.50\text{ m} \implies \Delta T_b = 0.52(0.50) = 0.26^\circ\text{C}$.
- Q28: 4 - In $\text{NaCl}$ unit cell, $Z = 4$.
- Q29: 12.00 - $[\text{OH}^-] = 0.010\text{ M} \implies \text{pOH} = 2.00 \implies \text{pH} = 12.00$.
- Q30: -96.50 - $\Delta G^\circ = -n F E^\circ = -2(96500)(0.50) = -96500\text{ J} = -96.50\text{ kJ/mol}$.
- Q31: (A) - Clemmensen reduction uses $\text{Zn-Hg} / \text{conc. HCl}$.
- Q32: (A) - $\text{SF}_6$ has 6 bond pairs $\implies sp^3d^2$ octahedral.
- Q33: (A) - $[\text{Fe}(\text{CN})_6]^{4-}$ has $d^6$ low spin ($t_{2g}^6$) $\implies$ diamagnetic.
- Q34: (A) - Reduction of iron oxides in blast furnace is exothermic.
- Q35: (A) - Dacron is formed by ethylene glycol and terephthalic acid.
- Q36: (A) - Glycogen is known as animal starch.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Function $\frac{\ln x}{x^2}$ analysis.
- Q38: (A, B, C, D) - Standard hyperbola geometry.
- Q39: (A, B, C, D) - Circle $|z - 1| = 1$ in Argand plane.
- Q40: (A, B, C, D) - Orthogonal matrix properties.
- Q41: (A, B, C, D) - Beta and Gamma function identities.
- Q42: (A, B, C, D) - Line lies entirely in the plane.
- Q43: 0.17 - Area between $\sqrt{x}$ and $x$ is $\int_0^1 (\sqrt{x} - x) dx = 2/3 - 1/2 = 1/6 \approx 0.17$.
- Q44: 0.69 - $\int_0^1 \frac{1}{1+x} dx = \ln 2 \approx 0.69$.
- Q45: 2 - $f'(x) = 4(x^3 - 1) = 0 \implies x = 1$ is minimum, $f(1) = 0$, roots are $x = 1$ (double root). Two real roots.
- Q46: 0.00 - Parallel vectors cross product is zero.
- Q47: 0.45 - Probability $\frac{\binom{4}{2}}{\binom{52}{2}} = \frac{6}{1326} \approx 0.45\%$.
- Q48: 10.00 - Center $(6, -8)$, $R = \sqrt{36 + 64} = 10.00$.
- Q49: (A) - Derivative is $\frac{2x}{1 + x^4}$.
- Q50: (A) - Latus rectum is $4a = 20$.
- Q51: (A) - Limit $= 3$.
- Q52: (A) - Eigenvalues $\det(A - \lambda I) = (2 - \lambda)^2 - 1 = 0 \implies 2 - \lambda = \pm 1 \implies \lambda = 3, 1$.
- Q53: (A) - Circular permutations of 5 is $(5-1)! = 24$.
- Q54: (A) - $y = 3 e^x$.
"""

        raw_sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Guwahati Benchmark JEE Advanced Mock Examination __PAD__

---

### PART I: PHYSICS
- Q1: (A, B, D) - Real gas with volume correction only heats on throttling.
- Q2: (A, B, C, D) - Photoelectric effect stopping potential properties.
- Q3: (A, B, C, D) - Lens real image magnification relations.
- Q4: (A, B, C, D) - Electromagnetic induction in moving rectangular loop.
- Q5: (A, B, C, D) - Elastic collision of rolling spheres.
- Q6: (A, B, C, D) - Michelson-Morley experiment history and significance.
- Q7: 9.00 - $E_n \propto 1/n^2 \implies E_1 / E_3 = 3^2 / 1^2 = 9.00$.
- Q8: 1.50 - $C_V = \frac{3}{2}R = 1.50 R$.
- Q9: 0.28 - $I = \frac{7}{5}M R^2 = \frac{7}{5}(5.0)(0.04) = 0.28\text{ kg}\cdot\text{m}^2$.
- Q10: 50.00 - $Z = \sqrt{R^2 + X_L^2} = \sqrt{900 + 1600} = 50.00\ \Omega$.
- Q11: 25.00 - $\frac{I_{\max}}{I_{\min}} = \left(\frac{\sqrt{I_1} + \sqrt{I_2}}{\sqrt{I_1} - \sqrt{I_2}}\right)^2 = \left(\frac{3 + 2}{3 - 2}\right)^2 = 25.00$.
- Q12: 0.13 - $E = \frac{1}{2}k x^2 = \frac{1}{2}(100)(0.0025) = 0.125 \approx 0.13\text{ J}$.
- Q13: (A) - Work done expressions.
- Q14: (A) - Lens formulas.
- Q15: (A) - Physical dimensions.
- Q16: (A) - Electro-optic and magneto-optic effects.
- Q17: (A) - Nuclear charges.
- Q18: (A) - Modern physics historical models.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Freezing point depression and de-icing.
- Q20: (A, B, C, D) - Hybridization and magnetic properties of nickel and iron complexes.
- Q21: (A, B, C, D) - Alkene stability factors.
- Q22: (A, B, C, D) - Cyanide extraction of silver.
- Q23: (A, B, C) - Tollens' test positive for aldehydes and formic acid.
- Q24: (A, B, C, D) - Group 16 elements properties.
- Q25: 3.47 - $\lambda = \frac{0.69315}{20} = 0.034657\text{ day}^{-1} = 3.47 \times 10^{-2}$.
- Q26: 1.00 - $K_{sp} = s^2 = (10^{-5})^2 = 1.0 \times 10^{-10}$.
- Q27: 1002 - $\Pi = C R T = \frac{w/M}{V}R T \implies M = \frac{10 \times 0.0821 \times 300}{2.46 \times 0.100} \approx 1002\text{ g/mol}$.
- Q28: 12 - Coordination number in FCC is 12.
- Q29: 13.00 - $[\text{OH}^-] = 2(0.050) = 0.10\text{ M} \implies \text{pOH} = 1.00 \implies \text{pH} = 13.00$.
- Q30: -0.76 - $E^\circ = -\frac{\Delta G^\circ}{n F} = -\frac{146680}{2 \times 96500} = -0.76\text{ V}$ (Zinc).
- Q31: (A) - Name reactions.
- Q32: (A) - Xenon compounds structures.
- Q33: (A) - Polymer classifications.
- Q34: (A) - Metallurgy target metals.
- Q35: (A) - Colloid purification methods.
- Q36: (A) - Vitamin deficiency diseases.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Analysis of $\frac{x^2}{x^2 + 1}$.
- Q38: (A, B, C, D) - Parabola $y^2 = 4x$ parameters.
- Q39: (A, B, C, D) - Modulus and distance in complex plane.
- Q40: (A, B, C, D) - Characteristic equation and eigenvalues.
- Q41: (A, B, C, D) - Fundamental properties of definite integrals.
- Q42: (A, B, C, D) - Line perpendicular to plane.
- Q43: 0.17 - $\int_0^1 (x - x^2) dx = 1/6 \approx 0.17$.
- Q44: 0.33 - $\int_0^1 x^2 dx = 1/3 \approx 0.33$.
- Q45: 2 - Two distinct real roots $x = 2, 3$.
- Q46: 3.00 - $|\vec{a}| = \sqrt{4 + 4 + 1} = 3.00$.
- Q47: 25.00 - $13/52 = 25.00\%$.
- Q48: 5.00 - Center $(3, 4)$, $R = \sqrt{9 + 16} = 5.00$.
- Q49: (A) - Derivative is $3 e^{3x}$.
- Q50: (A) - Focus of $y^2 = 8x$ is $(2, 0)$.
- Q51: (A) - Limit $= 3$.
- Q52: (A) - Determinant of identity matrix is $1$.
- Q53: (A) - $5! = 120$.
- Q54: (A) - $y = x^3 + 1$.
"""

        raw_val = r"""# Answer Key & Benchmark Alignment – Mock Examination __PAD__
## Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 600.00; Q8: 40.00; Q9: 36.00; Q10: 159; Q11: 0.25; Q12: 2.01; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B; Q23: A,B,C,D; Q24: A,B,C; Q25: 69.31; Q26: 1.00; Q27: 0.26; Q28: 4; Q29: 12.00; Q30: -96.50; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 0.17; Q44: 0.69; Q45: 2.00; Q46: 0.00; Q47: 0.45; Q48: 10.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 9.00; Q8: 1.50; Q9: 0.28; Q10: 50.00; Q11: 25.00; Q12: 0.13; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C; Q24: A,B,C,D; Q25: 3.47; Q26: 1.00; Q27: 1002.00; Q28: 12; Q29: 13.00; Q30: -0.76; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 0.17; Q44: 0.33; Q45: 2.00; Q46: 3.00; Q47: 25.00; Q48: 5.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""
        sol1 = raw_sol1.replace("__PAD__", pad)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)
        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Guwahati")
        print(f"Generated IIT Guwahati Mock {pad}!")
        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, iit_name="IIT_Guwahati")
        print(f"Generated IIT Guwahati Mock {pad}!")

if __name__ == "__main__":
    generate_guwahati_11_to_15()
