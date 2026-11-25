# Detailed Solutions and Pedagogical Analysis — Mock Examination 15 (Paper 2)
### Organising Institute Style: IIT Madras (`IIT_MADRAS_STYLE` — 2017 Benchmark)

---

## PART I: PHYSICS

### Q1. Non-Uniform Spherical Charge Distribution
- **Analysis**:
  - $Q = \int_0^R \rho_0 (1 - r/R) 4\pi r^2\,dr = 4\pi \rho_0 [r^3/3 - r^4/(4R)]_0^R = 4\pi \rho_0 R^3 (1/3 - 1/4) = \frac{\pi \rho_0 R^3}{3}$. (A is True)
  - Inside: $q(r) = 4\pi \rho_0 [r^3/3 - r^4/(4R)]$.
    $E(r) = \frac{q(r)}{4\pi\varepsilon_0 r^2} = \frac{\rho_0 r}{\varepsilon_0}\left(\frac{1}{3} - \frac{r}{4R}\right)$. (B is True)
  - To maximize $E(r)$: $\frac{d}{dr}[r/3 - r^2/(4R)] = 1/3 - 2r/(4R) = 0 \implies r = \frac{2}{3} R$. (C is True)
  - Potential at center: $V(0) = \frac{Q}{4\pi\varepsilon_0 R} + \int_0^R E(r)\,dr$.
    $\int_0^R E(r)\,dr = \frac{\rho_0}{\varepsilon_0} [r^2/6 - r^3/(12R)]_0^R = \frac{\rho_0 R^2}{\varepsilon_0}(1/6 - 1/12) = \frac{\rho_0 R^2}{12\varepsilon_0}$.
    $\frac{Q}{4\pi\varepsilon_0 R} = \frac{\pi \rho_0 R^3 / 3}{4\pi\varepsilon_0 R} = \frac{\rho_0 R^2}{12\varepsilon_0}$.
    $V(0) = \frac{\rho_0 R^2}{12\varepsilon_0} + \frac{\rho_0 R^2}{12\varepsilon_0} = \frac{\rho_0 R^2}{6\varepsilon_0} = \frac{4\rho_0 R^2}{24\varepsilon_0}$. (Option D states $5\rho_0 R^2 / 24\varepsilon_0$, so D is False).
- **Correct Options**: **(A, B, C)**.

### Q2. Rectangular Loop in Non-Uniform B Field
- **Analysis**:
  - Flux: $\Phi = \int_0^a B_0 (x/a)^2 (b\,dx) = \frac{B_0 b}{a^2} [x^3/3]_0^a = \frac{1}{3} B_0 a b$. (A is True)
  - $\mathcal{E} = \frac{d\Phi}{dt} = \frac{1}{3} a b \frac{dB_0}{dt} = \frac{1}{3} \alpha a b$. (B is True)
  - By Lenz's law, flux into the page (+z) is increasing, so induced field is out of page (-z) $\implies$ counter-clockwise! So (C) is False.
  - Current is uniform in loop, but magnetic field is non-uniform ($B(x) \propto x^2$). The force on left wire ($x = 0$) is zero, force on right wire ($x = a$) is non-zero, so net magnetic force is non-zero. (D is True)
- **Correct Options**: **(A, B, D)**.

### Q3. LC Oscillations
- **Analysis**: Standard $LC$ oscillation equations. All four statements are correct.
- **Correct Options**: **(A, B, C, D)**.

### Q4. Optical Fiber Total Internal Reflection
- **Analysis**:
  - $\sin\theta_c = \mu_2 / \mu_1 = 1.40 / 1.50 = 14/15$. (A is True)
  - $\text{NA} = \sqrt{1.5^2 - 1.4^2} = \sqrt{2.25 - 1.96} = \sqrt{0.29} \approx 0.539$. (B is True)
  - Acceptance angle $\sin\alpha_{\max} = \text{NA}$. (C is True)
  - TIR occurs only from denser to rarer. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q5. Electron Microscope
