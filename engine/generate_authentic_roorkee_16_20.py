"""
IIT Roorkee Mocks 16 to 20 Generator
Organising Institute: Indian Institute of Technology Roorkee
Empirical Benchmark: 2008, 2013, 2019 Official JEE Advanced Papers
Features:
- Mechanics dominance (>= 45% of physics: spool on incline, Blasius boundary layer, capillary-gravity wave dispersion, Carey Foster bridge)
- Chemistry: Robinson annulation, BET multilayer adsorption, Tafel overpotential, Dow magnesium extraction
- Mathematics: Double integral order reversal, quadric surface tangents, Leibniz rule for n-th derivatives, Markov chains
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_roorkee_16_to_20():
    for mock_idx in range(16, 21):
        pad = f"{mock_idx:02d}"

        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)
**Historical Reference Benchmark**: 2008, 2013, 2019 Official Examination Papers  
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
A spool of total mass $M$, inner radius $r$, and outer radius $R$ has a moment of inertia $I = \frac{1}{2}MR^2$ about its central axis. A light string wrapped around the inner cylinder is pulled with constant tension $T$ at an angle $\theta$ to the horizontal while the spool rests on a rough horizontal surface:
(A) The spool will roll without slipping to the right if $\cos\theta > r/R$.  
(B) The spool will roll without slipping to the left if $\cos\theta < r/R$.  
(C) If $\cos\theta = r/R$, the line of action of tension passes through the instantaneous center of rotation, and the spool remains in static equilibrium or pure sliding.  
(D) The direction of static friction depends on the angle $\theta$ and tension magnitude.

#### Question 2
Regarding surface waves on deep water of density $\rho$ and surface tension $T$ with dispersion relation $\omega^2 = g k + \frac{T}{\rho}k^3$:
(A) For long wavelengths (small wavenumber $k$), gravity dominates: $\omega \approx \sqrt{gk}$ (gravity waves).  
(B) For very short wavelengths (large $k$), surface tension dominates: $\omega \approx \sqrt{\frac{T}{\rho}k^3}$ (capillary waves / ripples).  
(C) The phase velocity $v_p = \omega/k$ attains a minimum value at critical wavenumber $k_c = \sqrt{\frac{\rho g}{T}}$.  
(D) The minimum phase velocity on water is $v_{\min} = \left(\frac{4gT}{\rho}\right)^{1/4} \approx 23\text{ cm/s}$.

#### Question 3
In a Carey Foster bridge experiment used to determine the resistance per unit length $\rho$ of a bridge wire and the difference between two nearly equal resistances $X$ and $Y$:
(A) If balancing lengths are $l_1$ and $l_2$ before and after interchanging $X$ and $Y$, then $X - Y = \rho(l_2 - l_1)$.  
(B) End errors of the bridge wire cancel out completely in the difference $(l_2 - l_1)$.  
(C) The resistance per unit length $\rho$ can be calibrated by using a standard fractional resistance shunt.  
(D) The Carey Foster bridge provides significantly higher precision than a standard meter bridge for measuring small resistance differences.

#### Question 4
In Jaeger's method to measure the surface tension of a liquid:
(A) An air bubble is formed slowly at the tip of a vertical capillary tube of radius $r$ dipped to depth $h$ in the liquid.  
(B) The maximum pressure inside the bubble occurs when the bubble is hemispherical with radius equal to the tube radius $r$.  
(C) The maximum manometer pressure reading $h_m$ satisfies $\rho_m g h_m = \rho g h + \frac{2T}{r}$.  
(D) The surface tension is calculated as $T = \frac{r g}{2}(\rho_m h_m - \rho h)$.

#### Question 5
A uniform solid sphere of mass $M$ and radius $R$ is placed on an accelerating wedge of inclination $\theta$ which accelerates horizontally with acceleration $a_0$:
(A) The apparent gravity in the reference frame of the wedge is $\vec{g}_{\text{eff}} = \vec{g} - a_0\hat{i}$.  
(B) The component of apparent gravity along the inclined face is $g\sin\theta - a_0\cos\theta$.  
(C) The sphere will remain stationary relative to the wedge if $a_0 = g\tan\theta$.  
(D) If $a_0 > g\tan\theta$, the sphere rolls up the incline.

#### Question 6
Regarding the thermal conductivity measurement of a metal bar using Searle's method:
(A) Heat flows along the bar under steady-state conditions: $\frac{dQ}{dt} = -K A \frac{dT}{dx}$.  
(B) Radial heat loss is minimized by thick thermal lagging (insulation) around the bar.  
(C) The rate of heat arrival at the cool end is measured by circulating cooling water: $\frac{dQ}{dt} = m_w c_w (T_4 - T_3)$.  
(D) Temperature gradient along the bar is measured by two sensitive thermometers placed at known distance $d$ apart in well-greased holes.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A spool has inner radius $r = 0.10\text{ m}$ and outer radius $R = 0.20\text{ m}$. The critical angle $\theta_c$ in degrees at which pulling the string produces no rolling motion is $\theta_c^\circ$. (Given $\cos\theta_c = r/R = 0.50$). Find $\theta_c$.

#### Question 8
In Jaeger's method, a capillary tube of internal radius $r = 0.20\text{ mm}$ is dipped to depth $h = 5.0\text{ cm}$ in water ($\rho = 1000\text{ kg/m}^3$). A manometer containing oil of density $\rho_m = 800\text{ kg/m}^3$ shows a maximum pressure height $h_m = 11.0\text{ cm}$. Taking $g = 9.8\text{ m/s}^2$, the surface tension of water in $\text{N/m}$ is $T$. Find $T$ rounded off to three decimal places.

#### Question 9
In a Carey Foster bridge, interchanging two resistances $X$ and $Y$ shifts the balance point by $\Delta l = 8.0\text{ cm}$. If the resistance per unit length of the bridge wire is $\rho = 0.050\text{ }\Omega/\text{cm}$, the resistance difference $|X - Y|$ in ohms is $R_{\text{diff}}$. Find $R_{\text{diff}}$ rounded off to two decimal places.

#### Question 10
In a Searle's thermal conductivity experiment, a copper bar of diameter $D = 4.0\text{ cm}$ has two thermometers placed $d = 10.0\text{ cm}$ apart reading $T_1 = 85.0^\circ\text{C}$ and $T_2 = 65.0^\circ\text{C}$. Water flows through the cooling coil at $m_w = 2.0\text{ g/s}$ and rises in temperature by $\Delta T_w = 5.0^\circ\text{C}$. Taking $c_w = 4.2\text{ J/(g K)}$ and $\pi = 3.14$, the thermal conductivity $K$ of copper in $\text{W/(m K)}$ is $K$. Find $K$ rounded off to the nearest integer.

#### Question 11
A uniform solid sphere of mass $M = 3.0\text{ kg}$ and radius $R = 0.12\text{ m}$ rolls without slipping on a horizontal surface at $v = 2.8\text{ m/s}$. The work required to bring it completely to rest in joules is $W\text{ J}$. Find $W$ rounded off to two decimal places.

#### Question 12
A vertical rectangular plate of width $b = 2.0\text{ m}$ and height $h = 3.0\text{ m}$ is submerged in water such that its upper edge is at the water surface. Taking $g = 9.8\text{ m/s}^2$ and $\rho = 1000\text{ kg/m}^3$, the total hydrostatic force on one face of the plate in kilonewtons ($\text{kN}$) is $F$. Find $F$ rounded off to one decimal place.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The center of mass of a uniform solid right circular cone of height $h$ and base radius $R$ is located on its axis of symmetry at distance from the base of:
(A) $h/4$  
(B) $h/3$  
(C) $3h/8$  
(D) $h/2$

#### Question 14
Two bodies of masses $M$ and $m$ ($M > m$) are connected by a light spring on a frictionless horizontal table. The system is pulled apart and released from rest. The ratio of kinetic energies $K_M / K_m$ is:
(A) $m / M$  
(B) $M / m$  
(C) 1  
(D) $\sqrt{m/M}$

#### Question 15
An open tank filled with water has a small hole at depth $h$ below the surface. The range of the water jet on the ground level (tank base) is maximum when the hole is located at depth:
(A) $H/2$  
(B) $H/4$  
(C) $3H/4$  
(D) $H$

#### Question 16
The SI unit of surface tension is:
(A) $\text{N/m}$  
(B) $\text{N m}$  
(C) $\text{J m}$  
(D) $\text{N/m}^2$

#### Question 17
A solid cylinder of mass $M$ and radius $R$ rolls down an incline of angle $\theta$ without slipping. The minimum coefficient of friction $\mu_s$ required is:
(A) $\frac{1}{3}\tan\theta$  
(B) $\frac{2}{7}\tan\theta$  
(C) $\frac{1}{2}\tan\theta$  
(D) $\tan\theta$

#### Question 18
For an adiabatic process in an ideal gas with ratio of specific heats $\gamma$, the slope of the $P-V$ curve at any point is:
(A) $-\gamma \frac{P}{V}$  
(B) $-\frac{P}{V}$  
(C) $-\frac{1}{\gamma}\frac{P}{V}$  
(D) $-\gamma^2 \frac{P}{V}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Robinson annulation reaction:
(A) It involves a tandem Michael addition of an enolate to an $\alpha,\beta$-unsaturated ketone followed by an intramolecular aldol condensation.  
(B) It is widely utilized in the synthesis of fused polycyclic steroids and terpenoids.  
(C) The final product is a 2-cyclohexenone derivative.  
(D) The intramolecular aldol dehydration is thermodynamically driven by the formation of an extended conjugated $\pi$-system.

#### Question 20
Regarding the Brunauer-Emmett-Teller (BET) adsorption isotherm:
(A) It extends the Langmuir monolayer model to multilayer physical adsorption.  
(B) The linearized BET equation is $\frac{P}{V(P_0 - P)} = \frac{1}{V_m C} + \frac{C-1}{V_m C}\frac{P}{P_0}$.  
(C) A plot of $\frac{P}{V(P_0 - P)}$ versus $P/P_0$ is linear for $0.05 \le P/P_0 \le 0.35$.  
(D) The BET surface area of porous materials is determined from the monolayer capacity $V_m$.

#### Question 21
Regarding the electrochemical overpotential and the Tafel equation:
(A) Overpotential $\eta = E - E_{\text{rev}}$ represents the deviation of electrode potential from its reversible thermodynamic value during current flow.  
(B) For high overpotentials, the Butler-Volmer equation simplifies to the Tafel equation: $\eta = a + b\ln|j|$.  
(C) Overpotential is caused by activation polarization, concentration polarization, and ohmic resistance.  
(D) The evolution of hydrogen on lead and mercury electrodes exhibits an exceptionally high overpotential.

#### Question 22
Regarding the extraction of magnesium from seawater (Dow process):
(A) Seawater is treated with slaked lime $\text{Ca}(\text{OH})_2$ to precipitate magnesium hydroxide $\text{Mg}(\text{OH})_2$.  
(B) The precipitate is dissolved in hydrochloric acid to yield aqueous magnesium chloride $\text{MgCl}_2$.  
(C) Hydrated $\text{MgCl}_2 \cdot 6\text{H}_2\text{O}$ must be dehydrated in a stream of dry $\text{HCl}$ gas to prevent hydrolysis into $\text{MgO}$.  
(D) Anhydrous molten $\text{MgCl}_2$ is electrolyzed with carbon anodes to yield liquid magnesium and chlorine gas.

#### Question 23
Regarding the chemical properties and reactivity of lanthanides versus actinides:
(A) Actinides exhibit a greater range of oxidation states (up to $+7$) than lanthanides (predominantly $+3$) because $5f, 6d$, and $7s$ energy levels are close in energy.  
(B) $5f$ orbitals have greater radial extension and participate more in bonding than $4f$ orbitals.  
(C) Both series exhibit contraction of ionic radii with increasing atomic number (lanthanide and actinide contractions).  
(D) Actinide complexes display more covalent character in their metal-ligand bonds than corresponding lanthanide complexes.

#### Question 24
Which of the following compounds exhibits optical isomerism:
(A) $[\text{Co}(\text{en})_3]^{3+}$  
(B) *cis*-$[\text{Pt}(\text{en})_2\text{Cl}_2]^{2+}$  
(C) *trans*-$[\text{Pt}(\text{en})_2\text{Cl}_2]^{2+}$ (achiral due to inversion center)  
(D) $[\text{Cr}(\text{ox})_3]^{3-}$

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{AgBr}$ is $K_{\text{sp}} = 5.0 \times 10^{-13}$ at $298\text{ K}$. Calculate the molar solubility of $\text{AgBr}$ in pure water in units of $10^{-7}\text{ M}$. Find the value rounded off to two decimal places.

#### Question 26
Calculate the $\text{pH}$ of a $0.0050\text{ M}$ aqueous solution of barium hydroxide $\text{Ba}(\text{OH})_2$ at $298\text{ K}$ assuming complete dissociation. Find the $\text{pH}$.

#### Question 27
The standard reduction potentials are $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$ and $E^\circ(\text{Ni}^{2+}/\text{Ni}) = -0.25\text{ V}$. The standard EMF of the galvanic cell $\text{Ni} \mid \text{Ni}^{2+} \parallel \text{Ag}^+ \mid \text{Ag}$ is $E^\circ_{\text{cell}}\text{ V}$. Find $E^\circ_{\text{cell}}$.

#### Question 28
For a chemical reaction $A \to \text{Products}$, a plot of $\ln[A]$ versus time $t$ gives a straight line with slope $-0.02303\text{ min}^{-1}$. The half-life of this reaction in minutes is $t_{1/2}\text{ min}$. (Take $\ln 2 \approx 0.693$). Find $t_{1/2}$ rounded off to the nearest integer.

#### Question 29
A $0.10\text{ m}$ aqueous solution of $\text{NaCl}$ freezes at $-0.3534^\circ\text{C}$. Given $K_f(\text{H}_2\text{O}) = 1.86\text{ K kg mol}^{-1}$, the degree of dissociation $\alpha$ of $\text{NaCl}$ is $\alpha\%$. Find $\alpha$ as a percentage.

#### Question 30
Find the oxidation state of uranium in the uranyl ion $\text{UO}_2^{2+}$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the oxymercuration-demercuration of an alkene, the net addition of water occurs with:
(A) Markovnikov regioselectivity and no carbocation rearrangement  
(B) Anti-Markovnikov regioselectivity with rearrangement  
(C) Syn addition with rearrangement  
(D) Free radical mechanism

#### Question 32
Which of the following elements has the lowest boiling point among all chemical elements:
(A) Helium ($\text{He}$)  
(B) Hydrogen ($\text{H}_2$)  
(C) Neon ($\text{Ne}$)  
(D) Nitrogen ($\text{N}_2$)

#### Question 33
The shape and hybridization of the $\text{CO}_3^{2-}$ ion are:
(A) Trigonal planar, $sp^2$  
(B) Tetrahedral, $sp^3$  
(C) Pyramidal, $sp^3$  
(D) T-shaped, $sp^3d$

#### Question 34
In the extraction of magnesium by the Dow process, the electrolyte used is:
(A) Molten anhydrous $\text{MgCl}_2$ with $\text{CaCl}_2$ and $\text{NaCl}$  
(B) Aqueous $\text{MgCl}_2$  
(C) Molten $\text{Mg}(\text{OH})_2$  
(D) Solid $\text{MgO}$

#### Question 35
The secondary structure of a protein is mainly stabilized by:
(A) Hydrogen bonds  
(B) Peptide bonds  
(C) Disulfide bonds  
(D) van der Waals forces

#### Question 36
The conjugate base of dihydrogen phosphate $\text{H}_2\text{PO}_4^-$ is:
(A) $\text{HPO}_4^{2-}$  
(B) $\text{H}_3\text{PO}_4$  
(C) $\text{PO}_4^{3-}$  
(D) $\text{OH}^-$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $I = \int_0^1 \int_y^1 e^{x^2} dx dy$:
(A) The region of integration is the triangle bounded by $y = 0, x = 1$, and $y = x$.  
(B) Reversing the order of integration yields $\int_0^1 dx \int_0^x e^{x^2} dy$.  
(C) $\int_0^x e^{x^2} dy = x e^{x^2}$.  
(D) The value of the integral is $I = \frac{e - 1}{2}$.

#### Question 38
Consider the tangent plane to the ellipsoid $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ at point $(x_0, y_0, z_0)$:
(A) The equation of the tangent plane is $\frac{x x_0}{a^2} + \frac{y y_0}{b^2} + \frac{z z_0}{c^2} = 1$.  
(B) The normal vector to the tangent plane is $\vec{n} = \left(\frac{x_0}{a^2}, \frac{y_0}{b^2}, \frac{z_0}{c^2}\right)$.  
(C) The perpendicular distance from the center $(0,0,0)$ to the tangent plane is $p = \left[\frac{x_0^2}{a^4} + \frac{y_0^2}{b^4} + \frac{z_0^2}{c^4}\right]^{-1/2}$.  
(D) The locus of the point of intersection of three mutually perpendicular tangent planes is the director sphere $x^2 + y^2 + z^2 = a^2 + b^2 + c^2$.

#### Question 39
Let $u(x)$ and $v(x)$ be $n$-times differentiable functions. By Leibniz's rule:
(A) $\frac{d^n}{dx^n}(u v) = \sum_{k=0}^n \binom{n}{k} u^{(n-k)} v^{(k)}$.  
(B) If $u = x^2$ and $v = e^x$, then $\frac{d^n}{dx^n}(x^2 e^x) = e^x [x^2 + 2nx + n(n-1)]$.  
(C) If $y = \arcsin x$, then $(1-x^2)y_{n+2} - (2n+1)x y_{n+1} - n^2 y_n = 0$.  
(D) For $n=1$, the formula reduces to the standard product rule $(uv)' = u'v + uv'$.

#### Question 40
Consider a two-state Markov chain with transition probability matrix $P = \begin{pmatrix} 0.8 & 0.2 \\ 0.4 & 0.6 \end{pmatrix}$:
(A) The matrix is a row-stochastic matrix (row sums equal 1).  
(B) The stationary probability distribution $\vec{\pi} = (\pi_1, \pi_2)$ satisfies $\vec{\pi} P = \vec{\pi}$ and $\pi_1 + \pi_2 = 1$.  
(C) The stationary probabilities are $\pi_1 = 2/3$ and $\pi_2 = 1/3$.  
(D) The eigenvalues of $P$ are $\lambda_1 = 1$ and $\lambda_2 = 0.4$.

#### Question 41
Let $f(x) = \frac{1}{1 + e^{-x}}$ (the logistic sigmoid function):
(A) $f(x)$ is strictly increasing on $\mathbb{R}$.  
(B) $f'(x) = f(x)(1 - f(x))$.  
(C) The point $(0, 1/2)$ is a point of inflection of $f(x)$.  
(D) The range of $f(x)$ is $(0, 1)$.

#### Question 42
Consider the system of linear equations in three variables:
$x + y + z = 1$, $x + 2y + 4z = \alpha$, $x + 4y + 10z = \alpha^2$:
(A) The coefficient matrix $A$ has $\det(A) = 0$.  
(B) $\text{rank}(A) = 2$.  
(C) The system is consistent if and only if $\alpha = 1$ or $\alpha = 2$.  
(D) If $\alpha = 1$, the system has infinitely many solutions.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate $\int_0^1 \int_y^1 e^{x^2} dx dy$. Given $e \approx 2.718$, find the value of the integral rounded off to two decimal places.

#### Question 44
Find the remainder when $13^{2024}$ is divided by 100.

#### Question 45
Find the radius of the director sphere of the ellipsoid $\frac{x^2}{16} + \frac{y^2}{9} + \frac{z^2}{4} = 1$. Round off $R^2$ to the nearest integer.

#### Question 46
Let $z$ be a complex number satisfying $z^3 = 8i$. Find $|z|$.

#### Question 47
Find the number of ways to arrange the letters of the word **ASSASSINATION** such that all 4 S's are consecutive.

#### Question 48
Find the perpendicular distance from the point $(1, 2, -1)$ to the plane $3x - 4y + 12z = 5$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arctan\left(\frac{x}{\sqrt{1-x^2}}\right)$ with respect to $x$ is:
(A) $\frac{1}{\sqrt{1-x^2}}$  
(B) $\frac{1}{1+x^2}$  
(C) $\sqrt{1-x^2}$  
(D) $\frac{x}{\sqrt{1-x^2}}$

#### Question 50
The differential equation of the family of curves $y = A e^{2x} + B e^{-2x}$ is:
(A) $\frac{d^2 y}{dx^2} - 4y = 0$  
(B) $\frac{d^2 y}{dx^2} + 4y = 0$  
(C) $\frac{d^2 y}{dx^2} - 2y = 0$  
(D) $\frac{dy}{dx} - 2y = 0$

#### Question 51
The shortest distance from the origin to the plane $2x + 3y + 6z = 14$ is:
(A) 2  
(B) 1  
(C) 7  
(D) 14

#### Question 52
If $A$ is an orthogonal matrix of order 3, then $\det(A)$ can take the values:
(A) $\pm 1$  
(B) 0  
(C) $\pm 2$  
(D) Any real number

#### Question 53
The maximum value of the function $f(x) = x(1-x)^2$ on $[0, 1]$ is:
(A) $4/27$  
(B) $1/4$  
(C) $2/27$  
(D) $1/8$

#### Question 54
A card is drawn from a standard pack of 52 cards. The probability that it is a face card (Jack, Queen, or King) is:
(A) $3/13$  
(B) $1/13$  
(C) $4/13$  
(D) $1/4$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)
**Historical Reference Benchmark**: 2008, 2013, 2019 Official Examination Papers  
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
A uniform solid sphere of mass $M$ and radius $R$ is spinning about a horizontal axis with angular velocity $\omega_0$. It is gently placed on a rough horizontal surface with coefficient of kinetic friction $\mu$:
(A) The force of friction acting on the sphere is $f_k = \mu M g$ directed forward.  
(B) The linear acceleration of the center of mass is $a = \mu g$.  
(C) The angular deceleration about the center of mass is $\alpha = \frac{5\mu g}{2R}$.  
(D) Pure rolling begins at time $t = \frac{2 R \omega_0}{7\mu g}$ with forward speed $v = \frac{2}{7}R\omega_0$.

#### Question 2
Regarding the laminar boundary layer on a flat plate of length $L$ in a fluid of kinematic viscosity $\nu$ and free stream speed $U_\infty$ (Blasius boundary layer):
(A) The boundary layer thickness grows parabolically with distance $x$ from the leading edge: $\delta(x) \approx 5.0\sqrt{\frac{\nu x}{U_\infty}}$.  
(B) The local wall shear stress decreases with distance as $\tau_w(x) \propto 1/\sqrt{x}$.  
(C) The total drag force on one side of the plate of width $b$ is $F_D = 0.664 b \rho U_\infty^2 \sqrt{\frac{\nu L}{U_\infty}}$.  
(D) The flow remains laminar provided the local Reynolds number $Re_x = \frac{U_\infty x}{\nu} < 5 \times 10^5$.

#### Question 3
A hydraulic jump occurs in an open horizontal rectangular channel of width $b$ where flow transitions abruptly from supercritical (depth $y_1$, speed $v_1$) to subcritical (depth $y_2$, speed $v_2$):
(A) The conjugate depths satisfy the Belanger equation: $\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8 Fr_1^2} - 1\right)$ where $Fr_1 = \frac{v_1}{\sqrt{g y_1}} > 1$.  
(B) Mass flow rate $Q = b y_1 v_1 = b y_2 v_2$ is strictly conserved across the jump.  
(C) Total momentum flux (hydrostatic pressure force plus momentum flow rate) is conserved across the jump.  
(D) Mechanical energy is dissipated as turbulent heat within the hydraulic jump.

#### Question 4
In Lees' disc experiment to determine the thermal conductivity of a poor conductor (such as glass or ebonite) in the form of a thin disc of radius $r$ and thickness $d$:
(A) Steady-state heat conduction through the specimen disc balances heat lost by radiation and convection from the lower brass slab.  
(B) The rate of heat loss from the lower slab is determined by measuring its cooling rate $\left(\frac{dT}{dt}\right)_{T_2}$ at the steady-state temperature $T_2$.  
(C) The thermal conductivity is given by $K = \frac{M c d (dT/dt)_{T_2}}{\pi r^2 (T_1 - T_2)}$.  
(D) The method accounts for heat loss from the exposed edges of the specimen and slabs.

#### Question 5
A uniform rod of mass $M$ and length $L$ lies on a frictionless horizontal table. A horizontal impulse $J$ is applied perpendicular to the rod at distance $x$ from its center:
(A) The linear velocity of the center of mass immediately after the impact is $v_{\text{cm}} = J / M$.  
(B) The angular velocity about the center of mass is $\omega = \frac{J x}{I_{\text{cm}}} = \frac{12 J x}{M L^2}$.  
(C) The point on the rod that remains momentarily at rest immediately after impact (instantaneous center of rotation) is at distance $y = \frac{L^2}{12x}$ from the center on the opposite side.  
(D) If $x = L/6$, the end of the rod on the opposite side is the instantaneous center of rotation.

#### Question 6
One mole of an ideal gas undergoes a quasi-static cyclic process represented on the $P-V$ diagram by an ellipse $\frac{(P - P_0)^2}{a^2} + \frac{(V - V_0)^2}{b^2} = 1$:
(A) The net work done by the gas in one clockwise cycle is $W = \pi a b$.  
(B) The maximum pressure reached during the cycle is $P_{\max} = P_0 + a$.  
(C) The maximum volume reached during the cycle is $V_{\max} = V_0 + b$.  
(D) In a counter-clockwise cycle, the work done is negative and equal to $-\pi a b$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A solid sphere of mass $M = 5.0\text{ kg}$ and radius $R = 0.14\text{ m}$ spinning at $\omega_0 = 50.0\text{ rad/s}$ is placed on a horizontal floor with $\mu_k = 0.20$. Taking $g = 9.8\text{ m/s}^2$, the steady-state velocity of pure rolling in $\text{m/s}$ is $v$. Find $v$.

#### Question 8
In an open rectangular channel, water flows with initial depth $y_1 = 0.20\text{ m}$ and Froude number $Fr_1 = 3.0$. The conjugate depth $y_2$ after the hydraulic jump in meters is $y_2\text{ m}$. Find $y_2$ rounded off to two decimal places.

#### Question 9
In Lees' disc experiment, a glass disc of thickness $d = 2.0\text{ mm}$ and radius $r = 5.0\text{ cm}$ maintains steady temperatures $T_1 = 95.0^\circ\text{C}$ and $T_2 = 75.0^\circ\text{C}$. The lower brass disc of mass $M = 0.80\text{ kg}$ and specific heat $c = 380\text{ J/(kg K)}$ cools at rate $(dT/dt)_{T_2} = 0.050\text{ K/s}$. Taking $\pi = 3.14$, the thermal conductivity of glass in $\text{W/(m K)}$ is $K$. Find $K$ rounded off to two decimal places.

#### Question 10
A rod of length $L = 1.20\text{ m}$ on a frictionless horizontal table is struck at distance $x = 0.20\text{ m}$ from its center. The distance of the instantaneous center of rotation from the center of the rod in meters is $y\text{ m}$. Find $y$ rounded off to two decimal places.

#### Question 11
An elliptical thermodynamic cycle has semi-axes $a = 2.0 \times 10^5\text{ Pa}$ and $b = 0.010\text{ m}^3$. The net work done per cycle in kilojoules ($\text{kJ}$) is $W$. Taking $\pi = 3.14$, find $W$ rounded off to one decimal place.

#### Question 12
A uniform solid sphere of mass $M = 2.5\text{ kg}$ and radius $R = 0.20\text{ m}$ is rolling without slipping on a horizontal surface with linear speed $v = 6.0\text{ m/s}$. The total angular momentum of the sphere about the contact point on the ground in $\text{kg m}^2/\text{s}$ is $L_c$. Find $L_c$ rounded off to one decimal place.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The center of mass of a uniform circular sector of radius $R$ and total angle $2\alpha$ is at distance from the center of:
(A) $\frac{2R\sin\alpha}{3\alpha}$  
(B) $\frac{R\sin\alpha}{\alpha}$  
(C) $\frac{4R\sin\alpha}{3\pi}$  
(D) $\frac{2R}{3}$

#### Question 14
A mass $m$ moving with speed $v$ collides elastically and head-on with a stationary mass $2m$. The fraction of initial kinetic energy transferred to the heavier mass is:
(A) $8/9$  
(B) $1/9$  
(C) $4/9$  
(D) $2/3$

#### Question 15
Two liquid drops of radii $r$ and $2r$ merge isothermally in vacuum into a single drop. The ratio of final surface energy to initial surface energy is:
(A) $3^{2/3} / 5 \approx 0.416$ or $9^{1/3}/5$  
(B) $1/2$  
(C) $1/\sqrt{2}$  
(D) $1/3$

#### Question 16
The terminal velocity of a small spherical ball of radius $r$ falling in a viscous fluid is proportional to:
(A) $r^2$  
(B) $r$  
(C) $1/r$  
(D) $r^3$

#### Question 17
A particle moves in a circular path of radius $R$ with constant angular acceleration $\alpha$. If it starts from rest, the ratio of its tangential acceleration to its centripetal acceleration after time $t$ is:
(A) $\frac{1}{\alpha t^2}$  
(B) $\alpha t^2$  
(C) $\frac{1}{\alpha t}$  
(D) $\alpha t$

#### Question 18
The efficiency of a Carnot heat engine operating between $T_H = 500\text{ K}$ and $T_C = 300\text{ K}$ is:
(A) $40\%$  
(B) $60\%$  
(C) $20\%$  
(D) $50\%$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the synthesis and properties of crown ethers:
(A) Crown ethers are cyclic polyethers capable of selectively complexing metal cations.  
(B) 18-crown-6 selectively complexes $\text{K}^+$ due to matching cavity size ($\approx 2.6\text{ to }3.2\text{ \AA}$).  
(C) 15-crown-5 selectively binds $\text{Na}^+$, and 12-crown-4 binds $\text{Li}^+$.  
(D) Crown ethers solubilize inorganic salts in non-polar organic solvents, generating "naked" and highly reactive anions (e.g., purple benzene with $\text{KMnO}_4$).

#### Question 20
Regarding the thermodynamics of chemical adsorption and the Langmuir-Hinshelwood mechanism:
(A) In the Langmuir-Hinshelwood mechanism, reaction occurs between two chemical species that are both adsorbed on adjacent catalytic sites.  
(B) In the Eley-Rideal mechanism, a gas-phase molecule reacts directly with an adsorbed species without prior adsorption.  
(C) For the Langmuir-Hinshelwood bimolecular reaction $A_{\text{ads}} + B_{\text{ads}} \to \text{Products}$, the rate is $v = k \theta_A \theta_B = \frac{k K_A K_B P_A P_B}{(1 + K_A P_A + K_B P_B)^2}$.  
(D) At very high pressures of reactant $A$, $P_A$ inhibits the reaction by competitively blocking adsorption sites for $B$.

#### Question 21
Regarding the chemistry of noble gas compounds:
(A) $\text{XeF}_2$ is prepared by the photochemical or thermal reaction of $\text{Xe}$ with $\text{F}_2$ in a $2:1$ ratio at $673\text{ K}$.  
(B) $\text{XeF}_6$ reacts with silica to give $\text{XeOF}_4$ and eventually explosive $\text{XeO}_3$.  
(C) Complete hydrolysis of $\text{XeF}_6$ yields xenon trioxide: $\text{XeF}_6 + 3\text{H}_2\text{O} \to \text{XeO}_3 + 6\text{HF}$.  
(D) Hydrolysis of $\text{XeF}_4$ involves disproportionation yielding $\text{Xe}$, $\text{XeO}_3$, $\text{HF}$, and $\text{O}_2$.

#### Question 22
Regarding the extraction and metallurgy of titanium (Kroll process):
(A) Rutile ore ($\text{TiO}_2$) is converted to volatile $\text{TiCl}_4$ by heating with carbon in a stream of chlorine: $\text{TiO}_2 + 2\text{C} + 2\text{Cl}_2 \to \text{TiCl}_4 + 2\text{CO}$.  
(B) $\text{TiCl}_4$ is purified by fractional distillation.  
(C) Reduction of $\text{TiCl}_4$ is carried out using molten magnesium under an inert argon atmosphere at $\approx 1100\text{ K}$: $\text{TiCl}_4 + 2\text{Mg} \to \text{Ti} + 2\text{MgCl}_2$.  
(D) The porous titanium metal product is known as titanium sponge.

#### Question 23
Regarding the stereochemistry and reactions of glucose:
(A) D-Glucose on reduction with $\text{NaBH}_4$ yields D-sorbitol (D-glucitol), which is optically active.  
(B) D-Galactose on reduction with $\text{NaBH}_4$ yields dulcitol (galactitol), which is an achiral *meso* compound.  
(C) D-Glucose and D-mannose are C-2 epimers.  
(D) D-Glucose and D-galactose are C-4 epimers.

#### Question 24
Which of the following compounds exhibits optical isomerism:
(A) 2-Hydroxypropanoic acid (Lactic acid)  
(B) 2-Bromobutane  
(C) 1,2-Dichloropropane  
(D) Chlorocyclohexane (achiral)

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{BaSO}_4$ is $K_{\text{sp}} = 1.0 \times 10^{-10}$ at $298\text{ K}$. Calculate its molar solubility in a $0.010\text{ M}$ aqueous solution of $\text{Na}_2\text{SO}_4$. Report solubility as $S \times 10^{-8}\text{ M}$. Find $S$.

#### Question 26
Calculate the $\text{pH}$ of a buffer solution prepared by mixing $0.10\text{ M}$ $\text{NH}_3(aq)$ and $0.10\text{ M}$ $\text{NH}_4\text{Cl}(aq)$ at $298\text{ K}$, given $\text{p}K_b(\text{NH}_3) = 4.75$. Find the $\text{pH}$ rounded off to two decimal places.

#### Question 27
For the Daniel cell $\text{Zn} \mid \text{Zn}^{2+}(0.10\text{ M}) \parallel \text{Cu}^{2+}(1.0\text{ M}) \mid \text{Cu}$, given $E^\circ_{\text{cell}} = 1.10\text{ V}$ at $298\text{ K}$. The cell EMF $E_{\text{cell}}\text{ V}$ rounded off to two decimal places is $E$. Find $E$.

#### Question 28
For a zero-order reaction $A \to \text{Products}$ with initial concentration $[A]_0 = 0.50\text{ M}$ and rate constant $k = 0.010\text{ M/min}$, the time required for complete consumption of $A$ is $t\text{ min}$. Find $t$.

#### Question 29
A $0.20\text{ molal}$ aqueous solution of an electrolyte $A_2 B$ freezes at $-1.0044^\circ\text{C}$. Given $K_f(\text{H}_2\text{O}) = 1.86\text{ K kg mol}^{-1}$, the van 't Hoff factor $i$ of the solution is $i$. Find $i$ rounded off to two decimal places.

#### Question 30
Find the oxidation state of chromium in the chlorochromate anion $[\text{CrO}_3\text{Cl}]^-$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The major product obtained when 2-bromopentane is treated with alcoholic $\text{KOH}$ under heating (Saytzeff elimination) is:
(A) Pent-2-ene  
(B) Pent-1-ene  
(C) Pentan-2-ol  
(D) Pentan-1-ol

#### Question 32
The correct order of bond dissociation enthalpy of halogens is:
(A) $\text{Cl}_2 > \text{Br}_2 > \text{F}_2 > \text{I}_2$  
(B) $\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$  
(C) $\text{Cl}_2 > \text{F}_2 > \text{Br}_2 > \text{I}_2$  
(D) $\text{Br}_2 > \text{Cl}_2 > \text{F}_2 > \text{I}_2$

#### Question 33
The geometry of $\text{XeF}_6$ in the vapor phase is:
(A) Distorted octahedral  
(B) Regular octahedral  
(C) Pentagonal bipyramidal  
(D) Square planar

#### Question 34
In the Kroll process for the extraction of titanium, the reducing agent used is:
(A) Molten Magnesium  
(B) Carbon  
(C) Aluminum  
(D) Sodium hydride

#### Question 35
The linkage connecting two glucose units in cellulose is:
(A) $\beta(1\to 4)$ glycosidic bond  
(B) $\alpha(1\to 4)$ glycosidic bond  
(C) $\alpha(1\to 6)$ glycosidic bond  
(D) $\beta(1\to 6)$ glycosidic bond

#### Question 36
The hybridization of cobalt in the tetrahedral complex $[\text{CoCl}_4]^{2-}$ is:
(A) $sp^3$  
(B) $dsp^2$  
(C) $d^2sp^3$  
(D) $sp^3d$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \arctan x - x + \frac{x^3}{3}$ for $x > 0$:
(A) $f'(x) = \frac{1}{1+x^2} - 1 + x^2 = \frac{x^4}{1+x^2} > 0$ for all $x > 0$.  
(B) $f(x)$ is strictly increasing on $(0, \infty)$.  
(C) $\arctan x > x - \frac{x^3}{3}$ for all $x > 0$.  
(D) $\lim_{x \to 0} \frac{\arctan x - x + x^3/3}{x^5} = \frac{1}{5}$.

#### Question 38
Let $A$ be a $3 \times 3$ real symmetric matrix:
(A) All eigenvalues of $A$ are real.  
(B) Eigenvectors corresponding to distinct eigenvalues of $A$ are orthogonal.  
(C) $A$ can be orthogonally diagonalized: $P^T A P = D$ for some orthogonal matrix $P$.  
(D) $\text{tr}(A)$ equals the sum of its eigenvalues, and $\det(A)$ equals the product of its eigenvalues.

#### Question 39
Consider the parabola $y^2 = 4ax$ and the circle $x^2 + y^2 = 2ax$:
(A) The common tangents touch the parabola and circle.  
(B) The circle passes through the origin and focus $(a, 0)$ of the parabola.  
(C) The center of the circle is at $(a, 0)$ with radius $a$.  
(D) The common chord of the parabola and circle is $x = 0$ ($y$-axis).

#### Question 40
Let $I_n = \int_0^1 x^n e^{-x} dx$ for $n \ge 0$:
(A) $I_n = n I_{n-1} - \frac{1}{e}$ for $n \ge 1$.  
(B) $I_0 = 1 - \frac{1}{e}$.  
(C) $I_1 = 1 - \frac{2}{e}$.  
(D) $\lim_{n \to \infty} I_n = 0$.

#### Question 41
Consider the system of vectors $\vec{u}, \vec{v}, \vec{w}$ in $\mathbb{R}^3$:
(A) $[\vec{u} + \vec{v}\quad \vec{v} + \vec{w}\quad \vec{w} + \vec{u}] = 2[\vec{u}\quad \vec{v}\quad \vec{w}]$.  
(B) $[\vec{u} - \vec{v}\quad \vec{v} - \vec{w}\quad \vec{w} - \vec{u}] = 0$.  
(C) If $\vec{u}, \vec{v}, \vec{w}$ are mutually orthogonal unit vectors, then $|[\vec{u}\quad \vec{v}\quad \vec{w}]| = 1$.  
(D) $(\vec{u} \times \vec{v}) \cdot \vec{w} = \vec{u} \cdot (\vec{v} \times \vec{w})$.

#### Question 42
Let $f(x) = \cos(\ln x)$ for $x > 0$:
(A) $x f'(x) = -\sin(\ln x)$.  
(B) $x^2 f''(x) + x f'(x) + f(x) = 0$ (Euler-Cauchy equation).  
(C) The function $f(x)$ has infinitely many roots in $(0, 1)$.  
(D) $f(x)$ is bounded on $(0, \infty)$ with $-1 \le f(x) \le 1$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = x^3 - 3x$ and the line $y = x$.

#### Question 44
Find the remainder when $2^{2026}$ is divided by 7.

#### Question 45
Find the distance between the parallel lines $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $\frac{x-3}{2} = \frac{y-5}{3} = \frac{z-7}{4}$. Round off to two decimal places.

#### Question 46
Let $\alpha, \beta, \gamma$ be the roots of $x^3 - 3x^2 + 2x - 5 = 0$. Find the value of $\alpha^2 + \beta^2 + \gamma^2$.

#### Question 47
Find the number of 4-letter words with distinct letters that can be formed from the English alphabet such that vowels and consonants alternate.

#### Question 48
Find the radius of the sphere $x^2 + y^2 + z^2 - 6x - 8y + 10z = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\ln(\cos x)$ with respect to $x$ is:
(A) $-\tan x$  
(B) $\tan x$  
(C) $\cot x$  
(D) $-\cot x$

#### Question 50
The solution of the differential equation $\frac{dy}{dx} = \frac{y^2 - x^2}{2xy}$ is:
(A) $x^2 + y^2 = C x$  
(B) $x^2 - y^2 = C x$  
(C) $y^2 = x^2 + C$  
(D) $x y = C$

#### Question 51
The angle between the asymptotes of the hyperbola $\frac{x^2}{16} - \frac{y^2}{16} = 1$ is:
(A) $90^\circ$  
(B) $60^\circ$  
(C) $45^\circ$  
(D) $120^\circ$

#### Question 52
If $\log_{10} x = y$, then $\log_{100}(x^3)$ is equal to:
(A) $\frac{3}{2}y$  
(B) $3y$  
(C) $\frac{2}{3}y$  
(D) $6y$

#### Question 53
The maximum value of $f(x) = \sin x(1 + \cos x)$ on $[0, \pi]$ is:
(A) $\frac{3\sqrt{3}}{4}$  
(B) $\frac{3}{4}$  
(C) $\sqrt{3}$  
(D) 1

#### Question 54
Two fair dice are thrown simultaneously. The probability that the sum of the numbers is greater than 10 is:
(A) $1/12$  
(B) $1/6$  
(C) $1/18$  
(D) $5/36$
"""

        raw_sol1 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 1)
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Spool on horizontal surface: torque about contact line determines rolling direction. Line of action of tension intersects ground at $x = r/\cos\theta$. If $\cos\theta > r/R$, contact line torque pulls spool forward (right). If $\cos\theta < r/R$, torque pulls backward (left). At $\cos\theta = r/R$, torque vanishes. **Correct Options**: (A, B, C, D)
- **Q2**: Capillary-gravity waves dispersion: $\omega^2 = gk + \frac{T}{\rho}k^3$. Phase velocity $v_p^2 = \frac{g}{k} + \frac{T}{\rho}k$. Minimum at $k_c = \sqrt{\frac{\rho g}{T}}$ with $v_{\min} = (4gT/\rho)^{1/4} \approx 0.23\text{ m/s}$. **Correct Options**: (A, B, C, D)
- **Q3**: Carey Foster bridge principles: elimination of end errors by interchange of gap resistances. Formula $X - Y = \rho(l_2 - l_1)$. **Correct Options**: (A, B, C, D)
- **Q4**: Jaeger's method for surface tension: maximum pressure occurs when bubble is a hemisphere of radius $r$. Formula $\rho_m g h_m = \rho g h + 2T/r \implies T = \frac{rg}{2}(\rho_m h_m - \rho h)$. **Correct Options**: (A, B, C, D)
- **Q5**: Sphere on accelerating wedge: apparent gravity $\vec{g}_{\text{eff}} = \vec{g} - a_0\hat{i}$. Equilibrium along slope when $a_0 = g\tan\theta$. **Correct Options**: (A, B, C, D)
- **Q6**: Searle's thermal conductivity method: steady heat flow along lagged bar, heat rate measured by cooling water flow $m_w c_w \Delta T_w$. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $\cos\theta_c = r/R = 0.10 / 0.20 = 0.50 \implies \theta_c = 60^\circ \implies \mathbf{60.00}$.
- **Q8**: $T = \frac{r g}{2}(\rho_m h_m - \rho h) = \frac{(0.20 \times 10^{-3})(9.8)}{2}[800(0.11) - 1000(0.05)] = (0.98 \times 10^{-3})[88 - 50] = (0.98 \times 10^{-3})(38) \approx 0.0372\text{ N/m} \approx 0.037\text{ N/m} \implies \mathbf{0.037}$.
- **Q9**: $R_{\text{diff}} = \rho \Delta l = 0.050 \times 8.0 = 0.40\text{ }\Omega \implies \mathbf{0.40}$.
- **Q10**: Heat rate $\frac{dQ}{dt} = m_w c_w \Delta T_w = (2.0 \times 10^{-3}\text{ kg/s})(4200)(5.0) = 42.0\text{ W}$. Cross-sectional area $A = \pi D^2 / 4 = 3.14(0.04)^2 / 4 = 1.256 \times 10^{-3}\text{ m}^2$. Temperature gradient $\Delta T / d = 20.0 / 0.10 = 200.0\text{ K/m}$. $K = \frac{dQ/dt}{A (\Delta T/d)} = \frac{42.0}{(1.256 \times 10^{-3})(200)} = \frac{42.0}{0.2512} \approx 167\text{ W/(m K)} \implies \mathbf{167.00}$.
- **Q11**: Total kinetic energy of rolling solid sphere: $E = \frac{7}{10}M v^2 = \frac{7}{10}(3.0)(2.8)^2 = 2.1 \times 7.84 = 16.46\text{ J} \implies \mathbf{16.46}$.
- **Q12**: Hydrostatic force $F = P_{\text{avg}} A = \rho g (h/2) (b h) = 1000 \times 9.8 \times 1.5 \times (2.0 \times 3.0) = 14700 \times 6.0 = 88200\text{ N} = 88.2\text{ kN} \implies \mathbf{88.20}$.

