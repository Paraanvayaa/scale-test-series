# Detailed Solutions and Pedagogical Analysis — Mock Examination 14 (Paper 2)
### Organising Institute Style: IIT Kharagpur (`IIT_KHARAGPUR_STYLE` — 2021 Paradigm)

---

## PART I: PHYSICS

### Q1. Rolling Spherical Shell
- **Analysis**:
  - $I = \frac{2}{3} M R^2$. Kinetic energy: $E_k = \frac{1}{2} M v_0^2 + \frac{1}{2} \left(\frac{2}{3} M R^2\right) \frac{v_0^2}{R^2} = \frac{5}{6} M v_0^2$. (A is True)
  - Conservation of mechanical energy: $M g h = \frac{5}{6} M v_0^2 \implies h = \frac{5 v_0^2}{6g}$. (B is True)
  - For rolling without slipping on incline: $a = \frac{g \sin\alpha}{1 + I/(MR^2)} = \frac{g \sin\alpha}{1 + 2/3} = \frac{3}{5} g \sin\alpha$.
    Friction $f = M g \sin\alpha - M a = M g \sin\alpha \left(1 - \frac{3}{5}\right) = \frac{2}{5} M g \sin\alpha$.
    Static friction condition: $f \le \mu N \implies \frac{2}{5} M g \sin\alpha \le \mu M g \cos\alpha \implies \mu \ge \frac{2}{5} \tan\alpha$. (C is True)
  - Static friction acts at the point of instantaneous rest, so work done by friction is zero. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q2. Thermodynamic Monatomic Cycle
- **Analysis**:
  - $2 \rightarrow 3$ is isothermal at $T_2 = 2 T_0$: $W_{23} = P_2 V_2 \ln(V_3/V_2) = (2P_0)(V_0) \ln(2V_0/V_0) = 2P_0 V_0 \ln 2$. (A is True)
  - $3 \rightarrow 1$ is isobaric at $P_0$: $Q_{31} = n C_P \Delta T = \frac{5}{2} n R (T_1 - T_3) = \frac{5}{2} (P_0 V_0 - P_0 2V_0) = -\frac{5}{2} P_0 V_0$. Heat rejected is $\frac{5}{2} P_0 V_0$. (B is True)
  - Heat input: $Q_{\text{in}} = Q_{12} + Q_{23} = n C_V \Delta T + W_{23} = \frac{3}{2}(2P_0 V_0 - P_0 V_0) + 2P_0 V_0 \ln 2 = P_0 V_0 \left(\frac{3}{2} + 2\ln 2\right)$.
    Work done: $W_{\text{net}} = W_{23} + W_{31} = 2P_0 V_0 \ln 2 - P_0(2V_0 - V_0) = P_0 V_0(2\ln 2 - 1)$.
    Efficiency: $\eta = \frac{W_{\text{net}}}{Q_{\text{in}}} = \frac{2\ln 2 - 1}{\frac{3}{2} + 2\ln 2}$. (C is True)
  - Clockwise cycle $\implies W_{\text{net}} > 0$, acts as a heat engine. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q3. Concentric Coplanar Inductive Loops
- **Analysis**:
  - Outer loop flux: $\Phi = B \pi a^2 = \pi a^2 B_0 \sin(\omega t)$. EMF: $-\frac{d\Phi}{dt} = -\pi a^2 B_0 \omega \cos(\omega t)$, amplitude $\pi a^2 B_0 \omega$. (A is True)
  - Current $I = \frac{\mathcal{E}}{R} = -\frac{\pi a^2 B_0 \omega}{R}\cos(\omega t)$. Magnitude is $\frac{\pi a^2 B_0 \omega}{R}\cos(\omega t)$. (B is True)
  - Magnetic field at center: $B_c = \frac{\mu_0 I}{2a} \propto \frac{B_0 \omega}{R}$. (C is True)
  - Mutual inductance: field at center from unit current in outer loop is $\frac{\mu_0}{2a}$, flux through inner loop is $\frac{\mu_0 \pi b^2}{2a} \implies M = \frac{\mu_0 \pi b^2}{2a}$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q4. Dielectric Slab in Capacitor
