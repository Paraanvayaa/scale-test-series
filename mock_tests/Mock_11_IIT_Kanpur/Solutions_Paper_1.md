# Detailed Solutions and Pedagogical Analysis — Mock Examination 11 (Paper 1)
### Organising Institute Style: IIT Kanpur (`IIT_KANPUR_STYLE`)

---

## PART I: PHYSICS

### Q1. Anharmonic Small Oscillations
- **First Observation & Concept**: Frequency of small oscillations $\omega = \sqrt{\frac{k_{\text{eff}}}{m}}$ where $k_{\text{eff}} = V''(0)$.
- **Derivation**:
  $$V'(x) = V_0 \left(\frac{2x}{a^2} - \frac{2x^3}{a^4}\right) = 0 \implies x = 0$$
  $$V''(x) = V_0 \left(\frac{2}{a^2} - \frac{6x^2}{a^4}\right)$$
  $$V''(0) = \frac{2V_0}{a^2} > 0 \implies k_{\text{eff}} = \frac{2V_0}{a^2}$$
  $$\omega = \sqrt{\frac{k_{\text{eff}}}{m}} = \sqrt{\frac{2V_0}{m a^2}}$$
- **Correct Option**: **(A)**.

### Q2. Potential Inside Shell with Point Charge
- **First Observation & Concept**: Electrostatic potential inside conducting material ($a < r < b$).
- **Key Insight**: A conductor in electrostatic equilibrium is an equipotential volume. The potential everywhere inside the conductor ($a \le r \le b$) equals the potential at the outer surface $r = b$.
- **Derivation**: Outer surface carries net charge $q + Q$. By Gauss's law for $r > b$, potential is:
  $$V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q + Q}{r} \implies V(b) = \frac{1}{4\pi\varepsilon_0}\frac{q + Q}{b}$$
  Since $a < r < b$ is within the conductor: $V(r) = V(b) = \frac{1}{4\pi\varepsilon_0}\frac{Q + q}{b}$.
- **Correct Option**: **(A)**.

### Q3. Polytropic Gas Molar Heat Capacity
- **First Observation & Concept**: $P = \alpha V \implies P V^{-1} = \text{const} \implies n = -1$.
- **Derivation**:
  $$C = C_v + \frac{R}{1 - n} = C_v + \frac{R}{1 - (-1)} = C_v + \frac{R}{2}$$
- **Correct Option**: **(A)**.

### Q4. Coaxial Cable Inductance
- **First Observation & Concept**: Energy in magnetic field: $U_B = \int \frac{B^2}{2\mu_0}\,dV = \frac{1}{2} L' I^2$.
- **Key Insight**: In the region $a < r < b$, Ampère's law gives $B(r) = \frac{\mu_0 I}{2\pi r}$.
- **Derivation**: Per unit length:
  $$U_B = \int_a^b \frac{1}{2\mu_0}\left(\frac{\mu_0 I}{2\pi r}\right)^2 (2\pi r\,dr) = \frac{\mu_0 I^2}{4\pi}\int_a^b \frac{dr}{r} = \frac{\mu_0 I^2}{4\pi}\ln(b/a)$$
  Equating to $\frac{1}{2} L' I^2$: $L' = \frac{\mu_0}{2\pi}\ln(b/a)$.
- **Correct Option**: **(A)**.

### Q5. Compensating Glass Plates in YDSE
- **First Observation & Concept**: Condition for zero shift of central fringe: $(\mu_1 - 1)t_1 = (\mu_2 - 1)t_2$.
- **Derivation**:
  $$(1.6 - 1)t_1 = (1.4 - 1)t_2 \implies 0.6 t_1 = 0.4 t_2 \implies \frac{t_1}{t_2} = \frac{0.4}{0.6} = \frac{2}{3}$$
- **Correct Option**: **(A)**.

### Q6. Nuclear Mass and Binding Energy
- **First Observation & Concept**: Binding energy definition: $E_{\text{total}} = [Z m_p + (A - Z)m_n - M_{\text{nuc}}]c^2 = A E_b$.
- **Derivation**: $M_{\text{nuc}} = Z m_p + (A - Z)m_n - \frac{A E_b}{c^2}$.
- **Correct Option**: **(A)**.

