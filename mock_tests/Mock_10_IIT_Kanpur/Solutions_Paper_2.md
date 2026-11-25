# Detailed Solutions and Pedagogical Analysis — Mock Examination 10 (Paper 2)
### Organising Institute Style: IIT Kanpur (`IIT_KANPUR_STYLE`)

---

## PART I: PHYSICS

### Q1. Cylinder Rolling Down Incline
- **Analysis**:
  - $M g \sin\theta - f = M a$ and $f R = I \alpha = (\frac{1}{2} M R^2)(a/R) \implies f = \frac{1}{2} M a$.
  - Adding: $M g \sin\theta = \frac{3}{2} M a \implies a = \frac{2}{3} g \sin\theta$. (A is correct).
  - Friction force $f = \frac{1}{3} M g \sin\theta$. (B is correct).
  - For no slipping: $f \le \mu M g \cos\theta \implies \frac{1}{3} M g \sin\theta \le \mu M g \cos\theta \implies \mu \ge \frac{1}{3}\tan\theta$. (C and D correct).
- **Correct Options**: **(A, B, C, D)**.

### Q2. Rectangular PV Cycle
- **Analysis**:
  - Base $= 2V_0 - V_0 = V_0$. Height $= P_0 - P_0/2 = P_0 / 2$.
  - Work done $= \text{Area} = (P_0 / 2) V_0 = \frac{1}{2} P_0 V_0$. (B is correct).
  - Shape is a rectangle, traversed clockwise. (A and C correct).
  - Total heat absorbed $Q_{\text{in}} = Q_{\text{heating}} + Q_{\text{expansion}} = n C_v \Delta T_1 + n C_p \Delta T_2$.
    For monoatomic gas, efficiency $\eta = W / Q_{\text{in}} = \frac{1}{13} \approx 7.69\%$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q3. Linear 2D Electric Field
- **Analysis**:
  - Divergence: $\nabla \cdot \vec{E} = \frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} = a + b$.
  - By Gauss's law: $\rho = \varepsilon_0 \nabla \cdot \vec{E} = \varepsilon_0(a + b)$. (A and B correct).
  - $\vec{E} = -\nabla V \implies V(x, y) = -\frac{1}{2}(a x^2 + b y^2) + V_0$. (C is correct).
  - Curl $\nabla \times \vec{E} = (\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y})\hat{k} = 0$, so conservative. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q4. Series RLC Circuit Characteristics
- **Analysis**:
  - $\omega_0 = 1/\sqrt{L C} = 1/\sqrt{0.1 \times 10^{-4}} = 1/\sqrt{10^{-5}} = 100\sqrt{10}\text{ rad/s}$. (A is correct).
  - At resonance, $Z = R$, $I_0 = V_0 / R$. (B is correct).
  - $Q = \frac{\omega_0 L}{R} = \frac{100\sqrt{10} \times 0.1}{10} = \sqrt{10}$. (C is correct).
  - At $\omega > \omega_0$, circuit is inductive ($X_L > X_C$). (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q5. Electron Single-Slit Diffraction
- **Analysis**: All four statements correctly state wave properties of matter in single-slit diffraction.
- **Correct Options**: **(A, B, C, D)**.

### Q6. Apparent Shift by Glass Slab
- **Analysis**: All four statements correctly describe the normal refraction shift $\Delta y = t(1 - 1/\mu)$.
- **Correct Options**: **(A, B, C, D)**.

### Q7–Q12 Numerical Solutions
- **Q7**: Normal reaction from floor $= M g = 200\text{ N}$.
  Height of wall contact: $h = \sqrt{5^2 - 3^2} = 4.0\text{ m}$.
  Torque about base on floor in equilibrium:
  $$N_{\text{wall}} h = M g (d/2) \implies N_{\text{wall}}(4.0) = 200(1.5) = 300 \implies N_{\text{wall}} = 75\text{ N}$$
  **Answer: 75**.
- **Q8**: $T V^{\gamma - 1} = \text{const}$. For monoatomic, $\gamma - 1 = 5/3 - 1 = 2/3$.
  $$T_f / T_i = (V_i / V_f)^{2/3} = (1/8)^{2/3} = (1/2)^2 = 1/4 = 0.25$$
  **Answer: 0.25**.
- **Q9**: Two halves in series: $C_1 = 2 C_0 = 100\,\mu\text{F}$, $C_2 = 2 \kappa C_0 = 8 C_0 = 400\,\mu\text{F}$.
  $$C_{\text{eq}} = \frac{C_1 C_2}{C_1 + C_2} = \frac{100 \times 400}{500} = 80\,\mu\text{F}$$
  **Answer: 80**.
- **Q10**: $E_{\text{photon}} = \frac{1240}{300} = 4.133\text{ eV}$.
  $$e V_s = E_{\text{photon}} - \Phi = 4.133 - 2.25 = 1.88\text{ eV} \implies V_s = 1.88\text{ V}$$
  **Answer: 1.88**.
- **Q11**: Magnification $m = +1/4 = -v/u \implies v = -u/4$.
  $$\frac{1}{v} + \frac{1}{u} = \frac{1}{f} \implies -\frac{4}{u} + \frac{1}{u} = -\frac{3}{u} = \frac{1}{20} \implies u = -60\text{ cm}$$
  Distance is $60\text{ cm}$. **Answer: 60**.
- **Q12**: Force per unit length:
  $$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d} = \frac{(4\pi \times 10^{-7})(10)(20)}{2\pi (0.20)} = \frac{400 \times 10^{-7}}{0.20} = 2.0 \times 10^{-4}\text{ N/m} = 200\,\mu\text{N/m}$$
  **Answer: 200**.