- **Analysis**:
  - Series combination of air gap ($d/2$) and dielectric ($d/2$ with $K$):
    $$C = \frac{\varepsilon_0 A}{\frac{d}{2} + \frac{d/2}{K}} = \frac{2\varepsilon_0 A}{d \left(1 + \frac{1}{K}\right)} = \frac{2K \varepsilon_0 A}{(K + 1)d}$$ (A is True)
  - $V_0 = E_{\text{air}} \frac{d}{2} + E_{\text{dielectric}} \frac{d}{2} = E_{\text{air}} \frac{d}{2} \left(1 + \frac{1}{K}\right) \implies E_{\text{air}} = \frac{2K V_0}{(K + 1)d}$. (B is True)
  - $E_{\text{dielectric}} = \frac{E_{\text{air}}}{K} = \frac{2V_0}{(K + 1)d}$. (C is True)
  - Induced charge: $\sigma_b = \varepsilon_0 (E_{\text{air}} - E_{\text{dielectric}}) = \frac{2(K - 1)\varepsilon_0 V_0}{(K + 1)d}$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q5. Singly Ionized Helium Properties
- **Analysis**:
  - $r_n = \frac{n^2 a_0}{Z}$. For $\text{He}^+, Z = 2 \implies r_1 = a_0 / 2$. (A is True)
  - $E_n = -13.6 \frac{Z^2}{n^2}\text{ eV}$. For $n = 1$, $E_1 = -13.6 \times 4 = -54.4\text{ eV}$. Ionization energy is $54.4\text{ eV}$. (B is True)
  - $\frac{1}{\lambda} = R Z^2 \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right) \propto Z^2 = 4 \implies \lambda_{\text{He}^+} = \frac{1}{4} \lambda_H$. (C is True)
  - Orbital magnetic moment $\mu = I A = \frac{e}{2m} L = \frac{e}{2m} n\hbar \propto n$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q6. Sound Wave Propagation
- **Analysis**:
  - $\lambda = v/f = 340/680 = 0.50\text{ m}$. (A is True)
  - Phase difference $\Delta\phi = \frac{2\pi}{\lambda}\Delta x = \frac{2\pi}{0.50} \times 0.25 = \pi\text{ rad}$. (B is True)
  - Phase difference of $\pi$ means opposite phase / anti-phase. (C is True)
  - Rigid boundary forces particle velocity/displacement to be zero $\implies$ displacement node. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q7. Pulling Rolling Cylinder
- **Derivation**:
  - Taking torque about instantaneous axis of rotation (contact point with ground):
    $$\tau_C = F (2R) = I_C \alpha$$
  - $I_C = \frac{1}{2} M R^2 + M R^2 = \frac{3}{2} M R^2$.
  - $F (2R) = \frac{3}{2} M R^2 \left(\frac{a}{R}\right) = \frac{3}{2} M R a \implies 2F = \frac{3}{2} M a \implies a = \frac{4F}{3M}$.
  - $a = \frac{4 \times 18.0}{3 \times 6.0} = \frac{72.0}{18.0} = 4.0\text{ m/s}^2$.
- **Answer**: **4.0** (or **4**).

### Q8. Isobaric Heating of Diatomic Gas
- **Derivation**:
  - $Q = n C_P \Delta T$.
  - For diatomic gas, $C_P = \frac{7}{2} R$.
  - $Q = 2.0 \times \frac{7}{2} \times 8.314 \times (400 - 300) = 7 \times 8.314 \times 100 = 5819.8 \approx 5820\text{ J}$.
- **Answer**: **5820**.

### Q9. Coinciding Fringes in YDSE
- **Derivation**:
  - $y = n_1 \frac{\lambda_1 D}{d} = n_2 \frac{\lambda_2 D}{d} \implies n_1 \lambda_1 = n_2 \lambda_2$.
  - $\frac{n_1}{n_2} = \frac{\lambda_2}{\lambda_1} = \frac{480}{600} = \frac{4}{5}$.
  - Minimum non-zero integers: $n_1 = 4, n_2 = 5$.
  - $y = 4 \times \frac{600 \times 10^{-9} \times 1.0}{1.0 \times 10^{-3}} = 2.4 \times 10^{-3}\text{ m} = 2.4\text{ mm}$.
- **Answer**: **2.4** (or **2.40**).

### Q10. de Broglie Wavelength of Electron
- **Derivation**:
  - $\lambda = \frac{12.27}{\sqrt{V}}\text{ \AA} = \frac{12.27}{\sqrt{150}} = \frac{12.27}{12.247} \approx 1.00\text{ \AA}$.
- **Answer**: **1.00** (or **1.0**).

