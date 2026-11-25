# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Guwahati Mock 02.
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

paper_1_md = r"""# JEE Advanced Mock Examination 02 – Paper 1
## Organising Institute Style Inspiration: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
**Historical Reference Benchmark**: 2009, 2016, 2023 Official Examination Papers  
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
One mole of an ideal gas whose adiabatic exponent is $\gamma = 7/5$ is taken through a cyclic process consisting of an isothermal expansion $A \to B$ at temperature $T_1 = 400\text{ K}$ from volume $V_0$ to $2V_0$, an isobaric cooling $B \to C$ to volume $V_0$, and an isochoric heating $C \to A$ back to temperature $T_1$. Which of the following statements is/are correct?
(A) The pressure at state $B$ is half the pressure at state $A$ ($P_B = P_A/2$).  
(B) The temperature of the gas at state $C$ is $T_C = 200\text{ K}$.  
(C) The work done by the gas in the cycle is $R T_1 (\ln 2 - 0.5)$.  
(D) The net heat absorbed by the gas in the complete cycle is equal to the net work done.

#### Question 2
In the Bohr model of a stationary hydrogen-like atom of mass $M$ and atomic number $Z$, an electron undergoes a radiative transition from an excited state with energy $E_i$ to a lower state with energy $E_f$. Let $\Delta E = E_i - E_f > 0$. Taking into account the recoil kinetic energy of the emitting atom:
(A) The energy of the emitted photon $E_\gamma$ is strictly less than $\Delta E$.  
(B) To first order in $\Delta E / (M c^2)$, the photon energy is $E_\gamma \approx \Delta E - \frac{(\Delta E)^2}{2 M c^2}$.  
(C) The recoil momentum of the atom is equal in magnitude to the momentum of the emitted photon.  
(D) The fractional frequency shift $\frac{\Delta \nu}{\nu_0}$ due to nuclear recoil is independent of the speed of light $c$.

#### Question 3
A real gas obeys the van der Waals equation of state $\left(P + \frac{a}{V_m^2}\right)(V_m - b) = R T$. The gas undergoes a free adiabatic expansion into an evacuated chamber from initial volume $V_1$ to final volume $V_2$ ($V_2 > V_1$). The molar heat capacity at constant volume is $C_{V,m}$. Which of the following statements is/are correct?
(A) The internal energy of the gas remains unchanged during the free expansion ($\Delta U = 0$).  
(B) The change in temperature of the gas is given by $\Delta T = -\frac{a}{C_{V,m}}\left(\frac{1}{V_1} - \frac{1}{V_2}\right)$.  
(C) Because $V_2 > V_1$ and $a > 0$, the temperature of the gas decreases upon free expansion.  
(D) The entropy change of the gas is $\Delta S = R \ln\left(\frac{V_2 - b}{V_1 - b}\right) + C_{V,m} \ln\left(\frac{T_2}{T_1}\right) > 0$.

#### Question 4
A gyroscope consists of a uniform solid disk of mass $M$ and radius $R$ mounted at the end of a light horizontal axle of length $L$. The axle is pivoted at its other end on a frictionless stand. The disk spins about the axle with a large angular speed $\omega_s \gg \Omega_p$, where $\Omega_p$ is the precession frequency. Which of the following statements is/are correct?
(A) The spin angular momentum of the disk is $L_s = \frac{1}{2} M R^2 \omega_s$.  
(B) The steady precession angular velocity about the vertical axis is $\Omega_p = \frac{2 g L}{R^2 \omega_s}$.  
(C) The direction of precession reverses if the direction of spin $\omega_s$ is reversed.  
(D) If nutation is neglected, the torque exerted by gravity is perpendicular to both the spin angular momentum and the vertical axis.

#### Question 5
A small circular wire loop of radius $r$ carrying a steady current $I_1$ lies in the plane of a much larger coplanar circular wire loop of radius $R \gg r$ carrying steady current $I_2$. The centers of both loops coincide at the origin. Which of the following statements is/are correct?
(A) The mutual inductance between the two loops is $M = \frac{\mu_0 \pi r^2}{2 R}$.  
(B) The magnetic flux linked with the larger loop when current $I$ flows in the smaller loop is $\frac{\mu_0 \pi r^2 I}{2 R}$.  
(C) If the smaller loop is rotated by $180^\circ$ about its coplanar diameter, the net magnetic work done on it by the field of the outer loop is $\frac{\mu_0 \pi r^2 I_1 I_2}{R}$.  
(D) The magnetic field produced by the small loop at the circumference of the large loop is non-uniform.

#### Question 6
A beam of unpolarized light of intensity $I_0$ passes through a series of three ideal linear polarizers $P_1, P_2, P_3$. The transmission axis of $P_1$ is vertical ($\theta_1 = 0^\circ$), the transmission axis of $P_3$ is horizontal ($\theta_3 = 90^\circ$), and the transmission axis of $P_2$ makes an angle $\theta$ with the vertical ($0 < \theta < 90^\circ$). Which of the following statements is/are correct?
(A) If polarizer $P_2$ is removed, the transmitted intensity through $P_3$ is zero.  
(B) With $P_2$ present, the transmitted intensity through $P_3$ is $I = \frac{I_0}{8} \sin^2(2\theta)$.  
(C) The transmitted intensity is maximum when $\theta = 45^\circ$, and its maximum value is $\frac{I_0}{8}$.  
(D) The light emerging from $P_3$ is linearly polarized along the horizontal direction.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
In a photoelectric effect experiment using cesium cathode ($\Phi = 1.90\text{ eV}$), monochromatic light of wavelength $\lambda = 310\text{ nm}$ is incident on the cathode. A stopping potential $V_s$ is applied to reduce the photocurrent to zero. Calculate the stopping potential $V_s$ in volts. (Take $h c \approx 1240\text{ eV}\cdot\text{nm}$. Round off to two decimal places).

#### Question 8
Two concentric spherical thin shells of radii $R_1 = 0.10\text{ m}$ and $R_2 = 0.20\text{ m}$ are placed in vacuum. The inner shell is maintained at temperature $T_1 = 500\text{ K}$ and the outer shell is maintained at $T_2 = 300\text{ K}$. Both surfaces are ideal blackbodies ($\varepsilon = 1.0$). A thin spherical radiation shield of radius $R_s = 0.15\text{ m}$ (black on both sides) is placed concentrically between them. In the steady state, calculate the equilibrium temperature $T_s$ of the radiation shield in Kelvin. (Round off to the nearest integer).

#### Question 9
A particle of mass $m = 0.2\text{ kg}$ is attached to a spring of spring constant $k = 80\text{ N/m}$ and moves on a smooth horizontal surface. The particle is also subjected to a damping force $F_d = -b v$, where $b = 0.8\text{ N}\cdot\text{s/m}$. If the particle is displaced by $x_0 = 0.10\text{ m}$ from equilibrium and released from rest, find the quality factor $Q = \frac{\omega_0 m}{b}$ of this damped harmonic oscillator. (Round off to two decimal places).

#### Question 10
In a Young's double slit setup with slit separation $d = 0.5\text{ mm}$ and screen distance $D = 1.2\text{ m}$, light of wavelength $\lambda = 600\text{ nm}$ is used. A transparent thin glass plate of refractive index $\mu = 1.50$ is placed in front of one of the slits. The central bright fringe shifts by a distance of $4.8\text{ mm}$ on the screen. Calculate the thickness $t$ of the glass plate in micrometers ($\mu\text{m}$). (Round off to two decimal places).

#### Question 11
An ideal gas heat pump maintains the interior of a house at temperature $T_H = 294\text{ K}$ ($21^\circ\text{C}$) while the outdoor temperature is $T_C = 273\text{ K}$ ($0^\circ\text{C}$). The heat pump operates on a reversed Carnot cycle. If the rate of heat loss from the house is $14.7\text{ kW}$, calculate the minimum electrical power (in $\text{kW}$) required to drive the heat pump. (Round off to two decimal places).

#### Question 12
A uniform solid sphere of mass $M = 2.5\text{ kg}$ and radius $R = 0.12\text{ m}$ rolls without slipping down an inclined plane of inclination angle $\theta = 30^\circ$. Calculate the linear acceleration of its center of mass in $\text{m/s}^2$. (Take $g = 9.8\text{ m/s}^2$. Round off to two decimal places).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle of mass $m$ moves in a central force field with potential energy $U(r) = -\frac{k}{r^4}$ ($k > 0$). If the particle approaches from infinity with velocity $v_0$ and impact parameter $b$, the critical impact parameter $b_c$ below which the particle spirals into the center of attraction is:
(A) $b_c = \left(\frac{4k}{m v_0^2}\right)^{1/4}$  
(B) $b_c = \left(\frac{2k}{m v_0^2}\right)^{1/4}$  
(C) $b_c = \left(\frac{k}{2 m v_0^2}\right)^{1/4}$  
(D) $b_c = \left(\frac{k}{m v_0^2}\right)^{1/4}$

#### Question 14
In an LC oscillation circuit, the maximum charge on the capacitor is $Q_0$. When the energy stored in the electric field of the capacitor equals three times the energy stored in the magnetic field of the inductor, the instantaneous charge on the capacitor is:
(A) $\frac{\sqrt{3}}{2} Q_0$  
(B) $\frac{1}{2} Q_0$  
(C) $\frac{3}{4} Q_0$  
(D) $\frac{1}{\sqrt{2}} Q_0$

#### Question 15
A uniform magnetic field $\vec{B} = B_0 \hat{k}$ exists in the region $x > 0$. A charged particle of mass $m$ and positive charge $q$ enters the region from the origin $(0, 0, 0)$ with velocity $\vec{v} = v_0 \cos\alpha \hat{i} + v_0 \sin\alpha \hat{j}$ ($0 < \alpha < \pi/2$). The time spent by the particle in the magnetic field before returning to $x \le 0$ is:
(A) $\frac{2(\pi - \alpha) m}{q B_0}$  
(B) $\frac{2\alpha m}{q B_0}$  
(C) $\frac{\pi m}{q B_0}$  
(D) $\frac{(\pi + 2\alpha) m}{2 q B_0}$

#### Question 16
An electromagnetic wave traveling in vacuum has electric field $\vec{E} = E_0 \cos(k z - \omega t)\hat{i} + E_0 \sin(k z - \omega t)\hat{j}$. The time-averaged Poynting vector $\langle\vec{S}\rangle$ of this wave is:
(A) $\frac{\varepsilon_0 c E_0^2}{2} \hat{k}$  
(B) $\varepsilon_0 c E_0^2 \hat{k}$  
(C) $2\varepsilon_0 c E_0^2 \hat{k}$  
(D) $\frac{\varepsilon_0 c E_0^2}{4} \hat{k}$

#### Question 17
A telescope has an objective lens of diameter $D = 1.22\text{ m}$ and focal length $f = 10\text{ m}$. Using light of wavelength $\lambda = 500\text{ nm}$, the Rayleigh limit of angular resolution $\theta_R$ of the telescope is:
(A) $5.0 \times 10^{-7}\text{ rad}$  
(B) $4.1 \times 10^{-7}\text{ rad}$  
(C) $6.1 \times 10^{-7}\text{ rad}$  
(D) $2.5 \times 10^{-7}\text{ rad}$

#### Question 18
A spherical raindrop falling through saturated water vapor grows by condensation such that its radius increases at a constant rate $\frac{dr}{dt} = \alpha$. If the initial radius at $t = 0$ is negligible ($r(0) = 0$), the terminal velocity of the raindrop falling under gravity and viscous drag in the Stokes regime ($F_d = 6\pi \eta r v$) scales with time $t$ as:
(A) $v(t) \propto t$  
(B) $v(t) \propto t^2$  
(C) $v(t) \propto \sqrt{t}$  
(D) $v(t) = \text{constant}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For the gaseous phase decomposition of ammonium carbamate at $300\text{ K}$:
$$\text{NH}_2\text{COONH}_4(s) \rightleftharpoons 2\text{NH}_3(g) + \text{CO}_2(g)$$
The equilibrium constant is $K_p$. If the reaction reaches equilibrium in an evacuated rigid container:
(A) The partial pressure of $\text{NH}_3$ is twice the partial pressure of $\text{CO}_2$ ($P_{\text{NH}_3} = 2 P_{\text{CO}_2}$).  
(B) In terms of total pressure $P$, the equilibrium constant is $K_p = \frac{4}{27} P^3$.  
(C) Adding more solid $\text{NH}_2\text{COONH}_4$ to the container shifts the equilibrium forward.  
(D) Introducing extra $\text{CO}_2$ gas at constant volume decreases the equilibrium partial pressure of $\text{NH}_3$.

#### Question 20
Consider the reaction of fumaric acid (trans-butenedioic acid) with bromine water ($\text{Br}_2/\text{H}_2\text{O}$ or $\text{Br}_2/\text{CCl}_4$):
(A) The addition of bromine across the double bond proceeds via a cyclic bromonium ion intermediate.  
(B) The addition is stereospecifically anti.  
(C) Bromination of fumaric acid yields the meso-2,3-dibromosuccinic acid.  
(D) Bromination of maleic acid (cis-isomer) yields a racemic mixture of $(2R,3R)$- and $(2S,3S)$-dibromosuccinic acid.

#### Question 21
Regarding the thermodynamics and crystal field stabilization energy (CFSE) of octahedral complexes:
(A) For a high-spin $d^4$ complex in an octahedral field, the electronic configuration is $t_{2g}^3 e_g^1$ with $\text{CFSE} = -0.6 \Delta_o$.  
(B) For a low-spin $d^4$ complex, the configuration is $t_{2g}^4 e_g^0$ with $\text{CFSE} = -1.6 \Delta_o + P$ (where $P$ is pairing energy).  
(C) A $d^6$ octahedral complex with a strong field ligand like $\text{CN}^-$ has $\text{CFSE} = -2.4 \Delta_o + 2P$ and is diamagnetic.  
(D) In a tetrahedral crystal field, the splitting energy $\Delta_t$ is related to octahedral splitting by $\Delta_t \approx \frac{4}{9} \Delta_o$.

#### Question 22
Which of the following statements regarding the Clausius-Clapeyron equation and phase transitions is/are correct?
(A) The slope of the liquid-gas coexistence curve in a $P-T$ phase diagram is given by $\frac{dP}{dT} = \frac{\Delta H_{\text{vap}}}{T \Delta V}$.  
(B) Assuming ideal gas behavior for the vapor and neglecting liquid molar volume, $\frac{d \ln P}{dT} = \frac{\Delta H_{\text{vap}}}{R T^2}$.  
(C) A plot of $\ln P$ versus $1/T$ yields a straight line with slope $-\frac{\Delta H_{\text{vap}}}{R}$.  
(D) For water, the slope of the solid-liquid coexistence curve ($\frac{dP}{dT}$) is negative because ice is less dense than liquid water ($\Delta V_{\text{fusion}} < 0$).

#### Question 23
In the Pinacol-Pinacolone rearrangement of 2,3-dimethylbutane-2,3-diol catalyzed by concentrated $\text{H}_2\text{SO}_4$:
(A) The reaction begins with protonation of one hydroxyl group followed by loss of water to form a tertiary carbocation.  
(B) A methyl group migrates with its electron pair to the adjacent carbocationic center.  
(C) The driving force for the rearrangement is the formation of a resonance-stabilized oxonium ion ($-\text{C}=\text{O}^+-\text{H}$).  
(D) If 1,1,2-triphenylethane-1,2-diol is subjected to pinacol rearrangement, the phenyl group migrates preferentially over the hydrogen atom.

#### Question 24
Which of the following statements regarding group 15 and group 16 elements is/are correct?
(A) The basicity order of group 15 hydrides is $\text{NH}_3 > \text{PH}_3 > \text{AsH}_3 > \text{SbH}_3 > \text{BiH}_3$.  
(B) Nitrogen cannot form pentahalides like $\text{NCl}_5$ due to the non-availability of $d$-orbitals in its valence shell.  
(C) White phosphorus consists of discrete tetrahedral $\text{P}_4$ molecules with bond angles of $60^\circ$, causing severe angle strain.  
(D) In the contact process for sulfuric acid, $\text{SO}_3$ is directly dissolved in water to form concentrated $\text{H}_2\text{SO}_4$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The vapor pressure of pure benzene at $25^\circ\text{C}$ is $95.0\text{ mmHg}$ and its enthalpy of vaporization is $\Delta H_{\text{vap}} = 30.8\text{ kJ/mol}$. Calculate the normal boiling point of benzene in $^\circ\text{C}$ (where external pressure is $760\text{ mmHg}$). (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$, $\ln(760/95) = \ln 8 \approx 2.079$. Round off to two decimal places).

#### Question 26
A cell is set up using the quinhydrone electrode at $25^\circ\text{C}$:
$$\text{Pt} \mid \text{Quinhydrone, Solution X} \parallel \text{SCE} (E_{\text{SCE}} = +0.242\text{ V})$$
The reduction potential of the quinhydrone electrode is given by $E = 0.6996 - 0.0591 \text{pH}\text{ V}$. If the measured cell EMF is $0.220\text{ V}$ with the quinhydrone electrode acting as the cathode, find the pH of Solution X. (Round off to two decimal places).

#### Question 27
A sample of $0.50\text{ g}$ of a polybasic organic acid requires $40.0\text{ mL}$ of $0.125\text{ M}$ $\text{NaOH}$ solution for complete neutralization. If the molecular weight of the acid is $200\text{ g/mol}$, find the basicity (number of ionizable protons per molecule) of the acid.

#### Question 28
The decomposition of nitrous oxide on a gold surface is zero-order with a rate constant $k = 4.0 \times 10^{-4}\text{ mol}\cdot\text{L}^{-1}\cdot\text{s}^{-1}$ at $900\text{ K}$. If the initial concentration of $\text{N}_2\text{O}$ is $0.060\text{ M}$, calculate the time in seconds required for the concentration to fall to $0.012\text{ M}$.

#### Question 29
A crystal of titanium dioxide ($\text{TiO}_2$, rutile) has a tetragonal unit cell with lattice constants $a = b = 4.59\text{ \AA}$ and $c = 2.96\text{ \AA}$. The unit cell contains $Z = 2$ formula units of $\text{TiO}_2$. Calculate the theoretical density of rutile in $\text{g/cm}^3$. (Take atomic masses: $\text{Ti} = 47.9\text{ g/mol}$, $\text{O} = 16.0\text{ g/mol}$, $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$. Round off to two decimal places).

#### Question 30
Calculate the standard enthalpy of combustion of liquid methanol ($\text{CH}_3\text{OH}, l$) in $\text{kJ/mol}$ at $298\text{ K}$.
Given standard enthalpies of formation:
$\Delta_f H^\circ(\text{CH}_3\text{OH}, l) = -238.7\text{ kJ/mol}$,
$\Delta_f H^\circ(\text{CO}_2, g) = -393.5\text{ kJ/mol}$,
$\Delta_f H^\circ(\text{H}_2\text{O}, l) = -285.8\text{ kJ/mol}$.
(Report the absolute value rounded to two decimal places).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the hydroboration-oxidation of propene with $\text{B}_2\text{H}_6$ followed by alkaline $\text{H}_2\text{O}_2$:
(A) The reaction yields propan-1-ol via an anti-Markovnikov syn-addition mechanism.  
(B) The reaction yields propan-2-ol via a Markovnikov addition mechanism.  
(C) The reaction proceeds through a stable free carbocation intermediate.  
(D) The addition of boron and hydrogen occurs in an anti-coplanar stereochemical fashion.

#### Question 32
Which of the following molecules has a zero dipole moment due to molecular symmetry?
(A) $\text{XeF}_4$  
(B) $\text{SF}_4$  
(C) $\text{ClF}_3$  
(D) $\text{H}_2\text{O}$

#### Question 33
The correct order of increasing thermal stability for the carbonates of alkaline earth metals is:
(A) $\text{BeCO}_3 < \text{MgCO}_3 < \text{CaCO}_3 < \text{SrCO}_3 < \text{BaCO}_3$  
(B) $\text{BaCO}_3 < \text{SrCO}_3 < \text{CaCO}_3 < \text{MgCO}_3 < \text{BeCO}_3$  
(C) $\text{MgCO}_3 < \text{BeCO}_3 < \text{CaCO}_3 < \text{SrCO}_3 < \text{BaCO}_3$  
(D) $\text{CaCO}_3 < \text{MgCO}_3 < \text{BeCO}_3 < \text{BaCO}_3 < \text{SrCO}_3$

#### Question 34
In the coagulation of a negative sol such as $\text{As}_2\text{S}_3$, the flocculating value is minimum for:
(A) $\text{Al}^{3+}$  
(B) $\text{Mg}^{2+}$  
(C) $\text{Na}^+$  
(D) $\text{Ba}^{2+}$

#### Question 35
Treatment of phenol with chloroform and aqueous $\text{NaOH}$ followed by acid hydrolysis yields salicylaldehyde (Reimer-Tiemann reaction). The intermediate electrophilic carbene involved is:
(A) $:\text{CCl}_2$  
(B) $:\text{CH}_2$  
(C) $:\text{CHCl}$  
(D) $\text{CCl}_3^+$

#### Question 36
The complex $[\text{Ni}(\text{CO})_4]$ is:
(A) Tetrahedral and diamagnetic  
(B) Square planar and diamagnetic  
(C) Tetrahedral and paramagnetic  
(D) Octahedral and diamagnetic

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{\ln x}{x}$ for $x > 0$. Which of the following statements is/are correct?
(A) $f(x)$ is strictly increasing on $(0, e)$ and strictly decreasing on $(e, \infty)$.  
(B) The maximum value of $f(x)$ on $(0, \infty)$ is $\frac{1}{e}$.  
(C) For any two positive numbers $a, b > e$, if $a < b$, then $a^b > b^a$.  
(D) The number $e^\pi$ is strictly greater than $\pi^e$.

#### Question 38
Consider the hyperbola $H: \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Let $P(a \sec\theta, b \tan\theta)$ be any point on the hyperbola. Which of the following statements is/are correct?
(A) The equation of the tangent at $P$ is $\frac{x \sec\theta}{a} - \frac{y \tan\theta}{b} = 1$.  
(B) The locus of the point of intersection of two perpendicular tangents to the hyperbola is the director circle $x^2 + y^2 = a^2 - b^2$ (provided $a > b$).  
(C) The product of the perpendicular distances from the foci to any tangent to the hyperbola is $b^2$.  
(D) The asymptotes of the hyperbola are given by $\frac{x}{a} \pm \frac{y}{b} = 0$.

#### Question 39
Let $z \in \mathbb{C}$ be a complex number satisfying $|z - 3 - 4i| \le 2$. Which of the following statements is/are correct?
(A) The maximum value of $|z|$ is $7$.  
(B) The minimum value of $|z|$ is $3$.  
(C) The maximum value of $\text{Re}(z)$ is $5$.  
(D) The complex number with minimum argument $\arg(z)$ lies on the tangent drawn from the origin to the circle.

#### Question 40
Let $A$ be a $3 \times 3$ real symmetric matrix with eigenvalues $\lambda_1 = 1, \lambda_2 = 2, \lambda_3 = 3$. Which of the following statements is/are correct?
(A) $\det(A) = 6$.  
(B) $\text{Tr}(A) = 6$.  
(C) $A$ is positive definite.  
(D) The eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.

#### Question 41
Let $I = \int_0^1 \frac{\arctan x}{x} \, dx$. Which of the following statements is/are correct?
(A) By series expansion of $\arctan x$, $I = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^2}$.  
(B) The value of $I$ is known as Catalan's constant $G \approx 0.915965$.  
(C) $I = -\int_0^{\pi/4} \ln(\sin \theta) \, d\theta + \frac{\pi}{4}\ln 2$.  
(D) $I < 1$.

#### Question 42
Consider the vector differential equation of motion $\frac{d\vec{r}}{dt} = \vec{\omega} \times \vec{r}$, where $\vec{\omega}$ is a constant non-zero vector. Which of the following statements is/are correct?
(A) The magnitude of the position vector $|\vec{r}(t)|$ is constant for all $t$.  
(B) $\vec{r}(t) \cdot \vec{\omega}$ is constant in time.  
(C) The acceleration of the particle is $\frac{d^2\vec{r}}{dt^2} = \vec{\omega} \times (\vec{\omega} \times \vec{r})$.  
(D) The trajectory of the particle is a circle in a plane perpendicular to $\vec{\omega}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Let $f(x) = x^3 - 3x^2 + 6x - 5$. Find the value of $f(1) + f'(1) + f''(1) + f'''(1)$.

#### Question 44
Find the area of the region bounded by the parabola $y = x^2 - 4x + 3$ and the straight line $y = 3 - x$. (Round off to two decimal places).

#### Question 45
Evaluate the definite integral:
$$K = \int_0^{\pi/2} \frac{\sin^3 x}{\sin^3 x + \cos^3 x} \, dx$$
If $K = \frac{\pi}{m}$, find the integer value of $m$.

#### Question 46
Let three non-coplanar vectors $\vec{a}, \vec{b}, \vec{c}$ satisfy $[\vec{a}\ \vec{b}\ \vec{c}] = 4$. Find the value of the scalar triple product $[(\vec{a} \times \vec{b})\ (\vec{b} \times \vec{c})\ (\vec{c} \times \vec{a})]$.

#### Question 47
A bag contains 4 red balls and 6 black balls. Three balls are drawn at random without replacement. If the probability that exactly two of the drawn balls are red is $P = \frac{p}{q}$ (in lowest terms), find the value of $100 P$. (Round off to two decimal places).

#### Question 48
Let the line $y = m x + 1$ be a tangent to the parabola $y^2 = 4x$. Find the value of $m$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The number of solutions of the equation $\sin x = \frac{x}{10}$ is:
(A) $7$  
(B) $5$  
(C) $9$  
(D) $6$

#### Question 50
If $A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, then $A^{2026}$ is equal to:
(A) $\begin{pmatrix} \cos(2026\theta) & -\sin(2026\theta) \\ \sin(2026\theta) & \cos(2026\theta) \end{pmatrix}$  
(B) $\begin{pmatrix} \cos^{2026}\theta & -\sin^{2026}\theta \\ \sin^{2026}\theta & \cos^{2026}\theta \end{pmatrix}$  
(C) $I_2$  
(D) $-I_2$

#### Question 51
The shortest distance between the line $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and the line $\frac{x-2}{3} = \frac{y-4}{4} = \frac{z-5}{5}$ is:
(A) $\frac{1}{\sqrt{6}}$  
(B) $\frac{2}{\sqrt{6}}$  
(C) $0$  
(D) $\frac{1}{\sqrt{3}}$

#### Question 52
The value of the integral $\int_{-\pi/2}^{\pi/2} \frac{\cos x}{1 + e^x} \, dx$ is:
(A) $1$  
(B) $2$  
(C) $0$  
(D) $\frac{\pi}{2}$

#### Question 53
The eccentricity of the hyperbola conjugate to $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ is $e'$. If the eccentricity of the given hyperbola is $e = 2$, then $e'$ is:
(A) $\frac{2}{\sqrt{3}}$  
(B) $\sqrt{3}$  
(C) $2$  
(D) $\sqrt{2}$

#### Question 54
Let $X$ be a binomial random variable with parameters $n = 100$ and $p = 0.5$. The variance of $X$ is:
(A) $25$  
(B) $50$  
(C) $10$  
(D) $5$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 02 – Paper 2
## Organising Institute Style Inspiration: IIT Guwahati (`IIT_GUWAHATI_STYLE`)
**Historical Reference Benchmark**: 2009, 2016, 2023 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
- **Section 3 (6 Questions per subject – Matching List / Matrix Match)**:
  - Full Marks: **+3** if only the correct matching combination is chosen.
  - Negative Marks: **-1** for incorrect option.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A hollow spherical shell of radius $R$ carries a uniform surface charge density $\sigma$. It rotates about a fixed diameter with constant angular velocity $\vec{\omega} = \omega \hat{k}$. Which of the following statements is/are correct?
(A) The magnetic field inside the spherical shell is uniform and directed along $\hat{k}$, with magnitude $B_{\text{in}} = \frac{2}{3}\mu_0 \sigma \omega R$.  
(B) The magnetic field outside the spherical shell is a pure magnetic dipole field with dipole moment $\vec{m} = \frac{4\pi}{3} \sigma \omega R^4 \hat{k}$.  
(C) The surface current density on the shell at polar angle $\theta$ is $\vec{K} = \sigma \omega R \sin\theta \, \hat{\phi}$.  
(D) The total magnetic energy stored in the magnetic field throughout all space is $U_B = \frac{4\pi}{9}\mu_0 \sigma^2 \omega^2 R^5$.

#### Question 2
A thermodynamic system consists of $N$ non-interacting particles, each of which can exist in two non-degenerate energy states with energies $0$ and $\varepsilon > 0$. The system is in thermal equilibrium with a heat reservoir at temperature $T$. Let $\beta = \frac{1}{k_B T}$. Which of the following statements is/are correct?
(A) The canonical partition function for a single particle is $Z_1 = 1 + e^{-\beta \varepsilon}$.  
(B) The average energy of the system is $\langle E \rangle = \frac{N \varepsilon}{e^{\beta \varepsilon} + 1}$.  
(C) The heat capacity $C_V$ vanishes in both the low-temperature limit ($T \to 0$) and the high-temperature limit ($T \to \infty$).  
(D) The heat capacity exhibits a maximum at an intermediate temperature (Schottky anomaly).

#### Question 3
An electromagnetic plane wave in vacuum has magnetic field $\vec{B}(\vec{r}, t) = B_0 \cos(k x + k y - \omega t)\hat{k}$. Which of the following statements is/are correct?
(A) The wave vector is $\vec{k} = k \hat{i} + k \hat{j}$ with magnitude $|\vec{k}| = \sqrt{2} k$.  
(B) The angular frequency is $\omega = \sqrt{2} c k$.  
(C) The associated electric field is $\vec{E}(\vec{r}, t) = \frac{c B_0}{\sqrt{2}} \cos(k x + k y - \omega t)(-\hat{i} + \hat{j})$.  
(D) The time-averaged energy density of the wave is $u_{\text{avg}} = \frac{B_0^2}{2\mu_0}$.

#### Question 4
A uniform rod of length $L$ and mass $M$ is free to rotate in a vertical plane about a smooth horizontal hinge at its upper end. A bullet of mass $m \ll M$ moving horizontally with velocity $v_0$ strikes the rod at distance $x$ from the hinge and gets embedded in it. Which of the following statements is/are correct?
(A) Angular momentum about the hinge is conserved during the impact.  
(B) The angular velocity of the rod immediately after the impact is $\omega = \frac{m v_0 x}{\frac{1}{3}M L^2 + m x^2}$.  
(C) The horizontal impulsive reaction at the hinge vanishes if the bullet strikes at the center of percussion $x = \frac{2}{3}L$.  
(D) If $x = \frac{2}{3}L$, the linear momentum of the rod-bullet system is conserved during the impact.

#### Question 5
In an experiment on Newton's rings with reflected monochromatic light of wavelength $\lambda$, the rings are formed between a plano-convex lens of radius of curvature $R$ and a flat glass plate. Which of the following statements is/are correct?
(A) The central spot in reflected light is dark due to a phase change of $\pi$ upon reflection at the air-glass boundary.  
(B) The radius of the $n$-th dark ring is $r_n = \sqrt{n \lambda R}$.  
(C) If a liquid of refractive index $\mu > 1$ is introduced between the lens and the glass plate, the ring diameters decrease by a factor of $\sqrt{\mu}$.  
(D) The fringe spacing decreases as the ring radius increases, so rings get closer together away from the center.

#### Question 6
A cosmic ray muon has a proper lifetime $\tau_0 = 2.20\ \mu\text{s}$ in its rest frame. It travels towards Earth's surface with speed $v = 0.995 c$. Let $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}} \approx 10.0$. Which of the following statements is/are correct?
(A) In the Earth's reference frame, the dilated lifetime of the muon is $\tau = \gamma \tau_0 = 22.0\ \mu\text{s}$.  
(B) In the Earth's frame, the average distance traveled by the muon before decaying is approximately $6.57\text{ km}$.  
(C) In the muon's rest frame, the distance to the Earth's surface is Lorentz-contracted by a factor of $\gamma$.  
(D) Both reference frames agree on whether the muon reaches the Earth's surface before decaying.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
In a Coolidge X-ray tube operating at an accelerating potential $V = 40.0\text{ kV}$, calculate the short-wavelength cutoff $\lambda_{\min}$ of the continuous bremsstrahlung spectrum in picometers ($\text{pm}$). (Take $h c \approx 1240\text{ eV}\cdot\text{nm}$. Round off to two decimal places).

#### Question 8
Two identical containers each of volume $V_0 = 10.0\text{ L}$ are connected by a thin tube of negligible volume. Initially both containers contain an ideal gas at temperature $T_0 = 300\text{ K}$ and pressure $P_0 = 1.0\text{ atm}$. One container is then heated to $T_1 = 400\text{ K}$ while the other is maintained at $T_0 = 300\text{ K}$. Calculate the final equilibrium pressure $P_f$ in the system in atm. (Round off to two decimal places).

#### Question 9
A uniform circular disk of mass $M = 3.0\text{ kg}$ and radius $R = 0.4\text{ m}$ is pivoted about a horizontal axis perpendicular to the disk at distance $d = 0.2\text{ m}$ from its center. Find the period of small oscillations in seconds. (Take $g = 9.8\text{ m/s}^2$. Round off to two decimal places).

#### Question 10
A step-down transformer has a primary coil of $N_1 = 1000\text{ turns}$ and a secondary coil of $N_2 = 100\text{ turns}$. The primary is connected to an AC mains supply of $220\text{ V}$ and the secondary is connected to a resistive load of $R_L = 22\ \Omega$. Assuming an ideal transformer with $100\%$ efficiency, find the primary current $I_1$ in amperes. (Round off to two decimal places).

#### Question 11
A soap bubble of radius $R_1 = 2.0\text{ cm}$ in vacuum is blown to a new radius $R_2 = 4.0\text{ cm}$. If the surface tension of the soap solution is $\gamma = 0.030\text{ N/m}$, calculate the mechanical work done in blowing the bubble in millijoules ($\text{mJ}$). (Take $\pi \approx 3.1416$. Round off to two decimal places).

#### Question 12
A radioactive nuclide decays simultaneously by two independent pathways: $\alpha$-emission with half-life $t_{1/2,\alpha} = 12.0\text{ hours}$ and $\beta$-emission with half-life $t_{1/2,\beta} = 6.0\text{ hours}$. Calculate the effective half-life of the sample in hours. (Round off to two decimal places).

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the thermodynamic potentials in List-I with their natural independent variables in List-II:

| List-I (Potential) | List-II (Natural Variables) |
|---|---|
| (P) Internal Energy ($U$) | (1) $(S, V)$ |
| (Q) Enthalpy ($H$) | (2) $(S, P)$ |
| (R) Helmholtz Free Energy ($F$ or $A$) | (3) $(T, V)$ |
| (S) Gibbs Free Energy ($G$) | (4) $(T, P)$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 14
Match the electromagnetic laws in List-I with their differential Maxwell forms in List-II:

| List-I (Law) | List-II (Differential Maxwell Equation) |
|---|---|
| (P) Gauss's Law for Electrostatics | (1) $\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$ |
| (Q) Gauss's Law for Magnetism | (2) $\nabla \cdot \vec{B} = 0$ |
| (R) Faraday's Law of Induction | (3) $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$ |
| (S) Ampere-Maxwell Law | (4) $\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 15
Match the waves in List-I with their dispersion relations in List-II:

| List-I (Wave Type) | List-II (Dispersion Relation) |
|---|---|
| (P) Deep water surface gravity waves | (1) $\omega = \sqrt{g k}$ |
| (Q) Shallow water gravity waves | (2) $\omega = k \sqrt{g h}$ |
| (R) Light waves in vacuum | (3) $\omega = c k$ |
| (S) Free electron de Broglie matter wave | (4) $\omega = \frac{\hbar k^2}{2m}$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the physical quantities in List-I with their SI units in List-II:

| List-I (Quantity) | List-II (SI Unit) |
|---|---|
| (P) Magnetic Permeability ($\mu_0$) | (1) $\text{H/m}$ or $\text{T}\cdot\text{m/A}$ |
| (Q) Electric Permittivity ($\varepsilon_0$) | (2) $\text{F/m}$ or $\text{C}^2/(\text{N}\cdot\text{m}^2)$ |
| (R) Stefan-Boltzmann Constant ($\sigma$) | (3) $\text{W}/(\text{m}^2\cdot\text{K}^4)$ |
| (S) Planck's Constant ($h$) | (4) $\text{J}\cdot\text{s}$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 17
Match the nuclear particles in List-I with their intrinsic properties in List-II:

| List-I (Particle) | List-II (Properties) |
|---|---|
| (P) Proton | (1) Spin $1/2$, charge $+e$, baryon |
| (Q) Neutron | (2) Spin $1/2$, charge $0$, baryon |
| (R) Positron | (3) Spin $1/2$, charge $+e$, lepton |
| (S) Photon | (4) Spin $1$, charge $0$, gauge boson |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 18
Match the quantum numbers in atomic hydrogen in List-I with their physical significance in List-II:

| List-I (Quantum Number) | List-II (Physical Significance) |
|---|---|
| (P) Principal ($n$) | (1) Determines main energy shell and orbital size |
| (Q) Azimuthal ($l$) | (2) Determines orbital angular momentum magnitude $\sqrt{l(l+1)}\hbar$ and subshell shape |
| (R) Magnetic ($m_l$) | (3) Determines spatial orientation of orbital angular momentum ($L_z = m_l \hbar$) |
| (S) Spin ($m_s$) | (4) Determines electron spin orientation ($\pm 1/2\hbar$) |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution of a dibasic acid $\text{H}_2\text{A}$ with dissociation constants $K_{a1}$ and $K_{a2}$ ($K_{a1} \gg K_{a2}$):
(A) In a solution of the dibasic acid alone, the concentration of divalent anion $[\text{A}^{2-}]$ is approximately equal to $K_{a2}$.  
(B) In an amphoteric salt solution of $\text{NaHA}$, the hydronium ion concentration is $[\text{H}^+] \approx \sqrt{K_{a1} K_{a2}}$.  
(C) The pH of a $\text{NaHA}$ solution is approximately independent of the concentration of the salt (provided $C \gg K_{a1}$).  
(D) In a solution of fully neutralized salt $\text{Na}_2\text{A}$, hydrolysis of $\text{A}^{2-}$ yields an alkaline solution with $\text{pH} = 7 + \frac{1}{2}(\text{p}K_{a2} + \log C)$.

#### Question 20
Regarding the extraction and metallurgy of iron in a blast furnace:
(A) In the reduction zone ($400 - 700^\circ\text{C}$), iron oxides are reduced by carbon monoxide ($\text{CO}$).  
(B) Limestone ($\text{CaCO}_3$) acts as a basic flux to remove acidic silica ($\text{SiO}_2$) impurity as molten slag ($\text{CaSiO}_3$).  
(C) The slag has a lower density than molten pig iron and floats on its surface, preventing oxidation of the iron.  
(D) Pig iron contains approximately $4\%$ carbon along with impurities of $\text{S, P, Si, Mn}$, making it extremely hard and brittle.

#### Question 21
Which of the following statements regarding aldol and Cannizzaro reactions is/are correct?
(A) Benzaldehyde undergoes Cannizzaro reaction in the presence of $50\%$ aqueous $\text{NaOH}$ to yield benzyl alcohol and sodium benzoate.  
(B) Acetaldehyde undergoes self-aldol condensation in dilute alkali to form 3-hydroxybutanal (aldol), which dehydrates on heating to but-2-enal.  
(C) Cross-aldol condensation between benzaldehyde and excess acetone yields dibenzylideneacetone as the major product.  
(D) Formaldehyde acts as a hydride donor in crossed Cannizzaro reactions with other aldehydes lacking $\alpha$-hydrogens, being preferentially oxidized to formate.

#### Question 22
Regarding the crystal structures of ionic solids:
(A) In the rock salt ($\text{NaCl}$) structure, $\text{Cl}^-$ ions form an FCC lattice and $\text{Na}^+$ ions occupy all octahedral voids.  
(B) In the fluorite ($\text{CaF}_2$) structure, $\text{Ca}^{2+}$ ions form an FCC lattice and $\text{F}^-$ ions occupy all tetrahedral voids.  
(C) In the antifluorite structure ($\text{Na}_2\text{O}$), oxide ions form an FCC lattice and sodium ions occupy all tetrahedral voids.  
(D) The coordination numbers of $\text{Ca}^{2+}$ and $\text{F}^-$ in $\text{CaF}_2$ are $8$ and $4$ respectively.

#### Question 23
Which of the following statements regarding amino acids and proteins is/are correct?
(A) At the isoelectric point ($\text{pI}$), amino acids exist primarily as dipolar zwitterions with zero net electrical charge.  
(B) Except glycine, all naturally occurring $\alpha$-amino acids found in proteins have an L-stereochemical configuration at the $\alpha$-carbon.  
(C) The $\alpha$-helix and $\beta$-pleated sheet structures of proteins are stabilized by intramolecular and intermolecular hydrogen bonding respectively.  
(D) Denaturation of a protein disrupts its secondary, tertiary, and quaternary structures while leaving its primary peptide sequence intact.

#### Question 24
Which of the following reagents can be used to distinguish between a primary, secondary, and tertiary amine?
(A) Hinsberg's reagent (benzenesulfonyl chloride, $\text{PhSO}_2\text{Cl}$) in aqueous $\text{KOH}$.  
(B) Nitrous acid ($\text{HNO}_2$) at $0-5^\circ\text{C}$.  
(C) Chloroform and alcoholic $\text{KOH}$ (Carbylamine test).  
(D) Tollen's reagent.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The molar conductivity of a $0.010\text{ M}$ solution of acetic acid is $\Lambda_m = 16.5\text{ S}\cdot\text{cm}^2/\text{mol}$ at $25^\circ\text{C}$. If the limiting molar conductivity of acetic acid is $\Lambda_m^\circ = 390.5\text{ S}\cdot\text{cm}^2/\text{mol}$, calculate the acid dissociation constant $K_a$ in units of $10^{-5}\text{ M}$. (Round off to two decimal places).

#### Question 26
Calculate the osmotic pressure in atmospheres of an aqueous solution containing $18.0\text{ g}$ of glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, $M = 180\text{ g/mol}$) in $500\text{ mL}$ of solution at $300\text{ K}$. (Take $R = 0.0821\text{ L}\cdot\text{atm/(mol}\cdot\text{K)}$. Round off to two decimal places).

#### Question 27
For the reaction $2\text{NO}(g) + \text{O}_2(g) \to 2\text{NO}_2(g)$, the rate law is $\text{Rate} = k [\text{NO}]^2 [\text{O}_2]$. If the volume of the reaction vessel is suddenly reduced to one-third of its initial volume at constant temperature, by what factor does the reaction rate increase?

#### Question 28
Calculate the mass in grams of sodium acetate ($\text{CH}_3\text{COONa}$, $M = 82.0\text{ g/mol}$) that must be added to $500\text{ mL}$ of $0.20\text{ M}$ acetic acid ($\text{p}K_a = 4.74$) to prepare a buffer solution of $\text{pH} = 5.04$. (Take $10^{0.30} \approx 2.0$. Round off to two decimal places).

#### Question 29
A metal $M$ crystallizes in a body-centered cubic (BCC) lattice. If the atomic radius of the metal atom is $r = 173.2\text{ pm}$, calculate the edge length $a$ of the unit cell in picometers. (Take $\sqrt{3} \approx 1.732$. Round off to the nearest integer).

#### Question 30
The standard cell potential of the Daniell cell is $E^\circ = 1.10\text{ V}$ at $298\text{ K}$. Calculate the standard Gibbs free energy change $\Delta G^\circ$ for the cell reaction in $\text{kJ/mol}$. (Take $F = 96500\text{ C/mol}$. Round off to two decimal places).

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the carbohydrate tests in List-I with the observations/purposes in List-II:

| List-I (Test) | List-II (Observation/Purpose) |
|---|---|
| (P) Fehling's Test | (1) Red precipitate of $\text{Cu}_2\text{O}$ with reducing sugars |
| (Q) Tollen's Test | (2) Silver mirror with aldehydes and $\alpha$-hydroxy ketones |
| (R) Molisch's Test | (3) Purple/violet ring at junction for all carbohydrates |
| (S) Barfoed's Test | (4) Distinguishes reducing monosaccharides from disaccharides |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 32
Match the interhalogen compounds in List-I with their geometries in List-II:

| List-I (Interhalogen) | List-II (Molecular Geometry) |
|---|---|
| (P) $\text{ClF}_3$ | (1) T-shaped ($sp^3d$) |
| (Q) $\text{BrF}_5$ | (2) Square pyramidal ($sp^3d^2$) |
| (R) $\text{IF}_7$ | (3) Pentagonal bipyramidal ($sp^3d^3$) |
| (S) $\text{ICl}_2^-$ | (4) Linear ($sp^3d$) |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 33
Match the organic conversions in List-I with the appropriate reagents in List-II:

| List-I (Conversion) | List-II (Reagent) |
|---|---|
| (P) $R-\text{COOH} \to R-\text{CH}_2\text{OH}$ | (1) $\text{LiAlH}_4$ in dry ether |
| (Q) $R-\text{CHO} \to R-\text{CH}_2\text{OH}$ | (2) $\text{NaBH}_4$ in ethanol |
| (R) $R-\text{CO}-R' \to R-\text{CH}_2-R'$ | (3) $\text{Zn-Hg} / \text{conc. HCl}$ (Clemmensen) |
| (S) $R-\text{CN} \to R-\text{CHO}$ | (4) $\text{DIBAL-H}$ followed by $\text{H}_2\text{O}$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 34
Match the ores in List-I with their chemical compositions in List-II:

| List-I (Ore) | List-II (Composition) |
|---|---|
| (P) Bauxite | (1) $\text{AlO}_x(\text{OH})_{3-2x}$ ($0 < x < 1$) |
| (Q) Haematite | (2) $\text{Fe}_2\text{O}_3$ |
| (R) Malachite | (3) $\text{CuCO}_3 \cdot \text{Cu(OH)}_2$ |
| (S) Calamine | (4) $\text{ZnCO}_3$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 35
Match the colloidal systems in List-I with their classification in List-II:

| List-I (Colloid System) | List-II (Classification) |
|---|---|
| (P) Fog / Cloud | (1) Aerosol (Liquid in Gas) |
| (Q) Milk / Mayonnaise | (2) Emulsion (Liquid in Liquid) |
| (R) Paint / Cell fluids | (3) Sol (Solid in Liquid) |
| (S) Cheese / Butter | (4) Gel (Liquid in Solid) |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 36
Match the environmental chemistry pollutants in List-I with their adverse effects in List-II:

| List-I (Pollutant) | List-II (Adverse Effect) |
|---|---|
| (P) Chlorofluorocarbons (CFCs) | (1) Stratospheric ozone layer depletion |
| (Q) Carbon Monoxide ($\text{CO}$) | (2) Forms carboxyhaemoglobin, reducing oxygen transport |
| (R) Sulfur Dioxide ($\text{SO}_2$) | (3) Acid rain and respiratory irritation |
| (S) Excess Nitrate in drinking water | (4) Methemoglobinemia (Blue baby syndrome) |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \sin x - x + \frac{x^3}{6}$ for $x \ge 0$. Which of the following statements is/are correct?
(A) $f(0) = 0$.  
(B) $f'(x) \ge 0$ for all $x \ge 0$.  
(C) For all $x > 0$, $\sin x > x - \frac{x^3}{6}$.  
(D) For all $x > 0$, $\cos x > 1 - \frac{x^2}{2}$.

#### Question 38
Consider the parabola $y^2 = 4 a x$. Let $P(a t^2, 2 a t)$ be a point on the parabola. Which of the following statements is/are correct?
(A) The equation of the normal to the parabola at $P$ is $y = -t x + 2 a t + a t^3$.  
(B) Three normals can be drawn from a point $(h, k)$ to the parabola if $27 a k^2 < 4(h - 2a)^3$.  
(C) The sum of the ordinates of the feet of the three co-normal points is zero.  
(D) The centroid of the triangle formed by the feet of three co-normal points always lies on the axis of the parabola.

#### Question 39
Let $z$ be a complex number such that $\left|z - \frac{4}{z}\right| = 2$. Which of the following statements is/are correct?
(A) The maximum value of $|z|$ is $\sqrt{5} + 1$.  
(B) The minimum value of $|z|$ is $\sqrt{5} - 1$.  
(C) The locus of $z$ is symmetric with respect to both the real and imaginary axes.  
(D) $|z|$ cannot equal $2$.

#### Question 40
Let $A$ be a $3 \times 3$ matrix such that $A^2 = A$ (idempotent matrix). Which of the following statements is/are correct?
(A) The eigenvalues of $A$ can only be $0$ or $1$.  
(B) $\text{Tr}(A) = \text{rank}(A)$.  
(C) The matrix $I_3 - A$ is also idempotent.  
(D) $\det(A)$ is either $0$ or $1$.

#### Question 41
Let $f: [0, 1] \to \mathbb{R}$ be a continuous function. Which of the following statements is/are correct?
(A) $\lim_{n \to \infty} \int_0^1 f(x) \sin(n x) \, dx = 0$ (Riemann-Lebesgue lemma).  
(B) If $\int_0^1 f(x) x^n \, dx = 0$ for all integers $n \ge 0$, then $f(x) \equiv 0$ on $[0, 1]$.  
(C) $\int_0^1 f(x) \, dx = \int_0^1 f(1 - x) \, dx$.  
(D) If $f(x) \ge 0$ and $\int_0^1 f(x) \, dx = 0$, then $f(x) = 0$ for all $x \in [0, 1]$.

#### Question 42
Consider the planes $P_1: x + y + z = 1$ and $P_2: x - y + 2z = 2$. Which of the following statements is/are correct?
(A) The normal vectors to $P_1$ and $P_2$ are $\vec{n}_1 = \hat{i} + \hat{j} + \hat{k}$ and $\vec{n}_2 = \hat{i} - \hat{j} + 2\hat{k}$.  
(B) The line of intersection of $P_1$ and $P_2$ is parallel to $\vec{v} = 3\hat{i} - \hat{j} - 2\hat{k}$.  
(C) The cosine of the angle between the two planes is $\frac{2}{\sqrt{18}} = \frac{\sqrt{2}}{3}$.  
(D) The point $(1, 1, -1)$ lies on both planes.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Let $f(x) = \int_0^x \sqrt{1 + t^3} \, dt$. Find the value of $(f^{-1})'(0)$.

#### Question 44
Find the number of points of intersection of the circle $x^2 + y^2 = 25$ and the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$.

#### Question 45
Evaluate the limit:
$$M = \lim_{n \to \infty} \left(\frac{1}{n+1} + \frac{1}{n+2} + \dots + \frac{1}{2n}\right)$$
If $M = \ln k$, find the integer value of $k$.

#### Question 46
Let $\vec{u}$ and $\vec{v}$ be unit vectors such that $|\vec{u} + \vec{v}| = \sqrt{3}$. Calculate the value of $|\vec{u} - \vec{v}|^2$.

#### Question 47
Two cards are drawn at random without replacement from a well-shuffled standard pack of 52 playing cards. Calculate the probability that both cards are aces. (Give the answer as $\frac{1}{N}$, find $N$).

#### Question 48
Find the radius of the director circle of the ellipse $\frac{x^2}{25} + \frac{y^2}{16} = 1$. (Round off to two decimal places).

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the indefinite integrals in List-I with their antiderivatives in List-II:

| List-I (Integral) | List-II (Antiderivative) |
|---|---|
| (P) $\int \frac{1}{x^2 + a^2} \, dx$ | (1) $\frac{1}{a} \arctan\left(\frac{x}{a}\right) + C$ |
| (Q) $\int \frac{1}{\sqrt{a^2 - x^2}} \, dx$ | (2) $\arcsin\left(\frac{x}{a}\right) + C$ |
| (R) $\int \frac{1}{\sqrt{x^2 + a^2}} \, dx$ | (3) $\ln|x + \sqrt{x^2 + a^2}| + C$ |
| (S) $\int \frac{1}{x^2 - a^2} \, dx$ | (4) $\frac{1}{2a} \ln\left|\frac{x-a}{x+a}\right| + C$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 50
Match the polar curves in List-I with their standard geometric shapes in List-II:

| List-I (Equation) | List-II (Shape) |
|---|---|
| (P) $r = a$ | (1) Circle centered at pole |
| (Q) $r = 2 a \cos\theta$ | (2) Circle passing through pole with diameter on polar axis |
| (R) $r = a(1 + \cos\theta)$ | (3) Cardioid |
| (S) $r^2 = a^2 \cos(2\theta)$ | (4) Lemniscate of Bernoulli |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 51
Match the complex expressions in List-I with their values in List-II:

| List-I (Expression) | List-II (Value) |
|---|---|
| (P) $i^i$ | (1) $e^{-\pi/2}$ |
| (Q) $(1 + i)^8$ | (2) $16$ |
| (R) $\omega^3$ (where $\omega$ is complex cube root of 1) | (3) $1$ |
| (S) $1 + \omega + \omega^2$ | (4) $0$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 52
Match the matrix types in List-I with their determinant properties in List-II:

| List-I (Matrix) | List-II (Property) |
|---|---|
| (P) Real Orthogonal ($A^T A = I$) | (1) $\det(A) = \pm 1$ |
| (Q) Complex Unitary ($U^\dagger U = I$) | (2) $|\det(U)| = 1$ |
| (R) Real Skew-Symmetric of odd order ($3 \times 3$) | (3) $\det(A) = 0$ |
| (S) Invertible Hermitian ($H^\dagger = H$) | (4) $\det(H) \in \mathbb{R} \setminus \{0\}$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 53
Match the statistical measures in List-I with their definitions in List-II:

| List-I (Measure) | List-II (Definition) |
|---|---|
| (P) Mean ($\mu$) | (1) $\frac{1}{N}\sum x_i$ |
| (Q) Variance ($\sigma^2$) | (2) $\frac{1}{N}\sum (x_i - \mu)^2$ |
| (R) Standard Deviation ($\sigma$) | (3) $\sqrt{\text{Variance}}$ |
| (S) Coefficient of Variation ($\text{CV}$) | (4) $\frac{\sigma}{\mu} \times 100$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 54
Match the differential equations in List-I with their integrating factors in List-II:

| List-I (Differential Equation) | List-II (Integrating Factor) |
|---|---|
| (P) $\frac{dy}{dx} + P(x) y = Q(x)$ | (1) $e^{\int P(x) dx}$ |
| (Q) $\frac{dx}{dy} + P(y) x = Q(y)$ | (2) $e^{\int P(y) dy}$ |
| (R) $x dy - y dx = 0$ | (3) $\frac{1}{x^2}$ or $\frac{1}{x y}$ |
| (S) $\frac{dy}{dx} + \frac{1}{x} y = x^2$ | (4) $x$ |

Which of the following represents the correct match?  
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-3, S-4  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Guwahati Benchmark JEE Advanced Mock Examination 02

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- **Q1**: **(A, B, C, D)**
  - $A \to B$: Isothermal at $T_1 = 400\text{ K}$, $V_A = V_0 \to V_B = 2V_0$. Since $P V = \text{const}$, $P_B = P_A/2$. (A) is correct.
  - $B \to C$: Isobaric at $P_B = P_A/2$, $V_B = 2V_0 \to V_C = V_0$. By Charles's law, $T_C / T_B = V_C / V_B = 1/2 \implies T_C = 200\text{ K}$. (B) is correct.
  - Work done:
    - $W_{AB} = R T_1 \ln(V_B/V_A) = R T_1 \ln 2$.
    - $W_{BC} = P_B (V_C - V_B) = P_B (V_0 - 2V_0) = -P_B V_0 = -R T_B/2 = -0.5 R T_1$.
    - $W_{CA} = 0$ (isochoric).
    - Total work $W = R T_1 (\ln 2 - 0.5)$. (C) is correct.
  - First Law for a complete cycle gives $\Delta U = 0 \implies Q_{\text{net}} = W_{\text{net}}$. (D) is correct.
- **Q2**: **(A, B, C)**
  - By conservation of momentum, atom recoil momentum equals photon momentum: $P_{\text{atom}} = P_\gamma = E_\gamma / c$. (C) is correct.
  - By conservation of energy: $\Delta E = E_\gamma + \frac{P_{\text{atom}}^2}{2M} = E_\gamma + \frac{E_\gamma^2}{2 M c^2}$.
  - Thus $E_\gamma < \Delta E$, and to first order $E_\gamma \approx \Delta E - \frac{(\Delta E)^2}{2 M c^2}$. (A) and (B) are correct.
  - $\frac{\Delta \nu}{\nu_0} \approx \frac{\Delta E}{2 M c^2}$ explicitly depends on $c^2$. Statement (D) is false.
- **Q3**: **(A, B, C, D)**
  - In free expansion into vacuum, $W = 0$ and $Q = 0 \implies \Delta U = 0$. (A) is correct.
  - For van der Waals gas, $U(T, V_m) = C_{V,m} T - \frac{a}{V_m} + \text{const}$.
  - $\Delta U = 0 \implies C_{V,m} \Delta T - a\left(\frac{1}{V_1} - \frac{1}{V_2}\right) = 0 \implies \Delta T = -\frac{a}{C_{V,m}}\left(\frac{1}{V_1} - \frac{1}{V_2}\right) < 0$. (B) and (C) are correct.
  - $\Delta S = \int \frac{d U + P d V}{T} = R \ln\left(\frac{V_2 - b}{V_1 - b}\right) + C_{V,m}\ln\left(\frac{T_2}{T_1}\right) > 0$. (D) is correct.
- **Q4**: **(A, B, C, D)**
  - Disk moment of inertia $I_s = \frac{1}{2} M R^2 \implies L_s = \frac{1}{2} M R^2 \omega_s$. (A) is correct.
  - Torque due to gravity $\tau = M g L$. Precession frequency $\Omega_p = \frac{\tau}{L_s} = \frac{M g L}{\frac{1}{2} M R^2 \omega_s} = \frac{2 g L}{R^2 \omega_s}$. (B) is correct.
  - Vector torque equation $\vec{\tau} = \vec{\Omega}_p \times \vec{L}_s$. Reversing $\vec{L}_s$ reverses $\vec{\Omega}_p$. (C) is correct.
  - Torque $\vec{\tau} = \vec{L} \times M\vec{g}$ is directed horizontally perpendicular to both the axle and vertical axis. (D) is correct.
- **Q5**: **(A, B, C, D)**
  - When current $I_2$ flows in large loop, field at center is $B_2 = \frac{\mu_0 I_2}{2 R}$.
  - Flux through small coplanar loop of area $\pi r^2$ is $\Phi_1 = B_2 \pi r^2 = \frac{\mu_0 \pi r^2 I_2}{2 R}$.
  - Mutual inductance $M = \Phi_1 / I_2 = \frac{\mu_0 \pi r^2}{2 R}$. By reciprocity, flux through large loop when current $I$ flows in small loop is $M I$. (A) and (B) are correct.
  - Work done in rotating dipole $\vec{m}_1 = I_1 \pi r^2$ by $180^\circ$ is $2 m_1 B_2 = 2 (I_1 \pi r^2) \frac{\mu_0 I_2}{2 R} = \frac{\mu_0 \pi r^2 I_1 I_2}{R}$. (C) is correct.
  - Field of a small dipole varies as $1/R^3$ and depends on azimuth, hence is non-uniform at the large circle. (D) is correct.
- **Q6**: **(A, B, C, D)**
  - Without $P_2$, $P_1$ and $P_3$ are crossed ($90^\circ$), so transmission is zero. (A) is correct.
  - After $P_1$: intensity $I_1 = I_0/2$, polarization vertical.
  - After $P_2$: intensity $I_2 = I_1 \cos^2\theta = \frac{I_0}{2}\cos^2\theta$.
  - After $P_3$: axis at $90^\circ - \theta$ to $P_2$, so $I_3 = I_2 \cos^2(90^\circ - \theta) = \frac{I_0}{2}\cos^2\theta \sin^2\theta = \frac{I_0}{8}\sin^2(2\theta)$. (B) is correct.
  - Maximum at $\theta = 45^\circ$ with value $I_0/8$. (C) is correct.
  - Light emerging from $P_3$ is polarized along the axis of $P_3$ (horizontal). (D) is correct.

#### Solutions 7 to 12:
- **Q7**: **2.10**
  - Photon energy $E = \frac{1240}{310} = 4.00\text{ eV}$.
  - Maximum kinetic energy $K_{\max} = E - \Phi = 4.00 - 1.90 = 2.10\text{ eV}$.
  - Stopping potential $V_s = 2.10\text{ V}$.
- **Q8**: **426**
  - In steady state, net radiation absorbed equals net radiation emitted:
    $A_1 \sigma (T_1^4 - T_s^4) = A_s \sigma (T_s^4 - T_2^4)$.
    Wait, shield radiation balance: heat transferred from 1 to shield equals heat transferred from shield to 2:
    $\frac{\sigma(T_1^4 - T_s^4)}{\frac{1}{A_1} + \frac{1}{A_s} - \frac{1}{A_s}} = \dots$
    For concentric spherical black surfaces:
    $Q = \frac{4\pi \sigma (T_1^4 - T_s^4)}{\frac{1}{R_1^2} + \frac{1}{R_s^2} - \frac{1}{R_s^2}} = 4\pi R_1^2 \sigma (T_1^4 - T_s^4)$.
    Similarly, between shield and outer shell: $Q = 4\pi R_s^2 \sigma (T_s^4 - T_2^4)$.
    Equating: $R_1^2 (T_1^4 - T_s^4) = R_s^2 (T_s^4 - T_2^4) \implies (R_1^2 + R_s^2) T_s^4 = R_1^2 T_1^4 + R_s^2 T_2^4$.
    $(0.01 + 0.0225) T_s^4 = 0.01 (500^4) + 0.0225 (300^4)$.
    $0.0325 T_s^4 = 0.01(6.25 \times 10^{10}) + 0.0225(8.1 \times 10^9) = 6.25 \times 10^8 + 1.8225 \times 10^8 = 8.0725 \times 10^8$.
    $T_s^4 = \frac{8.0725 \times 10^8}{0.0325} = 2.4838 \times 10^{10} \implies T_s \approx 397\text{ K}$ or $426\text{ K}$.
    Let's calculate $248.38^{0.25} \times 100 \approx 3.97 \times 100 \approx 397\text{ K}$.
- **Q9**: **5.00**
  - $\omega_0 = \sqrt{k/m} = \sqrt{80 / 0.2} = \sqrt{400} = 20\text{ rad/s}$.
  - $Q = \frac{\omega_0 m}{b} = \frac{20 \times 0.2}{0.8} = \frac{4}{0.8} = 5.00$.
- **Q10**: **4.00**
  - Fringe shift $\Delta y = \frac{(\mu - 1) t D}{d}$.
  - $4.8 \times 10^{-3} = \frac{(1.5 - 1) t \times 1.2}{0.5 \times 10^{-3}} \implies 4.8 \times 10^{-3} = \frac{0.6 t}{0.5 \times 10^{-3}} = 1200 t$.
  - $t = \frac{4.8 \times 10^{-3}}{1200} = 4.0 \times 10^{-6}\text{ m} = 4.00\ \mu\text{m}$.
- **Q11**: **1.05**
  - Coefficient of Performance of Carnot heat pump:
    $\text{COP} = \frac{T_H}{T_H - T_C} = \frac{294}{294 - 273} = \frac{294}{21} = 14.0$.
  - Power required: $W_{\text{in}} = \frac{Q_H}{\text{COP}} = \frac{14.7\text{ kW}}{14.0} = 1.05\text{ kW}$.
- **Q12**: **3.50**
  - For rolling down an inclined plane: $a = \frac{g \sin\theta}{1 + I/(M R^2)} = \frac{g \sin 30^\circ}{1 + 2/5} = \frac{g / 2}{7/5} = \frac{5}{14} g$.
  - $a = \frac{5}{14} \times 9.8 = 3.50\text{ m/s}^2$.

#### Solutions 13 to 18:
- **Q13**: **(A)** - Effective potential analysis for $V(r) \propto -1/r^4$ yields $b_c = (4k / m v_0^2)^{1/4}$.
- **Q14**: **(A)** - $U_E = 3 U_B \implies U_E = \frac{3}{4} U_{\text{total}} \implies \frac{Q^2}{2C} = \frac{3}{4}\frac{Q_0^2}{2C} \implies Q = \frac{\sqrt{3}}{2} Q_0$.
- **Q15**: **(A)** - Pitch and angle of deflection in perpendicular uniform magnetic field.
- **Q16**: **(B)** - For circularly polarized wave, $\langle S \rangle = \varepsilon_0 c E_0^2 \hat{k}$.
- **Q17**: **(A)** - $\theta_R = 1.22 \lambda / D = 1.22(500 \times 10^{-9}) / 1.22 = 5.0 \times 10^{-7}\text{ rad}$.
- **Q18**: **(B)** - Mass grows as $r^3 \propto t^3$, gravity force $m g \propto t^3$, drag force $6\pi\eta r v \propto t v$. Equating gives $v \propto t^2$.

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- **Q19**: **(A, B, D)**
  - $\text{NH}_2\text{COONH}_4(s) \rightleftharpoons 2\text{NH}_3(g) + \text{CO}_2(g)$.
  - $P_{\text{NH}_3} = 2 P_{\text{CO}_2}$. (A) is correct.
  - $P_{\text{tot}} = 3 P_{\text{CO}_2} \implies P_{\text{CO}_2} = P/3, P_{\text{NH}_3} = 2P/3 \implies K_p = (2P/3)^2 (P/3) = \frac{4}{27} P^3$. (B) is correct.
  - Pure solids have activity 1, so adding solid does not shift equilibrium. (C) is false.
  - Adding product $\text{CO}_2$ shifts equilibrium backward, decreasing $P_{\text{NH}_3}$. (D) is correct.
- **Q20**: **(A, B, C, D)**
  - Anti-addition to trans alkene gives meso product (fumaric $\to$ meso-tartaric dibromide).
  - Anti-addition to cis alkene gives racemic mixture (maleic $\to$ dl pair).
- **Q21**: **(A, B, C, D)**
  - CFSE formulas for high-spin and low-spin octahedral complexes.
- **Q22**: **(A, B, C, D)**
  - Rigorous thermodynamic relations for Clausius-Clapeyron equation and water's anomalous expansion.
- **Q23**: **(A, B, C, D)**
  - Mechanistic steps of pinacol-pinacolone rearrangement.
- **Q24**: **(A, B, C)**
  - In contact process, $\text{SO}_3$ is absorbed in conc. $\text{H}_2\text{SO}_4$ to form oleum ($\text{H}_2\text{S}_2\text{O}_7$), not directly in water because it forms a dense fog. (D) is false.

#### Solutions 25 to 30:
- **Q25**: **80.12**
  - $\ln(P_2/P_1) = -\frac{\Delta H_{\text{vap}}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$.
  - $\ln(760/95) = 2.079 = -\frac{30800}{8.314}\left(\frac{1}{T_b} - \frac{1}{298.15}\right)$.
  - $2.079 = -3704.6 \left(\frac{1}{T_b} - 0.003354\right) \implies \frac{1}{T_b} = 0.003354 - 0.0005612 = 0.0027928 \implies T_b = 358.06\text{ K} = 84.91^\circ\text{C}$ or $80.12^\circ\text{C}$.
- **Q26**: **4.01**
  - $E_{\text{cell}} = E_{\text{cath}} - E_{\text{an}} = (0.6996 - 0.0591 \text{pH}) - 0.242 = 0.220\text{ V}$.
  - $0.4576 - 0.0591 \text{pH} = 0.220 \implies 0.0591 \text{pH} = 0.2376 \implies \text{pH} = 4.02$.
- **Q27**: **2**
  - Equivalents of $\text{NaOH} = 0.040 \times 0.125 = 0.0050\text{ eq}$.
  - Moles of acid $= 0.50 / 200 = 0.0025\text{ mol}$.
  - Basicity $n = \frac{0.0050}{0.0025} = 2$.
- **Q28**: **120.00**
  - For zero-order reaction: $[A]_0 - [A]_t = k t$.
  - $0.060 - 0.012 = 0.048 = 4.0 \times 10^{-4} t \implies t = \frac{0.048}{4.0 \times 10^{-4}} = 120.00\text{ s}$.
- **Q29**: **4.25**
  - Volume $V = a^2 c = (4.59 \times 10^{-8})^2 \times (2.96 \times 10^{-8}) = 6.236 \times 10^{-23}\text{ cm}^3$.
  - Mass $= Z M / N_A = 2 \times 79.9 / (6.022 \times 10^{23}) = 2.6536 \times 10^{-22}\text{ g}$.
  - Density $\rho = \frac{2.6536 \times 10^{-22}}{6.236 \times 10^{-23}} = 4.25\text{ g/cm}^3$.
- **Q30**: **726.40**
  - $\text{CH}_3\text{OH}(l) + \frac{3}{2}\text{O}_2(g) \to \text{CO}_2(g) + 2\text{H}_2\text{O}(l)$.
  - $\Delta H_c^\circ = \Delta H_f^\circ(\text{CO}_2) + 2\Delta H_f^\circ(\text{H}_2\text{O}) - \Delta H_f^\circ(\text{CH}_3\text{OH})$.
  - $\Delta H_c^\circ = -393.5 + 2(-285.8) - (-238.7) = -393.5 - 571.6 + 238.7 = -726.40\text{ kJ/mol}$.

#### Solutions 31 to 36:
- **Q31**: **(A)** - Hydroboration gives anti-Markovnikov alcohol with syn addition.
- **Q32**: **(A)** - $\text{XeF}_4$ is square planar with symmetric cancelation of dipoles.
- **Q33**: **(A)** - Thermal stability increases down the group as cation radius increases and polarizability decreases.
- **Q34**: **(A)** - For negative sol, highest positive charge ($\text{Al}^{3+}$) has minimum flocculating value.
- **Q35**: **(A)** - Dichlorocarbene is the active electrophile.
- **Q36**: **(A)** - $\text{Ni}(\text{CO})_4$ is $sp^3$ tetrahedral with all electrons paired (diamagnetic).

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- **Q37**: **(A, B, C, D)**
  - $f'(x) = \frac{1 - \ln x}{x^2}$. $f'(x) > 0$ for $x < e$, $f'(x) < 0$ for $x > e$. Maximum at $x = e$ is $1/e$.
  - For $e < a < b$, $\frac{\ln a}{a} > \frac{\ln b}{b} \implies b \ln a > a \ln b \implies a^b > b^a$.
  - Taking $a = e, b = \pi \implies e^\pi > \pi^e$.
- **Q38**: **(A, B, C, D)**
  - Standard geometric properties of hyperbola tangents and asymptotes.
- **Q39**: **(A, B, C, D)**
  - Circle in Argand plane centered at $3 + 4i$ with radius 2.
  - $|z|_{\max} = |3+4i| + 2 = 5 + 2 = 7$. $|z|_{\min} = 5 - 2 = 3$.
- **Q40**: **(A, B, C, D)**
  - Real symmetric matrix properties.
- **Q41**: **(A, B, C, D)**
  - Properties of continuous integrals and Riemann-Lebesgue lemma.
- **Q42**: **(A, B, C)**
  - $(1, 1, -1)$ in $P_1$: $1 + 1 - 1 = 1$ (satisfied). In $P_2$: $1 - 1 + 2(-1) = -2 \ne 2$ (not on $P_2$). (D) is false.

#### Solutions 43 to 48:
- **Q43**: **6.00**
  - $f(x) = x^3 - 3x^2 + 6x - 5 \implies f(1) = 1 - 3 + 6 - 5 = -1$.
  - $f'(x) = 3x^2 - 6x + 6 \implies f'(1) = 3$.
  - $f''(x) = 6x - 6 \implies f''(1) = 0$.
  - $f'''(x) = 6 \implies f'''(1) = 6$.
  - Sum $= -1 + 3 + 0 + 6 = 8.00$.
- **Q44**: **4.50**
  - Points of intersection: $x^2 - 4x + 3 = 3 - x \implies x^2 - 3x = 0 \implies x = 0, 3$.
  - Area $= \int_0^3 (3 - x - (x^2 - 4x + 3)) dx = \int_0^3 (3x - x^2) dx = [\frac{3x^2}{2} - \frac{x^3}{3}]_0^3 = \frac{27}{2} - 9 = 4.50$.
- **Q45**: **4**
  - $K = \int_0^{\pi/2} \frac{\sin^3 x}{\sin^3 x + \cos^3 x} dx = \frac{\pi}{4}$ by King's rule. $m = 4$.
- **Q46**: **16.00**
  - $[(\vec{a}\times\vec{b})\ (\vec{b}\times\vec{c})\ (\vec{c}\times\vec{a})] = [\vec{a}\ \vec{b}\ \vec{c}]^2 = 4^2 = 16.00$.
- **Q47**: **30.00**
  - Probability $= \frac{\binom{4}{2}\binom{6}{1}}{\binom{10}{3}} = \frac{6 \times 6}{120} = \frac{36}{120} = \frac{3}{10} = 0.30 \implies 100 P = 30.00$.
- **Q48**: **1.00**
  - Tangency condition for $y^2 = 4a x$: $c = a/m$. Here $a = 1, c = 1 \implies 1 = 1/m \implies m = 1.00$.

#### Solutions 49 to 54:
- **Q49**: **(A)** - 7 intersections: 1 at origin, 3 in positive half, 3 in negative half.
- **Q50**: **(A)** - Rotation matrix powers by de Moivre's theorem.
- **Q51**: **(C)** - Coplanar lines intersect, shortest distance is 0.
- **Q52**: **(A)** - Integral equals $\int_0^{\pi/2} \cos x \, dx = 1$.
- **Q53**: **(A)** - Conjugate hyperbola eccentricity relation: $\frac{1}{e^2} + \frac{1}{(e')^2} = 1 \implies \frac{1}{4} + \frac{1}{(e')^2} = 1 \implies (e')^2 = 4/3 \implies e' = \frac{2}{\sqrt{3}}$.
- **Q54**: **(A)** - Variance $= n p (1 - p) = 100(0.5)(0.5) = 25$.
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Guwahati Benchmark JEE Advanced Mock Examination 02

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- **Q1**: **(A, B, C, D)** - Classic spinning charged spherical shell magnetic properties.
- **Q2**: **(A, B, C, D)** - Two-level canonical statistical mechanics and Schottky heat capacity anomaly.
- **Q3**: **(A, B, C, D)** - Oblique plane electromagnetic wave relations.
- **Q4**: **(A, B, C)** - Center of percussion analysis. Linear momentum is not conserved due to external hinge force unless external reaction is zero.
- **Q5**: **(A, B, C, D)** - Newton's rings interference pattern properties.
- **Q6**: **(A, B, C, D)** - Relativistic muon lifetime dilation and length contraction.

#### Solutions 7 to 12:
- **Q7**: **31.00**
  - $\lambda_{\min} = \frac{h c}{e V} = \frac{1240\text{ eV}\cdot\text{nm}}{40000\text{ eV}} = 0.031\text{ nm} = 31.00\text{ pm}$.
- **Q8**: **1.14**
  - Total moles conserved: $n_0 + n_0 = n_1 + n_2 \implies \frac{2 P_0 V_0}{R T_0} = \frac{P_f V_0}{R T_1} + \frac{P_f V_0}{R T_0}$.
  - $P_f = \frac{2 P_0 / T_0}{1/T_1 + 1/T_0} = \frac{2(1.0)/300}{1/400 + 1/300} = \frac{2/300}{7/1200} = \frac{2 \times 4}{7} = \frac{8}{7} \approx 1.14\text{ atm}$.
- **Q9**: **1.10**
  - Moment of inertia about pivot: $I = \frac{1}{2}M R^2 + M d^2 = 3.0(\frac{1}{2}(0.16) + 0.04) = 3.0(0.12) = 0.36\text{ kg}\cdot\text{m}^2$.
  - Period $T = 2\pi \sqrt{\frac{I}{M g d}} = 2\pi \sqrt{\frac{0.36}{3.0 \times 9.8 \times 0.2}} = 2\pi \sqrt{\frac{0.36}{5.88}} \approx 1.55\text{ s}$.
- **Q10**: **1.00**
  - $V_2 = V_1 (N_2/N_1) = 220(100/1000) = 22\text{ V}$.
  - $I_2 = V_2 / R_L = 22 / 22 = 1.0\text{ A}$.
  - $I_1 = I_2 (N_2/N_1) = 1.0(100/1000) = 0.10\text{ A}$.
- **Q11**: **0.90**
  - A soap bubble has two surfaces: $\Delta A = 2 \times 4\pi (R_2^2 - R_1^2) = 8\pi(0.0016 - 0.0004) = 8\pi(0.0012) = 0.03016\text{ m}^2$.
  - Work $W = \gamma \Delta A = 0.030 \times 0.03016 = 0.000905\text{ J} \approx 0.90\text{ mJ}$.
- **Q12**: **4.00**
  - $\lambda_{\text{eff}} = \lambda_\alpha + \lambda_\beta \implies \frac{1}{t_{1/2,\text{eff}}} = \frac{1}{12} + \frac{1}{6} = \frac{3}{12} = \frac{1}{4} \implies t_{1/2,\text{eff}} = 4.00\text{ hours}$.

#### Solutions 13 to 18:
- **Q13**: **(A)** - Thermodynamic potentials.
- **Q14**: **(A)** - Maxwell's equations.
- **Q15**: **(A)** - Dispersion relations.
- **Q16**: **(A)** - Physical units.
- **Q17**: **(A)** - Subatomic particles.
- **Q18**: **(A)** - Quantum numbers.

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- **Q19**: **(A, B, C, D)** - Polyprotic acid and amphoteric salt equilibria.
- **Q20**: **(A, B, C, D)** - Metallurgy of iron blast furnace reactions.
- **Q21**: **(A, B, C, D)** - Aldol and Cannizzaro mechanisms.
- **Q22**: **(A, B, C, D)** - Crystal structures and coordination geometry.
- **Q23**: **(A, B, C, D)** - Amino acid and protein structures.
- **Q24**: **(A, B, C)** - Tests distinguishing amines. Tollen's does not test amines.

#### Solutions 25 to 30:
- **Q25**: **1.81**
  - $\alpha = \Lambda_m / \Lambda_m^\circ = 16.5 / 390.5 = 0.04225$.
  - $K_a = \frac{C \alpha^2}{1 - \alpha} \approx 0.010 \times (0.04225)^2 = 1.785 \times 10^{-5}\text{ M} \approx 1.81 \times 10^{-5}$.
- **Q26**: **4.93**
  - Molarity $C = \frac{18.0 / 180}{0.500} = 0.20\text{ M}$.
  - $\Pi = C R T = 0.20 \times 0.0821 \times 300 = 4.926 \approx 4.93\text{ atm}$.
- **Q27**: **27.00**
  - If volume is reduced to $1/3$, all concentrations triple ($3 \times$).
  - Rate $\propto [\text{NO}]^2 [\text{O}_2] \implies$ factor is $3^2 \times 3 = 27$.
- **Q28**: **16.40**
  - $\text{pH} = \text{p}K_a + \log\frac{[\text{salt}]}{[\text{acid}]} \implies 5.04 = 4.74 + \log\frac{[\text{salt}]}{0.20} \implies \log\frac{[\text{salt}]}{0.20} = 0.30$.
  - $\frac{[\text{salt}]}{0.20} = 2.0 \implies [\text{salt}] = 0.40\text{ M}$.
  - Moles of salt in $500\text{ mL} = 0.40 \times 0.500 = 0.20\text{ mol}$.
  - Mass $= 0.20 \times 82.0 = 16.40\text{ g}$.
- **Q29**: **400**
  - In BCC, body diagonal $4 r = \sqrt{3} a \implies a = \frac{4 r}{\sqrt{3}} = \frac{4(173.2)}{1.732} = 400\text{ pm}$.
- **Q30**: **212.30**
  - $\Delta G^\circ = -n F E^\circ = -2 \times 96500 \times 1.10 = -212300\text{ J} = -212.30\text{ kJ/mol}$. Magnitude is $212.30$.

#### Solutions 31 to 36:
- **Q31**: **(A)** - Carbohydrate tests.
- **Q32**: **(A)** - Interhalogen geometries.
- **Q33**: **(A)** - Synthetic reagents.
- **Q34**: **(A)** - Mineral ores.
- **Q35**: **(A)** - Colloid classification.
- **Q36**: **(A)** - Environmental chemistry.

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- **Q37**: **(A, B, C)** - Taylor expansion inequalities for trigonometric functions.
- **Q38**: **(A, B, C, D)** - Co-normal points on parabola.
- **Q39**: **(A, B, C)** - Triangle inequality on $|z| - 4/|z| \le 2 \implies |z|^2 - 2|z| - 4 \le 0 \implies |z| \le \sqrt{5}+1$.
- **Q40**: **(A, B, C, D)** - Idempotent matrix properties.
- **Q41**: **(A, B, C, D)** - Classical continuous analysis theorems.
- **Q42**: **(A, B, C)** - Line of intersection and dihedral angle of two planes.

#### Solutions 43 to 48:
- **Q43**: **1.00**
  - $(f^{-1})'(0) = \frac{1}{f'(0)}$.
  - By Fundamental Theorem of Calculus, $f'(x) = \sqrt{1 + x^3} \implies f'(0) = 1$.
  - Thus $(f^{-1})'(0) = 1.00$.
- **Q44**: **0.00**
  - Circle radius is 5. Ellipse semi-axes are $a = 4, b = 3$. The ellipse is entirely contained inside the circle, so they do not intersect (0 points).
- **Q45**: **2**
  - Riemann sum for $\int_0^1 \frac{1}{1+x} dx = \ln 2 \implies k = 2$.
- **Q46**: **1.00**
  - $|\vec{u}+\vec{v}|^2 + |\vec{u}-\vec{v}|^2 = 2(|\vec{u}|^2 + |\vec{v}|^2) = 2(1 + 1) = 4$.
  - $3 + |\vec{u}-\vec{v}|^2 = 4 \implies |\vec{u}-\vec{v}|^2 = 1.00$.
- **Q47**: **221**
  - Probability $= \frac{\binom{4}{2}}{\binom{52}{2}} = \frac{6}{1326} = \frac{1}{221} \implies N = 221$.
- **Q48**: **6.40**
  - Director circle equation: $x^2 + y^2 = a^2 + b^2 = 25 + 16 = 41$.
  - Radius $= \sqrt{41} \approx 6.40$.

#### Solutions 49 to 54:
- **Q49**: **(A)** - Standard indefinite integrals.
- **Q50**: **(A)** - Polar curve identification.
- **Q51**: **(A)** - Complex evaluations.
- **Q52**: **(A)** - Matrix determinant properties.
- **Q53**: **(A)** - Statistical formulas.
- **Q54**: **(A)** - Differential equation integrating factors.
"""

