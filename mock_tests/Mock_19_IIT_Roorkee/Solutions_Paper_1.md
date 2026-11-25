# Detailed Solutions and Pedagogical Analysis — Mock Examination 19 (Paper 1)
### Organising Institute Style: IIT Roorkee (`IIT_ROORKEE_STYLE` — 2019 Benchmark)

---

## PART I: PHYSICS

### Q1. Fluid Filled Spherical Shell on Incline
- **First Observation & Concept**: Rotational dynamics with inviscid fluid vs rigid body.
- **Derivation**:
  - Case 1: Inviscid fluid does not acquire angular acceleration (it translates without rotating).
    Only the shell rotates: $I_{\text{rot}} = \frac{2}{3} M R^2$.
    Total translating mass: $M_{\text{tot}} = M + M = 2M$.
    Torque about contact point: $(2M) g R \sin\theta = I_{\text{contact}} \alpha$.
    $I_{\text{contact}} = I_{\text{shell, cm}} + M R^2 + M R^2 = \frac{2}{3} M R^2 + 2 M R^2 = \frac{8}{3} M R^2$.
    $\alpha = \frac{2 M g R \sin\theta}{\frac{8}{3} M R^2} = \frac{3}{4} \frac{g \sin\theta}{R} \implies a = \frac{3}{4} g \sin\theta$.
  - Case 2: Fluid frozen to solid: sphere is a solid sphere of mass $2M$, $I = \frac{2}{5} (2M) R^2 = \frac{4}{5} M R^2$.
    $a = \frac{g \sin\theta}{1 + I/(M_{\text{tot}} R^2)} = \frac{g \sin\theta}{1 + 2/5} = \frac{5}{7} g \sin\theta$.
- **Correct Option**: **(C)** (or **D**). Both (C) and (D) match the physical derivation. Option (C) matches inviscid case.
- **Correct Option**: **(C)**.

### Q2. Sphere Placed on Moving Belt
- **First Observation & Concept**: Slipping to rolling on moving belt: $v_{\text{rel}} = v - \omega R - v_0$.
- **Derivation**:
  - Kinetic friction $f_k = \mu_k M g$ accelerates sphere forward and creates counter-clockwise angular acceleration:
    $a = \mu_k g$, $\alpha = \frac{\mu_k M g R}{2/5 M R^2} = \frac{5 \mu_k g}{2R}$.
  - At time $t$: $v(t) = \mu_k g t$, $\omega(t) = \frac{5 \mu_k g}{2R} t$.
  - Pure rolling on belt moving at speed $v_0$: contact point moves with belt velocity $v_0$:
    $v(t) + \omega(t) R = v_0 \implies \mu_k g t + \frac{5}{2} \mu_k g t = v_0 \implies \frac{7}{2} \mu_k g t = v_0 \implies t = \frac{2 v_0}{7 \mu_k g}$.
  - Velocity of CM: $v = \mu_k g \left(\frac{2 v_0}{7 \mu_k g}\right) = \frac{2}{7} v_0$.
- **Correct Option**: **(A)**.

### Q3. Eccentricity of Keplerian Orbit
- **First Observation & Concept**: Orbit equation for inverse square central force: $e = \sqrt{1 + \frac{2 E L^2}{m k^2}}$.
- **Correct Option**: **(A)**.

### Q4. Force of Liquid Jet on Wall
- **First Observation & Concept**: Momentum conservation / impulse of fluid stream.
- **Derivation**:
  - Mass flow rate $\frac{dm}{dt} = \rho A v$.
  - Change in perpendicular velocity: $\Delta v = v - 0 = v$.
  - Force $F = \frac{dm}{dt} v = (\rho A v) v = \rho A v^2$.
- **Correct Option**: **(A)**.

### Q5. Critical Velocity for Vertical Loop
- **First Observation & Concept**: Top point requires $T \ge 0 \implies v_{\text{top}}^2 \ge g L$.
- **Derivation**:
  - Conservation of energy: $\frac{1}{2} m v_0^2 = \frac{1}{2} m v_{\text{top}}^2 + m g (2L) = \frac{1}{2} m g L + 2 m g L = \frac{5}{2} m g L$.
  - $v_0 = \sqrt{5gL}$.
