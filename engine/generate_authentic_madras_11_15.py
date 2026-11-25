"""
IIT Madras Mocks 11 to 15 Generator
Organising Institute: Indian Institute of Technology Madras
Empirical Benchmark: 2010, 2017, 2024 Official JEE Advanced Papers
Features:
- Electromagnetism dominance (>= 37% of physics: Betatron condition, wave velocity in transmission line, Poynting vector flux, eddy currents)
- Single-correct traps and speed/precision tests
- Physical chemistry dominance: Debye-Huckel, chemical kinetics (consecutive/parallel), Gibbs-Duhem, electrochemistry
- Mathematics: Conics invariants, Leibniz integral rule, vector triple product Jacobi identity, circulant determinants
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_madras_11_to_15():
    for mock_idx in range(11, 16):
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
In a betatron accelerator, an electron beam of radius $R_0$ is accelerated in an axially symmetric time-varying magnetic field $B(r, t)$:
(A) The condition for stable circular orbit of constant radius $R_0$ (the Betatron condition) is that the average magnetic field inside the orbit $\langle B \rangle$ must be twice the magnetic field at the orbit $B(R_0)$, i.e., $\langle B \rangle = 2 B(R_0)$.  
(B) The tangential accelerating electric field at radius $R_0$ is given by $E_\theta = \frac{R_0}{2}\frac{d\langle B \rangle}{dt}$.  
(C) The momentum gained by the electron satisfies $\frac{dp}{dt} = e E_\theta$.  
(D) If $\langle B \rangle = B(R_0)$, the orbital radius of the electron would decrease with time.

#### Question 2
A long cylindrical resistor of radius $a$, length $L$, and conductivity $\sigma$ carries a steady current $I$ uniformly distributed across its cross-section:
(A) The electric field inside the resistor is uniform and directed along the axis: $\vec{E} = \frac{I}{\sigma \pi a^2}\hat{k}$.  
(B) The magnetic field at the outer surface $r = a$ is $\vec{B} = \frac{\mu_0 I}{2\pi a}\hat{\phi}$.  
(C) The Poynting vector $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$ at $r = a$ is directed radially inward into the resistor.  
(D) The total flux of the Poynting vector integrated over the cylindrical surface equals the Joule heating rate $I^2 R$.

#### Question 3
A loss-free parallel-plate transmission line has plates of width $w$ separated by distance $d \ll w$ with vacuum between them:
(A) The capacitance per unit length is $\mathcal{C} = \frac{\varepsilon_0 w}{d}$.  
(B) The inductance per unit length is $\mathcal{L} = \frac{\mu_0 d}{w}$.  
(C) The propagation velocity of transverse electromagnetic (TEM) waves along the line is $v = \frac{1}{\sqrt{\mathcal{L}\mathcal{C}}} = c$.  
(D) The characteristic wave impedance of the transmission line is $Z_0 = \sqrt{\frac{\mathcal{L}}{\mathcal{C}}} = \frac{d}{w}\sqrt{\frac{\mu_0}{\varepsilon_0}}$.

#### Question 4
A thin uniform metallic disc of radius $R$, mass $M$, and electrical conductivity $\sigma$ spins with initial angular velocity $\omega_0$ in a uniform magnetic field $B_0\hat{k}$ applied perpendicular to the disc:
(A) Radial non-conservative electric fields are induced by the rotation: $\vec{E} = (\vec{\omega} \times \vec{r}) \times \vec{B}$.  
(B) If the magnetic field covers only a localized sector of the disc, circulating eddy currents are generated.  
(C) The eddy currents exert a retarding Lorentz torque proportional to the instantaneous angular speed $\omega$.  
(D) The angular speed of the disc decays exponentially with time when localized eddy current braking is active.

#### Question 5
In a quarter-wave plate ($\lambda/4$ plate) made of an anisotropic uniaxial crystal with refractive indices $n_e$ and $n_o$:
(A) The minimum thickness required is $t = \frac{\lambda}{4|n_e - n_o|}$.  
(B) When linearly polarized light is incident with its polarization direction at $45^\circ$ to the optic axis, the transmitted light is circularly polarized.  
(C) When linearly polarized light is incident parallel to the optic axis, its polarization state is completely unchanged.  
(D) A half-wave plate introduces a phase difference of $\pi$ radians between ordinary and extraordinary rays.

#### Question 6
For a real gas obeying the van der Waals equation of state $\left(P + \frac{a}{V_m^2}\right)(V_m - b) = RT$:
(A) The critical temperature is $T_c = \frac{8a}{27Rb}$.  
(B) The critical pressure is $P_c = \frac{a}{27b^2}$.  
(C) The critical molar volume is $V_c = 3b$.  
(D) The critical compressibility factor is $Z_c = \frac{P_c V_c}{R T_c} = \frac{3}{8} = 0.375$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A parallel-plate capacitor with plate area $A = 0.04\text{ m}^2$ and separation $d = 1.0\text{ mm}$ is being charged such that the electric field between plates increases at $\frac{dE}{dt} = 1.0 \times 10^{12}\text{ V/(m s)}$. The displacement current $I_d$ in amperes is $I_d$. Taking $\varepsilon_0 = 8.85 \times 10^{-12}\text{ F/m}$, evaluate $I_d$ rounded off to two decimal places.

#### Question 8
A toroidal coil has mean radius $R = 0.20\text{ m}$ and cross-sectional area $A = 1.0 \times 10^{-3}\text{ m}^2$. It is closely wound with $N = 1000\text{ turns}$. If the coil carries a current of $2.0\text{ A}$, the energy stored in its magnetic field is $U\text{ mJ}$. Taking $\mu_0 = 4\pi \times 10^{-7}\text{ T m/A}$, find $U$ rounded off to two decimal places.

#### Question 9
In a Lloyd's mirror experiment with $\lambda = 600\text{ nm}$, the distance between the source and screen is $D = 1.20\text{ m}$ and source height above the mirror is $h = 1.50\text{ mm}$. The fringe width $\beta$ in millimeters is $\beta\text{ mm}$. Find $\beta$ rounded off to two decimal places.

#### Question 10
A heat engine operates between temperatures $T_H = 600\text{ K}$ and $T_C = 300\text{ K}$. If the actual efficiency is $75\%$ of the maximum possible Carnot efficiency, and the engine absorbs $4000\text{ J}$ of heat per cycle, the work produced per cycle is $W\text{ J}$. Find $W$.

#### Question 11
Two coupled inductors have $L_1 = 0.18\text{ H}$, $L_2 = 0.32\text{ H}$, and coupling coefficient $k = 0.50$. The mutual inductance $M$ in henrys is $M\text{ H}$. Find $M$ rounded off to two decimal places.

#### Question 12
A uniform rod of length $L = 1.0\text{ m}$ rotates in a horizontal plane about a vertical axis passing through one of its ends with constant angular velocity $\omega = 20\text{ rad/s}$ in a uniform vertical magnetic field $B = 0.50\text{ T}$. The potential difference developed between the ends of the rod is $V\text{ V}$. Find $V$.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The magnetic energy density $u_m$ in a region of space with magnetic field $B$ is:
(A) $\frac{B^2}{2\mu_0}$  
(B) $\frac{\mu_0 B^2}{2}$  
(C) $\frac{B}{2\mu_0}$  
(D) $\frac{B^2}{\mu_0}$

#### Question 14
A copper ring is suspended horizontally by a light thread. A bar magnet is dropped vertically along the axis of the ring with its north pole pointing downward. The acceleration of the falling magnet is:
(A) Always equal to $g$  
(B) Less than $g$ while approaching and less than $g$ while receding  
(C) Greater than $g$ while approaching and less than $g$ while receding  
(D) Less than $g$ while approaching and greater than $g$ while receding

#### Question 15
The quality factor $Q$ of a series $RLC$ circuit is given by:
(A) $\frac{1}{R}\sqrt{\frac{L}{C}}$  
(B) $R\sqrt{\frac{C}{L}}$  
(C) $\frac{1}{R}\sqrt{\frac{C}{L}}$  
(D) $\sqrt{\frac{L}{RC}}$

#### Question 16
The ratio of the speed of an electron in the first Bohr orbit of a hydrogen atom to the speed of light in vacuum is approximately:
(A) $1/137$  
(B) $1/274$  
(C) $1/68$  
(D) $1/1836$

#### Question 17
A slit of width $a$ is illuminated by white light. The first diffraction minimum for red light ($\lambda = 650\text{ nm}$) coincides with the first diffraction maximum for another wavelength $\lambda'$. The value of $\lambda'$ is approximately:
(A) $433\text{ nm}$  
(B) $520\text{ nm}$  
(C) $325\text{ nm}$  
(D) $866\text{ nm}$

#### Question 18
For an ideal monoatomic gas, the ratio of molar heat capacity at constant pressure to that at constant volume is:
(A) $5/3$  
(B) $7/5$  
(C) $4/3$  
(D) $9/7$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Jahn-Teller effect in transition metal complexes:
(A) Any non-linear molecule in an orbitally degenerate electronic state undergoes geometric distortion to remove degeneracy and lower energy.  
(B) High-spin $d^4$ ($\text{Cr}^{2+}, \text{Mn}^{3+}$) and $d^9$ ($\text{Cu}^{2+}$) octahedral complexes show strong Jahn-Teller distortions.  
(C) In an octahedral complex showing tetragonal elongation (z-out), the two axial bonds are significantly longer than the four equatorial bonds.  
(D) Low-spin $d^6$ octahedral complexes (e.g., $[\text{Co}(\text{NH}_3)_6]^{3+}$) do not show Jahn-Teller distortion because the $t_{2g}^6$ ground state is orbitally non-degenerate.

#### Question 20
Regarding the thermodynamics and kinetics of consecutive first-order reactions $A \xrightarrow{k_1} B \xrightarrow{k_2} C$ ($[B]_0 = [C]_0 = 0$):
(A) $[A](t) = [A]_0 e^{-k_1 t}$.  
(B) $[B](t) = \frac{k_1 [A]_0}{k_2 - k_1}(e^{-k_1 t} - e^{-k_2 t})$ (for $k_1 \ne k_2$).  
(C) The concentration of intermediate $B$ reaches its maximum at time $t_{\max} = \frac{\ln(k_1/k_2)}{k_1 - k_2}$.  
(D) If $k_2 \gg k_1$, the steady-state approximation $d[B]/dt \approx 0$ is valid for most of the reaction duration.

#### Question 21
Regarding the trans-effect in square planar platinum(II) complexes:
(A) The trans-effect is the labilization of ligands trans to a specific directing ligand.  
(B) The directing ability follows the approximate order: $\text{CN}^- \approx \text{CO} \approx \text{C}_2\text{H}_4 > \text{PR}_3 \approx \text{H}^- > \text{I}^- > \text{Br}^- > \text{Cl}^- > \text{NH}_3 > \text{H}_2\text{O}$.  
(C) Pure *cis*-$[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$ (cisplatin) can be synthesized by reacting $[\text{PtCl}_4]^{2-}$ with two equivalents of $\text{NH}_3$.  
(D) Reaction of $[\text{Pt}(\text{NH}_3)_4]^{2+}$ with two equivalents of $\text{HCl}$ yields pure *trans*-$[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$.

#### Question 22
Which of the following statements about boranes and boron compounds is/are CORRECT:
(A) Diborane ($\text{B}_2\text{H}_6$) has two $3\text{c}-2\text{e}$ $\text{B}-\text{H}-\text{B}$ bridge bonds and four terminal $2\text{c}-2\text{e}$ $\text{B}-\text{H}$ bonds.  
(B) Boric acid ($\text{H}_3\text{BO}_3$) acts as a weak Lewis acid by accepting $\text{OH}^-$ from water: $\text{B}(\text{OH})_3 + 2\text{H}_2\text{O} \rightleftharpoons [\text{B}(\text{OH})_4]^- + \text{H}_3\text{O}^+$.  
(C) Borazine ($\text{B}_3\text{N}_3\text{H}_6$, "inorganic benzene") is isoelectronic with benzene but undergoes addition reactions more readily due to bond polarity.  
(D) The terminal $\text{B}-\text{H}$ bond length is shorter than the bridging $\text{B}-\text{H}$ bond length in $\text{B}_2\text{H}_6$.

#### Question 23
Regarding carbocation rearrangements:
(A) The pinacol-pinacolone rearrangement involves protonation of a 1,2-diol followed by dehydration and 1,2-migration.  
(B) The driving force of the pinacol rearrangement is the stabilization of the resulting resonance-stabilized oxocarbenium ion.  
(C) Neopentyl alcohol undergoes rapid rearrangement in strong acid to form the more stable tertiary carbocation.  
(D) The migratory aptitude in pinacol rearrangement follows: $p\text{-anisyl} > p\text{-tolyl} > \text{phenyl} > \text{alkyl}$.

#### Question 24
In the extraction and metallurgy of metals:
(A) In the Hall-Héroult process, cryolite ($\text{Na}_3\text{AlF}_6$) lowers the melting point of alumina and increases electrical conductivity.  
(B) Ellingham diagrams show plots of $\Delta G^\circ$ versus temperature for metal oxide formation.  
(C) A metal can reduce the oxide of any other metal whose curve lies above it on the Ellingham diagram.  
(D) In the Mond process, nickel is purified via the formation and subsequent thermal decomposition of volatile $\text{Ni}(\text{CO})_4$.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
For the reaction $2\text{NO}_2(g) \rightleftharpoons \text{N}_2\text{O}_4(g)$, at $298\text{ K}$, $\Delta H^\circ = -57.2\text{ kJ/mol}$ and $\Delta S^\circ = -175.8\text{ J/(mol K)}$. Calculate the standard Gibbs free energy change $\Delta G^\circ$ in $\text{kJ/mol}$ rounded off to two decimal places.

#### Question 26
The rate constant of a reaction triples when the temperature is raised from $300\text{ K}$ to $310\text{ K}$. Calculate the activation energy $E_a$ in $\text{kJ/mol}$ rounded off to one decimal place. (Take $R = 8.314\text{ J/(mol K)}$ and $\ln 3 \approx 1.0986$).

#### Question 27
The conductivity of a saturated solution of $\text{BaSO}_4$ at $298\text{ K}$ is $\kappa = 3.06 \times 10^{-6}\text{ S cm}^{-1}$ and that of water used is $0.60 \times 10^{-6}\text{ S cm}^{-1}$. Given $\Lambda_m^\circ(\text{BaSO}_4) = 287.0\text{ S cm}^2\text{mol}^{-1}$, the solubility product $K_{\text{sp}}$ of $\text{BaSO}_4$ is $X \times 10^{-10}$. Find $X$ rounded off to two decimal places.

#### Question 28
Calculate the osmotic pressure in atmospheres exerted by a solution prepared by dissolving $1.0\text{ g}$ of a polymer of molar mass $185000\text{ g/mol}$ in $450\text{ mL}$ of water at $37^\circ\text{C}$ ($310\text{ K}$). Round off to two decimal places in units of $10^{-4}\text{ atm}$.

#### Question 29
A sample of hard water contains $12.0\text{ mg}$ of $\text{MgSO}_4$ (molar mass $120\text{ g/mol}$) per liter of water. The hardness of this water sample expressed in $\text{ppm}$ of $\text{CaCO}_3$ equivalent is $H\text{ ppm}$. Find $H$.

#### Question 30
In the electrolysis of aqueous $\text{CuSO}_4$ solution with inert electrodes, a steady current of $1.93\text{ A}$ is passed for $500\text{ seconds}$. The mass of copper deposited at the cathode is $m\text{ g}$. (Atomic mass of $\text{Cu} = 63.5\text{ g/mol}$, $F = 96500\text{ C/mol}$). Find $m$ rounded off to three decimal places.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following ligands is an ambidentate ligand:
(A) $\text{NO}_2^-$  
(B) $\text{NH}_3$  
(C) $\text{H}_2\text{O}$  
(D) $\text{en}$ (ethylenediamine)

#### Question 32
The oxidation state of sulfur in Marshall's acid ($\text{H}_2\text{S}_2\text{O}_8$) is:
(A) $+6$  
(B) $+7$  
(C) $+8$  
(D) $+5$

#### Question 33
Lucas reagent is a solution of:
(A) Anhydrous $\text{ZnCl}_2$ in conc. $\text{HCl}$  
(B) $\text{AlCl}_3$ in conc. $\text{HCl}$  
(C) $\text{ZnSO}_4$ in $\text{H}_2\text{SO}_4$  
(D) $\text{SnCl}_2$ in $\text{HCl}$

#### Question 34
Which of the following compounds exhibits optical isomerism:
(A) $[\text{Co}(\text{en})_3]^{3+}$  
(B) $[\text{Zn}(\text{NH}_3)_4]^{2+}$  
(C) $[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$  
(D) $[\text{Ni}(\text{CN})_4]^{2-}$

#### Question 35
The monomer units of Nylon 6,6 are:
(A) Hexamethylenediamine and Adipic acid  
(B) Caprolactam  
(C) Terephthalic acid and Ethylene glycol  
(D) Phenol and Formaldehyde

#### Question 36
The conjugate base of $\text{NH}_4^+$ is:
(A) $\text{NH}_3$  
(B) $\text{NH}_2^-$  
(C) $\text{NH}^{2-}$  
(D) $\text{N}^{3-}$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-coplanar vectors in $\mathbb{R}^3$:
(A) $\vec{a} \times (\vec{b} \times \vec{c}) + \vec{b} \times (\vec{c} \times \vec{a}) + \vec{c} \times (\vec{a} \times \vec{b}) = \vec{0}$ (Jacobi Identity).  
(B) $[\vec{a} \times \vec{b}\quad \vec{b} \times \vec{c}\quad \vec{c} \times \vec{a}] = [\vec{a}\quad \vec{b}\quad \vec{c}]^2$.  
(C) If $\vec{a}' = \frac{\vec{b} \times \vec{c}}{[\vec{a}\quad \vec{b}\quad \vec{c}]}$, then $\vec{a} \cdot \vec{a}' = 1$.  
(D) $[\vec{a} + \vec{b}\quad \vec{b} + \vec{c}\quad \vec{c} + \vec{a}] = 2[\vec{a}\quad \vec{b}\quad \vec{c}]$.

#### Question 38
Let $F(x) = \int_0^{x^2} \frac{\sin t}{1 + t} dt$ for $x > 0$:
(A) $F'(x) = \frac{2x \sin(x^2)}{1 + x^2}$ by Leibniz Rule.  
(B) $F(x)$ has critical points at $x = \sqrt{n\pi}$ ($n \in \mathbb{N}$).  
(C) $x = \sqrt{\pi}$ is a local maximum of $F(x)$.  
(D) $x = \sqrt{2\pi}$ is a local minimum of $F(x)$.

#### Question 39
Consider the family of ellipses $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$:
(A) The locus of the point of intersection of two perpendicular tangents is the director circle $x^2 + y^2 = a^2 + b^2$.  
(B) The product of perpendiculars drawn from the foci upon any tangent is constant and equal to $b^2$.  
(C) The feet of the perpendiculars from the foci onto any tangent lie on the auxiliary circle $x^2 + y^2 = a^2$.  
(D) The tangent at any point $P$ bisects the external angle between the focal radii $SP$ and $S'P$.

#### Question 40
Let $C_n = \begin{vmatrix} a & b & c \\ c & a & b \\ b & c & a \end{vmatrix}$ be a $3 \times 3$ circulant matrix:
(A) $\det(C_n) = a^3 + b^3 + c^3 - 3abc$.  
(B) $\det(C_n) = (a + b + c)(a + b\omega + c\omega^2)(a + b\omega^2 + c\omega)$ where $\omega$ is a complex cube root of unity.  
(C) If $a, b, c > 0$ and $a \ne b \ne c$, then $\det(C_n) > 0$.  
(D) If $a + b + c = 0$, then $\det(C_n) = 0$.

#### Question 41
Let $f(x) = \sin x - x + \frac{x^3}{6}$ for $x > 0$:
(A) $f'(x) = \cos x - 1 + \frac{x^2}{2} > 0$ for all $x > 0$.  
(B) $f(x) > 0$ for all $x > 0$.  
(C) $\sin x > x - \frac{x^3}{6}$ for all $x > 0$.  
(D) $\lim_{x \to 0} \frac{\sin x - x + x^3/6}{x^5} = \frac{1}{120}$.

#### Question 42
Let $A$ and $B$ be two $3 \times 3$ matrices such that $AB = BA$:
(A) $A$ and $B$ commute.  
(B) $(A+B)^2 = A^2 + 2AB + B^2$.  
(C) If $A$ is invertible, then $A^{-1}B = BA^{-1}$.  
(D) If $\vec{v}$ is an eigenvector of $A$ with unique eigenvalue $\lambda$, then $\vec{v}$ is also an eigenvector of $B$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate $\int_0^1 \frac{\ln(1+x)}{1+x^2} dx$. The value of the integral is $\frac{\pi}{k} \ln 2$. Find $k$.

#### Question 44
Find the number of positive integral solutions $(x, y, z)$ to the equation $x + y + z = 12$.

#### Question 45
Let the shortest distance between the skew lines $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $\frac{x-2}{3} = \frac{y-4}{4} = \frac{z-5}{5}$ be $d$. If $d^2 = \frac{1}{k}$, find $k$.

#### Question 46
Let $z$ be a complex number satisfying $z^5 = 1$ with $z \ne 1$. Find the value of $1 + z + z^2 + z^3 + z^4$.

#### Question 47
Find the number of points of discontinuity of the function $f(x) = [2x]$ in the open interval $(0, 3)$, where $[\cdot]$ denotes the greatest integer function.

#### Question 48
A committee of 4 persons is to be chosen from 5 men and 4 women. If the committee must contain at least 2 women, the number of ways to form the committee is $N$. Find $N$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The value of $\lim_{n \to \infty} \left(1 + \frac{2}{n}\right)^n$ is:
(A) $e^2$  
(B) $e$  
(C) $2e$  
(D) $1$

#### Question 50
The area bounded by the curve $y = \sin x$, the $x$-axis, and the lines $x = 0$ to $x = 2\pi$ is:
(A) 4  
(B) 2  
(C) 0  
(D) 1

#### Question 51
If the lines $3x + 4y - 5 = 0$ and $4x - 3y + 2 = 0$ are tangents to a circle, the angle between the two lines is:
(A) $90^\circ$  
(B) $60^\circ$  
(C) $45^\circ$  
(D) $30^\circ$

#### Question 52
If $\omega$ is a complex cube root of unity, then $(1 - \omega + \omega^2)^5 + (1 + \omega - \omega^2)^5$ is:
(A) 32  
(B) $-32$  
(C) 64  
(D) $-64$

#### Question 53
The maximum value of $3\sin\theta + 4\cos\theta$ is:
(A) 5  
(B) 7  
(C) 1  
(D) 25

#### Question 54
The probability of drawing an ace or a king from a well-shuffled standard pack of 52 cards is:
(A) $2/13$  
(B) $1/13$  
(C) $1/26$  
(D) $4/13$
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
A thin spherical conducting shell of radius $R_1$ carries charge $+Q$. It is surrounded by a concentric dielectric shell with inner radius $R_1$, outer radius $R_2$, and relative permittivity $\varepsilon_r$:
(A) The electric displacement $\vec{D}$ in $R_1 < r < R_2$ is $\vec{D} = \frac{Q}{4\pi r^2}\hat{r}$.  
(B) The electric field in $R_1 < r < R_2$ is $\vec{E} = \frac{Q}{4\pi \varepsilon_0 \varepsilon_r r^2}\hat{r}$.  
(C) The total bound surface charge at $r = R_1$ is $q_{b1} = -Q\left(1 - \frac{1}{\varepsilon_r}\right)$.  
(D) The total bound surface charge at $r = R_2$ is $q_{b2} = +Q\left(1 - \frac{1}{\varepsilon_r}\right)$.

#### Question 2
In an electromagnetic plane wave traveling along the $+z$ direction in vacuum:
(A) The electric field $\vec{E}$ and magnetic field $\vec{B}$ oscillate in phase.  
(B) The magnitude ratio is $|\vec{E}|/|\vec{B}| = c$.  
(C) The energy densities in electric and magnetic fields are equal: $u_e = u_m$.  
(D) The instantaneous Poynting vector is $\vec{S} = c u \hat{k}$ where $u$ is the total instantaneous energy density.

#### Question 3
A uniform solid sphere of mass $M$ and radius $R$ is given a purely translational velocity $v_0$ on a rough horizontal surface with coefficient of kinetic friction $\mu$:
(A) The friction force acts in the direction opposite to motion and has magnitude $\mu M g$.  
(B) The angular acceleration about the center of mass is $\alpha = \frac{5\mu g}{2R}$.  
(C) Pure rolling begins at time $t_r = \frac{2v_0}{7\mu g}$.  
(D) The velocity of the sphere at the onset of pure rolling is $v = \frac{5}{7}v_0$.

#### Question 4
A metallic rod of mass $m$ and length $L$ falls vertically from rest in a horizontal magnetic field $B$ while sliding on two vertical, frictionless conducting rails connected at the top by a resistor $R$:
(A) The induced EMF is $\mathcal{E} = B L v$.  
(B) The upward magnetic Lorentz force is $F = \frac{B^2 L^2 v}{R}$.  
(C) The terminal velocity of the rod is $v_t = \frac{mgR}{B^2 L^2}$.  
(D) At terminal velocity, the rate of potential energy loss equals the rate of Joule heating in the resistor.

#### Question 5
A particle executes simple harmonic motion along the $x$-axis with equation $x(t) = A\cos(\omega t + \phi)$:
(A) The acceleration is proportional and opposite to displacement: $a = -\omega^2 x$.  
(B) The time-averaged kinetic energy over one full cycle is $\langle K \rangle = \frac{1}{4} m \omega^2 A^2$.  
(C) The time-averaged potential energy over one full cycle is $\langle U \rangle = \frac{1}{4} m \omega^2 A^2$.  
(D) The position-averaged kinetic energy over the interval $[-A, A]$ is $\frac{1}{3} m \omega^2 A^2$.

#### Question 6
Regarding interference in thin films:
(A) For normal incidence on a film of refractive index $\mu$ in air, reflection at the upper surface introduces a phase shift of $\pi$.  
(B) The condition for constructive interference in reflected light is $2\mu d = (m + 1/2)\lambda$.  
(C) The condition for destructive interference in reflected light is $2\mu d = m\lambda$.  
(D) The colors seen in soap bubbles arise from thin-film optical interference.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A parallel-plate capacitor with plate area $A = 0.05\text{ m}^2$ and separation $d = 2.0\text{ mm}$ is filled with two dielectric slabs of equal thickness $1.0\text{ mm}$ with dielectric constants $\kappa_1 = 2$ and $\kappa_2 = 4$. If $\varepsilon_0 = 8.85 \times 10^{-12}\text{ F/m}$, the capacitance in picofarads ($\text{pF}$) is $C$. Find $C$ rounded off to one decimal place.

#### Question 8
A proton of mass $m = 1.67 \times 10^{-27}\text{ kg}$ and charge $q = 1.6 \times 10^{-19}\text{ C}$ moves in a circular path of radius $r = 0.50\text{ m}$ in a uniform magnetic field $B = 0.20\text{ T}$. The kinetic energy of the proton in mega-electronvolts ($\text{MeV}$) is $K\text{ MeV}$. Find $K$ rounded off to two decimal places.

#### Question 9
In an $RL$ circuit, an inductor $L = 0.50\text{ H}$ and resistor $R = 25\text{ }\Omega$ are connected in series to a $100\text{ V}$ DC source. The initial rate of rise of current $(di/dt)_{t=0}$ in $\text{A/s}$ is $X$. Find $X$.

#### Question 10
A siren emitting a frequency of $500\text{ Hz}$ moves toward a stationary observer at $20\text{ m/s}$. If the speed of sound in air is $340\text{ m/s}$, the apparent frequency heard by the observer is $f'\text{ Hz}$. Find $f'$ rounded off to the nearest integer.

#### Question 11
A concave mirror of focal length $f = 20\text{ cm}$ produces a real image that is twice the size of the object. The distance of the object from the mirror is $u\text{ cm}$. Find $u$.

#### Question 12
The work function of caesium is $\Phi = 2.14\text{ eV}$. The threshold frequency for photoelectric emission from caesium is $\nu_0 \times 10^{14}\text{ Hz}$. (Take $h = 4.14 \times 10^{-15}\text{ eV s}$). Find $\nu_0$ rounded off to two decimal places.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The magnetic field at the center of a circular loop of radius $R$ carrying steady current $I$ is:
(A) $\frac{\mu_0 I}{2R}$  
(B) $\frac{\mu_0 I}{2\pi R}$  
(C) $\frac{\mu_0 I}{4R}$  
(D) $\frac{\mu_0 I}{4\pi R}$

#### Question 14
Two point charges $+q$ and $-q$ are separated by distance $2a$. The electric potential at any point on the equatorial plane is:
(A) Zero  
(B) $\frac{q}{4\pi\varepsilon_0 a}$  
(C) $\frac{q}{2\pi\varepsilon_0 a}$  
(D) Infinite

#### Question 15
The time constant of a capacitive circuit with resistance $R = 100\text{ k}\Omega$ and capacitance $C = 10\text{ }\mu\text{F}$ is:
(A) $1.0\text{ s}$  
(B) $0.1\text{ s}$  
(C) $10.0\text{ s}$  
(D) $0.01\text{ s}$

#### Question 16
In a diffraction grating, the resolving power is proportional to:
(A) Total number of lines $N$ and diffraction order $m$  
(B) Grating width only  
(C) Slit separation only  
(D) Wavelength $\lambda$

#### Question 17
A heat engine operating on a Carnot cycle absorbs $1000\text{ J}$ of heat from a reservoir at $400\text{ K}$ and rejects heat to a reservoir at $300\text{ K}$. The heat rejected per cycle is:
(A) $750\text{ J}$  
(B) $500\text{ J}$  
(C) $250\text{ J}$  
(D) $800\text{ J}$

#### Question 18
The half-life of a radioactive nucleus is $T$. In time $2T$, the probability that a particular nucleus has decayed is:
(A) $3/4$  
(B) $1/4$  
(C) $1/2$  
(D) $7/8$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
According to the Debye-Hückel limiting law for electrolyte solutions at $298\text{ K}$:
(A) The mean ionic activity coefficient satisfies $\log_{10} \gamma_{\pm} = -A |z_+ z_-|\sqrt{I}$.  
(B) The ionic strength of the solution is defined as $I = \frac{1}{2}\sum c_i z_i^2$.  
(C) The constant $A$ depends on the dielectric constant of the solvent and temperature.  
(D) For a 1:1 electrolyte like $\text{NaCl}$, $I = c$.

#### Question 20
Regarding the Gibbs-Duhem equation at constant temperature and pressure:
(A) $\sum n_i d\mu_i = 0$ for a closed multicomponent system.  
(B) For a binary solution, $x_1 d\mu_1 + x_2 d\mu_2 = 0$.  
(C) If the chemical potential of component 1 increases, the chemical potential of component 2 must decrease.  
(D) It provides a thermodynamic consistency check for measured vapor pressures.

#### Question 21
Regarding the preparation and properties of diborane ($\text{B}_2\text{H}_6$):
(A) Industrial synthesis involves the reaction of $\text{BF}_3$ with $\text{NaH}$ at $450\text{ K}$.  
(B) Laboratory preparation involves the oxidation of $\text{NaBH}_4$ with $\text{I}_2$.  
(C) $\text{B}_2\text{H}_6$ reacts with ammonia at low temperatures to give $\text{B}_2\text{H}_6 \cdot 2\text{NH}_3$, which on heating yields borazine ($\text{B}_3\text{N}_3\text{H}_6$).  
(D) It ignites spontaneously in air releasing a large quantity of heat.

#### Question 22
Which of the following polymers are classified as condensation polymers:
(A) Dacron (Terylene)  
(B) Nylon 6,6  
(C) Bakelite  
(D) Polythene

#### Question 23
Regarding the stereochemistry of nucleophilic substitutions:
(A) $\text{S}_N2$ reactions proceed with complete inversion of configuration (Walden inversion).  
(B) $\text{S}_N1$ reactions proceeding through a planar carbocation typically result in partial or complete racemization.  
(C) $\text{S}_N\text{i}$ reaction of secondary alcohols with $\text{SOCl}_2$ in dioxane proceeds with retention of configuration.  
(D) In the presence of pyridine, reaction of alcohols with $\text{SOCl}_2$ gives inversion of configuration.

#### Question 24
Regarding the chemistry of transition metals:
(A) $\text{Sc}^{3+}$ is diamagnetic ($d^0$).  
(B) $\text{Zn}^{2+}$ is diamagnetic ($d^{10}$).  
(C) $\text{Cr}^{3+}$ has $d^3$ configuration with 3 unpaired electrons.  
(D) Transition metals form interstitial compounds with small atoms like $\text{H}, \text{C}, \text{N}$.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{PbI}_2$ is $K_{\text{sp}} = 7.0 \times 10^{-9}$ at $298\text{ K}$. Calculate its molar solubility in pure water in $\text{mmol/L}$ rounded off to two decimal places.

#### Question 26
For the equilibrium $\text{PCl}_5(g) \rightleftharpoons \text{PCl}_3(g) + \text{Cl}_2(g)$, at $500\text{ K}$, $K_p = 1.80\text{ bar}$. If the total equilibrium pressure is $3.0\text{ bar}$, find the degree of dissociation $\alpha$ rounded off to two decimal places.

#### Question 27
The standard reduction potential for $\text{Fe}^{3+} + e^- \to \text{Fe}^{2+}$ is $+0.77\text{ V}$ and for $\text{Fe}^{2+} + 2e^- \to \text{Fe}$ is $-0.44\text{ V}$. Find the standard reduction potential for $\text{Fe}^{3+} + 3e^- \to \text{Fe}$ in volts rounded off to two decimal places.

#### Question 28
The rate constant for a second-order reaction $2A \to \text{Products}$ is $k = 0.050\text{ M}^{-1}\text{s}^{-1}$. The half-life of this reaction when initial concentration $[A]_0 = 0.20\text{ M}$ is $t_{1/2}\text{ s}$. Find $t_{1/2}$.

#### Question 29
A compound has the molecular formula $\text{CrCl}_3 \cdot 6\text{H}_2\text{O}$. When $0.1\text{ mole}$ of this compound is treated with excess $\text{AgNO}_3(aq)$, $0.2\text{ mole}$ of $\text{AgCl}$ is precipitated. The number of coordinated water molecules in this complex is $N$. Find $N$.

#### Question 30
Calculate the standard enthalpy of combustion of propane ($\text{C}_3\text{H}_8$) in $\text{kJ/mol}$ given: $\Delta_f H^\circ(\text{C}_3\text{H}_8) = -104\text{ kJ/mol}$, $\Delta_f H^\circ(\text{CO}_2) = -394\text{ kJ/mol}$, and $\Delta_f H^\circ(\text{H}_2\text{O}) = -286\text{ kJ/mol}$. Report the magnitude $|\Delta H^\circ|$ in $\text{kJ/mol}$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The major product of the reaction between propene and $\text{HBr}$ in the presence of benzoyl peroxide is:
(A) 1-Bromopropane  
(B) 2-Bromopropane  
(C) 1,2-Dibromopropane  
(D) Allyl bromide

#### Question 32
The geometry of $\text{SF}_6$ is:
(A) Octahedral  
(B) Trigonal bipyramidal  
(C) Tetrahedral  
(D) Square planar

#### Question 33
Which of the following compounds is the strongest Bronsted base in aqueous medium:
(A) Dimethylamine ($(\text{CH}_3)_2\text{NH}$)  
(B) Methylamine ($\text{CH}_3\text{NH}_2$)  
(C) Trimethylamine ($(\text{CH}_3)_3\text{N}$)  
(D) Ammonia ($\text{NH}_3$)

#### Question 34
The hybridization of carbon in graphite is:
(A) $sp^2$  
(B) $sp^3$  
(C) $sp$  
(D) $dsp^2$

#### Question 35
Which of the following vitamins is water-soluble:
(A) Vitamin C  
(B) Vitamin A  
(C) Vitamin D  
(D) Vitamin K

#### Question 36
The IUPAC name of $\text{CH}_3-\text{CH}(\text{OH})-\text{COOH}$ is:
(A) 2-Hydroxypropanoic acid  
(B) Lactic acid  
(C) 1-Hydroxyethanoic acid  
(D) 2-Carboxyethanol

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \arctan x + \arctan\left(\frac{1-x}{1+x}\right)$ for $x > -1$:
(A) $f'(x) = 0$ for all $x > -1$.  
(B) $f(x) = \frac{\pi}{4}$ for all $x > -1$.  
(C) The function $f(x)$ is a constant function on $(-1, \infty)$.  
(D) $f(1) = \frac{\pi}{4}$.

#### Question 38
Let $A$ and $B$ be two symmetric matrices of order $n$:
(A) $A + B$ is symmetric.  
(B) $AB$ is symmetric if and only if $AB = BA$.  
(C) $AB - BA$ is skew-symmetric.  
(D) $AB + BA$ is symmetric.

#### Question 39
Consider the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$:
(A) The equations of the asymptotes are $y = \pm \frac{b}{a}x$.  
(B) The product of perpendiculars from any point on the hyperbola to its asymptotes is constant and equal to $\frac{a^2 b^2}{a^2 + b^2}$.  
(C) The eccentricity satisfies $e = \sqrt{1 + b^2/a^2}$.  
(D) A rectangular hyperbola has eccentricity $e = \sqrt{2}$.

#### Question 40
Let $I = \int_0^1 x^p (1-x)^q dx$ where $p, q > -1$:
(A) $I$ is the Euler Beta function $B(p+1, q+1)$.  
(B) $B(p+1, q+1) = \frac{\Gamma(p+1)\Gamma(q+1)}{\Gamma(p+q+2)}$.  
(C) $B(p+1, q+1) = B(q+1, p+1)$.  
(D) If $p = 1, q = 1$, then $I = 1/6$.

#### Question 41
Let the roots of the cubic equation $x^3 - 6x^2 + 11x - 6 = 0$ be $\alpha, \beta, \gamma$:
(A) The roots are 1, 2, and 3.  
(B) $\alpha + \beta + \gamma = 6$.  
(C) $\alpha\beta + \beta\gamma + \gamma\alpha = 11$.  
(D) $\alpha\beta\gamma = 6$.

#### Question 42
Consider the differential equation $\frac{d^2 y}{dx^2} + 4y = 0$:
(A) The general solution is $y(x) = C_1 \cos(2x) + C_2 \sin(2x)$.  
(B) The solution is periodic with period $T = \pi$.  
(C) If $y(0) = 1$ and $y'(0) = 0$, then $y(x) = \cos(2x)$.  
(D) All non-trivial solutions are bounded on $\mathbb{R}$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = 4 - x^2$ and the $x$-axis. Round off to two decimal places.

#### Question 44
Find the coefficient of $x^4$ in the expansion of $(1 + x + x^2 + x^3)^4$.

#### Question 45
Find the acute angle in degrees between the lines whose direction ratios are $(1, 1, 0)$ and $(1, 0, 1)$.

#### Question 46
Let $A$ be a $3 \times 3$ matrix such that $\det(A) = 4$. Find $\det(2 A^{-1})$.

#### Question 47
How many 4-digit numbers can be formed using the digits 1, 2, 3, 4, 5 without repetition?

#### Question 48
Find the radius of the circle $x^2 + y^2 - 4x - 6y - 12 = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\ln(\sec x + \tan x)$ with respect to $x$ is:
(A) $\sec x$  
(B) $\tan x$  
(C) $\sec x \tan x$  
(D) $\sec^2 x$

#### Question 50
The locus of the center of a circle which touches externally two given circles is:
(A) A hyperbola  
(B) An ellipse  
(C) A parabola  
(D) A circle

#### Question 51
If $\vec{a}$ and $\vec{b}$ are unit vectors such that $|\vec{a} + \vec{b}| = \sqrt{3}$, the angle between $\vec{a}$ and $\vec{b}$ is:
(A) $\pi/3$  
(B) $\pi/6$  
(C) $\pi/2$  
(D) $2\pi/3$

#### Question 52
The value of $\int_0^{\pi/2} \sin^2 x dx$ is:
(A) $\pi/4$  
(B) $\pi/2$  
(C) $\pi$  
(D) $1$

#### Question 53
The term independent of $x$ in the expansion of $\left(x + \frac{1}{x}\right)^{10}$ is:
(A) $\binom{10}{5} = 252$  
(B) $\binom{10}{4} = 210$  
(C) $\binom{10}{6} = 210$  
(D) 120

#### Question 54
If $P(A) = 0.6, P(B) = 0.3$, and $P(A \cap B) = 0.2$, then $P(A \mid B)$ is:
(A) $2/3$  
(B) $1/3$  
(C) $1/2$  
(D) $3/5$
"""

        raw_sol1 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 1)
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)

