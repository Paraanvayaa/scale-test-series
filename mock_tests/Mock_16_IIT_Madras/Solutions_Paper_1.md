# Detailed Solutions and Pedagogical Analysis — Mock Examination 16 (Paper 1)
### Organising Institute Style: IIT Madras (`IIT_MADRAS_STYLE` — 2010 Benchmark)

---

## PART I: PHYSICS

### Q1. Dielectric Coated Charged Sphere
- **First Observation & Concept**: Gauss's law with concentric dielectric shell.
- **Derivation**:
  - For $r > b$: $E(r) = \frac{Q}{4\pi\varepsilon_0 r^2}$.
  - For $a < r < b$: $E(r) = \frac{Q}{4\pi\varepsilon_0 K r^2}$.
  - Potential at $r = a$:
    $$V(a) = \int_a^b E_{\text{in}}\,dr + \int_b^\infty E_{\text{out}}\,dr = \frac{Q}{4\pi\varepsilon_0 K}\left(\frac{1}{a} - \frac{1}{b}\right) + \frac{Q}{4\pi\varepsilon_0}\frac{1}{b} = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{Ka} - \frac{1}{Kb} + \frac{1}{b}\right)$$
- **Correct Option**: **(A)**.

### Q2. Magnetic Moment of Rotating Ring
- **First Observation & Concept**: Magnetic moment $\mu = I A$.
- **Derivation**:
  - Current $I = \frac{Q}{T} = \frac{Q \omega}{2\pi}$.
  - Area $A = \pi R^2$.
  - $\mu = I A = \frac{Q \omega}{2\pi} (\pi R^2) = \frac{1}{2} Q \omega R^2$.
- **Correct Option**: **(A)**.

### Q3. Average AC Power Dissipation
- **First Observation & Concept**: $P = V_{\text{rms}} I_{\text{rms}} \cos\phi$.
- **Derivation**:
  - $V_0 = 200\text{ V} \implies V_{\text{rms}} = 200/\sqrt{2}$.
  - $I_0 = 5.0\text{ A} \implies I_{\text{rms}} = 5.0/\sqrt{2}$.
  - Phase difference $\phi = \pi/3 \implies \cos\phi = 1/2$.
  - $P = \frac{200}{\sqrt{2}} \times \frac{5.0}{\sqrt{2}} \times \frac{1}{2} = \frac{1000}{2} \times \frac{1}{2} = 250\text{ W}$.
- **Correct Option**: **(A)**.

### Q4. Torque on Current Loop
- **First Observation & Concept**: $\vec{\tau} = \vec{M} \times \vec{B} \implies \tau = M B \sin\theta$.
- **Derivation**:
  - $M = I a b$.
  - Angle between normal and field is $\theta = 30^\circ$.
  - $\tau = I a b B_0 \sin 30^\circ = \frac{1}{2} I a b B_0$.
- **Correct Option**: **(A)**.

### Q5. Minimum Period of Compound Pendulum
- **First Observation & Concept**: $T = 2\pi \sqrt{\frac{k^2 + d^2}{g d}}$.
- **Derivation**:
  - $\frac{d}{dd}\left(\frac{k^2}{d} + d\right) = -\frac{k^2}{d^2} + 1 = 0 \implies d = k$.
  - Distance of knife-edge equals radius of gyration $k$ about CM.
- **Correct Option**: **(A)**.

### Q6. Brewster's Law and Snell's Law
- **First Observation & Concept**: $\tan\theta_B = \mu = \sqrt{3} \implies \theta_B = 60^\circ$.
- **Derivation**:
  - At Brewster angle, reflected and refracted rays are perpendicular: $\theta_B + r = 90^\circ$.
  - $r = 90^\circ - 60^\circ = 30^\circ$.
- **Correct Option**: **(A)**.

### Q7. Induced Electric Field from Changing B
- **Analysis**:
  - Symmetry gives circular field lines. (A is True)
  - For $r \le R$: $E(2\pi r) = \pi r^2 \alpha \implies E = \frac{1}{2} \alpha r$. (B is True)
  - For $r > R$: $E(2\pi r) = \pi R^2 \alpha \implies E = \frac{\alpha R^2}{2r}$. (C is True)
  - $F = q E(r)$ is tangential $\implies$ tangential acceleration. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q8. Dielectric Insertion at Constant Voltage
