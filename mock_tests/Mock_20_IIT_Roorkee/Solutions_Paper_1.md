# Detailed Solutions and Pedagogical Analysis — Mock Examination 20 (Paper 1)
### Organising Institute Style: IIT Roorkee (`IIT_ROORKEE_STYLE` — Contemporary Comprehensive Paradigm)

---

## PART I: PHYSICS

### Q1. Impulse on Spherical Shell
- **First Observation & Concept**: Rolling without slipping immediately after impulse requires $v_{cm} = R \omega$.
- **Derivation**:
  - Linear impulse: $J = M v_{cm}$.
  - Angular impulse about CM: $J h = I_{cm} \omega = \left(\frac{2}{3} M R^2\right) \omega$.
  - Pure rolling condition: $\omega = \frac{v_{cm}}{R} = \frac{J}{M R}$.
  - $J h = \frac{2}{3} M R^2 \left(\frac{J}{M R}\right) = \frac{2}{3} J R \implies h = \frac{2}{3} R$.
- **Correct Option**: **(A)**.

### Q2. Rolling Sphere Entering Smooth Curved Track
- **First Observation & Concept**: On the smooth track, friction is absent $\implies$ no torque about CM, so rotational kinetic energy remains unchanged!
- **Derivation**:
  - Only translational kinetic energy converts into gravitational potential energy.
  - $M g h = \frac{1}{2} M v_0^2 \implies h = \frac{v_0^2}{2g}$.
- **Correct Option**: **(A)**.

### Q3. Conical Pendulum
- **First Observation & Concept**: Balance of vertical forces: $T \cos\theta = m g \implies T = \frac{m g}{\cos\theta}$.
- **Correct Option**: **(A)**.

### Q4. Mass of Liquid in Capillary
- **First Observation & Concept**: $h = \frac{2T \cos\theta}{\rho g r}$.
- **Derivation**:
  - Mass of liquid column: $M = \rho (\pi r^2) h = \rho \pi r^2 \left(\frac{2T \cos\theta}{\rho g r}\right) = \frac{2\pi r T \cos\theta}{g} \propto r$.
  - When radius is doubled ($2r$), mass doubles: $M' = 2M$.
- **Correct Option**: **(A)**.

### Q5. Sliding Off Hemispherical Dome
- **First Observation & Concept**: Normal force vanishes: $N = m g \cos\theta - \frac{m v^2}{R} = 0 \implies v^2 = g R \cos\theta$.
- **Derivation**:
  - Conservation of energy: $\frac{1}{2} m v^2 - \frac{1}{2} m v_0^2 = m g R (1 - \cos\theta)$.
  - $\frac{1}{2} g R \cos\theta - \frac{1}{2} v_0^2 = g R - g R \cos\theta \implies \frac{3}{2} g R \cos\theta = g R + \frac{1}{2} v_0^2$.
  - $\cos\theta = \frac{2}{3} + \frac{v_0^2}{3gR} \implies \theta = \arccos\left(\frac{2}{3} + \frac{v_0^2}{3gR}\right)$.
- **Correct Option**: **(A)**.

### Q6. Gravity at Depth
- **First Observation & Concept**: Inside uniform solid sphere: $g(d) = g \left(1 - \frac{d}{R_e}\right)$.
- **Correct Option**: **(A)**.

### Q7. Rolling Solid Sphere on Incline
- **Analysis**: $a = \frac{g \sin\theta}{1 + 2/5} = \frac{5}{7} g \sin\theta$; friction $f = \frac{2}{7} M g \sin\theta$; $\mu_{\min} = \frac{2}{7}\tan\theta$; for $45^\circ$, $\mu_{\min} = 2/7$.
- **Correct Options**: **(A, B, C, D)**.

### Q8. Off-Center Force on Rod
- **Analysis**:
  - $a_{cm} = F/M$. (A is True)
  - $\tau = F (L/2) = I_{cm} \alpha = \left(\frac{1}{12} M L^2\right) \alpha \implies \alpha = \frac{6F}{ML}$. (B is True)
  - Point at distance $x$ from CM has acceleration $a = a_{cm} - \alpha x = \frac{F}{M} - \frac{6F x}{M L} = 0 \implies x = L/6$. (C, D are True)
- **Correct Options**: **(A, B, C, D)**.

