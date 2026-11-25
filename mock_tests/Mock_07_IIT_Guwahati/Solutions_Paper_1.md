# Detailed Solutions and Pedagogical Analysis — Mock Examination 07 (Paper 1)
### Organising Institute Style: IIT Guwahati (`IIT_GUWAHATI_STYLE`)

---

## PART I: PHYSICS

### Q1. Earthed Concentric Conducting Shells
- **First Observation & Concept**: Electrostatic potential of concentric conducting shells upon earthing.
- **Key Insight**: Earthing the inner shell forces its electric potential to zero: $V_{\text{inner}} = 0$.
- **Derivation**: Let charge on inner shell be $q$. Charge on outer shell is $-2Q$.
  $$V_{\text{inner}} = \frac{1}{4\pi\varepsilon_0}\left(\frac{q}{R} + \frac{-2Q}{2R}\right) = 0 \implies \frac{q}{R} - \frac{Q}{R} = 0 \implies q = +Q$$
- **Correct Option**: **(A)**.
- **Common Trap**: Assuming that earthing removes all charge on the inner shell ($q = 0$, option B). Earthing sets potential to zero, not net charge!

### Q2. Polytropic Gas Molar Heat Capacity
- **First Observation & Concept**: Polytropic process $P V^n = \text{const}$ with $n = 2$.
- **Key Insight**: For a polytropic process of an ideal gas, molar heat capacity is $C = C_v + \frac{R}{1 - n}$.
- **Derivation**: For monoatomic gas, $C_v = \frac{3}{2}R$. With $n = 2$:
  $$C = \frac{3}{2}R + \frac{R}{1 - 2} = \frac{3}{2}R - R = \frac{R}{2}$$
- **Correct Option**: **(A)**.

### Q3. Moment of Inertia of Square Plate via Symmetry
- **First Observation & Concept**: Symmetry invariants and perpendicular axis theorem in 2D plates.
- **Key Insight**: By perpendicular axis theorem, $I_z = I_x + I_y = \frac{1}{12} M a^2 + \frac{1}{12} M a^2 = \frac{1}{6} M a^2$.
- **Derivation**: For any two mutually perpendicular axes in the plane of a 4-fold symmetric square plate, $I_1 + I_2 = I_z$. By 4-fold symmetry, $I_1 = I_2 = I_z / 2 = \frac{1}{12} M a^2$ independent of $\theta$!
- **Correct Option**: **(A)**.

### Q4. Grating Principal Maxima Count
- **First Observation & Concept**: Grating equation $d \sin\theta = m \lambda$.
- **Key Insight**: Grating spacing $d = \frac{1\text{ mm}}{500} = 2.0\times 10^{-6}\text{ m} = 2000\text{ nm}$.
- **Derivation**: Maximum possible order satisfies $\sin\theta \le 1$:
  $$m \le \frac{d}{\lambda} = \frac{2000\text{ nm}}{500\text{ nm}} = 4.0$$
  Possible orders are $m = 0, \pm 1, \pm 2, \pm 3, \pm 4$. However, $m = 4$ corresponds to $\sin\theta = 1$ (glancing along screen plane, usually not collected or on boundary). If collected, total $= 2(4) + 1 = 9$. If $m=4$ is at $90^\circ$, physically $m \in \{-4, \dots, +4\}$, total $= 9$. (If boundary excluded, 7). Here 9 is standard.
- **Correct Option**: **(C)**.

### Q5. Hydrogen-like Bohr Transition
- **First Observation & Concept**: Bohr formula $\Delta E = 13.6 Z^2 \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$.
- **Key Insight**: $\Delta E = 13.6 Z^2 \left(\frac{1}{4} - \frac{1}{9}\right) = 13.6 Z^2 \left(\frac{5}{36}\right) = 40.8\text{ eV}$.
- **Derivation**:
  $$\frac{40.8}{13.6} = 3 \implies Z^2 \left(\frac{5}{36}\right) = 3 \implies Z^2 = \frac{108}{5} = 21.6$$
  Wait, for $n=3 \to n=2$ if $\Delta E = 13.6 Z^2 (5/36)$. If $\text{He}^+$, $Z=2 \implies \Delta E = 13.6 \times 4 \times (5/36) = 7.56\text{ eV}$. If $n=2 \to n=1$, $\Delta E = 13.6 Z^2 (3/4) = 10.2 Z^2 = 40.8 \implies Z^2 = 4 \implies Z = 2$.
  In the question text, with $Z=2$, $n=2 \to n=1$ yields $40.8\text{ eV}$. If $Z=2$:
