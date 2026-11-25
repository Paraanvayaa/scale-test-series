# Detailed Pedagogical Solutions — Mock Examination 06 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Betatron Acceleration, Induced Electric Field from Changing Flux, Magnetic Orbit Stability.
- **2. Derivation**:
  - Faraday's Law: $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi}{dt} \implies E_\theta (2\pi R) = \frac{d\Phi}{dt} \implies E_\theta = \frac{1}{2\pi R}\frac{d\Phi}{dt}$. (A) is correct.
  - Tangential force on electron: $F_\theta = e E_\theta = \frac{e}{2\pi R}\frac{d\Phi}{dt} = \frac{dp}{dt} \implies \Delta p = \frac{e \Delta \Phi}{2\pi R}$.
  - For circular orbit: $p = e R B_{\text{orb}} \implies \Delta p = e R \Delta B_{\text{orb}}$.
  - Equating: $e R \Delta B_{\text{orb}} = \frac{e \Delta \Phi}{2\pi R} \implies \Delta \Phi = 2\pi R^2 \Delta B_{\text{orb}}$.
  - Since average field $\langle B \rangle = \frac{\Phi}{\pi R^2}$, this implies $\Delta \langle B \rangle = 2 \Delta B_{\text{orb}}$ (the famous $2:1$ Betatron rule). (B) and (C) are correct.
  - Radial and vertical stability: requires field index $0 < n < 1$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Charge Sharing between Capacitors, Joule Heat Dissipation.
- **2. Derivation**:
  - Conservation of charge: $Q_{\text{total}} = C_1 V_1 + C_2 V_2 = (C_1 + C_2) V_f \implies V_f = \frac{C_1 V_1 + C_2 V_2}{C_1 + C_2}$. (A) and (B) are correct.
  - Initial energy: $U_i = \frac{1}{2} C_1 V_1^2 + \frac{1}{2} C_2 V_2^2$.
  - Final energy: $U_f = \frac{1}{2}(C_1 + C_2) V_f^2 = \frac{1}{2}\frac{(C_1 V_1 + C_2 V_2)^2}{C_1 + C_2}$.
  - Heat dissipated: $\Delta U = U_i - U_f = \frac{1}{2}\frac{C_1 C_2}{C_1 + C_2}(V_1 - V_2)^2$. (C) is correct.
  - The total energy dissipated is completely independent of the resistance $R$ of the connecting wire (it affects only the time constant $\tau = R C_{\text{eq}}$, not the integral $\int i^2 R dt$). Thus (D) is incorrect.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Hertzian Oscillating Dipole Radiation, Larmor Formula.
- **2. Derivation**:
  - Radiated power: $P = \frac{\mu_0 p_0^2 \omega^4}{12\pi c}$. (A) is correct.
  - Power scales as $\omega^4 \propto \lambda^{-4}$ (Rayleigh scattering law). (B) is correct.
  - Angular intensity: $\frac{dP}{d\Omega} = \frac{\mu_0 p_0^2 \omega^4}{32\pi^2 c}\sin^2\theta$. (C) is correct.
  - At $\theta = 0^\circ$ and $180^\circ$, $\sin\theta = 0$, so no power is radiated along the dipole axis. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Dieterici Equation of State, Critical State Conditions.
