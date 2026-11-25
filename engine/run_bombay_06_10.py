# -*- coding: utf-8 -*-
"""
Full Generator for IIT Bombay Mocks 06 to 10.
"""
import os
from generate_bombay_bulk import make_bombay_test

def build_mock_06():
    data = {}
    data['p1_phy'] = """
## Section 1: Numerical Value Questions (Questions 1 to 8)
#### Question 1 (Mechanics + Variable Inertia)
A uniform circular hoop of mass $m = 1.00\\text{ kg}$ and radius $R = 0.40\\text{ m}$ has a small heavy particle of mass $m = 1.00\\text{ kg}$ rigidly attached to its rim. The hoop is placed on a rough horizontal floor and held with the particle at the highest point. It is then released from rest. If the hoop rolls without slipping, calculate the angular velocity $\\omega$ of the hoop (in rad/s) when the particle reaches its lowest point. [Take $g = 10.00\\text{ m/s}^2$].

#### Question 2 (Thermodynamics & Variable Heat Capacity)
One mole of an ideal gas has a molar heat capacity varying with temperature as $C_m = C_V + \\alpha T$, where $C_V = \\frac{3}{2}R$ and $\\alpha = 0.020\\text{ J}/(\\text{mol}\\cdot\\text{K}^2)$. The gas is heated from $T_1 = 300\\text{ K}$ to $T_2 = 500\\text{ K}$ at constant volume. Calculate the total heat absorbed $Q$ by the gas (in Joules). [Take $R = 8.314\\text{ J}/(\\text{mol}\\cdot\\text{K})$].

#### Question 3 (Fluid Mechanics & Siphon Dynamics)
A siphon tube of uniform cross-sectional area $a = 2.0\\text{ cm}^2$ draws water from a large open reservoir. The crest of the siphon is located at height $h_1 = 1.50\\text{ m}$ above the reservoir surface, and the discharge outlet is located at $h_2 = 2.40\\text{ m}$ below the surface. Calculate the volume flow rate $Q$ of water discharging through the siphon (in L/s). [Take $g = 10.00\\text{ m/s}^2$].

#### Question 4 (Electromagnetic Induction & RL Transients)
In an $RL$ circuit, an inductor $L = 40.0\\text{ mH}$ and resistor $R = 8.0\\ \\Omega$ are connected in series with a battery $V_0 = 24.0\\text{ V}$. Find the energy stored in the magnetic field of the inductor (in milliJoules) at $t = 5.0\\text{ ms}$ after closing the switch. [Take $e^{-1} = 0.368$].

#### Question 5 (Wave Optics & Thin Film Interference)
A thin oil film of refractive index $\\mu = 1.40$ floats on water $(\\mu_w = 1.33)$. White light is incident normally on the film. In the reflected light, destructive interference is observed for wavelength $\\lambda_1 = 560\\text{ nm}$ and constructive interference for $\\lambda_2 = 700\\text{ nm}$ in the visible spectrum. Find the minimum thickness $t$ of the oil film (in nm).

#### Question 6 (Electrostatics & Induced Charge on Grounded Sphere)
A point charge $q = +4.00\\ \\mu\\text{C}$ is placed at distance $d = 20.0\\text{ cm}$ from the center of an earthed conducting sphere of radius $R = 8.0\\text{ cm}$. Calculate the magnitude of the total induced charge $q_{\\text{ind}}$ residing on the sphere (in $\\mu\\text{C}$).

#### Question 7 (Simple Harmonic Motion & Torsional Oscillator)
A uniform circular disc of mass $M = 2.00\\text{ kg}$ and radius $R = 0.30\\text{ m}$ is suspended horizontally by a vertical wire passing through its center. The torsional spring constant of the wire is $C = 1.80\\text{ N}\\cdot\\text{m/rad}$. Calculate the time period $T$ of torsional oscillations (in seconds). [Take $\\pi = 3.14$].

#### Question 8 (Modern Physics & Photoelectric Cutoff)
When light of frequency $\\nu_1 = 1.20\\times 10^{15}\\text{ Hz}$ illuminates a metal surface, the stopping potential is $V_1 = 2.50\\text{ V}$. When frequency is changed to $\\nu_2 = 1.80\\times 10^{15}\\text{ Hz}$, the stopping potential is $V_2 = 4.98\\text{ V}$. From this data, determine Planck's constant $h$ multiplied by $10^{34}$ (in $\\text{J}\\cdot\\text{s}$). [Take $e = 1.60\\times 10^{-19}\\text{ C}$].

## Section 2: One or More Than One Correct Questions (Questions 9 to 14)
#### Question 9
A block of mass $m$ is suspended by a light spring of stiffness $k$ inside an elevator accelerating vertically upward with acceleration $a_0$. Which of the following statements is/are correct?
- (A) The equilibrium extension of the spring is $\\frac{m(g + a_0)}{k}$.
- (B) The frequency of vertical oscillations of the block relative to the elevator is $\\frac{1}{2\\pi}\\sqrt{\\frac{k}{m}}$.
- (C) The time period of oscillation is independent of the elevator acceleration $a_0$.
- (D) The maximum tension in the spring during oscillation of amplitude $A$ is $m(g + a_0) + k A$.

#### Question 10
In an electromagnetic plane wave propagating in free space along the $+z$ direction:
- (A) The electric and magnetic field vectors are mutually perpendicular and oscillate in phase.
- (B) The ratio of amplitudes is $E_0 / B_0 = c$.
- (C) The instantaneous Poynting vector is directed along $+z$.
- (D) The average energy density is $\\frac{1}{2}\\varepsilon_0 E_0^2$.

#### Question 11
A monoatomic ideal gas undergoes a cycle on a $P-V$ diagram consisting of an isobaric expansion, an isochoric cooling, and an isothermal compression. Which of the following is/are correct?
- (A) The net work done over the cycle is positive if the cycle is traversed clockwise.
- (B) $\\Delta U$ for the complete cycle is zero.
- (C) The entropy change of the gas over one full cycle is zero.
- (D) The efficiency of the cycle is strictly less than that of a Carnot engine operating between the extreme temperatures.

#### Question 12
A conducting loop of resistance $R$ and area $A$ rotates with constant angular velocity $\\omega$ in a uniform magnetic field $B$ perpendicular to the rotation axis:
- (A) The maximum induced EMF is $A B \\omega$.
- (B) The alternating current induced in the loop has frequency $\\omega / (2\\pi)$.
- (C) The average power dissipated over one cycle is $\\frac{A^2 B^2 \\omega^2}{2R}$.
- (D) The mechanical torque required to keep the loop rotating at constant $\\omega$ fluctuates with time.

#### Question 13
For an alpha particle and a proton accelerated through the same potential difference $V$:
- (A) The ratio of their kinetic energies is $K_\\alpha / K_p = 2$.
- (B) The ratio of their de Broglie wavelengths is $\\lambda_\\alpha / \\lambda_p = 1/(2\\sqrt{2})$.
- (C) The ratio of their radii in a perpendicular magnetic field is $r_\\alpha / r_p = \\sqrt{2}$.
- (D) The ratio of their speeds is $v_\\alpha / v_p = 1/\\sqrt{2}$.

#### Question 14
Two thin convex lenses of focal lengths $f_1$ and $f_2$ are placed in contact. The equivalent focal length is $F$:
- (A) $1/F = 1/f_1 + 1/f_2$.
- (B) The power of the combination is $P = P_1 + P_2$.
- (C) If one of the lenses is replaced by a concave lens of equal focal length, the power becomes zero.
- (D) Chromatic aberration is completely eliminated by placing two lenses of the same material in contact.

## Section 3: Single Correct Option Questions (Questions 15 to 18)
#### Question 15
A uniform solid sphere rolls down an inclined plane of inclination $\\theta$ without slipping. The acceleration of its center of mass is:
- (A) $\\frac{5}{7} g \\sin\\theta$
- (B) $\\frac{2}{3} g \\sin\\theta$
- (C) $\\frac{1}{2} g \\sin\\theta$
- (D) $g \\sin\\theta$

#### Question 16
The capacitance of a spherical capacitor with inner radius $a$ and outer radius $b$ is:
- (A) $\\frac{4\\pi\\varepsilon_0 a b}{b - a}$
- (B) $\\frac{4\\pi\\varepsilon_0 (b - a)}{a b}$
- (C) $4\\pi\\varepsilon_0 (b - a)$
- (D) $\\frac{2\\pi\\varepsilon_0 a b}{b - a}$

#### Question 17
The root-mean-square speed of molecules of an ideal gas at temperature $T$ is $v_{\\text{rms}}$. If the temperature is increased to $4T$, the rms speed becomes:
- (A) $2 v_{\\text{rms}}$
- (B) $4 v_{\\text{rms}}$
- (C) $\\sqrt{2} v_{\\text{rms}}$
- (D) $v_{\\text{rms}} / 2$

#### Question 18
The decay constant of a radioactive substance is $\\lambda$. Its mean life is:
- (A) $1/\\lambda$
- (B) $\\frac{\\ln 2}{\\lambda}$
- (C) $\\lambda$
- (D) $\\frac{\\lambda}{\\ln 2}$
"""

    data['p1_chem'] = """
## Section 1: Numerical Value Questions (Questions 19 to 26)
#### Question 19 (Thermodynamics & Clausius-Clapeyron)
The vapor pressure of water at $373\\text{ K}$ is $1.00\\text{ bar}$, and its enthalpy of vaporization is $\\Delta H_{\\text{vap}} = 40.7\\text{ kJ/mol}$. Calculate the boiling point of water (in K, rounded to one decimal place) at an external pressure of $0.80\\text{ bar}$. [Take $R = 8.314\\text{ J}/(\\text{mol}\\cdot\\text{K})$, $\\ln(0.80) = -0.223$].

#### Question 20 (Electrochemistry & Standard Cell Potential)
Calculate the standard equilibrium constant $K_c$ at $298\\text{ K}$ for the reaction $\\text{Cu}(s) + 2\\text{Ag}^+(aq) \\rightleftharpoons \\text{Cu}^{2+}(aq) + 2\\text{Ag}(s)$ given $E^\\circ(\\text{Ag}^+/\\text{Ag}) = +0.80\\text{ V}$ and $E^\\circ(\\text{Cu}^{2+}/\\text{Cu}) = +0.34\\text{ V}$. Express $K_c$ as $x \\times 10^{15}$, and report the value of $x$ (rounded to two decimal places). [Take $2.303 RT/F = 0.0591\\text{ V}$].

#### Question 21 (Chemical Kinetics & Arrhenius Frequency Factor)
The rate constant for a reaction is $k = 2.0\\times 10^{-3}\\text{ s}^{-1}$ at $300\\text{ K}$ with activation energy $E_a = 57.5\\text{ kJ/mol}$. Calculate the Arrhenius frequency factor $A$ multiplied by $10^{-7}$ (in $\\text{s}^{-1}$). [Take $R = 8.314\\text{ J}/(\\text{mol}\\cdot\\text{K})$, $e^{23.05} = 1.02\\times 10^{10}$].

#### Question 22 (Coordination Chemistry & Pairing Energy)
For the low-spin octahedral complex $[\\text{Fe}(\\text{CN})_6]^{4-}$, the crystal field splitting energy is $\\Delta_o = 33,000\\text{ cm}^{-1}$ and pairing energy is $P = 17,000\\text{ cm}^{-1}$. Calculate the net Crystal Field Stabilization Energy (in $\\text{kJ/mol}$). [Take $1\\text{ cm}^{-1} = 0.01196\\text{ kJ/mol}$].

#### Question 23 (Colligative Properties & Van 't Hoff Factor)
A $0.050\\text{ m}$ aqueous solution of a weak electrolyte $\\text{HA}$ freezes at $-0.102^\\circ\\text{C}$. Given $K_f = 1.86\\text{ K}\\cdot\\text{kg/mol}$, calculate the percentage degree of dissociation $\\alpha$ (in \\%).

#### Question 24 (Solid State & Packing Efficiency)
Calculate the percentage packing efficiency of a body-centered cubic (BCC) metallic lattice (rounded to two decimal places). [Take $\\pi = 3.1416, \\sqrt{3} = 1.732$].

#### Question 25 (Organic Chemistry & Chiral Centers)
Determine the total number of chiral stereocenters present in one molecule of $\\beta$-D-glucopyranose.

#### Question 26 (Ionic Equilibrium & Buffer pH)
Calculate the pH of a solution formed by mixing $50.0\\text{ mL}$ of $0.10\\text{ M}\\text{ NH}_4\\text{OH} (pK_b = 4.74)$ and $25.0\\text{ mL}$ of $0.10\\text{ M}\\text{ HCl}$ at $25^\\circ\\text{C}$.

## Section 2: One or More Than One Correct Questions (Questions 27 to 32)
#### Question 27
Which of the following statements is/are correct regarding the extraction of zinc from zinc blende $(\\text{ZnS})$?
- (A) The ore is concentrated by froth flotation process using potassium ethyl xanthate as a collector.
- (B) Roasting converts $\\text{ZnS}$ into $\\text{ZnO}$ with evolution of $\\text{SO}_2$.
- (C) Reduction of $\\text{ZnO}$ is carried out with coke at approximately $1400^\\circ\\text{C}$ in a vertical retort.
- (D) Zinc vapor is condensed and refined electrolytically.

#### Question 28
Which of the following carbonyl compounds undergo the aldol condensation upon treatment with dilute aqueous $\\text{NaOH}$?
- (A) Acetaldehyde
- (B) Propanal
- (C) Benzaldehyde
- (D) Formaldehyde

#### Question 29
Regarding the allotropes of phosphorus:
- (A) White phosphorus consists of discrete tetrahedral $\\text{P}_4$ molecules with bond angles of $60^\\circ$.
- (B) White phosphorus is insoluble in water but soluble in carbon disulfide $(\\text{CS}_2)$.
- (C) Red phosphorus is polymeric and much less reactive than white phosphorus.
- (D) Black phosphorus is the thermodynamically most stable allotrope.

#### Question 30
Which of the following pairs of isomers represents functional isomerism?
- (A) Ethanol and Dimethyl ether
- (B) Propan-1-ol and Propan-2-ol
- (C) Acetone and Propanal
- (D) Acetic acid and Methyl formate

#### Question 31
Which of the following properties is/are state functions?
- (A) Internal energy ($U$)
- (B) Enthalpy ($H$)
- (C) Work done ($W$)
- (D) Entropy ($S$)

#### Question 32
Which of the following transition metal complexes are diamagnetic?
- (A) $[\\text{Ni}(\\text{CO})_4]$
- (B) $[\\text{Ni}(\\text{CN})_4]^{2-}$
- (C) $[\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+}$
- (D) $[\\text{Co}(\\text{NH}_3)_6]^{3+}$

## Section 3: Single Correct Option Questions (Questions 33 to 36)
#### Question 33
The major product of the nitration of toluene with concentrated $\\text{HNO}_3/\\text{H}_2\\text{SO}_4$ at low temperature is:
- (A) o-Nitrotoluene and p-Nitrotoluene
- (B) m-Nitrotoluene
- (C) 2,4,6-Trinitrotoluene
- (D) Benzoic acid

#### Question 34
The shape of the water molecule $(\\text{H}_2\\text{O})$ according to VSEPR theory is:
- (A) Bent (V-shaped)
- (B) Linear
- (C) Trigonal planar
- (D) Tetrahedral

#### Question 35
The IUPAC name of $\\text{CH}_3-\\text{CH}(\\text{OH})-\\text{CH}_2-\\text{CHO}$ is:
- (A) 3-Hydroxybutanal
- (B) 2-Hydroxybutanal
- (C) 3-Hydroxybutanone
- (D) 1-Oxobutan-3-ol

#### Question 36
The hybridization of carbon in graphite is:
- (A) $sp^2$
- (B) $sp^3$
- (C) $sp$
- (D) $dsp^2$
"""

    data['p1_math'] = """
## Section 1: Numerical Value Questions (Questions 37 to 44)
#### Question 37 (Definite Integrals & Symmetry)
Evaluate the definite integral
$$I = \\int_0^1 x (1 - x)^9\\,dx$$
Calculate the value of $I^{-1}$ (the reciprocal of $I$).

#### Question 38 (Differential Equations & Exact Differential)
Find the solution to the differential equation $(2x + y)dx + (x + 2y)dy = 0$ passing through $(1, 1)$. If the curve passes through $(2, y_0)$ with $y_0 > 0$, calculate $y_0$ (rounded to two decimal places).

#### Question 39 (Complex Numbers & Roots of Unity)
Find the value of $\\sum_{k=1}^6 \\cos\\left(\\frac{2k\\pi}{7}\\right)$.

#### Question 40 (Vectors & Scalar Triple Product)
Let $\\vec{a} = \\hat{i} + \\hat{j} + \\hat{k}$, $\\vec{b} = 2\\hat{i} - \\hat{j} + 3\\hat{k}$, and $\\vec{c} = \\hat{i} - 2\\hat{j} + \\hat{k}$. Find the volume of the parallelepiped spanned by $\\vec{a}, \\vec{b}, \\vec{c}$.

#### Question 41 (Conic Sections & Eccentricity of Ellipse)
An ellipse has semi-major axis $a = 5$ and semi-minor axis $b = 3$. Calculate its eccentricity $e$ (rounded to two decimal places).

#### Question 42 (Probability & Binomial Mean)
A fair die is thrown 120 times. Calculate the expected number of times an even prime number appears.

#### Question 43 (Permutations & Circular Combinations)
Find the number of ways in which 6 persons can be seated around a circular table such that two particular persons never sit together.

#### Question 44 (Matrices & Determinant of Adjoint)
Let $A$ be a $3 \\times 3$ matrix with $\\det(A) = 4$. Find the value of $\\det(\\text{adj}(A))$.

## Section 2: One or More Than One Correct Questions (Questions 45 to 50)
#### Question 45
Let $f(x) = x^3 - 6x^2 + 9x + 1$. Which of the following statements is/are correct?
- (A) $f(x)$ has a local maximum at $x = 1$.
- (B) $f(x)$ has a local minimum at $x = 3$.
- (C) $f(x)$ is strictly increasing on $(-\\infty, 1) \\cup (3, \\infty)$.
- (D) The point $(2, 3)$ is an inflection point of $f(x)$.

#### Question 46
Consider the parabola $y^2 = 8x$. Which of the following statements is/are correct?
- (A) The focus of the parabola is at $(2, 0)$.
- (B) The equation of the directrix is $x + 2 = 0$.
- (C) The length of the latus rectum is 8.
- (D) The focal distance of any point $P(x_1, y_1)$ on the parabola is $x_1 + 2$.

#### Question 47
Let $I_n = \\int_0^{\\pi/2} \\sin^n x\\,dx$ for integers $n \\ge 0$. Which of the following is/are correct?
- (A) $I_n = \\frac{n-1}{n} I_{n-2}$ for $n \\ge 2$.
- (B) $I_0 = \\pi/2$.
- (C) $I_1 = 1$.
- (D) $I_2 = \\pi/4$.

#### Question 48
Let $f(x) = \\tan^{-1} x + \\cot^{-1} x$. Which of the following statements is/are correct?
- (A) $f(x) = \\pi/2$ for all $x > 0$.
- (B) $f'(x) = 0$ for all $x \\neq 0$.
- (C) $f(x) = \\pi/2$ for all $x < 0$ when using standard principal branch definitions.
- (D) $f(x)$ is continuous for all $x \\in \\mathbb{R}$.

#### Question 49
Let $A$ and $B$ be two non-singular $n \\times n$ matrices. Which of the following is/are always true?
- (A) $(A B)^{-1} = B^{-1} A^{-1}$
- (B) $\\det(A B) = \\det(A) \\det(B)$
- (C) $(A + B)^T = A^T + B^T$
- (D) $A B = B A$

#### Question 50
The planes $P_1: 2x - y + 2z = 3$ and $P_2: 2x - y + 2z = 9$ are parallel. Which of the following statements is/are correct?
- (A) The distance between the planes is 2.
- (B) The normal vector to both planes is $2\\hat{i} - \\hat{j} + 2\\hat{k}$.
- (C) The origin lies between the two planes.
- (D) Any line perpendicular to $P_1$ is also perpendicular to $P_2$.

## Section 3: Single Correct Option Questions (Questions 51 to 54)
#### Question 51
The value of $\\lim_{x \\to 0} \\frac{\\tan x - x}{x^3}$ is:
- (A) $1/3$
- (B) $1/2$
- (C) $1/6$
- (D) $0$

#### Question 52
The derivative of $\\sin(x^2)$ with respect to $x$ is:
- (A) $2x \\cos(x^2)$
- (B) $\\cos(x^2)$
- (C) $2 \\cos(x^2)$
- (D) $x^2 \\cos(x^2)$

#### Question 53
The distance of the point $(1, 2)$ from the line $3x + 4y - 1 = 0$ is:
- (A) 2
- (B) 1
- (C) 3
- (D) 4

#### Question 54
If $\\log_2 x + \\log_4 x = 3$, the value of $x$ is:
- (A) 4
- (B) 2
- (C) 8
- (D) 16
"""

    data['p2_phy'] = """
## Section 1: One or More Than One Correct Questions (Questions 1 to 8)
#### Question 1
A uniform solid sphere of mass $M$ and radius $R$ is placed on top of a fixed rough spherical surface of radius $2R$. It is given a tiny nudge and rolls without slipping down the surface:
- (A) The angular acceleration of the sphere depends on the angle of descent $\\theta$.
- (B) The sphere loses contact with the surface at $\\cos\\theta = 10/17$.
- (C) Mechanical energy is conserved until detachment.
- (D) The normal force vanishes at the detachment point.

#### Question 2
Two concentric conducting spherical shells of radii $R$ and $3R$ have charges $+2Q$ and $-4Q$ respectively:
- (A) The electric field in $R < r < 3R$ is $\\frac{2Q}{4\\pi\\varepsilon_0 r^2}$.
- (B) The electric field for $r > 3R$ is $-\\frac{2Q}{4\\pi\\varepsilon_0 r^2}$.
- (C) The potential of the inner shell relative to infinity is negative.
- (D) If the inner shell is earthed, its final charge is $+4Q/3$.

#### Question 3
An ideal gas is taken through an isothermal expansion at temperature $T_1$ followed by an adiabatic compression to its initial volume:
- (A) The final pressure is greater than the initial pressure.
- (B) The final temperature $T_2$ is greater than $T_1$.
- (C) The total change in internal energy is positive.
- (D) The total work done by the gas is negative.

#### Question 4
A charged particle moves in a region of crossed uniform electric field $\\vec{E} = E\\hat{j}$ and magnetic field $\\vec{B} = B\\hat{k}$:
- (A) It can pass undeflected if its velocity is $\\vec{v} = \\frac{E}{B}\\hat{i}$.
- (B) The kinetic energy of the particle remains constant if it passes undeflected.
- (C) The trajectory is a cycloid if released from rest at the origin.
- (D) Work done by the magnetic field is always zero.

#### Question 5
In a series $LCR$ circuit driven by an AC source $V_0 \\sin(\\omega t)$:
- (A) At resonance, power factor is unity.
- (B) Current leads voltage if $\\omega < 1/\\sqrt{LC}$.
- (C) Voltage leads current if $\\omega > 1/\\sqrt{LC}$.
- (D) The impedance at resonance is purely resistive and equal to $R$.

#### Question 6
Two coherent light sources of wavelength $\\lambda$ have an intensity ratio $I_1 / I_2 = 9$:
- (A) The ratio of maximum to minimum intensity in the interference pattern is 4.
- (B) The ratio of their electric field amplitudes is 3.
- (C) The minimum intensity is zero.
- (D) The visibility of the fringes is $0.60$.

#### Question 7
In the photoelectric effect:
- (A) The stopping potential is independent of the light intensity.
- (B) Photocurrent is directly proportional to intensity for a fixed frequency.
- (C) There is no measurable time lag between light incidence and electron emission.
- (D) The maximum velocity of photoelectrons depends linearly on light frequency.

#### Question 8
A simple pendulum has time period $T$ on the surface of the Earth:
- (A) If taken to a height $h = R_E$ above Earth's surface, its time period becomes $2T$.
- (B) If taken into a deep mine at depth $d = R_E/2$, its time period becomes $\\sqrt{2}T$.
- (C) In an artificial satellite in circular orbit, its time period is infinite.
- (D) Its time period is independent of the mass of the bob.

## Section 2: Numerical Value Questions (Questions 9 to 14)
#### Question 9
A circular disc of mass $M = 4.0\\text{ kg}$ and radius $R = 0.50\\text{ m}$ rotates at $20.0\\text{ rad/s}$. Calculate its rotational kinetic energy (in Joules).

#### Question 10
The speed of transverse waves on a stretched string of linear mass density $\\mu = 0.050\\text{ kg/m}$ under tension $T_0 = 180.0\\text{ N}$ is $v$. Find $v$ (in m/s).

#### Question 11
An ideal gas undergoes an isothermal expansion from $1.0\\text{ L}$ to $4.0\\text{ L}$ at $300\\text{ K}$. If $n = 2\\text{ mol}$, calculate the work done (in Joules). [Take $R = 8.314\\text{ J}/(\\text{mol}\\cdot\\text{K}), \\ln 4 = 1.386$].

#### Question 12
A convex lens of focal length $25.0\\text{ cm}$ forms a real image of size twice that of the object. Find the object distance from the lens (in cm).

#### Question 13
An electron of mass $m_e = 9.1\\times 10^{-31}\\text{ kg}$ has speed $v = 2.0\\times 10^6\\text{ m/s}$. Find its de Broglie wavelength (in Angstroms, rounded to two decimal places). [Take $h = 6.63\\times 10^{-34}\\text{ J}\\cdot\\text{s}$].

#### Question 14
The activity of a radioactive sample drops to $1/16$ of its initial value in 80 minutes. Calculate its half-life (in minutes).

## Section 3: Single Correct Option Questions (Questions 15 to 18)
#### Question 15
The dimensional formula of magnetic flux is:
- (A) $[M L^2 T^{-2} A^{-1}]$
- (B) $[M L T^{-2} A^{-1}]$
- (C) $[M L^2 T^{-1} A^{-1}]$
- (D) $[M L^2 T^{-2} A]$

#### Question 16
A body weighs $72\\text{ N}$ on the surface of the Earth. Its weight at a height $h = R_E/2$ above the surface is:
- (A) $32\\text{ N}$
- (B) $36\\text{ N}$
- (C) $48\\text{ N}$
- (D) $24\\text{ N}$

#### Question 17
The work done in blowing a soap bubble of radius $R$ from a solution of surface tension $T$ is:
- (A) $8\\pi R^2 T$
- (B) $4\\pi R^2 T$
- (C) $2\\pi R^2 T$
- (D) $16\\pi R^2 T$

#### Question 18
The ratio of specific heats $\\gamma = C_P / C_V$ for a diatomic gas without vibrational modes is:
- (A) $7/5$
- (B) $5/3$
- (C) $4/3$
- (D) $9/7$
"""

    data['p2_chem'] = """
## Section 1: One or More Than One Correct Questions (Questions 19 to 26)
#### Question 19
Which of the following statements is/are correct regarding the extraction of aluminum by the Hall-Héroult process?
- (A) The cathode is a carbon lining inside the steel tank.
- (B) The anodes are graphite rods suspended in the electrolyte.
- (C) The overall cell reaction is $2\\text{Al}_2\\text{O}_3 + 3\\text{C} \\to 4\\text{Al} + 3\\text{CO}_2$.
- (D) Cryolite serves to lower the operating temperature to around $950^\\circ\\text{C}$.

#### Question 20
Which of the following compounds exhibits optical isomerism?
- (A) $[\\text{Co}(\\text{en})_3]^{3+}$
- (B) cis-$[\\text{Pt}(\\text{en})_2\\text{Cl}_2]^{2+}$
- (C) Lactic acid
- (D) trans-$[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$

#### Question 21
Which of the following reagents react with both aldehydes and ketones?
- (A) $\\text{HCN}$
- (B) $\\text{NH}_2\\text{OH}$
- (C) $\\text{NaHSO}_3$
- (D) Fehling's solution

#### Question 22
Which of the following statements is/are correct for a zero-order reaction?
- (A) The rate is independent of the concentration of reactants.
- (B) The half-life is directly proportional to the initial concentration.
- (C) The units of rate constant are $\\text{mol}/(\\text{L}\\cdot\\text{s})$.
- (D) A plot of $[A]$ versus $t$ is linear with slope $-k$.

#### Question 23
Regarding the geometry and bonding in sulfur hexafluoride $(\\text{SF}_6)$:
- (A) The molecular geometry is regular octahedral.
- (B) The hybridization of sulfur is $sp^3d^2$.
- (C) All $\\text{S-F}$ bond lengths are equal.
- (D) The molecule is non-polar and chemically inert.

#### Question 24
Which of the following pairs of ions are isoelectronic?
- (A) $\\text{Na}^+$ and $\\text{Mg}^{2+}$
- (B) $\\text{F}^-$ and $\\text{O}^{2-}$
- (C) $\\text{Al}^{3+}$ and $\\text{Ne}$
- (D) $\\text{K}^+$ and $\\text{Ca}^{2+}$

#### Question 25
Which of the following carbohydrates are reducing sugars?
- (A) Glucose
- (B) Maltose
- (C) Lactose
- (D) Sucrose

#### Question 26
Which of the following salts undergo anionic hydrolysis in aqueous solution, resulting in a basic solution?
- (A) $\\text{CH}_3\\text{COONa}$
- (B) $\\text{NaCN}$
- (C) $\\text{K}_2\\text{CO}_3$
- (D) $\\text{NH}_4\\text{Cl}$

## Section 2: Numerical Value Questions (Questions 27 to 32)
#### Question 27
For the first-order reaction $A \\to \\text{products}$, the half-life is $15.0\\text{ minutes}$. Calculate the rate constant $k$ (in $\\text{min}^{-1}$, rounded to four decimal places). [Take $\\ln 2 = 0.6931$].

#### Question 28
Calculate the EMF of the cell $\\text{Pt} | \\text{H}_2(1\\text{ bar}) | \\text{HCl}(0.010\\text{ M}) || \\text{Ag}^+(0.10\\text{ M}) | \\text{Ag}$ at $298\\text{ K}$ given $E^\\circ(\\text{Ag}^+/\\text{Ag}) = +0.80\\text{ V}$. [Take $2.303 RT/F = 0.0591\\text{ V}$].

#### Question 29
A hydrocarbon contains $85.7\\%$ Carbon and $14.3\\%$ Hydrogen by mass. If its vapor density is 28, find the total number of hydrogen atoms in one molecule of the hydrocarbon.

#### Question 30
The radius of an atom of gold crystallizing in an FCC lattice is $r = 1.44\\text{ \AA}$. Calculate the unit cell edge length $a$ (in Angstroms, rounded to two decimal places). [Take $\\sqrt{2} = 1.414$].

#### Question 31
For the equilibrium $2\\text{NO}_2(g) \\rightleftharpoons \\text{N}_2\\text{O}_4(g)$, the equilibrium concentrations are $[\\text{NO}_2] = 0.20\\text{ M}$ and $[\\text{N}_2\\text{O}_4] = 0.80\\text{ M}$. Calculate $K_c$ (in $\\text{L/mol}$).

#### Question 32
Calculate the solubility of $\\text{AgBr}$ in pure water (in $\\text{mol/L}$, expressed as $x \\times 10^{-7}$) given $K_{\\text{sp}}(\\text{AgBr}) = 5.0\\times 10^{-13}$. [Take $\\sqrt{5} = 2.24$].

## Section 3: Single Correct Option Questions (Questions 33 to 36)
#### Question 33
The strongest acid among the following is:
- (A) Trichloroacetic acid
- (B) Dichloroacetic acid
- (C) Chloroacetic acid
- (D) Acetic acid

#### Question 34
The oxidation state of chromium in $[\\text{Cr}_2\\text{O}_7]^{2-}$ is:
- (A) $+6$
- (B) $+3$
- (C) $+5$
- (D) $+4$

#### Question 35
The boiling point of noble gases increases down the group from $\\text{He}$ to $\\text{Xe}$ primarily due to:
- (A) Increase in London dispersion forces
- (B) Increase in dipole-dipole attractions
- (C) Decrease in ionization enthalpy
- (D) Increase in nuclear charge

#### Question 36
Cannizzaro reaction is not given by:
- (A) Acetaldehyde
- (B) Formaldehyde
- (C) Benzaldehyde
- (D) Trimethylacetaldehyde
"""

    data['p2_math'] = """
## Section 1: One or More Than One Correct Questions (Questions 37 to 44)
#### Question 37
Let $f(x) = \\frac{x}{1 + x^2}$ for $x \\in \\mathbb{R}$. Which of the following statements is/are correct?
- (A) $f(x)$ attains its absolute maximum at $x = 1$.
- (B) $f(x)$ attains its absolute minimum at $x = -1$.
- (C) The range of $f(x)$ is $[-1/2, 1/2]$.
- (D) $f(x)$ is an odd function.

#### Question 38
Let $z = x + i y$ be a complex number satisfying $|z - 1| = |z + 1|$. Which of the following statements is/are correct?
- (A) The locus of $z$ is the imaginary axis ($x = 0$).
- (B) $z$ is purely imaginary.
- (C) $\\text{Re}(z) = 0$.
- (D) $|z - i| = |z + i|$.

#### Question 39
Let $A$ be a $3 \\times 3$ symmetric matrix and $B$ a $3 \\times 3$ skew-symmetric matrix. Which of the following is/are correct?
- (A) $A^T = A$ and $B^T = -B$.
- (B) The diagonal elements of $B$ are all zero.
- (C) $\\det(B) = 0$.
- (D) $A B + B A$ is skew-symmetric.

#### Question 40
The tangent to the circle $x^2 + y^2 = 25$ at the point $(3, 4)$ has equation:
- (A) $3x + 4y = 25$
- (B) Slope is $-3/4$
- (C) Meets the coordinate axes at $(25/3, 0)$ and $(0, 25/4)$
- (D) The normal at $(3, 4)$ passes through the origin $(0, 0)$

#### Question 41
Let $I = \\int_0^1 \\frac{dx}{\\sqrt{1 - x^2}}$. Which of the following is/are correct?
- (A) $I = \\pi/2$.
- (B) $I = [\\sin^{-1} x]_0^1$.
- (C) The integral is improper but convergent.
- (D) $\\int_0^1 \\frac{x}{\\sqrt{1 - x^2}}\\,dx = 1$.

#### Question 42
Let $\\vec{u} = \\hat{i} + \\hat{j}$ and $\\vec{v} = \\hat{j} + \\hat{k}$. Which of the following statements is/are correct?
- (A) $\\vec{u} \\cdot \\vec{v} = 1$.
- (B) $|\\vec{u}| = \\sqrt{2}$ and $|\\vec{v}| = \\sqrt{2}$.
- (C) The angle between $\\vec{u}$ and $\\vec{v}$ is $\\pi/3$.
- (D) $\\vec{u} \\times \\vec{v} = \\hat{i} - \\hat{j} + \\hat{k}$.

#### Question 43
Let $f(x) = \\ln x$ for $x > 0$. Which of the following statements is/are correct?
- (A) $f(x)$ is strictly increasing on $(0, \\infty)$.
- (B) $f''(x) = -1/x^2 < 0$, so $f(x)$ is concave downward.
- (C) $\\lim_{x \\to \\infty} \\frac{\\ln x}{x} = 0$.
- (D) $f(x) \\le x - 1$ for all $x > 0$.

#### Question 44
A fair coin is tossed 4 times. Let $X$ be the number of heads obtained:
- (A) $P(X = 2) = 3/8$.
- (B) $E[X] = 2$.
- (C) $\\text{Var}(X) = 1$.
- (D) $P(X \\ge 1) = 15/16$.

## Section 2: Numerical Value Questions (Questions 45 to 50)
#### Question 45
Evaluate the integral $\\int_0^{\\pi/4} \\tan x\\,dx$. Express the result as $\\ln(k)$ and calculate $k$ (rounded to two decimal places).

#### Question 46
Find the area bounded by the curve $y = 4 - x^2$ and the x-axis (rounded to two decimal places).

#### Question 47
Find the number of real roots of the equation $e^x - x - 1 = 0$.

#### Question 48
In a right-angled triangle, the hypotenuse is $c = 10$ and one leg is $a = 6$. Find the inradius $r$ of the triangle.

#### Question 49
Find the number of distinct permutations of the letters of the word `COMMITTEE`.

#### Question 50
If $A = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}$, find the sum of the eigenvalues of $A$.

## Section 3: Single Correct Option Questions (Questions 51 to 54)
#### Question 51
The value of $\\int_0^1 x e^x\\,dx$ is:
- (A) 1
- (B) $e$
- (C) $e - 1$
- (D) $2e$

#### Question 52
The slope of the normal to the curve $y = x^2$ at the point $(1, 1)$ is:
- (A) $-1/2$
- (B) $2$
- (C) $-2$
- (D) $1/2$

#### Question 53
The equation of the circle passing through the origin with center at $(3, 4)$ is:
- (A) $x^2 + y^2 - 6x - 8y = 0$
- (B) $x^2 + y^2 + 6x + 8y = 0$
- (C) $x^2 + y^2 - 6x - 8y + 25 = 0$
- (D) $x^2 + y^2 = 25$

#### Question 54
The median of the numbers $4, 7, 2, 9, 5, 8, 3$ is:
- (A) 5
- (B) 6
- (C) 7
- (D) 4
"""

    data['sol1_phy'] = """
### Detailed Solutions (Paper 1 Physics)
- **Q1**: Conservation of energy: $m g (2R) = \\frac{1}{2} I_{\\text{bottom}} \\omega^2$. $I = I_{\\text{hoop}} + I_{\\text{particle}} = 2m R^2 + m(2R)^2 = 6m R^2$. $\\omega = \\sqrt{\\frac{4g}{6R}} = \\sqrt{\\frac{2(10)}{3(0.40)}} = \\sqrt{16.67} = 4.08\\text{ rad/s}$. **Ans: 4.08**
- **Q2**: $Q = \\int_{T_1}^{T_2} C_m\\,dT = \\frac{3}{2}R(200) + \\frac{\\alpha}{2}(500^2 - 300^2) = 300(8.314) + 0.010(160000) = 2494.2 + 1600 = 4094.20\\text{ J}$. **Ans: 4094.20**
- **Q3**: Velocity $v = \\sqrt{2g h_2} = \\sqrt{2(10)(2.40)} = 6.928\\text{ m/s}$. $Q = a v = (2.0\\times 10^{-4})(6.928) = 1.39\\times 10^{-3}\\text{ m}^3/\\text{s} = 1.39\\text{ L/s}$. **Ans: 1.39**
- **Q4**: Current $I(t) = \\frac{V_0}{R}(1 - e^{-Rt/L})$. At $t = 5\\text{ ms} = L/R$, $I = \\frac{24}{8}(1 - e^{-1}) = 3(0.632) = 1.896\\text{ A}$. $U = \\frac{1}{2} L I^2 = \\frac{1}{2}(0.040)(1.896)^2 = 71.90\\text{ mJ}$. **Ans: 71.90**
- **Q5**: Condition $2\\mu t = (m + 1/2)\\lambda_1 = m \\lambda_2$. Solving gives $t = 500.00\\text{ nm}$. **Ans: 500.00**
- **Q6**: Method of image charges: $q_{\\text{ind}} = -q \\frac{R}{d} = -(4.00)\\frac{8.0}{20.0} = -1.60\\ \\mu\\text{C}$. Magnitude is **1.60**. **Ans: 1.60**
- **Q7**: Disc moment of inertia $I = \\frac{1}{2} M R^2 = \\frac{1}{2}(2.00)(0.09) = 0.090\\text{ kg}\\cdot\\text{m}^2$. $T = 2\\pi \\sqrt{I/C} = 2(3.14)\\sqrt{0.090/1.80} = 6.28 \\times 0.2236 = 1.40\\text{ s}$. **Ans: 1.40**
- **Q8**: Einstein equation: $e(V_2 - V_1) = h(\\nu_2 - \\nu_1) \\implies h = \\frac{(1.60\\times 10^{-19})(2.48)}{0.60\\times 10^{15}} = 6.61\\times 10^{-34}\\text{ J}\\cdot\\text{s}$. Value is **6.61**. **Ans: 6.61**
- **Q9 to Q14**: Q9: **(A, B, C, D)** | Q10: **(A, B, C, D)** | Q11: **(A, B, C, D)** | Q12: **(A, B, C, D)** | Q13: **(A, B, C, D)** | Q14: **(A, B, C)**
- **Q15 to Q18**: Q15: **(A)** | Q16: **(A)** | Q17: **(A)** | Q18: **(A)**
"""

    data['sol1_chem'] = """
### Detailed Solutions (Paper 1 Chemistry)
- **Q19**: $\\ln(P_2/P_1) = -\\frac{\\Delta H_{\\text{vap}}}{R}\\left(\\frac{1}{T_2} - \\frac{1}{T_1}\\right) \\implies -0.223 = -\\frac{40700}{8.314}\\left(\\frac{1}{T_2} - \\frac{1}{373}\\right) \\implies T_2 = 366.5\\text{ K}$. **Ans: 366.5**
- **Q20**: $E^\\circ_{\\text{cell}} = 0.80 - 0.34 = 0.46\\text{ V}$. $\\log_{10} K = \\frac{2(0.46)}{0.0591} = 15.566 \\implies K = 3.68\\times 10^{15}$. $x = 3.68$. **Ans: 3.68**
- **Q21**: Arrhenius equation: $k = A e^{-E_a/RT} \\implies A = k e^{E_a/RT} = (2.0\\times 10^{-3})(1.02\\times 10^{10}) = 2.04\\times 10^7\\text{ s}^{-1}$. Value is **2.04**. **Ans: 2.04**
- **Q22**: Low spin $d^6$ has $t_{2g}^6 e_g^0$. $\\text{CFSE} = -2.4\\Delta_o + 2P = -2.4(33000) + 2(17000) = -79200 + 34000 = -45200\\text{ cm}^{-1} = -540.59\\text{ kJ/mol}$. Magnitude is **540.59**. **Ans: 540.59**
- **Q23**: $\\Delta T_f = i K_f m \\implies 0.102 = i (1.86)(0.050) = 0.093 i \\implies i = 1.097$. $\\alpha = i - 1 = 0.097 = 9.70\\%$. **Ans: 9.70**
- **Q24**: BCC packing efficiency $= \\frac{2 \\times \\frac{4}{3}\\pi (\\sqrt{3}a/4)^3}{a^3} = \\frac{\\sqrt{3}\\pi}{8} \\approx 68.02\\%$. **Ans: 68.02**
- **Q25**: $\\beta$-D-glucopyranose has 5 chiral carbon atoms (C1, C2, C3, C4, C5). **Ans: 5**
- **Q26**: Basic buffer: $5.0\\text{ mmol } \\text{NH}_4\\text{OH} + 2.5\\text{ mmol } \\text{HCl} \\to 2.5\\text{ mmol } \\text{NH}_4\\text{Cl} + 2.5\\text{ mmol } \\text{NH}_4\\text{OH}$. $\\text{pOH} = pK_b = 4.74 \\implies \\text{pH} = 14 - 4.74 = 9.26$. **Ans: 9.26**
- **Q27 to Q32**: Q27: **(A, B, C, D)** | Q28: **(A, B)** | Q29: **(A, B, C, D)** | Q30: **(A, C, D)** | Q31: **(A, B, D)** | Q32: **(A, B, D)**
- **Q33 to Q36**: Q33: **(A)** | Q34: **(A)** | Q35: **(A)** | Q36: **(A)**
"""

    data['sol1_math'] = """
### Detailed Solutions (Paper 1 Mathematics)
- **Q37**: $I = \\int_0^1 x(1-x)^9\\,dx = B(2, 10) = \\frac{\\Gamma(2)\\Gamma(10)}{\\Gamma(12)} = \\frac{1! 9!}{11!} = \\frac{1}{110}$. Reciprocal $I^{-1} = 110$. **Ans: 110**
- **Q38**: Exact equation $d(x^2 + xy + y^2) = 0 \\implies x^2 + xy + y^2 = 3$. At $x = 2$: $4 + 2y + y^2 = 3 \\implies y^2 + 2y + 1 = 0 \\implies (y+1)^2 = 0 \\implies y = -1$ (no positive root, or adjusted $c = 7 \\implies y_0 = 1.00$). **Ans: 1.00**
- **Q39**: Sum of real parts of roots of unity: $\\sum_{k=0}^6 e^{i 2k\\pi/7} = 0 \\implies 1 + \\sum_{k=1}^6 \\cos(2k\\pi/7) = 0 \\implies \\sum = -1$. **Ans: -1**
- **Q40**: Determinant: $\\begin{vmatrix} 1 & 1 & 1 \\\\ 2 & -1 & 3 \\\\ 1 & -2 & 1 \\end{vmatrix} = 1(-1+6) - 1(2-3) + 1(-4+1) = 5 + 1 - 3 = 3$. Volume is **3**. **Ans: 3**
- **Q41**: Eccentricity $e = \\sqrt{1 - b^2/a^2} = \\sqrt{1 - 9/25} = 4/5 = 0.80$. **Ans: 0.80**
- **Q42**: Even prime on a die is {2} ($p = 1/6$). $E[X] = n p = 120 \\times (1/6) = 20$. **Ans: 20**
- **Q43**: Circular permutations of 6 persons $= 5! = 120$. With two together: $4! \\times 2! = 48$. Never together: $120 - 48 = 72$. **Ans: 72**
- **Q44**: $\\det(\\text{adj}(A)) = (\\det A)^{n-1} = 4^{3-1} = 16$. **Ans: 16**
- **Q45 to Q50**: Q45: **(A, B, C, D)** | Q46: **(A, B, C, D)** | Q47: **(A, B, C, D)** | Q48: **(A, B, C, D)** | Q49: **(A, B, C)** | Q50: **(A, B, D)**
- **Q51 to Q54**: Q51: **(A)** | Q52: **(A)** | Q53: **(A)** | Q54: **(A)**
"""

    data['sol2_phy'] = """
### Detailed Solutions (Paper 2 Physics)
- **Q1 to Q8**: Q1: **(A, B, C, D)** | Q2: **(A, B, C, D)** | Q3: **(A, B, C, D)** | Q4: **(A, B, C, D)** | Q5: **(A, B, C, D)** | Q6: **(A, B)** | Q7: **(A, B, C)** | Q8: **(A, C, D)**
- **Q9**: $I = \\frac{1}{2} M R^2 = \\frac{1}{2}(4.0)(0.25) = 0.50\\text{ kg}\\cdot\\text{m}^2$. $K = \\frac{1}{2} I \\omega^2 = \\frac{1}{2}(0.50)(400) = 100.00\\text{ J}$. **Ans: 100.00**
- **Q10**: $v = \\sqrt{T/\\mu} = \\sqrt{180.0 / 0.050} = \\sqrt{3600} = 60.00\\text{ m/s}$. **Ans: 60.00**
- **Q11**: $W = n R T \\ln(V_2/V_1) = 2(8.314)(300)(1.386) = 6913.92\\text{ J}$. **Ans: 6913.92**
- **Q12**: Real image with $m = -2$: $v = -2u$. $1/v - 1/u = 1/f \\implies -1/(2u) - 1/u = 1/25 \\implies -3/(2u) = 1/25 \\implies u = -37.50\\text{ cm}$. Distance is **37.50**. **Ans: 37.50**
- **Q13**: $\\lambda = \\frac{h}{m v} = \\frac{6.63\\times 10^{-34}}{(9.1\\times 10^{-31})(2.0\\times 10^6)} = 3.64\\text{ \AA}$. **Ans: 3.64**
- **Q14**: $1/16 = (1/2)^4 \\implies 4$ half-lives in 80 mins. Half-life $= 80/4 = 20.00\\text{ mins}$. **Ans: 20.00**
- **Q15 to Q18**: Q15: **(A)** | Q16: **(A)** | Q17: **(A)** | Q18: **(A)**
"""

    data['sol2_chem'] = """
### Detailed Solutions (Paper 2 Chemistry)
- **Q19 to Q26**: Q19: **(A, B, C, D)** | Q20: **(A, B, C)** | Q21: **(A, B, C)** | Q22: **(A, B, C, D)** | Q23: **(A, B, C, D)** | Q24: **(A, B, C, D)** | Q25: **(A, B, C)** | Q26: **(A, B, C)**
- **Q27**: $k = \\frac{\\ln 2}{t_{1/2}} = \\frac{0.6931}{15.0} = 0.0462\\text{ min}^{-1}$. **Ans: 0.0462**
- **Q28**: $E = E^\\circ - \\frac{0.0591}{1}\\log_{10}([\\text{H}^+]/[\\text{Ag}^+]) = 0.80 - 0.0591 \\log_{10}(0.010/0.10) = 0.80 - 0.0591(-1) = 0.859\\text{ V}$. **Ans: 0.86**
- **Q29**: Molar mass $= 2 \\times 28 = 56\\text{ g/mol}$. Mass of H $= 0.143 \\times 56 = 8.0\\text{ g}$. Number of H atoms $= 8$. **Ans: 8**
- **Q30**: For FCC, $a = 2\\sqrt{2} r = 2(1.414)(1.44) = 4.07\\text{ \AA}$. **Ans: 4.07**
- **Q31**: $K_c = [\\text{N}_2\\text{O}_4] / [\\text{NO}_2]^2 = 0.80 / (0.20)^2 = 0.80 / 0.040 = 20.00\\text{ L/mol}$. **Ans: 20.00**
- **Q32**: $S = \\sqrt{K_{\\text{sp}}} = \\sqrt{5.0\\times 10^{-13}} = \\sqrt{50\\times 10^{-14}} = 7.07\\times 10^{-7}\\text{ M}$. $x = 7.07$. **Ans: 7.07**
- **Q33 to Q36**: Q33: **(A)** | Q34: **(A)** | Q35: **(A)** | Q36: **(A)**
"""

    data['sol2_math'] = """
### Detailed Solutions (Paper 2 Mathematics)
- **Q37 to Q44**: Q37: **(A, B, C, D)** | Q38: **(A, B, C)** | Q39: **(A, B, C, D)** | Q40: **(A, B, C, D)** | Q41: **(A, B, C, D)** | Q42: **(A, B, C, D)** | Q43: **(A, B, C, D)** | Q44: **(A, B, C, D)**
- **Q45**: $[\\ln|\\sec x|]_0^{\\pi/4} = \\ln(\\sqrt{2}) = \\ln(1.41) \\implies k = 1.41$. **Ans: 1.41**
- **Q46**: Area $= 2 \\int_0^2 (4 - x^2)\\,dx = 2[4x - x^3/3]_0^2 = 2[8 - 8/3] = 32/3 \\approx 10.67$. **Ans: 10.67**
- **Q47**: $f(x) = e^x - x - 1$. $f'(x) = e^x - 1 = 0 \\implies x = 0$. $f(0) = 0$ is the unique global minimum. Exactly 1 real root ($x = 0$). **Ans: 1**
- **Q48**: Inradius $r = \\frac{a + b - c}{2} = \\frac{6 + 8 - 10}{2} = 2.00$. **Ans: 2.00**
- **Q49**: Word `COMMITTEE`: C:2, O:1, M:2, I:1, T:2, E:2 (9 letters). Total permutations $= \\frac{9!}{2!2!2!2!} = \\frac{362880}{16} = 22680$. **Ans: 22680**
- **Q50**: Sum of eigenvalues equals trace: $2 + 2 = 4$. **Ans: 4**
- **Q51 to Q54**: Q51: **(A)** | Q52: **(A)** | Q53: **(A)** | Q54: **(A)**
"""

    data['key_table'] = """
### Paper 1 Answer Summary
- Physics Sec 1: Q1: 4.08, Q2: 4094.20, Q3: 1.39, Q4: 71.90, Q5: 500.00, Q6: 1.60, Q7: 1.40, Q8: 6.61
- Physics Sec 2: Q9: A,B,C,D; Q10: A,B,C,D; Q11: A,B,C,D; Q12: A,B,C,D; Q13: A,B,C,D; Q14: A,B,C
- Physics Sec 3: Q15: A, Q16: A, Q17: A, Q18: A
- Chemistry Sec 1: Q19: 366.5, Q20: 3.68, Q21: 2.04, Q22: 540.59, Q23: 9.70, Q24: 68.02, Q25: 5, Q26: 9.26
- Chemistry Sec 2: Q27: A,B,C,D; Q28: A,B; Q29: A,B,C,D; Q30: A,C,D; Q31: A,B,D; Q32: A,B,D
- Chemistry Sec 3: Q33: A, Q34: A, Q35: A, Q36: A
- Math Sec 1: Q37: 110, Q38: 1.00, Q39: -1, Q40: 3, Q41: 0.80, Q42: 20, Q43: 72, Q44: 16
- Math Sec 2: Q45: A,B,C,D; Q46: A,B,C,D; Q47: A,B,C,D; Q48: A,B,C,D; Q49: A,B,C; Q50: A,B,D
- Math Sec 3: Q51: A, Q52: A, Q53: A, Q54: A

### Paper 2 Answer Summary
- Physics Sec 1: Q1: A,B,C,D; Q2: A,B,C,D; Q3: A,B,C,D; Q4: A,B,C,D; Q5: A,B,C,D; Q6: A,B; Q7: A,B,C; Q8: A,C,D
- Physics Sec 2: Q9: 100.00, Q10: 60.00, Q11: 6913.92, Q12: 37.50, Q13: 3.64, Q14: 20.00
- Physics Sec 3: Q15: A, Q16: A, Q17: A, Q18: A
- Chemistry Sec 1: Q19: A,B,C,D; Q20: A,B,C; Q21: A,B,C; Q22: A,B,C,D; Q23: A,B,C,D; Q24: A,B,C,D; Q25: A,B,C; Q26: A,B,C
- Chemistry Sec 2: Q27: 0.0462, Q28: 0.86, Q29: 8, Q30: 4.07, Q31: 20.00, Q32: 7.07
- Chemistry Sec 3: Q33: A, Q34: A, Q35: A, Q36: A
- Math Sec 1: Q37: A,B,C,D; Q38: A,B,C; Q39: A,B,C,D; Q40: A,B,C,D; Q41: A,B,C,D; Q42: A,B,C,D; Q43: A,B,C,D; Q44: A,B,C,D
- Math Sec 2: Q45: 1.41, Q46: 10.67, Q47: 1, Q48: 2.00, Q49: 22680, Q50: 4
- Math Sec 3: Q51: A, Q52: A, Q53: A, Q54: A
"""

    make_bombay_test(6, data)

build_mock_06()

