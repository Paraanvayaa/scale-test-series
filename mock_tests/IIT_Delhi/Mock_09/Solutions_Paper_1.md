# Detailed Pedagogical Solutions — Mock Examination 09 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Relativistic Aberration, Beaming Effect, Doppler Transformation.
- **2. Derivation**:
  - Lorentz velocity transformation for photon with components $c_x = c\cos\theta, c_y = c\sin\theta$:
    $c_x' = \frac{c_x - v}{1 - v c_x/c^2} \implies c\cos\theta' = \frac{c\cos\theta - v}{1 - (v/c)\cos\theta} \implies \cos\theta' = \frac{\cos\theta - v/c}{1 - (v/c)\cos\theta}$. (A) is correct.
  - For $\theta = 90^\circ$, $\cos\theta = 0 \implies \cos\theta' = -v/c$. (B) is correct.
  - As $v \to c$, radiation in forward hemisphere is compressed into cone $\theta' \approx 1/\gamma$ (synchrotron beaming). (C) is correct.
  - Four-momentum transformation yields $\nu' = \nu \gamma (1 - (v/c)\cos\theta)$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Coupled Inductors, Series Combinations, Magnetic Energy.
- **2. Derivation**:
  - In series aiding, $L_{\text{eq}} = L_1 + L_2 + 2M$. (A) is correct.
  - In series opposing, $L_{\text{eq}} = L_1 + L_2 - 2M$. (B) is correct.
  - Energy $U_m = \frac{1}{2}L_1 I_1^2 + \frac{1}{2}L_2 I_2^2 \pm M I_1 I_2$. (C) is correct.
  - For $U_m \ge 0$ for all real currents, the quadratic form discriminant requires $M^2 \le L_1 L_2 \implies k \le 1$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Non-Inertial Frames, Centrifugal Force, Bifurcation Analysis.
- **2. Derivation**:
  - Outward centrifugal force: $F_{\text{cf}} = m \omega^2 r = m \omega^2 R \sin\theta$. (A) is correct.
  - Tangential equation of motion: $m R \ddot{\theta} = m \omega^2 R \sin\theta \cos\theta - m g \sin\theta = m R \sin\theta (\omega^2 \cos\theta - g/R)$.
  - For $\omega^2 \le g/R$, only $\theta = 0$ is stable. (B) is correct.
  - For $\omega^2 > g/R$, $\theta = 0$ becomes unstable, and stable equilibrium appears where $\cos\theta_0 = \frac{g}{\omega^2 R}$. (C) is correct.
  - Expanding around $\theta_0$: $\ddot{\theta} + \Omega^2 (\theta - \theta_0) = 0$ gives $\Omega = \omega\sin\theta_0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Throttling Process, Enthalpy Invariance, Joule-Thomson Inversion Curve.
- **2. Derivation**:
  - Throttling has $Q = 0, W = P_1 V_1 - P_2 V_2 \implies U_1 + P_1 V_1 = U_2 + P_2 V_2 \implies H_1 = H_2$ (isenthalpic). (A) is correct.
  - Fundamental relation $dH = T dS + V dP = C_P dT + [V - T(\partial V/\partial T)_P]dP = 0 \implies \mu_{\text{JT}} = \frac{1}{C_P}[T(\partial V/\partial T)_P - V]$. (B) is correct.
  - For van der Waals gas at low pressure: $V = \frac{RT}{P} + b - \frac{a}{RT} \implies T(\partial V/\partial T)_P - V = \frac{2a}{RT} - b$. Setting to zero gives $T_i = \frac{2a}{Rb}$. (C) is correct.
  - If $T > T_i$, $\mu_{\text{JT}} < 0$, so $dP < 0$ produces $dT > 0$ (heating). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Diffraction Grating, Resolving Power, Missing Orders.
- **2. Derivation**:
  - Principal maxima: path difference between adjacent slits is $d \sin\theta = m\lambda$. (A) is correct.
  - Width between first minima on either side gives half-width $\Delta\theta = \frac{\lambda}{N d\cos\theta}$. (B) is correct.
  - Rayleigh criterion gives chromatic resolving power $R = \lambda/\Delta\lambda = m N$. (C) is correct.
  - Missing orders: single-slit minima occur at $a \sin\theta = p \lambda$. If $d = 2a$, then $m = d\sin\theta/\lambda = 2(a\sin\theta/\lambda) = 2p$, so all even orders $m = 2, 4, 6, \dots$ vanish. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Symmetric Top Dynamics, Precession and Nutation.
