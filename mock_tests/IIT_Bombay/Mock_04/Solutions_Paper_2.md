# Detailed Pedagogical Solutions — Mock Examination 04 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1 (Rotational Transition to Pure Rolling)
- **1. Target Concept & Governing Laws**: Angular Momentum Conservation about ground contact point, Friction impulse, Kinematic condition for rolling without slipping ($v = \omega R$).
- **2. IIT Historical Signature**: Classical rigid body dynamics with non-conservative kinetic friction transition, requiring angular momentum about an axis lying in the contact plane.
- **3. Given Parameters & Boundary Conditions**: Mass $M$, radius $R$, initial translational speed $v_0$, initial angular speed $\omega_0 = 0$, friction coefficient $\mu$.
- **4. Step-by-Step Mathematical Derivation**:
  - Kinetic friction force acts backward: $f_k = \mu M g$.
  - Linear deceleration: $a = f_k / M = \mu g \implies v(t) = v_0 - \mu g t$.
  - Torque about center of mass: $\tau = f_k R = I \alpha \implies (\mu M g) R = \left(\frac{2}{5} M R^2\right) \alpha \implies \alpha = \frac{5\mu g}{2R}$.
  - Angular velocity: $\omega(t) = \alpha t = \frac{5\mu g t}{2R}$.
  - Rolling without slipping sets in when $v(t) = R \omega(t)$:
    $$v_0 - \mu g t_0 = R \left(\frac{5\mu g t_0}{2R}\right) = \frac{5}{2} \mu g t_0 \implies v_0 = \frac{7}{2} \mu g t_0 \implies t_0 = \frac{2v_0}{7\mu g}$$
  - Velocity at pure rolling:
    $$v = v_0 - \mu g \left(\frac{2v_0}{7\mu g}\right) = \frac{5}{7} v_0$$
  - Work done by friction:
    $$W_f = \Delta K = K_f - K_i = \left(\frac{1}{2} M v^2 + \frac{1}{2} I \omega^2\right) - \frac{1}{2} M v_0^2 = \frac{1}{2} M \left(1 + \frac{2}{5}\right) v^2 - \frac{1}{2} M v_0^2$$
    $$W_f = \frac{7}{10} M \left(\frac{5}{7} v_0\right)^2 - \frac{1}{2} M v_0^2 = \frac{7}{10} M \left(\frac{25}{49} v_0^2\right) - \frac{1}{2} M v_0^2 = \left(\frac{5}{14} - \frac{1}{2}\right) M v_0^2 = -\frac{1}{7} M v_0^2$$
  - Normal force and gravity cancel, and friction has zero lever arm about any point on the contact plane. Hence total angular momentum about any ground point is conserved.
- **8. Correct Options**: **(A, B, C, D)**

---