### Q7. Rod on Supports Sudden Release
- **Analysis**:
  - Immediately after release, torque about $A$: $\tau_A = M g (L/2) = I_A \alpha = (\frac{1}{3} M L^2)\alpha \implies \alpha = \frac{3g}{2L}$. (A is correct).
  - Downward acceleration of CM: $a_{cm} = \alpha(L/2) = \frac{3g}{4}$. (C is correct).
  - Equation for vertical motion: $M g - N_A = M a_{cm} = M (3g/4) \implies N_A = M g / 4$. (B is correct, D is incorrect).
- **Correct Options**: **(A, B, C)**.

### Q8. Rotating Half-Filled Liquid Cylinder
- **Analysis**: All four statements correctly state classical fluid dynamics of rotational pressure distributions.
- **Correct Options**: **(A, B, C, D)**.

### Q9. Decaying Magnetic Field in Loop
- **Analysis**:
  - Induced EMF $\mathcal{E} = -\frac{d\Phi}{dt} = \pi r^2 B_0 \alpha e^{-\alpha t}$.
  - $E(2\pi r) = \mathcal{E} \implies E = \frac{1}{2} r B_0 \alpha e^{-\alpha t}$. (A is correct).
  - Current $I = \mathcal{E}/R$. Total charge $q = \int_0^\infty I\,dt = \frac{\Delta\Phi}{R} = \frac{\pi r^2 B_0}{R}$. (B is correct).
  - Power $P = I^2 R = \frac{\pi^2 r^4 B_0^2 \alpha^2}{R} e^{-2\alpha t}$, maximum at $t = 0$. (C is correct).
  - Total energy $H = \int_0^\infty P\,dt = \frac{\pi^2 r^4 B_0^2 \alpha^2}{R} \frac{1}{2\alpha} = \frac{\pi^2 r^4 B_0^2 \alpha}{2R}$. (D states $4R$, so incorrect).
- **Correct Options**: **(A, B, C)**.

### Q10. Polytropic Thermodynamic Relations
- **Analysis**: All four statements correctly state polytropic gas thermodynamics.
- **Correct Options**: **(A, B, C, D)**.

### Q11. Davisson-Germer Experiment
- **Analysis**: All four statements correctly state facts and historical significance of the Davisson-Germer experiment.
- **Correct Options**: **(A, B, C, D)**.

### Q12. Astronomical Telescope Normal Adjustment
- **Analysis**: All four statements are standard geometric optics principles for refracting telescopes.
- **Correct Options**: **(A, B, C, D)**.

### Q13–Q18 Numerical Solutions
- **Q13**: Total kinetic energy of rolling disc: $K = \frac{1}{2} M v^2 + \frac{1}{2} I \omega^2 = \frac{3}{4} M v^2 = \frac{3}{4}(2.0)(6.0)^2 = 1.5 \times 36 = 54\text{ J}$. **Answer: 54**.
- **Q14**: In charging RC circuit, $q(t) = Q_0(1 - e^{-t/RC})$. At $t = \tau = RC$, $q = Q_0(1 - 1/e) = 0.632 Q_0$.
  $$t = R C = (20 \times 10^3 \,\Omega)(50 \times 10^{-6}\text{ F}) = 1.0\text{ s}$$
  **Answer: 1.0 (or 1)**.
- **Q15**: $h = \frac{2 T \cos\theta}{\rho g r} = \frac{2(0.075)(1)}{(1000)(10)(0.5 \times 10^{-3})} = \frac{0.15}{5.0} = 0.03\text{ m} = 3.0\text{ cm}$. **Answer: 3.0 (or 3)**.
- **Q16**: $\omega = 2\pi f = 20\pi\text{ rad/s}$.
  $F_{\max} = m \omega^2 A = (0.1)(400\pi^2)(0.05) = 2\pi^2 \approx 2(9.87) \approx 19.7\text{ N}$. **Answer: 19.7**.
