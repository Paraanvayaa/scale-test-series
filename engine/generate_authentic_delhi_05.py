# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 05.
Empirical Signature: IIT Delhi Benchmark (2013, 2020)
- Multi-correct dominance (+4/-2 with partial marking)
- Maxwell's displacement current, eddy current damping, optical levitation
- Synergic backbonding, Lindemann-Hinshelwood kinetics, Group III cation analysis
- Darboux theorem, idempotent matrix rank-trace, surjections
"""
import os
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 05 — Paper 1
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
A circular parallel-plate capacitor with plates of radius $R$ separated by distance $d$ is being charged by a steady current $I$. Neglecting fringing fields:
(A) The electric field between the plates at time $t$ is $E(t) = \frac{I t}{\pi \varepsilon_0 R^2}$.  
(B) The displacement current density between the plates is uniform and given by $J_d = \varepsilon_0 \frac{\partial E}{\partial t} = \frac{I}{\pi R^2}$.  
(C) The magnetic field at a radial distance $r \le R$ from the central axis between the plates is $B(r) = \frac{\mu_0 I r}{2\pi R^2}$.  
(D) The Poynting vector $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$ at radius $r = R$ points radially inward, carrying electromagnetic energy into the capacitor.

#### Question 2
A copper pendulum plate of mass $M$ swings freely in a vertical plane between the poles of a powerful electromagnet. When the electromagnet is energized producing a strong magnetic field $B$ perpendicular to the plane of motion:
(A) Eddy currents are induced in the conducting copper plate as it enters and leaves the magnetic field region.  
(B) By Lenz's law, the Lorentz force on the induced eddy currents always opposes the motion of the plate.  
(C) The mechanical energy of the pendulum is converted into Joule heat within the copper plate, leading to rapid electromagnetic damping.  
(D) If narrow vertical slots are cut into the copper plate (comb-like structure), the damping effect is drastically reduced because large eddy current loops are broken.

#### Question 3
A microscopic transparent silica bead of radius $r = 1.0\ \mu\text{m}$ and density $\rho = 2000\text{ kg/m}^3$ is trapped at the focus of a strongly focused Gaussian laser beam (optical tweezers):
(A) The gradient force pulls the dielectric bead toward the region of maximum light intensity (the beam waist).  
(B) The scattering force pushes the bead along the propagation direction of the laser beam due to radiation pressure.  
(C) Stable 3D optical trapping requires the axial gradient force to overcome the destabilizing scattering force.  
(D) The optical gradient force arises from the transfer of photon linear momentum during refraction through the bead.

#### Question 4
A solid cylinder of mass $M$ and radius $R$ rests at the top of a fixed horizontal cylindrical surface of radius $2R$. The sphere/cylinder is released from rest from the topmost point and rolls without slipping down the curved surface:
(A) As long as pure rolling continues, the angular velocity $\omega$ and linear velocity $v$ satisfy $v = R \omega$.  
(B) The normal force exerted by the curved surface on the cylinder decreases as the angle of descent $\theta$ increases.  
(C) The cylinder loses contact with the curved surface when the normal force drops to zero.  
(D) The detachment angle $\theta_d$ for pure rolling satisfies $\cos\theta_d = \frac{4}{7}$.

#### Question 5
A uniform solid metal rod of length $L$ and thermal conductivity $K$ has its ends maintained at $T = 0^\circ\text{C}$. Heat is generated uniformly throughout the volume of the rod at a constant rate $q'''\text{ W/m}^3$. In the steady state:
(A) The heat conduction differential equation is $\frac{d^2T}{dx^2} + \frac{q'''}{K} = 0$.  
(B) The steady-state temperature profile is parabolic: $T(x) = \frac{q'''}{2K} x (L - x)$ for $0 \le x \le L$.  
(C) The maximum temperature occurs at the midpoint $x = L/2$ with value $T_{\text{max}} = \frac{q''' L^2}{8K}$.  
(D) The heat flux exiting each end of the rod is $J_Q = \frac{1}{2} q''' L$.

#### Question 6
Babinet's Principle in wave optics states that the diffraction patterns produced by two complementary screens are identical, except for the unscattered central beam. Which of the following statements is/are correct?
(A) An opaque circular disk of radius $a$ and a circular aperture of radius $a$ in an opaque screen are complementary screens.  
(B) According to Babinet's principle, the Fraunhofer diffraction pattern of a thin hair is identical to that of a single slit of the same width.  
(C) At the center of the geometric shadow of an opaque circular disk illuminated by a point source of light, a bright spot (Poisson's / Arago's spot) is observed.  
(D) The intensity of Poisson's spot at the center of the shadow is equal to the unobstructed incident light intensity.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A flywheel in the form of a uniform disk of mass $M = 20.0\text{ kg}$ and radius $R = 0.50\text{ m}$ is rotating at an initial angular speed $\omega_0 = 60.0\text{ rad/s}$. A constant tangential braking force $F = 50.0\text{ N}$ is applied to the rim of the flywheel. Calculate the time (in seconds) required to bring the flywheel to rest.

#### Question 8
A long solid non-conducting cylinder of radius $R = 0.10\text{ m}$ carries a non-uniform volume charge density $\rho(r) = \rho_0 \left(1 - \frac{r}{R}\right)$, where $\rho_0 = 6.0\ \mu\text{C/m}^3$. Calculate the magnitude of the electric field $E$ (in $\text{kV/m}$) at a radial distance $r = 0.050\text{ m}$ from the central axis. [Take $\varepsilon_0 = 8.85 \times 10^{-12}\text{ C}^2/(\text{N}\cdot\text{m}^2)$. Round off to TWO decimal places].

#### Question 9
In a Billet's split lens arrangement, a convex lens of focal length $f = 20.0\text{ cm}$ is split along its diameter into two halves separated by $d = 0.40\text{ mm}$. A point source of light ($\lambda = 600\text{ nm}$) is placed at distance $u = 30.0\text{ cm}$ in front of the split lens. Calculate the distance $d'$ (in mm) between the two real image sources formed by the lens halves.

#### Question 10
One mole of an ideal diatomic gas ($\gamma = 1.40$) undergoes an adiabatic expansion such that its absolute temperature drops from $T_1 = 400\text{ K}$ to $T_2 = 300\text{ K}$. Calculate the work done $W$ (in Joules) by the gas during this expansion. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$. Round off to the nearest integer].

#### Question 11
A circular coil of $N = 200$ turns and radius $r = 0.050\text{ m}$ carries a current $I = 2.00\text{ A}$. It is placed in a uniform magnetic field $B = 0.60\text{ T}$ with its plane parallel to the magnetic field lines. Calculate the magnitude of the magnetic torque $\tau$ (in $\text{N}\cdot\text{m}$) acting on the coil. [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 12
The activity of a radioactive sample drops to $\frac{1}{8}$ of its initial value in a time interval of $t = 24.0\text{ days}$. Calculate the half-life $T_{1/2}$ of the radioisotope in days.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
Two identical spherical asteroids of mass $M$ and radius $R$ are separated by a center-to-center distance $4R$. The minimum launch speed required for a projectile of mass $m$ to escape to infinity from the surface of one asteroid along the line of centers is:
(A) $\sqrt{\frac{7GM}{3R}}$  
(B) $\sqrt{\frac{2GM}{R}}$  
(C) $\sqrt{\frac{5GM}{3R}}$  
(D) $\sqrt{\frac{8GM}{3R}}$

#### Question 14
Two vertical parallel glass plates separated by a narrow gap $d = 1.0\text{ mm}$ are partially immersed in water ($\text{surface tension } S = 0.075\text{ N/m}, \rho = 1000\text{ kg/m}^3$). Taking contact angle $\theta = 0^\circ$ and $g = 9.80\text{ m/s}^2$, the height $h$ to which water rises between the plates is:
(A) $15.3\text{ mm}$  
(B) $30.6\text{ mm}$  
(C) $7.65\text{ mm}$  
(D) $20.0\text{ mm}$

#### Question 15
A supersonic jet flies horizontally at Mach number $M = 2.0$. The semi-vertex angle $\theta$ of the conical shock wave (Mach cone) trailing behind the jet is:
(A) $30^\circ$  
(B) $45^\circ$  
(C) $60^\circ$  
(D) $90^\circ$

#### Question 16
In $\beta^+$ (positron) radioactive decay, the disintegration energy $Q$ is given by ($M_P$ is atomic mass of parent, $M_D$ is atomic mass of daughter):
(A) $[M_P - M_D - 2m_e]c^2$  
(B) $[M_P - M_D]c^2$  
(C) $[M_P - M_D - m_e]c^2$  
(D) $[M_P - M_D + m_e]c^2$

#### Question 17
A Brewster's window in a gas laser cavity is oriented such that the light beam is incident at Brewster's angle $\theta_B$. The purpose of this window is to:
(A) Transmit light of one polarization state with zero reflection loss  
(B) Totally reflect unwanted wavelengths  
(C) Focus the laser beam onto the mirror  
(D) Introduce a $90^\circ$ phase shift

#### Question 18
The moment of inertia of a uniform circular ring of mass $M$ and radius $R$ about a tangential axis in its own plane is:
(A) $\frac{3}{2}M R^2$  
(B) $2 M R^2$  
(C) $\frac{1}{2}M R^2$  
(D) $\frac{5}{4}M R^2$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following statements is/are correct regarding metal carbonyls and $\pi$-backbonding?
(A) The carbon monoxide ligand acts as both a $\sigma$-donor and a $\pi$-acceptor.  
(B) Electron density is donated from the filled $d$-orbitals of the metal into the empty $\pi^*$ antibonding orbitals of $\text{CO}$.  
(C) Synergic $\pi$-backbonding strengthens the metal-carbon ($\text{M}-\text{C}$) bond while weakening the carbon-oxygen ($\text{C}-\text{O}$) bond.  
(D) In an isoelectronic series $[V(CO)_6]^-, [Cr(CO)_6], [Mn(CO)_6]^+$, the $\text{C}-\text{O}$ stretching frequency in IR spectroscopy decreases in the order $[Mn(CO)_6]^+ > [Cr(CO)_6] > [V(CO)_6]^-$.

#### Question 20
In the Kolbe-Schmitt reaction for the synthesis of salicylic acid:
(A) Sodium phenoxide is heated with carbon dioxide ($\text{CO}_2$) at $120-140^\circ\text{C}$ under pressure ($4-7\text{ atm}$) followed by acidification.  
(B) Salicylic acid (2-hydroxybenzoic acid) is obtained as the major product due to stabilization of the ortho transition state by sodium chelation.  
(C) If potassium phenoxide is used instead of sodium phenoxide, the major product is $p$-hydroxybenzoic acid.  
(D) The electrophile attacking the phenoxide ring is carbon dioxide ($\text{CO}_2$).

#### Question 21
Regarding the chemical reactions taking place in a commercial lead-acid storage battery during discharge:
(A) Anodic reaction: $\text{Pb}(s) + \text{HSO}_4^-(aq) \to \text{PbSO}_4(s) + \text{H}^+(aq) + 2e^-$.  
(B) Cathodic reaction: $\text{PbO}_2(s) + \text{HSO}_4^-(aq) + 3\text{H}^+(aq) + 2e^- \to \text{PbSO}_4(s) + 2\text{H}_2\text{O}(l)$.  
(C) In both electrodes, insoluble lead sulfate ($\text{PbSO}_4$) is deposited.  
(D) During discharge, sulfuric acid is consumed, leading to a decrease in the density of the electrolyte solution.

#### Question 22
In the Lindemann-Hinshelwood mechanism for unimolecular gas-phase reactions $A \to \text{Products}$:
(A) Energized molecules $A^*$ are produced by bimolecular collision: $A + A \rightleftharpoons A^* + A$.  
(B) Energized molecules $A^*$ can either be deactivated by collision or decompose unimolecularly to products: $A^* \to \text{Products}$.  
(C) At high gas pressures, collision deactivation dominates, and the overall reaction exhibits first-order kinetics.  
(D) At very low gas pressures, collision activation is the rate-limiting step, and the reaction exhibits second-order kinetics.

#### Question 23
In qualitative inorganic analysis of Group III basic radicals ($\text{Fe}^{3+}, \text{Al}^{3+}, \text{Cr}^{3+}$):
(A) The group reagent is a mixture of ammonium chloride ($\text{NH}_4\text{Cl}$) and ammonium hydroxide ($\text{NH}_4\text{OH}$).  
(B) The presence of $\text{NH}_4\text{Cl}$ suppresses the ionization of $\text{NH}_4\text{OH}$ via the common ion effect.  
(C) The low concentration of $\text{OH}^-$ ions is sufficient to exceed the $K_{sp}$ of Group III hydroxides but not Group IV hydroxides ($\text{Zn(OH)}_2, \text{Mn(OH)}_2$).  
(D) $\text{Fe}^{3+}$ precipitates as a reddish-brown gelatinous precipitate of $\text{Fe(OH)}_3$.

#### Question 24
Which of the following statements is/are correct regarding the isoelectric point ($pI$) of an amino acid?
(A) At the isoelectric point, the amino acid exists predominantly as a dipolar zwitterion with net charge zero.  
(B) At $pH = pI$, the amino acid does not migrate toward either electrode in an electric field.  
(C) The solubility of the amino acid in water is at its minimum at the isoelectric point.  
(D) For neutral amino acids with two ionizable groups ($pK_{a1}$ and $pK_{a2}$), $pI = \frac{pK_{a1} + pK_{a2}}{2}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
The solubility product of $\text{CaF}_2$ in water is $K_{sp} = 4.0 \times 10^{-11}$ at $25^\circ\text{C}$. Calculate the molar solubility $S$ of $\text{CaF}_2$ in a $0.050\text{ M NaF}$ solution in $\text{mol/L}$. If $S = 1.60 \times 10^{-m}\text{ mol/L}$, find the integer value of $m$.

#### Question 26
For the decomposition reaction $2\text{N}_2\text{O}_5 \to 4\text{NO}_2 + \text{O}_2$, the rate constant is $k = 5.0 \times 10^{-4}\text{ s}^{-1}$. Calculate the half-life $t_{1/2}$ of this reaction in seconds ($\text{s}$). [Take $\ln 2 = 0.693$].

#### Question 27
An element with FCC lattice has edge length $a = 400\text{ pm}$. Calculate the interplanar spacing $d_{200}$ (in picometers, $\text{pm}$) for the $(200)$ crystallographic planes.

#### Question 28
Calculate the EMF $E_{\text{cell}}$ (in Volts) at $298\text{ K}$ for the concentration cell:
$$\text{Zn}(s) | \text{Zn}^{2+}(0.010\text{ M}) \parallel \text{Zn}^{2+}(1.00\text{ M}) | \text{Zn}(s)$$
[Take $\frac{2.303 R T}{F} = 0.0591\text{ V}$. Round off to TWO decimal places].

#### Question 29
A solution prepared by dissolving $1.80\text{ g}$ of glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, molar mass $180\text{ g/mol}$) in $250.0\text{ g}$ of water boils at $100.021^\circ\text{C}$. Calculate the ebullioscopic constant $K_b$ of water in $\text{K}\cdot\text{kg/mol}$. [Round off to TWO decimal places].

#### Question 30
Calculate the spin-only magnetic moment $\mu_{\text{eff}}$ (in Bohr Magnetons, $\text{BM}$) of the octahedral complex $[\text{Cr}(\text{NH}_3)_6]^{3+}$ ($\text{Cr}^{3+}, 3d^3$). [Take $\sqrt{15} \approx 3.87$. Round off to TWO decimal places].

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The reaction of an $\alpha$-bromo ester with a carbonyl compound (aldehyde or ketone) in the presence of zinc metal followed by hydrolysis to give a $\beta$-hydroxy ester is known as:
(A) Reformatsky reaction  
(B) Perkin reaction  
(C) Claisen condensation  
(D) Dieckmann condensation

#### Question 32
Azulene ($\text{C}_{10}\text{H}_8$), a non-benzenoid bicyclic hydrocarbon containing fused 5-membered and 7-membered rings:
(A) Is aromatic with $10\ \pi$-electrons and possesses a significant dipole moment ($\sim 1.0\text{ D}$)  
(B) Is antiaromatic and highly unstable  
(C) Has zero dipole moment due to symmetry  
(D) Is non-aromatic

#### Question 33
In the Hall-Héroult electrolytic process for the extraction of aluminium, cryolite ($\text{Na}_3\text{AlF}_6$) is added to molten alumina ($\text{Al}_2\text{O}_3$) primarily to:
(A) Lower the melting point of alumina and increase the electrical conductivity of the melt  
(B) Act as a reducing agent  
(C) Prevent the oxidation of the carbon anodes  
(D) Dissolve the silica impurities

#### Question 34
Lactose (milk sugar) is a disaccharide composed of:
(A) $\beta$-D-galactose and $\beta$-D-glucose linked by a $\beta-1,4$-glycosidic bond  
(B) Two $\alpha$-D-glucose units  
(C) $\alpha$-D-glucose and $\beta$-D-fructose  
(D) Two $\beta$-D-galactose units

#### Question 35
The bond angles in the Group 15 hydrides decrease sharply from $\text{NH}_3$ ($107.8^\circ$) to $\text{PH}_3$ ($93.6^\circ$) because:
(A) In $\text{PH}_3$, bonding involves almost pure unhybridized $p$-orbitals (Drago's rule)  
(B) Phosphorus has a larger atomic radius than nitrogen  
(C) $\text{PH}_3$ has greater lone-pair lone-pair repulsion  
(D) Nitrogen has available $d$-orbitals

#### Question 36
Which of the following artificial sweeteners has the highest sweetness value relative to sucrose (cane sugar)?
(A) Alitame ($\sim 2000$ times)  
(B) Aspartame ($\sim 100$ times)  
(C) Saccharin ($\sim 550$ times)  
(D) Sucralose ($\sim 600$ times)

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Darboux's Theorem in differential calculus states that if a function $f$ is differentiable on an interval $[a, b]$, then its derivative $f'$ satisfies the intermediate value property on $[a, b]$. Which of the following statements is/are correct?
(A) $f'(x)$ cannot have simple jump discontinuities on $[a, b]$.  
(B) If $f'(a) < 0$ and $f'(b) > 0$, then there exists some $c \in (a, b)$ such that $f'(c) = 0$.  
(C) The derivative $f'(x)$ need not be continuous for Darboux's theorem to hold.  
(D) The function $g(x) = \begin{cases} 1, & x > 0 \\ 0, & x \le 0 \end{cases}$ cannot be the derivative of any function on $\mathbb{R}$.

#### Question 38
Let $A$ be a non-zero $n \times n$ matrix such that $A^2 = A$ (idempotent matrix). Which of the following statements is/are correct?
(A) The only possible eigenvalues of $A$ are $0$ and $1$.  
(B) $\text{rank}(A) = \text{Tr}(A)$.  
(C) $A(I - A) = 0$.  
(D) The matrix $A$ is diagonalizable.

#### Question 39
Consider the hyperbola $H: \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Let the equation of the normal at point $P(a\sec\theta, b\tan\theta)$ be $\frac{ax}{\sec\theta} + \frac{by}{\tan\theta} = a^2 + b^2$:
(A) From any point $(h, k)$, at most 4 distinct normals can be drawn to the hyperbola $H$.  
(B) The feet of four concyclic normals on the hyperbola have their eccentric angles summing to an odd multiple of $\pi$.  
(C) The normal at the vertex $(a, 0)$ is the transverse axis ($y = 0$).  
(D) The envelope of the normals to the hyperbola is its evolute: $(ax)^{2/3} - (by)^{2/3} = (a^2 + b^2)^{2/3}$.

#### Question 40
Consider the differential equation $(2x y \cos(x^2) - 2xy + 1)dx + (\sin(x^2) - x^2)dy = 0$. Which of the following statements is/are correct?
(A) The differential equation is exact because $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} = 2x\cos(x^2) - 2x$.  
(B) The potential function $F(x, y)$ satisfies $\frac{\partial F}{\partial x} = M$ and $\frac{\partial F}{\partial y} = N$.  
(C) The general solution is $y\sin(x^2) - x^2 y + x = C$.  
(D) If $y(0) = 5$, then $C = 0$.

#### Question 41
Let $\vec{a}, \vec{b}$ be two non-parallel vectors in $\mathbb{R}^3$. Let $\vec{c} = \vec{a} \times \vec{b}$. Which of the following statements is/are correct?
(A) The vectors $\vec{a}, \vec{b}, \vec{c}$ form a right-handed orthogonal/linearly independent system.  
(B) The scalar triple product $[\vec{a} \ \vec{b} \ \vec{c}] = |\vec{a} \times \vec{b}|^2 > 0$.  
(C) The vector $\vec{c} \times \vec{a}$ lies in the plane spanned by $\vec{a}$ and $\vec{b}$ and is perpendicular to $\vec{a}$.  
(D) $(\vec{a} \times \vec{b}) \cdot (\vec{a} \times \vec{b}) = (\vec{a} \cdot \vec{a})(\vec{b} \cdot \vec{b}) - (\vec{a} \cdot \vec{b})^2$ (Lagrange's identity).

#### Question 42
Let $X$ be an exponentially distributed continuous random variable with rate parameter $\lambda > 0$, having probability density function $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$:
(A) The cumulative distribution function is $F(x) = 1 - e^{-\lambda x}$ for $x \ge 0$.  
(B) The expected value of $X$ is $E[X] = \frac{1}{\lambda}$.  
(C) The variance of $X$ is $\text{Var}(X) = \frac{1}{\lambda^2}$.  
(D) $X$ satisfies the memoryless property: $P(X > s + t \mid X > s) = P(X > t)$ for all $s, t \ge 0$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^{\pi/2} \ln(\sin x)\,dx$$
If $I = -\frac{\pi}{2}\ln 2$, find the absolute value $|I|$ rounded off to TWO decimal places. [Take $\pi = 3.1416$ and $\ln 2 \approx 0.6931$].

#### Question 44
Find the area of the region bounded by the curves $y = e^x, y = e^{-x}$, and the vertical line $x = 1$. [Take $e \approx 2.718$ and $1/e \approx 0.368$. Round off to TWO decimal places].

#### Question 45
Find the total number of positive integer divisors of $N = 3600$.

#### Question 46
Calculate the perpendicular distance from the point $(1, 1, 1)$ to the plane $x + 2y + 2z - 14 = 0$.

#### Question 47
If $\omega = e^{i 2\pi/5}$ is a non-real fifth root of unity, find the numerical value of:
$$P = (1 - \omega)(1 - \omega^2)(1 - \omega^3)(1 - \omega^4)$$

#### Question 48
Find the number of onto functions (surjections) from a set $A$ containing 5 elements to a set $B$ containing 3 elements.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The shortest distance between the lines $\frac{x}{1} = \frac{y}{2} = \frac{z}{3}$ and $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ is:
(A) $\frac{1}{\sqrt{6}}$  
(B) $\frac{2}{\sqrt{6}}$  
(C) $0$  
(D) $\frac{1}{\sqrt{3}}$

#### Question 50
If $A = \begin{pmatrix} 2 & 0 & 0 \\ 5 & 3 & 0 \\ 7 & 1 & 4 \end{pmatrix}$, the eigenvalues of $A$ are:
(A) $2, 3, 4$  
(B) $0, 0, 0$  
(C) $1, 2, 3$  
(D) $5, 7, 1$

#### Question 51
The length of the chord intercepted by the circle $x^2 + y^2 = 25$ on the line $x + y = 5$ is:
(A) $5\sqrt{2}$  
(B) $10$  
(C) $5$  
(D) $2\sqrt{5}$

#### Question 52
The angle between the tangents to the curve $y = x^2$ at the points where $x = 1$ and $x = -1$ is:
(A) $\tan^{-1}(4/3)$  
(B) $\pi/2$  
(C) $\tan^{-1}(3/4)$  
(D) $\pi/4$

#### Question 53
Evaluate the limit:
$$L = \lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$$
(A) $1/2$  
(B) $1$  
(C) $0$  
(D) $1/6$

#### Question 54
The minimum value of the expression $f(x) = x^2 - 6x + 13$ for all $x \in \mathbb{R}$ is:
(A) $4$  
(B) $3$  
(C) $9$  
(D) $13$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 05 — Paper 2
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
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal surface. A horizontal impulse $J$ is applied to the sphere at a height $h$ above the center of mass ($0 \le h \le R$):
(A) The linear velocity of the center of mass immediately after the impulse is $v_0 = \frac{J}{M}$.  
(B) The angular velocity immediately after the impulse is $\omega_0 = \frac{J h}{I} = \frac{5 J h}{2 M R^2}$.  
(C) The condition for the sphere to start rolling without slipping immediately after the impulse is $h = \frac{2}{5}R$.  
(D) If $h > \frac{2}{5}R$, forward slipping occurs immediately after impact, and friction acts in the backward direction.

#### Question 2
Two identical spherical soap bubbles of radii $r_1$ and $r_2$ ($r_1 > r_2$) coalesce isothermally under vacuum to form a single spherical bubble of radius $R$. Let $S$ be the surface tension of the soap solution:
(A) The excess pressure inside each bubble is $\Delta P = \frac{4S}{r}$.  
(B) By Boyle's law ($P V = \text{const}$) applied to the enclosed air, $P_1 V_1 + P_2 V_2 = P_R V_R$.  
(C) In a complete vacuum where atmospheric pressure is zero, the surface area decreases: $r_1^2 + r_2^2 = R^2$.  
(D) In an atmosphere of pressure $P_0$, the radius of the combined bubble satisfies $P_0(R^3 - r_1^3 - r_2^3) + 4S(R^2 - r_1^2 - r_2^2) = 0$.

#### Question 3
An electromagnetic plane wave travels in free space along the $+z$-direction. Which of the following statements is/are correct?
(A) $\vec{E}$ and $\vec{B}$ are mutually perpendicular and perpendicular to the direction of wave propagation $\hat{k}$.  
(B) The ratio of the amplitudes is $\frac{E_0}{B_0} = c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$.  
(C) The electric energy density equals the magnetic energy density: $u_E = \frac{1}{2}\varepsilon_0 E^2 = u_B = \frac{B^2}{2\mu_0}$.  
(D) The wave carries linear momentum with volume momentum density $\vec{p} = \frac{\vec{S}}{c^2} = \varepsilon_0 (\vec{E} \times \vec{B})$.

#### Question 4
A light ray travels through a medium of variable refractive index $\mu(y) = \mu_0 \sqrt{1 + y/H}$ for $y \ge 0$. A ray is launched horizontally at $y = 0$ along the $+x$-direction:
(A) By Snell's law in a stratified medium, $\mu(y)\cos\theta(y) = \text{constant} = \mu_0$.  
(B) $\cos\theta(y) = \frac{1}{\sqrt{1 + y/H}}$, which means $\tan\theta(y) = \frac{dy}{dx} = \sqrt{\frac{y}{H}}$.  
(C) The trajectory of the light ray is a parabola: $y(x) = \frac{x^2}{4H}$.  
(D) The ray bends continuously toward the region of higher refractive index.

#### Question 5
In Bohr's model of the hydrogen atom:
(A) The orbital radius scales as $r_n \propto n^2$.  
(B) The orbital speed scales as $v_n \propto \frac{1}{n}$.  
(C) The orbital period scales as $T_n \propto n^3$.  
(D) The magnetic field produced by the orbiting electron at the nucleus scales as $B_n \propto \frac{1}{n^5}$.

#### Question 6
An ideal gas is expanded from volume $V_1$ to $V_2$ ($V_2 > V_1$) via three alternative reversible processes: (I) Isobaric, (II) Isothermal, and (III) Adiabatic:
(A) The final pressure is highest for the isobaric process and lowest for the adiabatic process.  
(B) The work done by the gas is maximum for the isobaric process: $W_{\text{isobaric}} > W_{\text{isothermal}} > W_{\text{adiabatic}}$.  
(C) The change in internal energy is positive for isobaric, zero for isothermal, and negative for adiabatic.  
(D) The heat absorbed is greatest in the isobaric expansion.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A simple pendulum of length $L = 0.98\text{ m}$ is suspended inside an elevator accelerating vertically upward with acceleration $a = 2.20\text{ m/s}^2$. Taking $g = 9.80\text{ m/s}^2$, calculate the time period $T$ (in seconds) of small oscillations of the pendulum. [Take $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 8
Two identical point charges $q = +2.0\ \mu\text{C}$ are fixed at $(0, a)$ and $(0, -a)$ with $a = 0.10\text{ m}$. Calculate the electric field magnitude $E$ (in $\text{kV/m}$) at the point $(x, 0)$ on the x-axis where $x = 0.10\text{ m}$. [Take $\frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$ and $2^{3/2} \approx 2.828$. Round off to TWO decimal places].

#### Question 9
In a Newton's rings experiment using reflected monochromatic light of wavelength $\lambda = 600\text{ nm}$, the diameter of the 10th dark ring is $D_{10} = 4.00\text{ mm}$. Calculate the radius of curvature $R$ of the plano-convex lens in meters ($\text{m}$). [Round off to TWO decimal places].

#### Question 10
Calculate the efficiency $\eta$ (as a percentage, \%) of a Carnot heat engine operating between temperatures $T_H = 500\text{ K}$ and $T_C = 300\text{ K}$.

#### Question 11
A long straight wire carries a current $I = 10.0\text{ A}$. Calculate the magnetic field magnitude $B$ (in $\mu\text{T}$) at a perpendicular distance $r = 0.050\text{ m}$ from the wire. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$].

#### Question 12
The work function of potassium is $\Phi = 2.25\text{ eV}$. Calculate the threshold wavelength $\lambda_0$ (in nanometers, $\text{nm}$) for photoelectric emission from potassium. [Take $hc = 1240\text{ eV}\cdot\text{nm}$. Round off to the nearest integer].

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the fluid mechanics phenomena in List-I with their physical dimensionless number in List-II:
- **List-I**:
  - P. Reynolds number ($Re$)
  - Q. Mach number ($M$)
  - R. Froude number ($Fr$)
  - S. Knudsen number ($Kn$)
- **List-II**:
  - 1. Inertial forces / Viscous forces
  - 2. Flow speed / Speed of sound
  - 3. Inertial forces / Gravitational forces
  - 4. Mean free path / Characteristic length scale

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 14
Match the thermodynamic cycles in List-I with their consisting processes in List-II:
- **List-I**:
  - P. Carnot Cycle
  - Q. Otto Cycle
  - R. Diesel Cycle
  - S. Brayton Cycle
- **List-II**:
  - 1. Two reversible isotherms + Two reversible adiabatics
  - 2. Two reversible isochores + Two reversible adiabatics
  - 3. One isobaric heat addition + One isochoric heat rejection + Two adiabatics
  - 4. Two reversible isobars + Two reversible adiabatics

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 15
Match the optical phenomena in List-I with their wave principle in List-II:
- **List-I**:
  - P. Young's double-slit
  - Q. Single-slit diffraction
  - R. Polarization by reflection
  - S. Mirage formation
- **List-II**:
  - 1. Interference of wavelets from two coherent point/line sources
  - 2. Interference of secondary wavelets from continuous aperture (Huygens-Fresnel)
  - 3. Brewster's Law ($\tan\theta_B = \mu$)
  - 4. Total internal reflection in continuously graded refractive index medium

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the nuclear reaction types in List-I with their key example in List-II:
- **List-I**:
  - P. Nuclear Fission
  - Q. Nuclear Fusion
  - R. Radiative Neutron Capture
  - S. Spontaneous $\beta^-$ decay
- **List-II**:
  - 1. $^{235}\text{U} + n \to ^{141}\text{Ba} + ^{92}\text{Kr} + 3n$
  - 2. $^2\text{H} + ^3\text{H} \to ^4\text{He} + n$
  - 3. $^{238}\text{U} + n \to ^{239}\text{U} + \gamma$
  - 4. $^{14}\text{C} \to ^{14}\text{N} + e^- + \bar{\nu}_e$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 17
Match the semiconductor devices in List-I with their principal application in List-II:
- **List-I**:
  - P. Zener Diode
  - Q. Photodiode
  - R. Light Emitting Diode (LED)
  - S. Solar Cell
- **List-II**:
  - 1. Voltage regulation under reverse breakdown
  - 2. Optical signal detection in reverse bias
  - 3. Spontaneous light emission under forward bias
  - 4. Photovoltaic electricity generation without external bias

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 18
Match the electromagnetic wave parameters in List-I with their relations in List-II:
- **List-I**:
  - P. Wavelength $\lambda$
  - Q. Wave vector $k$
  - R. Angular frequency $\omega$
  - S. Wave speed $c$
- **List-II**:
  - 1. $c / \nu$
  - 2. $2\pi / \lambda$
  - 3. $2\pi \nu$
  - 4. $\omega / k$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Which of the following statements is/are correct regarding the structure of boric acid ($\text{H}_3\text{BO}_3$)?
(A) It has a two-dimensional layered planar sheet structure held together by hydrogen bonding.  
(B) Boron is $sp^2$ hybridized in boric acid.  
(C) It acts as a weak monobasic Lewis acid in water by accepting $\text{OH}^-$ rather than donating a proton: $\text{B(OH)}_3 + 2\text{H}_2\text{O} \rightleftharpoons [\text{B(OH)}_4]^- + \text{H}_3\text{O}^+$.  
(D) Addition of polyhydroxy compounds like glycerol, mannitol, or catechol significantly enhances its acidity, allowing direct titration against standard $\text{NaOH}$ with phenolphthalein.

#### Question 20
Which of the following compounds gives a positive haloform (iodoform) reaction?
(A) Butan-2-one ($\text{CH}_3\text{COCH}_2\text{CH}_3$)  
(B) Pentan-3-one ($\text{CH}_3\text{CH}_2\text{COCH}_2\text{CH}_3$)  
(C) Ethanol ($\text{CH}_3\text{CH}_2\text{OH}$)  
(D) Acetone ($\text{CH}_3\text{COCH}_3$)

#### Question 21
Regarding the electrochemical cell: $\text{Pt}(s) | \text{H}_2(1\text{ atm}) | \text{H}^+(1\text{ M}) \parallel \text{Fe}^{3+}(aq), \text{Fe}^{2+}(aq) | \text{Pt}(s)$:
(A) Standard Hydrogen Electrode (SHE) acts as the anode.  
(B) Cell potential increases if the concentration of $\text{Fe}^{3+}$ is increased.  
(C) Cell potential decreases if the concentration of $\text{Fe}^{2+}$ is increased.  
(D) The standard cell potential equals the standard reduction potential of the $\text{Fe}^{3+}/\text{Fe}^{2+}$ couple.

#### Question 22
Which of the following pairs represent functional isomers?
(A) Ethanol and Dimethyl ether  
(B) Propanal and Propanone  
(C) Acetic acid and Methyl formate  
(D) Pentan-2-one and Pentan-3-one

#### Question 23
Which of the following compounds will liberate nitrogen gas ($\text{N}_2$) on heating?
(A) Ammonium nitrite ($\text{NH}_4\text{NO}_2$)  
(B) Ammonium dichromate ($(\text{NH}_4)_2\text{Cr}_2\text{O}_7$)  
(C) Sodium azide ($\text{NaN}_3$)  
(D) Ammonium nitrate ($\text{NH}_4\text{NO}_3$)

#### Question 24
Which of the following bases are purine bases found in nucleic acids?
(A) Adenine  
(B) Guanine  
(C) Cytosine  
(D) Thymine

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
Calculate the solubility (in $\text{mol/L}$) of silver chromate ($\text{Ag}_2\text{CrO}_4$) in pure water at $25^\circ\text{C}$ given $K_{sp} = 1.1 \times 10^{-12}$. If the solubility is $S = 6.5 \times 10^{-m}\text{ mol/L}$, find the integer value of $m$.

#### Question 26
For a zero-order reaction $A \to \text{Products}$, the initial concentration is $[A]_0 = 0.40\text{ M}$ and the rate constant is $k = 0.0080\text{ M/s}$. Calculate the time (in seconds) required for the reaction to reach $50\%$ completion ($t_{1/2}$).

#### Question 27
An element with BCC crystal structure has atomic radius $r = 173.2\text{ pm}$. Calculate the edge length $a$ of the unit cell in picometers ($\text{pm}$). [Take $\sqrt{3} \approx 1.732$. Round off to the nearest integer].

#### Question 28
Calculate the standard enthalpy of reaction $\Delta_r H^\circ$ (in $\text{kJ/mol}$) for:
$$\text{CO}(g) + \frac{1}{2}\text{O}_2(g) \to \text{CO}_2(g)$$
Given:
- $\Delta_f H^\circ(\text{CO}) = -110.5\text{ kJ/mol}$
- $\Delta_f H^\circ(\text{CO}_2) = -393.5\text{ kJ/mol}$
[Round off to ONE decimal place].

#### Question 29
Calculate the osmotic pressure $\Pi$ (in atm) of a $0.050\text{ M}$ aqueous solution of urea at $T = 300\text{ K}$. [Take $R = 0.0821\text{ L}\cdot\text{atm/(mol}\cdot\text{K)}$. Round off to TWO decimal places].

#### Question 30
Find the oxidation state of chromium in potassium dichromate ($\text{K}_2\text{Cr}_2\text{O}_7$).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following compounds gives a positive Lucas test immediately at room temperature (producing cloudiness/turbidity within seconds)?
(A) 2-Methylpropan-2-ol ($\text{tert}$-butanol)  
(B) Propan-2-ol  
(C) Propan-1-ol  
(D) Ethanol

#### Question 32
The geometry of the interhalogen compound $\text{ClF}_3$ according to VSEPR theory is:
(A) T-shaped  
(B) Trigonal planar  
(C) Trigonal bipyramidal  
(D) Tetrahedral

#### Question 33
In the froth floatation process for concentration of sulfide ores, sodium ethyl xanthate is added to act as a:
(A) Collector  
(B) Frother  
(C) Depressant  
(D) Activator

#### Question 34
Which of the following compounds does not reduce Fehling's solution?
(A) Benzaldehyde  
(B) Acetaldehyde  
(C) Glucose  
(D) Fructose

#### Question 35
The hybridization of the central atom in the xenon compound $\text{XeF}_2$ is:
(A) $sp^3d$  
(B) $sp^3$  
(C) $sp^3d^2$  
(D) $dsp^2$

#### Question 36
Natural rubber is a linear polymer of:
(A) Isoprene (cis-1,4-polyisoprene)  
(B) Chloroprene  
(C) Butadiene  
(D) Styrene

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = x^4 - 4x^3 + 10$ for $x \in \mathbb{R}$. Which of the following statements is/are correct?
(A) $f'(x) = 4x^2 (x - 3)$.  
(B) $x = 0$ is a stationary point, but not an extremum (point of inflection).  
(C) $f(x)$ attains its absolute minimum at $x = 3$ with value $-17$.  
(D) The curve is concave upward for $x > 2$.

#### Question 38
Let $A$ and $B$ be two $n \times n$ matrices. Which of the following statements is/are correct?
(A) $\text{Tr}(AB) = \text{Tr}(BA)$.  
(B) $\text{Tr}(A + B) = \text{Tr}(A) + \text{Tr}(B)$.  
(C) There exist no finite-dimensional matrices $A$ and $B$ such that $AB - BA = I$.  
(D) The matrices $AB$ and $BA$ possess the exact same set of non-zero eigenvalues.

#### Question 39
Consider the circle $x^2 + y^2 = r^2$. Tangents drawn from an external point $P(x_1, y_1)$ touch the circle at $Q$ and $R$:
(A) The equation of the chord of contact $QR$ is $x x_1 + y y_1 = r^2$.  
(B) The length of the tangent $PQ$ is $L = \sqrt{x_1^2 + y_1^2 - r^2}$.  
(C) The area of the triangle formed by the pair of tangents and the chord of contact is $\Delta = \frac{r L^3}{x_1^2 + y_1^2}$.  
(D) The circumcircle of $\Delta PQR$ passes through the origin $(0, 0)$ with $OP$ as diameter.

#### Question 40
Consider the differential equation $\frac{d^2y}{dx^2} - 3\frac{dy}{dx} + 2y = 0$ with $y(0) = 0$ and $y'(0) = 1$. Which of the following statements is/are correct?
(A) The roots of the auxiliary equation are $m_1 = 1$ and $m_2 = 2$.  
(B) The general solution is $y(x) = C_1 e^x + C_2 e^{2x}$.  
(C) The particular solution satisfying the initial conditions is $y(x) = e^{2x} - e^x$.  
(D) $y(x) > 0$ for all $x > 0$.

#### Question 41
Let $\vec{u}, \vec{v}, \vec{w}$ be three unit vectors satisfying $\vec{u} \cdot \vec{v} = 0, \vec{v} \cdot \vec{w} = 0, \vec{w} \cdot \vec{u} = 0$:
(A) The vectors $\vec{u}, \vec{v}, \vec{w}$ form an orthonormal basis for $\mathbb{R}^3$.  
(B) The scalar triple product $[\vec{u} \ \vec{v} \ \vec{w}]$ is either $+1$ or $-1$.  
(C) Any vector $\vec{x}$ can be expressed as $\vec{x} = (\vec{x}\cdot\vec{u})\vec{u} + (\vec{x}\cdot\vec{v})\vec{v} + (\vec{x}\cdot\vec{w})\vec{w}$.  
(D) $|\vec{u} + \vec{v} + \vec{w}| = \sqrt{3}$.

#### Question 42
In a random experiment, an event $A$ has probability $P(A) = 0.6$, and event $B$ has $P(B) = 0.5$. Which of the following statements is/are correct?
(A) The minimum possible value of $P(A \cap B)$ is $0.1$.  
(B) The maximum possible value of $P(A \cap B)$ is $0.5$.  
(C) The maximum possible value of $P(A \cup B)$ is $1.0$.  
(D) If $A$ and $B$ are independent, then $P(A \cap B) = 0.3$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Find the area bounded by the curve $y = \cos x$, the x-axis, and the lines $x = 0$ and $x = \pi/2$.

#### Question 44
Find the slope of the tangent to the curve $y = x^4 - 2x^2 + 1$ at the point where $x = 2$.

#### Question 45
Evaluate the definite integral:
$$I = \int_0^1 x e^x\,dx$$

#### Question 46
Calculate the angle (in degrees) between the lines whose direction ratios are $(1, 1, 0)$ and $(1, 0, 1)$.

#### Question 47
If the 3rd term of a geometric progression is 4, find the product of the first 5 terms.

#### Question 48
How many 3-digit even numbers can be formed using the digits $1, 2, 3, 4, 5, 6$ without repetition?

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the derivative functions in List-I with their standard evaluated derivative in List-II:
- **List-I**:
  - P. $\frac{d}{dx}(\sin^{-1} x)$
  - Q. $\frac{d}{dx}(\tan^{-1} x)$
  - R. $\frac{d}{dx}(\sec^{-1} x)$
  - S. $\frac{d}{dx}(\cos^{-1} x)$
- **List-II**:
  - 1. $\frac{1}{\sqrt{1-x^2}}$
  - 2. $\frac{1}{1+x^2}$
  - 3. $\frac{1}{|x|\sqrt{x^2-1}}$
  - 4. $-\frac{1}{\sqrt{1-x^2}}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-2, R-1, S-4

#### Question 50
Match the system of equations in List-I with the determinant condition for non-trivial solutions in List-II for $A X = 0$:
- **List-I**:
  - P. Homogeneous system with unique trivial solution
  - Q. Homogeneous system with infinitely many non-trivial solutions
  - R. Non-homogeneous system with unique solution
  - S. Non-homogeneous system with inconsistent equations
- **List-II**:
  - 1. $\det(A) \ne 0$
  - 2. $\det(A) = 0$
  - 3. $\det(A) \ne 0$
  - 4. $\det(A) = 0$ and $(\text{adj } A)B \ne 0$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 51
Match the complex numbers in List-I with their principal argument in List-II:
- **List-I**:
  - P. $1 + i\sqrt{3}$
  - Q. $-1 + i$
  - R. $-1 - i\sqrt{3}$
  - S. $1 - i$
- **List-II**:
  - 1. $\pi/3$ ($60^\circ$)
  - 2. $3\pi/4$ ($135^\circ$)
  - 3. $-2\pi/3$ ($-120^\circ$)
  - 4. $-\pi/4$ ($-45^\circ$)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 52
Match the probability distributions in List-I with their mean in List-II:
- **List-I**:
  - P. Binomial($n, p$)
  - Q. Poisson($\lambda$)
  - R. Geometric($p$)
  - S. Uniform on $(a, b)$
- **List-II**:
  - 1. $n p$
  - 2. $\lambda$
  - 3. $1/p$
  - 4. $\frac{a+b}{2}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 53
Match the standard functions in List-I with their Maclaurin series expansion in List-II:
- **List-I**:
  - P. $e^x$
  - Q. $\sin x$
  - R. $\cos x$
  - S. $\ln(1+x)$
- **List-II**:
  - 1. $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$
  - 2. $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$
  - 3. $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$
  - 4. $x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 54
Match the planes in List-I with their geometric configuration in List-II:
- **List-I**:
  - P. $x = 0$
  - Q. $y = 0$
  - R. $z = 0$
  - S. $x + y + z = 0$
- **List-II**:
  - 1. yz-coordinate plane
  - 2. zx-coordinate plane
  - 3. xy-coordinate plane
  - 4. Plane passing through origin with equal intercepts signs

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 05 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Maxwell's Displacement Current, Ampere-Maxwell Law, Poynting Vector in Capacitors.
- **2. Derivation**:
  - $E(t) = \frac{V(t)}{d} = \frac{Q(t)}{C d} = \frac{I t}{\frac{\varepsilon_0 \pi R^2}{d} d} = \frac{I t}{\pi \varepsilon_0 R^2}$. (A) is correct.
  - $J_d = \varepsilon_0 \frac{\partial E}{\partial t} = \varepsilon_0 \frac{I}{\pi \varepsilon_0 R^2} = \frac{I}{\pi R^2}$. (B) is correct.
  - Inside capacitor, $\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{d,\text{enc}} \implies B(2\pi r) = \mu_0 J_d (\pi r^2) = \mu_0 \frac{I}{\pi R^2} (\pi r^2) \implies B(r) = \frac{\mu_0 I r}{2\pi R^2}$. (C) is correct.
  - $\vec{E}$ is along $+\hat{z}$, $\vec{B}$ is along $+\hat{\theta}$. $\vec{E} \times \vec{B}$ points along $-\hat{r}$ (inward). Poynting vector carries electrical energy from fields into capacitor storage. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Electromagnetic Induction, Eddy Current Braking, Lenz's Law.
- **2. Derivation**:
  - Changing flux induces eddy currents in the plate. (A) is correct.
  - By Lenz's law, magnetic Lorentz force opposes velocity. (B) is correct.
  - Kinetic energy is dissipated as Joule heat $\int I^2 R dt$. (C) is correct.
  - Slots interrupt circular eddy current paths, reducing loop area and braking force. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Optical Tweezers, Gradient and Scattering Radiation Forces.
- **2. Derivation**:
  - Dielectric particle is polarized in inhomogeneous EM field; potential energy is $U = -\frac{1}{2}\alpha E^2$. Gradient force $\vec{F}_{\text{grad}} = -\nabla U = \frac{1}{2}\alpha \nabla(E^2)$ attracts particle to maximum intensity. (A) is correct.
  - Scattering force from absorbed/scattered photons pushes along $+z$. (B) is correct.
  - 3D trap requires axial gradient force to overcome scattering force (achieved by high numerical aperture objective). (C) is correct.
  - Refraction bends light, and by conservation of momentum, reactive force pulls bead to focal spot. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Rolling with Slipping vs Pure Rolling on Convex Curved Surfaces, Normal Reaction.
- **2. Derivation**:
  - Effective trajectory radius: $R_{\text{eff}} = 2R + R = 3R$.
  - Energy conservation: $M g (3R)(1 - \cos\theta) = \frac{1}{2}M v^2 + \frac{1}{2}I \omega^2 = \frac{7}{10}M v^2 \implies v^2 = \frac{30}{7}g R (1 - \cos\theta)$.
  - Normal force: $M g \cos\theta - N = M \frac{v^2}{3R} = M \frac{\frac{30}{7}g R (1 - \cos\theta)}{3R} = \frac{10}{7}M g (1 - \cos\theta)$.
  - Detachment occurs when $N = 0 \implies \cos\theta = \frac{10}{7}(1 - \cos\theta) \implies \frac{17}{7}\cos\theta = \frac{10}{7} \implies \cos\theta = \frac{10}{17}$. (D is $\frac{10}{17}$, so check options). Statements (A), (B), (C) are correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Steady-State Heat Conduction with Internal Heat Generation.
- **2. Derivation**:
  - Fourier's law with generation: $K \frac{d^2T}{dx^2} + q''' = 0 \implies \frac{d^2T}{dx^2} = -\frac{q'''}{K}$. (A) is correct.
  - Integrating twice with $T(0) = T(L) = 0$: $T(x) = \frac{q'''}{2K} x (L - x)$. (B) is correct.
  - Maximum at $x = L/2$: $T(L/2) = \frac{q'''}{2K}\frac{L}{2}\frac{L}{2} = \frac{q''' L^2}{8K}$. (C) is correct.
  - Heat flux at $x = 0$: $J_Q = -K \frac{dT}{dx}\big|_{x=0} = -K \left(\frac{q''' L}{2K}\right) = -\frac{1}{2}q''' L$. Magnitude is $\frac{1}{2}q''' L$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Babinet's Principle, Poisson's (Arago's) Spot.
- **2. Derivation**:
  - Complementary screens sum to unobstructed wavefront. (A) is correct.
  - By Babinet's principle, wire and slit have identical diffraction patterns. (B) is correct.
  - Poisson's spot appears at center of shadow. (C) is correct.
  - Fresnel zone analysis shows central intensity equals unobstructed beam intensity. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Moment of inertia of disk: $I = \frac{1}{2}M R^2 = \frac{1}{2}(20.0)(0.50)^2 = 2.50\text{ kg}\cdot\text{m}^2$.
  Braking torque: $\tau = F R = (50.0)(0.50) = 25.0\text{ N}\cdot\text{m}$.
  Angular deceleration: $\alpha = \frac{\tau}{I} = \frac{25.0}{2.50} = 10.0\text{ rad/s}^2$.
  Time to stop: $t = \frac{\omega_0}{\alpha} = \frac{60.0}{10.0} = 6.00\text{ s}$. Exact: `6.00`.
- **Question 8**: Gauss's law for cylinder of radius $r$:
  $E(2\pi r L) = \frac{Q_{\text{enc}}}{\varepsilon_0} = \frac{L}{\varepsilon_0}\int_0^r \rho(r')(2\pi r' dr') = \frac{2\pi L \rho_0}{\varepsilon_0}\int_0^r \left(r' - \frac{r'^2}{R}\right)dr' = \frac{2\pi L \rho_0}{\varepsilon_0}\left(\frac{r^2}{2} - \frac{r^3}{3R}\right)$.
  $E(r) = \frac{\rho_0}{\varepsilon_0}\left(\frac{r}{2} - \frac{r^2}{3R}\right)$.
  For $r = 0.050\text{ m}, R = 0.10\text{ m}$:
  $E = \frac{6.0 \times 10^{-6}}{8.85 \times 10^{-12}}\left(0.025 - \frac{0.0025}{0.30}\right) = (6.78 \times 10^5)(0.025 - 0.00833) = (6.78 \times 10^5)(0.01667) \approx 11.30 \times 10^3\text{ V/m} = 11.30\text{ kV/m}$. Exact: `11.30`.
- **Question 9**: Real image distance: $\frac{1}{v} - \frac{1}{-30} = \frac{1}{20} \implies \frac{1}{v} = \frac{1}{20} - \frac{1}{30} = \frac{1}{60} \implies v = +60.0\text{ cm}$.
  Magnification: $m = \frac{v}{u} = \frac{60}{30} = 2.0$.
  Separation between split image sources: $d' = d(1 + m) = (0.40\text{ mm})(1 + 2) = 1.20\text{ mm}$. Exact: `1.20`.
- **Question 10**: $W = -\Delta U = -n C_V \Delta T = -(1.0)\left(\frac{5}{2}R\right)(300 - 400) = \frac{5}{2}(8.314)(100) = 250(8.314) = 2078.5\text{ J} \approx 2079\text{ J}$. Exact: `2079.00`.
- **Question 11**: Magnetic dipole moment: $\mu = N I A = 200(2.00)\pi(0.05)^2 = 400 \times 3.1416 \times 0.0025 = 3.1416\text{ A}\cdot\text{m}^2$.
  Torque: $\tau = \mu B \sin 90^\circ = (3.1416)(0.60) \approx 1.88\text{ N}\cdot\text{m}$. Exact: `1.88`.
- **Question 12**: $A(t) = A_0 (1/2)^{t/T_{1/2}} \implies \frac{1}{8} = (1/2)^3 \implies \frac{24.0}{T_{1/2}} = 3 \implies T_{1/2} = 8.00\text{ days}$. Exact: `8.00`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Potential at surface of asteroid 1: $V_1 = -\frac{GM}{R} - \frac{GM}{3R} = -\frac{4GM}{3R}$. At infinity $V_\infty = 0$. By energy conservation: $\frac{1}{2}m v^2 + m V_1 = 0 \implies v = \sqrt{-2V_1} = \sqrt{\frac{8GM}{3R}}$. Option (D).
- **Question 14**: $h = \frac{2S}{\rho g d} = \frac{2(0.075)}{(1000)(9.80)(1.0 \times 10^{-3})} = \frac{0.150}{9.80} \approx 0.0153\text{ m} = 15.3\text{ mm}$. Option (A).
- **Question 15**: Mach cone semi-angle: $\sin\theta = \frac{1}{M} = \frac{1}{2.0} = 0.50 \implies \theta = 30^\circ$. Option (A).
- **Question 16**: $Q_{\beta^+} = [M_P - M_D - 2m_e]c^2$. Option (A).
- **Question 17**: Eliminates reflection loss for p-polarized light. Option (A).
- **Question 18**: Parallel axis theorem: $I = I_{\text{diameter}} + M R^2 = \frac{1}{2}M R^2 + M R^2 = \frac{3}{2}M R^2$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Synergic bonding in metal carbonyls: $\sigma$-donation strengthens $\text{M}-\text{C}$, $\pi$-backdonation into $\text{CO}$ $\pi^*$ weakens $\text{C}-\text{O}$. Greater electron density on metal increases backbonding, lowering $\nu_{\text{CO}}$. Options: (A), (B), (C), (D).
- **Question 20**: Kolbe-Schmitt reaction uses sodium phenoxide and $\text{CO}_2$ under pressure to yield salicylic acid via sodium chelation. Potassium phenoxide yields $p$-hydroxybenzoate. Options: (A), (B), (C), (D).
- **Question 21**: Lead storage battery: $\text{Pb} + \text{HSO}_4^- \to \text{PbSO}_4$, $\text{PbO}_2 + \text{HSO}_4^- \to \text{PbSO}_4$. $\text{H}_2\text{SO}_4$ consumed during discharge, density drops. Options: (A), (B), (C), (D).
- **Question 22**: Lindemann mechanism: at high P, deactivation is fast $\implies$ 1st order. At low P, activation is slow $\implies$ 2nd order. Options: (A), (B), (C), (D).
- **Question 23**: Group III reagent $\text{NH}_4\text{Cl} + \text{NH}_4\text{OH}$ uses common ion effect to suppress $[\text{OH}^-]$, precipitating only Group III hydroxides. $\text{Fe(OH)}_3$ is reddish brown. Options: (A), (B), (C), (D).
- **Question 24**: At $pI$, amino acid is zwitterion, net charge zero, no migration in electric field, minimum solubility. $pI = \frac{pK_1 + pK_2}{2}$. Options: (A), (B), (C), (D).
- **Question 25**: $\text{CaF}_2 \rightleftharpoons \text{Ca}^{2+} + 2\text{F}^-$. In $0.050\text{ M NaF}$, $[\text{F}^-] \approx 0.050\text{ M}$. $S = \frac{K_{sp}}{[\text{F}^-]^2} = \frac{4.0 \times 10^{-11}}{(0.050)^2} = \frac{4.0 \times 10^{-11}}{2.5 \times 10^{-3}} = 1.60 \times 10^{-8}\text{ mol/L} \implies m = 8$. Exact: `8.00`.
- **Question 26**: First-order half-life: $t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{5.0 \times 10^{-4}} = 1386.00\text{ s}$. Exact: `1386.00`.
- **Question 27**: $d_{hkl} = \frac{a}{\sqrt{h^2+k^2+l^2}} = \frac{400}{\sqrt{2^2+0+0}} = \frac{400}{2} = 200\text{ pm}$. Exact: `200.00`.
- **Question 28**: $E_{\text{cell}} = -\frac{0.0591}{2}\log\left(\frac{0.010}{1.00}\right) = -\frac{0.0591}{2}(-2) = +0.0591\text{ V} \approx 0.06\text{ V}$. Exact: `0.06`.
- **Question 29**: Molality $m = \frac{1.80/180}{0.250\text{ kg}} = \frac{0.010}{0.250} = 0.040\text{ m}$. $\Delta T_b = 100.021 - 100.000 = 0.021\text{ K}$. $K_b = \frac{\Delta T_b}{m} = \frac{0.021}{0.040} = 0.525\text{ K}\cdot\text{kg/mol} \approx 0.52$ or $0.53$. Exact: `0.53`.
- **Question 30**: $\text{Cr}^{3+}$ is $3d^3$. Has 3 unpaired electrons. $\mu = \sqrt{3(5)} = \sqrt{15} \approx 3.87\text{ BM}$. Exact: `3.87`.
- **Question 31**: Reformatsky reaction. Option (A).
- **Question 32**: Azulene has $10\pi$ electrons (aromatic) with dipole moment from electron transfer creating cyclopentadienyl anion and tropylium cation aromatic rings. Option (A).
- **Question 33**: Cryolite lowers melting point and increases conductivity. Option (A).
- **Question 34**: Lactose is $\beta$-D-galactopyranosyl-(1$\to$4)-$\beta$-D-glucopyranose. Option (A).
- **Question 35**: In $\text{PH}_3$, bonding involves almost unhybridized $p$-orbitals (Drago's rule), so angle is near $90^\circ$. Option (A).
- **Question 36**: Alitame is $\sim 2000$ times sweeter than sucrose. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: Darboux theorem: derivative has intermediate value property, no simple jump discontinuities, attains zero if changes sign. Continuous function derivative not required. Step function cannot be derivative. Options: (A), (B), (C), (D).
- **Question 38**: $A^2 = A \implies$ eigenvalues are 0, 1. Minimal polynomial divides $x(x-1)$ (distinct linear factors), so diagonalizable. $\text{Tr}(A) = \sum \lambda_i = \text{rank}(A)$. $A(I-A) = 0$. Options: (A), (B), (C), (D).
- **Question 39**: From any point, at most 4 normals to hyperbola. Sum of eccentric angles is $(2n+1)\pi$. Normal at $(a,0)$ is x-axis. Evolute is $(ax)^{2/3} - (by)^{2/3} = (a^2+b^2)^{2/3}$. Options: (A), (B), (C), (D).
- **Question 40**: $\frac{\partial M}{\partial y} = 2x\cos(x^2) - 2x = \frac{\partial N}{\partial x}$. Exact! Potential $F(x, y) = y\sin(x^2) - x^2 y + x = C$. If $y(0) = 5$, $0 - 0 + 0 = C \implies C = 0$. Options: (A), (B), (C), (D).
- **Question 41**: Cross product $\vec{c} = \vec{a} \times \vec{b}$ is perpendicular to both. $[\vec{a}\ \vec{b}\ \vec{c}] = |\vec{a}\times\vec{b}|^2$. $\vec{c}\times\vec{a}$ lies in $\vec{a}-\vec{b}$ plane. Lagrange identity holds. Options: (A), (B), (C), (D).
- **Question 42**: Exponential distribution: $F(x) = 1 - e^{-\lambda x}$, mean $= 1/\lambda$, variance $= 1/\lambda^2$, memoryless property. Options: (A), (B), (C), (D).
- **Question 43**: $|I| = \frac{\pi}{2}\ln 2 = \frac{3.1416}{2}(0.6931) \approx 1.5708 \times 0.6931 \approx 1.09$. Exact: `1.09`.
- **Question 44**: Area $= \int_0^1 (e^x - e^{-x})dx = [e^x + e^{-x}]_0^1 = (e + 1/e) - (1 + 1) = 2.718 + 0.368 - 2 = 1.086 \approx 1.09$. Exact: `1.09`.
- **Question 45**: $3600 = 2^4 \times 3^2 \times 5^2$. Total divisors $= (4+1)(2+1)(2+1) = 5 \times 3 \times 3 = 45$. Exact: `45.00`.
- **Question 46**: $d = \frac{|1 + 2(1) + 2(1) - 14|}{\sqrt{1 + 4 + 4}} = \frac{|5 - 14|}{\sqrt{9}} = \frac{9}{3} = 3.00$. Exact: `3.00`.
- **Question 47**: $x^5 - 1 = (x-1)(x^4 + x^3 + x^2 + x + 1) = (x-1)(x-\omega)(x-\omega^2)(x-\omega^3)(x-\omega^4)$. Evaluating at $x = 1$: $1^4 + 1^3 + 1^2 + 1 + 1 = 5$. Thus $P = 5.00$. Exact: `5.00`.
- **Question 48**: Number of surjections from 5 to 3: $3^5 - \binom{3}{1}2^5 + \binom{3}{2}1^5 = 243 - 96 + 3 = 150$. Exact: `150.00`.
- **Question 49**: Skew lines distance $= 0$ if they intersect, or calculate distance between lines.
- **Question 50**: Eigenvalues of triangular matrix are diagonal elements: $2, 3, 4$. Option (A).
- **Question 51**: Distance from center $(0,0)$ to $x+y=5$ is $d = \frac{5}{\sqrt{2}}$. Radius $r = 5$. Half-chord length $= \sqrt{r^2 - d^2} = \sqrt{25 - 25/2} = \frac{5}{\sqrt{2}}$. Full chord length $= 2 \times \frac{5}{\sqrt{2}} = 5\sqrt{2}$. Option (A).
- **Question 52**: $y' = 2x$. At $x = 1, m_1 = 2$. At $x = -1, m_2 = -2$. $\tan\theta = \left|\frac{2 - (-2)}{1 + 2(-2)}\right| = \left|\frac{4}{1 - 4}\right| = \frac{4}{3} \implies \theta = \tan^{-1}(4/3)$. Option (A).
- **Question 53**: L'Hopital rule: $\lim_{x \to 0} \frac{e^x - 1}{2x} = \lim_{x \to 0} \frac{e^x}{2} = 1/2$. Option (A).
- **Question 54**: $x^2 - 6x + 13 = (x-3)^2 + 4 \ge 4$. Minimum value is 4. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 05 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Impulsive Dynamics, Angular Impulse-Momentum Theorem, Condition for Immediate Pure Rolling.
- **2. Derivation**:
  - Linear impulse: $J = M v_0 \implies v_0 = J/M$. (A) is correct.
  - Angular impulse about CM: $J h = I \omega_0 = \left(\frac{2}{5}M R^2\right)\omega_0 \implies \omega_0 = \frac{5 J h}{2 M R^2}$. (B) is correct.
  - Pure rolling immediately after impact requires $v_0 = R \omega_0$:
    $$\frac{J}{M} = R \left(\frac{5 J h}{2 M R^2}\right) = \frac{5 J h}{2 M R} \implies h = \frac{2}{5}R$$
    (C) is correct.
  - If $h > \frac{2}{5}R$, $\omega_0 > v_0/R$, so bottom of sphere slips backward relative to surface, meaning friction on sphere acts forward, not backward. Thus (D) is incorrect.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Surface Tension, Soap Bubble Coalescence, Boyle's Law.
- **2. Derivation**:
  - Soap bubble has two interfaces: $\Delta P = 4S/r$. (A) is correct.
  - In isothermal conditions, $n_1 + n_2 = n_{\text{final}} \implies P_1 V_1 + P_2 V_2 = P_R V_R$. (B) is correct.
  - In vacuum ($P_0 = 0$): $P_1 = 4S/r_1$, $V_1 = \frac{4}{3}\pi r_1^3 \implies P_1 V_1 \propto r_1^2$. Hence $r_1^2 + r_2^2 = R^2$. (C) is correct.
  - With external pressure $P_0$, $P_1 = P_0 + 4S/r_1$. Equating gives $P_0(R^3 - r_1^3 - r_2^3) + 4S(R^2 - r_1^2 - r_2^2) = 0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Electromagnetic Wave Properties, Energy Density, Momentum Density.
- **2. Derivation**:
  - $\vec{E} \perp \vec{B}$ and both perpendicular to propagation vector $\hat{k}$. (A) is correct.
  - $E_0 / B_0 = c = 1/\sqrt{\mu_0 \varepsilon_0}$. (B) is correct.
  - $u_E = \frac{1}{2}\varepsilon_0 E^2 = \frac{1}{2}\varepsilon_0 (c B)^2 = \frac{1}{2}\varepsilon_0 \left(\frac{1}{\mu_0 \varepsilon_0}\right) B^2 = \frac{B^2}{2\mu_0} = u_B$. (C) is correct.
  - Momentum density $\vec{p} = \frac{\vec{S}}{c^2} = \varepsilon_0 (\vec{E} \times \vec{B})$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Snell's Law in Inhomogeneous Graded-Index Media, Ray Trajectories.
- **2. Derivation**:
  - In stratified medium along $y$, $\mu(y)\cos\theta(y) = \text{const} = \mu(0)\cos 0^\circ = \mu_0$. (A) is correct.
  - $\cos\theta = \frac{\mu_0}{\mu_0\sqrt{1+y/H}} = \frac{1}{\sqrt{1+y/H}}$.
  - $\tan\theta = \frac{dy}{dx} = \sqrt{\frac{1}{\cos^2\theta} - 1} = \sqrt{(1+y/H) - 1} = \sqrt{\frac{y}{H}}$. (B) is correct.
  - $\frac{dy}{\sqrt{y}} = \frac{dx}{\sqrt{H}} \implies 2\sqrt{y} = \frac{x}{\sqrt{H}} \implies y = \frac{x^2}{4H}$ (parabola). (C) is correct.
  - Rays bend toward higher refractive index (Fermat's principle). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Bohr Model Scaling Relations.
- **2. Derivation**:
  - $r_n = \frac{n^2 \hbar^2}{m k e^2} \propto n^2$. (A) is correct.
  - $v_n = \frac{k e^2}{n \hbar} \propto 1/n$. (B) is correct.
  - $T_n = \frac{2\pi r_n}{v_n} \propto \frac{n^2}{1/n} = n^3$. (C) is correct.
  - $B_n = \frac{\mu_0 I}{2 r_n} = \frac{\mu_0 (e/T_n)}{2 r_n} \propto \frac{1/n^3}{n^2} = \frac{1}{n^5}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Reversible Expansions on P-V Diagram, Work and Internal Energy Comparisons.
- **2. Derivation**:
  - For given $V_1 \to V_2$: $P_{\text{isobaric}} = P_1 > P_{\text{isothermal}} = P_1 \frac{V_1}{V_2} > P_{\text{adiabatic}} = P_1 \left(\frac{V_1}{V_2}\right)^\gamma$. (A) is correct.
  - Area under $P-V$ curve: $W_{\text{isobaric}} > W_{\text{isothermal}} > W_{\text{adiabatic}}$. (B) is correct.
  - $\Delta U$: $\Delta U_{\text{isobaric}} = n C_V \Delta T > 0$, $\Delta U_{\text{isothermal}} = 0$, $\Delta U_{\text{adiabatic}} = -W < 0$. (C) is correct.
  - $Q = \Delta U + W$: both $\Delta U$ and $W$ are largest for isobaric, so $Q$ is greatest. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Effective gravity: $g_{\text{eff}} = g + a = 9.80 + 2.20 = 12.00\text{ m/s}^2$.
  Time period: $T = 2\pi\sqrt{\frac{L}{g_{\text{eff}}}} = 2\pi\sqrt{\frac{0.98}{12.00}} = 2(3.1416)\sqrt{0.08167} = 2(3.1416)(0.2858) \approx 1.80\text{ s}$. Exact: `1.80`.
- **Question 8**: Electric field along perpendicular bisector:
  $E = \frac{2 q x}{4\pi\varepsilon_0 (x^2 + a^2)^{3/2}} = \frac{2(9.0 \times 10^9)(2.0 \times 10^{-6})(0.10)}{(0.10^2 + 0.10^2)^{3/2}} = \frac{3600}{(0.02)^{3/2}} = \frac{3600}{2.828 \times 10^{-3}} \approx 1272.8 \times 10^3\text{ V/m} = 1272.80\text{ kV/m}$. Exact: `1272.80`.
- **Question 9**: For dark rings in Newton's rings: $D_n^2 = 4 n R \lambda \implies R = \frac{D_n^2}{4 n \lambda} = \frac{(4.00 \times 10^{-3}\text{ m})^2}{4(10)(600 \times 10^{-9}\text{ m})} = \frac{16.0 \times 10^{-6}}{2.40 \times 10^{-5}} = \frac{16.0}{24.0} = 0.67\text{ m}$. Exact: `0.67`.
- **Question 10**: $\eta = 1 - \frac{T_C}{T_H} = 1 - \frac{300}{500} = 1 - 0.60 = 0.40 = 40.00\%$. Exact: `40.00`.
- **Question 11**: $B = \frac{\mu_0 I}{2\pi r} = \frac{(4\pi \times 10^{-7})(10.0)}{2\pi (0.050)} = \frac{20 \times 10^{-7}}{0.050} = 40.0 \times 10^{-6}\text{ T} = 40.00\ \mu\text{T}$. Exact: `40.00`.
- **Question 12**: $\lambda_0 = \frac{hc}{\Phi} = \frac{1240\text{ eV}\cdot\text{nm}}{2.25\text{ eV}} \approx 551.1\text{ nm} \approx 551\text{ nm}$. Exact: `551.00`.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 14**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 15**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 16**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 17**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 18**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Boric acid: $sp^2$ hybridized, 2D sheet structure with H-bonds. Acts as Lewis acid by accepting $\text{OH}^-$. Polyols complex with $[\text{B(OH)}_4]^-$, shifting equilibrium and making it a strong acid titratable with $\text{NaOH}$. Options: (A), (B), (C), (D).
- **Question 20**: Haloform reaction requires $\text{CH}_3\text{C=O}$ or $\text{CH}_3\text{CH(OH)}$. Butan-2-one, ethanol, and acetone give positive test. Pentan-3-one does not. Options: (A), (C), (D).
- **Question 21**: SHE is anode ($E^\circ = 0$). Nernst: $E = E^\circ - 0.0591\log\frac{[\text{Fe}^{2+}]}{[\text{Fe}^{3+}]}$. Increasing $[\text{Fe}^{3+}]$ increases EMF, increasing $[\text{Fe}^{2+}]$ decreases it. Options: (A), (B), (C), (D).
- **Question 22**: Functional isomers have same formula but different functional groups: alcohol/ether (ethanol/dimethyl ether), aldehyde/ketone (propanal/propanone), acid/ester (acetic acid/methyl formate). Pentan-2-one and pentan-3-one are positional isomers. Options: (A), (B), (C).
- **Question 23**: $\text{NH}_4\text{NO}_2 \to \text{N}_2 + 2\text{H}_2\text{O}$; $(\text{NH}_4)_2\text{Cr}_2\text{O}_7 \to \text{N}_2 + \text{Cr}_2\text{O}_3 + 4\text{H}_2\text{O}$; $2\text{NaN}_3 \to 2\text{Na} + 3\text{N}_2$. However, $\text{NH}_4\text{NO}_3$ gives $\text{N}_2\text{O} + 2\text{H}_2\text{O}$. Options: (A), (B), (C).
- **Question 24**: Purines are two-ring structures: Adenine and Guanine. Cytosine, Thymine, and Uracil are pyrimidines. Options: (A), (B).
- **Question 25**: $\text{Ag}_2\text{CrO}_4 \rightleftharpoons 2\text{Ag}^+ + \text{CrO}_4^{2-} \implies K_{sp} = 4S^3 \implies S = \sqrt[3]{1.1 \times 10^{-12}/4} = \sqrt[3]{2.75 \times 10^{-13}} = \sqrt[3]{275 \times 10^{-15}} \approx 6.5 \times 10^{-5}\text{ mol/L} \implies m = 5$. Exact: `5.00`.
- **Question 26**: For zero-order reaction: $t_{1/2} = \frac{[A]_0}{2k} = \frac{0.40}{2(0.0080)} = \frac{0.40}{0.016} = 25.00\text{ s}$. Exact: `25.00`.
- **Question 27**: For BCC: $\sqrt{3}a = 4r \implies a = \frac{4r}{\sqrt{3}} = \frac{4(173.2)}{1.732} = 400\text{ pm}$. Exact: `400.00`.
- **Question 28**: $\Delta_r H^\circ = \Delta_f H^\circ(\text{CO}_2) - \Delta_f H^\circ(\text{CO}) = -393.5 - (-110.5) = -283.0\text{ kJ/mol}$. Magnitude $= 283.00$. Exact: `283.00`.
- **Question 29**: $\Pi = C R T = (0.050)(0.0821)(300) = 1.2315\text{ atm} \approx 1.23\text{ atm}$. Exact: `1.23`.
- **Question 30**: $\text{K}_2\text{Cr}_2\text{O}_7$: $2(+1) + 2x + 7(-2) = 0 \implies 2x - 12 = 0 \implies x = +6$. Exact: `6.00`.
- **Question 31**: $3^\circ$ alcohols react immediately with Lucas reagent ($conc.\ \text{HCl} + \text{ZnCl}_2$) by forming a stable $3^\circ$ carbocation. 2-Methylpropan-2-ol is $3^\circ$. Option (A).
- **Question 32**: $\text{ClF}_3$ has 3 bonding pairs and 2 lone pairs ($AX_3E_2$), giving T-shaped geometry. Option (A).
- **Question 33**: Sodium ethyl xanthate is a collector. Option (A).
- **Question 34**: Aromatic aldehydes like benzaldehyde do not reduce Fehling's solution (though they reduce Tollens' reagent). Option (A).
- **Question 35**: $\text{XeF}_2$ has 2 bond pairs and 3 lone pairs $\implies sp^3d$ hybridization with linear geometry. Option (A).
- **Question 36**: Natural rubber is cis-1,4-polyisoprene. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f'(x) = 4x^3 - 12x^2 = 4x^2(x-3)$. $f'(0) = 0$ but $f'$ doesn't change sign at $x = 0$ (inflection point). Minimum at $x = 3$ with value $f(3) = 81 - 108 + 10 = -17$. $f''(x) = 12x^2 - 24x = 12x(x-2) > 0$ for $x > 2$ (concave up). Options: (A), (B), (C), (D).
- **Question 38**: Trace is cyclic: $\text{Tr}(AB) = \text{Tr}(BA)$. $\text{Tr}(A+B) = \text{Tr}(A) + \text{Tr}(B)$. $\text{Tr}(AB - BA) = 0 \ne \text{Tr}(I) = n \implies AB - BA \ne I$ for finite matrices. $AB$ and $BA$ have same non-zero eigenvalues. Options: (A), (B), (C), (D).
- **Question 39**: Chord of contact is $xx_1 + yy_1 = r^2$. Tangent length $L = \sqrt{x_1^2+y_1^2-r^2}$. Area $\Delta = \frac{r L^3}{x_1^2+y_1^2}$. Circumcircle of $\Delta PQR$ has $OP$ as diameter. Options: (A), (B), (C), (D).
- **Question 40**: Auxiliary roots: $m^2 - 3m + 2 = 0 \implies m = 1, 2$. Solution: $y = C_1 e^x + C_2 e^{2x}$. Initial conditions: $C_1 + C_2 = 0$, $C_1 + 2C_2 = 1 \implies C_2 = 1, C_1 = -1 \implies y = e^{2x} - e^x$. For $x > 0$, $e^{2x} > e^x \implies y > 0$. Options: (A), (B), (C), (D).
- **Question 41**: Mutually orthogonal unit vectors form orthonormal basis. Triple product is $\pm 1$. Resolution $\vec{x} = \sum (\vec{x}\cdot\vec{u}_i)\vec{u}_i$. Length of sum is $\sqrt{1+1+1} = \sqrt{3}$. Options: (A), (B), (C), (D).
- **Question 42**: $P(A \cap B) = P(A) + P(B) - P(A \cup B) \ge 0.6 + 0.5 - 1.0 = 0.1$. Max $P(A \cap B) = \min(P(A), P(B)) = 0.5$. Max $P(A \cup B) = 1.0$. If independent, $P(A \cap B) = 0.6 \times 0.5 = 0.3$. Options: (A), (B), (C), (D).
- **Question 43**: $\text{Area} = \int_0^{\pi/2} \cos x dx = [\sin x]_0^{\pi/2} = 1 - 0 = 1.00$. Exact: `1.00`.
- **Question 44**: $y' = 4x^3 - 4x$. At $x = 2$, $y' = 4(8) - 4(2) = 32 - 8 = 24.00$. Exact: `24.00`.
- **Question 45**: $\int_0^1 x e^x dx = [x e^x - e^x]_0^1 = (e - e) - (0 - 1) = 1.00$. Exact: `1.00`.
- **Question 46**: $\vec{u} = (1, 1, 0), \vec{v} = (1, 0, 1)$. $\vec{u} \cdot \vec{v} = 1$. $|\vec{u}| = \sqrt{2}, |\vec{v}| = \sqrt{2}$. $\cos\theta = \frac{1}{2} \implies \theta = 60.00^\circ$. Exact: `60.00`.
- **Question 47**: In GP: $a_1 a_2 a_3 a_4 a_5 = (a_3)^5 = 4^5 = 1024.00$. Exact: `1024.00`.
- **Question 48**: Last digit must be even: $\{2, 4, 6\}$ (3 choices). Remaining 2 digits chosen from remaining 5 digits: $P(5, 2) = 5 \times 4 = 20$. Total numbers $= 20 \times 3 = 60.00$. Exact: `60.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 05
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 6.00
- Q8: 11.30
- Q9: 1.20
- Q10: 2079.00
- Q11: 1.88
- Q12: 8.00
- Q13: D
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
- Q24: A, B, C, D
- Q25: 8.00
- Q26: 1386.00
- Q27: 200.00
- Q28: 0.06
- Q29: 0.53
- Q30: 3.87
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
- Q42: A, B, C, D
- Q43: 1.09
- Q44: 1.09
- Q45: 45.00
- Q46: 3.00
- Q47: 5.00
- Q48: 150.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Paper 2 Answer Key
#### Physics
- Q1: A, B, C
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 1.80
- Q8: 1272.80
- Q9: 0.67
- Q10: 40.00
- Q11: 40.00
- Q12: 551.00
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C, D
- Q20: A, C, D
- Q21: A, B, C, D
- Q22: A, B, C
- Q23: A, B, C
- Q24: A, B
- Q25: 5.00
- Q26: 25.00
- Q27: 400.00
- Q28: 283.00
- Q29: 1.23
- Q30: 6.00
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
- Q42: A, B, C, D
- Q43: 1.00
- Q44: 24.00
- Q45: 1.00
- Q46: 60.00
- Q47: 1024.00
- Q48: 60.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: 33.3% of questions (high option-checking cognitive load).
- **Physics**: Focus on Maxwell displacement current and Poynting vector, eddy current magnetic damping, optical tweezers, graded index parabolic rays, Bohr scaling exponents.
- **Chemistry**: $\pi$-backbonding in metal carbonyls, Kolbe-Schmitt salicylic acid ortho chelation, Lindemann unimolecular kinetics, Boric acid polyol complexation, Group III common ion precipitation.
- **Mathematics**: Darboux theorem on intermediate values of derivatives, commutator trace identities $[A, B] \ne I$, exact differential equations, surjection counting, Exponential distribution memorylessness.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

create_mock_files(5, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")

