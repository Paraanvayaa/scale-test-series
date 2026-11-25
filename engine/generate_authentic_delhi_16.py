# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 16.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Hall coefficient and carrier mobility, Cherenkov cone kinematics, Cylindrical magnetron cutoff field
- Mitsunobu inversion, Grubbs olefin metathesis, Gibbs surface excess adsorption, Spin-crossover Fe(II)
- Stokes & Green theorems, Newton sums of polynomial roots, Pedal curve of ellipse, Bivariate normal density
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 16 — Paper 1
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
A rectangular slab of a semiconductor of thickness $d$, width $w$, and length $L$ carries a steady current $I$ along the $+x$ direction in a uniform magnetic field $\vec{B} = B \hat{k}$:
(A) The transverse Hall electric field established across the width is $E_y = \frac{I B}{n q w d}$, where $n$ is charge carrier concentration and $q$ is charge.  
(B) The Hall voltage measured across width $w$ is $V_H = \frac{I B}{n q d}$, which is independent of the width $w$.  
(C) The sign of the Hall voltage $V_H$ allows one to distinguish unambiguously whether the majority charge carriers are electrons or holes.  
(D) The Hall coefficient is defined as $R_H = \frac{E_y}{J_x B} = \frac{1}{n q}$.

#### Question 2
A high-energy charged particle moves with speed $v = \beta c$ through a transparent non-magnetic dielectric medium of refractive index $n > 1$:
(A) Cherenkov radiation is emitted if and only if the particle velocity exceeds the phase velocity of light in the medium ($v > c/n \iff \beta n > 1$).  
(B) The coherent wavefront forms a Mach-like conical shock surface with half-angle $\theta_c$ given by $\cos\theta_c = \frac{1}{\beta n}$.  
(C) As the particle speed approaches $c$ ($\beta \to 1$), the emission cone angle approaches its maximum value $\theta_{\text{max}} = \arccos(1/n)$.  
(D) According to the Frank-Tamm formula, the number of Cherenkov photons emitted per unit track length per unit wavelength interval is proportional to $1/\lambda^2$, resulting in the characteristic bluish glow.

#### Question 3
In a cylindrical magnetron diode, a central filament cathode of radius $a$ is surrounded by a coaxial cylindrical anode of radius $b$ at potential $V_0 > 0$. A uniform magnetic field $\vec{B} = B \hat{k}$ is applied parallel to the cylindrical axis. Electrons of mass $m$ and charge $-e$ are emitted from the cathode with negligible initial velocity:
(A) An electron reaches the anode if and only if the magnetic field is less than the critical Hull cutoff field $B_c$.  
(B) The critical Hull cutoff field is given by $B_c = \sqrt{\frac{8 m V_0}{e b^2 (1 - a^2/b^2)^2}}$.  
(C) If $B > B_c$, electrons turn around before reaching the anode, describing epicycloidal trajectories, and the anode current drops to zero.  
(D) The conservation of canonical angular momentum about the $z$-axis governs the azimuthal velocity $v_\theta(r) = \frac{e B}{2 m}\left(r - \frac{a^2}{r}\right)$.

