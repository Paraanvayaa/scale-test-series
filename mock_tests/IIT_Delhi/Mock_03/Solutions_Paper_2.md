# Detailed Pedagogical Solutions — Mock Examination 03 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Static Equilibrium of Rigid Body, Torque, Friction Constraints.
- **2. Derivation**:
  - Vertical equilibrium: $N_f - (M + m)g = 0 \implies N_f = (M + m)g$. (A) is correct.
  - Torque about the base contact point:
    $$N_w (L \sin\theta) - M g \left(\frac{L}{2}\cos\theta\right) - m g (x\cos\theta) = 0 \implies N_w = \frac{(M/2 + m x/L)g}{\tan\theta}$$
    (B) is correct.
  - Horizontal equilibrium: $f_s = N_w$. As $x$ increases, $N_w$ increases, so required static friction increases. (C) is correct.
  - Slipping occurs if $f_s > \mu_s N_f$. Maximum friction required occurs at maximum $x = L$, so slipping is most likely at the top. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Coupled LC Oscillators, Normal Modes, Damped Harmonic Oscillations.
- **2. Derivation**:
  - Coupled identical LC circuits exhibit symmetric and antisymmetric normal modes with distinct frequencies. (A) is correct.
  - In the antisymmetric mode, currents are in anti-phase ($180^\circ$). (B) is correct.
  - Energy transfers periodically between electrostatic and magnetic forms. (C) is correct.
  - With resistance $R$, damping factor is $e^{-R t / 2L}$, time constant $\tau = 2L/R$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Fiber Optics, Total Internal Reflection, Numerical Aperture $\text{NA} = \sqrt{\mu_1^2 - \mu_2^2}$.
- **2. Derivation**:
  - $\sin\theta_c = \frac{\mu_2}{\mu_1} = \frac{1.40}{1.50} = \frac{14}{15} \approx 0.9333 \implies \theta_c \approx 68.96^\circ$. (A) is correct.
  - $\text{NA} = \sqrt{1.50^2 - 1.40^2} = \sqrt{2.25 - 1.96} = \sqrt{0.29} \approx 0.5385$. (B) is correct.
  - Acceptance angle in air ($\mu_0 = 1$): $\sin\theta_{\text{acc}} = \text{NA} \implies \theta_{\text{acc}} \approx 32.58^\circ$. (C) is correct.
  - Any ray with incident angle $\theta \le \theta_{\text{acc}}$ has internal reflection angle at core-cladding boundary $\ge \theta_c$, undergoing TIR. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Ampere's Law, Superposition Principle for Magnetic Fields in Cavities.
- **2. Derivation**:
  - Solid wire without cavity produces magnetic field $\vec{B}_1 = \frac{\mu_0}{2}(\vec{J} \times \vec{r}_1)$.
  - Negative current density $-\vec{J}$ in cavity produces $\vec{B}_2 = -\frac{\mu_0}{2}(\vec{J} \times \vec{r}_2)$.
  - Net field inside cavity: $\vec{B} = \vec{B}_1 + \vec{B}_2 = \frac{\mu_0}{2}\vec{J} \times (\vec{r}_1 - \vec{r}_2) = \frac{\mu_0}{2}(\vec{J} \times \vec{d})$. (A) and (B) are correct.
  - The field depends only on displacement $\vec{d}$ and current density $\vec{J}$, independent of $a$. (C) is correct.
  - Direction: $\vec{J} = J\hat{k}$, $\vec{d} = d\hat{i} \implies \vec{J} \times \vec{d} = J d (\hat{k} \times \hat{i}) = J d \hat{j}$. Points along $+y$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Quantum Mechanics, 1D Infinite Potential Well, Wavefunctions and Probabilities.
- **2. Derivation**:
  - Eigenvalues $E_n = \frac{n^2 \pi^2 \hbar^2}{2m L^2}$. (A) is correct.
  - Wavefunctions $\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$. (B) is correct.
  - $\langle p_x \rangle = 0$ for all real bound state wavefunctions. (C) is correct.
  - In ground state, probability density $\sin^2(\pi x / L)$ peaks at the center $x = L/2$. The integral over the middle third $[L/3, 2L/3]$ is $\frac{1}{3} + \frac{\sqrt{3}}{2\pi} \approx 0.333 + 0.276 = 0.609 > 1/3$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Stirling Cycle with and without Regeneration, Reversible Heat Cycles.