### Q9. Torricelli Efflux and Range
- **Analysis**: $v = \sqrt{2gy}$, time to fall $t = \sqrt{2(H - y)/g}$, range $x = v t = 2\sqrt{y(H - y)}$, max range $H$ at $y = H/2$.
- **Correct Options**: **(A, B, C, D)**.

### Q10. Simple Harmonic Motion Dynamics
- **Analysis**: Maximum speed $\omega A$, maximum acceleration $\omega^2 A$, average kinetic energy, total energy.
- **Correct Options**: **(A, B, C, D)**.

### Q11. Reversible Adiabatic Gas Laws
- **Analysis**: $P V^\gamma = c$, $T V^{\gamma - 1} = c$, work formula, isentropic nature.
- **Correct Options**: **(A, B, C, D)**.

### Q12. Satellite Orbital Dynamics
- **Analysis**: $v = \sqrt{GM/R}$, $T \propto R^{3/2}$, energy $E = -GMm/(2R)$, angular momentum $L = m\sqrt{GMR}$.
- **Correct Options**: **(A, B, C, D)**.

### Q13. Disc Braking Time
- **Derivation**:
  - $I = \frac{1}{2} M R^2 = \frac{1}{2} (2.0) (0.50)^2 = 0.25\text{ kg}\cdot\text{m}^2$.
  - Torque $\tau = F R = 3.0 \times 0.50 = 1.50\text{ N}\cdot\text{m}$.
  - Angular deceleration $\alpha = \frac{\tau}{I} = \frac{1.50}{0.25} = 6.0\text{ rad/s}^2$.
  - Time $t = \frac{\omega_0}{\alpha} = \frac{12.0}{6.0} = 2.0\text{ s}$.
- **Answer**: **2.0** (or **2**).

### Q14. Force from Elastic Rebound
- **Derivation**:
  $$\Delta p = m v - (-m v) = 2 m v = 2 \times 0.50 \times 10.0 = 10.0\text{ N}\cdot\text{s}$$
  $$F_{\text{avg}} = \frac{\Delta p}{\Delta t} = \frac{10.0}{0.020} = 500.0\text{ N}$$
- **Answer**: **500** (or **500.0**).

### Q15. Simple Pendulum Length
- **Derivation**:
  $$T = 2\pi \sqrt{\frac{L}{g}} \implies 2.0 = 2\pi \sqrt{\frac{L}{9.8}} \implies \frac{L}{9.8} = \frac{1}{\pi^2} \implies L = \frac{9.8}{\pi^2} \approx \frac{9.8}{9.87} \approx 0.99\text{ m}$$
- **Answer**: **0.99**.

### Q16. Tension in Submerged Block String
- **Derivation**:
  - Buoyant force $F_B = \rho_w V g = 1000 \times 0.0050 \times 10.0 = 50.0\text{ N}$.
  - Weight $W = M g = 4.0 \times 10.0 = 40.0\text{ N}$.
  - Equilibrium: $F_B = W + T \implies T = F_B - W = 50.0 - 40.0 = 10.0\text{ N}$.
- **Answer**: **10** (or **10.0**).

### Q17. Skidding Distance Friction
- **Derivation**:
  $$v^2 = 2 a d = 2 (\mu g) d \implies 20.0^2 = 2 \times \mu \times 10.0 \times 40.0 = 800 \mu \implies 400 = 800 \mu \implies \mu = 0.50$$
- **Answer**: **0.50** (or **0.5**).

### Q18. Equal Mass Elastic Collision
- **Derivation**: Equal mass elastic head-on collision exchanges velocities $\implies v_2' = v_1 = 4.0\text{ m/s}$.
- **Answer**: **4.0** (or **4**).

---

## PART II: CHEMISTRY

### Q19. Hofmann Bromamide to Ethanol
- **Analysis**:
  - Amine $Y$ gives ethanol with nitrous acid $\implies Y$ is ethylamine ($\text{CH}_3\text{CH}_2\text{NH}_2$).
  - Hofmann bromamide reduces carbon count by 1, so compound $X$ is propanamide ($\text{CH}_3\text{CH}_2\text{CONH}_2$).
- **Correct Option**: **(A)**.

### Q20. Outer Orbital Complex
- **Analysis**:
  - $[\text{CoF}_6]^{3-}$ has weak-field $\text{F}^-$, high-spin $sp^3d^2$ (outer orbital), paramagnetic with 4 unpaired electrons.
- **Correct Option**: **(A)**.

### Q21. Iodoform Test
- **Analysis**: Pentan-2-one has a methyl ketone group ($-\text{COCH}_3$) and gives a positive iodoform test.
- **Correct Option**: **(A)**.