---

# PART I: PHYSICS

### Question 1
- **Concept**: Betatron Condition.
- **Step 1**: Faraday's law gives induced electric field $E(2\pi R_0) = \frac{d\Phi}{dt} = \pi R_0^2 \frac{d\langle B \rangle}{dt} \implies E = \frac{R_0}{2}\frac{d\langle B \rangle}{dt}$.
- **Step 2**: Lorentz force for circular orbit: $p = e R_0 B(R_0) \implies \frac{dp}{dt} = e R_0 \frac{dB(R_0)}{dt}$.
- **Step 3**: Newton's second law: $\frac{dp}{dt} = e E = \frac{e R_0}{2}\frac{d\langle B \rangle}{dt}$.
- **Step 4**: Equating the two expressions: $\frac{dB(R_0)}{dt} = \frac{1}{2}\frac{d\langle B \rangle}{dt} \implies \langle B \rangle = 2 B(R_0)$.
- **Correct Options**: (A, B, C, D)

### Question 2
- **Concept**: Poynting vector in a current-carrying resistor.
- **Step 1**: Current density $J = I/(\pi a^2) \implies E = J/\sigma = \frac{I}{\sigma \pi a^2}\hat{k}$. (A) is correct.
- **Step 2**: Surface magnetic field $B(a) = \frac{\mu_0 I}{2\pi a}\hat{\phi}$. (B) is correct.
- **Step 3**: $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B}) = \frac{1}{\mu_0} (E \hat{k}) \times (B \hat{\phi}) = -\frac{E B}{\mu_0}\hat{r}$, pointing inward. (C) is correct.
- **Step 4**: Surface integral $\oint \vec{S} \cdot d\vec{A} = S(2\pi a L) = \frac{1}{\mu_0} \frac{I}{\sigma \pi a^2} \frac{\mu_0 I}{2\pi a} (2\pi a L) = \frac{I^2 L}{\sigma \pi a^2} = I^2 R$. (D) is correct.
- **Correct Options**: (A, B, C, D)

