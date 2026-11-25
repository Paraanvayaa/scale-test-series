# Detailed Solutions and Pedagogical Analysis — Mock Examination 20 (Paper 2)
### Organising Institute Style: IIT Roorkee (`IIT_ROORKEE_STYLE` — Contemporary Comprehensive Paradigm)

---

## PART I: PHYSICS

### Q1. Cylinder on Plank
- **Analysis**:
  - Let $a_p$ be plank acceleration, $a_c$ cylinder CM acceleration, $f$ friction between them.
  - Plank: $F - f = M a_p$.
  - Cylinder: $f = M a_c$. Torque: $f R = I \alpha = \frac{1}{2} M R^2 \alpha \implies \alpha R = 2 a_c$.
  - Rolling without slipping: $a_p = a_c + \alpha R = 3 a_c$.
  - $F - M a_c = M (3 a_c) = 3 M a_c \implies F = 4 M a_c \implies a_c = \frac{F}{4M}$. (B is True)
  - $a_p = 3 a_c = \frac{3F}{4M}$. (A is True)
  - Friction force $f = M a_c = \frac{F}{4}$ forward on cylinder. (C is True)
  - Because there is no relative slipping at the contact surface, work done by static friction on the system is zero. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q2. Rolling Sphere on Incline
- **Analysis**:
  - Pure rolling condition: $\mu_s \ge \frac{2}{7}\tan\alpha$, $v = \sqrt{\frac{2gh}{1 + 2/5}} = \sqrt{\frac{10}{7}gh}$. (A is True)
  - During slipping: $a = g(\sin\alpha - \mu_k\cos\alpha)$. (B is True)
  - Static friction does no net work. (C is True)
  - Kinetic friction dissipates mechanical energy into thermal energy. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q3. Pendulum in Accelerated Cart
- **Analysis**: Effective gravity $g_{\text{eff}} = \sqrt{g^2 + a^2}$ at angle $\theta = \arctan(a/g)$. Tension $m g_{\text{eff}}$, period $2\pi\sqrt{L/g_{\text{eff}}}$.
- **Correct Options**: **(A, B, C, D)**.

### Q4. Venturi Meter and Fluid Dynamics
- **Analysis**: Lower pressure at throat, flow rate $\propto \sqrt{\Delta P}$, discharge coefficient accounts for head loss, Bernoulli elevation term.
- **Correct Options**: **(A, B, C, D)**.

### Q5. Brayton Cycle
- **Analysis**: All four statements correctly state the ideal gas turbine cycle thermodynamics.
- **Correct Options**: **(A, B, C, D)**.

### Q6. Elliptical Trajectory of Projectile
- **Analysis**:
  - $v = \sqrt{G M_e / R_e} < v_e = \sqrt{2 G M_e / R_e}$, so orbit is bound ellipse with center of Earth as focus. (A, B are True)
  - Semi-major axis $a$: $E = \frac{1}{2} m v^2 - \frac{G M m}{R_e} = \frac{1}{2} \frac{G M m}{R_e} - \frac{G M m}{R_e} = -\frac{G M m}{2 R_e} \implies a = R_e$.
  - Since perigee is at $R_e$, apogee is at $2a - R_e = 2R_e - R_e = R_e$, wait! If $a = R_e$, apogee is $R_e$ (circular orbit at surface). So $h = 0$ if launched horizontally, or for vertical launch $v^2 = 2g h / (1 + h/R_e) \implies h = R_e / 1$. (C is False)
  - Energy is negative. (D is True)
- **Correct Options**: **(A, B, D)**.

### Q7. Distance Travelled Along Incline
- **Derivation**:
  - Deceleration rolling up: $a = \frac{g \sin\theta}{1 + 1/2} = \frac{2}{3} (10.0) \sin 30^\circ = \frac{10}{3}\text{ m/s}^2$.
  - $v_0^2 = 2 a d \implies 25.0 = 2 \left(\frac{10}{3}\right) d = \frac{20}{3} d \implies d = \frac{75}{20} = 3.75\text{ m}$.
- **Answer**: **3.75**.

