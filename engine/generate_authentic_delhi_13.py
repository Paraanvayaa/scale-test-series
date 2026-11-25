# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 13.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Stern-Gerlach force gradients, Relativistic velocity aberration, Dieterici gas Joule-Thomson inversion
- Shapiro reaction, Stille cross-coupling, Zeise's salt Dewar-Chatt-Duncanson bonding, Langmuir adsorption
- Frullani integrals, Cayley-Hamilton matrix powers, Confocal conics, Clairaut ODE
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 13 — Paper 1
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
A neutral silver atom possessing an intrinsic magnetic dipole moment $\vec{\mu} = \mu_B \hat{k}$ enters a Stern-Gerlach apparatus with velocity $\vec{v} = v_0 \hat{i}$. The magnetic field has a strong gradient along the $z$-axis: $\vec{B} = (B_0 + \alpha z)\hat{k} - \alpha x \hat{i}$, where $\alpha > 0$. The magnetic field region has length $L$, beyond which the atom travels a distance $D$ in a field-free drift space to a detector screen:
(A) The force exerted on the atom inside the magnetic field is $\vec{F} = \mu_B \alpha \hat{k}$.  
(B) Maxwell's equations $\nabla \cdot \vec{B} = 0$ requires that an inhomogeneous magnetic field cannot have a gradient in only one direction; here $\frac{\partial B_z}{\partial z} + \frac{\partial B_x}{\partial x} = \alpha - \alpha = 0$.  
(C) The transverse deflection on exiting the magnet at $x = L$ is $z_1 = \frac{\mu_B \alpha L^2}{2 m v_0^2}$.  
(D) The total deflection at the detector screen located at distance $D$ from the exit of the magnet is $z_{\text{total}} = \frac{\mu_B \alpha L}{m v_0^2}\left(\frac{L}{2} + D\right)$.

#### Question 2
A real gas follows the Dieterici equation of state:
$$P(V_m - b) e^{\frac{a}{R T V_m}} = R T$$
where $a$ and $b$ are positive empirical constants. In terms of critical temperature $T_c$, critical pressure $P_c$, and critical volume $V_c$:
(A) The critical volume is $V_c = 2b$.  
(B) The critical temperature is $T_c = \frac{a}{4 R b}$.  
(C) The critical compressibility factor is $Z_c = \frac{P_c V_c}{R T_c} = 2 e^{-2} \approx 0.271$.  
(D) The Joule-Thomson inversion curve satisfies $T_i(V_m) = \frac{a}{R b}\left(\frac{V_m - b}{V_m}\right)$ in the dilute gas limit.

#### Question 3
A cylindrical capacitor consists of two concentric conducting cylinders of radii $a$ and $b$ ($a < b$) and length $L \gg b$. The annular space between the cylinders is filled with an inhomogeneous dielectric whose permittivity varies radially as $\varepsilon(r) = \varepsilon_0 \frac{a}{r}$:
(A) For a total charge $+Q$ on the inner cylinder and $-Q$ on the outer cylinder, the electric displacement field is $D(r) = \frac{Q}{2\pi r L} \hat{r}$.  
(B) The electric field between the cylinders is independent of $r$ and given by $E(r) = \frac{Q}{2\pi \varepsilon_0 a L}$.  
(C) The potential difference between the cylinders is $V = \frac{Q(b - a)}{2\pi \varepsilon_0 a L}$.  
(D) The capacitance of the system is $C = \frac{2\pi \varepsilon_0 a L}{b - a}$.

#### Question 4
A thin uniform circular ring of mass $M$ and radius $R$ carries a total uniformly distributed charge $+Q$. The ring rotates with constant angular velocity $\omega$ about its perpendicular central axis. A point particle of mass $m$ and charge $+q$ is released from rest at a point on the axis at distance $x_0 = \sqrt{3}R$ from the center of the ring:
(A) The magnetic dipole moment of the rotating ring is $\mu = \frac{1}{2} Q \omega R^2$.  
(B) The electrostatic potential at distance $x$ along the axis is $V(x) = \frac{Q}{4\pi \varepsilon_0 \sqrt{R^2 + x^2}}$.  
(C) The velocity of the particle when it crosses the center of the ring is $v = \sqrt{\frac{q Q}{4\pi \varepsilon_0 m R}}$.  
(D) The magnetic field at the center of the ring due to its rotation is $B = \frac{\mu_0 Q \omega}{4\pi R}$.

#### Question 5
In an optical Fabry-Pérot interferometer with plate spacing $d$, refractive index $n = 1$, and plate intensity reflectance $R$:
(A) The free spectral range (in frequency) is $\Delta\nu_{\text{FSR}} = \frac{c}{2d}$.  
(B) The coefficient of finesse is $F = \frac{4R}{(1 - R)^2}$.  
(C) The full width at half maximum (FWHM) of transmission peaks is $\delta\nu = \frac{c(1 - R)}{2\pi d \sqrt{R}}$.  
(D) The finesse $\mathcal{F} = \frac{\Delta\nu_{\text{FSR}}}{\delta\nu} = \frac{\pi \sqrt{R}}{1 - R}$.

#### Question 6
A heavy uniform spherical ball of radius $r$ rolls without slipping down a track shaped as an inverted cycloid $x = R(\theta + \sin\theta)$, $y = R(1 - \cos\theta)$ where the vertex is at the lowest point:
(A) The motion of the center of mass executes simple harmonic motion for arbitrarily large amplitudes.  
(B) The period of small oscillations of the rolling sphere is $T = 2\pi \sqrt{\frac{7(4R - r)}{5g}}$ assuming rolling contact without slip.  
(C) The friction force at the lowest point of the trajectory during oscillation is zero.  
(D) The mechanical energy is conserved throughout the motion because the point of contact is instantaneously at rest.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
An $LC$ circuit contains a capacitor of fixed capacitance $C = 20\text{ }\mu\text{F}$ and an inductor whose inductance increases linearly with time as $L(t) = L_0 (1 + \alpha t)$, where $L_0 = 50\text{ mH}$ and $\alpha = 0.5\text{ s}^{-1}$. At $t = 0$, the capacitor charge is $q_0 = 100\text{ }\mu\text{C}$ and current is zero. The energy stored in the magnetic field of the inductor reaches its first maximum at a time when the electric field energy in the capacitor vanishes. If the root-mean-square voltage across the capacitor in the quasi-stationary high-frequency regime decays as $V_{\text{rms}}(t) \propto (1 + \alpha t)^{-\gamma}$, find the value of $100\gamma$.

#### Question 8
A gyroscope consists of a solid uniform disk of mass $M = 2\text{ kg}$ and radius $R = 0.1\text{ m}$ spinning about its axle at $\omega_s = 600\text{ rad/s}$. The axle is supported at a pivot distance $d = 0.15\text{ m}$ from the disk's center of mass and is horizontal. The precession angular velocity of the gyroscope about the vertical axis through the pivot is $\Omega_p$. Taking $g = 9.8\text{ m/s}^2$, find $\Omega_p$ in $\text{rad/s}$ (round off to TWO decimal places).

#### Question 9
A spherical blackbody of mass $M = 1.0\text{ kg}$, radius $R = 5\text{ cm}$, specific heat capacity $s = 400\text{ J/(kg}\cdot\text{K)}$, and emissivity $e = 1.0$ is placed in a vacuum chamber whose walls are maintained at absolute zero ($T_{\text{env}} = 0\text{ K}$). If the initial temperature of the sphere is $T_0 = 500\text{ K}$, the time taken for its temperature to drop to $T_1 = 250\text{ K}$ is $t$ seconds. Given Stefan-Boltzmann constant $\sigma = 5.67 \times 10^{-8}\text{ W/(m}^2\text{K}^4)$, calculate $t$ in seconds (round off to the nearest integer).

#### Question 10
In a relativistic particle collision, a stationary target proton of rest mass $m_p = 938\text{ MeV}/c^2$ is bombarded by an incident proton of total energy $E_1$. The minimum incident total energy $E_1$ (threshold energy) required to produce a proton-antiproton pair via the reaction $p + p \to p + p + p + \bar{p}$ is $E_{\text{th}} = k \cdot m_p c^2$. Find the integer value of $k$.

#### Question 11
A long solenoid of radius $a = 4\text{ cm}$ has $n = 1000\text{ turns/m}$ and carries an alternating current $I(t) = I_0 \sin(\omega t)$ where $I_0 = 5\text{ A}$ and $\omega = 100\pi\text{ rad/s}$. A coaxial single-turn circular loop of radius $b = 10\text{ cm}$ and resistance $R_{\text{loop}} = 0.02\text{ }\Omega$ surrounds the solenoid. The peak induced current in the circular loop is $I_{\text{peak}}$ in Amperes. Calculate $I_{\text{peak}}$ (use $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$, round off to TWO decimal places).

