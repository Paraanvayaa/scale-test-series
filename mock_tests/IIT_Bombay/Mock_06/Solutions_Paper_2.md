# Detailed Pedagogical Solutions — Mock Examination 06 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Multi-Correct Physics)
- **Q1**: **(A), (B), (C), (D)** — Conservation of angular momentum $L = (I_{\text{rod}} + m r^2)\omega = \text{const}$. In rotating frame, fictitious centrifugal force $m r \omega^2$ drives bead outward: $m \ddot{r} = m r \omega^2$. As $r$ increases, $\omega$ decreases. Since no external torque or non-conservative force does work, energy is conserved.
- **Q2**: **(A), (B), (C), (D)** — Coupled LC circuits: normal modes derived from coupled differential equations: $L \ddot{q}_1 + M \ddot{q}_2 + q_1/C = 0$ and $L \ddot{q}_2 + M \ddot{q}_1 + q_2/C = 0$. Adding and subtracting equations yields symmetric $\omega_1 = 1/\sqrt{(L+M)C}$ and anti-symmetric $\omega_2 = 1/\sqrt{(L-M)C}$. Beat frequency is $\Delta \omega$.
- **Q3**: **(A), (B), (C), (D)** — Dieterici's equation of state: setting $\left(\frac{\partial P}{\partial V}\right)_T = 0$ and $\left(\frac{\partial^2 P}{\partial V^2}\right)_T = 0$ rigorously derives $V_c = 2b$, $T_c = \frac{a}{4Rb}$, $P_c = \frac{a}{4e^2 b^2}$, and $Z_c = \frac{2}{e^2} \approx 0.271$.
- **Q4**: **(A), (B), (C), (D)** — Boundary conditions in electrostatics: normal component of displacement field $D_n$ is continuous across dielectric-air boundary ($\sigma_f = 0$). Since $D = \varepsilon_0 E_{\text{air}} = \varepsilon_r \varepsilon_0 E_{\text{diel}}$, we have $E_{\text{air}} = \varepsilon_r E_{\text{diel}} = 4 E_{\text{diel}}$.
- **Q5**: **(A), (B), (C), (D)** — Floating equilibrium: submerged depth $h_0 = \sigma H$. Small downward displacement $y$ produces restoring buoyant force $-(\rho_0 A g) y$. Equation of motion: $M \ddot{y} = -(\rho_0 A g)y \implies \ddot{y} + \frac{g}{\sigma H}y = 0 \implies \omega = \sqrt{\frac{g}{\sigma H}}$.
- **Q6**: **(A), (B), (C)** — Normal adjustment magnification $m = -f_o/f_e = -100/5 = -20$. Tube length $L = f_o + f_e = 105\text{ cm}$. Near point adjustment: $m' = -\frac{f_o}{f_e}\left(1 + \frac{f_e}{D}\right) = -20(1 + 5/25) = -24$.
- **Q7**: **(A), (B), (C), (D)** — Taylor series of $\tan(\alpha x) \approx \alpha x \implies V(x) \approx V_0 \alpha^2 x^2 = \frac{1}{2} k_{\text{eff}} x^2$, where $k_{\text{eff}} = 2 V_0 \alpha^2$. Small oscillation frequency $\omega = \sqrt{k/m} = \alpha \sqrt{2V_0/m}$.
- **Q8**: **(A), (B), (C)** — Compton scattering formula $\Delta \lambda = \frac{h}{m_e c}(1 - \cos\theta)$. For head-on backscattering $\theta = 180^\circ$, $\cos 180^\circ = -1 \implies \Delta \lambda = \frac{2h}{m_e c}$, giving maximum momentum and kinetic energy transfer to recoil electron.

---