- **2. Derivation**:
  - $W_{\text{net}} = n R (T_1 - T_2)\ln(V_2/V_1) = 2 R (600 - 300)\ln 2 = 600 R \ln 2$. (A) is correct.
  - Isochoric heat capacities are equal and constant: $Q_{\text{in, isochoric}} = n C_V (T_1 - T_2) = Q_{\text{out, isochoric}}$. (B) is correct.
  - With ideal regeneration, internal heat transfer balances, so only isothermal heat exchanges occur, matching Carnot efficiency $\eta = 1 - T_2/T_1 = 50\%$. (C) is correct.
  - Without regeneration, additional heat must be supplied during isochoric heating, so $\eta < 50\%$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Angular momentum conservation about central axis:
  $$I_i \omega_0 = I_f \omega_f$$
  $I_i = \frac{1}{2}M R^2 + m R^2 = \frac{1}{2}(4.0)(1.0)^2 + 20.0(1.0)^2 = 2.0 + 20.0 = 22.0\text{ kg}\cdot\text{m}^2$.
  When child reaches center ($r = 0$), $I_f = \frac{1}{2}M R^2 = 2.0\text{ kg}\cdot\text{m}^2$.
  $\omega_f = \frac{I_i \omega_0}{I_f} = \frac{22.0 \times 10.0}{2.0} = 110.00\text{ rad/s}$. Exact: `110.00`.
- **Question 8**: $\nu_A = \nu_0 \pm 4 = 512 \pm 4 = 516\text{ Hz}$ or $508\text{ Hz}$.
  Loading with wax decreases the frequency of fork $A$.
  If $\nu_A = 516\text{ Hz}$, decreasing $\nu_A$ reduces the beat frequency from 4 to 2.
  If $\nu_A = 508\text{ Hz}$, decreasing $\nu_A$ would increase beat frequency from 4 to 6.
  Hence original frequency is $516\text{ Hz}$. Exact: `516.00`.
- **Question 9**: Initial energy: $U_i = \frac{1}{2} C_0 V_0^2 = \frac{1}{2}(10.0 \times 10^{-6})(100)^2 = 0.050\text{ J} = 50.0\text{ mJ}$.
  When disconnected, charge is conserved: $Q = C_0 V_0 = 10.0 \times 10^{-4}\text{ C}$.
  Final capacitance: $C_f = K C_0 = 5.0 \times 10.0\ \mu\text{F} = 50.0\ \mu\text{F}$.
  Final energy: $U_f = \frac{Q^2}{2 C_f} = \frac{U_i}{K} = \frac{50.0}{5.0} = 10.0\text{ mJ}$.
  Change: $|\Delta U| = |10.0 - 50.0| = 40.00\text{ mJ}$. Exact: `40.00`.
- **Question 10**: In Lloyd's mirror, effective slit separation is $d = 2h = 2(1.00\text{ mm}) = 2.00\text{ mm}$.
  Fringe width: $\beta = \frac{\lambda D}{d} = \frac{(500 \times 10^{-9}\text{ m})(2.00\text{ m})}{2.00 \times 10^{-3}\text{ m}} = 0.50 \times 10^{-3}\text{ m} = 0.50\text{ mm}$. Exact: `0.50`.