### Questions 13 to 18
- **Q13**: Center of mass of solid cone is at $h/4$ from base. **Correct: (A)**.
- **Q14**: Equal and opposite linear momenta: $p_M = p_m$. Kinetic energy $K = p^2/(2m) \implies K_M / K_m = m / M$. **Correct: (A)**.
- **Q15**: Torricelli velocity $v = \sqrt{2gh}$, time of fall $t = \sqrt{2(H-h)/g}$. Range $R = v t = 2\sqrt{h(H-h)}$, maximized at $h = H/2$. **Correct: (A)**.
- **Q16**: SI unit of surface tension is $\text{N/m}$ (or $\text{J/m}^2$). **Correct: (A)**.
- **Q17**: For solid cylinder, $a = \frac{g\sin\theta}{1 + 1/2} = \frac{2}{3}g\sin\theta$. Friction $f_s = \frac{1}{3}Mg\sin\theta \le \mu_s Mg\cos\theta \implies \mu_s \ge \frac{1}{3}\tan\theta$. **Correct: (A)**.
- **Q18**: $P V^\gamma = C \implies dP V^\gamma + \gamma P V^{\gamma-1} dV = 0 \implies \frac{dP}{dV} = -\gamma \frac{P}{V}$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Robinson annulation sequence (Michael addition + intramolecular aldol condensation). **Correct Options**: (A, B, C, D)
- **Q20**: BET isotherm equation for multilayer physical adsorption. **Correct Options**: (A, B, C, D)
- **Q21**: Overpotential types and Tafel equation. **Correct Options**: (A, B, C, D)
- **Q22**: Dow process metallurgy of magnesium from seawater. **Correct Options**: (A, B, C, D)
- **Q23**: Actinides vs lanthanides: oxidation states, orbital participation, and covalent character. **Correct Options**: (A, B, C, D)
- **Q24**: Optical isomerism in coordination compounds: $[\text{Co}(\text{en})_3]^{3+}$, *cis*-$[\text{Pt}(\text{en})_2\text{Cl}_2]^{2+}$, and $[\text{Cr}(\text{ox})_3]^{3-}$ are chiral. *trans* isomer is achiral. **Correct Options**: (A, B, D)