### Q11. Deviation by Thin Prism
- **Derivation**:
  - $\delta = (\mu - 1) A = (1.50 - 1) \times 4.0^\circ = 0.50 \times 4.0^\circ = 2.0^\circ$.
- **Answer**: **2.0** (or **2**).

### Q12. AC Power Factor
- **Derivation**:
  - $\omega = 2\pi f = 2 \times 3.1416 \times 50 = 314.16\text{ rad/s}$.
  - $X_L = \omega L = 314.16 \times 0.050 = 15.71\,\Omega$.
  - $Z = \sqrt{R^2 + X_L^2} = \sqrt{10^2 + (15.71)^2} = \sqrt{100 + 246.8} = \sqrt{346.8} \approx 18.62\,\Omega$.
  - $\cos\phi = \frac{R}{Z} = \frac{10}{18.62} \approx 0.54$.
- **Answer**: **0.54**.

### Q13. Kepler's Third Law
- **Derivation**: $T^2 \propto r^3 \implies T \propto r^{3/2}$. If $r \rightarrow 4r$, $T \rightarrow (4)^{3/2} T = 8 T \implies k = 8$.
- **Answer**: **8**.

### Q14. Nodes in Standing Wave
- **Derivation**: In a string fixed at both ends with 4 antinodes, it is vibrating in the 4th harmonic. Number of nodes $= n + 1 = 4 + 1 = 5$.
- **Answer**: **5**.

### Q15. Beta Decays in Uranium Chain
- **Derivation**:
  - $Z_{\text{final}} = Z_{\text{initial}} - 2 N_\alpha + N_\beta$.
  - $82 = 92 - 2(8) + N_\beta = 92 - 16 + N_\beta = 76 + N_\beta \implies N_\beta = 6$.
- **Answer**: **6**.

### Q16. Elastic Constants of Isotropic Solid
- **Derivation**: For an isotropic elastic solid, there are exactly 2 independent elastic constants (e.g., Young's modulus and Poisson's ratio, or Lamé parameters $\lambda$ and $\mu$).
- **Answer**: **2**.

### Q17. Frequency of Cut Spring
- **Derivation**: When cut into two halves, spring constant doubles: $k' = 2k$.
  Frequency $f' = \frac{1}{2\pi}\sqrt{\frac{k'}{m}} = \sqrt{2} \left(\frac{1}{2\pi}\sqrt{\frac{k}{m}}\right) = 5\sqrt{2}\text{ Hz} \implies k = 2$.
- **Answer**: **2**.

### Q18. Degeneracy of n = 3 Level
- **Derivation**: Neglecting spin, degeneracy of level $n$ is $n^2 = 3^2 = 9$.
- **Answer**: **9**.

---

## PART II: CHEMISTRY

### Q19. Organic Cascade Analysis
- **Analysis**:
  - $A$ ($\text{C}_7\text{H}_7\text{NO}$) with $\text{Br}_2/\text{KOH}$ gives aniline ($B$, $\text{C}_6\text{H}_7\text{N}$) via Hofmann degradation $\implies A$ is benzamide.
  - Diazotization and reaction with $\text{CuCN}$ yields benzonitrile ($C$).
  - Acid hydrolysis of benzonitrile produces benzoic acid ($D$).
- **Correct Options**: **(A, B, C, D)**.

### Q20. Isomerism in [Cr(NH3)4Cl2]+
- **Analysis**:
  - $[M a_4 b_2]$ octahedral complex exhibits cis and trans geometrical isomerism.
  - Trans has $D_{4h}$ symmetry (achiral).
  - Cis has $C_{2v}$ symmetry with a plane of symmetry passing through Cr and bisecting the $\text{Cl}-\text{Cr}-\text{Cl}$ angle, so cis-$[\text{Cr}(\text{NH}_3)_4\text{Cl}_2]^+$ is ACHIRAL (optically inactive!).
  - Therefore (B) is FALSE!
  - Trans isomer has chlorides at opposite vertices. (C is True)
  - $\text{Cr}^{3+}$ has $3d^3$, $t_{2g}^3$. (D is True)
- **Correct Options**: **(A, C, D)**.