### Question 3
- **Concept**: Parallel-plate transmission line parameters.
- **Step 1**: Capacitance per unit length: $\mathcal{C} = \frac{\varepsilon_0 w}{d}$.
- **Step 2**: Inductance per unit length: $\mathcal{L} = \frac{\mu_0 d}{w}$.
- **Step 3**: Wave speed: $v = 1/\sqrt{\mathcal{L}\mathcal{C}} = 1/\sqrt{\mu_0 \varepsilon_0} = c$.
- **Step 4**: Characteristic impedance: $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}} = \frac{d}{w}\sqrt{\mu_0/\varepsilon_0}$.
- **Correct Options**: (A, B, C, D)

### Question 4
- **Concept**: Eddy current braking.
- **Step 1**: Localized field produces asymmetric eddy currents.
- **Step 2**: Retarding Lorentz torque $\tau = -\gamma \omega$.
- **Step 3**: Equation of motion $I \frac{d\omega}{dt} = -\gamma \omega \implies \omega(t) = \omega_0 e^{-t/\tau_d}$.
- **Correct Options**: (A, B, C, D)

### Question 5
- **Concept**: Wave plates and polarization.
- **Step 1**: Phase difference $\Delta \phi = \frac{2\pi}{\lambda}|n_e - n_o|t = \pi/2 \implies t = \frac{\lambda}{4|n_e - n_o|}$. (A) is correct.
- **Step 2**: At $45^\circ$, $E_x = E_y$, phase difference $\pi/2$ creates circularly polarized light. (B) is correct.
- **Step 3**: Linearly polarized parallel to optic axis experiences only one refractive index, unchanged. (C) is correct.
- **Step 4**: Half-wave plate creates $\pi$ phase shift. (D) is correct.
- **Correct Options**: (A, B, C, D)