### Q13–Q18 Integer Solutions
- **Q13**: $T = 2\pi\sqrt{L/g}$. If $L' = 4L$, $T' = 2 T = 2(2.0) = 4.0\text{ s}$. **Answer: 4**.
- **Q14**: A string fixed at both ends vibrating in the $n$-th harmonic has $n + 1$ nodes. For $n = 3$, nodes $= 4$. **Answer: 4**.
- **Q15**: $1/16 = (1/2)^4 \implies 4$ half-lives in 24 hours $\implies T_{1/2} = 24 / 4 = 6\text{ hours}$. **Answer: 6**.
- **Q16**: $7 - 5 = 2$. **Answer: 2**.
- **Q17**: $\omega = \sqrt{k/m}$. $\omega' = \sqrt{(2k)/(m/2)} = \sqrt{4k/m} = 2\omega_0 \implies k = 2$. **Answer: 2**.
- **Q18**: Maximum electrons in $n$-th shell $= 2n^2 = 2(3)^2 = 18$. **Answer: 18**.

---

## PART II: CHEMISTRY

### Q19. Cesium Chloride Structure
- **Analysis**: All four statements correctly describe the CsCl crystal lattice.
- **Correct Options**: **(A, B, C, D)**.

### Q20. Le Chatelier Equilibrium of $\text{PCl}_5$
- **Analysis**: All four statements are standard Le Chatelier principles.
- **Correct Options**: **(A, B, C, D)**.

### Q21. Victor Meyer Test
- **Analysis**: Victor Meyer test yields blood red color for primary alcohols (nitrolic acid), blue color for secondary alcohols (pseudonitrol), and colorless for tertiary alcohols. Hence it distinguishes $1^\circ, 2^\circ, 3^\circ$ alcohols from one another.
- **Correct Options**: **(A, B, C)**.

### Q22. High-Spin Outer Orbital Complexes
- **Analysis**:
  - $[\text{CoF}_6]^{3-}$: $d^6$ weak field $\implies sp^3d^2$ outer orbital. (A is correct).
  - $[\text{Fe}(\text{H}_2\text{O})_6]^{2+}$: $d^6$ weak field $\implies sp^3d^2$ outer orbital. (B is correct).
  - $[\text{Cr}(\text{NH}_3)_6]^{3+}$: $d^3$ uses vacant inner $3d$ orbitals $\implies d^2sp^3$. (C is incorrect).
  - $[\text{Ni}(\text{NH}_3)_6]^{2+}$: $d^8$ uses $4d$ orbitals $\implies sp^3d^2$ outer orbital. (D is correct).
- **Correct Options**: **(A, B, D)**.

### Q23. MacArthur-Forrest Leaching of Gold
- **Analysis**: All four statements correctly state metallurgical chemistry of gold extraction.
- **Correct Options**: **(A, B, C, D)**.

### Q24. First Order Reaction Kinetics
- **Analysis**: All four statements correctly describe first-order reaction kinetics.
- **Correct Options**: **(A, B, C, D)**.

### Q25–Q30 Numerical Solutions
- **Q25**: Overall: $\text{Zn} + \text{Cu}^{2+} \rightarrow \text{Zn}^{2+} + \text{Cu}$.
  $$Q = \frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]} = \frac{0.1}{0.01} = 10$$
  $$E_{\text{cell}} = 1.10 - \frac{0.06}{2}\log(10) = 1.10 - 0.03 = 1.07\text{ V}$$
  **Answer: 1.07**.
- **Q26**: Moles of $\text{CH}_4 = 3.2 / 16 = 0.20\text{ mol}$.
  Heat evolved $= 0.20 \times 890.0 = 178.0\text{ kJ}$. **Answer: 178 (or 178.0)**.