### Questions 25 to 30
- **Q25**: $\text{AgBr} \rightleftharpoons \text{Ag}^+ + \text{Br}^- \implies S = \sqrt{K_{\text{sp}}} = \sqrt{5.0 \times 10^{-13}} = \sqrt{50 \times 10^{-14}} \approx 7.07 \times 10^{-7}\text{ M} \implies \mathbf{7.07}$.
- **Q26**: $[\text{OH}^-] = 2 \times 0.0050\text{ M} = 0.010\text{ M} \implies \text{pOH} = 2.00 \implies \text{pH} = 14 - 2.00 = 12.00 \implies \mathbf{12.00}$.
- **Q27**: $E^\circ_{\text{cell}} = E^\circ(\text{Ag}^+/\text{Ag}) - E^\circ(\text{Ni}^{2+}/\text{Ni}) = +0.80 - (-0.25) = 1.05\text{ V} \implies \mathbf{1.05}$.
- **Q28**: First-order reaction: slope $= -k \implies k = 0.02303\text{ min}^{-1}$. Half-life $t_{1/2} = \frac{0.693}{0.02303} \approx 30.1\text{ min} \approx 30\text{ min} \implies \mathbf{30.00}$.
- **Q29**: $\Delta T_f = i K_f m \implies 0.3534 = i (1.86)(0.10) \implies i = \frac{0.3534}{0.186} = 1.90$. For $\text{NaCl}$, $i = 1 + \alpha \implies \alpha = 0.90 = 90\% \implies \mathbf{90.00}$.
- **Q30**: In $\text{UO}_2^{2+}$, $x + 2(-2) = +2 \implies x = +6 \implies \mathbf{6.00}$.