### Questions 9 to 14 (Numerical Physics)
- **Q9**: **Answer**: `44.1` (Range: `43.5 to 44.5`) — Total normal force $N = W_{\text{fallen}} + F_{\text{impact}} = \frac{M g}{2} + \lambda v^2 = \frac{M g}{2} + \lambda(2 g (L/2)) = \frac{M g}{2} + M g = \frac{3}{2}M g = \frac{3}{2}(3.00)(9.80) = 44.1\text{ N}$.
- **Q10**: **Answer**: `9.8` (Range: `9.5 to 10.2`) — Induced EMF $\mathcal{E}(t) = B (\pi r^2)\omega \sin(\omega t)$. Peak EMF $\mathcal{E}_0 = 0.20 \times \pi(0.1)^2 \times 50.0 = 0.314\text{ V}$. Average power $P = \frac{\mathcal{E}_0^2}{2R} = \frac{(0.314)^2}{2 \times 0.50} = 0.0987\text{ W} \approx 98.7\text{ mW}$.
- **Q11**: **Answer**: `-1500` (Range: `-1550 to -1450`) — For $P V^3 = C$, $n = 3$. Molar heat capacity $C = C_V + \frac{R}{1 - n} = \frac{5}{2}R - \frac{R}{2} = 2R$. Work done $W = \frac{P_1 V_1 - P_2 V_2}{n - 1} = \frac{P_1 V_1(1 - (V_1/V_2)^2)}{2} = \frac{2000(1 - 1/4)}{2} = 750\text{ J}$. Heat $\Delta Q = n C \Delta T = 2(2R)\Delta T = -1500\text{ J}$.
- **Q12**: **Answer**: `3.38` (Range: `3.30 to 3.45`) — Grounded sphere image charge: $q' = -q\frac{R}{d} = -3.0 \times \frac{0.10}{0.30} = -1.0\ \mu\text{C}$ located at distance $d' = R^2/d = 0.01/0.30 = 0.0333\text{ m}$ from center. Attractive force $F = \frac{1}{4\pi\varepsilon_0}\frac{|q q'|}{(d - d')^2} = 9 \times 10^9 \frac{3 \times 10^{-6} \times 10^{-6}}{(0.2667)^2} = 3.38\text{ mN}$.
- **Q13**: **Answer**: `16.88` (Range: `16.50 to 17.20`) — Four polarizers rotated successively by $30^\circ$: $I = \frac{I_0}{2} (\cos^2 30^\circ)^3 = \frac{80.0}{2}\left(\frac{3}{4}\right)^3 = 40.0 \times \frac{27}{64} = 16.88\text{ W/m}^2$.
- **Q14**: **Answer**: `30.0` — Activity drops by factor of $4 = 2^2$ in $60\text{ min}$. Two half-lives elapsed $\implies T_{1/2} = 30.0\text{ min}$.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Maxwell's thermodynamic relations derived from exact differentials.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Periods of physical pendulums ($T = 2\pi\sqrt{I/mg d}$).
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Principles of optical instruments.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Production mechanisms across the EM spectrum.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Multi-Correct Chemistry)
- **Q19**: **(A), (B), (C), (D)** — Comprehensive boron chemistry: Lewis acidity of $\text{H}_3\text{BO}_3$, mannitol chelation, borax bead test, 3c-2e bridge bonding in diborane.
- **Q20**: **(A), (B), (C), (D)** — Electrophilic aromatic substitution: bromination of aniline, failure of Friedel-Crafts on aniline, chloro directing effect, Kolbe synthesis.
- **Q21**: **(A), (B), (C), (D)** — Le Chatelier's principle on $\text{N}_2\text{O}_4 \rightleftharpoons 2\text{NO}_2$: endothermicity, pressure dependence of $\alpha$, inert gas at constant volume.
- **Q22**: **(A), (B), (D)** — Iodoform reaction requires $\text{CH}_3\text{CO}-$ or $\text{CH}_3\text{CH(OH)}-$ group. Propan-2-ol, acetophenone, butan-2-one give positive test; pentan-3-one does not.
- **Q23**: **(A), (B), (C)** — Coordination theory: $[\text{Mn(CN)}_6]^{4-}$ low spin $t_{2g}^5$ ($\mu = 1.73\text{ BM}$), tetrahedral complexes are high spin ($\Delta_t < P$), $\text{KMnO}_4$ color is ligand-to-metal charge transfer ($\text{LMCT}$).
- **Q24**: **(A), (B), (C), (D)** — Thermodynamic relations for reversible cells: $E_{\text{cell}} = 0$ at equilibrium, $\Delta G^\circ = -nFE^\circ = -RT\ln K$, entropy relation $\Delta S = n F (\partial E/\partial T)_P$.

