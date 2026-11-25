# Detailed Pedagogical Solutions — Mock Examination 08 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Electromagnetic Induction on Inclined Rails, Motional EMF, Terminal Velocity.
- **2. Derivation**:
  - The vertical magnetic field has component perpendicular to the inclined plane $B_\perp = B\cos\theta$. Option (A) is correct.
  - Motional EMF induced along rod of length $L$: $\mathcal{E} = B_\perp L v = B L v \cos\theta$. Option (B) is correct.
  - Induced current $I = \mathcal{E}/R = \frac{BLv\cos\theta}{R}$. Magnetic force $\vec{F} = I(\vec{L}\times\vec{B})$ is horizontal.
  - Component along the incline opposing motion is $F_{\text{mag}}\cos\theta = I L B \cos\theta = \frac{B^2 L^2 v \cos^2\theta}{R}$. Option (C) is correct.
  - At terminal velocity, gravity component down incline balances magnetic retarding force: $mg\sin\theta = \frac{B^2 L^2 v_t \cos^2\theta}{R} \implies v_t = \frac{mgR\sin\theta}{B^2 L^2 \cos^2\theta}$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Dielectric Liquid Rise, Virtual Work, Electrostatic Fringing Fields.
- **2. Derivation**:
  - Fringing fields at the lower capacitor boundary exert an upward gradient force on the polarized dielectric molecules. Option (A) is correct.
  - Capacitance when liquid rises to height $y$: $C(y) = \frac{\varepsilon_0 w}{d}[(H-y) + Ky] = \frac{\varepsilon_0 w}{d}[H + (K-1)y]$.
  - Upward force at constant voltage: $F_e = \frac{1}{2}V_0^2 \frac{dC}{dy} = \frac{1}{2}\varepsilon_0 (K-1)\frac{w}{d}V_0^2$. Option (B) is correct.
  - Gravity force: $F_g = m g = (\rho w d h)g$. Equating forces: $\rho w d h g = \frac{1}{2}\varepsilon_0 (K-1)\frac{w}{d}V_0^2 \implies h = \frac{\varepsilon_0 (K-1)V_0^2}{2\rho g d^2}$. Option (C) is correct.
  - Disconnected plates carry constant charge $Q$, and energy is lowered by liquid insertion ($U = Q^2/(2C)$), so liquid still rises. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Adiabatic Sound Propagation, Laplace Formula, Heat Capacity Ratio.
- **2. Derivation**:
  - Sound propagation involves rapid compressions and rarefactions with negligible heat exchange, hence adiabatic ($P V^\gamma = \text{const}$). Option (A) is correct.
  - Sound speed: $v = \sqrt{\frac{B_{\text{ad}}}{\rho}} = \sqrt{\frac{\gamma P}{\rho}} = \sqrt{\frac{\gamma RT}{M}}$. Option (B) is correct.
  - For polyatomic molecules, as vibrational degrees of freedom activate at elevated temperatures, $C_V$ increases, causing $\gamma = 1 + R/C_V$ to decrease towards $4/3$. Option (C) is correct.
  - Newton assumed isothermal propagation ($v = \sqrt{RT/M} \approx 280\text{ m/s}$), which is $\approx 15\%$ lower than Laplace's $331\text{ m/s}$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Lloyd's Mirror Interference, Boundary Phase Shift, Virtual Coherent Source.
- **2. Derivation**:
  - Virtual source $S_2$ is the specular reflection of $S_1$ across the mirror plane, located at distance $h$ below the mirror surface. Option (A) is correct.
  - Reflection from a higher index medium (glass) introduces a $\pi$ phase shift (half-wavelength optical path shift $\lambda/2$). Option (B) is correct.
  - Separation between coherent sources is $2h$, so fringe width is $\beta = \frac{\lambda D}{2h}$. Option (C) is correct.
  - At grazing contact line ($y = 0$), geometric path difference is 0, but the reflection phase shift of $\pi$ produces destructive interference (dark fringe). Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Quantum Particle in 1D Infinite Potential Box, Eigenfunctions, Probability Density.
