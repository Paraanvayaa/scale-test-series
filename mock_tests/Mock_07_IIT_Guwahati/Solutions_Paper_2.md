# Detailed Solutions and Pedagogical Analysis — Mock Examination 07 (Paper 2)
### Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)

---

## PART I: PHYSICS

### Q1. Rolling Cylinder on Accelerated Plank
- **Analysis**:
  - Let $a_p$ be plank acceleration and $a_c$ be cylinder linear acceleration.
  - Friction force $f$ on cylinder acts forward, causing linear acceleration $f = M a_c$.
  - Torque on cylinder about CM: $f R = I \alpha = (\frac{1}{2} M R^2)\alpha \implies R\alpha = 2a_c$.
  - No slipping condition at contact: $a_{\text{contact, plank}} = a_p = a_{\text{contact, cylinder}} = a_c + R\alpha = 3a_c$.
  - For plank: $F - f = m a_p = m (3a_c)$.
  - Substitute $f = M a_c$: $F - M a_c = 3m a_c \implies a_c = \frac{F}{3m + M}$. (C is correct).
  - Friction $f = M a_c = \frac{M F}{3m + M}$. (B is correct).
  - Plank acceleration $a_p = 3a_c = \frac{3F}{3m + M} = \frac{F}{m + M/3}$. (A is correct).
  - In pure rolling without slipping, relative velocity at contact point is zero, so no net mechanical energy is dissipated by static friction. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q2. Isothermal vs Adiabatic Expansion
- **Analysis**:
  - $P_{\text{iso}} = P_0 (V_0 / 2V_0) = P_0 / 2$.
  - $P_{\text{adia}} = P_0 (V_0 / 2V_0)^\gamma = P_0 / 2^{5/3} < P_0 / 2$. (A is correct).
  - The isothermal curve lies above the adiabatic curve on a PV diagram, hence enclosing greater area ($W_{\text{iso}} > W_{\text{adia}}$). (B is correct).
  - For ideal gas, $U = n C_v T$. In isothermal, $T = \text{const} \implies \Delta U = 0$. (C is correct).
  - $\Delta S = n R \ln(V_f/V_i) > 0$ for isothermal, and zero for reversible adiabatic. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q3. Oblique Entry of Charge into Magnetic Field
- **Analysis**:
  - Velocity components: $v_x = v_0 \cos\theta$, $v_y = v_0 \sin\theta$.
  - Magnetic force is in xy-plane, causing circular motion of radius $R = \frac{m v_0}{q B_0}$.
  - The trajectory turns through an angle $2(\pi - \theta)$ or $2\theta$?
    Initial angle with x-axis is $\theta$. It curves towards the $-y$ direction and exits when x becomes 0 again.
    The chord connects entry $(0, 0)$ to exit $(0, -y)$. Angle turned by velocity vector is $2(\pi/2 - \theta) = \pi - 2\theta$ or similar depending on sign. The chord length on y-axis is $2 R \sin\theta = \frac{2m v_0 \sin\theta}{q B_0}$. (C is correct).
  - Magnetic force does no work, speed remains $v_0$. (D is correct).
  - It returns to $x < 0$ region. (A is correct).
- **Correct Options**: **(A, C, D)**.

### Q4. Thin Oil Film Interference
- **Analysis**:
  - Refractive index order: $n_{\text{air}} = 1.0 < n_{\text{oil}} = 1.40 > n_{\text{water}} = 1.33$.
  - Reflection at air-oil has $n_1 < n_2$, so phase change is $\pi$.
  - Reflection at oil-water has $n_2 > n_3$, so phase change is $0$.
  - Only ONE reflection has phase shift $\pi$. Thus statement (A) is false!
  - Net phase difference condition for constructive interference is $2 n t = (m + 1/2)\lambda$. (B is incorrect).
  - Energy conservation ensures transmitted light has destructive interference when reflected is constructive. (D is correct).
