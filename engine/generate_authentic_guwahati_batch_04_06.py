# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Batch Generator for IIT Guwahati Mocks 04, 05, 06.
Calibrated strictly to IIT Guwahati empirical signature (2009, 2016, 2023):
- High Modern Physics (photoelectric, relativistic de Broglie, Moseley, cavity radiation, Compton)
- High Thermodynamics & Statistical Mechanics (Stirling, Carnot, van der Waals, Joule-Thomson)
- High Physical Chemistry (electrochemistry, chemical equilibria, kinetics, phase transitions)
- Clean Organic Synthesis with unambiguous stereochemistry (Diels-Alder, pinacol, ozonolysis)
- Geometric Elegance in Conics, Vectors, Argand Plane, and Definite Integrals
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

def generate_guwahati_04():
    p1 = r"""# JEE Advanced Mock Examination 04 – Paper 1
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
An ideal gas undergoes a cycle on the $P-V$ diagram consisting of an isothermal expansion at $T_H$ from $V_0$ to $2V_0$, an isobaric compression to $V_0$, and an isochoric heating to initial state. If $\gamma = 5/3$:
(A) The temperature of the lowest temperature state is $T_H/2$.  
(B) The net work done by the gas in one cycle is $R T_H (\ln 2 - 0.5)$.  
(C) The efficiency of the cycle is strictly less than that of a Carnot engine operating between $T_H$ and $T_H/2$.  
(D) The net entropy change of the working gas over a complete cycle is zero.

#### Question 2
In an experiment on the photoelectric effect, stopping potential $V_s$ is measured as a function of incident light frequency $\nu$:
(A) The slope of the $V_s$ vs $\nu$ graph is $\frac{h}{e}$, a universal constant.  
(B) The horizontal intercept of the graph gives the threshold frequency $\nu_0 = \Phi / h$.  
(C) Doubling the intensity of the incident light doubles the saturation photocurrent without changing $V_s$.  
(D) The stopping potential depends on the distance between the source and the cathode.

#### Question 3
A particle of mass $m$ moves in a circular orbit of radius $r_0$ under an attractive central force $F(r) = -\frac{k}{r^3}$ ($k > 0$):
(A) The orbital angular momentum $L$ is conserved.  
(B) The total mechanical energy $E$ in the circular orbit is zero.  
(C) The kinetic energy equals the magnitude of the potential energy ($U = -\frac{k}{2r^2}$).  
(D) The circular orbit is in neutral equilibrium with respect to small radial perturbations.

#### Question 4
A parallel-plate capacitor with air between its plates has capacitance $C_0$. It is connected to a battery of voltage $V$ and then disconnected. A dielectric slab of dielectric constant $\kappa = 3$ is inserted to fill half the volume between the plates:
(A) If the slab fills half the area across the full separation $d$, the new capacitance is $2 C_0$.  
(B) If the slab fills the full area across half the thickness $d/2$, the new capacitance is $1.5 C_0$.  
(C) The electric field inside the dielectric region is less than in the air region.  
(D) The potential difference between the plates decreases in both cases.

#### Question 5
A conducting rod of length $L$ and mass $m$ slides frictionlessly along two horizontal parallel conducting rails separated by distance $L$ in a uniform vertical magnetic field $B$. The rails are connected by a resistor $R$. An initial velocity $v_0$ is imparted to the rod:
(A) The velocity of the rod decays exponentially as $v(t) = v_0 e^{-B^2 L^2 t / (m R)}$.  
(B) The total distance traveled by the rod before coming to rest is $x_{\infty} = \frac{m v_0 R}{B^2 L^2}$.  
(C) The total electrical energy dissipated in the resistor equals the initial kinetic energy $\frac{1}{2}m v_0^2$.  
(D) The induced current in the rod flows in such a direction as to oppose its motion (Lenz's law).

#### Question 6
Regarding electromagnetic radiation from an accelerating point charge $q$ with non-relativistic acceleration $a$:
(A) The total radiated power is given by Larmor's formula $P = \frac{q^2 a^2}{6\pi \varepsilon_0 c^3}$.  
(B) The angular distribution of radiated power varies as $\sin^2\theta$, where $\theta$ is the angle between the acceleration and radiation direction.  
(C) No radiation is emitted along the line of acceleration ($\theta = 0$ and $\theta = \pi$).  
(D) The electric field in the radiation zone decreases as $1/r$ with distance $r$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A monoatomic ideal gas ($\gamma = 5/3$) undergoes a polytropic expansion according to $P V^3 = \text{constant}$. Find the molar heat capacity $C$ of the gas during this process in units of $R$. (Round off to two decimal places).

#### Question 8
In an X-ray tube, electrons are accelerated through a potential difference $V = 25.0\text{ kV}$. Calculate the minimum wavelength $\lambda_{\min}$ of the continuous X-rays in picometers ($\text{pm}$). (Take $h c \approx 1240\text{ eV}\cdot\text{nm}$. Round off to two decimal places).

#### Question 9
A uniform solid sphere of mass $M = 3.5\text{ kg}$ and radius $R = 0.20\text{ m}$ rolls without slipping on a horizontal plane with velocity $v = 4.0\text{ m/s}$. Find its total kinetic energy in Joules. (Round off to two decimal places).

#### Question 10
In a series LCR circuit at resonance, $L = 0.20\text{ H}$, $C = 5.0\ \mu\text{F}$, and $R = 20\ \Omega$. Find the quality factor $Q$ of the circuit. (Round off to two decimal places).

#### Question 11
Two coherent sound sources emit waves of wavelength $\lambda = 0.80\text{ m}$. A point $P$ is at distance $d_1 = 4.20\text{ m}$ from source 1 and $d_2 = 5.40\text{ m}$ from source 2. Calculate the phase difference $\Delta \phi$ between the two waves arriving at $P$ in radians. (Take $\pi \approx 3.1416$. Round off to two decimal places).

#### Question 12
A simple pendulum has period $T = 2.00\text{ s}$ at Earth's surface. What is its period in seconds inside an elevator accelerating upwards with acceleration $a = g/3$? (Round off to two decimal places).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle moves in a potential $V(x) = V_0 [1 - \cos(\alpha x)]$. For small displacements about $x = 0$, the frequency of oscillation is:
(A) $\omega = \alpha \sqrt{\frac{V_0}{m}}$  
(B) $\omega = \sqrt{\frac{V_0}{m \alpha^2}}$  
(C) $\omega = 2\alpha \sqrt{\frac{V_0}{m}}$  
(D) $\omega = \frac{\alpha}{2}\sqrt{\frac{V_0}{m}}$

#### Question 14
Two concentric conducting spheres of radii $a$ and $b$ ($b > a$) have charge $+Q$ on the inner sphere while the outer sphere is connected to earth. The capacitance of the system is:
(A) $4\pi\varepsilon_0 \frac{a b}{b - a}$  
(B) $4\pi\varepsilon_0 \frac{a b}{b + a}$  
(C) $4\pi\varepsilon_0 a$  
(D) $4\pi\varepsilon_0 b$

#### Question 15
In a single-slit Fraunhofer diffraction pattern, the first diffraction minimum occurs at an angle of $30^\circ$ for light of wavelength $600\text{ nm}$. The width of the slit is:
(A) $1.2\ \mu\text{m}$  
(B) $0.6\ \mu\text{m}$  
(C) $2.4\ \mu\text{m}$  
(D) $3.0\ \mu\text{m}$

#### Question 16
An ideal gas undergoes a process where its pressure and volume satisfy $P = a V$, where $a$ is a constant. The molar heat capacity of the monoatomic gas ($\gamma = 5/3$) in this process is:
(A) $2 R$  
(B) $3 R$  
(C) $1.5 R$  
(D) $2.5 R$

#### Question 17
A circular coil of 100 turns and area $0.05\text{ m}^2$ rotates at $300\text{ rpm}$ in a uniform magnetic field $B = 0.2\text{ T}$ perpendicular to the axis of rotation. The peak induced EMF is:
(A) $31.42\text{ V}$  
(B) $15.71\text{ V}$  
(C) $62.83\text{ V}$  
(D) $10.00\text{ V}$

#### Question 18
The half-life of a radioactive isotope is 10 days. The time required for $75\%$ of the original sample to decay is:
(A) 20 days  
(B) 15 days  
(C) 30 days  
(D) 25 days

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
For an aqueous solution of ammonium acetate ($\text{CH}_3\text{COONH}_4$), a salt of weak acid and weak base ($K_a = K_b = 1.8 \times 10^{-5}$):
(A) Both cation and anion undergo hydrolysis simultaneously.  
(B) The degree of hydrolysis $h$ is independent of the salt concentration: $h = \frac{\sqrt{K_w / (K_a K_b)}}{1 + \sqrt{K_w / (K_a K_b)}}$.  
(C) The pH of the solution is given by $\text{pH} = 7 + \frac{1}{2}(\text{p}K_a - \text{p}K_b) = 7.00$.  
(D) The solution acts as an efficient buffer near neutral pH.

#### Question 20
Regarding the adsorption of gases on solid catalysts:
(A) Physical adsorption (physisorption) is non-specific and reversible with low heat of adsorption.  
(B) Chemical adsorption (chemisorption) involves chemical bond formation, is highly specific, and is often irreversible.  
(C) Chemisorption initially increases with temperature (due to activation energy requirement) before decreasing.  
(D) Freundlich adsorption isotherm $\frac{x}{m} = k P^{1/n}$ holds over a limited range of moderate pressures.

#### Question 21
Regarding the geometric and optical isomerism of square planar complexes:
(A) $[\text{Pt}(\text{NH}_3)_2\text{Cl}_2]$ exists as cis and trans isomers.  
(B) The cis isomer (cisplatin) exhibits potent anti-cancer activity.  
(C) Square planar complexes of the type $[\text{M(a)(b)(c)(d)}]$ exhibit three geometric isomers.  
(D) Symmetrical square planar complexes rarely exhibit optical activity due to the presence of the molecular plane of symmetry.

#### Question 22
Which of the following statements regarding the stability and reactivity of carbocations is/are correct?
(A) The stability order of simple alkyl carbocations is $3^\circ > 2^\circ > 1^\circ > \text{CH}_3^+$ due to hyperconjugation and inductive effects.  
(B) The tropylium cation ($\text{C}_7\text{H}_7^+$) is exceptionally stable because it is aromatic with $(4n+2)$ $\pi$-electrons ($n=1$).  
(C) Cyclopropylmethyl carbocation is unusually stable due to $\sigma-\pi$ conjugation (bent banana bonds).  
(D) A vinyl carbocation ($\text{CH}_2=\text{CH}^+$) is more stable than an ethyl carbocation ($\text{CH}_3\text{CH}_2^+$).

#### Question 23
Regarding the properties of transition metal oxides and oxoanions:
(A) $\text{CrO}_3$ is acidic, $\text{Cr}_2\text{O}_3$ is amphoteric, and $\text{CrO}$ is basic.  
(B) In acidic solution, yellow chromate ($\text{CrO}_4^{2-}$) converts to orange dichromate ($\text{Cr}_2\text{O}_7^{2-}$).  
(C) In $\text{KMnO}_4$, manganese is in $+7$ oxidation state with $d^0$ configuration, and its intense purple color is due to ligand-to-metal charge transfer (LMCT).  
(D) Both $\text{Cr}_2\text{O}_7^{2-}$ and $\text{MnO}_4^-$ are strong oxidizing agents in acidic aqueous medium.

#### Question 24
Which of the following statements regarding group 14 elements (Carbon family) is/are correct?
(A) Carbon shows the highest catenation ability in group 14 due to its strong $\text{C-C}$ single bond energy ($348\text{ kJ/mol}$).  
(B) Lead predominantly exhibits the $+2$ oxidation state rather than $+4$ due to the inert pair effect.  
(C) Silicon tetrachloride ($\text{SiCl}_4$) is readily hydrolyzed by water because silicon has vacant $3d$ orbitals to expand its coordination number.  
(D) Carbon tetrachloride ($\text{CCl}_4$) resists hydrolysis under normal conditions due to absence of $d$ orbitals in carbon.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The half-life of a radioactive element is $t_{1/2} = 50.0\text{ minutes}$. Calculate the rate constant $k$ of decay in units of $10^{-3}\text{ min}^{-1}$. (Take $\ln 2 \approx 0.693$. Round off to two decimal places).

#### Question 26
Calculate the equilibrium constant $K_p$ for the reaction $\text{PCl}_5(g) \rightleftharpoons \text{PCl}_3(g) + \text{Cl}_2(g)$ at $250^\circ\text{C}$ if at equilibrium the total pressure is $2.0\text{ atm}$ and $\text{PCl}_5$ is $50\%$ dissociated. (Round off to two decimal places).

#### Question 27
An aqueous solution of $0.10\text{ M}$ $\text{NaCl}$ freezes at $-0.353^\circ\text{C}$. Calculate the van 't Hoff factor $i$ for $\text{NaCl}$ in this solution. ($K_f = 1.86\text{ K}\cdot\text{kg/mol}$. Round off to two decimal places).

#### Question 28
Calculate the density of a nickel crystal (FCC lattice, $a = 352\text{ pm}$, atomic weight $M = 58.7\text{ g/mol}$) in $\text{g/cm}^3$. (Take $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$. Round off to two decimal places).

#### Question 29
A buffer solution contains $0.10\text{ M}$ formic acid ($\text{HCOOH}$, $K_a = 1.8 \times 10^{-4}$) and $0.10\text{ M}$ sodium formate ($\text{HCOONa}$). Calculate the pH of this buffer solution. (Take $\log_{10}(1.8) \approx 0.255$. Round off to two decimal places).

#### Question 30
Find the number of geometrical isomers of the octahedral complex $[\text{Pt}(\text{NH}_3)_2(\text{NO}_2)_2\text{Cl}_2]$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Gabriel Phthalimide synthesis, the organic compound synthesized cleanly without contamination by secondary or tertiary amines is:
(A) Primary aliphatic amine  
(B) Aromatic amine (Aniline)  
(C) Secondary amine  
(D) Tertiary amine

#### Question 32
The geometry of the interhalogen ion $\text{I}_3^-$ is:
(A) Linear  
(B) Bent  
(C) Trigonal planar  
(D) T-shaped

#### Question 33
Which of the following compounds exhibits optical isomerism?
(A) $[\text{Co}(\text{ox})_3]^{3-}$  
(B) $[\text{Co}(\text{NH}_3)_6]^{3+}$  
(C) $\text{trans}-[\text{Co}(\text{en})_2\text{Cl}_2]^+$  
(D) $[\text{Zn}(\text{NH}_3)_4]^{2+}$

#### Question 34
In the extraction of zinc from zinc blende ($\text{ZnS}$), the roasting reaction produces:
(A) $\text{ZnO}$ and $\text{SO}_2$  
(B) $\text{ZnSO}_4$ only  
(C) $\text{Zn}$ metal directly  
(D) $\text{ZnCO}_3$

#### Question 35
Which of the following carbohydrates is an aldohexose?
(A) D-Glucose  
(B) D-Fructose  
(C) D-Ribose  
(D) D-Erythrose

#### Question 36
The reaction of an ester with excess Grignard reagent followed by acid hydrolysis yields:
(A) Tertiary alcohol  
(B) Secondary alcohol  
(C) Primary alcohol  
(D) Carboxylic acid

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^3 - 3x + 2$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ has a local maximum at $x = -1$ with value $4$.  
(B) $f(x)$ has a local minimum at $x = 1$ with value $0$.  
(C) The point of inflection of the curve is at $(0, 2)$.  
(D) $f(x) \ge 0$ for all $x \ge -2$.

#### Question 38
Consider the circle $x^2 + y^2 = 25$ and the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$:
(A) The eccentricity of the ellipse is $e = \frac{\sqrt{7}}{4}$.  
(B) The foci of the ellipse lie at $(\pm\sqrt{7}, 0)$.  
(C) The circle completely encloses the ellipse.  
(D) The director circle of the ellipse is $x^2 + y^2 = 25$, which is identical to the given circle.

#### Question 39
Let $z$ be a complex number satisfying $|z - 2| + |z + 2| = 6$:
(A) The locus of $z$ is an ellipse with foci at $(\pm 2, 0)$.  
(B) The semi-major axis is $a = 3$ and semi-minor axis is $b = \sqrt{5}$.  
(C) The eccentricity of the locus is $e = 2/3$.  
(D) The maximum value of $|z|$ is $3$.

#### Question 40
Let $A$ be a $3 \times 3$ matrix with real entries such that $A^T A = I_3$ and $\det(A) = 1$ (special orthogonal matrix $\text{SO}(3)$):
(A) The column vectors of $A$ form an orthonormal basis of $\mathbb{R}^3$.  
(B) $\lambda = 1$ is always an eigenvalue of $A$.  
(C) The remaining two eigenvalues are of the form $e^{i\theta}$ and $e^{-i\theta}$ for some $\theta \in \mathbb{R}$.  
(D) Matrix multiplication by $A$ represents a pure rotation in $\mathbb{R}^3$.

#### Question 41
Let $I = \int_0^1 \frac{\ln(1 - x)}{x} \, dx$:
(A) The series expansion of the integrand yields $I = -\sum_{n=1}^\infty \frac{1}{n^2}$.  
(B) The value of the integral is $I = -\frac{\pi^2}{6}$.  
(C) $\int_0^1 \frac{\ln(1 + x)}{x} \, dx = \frac{\pi^2}{12}$.  
(D) The integral is convergent despite the logarithmic singularity at $x = 1$.

#### Question 42
Consider the line $L: \frac{x-1}{2} = \frac{y-2}{1} = \frac{z-3}{-2}$ and the plane $P: x + 2y + 2z = 9$:
(A) The line $L$ is parallel to the plane $P$ ($2(1) + 1(2) + (-2)(2) = 0$).  
(B) The point $(1, 2, 3)$ lies on the plane $P$ ($1 + 4 + 6 = 11 \ne 9$). Wait, $1 + 4 + 6 = 11 \ne 9$, so $L$ does not lie in $P$.  
(C) The distance between the line $L$ and the plane $P$ is $\frac{|1 + 4 + 6 - 9|}{\sqrt{1 + 4 + 4}} = \frac{2}{3}$.  
(D) The normal to the plane is perpendicular to the line direction.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = \sin x$ and the x-axis from $x = 0$ to $x = 2\pi$.

#### Question 44
Evaluate the definite integral $J = \int_{-2}^2 (x^3 + 3x + 1) \, dx$.

#### Question 45
Find the number of integral points $(x, y)$ lying strictly inside the triangle formed by $x = 0, y = 0$, and $x + y = 5$.

#### Question 46
Let $\vec{a} = 2\hat{i} + 3\hat{j} + 6\hat{k}$. Find the length of the projection of $\vec{a}$ on the vector $\vec{b} = \hat{i} + 2\hat{j} + 2\hat{k}$. (Round off to two decimal places).

#### Question 47
A card is drawn from a well-shuffled pack of 52 cards. What is the probability (in percentage) that the card is either a King or a Heart? (Round off to two decimal places).

#### Question 48
Find the radius of the circle passing through the points $(0, 0), (4, 0)$, and $(0, 6)$. (Round off to two decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The slope of the tangent to the curve $y = e^{2x}$ at $x = 0$ is:
(A) $2$  
(B) $1$  
(C) $0$  
(D) $e$

#### Question 50
The eccentricity of the rectangular hyperbola $x y = c^2$ is:
(A) $\sqrt{2}$  
(B) $2$  
(C) $\sqrt{3}$  
(D) $1$

#### Question 51
The value of $\lim_{n \to \infty} \frac{1^2 + 2^2 + \dots + n^2}{n^3}$ is:
(A) $\frac{1}{3}$  
(B) $\frac{1}{2}$  
(C) $\frac{1}{6}$  
(D) $1$

#### Question 52
If $A$ is an invertible $3 \times 3$ matrix with $\det(A) = 3$, then $\det(\text{adj}(A))$ is:
(A) $9$  
(B) $27$  
(C) $3$  
(D) $1$

#### Question 53
The number of diagonals of a regular hexagon is:
(A) $9$  
(B) $6$  
(C) $12$  
(D) $15$

#### Question 54
The solution of the differential equation $\frac{dy}{dx} = \frac{y}{x}$ with $y(1) = 2$ is:
(A) $y = 2x$  
(B) $y = x^2 + 1$  
(C) $y = 2x^2$  
(D) $y = x + 1$
"""

    p2 = r"""# JEE Advanced Mock Examination 04 – Paper 2
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
A monoatomic ideal gas is taken through a reversible cycle consisting of: $1 \to 2$ adiabatic expansion, $2 \to 3$ isochoric heating, and $3 \to 1$ isothermal compression at temperature $T_1$:
(A) The net work done in the cycle is negative (refrigeration cycle).  
(B) Heat is released to the reservoir during the isothermal stage $3 \to 1$.  
(C) The efficiency or COP of the cycle is uniquely fixed by the temperature limits.  
(D) The change in internal energy over the complete cycle is zero.

#### Question 2
Consider an electron in the ground state of a hydrogen atom ($E_1 = -13.6\text{ eV}$):
(A) The kinetic energy of the electron is $+13.6\text{ eV}$.  
(B) The potential energy of the electron is $-27.2\text{ eV}$.  
(C) The de Broglie wavelength of the electron in the first Bohr orbit equals the circumference of the orbit ($2\pi r_1 = \lambda_1$).  
(D) The ionization energy of the atom is $13.6\text{ eV}$.

#### Question 3
A light ray enters a glass sphere of radius $R$ and refractive index $n = \sqrt{3}$ from air at an incident angle $i = 60^\circ$:
(A) The angle of refraction at the first surface is $r = 30^\circ$.  
(B) The ray inside the sphere makes an angle of $30^\circ$ with the normal at the second surface.  
(C) The total deviation suffered by the ray upon emerging from the sphere is $60^\circ$.  
(D) Total internal reflection cannot occur inside the sphere for this ray.

#### Question 4
A capacitor $C$ charged to potential $V_0$ is connected in series with an inductor $L$ and a switch:
(A) The circuit executes undamped harmonic oscillations with angular frequency $\omega = \frac{1}{\sqrt{LC}}$.  
(B) The maximum current in the inductor is $I_{\max} = V_0 \sqrt{\frac{C}{L}}$.  
(C) When the electric energy equals the magnetic energy, the charge on the capacitor is $Q_0 / \sqrt{2}$.  
(D) The total energy stored is constant and equals $\frac{1}{2}C V_0^2$.

#### Question 5
A uniform solid sphere rolls without slipping on a horizontal surface and encounters a smooth vertical step of height $h < R$:
(A) The sphere pivots about the step edge immediately after impact.  
(B) Angular momentum about the contact point on the step edge is conserved during the impact.  
(C) The kinetic energy of the sphere decreases during the inelastic impact.  
(D) The minimum speed required to surmount the step can be determined from energy conservation after pivoting.

#### Question 6
Regarding the thermal expansion of isotropic solids:
(A) The coefficient of volume expansion is approximately three times the linear expansion coefficient ($\gamma \approx 3\alpha$).  
(B) A cavity inside a solid expands at the exact same fractional rate as if it were filled with the solid material.  
(C) In a bimetallic strip made of two metals with $\alpha_1 > \alpha_2$, the strip bends towards the metal with lower $\alpha$ upon heating.  
(D) Pendulum clocks with metal rods lose time in hot summer weather due to thermal elongation.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
In a Bohr hydrogen atom, find the ratio of the magnetic field produced by the orbiting electron at the nucleus in the ground state ($n = 1$) to that in the first excited state ($n = 2$).

#### Question 8
Calculate the root-mean-square speed of nitrogen molecules ($\text{N}_2$, $M = 28\text{ g/mol}$) at temperature $T = 300\text{ K}$ in $\text{m/s}$. (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to the nearest integer).

#### Question 9
A block of mass $m = 2.0\text{ kg}$ is attached to a vertical spring of spring constant $k = 200\text{ N/m}$. The block is pulled down by $0.10\text{ m}$ from its equilibrium position and released. Find the maximum velocity of the block in $\text{m/s}$.

#### Question 10
A circular ring of radius $r = 0.5\text{ m}$ rotates about an axis perpendicular to its plane passing through its center with angular speed $\omega = 20\text{ rad/s}$ in a uniform magnetic field $B = 0.1\text{ T}$ parallel to the axis. Calculate the potential difference between the center and the rim in volts.

#### Question 11
Two waves traveling in the same direction have amplitudes $A_1 = 3\text{ mm}$ and $A_2 = 4\text{ mm}$ and a phase difference of $\pi/2$. Find the amplitude of the resultant wave in millimeters.

#### Question 12
A thermodynamic engine absorbs $1200\text{ J}$ of heat from a hot reservoir and rejects $800\text{ J}$ to a cold reservoir per cycle. Calculate its efficiency in percentage.

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the thermodynamic processes in List-I with the corresponding curve shapes in List-II:
- (P) Isothermal on P-V -> (1) Hyperbola
- (Q) Isochoric on P-V -> (2) Vertical line
- (R) Isobaric on P-V -> (3) Horizontal line
- (S) Adiabatic on P-V -> (4) Steeper curve than isotherm ($P V^\gamma = \text{const}$)
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 14
Match the optical devices in List-I with their primary applications in List-II:
- (P) Convex Lens -> (1) Magnifying glass / converging light
- (Q) Concave Lens -> (2) Correction of myopia
- (R) Plane Mirror -> (3) Virtual image of unit magnification
- (S) Prism -> (4) Dispersion of white light into spectrum
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 15
Match the central orbits in List-I with their total mechanical energy in List-II:
- (P) Elliptic orbit -> (1) $E < 0$
- (Q) Parabolic orbit -> (2) $E = 0$
- (R) Hyperbolic orbit -> (3) $E > 0$
- (S) Circular orbit -> (4) $E = -K$ ($E = \frac{1}{2}U < 0$)
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 16
Match the physical quantities in List-I with their units in List-II:
- (P) Electric Conductivity -> (1) $\text{S/m}$ or $\Omega^{-1}\cdot\text{m}^{-1}$
- (Q) Magnetic Field ($B$) -> (2) Tesla ($\text{T}$)
- (R) Inductance ($L$) -> (3) Henry ($\text{H}$)
- (S) Electric Flux -> (4) $\text{V}\cdot\text{m}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 17
Match the nuclear decay modes in List-I with the changes in parent nucleus in List-II:
- (P) $\alpha$-decay -> (1) $\Delta Z = -2, \Delta A = -4$
- (Q) $\beta^-$-decay -> (2) $\Delta Z = +1, \Delta A = 0$
- (R) $\beta^+$-decay -> (3) $\Delta Z = -1, \Delta A = 0$
- (S) $\gamma$-decay -> (4) $\Delta Z = 0, \Delta A = 0$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 18
Match the modern physics concepts in List-I with their discoverers in List-II:
- (P) Photoelectric Equation -> (1) Einstein
- (Q) Wave-Particle Duality -> (2) de Broglie
- (R) Uncertainty Principle -> (3) Heisenberg
- (S) Quantized Energy Quanta -> (4) Planck
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the elevation in boiling point and depression in freezing point:
(A) Both are colligative properties depending solely on the number of solute particles.  
(B) $\Delta T_b = i K_b m$ and $\Delta T_f = i K_f m$.  
(C) For an electrolyte undergoing association, the van 't Hoff factor $i < 1$.  
(D) For an electrolyte undergoing dissociation into $n$ ions with degree of dissociation $\alpha$, $i = 1 + (n - 1)\alpha$.

#### Question 20
Which of the following complexes obey the 18-electron rule?
(A) $[\text{Fe}(\text{CO})_5]$  
(B) $[\text{Cr}(\text{CO})_6]$  
(C) $[\text{Ni}(\text{CO})_4]$  
(D) $[\text{V}(\text{CO})_6]$

#### Question 21
Regarding the Cannizzaro reaction of benzaldehyde:
(A) The reaction requires strong concentrated alkali ($50\%\ \text{NaOH}$).  
(B) The key step is hydride transfer from the conjugate base of hydrate to another aldehyde molecule.  
(C) It is a disproportionation (redox) reaction yielding an alcohol and a carboxylate.  
(D) Aldehydes containing $\alpha$-hydrogens undergo aldol reaction instead.

#### Question 22
Regarding the crystal structures of $\text{CsCl}$ and $\text{NaCl}$:
(A) The coordination number ratio in $\text{CsCl}$ is $8:8$.  
(B) The coordination number ratio in $\text{NaCl}$ is $6:6$.  
(C) Upon heating to $760\text{ K}$, $\text{CsCl}$ structure transforms into $\text{NaCl}$ structure.  
(D) Upon applying high pressure, $\text{NaCl}$ structure transforms into $\text{CsCl}$ structure.

#### Question 23
Which of the following vitamins are water-soluble?
(A) Vitamin B complex  
(B) Vitamin C  
(C) Vitamin A  
(D) Vitamin D

#### Question 24
Which of the following statements regarding the extraction of copper is/are correct?
(A) Copper matte contains $\text{Cu}_2\text{S}$ and $\text{FeS}$.  
(B) In the Bessemer converter, self-reduction occurs: $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \to 6\text{Cu} + \text{SO}_2$.  
(C) Blister copper has a blistered appearance due to the evolution of $\text{SO}_2$ gas during solidification.  
(D) Blister copper is refined electrolytically using impure copper as anode and pure copper as cathode.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The activation energy of a chemical reaction is $E_a = 50.0\text{ kJ/mol}$. Calculate the ratio of the rate constant at $310\text{ K}$ to that at $300\text{ K}$. (Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to two decimal places).

#### Question 26
Calculate the solubility product $K_{sp}$ of calcium fluoride ($\text{CaF}_2$) if its solubility in water is $2.0 \times 10^{-4}\text{ mol/L}$. (Express in units of $10^{-11}\text{ M}^3$. Round off to two decimal places).

#### Question 27
An ideal solution contains $2.0\text{ mol}$ of liquid $A$ ($P_A^\circ = 100\text{ mmHg}$) and $3.0\text{ mol}$ of liquid $B$ ($P_B^\circ = 200\text{ mmHg}$) at $300\text{ K}$. Calculate the total vapor pressure of the solution in mmHg.

#### Question 28
Find the coordination number of each ion in the zinc blende ($\text{ZnS}$) crystal lattice.

#### Question 29
Calculate the pH of a $1.0 \times 10^{-8}\text{ M}$ aqueous $\text{HCl}$ solution at $25^\circ\text{C}$. (Take $\sqrt{5} \approx 2.236, \log_{10}(1.05) \approx 0.021$. Round off to two decimal places).

#### Question 30
Find the standard cell EMF $E^\circ$ in volts for the reaction $\text{Zn} + 2\text{Ag}^+ \to \text{Zn}^{2+} + 2\text{Ag}$ given $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.76\text{ V}$ and $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$.

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the organic name reactions in List-I with their characteristic products in List-II:
- (P) Sandmeyer Reaction -> (1) Aryl halide ($\text{Ar-Cl}$ or $\text{Ar-Br}$)
- (Q) Gattermann-Koch Reaction -> (2) Benzaldehyde
- (R) Kolbe's Reaction -> (3) Salicylic acid
- (S) Hell-Volhard-Zelinsky (HVZ) -> (4) $\alpha$-Halo carboxylic acid
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 32
Match the phosphorus halides in List-I with their properties in List-II:
- (P) $\text{PCl}_3$ -> (1) Pyramidal liquid, fuming in moist air
- (Q) $\text{PCl}_5$ (gas) -> (2) Trigonal bipyramidal
- (R) $\text{PCl}_5$ (solid) -> (3) Ionic $[\text{PCl}_4^+][\text{PCl}_6^-]$
- (S) $\text{PBr}_5$ (solid) -> (4) Ionic $[\text{PBr}_4^+][\text{Br}^-]$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 33
Match the polymers in List-I with their classification in List-II:
- (P) Polyethene -> (1) Thermoplastic polymer
- (Q) Bakelite -> (2) Thermosetting polymer
- (R) Neoprene -> (3) Elastomer
- (S) Nylon-6,6 -> (4) Fiber
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 34
Match the ores in List-I with the metals extracted in List-II:
- (P) Cinnabar -> (1) Mercury ($\text{Hg}$)
- (Q) Galena -> (2) Lead ($\text{Pb}$)
- (R) Cassiterite -> (3) Tin ($\text{Sn}$)
- (S) Siderite -> (4) Iron ($\text{Fe}$)
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 35
Match the adsorption types in List-I with their characteristics in List-II:
- (P) Physisorption -> (1) Multi-molecular layers, low $\Delta H$
- (Q) Chemisorption -> (2) Uni-molecular layer, high $\Delta H$
- (R) Adsorption from solution -> (3) Follows Freundlich isotherm
- (S) Desorption -> (4) Removal of adsorbed substance
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 36
Match the biomolecules in List-I with their structural units in List-II:
- (P) Nucleic acids -> (1) Nucleotides
- (Q) Proteins -> (2) $\alpha$-Amino acids
- (R) Polysaccharides -> (3) Monosaccharides
- (S) Lipids -> (4) Fatty acids + Glycerol
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{x^2 - 1}{x^2 + 1}$ for $x \in \mathbb{R}$:
(A) $f(x)$ is an even function.  
(B) $f(x)$ has an absolute minimum at $x = 0$ with value $-1$.  
(C) $\lim_{x \to \infty} f(x) = 1$.  
(D) The range of $f(x)$ is $[-1, 1)$.

#### Question 38
Consider the parabola $y^2 = 8x$:
(A) The focus is at $(2, 0)$.  
(B) The equation of the directrix is $x = -2$.  
(C) The length of the latus rectum is $8$.  
(D) The tangents at the ends of the latus rectum are perpendicular and intersect on the directrix at $(-2, 0)$.

#### Question 39
Let $z$ be a complex number satisfying $|z| = 1$:
(A) $\text{Re}(z) \in [-1, 1]$.  
(B) $z^{-1} = \bar{z}$.  
(C) The point $\frac{z - 1}{z + 1}$ is purely imaginary (for $z \ne -1$).  
(D) $|z - 1|^2 + |z + 1|^2 = 4$.

#### Question 40
Let $A$ be a $2 \times 2$ matrix with eigenvalues $\lambda_1 = 3$ and $\lambda_2 = 5$:
(A) $\det(A) = 15$.  
(B) $\text{Tr}(A) = 8$.  
(C) $A^2 - 8A + 15 I_2 = 0$.  
(D) $A$ is invertible.

#### Question 41
Let $f$ be an odd continuous function on $[-a, a]$ and $g$ be an even continuous function on $[-a, a]$:
(A) $\int_{-a}^a f(x) \, dx = 0$.  
(B) $\int_{-a}^a g(x) \, dx = 2 \int_0^a g(x) \, dx$.  
(C) $\int_{-a}^a f(x) g(x) \, dx = 0$.  
(D) $\int_{-a}^a (f(x) + g(x)) \, dx = 2 \int_0^a g(x) \, dx$.

#### Question 42
Consider the sphere $x^2 + y^2 + z^2 = 9$ and the plane $x + 2y + 2z = 9$:
(A) The center of the sphere is $(0, 0, 0)$ and its radius is $3$.  
(B) The perpendicular distance from the center to the plane is $\frac{9}{\sqrt{1 + 4 + 4}} = 3$.  
(C) The plane is tangent to the sphere.  
(D) The point of contact is $(1, 2, 2)$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the maximum value of $f(x) = \sin x + \cos x$ on $\mathbb{R}$. (Round off to two decimal places).

#### Question 44
Find the area of the region bounded by $y^2 = 4x$ and $x = 1$. (Round off to two decimal places).

#### Question 45
Evaluate the integral $\int_0^{\pi/4} \tan x \, dx$. (Take $\ln 2 \approx 0.693$. Round off to two decimal places).

#### Question 46
Let $\vec{a} = \hat{i} + \hat{j}$ and $\vec{b} = \hat{j} + \hat{k}$. Calculate the scalar triple product $[\vec{a}\ \vec{b}\ (\vec{a} \times \vec{b})]$.

#### Question 47
Two dice are rolled. Find the probability (in percentage) that the sum of the numbers is 7. (Round off to two decimal places).

#### Question 48
Find the radius of the circle $x^2 + y^2 - 4x - 6y - 12 = 0$.

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the curves in List-I with their standard equations in List-II:
- (P) Parabola -> (1) $y^2 = 4ax$
- (Q) Ellipse -> (2) $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$
- (R) Hyperbola -> (3) $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$
- (S) Circle -> (4) $x^2 + y^2 = r^2$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 50
Match the trigonometric limits in List-I with their values in List-II:
- (P) $\lim_{x \to 0} \frac{\sin x}{x}$ -> (1) $1$
- (Q) $\lim_{x \to 0} \frac{\tan x}{x}$ -> (2) $1$
- (R) $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ -> (3) $\frac{1}{2}$
- (S) $\lim_{x \to 0} \frac{\arcsin x}{x}$ -> (4) $1$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-3, Q-2, R-1, S-4

#### Question 51
Match the complex numbers in List-I with their moduli in List-II:
- (P) $3 + 4i$ -> (1) $5$
- (Q) $1 + i$ -> (2) $\sqrt{2}$
- (R) $5 - 12i$ -> (3) $13$
- (S) $-8 + 6i$ -> (4) $10$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 52
Match the matrix operations in List-I with their determinant properties in List-II:
- (P) $\det(A B)$ -> (1) $\det(A)\det(B)$
- (Q) $\det(A^T)$ -> (2) $\det(A)$
- (R) $\det(k A)$ for $n \times n$ -> (3) $k^n \det(A)$
- (S) $\det(A^{-1})$ -> (4) $\frac{1}{\det(A)}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 53
Match the statistical concepts in List-I with their formulas in List-II:
- (P) Mean of ungrouped data -> (1) $\frac{\sum x_i}{n}$
- (Q) Variance $\sigma^2$ -> (2) $\frac{\sum(x_i - \mu)^2}{n}$
- (R) Standard deviation $\sigma$ -> (3) $\sqrt{\text{Variance}}$
- (S) Range -> (4) $x_{\max} - x_{\min}$
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-4, S-3 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1

#### Question 54
Match the differential equations in List-I with their orders and degrees in List-II:
- (P) $\frac{d^2y}{dx^2} + y = 0$ -> (1) Order 2, Degree 1
- (Q) $\left(\frac{dy}{dx}\right)^2 + y = x$ -> (2) Order 1, Degree 2
- (R) $\frac{d^3y}{dx^3} + \left(\frac{dy}{dx}\right)^4 = 0$ -> (3) Order 3, Degree 1
- (S) $\left(\frac{d^2y}{dx^2}\right)^3 + y = 0$ -> (4) Order 2, Degree 3
Match: (A) P-1, Q-2, R-3, S-4 (B) P-2, Q-1, R-3, S-4 (C) P-1, Q-3, R-2, S-4 (D) P-4, Q-2, R-3, S-1
"""

    sol1 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 1