- **Q17**: Kinetic energy $K = \frac{3}{2} k_B T$. Momentum $p = \sqrt{2 m_n K} = \sqrt{3 m_n k_B T}$.
  $$p = \sqrt{3(1.67 \times 10^{-27})(1.38 \times 10^{-23})(300)} = \sqrt{2.074 \times 10^{-47}} \approx 4.55 \times 10^{-24}\text{ kg}\cdot\text{m/s}$$
  $$\lambda = \frac{h}{p} = \frac{6.63 \times 10^{-34}}{4.55 \times 10^{-24}} \approx 1.46 \times 10^{-10}\text{ m} = 0.15\text{ nm}$$
  **Answer: 0.15**.
- **Q18**: $M = N I A = N I (\pi r^2) = 100 \times 0.5 \times \pi (0.10)^2 = 50 \times 0.01 \pi = 0.50\pi \approx 1.57\text{ A}\cdot\text{m}^2$. **Answer: 1.57**.

---

## PART II: CHEMISTRY

### Q19. Solubility of Sparingly Soluble Salt
- **Calculation**: $\text{Ag}_2\text{CrO}_4 \rightleftharpoons 2\text{Ag}^+ + \text{CrO}_4^{2-} \implies K_{sp} = (2s)^2(s) = 4s^3$.
  $$4s^3 = 1.1 \times 10^{-12} \implies s^3 = 2.75 \times 10^{-13} = 275 \times 10^{-15}$$
  $$s = (275)^{1/3} \times 10^{-5} \approx 6.5 \times 10^{-5}\text{ M}$$
- **Correct Option**: **(A)**.

### Q20. Second Order Kinetics Plot
- **Analysis**: Integrated rate law for $2A \rightarrow \text{Products}$: $-\frac{d[A]}{dt} = 2k [A]^2 \implies \frac{1}{[A]} = \frac{1}{[A]_0} + 2kt$.
  Slope is $2k$ (or $k$ depending on rate definition; if $-\frac{1}{2}\frac{d[A]}{dt} = k[A]^2$, slope is $2k$).
- **Correct Option**: **(A)**.

### Q21. Copper Ferrocyanide Color
- **Reaction**: $2\text{Cu}^{2+} + [\text{Fe}(\text{CN})_6]^{4-} \rightarrow \text{Cu}_2[\text{Fe}(\text{CN})_6] \downarrow$ (chocolate brown precipitate).
- **Correct Option**: **(B)**.

### Q22. Hydroboration-Oxidation Regiochemistry
- **Reaction**: 2-methylbut-2-ene ($\text{(CH}_3)_2\text{C=CH-CH}_3$) adds $\text{BH}_3$ with anti-Markovnikov regiochemistry, attaching boron to the less substituted carbon (C3) and subsequent oxidation yields 3-methylbutan-2-ol.
- **Correct Option**: **(B)**.

### Q23. Crystal Field Theory of Nickel(II) Complexes
- **Analysis**:
  - $[\text{NiCl}_4]^{2-}$: $\text{Ni}^{2+}$ ($d^8$) with weak field $\text{Cl}^- \implies sp^3$ tetrahedral (2 unpaired electrons).
  - $[\text{Ni}(\text{CN})_4]^{2-}$: $\text{Ni}^{2+}$ with strong field $\text{CN}^- \implies dsp^2$ square planar (diamagnetic).
- **Correct Option**: **(A)**.

### Q24. Photographic Fixing Reaction
- **Reaction**: $\text{AgBr} + 2\text{Na}_2\text{S}_2\text{O}_3 \rightarrow \text{Na}_3[\text{Ag}(\text{S}_2\text{O}_3)_2] + \text{NaBr}$.
- **Correct Option**: **(A)**.

### Q25. Daniell Cell Thermodynamics
- **Analysis**: All four statements correctly state electrochemical cell thermodynamics.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Negative Deviation from Raoult's Law
- **Analysis**: All four statements correctly describe negative deviation solutions.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Redox Reactions of $\text{KMnO}_4$
- **Analysis**: All four statements correctly summarize $\text{KMnO}_4$ redox behavior.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Kolbe-Schmitt Reaction Mechanism
- **Analysis**: All four statements correctly state Kolbe reaction principles.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Basic Buffer Capacity
- **Analysis**: All four statements correctly state Henderson-Hasselbalch buffer principles.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Alkene Elimination Selectivity
- **Analysis**: All four statements are standard E1/E2 elimination principles.
- **Correct Options**: **(A, B, C, D)**.