### Q21. Group 15 Chemistry
- **Analysis**:
  - $\text{H}_3\text{PO}_2$: one ionizable $-\text{OH}$, two $\text{P}-\text{H}$ bonds (monobasic). (A is True)
  - Crystalline $\text{PCl}_5$ consists of tetrahedral $[\text{PCl}_4]^+$ and octahedral $[\text{PCl}_6]^-$. (B is True)
  - Hydrogen bonding gives $\text{NH}_3$ abnormally high boiling point. (C is True)
  - Lone pair availability decreases down group as atomic size increases and $s$-character increases (Drago's rule). (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q22. Aldol Condensation Mechanism
- **Analysis**:
  - Enolate formation via $\alpha$-proton abstraction. (A is True)
  - Nucleophilic addition to carbonyl carbon gives aldol. (B is True)
  - Dehydration follows $E1cB$ elimination of hydroxide. (C is True)
  - Demonstrates $\alpha$-hydrogen acidity. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q23. Froth Floatation Principles
- **Analysis**:
  - Xanthates are collectors (make ore particles hydrophobic).
  - Pine oil creates stable froth.
  - $\text{NaCN}$ complexes $\text{Zn}^{2+}$ into soluble $[\text{Zn}(\text{CN})_4]^{2-}$ while allowing $\text{PbS}$ to float.
  - Collectors provide hydrophobic coating.
- **Correct Options**: **(A, B, C, D)**.

### Q24. Mechanism of Rusting
- **Analysis**:
  - Anodic oxidation: $\text{Fe} \rightarrow \text{Fe}^{2+} + 2e^-$.
  - Cathodic reduction of oxygen in presence of $\text{H}^+$.
  - Rust is $\text{Fe}_2\text{O}_3 \cdot x\text{H}_2\text{O}$.
  - Zinc provides sacrificial cathodic protection.
- **Correct Options**: **(A, B, C, D)**.

### Q25. EMF of Copper Half-Cell
- **Derivation**:
  $$E = E^\circ - \frac{0.0591}{2} \log_{10}\left(\frac{1}{[\text{Cu}^{2+}]}\right) = 0.34 - \frac{0.0591}{2}\log_{10}(10) = 0.34 - 0.0295 = 0.31\text{ V}$$
- **Answer**: **0.31**.

### Q26. Ksp Calculation
- **Derivation**:
  $$\text{CaF}_2 \rightleftharpoons \text{Ca}^{2+} + 2\text{F}^-$$
  $$K_{sp} = s \times (2s)^2 = 4s^3 = 4 \times (2.0 \times 10^{-4})^3 = 4 \times (8.0 \times 10^{-12}) = 32 \times 10^{-12} = 3.2 \times 10^{-11}$$
  $$k = 3.2$$
- **Answer**: **3.2**.

### Q27. Time for Zero-Order Completion
- **Derivation**:
  $$t_{\text{complete}} = \frac{[A]_0}{k} = \frac{0.80}{0.0040} = 200\text{ s}$$
- **Answer**: **200**.

### Q28. Degree of Dissociation of Weak Acid
- **Derivation**:
  $$\Delta T_f = i K_f m \implies 0.1116 = i \times 1.86 \times 0.050 = i \times 0.0930$$
  $$i = \frac{0.1116}{0.0930} = 1.20$$
  $$i = 1 + \alpha \implies \alpha = 0.20 = 20\%$$
- **Answer**: **20**.

### Q29. Heat of Combustion of Carbon
- **Derivation**:
  - $12.0\text{ g}$ corresponds to $1.0\text{ mol}$.
  - Heat evolved $= \frac{2.40}{12.0} \times 393.5 = 0.20 \times 393.5 = 78.7\text{ kJ}$.
- **Answer**: **78.7**.

### Q30. Relative Lowering of Vapor Pressure
- **Derivation**:
  - Moles of glucose: $n_2 = 18.0 / 180 = 0.10\text{ mol}$.
  - Moles of water: $n_1 = 178.2 / 18.0 = 9.90\text{ mol}$.
  - Total moles: $n_1 + n_2 = 10.00\text{ mol}$.
  - Relative lowering: $\frac{\Delta P}{P^\circ} = x_2 = \frac{n_2}{n_1 + n_2} = \frac{0.10}{10.00} = 0.010$.
- **Answer**: **0.010** (or **0.01**).

### Q31. Oxidation State of Cr in K2Cr2O7
- **Derivation**: $2(+1) + 2x + 7(-2) = 0 \implies 2x = 12 \implies x = 6$.
- **Answer**: **6**.

### Q32. Unpaired Electrons in [Ni(H2O)6]2+
- **Derivation**: $\text{Ni}^{2+}$ is $3d^8$. In octahedral field: $t_{2g}^6 e_g^2 \implies 2$ unpaired electrons.
- **Answer**: **2**.

### Q33. Basicity of Pyrophosphoric Acid
- **Derivation**: $\text{H}_4\text{P}_2\text{O}_7$ has structure $(\text{HO})_2\text{P}(=\text{O})-\text{O}-\text{P}(=\text{O})(\text{OH})_2$ with 4 ionizable $-\text{OH}$ groups $\implies$ basicity = 4.
- **Answer**: **4**.

### Q34. Stereoisomers of Tartaric Acid
- **Derivation**: Contains two identical stereocenters: $d$-tartaric acid, $l$-tartaric acid, and meso-tartaric acid $\implies 3$ stereoisomers.
- **Answer**: **3**.

### Q35. Coordination Number in NaCl
- **Derivation**: In rock salt structure, each $\text{Na}^+$ is surrounded octahedrally by $6$ $\text{Cl}^-$ ions $\implies$ coordination number = 6.
- **Answer**: **6**.

### Q36. Sigma Bonds in Benzene
- **Derivation**: 6 $\text{C}-\text{C}$ $\sigma$-bonds $+ 6$ $\text{C}-\text{H}$ $\sigma$-bonds $= 12$ $\sigma$-bonds.
- **Answer**: **12**.

---

## PART III: MATHEMATICS

### Q37. Analysis of Cubic Function
- **Analysis**:
  - $f(x) = (x - 1)^3$. (A is True)
  - $f'(x) = 3(x - 1)^2 \ge 0$, equals 0 at $x = 1$. (B is True)
  - Since $f'(x) > 0$ almost everywhere, $f(x)$ is strictly increasing. (C is True)
  - $f''(x) = 6(x - 1)$ changes sign from negative to positive at $x = 1$, so $x = 1$ is an inflection point. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q38. Consistency of Linear Systems
- **Analysis**:
  - Subtract equation 1 from equation 2: $y + 2z = 4$.
  - Subtract equation 1 from equation 3: $y + (\lambda - 1)z = \mu - 6$.
  - Subtract these two: $(\lambda - 3)z = \mu - 10$.
  - If $\lambda \ne 3$, $z$ is uniquely determined $\implies$ unique solution. (A is True)
  - If $\lambda = 3$ and $\mu = 10$, $0 \cdot z = 0 \implies$ infinitely many solutions. (B is True)
  - If $\lambda = 3$ and $\mu \ne 10$, $0 \cdot z = \text{non-zero} \implies$ inconsistent. (C is True)
  - For $\lambda = 3, \mu = 10$, plug $(1, 2, 3)$: $1+2+3 = 6$, $1+4+9 = 14 \ne 10$, so $(1, 2, 3)$ is NOT a solution! (D is False).
- **Correct Options**: **(A, B, C)**.

### Q39. Geometry of Parabola
- **Analysis**:
  - $y^2 = 8x \implies 4a = 8 \implies a = 2$.
  - Focus is $(a, 0) = (2, 0)$. (A is True)
  - Directrix is $x = -a = -2$. (B is True)
  - Tangent at $(2, 4)$: $y(4) = 4(x + 2) \implies 4y = 4x + 8 \implies x - y + 2 = 0$. (C is True)
  - Slope of tangent is 1, so normal has slope $-1$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q40. Reduction Formula for In
- **Analysis**:
  - $I_n = \int_0^1 x^n e^{-x}\,dx = [-x^n e^{-x}]_0^1 + n \int_0^1 x^{n-1} e^{-x}\,dx = -e^{-1} + n I_{n-1}$. (A is True)
  - $I_0 = \int_0^1 e^{-x}\,dx = 1 - e^{-1}$. (B is True)
  - $I_1 = -e^{-1} + I_0 = 1 - 2e^{-1}$. (C is True)
  - On $[0, 1]$, $0 \le x^n e^{-x} \le x^n \implies 0 \le I_n \le \frac{1}{n+1} \rightarrow 0$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q41. Classical Probability
- **Analysis**:
  - Total outcomes $\binom{10}{3} = 120$. (A is True)
  - 3 black balls: $\frac{\binom{6}{3}}{120} = \frac{20}{120} = \frac{1}{6}$. (B is True)
  - At least one white $= 1 - P(\text{all black}) = 1 - \frac{1}{6} = \frac{5}{6}$. (C is True)
  - Expected number of white balls: $n p = 3 \times \frac{4}{10} = 1.2$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q42. Vector Identities
- **Analysis**: All four identities are standard vector algebra theorems.
- **Correct Options**: **(A, B, C, D)**.

### Q43. Definite Integral Symmetry
- **Derivation**:
  - Let $I = \int_0^{\pi/2} \frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}}\,dx$.
  - Using $x \rightarrow \pi/2 - x$: $I = \int_0^{\pi/2} \frac{\sqrt{\cos x}}{\sqrt{\cos x} + \sqrt{\sin x}}\,dx$.
  - $2I = \int_0^{\pi/2} 1\,dx = \frac{\pi}{2} \implies I = \frac{\pi}{4}$.
  - $k = 4$.