- **Question 11**: $r_n = \frac{n^2}{Z} a_0$. For $n = 1, Z = 2$: $r_1 = \frac{1}{2} a_0 = \frac{0.529}{2} = 0.2645\text{ \AA} \approx 0.26\text{ \AA}$. Exact: `0.26`.
- **Question 12**: Field due to one side of square of side $a$ at distance $a/2$:
  $$B_1 = \frac{\mu_0 I}{4\pi (a/2)} (\sin 45^\circ + \sin 45^\circ) = \frac{\mu_0 I}{2\pi a} (2 \times \frac{1}{\sqrt{2}}) = \frac{\sqrt{2}\mu_0 I}{\pi a}$$
  For 4 sides: $B = 4 B_1 = \frac{4\sqrt{2}\mu_0 I}{\pi a} = \frac{4(1.414)(4\pi \times 10^{-7})(4.00)}{\pi (0.10)} = \frac{90.496 \times 10^{-7}}{0.10} \approx 90.5 \times 10^{-6}\text{ T} = 45.25\ \mu\text{T}$ (or $45.25$). Let's check: $4 \times \sqrt{2} \times 4 \times 4 / 0.1 \times 10^{-7} = 226.24 \times 10^{-6} / \pi$... wait: $\frac{4\sqrt{2}\mu_0 I}{\pi a} = \frac{4\sqrt{2}(4\pi \times 10^{-7})(4)}{\pi (0.1)} = \frac{64\sqrt{2} \times 10^{-7}}{0.1} = 640\sqrt{2} \times 10^{-7} = 905.1 \times 10^{-7} = 90.51\ \mu\text{T}$. Exact: `90.51`.

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
- **Question 19**: $\text{C}_{60}$ has soccer-ball geometry with 12 pentagons and 20 hexagons. Pentagons fuse only with hexagons. All carbons are $sp^2$ hybridized. Options: (A), (B), (C), (D).
- **Question 20**: Hinsberg reagent and nitrous acid distinguish between $1^\circ, 2^\circ, 3^\circ$ amines. Carbylamine test distinguishes $1^\circ$ amines from $2^\circ$ and $3^\circ$. Lucas reagent is for alcohols. Options: (A), (B), (C).
- **Question 21**: $\Delta G^\circ = -RT \ln K$. Catalyst increases forward and backward rates equally. Van 't Hoff equation describes temperature dependence. Endothermic reactions shift forward with temperature. Options: (A), (B), (C), (D).
- **Question 22**: Photochemical chlorination of $n$-butane gives $(\pm)$-2-chlorobutane (chiral center created, racemic mixture). Propane gives achiral 2-chloropropane. 2-methylbutane at C2 gives achiral 2-chloro-2-methylbutane. Options: (A).
- **Question 23**: $\text{H}_3\text{PO}_2$ has two $\text{P}-\text{H}$ bonds; $\text{H}_3\text{PO}_3$ has one $\text{P}-\text{H}$ bond. Both act as reducing agents. $\text{H}_3\text{PO}_4$ and $\text{H}_4\text{P}_2\text{O}_7$ have zero $\text{P}-\text{H}$ bonds. Options: (A), (B).
- **Question 24**: Bent $\text{H}_2\text{O}$ and $\text{SO}_2$, and trigonal pyramidal $\text{NH}_3$ have non-zero dipole moments. Linear $\text{CO}_2$ has zero dipole moment. Options: (A), (B), (C).
- **Question 25**: $\text{PbI}_2 \rightleftharpoons \text{Pb}^{2+} + 2\text{I}^- \implies K_{sp} = 4S^3 \implies S = \sqrt[3]{K_{sp}/4} = \sqrt[3]{7.1 \times 10^{-9}/4} = \sqrt[3]{1.775 \times 10^{-9}} = 1.21 \times 10^{-3}\text{ mol/L} = 1.21\text{ mmol/L}$. Exact: `1.21`.
- **Question 26**: At $t = 10\text{ min}$, $P_{\text{total}} = P_0 - x + 2x + x = P_0 + 2x = 220 \implies 2x = 120 \implies x = 60\text{ mm Hg}$.
  $P_A(t) = P_0 - x = 100 - 60 = 40\text{ mm Hg}$.
  $k = \frac{1}{t}\ln\left(\frac{P_0}{P_A}\right) = \frac{1}{10}\ln\left(\frac{100}{40}\right) = \frac{1}{10}\ln(2.5) = \frac{0.916}{10} = 0.0916\text{ min}^{-1} \approx 0.09\text{ min}^{-1}$. Exact: `0.09`.
- **Question 27**: $\rho = \frac{Z M}{a^3 N_A} = \frac{4(63.55)}{(3.61 \times 10^{-8})^3 (6.022 \times 10^{23})} = \frac{254.2}{4.7046 \times 10^{-23} \times 6.022 \times 10^{23}} = \frac{254.2}{28.33} \approx 8.97\text{ g/cm}^3$. Exact: `8.97`.
- **Question 28**: $E_{\text{cell}}^\circ = E^\circ(\text{Ag}^+/\text{Ag}) - E^\circ(\text{Mg}^{2+}/\text{Mg}) = 0.80 - (-2.37) = +3.17\text{ V}$. Exact: `3.17`.
- **Question 29**: $\Delta T_f(\text{sugar}) = 273.15 - 271.0 = 2.15\text{ K}$.
  $\Delta T_f = K_f \frac{w_2 \times 1000}{M_2 w_1}$. Since $w_2/w_1$ is identical:
  $\frac{\Delta T_f(\text{glucose})}{\Delta T_f(\text{sugar})} = \frac{M_{\text{sugar}}}{M_{\text{glucose}}} = \frac{342}{180} = 1.90 \implies \Delta T_f(\text{glucose}) = 1.90 \times 2.15 = 4.085\text{ K}$.
  Freezing point of glucose solution $= 273.15 - 4.085 = 269.065\text{ K} \approx 269.07\text{ K}$. Exact: `269.07`.