### Q31–Q36 Numerical Solutions
- **Q31**: $\text{Mg(OH)}_2 \rightleftharpoons \text{Mg}^{2+} + 2\text{OH}^- \implies K_{sp} = 4s^3 = 1.2 \times 10^{-11}$.
  $$s^3 = 3.0 \times 10^{-12} \implies s \approx 1.442 \times 10^{-4}\text{ M}$$
  $$[\text{OH}^-] = 2s = 2.884 \times 10^{-4}\text{ M} \implies pOH = 4 - \log(2.884) = 4 - 0.46 = 3.54$$
  $$\text{pH} = 14.0 - 3.54 = 10.46$$
  **Answer: 10.46**.
- **Q32**: Volume of 1 unit cell $V = a^3 = (400 \times 10^{-10}\text{ cm})^3 = 64 \times 10^{-24}\text{ cm}^3$.
  Number of unit cells in $1\text{ cm}^3$:
  $$N = \frac{1.0}{64 \times 10^{-24}} = 1.5625 \times 10^{22} \implies A = 1.56$$
  **Answer: 1.56**.
- **Q33**: $t_{1/2} = \frac{0.693}{k} = \frac{0.693}{4.62 \times 10^{-3}} = 150\text{ s}$. **Answer: 150**.
- **Q34**: Formula mass of $\text{CH}_2 = 14$. $n = 70 / 14 = 5 \implies \text{C}_5\text{H}_{10}$. Hydrogen atoms $= 10$. **Answer: 10**.
- **Q35**: $\Delta G_1^\circ = -3 F (-0.036) = +0.108 F$.
  $\Delta G_2^\circ = -2 F (-0.440) = +0.880 F$.
  $$\Delta G_3^\circ = \Delta G_1^\circ - \Delta G_2^\circ = 0.108 F - 0.880 F = -0.772 F = -1 F E^\circ \implies E^\circ = +0.772\text{ V}$$
  **Answer: 0.772**.
- **Q36**: Square planar $[Mabcd]$ has 3 geometrical isomers. **Answer: 3**.

---

## PART III: MATHEMATICS

### Q37. Definite Integral Symmetry
- **Calculation**: $I = \int_0^\pi \frac{\pi - x}{1 + \sin x}\,dx$.
  $$2I = \pi \int_0^\pi \frac{dx}{1 + \sin x} = \pi \int_0^\pi \frac{1 - \sin x}{\cos^2 x}\,dx = \pi [\tan x - \sec x]_0^\pi = \pi [(0 - (-1)) - (0 - 1)] = 2\pi \implies I = \pi$$
- **Correct Option**: **(A)**.

### Q38. Equation of Normal
- **Calculation**: $y' = 3x^2 - 2$. At $(1, 0)$, $y' = 3(1) - 2 = 1$.
  Normal slope $m_N = -1$.
  Normal equation: $y - 0 = -1(x - 1) \implies x + y - 1 = 0$.
- **Correct Option**: **(A)**.

