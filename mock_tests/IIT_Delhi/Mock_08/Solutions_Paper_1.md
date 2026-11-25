# Detailed Pedagogical Solutions — Mock Examination 08 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Electromagnetic Induction in Rotating Systems, Conservation of Canonical Angular Momentum.
- **2. Derivation**:
  - Faraday's law gives $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi}{dt} \implies E_\theta(2\pi R) = -\pi R^2 \frac{dB}{dt} \implies E_\theta = -\frac{R}{2}\frac{dB}{dt}$. (A) is correct.
  - Torque on cylinder: $\tau = \int R dF = R(\sigma 2\pi R L)E_\theta = -R^2 \sigma \pi R L \frac{dB}{dt}$.
  - Angular acceleration: $I \frac{d\omega}{dt} = \tau$. With $I = M R^2$: $M R^2 \frac{d\omega}{dt} = -\pi \sigma L R^3 \frac{dB}{dt}$.
  - Integrating from $B_0$ to $0$: $M \omega_f = \pi \sigma L R B_0 \implies \omega_f = \frac{\pi \sigma L R B_0}{M} = \frac{\sigma B_0}{M/(\pi R L)}$. (B) is correct with area geometry.
  - Angular momentum conservation includes field angular momentum $\vec{L}_{\text{EM}} = \varepsilon_0 \int \vec{r} \times (\vec{E} \times \vec{B}) dV$. (C) is correct.
  - By Meissner/fluxoid quantization in superconductors, total flux is conserved. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Nonlinear LC Oscillations, Energy Conservation.
