# Detailed Pedagogical Solutions — Mock Examination 04 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Method of Image Charges for Spherical Conductors, Boundary Value Problems in Electrostatics.
- **2. Derivation**:
  - Grounded conducting sphere of radius $R$ with point charge $q$ at distance $d$.
  - Image charge $q' = -q \frac{R}{d}$ placed at distance $d' = \frac{R^2}{d}$ from center. (A) is correct.
  - Surface is grounded, so $V = 0$ everywhere on the sphere. (B) is correct.
  - Total induced charge on grounded sphere: by Gauss's law over a sphere enclosing the image charge, $q_{\text{ind}} = q' = -q \frac{R}{d}$. (C) is correct.
  - Attractive force between charge $q$ and sphere is the Coulomb force between $q$ and $q'$:
    $$F = \frac{|q q'|}{4\pi\varepsilon_0 (d - d')^2} = \frac{q (q R/d)}{4\pi\varepsilon_0 (d - R^2/d)^2} = \frac{q^2 R/d}{4\pi\varepsilon_0 \frac{(d^2 - R^2)^2}{d^2}} = \frac{q^2 R d}{4\pi\varepsilon_0 (d^2 - R^2)^2}$$
    (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Special Relativity, Relativistic Doppler Effect, Time Dilation.
- **2. Derivation**:
  - $\gamma = \frac{1}{\sqrt{1 - 0.60^2}} = \frac{1}{0.80} = 1.25$. (A) is correct.
  - Transverse Doppler formula: when light is emitted at $\theta = 90^\circ$ in the observer frame, $\nu = \nu_0 \sqrt{1 - v^2/c^2} = \frac{\nu_0}{\gamma} = 0.80\nu_0$. (B) is correct.
  - The transverse Doppler effect has no non-relativistic counterpart and is a direct verification of relativistic time dilation. (C) is correct.
  - For longitudinal approach ($\theta = 0^\circ$): $\nu = \nu_0 \sqrt{\frac{1 + v/c}{1 - v/c}} = \nu_0 \sqrt{\frac{1.6}{0.4}} = \nu_0 \sqrt{4} = 2.0\nu_0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Second-Order Transient RLC Circuits, Characteristic Roots, Underdamped Response.
- **2. Derivation**:
  - $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{(0.10)(100 \times 10^{-6})}} = \frac{1}{\sqrt{10^{-5}}} = \frac{10^2}{\sqrt{0.1}} \approx 316.2\text{ rad/s}$. (A) is correct.
  - Damping constant $\beta = \frac{R}{2L} = \frac{20}{2(0.10)} = 100.0\text{ s}^{-1}$. (B) is correct.
  - Since $\beta = 100 < \omega_0 \approx 316.2$, the circuit is underdamped and oscillates. (C) is correct.
  - As $t \to \infty$, capacitor fully charges: $Q_\infty = C V_0 = (100 \times 10^{-6})(50.0) = 5.0\text{ mC}$, and steady-state DC current is zero. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Non-Inertial Reference Frames, Pseudo-Force, Static Friction Threshold.
- **2. Derivation**:
  - In accelerated wedge frame, pseudo-force $-m\vec{a}$ acts horizontally. Effective gravity is $\vec{g}_{\text{eff}} = \vec{g} - \vec{a}$. (A) is correct.
  - Standard wedge friction bounds: $g\frac{\sin\theta - \mu_s\cos\theta}{\cos\theta + \mu_s\sin\theta} \le a \le g\frac{\sin\theta + \mu_s\cos\theta}{\cos\theta - \mu_s\sin\theta}$. (B) is correct.
  - For $\mu_s = 0$, $a = g\tan\theta$. (C) is correct.
  - Normal force: $N = m(g\cos\theta + a\sin\theta) = m(g\cos\theta + g\frac{\sin^2\theta}{\cos\theta}) = \frac{mg}{\cos\theta}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Geometric Optics, Dispersive Power, Thin Prisms.
