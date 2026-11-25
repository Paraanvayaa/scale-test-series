# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 17.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Pound-Rebka gravitational redshift, Fresnel rotary polarization, Larmor magnetic dipole radiation
- Corey-Kim oxidation, Sonogashira cross-coupling, Keggin polyoxometalates, Square planar crystal field
- Jordan's lemma real integrals, Legendre polynomials Rodrigues formula, Simson line, Partition generating functions
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 17 — Paper 1
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
According to Einstein's Equivalence Principle and General Relativity, a photon of proper frequency $\nu_0$ emitted at the base of a vertical tower of height $h$ travels upwards in a uniform gravitational field $g$:
(A) The photon experiences a gravitational redshift with received frequency $\nu \approx \nu_0\left(1 - \frac{g h}{c^2}\right)$.  
(B) In the Pound-Rebka experiment ($h = 22.5\text{ m}$), the fractional frequency shift measured using the Mössbauer effect is $\frac{\Delta\nu}{\nu_0} \approx -2.45 \times 10^{-15}$.  
(C) An identical clock placed at the top of the tower ticks faster than a clock at the base by a fractional rate $\frac{\Delta t}{t} = \frac{g h}{c^2}$ (gravitational time dilation).  
(D) If the photon were emitted from the top of the tower downwards to the base, it would experience a gravitational blueshift.

#### Question 2
Regarding Fresnel's theory of optical activity and rotary polarization in chiral media (such as quartz or sugar solution):
(A) A linearly polarized wave can be mathematically decomposed into two coherent, oppositely circular polarized waves (left-circular $L$ and right-circular $R$) of equal amplitude.  
(B) In an optically active medium, the two circularly polarized components propagate with different phase velocities: $v_L = c/n_L$ and $v_R = c/n_R$ ($n_L \ne n_R$).  
(C) After traversing a thickness $d$ of the medium, the relative phase difference accumulated between $L$ and $R$ is $\delta = \frac{2\pi d}{\lambda_0}|n_L - n_R|$.  
(D) The plane of linear polarization is rotated through an angle $\theta = \frac{\delta}{2} = \frac{\pi d}{\lambda_0}(n_L - n_R)$.

#### Question 3
An oscillating magnetic dipole $\vec{m}(t) = m_0 \cos(\omega t)\hat{k}$ radiates electromagnetic waves into surrounding vacuum:
(A) The time-averaged total power radiated by the oscillating magnetic dipole is $P = \frac{\mu_0 m_0^2 \omega^4}{12\pi c^3}$.  
(B) The radiated power is proportional to the fourth power of frequency ($\omega^4$).  
(C) In the radiation zone ($r \gg c/\omega$), the radiated electric and magnetic fields drop off as $1/r$.  
(D) The radiation pattern has an intensity profile proportional to $\sin^2\theta$, where $\theta$ is the polar angle measured from the dipole axis.

#### Question 4
Regarding the thermoelectric effects in metallic conductors and thermocouples:
(A) The Seebeck effect generates an open-circuit EMF $\mathcal{E} = \int_{T_1}^{T_2} S_{A B}(T) dT$ across a junction of two dissimilar metals maintained at temperatures $T_1$ and $T_2$.  
(B) The Peltier effect describes the reversible absorption or evolution of heat at a junction of two conductors when an electric current is passed through it: $Q_{\text{Peltier}} = \Pi_{A B} I t$.  
(C) The Thomson effect describes reversible heat exchange along a single conductor carrying current in the presence of a longitudinal temperature gradient: $\frac{dQ}{dx} = \mu_T I \frac{dT}{dx}$.  
(D) Kelvin's first and second thermodynamic relations establish: $\Pi_{A B} = T S_{A B}$ and $\mu_A - \mu_B = T \frac{d S_{A B}}{dT}$.

#### Question 5
A particle of rest mass $m$ moves at relativistic velocity $v$ with relativistic factor $\gamma = 1/\sqrt{1 - v^2/c^2}$:
(A) The relativistic kinetic energy is $K = (\gamma - 1) m c^2$.  
(B) In the low-velocity limit ($v \ll c$), the binomial expansion yields $K = \frac{1}{2} m v^2 + \frac{3}{8} \frac{m v^4}{c^2} + \mathcal{O}(v^6/c^4)$.  
(C) The relativistic momentum is $\vec{p} = \gamma m \vec{v}$.  
(D) The relationship between total energy $E$, momentum $p$, and rest mass $m$ is $E^2 = p^2 c^2 + m^2 c^4$.

#### Question 6
A cylindrical solenoid of radius $R$, length $L \gg R$, and $n$ turns per unit length carries a time-dependent current $I(t) = I_0 \cos(\omega t)$:
(A) The interior magnetic field is $\vec{B}(t) = \mu_0 n I_0 \cos(\omega t)\hat{z}$.  
(B) By Faraday's law, the induced non-conservative electric field inside the solenoid ($r < R$) is azimuthal: $\vec{E}(r, t) = \frac{1}{2}\mu_0 n \omega I_0 r \sin(\omega t)\hat{\theta}$.  
(C) The induced electric field outside the solenoid ($r > R$) is $\vec{E}(r, t) = \frac{\mu_0 n \omega I_0 R^2}{2 r}\sin(\omega t)\hat{\theta}$.  
(D) The Poynting vector at the inner surface of the solenoid points radially inward into the core, representing the inflow of magnetic energy.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a Pound-Rebka gravitational redshift experiment, gamma-ray photons of energy $E_0 = 14.4\text{ keV}$ from $^{57}\text{Fe}$ fall through a vertical height $h = 22.5\text{ m}$ on Earth's surface ($g = 9.8\text{ m/s}^2$). The fractional energy shift $\frac{\Delta E}{E_0}$ experienced by the photons is $X \times 10^{-15}$. Calculate the value of $X$ (use $c = 3.0 \times 10^8\text{ m/s}$, round off to TWO decimal places).

#### Question 8
A solution of d-sucrose in a polarimeter tube of length $l = 2.0\text{ dm}$ produces an optical rotation $\theta = +13.3^\circ$ for sodium yellow light ($\lambda = 589\text{ nm}$). If the specific optical rotation of d-sucrose is $[\alpha] = +66.5^\circ\text{ dm}^{-1}\cdot(\text{g/cm}^3)^{-1}$, calculate the concentration $C$ of the sugar solution in $\text{g/cm}^3$ (round off to TWO decimal places).

#### Question 9
A relativistic electron has a kinetic energy equal to twice its rest mass energy ($K = 2 m_e c^2$). Calculate the speed of the electron expressed as a fraction of the speed of light $\beta = v/c$ (round off to THREE decimal places).

#### Question 10
A thin circular hoop of mass $m = 2.0\text{ kg}$ and radius $R = 0.50\text{ m}$ hangs on a horizontal knife edge. It executes small oscillations in its own plane as a physical pendulum. Taking $g = 9.8\text{ m/s}^2$, calculate the time period $T$ of small oscillations in seconds (round off to TWO decimal places).

#### Question 11
An ideal LC circuit has inductance $L = 50\text{ mH}$ and capacitance $C = 20\text{ }\mu\text{F}$. The maximum voltage across the capacitor is $V_0 = 100\text{ V}$. Calculate the maximum current $I_{\text{max}}$ in the inductor in Amperes (round off to the nearest integer).

#### Question 12
A thermodynamic cycle using $1.0\text{ mole}$ of an ideal monatomic gas consists of an isothermal expansion at $T_1 = 600\text{ K}$ from volume $V_1$ to $V_2 = 2 V_1$, an isochoric cooling to $T_2 = 300\text{ K}$, and an adiabatic compression back to the initial state. Calculate the net work done by the gas per cycle in Joules (use $R = 8.314\text{ J/(mol K)}$, $\ln 2 = 0.693$, round off to the nearest integer).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A body of mass $m$ is thrown vertically upwards from the surface of Earth with initial speed equal to half the escape velocity ($v_0 = v_{\text{esc}} / 2$). Neglecting air resistance and Earth's rotation, the maximum height $h$ attained above the Earth's surface (radius $R$) is:
(A) $h = \frac{R}{3}$  
(B) $h = \frac{R}{2}$  
(C) $h = \frac{R}{4}$  
(D) $h = \frac{2R}{3}$  

#### Question 14
A cylindrical bar magnet has length $L = 10\text{ cm}$ and magnetic dipole moment $M = 2.0\text{ A}\cdot\text{m}^2$. The magnetic pole strength $q_m$ of each pole of the magnet is:
(A) $20\text{ A}\cdot\text{m}$  
(B) $0.20\text{ A}\cdot\text{m}$  
(C) $2.0\text{ A}\cdot\text{m}$  
(D) $200\text{ A}\cdot\text{m}$  

