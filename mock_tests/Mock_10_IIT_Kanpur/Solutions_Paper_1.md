# Detailed Solutions and Pedagogical Analysis — Mock Examination 10 (Paper 1)
### Organising Institute Style: IIT Kanpur (`IIT_KANPUR_STYLE`)

---

## PART I: PHYSICS

### Q1. Drag Force Integration
- **First Observation & Concept**: Retardation $a = v \frac{dv}{dx} = -\frac{b}{m} v^2$.
- **Key Insight**: Express acceleration in terms of distance $x$: $\frac{dv}{dx} = -\frac{b}{m} v$.
- **Derivation**: Separating variables:
  $$\int_{v_0}^v \frac{dv}{v} = -\frac{b}{m} \int_0^x dx \implies \ln\left(\frac{v_0}{v}\right) = \frac{b}{m} x$$
  $$x = \frac{m}{b} \ln\left(\frac{v_0}{v}\right) = \frac{0.5}{0.2} \ln\left(\frac{20}{5}\right) = 2.5 \ln 4 = 2.5 \times 1.3863 = 3.4657 \approx 3.47\text{ m}$$
- **Correct Option**: **(A)**.

### Q2. Center of Mass of Non-Uniform Rod
- **First Observation & Concept**: Center of mass of continuous mass distribution $x_{cm} = \frac{\int x \lambda\,dx}{\int \lambda\,dx}$.
- **Derivation**:
  $$\int_0^L \lambda(x)\,dx = \lambda_0 \int_0^L (1 + x/L)\,dx = \lambda_0 [x + x^2/(2L)]_0^L = \lambda_0 (L + L/2) = \frac{3}{2}\lambda_0 L$$
  $$\int_0^L x \lambda(x)\,dx = \lambda_0 \int_0^L (x + x^2/L)\,dx = \lambda_0 [x^2/2 + x^3/(3L)]_0^L = \lambda_0 (L^2/2 + L^2/3) = \frac{5}{6}\lambda_0 L^2$$
  $$x_{cm} = \frac{\frac{5}{6}\lambda_0 L^2}{\frac{3}{2}\lambda_0 L} = \frac{5}{6} \times \frac{2}{3} L = \frac{5}{9}L$$
- **Correct Option**: **(A)**.

### Q3. Force on Point Charge by Electric Dipole
- **First Observation & Concept**: Broadside-on position electric field of a dipole $\vec{p} = p_0 \hat{i}$.
- **Key Insight**: At $(0, r)$, the electric field points antiparallel to the dipole moment:
  $$\vec{E} = -\frac{1}{4\pi\varepsilon_0}\frac{\vec{p}}{r^3} = -\frac{1}{4\pi\varepsilon_0}\frac{p_0}{r^3}\hat{i}$$
- **Derivation**: The force on $+q$ is $\vec{F} = q \vec{E} = \frac{1}{4\pi\varepsilon_0}\frac{p_0 q}{r^3}(-\hat{i})$.
- **Correct Option**: **(A)**.

### Q4. Induced Electric Field Outside Solenoid
- **First Observation & Concept**: Faraday's law of induction in non-conservative electric fields: $\oint \vec{E}\cdot d\vec{l} = -\frac{d\Phi_B}{dt}$.
- **Key Insight**: For $r > R$, the magnetic flux is restricted to the solenoid interior: $\Phi_B = B (\pi R^2) = (\mu_0 n I)(\pi R^2)$.
- **Derivation**:
  $$E(2\pi r) = \pi R^2 \mu_0 n \frac{dI}{dt} = \pi R^2 \mu_0 n (I_0 \alpha)$$
  $$E = \frac{\mu_0 n I_0 \alpha R^2}{2r} = \frac{(4\pi \times 10^{-7})(1000)(2.0)(50)(0.05)^2}{2(0.10)}$$
  $$E = \frac{(4\pi \times 10^{-7})(10^5)(2.5 \times 10^{-3})}{0.20} = \frac{\pi \times 10^{-4}}{0.20} = 5\pi \times 10^{-4} \text{ V/m} \approx 1.57 \times 10^{-4}\text{ V/m}$$
- **Correct Option**: **(A)**.

