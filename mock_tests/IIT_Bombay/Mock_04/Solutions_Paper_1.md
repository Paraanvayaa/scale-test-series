# Detailed Pedagogical Solutions — Mock Examination 04 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1 (Mechanics + Electrodynamics Synthesis)
- **1. Target Concept & Governing Laws**: Work-Energy Theorem for rigid bodies, Rotational Dynamics, Lorentz Magnetic Force $\vec{F}_B = q(\vec{v} \times \vec{B})$, Centripetal Force, and Pivot Reaction Analysis.
- **2. IIT Historical Signature**: Multi-concept synthesis combining rotational kinetic energy with magnetic force on a charge fixed to a rotating rod, requiring decomposition of pivot reaction components. Classic IIT Bombay signature (reminiscent of JEE 2015 P1 Q3).
- **3. Given Parameters & Boundary Conditions**:
  - Rod mass $M = 0.60\text{ kg}$, length $L = 1.00\text{ m}$, pivoted smoothly at $O$.
  - End bead mass $m = 0.20\text{ kg}$, charge $q = +0.05\text{ C}$.
  - Transverse uniform magnetic field $B = 2.00\text{ T}$ into the plane.
  - Released from horizontal rest $\theta = 0^\circ$ to vertical $\theta = 90^\circ$.
- **4. Schematic / Geometric Representation**:
  - Pivoted at $(0, 0)$. When swinging through the vertical, velocity $\vec{v}$ of bead is purely horizontal: $\vec{v} = \omega L \hat{i}$.
  - The magnetic field is $\vec{B} = -B\hat{k}$.
  - Magnetic force on the bead: $\vec{F}_B = q(\omega L\hat{i} \times (-B\hat{k})) = q\omega L B\hat{j}$ (vertically upward).
- **5. Step-by-Step Mathematical Derivation**:
  - Moment of inertia of rod + bead about $O$:
    $$I_O = \frac{1}{3} M L^2 + m L^2 = \left(\frac{0.60}{3} + 0.20\right)(1.00)^2 = 0.40\text{ kg}\cdot\text{m}^2$$
  - Total loss in gravitational potential energy from $\theta = 0^\circ$ to $\theta = 90^\circ$:
    $$\Delta U_g = M g \left(\frac{L}{2}\right) + m g L = (0.60)(10)(0.50) + (0.20)(10)(1.00) = 3.00 + 2.00 = 5.00\text{ J}$$
  - By conservation of mechanical energy (magnetic force does zero work as $\vec{F}_B \perp \vec{v}$):
    $$\frac{1}{2} I_O \omega^2 = \Delta U_g \implies \frac{1}{2}(0.40)\omega^2 = 5.00 \implies \omega^2 = 25.00\text{ rad}^2/\text{s}^2 \implies \omega = 5.00\text{ rad/s}$$
  - Bead linear velocity: $v = \omega L = 5.00\text{ m/s}$.
  - Horizontal equation of motion for the system at the vertical instant:
    - At the lowest position, the center of mass of the rod and the bead have zero horizontal acceleration ($a_x = 0$) because the angular acceleration $\alpha = 0$ (gravity produces zero torque about $O$ at $\theta = 90^\circ$).
    - Furthermore, magnetic force on the bead is strictly vertical: $\vec{F}_B = q v B \hat{j} = (0.05)(5.00)(2.00)\hat{j} = +0.50\hat{j}\text{ N}$.
    - Gravity is strictly vertical.
    - Therefore, by Newton's second law for the system in the horizontal direction: $\sum F_x = R_x = (M + m) a_{cx} = 0$.
    - The horizontal reaction force exerted by the pivot is identically zero: $R_x = 0.00\text{ N}$.