- **Correct Option**: **(A)**.

### Q6. Poiseuille's Flow Formula
- **First Observation & Concept**: Poiseuille's formula $Q = \frac{\pi r^4 \Delta P}{8 \eta L}$.
- **Key Insight**: Flow rate is proportional to $r^4 \Delta P$.
- **Derivation**: $Q' \propto (r/2)^4 (2\Delta P) = \frac{r^4}{16} \times 2 \Delta P = \frac{1}{8} Q$.
- **Correct Option**: **(A)**.

### Q7. End Impulse on Free Rod
- **Analysis**:
  - Linear momentum: $J = m v_{cm} \implies v_{cm} = J/m$. (A is correct).
  - Angular momentum about CM: $J(L/2) = I_{cm} \omega = (\frac{1}{12} m L^2)\omega \implies \omega = \frac{6J}{mL}$. (B is correct).
  - Velocity of a point at distance $x$ from CM towards $B$: $v(x) = v_{cm} - \omega x = \frac{J}{m} - \frac{6J}{mL} x = 0 \implies x = L/6$. (C is correct).
  - Kinetic energy: $K = \frac{1}{2} m v_{cm}^2 + \frac{1}{2} I \omega^2 = \frac{1}{2} m (J/m)^2 + \frac{1}{2} (\frac{1}{12} m L^2)(36 J^2 / m^2 L^2) = \frac{J^2}{2m} + \frac{3J^2}{2m} = \frac{2J^2}{m}$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q8. SHM Energy and Dynamics
- **Analysis**:
  - $U = \frac{1}{2} k x^2 = \frac{1}{2} k (A^2/2) = \frac{1}{4} k A^2$. Total energy $E = \frac{1}{2} k A^2$.
    $K = E - U = \frac{1}{4} k A^2 = U$. (A is correct).
  - Acceleration $a = \omega^2 x = (k/m)(A/\sqrt{2}) = \frac{k A}{\sqrt{2} m}$. (B is correct).
  - $v = \omega \sqrt{A^2 - x^2} = \sqrt{k/m} \sqrt{A^2 - A^2/2} = A\sqrt{k/(2m)}$. (C is correct).
  - Work by restoring force from $x$ to $0$: $W = -\Delta U = U(x) - U(0) = \frac{1}{4} k A^2$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q9. Stefan-Boltzmann and Wien's Law
- **Analysis**:
  - $P = \sigma (4\pi R^2) T^4$.
    $P_2 / P_1 = (R_2/R_1)^2 (T_2/T_1)^4 = (2)^2 (1/2)^4 = 4 \times (1/16) = 1/4$. (A is correct).
  - Wien's law: $\lambda_{\max} T = \text{const} \implies \lambda_{\max, 2} / \lambda_{\max, 1} = T_1 / T_2 = 2$. (B is correct).
  - Emissive power $E = \sigma T^4 \implies E_2 / E_1 = (1/2)^4 = 1/16$. (C is correct).
  - Rate of heat loss per unit area is emissive power, which is $1/16$ (not $1/8$). (D is incorrect).
- **Correct Options**: **(A, B, C)**.

### Q10. Classical EM Wave Properties
- **Analysis**: All statements A, B, C, D are textbook properties of a linearly polarized plane wave in vacuum.
- **Correct Options**: **(A, B, C, D)**.

### Q11. Successive Radioactive Decay
- **Analysis**: Bateman equations confirm maximum at $t_{\max} = \frac{\ln(\lambda_1/\lambda_2)}{\lambda_1 - \lambda_2}$, secular equilibrium condition, and particle conservation.
- **Correct Options**: **(A, B, C, D)**.

### Q12. Moving Loop in Magnetic Field
- **Analysis**:
  - Induced EMF $\mathcal{E} = B a v$, current $I = B a v / R$.
  - Magnetic retarding force $F = I a B = \frac{B^2 a^2 v}{R}$. External force must match it. (A is correct).
  - Mechanical power $P = F v = \frac{B^2 a^2 v^2}{R} = I^2 R$. (B is correct).
  - Total heat $H = P \times (b/v) = \frac{B^2 a^2 b v}{R}$. (C is correct).
  - Lenz's law dictates current direction opposes withdrawal. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q13–Q18 Numerical Solutions