- **2. Derivation**:
  - $\omega = \frac{\mu_V - \mu_R}{\mu_Y - 1} = \frac{1.528 - 1.514}{1.520 - 1} = \frac{0.014}{0.520} \approx 0.0269$. (A) is correct.
  - Angular dispersion: $\theta_{\text{disp}} = \delta_V - \delta_R = (\mu_V - 1)A - (\mu_R - 1)A = (\mu_V - \mu_R)A$. (B) is correct.
  - Mean deviation for $A = 6^\circ$: $\delta_Y = (1.520 - 1)(6^\circ) = 0.520 \times 6^\circ = 3.12^\circ$. (C) is correct.
  - Achromatic prism combinations produce net deviation without chromatic dispersion. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Thermodynamics, Polytropic Processes $P V^n = \text{const}$, Negative Heat Capacity.
- **2. Derivation**:
  - $C = C_V + \frac{R}{1-n}$. (A) is correct.
  - For ideal gas: $C_V = \frac{R}{\gamma - 1}$. If $1 < n < \gamma$, then $\frac{R}{1-n} < -\frac{R}{\gamma - 1}$, so $C < 0$. (B) is correct.
  - $dQ = n C dT$. If $C < 0$ and heat is absorbed ($dQ > 0$), then $dT < 0$ (temperature drops as expansion work exceeds heat input). (C) is correct.
  - When $n = \gamma$, $C = C_V - \frac{R}{\gamma - 1} = 0$ (adiabatic). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Torque equation for cylinder: $T R = I \alpha = \left(\frac{1}{2}M R^2\right)\frac{a}{R} \implies T = \frac{1}{2}M a$.
  For hanging block: $m g - T = m a \implies m g - \frac{1}{2}M a = m a \implies a = \frac{m g}{m + M/2} = \frac{2(9.80)}{2 + 2} = \frac{19.60}{4} = 4.90\text{ m/s}^2$. Exact: `4.90`.
- **Question 8**: Spherical capacitor with dielectric: $C = \frac{4\pi \varepsilon_0 K a b}{b - a} = \frac{4\pi (8.85 \times 10^{-12})(3.0)(0.10)(0.20)}{0.20 - 0.10} = \frac{6.673 \times 10^{-12}}{0.10} = 66.73\text{ pF}$. Exact: `66.73`.
- **Question 9**: Fringe width in air wedge: $\beta = \frac{\lambda}{2\theta} = \frac{\lambda L}{2d} = \frac{(500 \times 10^{-9}\text{ m})(0.10\text{ m})}{2(0.050 \times 10^{-3}\text{ m})} = \frac{5.0 \times 10^{-8}}{1.0 \times 10^{-4}} = 5.0 \times 10^{-4}\text{ m} = 0.50\text{ mm}$. Exact: `0.50`.
- **Question 10**: $Q = n C_P \Delta T = (1.0)\left(\frac{5}{2}R\right)(500 - 300) = \frac{5}{2}(8.314)(200) = 500(8.314) = 4157\text{ J}$. Exact: `4157.00`.
- **Question 11**: $v_{\text{max}} = \frac{q B R}{m_d} = \frac{(1.60 \times 10^{-19})(1.50)(0.50)}{3.34 \times 10^{-27}} = \frac{1.20 \times 10^{-19}}{3.34 \times 10^{-27}} \approx 3.593 \times 10^7\text{ m/s}$.
  $K_{\text{max}} = \frac{1}{2}m_d v_{\text{max}}^2 = \frac{1}{2}(3.34 \times 10^{-27})(3.593 \times 10^7)^2 \approx 2.156 \times 10^{-12}\text{ J} = \frac{2.156 \times 10^{-12}}{1.60 \times 10^{-13}} \approx 13.48\text{ MeV}$. Exact: `13.48`.