- **Analysis**:
  - Voltage held constant by battery: $V = V_0$. (A is True)
  - $C = K C_0 \implies Q = C V_0 = K C_0 V_0$. (B is True)
  - $U = \frac{1}{2} C V_0^2 = K \left(\frac{1}{2} C_0 V_0^2\right)$. (C is True)
  - Work done by battery: $W_b = \Delta Q V_0 = (K - 1) C_0 V_0^2$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q9. Simple Harmonic Motion Dynamics
- **Analysis**: All four statements correctly state phase relations and energy equipartition in SHM.
- **Correct Options**: **(A, B, C, D)**.

### Q10. Heat Pump Thermodynamics
- **Analysis**: $\text{COP} = 300 / 50 = 6.0$; $W = Q_H / 6 = 1000\text{ J}$; $Q_C = 5000\text{ J}$; reversible cycle has $\Delta S_{\text{univ}} = 0$.
- **Correct Options**: **(A, B, C, D)**.

### Q11. Davisson-Germer Experiment
- **Analysis**: All four statements are standard historical and theoretical facts of the Davisson-Germer experiment.
- **Correct Options**: **(A, B, C, D)**.

### Q12. Sound Interference
- **Analysis**: Constructive and destructive conditions, maximum intensity $4I_0$, zero minimum intensity.
- **Correct Options**: **(A, B, C, D)**.

### Q13. Attractive Force Between Capacitor Plates
- **Derivation**:
  - $F = \frac{1}{2} Q E = \frac{\varepsilon_0 A V^2}{2 d^2}$.
  - $F = \frac{8.85 \times 10^{-12} \times 0.050 \times 200^2}{2 \times (1.0 \times 10^{-3})^2} = \frac{8.85 \times 10^{-12} \times 0.050 \times 40000}{2 \times 10^{-6}} = \frac{1.77 \times 10^{-8}}{2 \times 10^{-6}} = 8.85 \times 10^{-3}\text{ N} = 8.85\text{ mN}$.
- **Answer**: **8.85**.

### Q14. Magnetic Field at Center of Coil
- **Derivation**:
  $$B = \frac{\mu_0 N I}{2 r} = \frac{4\pi \times 10^{-7} \times 100 \times 2.0}{2 \times 0.050} = \frac{8\pi \times 10^{-5}}{0.10} = 8\pi \times 10^{-4}\text{ T} = 2.51 \times 10^{-3}\text{ T} = 2.51\text{ mT}$$
- **Answer**: **2.51**.

### Q15. Rolling Sphere Kinetic Energy
- **Derivation**:
  - $E_k = \frac{7}{10} M v^2 = \frac{7}{10} \times 5.0 \times 4.0^2 = \frac{7}{10} \times 5.0 \times 16 = 56.0\text{ J}$.
- **Answer**: **56** (or **56.0**).

### Q16. Radius of Curvature from Newton's Rings
- **Derivation**:
  - For $n$-th dark ring: $D_n^2 = 4 n \lambda R$.
  - $(4.0 \times 10^{-3})^2 = 4 \times 4 \times (600 \times 10^{-9}) \times R$.
  - $16.0 \times 10^{-6} = 16 \times 600 \times 10^{-9} R = 9.6 \times 10^{-6} R$.
  - $R = \frac{16.0 \times 10^{-6}}{9.6 \times 10^{-6}} = \frac{16}{9.6} = 1.67\text{ m}$.
- **Answer**: **1.67**.

### Q17. Doppler Effect in Whirled Whistle
- **Derivation**:
  - Speed of whistle $u = \omega L = 20.0 \times 1.0 = 20.0\text{ m/s}$.
  - $f_{\max} = f \frac{v}{v - u} = 500 \times \frac{340}{340 - 20} = 500 \times \frac{340}{320} = 531.25\text{ Hz}$.
  - $f_{\min} = f \frac{v}{v + u} = 500 \times \frac{340}{340 + 20} = 500 \times \frac{340}{360} = 472.22\text{ Hz}$.
  - Difference $\Delta f = 531.25 - 472.22 = 59.03 \approx 59.0\text{ Hz}$.