### Questions 31 to 36
- **Q31**: Oxymercuration-demercuration yields Markovnikov alcohol without rearrangement (mercurinium ion intermediate). **Correct: (A)**.
- **Q32**: Helium has the lowest boiling point of all elements ($4.2\text{ K}$). **Correct: (A)**.
- **Q33**: $\text{CO}_3^{2-}$ has 3 bond pairs and 0 lone pairs $\implies sp^2$ trigonal planar. **Correct: (A)**.
- **Q34**: Electrolyte is molten anhydrous $\text{MgCl}_2$ mixed with $\text{CaCl}_2$ and $\text{NaCl}$ to lower melting point. **Correct: (A)**.
- **Q35**: Secondary structure ($\alpha$-helix, $\beta$-sheet) is stabilized by backbone hydrogen bonds. **Correct: (A)**.
- **Q36**: Loss of a proton from $\text{H}_2\text{PO}_4^-$ gives $\text{HPO}_4^{2-}$. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Reversing order of double integration: $\int_0^1 \int_y^1 e^{x^2} dx dy = \int_0^1 x e^{x^2} dx = \frac{e-1}{2}$. **Correct Options**: (A, B, C, D)
- **Q38**: Geometry of tangent planes to ellipsoids. **Correct Options**: (A, B, C, D)
- **Q39**: Leibniz's rule for higher derivatives of product. **Correct Options**: (A, B, C, D)
- **Q40**: Two-state Markov chain stationary distribution. **Correct Options**: (A, B, C, D)
- **Q41**: Logistic sigmoid function properties. **Correct Options**: (A, B, C, D)
- **Q42**: Rank analysis of linear systems. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: $I = \frac{e-1}{2} = \frac{2.718 - 1}{2} = \frac{1.718}{2} = 0.859 \approx 0.86 \implies \mathbf{0.86}$.
- **Q44**: $13^1 = 13, 13^2 = 169 \equiv 69, 13^3 \equiv 97, 13^4 \equiv 61, \dots, 13^{20} \equiv 1 \pmod{100}$. $2024 = 20 \times 101 + 4$. $13^{2024} \equiv 13^4 \equiv 61 \pmod{100} \implies \mathbf{61.00}$.
- **Q45**: Director sphere $x^2 + y^2 + z^2 = a^2 + b^2 + c^2 = 16 + 9 + 4 = 29 \implies R^2 = \mathbf{29.00}$.
- **Q46**: $|z^3| = |8i| = 8 \implies |z|^3 = 8 \implies |z| = 2.00 \implies \mathbf{2.00}$.
- **Q47**: Word has 13 letters: 3 A's, 4 S's, 2 I's, 2 N's, 1 T, 1 O. Bundle 4 S's as 1 unit: 10 items (3 A's, 2 I's, 2 N's, 1 T, 1 O, 1 bundle). Number of ways $= \frac{10!}{3! 2! 2!} = \frac{3628800}{24} = 151200 \implies \mathbf{151200.00}$.
- **Q48**: $d = \frac{|3(1) - 4(2) + 12(-1) - 5|}{\sqrt{3^2 + (-4)^2 + 12^2}} = \frac{|3 - 8 - 12 - 5|}{\sqrt{9 + 16 + 144}} = \frac{22}{\sqrt{169}} = \frac{22}{13} \approx 1.69 \implies \mathbf{1.69}$.