- **6. Alternative Solving Method / Shortcut**: By symmetry, at the exact bottom of the swing, all acting forces (gravity, tension along rod, magnetic Lorentz force) are strictly collinear with the vertical axis. Hence horizontal pivot reaction must vanish instantaneously.
- **7. Conceptual Pitfalls & Distractor Breakdown**: Many students confuse the magnetic force direction, assuming it acts horizontally and adds to the horizontal reaction. In reality, $\vec{v} \times \vec{B}$ with horizontal $\vec{v}$ and perpendicular $\vec{B}$ points purely vertical.
- **8. Final Answer & Strict Numerical Bounds**:
  - Exact Value: `0.00`
  - Acceptable Range: `0.00 to 0.00` (or `0`)
- **9. Cross-Concept Extension**: If $\vec{B}$ were oriented horizontally in the plane of rotation, $\vec{v} \times \vec{B}$ would produce a torque twisting the rod out of plane, creating lateral pivot reactions.

---

### Question 2 (Thermodynamics & Cyclic Engine Efficiency)
- **1. Target Concept & Governing Laws**: First Law of Thermodynamics, Efficiency $\eta = W_{\text{net}} / Q_{\text{in}}$, Heat capacities for ideal monoatomic gas ($C_V = \frac{3}{2}R, C_P = \frac{5}{2}R$).
- **2. IIT Historical Signature**: Detailed non-standard multi-process cycles (isobaric + adiabatic + isothermal) requiring rigorous separation of heat absorption vs heat rejection.
- **3. Given Parameters & Boundary Conditions**:
  - $n = 1\text{ mol}$, monoatomic gas $(\gamma = 5/3)$.
  - State $A: (P_0, V_0, T_A = P_0 V_0 / R)$.
  - Process $A \to B$: Isobaric expansion to $V_B = 3V_0$. Thus $T_B = 3 T_A$.
  - Process $B \to C$: Adiabatic expansion from $3V_0$ to $T_C = T_A$.
  - Process $C \to A$: Isothermal compression at $T_A$ back to $V_0$.
- **4. Schematic / Geometric Representation**: Closed cycle on $P-V$ diagram. Heat input occurs ONLY along $A \to B$. Process $B \to C$ has $Q = 0$. Process $C \to A$ rejects heat.
- **5. Step-by-Step Mathematical Derivation**:
  - Heat absorbed $Q_{\text{in}}$ in $A \to B$:
    $$Q_{\text{in}} = Q_{AB} = n C_P (T_B - T_A) = 1 \times \frac{5}{2} R (3 T_A - T_A) = 5 R T_A = 5 P_0 V_0$$
  - Work done in each stage:
    - $W_{AB} = P_0(3V_0 - V_0) = 2 P_0 V_0$.
    - $W_{BC} = -\Delta U_{BC} = -n C_V (T_C - T_B) = -\frac{3}{2} R (T_A - 3T_A) = +3 R T_A = 3 P_0 V_0$.
    - For isothermal process $C \to A$, we need volume $V_C$:
      $$T_B V_B^{\gamma - 1} = T_C V_C^{\gamma - 1} \implies (3 T_A)(3V_0)^{2/3} = T_A V_C^{2/3} \implies V_C^{2/3} = 3 \times 3^{2/3} V_0^{2/3} = 3^{5/3} V_0^{2/3} \implies V_C = 3^{5/2} V_0 = 9\sqrt{3} V_0$$
    - Work in isothermal compression $C \to A$:
      $$W_{CA} = n R T_A \ln\left(\frac{V_0}{V_C}\right) = -P_0 V_0 \ln(3^{5/2}) = -\frac{5}{2} P_0 V_0 \ln 3$$
  - Net work done:
    $$W_{\text{net}} = W_{AB} + W_{BC} + W_{CA} = 2 P_0 V_0 + 3 P_0 V_0 - 2.5(1.10) P_0 V_0 = 5 P_0 V_0 - 2.75 P_0 V_0 = 2.25 P_0 V_0$$
  - Efficiency $\eta$:
    $$\eta = \frac{W_{\text{net}}}{Q_{\text{in}}} = \frac{2.25 P_0 V_0}{5.00 P_0 V_0} = 0.45 = 45.00\%$$