- **Analysis**:
  - $\lambda = h / p = h / \sqrt{2m_e e V}$. (A is True)
  - For $V = 100\text{ V}$, $\lambda = 12.27 / \sqrt{100} = 1.23\text{ \AA}$. (B is True)
  - Resolving power $\propto 1/\lambda$. (C is True)
  - Higher $V \implies$ smaller $\lambda \implies$ higher resolving power. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q6. Thermodynamic Cycle
- **Analysis**:
  - Cyclic $\implies \Delta U = 0$. (A is True)
  - Isochoric $\implies W = 0$. (B is True)
  - Adiabatic $\implies Q = 0 \implies W = -\Delta U$. (C is True)
  - Clockwise cycle $\implies W_{\text{net}} > 0 \implies Q_{\text{net}} > 0$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q7. Cyclotron Radius
- **Derivation**:
  $$r = \frac{m v}{q B} = \frac{1.0 \times 10^{-12} \times 2.0 \times 10^5}{1.0 \times 10^{-6} \times 0.50} = \frac{2.0 \times 10^{-7}}{0.50 \times 10^{-6}} = 0.40\text{ m}$$
- **Answer**: **0.4** (or **0.40**).

### Q8. Displacement Current Density
- **Derivation**:
  - Total displacement current between plates equals conduction current: $I_d = I = 2.0\text{ A}$.
  - Plate area $A = \pi R^2 = 3.14 \times (0.10)^2 = 0.0314\text{ m}^2$.
  - $J_d = \frac{I_d}{A} = \frac{2.0}{0.0314} \approx 63.7\text{ A/m}^2$.
- **Answer**: **63.7**.

### Q9. Interference Maxima on Enclosing Sphere
- **Derivation**:
  - Distance $d = 2.0\,\mu\text{m} = 2000\text{ nm} = 4\lambda$.
  - Maxima condition along line connecting sources: $\Delta x = d \cos\theta = m \lambda \implies \cos\theta = \frac{m \lambda}{d} = \frac{m}{4}$.
  - Possible values of $m$: $-4, -3, -2, -1, 0, 1, 2, 3, 4$ (9 values).
  - For $m = \pm 4$, $\theta = 0, \pi$ (each gives 1 point on the sphere: 2 points).
  - For $m = -3, -2, -1, 0, 1, 2, 3$ (7 values), each gives a circular ring of maxima on the sphere.
  - Number of circular rings $= 7$.
  - Total number of maxima rings/points on sphere $= 7$ rings $+ 2$ pole points $= 9$ sets of maxima.
  - Enter: 9.
- **Answer**: **9** (or **7** rings). Let's state 9.

### Q10. Undecayed Fraction
- **Derivation**:
  - Number of half-lives $n = 25.0 / 5.0 = 5$.
  - Fraction remaining: $(1/2)^5 = 1/32 \implies k = 32$.
- **Answer**: **32**.

### Q11. Telescope Magnification
- **Derivation**:
  $$M = \frac{f_o}{f_e} = \frac{100}{5.0} = 20$$
- **Answer**: **20**.

### Q12. Time to Heat Water
- **Derivation**:
  - Heat required $Q = m c \Delta T = 1.0 \times 4200 \times (100 - 20) = 4200 \times 80 = 336000\text{ J}$.
  - Electric power $P = \frac{V^2}{R} = \frac{200^2}{20} = \frac{40000}{20} = 2000\text{ W}$.
  - Time $t = \frac{Q}{P} = \frac{336000}{2000} = 168\text{ s}$.
- **Answer**: **168**.

### Q13. Ampere's Law Circulation
- **Derivation**: $\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enc}} = \mu_0 I \implies k = 1$.
- **Answer**: **1**.

### Q14. Nodes in Fundamental Mode
- **Derivation**: Fundamental mode on fixed string has 1 antinode and 2 nodes (at the boundaries).
- **Answer**: **2**.

### Q15. Neutrons in U-235
- **Derivation**: $N = A - Z = 235 - 92 = 143$.
- **Answer**: **143**.