- **2. Derivation**:
  - At critical point: $\left(\frac{\partial P}{\partial V}\right)_{T_c} = 0$ and $\left(\frac{\partial^2 P}{\partial V^2}\right)_{T_c} = 0$. (A) is correct.
  - For Dieterici gas: $V_c = 2b$, $T_c = \frac{a}{4Rb}$, $P_c = \frac{a}{4e^2 b^2}$. (B) and (C) are correct.
  - Critical compressibility factor:
    $$Z_c = \frac{P_c V_c}{R T_c} = \frac{(a / 4e^2 b^2)(2b)}{R(a / 4Rb)} = \frac{2a / 4e^2 b}{a / 4b} = \frac{2}{e^2} \approx 0.2707 \approx 0.271$$
    (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Fabry-Pérot Interferometer, Airy Transmission Function, Free Spectral Range.
- **2. Derivation**:
  - Finesse parameter: $F = \frac{4R_0}{(1 - R_0)^2}$. (A) is correct.
  - Airy formula: $T(\delta) = \frac{1}{1 + F\sin^2(\delta/2)}$. (B) is correct.
  - As $R_0 \to 1$, $F \to \infty$, making transmission resonance peaks extremely narrow. (C) is correct.
  - Free spectral range: $\Delta \nu_{\text{FSR}} = \frac{c}{2d}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Cycloidal Pendulum, Tautochrone Property, Isochronism.
- **2. Derivation**:
  - Along cycloid, component of gravity along curve is proportional to arc length $s$: $\ddot{s} + \frac{g}{4R} s = 0$.
  - This is an exact SHM equation for all amplitudes! (A) is correct.
  - Time period: $\omega = \sqrt{\frac{g}{4R}} \implies T = \frac{2\pi}{\omega} = 4\pi\sqrt{\frac{R}{g}}$. (B) is correct.
  - Invented by Christiaan Huygens for pendulum clocks. (C) is correct.
  - Geometric property of cycloid: $s^2 = 8 R y$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Moment of inertia of disk: $I = \frac{1}{2}M R^2 = \frac{1}{2}(6.00)(0.40)^2 = 0.48\text{ kg}\cdot\text{m}^2$.
  Torque: $\tau = F R = (15.0)(0.40) = 6.00\text{ N}\cdot\text{m}$.
  Angular acceleration: $\alpha = \frac{\tau}{I} = \frac{6.00}{0.48} = 12.50\text{ rad/s}^2$.
  Final angular velocity: $\omega = \alpha t = (12.50)(4.00) = 50.0\text{ rad/s}$.
  Kinetic energy: $K = \frac{1}{2}I \omega^2 = \frac{1}{2}(0.48)(50.0)^2 = 0.24(2500) = 600.00\text{ J}$. Exact: `600.00`.
- **Question 8**: Potential of inner shell:
  $$V = \frac{1}{4\pi\varepsilon_0}\left[\frac{Q_1}{R_1} + \frac{Q_2}{R_2}\right] = (9.0 \times 10^9)\left[\frac{2.0 \times 10^{-6}}{0.10} + \frac{-6.0 \times 10^{-6}}{0.30}\right] = (9.0 \times 10^9)[20.0 \times 10^{-6} - 20.0 \times 10^{-6}] = 0.00\text{ V}$$
  Exact: `0.00`.
- **Question 9**: For bright rings: $r_n^2 = (n - 1/2)\lambda R$.
  For $n = 5$: $r_5^2 = (5 - 0.5)(589 \times 10^{-9}\text{ m})(2.00\text{ m}) = (4.5)(1.178 \times 10^{-6}) = 5.301 \times 10^{-6}\text{ m}^2$.
  $r_5 = \sqrt{5.301 \times 10^{-6}} \approx 2.30 \times 10^{-3}\text{ m} = 2.30\text{ mm}$. Exact: `2.30`.
- **Question 10**: $W = n R T \ln\left(\frac{V_2}{V_1}\right) = (1.0)(8.314)(300)\ln(4) = (2494.2)(1.3863) \approx 3457.7\text{ J} \approx 3458\text{ J}$. Exact: `3458.00`.
- **Question 11**: $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi}{dt} \implies E(2\pi r) = \pi r^2 \mu_0 n \left|\frac{dI}{dt}\right|$.
  $E = \frac{1}{2}\mu_0 n r \left|\frac{dI}{dt}\right|_{\text{max}} = \frac{1}{2}(4\pi \times 10^{-7})(1000)(0.020)[4.0 \times 100\pi] = (4\pi \times 10^{-4})(0.010)(400\pi) = 16\pi^2 \times 10^{-3} \approx 16(9.87) \times 10^{-3} \approx 157.9\text{ mV/m}$. Exact: `157.91`.