- **Q13**: $\eta = 1 - \frac{T_C}{T_H} = 1 - \frac{300}{600} = 0.50$.
  $W = \eta Q_H = 0.50 \times 1200 = 600\text{ J}$. **Answer: 600**.
- **Q14**: Bragg's law: $\lambda = 2 d \sin\theta = 2(0.091)(0.906) = 0.16489 \approx 0.16\text{ nm}$. **Answer: 0.16**.
- **Q15**: Each semicircle has area $A_1 = \frac{1}{2}\pi R^2 = \frac{1}{2}(3.14)(0.25) = 0.3925\text{ m}^2$.
  Magnetic moment vectors: $\vec{M}_1 = I A_1 \hat{i}$, $\vec{M}_2 = I A_1 \hat{k}$.
  $$|\vec{M}| = \sqrt{M_1^2 + M_2^2} = \sqrt{2} I A_1 = 1.414 \times 2.0 \times 0.3925 \approx 1.11\text{ A}\cdot\text{m}^2$$
  **Answer: 1.11**.
- **Q16**: By Gauss's law for $r \le R$:
  $$q(r) = 4\pi \rho_0 \int_0^r (r'^2 - r'^3/R)\,dr' = 4\pi \rho_0 \left(\frac{r^3}{3} - \frac{r^4}{4R}\right)$$
  $$E(r) = \frac{\rho_0}{\varepsilon_0}\left(\frac{r}{3} - \frac{r^2}{4R}\right)$$
  To maximize $E(r)$: $\frac{dE}{dr} = \frac{\rho_0}{\varepsilon_0}\left(\frac{1}{3} - \frac{2r}{4R}\right) = 0 \implies \frac{r}{2R} = \frac{1}{3} \implies r_m = \frac{2}{3}R = \frac{2}{3}(10) \approx 6.67\text{ cm}$. **Answer: 6.67**.
- **Q17**: For 1D elastic collision with $M_2$ initially at rest:
  $$v_2 = \frac{2 M_1}{M_1 + M_2} v = \frac{2(4)}{4 + 1}(10) = \frac{8}{5}(10) = 16\text{ m/s}$$
  $$K_2 = \frac{1}{2} M_2 v_2^2 = \frac{1}{2}(1)(16)^2 = 128\text{ J}$$
  **Answer: 128**.
- **Q18**: Lens maker's formula in air: $\frac{1}{f_a} = (1.5 - 1)\left(\frac{1}{20} - \frac{1}{-30}\right) = 0.5 \left(\frac{5}{60}\right) = \frac{1}{24} \implies f_a = 24\text{ cm}$.
  In water: $\frac{1}{f_w} = \left(\frac{1.5}{4/3} - 1\right)\left(\frac{5}{60}\right) = \left(\frac{9}{8} - 1\right)\left(\frac{1}{12}\right) = \frac{1}{8} \times \frac{1}{12} = \frac{1}{96} \implies f_w = 96\text{ cm}$. **Answer: 96**.

---

## PART II: CHEMISTRY

### Q19. Closest Approach in FCC Lattice
- **Calculation**: In FCC, atoms touch along the face diagonal: $4r = a\sqrt{2}$. Closest approach distance $d = 2r = \frac{a}{\sqrt{2}} = \frac{400}{1.414} \approx 282.8\text{ pm}$.
- **Correct Option**: **(B)**.

### Q20. Endothermic Dissociation & Temperature
- **Chemistry**: Van 't Hoff: $\frac{d\ln K_p}{dT} = \frac{\Delta H^\circ}{R T^2} > 0$. An increase in temperature increases $K_p$.
- **Correct Option**: **(A)**.

### Q21. Crystal Field Stabilization Energy
- **Analysis**:
  - $[\text{Co}(\text{CN})_6]^{3-}$: $\text{Co}^{3+}$ ($d^6$) low-spin with strong field $\text{CN}^- \implies t_{2g}^6 e_g^0$.
  - $\text{CFSE} = 6 \times (-0.4\Delta_o) = -2.4\Delta_o$. This is the maximum CFSE possible in octahedral geometry.
- **Correct Option**: **(D)**.