- **Correct Option**: **(A)**.

### Q6. Floating Cylinder Oscillations
- **First Observation & Concept**: Restoring buoyant force $F = -(\rho A x) g$.
- **Derivation**:
  - $m \ddot{x} + \rho A g x = 0 \implies \omega = \sqrt{\frac{\rho A g}{m}} \implies T = 2\pi \sqrt{\frac{m}{\rho A g}}$.
- **Correct Option**: **(A)**.

### Q7. Force Applied to Cylinder at Height h
- **Analysis**:
  - $F + f = M a$, $\tau = F h - f R = I \alpha = \left(\frac{1}{2} M R^2\right) \frac{a}{R} = \frac{1}{2} M R a$.
  - For $f = 0$: $F = M a$ and $F h = \frac{1}{2} M R a = \frac{1}{2} R F \implies h = R/2$. (A is True)
  - For $h > R/2$: $f > 0$ (forward). (B is True)
  - For $h < R/2$: $f < 0$ (backward). (C is True)
  - At $h = R$: both $F$ and forward $f$ act in same direction, giving maximum acceleration. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q8. Sliding Beads on Rotating Rod
- **Analysis**:
  - No external torque $\implies$ angular momentum $L$ is conserved. (A is True)
  - Moment of inertia increases as beads slide outward $\implies \omega(t)$ decreases. (B is True)
  - $I_i = \frac{1}{12} M L^2$, $I_f = \frac{1}{12} M L^2 + 2 m (L/2)^2 = \frac{1}{12} M L^2 + \frac{1}{2} m L^2 = \frac{L^2}{12}(M + 6m)$.
    $L_i = L_f \implies \frac{1}{12} M L^2 \omega_0 = \frac{1}{12}(M + 6m) L^2 \omega_f \implies \omega_f = \frac{M}{M + 6m} \omega_0$. (C is True)
  - As beads slide outward without friction, Coriolis force does work transferring rotational KE to bead radial KE; total mechanical energy is conserved. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q9. Siphon Operation
- **Analysis**: Torricelli efflux speed, sub-atmospheric pressure at bend, vapor pressure cavitation limit.
- **Correct Options**: **(A, B, C)**.

### Q10. Linear Restoring Central Force
- **Analysis**:
  - $\frac{m v^2}{R} = k R \implies v = R\sqrt{k/m}$. (A is True)
  - $T = \frac{2\pi R}{v} = 2\pi \sqrt{m/k}$ (independent of $R$). (B is True)
  - $K = \frac{1}{2} m v^2 = \frac{1}{2} k R^2$, $U = \frac{1}{2} k R^2$. (C is True)
  - Total energy $E = K + U = k R^2$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q11. Speed of Sound Properties
- **Analysis**: Laplace formula, independence of pressure, humidity effect (density of moist air is lower $\implies$ higher speed), harmonic spectrum of open pipe.
- **Correct Options**: **(A, B, C, D)**.

### Q12. Block on Accelerated Wedge
- **Analysis**: Normal force components, pseudo-force cancellation at $a = g\tan\theta$, impending sliding limits.
- **Correct Options**: **(A, B, C, D)**.

### Q13. Kinetic Energy of Rolling Sphere
- **Derivation**:
  - $E_k = \frac{7}{10} M v^2 = \frac{7}{10} \times 7.0 \times 10.0^2 = \frac{7}{10} \times 7.0 \times 100 = 490\text{ J}$.
- **Answer**: **490**.

### Q14. Rocket Equation
- **Derivation**:
  - $v = u \ln(M_0 / M_f) = 2000 \ln(5000 / 1000) = 2000 \ln 5 = 2000 \times 1.609 = 3218\text{ m/s} = 3.22\text{ km/s}$.
- **Answer**: **3.22**.

### Q15. Period of Physical Pendulum
- **Derivation**:
  - $I = \frac{1}{3} M L^2$, $d = L/2$.
  - $T = 2\pi \sqrt{\frac{I}{M g d}} = 2\pi \sqrt{\frac{\frac{1}{3} M L^2}{M g (L/2)}} = 2\pi \sqrt{\frac{2L}{3g}} = 2\pi \sqrt{\frac{2(1.0)}{3(9.8)}} = 2\pi \sqrt{\frac{2}{29.4}} = 2\pi \sqrt{0.0680} = 2\pi \times 0.2608 \approx 1.64\text{ s}$.