- **Correct Option**: **(D)**.

### Q5. Physics of Nuclear Fission
- **Analysis**: All four statements A, B, C, D accurately convey fundamental physical principles of thermal neutron-induced fission.
- **Correct Options**: **(A, B, C, D)**.

### Q6. Isolated Capacitor Plate Separation
- **Analysis**:
  - Disconnected battery $\implies Q = \text{constant}$.
  - Capacitance $C = \frac{\varepsilon_0 A}{d} \to C' = \frac{\varepsilon_0 A}{2d} = C/2$.
  - Electric field $E = \frac{\sigma}{\varepsilon_0} = \frac{Q}{A \varepsilon_0}$ is independent of $d$. (A is correct).
  - Potential difference $V' = E(2d) = 2 E d = 2V$. (B is correct).
  - Stored energy $U' = \frac{Q^2}{2 C'} = \frac{Q^2}{C} = 2 U$. (C is correct).
  - Work by external agent $= U' - U = U = \Delta U$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q7–Q12 Numerical Solutions
- **Q7**: Tension at distance $x$ from bottom is $T(x) = \frac{M}{L} x g$.
  Wave speed $v(x) = \sqrt{\frac{T(x)}{\mu}} = \sqrt{g x}$.
  $$t = \int_0^L \frac{dx}{\sqrt{g x}} = 2\sqrt{\frac{L}{g}} = 2\sqrt{\frac{6.0}{10}} = 2\sqrt{0.6} \approx 2(0.775) = 1.55\text{ s}$$
  **Answer: 1.55**.
- **Q8**: $T_H = 327 + 273 = 600\text{ K}$, $T_C = 27 + 273 = 300\text{ K}$.
  $\eta_{\text{Carnot}} = 1 - \frac{300}{600} = 50\%$.
  Actual efficiency $\eta = 0.80 \times 50\% = 40\%$. **Answer: 40**.
- **Q9**: Quality factor $Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{40}\sqrt{\frac{0.1}{100 \times 10^{-6}}} = \frac{1}{40}\sqrt{1000} = \frac{31.62}{40} \approx 0.79$. **Answer: 0.79**.
- **Q10**: $\lambda_0 = \frac{hc}{\Phi} = \frac{1242\text{ eV}\cdot\text{nm}}{2.3\text{ eV}} = 540\text{ nm}$. **Answer: 540**.
- **Q11**: In vacuum, surface energy is conserved during isothermal coalescence:
  $$2(4\pi r_1^2 \times 2T) + 2(4\pi r_2^2 \times 2T) \implies R^2 = r_1^2 + r_2^2 = 2^2 + 4^2 = 20 \implies R = \sqrt{20} \approx 4.47\text{ cm}$$
  **Answer: 4.47**.
- **Q12**: de Broglie wavelength $\lambda = \frac{h}{\sqrt{2 m q V}}$.
  $$\frac{\lambda_p}{\lambda_\alpha} = \sqrt{\frac{m_\alpha q_\alpha}{m_p q_p}} = \sqrt{4 \times 2} = \sqrt{8} \approx 2.83$$
  **Answer: 2.83**.

### Q13–Q18 Integer Solutions
- **Q13**: Conservation of angular momentum: $r_p v_p = r_a v_a \implies \frac{v_p}{v_a} = \frac{r_a}{r_p} = 3$. **Answer: 3**.
- **Q14**: Brewster's angle: $\tan i_B = \mu = \sqrt{3} \implies i_B = 60^\circ$.
  Since $i_B + r = 90^\circ \implies r = 30^\circ$. $30/10 = 3$. **Answer: 3**.
- **Q15**: Number of half-lives $n = 80 / 20 = 4$.
  Fraction remaining $= (1/2)^4 = 1/16 \implies N = 16$. **Answer: 16**.