- **Question 12**: $\Delta m = m_p + m_n - m_d = 1.007276 + 1.008665 - 2.013553 = 2.015941 - 2.013553 = 0.002388\text{ u}$.
  $BE = (0.002388)(931.5) \approx 2.224\text{ MeV} \approx 2.22\text{ MeV}$. Exact: `2.22`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Inside a uniform spherical shell, gravitational field is zero everywhere. Option (A).
- **Question 14**: $\Delta P = \frac{4S}{R} - \frac{Q^2}{32\pi^2\varepsilon_0 R^4}$. Option (A).
- **Question 15**: Doppler shift for approaching source: $\nu = \nu_0 \frac{v}{v - u} = 400 \frac{340}{340 - 34} = 400 \frac{340}{306} = 400 \times \frac{10}{9} \approx 444.44\text{ Hz} \approx 444\text{ Hz}$. Option (A).
- **Question 16**: Electron neutrino ($\nu_e$) is emitted. Option (A).
- **Question 17**: A half-wave plate rotates polarization by $2\theta$. To rotate by $90^\circ$, angle must be $\theta = 45^\circ$. Option (A).
- **Question 18**: Tangential axis in sphere's plane: $I = \frac{2}{5}M R^2 + M R^2 = \frac{7}{5}M R^2$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Chelate effect: polydentate complexes are more stable due to entropy increase ($\Delta S > 0$) from releasing multiple monodentate solvent molecules. $\text{EDTA}^{4-}$ is hexadentate. Macrocyclic effect confers extra stability. Options: (A), (B), (C), (D).
- **Question 20**: Beckmann rearrangement converts ketoximes to amides via anti-migration with retention of stereochemistry. Used for Nylon-6 monomer caprolactam. Options: (A), (B), (C), (D).
- **Question 21**: Passivation forms protective oxide film. Concentrated $\text{HNO}_3$ passivates Fe and Cr. Stainless steel protected by $\text{Cr}_2\text{O}_3$. Pitting by $\text{Cl}^-$. Options: (A), (B), (C), (D).
- **Question 22**: Berthelot equation has $a/TV^2$. Redlich-Kwong has $a/\sqrt{T}V(V+b)$. Both improve over van der Waals. Options: (A), (B), (C), (D).
- **Question 23**: Nitrate brown ring test forms $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$. Nitrite reacts even in dilute acid. Urea removes $\text{NO}_2^-$. $\text{I}^-$ gives violet layer in $\text{CCl}_4$. Options: (A), (B), (C), (D).
- **Question 24**: Primary (peptide sequence), secondary ($\alpha$-helix, $\beta$-sheet with H-bonds), tertiary (3D fold with disulfides and hydrophobic interactions), quaternary (multimeric subunits). Options: (A), (B), (C), (D).
- **Question 25**: Addition of $0.020\text{ mol HCl}$: $[\text{CH}_3\text{COOH}] = 0.20 + 0.02 = 0.22\text{ M}$, $[\text{CH}_3\text{COO}^-] = 0.20 - 0.02 = 0.18\text{ M}$.
  $\text{pH} = pK_a + \log\left(\frac{0.18}{0.22}\right) = 4.74 - \log(1.22) = 4.74 - 0.087 = 4.653 \approx 4.65$. Exact: `4.65`.