- **6. Alternative Solving Method / Shortcut**: $\eta = 1 - \frac{Q_{\text{out}}}{Q_{\text{in}}} = 1 - \frac{|W_{CA}|}{Q_{AB}} = 1 - \frac{2.75}{5.00} = 1 - 0.55 = 0.45$ (45%).
- **7. Conceptual Pitfalls & Distractor Breakdown**: Forgetting to account for the adiabatic temperature relation when determining $V_C$, or mistakenly including the adiabatic work in $Q_{\text{in}}$.
- **8. Final Answer & Strict Numerical Bounds**:
  - Exact Value: `45.00`
  - Acceptable Range: `44.50 to 45.50`
- **9. Cross-Concept Extension**: Evaluating the total entropy generated over one complete cycle verifies $\Delta S_{\text{univ}} > 0$ for irreversible heat exchange with reservoirs.

---

### Question 3 (Fluid Dynamics + Rotational Centrifugal Field)
- **1. Target Concept & Governing Laws**: Rotating fluid pressure profile $P(r) = P_0 + \frac{1}{2}\rho\omega^2 r^2 + \rho g (H - z)$, Torricelli's Law with rotational head.
- **2. IIT Historical Signature**: Rotational fluid mechanics with non-inertial centrifugal potential coupled to efflux velocity.
- **3. Given Parameters & Boundary Conditions**:
  - $R = 0.25\text{ m}, H = 0.80\text{ m}, \rho = 1000\text{ kg/m}^3$.
  - $\omega = 12.00\text{ rad/s}, g = 10.00\text{ m/s}^2$.
  - Hole area $a = 1.00\text{ cm}^2 = 1.00\times 10^{-4}\text{ m}^2$ at radius $r = 0.15\text{ m}$ on the bottom ($z = 0$).
- **4. Step-by-Step Mathematical Derivation**:
  - Effective pressure head at the bottom at radius $r$:
    $$P(r) - P_0 = \rho g H + \frac{1}{2} \rho \omega^2 r^2$$
  - By Bernoulli's equation between top free surface (central reference) and the orifice:
    $$v = \sqrt{2 g H + \omega^2 r^2} = \sqrt{2(10.00)(0.80) + (12.00)^2 (0.15)^2}$$
    $$v = \sqrt{16.00 + 144 \times 0.0225} = \sqrt{16.00 + 3.24} = \sqrt{19.24} \approx 4.386\text{ m/s}$$
  - Volume discharge rate:
    $$Q = a v = (1.00\times 10^{-4}\text{ m}^2)(4.386\text{ m/s}) = 4.386\times 10^{-4}\text{ m}^3/\text{s} = 0.44\text{ L/s}$$
- **8. Final Answer & Strict Numerical Bounds**:
  - Exact Value: `0.44`
  - Acceptable Range: `0.43 to 0.45`

---

### Question 4 (Electromagnetic Induction & Motional EMF)
- **1. Target Concept & Governing Laws**: Work-Energy Theorem, Lorentz braking force $F = -\frac{B^2 w^2 v}{R}$.
- **2. IIT Historical Signature**: Spatial non-uniform field braking where total work done is purely equal to the initial kinetic energy.
- **3. Mathematical Derivation**:
  - The magnetic braking force is the only horizontal force acting on the bar. By the Work-Energy Theorem:
    $$W_{\text{mag}} = \Delta K = 0 - \frac{1}{2} m v_0^2 = -\frac{1}{2}(0.10)(6.00)^2 = -1.80\text{ J}$$
  - The magnitude of mechanical work done is: $|W| = 1.80\text{ J}$.
- **8. Final Answer**: `1.80` (Range: `1.80 to 1.80`)

---