- **Answer**: **4**.

### Q44. Maximum of Polynomial
- **Derivation**:
  - $f(x) = x(1 - 2x + x^2) = x - 2x^2 + x^3$.
  - $f'(x) = 1 - 4x + 3x^2 = (3x - 1)(x - 1) = 0 \implies x = 1/3$ or $x = 1$.
  - At $x = 1/3$: $f(1/3) = \frac{1}{3} (1 - 1/3)^2 = \frac{1}{3} \times \frac{4}{9} = \frac{4}{27}$.
  - Fraction form: $p/q = 4/27 \implies q - p = 27 - 4 = 23$.
- **Answer**: **23**.

### Q45. Distance from Point to Plane
- **Derivation**:
  $$d = \frac{|2(1) - 3(2) + 6(3) + 12|}{\sqrt{2^2 + (-3)^2 + 6^2}} = \frac{|2 - 6 + 18 + 12|}{\sqrt{4 + 9 + 36}} = \frac{26}{\sqrt{49}} = \frac{26}{7} \approx 3.71$$
- **Answer**: **3.71**.

### Q46. Eccentricity of Hyperbola
- **Derivation**:
  - $\frac{x^2}{16} - \frac{y^2}{9} = 1 \implies a^2 = 16, b^2 = 9$.
  - $e = \sqrt{1 + \frac{b^2}{a^2}} = \sqrt{1 + \frac{9}{16}} = \sqrt{\frac{25}{16}} = \frac{5}{4} = 1.25$.