### Q8. Bullet Impact on Pivoted Rod
- **Derivation**:
  - Angular momentum about central pivot:
    $$L_i = m v d = 0.10 \times 100.0 \times 0.40 = 4.0\text{ kg}\cdot\text{m}^2\text{/s}$$
  - Final moment of inertia:
    $$I = \frac{1}{12} M L^2 + m d^2 = \frac{1}{12} (3.0) (1.0)^2 + 0.10 (0.40)^2 = 0.25 + 0.016 = 0.266\text{ kg}\cdot\text{m}^2$$
  - $\omega = \frac{L_i}{I} = \frac{4.0}{0.266} \approx 15.0\text{ rad/s}$.
- **Answer**: **15.0** (or **15**).

### Q9. Elastic Potential Energy in Stretched Wire
- **Derivation**:
  - Force $F = M g = 20.0 \times 10.0 = 200.0\text{ N}$.
  - Elongation $\Delta L = \frac{F L}{A Y} = \frac{200.0 \times 2.0}{(2.0 \times 10^{-6}) \times (2.0 \times 10^{11})} = \frac{400}{4.0 \times 10^5} = 1.0 \times 10^{-3}\text{ m}$.
  - Stored energy $U = \frac{1}{2} F \Delta L = \frac{1}{2} \times 200.0 \times 1.0 \times 10^{-3} = 0.10\text{ J} = 100.0\text{ mJ}$.
- **Answer**: **100.0** (or **100**).

### Q10. Efflux Rate
- **Derivation**:
  - $v = \sqrt{2gh} = \sqrt{2 \times 10.0 \times 5.0} = 10.0\text{ m/s}$.
  - $Q = a v = (2.0 \times 10^{-4}\text{ m}^2) \times 10.0\text{ m/s} = 2.0 \times 10^{-3}\text{ m}^3/\text{s} = 2.0\text{ L/s}$.
- **Answer**: **2.0** (or **2**).

### Q11. Satellite Energy
- **Derivation**:
  - For circular orbit of radius $r$: $K = \frac{G M m}{2r}$, $E = -K = -\frac{G M m}{2r}$.
  - At $r_1 = 2 R_e$: $E_1 = -\frac{G M m}{4 R_e} = -K$.
  - At $r_2 = 4 R_e$: $E_2 = -\frac{G M m}{8 R_e} = -\frac{1}{2} K$.
  - Energy required $\Delta E = E_2 - E_1 = -\frac{1}{2} K - (-K) = \frac{1}{2} K = 0.5 K$.
- **Answer**: **0.5**.

### Q12. Resultant Oscillation Amplitude
- **Derivation**: $A = \sqrt{3.0^2 + 4.0^2} = 5.0\text{ cm}$.
- **Answer**: **5.0** (or **5**).

### Q13. Radius of Gyration About Tangent
- **Derivation**:
  - $I = \frac{2}{5} M R^2 + M R^2 = \frac{7}{5} M R^2 = M k^2 \implies k = \sqrt{7/5} R = \sqrt{1.4} \times 10 = 1.183 \times 10 = 11.83 \approx 12\text{ cm}$ (or $\sqrt{70} \approx 8.37$).
  - If question takes $\sqrt{7/5} R = 11.83 \approx 12$. Let's state 12.
- **Answer**: **12**.

### Q14. Fraction of Retained KE
- **Derivation**:
  - $v_1' = \frac{m_1 - m_2}{m_1 + m_2} v_0 = \frac{m - 3m}{m + 3m} v_0 = -\frac{2m}{4m} v_0 = -\frac{1}{2} v_0$.
  - $K_1' = \frac{1}{2} m (v_1')^2 = \frac{1}{4} K_0 \implies \frac{1}{k} = \frac{1}{4} \implies k = 4$.
- **Answer**: **4**.

### Q15. Planes of Symmetry in Cube
- **Derivation**: A cube has 3 planes parallel to faces and 6 diagonal planes $= 9$ planes of symmetry.
- **Answer**: **9**.

### Q16. Translational Degrees of Freedom
- **Derivation**: Every atom or molecule in 3D space has 3 translational degrees of freedom.
- **Answer**: **3**.

### Q17. Period of Cut Spring
- **Derivation**:
  - When spring is cut into 4 equal pieces, $k' = 4k$.
  - $T' = 2\pi \sqrt{\frac{m}{4k}} = \frac{T}{2} = \frac{4}{2} = 2\text{ s}$.
- **Answer**: **2**.