### Q22. Stereospecific Debromination
- **Analysis**: Debromination with Zn is an anti-periplanar elimination ($E2$). For $(2R, 3S)$-2,3-dibromobutane (meso isomer), rotating to anti-periplanar conformation places the two methyl groups trans to each other, yielding $(E)$-but-2-ene.
- **Correct Option**: **(A)**.

### Q23. Redox Spontaneity of $\text{Fe}^{3+}$ and $\text{I}^-$
- **Analysis**: $E^\circ_{\text{cell}} = E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) - E^\circ(\text{I}_2/\text{I}^-) = 0.77 - 0.54 = +0.23\text{ V} > 0$. Spontaneous oxidation of iodide to iodine.
- **Correct Option**: **(A)**.

### Q24. Anomalous Radius of Gallium
- **Fact**: Due to poor shielding by the intervening 10 $3d$ electrons (d-block contraction), atomic radius of $\text{Ga} (135\text{ pm})$ is slightly smaller than that of $\text{Al} (143\text{ pm})$. Hence $\text{Al} > \text{Ga}$, making (D) false.
- **Correct Option**: **(D)**.

### Q25. Reversible Adiabatic Thermodynamics
- **Analysis**: Reversible adiabatic $\implies dQ_{\text{rev}} = 0 \implies dS = 0$ for both system and surroundings (isentropic). Gas does expansion work at the expense of internal energy, so $T$ decreases.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Intramolecular Aldol Ring Size
- **Analysis**:
  - Hexane-2,5-dione: forms 5-membered 3-methylcyclopent-2-en-1-one. (A is correct).
  - Heptane-2,6-dione: forms 6-membered 3-methylcyclohex-2-en-1-one. (B is correct).
  - Pentanedial: forms cyclopent-1-enecarbaldehyde (5-membered). (C is correct).
  - Butanedial: would form a strained 4-membered ring, so it does not condense cleanly. (D is incorrect).
- **Correct Options**: **(A, B, C)**.

### Q27. Square Planar Complex $[Mabcd]$
- **Analysis**: Standard textbook case $[\text{Pt}(\text{NH}_3)(\text{py})(\text{Cl})(\text{Br})]$ has 3 geometrical isomers. None is optically active because the molecular plane is a plane of symmetry.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Phosphorus Oxoacids
- **Analysis**: All four statements correctly state classical inorganic structure and oxidation states of phosphorus oxoacids.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Thermodynamics of Daniell Cell
- **Analysis**: $\Delta G^\circ = -n F E^\circ = -2 \times 96500 \times 1.10 = -212300\text{ J} = -212.3\text{ kJ}$. All statements are correct.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Darzens Reaction of Alcohols with Thionyl Chloride
- **Analysis**: Without pyridine: $S_N i$ mechanism with retention of configuration. With pyridine: pyridinium chloride generates chloride ion which attacks from back side ($S_N 2$) with inversion.
- **Correct Options**: **(A, B, C, D)**.

### Q31–Q36 Numerical Solutions
- **Q31**: FCC packing efficiency $= \frac{4 \times \frac{4}{3}\pi r^3}{(2\sqrt{2}r)^3} = \frac{\pi}{3\sqrt{2}} \approx 0.7405 = 74.05\%$. **Answer: 74.05**.
- **Q32**: $2\text{HI} \rightleftharpoons \text{H}_2 + \text{I}_2$.
  Initial $[	ext{HI}] = 2.0$. At equilibrium: $[	ext{HI}] = 2 - 2x$, $[	ext{H}_2] = [	ext{I}_2] = x$.
  $$K_c = \frac{x^2}{(2 - 2x)^2} = 0.02 \implies \frac{x}{2 - 2x} = \sqrt{0.02} \approx 0.1414$$
  $$x = 0.2828 - 0.2828 x \implies 1.2828 x = 0.2828 \implies x \approx 0.22\text{ M}$$
  **Answer: 0.22**.
- **Q33**: $t_{90\%} = \frac{\ln(1/0.10)}{k} = \frac{\ln 10}{\ln 2 / T_{1/2}} = 138.6 \times \frac{2.303}{0.693} = 138.6 \times 3.323 \approx 460.6 \approx 461\text{ days}$. **Answer: 461**.
- **Q34**: $\Delta T_f = i K_f m \implies 0.1116 = i (1.86)(0.05) = i (0.093) \implies i = \frac{0.1116}{0.093} = 1.20$. **Answer: 1.2 (or 1.20)**.
- **Q35**: $m = \frac{M I t}{n F} = \frac{63.5 \times 2.0 \times 965}{2 \times 96500} = \frac{63.5 \times 1930}{193000} = \frac{63.5}{100} = 0.635 \approx 0.64\text{ g}$. **Answer: 0.64**.
- **Q36**: Tartaric acid has 2 chiral centers with identical substituents: $d$-tartaric acid, $l$-tartaric acid, and meso-tartaric acid. Total stereoisomers $= 3$. **Answer: 3**.

