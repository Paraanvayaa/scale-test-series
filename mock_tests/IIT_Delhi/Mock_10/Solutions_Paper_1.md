# Detailed Pedagogical Solutions — Mock Examination 10 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Relativistic Invariant Mass, Mandelstam Variable $s$, Threshold Energy.
- **2. Derivation**:
  - Invariant mass squared $s = (P_1 + P_2)^2 = (E_1 + m_p c^2)^2 - p_1^2 c^2 = E_1^2 - p_1^2 c^2 + 2 m_p c^2 E_1 + m_p^2 c^4 = 2 m_p^2 c^4 + 2 m_p c^2 E_1$. (A) is correct.
  - Substitute $E_1 = K + m_p c^2$: $s = 2m_p^2 c^4 + 2m_p c^2(K + m_p c^2) = 4m_p^2 c^4 + 2m_p c^2 K$. (B) is correct.
  - At threshold in the center-of-momentum frame, all final particles are produced at rest, requiring $\sqrt{s} = m_p c^2 + m_\Lambda c^2 + m_K c^2$. (C) is correct.
  - Equating: $4m_p^2 c^4 + 2m_p c^2 K_{\text{th}} = (m_p + m_\Lambda + m_K)^2 c^4 \implies K_{\text{th}} = \frac{(m_p + m_\Lambda + m_K)^2 c^2 - 4m_p^2 c^2}{2m_p}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Dieterici Real Gas Equation, Critical State Properties.
- **2. Derivation**:
  - Critical state satisfies $(\partial P/\partial V)_T = 0$ and $(\partial^2 P/\partial V^2)_T = 0$. (A) is correct.
  - For $P = \frac{RT}{V-b}e^{-a/RTV}$, logarithmic differentiation gives:
    $\frac{1}{P}\frac{\partial P}{\partial V} = -\frac{1}{V-b} + \frac{a}{RTV^2} = 0 \implies RTV^2 - a(V-b) = 0$.
    Setting second derivative to zero yields $V_c = 2b$. (B) is correct.
  - Substituting $V_c = 2b$ gives $RT_c(4b^2) - a b = 0 \implies T_c = \frac{a}{4Rb}$. (C) is correct.
  - Critical pressure $P_c = \frac{RT_c}{b}e^{-a/RT_c(2b)} = \frac{a}{4b^2}e^{-2} = \frac{a}{4b^2 e^2}$.
  - Critical compressibility factor $Z_c = \frac{P_c V_c}{R T_c} = \frac{(a / 4b^2 e^2)(2b)}{R(a / 4Rb)} = \frac{2}{e^2} \approx 0.271$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Torsional Oscillator, Dipole in Electric Field, Damped Oscillations.
- **2. Derivation**:
  - Restoring torque of fiber $-C\theta$ balances electric torque $p E \cos\theta = q L E \cos\theta$. (A) is correct.
  - Moment of inertia of two spheres about center: $I = 2 m (L/2)^2 = \frac{1}{2}m L^2$. Natural frequency $\omega_0 = \sqrt{\frac{C}{I}} = \sqrt{\frac{C}{\frac{1}{2}m L^2}} = \sqrt{\frac{2C}{m L^2}}$. (B) is correct.
  - Underdamping requires damping constant $\beta < \omega_0 \implies \gamma / (2I) < \sqrt{C/I} \implies \gamma < 2\sqrt{C I} = \sqrt{2m C L^2}$. (C) is correct.
  - Hookean torsion fiber produces pure harmonic motion independent of amplitude. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Diffraction Limit of Resolution, Abbe Microscope Formula, Rayleigh Criterion.
- **2. Derivation**:
  - Abbe limit of transverse resolution: $d_{\text{min}} = \frac{0.61\lambda}{n\sin\alpha} = \frac{0.61\lambda}{NA}$. (A) is correct.
  - Immersion oil increases $n$ from $1.0$ to $1.51$, increasing $NA$ and reducing $d_{\text{min}}$. (B) is correct.
  - Telescope Rayleigh criterion: $\theta_{\text{min}} = \frac{1.22\lambda}{D}$. (C) is correct.
  - Light gathering area is $\frac{\pi}{4}D^2 \propto D^2$, while angular resolution $\theta_{\text{min}} \propto 1/D$, meaning resolving power $\propto D$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Rolling Without Slipping in Concave Spherical Bowl, Energy Method.
