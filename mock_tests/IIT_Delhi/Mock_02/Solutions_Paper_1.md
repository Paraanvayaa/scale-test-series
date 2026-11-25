# Detailed Pedagogical Solutions — Mock Examination 02 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Variable Mass Systems, Impulse-Momentum Theorem, Work-Energy Principle for Dissipative Systems ($W_{\text{motor}} = \Delta K + Q_{\text{heat}}$).
- **2. IIT Historical Signature**: Classic momentum flow problem with vertical mass deposition onto horizontal conveyor belt.
- **3. Derivation**:
  - Sand drops with zero horizontal velocity. To accelerate mass $dm$ to speed $v$, horizontal impulse required is $d p_x = (dm)v$.
  - Force exerted by belt: $F = \frac{dp_x}{dt} = v \frac{dm}{dt} = \mu v$. (A) is correct.
  - Power delivered by motor: $P = F v = (\mu v)v = \mu v^2$. (B) is correct.
  - Kinetic energy gained by sand per second: $\frac{dK}{dt} = \frac{1}{2}\left(\frac{dm}{dt}\right)v^2 = \frac{1}{2}\mu v^2$. (C) is correct.
  - Rate of energy dissipated as heat: $P_{\text{diss}} = P_{\text{motor}} - \frac{dK}{dt} = \mu v^2 - \frac{1}{2}\mu v^2 = \frac{1}{2}\mu v^2$. Exactly half the energy is lost to heat. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Capacitance with Partially Inserted Dielectric, Electrostatic Forces at Constant Potential ($F = \frac{1}{2}V_0^2 \frac{dC}{dx}$).
- **2. Derivation**:
  - System consists of two capacitors in parallel: $C(x) = \frac{\varepsilon_0 K w x}{d} + \frac{\varepsilon_0 w (L - x)}{d} = \frac{\varepsilon_0 w}{d}[(K-1)x + L]$. (A) is correct.
  - At constant battery potential $V_0$, electrostatic force:
    $$F = \frac{1}{2}V_0^2 \frac{dC}{dx} = \frac{1}{2}V_0^2 \frac{\varepsilon_0 w(K-1)}{d} = \frac{1}{2}(K-1)\frac{\varepsilon_0 w V_0^2}{d}$$
    (B) is correct.
  - The force is constant, independent of $x$ for $0 < x < L$. (C) is correct.
  - Since force is constant (not proportional to displacement $-x$), the slab undergoes constant acceleration, not simple harmonic motion. Thus (D) is incorrect.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Real Gases, van der Waals Equation, Critical Constants, Inversion Temperature.
- **2. Derivation**:
  - Critical constants: $T_c = \frac{8a}{27Rb}$, $P_c = \frac{a}{27b^2}$, $V_c = 3b$. (A) and (B) are correct.
  - Critical compressibility factor: $Z_c = \frac{P_c V_c}{R T_c} = \frac{(a/27b^2)(3b)}{R(8a/27Rb)} = \frac{3a/27b}{8a/27b} = \frac{3}{8} = 0.375$. (C) is correct.
  - Joule-Thomson inversion temperature: $T_i = \frac{2a}{Rb}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Faraday's Law of Induction, Alternating Current Generation, Magnetic Torque.
- **2. Derivation**:
  - Area of semicircle: $A = \frac{1}{2}\pi R^2$.
  - Flux: $\Phi(t) = B A \cos(\omega t) = \frac{1}{2}\pi R^2 B \cos(\omega t)$. (A) is correct.
  - Induced EMF: $\mathcal{E}(t) = -\frac{d\Phi}{dt} = \frac{1}{2}\pi R^2 B \omega \sin(\omega t) \implies \mathcal{E}_0 = \frac{1}{2}\pi R^2 B \omega$. (B) is correct.
  - Average power: $P_{\text{avg}} = \frac{\mathcal{E}_0^2}{2r} = \frac{(\frac{1}{2}\pi R^2 B \omega)^2}{2r} = \frac{\pi^2 R^4 B^2 \omega^2}{8r}$. (C) is correct.
  - Torque $\tau(t) = \vec{\mu} \times \vec{B}$ fluctuates with time as $\sin^2(\omega t)$, requiring time-dependent mechanical torque. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Wave Optics, Thin Film Interference, Phase Changes on Reflection.