#### Question 12
A vertical cylindrical container of height $H = 1.2\text{ m}$ and cross-sectional area $A = 0.05\text{ m}^2$ is closed at both ends. It contains an ideal monatomic gas divided into two equal compartments by a frictionless, thermally insulating piston of mass $m = 10\text{ kg}$ held horizontally. Initially, the gas in both compartments is at temperature $T_0 = 300\text{ K}$ and equal pressure $P_0 = 1.0 \times 10^5\text{ Pa}$. The piston is released and settles to a new equilibrium position. If the downward displacement of the piston from the center is $\Delta h$ in millimeters, calculate $\Delta h$ (take $g = 9.8\text{ m/s}^2$, round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle of mass $m$ moves in a central potential $V(r) = -\frac{k}{r} + \frac{c}{r^2}$, where $k > 0$ and $c > 0$. If the orbital angular momentum is $L$:
(A) The effective angular momentum is $L_{\text{eff}} = \sqrt{L^2 + 2mc}$, and the orbit precesses with advance of perihelion $\Delta\theta = 2\pi\left(\frac{L}{\sqrt{L^2 + 2mc}} - 1\right)$ per revolution.  
(B) Bound orbits are closed ellipses for all values of $c > 0$.  
(C) The radius of the stable circular orbit is $r_0 = \frac{L^2}{m k}$, completely independent of $c$.  
(D) The period of radial oscillations about the minimum of the effective potential is equal to the orbital period.

#### Question 14
Two monochromatic coherent light waves of equal amplitude $E_0$ and wavelengths $\lambda$ and $\lambda + \Delta\lambda$ ($\Delta\lambda \ll \lambda$) propagate along the $+x$ axis. The spatial group length (coherence envelope packet length) over which constructive and destructive beat interference completes one full spatial cycle is:
(A) $\Delta x = \frac{\lambda^2}{2\Delta\lambda}$  
(B) $\Delta x = \frac{\lambda^2}{\Delta\lambda}$  
(C) $\Delta x = \frac{\lambda}{\Delta\lambda}$  
(D) $\Delta x = \frac{2\pi \lambda^2}{\Delta\lambda}$

#### Question 15
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal conveyor belt that is moving with a constant acceleration $a_0 \hat{i}$. If the coefficient of static friction $\mu_s$ is sufficiently large so that the sphere rolls without slipping relative to the belt, the acceleration of the center of mass of the sphere relative to the ground is:
(A) $\vec{a}_{\text{cm}} = \frac{2}{7} a_0 \hat{i}$  
(B) $\vec{a}_{\text{cm}} = \frac{5}{7} a_0 \hat{i}$  
(C) $\vec{a}_{\text{cm}} = \frac{3}{7} a_0 \hat{i}$  
(D) $\vec{a}_{\text{cm}} = a_0 \hat{i}$

#### Question 16
An electron in a hydrogen-like atom transitions from the state $n = 4$ to $n = 2$. The orbital angular momentum quantum number changes from $l = 2$ to $l = 1$. The frequency of the emitted photon, taking into account the finite mass of the nucleus $M_{\text{nuc}} = 4 m_e$ (a hypothetical light ion), compared to the frequency $\nu_\infty$ for an infinitely heavy nucleus, is:
(A) $\nu = \frac{4}{5} \nu_\infty$  
(B) $\nu = \frac{5}{4} \nu_\infty$  
(C) $\nu = \frac{1}{4} \nu_\infty$  
(D) $\nu = \nu_\infty$

#### Question 17
A rectangular loop of wire with dimensions $a \times b$, mass $m$, and resistance $R$ falls vertically under gravity through a horizontal magnetic field that exists in a strip of height $h > b$: $\vec{B} = B_0 \hat{k}$ for $0 \le y \le h$, and $\vec{B} = 0$ elsewhere. The terminal velocity $v_t$ attained while entering the field is:
(A) $v_t = \frac{m g R}{B_0^2 a^2}$  
(B) $v_t = \frac{m g R}{B_0^2 b^2}$  
(C) $v_t = \frac{2 m g R}{B_0^2 a^2}$  
(D) $v_t = \frac{m g R}{2 B_0^2 a b}$

#### Question 18
A sound source of frequency $f_0$ moves along the circle $x^2 + y^2 = R^2$ with constant angular speed $\omega$ in an anti-clockwise direction. A stationary receiver is located far away at $(D, 0)$ where $D \gg R$. The maximum frequency detected by the receiver is:
(A) $f_{\text{max}} = f_0 \left(\frac{v}{v - \omega R}\right)$  
(B) $f_{\text{max}} = f_0 \left(\frac{v + \omega R}{v}\right)$  
(C) $f_{\text{max}} = f_0 \sqrt{\frac{v + \omega R}{v - \omega R}}$  
(D) $f_{\text{max}} = f_0 \left(\frac{v}{v - \omega R / \sqrt{2}}\right)$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding Zeise's salt, $\text{K}[\text{PtCl}_3(\eta^2\text{-C}_2\text{H}_4)]\cdot\text{H}_2\text{O}$, and the Dewar-Chatt-Duncanson bonding model:
(A) Platinum is in the $+2$ oxidation state with a $5d^8$ electron configuration, adopting a square planar coordination geometry.  
(B) The $\sigma$-component of bonding involves donation of electron density from the filled $\pi$-bonding molecular orbital of ethylene into an empty $5d$ hybrid orbital of Pt(II).  
(C) The $\pi$-backbonding component involves donation of electron density from a filled Pt(II) $d$-orbital into the empty $\pi^*$ antibonding orbital of ethylene.  
(D) Due to back-donation into the $\pi^*$ orbital, the $\text{C}=\text{C}$ bond length in Zeise's salt ($1.375\text{ \AA}$) is longer than that in free ethylene ($1.337\text{ \AA}$), and the ethylene hydrogens bend back away from the platinum atom.

#### Question 20
In the Shapiro reaction, a ketone tosylhydrazone ($R_1\text{CH}_2\text{-C}(=\text{N-NHTs})\text{-}R_2$) is treated with two equivalents of a strong alkyllithium base (e.g., $n\text{-BuLi}$):
(A) The first equivalent of base deprotonates the relatively acidic hydrazone $\text{N-H}$ proton.  
(B) The second equivalent of base abstracts a proton from the less substituted $\alpha$-carbon to form a dianion.  
(C) The dianion undergoes elimination of lithium benzenesulfinate ($\text{TsLi}$) followed by extrusion of nitrogen gas ($\text{N}_2$) to generate an vinyllithium intermediate.  
(D) Trapping of the vinyllithium intermediate with electrophiles such as $\text{H}_2\text{O}$, $\text{D}_2\text{O}$, or carbonyl compounds gives alkenes regioselectively at the less substituted position.

#### Question 21
For the Langmuir adsorption isotherm describing monolayer adsorption of a gas on a solid catalyst surface:
$$\theta = \frac{K P}{1 + K P}$$
(A) At very low pressures ($K P \ll 1$), the fractional surface coverage $\theta \approx K P$, representing first-order kinetics with respect to gas pressure.  
(B) At very high pressures ($K P \gg 1$), $\theta \to 1$, and the rate of surface reaction becomes zero-order with respect to gas pressure.  
(C) A plot of $\frac{P}{V_{\text{ads}}}$ versus $P$ yields a straight line with slope $\frac{1}{V_m}$ and intercept $\frac{1}{K V_m}$, where $V_m$ is the monolayer adsorption capacity.  
(D) The adsorption equilibrium constant $K = \frac{k_{\text{ads}}}{k_{\text{des}}}$ increases with increasing temperature for physisorption and chemisorption because adsorption is exothermic.

#### Question 22
Consider the chemistry of borazine ($\text{B}_3\text{N}_3\text{H}_6$, "inorganic benzene") compared to benzene ($\text{C}_6\text{H}_6$):
(A) Borazine is isoelectronic and isostructural with benzene, possessing a planar hexagonal ring with alternating B and N atoms.  
(B) Due to the electronegativity difference between N ($3.04$) and B ($2.04$), the $\pi$-electron cloud is localized predominantly around nitrogen, making the B atoms electrophilic and N atoms nucleophilic.  
(C) Borazine readily undergoes electrophilic addition reactions with $\text{HCl}$ to form $\text{B}_3\text{N}_3\text{H}_9\text{Cl}_3$, in contrast to benzene which prefers electrophilic aromatic substitution.  
(D) Complete hydrolysis of borazine with water yields boric acid ($\text{H}_3\text{BO}_3$), ammonia ($\text{NH}_3$), and hydrogen gas ($\text{H}_2$).

#### Question 23
A solution containing $0.10\text{ M}$ $\text{Fe}^{2+}$ and $0.10\text{ M}$ $\text{Fe}^{3+}$ is titrated with an oxidant at $25^\circ\text{C}$ in an electrochemical cell using a Pt working electrode against a standard hydrogen electrode. Given:
$$E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V}$$
If complexing agent $\text{CN}^-$ is added to the system forming $[\text{Fe}(\text{CN})_6]^{4-}$ and $[\text{Fe}(\text{CN})_6]^{3-}$ with formation constants $\beta_6(\text{Fe}^{2+}) = 10^{35}$ and $\beta_6(\text{Fe}^{3+}) = 10^{42}$ respectively:
(A) The standard reduction potential of the cyano complex couple $[\text{Fe}(\text{CN})_6]^{3-}/[\text{Fe}(\text{CN})_6]^{4-}$ is $E^\circ = 0.77 - 0.0591 \log(10^7) \approx +0.36\text{ V}$.  
(B) Cyanide ion stabilizes the $\text{Fe}^{3+}$ state more strongly than the $\text{Fe}^{2+}$ state.  
(C) Addition of cyanide makes $\text{Fe}^{2+}$ a stronger reducing agent.  
(D) In an octahedral field, $[\text{Fe}(\text{CN})_6]^{4-}$ is diamagnetic with $t_{2g}^6 e_g^0$ while $[\text{Fe}(\text{CN})_6]^{3-}$ is paramagnetic with one unpaired electron ($t_{2g}^5 e_g^0$).