- **Q16**: Buoyant force $F_B = \rho V g = \rho (\frac{4}{3}\pi r^3) g \propto r^3$.
  If radius is doubled, volume increases by $2^3 = 8$. $k = 8$. **Answer: 8**.
- **Q17**: For any $d$-orbital, azimuthal quantum number $l = 2$, which gives 2 angular nodal surfaces (nodal planes). For $d_{xy}$, nodal planes are $xz$ and $yz$ ($x=0$ and $y=0$). Total nodal planes $= 2$. **Answer: 2**.
- **Q18**: For a long straight wire, $B(r) = \frac{\mu_0 I}{2\pi r} \propto 1/r$.
  At distance $r/4$, field is $4 B_0$. Integer $n = 4$. **Answer: 4**.

---

## PART II: CHEMISTRY

### Q19. Carbon Allotropes
- **Analysis**: All four statements correctly state classical structural and thermodynamic properties of diamond, graphite, and buckminsterfullerene.
- **Correct Options**: **(A, B, C, D)**.

### Q20. Le Chatelier Equilibrium of $\text{SO}_3$
- **Analysis**:
  - Exothermic reaction ($\Delta H < 0$) favored by lower temperature. (A is correct).
  - Decrease in moles of gas ($\Delta n_g = 2 - 3 = -1$) favored by high pressure. (B is correct).
  - Constant volume inert gas does not change partial pressures. (C is correct).
  - Catalyst lowers both forward and reverse activation barriers by equal amounts. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q21. Differentiation of Coordination Isomers by $\text{AgNO}_3$
- **Analysis**:
  - (A) $[\text{Co}(\text{NH}_3)_5\text{SO}_4]\text{Br}$ gives a pale yellow precipitate of $\text{AgBr}$ with $\text{AgNO}_3$, while the sulfate isomer gives no precipitate. (A is correct).
  - (B) $[\text{Pt}(\text{NH}_3)_4\text{Cl}_2]\text{Br}_2$ precipitates $\text{AgBr}$ (pale yellow), while $[\text{Pt}(\text{NH}_3)_4\text{Br}_2]\text{Cl}_2$ precipitates $\text{AgCl}$ (white). (B is correct).
  - (C) Hydrate isomers: $[\text{Cr}(\text{H}_2\text{O})_6]\text{Cl}_3$ precipitates 3 equivalents of $\text{AgCl}$, while the monohydrate precipitates 2 equivalents. (C is correct).
  - (D) Neither contains free halide ion in outer coordination sphere. (D is incorrect).
- **Correct Options**: **(A, B, C)**.

### Q22. Stereochemistry of Diels-Alder Reaction
- **Analysis**: All statements describe established mechanistic tenets of the thermal $[4_s + 2_s]$ Diels-Alder cycloaddition.
- **Correct Options**: **(A, B, C, D)**.

### Q23. Electronic Configurations of Transition Metals
- **Analysis**: All four statements correctly reflect NCERT/standard advanced transition metal behavior.
- **Correct Options**: **(A, B, C, D)**.

### Q24. Langmuir Adsorption Isotherm
- **Analysis**: All four statements accurately summarize Langmuir's monolayer adsorption model.
- **Correct Options**: **(A, B, C, D)**.

### Q25–Q30 Numerical Solutions
- **Q25**: Overall: $\text{Zn} + \text{Cu}^{2+} \rightarrow \text{Zn}^{2+} + \text{Cu}$.
  $$Q = \frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]} = \frac{0.1}{0.01} = 10$$
  $$E_{\text{cell}} = E^\circ - \frac{0.06}{2} \log Q = 1.10 - 0.03 \log(10) = 1.10 - 0.03 = 1.07\text{ V}$$
  **Answer: 1.07**.