- **2. Derivation**:
  - Gravitational torque: $\tau = M g l \sin\theta$. (A) is correct.
  - Steady precession rate: $\tau = \Omega_p L_s \sin\theta = \Omega_p (I_z \omega_s)\sin\theta \implies \Omega_p = \frac{M g l}{I_z \omega_s}$. (B) is correct.
  - Gyroscopic reaction torque balances gravitational torque. (C) is correct.
  - Fast nutational frequency is $\omega_n \approx \frac{I_z \omega_s}{I_x}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Angular momentum about fixed pivot: $L_i = m v_0 x = (0.50)(12.0)(0.80) = 4.80\text{ kg}\cdot\text{m}^2/\text{s}$.
  Moment of inertia after sticking: $I = \frac{1}{3}M L^2 + m x^2 = \frac{1}{3}(2.00)(1.20)^2 + (0.50)(0.80)^2 = \frac{1}{3}(2.00)(1.44) + 0.50(0.64) = 0.96 + 0.32 = 1.28\text{ kg}\cdot\text{m}^2$.
  $\omega = \frac{L_i}{I} = \frac{4.80}{1.28} = 3.75\text{ rad/s}$.
- **Question 8**: Force per unit length: $F/L = \frac{\mu_0 I^2}{2\pi d} = \frac{(4\pi \times 10^{-7})(50.0)^2}{2\pi (0.020)} = \frac{2 \times 10^{-7} \times 2500}{0.020} = \frac{5.0 \times 10^{-4}}{0.020} = 0.025\text{ N/m} = 25.00\text{ mN/m}$.
- **Question 9**: Coefficient of finesse: $F = \frac{4R_0}{(1 - R_0)^2} = \frac{4(0.90)}{(1 - 0.90)^2} = \frac{3.60}{0.01} = 360$.
- **Question 10**: Adiabatic work: $W = n C_V(T_1 - T_2) = (1)\left(\frac{5}{2} \times 8.314\right)(400.0 - 300.0) = 2.5 \times 8.314 \times 100.0 = 2078.5\text{ J}$.
- **Question 11**: Capacitance $C = \frac{\varepsilon_0 A}{d} = \frac{(8.854 \times 10^{-12})(0.040)}{2.0 \times 10^{-3}} = 1.7708 \times 10^{-10}\text{ F}$.
  Displacement current $I_d(t) = C \frac{dV}{dt} = C V_0 \omega \cos(\omega t)$.
  $I_{d,\text{peak}} = C V_0 \omega = (1.7708 \times 10^{-10})(100.0)(2\pi \times 50.0 \times 10^6) = (1.7708 \times 10^{-8})(3.1416 \times 10^8) = 5.56\text{ A} \implies 5560\text{ mA}$ (or keyed appropriately).
- **Question 12**: Activity $A_0 = \lambda N_0 = (2.00 \times 10^{-4}\text{ s}^{-1})(1.00 \times 10^{16}) = 2.00 \times 10^{12}\text{ Bq} = 2000.0\text{ GBq}$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $f = -R/2 = -20.0\text{ cm}$. Mirror formula $\frac{1}{v} + \frac{1}{u} = \frac{1}{f} \implies \frac{1}{v} - \frac{1}{30} = -\frac{1}{20} \implies \frac{1}{v} = \frac{1}{30} - \frac{1}{20} = -\frac{1}{60} \implies v = -60.0\text{ cm}$.
  $m = -v/u = -(-60)/(-30) = -2.0$. Option (A).