- **2. Derivation**:
  - $\mu_{\text{air}} < \mu_{\text{oil}} \implies$ reflection at upper interface has phase shift $\pi$. (A) is correct.
  - $\mu_{\text{oil}} = 1.40 > \mu_{\text{water}} = 1.33 \implies$ reflection at lower interface has phase shift 0. (B) is correct.
  - Net relative phase difference: $\Delta \phi = \frac{2\pi}{\lambda}(2\mu t) + \pi$.
  - Constructive interference condition: $\Delta \phi = 2m\pi \implies 2\mu t = \left(m - \frac{1}{2}\right)\lambda = \left(k + \frac{1}{2}\right)\lambda$. (C) is correct.
  - For $t = 280\text{ nm}, \mu = 1.40$: $2\mu t = 2(1.40)(280) = 784\text{ nm}$.
  - For $k = 1$: $\lambda = \frac{784}{1.5} \approx 522.7\text{ nm} \approx 523\text{ nm}$ (visible green light). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Relativistic Kinematics, Invariant Mass $s = (p_1 + p_2)^2$, Threshold Energy.
- **2. Derivation**:
  - At threshold, all four final particles are at rest in the CM frame: $s = (4 m_p c^2)^2 = 16 m_p^2 c^4$. (A) is correct.
  - In laboratory frame where target is stationary:
    $$s = (p_1 + p_2)^2 = m_p^2 c^4 + m_p^2 c^4 + 2(E_{\text{th}} m_p c^2) = 2 m_p^2 c^4 + 2 E_{\text{th}} m_p c^2$$
  - Equating: $2 m_p^2 c^4 + 2 E_{\text{th}} m_p c^2 = 16 m_p^2 c^4 \implies 2 E_{\text{th}} m_p c^2 = 14 m_p^2 c^4 \implies E_{\text{th}} = 7 m_p c^2$. (B) is correct.
  - Kinetic energy: $K_{\text{th}} = E_{\text{th}} - m_p c^2 = 7 m_p c^2 - m_p c^2 = 6 m_p c^2$. (C) is correct.
  - Numerical value: $K_{\text{th}} = 6(0.938) \approx 5.63\text{ GeV}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Moment of inertia of disk about central axis: $I = \frac{1}{2}M R^2 = \frac{1}{2}(2.00)(0.20)^2 = 0.040\text{ kg}\cdot\text{m}^2$. Time period: $T = 2\pi\sqrt{\frac{I}{\kappa}} = 2\pi\sqrt{\frac{0.040}{0.80}} = 2\pi\sqrt{0.05} = 2(3.1416)(0.2236) \approx 1.405\text{ s} \approx 1.41\text{ s}$. Exact: `1.41`.
- **Question 8**: Rotating spherical shell: $\mu_m = \frac{1}{3} Q R^2 \omega = \frac{1}{3}(6.00 \times 10^{-6})(0.10)^2(100.0) = \frac{1}{3}(6.00 \times 10^{-6})(0.01)(100) = 2.00 \times 10^{-6}\text{ A}\cdot\text{m}^2 = 2.00\ \mu\text{A}\cdot\text{m}^2$. Exact: `2.00`.
- **Question 9**: Thermal resistance between concentric spheres: $R_{\text{th}} = \frac{1}{4\pi K}\left(\frac{1}{r_1} - \frac{1}{r_2}\right) = \frac{1}{4\pi (0.50)}\left(\frac{1}{0.05} - \frac{1}{0.15}\right) = \frac{1}{2\pi}(20 - 6.667) = \frac{13.333}{2\pi} \approx 2.122\text{ K/W}$.
  Heat current $\dot{Q} = \frac{\Delta T}{R_{\text{th}}} = \frac{100}{2.122} \approx 47.12\text{ W}$. Exact: `47.12`.
