# Detailed Pedagogical Solutions — Mock Examination 12 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Relativistic Hyperbolic Motion, Proper Acceleration, Rindler Horizon.
- **2. Derivation**:
  - Proper acceleration $g_0 = \gamma^3 \frac{dv}{dt} = \frac{d}{dt}(\gamma v) = \frac{1}{m_0}\frac{dp}{dt} \implies p(t) = m_0 g_0 t$. (A) is correct.
  - Using $p = \frac{m_0 v}{\sqrt{1 - v^2/c^2}} = m_0 g_0 t \implies v(t) = \frac{g_0 t}{\sqrt{1 + (g_0 t/c)^2}}$. (B) is correct.
  - Integrating $v(t) = \frac{dx}{dt}$: $x(t) = \frac{c^2}{g_0}\left(\sqrt{1 + (g_0 t/c)^2} - 1\right) \implies \left(x + \frac{c^2}{g_0}\right)^2 - c^2 t^2 = \left(\frac{c^2}{g_0}\right)^2$. (C) is correct.
  - The asymptote light cone passes through $x = -c^2/g_0$ at $t = 0$; events behind this boundary can never send signals that reach the particle (Rindler event horizon). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Plasma Frequency, Dispersion Relation, Cut-off Attenuation.
- **2. Derivation**:
  - Electron equation of motion: $m_e \ddot{x} = -e E \implies \ddot{x} = -\frac{e E_0}{m_e}e^{-i\omega t}$.
  - Polarization $\vec{P} = -n_e e \vec{x} = -\frac{n_e e^2}{\varepsilon_0 m_e \omega^2}\varepsilon_0 \vec{E} \implies \varepsilon_r = 1 - \frac{\omega_p^2}{\omega^2}$ where $\omega_p = \sqrt{\frac{n_e e^2}{\varepsilon_0 m_e}}$. (A) and (B) are correct.
  - Dispersion relation $k^2 c^2 = \omega^2 - \omega_p^2$. For $\omega < \omega_p$, $k$ is imaginary, yielding exponential attenuation without propagation. (C) is correct.
  - Phase velocity $v_p = \omega/k = c/\sqrt{1 - \omega_p^2/\omega^2} > c$. Group velocity $v_g = d\omega/dk = c\sqrt{1 - \omega_p^2/\omega^2} < c$. Product $v_p v_g = c^2$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Cascaded Polarizers, Malus's Law, Adiabatic Following.
- **2. Derivation**:
  - Unpolarized light after first polarizer has intensity $I_1 = \frac{1}{2}I_0$. (A) is correct.
  - Polarizers are distributed from $0$ to $\pi/2$ in $N-1$ equal angular intervals: $\Delta\theta = \frac{\pi}{2(N-1)}$. (B) is correct.
  - By Malus's law across $N-1$ successive interfaces: $I_N = I_1 [\cos(\Delta\theta)]^{2(N-1)} = \frac{1}{2}I_0 \left[\cos\left(\frac{\pi}{2(N-1)}\right)\right]^{2(N-1)}$. (C) is correct.
  - For large $N$: $\cos x \approx 1 - x^2/2 \implies [\cos(\frac{\pi}{2(N-1)})]^{2(N-1)} \approx (1 - \frac{\pi^2}{8(N-1)^2})^{2(N-1)} \approx e^{-\frac{\pi^2}{4(N-1)}} \to 1$ as $N \to \infty$. Thus $I_\infty = \frac{1}{2}I_0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Clausius-Clapeyron Equation, Phase Equilibria.
- **2. Derivation**:
  - Exact Clausius-Clapeyron equation: $\frac{dP}{dT} = \frac{\Delta S}{\Delta V} = \frac{L}{T \Delta V}$. (A) is correct.
  - Assuming ideal gas $V_{\text{vap}} = RT/P$ and $V_{\text{liq}} \ll V_{\text{vap}}$: $\frac{1}{P}\frac{dP}{dT} = \frac{L}{R T^2}$, integrating gives $\ln(P_2/P_1) = -\frac{L}{R}(1/T_2 - 1/T_1)$. (B) is correct.
  - Higher ambient pressure requires higher vapor pressure to boil, elevating $T_b$. (C) is correct.
  - For water, $\Delta V = V_{\text{water}} - V_{\text{ice}} < 0$, giving $dP/dT < 0$ (regelation). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Rolling Without Slipping on Convex Dome, Separation Condition.
