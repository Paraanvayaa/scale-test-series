# Detailed Pedagogical Solutions — Mock Examination 03 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Electromagnetic Induction, Thomson's Jumping Ring Effect, Mutual Inductance, Phase Shift in RL Circuits ($\tan\phi = \omega L / R_0$).
- **2. Derivation**:
  - The magnetic field of the solenoid is $B_z(t) = B_0 \sin(\omega t)$.
  - The induced EMF in the ring is $\mathcal{E}(t) = -\frac{d\Phi}{dt} = -\omega \Phi_0 \cos(\omega t)$.
  - The ring has resistance $R_0$ and self-inductance $L$, so its impedance is $Z = \sqrt{R_0^2 + \omega^2 L^2}$, and current lags EMF by $\phi = \tan^{-1}\left(\frac{\omega L}{R_0}\right)$. (A) is correct.
  - The current is $I_{\text{ring}}(t) = I_{\text{ind}} \cos(\omega t - \phi)$.
  - The vertical force on the ring arises from the radial field component $B_r$: $F_z(t) = -2\pi r I_{\text{ring}}(t) B_r(t)$.
  - Time average: $\langle F_z \rangle \propto -\langle \cos(\omega t - \phi)\sin(\omega t) \rangle = \frac{1}{2}\sin\phi = \frac{1}{2}\frac{\omega L}{\sqrt{R_0^2 + \omega^2 L^2}}$.
  - If $L = 0 \implies \phi = 0 \implies \sin\phi = 0 \implies \langle F_z \rangle = 0$. (B) is correct.
  - Because $L > 0$, $\sin\phi > 0$, producing a steady repulsive time-averaged upward force $\langle F_z \rangle > 0$. (C) is correct.
  - Lowering temperature decreases $R_0$, increasing $\sin\phi \to 1$ and increasing current, producing stronger repulsion and higher levitation. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Rolling without Slipping on Curvilinear Surfaces, Work-Energy Theorem, Centripetal Acceleration.
