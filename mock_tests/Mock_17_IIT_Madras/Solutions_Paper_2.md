# Detailed Solutions and Pedagogical Analysis — Mock Examination 17 (Paper 2)
### Organising Institute Style: IIT Madras (`IIT_MADRAS_STYLE` — 2024 Benchmark)

---

## PART I: PHYSICS

### Q1. Concentric Spherical Shells
- **Analysis**:
  - Inner charge $+Q$ induces $-Q$ on inner surface of outer shell and $+Q$ on outer surface. (A, B are True)
  - Electrostatic energy: $U = \frac{Q^2}{8\pi\varepsilon_0}\left(\frac{1}{R_1} - \frac{1}{R_2} + \frac{1}{R_3}\right)$. (C is True)
  - Grounding the outer shell sets its potential to 0, removing the outer surface charge. Potential of inner sphere becomes $V_1 = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q2. Coaxial Current Loops
- **Analysis**:
  - Axial field: $B(z) = \frac{\mu_0 I_1 a^2}{2(a^2 + z^2)^{3/2}}$. (A is True)
  - Flux through small loop: $\Phi = B(z) (\pi b^2) = \frac{\mu_0 \pi a^2 b^2 I_1}{2(a^2 + z^2)^{3/2}} \implies M = \frac{\mu_0 \pi a^2 b^2}{2(a^2 + z^2)^{3/2}}$. (B is True)
  - Force: $F_z = I_2 \frac{d\Phi}{dz} = -\frac{3\mu_0 \pi a^2 b^2 I_1 I_2 z}{2(a^2 + z^2)^{5/2}}$. (C is True)
  - Parallel currents attract. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q3. Parallel RL Circuit
- **Analysis**:
  - Across resistor: $i_R(t) = \frac{v(t)}{R} = \frac{V_0}{R}\cos(\omega t)$. (A is True)
  - Across inductor: $v(t) = L \frac{di_L}{dt} \implies i_L(t) = \frac{V_0}{\omega L}\sin(\omega t)$. (B is True)
  - Total current: $i(t) = i_R(t) + i_L(t) = V_0 \sqrt{\frac{1}{R^2} + \frac{1}{\omega^2 L^2}} \cos(\omega t - \phi)$. (C is True)
  - Current lags voltage by $\phi = \arctan(R / (\omega L))$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q4. Circular Polarization
- **Analysis**:
  - $E_x = E_0 \cos(kz - \omega t)$, $E_y = E_0 \sin(kz - \omega t) = E_0 \cos(kz - \omega t - \pi/2)$.
  - Components have equal amplitude and $\pi/2$ phase difference $\implies$ circular polarization.
  - Direction of rotation and constant amplitude.
- **Correct Options**: **(A, B, C, D)**.

### Q5. X-Ray Physics
- **Analysis**: Duane-Hunt law for $\lambda_{\min}$; Moseley's law $\sqrt{\nu} = a(Z - b)$ with $b = 1$ for $K_\alpha$.
- **Correct Options**: **(A, B, C, D)**.

### Q6. Exponential Equation of State
- **Analysis**:
  - $W = \int_0^\infty P_0 e^{-\alpha V}\,dV = \frac{P_0}{\alpha}$. (A is True)
  - $T = \frac{P V}{R} = \frac{P_0}{R} V e^{-\alpha V}$. Maximum at $\frac{d}{dV}[V e^{-\alpha V}] = (1 - \alpha V)e^{-\alpha V} = 0 \implies V = 1/\alpha$. (B is True)
  - $T_{\max} = \frac{P_0}{\alpha e R}$. (C is True)
  - Bulk modulus $B = -V \frac{dP}{dV} = -V [-\alpha P_0 e^{-\alpha V}] = \alpha P V$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q7. Pulling Force on Loop