- **2. Derivation**:
  - Boundary conditions $\psi(0) = \psi(L) = 0$ yield $\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$. Option (A) is correct.
  - Energy eigenvalues $E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2} = \frac{n^2 h^2}{8mL^2}$. Option (B) is correct.
  - For $n=1$, $|\psi_1(L/2)|^2 = \frac{2}{L}\sin^2(\pi/2) = \frac{2}{L} \ne 0$ (probability is maximum, not zero). Option (C) is incorrect!
  - By symmetry of probability density $|\psi_n(x)|^2$ about $x = L/2$, $\langle x \rangle = L/2$ for all stationary states. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Non-Inertial Frames, Coriolis Force and Easterly Deflection.
- **2. Derivation**:
  - Coriolis acceleration in rotating frame: $\vec{a}_C = -2(\vec{\Omega} \times \vec{v})$. Option (A) is correct.
  - For falling body, $\vec{v} \approx -g t \hat{k}$. Since $\vec{\Omega}$ points northward, $-2(\vec{\Omega}\times\vec{v})$ points toward the East. Option (B) is correct.
  - Integration: $a_x = 2\Omega g t \cos\lambda \implies v_x = \Omega g t^2 \cos\lambda \implies x = \frac{1}{3}\Omega g t^3 \cos\lambda$. With $t = \sqrt{2H/g}$: $x = \frac{1}{3}\Omega \cos\lambda \sqrt{\frac{8H^3}{g}}$. Option (C) is correct.
  - $\cos\lambda$ is maximum at the equator ($\lambda = 0^\circ$). Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: $f = \frac{q B}{2\pi m} = \frac{(1.60 \times 10^{-19})(1.50)}{2\pi (1.67 \times 10^{-27})} = \frac{2.40 \times 10^{-19}}{1.0493 \times 10^{-26}} = 2.287 \times 10^7\text{ Hz} = 22.9\text{ MHz}$.
- **Question 8**: Helmholtz center field $B = \left(\frac{4}{5}\right)^{3/2} \frac{\mu_0 N I}{R} = (0.7155) \frac{(4\pi \times 10^{-7})(100)(2.0)}{0.20} = 0.7155 \times (1.2566 \times 10^{-3}) = 8.99 \times 10^{-4}\text{ T} = 0.90\text{ mT}$.
- **Question 9**: $\lambda_A = \frac{\ln 2}{100} = 0.00693\text{ d}^{-1}$, $\lambda_B = \frac{\ln 2}{5.0} = 0.1386\text{ d}^{-1}$.
  $t_{\text{max}} = \frac{\ln(\lambda_B/\lambda_A)}{\lambda_B - \lambda_A} = \frac{\ln(20)}{0.1386 - 0.00693} = \frac{2.9957}{0.1317} \approx 22.7\text{ days}$.