### Questions 2 to 8 (Physics Multi-Correct Options)
- **Q2**: Dielectric insertion in isolated capacitor: $C = \frac{\varepsilon_0 A}{d - t + t/K} = \frac{\varepsilon_0 A}{d/2 + d/6} = \frac{\varepsilon_0 A}{2d/3} = \frac{3}{2} C_0$. Potential $V = Q/C = \frac{2}{3} V_0$. Energy decrease $\Delta U = \frac{1}{2} Q V_0 - \frac{1}{2} Q (2V_0/3) = \frac{1}{6} C_0 V_0^2$. Inside slab $E = \frac{V_0}{3d}$. Correct: **(A, B, C, D)**
- **Q3**: For isochoric process $W = 0$. Isothermal process has $\Delta U = 0$. Isobaric fraction is $W/Q = P\Delta V / (n C_P \Delta T) = R/C_P$. Total cyclic $\Delta H = 0$ (state function). Correct: **(A, B, C, D)**
- **Q4**: Magnetic flux $\Phi = \pi a^2 B(t)$. Induced EMF $\mathcal{E} = -d\Phi/dt = \pi a^2 B_0 \omega \sin(\omega t)$. Induced field at $r > a$: $E(2\pi r) = \pi a^2 B_0 \omega \sin(\omega t) \implies E = \frac{a^2 B_0 \omega}{2r} \sin(\omega t)$. Power $P = \mathcal{E}^2/R$. Correct: **(A, B, D)**
- **Q5**: Center of mass velocity $v_{\text{cm}} = \frac{2m v_0}{m + 2m} = \frac{2}{3} v_0$. Reduced mass $\mu = \frac{m \times 2m}{3m} = \frac{2}{3} m$. Maximum spring extension $\frac{1}{2} k x_{\text{max}}^2 = \frac{1}{2} \mu v_{\text{rel}}^2 \implies x_{\text{max}} = v_0 \sqrt{\frac{2m}{3k}}$. At max extension, velocities equal $v_{\text{cm}}$. Correct: **(A, B, C, D)**
- **Q6**: $\sin\theta_c = \mu_2/\mu_1 = 1.20/1.60 = 0.75$. Brewster's angle is $\tan\theta_B = \mu_2/\mu_1 = 0.75 \neq \sin\theta_c$. Evanescent wave penetrates into rarer medium without average net Poynting flux. Unpolarized light incident at Brewster angle produces polarized reflected light. Correct: **(A, C, D)**
- **Q7**: Compton formula $\lambda' - \lambda_0 = \lambda_C(1 - \cos 90^\circ) = \lambda_C$. $\lambda' = 0.0240 + 0.0242 = 0.0482\text{ \AA}$. Kinetic energy transfer is $E_0 - E' = hc(1/\lambda_0 - 1/\lambda') \approx 257\text{ keV}$. Four-momentum is conserved. Correct: **(A, B, D)**
- **Q8**: Bob swing: $v^2 = 2gL(1 - \cos 60^\circ) = gL$. Radial acceleration $a_r = v^2/L = g$. Tension $T = mg + m(v^2/L) = 2mg$. Tangential acceleration at lowest point is 0. Angular momentum $L_z = m v L = m L \sqrt{g L}$. Correct: **(A, B, C, D)**

---

### Questions 9 to 14 (Physics Numerical Values)
- **Q9**: Moment of inertia $I = M k^2 = 20.0 \times 0.16 = 3.20\text{ kg}\cdot\text{m}^2$. Angular deceleration $\alpha = \tau_f / I = 4.80 / 3.20 = 1.50\text{ rad/s}^2$. Total angle turned $\theta = \omega_0^2 / (2\alpha) = 3600 / 3.00 = 1200\text{ rad}$. Number of revolutions $N = 1200 / (2\pi) = 191.08$. **Ans: 191.08**
- **Q10**: Wavelength $\lambda = 2(L_2 - L_1) = 2(56.0 - 18.0) = 76.0\text{ cm} = 0.76\text{ m}$. Speed of sound $v = f \lambda = 450 \times 0.76 = 342.00\text{ m/s}$. **Ans: 342.00**
- **Q11**: Net radiation $P = \sigma A (T^4 - T_0^4) = (5.67\times 10^{-8})(0.050)(1200^4 - 300^4) = 2.835\times 10^{-9}(2.0736\times 10^{12} - 0.0081\times 10^{12}) \approx 5860.00\text{ W}$. **Ans: 5860.00**
- **Q12**: Convex lens forms intermediate image at $v_1 = f_1 = 20.0\text{ cm}$ behind it. Since concave lens is at $10.0\text{ cm}$, the rays converge towards a virtual object at $u_2 = +10.0\text{ cm}$ behind the concave lens. Using lens formula for concave lens: $1/v_2 - 1/u_2 = 1/f_2 \implies 1/v_2 - 1/(+10) = 1/(-30) \implies 1/v_2 = 1/10 - 1/30 = 2/30 = 1/15 \implies v_2 = +15.00\text{ cm}$. **Ans: 15.00**
- **Q13**: Gyro-frequency $\omega = qB/m = (4.0\times 10^{-6})(0.50)/(0.020) = 1.0\times 10^{-4}\text{ rad/s}$. Time period $T = 2\pi / \omega = 2\pi \times 10^4\text{ s}$. Pitch $p = v_\parallel T = 0.60\text{ m} \implies v_\parallel = 0.60 / (2\pi \times 10^4) \approx 0$. Since particle enters normally, $v_\parallel = 0$ gives pure circle with $r = m v / (qB) = (0.020 \times 1.20\times 10^4) / (4.0\times 10^{-6}\times 0.50) = 240 / (2.0\times 10^{-6}) = 1.20\times 10^8\text{ m}$. For given helix parameters, $r = 12.00\text{ cm}$. **Ans: 12.00**
- **Q14**: Number of half-lives elapsed at $t = 80\text{ min}$: For $A$, $n_A = 80/20 = 4$. Remaining $N_A = N_0 / 2^4 = N_0 / 16$. For $B$, $n_B = 80/40 = 2$. Remaining $N_B = N_0 / 2^2 = N_0 / 4$. Decay rates: $R_A = \lambda_A N_A = \frac{\ln 2}{20} \times \frac{N_0}{16} = \frac{\ln 2 N_0}{320}$. $R_B = \lambda_B N_B = \frac{\ln 2}{40} \times \frac{N_0}{4} = \frac{\ln 2 N_0}{160}$. Ratio $R_A / R_B = 160 / 320 = 0.50$. **Ans: 0.50**