### Q16. Ratio of RMS Speeds
- **Derivation**:
  $$v_{\text{rms}} = \sqrt{\frac{3RT}{M}} \implies \frac{v_{\text{H}_2}}{v_{\text{O}_2}} = \sqrt{\frac{M_{\text{O}_2}}{M_{\text{H}_2}}} = \sqrt{\frac{32}{2}} = \sqrt{16} = 4$$
- **Answer**: **4**.

### Q17. Period of Parallel Springs
- **Derivation**:
  - Parallel springs have equivalent constant $k_{\text{eq}} = 2k$.
  - $T' = 2\pi \sqrt{\frac{m}{2k}} = \frac{T}{\sqrt{2}} = \frac{2}{\sqrt{2}} \implies k = 2$.
- **Answer**: **2**.

### Q18. Electrons in 3d Subshell
- **Derivation**: For $d$-subshell ($l = 2$), $2(2l + 1) = 2(5) = 10$ electrons.
- **Answer**: **10**.

---

## PART II: CHEMISTRY

### Q19. Leclanché Dry Cell Reactions
- **Analysis**:
  - Anodic oxidation of zinc container. (A is True)
  - Cathode is carbon rod surrounded by $\text{MnO}_2$. (B is True)
  - Reduction of $\text{MnO}_2$ to $\text{MnO(OH)}$. (C is True)
  - $\text{Zn}^{2+}$ complexes with $\text{NH}_3$ to form $[\text{Zn}(\text{NH}_3)_4]^{2+}$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q20. Fe(III) Complexes Comparison
- **Analysis**:
  - $[\text{Fe}(\text{CN})_6]^{3-}$: $\text{CN}^-$ is strong field $\implies t_{2g}^5 e_g^0$, low-spin, $d^2sp^3$, 1 unpaired electron ($\mu = \sqrt{3} \approx 1.73\text{ BM}$). (A, B are True)
  - $[\text{Fe}(\text{H}_2\text{O})_6]^{3+}$: $\text{H}_2\text{O}$ is weak field $\implies t_{2g}^3 e_g^2$, high-spin, $sp^3d^2$, 5 unpaired electrons ($\mu = \sqrt{35} \approx 5.92\text{ BM}$). (C, D are True)
- **Correct Options**: **(A, B, C, D)**.

### Q21. Halogen Group Trends
- **Analysis**: All four statements correctly state periodic properties and anomalies of halogens.
- **Correct Options**: **(A, B, C, D)**.

### Q22. Acyl Derivative Reactivity
- **Analysis**: Acyl chloride $>$ anhydride $>$ ester $>$ amide; leaving group ability; tetrahedral intermediate; amide hydrolysis severity.
- **Correct Options**: **(A, B, C, D)**.

### Q23. Hall-Héroult Aluminum Extraction
- **Analysis**: Cryolite and fluorspar roles, electrode materials, anode carbon consumption.
- **Correct Options**: **(A, B, C, D)**.

### Q24. Adsorption Isotherm Fundamentals
- **Analysis**: Freundlich and Langmuir models and their logarithmic and limiting behaviors.
- **Correct Options**: **(A, B, C, D)**.

### Q25. Equilibrium Constant of Daniell Cell
- **Derivation**:
  $$\log_{10} K_c = \frac{n E^\circ}{0.0591} = \frac{2 \times 1.10}{0.0591} = \frac{2.20}{0.0591} \approx 37.22 \approx 37$$
  $$x = 37$$
- **Answer**: **37**.

### Q26. pH of Sulfuric Acid
- **Derivation**:
  - $[	ext{H}^+] = 2 	imes 0.0050 = 0.010	ext{ M} = 10^{-2}	ext{ M}$.
  - $	ext{pH} = -\log_{10}(10^{-2}) = 2.0$.
- **Answer**: **2** (or **2.0**).

### Q27. Partial Pressure in Gaseous Reaction
- **Derivation**:
  - Reaction: $A(g) ightarrow 2B(g) + C(g)$.
  - Initially: $P_A = P_0 = 100	ext{ mm Hg}, P_B = 0, P_C = 0$.
  - At $t$: $P_A = 100 - x, P_B = 2x, P_C = x$.
  - Total pressure: $P_{	ext{tot}} = (100 - x) + 2x + x = 100 + 2x = 200 \implies 2x = 100 \implies x = 50	ext{ mm Hg}$.
  - Partial pressure of $A$: $P_A = 100 - 50 = 50	ext{ mm Hg}$.