### Q22. Metallurgy of Zinc
- **Analysis**: Roasted zinc oxide is reduced with carbon/coke in a vertical retort at $1673\text{ K}$.
- **Correct Option**: **(A)**.

### Q23. Effect of Volume on Reaction Rate
- **Analysis**:
  - Reducing volume to $1/3$ increases concentrations by factor of 3: $[A]' = 3[A]$, $[B]' = 3[B]$.
  - $\text{Rate}' = k (3[A])^2 (3[B]) = 27 k [A]^2 [B] = 27 \times \text{Rate}$.
- **Correct Option**: **(A)**.

### Q24. Chromyl Chloride Test
- **Analysis**:
  - $\text{K}_2\text{Cr}_2\text{O}_7 + 4\text{NaCl} + 6\text{H}_2\text{SO}_4 \rightarrow 2\text{CrO}_2\text{Cl}_2 + 2\text{KHSO}_4 + 4\text{NaHSO}_4 + 3\text{H}_2\text{O}$.
  - $\text{CrO}_2\text{Cl}_2$ is chromyl chloride (red vapors).
- **Correct Option**: **(A)**.

### Q25. Williamson Ether Synthesis
- **Analysis**: $S_N 2$ mechanism, steric hindrance avoidance (primary halide + tertiary alkoxide), elimination if tertiary halide used.
- **Correct Options**: **(A, B, D)**.

### Q26. Actinoids Chemistry
- **Analysis**: Radioactivity, variable oxidation states from comparable $5f, 6d, 7s$ energies, actinoid contraction, nuclear fuel applications.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Lead-Acid Battery Recharge
- **Analysis**: Reverse electrode reactions, regeneration of $\text{H}_2\text{SO}_4$, electrolytic mode of operation.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Vitamins
- **Analysis**: Water vs fat solubility, scurvy/rickets/anemia deficiency syndromes.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Qualitative Group III Analysis
- **Analysis**: $\text{NH}_4\text{OH} + \text{NH}_4\text{Cl}$, common ion suppression of $[\text{OH}^-]$, precipitation of insoluble hydroxides.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Ideal Gas Thermodynamic Relations
- **Analysis**: $U = U(T)$, zero Joule-Thomson coefficient, Mayer's relation $C_P - C_V = R$, free expansion.
- **Correct Options**: **(A, B, C, D)**.

### Q31. pH of NaOH Solution
- **Derivation**: $[\text{OH}^-] = 0.010\text{ M} = 10^{-2}\text{ M} \implies \text{pOH} = 2.0 \implies \text{pH} = 12.0$.
- **Answer**: **12** (or **12.0**).

### Q32. Radioactive Decay
- **Derivation**: Number of half-lives $n = 45.0 / 15.0 = 3$. Remaining fraction $(1/2)^3 = 1/8 \implies k = 8$.
- **Answer**: **8**.

### Q33. Molar Mass of FCC Metal
- **Derivation**:
  - $V = a^3 = (3.60 \times 10^{-8})^3 = 4.666 \times 10^{-23}\text{ cm}^3$.
  - In FCC, $Z = 4$.
  - $\rho = \frac{Z M}{N_A V} \implies 9.0 = \frac{4 M}{6.02 \times 10^{23} \times 4.666 \times 10^{-23}} = \frac{4 M}{28.09} \implies M = \frac{9.0 \times 28.09}{4} \approx 63.2\text{ g/mol}$.
- **Answer**: **63.2**.

### Q34. Coordination Number in ZnS
- **Derivation**: $\text{Zn}^{2+}$ occupies alternate tetrahedral voids $\implies$ coordination number = 4.
- **Answer**: **4**.

### Q35. Moles of Electrons for Copper
- **Derivation**: $\text{Cu}^{2+} + 2e^- \rightarrow \text{Cu}$. 1 mole ($63.5\text{ g}$) requires 2 moles of electrons.
- **Answer**: **2**.

### Q36. Heat of Combustion of Ethanol
- **Derivation**:
  - Moles $= 23.0 / 46.0 = 0.50\text{ mol}$.
  - Heat evolved $= 0.50 \times 1368.0 = 684.0\text{ kJ}$.
- **Answer**: **684.0** (or **684**).

---

## PART III: MATHEMATICS