- **Question 10**: $\mu = \frac{\sin\left(\frac{A + \delta_{\text{min}}}{2}\right)}{\sin(A/2)} \implies \sqrt{3} = \frac{\sin(30^\circ + \delta_{\text{min}}/2)}{\sin 30^\circ} = 2\sin(30^\circ + \delta_{\text{min}}/2) \implies \sin(30^\circ + \delta_{\text{min}}/2) = \frac{\sqrt{3}}{2} \implies 30^\circ + \delta_{\text{min}}/2 = 60^\circ \implies \delta_{\text{min}} = 60.0^\circ$.
- **Question 11**: $\eta = 1 - \frac{1}{r^{\gamma - 1}} = 1 - \frac{1}{8^{0.4}} = 1 - \frac{1}{2.30} = 1 - 0.435 = 0.565 = 56.5\% \approx 57\%$.
- **Question 12**: $\Delta y = \frac{(\mu - 1)t D}{d} \implies t = \frac{\Delta y \cdot d}{(\mu - 1) D} = \frac{(6.0 \times 10^{-3}\text{ m})(0.50 \times 10^{-3}\text{ m})}{(1.60 - 1)(1.00\text{ m})} = \frac{3.0 \times 10^{-6}}{0.60} = 5.0 \times 10^{-6}\text{ m} = 5.0\ \mu\text{m}$.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: Elastic collision: both linear momentum and mechanical energy conserved (P-1); Planetary motion: angular momentum about sun conserved (Q-2); Ballistic pendulum: linear momentum conserved during collision, energy lost (R-3); Fixed pivot: angular momentum about pivot conserved (S-4). Option (A).
- **Question 14**: Boundary conditions: $D_{1n}-D_{2n}=\sigma_f$ from Gauss law (P-1); $E_{1t}=E_{2t}$ from zero curl / circulation (Q-2); $B_{1n}=B_{2n}$ from $\nabla\cdot\vec{B}=0$ (R-3); $H_{1t}-H_{2t}=K_f$ from Ampere law (S-4). Option (A).
- **Question 15**: Polarization: $\delta = 0$ is $45^\circ$ linear (P-1); $\delta = \pi/2$ is right circular (P-2); $\delta = \pi$ is $-45^\circ$ linear (R-3); $\delta = 3\pi/2$ is left circular (S-4). Option (A).
- **Question 16**: Differentials: $dU = TdS - PdV$ (P-1); $dH = TdS + VdP$ (Q-2); $dF = -SdT - PdV$ (R-3); $dG = -SdT + VdP$ (S-4). Option (A).
- **Question 17**: Experiments: Photoelectric effect: photon quanta (P-1); Compton: photon momentum (Q-2); Davisson-Germer: matter waves (R-3); Franck-Hertz: atomic discrete levels (S-4). Option (A).
- **Question 18**: Fluid laws: Bernoulli: energy conservation (P-1); Poiseuille: laminar pipe flow (Q-2); Stokes: viscous drag (R-3); Reynolds: turbulence criterion (S-4). Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Small unhindered base yields Saytzeff product (more substituted). Bulky hindered base yields Hofmann product. E2 requires anti-coplanar transition state ($180^\circ$). Quaternary ammonium hydroxide Hofmann elimination gives less substituted alkene due to steric hindrance. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: $\text{cis-}[\text{Co(en)}_2\text{Cl}_2]^+$ lacks plane of symmetry and is chiral (enantiomeric pair). $[\text{Co(en)}_3]^{3+}$ has $D_3$ symmetry (no plane of symmetry, chiral). $\text{trans-}[\text{Co(en)}_2\text{Cl}_2]^+$ has an inversion center and plane of symmetry (achiral). Square planar $[\text{Pt(en)}_2]^{2+}$ has a horizontal mirror plane (achiral). Correct options: **(A), (B)**.
- **Question 21**: Maximum boiling azeotropes show negative deviation from Raoult's law ($\Delta H_{\text{mix}} < 0, \Delta V_{\text{mix}} < 0$). Vapor pressure is minimum at azeotrope. Classic example: $\text{HNO}_3$-water ($68\%$). Liquid and vapor have identical composition at azeotropic boiling point. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: At $pI$, net charge is zero. For neutral amino acids, $pI = (pK_{a1}+pK_{a2})/2$. For aspartic acid, $pI = (2.1+3.9)/2 = 3.0$. At $\text{pH} > pI$, deprotonation yields net negative charge, migrating to anode. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Diels-Alder is a [4+2] concerted pericyclic cycloaddition. Diene must be $s\text{-cis}$. EDG on diene and EWG on dienophile accelerate reaction. Highly stereospecific (syn-addition). Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Pourbaix diagram maps potential vs pH. Immunity zone is metallic stability. Passivation is insoluble protective oxide. Horizontal boundaries are pure redox ($m=0$). Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: First order half-life: $t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{6.93 \times 10^{-4}} = 1000.00\text{ s}$.
- **Question 26**: Molar solubility: $s = \frac{2.33 \times 10^{-3}\text{ g/L}}{233.3\text{ g/mol}} = 1.00 \times 10^{-5}\text{ mol/L}$.
  $K_{sp} = s^2 = (1.00 \times 10^{-5})^2 = 1.00 \times 10^{-10}$. Multiplied by $10^{10}$, the value is $1.00$.