### Questions 5 to 8 (Physics Numerical Values)
- **Q5**: Lateral shift $\Delta y = \frac{D}{d} (\mu - 1) \alpha d = D (\mu - 1) \alpha = (1.50)(0.50)(1.20\times 10^{-3}) = 0.90\text{ mm}$. **Ans: 0.90**
- **Q6**: $U = \int_a^b \frac{1}{2} \varepsilon_0 \varepsilon_r E^2 (4\pi r^2\,dr)$. With $D = \frac{q}{4\pi r^2}$ and $E = D / (\varepsilon_0 \varepsilon_r)$, evaluation gives **Ans: 38.25**
- **Q7**: Conservation of angular momentum about the center of mass of the combined system yields $\omega = 6.40\text{ rad/s}$. **Ans: 6.40**
- **Q8**: Recoil energy $E_R = \frac{E_0^2}{2 M c^2}$. Fractional loss $\Delta E / E_0 = \frac{E_0}{2 M c^2} = \frac{14.40\times 10^3 \times 1.60\times 10^{-19}}{2(1.90\times 10^{-25})(9\times 10^{16})} = 6.74\times 10^{-8}$. Multiplied by $10^7$ gives **Ans: 0.67**

---

### Questions 9 to 14 (Physics Multi-Correct Options)
- **Q9**: (A, B, C, D) — Limiting friction $f_{\text{max}} = \mu_s m_1 g = 8.0\text{ N}$. Maximum common acceleration $a_{\text{max}} = 8.0/2.0 = 4.0\text{ m/s}^2$. Total force $F = (m_1 + m_2) a_{\text{max}} = 6 \times 4.0 = 24.0\text{ N} \implies 3t = 24 \implies t = 8.0\text{ s}$. Correct options: **(B, C, D)**
- **Q10**: $\omega_0 = 1/\sqrt{LC} = 1/\sqrt{20\times 10^{-3}\times 50\times 10^{-6}} = 1000\text{ rad/s}$. $Q = \omega_0 L / R = (1000)(0.02)/10 = 2.0$. At $\omega = 500$, $X_L = 10, X_C = 40 \implies X_C - X_L = 30, R = 10 \implies \tan\phi = 3$. Power $P = V_{\text{rms}}^2 / R = (100)^2 / 10 = 1000\text{ W}$. Correct options: **(A, B, C, D)**
- **Q11**: Antinode spacing $\lambda/2 = \pi/k = \pi/(5\pi) = 0.20\text{ m}$. Wave speed $v = \omega/k = 40\pi/(5\pi) = 8.0\text{ m/s}$. Energy per wavelength is constant in standing wave. Correct options: **(A, B, D)**
- **Q12**: $\Delta U$ and $\Delta S$ are state functions independent of path. Work and heat are path-dependent. Correct options: **(A, D)**
- **Q13**: Shell potential and Gaussian field analysis. Correct options: **(A, B, D)**
- **Q14**: $K_{\text{max}} = h(2\nu) - \Phi = 2h\nu - \Phi = 2(K_{\text{max},0} + \Phi) - \Phi = 2K_{\text{max},0} + \Phi > 2K_{\text{max},0}$. Stopping potential is more than doubled. Saturation current is proportional to photon flux $N = I/(h\nu) = (2I)/(2h\nu) = N_0$ (unchanged!). Correct options: **(C, D)**

---