- **Answer**: **59.0**.

### Q18. Mean Lifetime of Radioactive Nuclide
- **Derivation**:
  $$\tau = \frac{1}{\lambda} = \frac{1}{0.050} = 20.0\text{ s}$$
- **Answer**: **20** (or **20.0**).

---

## PART II: CHEMISTRY

### Q19. Specific Conductance
- **Analysis**:
  $$\Lambda_m = \frac{1000 \kappa}{M} \implies \kappa = \frac{\Lambda_m M}{1000} = \frac{120.0 \times 0.010}{1000} = 1.20 \times 10^{-3}\text{ S/cm}$$
- **Correct Option**: **(A)**.

### Q20. Chelating Ligands
- **Analysis**:
  - Glycinate ($\text{H}_2\text{N}-\text{CH}_2-\text{COO}^-$) is bidentate with charge $-1$ (monoanionic).
  - $\text{en}$ and $\text{phen}$ are neutral bidentate; oxalate is dianionic ($-2$).
- **Correct Option**: **(A)**.

### Q21. Cresol Isomer Identification
- **Analysis**:
  - $p$-Cresol has the para position occupied; upon bromination, the two positions ortho to $-\text{OH}$ are equivalent due to symmetry, yielding a single monobromo derivative (2-bromo-4-methylphenol).
- **Correct Option**: **(A)**.

### Q22. Alkali Metal Halide Lattice Enthalpy
- **Analysis**:
  - Lattice energy $\propto \frac{1}{r_+ + r_-}$. Down the group from $\text{Li}^+$ to $\text{Cs}^+$, ionic radius increases, so lattice enthalpy decreases: $\text{LiF} > \text{NaF} > \text{KF} > \text{RbF} > \text{CsF}$.
- **Correct Option**: **(A)**.

### Q23. Effect of Volume on Rate
- **Analysis**:
  - Halving volume doubles all concentrations: $[\text{A}]' = 2[\text{A}]$, $[\text{B}]' = 2[\text{B}]$.
  - $\text{Rate}' = k (2[\text{A}])^2 (2[\text{B}]) = 8 k [\text{A}]^2 [\text{B}] = 8 \times \text{Rate}$.
- **Correct Option**: **(A)**.

### Q24. KMnO4 in Acidic Medium
- **Analysis**:
  - $\text{MnO}_4^- + 8\text{H}^+ + 5e^- \rightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O}$ ($+7 \rightarrow +2$, gain of $5e^-$).
- **Correct Option**: **(A)**.

### Q25. Thermodynamic Relations of Electrochemical Cells
- **Analysis**: All four relations are rigorous consequences of the Gibbs-Helmholtz equation applied to reversible cells.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Crystal Field Splitting Parameters
- **Analysis**: $e_g$ destabilization $+0.6\Delta_o$, $\Delta_t = \frac{4}{9}\Delta_o$, spectrochemical series high-spin/low-spin criteria.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Tollens' Reagent Reduction
- **Analysis**:
  - Aldehydes (glucose, benzaldehyde, formic acid) reduce Tollens' reagent.
  - Fructose (an $\alpha$-hydroxy ketone) isomerizes to glucose/mannose in alkaline Tollens' reagent (Lobry de Bruyn-van Ekenstein transformation) and gives a positive test.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Cyanide Leaching of Gold
- **Analysis**: MacArthur-Forrest process chemistry: oxidative leaching, complexation, zinc cementation reduction.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Reversible Isothermal Expansion
- **Analysis**: $\Delta U = 0$, $W = nRT\ln(V_2/V_1)$, $Q = W$, $\Delta S = nR\ln(V_2/V_1)$.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Group 14 Characteristics
- **Analysis**: Catenation of C, inert pair effect of Pb, $\text{CCl}_4$ resistance to hydrolysis vs $\text{SiCl}_4$ rapid hydrolysis.
- **Correct Options**: **(A, B, C, D)**.

### Q31. Standard Reduction Potential
- **Derivation**:
  $$E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} \implies 1.56 = E^\circ_{\text{Ag}^+/\text{Ag}} - (-0.76) \implies E^\circ_{\text{Ag}^+/\text{Ag}} = 1.56 - 0.76 = +0.80\text{ V}$$