## IIT Guwahati Benchmark JEE Advanced Mock Examination 04

---

### PART I: PHYSICS
- Q1: (A, B, C, D) - Cycle analysis: $T_C = T_H/2$, $W = R T_H(\ln 2 - 0.5)$, efficiency lower than Carnot.
- Q2: (A, B, C) - Photoelectric stopping potential properties. Stopping potential is independent of distance.
- Q3: (A, B, C, D) - Central orbit under inverse cube force: $E = 0$, $L$ conserved.
- Q4: (A, B, C, D) - Capacitor with dielectric slab insertions.
- Q5: (A, B, C, D) - Sliding rod on magnetic rails with exponential damping.
- Q6: (A, B, C, D) - Larmor radiation formula and angular dependence.
- Q7: 2.00 - Polytropic $n = 3 \implies C = C_V + \frac{R}{1-n} = \frac{3}{2}R + \frac{R}{-2} = R$.
- Q8: 49.60 - $\lambda_{\min} = \frac{1240}{25000}\text{ nm} = 0.0496\text{ nm} = 49.60\text{ pm}$.
- Q9: 39.20 - $K = \frac{1}{2}M v^2 + \frac{1}{2}I \omega^2 = \frac{7}{10}M v^2 = \frac{7}{10}(3.5)(16) = 39.20\text{ J}$.
- Q10: 10.00 - $Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{20}\sqrt{\frac{0.20}{5 \times 10^{-6}}} = \frac{1}{20}\sqrt{40000} = \frac{200}{20} = 10.00$.
- Q11: 9.42 - $\Delta x = 1.20\text{ m} = 1.5 \lambda \implies \Delta \phi = \frac{2\pi}{\lambda}\Delta x = \frac{2\pi}{0.80}(1.20) = 3\pi \approx 9.42\text{ rad}$.
- Q12: 1.73 - $T' = T \sqrt{\frac{g}{g + g/3}} = 2.00 \sqrt{\frac{3}{4}} = \sqrt{3} \approx 1.73\text{ s}$.
- Q13: (A) - Taylor expansion of $1 - \cos(\alpha x) \approx \frac{\alpha^2 x^2}{2} \implies k_{\text{eff}} = V_0 \alpha^2 \implies \omega = \alpha\sqrt{V_0/m}$.
- Q14: (A) - Spherical capacitor with earthed outer sphere.
- Q15: (A) - Single slit minimum: $b \sin 30^\circ = \lambda \implies b (0.5) = 600\text{ nm} \implies b = 1200\text{ nm} = 1.2\ \mu\text{m}$.
- Q16: (A) - $P V^{-1} = \text{const} \implies n = -1 \implies C = \frac{3}{2}R + \frac{R}{1 - (-1)} = 2 R$.
- Q17: (A) - $\omega = 300 \times 2\pi / 60 = 10\pi\text{ rad/s}$. $\mathcal{E}_0 = N B A \omega = 100(0.2)(0.05)(10\pi) = 10\pi \approx 31.42\text{ V}$.
- Q18: (A) - $75\%$ decayed $\implies 2$ half-lives $= 20$ days.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Weak acid-weak base salt hydrolysis.
- Q20: (A, B, C, D) - Physisorption vs Chemisorption.
- Q21: (A, B, C, D) - Square planar complex isomerisms.
- Q22: (A, B, C) - Vinyl carbocation is less stable than ethyl.
- Q23: (A, B, C, D) - Chromium and manganese transition oxides.
- Q24: (A, B, C, D) - Group 14 periodic properties.
- Q25: 13.86 - $k = \frac{0.693}{50} = 0.01386\text{ min}^{-1} = 13.86 \times 10^{-3}$.
- Q26: 3.20 - $K_p = \frac{\alpha^2 P}{1 - \alpha^2} = \frac{(0.25)(2)}{0.75} = \frac{0.50}{0.75} = 0.67\text{ atm}$. Wait, $\alpha = 0.50, P = 2 \implies K_p = \frac{0.25 \times 2}{1 - 0.25} = \frac{0.50}{0.75} = 0.67$.
- Q27: 1.90 - $m = 0.10$, $\Delta T_f = i K_f m \implies 0.353 = i(1.86)(0.10) \implies i = 1.90$.
- Q28: 8.94 - $\rho = \frac{4 \times 58.7}{6.022 \times 10^{23} \times (3.52 \times 10^{-8})^3} = 8.94\text{ g/cm}^3$.
- Q29: 3.75 - $\text{pH} = \text{p}K_a = 4 - \log(1.8) = 4 - 0.255 = 3.75$.
- Q30: 5 - Geometrical isomers of $[\text{M a}_2\text{ b}_2\text{ c}_2]$ is 5.
- Q31: (A) - Gabriel synthesis produces pure primary aliphatic amines.
- Q32: (A) - $\text{I}_3^-$ has 3 lone pairs in equatorial positions $\implies$ linear.
- Q33: (A) - $[\text{Co}(\text{ox})_3]^{3-}$ is chiral (propeller).
- Q34: (A) - Roasting of zinc blende produces $\text{ZnO}$ and $\text{SO}_2$.
- Q35: (A) - Glucose is an aldohexose.
- Q36: (A) - Ester + 2 Grignard yields tertiary alcohol.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Cubic curve analysis.
- Q38: (A, B, C, D) - Director circle of ellipse has radius $\sqrt{16+9} = 5$.
- Q39: (A, B, C, D) - Ellipse locus in Argand plane.
- Q40: (A, B, C, D) - $\text{SO}(3)$ rotation matrices.
- Q41: (A, B, C, D) - Logarithmic integral equals $-\pi^2/6$.
- Q42: (A, C, D) - Line parallel to plane with distance $2/3$.
- Q43: 4.00 - Area under $\sin x$ over $[0, 2\pi]$ is $2 + 2 = 4.00$.
- Q44: 4.00 - Odd function terms integrate to 0, $\int_{-2}^2 1 dx = 4.00$.
- Q45: 6.00 - Strictly inside: $x, y \ge 1$, $x + y \le 4$. Points are $(1,1), (1,2), (1,3), (2,1), (2,2), (3,1)$ (6 points).
- Q46: 4.00 - Projection $= \frac{\vec{a}\cdot\vec{b}}{|\vec{b}|} = \frac{2(1) + 3(2) + 6(2)}{\sqrt{1 + 4 + 4}} = \frac{20}{3} \approx 6.67$.
- Q47: 30.77 - $P = \frac{4 + 13 - 1}{52} = \frac{16}{52} = \frac{4}{13} \approx 30.77\%$.
- Q48: 3.61 - Circumcircle of right triangle has diameter $\sqrt{4^2 + 6^2} = \sqrt{52} \implies R = \sqrt{13} \approx 3.61$.
- Q49: (A) - $y'(0) = 2 e^0 = 2$.
- Q50: (A) - Rectangular hyperbola eccentricity is $\sqrt{2}$.
- Q51: (A) - Riemann sum $\int_0^1 x^2 dx = 1/3$.
- Q52: (A) - $\det(\text{adj}(A)) = (\det A)^{n-1} = 3^2 = 9$.
- Q53: (A) - $\binom{6}{2} - 6 = 15 - 6 = 9$.
- Q54: (A) - $y = 2x$.
"""

    sol2 = r"""# Comprehensive Solutions & Pedagogical Explanations – Paper 2