### Q18. Orbitals in n = 3 Shell
- **Derivation**: Total orbitals $= n^2 = 3^2 = 9$.
- **Answer**: **9**.

---

## PART II: CHEMISTRY

### Q19. Claisen Condensation
- **Analysis**: Ester enolate formation, nucleophilic acyl substitution, ethyl acetoacetate synthesis, driving force deprotonation.
- **Correct Options**: **(A, B, C, D)**.

### Q20. Ionization Isomerism
- **Analysis**: Sulfate vs bromide counter-ions, specific precipitation tests with $\text{AgNO}_3$ and $\text{BaCl}_2$, low-spin octahedral $\text{Co(III)}$.
- **Correct Options**: **(A, B, C, D)**.

### Q21. Carbonyl Reactivity
- **Analysis**: Aldehyde vs ketone reactivity, bisulfite adducts, selective Tollens' behavior, Schiff's base formation.
- **Correct Options**: **(A, B, C, D)**.

### Q22. Metallurgy of Aluminum
- **Analysis**: Bayer's process leaching, precipitation, Hall-Héroult molten salt electrolysis.
- **Correct Options**: **(A, B, C, D)**.

### Q23. Halogen Periodic Trends
- **Analysis**: Visible absorption colors, standard reduction potential ordering, fluorine electronegativity, $\text{HF}$ weakness.
- **Correct Options**: **(A, B, C, D)**.

### Q24. Solution Adsorption
- **Analysis**: Temperature and surface area dependence, concentration dependence, modified Freundlich isotherm.
- **Correct Options**: **(A, B, C, D)**.

### Q25. Standard Cadmium Potential
- **Derivation**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = 0.00 - E^\circ_{\text{Cd}^{2+}/\text{Cd}} = 0.40\text{ V} \implies E^\circ_{\text{Cd}^{2+}/\text{Cd}} = -0.40\text{ V}$.
- **Answer**: **-0.40** (or **-0.4**).

### Q26. Ksp of Ca(OH)2
- **Derivation**:
  - $s = 0.010\text{ M}$.
  - $K_{sp} = 4s^3 = 4 (0.010)^3 = 4 \times 10^{-6} \implies k = 4$.
- **Answer**: **4**.

### Q27. Time for 87.5% Reaction
- **Derivation**:
  - $87.5\% = 7/8$ reacted $\implies 1/8 = (1/2)^3$ remains $\implies 3$ half-lives.
  - $t = 3 \times 20.0 = 60.0\text{ min}$.
- **Answer**: **60** (or **60.0**).

### Q28. Molality from Freezing Point
- **Derivation**:
  $$m = \frac{\Delta T_f}{K_f} = \frac{0.186}{1.86} = 0.10\text{ mol/kg}$$
- **Answer**: **0.10** (or **0.1**).

### Q29. Enthalpy of Transition
- **Derivation**:
  $$\Delta H_{\text{trans}} = \Delta H_c(\text{graphite}) - \Delta H_c(\text{diamond}) = -393.5 - (-395.4) = +1.9\text{ kJ/mol}$$
- **Answer**: **1.9**.

### Q30. Limiting Molar Conductivity of CH3COOH
- **Derivation**:
  $$\Lambda_m^\circ = 349.6 + 40.9 = 390.5\text{ S}\cdot\text{cm}^2/\text{mol}$$
- **Answer**: **390.5**.

### Q31. Oxidation State of S in Caro's Acid
- **Derivation**: In $\text{H}_2\text{SO}_5$ (contains one peroxo bond): $2(+1) + x + 3(-2) + 2(-1) = 0 \implies x = +6$.
- **Answer**: **6**.

### Q32. Bridging Carbonyls in Co2(CO)8
- **Derivation**: 2 bridging carbonyl ligands.
- **Answer**: **2**.

### Q33. Basicity of Trimeric Metaphosphoric Acid
- **Derivation**: Cyclic $(HPO_3)_3$ has 3 ionizable $-\text{OH}$ groups $\implies$ basicity = 3.
- **Answer**: **3**.

### Q34. Coordination Number in FCC
- **Derivation**: 12 nearest neighbors.
- **Answer**: **12**.

### Q35. Enantiomers of Lactic Acid
- **Derivation**: 1 chiral center $\implies$ 2 enantiomers (d and l).
- **Answer**: **2**.