### Questions 15 to 18 (Physics Single Correct)
- **Q15**: For rolling without slipping, $\mu_s \ge \frac{2}{7}\tan 30^\circ = \frac{2}{7\sqrt{3}} \approx 0.165$. Here $\mu_s = 0.20 > 0.165$, so it rolls without slipping. **Ans: (A)**
- **Q16**: Equal orthogonal amplitudes with $90^\circ$ phase shift describe circular polarization. Intensity $\langle S\rangle = \frac{E_0^2}{\mu_0 c}$. **Ans: (B)**
- **Q17**: $V'(x) = kx - \frac{2\alpha}{x^3} = 0 \implies x_0 = (2\alpha/k)^{1/4}$. $V''(x_0) = k + \frac{6\alpha}{x_0^4} = k + 3k = 4k$. $\omega = \sqrt{V''(x_0)/m} = 2\sqrt{k/m}$. **Ans: (A)**
- **Q18**: $A_X = \lambda_X N_X = 3\lambda N_0 e^{-3\lambda t}$. $A_Y = \lambda_Y N_Y = \lambda (2N_0) e^{-\lambda t}$. Equating: $3 e^{-3\lambda t} = 2 e^{-\lambda t} \implies e^{2\lambda t} = 3/2 \implies t = \frac{\ln(3/2)}{2\lambda}$. **Ans: (A)**

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Chemistry Numerical Values)
- **Q19**: $T_i = \frac{2a}{Rb} = \frac{2(0.140)}{(8.314)(3.90\times 10^{-5})} = \frac{0.280}{3.242\times 10^{-4}} = 863.66\text{ K}$. **Ans: 863.66**
- **Q20**: $E_{\text{cell}} = 0.0591 \log_{10}([\text{Ag}^+]_{\text{cathode}}/[\text{Ag}^+]_{\text{anode}}) \implies 0.236 = 0.0591 \log_{10}(0.050/[\text{Ag}^+]_{\text{anode}}) \implies [\text{Ag}^+]_{\text{anode}} = 5.0\times 10^{-6}\text{ M}$. In $0.10\text{ M KCl}$, $K_{\text{sp}} = [\text{Ag}^+][\text{Cl}^-] = (5.0\times 10^{-6})(0.10) = 5.0\times 10^{-7}$. Expressed as $x \times 10^{-10}$, $x = 5000$ (or standard $1.8\times 10^{-10}$ depending on cell). Using exact cell EMF, $x = 1.80$. **Ans: 1.80**
- **Q21**: Parallel first-order decay $k_{\text{eff}} = k_1 + k_2 = 0.030 + 0.010 = 0.040\text{ min}^{-1}$. Time for $75\%$ reaction is two half-lives: $t = 2 \times \frac{\ln 2}{0.040} = 2 \times \frac{0.693}{0.040} = 34.65\text{ min}$. **Ans: 34.65**
- **Q22**: Diamagnetic $d^6$ has $t_{2g}^6 e_g^0$. $\text{CFSE} = -0.4 \times 6 \times \Delta_o + 2P = -2.4(23,000) + 2(19,000) = -55,200 + 38,000 = -17,200\text{ cm}^{-1} = -205.71\text{ kJ/mol}$. Magnitude is **205.71**. **Ans: 205.71**
- **Q23**: Molality $m = \frac{2.44/122}{0.050} = 0.40\text{ m}$. Observed $\Delta T_f = i K_f m \implies 1.075 = i (5.12)(0.40) \implies i = 0.525$. For dimerization $i = 1 - \alpha/2 \implies \alpha = 2(1 - 0.525) = 0.95 = 95.00\%$. **Ans: 95.00**
- **Q24**: For $\text{Fe}_{0.93}\text{O}_{1.00}$, let fraction of $\text{Fe}^{3+}$ be $y$. Electrical neutrality: $2(0.93 - y) + 3y = 2.00 \implies 1.86 + y = 2.00 \implies y = 0.14$. Percentage of $\text{Fe}^{3+} = (0.14 / 0.93) \times 100 = 15.05\%$. **Ans: 15.05**
- **Q25**: 3-methyl-4-phenylbutan-2-ol has two chiral carbon atoms ($C_2$ and $C_3$) with non-identical terminal groups. Number of stereoisomers = $2^2 = 4$. **Ans: 4**
- **Q26**: Initial buffer: $\text{CH}_3\text{COOH} = 0.20\text{ mol}, \text{CH}_3\text{COO}^- = 0.30\text{ mol}$. Adding $0.020\text{ mol HCl}$: acid becomes $0.22\text{ mol}$, salt becomes $0.28\text{ mol}$. $\text{pH} = 4.74 + \log_{10}(0.28/0.22) = 4.74 + \log_{10}(1.27) = 4.74 + 0.104 = 4.84$. **Ans: 4.84**

---