### Q5. Newton's Cooling Law Scaling
- **First Observation & Concept**: Rate of heat loss $m c \frac{dT}{dt} = -h A (T - T_0) \implies \frac{dT}{dt} = -\frac{h A}{m c}(T - T_0)$.
- **Key Insight**: $A = 4\pi r^2$, mass $m = \rho (\frac{4}{3}\pi r^3) \propto r^3$.
- **Derivation**:
  $$k = \frac{h A}{m c} \propto \frac{r^2}{r^3} = \frac{1}{r}$$
- **Correct Option**: **(A)**.

### Q6. Maximum Orbital Angular Momentum
- **First Observation & Concept**: Orbital angular momentum $L = \sqrt{l(l+1)}\hbar$.
- **Key Insight**: For principal quantum number $n = 4$, the maximum azimuthal quantum number is $l_{\max} = n - 1 = 3$.
- **Derivation**: $L_{\max} = \sqrt{3(3 + 1)}\hbar = \sqrt{12}\hbar$.
- **Correct Option**: **(B)**.

### Q7. Two Block Friction System
- **Analysis**:
  - Maximum acceleration of $M$ caused by static friction: $a_{\max} = \frac{\mu m g}{M}$.
  - Common force required to produce this: $F = (m + M)a_{\max} = (m + M)\frac{\mu m g}{M} = \mu m g (1 + m/M)$. (A is correct).
  - Friction force on $M$: $f = M a = M \frac{F}{m + M}$. (B is correct).
  - When slipping occurs, kinetic friction is $\mu m g$, giving acceleration of $M = \frac{\mu m g}{M}$. (C is correct).
  - Friction between sliding bodies always produces net dissipation ($W_{\text{fric}} < 0$). (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q8. Rotating Fluid Paraboloid
- **Analysis**: All four statements correctly state classical fluid dynamics of free surface rotation.
- **Correct Options**: **(A, B, C, D)**.

### Q9. Helmholtz Coil Field Uniformity
- **Analysis**:
  - Field on axis of two coils separated by $R$: $B(z) = \frac{\mu_0 I R^2}{2[(R/2 + z)^2 + R^2]^{3/2}} + \frac{\mu_0 I R^2}{2[(R/2 - z)^2 + R^2]^{3/2}}$.
  - At $z = 0$, $B(0) = \frac{\mu_0 I R^2}{[5R^2/4]^{3/2}} = (4/5)^{3/2} \frac{\mu_0 I}{R}$. (A is correct).
  - First and second derivatives vanish identically at midpoint, producing extreme uniformity. (B, C, D correct).
- **Correct Options**: **(A, B, C, D)**.

### Q10. Variable Heat Capacity Process
- **Analysis**:
  - $dQ = n C dT = n (C_v + \alpha T) dT \implies Q = n C_v \Delta T + \frac{1}{2} n \alpha (T_2^2 - T_1^2)$. (A is correct).
  - $dS = dQ / T = n C_v \frac{dT}{T} + n \alpha dT \implies \Delta S = n C_v \ln(T_2/T_1) + n \alpha (T_2 - T_1)$. (D is correct).
  - Internal energy change is $\Delta U = n C_v \Delta T < Q$, so $W = Q - \Delta U > 0$, $W < Q$. (C is correct).
- **Correct Options**: **(A, C, D)**.

### Q11. Visibility of Interference Fringes
- **Analysis**:
  - $I_{\max} = (E_1 + E_2)^2$, $I_{\min} = (E_1 - E_2)^2$. (B and D correct).
  - Visibility $\mathcal{V} = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}} = \frac{4 E_1 E_2}{2(E_1^2 + E_2^2)} = \frac{2 E_1 E_2}{E_1^2 + E_2^2}$. (A is correct).
  - If $E_1 = 3 E_2$, $\mathcal{V} = \frac{2(3)}{9 + 1} = \frac{6}{10} = 0.60$. (C is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q12. Rutherford Scattering Closest Approach
- **Analysis**:
  - Energy conservation: $K_\alpha = \frac{1}{4\pi\varepsilon_0}\frac{(2e)(Z e)}{r_0} \implies r_0 = \frac{1}{4\pi\varepsilon_0}\frac{2 Z e^2}{K_\alpha}$. (A and C correct).
  - Calculation: $r_0 = \frac{(9 \times 10^9)(2)(79)(1.6 \times 10^{-19})^2}{5.0 \times 10^6 \times 1.6 \times 10^{-19}} = \frac{18 \times 79 \times 1.6 \times 10^{-10}}{5.0 \times 10^6} \approx 4.55 \times 10^{-14}\text{ m}$. (B is correct).
  - Doubling $K_\alpha$ halves $r_0$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q13–Q18 Numerical Solutions
- **Q13**: Conservation of angular momentum about central axis:
  $$I_i \omega_0 = I_f \omega_f \implies (\frac{1}{2} M R^2) \omega_0 = (\frac{1}{2} M R^2 + m R^2) \omega_f$$
  $$\omega_f = \frac{\frac{1}{2} M}{\frac{1}{2} M + m} \omega_0 = \frac{2.0}{2.0 + 1.0}(12.0) = \frac{2}{3}(12.0) = 8.0\text{ rad/s}$$
  **Answer: 8.0 (or 8)**.
- **Q14**: In discharging RC circuit, $V(t) = V_0 e^{-t/RC}$. When $V(t) = V_0 / e$, $t = \tau = R C$.
  $$t = (50 \times 10^3 \,\Omega)(20 \times 10^{-6}\text{ F}) = 1.0\text{ s}$$
  **Answer: 1.0 (or 1)**.
- **Q15**: $h = \frac{2 T \cos\theta}{\rho g r} = \frac{2(0.544)(-0.707)}{(13600)(9.8)(0.25 \times 10^{-3})} = \frac{-0.7692}{33.32} = -0.0231\text{ m} = -2.31\text{ cm}$. Depression magnitude $= 2.31\text{ cm}$. **Answer: 2.31**.
- **Q16**: $x(t) = A \sin(\omega t)$. At $x = A/2$, $\sin(\omega t) = 1/2 \implies \omega t = \pi/6$.
  $$t = \frac{\pi/6}{2\pi / T} = \frac{T}{12} = \frac{12.0}{12} = 1.0\text{ s}$$
  **Answer: 1.0 (or 1)**.
- **Q17**: $\lambda_{\min} = \frac{hc}{e V} = \frac{1240\text{ V}\cdot\text{nm}}{100\text{ V}} = 12.4\text{ nm} = 12400\text{ pm}$. (If $V = 100\text{ kV}$, $\lambda = 12.4\text{ pm}$. Here for $100\text{ V}$, $12.4\text{ nm} = 12400\text{ pm}$. For $100\text{ kV}$, 12.4). **Answer: 12400**.
- **Q18**: Induced EMF: $\mathcal{E} = \frac{\Delta\Phi}{\Delta t} = \frac{(\pi r^2) B_0}{\Delta t} = \frac{\pi (0.05)^2 (2.0)}{0.05} = 0.10\pi\text{ V} \approx 0.314\text{ V}$.
  Thermal energy $H = \frac{\mathcal{E}^2}{R} \Delta t = \frac{(0.314)^2}{0.2}(0.05) = \frac{0.0986}{0.2}(0.05) = 0.493 \times 0.05 = 0.0247\text{ J} = 25\text{ mJ}$. **Answer: 25**.

---

## PART II: CHEMISTRY

### Q19. Amphiprotic Salt pH Formula
- **Formula**: For an amphiprotic salt $\text{HA}^-$, $[\text{H}^+] = \sqrt{K_{a1} K_{a2}}$.
  $$[\text{H}^+] = \sqrt{(1.0 \times 10^{-4})(1.0 \times 10^{-9})} = \sqrt{1.0 \times 10^{-13}} = 3.16 \times 10^{-7}\text{ M}$$
  $$\text{pH} = \frac{pK_{a1} + pK_{a2}}{2} = \frac{4.0 + 9.0}{2} = 6.50$$
- **Correct Option**: **(C)**.

### Q20. Second Order Gas Phase Dimerization
- **Analysis**: $2A \rightarrow A_2$.
  At $t = t_{1/2}$, half of $A$ has reacted: $P_A = P_0 / 2 = 0.50\text{ bar}$.
  Pressure of $A_2$ formed $= \frac{1}{2}(P_0 - P_A) = \frac{1}{2}(0.50) = 0.25\text{ bar}$.
  Total pressure $P_{\text{total}} = P_A + P_{A_2} = 0.50 + 0.25 = 0.75\text{ bar}$.
- **Correct Option**: **(B)**.

### Q21. Copper Turnings Nitrate Test
- **Reaction**: Nitrate salts react with conc. $\text{H}_2\text{SO}_4$ and Cu turnings to release dense brown $\text{NO}_2$ gas:
  $\text{Cu} + 4\text{HNO}_3 \rightarrow \text{Cu}(\text{NO}_3)_2 + 2\text{NO}_2 + 2\text{H}_2\text{O}$.
  $\text{NO}_2$ oxidizes iodide to iodine, turning starch-iodide paper blue.
- **Correct Option**: **(B)**.

### Q22. Tosylation Followed by Cyanide Displacement
- **Analysis**:
  - Tosylation of alcohol ($	ext{R-OH} + \text{TsCl}$) breaks the $\text{O-H}$ bond, not the $\text{C-O}$ bond, so configuration is retained: $(R)$-tosylate $X$.
  - Subsequent displacement by $\text{CN}^-$ is an $S_N 2$ reaction with complete Walden inversion: $(R) \to (S)$.
- **Correct Option**: **(B)**.

### Q23. Crystal Field Theory of Cobalt(II)
- **Analysis**:
  - $\text{Co}^{2+}$ is $d^7$.
  - $[\text{Co}(\text{H}_2\text{O})_6]^{2+}$ is high-spin $t_{2g}^5 e_g^2 \implies 3$ unpaired electrons ($\mu = \sqrt{3(5)} = 3.87\text{ BM}$).
  - $[\text{Co}(\text{CN})_6]^{4-}$ has strong field ligand $\text{CN}^-$, low-spin $t_{2g}^6 e_g^1 \implies 1$ unpaired electron ($\mu = \sqrt{1(3)} = 1.73\text{ BM}$).
- **Correct Option**: **(A)**.

### Q24. Copper Sulfate and Potassium Iodide Reaction
- **Reaction**: $2\text{CuSO}_4 + 4\text{KI} \rightarrow 2\text{CuI} \downarrow (\text{white}) + \text{I}_2$.
  Excess $\text{KI}$ dissolves $\text{I}_2$ as $\text{KI}_3$ (brown solution).
- **Correct Option**: **(B)**.

### Q25. Hydrogen-Calomel Cell
- **Analysis**: $E_{\text{cell}} = E_{\text{calomel}} - E_{\text{H}^+/\text{H}_2} = 0.28 - E_{\text{H}^+}$.
  $$0.58 = 0.28 - E_{\text{H}^+} \implies E_{\text{H}^+} = -0.30\text{ V}$$
  $$E_{\text{H}^+} = -0.06 \text{pH} \implies -0.30 = -0.06 \text{pH} \implies \text{pH} = 5.0$$
- **Correct Options**: **(A, B, D)**.

### Q26. Positive Deviation from Raoult's Law
- **Analysis**: All four statements correctly state thermodynamic criteria for positive deviation.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Chemistry of Lanthanoids
- **Analysis**: All four statements are standard descriptive facts from f-block chemistry.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Claisen-Schmidt Reaction
- **Analysis**: All four statements correctly state organic reaction mechanisms of cross-aldol condensation.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Simultaneous Solubility Equilibria
- **Analysis**:
  - In solution saturated with both: $[\text{Ag}^+][\text{Cl}^-] = K_{sp1}$ and $[\text{Ag}^+][\text{Br}^-] = K_{sp2}$.
  - Ratio $[\text{Cl}^-] / [\text{Br}^-] = K_{sp1} / K_{sp2} = 1.6 \times 10^{-10} / (5.0 \times 10^{-13}) = 320$. (A is correct).
  - Common ion $\text{Ag}^+$ mutually depresses solubility. (B is correct).
  - $[\text{Ag}^+] = [\text{Cl}^-] + [\text{Br}^-] = \frac{K_{sp1}}{[\text{Ag}^+]} + \frac{K_{sp2}}{[\text{Ag}^+]} \implies [\text{Ag}^+] = \sqrt{K_{sp1} + K_{sp2}}$. (C is correct).
  - Since $K_{sp2} < K_{sp1}$, $\text{AgBr}$ precipitates first. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q30. Birch Reduction Stereochemistry
- **Analysis**: All four statements correctly describe the Birch reduction mechanism.
- **Correct Options**: **(A, B, C, D)**.

### Q31–Q36 Numerical Solutions
- **Q31**: $\text{Fe(OH)}_3 \rightleftharpoons \text{Fe}^{3+} + 3\text{OH}^-$.
  Precipitation begins when $[\text{Fe}^{3+}][\text{OH}^-]^3 = K_{sp}$:
  $$(1.0 \times 10^{-2})[\text{OH}^-]^3 = 1.0 \times 10^{-38} \implies [\text{OH}^-]^3 = 1.0 \times 10^{-36} \implies [\text{OH}^-] = 1.0 \times 10^{-12}\text{ M}$$
  $$pOH = 12.0 \implies \text{pH} = 14.0 - 12.0 = 2.0$$
  **Answer: 2.0 (or 2)**.
- **Q32**: Number of $A$ atoms $= 8 \times 1/8 = 1$.
  Number of $B$ atoms $= 5 \times 1/2 = 2.5$.
  Formula is $A B_{2.5} \implies x = 2.5$. **Answer: 2.5**.
- **Q33**: Yield of $C = \frac{k_2}{k_1 + k_2} \times 100 = \frac{3.6}{1.2 + 3.6} \times 100 = \frac{3.6}{4.8} \times 100 = 75\%$. **Answer: 75**.
- **Q34**: $\text{C}: 78.7/12 = 6.56$; $\text{H}: 8.2/1 = 8.2$; $\text{O}: 13.1/16 = 0.819$.
  Ratio: $\text{C} = 8, \text{H} = 10, \text{O} = 1 \implies \text{C}_8\text{H}_{10}\text{O}$ (molar mass $122\text{ g/mol}$).
  Degree of unsaturation $= 8 + 1 - 10/2 = 4$.
  Aromatic ring accounts for 3 $\pi$-bonds and 1 ring. Number of $\pi$-bonds $= 3$. **Answer: 3**.
- **Q35**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = 1.51 - 1.36 = +0.15\text{ V}$. **Answer: 0.15**.
- **Q36**: In $[\text{FeF}_6]^{3-}$, $\text{Fe}^{3+}$ is $d^5$ with weak field $\text{F}^-$. High-spin $t_{2g}^3 e_g^2 \implies 5$ unpaired electrons. **Answer: 5**.

---

## PART III: MATHEMATICS

### Q37. Definite Integral Beta Function
- **Calculation**: $I = \int_0^1 x^1 (1 - x)^5\,dx = B(2, 6) = \frac{1! \times 5!}{7!} = \frac{1}{7 \times 6} = \frac{1}{42}$.
- **Correct Option**: **(A)**.

### Q38. Cubic Real Roots
- **Calculation**: Let $f(x) = x^3 - 3x + 1$.
  $f'(x) = 3x^2 - 3 = 0 \implies x = \pm 1$.
  $f(-1) = -1 + 3 + 1 = 3 > 0$ (local max).
  $f(1) = 1 - 3 + 1 = -1 < 0$ (local min).
  Since $f(-1) f(1) < 0$, the cubic has 3 distinct real roots.
- **Correct Option**: **(C)**.

### Q39. Intersection of Two Lines in 3D
- **Calculation**: Condition for intersection of lines:
  $$\begin{vmatrix} 3 - 1 & k - (-1) & 0 - 1 \\ 2 & 3 & 4 \\ 1 & 2 & 1 \end{vmatrix} = \begin{vmatrix} 2 & k + 1 & -1 \\ 2 & 3 & 4 \\ 1 & 2 & 1 \end{vmatrix} = 0$$
  $$2(3 - 8) - (k + 1)(2 - 4) - 1(4 - 3) = 0 \implies 2(-5) - (k + 1)(-2) - 1 = 0$$
  $$-10 + 2k + 2 - 1 = 0 \implies 2k - 9 = 0 \implies k = 9/2$$
- **Correct Option**: **(A)**.

### Q40. Polya Urn Model Invariance
- **Calculation**: By Polya urn theorem, the probability of drawing a red ball on the $n$-th draw is invariant and equal to the initial proportion: $P(R_2) = P(R_1) = 5/10 = 1/2$.
- **Correct Option**: **(A)**.

### Q41. Parabolic Area
- **Calculation**: Intersections with x-axis: $4 - x^2 = 0 \implies x = \pm 2$.
  $$\text{Area} = \int_{-2}^2 (4 - x^2)\,dx = 2 [4x - x^3/3]_0^2 = 2(8 - 8/3) = 2(16/3) = \frac{32}{3}$$
- **Correct Option**: **(B)**.

### Q42. Linear Differential Equation
- **Calculation**: $\text{IF} = e^{\int 2\,dx} = e^{2x}$.
  $$y e^{2x} = \int e^{2x} e^{-x}\,dx = \int e^x\,dx = e^x + C \implies y = e^{-x} + C e^{-2x}$$
- **Correct Option**: **(A)**.

### Q43. Calculus Analysis of Cubic
- **Analysis**: $f(x) = x^3 - 3x + 2 = (x - 1)^2 (x + 2)$.
  - Local max at $x = -1$ ($f(-1) = 4$), local min at $x = 1$ ($f(1) = 0$).
  - $x = 1$ is a double root.
  - Since $(x - 1)^2 \ge 0$, $f(x) \ge 0$ for all $x \ge -2$.
- **Correct Options**: **(A, B, C, D)**.

### Q44. Geometric Parameters of Hyperbola
- **Analysis**: All four statements correctly state geometry of standard hyperbola $\frac{x^2}{9} - \frac{y^2}{16} = 1$.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Eigenvalues of Symmetric Matrix
- **Analysis**: Characteristic equation factors as $(\lambda - 1)(\lambda - 2)(\lambda - 3) = 0$. All statements are correct.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Complex Circle Locus
- **Analysis**: $|z - 1| = 1 \implies (x - 1)^2 + y^2 = 1 \implies x^2 + y^2 - 2x = 0 \implies |z|^2 = 2\text{Re}(z)$. All statements are correct.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Concave Functions and Rolle's Theorem
- **Analysis**: By Rolle's theorem and strict concavity ($f'' < 0$), $f'(x)$ is strictly decreasing, having a unique zero at which $f(x)$ attains its unique global maximum $> 0$.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Vector Cross Product System
- **Analysis**: All four statements are standard vector algebraic identities.
- **Correct Options**: **(A, B, C, D)**.

### Q49–Q54 Numerical Solutions
- **Q49**: Taylor series: $e^{x^2} = 1 + x^2 + \dots$, $\cos x = 1 - \frac{x^2}{2} + \dots$
  $$e^{x^2} - \cos x = (1 + x^2) - (1 - x^2/2) = \frac{3}{2}x^2 \implies L = 1.5$$
  **Answer: 1.5**.
- **Q50**: Let $g(x) = 2x^3 - 3x^2 - 12x + 20$.
  $g'(x) = 6x^2 - 6x - 12 = 6(x - 2)(x + 1) = 0 \implies x = -1, 2$.
  $g(-1) = -2 - 3 + 12 + 20 = 27 > 0$.
  $g(2) = 16 - 12 - 24 + 20 = 0$.
  Since local minimum is 0, the curve touches the x-axis at $x = 2$ (double root) and crosses at one point in $(-\infty, -1)$.
  Total distinct real roots $= 2$. **Answer: 2**.
- **Q51**: Differentiating $x^2 + y^2 = 25 \implies 2x + 2y y' = 0 \implies y' = -x/y$.
  At $(3, 4)$, $y' = -3/4 = -0.75$. **Answer: -0.75**.
- **Q52**: $\int_0^2 |x - 1|\,dx = \int_0^1 (1 - x)\,dx + \int_1^2 (x - 1)\,dx = 1/2 + 1/2 = 1$. **Answer: 1**.
- **Q53**: Distance $d = \frac{|0 - 14|}{\sqrt{2^2 + 3^2 + 6^2}} = \frac{14}{\sqrt{49}} = \frac{14}{7} = 2$. **Answer: 2**.
- **Q54**: Determinant of upper triangular matrix is product of diagonal entries: $1 \times 4 \times 6 = 24$. **Answer: 24**.