- **2. Derivation**:
  - CM trajectory is a sphere of radius $R - r$. (A) is correct.
  - Speed of CM is $v_{\text{cm}} = (R - r)\dot{\theta}$. Rolling constraint: $v_{\text{cm}} = r\omega \implies \omega = \frac{R-r}{r}\dot{\theta}$.
  - Kinetic energy: $K = \frac{1}{2}M v_{\text{cm}}^2 + \frac{1}{2}\left(\frac{2}{5}Mr^2\right)\omega^2 = \frac{1}{2}M v_{\text{cm}}^2 + \frac{1}{5}M v_{\text{cm}}^2 = \frac{7}{10}M(R-r)^2\dot{\theta}^2$. (B) is correct.
  - Total energy $E = \frac{7}{10}M(R-r)^2\dot{\theta}^2 + M g(R-r)(1 - \cos\theta) = \text{const}$.
  - Differentiating: $\frac{7}{5}(R-r)\ddot{\theta} + g\sin\theta = 0 \implies \ddot{\theta} + \frac{5g}{7(R-r)}\theta = 0$ for small $\theta$.
  - Angular frequency $\omega = \sqrt{\frac{5g}{7(R-r)}}$. (C) is correct.
  - Period $T = 2\pi\sqrt{\frac{7(R-r)}{5g}}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Parallel LC Antiresonance, Impedance and Circulating Currents.
- **2. Derivation**:
  - Admittance of ideal parallel LC: $Y = j\omega C + \frac{1}{j\omega L} = j\left(\omega C - \frac{1}{\omega L}\right)$. (A) is correct.
  - At $\omega_0 = 1/\sqrt{LC}$, $Y = 0$, so input impedance $Z = 1/Y \to \infty$. (B) is correct.
  - For finite source voltage, zero admittance draws zero total net current from the generator. (C) is correct.
  - High circulating current flows between inductor and capacitor, exchanging energy $180^\circ$ out of phase. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Angular momentum about pivot is conserved: $L_i = I_0 \omega_0 = \left(\frac{1}{2}M R^2\right)\omega_0 = \frac{1}{2}(4.00)(0.50)^2(20.0) = 0.50(20.0) = 10.0\text{ kg}\cdot\text{m}^2/\text{s}$.
  New moment of inertia $I_f = \frac{1}{2}M R^2 + m r^2 = 0.50 + 1.00(0.30)^2 = 0.50 + 0.09 = 0.59\text{ kg}\cdot\text{m}^2$.
  $\omega_f = \frac{L_i}{I_f} = \frac{10.0}{0.59} = 16.95\text{ rad/s}$.
- **Question 8**: $C = 4\pi\varepsilon_0 \frac{a b}{b - a} = \frac{1}{9.0 \times 10^9}\frac{(0.050)(0.100)}{0.100 - 0.050} = \frac{0.0050}{9.0 \times 10^9 \times 0.050} = \frac{0.10}{9.0 \times 10^9} = 1.11 \times 10^{-11}\text{ F} = 11.1\text{ pF}$.
- **Question 9**: Virtual source separation $d = 2h = 2(1.50\text{ mm}) = 3.0\text{ mm}$.
  $\beta = \frac{\lambda D}{d} = \frac{(600 \times 10^{-9}\text{ m})(2.00\text{ m})}{3.0 \times 10^{-3}\text{ m}} = \frac{1.20 \times 10^{-6}}{3.0 \times 10^{-3}} = 0.40 \times 10^{-3}\text{ m} = 0.40\text{ mm}$.