---

## PART III: MATHEMATICS

### Q37. Integral Inequality with Exponential Denominator
- **Calculation**: $I = \int_{-\pi/2}^{\pi/2} \frac{\cos x}{1 + e^x}\,dx$.
  Using King's property ($x \to -x$):
  $$I = \int_{-\pi/2}^{\pi/2} \frac{\cos x}{1 + e^{-x}}\,dx = \int_{-\pi/2}^{\pi/2} \frac{e^x \cos x}{1 + e^x}\,dx$$
  $$2I = \int_{-\pi/2}^{\pi/2} \cos x\,dx = [\sin x]_{-\pi/2}^{\pi/2} = 1 - (-1) = 2 \implies I = 1$$
- **Correct Option**: **(B)**.

### Q38. Director Circle of Ellipse
- **Formula**: The locus of points of intersection of perpendicular tangents to an ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ is the director circle $x^2 + y^2 = a^2 + b^2$.
  Here $a^2 = 16, b^2 = 9 \implies x^2 + y^2 = 25$.
- **Correct Option**: **(B)**.

### Q39. Orthonormal Vector Decomposition
- **Calculation**: Since $\vec{u}, \vec{v}, \vec{w}$ form an orthonormal basis of $\mathbb{R}^3$:
  $$\vec{x} = (\vec{x}\cdot\vec{u})\vec{u} + (\vec{x}\cdot\vec{v})\vec{v} + (\vec{x}\cdot\vec{w})\vec{w} = 2\vec{u} + 3\vec{v} - 6\vec{w}$$
  $$|\vec{x}| = \sqrt{2^2 + 3^2 + (-6)^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$$
- **Correct Option**: **(B)**.

### Q40. Binomial Probability of Even Successes
- **Calculation**: $p = 1/6, q = 5/6$.
  $P(\text{even}) = \frac{1}{2}[(q + p)^n + (q - p)^n] = \frac{1}{2}\left(1 + (5/6 - 1/6)^6\right) = \frac{1}{2}\left(1 + (2/3)^6\right)$.
- **Correct Option**: **(A)**.

### Q41. Geometric Area of Sine Wave
- **Calculation**: Area $= \int_{0}^{2\pi} |\sin x|\,dx = 2 \int_{0}^{\pi} \sin x\,dx = 2 [-\cos x]_0^\pi = 2(2) = 4$.
- **Correct Option**: **(C)**.

### Q42. Homogeneous Differential Equation
- **Calculation**: Let $y = v x \implies v + x \frac{dv}{dx} = \frac{1 + v^2}{2v}$.
  $$x \frac{dv}{dx} = \frac{1 - v^2}{2v} \implies \frac{2v}{1 - v^2}\,dv = \frac{dx}{x} \implies -\ln|1 - v^2| = \ln|x| - \ln C$$
  $$\ln\left(\frac{1}{|1 - y^2/x^2|}\right) = \ln|x/C| \implies \frac{x^2}{|x^2 - y^2|} = \frac{|x|}{C} \implies |x^2 - y^2| = C |x|$$
- **Correct Option**: **(A)**.

### Q43. Piecewise Absolute Value Function
- **Analysis**:
  - $f(x)$ is continuous everywhere on $\mathbb{R}$ as the sum of continuous functions. (A is correct).
  - Differentiability fails at the transition corner points $x = 0, 1, 2$. (B is correct).
  - For $x < 0$, $f(x) = -3x + 3$. For $0 \le x \le 1$, $f(x) = -x + 3$. For $1 \le x \le 2$, $f(x) = x + 1$. For $x > 2$, $f(x) = 3x - 3$. Minimum occurs at $x = 1$, where $f(1) = 2$. (C and D correct).
- **Correct Options**: **(A, B, C, D)**.

### Q44. Geometric Invariants of Hyperbola
- **Analysis**: All four properties are fundamental geometric theorems for the general hyperbola.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Matrix Algebraic Identities
- **Analysis**: $A B - A - B + I = I \implies (A - I)(B - I) = I$.
  This implies $(A - I)$ is invertible, with inverse $(B - I)$.
  Since a matrix commutes with its inverse, $(B - I)(A - I) = I \implies B A - B - A + I = I \implies B A = A + B = A B$.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Complex Cube Roots and Equilateral Triangle
- **Analysis**: $z_1 = 2$. Vertices of an equilateral triangle inscribed in $|z| = 2$ are $2, 2\omega, 2\omega^2$.
  - Centroid $= (z_1 + z_2 + z_3)/3 = 0$. (A is correct).
  - $2\omega = 2(-1/2 + i\sqrt{3}/2) = -1 + i\sqrt{3}$. (B is correct).
  - Side length $= 2\sqrt{3}$. (C is correct).
  - $z_1^3 + z_2^3 + z_3^3 = 8 + 8 + 8 = 24$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q47. Calculus Analysis of $(\ln x)/x$
- **Analysis**: $f'(x) = \frac{1 - \ln x}{x^2} = 0 \implies x = e$. Absolute maximum is $f(e) = 1/e$.
  - Since $f(e) > f(\pi) \implies \frac{\ln e}{e} > \frac{\ln\pi}{\pi} \implies \pi \ln e > e \ln\pi \implies e^\pi > \pi^e$.
  - $f''(x) = \frac{2\ln x - 3}{x^3} = 0 \implies x = e^{3/2}$.
  - $\lim_{x\to\infty} \frac{\ln x}{x} = 0$.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Vector Identities
- **Analysis**: All four formulas are standard vector triple product identities.
- **Correct Options**: **(A, B, C, D)**.

### Q49–Q54 Numerical Solutions
- **Q49**: Using identity $\frac{1}{k+1}\binom{n}{k} = \frac{1}{n+1}\binom{n+1}{k+1}$:
  $$S = \frac{1}{11} \sum_{k=1}^{10} \binom{11}{k+1} = \frac{1}{11} [2^{11} - \binom{11}{0} - \binom{11}{1}] = \frac{1}{11}[2048 - 1 - 11] = \frac{2036}{11} \approx 185.09$$
  **Answer: 185.09**.
- **Q50**: $\sin 3x + \sin x = 2\sin 2x \cos x = \sin 2x \implies \sin 2x (2\cos x - 1) = 0$.
  - $\sin 2x = 0 \implies 2x = 0, \pi, 2\pi \implies x = 0, \pi/2, \pi$ (3 solutions).
  - $2\cos x - 1 = 0 \implies \cos x = 1/2 \implies x = \pi/3$ (1 solution).
  - Total distinct solutions in $[0, \pi] = 4$. **Answer: 4**.
- **Q51**: Sub-tangent length $= |y / y'|$.
  $y' = b e^{x/a} \cdot (1/a) = y / a$.
  Sub-tangent $= |y / (y/a)| = a$. The multiple of $a$ is 1. **Answer: 1**.
- **Q52**: $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$.
  $f(-2) = -8 + 6 + 1 = -1 < 0$.
  $f(-1) = -1 + 3 + 1 = 3 > 0$ (Root in $(-2, -1)$).
  $f(1) = 1 - 3 + 1 = -1 < 0$ (Root in $(-1, 1)$).
  $f(2) = 8 - 6 + 1 = 3 > 0$ (Root in $(1, 2)$).
  All 3 roots lie in $[-2, 2]$. **Answer: 3**.
- **Q53**: Parabola $y^2 = 4x$. At $(1, 2)$:
  Tangent: $y(2) = 2(x + 1) \implies y = x + 1$. X-intercept ($y=0$): $x_T = -1$.
  Slope of tangent is $1$, so slope of normal is $-1$.
  Normal: $y - 2 = -1(x - 1) \implies y = -x + 3$. X-intercept ($y=0$): $x_N = 3$.
  Base of triangle on x-axis $= |x_N - x_T| = 3 - (-1) = 4$.
  Height $= y$-coordinate of point of intersection $= 2$.
  $$\text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 4 \times 2 = 4$$
  **Answer: 4**.
- **Q54**: Vandermonde determinant $D = (b - a)(c - a)(c - b) = (3 - 1)(6 - 1)(6 - 3) = 2 \times 5 \times 3 = 30$. **Answer: 30**.
