# Detailed Solutions and Pedagogical Analysis — Mock Examination 18 (Paper 2)
### Organising Institute Style: IIT Roorkee (`IIT_ROORKEE_STYLE` — Mechanics Dominance)

---

## PART I: PHYSICS

### Q1. Disc Climbing Step
- **Analysis**:
  - During collision, impact forces act at the corner $P$, so torque about $P$ is zero $\implies$ angular momentum about $P$ is conserved. (A is True)
  - $L_i = I_{cm} \omega_0 + M v_0 (R - h) = \left(\frac{1}{2} M R^2\right) \omega_0 + M (R \omega_0) (R - h) = M R \omega_0 [R/2 + R - h] = M R^2 \omega_0 \left(\frac{3}{2} - \frac{h}{R}\right)$.
  - After impact, rotation is about $P$: $I_P = \frac{1}{2} M R^2 + M R^2 = \frac{3}{2} M R^2$.
  - $L_f = I_P \omega = \frac{3}{2} M R^2 \omega$.
  - Equating: $\frac{3}{2} M R^2 \omega = M R^2 \omega_0 \left(\frac{3}{2} - \frac{h}{R}\right) \implies \omega = \omega_0 \left(1 - \frac{2h}{3R}\right)$. (B is True)
  - To clear step, kinetic energy must overcome potential energy barrier $Mgh$. (C is True)
  - Normal force from ground does no work. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q2. Rolling Cylinder with Spring
- **Analysis**:
  - Restoring torque / force from spring: effective inertia is $M + I/R^2 = M + M/2 = \frac{3}{2} M$. (B is True)
  - Equation of motion: $\frac{3}{2} M \ddot{x} + k x = 0 \implies \omega = \sqrt{\frac{2k}{3M}} \implies T = 2\pi\sqrt{\frac{3M}{2k}}$. (A, C are True)
  - For thin spherical shell, $I = \frac{2}{3} M R^2 \implies M_{\text{eff}} = M + 2/3 M = \frac{5}{3} M \implies T = 2\pi\sqrt{\frac{5M}{3k}}$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q3. Falling Dumbbell
- **Analysis**:
  - Coordinates: $(x_1, 0) = (L\sin\theta, 0)$ and $(0, y_2) = (0, L\cos\theta)$. Midpoint $(L/2 \sin\theta, L/2 \cos\theta)$ traces circle of radius $L/2$. (A is True)
  - Normal force from vertical wall: $N_w = m \ddot{x}_2$. Setting $N_w = 0$ gives separation at $\cos\theta = 2/3$. (B, C are True)
  - Smooth surfaces $\implies$ mechanical energy conserved. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q4. Capillary Rise
- **Analysis**: All four statements correctly state equilibrium height, surface tension force, work done, and energy dissipation.
- **Correct Options**: **(A, B, C, D)**.

### Q5. Diesel Cycle Thermodynamics
- **Analysis**: Reversible isobaric heat addition, isochoric heat rejection, isentropic compression/expansion.
- **Correct Options**: **(A, B, C, D)**.

### Q6. Binary Star System
- **Analysis**: Center of mass coordinates, Kepler's third law, orbital angular momentum ratio, total mechanical energy.
- **Correct Options**: **(A, B, C, D)**.

### Q7. Time to Roll Down Incline
- **Derivation**:
  - Linear acceleration of rolling cylinder: $a = \frac{g \sin\theta}{1 + 1/2} = \frac{2}{3} g \sin 30^\circ = \frac{2}{3} (10.0) (0.50) = \frac{10}{3} = 3.33\text{ m/s}^2$.
  - $L = \frac{1}{2} a t^2 \implies 6.0 = \frac{1}{2} \left(\frac{10}{3}\right) t^2 = \frac{5}{3} t^2 \implies t^2 = \frac{18}{5} = 3.6 \implies t = \sqrt{3.6} \approx 1.90\text{ s}$.
- **Answer**: **1.90** (or **1.9**).

### Q8. Angular Impulse on Hanging Rod
- **Derivation**:
  - Angular impulse about pivot: $\Delta L = J L = 2.0 \times 1.0 = 2.0\text{ N}\cdot\text{m}\cdot\text{s}$.
  - $I = \frac{1}{3} M L^2 = \frac{1}{3} (1.0) (1.0)^2 = \frac{1}{3}\text{ kg}\cdot\text{m}^2$.
  - $\omega = \frac{\Delta L}{I} = \frac{2.0}{1/3} = 6.0\text{ rad/s}$.