### Question 6
- **Concept**: van der Waals gas critical parameters.
- **Step 1**: At critical point, $\left(\frac{\partial P}{\partial V}\right)_T = 0$ and $\left(\frac{\partial^2 P}{\partial V^2}\right)_T = 0$.
- **Step 2**: Yields $V_c = 3b$, $P_c = \frac{a}{27b^2}$, $T_c = \frac{8a}{27Rb}$.
- **Step 3**: Compressibility factor $Z_c = \frac{P_c V_c}{R T_c} = \frac{(a/27b^2)(3b)}{R(8a/27Rb)} = \frac{3}{8} = 0.375$.
- **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: Displacement current $I_d = \varepsilon_0 A \frac{dE}{dt} = (8.85 \times 10^{-12})(0.04)(1.0 \times 10^{12}) = 0.354\text{ A} \implies \mathbf{0.35}$.
- **Q8**: Toroid inductance $L = \frac{\mu_0 N^2 A}{2\pi R} = \frac{(4\pi \times 10^{-7})(10^6)(10^{-3})}{2\pi (0.20)} = 1.0 \times 10^{-3}\text{ H}$. Energy $U = \frac{1}{2} L I^2 = \frac{1}{2}(1.0 \times 10^{-3})(2.0)^2 = 2.0\text{ mJ} \implies \mathbf{2.00}$.
- **Q9**: $\beta = \frac{\lambda D}{2h} = \frac{(600 \times 10^{-9})(1.20)}{2(1.50 \times 10^{-3})} = 0.24\text{ mm} \implies \mathbf{0.24}$.
- **Q10**: Carnot efficiency $\eta_{\text{Carnot}} = 1 - 300/600 = 0.50$. Actual efficiency $\eta = 0.75 \times 0.50 = 0.375$. Work $W = \eta Q_H = 0.375 \times 4000 = 1500\text{ J} \implies \mathbf{1500.00}$.
- **Q11**: $M = k\sqrt{L_1 L_2} = 0.50\sqrt{0.18 \times 0.32} = 0.50\sqrt{0.0576} = 0.50 \times 0.24 = 0.12\text{ H} \implies \mathbf{0.12}$.
- **Q12**: $V = \frac{1}{2} B \omega L^2 = \frac{1}{2}(0.50)(20)(1.0)^2 = 5.0\text{ V} \implies \mathbf{5.00}$.