- **Question 14**: $\vec{F} = q(\vec{E} + \vec{v}\times\vec{B}) = \vec{0} \implies \vec{E} = -\vec{v}\times\vec{B} \implies v = E/B$ along $+\hat{i}$. Option (A).
- **Question 15**: $v_{\text{rms}} = \sqrt{\frac{3 R T}{M}} = \sqrt{\frac{3 \times 8.314 \times 300}{0.028}} = \sqrt{\frac{7482.6}{0.028}} = \sqrt{267235} \approx 517\text{ m/s}$. Option (A).
- **Question 16**: $\lambda_{\text{min}} = \frac{h c}{e V_0} = \frac{1240\text{ eV}\cdot\text{nm}}{40000\text{ eV}} = 0.031\text{ nm}$. Option (A).
- **Question 17**: Angular momentum about contact point is conserved: $M v_0 R = I_c \omega = \left(\frac{2}{5}MR^2 + MR^2\right)\frac{v}{R} = \frac{7}{5}M R v \implies v = \frac{5}{7}v_0$. Option (A).
- **Question 18**: Amplitude $A = \sqrt{3^2 + 4^2} = 5$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: 2-chlorocyclohexanone reacts via Favorskii to give methyl cyclopentanecarboxylate (ring contraction). Proceeds via cyclopropanone intermediate. Symmetrical ring opening yields stable carbanion. Non-enolizable haloketones follow quasi-Favorskii without cyclopropanone. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Tanabe-Sugano diagrams map term energies relative to ground state. $d^4-d^7$ have spin crossover at critical $\Delta_0/B$. $[\text{Fe(phen)}_3]^{2+}$ shows sharp spin transition. Exhibits bistability. Correct options: **(A), (B), (C), (D)**.
- **Question 21**: Closo has $n+1$ pairs ($2n+2$ electrons). Nido has $n+2$ pairs. Arachno has $n+3$ pairs. $\text{B}_2\text{H}_6$ has 12 valence electrons with two $3c-2e$ bridge bonds. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: BET theory models multilayer adsorption. Linear equation holds between $0.05 \le P/P_0 \le 0.35$. Slope and intercept yield monolayer capacity $V_m$ and specific surface area. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Sharpless epoxidation uses $\text{Ti(O}i\text{Pr})_4, \text{TBHP}$, and DET. (+)-DET gives $\alpha$-attack, (-)-DET gives $\beta$-attack. Catalytic dimeric Ti-tartrate complex provides asymmetric induction. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Lead-acid battery: oxidation of $\text{Pb}$ at anode to $\text{PbSO}_4$; reduction of $\text{PbO}_2$ at cathode to $\text{PbSO}_4$; $\text{H}_2\text{SO}_4$ consumed during discharge, density drops from $1.28$ to $1.15$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: Amphiprotic salt $\text{pH} = \frac{pK_{a1} + pK_{a2}}{2} = \frac{6.35 + 10.33}{2} = \frac{16.68}{2} = 8.34$.
- **Question 26**: Equilibrium: $2\text{HI} \rightleftharpoons \text{H}_2 + \text{I}_2$. Initial $1.00\text{ M}$, equilibrium $1 - 2x, x, x$.
  $K_c = \frac{x^2}{(1 - 2x)^2} = 0.020 \implies \frac{x}{1 - 2x} = 0.1414 \implies x = 0.1414 - 0.2828x \implies 1.2828x = 0.1414 \implies x = 0.11\text{ mol/L}$.
- **Question 27**: BCC lattice body diagonal: $4r = \sqrt{3}a \implies r = \frac{\sqrt{3} \times 520.0}{4} = \frac{1.732 \times 520.0}{4} = 225.2\text{ pm}$.
- **Question 28**: $E^\circ_{\text{cell}} = 0.80 - 0.34 = +0.46\text{ V}$. $\Delta G^\circ = -n F E^\circ = -2(96485)(0.46) = -88766\text{ J/mol} = -88.8\text{ kJ/mol}$.
- **Question 29**: $\Delta T_f = i K_f m \implies 1.60 = i(1.86)(0.20) = 0.372 i \implies i = \frac{1.60}{0.372} = 4.30$.
  For $\text{K}_4[\text{Fe(CN)}_6]$, $n = 5$ ions. $i = 1 + (n - 1)\alpha = 1 + 4\alpha \implies 4\alpha = 3.30 \implies \alpha = 0.825 = 82.5\%$.