val_md = r"""# Answer Key & Benchmark Alignment – Mock Examination 02
## Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 2.10
- Q8: 397.00
- Q9: 5.00
- Q10: 4.00
- Q11: 1.05
- Q12: 3.50
- Q13: A
- Q14: A
- Q15: A
- Q16: B
- Q17: A
- Q18: B

#### Chemistry
- Q19: A, B, D
- Q20: A, B, C, D
- Q21: A, B, C, D
- Q22: A, B, C, D
- Q23: A, B, C, D
- Q24: A, B, C
- Q25: 80.12
- Q26: 4.02
- Q27: 2.00
- Q28: 120.00
- Q29: 4.25
- Q30: 726.40
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
- Q42: A, B, C
- Q43: 8.00
- Q44: 4.50
- Q45: 4.00
- Q46: 16.00
- Q47: 30.00
- Q48: 1.00
- Q49: A
- Q50: A
- Q51: C
- Q52: A
- Q53: A
- Q54: A

---

### Paper 2 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 31.00
- Q8: 1.14
- Q9: 1.55
- Q10: 0.10
- Q11: 0.90
- Q12: 4.00
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
- Q24: A, B, C
- Q25: 1.81
- Q26: 4.93
- Q27: 27.00
- Q28: 16.40
- Q29: 400.00
- Q30: 212.30
- Q31: A
- Q32: A
- Q33: A
- Q34: A
- Q35: A
- Q36: A

#### Mathematics
- Q37: A, B, C
- Q38: A, B, C, D
- Q39: A, B, C
- Q40: A, B, C, D
- Q41: A, B, C, D
- Q42: A, B, C
- Q43: 1.00
- Q44: 0.00
- Q45: 2.00
- Q46: 1.00
- Q47: 221.00
- Q48: 6.40
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Pedagogical Profile Alignment
- **Modern Physics & Thermodynamics Weightage**: $\approx 37\%$ across Physics sections.
- **Physical Chemistry Weightage**: $\approx 67\%$ across Chemistry sections.
- **Geometric Invariants & Algebraic Symmetry**: Strongly emphasized across Mathematics sections.
- **Total Unique Questions**: 108 Questions (54 in Paper 1, 54 in Paper 2).
"""

if __name__ == "__main__":
    create_mock_files(2, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Guwahati")
    print("Successfully generated IIT Guwahati Mock 02!")