### Questions 13 to 18
- **Q13**: Magnetic energy density $u_m = \frac{B^2}{2\mu_0}$. **Correct: (A)**.
- **Q14**: By Lenz's law, induced currents oppose relative motion during approach and during recession, so acceleration is always less than $g$. **Correct: (B)**.
- **Q15**: $Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$. **Correct: (A)**.
- **Q16**: $v_1 = \frac{e^2}{2\varepsilon_0 h} = \alpha c$ where $\alpha = \frac{e^2}{2\varepsilon_0 h c} \approx \frac{1}{137}$. **Correct: (A)**.
- **Q17**: First minimum: $a\sin\theta = \lambda \implies a\theta = 650\text{ nm}$. First secondary maximum: $a\theta = \frac{3}{2}\lambda' \implies \lambda' = \frac{2}{3}(650) \approx 433.3\text{ nm}$. **Correct: (A)**.
- **Q18**: Monoatomic gas: $C_V = 3R/2$, $C_P = 5R/2 \implies \gamma = 5/3$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Jahn-Teller distortion fundamentals. **Correct Options**: (A, B, C, D)
- **Q20**: Consecutive reaction kinetics solutions. **Correct Options**: (A, B, C, D)
- **Q21**: Trans-effect directing series and synthesis routes to cisplatin and transplatin. **Correct Options**: (A, B, C, D)
- **Q22**: Boron hydrides and boric acid characteristics. **Correct Options**: (A, B, C, D)
- **Q23**: Carbocation rearrangements and migratory aptitudes. **Correct Options**: (A, B, C, D)
- **Q24**: Metallurgical principles and Ellingham diagram rules. **Correct Options**: (A, B, C, D)