- **Answer**: **0.80** (or **0.8**).

### Q32. pOH of Weak Base
- **Derivation**:
  $$[\text{OH}^-] = \sqrt{K_b c} = \sqrt{1.8 \times 10^{-5} \times 0.10} = \sqrt{1.8 \times 10^{-6}} = 1.34 \times 10^{-3}\text{ M}$$
  $$\text{pOH} = -\log_{10}(1.34 \times 10^{-3}) = 3 - 0.127 = 2.873 \approx 2.87$$
- **Answer**: **2.87**.

### Q33. Density of Simple Cubic Metal
- **Derivation**:
  - Simple cubic: $Z = 1$ atom per unit cell.
  - $V = a^3 = (3.0 \times 10^{-8})^3 = 27.0 \times 10^{-24}\text{ cm}^3$.
  - $\rho = \frac{Z M}{N_A V} = \frac{1 \times 108.0}{6.02 \times 10^{23} \times 27.0 \times 10^{-24}} = \frac{108.0}{16.25} \approx 6.6\text{ g/cm}^3$.
- **Answer**: **6.6**.

### Q34. Time for 75% Decay
- **Derivation**:
  - $75\%$ decay means $25\% = 1/4 = (1/2)^2$ remains $\implies 2$ half-lives.
  - Total time $= 2 \times 20.0 = 40.0\text{ days}$.
- **Answer**: **40** (or **40.0**).

### Q35. Freezing Point Depression of Urea Solution
- **Derivation**:
  - Moles of urea $= 6.0 / 60.0 = 0.10\text{ mol}$.
  - Mass of solvent $= 0.500\text{ kg} \implies m = 0.10 / 0.500 = 0.20\text{ m}$.
  - $\Delta T_f = K_f m = 1.86 \times 0.20 = 0.372\text{ K} \approx 0.37\text{ K}$.
- **Answer**: **0.37**.

### Q36. Molar Solubility of PbCl2
- **Derivation**:
  - $K_{sp} = 4s^3 \implies 1.6 \times 10^{-5} = 4s^3 \implies s^3 = 4.0 \times 10^{-6}$.
  - $s = (4.0)^{1/3} \times 10^{-2} = 1.59 \times 10^{-2}\text{ M} = 15.9\text{ mmol/L}$.
- **Answer**: **15.9**.

---

## PART III: MATHEMATICS

### Q37. Locus in Complex Plane
- **Derivation**:
  - $\left|\frac{z - i}{z + i}\right| = 1 \iff |z - i| = |z + i|$.
  - This is the locus of points equidistant from $(0, 1)$ and $(0, -1)$, which is the perpendicular bisector: the real axis ($y = 0$).
- **Correct Option**: **(A)**.

### Q38. Beta Function Integral
- **Derivation**:
  - Using $\int_0^1 x (1 - x)^9\,dx$: let $u = 1 - x \implies \int_0^1 (1 - u) u^9\,du = \int_0^1 (u^9 - u^{10})\,du = \frac{1}{10} - \frac{1}{11} = \frac{1}{110}$.
- **Correct Option**: **(A)**.

### Q39. Tangent to Parabola
- **Derivation**: Standard condition of tangency for $y = mx + c$ to $y^2 = 4ax$ is $c = a/m$.
- **Correct Option**: **(A)**.

### Q40. Differential Equation Family
- **Derivation**:
  $$\frac{dy}{y} = \frac{dx}{x} \implies \ln|y| = \ln|x| + \ln|k| \implies y = kx$$
  This represents a family of straight lines passing through the origin.
- **Correct Option**: **(A)**.

### Q41. Permutations with Restriction
- **Derivation**:
  - Digits: $2, 4, 5, 7, 8$ (5 digits).
  - To be $> 5000$, the first digit must be $5, 7,$ or $8$ (3 choices).
  - The remaining 3 positions can be filled by the remaining 4 digits in $P(4, 3) = 4 \times 3 \times 2 = 24$ ways.
  - Total numbers $= 3 \times 24 = 72$.
- **Correct Option**: **(A)**.