- **Answer**: **1.25**.

### Q47. Sum of AP
- **Derivation**:
  - $a = 3, d = 4, n = 20$.
  - $S_{20} = \frac{20}{2} [2(3) + 19(4)] = 10 [6 + 76] = 10 \times 82 = 820$.
- **Answer**: **820**.

### Q48. Orthogonal Vectors
- **Derivation**:
  $$\vec{u} \cdot \vec{v} = 1(2) + 2(-1) + 3(\alpha) = 2 - 2 + 3\alpha = 3\alpha = 0 \implies \alpha = 0$$
- **Answer**: **0**.

### Q49. Permutations
- **Derivation**:
  $$P(5, 4) = \frac{5!}{(5 - 4)!} = 5! = 120$$
- **Answer**: **120**.

### Q50. Degree of Differential Equation
- **Derivation**:
  - Highest order derivative is $\frac{d^2 y}{dx^2}$, which appears raised to the power 3 $\implies$ degree is 3.
- **Answer**: **3**.

### Q51. Limit Calculation
- **Derivation**:
  $$\lim_{x \to 0} \frac{\sin 5x}{\sin 2x} = \frac{5}{2} \implies a = 5, b = 2 \implies a + b = 7$$
- **Answer**: **7**.

### Q52. Circle and Line Intersection
- **Derivation**:
  - $x^2 + y^2 = 4$ has radius 2, so maximum $y$-value is 2. The line $y = 3$ does not intersect the circle $\implies 0$ points.
- **Answer**: **0**.

### Q53. Radius of Sphere
- **Derivation**:
  - Center is $(1, -2, 3)$, $d = -11$.
  - $R = \sqrt{u^2 + v^2 + w^2 - d} = \sqrt{1^2 + (-2)^2 + 3^2 - (-11)} = \sqrt{1 + 4 + 9 + 11} = \sqrt{25} = 5$.
- **Answer**: **5**.

### Q54. Sum of Roots
- **Derivation**:
  - For $x^3 - 6x^2 + 11x - 6 = 0$, sum of roots is $-(-6)/1 = 6$.
- **Answer**: **6**.