- **Q27**: $\text{C}_6\text{H}_{12}$ has 1 degree of unsaturation. Since it does not decolorize $\text{Br}_2$ water, it has no double bonds, meaning it must be a cycloalkane (1 ring). Number of rings $= 1$. **Answer: 1**.
- **Q28**: $\text{CaF}_2 \rightleftharpoons \text{Ca}^{2+} + 2\text{F}^- \implies K_{sp} = 4s^3 = 3.2 \times 10^{-11}$.
  $$s^3 = 8.0 \times 10^{-12} \implies s = 2.0 \times 10^{-4}\text{ mol/L} \implies A = 2.0$$
  **Answer: 2.0 (or 2)**.
- **Q29**: $t_{1/2} = \frac{0.693}{k} = \frac{0.693}{1.386 \times 10^{-2}} = 50\text{ minutes}$. **Answer: 50**.
- **Q30**: Raoult's law: $P = P_0 (1 - x_{\text{solute}}) = 23.8 (1 - 0.05) = 23.8(0.95) = 22.61 \approx 22.6\text{ mmHg}$. **Answer: 22.6**.

### Q31–Q36 Integer Solutions
- **Q31**: In $\text{K}_2\text{Cr}_2\text{O}_7$: $2(+1) + 2(x) + 7(-2) = 0 \implies 2x = 12 \implies x = +6$. **Answer: 6**.
- **Q32**: In solid $\text{Co}_2(\text{CO})_8$, there are 2 bridging carbonyl ligands. **Answer: 2**.
- **Q33**: Pyrophosphoric acid ($\text{H}_4\text{P}_2\text{O}_7$) has 4 acidic $\text{P-OH}$ groups, basicity $= 4$. **Answer: 4**.
- **Q34**: In CsCl, both ions have coordination number 8. **Answer: 8**.
- **Q35**: Complex $[M a_2 b_4]$ has 2 geometrical isomers: cis and trans. **Answer: 2**.
- **Q36**: Ethyl carbocation ($\text{CH}_3\text{CH}_2^+$) has 3 $\alpha$-hydrogens, giving 3 hyperconjugative no-bond resonance structures. **Answer: 3**.

---

## PART III: MATHEMATICS

### Q37. Function $x + 1/x$ Analysis
- **Analysis**: $f'(x) = 1 - 1/x^2 = 0 \implies x = \pm 1$. Local max at $x = -1$ ($f = -2$), local min at $x = 1$ ($f = 2$). Range is $(-\infty, -2] \cup [2, \infty)$.
- **Correct Options**: **(A, B, C, D)**.

### Q38. Geometry of Parabola
- **Analysis**: All four statements correctly state geometry of standard parabola $y^2 = 4ax$.
- **Correct Options**: **(A, B, C, D)**.

### Q39. Nilpotent Matrix Properties
- **Analysis**: All four statements are standard linear algebra theorems for nilpotent matrices.
- **Correct Options**: **(A, B, C, D)**.

### Q40. King's Property and Integral Symmetries
- **Analysis**: All four statements are standard definite integral theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q41. Elementary Probability Axioms
- **Analysis**: All four statements are standard probability theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q42. Vector Cross Product Properties
- **Analysis**: All four statements are standard vector algebra theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q43–Q48 Numerical Solutions
- **Q43**: Let $u = 1 + x^2 \implies du = 2x\,dx$.
  $$I = \frac{1}{2}\int_1^2 u^{-1/2}\,du = [\sqrt{u}]_1^2 = \sqrt{2} - 1 \approx 1.414 - 1 = 0.41$$
  **Answer: 0.41**.
- **Q44**: $\sqrt{3^2 + 4^2} = 5$. **Answer: 5**.
- **Q45**: Distance $d = \frac{|26 - (-13)|}{\sqrt{5^2 + (-12)^2}} = \frac{39}{13} = 3$. **Answer: 3**.
- **Q46**: $e = \sqrt{1 + 9/16} = \sqrt{25/16} = 5/4 = 1.25$. **Answer: 1.25**.
- **Q47**: $\frac{20 \times 21}{2} = 210$. **Answer: 210**.
- **Q48**: $\vec{a}\cdot\vec{b} = 2(1) + 1(-2) + (-1)(k) = 2 - 2 - k = -k = 0 \implies k = 0$. **Answer: 0**.

### Q49–Q54 Integer Solutions
- **Q49**: $4! = 24$. **Answer: 24**.
- **Q50**: Highest derivative is $\frac{d^2 y}{dx^2}$, which appears with power 3. Degree is 3. **Answer: 3**.
- **Q51**: $\lim_{x\to 0} \frac{\sin 3x}{\sin x} = 3$. **Answer: 3**.
- **Q52**: $|x| = -2$ has no real solutions because absolute value is non-negative. Number of solutions $= 0$. **Answer: 0**.
- **Q53**: Circle: $(x - 2)^2 + (y - 3)^2 = 12 + 4 + 9 = 25$. Radius $= 5$. **Answer: 5**.
- **Q54**: Sum of roots $= 7$. **Answer: 7**.