- **Question 26**: $\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{10}{300 \times 310}\right) \implies \ln 2 = \frac{E_a}{8.314}\left(\frac{10}{93000}\right) \implies 0.693 = \frac{E_a}{8.314}(1.075 \times 10^{-4}) \implies E_a = \frac{0.693 \times 8.314}{1.075 \times 10^{-4}} \approx 53580\text{ J/mol} = 53.58\text{ kJ/mol}$. Exact: `53.58`.
- **Question 27**: In $\text{CsCl}$ structure: $2(r_+ + r_-) = \sqrt{3}a \implies d = r_+ + r_- = \frac{\sqrt{3}a}{2} = \frac{1.732 \times 412.0}{2} = 356.8\text{ pm}$. Exact: `356.80`.
- **Question 28**: $E_{\text{cell}}^\circ = E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) - E^\circ(\text{I}_2/\text{I}^-) = +0.77 - (+0.54) = +0.23\text{ V}$. Exact: `0.23`.
- **Question 29**: Molality $m = \frac{2.00 \times 1000}{122.0 \times 25.0} = \frac{2000}{3050} \approx 0.6557\text{ m}$.
  For dimerization: $i = 1 - \alpha/2 = 1 - 0.40 = 0.60$.
  $\Delta T_f = i K_f m = (0.60)(5.12)(0.6557) \approx 2.015\text{ K} \approx 2.02\text{ K}$. Exact: `2.02`.
- **Question 30**: $[\text{Mn}(\text{CN})_6]^{3-}$: $\text{Mn}^{3+}$ ($3d^4$), strong field $\text{CN}^-$ gives $t_{2g}^4 e_g^0$, with 2 unpaired electrons ($n = 2$). $\mu = \sqrt{2(4)} = \sqrt{8} \approx 2.83\text{ BM}$. Exact: `2.83`.
- **Question 31**: Gabriel synthesis produces pure $1^\circ$ aliphatic amines. Option (A).
- **Question 32**: Cyclooctatetraene is non-planar tub-shaped (non-aromatic). Option (A).
- **Question 33**: Carbon monoxide is the main reducing agent in the upper reduction zone. Option (A).
- **Question 34**: Glycogen is structurally analogous to amylopectin. Option (A).
- **Question 35**: $\text{B}_2$ has bond order 1 ($\pi_{2p_x}^1 = \pi_{2p_y}^1$, paramagnetic). $\text{O}_2$ has bond order 2 ($\pi^*_{2p_x}^1 = \pi^*_{2p_y}^1$, paramagnetic). Option (C).
- **Question 36**: Cetyltrimethylammonium bromide is a cationic detergent. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: For convex function $f''(x) > 0$: tangent lies below curve, secants lie above curve, Jensen's inequality holds, $f'(x)$ is strictly increasing. Options: (A), (B), (C), (D).
- **Question 38**: Real symmetric positive definite matrix: all eigenvalues $> 0$, Sylvester's criterion (positive leading principal minors), invertible with positive definite inverse, unique Cholesky factorization $A = L L^T$. Options: (A), (B), (C), (D).
- **Question 39**: Common tangent to $y^2 = 4ax$ and $x^2 = 4by$: tangent to first is $y = mx + a/m$. Substituting into $x^2 = 4by$ gives $x^2 - 4b(mx + a/m) = 0$. For tangency, discriminant $= 16b^2 m^2 + 16ab/m = 0 \implies m^3 = -a/b \implies m = -(a/b)^{1/3}$. Equation: $x a^{1/3} + y b^{1/3} + a^{2/3}b^{2/3} = 0$. Options: (A), (B), (C), (D).
- **Question 40**: Cauchy-Euler equation: let $x = e^t \implies \frac{d^2y}{dt^2} - 3\frac{dy}{dt} + 2y = 0$. Roots $m = 1, 2 \implies y = C_1 x + C_2 x^2$. Initial conditions: $C_1 + C_2 = 3$, $C_1 + 2C_2 = 5 \implies C_2 = 2, C_1 = 1 \implies y = x + 2x^2$. Options: (A), (B), (C), (D).
- **Question 41**: Non-coplanar $\implies [\vec{a}\ \vec{b}\ \vec{c}] \ne 0$. Volume of sum vectors is $2[\vec{a}\ \vec{b}\ \vec{c}]$. Volume of cross vectors is $[\vec{a}\ \vec{b}\ \vec{c}]^2$. Positive triple product indicates right-handed system. Options: (A), (B), (C), (D).
- **Question 42**: Normalization: $\int_0^1 \int_0^1 c(x+y)dx dy = c(1/2 + 1/2) = c = 1$. (A) is correct.
  Marginal: $f_X(x) = \int_0^1 (x+y)dy = x + 1/2$. (B) is correct.
  $E[X] = \int_0^1 x(x + 1/2)dx = [x^3/3 + x^2/4]_0^1 = 1/3 + 1/4 = 7/12$. (C) is correct.
  $f(x, y) = x + y \ne (x + 1/2)(y + 1/2)$, so NOT independent. Thus (D) is incorrect.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**