### Q36. Sigma Bonds in Ethyne
- **Derivation**: $\text{H}-\text{C}\equiv\text{C}-\text{H}$ contains 2 $\text{C}-\text{H}$ and 1 $\text{C}-\text{C}$ $\sigma$-bonds $= 3$ $\sigma$-bonds.
- **Answer**: **3**.

---

## PART III: MATHEMATICS

### Q37. Analysis of x / (1 + |x|)
- **Analysis**: Continuous, strictly increasing ($f'(x) = 1/(1+|x|)^2 > 0$), differentiable at $x = 0$ ($f'(0) = 1$), range $(-1, 1)$, odd.
- **Correct Options**: **(A, B, C, D)**.

### Q38. Ellipse Parameters
- **Analysis**: Major axis $2a = 10$, minor axis $2b = 8$, $e = \sqrt{1 - 16/25} = 3/5$, latus rectum $2b^2/a = 32/5$.
- **Correct Options**: **(A, B, C, D)**.

### Q39. Orthogonal Matrix Properties
- **Analysis**: $\det = \pm 1$, inverse is transpose, $\det = 1$ is pure rotation, eigenvalues lie on unit circle in $\mathbb{C}$.
- **Correct Options**: **(A, B, C, D)**.

### Q40. Integrals of 1 / (1 + x^2)
- **Analysis**: Standard arctan integrals over finite, infinite, and symmetric intervals, Fundamental Theorem of Calculus.
- **Correct Options**: **(A, B, C, D)**.

### Q41. Probability Rules
- **Analysis**: Addition rule, independence, conditional probability, De Morgan's law.
- **Correct Options**: **(A, B, C, D)**.

### Q42. Vector Cross and Box Products
- **Analysis**: Distributivity, cyclic permutation, vector triple product, orthonormal basis volume.
- **Correct Options**: **(A, B, C, D)**.

### Q43. Definite Integral
- **Derivation**:
  $$\int_0^1 x(1 - 2x + x^2)\,dx = \int_0^1 (x - 2x^2 + x^3)\,dx = \left[\frac{x^2}{2} - \frac{2x^3}{3} + \frac{x^4}{4}\right]_0^1 = \frac{1}{2} - \frac{2}{3} + \frac{1}{4} = \frac{6 - 8 + 3}{12} = \frac{1}{12}$$
  $$k = 12$$
- **Answer**: **12**.

### Q44. Maximum Value of Linear Combination
- **Derivation**: $\sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.
- **Answer**: **10**.

### Q45. Distance Between Parallel Lines
- **Derivation**:
  $$d = \frac{|10 - (-16)|}{\sqrt{5^2 + (-12)^2}} = \frac{26}{\sqrt{25 + 144}} = \frac{26}{13} = 2$$
- **Answer**: **2**.

### Q46. Latus Rectum of Parabola
- **Derivation**: $y^2 = 16x \implies 4a = 16$.
- **Answer**: **16**.

### Q47. Sum of Infinite GP
- **Derivation**:
  $$a = 5, r = 1/2 \implies S = \frac{5}{1 - 1/2} = 10$$
- **Answer**: **10**.

### Q48. Orthogonal Vectors
- **Derivation**:
  $$3(4) + 2(-k) = 12 - 2k = 0 \implies k = 6$$
- **Answer**: **6**.

### Q49. Permutations of "ROORKEE"
- **Derivation**: $\frac{7!}{2! 2! 2!} = \frac{5040}{8} = 630$.
- **Answer**: **630**.

### Q50. Order of Differential Equation
- **Derivation**: Highest derivative is $\frac{d^4 y}{dx^4} \implies$ order is 4.
- **Answer**: **4**.

### Q51. Limit
- **Derivation**: $\lim_{x \to 0} \frac{\sin 8x}{8x} \times \frac{8}{2} = 1 \times 4 = 4$.
- **Answer**: **4**.

### Q52. Real Solutions
- **Derivation**: $|x - 5| = 0 \implies x = 5$ (1 solution).
- **Answer**: **1**.

### Q53. Radius of Circle
- **Derivation**: $R = \sqrt{64} = 8$.
- **Answer**: **8**.

### Q54. Sum of Roots
- **Derivation**: For $x^2 - 16x + 63 = 0$, sum of roots is 16.
- **Answer**: **16**.