- **Derivation**:
  - Induced EMF $\mathcal{E} = B L v = 0.50 \times 0.10 \times 4.0 = 0.20\text{ V}$.
  - Current $I = \frac{\mathcal{E}}{R} = \frac{0.20}{2.0} = 0.10\text{ A}$.
  - Force $F = I L B = 0.10 \times 0.10 \times 0.50 = 0.0050\text{ N}$.
- **Answer**: **0.005** (or **0.0050**).

### Q8. Magnetic Field Inside Capacitor
- **Derivation**:
  - $B(r) = \frac{\mu_0 I r}{2\pi R^2} = \frac{(4\pi \times 10^{-7}) \times 1.0 \times 0.025}{2\pi \times (0.050)^2} = \frac{2 \times 10^{-7} \times 0.025}{0.0025} = 2.0 \times 10^{-6}\text{ T} = 2.00\,\mu\text{T}$.
- **Answer**: **2.00** (or **2**).

### Q9. Distance of 3rd Dark Fringe
- **Derivation**:
  - Dark fringes occur at $y_n = (n - 1/2) \frac{\lambda D}{d}$.
  - For 3rd dark fringe, $n = 3 \implies y_3 = \frac{5}{2} \frac{\lambda D}{d} = 2.5 \times \frac{600 \times 10^{-9} \times 1.0}{0.50 \times 10^{-3}} = 2.5 \times 1.2 \times 10^{-3}\text{ m} = 3.0\text{ mm}$.
- **Answer**: **3.0** (or **3**).

### Q10. Threshold Wavelength
- **Derivation**:
  $$\lambda_0 = \frac{hc}{\Phi} = \frac{1240}{2.14} \approx 579\text{ nm}$$
- **Answer**: **579**.

### Q11. Refraction through Equilateral Prism
- **Derivation**:
  - $A = 60^\circ$, $i = 45^\circ$, $\mu = \sqrt{2}$.
  - Snell's law at first face: $\sin 45^\circ = \sqrt{2}\sin r_1 \implies \frac{1}{\sqrt{2}} = \sqrt{2}\sin r_1 \implies \sin r_1 = \frac{1}{2} \implies r_1 = 30^\circ$.
  - $r_2 = A - r_1 = 60^\circ - 30^\circ = 30^\circ$.
  - Snell's law at second face: $\sqrt{2}\sin 30^\circ = \sin e \implies \sqrt{2}(1/2) = \frac{1}{\sqrt{2}} = \sin e \implies e = 45^\circ$.
- **Answer**: **45**.

### Q12. Electric Heater Power
- **Derivation**:
  - Total heat $Q = m L_v = 1.0 \times 2.26 \times 10^6\text{ J}$.
  - Time $t = 20.0 \times 60 = 1200\text{ s}$.
  - $P = \frac{Q}{t} = \frac{2.26 \times 10^6}{1200} \approx 1883\text{ W}$.
- **Answer**: **1883**.

### Q13. Divergence Equations of Maxwell
- **Derivation**: Two equations: Gauss's law for electricity ($\nabla \cdot \vec{E} = \rho/\varepsilon_0$) and Gauss's law for magnetism ($\nabla \cdot \vec{B} = 0$).
- **Answer**: **2**.

### Q14. Harmonics Ratio
- **Derivation**: In an open organ pipe, harmonics are $f_1, 2f_1, 3f_1, 4f_1, \dots$. Fourth harmonic is $4f_1$, second harmonic is $2f_1$. Ratio is $4/2 = 2$.
- **Answer**: **2**.

### Q15. Beta Decays in Thorium Series
- **Derivation**:
  - $82 = 90 - 2(6) + N_\beta = 90 - 12 + N_\beta = 78 + N_\beta \implies N_\beta = 4$.
- **Answer**: **4**.

### Q16. Vibrational Modes of Linear Triatomic Molecule
- **Derivation**: Degrees of freedom $= 3N - 5 = 3(3) - 5 = 4$.
- **Answer**: **4**.

### Q17. Period Scaling
- **Derivation**: $T \propto \sqrt{m}$. When mass doubles, $T \rightarrow \sqrt{2} T = 3\sqrt{2} \implies k = 2$.
- **Answer**: **2**.

