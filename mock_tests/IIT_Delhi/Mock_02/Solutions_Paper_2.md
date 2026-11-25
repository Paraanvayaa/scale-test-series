# Detailed Pedagogical Solutions — Mock Examination 02 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rolling with Slipping, Torque about Point of Contact, Angular Momentum Conservation about ground contact line.
- **2. Derivation**:
  - Kinetic friction force on sphere: $f_k = \mu_k M g$ acting backward.
  - Deceleration of CM: $a_c = \mu_k g \implies v(t) = v_0 - \mu_k g t$.
  - Angular acceleration: $\alpha = \frac{f_k R}{I} = \frac{\mu_k M g R}{\frac{2}{5}M R^2} = \frac{5\mu_k g}{2R} \implies \omega(t) = \frac{5\mu_k g}{2R} t$.
  - Pure rolling condition: $v(t_r) = R \omega(t_r) \implies v_0 - \mu_k g t_r = \frac{5}{2}\mu_k g t_r \implies \frac{7}{2}\mu_k g t_r = v_0 \implies t_r = \frac{2v_0}{7\mu_k g}$. (A) is correct.
  - Linear velocity at rolling: $v_r = v_0 - \mu_k g \left(\frac{2v_0}{7\mu_k g}\right) = \frac{5}{7}v_0$. (B) is correct.
  - Distance traveled: $s = v_0 t_r - \frac{1}{2} a_c t_r^2 = v_0\left(\frac{2v_0}{7\mu_k g}\right) - \frac{1}{2}(\mu_k g)\left(\frac{2v_0}{7\mu_k g}\right)^2 = \frac{2v_0^2}{7\mu_k g} - \frac{2v_0^2}{49\mu_k g} = \frac{12v_0^2}{49\mu_k g}$. (C) is correct.
  - Energy loss: $\Delta E = E_i - E_f = \frac{1}{2}M v_0^2 - \left[\frac{1}{2}M v_r^2 + \frac{1}{2}I \omega_r^2\right] = \frac{1}{2}M v_0^2 - \frac{7}{10}M v_r^2 = \frac{1}{2}M v_0^2 - \frac{7}{10}M \left(\frac{25}{49}v_0^2\right) = \frac{1}{2}M v_0^2 - \frac{5}{14}M v_0^2 = \frac{1}{7}M v_0^2$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Electromagnetic Oscillations in LC Tank Circuits, Energy Conservation.
- **2. Derivation**:
  - Kirchhoff's loop rule: $\frac{q}{C} + L \frac{d^2q}{dt^2} = 0 \implies \frac{d^2q}{dt^2} + \omega_0^2 q = 0$, with $\omega_0 = \frac{1}{\sqrt{LC}}$.
  - Solution with initial charge $Q_0$: $q(t) = Q_0 \cos(\omega_0 t)$. (A) is correct.
  - Current: $i(t) = \frac{dq}{dt} = -\omega_0 Q_0 \sin(\omega_0 t)$. (B) is correct.
  - Energy: $U_E(t) = \frac{q^2}{2C} = \frac{Q_0^2}{2C}\cos^2(\omega_0 t)$, $U_B(t) = \frac{1}{2}L i^2 = \frac{1}{2}L(\omega_0^2 Q_0^2)\sin^2(\omega_0 t) = \frac{Q_0^2}{2C}\sin^2(\omega_0 t)$. Peak energies are equal: $U_{\text{max}} = \frac{Q_0^2}{2C}$. (C) is correct.
  - Total energy $U_E + U_B = \frac{Q_0^2}{2C} = \text{const}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Doppler Effect for Sound Waves in Still Air.
