# Detailed Solutions and Pedagogical Analysis — Mock Examination 09 (Paper 1)
### Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)

---

## PART I: PHYSICS

### Q1. Sliding Bar on Inclined Rails in Vertical B-field
- **First Observation & Concept**: Motional EMF and terminal velocity under gravitational and magnetic force balance.
- **Key Insight**: Bar moves down incline with speed $v$. Horizontal component of velocity perpendicular to $\vec{B}$ is $v\cos\theta$.
- **Derivation**: Motional EMF $\mathcal{E} = B L v\cos\theta$. Current $I = \mathcal{E}/R = \frac{B L v\cos\theta}{R}$.
  Magnetic force $\vec{F}_m = I \vec{L} \times \vec{B}$ is purely horizontal, directed opposite to horizontal velocity. Magnitude $F_m = I L B = \frac{B^2 L^2 v\cos\theta}{R}$.
  Component of $F_m$ up the incline is $F_m \cos\theta = \frac{B^2 L^2 v\cos^2\theta}{R}$.
  At terminal velocity, downhill gravity component equals uphill magnetic force:
  $$m g \sin\theta = \frac{B^2 L^2 v_t \cos^2\theta}{R} \implies v_t = \frac{m g R \sin\theta}{B^2 L^2 \cos^2\theta}$$
- **Correct Option**: **(A)**.

### Q2. Polytropic Adiabatic Relation
- **First Observation & Concept**: $P \propto T^3 \implies P T^{-3} = \text{const}$.
- **Key Insight**: For an adiabatic process, $P^{1-\gamma} T^\gamma = \text{const} \implies P T^{\gamma/(1-\gamma)} = \text{const}$.
- **Derivation**: Equating exponents: $\frac{\gamma}{1 - \gamma} = -3 \implies \gamma = -3 + 3\gamma \implies 2\gamma = 3 \implies \gamma = 3/2$.
- **Correct Option**: **(B)**.

### Q3. Loss of Contact on Hemispherical Bowl
- **First Observation & Concept**: Centripetal force and normal reaction $N = 0$.
- **Key Insight**: By conservation of energy, $m g R(1 - \cos\theta) = \frac{1}{2} m v^2 \implies v^2 = 2 g R(1 - \cos\theta)$.
- **Derivation**: Radial dynamics: $m g \cos\theta - N = \frac{m v^2}{R}$. Setting $N = 0$:
  $$m g \cos\theta = \frac{m [2gR(1 - \cos\theta)]}{R} = 2mg - 2mg\cos\theta \implies 3\cos\theta = 2 \implies \cos\theta = 2/3$$
- **Correct Option**: **(B)**.

### Q4. Three-Slit Interference Intensities
- **First Observation & Concept**: Phasor addition for $N=3$ identical coherent slits.
- **Key Insight**: Intensity is $I(\delta) = I_0 \left(\frac{\sin(3\delta/2)}{\sin(\delta/2)}\right)^2$.
- **Derivation**: Principal maximum occurs at $\delta = 0$, giving $I_{\max} = 9 I_0$.
  First secondary maximum occurs at $\delta = 3\pi/3 = \pi$ (giving zero) or near $\delta = 3\pi/2 \implies \sin(3\delta/2) = 1, \sin(\delta/2) = 1/\sqrt{2} \implies I_{\text{sec}} \approx I_0 / (1/2) = 2I_0$ or exact phasor addition gives $I_{\text{sec}} = I_0$.
  Ratio $I_{\text{principal}} / I_{\text{secondary}} = 9 : 1$.
- **Correct Option**: **(B)**.

### Q5. Q-Value of D-D Fusion
- **First Observation & Concept**: Mass defect $\Delta m = 2 m(^{2}\text{H}) - [m(^{3}\text{He}) + m(^{1}\text{n})]$.
- **Derivation**:
  $$\Delta m = 2(2.0141) - (3.0160 + 1.0087) = 4.0282 - 4.0247 = 0.0035\text{ u}$$
  $$Q = 0.0035 \times 931.5\text{ MeV} \approx 3.26\text{ MeV}$$
- **Correct Option**: **(A)**.