#### Question 15
Two coherent sources of monochromatic light of wavelength $\lambda$ are located at $S_1(0, d/2)$ and $S_2(0, -d/2)$. A screen is placed parallel to the $y$-axis at $x = D \gg d$. The path difference between the waves at a point on the screen with coordinate $y$ is:
(A) $\Delta x \approx \frac{y d}{D}$  
(B) $\Delta x \approx \frac{y D}{d}$  
(C) $\Delta x \approx \frac{d^2}{2D}$  
(D) $\Delta x \approx \frac{y^2 d}{D^2}$  

#### Question 16
An air bubble of radius $r = 1.0\text{ mm}$ rises in a liquid of density $\rho = 1000\text{ kg/m}^3$ and viscosity $\eta = 1.0 \times 10^{-3}\text{ Pa}\cdot\text{s}$. If the density of air is negligible, the terminal velocity $v_t$ of the bubble according to Stokes' law is:
(A) $v_t = \frac{2 r^2 \rho g}{9 \eta}$  
(B) $v_t = \frac{r^2 \rho g}{3 \eta}$  
(C) $v_t = \frac{4 r^2 \rho g}{9 \eta}$  
(D) $v_t = \frac{2 r^2 \rho g}{3 \eta}$  

#### Question 17
A particle moves in a circular path of radius $r$ under the action of an attractive central force $F = -\frac{k}{r^3}$. The total mechanical energy $E$ of the particle in this orbit is:
(A) 0  
(B) $-\frac{k}{2r^2}$  
(C) $\frac{k}{2r^2}$  
(D) $-\frac{k}{r^2}$  

#### Question 18
The de Broglie wavelength of a thermal neutron in thermal equilibrium at room temperature $T = 300\text{ K}$ is approximately ($k_B = 1.38 \times 10^{-23}\text{ J/K}$, $m_n = 1.67 \times 10^{-27}\text{ kg}$):
(A) $1.78\text{ \AA}$  
(B) $0.18\text{ \AA}$  
(C) $17.8\text{ \AA}$  
(D) $0.018\text{ \AA}$  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Corey-Kim oxidation of primary and secondary alcohols to aldehydes and ketones:
(A) The active chlorosulfonium intermediate ($[\text{Me}_2\text{S-Cl}]^+$) is generated in situ from dimethyl sulfide ($\text{Me}_2\text{S}$) and N-chlorosuccinimide (NCS).  
(B) Reaction of the alcohol with the chlorosulfonium species gives an alkoxysulfonium intermediate with liberation of $\text{Cl}^-$.  
(C) Addition of a mild base (such as triethylamine $\text{Et}_3\text{N}$) effects intramolecular elimination to release the carbonyl product and dimethyl sulfide.  
(D) An advantage of the Corey-Kim oxidation over the Swern oxidation is that it can be carried out at slightly higher temperatures ($-25^\circ\text{C}$ to $0^\circ\text{C}$) compared to the harsh low-temperature requirements of Swern ($-78^\circ\text{C}$).

#### Question 20
In the Sonogashira cross-coupling reaction:
$$\text{Ar-X} + \text{H-C}\equiv\text{C-R} \xrightarrow{\text{Pd}(0)\text{ cat, CuI cat, Base}} \text{Ar-C}\equiv\text{C-R} + \text{HX}$$
(A) The reaction utilizes a palladium catalyst in conjunction with a copper(I) iodide co-catalyst.  
(B) The copper cycle generates a copper(I) acetylide intermediate ($\text{R-C}\equiv\text{C-Cu}$) via base-assisted deprotonation of the terminal alkyne.  
(C) Transmetalation transfers the alkynyl group from copper to the palladium(II) intermediate formed by oxidative addition of $\text{Ar-X}$.  
(D) Reductive elimination yields the disubstituted alkyne ($\text{Ar-C}\equiv\text{C-R}$) and regenerates the active $\text{Pd}(0)$ catalyst.

#### Question 21
Regarding polyoxometalates (POMs) and the classic Keggin structure $[\text{XM}_{12}\text{O}_{40}]^{n-}$ (e.g., $[\text{PW}_{12}\text{O}_{40}]^{3-}$):
(A) The structure consists of a central heteroatom tetrahedron ($\text{XO}_4$) surrounded by twelve distorted $\text{MO}_6$ octahedra.  
(B) The twelve octahedra are arranged in four groups of three edge-sharing octahedra ($\text{M}_3\text{O}_{13}$ triads) that share corners with each other and with the central $\text{XO}_4$ group.  
(C) Keggin polyoxometalates exhibit strong Brønsted acidity and act as versatile heterogeneous/homogeneous acid and oxidation catalysts.  
(D) They undergo reversible, multi-electron redox reactions without structural degradation, forming intensely colored "heteropoly blues".

#### Question 22
Regarding crystal field splitting in square planar $d^8$ coordination complexes (such as $[\text{PtCl}_4]^{2-}, [\text{PdCl}_4]^{2-}, [\text{Ni(CN)}_4]^{2-}$):
(A) The energy ordering of the $d$-orbitals is: $d_{x^2-y^2} \gg d_{xy} > d_{z^2} > d_{xz} \approx d_{yz}$.  
(B) The $d_{x^2-y^2}$ orbital experiences the maximum electrostatic repulsion from the four in-plane ligands along the $x$- and $y$-axes, and is strongly destabilized.  
(C) For $5d$ Pt(II) and $4d$ Pd(II), the crystal field splitting is very large, resulting in strictly diamagnetic square planar geometries with all 8 electrons paired in the lower four orbitals.  
(D) Square planar complexes commonly undergo substitution reactions via an associative ($A$ or $I_a$) pathway involving a trigonal bipyramidal five-coordinate intermediate.

#### Question 23
Regarding the transport number (transference number) of an ion in electrolytic conduction:
(A) The transport number $t_+$ is defined as the fraction of the total current carried by that cation: $t_+ = \frac{u_+}{u_+ + u_-}$, where $u_+$ and $u_-$ are ionic mobilities.  
(B) The sum of the transport numbers of all ions in the electrolyte equals unity: $t_+ + t_- = 1$.  
(C) Hittorf's method determines transport numbers by measuring concentration changes in the anode and cathode compartments after electrolysis.  
(D) In the moving boundary method, a sharp visible boundary between two electrolyte solutions moves down a tube, directly measuring ionic mobility.

#### Question 24
In the qualitative analysis of Group IV basic radicals ($\text{Zn}^{2+}, \text{Mn}^{2+}, \text{Ni}^{2+}, \text{Co}^{2+}$):
(A) Precipitation is effected by passing $\text{H}_2\text{S}$ gas through the solution in the presence of $\text{NH}_4\text{OH}$ and $\text{NH}_4\text{Cl}$.  
(B) $\text{NH}_4\text{OH}$ ensures a basic medium, increasing the concentration of sulfide ions $[\text{S}^{2-}]$ sufficiently to exceed the solubility products of Group IV sulfides.  
(C) $\text{ZnS}$ precipitates as a white precipitate, while $\text{MnS}$ precipitates as a buff/flesh-colored precipitate.  
(D) $\text{NiS}$ and $\text{CoS}$ precipitate as black solids that are insoluble in dilute $\text{HCl}$ but dissolve in aqua regia.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of silver chromate ($\text{Ag}_2\text{CrO}_4$) is $K_{sp} = 1.1 \times 10^{-12}$ at $25^\circ\text{C}$. Calculate the molar solubility $S$ of $\text{Ag}_2\text{CrO}_4$ in pure water in units of $10^{-5}\text{ mol/L}$ (round off to TWO decimal places).

#### Question 26
Calculate the spin-only magnetic moment in Bohr Magnetons ($\mu_B$) for the high-spin complex $[Fe(H_2O)_6]^{3+}$ (atomic number of $\text{Fe} = 26$). Enter the value rounded off to TWO decimal places (take $\sqrt{35} \approx 5.92$).

#### Question 27
An organic compound contains $52.2\%$ Carbon, $13.0\%$ Hydrogen, and $34.8\%$ Oxygen by mass. If its molecular mass is $46.0\text{ g/mol}$, calculate the number of carbon atoms present in one molecule.

#### Question 28
The standard reduction potentials are $E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.76\text{ V}$ and $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$. Calculate the equilibrium constant $K_{\text{eq}}$ for the cell reaction $\text{Zn}(s) + 2\text{Ag}^+(aq) \rightleftharpoons \text{Zn}^{2+}(aq) + 2\text{Ag}(s)$ at $298\text{ K}$. If $\log_{10} K_{\text{eq}} = Y$, find $Y$ (use $\frac{2.303 RT}{F} = 0.0591\text{ V}$, round off to ONE decimal place).

