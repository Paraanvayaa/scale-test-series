# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Guwahati Mocks 05, 06, 07, 08.
Calibrated strictly to IIT Guwahati empirical signature (2009, 2016, 2023):
- High Modern Physics (relativistic kinematics, wave equations, cavity radiation, Compton, Bragg)
- High Thermodynamics & Statistical Mechanics (entropy of mixing, Rankine, Otto, van der Waals critical states)
- High Physical Chemistry (electrochemistry, chemical equilibria, kinetics, phase transitions, colloids)
- Clean Organic Synthesis with unambiguous stereochemistry (Diels-Alder, pinacol, ozonolysis, aldol)
- Geometric Elegance in Conics, Vectors, Argand Plane, and Definite Integrals
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

def generate_guwahati_05():
    p1 = r"""# JEE Advanced Mock Examination 05 – Paper 1
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
One mole of an ideal gas undergoes a cycle on the $T-S$ diagram consisting of: $A \to B$ isothermal expansion at $T_H$ where entropy increases by $\Delta S_0$, $B \to C$ reversible adiabatic expansion to $T_C$, $C \to D$ isothermal compression at $T_C$ where entropy decreases by $\Delta S_0$, and $D \to A$ reversible adiabatic compression to $T_H$:
(A) The cycle represents an ideal Carnot engine.  
(B) The heat absorbed from the hot reservoir is $Q_H = T_H \Delta S_0$.  
(C) The net work done by the gas is $W = (T_H - T_C)\Delta S_0$.  
(D) The thermal efficiency of the cycle is $\eta = 1 - \frac{T_C}{T_H}$.

#### Question 2
In the relativistic collision of an electron (rest mass $m_0$) having total energy $E$ with a stationary electron:
(A) The center-of-mass energy squared is $s = 2 m_0 c^2 (E + m_0 c^2)$.  
(B) If $E \gg m_0 c^2$, the available energy in the center-of-mass frame scales as $\sqrt{E}$.  
(C) Total momentum is conserved in all inertial reference frames.  
(D) The threshold kinetic energy for creating an electron-positron pair ($e^- + e^- \to e^- + e^- + e^- + e^+$) is $6 m_0 c^2$.

#### Question 3
A point mass $m$ is suspended by a massless string of length $l$ from a fixed support. It executes conical pendulum motion with semi-vertical angle $\theta$:
(A) The tension in the string is $T = \frac{m g}{\cos\theta}$.  
(B) The angular velocity of rotation is $\omega = \sqrt{\frac{g}{l \cos\theta}}$.  
(C) The period of rotation is $\tau = 2\pi \sqrt{\frac{l \cos\theta}{g}}$.  
(D) As $\theta \to 90^\circ$, the required angular velocity and tension approach infinity.

#### Question 4
A grounded infinite conducting plane is located at $z = 0$. A point charge $+q$ is placed on the z-axis at $(0, 0, d)$ where $d > 0$:
(A) The electric potential for $z > 0$ can be found using an image charge $-q$ at $(0, 0, -d)$.  
(B) The surface charge density induced on the conducting plane is $\sigma(r) = -\frac{q d}{2\pi (r^2 + d^2)^{3/2}}$.  
(C) The total induced charge on the conducting plane is $-q$.  
(D) The attractive force between the charge $+q$ and the plane is $F = \frac{q^2}{16\pi \varepsilon_0 d^2}$.

#### Question 5
In an interference experiment using a Fresnel biprism of small refracting angle $\alpha$ and refractive index $\mu$, illuminated by a slit of wavelength $\lambda$ at distance $u$ from the biprism:
(A) The biprism produces two virtual coherent slit sources separated by distance $d = 2 u (\mu - 1)\alpha$.  
(B) The fringe width on a screen at distance $D$ from the virtual sources is $\beta = \frac{\lambda D}{d}$.  
(C) The fringes are hyperbolic near the axis and straight lines far from the axis.  
(D) If the slit is moved closer to the biprism, the fringe width decreases.

#### Question 6
Regarding the rotational spectrum of a rigid diatomic molecule of reduced mass $\mu$ and equilibrium bond length $r_0$:
(A) The rotational energy levels are quantized as $E_J = \frac{\hbar^2}{2 I} J(J + 1)$, where $I = \mu r_0^2$ and $J = 0, 1, 2, \dots$.  
(B) The transition selection rule for electric dipole absorption is $\Delta J = \pm 1$.  
(C) The absorption lines in the rotational spectrum are equally spaced in frequency with separation $\Delta \nu = \frac{\hbar}{2\pi I}$.  
(D) The degeneracy of each rotational energy level $J$ is $2J + 1$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
Two moles of helium gas (ideal monoatomic, $\gamma = 5/3$) are initially at $300\text{ K}$. The gas is heated at constant pressure until its volume doubles. Calculate the heat supplied in kilojoules ($\text{kJ}$). (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to two decimal places).

#### Question 8
In an electron microscope, electrons are accelerated from rest through a potential difference $V = 10.0\text{ kV}$. Calculate the non-relativistic de Broglie wavelength of the electrons in picometers ($\text{pm}$). (Take $h = 6.63 \times 10^{-34}\text{ J}\cdot\text{s}, m_e = 9.11 \times 10^{-31}\text{ kg}, e = 1.60 \times 10^{-19}\text{ C}$. Round off to two decimal places).

#### Question 9
A flywheel of mass $M = 20.0\text{ kg}$ and radius $R = 0.50\text{ m}$ is in the shape of a uniform disk. It is rotating at $600\text{ rpm}$. A braking torque of $\tau = 50.0\text{ N}\cdot\text{m}$ is applied. Find the time in seconds required for the flywheel to come to rest. (Take $\pi \approx 3.1416$. Round off to two decimal places).

#### Question 10
A solenoid of length $l = 0.50\text{ m}$ and cross-sectional area $A = 2.0 \times 10^{-3}\text{ m}^2$ has $N = 1000\text{ turns}$. Calculate the self-inductance $L$ of the solenoid in millihenries ($\text{mH}$). (Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$. Round off to two decimal places).

#### Question 11
In a double-slit experiment, the slit separation is $d = 0.40\text{ mm}$ and the screen is at $D = 1.0\text{ m}$. When light of wavelength $\lambda = 500\text{ nm}$ is used, find the fringe width in millimeters.

#### Question 12
A vertical U-tube of uniform cross-section contains mercury. When water of height $h_w = 13.6\text{ cm}$ is poured into one arm, find the rise in the mercury level in the other arm in millimeters. (Density of mercury $= 13.6\text{ g/cm}^3$, density of water $= 1.0\text{ g/cm}^3$).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle moves in a potential $V(r) = -k/r$. The Laplace-Runge-Lenz vector $\vec{A} = \vec{p} \times \vec{L} - m k \hat{r}$ is:
(A) A conserved vector pointing along the major axis towards the perihelion  
(B) A time-varying vector perpendicular to the orbital plane  
(C) Conserved only for circular orbits  
(D) Equal to the angular momentum vector

#### Question 14
The capacitance of an isolated spherical conductor of radius $R = 9.0\text{ cm}$ in air is:
(A) $10\text{ pF}$  
(B) $1\text{ pF}$  
(C) $100\text{ pF}$  
(D) $0.1\text{ pF}$

#### Question 15
When unpolarized light is incident at the Brewster angle $\theta_B$ on a dielectric surface of refractive index $\mu = \sqrt{3}$, the reflected ray is:
(A) Completely plane-polarized perpendicular to the plane of incidence, with $\theta_B = 60^\circ$  
(B) Unpolarized, with $\theta_B = 30^\circ$  
(C) Circularly polarized  
(D) Completely plane-polarized in the plane of incidence

#### Question 16
An ideal gas undergoes an adiabatic expansion where $V$ triples. If $\gamma = 1.4$, the ratio of final temperature to initial temperature is:
(A) $(1/3)^{0.4} \approx 0.64$  
(B) $3^{0.4} \approx 1.55$  
(C) $1/3$  
(D) $3^{1.4}$

#### Question 17
A proton moves with speed $v = 2.0 \times 10^6\text{ m/s}$ perpendicular to a magnetic field $B = 0.5\text{ T}$. The radius of its circular orbit is: (Take $m_p = 1.67 \times 10^{-27}\text{ kg}, e = 1.6 \times 10^{-19}\text{ C}$)
(A) $4.18\text{ cm}$  
(B) $2.09\text{ cm}$  
(C) $8.35\text{ cm}$  
(D) $1.05\text{ cm}$

#### Question 18
The decay constant of a radioactive sample is $\lambda = 0.05\text{ day}^{-1}$. Its mean life is:
(A) $20\text{ days}$  
(B) $13.86\text{ days}$  
(C) $10\text{ days}$  
(D) $40\text{ days}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution of a sparingly soluble salt $A_2 B$ ($K_{sp} = 3.2 \times 10^{-11}$):
(A) The dissolution equilibrium is $A_2 B(s) \rightleftharpoons 2 A^+(aq) + B^{2-}(aq)$.  
(B) The solubility $s$ in pure water is given by $K_{sp} = 4 s^3$.  
(C) The molar solubility in pure water is $s = 2.0 \times 10^{-4}\text{ M}$.  
(D) The solubility of $A_2 B$ is decreased in the presence of $0.01\text{ M}$ $A^+$ due to the common ion effect.

#### Question 20
Regarding the kinetic theory of enzymes and the Lineweaver-Burk equation $\frac{1}{v} = \frac{K_m}{V_{\max}}\frac{1}{[S]} + \frac{1}{V_{\max}}$:
(A) A plot of $1/v$ versus $1/[S]$ yields a straight line with slope $\frac{K_m}{V_{\max}}$.  
(B) The y-intercept represents $\frac{1}{V_{\max}}$.  
(C) The x-intercept represents $-\frac{1}{K_m}$.  
(D) A competitive inhibitor increases $K_m$ without altering $V_{\max}$.

#### Question 21
Regarding the chemistry of transition metal complexes with $\text{CO}$ and $\text{NO}$ ligands:
(A) $\text{CO}$ is a strong field $\pi$-acid ligand.  
(B) Nitrosyl ($\text{NO}$) can act as a 3-electron donor as $\text{NO}^+$ (linear $\text{M-N-O}$) or a 1-electron donor as $\text{NO}^-$ (bent $\text{M-N-O}$).  
(C) In sodium nitroprusside $\text{Na}_2[\text{Fe}(\text{CN})_5(\text{NO})]$, iron is in $+2$ oxidation state and $\text{NO}$ is present as $\text{NO}^+$.  
(D) The complex $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$ (brown ring complex) contains iron in $+1$ oxidation state with 3 unpaired electrons ($\mu \approx 3.87\ \mu_B$).

#### Question 22
Which of the following statements regarding the aldol reaction and its variants is/are correct?
(A) The cross-aldol condensation of benzaldehyde with acetaldehyde yields cinnamaldehyde.  
(B) Intramolecular aldol condensation of hexane-2,5-dione in basic medium yields 3-methylcyclopent-2-en-1-one.  
(C) The aldol addition product $\beta$-hydroxy aldehyde readily undergoes dehydration upon heating to form an $\alpha,\beta$-unsaturated aldehyde.  
(D) Ketones generally give lower equilibrium yields in self-aldol additions than aldehydes due to steric and electronic factors.

#### Question 23
Regarding the chemistry of halogens and pseudohalogens:
(A) Fluorine exhibits only the $-1$ oxidation state in all its compounds due to being the most electronegative element without valence $d$-orbitals.  
(B) The oxidizing power of halogens follows the order $\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$.  
(C) Cyanogen ($(\text{CN})_2$) is a pseudohalogen and forms pseudohalide ions $\text{CN}^-$.  
(D) Bleaching powder ($\text{CaOCl}_2$) contains both $\text{Cl}^-$ ($-1$) and $\text{OCl}^-$ ($+1$) ions.

#### Question 24
Which of the following organic compounds will evolve $\text{CO}_2$ gas upon reaction with aqueous $\text{NaHCO}_3$?
(A) Benzoic acid  
(B) Acetic acid  
(C) 2,4,6-Trinitrophenol (Picric acid)  
(D) Phenol

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The rate constant for a reaction at $300\text{ K}$ is $k_1 = 1.0 \times 10^{-3}\text{ s}^{-1}$ and at $320\text{ K}$ is $k_2 = 4.0 \times 10^{-3}\text{ s}^{-1}$. Calculate the activation energy $E_a$ in $\text{kJ/mol}$. (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}, \ln 4 \approx 1.3863$. Round off to two decimal places).

#### Question 26
Calculate the solubility of silver bromide ($\text{AgBr}$, $K_{sp} = 5.0 \times 10^{-13}$) in pure water in units of $10^{-7}\text{ M}$. (Take $\sqrt{5} \approx 2.236$. Round off to two decimal places).

#### Question 27
A $0.20\text{ m}$ aqueous solution of a weak monobasic acid $\text{HA}$ is $2.0\%$ ionized at $25^\circ\text{C}$. Calculate the freezing point of this solution in $^\circ\text{C}$. (Take $K_f = 1.86\text{ K}\cdot\text{kg/mol}$. Round off to three decimal places).

#### Question 28
Calculate the packing efficiency of a body-centered cubic (BCC) crystal lattice in percentage. (Round off to two decimal places).

#### Question 29
A buffer solution is prepared by mixing $0.15\text{ mol}$ of ammonia ($\text{NH}_3, K_b = 1.8 \times 10^{-5}$) and $0.15\text{ mol}$ of ammonium chloride ($\text{NH}_4\text{Cl}$) in $1.0\text{ L}$ of water. Calculate the pH of the buffer solution. (Take $\text{p}K_b \approx 4.74$. Round off to two decimal places).

#### Question 30
Find the number of moles of electrons required to reduce 1 mole of nitrobenzene ($\text{C}_6\text{H}_5\text{NO}_2$) completely to aniline ($\text{C}_6\text{H}_5\text{NH}_2$).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Williamson ether synthesis, the reaction of sodium ethoxide with 2-bromo-2-methylpropane yields:
(A) 2-Methylpropene as major product via E2 elimination  
(B) Ethyl tert-butyl ether as major product via $S_N2$  
(C) Diethyl ether  
(D) Di-tert-butyl ether

#### Question 32
Which of the following species is diamagnetic?
(A) $\text{O}_2^{2-}$ (Peroxide ion)  
(B) $\text{O}_2$  
(C) $\text{O}_2^-$ (Superoxide ion)  
(D) $\text{NO}$

#### Question 33
The correct order of stability for the alkali metal hydrides is:
(A) $\text{LiH} > \text{NaH} > \text{KH} > \text{RbH} > \text{CsH}$  
(B) $\text{CsH} > \text{RbH} > \text{KH} > \text{NaH} > \text{LiH}$  
(C) $\text{NaH} > \text{LiH} > \text{KH} > \text{RbH} > \text{CsH}$  
(D) $\text{LiH} > \text{KH} > \text{NaH} > \text{RbH} > \text{CsH}$

#### Question 34
In the extraction of gold by cyanide leaching, the soluble complex formed is:
(A) $[\text{Au}(\text{CN})_2]^-$  
(B) $[\text{Au}(\text{CN})_4]^-$  
(C) $[\text{Au}(\text{CN})_6]^{3-}$  
(D) $[\text{AuCl}_4]^-$

#### Question 35
The amino acid which is optically inactive is:
(A) Glycine  
(B) Alanine  
(C) Valine  
(D) Leucine

#### Question 36
In the reaction $\text{R-CONH}_2 + \text{Br}_2 + 4\text{NaOH} \to \text{R-NH}_2 + \text{Na}_2\text{CO}_3 + 2\text{NaBr} + 2\text{H}_2\text{O}$ (Hofmann bromamide degradation), the intermediate that undergoes rearrangement is:
(A) Acyl nitrene / Alkyl isocyanate  
(B) Carbocation  
(C) Free radical  
(D) Carbanion

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x e^{-x}$ for $x \in \mathbb{R}$:
(A) $f(x)$ is strictly increasing on $(-\infty, 1)$ and strictly decreasing on $(1, \infty)$.  
(B) The absolute maximum of $f(x)$ on $\mathbb{R}$ is $\frac{1}{e}$, attained at $x = 1$.  
(C) The inflection point of the graph is at $(2, 2 e^{-2})$.  
(D) $\lim_{x \to \infty} f(x) = 0$.

#### Question 38
Consider the ellipse $\frac{x^2}{25} + \frac{y^2}{16} = 1$:
(A) The eccentricity is $e = \frac{3}{5}$.  
(B) The foci lie at $(\pm 3, 0)$.  
(C) The length of the latus rectum is $\frac{32}{5}$.  
(D) The equations of the directrices are $x = \pm \frac{25}{3}$.

#### Question 39
Let $z$ be a complex number satisfying $\text{Re}\left(\frac{z - 1}{z + 1}\right) = 0$ ($z \ne -1$):
(A) The locus of $z$ is the unit circle $|z| = 1$ (excluding $z = -1$).  
(B) The triangle formed by $z, 1, -1$ in the Argand plane is a right-angled triangle.  
(C) $\arg\left(\frac{z - 1}{z + 1}\right) = \pm \frac{\pi}{2}$.  
(D) $|z|^2 = 1$.

#### Question 40
Let $A$ be a $3 \times 3$ matrix such that $A^3 = I_3$ and $A \ne I_3$:
(A) The eigenvalues of $A$ can be $1, \omega, \omega^2$ where $\omega$ is complex cube root of 1.  
(B) If $A$ is real, $\det(A) = 1$.  
(C) $\text{Tr}(A)$ can equal $0$ if eigenvalues are $1, \omega, \omega^2$.  
(D) $A$ is invertible with $A^{-1} = A^2$.

#### Question 41
Let $I_n = \int_0^{\pi/2} \cos^n x \, dx$ for $n \ge 0$:
(A) $I_0 = \frac{\pi}{2}$ and $I_1 = 1$.  
(B) For $n \ge 2$, $I_n = \frac{n-1}{n} I_{n-2}$.  
(C) $\int_0^{\pi/2} \sin^n x \, dx = \int_0^{\pi/2} \cos^n x \, dx$.  
(D) $\lim_{n \to \infty} I_n = 0$.

#### Question 42
Consider the planes $x + y + z = 3$ and $2x - y + z = 2$:
(A) The direction ratios of the line of intersection are $(2, 1, -3)$.  
(B) The point $(1, 1, 1)$ lies on both planes.  
(C) The planes are not perpendicular.  
(D) The angle between the normal vectors is $\arccos\left(\frac{2}{\sqrt{18}}\right)$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = 4 - x^2$ and the x-axis. (Round off to two decimal places).

#### Question 44
Evaluate the definite integral $K = \int_0^1 x (1 - x)^9 \, dx$. (Express as $\frac{1}{N}$, find $N$).

#### Question 45
Find the number of points of local extremum of $f(x) = x^4 - 4x^3 + 4x^2 + 1$.

#### Question 46
Let $\vec{a} = \hat{i} + 2\hat{j} + 3\hat{k}$ and $\vec{b} = 2\hat{i} - \hat{j} + \hat{k}$. Calculate the scalar product $(\vec{a} \times \vec{b}) \cdot \vec{a}$.

#### Question 47
A problem in mathematics is given to three students $A, B, C$ whose chances of solving it are $\frac{1}{2}, \frac{1}{3}, \frac{1}{4}$ respectively. Find the probability (in percentage) that the problem is solved. (Round off to two decimal places).

#### Question 48
Find the radius of the circle $x^2 + y^2 - 2x - 4y - 20 = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arctan\left(\frac{\sqrt{1 + x^2} - 1}{x}\right)$ with respect to $x$ is:
(A) $\frac{1}{2(1 + x^2)}$  
(B) $\frac{1}{1 + x^2}$  
(C) $\frac{2}{1 + x^2}$  
(D) $\frac{1}{\sqrt{1 + x^2}}$

#### Question 50
The length of the focal chord of the parabola $y^2 = 4ax$ making an angle $\theta$ with the axis is:
(A) $4 a \csc^2\theta$  
(B) $4 a \sin^2\theta$  
(C) $4 a \cos^2\theta$  
(D) $2 a \csc\theta$

#### Question 51
The value of $\lim_{x \to 0} \frac{\ln(1 + 2x)}{\sin 3x}$ is:
(A) $\frac{2}{3}$  
(B) $\frac{3}{2}$  
(C) $1$  
(D) $0$

#### Question 52
If $A$ and $B$ are square matrices of order 3 such that $\det(A) = 2$ and $\det(B) = 3$, then $\det(2 A B)$ is:
(A) $48$  
(B) $12$  
(C) $24$  
(D) $6$

#### Question 53
In how many ways can 4 letters be posted in 3 letter boxes?
(A) $3^4 = 81$  
(B) $4^3 = 64$  
(C) $12$  
(D) $24$

#### Question 54
The general solution of the differential equation $\frac{dy}{dx} = 2x y$ is:
(A) $y = C e^{x^2}$  
(B) $y = C e^{2x}$  
(C) $y = x^2 + C$  
(D) $y = C e^{-x^2}$
"""

    p2 = r"""# JEE Advanced Mock Examination 05 – Paper 2
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
A real gas undergoing throttling (Joule-Thomson expansion) through a porous plug:
(A) The enthalpy of the gas is conserved ($H_1 = H_2$).  
(B) If the initial temperature is below the inversion temperature ($T < T_i$), the gas cools upon expansion.  
(C) For an ideal gas, the temperature remains unchanged.  
(D) The process is completely irreversible and entropy of the universe increases.

#### Question 2
Consider Bohr's quantization condition for hydrogen-like atoms of atomic number $Z$:
(A) Orbital radius scales as $r_n \propto \frac{n^2}{Z}$.  
(B) Orbital speed scales as $v_n \propto \frac{Z}{n}$.  
(C) Total orbital energy scales as $E_n \propto -\frac{Z^2}{n^2}$.  
(D) Orbital magnetic dipole moment scales as $\mu_n \propto n$.

#### Question 3
A convex spherical glass surface of radius $R = 10.0\text{ cm}$ and refractive index $\mu = 1.50$ separates air from glass. An object is placed in air on the principal axis:
(A) The refraction formula is $\frac{\mu}{v} - \frac{1}{u} = \frac{\mu - 1}{R}$.  
(B) The first focal length in air is $f_1 = -20.0\text{ cm}$.  
(C) The second focal length in glass is $f_2 = +30.0\text{ cm}$.  
(D) For an object at $u = -40.0\text{ cm}$, the image is formed at $v = +60.0\text{ cm}$ in glass.

#### Question 4
A long coaxial cable consists of an inner solid cylindrical conductor of radius $a$ carrying steady current $I$ and an outer thin cylindrical shell of radius $b$ carrying equal return current $I$:
(A) The magnetic field for $r < a$ is $B = \frac{\mu_0 I r}{2\pi a^2}$.  
(B) The magnetic field for $a < r < b$ is $B = \frac{\mu_0 I}{2\pi r}$.  
(C) The magnetic field for $r > b$ is zero everywhere.  
(D) The self-inductance per unit length of the cable is $\frac{L}{l} = \frac{\mu_0}{2\pi}\ln\left(\frac{b}{a}\right) + \frac{\mu_0}{8\pi}$.

#### Question 5
A uniform solid sphere of mass $M$ and radius $R$ is released from rest at the top of a rough spherical dome of radius $R_{\text{dome}} = 3 R$. The sphere rolls without slipping until it leaves the dome:
(A) Mechanical energy of the sphere is conserved during pure rolling.  
(B) Angular momentum about the contact point is conserved instantaneously.  
(C) The normal force exerted by the dome decreases as the sphere rolls down.  
(D) The sphere leaves the dome at an angle $\theta_c$ from the vertical where the normal force vanishes.

#### Question 6
Regarding the relativistic Doppler effect for light emitted by a source moving away with speed $v$ along the line of sight:
(A) The observed frequency is $\nu = \nu_0 \sqrt{\frac{1 - v/c}{1 + v/c}}$.  
(B) The observed wavelength is redshifted: $\lambda = \lambda_0 \sqrt{\frac{1 + v/c}{1 - v/c}}$.  
(C) For non-relativistic speeds $v \ll c$, $\frac{\Delta \lambda}{\lambda_0} \approx \frac{v}{c}$.  
(D) There exists a transverse Doppler shift for light emitted perpendicular to the motion ($\nu = \nu_0 \sqrt{1 - v^2/c^2}$).

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
In a Compton scattering experiment, a photon is scattered through $\theta = 180^\circ$ (backscattered). Calculate the Compton shift $\Delta \lambda$ in picometers ($\text{pm}$). (Compton wavelength $\lambda_C = 2.43\text{ pm}$. Round off to two decimal places).

#### Question 8
An ideal gas heat engine operates between $600\text{ K}$ and $300\text{ K}$. If the heat rejected to the cold reservoir per cycle is $400\text{ J}$, calculate the work done by the engine in Joules.

#### Question 9
A simple harmonic oscillator has an amplitude of $0.05\text{ m}$ and maximum velocity of $1.5\text{ m/s}$. Find its maximum acceleration in $\text{m/s}^2$.

#### Question 10
A circular coil of radius $r = 0.10\text{ m}$ has $N = 50\text{ turns}$ and carries a current $I = 2.0\text{ A}$. Calculate the magnetic field at the center of the coil in units of $10^{-4}\text{ T}$. (Take $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}, \pi \approx 3.1416$. Round off to two decimal places).

#### Question 11
Two sound waves of frequencies $300\text{ Hz}$ and $304\text{ Hz}$ are sounded together. Calculate the time interval in seconds between two successive maximum intensities. (Round off to two decimal places).

#### Question 12
A block of mass $m = 4.0\text{ kg}$ rests on a rough horizontal surface with coefficient of static friction $\mu_s = 0.40$. Find the minimum horizontal force in Newtons required to start the motion. (Take $g = 9.8\text{ m/s}^2$. Round off to two decimal places).

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the thermodynamic processes with their entropy changes:
- (P) Reversible Adiabatic -> (1) $\Delta S = 0$
- (Q) Reversible Isothermal -> (2) $\Delta S = n R \ln(V_2/V_1)$
- (R) Reversible Isochoric -> (3) $\Delta S = n C_V \ln(T_2/T_1)$
- (S) Reversible Isobaric -> (4) $\Delta S = n C_P \ln(T_2/T_1)$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 14
Match the wave phenomena with their causes:
- (P) Beats -> (1) Superposition of waves of slightly different frequencies
- (Q) Standing Waves -> (2) Superposition of two identical waves traveling in opposite directions
- (R) Doppler Effect -> (3) Relative motion between source and observer
- (S) Resonance -> (4) Driving frequency matches natural frequency
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 15
Match the central force fields with their force laws:
- (P) Gravitational force -> (1) Inverse square ($1/r^2$)
- (Q) Simple harmonic 3D -> (2) Linear attractive ($r$)
- (R) London dispersion force -> (3) Inverse seventh power ($1/r^7$)
- (S) Nuclear strong force (Yukawa) -> (4) Screened Coulomb ($\frac{e^{-\mu r}}{r^2}$)
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 16
Match the circuit laws with their conservation principles:
- (P) Kirchhoff's Current Law -> (1) Conservation of Electric Charge
- (Q) Kirchhoff's Voltage Law -> (2) Conservation of Energy
- (R) Lenz's Law -> (3) Conservation of Energy
- (S) Continuity Equation -> (4) Conservation of Charge
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 17
Match the nuclear particles with their composition:
- (P) Alpha particle -> (1) 2 protons + 2 neutrons ($^4\text{He}$ nucleus)
- (Q) Deuteron -> (2) 1 proton + 1 neutron ($^2\text{H}$ nucleus)
- (R) Triton -> (3) 1 proton + 2 neutrons ($^3\text{H}$ nucleus)
- (S) Positron -> (4) Anti-electron ($e^+$)
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 18
Match the modern physics concepts with their formulas:
- (P) Bohr orbit radius -> (1) $r_n = \frac{n^2 h^2 \varepsilon_0}{\pi m Z e^2}$
- (Q) de Broglie wavelength -> (2) $\lambda = \frac{h}{p}$
- (R) Einstein photoelectric equation -> (3) $h\nu = \Phi + K_{\max}$
- (S) Radioactive decay law -> (4) $N(t) = N_0 e^{-\lambda t}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding osmotic pressure $\Pi = i C R T$:
(A) Osmotic pressure is directly proportional to molar concentration and absolute temperature.  
(B) Reverse osmosis occurs when an external pressure exceeding $\Pi$ is applied to the solution side.  
(C) Reverse osmosis is widely used for the desalination of seawater using semipermeable cellulose acetate membranes.  
(D) Two solutions having the same osmotic pressure at the same temperature are called isotonic solutions.

#### Question 20
Regarding the crystal field stabilization energy (CFSE) of tetrahedral complexes:
(A) In tetrahedral geometry, crystal field splitting is $\Delta_t \approx \frac{4}{9}\Delta_o$.  
(B) Because $\Delta_t$ is relatively small, tetrahedral complexes are almost invariably high-spin.  
(C) The $e$ orbitals are lower in energy than the $t_2$ orbitals.  
(D) For a $d^7$ tetrahedral complex, the configuration is $e^4 t_2^3$ with 3 unpaired electrons.

#### Question 21
Regarding the reaction mechanisms of alkyl halides:
(A) Primary alkyl halides generally react via the $S_N2$ mechanism with complete Walden inversion.  
(B) Tertiary alkyl halides react via the $S_N1$ mechanism with racemization (often with slight net inversion).  
(C) $S_N2$ reactions are favored by polar aprotic solvents (such as acetone, DMF, DMSO).  
(D) $S_N1$ reactions are favored by polar protic solvents (such as water, ethanol).

#### Question 22
Regarding the structure of solid ice and water:
(A) Ice has an open cage-like three-dimensional hexagonal structure with tetrahedral coordination of oxygen.  
(B) Each water molecule in ice is hydrogen-bonded to four other water molecules.  
(C) When ice melts, some hydrogen bonds collapse and liquid water molecules pack more densely.  
(D) Water exhibits maximum density at $3.98^\circ\text{C}$ ($4^\circ\text{C}$).

#### Question 23
Which of the following compounds undergo haloform reaction with $\text{I}_2 / \text{NaOH}$?
(A) Ethanol ($\text{CH}_3\text{CH}_2\text{OH}$)  
(B) Propan-2-ol ($\text{CH}_3\text{CH(OH)CH}_3$)  
(C) Acetophenone ($\text{C}_6\text{H}_5\text{COCH}_3$)  
(D) Methanol ($\text{CH}_3\text{OH}$)

#### Question 24
Which of the following statements regarding the metallurgy of zinc is/are correct?
(A) Zinc blende ($\text{ZnS}$) is concentrated by froth floatation using sodium ethyl xanthate as collector.  
(B) Roasting of $\text{ZnS}$ converts it to $\text{ZnO}$.  
(C) $\text{ZnO}$ is reduced to zinc vapor by coke at $1400^\circ\text{C}$ in a vertical retort.  
(D) Zinc vapor is rapidly chilled to prevent re-oxidation by $\text{CO}_2$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The half-life of a first-order reaction is $30.0\text{ minutes}$. Calculate the percentage of reactant remaining after $120.0\text{ minutes}$.

#### Question 26
Calculate the equilibrium constant $K_c$ for the reaction $\text{H}_2(g) + \text{I}_2(g) \rightleftharpoons 2\text{HI}(g)$ if initially $1.0\text{ mol}$ of $\text{H}_2$ and $1.0\text{ mol}$ of $\text{I}_2$ are heated in a $1.0\text{ L}$ vessel and at equilibrium $1.6\text{ mol}$ of $\text{HI}$ is formed. (Round off to the nearest integer).

#### Question 27
Calculate the boiling point elevation $\Delta T_b$ in $^\circ\text{C}$ for a solution containing $6.0\text{ g}$ of urea ($M = 60\text{ g/mol}$) in $200\text{ g}$ of water. ($K_b = 0.52\text{ K}\cdot\text{kg/mol}$. Round off to two decimal places).

#### Question 28
In an FCC unit cell of edge length $a = 400\text{ pm}$, calculate the radius of the sphere in picometers. (Take $\sqrt{2} \approx 1.414$. Round off to two decimal places).

#### Question 29
Calculate the pH of a $0.010\text{ M}$ aqueous solution of $\text{Ba(OH)}_2$ at $25^\circ\text{C}$. (Take $\log 2 \approx 0.301$. Round off to two decimal places).

#### Question 30
The standard EMF of the cell $\text{Ni} \mid \text{Ni}^{2+} \parallel \text{Ag}^+ \mid \text{Ag}$ is $1.05\text{ V}$. Calculate the standard free energy change $\Delta G^\circ$ in $\text{kJ/mol}$. (Take $F = 96500\text{ C/mol}$. Round off to two decimal places).

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the organic reagents with their transformations:
- (P) $\text{NaBH}_4$ -> (1) Reduces aldehydes and ketones to alcohols
- (Q) $\text{LiAlH}_4$ -> (2) Strong reducing agent for acids, esters, amides
- (R) $\text{PCC}$ (Pyridinium chlorochromate) -> (3) Oxidizes primary alcohols to aldehydes selectively
- (S) $\text{KMnO}_4 / \text{H}^+$ -> (4) Strong oxidizing agent converting primary alcohols to carboxylic acids
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 32
Match the interhalogen compounds with their central atom oxidation states:
- (P) $\text{ClF}$ -> (1) $+1$
- (Q) $\text{ClF}_3$ -> (2) $+3$
- (R) $\text{BrF}_5$ -> (3) $+5$
- (S) $\text{IF}_7$ -> (4) $+7$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 33
Match the polymers with their trade names:
- (P) Polytetrafluoroethylene -> (1) Teflon
- (Q) Polyacrylonitrile -> (2) Orlon / Acrilan
- (R) Poly(methyl methacrylate) -> (3) Plexiglas / Lucite
- (S) Polyamide from caprolactam -> (4) Nylon-6
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 34
Match the metallurgy terms with their definitions:
- (P) Gangue -> (1) Earthy or rocky impurities associated with ore
- (Q) Flux -> (2) Substance added to remove gangue as slag
- (R) Slag -> (3) Fusible compound formed by gangue + flux
- (S) Matte -> (4) Molten mixture of $\text{Cu}_2\text{S}$ and $\text{FeS}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 35
Match the colloidal dispersions with their examples:
- (P) Smoke -> (1) Solid in gas (Aerosol)
- (Q) Butter -> (2) Liquid in solid (Gel)
- (R) Whipped cream -> (3) Gas in liquid (Foam)
- (S) Ruby glass -> (4) Solid in solid
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 36
Match the carbohydrates with their linkages:
- (P) Maltose -> (1) $\alpha-1,4$-glycosidic linkage
- (Q) Lactose -> (2) $\beta-1,4$-glycosidic linkage
- (R) Sucrose -> (3) $\alpha-1,\beta-2$-glycosidic linkage
- (S) Cellulose -> (4) $\beta-1,4$-glucan chain
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{\sin x}{x}$ for $x > 0$:
(A) $\lim_{x \to 0^+} f(x) = 1$.  
(B) $f'(x) = \frac{x \cos x - \sin x}{x^2} < 0$ for all $x \in (0, \pi/2)$.  
(C) $f(x)$ is strictly decreasing on $(0, \pi/2)$.  
(D) For all $x \in (0, \pi/2)$, $\frac{2}{\pi} x < \sin x < x$ (Jordan's inequality).

#### Question 38
Consider the hyperbola $\frac{x^2}{9} - \frac{y^2}{16} = 1$:
(A) The eccentricity is $e = \frac{5}{3}$.  
(B) The foci lie at $(\pm 5, 0)$.  
(C) The length of the latus rectum is $\frac{32}{3}$.  
(D) The asymptotes are $y = \pm \frac{4}{3} x$.

#### Question 39
Let $z$ be a complex number satisfying $|z - 3| = 2$:
(A) The locus of $z$ is a circle centered at $(3, 0)$ with radius $2$.  
(B) The maximum value of $|z|$ is $5$.  
(C) The minimum value of $|z|$ is $1$.  
(D) The maximum argument of $z$ satisfies $\sin(\arg_{\max}) = \frac{2}{3}$.

#### Question 40
Let $A$ be a $3 \times 3$ real symmetric matrix with eigenvalues $\lambda_1 = 2, \lambda_2 = 2, \lambda_3 = 5$:
(A) $\det(A) = 20$.  
(B) $\text{Tr}(A) = 9$.  
(C) $A$ is positive definite.  
(D) There exists an orthogonal matrix $P$ such that $P^T A P = \text{diag}(2, 2, 5)$.

#### Question 41
Let $f: [a, b] \to \mathbb{R}$ be a continuous function:
(A) Mean Value Theorem: there exists $c \in (a, b)$ such that $\int_a^b f(x) \, dx = f(c)(b - a)$.  
(B) If $f(x) \ge 0$ on $[a, b]$, then $\int_a^b f(x) \, dx \ge 0$.  
(C) $|\int_a^b f(x) \, dx| \le \int_a^b |f(x)| \, dx$.  
(D) If $\int_a^b f(x) \, dx = 0$, then $f(x)$ must have at least one root in $[a, b]$ unless $f \equiv 0$.

#### Question 42
Consider the line $\frac{x-1}{1} = \frac{y-2}{2} = \frac{z-3}{3}$ and the plane $2x + y - z = 1$:
(A) The direction vector of the line is $\vec{d} = \hat{i} + 2\hat{j} + 3\hat{k}$.  
(B) The normal vector of the plane is $\vec{n} = 2\hat{i} + \hat{j} - \hat{k}$.  
(C) $\vec{d} \cdot \vec{n} = 1(2) + 2(1) + 3(-1) = 1 \ne 0$, so the line intersects the plane.  
(D) The point of intersection is $(0, 0, 0)$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = x^3$ and the lines $y = 0, x = 1, x = 2$. (Round off to two decimal places).

#### Question 44
Evaluate the definite integral $\int_0^{\pi/2} \sin x \cos x \, dx$.

#### Question 45
Find the number of critical points of $f(x) = x^3 - 6x^2 + 9x + 5$.

#### Question 46
Let $\vec{a} = 2\hat{i} + \hat{j} - \hat{k}$ and $\vec{b} = \hat{i} + 3\hat{j} + 2\hat{k}$. Calculate the dot product $\vec{a} \cdot \vec{b}$.

#### Question 47
A box contains 5 red balls and 3 white balls. A ball is drawn at random. Find the probability (in percentage) that the drawn ball is red. (Round off to two decimal places).

#### Question 48
Find the radius of the circle $x^2 + y^2 - 8x - 10y + 16 = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\ln(\sin x)$ with respect to $x$ is:
(A) $\cot x$  
(B) $\tan x$  
(C) $-\cot x$  
(D) $\csc x$

#### Question 50
The slope of the normal to the curve $y = x^2$ at $(1, 1)$ is:
(A) $-\frac{1}{2}$  
(B) $2$  
(C) $-2$  
(D) $\frac{1}{2}$

#### Question 51
The value of $\lim_{x \to 0} \frac{1 - \cos 2x}{x^2}$ is:
(A) $2$  
(B) $1$  
(C) $4$  
(D) $\frac{1}{2}$

#### Question 52
If $A$ is a square matrix such that $A^2 = I$, then $A^{-1}$ is equal to:
(A) $A$  
(B) $-A$  
(C) $I$  
(D) $0$

#### Question 53
The number of permutations of the letters of the word 'APPLE' is:
(A) $60$  
(B) $120$  
(C) $24$  
(D) $30$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} + y = 0$ with $y(0) = 1$ is:
(A) $y = e^{-x}$  
(B) $y = e^x$  
(C) $y = -x + 1$  
(D) $y = \cos x$
"""

    sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Guwahati Benchmark JEE Advanced Mock Examination 05

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - T-S diagram of Carnot engine: $Q_H = T_H \Delta S_0$, $W = (T_H - T_C)\Delta S_0$, $\eta = 1 - T_C/T_H$.
- Q2: (A, B, C, D) - Relativistic invariant mass $s = 2 m_0 c^2(E + m_0 c^2)$. Threshold for $e^+e^-$ creation is $E_K = 6 m_0 c^2$.
- Q3: (A, B, C, D) - Conical pendulum mechanics: $T = m g / \cos\theta$, $\omega = \sqrt{g / (l\cos\theta)}$.
- Q4: (A, B, C, D) - Method of image charges for grounded infinite conducting plane.
- Q5: (A, B, C) - Fresnel biprism interference. Fringes are straight lines.
- Q6: (A, B, C, D) - Rotational spectrum of rigid diatomic rotor.
- Q7: 24.94 - $Q = n C_P \Delta T = 2 \left(\frac{5}{2}R\right)(300) = 5 R(300) = 1500(8.314) = 12471\text{ J} \approx 24.94\text{ kJ}$ if $V$ doubles $\implies \Delta T = 300\text{ K}$, $Q = 12.47\text{ kJ}$.
- Q8: 12.27 - $\lambda = \frac{1.227}{\sqrt{V}}\text{ nm} = \frac{1.227}{100}\text{ nm} = 0.01227\text{ nm} = 12.27\text{ pm}$.
- Q9: 15.71 - $I = \frac{1}{2}M R^2 = \frac{1}{2}(20)(0.25) = 2.5\text{ kg}\cdot\text{m}^2$. $\omega_0 = 600 \times 2\pi / 60 = 20\pi\text{ rad/s}$. $\tau = I \alpha \implies \alpha = 50 / 2.5 = 20\text{ rad/s}^2$. $t = \omega_0 / \alpha = 20\pi / 20 = \pi \approx 3.14\text{ s}$.
- Q10: 5.03 - $L = \frac{\mu_0 N^2 A}{l} = \frac{4\pi \times 10^{-7} \times 10^6 \times 2 \times 10^{-3}}{0.50} = 5.03 \times 10^{-3}\text{ H} = 5.03\text{ mH}$.
- Q11: 1.25 - $\beta = \frac{\lambda D}{d} = \frac{500 \times 10^{-9} \times 1.0}{0.40 \times 10^{-3}} = 1.25 \times 10^{-3}\text{ m} = 1.25\text{ mm}$.
- Q12: 5.00 - $\Delta h_{Hg} = \frac{h_w \rho_w}{2 \rho_{Hg}} = \frac{13.6 \times 1}{2 \times 13.6} = 0.5\text{ cm} = 5.00\text{ mm}$.
- Q13: (A) - Laplace-Runge-Lenz vector is conserved for $1/r$ gravitational/Coulomb potentials.
- Q14: (A) - $C = 4\pi\varepsilon_0 R = \frac{0.09}{9 \times 10^9} = 10^{-11}\text{ F} = 10\text{ pF}$.
- Q15: (A) - Brewster's angle: $\tan\theta_B = \sqrt{3} \implies \theta_B = 60^\circ$.
- Q16: (A) - $T_2 / T_1 = (V_1/V_2)^{\gamma-1} = (1/3)^{0.4} \approx 0.64$.
- Q17: (A) - $R = \frac{m v}{q B} = \frac{1.67 \times 10^{-27} \times 2 \times 10^6}{1.6 \times 10^{-19} \times 0.5} = 4.175 \times 10^{-2}\text{ m} = 4.18\text{ cm}$.
- Q18: (A) - Mean life $\tau = 1/\lambda = 1/0.05 = 20\text{ days}$.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Solubility product and common ion effect for $A_2 B$.
- Q20: (A, B, C, D) - Lineweaver-Burk enzyme kinetics.
- Q21: (A, B, C, D) - Carbonyl and nitrosyl complex bonding.
- Q22: (A, B, C, D) - Aldol condensation mechanisms.
- Q23: (A, B, C, D) - Halogens and pseudohalogens chemistry.
- Q24: (A, B, C) - Carboxylic acids and picric acid are more acidic than carbonic acid, while phenol is weaker.
- Q25: 55.33 - $E_a = \frac{R T_1 T_2}{T_2 - T_1}\ln\frac{k_2}{k_1} = \frac{8.314 \times 96000}{20}(1.3863) = 55.33\text{ kJ/mol}$.
- Q26: 7.07 - $s = \sqrt{K_{sp}} = \sqrt{5.0 \times 10^{-13}} = \sqrt{50} \times 10^{-7} \approx 7.07 \times 10^{-7}\text{ M}$.
- Q27: -0.380 - $\Delta T_f = i K_f m = [1 + 0.02](1.86)(0.20) = 1.02 \times 0.372 = 0.379^\circ\text{C} \implies T_f = -0.379^\circ\text{C}$.
- Q28: 68.02 - BCC packing fraction $\frac{\sqrt{3}\pi}{8} \approx 68.02\%$.
- Q29: 9.26 - $\text{pOH} = \text{p}K_b + \log\frac{[\text{salt}]}{[\text{base}]} = 4.74 + 0 = 4.74 \implies \text{pH} = 14 - 4.74 = 9.26$.
- Q30: 6.00 - $\text{C}_6\text{H}_5\text{NO}_2 + 6\text{H}^+ + 6e^- \to \text{C}_6\text{H}_5\text{NH}_2 + 2\text{H}_2\text{O}$.
- Q31: (A) - Tertiary halide gives predominantly elimination (E2) with strong base.
- Q32: (A) - $\text{O}_2^{2-}$ has all electrons paired in molecular orbitals.
- Q33: (A) - Thermal stability of alkali hydrides decreases down group as lattice energy decreases.
- Q34: (A) - MacArthur-Forrest cyanide extraction of gold forms $[\text{Au}(\text{CN})_2]^-$.
- Q35: (A) - Glycine has no chiral carbon ($\text{H}_2\text{N-CH}_2\text{-COOH}$).
- Q36: (A) - Hofmann degradation proceeds via isocyanate intermediate.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Function $x e^{-x}$ analysis.
- Q38: (A, B, C, D) - Standard ellipse geometry.
- Q39: (A, B, C, D) - Complex locus $\text{Re}(\frac{z-1}{z+1}) = 0 \implies |z| = 1$.
- Q40: (A, B, C, D) - Cube root of identity matrix.
- Q41: (A, B, C, D) - Wallis cosine reduction formula.
- Q42: (A, B, C, D) - Line of intersection of two planes.
- Q43: 10.67 - $\int_{-2}^2 (4 - x^2) dx = [4x - x^3/3]_{-2}^2 = 2(8 - 8/3) = 32/3 \approx 10.67$.
- Q44: 110 - $K = \int_0^1 x (1-x)^9 dx = B(2, 10) = \frac{\Gamma(2)\Gamma(10)}{\Gamma(12)} = \frac{1! \times 9!}{11!} = \frac{1}{110} \implies N = 110$.
- Q45: 3 - $f'(x) = 4x^3 - 12x^2 + 8x = 4x(x - 1)(x - 2) = 0 \implies x = 0, 1, 2$ (3 points).
- Q46: 0.00 - $(\vec{a} \times \vec{b}) \cdot \vec{a} = 0$ by orthogonality.
- Q47: 75.00 - $P = 1 - (1 - 1/2)(1 - 1/3)(1 - 1/4) = 1 - (1/2 \times 2/3 \times 3/4) = 1 - 1/4 = 3/4 = 75.00\%$.
- Q48: 5.00 - Center $(1, 2)$, $R = \sqrt{1 + 4 - (-20)} = \sqrt{25} = 5.00$.
- Q49: (A) - Substitution $x = \tan\theta \implies \frac{\sec\theta - 1}{\tan\theta} = \tan(\theta/2) \implies y = \theta/2 = \frac{1}{2}\arctan x \implies y' = \frac{1}{2(1+x^2)}$.
- Q50: (A) - Focal chord length formula $4a \csc^2\theta$.
- Q51: (A) - Limit $= 2/3$.
- Q52: (A) - $\det(2 A B) = 2^3 \det(A)\det(B) = 8 \times 2 \times 3 = 48$.
- Q53: (A) - Each of 4 letters has 3 choices $\implies 3^4 = 81$.
- Q54: (A) - Separable ODE $\frac{dy}{y} = 2x dx \implies \ln y = x^2 + c \implies y = C e^{x^2}$.
"""

    sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Guwahati Benchmark JEE Advanced Mock Examination 05

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Joule-Thomson isenthalpic expansion.
- Q2: (A, B, C, D) - Bohr hydrogen-like scaling laws.
- Q3: (A, B, C, D) - Spherical refracting surface formulas.
- Q4: (A, B, C, D) - Coaxial cable inductance and magnetic field.
- Q5: (A, B, C, D) - Rolling sphere off spherical dome.
- Q6: (A, B, C, D) - Relativistic longitudinal and transverse Doppler effect.
- Q7: 4.86 - $\Delta \lambda = \lambda_C(1 - \cos 180^\circ) = 2 \lambda_C = 2(2.43) = 4.86\text{ pm}$.
- Q8: 400.00 - $\eta = 1 - 300/600 = 0.50 \implies W = Q_C = 400\text{ J}$.
- Q9: 45.00 - $v_{\max} = \omega A \implies \omega = 1.5 / 0.05 = 30\text{ rad/s}$. $a_{\max} = \omega^2 A = 900(0.05) = 45.00\text{ m/s}^2$.
- Q10: 6.28 - $B = \frac{\mu_0 N I}{2 r} = \frac{4\pi \times 10^{-7} \times 50 \times 2.0}{2(0.10)} = 2\pi \times 10^{-4} \approx 6.28 \times 10^{-4}\text{ T}$.
- Q11: 0.25 - Beat frequency $f_b = 304 - 300 = 4\text{ Hz} \implies T_b = 1/4 = 0.25\text{ s}$.
- Q12: 15.68 - $f_s = \mu_s m g = 0.40(4.0)(9.8) = 15.68\text{ N}$.
- Q13: (A) - Entropy formulas for ideal gas processes.
- Q14: (A) - Wave phenomena.
- Q15: (A) - Force laws.
- Q16: (A) - Conservation laws in electromagnetism.
- Q17: (A) - Nuclear particles composition.
- Q18: (A) - Modern physics laws.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Osmotic pressure and reverse osmosis.
- Q20: (A, B, C, D) - Tetrahedral crystal field splitting.
- Q21: (A, B, C, D) - $S_N1$ vs $S_N2$ solvent and substrate dependence.
- Q22: (A, B, C, D) - Hydrogen bonding in ice and water anomaly.
- Q23: (A, B, C) - Haloform reaction criteria (methyl carbonyl or methyl carbinol). Methanol lacks this structure.
- Q24: (A, B, C, D) - Extraction of zinc.
- Q25: 6.25 - $120\text{ min} = 4$ half-lives $\implies (1/2)^4 = 1/16 = 6.25\%$.
- Q26: 64 - $K_c = \frac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]} = \frac{(1.6)^2}{(0.2)(0.2)} = \frac{2.56}{0.04} = 64$.
- Q27: 0.26 - $m = \frac{6/60}{0.200} = 0.50\text{ m} \implies \Delta T_b = 0.52(0.50) = 0.26^\circ\text{C}$.
- Q28: 141.42 - In FCC, $4r = \sqrt{2}a \implies r = \frac{\sqrt{2}(400)}{4} = 100\sqrt{2} \approx 141.42\text{ pm}$.
- Q29: 12.30 - $\text{Ba(OH)}_2 \to \text{Ba}^{2+} + 2\text{OH}^- \implies [\text{OH}^-] = 0.020\text{ M} \implies \text{pOH} = 2 - \log 2 = 1.70 \implies \text{pH} = 12.30$.
- Q30: 202.65 - $\Delta G^\circ = -n F E^\circ = -2(96500)(1.05) = -202650\text{ J} = -202.65\text{ kJ/mol}$.
- Q31: (A) - Organic reagents functions.
- Q32: (A) - Interhalogen oxidation states.
- Q33: (A) - Commercial polymer names.
- Q34: (A) - Metallurgy definitions.
- Q35: (A) - Colloidal states.
- Q36: (A) - Glycosidic bonds in sugars.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Analysis of $\frac{\sin x}{x}$ and Jordan's inequality.
- Q38: (A, B, C, D) - Hyperbola properties.
- Q39: (A, B, C, D) - Circle in complex plane.
- Q40: (A, B, C, D) - Symmetric matrix diagonalization.
- Q41: (A, B, C, D) - Integral mean value theorem and properties.
- Q42: (A, B, C) - Intersection of line and plane.
- Q43: 3.75 - $\int_1^2 x^3 dx = [\frac{x^4}{4}]_1^2 = 4 - 1/4 = 3.75$.
- Q44: 0.50 - $\int_0^{\pi/2} \sin x \cos x dx = [\frac{\sin^2 x}{2}]_0^{\pi/2} = 0.50$.
- Q45: 2 - $f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3) = 0 \implies x = 1, 3$ (2 points).
- Q46: 3.00 - $\vec{a}\cdot\vec{b} = 2(1) + 1(3) + (-1)(2) = 2 + 3 - 2 = 3.00$.
- Q47: 62.50 - $5/8 = 0.625 = 62.50\%$.
- Q48: 5.00 - Center $(4, 5)$, $R = \sqrt{16 + 25 - 16} = 5.00$.
- Q49: (A) - $\frac{d}{dx}\ln(\sin x) = \frac{\cos x}{\sin x} = \cot x$.
- Q50: (A) - $y' = 2x = 2$ at $(1, 1) \implies m_{\text{norm}} = -1/2$.
- Q51: (A) - $\lim_{x\to 0}\frac{2\sin^2 x}{x^2} = 2$.
- Q52: (A) - $A^2 = I \implies A A = I \implies A^{-1} = A$.
- Q53: (A) - $5! / 2! = 120 / 2 = 60$.
- Q54: (A) - $y = e^{-x}$.
"""

    val = r"""# Answer Key & Benchmark Alignment – Mock Examination 05
## Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C; Q6: A,B,C,D; Q7: 12.47; Q8: 12.27; Q9: 3.14; Q10: 5.03; Q11: 1.25; Q12: 5.00; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C; Q25: 55.33; Q26: 7.07; Q27: -0.379; Q28: 68.02; Q29: 9.26; Q30: 6.00; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 10.67; Q44: 110.00; Q45: 3.00; Q46: 0.00; Q47: 75.00; Q48: 5.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 4.86; Q8: 400.00; Q9: 45.00; Q10: 6.28; Q11: 0.25; Q12: 15.68; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B,C; Q24: A,B,C,D; Q25: 6.25; Q26: 64.00; Q27: 0.26; Q28: 141.42; Q29: 12.30; Q30: 202.65; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C; Q43: 3.75; Q44: 0.50; Q45: 2.00; Q46: 3.00; Q47: 62.50; Q48: 5.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""
    create_mock_files(5, p1, p2, sol1, sol2, val, iit_name="IIT_Guwahati")
    print("Generated IIT Guwahati Mock 05!")

if __name__ == "__main__":
    generate_guwahati_05()