- **Answer**: **6.0** (or **6**).

### Q9. Tension in Pendulum at Lowest Point
- **Derivation**:
  - By conservation of energy: $m g l = \frac{1}{2} m v^2 \implies v^2 = 2 g l$.
  - Centripetal force: $T - m g = \frac{m v^2}{l} = 2 m g \implies T = 3 m g$.
  - $T = 3 \times 0.50 \times 9.8 = 1.5 \times 9.8 = 14.7\text{ N}$.
- **Answer**: **14.7**.

### Q10. Poiseuille Flow Rate
- **Derivation**:
  $$Q = \frac{\pi r^4 \Delta P}{8 \eta l} = \frac{3.14 \times (1.0 \times 10^{-3})^4 \times 800}{8 \times 0.0010 \times 1.0} = \frac{3.14 \times 10^{-12} \times 800}{8 \times 10^{-3}} = 3.14 \times 10^{-7}\text{ m}^3/\text{s} = 0.314 \approx 0.3\text{ mL/s}$$
- **Answer**: **0.3** (or **0.31**).

### Q11. Satellite Speed Ratio
- **Derivation**:
  - By conservation of angular momentum: $r_{\max} v_{\min} = r_{\min} v_{\max} \implies \frac{v_{\max}}{v_{\min}} = \frac{r_{\max}}{r_{\min}} = 3.0$.
- **Answer**: **3.0** (or **3**).

### Q12. Organ Pipe Resonant Length
- **Derivation**:
  - Open pipe fundamental: $f = \frac{v}{2 L_1}$.
  - Closed pipe fundamental: $f = \frac{v}{4 L_2}$.
  - $\frac{v}{2 L_1} = \frac{v}{4 L_2} \implies 4 L_2 = 2 L_1 \implies L_2 = \frac{L_1}{2} = \frac{85.0}{2} = 42.5\text{ cm}$.
- **Answer**: **42.5**.

### Q13. Moment of Inertia of Square Plate
- **Derivation**:
  - By perpendicular axis theorem: $I_z = I_x + I_y = \frac{1}{12} M a^2 + \frac{1}{12} M a^2 = \frac{1}{6} M a^2 \implies k = 6$.
- **Answer**: **6**.

### Q14. Stable Equilibrium of Pendulum
- **Derivation**: Only the vertically downward position is a stable equilibrium (1 position).
- **Answer**: **1**.

### Q15. Angle in Elastic Glancing Collision
- **Derivation**: For equal mass elastic collision with stationary target, $\vec{v}_1 \cdot \vec{v}_2 = 0 \implies 90^\circ$.
- **Answer**: **90**.

### Q16. Degrees of Freedom of Rigid Body
- **Derivation**: A 3D rigid body has 3 translational + 3 rotational = 6 degrees of freedom.
- **Answer**: **6**.

### Q17. Period of Series Springs
- **Derivation**:
  - $T_1 = 2\pi\sqrt{m/k_1} = 3 \implies m/k_1 = 9 / (4\pi^2)$.
  - $T_2 = 2\pi\sqrt{m/k_2} = 4 \implies m/k_2 = 16 / (4\pi^2)$.
  - For series: $\frac{1}{k_{\text{eq}}} = \frac{1}{k_1} + \frac{1}{k_2} \implies T_{\text{eq}}^2 = T_1^2 + T_2^2 = 3^2 + 4^2 = 25 \implies T_{\text{eq}} = 5\text{ s}$.
- **Answer**: **5**.

### Q18. Quantum Numbers
- **Derivation**: For $n = 4$, $l$ can be $2, 3$ to have $m_l = +2$. For each $l$, there are 2 spin states ($m_s = \pm 1/2$).
  $l = 2$ gives 2 electrons, $l = 3$ gives 2 electrons $\implies$ total = 4 electrons.
- **Answer**: **4**.

---

## PART II: CHEMISTRY

### Q19. Cannizzaro Reaction
- **Analysis**: Disproportionation of formaldehyde to methanol and formate, hydride transfer as RDS.
- **Correct Options**: **(A, B, C)**.

### Q20. Spectrochemical Series and CFT
- **Analysis**: Ligand field strength ordering, backbonding ligands, halide weak fields, pairing condition.
- **Correct Options**: **(A, B, C, D)**.

### Q21. Blast Furnace Metallurgy of Iron
- **Analysis**: Haematite ore, CO reduction in upper zone, C reduction in lower zone, wrought iron purity.
- **Correct Options**: **(A, B, C, D)**.