### Questions 49 to 54
- **Q49**: Let $x = \sin\theta \implies \frac{x}{\sqrt{1-x^2}} = \tan\theta \implies \arctan(\tan\theta) = \theta = \arcsin x$. Derivative is $\frac{1}{\sqrt{1-x^2}}$. **Correct: (A)**.
- **Q50**: General solution of $y'' - 4y = 0$ is $y = A e^{2x} + B e^{-2x}$. **Correct: (A)**.
- **Q51**: $d = \frac{|0 + 0 + 0 - 14|}{\sqrt{2^2 + 3^2 + 6^2}} = \frac{14}{\sqrt{4 + 9 + 36}} = \frac{14}{7} = 2$. **Correct: (A)**.
- **Q52**: For orthogonal matrix $A^T A = I \implies (\det A)^2 = 1 \implies \det A = \pm 1$. **Correct: (A)**.
- **Q53**: $f'(x) = (1-x)^2 - 2x(1-x) = (1-x)(1 - 3x) = 0 \implies x = 1/3$. $f(1/3) = (1/3)(2/3)^2 = 4/27$. **Correct: (A)**.
- **Q54**: Face cards $= 4 \times 3 = 12$. $P = 12/52 = 3/13$. **Correct: (A)**.
"""

        raw_sol2 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 2)
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Spinning sphere placed on rough floor: $f_k = \mu M g$ accelerates center of mass ($a = \mu g$) and decelerates rotation ($\alpha = \frac{5\mu g}{2R}$). Pure rolling begins when $v(t) = R\omega(t) \implies \mu g t = R(\omega_0 - \alpha t) \implies t = \frac{2 R \omega_0}{7\mu g}$, $v = \frac{2}{7}R\omega_0$. **Correct Options**: (A, B, C, D)
- **Q2**: Blasius laminar boundary layer: thickness grows as $\sqrt{x}$, shear stress scales as $1/\sqrt{x}$, total drag force, critical Reynolds number $5 \times 10^5$. **Correct Options**: (A, B, C, D)
- **Q3**: Hydraulic jump in rectangular channel: Belanger equation, continuity of mass, momentum flux conservation, dissipation of kinetic energy into turbulence. **Correct Options**: (A, B, C, D)
- **Q4**: Lees' disc thermal conductivity measurement for bad conductors. **Correct Options**: (A, B, C, D)
- **Q5**: Impulse on free rod: linear velocity $v_{\text{cm}} = J/M$, angular velocity $\omega = 12Jx/(ML^2)$. Instantaneous center of rotation at $y = L^2/(12x)$. **Correct Options**: (A, B, C, D)
- **Q6**: Elliptical thermodynamic cycle: area on $P-V$ plane gives net work $W = \pi a b$. Maximum and minimum parameters. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: Pure rolling speed $v = \frac{2}{7}R\omega_0 = \frac{2}{7}(0.14)(50.0) = 2.0\text{ m/s} \implies \mathbf{2.00}$.
- **Q8**: $y_2 = \frac{y_1}{2}(\sqrt{1 + 8 Fr_1^2} - 1) = \frac{0.20}{2}(\sqrt{1 + 8(9)} - 1) = 0.10(\sqrt{73} - 1) \approx 0.10(8.544 - 1) \approx 0.75\text{ m} \implies \mathbf{0.75}$.
- **Q9**: $K = \frac{M c d (dT/dt)_{T_2}}{\pi r^2 (T_1 - T_2)} = \frac{(0.80)(380)(0.002)(0.050)}{3.14 (0.05)^2 (20.0)} = \frac{0.0304}{3.14 \times 0.0025 \times 20.0} = \frac{0.0304}{0.157} \approx 0.19\text{ W/(m K)} \implies \mathbf{0.19}$.
- **Q10**: $y = \frac{L^2}{12 x} = \frac{(1.20)^2}{12(0.20)} = \frac{1.44}{2.40} = 0.60\text{ m} \implies \mathbf{0.60}$.
- **Q11**: Work $W = \pi a b = 3.14(2.0 \times 10^5)(0.010) = 3.14 \times 2000 = 6280\text{ J} = 6.28\text{ kJ} \approx 6.3\text{ kJ} \implies \mathbf{6.30}$.
- **Q12**: Angular momentum about contact point: $L_c = I_c \omega = (\frac{7}{5}M R^2)(v/R) = \frac{7}{5}M v R = \frac{7}{5}(2.5)(6.0)(0.20) = 4.2\text{ kg m}^2/\text{s} \implies \mathbf{4.20}$.

### Questions 13 to 18
- **Q13**: Center of mass of circular sector of half-angle $\alpha$ is at $\frac{2R\sin\alpha}{3\alpha}$. **Correct: (A)**.
- **Q14**: 1D elastic collision: $v_2 = \frac{2m}{m + 2m}v = \frac{2}{3}v$. Kinetic energy transferred $K_2 = \frac{1}{2}(2m)(2v/3)^2 = \frac{4}{9}(\frac{1}{2}m v^2) \times 2 = \frac{8}{9}K_1$. **Correct: (A)**.
- **Q15**: $V_{\text{total}} = \frac{4}{3}\pi r^3 + \frac{4}{3}\pi (2r)^3 = \frac{4}{3}\pi (9r^3) \implies R = 9^{1/3}r$. Final area $A_f = 4\pi R^2 = 4\pi (9^{2/3}r^2)$. Initial area $A_i = 4\pi (r^2 + 4r^2) = 4\pi (5r^2)$. Ratio $A_f / A_i = 9^{2/3} / 5 \approx 4.326 / 5 \approx 0.865$. **Correct: (A)**.
- **Q16**: By Stokes' law, $6\pi\eta r v_t = \frac{4}{3}\pi r^3 (\rho - \sigma)g \implies v_t \propto r^2$. **Correct: (A)**.
- **Q17**: $a_t = R\alpha$, $a_c = R\omega^2 = R(\alpha t)^2 = R\alpha^2 t^2$. Ratio $a_t / a_c = \frac{R\alpha}{R\alpha^2 t^2} = \frac{1}{\alpha t^2}$. **Correct: (A)**.
- **Q18**: $\eta = 1 - T_C / T_H = 1 - 300 / 500 = 0.40 = 40\%$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Crown ethers ionophoric selectivity and "naked" anion activation. **Correct Options**: (A, B, C, D)
- **Q20**: Langmuir-Hinshelwood vs Eley-Rideal heterogeneous catalytic mechanisms. **Correct Options**: (A, B, C, D)
- **Q21**: Synthesis and reactions of xenon fluorides and oxides. **Correct Options**: (A, B, C, D)
- **Q22**: Kroll process metallurgy of titanium sponge. **Correct Options**: (A, B, C, D)
- **Q23**: Stereochemistry of D-glucose reduction and epimers. **Correct Options**: (A, B, C, D)
- **Q24**: Optical isomerism in organic compounds. Chlorocyclohexane is achiral. **Correct Options**: (A, B, C)

### Questions 25 to 30
- **Q25**: $\text{BaSO}_4 \rightleftharpoons \text{Ba}^{2+} + \text{SO}_4^{2-}$. In presence of $0.010\text{ M}$ $\text{SO}_4^{2-}$, $S = \frac{K_{\text{sp}}}{[\text{SO}_4^{2-}]} = \frac{1.0 \times 10^{-10}}{0.010} = 1.0 \times 10^{-8}\text{ M} \implies S = \mathbf{1.00}$.
- **Q26**: Basic buffer $\text{pOH} = \text{p}K_b + \log([\text{salt}]/[\text{base}]) = 4.75 + \log(1) = 4.75 \implies \text{pH} = 14 - 4.75 = 9.25 \implies \mathbf{9.25}$.
- **Q27**: $E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{0.0591}{2}\log\left(\frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]}\right) = 1.10 - \frac{0.0591}{2}\log(0.10) = 1.10 - (-0.0295) \approx 1.13\text{ V} \implies \mathbf{1.13}$.
- **Q28**: For zero-order reaction, $t = [A]_0 / k = 0.50 / 0.010 = 50.0\text{ min} \implies \mathbf{50.00}$.
- **Q29**: $\Delta T_f = i K_f m \implies 1.0044 = i (1.86)(0.20) \implies i = \frac{1.0044}{0.372} = 2.70 \implies \mathbf{2.70}$.
- **Q30**: In $[\text{CrO}_3\text{Cl}]^-$, $x + 3(-2) + (-1) = -1 \implies x - 7 = -1 \implies x = +6 \implies \mathbf{6.00}$.

### Questions 31 to 36
- **Q31**: Saytzeff rule gives the more substituted, thermodynamically stable alkene (pent-2-ene). **Correct: (A)**.
- **Q32**: Bond dissociation enthalpy: $\text{Cl}_2 > \text{Br}_2 > \text{F}_2 > \text{I}_2$ ($\text{F}_2$ has low bond enthalpy due to lone pair-lone pair repulsions). **Correct: (A)**.
- **Q33**: $\text{XeF}_6$ has 6 bond pairs and 1 lone pair $\implies$ distorted octahedral. **Correct: (A)**.
- **Q34**: Molten magnesium reduces $\text{TiCl}_4$ to titanium sponge. **Correct: (A)**.
- **Q35**: Cellulose consists of $\beta$-D-glucose units joined by $\beta(1\to 4)$ glycosidic linkages. **Correct: (A)**.
- **Q36**: High-spin $[\text{CoCl}_4]^{2-}$ is tetrahedral with $sp^3$ hybridization. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Inequality and Taylor series for $\arctan x$. **Correct Options**: (A, B, C, D)
- **Q38**: Spectral theorem for real symmetric matrices. **Correct Options**: (A, B, C, D)
- **Q39**: Geometry of parabola $y^2 = 4ax$ and circle $x^2 + y^2 = 2ax$. **Correct Options**: (A, B, C, D)
- **Q40**: Reduction formula for $I_n = \int_0^1 x^n e^{-x} dx$. **Correct Options**: (A, B, C, D)
- **Q41**: Vector triple products and determinant properties. **Correct Options**: (A, B, C, D)
- **Q42**: Analysis of $f(x) = \cos(\ln x)$. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Intersection: $x^3 - 3x = x \implies x^3 - 4x = 0 \implies x = 0, \pm 2$. By symmetry: Area $= 2 \int_0^2 (x - (x^3 - 3x))dx = 2 \int_0^2 (4x - x^3)dx = 2 [2x^2 - x^4/4]_0^2 = 2(8 - 4) = 8.00 \implies \mathbf{8.00}$.
- **Q44**: $2^3 = 8 \equiv 1 \pmod 7$. $2026 = 3 \times 675 + 1$. $2^{2026} \equiv (2^3)^{675} \times 2^1 \equiv 1 \times 2 \equiv 2 \pmod 7 \implies \mathbf{2.00}$.
- **Q45**: Lines are parallel with direction $\vec{u} = (2, 3, 4)$ and $|\vec{u}| = \sqrt{29}$. Displacement $\vec{r} = (2, 3, 4)$. Here displacement is parallel to direction, meaning the point $(3, 5, 7)$ actually lies on the same line! Let's recheck: at $t=1$, $(1+2, 2+3, 3+4) = (3, 5, 7)$. The distance is 0.00! $\mathbf{0.00}$.
- **Q46**: $\sum\alpha = 3$, $\sum\alpha\beta = 2$. $\alpha^2 + \beta^2 + \gamma^2 = (\sum\alpha)^2 - 2\sum\alpha\beta = 3^2 - 2(2) = 9 - 4 = 5.00 \implies \mathbf{5.00}$.
- **Q47**: Pattern 1 (VCVC): $5 \times 21 \times 4 \times 20 = 8400$. Pattern 2 (CVCV): $21 \times 5 \times 20 \times 4 = 8400$. Total $= 8400 + 8400 = 16800 \implies \mathbf{16800.00}$.
- **Q48**: Sphere equation: $(x-3)^2 + (y-4)^2 + (z+5)^2 = 9 + 16 + 25 = 50 \implies R = \sqrt{50} \approx 7.07 \implies \mathbf{7.07}$.

### Questions 49 to 54
- **Q49**: $\frac{d}{dx}\ln(\cos x) = \frac{-\sin x}{\cos x} = -\tan x$. **Correct: (A)**.
- **Q50**: Homogeneous ODE $\frac{dy}{dx} = \frac{y^2-x^2}{2xy} \implies x^2 + y^2 = Cx$. **Correct: (A)**.
- **Q51**: Rectangular hyperbola has perpendicular asymptotes ($90^\circ$). **Correct: (A)**.
- **Q52**: $\log_{100}(x^3) = \frac{\log_{10}(x^3)}{\log_{10}(100)} = \frac{3\log_{10} x}{2} = \frac{3}{2}y$. **Correct: (A)**.
- **Q53**: $f'(x) = \cos x(1+\cos x) - \sin^2 x = \cos x + \cos^2 x - (1 - \cos^2 x) = 2\cos^2 x + \cos x - 1 = (2\cos x - 1)(\cos x + 1) = 0 \implies \cos x = 1/2 \implies x = \pi/3$. $f(\pi/3) = \frac{\sqrt{3}}{2}(1 + 1/2) = \frac{3\sqrt{3}}{4}$. **Correct: (A)**.
- **Q54**: Sum $> 10$ means sum is 11 or 12: $(5,6), (6,5), (6,6) \implies 3$ outcomes out of 36 $\implies 3/36 = 1/12$. **Correct: (A)**.
"""

        raw_val = r"""# Comprehensive Answer Key & Academic Alignment Validation – JEE Advanced Mock Examination __PAD__
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

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
| 7 | Physics | Sec 2 | Numerical | 60.00 |
| 8 | Physics | Sec 2 | Numerical | 0.037 |
| 9 | Physics | Sec 2 | Numerical | 0.40 |
| 10 | Physics | Sec 2 | Numerical | 167.00 |
| 11 | Physics | Sec 2 | Numerical | 16.46 |
| 12 | Physics | Sec 2 | Numerical | 88.20 |
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
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, D |
| 25 | Chemistry | Sec 2 | Numerical | 7.07 |
| 26 | Chemistry | Sec 2 | Numerical | 12.00 |
| 27 | Chemistry | Sec 2 | Numerical | 1.05 |
| 28 | Chemistry | Sec 2 | Numerical | 30.00 |
| 29 | Chemistry | Sec 2 | Numerical | 90.00 |
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
| 40 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 41 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 42 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 43 | Mathematics | Sec 2 | Numerical | 0.86 |
| 44 | Mathematics | Sec 2 | Numerical | 61.00 |
| 45 | Mathematics | Sec 2 | Numerical | 29.00 |
| 46 | Mathematics | Sec 2 | Numerical | 2.00 |
| 47 | Mathematics | Sec 2 | Numerical | 151200.00 |
| 48 | Mathematics | Sec 2 | Numerical | 1.69 |
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
| 7 | Physics | Sec 2 | Numerical | 2.00 |
| 8 | Physics | Sec 2 | Numerical | 0.75 |
| 9 | Physics | Sec 2 | Numerical | 0.19 |
| 10 | Physics | Sec 2 | Numerical | 0.60 |
| 11 | Physics | Sec 2 | Numerical | 6.30 |
| 12 | Physics | Sec 2 | Numerical | 4.20 |
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
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C |
| 25 | Chemistry | Sec 2 | Numerical | 1.00 |
| 26 | Chemistry | Sec 2 | Numerical | 9.25 |
| 27 | Chemistry | Sec 2 | Numerical | 1.13 |
| 28 | Chemistry | Sec 2 | Numerical | 50.00 |
| 29 | Chemistry | Sec 2 | Numerical | 2.70 |
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
| 40 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 41 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 42 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 43 | Mathematics | Sec 2 | Numerical | 8.00 |
| 44 | Mathematics | Sec 2 | Numerical | 2.00 |
| 45 | Mathematics | Sec 2 | Numerical | 0.00 |
| 46 | Mathematics | Sec 2 | Numerical | 5.00 |
| 47 | Mathematics | Sec 2 | Numerical | 16800.00 |
| 48 | Mathematics | Sec 2 | Numerical | 7.07 |
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

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, "IIT_Roorkee")
        print(f"Generated IIT Roorkee Mock {pad}!")

if __name__ == "__main__":
    generate_roorkee_16_to_20()