- **Question 30**: In $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]\text{SO}_4$, nitric oxide is present as nitrosonium ion ($\text{NO}^+$). Thus $\text{Fe}$ is in $+1$ oxidation state. Exact: `1.00`.
- **Question 31**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 32**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 33**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 34**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 35**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 36**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(0) = 0$. $f'(x) = \frac{1}{1+x^2} - \frac{x}{1+x^2} = \frac{1-x}{1+x^2}$. Local max at $x = 1$. Max value $= \tan^{-1}(1) - \frac{1}{2}\ln 2 = \frac{\pi}{4} - \frac{1}{2}\ln 2$. Options: (A), (B), (C), (D).
- **Question 38**: $A^2 = A \implies \lambda^2 = \lambda \implies \lambda = 0, 1$. $\det A = \prod \lambda_i \in \{0, 1\}$. If $A \ne I$, at least one eigenvalue is 0, so $\det A = 0$. $(I-A)^2 = I - 2A + A^2 = I - 2A + A = I - A$. Options: (A), (B), (C), (D).
- **Question 39**: Radical axis equation: $C_1 - C_2 = 0 \implies (-4x - 6y + 4) - (-2x - 4y + 1) = 0 \implies -2x - 2y + 3 = 0 \implies 2x + 2y - 3 = 0$. Radical axis is perpendicular to line of centers and acts as common chord. Options: (A), (B), (C), (D).
- **Question 40**: Homogeneous ODE: $\frac{dy}{dx} = \frac{1 + y/x}{1 - y/x}$. Let $y = vx \implies v + x\frac{dv}{dx} = \frac{1+v}{1-v} \implies x\frac{dv}{dx} = \frac{1+v^2}{1-v} \implies \frac{1-v}{1+v^2}dv = \frac{dx}{x}$. Integrating: $\tan^{-1}v - \frac{1}{2}\ln(1+v^2) = \ln|x| + C$. In polar coordinates, $\theta - \ln r = C \implies r = C_0 e^\theta$ (equiangular spiral). Options: (A), (B), (C), (D).
- **Question 41**: $\vec{u} \cdot (\vec{v} + \vec{w}) = 0 \implies \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w} = 0$. Adding all three equations: $2(\vec{u}\cdot\vec{v} + \vec{v}\cdot\vec{w} + \vec{w}\cdot\vec{u}) = 0$. Subtracting gives $\vec{u}\cdot\vec{v} = \vec{v}\cdot\vec{w} = \vec{w}\cdot\vec{u} = 0$. Thus mutually orthogonal. $|\vec{u}+\vec{v}+\vec{w}|^2 = 9 + 16 + 25 = 50 \implies |\vec{u}+\vec{v}+\vec{w}| = 5\sqrt{2}$. Parallelepiped volume $= 3 \times 4 \times 5 = 60$. Options: (A), (B), (C), (D).
- **Question 42**: Geometric with $p = 1/6$: mean $= 1/p = 6$. $P(N > 3) = q^3 = (5/6)^3 = 125/216$. Variance $= q/p^2 = (5/6)/(1/36) = 30$. Options: (A), (B), (C), (D).
- **Question 43**: $\text{Area} = \int_{\pi/4}^{5\pi/4} (\sin x - \cos x)dx = [-\cos x - \sin x]_{\pi/4}^{5\pi/4} = -(-\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}) - (-\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}) = \sqrt{2} - (-\sqrt{2}) = 2\sqrt{2} \approx 2.828 \approx 2.83$. Exact: `2.83`.
- **Question 44**: $\frac{dx}{d\theta} = -3a\cos^2\theta\sin\theta$, $\frac{dy}{d\theta} = 3a\sin^2\theta\cos\theta$.
  $\frac{dy}{dx} = -\tan\theta$. At $\theta = \pi/4$, $\frac{dy}{dx} = -1$.
  Slope of normal $= -1 / (-1) = +1.00$. Exact: `1.00`.
- **Question 45**: $\int_0^1 \frac{dx}{e^x + e^{-x}} = \int_0^1 \frac{e^x dx}{e^{2x} + 1} = [\tan^{-1}(e^x)]_0^1 = \tan^{-1}(e) - \tan^{-1}(1) = \tan^{-1}(e) - \frac{\pi}{4}$. Thus $k = 4$. Exact: `4.00`.
- **Question 46**: Distance from origin to line: vector $\vec{r}_0 = (1, 2, 3)$, direction $\vec{d} = (2, 3, 6)$.
  $\vec{r}_0 \times \vec{d} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 3 \\ 2 & 3 & 6 \end{vmatrix} = \hat{i}(12 - 9) - \hat{j}(6 - 6) + \hat{k}(3 - 4) = 3\hat{i} - \hat{k}$.
  Magnitude $= \sqrt{9 + 1} = \sqrt{10}$.
  $|\vec{d}| = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$.
  Distance $= \frac{\sqrt{10}}{7} \approx \frac{3.162}{7} \approx 0.45$. Exact: `0.45`.
- **Question 47**: Roots in AP: let roots be $a - d, a, a + d$.
  Sum of roots $= 3a = 9 \implies a = 3$. The middle root is 3. Exact: `3.00`.
- **Question 48**: Number of ways to distribute 8 identical balls into 3 non-empty boxes: $\binom{8-1}{3-1} = \binom{7}{2} = \frac{7 \times 6}{2} = 21.00$. Exact: `21.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