- **2. Derivation**:
  - Approaching source: $\nu = \nu_0 \frac{v}{v - u} = \nu_0 \frac{v}{v - 0.20v} = \frac{\nu_0}{0.80} = 1.25\nu_0 = \frac{5}{4}\nu_0$. (A) is correct.
  - Wavelength in front: $\lambda' = \frac{v - u}{\nu_0} = \frac{0.80v}{\nu_0} = 0.80\lambda_0$. (B) is correct.
  - Receding source: $\nu' = \nu_0 \frac{v}{v + u} = \frac{\nu_0}{1.20} = \frac{5}{6}\nu_0 \approx 0.833\nu_0$. (C) is correct.
  - Wave propagation speed in a medium depends solely on the medium's elastic and inertial properties ($v = \sqrt{B/\rho}$), independent of source velocity. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Lens Maker's Formula in Medium $\frac{1}{f_m} = \left(\frac{\mu_l}{\mu_m} - 1\right)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$.
- **2. Derivation**:
  - In air: $\frac{1}{f} = (1.50 - 1) K = 0.50 K = \frac{1}{15} \implies K = \frac{2}{15}$.
  - In liquid $\mu_m = 1.20$: $\frac{1}{f'} = \left(\frac{1.50}{1.20} - 1\right) K = (1.25 - 1)\left(\frac{2}{15}\right) = 0.25 \times \frac{2}{15} = \frac{1}{30} \implies f' = +30\text{ cm}$. (A) is correct.
  - Power $P = 1/f'$ drops from $1/15$ to $1/30$. (B) is correct.
  - For $\mu_m = 1.60$: $\frac{\mu_l}{\mu_m} - 1 = \frac{1.50}{1.60} - 1 = -\frac{1}{16} < 0 \implies$ diverging lens. (C) is correct.
  - For $\mu_m = 1.50$: $\frac{\mu_l}{\mu_m} - 1 = 0 \implies 1/f' = 0 \implies f' \to \infty$ (invisible). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Einstein's Photoelectric Equation $K_{\text{max}} = h\nu - \Phi_0 = e V_0$.
- **2. Derivation**:
  - $K_{\text{max}} = h\nu - \Phi_0$ is linear in $\nu$. (A) is correct.
  - Saturation current is proportional to photon flux (intensity). (B) is correct.
  - Stopping potential $V_0 = \frac{h\nu - \Phi_0}{e}$ depends only on frequency, not intensity. (C) is correct.
  - Time lag is $\sim 10^{-9}\text{ s}$, indicating discrete photon-electron collisions. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Thermodynamic Cycles, Second Law, Entropy as State Function.
- **2. Derivation**:
  - Carnot cycle achieves maximum possible efficiency between two temperatures. Any other cycle has lower efficiency. (A) is correct.
  - Isochoric cooling: $dQ = n C_V dT < 0$ (heat rejected). (B) is correct.
  - Clockwise cycle on $P-V$ diagram encloses positive net work. (C) is correct.
  - Entropy $S$ is a state function; for any complete cycle, $\oint dS = 0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Angular momentum conservation about central pivot:
  $$L_i = m v (L/2) = (0.50)(6.00)(0.40) = 1.20\text{ kg}\cdot\text{m}^2/\text{s}$$
  Moment of inertia after sticking:
  $$I = \frac{1}{12}M L^2 + m(L/2)^2 = \frac{1}{12}(1.50)(0.80)^2 + 0.50(0.40)^2 = \frac{1}{12}(1.50)(0.64) + 0.50(0.16) = 0.080 + 0.080 = 0.160\text{ kg}\cdot\text{m}^2$$
  Angular velocity: $\omega = \frac{L_i}{I} = \frac{1.20}{0.160} = 7.50\text{ rad/s}$. Exact: `7.50`.
- **Question 8**: Fundamental for closed pipe: $\nu_1 = \frac{v}{4L} = \frac{340}{4(0.85)} = \frac{340}{3.40} = 100.00\text{ Hz}$. Exact: `100.00`.
- **Question 9**: By Gauss's Law, total flux through cube is $q/\varepsilon_0$. By symmetry, flux through one face is:
  $$\Phi_1 = \frac{q}{6\varepsilon_0} = \frac{4.0 \times 10^{-6}}{6(8.85 \times 10^{-12})} = \frac{4.0 \times 10^6}{53.1} \approx 75329.57\text{ N}\cdot\text{m}^2/\text{C} \approx 75329.60$$. Exact: `75329.60`.
- **Question 10**: Fringe shift $\Delta y = \frac{(\mu - 1)t D}{d} = 6 \beta = 6 \frac{\lambda D}{d} \implies (\mu - 1)t = 6\lambda \implies t = \frac{6\lambda}{\mu - 1} = \frac{6(600 \times 10^{-9})}{1.60 - 1} = \frac{3600 \times 10^{-9}}{0.60} = 6.0 \times 10^{-6}\text{ m} = 6.00\ \mu\text{m}$. Exact: `6.00`.
- **Question 11**: $\lambda = \frac{12.27}{\sqrt{150.0}} = \frac{12.27}{12.247} \approx 1.00\text{ \AA}$. Exact: `1.00`.
- **Question 12**: Axial magnetic field: $B = \frac{\mu_0 I R^2}{2(R^2 + x^2)^{3/2}} = \frac{\mu_0 I R^2}{2(2R^2)^{3/2}} = \frac{\mu_0 I}{2 \cdot 2\sqrt{2} R} = \frac{\mu_0 I}{4\sqrt{2} R} = \frac{(4\pi \times 10^{-7})(5.0)}{4(1.414)(0.10)} = \frac{20\pi \times 10^{-7}}{0.5657} \approx 11.11 \times 10^{-6}\text{ T} = 11.11\ \mu\text{T}$. Exact: `11.11`.

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
- **Question 19**: $[\text{Ni}(\text{CN})_4]^{2-}$ ($d^8$ square planar, all paired), $[\text{Fe}(\text{CN})_6]^{4-}$ ($d^6$ low spin, $t_{2g}^6$, paired), $[\text{Co}(\text{NH}_3)_6]^{3+}$ ($d^6$ low spin, $t_{2g}^6$, paired) are diamagnetic. $[\text{NiCl}_4]^{2-}$ ($d^8$ tetrahedral) has 2 unpaired electrons (paramagnetic). Options: (A), (B), (C).
- **Question 20**: Etard reaction, Gattermann-Koch reaction, Rosenmund reduction, and Stephen reduction are classical named reactions for synthesizing benzaldehyde. Options: (A), (B), (C), (D).
- **Question 21**: Standard reduction potentials: more negative $\implies$ stronger reducing agent. Lithium has highest reducing power in water due to high hydration energy. Fluorine is strongest oxidizer. Zinc reduces copper. Options: (A), (B), (C), (D).
- **Question 22**: Racemization occurs via planar carbocation intermediate in $S_N1$ solvolysis. Secondary and benzylic halides like 2-bromobutane and 1-phenylethyl chloride form carbocations that undergo racemization. Primary 1-bromobutane undergoes $S_N2$ with inversion. Achiral 2-bromo-2-methylpropane cannot racemize. Options: (A), (B).
- **Question 23**: Across a period, $Z_{\text{eff}}$, electronegativity, and ionization enthalpy increase; atomic radius decreases. Options: (A), (B), (C).
- **Question 24**: Phenylalanine, tyrosine, and tryptophan have aromatic side chains. Alanine has methyl group. Options: (A), (B), (C).
- **Question 25**: $K_p = \frac{4\alpha^2 P}{1 - \alpha^2} \implies 0.15 = \frac{4(0.04) P}{1 - 0.04} = \frac{0.16 P}{0.96} = \frac{P}{6} \implies P = 6 \times 0.15 = 0.90\text{ atm}$. Exact: `0.90`.
- **Question 26**: First-order reaction: slope $= -k = -0.0231\text{ min}^{-1} \implies k = 0.0231\text{ min}^{-1}$. Half-life $t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{0.0231} = 30.00\text{ min}$. Exact: `30.00`.
- **Question 27**: $V_{\text{cell}} = \frac{Z M}{\rho N_A} = \frac{4 \times 63.5}{8.92 \times 6.022 \times 10^{23}} = \frac{254}{5.3716 \times 10^{24}} \approx 4.73 \times 10^{-23}\text{ cm}^3 \implies V_{\text{cell}} \times 10^{23} = 4.73$. Exact: `4.73`.
- **Question 28**: $\Delta G^\circ = -n F E^\circ = -2(96500)(1.10) = -212300\text{ J/mol} = -212.3\text{ kJ/mol}$. Magnitude $= 212.30$. Exact: `212.30`.
- **Question 29**: $\Delta T_f = K_f m \implies 0.372 = K_f (0.20) \implies K_f = \frac{0.372}{0.20} = 1.86\text{ K}\cdot\text{kg/mol}$. Exact: `1.86`.
- **Question 30**: $\text{Mn}^{2+}$ is $3d^5$. High spin has 5 unpaired electrons. $\mu = \sqrt{5(7)} = \sqrt{35} \approx 5.92\text{ BM}$. Exact: `5.92`.
- **Question 31**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 32**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 33**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 34**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 35**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 36**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f'(x) = \frac{1 - \ln x}{x^2} = 0 \implies x = e$. Maximum is $1/e$. Since $f(e) > f(\pi)$, $e^\pi > \pi^e$. $\lim_{x \to \infty} \frac{\ln x}{x} = 0$. Options: (A), (B), (C), (D).
- **Question 38**: Standard matrix theorems: $\det(AB) = \det(A)\det(B)$, $(AB)^{-1} = B^{-1}A^{-1}$, $\text{adj}(AB) = \text{adj}(B)\text{adj}(A)$, $\det(\text{adj}(A)) = (\det A)^{n-1}$. Options: (A), (B), (C), (D).
- **Question 39**: $xx_1 + yy_1 = r^2 \implies 3x + 4y = 25$ touches at $(3, 4)$. Normal passes through $(0,0)$ with equation $4x - 3y = 0$. Tangent length from $(5,5)$ is 5. Chord of contact is $x + y = 5$. Options: (A), (B), (C), (D).
- **Question 40**: Harmonic oscillator ODE: $y'' + 4y = 0 \implies y = \cos(2x) + \sin(2x)$. Amplitude $= \sqrt{2}$, period $= \pi$. Options: (A), (B), (C), (D).
- **Question 41**: $|\vec{a}+\vec{b}| = 2\cos(\theta/2)$, $|\vec{a}-\vec{b}| = 2\sin(\theta/2)$, dot product is 0, vector sum bisects angle. Options: (A), (B), (C), (D).
- **Question 42**: Poisson with $\lambda = 2$: mean $= 2$, variance $= 2$, $P(0) = e^{-2}$, $P(1) = 2e^{-2}$. Options: (A), (B), (C), (D).
- **Question 43**: Limit of $(\sin x / x)^{1/x^2}$ is $e^{-1/6}$, so $k = 6$. Exact: `6.00`.
- **Question 44**: $f'(x) = 1 - \frac{4}{x^2} = 0 \implies x = 2$. Minimum value $= 2 + 4/2 = 4.00$. Exact: `4.00`.
- **Question 45**: $\int_0^1 x(1-x)^9 dx = B(2, 10) = \frac{1! 9!}{11!} = \frac{1}{110} \implies m = 110$. Exact: `110.00`.
- **Question 46**: Planes: $2x - y + 2z + 3 = 0$ and $2x - y + 2z + 9 = 0$. Distance $d = \frac{|9 - 3|}{\sqrt{4+1+4}} = \frac{6}{3} = 2.00$. Exact: `2.00`.
- **Question 47**: $a_n = S_n - S_{n-1} = 6n + 2 \implies a_{10} = 62.00$. Exact: `62.00`.
- **Question 48**: Block of 2: $(5-1)! \times 2! = 24 \times 2 = 48.00$. Exact: `48.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