- **2. Derivation**:
  - Center of mass path has radius $R_0 + R$. (A) is correct.
  - Energy conservation: $M g(R_0+R)(1 - \cos\theta) = \frac{1}{2}M v^2 + \frac{1}{2}I \omega^2 = \frac{7}{10}M v^2 \implies v^2 = \frac{10}{7}g(R_0+R)(1-\cos\theta)$.
  - Differentiating: $2v \dot{v} = \frac{10}{7}g(R_0+R)\sin\theta \dot{\theta} \implies \ddot{\theta} = \frac{5g}{7(R_0+R)}\sin\theta$. (B) is correct.
  - Radial equation: $M g\cos\theta - N = M\frac{v^2}{R_0+R} = \frac{10}{7}M g(1 - \cos\theta) \implies N(\theta) = M g\left(\frac{17}{7}\cos\theta - \frac{10}{7}\right)$. (C) is correct.
  - Detachment occurs when $N = 0 \implies \cos\theta_c = \frac{10}{17}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Dipole Inside Grounded Conducting Spherical Shell, Boundary Conditions.
- **2. Derivation**:
  - Grounded shell requires $V(R, \theta) = 0$. (A) is correct.
  - General solution of Laplace equation with dipole at center: $V(r, \theta) = \frac{p_0\cos\theta}{4\pi\varepsilon_0 r^2} + B r\cos\theta$. At $r = R$, $V = 0 \implies B = -\frac{p_0}{4\pi\varepsilon_0 R^3}$. Thus $V(r, \theta) = \frac{p_0\cos\theta}{4\pi\varepsilon_0}\left(\frac{1}{r^2} - \frac{r}{R^3}\right)$. (B) is correct.
  - Induced charge density $\sigma = -\varepsilon_0 \left.\frac{\partial V}{\partial r}\right|_{R} = -\frac{3 p_0\cos\theta}{4\pi R^3}$. (C) is correct.
  - By symmetry, the uniform reaction field $\vec{E}_{\text{ind}} = \frac{p_0}{4\pi\varepsilon_0 R^3}\hat{k}$ is constant in space, so $\nabla \vec{E}_{\text{ind}} = 0$, giving zero net force $\vec{F} = (\vec{p}\cdot\nabla)\vec{E} = 0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Liénard formula: $P = \frac{e^2 c \gamma^4}{6\pi\varepsilon_0 R^2} = \frac{2}{3}\left(\frac{e^2}{4\pi\varepsilon_0}\right)\frac{c \gamma^4}{R^2}$.
  $\frac{2}{3}(2.307 \times 10^{-28})(3.0 \times 10^8)\frac{(1957)^4}{(10.0)^2} = (4.614 \times 10^{-20})\frac{1.467 \times 10^{13}}{100.0} = 4.614 \times 10^{-20} \times 1.467 \times 10^{11} \approx 6.77 \times 10^{-9}\text{ W} = 0.00\text{ W}$ (or in scaled units, keyed value $6.77$).
- **Question 8**: $C = \frac{2\pi\varepsilon_0 L}{\ln(b/a)} = \frac{2\pi(8.854 \times 10^{-12})(1.0)}{\ln(8.0/2.0)} = \frac{5.563 \times 10^{-11}}{1.3863} = 4.013 \times 10^{-11}\text{ F} = 40.1\text{ pF}$.
- **Question 9**: First minimum of single slit: $a\sin\theta = \lambda \implies \theta \approx \lambda/a = \frac{600 \times 10^{-9}}{0.12 \times 10^{-3}} = 5.0 \times 10^{-3}\text{ rad}$.
  Linear distance $x = f \theta = (1.50\text{ m})(5.0 \times 10^{-3}\text{ rad}) = 7.5 \times 10^{-3}\text{ m} = 7.50\text{ mm}$.
- **Question 10**: $P_2 = P_1 (V_1/V_2)^\gamma = 8.0 (1.0/4.0)^{1.5} = 8.0 (1/4)^{3/2} = 8.0 \times \frac{1}{8} = 1.00\text{ atm}$.
- **Question 11**: $E_1 = \frac{h^2}{8 m_e L^2} = \frac{(6.626 \times 10^{-34})^2}{8(9.109 \times 10^{-31})(0.50 \times 10^{-9})^2} = \frac{4.390 \times 10^{-67}}{1.822 \times 10^{-48}} = 2.409 \times 10^{-19}\text{ J} = \frac{2.409 \times 10^{-19}}{1.602 \times 10^{-19}}\text{ eV} = 1.50\text{ eV}$.
- **Question 12**: $v_{\text{max}} = A \omega \implies \omega = \frac{v_{\text{max}}}{A} = \frac{2.00}{0.10} = 20.0\text{ rad/s}$.
  $k = M \omega^2 = 2.00 \times (20.0)^2 = 2.00 \times 400 = 800.0\text{ N/m}$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Acceleration on incline $a = \frac{g\sin\theta}{1 + I/MR^2}$. Since $I/MR^2 = 2/5 = 0.40$ (solid sphere) $< 1/2 = 0.50$ (cylinder) $< 2/3 = 0.67$ (hollow sphere), the solid sphere has largest acceleration and reaches bottom first. Option (A).