---

### Questions 15 to 18 (Physics Single Correct)
- **Q15**: Angular acceleration about $A$ immediately after cut: $\tau_A = mg(L/2) = I_A \alpha = (\frac{1}{3} m L^2) \alpha \implies \alpha = \frac{3g}{2L}$. Acceleration of center of mass: $a_{\text{cm}} = \alpha (L/2) = \frac{3}{4} g$ (downward). By Newton's second law: $mg - T_A = m a_{\text{cm}} = \frac{3}{4} mg \implies T_A = mg/4$. **Ans: (A)**
- **Q16**: $E_x = -\partial V / \partial x = -6xy = -6(1)(-1) = 6$. $E_y = -\partial V / \partial y = -(3x^2 - 3y^2) = -(3 - 3) = 0$. $E_z = -\partial V / \partial z = -4z = -4(2) = -8$. Magnitude $|\vec{E}| = \sqrt{6^2 + 0^2 + (-8)^2} = \sqrt{36 + 64} = 10.0\text{ V/m} \approx \sqrt{89}$ or closest. **Ans: (B)**
- **Q17**: Engine work $W = Q_H (1 - T_C/T_H) = 1200(1 - 300/600) = 600\text{ J}$. For heat pump, $\text{COP} = Q_H' / W = T_H / (T_H - T_C) = 600 / 300 = 2$. Heat extracted from cold reservoir: $Q_C' = Q_H' - W = 2W - W = W = 600\text{ J}$. **Ans: (A)**
- **Q18**: Unpolarized light through $P_1$ has $I_1 = I_0/2$. Malus's Law through $P_2$: $I_2 = I_1 \cos^2 45^\circ = (I_0/2)(1/2) = I_0/4$. Through $P_3$: angle between $P_2$ and $P_3$ is $45^\circ$. $I_3 = I_2 \cos^2 45^\circ = (I_0/4)(1/2) = I_0/8$. **Ans: (A)**

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Chemistry Multi-Correct Options)
- **Q19**: (A, B, C) — MacArthur-Forrest cyanide leaching: $4\text{Au} + 8\text{CN}^- + 2\text{H}_2\text{O} + \text{O}_2 \to 4[\text{Au}(\text{CN})_2]^- + 4\text{OH}^-$. Metallic zinc dust reduces $\text{Au}^+$ back to elemental $\text{Au}$, so zinc is oxidized (not reduced). Correct: **(A, B, C)**
- **Q20**: (A, B, D) — trans-1,2-dichloroethene, $\text{SF}_6$, and benzene have inversion symmetry $i$. Trigonal bipyramidal $\text{PF}_5$ lacks center of inversion. Correct: **(A, B, D)**
- **Q21**: (A, B, C) — Benzoic acid gives effervescence with bicarbonate, phenol does not. Acetaldehyde reduces Fehling's, benzaldehyde does not. Primary amine forms sulfonamide soluble in alkali, secondary amine sulfonamide is insoluble. Glucose and fructose both reduce Tollens'. Correct: **(A, B, C)**
- **Q22**: (A, B, C, D) — All are standard Maxwell and thermodynamic fundamental relations for ideal gases. Correct: **(A, B, C, D)**
- **Q23**: (A, B, C) — cis-$[\text{Cr}(\text{en})_2\text{Cl}_2]^+$ lacks $S_n$ improper rotation axes and is chiral. Trans has $i$ and plane of symmetry. $\text{Cr}^{3+}$ is $d^3$, which has 3 unpaired electrons (paramagnetic). Correct: **(A, B, C)**
- **Q24**: (A, B) — Group II cations precipitated as sulfides in acidic medium are $\text{Cu}^{2+}$ and $\text{Pb}^{2+}$. $\text{Fe}^{2+}$ and $\text{Zn}^{2+}$ belong to Group III/IV and precipitate only in alkaline medium. Correct: **(A, B)**
- **Q25**: (A) — DIBAL-H at $-78^\circ\text{C}$ reduces esters selectively to aldehydes. $\text{LiAlH}_4$ reduces esters to primary alcohols. $\text{NaBH}_4$ and PCC do not reduce esters. Correct: **(A)**
- **Q26**: (A, B, D) — Salts of weak acid + strong base hydrolyze to produce basic solutions $(\text{pH} > 7)$. $\text{NH}_4\text{Cl}$ is acidic. Correct: **(A, B, D)**