- **Question 10**: $\mu = \frac{\sin((A+\delta_m)/2)}{\sin(A/2)} \implies \sqrt{3} = \frac{\sin((60^\circ+\delta_m)/2)}{\sin(30^\circ)} = \frac{\sin((60^\circ+\delta_m)/2)}{0.5} \implies \sin((60^\circ+\delta_m)/2) = \frac{\sqrt{3}}{2} \implies \frac{60^\circ+\delta_m}{2} = 60^\circ \implies \delta_m = 60^\circ$. Exact: `60.00`.
- **Question 11**: $\Delta\lambda = \lambda_c (1 - \cos 90^\circ) = \lambda_c = 0.00243\text{ nm}$. Fractional increase: $\frac{\Delta\lambda}{\lambda} = \frac{0.00243}{0.0200} = 0.1215 = 12.15\%$. Exact: `12.15`.
- **Question 12**: Quality factor: $Q = \frac{\sqrt{mk}}{b} = \frac{\sqrt{0.20 \times 80.0}}{0.040} = \frac{\sqrt{16.0}}{0.040} = \frac{4.0}{0.040} = 100.00$. Exact: `100.00`.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $F = -\frac{dU}{dx} = -\left(-\frac{2a}{x^3} + \frac{b}{x^2}\right) = \frac{2a}{x^3} - \frac{b}{x^2} = 0 \implies \frac{2a}{x^3} = \frac{b}{x^2} \implies x_0 = \frac{2a}{b}$. Option (A).
- **Question 14**: $I = \int_0^R J(r)(2\pi r dr) = 2\pi J_0 \int_0^R \left(r - \frac{r^2}{R}\right)dr = 2\pi J_0 \left(\frac{R^2}{2} - \frac{R^2}{3}\right) = 2\pi J_0 \left(\frac{R^2}{6}\right) = \frac{1}{3}\pi R^2 J_0$. Option (A).
- **Question 15**: $P V^\gamma = \text{const} \implies dP V^\gamma + \gamma P V^{\gamma-1} dV = 0 \implies -V \frac{dP}{dV} = \gamma P$. Hence $B_s = \gamma P$. Option (A).
- **Question 16**: $\theta_{\text{min}} = \frac{1.22\lambda}{D} = \frac{1.22(600 \times 10^{-9})}{2.44} = \frac{732 \times 10^{-9}}{2.44} = 3.0 \times 10^{-7}\text{ rad}$. Option (A).
- **Question 17**: $A(t) = A_0 (1/2)^{t/T_{1/2}} \implies \frac{100}{1600} = \frac{1}{16} = \left(\frac{1}{2}\right)^4 \implies \frac{8\text{ h}}{T_{1/2}} = 4 \implies T_{1/2} = 2\text{ hours}$. Option (A).
- **Question 18**: $d_{\text{app}} = \frac{d_1}{\mu_1} + \frac{d_2}{\mu_2} = \frac{12}{4/3} + \frac{6}{1.5} = 9 + 4 = 13\text{ cm}$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: $\text{B}_2\text{H}_6$ has 4 terminal $2c-2e$ bonds and 2 bridging $3c-2e$ bonds. Both borons are $sp^3$ hybridized. The two bridging hydrogens lie in a perpendicular plane above and below the plane containing the four terminal hydrogens and borons. Options: (A), (B), (C).
- **Question 20**: Reimer-Tiemann reaction generates $:\text{CCl}_2$ by $\alpha$-elimination from chloroform, attacking phenol to yield salicylaldehyde. $\text{CCl}_4$ yields salicylic acid. Options: (A), (B), (C), (D).
- **Question 21**: Nernst equation: $E = E^\circ - \frac{0.0591}{2}\log\frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]}$. Increasing $[\text{Cu}^{2+}]$ increases EMF, increasing $[\text{Zn}^{2+}]$ decreases it. At equilibrium, $E = 0$. $\Delta G^\circ = -nFE^\circ$. Options: (A), (B), (C), (D).
- **Question 22**: Aldol condensation requires $\alpha$-hydrogen atoms. Acetaldehyde ($\text{CH}_3\text{CHO}$) and acetone ($\text{CH}_3\text{COCH}_3$) have $\alpha$-hydrogens. Benzaldehyde and trimethylacetaldehyde lack $\alpha$-hydrogens. Options: (A), (B).
- **Question 23**: Across a period, $Z_{\text{eff}}$, electronegativity, and ionization energy generally increase, while atomic radius decreases. Options: (A), (B), (C).
- **Question 24**: Phenylalanine, tyrosine, and tryptophan have aromatic side chains (phenyl, 4-hydroxyphenyl, and indole). Alanine has a methyl side chain. Options: (A), (B), (C).
- **Question 25**: In $0.010\text{ M Na}_2\text{SO}_4$, $[\text{SO}_4^{2-}] = 0.010\text{ M}$. $S = \frac{K_{sp}}{[\text{SO}_4^{2-}]} = \frac{1.0 \times 10^{-10}}{1.0 \times 10^{-2}} = 1.0 \times 10^{-8}\text{ mol/L} \implies m = 8$. Exact: `8.00`.
- **Question 26**: For second-order reaction: $t_{1/2} = \frac{1}{k [A]_0} = \frac{1}{(0.040)(0.50)} = \frac{1}{0.020} = 50.00\text{ s}$. Exact: `50.00`.
- **Question 27**: For BCC: $\sqrt{3}a = 4r \implies r = \frac{\sqrt{3}a}{4} = \frac{1.732 \times 300}{4} = 129.90\text{ pm}$. Exact: `129.90`.
- **Question 28**: $\Delta_f H^\circ(\text{CH}_4) = \Delta_{\text{comb}} H^\circ(\text{C}) + 2\Delta_{\text{comb}} H^\circ(\text{H}_2) - \Delta_{\text{comb}} H^\circ(\text{CH}_4) = -393.5 + 2(-285.8) - (-890.3) = -393.5 - 571.6 + 890.3 = -74.8\text{ kJ/mol}$. Exact: `-74.80` (or `74.80` magnitude). Let's take `74.80`.
- **Question 29**: $\Delta T_b = 100.050 - 100.000 = 0.050\text{ K}$. $\Delta T_b = i K_b m \implies 0.050 = i (0.512)(0.050) \implies i = \frac{1}{0.512} \approx 1.95$. Exact: `1.95`.
- **Question 30**: $[Co(en)_2Cl_2]^+$ exists as trans (achiral, 1 isomer) and cis (chiral enantiomeric pair, 2 isomers). Total stereoisomers = $1 + 2 = 3$. Exact: `3.00`.
- **Question 31**: Protonation of oxygen followed by $S_N2$ attack of $I^-$ on the less hindered methyl carbon gives phenol and iodomethane. Option (A).
- **Question 32**: $\text{H}_3\text{PO}_2$: $3(+1) + x + 2(-2) = 0 \implies x - 1 = 0 \implies x = +1$. Option (A).
- **Question 33**: Zinc dust reduces $\text{Au}^+$ in $[Au(CN)_2]^-$ to metallic gold: $2[Au(CN)_2]^- + \text{Zn} \to [\text{Zn}(CN)_4]^{2-} + 2\text{Au}$. Option (A).
- **Question 34**: Glucose contains an aldehyde group (reducing sugar) and reduces Tollens' reagent to form a silver mirror. Option (A).
- **Question 35**: $\text{SF}_6$ has 6 bonding pairs and 0 lone pairs $\implies sp^3d^2$ hybridization. Option (A).
- **Question 36**: Buna-S is a copolymer of 1,3-butadiene and styrene. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f'(x) = \frac{1 - \ln x}{x^2} = 0 \implies x = e$. Maximum value $= \frac{1}{e}$. Since $f(e) > f(\pi)$, $\frac{\ln e}{e} > \frac{\ln \pi}{\pi} \implies \pi \ln e > e \ln \pi \implies \ln(e^\pi) > \ln(\pi^e) \implies e^\pi > \pi^e$. $\lim_{x \to \infty} \frac{\ln x}{x} = 0$. Options: (A), (B), (C), (D).
- **Question 38**: Invertible matrices obey $\det(AB) = \det(A)\det(B)$, $(AB)^{-1} = B^{-1}A^{-1}$, $\text{adj}(AB) = \text{adj}(B)\text{adj}(A)$, and $\det(\text{adj}(A)) = (\det A)^{n-1}$. Options: (A), (B), (C), (D).
- **Question 39**: Tangent formula: $xx_1 + yy_1 = r^2 \implies 3x + 4y = 25$ touches at $(3, 4)$. Normal passes through center $(0,0)$ with slope $4/3 \implies 4x - 3y = 0$. Length of tangent from $(5,5) = \sqrt{25 + 25 - 25} = 5$. Chord of contact: $5x + 5y = 25 \implies x + y = 5$. Options: (A), (B), (C), (D).
- **Question 40**: Auxiliary equation: $m^2 + 4 = 0 \implies m = \pm 2i$. General solution: $y = C_1\cos(2x) + C_2\sin(2x)$. Initial conditions: $y(0) = C_1 = 1$; $y'(0) = 2C_2 = 2 \implies C_2 = 1$. Solution: $y = \cos(2x) + \sin(2x)$. Amplitude $= \sqrt{1^2+1^2} = \sqrt{2}$. Period $= 2\pi/2 = \pi$. Options: (A), (B), (C), (D).
- **Question 41**: For unit vectors: $|\vec{a}+\vec{b}| = \sqrt{1 + 1 + 2\cos\theta} = \sqrt{2(1+\cos\theta)} = 2\cos(\theta/2)$. $|\vec{a}-\vec{b}| = 2\sin(\theta/2)$. $(\vec{a}+\vec{b})\cdot(\vec{a}-\vec{b}) = |\vec{a}|^2 - |\vec{b}|^2 = 1 - 1 = 0$. $\vec{a}+\vec{b}$ bisects the angle. Options: (A), (B), (C), (D).
- **Question 42**: For Poisson with $\lambda = 2$: mean $= 2$, variance $= 2$, $P(X=0) = \frac{e^{-2}2^0}{0!} = e^{-2}$, $P(X=1) = \frac{e^{-2}2^1}{1!} = 2e^{-2}$. Options: (A), (B), (C), (D).
- **Question 43**: $L = \lim_{x \to 0} \exp\left(\frac{\ln(\sin x / x)}{x^2}\right)$. Using Taylor series: $\frac{\sin x}{x} = 1 - \frac{x^2}{6}$, so $\ln(1 - x^2/6) \approx -\frac{x^2}{6}$. Thus exponent is $-\frac{x^2/6}{x^2} = -\frac{1}{6}$. $L = e^{-1/6} \implies k = 6$. Exact: `6.00`.
- **Question 44**: By AM-GM inequality, $x + \frac{4}{x} \ge 2\sqrt{x \cdot \frac{4}{x}} = 4.00$, with equality at $x = 2$. Exact: `4.00`.
- **Question 45**: Using Beta function: $\int_0^1 x^1 (1-x)^9 dx = B(2, 10) = \frac{\Gamma(2)\Gamma(10)}{\Gamma(12)} = \frac{1! 9!}{11!} = \frac{1}{11 \times 10} = \frac{1}{110}$. Thus $m = 110$. Exact: `110.00`.
- **Question 46**: Second plane: $2x - y + 2z + 9 = 0$. Distance $d = \frac{|9 - 3|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{6}{\sqrt{9}} = \frac{6}{3} = 2.00$. Exact: `2.00`.
- **Question 47**: $a_n = S_n - S_{n-1} = (3n^2 + 5n) - [3(n-1)^2 + 5(n-1)] = 6n + 2$. For $n = 10$: $a_{10} = 6(10) + 2 = 62.00$. Exact: `62.00`.
- **Question 48**: Treat the 2 particular persons as 1 block: $(5 - 1)! = 4! = 24$. The 2 persons can arrange among themselves in $2! = 2$ ways. Total circular arrangements $= 24 \times 2 = 48$. Exact: `48.00`.
- **Question 49**: $y = x^3 - 3x + 1$. At $x = 2$, $y = 8 - 6 + 1 = 3$. Slope $y' = 3x^2 - 3 = 12 - 3 = 9$. Equation: $y - 3 = 9(x - 2) \implies y - 3 = 9x - 18 \implies 9x - y - 15 = 0$. Option (A).
- **Question 50**: For independent events, $P(A \cap B) = P(A)P(B) = 0.4 \times 0.5 = 0.2$. $P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.4 + 0.5 - 0.2 = 0.70$. Option (A).
- **Question 51**: General term $T_{r+1} = \binom{9}{r}(x^2)^{9-r}(-1/x)^r = (-1)^r \binom{9}{r} x^{18-3r}$. For constant term: $18 - 3r = 0 \implies r = 6$. Coefficient $= (-1)^6 \binom{9}{6} = \binom{9}{3} = \frac{9 \times 8 \times 7}{6} = 84$. Option (A).
- **Question 52**: First line: $6x + 8y - 18 = 0$. Second line: $6x + 8y + 7 = 0$. Distance $d = \frac{|7 - (-18)|}{\sqrt{6^2 + 8^2}} = \frac{25}{10} = 2.5$. Option (A).
- **Question 53**: $\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -1 & 1 \\ 3 & 4 & -1 \end{vmatrix} = \hat{i}(1 - 4) - \hat{j}(-2 - 3) + \hat{k}(8 + 3) = -3\hat{i} + 5\hat{j} + 11\hat{k}$. Magnitude $= \sqrt{9 + 25 + 121} = \sqrt{155}$. Unit vector $= \frac{-3\hat{i} + 5\hat{j} + 11\hat{k}}{\sqrt{155}}$. Option (A).
- **Question 54**: $\tan x - \sin x = \sin x\left(\frac{1}{\cos x} - 1\right) = \tan x(1 - \cos x) = x \left(\frac{x^2}{2}\right) = \frac{x^3}{2}$. Limit is $1/2$. Option (A).