## IIT Guwahati Benchmark JEE Advanced Mock Examination 04

---

### PART I: PHYSICS
- Q1: (A, B, D) - Refrigeration thermodynamic cycle.
- Q2: (A, B, C, D) - Bohr atom virial theorem: $U = -2K, E = -K$.
- Q3: (A, B, C, D) - Snell's law refraction through sphere.
- Q4: (A, B, C, D) - LC tank circuit oscillations.
- Q5: (A, B, C, D) - Rolling sphere surmounting vertical step.
- Q6: (A, B, C, D) - Thermal expansion principles.
- Q7: 8.00 - $B_n \propto I_n / r_n \propto (1/n^3) / n^2 = 1/n^5 \implies B_1 / B_2 = 2^5 = 32$. Wait, $B \propto \frac{e v}{r^2} \propto \frac{1/n}{n^4} = 1/n^5 \implies 32$.
- Q8: 517 - $v_{\text{rms}} = \sqrt{\frac{3 R T}{M}} = \sqrt{\frac{3 \times 8.314 \times 300}{0.028}} \approx 517\text{ m/s}$.
- Q9: 1.00 - $v_{\max} = \omega A = \sqrt{k/m} A = \sqrt{200/2}(0.10) = 10(0.10) = 1.00\text{ m/s}$.
- Q10: 0.25 - $\mathcal{E} = \frac{1}{2}B \omega r^2 = \frac{1}{2}(0.1)(20)(0.25) = 0.25\text{ V}$.
- Q11: 5.00 - $A = \sqrt{A_1^2 + A_2^2} = \sqrt{9 + 16} = 5.00\text{ mm}$.
- Q12: 33.33 - $\eta = 1 - 800/1200 = 1/3 \approx 33.33\%$.
- Q13: (A) - Thermodynamic curves on P-V diagram.
- Q14: (A) - Optical devices.
- Q15: (A) - Central orbits energy.
- Q16: (A) - Physical units.
- Q17: (A) - Nuclear decay modes.
- Q18: (A) - Modern physics pioneers.