- **Question 30**: In $[\text{CoCl}_4]^{2-}$, $\text{Co}^{2+}$ is $3d^7$. In tetrahedral field, splitting is $e^4 t_2^3$, having $n = 3$ unpaired electrons.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Swern oxidation uses oxalyl chloride, $\text{DMSO}$, and triethylamine. Option (A).
- **Question 32**: Spectrochemical series follows increasing ligand field strength: $\text{I}^- < \text{Br}^- < \text{Cl}^- < \text{F}^- < \text{H}_2\text{O} < \text{NH}_3 < \text{CN}^- < \text{CO}$. Option (A).
- **Question 33**: Silica acts as acidic flux to remove $\text{FeO}$ as $\text{FeSiO}_3$ slag. Option (A).
- **Question 34**: $\text{I}_3^-$ has 3 lone pairs and 2 bond pairs (steric number 5), linear geometry. Option (A).
- **Question 35**: Sucrose is a non-reducing sugar because both anomeric carbons are engaged in glycosidic linkage. Option (A).
- **Question 36**: Bakelite is synthesized from phenol and formaldehyde. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Leibniz rule: $F'(x) = e^{-(x^2)^2}\frac{d}{dx}(x^2) = 2x e^{-x^4}$. $F'(0) = 0, F''(0) = 2 > 0$ (local min). $F''(x) = 2e^{-x^4} - 8x^4 e^{-x^4} = 2e^{-x^4}(1 - 4x^4) = 0 \implies x = \pm (1/4)^{1/4}$. $\lim_{x\to\infty} F(x) = \int_0^\infty e^{-t^2}dt = \sqrt{\pi}/2$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Nilpotent matrix $N$: eigenvalues satisfy $\lambda^k = 0 \implies \lambda = 0$. Characteristic polynomial $-\lambda^3$. $\det(N) = 0, \text{tr}(N) = 0$. Inverse of $I+N$ is $I - N + N^2$ since $(I+N)(I-N+N^2) = I + N^3 = I$. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Clairaut equation $y = x p - p^2$. General solution $y = C x - C^2$ (lines). Singular solution: $x - 2p = 0 \implies p = x/2 \implies y = x(x/2) - (x/2)^2 = x^2/4$. Straight lines are tangent to this envelope. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Asymptotes: $y = \pm \frac{b}{a}x$. Product of distances from $(x_0, y_0)$ to $b x - a y = 0$ and $b x + a y = 0$ is $\frac{|b^2 x_0^2 - a^2 y_0^2|}{a^2 + b^2} = \frac{a^2 b^2}{a^2 + b^2}$. Tangent intersects asymptotes at segment whose midpoint is point of tangency. Area of formed triangle is $a b$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Reciprocal triad: $\vec{a}\cdot\vec{a}' = 1, \vec{a}\cdot\vec{b}' = 0$, volume of reciprocal triad is $1/[\vec{a}\ \vec{b}\ \vec{c}]$. Expansion formula holds. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Geometric distribution $P(X = k) = (1-p)^{k-1}p$. Mean $1/p = 6$. Variance $(1-p)/p^2 = 30$. Tail probability $P(X > 3) = (5/6)^3 = 125/216$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Frullani integral $\int_0^\infty \frac{e^{-ax} - e^{-bx}}{x}dx = \ln(b/a) = \ln(5/2) = \ln(2.50) \implies k = 2.50$.
- **Question 44**: Using AM-GM or Lagrange multipliers: $x^2 + 4y^2 \ge 2\sqrt{x^2 \cdot 4y^2} = 4xy \implies 8 \ge 4xy \implies xy \le 2.00$.
- **Question 45**: Catenary $y = 2\cosh(x/2)$. $y' = \sinh(x/2)$, $y'' = \frac{1}{2}\cosh(x/2)$. At $x = 0$, $y' = 0, y'' = 1/2$. Radius of curvature $\rho = \frac{(1 + (y')^2)^{3/2}}{|y''|} = \frac{1}{1/2} = 2.00$.
- **Question 46**: $\frac{1}{n(n+1)(n+2)} = \frac{1}{2}\left[\frac{1}{n(n+1)} - \frac{1}{(n+1)(n+2)}\right]$. Telescoping sum gives $\frac{1}{2}\left[\frac{1}{1 \times 2}\right] = \frac{1}{4} \implies k = 4.00$.
- **Question 47**: $\det(2 A^{-1}) = 2^3 \det(A^{-1}) = 8 \times \frac{1}{\det A} = \frac{8}{3} \approx 2.67$.
- **Question 48**: To be divisible by 5, the units digit must be 5 (1 choice). Remaining 3 digits chosen from $\{1, 2, 3, 4, 6\}$ (5 digits): $P(5, 3) = 5 \times 4 \times 3 = 60.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Let $L = \lim_{x\to 0}(\frac{\sin x}{x})^{1/x^2}$. $\ln L = \lim_{x\to 0}\frac{\ln(1 - x^2/6 + \dots)}{x^2} = -\frac{1}{6} \implies L = e^{-1/6}$. Option (A).
- **Question 50**: The locus of the foot of the perpendicular from either focus of an ellipse on any tangent is the auxiliary circle $x^2 + y^2 = a^2$. Option (A).
- **Question 51**: The two lines intersect (shortest distance is 0). Option (B).
- **Question 52**: $|z - i| = |z + i| \implies$ distance to $(0, 1)$ equals distance to $(0, -1)$, giving the real axis $y = 0$. Option (A).
- **Question 53**: Non-vertical lines $y = m x + c \implies y' = m \implies y'' = 0$. Option (A).
- **Question 54**: Non-negative integer solutions: $\binom{n + k - 1}{k - 1} = \binom{12 + 4 - 1}{4 - 1} = \binom{15}{3} = \frac{15 \times 14 \times 13}{3 \times 2 \times 1} = 455$. Option (A).