### Q18. Maximum Electrons in n = 3 Shell
- **Derivation**: $2n^2 = 2(3^2) = 18$.
- **Answer**: **18**.

---

## PART II: CHEMISTRY

### Q19. Rusting of Iron
- **Analysis**: All four statements correctly state anodic oxidation, cathodic reduction of oxygen, role of carbonic acid, and hydrated ferric oxide composition.
- **Correct Options**: **(A, B, C, D)**.

### Q20. Octahedral Complexes
- **Analysis**:
  - $[\text{Co}(\text{NH}_3)_6]^{3+}$ is low-spin diamagnetic ($t_{2g}^6$). (A is True)
  - $[\text{CoF}_6]^{3-}$ has weak field $\text{F}^-$, high-spin $t_{2g}^4 e_g^2$ with 4 unpaired electrons. (B is True)
  - $[\text{Fe}(\text{CN})_6]^{4-}$ is low-spin diamagnetic ($t_{2g}^6$). (C is True)
  - Higher oxidation state increases $\Delta_o$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q21. Oxoacids of Phosphorus
- **Analysis**: $\text{H}_3\text{PO}_2$ monobasic; $\text{H}_3\text{PO}_3$ dibasic; $\text{H}_3\text{PO}_4$ tribasic; $\text{P}-\text{H}$ bonds dictate reducing power.
- **Correct Options**: **(A, B, C, D)**.

### Q22. Hofmann Bromamide Degradation
- **Analysis**: Decarbonylation, isocyanate intermediate, retention of configuration during 1,2-migration, concerted mechanism.
- **Correct Options**: **(A, B, C, D)**.

### Q23. Extraction of Copper
- **Analysis**: Copper matte composition, silica slagging iron, auto-reduction of $\text{Cu}_2\text{S}$ with $\text{Cu}_2\text{O}$, blister copper.
- **Correct Options**: **(A, B, C, D)**.

### Q24. Coagulation of Colloids
- **Analysis**: Hardy-Schulze rule, flocculation values, inverse relationship with coagulating power.
- **Correct Options**: **(A, B, C, D)**.

### Q25. Copper Deposition Mass
- **Derivation**:
  $$m = \frac{M I t}{n F} = \frac{63.5 \times 3.0 \times 1930}{2 \times 96500} = \frac{63.5 \times 3.0 \times 1}{2 \times 50} = \frac{190.5}{100} = 1.91\text{ g}$$
- **Answer**: **1.91**.

### Q26. Solubility of CaSO4 in g/L
- **Derivation**:
  - $s = \sqrt{K_{sp}} = \sqrt{2.4 \times 10^{-5}} = 4.90 \times 10^{-3}\text{ mol/L}$.
  - Solubility in g/L $= 4.90 \times 10^{-3} \times 136.0 = 0.666 \approx 0.67\text{ g/L}$.
- **Answer**: **0.67**.

### Q27. Rate Constant Increase Factor
- **Derivation**:
  $$\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{10}{300 \times 310}\right) = \frac{50000}{8.314} \times \frac{10}{93000} = \frac{500000}{773202} \approx 0.647$$
  $$\frac{k_2}{k_1} = e^{0.647} = 1.91$$
- **Answer**: **1.91**.

### Q28. Freezing Point Depression of Complex Salt
- **Derivation**:
  - $\text{K}_3[\text{Fe}(\text{CN})_6] \rightarrow 3\text{K}^+ + [\text{Fe}(\text{CN})_6]^{3-} \implies i = 4$.
  - $\Delta T_f = i K_f m = 4 \times 1.86 \times 0.010 = 0.0744\text{ K} \approx 0.074\text{ K}$.
- **Answer**: **0.074**.

### Q29. Heat Absorbed in Isothermal Expansion
- **Derivation**:
  $$Q = W = n R T \ln(V_2/V_1) = 1.0 \times 8.314 \times 300 \times 2.303 = 5744\text{ J}$$