### Q39. Intersecting Lines in 3D
- **Calculation**: Both lines pass through the common point $(2, 4, 6)$ or check determinant:
  $$\begin{vmatrix} 2 - 1 & 3 - 2 & 4 - 3 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{vmatrix} = \begin{vmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{vmatrix} = 0$$
  The lines intersect! Shortest distance $= 0$.
- **Correct Option**: **(C)**.

### Q40. Probability Without Replacement
- **Calculation**: $P(\text{both white}) = \frac{3}{5} \times \frac{2}{4} = \frac{6}{20} = \frac{3}{10}$.
- **Correct Option**: **(A)**.

### Q41. Parabola and Line Area
- **Calculation**: $x = y^2 / 2$. Line: $x = y + 4$.
  Intersection: $y^2 / 2 = y + 4 \implies y^2 - 2y - 8 = 0 \implies (y - 4)(y + 2) = 0$.
  $$\text{Area} = \int_{-2}^4 \left(y + 4 - \frac{y^2}{2}\right)\,dy = \left[\frac{y^2}{2} + 4y - \frac{y^3}{6}\right]_{-2}^4 = (8 + 16 - 32/3) - (2 - 8 + 8/6) = \frac{40}{3} - \left(-\frac{14}{3}\right) = \frac{54}{3} = 18$$
- **Correct Option**: **(A)**.

### Q42. Integrating Factor
- **Calculation**: $\text{IF} = e^{\int (2/x)dx} = e^{2\ln x} = x^2$.
- **Correct Option**: **(A)**.

### Q43. Fourth Degree Function Analysis
- **Analysis**: $f(x) = (x^2 - 1)^2 + 2$. Since $(x^2 - 1)^2 \ge 0$, minimum value is $2$ at $x = \pm 1$.
  $f'(x) = 4x(x^2 - 1) = 0 \implies x = 0, \pm 1$. Local max at $x = 0$ ($f = 3$).
- **Correct Options**: **(A, B, C, D)**.

### Q44. Tangent and Intercepts of Circle
- **Analysis**: Center $(2, 3)$, radius $r = \sqrt{4 + 9 - 9} = 2$.
  Distance from center to x-axis is $3 \ne 2$, so it does not touch x-axis.
  Distance from center to y-axis is $2 = r$, so it touches the y-axis! (A, B, D correct).
- **Correct Options**: **(A, B, D)**.

### Q45. Matrix Zero Products
- **Analysis**: All four statements correctly state linear algebra properties of matrix multiplication.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Orthogonal Complex Numbers
- **Analysis**: $|z_1 + z_2| = |z_1 - z_2| \iff$ the diagonals of the parallelogram are equal $\iff$ the parallelogram is a rectangle $\iff z_1 \perp z_2$.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Stationary Inflection Point
- **Analysis**: $f(x) = (x - 1)^3$. $f'(x) = 3(x - 1)^2 \ge 0$, strictly increasing, with inflection point and triple root at $x = 1$.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Triangle of Three Vectors
- **Analysis**: $\vec{c} = -(\vec{a} + \vec{b})$.
  $|\vec{c}|^2 = |\vec{a}|^2 + |\vec{b}|^2 + 2\vec{a}\cdot\vec{b} \implies 49 = 9 + 25 + 2\vec{a}\cdot\vec{b} \implies 2\vec{a}\cdot\vec{b} = 15 \implies \vec{a}\cdot\vec{b} = 15/2$.
  $\cos\theta = \frac{15/2}{3 \times 5} = \frac{1}{2} \implies \theta = 60^\circ$.
- **Correct Options**: **(A, B)**.

### Q49–Q54 Numerical Solutions
- **Q49**: Taylor series: $\tan x = x + x^3/3$, $\sin x = x - x^3/6$.
  $$\tan x - \sin x = \frac{x^3}{3} - \left(-\frac{x^3}{6}\right) = \frac{x^3}{2} \implies L = 0.5$$
  **Answer: 0.5**.
- **Q50**: Let $g(x) = x^4 - 4x + 3$.
  $g'(x) = 4x^3 - 4 = 0 \implies x = 1$.
  $g(1) = 1 - 4 + 3 = 0$.
  Since $g'(1) = 0$ and $g(1) = 0$, $x = 1$ is a double root.
  Since $g''(x) = 12x^2 > 0$, the function is strictly convex, so $x = 1$ is the unique global minimum.
  Factoring: $(x - 1)^2 (x^2 + 2x + 3) = 0$.
  $x^2 + 2x + 3$ has no real roots (discriminant $4 - 12 < 0$).
  Total distinct real roots $= 2$ (only $x = 1$, wait, only $1$ distinct real root!).
  Distinct real roots: only $x = 1$. Number of distinct real roots $= 1$. **Answer: 1**.
- **Q51**: Parabola $y^2 = 4x$. At $(1, 2)$:
  $2y y' = 4 \implies y' = 2/y = 2/2 = 1$.
  Normal slope $m_N = -1$. **Answer: -1**.
- **Q52**: $\int_0^{\pi/2} \sin^2 x\,dx = \frac{\pi}{4} \approx 0.785 \approx 0.79$. **Answer: 0.79**.
- **Q53**: Distance $d = \frac{|6 - (-3)|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \frac{9}{\sqrt{9}} = 3$. **Answer: 3**.
- **Q54**: Expansion along first column: $2(4 - 1) - 1(2 - 0) = 2(3) - 2 = 6 - 2 = 4$. **Answer: 4**.