### Questions 25 to 30
- **Q25**: $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ = -57.2 - 298(-0.1758) = -57.2 + 52.39 = -4.81\text{ kJ/mol} \implies \mathbf{-4.81}$.
- **Q26**: $\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies 1.0986 = \frac{E_a}{8.314}\left(\frac{10}{300 \times 310}\right) \implies E_a = \frac{1.0986 \times 8.314 \times 93000}{10} \approx 84.9\text{ kJ/mol} \implies \mathbf{84.90}$.
- **Q27**: $\kappa_{\text{BaSO}_4} = 3.06 \times 10^{-6} - 0.60 \times 10^{-6} = 2.46 \times 10^{-6}\text{ S cm}^{-1}$. Solubility $S = \frac{1000 \kappa}{\Lambda_m^\circ} = \frac{2.46 \times 10^{-3}}{287.0} = 8.57 \times 10^{-6}\text{ M}$. $K_{\text{sp}} = S^2 = (8.57 \times 10^{-6})^2 \approx 7.35 \times 10^{-11} = 0.74 \times 10^{-10} \implies \mathbf{0.74}$.
- **Q28**: Molarity $M = \frac{1.0 / 185000}{0.450} = 1.20 \times 10^{-5}\text{ M}$. $\Pi = MRT = (1.20 \times 10^{-5})(0.0821)(310) = 3.06 \times 10^{-4}\text{ atm} \implies \mathbf{3.06}$.
- **Q29**: Moles of $\text{MgSO}_4 = \frac{12.0\text{ mg}}{120\text{ g/mol}} = 0.10\text{ mmol/L}$. Equivalent $\text{CaCO}_3 = 0.10\text{ mmol} \times 100\text{ mg/mmol} = 10.0\text{ mg/L} = 10\text{ ppm} \implies \mathbf{10.00}$.
- **Q30**: $m = \frac{M I t}{n F} = \frac{63.5 \times 1.93 \times 500}{2 \times 96500} = \frac{61277.5}{193000} \approx 0.318\text{ g} \implies \mathbf{0.318}$.

### Questions 31 to 36
- **Q31**: $\text{NO}_2^-$ can coordinate via N (nitro) or O (nitrito). **Correct: (A)**.
- **Q32**: Marshall's acid has a peroxo linkage $-\text{O}-\text{O}-$; sulfur oxidation state is $+6$. **Correct: (A)**.
- **Q33**: Lucas reagent is anhydrous $\text{ZnCl}_2$ in conc. $\text{HCl}$. **Correct: (A)**.
- **Q34**: $[\text{Co}(\text{en})_3]^{3+}$ is chiral (non-superimposable mirror images). **Correct: (A)**.
- **Q35**: Nylon 6,6 is made from hexamethylenediamine and adipic acid. **Correct: (A)**.
- **Q36**: Conjugate base of $\text{NH}_4^+$ is $\text{NH}_3$. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Standard vector identities and reciprocal systems of vectors. **Correct Options**: (A, B, C, D)
- **Q38**: Leibniz rule for differentiation of integrals. Critical points and concavity. **Correct Options**: (A, B, C, D)
- **Q39**: Loci and properties associated with tangents to an ellipse. **Correct Options**: (A, B, C, D)
- **Q40**: Circulant matrix determinant factorizations. **Correct Options**: (A, B, C, D)
- **Q41**: Taylor series remainder and polynomial inequality for $\sin x$. **Correct Options**: (A, B, C, D)
- **Q42**: Commuting matrices properties. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Let $x = \tan\theta \implies I = \int_0^{\pi/4} \ln(1+\tan\theta) d\theta = \frac{\pi}{8}\ln 2 \implies k = \mathbf{8.00}$.
- **Q44**: Positive integral solutions: $\binom{12-1}{3-1} = \binom{11}{2} = 55 \implies \mathbf{55.00}$.
- **Q45**: Vectors $\vec{u} = (2, 3, 4)$, $\vec{v} = (3, 4, 5)$. $\vec{u} \times \vec{v} = (-1, 2, -1)$. Point difference $\vec{r} = (1, 2, 2)$. Shortest distance $d = \frac{|\vec{r} \cdot (\vec{u} \times \vec{v})|}{|\vec{u} \times \vec{v}|} = \frac{|-1 + 4 - 2|}{\sqrt{1 + 4 + 1}} = \frac{1}{\sqrt{6}} \implies d^2 = 1/6 \implies k = \mathbf{6.00}$.
- **Q46**: $1 + z + z^2 + z^3 + z^4 = \frac{z^5 - 1}{z - 1} = 0 \implies \mathbf{0.00}$.
- **Q47**: $[2x]$ has discontinuities where $2x \in \mathbb{Z}$. In $(0, 3)$, $2x \in (0, 6)$. Integers: $1, 2, 3, 4, 5 \implies 5$ points. $\mathbf{5.00}$.
- **Q48**: Total ways: 2 women $\binom{4}{2}\binom{5}{2} = 6 \times 10 = 60$; 3 women $\binom{4}{3}\binom{5}{1} = 4 \times 5 = 20$; 4 women $\binom{4}{4}\binom{5}{0} = 1$. Total $N = 60 + 20 + 1 = 81 \implies \mathbf{81.00}$.

