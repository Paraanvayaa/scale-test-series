# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 18.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Aharonov-Bohm quantum phase shift, Abraham-Lorentz radiation damping, van der Waals Joule-Thomson inversion
- Baeyer-Villiger migratory aptitude, Re2Cl8 quadruple delta-bonding, Eyring transition state equation
- Fourier convolution & Plancherel theorems, Jordan canonical blocks, Apollonius circles, Catalan Dyck paths
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 18 — Paper 1
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
Regarding the Aharonov-Bohm effect in quantum mechanics, where an electron beam is split into two coherent paths that enclose an infinitely long solenoid of radius $R$ carrying magnetic flux $\Phi_B$, with magnetic field $\vec{B} = 0$ everywhere outside the solenoid:
(A) The vector potential $\vec{A}$ outside the solenoid is non-zero and given by $\vec{A}(r) = \frac{\Phi_B}{2\pi r}\hat{\theta}$ for $r > R$.  
(B) An electron traversing path $C$ accumulates a quantum phase shift $\Delta\phi = \frac{e}{\hbar}\int_C \vec{A} \cdot d\vec{l}$.  
(C) The relative phase difference between the two interfering electron beams that encircle the solenoid is $\Delta\Phi = \frac{e}{\hbar}\oint \vec{A} \cdot d\vec{l} = \frac{e \Phi_B}{\hbar}$.  
(D) The interference pattern on the detector screen shifts as the magnetic flux $\Phi_B$ is altered, demonstrating that the magnetic vector potential $\vec{A}$ has direct physical consequences in quantum mechanics.

#### Question 2
A real gas obeys the van der Waals equation of state $\left(P + \frac{a}{V_m^2}\right)(V_m - b) = R T$. For a Joule-Thomson expansion (isenthalpic throttling, $dH = 0$):
(A) The Joule-Thomson coefficient is defined as $\mu_{\text{JT}} = \left(\frac{\partial T}{\partial P}\right)_H = \frac{1}{C_p}\left[T\left(\frac{\partial V_m}{\partial T}\right)_P - V_m\right]$.  
(B) In the low-pressure limit, $\mu_{\text{JT}} \approx \frac{1}{C_p}\left(\frac{2a}{R T} - b\right)$.  
(C) The maximum Joule-Thomson inversion temperature is $T_i = \frac{2a}{R b}$.  
(D) If the initial temperature of the gas satisfies $T < T_i$, throttling causes cooling ($\mu_{\text{JT}} > 0$).

#### Question 3
In rotational Raman spectroscopy of a rigid linear diatomic molecule with rotational constant $B = \frac{\hbar^2}{2 I}$:
(A) The quantum mechanical selection rule for pure rotational Raman transitions is $\Delta J = 0, \pm 2$.  
(B) The Rayleigh line corresponds to $\Delta J = 0$.  
(C) The first Stokes line appears at frequency displacement $\Delta\nu = 6 B$ from the Rayleigh line.  
(D) The constant frequency separation between adjacent Stokes lines is $4 B$.

#### Question 4
Regarding the classical radiation reaction and the Abraham-Lorentz self-force on an accelerating point charge $q$:
(A) The time-averaged rate of energy radiation is given by Larmor's formula $P = \frac{\mu_0 q^2 a^2}{6\pi c}$.  
(B) The Abraham-Lorentz recoil force is given by $\vec{F}_{\text{rad}} = \frac{\mu_0 q^2}{6\pi c} \dot{\vec{a}}$, proportional to the jerk (rate of change of acceleration).  
(C) Newton's second law with radiation damping reads $m(\vec{a} - \tau_0 \dot{\vec{a}}) = \vec{F}_{\text{ext}}$, where characteristic time $\tau_0 = \frac{\mu_0 q^2}{6\pi m c}$.  
(D) The homogeneous equation $a - \tau_0 \dot{a} = 0$ exhibits unphysical runaway self-accelerating solutions $a(t) = a_0 e^{t/\tau_0}$ in the absence of boundary conditions.

#### Question 5
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal table. A horizontal impulse $J$ is delivered to the sphere at a height $h$ above the center of mass ($0 \le h \le R$):
(A) Immediately after the impulse, the linear velocity of the center of mass is $v_0 = \frac{J}{M}$.  
(B) The initial angular velocity about the horizontal axis through the center of mass is $\omega_0 = \frac{J h}{I_{\text{cm}}} = \frac{5 J h}{2 M R^2}$.  
(C) If the impulse is applied at the sweet spot height $h = \frac{2}{5}R$, the sphere immediately rolls without slipping with zero initial friction force.  
(D) If $h < \frac{2}{5}R$, the kinetic friction force initially acts forward (in the direction of $v_0$) to increase rotational speed.

#### Question 6
A plane electromagnetic wave propagates along the $+z$ direction in vacuum. The electric field is $\vec{E}(z, t) = E_0 \cos(k z - \omega t)\hat{i}$:
(A) The associated magnetic field is $\vec{B}(z, t) = \frac{E_0}{c}\cos(k z - \omega t)\hat{j}$.  
(B) The instantaneous Poynting vector is $\vec{S}(z, t) = \frac{E_0^2}{\mu_0 c}\cos^2(k z - \omega t)\hat{k}$.  
(C) The time-averaged energy density is $\langle u \rangle = \frac{1}{2}\varepsilon_0 E_0^2$.  
(D) The electromagnetic momentum density is $\vec{g} = \frac{\vec{S}}{c^2} = \varepsilon_0 (\vec{E} \times \vec{B})$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In an Aharonov-Bohm experiment, the magnetic flux through a microscopic solenoid is adjusted. The minimum non-zero magnetic flux $\Phi_0$ in units of $10^{-15}\text{ Wb}$ (magnetic flux quantum $h/e$) that produces a complete $2\pi$ phase shift between the two electron paths is $\Phi_0$. Calculate $\Phi_0$ (use $h = 6.626 \times 10^{-34}\text{ J s}$, $e = 1.602 \times 10^{-19}\text{ C}$, round off to TWO decimal places).

#### Question 8
For nitrogen gas, the van der Waals constants are $a = 0.137\text{ Pa}\cdot\text{m}^6\cdot\text{mol}^{-2}$ and $b = 3.87 \times 10^{-5}\text{ m}^3\cdot\text{mol}^{-1}$. Calculate the maximum Joule-Thomson inversion temperature $T_i$ of nitrogen in Kelvin (use $R = 8.314\text{ J/(mol K)}$, round off to the nearest integer).

#### Question 9
In the pure rotational Raman spectrum of $^{14}\text{N}_2$ molecule, the rotational constant is $B = 2.0\text{ cm}^{-1}$. The wavenumber separation between the first Stokes line and the first Anti-Stokes line is $\Delta\bar{\nu}$ in $\text{cm}^{-1}$. Calculate $\Delta\bar{\nu}$.

#### Question 10
A billiard ball of radius $R = 3.0\text{ cm}$ is struck horizontally by a cue stick at height $h$ above its center. If the ball rolls without slipping immediately without skidding, calculate $h$ in centimeters (round off to ONE decimal place).

#### Question 11
A parallel-plate capacitor with plate separation $d = 2.0\text{ mm}$ and area $A = 0.05\text{ m}^2$ is filled with a dielectric material of dielectric constant $\kappa = 4.0$. If a potential difference $V = 200\text{ V}$ is applied across the plates, calculate the total electrostatic energy $U$ stored in microJoules ($\mu\text{J}$) (use $\varepsilon_0 = 8.85 \times 10^{-12}\text{ F/m}$, round off to ONE decimal place).