### Q6. Resonant Frequency of Water-Dipped Pipe
- **First Observation & Concept**: Open pipe of length $L$ has $f_0 = \frac{v}{2L}$.
- **Key Insight**: When half-dipped, it becomes a closed pipe of length $L/2$.
- **Derivation**: Fundamental frequency of closed pipe of length $L' = L/2$ is $f' = \frac{v}{4 L'} = \frac{v}{4(L/2)} = \frac{v}{2L} = f_0$.
- **Correct Option**: **(B)**.

### Q7. Rolling Transition of Sphere
- **Analysis**:
  - Kinetic friction $f_k = \mu M g$ opposes translational motion, doing negative work on translation. (A is correct).
  - Torque of friction $\tau = f_k R$ spins up the sphere, doing positive rotational work. (B is correct).
  - Friction dissipates energy into heat, so total mechanical energy is not conserved. (C is incorrect).
  - Angular momentum about the contact point on the ground is conserved: $M v_0 R = M v_f R + I_{cm} \omega_f = M v_f R + (\frac{2}{5}MR^2)(v_f/R) = \frac{7}{5} M v_f R \implies v_f = \frac{5}{7}v_0$. (D is correct).
- **Correct Options**: **(A, B, D)**.

### Q8. Mixing of Two Gas Volumes
- **Analysis**:
  - Moles: $n_1 = P_1 V / (R T_1)$, $n_2 = P_2 V / (R T_2)$. Total moles $n = n_1 + n_2$. (B is correct).
  - Final volume $V_{\text{total}} = 2V$.
  - Final pressure $P = \frac{n R T}{2V} = \frac{R T}{2V}\left(\frac{P_1 V}{R T_1} + \frac{P_2 V}{R T_2}\right) = \frac{1}{2}\left(\frac{P_1 T}{T_1} + \frac{P_2 T}{T_2}\right)$. (A is correct).
  - Spontaneous mixing of two gases at different states is irreversible, increasing entropy. (D is correct).
- **Correct Options**: **(A, B, D)**.

### Q9. Azimuthally Charged Ring
- **Analysis**:
  - Net charge: $q = \int_0^{2\pi} \lambda_0 \cos\theta R\,d\theta = 0$. (A is correct).
  - Potential at center: $V = \frac{1}{4\pi\varepsilon_0 R}\int dq = 0$. (B is correct).
  - Electric dipole moment: $\vec{p} = \int \vec{r}\,dq = \int_0^{2\pi} (R\cos\theta\hat{i} + R\sin\theta\hat{j})(\lambda_0\cos\theta R\,d\theta) = \lambda_0 R^2 \pi \hat{i}$. Magnitude is $\pi R^2 \lambda_0$. (D is correct).
  - Field at center integrates to $\frac{\lambda_0}{4\varepsilon_0 R}(-\hat{i})$. (C is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q10. Cyclotron Motion of Electron
- **Analysis**: All four statements correctly state classical magnetic orbital relations.
- **Correct Options**: **(A, B, C, D)**.

### Q11. EM Wave in Dielectric Medium
- **Analysis**: All four statements correctly state Maxwell wave properties in linear dielectric media.
- **Correct Options**: **(A, B, C, D)**.

### Q12. Multi-Frequency Photoelectric Relations
- **Analysis**:
  - $K_1 = h\nu - \Phi$, $K_2 = 2h\nu - \Phi = 2(K_1 + \Phi) - \Phi = 2K_1 + \Phi > 2K_1$. (A and B correct).
  - $\Phi = K_2 - 2K_1$. (D is correct).
- **Correct Options**: **(A, B, D)**.

### Q13–Q18 Numerical Solutions
- **Q13**: $\eta = 1 - 300/400 = 0.25$. $W = \eta Q_H = 0.25 \times 500 = 125\text{ J}$. **Answer: 125**.
- **Q14**: $\beta = \frac{\lambda D}{d} = \frac{(500 \times 10^{-9})(1.0)}{0.2 \times 10^{-3}} = 2.5 \times 10^{-3}\text{ m} = 2.5\text{ mm}$. **Answer: 2.5 (or 2.50)**.
- **Q15**: $I = \frac{1}{3} M L^2 = \frac{1}{3}(3)(1.0)^2 = 1.0\text{ kg}\cdot\text{m}^2$. **Answer: 1.0 (or 1)**.
- **Q16**: $p = mv = h/\lambda \implies v = \frac{h}{m \lambda} = \frac{6.63 \times 10^{-34}}{(1.0 \times 10^{-20})(0.663 \times 10^{-9})} = \frac{6.63 \times 10^{-34}}{6.63 \times 10^{-30}} = 1.0 \times 10^{-4}\text{ m/s}$. **Answer: 0.0001 (or 1e-4)**.
- **Q17**: $U = \frac{1}{2} C V^2 = \frac{1}{2}(10 \times 10^{-6})(100)^2 = 5 \times 10^{-6} \times 10^4 = 0.05\text{ J}$. **Answer: 0.05**.
- **Q18**: $T = m \omega^2 l = 0.1 \times 100 \times 1.0 = 10\text{ N}$. **Answer: 10**.

---

## PART II: CHEMISTRY

### Q19. BCC Atomic Radius
- **Calculation**: In BCC, atoms touch along the body diagonal: $4r = a\sqrt{3} \implies r = \frac{\sqrt{3}}{4}a = \frac{1.732}{4}(300) = 129.9\text{ pm}$.
- **Correct Option**: **(B)**.

### Q20. Relationship Between $K_p$ and $K_c$
- **Calculation**: $\Delta n_g = 3 - (1 + 2) = 0 \implies K_p = K_c (RT)^0 = K_c$.
- **Correct Option**: **(C)**.

### Q21. Paramagnetic Square Planar Complex
- **Analysis**: $[\text{Cu}(\text{NH}_3)_4]^{2+}$: $\text{Cu}^{2+}$ ($d^9$) has 1 unpaired electron ($S = 1/2$), $\mu = \sqrt{1(3)} = 1.73\text{ BM}$. All other complexes are $d^8$ square planar (Ni) or $d^{10}$ (Zn) or low-spin $d^6$ (Co), all diamagnetic.
- **Correct Option**: **(B)**.

### Q22. Ether Cleavage by Concentrated HI
- **Reaction**: $\text{Ph-O-CH}_3 + \text{HI} \xrightarrow{373\text{ K}} \text{Ph-OH} + \text{CH}_3\text{I}$.
  The phenyl-oxygen bond has partial double bond character due to resonance, so iodide nucleophile attacks the methyl carbon ($S_N 2$).
- **Correct Option**: **(B)**.

### Q23. Standard Cell EMF
- **Calculation**: $E^\circ_{\text{cell}} = E^\circ(\text{Ag}^+/\text{Ag}) - E^\circ(\text{Cu}^{2+}/\text{Cu}) = +0.80 - (+0.34) = +0.46\text{ V}$.
- **Correct Option**: **(B)**.

### Q24. Xenon Trioxide Geometry
- **Analysis**: In $\text{XeO}_3$, Xe has 8 valence electrons. 3 $\text{Xe=O}$ double bonds consume 6 electrons, leaving 1 lone pair. Steric number $= 3 + 1 = 4 \implies sp^3$ hybridization, pyramidal molecular geometry.
- **Correct Option**: **(B)**.

### Q25. Reversible Isothermal Expansion Thermodynamics
- **Analysis**: All four statements correctly state reversible isothermal thermodynamics of ideal gases.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Tollens' Reagent Reduction
- **Analysis**: Glucose (aldose), fructose (ketose undergoing Lobry de Bruyn-Alberda van Ekenstein rearrangement in alkaline medium), formic acid (contains aldehyde group $\text{H-C=O}$), and benzaldehyde (aromatic aldehyde) all reduce Tollens' reagent!
- **Correct Options**: **(A, B, C, D)**.

### Q27. Cobalt Ammine Isomerism
- **Analysis**:
  - $[\text{Co}(\text{NH}_3)_4\text{Cl}_2]^+$ exhibits cis and trans isomerism. (A is correct).
  - The cis-isomer has $C_{2v}$ symmetry with planes of symmetry, making it achiral (optically inactive). Thus (B) is false.
  - The trans-isomer has an inversion center ($i$), achiral. (C is correct).
  - One chloride counterion precipitates as $\text{AgCl}$. (D is correct).
- **Correct Options**: **(A, C, D)**.

### Q28. Group 14 and 15 Hydrides
- **Analysis**: All four statements are standard descriptive p-block inorganic facts.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Qualitative Analysis Group III
- **Analysis**: All four statements describe the precipitation and separation chemistry of Group III cations.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Acyl Derivative Reactivity
- **Analysis**: Reactivity order: Acyl chloride > Anhydride > Ester > Amide. Statements A, B, C are correct. D is false.
- **Correct Options**: **(A, B, C)**.

### Q31–Q36 Numerical Solutions
- **Q31**: BCC lattice has 8 corner atoms ($8 \times 1/8 = 1$) and 1 center atom ($1$). Total atoms $= 2$. **Answer: 2**.
- **Q32**: $[\text{H}^+] = 1.0 \times 10^{-3}\text{ M} \implies \text{pH} = -\log(10^{-3}) = 3.0$. **Answer: 3.0 (or 3)**.
- **Q33**: $\text{Rate} \propto [A]^n$. When $[A] \to 4[A]$, $\text{Rate} \to 2\times \implies 4^n = 2 = 4^{1/2} \implies n = 0.5$. **Answer: 0.5**.
- **Q34**: $\Delta T_b = K_b m = 0.52 \times 0.50 = 0.26\text{ K}$. **Answer: 0.26**.
- **Q35**: $\mu = \sqrt{4(4+2)} = \sqrt{24} \approx 4.90\text{ BM}$. **Answer: 4.90**.
- **Q36**: Pentane ($\text{C}_5\text{H}_{12}$) has 3 structural isomers: n-pentane, isopentane, and neopentane. **Answer: 3**.

---

## PART III: MATHEMATICS

### Q37. Definite Integral of Rational Function
- **Calculation**: $\int_0^1 \frac{dx}{1 + x^2} = [\arctan x]_0^1 = \pi/4 - 0 = \pi/4$.
- **Correct Option**: **(A)**.

### Q38. Ellipse Eccentricity
- **Calculation**: Standard form: $\frac{x^2}{16} + \frac{y^2}{25} = 1$. Here $b^2 = 25 > a^2 = 16$.
  $$e = \sqrt{1 - a^2/b^2} = \sqrt{1 - 16/25} = \sqrt{9/25} = 3/5$$
- **Correct Option**: **(A)**.

### Q39. Unit Vector
- **Calculation**: $|\vec{a}| = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$.
  $\hat{a} = \frac{1}{7}(2\hat{i} + 3\hat{j} + 6\hat{k})$.
- **Correct Option**: **(A)**.

### Q40. Probability of Sum 7
- **Calculation**: Favorable outcomes: $(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)$ (6 outcomes).
  Probability $= 6 / 36 = 1/6$.
- **Correct Option**: **(A)**.

### Q41. Area Under Curve
- **Calculation**: $\int_0^2 x^3\,dx = [x^4/4]_0^2 = 16/4 = 4$.
- **Correct Option**: **(B)**.

### Q42. Variable Separable Differential Equation
- **Calculation**: $\frac{dy}{y} = \frac{dx}{x} \implies \ln y = \ln x + \ln C \implies y = C x$.
  $y(1) = 2 \implies C = 2 \implies y = 2x$.
- **Correct Option**: **(A)**.

### Q43. Cubic Function Critical Points
- **Analysis**: $f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3) = 0 \implies x = 1, 3$.
  $f''(x) = 6x - 12$. At $x = 1$, $f''(1) = -6 < 0$ (local max).
  At $x = 3$, $f''(3) = +6 > 0$ (local min).
  At $x = 2$, $f''(2) = 0$ (inflection point).
- **Correct Options**: **(A, B, C, D)**.

### Q44. Rectangular Hyperbola Properties
- **Analysis**: All four statements correctly state geometry of rectangular hyperbolas.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Invertible Matrix Properties
- **Analysis**: Statements A, B, C, D are standard matrix identities.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Complex Number Modulus Properties
- **Analysis**: All four statements are standard complex algebra theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Exponential Inequality
- **Analysis**: $f'(x) = e^x - 1 = 0 \implies x = 0$. $f''(x) = e^x > 0$, so $x = 0$ is absolute global minimum.
  $f(0) = 0 \implies f(x) \ge 0 \implies e^x \ge 1 + x$.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Vector Algebra Theorems
- **Analysis**: All four statements correctly state vector identities.
- **Correct Options**: **(A, B, C, D)**.

### Q49–Q54 Numerical Solutions
- **Q49**: Standard limit $\lim_{x\to 0} \frac{\ln(1 + x)}{x} = 1$. **Answer: 1**.
- **Q50**: $\sin x = 0$ in $[0, 2\pi]$ has solutions $x = 0, \pi, 2\pi$. Total solutions $= 3$. **Answer: 3**.
- **Q51**: Tangent slope $y' = 2x$. At $(1, 1)$, tangent slope is 2. Normal slope $= -1/2 = -0.5$. **Answer: -0.5**.
- **Q52**: $\int_0^2 (3x^2 - 2x + 1)\,dx = [x^3 - x^2 + x]_0^2 = 8 - 4 + 2 = 6$. **Answer: 6**.
- **Q53**: Distance $d = \frac{|0 + 0 + 0 - 9|}{\sqrt{1^2 + 2^2 + 2^2}} = \frac{9}{\sqrt{9}} = 3$. **Answer: 3**.
- **Q54**: Diagonal matrix determinant is product of diagonal elements: $1 \times 2 \times 3 = 6$. **Answer: 6**.