### Questions 49 to 54
- **Q49**: Standard limit $\lim_{n \to \infty} (1 + 2/n)^n = e^2$. **Correct: (A)**.
- **Q50**: Area $= \int_0^{2\pi} |\sin x| dx = 2 \int_0^\pi \sin x dx = 2(2) = 4$. **Correct: (A)**.
- **Q51**: Product of slopes $m_1 m_2 = (-3/4)(4/3) = -1 \implies 90^\circ$. **Correct: (A)**.
- **Q52**: Since $1 + \omega^2 = -\omega$ and $1 + \omega = -\omega^2$, $(-2\omega)^5 + (-2\omega^2)^5 = -32\omega^2 - 32\omega = -32(\omega^2 + \omega) = -32(-1) = 32$. **Correct: (A)**.
- **Q53**: $\sqrt{3^2 + 4^2} = 5$. **Correct: (A)**.
- **Q54**: 4 aces and 4 kings $= 8$ cards. $P = 8/52 = 2/13$. **Correct: (A)**.
"""

        raw_sol2 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 2)
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Dielectric spherical shell: $\vec{D} = \frac{Q}{4\pi r^2}\hat{r}$, $\vec{E} = \frac{Q}{4\pi\varepsilon_0\varepsilon_r r^2}\hat{r}$, $\sigma_b = \vec{P} \cdot \hat{n}$. Bound charges at boundaries $q_{b1} = -Q(1-1/\varepsilon_r)$, $q_{b2} = +Q(1-1/\varepsilon_r)$. **Correct Options**: (A, B, C, D)
- **Q2**: Plane EM waves in vacuum. In phase, $E = cB$, equal energy densities, instantaneous Poynting vector $\vec{S} = c u \hat{k}$. **Correct Options**: (A, B, C, D)
- **Q3**: Rolling with slipping transition: $\mu M g$ retards center of mass, torque $\mu M g R$ increases $\omega$. Pure rolling occurs at $t = \frac{2v_0}{7\mu g}$ with velocity $v = \frac{5}{7}v_0$. **Correct Options**: (A, B, C, D)
- **Q4**: Falling rod on rails under gravity with magnetic braking. Terminal velocity balances gravity force. Joule heating equals potential energy loss rate. **Correct Options**: (A, B, C, D)
- **Q5**: Simple harmonic motion averages: time averages are both $\frac{1}{4}m\omega^2 A^2$. Position average of kinetic energy is $\frac{1}{2A}\int_{-A}^A \frac{1}{2}m\omega^2(A^2 - x^2)dx = \frac{1}{3}m\omega^2 A^2$. **Correct Options**: (A, B, C, D)
- **Q6**: Thin film interference: phase change of $\pi$ on reflection at denser medium, path difference conditions. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: Two equal thickness capacitors in series: $C_1 = \frac{\kappa_1 \varepsilon_0 A}{d/2} = \frac{2 \times 8.85 \times 10^{-12} \times 0.05}{1.0 \times 10^{-3}} = 885\text{ pF}$. $C_2 = \frac{4 \times 8.85 \times 10^{-12} \times 0.05}{1.0 \times 10^{-3}} = 1770\text{ pF}$. $C_{\text{eq}} = \frac{C_1 C_2}{C_1 + C_2} = \frac{885 \times 1770}{2655} = 590.0\text{ pF} \implies \mathbf{590.00}$.
- **Q8**: $p = q B r = (1.6 \times 10^{-19})(0.20)(0.50) = 1.6 \times 10^{-20}\text{ kg m/s}$. $K = \frac{p^2}{2m} = \frac{(1.6 \times 10^{-20})^2}{2(1.67 \times 10^{-27})} = 7.66 \times 10^{-14}\text{ J} = \frac{7.66 \times 10^{-14}}{1.6 \times 10^{-13}}\text{ MeV} \approx 0.48\text{ MeV} \implies \mathbf{0.48}$.
- **Q9**: At $t = 0$, current $i = 0$, so voltage across inductor is $V = 100\text{ V}$. $L \frac{di}{dt} = V \implies \frac{di}{dt} = \frac{100}{0.50} = 200\text{ A/s} \implies \mathbf{200.00}$.
- **Q10**: Doppler effect: $f' = f \left(\frac{v}{v - v_s}\right) = 500 \left(\frac{340}{340 - 20}\right) = 500 \left(\frac{340}{320}\right) \approx 531.25\text{ Hz} \implies \mathbf{531.00}$.
- **Q11**: Real image $\implies m = -v/u = -2 \implies v = 2u$. Mirror formula: $1/v + 1/u = 1/f \implies 1/(2u) + 1/u = -1/20 \implies 3/(2u) = -1/20 \implies u = -30\text{ cm} \implies \mathbf{30.00}$.
- **Q12**: $\nu_0 = \Phi / h = \frac{2.14\text{ eV}}{4.14 \times 10^{-15}\text{ eV s}} \approx 5.17 \times 10^{14}\text{ Hz} \implies \mathbf{5.17}$.

### Questions 13 to 18
- **Q13**: Biot-Savart law at center of circular loop: $B = \frac{\mu_0 I}{2R}$. **Correct: (A)**.
- **Q14**: Equatorial plane is equidistant from $+q$ and $-q$, so $V = \frac{q}{4\pi\varepsilon_0 r} - \frac{q}{4\pi\varepsilon_0 r} = 0$. **Correct: (A)**.
- **Q15**: $\tau = RC = (100 \times 10^3)(10 \times 10^{-6}) = 1.0\text{ s}$. **Correct: (A)**.
- **Q16**: Resolving power of grating is $R = \lambda / \Delta\lambda = N m$. **Correct: (A)**.
- **Q17**: For Carnot cycle, $Q_C / Q_H = T_C / T_H \implies Q_C = 1000 \times (300/400) = 750\text{ J}$. **Correct: (A)**.
- **Q18**: After 2 half-lives, fraction remaining is $(1/2)^2 = 1/4$. Probability of decay is $1 - 1/4 = 3/4$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Debye-Hückel limiting law fundamentals. **Correct Options**: (A, B, C, D)
- **Q20**: Gibbs-Duhem equation and thermodynamic consistency. **Correct Options**: (A, B, C, D)
- **Q21**: Synthesis and chemical reactions of diborane. **Correct Options**: (A, B, C, D)
- **Q22**: Classification of polymers. Polythene is an addition polymer; Dacron, Nylon 6,6, and Bakelite are condensation polymers. **Correct Options**: (A, B, C)
- **Q23**: Stereochemical pathways of substitution. **Correct Options**: (A, B, C, D)
- **Q24**: Electronic configurations and properties of transition elements. **Correct Options**: (A, B, C, D)

### Questions 25 to 30
- **Q25**: $\text{PbI}_2 \rightleftharpoons \text{Pb}^{2+} + 2\text{I}^- \implies K_{\text{sp}} = 4S^3 \implies 4S^3 = 7.0 \times 10^{-9} \implies S^3 = 1.75 \times 10^{-9} \implies S \approx 1.21 \times 10^{-3}\text{ M} = 1.21\text{ mmol/L} \implies \mathbf{1.21}$.
- **Q26**: $\text{PCl}_5 \rightleftharpoons \text{PCl}_3 + \text{Cl}_2$. $K_p = \frac{\alpha^2}{1-\alpha^2} P$. $1.80 = \frac{\alpha^2}{1-\alpha^2}(3.0) \implies \frac{\alpha^2}{1-\alpha^2} = 0.60 \implies \alpha^2 = 0.60 - 0.60\alpha^2 \implies 1.60\alpha^2 = 0.60 \implies \alpha^2 = 0.375 \implies \alpha \approx 0.61 \implies \mathbf{0.61}$.
- **Q27**: $\Delta G^\circ = -n F E^\circ$. For $\text{Fe}^{3+} \to \text{Fe}$, $\Delta G^\circ_3 = \Delta G^\circ_1 + \Delta G^\circ_2 \implies -3 F E^\circ_3 = -1 F(0.77) - 2 F(-0.44) \implies 3 E^\circ_3 = 0.77 - 0.88 = -0.11 \implies E^\circ_3 = -0.037\text{ V} \approx -0.04\text{ V} \implies \mathbf{-0.04}$.
- **Q28**: For second-order reaction, $t_{1/2} = \frac{1}{k [A]_0} = \frac{1}{0.050 \times 0.20} = \frac{1}{0.010} = 100.0\text{ s} \implies \mathbf{100.00}$.
- **Q29**: Precipitation of 2 moles $\text{AgCl}$ indicates 2 ionizable $\text{Cl}^-$ ions outside the coordination sphere: $[\text{Cr}(\text{H}_2\text{O})_5\text{Cl}]\text{Cl}_2 \cdot \text{H}_2\text{O}$. Thus 5 water molecules are coordinated. $N = \mathbf{5.00}$.
- **Q30**: $\text{C}_3\text{H}_8 + 5\text{O}_2 \to 3\text{CO}_2 + 4\text{H}_2\text{O}$. $\Delta_c H^\circ = [3(-394) + 4(-286)] - [-104] = [-1182 - 1144] + 104 = -2326 + 104 = -2222\text{ kJ/mol} \implies |\Delta_c H^\circ| = \mathbf{2222.00}$.

### Questions 31 to 36
- **Q31**: Peroxide effect (Kharasch effect) causes anti-Markovnikov free radical addition of $\text{HBr}$, forming 1-bromopropane. **Correct: (A)**.
- **Q32**: $\text{SF}_6$ has 6 bond pairs and 0 lone pairs $\implies sp^3d^2$ octahedral. **Correct: (A)**.
- **Q33**: In aqueous solution, secondary aliphatic amine $(\text{CH}_3)_2\text{NH}$ is the strongest base due to combined inductive, solvation, and steric effects. **Correct: (A)**.
- **Q34**: Each carbon in graphite forms 3 $\sigma$-bonds in hexagonal planar sheets $\implies sp^2$. **Correct: (A)**.
- **Q35**: Vitamin C (ascorbic acid) is water-soluble. **Correct: (A)**.
- **Q36**: IUPAC name is 2-hydroxypropanoic acid. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Identity $\arctan\left(\frac{1-x}{1+x}\right) = \frac{\pi}{4} - \arctan x$ for $x > -1$. Thus $f(x) = \pi/4$ identically. **Correct Options**: (A, B, C, D)
- **Q38**: Properties of symmetric and skew-symmetric matrices. **Correct Options**: (A, B, C, D)
- **Q39**: Asymptotes, eccentricity, and geometric theorems of hyperbolas. **Correct Options**: (A, B, C, D)
- **Q40**: Euler Beta and Gamma function identities. **Correct Options**: (A, B, C, D)
- **Q41**: Vieta's relations for cubic equations. **Correct Options**: (A, B, C, D)
- **Q42**: Second-order linear differential equations with constant coefficients. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Parabola $y = 4 - x^2$ crosses $x$-axis at $x = \pm 2$. Area $= \int_{-2}^2 (4 - x^2)dx = [4x - x^3/3]_{-2}^2 = (8 - 8/3) - (-8 + 8/3) = 16/3 + 16/3 = 32/3 \approx 10.67 \implies \mathbf{10.67}$.
- **Q44**: $(1 + x + x^2 + x^3)^4 = \left(\frac{1-x^4}{1-x}\right)^4 = (1 - x^4)^4 (1-x)^{-4} = (1 - 4x^4 + \dots)\sum_{r=0}^\infty \binom{r+3}{3} x^r$. Coefficient of $x^4$ is $\binom{4+3}{3} - 4\binom{0+3}{3} = \binom{7}{3} - 4 = 35 - 4 = 31 \implies \mathbf{31.00}$.
- **Q45**: Vectors $\vec{a} = (1, 1, 0)$, $\vec{b} = (1, 0, 1)$. $\cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|} = \frac{1}{\sqrt{2}\sqrt{2}} = 1/2 \implies \theta = 60^\circ \implies \mathbf{60.00}$.
- **Q46**: $\det(2 A^{-1}) = 2^3 \det(A^{-1}) = 8 / \det(A) = 8 / 4 = 2.00 \implies \mathbf{2.00}$.
- **Q47**: Permutations of 5 digits taken 4 at a time: $P(5, 4) = 5 \times 4 \times 3 \times 2 = 120 \implies \mathbf{120.00}$.
- **Q48**: Circle $(x-2)^2 + (y-3)^2 = 12 + 4 + 9 = 25 \implies R = 5 \implies \mathbf{5.00}$.

### Questions 49 to 54
- **Q49**: $\frac{d}{dx}\ln(\sec x + \tan x) = \frac{\sec x \tan x + \sec^2 x}{\sec x + \tan x} = \sec x$. **Correct: (A)**.
- **Q50**: Difference of distances from centers is constant $\implies$ hyperbola. **Correct: (A)**.
- **Q51**: $|\vec{a} + \vec{b}|^2 = |\vec{a}|^2 + |\vec{b}|^2 + 2\vec{a}\cdot\vec{b} \implies 3 = 1 + 1 + 2\cos\theta \implies 2\cos\theta = 1 \implies \cos\theta = 1/2 \implies \theta = \pi/3$. **Correct: (A)**.
- **Q52**: $\int_0^{\pi/2}\sin^2 x dx = \int_0^{\pi/2}\frac{1-\cos(2x)}{2}dx = \pi/4$. **Correct: (A)**.
- **Q53**: General term $\binom{10}{r} x^{10-r} x^{-r} = \binom{10}{r} x^{10-2r}$. For constant term, $10 - 2r = 0 \implies r = 5$. Coefficient is $\binom{10}{5} = 252$. **Correct: (A)**.
- **Q54**: $P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{0.2}{0.3} = 2/3$. **Correct: (A)**.
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
| 7 | Physics | Sec 2 | Numerical | 0.35 |
| 8 | Physics | Sec 2 | Numerical | 2.00 |
| 9 | Physics | Sec 2 | Numerical | 0.24 |
| 10 | Physics | Sec 2 | Numerical | 1500.00 |
| 11 | Physics | Sec 2 | Numerical | 0.12 |
| 12 | Physics | Sec 2 | Numerical | 5.00 |
| 13 | Physics | Sec 3 | Single Correct | A |
| 14 | Physics | Sec 3 | Single Correct | B |
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
| 25 | Chemistry | Sec 2 | Numerical | -4.81 |
| 26 | Chemistry | Sec 2 | Numerical | 84.90 |
| 27 | Chemistry | Sec 2 | Numerical | 0.74 |
| 28 | Chemistry | Sec 2 | Numerical | 3.06 |
| 29 | Chemistry | Sec 2 | Numerical | 10.00 |
| 30 | Chemistry | Sec 2 | Numerical | 0.318 |
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
| 43 | Mathematics | Sec 2 | Numerical | 8.00 |
| 44 | Mathematics | Sec 2 | Numerical | 55.00 |
| 45 | Mathematics | Sec 2 | Numerical | 6.00 |
| 46 | Mathematics | Sec 2 | Numerical | 0.00 |
| 47 | Mathematics | Sec 2 | Numerical | 5.00 |
| 48 | Mathematics | Sec 2 | Numerical | 81.00 |
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
| 7 | Physics | Sec 2 | Numerical | 590.00 |
| 8 | Physics | Sec 2 | Numerical | 0.48 |
| 9 | Physics | Sec 2 | Numerical | 200.00 |
| 10 | Physics | Sec 2 | Numerical | 531.00 |
| 11 | Physics | Sec 2 | Numerical | 30.00 |
| 12 | Physics | Sec 2 | Numerical | 5.17 |
| 13 | Physics | Sec 3 | Single Correct | A |
| 14 | Physics | Sec 3 | Single Correct | A |
| 15 | Physics | Sec 3 | Single Correct | A |
| 16 | Physics | Sec 3 | Single Correct | A |
| 17 | Physics | Sec 3 | Single Correct | A |
| 18 | Physics | Sec 3 | Single Correct | A |
| 19 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 20 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 21 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 22 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C |
| 23 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 25 | Chemistry | Sec 2 | Numerical | 1.21 |
| 26 | Chemistry | Sec 2 | Numerical | 0.61 |
| 27 | Chemistry | Sec 2 | Numerical | -0.04 |
| 28 | Chemistry | Sec 2 | Numerical | 100.00 |
| 29 | Chemistry | Sec 2 | Numerical | 5.00 |
| 30 | Chemistry | Sec 2 | Numerical | 2222.00 |
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
| 43 | Mathematics | Sec 2 | Numerical | 10.67 |
| 44 | Mathematics | Sec 2 | Numerical | 31.00 |
| 45 | Mathematics | Sec 2 | Numerical | 60.00 |
| 46 | Mathematics | Sec 2 | Numerical | 2.00 |
| 47 | Mathematics | Sec 2 | Numerical | 120.00 |
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
    generate_madras_11_to_15()