- **Question 27**: $\Delta T_f = K_f m = K_f \frac{w_B / M_B}{w_A / 1000} \implies M_B = \frac{1000 K_f w_B}{w_A \Delta T_f} = \frac{1000 \times 5.12 \times 1.20}{50.0 \times 0.80} = \frac{6144}{40.0} = 153.6\text{ g/mol} \approx 154\text{ g/mol}$.
- **Question 28**: Nernst equation: $E_{\text{cell}} = E_{\text{cell}}^\circ - \frac{0.0591}{2}\log\left(\frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]}\right) = 1.10 - \frac{0.0591}{2}\log(0.010/1.00) = 1.10 - \frac{0.0591}{2}(-2) = 1.10 + 0.0591 = 1.159\text{ V}$.
- **Question 29**: $p = q d = (1.60 \times 10^{-19}\text{ C})(2.0 \times 10^{-11}\text{ m}) = 3.20 \times 10^{-30}\text{ C}\cdot\text{m}$.
  In Debye: $p = \frac{3.20 \times 10^{-30}}{3.336 \times 10^{-30}} = 0.959\text{ D} \approx 0.96\text{ D}$.
- **Question 30**: $\text{HCl}$ is the limiting reagent ($0.20\text{ mol}$). Heat evolved $q = 0.20\text{ mol} \times 57.3\text{ kJ/mol} = 11.46\text{ kJ}$.

---

