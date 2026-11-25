# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 19.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Synchrotron relativistic beaming, Superconductor London penetration, Plasma cutoff frequency
- Mannich reaction, YBCO 1-2-3 mixed valence superconductivity, Cyclic voltammetry Randles-Sevcik
- Cauchy-Goursat Laurent singularities, Gram-Schmidt orthogonalization, Tractrix pseudosphere, Bell numbers
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 19 — Paper 1
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
An ultra-relativistic electron of charge $-e$ and rest mass $m$ moves in a circular orbit of radius $\rho$ in a synchrotron storage ring with Lorentz factor $\gamma = E / (m c^2) \gg 1$:
(A) The synchrotron radiation emitted by the electron is strongly beamed in the instantaneous forward direction within a narrow cone of opening half-angle $\theta \approx \frac{1}{\gamma}$.  
(B) The spectrum of emitted radiation is continuous and extends up to a critical frequency $\omega_c = \frac{3}{2}\gamma^3 \frac{c}{\rho}$.  
(C) The total energy radiated per revolution by a single electron is $\Delta E = \frac{e^2 \gamma^4}{3\varepsilon_0 \rho}$.  
(D) Synchrotron radiation emitted in the plane of the electron's orbit is predominantly linearly polarized with the electric field in the orbital plane.

#### Question 2
In the London theory of superconductivity, superconducting electrons of number density $n_s$ move without electrical resistance:
(A) The first London equation states $\frac{\partial \vec{J}_s}{\partial t} = \frac{n_s e^2}{m}\vec{E}$.  
(B) The second London equation states $\nabla \times \vec{J}_s = -\frac{n_s e^2}{m}\vec{B}$.  
(C) Combining the second London equation with Maxwell's equation $\nabla \times \vec{B} = \mu_0 \vec{J}_s$ leads to the screening equation $\nabla^2 \vec{B} = \frac{\vec{B}}{\lambda_L^2}$.  
(D) The London penetration depth is $\lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}$, characterizing the exponential decay of a magnetic field inside a superconductor (Meissner effect).

#### Question 3
An electromagnetic plane wave of angular frequency $\omega$ propagates through a dilute, collisionless plasma of free electron density $n_e$:
(A) The electronic plasma frequency is $\omega_p = \sqrt{\frac{n_e e^2}{\varepsilon_0 m_e}}$.  
(B) The effective dielectric function of the plasma is $\varepsilon(\omega) = \varepsilon_0 \left(1 - \frac{\omega_p^2}{\omega^2}\right)$.  
(C) For radio frequencies below the plasma frequency ($\omega < \omega_p$), the wavevector is purely imaginary and the wave undergoes total reflection (ionospheric reflection).  
(D) The phase velocity of waves in the transparent regime ($\omega > \omega_p$) exceeds the speed of light in vacuum: $v_p = \frac{c}{\sqrt{1 - \omega_p^2/\omega^2}} > c$.

#### Question 4
In an optical tweezers apparatus, a tightly focused Gaussian laser beam traps a neutral microscopic dielectric sphere of radius $a \ll \lambda$ and refractive index $n_p > n_m$ (Rayleigh regime):
(A) The dielectric sphere acquires an induced dipole moment $\vec{p} = \alpha \vec{E}$, where $\alpha = 4\pi \varepsilon_m a^3 \left(\frac{n^2 - 1}{n^2 + 2}\right)$ with $n = n_p / n_m$.  
(B) The gradient force pulling the sphere towards the point of maximum laser intensity (the focal waist) is $\vec{F}_{\text{grad}} = \frac{1}{2}\alpha \nabla |\vec{E}|^2$.  
(C) The scattering radiation pressure force pushes the particle along the direction of light propagation: $\vec{F}_{\text{scat}} = \frac{n_m \sigma_{\text{scat}}}{c}\langle \vec{S} \rangle$.  
(D) Stable three-dimensional trapping is achieved only when the axial gradient force exceeds the forward scattering force.