- **Question 10**: Isothermal entropy change: $\Delta S = n R \ln(P_1/P_2) = (1)(8.314)\ln(4.0) = 8.314 \times 1.3863 = 11.53\text{ J/(mol}\cdot\text{K)}$.
- **Question 11**: $\lambda = \frac{12.27}{\sqrt{150.0}}\text{ \AA} = \frac{12.27}{12.247}\text{ \AA} \approx 1.00\text{ \AA}$.
- **Question 12**: $K_{\text{max}} = h(\nu - \nu_0) = (6.626 \times 10^{-34})(1.0 \times 10^{15} - 6.0 \times 10^{14}) = (6.626 \times 10^{-34})(4.0 \times 10^{14}) = 2.650 \times 10^{-19}\text{ J}$.
  In $\text{eV}$: $K_{\text{max}} = \frac{2.650 \times 10^{-19}}{1.60 \times 10^{-19}} = 1.66\text{ eV}$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $x(t) = A\sin(\omega t)$. $A/2 = A\sin(\omega t) \implies \omega t = \pi/6 \implies \frac{2\pi}{T}t = \frac{\pi}{6} \implies t = T/12$. Option (A).
- **Question 14**: Neutral point between $+4q$ and $+q$: $\frac{4q}{x^2} = \frac{q}{(L - x)^2} \implies \frac{2}{x} = \frac{1}{L - x} \implies x = 2L/3$.
  Equilibrium of $+q$: $\frac{4q^2}{L^2} + \frac{Q q}{(L/3)^2} = 0 \implies \frac{4q}{L^2} + \frac{9Q}{L^2} = 0 \implies Q = -4q/9$. Option (A).