- **Answer**: **1.64**.

### Q16. Venturi Pressure Difference
- **Derivation**:
  - $v_2 = v_1 (A_1 / A_2) = 2.0 \times 2 = 4.0\text{ m/s}$.
  - $\Delta P = \frac{1}{2} \rho (v_2^2 - v_1^2) = \frac{1}{2} (1000) (16.0 - 4.0) = 500 \times 12.0 = 6000\text{ Pa} = 6.0\text{ kPa}$.
- **Answer**: **6.0** (or **6**).

### Q17. Static Spring Extension
- **Derivation**:
  $$\Delta x = \frac{M g}{k} = \frac{2.0 \times 10.0}{200} = \frac{20}{200} = 0.10\text{ m} = 10.0\text{ cm}$$
- **Answer**: **10** (or **10.0**).

### Q18. Atwood Machine Acceleration
- **Derivation**:
  $$a = \frac{m_2 - m_1}{m_1 + m_2} g = \frac{3.0 - 2.0}{2.0 + 3.0} \times 10.0 = \frac{1}{5} \times 10.0 = 2.0\text{ m/s}^2$$
- **Answer**: **2.0** (or **2**).

---

## PART II: CHEMISTRY

### Q19. Optically Active Alkyl Halide
- **Analysis**:
  - Propanal and ethanal ozonolysis products require pent-2-ene.
  - 2-Bromopentane ($\text{CH}_3-\text{CH(Br)}-\text{CH}_2-\text{CH}_2-\text{CH}_3$) has a chiral carbon at C2. Elimination gives pent-2-ene (achiral alkene).
- **Correct Option**: **(A)**.

### Q20. Incorrect Complex Statement
- **Analysis**:
  - In $[\text{Co}(\text{NH}_3)_6]^{3+}$, $\text{Co}^{3+}$ has $3d^6$ configuration. Ammonia is strong-field for $\text{Co}^{3+}$, pairing all electrons in $t_{2g}^6$ (diamagnetic, not paramagnetic!).
- **Correct Option**: **(A)**.

### Q21. Non-Reducing Sugar
- **Analysis**: Sucrose is a non-reducing disaccharide with no free hemiacetal group; gives negative Benedict's and Tollens' tests.
- **Correct Option**: **(A)**.

### Q22. Roasting of Copper Pyrites
- **Analysis**: $2\text{CuFeS}_2 + \text{O}_2 \rightarrow \text{Cu}_2\text{S} + 2\text{FeS} + \text{SO}_2$; $\text{FeS}$ is oxidized to $\text{FeO}$.
- **Correct Option**: **(A)**.

### Q23. Inert Gas Addition at Constant Volume
- **Analysis**: Adding inert gas at constant volume does not change the partial pressures of reactants and products, so equilibrium is undisturbed.
- **Correct Option**: **(A)**.

### Q24. Acidified Permanganate with Iodide
- **Analysis**: In acidic medium, $\text{MnO}_4^-$ oxidizes $\text{I}^-$ to elemental iodine ($\text{I}_2$).
- **Correct Option**: **(A)**.

### Q25. Reimer-Tiemann Reaction
- **Analysis**: Dichlorocarbene electrophile, salicylaldehyde major product, $\text{CCl}_4$ yields salicylic acid.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Lanthanoid Contraction
- **Analysis**: Poor $4f$ shielding, steady size decrease, $\text{Zr}-\text{Hf}$ pair similarity, decreasing basicity of hydroxides.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Lead Storage Battery
- **Analysis**: Anode/cathode reactions, formation of $\text{PbSO}_4$, consumption of $\text{H}_2\text{SO}_4$, reversibility upon charging.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Protein Denaturation
- **Analysis**: Disruption of $2^\circ/3^\circ$ structure while preserving $1^\circ$ covalent sequence, irreversibility, loss of biological activity.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Group II Cations
- **Analysis**: $\text{H}_2\text{S}$ with $\text{HCl}$, common ion suppression, low $K_{sp}$ requirement, subdivision into IIA and IIB.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Van der Waals Equation
- **Analysis**: Physical meaning of $a$ and $b$, critical constants $T_c = \frac{8a}{27Rb}$, $Z_c = 3/8 = 0.375$.
- **Correct Options**: **(A, B, C, D)**.

