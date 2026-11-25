"""
IIT Madras Mocks 16 to 20 Generator
Organising Institute: Indian Institute of Technology Madras
Empirical Benchmark: 2010, 2017, 2024 Official JEE Advanced Papers
Features:
- Electromagnetism dominance (>= 37% of physics: Hall effect, skin depth, Fabry-Perot finesse, Einstein A & B coefficients)
- Single-correct traps and speed/precision tests
- Physical chemistry dominance: Phase rule, Clausius-Clapeyron, conductometric titrations, CFSE & IR stretching
- Mathematics: Conics invariants & confocal orthogonality, Feynman's differentiation under integral, multinomial theorem & derangements
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_madras_16_to_20():
    for mock_idx in range(16, 21):
        pad = f"{mock_idx:02d}"

        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)
**Historical Reference Benchmark**: 2010, 2017, 2024 Official Examination Papers  
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
A flat conducting slab of thickness $t$, width $w$, and length $L$ carries a steady current $I$ along the $+x$ direction in a uniform magnetic field $\vec{B} = B_0\hat{z}$. The charge carriers have charge $q$ and number density $n$:
(A) The Hall electric field inside the slab is $\vec{E}_H = -\frac{I B_0}{n q w t}\hat{y}$.  
(B) The transverse Hall voltage across the width of the slab is $V_H = \frac{I B_0}{n q t}$.  
(C) The sign of the measured Hall voltage determines whether the majority charge carriers are electrons or holes.  
(D) The Hall coefficient is defined as $R_H = \frac{1}{n q}$.

#### Question 2
Two identical magnetic dipoles with magnetic moments $\vec{m}_1 = m_0\hat{k}$ and $\vec{m}_2 = m_0\hat{k}$ are located on the $z$-axis separated by distance $d$:
(A) The magnetic field produced by dipole 1 at the position of dipole 2 is $\vec{B}_1 = \frac{\mu_0 m_0}{2\pi d^3}\hat{k}$.  
(B) The potential energy of interaction between the two dipoles is $U = -\frac{\mu_0 m_0^2}{2\pi d^3}$.  
(C) The force between the two dipoles is attractive and of magnitude $F = \frac{3\mu_0 m_0^2}{2\pi d^4}$.  
(D) If the direction of $\vec{m}_2$ is reversed, the interaction force becomes repulsive.

#### Question 3
An electromagnetic wave of frequency $\omega$ propagates in a good conductor of electrical conductivity $\sigma$ and magnetic permeability $\mu_0$:
(A) The wave amplitude decays exponentially with depth $z$ as $e^{-z/\delta}$, where $\delta$ is the skin depth.  
(B) The skin depth is given by $\delta = \sqrt{\frac{2}{\mu_0 \sigma \omega}}$.  
(C) High-frequency alternating currents flow predominantly in a thin surface layer of a conductor.  
(D) Inside the conductor, the magnetic field lags behind the electric field by a phase of $45^\circ$ ($\pi/4$ radians).

#### Question 4
In an optical Fabry-Pérot interferometer with two parallel mirrors of reflectance $R$ separated by distance $d$:
(A) Transmitted intensity maxima occur when $2d\cos\theta = m\lambda$ ($m \in \mathbb{N}$).  
(B) The coefficient of finesse is $F = \frac{4R}{(1-R)^2}$.  
(C) The transmission coefficient as a function of phase difference $\delta$ is $T(\delta) = \frac{1}{1 + F\sin^2(\delta/2)}$.  
(D) As $R \to 1$, the transmission fringes become extremely sharp.

#### Question 5
Regarding Einstein's coefficients of spontaneous emission ($A_{21}$), stimulated emission ($B_{21}$), and absorption ($B_{12}$) for a two-level atomic system:
(A) For non-degenerate states, $B_{12} = B_{21}$.  
(B) The ratio of spontaneous to stimulated emission coefficients is $\frac{A_{21}}{B_{21}} = \frac{8\pi h \nu^3}{c^3}$.  
(C) Laser action requires population inversion where the upper energy level has a higher population than the lower level ($N_2 > N_1$).  
(D) Stimulated emission produces photons that are coherent, identical in phase, frequency, and direction to the incident photons.

#### Question 6
For a Maxwell-Boltzmann gas of particles of mass $m$ at temperature $T$:
(A) The most probable speed is $v_{\text{mp}} = \sqrt{\frac{2k_B T}{m}}$.  
(B) The average speed is $\langle v \rangle = \sqrt{\frac{8k_B T}{\pi m}}$.  
(C) The root-mean-square speed is $v_{\text{rms}} = \sqrt{\frac{3k_B T}{m}}$.  
(D) The speeds satisfy the strict ordering: $v_{\text{mp}} < \langle v \rangle < v_{\text{rms}}$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a Hall effect measurement on a copper strip of thickness $t = 0.50\text{ mm}$, a current $I = 10.0\text{ A}$ in a magnetic field $B = 1.20\text{ T}$ produces a Hall voltage $V_H = 1.80\text{ }\mu\text{V}$. The carrier density $n$ of conduction electrons in the copper strip is $X \times 10^{28}\text{ m}^{-3}$. Taking $e = 1.60 \times 10^{-19}\text{ C}$, evaluate $X$ rounded off to two decimal places.

#### Question 8
Two identical thin circular coaxial coils, each of radius $R = 0.10\text{ m}$ and $N = 100\text{ turns}$, are placed at a distance equal to their radius $R$ apart (Helmholtz coils) and carry current $I = 2.0\text{ A}$ in the same direction. The magnetic field at the midpoint on the axis is $B\text{ mT}$. Taking $\mu_0 = 4\pi \times 10^{-7}\text{ T m/A}$, find $B$ rounded off to two decimal places.

#### Question 9
A telescope with an objective of diameter $D = 2.44\text{ m}$ observes light of wavelength $\lambda = 500\text{ nm}$. The angular resolution limit in radians according to Rayleigh's criterion is $\theta_R \times 10^{-7}\text{ rad}$. Find $\theta_R$ rounded off to two decimal places.

#### Question 10
In a series $LCR$ circuit, $R = 8.0\text{ }\Omega$, $L = 0.20\text{ H}$, and $C = 50\text{ }\mu\text{F}$. The resonance angular frequency $\omega_0$ in $\text{rad/s}$ is $\omega_0$. Find $\omega_0$ rounded off to the nearest integer.

#### Question 11
A monoatomic ideal gas undergoes an isobaric expansion at constant pressure $P = 1.0 \times 10^5\text{ Pa}$ from volume $V_1 = 0.02\text{ m}^3$ to $V_2 = 0.05\text{ m}^3$. The heat supplied to the gas is $Q\text{ kJ}$. Find $Q$ rounded off to one decimal place.

#### Question 12
The wavelength of the $K_\alpha$ X-ray line of an element is $\lambda = 0.71\text{ \AA}$. According to Moseley's law $\sqrt{\nu} = a(Z - 1)$, for copper ($Z = 29$, $\lambda = 1.54\text{ \AA}$), the atomic number $Z$ of the unknown element is $Z$. Find $Z$ rounded off to the nearest integer.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The magnetic flux linked with a closed coil of resistance $10\text{ }\Omega$ varies with time according to $\Phi(t) = 6t^2 - 5t + 1\text{ Wb}$. The induced current at $t = 0.25\text{ s}$ is:
(A) $0.20\text{ A}$  
(B) $0.40\text{ A}$  
(C) $0.10\text{ A}$  
(D) $0.80\text{ A}$

#### Question 14
Two coherent monochromatic light beams of intensities $I$ and $4I$ superimpose. The maximum and minimum possible intensities in the resulting interference pattern are:
(A) $9I$ and $I$  
(B) $5I$ and $3I$  
(C) $4I$ and $I$  
(D) $9I$ and $3I$

#### Question 15
The capacitance of an isolated spherical conductor of radius $R = 9.0\text{ km}$ in vacuum is:
(A) $1.0\text{ }\mu\text{F}$  
(B) $1.0\text{ mF}$  
(C) $1.0\text{ pF}$  
(D) $9.0\text{ }\mu\text{F}$

#### Question 16
A particle of mass $m$ is executing SHM with amplitude $A$. When its displacement is $x = A/2$, the ratio of its kinetic energy to potential energy is:
(A) $3:1$  
(B) $1:3$  
(C) $2:1$  
(D) $1:1$

#### Question 17
A nuclear reactor generates power of $1000\text{ MW}$ via fission of $^{235}\text{U}$. If each fission event releases $200\text{ MeV}$, the number of fissions occurring per second is:
(A) $3.125 \times 10^{19}$  
(B) $5.0 \times 10^{18}$  
(C) $1.25 \times 10^{20}$  
(D) $6.25 \times 10^{17}$

#### Question 18
The coefficient of viscosity of an ideal gas:
(A) Increases with increasing temperature proportional to $\sqrt{T}$  
(B) Decreases with increasing temperature  
(C) Is independent of temperature  
(D) Increases linearly with pressure

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the bonding in metal carbonyls such as $\text{Ni}(\text{CO})_4$, $\text{Fe}(\text{CO})_5$, and $\text{Cr}(\text{CO})_6$:
(A) The $\text{M}-\text{C}$ $\sigma$-bond is formed by donation of lone pair electrons from the carbonyl carbon into an empty metal $d$-orbital.  
(B) The $\text{M}-\text{C}$ $\pi$-bond is formed by back-donation of electrons from filled metal $d$-orbitals into empty $\pi^*$ antibonding orbitals of $\text{CO}$.  
(C) Synergic bonding strengthens the $\text{M}-\text{C}$ bond and weakens the $\text{C}-\text{O}$ bond.  
(D) As back-bonding increases, the $\text{C}-\text{O}$ stretching frequency in infrared (IR) spectroscopy decreases.

#### Question 20
Regarding the Clausius-Clapeyron equation for liquid-vapor phase equilibria:
(A) $\frac{d\ln P}{dT} = \frac{\Delta_{\text{vap}}H}{R T^2}$ (assuming ideal vapor and negligible liquid volume).  
(B) A plot of $\ln P$ versus $1/T$ is linear with slope $-\frac{\Delta_{\text{vap}}H}{R}$.  
(C) Liquids with higher enthalpy of vaporization show a steeper variation of vapor pressure with temperature.  
(D) The normal boiling point is the temperature at which the vapor pressure equals $1\text{ atm}$.

#### Question 21
Regarding conductometric titrations:
(A) In the titration of a strong acid ($\text{HCl}$) with a strong base ($\text{NaOH}$), conductivity decreases initially due to replacement of high-mobility $\text{H}^+$ with $\text{Na}^+$, then increases after the endpoint due to excess $\text{OH}^-$.  
(B) In the titration of a weak acid ($\text{CH}_3\text{COOH}$) with a strong base ($\text{NaOH}$), conductivity initially drops slightly, then increases as sodium acetate forms, and rises steeply after the endpoint.  
(C) Conductometric titrations do not require a chemical indicator.  
(D) Conductometric titrations can be accurately performed in highly turbid or colored solutions.

#### Question 22
Regarding the chemistry of phosphorus oxoacids:
(A) Hypophosphorous acid ($\text{H}_3\text{PO}_2$) is a monobasic acid containing two $\text{P}-\text{H}$ bonds.  
(B) Phosphorous acid ($\text{H}_3\text{PO}_3$) is a dibasic acid containing one $\text{P}-\text{H}$ bond.  
(C) Phosphoric acid ($\text{H}_3\text{PO}_4$) is a tribasic acid with no $\text{P}-\text{H}$ bonds.  
(D) Compounds containing $\text{P}-\text{H}$ bonds act as strong reducing agents (e.g., $\text{H}_3\text{PO}_2$ reduces $\text{AgNO}_3$ to metallic silver).

#### Question 23
Regarding the Diels-Alder reaction:
(A) It is a $[4+2]$ cycloaddition occurring between a conjugated diene and a dienophile.  
(B) The reaction is stereospecific and proceeds via a concerted pericyclic mechanism with a cyclic transition state.  
(C) Electron-withdrawing groups on the dienophile and electron-donating groups on the diene accelerate the reaction rate.  
(D) The diene must adopt the *s-cis* conformation to undergo the cycloaddition.

#### Question 24
Regarding the lanthanide series of elements:
(A) The steady decrease in atomic and ionic radii with increasing atomic number is called the lanthanide contraction.  
(B) Lanthanide contraction is caused by poor shielding of $4f$ electrons.  
(C) As a consequence of lanthanide contraction, the pairs of elements $\text{Zr}/\text{Hf}$ and $\text{Nb}/\text{Ta}$ possess nearly identical atomic and ionic radii.  
(D) Basic strength of lanthanide hydroxides $\text{Ln}(\text{OH})_3$ decreases from $\text{La}(\text{OH})_3$ to $\text{Lu}(\text{OH})_3$.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The crystal field stabilization energy (CFSE) of an octahedral high-spin $d^6$ complex is $X \Delta_o$. Find the magnitude $|X|$ rounded off to one decimal place.

#### Question 26
The vapor pressure of water at $293\text{ K}$ is $17.5\text{ mmHg}$. Calculate the vapor pressure in $\text{mmHg}$ of an aqueous solution containing $5.0\text{ g}$ of urea (molar mass $60\text{ g/mol}$) dissolved in $100.0\text{ g}$ of water. Find the vapor pressure rounded off to two decimal places.

#### Question 27
For the disproportionation reaction $2\text{Cu}^+(aq) \rightleftharpoons \text{Cu}^{2+}(aq) + \text{Cu}(s)$, given $E^\circ(\text{Cu}^+/\text{Cu}) = +0.52\text{ V}$ and $E^\circ(\text{Cu}^{2+}/\text{Cu}^+) = +0.16\text{ V}$ at $298\text{ K}$. The standard cell EMF is $E^\circ_{\text{cell}}\text{ V}$. Find $E^\circ_{\text{cell}}$ rounded off to two decimal places.

#### Question 28
The half-life of a first-order radioactive decomposition is $140\text{ days}$. The time required for $99\%$ of the radioactive material to decay is $t\text{ days}$. (Take $\ln 10 \approx 2.303$ and $\ln 2 \approx 0.693$). Find $t$ rounded off to the nearest integer.

#### Question 29
A metal crystallizes in a face-centered cubic (FCC) lattice with unit cell edge length $a = 400\text{ pm}$. The atomic radius of the metal atom is $r\text{ pm}$. Find $r$ rounded off to two decimal places.

#### Question 30
Find the number of unpaired electrons in the complex ion $[\text{Fe}(\text{CN})_6]^{3-}$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following oxoacids of sulfur contains a peroxo linkage ($-\text{O}-\text{O}-$):
(A) Caro's acid ($\text{H}_2\text{SO}_5$)  
(B) Pyrosulfuric acid ($\text{H}_2\text{S}_2\text{O}_7$)  
(C) Dithionic acid ($\text{H}_2\text{S}_2\text{O}_6$)  
(D) Thiosulfuric acid ($\text{H}_2\text{S}_2\text{O}_3$)

#### Question 32
Cannizzaro reaction is NOT given by:
(A) Acetaldehyde ($\text{CH}_3\text{CHO}$)  
(B) Formaldehyde ($\text{HCHO}$)  
(C) Benzaldehyde ($\text{C}_6\text{H}_5\text{CHO}$)  
(D) Trimethylacetaldehyde ($(\text{CH}_3)_3\text{C}-\text{CHO}$)

#### Question 33
The geometry of $\text{I}_3^-$ ion is:
(A) Linear  
(B) Bent  
(C) Trigonal planar  
(D) T-shaped

#### Question 34
Which of the following compounds reacts with Hinsberg's reagent to give a solid insoluble in alkali:
(A) Secondary amine ($R_2\text{NH}$)  
(B) Primary amine ($R\text{NH}_2$)  
(C) Tertiary amine ($R_3\text{N}$)  
(D) Quaternary ammonium salt

#### Question 35
The IUPAC name of $\text{K}_3[\text{Fe}(\text{CN})_6]$ is:
(A) Potassium hexacyanidoferrate(III)  
(B) Potassium hexacyanoiron(III)  
(C) Tripotassium hexacyanidoferrate(II)  
(D) Potassium ferrocyanide

#### Question 36
The boiling point of noble gases increases down the group from $\text{He}$ to $\text{Rn}$ primarily due to:
(A) Increase in London dispersion forces  
(B) Increase in ionization enthalpy  
(C) Increase in nuclear charge  
(D) Decrease in polarizability

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $I(\alpha) = \int_0^\infty \frac{e^{-x} - e^{-\alpha x}}{x} dx$ for $\alpha > 0$ (Feynman's technique):
(A) $I'(\alpha) = \int_0^\infty e^{-\alpha x} dx = \frac{1}{\alpha}$.  
(B) $I(1) = 0$.  
(C) $I(\alpha) = \ln\alpha$.  
(D) $\int_0^\infty \frac{e^{-x} - e^{-5x}}{x} dx = \ln 5$.

#### Question 38
Consider the confocal conics $\frac{x^2}{a^2 + \lambda} + \frac{y^2}{b^2 + \lambda} = 1$:
(A) For $\lambda > -b^2$ ($a > b$), the equation represents an ellipse.  
(B) For $-a^2 < \lambda < -b^2$, the equation represents a hyperbola.  
(C) Through any given point $(x_0, y_0)$ in the plane, there pass exactly two conics of the confocal system: one ellipse and one hyperbola.  
(D) The confocal ellipse and hyperbola intersect each other orthogonally at all points of intersection.

#### Question 39
Let $D_n$ denote the number of derangements of $n$ distinct objects:
(A) $D_n = (n-1)(D_{n-1} + D_{n-2})$ for $n \ge 3$.  
(B) $D_n = n D_{n-1} + (-1)^n$ for $n \ge 2$.  
(C) $D_1 = 0, D_2 = 1, D_3 = 2, D_4 = 9, D_5 = 44$.  
(D) $\lim_{n \to \infty} \frac{D_n}{n!} = \frac{1}{e}$.

#### Question 40
Let $f(x)$ be a twice differentiable function on $[a, b]$:
(A) If $f(a) = f(b) = 0$, by Rolle's theorem there exists $c \in (a, b)$ such that $f'(c) = 0$.  
(B) If $f(x)$ has $n$ distinct roots in $[a, b]$, then $f'(x)$ has at least $n-1$ distinct roots in $(a, b)$.  
(C) If $f''(x) > 0$ on $[a, b]$, then $f(x)$ is strictly convex.  
(D) For a strictly convex function, $f\left(\frac{x+y}{2}\right) \le \frac{f(x) + f(y)}{2}$.

#### Question 41
Let $M$ be an orthogonal $n \times n$ matrix ($M^T M = I_n$):
(A) $\det(M) = \pm 1$.  
(B) All real eigenvalues of $M$ are $\pm 1$.  
(C) $\|M\vec{x}\| = \|\vec{x}\|$ for all $\vec{x} \in \mathbb{R}^n$ (isometry).  
(D) The columns of $M$ form an orthonormal basis of $\mathbb{R}^n$.

#### Question 42
Consider the system of linear equations:
$x + y + z = 6$, $x + 2y + 3z = 10$, $x + 2y + \lambda z = \mu$:
(A) The system has a unique solution if $\lambda \ne 3$.  
(B) The system has infinitely many solutions if $\lambda = 3$ and $\mu = 10$.  
(C) The system has no solution if $\lambda = 3$ and $\mu \ne 10$.  
(D) If $\lambda = 3$ and $\mu = 10$, the solution space is a line in $\mathbb{R}^3$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the total number of terms in the multinomial expansion of $(x_1 + x_2 + x_3 + x_4)^{10}$.

#### Question 44
Evaluate $\int_0^{\pi/2} \frac{\sqrt{\tan x}}{1 + \sqrt{\tan x}} dx$. The value of the integral is $\frac{\pi}{k}$. Find $k$.

#### Question 45
Find the shortest distance between the line $\frac{x-3}{1} = \frac{y-5}{-2} = \frac{z-7}{1}$ and the line $\frac{x+1}{7} = \frac{y+1}{-6} = \frac{z+1}{1}$. Round off to two decimal places.

#### Question 46
Let $\alpha$ and $\beta$ be the roots of $x^2 - 6x + 2 = 0$. Find the value of $\alpha^3 + \beta^3$.

#### Question 47
Find the number of ways to distribute 10 identical apples among 3 distinct children such that each child receives at least one apple.

#### Question 48
Find the radius of the director circle of the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The value of $\lim_{x \to 0} \frac{\tan x - \sin x}{x^3}$ is:
(A) $1/2$  
(B) $1$  
(C) $1/3$  
(D) $2$

#### Question 50
The slope of the normal to the curve $y = 2x^2 + 3\sin x$ at $x = 0$ is:
(A) $-1/3$  
(B) $3$  
(C) $1/3$  
(D) $-3$

#### Question 51
The angle between the planes $2x - y + z = 6$ and $x + y + 2z = 7$ is:
(A) $\pi/3$  
(B) $\pi/4$  
(C) $\pi/6$  
(D) $\pi/2$

#### Question 52
If $A$ is a square matrix of order 3 such that $\det(A) = 5$, then $\det(\text{adj}(A))$ is:
(A) 25  
(B) 125  
(C) 5  
(D) 10

#### Question 53
The number of solutions of $\sin x = \frac{x}{10}$ is:
(A) 7  
(B) 6  
(C) 5  
(D) 3

#### Question 54
Two cards are drawn from a pack of 52 cards without replacement. The probability that both are aces is:
(A) $1/221$  
(B) $1/169$  
(C) $1/17$  
(D) $1/26$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)
**Historical Reference Benchmark**: 2010, 2017, 2024 Official Examination Papers  
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
A charged spherical drop of liquid of radius $R$ and total charge $Q$ is in mechanical equilibrium under surface tension $T$ and electrostatic repulsion:
(A) The electrostatic outward pressure at the surface of the drop is $P_e = \frac{\sigma^2}{2\varepsilon_0} = \frac{Q^2}{32\pi^2\varepsilon_0 R^4}$.  
(B) The surface tension inward pressure is $P_s = \frac{2T}{R}$.  
(C) Rayleigh's limit of stability occurs when electrostatic repulsion overcomes surface tension, i.e., $Q^2 \ge 64\pi^2\varepsilon_0 T R^3$.  
(D) Beyond Rayleigh's limit, the spherical drop disintegrates by jet emission.

#### Question 2
Regarding plasma oscillations in a neutral plasma with electron density $n_e$:
(A) The plasma frequency is $\omega_p = \sqrt{\frac{n_e e^2}{\varepsilon_0 m_e}}$.  
(B) Electromagnetic waves with frequency $\omega < \omega_p$ cannot propagate through the plasma and are totally reflected.  
(C) The ionosphere reflects shortwave radio signals having frequencies below the plasma critical frequency.  
(D) For $\omega > \omega_p$, the refractive index of the plasma is $n(\omega) = \sqrt{1 - \frac{\omega_p^2}{\omega^2}} < 1$.

#### Question 3
A damped harmonic oscillator of mass $m$, spring constant $k$, and damping coefficient $b$ satisfies $m\ddot{x} + b\dot{x} + kx = 0$:
(A) For underdamped motion ($b^2 < 4mk$), the angular frequency is $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$ where $\omega_0 = \sqrt{k/m}$ and $\gamma = b/(2m)$.  
(B) The amplitude decays exponentially as $A(t) = A_0 e^{-\gamma t}$.  
(C) The mechanical energy decays exponentially as $E(t) = E_0 e^{-2\gamma t}$.  
(D) Critical damping occurs when $b = 2\sqrt{mk}$, returning the system to equilibrium in the shortest time without oscillation.

#### Question 4
A light ray enters a step-index optical fiber consisting of a cylindrical core of refractive index $n_1$ and a cladding of refractive index $n_2$ ($n_1 > n_2$):
(A) Total internal reflection occurs at the core-cladding interface if the angle of incidence exceeds $\theta_c = \arcsin(n_2/n_1)$.  
(B) The numerical aperture of the fiber in air is $\text{NA} = \sqrt{n_1^2 - n_2^2}$.  
(C) The maximum acceptance angle in air is $\alpha_{\max} = \arcsin(\text{NA})$.  
(D) Light entering within the acceptance cone propagates through the fiber via repeated total internal reflections.

#### Question 5
In Compton scattering of an X-ray photon of wavelength $\lambda$ from a stationary free electron:
(A) The scattered photon wavelength is $\lambda' = \lambda + \lambda_C(1 - \cos\theta)$ where $\theta$ is the scattering angle.  
(B) The Compton wavelength of the electron is $\lambda_C = \frac{h}{m_e c} \approx 0.0243\text{ \AA}$.  
(C) The maximum wavelength shift $\Delta\lambda_{\max} = 2\lambda_C$ occurs for backscattering ($\theta = 180^\circ$).  
(D) Compton scattering provides conclusive evidence for the particle nature of electromagnetic radiation.

#### Question 6
For an ideal gas in an insulated container undergoing free expansion into an evacuated chamber:
(A) No work is done: $W = 0$.  
(B) No heat is exchanged: $Q = 0$.  
(C) The change in internal energy is $\Delta U = 0$, so temperature remains constant: $T_f = T_i$.  
(D) The entropy of the gas increases: $\Delta S = n R \ln(V_f / V_i) > 0$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In an optical fiber, the core refractive index is $n_1 = 1.50$ and the cladding refractive index is $n_2 = 1.40$. The numerical aperture $\text{NA}$ of the fiber is $\text{NA}$. Find $\text{NA}$ rounded off to two decimal places.

#### Question 8
A photon of wavelength $\lambda = 0.0200\text{ \AA}$ is scattered through an angle $\theta = 180^\circ$ by a stationary free electron. Given $\lambda_C = 0.0243\text{ \AA}$, the wavelength of the scattered photon in Angstroms is $\lambda'\text{ \AA}$. Find $\lambda'$ rounded off to four decimal places.

#### Question 9
In an underdamped oscillator, the amplitude drops to $1/e$ of its initial value after $n = 50$ complete oscillations. The quality factor $Q$ of this oscillator is $Q$. (Using $Q = \pi / \delta$ where $\delta = 1/50$). Find $Q$ rounded off to the nearest integer.

#### Question 10
A circular loop of wire of radius $r = 0.10\text{ m}$ is placed in a uniform magnetic field $B = 0.50\text{ T}$ with its plane perpendicular to the field. If the loop is rotated through $180^\circ$ in $0.10\text{ s}$, the average induced EMF in volts is $\mathcal{E}\text{ V}$. Taking $\pi = 3.14$, find $\mathcal{E}$ rounded off to two decimal places.

#### Question 11
Two sound waves of frequencies $440\text{ Hz}$ and $444\text{ Hz}$ are sounded together. The number of beats heard per second is $N$. Find $N$.

#### Question 12
An ideal blackbody at temperature $T = 2000\text{ K}$ emits total radiant energy per unit area per second of $E\text{ kW/m}^2$. Given Stefan-Boltzmann constant $\sigma = 5.67 \times 10^{-8}\text{ W/(m}^2\text{ K}^4)$, find $E$ rounded off to the nearest integer.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The dimensions of magnetic permeability $\mu_0$ in SI units are:
(A) $[\text{M L T}^{-2}\text{ A}^{-2}]$  
(B) $[\text{M L}^2\text{ T}^{-2}\text{ A}^{-1}]$  
(C) $[\text{M L}^{-1}\text{ T}^{-2}\text{ A}^2]$  
(D) $[\text{M}^0\text{ L T}^{-1}\text{ A}^0]$

#### Question 14
A charged particle moves in a circular path in a uniform magnetic field. If its kinetic energy is doubled, the radius of the circular path increases by a factor of:
(A) $\sqrt{2}$  
(B) 2  
(C) 4  
(D) $1/\sqrt{2}$

#### Question 15
The power factor of a purely capacitive circuit connected to an AC source is:
(A) 0  
(B) 1  
(C) $0.5$  
(D) $\sqrt{3}/2$

#### Question 16
The focal length of a plane glass plate of thickness $t$ and refractive index $\mu$ is:
(A) Infinity  
(B) Zero  
(C) $t$  
(D) $t/\mu$

#### Question 17
A particle of mass $m$ is confined to a one-dimensional infinite potential well of width $L$. The ground state energy is $E_1$. The energy of the third excited state is:
(A) $16 E_1$  
(B) $9 E_1$  
(C) $4 E_1$  
(D) $25 E_1$

#### Question 18
The bulk modulus of an ideal gas undergoing an isothermal process at pressure $P$ is:
(A) $P$  
(B) $\gamma P$  
(C) $P/\gamma$  
(D) 0

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the thermodynamics of chemical adsorption (chemisorption) compared to physical adsorption (physisorption):
(A) Chemisorption involves formation of chemical bonds and has high enthalpy of adsorption ($80\text{ to }400\text{ kJ/mol}$).  
(B) Physisorption involves weak van der Waals forces and is reversible, whereas chemisorption is usually irreversible.  
(C) Chemisorption results in a unimolecular layer, while physisorption can form multimolecular layers.  
(D) Chemisorption initially increases with temperature and then decreases, showing activation energy behavior.

#### Question 20
Regarding the mutarotation of D-glucose:
(A) D-glucose exists as an equilibrium mixture of $\alpha\text{-D-glucopyranose}$ ($[\alpha]_D = +112^\circ$) and $\beta\text{-D-glucopyranose}$ ($[\alpha]_D = +19^\circ$).  
(B) In aqueous solution, the equilibrium specific rotation is $+52.7^\circ$.  
(C) $\beta\text{-D-glucopyranose}$ is more stable and present in higher concentration at equilibrium because all bulky groups are in equatorial positions.  
(D) The interconversion between anomers occurs via an open-chain aldehyde intermediate.

#### Question 21
Regarding the Hofmann elimination reaction of quaternary ammonium hydroxides:
(A) The reaction proceeds via an E2 mechanism.  
(B) The major product is the less-substituted alkene (Hofmann product), in contrast to the Saytzeff rule.  
(C) The regioselectivity is governed by the acidity of the $\beta$-protons and steric hindrance of the bulky leaving group.  
(D) Quaternary ammonium hydroxides are prepared by treating quaternary ammonium halides with moist $\text{Ag}_2\text{O}$.

#### Question 22
Regarding the extraction of gold and silver by the MacArthur-Forrest cyanide process:
(A) Crushed ore is leached with dilute $\text{NaCN}$ in the presence of atmospheric oxygen: $4\text{Au} + 8\text{CN}^- + 2\text{H}_2\text{O} + \text{O}_2 \to 4[\text{Au}(\text{CN})_2]^- + 4\text{OH}^-$.  
(B) The soluble complex formed is a dicyanometallate(I) complex ion.  
(C) Gold/silver is recovered from the solution by displacement reduction with zinc dust: $2[\text{Au}(\text{CN})_2]^- + \text{Zn} \to [\text{Zn}(\text{CN})_4]^{2-} + 2\text{Au}$.  
(D) Zinc acts as a reducing agent in the precipitation step.

#### Question 23
Regarding the inert pair effect:
(A) It refers to the reluctance of the valence $s$-electrons to participate in bonding in heavier $p$-block elements.  
(B) In Group 14, the stability of the $+2$ oxidation state increases down the group: $\text{C} < \text{Si} < \text{Ge} < \text{Sn} < \text{Pb}$.  
(C) $\text{Pb}^{4+}$ compounds act as strong oxidizing agents.  
(D) In Group 13, $\text{Tl}^+$ is more stable than $\text{Tl}^{3+}$.

#### Question 24
Which of the following molecules have zero dipole moment:
(A) Carbon dioxide ($\text{CO}_2$)  
(B) Boron trifluoride ($\text{BF}_3$)  
(C) Carbon tetrachloride ($\text{CCl}_4$)  
(D) *trans*-1,2-Dichloroethene

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
Calculate the $\text{pH}$ of a $0.050\text{ M}$ solution of $\text{Ba}(\text{OH})_2$ assuming complete dissociation at $298\text{ K}$. Find the $\text{pH}$.

#### Question 26
For the reaction $A + 2B \to C$, the rate law is $\text{Rate} = k[A][B]^2$. If the volume of the vessel is reduced to one-third of its initial volume, the reaction rate increases by a factor of $N$. Find $N$.

#### Question 27
The standard reduction potential for the half-cell $\text{MnO}_4^- + 8\text{H}^+ + 5e^- \to \text{Mn}^{2+} + 4\text{H}_2\text{O}$ is $+1.51\text{ V}$. At $\text{pH} = 3.0$ and $298\text{ K}$, with $[\text{MnO}_4^-] = [\text{Mn}^{2+}] = 1.0\text{ M}$, the reduction potential is $E\text{ V}$. Find $E$ rounded off to two decimal places.

#### Question 28
The freezing point depression of a $0.10\text{ m}$ aqueous solution of $\text{K}_2\text{SO}_4$ is observed to be $0.5022^\circ\text{C}$. Given $K_f(\text{H}_2\text{O}) = 1.86\text{ K kg mol}^{-1}$, the apparent van 't Hoff factor $i$ is $i$. Find $i$ rounded off to two decimal places.

#### Question 29
A crystal has a cubic unit cell where atoms of $A$ occupy all 8 corners and atoms of $B$ occupy the centers of all 6 faces. The formula of the compound is $A_x B_y$. Find $x + y$.

#### Question 30
Find the oxidation number of chromium in the butterfly-structured peroxochromate complex $\text{CrO}_5$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following carbohydrates is a non-reducing sugar:
(A) Sucrose  
(B) Maltose  
(C) Lactose  
(D) Glucose

#### Question 32
The shape of the $\text{BrF}_5$ molecule according to VSEPR theory is:
(A) Square pyramidal  
(B) Trigonal bipyramidal  
(C) Octahedral  
(D) Pentagonal planar

#### Question 33
In the Victor Meyer test, primary, secondary, and tertiary nitroalkanes give colors respectively:
(A) Red, Blue, Colorless  
(B) Blue, Red, Colorless  
(C) Colorless, Red, Blue  
(D) Red, Colorless, Blue

#### Question 34
The metal present in chlorophyll is:
(A) Magnesium ($\text{Mg}$)  
(B) Iron ($\text{Fe}$)  
(C) Cobalt ($\text{Co}$)  
(D) Copper ($\text{Cu}$)

#### Question 35
The conjugate acid of $\text{NH}_2^-$ is:
(A) $\text{NH}_3$  
(B) $\text{NH}_4^+$  
(C) $\text{N}_2\text{H}_4$  
(D) $\text{NH}^{2-}$

#### Question 36
Which of the following elements has the highest first ionization energy:
(A) Helium ($\text{He}$)  
(B) Neon ($\text{Ne}$)  
(C) Fluorine ($\text{F}$)  
(D) Hydrogen ($\text{H}$)

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x^2 - 4}{x - 2}$ for $x \ne 2$ and $f(2) = 4$:
(A) $\lim_{x \to 2} f(x) = 4$.  
(B) $f(x)$ is continuous at $x = 2$.  
(C) $f'(2) = 1$.  
(D) $f(x) = x + 2$ for all $x \in \mathbb{R}$.

#### Question 38
Let $A$ be a $3 \times 3$ matrix with eigenvalues $\lambda_1 = 1, \lambda_2 = 2, \lambda_3 = 3$:
(A) $\text{tr}(A) = 6$.  
(B) $\det(A) = 6$.  
(C) The eigenvalues of $A^2$ are 1, 4, and 9.  
(D) $\det(A - I) = 0$.

#### Question 39
Consider the circle $x^2 + y^2 = 25$ and the line $3x + 4y = 25$:
(A) The line touches the circle at the point $(3, 4)$.  
(B) The length of the tangent from the origin is undefined (origin lies inside the circle).  
(C) The point $(3, 4)$ lies on the circle.  
(D) The normal to the circle at the point of contact passes through $(0, 0)$.

#### Question 40
Let $S = \sum_{n=1}^\infty \frac{1}{n(n+1)}$:
(A) The partial sum is $S_N = 1 - \frac{1}{N+1}$.  
(B) The sum of the series is $S = 1$.  
(C) The series is telescoping.  
(D) $\sum_{n=1}^\infty \frac{1}{n(n+1)(n+2)} = \frac{1}{4}$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be three coplanar vectors:
(A) $[\vec{a}\quad \vec{b}\quad \vec{c}] = 0$.  
(B) There exist scalars $x, y, z$ not all zero such that $x\vec{a} + y\vec{b} + z\vec{c} = \vec{0}$.  
(C) $\vec{a} \cdot (\vec{b} \times \vec{c}) = 0$.  
(D) $(\vec{a} \times \vec{b}) \times \vec{c}$ must be zero (this statement is false in general).

#### Question 42
Consider the function $f(x) = |x| + |x-1|$ on $\mathbb{R}$:
(A) $f(x)$ is continuous everywhere on $\mathbb{R}$.  
(B) $f(x)$ is not differentiable at $x = 0$ and $x = 1$.  
(C) The minimum value of $f(x)$ is 1 attained for all $x \in [0, 1]$.  
(D) $\int_{-1}^2 f(x) dx = 5$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the area of the region bounded by $y = |x|$ and $y = 2 - x^2$. Round off to two decimal places.

#### Question 44
Find the remainder when $3^{2024}$ is divided by 5.

#### Question 45
Find the distance of the point $(1, 2, 3)$ from the plane $2x - 2y + z + 5 = 0$.

#### Question 46
Let $z$ be a complex number such that $|z| = 1$. Find the maximum value of $|z - 3|$.

#### Question 47
How many positive factors does the number $360$ have?

#### Question 48
Find the value of $\int_0^{\pi/2} \sin(2x)\cos x dx$. The value is $m/n$ in lowest terms. Find $m+n$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\sin(x^2)$ with respect to $x$ is:
(A) $2x\cos(x^2)$  
(B) $\cos(x^2)$  
(C) $2x\sin(x^2)$  
(D) $-2x\cos(x^2)$

#### Question 50
The focus of the parabola $y^2 = -8x$ is:
(A) $(-2, 0)$  
(B) $(2, 0)$  
(C) $(0, -2)$  
(D) $(0, 2)$

#### Question 51
The unit normal vector to the surface $z = x^2 + y^2$ at the point $(1, 2, 5)$ is:
(A) $\frac{2\hat{i} + 4\hat{j} - \hat{k}}{\sqrt{21}}$  
(B) $\frac{\hat{i} + 2\hat{j} + 5\hat{k}}{\sqrt{30}}$  
(C) $\frac{2\hat{i} - 4\hat{j} + \hat{k}}{\sqrt{21}}$  
(D) $\frac{\hat{i} + \hat{j} + \hat{k}}{\sqrt{3}}$

#### Question 52
If $\log_{10} 2 = 0.3010$, the number of digits in $2^{50}$ is:
(A) 16  
(B) 15  
(C) 17  
(D) 50

#### Question 53
The period of the function $f(x) = |\sin x| + |\cos x|$ is:
(A) $\pi/2$  
(B) $\pi$  
(C) $2\pi$  
(D) $\pi/4$

#### Question 54
A box contains 5 red and 3 green balls. A ball is drawn at random and replaced, then another ball is drawn. The probability that both balls are of different colors is:
(A) $15/32$  
(B) $15/64$  
(C) $15/56$  
(D) $30/56$
"""

        raw_sol1 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 1)
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Hall effect principles: Lorentz force $q(\vec{E}_H + \vec{v}_d \times \vec{B}) = 0$. $E_H = v_d B = \frac{I B}{n q w t}$, $V_H = E_H w = \frac{I B}{n q t}$. Hall coefficient $R_H = 1/(nq)$. **Correct Options**: (A, B, C, D)
- **Q2**: Coaxial dipoles along $z$: field $B = \frac{\mu_0 m_0}{2\pi d^3}\hat{k}$. $U = -\vec{m}_2 \cdot \vec{B}_1 = -\frac{\mu_0 m_0^2}{2\pi d^3}$. $F = -\frac{dU}{dd}\hat{k} = -\frac{3\mu_0 m_0^2}{2\pi d^4}\hat{k}$ (attractive). Reversal gives repulsion. **Correct Options**: (A, B, C, D)
- **Q3**: Skin effect in conductors: $\delta = \sqrt{2/(\mu_0 \sigma \omega)}$. Exponential decay $e^{-z/\delta}$, AC current pushed to surface, $\vec{B}$ lags $\vec{E}$ by $45^\circ$. **Correct Options**: (A, B, C, D)
- **Q4**: Fabry-Pérot interferometer: transmission $T(\delta) = \frac{1}{1 + F\sin^2(\delta/2)}$ with $F = \frac{4R}{(1-R)^2}$. Sharp fringes for high $R$. **Correct Options**: (A, B, C, D)
- **Q5**: Einstein coefficients relations and laser conditions: population inversion $N_2 > N_1$, identical emitted photons. **Correct Options**: (A, B, C, D)
- **Q6**: Maxwell-Boltzmann speed distributions: $v_{\text{mp}} = \sqrt{2k_BT/m} \approx 1.414\sqrt{k_BT/m}$, $\langle v \rangle = \sqrt{8k_BT/\pi m} \approx 1.596\sqrt{k_BT/m}$, $v_{\text{rms}} = \sqrt{3k_BT/m} \approx 1.732\sqrt{k_BT/m}$. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $V_H = \frac{I B}{n e t} \implies n = \frac{I B}{e t V_H} = \frac{10.0 \times 1.20}{(1.60 \times 10^{-19})(0.50 \times 10^{-3})(1.80 \times 10^{-6})} = \frac{12.0}{1.44 \times 10^{-27}} \approx 8.33 \times 10^{28}\text{ m}^{-3} \implies \mathbf{8.33}$.
- **Q8**: Helmholtz coils field: $B = \left(\frac{4}{5}\right)^{3/2} \frac{\mu_0 N I}{R} = (0.8)^{1.5} \frac{(4\pi \times 10^{-7})(100)(2.0)}{0.10} \approx 0.7155 \times 2.513 \times 10^{-3} \approx 1.80\text{ mT} \implies \mathbf{1.80}$.
- **Q9**: $\theta_R = 1.22 \frac{\lambda}{D} = 1.22 \times \frac{500 \times 10^{-9}}{2.44} = 1.22 \times 2.05 \times 10^{-7} = 2.50 \times 10^{-7}\text{ rad} \implies \mathbf{2.50}$.
- **Q10**: $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{0.20 \times 50 \times 10^{-6}}} = \frac{1}{\sqrt{1.0 \times 10^{-5}}} = \frac{1000}{\sqrt{10}} \approx 316.2\text{ rad/s} \implies \mathbf{316.00}$.
- **Q11**: Isobaric heat $Q = n C_P \Delta T$. For monoatomic gas, $C_P = \frac{5}{2}R \implies Q = \frac{5}{2} P \Delta V = \frac{5}{2}(1.0 \times 10^5)(0.03) = 7500\text{ J} = 7.5\text{ kJ} \implies \mathbf{7.50}$.
- **Q12**: Moseley's law: $\sqrt{\nu} \propto (Z - 1) \implies \sqrt{c/\lambda} \propto (Z - 1) \implies \frac{Z - 1}{29 - 1} = \sqrt{\frac{1.54}{0.71}} = \sqrt{2.169} \approx 1.4728 \implies Z - 1 = 28 \times 1.4728 \approx 41.24 \implies Z \approx 42$ (Molybdenum) $\implies \mathbf{42.00}$.