- **Q26**: $\Delta H^\circ = \Delta H_f^\circ(\text{CO}_2) - \Delta H_f^\circ(\text{CO}) = -393.5 - (-110.5) = -283.0\text{ kJ}$. **Answer: -283 (or -283.0)**.
- **Q27**: Acetone ($\text{CH}_3\text{COCH}_3$, 3 carbons) + Formaldehyde ($\text{HCHO}$, 1 carbon) $\implies$ 2-methylprop-1-ene (isobutylene, $\text{C}_4\text{H}_8$). Total carbons $= 4$. **Answer: 4**.
- **Q28**: In presence of $0.1\text{ M}\text{ Cl}^-$, $s = \frac{K_{sp}}{[\text{Cl}^-]} = \frac{1.0 \times 10^{-10}}{0.1} = 1.0 \times 10^{-9}\text{ M}$. Value of $A = 1.0$. **Answer: 1.0 (or 1)**.
- **Q29**: $t = \frac{2.303}{k} \log\left(\frac{1.0}{0.1}\right) = \frac{2.303}{2.303 \times 10^{-2}} \times 1 = 100\text{ min}$. **Answer: 100**.
- **Q30**: In $1\text{ L}$ solution: mass of solution $= 1000 \times 1.10 = 1100\text{ g}$.
  Mass of solute $= 3.0 \times 58.5 = 175.5\text{ g}$.
  Mass of solvent $= 1100 - 175.5 = 924.5\text{ g} = 0.9245\text{ kg}$.
  $$\text{Molality } m = \frac{3.0\text{ mol}}{0.9245\text{ kg}} \approx 3.25\text{ m}$$
  **Answer: 3.25**.

### Q31–Q36 Integer Solutions
- **Q31**: A linear peptide of $N$ amino acids contains $N - 1$ peptide bonds. For hexapeptide ($N = 6$), peptide bonds $= 6 - 1 = 5$. **Answer: 5**.
- **Q32**: Green vitriol is ferrous sulfate heptahydrate: $\text{FeSO}_4\cdot 7\text{H}_2\text{O}$. $x = 7$. **Answer: 7**.
- **Q33**: $\text{Mn}^{2+}$ is $d^5$ with 5 unpaired electrons. $\mu = \sqrt{5(5+2)} = \sqrt{35}\text{ BM} \implies N = 35$. **Answer: 35**.
- **Q34**: In rock salt, both $\text{Na}^+$ and $\text{Cl}^-$ have octahedral coordination number of 6. **Answer: 6**.
- **Q35**: In osmium tetroxide ($\text{OsO}_4$), oxidation state of $\text{Os}$ is $+8$. **Answer: 8**.
- **Q36**: Open chain D-glucose has 4 stereocenters ($C_2, C_3, C_4, C_5$). Total stereocenters $= 4$. **Answer: 4**.

---

## PART III: MATHEMATICS

### Q37. Taylor Series Remainder and Inequalities
- **Analysis**:
  - $f'(x) = \cos x - 1 + \frac{x^2}{2} > 0$ for all $x > 0$ since $\cos x > 1 - x^2/2$. (A is correct).
  - Since $f(0) = 0$ and $f'(x) > 0$, $f(x) > 0$ for all $x > 0$. (B and C correct).
  - Taylor series: $\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \dots \implies \lim_{x\to 0} \frac{f(x)}{x^5} = \frac{1}{120}$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q38. Orthogonal Matrix Properties
- **Analysis**: All four statements are standard linear algebra theorems for $O(3)$ and $SO(3)$.
- **Correct Options**: **(A, B, C, D)**.

### Q39. Rectangular Hyperbola Normal
- **Analysis**: Tangent slope at $(c t, c/t)$ is $-1/t^2$. Hence normal slope is $t^2$.
  Equation: $y - c/t = t^2(x - ct) \implies t^3 x - t y - c t^4 + c = 0$.
  Intersection with $x y = c^2$: substituting $x = ct', y = c/t'$ gives $t' = -1/t^3$.
- **Correct Options**: **(A, B, C, D)**.

### Q40. Wallis' Formulas
- **Analysis**: All statements are standard properties and Wallis integral reductions.
- **Correct Options**: **(A, B, C, D)**.