- **Question 43**: $\int_0^1 \frac{\ln(1+x)}{x}dx = \frac{\pi^2}{12} \implies k = 12$. Exact: `12.00`.
- **Question 44**: Area $= \int_0^{\pi/2} (\sin x - \frac{2}{\pi}x)dx = [-\cos x - \frac{x^2}{\pi}]_0^{\pi/2} = (0 - \frac{\pi^2/4}{\pi}) - (-1 - 0) = 1 - \frac{\pi}{4} \approx 1 - 0.7854 = 0.2146 \approx 0.21$. Exact: `0.21`.
- **Question 45**: $2520 = 2^3 \times 3^2 \times 5^1 \times 7^1$. Total divisors $= (3+1)(2+1)(1+1)(1+1) = 4 \times 3 \times 2 \times 2 = 48$. Exact: `48.00`.
- **Question 46**: Parallel lines with direction $\vec{d} = (2, 3, 6)$. Point difference: $\vec{r}_2 - \vec{r}_1 = (3-1, 3-2, 2-3) = (2, 1, -1)$.
  $(\vec{r}_2 - \vec{r}_1) \times \vec{d} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -1 \\ 2 & 3 & 6 \end{vmatrix} = \hat{i}(6 + 3) - \hat{j}(12 + 2) + \hat{k}(6 - 2) = 9\hat{i} - 14\hat{j} + 4\hat{k}$.
  Magnitude $= \sqrt{81 + 196 + 16} = \sqrt{293} \approx 17.117$.
  $|\vec{d}| = \sqrt{4 + 9 + 36} = 7$.
  Distance $= \frac{17.117}{7} \approx 2.45$. Exact: `2.45`.
- **Question 47**: $S = \frac{1/2}{1 - 1/2} + \frac{1/4}{(1 - 1/2)^2} = 1 + 1 = 2.00$. Exact: `2.00`.
- **Question 48**: Arrange 4 men around circle in $(4-1)! = 3! = 6$ ways. This creates 4 spaces. Place 4 women in $4! = 24$ ways. Total $= 6 \times 24 = 144$. Exact: `144.00`.
- **Question 49**: Distance from $(3, -1, 11)$ to line: vector calculation gives $\sqrt{53}$. Option (A).
- **Question 50**: Trace is linear: $\text{Tr}(2A - 3B) = 2\text{Tr}(A) - 3\text{Tr}(B) = 2(5) - 3(3) = 10 - 9 = 1$. Option (A).
- **Question 51**: Tangent to $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ with slope $m$: $y = mx \pm \sqrt{a^2 m^2 - b^2}$.
  Here $a^2 = 9, b^2 = 4, m = 2 \implies a^2 m^2 - b^2 = 9(4) - 4 = 32$.
  $y = 2x \pm \sqrt{32} = 2x \pm 4\sqrt{2}$. Option (A).
- **Question 52**: At $(1, 1)$: $y = x^3 \implies y' = 3x^2 = 3$.
  $6y = 7 - x^2 \implies 6y' = -2x \implies y' = -x/3 = -1/3$.
  $m_1 m_2 = 3(-1/3) = -1 \implies$ orthogonal ($\theta = 90^\circ = \pi/2$). Option (A).
- **Question 53**: $\lim_{x \to 0} \frac{x - (x - x^3/6)}{x^3} = \frac{1}{6}$. Option (A).
- **Question 54**: $f(x) = \frac{1}{2}\sin(2x) \le \frac{1}{2}$. Option (A).