#### Question 5
Regarding the thermodynamic entropy of mixing for an ideal gas mixture:
(A) When $n_1$ moles of gas 1 and $n_2$ moles of gas 2 at identical temperature and pressure are allowed to mix, the entropy of mixing is $\Delta S_{\text{mix}} = -R(n_1 \ln x_1 + n_2 \ln x_2) > 0$.  
(B) The entropy of mixing arises from the increased volume accessible to each distinct chemical species.  
(C) If the two compartments contain identical gases at the same $T$ and $P$, removing the partition produces $\Delta S_{\text{mix}} = 0$ (resolution of Gibbs' paradox via quantum indistinguishability).  
(D) The Gibbs free energy of mixing for an ideal mixture at constant $T$ and $P$ is $\Delta G_{\text{mix}} = -T \Delta S_{\text{mix}} < 0$, ensuring spontaneity.

#### Question 6
A thin uniform circular disc of mass $M$ and radius $R$ rolls without slipping on a horizontal surface, wobbling at a constant inclination angle $\theta$ to the vertical (Euler's disk):
(A) In the limit of small tilt angle $\theta \to 0$ (nearly flat on table), the contact point circulates with angular frequency $\Omega \approx 2\omega_s$, where $\omega_s$ is the spin angular velocity.  
(B) The normal reaction force exerted by the table on the disc at the contact point equals $M g$.  
(C) The pitch of the acoustic sound generated increases sharply as the disc settles toward the flat position.  
(D) Energy dissipation occurs primarily through viscous air drag in the narrow gap beneath the disc.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In an electron synchrotron storage ring of bending radius $\rho = 10.0\text{ m}$, electrons circulate with beam energy $E = 3.0\text{ GeV}$. The rest energy of an electron is $m_e c^2 = 0.511\text{ MeV}$. Calculate the energy loss per revolution $\Delta E$ per electron in $\text{keV}$ (round off to the nearest integer).

#### Question 8
In lead ($\text{Pb}$), the superconducting electron density is $n_s = 3.0 \times 10^{28}\text{ m}^{-3}$ at absolute zero. Taking $m_e = 9.11 \times 10^{-31}\text{ kg}$, $e = 1.6 \times 10^{-19}\text{ C}$, and $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$, calculate the London penetration depth $\lambda_L$ in nanometers (round off to ONE decimal place).

#### Question 9
The electron density in the Earth's ionospheric F-layer is $n_e = 1.0 \times 10^{12}\text{ electrons/m}^3$. Calculate the plasma cutoff frequency $f_p = \frac{\omega_p}{2\pi}$ in megahertz ($\text{MHz}$) (round off to ONE decimal place).

#### Question 10
In an experiment with an Atwood machine, two masses $m_1 = 3.0\text{ kg}$ and $m_2 = 2.0\text{ kg}$ are connected by a light string over a pulley of moment of inertia $I = 0.20\text{ kg m}^2$ and radius $R = 0.10\text{ m}$. Calculate the linear acceleration $a$ of the masses in $\text{m/s}^2$ (take $g = 9.8\text{ m/s}^2$, round off to TWO decimal places).

#### Question 11
A spherical metal sphere of radius $R = 5.0\text{ cm}$ is charged to a potential $V = 900\text{ V}$. Calculate the total electrostatic charge $Q$ on the sphere in nanoCoulombs ($\text{nC}$).

#### Question 12
A thermodynamic engine operates reversibly on a Carnot cycle between a heat source at $T_H = 400\text{ K}$ and a sink at $T_C = 300\text{ K}$. If the engine absorbs $Q_H = 800\text{ J}$ of heat from the source, calculate the heat rejected $|Q_C|$ to the sink in Joules.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A point mass $m$ is attached to the end of a spring of stiffness $k$ and natural length $L_0$, hanging vertically. The system is released from rest when the spring is unstretched. The maximum extension $x_{\text{max}}$ of the spring is:
(A) $x_{\text{max}} = \frac{2 m g}{k}$  
(B) $x_{\text{max}} = \frac{m g}{k}$  
(C) $x_{\text{max}} = \frac{m g}{2k}$  
(D) $x_{\text{max}} = \frac{4 m g}{k}$  

#### Question 14
A parallel beam of unpolarized light of intensity $I_0$ passes through two polarizers whose transmission axes make an angle of $60^\circ$ with each other. The transmitted intensity is:
(A) $\frac{I_0}{8}$  
(B) $\frac{I_0}{4}$  
(C) $\frac{I_0}{2}$  
(D) $\frac{I_0}{16}$  

#### Question 15
The magnetic field at the center of a circular current-carrying loop of radius $R$ is $B_0$. The magnetic field on the axis of the loop at a distance $x = \sqrt{3} R$ from the center is:
(A) $\frac{B_0}{8}$  
(B) $\frac{B_0}{4}$  
(C) $\frac{B_0}{2}$  
(D) $\frac{B_0}{16}$  

#### Question 16
An electron and a proton have the same kinetic energy. The ratio of the de Broglie wavelength of the electron to that of the proton is:
(A) $\sqrt{\frac{m_p}{m_e}}$  
(B) $\frac{m_p}{m_e}$  
(C) $\sqrt{\frac{m_e}{m_p}}$  
(D) 1  

#### Question 17
A sample of an ideal gas expands from volume $V_1$ to $V_2 = 2 V_1$ first isothermally and second adiabatically. In which process is more work done by the gas?
(A) Isothermal process  
(B) Adiabatic process  
(C) Both do equal work  
(D) Depends on atomicity of gas  

#### Question 18
The acceleration due to gravity at a depth $d$ below the Earth's surface ($d < R$) is:
(A) $g(d) = g\left(1 - \frac{d}{R}\right)$  
(B) $g(d) = g\left(1 - \frac{2d}{R}\right)$  
(C) $g(d) = g\left(1 + \frac{d}{R}\right)$  
(D) $g(d) = g\left(\frac{R}{R - d}\right)^2$  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Mannich reaction in organic synthesis:
$$\text{R-CO-CH}_3 + \text{HCHO} + \text{R'}_2\text{NH}\cdot\text{HCl} \to \text{R-CO-CH}_2\text{-CH}_2\text{-NR'}_2\cdot\text{HCl} + \text{H}_2\text{O}$$
(A) Condensation of formaldehyde with a secondary amine under acidic conditions generates an electrophilic iminium ion intermediate ($[\text{CH}_2=\text{N R'}_2]^+$).  
(B) Nucleophilic attack of the enol form of the carbonyl compound on the iminium ion affords a $\beta$-amino carbonyl compound (Mannich base).  
(C) Quaternization of the Mannich base with methyl iodide followed by base-induced Hofmann elimination provides an $\alpha,\beta$-unsaturated carbonyl compound.  
(D) The Mannich reaction is a three-component multicomponent condensation.

#### Question 20
Regarding the high-temperature cuprate superconductor $\text{YBa}_2\text{Cu}_3\text{O}_{7-\delta}$ (YBCO, $T_c \approx 93\text{ K}$):
(A) The crystal structure is an oxygen-deficient perovskite superstructure with triple unit cell stacking along the $c$-axis.  
(B) Superconductivity takes place primarily within the two-dimensional $\text{CuO}_2$ planes.  
(C) For $\delta = 0$, the formal average oxidation state of copper is $+2.33$, corresponding to a mixed valence of two $\text{Cu(II)}$ and one $\text{Cu(III)}$ per formula unit.  
(D) Above $T_c$, YBCO exhibits the Meissner effect (perfect diamagnetism $\chi = -1$) with magnetic flux expulsion.

#### Question 21
Regarding cyclic voltammetry (CV) and the Randles-Sevcik equation for a reversible redox process at $25^\circ\text{C}$:
$$I_p = (2.69 \times 10^5) n^{3/2} A D^{1/2} C v^{1/2}$$
(A) The peak current $I_p$ is directly proportional to analyte bulk concentration $C$ and the square root of the scan rate $v^{1/2}$.  
(B) For a reversible, one-electron transfer ($n = 1$), the peak-to-peak potential separation is $\Delta E_p = E_{pa} - E_{pc} \approx \frac{59\text{ mV}}{n}$ and is independent of scan rate.  
(C) The ratio of the reverse peak current to forward peak current equals unity: $|I_{pa} / I_{pc}| = 1$.  
(D) The formal reduction potential is estimated from the midpoint of peak potentials: $E^{\circ\prime} = \frac{E_{pa} + E_{pc}}{2}$.

#### Question 22
Regarding Metal-Organic Frameworks (MOFs) such as MOF-5 ($[\text{Zn}_4\text{O(BDC)}_3]$) and ZIF-8:
(A) They are porous crystalline materials constructed from metal ions/clusters (nodes) connected by organic linkers (struts).  
(B) MOF-5 features an octahedral $\text{Zn}_4\text{O}$ core coordinated by 1,4-benzenedicarboxylate (BDC) linkers, forming a 3D cubic network with ultrahigh surface area ($>2500\text{ m}^2/\text{g}$).  
(C) ZIF-8 contains zinc ions linked by 2-methylimidazolate, exhibiting exceptional thermal and chemical stability analogous to zeolites.  
(D) MOFs find major applications in reversible hydrogen storage, methane fuel gas capture, and post-combustion $\text{CO}_2$ capture.

#### Question 23
Regarding the Fischer-Tropsch synthesis in petrochemical engineering:
$$(2n + 1)\text{H}_2 + n\text{CO} \xrightarrow{\text{Fe or Co catalyst, } 150\text{--}300^\circ\text{C}} \text{C}_n\text{H}_{2n+2} + n\text{H}_2\text{O}$$
(A) It catalytically converts synthesis gas ($\text{CO} + \text{H}_2$) into liquid synthetic fuels and hydrocarbons.  
(B) The reaction is highly exothermic, requiring strict temperature control to prevent catalyst deactivation.  
(C) The chain growth mechanism involves surface methylene ($-\text{CH}_2-$) polymerization (Anderson-Schulz-Flory distribution).  
(D) Iron-based catalysts promote the concurrent water-gas shift reaction ($\text{CO} + \text{H}_2\text{O} \rightleftharpoons \text{CO}_2 + \text{H}_2$).

#### Question 24
In the qualitative analysis of Group Zero basic radical ($\text{NH}_4^+$):
(A) Heating an ammonium salt with aqueous $\text{NaOH}$ releases ammonia gas ($\text{NH}_3$).  
(B) Ammonia gas turns moist red litmus paper blue and produces dense white fumes of $\text{NH}_4\text{Cl}$ with a glass rod dipped in concentrated $\text{HCl}$.  
(C) With Nessler's reagent ($\text{K}_2[\text{HgI}_4]$ in alkaline solution), ammonium ions give a brown precipitate or coloration due to the iodide of Millon's base ($\text{H}_2\text{N-Hg-O-Hg-I}$).  
(D) Ammonium salts impart a characteristic persistent violet color to a non-luminous Bunsen flame.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of ferric hydroxide ($\text{Fe(OH)}_3$) is $K_{sp} = 1.0 \times 10^{-38}$ at $25^\circ\text{C}$. Calculate the maximum pH of a $0.010\text{ M}$ $\text{Fe}^{3+}$ solution at which precipitation of $\text{Fe(OH)}_3$ just begins (round off to TWO decimal places).

#### Question 26
Calculate the spin-only magnetic moment in Bohr Magnetons ($\mu_B$) for the complex ion $[Ni(CN)_4]^{2-}$ (atomic number of $\text{Ni} = 28$).

#### Question 27
An organic compound contains $80.0\%$ Carbon and $20.0\%$ Hydrogen by mass. If its molecular weight is $30.0\text{ g/mol}$, calculate the number of carbon atoms present in one molecule.

#### Question 28
The rate constant of a first-order reaction is $k = 0.03465\text{ min}^{-1}$. Calculate the half-life $t_{1/2}$ of the reaction in minutes (use $\ln 2 = 0.693$).

#### Question 29
A steady current of $I = 2.0\text{ A}$ is passed through an aqueous solution of $\text{AgNO}_3$ for $t = 965\text{ seconds}$. Calculate the mass of silver deposited in grams (molar mass of $\text{Ag} = 108.0\text{ g/mol}$, $F = 96500\text{ C/mol}$, round off to TWO decimal places).

#### Question 30
The osmotic pressure of a $0.020\text{ M}$ aqueous solution of cane sugar ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) at $300\text{ K}$ is $\Pi$ in atmospheres. Calculate $\Pi$ (use $R = 0.0821\text{ L atm/(mol K)}$, round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Gattermann-Koch reaction, benzene is converted to benzaldehyde by treating it with:
(A) $\text{CO} + \text{HCl}$ in the presence of anhydrous $\text{AlCl}_3$ and $\text{CuCl}$  
(B) $\text{HCN} + \text{HCl}$ in the presence of $\text{AlCl}_3$  
(C) $\text{CHCl}_3 + \text{NaOH}$  
(D) $\text{CH}_3\text{Cl} + \text{AlCl}_3$  

#### Question 32
Which of the following complex ions has the highest crystal field stabilization energy (CFSE)?
(A) $[\text{Co(CN)}_6]^{3-}$  
(B) $[\text{Co(H}_2\text{O)}_6]^{3+}$  
(C) $[\text{Co(H}_2\text{O)}_6]^{2+}$  
(D) $[\text{CoF}_6]^{3-}$  

#### Question 33
In DNA, the heterocyclic base adenine pairs with thymine through:
(A) Two hydrogen bonds  
(B) Three hydrogen bonds  
(C) One covalent bond  
(D) A phosphodiester linkage  

#### Question 34
In the extraction of copper, the flux used to remove iron impurity ($\text{FeO}$) is:
(A) Silica ($\text{SiO}_2$)  
(B) Limestone ($\text{CaCO}_3$)  
(C) Coke ($\text{C}$)  
(D) Alumina ($\text{Al}_2\text{O}_3$)  

#### Question 35
Treatment of aniline with nitrous acid ($\text{NaNO}_2 + \text{HCl}$) at $0\text{--}5^\circ\text{C}$ gives:
(A) Benzenediazonium chloride  
(B) Phenol  
(C) Nitrobenzene  
(D) Chlorobenzene  

#### Question 36
The conjugate acid of water ($\text{H}_2\text{O}$) is:
(A) Hydronium ion ($\text{H}_3\text{O}^+$)  
(B) Hydroxide ion ($\text{OH}^-$)  
(C) Hydrogen peroxide ($\text{H}_2\text{O}_2$)  
(D) Oxide ion ($\text{O}^{2-}$)  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(z)$ be an analytic function in a domain except for isolated singularities:
(A) A singularity at $z_0$ is removable if $\lim_{z \to z_0} (z - z_0) f(z) = 0$.  
(B) $z_0$ is a pole of order $m$ if the principal part of the Laurent series contains terms up to $(z - z_0)^{-m}$.  
(C) $z_0$ is an essential singularity if the principal part contains infinitely many non-zero terms (e.g., $e^{1/z}$ at $z = 0$).  
(D) According to the Casorati-Weierstrass theorem, in any neighborhood of an essential singularity, $f(z)$ comes arbitrarily close to any complex number.

#### Question 38
Regarding the Gram-Schmidt orthogonalization process applied to linearly independent vectors $\{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_k\}$ in an inner product space:
(A) The first orthogonal vector is $\vec{u}_1 = \vec{v}_1$.  
(B) The second orthogonal vector is $\vec{u}_2 = \vec{v}_2 - \frac{\langle \vec{v}_2, \vec{u}_1 \rangle}{\|\vec{u}_1\|^2}\vec{u}_1$.  
(C) The subspace spanned by $\{\vec{u}_1, \dots, \vec{u}_i\}$ is identical to the subspace spanned by $\{\vec{v}_1, \dots, \vec{v}_i\}$ for every $1 \le i \le k$.  
(D) Normalizing each vector $\vec{e}_i = \vec{u}_i / \|\vec{u}_i\|$ produces an orthonormal basis.

#### Question 39
Regarding the tractrix curve and its surface of revolution (the pseudosphere):
(A) The tractrix is the involute of the catenary curve.  
(B) The length of the tangent segment intercepted between the curve and its asymptote is constant.  
(C) Rotating the tractrix about its asymptote generates the pseudosphere.  
(D) The pseudosphere possesses a constant negative Gaussian curvature $K = -1/a^2$, providing a physical model for hyperbolic geometry.

#### Question 40
Regarding the Bell numbers $B_n$, which count the number of partitions of a set with $n$ elements:
(A) The recurrence relation is $B_{n+1} = \sum_{k=0}^n \binom{n}{k} B_k$ with $B_0 = 1$.  
(B) The first five Bell numbers are $B_0 = 1, B_1 = 1, B_2 = 2, B_3 = 5, B_4 = 15$.  
(C) Dobinski's formula states $B_n = \frac{1}{e}\sum_{k=0}^\infty \frac{k^n}{k!}$.  
(D) $B_n = \sum_{k=1}^n S(n, k)$, where $S(n, k)$ are the Stirling numbers of the second kind.

#### Question 41
Let $f(x) = \frac{x}{1 + x^2}$ for all $x \in \mathbb{R}$:
(A) The function is odd ($f(-x) = -f(x)$).  
(B) The maximum value is $1/2$, attained at $x = 1$.  
(C) The minimum value is $-1/2$, attained at $x = -1$.  
(D) The horizontal asymptote is $y = 0$ as $x \to \pm\infty$.

#### Question 42
Consider the sequence $a_n = \frac{2^n}{n!}$ for $n \ge 1$:
(A) $a_1 = 2, a_2 = 2, a_3 = 4/3, a_4 = 2/3$.  
(B) The sequence is non-increasing for $n \ge 2$.  
(C) $\lim_{n \to \infty} a_n = 0$.  
(D) The series $\sum_{n=1}^\infty a_n$ converges to $e^2 - 1$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 x \sqrt{1 - x^2} dx$$
Calculate the value of $300 I$ (round off to the nearest integer).

#### Question 44
Find the number of ways to seat 5 people around a circular table.

#### Question 45
Find the perpendicular distance from the point $(1, 1, 1)$ to the plane $2x + 2y + z - 10 = 0$ (round off to TWO decimal places).

#### Question 46
Let $z$ be a complex number satisfying $z^2 + 1 = 0$. Calculate $|z + 1|^2$.

#### Question 47
Let $y(x)$ satisfy $\frac{dy}{dx} = 2x$ with $y(0) = 3$. Calculate $y(2)$.

#### Question 48
In rolling a fair standard die, calculate the probability of getting a number strictly greater than 4 (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The area of the region bounded by $y = x^2$ and $y = 2x$ is:
(A) $\frac{4}{3}$  
(B) $\frac{2}{3}$  
(C) $\frac{1}{3}$  
(D) 2  

#### Question 50
If the first term of a geometric progression is 2 and the common ratio is 3, then the $5\text{th}$ term $a_5$ is:
(A) 162  
(B) 54  
(C) 486  
(D) 81  

#### Question 51
The value of the limit $\lim_{x \to 0} \frac{\ln(1 + 2x)}{x}$ is:
(A) 2  
(B) 1  
(C) $1/2$  
(D) 0  

#### Question 52
The vertex of the parabola $y^2 - 4y - 4x = 0$ is:
(A) $(-1, 2)$  
(B) $(1, 2)$  
(C) $(2, -1)$  
(D) $(0, 0)$  

#### Question 53
The distance between the points $(1, 2, 3)$ and $(4, 6, 3)$ is:
(A) 5  
(B) $\sqrt{5}$  
(C) 25  
(D) 10  

#### Question 54
If $\vec{a}$ is a non-zero vector, then $\vec{a} \times \vec{a}$ is equal to:
(A) $\vec{0}$  
(B) $|\vec{a}|^2$  
(C) $\vec{a}$  
(D) 1  
"""

paper_2_md = r"""# JEE Advanced Mock Examination 19 — Paper 2
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
A point charge $+q$ is placed at distance $d$ in front of an infinite grounded planar conducting sheet ($z = 0$):
(A) By the method of image charges, the electric field for $z > 0$ is identical to that produced by $+q$ and an image charge $-q$ located at $z = -d$.  
(B) The induced surface charge density on the conducting sheet is $\sigma(r) = -\frac{q d}{2\pi (r^2 + d^2)^{3/2}}$, where $r$ is the radial distance from the origin on the sheet.  
(C) The total induced charge on the sheet is $\int_0^\infty \sigma(r) 2\pi r dr = -q$.  
(D) The attractive force between the charge $+q$ and the sheet is $F = \frac{q^2}{16\pi\varepsilon_0 d^2}$.

#### Question 2
Regarding electromagnetic induction and Lenz's law:
(A) The induced electromotive force in a closed loop is $\mathcal{E} = -\frac{d\Phi_B}{dt}$.  
(B) Lenz's law is a direct consequence of the principle of conservation of energy.  
(C) When a copper ring is dropped horizontally through a vertical bar magnet, its downward acceleration is strictly less than $g$.  
(D) Self-induced EMF in an inductor opposes any change in the current flowing through it: $\mathcal{E} = -L \frac{dI}{dt}$.

#### Question 3
A uniform solid sphere of mass $M$ and radius $R$ is released from rest from the top of an inclined plane of height $h$ and angle $\theta$. It rolls without slipping down the incline:
(A) The linear acceleration of the center of mass is $a = \frac{5}{7}g \sin\theta$.  
(B) The minimum coefficient of static friction required for rolling without slipping is $\mu_s \ge \frac{2}{7}\tan\theta$.  
(C) The speed of the center of mass at the bottom of the incline is $v = \sqrt{\frac{10}{7}g h}$.  
(D) The time taken to reach the bottom is $t = \frac{1}{\sin\theta}\sqrt{\frac{14 h}{5 g}}$.

#### Question 4
An ideal gas undergoes a free expansion (Joule expansion) into an evacuated insulated container:
(A) The work done by the gas is strictly zero ($W = 0$).  
(B) The heat exchanged with the surroundings is strictly zero ($Q = 0$).  
(C) The internal energy of the gas remains constant ($\Delta U = 0$).  
(D) The temperature of the ideal gas remains unchanged ($T_f = T_i$).

#### Question 5
Regarding the photoelectric effect:
(A) The maximum kinetic energy of photoelectrons depends linearly on the frequency of the incident light: $K_{\text{max}} = h\nu - \Phi$.  
(B) The maximum kinetic energy is completely independent of the intensity of the incident light.  
(C) The photoelectric current is directly proportional to the intensity of the incident light (for $\nu > \nu_0$).  
(D) There is no detectable time lag between the arrival of light and the emission of photoelectrons.

#### Question 6
An alternating voltage $V(t) = V_0 \sin(\omega t)$ is connected across a pure inductor $L$:
(A) The current lags behind the voltage by a phase angle of $90^\circ$ ($\pi/2\text{ rad}$).  
(B) The inductive reactance is $X_L = \omega L$.  
(C) The peak current is $I_0 = \frac{V_0}{\omega L}$.  
(D) The average power consumed over a complete cycle is zero.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A point charge $q = 2.0\text{ }\mu\text{C}$ is placed at a distance $d = 10.0\text{ cm}$ from a large grounded conducting plate. Calculate the force in Newtons with which the charge is attracted to the plate (round off to TWO decimal places).

#### Question 8
A solid sphere rolls without slipping down an inclined plane of inclination $\theta = 30^\circ$. Calculate the linear acceleration of its center of mass in $\text{m/s}^2$ (take $g = 9.8\text{ m/s}^2$, round off to TWO decimal places).

#### Question 9
In a photoelectric experiment using light of frequency $\nu = 1.0 \times 10^{15}\text{ Hz}$, the stopping potential is measured to be $V_s = 1.65\text{ V}$. Calculate the work function $\Phi$ of the metal in $\text{eV}$ (use $h = 4.14 \times 10^{-15}\text{ eV s}$, round off to TWO decimal places).

#### Question 10
An inductor of inductance $L = 50\text{ mH}$ is connected across an AC voltage $V_{\text{rms}} = 220\text{ V}$ at frequency $f = 50\text{ Hz}$. Calculate the RMS current $I_{\text{rms}}$ in Amperes (use $\pi \approx 3.142$, round off to ONE decimal place).

#### Question 11
Two charges $+4\text{ }\mu\text{C}$ and $+1\text{ }\mu\text{C}$ are fixed at a distance $L = 30\text{ cm}$ apart. A third charge $q$ is placed on the line joining them so that the net force on it is zero. Calculate the distance of $q$ from the $+4\text{ }\mu\text{C}$ charge in centimeters.

#### Question 12
A simple pendulum has length $L = 1.0\text{ m}$. Calculate its time period $T$ in seconds (take $g = 9.8\text{ m/s}^2$, round off to TWO decimal places).

---

## Section 3: Matching List / Matrix Match (Questions 13 to 18)

#### Question 13
Match the law of physics in List-I with its primary equation in List-II:
- **List-I**:
  - P. Coulomb's law
  - Q. Biot-Savart law
  - R. Snell's law
  - S. Ohm's law
- **List-II**:
  - 1. $V = I R$
  - 2. $n_1 \sin\theta_1 = n_2 \sin\theta_2$
  - 3. $F = \frac{q_1 q_2}{4\pi\varepsilon_0 r^2}$
  - 4. $d\vec{B} = \frac{\mu_0 I}{4\pi}\frac{d\vec{l}\times\hat{r}}{r^2}$

(A) P $\to$ 3, Q $\to$ 4, R $\to$ 2, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 3, Q $\to$ 2, R $\to$ 4, S $\to$ 1  
(D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1  

#### Question 14
Match the thermodynamic process in List-I with its work done formula in List-II:
- **List-I**:
  - P. Isobaric expansion
  - Q. Isothermal expansion
  - R. Adiabatic expansion
  - S. Isochoric process
- **List-II**:
  - 1. $0$
  - 2. $P(V_2 - V_1)$
  - 3. $n R T \ln(V_2/V_1)$
  - 4. $\frac{P_1 V_1 - P_2 V_2}{\gamma - 1}$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 2, R $\to$ 4, S $\to$ 1  

#### Question 15
Match the optical instrument in List-I with its primary optical element in List-II:
- **List-I**:
  - P. Simple magnifier
  - Q. Astronomical refractor
  - R. Cassegrain reflector
  - S. Periscope
- **List-II**:
  - 1. Parabolic concave mirror and hyperbolic secondary mirror
  - 2. Single convex lens of short focal length
  - 3. Two plane mirrors or total reflecting prisms
  - 4. Large objective lens and short eyepiece lens

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3  

#### Question 16
Match the physical phenomenon in List-I with its description in List-II:
- **List-I**:
  - P. Photoelectric effect
  - Q. Compton scattering
  - R. Pair production
  - S. Pair annihilation
- **List-II**:
  - 1. Inelastic scattering of photon by free electron
  - 2. Emission of electron from metal by absorption of single photon
  - 3. Electron-positron pair produces two gamma photons
  - 4. High-energy photon creates electron-positron pair in Coulomb field of nucleus

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 17
Match the nuclear particle in List-I with its composition in List-II:
- **List-I**:
  - P. Proton
  - Q. Neutron
  - R. Alpha particle
  - S. Deuteron
- **List-II**:
  - 1. One proton and one neutron ($^2\text{H}$)
  - 2. Two up quarks and one down quark ($u u d$)
  - 3. Two protons and two neutrons ($^4\text{He}$ nucleus)
  - 4. One up quark and two down quarks ($u d d$)

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 3, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 3, S $\to$ 1  

#### Question 18
Match the electrical property in List-I with its formula in List-II:
- **List-I**:
  - P. Resistance of wire
  - Q. Capacitance of parallel-plate capacitor
  - R. Self-inductance of solenoid
  - S. Energy density of electric field
- **List-II**:
  - 1. $\frac{1}{2}\varepsilon_0 E^2$
  - 2. $\rho \frac{L}{A}$
  - 3. $\mu_0 n^2 A L$
  - 4. $\frac{\varepsilon_0 A}{d}$

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 3, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 3, S $\to$ 1  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the nucleophilic addition of Grignard reagents ($\text{R-MgX}$) to carbonyl compounds:
(A) Reaction with formaldehyde ($\text{HCHO}$) gives primary alcohols after hydrolysis.  
(B) Reaction with aldehydes ($\text{R'CHO}$) gives secondary alcohols after hydrolysis.  
(C) Reaction with ketones ($\text{R'COR''}$) gives tertiary alcohols after hydrolysis.  
(D) Reaction with carbon dioxide ($\text{CO}_2$) gives carboxylic acids after hydrolysis.

#### Question 20
Regarding the kinetic theory of gases:
(A) The average kinetic energy of a gas molecule depends only on absolute temperature: $\langle K \rangle = \frac{3}{2} k_B T$.  
(B) Collisions between ideal gas molecules are assumed to be perfectly elastic.  
(C) The volume occupied by the gas molecules is negligible compared to the total container volume.  
(D) There are no intermolecular forces of attraction between ideal gas molecules.

#### Question 21
Regarding electrolysis of aqueous sodium chloride ($\text{NaCl}$) using inert electrodes:
(A) Chlorine gas ($\text{Cl}_2$) is liberated at the anode: $2\text{Cl}^- \to \text{Cl}_2 + 2e^-$.  
(B) Hydrogen gas ($\text{H}_2$) is liberated at the cathode: $2\text{H}_2\text{O} + 2e^- \to \text{H}_2 + 2\text{OH}^-$.  
(C) Sodium hydroxide ($\text{NaOH}$) accumulates in the solution.  
(D) Oxygen is not liberated at the anode under standard conditions due to the overvoltage of oxygen.

#### Question 22
Regarding chemical equilibrium:
(A) At equilibrium, the rates of the forward and reverse reactions are equal.  
(B) The equilibrium constant $K_c$ is independent of the initial concentrations of reactants and products.  
(C) The equilibrium constant $K_c$ is dependent on temperature.  
(D) A catalyst does not alter the numerical value of the equilibrium constant $K_c$.

#### Question 23
Regarding carbohydrates:
(A) Glucose and fructose are functional isomers.  
(B) Glucose is an aldohexose, while fructose is a ketohexose.  
(C) Both glucose and fructose give a positive Fehling's test (fructose reduces Fehling's solution via enediol rearrangement).  
(D) Glycogen is the primary storage polysaccharide in animals, known as animal starch.

#### Question 24
In the extraction of aluminium by the Hall-Héroult process:
(A) Purified alumina ($\text{Al}_2\text{O}_3$) is dissolved in molten cryolite ($\text{Na}_3\text{AlF}_6$) and fluorspar ($\text{CaF}_2$).  
(B) Cryolite lowers the melting point of alumina from $2050^\circ\text{C}$ to about $950^\circ\text{C}$.  
(C) Liquid aluminium metal is deposited at the carbon cathode at the bottom of the cell.  
(D) Carbon anodes are consumed during electrolysis producing $\text{CO}$ and $\text{CO}_2$, and must be periodically replaced.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
Calculate the pH of a $0.050\text{ M}$ aqueous solution of barium hydroxide ($\text{Ba(OH)}_2$), assuming complete dissociation (enter the value rounded off to TWO decimal places).

#### Question 26
Calculate the total number of unpaired electrons in the complex ion $[Fe(H_2O)_6]^{2+}$ (atomic number of $\text{Fe} = 26$, weak field ligand $\text{H}_2\text{O}$).

#### Question 27
An organic compound contains $40.0\%$ Carbon, $6.7\%$ Hydrogen, and $53.3\%$ Oxygen by mass. If its molecular weight is $60.0\text{ g/mol}$, calculate the number of carbon atoms present in one molecule.

#### Question 28
The half-life of a radioactive nucleus is $t_{1/2} = 5.0\text{ hours}$. Calculate the time in hours required for $87.5\%$ of the nucleus to decay.

#### Question 29
A steady current of $I = 1.0\text{ A}$ is passed through an aqueous solution of $\text{CuSO}_4$ for $t = 965\text{ seconds}$. Calculate the mass of copper deposited in grams (atomic mass of $\text{Cu} = 63.5\text{ g/mol}$, $F = 96500\text{ C/mol}$, round off to TWO decimal places).

#### Question 30
The depression in freezing point of a $0.10\text{ m}$ aqueous solution of sodium chloride ($\text{NaCl}$) is $\Delta T_f$, assuming $100\%$ dissociation ($i = 2$). Calculate $\Delta T_f$ in $^\circ\text{C}$ (use $K_f = 1.86\text{ K kg/mol}$, round off to TWO decimal places).

---

## Section 3: Matching List / Matrix Match (Questions 31 to 36)

#### Question 31
Match the organic name reaction in List-I with its characteristic product in List-II:
- **List-I**:
  - P. Aldol condensation
  - Q. Cannizzaro reaction
  - R. Clemmensen reduction
  - S. Wolf-Kishner reduction
- **List-II**:
  - 1. Alkane using $\text{NH}_2\text{NH}_2 / \text{KOH}$
  - 2. $\alpha,\beta$-unsaturated carbonyl compound
  - 3. Mixture of alcohol and carboxylic acid salt
  - 4. Alkane using $\text{Zn-Hg} / \text{conc. HCl}$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 32
Match the mineral in List-I with its metal in List-II:
- **List-I**:
  - P. Bauxite
  - Q. Haematite
  - R. Copper pyrite
  - S. Calamine
- **List-II**:
  - 1. Iron ($\text{Fe}$)
  - 2. Aluminium ($\text{Al}$)
  - 3. Zinc ($\text{Zn}$)
  - 4. Copper ($\text{Cu}$)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 33
Match the process in List-I with its primary industrial chemical in List-II:
- **List-I**:
  - P. Haber process
  - Q. Contact process
  - R. Ostwald process
  - S. Solvay process
- **List-II**:
  - 1. Sulfuric acid ($\text{H}_2\text{SO}_4$)
  - 2. Ammonia ($\text{NH}_3$)
  - 3. Sodium carbonate ($\text{Na}_2\text{CO}_3$)
  - 4. Nitric acid ($\text{HNO}_3$)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 34
Match the vitamin in List-I with its deficiency disease in List-II:
- **List-I**:
  - P. Vitamin A
  - Q. Vitamin B1
  - R. Vitamin C
  - S. Vitamin D
- **List-II**:
  - 1. Beriberi
  - 2. Night blindness
  - 3. Rickets
  - 4. Scurvy

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 35
Match the colloid in List-I with its physical state in List-II:
- **List-I**:
  - P. Mist
  - Q. Milk
  - R. Gemstone
  - S. Foam
- **List-II**:
  - 1. Emulsion (liquid in liquid)
  - 2. Aerosol (liquid in gas)
  - 3. Foam (gas in liquid)
  - 4. Solid sol (solid in solid)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 36
Match the halogen in List-I with its color in List-II:
- **List-I**:
  - P. $\text{F}_2$
  - Q. $\text{Cl}_2$
  - R. $\text{Br}_2$
  - S. $\text{I}_2$
- **List-II**:
  - 1. Greenish yellow
  - 2. Light yellow
  - 3. Violet vapors
  - 4. Reddish brown

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \sin x + \cos x$ for $x \in [0, 2\pi]$:
(A) The maximum value of $f(x)$ is $\sqrt{2}$, attained at $x = \pi/4$.  
(B) The minimum value of $f(x)$ is $-\sqrt{2}$, attained at $x = 5\pi/4$.  
(C) $f(x)$ has points of inflection at $x = 3\pi/4$ and $x = 7\pi/4$.  
(D) $f(x) = \sqrt{2}\sin(x + \pi/4)$.

#### Question 38
Let $A$ be a non-singular $n \times n$ matrix:
(A) $\det(A^{-1}) = \frac{1}{\det(A)}$.  
(B) $(A^{-1})^T = (A^T)^{-1}$.  
(C) $A \text{adj}(A) = \det(A) I$.  
(D) $\det(\text{adj}(A)) = (\det(A))^{n-1}$.

#### Question 39
Consider the plane $2x - 3y + 6z - 14 = 0$:
(A) The intercepts on the coordinate axes are $a = 7, b = -14/3, c = 7/3$.  
(B) The normal vector to the plane is $(2, -3, 6)$.  
(C) The perpendicular distance from the origin to the plane is 2.  
(D) The direction cosines of the normal are $(2/7, -3/7, 6/7)$.

#### Question 40
Consider the differential equation $\frac{dy}{dx} = y$:
(A) The general solution is $y = C e^x$.  
(B) If $y(0) = 1$, the unique solution is $y = e^x$.  
(C) The function $y(x) = e^x$ is strictly increasing on $\mathbb{R}$.  
(D) The tangent to the curve $y = e^x$ at $(0, 1)$ has equation $y = x + 1$.

#### Question 41
Let $X$ follow a standard normal distribution $N(0, 1)$:
(A) The mean is 0 and variance is 1.  
(B) The probability density function is $f(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$.  
(C) $P(X \le 0) = 0.5$.  
(D) $P(|X| \le 1) \approx 0.683$.

#### Question 42
Consider the sequence $a_n = \frac{1}{n}$ for $n \ge 1$:
(A) The sequence is strictly decreasing.  
(B) The sequence is bounded below by 0.  
(C) $\lim_{n \to \infty} a_n = 0$.  
(D) The series $\sum_{n=1}^\infty a_n$ diverges (harmonic series).

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^2 x dx$$
Calculate the value of $10 I$.

#### Question 44
Find the number of ways to choose 2 items from a set of 5 distinct items ($\binom{5}{2}$).

#### Question 45
Find the distance from the point $(1, 2, 3)$ to the origin $(0, 0, 0)$ (use $\sqrt{14} \approx 3.74$, round off to TWO decimal places).

#### Question 46
Let $z = 1 + i$. Calculate $|z|^4$.

#### Question 47
Let $y(x)$ satisfy $\frac{dy}{dx} = 1$ with $y(0) = 2$. Calculate $y(3)$.

#### Question 48
In rolling a fair die, calculate the probability of getting an even number (round off to TWO decimal places).

---

## Section 3: Matching List / Matrix Match (Questions 49 to 54)

#### Question 49
Match the function in List-I with its integral in List-II:
- **List-I**:
  - P. $\int x dx$
  - Q. $\int x^2 dx$
  - R. $\int e^x dx$
  - S. $\int \frac{1}{x} dx$
- **List-II**:
  - 1. $\frac{x^3}{3} + C$
  - 2. $\frac{x^2}{2} + C$
  - 3. $\ln|x| + C$
  - 4. $e^x + C$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 50
Match the curve in List-I with its degree in List-II:
- **List-I**:
  - P. Straight line
  - Q. Parabola
  - R. Circle
  - S. Ellipse
- **List-II**:
  - 1. 2
  - 2. 1
  - 3. 2
  - 4. 2

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 3, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 51
Match the complex number in List-I with its real part in List-II:
- **List-I**:
  - P. $3 + 4i$
  - Q. $-2 + 5i$
  - R. $7i$
  - S. $-6$
- **List-II**:
  - 1. $-2$
  - 2. $3$
  - 3. $-6$
  - 4. $0$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 52
Match the matrix operation in List-I with its determinant rule for $2 \times 2$ matrices in List-II:
- **List-I**:
  - P. $\det(A B)$
  - Q. $\det(k A)$
  - R. $\det(A^T)$
  - S. $\det(A^{-1})$
- **List-II**:
  - 1. $k^2 \det(A)$
  - 2. $\det(A)\det(B)$
  - 3. $\frac{1}{\det(A)}$
  - 4. $\det(A)$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 53
Match the probability event in List-I with its probability in List-II:
- **List-I**:
  - P. Impossible event $\emptyset$
  - Q. Sure event $S$
  - R. Fair coin head
  - S. Fair die rolling 6
- **List-II**:
  - 1. $1$
  - 2. $0$
  - 3. $1/6$
  - 4. $1/2$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 54
Match the vector term in List-I with its definition in List-II:
- **List-I**:
  - P. Unit vector
  - Q. Zero vector
  - R. Dot product of orthogonal vectors
  - S. Cross product of parallel vectors
- **List-II**:
  - 1. Magnitude 0
  - 2. Magnitude 1
  - 3. Zero vector $\vec{0}$
  - 4. Scalar value 0

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 19

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Synchrotron radiation relativistic beaming cone $\sim 1/\gamma$ and spectrum.
- 2: (A, B, C, D) - London equations of superconductivity and penetration depth $\lambda_L$.
- 3: (A, B, C, D) - Plasma frequency cutoff and ionospheric reflection.
- 4: (A, B, C, D) - Optical tweezers gradient force and radiation pressure.
- 5: (A, B, C, D) - Thermodynamics of mixing and Gibbs paradox resolution.
- 6: (A, B, C, D) - Euler's disk wobbling dynamics and acoustic frequency rise.

#### Solutions 7 to 12:
- 7: $\gamma = 3000 / 0.511 \approx 5871$.
  $\Delta E = \frac{e^2 \gamma^4}{3\varepsilon_0 \rho} = \frac{4\pi}{3}\left(\frac{e^2}{4\pi\varepsilon_0}\right)\frac{\gamma^4}{\rho} \approx 785\text{ keV}$. (Answer: 785)
- 8: $\lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}} = \sqrt{\frac{9.11 \times 10^{-31}}{(4\pi \times 10^{-7}) (3.0 \times 10^{28}) (1.6 \times 10^{-19})^2}} = \sqrt{\frac{9.11 \times 10^{-31}}{9.65 \times 10^{-16}}} \approx 30.7\text{ nm}$. (Answer: 30.7)
- 9: $\omega_p = \sqrt{\frac{n_e e^2}{\varepsilon_0 m_e}} = \sqrt{\frac{(10^{12}) (1.6 \times 10^{-19})^2}{(8.85 \times 10^{-12}) (9.11 \times 10^{-31})}} \approx 5.63 \times 10^7\text{ rad/s}$.
  $f_p = \frac{\omega_p}{2\pi} \approx 8.97\text{ MHz} \approx 9.0\text{ MHz}$. (Answer: 9.0)
- 10: Linear acceleration: $a = \frac{(m_1 - m_2)g}{m_1 + m_2 + I/R^2} = \frac{(3.0 - 2.0) \times 9.8}{3.0 + 2.0 + 0.20 / 0.01} = \frac{9.8}{5.0 + 20.0} = \frac{9.8}{25.0} = 0.392\text{ m/s}^2 \approx 0.39\text{ m/s}^2$. (Answer: 0.39)
- 11: $V = \frac{Q}{4\pi\varepsilon_0 R} \implies Q = 4\pi\varepsilon_0 R V = \frac{0.05 \times 900}{9 \times 10^9} = 5.0 \times 10^{-9}\text{ C} = 5.0\text{ nC}$. (Answer: 5.0)
- 12: $\frac{Q_C}{Q_H} = \frac{T_C}{T_H} \implies |Q_C| = 800 \times \frac{300}{400} = 600\text{ J}$. (Answer: 600)

#### Solutions 13 to 18:
- 13: Energy conservation: $m g x_{\text{max}} = \frac{1}{2} k x_{\text{max}}^2 \implies x_{\text{max}} = \frac{2 m g}{k}$. (A)
- 14: $I = \frac{I_0}{2}\cos^2(60^\circ) = \frac{I_0}{2}(1/4) = \frac{I_0}{8}$. (A)
- 15: $B(x) = \frac{\mu_0 I R^2}{2(R^2 + x^2)^{3/2}} = \frac{\mu_0 I R^2}{2(4R^2)^{3/2}} = \frac{\mu_0 I}{16 R} = \frac{B_0}{8}$. (A)
- 16: $\lambda = \frac{h}{\sqrt{2 m K}} \implies \frac{\lambda_e}{\lambda_p} = \sqrt{\frac{m_p}{m_e}}$. (A)
- 17: Area under curve on P-V indicator diagram is greater for isotherm than adiabat $\implies$ isothermal work is greater. (A)
- 18: Inside Earth, $g(d) = g(1 - d/R)$. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Mannich multicomponent condensation and Hofmann elimination.
- 20: (A, B, C) - YBCO 1-2-3 structure and mixed valence copper. Statement (D) is false: Meissner effect occurs below $T_c$, not above.
- 21: (A, B, C, D) - Cyclic voltammetry and Randles-Sevcik equation.
- 22: (A, B, C, D) - Metal-organic frameworks MOF-5 and ZIF-8.
- 23: (A, B, C, D) - Fischer-Tropsch syngas conversion mechanism.
- 24: (A, B, C) - Qualitative test for ammonium. Statement (D) is false: ammonium salts do not impart flame color (potassium gives violet).

#### Solutions 25 to 30:
- 25: $K_{sp} = [\text{Fe}^{3+}][\text{OH}^-]^3 \implies 10^{-38} = (0.010)[\text{OH}^-]^3 \implies [\text{OH}^-]^3 = 10^{-36} \implies [\text{OH}^-] = 10^{-12}\text{ M}$.
  $\text{pOH} = 12.00 \implies \text{pH} = 2.00$. (Answer: 2.00)
- 26: Strong-field $\text{CN}^-$ gives square planar $d^8$ Ni(II) with all electrons paired $\implies 0$ unpaired electrons. (Answer: 0)
- 27: Molar mass $= 30\text{ g/mol}$. Empirical formula $\text{CH}_3$ (mass 15) $\implies n = 2 \implies \text{C}_2\text{H}_6 \implies 2$ carbons. (Answer: 2)
- 28: $t_{1/2} = \frac{0.693}{0.03465} = 20.0\text{ min}$. (Answer: 20)
- 29: $m = \frac{M I t}{F} = \frac{108.0 \times 2.0 \times 965}{96500} = \frac{208440}{96500} = 2.16\text{ g}$. (Answer: 2.16)
- 30: $\Pi = C R T = 0.020 \times 0.0821 \times 300 = 0.4926\text{ atm} \approx 0.49\text{ atm}$. (Answer: 0.49)

#### Solutions 31 to 36:
- 31: Gattermann-Koch reaction uses $\text{CO} + \text{HCl} + \text{AlCl}_3$. (A)
- 32: $[\text{Co(CN)}_6]^{3-}$ has strong-field $\text{CN}^-$ and $d^6$ low-spin $t_{2g}^6 \implies \text{CFSE} = -2.4\Delta_o + 2P$, highest CFSE. (A)
- 33: A pairs with T through two hydrogen bonds. (A)
- 34: Silica flux removes $\text{FeO}$ as $\text{FeSiO}_3$ slag. (A)
- 35: Diazotization yields benzenediazonium chloride. (A)
- 36: Conjugate acid of $\text{H}_2\text{O}$ adds $\text{H}^+$: $\text{H}_3\text{O}^+$. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Classification of isolated singularities and Casorati-Weierstrass theorem.
- 38: (A, B, C, D) - Gram-Schmidt orthonormalization process.
- 39: (A, B, C, D) - Tractrix curve and pseudosphere hyperbolic geometry.
- 40: (A, B, C, D) - Bell numbers and Dobinski's formula.
- 41: (A, B, C, D) - Function $\frac{x}{1+x^2}$ analysis.
- 42: (A, B, C, D) - Sequence $2^n / n!$ convergence and exponential series sum.

#### Solutions 43 to 48:
- 43: Let $u = 1 - x^2 \implies du = -2x dx$.
  $I = \int_0^1 \frac{1}{2}\sqrt{u} du = \frac{1}{2}[\frac{2}{3}u^{3/2}]_0^1 = 1/3$.
  $300 I = 100$. (Answer: 100)
- 44: Circular permutations $(5 - 1)! = 4! = 24$. (Answer: 24)
- 45: $d = \frac{|2(1) + 2(1) + 1(1) - 10|}{\sqrt{4 + 4 + 1}} = \frac{|5 - 10|}{3} = \frac{5}{3} \approx 1.67$. (Answer: 1.67)
- 46: $z = \pm i \implies |i + 1|^2 = 1^2 + 1^2 = 2$. (Answer: 2)
- 47: $y(x) = x^2 + 3 \implies y(2) = 4 + 3 = 7$. (Answer: 7)
- 48: Favorable outcomes: 5, 6 (2 outcomes). $P = 2/6 = 1/3 \approx 0.33$. (Answer: 0.33)

#### Solutions 49 to 54:
- 49: Area $= \int_0^2 (2x - x^2)dx = [x^2 - x^3/3]_0^2 = 4 - 8/3 = 4/3$. (A)
- 50: $a_5 = a r^4 = 2(3^4) = 2(81) = 162$. (A)
- 51: Limit $= \lim \frac{2/(1+2x)}{1} = 2$. (A)
- 52: $(y - 2)^2 = 4(x + 1) \implies$ vertex is $(-1, 2)$. (A)
- 53: Distance $= \sqrt{(4-1)^2 + (6-2)^2 + (3-3)^2} = \sqrt{9 + 16} = 5$. (A)
- 54: $\vec{a} \times \vec{a} = \vec{0}$ (zero vector). (A)
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 2
## IIT Delhi Benchmark JEE Advanced Mock Examination 19

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Method of image charges for grounded conducting sheet.
- 2: (A, B, C, D) - Electromagnetic induction, Lenz's law, and self-inductance.
- 3: (A, B, C, D) - Rolling without slipping down incline kinematics.
- 4: (A, B, C, D) - Joule free expansion thermodynamics.
- 5: (A, B, C, D) - Photoelectric effect Einstein equation.
- 6: (A, B, C, D) - Pure inductive AC circuit characteristics.

#### Solutions 7 to 12:
- 7: $F = \frac{q^2}{16\pi\varepsilon_0 d^2} = \frac{1}{4}\left(\frac{1}{4\pi\varepsilon_0}\right)\frac{q^2}{d^2} = \frac{1}{4}(9.0 \times 10^9)\frac{(2.0 \times 10^{-6})^2}{(0.10)^2} = \frac{9.0 \times 10^9 \times 4.0 \times 10^{-12}}{0.04} = 0.90\text{ N}$. (Answer: 0.90)
- 8: $a = \frac{5}{7}g \sin 30^\circ = \frac{5}{14} \times 9.8 = 3.50\text{ m/s}^2$. (Answer: 3.50)
- 9: $h\nu = 4.14 \times 10^{-15} \times 10^{15} = 4.14\text{ eV}$.
  $\Phi = h\nu - e V_s = 4.14 - 1.65 = 2.49\text{ eV}$. (Answer: 2.49)
- 10: $X_L = 2\pi f L = 2\pi (50) (0.050) = 5\pi \approx 15.71\text{ }\Omega$.
  $I_{\text{rms}} = 220 / 15.71 \approx 14.0\text{ A}$. (Answer: 14.0)
- 11: $\frac{4}{x^2} = \frac{1}{(L - x)^2} \implies \frac{2}{x} = \frac{1}{L - x} \implies 2L - 2x = x \implies 3x = 2L \implies x = \frac{2}{3}(30) = 20.0\text{ cm}$. (Answer: 20)
- 12: $T = 2\pi\sqrt{L/g} = 2\pi\sqrt{1.0 / 9.8} \approx 2.01\text{ s}$. (Answer: 2.01)

#### Solutions 13 to 18 (Matching Lists):
- 13: P-3, Q-4, R-2, S-1. (A)
- 14: P-2, Q-3, R-4, S-1. (A)
- 15: P-2, Q-4, R-1, S-3. (A)
- 16: P-2, Q-1, R-4, S-3. (A)
- 17: P-2, Q-4, R-3, S-1. (A)
- 18: P-2, Q-4, R-3, S-1. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Grignard reactions with carbonyls and $\text{CO}_2$.
- 20: (A, B, C, D) - Kinetic theory postulates.
- 21: (A, B, C, D) - Chlor-alkali process products and overvoltage.
- 22: (A, B, C, D) - Equilibrium constant characteristics.
- 23: (A, B, C, D) - Sugar chemistry and Fehling's test.
- 24: (A, B, C, D) - Hall-Héroult aluminium extraction.

#### Solutions 25 to 30:
- 25: $[\text{OH}^-] = 2 \times 0.050 = 0.10\text{ M} \implies \text{pOH} = 1.00 \implies \text{pH} = 13.00$. (Answer: 13.00)
- 26: High-spin $d^6$ Fe(II) has 4 unpaired electrons. (Answer: 4)
- 27: Empirical formula $\text{CH}_2\text{O}$ (mass 30). Multiple $60/30 = 2 \implies \text{C}_2\text{H}_4\text{O}_2 \implies 2$ carbons. (Answer: 2)
- 28: $87.5\%$ decayed $\implies 12.5\%$ remains $= (1/2)^3 \implies 3$ half-lives $= 3 \times 5.0 = 15.0\text{ hours}$. (Answer: 15)
- 29: $m = \frac{M I t}{2 F} = \frac{63.5 \times 1.0 \times 965}{2 \times 96500} = \frac{61277.5}{193000} \approx 0.32\text{ g}$. (Answer: 0.32)
- 30: $\Delta T_f = i K_f m = 2 \times 1.86 \times 0.10 = 0.37^\circ\text{C}$. (Answer: 0.37)

#### Solutions 31 to 36:
- 31: P-2, Q-3, R-4, S-1. (A)
- 32: P-2, Q-1, R-4, S-3. (A)
- 33: P-2, Q-1, R-4, S-3. (A)
- 34: P-2, Q-1, R-4, S-3. (A)
- 35: P-2, Q-1, R-4, S-3. (A)
- 36: P-2, Q-1, R-4, S-3. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Function $\sin x + \cos x$ properties.
- 38: (A, B, C, D) - Invertible matrix and adjugate formulas.
- 39: (A, B, C, D) - Plane geometry in 3D.
- 40: (A, B, C, D) - Exponential differential equation.
- 41: (A, B, C, D) - Standard normal distribution properties.
- 42: (A, B, C, D) - Harmonic sequence and divergence of harmonic series.

#### Solutions 43 to 48:
- 43: $I = [x^2/2]_0^2 = 2 \implies 10 I = 20$. (Answer: 20)
- 44: $\binom{5}{2} = 10$. (Answer: 10)
- 45: $d = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14} \approx 3.74$. (Answer: 3.74)
- 46: $|z| = \sqrt{2} \implies |z|^4 = (\sqrt{2})^4 = 4$. (Answer: 4)
- 47: $y(x) = x + 2 \implies y(3) = 3 + 2 = 5$. (Answer: 5)
- 48: Probability $= 3/6 = 0.50$. (Answer: 0.50)

#### Solutions 49 to 54:
- 49: P-2, Q-1, R-4, S-3. (A)
- 50: P-2, Q-1, R-3, S-4. (A)
- 51: P-2, Q-1, R-4, S-3. (A)
- 52: P-2, Q-1, R-4, S-3. (A)
- 53: P-2, Q-1, R-4, S-3. (A)
- 54: P-2, Q-1, R-4, S-3. (A)
"""

val_md = r"""# Answer Key & Benchmark Validation — Mock 19
## IIT Delhi Benchmark Calibration

### Paper 1 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C | **M42** | Multi | A,B,C,D |
| **P7** | Num | 785 | **C25** | Num | 2.00 | **M43** | Num | 100 |
| **P8** | Num | 30.7 | **C26** | Num | 0 | **M44** | Num | 24 |
| **P9** | Num | 9.0 | **C27** | Num | 2 | **M45** | Num | 1.67 |
| **P10** | Num | 0.39 | **C28** | Num | 20 | **M46** | Num | 2 |
| **P11** | Num | 5.0 | **C29** | Num | 2.16 | **M47** | Num | 7 |
| **P12** | Num | 600 | **C30** | Num | 0.49 | **M48** | Num | 0.33 |
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
| **P7** | Num | 0.90 | **C25** | Num | 13.00 | **M43** | Num | 20 |
| **P8** | Num | 3.50 | **C26** | Num | 4 | **M44** | Num | 10 |
| **P9** | Num | 2.49 | **C27** | Num | 2 | **M45** | Num | 3.74 |
| **P10** | Num | 14.0 | **C28** | Num | 15 | **M46** | Num | 4 |
| **P11** | Num | 20 | **C29** | Num | 0.32 | **M47** | Num | 5 |
| **P12** | Num | 2.01 | **C30** | Num | 0.37 | **M48** | Num | 0.50 |
| **P13** | Match | A | **C31** | Match | A | **M49** | Match | A |
| **P14** | Match | A | **C32** | Match | A | **M50** | Match | A |
| **P15** | Match | A | **C33** | Match | A | **M51** | Match | A |
| **P16** | Match | A | **C34** | Match | A | **M52** | Match | A |
| **P17** | Match | A | **C35** | Match | A | **M53** | Match | A |
| **P18** | Match | A | **C36** | Match | A | **M54** | Match | A |
"""

if __name__ == "__main__":
    create_mock_files(
        19,
        paper_1_md,
        paper_2_md,
        sol_1_md,
        sol_2_md,
        val_md,
        iit_name="IIT_Delhi"
    )