### Q41. Classical Vector Identities
- **Analysis**: Statements A, B, C, D are classical vector algebraic identities.
- **Correct Options**: **(A, B, C, D)**.

### Q42. Probability Independence
- **Analysis**:
  - $P(E_1 \cup E_2) = P(E_1) + P(E_2) - P(E_1 \cap E_2) \implies 0.7 = 0.4 + 0.5 - P(E_1 \cap E_2) \implies P(E_1 \cap E_2) = 0.2$. (A is correct).
  - $P(E_1) P(E_2) = 0.4 \times 0.5 = 0.2 = P(E_1 \cap E_2) \implies$ independent. (B is correct).
  - $P(E_1 | E_2) = P(E_1) = 0.4$. (C is correct).
  - $P(E_1 \cap E_2') = P(E_1) - P(E_1 \cap E_2) = 0.4 - 0.2 = 0.2$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q43–Q48 Numerical Solutions
- **Q43**: Beta function: $I = B(2, 10) = \frac{\Gamma(2)\Gamma(10)}{\Gamma(12)} = \frac{1! \times 9!}{11!} = \frac{1}{11 \times 10} = \frac{1}{110}$. Integer $N = 110$. **Answer: 110**.
- **Q44**: $f(x) = \frac{1}{2}\sin 2x$. Maximum value is $1/2 = 0.5$. **Answer: 0.5**.
- **Q45**: Second plane: $2x - y + 2z = 17/2 = 8.5$.
  Distance $d = \frac{|8.5 - 4|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{4.5}{\sqrt{9}} = \frac{4.5}{3} = 1.5$. **Answer: 1.5**.
- **Q46**: Standard form: $\frac{x^2}{16} + \frac{y^2}{9} = 1 \implies a^2 = 16, b^2 = 9$.
  $$e = \sqrt{1 - b^2/a^2} = \sqrt{1 - 9/16} = \frac{\sqrt{7}}{4} \approx \frac{2.646}{4} \approx 0.66$$
  **Answer: 0.66**.
- **Q47**: Telescoping series: $\sum_{n=1}^\infty \left(\frac{1}{n} - \frac{1}{n+1}\right) = 1$. **Answer: 1**.
- **Q48**: $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x + y \\ x + 2y \end{pmatrix} = \begin{pmatrix} 3x \\ 3y \end{pmatrix} \implies x = y$.
  Given $x^2 + y^2 = 2 \implies 2x^2 = 2 \implies x = 1$ (since $x > 0$). Thus $y = 1$.
  $x + y = 1 + 1 = 2$. **Answer: 2**.

### Q49–Q54 Integer Solutions
- **Q49**: Number of diagonals in an $n$-gon is $\frac{n(n-3)}{2}$. For $n = 10$: $\frac{10 \times 7}{2} = 35$. **Answer: 35**.
- **Q50**: The highest order derivative present is $\frac{d^3 y}{dx^3}$, so the order is 3. **Answer: 3**.
- **Q51**: Standard limit $\lim_{x\to 0} \frac{e^{3x} - 1}{x} = 3$. **Answer: 3**.
- **Q52**: Dividing by $5^x$: $(2/5)^x + (3/5)^x = 1$.
  The LHS is strictly decreasing on $\mathbb{R}$, taking all values in $(0, \infty)$.
  At $x = 1$, $(2/5)^1 + (3/5)^1 = 1$. Hence $x = 1$ is the unique real solution. Number of solutions $= 1$. **Answer: 1**.
- **Q53**: Circle: $(x - 3)^2 + (y - 4)^2 = 9 + 16 = 25$. Radius $= 5$. **Answer: 5**.
- **Q54**: By Vieta's formulas for $x^3 - 6x^2 + 11x - 6 = 0$, sum of roots $= -(-6)/1 = 6$. **Answer: 6**.