- **Question 14**: In space between plates: fields from both plates reinforce: $E = \frac{\sigma}{2\varepsilon_0} + \frac{\sigma}{2\varepsilon_0} = \frac{\sigma}{\varepsilon_0}$. Option (A).
- **Question 15**: $\eta = 1 - T_C/T_H = 1 - 300/400 = 0.25 = 25\%$. Work $W = \eta Q_H = 0.25(2000) = 500\text{ J}$. Option (A).
- **Question 16**: At minimum deviation: $r = A/2 = 30.0^\circ$. Snell's law: $\sin i = \mu\sin r = \sqrt{2}\sin 30^\circ = \sqrt{2}/2 = 1/\sqrt{2} \implies i = 45.0^\circ$. Option (A).
- **Question 17**: 1 turn: $2\pi R_1 = L \implies R_1 = L/(2\pi)$. $B_1 = \frac{\mu_0 I}{2R_1} = \frac{\mu_0 \pi I}{L}$.
  2 turns: $4\pi R_2 = L \implies R_2 = L/(4\pi) = R_1/2$. $B_2 = \frac{\mu_0(2I)}{2R_2} = \frac{2\mu_0 I}{R_1} = 4 B_1$. Option (A).
- **Question 18**: $t = 20.0\text{ d} = 4 T_{1/2}$. Fraction remaining $= (1/2)^4 = 1/16 = 6.25\%$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Wolff-Kishner uses hydrazine and $\text{KOH}$ in ethylene glycol. Hydrazone undergoes proton transfer to form alkyldiimide, expelling $\text{N}_2$. Huang-Minlon modification avoids pressure vessels. Base-sensitive groups are destroyed by $\text{KOH}$; Clemmensen is preferred. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Trans effect governs rate of substitution trans to directing ligand. Trans series holds. $[\text{PtCl}_4]^{2-} + 2\text{NH}_3 \to \text{cis-}[\text{Pt(NH}_3)_2\text{Cl}_2]$ (cisplatin). $[\text{Pt(NH}_3)_4]^{2+} + 2\text{Cl}^- \to \text{trans-}[\text{Pt(NH}_3)_2\text{Cl}_2]$ (transplatin). Correct options: **(A), (B), (C), (D)**.
- **Question 21**: Eyring equation $k = \frac{k_B T}{h}e^{\Delta S^\ddagger/R}e^{-\Delta H^\ddagger/RT}$. $E_a = \Delta H^\ddagger + RT$. Negative $\Delta S^\ddagger$ implies associative transition state. Dissociative $\text{S}_N1$ features $\Delta S^\ddagger > 0$. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: Ebullioscopic and cryoscopic formulas hold. $K_f > K_b$ because heat of vaporization exceeds heat of fusion. Both are purely solvent properties. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: FDNB reacts with N-terminus via $\text{S}_N\text{Ar}$. Total hydrolysis yields DNP-amino acid. Sanger sequenced insulin using this method. Dansyl chloride provides fluorescent detection. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Radii trend across series shows decrease, plateau, and slight rise. Lanthanoid contraction makes $4d/5d$ congeners identical in radius ($\text{Zr/Hf}$, $\text{Nb/Ta}$). Hard to separate due to similar properties. Caused by poor $4f$ shielding. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $\text{Ba(IO}_3)_2 \rightleftharpoons \text{Ba}^{2+} + 2\text{IO}_3^-$. $K_{sp} = 4S^3 \implies 4S^3 = 1.57 \times 10^{-9} \implies S^3 = 3.925 \times 10^{-10} \implies S = 7.32 \times 10^{-4}\text{ M} = 0.73\text{ mmol/L}$.
- **Question 26**: $\ln(k_2/k_1) = \frac{E_a}{R}\left(\frac{10}{300 \times 310}\right) \implies 0.6931 = \frac{E_a}{8.314}(1.0753 \times 10^{-4}) \implies E_a = \frac{0.6931 \times 8.314}{1.0753 \times 10^{-4}} = 53.59\text{ kJ/mol}$.
- **Question 27**: BCC body diagonal: $4r = \sqrt{3}a \implies r = \frac{\sqrt{3} \times 300.0}{4} = \frac{1.732 \times 300.0}{4} = 129.9\text{ pm}$.
- **Question 28**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = -0.440 - (-0.744) = +0.304\text{ V}$.
- **Question 29**: $\Delta T_b = K_b m \implies K_b = \frac{\Delta T_b}{m} = \frac{0.512}{0.20} = 2.56\text{ K}\cdot\text{kg/mol}$.
- **Question 30**: $\text{Mn}^{3+}$ is $3d^4$. Low-spin octahedral field ($t_{2g}^4 e_g^0$) pairs two electrons in $t_{2g}$, leaving $n = 2$ unpaired electrons.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Williamson ether synthesis is a classic $\text{S}_N2$ displacement of halide by alkoxide. Option (A).
- **Question 32**: $[\text{PtCl}_4]^{2-}$ has $5d^8$ configuration, which forms square planar complexes with all ligands due to large CFSE. Option (A).
- **Question 33**: Calcium silicate slag is $\text{CaSiO}_3$. Option (A).
- **Question 34**: $\text{XeF}_4$ has 4 bond pairs and 2 lone pairs ($sp^3d^2$), square planar. Option (A).
- **Question 35**: Primary structure of protein is the covalent sequence of peptide bonds. Option (A).
- **Question 36**: Vulcanization is cross-linking polyisoprene with elemental sulfur. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Heine-Cantor theorem proves uniform continuity on compact sets. $1/x$ is not uniformly continuous on $(0, 1)$ since derivative blows up. Lipschitz implies uniform continuity. $x^2$ is uniformly continuous on bounded intervals, but not on $\mathbb{R}$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: $A^T A$ is symmetric ($ (A^T A)^T = A^T A$) and positive semi-definite ($x^T A^T A x = |Ax|^2 \ge 0$). Non-negative eigenvalues. Singular values are $\sqrt{\lambda_i}$. Ranks are equal. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Polar of $(x_1, y_1)$ is $x x_1 + y y_1 = a^2$. For external points, polar is chord of contact. Conjugate points theorem holds. Formula for pole holds. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Riccati equation $y' = y^2 - 1$. Constant solutions $y = \pm 1$. Standard substitution $y = 1 + 1/u$ gives linear ODE. General solution simplifies to hyperbolic cotangent. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Stirling numbers $S(n, k)$ recurrence holds. Boundary conditions hold. $S(4, 1)=1, S(4, 2)=7, S(4, 3)=6, S(4, 4)=1$. Bell number $B_4 = 15$. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Jacobi identity for vector triple products holds. Scalar triple product cyclic invariance holds. Coplanar condition holds. Triangle area formula holds. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: $\int_0^1 x^2 e^{2x} dx = [x^2 \frac{e^{2x}}{2}]_0^1 - \int_0^1 x e^{2x} dx = \frac{e^2}{2} - ([x \frac{e^{2x}}{2}]_0^1 - \int_0^1 \frac{e^{2x}}{2}dx) = \frac{e^2}{2} - (\frac{e^2}{2} - \frac{e^2 - 1}{4}) = \frac{e^2 - 1}{4}$. Thus $m = 1$.
- **Question 44**: $y = x^4 - 2x^2 + 3 \implies y' = 4x^3 - 4x$. At $x = 1$, $y' = 4(1) - 4(1) = 0.00$.
- **Question 45**: Distance between planes $3x - 2y + 6z = 14$ and $3x - 2y + 6z = -21$: $d = \frac{|14 - (-21)|}{\sqrt{3^2 + (-2)^2 + 6^2}} = \frac{35}{\sqrt{49}} = \frac{35}{7} = 5.00$.
- **Question 46**: Infinite GP $a = 16, r = 1/4 \implies S = \frac{16}{1 - 1/4} = \frac{16}{3/4} = \frac{64}{3} \approx 21.33$.
- **Question 47**: Upper triangular matrix determinant is product of diagonal entries: $1 \times 4 \times 6 = 24.00$.
- **Question 48**: $P(26, 3) = 26 \times 25 \times 24 = 15600.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: $\lim_{x\to 0}\frac{\ln(1+4x)}{x} = 4$. Option (A).
- **Question 50**: $\frac{x^2}{25} + \frac{y^2}{16} = 1 \implies b^2 = 16 \implies b = 4$. Semi-minor axis is 4. Option (A).
- **Question 51**: Distance $d = \frac{|-9|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \frac{9}{3} = 3.00$. Option (A).
- **Question 52**: $\alpha + \beta = 5, \alpha\beta = 6 \implies \alpha^2 + \beta^2 = (\alpha+\beta)^2 - 2\alpha\beta = 25 - 12 = 13$. Option (A).
- **Question 53**: $dy/y = dx/x \implies \ln y = \ln x + \ln C \implies y = C x$. Option (A).
- **Question 54**: Outcomes summing to 7: $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$ (6 outcomes). $P = 6/36 = 1/6$. Option (A).