### Q31. pH of Strong Base
- **Derivation**:
  - $[\text{OH}^-] = 2 \times 0.050 = 0.10\text{ M} = 10^{-1}\text{ M}$.
  - $\text{pOH} = 1.0 \implies \text{pH} = 14.0 - 1.0 = 13.0$.
- **Answer**: **13** (or **13.0**).

### Q32. Arrhenius Activation Energy
- **Derivation**:
  $$\ln 4 = \frac{E_a}{R}\left(\frac{20}{293 \times 313}\right) \implies 1.386 = \frac{E_a}{8.314} \times \frac{20}{91709} \implies E_a = \frac{1.386 \times 8.314 \times 91709}{20} \approx 52838\text{ J/mol} = 52.8\text{ kJ/mol}$$
- **Answer**: **52.8**.

### Q33. Molar Mass of BCC Metal
- **Derivation**:
  - $V = a^3 = (2.88 \times 10^{-8})^3 = 2.389 \times 10^{-23}\text{ cm}^3$.
  - In BCC, $Z = 2$.
  - $\rho = \frac{Z M}{N_A V} \implies 7.2 = \frac{2 M}{6.02 \times 10^{23} \times 2.389 \times 10^{-23}} = \frac{2M}{14.38} \implies M = \frac{7.2 \times 14.38}{2} = 51.8\text{ g/mol}$.
- **Answer**: **51.8**.

### Q34. Octahedral Void Coordination Number
- **Derivation**: An octahedral void is surrounded by 6 spheres $\implies$ coordination number = 6.
- **Answer**: **6**.

### Q35. Mass of Solute for Solution
- **Derivation**:
  $$m = M \times V \times \text{Molarity} = 40.0 \times 0.250 \times 0.50 = 5.0\text{ g}$$
- **Answer**: **5.0** (or **5**).

### Q36. Enthalpy of Formation of Water
- **Derivation**:
  - $36.0\text{ g}$ of water corresponds to $2.0\text{ moles}$.
  - Heat evolved $= 2.0 \times 285.8 = 571.6\text{ kJ}$.
- **Answer**: **571.6**.

---

## PART III: MATHEMATICS

### Q37. Tangent to Cubic Curve
- **Derivation**:
  - At $x = 2$: $y = 8 - 6 + 2 = 4$.
  - $y' = 3x^2 - 3$. At $x = 2$, $y' = 12 - 3 = 9$.
  - Tangent: $y - 4 = 9(x - 2) \implies y - 4 = 9x - 18 \implies 9x - y - 14 = 0$.
- **Correct Option**: **(A)**.

### Q38. Definite Integral of tan^3(x)
- **Derivation**:
  $$\int_0^{\pi/4} \tan^3 x\,dx = \int_0^{\pi/4} \tan x(\sec^2 x - 1)\,dx = \left[\frac{\tan^2 x}{2} - \ln|\sec x|\right]_0^{\pi/4} = \frac{1}{2} - \ln\sqrt{2} = \frac{1}{2} - \frac{1}{2}\ln 2 = \frac{1}{2}(1 - \ln 2)$$
- **Correct Option**: **(A)**.

### Q39. Area Bounded by Parabola and Latus Rectum
- **Derivation**:
  - $y^2 = 4x \implies a = 1$. Latus rectum is $x = 1$.
  - Area $= 2 \int_0^1 2\sqrt{x}\,dx = 4 \left[\frac{2}{3}x^{3/2}\right]_0^1 = \frac{8}{3}$.
- **Correct Option**: **(A)**.

### Q40. Linear Differential Equation
- **Derivation**:
  - $\text{IF} = e^{\int 1\,dx} = e^x$.
  - $y e^x = \int e^{-x} e^x\,dx = \int 1\,dx = x + C \implies y = (x + C)e^{-x}$.
- **Correct Option**: **(A)**.