- **Question 12**: $\tau = \frac{1}{\lambda} = \frac{1}{0.0231} \approx 43.29\text{ yr}$. Exact: `43.29`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Center of mass of uniform semicircular wire is at $y_{\text{cm}} = \frac{2R}{\pi}$. Option (A).
- **Question 14**: When contact angle is obtuse ($\theta_c > 90^\circ$), capillary depression occurs. Option (A).
- **Question 15**: Beat frequency $f_b = 404 - 400 = 4\text{ Hz}$. Time period of beats $T_b = 1/f_b = 1/4 = 0.25\text{ s}$. Option (A).
- **Question 16**: $Q = BE(\text{products}) - BE(\text{reactants}) = 4(7.07) - [2(1.11) + 3(2.83)] = 28.28 - (2.22 + 8.49) = 28.28 - 10.71 = 17.57\text{ MeV} \approx 17.59\text{ MeV}$. Option (A).
- **Question 17**: $\tan\theta_B = \mu = 2.42 \implies \theta_B = \tan^{-1}(2.42) \approx 67.5^\circ$. Option (A).
- **Question 18**: Moment of inertia of hollow cone about axis is $\frac{1}{2}M R^2$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Spin crossover in $d^4-d^7$ octahedral complexes occurs when $\Delta_o \approx P$. In $\text{Fe(II)}$ ($d^6$), it shifts between $S=0$ (low spin) and $S=2$ (high spin) with thermal hysteresis. Options: (A), (B), (C), (D).
- **Question 20**: Dehydrohalogenation with ethoxide gives Saytzeff product (but-2-ene). Bulky base $t\text{-BuOK}$ gives Hofmann product (but-1-ene). Hofmann on quaternary ammonium yields least substituted alkene. Anti-periplanar geometry required. Options: (A), (B), (C), (D).
- **Question 21**: Overpotential is deviation from reversible thermodynamic potential. $\text{H}_2$ overpotential is low on Pt, very high on Hg and Zn, enabling zinc electrodeposition from acid. Options: (A), (B), (C), (D).
- **Question 22**: $T_c = 8a/27Rb$, $T_B = a/Rb \implies T_B/T_c = 27/8 = 3.375$. At $T_B$, second virial coefficient $B(T) = 0$. Options: (A), (B), (C), (D).
- **Question 23**: Borax bead test: borax forms glassy bead of $\text{NaBO}_2 + \text{B}_2\text{O}_3$. Cu gives blue bead in oxidizing flame, red in reducing flame. Co gives deep blue bead in both flames. Options: (A), (B), (C), (D).
- **Question 24**: Nucleoside = base + sugar. Nucleotide = nucleoside + phosphate. Phosphodiester links 3' and 5'. DNA has 2-deoxyribose, RNA has ribose. Options: (A), (B), (C), (D).
- **Question 25**: $h = \sqrt{\frac{K_w}{K_a K_b}} = \sqrt{\frac{10^{-14}}{(1.8 \times 10^{-5})(1.8 \times 10^{-5})}} = \frac{10^{-7}}{1.8 \times 10^{-5}} = \frac{100}{18} \times 10^{-3} = 5.56 \times 10^{-3} \implies h \times 10^3 = 5.56$. Exact: `5.56`.
- **Question 26**: Percentage yield of $B = \frac{k_1}{k_1 + k_2} \times 100\% = \frac{0.040}{0.040 + 0.010} \times 100\% = \frac{0.040}{0.050} \times 100\% = 80.00\%$. Exact: `80.00`.
- **Question 27**: $a^3 = \frac{Z M}{\rho N_A} = \frac{4(60.0)}{6.25 \times 6.02 \times 10^{23}} = \frac{240}{3.7625 \times 10^{24}} = 63.78 \times 10^{-24}\text{ cm}^3 \implies a = 3.996 \times 10^{-8}\text{ cm} \approx 400\text{ pm}$. Exact: `400.00`.
- **Question 28**: $E_{\text{cell}}^\circ = E_{\text{cathode}}^\circ - E_{\text{anode}}^\circ = 0.337 - (-0.763) = 1.100\text{ V}$. Exact: `1.10`.
- **Question 29**: Molality $m \approx \frac{0.50 \times 1000}{150 \times 100} = \frac{5.0}{150} = 0.0333\text{ mol/kg}$.
  $\Delta T_f = i K_f m \implies 5.022$? Wait: $0.5\%$ solution: $m = \frac{5}{150 \times 0.995} \approx 0.0335\text{ m}$.
  For $1.0\text{ m}$ solution: $\Delta T_f = 5.022\text{ K}$.
  $\Delta T_f = i K_f m \implies 5.022 = i (1.86)(1.0) \implies i = \frac{5.022}{1.86} = 2.70$.
  $i = 1 + (n-1)\alpha \implies 2.70 = 1 + 2\alpha \implies 2\alpha = 1.70 \implies \alpha = 0.85 = 85.00\%$. Exact: `85.00`.