- **Answer**: **5744**.

### Q30. Solubility of AgCl
- **Derivation**:
  $$s = \frac{1000 \kappa}{\Lambda_m^\circ} = \frac{1000 \times (1.38 \times 10^{-6})}{138.0} = 1.0 \times 10^{-5}\text{ mol/L} = 10\,\mu\text{mol/L}$$
- **Answer**: **10**.

### Q31. Oxidation State of Fe in Brown Ring
- **Derivation**: In $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]^{2+}$, $\text{NO}$ is $\text{NO}^+ \implies x + 5(0) + (+1) = +2 \implies x = +1$.
- **Answer**: **1**.

### Q32. Bridging Carbonyls in Fe3(CO)12
- **Derivation**: $\text{Fe}_3(\text{CO})_{12}$ contains 2 bridging carbonyl ligands and 10 terminal carbonyl ligands.
- **Answer**: **2**.

### Q33. Basicity of Pyrophosphoric Acid
- **Derivation**: $\text{H}_4\text{P}_2\text{O}_7$ has 4 ionizable $-\text{OH}$ groups $\implies$ basicity = 4.
- **Answer**: **4**.

### Q34. Coordination Number in HCP
- **Derivation**: HCP lattice has coordination number = 12.
- **Answer**: **12**.

### Q35. Geometrical Isomers of [Pt(NH3)2Cl4]
- **Derivation**: Octahedral $[M a_2 b_4]$ has 2 geometrical isomers: cis and trans.
- **Answer**: **2**.

### Q36. Sigma Bonds in Toluene
- **Derivation**: Benzene ring has 6 $\text{C}-\text{C}$ and 5 $\text{C}-\text{H}$ $\sigma$-bonds; methyl group has 1 $\text{C}-\text{C}$ and 3 $\text{C}-\text{H}$ $\sigma$-bonds. Total $= 6 + 5 + 1 + 3 = 15$.
- **Answer**: **15**.

---

## PART III: MATHEMATICS

### Q37. Cosine Inequality Analysis
- **Analysis**:
  - $f(0) = 0$. (A is True)
  - $f'(x) = -\sin x + x \ge 0$ for all $x \ge 0$ since $x \ge \sin x$. (B is True)
  - Since $f'(x) \ge 0$ and $f(0) = 0$, $f(x) \ge 0$ for $x \ge 0$. Since $f(x)$ is even, $f(x) \ge 0$ for all $x \in \mathbb{R}$. (C is True)
  - $\cos x \ge 1 - \frac{x^2}{2}$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q38. Ellipse Properties
- **Analysis**:
  - $\frac{x^2}{16} + \frac{y^2}{9} = 1 \implies a = 4, b = 3$.
  - $c = \sqrt{16 - 9} = \sqrt{7} \implies$ foci $(\pm\sqrt{7}, 0)$, $e = \sqrt{7}/4$. (A, B are True)
  - Latus rectum $2b^2/a = 2(9)/4 = 9/2$. (C is True)
  - Auxiliary circle $x^2 + y^2 = a^2 = 16$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q39. Nilpotent Matrices
- **Analysis**:
  - $\lambda^3 = 0 \implies \lambda = 0$. (A is True)
  - $\det(A) = 0$, $\text{tr}(A) = 0$. (B, C are True)
  - Eigenvalues of $I + A$ are $1 + \lambda = 1 \implies \det(I + A) = 1$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q40. Definite Integral
- **Analysis**:
  - Standard contour / substitution integral: $\int_0^{2\pi} \frac{dx}{a + \cos x} = \frac{2\pi}{\sqrt{a^2 - 1}}$.
  - For $a = 2$: $\frac{2\pi}{\sqrt{4 - 1}} = \frac{2\pi}{\sqrt{3}}$. (A is True)
  - By symmetry, integral over $[0, \pi]$ is half: $\frac{\pi}{\sqrt{3}}$. (B is True)
  - Integrand is $2\pi$-periodic and strictly positive. (C, D are True)