- **Answer**: **50**.

### Q28. van 't Hoff Factor
- **Derivation**:
  $$\Delta T_f = i K_f m \implies 0.3534 = i 	imes 1.86 	imes 0.10 = i 	imes 0.186 \implies i = rac{0.3534}{0.186} = 1.90$$
- **Answer**: **1.90** (or **1.9**).

### Q29. Enthalpy of Carbon Monoxide Formation
- **Derivation**:
  $$\Delta H^\circ = 2\Delta H_f^\circ(	ext{CO}) - \Delta H_f^\circ(	ext{CO}_2) = 2(-110.5) - (-393.5) = -221.0 + 393.5 = +172.5	ext{ kJ}$$
- **Answer**: **172.5**.

### Q30. Degree of Dissociation of HCOOH
- **Derivation**:
  $$lpha = rac{\Lambda_m}{\Lambda_m^\circ} = rac{46.1}{405.0} pprox 0.1138 = 11.4\%$$
- **Answer**: **11.4**.

### Q31. Oxidation State of P in H3PO4
- **Derivation**: $3(+1) + x + 4(-2) = 0 \implies x - 5 = 0 \implies x = +5$.
- **Answer**: **5**.

### Q32. Bridging Carbonyls in Co2(CO)8
- **Derivation**: In solid state, $	ext{Co}_2(	ext{CO})_8$ has 2 bridging carbonyls and 6 terminal carbonyls.
- **Answer**: **2**.

### Q33. Basicity of Phosphorous Acid
- **Derivation**: $	ext{H}_3	ext{PO}_3$ has structure $	ext{HPO(OH)}_2$ with 2 ionizable $-	ext{OH}$ groups $\implies$ basicity = 2.
- **Answer**: **2**.

### Q34. Coordination Number in Tetrahedral Void
- **Derivation**: A tetrahedral void is enclosed by 4 spheres $\implies$ coordination number = 4.
- **Answer**: **4**.

### Q35. Chiral Centers in D-Glucose
- **Derivation**: Open-chain D-glucose has 4 chiral carbons (C2, C3, C4, C5).
- **Answer**: **4**.

### Q36. Pi Bonds in Ethyne
- **Derivation**: $	ext{H}-	ext{C}\equiv	ext{C}-	ext{H}$ contains 1 triple bond, which consists of 1 $\sigma$-bond and 2 $\pi$-bonds.
- **Answer**: **2**.

---

## PART III: MATHEMATICS

### Q37. Properties of f(x) = ln(x)/x
- **Analysis**:
  - $f'(x) = rac{1 - \ln x}{x^2} = 0 \implies x = e$. Max value $1/e$. (A, B are True)
  - $f(e) > f(\pi) \implies rac{\ln e}{e} > rac{\ln\pi}{\pi} \implies \pi \ln e > e \ln\pi \implies \ln(e^\pi) > \ln(\pi^e) \implies e^\pi > \pi^e$. (C is True)
  - $f''(x) = rac{-x - 2x(1 - \ln x)}{x^4} = rac{2\ln x - 3}{x^3} = 0 \implies \ln x = 3/2 \implies x = e^{3/2}$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q38. Rectangular Hyperbola x^2 - y^2 = a^2
- **Analysis**:
  - $e = \sqrt{1 + b^2/a^2} = \sqrt{1 + 1} = \sqrt{2}$. (A is True)
  - Asymptotes $y = \pm x$ are perpendicular. (B is True)
  - Latus rectum $2b^2/a = 2a^2/a = 2a$. (C is True)
  - Area of triangle formed by any tangent with asymptotes is $ab = a^2$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q39. Invertible Matrix Properties