### Q37. Tangent to Circle
- **Derivation**:
  - Equation of tangent at $(x_1, y_1)$ to $x^2 + y^2 = r^2$ is $x x_1 + y y_1 = r^2$.
  - For $(3, 4)$ on $x^2 + y^2 = 25$: $3x + 4y = 25$.
- **Correct Option**: **(A)**.

### Q38. Standard Definite Integral
- **Derivation**:
  - By King's property: $2I = \int_0^{\pi/2} 1\,dx = \frac{\pi}{2} \implies I = \frac{\pi}{4}$.
- **Correct Option**: **(A)**.

### Q39. Area of Parabola Segment
- **Derivation**:
  - $y^2 = 8x$, line $x = 2$.
  - Area $= 2 \int_0^2 \sqrt{8x}\,dx = 2(2\sqrt{2}) \left[\frac{2}{3}x^{3/2}\right]_0^2 = \frac{8\sqrt{2}}{3} (2\sqrt{2}) = \frac{32}{3}$.
- **Correct Option**: **(A)**.

### Q40. Separable Differential Equation
- **Derivation**: $\frac{dy}{y} = \frac{dx}{x} \implies \ln|y| = \ln|x| + \ln|C| \implies y = C x$.
- **Correct Option**: **(A)**.

### Q41. Permutations with Grouping
- **Derivation**: Group 4 math books as 1 block $\implies 4$ objects to arrange in $4! = 24$ ways. Math books internally arrange in $4! = 24$ ways. Total $= 24 \times 24 = 576$.
- **Correct Option**: **(A)**.

### Q42. Distance to Plane
- **Derivation**:
  $$d = \frac{|0(1) + 0(2) - 0(2) + 6|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \frac{6}{\sqrt{9}} = \frac{6}{3} = 2$$
- **Correct Option**: **(A)**.

### Q43. Curve Analysis
- **Analysis**:
  - $f'(x) = 2x e^{-x} - x^2 e^{-x} = x(2 - x)e^{-x}$. (A is True)
  - At $x = 0$: $f'(x)$ changes from negative to positive $\implies$ local minimum $f(0) = 0$. (B is True)
  - At $x = 2$: $f'(x)$ changes from positive to negative $\implies$ local maximum $f(2) = 4/e^2$. (C is True)
  - $\lim_{x\to\infty} x^2 e^{-x} = 0$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q44. Circle Tangency
- **Analysis**: Center $(1, 2)$, radius 5, point $(4, 6)$ distance $\sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9+16} = 5$ on circle, tangent equation $(x-1)(3) + (y-2)(4) = 25 \implies 3x + 4y - 36 = 0$.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Matrix Determinant Properties
- **Analysis**: Transpose invariance, commutativity in determinant, orthogonal matrix $\det = \pm 1$, singular matrix non-trivial kernel.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Vector Identities
- **Analysis**: Cyclic scalar triple product, anticommutativity of cross product, cross product magnitude, orthogonality.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Modulus Properties
- **Analysis**: Modulus multiplicativity, quotient rule, triangle inequalities.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Binomial Distribution Properties
- **Analysis**: Mean $np$, variance $np(1-p)$, standard deviation, symmetry for $p = 1/2$.
- **Correct Options**: **(A, B, C, D)**.

### Q49. Standard Limit
- **Derivation**: $\lim_{x \to 0} \frac{e^{3x} - 1}{3x} \times 3 = 1 \times 3 = 3$.
- **Answer**: **3**.

### Q50. Area Under Parabola
- **Derivation**:
  $$\text{Area} = 2 \int_0^2 (4 - x^2)\,dx = 2 \left[4x - \frac{x^3}{3}\right]_0^2 = 2 \left(8 - \frac{8}{3}\right) = 2 \times \frac{16}{3} = \frac{32}{3} \approx 10.67$$
- **Answer**: **10.67**.

### Q51. Definite Integral
- **Derivation**:
  $$\int_0^1 x^5\,dx = \left[\frac{x^6}{6}\right]_0^1 = \frac{1}{6} \approx 0.167$$
- **Answer**: **0.167**.

### Q52. Radius of Circle
- **Derivation**: $R = \sqrt{100} = 10$.
- **Answer**: **10**.

### Q53. Real Solutions
- **Derivation**: $x^2 = -4 \implies$ no real solutions (0 real solutions).
- **Answer**: **0**.

### Q54. Determinant
- **Derivation**: $5(1) - 2(3) = 5 - 6 = -1$.
- **Answer**: **-1**.