### Q22. Alcohol Dehydration Mechanisms
- **Analysis**: $3^\circ$ via $E1$, $2^\circ$ carbocation rearrangement, $1^\circ$ via $E2$, Saytzeff rule.
- **Correct Options**: **(A, B, C, D)**.

### Q23. Group 16 Allotropes and Properties
- **Analysis**: Oxygen anomalous behavior, ozone structure, rhombic vs monoclinic sulfur transition at $369\text{ K}$.
- **Correct Options**: **(A, B, C, D)**.

### Q24. Adsorption Thermodynamics
- **Analysis**: Negative $\Delta H$ and $\Delta S$, spontaneity condition, enthalpy ranges for physisorption vs chemisorption.
- **Correct Options**: **(A, B, C, D)**.

### Q25. Zinc Electrode Potential
- **Derivation**:
  $$E = E^\circ - \frac{0.0591}{2}\log_{10}\left(\frac{1}{[\text{Zn}^{2+}]}\right) = -0.76 - \frac{0.0591}{2}\log_{10}(10^2) = -0.76 - 0.0591 = -0.819 \approx -0.82\text{ V}$$
- **Answer**: **-0.82**.

### Q26. Solubility of Ag2CrO4
- **Derivation**:
  - $K_{sp} = 4s^3 \implies 1.1 \times 10^{-12} = 4s^3 \implies s^3 = 2.75 \times 10^{-13} = 275 \times 10^{-15}$.
  - $s = (275)^{1/3} \times 10^{-5} \approx 6.50 \times 10^{-5}\text{ M} = 65\,\mu\text{mol/L}$.
- **Answer**: **65**.

### Q27. Remaining Reactant
- **Derivation**:
  - $t_{1/2} = \frac{0.693}{0.020} = 34.65\text{ min}$.
  - Total time $69.3\text{ min} = 2 \times 34.65 = 2$ half-lives.
  - Percentage remaining $= (1/2)^2 \times 100 = 25.0\%$.
- **Answer**: **25.0** (or **25**).

### Q28. Molar Mass from Boiling Point Elevation
- **Derivation**:
  - $\Delta T_b = 100.26 - 100.00 = 0.26\text{ K}$.
  - $\Delta T_b = K_b \frac{w_2 \times 1000}{M_2 \times w_1} \implies 0.26 = 0.52 \times \frac{5.0 \times 1000}{M_2 \times 100} = 0.52 \times \frac{50}{M_2} = \frac{26}{M_2}$.
  - $M_2 = \frac{26}{0.26} = 100.0\text{ g/mol}$.
- **Answer**: **100**.

### Q29. Heat of Combustion of Methane
- **Derivation**:
  - Moles of methane $= 3.20 / 16.0 = 0.20\text{ mol}$.
  - Heat evolved $= 0.20 \times 890.0 = 178.0\text{ kJ}$.
- **Answer**: **178.0** (or **178**).

### Q30. Limiting Molar Conductivity of NaBr
- **Derivation**:
  $$\Lambda_m^\circ(\text{NaBr}) = \Lambda_m^\circ(\text{NaCl}) + \Lambda_m^\circ(\text{KBr}) - \Lambda_m^\circ(\text{KCl}) = 126.4 + 151.8 - 149.8 = 128.4\text{ S}\cdot\text{cm}^2/\text{mol}$$
- **Answer**: **128.4**.

### Q31. Oxidation State of Ni in Ni(CO)4
- **Derivation**: Carbonyl ligand is neutral $\implies$ oxidation state of Ni is 0.
- **Answer**: **0**.

### Q32. Bridging Oxygens in P4O10
- **Derivation**: In $\text{P}_4\text{O}_{10}$, there are 6 bridging $\text{P}-\text{O}-\text{P}$ oxygen atoms and 4 terminal $\text{P}=\text{O}$ oxygens.
- **Answer**: **6**.

### Q33. Basicity of H3PO2
- **Derivation**: Contains 1 ionizable $-\text{OH}$ group $\implies$ basicity = 1.
- **Answer**: **1**.

### Q34. Coordination Number in Simple Cubic
- **Derivation**: Each sphere touches 6 neighbors $\implies$ coordination number = 6.
- **Answer**: **6**.

### Q35. Stereoisomers of 2,3-Dichlorobutane
- **Derivation**: Contains 2 similar chiral centers: $(2R, 3R)$, $(2S, 3S)$ enantiomeric pair, and 1 meso form $\implies 3$ stereoisomers.
- **Answer**: **3**.