- **2. Derivation**:
  - For $V \ll V_0$, $C(V) \approx C_0$, yielding standard harmonic frequency $\omega_0 = 1/\sqrt{L C_0}$. (A) is correct.
  - As amplitude grows, effective capacitance changes during cycle, altering period. (B) is correct.
  - Stored electrostatic energy $U_e = \int_0^V Q(V') dV' = \int_0^V C(V') V' dV' = \frac{2}{3}C_0 V_0^2 [(1+V/V_0)^{3/2}-1] - C_0 V_0 V$. (C) is correct.
  - In absence of resistance, total energy $E = U_e + \frac{1}{2}L I^2$ is strictly constant. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Relativistic Doppler Effect, Kepler's Third Law in Binary Systems.
- **2. Derivation**:
  - Center of mass relation $r_1 = \frac{M_2}{M_1+M_2}a$. Using Kepler's 3rd law $a^3 = \frac{G(M_1+M_2)T^2}{4\pi^2}$ gives $r_1 = [\frac{G M_2^3 T^2}{4\pi^2(M_1+M_2)^2}]^{1/3}$. (A) is correct.
  - Orbital speed $v_{1} = 2\pi r_1 / T$. (B) is correct.
  - Relativistic Doppler formula along line of sight $\lambda = \lambda_0 \sqrt{\frac{1+v/c}{1-v/c}}$. (C) is correct.
  - Mass function definition $f(M) = \frac{(M_2 \sin i)^3}{(M_1+M_2)^2} = \frac{T v_{1r,\text{max}}^3}{2\pi G}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Radial Heat Conduction with Temperature-Dependent Conductivity.
- **2. Derivation**:
  - In steady state, energy conservation requires heat flux through any spherical shell of radius $r$ to be constant: $Q = -4\pi r^2 k(T)\frac{dT}{dr}$. (A) is correct.
  - Substitute $k(T) = k_0 T_0 / T$: $Q \frac{dr}{r^2} = -4\pi k_0 T_0 \frac{dT}{T}$.
  - Integrating from $R_1$ to $R_2$: $Q\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = 4\pi k_0 T_0 \ln\left(\frac{T_1}{T_2}\right) \implies Q = \frac{4\pi k_0 T_0}{\frac{1}{R_1} - \frac{1}{R_2}}\ln\left(\frac{T_1}{T_2}\right)$. (C) is correct.
  - Temperature profile: $4\pi k_0 T_0 \ln(T_1/T(r)) = Q(1/R_1 - 1/r) \implies T(r) = T_1 (T_2/T_1)^{\frac{1/R_1 - 1/r}{1/R_1 - 1/R_2}}$. (B) is correct.
  - For constant $k$, $T(r) = A + B/r$ (linear in $1/r$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Temporal Coherence, Coherence Length, Michelson Interferometry.
- **2. Derivation**:
  - Coherence length $L_c = \frac{\lambda_0^2}{\Delta \lambda} = \frac{(600 \times 10^{-9}\text{ m})^2}{0.020 \times 10^{-9}\text{ m}} = 1.80 \times 10^{-2}\text{ m} = 1.80\text{ cm}$. (A) is correct.
  - For $|\Delta d| > L_c$, coherence is lost and fringe visibility vanishes. (B) is correct.
  - Fringe visibility $V(\Delta d)$ decays smoothly as envelope function. (C) is correct.
  - Additional path difference is $2(\mu - 1)t$, corresponding to $\Delta N = \frac{2(\mu - 1)t}{\lambda_0}$ fringes. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Rolling Without Slipping on Curved Surface, Normal Reaction and Detachment.
- **2. Derivation**:
  - Conservation of energy: $m g(R+r)(1 - \cos\theta) = \frac{1}{2}m v^2 + \frac{1}{2}I \omega^2 = \frac{1}{2}m v^2 + \frac{1}{2}\left(\frac{1}{2}mr^2\right)\left(\frac{v}{r}\right)^2 = \frac{3}{4}m v^2$.
  - Thus $v^2 = \frac{4}{3}g(R+r)(1 - \cos\theta)$, and $\ddot{\theta} = \frac{2g}{3(R+r)}\sin\theta$. (A) is correct.
  - Radial equation: $m g \cos\theta - N = \frac{m v^2}{R+r} = \frac{4}{3}mg(1 - \cos\theta) \implies N(\theta) = mg\left(\frac{7}{3}\cos\theta - \frac{4}{3}\right)$. (B) is correct.
  - Detachment occurs when $N = 0 \implies \frac{7}{3}\cos\theta_c = \frac{4}{3} \implies \cos\theta_c = \frac{4}{7}$. (C) is correct.
  - Static friction prevents slip provided $f_s \le \mu_s N$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Precession frequency $\Omega_p = \frac{\tau}{L_s} = \frac{M g d}{I_s \omega_s} = \frac{1.50 \times 9.80 \times 0.10}{0.020 \times 300.0} = \frac{1.47}{6.00} = 0.245\text{ rad/s} \approx 0.25\text{ rad/s}$.
- **Question 8**: At cut-off, electron trajectory grazes anode: $B_c = \frac{\sqrt{8 m V_a / e}}{b(1 - a^2/b^2)}$.
  $\sqrt{8 V_a / (e/m)} = \sqrt{\frac{8 \times 400}{1.76 \times 10^{11}}} = \sqrt{1.818 \times 10^{-8}} = 1.348 \times 10^{-4}\text{ T}\cdot\text{m}$.
  Denominator: $b(1 - 0.04) = 0.010 \times 0.96 = 0.0096\text{ m}$.
  $B_c = \frac{1.348 \times 10^{-4}}{0.0096} = 0.01404\text{ T} = 14.04\text{ mT}$.
- **Question 9**: Radiated thermal power $P = \varepsilon \sigma A T^4$. Surface area $A = 4\pi R^2 = 4\pi(0.05)^2 = 0.03142\text{ m}^2$.
  Mass $M = \rho \frac{4}{3}\pi R^3 = 8900 \times \frac{4}{3}\pi(0.05)^3 = 4.660\text{ kg}$.
  Heat capacity $C = M c = 4.660 \times 385 = 1794\text{ J/K}$.
  $P = 0.80 \times (5.67 \times 10^{-8}) \times 0.03142 \times (300)^4 = 1.425 \times 10^{-9} \times 8.1 \times 10^9 = 11.54\text{ W}$.
  Cooling rate $\left|\frac{dT}{dt}\right| = \frac{P}{C} = \frac{11.54}{1794} \approx 0.0064\text{ K/s} \implies 0.01\text{ K/s}$.
- **Question 10**: Numerical aperture $NA = \sqrt{n_1^2 - n_2^2} = \sqrt{1.500^2 - 1.480^2} = \sqrt{2.25 - 2.1904} = \sqrt{0.0596} \approx 0.244 \approx 0.24$.
- **Question 11**: Electric field: $E(r) = \frac{\lambda}{2\pi \varepsilon_0 \varepsilon_r(r) r} = \frac{\lambda}{2\pi \varepsilon_0 k}$.
  Potential difference: $V = \int_a^b E(r) dr = \frac{\lambda (b - a)}{2\pi \varepsilon_0 k}$.
  Capacitance per unit length: $C' = \frac{\lambda}{V} = \frac{2\pi \varepsilon_0 k}{b - a} = \frac{2\pi (8.854 \times 10^{-12})(0.020)}{0.040 - 0.010} = \frac{1.1126 \times 10^{-12}}{0.030} = 37.09\text{ pF/m}$.
- **Question 12**: Distance of closest approach: $K = \frac{1}{4\pi\varepsilon_0}\frac{(2e)(Ze)}{d_0} \implies d_0 = \frac{2 Z e^2}{4\pi\varepsilon_0 K} = \frac{2(79)(9.0 \times 10^9)(1.60 \times 10^{-19})}{5.0 \times 10^6} = \frac{2.275 \times 10^{-7}}{5.0 \times 10^6} = 4.55 \times 10^{-14}\text{ m} = 45.5\text{ fm}$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Negative Hall voltage implies negative charge carriers (electrons). $n = \frac{I B}{e t |V_H|} = \frac{(10 \times 10^{-3})(0.50)}{(1.60 \times 10^{-19})(1.0 \times 10^{-3})(2.5 \times 10^{-3})} = \frac{5.0 \times 10^{-3}}{4.0 \times 10^{-25}} = 1.25 \times 10^{22}\text{ m}^{-3} \implies$ Option (A).
- **Question 14**: Four sides of square loop each contribute $B_1 = \frac{\mu_0 I}{4\pi (L/2)}(\sin 45^\circ + \sin 45^\circ) = \frac{\mu_0 I}{2\pi L}(\sqrt{2})$. Total $B = 4 B_1 = \frac{2\sqrt{2}\mu_0 I}{\pi L}$. Option (A).
- **Question 15**: Brewster's angle $\tan\theta_B = \mu \implies \theta_B = \arctan(1.50) \approx 56.3^\circ$. Option (A).
- **Question 16**: $T_c = \frac{8a}{27Rb}$ and $T_B = \frac{a}{Rb}$. Ratio $T_c / T_B = \frac{8}{27}$. Option (A).
- **Question 17**: Total energy $E = \sqrt{p^2 c^2 + m_0^2 c^4} = 3 m_0 c^2 \implies p^2 c^2 = 8 m_0^2 c^4 \implies p = \sqrt{8} m_0 c$. $\lambda = \frac{h}{p} = \frac{h}{\sqrt{8} m_0 c} = \frac{\lambda_C}{\sqrt{8}}$. Option (A).
- **Question 18**: Moment of inertia of equilateral triangle about perpendicular axis through centroid is $I = \frac{1}{12}M a^2$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Jahn-Teller theorem states any non-linear degenerate state distorts to remove degeneracy. $d^4$ and $d^9$ octahedral show large tetragonal elongation ($z$-out). In $[\text{Cu(H}_2\text{O})_6]^{2+}$, equatorial bonds are $1.97\text{ \AA}$, axial are $2.30\text{ \AA}$. $d^3, d^6(\text{LS}), d^8$ have non-degenerate ground states ($A$ or $B$ states), showing no distortion. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: In pinacol rearrangement, carbocation forms at more substituted carbon. Migratory aptitude of aryl groups is enhanced by electron donation. Migration occurs with retention. In 1,1-diphenyl-2-methylpropane-1,2-diol, protonation occurs at diphenyl carbon, methyl migrates. Correct options: **(A), (B), (C), (D)**.
- **Question 21**: Electrode concentration cell EMF is $\frac{RT}{2F}\ln(P_1/P_2)$. Liquid junction potential depends on difference in transport numbers. $\text{KCl}$ minimizes junction potential because $t_+ \approx t_- \approx 0.50$. Standard cell potential of concentration cell is zero. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: Langmuir model assumes uniform, localized, monolayer adsorption without lateral interactions. Coverage $\theta = \frac{KP}{1+KP}$. At low $P$, $\theta \approx KP$; at high $P$, $\theta \to 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Schottky defects feature equal cation and anion vacancies, lowering density. Frenkel defects feature displaced cations into interstitials, conserving density. $\text{AgBr}$ exhibits both defects. Both increase conductivity. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Specific rotation of $\alpha\text{-D-glucose}$ is $+112^\circ$, $\beta\text{-D-glucose}$ is $+18.7^\circ$, equilibrium is $+52.7^\circ$. At equilibrium, $\beta$-anomer is $64\%$ (all equatorial). Mutarotation occurs via open chain. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: Initial: $[HA] = 0.15\text{ M}, [A^-] = 0.10\text{ M}$. Initial $\text{pH} = 4.74 + \log(0.10/0.15) = 4.74 - 0.176 = 4.564$.
  After adding $0.020\text{ mol NaOH}$: $[HA] = 0.13\text{ M}, [A^-] = 0.12\text{ M}$.
  New $\text{pH} = 4.74 + \log(0.12/0.13) = 4.74 - 0.035 = 4.705$.
  $\Delta \text{pH} = 4.705 - 4.564 = +0.14$.
- **Question 26**: $\ln(k_2/k_1) = \frac{E_a}{R}\left(\frac{T_2 - T_1}{T_1 T_2}\right) \implies 1.3863 = \frac{E_a}{8.314}\left(\frac{20}{300 \times 320}\right) = \frac{E_a}{8.314}(2.0833 \times 10^{-4}) \implies E_a = \frac{1.3863 \times 8.314}{2.0833 \times 10^{-4}} = 55.32\text{ kJ/mol}$.
- **Question 27**: For FCC lattice: $\rho = \frac{Z M}{N_A a^3}$ with $Z = 4$.
  $a^3 = \frac{4 \times 107.87}{6.022 \times 10^{23} \times 10.50} = \frac{431.48}{6.323 \times 10^{24}} = 6.824 \times 10^{-23}\text{ cm}^3 = 68.24 \times 10^{-24}\text{ cm}^3$.
  $a = (68.24)^{1/3} \times 10^{-8}\text{ cm} = 4.086 \times 10^{-8}\text{ cm} = 408.6\text{ pm}$.
- **Question 28**: $E_{\text{cell}}^\circ = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = 0.799 - (-0.763) = +1.562\text{ V} \approx 1.56\text{ V}$.
- **Question 29**: $\Pi = \frac{w}{M V} R T \implies M = \frac{w R T}{\Pi V} = \frac{(4.00 \times 10^{-3}\text{ kg})(8.314)(300)}{(2.46 \times 10^3\text{ Pa})(1.00 \times 10^{-4}\text{ m}^3)} = \frac{9.977}{0.246} = 40.56\text{ kg/mol} \approx 40.6\text{ kg/mol}$.
- **Question 30**: $\text{Cr}^{3+}$ has $d^3$ configuration ($t_{2g}^3 e_g^0$) with $n=3$ unpaired electrons. $\mu_{\text{eff}} = \sqrt{n(n+2)} = \sqrt{3(5)} = \sqrt{15} \approx 3.87\text{ BM}$.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Reimer-Tiemann reactive intermediate is neutral electrophilic dichlorocarbene ($:\text{CCl}_2$). Option (A).
- **Question 32**: All statements regarding Ellingham diagrams are thermodynamically correct. Option (D).
- **Question 33**: Aryl halides do not undergo nucleophilic substitution due to partial double-bond character of $\text{C-X}$ bond from resonance. Option (A).
- **Question 34**: $\text{XeF}_4$ has steric number 6 (4 bonding pairs, 2 lone pairs), $sp^3d^2$ hybridization, square planar shape. Option (A).
- **Question 35**: $r_n = \frac{n^2 a_0}{Z}$. For $n=1$, $r_1 = a_0/Z$. Option (A).
- **Question 36**: Teflon is polytetrafluoroethene (PTFE) from $\text{CF}_2\text{=CF}_2$. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Since $|\frac{\sin(3^n x)}{2^n}| \le \frac{1}{2^n}$ and $\sum \frac{1}{2^n} = 1 < \infty$, the Weierstrass M-test guarantees uniform convergence. Continuous everywhere. Period is $2\pi$. Maximum value bounded by $\sum 1/2^n = 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Coefficient matrix determinant $\Delta = 1(2\lambda - 6) - 1(\lambda - 3) + 1(2 - 2) = 2\lambda - 6 - \lambda + 3 = \lambda - 3$. If $\lambda \ne 3$, unique solution. If $\lambda = 3$ and $\mu = 10$, augmented matrix has rank 2 (infinitely many solutions). If $\lambda = 3$ and $\mu \ne 10$, no solution. When $\lambda = 3, \mu = 10$, $(2, 4, 0)$ satisfies all equations ($2+4+0=6, 2+8+0=10$). Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Director circle of ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ is $x^2 + y^2 = a^2 + b^2 = 16 + 9 = 25$. Radius is $5$. Chord of contact from $(5, 0)$ is $\frac{5x}{16} = 1 \implies x = 16/5 = 3.20$. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Euler equation: $x = e^t \implies \frac{d^2 y}{dt^2} - 4\frac{dy}{dt} + 4y = 0$. Roots $m = 2, 2$. $y = (C_1 + C_2 t)e^{2t} = (C_1 + C_2 \ln x)x^2$. $y(1) = C_1 = 2$. $y'(x) = C_2 x + 2(C_1 + C_2 \ln x)x \implies y'(1) = C_2 + 2C_1 = C_2 + 4 = 5 \implies C_2 = 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: $\vec{d}_1 \times \vec{d}_2 = (3\times 5 - 4\times 4, 4\times 3 - 2\times 5, 2\times 4 - 3\times 3) = (-1, 2, -1)$. $\vec{a}_2 - \vec{a}_1 = (1, 2, 2)$. Shortest distance $d = \frac{|(1, 2, 2) \cdot (-1, 2, -1)|}{\sqrt{1+4+1}} = \frac{|-1 + 4 - 2|}{\sqrt{6}} = \frac{1}{\sqrt{6}}$. Non-zero distance implies skew non-intersecting lines. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Polya urn probabilities: $P(W_1) = \frac{w}{w+b}$. $P(W_2) = P(W_1)P(W_2|W_1) + P(B_1)P(W_2|B_1) = \frac{w}{w+b}\frac{w+c}{w+b+c} + \frac{b}{w+b}\frac{w}{w+b+c} = \frac{w(w+b+c)}{(w+b)(w+b+c)} = \frac{w}{w+b}$. By induction, $P(W_n) = \frac{w}{w+b}$. $P(W_2|W_1) = \frac{w+c}{w+b+c} > \frac{w}{w+b}$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Using King's property: $I = \int_0^{\pi/2} \frac{\cos^3 x}{\cos^3 x + \sin^3 x}dx$. $2I = \int_0^{\pi/2} 1 dx = \pi/2 \implies I = \pi/4$. Thus $k = 4.00$.
- **Question 44**: $A = \begin{pmatrix} 1 & \omega & \omega^2 \\ \omega & \omega^2 & 1 \\ \omega^2 & 1 & \omega \end{pmatrix}$. Note row 2 is $\omega \times$ row 1 because $\omega(1, \omega, \omega^2) = (\omega, \omega^2, 1)$. Thus rows are linearly dependent, so $\det(A) = 0.00$.
- **Question 45**: Distance $d = \frac{|2(2) - 2(3) + (-1) + 5|}{\sqrt{2^2 + (-2)^2 + 1^2}} = \frac{|4 - 6 - 1 + 5|}{\sqrt{9}} = \frac{2}{3} \approx 0.67$.
- **Question 46**: AGP: $S = 1 + \frac{2}{2} + \frac{3}{4} + \dots$. $\frac{1}{2}S = \frac{1}{2} + \frac{2}{4} + \dots$. $\frac{1}{2}S = 1 + \frac{1}{2} + \frac{1}{4} + \dots = \frac{1}{1 - 1/2} = 2 \implies S = 4.00$.
- **Question 47**: $x y = 16 \implies y = 16/x \implies \frac{dy}{dx} = -16/x^2$. At $(4, 4)$, $\frac{dy}{dx} = -16/16 = -1$. Magnitude is $1.00$.
- **Question 48**: Intersection of $y = x^2$ and $y = 2x$: $x^2 = 2x \implies x = 0, 2$. Area $= \int_0^2 (2x - x^2)dx = [x^2 - x^3/3]_0^2 = 4 - 8/3 = 4/3$. Multiplied by 3: $3 \times (4/3) = 4.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Maclaurin expansion $e^x = 1 + x + x^2/2! + x^3/3! + \dots$. $e^x - 1 - x - x^2/2 = x^3/6 + O(x^4)$. Dividing by $x^3$ gives $1/6$. Option (A).
- **Question 50**: Angle between asymptotes is $2\theta = 60^\circ \implies \theta = 30^\circ$, where $\tan\theta = b/a = 1/\sqrt{3}$. Eccentricity $e = \sqrt{1 + b^2/a^2} = \sqrt{1 + 1/3} = \sqrt{4/3} = 2/\sqrt{3}$. Option (A).
- **Question 51**: For any odd $n \times n$ skew-symmetric matrix, $\det(A) = \det(A^T) = \det(-A) = (-1)^3 \det(A) = -\det(A) \implies 2\det(A) = 0 \implies \det(A) = 0$. Option (A).
- **Question 52**: Standard vector triple product identity is BAC-CAB: $\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$. Option (A).
- **Question 53**: $|z - 3| + |z + 3| = 10 \implies 2a = 10 \implies a = 5$. Foci at $(\pm 3, 0) \implies a e = 3 \implies e = 3/5 = 0.60$. Option (A).
- **Question 54**: Binomial sum $\sum_{k=0}^n \binom{n}{k} 3^k = (1 + 3)^n = 4^n$. Option (A).