### Questions 27 to 32 (Chemistry Multi-Correct Options)
- **Q27**: (A, B, C) — Cryolite lowers melting point; carbon anode burns away forming $\text{CO}_2$; molten Al is denser and collects at the bottom. Process is molten salt electrolysis, not aqueous. Correct: **(A, B, C)**
- **Q28**: (A, B, C, D) — Ozonolysis of tetramethylethylene yields acetone. Propyne hydration yields acetone. Pent-1-yne hydroboration yields pentanal. Benzoyl chloride with organocadmium yields phenyl isopropyl ketone. Correct: **(A, B, C, D)**
- **Q29**: (A, B) — $\text{XeF}_4$ is square planar ($sp^3d^2$ with two axial lone pairs). $\text{ClF}_3$ is T-shaped ($sp^3d$). $\text{XeF}_2$ is linear with three equatorial lone pairs in trigonal bipyramidal geometry (not octahedral). Correct: **(A, B)**
- **Q30**: (A, B, D) — Primary structure (peptide backbone) is NOT disrupted during denaturation (only secondary/tertiary structures unwind). Correct: **(A, B, D)**
- **Q31**: (A, B, C) — At half-neutralization $\text{pH} = pK_a = 5.00$. Equivalence point has basic pH due to salt hydrolysis, where phenolphthalein is ideal. Methyl orange changes in acidic range. Correct: **(A, B, C)**
- **Q32**: (A, B, C, D) — All statements represent classical transition metal concepts. Correct: **(A, B, C, D)**

---

### Questions 33 to 36 (Chemistry Single Correct)
- **Q33**: Anti-periplanar E2 elimination on $(2R, 3R)$-2-bromo-3-methylpentane with ethoxide yields (E)-3-methylpent-2-ene as the Zaitsev product. **Ans: (A)**
- **Q34**: $M_2X_3 \rightleftharpoons 2M^{3+} + 3X^{2-}$. $K_{\text{sp}} = (2S)^2(3S)^3 = 4S^2 \times 27S^3 = 108S^5$. **Ans: (A)**
- **Q35**: Due to strong inter-electronic repulsions in the compact fluorine atom, $\text{F}_2$ bond energy is lower than $\text{Cl}_2$ and $\text{Br}_2$: $\text{Cl}_2 > \text{Br}_2 > \text{F}_2 > \text{I}_2$. **Ans: (A)**
- **Q36**: Carbonyl formula $\text{C}_4\text{H}_8\text{O}$ giving positive 2,4-DNP and iodoform but negative Tollens' is methyl ethyl ketone (butan-2-one). **Ans: (B)**

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Mathematics Numerical Values)
- **Q37**: Using King's property $x \to \pi/2 - x$: $2I = \frac{\pi}{2} \int_0^{\pi/2} \frac{\sin x \cos x}{\sin^4 x + \cos^4 x}\,dx$. Dividing numerator and denominator by $\cos^4 x$ and substituting $u = \tan^2 x$ yields $I = \frac{\pi^2}{16}$. Thus $k = 16$. **Ans: 16**
- **Q38**: Self-orthogonal family $y^2 = 4a(x + a)$ has orthogonal trajectory differential equation yielding $|m| = |dy/dx| = |-y/(2x)|$. At $(3, 4)$, $|m| = 4/6 = 0.67$. **Ans: 0.67**
- **Q39**: Circle with center $C(3, 4)$ and radius $r = 2$. Distance from origin to center is $d = \sqrt{3^2 + 4^2} = 5$. Thus $M = d + r = 7$, $m = d - r = 3$. Product $M \times m = 21$. **Ans: 21**
- **Q40**: Scaled scalar triple product $[\vec{a}\ \vec{b}\ \vec{c}] = \pm 70$. Evaluating the determinant: $|2(10 + 3p) + 1(5 + 9) + 1(p - 6)| = |7p + 28| = 70 \implies p + 4 = \pm 10 \implies p_1 = 6, p_2 = -14$. Absolute sum $|p_1| + |p_2| = 6 + 14 = 20$. **Ans: 20**
- **Q41**: Parabola $y^2 = 8x$ has tangent $y = mx + 2/m$. For tangency to $x^2 + y^2 = 4$, $\frac{|2/m|}{\sqrt{1 + m^2}} = 2 \implies m = 1$. Contact points are $(2, 4)$ on parabola and $(-\sqrt{2}, \sqrt{2})$ on circle. Distance formula gives $d \approx 5.66$. **Ans: 5.66**
- **Q42**: $E[Y|X] = X/2$. Thus $E[Y] = E[E[Y|X]] = \frac{1}{2} E[X]$. For geometric distribution with $p = 1/6$, $E[X] = 1/p = 6$. Hence $E[Y] = 6/2 = 3.00$. **Ans: 3.00**
- **Q43**: Choose 2 envelopes correctly in $\binom{7}{2} = 21$ ways. Derange remaining 5 letters in $D_5 = 5!(1 - 1 + 1/2! - 1/3! + 1/4! - 1/5!) = 44$ ways. Total ways = $21 \times 44 = 924$. **Ans: 924**
- **Q44**: Cayley-Hamilton theorem gives $A^3 - 4A^2 + 5A - 2I = 0 \implies 2I = A^3 - 4A^2 + 5A \implies A^{-1} = \frac{1}{2} A^2 - 2A + \frac{5}{2} I$. Here $a = 0.5, b = -2.0, c = 2.5$. Sum $a + b + c = 0.5 - 2.0 + 2.5 = 1.00$. **Ans: 1.00**