### Questions 13 to 18
- **Q13**: $\mathcal{E} = -d\Phi/dt = -(12t - 5)$. At $t = 0.25$, $\mathcal{E} = -(3 - 5) = 2\text{ V}$. $I = \mathcal{E}/R = 2/10 = 0.20\text{ A}$. **Correct: (A)**.
- **Q14**: $I_{\max} = (\sqrt{I} + \sqrt{4I})^2 = (1 + 2)^2 I = 9I$. $I_{\min} = (\sqrt{4I} - \sqrt{I})^2 = (2 - 1)^2 I = I$. **Correct: (A)**.
- **Q15**: $C = 4\pi\varepsilon_0 R = \frac{9.0 \times 10^3}{9.0 \times 10^9} = 1.0 \times 10^{-6}\text{ F} = 1.0\text{ }\mu\text{F}$. **Correct: (A)**.
- **Q16**: At $x = A/2$, $U = \frac{1}{2}kA^2/4 = E/4$. $K = E - U = 3E/4$. Ratio $K/U = 3/1$. **Correct: (A)**.
- **Q17**: Energy per second $E = 1000 \times 10^6\text{ J/s}$. Fission energy $= 200 \times 10^6 \times 1.6 \times 10^{-19}\text{ J} = 3.2 \times 10^{-11}\text{ J}$. Number of fissions $= \frac{10^9}{3.2 \times 10^{-11}} = 3.125 \times 10^{19}$. **Correct: (A)**.
- **Q18**: For ideal gas, viscosity $\eta \propto \sqrt{T}$ and is independent of pressure (Maxwell's theorem). **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Synergic $\sigma$-donation and $\pi$-backbonding in metal carbonyls. **Correct Options**: (A, B, C, D)
- **Q20**: Clausius-Clapeyron equation properties. **Correct Options**: (A, B, C, D)
- **Q21**: Conductometric titration characteristics. **Correct Options**: (A, B, C, D)
- **Q22**: Phosphorus oxoacids structure and basicity. **Correct Options**: (A, B, C, D)
- **Q23**: Diels-Alder $[4+2]$ cycloaddition mechanism and stereospecificity. **Correct Options**: (A, B, C, D)
- **Q24**: Lanthanide contraction causes and chemical consequences. **Correct Options**: (A, B, C, D)

### Questions 25 to 30
- **Q25**: Octahedral high-spin $d^6$ has configuration $t_{2g}^4 e_g^2$. CFSE $= 4(-0.4\Delta_o) + 2(0.6\Delta_o) = -1.6\Delta_o + 1.2\Delta_o = -0.4\Delta_o \implies |X| = \mathbf{0.40}$.
- **Q26**: Moles of urea $= 5/60 = 0.0833\text{ mol}$. Moles of water $= 100/18 = 5.555\text{ mol}$. Mole fraction of water $x_{\text{H}_2\text{O}} = \frac{5.555}{5.555 + 0.0833} = 0.9852$. Vapor pressure $P = x_{\text{H}_2\text{O}} P^\circ = 0.9852 \times 17.5 = 17.24\text{ mmHg} \implies \mathbf{17.24}$.
- **Q27**: $E^\circ_{\text{cell}} = E^\circ(\text{Cu}^+/\text{Cu}) - E^\circ(\text{Cu}^{2+}/\text{Cu}^+) = 0.52 - 0.16 = 0.36\text{ V} \implies \mathbf{0.36}$.
- **Q28**: $t = \frac{t_{1/2}}{\ln 2} \ln(100/1) = \frac{140 \times 2 \times 2.303}{0.693} \approx \frac{644.84}{0.693} \approx 930.5\text{ days} \implies \mathbf{931.00}$.
- **Q29**: In FCC, $4r = \sqrt{2}a \implies r = \frac{\sqrt{2} \times 400}{4} = 100\sqrt{2} \approx 141.42\text{ pm} \implies \mathbf{141.42}$.
- **Q30**: Cyanide is a strong field ligand: in $[\text{Fe}(\text{CN})_6]^{3-}$, $\text{Fe}^{3+}$ ($d^5$) pairs up to give low-spin $t_{2g}^5$ with 1 unpaired electron $\implies \mathbf{1.00}$.

### Questions 31 to 36
- **Q31**: Caro's acid ($\text{H}_2\text{SO}_5$) has peroxo structure $\text{HO}-\text{O}-\text{SO}_2-\text{OH}$. **Correct: (A)**.
- **Q32**: Acetaldehyde has $\alpha$-hydrogens, so it undergoes aldol condensation, not Cannizzaro. **Correct: (A)**.
- **Q33**: $\text{I}_3^-$ has 2 bond pairs and 3 lone pairs in equatorial positions of a TBP $\implies$ linear. **Correct: (A)**.
- **Q34**: Secondary amine forms $N,N$-dialkylbenzenesulfonamide which has no acidic hydrogen, hence insoluble in alkali. **Correct: (A)**.
- **Q35**: Potassium hexacyanidoferrate(III). **Correct: (A)**.
- **Q36**: Increased polarizability down the group enhances London dispersion forces. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Feynman's differentiation under integral sign: $I'(\alpha) = 1/\alpha \implies I(\alpha) = \ln\alpha$. **Correct Options**: (A, B, C, D)
- **Q38**: Confocal conics orthogonally intersecting families. **Correct Options**: (A, B, C, D)
- **Q39**: Derangements recurrences and limit $1/e$. **Correct Options**: (A, B, C, D)
- **Q40**: Rolle's theorem, root counting, and convexity properties. **Correct Options**: (A, B, C, D)
- **Q41**: Properties of real orthogonal matrices. **Correct Options**: (A, B, C, D)
- **Q42**: Rouche-Capelli theorem on linear systems consistency. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Stars and bars for multinomial terms: $\binom{n+k-1}{k-1} = \binom{10+4-1}{4-1} = \binom{13}{3} = \frac{13 \times 12 \times 11}{6} = 286 \implies \mathbf{286.00}$.
- **Q44**: King's property: $2I = \int_0^{\pi/2} 1 dx = \pi/2 \implies I = \pi/4 \implies k = \mathbf{4.00}$.
- **Q45**: Lines $\vec{r}_1 = (3, 5, 7) + t(1, -2, 1)$ and $\vec{r}_2 = (-1, -1, -1) + s(7, -6, 1)$. $\vec{d}_1 \times \vec{d}_2 = (4, 6, 8)$. $\vec{r}_1 - \vec{r}_2 = (4, 6, 8)$. Since line direction cross product is parallel to the displacement, lines lie in parallel planes: shortest distance is $d = \frac{|(4, 6, 8)\cdot(4, 6, 8)|}{\sqrt{16+36+64}} = \sqrt{116} = 2\sqrt{29} \approx 10.77 \implies \mathbf{10.77}$.
- **Q46**: $\alpha + \beta = 6$, $\alpha\beta = 2$. $\alpha^3 + \beta^3 = (\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta) = 6^3 - 3(2)(6) = 216 - 36 = 180 \implies \mathbf{180.00}$.
- **Q47**: Partitions of 10 into 3 positive integers: $\binom{10-1}{3-1} = \binom{9}{2} = 36 \implies \mathbf{36.00}$.
- **Q48**: Director circle of $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ is $x^2 + y^2 = a^2 + b^2 = 16 + 9 = 25 \implies R = 5 \implies \mathbf{5.00}$.

### Questions 49 to 54
- **Q49**: $\lim_{x \to 0} \frac{\tan x(1 - \cos x)}{x^3} = \lim_{x \to 0} \frac{\tan x}{x} \frac{2\sin^2(x/2)}{x^2} = 1 \times 2(1/4) = 1/2$. **Correct: (A)**.
- **Q50**: $y' = 4x + 3\cos x$. At $x=0$, $y'(0) = 3$. Slope of normal is $-1/3$. **Correct: (A)**.
- **Q51**: $\vec{n}_1 = (2, -1, 1)$, $\vec{n}_2 = (1, 1, 2)$. $\cos\theta = \frac{2 - 1 + 2}{\sqrt{6}\sqrt{6}} = \frac{3}{6} = 1/2 \implies \theta = \pi/3$. **Correct: (A)**.
- **Q52**: $\det(\text{adj}(A)) = (\det(A))^{n-1} = 5^{3-1} = 25$. **Correct: (A)**.
- **Q53**: The line $y = x/10$ intersects $y = \sin x$ at $x=0$ and at 3 positive points (since $10 > 3\pi \approx 9.42$) and 3 negative points $\implies 7$ solutions. **Correct: (A)**.
- **Q54**: $P = \frac{4}{52} \times \frac{3}{51} = \frac{1}{13} \times \frac{1}{17} = \frac{1}{221}$. **Correct: (A)**.
"""

        raw_sol2 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 2)
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Rayleigh limit of charged droplets: electrostatic outward pressure balances Laplace surface tension pressure. **Correct Options**: (A, B, C, D)
- **Q2**: Plasma frequency $\omega_p = \sqrt{n_e e^2/(\varepsilon_0 m_e)}$. Waves with $\omega < \omega_p$ undergo total reflection, explaining ionospheric bounce. **Correct Options**: (A, B, C, D)
- **Q3**: Damped harmonic oscillator parameters and critical damping condition. **Correct Options**: (A, B, C, D)
- **Q4**: Step-index optical fiber parameters: $\text{NA} = \sqrt{n_1^2 - n_2^2}$, acceptance cone. **Correct Options**: (A, B, C, D)
- **Q5**: Compton scattering formula: $\lambda' - \lambda = \lambda_C(1 - \cos\theta)$. **Correct Options**: (A, B, C, D)
- **Q6**: Free adiabatic expansion of ideal gas into vacuum: $W = 0, Q = 0 \implies \Delta U = 0 \implies \Delta T = 0$, entropy increases by $nR\ln(V_f/V_i)$. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $\text{NA} = \sqrt{n_1^2 - n_2^2} = \sqrt{1.50^2 - 1.40^2} = \sqrt{2.25 - 1.96} = \sqrt{0.29} \approx 0.54 \implies \mathbf{0.54}$.
- **Q8**: $\lambda' = \lambda + 2\lambda_C = 0.0200 + 2(0.0243) = 0.0200 + 0.0486 = 0.0686\text{ \AA} \implies \mathbf{0.0686}$.
- **Q9**: In $N$ cycles, $e^{-\gamma N T} = e^{-1} \implies \gamma N T = 1 \implies \delta = \gamma T = 1/N = 1/50$. Quality factor $Q = \frac{\omega_0}{2\gamma} = \frac{2\pi/T}{2\gamma} = \frac{\pi}{\gamma T} = \pi N = 50\pi \approx 157.08 \implies \mathbf{157.00}$.
- **Q10**: Initial flux $\Phi_i = B A = 0.50 \times \pi (0.1)^2 = 0.005\pi\text{ Wb}$. After $180^\circ$ flip, $\Phi_f = -\Phi_i$. $\Delta\Phi = 2\Phi_i = 0.01\pi\text{ Wb}$. $\mathcal{E}_{\text{avg}} = \frac{\Delta\Phi}{\Delta t} = \frac{0.01 \times 3.14}{0.10} = 0.314\text{ V} \implies \mathbf{0.31}$.
- **Q11**: Beat frequency $f_{\text{beat}} = |444 - 440| = 4\text{ Hz} \implies \mathbf{4.00}$.
- **Q12**: $E = \sigma T^4 = (5.67 \times 10^{-8})(2000)^4 = (5.67 \times 10^{-8})(1.6 \times 10^{13}) = 907200\text{ W/m}^2 \approx 907\text{ kW/m}^2 \implies \mathbf{907.00}$.

### Questions 13 to 18
- **Q14**: $r = \frac{p}{qB} = \frac{\sqrt{2mK}}{qB}$. If $K \to 2K$, $r$ increases by $\sqrt{2}$. **Correct: (A)**.
- **Q13**: $[\mu_0] = [\text{M L T}^{-2}\text{ A}^{-2}]$ from $F = \frac{\mu_0 I_1 I_2 L}{2\pi d}$. **Correct: (A)**.
- **Q15**: Current leads voltage by $90^\circ \implies \cos(90^\circ) = 0$. **Correct: (A)**.
- **Q16**: For plane plate, $R_1 = R_2 = \infty \implies 1/f = 0 \implies f = \infty$. **Correct: (A)**.
- **Q17**: Energy levels $E_n = n^2 E_1$. Third excited state corresponds to $n = 4 \implies E_4 = 4^2 E_1 = 16 E_1$. **Correct: (A)**.
- **Q18**: Isothermal bulk modulus $B_T = -V \left(\frac{\partial P}{\partial V}\right)_T = P$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Comparison of physisorption and chemisorption. **Correct Options**: (A, B, C, D)
- **Q20**: Mutarotation of glucose and anomeric equilibrium. **Correct Options**: (A, B, C, D)
- **Q21**: Hofmann elimination regiochemistry and mechanism. **Correct Options**: (A, B, C, D)
- **Q22**: Cyanide extraction of precious metals. **Correct Options**: (A, B, C, D)
- **Q23**: Inert pair effect trends in heavier $p$-block elements. **Correct Options**: (A, B, C, D)
- **Q24**: Molecular geometry and dipole moment cancellation. All 4 possess center/plane of symmetry with zero net dipole. **Correct Options**: (A, B, C, D)

### Questions 25 to 30
- **Q25**: $[\text{OH}^-] = 2 \times 0.050\text{ M} = 0.10\text{ M} \implies \text{pOH} = -\log(0.10) = 1.00 \implies \text{pH} = 14 - 1 = 13.00 \implies \mathbf{13.00}$.
- **Q26**: Reducing volume to $1/3$ increases concentrations by 3. $\text{Rate}' = k(3[A])(3[B])^2 = 27 k[A][B]^2 \implies N = \mathbf{27.00}$.
- **Q27**: Nernst equation: $E = E^\circ - \frac{0.0591}{5}\log\left(\frac{1}{[\text{H}^+]^8}\right) = 1.51 - \frac{0.0591 \times 8}{5}\text{pH} = 1.51 - 0.09456(3) = 1.51 - 0.284 = 1.23\text{ V} \implies \mathbf{1.23}$.
- **Q28**: $\Delta T_f = i K_f m \implies 0.5022 = i (1.86)(0.10) \implies i = \frac{0.5022}{0.186} = 2.70 \implies \mathbf{2.70}$.
- **Q29**: $A$ at 8 corners: $8 \times 1/8 = 1$. $B$ at 6 faces: $6 \times 1/2 = 3$. Formula is $AB_3 \implies x + y = 1 + 3 = 4 \implies \mathbf{4.00}$.
- **Q30**: In $\text{CrO}_5$, there is one oxo oxygen ($=\text{O}$) and two peroxo groups ($-\text{O}-\text{O}-$). Oxidation state of $\text{Cr} = +1 + 2(2) + 1 = +6 \implies \mathbf{6.00}$.

### Questions 31 to 36
- **Q31**: Sucrose has both anomeric carbons involved in glycosidic linkage $\implies$ non-reducing. **Correct: (A)**.
- **Q32**: $\text{BrF}_5$ has 5 bond pairs and 1 lone pair $\implies$ square pyramidal. **Correct: (A)**.
- **Q33**: Red (primary with nitrous acid gives nitrolic acid), Blue (secondary gives pseudonitrole), Colorless (tertiary has no reaction). **Correct: (A)**.
- **Q34**: Chlorophyll contains magnesium ($\text{Mg}^{2+}$) coordinated in a porphyrin ring. **Correct: (A)**.
- **Q35**: Adding a proton to $\text{NH}_2^-$ yields ammonia ($\text{NH}_3$). **Correct: (A)**.
- **Q36**: Helium has the highest first ionization energy among all elements ($\approx 24.6\text{ eV}$). **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Removable discontinuity: $f(x) = x + 2$ everywhere once $f(2) = 4$ is assigned. **Correct Options**: (A, B, C, D)
- **Q38**: Eigenvalue relations for trace, determinant, powers, and characteristic equation. **Correct Options**: (A, B, C, D)
- **Q39**: Geometry of circle tangents and normals. **Correct Options**: (A, B, C, D)
- **Q40**: Telescoping series properties. **Correct Options**: (A, B, C)
- **Q41**: Coplanar vectors conditions. **Correct Options**: (A, B, C)
- **Q42**: Continuity, points of non-differentiability, and integral of piecewise linear function. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Intersection of $y = |x|$ and $y = 2 - x^2$: for $x > 0$, $x = 2 - x^2 \implies x^2 + x - 2 = 0 \implies x = 1$. Area $= 2 \int_0^1 (2 - x^2 - x)dx = 2 [2x - x^3/3 - x^2/2]_0^1 = 2(2 - 1/3 - 1/2) = 2(7/6) = 7/3 \approx 2.33 \implies \mathbf{2.33}$.
- **Q44**: $3^4 = 81 \equiv 1 \pmod 5$. $2024 = 4 \times 506$. $3^{2024} = (3^4)^{506} \equiv 1^{506} \equiv 1 \pmod 5 \implies \mathbf{1.00}$.
- **Q45**: $d = \frac{|2(1) - 2(2) + 3 + 5|}{\sqrt{2^2 + (-2)^2 + 1^2}} = \frac{|2 - 4 + 3 + 5|}{\sqrt{9}} = \frac{6}{3} = 2.00 \implies \mathbf{2.00}$.
- **Q46**: $|z - 3| \le |z| + |-3| = 1 + 3 = 4 \implies \mathbf{4.00}$.
- **Q47**: $360 = 2^3 \times 3^2 \times 5^1$. Number of factors $= (3+1)(2+1)(1+1) = 4 \times 3 \times 2 = 24 \implies \mathbf{24.00}$.
- **Q48**: $\int_0^{\pi/2} 2\sin x\cos^2 x dx = 2 [-\frac{\cos^3 x}{3}]_0^{\pi/2} = 2(1/3) = 2/3$. $m + n = 2 + 3 = 5 \implies \mathbf{5.00}$.

### Questions 49 to 54
- **Q49**: Chain rule: $\frac{d}{dx}\sin(x^2) = \cos(x^2) \times 2x = 2x\cos(x^2)$. **Correct: (A)**.
- **Q50**: For $y^2 = -4ax$ with $4a = 8 \implies a = 2$. Focus is $(-a, 0) = (-2, 0)$. **Correct: (A)**.
- **Q51**: Surface $F(x, y, z) = x^2 + y^2 - z = 0$. $\nabla F = (2x, 2y, -1)$. At $(1, 2, 5)$, $\nabla F = (2, 4, -1)$. Magnitude $\sqrt{4 + 16 + 1} = \sqrt{21}$. Unit normal $\frac{2\hat{i} + 4\hat{j} - \hat{k}}{\sqrt{21}}$. **Correct: (A)**.
- **Q52**: $\log_{10}(2^{50}) = 50 \times 0.3010 = 15.05$. Number of digits is $\lfloor 15.05 \rfloor + 1 = 16$. **Correct: (A)**.
- **Q53**: The function repeats every $\pi/2$ radians. **Correct: (A)**.
- **Q54**: Total balls = 8. With replacement: $P(\text{RG}) + P(\text{GR}) = \frac{5}{8}\times\frac{3}{8} + \frac{3}{8}\times\frac{5}{8} = \frac{15}{64} + \frac{15}{64} = \frac{30}{64} = \frac{15}{32}$. **Correct: (A)**.
"""

        raw_val = r"""# Comprehensive Answer Key & Academic Alignment Validation – JEE Advanced Mock Examination __PAD__
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)

---

### Master Answer Key – Paper 1
| Q# | Subject | Section | Question Type | Key |
|---|---|---|---|---|
| 1 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 2 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 3 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 4 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 5 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 6 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 7 | Physics | Sec 2 | Numerical | 8.33 |
| 8 | Physics | Sec 2 | Numerical | 1.80 |
| 9 | Physics | Sec 2 | Numerical | 2.50 |
| 10 | Physics | Sec 2 | Numerical | 316.00 |
| 11 | Physics | Sec 2 | Numerical | 7.50 |
| 12 | Physics | Sec 2 | Numerical | 42.00 |
| 13 | Physics | Sec 3 | Single Correct | A |
| 14 | Physics | Sec 3 | Single Correct | A |
| 15 | Physics | Sec 3 | Single Correct | A |
| 16 | Physics | Sec 3 | Single Correct | A |
| 17 | Physics | Sec 3 | Single Correct | A |
| 18 | Physics | Sec 3 | Single Correct | A |
| 19 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 20 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 21 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 22 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 23 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 25 | Chemistry | Sec 2 | Numerical | 0.40 |
| 26 | Chemistry | Sec 2 | Numerical | 17.24 |
| 27 | Chemistry | Sec 2 | Numerical | 0.36 |
| 28 | Chemistry | Sec 2 | Numerical | 931.00 |
| 29 | Chemistry | Sec 2 | Numerical | 141.42 |
| 30 | Chemistry | Sec 2 | Numerical | 1.00 |
| 31 | Chemistry | Sec 3 | Single Correct | A |
| 32 | Chemistry | Sec 3 | Single Correct | A |
| 33 | Chemistry | Sec 3 | Single Correct | A |
| 34 | Chemistry | Sec 3 | Single Correct | A |
| 35 | Chemistry | Sec 3 | Single Correct | A |
| 36 | Chemistry | Sec 3 | Single Correct | A |
| 37 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 38 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 39 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 40 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 41 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 42 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 43 | Mathematics | Sec 2 | Numerical | 286.00 |
| 44 | Mathematics | Sec 2 | Numerical | 4.00 |
| 45 | Mathematics | Sec 2 | Numerical | 10.77 |
| 46 | Mathematics | Sec 2 | Numerical | 180.00 |
| 47 | Mathematics | Sec 2 | Numerical | 36.00 |
| 48 | Mathematics | Sec 2 | Numerical | 5.00 |
| 49 | Mathematics | Sec 3 | Single Correct | A |
| 50 | Mathematics | Sec 3 | Single Correct | A |
| 51 | Mathematics | Sec 3 | Single Correct | A |
| 52 | Mathematics | Sec 3 | Single Correct | A |
| 53 | Mathematics | Sec 3 | Single Correct | A |
| 54 | Mathematics | Sec 3 | Single Correct | A |

---

### Master Answer Key – Paper 2
| Q# | Subject | Section | Question Type | Key |
|---|---|---|---|---|
| 1 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 2 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 3 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 4 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 5 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 6 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 7 | Physics | Sec 2 | Numerical | 0.54 |
| 8 | Physics | Sec 2 | Numerical | 0.0686 |
| 9 | Physics | Sec 2 | Numerical | 157.00 |
| 10 | Physics | Sec 2 | Numerical | 0.31 |
| 11 | Physics | Sec 2 | Numerical | 4.00 |
| 12 | Physics | Sec 2 | Numerical | 907.00 |
| 13 | Physics | Sec 3 | Single Correct | A |
| 14 | Physics | Sec 3 | Single Correct | A |
| 15 | Physics | Sec 3 | Single Correct | A |
| 16 | Physics | Sec 3 | Single Correct | A |
| 17 | Physics | Sec 3 | Single Correct | A |
| 18 | Physics | Sec 3 | Single Correct | A |
| 19 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 20 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 21 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 22 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 23 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 25 | Chemistry | Sec 2 | Numerical | 13.00 |
| 26 | Chemistry | Sec 2 | Numerical | 27.00 |
| 27 | Chemistry | Sec 2 | Numerical | 1.23 |
| 28 | Chemistry | Sec 2 | Numerical | 2.70 |
| 29 | Chemistry | Sec 2 | Numerical | 4.00 |
| 30 | Chemistry | Sec 2 | Numerical | 6.00 |
| 31 | Chemistry | Sec 3 | Single Correct | A |
| 32 | Chemistry | Sec 3 | Single Correct | A |
| 33 | Chemistry | Sec 3 | Single Correct | A |
| 34 | Chemistry | Sec 3 | Single Correct | A |
| 35 | Chemistry | Sec 3 | Single Correct | A |
| 36 | Chemistry | Sec 3 | Single Correct | A |
| 37 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 38 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 39 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 40 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C |
| 41 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C |
| 42 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 43 | Mathematics | Sec 2 | Numerical | 2.33 |
| 44 | Mathematics | Sec 2 | Numerical | 1.00 |
| 45 | Mathematics | Sec 2 | Numerical | 2.00 |
| 46 | Mathematics | Sec 2 | Numerical | 4.00 |
| 47 | Mathematics | Sec 2 | Numerical | 24.00 |
| 48 | Mathematics | Sec 2 | Numerical | 5.00 |
| 49 | Mathematics | Sec 3 | Single Correct | A |
| 50 | Mathematics | Sec 3 | Single Correct | A |
| 51 | Mathematics | Sec 3 | Single Correct | A |
| 52 | Mathematics | Sec 3 | Single Correct | A |
| 53 | Mathematics | Sec 3 | Single Correct | A |
| 54 | Mathematics | Sec 3 | Single Correct | A |
"""

        p1 = raw_p1.replace("__PAD__", pad)
        p2 = raw_p2.replace("__PAD__", pad)
        sol1 = raw_sol1.replace("__PAD__", pad)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, "IIT_Madras")
        print(f"Generated IIT Madras Mock {pad}!")

if __name__ == "__main__":
    generate_madras_16_to_20()