### Q36. Pi Electrons in Benzene
- **Derivation**: 3 conjugated double bonds $\implies 6$ $\pi$-electrons.
- **Answer**: **6**.

---

## PART III: MATHEMATICS

### Q37. Analysis of x + 1/x
- **Analysis**:
  - AM-GM inequality gives $x + 1/x \ge 2$ with equality at $x = 1$. (A is True)
  - $f'(x) = 1 - 1/x^2 = 0 \implies x = 1$. Decreasing on $(0, 1)$, increasing on $(1, \infty)$. (B is True)
  - $f''(x) = 2/x^3 > 0$ for $x > 0$. (C is True)
  - $\lim_{x\to\infty} [f(x) - x] = \lim_{x\to\infty} 1/x = 0 \implies y = x$ is oblique asymptote. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q38. Parabola Properties
- **Analysis**:
  - $y^2 = 4ax = 12x \implies a = 3$. Focus $(3, 0)$, latus rectum $4a = 12$, directrix $x = -3$, focal distance $x_1 + a = x_1 + 3$.
- **Correct Options**: **(A, B, C, D)**.

### Q39. Matrix Symmetry
- **Analysis**: Sum is symmetric, product $AB$ symmetric iff $AB = BA$, $A - A^T$ skew-symmetric, $AA^T$ symmetric.
- **Correct Options**: **(A, B, C, D)**.

### Q40. Euler Log-Sine Integrals
- **Analysis**: All four identities are classical properties of the log-sine integral.
- **Correct Options**: **(A, B, C, D)**.

### Q41. Axiomatic Probability
- **Analysis**: Product rule, conditional probability, addition rule, exclusivity precludes independence (for positive probabilities).
- **Correct Options**: **(A, B, C, D)**.

### Q42. Vector Identities
- **Analysis**: Jacobi identity, Gram determinant, coplanar box product property.
- **Correct Options**: **(A, B, C, D)**.

### Q43. Definite Integral Evaluation
- **Derivation**:
  $$\int_0^3 (x^2 - 2x)\,dx = \left[\frac{x^3}{3} - x^2\right]_0^3 = \frac{27}{3} - 9 = 9 - 9 = 0$$
- **Answer**: **0**.

### Q44. Maximum of Quadratic
- **Derivation**: Vertex of $4x - x^2$ is at $x = 2$: $f(2) = 2(2) = 4$.
- **Answer**: **4**.

### Q45. Distance Between Parallel Lines
- **Derivation**:
  $$d = \frac{|7 - (-8)|}{\sqrt{4^2 + (-3)^2}} = \frac{15}{5} = 3$$
- **Answer**: **3**.

### Q46. Latus Rectum of Hyperbola
- **Derivation**:
  $$\text{Latus rectum} = \frac{2b^2}{a} = \frac{2(16)}{3} = \frac{32}{3} \approx 10.67$$
- **Answer**: **10.67**.

### Q47. Sum of Infinite GP
- **Derivation**:
  $$a = 4, r = 1/2 \implies S = \frac{a}{1 - r} = \frac{4}{1 - 1/2} = 8$$
- **Answer**: **8**.

### Q48. Orthogonal Vectors
- **Derivation**:
  $$\vec{u} \cdot \vec{v} = 2(1) - 1(3) + 1(k) = 2 - 3 + k = -1 + k = 0 \implies k = 1$$
- **Answer**: **1**.

### Q49. Permutations of "ROORKEE"
- **Derivation**:
  - 7 letters: R (2), O (2), K (1), E (2).
  - Total permutations $= \frac{7!}{2! 2! 2!} = \frac{5040}{8} = 630$.
- **Answer**: **630**.

### Q50. Degree of Differential Equation
- **Derivation**: Highest order derivative is $\frac{d^2 y}{dx^2}$, which has power 2 $\implies$ degree is 2.
- **Answer**: **2**.

### Q51. Limit
- **Derivation**: $\lim_{x \to 0} \frac{\sin 6x}{6x} \times \frac{6}{2} = 1 \times 3 = 3$.
- **Answer**: **3**.

### Q52. Real Solutions
- **Derivation**: $|x - 2| = 0 \implies x = 2$ (1 real solution).
- **Answer**: **1**.

### Q53. Diameter of Circle
- **Derivation**: $R = \sqrt{36} = 6 \implies$ diameter $= 2R = 12$.
- **Answer**: **12**.

### Q54. Sum of Roots
- **Derivation**: For $x^2 - 12x + 35 = 0$, sum of roots is $-(-12)/1 = 12$.
- **Answer**: **12**.