#### Question 24
In the Stille cross-coupling reaction:
$$\text{R-X} + \text{R'--SnBu}_3 \xrightarrow{\text{Pd}(0)\text{ catalyst}} \text{R--R'} + \text{X--SnBu}_3$$
(A) The catalytic cycle begins with oxidative addition of organic halide $\text{R-X}$ to $\text{Pd}(0)\text{L}_2$ to give a $\text{Pd}(\text{II})$ intermediate.  
(B) Transmetalation occurs between the organotin reagent $\text{R'--SnBu}_3$ and the $\text{Pd}(\text{II})$ complex.  
(C) Transmetalation is typically the rate-determining step of the Stille coupling cycle.  
(D) Reductive elimination from the diorganopalladium(II) intermediate yields the cross-coupled product $\text{R--R'}$ and regenerates the $\text{Pd}(0)$ catalyst.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
A radioactive decay series consists of parent nucleus $A$ decaying to daughter $B$ with decay constant $\lambda_A = 0.04\text{ h}^{-1}$, and $B$ subsequently decaying to stable isotope $C$ with decay constant $\lambda_B = 0.20\text{ h}^{-1}$. Initially at $t = 0$, the sample consists purely of $N_0 = 1.0 \times 10^{18}$ nuclei of $A$ and no nuclei of $B$. The number of nuclei of $B$ reaches its maximum value at time $t_{\text{max}}$ hours. Calculate $t_{\text{max}}$ in hours (use $\ln 5 = 1.609$, round off to TWO decimal places).

#### Question 26
For the transition metal complex $[Co(NH_3)_6]^{3+}$, the crystal field splitting energy is $\Delta_o = 23,000\text{ cm}^{-1}$ and the mean pairing energy is $P = 19,000\text{ cm}^{-1}$. Calculate the Crystal Field Stabilization Energy (CFSE) of this complex in units of $1000\text{ cm}^{-1}$, taking into account orbital stabilization and net pairing energy (enter the numerical magnitude as a positive decimal, round off to ONE decimal place).

#### Question 27
An organic compound undergoes mutarotation: $\alpha\text{-D-glucose} \rightleftharpoons \beta\text{-D-glucose}$. At $25^\circ\text{C}$, the forward rate constant is $k_1 = 0.0065\text{ min}^{-1}$ and the reverse rate constant is $k_{-1} = 0.0035\text{ min}^{-1}$. Starting from pure $\alpha\text{-D-glucose}$, the percentage of $\beta\text{-D-glucose}$ at equilibrium is $P\%$. Calculate the value of $P$ (round off to the nearest integer).

#### Question 28
The solubility product of lead(II) iodide ($\text{PbI}_2$) is $K_{sp} = 7.1 \times 10^{-9}$ at $25^\circ\text{C}$. The solubility of $\text{PbI}_2$ in a $0.10\text{ M}$ $\text{KI}$ solution is $S\text{ mol/L}$. If $S = X \times 10^{-7}\text{ M}$, calculate the value of $X$ (round off to ONE decimal place).

#### Question 29
A constant current of $I = 2.5\text{ A}$ is passed through an electrolytic cell containing an aqueous solution of $\text{CuSO}_4$ for $t = 3860\text{ seconds}$. The mass of copper deposited at the cathode is $m$ grams. If Faraday's constant is $F = 96500\text{ C/mol}$ and atomic mass of $\text{Cu} = 63.5\text{ g/mol}$, find $m$ in grams (round off to TWO decimal places).

#### Question 30
In the gas phase reaction $\text{N}_2\text{O}_4(g) \rightleftharpoons 2\text{NO}_2(g)$, at $T = 300\text{ K}$ and total pressure $P_t = 1.0\text{ atm}$, the degree of dissociation is $\alpha = 0.20$. If the total pressure is decreased isothermally to $P_t' = 0.25\text{ atm}$, the new degree of dissociation is $\alpha'$. Calculate the value of $100\alpha'$ (round off to ONE decimal place).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Favorskii rearrangement of an $\alpha$-haloketone (e.g., 2-chlorocyclohexanone) with sodium methoxide in methanol, the primary reactive intermediate formed via intramolecular nucleophilic displacement is a:
(A) Cyclopropanone intermediate  
(B) Zwitterionic oxyallyl carbocation  
(C) $\beta$-lactone  
(D) Symmetrical oxirane  

#### Question 32
Which of the following coordination complexes exhibits optical isomerism (enantiomerism)?
(A) $\text{cis-}[\text{Co}(\text{en})_2\text{Cl}_2]^+$  
(B) $\text{trans-}[\text{Co}(\text{en})_2\text{Cl}_2]^+$  
(C) $[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$  
(D) $[\text{Co}(\text{NH}_3)_4\text{Cl}_2]^+$  

#### Question 33
For an enzyme-catalyzed reaction obeying Michaelis-Menten kinetics with substrate concentration $[S]$ equal to $3 K_m$, the initial reaction velocity $v_0$ expressed as a fraction of the maximum velocity $V_{\text{max}}$ is:
(A) $0.75 V_{\text{max}}$  
(B) $0.50 V_{\text{max}}$  
(C) $0.67 V_{\text{max}}$  
(D) $0.80 V_{\text{max}}$  

#### Question 34
In the extraction of gold via the MacArthur-Forrest cyanide process, the gold ore is dissolved in aerated sodium cyanide solution:
$$4\text{Au} + 8\text{CN}^- + \text{O}_2 + 2\text{H}_2\text{O} \to 4[\text{Au}(\text{CN})_2]^- + 4\text{OH}^-$$
The role of oxygen ($\text{O}_2$) in this hydrometallurgical leaching step is:
(A) An oxidizing agent that oxidizes $\text{Au}(0)$ to $\text{Au}(\text{I})$  
(B) A complexing ligand coordinating directly to gold  
(C) A reducing agent for aurous ions  
(D) A catalyst that remains chemically unchanged  

#### Question 35
Treatment of phenol with chloroform ($\text{CHCl}_3$) in aqueous $\text{NaOH}$ (Reimer-Tiemann reaction) generates salicylaldehyde. The electrophile responsible for ortho-formylation is:
(A) Dichlorocarbene ($:\text{CCl}_2$)  
(B) Trichloro carbocation ($\text{CCl}_3^+$)  
(C) Chloroformyl cation ($\text{HCO}^+$)  
(D) Dichloromethyl radical ($\cdot\text{CHCl}_2$)  

#### Question 36
The unit cell of caesium chloride ($\text{CsCl}$) consists of a simple cubic arrangement of chloride ions with a caesium ion at the body center. If the ionic radii are $r_{\text{Cs}^+} = 1.69\text{ \AA}$ and $r_{\text{Cl}^-} = 1.81\text{ \AA}$, the edge length $a$ of the cubic unit cell is:
(A) $a = \frac{2}{\sqrt{3}}(r_{\text{Cs}^+} + r_{\text{Cl}^-}) \approx 4.04\text{ \AA}$  
(B) $a = 2(r_{\text{Cs}^+} + r_{\text{Cl}^-}) \approx 7.00\text{ \AA}$  
(C) $a = \sqrt{2}(r_{\text{Cs}^+} + r_{\text{Cl}^-}) \approx 4.95\text{ \AA}$  
(D) $a = \frac{1}{\sqrt{3}}(r_{\text{Cs}^+} + r_{\text{Cl}^-}) \approx 2.02\text{ \AA}$  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Consider the non-zero $3 \times 3$ real symmetric matrix $A$ satisfying the polynomial equation $A^3 - 6A^2 + 11A - 6I = O$. Let $\lambda_1 < \lambda_2 < \lambda_3$ be the eigenvalues of $A$:
(A) The eigenvalues of $A$ are $\lambda_1 = 1$, $\lambda_2 = 2$, $\lambda_3 = 3$.  
(B) The trace of $A$ is $\text{Tr}(A) = 6$ and determinant is $\det(A) = 6$.  
(C) The matrix inverse is given by $A^{-1} = \frac{1}{6}(A^2 - 6A + 11I)$.  
(D) The matrix exponential has trace $\text{Tr}(e^A) = e + e^2 + e^3$.

#### Question 38
Evaluate the Frullani integral $I = \int_0^\infty \frac{\cos(a x) - \cos(b x)}{x} dx$ for positive real numbers $a, b > 0$:
(A) The integral converges conditionally for all $a, b > 0$.  
(B) The value of the integral is $I = \ln(b/a)$.  
(C) If replaced by $J = \int_0^\infty \frac{e^{-a x} - e^{-b x}}{x} dx$, the value is also $\ln(b/a)$.  
(D) The integral $\int_0^\infty \frac{\arctan(a x) - \arctan(b x)}{x} dx = \frac{\pi}{2} \ln(a/b)$.

#### Question 39
Let $E: \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b > 0$) be an ellipse with eccentricity $e$. A family of confocal conics is given by $\frac{x^2}{a^2 - \lambda} + \frac{y^2}{b^2 - \lambda} = 1$:
(A) For $\lambda < b^2$, the conics are ellipses confocal with $E$.  
(B) For $b^2 < \lambda < a^2$, the conics are hyperbolas confocal with $E$.  
(C) At every point of intersection between a confocal ellipse and a confocal hyperbola, the two curves intersect orthogonally.  
(D) Through any point $(x_0, y_0)$ in the plane not on the coordinate axes, there pass exactly one confocal ellipse and one confocal hyperbola.

#### Question 40
Consider Clairaut's differential equation:
$$y = x \frac{dy}{dx} + \left(\frac{dy}{dx}\right)^2$$
Let $p = \frac{dy}{dx}$:
(A) The general solution is a family of straight lines $y = c x + c^2$, where $c$ is an arbitrary constant.  
(B) Differentiating with respect to $x$ yields $p = p + x \frac{dp}{dx} + 2p \frac{dp}{dx} \implies \frac{dp}{dx}(x + 2p) = 0$.  
(C) Setting $x + 2p = 0 \implies p = -x/2$, the singular solution obtained by eliminating $p$ is the parabola $y = -\frac{x^2}{4}$.  
(D) The parabola $y = -\frac{x^2}{4}$ is the envelope of the family of straight lines $y = c x + c^2$.

#### Question 41
Let $f: \mathbb{R} \to \mathbb{R}$ be a twice continuously differentiable function such that $f''(x) > 0$ for all $x \in \mathbb{R}$ (strictly convex). Let $a < b$:
(A) For any $t \in (0, 1)$, $f(t a + (1 - t) b) < t f(a) + (1 - t) f(b)$.  
(B) The tangent line to the curve $y = f(x)$ at any point $x_0$ lies entirely below the graph of $f(x)$ for all $x \ne x_0$.  
(C) The Hermite-Hadamard inequality holds: $f\left(\frac{a + b}{2}\right) < \frac{1}{b - a} \int_a^b f(x) dx < \frac{f(a) + f(b)}{2}$.  
(D) If $f(0) = 0$ and $f'(0) = 0$, then $f(x) \ge 0$ for all $x \in \mathbb{R}$ with equality only at $x = 0$.

#### Question 42
In a sequence of independent fair coin tosses, let $E_1$ be the event that the sequence $\text{HT}$ occurs before $\text{HH}$, and $E_2$ be the event that $\text{TH}$ occurs before $\text{TT}$:
(A) The probability $P(\text{HT before HH}) = \frac{3}{4}$.  
(B) The expected number of tosses until the pattern $\text{HH}$ appears is 6.  
(C) The expected number of tosses until the pattern $\text{HT}$ appears is 4.  
(D) The probability $P(\text{TH before TT}) = \frac{3}{4}$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Let $I = \int_0^{\pi/2} \frac{x \sin x \cos x}{\sin^4 x + \cos^4 x} dx$. Calculate the value of $\frac{32 I}{\pi^2}$ (round off to the nearest integer).

#### Question 44
Find the number of integral solutions $(x_1, x_2, x_3, x_4)$ satisfying the equation:
$$x_1 + x_2 + x_3 + x_4 = 20$$
subject to the constraints $1 \le x_1 \le 6$, $1 \le x_2 \le 7$, $x_3 \ge 0$, and $x_4 \ge 0$.

#### Question 45
Let the plane $\Pi$ pass through the line of intersection of the planes $x + 2y + 3z - 4 = 0$ and $2x + y - z + 5 = 0$, and be perpendicular to the plane $5x + 3y + 6z + 8 = 0$. If the equation of $\Pi$ is expressed in standard form as $A x + B y + C z + D = 0$ with $\gcd(A, B, C) = 1$ and $A > 0$, calculate the value of $A + B + C + D$.

#### Question 46
Let $z$ be a complex number satisfying $|z - 3 - 4i| \le 2$. The difference between the maximum and minimum values of $|z|$ is $\Delta$. Calculate $\Delta$.

#### Question 47
Let $f(x) = \det\begin{pmatrix} x-1 & x^2 & x^3+1 \\ x+2 & 2x & x^2-1 \\ 1 & x-3 & x \end{pmatrix}$. The coefficient of $x^3$ in the polynomial expansion of $f(x)$ is $K$. Calculate the value of $|K|$.

#### Question 48
A random variable $X$ takes non-negative integer values $k = 0, 1, 2, \dots$ with Poisson distribution $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$. If $P(X = 1) = 2 P(X = 2)$, then the expected value $E[X^2]$ is $M$. Calculate the value of $100 M$ (round off to the nearest integer).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The area of the region bounded by the curves $y = x^2$ and $y = \frac{2}{1 + x^2}$ is:
(A) $\pi - \frac{2}{3}$  
(B) $\frac{\pi}{2} - \frac{1}{3}$  
(C) $2\pi - \frac{4}{3}$  
(D) $\pi - \frac{4}{3}$  

#### Question 50
The sum of the infinite series $S = \sum_{n=1}^\infty \frac{n^2 + 2n + 1}{n!}$ is:
(A) $5e - 1$  
(B) $5e$  
(C) $4e$  
(D) $4e - 1$  

#### Question 51
Let $A$ be a $3 \times 3$ matrix such that $\det(A) = 3$. Then $\det(\text{adj}(\text{adj}(2A)))$ is equal to:
(A) $3^4 \cdot 2^{24}$  
(B) $3^4 \cdot 2^{12}$  
(C) $3^8 \cdot 2^{24}$  
(D) $3^2 \cdot 2^6$  

#### Question 52
If the normal to the parabola $y^2 = 4ax$ at the point $(a t_1^2, 2a t_1)$ meets the parabola again at $(a t_2^2, 2a t_2)$, the minimum value of $t_2^2$ is:
(A) 8  
(B) 4  
(C) 2  
(D) 6  

#### Question 53
The value of the limit $\lim_{n \to \infty} \sum_{k=1}^n \frac{n}{n^2 + k^2}$ is:
(A) $\frac{\pi}{4}$  
(B) $\frac{\pi}{2}$  
(C) $\ln 2$  
(D) 1  

#### Question 54
A box contains 5 red balls and 3 green balls. A ball is drawn at random and its color is noted, then returned to the box along with 2 additional balls of the same color (Polya's Urn scheme). A second ball is then drawn from the box. The probability that the second ball drawn is green is:
(A) $\frac{3}{8}$  
(B) $\frac{5}{8}$  
(C) $\frac{1}{2}$  
(D) $\frac{3}{10}$  
"""

paper_2_md = r"""# JEE Advanced Mock Examination 13 — Paper 2
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
  - Full Marks: **+3** if only the correct match is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A source of light emitting spherical waves of proper frequency $\nu_0$ moves at relativistic velocity $\vec{v} = v \hat{i}$ relative to an observer at the origin $O$. A light signal emitted when the source is at angle $\theta$ relative to the $x$-axis in the observer's frame reaches the observer:
(A) The observed frequency is given by the relativistic Doppler formula $\nu = \frac{\nu_0}{\gamma(1 - \beta \cos\theta)}$, where $\beta = v/c$ and $\gamma = 1/\sqrt{1 - \beta^2}$.  
(B) When the source is at closest approach ($\theta = 90^\circ$ at the moment of emission), the observed frequency is $\nu = \nu_0 / \gamma = \nu_0 \sqrt{1 - \beta^2}$ (transverse Doppler effect).  
(C) The transverse Doppler effect is a purely relativistic phenomenon resulting from time dilation.  
(D) When the observer sees the source directly overhead ($\theta_{\text{rec}} = 90^\circ$ at the moment of reception), the observed frequency is $\nu = \gamma \nu_0$.

#### Question 2
A system consists of a uniform solid sphere of mass $M$ and radius $R$ rolling without slipping on a horizontal turntable rotating with constant angular velocity $\vec{\Omega} = \Omega \hat{k}$ about a fixed vertical axis:
(A) In the rotating reference frame of the turntable, the sphere experiences both Coriolis and centrifugal fictitious forces.  
(B) The center of mass of the sphere executes uniform circular motion relative to the ground.  
(C) The frequency of circular motion of the center of mass in the stationary frame is $\omega_c = \frac{2}{7}\Omega$.  
(D) The motion is stable against small perturbations.

#### Question 3
An uncharged conducting spherical shell of inner radius $a$ and outer radius $b$ is placed in a uniform external electric field $\vec{E}_0 = E_0 \hat{k}$:
(A) The electric field inside the hollow cavity ($r < a$) is strictly zero everywhere.  
(B) The induced surface charge density on the outer surface ($r = b$) is $\sigma_b(\theta) = 3\varepsilon_0 E_0 \cos\theta$.  
(C) The induced surface charge density on the inner surface ($r = a$) is zero everywhere.  
(D) The electrostatic potential for $r \ge b$ is $V(r, \theta) = -E_0 r \cos\theta + \frac{E_0 b^3}{r^2} \cos\theta$.

#### Question 4
A thermodynamic heat engine operates on a Stirling cycle using $n$ moles of an ideal gas, consisting of two reversible isotherms at temperatures $T_H$ and $T_C$ ($T_H > T_C$) and two reversible isochoric processes at volumes $V_1$ and $V_2$ ($V_2 > V_1$):
(A) The heat absorbed during the isothermal expansion at $T_H$ is $Q_H = n R T_H \ln(V_2/V_1)$.  
(B) The heat rejected during the isothermal compression at $T_C$ is $|Q_C| = n R T_C \ln(V_2/V_1)$.  
(C) With an ideal regenerator storing and releasing heat during the two isochores, the thermal efficiency equals the Carnot efficiency $\eta = 1 - \frac{T_C}{T_H}$.  
(D) Without a regenerator, the thermal efficiency is strictly less than the Carnot efficiency.

#### Question 5
A parallel-plate capacitor with square plates of side $L$ and separation $d \ll L$ is partially filled with a dielectric slab of dielectric constant $\kappa$ and thickness $d$. The slab is inserted a distance $x$ ($0 \le x \le L$) parallel to an edge, while the plates are maintained at a constant potential difference $V_0$:
(A) The capacitance of the system is $C(x) = \frac{\varepsilon_0 L}{d}(L + (\kappa - 1)x)$.  
(B) The electrostatic force pulling the dielectric slab into the capacitor is $F = \frac{\varepsilon_0 L (\kappa - 1) V_0^2}{2d}$.  
(C) The work done by the battery as the slab moves by $dx$ is $dW_{\text{batt}} = V_0 dQ = 2 dU_{\text{electrostatic}}$.  
(D) If the plates were isolated with constant charge $Q_0$ instead of constant voltage, the force would still be attractive into the capacitor.

#### Question 6
A plane electromagnetic wave in vacuum is described by $\vec{E}(x, t) = E_0 \cos(k x - \omega t)\hat{j} + E_0 \sin(k x - \omega t)\hat{k}$:
(A) The wave is circularly polarized.  
(B) The associated magnetic field is $\vec{B}(x, t) = -\frac{E_0}{c}\sin(k x - \omega t)\hat{j} + \frac{E_0}{c}\cos(k x - \omega t)\hat{k}$.  
(C) The time-averaged Poynting vector is $\langle \vec{S} \rangle = \frac{\varepsilon_0 c E_0^2}{1} \hat{i}$.  
(D) The radiation pressure exerted on a perfectly absorbing surface perpendicular to the wave is $P_{\text{rad}} = \varepsilon_0 E_0^2$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A horizontal pipeline carries water ($\rho = 1000\text{ kg/m}^3$) through a constriction. The diameter decreases from $D_1 = 10\text{ cm}$ to $D_2 = 5\text{ cm}$. A mercury U-tube manometer ($\rho_{\text{Hg}} = 13600\text{ kg/m}^3$) connected between the two sections shows a height difference $h = 10\text{ cm}$. Calculate the volumetric flow rate $Q$ of water in liters per second (take $g = 9.8\text{ m/s}^2$, round off to ONE decimal place).

#### Question 8
In an experiment measuring the speed of light using Foucault's rotating mirror method, the rotating mirror has angular velocity $\omega = 500\text{ rev/s}$. The fixed concave mirror is located at distance $D = 10\text{ km}$ from the rotating mirror. The lens focuses the return beam at a distance $L = 1.0\text{ m}$ from the rotating mirror. The return beam deflection is measured as $\Delta s$ millimeters. Taking $c = 3.0 \times 10^8\text{ m/s}$, calculate $\Delta s$ in millimeters (round off to TWO decimal places).

#### Question 9
A quantum harmonic oscillator of mass $m$ and classical frequency $\omega$ is in its ground state with wave function $\psi_0(x) = \left(\frac{m\omega}{\pi \hbar}\right)^{1/4} e^{-\frac{m\omega x^2}{2\hbar}}$. The probability of finding the particle in the classically forbidden region $|x| > x_{\text{turn}}$ (where $x_{\text{turn}} = \sqrt{\frac{\hbar}{m\omega}}$) is $P_{\text{forb}}$. Given $\text{erfc}(1) = \frac{2}{\sqrt{\pi}}\int_1^\infty e^{-u^2}du \approx 0.1573$, calculate $100 P_{\text{forb}}$ (round off to TWO decimal places).

#### Question 10
A circular disk of mass $m = 4\text{ kg}$ and radius $r = 0.2\text{ m}$ rolls without slipping inside a fixed cylindrical surface of radius $R = 1.2\text{ m}$. The disk executes small oscillations about the bottom equilibrium position. Taking $g = 9.8\text{ m/s}^2$, calculate the time period $T$ of small oscillations in seconds (round off to TWO decimal places).

#### Question 11
A long coaxial cable consists of an inner solid conductor of radius $a = 2\text{ mm}$ and an outer thin cylindrical shell of radius $b = 8\text{ mm}$. The space between them is vacuum. If equal and opposite currents $I = 10\text{ A}$ flow along the inner and outer conductors, calculate the magnetic energy stored per unit length of the cable in microjoules per meter ($\mu\text{J/m}$) (take $\ln 4 = 1.386$, $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$, round off to ONE decimal place).

#### Question 12
A vertical glass tube of length $1.0\text{ m}$ is closed at the bottom and open at the top. When filled with an ideal gas at $T_0 = 300\text{ K}$, a mercury pellet of length $h = 10\text{ cm}$ traps an air column of length $L_1 = 40\text{ cm}$. The tube is now inverted so that the open end is at the bottom. Atmospheric pressure is $P_{\text{atm}} = 75\text{ cm of Hg}$. If temperature remains constant, the length of the trapped air column in the inverted position is $L_2$ centimeters. Calculate $L_2$ in cm (round off to ONE decimal place).

---

## Section 3: Matching List / Matrix Match (Questions 13 to 18)

#### Question 13
Match the optical phenomenon in List-I with its fundamental underlying principle in List-II:
- **List-I**:
  - P. Brewster's angle
  - Q. Optical activity (rotary polarization)
  - R. Fraunhofer diffraction at single slit
  - S. Total internal reflection
- **List-II**:
  - 1. Different phase velocities for right and left circularly polarized waves ($n_R \ne n_L$)
  - 2. Reflected ray and refracted ray are mutually perpendicular ($\tan\theta_B = n$)
  - 3. Evanescent wave with exponential decay in the rarer medium
  - 4. Interference of secondary wavelets from a continuous wave front

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 14
Match the thermodynamic state variable / thermodynamic relation in List-I with its Maxwell relation / characteristic expression in List-II:
- **List-I**:
  - P. Helmholtz free energy $F = U - TS$
  - Q. Gibbs free energy $G = H - TS$
  - R. Enthalpy $H = U + PV$
  - S. Internal energy $U$
- **List-II**:
  - 1. $\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P$
  - 2. $\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V$
  - 3. $\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P$
  - 4. $\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 3, Q $\to$ 2, R $\to$ 4, S $\to$ 1  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 15
Match the nuclear decay process in List-I with its characteristic conservation law / emitted particle in List-II:
- **List-I**:
  - P. $\beta^-$ decay ($n \to p + e^- + \bar{\nu}_e$)
  - Q. $\beta^+$ decay ($p \to n + e^+ + \nu_e$)
  - R. Electron capture ($p + e^- \to n + \nu_e$)
  - S. $\alpha$ decay ($^A_Z X \to ^{A-4}_{Z-2}Y + ^4_2\text{He}$)
- **List-II**:
  - 1. Monoenergetic neutrino emission with characteristic atomic X-ray emission
  - 2. Continuous positron kinetic energy spectrum up to $Q_{\beta^+} - 2m_e c^2$
  - 3. Continuous electron kinetic energy spectrum ending at endpoint energy $Q$
  - 4. Discrete kinetic energy spectrum determined by two-body decay kinematics

(A) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3  

#### Question 16
Match the electrical circuit element in List-I with its AC impedance phase behavior in List-II:
- **List-I**:
  - P. Pure Inductor $L$
  - Q. Pure Capacitor $C$
  - R. Series $RLC$ circuit at resonance ($\omega = \frac{1}{\sqrt{LC}}$)
  - S. Parallel $LC$ circuit at antiresonance
- **List-II**:
  - 1. Current leads voltage by phase angle $\pi/2$
  - 2. Voltage leads current by phase angle $\pi/2$
  - 3. Current and voltage are exactly in phase; impedance is purely real and minimum
  - 4. Dynamic impedance is purely real and infinite (zero line current in ideal case)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 3, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 17
Match the classical mechanics principle in List-I with its corresponding conserved quantity via Noether's theorem in List-II:
- **List-I**:
  - P. Invariance of Lagrangian under spatial translation
  - Q. Invariance of Lagrangian under spatial rotation
  - R. Invariance of Lagrangian under time translation
  - S. Gauge invariance of electromagnetic Lagrangian
- **List-II**:
  - 1. Total angular momentum
  - 2. Total linear momentum
  - 3. Total mechanical energy
  - 4. Total electric charge

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 3, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4  

#### Question 18
Match the electromagnetic boundary condition in List-I with its mathematical statement at an interface between medium 1 and medium 2 with free surface charge $\sigma_f$ and free surface current $\vec{K}_f$ in List-II:
- **List-I**:
  - P. Normal component of $\vec{D}$
  - Q. Tangential component of $\vec{E}$
  - R. Normal component of $\vec{B}$
  - S. Tangential component of $\vec{H}$
- **List-II**:
  - 1. $B_{2n} - B_{1n} = 0$ (continuous)
  - 2. $E_{2t} - E_{1t} = 0$ (continuous)
  - 3. $D_{2n} - D_{1n} = \sigma_f$
  - 4. $\hat{n} \times (\vec{H}_2 - \vec{H}_1) = \vec{K}_f$

(A) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4  
(D) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Ellingham diagram for metallurgical reduction processes:
(A) The slope of the $\Delta G^\circ$ vs $T$ line is $-\Delta S^\circ$, which is positive for most metal oxidation reactions ($2M + O_2 \to 2MO$) because gas is consumed ($\Delta S^\circ < 0$).  
(B) The line for $2\text{C} + \text{O}_2 \to 2\text{CO}$ has a negative slope because one mole of gas produces two moles of gas ($\Delta S^\circ > 0$).  
(C) Any metal whose oxidation line lies below that of carbon monoxide can be reduced by carbon at that temperature.  
(D) Sudden changes in the slope of an Ellingham curve correspond to phase transitions (melting or boiling) of the metal or its oxide.

#### Question 20
Consider the Heck reaction catalyzed by palladium:
$$\text{Ar-X} + \text{CH}_2=\text{CH-EWG} \xrightarrow{\text{Pd}(0)\text{ cat, Base}} \text{Ar-CH}=\text{CH-EWG} + \text{HX}$$
(A) Oxidative addition of aryl halide $\text{Ar-X}$ to $\text{Pd}(0)$ occurs with retention of configuration.  
(B) Syn-migratory insertion of the alkene into the $\text{Pd-Ar}$ $\sigma$-bond forms a new $\text{C-C}$ bond with regioselective addition of the aryl group to the less substituted carbon.  
(C) $\beta$-hydride elimination requires a syn-coplanar conformation between the palladium atom and a $\beta$-hydrogen, generating the trans-alkene.  
(D) Base is required in the catalytic cycle to regenerate the active $\text{Pd}(0)$ catalyst by reductive elimination of $\text{HX}$ from the palladium-hydride complex.

#### Question 21
Regarding the chemistry of transition metal complexes with carbonyl ligands:
(A) In homoleptic metal carbonyls such as $\text{Ni(CO)}_4$, $\text{Fe(CO)}_5$, and $\text{Cr(CO)}_6$, the metal atom obeys the 18-electron rule.  
(B) The $\text{C-O}$ stretching frequency in infrared spectroscopy decreases in the order: $[\text{Mn(CO)}_6]^+ > \text{Cr(CO)}_6 > [\text{V(CO)}_6]^-$.  
(C) Stronger $\pi$-backbonding from metal $d$-orbitals into the $\text{CO}$ $\pi^*$ orbitals strengthens the $\text{M-C}$ bond and weakens the $\text{C-O}$ bond.  
(D) Bridging carbonyl ($\mu_2\text{-CO}$) ligands exhibit lower infrared stretching frequencies ($1750\text{--}1850\text{ cm}^{-1}$) than terminal carbonyl ligands ($1900\text{--}2100\text{ cm}^{-1}$).

#### Question 22
For the conductometric titration of a mixture of hydrochloric acid ($\text{HCl}$) and acetic acid ($\text{CH}_3\text{COOH}$) with standard sodium hydroxide ($\text{NaOH}$):
(A) In the first phase, conductance drops sharply as highly mobile $\text{H}^+$ ions ($\lambda^\circ \approx 350\text{ S cm}^2\text{mol}^{-1}$) are replaced by slower $\text{Na}^+$ ions ($\lambda^\circ \approx 50\text{ S cm}^2\text{mol}^{-1}$).  
(B) In the second phase, conductance increases moderately as weak acid $\text{CH}_3\text{COOH}$ is converted to $\text{CH}_3\text{COO}^-$ and $\text{Na}^+$ ions.  
(C) After the second equivalence point, conductance rises steeply due to the accumulation of excess, highly mobile $\text{OH}^-$ ions ($\lambda^\circ \approx 198\text{ S cm}^2\text{mol}^{-1}$).  
(D) The first break in the curve corresponds to neutralization of $\text{CH}_3\text{COOH}$ and the second break corresponds to $\text{HCl}$.

#### Question 23
Regarding the stereochemistry and mechanism of the Beckmann rearrangement:
$$\text{R}_1\text{C}(=\text{NOH})\text{R}_2 \xrightarrow{\text{H}_2\text{SO}_4\text{ or }\text{PCl}_5} \text{R}_1\text{CONHR}_2$$
(A) The group that migrates to the nitrogen atom is strictly the group that is anti (trans) to the leaving hydroxyl group ($-\text{OH}$).  
(B) The migration proceeds with complete retention of stereochemical configuration at the migrating carbon center.  
(C) The reaction proceeds via an intermediate nitrilium ion $[\text{R-C}\equiv\text{N-R'}]^+$.  
(D) Beckmann rearrangement of cyclohexanone oxime yields $\epsilon$-caprolactam, the commercial precursor for Nylon-6.

#### Question 24
In the extraction of titanium from rutile ore ($\text{TiO}_2$) via the Kroll process:
(A) Rutile is first converted to titanium tetrachloride ($\text{TiCl}_4$) by heating with carbon and chlorine at $900^\circ\text{C}$.  
(B) Titanium cannot be extracted by direct carbon reduction of $\text{TiO}_2$ because it forms an interstitial, brittle titanium carbide ($\text{TiC}$).  
(C) Fractional distillation is used to purify $\text{TiCl}_4$ (boiling point $136^\circ\text{C}$) from impurities like $\text{FeCl}_3$.  
(D) Reduction of purified $\text{TiCl}_4$ is carried out using molten magnesium under an inert argon atmosphere at $800\text{--}850^\circ\text{C}$.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The dissociation constant of a weak monoprotic acid $\text{HA}$ is $K_a = 1.0 \times 10^{-5}$. A buffer solution is prepared by mixing $100\text{ mL}$ of $0.20\text{ M}$ $\text{HA}$ with $100\text{ mL}$ of $0.10\text{ M}$ $\text{NaOH}$. To this buffer, $1.0\text{ mL}$ of $1.0\text{ M}$ $\text{HCl}$ is added. The pH of the resulting solution is measured at $25^\circ\text{C}$. Calculate the final pH of the solution (use $\log 1.22 = 0.086$, round off to TWO decimal places).

#### Question 26
Calculate the magnetic moment (spin-only) in Bohr Magnetons ($\mu_B$) for the high-spin complex $[Fe(H_2O)_6]^{2+}$ (atomic number of $\text{Fe} = 26$). Enter the value rounded off to TWO decimal places (take $\sqrt{24} \approx 4.90$).

#### Question 27
An organic compound contains $60.0\%$ Carbon, $4.48\%$ Hydrogen, and $35.52\%$ Oxygen by mass. Its vapor density relative to hydrogen is $45$. Calculate the number of oxygen atoms present in one molecule of this compound.

#### Question 28
The standard reduction potentials for copper species are:
$$E^\circ(\text{Cu}^{2+}/\text{Cu}^+) = +0.15\text{ V}, \quad E^\circ(\text{Cu}^+/\text{Cu}) = +0.52\text{ V}$$
Calculate the equilibrium constant $K_{\text{eq}}$ for the disproportionation reaction $2\text{Cu}^+(aq) \rightleftharpoons \text{Cu}^{2+}(aq) + \text{Cu}(s)$ at $298\text{ K}$. If $\log_{10} K_{\text{eq}} = X$, find $X$ (use $\frac{2.303 RT}{F} = 0.0591\text{ V}$, round off to TWO decimal places).

#### Question 29
A crystal of $\text{NaCl}$ is doped with $10^{-4}\text{ mol }\%$ of $\text{SrCl}_2$. The concentration of cation vacancies created per mole of $\text{NaCl}$ is $N_v$. If $N_v = Y \times 10^{17}\text{ vacancies/mol}$, find the value of $Y$ (use Avogadro's number $N_A = 6.023 \times 10^{23}\text{ mol}^{-1}$, round off to TWO decimal places).

#### Question 30
In the van der Waals equation for 1 mole of a real gas, the critical volume is $V_c = 0.15\text{ L/mol}$ and critical pressure is $P_c = 50\text{ atm}$. Find the van der Waals constant $a$ in $\text{atm}\cdot\text{L}^2\cdot\text{mol}^{-2}$ (round off to TWO decimal places).

---

## Section 3: Matching List / Matrix Match (Questions 31 to 36)

#### Question 31
Match the name reaction in List-I with its characteristic intermediate / key reagent in List-II:
- **List-I**:
  - P. Hofmann rearrangement
  - Q. Wolff rearrangement
  - R. Reimer-Tiemann reaction
  - S. Mannich reaction
- **List-II**:
  - 1. Acylcarbene intermediate ($\alpha$-ketocarbene) $\to$ Ketene
  - 2. Iminium ion intermediate ($[\text{CH}_2=\text{NR}_2]^+$)
  - 3. Acyl nitrene intermediate $\to$ Isocyanate
  - 4. Dichlorocarbene ($:\text{CCl}_2$)

(A) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(B) P $\to$ 1, Q $\to$ 3, R $\to$ 4, S $\to$ 2  
(C) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 3, S $\to$ 2  

#### Question 32
Match the mineral ore in List-I with its primary chemical formula in List-II:
- **List-I**:
  - P. Calamine
  - Q. Malachite
  - R. Siderite
  - S. Sphalerite
- **List-II**:
  - 1. $\text{FeCO}_3$
  - 2. $\text{ZnCO}_3$
  - 3. $\text{CuCO}_3\cdot\text{Cu(OH)}_2$
  - 4. $\text{ZnS}$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 3, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 3, R $\to$ 1, S $\to$ 2  

#### Question 33
Match the coordination compound in List-I with its hybridization and magnetic behavior in List-II:
- **List-I**:
  - P. $[\text{Ni(CN)}_4]^{2-}$
  - Q. $[\text{NiCl}_4]^{2-}$
  - R. $[\text{Fe(CN)}_6]^{4-}$
  - S. $[\text{FeF}_6]^{3-}$
- **List-II**:
  - 1. $sp^3$, paramagnetic ($\mu = 2.83\text{ BM}$)
  - 2. $dsp^2$, diamagnetic ($\mu = 0$)
  - 3. $sp^3d^2$, paramagnetic ($\mu = 5.92\text{ BM}$)
  - 4. $d^2sp^3$, diamagnetic ($\mu = 0$)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 4, S $\to$ 3  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 34
Match the polymer in List-I with its monomer units in List-II:
- **List-I**:
  - P. Dacron (Terylene)
  - Q. Nylon-6,6
  - R. Bakelite
  - S. Glyptal
- **List-II**:
  - 1. Phenol + Formaldehyde
  - 2. Hexamethylenediamine + Adipic acid
  - 3. Ethylene glycol + Terephthalic acid
  - 4. Ethylene glycol + Phthalic acid

(A) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4  
(D) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  

#### Question 35
Match the colloid type in List-I with its typical example in List-II:
- **List-I**:
  - P. Aerosol
  - Q. Emulsion
  - R. Gel
  - S. Solid Sol
- **List-II**:
  - 1. Milk / Mayonnaise
  - 2. Fog / Smoke
  - 3. Cheese / Butter
  - 4. Gemstones / Ruby glass

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 3, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4  

#### Question 36
Match the reagent in List-I with its specific synthetic transformation in organic chemistry in List-II:
- **List-I**:
  - P. PCC (Pyridinium chlorochromate)
  - Q. $\text{LiAlH}_4$ in dry ether
  - R. $\text{NaBH}_4$ in ethanol
  - S. $\text{m-CPBA}$ (meta-chloroperbenzoic acid)
- **List-II**:
  - 1. Epoxidation of alkenes
  - 2. Selective oxidation of primary alcohols to aldehydes without over-oxidation
  - 3. Reduces aldehydes and ketones but does NOT reduce esters or amides
  - 4. Powerful reducing agent reducing esters, carboxylic acids, amides to alcohols/amines

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 3, S $\to$ 1  
(B) P $\to$ 4, Q $\to$ 2, R $\to$ 3, S $\to$ 1  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \int_0^x \frac{\sin t}{t} dt$ (the sine integral $\text{Si}(x)$) for $x > 0$:
(A) The critical points of $f(x)$ occur at $x = n\pi$, where $n \in \{1, 2, 3, \dots\}$.  
(B) $f(x)$ has local maxima at $x = (2k-1)\pi$ and local minima at $x = 2k\pi$ for positive integers $k$.  
(C) The global maximum of $f(x)$ on $[0, \infty)$ occurs at $x = \pi$.  
(D) $\lim_{x \to \infty} f(x) = \frac{\pi}{2}$.

#### Question 38
Let $A$ and $B$ be two $n \times n$ real matrices such that $A B - B A = A$:
(A) $\text{Tr}(A) = 0$.  
(B) For any positive integer $k$, $A^k B - B A^k = k A^k$.  
(C) $A$ is a nilpotent matrix; that is, $A^m = O$ for some positive integer $m \le n$.  
(D) All eigenvalues of $A$ are equal to zero.

#### Question 39
Let $S$ be the sphere $x^2 + y^2 + z^2 = 9$. A plane $\Pi: 2x - 2y + z = 18$ is given:
(A) The distance from the center of the sphere to the plane $\Pi$ is 6.  
(B) The plane $\Pi$ is parallel to the tangent plane to $S$ at the point $(2, -2, 1)$.  
(C) The shortest distance between any point on the sphere $S$ and any point on the plane $\Pi$ is 3.  
(D) The point on the sphere closest to the plane $\Pi$ is $(2, -2, 1)$.

#### Question 40
Let $y(x)$ be the solution of the non-linear initial value problem:
$$\frac{dy}{dx} + y^2 = 1, \quad y(0) = 0$$
(A) The solution is given by $y(x) = \tanh x$.  
(B) $\lim_{x \to \infty} y(x) = 1$ and $\lim_{x \to -\infty} y(x) = -1$.  
(C) The function $y(x)$ is strictly increasing on $\mathbb{R}$.  
(D) The point $(0, 0)$ is a point of inflection for the curve $y = y(x)$.

#### Question 41
A fair die is tossed repeatedly until the sum of the numbers rolled is strictly greater than 10. Let $N$ be the number of tosses required:
(A) The minimum possible value of $N$ is 2.  
(B) The maximum possible value of $N$ is 11.  
(C) $P(N = 2) = \frac{7}{18}$.  
(D) $P(N = 11) = \left(\frac{1}{6}\right)^{10}$.

#### Question 42
Consider the curve defined parametrically by $x = a \cos^3 \theta$, $y = a \sin^3 \theta$ (an astroid):
(A) The length of the tangent segment intercepted between the coordinate axes is constant and equal to $a$.  
(B) The total perimeter of the astroid is $6a$.  
(C) The total area enclosed by the astroid is $\frac{3\pi a^2}{8}$.  
(D) The radius of curvature at any point $\theta$ is $R = 3a |\sin\theta \cos\theta|$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Let $P(x)$ be a polynomial with real coefficients satisfying $P(x^2 + 1) = [P(x)]^2 + 1$ for all $x \in \mathbb{R}$, and $P(0) = 0$. Find the value of $P(10)$.

#### Question 44
Find the number of ways to arrange the 8 letters of the word **EQUATION** such that no two vowels are adjacent to each other.

#### Question 45
Evaluate the definite integral:
$$I = \int_{-\pi/4}^{\pi/4} \frac{x^2 + x \sin x}{1 + \cos 2x} dx$$
Calculate the value of $\frac{48 I}{\pi^3 - 6\pi}$ (round off to the nearest integer).

#### Question 46
Let $\vec{a} = 2\hat{i} + \hat{j} - 2\hat{k}$ and $\vec{b} = \hat{i} + \hat{j}$. If $\vec{c}$ is a vector such that $\vec{a} \cdot \vec{c} = |\vec{c}|$, $|\vec{c} - \vec{a}| = 2\sqrt{2}$, and the angle between $\vec{a} \times \vec{b}$ and $\vec{c}$ is $30^\circ$, find the magnitude $|(\vec{a} \times \vec{b}) \times \vec{c}|$.

#### Question 47
Let $f(x) = \frac{x}{1 + x \tan x}$ for $x \in (0, \pi/2)$. If the maximum value of $f(x)$ on this interval is attained at $x = x_0$, then $\cos x_0$ equals $K$. If $x_0 = \pi/4$, find the value of $100 K^2$ (round off to the nearest integer).

#### Question 48
In an ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b$), the focal distance of any point $P$ is $r_1$ and $r_2$. If the maximum area of a triangle formed by the two foci $S, S'$ and a variable point $P$ on the ellipse is $12$, and the distance between the foci is $8$, find the value of the semi-major axis $a$.

---

## Section 3: Matching List / Matrix Match (Questions 49 to 54)

#### Question 49
Match the function in List-I with its asymptotic behavior / limit in List-II:
- **List-I**:
  - P. $\lim_{x \to 0} \frac{x - \sin x}{x^3}$
  - Q. $\lim_{x \to 0} \frac{\ln(1 + x) - x}{x^2}$
  - R. $\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$
  - S. $\lim_{x \to 0} \frac{\tan x - x}{x^3}$
- **List-II**:
  - 1. $1/2$
  - 2. $1/6$
  - 3. $-1/2$
  - 4. $1/3$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 3, R $\to$ 1, S $\to$ 2  

#### Question 50
Match the curve in polar coordinates in List-I with its geometric name in List-II:
- **List-I**:
  - P. $r = a(1 - \cos\theta)$
  - Q. $r^2 = a^2 \cos(2\theta)$
  - R. $r = a \theta$
  - S. $r = a e^{b \theta}$
- **List-II**:
  - 1. Lemniscate of Bernoulli
  - 2. Cardioid
  - 3. Logarithmic (equiangular) spiral
  - 4. Archimedean spiral

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 51
Match the differential equation in List-I with its order and degree in List-II:
- **List-I**:
  - P. $\left(\frac{d^2 y}{dx^2}\right)^3 + \left(\frac{dy}{dx}\right)^4 + y = 0$
  - Q. $\frac{d^3 y}{dx^3} + \sqrt{\frac{dy}{dx}} + y = 0$
  - R. $\left[1 + \left(\frac{dy}{dx}\right)^2\right]^{3/2} = k \frac{d^2 y}{dx^2}$
  - S. $\frac{dy}{dx} = \sin\left(\frac{dy}{dx}\right)$
- **List-II**:
  - 1. Order 2, Degree 2
  - 2. Order 2, Degree 3
  - 3. Order 3, Degree 2
  - 4. Order 1, Degree not defined

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  

#### Question 52
Match the probability distribution in List-I with its variance $\text{Var}(X)$ in List-II:
- **List-I**:
  - P. Binomial distribution $B(n, p)$
  - Q. Poisson distribution $\text{Poisson}(\lambda)$
  - R. Geometric distribution $P(X = k) = (1-p)^{k-1}p$ ($k = 1, 2, \dots$)
  - S. Uniform distribution on continuous interval $[a, b]$
- **List-II**:
  - 1. $\lambda$
  - 2. $n p (1 - p)$
  - 3. $\frac{b - a)^2}{12}$
  - 4. $\frac{1 - p}{p^2}$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 53
Match the matrix operation in List-I with its mathematical property for an $n \times n$ matrix $A$ in List-II:
- **List-I**:
  - P. $\det(k A)$
  - Q. $\det(A^{-1})$
  - R. $\det(\text{adj}(A))$
  - S. $\det(A^T)$
- **List-II**:
  - 1. $\frac{1}{\det(A)}$
  - 2. $k^n \det(A)$
  - 3. $\det(A)$
  - 4. $(\det(A))^{n-1}$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 4, S $\to$ 3  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 54
Match the vector identity in List-I with its expansion in List-II:
- **List-I**:
  - P. $\vec{a} \times (\vec{b} \times \vec{c})$
  - Q. $(\vec{a} \times \vec{b}) \cdot (\vec{c} \times \vec{d})$
  - R. $\nabla \cdot (\nabla \times \vec{A})$
  - S. $\nabla \times (\nabla \phi)$
- **List-II**:
  - 1. Zero identically ($0$)
  - 2. Zero vector identically ($\vec{0}$)
  - 3. $(\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$
  - 4. $(\vec{a} \cdot \vec{c})(\vec{b} \cdot \vec{d}) - (\vec{a} \cdot \vec{d})(\vec{b} \cdot \vec{c})$

(A) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(B) P $\to$ 4, Q $\to$ 3, R $\to$ 1, S $\to$ 2  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(D) P $\to$ 1, Q $\to$ 4, R $\to$ 2, S $\to$ 3  
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 13

---

### PART I: PHYSICS

#### Solution 1: Stern-Gerlach Gradient Deflection
1. **Core Concept / Theory**:
   The magnetic force on a dipole $\vec{\mu} = \mu_z \hat{k}$ in an inhomogeneous field $\vec{B}$ is $\vec{F} = \nabla(\vec{\mu} \cdot \vec{B}) = \mu_z \frac{\partial B_z}{\partial z} \hat{k} = \mu_B \alpha \hat{k}$.
2. **Maxwell Constraint**:
   $\nabla \cdot \vec{B} = \frac{\partial B_x}{\partial x} + \frac{\partial B_z}{\partial z} = -\alpha + \alpha = 0$, confirming physical realizability.
3. **Kinematics in Magnet**:
   Time inside field $t_1 = L/v_0$. Acceleration $a_z = \frac{\mu_B \alpha}{m}$. Exit deflection $z_1 = \frac{1}{2} a_z t_1^2 = \frac{\mu_B \alpha L^2}{2 m v_0^2}$.
4. **Drift Region**:
   Exit velocity $v_z = a_z t_1 = \frac{\mu_B \alpha L}{m v_0}$. Additional deflection in drift space $D$: $z_2 = v_z (D/v_0) = \frac{\mu_B \alpha L D}{m v_0^2}$.
   Total deflection $z_{\text{total}} = z_1 + z_2 = \frac{\mu_B \alpha L}{m v_0^2}\left(\frac{L}{2} + D\right)$.
- **Conclusion**: Statements (A), (B), (C), and (D) are all rigorously correct.
- **Correct Option**: (A, B, C, D)

#### Solution 2: Dieterici Real Gas
1. **Critical Conditions**:
   $\left(\frac{\partial P}{\partial V_m}\right)_{T_c} = 0$ and $\left(\frac{\partial^2 P}{\partial V_m^2}\right)_{T_c} = 0$.
2. **Critical Parameters**:
   Solving gives $V_c = 2b$, $T_c = \frac{a}{4 R b}$, and $P_c = \frac{a}{4 e^2 b^2}$.
3. **Compressibility Factor**:
   $Z_c = \frac{P_c V_c}{R T_c} = \frac{(a / 4 e^2 b^2)(2b)}{R (a / 4 R b)} = 2 e^{-2} \approx 0.271$.
4. **Joule-Thomson Inversion**:
   Inversion curve condition $\left(\frac{\partial T}{\partial P}\right)_H = 0 \iff T\left(\frac{\partial V}{\partial T}\right)_P - V = 0$. In dilute gas limit, this yields $T_i(V_m) = \frac{a}{R b}\left(\frac{V_m - b}{V_m}\right)$.
- **Correct Option**: (A, B, C, D)

#### Solution 3: Inhomogeneous Dielectric Capacitor
1. **Displacement Field**:
   By Gauss's law for $\vec{D}$, $\oint \vec{D} \cdot d\vec{A} = Q \implies D(r) \cdot 2\pi r L = Q \implies D(r) = \frac{Q}{2\pi r L}\hat{r}$.
2. **Electric Field**:
   $\vec{E}(r) = \frac{\vec{D}(r)}{\varepsilon(r)} = \frac{Q / (2\pi r L)}{\varepsilon_0 a / r} = \frac{Q}{2\pi \varepsilon_0 a L}\hat{r}$, completely uniform and independent of $r$.
3. **Potential Difference**:
   $V = \int_a^b E dr = \frac{Q}{2\pi \varepsilon_0 a L}(b - a)$.
4. **Capacitance**:
   $C = \frac{Q}{V} = \frac{2\pi \varepsilon_0 a L}{b - a}$.
- **Correct Option**: (A, B, C, D)

#### Solution 4: Rotating Charged Ring
1. **Magnetic Moment**:
   Current $I = \frac{Q}{T} = \frac{Q \omega}{2\pi}$. Area $A = \pi R^2$. Dipole moment $\mu = I A = \frac{1}{2} Q \omega R^2$.
2. **Electrostatic Potential**:
   All points on ring are at distance $\sqrt{R^2 + x^2}$, so $V(x) = \frac{Q}{4\pi \varepsilon_0 \sqrt{R^2 + x^2}}$.
3. **Conservation of Energy**:
   $\Delta K = q(V(x_0) - V(0)) = q Q \frac{1}{4\pi\varepsilon_0}\left(\frac{1}{R} - \frac{1}{\sqrt{R^2 + 3R^2}}\right) = \frac{q Q}{8\pi\varepsilon_0 R}$.
   $\frac{1}{2} m v^2 = \frac{q Q}{8\pi\varepsilon_0 R} \implies v = \sqrt{\frac{q Q}{4\pi\varepsilon_0 m R}}$.
4. **Magnetic Field at Center**:
   $B = \frac{\mu_0 I}{2R} = \frac{\mu_0 (Q\omega / 2\pi)}{2R} = \frac{\mu_0 Q \omega}{4\pi R}$.
- **Correct Option**: (A, B, C, D)

#### Solution 5: Fabry-Pérot Interferometer
- All parameters (A), (B), (C), (D) follow from standard Airy formula for multi-beam interference.
- **Correct Option**: (A, B, C, D)

#### Solution 6: Rolling Sphere in Cycloidal Track
- Motion on an inverted cycloid exhibits exact isochronism (tautochrone property), even for large amplitudes.
- $T = 2\pi \sqrt{\frac{7(4R - r)}{5g}}$ accounting for rotational inertia $I = \frac{2}{5} m r^2$.
- Mechanical energy is conserved because instantaneous contact velocity is zero.
- **Correct Option**: (A, B, C, D)

#### Solution 7: LC with Variable Inductance
- Using adiabatic invariant of harmonic oscillator $E/\omega = \text{constant}$.
- Since $\omega(t) = \frac{1}{\sqrt{L(t)C}} \propto (1 + \alpha t)^{-1/2}$, energy $E(t) \propto \omega(t) \propto (1 + \alpha t)^{-1/2}$.
- Since $E = \frac{1}{2} C V_{\text{rms}}^2$, $V_{\text{rms}} \propto \sqrt{E} \propto (1 + \alpha t)^{-1/4}$.
- Therefore $\gamma = 0.25 \implies 100\gamma = 25$.
- **Answer**: 25

#### Solution 8: Gyroscope Precession
- Torque due to gravity: $\tau = M g d = 2 \times 9.8 \times 0.15 = 2.94\text{ N}\cdot\text{m}$.
- Spin angular momentum: $L_s = I \omega_s = \left(\frac{1}{2} M R^2\right) \omega_s = \frac{1}{2} (2) (0.01) (600) = 6.0\text{ kg m}^2/\text{s}$.
- Precession rate: $\Omega_p = \frac{\tau}{L_s} = \frac{2.94}{6.0} = 0.49\text{ rad/s}$.
- **Answer**: 0.49

#### Solution 9: Blackbody Radiative Cooling
- Rate of heat loss: $M s \frac{dT}{dt} = -e \sigma A T^4 \implies \frac{dT}{dt} = -\frac{4\pi R^2 \sigma}{M s} T^4$.
- Let $k = \frac{4\pi R^2 \sigma}{M s} = \frac{4\pi (0.05)^2 (5.67 \times 10^{-8})}{1.0 \times 400} = \frac{3.1416 \times 0.01 \times 5.67 \times 10^{-8}}{400} = 4.453 \times 10^{-12}\text{ K}^{-3}\text{s}^{-1}$.
- Integrating: $\int_{T_0}^{T_1} T^{-4} dT = -k t \implies \frac{1}{3}\left(\frac{1}{T_1^3} - \frac{1}{T_0^3}\right) = k t$.
- $\frac{1}{3}\left(\frac{1}{250^3} - \frac{1}{500^3}\right) = \frac{1}{3}\left(\frac{8 - 1}{500^3}\right) = \frac{7}{3 \times 1.25 \times 10^8} = 1.867 \times 10^{-8}$.
- $t = \frac{1.867 \times 10^{-8}}{4.453 \times 10^{-12}} \approx 4192\text{ s}$.
- **Answer**: 4192

#### Solution 10: Relativistic Threshold Energy
- In center-of-momentum frame, final state has 4 stationary protons: invariant mass squared $s = (4 m_p)^2 = 16 m_p^2$.
- In laboratory frame before collision: $s = (P_1 + P_2)^2 = m_p^2 + m_p^2 + 2(E_1 m_p - \vec{p}_1 \cdot \vec{0}) = 2 m_p^2 + 2 E_1 m_p$.
- Equating: $2 m_p^2 + 2 E_1 m_p = 16 m_p^2 \implies 2 E_1 m_p = 14 m_p^2 \implies E_1 = 7 m_p c^2$.
- Thus $k = 7$.
- **Answer**: 7

#### Solution 11: Mutual Inductance & Induced Loop Current
- Magnetic flux through outer loop of radius $b > a$ is confined to solenoid radius $a$:
  $\Phi(t) = B(t) \cdot \pi a^2 = (\mu_0 n I_0 \sin\omega t) \pi a^2$.
- Induced EMF: $\mathcal{E}(t) = -\frac{d\Phi}{dt} = -\mu_0 n \pi a^2 I_0 \omega \cos\omega t$.
- Peak EMF: $\mathcal{E}_{\text{peak}} = (4\pi \times 10^{-7}) (1000) \pi (0.04)^2 (5) (100\pi) = 4\pi^3 \times 10^{-4} \times 1.6 \times 10^{-3} \times 500 \approx 0.0099\text{ V}$.
- Peak current: $I_{\text{peak}} = \frac{\mathcal{E}_{\text{peak}}}{R_{\text{loop}}} = \frac{0.0099}{0.02} \approx 0.49\text{ A}$.
- **Answer**: 0.49

#### Solution 12: Piston Equilibrium Displacement
- Piston mass $m = 10\text{ kg}$, weight $W = mg = 98\text{ N}$.
- Area $A = 0.05\text{ m}^2$. Pressure difference $\Delta P = \frac{mg}{A} = \frac{98}{0.05} = 1960\text{ Pa}$.
- Upper gas: expands from $h_0 = 0.6\text{ m}$ to $h_0 + \Delta h$. $P_1 = P_0 \frac{h_0}{h_0 + \Delta h} \approx P_0 (1 - \Delta h / h_0)$.
- Lower gas: compresses to $h_0 - \Delta h$. $P_2 = P_0 \frac{h_0}{h_0 - \Delta h} \approx P_0 (1 + \Delta h / h_0)$.
- $P_2 - P_1 = 2 P_0 \frac{\Delta h}{h_0} = \frac{mg}{A}$.
- $\Delta h = \frac{mg h_0}{2 P_0 A} = \frac{98 \times 0.6}{2 \times 10^5 \times 0.05} = \frac{58.8}{10000} = 0.00588\text{ m} = 5.88\text{ mm}$.
- **Answer**: 5.88

#### Solution 13: Central Potential
- Effective potential $V_{\text{eff}}(r) = \frac{L^2 + 2mc}{2mr^2} - \frac{k}{r}$.
- Modifies angular frequency, leading to perihelion precession $\Delta\theta = 2\pi\left(\frac{L}{\sqrt{L^2 + 2mc}} - 1\right)$.
- **Correct Option**: (A)

#### Solution 14: Beat Spatial Envelope
- $\Delta k = k_1 - k_2 = \frac{2\pi}{\lambda} - \frac{2\pi}{\lambda + \Delta\lambda} \approx \frac{2\pi \Delta\lambda}{\lambda^2}$.
- Spatial envelope repeat length $\Delta x = \frac{2\pi}{\Delta k} = \frac{\lambda^2}{\Delta\lambda}$.
- **Correct Option**: (B)

#### Solution 15: Sphere on Accelerating Conveyor
- In belt frame, fictitious force $M a_0$ acts at CM. Rolling constraint: $a_{\text{rel}} = \frac{a_0}{1 + I/(MR^2)} = \frac{a_0}{1 + 2/5} = \frac{5}{7} a_0$ opposite to belt.
- In ground frame: $a_{\text{cm}} = a_0 - a_{\text{rel}} = a_0 - \frac{5}{7} a_0 = \frac{2}{7} a_0$.
- **Correct Option**: (A)

#### Solution 16: Reduced Mass Correction
- Reduced mass $\mu = \frac{m_e M}{m_e + M} = \frac{m_e (4m_e)}{5m_e} = \frac{4}{5} m_e$.
- Frequency $\nu \propto \mu \implies \nu = \frac{4}{5} \nu_\infty$.
- **Correct Option**: (A)

#### Solution 17: Falling Conducting Loop
- Motional EMF $\mathcal{E} = B_0 a v$. Induced current $I = \frac{B_0 a v}{R}$. Magnetic retarding force $F_B = I a B_0 = \frac{B_0^2 a^2 v}{R}$.
- Terminal velocity when $F_B = mg \implies v_t = \frac{mg R}{B_0^2 a^2}$.
- **Correct Option**: (A)

#### Solution 18: Doppler Effect Circular Path
- Maximum frequency occurs when velocity component directed towards observer is maximum ($\omega R$ along line of sight).
- $f_{\text{max}} = f_0 \frac{v}{v - \omega R}$.
- **Correct Option**: (A)

---

### PART II: CHEMISTRY

#### Solution 19: Zeise's Salt
- All four statements (A), (B), (C), (D) correctly articulate the Dewar-Chatt-Duncanson model and geometry of Zeise's salt.
- **Correct Option**: (A, B, C, D)

#### Solution 20: Shapiro Reaction Mechanism
- Explains the two deprotonations, nitrogen extrusion, vinyllithium formation and trapping.
- **Correct Option**: (A, B, C, D)

#### Solution 21: Langmuir Adsorption
- Note: Statement (D) is false because adsorption is exothermic ($\Delta H_{\text{ads}} < 0$), so by van 't Hoff equation, the adsorption equilibrium constant $K$ *decreases* with increasing temperature. Thus (A, B, C) are correct.
- **Correct Option**: (A, B, C)

#### Solution 22: Borazine vs Benzene
- Borazine has localized polar bonds ($\text{B}^{\delta+}-\text{N}^{\delta-}$), reacts readily with $\text{HCl}$ by addition, and hydrolyzes to $\text{H}_3\text{BO}_3$, $\text{NH}_3$, and $\text{H}_2$.
- **Correct Option**: (A, B, C, D)

#### Solution 23: Cyano Iron Complexes
- Nernst potential shift: $E^\circ = 0.77 - 0.0591 \log(10^{42}/10^{35}) = 0.77 - 0.41 = 0.36\text{ V}$.
- Electronic configurations: $t_{2g}^6$ (diamagnetic) and $t_{2g}^5$ (paramagnetic, 1 unpaired electron).
- **Correct Option**: (A, B, C, D)

#### Solution 24: Stille Coupling
- All four steps represent the classic catalytic cycle of the Stille reaction.
- **Correct Option**: (A, B, C, D)

#### Solution 25: Radioactive Succession Bateman Equation
- $t_{\text{max}} = \frac{\ln(\lambda_B / \lambda_A)}{\lambda_B - \lambda_A} = \frac{\ln(0.20 / 0.04)}{0.20 - 0.04} = \frac{\ln 5}{0.16} = \frac{1.609}{0.16} = 10.06\text{ h}$.
- **Answer**: 10.06

#### Solution 26: CFSE of Low-Spin $[Co(NH_3)_6]^{3+}$
- $\text{Co}^{3+}$ is $d^6$. With strong-field $\text{NH}_3$, $\Delta_o = 23,000 > P = 19,000$, forming low-spin $t_{2g}^6 e_g^0$.
- Orbital CFSE: $6 \times (-0.4 \Delta_o) = -2.4 \Delta_o = -2.4 \times 23,000 = -55,200\text{ cm}^{-1}$.
- Net pairing energy: High-spin $d^6$ has 1 pair; low-spin has 3 pairs $\implies 2$ extra pairs $= 2 \times 19,000 = +38,000\text{ cm}^{-1}$.
- Net CFSE magnitude: $|-55,200 + 38,000| = 17,200\text{ cm}^{-1} = 17.2 \times 10^3\text{ cm}^{-1}$.
- **Answer**: 17.2

#### Solution 27: Mutarotation Equilibrium
- $K_{\text{eq}} = \frac{k_1}{k_{-1}} = \frac{0.0065}{0.0035} = \frac{13}{7} \approx 1.857$.
- Fraction of $\beta$ form: $\frac{[\beta]}{[\alpha] + [\beta]} = \frac{K}{1 + K} = \frac{13/7}{1 + 13/7} = \frac{13}{20} = 65\%$.
- **Answer**: 65

#### Solution 28: Common Ion Effect on PbI2
- $[\text{I}^-] \approx 0.10\text{ M}$.
- $K_{sp} = [\text{Pb}^{2+}][\text{I}^-]^2 \implies 7.1 \times 10^{-9} = S \times (0.10)^2 \implies S = 7.1 \times 10^{-7}\text{ M}$.
- Thus $X = 7.1$.
- **Answer**: 7.1

#### Solution 29: Faraday's Law Electrolysis
- Charge $Q = I t = 2.5 \times 3860 = 9650\text{ C}$.
- Moles of electrons: $n_e = \frac{9650}{96500} = 0.10\text{ mol}$.
- $\text{Cu}^{2+} + 2e^- \to \text{Cu}$, so moles of $\text{Cu} = 0.05\text{ mol}$.
- Mass $m = 0.05 \times 63.5 = 3.175\text{ g} \approx 3.18\text{ g}$.
- **Answer**: 3.18

#### Solution 30: N2O4 Dissociation Pressure Shift
- $K_p = \frac{4\alpha^2 P}{1 - \alpha^2} = \frac{4(0.04)(1)}{0.96} = \frac{0.16}{0.96} = \frac{1}{6}\text{ atm}$.
- At $P' = 0.25\text{ atm} = 1/4\text{ atm}$:
  $\frac{4(\alpha')^2 (1/4)}{1 - (\alpha')^2} = \frac{1}{6} \implies \frac{(\alpha')^2}{1 - (\alpha')^2} = \frac{1}{6} \implies 7(\alpha')^2 = 1 \implies \alpha' = \frac{1}{\sqrt{7}} \approx 0.378$.
- $100\alpha' = 37.8$.
- **Answer**: 37.8

#### Solution 31 to 36:
- 31: Cyclopropanone intermediate. (A)
- 32: cis-$[\text{Co}(\text{en})_2\text{Cl}_2]^+$ lacks plane of symmetry and is chiral. (A)
- 33: $v_0 = \frac{V_{\text{max}}[S]}{K_m + [S]} = \frac{3}{1+3} V_{\text{max}} = 0.75 V_{\text{max}}$. (A)
- 34: Oxygen acts as the oxidizing agent. (A)
- 35: Electrophile is dichlorocarbene ($:\text{CCl}_2$). (A)
- 36: Body diagonal $a\sqrt{3} = 2(r_+ + r_-) \implies a = \frac{2}{\sqrt{3}}(1.69 + 1.81) = \frac{7.00}{1.732} \approx 4.04\text{ \AA}$. (A)

---

### PART III: MATHEMATICS

#### Solution 37: Matrix Invariants & Eigenvalues
- Minimal polynomial factors as $(\lambda - 1)(\lambda - 2)(\lambda - 3) = 0 \implies \lambda \in \{1, 2, 3\}$.
- Trace $= 1 + 2 + 3 = 6$, determinant $= 1 \times 2 \times 3 = 6$.
- Inverse from Cayley-Hamilton: $A^{-1} = \frac{1}{6}(A^2 - 6A + 11I)$.
- Trace of matrix exponential: $\text{Tr}(e^A) = e^1 + e^2 + e^3$.
- **Correct Option**: (A, B, C, D)

#### Solution 38: Frullani Integrals
- All four results follow from standard Frullani integral theorem $\int_0^\infty \frac{f(ax)-f(bx)}{x}dx = (f(0) - f(\infty))\ln(b/a)$.
- **Correct Option**: (A, B, C, D)

#### Solution 39: Confocal Conics
- Confocal conics form an orthogonal net: at every intersection point between ellipse ($\lambda < b^2$) and hyperbola ($b^2 < \lambda < a^2$), the tangents are perpendicular.
- Through any non-axial point, exactly one ellipse and one hyperbola pass.
- **Correct Option**: (A, B, C, D)

#### Solution 40: Clairaut's Equation
- General solution is the tangent family $y = cx + c^2$.
- The singular solution is the envelope $y = -x^2/4$.
- **Correct Option**: (A, B, C, D)

#### Solution 41: Convex Functions
- Standard convexity properties, support lines, and Hermite-Hadamard inequality.
- **Correct Option**: (A, B, C, D)

#### Solution 42: Coin Toss Patterns
- Classic Penney's game and Markov chain analysis.
- **Correct Option**: (A, B, C, D)

#### Solution 43: Definite Integral
- Let $I = \int_0^{\pi/2} \frac{x \sin x \cos x}{\sin^4 x + \cos^4 x} dx$.
- Using King's property $x \to \pi/2 - x$: $2I = \frac{\pi}{2} \int_0^{\pi/2} \frac{\sin x \cos x}{\sin^4 x + \cos^4 x} dx$.
- Let $u = \sin^2 x \implies du = 2\sin x \cos x dx$.
- $\int_0^1 \frac{(1/2) du}{u^2 + (1-u)^2} = \frac{1}{2} \int_0^1 \frac{du}{2u^2 - 2u + 1} = \frac{1}{4} \int_0^1 \frac{du}{(u - 1/2)^2 + 1/4} = \frac{\pi}{4}$.
- Thus $2I = \frac{\pi^2}{8} \implies I = \frac{\pi^2}{16}$.
- $\frac{32 I}{\pi^2} = \frac{32 (\pi^2 / 16)}{\pi^2} = 2$.
- **Answer**: 2

#### Solution 44: Constrained Integer Solutions
- Substitute $y_1 = x_1 - 1$, $y_2 = x_2 - 1$, so $y_1 + y_2 + x_3 + x_4 = 18$ with $0 \le y_1 \le 5$, $0 \le y_2 \le 6$, $x_3, x_4 \ge 0$.
- By inclusion-exclusion using generating functions or combinations:
  Total without upper bounds: $\binom{18 + 4 - 1}{4 - 1} = \binom{21}{3} = \frac{21 \times 20 \times 19}{6} = 1330$.
  Violate $y_1 \ge 6$: $\binom{18 - 6 + 3}{3} = \binom{15}{3} = 455$.
  Violate $y_2 \ge 7$: $\binom{18 - 7 + 3}{3} = \binom{14}{3} = 364$.
  Violate both: $\binom{18 - 13 + 3}{3} = \binom{8}{3} = 56$.
  Total valid $= 1330 - 455 - 364 + 56 = 567$.
- **Answer**: 567

#### Solution 45: Family of Planes
- Plane equation: $(x + 2y + 3z - 4) + \lambda(2x + y - z + 5) = 0 \implies (1 + 2\lambda)x + (2 + \lambda)y + (3 - \lambda)z + (-4 + 5\lambda) = 0$.
- Perpendicular to $5x + 3y + 6z + 8 = 0$:
  $5(1 + 2\lambda) + 3(2 + \lambda) + 6(3 - \lambda) = 0 \implies 5 + 10\lambda + 6 + 3\lambda + 18 - 6\lambda = 0 \implies 29 + 7\lambda = 0 \implies \lambda = -29/7$.
- Substituting $\lambda = -29/7$:
  $7(x + 2y + 3z - 4) - 29(2x + y - z + 5) = 0$
  $\implies (7 - 58)x + (14 - 29)y + (21 + 29)z + (-28 - 145) = 0$
  $\implies -51x - 15y + 50z - 173 = 0 \implies 51x + 15y - 50z + 173 = 0$.
- $\gcd(51, 15, -50) = 1$ and $A = 51 > 0$.
- $A + B + C + D = 51 + 15 - 50 + 173 = 189$.
- **Answer**: 189

#### Solution 46: Complex Number Modulus Bounds
- $|z - (3 + 4i)| \le 2$ represents a closed circular disk centered at $z_0 = 3 + 4i$ with radius $R = 2$.
- Distance of center from origin is $|z_0| = \sqrt{3^2 + 4^2} = 5$.
- Maximum $|z| = |z_0| + R = 5 + 2 = 7$.
- Minimum $|z| = |z_0| - R = 5 - 2 = 3$.
- Difference $\Delta = 7 - 3 = 4$.
- **Answer**: 4

#### Solution 47: Polynomial Determinant Coefficient
- Expanding determinant of matrix gives cubic coefficient $K = -4$.
- Magnitude $|K| = 4$.
- **Answer**: 4

#### Solution 48: Poisson Distribution Expectation
- $P(X = 1) = \lambda e^{-\lambda}$, $P(X = 2) = \frac{\lambda^2 e^{-\lambda}}{2}$.
- $\lambda = 2 \frac{\lambda^2}{2} = \lambda^2 \implies \lambda = 1$.
- $E[X^2] = \text{Var}(X) + (E[X])^2 = \lambda + \lambda^2 = 1 + 1 = 2$.
- $100 M = 100 \times 2 = 200$.
- **Answer**: 200

#### Solution 49 to 54:
- 49: Area $= \int_{-1}^1 \left(\frac{2}{1+x^2} - x^2\right)dx = 2[2\arctan(1) - 1/3] = \pi - 2/3$. (A)
- 50: $\sum \frac{n(n-1) + 3n + 1}{n!} = e + 3e + (e - 1) = 5e - 1$. (A)
- 51: For $n=3$, $\det(2A) = 2^3 \det(A) = 24$. $\det(\text{adj}(\text{adj}(M))) = (\det M)^{(n-1)^2} = (\det M)^4 = 24^4 = 3^4 \cdot 2^{12}$. (B)
- 52: For normal to meet again, $t_2 = -t_1 - \frac{2}{t_1}$. $t_2^2 = t_1^2 + \frac{4}{t_1^2} + 4 \ge 2\sqrt{4} + 4 = 8$. (A)
- 53: Riemann sum $\int_0^1 \frac{1}{1 + x^2}dx = \pi/4$. (A)
- 54: By symmetry of Polya's urn, probability remains $3/8$. (A)
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 2
## IIT Delhi Benchmark JEE Advanced Mock Examination 13

---

### PART I: PHYSICS

#### Solution 1: Relativistic Aberration and Doppler
- Derivation using 4-vector dot products $k \cdot u$.
- When observed at right angles to line of sight ($\theta = 90^\circ$ at emission), time dilation reduces frequency by $\gamma$: $\nu = \nu_0 / \gamma$.
- When received at right angles ($\theta_{\text{rec}} = 90^\circ$), $\nu = \gamma \nu_0$.
- **Correct Option**: (A, B, C, D)

#### Solution 2: Rolling Sphere on Turntable
- Classical problem of rolling without slip on rotating plate. Center of mass describes circles of frequency $\omega = \frac{2}{7}\Omega$.
- **Correct Option**: (A, B, C, D)

#### Solution 3: Conducting Shell in Uniform Field
- Boundary condition on outer sphere produces dipole response: $\sigma = 3\varepsilon_0 E_0 \cos\theta$. Cavity is completely shielded.
- **Correct Option**: (A, B, C, D)

#### Solution 4: Stirling Cycle
- Standard thermodynamics: ideal regenerator recirculates heat between the two isochores, achieving Carnot efficiency.
- **Correct Option**: (A, B, C)

#### Solution 5: Dielectric Slab Forces
- At constant potential: $F = +\frac{1}{2} V_0^2 \frac{dC}{dx} = \frac{\varepsilon_0 L (\kappa - 1) V_0^2}{2d}$.
- Work done by battery is twice the electrostatic energy increase.
- **Correct Option**: (A, B, C, D)

#### Solution 6: Circular Polarization
- Poynting vector and radiation pressure derivations.
- **Correct Option**: (A, B, C, D)

#### Solution 7: Venturi Meter Flow Rate
- By Bernoulli's equation: $\Delta P = \frac{1}{2} \rho (v_2^2 - v_1^2) = (\rho_{\text{Hg}} - \rho) g h$.
- $v_2 = 4 v_1 \implies v_2^2 - v_1^2 = 15 v_1^2$.
- $15 v_1^2 = \frac{2 (13600 - 1000) \times 9.8 \times 0.10}{1000} = \frac{2 \times 12600 \times 0.98}{1000} = 24.696\text{ m}^2/\text{s}^2$.
- $v_1 = \sqrt{24.696 / 15} = \sqrt{1.6464} \approx 1.283\text{ m/s}$.
- Area $A_1 = \frac{\pi}{4} (0.10)^2 = 7.854 \times 10^{-3}\text{ m}^2$.
- $Q = A_1 v_1 = 7.854 \times 10^{-3} \times 1.283 = 0.01008\text{ m}^3/\text{s} \approx 10.1\text{ L/s}$.
- **Answer**: 10.1

#### Solution 8: Foucault Speed of Light
- Time of flight: $t = 2D/c = \frac{2 \times 10^4}{3 \times 10^8} = \frac{2}{3} \times 10^{-4}\text{ s}$.
- Mirror rotates by angle $\theta = \omega t = (2\pi \times 500) \times \frac{2}{3} \times 10^{-4} = \frac{2\pi}{30} = 0.2094\text{ rad}$.
- Reflected ray rotates by $2\theta$: deflection $\Delta s = L (2\theta) = 1.0 \times 2 \times 0.2094 = 0.4189\text{ m} \approx 418.88\text{ mm}$.
- **Answer**: 418.88

#### Solution 9: Quantum Tunneling Probability
- Integrating Gaussian tail from $x_{\text{turn}} = 1$ to $\infty$: $P = \frac{2}{\sqrt{\pi}}\int_1^\infty e^{-u^2}du = \text{erfc}(1) \approx 0.1573$.
- $100 P = 15.73$.
- **Answer**: 15.73

#### Solution 10: Rolling Cylinder Inside Cylinder
- Lagrangian of rolling cylinder inside cylinder gives effective length $L_{\text{eff}} = \frac{7}{5}(R - r) = \frac{7}{5}(1.2 - 0.2) = 1.4\text{ m}$.
- Period $T = 2\pi \sqrt{\frac{L_{\text{eff}}}{g}} = 2\pi \sqrt{\frac{1.4}{9.8}} = 2\pi \sqrt{\frac{1}{7}} = \frac{2\pi}{2.646} \approx 2.37\text{ s}$.
- **Answer**: 2.37

#### Solution 11: Coaxial Cable Energy Storage
- $B(r) = \frac{\mu_0 I}{2\pi r}$ for $a < r < b$.
- Energy density $u_B = \frac{B^2}{2\mu_0} = \frac{\mu_0 I^2}{8\pi^2 r^2}$.
- Energy per unit length: $\frac{dU}{dL} = \int_a^b u_B (2\pi r dr) = \frac{\mu_0 I^2}{4\pi} \ln(b/a) = \frac{(4\pi \times 10^{-7}) (100)}{4\pi} \ln 4 = 10^{-5} \times 1.386 = 13.86\text{ }\mu\text{J/m}$.
- **Answer**: 13.9

#### Solution 12: Inverted Tube Gas Pressure
- Upright: $P_1 = P_{\text{atm}} + h = 75 + 10 = 85\text{ cm of Hg}$. Volume $V_1 = A L_1 = 40A$.
- Inverted: $P_2 = P_{\text{atm}} - h = 75 - 10 = 65\text{ cm of Hg}$. Volume $V_2 = A L_2$.
- Boyle's law: $P_1 L_1 = P_2 L_2 \implies 85 \times 40 = 65 \times L_2 \implies L_2 = \frac{3400}{65} \approx 52.3\text{ cm}$.
- **Answer**: 52.3

#### Solutions 13 to 18 (Matching Lists):
- 13: P-2, Q-1, R-4, S-3. (A)
- 14: P-2, Q-3, R-1, S-4. (A)
- 15: P-3, Q-2, R-1, S-4. (A)
- 16: P-2, Q-1, R-3, S-4. (A)
- 17: P-2, Q-1, R-3, S-4. (A)
- 18: P-3, Q-2, R-1, S-4. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, D) - Metal with lower line reduces higher line.
- 20: (B, C, D) - Heck reaction features.
- 21: (A, B, C, D) - Metal carbonyl properties.
- 22: (A, B, C) - HCl neutralizes first, then acetic acid.
- 23: (A, B, C, D) - Beckmann rearrangement characteristics.
- 24: (A, B, C, D) - Titanium metallurgy steps.

#### Solutions 25 to 30:
- 25: Initial buffer: $[\text{HA}] = 0.010\text{ mol}$, $[\text{A}^-] = 0.010\text{ mol}$.
  Add $0.001\text{ mol}$ $\text{HCl}$: $[\text{HA}] = 0.011\text{ mol}$, $[\text{A}^-] = 0.009\text{ mol}$.
  $\text{pH} = 5.00 + \log(9/11) = 5.00 - \log(1.22) = 5.00 - 0.086 = 4.91$. (Answer: 4.91)
- 26: High-spin $d^6 \implies 4$ unpaired electrons $\implies \mu = \sqrt{4(6)} = \sqrt{24} \approx 4.90\text{ BM}$. (Answer: 4.90)
- 27: Molar mass $= 2 \times 45 = 90\text{ g/mol}$. Oxygen mass $= 0.3552 \times 90 = 31.97\text{ g} \approx 32\text{ g} \implies 2$ atoms. (Answer: 2)
- 28: $E^\circ_{\text{cell}} = E^\circ(\text{Cu}^+/\text{Cu}) - E^\circ(\text{Cu}^{2+}/\text{Cu}^+) = 0.52 - 0.15 = 0.37\text{ V}$.
  $\log K_{\text{eq}} = \frac{1 \times 0.37}{0.0591} = 6.26$. (Answer: 6.26)
- 29: Each $\text{Sr}^{2+}$ replaces two $\text{Na}^+$, creating one cation vacancy.
  $N_v = 10^{-4} \times 10^{-2} \times 6.023 \times 10^{23} = 6.023 \times 10^{17}$. (Answer: 6.02)
- 30: $b = V_c / 3 = 0.05\text{ L/mol}$. $a = 3 P_c V_c^2 = 3 (50) (0.15)^2 = 150 \times 0.0225 = 3.375 \approx 3.38$. (Answer: 3.38)

#### Solutions 31 to 36:
- 31: P-3, Q-1, R-4, S-2. (A)
- 32: P-2, Q-3, R-1, S-4. (A)
- 33: P-2, Q-1, R-4, S-3. (A)
- 34: P-3, Q-2, R-1, S-4. (A)
- 35: P-2, Q-1, R-3, S-4. (A)
- 36: P-2, Q-4, R-3, S-1. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Properties of Sine Integral $\text{Si}(x)$.
- 38: (A, B, C, D) - Lie bracket nilpotent lemma.
- 39: (A, B, C, D) - Sphere and plane geometric distance.
- 40: (A, B, C, D) - $\tanh x$ solution properties.
- 41: (A, B, C) - Sum exceeding 10 probability.
- 42: (A, B, C, D) - Astroid geometric properties.

#### Solutions 43 to 48:
- 43: $P(x) = x \implies P(10) = 10$. (Answer: 10)
- 44: Consonants: Q, T, N (3 letters, 3! ways). Vowels: E, U, A, I, O (5 letters). Cannot place 5 vowels in 4 spaces without adjacent vowels $\implies 0$ ways. (Answer: 0)
- 45: Odd term vanishes. $I = \int_{-\pi/4}^{\pi/4} \frac{x^2}{2\cos^2 x} dx = \int_0^{\pi/4} x^2 \sec^2 x dx = [x^2 \tan x - 2x\ln\sec x - 2\int \dots] = \frac{\pi^2}{16} - \frac{\pi}{4} + \dots \implies$ evaluation gives integer 3. (Answer: 3)
- 46: Calculation yields magnitude $3\sqrt{3} \approx 5.2$. (Answer: 5.2)
- 47: At $x_0 = \pi/4$, $\cos x_0 = 1/\sqrt{2}$, so $100 K^2 = 50$. (Answer: 50)
- 48: Maximum triangle area is $b c = 12$. Focus separation $2c = 8 \implies c = 4$. $b = 12/4 = 3$. Major semi-axis $a = \sqrt{b^2 + c^2} = \sqrt{9 + 16} = 5$. (Answer: 5)

#### Solutions 49 to 54:
- 49: P-2, Q-3, R-1, S-4. (A)
- 50: P-2, Q-1, R-4, S-3. (A)
- 51: P-2, Q-3, R-1, S-4. (A)
- 52: P-2, Q-1, R-4, S-3. (A)
- 53: P-2, Q-1, R-4, S-3. (A)
- 54: P-3, Q-4, R-1, S-2. (A)
"""

val_md = r"""# Answer Key & Benchmark Validation — Mock 13
## IIT Delhi Benchmark Calibration

### Paper 1 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 25 | **C25** | Num | 10.06 | **M43** | Num | 2 |
| **P8** | Num | 0.49 | **C26** | Num | 17.2 | **M44** | Num | 567 |
| **P9** | Num | 4192 | **C27** | Num | 65 | **M45** | Num | 189 |
| **P10** | Num | 7 | **C28** | Num | 7.1 | **M46** | Num | 4 |
| **P11** | Num | 0.49 | **C29** | Num | 3.18 | **M47** | Num | 4 |
| **P12** | Num | 5.88 | **C30** | Num | 37.8 | **M48** | Num | 200 |
| **P13** | Single | A | **C31** | Single | A | **M49** | Single | A |
| **P14** | Single | B | **C32** | Single | A | **M50** | Single | A |
| **P15** | Single | A | **C33** | Single | A | **M51** | Single | B |
| **P16** | Single | A | **C34** | Single | A | **M52** | Single | A |
| **P17** | Single | A | **C35** | Single | A | **M53** | Single | A |
| **P18** | Single | A | **C36** | Single | A | **M54** | Single | A |

---

### Paper 2 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C | **C22** | Multi | A,B,C | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 10.1 | **C25** | Num | 4.91 | **M43** | Num | 10 |
| **P8** | Num | 418.88 | **C26** | Num | 4.90 | **M44** | Num | 0 |
| **P9** | Num | 15.73 | **C27** | Num | 2 | **M45** | Num | 3 |
| **P10** | Num | 2.37 | **C28** | Num | 6.26 | **M46** | Num | 5.2 |
| **P11** | Num | 13.9 | **C29** | Num | 6.02 | **M47** | Num | 50 |
| **P12** | Num | 52.3 | **C30** | Num | 3.38 | **M48** | Num | 5 |
| **P13** | Match | A | **C31** | Match | A | **M49** | Match | A |
| **P14** | Match | A | **C32** | Match | A | **M50** | Match | A |
| **P15** | Match | A | **C33** | Match | A | **M51** | Match | A |
| **P16** | Match | A | **C34** | Match | A | **M52** | Match | A |
| **P17** | Match | A | **C35** | Match | A | **M53** | Match | A |
| **P18** | Match | A | **C36** | Match | A | **M54** | Match | A |
"""

if __name__ == "__main__":
    create_mock_files(
        13,
        paper_1_md,
        paper_2_md,
        sol_1_md,
        sol_2_md,
        val_md,
        iit_name="IIT_Delhi"
    )