- **2. Derivation**:
  - Distance of sphere's CM from bowl center: $R_{\text{eff}} = 5R - R = 4R$. (A) is correct.
  - Equation of motion along tangent: $M g \sin\theta - f_s = M a_c$.
  - About CM: $f_s R = I \alpha = \left(\frac{2}{5}M R^2\right)\alpha \implies f_s = \frac{2}{5}M a_c$.
  - Thus $M g \sin\theta - \frac{2}{5}M a_c = M a_c \implies a_c = \frac{5}{7}g \sin\theta \implies \alpha = \frac{a_c}{R} = \frac{5g\sin\theta}{7R}$. (B) is correct.
  - Conservation of energy to bottommost point ($\theta = 0$):
    $$M g (4R) = \frac{1}{2}M v^2 + \frac{1}{2}I \omega^2 = \frac{7}{10}M v^2 \implies v^2 = \frac{40}{7}g R \implies v = \sqrt{\frac{40}{7}g R}$$
    (C) is correct.
  - Normal force at the bottom:
    $$N - M g = M \frac{v^2}{R_{\text{eff}}} = M \frac{\frac{40}{7}g R}{4R} = \frac{10}{7}M g \implies N = M g + \frac{10}{7}M g = \frac{17}{7}M g$$
    (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Relativistic Kinematics, Doppler Shift of Photons, Conservation of Four-Momentum.
- **2. Derivation**:
  - Lorentz factor: $\gamma = \frac{1}{\sqrt{1 - 0.8^2}} = \frac{1}{0.6} = \frac{5}{3} \approx 1.667$. (A) is correct.
  - Relativistic Doppler shift for collinear decay:
    $$E_1 = \frac{1}{2} m_\pi c^2 \sqrt{\frac{1 + 0.8}{1 - 0.8}} = \frac{1}{2}(135)\sqrt{\frac{1.8}{0.2}} = \frac{135}{2}\sqrt{9} = \frac{135 \times 3}{2} = 202.5\text{ MeV}$$
    (B) is correct.
    $$E_2 = \frac{1}{2} m_\pi c^2 \sqrt{\frac{1 - 0.8}{1 + 0.8}} = \frac{135}{2}\sqrt{\frac{1}{9}} = \frac{135}{6} = 22.5\text{ MeV}$$
    (C) is correct.
  - Product: $E_1 E_2 = (202.5)(22.5) = 4556.25\text{ MeV}^2 = \frac{1}{4}(135)^2$. This is an invariant! (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Polarization in Dielectrics, Bound Charges ($\rho_b = -\nabla \cdot \vec{P}$, $\sigma_b = \vec{P} \cdot \hat{n}$).
- **2. Derivation**:
  - $\rho_b = -\nabla \cdot \vec{P} = -\frac{1}{r^2}\frac{\partial}{\partial r}(r^2 \cdot kr) = -\frac{1}{r^2}(3k r^2) = -3k$. (A) is correct.
  - $\sigma_b = \vec{P}(R) \cdot \hat{r} = k R$. (B) is correct.
  - Total volume bound charge: $Q_b^{\text{vol}} = \rho_b \left(\frac{4}{3}\pi R^3\right) = (-3k)\left(\frac{4}{3}\pi R^3\right) = -4\pi k R^3$.
  - Total surface bound charge: $Q_b^{\text{surf}} = \sigma_b (4\pi R^2) = (k R)(4\pi R^2) = +4\pi k R^3$.
  - Net bound charge: $Q_b^{\text{net}} = -4\pi k R^3 + 4\pi k R^3 = 0$. (C) is correct.
  - Inside the sphere, by Gauss's law for total bound charge enclosed at radius $r$:
    $$\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0} \implies E(4\pi r^2) = \frac{-3k(4/3\pi r^3)}{\varepsilon_0} \implies E(r) = -\frac{kr}{\varepsilon_0}$$
    Magnitude is $\frac{kr}{\varepsilon_0}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Thermodynamic Cycles, Otto Cycle Thermal Efficiency $\eta = 1 - r^{1-\gamma}$.
- **2. Derivation**:
  - Otto cycle efficiency: $\eta = 1 - r^{1-\gamma} = 1 - 8^{1 - 1.4} = 1 - 8^{-0.40}$. (A) is correct.
  - $8^{0.40} = (2^3)^{0.4} = 2^{1.2} \approx 2.2974 \implies \eta = 1 - \frac{1}{2.2974} = 1 - 0.4353 = 0.5647 \approx 56.5\%$. (B) is correct.
  - In isochoric processes, $dV = 0 \implies dW = P dV = 0$. (C) is correct.
  - $\eta = 1 - r^{-0.4}$; as $r$ increases, $r^{-0.4}$ decreases, so efficiency increases. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Wave Optics, Fresnel Zone Plate, Multiple Focal Points.
- **2. Derivation**:
  - $r_1 = \sqrt{\lambda f} = \sqrt{(500 \times 10^{-9})(1.00)} = \sqrt{5.0 \times 10^{-7}} \approx 7.07 \times 10^{-4}\text{ m} = 0.707\text{ mm}$. (A) is correct.
  - A zone plate possesses higher-order foci at odd fractions $f_m = \frac{f}{2m-1}$ for $m = 1, 2, 3, \dots$. (B) is correct.
  - Since $f = \frac{r_1^2}{\lambda}$, focal length is inversely proportional to wavelength $\lambda$ (opposite to a conventional refractive lens). (C) is correct.
  - All open half-period zones add in phase at the primary focus, producing an intensity much higher than the unobstructed wave. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Moment of inertia of rotor: $I_s = M k^2 = (3.00)(0.10)^2 = 0.030\text{ kg}\cdot\text{m}^2$.
  Spin angular momentum: $L_s = I_s \omega_s = (0.030)(600.0) = 18.0\text{ kg}\cdot\text{m}^2/\text{s}$.
  Torque due to gravity: $\tau = M g d = (3.00)(9.80)(0.15) = 4.41\text{ N}\cdot\text{m}$.
  Precessional angular velocity: $\Omega_p = \frac{\tau}{L_s} = \frac{4.41}{18.0} = 0.245\text{ rad/s} \approx 0.25\text{ rad/s}$. Exact: `0.25`.
- **Question 8**: Two coaxial dielectric cylinders in series:
  $\frac{1}{C} = \frac{1}{2\pi\varepsilon_0 L}\left[\frac{\ln(r_2/r_1)}{\varepsilon_{r1}} + \frac{\ln(r_3/r_2)}{\varepsilon_{r2}}\right] = \frac{1}{2\pi\varepsilon_0(1.0)}\left[\frac{\ln 2}{4.0} + \frac{\ln 2}{2.0}\right] = \frac{0.693}{2\pi\varepsilon_0}\left[\frac{1}{4} + \frac{1}{2}\right] = \frac{0.693 \times 0.75}{2\pi (8.85 \times 10^{-12})} = \frac{0.51975}{5.56 \times 10^{-11}} \approx 9.35 \times 10^9\text{ F}^{-1} \implies C = \frac{1}{9.35 \times 10^9} \approx 107.0\text{ pF}$. Exact: `107.00`.
- **Question 9**: Energy radiated by inner sphere: $P_1 = \sigma (4\pi R_1^2) T_1^4$.
  Outer shell absorbs $P_1$ and radiates from both its inner and outer surfaces:
  $P_{\text{emit}} = \sigma (4\pi R_2^2) T_2^4 + \sigma (4\pi R_2^2) T_2^4 = 2 \sigma (4\pi R_2^2) T_2^4$.
  Equating: $4\pi R_1^2 T_1^4 = 2 (4\pi R_2^2) T_2^4 \implies T_2^4 = \frac{R_1^2}{2 R_2^2} T_1^4 = \frac{(0.1)^2}{2(0.2)^2} T_1^4 = \frac{1}{8} T_1^4 \implies T_2 = \frac{T_1}{8^{1/4}} = \frac{500}{1.6818} \approx 297.3\text{ K} \approx 297\text{ K}$. Exact: `297.00`.
- **Question 10**: At minimum deviation, $r_1 = A/2 = 30^\circ$. Snell's law: $\sin i = \mu \sin r_1 = 1.50 \sin 30^\circ = 0.75 \implies i = \sin^{-1}(0.75) \approx 48.59^\circ$. Exact: `48.59`.
- **Question 11**: Magnetic field at center of finite solenoid: $B = \mu_0 n I \cos\theta$.
  $n = N/L = 800/0.40 = 2000\text{ turns/m}$.
  $B = (4\pi \times 10^{-7})(2000)(2.50)(0.989) = (2\pi \times 10^{-3})(0.989) \approx 6.283 \times 0.989 \approx 6.21\text{ mT}$. Exact: `6.21`.
- **Question 12**: $e(V_1 - V_2) = hc \left(\frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right) \implies 1.60 \times 10^{-19}(1.03) = h (3.0 \times 10^8)\left(\frac{100 \times 10^{-9}}{120000 \times 10^{-18}}\right) \implies 1.648 \times 10^{-19} = h (2.50 \times 10^{14}) \implies h = \frac{1.648 \times 10^{-19}}{2.50 \times 10^{14}} = 6.59 \times 10^{-34}\text{ J}\cdot\text{s}$. Exact: `6.59`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $v_e = \sqrt{\frac{2GM}{R}} = \sqrt{\frac{2G(\frac{4}{3}\pi R^3 \rho)}{R}} = R \sqrt{\frac{8\pi G \rho}{3}} \propto R$. Doubling radius doubles escape velocity. Option (A).
- **Question 14**: Vertical height remains constant $h = l \cos\theta \implies l = \frac{h}{\cos 60^\circ} = \frac{6.0}{0.5} = 12.0\text{ cm}$. Option (A).
- **Question 15**: $\Delta \beta = 10 \log_{10}\left(\frac{I_2}{I_1}\right) = 10 \log_{10}(100) = 10(2) = 20\text{ dB}$. Option (A).
- **Question 16**: $K_\alpha = \frac{A - 4}{A} Q = \frac{234}{238}(4.27) \approx 4.20\text{ MeV}$. Option (A).
- **Question 17**: $\tan\theta_B = \frac{\mu_2}{\mu_1} = \frac{1.50}{4/3} = \frac{3/2}{4/3} = \frac{9}{8} \implies \theta_B = \tan^{-1}(9/8)$. Option (A).
- **Question 18**: Center of mass of solid hemisphere is at $y_{\text{cm}} = \frac{3}{8}R$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Jahn-Teller theorem states any non-linear molecular system in a degenerate electronic state undergoes distortion to remove degeneracy. Occurs strongly in $d^9$ ($\text{Cu}^{2+}$) and high spin $d^4$ ($\text{Cr}^{2+}$) where $e_g$ orbitals are unevenly occupied. Low spin $d^6$ ($t_{2g}^6$) has completely filled non-degenerate ground state (no distortion). Options: (A), (B), (C).
- **Question 20**: Pinacol rearrangement: protonation creates most stable carbocation. Migratory aptitude of aryl groups is enhanced by electron-donating groups: $p\text{-anisyl} > p\text{-tolyl} > \text{phenyl} > p\text{-chlorophenyl}$. Forming stable oxonium ion drives rearrangement. Options: (A), (B), (C).
- **Question 21**: Rusting involves anodic oxidation of Fe, cathodic reduction of dissolved oxygen, accelerated by electrolytes, prevented by sacrificial anode like Zn/Mg. Options: (A), (B), (C), (D).
- **Question 22**: Boyle temperature $T_B = a/Rb$ where second virial coefficient vanishes. $\text{H}_2$ and $\text{He}$ have very low inversion temperatures ($T_i < 298\text{ K}$), so $Z > 1$. High pressure gives $Z = 1 + Pb/RT$. Options: (A), (B), (C), (D).
- **Question 23**: Chromyl chloride test: solid chloride + dichromate + concentrated $\text{H}_2\text{SO}_4$ gives red $\text{CrO}_2\text{Cl}_2$ vapours, absorbed in $\text{NaOH}$ to give yellow chromate. Covalent chlorides of Hg, Ag, Pb do not respond. Options: (A), (B), (C), (D).
- **Question 24**: PHBV, Nylon-2-nylon-6, and PGA are biodegradable. Bakelite is non-biodegradable synthetic plastic. Options: (A), (B), (C).
- **Question 25**: $pOH = pK_b + \log\frac{[\text{NH}_4^+]}{[\text{NH}_4\text{OH}]} = 4.75 + \log(1) = 4.75$. $\text{pH} = 14 - 4.75 = 9.25$. Exact: `9.25`.
- **Question 26**: $\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies \ln 4 = \frac{E_a}{8.314}\left(\frac{20}{300 \times 320}\right) \implies 1.386 = \frac{E_a}{8.314}\left(\frac{20}{96000}\right) \implies E_a = \frac{1.386 \times 8.314 \times 96000}{20} = 55310\text{ J/mol} = 55.31\text{ kJ/mol}$. Exact: `55.31`.
- **Question 27**: Percentage packing efficiency of HCP lattice is $74\%$. Exact: `74.00`.
- **Question 28**: $\Delta G_3^\circ = \Delta G_1^\circ + \Delta G_2^\circ \implies -3 F E_3^\circ = -1 F E_1^\circ - 2 F E_2^\circ \implies 3 E_3^\circ = E_1^\circ + 2 E_2^\circ = 0.77 + 2(-0.44) = 0.77 - 0.88 = -0.11\text{ V} \implies E_3^\circ = -0.0367\text{ V} \approx -0.04\text{ V}$. Exact: `-0.04`.
- **Question 29**: $\Delta T_b = 80.50 - 80.10 = 0.40\text{ K}$. $\Delta T_b = K_b \frac{w_2 \times 1000}{M_2 w_1} \implies 0.40 = 2.53 \frac{3.00 \times 1000}{M_2 \times 100} = \frac{75.9}{M_2} \implies M_2 = \frac{75.9}{0.40} \approx 190\text{ g/mol}$. Exact: `190.00`.
- **Question 30**: $[\text{Fe}(\text{CN})_6]^{3-}$: $\text{Fe}^{3+}$ ($3d^5$), strong field ligand pairs up electrons giving $t_{2g}^5 e_g^0$, leaving 1 unpaired electron ($n = 1$). $\mu = \sqrt{1(3)} = \sqrt{3} \approx 1.73\text{ BM}$. Exact: `1.73`.
- **Question 31**: Any alkyl side chain containing at least one benzylic hydrogen (toluene, ethylbenzene, isopropylbenzene) is oxidized to benzoic acid by alkaline $\text{KMnO}_4$. Option (D).
- **Question 32**: In aqueous solution, the order of basicity of methylamines is secondary > primary > tertiary: $(\text{CH}_3)_2\text{NH} > \text{CH}_3\text{NH}_2 > (\text{CH}_3)_3\text{N}$. In increasing order: $(\text{CH}_3)_3\text{N} < \text{CH}_3\text{NH}_2 < (\text{CH}_3)_2\text{NH}$. Option (A).
- **Question 33**: Limestone decomposes to $\text{CaO}$, which reacts with silica to form fusible slag $\text{CaSiO}_3$. Option (A).
- **Question 34**: Maltose is a disaccharide of two $\alpha$-D-glucose units joined by an $\alpha-1,4$-glycosidic linkage. Option (A).
- **Question 35**: Molecular orbital bond orders: $\text{O}_2^{2-} = 1, \text{O}_2^- = 1.5, \text{O}_2 = 2.0, \text{O}_2^+ = 2.5$. Highest is $\text{O}_2^+$. Option (A).
- **Question 36**: Clark's method uses slaked lime $\text{Ca(OH)}_2$. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(-x) = -f(x)$ (odd). $f'(x) = \frac{1 - x^2}{(1+x^2)^2} = 0 \implies x = \pm 1$. Extrema at $\pm 1$ with values $\pm 1/2$. Range is $[-1/2, 1/2]$. Points of inflection at $x = 0, \pm\sqrt{3}$. Options: (A), (B), (C), (D).
- **Question 38**: Spectral theorem for real symmetric matrices: all eigenvalues are real, eigenvectors of distinct eigenvalues are orthogonal, orthogonally diagonalizable, positive eigenvalues imply positive definite. Options: (A), (B), (C), (D).
- **Question 39**: For $xy = c^2$: tangent is $x/t + yt = 2c$. Axis intercepts are $(2ct, 0)$ and $(0, 2c/t)$. Area of triangle $= \frac{1}{2}(2ct)(2c/t) = 2c^2$ (constant). Midpoint of intercepts is $(ct, c/t) = P$. Normal equation is $xt^3 - yt - ct^4 + c = 0$. Options: (A), (B), (C), (D).
- **Question 40**: Bernoulli ODE: divide by $y^2 \implies \frac{1}{y^2}\frac{dy}{dx} + \frac{1}{xy} = \ln x$. Let $v = 1/y \implies -\frac{dv}{dx} + \frac{v}{x} = \ln x \implies \frac{dv}{dx} - \frac{v}{x} = -\ln x$. Integrating factor: $e^{\int -dx/x} = 1/x$. Solution: $\frac{v}{x} = -\int \frac{\ln x}{x}dx = -\frac{(\ln x)^2}{2} + C$. Options: (A), (B).
- **Question 41**: $\vec{a} \times \vec{b} = \vec{c} \implies \vec{c} \perp \vec{a}$ and $\vec{c} \perp \vec{b}$. Also $\vec{b} \times \vec{c} = \vec{a} \implies \vec{a} \perp \vec{b}$. Thus all 3 are mutually perpendicular. Magnitudes: $|\vec{c}| = |\vec{a}||\vec{b}|$ and $|\vec{a}| = |\vec{b}||\vec{c}| \implies |\vec{a}| = |\vec{b}|^2 |\vec{a}| \implies |\vec{b}| = 1$, and $|\vec{a}| = |\vec{c}|$. $[\vec{a}\ \vec{b}\ \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c}) = \vec{a} \cdot \vec{a} = |\vec{a}|^2$. Options: (A), (B), (C), (D).
- **Question 42**: Geometric distribution with parameter $p$: mean is $1/p$, variance is $\frac{1-p}{p^2}$, satisfies memoryless property, and $P(X \ge 3) = (1-p)^2$. Options: (A), (B), (C), (D).
- **Question 43**: Frullani's integral: $\int_0^\infty \frac{f(ax) - f(bx)}{x}dx = (f(0) - f(\infty))\ln(b/a)$. Here $f(x) = e^{-x}$, $a = 1, b = 3$. $I = (1 - 0)\ln(3/1) = \ln 3 \implies k = 3$. Exact: `3.00`.
- **Question 44**: Total area of ellipse $= \pi a b = \pi(4)(3) = 12\pi$. Area in first quadrant $= \frac{12\pi}{4} = 3\pi$. Divided by $\pi$, the answer is 3. Exact: `3.00`.
- **Question 45**: Strictly positive integers: $x \ge 1, y \ge 1$. $x + y < 10 \implies x + y \le 9$. For each $x \in \{1, 2, \dots, 8\}$, $y \in \{1, \dots, 9-x\}$. Total points $= \sum_{x=1}^8 (9 - x) = 8 + 7 + \dots + 1 = \frac{8 \times 9}{2} = 36$. Exact: `36.00`.
- **Question 46**: Distance $d = \frac{|3(2) - 4(3) + 12(-1) - 7|}{\sqrt{3^2 + (-4)^2 + 12^2}} = \frac{|6 - 12 - 12 - 7|}{\sqrt{9 + 16 + 144}} = \frac{|-25|}{\sqrt{169}} = \frac{25}{13} \approx 1.92$. Exact: `1.92`.
- **Question 47**: Telescoping series: $\frac{1}{n(n+1)(n+2)} = \frac{1}{2}\left[\frac{1}{n(n+1)} - \frac{1}{(n+1)(n+2)}\right]$. Sum $= \frac{1}{2}\left(\frac{1}{1 \times 2}\right) = \frac{1}{4} \implies m = 4$. Exact: `4.00`.
- **Question 48**: Non-negative integer solutions to $x_1 + x_2 + x_3 + x_4 = 6$: stars and bars formula $\binom{n + k - 1}{k - 1} = \binom{6 + 4 - 1}{4 - 1} = \binom{9}{3} = \frac{9 \times 8 \times 7}{6} = 84$. Exact: `84.00`.
- **Question 49**: Distance from origin: $d = \frac{|-14|}{\sqrt{2^2 + 3^2 + 6^2}} = \frac{14}{\sqrt{4 + 9 + 36}} = \frac{14}{7} = 2$. Option (A).
- **Question 50**: Circulant matrix determinant $= -(1 + \omega + \omega^2)(1 - \omega)(1 - \omega^2) = 0$ because $1 + \omega + \omega^2 = 0$. Option (A).
- **Question 51**: Length of tangent $= \sqrt{S_1} = \sqrt{7^2 + 1^2 - 4(7) - 6(1) - 12} = \sqrt{49 + 1 - 28 - 6 - 12} = \sqrt{4} = 2$ (or 4 for center distance). Let's verify: $S_1 = 50 - 46 = 4 \implies \sqrt{4} = 2$.
- **Question 52**: Curves $y = x^2 \implies y' = 2x = 2$; $x = y^2 \implies y' = \frac{1}{2y} = 1/2$. $\tan\theta = \left|\frac{2 - 1/2}{1 + 2(1/2)}\right| = \left|\frac{3/2}{2}\right| = \frac{3}{4} \implies \theta = \tan^{-1}(3/4)$. Option (A).
- **Question 53**: $S = \frac{a}{1 - r} = \frac{1}{1 - 2/3} = \frac{1}{1/3} = 3$. Option (A).
- **Question 54**: Maximum value $= \sqrt{3^2 + 4^2} + 5 = 5 + 5 = 10$. Option (A).