### Questions 31 to 36 (Matching List Solutions)
- **Question 31**: Cannizzaro gives alcohol and carboxylate (P-1); Aldol gives $\alpha,\beta$-unsaturated carbonyl (Q-2); Clemmensen reduces carbonyl to methylene (R-3); Hofmann bromamide gives primary amine with one less carbon (S-4). Option (A).
- **Question 32**: $[\text{Fe(CN)}_6]^{4-}$ diamagnetic $0\text{ BM}$ (P-1); $[\text{Fe(H}_2\text{O})_6]^{2+}$ 4 unpaired $4.90\text{ BM}$ (Q-2); $[\text{Fe(H}_2\text{O})_6]^{3+}$ 5 unpaired $5.92\text{ BM}$ (R-3); $[\text{Ni(H}_2\text{O})_6]^{2+}$ 2 unpaired $2.83\text{ BM}$ (S-4). Option (A).
- **Question 33**: Pine oil is frother (P-1); Xanthate is collector (Q-2); $\text{NaCN}$ is depressant (R-3); $\text{CuSO}_4$ is activator (S-4). Option (A).
- **Question 34**: Brown ring for nitrate (P-1); $\text{BaSO}_4$ white ppt for sulfate (Q-2); $\text{AgCl}$ curdy white for chloride (R-3); $\text{PbS}$ black ppt for sulfide (S-4). Option (A).
- **Question 35**: Nylon-6,6 from hexamethylenediamine + adipic acid (P-1); Bakelite from phenol + formaldehyde (Q-2); Dacron from glycol + terephthalic acid (R-3); Buna-S from butadiene + styrene (S-4). Option (A).
- **Question 36**: Vitamin A: night blindness (P-1); Vitamin B1: beriberi (Q-2); Vitamin C: scurvy (R-3); Vitamin D: rickets (S-4). Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Lagrange multipliers: $\nabla f = \lambda \nabla g$ at extremum. Multiplier $\lambda = \partial f^*/\partial c$. Shortest distance formula $d = |d|/\sqrt{a^2+b^2+c^2}$ derived directly. Can be applied to general smooth functions (not only quadratic). Correct options: **(A), (B), (C)**.
- **Question 38**: Orthogonal projection operator $P$ onto subspace $V$: idempotent $P^2 = P$, symmetric $P^T = P$, eigenvalues in $\{0, 1\}$, trace equals rank equals dimension of $V$. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Confocal family: $\lambda < b^2$ gives ellipses, $b^2 < \lambda < a^2$ gives hyperbolas with identical foci $(\pm\sqrt{a^2-b^2}, 0)$. Through each point passes exactly one ellipse and one hyperbola, which intersect orthogonally. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Equation is exact: $M_y = 2x+2y = N_x$. Potential function $\phi = x^2 y + x y^2 = C$. Curve through $(1, 1)$ gives $1(1) + 1(1) = 2 \implies C = 2$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Lagrange identity holds (A). Product formula $(\vec{a}\times\vec{b})\times(\vec{c}\times\vec{d}) = [\vec{a}\ \vec{c}\ \vec{d}]\vec{b} - [\vec{b}\ \vec{c}\ \vec{d}]\vec{a}$ holds (B). Scalar triple product of cross products equals $[\vec{a}\ \vec{b}\ \vec{c}]^2$ (C). Correct options: **(A), (B), (C)**.
- **Question 42**: Derangements formula $D_n = n!\sum_{k=0}^n \frac{(-1)^k}{k!}$. Recurrence $D_n = (n-1)(D_{n-1}+D_{n-2})$ and $D_n = n D_{n-1} + (-1)^n$. Values: $D_1=0, D_2=1, D_3=2, D_4=9, D_5=44$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: $I = \int_0^1 x^3(1-x)^4 dx = B(4, 5) = \frac{\Gamma(4)\Gamma(5)}{\Gamma(9)} = \frac{3! \times 4!}{8!} = \frac{6 \times 24}{40320} = \frac{144}{40320} = \frac{1}{280}$. Thus $m = 280$.
- **Question 44**: $y = e^{2x} \implies \frac{dy}{dx} = 2e^{2x}$. At $x=0$, tangent slope $m_T = 2$. Normal slope $m_N = -1/2 = -0.50$. Absolute magnitude is $0.50$.
- **Question 45**: Distance between parallel planes $2x - y + 2z = 4$ and $2x - y + 2z = 13$: $d = \frac{|13 - 4|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{9}{\sqrt{9}} = \frac{9}{3} = 3.00$.
- **Question 46**: Infinite GP: $a = 5, r = 1/3$. $S = \frac{a}{1-r} = \frac{5}{1 - 1/3} = \frac{5}{2/3} = 7.50$.
- **Question 47**: $\binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$.
- **Question 48**: $\det\begin{pmatrix} 7 & 4 \\ 3 & 2 \end{pmatrix} = 7(2) - 4(3) = 14 - 12 = 2.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Director circle: Parabola is directrix line (P-1); Ellipse is $x^2+y^2=a^2+b^2$ (Q-2); Hyperbola is $x^2+y^2=a^2-b^2$ (R-3); Rectangular hyperbola is point circle at origin (S-4). Option (A).
- **Question 50**: Rolle: $f'(c)=0$ (P-1); LMVT: $f'(c)=\frac{f(b)-f(a)}{b-a}$ (Q-2); Cauchy: $\frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)}$ (R-3); Darboux: intermediate value for derivatives (S-4). Option (A).
- **Question 51**: Separable variables (P-1); Linear ODE integrating factor (Q-2); Exact potential function (R-3); Clairaut equation (S-4). Option (A).
- **Question 52**: Rotation matrix (P-1); Reflection matrix (Q-2); Projection matrix (R-3); Scaling matrix (S-4). Option (A).
- **Question 53**: Poisson ratio = 1 (P-1); Binomial ratio < 1 (Q-2); Geometric ratio > 1 (R-3); Degenerate ratio = 0 (S-4). Option (A).
- **Question 54**: Ellipsoid (P-1); Hyperboloid of 1 sheet (Q-2); Hyperboloid of 2 sheets (R-3); Elliptic paraboloid (S-4). Option (A).
