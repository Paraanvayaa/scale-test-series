# -*- coding: utf-8 -*-
"""
Generator for JEE Advanced Mock Test 02 - IIT Bombay-Inspired Examination
Variant: 2015 Structural Shock Simulation (High-penalty multi-correct & non-negative integer focus)
"""

import os

def create_mock_02():
    os.makedirs('mock_tests/Mock_02_IIT_Bombay', exist_ok=True)
    
    # -------------------------------------------------------------------------
    # PAPER 1
    # -------------------------------------------------------------------------
    p1 = """# JEE Advanced Mock Examination 02 — Paper 1
## Organising Style Inspiration: IIT Bombay (`IIT_BOMBAY_STYLE`)
**Historical Variant Benchmark**: 2015 Structural Shock Simulation (Intense multi-correct penalty & integer focus)  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (8 Questions per subject - Non-Negative Integer Answer)**:
  - Full Marks: **+3** if only the correct non-negative integer is entered.
  - Zero Marks: **0** in all other cases.
- **Section 2 (8 Questions per subject - One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+1** for each correct option chosen, provided NO incorrect option is chosen.
  - Negative Marks: **-2** in all other cases (wrong option selected).
- **Section 3 (2 Questions per subject - Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.

---

# PART I: PHYSICS (54 Marks)

## Section 1: Non-Negative Integer Questions (Questions 1 to 8)
*The answer to each question is a non-negative integer.*

#### Question 1 (Mechanics + Electrodynamics Synthesis)
Two parallel, long, horizontal conducting rails separated by distance $L = 1.0\\text{ m}$ and having negligible resistance are placed in a uniform vertical magnetic field $B = 2.0\\text{ T}$. A conducting rod of mass $m = 0.5\\text{ kg}$ and resistance $R = 4.0\\ \\Omega$ rests across the rails. An ideal capacitor of capacitance $C = 0.125\\text{ F}$ is connected between the ends of the rails. A constant horizontal external pulling force $F = 6.0\\text{ N}$ is applied to the rod at $t = 0$. If the acceleration of the rod reaches a constant value $a_0$ (in $\\text{m/s}^2$), find the integer value of $a_0$.

#### Question 2 (Rotational Dynamics & Torque)
A uniform disc of mass $M = 4\\text{ kg}$ and radius $R = 0.5\\text{ m}$ is pivoted at its center so it can rotate freely in a vertical plane. A particle of mass $m = 2\\text{ kg}$ is attached to the rim at the rightmost horizontal position (at angle $\\theta = 0$). When released from rest, the angular velocity $\\omega$ of the system as the particle passes through the lowest point is $\\sqrt{k}\\text{ rad/s}$. Find the integer value of $k$. [Take $g = 10\\text{ m/s}^2$].

#### Question 3 (Thermodynamic Cycles)
An ideal diatomic gas ($\\gamma = 1.4$) is taken through a cycle consisting of: an adiabatic expansion from volume $V_0$ to $2V_0$, an isobaric compression back to initial temperature, and an isochoric restoration to initial state. If the number of degrees of freedom of the gas molecules is $f$, find the value of $f$.

#### Question 4 (Electromagnetism — Mutual Inductance)
A long solenoid of cross-sectional area $A = 0.02\\text{ m}^2$ has $n_1 = 1000\\text{ turns/m}$. A short secondary coil of $N_2 = 100\\text{ turns}$ is tightly wound around the center of the solenoid. If a steady current of $I_1 = 5\\text{ A}$ through the solenoid is reversed in direction in $\\Delta t = 0.04\\text{ s}$, the magnitude of the average EMF induced in the secondary coil is $\\mathcal{E}$ Volts. If $\\mathcal{E} = k \\pi\\text{ V}$, find the integer $k$. [Take $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ T}\\cdot\\text{m/A}$].

#### Question 5 (Wave Optics — Thin Film Interference)
Light of wavelength $\\lambda = 600\\text{ nm}$ is incident normally on a thin soap film of refractive index $\\mu = 1.50$ surrounded by air. The minimum non-zero thickness $t$ (in nm) of the film for which constructive interference occurs in reflected light is an integer. Find the value of $t/10$.

#### Question 6 (Electrostatics — Concentric Shells)
Three concentric conducting spherical shells $A, B$, and $C$ of radii $a = 1\\text{ m}, b = 2\\text{ m}$, and $c = 3\\text{ m}$ carry charges $q_A = +Q, q_B = -2Q$, and $q_C = +3Q$ respectively. The potential of the innermost shell $A$ is $V_A = \\frac{1}{4\\pi \\varepsilon_0} \\frac{k Q}{6}$. Find the integer value of $k$.

#### Question 7 (Modern Physics — Bohr Model Orbitals)
In a hydrogen-like atom, an electron in the $n$-th excited state transitions to the first excited state, emitting a photon of energy $E_1$. If the atom has atomic number $Z = 3$ (lithium ion $\\text{Li}^{2+}$) and the emitted photon has energy equal to $108.8\\text{ eV}$, find the principal quantum number $n$ of the initial state. [Ground state ionization energy of $\\text{H} = 13.6\\text{ eV}$].

#### Question 8 (Oscillations & Waves — String Resonance)
A guitar string of length $L = 0.8\\text{ m}$ and linear mass density $\\mu = 5.0\\text{ g/m}$ is held under tension $T = 320\\text{ N}$. The fundamental frequency of transverse standing waves on this string is $f_1$ (in Hz). Find the integer value of $f_1 / 25$.

---

## Section 2: Multiple Correct Questions (Questions 9 to 16)
*One or more than one option is correct. Negative marking (-2) for incorrect choices.*

#### Question 9 (Mechanics — Conservation Laws in Collisions)
A smooth sphere $A$ of mass $m$ moving with velocity $v_0 \\hat{i}$ on a frictionless horizontal plane collides obliquely with an identical stationary sphere $B$. The coefficient of restitution between the spheres is $e = 0.50$. The line of centers at the impact instant makes an angle $\\theta = 45^\\circ$ with the initial direction of motion $\\hat{i}$. Which of the following statements is/are correct?
(A) The component of velocity of sphere $A$ perpendicular to the line of centers remains unchanged during the collision.  
(B) The velocity of sphere $B$ immediately after the collision is directed purely along the line of centers.  
(C) The speed of sphere $B$ immediately after the collision is $\\frac{3\\sqrt{2}}{8} v_0$.  
(D) The total kinetic energy of the system is conserved during the impact.

#### Question 10 (Electrodynamics — Moving Conductors & Inductance)
A metal rod of mass $m$, length $L$, and resistance $R$ is constrained to slide horizontally without friction on two parallel vertical rails connected at the bottom by an ideal inductor $L_0$. A uniform horizontal magnetic field $B$ is applied perpendicular to the plane of the rails. The rod is released from rest under gravity from $y = 0$. Which of the following statements is/are correct?
(A) The rod executes simple harmonic motion in the vertical direction.  
(B) The angular frequency of oscillation of the rod is $\\omega = \\sqrt{\\frac{B^2 L^2}{m L_0}}$.  
(C) The maximum downward displacement of the rod from its release point is $\\frac{2 m g L_0}{B^2 L^2}$.  
(D) The current in the inductor reaches its maximum magnitude when the rod is at its lowest position.

#### Question 11 (Thermodynamics — Heat Engines with Variable Heat Capacity)
A heat engine utilizes an ideal gas whose molar heat capacity at constant volume varies linearly with temperature according to $C_V(T) = C_0 + \\alpha T$. The gas undergoes an isochoric heating from $T_1$ to $T_2$, followed by an adiabatic expansion back to temperature $T_1$, and an isothermal compression back to initial state. Which of the following statements is/are correct?
(A) The internal energy change during isochoric heating is $\\Delta U = C_0 (T_2 - T_1) + \\frac{1}{2} \\alpha (T_2^2 - T_1^2)$.  
(B) The entropy change of the gas during isochoric heating is $\\Delta S = C_0 \\ln(T_2/T_1) + \\alpha(T_2 - T_1)$.  
(C) The efficiency of this engine is strictly less than the Carnot efficiency operating between $T_1$ and $T_2$.  
(D) During the adiabatic stage, $T V^{\\gamma - 1} = \\text{constant}$ remains strictly valid with a constant $\\gamma$.

#### Question 12 (Wave Optics — Diffraction Grating & Dispersion)
A plane transmission diffraction grating with $N$ lines per millimeter is illuminated normally with white light. Which of the following statements is/are correct?
(A) The principal maxima for wavelength $\\lambda$ occur at angles satisfying $d \\sin\\theta = m \\lambda$, where $d = 1/N$ and $m$ is an integer.  
(B) The angular dispersion $\\frac{d\\theta}{d\\lambda} = \\frac{m}{d \\cos\\theta}$.  
(C) In any given diffraction order $m \\ge 1$, red light is diffracted through a larger angle than violet light.  
(D) If grating spacing $d < \\lambda$ for all visible light, no diffraction maxima other than the central zero-order maximum can be observed.

#### Question 13 (Ray Optics — Aberrations & Total Internal Reflection)
A solid glass hemisphere of radius $R$ and refractive index $\\mu = 1.50$ is placed on a horizontal table with its flat planar surface in contact with the table. A narrow vertical parallel beam of monochromatic light of radius $r < R$ is incident symmetrically from above onto the curved surface. Which of the following statements is/are correct?
(A) Light rays passing very close to the optical axis focus at a distance of $2R$ below the curved vertex.  
(B) Rays incident at the peripheral edge experience total internal reflection if their angle of incidence exceeds $\\arcsin(1/\\mu)$.  
(C) The hemisphere exhibits positive spherical aberration for paraxial versus marginal rays.  
(D) If the flat bottom surface is coated with a reflecting silver layer, the system acts as a converging mirror.

#### Question 14 (Electrostatics — Conductors with Non-Uniform Charge Distribution)
An isolated neutral solid metallic sphere of radius $R$ is placed in a uniform external electric field $\\vec{E}_0 = E_0 \\hat{k}$. Which of the following statements is/are correct?
(A) The surface charge density induced on the sphere varies with polar angle $\\theta$ as $\\sigma(\\theta) = 3 \\varepsilon_0 E_0 \\cos\\theta$.  
(B) The electric potential of the metallic sphere is zero everywhere on and inside the sphere.  
(C) The electric field inside the conductor is zero because the field produced by induced surface charges exactly cancels $\\vec{E}_0$.  
(D) The total electrostatic energy stored in the electric field around the sphere increases upon introducing the conductor.

#### Question 15 (Modern Physics — X-Rays & Moseley's Law)
In an X-ray Coolidge tube operating at an accelerating potential $V_0$:
(A) The cut-off wavelength $\\lambda_{\\text{min}}$ of the continuous bremsstrahlung spectrum is inversely proportional to $V_0$.  
(B) The characteristic $K_\\alpha$ X-ray frequency satisfies Moseley's law: $\\sqrt{\\nu} = a(Z - b)$, where $b \\approx 1.0$.  
(C) If the target metal is replaced by another metal of higher atomic number $Z$, the cut-off wavelength $\\lambda_{\\text{min}}$ shifts to a lower value.  
(D) If the accelerating voltage $V_0$ is doubled, the frequency of the characteristic $K_\\alpha$ line remains unchanged, provided $V_0$ remains above the excitation potential.

#### Question 16 (Mechanics — Non-Inertial Frames & Centrifugal Force)
A straight smooth tube of length $L$ is pivoted at one end on a horizontal frictionless table and rotates in the horizontal plane with constant angular velocity $\\omega$. A small pellet of mass $m$ is placed inside the tube at distance $r_0$ from the pivot with zero radial velocity at $t = 0$. Which of the following statements is/are correct?
(A) The radial equation of motion of the pellet inside the tube is $\\frac{d^2 r}{dt^2} - \\omega^2 r = 0$.  
(B) The radial distance of the pellet as a function of time is $r(t) = r_0 \\cosh(\\omega t)$.  
(C) The Coriolis force exerted by the tube on the pellet is perpendicular to the tube and equals $2 m \\omega \\frac{dr}{dt}$.  
(D) The mechanical energy of the pellet in the inertial frame is conserved throughout the motion.

---

## Section 3: Single Correct Questions (Questions 17 to 18)
*Only one option is correct. Marking: +3 for correct, -1 for incorrect.*

#### Question 17 (Mechanics — Elastic Strings & Hooke's Law)
A light elastic spring of natural length $l_0$ and spring constant $k$ has one end fixed to a ceiling and the other attached to a mass $m$. The mass is held at the ceiling ($y = 0$) where the spring is completely unstretched and released from rest. The maximum extension $y_{\\text{max}}$ attained by the spring during its downward fall is:
(A) $\\frac{mg}{k}$  
(B) $\\frac{2mg}{k}$  
(C) $\\frac{4mg}{k}$  
(D) $\\frac{mg}{2k}$

#### Question 18 (Electrodynamics — Point Charge in Crossed Fields)
A particle of mass $m$ and positive charge $q$ is released from rest at the origin in the presence of crossed uniform fields $\\vec{E} = E_0 \\hat{j}$ and $\\vec{B} = B_0 \\hat{k}$. The maximum $y$-coordinate reached by the particle along its cycloidal path is:
(A) $\\frac{m E_0}{q B_0^2}$  
(B) $\\frac{2 m E_0}{q B_0^2}$  
(C) $\\frac{4 m E_0}{q B_0^2}$  
(D) $\\frac{m E_0}{2 q B_0^2}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: Non-Negative Integer Questions (Questions 19 to 26)

#### Question 19 (Thermodynamics — Hess's Law & Bond Energies)
Given the bond dissociation enthalpies: $\\text{C}-\\text{C} = 348\\text{ kJ/mol}$, $\\text{C}=\\text{C} = 614\\text{ kJ/mol}$, $\\text{C}-\\text{H} = 413\\text{ kJ/mol}$, and $\\text{H}-\\text{H} = 436\\text{ kJ/mol}$. Calculate the magnitude of the enthalpy of hydrogenation $\\Delta_r H^\\circ$ of ethene gas to ethane gas (in $\\text{kJ/mol}$). If the answer is an integer, enter it directly.

#### Question 20 (Electrochemistry — Nernst Potential Equilibrium)
For the Daniel cell $\\text{Zn}(s) \\mid \\text{Zn}^{2+}(\\text{aq}, 1.0\\text{ M}) \\parallel \\text{Cu}^{2+}(\\text{aq}, 1.0\\text{ M}) \\mid \\text{Cu}(s)$, the standard cell potential is $E^\\circ = 1.10\\text{ V}$. If the equilibrium constant for the cell reaction at $298\\text{ K}$ is written as $10^K$, find the integer value of $K$. [Take $\\frac{2.303 RT}{F} = 0.059\\text{ V}$, $1.10 / 0.0295 \\approx 37$].

#### Question 21 (Chemical Kinetics — Radioactive Decay Series)
A radioactive isotope nucleus $^{238}_{92}\\text{U}$ decays via a sequence of consecutive $\\alpha$ and $\\beta^-$ emissions into the stable lead isotope $^{206}_{82}\\text{Pb}$. Find the total number of $\\alpha$-particles emitted in this decay series.

#### Question 22 (Inorganic Chemistry — Coordination Isomerism Count)
Find the total number of geometrical and stereoisomers possible for the octahedral coordination complex $[\\text{Pt}(\\text{NH}_3)_2(\\text{py})_2\\text{Cl}_2]^{2+}$ (where $\\text{py} = \\text{pyridine}$).

#### Question 23 (Organic Chemistry — Aromaticity & Huckel's Rule)
Among the following planar cyclic species, find the number of species that are completely aromatic according to Hückel's $(4n + 2)\\pi$ rule:
1. Cyclopropenyl cation
2. Cyclobutadiene
3. Cyclopentadienyl anion
4. Benzene
5. Cycloheptatrienyl cation (tropylium)
6. Cyclooctatetraene (tub-shaped)
7. Pyridine
8. Pyrrole

#### Question 24 (Solid State — Octahedral Voids)
In a face-centered cubic (FCC) unit cell of close-packed hard spheres, find the total number of octahedral interstitial voids located entirely within or on the boundaries of a single unit cell.

#### Question 25 (Surface Chemistry — Coagulation & Hardy-Schulze Rule)
According to the Hardy-Schulze rule, the coagulation power of an electrolyte for a negatively charged arsenious sulfide sol ($\\text{As}_2\\text{S}_3$) increases rapidly with the valency of the active cation. If the coagulation values of $\\text{NaCl}, \\text{BaCl}_2$, and $\\text{AlCl}_3$ are in the ratio roughly $100 : 10 : 1$, find the positive charge valency $z$ of the cation in the most effective coagulating salt.

#### Question 26 (Physical Chemistry — Gaseous State Critical Constants)
For a real gas obeying the van der Waals equation, the critical compression factor is defined as $Z_c = \\frac{P_c V_c}{R T_c}$. If $Z_c$ is expressed as a fraction $3/k$, find the integer value of $k$.

---

## Section 2: Multiple Correct Questions (Questions 27 to 34)

#### Question 27 (Chemical Thermodynamics — Spontaneous Mixing & Entropy)
When two ideal non-reacting gases $A$ ($n_A$ moles) and $B$ ($n_B$ moles) at the same temperature and pressure are mixed spontaneously:
(A) The enthalpy of mixing is zero: $\\Delta_{\\text{mix}} H = 0$.  
(B) The volume of mixing is zero: $\\Delta_{\\text{mix}} V = 0$.  
(C) The entropy of mixing is positive: $\\Delta_{\\text{mix}} S = -R [n_A \\ln x_A + n_B \\ln x_B] > 0$.  
(D) The Gibbs free energy of mixing is negative: $\\Delta_{\\text{mix}} G < 0$.

#### Question 28 (Inorganic Chemistry — Qualitative Salt Analysis)
A white water-soluble solid gives a white precipitate with dilute $\\text{HCl}$ that dissolves in hot water and reappears as shining crystalline needles on cooling. The solid could contain:
(A) $\\text{Pb}^{2+}$ cations  
(B) $\\text{Ag}^{+}$ cations  
(C) $\\text{Hg}_2^{2+}$ cations  
(D) $\\text{Bi}^{3+}$ cations

#### Question 29 (Organic Chemistry — Nucleophilic Addition to Carbonyls)
Regarding the nucleophilic addition of hydrogen cyanide ($\\text{HCN}$) to benzaldehyde in the presence of base catalyst:
(A) The reaction is catalyzed by base because hydroxide converts weak acid $\\text{HCN}$ into the reactive nucleophile cyanide ion ($\\text{CN}^-$).  
(B) The rate-determining step is the attack of cyanide ion on the electrophilic carbonyl carbon.  
(C) The product mandelonitrile formed is a racemic mixture of enantiomers.  
(D) Electron-withdrawing groups on the aromatic ring increase the equilibrium constant for cyanohydrin formation.

#### Question 30 (Coordination Chemistry — Ligand Field & Spectrochemical Series)
Regarding the spectrochemical series and ligand behavior:
(A) Cyanide ($\\text{CN}^-$) and carbon monoxide ($\\text{CO}$) are strong field ligands because of synergic $\\pi$-backbonding.  
(B) Halide ions ($\\text{F}^-, \\text{Cl}^-, \\text{Br}^-$) are weak field ligands because of repulsive ligand-to-metal $\\pi$-donation into $t_{2g}$ orbitals.  
(C) High-spin octahedral complexes of $d^4, d^5, d^6, d^7$ transition metal ions always have smaller CFSE than their low-spin counterparts.  
(D) The magnitude of $\\Delta_o$ increases by roughly $40-50\\%$ in going from 3d to 4d and 4d to 5d transition metal series.

#### Question 31 (Electrochemistry — Fuel Cells & Efficiency)
For a hydrogen-oxygen fuel cell operating at $298\\text{ K}$ with reaction $2\\text{H}_2(g) + \\text{O}_2(g) \\to 2\\text{H}_2\\text{O}(l)$:
(A) The anode reaction is $\\text{H}_2(g) + 2\\text{OH}^-(\\text{aq}) \\to 2\\text{H}_2\\text{O}(l) + 2e^-$.  
(B) The theoretical thermodynamic efficiency is $\\eta = \\frac{\\Delta G^\\circ}{\\Delta H^\\circ}$.  
(C) Because $\\Delta S^\\circ < 0$ for water condensation, the theoretical efficiency $\\eta$ is slightly less than $100\\%$ ($~83\\%$).  
(D) Fuel cells produce continuous electrical energy without running down as long as fuel reactants are supplied.

#### Question 32 (Organic Reaction Mechanisms — Carbocation Rearrangements)
When 3,3-dimethylbutan-2-ol is heated with concentrated sulfuric acid:
(A) The reaction proceeds through a secondary carbocation intermediate formed by protonation and loss of water.  
(B) A 1,2-hydride shift occurs to form a more stable tertiary carbocation.  
(C) A 1,2-methyl shift occurs to form a more stable tertiary carbocation.  
(D) The major alkene product obtained is 2,3-dimethylbut-2-ene (tetramethylethene).

#### Question 33 (Solid State — Defect Structures)
Regarding stoichiometric and non-stoichiometric defects in crystalline solids:
(A) Frenkel defects do not alter the bulk density of the crystal lattice.  
(B) Schottky defects decrease the density of the crystal due to equal numbers of missing cations and anions.  
(C) $\\text{AgBr}$ exhibits both Frenkel and Schottky defects.  
(D) Non-stoichiometric metal-excess defects produced by heating $\\text{NaCl}$ in sodium vapor produce yellow coloration due to F-centers.

#### Question 34 (Chemical Kinetics — Collision Theory & Transition State)
According to the collision theory of bimolecular gas-phase reactions:
(A) The rate constant is given by $k = P Z e^{-E_a / RT}$, where $P$ is the steric or orientation factor.  
(B) The activation energy $E_a$ is the minimum kinetic energy colliding molecules must possess along the line of centers.  
(C) All collisions between molecules possessing energy greater than $E_a$ necessarily result in chemical reaction.  
(D) For reactions involving complex polyatomic molecules, the steric factor $P$ is often significantly less than unity.

---

## Section 3: Single Correct Questions (Questions 35 to 36)

#### Question 35 (Coordination Chemistry — Optical Resolution)
Which of the following octahedral complexes is optically active and can be resolved into enantiomers?
(A) trans-$[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$  
(B) cis-$[\\text{Co}(\\text{en})_2\\text{Cl}_2]^+$  
(C) $[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]^+$  
(D) trans-$[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$

#### Question 36 (Chemical Equilibrium — Le Chatelier's Principle)
For the exothermic Haber synthesis of ammonia:
$$\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g), \\quad \\Delta H < 0$$
Addition of an inert gas at constant volume to the equilibrium mixture:
(A) Shifts the equilibrium toward ammonia formation  
(B) Shifts the equilibrium toward nitrogen and hydrogen formation  
(C) Has no effect on the equilibrium state or concentrations  
(D) Increases the total equilibrium conversion of nitrogen

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: Non-Negative Integer Questions (Questions 37 to 44)

#### Question 37 (Calculus — Definite Integrals with Greatest Integer Functions)
Evaluate the definite integral:
$$I = \\int_{0}^{3} [x^2] \\, dx$$
where $[t]$ denotes the greatest integer less than or equal to $t$. If $I = 5 - \\sqrt{2} - \\sqrt{k}$, find the integer value of $k$.

#### Question 38 (Matrices & Determinants — System Consistency)
Consider the system of linear equations in variables $x, y, z$:
$$x + y + z = 6$$
$$x + 2y + 3z = 10$$
$$x + 2y + \\lambda z = \\mu$$
If the system has infinitely many solutions, find the integer value of $\\lambda + \\mu$.

#### Question 39 (Probability — Binomial Distribution Mode)
A fair six-faced die is rolled $n = 10$ times. Let $X$ be the number of times the number '4' appears. The most probable value (mode) of $X$ is an integer $m$. Find the value of $m$.

#### Question 40 (Coordinate Geometry — Circles Tangency)
Two circles $C_1: x^2 + y^2 = 9$ and $C_2: (x - 8)^2 + y^2 = r^2$ touch each other externally. Find the radius $r$ of circle $C_2$.

#### Question 41 (Differential Equations — Homogeneous Degree)
Find the degree of the homogeneous differential equation:
$$\\left(x^2 + y^2\\right) dx - 2xy \\, dy = 0$$
Enter the integer degree of the polynomials.

#### Question 42 (Complex Numbers — De Moivre Roots Sum)
Let $\\alpha_k = \\cos\\left(\\frac{2k\\pi}{7}\\right) + i \\sin\\left(\\frac{2k\\pi}{7}\\right)$ for $k = 1, 2, \\dots, 6$ be the non-real 7th roots of unity. Find the value of:
$$\\sum_{k=1}^{6} \\alpha_k$$
If the sum is $-k_0$, find the positive integer $k_0$.

#### Question 43 (Vectors — Orthogonal Projection)
Let $\\vec{u} = 3\\hat{i} + 4\\hat{j}$ and $\\vec{v} = \\hat{i} + \\hat{j}$. The magnitude of the vector component of $\\vec{u}$ perpendicular to $\\vec{v}$ is $\\frac{1}{\\sqrt{k}}$. Find the integer $k$.

#### Question 44 (Limits — Squeeze Theorem)
Evaluate the limit:
$$L = \\lim_{n \\to \\infty} \\left[ \\frac{1}{\\sqrt{n^2 + 1}} + \\frac{1}{\\sqrt{n^2 + 2}} + \\dots + \\frac{1}{\\sqrt{n^2 + n}} \\right]$$
The value of $L$ is an integer. Find $L$.

---

## Section 2: Multiple Correct Questions (Questions 45 to 52)

#### Question 45 (Calculus — Rolle's Theorem & Monotonicity)
Let $f(x) = x^3 - 3x^2 + 3x - 1$ for $x \\in \\mathbb{R}$. Which of the following statements is/are correct?
(A) $f(x)$ is strictly increasing on $\\mathbb{R}$.  
(B) $f'(1) = 0$ and $x = 1$ is a point of inflection.  
(C) $f(x)$ has no local maxima or local minima.  
(D) The tangent to the curve at $x = 1$ is horizontal.

#### Question 46 (Coordinate Geometry — Parabola Normal Chords)
Let $P(a t_1^2, 2a t_1)$ be a point on the parabola $y^2 = 4ax$. The normal at $P$ intersects the parabola again at point $Q(a t_2^2, 2a t_2)$. Which of the following statements is/are correct?
(A) The relation between the parameters is $t_2 = -t_1 - \\frac{2}{t_1}$.  
(B) If the normal chord subtends a right angle at the vertex, then $t_1^2 = 2$.  
(C) The minimum length of the normal chord occurs when $t_1 = \\sqrt{2}$.  
(D) The normal chord always passes through the focus of the parabola.

#### Question 47 (Algebra — Permutations & Derangements)
Let $D_n$ denote the number of derangements of $n$ distinct objects. Which of the following statements is/are correct?
(A) $D_1 = 0$ and $D_2 = 1$.  
(B) The recurrence relation $D_n = (n - 1)(D_{n-1} + D_{n-2})$ holds for all $n \\ge 3$.  
(C) $D_4 = 9$ and $D_5 = 44$.  
(D) $\\lim_{n \\to \\infty} \\frac{D_n}{n!} = \\frac{1}{e}$.

#### Question 48 (Vectors & 3D Geometry — Line in Planes)
Consider the line $L: \\frac{x - 2}{1} = \\frac{y - 3}{2} = \\frac{z - 4}{3}$ and the plane $\\Pi: 2x + y - z = 3$. Which of the following statements is/are correct?
(A) The line $L$ is parallel to the plane $\\Pi$.  
(B) The line $L$ lies entirely in the plane $\\Pi$.  
(C) The distance between the line $L$ and the plane $\\Pi$ is zero.  
(D) The point $(2, 3, 4)$ lies on the plane $\\Pi$.

#### Question 49 (Calculus — Definite Integrals Properties)
Let $f(x)$ be a continuous function on $[0, a]$. Which of the following statements is/are correct?
(A) $\\int_0^a f(x) \\, dx = \\int_0^a f(a - x) \\, dx$  
(B) $\\int_{-a}^a f(x) \\, dx = 2 \\int_0^a f(x) \\, dx$ if $f(x)$ is an even function.  
(C) $\\int_0^{2a} f(x) \\, dx = 2 \\int_0^a f(x) \\, dx$ if $f(2a - x) = f(x)$.  
(D) $\\int_0^{\\pi} x f(\\sin x) \\, dx = \\frac{\\pi}{2} \\int_0^\\pi f(\\sin x) \\, dx$.

#### Question 50 (Algebra — Complex Quadratic Equations)
Let $z^2 + \\alpha z + \\beta = 0$ be a quadratic equation with real coefficients. Which of the following statements is/are correct?
(A) If $\\alpha^2 - 4\\beta < 0$, the roots are complex conjugates: $z_1 = \\overline{z_2}$.  
(B) If $\\beta = 1$ and $|\\alpha| < 2$, both roots lie on the unit circle $|z| = 1$.  
(C) The sum of the roots is $-\\alpha$ and their product is $\\beta$.  
(D) If $\\alpha = 1$ and $\\beta = 1$, the roots are the non-real cube roots of $-1$.

#### Question 51 (Trigonometry — Inverse Trigonometric Sums)
Which of the following statements is/are correct?
(A) $\\arctan(1) + \\arctan(2) + \\arctan(3) = \\pi$  
(B) $\\arcsin x + \\arccos x = \\frac{\\pi}{2}$ for all $x \\in [-1, 1]$  
(C) $\\arctan x + \\arctan(1/x) = \\frac{\\pi}{2}$ for all $x > 0$  
(D) $\\arctan x + \\arctan(1/x) = -\\frac{\\pi}{2}$ for all $x < 0$

#### Question 52 (Probability — Independent Events)
Let $A$ and $B$ be two independent events with non-zero probabilities. Which of the following statements is/are correct?
(A) $P(A \\cap B) = P(A) P(B)$  
(B) $P(A \\mid B) = P(A)$  
(C) The complement events $A^c$ and $B^c$ are also independent.  
(D) $A$ and $B$ cannot be mutually exclusive.

---

## Section 3: Single Correct Questions (Questions 53 to 54)

#### Question 53 (Calculus — Tangent to Exponential Curves)
The slope of the tangent to the curve $y = x^x$ at the point where $x = 1$ is:
(A) $1$  
(B) $0$  
(C) $e$  
(D) $\\ln 2$

#### Question 54 (Coordinate Geometry — Locus of Midpoints)
The locus of the midpoint of a focal chord of the parabola $y^2 = 4ax$ is:
(A) $y^2 = 2a(x - a)$  
(B) $y^2 = a(x - a)$  
(C) $y^2 = 4a(x - a)$  
(D) $x^2 = 2a(y - a)$
"""

    with open('mock_tests/Mock_02_IIT_Bombay/Paper_1.md', 'w', encoding='utf-8') as f:
        f.write(p1)
    print("Generated mock_tests/Mock_02_IIT_Bombay/Paper_1.md")

if __name__ == '__main__':
    create_mock_02()