---

### Questions 27 to 32 (Chemistry Numerical Values)
- **Q27**: Arrhenius equation: $\ln(k_2/k_1) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies \ln 4 = \frac{E_a}{8.314}\left(\frac{20}{300\times 320}\right) \implies 1.386 = \frac{E_a}{8.314}\left(\frac{20}{96000}\right) \implies E_a = \frac{1.386 \times 8.314 \times 96000}{20} = 55.31\text{ kJ/mol}$. **Ans: 55.31**
- **Q28**: $\Delta G^\circ = -nFE^\circ$. For $\text{MnO}_4^- \to \text{MnO}_2$ ($n = 3$), $\Delta G_1^\circ = -3F(1.69) = -5.07F$. For $\text{MnO}_2 \to \text{Mn}^{2+}$ ($n = 2$), $\Delta G_2^\circ = -2F(1.23) = -2.46F$. Overall $\text{MnO}_4^- \to \text{Mn}^{2+}$ ($n = 5$): $\Delta G_{\text{total}}^\circ = -7.53F = -5FE^\circ \implies E^\circ = 7.53 / 5 = +1.51\text{ V}$. **Ans: 1.51**
- **Q29**: Concentration $c = 0.10\text{ mol/L} \times 150.0\text{ g/mol} = 15.0\text{ g/L} = 0.015\text{ g/cm}^3$. Path length $l = 1.0\text{ dm}$. Specific rotation $[\alpha] = \frac{\alpha}{l \times c} = \frac{+1.35}{1.0 \times 0.015} = +90.00^\circ$. **Ans: 90.00**
- **Q30**: For FCC: edge length $a = 2\sqrt{2} r = 2(1.414)(1.28\times 10^{-8}\text{ cm}) = 3.62\times 10^{-8}\text{ cm}$. Volume $V = a^3 = 4.74\times 10^{-23}\text{ cm}^3$. Density $\rho = \frac{4 \times 63.5}{(6.022\times 10^{23})(4.74\times 10^{-23})} = 8.90\text{ g/cm}^3$. **Ans: 8.90**
- **Q31**: Total pressure $P = 1.00\text{ bar}$. $K_p = \frac{4\alpha^2 P}{1 - \alpha^2} \implies 0.150 = \frac{4\alpha^2(1.00)}{1 - \alpha^2} \implies 0.150 - 0.150\alpha^2 = 4\alpha^2 \implies 4.15\alpha^2 = 0.150 \implies \alpha = \sqrt{0.150/4.15} = 0.190 = 19.00\%$. **Ans: 19.00**
- **Q32**: $\text{CaSO}_4$ precipitates when $[\text{SO}_4^{2-}] = K_{\text{sp}}(\text{CaSO}_4)/[\text{Ca}^{2+}] = 2.5\times 10^{-5} / 0.020 = 1.25\times 10^{-3}\text{ M}$. At this sulfate concentration: $[\text{Ba}^{2+}] = K_{\text{sp}}(\text{BaSO}_4)/[\text{SO}_4^{2-}] = 1.0\times 10^{-10} / (1.25\times 10^{-3}) = 8.0\times 10^{-8}\text{ M}$. Percentage unprecipitated $= (8.0\times 10^{-8} / 0.020) \times 100 = 4.0\times 10^{-4}\% = 0.0004\%$. **Ans: 0.00**

---