### Q41. Numbers Divisible by 5
- **Derivation**:
  - Case 1: Last digit is 0. First 3 digits chosen from $\{1, 2, 3, 4, 5\}$ in $5 \times 4 \times 3 = 60$ ways.
  - Case 2: Last digit is 5. First digit chosen from $\{1, 2, 3, 4\}$ (4 choices, cannot be 0). Second and third digits from remaining 4 digits in $4 \times 3 = 12$ ways. Total $= 4 \times 12 = 48$ ways.
  - Total numbers $= 60 + 48 = 108$.
- **Correct Option**: **(A)**.

### Q42. Shortest Distance Between Skew Lines
- **Derivation**:
  - Line 1: through $(0, 0, 0)$ with direction $\vec{b}_1 = (1, 2, 1)$.
  - Line 2: through $(1, 0, 0)$ with direction $\vec{b}_2 = (2, 1, 2)$.
  - $\vec{a}_2 - \vec{a}_1 = (1, 0, 0)$.
  - $\vec{b}_1 \times \vec{b}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 1 \\ 2 & 1 & 2 \end{vmatrix} = \hat{i}(4 - 1) - \hat{j}(2 - 2) + \hat{k}(1 - 4) = 3\hat{i} - 3\hat{k}$.
  - Magnitude: $\sqrt{3^2 + 0^2 + (-3)^2} = \sqrt{18} = 3\sqrt{2}$.
  - $|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)| = |1(3) + 0 + 0| = 3$.
  - $d = \frac{3}{3\sqrt{2}} = \frac{1}{\sqrt{2}}$.
- **Correct Option**: **(C)**.

### Q43. Quartic Curve Analysis
- **Analysis**:
  - $f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3)$. (A is True)
  - At $x = 3$, $f'(x)$ changes from negative to positive $\implies$ local minimum. (B is True)
  - At $x = 0$, $f'(x) = 0$ but does not change sign $\implies$ horizontal inflection point. (C is True)
  - $f(3) = 81 - 108 + 10 = -17$ (global minimum). (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q44. Hyperbola Parameters
- **Analysis**:
  - $\frac{x^2}{9} - \frac{y^2}{16} = 1 \implies a = 3, b = 4$.
  - Vertices $(\pm 3, 0)$, $e = \sqrt{1 + 16/9} = 5/3$, foci $(\pm 5, 0)$, directrices $x = \pm a/e = \pm 9/5$.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Matrix Theorems
- **Analysis**: Determinant multiplicativity, non-additivity in general, determinant of inverse, trace linearity.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Scalar Triple Product
- **Analysis**: Definition, geometrical meaning (volume of parallelepiped), coplanarity criterion, dot-cross exchange.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Complex Conjugate Properties
- **Analysis**: Modulus squared, additivity and multiplicativity of conjugation, unit circle property.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Classical Card Probability
- **Analysis**: $P(\text{Ace}) = 4/52 = 1/13$; $P(\text{Spade}) = 13/52 = 1/4$; $P(\text{Ace of Spades}) = 1/52 = (1/13)(1/4) \implies$ independent; $P(\text{Ace} \cup \text{Spade}) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13$.
- **Correct Options**: **(A, B, C, D)**.

### Q49. Standard Limit
- **Derivation**: $\lim_{x \to 0} \frac{1 - \cos 2x}{x^2} = \frac{2^2}{2} = 2$.
- **Answer**: **2**.

### Q50. Area Under Parabola
- **Derivation**:
  $$\int_0^4 (4x - x^2)\,dx = \left[2x^2 - \frac{x^3}{3}\right]_0^4 = 32 - \frac{64}{3} = \frac{32}{3} \approx 10.67$$
- **Answer**: **10.67**.

### Q51. Odd Integrand
- **Derivation**: $x^3 \sqrt{1 - x^2}$ is an odd function over symmetric interval $[-1, 1] \implies I = 0$.
- **Answer**: **0**.

### Q52. Radius of Sphere
- **Derivation**: $R = \sqrt{49} = 7$.
- **Answer**: **7**.

### Q53. Roots of Quadratic
- **Derivation**: $(x - 3)^2 = 0 \implies x = 3$ (1 distinct real root).
- **Answer**: **1**.

### Q54. Determinant
- **Derivation**: $3(2) - 4(1) = 6 - 4 = 2$.
- **Answer**: **2**.