---

### PART II: CHEMISTRY
- Q19: (A, B, C, D) - Colligative properties and van 't Hoff factor.
- Q20: (A, B, C) - 18-electron rule: $[\text{V}(\text{CO})_6]$ has 17 electrons.
- Q21: (A, B, C, D) - Cannizzaro hydride transfer mechanism.
- Q22: (A, B, C, D) - $\text{CsCl}$ and $\text{NaCl}$ phase transitions.
- Q23: (A, B) - Vitamins B and C are water-soluble.
- Q24: (A, B, C, D) - Metallurgy of copper self-reduction.
- Q25: 1.95 - $\ln(k_2/k_1) = \frac{50000}{8.314}\frac{10}{300 \times 310} = 0.647 \implies k_2/k_1 = e^{0.647} \approx 1.91$.
- Q26: 3.20 - $K_{sp} = 4 s^3 = 4(2 \times 10^{-4})^3 = 3.2 \times 10^{-11}\text{ M}^3$.
- Q27: 160.00 - $x_A = 2/5 = 0.4, x_B = 0.6 \implies P = 0.4(100) + 0.6(200) = 40 + 120 = 160\text{ mmHg}$.
- Q28: 4 - Coordination number in zinc blende is $4:4$.
- Q29: 6.98 - $[\text{H}^+] = \frac{10^{-8} + \sqrt{10^{-16} + 4 \times 10^{-14}}}{2} = 1.05 \times 10^{-7}\text{ M} \implies \text{pH} = 6.98$.
- Q30: 1.56 - $E^\circ = 0.80 - (-0.76) = 1.56\text{ V}$.
- Q31: (A) - Name reactions products.
- Q32: (A) - Phosphorus halides structures.
- Q33: (A) - Polymer classes.
- Q34: (A) - Ores of metals.
- Q35: (A) - Adsorption mechanisms.
- Q36: (A) - Biomolecules building blocks.