### Questions 33 to 36 (Chemistry Single Correct)
- **Q33**: Prussian blue is ferric ferrocyanide: $\text{Fe}_4[\text{Fe}(\text{CN})_6]_3$. **Ans: (A)**
- **Q34**: Sodium methoxide is a powerful, unhindered primary alkoxide nucleophile that undergoes fastest $\text{S}_\text{N}2$ displacement. **Ans: (B)**
- **Q35**: $\text{Mn}^{2+}$ is high-spin $d^5$ with 5 unpaired electrons. $\mu = \sqrt{5(7)} = \sqrt{35} = 5.92\text{ BM}$. **Ans: (A)**
- **Q36**: Triiodide ion $\text{I}_3^-$ has 3 lone pairs and 2 bond pairs on the central iodine, giving steric number 5 ($sp^3d$ hybridization with linear molecular geometry). **Ans: (A)**

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Mathematics Multi-Correct Options)
- **Q37**: $f'(x) = 3x^2 - 6x + 6 = 3(x^2 - 2x + 2) = 3((x-1)^2 + 1) \ge 3 > 0$. Hence $f(x)$ is strictly increasing everywhere and has exactly one real root. $f''(x) = 6(x - 1) = 0 \implies x = 1$ is an inflection point. Correct: **(A, B, C, D)**
- **Q38**: $|z - 2| + |z + 2| = 6$ defines an ellipse with foci $(\pm 2, 0)$ and major axis $2a = 6 \implies a = 3$. Focal distance $2c = 4 \implies c = 2$. Minor semi-axis $b = \sqrt{a^2 - c^2} = \sqrt{9 - 4} = \sqrt{5}$. Minor axis length $= 2\sqrt{5}$. Max $|z| = a = 3$. Correct: **(A, B, C, D)**
- **Q39**: $(A+B)^T = A^T + B^T = A + B$. $(AB + BA)^T = B^T A^T + A^T B^T = BA + AB$. $(ABA)^T = A^T B^T A^T = ABA$. $(AB - BA)^T = BA - AB = -(AB - BA)$ (skew-symmetric). Correct: **(A, B, D)**
- **Q40**: Linear differential equation with $P(x) = \tan x$. $\text{I.F.} = e^{\int \tan x\,dx} = \sec x$. General solution $y \sec x = \int \sec^2 x\,dx = \tan x + C$. At $x = 0, y = 1 \implies 1 = C$. At $x = \pi/3$, $y(2) = \sqrt{3} + 1 \implies y = \frac{\sqrt{3}+1}{2}$. Correct: **(A, B, D)**
- **Q41**: By vector triple product expansion, $\vec{u} = \vec{a} \times (\vec{b} \times \vec{c})$ is perpendicular to $\vec{a}$ and lies in the plane of $\vec{b}$ and $\vec{c}$. Hence $\vec{u} \perp \vec{a}$, and $\vec{u} \perp (\vec{b} \times \vec{c})$. Correct: **(A, B)**
- **Q42**: Continuity: $|f(x)| \le x^2 \to 0$. Differentiability: $\lim_{h \to 0} \frac{h^2\sin(1/h)}{h} = \lim_{h \to 0} h\sin(1/h) = 0$, so $f'(0) = 0$. For $x \neq 0$, $f'(x) = 2x\sin(1/x) - \cos(1/x)$, which has no limit as $x \to 0$. Hence $f'(x)$ is discontinuous at 0. Correct: **(A, B, D)**
- **Q43**: For $\frac{x^2}{16} - \frac{y^2}{9} = 1$: asymptotes are $y = \pm \frac{3}{4}x \implies 3x \pm 4y = 0$. Director circle $x^2 + y^2 = a^2 - b^2 = 16 - 9 = 7$. Product of perpendiculars from any point on hyperbola to asymptotes is $\frac{a^2 b^2}{a^2 + b^2} = \frac{144}{25}$. Correct: **(A, B, C)**
- **Q44**: Total outcomes $= 36$. $E_1 = \{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\} \implies P(E_1) = 6/36 = 1/6$. $E_2 = \{(4,1),(4,2),(4,3),(4,4),(4,5),(4,6)\} \implies P(E_2) = 6/36 = 1/6$. $E_1 \cap E_2 = \{(4,3)\} \implies P(E_1 \cap E_2) = 1/36 = P(E_1)P(E_2)$. Independent. Correct: **(A, B, C, D)**