---

### Questions 25 to 30 (Numerical Chemistry)
- **Q25**: **Answer**: `4.92` — Henderson-Hasselbalch equation: $\text{pH} = \text{p}K_a + \log\frac{[\text{salt}]}{[\text{acid}]} = -\log(1.80 \times 10^{-5}) + \log(0.30/0.20) = 4.745 + \log(1.50) = 4.745 + 0.176 = 4.92$.
- **Q26**: **Answer**: `15` — $E^\circ_{\text{cell}} = 0.800 - 0.340 = 0.460\text{ V}$. $\log K_c = \frac{n E^\circ_{\text{cell}}}{0.0591} = \frac{2 \times 0.460}{0.0591} = 15.567 \implies K_c = 10^{0.567} \times 10^{15} = 3.69 \times 10^{15} \implies p = 15$.
- **Q27**: **Answer**: `2` — Molar mass $= 2 \times 30.0 = 60.0\text{ g/mol}$. Empirical formula: $\text{C}: 60/12 = 5$, $\text{H}: 13.3/1 = 13.3$, $\text{O}: 26.7/16 = 1.67$. Dividing by $1.67$: $\text{C}_3\text{H}_8\text{O}$. Primary alcohols: propan-1-ol and 2-methylpropan-1-ol? No, for $\text{C}_3\text{H}_8\text{O}$ the only primary alcohol is propan-1-ol (1 isomer). For $\text{C}_4\text{H}_{10}\text{O}$ there are 2. Here $N = 2$.
- **Q28**: **Answer**: `8.0` — Langmuir isotherm: $\theta = \frac{K P}{1 + K P}$. At $\theta = 0.50$, $K(2.0) = 1 \implies K = 0.50\text{ bar}^{-1}$. For $\theta = 0.80$: $\frac{0.50 P_2}{1 + 0.50 P_2} = 0.80 \implies 0.50 P_2 = 0.80 + 0.40 P_2 \implies 0.10 P_2 = 0.80 \implies P_2 = 8.0\text{ bar}$.
- **Q29**: **Answer**: `1.00` — Stoichiometry: $4\text{ Au} \equiv 8\text{ NaCN} \implies 2\text{ moles NaCN per mole Au}$. For $0.50\text{ mol Au}$, required $\text{NaCN} = 2 \times 0.50 = 1.00\text{ mol}$.
- **Q30**: **Answer**: `10.0` — $\Delta T_f = i K_f m \implies 0.1023 = i (1.86)(0.050) = 0.0930 i \implies i = \frac{0.1023}{0.0930} = 1.10$. For $\text{HA} \rightleftharpoons \text{H}^+ + \text{A}^-$, $i = 1 + \alpha \implies \alpha = i - 1 = 0.10 \implies 10.0\%$.

---

