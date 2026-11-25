# Detailed Pedagogical Solutions — Mock Examination 10 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rolling Without Slipping Under External Force, Static Friction Constraint.
- **2. Derivation**:
  - Net force along incline: $M g\sin\theta - F\cos\theta - f = M a$.
  - Torque about CM: $f R = I \alpha = \left(\frac{1}{2}M R^2\right)\left(\frac{a}{R}\right) \implies f = \frac{1}{2}M a$.
  - Substituting $f$: $M g\sin\theta - F\cos\theta = \frac{3}{2}M a \implies a = \frac{2}{3}\left(g\sin\theta - \frac{F}{M}\cos\theta\right)$. (A) is correct.
  - Friction force: $f = \frac{1}{3}(M g\sin\theta - F\cos\theta)$. (B) is correct.
  - Normal force: $N = M g\cos\theta + F\sin\theta$. Pure rolling requires $|f| \le \mu N$. (C) is correct.
  - If $F = M g\tan\theta$, then $M g\sin\theta - F\cos\theta = 0$, giving $a = 0$ and $f = 0$ (static equilibrium). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Concentric Spherical Conductors, Electric Potential, Charge Redistribution.
- **2. Derivation**:
  - Outside both shells ($r \ge R_2$), Gauss's law gives potential $V(r) = \frac{Q_1 + Q_2}{4\pi\varepsilon_0 r}$. (A) is correct.
  - Between shells ($R_1 \le r \le R_2$), $V(r) = \frac{1}{4\pi\varepsilon_0}\left(\frac{Q_1}{r} + \frac{Q_2}{R_2}\right)$. (B) is correct.
  - When connected by a wire, interior conductor cannot maintain electrostatic field, so all charge moves to outer shell. (C) is correct.
  - Grounding outer shell sets $V(R_2) = 0 \implies \frac{1}{4\pi\varepsilon_0}\frac{Q_1 + Q_2'}{R_2} = 0 \implies Q_2' = -Q_1$ (if outside grounded, or with radius ratio for grounded inner/outer). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Polytropic Process, Molar Heat Capacity, P-V Relationship.
- **2. Derivation**:
  - Molar heat capacity $C = C_V + \frac{R}{1 - n}$. Given $C = C_V + R/2$, we have $\frac{1}{1-n} = \frac{1}{2} \implies 1 - n = 2 \implies n = -1$. (A) is correct.
  - $P V^{-1} = \text{constant} \implies P \propto V$. (B) is correct.
  - Work done: $W = \int_{V_1}^{2V_1} P dV = \int_{V_1}^{2V_1} \left(\frac{P_1}{V_1}V\right)dV = \frac{P_1}{V_1}\left[\frac{V^2}{2}\right]_{V_1}^{2V_1} = \frac{P_1}{2V_1}(4V_1^2 - V_1^2) = \frac{3}{2}P_1 V_1$. (C) is correct.
  - $\Delta T = \frac{P_2 V_2 - P_1 V_1}{R} = \frac{(2P_1)(2V_1) - P_1 V_1}{R} = \frac{3P_1 V_1}{R}$. $\Delta U = C_V \Delta T = \frac{3}{2}R\left(\frac{3P_1 V_1}{R}\right) = \frac{9}{2}P_1 V_1$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Fresnel Biprism, Virtual Source Separation, Fringe Width.
- **2. Derivation**:
  - Deviation produced by each half-prism: $\delta = (\mu - 1)\alpha$.
  - Separation between virtual sources: $d = 2 u \delta = 2 u (\mu - 1)\alpha$. (A) is correct.
  - Fringe width: $\beta = \frac{\lambda D}{d} = \frac{\lambda D}{2u(\mu - 1)\alpha}$. (B) is correct.
  - $\beta$ is proportional to screen distance $D$. (C) is correct.
  - As $\alpha$ decreases, $d$ decreases, so $\beta$ increases. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Davisson-Germer Experiment, de Broglie Matter Waves, Bragg Law.
- **2. Derivation**:
  - Experimentally verified wave nature of electrons. (A) is correct.
  - Maximum scattering at $54\text{ V}$ and $\phi = 50^\circ$. (B) is correct.
  - Bragg angle $\theta = 90^\circ - \phi/2 = 65^\circ$. (C) is correct.
  - Theoretical de Broglie wavelength ($0.167\text{ nm}$) matched experimental Bragg diffraction ($0.165\text{ nm}$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Adiabatic Oscillations of Gas-Piston System, Simple Harmonic Motion.
- **2. Derivation**:
  - Rapid oscillations are adiabatic ($P V^\gamma = \text{constant}$). (A) is correct.
  - Pressure changes: $dP_1 = -\gamma P_0 \frac{A x}{V_0}$, $dP_2 = +\gamma P_0 \frac{A x}{V_0}$.
  - Net restoring force: $F = (P_1 - P_2)A = -2\gamma\frac{P_0 A^2}{V_0}x$. (B) is correct.
  - Equation of motion: $m \ddot{x} + \frac{2\gamma P_0 A^2}{V_0}x = 0$. With $V_0 = A L$: $\omega = \sqrt{\frac{2\gamma P_0 A}{m L}}$. (C) is correct.
  - For isothermal process ($\gamma = 1$), $\omega_{\text{iso}} = \sqrt{\frac{2P_0 A}{m L}}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Momentum conservation: $m v = (M + m)v_f \implies v_f = \frac{0.020 \times 400.0}{3.98 + 0.020} = \frac{8.00}{4.00} = 2.00\text{ m/s}$.
  Energy conservation: $\frac{1}{2}(M + m)v_f^2 = (M + m)g h \implies h = \frac{v_f^2}{2g} = \frac{4.00}{2(9.80)} = \frac{4.00}{19.6} \approx 0.20\text{ m}$.
- **Question 8**: $Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{10.0}\sqrt{\frac{20.0 \times 10^{-3}}{50.0 \times 10^{-6}}} = \frac{1}{10.0}\sqrt{400} = \frac{20.0}{10.0} = 2.00$.
- **Question 9**: $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2} = \frac{1}{15.0} - \frac{1}{30.0} = \frac{1}{30.0} \implies F = 30.0\text{ cm}$.
- **Question 10**: Work done $W = P \Delta V = (1.0 \times 10^5)(0.012 - 0.010) = 1.0 \times 10^5 \times 0.002 = 200.0\text{ J}$.
  $\Delta U = Q - W = 500.0 - 200.0 = 300.0\text{ J}$.
- **Question 11**: Bohr quantization: $L = n \hbar = 3 \hbar$. Thus the value is $3.00$.
- **Question 12**: $\nu_0 = \frac{1}{2\pi}\sqrt{\frac{k}{m}} = \frac{1}{2\pi}\sqrt{\frac{200.0}{0.50}} = \frac{1}{2\pi}\sqrt{400} = \frac{20.0}{2\pi} = \frac{10.0}{\pi} \approx 3.2\text{ Hz}$.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: Hoop $a = \frac{1}{2}g\sin\theta$ (P-1); Solid cylinder $a = \frac{2}{3}g\sin\theta$ (Q-2); Solid sphere $a = \frac{5}{7}g\sin\theta$ (R-3); Shell $a = \frac{3}{5}g\sin\theta$ (S-4). Option (A).
- **Question 14**: Dimensions: Flux $[M L^2 T^{-2} A^{-1}]$ (P-1); Inductance $[M L^2 T^{-2} A^{-2}]$ (Q-2); Field $[M T^{-2} A^{-1}]$ (R-3); Permeability $[M L T^{-2} A^{-2}]$ (S-4). Option (A).
- **Question 15**: Blue sky: Rayleigh scattering (P-1); Rainbow: dispersion/reflection (Q-2); Mirage: TIR (R-3); Oil film: interference (S-4). Option (A).
- **Question 16**: First Maxwell from $dU$ (P-1); Second from $dH$ (Q-2); Third from $dF$ (R-3); Fourth from $dG$ (S-4). Option (A).
- **Question 17**: Alpha decay: $A-4, Z-2$ (P-1); Beta-minus: $Z+1$ (Q-2); Electron capture: $Z-1$ (R-3); Gamma decay: isomers (S-4). Option (A).
- **Question 18**: Inductor leads $+90^\circ$ (P-1); Capacitor lags $-90^\circ$ (Q-2); Resistor in phase $0^\circ$ (R-3); Resonant circuit in phase $0^\circ$ (S-4). Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Tropylium cation has $6\pi$ aromatic system. Cyclopropenyl cation has $2\pi$ aromatic system. Cyclopentadienyl cation has $4\pi$ antiaromatic system. Trityl carbocation is stabilized by 3 phenyl rings. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Acidic buffer requires weak acid and its conjugate salt. Acetic acid + sodium acetate, Formic acid + potassium formate, and Benzoic acid + sodium benzoate are buffers. $\text{HCl} + \text{NaCl}$ is a strong acid mixture (not a buffer). Correct options: **(A), (B), (C)**.
- **Question 21**: More negative $E^\circ$ indicates stronger reducing agent. Zinc displaces copper. Copper does not displace hydrogen from non-oxidizing acids. Silver cannot displace zinc. Correct options: **(A), (B), (C)**.
- **Question 22**: Calcination expels volatile gases without air. Roasting oxidizes sulfide ores in presence of air. Limestone heating is calcination. $\text{ZnS}$ oxidation is roasting. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Gabriel phthalimide yields pure primary amines. Hofmann degradation yields primary amines with one less carbon. Nitrile reduction yields primary amines. Direct alkylation gives mixture of $1^\circ, 2^\circ, 3^\circ$ and quaternary salts. Correct options: **(A), (B), (C)**.
- **Question 24**: Rock salt is $6:6$ coordination. Fluorite is $8:4$ coordination. Anti-fluorite is $4:8$ coordination. Zinc blende is $4:4$ coordination. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $\text{pH} = 4.00 \implies [\text{H}^+] = 1.0 \times 10^{-4}\text{ M}$.
  $K_a = \frac{[\text{H}^+]^2}{C} = \frac{(1.0 \times 10^{-4})^2}{0.010} = \frac{1.0 \times 10^{-8}}{1.0 \times 10^{-2}} = 1.0 \times 10^{-6}$.
  Multiplied by $10^6$, value is $1.00$.
- **Question 26**: Rate $\propto [A]^2 [B]^1$. Overall order $= 2 + 1 = 3.00$.
- **Question 27**: $\text{FCC}$ has $Z = 4$. $\rho = \frac{Z M}{N_A a^3} = \frac{4 \times 60.0}{(6.022 \times 10^{23})(64.0 \times 10^{-24})} = \frac{240.0}{38.54} = 6.23\text{ g/cm}^3$.
- **Question 28**: $\text{CH}_4 + 2\text{O}_2 \to \text{CO}_2 + 2\text{H}_2\text{O}(l)$.
  $\Delta_c H^\circ = \Delta_f H^\circ(\text{CO}_2) + 2\Delta_f H^\circ(\text{H}_2\text{O}) - \Delta_f H^\circ(\text{CH}_4) = -393.5 + 2(-285.8) - (-74.8) = -393.5 - 571.6 + 74.8 = -890.3\text{ kJ/mol}$.
- **Question 29**: Molality $m = \frac{18.0 / 180.0}{0.200\text{ kg}} = \frac{0.10}{0.200} = 0.50\text{ m}$. $\Delta T_f = K_f m = 1.86 \times 0.50 = 0.93\text{ K}$.
- **Question 30**: $\text{XeF}_2$ has 8 valence electrons, 2 used for bonding with F, leaving 6 non-bonding electrons $= 3$ lone pairs.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Tollens: silver mirror (P-1); Fehling: red ppt (Q-2); Ferric chloride: violet color (R-3); Lucas: alcohol classification (S-4). Option (A).
- **Question 32**: Complex names: Potassium hexacyanidoferrate(II) (P-1); Tetraamminecopper(II) sulfate (Q-2); Hexaamminecobalt(III) chloride (R-3); Potassium hexachloridoplatinate(IV) (S-4). Option (A).
- **Question 33**: Mond process for Ni (P-1); Van Arkel for Zr/Ti (Q-2); Electrolytic for Cu (R-3); Zone refining for semiconductors (S-4). Option (A).
- **Question 34**: Crimson: Lithium (P-1); Yellow: Sodium (Q-2); Apple green: Barium (R-3); Brick red: Calcium (S-4). Option (A).
- **Question 35**: Plexiglas (P-1); Teflon (Q-2); Orlon (R-3); Styron (S-4). Option (A).
- **Question 36**: Starch: polysaccharide (P-1); Insulin: peptide (Q-2); Cholesterol: steroid (R-3); ATP: nucleotide (S-4). Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: $f(-x) = \frac{(-x)^2 - 1}{(-x)^2 + 1} = \frac{x^2 - 1}{x^2 + 1} = f(x)$ (even). $f'(x) = \frac{2x(x^2+1) - (x^2-1)(2x)}{(x^2+1)^2} = \frac{4x}{(x^2+1)^2}$. Min at $x=0$ with $f(0) = -1$. As $x\to\pm\infty$, $f(x)\to 1$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: $A^3 - A = 0 \implies \lambda(\lambda - 1)(\lambda + 1) = 0 \implies \lambda \in \{0, 1, -1\}$. Determinant product of eigenvalues $\in \{0, 1, -1\}$. Distinct linear factors imply real diagonalizability. If $\det(A) \ne 0$, 0 is not an eigenvalue, so $A(A^2 - I) = 0 \implies A^2 = I$. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: $x^2 - 4x + y^2 - 6y = 12 \implies (x-2)^2 + (y-3)^2 = 12 + 4 + 9 = 25$. Center $(2, 3)$, radius $5$. $(5-2)^2 + (7-3)^2 = 9 + 16 = 25$ (on circle). Tangent: $(5-2)(x-2) + (7-3)(y-3) = 25 \implies 3(x-2) + 4(y-3) = 25 \implies 3x + 4y - 43 = 0$. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Homogeneous equation. $y = vx \implies v + x v' = \frac{1 - v}{1 + v} \implies x v' = \frac{1 - v - v - v^2}{1 + v} = \frac{1 - 2v - v^2}{1 + v}$. In polar coordinates, $\tan\theta = y/x$, giving spiral trajectories. Correct options: **(A), (B), (D)**.
- **Question 41**: $\vec{u} \times \vec{v} = (\hat{i}+\hat{j})\times(\hat{j}+\hat{k}) = \hat{k} - \hat{j} + \hat{i} = \hat{i} - \hat{j} + \hat{k}$. $[\vec{u}\ \vec{v}\ \vec{w}] = (\vec{u}\times\vec{v})\cdot\vec{w} = (1, -1, 1)\cdot(1, 0, 1) = 1 + 0 + 1 = 2$. Linearly independent; volume is 2. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Binomial $n = 5, p = 1/3$: Mean $n p = 5/3$. Variance $n p q = 5(1/3)(2/3) = 10/9$. $P(X = 2) = \binom{5}{2}(1/9)(8/27) = 80/243$. $P(X \ge 1) = 1 - (2/3)^5 = 1 - 32/243 = 211/243$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Beta integral $\int_0^1 x^4 (1-x)^3 dx = B(5, 4) = \frac{\Gamma(5)\Gamma(4)}{\Gamma(9)} = \frac{4! 3!}{8!} = \frac{24 \times 6}{40320} = \frac{144}{40320} = \frac{1}{280} \implies m = 280$.
- **Question 44**: $y = x^2 \implies y' = 2x$. At $(1, 1)$, tangent slope $m_T = 2$. Normal slope $m_N = -1/2 = -0.50$. Magnitude is $0.50$.
- **Question 45**: $d = \frac{|12 - 3|}{\sqrt{1^2 + (-2)^2 + 2^2}} = \frac{9}{\sqrt{9}} = \frac{9}{3} = 3.00$.
- **Question 46**: Infinite GP $a = 8, r = 1/4 \implies S = \frac{8}{1 - 1/4} = \frac{8}{3/4} = \frac{32}{3} \approx 10.67$.
- **Question 47**: `LEADER`: 6 letters with 2 E's. Permutations $= \frac{6!}{2!} = \frac{720}{2} = 360.00$.
- **Question 48**: Tridiagonal matrix determinant:
  $2(4 - 1) - 1(2 - 0) = 2(3) - 2 = 6 - 2 = 4.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: $\lim_{x\to\infty}(1 + 3/x)^{2x} = e^{\lim_{x\to\infty} 2x(3/x)} = e^6$. Option (A).
- **Question 50**: $\frac{x^2}{16} - \frac{y^2}{9} = 1 \implies a^2 = 16, b^2 = 9$. $e = \sqrt{1 + b^2/a^2} = \sqrt{1 + 9/16} = \sqrt{25/16} = 5/4$. Option (A).
- **Question 51**: The two lines intersect at the point $(0, 0, 0)$ (check coordinates), so shortest distance is 0. Option (A).
- **Question 52**: Since $|z| = 1 \implies z \bar{z} = 1 \implies \bar{z} = 1/z$. $\frac{1 + z}{1 + 1/z} = \frac{1 + z}{(z + 1)/z} = z$. Option (A).
- **Question 53**: $\frac{dy}{dx} + y = 1 \implies y = 1 - e^{-x}$. Option (A).
- **Question 54**: $n p = 4, n p (1 - p) = 2 \implies 1 - p = 1/2 \implies p = 1/2 \implies n = 8$. Option (A).