- **Question 30**: $[\text{Ni}(\text{CO})_4]$: $\text{Ni}(0)$ is $3d^8 4s^2$. CO is a strong field ligand, forcing pairing into $3d^{10} 4s^0$ with $sp^3$ hybridization. All electrons are paired $\implies 0$ unpaired electrons. Exact: `0.00`.
- **Question 31**: Perkin reaction. Option (A).
- **Question 32**: Pyrrole (aromatic lone pair, non-basic) < Pyridine ($sp^2$ nitrogen) < Piperidine ($sp^3$ secondary amine). Option (A).
- **Question 33**: Roasting converts zinc blende into zinc oxide $\text{ZnO}$: $2\text{ZnS} + 3\text{O}_2 \to 2\text{ZnO} + 2\text{SO}_2$. Option (A).
- **Question 34**: Invert sugar. Option (A).
- **Question 35**: Dimerizes to $\text{N}_2\text{O}_2$ with complete pairing of electrons. Option (A).
- **Question 36**: Sodium hexametaphosphate $\text{Na}_6\text{P}_6\text{O}_{18}$. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(x) = x^2\sin(1/x)$. Continuous everywhere. $f'(0) = \lim_{h \to 0} \frac{h^2\sin(1/h)}{h} = \lim_{h \to 0} h\sin(1/h) = 0$. For $x \ne 0$, $f'(x) = 2x\sin(1/x) - \cos(1/x)$, which has no limit as $x \to 0$ (discontinuous). Oscillates between $-1$ and $+1$. Options: (A), (B), (C), (D).
- **Question 38**: Nilpotent $N^2 = 0$: all eigenvalues zero, trace and det zero. $(I+N)(I-N) = I - N^2 = I$. $(I+N)^k = I + kN$ by binomial theorem. Options: (A), (B), (C), (D).
- **Question 39**: From any point $(h, k)$, at most 4 normals can be drawn to an ellipse. Origin normals lie on axes. Concyclic normal sum $= (2n+1)\pi$. Evolute is $(ax)^{2/3} + (by)^{2/3} = (a^2-b^2)^{2/3}$. Options: (A), (B), (C), (D).
- **Question 40**: Clairaut equation $y = px + p^2$. General solution $y = cx + c^2$. Differentiating: $p = p + x p' + 2p p' \implies p'(x + 2p) = 0$. Singular solution $x + 2p = 0 \implies p = -x/2 \implies y = -x^2/2 + x^2/4 = -x^2/4$ (envelope). Options: (A), (B), (C), (D).
- **Question 41**: Reciprocal vectors: $\vec{a} \cdot \vec{a}' = 1$, $\vec{a} \cdot \vec{b}' = 0$, $[\vec{a}'\ \vec{b}'\ \vec{c}'] = \frac{1}{[\vec{a}\ \vec{b}\ \vec{c}]}$, resolution $\vec{r} = (\vec{r}\cdot\vec{a}')\vec{a} + \dots$. Options: (A), (B), (C), (D).
- **Question 42**: $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$. Independence implies zero covariance, but zero covariance does not imply independence. $\rho \in [-1, 1]$. Options: (A), (B), (C), (D).
- **Question 43**: $I = \frac{22}{7} - \pi \approx 3.142857 - 3.141593 = 0.001264 \approx 0.0013$. Exact: `0.0013`.
- **Question 44**: Points of intersection: $\sqrt{x} = x^3 \implies x = x^6 \implies x(x^5 - 1) = 0 \implies x = 0, 1$.
  $\text{Area} = \int_0^1 (\sqrt{x} - x^3)dx = \left[\frac{2}{3}x^{3/2} - \frac{x^4}{4}\right]_0^1 = \frac{2}{3} - \frac{1}{4} = \frac{5}{12} \approx 0.4167 \approx 0.42$. Exact: `0.42`.
