# -*- coding: utf-8 -*-
"""
Generator for JEE Advanced Mock Test 05 - IIT Delhi-Inspired Examination
Variant: 2013 Benchmark (Circuit Transients, Wave Interference, Stereochemical Isomer Counts)
"""

import os

def create_mock_05():
    os.makedirs('mock_tests/Mock_05_IIT_Delhi', exist_ok=True)
    
    # -------------------------------------------------------------------------
    # PAPER 1
    # -------------------------------------------------------------------------
    p1 = """# JEE Advanced Mock Examination 05 — Paper 1
## Organising Style Inspiration: IIT Delhi (`IIT_DELHI_STYLE`)
**Historical Variant Benchmark**: 2013 Benchmark (Circuit Transients & Stereochemical Isomers)  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (8 Questions per subject - One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+1** for each correct option chosen, provided NO incorrect option is chosen.
  - Negative Marks: **-2** in all other cases.
- **Section 2 (6 Questions per subject - Numerical Value Answer)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Zero Marks: **0** in all other cases.
- **Section 3 (4 Questions per subject - Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.

---

# PART I: PHYSICS (54 Marks)

## Section 1: Multiple Correct Questions (Questions 1 to 8)

#### Question 1 (Electrodynamics — LC-Resistor Transient Network)
In an LCR circuit containing resistance $R = 20\\ \\Omega$, inductance $L = 0.10\\text{ H}$, and capacitance $C = 50\\ \\mu\\text{F}$ connected in series with an AC source $V(t) = 200 \\sin(100\\pi t)\\text{ V}$:
(A) The resonant angular frequency of the circuit is $\\omega_0 = \\frac{1}{\\sqrt{LC}} = 447.2\\text{ rad/s}$.  
(B) At resonance, the power factor of the circuit is unity.  
(C) The quality factor of the circuit is $Q = \\frac{\\omega_0 L}{R} = 2.24$.  
(D) The average power dissipated at resonance is $\\frac{V_{\\text{rms}}^2}{R} = 1000\\text{ W}$.

#### Question 2 (Mechanics — Rotational Collision with Hinge Reaction)
A uniform thin rod of mass $M$ and length $L$ is pivoted at one end on a frictionless horizontal table. A small putty ball of mass $m = M/3$ moving horizontally at speed $v_0$ strikes the rod perpendicularly at distance $x$ from the pivot and sticks to it:
(A) The angular velocity of the system immediately after impact is $\\omega = \\frac{m v_0 x}{\\frac{1}{3} M L^2 + m x^2}$.  
(B) If $x = \\frac{2}{3} L$, the impulsive reaction force exerted by the pivot during the collision is zero (center of percussion).  
(C) If $x < \\frac{2}{3} L$, the impulsive reaction at the pivot is directed in the direction of $v_0$.  
(D) Mechanical energy is conserved during the inelastic impact.

#### Question 3 (Thermodynamics — Polytropic Heat Capacity)
An ideal gas undergoes a polytropic process $P V^n = \\text{constant}$:
(A) The molar heat capacity is given by $C = C_V + \\frac{R}{1 - n}$.  
(B) If $1 < n < \\gamma$, the molar heat capacity $C$ is negative.  
(C) For an isobaric process ($n = 0$), $C = C_P = C_V + R$.  
(D) For an isothermal process ($n = 1$), the heat capacity $C$ is infinite.

#### Question 4 (Wave Motion — Doppler Shift with Two Observers)
A stationary whistle emits sound of frequency $f_0$. A wind blows with speed $w$ from west to east:
(A) An observer stationed east of the whistle hears a frequency $f_0$.  
(B) The wavelength of sound waves measured by an observer east of the whistle is $\\frac{v + w}{f_0}$.  
(C) The speed of sound relative to the ground is $v + w$ in the east direction and $v - w$ in the west direction.  
(D) The pitch of the sound heard by an observer stationary relative to the ground does not change with wind speed.

#### Question 5 (Electrostatics — Dipole Field Gradient)
A short electric dipole $\\vec{p} = p\\hat{k}$ is located at the origin. Which of the following statements is/are correct?
(A) The electrostatic potential at $(r, \\theta)$ is $V(r, \\theta) = \\frac{1}{4\\pi \\varepsilon_0} \\frac{p \\cos\\theta}{r^2}$.  
(B) The radial electric field component is $E_r = \\frac{1}{4\\pi \\varepsilon_0} \\frac{2p \\cos\\theta}{r^3}$.  
(C) The polar electric field component is $E_\\theta = \\frac{1}{4\\pi \\varepsilon_0} \\frac{p \\sin\\theta}{r^3}$.  
(D) The total electric field magnitude is $E = \\frac{p}{4\\pi \\varepsilon_0 r^3} \\sqrt{1 + 3\\cos^2\\theta}$.

#### Question 6 (Ray Optics — Refraction at Spherical Surface)
A glass sphere of radius $R$ and refractive index $\\mu = 1.50$ is placed in air:
(A) A parallel beam of light incident on the sphere comes to a focus at a distance of $R/2$ beyond the back surface.  
(B) An object placed at the surface of the sphere forms a virtual image at the same position.  
(C) A point object placed at the center of the sphere forms an image at the center itself.  
(D) The power of the complete glass sphere is positive.

#### Question 7 (Modern Physics — Bohr Energy of Hydrogen)
In the hydrogen atom:
(A) The radius of the $n$-th orbit is proportional to $n^2$.  
(B) The orbital velocity of the electron is inversely proportional to $n$.  
(C) The orbital period of the electron is proportional to $n^3$.  
(D) The magnetic dipole moment $\\mu_L$ of the electron is proportional to $n$.

#### Question 8 (Oscillations — Damped Oscillator Decay)
In an underdamped harmonic oscillator of mass $m$, spring constant $k$, and damping coefficient $b$:
(A) The equation of motion is $m \\ddot{x} + b \\dot{x} + k x = 0$.  
(B) The amplitude decays exponentially as $A(t) = A_0 e^{-b t / (2m)}$.  
(C) The damped angular frequency is $\\omega = \\sqrt{\\frac{k}{m} - \\frac{b^2}{4m^2}}$.  
(D) The mechanical energy decays exponentially as $E(t) = E_0 e^{-b t / m}$.

---

## Section 2: Numerical Value Questions (Questions 9 to 14)

#### Question 9 (Mechanics — Rotational Inertia of Disc)
A uniform circular disc of mass $M = 4.0\\text{ kg}$ and radius $R = 0.50\\text{ m}$ is rotated about an axis perpendicular to the disc and passing through a point on its circumference. Calculate the moment of inertia $I$ (in $\\text{kg}\\cdot\\text{m}^2$).

#### Question 10 (Electrodynamics — Induced Current in Ring)
A circular loop of wire of radius $r = 0.10\\text{ m}$ and resistance $R = 2.0\\ \\Omega$ is placed in a magnetic field directed perpendicular to the loop that changes at rate $\\frac{dB}{dt} = 5.0\\text{ T/s}$. Calculate the induced current $I$ (in mA) rounded to the nearest integer. [Take $\\pi = 3.14$].

#### Question 11 (Thermodynamics — Isothermal Work)
Two moles of an ideal gas at $T = 300\\text{ K}$ expand isothermally from $V_1 = 2.0\\text{ L}$ to $V_2 = 8.0\\text{ L}$. Calculate the work done $W$ by the gas (in kJ). [Take $R = 8.314\\text{ J/(mol}\\cdot\\text{K)}$, $\\ln 4 = 1.386$].

#### Question 12 (Wave Motion — Doppler Shift)
A source of sound of frequency $f_0 = 500\\text{ Hz}$ moves toward a stationary observer at $v_s = 34.0\\text{ m/s}$. If the speed of sound is $v = 340.0\\text{ m/s}$, find the apparent frequency $f'$ (in Hz).

#### Question 13 (Electrostatics — Potential of Sphere)
A conducting sphere of radius $R = 0.20\\text{ m}$ has a charge $Q = 4.0\\ \\mu\\text{C}$. Calculate the electric potential at a distance $r = 0.10\\text{ m}$ from the center (in kV). [Take $\\frac{1}{4\\pi\\varepsilon_0} = 9.0\\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$].

#### Question 14 (Modern Physics — Photoelectric Stopping Potential)
Light of frequency $\\nu = 1.5\\times 10^{15}\\text{ Hz}$ falls on a metal with work function $\\Phi = 2.2\\text{ eV}$. Find the stopping potential $V_0$ (in Volts). [Take $h = 4.14\\times 10^{-15}\\text{ eV}\\cdot\\text{s}$].

---

## Section 3: Single Correct Questions (Questions 15 to 18)

#### Question 15 (Mechanics — Range of Projectile on Incline)
A projectile is fired up an inclined plane of inclination angle $\\beta$ with initial speed $u$ at an angle $\\alpha$ with the horizontal. The condition for maximum range up the incline is:
(A) $\\alpha = \\frac{\\pi}{4} + \\frac{\\beta}{2}$  
(B) $\\alpha = \\frac{\\pi}{4} - \\frac{\\beta}{2}$  
(C) $\\alpha = \\frac{\\pi}{2} - \\beta$  
(D) $\\alpha = \\frac{\\beta}{2}$

#### Question 16 (Electrostatics — Parallel Plate Force)
The electrostatic attractive force between the two plates of a parallel-plate capacitor carrying charges $+Q$ and $-Q$ of area $A$ is:
(A) $\\frac{Q^2}{2\\varepsilon_0 A}$  
(B) $\\frac{Q^2}{\\varepsilon_0 A}$  
(C) $\\frac{2Q^2}{\\varepsilon_0 A}$  
(D) $\\frac{Q^2}{4\\varepsilon_0 A}$

#### Question 17 (Electromagnetism — Force on Wire in Magnetic Field)
A straight wire of length $L = 0.5\\text{ m}$ carrying current $I = 2.0\\text{ A}$ is placed in a uniform magnetic field $B = 0.4\\text{ T}$ at an angle of $30^\\circ$ to the field. The magnetic force on the wire is:
(A) $0.20\\text{ N}$  
(B) $0.40\\text{ N}$  
(C) $0.10\\text{ N}$  
(D) $0.35\\text{ N}$

#### Question 18 (Geometric Optics — Critical Angle)
The critical angle for total internal reflection from a medium of refractive index $\\mu = \\sqrt{2}$ into air is:
(A) $45^\\circ$  
(B) $30^\\circ$  
(C) $60^\\circ$  
(D) $90^\\circ$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Multiple Correct Questions (Questions 19 to 26)

#### Question 19 (Coordination Chemistry — Isomers of Pt(II))
For the square planar complex $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$:
(A) It exists as cis and trans geometrical isomers.  
(B) The cis-isomer (cisplatin) is an important anticancer chemotherapy drug.  
(C) Both isomers are square planar and diamagnetic ($d^8$ low spin).  
(D) Both isomers are optically active and can be resolved into enantiomers.

#### Question 20 (Physical Chemistry — Elevation of Boiling Point)
For a dilute solution of a non-volatile solute in a volatile solvent:
(A) The boiling point of the solution is higher than that of the pure solvent.  
(B) The elevation of boiling point $\\Delta T_b$ is directly proportional to the molality of the solute.  
(C) The ebullioscopic constant $K_b$ depends only on the nature of the solvent.  
(D) The freezing point of the solution is also elevated.

#### Question 21 (Organic Chemistry — Stereochemistry of Addition to Alkenes)
Regarding the addition of bromine ($\\text{Br}_2$) to alkenes:
(A) Addition proceeds via a cyclic bromonium ion intermediate.  
(B) The reaction is an anti-addition stereochemically.  
(C) Addition of $\\text{Br}_2$ to cis-but-2-ene produces a racemic mixture of $(\\pm)$-2,3-dibromobutane.  
(D) Addition of $\\text{Br}_2$ to trans-but-2-ene produces meso-2,3-dibromobutane.

#### Question 22 (Inorganic Chemistry — Extraction of Iron)
In the blast furnace for the metallurgy of iron:
(A) Hematite ($\\text{Fe}_2\\text{O}_3$) is reduced to spongy iron by carbon monoxide in the upper zone.  
(B) Calcium carbonate is added as a flux to remove silica as slag $\\text{CaSiO}_3$.  
(C) Molten slag floats on top of molten iron because it has lower density.  
(D) Wrought iron is the purest commercial form of iron.

#### Question 23 (Chemical Kinetics — Arrhenius Equation Parameters)
According to the Arrhenius equation $k = A e^{-E_a / RT}$:
(A) A plot of $\\ln k$ versus $1/T$ yields a straight line with slope $-E_a / R$.  
(B) The pre-exponential factor $A$ has the same units as the rate constant $k$.  
(C) Reactions with higher activation energies are more temperature-sensitive.  
(D) A catalyst increases the reaction rate by lowering the activation energy $E_a$.

#### Question 24 (Electrochemistry — Standard Reduction Potentials)
Given standard reduction potentials: $E^\\circ(\\text{Zn}^{2+}/\\text{Zn}) = -0.76\\text{ V}$, $E^\\circ(\\text{Fe}^{2+}/\\text{Fe}) = -0.44\\text{ V}$, $E^\\circ(\\text{Cu}^{2+}/\\text{Cu}) = +0.34\\text{ V}$:
(A) Zinc is a stronger reducing agent than iron.  
(B) Zinc can displace copper from aqueous copper sulfate solution.  
(C) The EMF of the cell $\\text{Zn} \\mid \\text{Zn}^{2+} \\parallel \\text{Cu}^{2+} \\mid \\text{Cu}$ is $+1.10\\text{ V}$.  
(D) Copper can displace hydrogen from dilute hydrochloric acid.

#### Question 25 (Organic Chemistry — Acidity of Phenols)
Regarding the acidity of substituted phenols:
(A) Phenol is more acidic than ethanol due to resonance stabilization of the phenoxide ion.  
(B) p-Nitrophenol is more acidic than phenol due to the strong $-M$ and $-I$ effects of the nitro group.  
(C) o-Nitrophenol is less acidic than p-nitrophenol due to intramolecular hydrogen bonding.  
(D) p-Cresol is more acidic than phenol.

#### Question 26 (Solid State — Crystal Packing)
In close-packed arrangements of identical spheres:
(A) Hexagonal close packing (HCP) has the stacking sequence $ABABAB\\dots$  
(B) Cubic close packing (CCP/FCC) has the stacking sequence $ABCABC\\dots$  
(C) Both HCP and CCP have identical packing efficiency of $74\\%$.  
(D) The coordination number of each sphere in both HCP and CCP is 12.

---

## Section 2: Numerical Value Questions (Questions 27 to 32)

#### Question 27 (Physical Chemistry — Depression of Freezing Point)
A solution containing $1.80\\text{ g}$ of glucose (molar mass $180\\text{ g/mol}$) dissolved in $100.0\\text{ g}$ of water has a freezing point depression $\\Delta T_f$ (in K). Given $K_f = 1.86\\text{ K}\\cdot\\text{kg/mol}$, calculate $\\Delta T_f$ rounded to three decimal places.

#### Question 28 (Electrochemistry — Moles of Metal Deposited)
During the electrolysis of molten $\\text{Al}_2\\text{O}_3$, a current of $I = 9.65\\text{ A}$ is passed for $t = 10,000\\text{ s}$. Calculate the moles of aluminum metal deposited. [Take $F = 96,500\\text{ C/mol}$].

#### Question 29 (Chemical Kinetics — First-Order Rate Constant)
A first-order reaction has a half-life $t_{1/2} = 69.3\\text{ s}$. Calculate the rate constant $k$ (in $\\text{s}^{-1}$) multiplied by $100$.

#### Question 30 (Coordination Chemistry — Coordination Number)
Find the coordination number of iron in the complex ion $[\\text{Fe}(\\text{EDTA})]^{-}$.

#### Question 31 (Organic Chemistry — Number of Monobromo Products)
Find the total number of constitutional isomers formed upon monobromination of propane.

#### Question 32 (Ionic Equilibria — pH of Strong Acid)
Calculate the pH of a $0.0010\\text{ M}$ solution of hydrochloric acid $\\text{HCl}$ at $298\\text{ K}$.

---

## Section 3: Single Correct Questions (Questions 33 to 36)

#### Question 33 (Inorganic Chemistry — White Vitriol)
The chemical formula of white vitriol is:
(A) $\\text{ZnSO}_4\\cdot 7\\text{H}_2\\text{O}$  
(B) $\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}$  
(C) $\\text{FeSO}_4\\cdot 7\\text{H}_2\\text{O}$  
(D) $\\text{MgSO}_4\\cdot 7\\text{H}_2\\text{O}$

#### Question 34 (Organic Chemistry — Reagent for Aldehyde to Alcohol)
Which of the following reducing agents selectively reduces aldehydes and ketones to alcohols without affecting ester or carboxylic acid groups?
(A) Sodium borohydride ($\\text{NaBH}_4$)  
(B) Lithium aluminum hydride ($\\text{LiAlH}_4$)  
(C) Hydrogen with platinum ($\\text{H}_2 / \\text{Pt}$)  
(D) Sodium in liquid ammonia

#### Question 35 (Physical Chemistry — Ideal Gas Internal Energy)
The internal energy of an ideal gas depends solely on its:
(A) Temperature  
(B) Volume  
(C) Pressure  
(D) Density

#### Question 36 (Biomolecules — Essential Amino Acids)
Which of the following is an essential amino acid for human nutrition?
(A) Valine  
(B) Glycine  
(C) Alanine  
(D) Serine

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Multiple Correct Questions (Questions 37 to 44)

#### Question 37 (Calculus — Extreme Value Theorem & Fermat's Theorem)
Let $f(x) = x^3 - 3x + 2$ defined on $[-2, 2]$:
(A) $f'(x) = 3(x - 1)(x + 1)$.  
(B) $x = -1$ is a local maximum point with $f(-1) = 4$.  
(C) $x = 1$ is a local minimum point with $f(1) = 0$.  
(D) The absolute maximum value on $[-2, 2]$ is $4$ and absolute minimum is $0$.

#### Question 38 (Coordinate Geometry — Tangents to Parabola)
Let $y^2 = 4ax$ be a parabola. Tangents are drawn from point $P(x_1, y_1)$ to the parabola:
(A) If $x_1 = -a$, the tangents are mutually perpendicular.  
(B) The chord of contact of the tangents is $y y_1 = 2a(x + x_1)$.  
(C) If the chord of contact passes through the focus $(a, 0)$, then $x_1 = -a$.  
(D) The locus of the point of intersection of perpendicular tangents is the directrix.

#### Question 39 (Algebra — Matrices & Inverses)
Let $A$ and $B$ be two $n \\times n$ invertible matrices:
(A) $(A B)^{-1} = B^{-1} A^{-1}$  
(B) $\\det(A B) = \\det(A) \\det(B)$  
(C) $(A^T)^{-1} = (A^{-1})^T$  
(D) $\\det(A^{-1}) = \\frac{1}{\\det(A)}$

#### Question 40 (Calculus — Fundamental Theorem of Calculus)
Let $F(x) = \\int_{0}^{x^2} \\cos(t) \\, dt$:
(A) $F'(x) = 2x \\cos(x^2)$ by Leibniz's rule.  
(B) $F(0) = 0$.  
(C) $F'(0) = 0$.  
(D) $F(x) = \\sin(x^2)$.

#### Question 41 (Vectors & 3D Geometry — Line in Plane)
Let line $L: \\frac{x - 1}{2} = \\frac{y - 2}{3} = \\frac{z - 3}{4}$ and plane $\\Pi: x + y - z = 0$:
(A) The line $L$ is parallel to the plane $\\Pi$.  
(B) The point $(1, 2, 3)$ lies on the plane $\\Pi$.  
(C) The line $L$ lies entirely in the plane $\\Pi$.  
(D) The distance between the line $L$ and the plane $\\Pi$ is zero.

#### Question 42 (Probability — Independent Events)
If $A$ and $B$ are independent events:
(A) $P(A \\cap B) = P(A) P(B)$  
(B) $P(A \\mid B) = P(A)$  
(C) $P(A^c \\cap B^c) = P(A^c) P(B^c)$  
(D) $P(A \\cup B) = P(A) + P(B) - P(A) P(B)$

#### Question 43 (Complex Numbers — Euler Formula & De Moivre)
For any complex number $z = e^{i \\theta}$:
(A) $|z| = 1$  
(B) $z^n = \\cos(n\\theta) + i \\sin(n\\theta)$  
(C) $\\overline{z} = \\frac{1}{z}$  
(D) $z + \\overline{z} = 2\\cos\\theta$

#### Question 44 (Differential Equations — Separable Variables)
For the differential equation $\\frac{dy}{dx} = \\frac{y}{x}$:
(A) The variables are separable: $\\frac{dy}{y} = \\frac{dx}{x}$.  
(B) The general solution is a family of straight lines passing through the origin: $y = C x$.  
(C) The orthogonal trajectories are concentric circles: $x^2 + y^2 = K$.  
(D) The equation is homogeneous of degree 0.

---

## Section 2: Numerical Value Questions (Questions 45 to 50)

#### Question 45 (Calculus — Limit of Indeterminate Form)
Evaluate the limit:
$$L = \\lim_{x \\to 0} \\frac{e^{2x} - 1}{\\sin(3x)}$$
Find the value of $L$ rounded to two decimal places.

#### Question 46 (Coordinate Geometry — Eccentricity of Hyperbola)
Find the eccentricity $e$ of the rectangular hyperbola $x^2 - y^2 = 16$ rounded to two decimal places.

#### Question 47 (Algebra — Determinant of Matrix)
Calculate the determinant of the $3 \\times 3$ matrix:
$$A = \\begin{pmatrix} 1 & 0 & 2 \\\\ 0 & 3 & 1 \\\\ 4 & 2 & 0 \\end{pmatrix}$$

#### Question 48 (Vectors — Cross Product Magnitude)
If $|\\vec{a}| = 2$, $|\\vec{b}| = 5$, and $|\\vec{a} \\cdot \\vec{b}| = 6$, calculate the magnitude of their cross product $|\\vec{a} \\times \\vec{b}|$.

#### Question 49 (Differential Equations — Slope of Orthogonal Trajectory)
The slope of the orthogonal trajectory to the family of curves $y = C x$ at the point $(3, 4)$ is $m$. Find the value of $-m$ rounded to two decimal places.

#### Question 50 (Probability — Two Heads in Three Tosses)
A fair coin is tossed 3 times. Find the probability of getting exactly two heads.

---

## Section 3: Single Correct Questions (Questions 51 to 54)

#### Question 51 (Calculus — Tangent to Circle)
The equation of the tangent to the circle $x^2 + y^2 = 25$ at the point $(3, 4)$ is:
(A) $3x + 4y = 25$  
(B) $4x + 3y = 25$  
(C) $3x - 4y = 25$  
(D) $4x - 3y = 25$

#### Question 52 (Trigonometry — Maximum Value of Linear Combination)
The maximum value of $f(x) = 3\\sin x + 4\\cos x$ is:
(A) $5$  
(B) $7$  
(C) $1$  
(D) $25$

#### Question 53 (Coordinate Geometry — Focus of Parabola)
The coordinates of the focus of the parabola $y^2 = 12x$ are:
(A) $(3, 0)$  
(B) $(0, 3)$  
(C) $(-3, 0)$  
(D) $(6, 0)$

#### Question 54 (Differential Calculus — Increasing Interval)
The function $f(x) = x^2 - 4x + 3$ is strictly increasing on the interval:
(A) $[2, \\infty)$  
(B) $(-\\infty, 2]$  
(C) $[0, 2]$  
(D) $(-\\infty, \\infty)$
"""

    with open('mock_tests/Mock_05_IIT_Delhi/Paper_1.md', 'w', encoding='utf-8') as f:
        f.write(p1)
    print("Generated mock_tests/Mock_05_IIT_Delhi/Paper_1.md")

if __name__ == '__main__':
    create_mock_05()