### Q42. Distance from Origin to Plane
- **Derivation**:
  $$d = \frac{|-14|}{\sqrt{2^2 + (-3)^2 + 6^2}} = \frac{14}{\sqrt{4 + 9 + 36}} = \frac{14}{\sqrt{49}} = \frac{14}{7} = 2$$
- **Correct Option**: **(A)**.

### Q43. Rational Function Analysis
- **Analysis**:
  - $f(-x) = -f(x)$ (odd). (A is True)
  - $f'(x) = \frac{1 - x^2}{(1+x^2)^2} = 0 \implies x = \pm 1$. Local max $f(1) = 1/2$, local min $f(-1) = -1/2$. (B, C are True)
  - Range is $[-1/2, 1/2]$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q44. Geometric Properties of Ellipse
- **Analysis**: Focal property, auxiliary circle foot of perpendicular, product of focal perpendiculars $= b^2$, director circle $= a^2 + b^2$.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Matrix Determinant and Trace Properties
- **Analysis**: Standard matrix algebra theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Unit Vector Identities
- **Analysis**:
  - $|\vec{a} + \vec{b}|^2 = 1 + 1 + 2\cos\theta = 2(1 + \cos\theta) = 4\cos^2(\theta/2) \implies |\vec{a} + \vec{b}| = 2\cos(\theta/2)$.
  - $|\vec{a} - \vec{b}|^2 = 2(1 - \cos\theta) = 4\sin^2(\theta/2) \implies |\vec{a} - \vec{b}| = 2\sin(\theta/2)$.
  - $(\vec{a} + \vec{b}) \cdot (\vec{a} - \vec{b}) = |\vec{a}|^2 - |\vec{b}|^2 = 1 - 1 = 0 \implies$ orthogonal.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Complex Number Properties
- **Analysis**: Triangle inequalities, parallelogram identity, argument additivity.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Dice Probability
- **Analysis**:
  - Sum of 7: 6 outcomes out of 36 $= 1/6$. (A is True)
  - Sum $\ge 10$: $(4,6), (5,5), (5,6), (6,4), (6,5), (6,6) = 6$ outcomes $= 1/6$. (B is True)
  - Doublet: 6 outcomes $= 1/6$. (C is True)
  - Given first die is 4, sum is 8 requires second die to be 4 $\implies 1/6$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q49. Standard Limit
- **Derivation**:
  $$\lim_{x \to 0} \frac{\tan x - x}{x^3} = \frac{1}{3} \approx 0.33$$
- **Answer**: **0.33**.

### Q50. Area Enclosed by Curves
- **Derivation**:
  - $\sqrt{x} = x \implies x = x^2 \implies x(x - 1) = 0 \implies x = 0, 1$.
  - Area $= \int_0^1 (\sqrt{x} - x)\,dx = [\frac{2}{3}x^{3/2} - \frac{x^2}{2}]_0^1 = \frac{2}{3} - \frac{1}{2} = \frac{1}{6} \approx 0.17$.
- **Answer**: **0.17**.

### Q51. Walli's Definite Integral
- **Derivation**:
  $$\int_0^{\pi/2} \sin^3 x\,dx = \frac{2}{3} \times 1 = \frac{2}{3} \approx 0.67$$
- **Answer**: **0.67**.

### Q52. In-Radius of Right Triangle
- **Derivation**:
  $$r = \frac{a + b - c}{2} = \frac{5 + 12 - 13}{2} = \frac{4}{2} = 2.0\text{ cm}$$
- **Answer**: **2** (or **2.0**).

### Q53. Real Roots of Cubic
- **Derivation**:
  - $f(x) = x^3 - 3x + 1$.
  - $f'(x) = 3x^2 - 3 = 3(x - 1)(x + 1) = 0 \implies x = \pm 1$.
  - $f(-1) = -1 + 3 + 1 = 3 > 0$.
  - $f(1) = 1 - 3 + 1 = -1 < 0$.
  - Since local max is positive and local min is negative, the graph crosses the x-axis 3 times $\implies 3$ real roots.
- **Answer**: **3**.

### Q54. Vandermonde Determinant
- **Derivation**:
  $$\begin{vmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 4 & 9 \end{vmatrix} = (2 - 1)(3 - 1)(3 - 2) = 1 \times 2 \times 1 = 2$$
- **Answer**: **2**.