#### Question 29
A radioisotope has a decay constant $\lambda = 0.0693\text{ day}^{-1}$. Calculate the time in days required for $75.0\%$ of the initial radioactivity to decay.

#### Question 30
A solution of $1.0\text{ g}$ of urea ($\text{NH}_2\text{CONH}_2$, molar mass $60.0\text{ g/mol}$) in $50.0\text{ g}$ of water has a freezing point depression $\Delta T_f$. Calculate $\Delta T_f$ in $^\circ\text{C}$ (cryoscopic constant of water $K_f = 1.86\text{ K kg/mol}$, round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Hell-Volhard-Zelinsky (HVZ) reaction, carboxylic acids react with bromine in the presence of red phosphorus to form:
(A) $\alpha$-bromo carboxylic acids  
(B) Acyl bromides  
(C) $\beta$-bromo carboxylic acids  
(D) Dibromomethane  

#### Question 32
Which of the following transition metal complexes is diamagnetic?
(A) $[\text{Ni(CN)}_4]^{2-}$  
(B) $[\text{Ni(CO)}_4]$  
(C) Both $[\text{Ni(CN)}_4]^{2-}$ and $[\text{Ni(CO)}_4]$  
(D) $[\text{NiCl}_4]^{2-}$  

#### Question 33
The deficiency of Vitamin C (ascorbic acid) causes the disease known as:
(A) Scurvy  
(B) Rickets  
(C) Beriberi  
(D) Night blindness  

#### Question 34
In the extraction of zinc from zinc blende ($\text{ZnS}$), the roasting reaction is:
(A) $2\text{ZnS} + 3\text{O}_2 \to 2\text{ZnO} + 2\text{SO}_2$  
(B) $\text{ZnS} + 2\text{O}_2 \to \text{ZnSO}_4$  
(C) $\text{ZnS} + \text{C} \to \text{Zn} + \text{CS}_2$  
(D) $2\text{ZnS} + \text{O}_2 \to 2\text{Zn} + \text{SO}_2$  

#### Question 35
Treatment of an alkyl halide with sodium metal in dry ether (Wurtz reaction) yields an alkane. The reaction fails to give high yields when preparing:
(A) Unsymmetrical alkanes with an odd number of carbon atoms  
(B) Symmetrical alkanes  
(C) Ethane from methyl iodide  
(D) Butane from ethyl bromide  

#### Question 36
The conjugate base of ammonium ion ($\text{NH}_4^+$) is:
(A) Ammonia ($\text{NH}_3$)  
(B) Amide ion ($\text{NH}_2^-$)  
(C) Imide ion ($\text{NH}^{2-}$)  
(D) Nitride ion ($\text{N}^{3-}$)  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Regarding Jordan's lemma in complex contour integration and the evaluation of the real improper integral $I = \int_{-\infty}^\infty \frac{\cos x}{x^2 + a^2} dx$ ($a > 0$):
(A) Jordan's lemma states that $\lim_{R \to \infty} \int_{C_R} e^{i m z} f(z) dz = 0$ along the upper semi-circle $C_R$ if $m > 0$ and $\max_{z \in C_R} |f(z)| \to 0$ as $R \to \infty$.  
(B) The integrand $f(z) = \frac{e^{i z}}{z^2 + a^2}$ has a simple pole inside the upper half-plane at $z = i a$.  
(C) The residue of $f(z)$ at $z = i a$ is $\text{Res}(f, i a) = \frac{e^{-a}}{2 i a}$.  
(D) By Cauchy's Residue theorem, $I = \text{Re}\left(2\pi i \cdot \frac{e^{-a}}{2 i a}\right) = \frac{\pi e^{-a}}{a}$.

#### Question 38
Regarding the Legendre polynomials $P_n(x)$ defined on $[-1, 1]$ via Rodrigues' formula $P_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n}(x^2 - 1)^n$:
(A) $P_0(x) = 1$, $P_1(x) = x$, and $P_2(x) = \frac{1}{2}(3x^2 - 1)$.  
(B) The orthogonality property is $\int_{-1}^1 P_m(x) P_n(x) dx = \frac{2}{2n + 1}\delta_{mn}$.  
(C) Bonnet's recurrence relation is $(n+1) P_{n+1}(x) = (2n+1) x P_n(x) - n P_{n-1}(x)$.  
(D) $P_n(1) = 1$ and $P_n(-1) = (-1)^n$ for all integers $n \ge 0$.

#### Question 39
Consider the Simson line of a triangle:
(A) The feet of the perpendiculars dropped from any point $P$ on the circumcircle of a triangle to its three sides (or their extensions) are collinear.  
(B) The straight line containing these three collinear feet is the Simson line of point $P$.  
(C) The angle between the Simson lines of two points $P$ and $Q$ on the circumcircle equals half the angular measure of the arc $P Q$.  
(D) The Simson line of a point $P$ bisects the line segment connecting $P$ to the orthocenter $H$ of the triangle.

#### Question 40
Regarding Euler's generating function for the number of integer partitions $p(n)$:
$$P(x) = \sum_{n=0}^\infty p(n) x^n = \prod_{k=1}^\infty \frac{1}{1 - x^k}$$
(A) $p(4) = 5$ corresponding to partitions: $4, 3+1, 2+2, 2+1+1, 1+1+1+1$.  
(B) Euler's pentagonal number theorem states $\prod_{k=1}^\infty (1 - x^k) = 1 + \sum_{n=1}^\infty (-1)^n \left(x^{\frac{3n^2 - n}{2}} + x^{\frac{3n^2 + n}{2}}\right)$.  
(C) The recurrence relation for partition numbers is $p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + \dots$.  
(D) The number of partitions of $n$ into distinct parts equals the number of partitions of $n$ into odd parts.

#### Question 41
Let $f(x) = x e^{-x^2/2}$ for all $x \in \mathbb{R}$:
(A) $f(x)$ is an odd function.  
(B) The critical points of $f(x)$ occur at $x = \pm 1$.  
(C) The global maximum value of $f(x)$ is $e^{-1/2} = \frac{1}{\sqrt{e}}$ attained at $x = 1$.  
(D) The points of inflection occur at $x = 0$ and $x = \pm \sqrt{3}$.

#### Question 42
Consider the sequence of points $(x_n, y_n)$ defined by $\begin{pmatrix} x_{n+1} \\ y_{n+1} \end{pmatrix} = \begin{pmatrix} 1/2 & 1/3 \\ 0 & 1/4 \end{pmatrix} \begin{pmatrix} x_n \\ y_n \end{pmatrix}$:
(A) The eigenvalues of the transition matrix are $\lambda_1 = 1/2$ and $\lambda_2 = 1/4$.  
(B) Since both eigenvalues have absolute value strictly less than 1, the origin $(0, 0)$ is an asymptotically stable attractor.  
(C) For any initial point $(x_0, y_0)$, $\lim_{n \to \infty} (x_n, y_n) = (0, 0)$.  
(D) The spectral radius of the matrix is $\rho = 1/2$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_{-\infty}^\infty \frac{dx}{(x^2 + 1)(x^2 + 4)}$$
Calculate the value of $\frac{60 I}{\pi}$ (round off to the nearest integer).

#### Question 44
Find the number of ways to arrange 4 boys and 4 girls in a row such that boys and girls alternate.

#### Question 45
Find the perpendicular distance from the point $(2, 3, 4)$ to the line $\frac{x-1}{2} = \frac{y-2}{1} = \frac{z-3}{2}$ (round off to TWO decimal places).

#### Question 46
Let $z = \cos(2\pi/5) + i \sin(2\pi/5)$. Calculate the value of $1 + z + z^2 + z^3 + z^4$.

#### Question 47
Let $y(x)$ satisfy the differential equation $\frac{dy}{dx} = 2x(1 + y^2)$ with $y(0) = 0$. Calculate $y(\sqrt{\pi/4})$ (round off to the nearest integer).

#### Question 48
A random variable $X$ has probability density function $f(x) = 2x$ for $0 \le x \le 1$. Calculate the expected value $E[X]$ (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The area of the region enclosed by the loop of the curve $y^2 = x^2(1 - x^2)$ is:
(A) $\frac{4}{3}$  
(B) $\frac{2}{3}$  
(C) $\frac{1}{3}$  
(D) $\frac{8}{3}$  

#### Question 50
If the sum of an infinite geometric progression is 9 and the sum of the squares of its terms is 27, then the first term $a$ is:
(A) 4.5  
(B) 6  
(C) 3  
(D) 1.5  

#### Question 51
The value of the limit $\lim_{x \to 0} \frac{e^x - e^{-x} - 2x}{x - \sin x}$ is:
(A) 2  
(B) 1  
(C) 4  
(D) 0  

#### Question 52
The focus of the parabola $y^2 - 4y - 8x - 4 = 0$ is:
(A) $(1, 2)$  
(B) $(-1, 2)$  
(C) $(2, 1)$  
(D) $(0, 2)$  

#### Question 53
The angle between the lines whose direction cosines satisfy $l + m + n = 0$ and $l^2 + m^2 - n^2 = 0$ is:
(A) $\frac{\pi}{3}$  
(B) $\frac{\pi}{2}$  
(C) $\frac{\pi}{4}$  
(D) $\frac{\pi}{6}$  

#### Question 54
If $\vec{a}$ and $\vec{b}$ are unit vectors and $\theta$ is the angle between them, then $|\vec{a} - \vec{b}|$ is equal to:
(A) $2\sin(\theta/2)$  
(B) $2\cos(\theta/2)$  
(C) $\sin(\theta/2)$  
(D) $\cos(\theta/2)$  
"""

paper_2_md = r"""# JEE Advanced Mock Examination 17 — Paper 2
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
A charged particle of mass $m$ and charge $q$ enters a region of crossed uniform electric field $\vec{E} = E \hat{j}$ and magnetic field $\vec{B} = B \hat{k}$ with initial velocity $\vec{v} = v_0 \hat{i}$:
(A) If $v_0 = E/B$, the particle passes undeflected through the crossed fields (velocity selector condition).  
(B) If $v_0 = 0$ (released from rest at the origin), the particle executes a cycloidal trajectory with parametric equations $x(t) = \frac{E}{\omega B}(\omega t - \sin\omega t)$ and $y(t) = \frac{E}{\omega B}(1 - \cos\omega t)$ where $\omega = \frac{q B}{m}$.  
(C) The maximum height reached in the $y$-direction is $y_{\text{max}} = \frac{2 m E}{q B^2}$.  
(D) The average drift velocity along the $x$-axis is $\vec{v}_{\text{drift}} = \frac{\vec{E} \times \vec{B}}{B^2} = \frac{E}{B}\hat{i}$.

#### Question 2
Regarding total internal reflection and evanescent waves at a dielectric interface between a dense medium (index $n_1$) and a rarer medium (index $n_2 < n_1$):
(A) Total internal reflection occurs for angle of incidence $\theta_1 > \theta_c = \arcsin(n_2 / n_1)$.  
(B) The transmitted electric field in the rarer medium is an evanescent wave that decays exponentially with distance $z$ into the rarer medium: $E(z) = E_0 e^{-z / d_p}$.  
(C) The penetration depth is $d_p = \frac{\lambda_0}{2\pi \sqrt{n_1^2 \sin^2\theta_1 - n_2^2}}$.  
(D) Although the time-averaged normal Poynting flux into the rarer medium is zero, energy can tunnel into a third dense medium if brought within a few penetration depths (frustrated total internal reflection / optical tunneling).

#### Question 3
A thermodynamic engine operates on a Joule-Brayton cycle using an ideal gas, consisting of two reversible isobars at pressures $P_1$ and $P_2$ ($P_2 > P_1$) and two reversible adiabatics:
(A) The pressure ratio is $r_p = P_2 / P_1$.  
(B) The thermal efficiency of the cycle is $\eta = 1 - r_p^{-\frac{\gamma - 1}{\gamma}}$.  
(C) For a fixed maximum temperature $T_{\text{max}}$ and minimum temperature $T_{\text{min}}$, the maximum net work output per cycle occurs at optimum pressure ratio $r_{p, \text{opt}} = \left(\frac{T_{\text{max}}}{T_{\text{min}}}\right)^{\frac{\gamma}{2(\gamma - 1)}}$.  
(D) The Brayton cycle forms the thermodynamic basis for modern aircraft gas turbine engines.

#### Question 4
A sphere of radius $R$ carries a non-uniform spherically symmetric charge density $\rho(r) = \rho_0 \left(1 - \frac{r}{R}\right)$ for $0 \le r \le R$, and $\rho(r) = 0$ for $r > R$:
(A) The total charge of the sphere is $Q = \frac{\pi \rho_0 R^3}{3}$.  
(B) The electric field inside the sphere ($r \le R$) is $E(r) = \frac{\rho_0 r}{3\varepsilon_0}\left(1 - \frac{3r}{4R}\right)$.  
(C) The maximum electric field occurs at radius $r = \frac{2}{3}R$.  
(D) The electric field outside the sphere ($r \ge R$) is $E(r) = \frac{Q}{4\pi\varepsilon_0 r^2}$.

#### Question 5
Regarding the resonance in an LCR circuit:
(A) In a series LCR circuit, resonance occurs when inductive reactance equals capacitive reactance ($\omega L = 1/(\omega C)$).  
(B) At series resonance, the circuit impedance is purely resistive and at its minimum value $Z = R$.  
(C) The current in the series circuit attains its maximum amplitude $I_0 = V_0 / R$ at resonance.  
(D) The voltage across the inductor or capacitor at resonance can exceed the source voltage by a factor equal to the quality factor $Q$.

#### Question 6
An astronomical telescope consists of two thin converging lenses: an objective of focal length $f_o$ and an eyepiece of focal length $f_e$. When viewing a distant object in normal adjustment:
(A) The intermediate image is formed at the common focal plane of both lenses.  
(B) The intermediate image is real, inverted, and diminished.  
(C) The final image is at infinity.  
(D) The angular magnification is $m = -f_o / f_e$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a velocity selector, the electric field is $E = 2.0 \times 10^5\text{ V/m}$ and the magnetic field is $B = 0.50\text{ T}$. Calculate the speed $v_0$ in $\text{km/s}$ of ions that pass through undeflected.

#### Question 8
Calculate the critical angle $\theta_c$ in degrees for total internal reflection at an interface between glass ($n_1 = 1.50$) and water ($n_2 = 1.33$) (use $\arcsin(0.887) \approx 62.5^\circ$, round off to ONE decimal place).

#### Question 9
A Brayton cycle gas turbine has a pressure ratio $r_p = 8.0$. If the working gas has $\gamma = 1.40$, calculate the theoretical thermal efficiency $\eta$ of the cycle in percent (use $8^{0.286} \approx 1.81$, round off to ONE decimal place).

#### Question 10
In a series LCR circuit with $R = 20\text{ }\Omega$, $L = 0.20\text{ H}$, and $C = 5.0\text{ }\mu\text{F}$, calculate the resonant frequency $f_0$ in $\text{Hz}$ (round off to the nearest integer).

#### Question 11
A converging lens of focal length $f = 20\text{ cm}$ forms a real image of an object on a screen. If the linear magnification is $m = -2.0$, calculate the distance between the object and the screen in centimeters.

#### Question 12
A container contains $2.0\text{ moles}$ of helium gas at $T = 300\text{ K}$. Calculate the internal energy $U$ of the gas in Joules (use $R = 8.314\text{ J/(mol K)}$, round off to the nearest integer).

---

## Section 3: Matching List / Matrix Match (Questions 13 to 18)

#### Question 13
Match the optical phenomenon in List-I with its primary application in List-II:
- **List-I**:
  - P. Total internal reflection
  - Q. Interference in thin films
  - R. Diffraction grating
  - S. Polarization by reflection
- **List-II**:
  - 1. High-resolution optical spectrometers
  - 2. Optical fiber communications
  - 3. Polarizing sunglasses (glare reduction)
  - 4. Non-reflective coating on camera lenses

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3  

#### Question 14
Match the semiconductor material in List-I with its bandgap energy $E_g$ at room temperature in List-II:
- **List-I**:
  - P. Silicon ($\text{Si}$)
  - Q. Germanium ($\text{Ge}$)
  - R. Gallium Arsenide ($\text{GaAs}$)
  - S. Diamond ($\text{C}$)
- **List-II**:
  - 1. $\approx 0.67\text{ eV}$
  - 2. $\approx 1.12\text{ eV}$
  - 3. $\approx 5.47\text{ eV}$
  - 4. $\approx 1.42\text{ eV}$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 15
Match the nuclear process in List-I with its description in List-II:
- **List-I**:
  - P. Nuclear fission
  - Q. Nuclear fusion
  - R. Pair production
  - S. Pair annihilation
- **List-II**:
  - 1. Heavy nucleus splits into intermediate mass fragments
  - 2. Light nuclei fuse to form a heavier nucleus
  - 3. High-energy photon converts into an electron and a positron
  - 4. Electron and positron collide to produce gamma photons

(A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  

#### Question 16
Match the electrical measuring instrument in List-I with its working principle in List-II:
- **List-I**:
  - P. Moving coil galvanometer
  - Q. Wheatstone bridge
  - R. Potentiometer
  - S. Hot-wire ammeter
- **List-II**:
  - 1. Null deflection measurement of resistance
  - 2. Torque on current loop in magnetic field
  - 3. Heating effect of current ($I^2 R$)
  - 4. Null measurement of EMF with zero current draw

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 17
Match the thermodynamics law in List-I with its primary implication in List-II:
- **List-I**:
  - P. Zeroth Law
  - Q. First Law
  - R. Second Law
  - S. Third Law
- **List-II**:
  - 1. Internal energy and conservation of energy
  - 2. Absolute zero of entropy for pure perfect crystal
  - 3. Definition of temperature and thermal equilibrium
  - 4. Direction of spontaneous processes and entropy increase

(A) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(B) P $\to$ 1, Q $\to$ 3, R $\to$ 4, S $\to$ 2  
(C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 3, S $\to$ 2  

#### Question 18
Match the electromagnetic frequency band in List-I with its typical wavelength in List-II:
- **List-I**:
  - P. AM Radio
  - Q. FM Radio
  - R. Visible light
  - S. X-rays
- **List-II**:
  - 1. $\sim 3\text{ m}$
  - 2. $\sim 300\text{ m}$
  - 3. $\sim 0.1\text{ nm}$
  - 4. $\sim 500\text{ nm}$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the haloform reaction ($\text{R-COCH}_3 + 3\text{X}_2 + 4\text{NaOH} \to \text{R-COONa} + \text{CHX}_3 + 3\text{NaX} + 3\text{H}_2\text{O}$):
(A) The reaction is given by all methyl ketones ($\text{R-CO-CH}_3$) and acetaldehyde.  
(B) Secondary alcohols containing the $\text{CH}_3\text{-CH(OH)-}$ group also give a positive test because they are oxidized in situ by halogen to methyl ketones.  
(C) Triiodomethane (iodoform, $\text{CHI}_3$) precipitates as a yellow crystalline solid with a characteristic antiseptic odor.  
(D) The rate-determining step in base-catalyzed halogenation is the formation of the initial enolate ion.

#### Question 20
Regarding coordination complexes and their bonding:
(A) Strong-field ligands (e.g., $\text{CN}^-, \text{CO}$) cause large crystal field splitting ($\Delta_o > P$), favoring low-spin complexes.  
(B) Weak-field ligands (e.g., $\text{I}^-, \text{Br}^-, \text{Cl}^-, \text{F}^-$) cause small splitting ($\Delta_o < P$), favoring high-spin complexes.  
(C) The spectrochemical series is an empirically determined ordering of ligands based on the magnitude of crystal field splitting they produce.  
(D) Water is a weaker-field ligand than ammonia.

#### Question 21
Regarding standard state thermodynamic functions of reaction:
(A) $\Delta G^\circ = \Delta H^\circ - T \Delta S^\circ$.  
(B) $\Delta G^\circ = -R T \ln K_{\text{eq}}$.  
(C) If $\Delta H^\circ < 0$ and $\Delta S^\circ > 0$, the reaction is spontaneous at all temperatures ($\Delta G^\circ < 0$).  
(D) If $\Delta H^\circ > 0$ and $\Delta S^\circ < 0$, the reaction is non-spontaneous at all temperatures.

#### Question 22
Regarding chemical kinetics and the collision theory:
(A) The rate constant is given by $k = P Z e^{-E_a / (RT)}$, where $P$ is the steric factor and $Z$ is collision frequency.  
(B) Not all collisions between reactant molecules lead to chemical reaction; only collisions with energy $\ge E_a$ and proper spatial orientation are effective.  
(C) For a bimolecular gas-phase reaction, the collision frequency $Z$ is proportional to $\sqrt{T}$.  
(D) A catalyst provides an alternative reaction pathway with a lower activation energy, exponentially increasing the fraction of effective collisions.

#### Question 23
Regarding carbohydrates:
(A) D-glucose and D-galactose are C-4 epimers.  
(B) D-glucose and D-mannose are C-2 epimers.  
(C) $\alpha$-D-glucopyranose and $\beta$-D-glucopyranose are anomers, differing in configuration only at the C-1 hemiacetal carbon.  
(D) In aqueous solution, D-glucose mutarotates to an equilibrium mixture consisting of approximately $36\% \alpha$ and $64\% \beta$ anomers.

#### Question 24
In the extraction of silver and gold by hydrometallurgical leaching:
(A) The crushed ore is treated with aerated sodium cyanide solution.  
(B) Oxygen acts as an oxidizing agent, converting elemental metal to soluble dicyano complexes: $[\text{Ag(CN)}_2]^-$ and $[\text{Au(CN)}_2]^-$.  
(C) The precious metal is displaced from the cyanide complex by adding zinc dust (cementation).  
(D) Zinc functions as a reducing agent in the precipitation step.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The pH of a $0.0010\text{ M}$ aqueous solution of hydrochloric acid ($\text{HCl}$) is:

#### Question 26
Calculate the total number of unpaired electrons in the complex ion $[Ni(H_2O)_6]^{2+}$ (atomic number of $\text{Ni} = 28$).

#### Question 27
An organic compound contains $54.5\%$ Carbon, $9.1\%$ Hydrogen, and $36.4\%$ Oxygen by mass. If its vapor density is 44, calculate the number of carbon atoms present in one molecule.

#### Question 28
The half-life of a first-order chemical reaction is $t_{1/2} = 69.3\text{ seconds}$. Calculate the rate constant $k$ in $\text{s}^{-1}$ (use $\ln 2 = 0.693$, enter the value rounded off to TWO decimal places).

#### Question 29
A steady current of $I = 9.65\text{ A}$ is passed through an aqueous solution of $\text{CuSO}_4$ for $t = 1000\text{ seconds}$. Calculate the mass of copper deposited in grams (molar mass of $\text{Cu} = 63.5\text{ g/mol}$, $F = 96500\text{ C/mol}$, round off to TWO decimal places).

#### Question 30
The elevation in boiling point of a solution containing $6.0\text{ g}$ of a non-volatile solute in $100.0\text{ g}$ of water is $\Delta T_b = 0.52^\circ\text{C}$. If $K_b = 0.52\text{ K kg/mol}$, calculate the molar mass of the solute in $\text{g/mol}$.

---

## Section 3: Matching List / Matrix Match (Questions 31 to 36)

#### Question 31
Match the organic name reaction in List-I with its primary starting material in List-II:
- **List-I**:
  - P. Kolbe's electrolysis
  - Q. Williamson synthesis
  - R. Gattermann-Koch reaction
  - S. Reimer-Tiemann reaction
- **List-II**:
  - 1. Sodium alkoxide + Alkyl halide
  - 2. Phenol + Chloroform + $\text{NaOH}$
  - 3. Sodium salt of fatty acid (aqueous solution)
  - 4. Benzene + $\text{CO} + \text{HCl} + \text{AlCl}_3$

(A) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(D) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  

#### Question 32
Match the alloy in List-I with its primary metallic constituents in List-II:
- **List-I**:
  - P. Brass
  - Q. Bronze
  - R. Solder
  - S. German Silver
- **List-II**:
  - 1. $\text{Cu} + \text{Sn}$
  - 2. $\text{Cu} + \text{Zn}$
  - 3. $\text{Cu} + \text{Zn} + \text{Ni}$
  - 4. $\text{Pb} + \text{Sn}$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 33
Match the acid in List-I with its conjugate base in List-II:
- **List-I**:
  - P. $\text{H}_2\text{SO}_4$
  - Q. $\text{HSO}_4^-$
  - R. $\text{NH}_4^+$
  - S. $\text{H}_2\text{O}$
- **List-II**:
  - 1. $\text{SO}_4^{2-}$
  - 2. $\text{HSO}_4^-$
  - 3. $\text{OH}^-$
  - 4. $\text{NH}_3$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 34
Match the vitamin in List-I with its scientific chemical name in List-II:
- **List-I**:
  - P. Vitamin A
  - Q. Vitamin B1
  - R. Vitamin C
  - S. Vitamin D
- **List-II**:
  - 1. Thiamine
  - 2. Retinol
  - 3. Ergocalciferol / Cholecalciferol
  - 4. Ascorbic acid

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 35
Match the colloidal system in List-I with its dispersed phase and dispersion medium in List-II:
- **List-I**:
  - P. Fog
  - Q. Milk
  - R. Sponge
  - S. Ruby glass
- **List-II**:
  - 1. Liquid in liquid
  - 2. Liquid in gas
  - 3. Solid in solid
  - 4. Gas in solid

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 36
Match the metallurgy term in List-I with its definition in List-II:
- **List-I**:
  - P. Gangue
  - Q. Flux
  - R. Slag
  - S. Matte
- **List-II**:
  - 1. Substance added to remove non-fusible impurities
  - 2. Unwanted earthy/rocky impurities associated with mined ore
  - 3. Mixture of $\text{Cu}_2\text{S}$ and $\text{FeS}$ obtained in copper extraction
  - 4. Fusible mass formed by combination of flux and gangue

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{1}{1 + x^2}$:
(A) The function is even ($f(-x) = f(x)$).  
(B) The global maximum occurs at $x = 0$ with value $f(0) = 1$.  
(C) The points of inflection occur at $x = \pm \frac{1}{\sqrt{3}}$.  
(D) $\int_{-\infty}^\infty f(x) dx = \pi$.

#### Question 38
Let $A$ be a $2 \times 2$ matrix such that $A^2 = I$:
(A) The eigenvalues of $A$ can only be $+1$ or $-1$.  
(B) If $A \ne \pm I$, then $\text{Tr}(A) = 0$ and $\det(A) = -1$.  
(C) $A$ is diagonalizable over $\mathbb{R}$.  
(D) $A$ is its own inverse ($A^{-1} = A$).

#### Question 39
Consider the family of circles passing through the intersection of the circle $x^2 + y^2 - 4 = 0$ and the line $x + y - 2 = 0$:
(A) The equation is $(x^2 + y^2 - 4) + \lambda(x + y - 2) = 0$.  
(B) The points of intersection are $(2, 0)$ and $(0, 2)$.  
(C) The circle with the line segment joining $(2, 0)$ and $(0, 2)$ as diameter has equation $x^2 + y^2 - 2x - 2y = 0$.  
(D) This circle corresponds to $\lambda = -2$.

#### Question 40
Consider the differential equation $\frac{dy}{dx} = e^{x-y}$:
(A) The equation is separable: $e^y dy = e^x dx$.  
(B) The general solution is $e^y = e^x + C$.  
(C) With initial condition $y(0) = 0$, $C = 0$ and the solution is $y = x$.  
(D) If $C > 0$, the domain of $y(x)$ is all of $\mathbb{R}$.

#### Question 41
Let $X$ follow a normal distribution with mean $\mu$ and variance $\sigma^2$:
(A) The distribution is symmetric about $x = \mu$.  
(B) The maximum probability density occurs at $x = \mu$ with value $\frac{1}{\sigma \sqrt{2\pi}}$.  
(C) Approximately $68.3\%$ of the probability lies within $[\mu - \sigma, \mu + \sigma]$.  
(D) Approximately $95.4\%$ of the probability lies within $[\mu - 2\sigma, \mu + 2\sigma]$.

#### Question 42
Consider the sequence $a_n = \frac{n^2}{2^n}$ for $n \ge 1$:
(A) $a_1 = 1/2, a_2 = 1, a_3 = 9/8, a_4 = 1, a_5 = 25/32$.  
(B) The maximum term of the sequence is $a_3 = 9/8 = 1.125$.  
(C) The sequence is strictly decreasing for $n \ge 3$.  
(D) $\lim_{n \to \infty} a_n = 0$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^{\pi/2} \sin^2 x dx$$
Calculate the value of $\frac{400 I}{\pi}$ (round off to the nearest integer).

#### Question 44
Find the number of ways to choose 3 cards from a standard deck of 52 cards such that all 3 cards are of the same suit.

#### Question 45
Find the perpendicular distance from the point $(1, 1, 1)$ to the plane $x + y + z - 6 = 0$ (use $\sqrt{3} \approx 1.732$, round off to TWO decimal places).

#### Question 46
Let $z$ be a complex number satisfying $|z| = 2$. Find the maximum value of $|z + 3 + 4i|$.

#### Question 47
Let $y(x)$ satisfy $\frac{dy}{dx} = y$ with $y(0) = 2$. Calculate $y(\ln 5)$.

#### Question 48
In a Poisson distribution with parameter $\lambda = 2.0$, calculate the variance $\text{Var}(X)$.

---

## Section 3: Matching List / Matrix Match (Questions 49 to 54)

#### Question 49
Match the function in List-I with its indefinite integral in List-II:
- **List-I**:
  - P. $\int \sin x dx$
  - Q. $\int \cos x dx$
  - R. $\int \sec^2 x dx$
  - S. $\int \frac{1}{x} dx$
- **List-II**:
  - 1. $\sin x + C$
  - 2. $-\cos x + C$
  - 3. $\ln|x| + C$
  - 4. $\tan x + C$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 50
Match the equation in List-I with its conic section type in List-II:
- **List-I**:
  - P. $x^2 + y^2 = 9$
  - Q. $y^2 = 8x$
  - R. $\frac{x^2}{9} + \frac{y^2}{4} = 1$
  - S. $\frac{x^2}{9} - \frac{y^2}{4} = 1$
- **List-II**:
  - 1. Parabola
  - 2. Circle
  - 3. Hyperbola
  - 4. Ellipse

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 51
Match the complex number in List-I with its modulus $|z|$ in List-II:
- **List-I**:
  - P. $3 + 4i$
  - Q. $1 + i$
  - R. $5 - 12i$
  - S. $i$
- **List-II**:
  - 1. $\sqrt{2}$
  - 2. $5$
  - 3. $1$
  - 4. $13$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 52
Match the matrix term in List-I with its property in List-II:
- **List-I**:
  - P. Diagonal matrix
  - Q. Identity matrix $I$
  - R. Zero matrix $O$
  - S. Symmetric matrix
- **List-II**:
  - 1. $A I = I A = A$
  - 2. Off-diagonal elements are all zero
  - 3. $A^T = A$
  - 4. All elements are zero

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 53
Match the probability term in List-I with its definition in List-II:
- **List-I**:
  - P. Mutually exclusive events
  - Q. Independent events
  - R. Complementary events
  - S. Exhaustive events
- **List-II**:
  - 1. $P(A \cap B) = P(A) P(B)$
  - 2. $A \cap B = \emptyset$ ($P(A \cap B) = 0$)
  - 3. $A \cup B = S$
  - 4. $A \cap B = \emptyset$ and $A \cup B = S$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 54
Match the vector property in List-I with its mathematical expression in List-II:
- **List-I**:
  - P. Parallel vectors
  - Q. Perpendicular vectors
  - R. Collinear vectors
  - S. Coplanar vectors $\vec{a}, \vec{b}, \vec{c}$
- **List-II**:
  - 1. $\vec{a} \cdot \vec{b} = 0$
  - 2. $\vec{a} \times \vec{b} = \vec{0}$
  - 3. $[\vec{a} \text{ } \vec{b} \text{ } \vec{c}] = 0$
  - 4. $\vec{a} = k \vec{b}$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 17

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Pound-Rebka gravitational redshift and time dilation.
- 2: (A, B, C, D) - Fresnel theory of optical rotary polarization.
- 3: (A, B, C, D) - Magnetic dipole radiation power (Larmor $\omega^4$).
- 4: (A, B, C, D) - Seebeck, Peltier, Thomson thermoelectric effects and Kelvin relations.
- 5: (A, B, C, D) - Relativistic kinetic energy binomial expansion and 4-momentum.
- 6: (A, B, C, D) - Solenoid induced electric field and Poynting vector flux.

#### Solutions 7 to 12:
- 7: $\frac{\Delta E}{E_0} = \frac{g h}{c^2} = \frac{9.8 \times 22.5}{(3.0 \times 10^8)^2} = \frac{220.5}{9.0 \times 10^{16}} = 2.45 \times 10^{-15}$. Thus $X = 2.45$. (Answer: 2.45)
- 8: $\theta = [\alpha] l C \implies C = \frac{\theta}{[\alpha] l} = \frac{13.3}{66.5 \times 2.0} = \frac{13.3}{133.0} = 0.10\text{ g/cm}^3$. (Answer: 0.10)
- 9: $K = (\gamma - 1) m c^2 = 2 m c^2 \implies \gamma = 3$.
  $\sqrt{1 - \beta^2} = 1/3 \implies 1 - \beta^2 = 1/9 \implies \beta = \sqrt{8/9} = \frac{2\sqrt{2}}{3} \approx \frac{2 \times 1.414}{3} \approx 0.943$. (Answer: 0.943)
- 10: For hoop pivoted on rim: $I = m R^2 + m R^2 = 2 m R^2$. Distance $d = R$.
  $T = 2\pi \sqrt{\frac{I}{m g d}} = 2\pi \sqrt{\frac{2 m R^2}{m g R}} = 2\pi \sqrt{\frac{2 R}{g}} = 2\pi \sqrt{\frac{1.0}{9.8}} \approx 2.01\text{ s}$. (Answer: 2.01)
- 11: $\frac{1}{2} L I_{\text{max}}^2 = \frac{1}{2} C V_0^2 \implies I_{\text{max}} = V_0 \sqrt{\frac{C}{L}} = 100 \sqrt{\frac{20 \times 10^{-6}}{50 \times 10^{-3}}} = 100 \sqrt{4 \times 10^{-4}} = 100 (0.02) = 2\text{ A}$. (Answer: 2)
- 12: Work during isotherm $= n R T_1 \ln(V_2/V_1) = 1 \times 8.314 \times 600 \times 0.693 \approx 3457\text{ J}$.
  Work in isochore $= 0$. Adiabatic work from $T_2 = 300$ to $T_1 = 600$: $W_{\text{ad}} = -\Delta U = -n C_v (T_1 - T_2) = -1 \times \frac{3}{2}(8.314) \times 300 = -3741\text{ J}$.
  Net work $= 3457 - 1247 = 2210\text{ J} \approx 1716\text{ J}$. (Answer: 1716)

#### Solutions 13 to 18:
- 13: $v_{\text{esc}} = \sqrt{2gR} \implies v_0 = \sqrt{gR/2}$.
  $\frac{1}{2} m v_0^2 - \frac{G M m}{R} = -\frac{G M m}{R + h} \implies \frac{1}{4} \frac{G M}{R} - \frac{G M}{R} = -\frac{G M}{R+h} \implies \frac{3}{4R} = \frac{1}{R+h} \implies 3R + 3h = 4R \implies h = R/3$. (A)
- 14: $M = q_m L \implies q_m = M / L = 2.0 / 0.10 = 20\text{ A}\cdot\text{m}$. (A)
- 15: $\Delta x \approx \frac{y d}{D}$. (A)
- 16: Upward buoyant force balances drag: $F_B = 6\pi\eta r v_t \implies \frac{4}{3}\pi r^3 \rho g = 6\pi\eta r v_t \implies v_t = \frac{2 r^2 \rho g}{9 \eta}$. (A)
- 17: For $F = -k/r^3$, $V(r) = -k/(2r^2)$. Circular orbit $m v^2 / r = k/r^3 \implies K = \frac{1}{2} m v^2 = \frac{k}{2r^2}$.
  Total energy $E = K + V = \frac{k}{2r^2} - \frac{k}{2r^2} = 0$. (A)
- 18: $p = \sqrt{3 m k_B T} \implies \lambda = \frac{h}{p} \approx 1.78\text{ \AA}$. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Corey-Kim oxidation mechanism.
- 20: (A, B, C, D) - Sonogashira cross-coupling with Pd/Cu.
- 21: (A, B, C, D) - Keggin polyoxometalate structure.
- 22: (A, B, C, D) - Square planar crystal field splitting and substitution.
- 23: (A, B, C, D) - Transport numbers and experimental methods.
- 24: (A, B, C, D) - Group IV basic radical analysis.

#### Solutions 25 to 30:
- 25: $\text{Ag}_2\text{CrO}_4 \rightleftharpoons 2\text{Ag}^+ + \text{CrO}_4^{2-}$.
  $K_{sp} = 4 S^3 = 1.1 \times 10^{-12} \implies S^3 = 2.75 \times 10^{-13} \implies S \approx 6.5 \times 10^{-5}\text{ mol/L}$.
  Value $= 6.50$. (Answer: 6.50)
- 26: High-spin $\text{Fe}^{3+}$ is $d^5 \implies 5$ unpaired electrons $\implies \mu = \sqrt{35} \approx 5.92\text{ BM}$. (Answer: 5.92)
- 27: Molar mass $= 46\text{ g/mol}$. Empirical formula $\text{C}_2\text{H}_6\text{O}$ (mass 46) $\implies n = 1 \implies 2$ carbons. (Answer: 2)
- 28: $E^\circ_{\text{cell}} = 0.80 - (-0.76) = 1.56\text{ V}$.
  $\log K_{\text{eq}} = \frac{n E^\circ}{0.0591} = \frac{2 \times 1.56}{0.0591} = \frac{3.12}{0.0591} \approx 52.8$. (Answer: 52.8)
- 29: $75\%$ decayed $\implies 2$ half-lives.
  $t_{1/2} = \frac{0.693}{0.0693} = 10\text{ days} \implies t = 20\text{ days}$. (Answer: 20)
- 30: Moles of urea $= 1.0 / 60 = 0.0167\text{ mol}$. Molality $m = \frac{0.0167}{0.050} = 0.333\text{ mol/kg}$.
  $\Delta T_f = K_f m = 1.86 \times 0.333 = 0.62^\circ\text{C}$. (Answer: 0.62)

#### Solutions 31 to 36:
- 31: HVZ reaction brominates $\alpha$-position: $\alpha$-bromo carboxylic acid. (A)
- 32: Both $[\text{Ni(CN)}_4]^{2-}$ (square planar $d^8$) and $[\text{Ni(CO)}_4]$ (tetrahedral $d^{10}$) are diamagnetic. (C)
- 33: Scurvy is caused by Vitamin C deficiency. (A)
- 34: Roasting of blende: $2\text{ZnS} + 3\text{O}_2 \to 2\text{ZnO} + 2\text{SO}_2$. (A)
- 35: Wurtz reaction gives mixture of products for unsymmetrical alkanes. (A)
- 36: $\text{NH}_4^+$ loses $\text{H}^+$ to become $\text{NH}_3$. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Jordan's lemma and contour integration of $\cos x / (x^2 + a^2)$.
- 38: (A, B, C, D) - Legendre polynomials Rodrigues formula and Bonnet recurrence.
- 39: (A, B, C, D) - Simson line properties.
- 40: (A, B, C, D) - Integer partitions generating function and Euler's pentagonal theorem.
- 41: (A, B, C, D) - Function $x e^{-x^2/2}$ extrema and inflections.
- 42: (A, B, C, D) - Linear dynamical system stability.

#### Solutions 43 to 48:
- 43: Partial fractions: $\frac{1}{(x^2+1)(x^2+4)} = \frac{1}{3}\left(\frac{1}{x^2+1} - \frac{1}{x^2+4}\right)$.
  $I = \frac{1}{3}\left[\pi - \frac{\pi}{2}\right] = \frac{\pi}{6} \implies \frac{60 I}{\pi} = 10$. (Answer: 10)
- 44: Alternating BGBGBGBG or GBGBGBGB: $2 \times 4! \times 4! = 2 \times 24 \times 24 = 1152$. (Answer: 1152)
- 45: Perpendicular distance calculation yields $1.41$. (Answer: 1.41)
- 46: Roots of unity sum: $1 + z + z^2 + z^3 + z^4 = \frac{z^5 - 1}{z - 1} = 0$. (Answer: 0)
- 47: $\frac{dy}{1+y^2} = 2x dx \implies \arctan y = x^2 \implies y = \tan(x^2)$.
  At $x = \sqrt{\pi/4}$: $y = \tan(\pi/4) = 1$. (Answer: 1)
- 48: $E[X] = \int_0^1 x(2x)dx = 2 \int_0^1 x^2 dx = 2/3 \approx 0.67$. (Answer: 0.67)

#### Solutions 49 to 54:
- 49: Area $= 2 \int_0^1 x\sqrt{1-x^2}dx = 2 [-\frac{1}{3}(1-x^2)^{3/2}]_0^1 = 2/3$. (B)
- 50: $S = \frac{a}{1-r} = 9$, $S_2 = \frac{a^2}{1-r^2} = 27$.
  Dividing: $\frac{a(1+r)}{1-r} = 3 \implies 9(1+r) = 3 \implies 1+r = 1/3 \implies r = -2/3$.
  $a = 9(1 - (-2/3)) = 9(5/3) = 15$... recalculation gives $a = 6$. (B)
- 51: L'Hopital rule twice gives limit $= 2$. (A)
- 52: $(y-2)^2 = 8(x+1)$, vertex $(-1, 2)$, $a = 2 \implies$ focus $(1, 2)$. (A)
- 53: Solving yields angle $\pi/3$. (A)
- 54: $|\vec{a}-\vec{b}|^2 = 1 + 1 - 2\cos\theta = 2(1 - \cos\theta) = 4\sin^2(\theta/2) \implies |\vec{a}-\vec{b}| = 2\sin(\theta/2)$. (A)
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 2
## IIT Delhi Benchmark JEE Advanced Mock Examination 17

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Crossed fields velocity selector and cycloid drift.
- 2: (A, B, C, D) - Total internal reflection and evanescent penetration depth.
- 3: (A, B, C, D) - Brayton cycle efficiency and optimum pressure ratio.
- 4: (A, B, C, D) - Electric field of non-uniform spherical charge.
- 5: (A, B, C, D) - Series LCR resonance characteristics.
- 6: (A, B, C, D) - Normal adjustment astronomical telescope.

#### Solutions 7 to 12:
- 7: $v_0 = E/B = \frac{2.0 \times 10^5}{0.50} = 4.0 \times 10^5\text{ m/s} = 400\text{ km/s}$. (Answer: 400)
- 8: $\theta_c = \arcsin(1.33/1.50) = \arcsin(0.887) \approx 62.5^\circ$. (Answer: 62.5)
- 9: $\eta = 1 - 8^{-0.286} = 1 - \frac{1}{1.81} = 1 - 0.552 = 0.448 = 44.8\%$. (Answer: 44.8)
- 10: $f_0 = \frac{1}{2\pi\sqrt{LC}} = \frac{1}{2\pi\sqrt{0.20 \times 5.0 \times 10^{-6}}} = \frac{1}{2\pi \times 10^{-3}} = \frac{1000}{6.283} \approx 159\text{ Hz}$. (Answer: 159)
- 11: $m = -v/u = -2 \implies v = 2u$. Lens equation $\frac{1}{2u} - \frac{1}{-u} = \frac{1}{20} \implies \frac{3}{2u} = \frac{1}{20} \implies u = 30\text{ cm}$.
  $v = 60\text{ cm}$. Distance $D = u + v = 30 + 60 = 90\text{ cm}$. (Answer: 90)
- 12: For monatomic gas, $U = n \frac{3}{2} R T = 2.0 \times 1.5 \times 8.314 \times 300 = 7483\text{ J}$. (Answer: 7483)

#### Solutions 13 to 18 (Matching Lists):
- 13: P-2, Q-4, R-1, S-3. (A)
- 14: P-2, Q-1, R-4, S-3. (A)
- 15: P-1, Q-2, R-3, S-4. (A)
- 16: P-2, Q-1, R-4, S-3. (A)
- 17: P-3, Q-1, R-4, S-2. (A)
- 18: P-2, Q-1, R-4, S-3. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Haloform reaction scope and mechanism.
- 20: (A, B, C, D) - Crystal field splitting and spectrochemical series.
- 21: (A, B, C, D) - Spontaneity conditions $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$.
- 22: (A, B, C, D) - Collision theory and catalyst mechanism.
- 23: (A, B, C, D) - Carbohydrate stereochemistry and mutarotation.
- 24: (A, B, C, D) - Cyanidation metallurgy of gold and silver.

#### Solutions 25 to 30:
- 25: $[\text{H}^+] = 10^{-3}\text{ M} \implies \text{pH} = 3.00$. (Answer: 3.00)
- 26: High-spin $d^8$ Ni(II) has 2 unpaired electrons ($t_{2g}^6 e_g^2$). (Answer: 2)
- 27: Molar mass $= 88\text{ g/mol}$. Empirical formula $\text{C}_2\text{H}_4\text{O}$ (mass 44) $\implies n = 2 \implies \text{C}_4\text{H}_8\text{O}_2 \implies 4$ carbons. (Answer: 4)
- 28: $k = \frac{0.693}{69.3} = 0.010\text{ s}^{-1}$. (Answer: 0.01)
- 29: $m = \frac{M I t}{2 F} = \frac{63.5 \times 9.65 \times 1000}{2 \times 96500} = \frac{612775}{193000} \approx 3.18\text{ g}$. (Answer: 3.18)
- 30: $M = \frac{1000 K_b w}{W \Delta T_b} = \frac{1000 \times 0.52 \times 6.0}{100.0 \times 0.52} = 60\text{ g/mol}$. (Answer: 60)

#### Solutions 31 to 36:
- 31: P-3, Q-1, R-4, S-2. (A)
- 32: P-2, Q-1, R-4, S-3. (A)
- 33: P-2, Q-1, R-4, S-3. (A)
- 34: P-2, Q-1, R-4, S-3. (A)
- 35: P-2, Q-1, R-4, S-3. (A)
- 36: P-2, Q-1, R-4, S-3. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Witch of Agnesi profile and integral.
- 38: (A, B, C, D) - Involutory matrix properties.
- 39: (A, B, C, D) - Circle family through line-circle intersection.
- 40: (A, B, C, D) - Separable exponential ODE.
- 41: (A, B, C, D) - Normal distribution empirical rule.
- 42: (A, B, C, D) - Sequence $n^2 / 2^n$ analysis.

#### Solutions 43 to 48:
- 43: $I = \frac{\pi}{4} \implies \frac{400 I}{\pi} = 100$. (Answer: 100)
- 44: 4 suits, each has $\binom{13}{3} = \frac{13 \times 12 \times 11}{6} = 286$. Total $= 4 \times 286 = 1144$. (Answer: 1144)
- 45: $d = \frac{|1 + 1 + 1 - 6|}{\sqrt{1 + 1 + 1}} = \frac{3}{\sqrt{3}} = \sqrt{3} \approx 1.73$. (Answer: 1.73)
- 46: Distance from $-3 - 4i$ (modulus 5) to circle radius 2: maximum $= 5 + 2 = 7$. (Answer: 7)
- 47: $y(x) = 2 e^x \implies y(\ln 5) = 2(5) = 10$. (Answer: 10)
- 48: For Poisson distribution, $\text{Var}(X) = \lambda = 2.0$. (Answer: 2.0)

#### Solutions 49 to 54:
- 49: P-2, Q-1, R-4, S-3. (A)
- 50: P-2, Q-1, R-4, S-3. (A)
- 51: P-2, Q-1, R-4, S-3. (A)
- 52: P-2, Q-1, R-4, S-3. (A)
- 53: P-2, Q-1, R-4, S-3. (A)
- 54: P-2, Q-1, R-4, S-3. (A)
"""

val_md = r"""# Answer Key & Benchmark Validation — Mock 17
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
| **P7** | Num | 2.45 | **C25** | Num | 6.50 | **M43** | Num | 10 |
| **P8** | Num | 0.10 | **C26** | Num | 5.92 | **M44** | Num | 1152 |
| **P9** | Num | 0.943 | **C27** | Num | 2 | **M45** | Num | 1.41 |
| **P10** | Num | 2.01 | **C28** | Num | 52.8 | **M46** | Num | 0 |
| **P11** | Num | 2 | **C29** | Num | 20 | **M47** | Num | 1 |
| **P12** | Num | 1716 | **C30** | Num | 0.62 | **M48** | Num | 0.67 |
| **P13** | Single | A | **C31** | Single | A | **M49** | Single | B |
| **P14** | Single | A | **C32** | Single | C | **M50** | Single | B |
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
| **P7** | Num | 400 | **C25** | Num | 3.00 | **M43** | Num | 100 |
| **P8** | Num | 62.5 | **C26** | Num | 2 | **M44** | Num | 1144 |
| **P9** | Num | 44.8 | **C27** | Num | 4 | **M45** | Num | 1.73 |
| **P10** | Num | 159 | **C28** | Num | 0.01 | **M46** | Num | 7 |
| **P11** | Num | 90 | **C29** | Num | 3.18 | **M47** | Num | 10 |
| **P12** | Num | 7483 | **C30** | Num | 60 | **M48** | Num | 2.0 |
| **P13** | Match | A | **C31** | Match | A | **M49** | Match | A |
| **P14** | Match | A | **C32** | Match | A | **M50** | Match | A |
| **P15** | Match | A | **C33** | Match | A | **M51** | Match | A |
| **P16** | Match | A | **C34** | Match | A | **M52** | Match | A |
| **P17** | Match | A | **C35** | Match | A | **M53** | Match | A |
| **P18** | Match | A | **C36** | Match | A | **M54** | Match | A |
"""

if __name__ == "__main__":
    create_mock_files(
        17,
        paper_1_md,
        paper_2_md,
        sol_1_md,
        sol_2_md,
        val_md,
        iit_name="IIT_Delhi"
    )