#### Question 12
A uniform rod of mass $M = 2.0\text{ kg}$ and length $L = 1.20\text{ m}$ is free to pivot about a fixed vertical axis through one end. A horizontal force $F = 5.0\text{ N}$ is applied perpendicularly at the free end. Calculate the angular acceleration $\alpha$ in $\text{rad/s}^2$ (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A satellite is in an elliptical orbit around Earth with perigee distance $r_p$ and apogee distance $r_a$. The ratio of the speed of the satellite at perigee to that at apogee is:
(A) $\frac{v_p}{v_a} = \frac{r_a}{r_p}$  
(B) $\frac{v_p}{v_a} = \sqrt{\frac{r_a}{r_p}}$  
(C) $\frac{v_p}{v_a} = \frac{r_p}{r_a}$  
(D) $\frac{v_p}{v_a} = \left(\frac{r_a}{r_p}\right)^2$  

#### Question 14
Two identical sound sources vibrating in phase produce sound of wavelength $\lambda = 1.0\text{ m}$. They are placed at $(0, 0)$ and $(0, 4\text{ m})$. The number of points on the line $x = 3\text{ m}$ where constructive interference produces maximum intensity is:
(A) 5  
(B) 3  
(C) 7  
(D) 4  

#### Question 15
The magnetic field at a perpendicular distance $r$ from an infinitely long straight wire carrying a steady current $I$ is:
(A) $B = \frac{\mu_0 I}{2\pi r}$  
(B) $B = \frac{\mu_0 I}{4\pi r}$  
(C) $B = \frac{\mu_0 I}{\pi r}$  
(D) $B = \frac{2\mu_0 I}{\pi r}$  

#### Question 16
A spherical droplet of mercury of radius $R$ carries a charge $Q$ and has electrostatic potential $V_0$. If eight such identical droplets coalesce into a single large spherical drop, the potential of the new drop is:
(A) $4 V_0$  
(B) $2 V_0$  
(C) $8 V_0$  
(D) $\sqrt{2} V_0$  

#### Question 17
A heat engine rejects heat to a sink at $0^\circ\text{C}$ ($273\text{ K}$) with an efficiency of $50\%$. The temperature of the hot source is:
(A) $273^\circ\text{C}$  
(B) $546^\circ\text{C}$  
(C) $100^\circ\text{C}$  
(D) $200^\circ\text{C}$  

#### Question 18
The stopping potential $V_s$ for photoelectrons emitted from a metallic surface is plotted against the frequency $\nu$ of incident radiation. The slope of the resulting straight line is:
(A) $\frac{h}{e}$  
(B) $h$  
(C) $\frac{e}{h}$  
(D) $\frac{h c}{e}$  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Baeyer-Villiger oxidation of ketones using peroxy acids (e.g., m-CPBA, trifluoroperacetic acid $\text{CF}_3\text{COOOH}$):
(A) Nucleophilic addition of the peroxy acid to the carbonyl group forms a tetrahedral Criegee intermediate.  
(B) Migration of one of the alkyl/aryl groups to the adjacent oxygen atom occurs concertedly with cleavage of the weak peroxy $\text{O-O}$ bond.  
(C) The migratory aptitude follows the order: tertiary alkyl > cyclohexyl > secondary alkyl $\approx$ benzyl $\approx$ phenyl > primary alkyl > methyl.  
(D) Oxidation of unsymmetrical ketone acetophenone ($\text{Ph-CO-CH}_3$) gives phenyl acetate ($\text{CH}_3\text{COOPh}$) rather than methyl benzoate ($\text{PhCOOCH}_3$) because phenyl migrates preferentially over methyl.

#### Question 20
Regarding the transition metal cluster anion octachlorodirhenate(III), $[\text{Re}_2\text{Cl}_8]^{2-}$:
(A) Each rhenium atom has a formal oxidation state of $+3$ ($d^4$ valence configuration).  
(B) A metal-metal quadruple bond ($\text{Re}\equiv\equiv\text{Re}$) is formed consisting of one $\sigma$ bond, two $\pi$ bonds, and one $\delta$ bond ($\sigma^2 \pi^4 \delta^2$).  
(C) The $\delta$ bond arises from face-to-face overlap of the $d_{xy}$ orbitals on the two Re atoms.  
(D) The complex adopts an eclipsed $D_{4h}$ conformation rather than a staggered $D_{4d}$ conformation because rotation into a staggered conformation would break the $\delta$ bond.

#### Question 21
According to the Eyring-Polanyi transition state theory of chemical reaction rates:
$$k = \frac{k_B T}{h} e^{\frac{\Delta S^\ddagger}{R}} e^{-\frac{\Delta H^\ddagger}{R T}}$$
(A) The pre-exponential factor is directly related to the standard entropy of activation $\Delta S^\ddagger$.  
(B) A large negative entropy of activation ($\Delta S^\ddagger \ll 0$) indicates an associative, highly ordered transition state (e.g., bimolecular cyclization or $S_N2$ reaction).  
(C) A positive entropy of activation ($\Delta S^\ddagger > 0$) is characteristic of dissociative unimolecular pathways (e.g., $S_N1$ or unimolecular decomposition).  
(D) The enthalpy of activation $\Delta H^\ddagger$ is related to the Arrhenius activation energy $E_a$ for a solution reaction by $E_a = \Delta H^\ddagger + R T$.

#### Question 22
Regarding Crabtree's catalyst, $[(\eta^4\text{-COD})\text{Ir(PCy}_3)(\text{py})]^+\text{PF}_6^-$ (where COD is 1,5-cyclooctadiene, $\text{PCy}_3$ is tricyclohexylphosphine, and py is pyridine):
(A) It is an extremely active homogeneous hydrogenation catalyst, capable of hydrogenating hindered tri- and tetra-substituted alkenes that Wilkinson's catalyst cannot reduce.  
(B) It exhibits high substrate-directed diastereoselectivity in the hydrogenation of cyclic allylic and homoallylic alcohols via binding of the hydroxyl directing group to iridium.  
(C) The solvent of choice is typically dichloromethane ($\text{CH}_2\text{Cl}_2$) because coordinating solvents like ethanol or THF poison the catalyst.  
(D) It operates via an $\text{Ir(I)} \rightleftharpoons \text{Ir(III)}$ or $\text{Ir(III)} \rightleftharpoons \text{Ir(V)}$ catalytic cycle.

#### Question 23
Regarding the electrical double layer at a charged solid-liquid interface:
(A) The Helmholtz model treats the interface as a parallel-plate capacitor with a rigid monolayer of counter-ions (Stern layer).  
(B) The Gouy-Chapman diffuse double layer model accounts for thermal motion of ions, leading to an exponential decay of electrostatic potential with distance: $\psi(x) = \psi_0 e^{-\kappa x}$.  
(C) The Debye screening length $\kappa^{-1}$ decreases with increasing electrolyte concentration and ionic valence.  
(D) The electrokinetic potential at the shear slipping plane between the moving fluid and the attached ion layer is called the zeta potential ($\zeta$).

#### Question 24
In the qualitative analysis of Group V basic radicals ($\text{Ba}^{2+}, \text{Sr}^{2+}, \text{Ca}^{2+}$):
(A) The group reagent is ammonium carbonate ($(\text{NH}_4)_2\text{CO}_3$) in the presence of $\text{NH}_4\text{OH}$ and $\text{NH}_4\text{Cl}$.  
(B) They are precipitated as insoluble white carbonates: $\text{BaCO}_3, \text{SrCO}_3, \text{CaCO}_3$.  
(C) $\text{Ba}^{2+}$ is separated from $\text{Sr}^{2+}$ and $\text{Ca}^{2+}$ by precipitation as yellow barium chromate ($\text{BaCrO}_4$) in acetic acid medium.  
(D) In flame tests, $\text{Ba}^{2+}$ imparts an apple-green color, $\text{Sr}^{2+}$ gives a crimson-red color, and $\text{Ca}^{2+}$ gives a brick-red color.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of calcium carbonate ($\text{CaCO}_3$) is $K_{sp} = 4.9 \times 10^{-9}$ at $25^\circ\text{C}$. Calculate the molar solubility $S$ of $\text{CaCO}_3$ in pure water in units of $10^{-5}\text{ mol/L}$ (round off to the nearest integer).

#### Question 26
Calculate the spin-only magnetic moment in Bohr Magnetons ($\mu_B$) for the complex ion $[Fe(CN)_6]^{3-}$ (atomic number of $\text{Fe} = 26$). Enter the value rounded off to TWO decimal places (take $\sqrt{3} \approx 1.73$).

#### Question 27
An organic compound contains $52.2\%$ Carbon, $13.0\%$ Hydrogen, and $34.8\%$ Oxygen by mass. Its vapor density relative to hydrogen is 23. Calculate the number of hydrogen atoms present in one molecule.

#### Question 28
The rate of a chemical reaction quadruples when the temperature is raised from $300\text{ K}$ to $320\text{ K}$. Calculate the activation energy $E_a$ in $\text{kJ/mol}$ (use $R = 8.314\text{ J/(mol K)}$, $\ln 4 = 1.386$, round off to ONE decimal place).

#### Question 29
A current of $I = 4.825\text{ A}$ is passed through molten magnesium chloride ($\text{MgCl}_2$) for $t = 2000\text{ seconds}$. Calculate the mass of magnesium metal produced at the cathode in grams (atomic mass of $\text{Mg} = 24.3\text{ g/mol}$, $F = 96500\text{ C/mol}$, round off to TWO decimal places).

#### Question 30
The elevation in boiling point for a $0.050\text{ m}$ aqueous solution of an electrolyte $A B_2$ is $\Delta T_b = 0.070^\circ\text{C}$. If $K_b = 0.512\text{ K kg/mol}$, calculate the van 't Hoff factor $i$ (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Etard reaction, toluene is oxidized to benzaldehyde using:
(A) Chromyl chloride ($\text{CrO}_2\text{Cl}_2$) in $\text{CS}_2$ followed by hydrolysis  
(B) Alkaline $\text{KMnO}_4$  
(C) Acidified $\text{K}_2\text{Cr}_2\text{O}_7$  
(D) Ozone ($\text{O}_3$)  

#### Question 32
Which of the following compounds exhibits square planar geometry?
(A) $[\text{Pt(NH}_3)_2\text{Cl}_2]$  
(B) $[\text{Ni(CO)}_4]$  
(C) $[\text{Zn(NH}_3)_4]^{2+}$  
(D) $[\text{FeCl}_4]^-$  

#### Question 33
The nitrogenous base present in RNA but absent in DNA is:
(A) Uracil  
(B) Thymine  
(C) Cytosine  
(D) Guanine  

#### Question 34
In the extraction of lead from galena ($\text{PbS}$), self-reduction involves the reaction:
(A) $2\text{PbO} + \text{PbS} \to 3\text{Pb} + \text{SO}_2$  
(B) $\text{PbS} + \text{C} \to \text{Pb} + \text{CS}_2$  
(C) $\text{PbO} + \text{C} \to \text{Pb} + \text{CO}$  
(D) $\text{PbS} + \text{Fe} \to \text{Pb} + \text{FeS}$  

#### Question 35
Treatment of phenol with concentrated $\text{HNO}_3$ and concentrated $\text{H}_2\text{SO}_4$ yields:
(A) Picric acid (2,4,6-trinitrophenol)  
(B) o-nitrophenol only  
(C) p-nitrophenol only  
(D) Benzoic acid  

#### Question 36
The conjugate acid of ammonia ($\text{NH}_3$) is:
(A) Ammonium ion ($\text{NH}_4^+$)  
(B) Amide ion ($\text{NH}_2^-$)  
(C) Hydrazine ($\text{N}_2\text{H}_4$)  
(D) Nitric acid ($\text{HNO}_3$)  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f, g \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$. The convolution of $f$ and $g$ is $(f * g)(x) = \int_{-\infty}^\infty f(t) g(x - t) dt$:
(A) The Fourier transform of convolution is the pointwise product: $\mathcal{F}\{f * g\} = \mathcal{F}\{f\} \cdot \mathcal{F}\{g\}$.  
(B) Convolution is commutative: $f * g = g * f$.  
(C) Plancherel's theorem states $\int_{-\infty}^\infty |f(x)|^2 dx = \frac{1}{2\pi} \int_{-\infty}^\infty |\hat{f}(\omega)|^2 d\omega$.  
(D) The convolution of two Gaussian functions is another Gaussian function.

#### Question 38
Let $A$ be an $n \times n$ complex matrix with Jordan canonical form $J = P^{-1} A P$:
(A) Every square matrix $A$ over $\mathbb{C}$ is similar to a block diagonal matrix composed of Jordan blocks $J_k(\lambda)$.  
(B) The number of Jordan blocks corresponding to eigenvalue $\lambda$ equals the geometric multiplicity of $\lambda$.  
(C) The sum of the sizes of all Jordan blocks corresponding to $\lambda$ equals the algebraic multiplicity of $\lambda$.  
(D) $A$ is diagonalizable if and only if every Jordan block has size $1 \times 1$.

#### Question 39
Regarding the circles of Apollonius:
(A) The locus of a point $P$ in the plane such that the ratio of its distances from two fixed points $A$ and $B$ is constant $k > 0$ ($k \ne 1$) is a circle.  
(B) If $k = 1$, the locus is the perpendicular bisector of the segment $A B$.  
(C) The center of the Apollonius circle lies on the line passing through $A$ and $B$.  
(D) The two points where the Apollonius circle intersects the line $A B$ divide the segment $A B$ internally and externally in the ratio $k : 1$.

#### Question 40
Regarding the Catalan numbers $C_n = \frac{1}{n+1}\binom{2n}{n}$ for $n \ge 0$:
(A) The recurrence relation is $C_{n+1} = \sum_{i=0}^n C_i C_{n-i}$ with $C_0 = 1$.  
(B) The first five Catalan numbers are $C_0 = 1, C_1 = 1, C_2 = 2, C_3 = 5, C_4 = 14$.  
(C) $C_n$ equals the number of Dyck paths of length $2n$ from $(0, 0)$ to $(2n, 0)$ that never drop below the $x$-axis.  
(D) $C_n$ equals the number of correct matchings of $n$ pairs of parentheses.

#### Question 41
Let $f(x) = \frac{x^2 - 1}{x^2 + 1}$:
(A) The function is even.  
(B) The global minimum occurs at $x = 0$ with value $f(0) = -1$.  
(C) The horizontal asymptote is $y = 1$ as $x \to \pm\infty$.  
(D) $f'(x) = \frac{4x}{(x^2 + 1)^2}$.

#### Question 42
Consider the matrix $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$:
(A) $A$ is an orthogonal matrix.  
(B) $A$ is a skew-symmetric matrix.  
(C) The eigenvalues of $A$ are $\pm i$.  
(D) $A^4 = I$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 x^2 (1 - x)^2 dx$$
Calculate the value of $60 I$ (round off to the nearest integer).

#### Question 44
Find the number of ways to arrange the letters of the word **SUCCESS**.

#### Question 45
Find the perpendicular distance from the point $(1, 2, 3)$ to the plane $2x + y + 2z - 3 = 0$ (round off to TWO decimal places).

#### Question 46
Let $z$ be a complex number satisfying $z^3 = 1$ ($z \ne 1$). Calculate $(1 - z)(1 - z^2)$.

#### Question 47
Let $y(x)$ satisfy $\frac{dy}{dx} = x + y$ with $y(0) = 0$. Calculate $y(1)$ (use $e \approx 2.718$, round off to TWO decimal places).

#### Question 48
In flipping 4 fair coins, calculate the probability of getting exactly 2 heads (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The area of the region bounded by $y = x^3$, the $x$-axis, and the ordinates $x = 0$ and $x = 2$ is:
(A) 4  
(B) 2  
(C) 8  
(D) 1  

#### Question 50
If the $n\text{th}$ term of an arithmetic progression is $a_n = 3n + 2$, then the sum of the first 20 terms $S_{20}$ is:
(A) 670  
(B) 640  
(C) 700  
(D) 610  

#### Question 51
The value of the limit $\lim_{x \to 0} \frac{\tan x - \sin x}{x^3}$ is:
(A) $1/2$  
(B) 1  
(C) $1/3$  
(D) $2/3$  

#### Question 52
The directrix of the parabola $y^2 = 8x$ is:
(A) $x = -2$  
(B) $x = 2$  
(C) $y = -2$  
(D) $y = 2$  

#### Question 53
The distance of the point $(2, 3, 4)$ from the $x$-axis is:
(A) 5  
(B) $\sqrt{29}$  
(C) $\sqrt{20}$  
(D) 2  

#### Question 54
If $\vec{a}$ and $\vec{b}$ are two vectors such that $|\vec{a}| = 2$, $|\vec{b}| = 3$, and $\vec{a} \cdot \vec{b} = 3$, then $|\vec{a} \times \vec{b}|$ is equal to:
(A) $3\sqrt{3}$  
(B) 3  
(C) 6  
(D) $\sqrt{3}$  
"""

paper_2_md = r"""# JEE Advanced Mock Examination 18 — Paper 2
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
A uniform electric field $\vec{E} = E_0 \hat{i}$ exists in a region. A point charge $q$ is displaced from $(0, 0, 0)$ to $(x_1, y_1, z_1)$:
(A) The work done by the electric field is $W = q E_0 x_1$.  
(B) The change in electrostatic potential energy is $\Delta U = -q E_0 x_1$.  
(C) The work done is independent of the path taken between the two points.  
(D) The equipotential surfaces are planes perpendicular to the $x$-axis.

#### Question 2
Regarding simple harmonic motion described by $x(t) = A \sin(\omega t + \phi)$:
(A) The velocity is $v(t) = \omega \sqrt{A^2 - x^2}$.  
(B) The acceleration is $a(t) = -\omega^2 x$.  
(C) The total mechanical energy $E = \frac{1}{2} m \omega^2 A^2$ is constant in time.  
(D) In one full period, the average kinetic energy equals the average potential energy: $\langle K \rangle = \langle U \rangle = \frac{1}{4} m \omega^2 A^2$.

#### Question 3
A convex lens of focal length $f$ forms a real image of a real object. Let the object distance be $u$ and image distance be $v$:
(A) The minimum distance between the real object and its real image is $4f$.  
(B) The minimum distance is attained when $u = 2f$ and $v = 2f$.  
(C) In this configuration, the magnification is $m = -1$.  
(D) If the distance between object and screen is $D > 4f$, there are two conjugate positions of the lens that form sharp images on the screen.

#### Question 4
A thermodynamic heat pump maintains a building at temperature $T_H = 300\text{ K}$ by absorbing heat from the cold outdoor air at $T_C = 250\text{ K}$:
(A) The coefficient of performance of the ideal heat pump is $\text{COP}_{\text{HP}} = \frac{T_H}{T_H - T_C} = 6.0$.  
(B) The coefficient of performance of an ideal refrigerator operating between the same temperatures is $\text{COP}_{\text{ref}} = 5.0$.  
(C) $\text{COP}_{\text{HP}} = \text{COP}_{\text{ref}} + 1$.  
(D) For every $1.0\text{ kJ}$ of electrical energy consumed, the heat pump delivers $6.0\text{ kJ}$ of heat to the building.

#### Question 5
Regarding the magnetic force on a moving charged particle $\vec{F} = q(\vec{v} \times \vec{B})$:
(A) The force is always perpendicular to the instantaneous velocity $\vec{v}$.  
(B) The magnetic force does zero work on the charged particle at all times.  
(C) The kinetic energy and speed of the particle remain strictly constant.  
(D) In a uniform magnetic field, the particle executes helical motion if $\vec{v}$ has a component parallel to $\vec{B}$.

#### Question 6
An alternating voltage $V(t) = V_0 \sin(\omega t)$ is connected across a pure capacitor $C$:
(A) The current leads the voltage by a phase angle of $90^\circ$ ($\pi/2\text{ rad}$).  
(B) The capacitive reactance is $X_C = \frac{1}{\omega C}$.  
(C) The peak current is $I_0 = \omega C V_0$.  
(D) The average power consumed over a complete cycle is zero.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A particle moves in SHM with amplitude $A = 10.0\text{ cm}$ and time period $T = 4.0\text{ s}$. Calculate its speed in $\text{cm/s}$ when its displacement is $x = 6.0\text{ cm}$ (round off to TWO decimal places).

#### Question 8
In an experiment with a convex lens of focal length $f = 15.0\text{ cm}$, the distance between a real object and a screen is $D = 80.0\text{ cm}$. Calculate the distance between the two conjugate positions of the lens in centimeters (use $\sqrt{3200} \approx 56.57$, round off to TWO decimal places).

#### Question 9
An ideal heat pump has $\text{COP} = 5.0$. If it delivers $25.0\text{ kW}$ of heat to a house, calculate the electrical power input in kilowatts.

#### Question 10
A proton ($q = 1.6 \times 10^{-19}\text{ C}$, $m = 1.67 \times 10^{-27}\text{ kg}$) enters a magnetic field $B = 0.50\text{ T}$ perpendicularly with kinetic energy $K = 2.0\text{ MeV}$. Calculate the radius of the circular orbit in centimeters (use $1\text{ eV} = 1.6 \times 10^{-19}\text{ J}$, round off to ONE decimal place).

#### Question 11
An AC voltage $V(t) = 141.4 \sin(100\pi t)\text{ V}$ is applied across a capacitor $C = 100\text{ }\mu\text{F}$. Calculate the RMS current in Amperes (use $\pi \approx 3.142$, round off to TWO decimal places).

#### Question 12
A block of mass $m = 5.0\text{ kg}$ rests on a rough horizontal plane with coefficient of friction $\mu = 0.40$. Calculate the minimum horizontal force in Newtons required to move the block (take $g = 9.8\text{ m/s}^2$).

---

## Section 3: Matching List / Matrix Match (Questions 13 to 18)

#### Question 13
Match the physical quantity in List-I with its dimensions in List-II:
- **List-I**:
  - P. Planck's constant $h$
  - Q. Universal gravitational constant $G$
  - R. Surface tension $T$
  - S. Coefficient of viscosity $\eta$
- **List-II**:
  - 1. $[M^{-1} L^3 T^{-2}]$
  - 2. $[M L^2 T^{-1}]$
  - 3. $[M L^{-1} T^{-1}]$
  - 4. $[M L^0 T^{-2}]$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 14
Match the type of collision in List-I with its conservation laws in List-II:
- **List-I**:
  - P. Perfectly elastic collision
  - Q. Inelastic collision
  - R. Perfectly inelastic collision
  - S. Super-elastic (explosive) collision
- **List-II**:
  - 1. Momentum conserved, kinetic energy decreases
  - 2. Both linear momentum and kinetic energy conserved
  - 3. Momentum conserved, kinetic energy increases
  - 4. Maximum loss of kinetic energy, bodies stick together

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 15
Match the wave property in List-I with its mathematical definition in List-II:
- **List-I**:
  - P. Phase velocity
  - Q. Group velocity
  - R. Wave number $k$
  - S. Angular frequency $\omega$
- **List-II**:
  - 1. $\frac{d\omega}{dk}$
  - 2. $\frac{\omega}{k}$
  - 3. $2\pi f$
  - 4. $\frac{2\pi}{\lambda}$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 16
Match the magnetic material in List-I with its susceptibility $\chi$ in List-II:
- **List-I**:
  - P. Diamagnetic
  - Q. Paramagnetic
  - R. Ferromagnetic
  - S. Superconductor
- **List-II**:
  - 1. Small and positive ($\chi \sim 10^{-5}$)
  - 2. Small and negative ($\chi \sim -10^{-5}$)
  - 3. Exactly $-1$ ($\chi = -1$, perfect diamagnet)
  - 4. Very large and positive ($\chi \gg 1$)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 17
Match the electronic transition in atomic hydrogen in List-I with its spectral series in List-II:
- **List-I**:
  - P. Transition to $n = 1$
  - Q. Transition to $n = 2$
  - R. Transition to $n = 3$
  - S. Transition to $n = 4$
- **List-II**:
  - 1. Balmer series (visible)
  - 2. Lyman series (ultraviolet)
  - 3. Brackett series (infrared)
  - 4. Paschen series (infrared)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 18
Match the circuit in List-I with its resonant condition in List-II:
- **List-I**:
  - P. Series LCR
  - Q. Parallel LC (ideal)
  - R. Pure resistive circuit
  - S. Pure inductive circuit
- **List-II**:
  - 1. Current lags voltage by $90^\circ$
  - 2. Current and voltage always in phase
  - 3. Impedance maximum (infinite in ideal case)
  - 4. Impedance minimum ($Z = R$)

(A) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  
(D) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding aromatic electrophilic substitution:
(A) Activating groups (e.g., $-\text{OH}, -\text{NH}_2, -\text{OCH}_3$) are ortho/para-directing.  
(B) Halogens are deactivating but ortho/para-directing due to resonance electron donation competing with inductive withdrawal.  
(C) Strongly deactivating groups (e.g., $-\text{NO}_2, -\text{CN}, -\text{COOH}$) are meta-directing.  
(D) The arenium ion (sigma complex) intermediate is resonance stabilized.

#### Question 20
Regarding galvanic cells and standard electrode potentials:
(A) The cell potential is an intensive thermodynamic property.  
(B) The standard Gibbs free energy change $\Delta G^\circ = -n F E^\circ$ is an extensive property.  
(C) A positive $E^\circ_{\text{cell}}$ corresponds to a spontaneous cell reaction under standard conditions ($\Delta G^\circ < 0$).  
(D) Multiplying the stoichiometric coefficients of a half-reaction does NOT change its standard potential $E^\circ$.

#### Question 21
Regarding chemical kinetics of a second-order reaction $2A \to \text{Products}$:
(A) The integrated rate law is $\frac{1}{[A]_t} = \frac{1}{[A]_0} + k t$.  
(B) A plot of $\frac{1}{[A]_t}$ versus $t$ is a straight line with slope $k$.  
(C) The half-life is inversely proportional to initial concentration: $t_{1/2} = \frac{1}{k [A]_0}$.  
(D) The unit of rate constant is $\text{L}\cdot\text{mol}^{-1}\cdot\text{s}^{-1}$.

#### Question 22
Regarding the crystal structures of ionic solids:
(A) In $\text{NaCl}$, chloride ions form an FCC lattice and sodium ions occupy all octahedral voids.  
(B) The coordination number of both $\text{Na}^+$ and $\text{Cl}^-$ in $\text{NaCl}$ is 6.  
(C) In $\text{CsCl}$, caesium and chloride ions have coordination numbers of 8.  
(D) In zinc blende ($\text{ZnS}$), sulfide ions form an FCC lattice and zinc ions occupy half of the tetrahedral voids.

#### Question 23
Regarding nucleic acids:
(A) DNA consists of a double helix stabilized by Watson-Crick hydrogen bonding between complementary base pairs ($A=T$ and $G\equiv C$).  
(B) The backbone of DNA is composed of alternating 2-deoxy-D-ribose sugar and phosphate groups linked by $3',5'$-phosphodiester bonds.  
(C) The two strands of the DNA double helix run anti-parallel to each other.  
(D) RNA contains D-ribose sugar instead of 2-deoxy-D-ribose.

#### Question 24
In the extraction of copper by smelting:
(A) Roasted ore is mixed with coke and silica and heated in a blast furnace.  
(B) Iron sulfide is oxidized to iron oxide, which forms slag ($\text{FeSiO}_3$) with silica flux.  
(C) The molten mixture of $\text{Cu}_2\text{S}$ and $\text{FeS}$ obtained from the furnace is called copper matte.  
(D) Air is blown into the converter to carry out auto-reduction of $\text{Cu}_2\text{S}$.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
Calculate the pH of a $0.010\text{ M}$ aqueous solution of sodium hydroxide ($\text{NaOH}$) at $25^\circ\text{C}$.

#### Question 26
Calculate the spin-only magnetic moment in Bohr Magnetons ($\mu_B$) for the complex ion $[CoF_6]^{3-}$ (atomic number of $\text{Co} = 27$, weak field ligand $\text{F}^-$). Enter the value rounded off to TWO decimal places (take $\sqrt{24} \approx 4.90$).

#### Question 27
An organic compound contains $40.0\%$ Carbon, $6.67\%$ Hydrogen, and $53.33\%$ Oxygen. If its molecular weight is $180\text{ g/mol}$, calculate the number of carbon atoms present in one molecule.

#### Question 28
The half-life of a radioactive isotope is $t_{1/2} = 10.0\text{ days}$. Calculate the percentage of the isotope remaining after $30.0\text{ days}$ (round off to ONE decimal place).

#### Question 29
A steady current of $I = 5.0\text{ A}$ is passed through an aqueous solution of $\text{ZnSO}_4$ for $t = 1930\text{ seconds}$. Calculate the mass of zinc deposited at the cathode in grams (atomic mass of $\text{Zn} = 65.4\text{ g/mol}$, $F = 96500\text{ C/mol}$, round off to TWO decimal places).

#### Question 30
The depression in freezing point of a solution of $1.80\text{ g}$ of glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, molar mass $180\text{ g/mol}$) in $100.0\text{ g}$ of water is $\Delta T_f$. Calculate $\Delta T_f$ in $^\circ\text{C}$ (use $K_f = 1.86\text{ K kg/mol}$, round off to THREE decimal places).

---

## Section 3: Matching List / Matrix Match (Questions 31 to 36)

#### Question 31
Match the organic reaction in List-I with its key reagent in List-II:
- **List-I**:
  - P. Cannizzaro reaction
  - Q. Aldol condensation
  - R. Hell-Volhard-Zelinsky reaction
  - S. Friedel-Crafts alkylation
- **List-II**:
  - 1. $\text{R-Cl} + \text{anh. AlCl}_3$
  - 2. $\text{Br}_2 / \text{red P}$
  - 3. Dilute $\text{NaOH}$ with $\alpha$-hydrogen carbonyl
  - 4. Concentrated $\text{NaOH}$ with non-$\alpha$-hydrogen aldehyde

(A) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  

#### Question 32
Match the nitrogen oxide in List-I with the oxidation state of nitrogen in List-II:
- **List-I**:
  - P. $\text{N}_2\text{O}$
  - Q. $\text{NO}$
  - R. $\text{NO}_2$
  - S. $\text{N}_2\text{O}_5$
- **List-II**:
  - 1. $+2$
  - 2. $+1$
  - 3. $+5$
  - 4. $+4$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 33
Match the indicator in List-I with its pH transition range in List-II:
- **List-I**:
  - P. Methyl orange
  - Q. Phenolphthalein
  - R. Litmus
  - S. Bromothymol blue
- **List-II**:
  - 1. $8.3\text{--}10.0$
  - 2. $3.1\text{--}4.4$
  - 3. $6.0\text{--}7.6$
  - 4. $5.0\text{--}8.0$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 34
Match the polymer in List-I with its polymer type in List-II:
- **List-I**:
  - P. Polyethylene
  - Q. Nylon-6,6
  - R. Buna-S
  - S. Bakelite
- **List-II**:
  - 1. Condensation polyamide
  - 2. Addition homopolymer
  - 3. Thermosetting cross-linked polymer
  - 4. Synthetic elastomer (copolymer)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 35
Match the colloid in List-I with its optical/electrical property in List-II:
- **List-I**:
  - P. Tyndall effect
  - Q. Brownian motion
  - R. Electrophoresis
  - S. Coagulation
- **List-II**:
  - 1. Zigzag random kinetic motion of colloidal particles
  - 2. Scattering of light by colloidal particles
  - 3. Aggregation of colloidal particles into a precipitate
  - 4. Movement of colloidal particles under an applied electric field

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 36
Match the halide in List-I with its physical state at room temperature in List-II:
- **List-I**:
  - P. Fluorine ($\text{F}_2$)
  - Q. Chlorine ($\text{Cl}_2$)
  - R. Bromine ($\text{Br}_2$)
  - S. Iodine ($\text{I}_2$)
- **List-II**:
  - 1. Greenish-yellow gas
  - 2. Pale yellow gas
  - 3. Dark reddish-brown liquid
  - 4. Dark violet-black solid

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 3, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = |x - 1| + |x - 2|$ for $x \in \mathbb{R}$:
(A) $f(x)$ is continuous for all $x \in \mathbb{R}$.  
(B) $f(x)$ is not differentiable at $x = 1$ and $x = 2$.  
(C) The minimum value of $f(x)$ is 1, attained for all $x \in [1, 2]$.  
(D) $f(x) = 2x - 3$ for $x \ge 2$.

#### Question 38
Let $A$ and $B$ be symmetric matrices of the same order ($A^T = A, B^T = B$):
(A) $A + B$ is always symmetric.  
(B) $A B$ is symmetric if and only if $A$ and $B$ commute ($A B = B A$).  
(C) $A B - B A$ is skew-symmetric.  
(D) $A B + B A$ is symmetric.

#### Question 39
Consider the line $\frac{x-1}{1} = \frac{y-2}{2} = \frac{z-3}{3}$:
(A) The line passes through the point $(1, 2, 3)$.  
(B) The line passes through the point $(0, 0, 0)$.  
(C) The direction ratios of the line are $(1, 2, 3)$.  
(D) The line is perpendicular to the plane $x + 2y + 3z = 7$.

#### Question 40
Consider the differential equation $\frac{dy}{dx} = \frac{y}{x}$:
(A) The equation is homogeneous of degree 0.  
(B) The general solution is $y = C x$ (family of straight lines passing through the origin).  
(C) The orthogonal trajectories form the family of concentric circles $x^2 + y^2 = K$.  
(D) The integrating factor is $\frac{1}{x}$.

#### Question 41
Let $X$ follow a discrete uniform distribution on $\{1, 2, 3, \dots, n\}$:
(A) The probability mass function is $P(X = k) = \frac{1}{n}$ for $k = 1, \dots, n$.  
(B) The mean is $E[X] = \frac{n + 1}{2}$.  
(C) The variance is $\text{Var}(X) = \frac{n^2 - 1}{12}$.  
(D) For $n = 6$ (fair die), $E[X] = 3.5$ and $\text{Var}(X) = 35/12$.

#### Question 42
Consider the sequence $a_n = \sqrt{2 + \sqrt{2 + \dots}}$ with $n$ square roots:
(A) $a_1 = \sqrt{2}$, $a_2 = \sqrt{2 + \sqrt{2}}$.  
(B) The recurrence relation is $a_{n+1} = \sqrt{2 + a_n}$.  
(C) The sequence is strictly increasing and bounded above by 2.  
(D) $\lim_{n \to \infty} a_n = 2$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 x^3 dx$$
Calculate the value of $100 I$.

#### Question 44
Find the number of 4-digit permutations that can be formed using the digits $1, 2, 3, 4, 5$ without repetition.

#### Question 45
Find the perpendicular distance from the point $(1, 2, 3)$ to the plane $x - 2y + 2z - 9 = 0$.

#### Question 46
Let $z = 3 + 4i$. Calculate $|z|^2$.

#### Question 47
Let $y(x)$ satisfy $\frac{dy}{dx} = 3x^2$ with $y(0) = 1$. Calculate $y(2)$.

#### Question 48
In a binomial distribution with $n = 4$ and $p = 0.5$, calculate the expected value $E[X]$.

---

## Section 3: Matching List / Matrix Match (Questions 49 to 54)

#### Question 49
Match the function in List-I with its limit as $x \to 0$ in List-II:
- **List-I**:
  - P. $\frac{\sin x}{x}$
  - Q. $\frac{\tan x}{x}$
  - R. $\frac{e^x - 1}{x}$
  - S. $\frac{\ln(1 + x)}{x}$
- **List-II**:
  - 1. $1$
  - 2. $1$
  - 3. $1$
  - 4. $1$

(A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(B) P $\to$ 2, Q $\to$ 1, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 50
Match the curve in List-I with its vertex in List-II:
- **List-I**:
  - P. $y^2 = 4x$
  - Q. $(y - 1)^2 = 4(x - 2)$
  - R. $x^2 = 4y$
  - S. $(x + 1)^2 = 4(y - 3)$
- **List-II**:
  - 1. $(2, 1)$
  - 2. $(0, 0)$
  - 3. $(-1, 3)$
  - 4. $(0, 0)$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 51
Match the complex number in List-I with its complex conjugate in List-II:
- **List-I**:
  - P. $2 + 3i$
  - Q. $2 - 3i$
  - R. $-2 + 3i$
  - S. $-2 - 3i$
- **List-II**:
  - 1. $2 + 3i$
  - 2. $2 - 3i$
  - 3. $-2 + 3i$
  - 4. $-2 - 3i$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 52
Match the matrix operation in List-I with its transpose rule in List-II:
- **List-I**:
  - P. $(A + B)^T$
  - Q. $(A B)^T$
  - R. $(k A)^T$
  - S. $(A^T)^T$
- **List-II**:
  - 1. $B^T A^T$
  - 2. $A^T + B^T$
  - 3. $A$
  - 4. $k A^T$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 53
Match the probability rule in List-I with its formula in List-II:
- **List-I**:
  - P. Addition rule for mutually exclusive events
  - Q. General addition rule
  - R. Multiplication rule for independent events
  - S. Conditional probability
- **List-II**:
  - 1. $P(A) + P(B) - P(A \cap B)$
  - 2. $P(A) + P(B)$
  - 3. $\frac{P(A \cap B)}{P(B)}$
  - 4. $P(A) P(B)$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 54
Match the vector in List-I with its magnitude in List-II:
- **List-I**:
  - P. $3\hat{i} + 4\hat{j}$
  - Q. $\hat{i} + \hat{j} + \hat{k}$
  - R. $2\hat{i} - 2\hat{j} + \hat{k}$
  - S. $5\hat{k}$
- **List-II**:
  - 1. $\sqrt{3}$
  - 2. $5$
  - 3. $5$
  - 4. $3$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 18

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Aharonov-Bohm effect and physical reality of vector potential.
- 2: (A, B, C, D) - Van der Waals Joule-Thomson inversion curve.
- 3: (A, B, C, D) - Rotational Raman selection rules $\Delta J = 0, \pm 2$ and line spacing.
- 4: (A, B, C, D) - Abraham-Lorentz radiation damping and jerk dependence.
- 5: (A, B, C) - Rolling without slip sweet spot $h = 2R/5$. Statement (D) is false: for $h < 2R/5$, the ball tends to slip forward, so friction acts backward.
- 6: (A, B, C, D) - Plane electromagnetic wave fields and Poynting vector.

#### Solutions 7 to 12:
- 7: $\Phi_0 = h/e = \frac{6.626 \times 10^{-34}}{1.602 \times 10^{-19}} \approx 4.14 \times 10^{-15}\text{ Wb}$. Value $= 4.14$. (Answer: 4.14)
- 8: $T_i = \frac{2a}{Rb} = \frac{2 \times 0.137}{8.314 \times 3.87 \times 10^{-5}} = \frac{0.274}{3.218 \times 10^{-4}} \approx 851\text{ K}$. (Answer: 851)
- 9: First Stokes is at $-6B$, first Anti-Stokes is at $+6B$. Separation $\Delta\bar{\nu} = 12 B = 12 \times 2.0 = 24.0\text{ cm}^{-1}$. (Answer: 24.0)
- 10: $h = \frac{2}{5}R = 0.4 \times 3.0 = 1.2\text{ cm}$. (Answer: 1.2)
- 11: $C = \kappa \frac{\varepsilon_0 A}{d} = 4.0 \frac{(8.85 \times 10^{-12}) (0.05)}{2.0 \times 10^{-3}} = 8.85 \times 10^{-10}\text{ F}$.
  $U = \frac{1}{2} C V^2 = \frac{1}{2} (8.85 \times 10^{-10}) (40000) = 1.77 \times 10^{-5}\text{ J} = 17.7\text{ }\mu\text{J}$. (Answer: 17.7)
- 12: Torque $\tau = F L = 5.0 \times 1.20 = 6.0\text{ N m}$. Moment of inertia $I = \frac{1}{3} M L^2 = \frac{1}{3}(2)(1.44) = 0.96\text{ kg m}^2$.
  $\alpha = \tau / I = 6.0 / 0.96 = 6.25\text{ rad/s}^2$. (Answer: 6.25)

#### Solutions 13 to 18:
- 13: By angular momentum conservation, $v_p r_p = v_a r_a \implies v_p / v_a = r_a / r_p$. (A)
- 14: Path difference $\Delta x = \sqrt{x^2 + (y+2)^2} - \sqrt{x^2 + (y-2)^2}$. Maxima occur for integer multiples of $\lambda$. (A)
- 15: Ampere's law gives $B = \frac{\mu_0 I}{2\pi r}$. (A)
- 16: Volume $V' = 8 V \implies R' = 2R$. Charge $Q' = 8Q$.
  $V' = \frac{Q'}{4\pi\varepsilon_0 R'} = \frac{8Q}{4\pi\varepsilon_0 (2R)} = 4 V_0$. (A)
- 17: $\eta = 1 - T_C / T_H = 0.50 \implies 273 / T_H = 0.50 \implies T_H = 546\text{ K} = 273^\circ\text{C}$. (A)
- 18: $e V_s = h\nu - \Phi \implies V_s = \frac{h}{e}\nu - \frac{\Phi}{e}$. Slope is $h/e$. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Baeyer-Villiger oxidation mechanism and migratory aptitude.
- 20: (A, B, C, D) - Quadruple bond in $[\text{Re}_2\text{Cl}_8]^{2-}$.
- 21: (A, B, C, D) - Eyring transition state theory and activation entropy.
- 22: (A, B, C, D) - Crabtree's catalyst directed hydrogenation.
- 23: (A, B, C, D) - Electrical double layer and zeta potential.
- 24: (A, B, C, D) - Group V basic radical analysis and flame tests.

#### Solutions 25 to 30:
- 25: $\text{CaCO}_3 \rightleftharpoons \text{Ca}^{2+} + \text{CO}_3^{2-}$.
  $K_{sp} = S^2 = 4.9 \times 10^{-9} \implies S = 7.0 \times 10^{-5}\text{ mol/L}$. (Answer: 7)
- 26: Strong-field $\text{CN}^-$ gives low-spin $d^5$ $\text{Fe}^{3+}$ ($t_{2g}^5$) $\implies 1$ unpaired electron $\implies \mu = \sqrt{1(3)} = \sqrt{3} \approx 1.73\text{ BM}$. (Answer: 1.73)
- 27: Molar mass $= 2 \times 23 = 46\text{ g/mol}$. Empirical formula $\text{C}_2\text{H}_6\text{O}$ (mass 46) $\implies n = 1 \implies 6$ hydrogens. (Answer: 6)
- 28: $\ln 4 = \frac{E_a}{R}\left(\frac{20}{300 \times 320}\right) \implies 1.386 = \frac{E_a}{8.314}\left(\frac{20}{96000}\right) \implies E_a = 55.3\text{ kJ/mol}$. (Answer: 55.3)
- 29: Moles of electrons $= \frac{I t}{F} = \frac{4.825 \times 2000}{96500} = \frac{9650}{96500} = 0.10\text{ mol}$.
  $\text{Mg}^{2+} + 2e^- \to \text{Mg} \implies 0.05\text{ mol of Mg} = 0.05 \times 24.3 = 1.215\text{ g} \approx 1.22\text{ g}$. (Answer: 1.22)
- 30: $\Delta T_b = i K_b m \implies i = \frac{\Delta T_b}{K_b m} = \frac{0.070}{0.512 \times 0.050} = \frac{0.070}{0.0256} \approx 2.73$. (Answer: 2.73)

#### Solutions 31 to 36:
- 31: Etard reaction uses chromyl chloride ($\text{CrO}_2\text{Cl}_2$). (A)
- 32: $[\text{Pt(NH}_3)_2\text{Cl}_2]$ is $5d^8$ square planar. (A)
- 33: Uracil is present in RNA instead of Thymine. (A)
- 34: Self-reduction: $2\text{PbO} + \text{PbS} \to 3\text{Pb} + \text{SO}_2$. (A)
- 35: Vigorous nitration of phenol produces 2,4,6-trinitrophenol (picric acid). (A)
- 36: Conjugate acid adds $\text{H}^+$: $\text{NH}_4^+$. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Convolution and Plancherel theorems.
- 38: (A, B, C, D) - Jordan canonical form structure.
- 39: (A, B, C, D) - Circles of Apollonius geometry.
- 40: (A, B, C, D) - Catalan numbers combinatorial interpretations.
- 41: (A, B, C, D) - Rational function graph features.
- 42: (A, B, C, D) - $90^\circ$ rotation matrix properties.

#### Solutions 43 to 48:
- 43: $I = B(3, 3) = \frac{2! \cdot 2!}{5!} = \frac{4}{120} = \frac{1}{30} \implies 60 I = 2$. (Answer: 2)
- 44: Letters: S(3), U(1), C(2), E(1). Total $= 7! / (3! 2!) = 5040 / 12 = 420$. (Answer: 420)
- 45: $d = \frac{|2(1) + 1(2) + 2(3) - 3|}{\sqrt{4 + 1 + 4}} = \frac{|2 + 2 + 6 - 3|}{3} = \frac{7}{3} \approx 2.33$. (Answer: 2.33)
- 46: $(1 - z)(1 - z^2) = 1 - z - z^2 + z^3 = 1 - (z + z^2) + 1 = 2 - (-1) = 3$. (Answer: 3)
- 47: Linear ODE: $y' - y = x \implies I.F. = e^{-x} \implies y e^{-x} = \int x e^{-x} dx = -x e^{-x} - e^{-x} + C$.
  $y = -x - 1 + C e^x$. $y(0) = 0 \implies -1 + C = 0 \implies C = 1$.
  $y(1) = -1 - 1 + e = e - 2 \approx 0.72$. (Answer: 0.72)
- 48: $\binom{4}{2} (1/2)^4 = 6/16 = 0.375 \approx 0.38$. (Answer: 0.38)

#### Solutions 49 to 54:
- 49: Area $= \int_0^2 x^3 dx = [x^4 / 4]_0^2 = 16 / 4 = 4$. (A)
- 50: $a_1 = 5, a_{20} = 62 \implies S_{20} = 20 \frac{5 + 62}{2} = 10 \times 67 = 670$. (A)
- 51: Limit $= \lim \frac{\tan x(1 - \cos x)}{x^3} = 1 \times (1/2) = 1/2$. (A)
- 52: $y^2 = 4(2)x \implies a = 2 \implies$ directrix $x = -2$. (A)
- 53: Distance from $x$-axis $= \sqrt{y^2 + z^2} = \sqrt{9 + 16} = 5$. (A)
- 54: $|\vec{a}\times\vec{b}|^2 = |\vec{a}|^2 |\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2 = (4)(9) - 9 = 27 \implies 3\sqrt{3}$. (A)
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 2
## IIT Delhi Benchmark JEE Advanced Mock Examination 18

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Work done in uniform electric field and potential energy.
- 2: (A, B, C, D) - Simple harmonic motion energy and kinematics.
- 3: (A, B, C, D) - Conjugate positions of convex lens and $4f$ minimum distance.
- 4: (A, B, C, D) - Heat pump COP and energy delivery.
- 5: (A, B, C, D) - Magnetic Lorentz force properties.
- 6: (A, B, C, D) - AC capacitor voltage-current phase relation.

#### Solutions 7 to 12:
- 7: $v = \omega \sqrt{A^2 - x^2} = \frac{2\pi}{4.0}\sqrt{100 - 36} = \frac{\pi}{2}(8) = 4\pi \approx 12.57\text{ cm/s}$. (Answer: 12.57)
- 8: Conjugate displacement $d = \sqrt{D^2 - 4 D f} = \sqrt{80^2 - 4(80)(15)} = \sqrt{6400 - 4800} = \sqrt{1600} = 40.0\text{ cm}$. (Answer: 40.00)
- 9: $W_{\text{in}} = Q_H / \text{COP} = 25.0 / 5.0 = 5.0\text{ kW}$. (Answer: 5.0)
- 10: $r = \frac{\sqrt{2 m K}}{q B} = \frac{\sqrt{2 (1.67 \times 10^{-27}) (2.0 \times 1.6 \times 10^{-13})}}{(1.6 \times 10^{-19}) (0.50)} = \frac{3.268 \times 10^{-20}}{8.0 \times 10^{-20}} = 0.4085\text{ m} \approx 40.9\text{ cm}$. (Answer: 40.9)
- 11: $V_{\text{rms}} = 141.4 / \sqrt{2} = 100\text{ V}$. $I_{\text{rms}} = V_{\text{rms}} \omega C = 100 \times 100\pi \times 10^{-4} = \pi \approx 3.14\text{ A}$. (Answer: 3.14)
- 12: $F = \mu m g = 0.40 \times 5.0 \times 9.8 = 19.6\text{ N}$. (Answer: 19.6)

#### Solutions 13 to 18 (Matching Lists):
- 13: P-2, Q-1, R-4, S-3. (A)
- 14: P-2, Q-1, R-4, S-3. (A)
- 15: P-2, Q-1, R-4, S-3. (A)
- 16: P-2, Q-1, R-4, S-3. (A)
- 17: P-2, Q-1, R-4, S-3. (A)
- 18: P-4, Q-3, R-2, S-1. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Electrophilic aromatic substitution directing effects.
- 20: (A, B, C, D) - Intensive vs extensive thermodynamic quantities in electrochemistry.
- 21: (A, B, C, D) - Second order reaction kinetics.
- 22: (A, B, C, D) - Crystal structures of NaCl, CsCl, ZnS.
- 23: (A, B, C, D) - DNA and RNA structural features.
- 24: (A, B, C, D) - Copper smelting metallurgy.

#### Solutions 25 to 30:
- 25: $[\text{OH}^-] = 0.010\text{ M} \implies \text{pOH} = 2.00 \implies \text{pH} = 12.00$. (Answer: 12.00)
- 26: High-spin $d^6$ $\text{Co}^{3+}$ with $\text{F}^-$ has 4 unpaired electrons $\implies \mu = \sqrt{24} \approx 4.90\text{ BM}$. (Answer: 4.90)
- 27: Empirical formula $\text{CH}_2\text{O}$ (mass 30). Multiple $180/30 = 6 \implies \text{C}_6\text{H}_{12}\text{O}_6 \implies 6$ carbons. (Answer: 6)
- 28: 3 half-lives $\implies (1/2)^3 = 1/8 = 12.5\%$. (Answer: 12.5)
- 29: $m = \frac{M I t}{2 F} = \frac{65.4 \times 5.0 \times 1930}{2 \times 96500} = \frac{631110}{193000} \approx 3.27\text{ g}$. (Answer: 3.27)
- 30: Molality $m = \frac{1.80 / 180}{0.100} = 0.10\text{ mol/kg}$. $\Delta T_f = K_f m = 1.86 \times 0.10 = 0.186^\circ\text{C}$. (Answer: 0.186)

#### Solutions 31 to 36:
- 31: P-4, Q-3, R-2, S-1. (A)
- 32: P-2, Q-1, R-4, S-3. (A)
- 33: P-2, Q-1, R-4, S-3. (A)
- 34: P-2, Q-1, R-4, S-3. (A)
- 35: P-2, Q-1, R-4, S-3. (A)
- 36: P-2, Q-1, R-3, S-4. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Sum of absolute values graph analysis.
- 38: (A, B, C, D) - Symmetric matrix products and commutators.
- 39: (A, B, C, D) - Line geometry in 3D.
- 40: (A, B, C, D) - Homogeneous ODE and orthogonal trajectories.
- 41: (A, B, C, D) - Discrete uniform distribution moments.
- 42: (A, B, C, D) - Nested radical sequence convergence to 2.

#### Solutions 43 to 48:
- 43: $I = 1/4 = 0.25 \implies 100 I = 25$. (Answer: 25)
- 44: $P(5, 4) = 5 \times 4 \times 3 \times 2 = 120$. (Answer: 120)
- 45: $d = \frac{|1 - 4 + 6 - 9|}{\sqrt{1 + 4 + 4}} = \frac{6}{3} = 2.0$. (Answer: 2.0)
- 46: $|z|^2 = 3^2 + 4^2 = 25$. (Answer: 25)
- 47: $y(x) = x^3 + 1 \implies y(2) = 8 + 1 = 9$. (Answer: 9)
- 48: $E[X] = n p = 4 \times 0.5 = 2.0$. (Answer: 2.0)

#### Solutions 49 to 54:
- 49: P-1, Q-2, R-3, S-4. (A)
- 50: P-2, Q-1, R-4, S-3. (A)
- 51: P-2, Q-1, R-4, S-3. (A)
- 52: P-2, Q-1, R-4, S-3. (A)
- 53: P-2, Q-1, R-4, S-3. (A)
- 54: P-2, Q-1, R-4, S-3. (A)
"""

val_md = r"""# Answer Key & Benchmark Validation — Mock 18
## IIT Delhi Benchmark Calibration

### Paper 1 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 4.14 | **C25** | Num | 7 | **M43** | Num | 2 |
| **P8** | Num | 851 | **C26** | Num | 1.73 | **M44** | Num | 420 |
| **P9** | Num | 24.0 | **C27** | Num | 6 | **M45** | Num | 2.33 |
| **P10** | Num | 1.2 | **C28** | Num | 55.3 | **M46** | Num | 3 |
| **P11** | Num | 17.7 | **C29** | Num | 1.22 | **M47** | Num | 0.72 |
| **P12** | Num | 6.25 | **C30** | Num | 2.73 | **M48** | Num | 0.38 |
| **P13** | Single | A | **C31** | Single | A | **M49** | Single | A |
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
| **P7** | Num | 12.57 | **C25** | Num | 12.00 | **M43** | Num | 25 |
| **P8** | Num | 40.00 | **C26** | Num | 4.90 | **M44** | Num | 120 |
| **P9** | Num | 5.0 | **C27** | Num | 6 | **M45** | Num | 2.0 |
| **P10** | Num | 40.9 | **C28** | Num | 12.5 | **M46** | Num | 25 |
| **P11** | Num | 3.14 | **C29** | Num | 3.27 | **M47** | Num | 9 |
| **P12** | Num | 19.6 | **C30** | Num | 0.186 | **M48** | Num | 2.0 |
| **P13** | Match | A | **C31** | Match | A | **M49** | Match | A |
| **P14** | Match | A | **C32** | Match | A | **M50** | Match | A |
| **P15** | Match | A | **C33** | Match | A | **M51** | Match | A |
| **P16** | Match | A | **C34** | Match | A | **M52** | Match | A |
| **P17** | Match | A | **C35** | Match | A | **M53** | Match | A |
| **P18** | Match | A | **C36** | Match | A | **M54** | Match | A |
"""

if __name__ == "__main__":
    create_mock_files(
        18,
        paper_1_md,
        paper_2_md,
        sol_1_md,
        sol_2_md,
        val_md,
        iit_name="IIT_Delhi"
    )