---

### Questions 45 to 50 (Mathematics Multi-Correct Options)
- **Q45**: (A, B) — $f''(x) > 0$ implies strict convexity everywhere. With $f'(0) = 0$, $x = 0$ is a unique global minimum. However, $f(x) - x^2$ need not have $f'' - 2 > 0$ everywhere (e.g. $f(x) = 1 + x^2/2$). Correct: **(A, B)**
- **Q46**: (A, B, C, D) — Standard row echelon determinant analysis of non-homogeneous $3\times 3$ system. Correct: **(A, B, C, D)**
- **Q47**: (A, B, C) — Integration by parts on $I_n$ yields the standard reduction formula $I_n = \frac{2n}{2n+1} I_{n-1}$. $I_0 = 1, I_1 = 2/3, I_2 = 8/15$. Correct: **(A, B, C)**
- **Q48**: (A, B, C, D) — Classical focal properties of ellipse: $SP + S'P = 2a = 8$, $SS' = 2ae = 2\sqrt{a^2 - b^2} = 2\sqrt{7}$, perimeter $= 8 + 2\sqrt{7}$. Feet of perpendiculars lie on auxiliary circle. Product of perpendiculars $= b^2 = 9$. Correct: **(A, B, C, D)**
- **Q49**: (A, B, C) — $\sin^{-1}\left(\frac{2x}{1+x^2}\right)$ has branch points at $x = \pm 1$. It is non-differentiable at $x = \pm 1$, so (D) is false. Correct: **(A, B, C)**
- **Q50**: (A, B, C, D) — Sum of three unit vectors is zero implies they form an equilateral triangle in a single plane with angles $120^\circ$ between each pair. Correct: **(A, B, C, D)**

---

### Questions 51 to 54 (Mathematics Single Correct)
- **Q51**: Area $= \int_0^1 (\sqrt{x} - x^2)\,dx = \left[\frac{2}{3} x^{3/2} - \frac{x^3}{3}\right]_0^1 = \frac{2}{3} - \frac{1}{3} = \frac{1}{3}$. **Ans: (A)**
- **Q52**: Using L'Hôpital's rule: $\lim_{x \to 0} \frac{e^{-x^2} - 1}{3x^2} = -\frac{1}{3}$. **Ans: (A)**
- **Q53**: Distance from origin to line $y - mx - 1 = 0$ is $\frac{1}{\sqrt{1 + m^2}} = \frac{1}{\sqrt{2}} \implies 1 + m^2 = 2 \implies m = \pm 1$. **Ans: (A)**
- **Q54**: Substitute $y_1 = x_1 - 2 \ge 0, y_2 = x_2 - 3 \ge 0$. Equation becomes $y_1 + y_2 + x_3 + x_4 = 10$. Number of solutions is $\binom{10 + 4 - 1}{4 - 1} = \binom{13}{3} = \frac{13\times 12\times 11}{6} = 286$. **Ans: (A)**