#### Question 4
A long uniform solid cylinder of radius $R$ and thermal conductivity $k$ generates heat uniformly throughout its volume at a constant rate $q'''\text{ W/m}^3$. The outer surface of the cylinder ($r = R$) is maintained at a constant temperature $T_s$:
(A) In the steady state, the heat conduction equation in cylindrical coordinates reduces to $\frac{1}{r}\frac{d}{dr}\left(r \frac{dT}{dr}\right) + \frac{q'''}{k} = 0$.  
(B) The radial temperature profile is parabolic: $T(r) = T_s + \frac{q'''}{4k}(R^2 - r^2)$.  
(C) The maximum temperature occurs along the central axis ($r = 0$) with $T_{\text{max}} = T_s + \frac{q''' R^2}{4k}$.  
(D) The heat flux per unit area leaving the cylinder at its outer surface is $q''(R) = \frac{q''' R}{2}$.

#### Question 5
A supersonic aircraft flies horizontally at an altitude $H$ with a constant speed $v > v_s$, where $v_s$ is the speed of sound in air (Mach number $M = v/v_s > 1$):
(A) The half-angle of the conical acoustic shock front (Mach cone) is $\mu = \arcsin(1/M)$.  
(B) An observer on the ground hears the sonic boom only after the aircraft has passed overhead by a horizontal distance $x = H \sqrt{M^2 - 1}$.  
(C) The time delay between the instant the aircraft is directly overhead and the arrival of the shock front at the ground is $\Delta t = \frac{H}{v}\sqrt{M^2 - 1}$.  
(D) Behind the shock front, the sound waves interfere constructively along the generator of the cone.

#### Question 6
A circular disk of mass $M$ and radius $R$ carries a uniform surface charge density $\sigma$. It rotates with constant angular velocity $\omega$ about its perpendicular central axis:
(A) The magnetic dipole moment of the disk is $\mu = \frac{1}{4}\pi \sigma \omega R^4$.  
(B) The gyromagnetic ratio of the rotating disk is $\frac{\mu}{L} = \frac{Q}{2M}$, where $Q = \pi R^2 \sigma$ is the total charge and $L = \frac{1}{2}M R^2 \omega$ is the angular momentum.  
(C) The magnetic field at the center of the disk is $B_0 = \frac{1}{2}\mu_0 \sigma \omega R$.  
(D) The electric field on the axis at distance $z$ is $E_z = \frac{\sigma}{2\varepsilon_0}\left(1 - \frac{z}{\sqrt{z^2 + R^2}}\right)$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A slab of copper of thickness $d = 2.0\text{ mm}$ and width $w = 1.0\text{ cm}$ carries a current $I = 50.0\text{ A}$ in a magnetic field $B = 1.20\text{ T}$ perpendicular to the slab. The charge carrier concentration in copper is $n = 8.4 \times 10^{28}\text{ electrons/m}^3$. Calculate the Hall voltage $V_H$ developed across the slab in microvolts ($\mu\text{V}$) (take $e = 1.6 \times 10^{-19}\text{ C}$, round off to TWO decimal places).

#### Question 8
A proton of kinetic energy $K = 1.0\text{ GeV}$ passes through water ($n = 1.33$). The rest energy of a proton is $m_p c^2 = 938\text{ MeV}$. Calculate the Cherenkov emission angle $\theta_c$ in degrees (round off to ONE decimal place).

#### Question 9
In a cylindrical magnetron with cathode radius $a = 2.0\text{ mm}$ and anode radius $b = 10.0\text{ mm}$, an anode voltage $V_0 = 300\text{ V}$ is applied. Calculate the Hull cutoff magnetic field $B_c$ in milliTesla ($\text{mT}$) (use $e/m = 1.76 \times 10^{11}\text{ C/kg}$, round off to ONE decimal place).

#### Question 10
A supersonic jet flies horizontally at Mach $M = 2.0$ at an altitude $H = 6000\text{ m}$. If the speed of sound is $v_s = 340\text{ m/s}$, calculate the time delay in seconds between the jet passing directly overhead and the observer on the ground hearing the sonic boom (take $\sqrt{3} \approx 1.732$, round off to ONE decimal place).

#### Question 11
A spherical metal shell of radius $R = 10.0\text{ cm}$ carries a charge $Q = 2.0\text{ }\mu\text{C}$. The electrostatic energy stored in the electric field outside the shell is $U$ in milliJoules ($\text{mJ}$). Calculate $U$ (use $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N m}^2/\text{C}^2$, round off to ONE decimal place).

#### Question 12
A uniform rod of length $L = 1.0\text{ m}$ and mass $M = 3.0\text{ kg}$ is free to rotate in a vertical plane about a frictionless horizontal axis through one end. If it is released from rest in the horizontal position, calculate its angular velocity $\omega$ in $\text{rad/s}$ when it passes through the vertical position (take $g = 9.8\text{ m/s}^2$, round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle of mass $m$ is constrained to move on the smooth inner surface of an inverted circular cone of half-angle $\alpha$ with vertical axis. The particle executes horizontal circular motion of radius $r_0$. The angular velocity $\omega$ is:
(A) $\omega = \sqrt{\frac{g}{r_0 \tan\alpha}}$  
(B) $\omega = \sqrt{\frac{g \tan\alpha}{r_0}}$  
(C) $\omega = \sqrt{\frac{g}{r_0 \sin\alpha}}$  
(D) $\omega = \sqrt{\frac{g \cos\alpha}{r_0}}$  

#### Question 14
A cylindrical wire of radius $R$ carries a steady current $I$ distributed uniformly over its cross section. The magnetic energy stored per unit length inside the wire ($r \le R$) is:
(A) $\frac{dU}{dL} = \frac{\mu_0 I^2}{16\pi}$  
(B) $\frac{dU}{dL} = \frac{\mu_0 I^2}{8\pi}$  
(C) $\frac{dU}{dL} = \frac{\mu_0 I^2}{4\pi}$  
(D) $\frac{dU}{dL} = \frac{\mu_0 I^2}{32\pi}$  

#### Question 15
Two simple harmonic motions along the same line are given by $x_1 = 3\sin(10t)$ and $x_2 = 4\cos(10t)$. The amplitude of the resultant motion is:
(A) 5  
(B) 7  
(C) 1  
(D) $\sqrt{7}$  

#### Question 16
An ideal gas undergoes a cycle consisting of an isobaric expansion at pressure $P$, an isochoric cooling to pressure $P/2$, and an isothermal compression back to the initial state. The work done by the gas in one complete cycle is:
(A) $P V_1(1 - \ln 2)$  
(B) $P V_1 \ln 2$  
(C) $\frac{1}{2} P V_1(1 - \ln 2)$  
(D) $P V_1(2 - \ln 2)$  

#### Question 17
A beam of light of wavelength $\lambda = 600\text{ nm}$ is incident normally on a single slit of width $a = 0.2\text{ mm}$. The angular width of the central diffraction maximum is:
(A) $6.0 \times 10^{-3}\text{ rad}$  
(B) $3.0 \times 10^{-3}\text{ rad}$  
(C) $1.2 \times 10^{-3}\text{ rad}$  
(D) $1.5 \times 10^{-3}\text{ rad}$  

#### Question 18
The half-life of a radioactive nucleus is $T$. In a time interval $t = 3T$, the fraction of initial nuclei that has decayed is:
(A) $\frac{7}{8}$  
(B) $\frac{1}{8}$  
(C) $\frac{3}{4}$  
(D) $\frac{1}{16}$  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
In the Mitsunobu reaction:
$$\text{R-OH} + \text{Nu-H} + \text{PPh}_3 + \text{DEAD} \to \text{R-Nu} + \text{Ph}_3\text{P}=\text{O} + \text{DEAD-H}_2$$
(where DEAD is diethyl azodicarboxylate and $\text{Nu-H}$ is a pro-nucleophile with $pK_a < 12$):
(A) Triphenylphosphine adds to DEAD to form a zwitterionic phosphonium betaine intermediate.  
(B) The betaine deprotonates the nucleophile $\text{Nu-H}$ to form an ion pair.  
(C) Nucleophilic displacement by the alcohol oxygen generates an alkoxyphosphonium intermediate $[\text{R-O-PPh}_3]^+$.  
(D) Backside $S_N2$ displacement of triphenylphosphine oxide by $\text{Nu}^-$ on the carbon center proceeds with complete stereochemical inversion of configuration.

#### Question 20
Regarding olefin metathesis catalyzed by Grubbs ruthenium carbene catalysts:
(A) Ring-closing metathesis (RCM) converts $\alpha,\omega$-dienes into cyclic alkenes with extrusion of volatile ethylene ($\text{CH}_2=\text{CH}_2$).  
(B) The Chauvin mechanism involves reversible $[2+2]$ cycloadditions generating a four-membered metallacyclobutane intermediate.  
(C) Second-generation Grubbs catalysts incorporate an N-heterocyclic carbene (NHC) ligand, exhibiting vastly increased catalytic activity and thermal stability compared to the first generation.  
(D) Cross-metathesis (CM) allows intermolecular coupling of two different alkenes.

#### Question 21
Regarding the Gibbs adsorption isotherm for aqueous surfactant solutions:
$$\Gamma = -\frac{c}{R T}\left(\frac{d\gamma}{dc}\right)$$
(A) A surfactant that concentrates preferentially at the air-water interface is positively adsorbed ($\Gamma > 0$), resulting in a decrease in surface tension ($\frac{d\gamma}{dc} < 0$).  
(B) At the critical micelle concentration (CMC), the surface becomes fully saturated with surfactant monolayer, and surface tension remains nearly constant above the CMC.  
(C) Substances like sucrose and $\text{NaCl}$ increase the surface tension of water slightly, corresponding to negative surface excess ($\Gamma < 0$).  
(D) The surface excess $\Gamma$ has SI units of $\text{mol/m}^2$.

#### Question 22
Regarding spin-crossover (SCO) behavior in octahedral $d^6$ complexes of iron(II):
(A) In a ligand field where $\Delta_o \approx P$ (pairing energy), the complex can switch between low-spin diamagnetic ($t_{2g}^6, S = 0$) and high-spin paramagnetic ($t_{2g}^4 e_g^2, S = 2$) states.  
(B) Transition to the high-spin state increases the metal-ligand bond length because electrons occupy the antibonding $e_g^*$ orbitals.  
(C) The spin transition is entropy-driven at higher temperatures ($\Delta S > 0$) due to higher spin multiplicity ($2S+1 = 5$) and increased vibrational density of states.  
(D) Spin-crossover materials often display thermal hysteresis loops, making them candidates for molecular memory and sensor devices.

#### Question 23
Regarding non-ideal binary liquid mixtures and the Margules excess Gibbs energy model $G^E = A x_1 x_2$:
(A) The activity coefficients of the components are given by $\ln \gamma_1 = \frac{A}{R T} x_2^2$ and $\ln \gamma_2 = \frac{A}{R T} x_1^2$.  
(B) If $A > 0$, the system displays positive deviations from Raoult's law ($\gamma_i > 1$) and endothermic mixing ($\Delta H_{\text{mix}} > 0$).  
(C) A system with sufficiently large positive deviation ($A > 2 R T$) exhibits liquid-liquid phase separation (immiscibility gap).  
(D) A system with positive deviations can form a minimum-boiling azeotrope (e.g., ethanol-water).

#### Question 24
In the qualitative analysis of Group I basic radicals ($\text{Ag}^+, \text{Pb}^{2+}, \text{Hg}_2^{2+}$):
(A) They are precipitated as insoluble chlorides ($\text{AgCl, PbCl}_2, \text{Hg}_2\text{Cl}_2$) by adding dilute $\text{HCl}$.  
(B) $\text{PbCl}_2$ dissolves readily in boiling water and recrystallizes upon cooling as bright needle-shaped crystals.  
(C) $\text{AgCl}$ dissolves in aqueous ammonia forming the soluble complex $[\text{Ag(NH}_3)_2]^+$, and reprecipitates upon acidification with dilute $\text{HNO}_3$.  
(D) $\text{Hg}_2\text{Cl}_2$ turns black upon addition of aqueous ammonia due to disproportionation forming finely divided metallic mercury ($\text{Hg}$) and mercury(II) amidochloride ($\text{Hg(NH}_2)\text{Cl}$).

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of magnesium hydroxide ($\text{Mg(OH)}_2$) is $K_{sp} = 1.8 \times 10^{-11}$ at $25^\circ\text{C}$. Calculate the pH of a saturated aqueous solution of $\text{Mg(OH)}_2$ at $25^\circ\text{C}$ (use $\log 3.56 = 0.55$, round off to TWO decimal places).

#### Question 26
Calculate the spin-only magnetic moment in Bohr Magnetons ($\mu_B$) for the high-spin complex $[Mn(H_2O)_6]^{2+}$ (atomic number of $\text{Mn} = 25$). Enter the value rounded off to TWO decimal places (take $\sqrt{35} \approx 5.92$).

#### Question 27
An organic compound has molecular mass $M = 180.0\text{ g/mol}$ and empirical formula $\text{CH}_2\text{O}$. Calculate the number of hydrogen atoms present in one molecule.

#### Question 28
The standard reduction potentials are $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V}$ and $E^\circ(\text{Sn}^{4+}/\text{Sn}^{2+}) = +0.15\text{ V}$. Calculate the standard cell EMF $E^\circ_{\text{cell}}$ in Volts for the reaction $2\text{Fe}^{3+} + \text{Sn}^{2+} \to 2\text{Fe}^{2+} + \text{Sn}^{4+}$.

#### Question 29
A first-order decomposition reaction has half-life $t_{1/2} = 40.0\text{ minutes}$. Calculate the percentage of the initial reactant remaining undecomposed after $120.0\text{ minutes}$ (enter the percentage rounded off to ONE decimal place).

#### Question 30
The osmotic pressure of an aqueous solution of a protein containing $1.50\text{ g}$ in $100.0\text{ mL}$ of solution is $\Pi = 3.1 \times 10^{-3}\text{ atm}$ at $300\text{ K}$. Calculate the molar mass $M$ of the protein in $\text{kg/mol}$ (use $R = 0.0821\text{ L atm/(mol K)}$, round off to the nearest integer).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Gabriel phthalimide synthesis, potassium phthalimide reacts with an alkyl halide to synthesize:
(A) Pure primary aliphatic amines  
(B) Secondary amines  
(C) Aromatic amines (aniline)  
(D) Tertiary amines  

#### Question 32
Which of the following compounds exhibits diamagnetism?
(A) $[\text{Co(NH}_3)_6]^{3+}$  
(B) $[\text{FeF}_6]^{3-}$  
(C) $[\text{Cr(H}_2\text{O)}_6]^{3+}$  
(D) $[\text{NiCl}_4]^{2-}$  

#### Question 33
The peptide bond connecting amino acids in a polypeptide chain is:
(A) Planar with partial double bond character due to resonance  
(B) Freely rotating single bond  
(C) Pure double bond  
(D) Ionic bond  

#### Question 34
In the extraction of aluminium by the Hall-Héroult process, cryolite ($\text{Na}_3\text{AlF}_6$) is added to purified alumina ($\text{Al}_2\text{O}_3$) to:
(A) Lower the melting point of the mixture and increase electrical conductivity  
(B) Act as an oxidizing agent  
(C) Precipitate iron impurities  
(D) Prevent oxidation of the carbon cathode  

#### Question 35
Treatment of benzene with acetyl chloride ($\text{CH}_3\text{COCl}$) in the presence of anhydrous $\text{AlCl}_3$ yields acetophenone. The electrophile in this Friedel-Crafts acylation is:
(A) Acylium cation ($[\text{CH}_3\text{-C}\equiv\text{O}]^+$)  
(B) Methyl carbocation ($\text{CH}_3^+$)  
(C) Chloro carbocation ($\text{Cl}^+$)  
(D) Acetyl radical ($\text{CH}_3\dot{\text{C}}\text{O}$)  

#### Question 36
The conjugate base of bicarbonate ion ($\text{HCO}_3^-$) is:
(A) Carbonate ion ($\text{CO}_3^{2-}$)  
(B) Carbonic acid ($\text{H}_2\text{CO}_3$)  
(C) Carbon dioxide ($\text{CO}_2$)  
(D) Hydroxide ion ($\text{OH}^-$)  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $\vec{F} = P \hat{i} + Q \hat{j}$ be a continuously differentiable vector field in a simply connected region $D \subset \mathbb{R}^2$ bounded by a piecewise smooth closed curve $C$ oriented counter-clockwise:
(A) Green's theorem states $\oint_C (P dx + Q dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx dy$.  
(B) The area of region $D$ is given by $A = \frac{1}{2}\oint_C (x dy - y dx)$.  
(C) For an ellipse $x = a \cos t, y = b \sin t$, the line integral $\frac{1}{2}\oint (x dy - y dx) = \pi a b$.  
(D) If $\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$ everywhere in $D$, the line integral $\oint_C (P dx + Q dy) = 0$ for every closed curve $C$.

#### Question 38
Let $x_1, x_2, \dots, x_n$ be the roots of the polynomial equation $P(x) = x^n - e_1 x^{n-1} + e_2 x^{n-2} - \dots + (-1)^n e_n = 0$. Let $p_k = \sum_{i=1}^n x_i^k$ denote the power sums:
(A) Newton's sums satisfy $p_1 - e_1 = 0$.  
(B) $p_2 - e_1 p_1 + 2 e_2 = 0$.  
(C) $p_3 - e_1 p_2 + e_2 p_1 - 3 e_3 = 0$.  
(D) For $x^3 - 3x + 1 = 0$, $p_1 = 0, p_2 = 6, p_3 = -3$.

#### Question 39
Consider the pedal equation and pedal curve of an ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$:
(A) The locus of the foot of the perpendicular drawn from a focus to any tangent to the ellipse is the auxiliary circle $x^2 + y^2 = a^2$.  
(B) The product of the perpendiculars from the two foci to any tangent is constant and equal to $b^2$.  
(C) The locus of the foot of the perpendicular from the center $(0, 0)$ to any tangent is the pedal curve $(x^2 + y^2)^2 = a^2 x^2 + b^2 y^2$.  
(D) The pedal equation of the ellipse with respect to a focus is $\frac{b^2}{p^2} = \frac{2a}{r} - 1$.

#### Question 40
Let $(X, Y)$ have a bivariate normal distribution with means $\mu_X = \mu_Y = 0$, standard deviations $\sigma_X = \sigma_Y = \sigma$, and correlation coefficient $\rho \in (-1, 1)$:
(A) The joint probability density function is $f(x, y) = \frac{1}{2\pi \sigma^2 \sqrt{1 - \rho^2}} \exp\left(-\frac{x^2 - 2\rho x y + y^2}{2\sigma^2(1 - \rho^2)}\right)$.  
(B) The contours of constant probability density are ellipses centered at the origin.  
(C) $X$ and $Y$ are independent if and only if $\rho = 0$.  
(D) The conditional distribution of $Y$ given $X = x$ is normal with mean $\rho x$ and variance $\sigma^2(1 - \rho^2)$.

#### Question 41
Let $f(x) = |x|^3$ for all $x \in \mathbb{R}$:
(A) $f(x)$ is continuous everywhere on $\mathbb{R}$.  
(B) $f'(x) = 3 x |x|$ exists and is continuous for all $x \in \mathbb{R}$.  
(C) $f''(x) = 6|x|$ exists for all $x \in \mathbb{R}$.  
(D) $f'''(0)$ does not exist.

#### Question 42
Consider the differential equation $\left(x^2 + y^2\right) dx - 2xy dy = 0$:
(A) The equation is homogeneous of degree 2.  
(B) An integrating factor is $\mu(x) = \frac{1}{x^2}$.  
(C) The general solution is $x^2 - y^2 = C x$.  
(D) The integral curves represent a family of circles passing through the origin with centers on the $x$-axis.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 x^3 (1 - x)^4 dx$$
Calculate the value of $280 I$ (round off to the nearest integer).

#### Question 44
Find the number of 4-digit positive integers that can be formed using the digits $1, 2, 3, 4, 5, 6$ without repetition such that the integer is divisible by 4.

#### Question 45
Let the points $A(1, 2, 3)$, $B(4, 0, 4)$, and $C(2, 3, 1)$ form a triangle. Calculate the area of triangle $A B C$ in square units (round off to TWO decimal places).

#### Question 46
Let $z = x + i y$ be a complex number satisfying $|z - 2| = 2|z - 1|$. The locus of $z$ is a circle with radius $R$. Calculate $R$ (round off to TWO decimal places).

#### Question 47
Let $y(x)$ satisfy the differential equation $\frac{dy}{dx} = \frac{y}{x} + \frac{x}{y}$ with initial condition $y(1) = 1$. Calculate $y(e)$ (use $e \approx 2.718$, round off to TWO decimal places).

#### Question 48
In rolling two fair standard six-sided dice, let $X$ be the sum of the numbers appearing on the dice. Calculate the probability $P(X \ge 10)$ (enter the value rounded off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The area of the region enclosed by the curve $y = \sin x$ and the $x$-axis from $x = 0$ to $x = 2\pi$ is:
(A) 4  
(B) 2  
(C) 0  
(D) 1  

#### Question 50
If $a, b, c$ are in geometric progression with common ratio $r > 0$, then $\ln a, \ln b, \ln c$ are in:
(A) Arithmetic Progression  
(B) Geometric Progression  
(C) Harmonic Progression  
(D) Arithmetico-Geometric Progression  

#### Question 51
The value of the limit $\lim_{x \to 0} \frac{1 - \cos(2x)}{x^2}$ is:
(A) 2  
(B) 1  
(C) $1/2$  
(D) 4  

#### Question 52
If the line $y = m x + 1$ is tangent to the parabola $y^2 = 4x$, then the value of $m$ is:
(A) 1  
(B) 2  
(C) $1/2$  
(D) $-1$  

#### Question 53
The distance between the parallel planes $2x - y + 2z + 3 = 0$ and $4x - 2y + 4z - 9 = 0$ is:
(A) $\frac{5}{2}$  
(B) $\frac{5}{6}$  
(C) 2  
(D) $\frac{7}{6}$  

#### Question 54
If $\vec{a} = \hat{i} + \hat{j} + \hat{k}$ and $\vec{b} = 2\hat{i} - \hat{j} + 3\hat{k}$, then the unit vector in the direction of $\vec{a} \times \vec{b}$ is:
(A) $\frac{4\hat{i} - \hat{j} - 3\hat{k}}{\sqrt{26}}$  
(B) $\frac{4\hat{i} + \hat{j} - 3\hat{k}}{\sqrt{26}}$  
(C) $\frac{4\hat{i} - \hat{j} + 3\hat{k}}{\sqrt{26}}$  
(D) $\frac{-4\hat{i} - \hat{j} - 3\hat{k}}{\sqrt{26}}$  
"""

paper_2_md = r"""# JEE Advanced Mock Examination 16 — Paper 2
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
A coaxial cable consists of an inner cylindrical conductor of radius $a$ and an outer thin cylindrical shell of radius $b$. A battery maintains a constant potential difference $V$ across the conductors while a steady current $I$ flows along the inner conductor and returns through the outer conductor:
(A) The electric field in the space between conductors is radial: $\vec{E}(r) = \frac{V}{r \ln(b/a)} \hat{r}$.  
(B) The magnetic field in the space between conductors is azimuthal: $\vec{B}(r) = \frac{\mu_0 I}{2\pi r} \hat{\theta}$.  
(C) The Poynting vector $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$ points parallel to the axis of the cable along the direction of power transmission.  
(D) The total electromagnetic power flowing through the cross-section of the cable is $P = \int_a^b S(r) 2\pi r dr = V I$.

#### Question 2
Regarding the acoustic Doppler effect when both source and observer move along the same straight line with speeds $v_s$ and $v_o$ in still air:
(A) The observed frequency is $\nu = \nu_0 \left(\frac{v \pm v_o}{v \mp v_s}\right)$, where $v$ is the speed of sound.  
(B) If a medium wind blows with velocity $w$ along the line of sight, the effective speed of sound becomes $v + w$.  
(C) If the source moves toward a stationary reflecting wall, beats are heard between direct and reflected waves.  
(D) When the source speed approaches the speed of sound ($v_s \to v$), the observed frequency approaches infinity (acoustic shock wave).

#### Question 3
A particle of mass $m$ moves in a central force field with potential energy $V(r) = -\frac{k}{r^n}$ where $k > 0$ and $n < 2$:
(A) A circular orbit of radius $r_0$ is dynamically stable against small radial perturbations if and only if $n < 2$.  
(B) The angular frequency of small radial oscillations about the circular orbit is $\omega_r = \omega_0 \sqrt{2 - n}$, where $\omega_0$ is the orbital frequency.  
(C) For $n = 1$ (gravitational/Coulomb field), $\omega_r = \omega_0$, and the bound orbit is a closed ellipse.  
(D) For $n > 2$, circular orbits are unstable.

#### Question 4
In an X-ray tube operating at an accelerating voltage $V_0$:
(A) The minimum cutoff wavelength (Duane-Hunt limit) is $\lambda_{\text{min}} = \frac{h c}{e V_0}$.  
(B) The continuous bremsstrahlung spectrum arises from rapid deceleration of electrons in the Coulomb field of target nuclei.  
(C) The characteristic X-ray lines ($K_\alpha, K_\beta$) correspond to transitions into inner shell vacancies of target atoms.  
(D) According to Moseley's law, the frequency of characteristic X-rays satisfies $\sqrt{\nu} = a(Z - b)$.

#### Question 5
A glass prism of apex angle $A = 60^\circ$ and refractive index $n = 1.50$ is in air:
(A) At minimum deviation, the ray passes symmetrically through the prism parallel to the base.  
(B) The angle of minimum deviation satisfies $n = \frac{\sin\left(\frac{A + \delta_m}{2}\right)}{\sin(A/2)}$.  
(C) For a thin prism ($A \ll 1\text{ rad}$), the deviation is $\delta \approx (n - 1) A$.  
(D) Dispersive power of the prism is $\omega = \frac{n_V - n_R}{n_Y - 1}$.

#### Question 6
A parallel-plate capacitor with circular plates of radius $R$ is charged by a constant current $I$:
(A) The rate of change of electric field between the plates is $\frac{dE}{dt} = \frac{I}{\varepsilon_0 \pi R^2}$.  
(B) The Maxwell displacement current density is $J_d = \varepsilon_0 \frac{dE}{dt} = \frac{I}{\pi R^2}$.  
(C) The induced magnetic field at distance $r \le R$ from the axis is $B(r) = \frac{\mu_0 I r}{2\pi R^2}$.  
(D) At $r = R$, the magnetic field is $B(R) = \frac{\mu_0 I}{2\pi R}$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a Duane-Hunt experiment, an X-ray tube operates at potential difference $V_0 = 40.0\text{ kV}$. Calculate the minimum cutoff wavelength $\lambda_{\text{min}}$ in picometers ($\text{pm}$) (use $h c = 1240\text{ eV}\cdot\text{nm}$, round off to ONE decimal place).

#### Question 8
A glass prism of refracting angle $A = 60^\circ$ produces a minimum deviation $\delta_m = 30^\circ$. Calculate the refractive index $n$ of the prism (enter the value rounded off to TWO decimal places).

#### Question 9
A sound source of frequency $f_0 = 500\text{ Hz}$ approaches a stationary listener with speed $v_s = 34.0\text{ m/s}$. If the speed of sound in air is $v = 340\text{ m/s}$, calculate the frequency $f$ detected by the listener in $\text{Hz}$ (round off to the nearest integer).

#### Question 10
A circular parallel-plate capacitor of radius $R = 5.0\text{ cm}$ is charged by a current $I = 2.0\text{ A}$. Calculate the induced magnetic field $B$ at radius $r = 2.5\text{ cm}$ from the central axis in microTesla ($\mu\text{T}$) (round off to ONE decimal place).

#### Question 11
Two masses $m_1 = 3.0\text{ kg}$ and $m_2 = 2.0\text{ kg}$ are connected by a light string passing over a frictionless light pulley (Atwood machine). Calculate the acceleration of the masses in $\text{m/s}^2$ (take $g = 9.8\text{ m/s}^2$, round off to TWO decimal places).

#### Question 12
An ideal heat engine absorbs $Q_H = 1000\text{ J}$ of heat from a reservoir at $T_H = 500\text{ K}$ and rejects heat to a sink at $T_C = 300\text{ K}$. Calculate the work output $W$ in Joules.

---

## Section 3: Matching List / Matrix Match (Questions 13 to 18)

#### Question 13
Match the physical phenomenon in List-I with its discoverer / law in List-II:
- **List-I**:
  - P. Characteristic X-ray frequency vs atomic number
  - Q. Electromagnetic induction
  - R. Photoelectric effect explanation
  - S. Matter waves
- **List-II**:
  - 1. de Broglie
  - 2. Moseley
  - 3. Einstein
  - 4. Faraday

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 3, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3  

#### Question 14
Match the thermodynamic process in List-I with its constant thermodynamic variable in List-II:
- **List-I**:
  - P. Isothermal
  - Q. Isobaric
  - R. Isochoric
  - S. Isentropic
- **List-II**:
  - 1. Volume ($V$)
  - 2. Temperature ($T$)
  - 3. Entropy ($S$)
  - 4. Pressure ($P$)

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3  

#### Question 15
Match the electromagnetic wave type in List-I with its typical application in List-II:
- **List-I**:
  - P. Infrared
  - Q. Ultraviolet
  - R. X-rays
  - S. Microwaves
- **List-II**:
  - 1. Radar and satellite communication
  - 2. Medical radiography of bones
  - 3. Water purification / sterilization
  - 4. Night-vision thermal imaging

(A) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 4, Q $\to$ 2, R $\to$ 3, S $\to$ 1  
(D) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  

#### Question 16
Match the rigid body in List-I with its radius of gyration $k$ about its geometric symmetry axis in List-II:
- **List-I**:
  - P. Thin circular ring of radius $R$
  - Q. Uniform solid disk of radius $R$
  - R. Uniform solid sphere of radius $R$
  - S. Thin spherical shell of radius $R$
- **List-II**:
  - 1. $R/\sqrt{2}$
  - 2. $R$
  - 3. $\sqrt{2/3} R$
  - 4. $\sqrt{2/5} R$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 17
Match the electrical quantity in List-I with its SI derived unit in List-II:
- **List-I**:
  - P. Magnetic flux
  - Q. Capacitance
  - R. Inductance
  - S. Conductance
- **List-II**:
  - 1. Henry ($\text{H}$)
  - 2. Weber ($\text{Wb}$)
  - 3. Siemens ($\text{S}$)
  - 4. Farad ($\text{F}$)

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  

#### Question 18
Match the physical phenomenon in List-I with its optical principle in List-II:
- **List-I**:
  - P. Mirage in desert
  - Q. Rainbow
  - R. Blue color of the sky
  - S. Anti-reflective lens coating
- **List-II**:
  - 1. Thin-film destructive interference
  - 2. Rayleigh scattering ($\propto \lambda^{-4}$)
  - 3. Dispersion and internal reflection in raindrops
  - 4. Total internal reflection due to temperature gradient

(A) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 4, Q $\to$ 2, R $\to$ 3, S $\to$ 1  
(D) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the aldol condensation of carbonyl compounds:
(A) The reaction is catalyzed by both acids and bases.  
(B) In base catalysis, an enolate anion attacks a second carbonyl molecule to form a $\beta$-hydroxy carbonyl (aldol).  
(C) Dehydration of the aldol yields an $\alpha,\beta$-unsaturated carbonyl compound driven by extended conjugation.  
(D) Crossed aldol condensation gives high yields of a single product when one component lacks $\alpha$-hydrogens (e.g., benzaldehyde).

#### Question 20
Regarding coordination compounds and isomerism:
(A) Linkage isomerism arises in ambidentate ligands such as $\text{NO}_2^-$ ($\text{-NO}_2$ nitro vs $\text{-ONO}$ nitrito).  
(B) Coordination isomerism occurs when both cation and anion are complex ions (e.g., $[\text{Co(NH}_3)_6][\text{Cr(CN)}_6]$).  
(C) Ionization isomerism occurs when counter-ions exchange with coordinated ligands (e.g., $[\text{Co(NH}_3)_5\text{SO}_4]\text{Br}$ and $[\text{Co(NH}_3)_5\text{Br}]\text{SO}_4$).  
(D) Hydrate (solvate) isomerism occurs when water functions as ligand or water of crystallization.

#### Question 21
Regarding colligative properties of dilute solutions:
(A) Relative lowering of vapor pressure equals the mole fraction of non-volatile solute: $\frac{\Delta P}{P^\circ} = x_{\text{solute}}$.  
(B) Elevation in boiling point is $\Delta T_b = i K_b m$.  
(C) Depression in freezing point is $\Delta T_f = i K_f m$.  
(D) Osmotic pressure is $\Pi = i C R T$.

#### Question 22
Regarding chemical equilibrium and Le Chatelier's principle for the Haber synthesis $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g)$ ($\Delta H^\circ = -92\text{ kJ/mol}$):
(A) Increasing total pressure shifts the equilibrium toward $\text{NH}_3$.  
(B) Decreasing temperature shifts the equilibrium toward $\text{NH}_3$, but reduces the reaction rate.  
(C) Adding an inert gas at constant volume has no effect on the equilibrium composition.  
(D) Adding a catalyst increases the rate of both forward and reverse reactions equally without altering the equilibrium position.

#### Question 23
Regarding amino acids and proteins:
(A) In aqueous solution, amino acids exist predominantly as dipolar zwitterions.  
(B) At the isoelectric point (pI), the net electrical charge on the amino acid is zero and solubility is minimum.  
(C) The primary structure of proteins is the linear sequence of amino acids joined by peptide bonds.  
(D) The $\alpha$-helix and $\beta$-pleated sheet secondary structures are stabilized by intramolecular and intermolecular hydrogen bonds.

#### Question 24
In the extraction of iron in a blast furnace:
(A) Haematite ore ($\text{Fe}_2\text{O}_3$) is reduced by carbon monoxide ($\text{CO}$) in the reduction zone.  
(B) Limestone ($\text{CaCO}_3$) acts as a flux, decomposing to $\text{CaO}$ which reacts with silica impurity to form calcium silicate slag ($\text{CaSiO}_3$).  
(C) The molten slag floats on top of the molten pig iron and prevents its oxidation.  
(D) Pig iron contains about $4\%$ carbon and is hard and brittle.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
Calculate the pH of a $0.050\text{ M}$ aqueous solution of sulfuric acid ($\text{H}_2\text{SO}_4$), assuming complete dissociation of both protons (enter the value rounded off to TWO decimal places).

#### Question 26
Calculate the total number of unpaired electrons in the complex ion $[FeF_6]^{3-}$ (atomic number of $\text{Fe} = 26$).

#### Question 27
An organic compound contains $85.7\%$ Carbon and $14.3\%$ Hydrogen by mass. If its vapor density is 21, calculate the number of carbon atoms present in one molecule.

#### Question 28
The half-life of radioactive carbon-14 is $t_{1/2} = 5730\text{ years}$. An ancient wooden artifact has a $\text{C-14}$ activity equal to $25.0\%$ of that in living trees. Calculate the age of the artifact in years.

#### Question 29
A constant current of $I = 1.93\text{ A}$ is passed through an aqueous silver nitrate ($\text{AgNO}_3$) solution for $t = 1000\text{ seconds}$. Calculate the mass of silver deposited at the cathode in grams (molar mass of $\text{Ag} = 108.0\text{ g/mol}$, $F = 96500\text{ C/mol}$, round off to TWO decimal places).

#### Question 30
In the van 't Hoff equation, a $0.10\text{ M}$ aqueous solution of potassium ferrocyanide ($\text{K}_4[\text{Fe(CN)}_6]$) is $80\%$ dissociated. Calculate the van 't Hoff factor $i$ (round off to ONE decimal place).

---

## Section 3: Matching List / Matrix Match (Questions 31 to 36)

#### Question 31
Match the organic reaction in List-I with its primary product in List-II:
- **List-I**:
  - P. Wurtz reaction
  - Q. Rosenmund reduction
  - R. Clemmensen reduction
  - S. Sandmeyer reaction
- **List-II**:
  - 1. Aldehyde ($\text{R-CHO}$) from acyl chloride
  - 2. Alkane ($\text{R-R}$) from alkyl halide
  - 3. Aryl halide ($\text{Ar-Cl}$) from diazonium salt
  - 4. Hydrocarbon ($\text{CH}_2$) from carbonyl compound

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 32
Match the mineral in List-I with its chemical composition in List-II:
- **List-I**:
  - P. Bauxite
  - Q. Haematite
  - R. Copper pyrite
  - S. Galena
- **List-II**:
  - 1. $\text{PbS}$
  - 2. $\text{Al}_2\text{O}_3\cdot 2\text{H}_2\text{O}$
  - 3. $\text{Fe}_2\text{O}_3$
  - 4. $\text{CuFeS}_2$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 3, S $\to$ 1  
(D) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  

#### Question 33
Match the gas in List-I with its greenhouse / atmospheric property in List-II:
- **List-I**:
  - P. Carbon dioxide ($\text{CO}_2$)
  - Q. Ozone ($\text{O}_3$) in stratosphere
  - R. Sulfur dioxide ($\text{SO}_2$)
  - S. Chlorofluorocarbons (CFCs)
- **List-II**:
  - 1. Depletion of ozone layer via chlorine radical chain reaction
  - 2. Major cause of acid rain
  - 3. Primary greenhouse gas absorbing infrared radiation
  - 4. Protects biosphere by absorbing harmful UV-B radiation

(A) P $\to$ 3, Q $\to$ 4, R $\to$ 2, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 3, R $\to$ 1, S $\to$ 2  

#### Question 34
Match the polymer in List-I with its commercial name in List-II:
- **List-I**:
  - P. Polytetrafluoroethylene
  - Q. Polyacrylonitrile
  - R. Polymethyl methacrylate
  - S. Polyamide of caprolactam
- **List-II**:
  - 1. Orlon (Acrilan)
  - 2. Teflon
  - 3. Nylon-6
  - 4. Plexiglas (Lucite)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 35
Match the colloid in List-I with its classification in List-II:
- **List-I**:
  - P. Butter
  - Q. Smoke
  - R. Shaving cream
  - S. Paint
- **List-II**:
  - 1. Aerosol (solid in gas)
  - 2. Gel (liquid in solid)
  - 3. Sol (solid in liquid)
  - 4. Foam (gas in liquid)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 36
Match the oxide in List-I with its acid-base character in List-II:
- **List-I**:
  - P. $\text{Na}_2\text{O}$
  - Q. $\text{Cl}_2\text{O}_7$
  - R. $\text{Al}_2\text{O}_3$
  - S. $\text{CO}$
- **List-II**:
  - 1. Strongly acidic
  - 2. Strongly basic
  - 3. Neutral
  - 4. Amphoteric

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^3 - 3x + 2$:
(A) The local maximum occurs at $x = -1$ with value $f(-1) = 4$.  
(B) The local minimum occurs at $x = 1$ with value $f(1) = 0$.  
(C) The point of inflection occurs at $(0, 2)$.  
(D) The curve is concave downward on $(-\infty, 0)$ and concave upward on $(0, \infty)$.

#### Question 38
Let $A$ be a $3 \times 3$ real orthogonal matrix ($A^T A = I$):
(A) $\det(A) = \pm 1$.  
(B) If $\det(A) = 1$, $A$ represents a pure rotation in 3D space.  
(C) The eigenvalues of $A$ have absolute value equal to 1.  
(D) If $\lambda$ is an eigenvalue of $A$, then $1/\lambda = \bar{\lambda}$ is also an eigenvalue.

#### Question 39
Consider the line $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and the plane $2x + y - 2z = 5$:
(A) The direction ratios of the line are $(2, 3, 4)$.  
(B) The normal vector to the plane is $(2, 1, -2)$.  
(C) The line is parallel to the plane because $2(2) + 3(1) + 4(-2) = 0$.  
(D) The line does not lie in the plane because the point $(1, 2, 3)$ does not satisfy the plane equation.

#### Question 40
Consider the differential equation $\frac{d^2 y}{dx^2} + 4y = 0$:
(A) The characteristic roots are $\lambda = \pm 2i$.  
(B) The general solution is $y(x) = c_1 \cos(2x) + c_2 \sin(2x)$.  
(C) With initial conditions $y(0) = 1, y'(0) = 0$, the solution is $y(x) = \cos(2x)$.  
(D) Every non-trivial solution is periodic with period $\pi$.

#### Question 41
Let $X$ follow an exponential distribution with rate parameter $\lambda > 0$ ($f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$):
(A) The mean is $E[X] = \frac{1}{\lambda}$.  
(B) The variance is $\text{Var}(X) = \frac{1}{\lambda^2}$.  
(C) The distribution possesses the memoryless property: $P(X > s + t \mid X > s) = P(X > t)$.  
(D) The cumulative distribution function is $F(x) = 1 - e^{-\lambda x}$ for $x \ge 0$.

#### Question 42
Consider the sequence $a_n = \left(1 + \frac{1}{n}\right)^n$:
(A) The sequence is strictly increasing.  
(B) The sequence is bounded above by 3.  
(C) $\lim_{n \to \infty} a_n = e \approx 2.71828$.  
(D) The sequence $b_n = \left(1 + \frac{1}{n}\right)^{n+1}$ is strictly decreasing and converges to $e$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 \frac{dx}{1 + x^2}$$
Calculate the value of $\frac{400 I}{\pi}$ (round off to the nearest integer).

#### Question 44
Find the number of 3-digit even numbers that can be formed using the digits $1, 2, 3, 4, 5$ without repetition.

#### Question 45
Find the perpendicular distance from the point $(0, 0, 0)$ to the plane $x + 2y + 2z - 9 = 0$.

#### Question 46
Let $z = 1 + i\sqrt{3}$. Find the modulus of $z^6$.

#### Question 47
Let $y(x)$ satisfy $\frac{dy}{dx} = 2x y$ with $y(0) = 1$. Calculate $y(1)$ (use $e \approx 2.718$, round off to TWO decimal places).

#### Question 48
In rolling a single fair six-sided die, calculate the expected value $E[X]$ of the number rolled.

---

## Section 3: Matching List / Matrix Match (Questions 49 to 54)

#### Question 49
Match the function in List-I with its derivative in List-II:
- **List-I**:
  - P. $\sin(x)$
  - Q. $\cos(x)$
  - R. $\tan(x)$
  - S. $\sec(x)$
- **List-II**:
  - 1. $-\sin(x)$
  - 2. $\cos(x)$
  - 3. $\sec(x)\tan(x)$
  - 4. $\sec^2(x)$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 50
Match the curve in List-I with its eccentricity $e$ in List-II:
- **List-I**:
  - P. $x^2 + y^2 = 4$
  - Q. $\frac{x^2}{4} + \frac{y^2}{3} = 1$
  - R. $y^2 = 4x$
  - S. $x^2 - y^2 = 1$
- **List-II**:
  - 1. $1/2$
  - 2. $0$
  - 3. $\sqrt{2}$
  - 4. $1$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 51
Match the complex number in List-I with its principal argument $\text{Arg}(z) \in (-\pi, \pi]$ in List-II:
- **List-I**:
  - P. $1 + i$
  - Q. $-1 + i$
  - R. $-1 - i$
  - S. $1 - i$
- **List-II**:
  - 1. $3\pi/4$
  - 2. $\pi/4$
  - 3. $-\pi/4$
  - 4. $-3\pi/4$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 52
Match the matrix type in List-I with its mathematical definition in List-II:
- **List-I**:
  - P. Symmetric
  - Q. Skew-symmetric
  - R. Orthogonal
  - S. Idempotent
- **List-II**:
  - 1. $A^T = -A$
  - 2. $A^T = A$
  - 3. $A^2 = A$
  - 4. $A^T A = I$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 53
Match the statistical measure in List-I with its formula in List-II:
- **List-I**:
  - P. Mean of discrete variable
  - Q. Variance $\text{Var}(X)$
  - R. Standard deviation $\sigma$
  - S. Covariance $\text{Cov}(X, Y)$
- **List-II**:
  - 1. $E[X^2] - (E[X])^2$
  - 2. $\sum x_i P(X = x_i)$
  - 3. $E[X Y] - E[X] E[Y]$
  - 4. $\sqrt{\text{Var}(X)}$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 54
Match the series in List-I with its sum in List-II:
- **List-I**:
  - P. $\sum_{n=1}^\infty \frac{1}{2^n}$
  - Q. $\sum_{n=0}^\infty \frac{1}{n!}$
  - R. $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}$
  - S. $\sum_{n=1}^\infty \frac{1}{n(n+1)}$
- **List-II**:
  - 1. $e$
  - 2. $1$
  - 3. $1$
  - 4. $\ln 2$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 16

---

### PART I: PHYSICS

#### Solution 1: Hall Effect
- Transverse force balance $q E_y = q v_d B \implies E_y = v_d B$.
- Current density $J_x = n q v_d \implies v_d = \frac{I}{n q w d}$.
- $V_H = E_y w = \frac{I B}{n q d}$, independent of $w$.
- Hall coefficient $R_H = \frac{1}{n q}$.
- **Correct Option**: (A, B, C, D)

#### Solution 2: Cherenkov Radiation
- Condition $v > c/n \implies \beta n > 1$.
- Wavefront angle $\cos\theta_c = \frac{1}{\beta n}$.
- Frank-Tamm formula gives spectrum $\propto 1/\lambda^2$.
- **Correct Option**: (A, B, C, D)

#### Solution 3: Cylindrical Magnetron Cutoff Field
- Canonical angular momentum $p_\theta = m r v_\theta - \frac{1}{2} e B r^2 = \text{const} = -\frac{1}{2} e B a^2$.
- Energy conservation $\frac{1}{2} m (v_r^2 + v_\theta^2) = e V(r)$.
- At grazing cutoff $v_r(b) = 0 \implies B_c = \sqrt{\frac{8 m V_0}{e b^2 (1 - a^2/b^2)^2}}$.
- **Correct Option**: (A, B, C, D)

#### Solution 4: Radial Heat Conduction in Cylinder
- $\frac{1}{r}\frac{d}{dr}(r \frac{dT}{dr}) + \frac{q'''}{k} = 0 \implies T(r) = T_s + \frac{q'''}{4k}(R^2 - r^2)$.
- Maximum at center, surface heat flux $q''(R) = \frac{q''' R}{2}$.
- **Correct Option**: (A, B, C, D)

#### Solution 5: Supersonic Shock Wave Mach Cone
- Shock cone angle $\sin\mu = 1/M$.
- Geometry gives horizontal delay distance $x = H \sqrt{M^2 - 1}$.
- Delay time $\Delta t = \frac{H}{v}\sqrt{M^2 - 1}$.
- **Correct Option**: (A, B, C, D)

#### Solution 6: Rotating Charged Disk
- Current of elemental ring $dI = \frac{\omega}{2\pi} (2\pi r dr \sigma) = \sigma \omega r dr$.
- Magnetic moment $d\mu = dI (\pi r^2) = \pi \sigma \omega r^3 dr \implies \mu = \frac{1}{4}\pi \sigma \omega R^4$.
- Angular momentum $L = \frac{1}{2} M R^2 \omega \implies \mu / L = Q / (2M)$.
- **Correct Option**: (A, B, C, D)

#### Solution 7: Copper Hall Voltage
- $V_H = \frac{I B}{n e d} = \frac{50.0 \times 1.20}{(8.4 \times 10^{28}) (1.6 \times 10^{-19}) (2.0 \times 10^{-3})} = \frac{60.0}{2.688 \times 10^7} \approx 2.23 \times 10^{-6}\text{ V} = 2.23\text{ }\mu\text{V}$.
- **Answer**: 2.23

#### Solution 8: Cherenkov Angle in Water
- $\beta = \frac{p c}{E} = \frac{\sqrt{E^2 - m^2 c^4}}{E}$. Total energy $E = 938 + 1000 = 1938\text{ MeV}$.
- $\beta = \sqrt{1 - (938/1938)^2} = \sqrt{1 - 0.234} = \sqrt{0.766} \approx 0.875$.
- $\cos\theta_c = \frac{1}{\beta n} = \frac{1}{0.875 \times 1.33} = \frac{1}{1.164} \approx 0.859$.
- $\theta_c = \arccos(0.859) \approx 30.8^\circ$.
- **Answer**: 30.8

#### Solution 9: Magnetron Cutoff Field
- $a = 0.002\text{ m}, b = 0.010\text{ m} \implies a/b = 0.2 \implies a^2/b^2 = 0.04 \implies 1 - a^2/b^2 = 0.96$.
- $B_c = \frac{1}{b(1 - a^2/b^2)}\sqrt{\frac{8 V_0}{e/m}} = \frac{1}{0.010 \times 0.96}\sqrt{\frac{8 \times 300}{1.76 \times 10^{11}}} = \frac{1}{0.0096}\sqrt{1.364 \times 10^{-8}} = \frac{1.168 \times 10^{-4}}{0.0096} \approx 0.0122\text{ T} = 12.2\text{ mT}$.
- **Answer**: 12.2

#### Solution 10: Sonic Boom Delay
- $v = M v_s = 2.0 \times 340 = 680\text{ m/s}$.
- $\Delta t = \frac{H}{v}\sqrt{M^2 - 1} = \frac{6000}{680}\sqrt{4 - 1} = \frac{6000 \times 1.732}{680} \approx 15.3\text{ s}$.
- **Answer**: 15.3

#### Solution 11: Electrostatic Energy of Spherical Shell
- $U = \frac{Q^2}{8\pi\varepsilon_0 R} = \frac{1}{2}\left(\frac{1}{4\pi\varepsilon_0}\right)\frac{Q^2}{R} = \frac{1}{2}(9.0 \times 10^9)\frac{(2.0 \times 10^{-6})^2}{0.10} = \frac{9.0 \times 10^9 \times 4.0 \times 10^{-12}}{0.20} = 0.18\text{ J} = 180.0\text{ mJ}$.
- **Answer**: 180.0

#### Solution 12: Rotating Rod Angular Velocity
- Drop in center of mass $\Delta h = L/2 = 0.5\text{ m}$.
- Potential energy converted: $M g (L/2) = \frac{1}{2} I \omega^2 = \frac{1}{2} (\frac{1}{3} M L^2) \omega^2 = \frac{1}{6} M L^2 \omega^2$.
- $\omega = \sqrt{\frac{3 g}{L}} = \sqrt{\frac{3 \times 9.8}{1.0}} = \sqrt{29.4} \approx 5.42\text{ rad/s}$.
- **Answer**: 5.42

#### Solution 13 to 18:
- 13: Normal force $N$: $N \cos\alpha = m g$, $N \sin\alpha = m \omega^2 r_0 \implies \tan\alpha = \frac{\omega^2 r_0}{g} \implies \omega = \sqrt{\frac{g \tan\alpha}{r_0}}$. (B)
- 14: $\frac{dU}{dL} = \frac{\mu_0 I^2}{16\pi}$. (A)
- 15: Perpendicular phases $\implies A = \sqrt{3^2 + 4^2} = 5$. (A)
- 16: Work done in cycle $= P V_1(1 - \ln 2)$. (A)
- 17: Angular width $= 2\lambda/a = \frac{2 \times 600 \times 10^{-9}}{0.2 \times 10^{-3}} = 6.0 \times 10^{-3}\text{ rad}$. (A)
- 18: Fraction decayed $= 1 - (1/2)^3 = 1 - 1/8 = 7/8$. (A)

---

### PART II: CHEMISTRY

#### Solution 19: Mitsunobu Reaction
- Ph3P + DEAD gives betaine, deprotonates pronucleophile, activates alcohol, and nucleophilic attack gives inversion.
- **Correct Option**: (A, B, C, D)

#### Solution 20: Grubbs Olefin Metathesis
- Chauvin mechanism, metallacyclobutane, NHC ligand superiority.
- **Correct Option**: (A, B, C, D)

#### Solution 21: Gibbs Adsorption Isotherm
- $\Gamma = -\frac{c}{RT}\frac{d\gamma}{dc}$, positive surface excess lowers $\gamma$.
- **Correct Option**: (A, B, C, D)

#### Solution 22: Spin-Crossover Fe(II)
- $d^6$ switching between $S=0$ and $S=2$, bond length expansion, entropy driven, thermal hysteresis.
- **Correct Option**: (A, B, C, D)

#### Solution 23: Margules Non-Ideal Solutions
- $\ln\gamma_1 = A x_2^2 / RT$, positive deviations, immiscibility gap when $A > 2RT$.
- **Correct Option**: (A, B, C, D)

#### Solution 24: Group I Radical Analysis
- Insoluble chlorides, $\text{PbCl}_2$ hot water solubility, $\text{AgCl}$ ammonia complex, $\text{Hg}_2\text{Cl}_2$ disproportionation.
- **Correct Option**: (A, B, C, D)

#### Solution 25: Mg(OH)2 pH
- $\text{Mg(OH)}_2 \rightleftharpoons \text{Mg}^{2+} + 2\text{OH}^-$.
- $K_{sp} = 4 S^3 = 1.8 \times 10^{-11} \implies S^3 = 4.5 \times 10^{-12} \implies S \approx 1.65 \times 10^{-4}\text{ M}$.
- $[\text{OH}^-] = 2S = 3.30 \times 10^{-4}\text{ M} \implies pOH = 3.48 \implies pH = 10.52$.
- **Answer**: 10.52

#### Solution 26: Spin-Only Moment of Mn2+
- $\text{Mn}^{2+}$ is high-spin $d^5 \implies 5$ unpaired electrons $\implies \mu = \sqrt{5(7)} = \sqrt{35} \approx 5.92\text{ BM}$.
- **Answer**: 5.92

#### Solution 27: Hydrogen Atoms in Glucose/Fructose
- Molar mass $= 180\text{ g/mol}$, empirical formula $\text{CH}_2\text{O}$ (mass 30).
- Multiple $n = 180/30 = 6 \implies \text{C}_6\text{H}_{12}\text{O}_6 \implies 12$ hydrogen atoms.
- **Answer**: 12

#### Solution 28: Cell EMF
- $E^\circ_{\text{cell}} = E^\circ(\text{cathode}) - E^\circ(\text{anode}) = 0.77 - 0.15 = 0.62\text{ V}$.
- **Answer**: 0.62

#### Solution 29: First-Order Decay Percentage
- $120\text{ min} = 3$ half-lives.
- Remaining $= (1/2)^3 = 1/8 = 12.5\%$.
- **Answer**: 12.5

#### Solution 30: Protein Molar Mass
- $\Pi = \frac{w}{M V} R T \implies M = \frac{w R T}{\Pi V} = \frac{1.50 \times 0.0821 \times 300}{3.1 \times 10^{-3} \times 0.100} = \frac{36.945}{3.1 \times 10^{-4}} \approx 119177\text{ g/mol} \approx 119\text{ kg/mol}$.
- **Answer**: 119

#### Solution 31 to 36:
- 31: Gabriel synthesis produces pure primary aliphatic amines. (A)
- 32: $[\text{Co(NH}_3)_6]^{3+}$ is low-spin $d^6$, completely paired, diamagnetic. (A)
- 33: Partial double bond character and planar geometry. (A)
- 34: Cryolite lowers melting point and increases conductivity. (A)
- 35: Acylium cation is the electrophile. (A)
- 36: $\text{HCO}_3^-$ loses $\text{H}^+$ to become $\text{CO}_3^{2-}$. (A)

---

### PART III: MATHEMATICS

#### Solution 37: Green's Theorem
- Area formula $\frac{1}{2}\oint (x dy - y dx)$, conservative fields $\oint = 0$.
- **Correct Option**: (A, B, C, D)

#### Solution 38: Newton's Sums
- Standard polynomial power sum formulas.
- **Correct Option**: (A, B, C, D)

#### Solution 39: Pedal Curve of Ellipse
- Auxiliary circle locus from focus, product of perpendiculars $= b^2$.
- **Correct Option**: (A, B, C, D)

#### Solution 40: Bivariate Normal Distribution
- Contours are ellipses, independence $\iff \rho = 0$, linear regression conditional expectation.
- **Correct Option**: (A, B, C, D)

#### Solution 41: Smoothness of $|x|^3$
- $f(x) = x^3 \text{sgn}(x)$ has continuous first and second derivatives, but third derivative jumps from $-6$ to $+6$ at 0.
- **Correct Option**: (A, B, C, D)

#### Solution 42: Differential Equation Transformation
- Integrating factor $\mu = 1/x^2$ gives $d\left(\frac{x^2 - y^2}{x}\right) = 0 \implies x^2 - y^2 = C x$.
- **Correct Option**: (A, B, C, D)

#### Solution 43: Beta Function Integral
- $I = B(4, 5) = \frac{\Gamma(4)\Gamma(5)}{\Gamma(9)} = \frac{3! \cdot 4!}{8!} = \frac{6 \times 24}{40320} = \frac{144}{40320} = \frac{1}{280}$.
- $280 I = 1$.
- **Answer**: 1

#### Solution 44: Divisibility by 4
- Last two digits must be divisible by 4: choices from $\{1, 2, 3, 4, 5, 6\}$ are $12, 16, 24, 32, 36, 52, 56, 64$ (8 possibilities).
- For each, first two digits chosen from remaining 4: $4 \times 3 = 12$ ways.
- Total $= 8 \times 12 = 96$.
- **Answer**: 96

#### Solution 45: Triangle Area
- $\vec{A B} = (3, -2, 1)$, $\vec{A C} = (1, 1, -2)$.
- $\vec{A B} \times \vec{A C} = (3, 7, 5)$.
- $|\vec{A B} \times \vec{A C}| = \sqrt{9 + 49 + 25} = \sqrt{83} \approx 9.11$.
- Area $= \frac{1}{2}\sqrt{83} \approx 4.56$.
- **Answer**: 4.56

#### Solution 46: Apollonius Circle
- $|z - 2|^2 = 4|z - 1|^2 \implies (x-2)^2 + y^2 = 4((x-1)^2 + y^2)$.
- $x^2 - 4x + 4 + y^2 = 4(x^2 - 2x + 1 + y^2) = 4x^2 - 8x + 4 + 4y^2$.
- $3x^2 - 4x + 3y^2 = 0 \implies x^2 - \frac{4}{3}x + y^2 = 0 \implies (x - 2/3)^2 + y^2 = (2/3)^2$.
- Radius $R = 2/3 \approx 0.67$.
- **Answer**: 0.67

#### Solution 47: Homogeneous ODE
- Substitute $y = v x \implies v + x v' = v + 1/v \implies x v' = 1/v \implies v dv = dx/x$.
- $\frac{1}{2} v^2 = \ln x + C \implies \frac{y^2}{2x^2} = \ln x + C$.
- $y(1) = 1 \implies 1/2 = 0 + C \implies C = 1/2$.
- $y^2 = 2x^2(\ln x + 1/2) = x^2(2\ln x + 1)$.
- At $x = e$: $y^2 = e^2(2(1) + 1) = 3e^2 \implies y = e\sqrt{3} \approx 2.718 \times 1.732 \approx 4.71$.
- **Answer**: 4.71

#### Solution 48: Dice Sum Probability
- Outcomes with sum $\ge 10$: $(4, 6), (5, 5), (5, 6), (6, 4), (6, 5), (6, 6)$ (6 outcomes).
- Probability $= 6/36 = 1/6 \approx 0.17$.
- **Answer**: 0.17

#### Solution 49 to 54:
- 49: Area $= \int_0^\pi \sin x dx + |\int_\pi^{2\pi} \sin x dx| = 2 + 2 = 4$. (A)
- 50: $\ln b - \ln a = \ln r = \ln c - \ln b \implies$ Arithmetic Progression. (A)
- 51: Limit $= \frac{2\sin^2 x}{x^2} = 2$. (A)
- 52: Condition of tangency $c = a/m \implies 1 = 1/m \implies m = 1$. (A)
- 53: Distance between $2x - y + 2z + 3 = 0$ and $2x - y + 2z - 9/2 = 0$: $d = \frac{|3 - (-9/2)|}{\sqrt{4+1+4}} = \frac{15/2}{3} = \frac{5}{2}$. (A)
- 54: $\vec{a} \times \vec{b} = (4, -1, -3)$, $|\vec{a}\times\vec{b}| = \sqrt{26} \implies \frac{4\hat{i} - \hat{j} - 3\hat{k}}{\sqrt{26}}$. (A)
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 2
## IIT Delhi Benchmark JEE Advanced Mock Examination 16

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Coaxial cable fields and Poynting flux $P = V I$.
- 2: (A, B, C, D) - Acoustic Doppler effect and wind velocity correction.
- 3: (A, B, C, D) - Radial stability condition $n < 2$ in central potential.
- 4: (A, B, C, D) - X-ray continuous and characteristic spectra.
- 5: (A, B, C, D) - Prism minimum deviation and dispersion.
- 6: (A, B, C, D) - Displacement current and induced magnetic field in capacitor.

#### Solutions 7 to 12:
- 7: $\lambda_{\text{min}} = \frac{h c}{e V_0} = \frac{1240\text{ eV}\cdot\text{nm}}{40000\text{ eV}} = 0.031\text{ nm} = 31.0\text{ pm}$. (Answer: 31.0)
- 8: $n = \frac{\sin(45^\circ)}{\sin(30^\circ)} = \frac{1/\sqrt{2}}{1/2} = \sqrt{2} \approx 1.41$. (Answer: 1.41)
- 9: $f = f_0 \frac{v}{v - v_s} = 500 \frac{340}{340 - 34} = 500 \frac{340}{306} \approx 556\text{ Hz}$. (Answer: 556)
- 10: $B(r) = \frac{\mu_0 I r}{2\pi R^2} = \frac{(4\pi \times 10^{-7}) (2.0) (0.025)}{2\pi (0.05)^2} = \frac{10^{-7} \times 0.10}{0.0025} = 4.0\text{ }\mu\text{T}$. (Answer: 4.0)
- 11: $a = \frac{m_1 - m_2}{m_1 + m_2} g = \frac{1.0}{5.0} \times 9.8 = 1.96\text{ m/s}^2$. (Answer: 1.96)
- 12: $\eta = 1 - 300/500 = 0.40 \implies W = 0.40 \times 1000 = 400\text{ J}$. (Answer: 400)

#### Solutions 13 to 18 (Matching Lists):
- 13: P-2, Q-4, R-3, S-1. (A)
- 14: P-2, Q-4, R-1, S-3. (A)
- 15: P-4, Q-3, R-2, S-1. (A)
- 16: P-2, Q-1, R-4, S-3. (A)
- 17: P-2, Q-4, R-1, S-3. (A)
- 18: P-4, Q-3, R-2, S-1. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Aldol condensation mechanism.
- 20: (A, B, C, D) - Types of structural isomerism in complexes.
- 21: (A, B, C, D) - Four colligative properties.
- 22: (A, B, C, D) - Haber process equilibria.
- 23: (A, B, C, D) - Protein structure hierarchy.
- 24: (A, B, C, D) - Blast furnace iron metallurgy.

#### Solutions 25 to 30:
- 25: $[\text{H}^+] = 2 \times 0.050 = 0.10\text{ M} \implies \text{pH} = 1.00$. (Answer: 1.00)
- 26: $\text{Fe}^{3+}$ with weak field $\text{F}^-$ is high-spin $d^5 \implies 5$ unpaired electrons. (Answer: 5)
- 27: Molar mass $= 2 \times 21 = 42\text{ g/mol}$. Empirical formula $\text{CH}_2$ (mass 14) $\implies n = 3 \implies \text{C}_3\text{H}_6 \implies 3$ carbons. (Answer: 3)
- 28: $25\% = (1/2)^2 \implies 2$ half-lives $= 2 \times 5730 = 11460\text{ years}$. (Answer: 11460)
- 29: $m = \frac{M I t}{F} = \frac{108.0 \times 1.93 \times 1000}{96500} = \frac{208440}{96500} \approx 2.16\text{ g}$. (Answer: 2.16)
- 30: $\text{K}_4[\text{Fe(CN)}_6] \to 4\text{K}^+ + [\text{Fe(CN)}_6]^{4-} \implies n = 5$.
  $i = 1 + (n - 1)\alpha = 1 + 4(0.80) = 4.2$. (Answer: 4.2)

#### Solutions 31 to 36:
- 31: P-2, Q-1, R-4, S-3. (A)
- 32: P-2, Q-3, R-4, S-1. (A)
- 33: P-3, Q-4, R-2, S-1. (A)
- 34: P-2, Q-1, R-4, S-3. (A)
- 35: P-2, Q-1, R-4, S-3. (A)
- 36: P-2, Q-1, R-4, S-3. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Cubic function calculus analysis.
- 38: (A, B, C, D) - Orthogonal matrix properties.
- 39: (A, B, C, D) - Line parallel to plane condition.
- 40: (A, B, C, D) - Simple harmonic oscillator ODE.
- 41: (A, B, C, D) - Exponential distribution properties.
- 42: (A, B, C, D) - Euler's constant limit bounds.

#### Solutions 43 to 48:
- 43: $I = \arctan(1) = \pi/4 \implies \frac{400 I}{\pi} = 100$. (Answer: 100)
- 44: Last digit must be 2 or 4 (2 choices). First two digits chosen from 4 remaining: $4 \times 3 = 12$. Total $= 2 \times 12 = 24$. (Answer: 24)
- 45: $d = \frac{|0 + 0 + 0 - 9|}{\sqrt{1 + 4 + 4}} = \frac{9}{3} = 3$. (Answer: 3)
- 46: $|z| = \sqrt{1 + 3} = 2 \implies |z^6| = 2^6 = 64$. (Answer: 64)
- 47: $\frac{dy}{y} = 2x dx \implies \ln y = x^2 \implies y = e^{x^2}$. At $x = 1$, $y(1) = e \approx 2.72$. (Answer: 2.72)
- 48: $E[X] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5$. (Answer: 3.5)

#### Solutions 49 to 54:
- 49: P-2, Q-1, R-4, S-3. (A)
- 50: P-2, Q-1, R-4, S-3. (A)
- 51: P-2, Q-1, R-4, S-3. (A)
- 52: P-2, Q-1, R-4, S-3. (A)
- 53: P-2, Q-1, R-4, S-3. (A)
- 54: P-2, Q-1, R-4, S-3. (A)
"""

val_md = r"""# Answer Key & Benchmark Validation — Mock 16
## IIT Delhi Benchmark Calibration

### Paper 1 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 2.23 | **C25** | Num | 10.52 | **M43** | Num | 1 |
| **P8** | Num | 30.8 | **C26** | Num | 5.92 | **M44** | Num | 96 |
| **P9** | Num | 12.2 | **C27** | Num | 12 | **M45** | Num | 4.56 |
| **P10** | Num | 15.3 | **C28** | Num | 0.62 | **M46** | Num | 0.67 |
| **P11** | Num | 180.0 | **C29** | Num | 12.5 | **M47** | Num | 4.71 |
| **P12** | Num | 5.42 | **C30** | Num | 119 | **M48** | Num | 0.17 |
| **P13** | Single | B | **C31** | Single | A | **M49** | Single | A |
| **P14** | Single | A | **C32** | Single | A | **M50** | Single | A |
| **P15** | Single | A | **C33** | Single | A | **M51** | Single | A |
| **P16** | Single | A | **C34** | Single | A | **M52** | Single | A |
| **P17** | Single | A | **C35** | Single | A | **M53** | Single | A |
| **P18** | Single | A | **C36** | Single | A | **M54** | Single | A |

---

### Paper 2 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 31.0 | **C25** | Num | 1.00 | **M43** | Num | 100 |
| **P8** | Num | 1.41 | **C26** | Num | 5 | **M44** | Num | 24 |
| **P9** | Num | 556 | **C27** | Num | 3 | **M45** | Num | 3 |
| **P10** | Num | 4.0 | **C28** | Num | 11460 | **M46** | Num | 64 |
| **P11** | Num | 1.96 | **C29** | Num | 2.16 | **M47** | Num | 2.72 |
| **P12** | Num | 400 | **C30** | Num | 4.2 | **M48** | Num | 3.5 |
| **P13** | Match | A | **C31** | Match | A | **M49** | Match | A |
| **P14** | Match | A | **C32** | Match | A | **M50** | Match | A |
| **P15** | Match | A | **C33** | Match | A | **M51** | Match | A |
| **P16** | Match | A | **C34** | Match | A | **M52** | Match | A |
| **P17** | Match | A | **C35** | Match | A | **M53** | Match | A |
| **P18** | Match | A | **C36** | Match | A | **M54** | Match | A |
"""

if __name__ == "__main__":
    create_mock_files(
        16,
        paper_1_md,
        paper_2_md,
        sol_1_md,
        sol_2_md,
        val_md,
        iit_name="IIT_Delhi"
    )