- **Correct Options**: **(A, B, C, D)**.

### Q41. Binomial Distribution
- **Analysis**:
  - $n = 6, p = 1/2$.
  - Exactly 3 heads: $\binom{6}{3}(1/2)^6 = \frac{20}{64} = \frac{5}{16}$. (A is True)
  - At least 4 heads: $\frac{15 + 6 + 1}{64} = \frac{22}{64} = \frac{11}{32}$. (B is True)
  - 6 heads: $(1/2)^6 = 1/64$. (C is True)
  - Mean $E = np = 6(1/2) = 3$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q42. Vector Triple Product
- **Analysis**:
  - $(\vec{a}\cdot\vec{c})\vec{b} - (\vec{a}\cdot\vec{b})\vec{c} = \frac{1}{2}\vec{b}$. (A is True)
  - Since $\vec{b}$ and $\vec{c}$ are non-collinear: $\vec{a}\cdot\vec{c} = 1/2$ and $\vec{a}\cdot\vec{b} = 0$. (B is True)
  - $\cos\theta_{ac} = 1/2 \implies \theta_{ac} = \pi/3$. (C is True)
  - $\cos\theta_{ab} = 0 \implies \theta_{ab} = \pi/2$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q43. Integration by Parts
- **Derivation**:
  $$\int_0^1 x e^x\,dx = [x e^x - e^x]_0^1 = (e - e) - (0 - 1) = 1.00$$
- **Answer**: **1.00** (or **1**).

### Q44. Maximum of 3 sin x + 4 cos x
- **Derivation**: $\sqrt{3^2 + 4^2} = \sqrt{25} = 5$.
- **Answer**: **5**.

### Q45. Distance Between Parallel Planes
- **Derivation**:
  $$d = \frac{|4 - (-5)|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{9}{\sqrt{9}} = \frac{9}{3} = 3$$
- **Answer**: **3**.

### Q46. Transverse Axis of Hyperbola
- **Derivation**: $a^2 = 25 \implies a = 5$. Transverse axis $= 2a = 10$.
- **Answer**: **10**.

### Q47. Sum of AP
- **Derivation**:
  - $a = 5, d = 3, n = 15$.
  - $S_{15} = \frac{15}{2}[2(5) + 14(3)] = \frac{15}{2}[10 + 42] = \frac{15}{2}(52) = 15 \times 26 = 390$.
- **Answer**: **390**.

### Q48. Orthogonal Vectors
- **Derivation**:
  $$\vec{u} \cdot \vec{v} = 3(2) - 1(4) + 2(-k) = 6 - 4 - 2k = 2 - 2k = 0 \implies k = 1$$
- **Answer**: **1**.

### Q49. Permutations of "INDIA"
- **Derivation**: 5 letters with two I's $\implies \frac{5!}{2!} = \frac{120}{2} = 60$.
- **Answer**: **60**.

### Q50. Order of Differential Equation
- **Derivation**: Highest derivative is $\frac{dy}{dx} \implies$ order is 1.
- **Answer**: **1**.

### Q51. Limit Calculation
- **Derivation**:
  $$\lim_{x \to 0} \frac{\tan 5x}{\sin 2x} = \frac{5}{2} \implies a = 5, b = 2 \implies a + b = 7$$
- **Answer**: **7**.

### Q52. Real Solutions of x^2 + 1 = 0
- **Derivation**: Roots are $\pm i$, which are purely imaginary $\implies 0$ real solutions.
- **Answer**: **0**.

### Q53. Radius of Circle
- **Derivation**:
  - Center $(3, 4)$, $c = 0$.
  - $R = \sqrt{3^2 + 4^2 - 0} = \sqrt{25} = 5$.
- **Answer**: **5**.

### Q54. Sum of Roots
- **Derivation**: For $x^2 - 14x + 45 = 0$, sum of roots is $-(-14)/1 = 14$.
- **Answer**: **14**.