- **Question 15**: $\eta = 1 - T_C/T_H = 1 - 300/500 = 1 - 0.60 = 0.40 = 40\%$. Option (A).
- **Question 16**: Lensmaker formula: $\frac{1}{f_{\text{air}}} = (\mu_g - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = 0.50 K = \frac{1}{20} \implies K = \frac{1}{10}$.
  In water: $\frac{1}{f'} = \left(\frac{\mu_g}{\mu_w} - 1\right)K = \left(\frac{1.50}{4/3} - 1\right)K = \left(\frac{9}{8} - 1\right)\frac{1}{10} = \frac{1}{80} \implies f' = 80.0\text{ cm}$. Option (A).
- **Question 17**: Rolling acceleration $a = \frac{g\sin\theta}{1 + I/MR^2} = \frac{g\sin\theta}{1 + 2/5} = \frac{5}{7}g\sin\theta$. Option (A).
- **Question 18**: $\tan\delta = B_V / B_H = 1 \implies \delta = 45^\circ$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Baeyer-Villiger oxidation proceeds via tetrahedral Criegee intermediate. Rate-determining step is alkyl migration with retention of configuration. Migratory aptitude follows electron density / hyperconjugation: $3^\circ > 2^\circ > 1^\circ > \text{methyl}$. Cyclohexanone yields $\varepsilon$-caprolactone. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Orgel diagrams illustrate weak-field high-spin term splittings. $d^1$ and $d^6$ have same terms ($D$ state). Inverted relationship between octahedral and tetrahedral configurations. $[\text{Ti(H}_2\text{O})_6]^{3+}$ shows single $^2T_{2g} \to {}^2E_g$ band. Correct options: **(A), (B), (C), (D)**.
- **Question 21**: Ionic strength $I = \frac{1}{2}\sum c_i z_i^2$. Debye-Huckel limiting law $\log\gamma_\pm = -A |z_+ z_-|\sqrt{I}$. Polyvalent electrolytes show severe deviations. At zero ionic strength $\gamma_\pm \to 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: $\bar{M}_n$ measured by osmometry; $\bar{M}_w$ measured by light scattering. $\text{PDI} = \bar{M}_w / \bar{M}_n \ge 1$. Monodisperse has $\text{PDI} = 1.0$. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Claisen condensation forms $\beta$-keto esters. Intramolecular version is Dieckmann cyclization. $\text{NaOEt}$ used to avoid transesterification. Driving force is final enolate resonance deprotonation. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Basic unit is $[\text{SiO}_4]^{4-}$. Sheet silicates share 3 corners $(\text{Si}_2\text{O}_5^{2-})_n$. Silicones contain $-\text{R}_2\text{Si-O-SiR}_2\text{O}-$ chains from $\text{Me}_2\text{SiCl}_2$ hydrolysis. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $K_{sp} = [Pb^{2+}][I^-]^2 = S(2S)^2 = 4S^3 \implies S = \left(\frac{7.1 \times 10^{-9}}{4}\right)^{1/3} = (1.775 \times 10^{-9})^{1/3} = 1.21 \times 10^{-3}\text{ mol/L} = 1.21\text{ mmol/L}$.
- **Question 26**: After 2 half-lives, $75\%$ of reactant is consumed ($25\%$ remains). $t = 2 \times 20.0 = 40.0\text{ minutes}$.
- **Question 27**: BCC has $Z = 2$. $\rho = \frac{Z M}{N_A a^3} \implies a^3 = \frac{2 \times 52.00}{(6.022 \times 10^{23})(7.19)} = \frac{104.0}{4.330 \times 10^{24}} = 2.402 \times 10^{-23}\text{ cm}^3 = 24.02 \times 10^{-24}\text{ cm}^3$.
  $a = (24.02)^{1/3} \times 10^{-8}\text{ cm} = 2.885 \times 10^{-8}\text{ cm} = 288.5\text{ pm}$.
- **Question 28**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = -0.257 - (-0.403) = +0.146\text{ V}$.
- **Question 29**: $\Delta T_f = i K_f m \implies 0.510 = i(1.86)(0.10) = 0.186 i \implies i = \frac{0.510}{0.186} = 2.74$.
- **Question 30**: $\text{Fe}^{2+}$ has $3d^6$ configuration. High-spin octahedral field ($t_{2g}^4 e_g^2$) has $n = 4$ unpaired electrons. $\mu_{\text{eff}} = \sqrt{4(6)} = \sqrt{24} \approx 4.90\text{ BM}$.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Methyl iodide has least steric hindrance, reacting fastest via $\text{S}_N2$. Option (A).
- **Question 32**: Correct IUPAC name: Pentaamminechloridocobalt(III) chloride. Option (A).
- **Question 33**: Zinc displaces silver from $[\text{Ag(CN)}_2]^-$ complex. Option (A).
- **Question 34**: $\text{IF}_5$ has 5 bond pairs and 1 lone pair ($sp^3d^2$), square pyramidal. Option (A).
- **Question 35**: Peptide linkage is an amide bond ($-\text{CONH}-$). Option (A).
- **Question 36**: Natural rubber is cis-1,4-polyisoprene. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Gradient vector $\nabla f = (2x, 4y, 6z) = (2, 4, 6)$ at $(1, 1, 1)$. Directional derivative along unit $(1, 1, 1)/\sqrt{3}$ is $\frac{2+4+6}{\sqrt{3}} = 12/\sqrt{3} = 4\sqrt{3}$. Maximum rate of change is $|\nabla f| = \sqrt{4+16+36} = \sqrt{56} = 2\sqrt{14}$. Tangent plane: $2(x-1) + 4(y-1) + 6(z-1) = 0 \implies x + 2y + 3z = 6$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Real orthogonal matrix: $A^T A = I \implies \det(A)^2 = 1 \implies \det(A) = \pm 1$. $\det(A) = +1$ is pure rotation. Eigenvalues satisfy $|\lambda| = 1$. Columns/rows form orthonormal basis. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Normal chord parameter relation: $t_2 = -t_1 - 2/t_1$. Chord length $L = 4a\frac{(1+t_1^2)^3}{t_1^2}$; minimum occurs at $t_1^2 = 2$, giving $L_{\text{min}} = 6\sqrt{3}a$. Subtends right angle at focus iff $t_1 = \pm 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Forced harmonic oscillator: transient decays exponentially; steady state amplitude $A(\omega) = F_0/\sqrt{(\omega_0^2-\omega^2)^2 + 4\gamma^2\omega^2}$; peak resonance frequency $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$; undamped resonant forcing produces secular term $t\sin(\omega_0 t)$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Tetrahedron volume formula holds. Centroid is average of 4 coordinates. Coplanarity condition holds. Lines connecting opposite midpoints bisect at centroid. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Stars and bars for positive integer solutions: $\binom{n-1}{k-1} = \binom{12-1}{4-1} = \binom{11}{3} = 165$. Generating function is $(x+x^2+\dots)^4$. Distinguishable case follows inclusion-exclusion. Non-negative case is $\binom{15}{3} = 455$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Wallis / Beta formula: $\int_0^{\pi/2}\sin^6 x \cos^4 x dx = \frac{1}{2}B(7/2, 5/2) = \frac{1}{2}\frac{\Gamma(7/2)\Gamma(5/2)}{\Gamma(6)} = \frac{1}{2}\frac{(5/2 \cdot 3/2 \cdot 1/2 \sqrt{\pi})(3/2 \cdot 1/2 \sqrt{\pi})}{120} = \frac{1}{2}\frac{(15/8)(3/4)\pi}{120} = \frac{45\pi}{64 \times 240} = \frac{3\pi}{512 \times 2} = \frac{3\pi}{1024} \implies m = 1024$ (or keyed factor).
- **Question 44**: $x^3 + y^3 = 6xy \implies 3x^2 + 3y^2 y' = 6y + 6x y' \implies y'(3y^2 - 6x) = 6y - 3x^2$. At $(3, 3)$: $y'(27 - 18) = 18 - 27 \implies 9 y' = -9 \implies y' = -1$. Magnitude is $1.00$.
- **Question 45**: $d = \frac{|-28|}{\sqrt{2^2 + (-3)^2 + 6^2}} = \frac{28}{\sqrt{4 + 9 + 36}} = \frac{28}{\sqrt{49}} = \frac{28}{7} = 4.00$.
- **Question 46**: $S = 1 + \frac{3}{3} + \frac{5}{9} + \dots$. $\frac{1}{3}S = \frac{1}{3} + \frac{3}{9} + \dots$.
  $\frac{2}{3}S = 1 + \frac{2}{3} + \frac{2}{9} + \dots = 1 + \frac{2/3}{1 - 1/3} = 1 + 1 = 2 \implies S = 3.00$.
- **Question 47**: Characteristic equation: $\lambda^3 - 4\lambda^2 + 5\lambda - 2 = 0$. Roots are $\lambda_1, \lambda_2, \lambda_3$ with $\sum \lambda_i = 4, \sum \lambda_i \lambda_j = 5$.
  $\text{tr}(A^2) = \sum \lambda_i^2 = (\sum \lambda_i)^2 - 2\sum \lambda_i \lambda_j = 4^2 - 2(5) = 16 - 10 = 6.00$.
- **Question 48**: Letters of `MISSISSIPPI`: 11 letters (1 M, 4 I, 4 S, 2 P).
  Number of permutations $= \frac{11!}{4! 4! 2!} = \frac{39916800}{24 \times 24 \times 2} = \frac{39916800}{1152} = 34650.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Maclaurin expansion $\sin x = x - x^3/6 + \dots \implies \frac{x - \sin x}{x^3} \to 1/6$. Option (A).
- **Question 50**: Director circle of hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ is $x^2 + y^2 = a^2 - b^2 = 16 - 9 = 7$. Option (A).
- **Question 51**: Normal vectors $\vec{n}_1 = (2, -1, 1), \vec{n}_2 = (1, 1, 2)$. $\vec{n}_1 \cdot \vec{n}_2 = 2 - 1 + 2 = 3$. $|\vec{n}_1| = \sqrt{6}, |\vec{n}_2| = \sqrt{6}$. $\cos\theta = 3/6 = 1/2 \implies \theta = 60^\circ = \pi/3$. Option (A).
- **Question 52**: $(1 + z)/(1 + \bar{z}) = z(1 + z)/(z + 1) = z$. Option (A).
- **Question 53**: $y' + y = 1 \implies \text{IF} = e^x$. $y e^x = e^x + C \implies y = 1 + C e^{-x}$. $y(0) = 0 \implies C = -1 \implies y = 1 - e^{-x}$. Option (A).
- **Question 54**: Mean $np = 4$, variance $np(1-p) = 2 \implies 1-p = 1/2 \implies p = 1/2 \implies n = 8$. Option (A).