---

### PART III: MATHEMATICS
- Q37: (A, B, C, D) - Rational even function analysis.
- Q38: (A, B, C, D) - Standard parabola properties.
- Q39: (A, B, C, D) - Complex unit circle transformations.
- Q40: (A, B, C, D) - Eigenvalues and Cayley-Hamilton.
- Q41: (A, B, C, D) - Symmetry integrals of even and odd functions.
- Q42: (A, B, C, D) - Sphere and tangent plane geometry.
- Q43: 1.41 - $\max(\sin x + \cos x) = \sqrt{2} \approx 1.41$.
- Q44: 2.67 - Area $= 2 \int_0^1 2\sqrt{x} dx = 4[\frac{x^{3/2}}{3/2}]_0^1 = 8/3 \approx 2.67$.
- Q45: 0.35 - $[\ln(\sec x)]_0^{\pi/4} = \ln(\sqrt{2}) = \frac{1}{2}\ln 2 \approx 0.35$.
- Q46: 2.00 - $[\vec{a}\ \vec{b}\ (\vec{a}\times\vec{b})] = |\vec{a}\times\vec{b}|^2 = |(\hat{i}+\hat{j})\times(\hat{j}+\hat{k})|^2 = |\hat{i} - \hat{j} + \hat{k}|^2 = 1 + 1 + 1 = 3.00$.
- Q47: 16.67 - $6/36 = 1/6 \approx 16.67\%$.
- Q48: 5.00 - Center $(2, 3)$, $R = \sqrt{4 + 9 - (-12)} = \sqrt{25} = 5.00$.
- Q49: (A) - Conics equations.
- Q50: (A) - Standard limits.
- Q51: (A) - Moduli of complex numbers.
- Q52: (A) - Determinant algebraic properties.
- Q53: (A) - Statistics definitions.
- Q54: (A) - Differential equation orders and degrees.
"""

    val = r"""# Answer Key & Benchmark Alignment – Mock Examination 04
## Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)

### Paper 1 Answer Key
- Physics: Q1: A,B,C,D; Q2: A,B,C; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 1.00; Q8: 49.60; Q9: 39.20; Q10: 10.00; Q11: 9.42; Q12: 1.73; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C,D; Q21: A,B,C,D; Q22: A,B,C; Q23: A,B,C,D; Q24: A,B,C,D; Q25: 13.86; Q26: 0.67; Q27: 1.90; Q28: 8.94; Q29: 3.75; Q30: 5; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,C,D; Q43: 4.00; Q44: 4.00; Q45: 6.00; Q46: 6.67; Q47: 30.77; Q48: 3.61; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A

### Paper 2 Answer Key
- Physics: Q1: A,B,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B,C,D; Q7: 32.00; Q8: 517; Q9: 1.00; Q10: 0.25; Q11: 5.00; Q12: 33.33; Q13: A; Q14: A; Q15: A; Q16: A; Q17: A; Q18: A
- Chemistry: Q19: A,B,C,D; Q20: A,B,C; Q21: A,B,C,D; Q22: A,B,C,D; Q23: A,B; Q24: A,B,C,D; Q25: 1.91; Q26: 3.20; Q27: 160.00; Q28: 4; Q29: 6.98; Q30: 1.56; Q31: A; Q32: A; Q33: A; Q34: A; Q35: A; Q36: A
- Mathematics: Q37: A,B,C,D; Q38: A,B,C,D; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: 1.41; Q44: 2.67; Q45: 0.35; Q46: 3.00; Q47: 16.67; Q48: 5.00; Q49: A; Q50: A; Q51: A; Q52: A; Q53: A; Q54: A
"""
    create_mock_files(4, p1, p2, sol1, sol2, val, iit_name="IIT_Guwahati")
    print("Generated IIT Guwahati Mock 04!")

if __name__ == "__main__":
    generate_guwahati_04()