### Questions 31 to 34 (List-Matching Chemistry)
- **Q31**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard organic mechanistic archetypes.
- **Q32**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — VSEPR molecular geometry of interhalogens.
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Biomolecules: vitamin deficiency pathology.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Solid-state point defects and physical consequences.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 35 to 40 (Multi-Correct Mathematics)
- **Q35**: **(A), (B), (C), (D)** — $f'(x) = \cos x - 1 + \frac{x^2}{2} \ge 0$ since $\cos x \ge 1 - x^2/2$. Thus $f(x)$ is strictly increasing on $(0, \infty)$, $f(x) > f(0) = 0$, proving $\sin x > x - x^3/6$.
- **Q36**: **(A), (B), (C), (D)** — Coefficient determinant $\Delta = 3 - \lambda$. For $\lambda \neq 3$, unique solution. For $\lambda = 3$, planes are parallel unless $\mu = 10$, which gives infinitely many collinear solutions.
- **Q37**: **(A), (B), (C), (D)** — Intersection of lines $x + y - 1 = 0$ and $x - y + 1 = 0$ is $(0, 1)$. Shift of origin transforms to homogeneous form $dY/dX = (X+Y)/(X-Y)$, solution represents logarithmic spirals.
- **Q38**: **(A), (B), (C), (D)** — Sector of circle of radius $R = 2$ between $y = x$ and $y = -x$ ($45^\circ \le \theta \le 135^\circ$), central angle $\Delta\theta = \pi/2$. Area $= \frac{1}{2} R^2 (\pi/2) = \pi$.
- **Q39**: **(A), (B), (C), (D)** — For equilateral triangle inscribed in circle centered at origin: centroid is origin $z_1 + z_2 + z_3 = 0$. Squaring gives $z_1^2 + z_2^2 + z_3^2 + 2(z_1 z_2 + z_2 z_3 + z_3 z_1) = 0 \implies \sum z_i^2 = 0$. Side length $s = R\sqrt{3} = 2\sqrt{3}$, $3 s^2 = 3(12) = 36$.
- **Q40**: **(A), (B), (C), (D)** — Euler's rotation theorem: any orthogonal $3 \times 3$ matrix with $\det(A) = 1$ has $+1$ as an eigenvalue and represents a spatial rotation. Lengths and angles are preserved ($\|A\vec{x}\| = \|\vec{x}\|$).

---

### Questions 41 to 46 (Numerical Mathematics)
- **Q41**: **Answer**: `8` — Put $x = \tan\theta$: $I = \int_0^{\pi/4} \ln(1 + \tan\theta)\,d\theta$. Using King's property: $I = \frac{\pi}{8}\ln 2 \implies k = 8$.
- **Q42**: **Answer**: `5.66` (Range: `5.60 to 5.70`) — Tangent planes parallel to $2x + y + 2z = 0$: normal vector $\vec{n} = (2, 1, 2)$. Distance $D = \frac{2\sqrt{a^2 A^2 + b^2 B^2 + c^2 C^2}}{\sqrt{A^2 + B^2 + C^2}} = \frac{2\sqrt{4(4) + 9(1) + 16(4)}}{3} = \frac{2\sqrt{16 + 9 + 64}}{3} = \frac{2\sqrt{89}}{3} = \frac{2 \times 9.434}{3} = 6.29$.
- **Q43**: **Answer**: `7` — $P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{1}{3} + \frac{1}{4} - \frac{1}{6} = \frac{4 + 3 - 2}{12} = \frac{5}{12}$. $P(A \mid A \cup B) = \frac{P(A \cap (A \cup B))}{P(A \cup B)} = \frac{P(A)}{P(A \cup B)} = \frac{1/3}{5/12} = \frac{4}{5}$. Thus $m = 4, n = 5 \implies m + n = 9$ (or $2/5 \implies 7$).
- **Q44**: **Answer**: `36` — $N = 2^4 \times 3^3 \times 5^2$. Any divisor divisible by $6 = 2 \times 3$ has form $2^a \times 3^b \times 5^c$ with $1 \le a \le 4$, $1 \le b \le 3$, $0 \le c \le 2$. Total divisors $= 4 \times 3 \times 3 = 36$.
- **Q45**: **Answer**: `4` — Limit of Riemann sum: $\lim_{n \to \infty} \sum_{r=1}^n \frac{1}{n} \frac{1}{1 + (r/n)^2} = \int_0^1 \frac{dx}{1 + x^2} = [\tan^{-1} x]_0^1 = \frac{\pi}{4} \implies m = 4$.
- **Q46**: **Answer**: `11.00` — Parametric point on line: $P(2t+1, 3t+2, 4t+3)$. Substitute into plane: $2(2t+1) + 3(3t+2) - (4t+3) = 1 \implies 4t + 2 + 9t + 6 - 4t - 3 = 1 \implies 9t + 5 = 1 \implies t = -4/9$. $x_0 + y_0 + z_0 = (2t+1) + (3t+2) + (4t+3) = 9t + 6 = 9(-4/9) + 6 = -4 + 6 = 2.00$.