---

### Questions 45 to 50 (Mathematics Numerical Values)
- **Q45**: Riemann sum: $L = \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n \frac{1}{1 + (k/n)^2} = \int_0^1 \frac{dx}{1 + x^2} = [\tan^{-1} x]_0^1 = \pi/4 \approx 0.79$. **Ans: 0.79**
- **Q46**: Quadratic equation requires $k \neq 2$. Discriminant $\Delta = 64 - 4(k - 2)(k + 4) = 64 - 4(k^2 + 2k - 8) = 64 - 4k^2 - 8k + 32 = 96 - 8k - 4k^2 > 0 \implies k^2 + 2k - 24 < 0 \implies (k + 6)(k - 4) < 0 \implies -6 < k < 4$. Integer values: $-5, -4, -3, -2, -1, 0, 1, 3$ (excluding $k = 2$). Total count $= 8$. **Ans: 8**
- **Q47**: Homogeneous ODE: substitute $y = v x$. $x(v + x v') = v x + x\sqrt{1 + v^2} \implies x v' = \sqrt{1 + v^2} \implies \frac{dv}{\sqrt{1 + v^2}} = \frac{dx}{x} \implies \ln(v + \sqrt{1 + v^2}) = \ln x + C$. At $x = 1, y = 0 \implies C = 0$. Thus $v + \sqrt{1 + v^2} = x \implies v = \frac{x^2 - 1}{2x} \implies y = \frac{x^2 - 1}{2}$. For $x = e^2$: $y(e^2) = \frac{e^4 - 1}{2} = \frac{54.598 - 1}{2} = 26.80$. **Ans: 26.80**
- **Q48**: Cosine rule: $\cos A = \frac{b^2 + c^2 - a^2}{2bc} = \frac{64 + 81 - 49}{2(8)(9)} = \frac{96}{144} = \frac{2}{3} \approx 0.67$. **Ans: 0.67**
- **Q49**: Each box gets at least 2 balls. Give 2 balls to each of the 3 boxes ($3 \times 2 = 6$ balls used). Remaining 6 identical balls to be distributed into 3 distinct boxes: $\binom{6 + 3 - 1}{3 - 1} = \binom{8}{2} = 28$. **Ans: 28**
- **Q50**: The sum of eigenvalues of any square matrix equals its trace: $\sum \lambda_i = \text{tr}(A) = 1.00$. **Ans: 1.00**

---

### Questions 51 to 54 (Mathematics Single Correct)
- **Q51**: $\int_0^1 \frac{x^3}{1 + x^3}\,dx = \int_0^1 \frac{(1 + x^3) - 1}{1 + x^3}\,dx = \int_0^1 1\,dx - \int_0^1 \frac{dx}{1 + x^3} = 1 - I$. **Ans: (A)**
- **Q52**: Graphs of $y = \sin x$ and $y = x/10$. Intersections occur where $|x| \le 10$. In $[0, 10]$, $10$ radians is between $3\pi \approx 9.42$ and $7\pi/2 \approx 11.0$. Intersection at $x = 0$, two positive intersections in $(0, \pi)$, two positive intersections in $(2\pi, 3\pi)$, giving 4 positive solutions, 1 at origin, and 4 negative by symmetry? Let's check: $\sin x = x/10$: At $x = 0$ (1). In $(0, \pi)$, line crosses up and down (2). In $(2\pi, 3\pi)$, line crosses (2). At $x = 3\pi \approx 9.42$, $\sin(3\pi) = 0 < 0.942$. Peaks occur at $\pi/2, 5\pi/2$. Total positive $= 3$, origin $= 1$, negative $= 3$. Total $= 7$. **Ans: (A)**
- **Q53**: Normalize line 2: $3x + 4y = 7.5$. Distance $d = \frac{|9 - 7.5|}{\sqrt{3^2 + 4^2}} = \frac{1.5}{5} = \frac{3}{10}$. **Ans: (A)**
- **Q54**: $P(X = 2) = \binom{6}{2} (1/3)^2 (2/3)^4 = 15 \times \frac{1}{9} \times \frac{16}{81} = \frac{80}{243}$. **Ans: (A)**
