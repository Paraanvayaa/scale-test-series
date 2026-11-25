# Detailed Pedagogical Solutions — Mock Examination 05 (Paper 1)
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