- **Analysis**: All four matrix identities are standard linear algebra theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q40. Definite Integral Analysis
- **Analysis**:
  - Let $x = 	an	heta \implies dx = \sec^2	heta\,d	heta$.
    $I = \int_0^{\pi/4} \ln(1 + 	an	heta)\,d	heta$. (A is True)
  - By King's property: $\int_0^{\pi/4} \ln\left(1 + 	an(\pi/4 - 	heta)ight)\,d	heta = \int_0^{\pi/4} \ln\left(rac{2}{1 + 	an	heta}ight)\,d	heta = rac{\pi}{4}\ln 2 - I \implies 2I = rac{\pi}{4}\ln 2 \implies I = rac{\pi}{8}\ln 2$. (B, C are True)
  - Integrand is strictly positive on $(0, 1) \implies I > 0$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q41. Probability Theorems
- **Analysis**: All four statements correctly state theorems of axiomatic probability.
- **Correct Options**: **(A, B, C, D)**.

### Q42. Orthonormal Vector Basis
- **Analysis**: Properties of an orthonormal triad in $\mathbb{R}^3$.
- **Correct Options**: **(A, B, C, D)**.

### Q43. Symmetric Integral
- **Derivation**:
  - $x^3$ and $\sin x$ are odd functions, so their integrals over $[-2, 2]$ vanish.
  - $I = \int_{-2}^2 x^2\,dx = 2 \left[rac{x^3}{3}ight]_0^2 = 2 	imes rac{8}{3} = rac{16}{3} pprox 5.33$.
- **Answer**: **5.33**.

### Q44. Maximum Value of sin(x)cos(x)
- **Derivation**:
  $$\sin x \cos x = rac{1}{2}\sin 2x \le rac{1}{2} = 0.5$$
- **Answer**: **0.5**.

### Q45. Distance from Point to z-Axis
- **Derivation**:
  $$d = \sqrt{x^2 + y^2} = \sqrt{2^2 + 3^2} = \sqrt{4 + 9} = \sqrt{13} pprox 3.61$$
- **Answer**: **3.61**.

### Q46. Latus Rectum of Ellipse
- **Derivation**:
  - Standard form: $rac{x^2}{16} + rac{y^2}{25} = 1$.
  - Major axis along y-axis with $a = 5$, minor axis with $b = 4$.
  - Latus rectum $= rac{2b^2}{a} = rac{2(16)}{5} = rac{32}{5} = 6.40$.
- **Answer**: **6.40** (or **6.4**).

### Q47. Sum of Infinite GP
- **Derivation**:
  $$a = 9, r = 1/3 \implies S = rac{a}{1 - r} = rac{9}{1 - 1/3} = rac{9}{2/3} = 13.5$$
- **Answer**: **13.5**.

### Q48. Orthogonal Vectors
- **Derivation**:
  $$ec{a} \cdot ec{b} = 2(1) + \lambda(-2) + 1(3) = 2 - 2\lambda + 3 = 5 - 2\lambda = 0 \implies \lambda = 2.5$$
- **Answer**: **2.5**.

### Q49. Circular Permutations
- **Derivation**: $(n - 1)! = (5 - 1)! = 4! = 24$.
- **Answer**: **24**.

### Q50. Order of Differential Equation
- **Derivation**: Highest order derivative present is $rac{d^2 y}{dx^2} \implies$ order is 2.
- **Answer**: **2**.

### Q51. Standard Exponential Limit
- **Derivation**: $\lim_{x 	o 0} rac{e^{2x} - 1}{x} = 2$.
- **Answer**: **2**.

### Q52. Real Solutions of cos(x) = 2
- **Derivation**: Range of $\cos x$ is $[-1, 1]$. Since $2 
otin [-1, 1]$, there are 0 real solutions.
- **Answer**: **0**.

### Q53. Diameter of Circle
- **Derivation**:
  - Center is $(2, 3)$, $c = -12$.
  - $R = \sqrt{2^2 + 3^2 - (-12)} = \sqrt{4 + 9 + 12} = \sqrt{25} = 5$.
  - Diameter $= 2R = 10$.
- **Answer**: **10**.

### Q54. Product of Roots
- **Derivation**: For $x^2 - 7x + 12 = 0$, product of roots is $c/a = 12/1 = 12$.
- **Answer**: **12**.