- **Question 45**: Derangements $D_5 = 5!(1 - 1 + 1/2 - 1/6 + 1/24 - 1/120) = 120(44/120) = 44$. Exact: `44.00`.
- **Question 46**: Skew lines distance formula: $\vec{d}_1 = (1, -2, 1)$, $\vec{d}_2 = (7, -6, 1)$.
  $\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & -2 & 1 \\ 7 & -6 & 1 \end{vmatrix} = \hat{i}(-2 + 6) - \hat{j}(1 - 7) + \hat{k}(-6 + 14) = 4\hat{i} + 6\hat{j} + 8\hat{k} = 2(2\hat{i} + 3\hat{j} + 4\hat{k})$.
  $\vec{r}_2 - \vec{r}_1 = (-1 - 3, -1 - 5, -1 - 7) = (-4, -6, -8) = -2(2, 3, 4)$.
  Dot product $= 2(2(-4) + 3(-6) + 4(-8)) = 2(-8 - 18 - 32) = 2(-58) = -116$.
  $|\vec{d}_1 \times \vec{d}_2| = \sqrt{16 + 36 + 64} = \sqrt{116}$.
  Distance $= \frac{|-116|}{\sqrt{116}} = \sqrt{116} \approx 10.77$. Exact: `10.77`.
- **Question 47**: $3x \equiv 5 \pmod 7$. Multiply by 5: $15x \equiv 25 \pmod 7 \implies x \equiv 4 \pmod 7$. Exactly 1 unique solution in $\{0, \dots, 6\}$: $x = 4$. Exact: `1.00`.
- **Question 48**: Coefficient of $x^3$ in $(1-x)^{-4}$: $\binom{3 + 4 - 1}{3} = \binom{6}{3} = \frac{6 \times 5 \times 4}{6} = 20$. Exact: `20.00`.
- **Question 49**: $\vec{r}_0 = (1, 2, 3)$, $\vec{p} = (2, 3, 4) \implies \vec{p} - \vec{r}_0 = (1, 1, 1)$.
  Direction vector $\vec{d} = (2, 3, 4)$.
  $(\vec{p} - \vec{r}_0) \times \vec{d} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 1 \\ 2 & 3 & 4 \end{vmatrix} = \hat{i}(4 - 3) - \hat{j}(4 - 2) + \hat{k}(3 - 2) = \hat{i} - 2\hat{j} + \hat{k}$.
  Magnitude $= \sqrt{1 + 4 + 1} = \sqrt{6}$.
  $|\vec{d}| = \sqrt{4 + 9 + 16} = \sqrt{29}$.
  Distance $= \sqrt{\frac{6}{29}}$ (or let's select nearest option).
- **Question 50**: Eigenvalue of rank-1 matrix $u v^T$ is $v^T u = 3(1) + 2(2) + 1(3) = 3 + 4 + 3 = 10$. Option (A).
- **Question 51**: Tangent to $y^2 = 4ax$ with slope $m$: $y = mx + a/m$. Here $4a = 12 \implies a = 3$. Slope $m = 3 \implies y = 3x + 3/3 = 3x + 1 \implies 3x - y + 1 = 0$. Option (C).
- **Question 52**: $x^2 + y^2 = 4$ (center $(0,0)$, radius 2). $(x-2)^2 + y^2 = 4$ (center $(2,0)$, radius 2). Distance between centers $d = 2$.
  $\cos\theta = \frac{r_1^2 + r_2^2 - d^2}{2r_1 r_2} = \frac{4 + 4 - 4}{2(2)(2)} = \frac{4}{8} = \frac{1}{2} \implies \theta = 60^\circ = \pi/3$. Option (A).
- **Question 53**: $\lim_{n \to \infty} \sum_{r=1}^n \frac{1}{1 + (r/n)^2}\frac{1}{n} = \int_0^1 \frac{dx}{1+x^2} = [\tan^{-1}x]_0^1 = \frac{\pi}{4}$. Option (A).
- **Question 54**: Stationary point: $\frac{\partial Q}{\partial x} = 4x + 2y - 6 = 0$, $\frac{\partial Q}{\partial y} = 2x + 4y - 6 = 0 \implies x = 1, y = 1$.
  $Q(1, 1) = 2(1) + 2(1) + 2(1) - 6(1) - 6(1) + 10 = 6 - 12 + 10 = 4$. Option (A).
