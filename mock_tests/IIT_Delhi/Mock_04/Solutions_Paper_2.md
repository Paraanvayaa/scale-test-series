# Detailed Pedagogical Solutions — Mock Examination 04 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rolling vs Slipping on Incline, Friction Angle, Dynamic vs Static Equations.
- **2. Derivation**:
  - Pure rolling: $M g \sin\theta - f_s = M a_c$, $f_s R = \left(\frac{2}{5}MR^2\right)\alpha \implies f_s = \frac{2}{5}M a_c$.
  - $a_c = \frac{5}{7}g\sin\theta$. (B) is correct.
  - $f_s = \frac{2}{7}Mg\sin\theta$. (C) is correct.
  - No slipping condition: $f_s \le \mu_s N = \mu_s M g \cos\theta \implies \frac{2}{7}Mg\sin\theta \le \mu_s M g \cos\theta \implies \mu_s \ge \frac{2}{7}\tan\theta$. (A) is correct.
  - If $\mu_s < \frac{2}{7}\tan\theta$, slipping occurs with kinetic friction $f_k = \mu_k M g \cos\theta \implies a_c = g(\sin\theta - \mu_k\cos\theta)$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Non-Uniform Dielectric Slab in Capacitor, Continuous Series Integration.
- **2. Derivation**:
  - Infinitesimal series element: $d\left(\frac{1}{C}\right) = \frac{dx}{\varepsilon_0 \varepsilon_r(x) A}$.
  - $\frac{1}{C} = \int_0^d \frac{dx}{\varepsilon_0 A (1 + \alpha x)} = \frac{1}{\varepsilon_0 A \alpha} \ln(1 + \alpha d)$.
  - Thus $C = \frac{\varepsilon_0 A \alpha}{\ln(1 + \alpha d)}$. (B) is correct.
  - As $\alpha \to 0$, $\ln(1+\alpha d) \approx \alpha d$, so $C \to \frac{\varepsilon_0 A}{d}$. (C) is correct.
  - In a 1D parallel plate configuration without free charges inside the dielectric, the displacement field $\vec{D}$ is divergence-free, so $D = \sigma_{\text{free}} = \text{const}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Acoustic Standing Waves in Open Organ Pipes, End Correction.
- **2. Derivation**:
  - Resonant frequencies: $\nu_n = \frac{n v}{2L}$. (A) is correct.
  - At open ends, air is free to oscillate $\implies$ displacement antinodes, pressure nodes. (B) is correct.
  - Open pipes support all harmonics $n = 1, 2, 3, \dots$. (C) is correct.
  - With Rayleigh end correction $e = 0.6r$ at each open end, $L_{\text{eff}} = L + 2e = L + 1.2r$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Ampere's Circuital Law for Coaxial Cables, Inductance per Unit Length.
- **2. Derivation**:
  - For $r < a$: $B(2\pi r) = \mu_0 I \frac{\pi r^2}{\pi a^2} \implies B(r) = \frac{\mu_0 I r}{2\pi a^2}$. (A) is correct.
  - For $a < r < b$: $B(2\pi r) = \mu_0 I \implies B(r) = \frac{\mu_0 I}{2\pi r}$. (B) is correct.
  - For $r > b$: net enclosed current $I - I = 0 \implies B = 0$. (C) is correct.
  - Self-inductance per unit length from field between conductors:
    $$U' = \int_a^b \frac{B^2}{2\mu_0} (2\pi r dr) = \frac{\mu_0 I^2}{4\pi}\ln\left(\frac{b}{a}\right) = \frac{1}{2} L' I^2 \implies L' = \frac{\mu_0}{2\pi}\ln\left(\frac{b}{a}\right)$$
    (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: X-Ray Physics, Duane-Hunt Law, Moseley's Law.
- **2. Derivation**:
  - Duane-Hunt cutoff: $\lambda_{\text{min}} = \frac{hc}{e V_0}$. (A) is correct.
  - Characteristic lines arise from electron transitions into inner shell vacancies. (B) is correct.
  - Moseley's law: $\sqrt{\nu} = a(Z - b)$, with $b = 1$ for $K_\alpha$. (C) is correct.
  - Filament current controls number of emitted electrons (intensity) without changing electron energy ($e V_0$), leaving $\lambda_{\text{min}}$ unchanged. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Heat Pump Thermodynamics, COP, Second Law of Thermodynamics.
- **2. Derivation**:
  - $\text{COP}_{\text{HP}} = \frac{Q_H}{W} = \frac{T_H}{T_H - T_C} = \frac{290}{30} \approx 9.67$. (A) is correct.
  - Heat delivered $= \text{COP} \times W = 9.67(1.0\text{ kJ}) = 9.67\text{ kJ}$. (B) is correct.
  - First law: $Q_H = Q_C + W \implies Q_C = Q_H - W$. (C) is correct.
  - Reversible cycle has $\Delta S_{\text{univ}} = 0$, satisfying second law. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: $U(x) = \frac{1}{2} k x^2 = 50.0 x^2 \implies k = 100.0\text{ N/m}$.
  Time period: $T = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{0.20}{100.0}} = 2\pi\sqrt{0.002} = 2(3.1416)(0.04472) \approx 0.28\text{ s}$. Exact: `0.28`.
- **Question 8**: Electric field between plates: $E = \frac{\sigma}{\varepsilon_0} = \frac{4.0 \times 10^{-6}}{8.85 \times 10^{-12}} \approx 4.52 \times 10^5\text{ V/m}$.
  Potential difference: $V = E d = (4.52 \times 10^5)(5.0 \times 10^{-3}) = 2260\text{ V}$. Exact: `2260.00`.
- **Question 9**: Fringe width $\beta = \frac{\lambda D}{d} = \frac{(600 \times 10^{-9})(1.20)}{0.30 \times 10^{-3}} = 2.40\text{ mm}$.
  Fourth dark fringe is at $y = (4 - 1/2)\beta = 3.5 \beta = 3.5(2.40) = 8.40\text{ mm}$. Exact: `8.40`.
- **Question 10**: $v_{\text{rms}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3(8.314)(300)}{0.004}} = \sqrt{1870650} \approx 1367.7\text{ m/s} \approx 1368\text{ m/s}$. Exact: `1368.00`.
- **Question 11**: $Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{10.0}\sqrt{\frac{0.10}{10.0 \times 10^{-6}}} = \frac{1}{10.0}\sqrt{10000} = \frac{100}{10.0} = 10.00$. Exact: `10.00`.
- **Question 12**: $\text{BE/nucleon} = \frac{28.30\text{ MeV}}{4} = 7.075\text{ MeV} \approx 7.08\text{ MeV}$. Exact: `7.08`.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 14**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 15**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 16**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 17**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 18**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Seesaw geometry arises from $AX_4E$ configuration (5 electron pairs, 1 lone pair): $\text{SF}_4, \text{XeO}_2\text{F}_2, \text{IF}_4^+$ all have seesaw shape. $\text{XeF}_4$ is square planar ($AX_4E_2$). Options: (A), (B), (C).
- **Question 20**: Hoffmann degradation (primary amide $\to$ amine), reduction of nitrobenzene, Sandmeyer reaction, and Friedel-Crafts acylation are all single-step transformations. Options: (A), (B), (C), (D).
- **Question 21**: Chemisorption involves chemical bond formation, high specificity, monolayer formation, and high enthalpy ($80-400\text{ kJ/mol}$). Options: (A), (B), (C), (D).
- **Question 22**: Coordination isomerism occurs with interchange of ligands between complex cation and complex anion. Options: (A), (B), (C), (D).
- **Question 23**: Phenolic compounds (phenol, salicylic acid, resorcinol) form colored coordination complexes with neutral $\text{FeCl}_3$. Benzyl alcohol is an aliphatic alcohol and does not give this test. Options: (A), (B), (C).
- **Question 24**: Fat-soluble vitamins are A, D, E, K. Vitamin C is water-soluble. Options: (A), (B), (C).
- **Question 25**: $[\text{OH}^-]^3 = \frac{K_{sp}}{[\text{Fe}^{3+}]} = \frac{1.0 \times 10^{-38}}{1.0 \times 10^{-3}} = 1.0 \times 10^{-35} \implies [\text{OH}^-] \approx 2.15 \times 10^{-12}\text{ M}$.
  $pOH \approx 11.67 \implies \text{pH} = 14 - 11.67 = 2.33$. Exact: `2.33`.
- **Question 26**: $r = k [A][B] \implies 1.20 \times 10^{-3} = k (0.20)(0.30) = 0.060 k \implies k = \frac{1.20 \times 10^{-3}}{0.060} = 0.020\text{ L/(mol}\cdot\text{s})$. Exact: `0.02`.
- **Question 27**: Closest approach in FCC is along face diagonal: $d = \frac{a}{\sqrt{2}} = \frac{408}{1.414} \approx 288.5\text{ pm}$. Exact: `288.50`.
- **Question 28**: $\Delta G^\circ = -n F E^\circ = -2.303 R T \log K \implies \log K = \frac{n E^\circ}{0.0591} = \frac{1(0.591)}{0.0591} = 10 \implies p = 10$. Exact: `10.00`.
- **Question 29**: $\Delta T_f = i K_f m \implies 5.022 = i (1.86)(1.0) \implies i = 2.70$.
  $i = 1 + 2\alpha \implies 2\alpha = 1.70 \implies \alpha = 85.00\%$. Exact: `85.00`.
- **Question 30**: $\text{Fe}_2(\text{CO})_9$ has 3 bridging carbonyl ligands and 6 terminal carbonyl ligands. Exact: `3.00`.
- **Question 31**: $S_N1$ reactivity follows carbocation stability: $3^\circ > 2^\circ > 1^\circ > \text{methyl}$. $\text{tert}$-Butyl bromide reacts fastest. Option (A).
- **Question 32**: $\text{H}_2\text{O}$ has extensive intermolecular hydrogen bonding, giving it the highest boiling point. Among the others, boiling point increases with molar mass (van der Waals forces): $\text{H}_2\text{S} < \text{H}_2\text{Se} < \text{H}_2\text{Te} < \text{H}_2\text{O}$. Option (A).
- **Question 33**: Combustion zone: $\text{C} + \text{O}_2 \to \text{CO}_2$. Option (A).
- **Question 34**: Sucrose is non-reducing because both anomeric carbons are linked. Option (A).
- **Question 35**: Solid $\text{N}_2\text{O}_5$ exists as $[\text{NO}_2^+][\text{NO}_3^-]$ (nitronium nitrate). Option (A).
- **Question 36**: Acetylsalicylic acid. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(x) = |x| + |x-1|$ is continuous everywhere, non-differentiable at sharp corners $x = 0, 1$. Minimum value is 1 on $[0, 1]$. $\int_{-1}^2 f(x)dx = \int_{-1}^0 (1-2x)dx + \int_0^1 1 dx + \int_1^2 (2x-1)dx = [x - x^2]_{-1}^0 + 1 + [x^2 - x]_1^2 = (0 - (-2)) + 1 + (2 - 0) = 2 + 1 + 2 = 5$. Options: (A), (B), (C), (D).
- **Question 38**: Odd-dimensional skew-symmetric matrix has $\det(A) = 0$. Diagonal entries are 0. At least one eigenvalue is 0. $\det(I+A) \ge 1$ because non-zero eigenvalues are purely imaginary pairs $\pm i\lambda$, so $\det(I+A) = 1(1 + \lambda^2) \ge 1$. Options: (A), (B), (C), (D).
- **Question 39**: Tangents from directrix are perpendicular. Chord of contact is $y y_0 = 2a(x + x_0)$. If chord passes through focus $(a, 0)$, $0 = 2a(a + x_0) \implies x_0 = -a$. Director circle is directrix. Options: (A), (B), (C), (D).
- **Question 40**: Linear ODE: $\frac{dy}{dx} - \frac{y}{x} = 2x^2$. $IF = e^{\int -dx/x} = 1/x$. Solution: $\frac{y}{x} = \int 2x dx = x^2 + C \implies y = x^3 + Cx$. $y(1) = 2 \implies C = 1 \implies y = x^3 + x$. $y' = 3x^2 + 1 > 0$ (strictly increasing). Options: (A), (B), (C), (D).
- **Question 41**: $\vec{a}+\vec{b}+\vec{c} = 0 \implies |\vec{a}+\vec{b}+\vec{c}|^2 = 3 + 2(\vec{a}\cdot\vec{b} + \vec{b}\cdot\vec{c} + \vec{c}\cdot\vec{a}) = 0 \implies \vec{a}\cdot\vec{b} = -1/2$. Angle is $120^\circ$. Form equilateral triangle. $|\vec{a}\times\vec{b}| = \sin 120^\circ = \sqrt{3}/2$. Options: (A), (B), (C), (D).
- **Question 42**: Sample space has 36 outcomes. Sum = 7 has 6 outcomes $\implies 6/36 = 1/6$. Sum > 9 has 6 outcomes $(4,6), (5,5), (5,6), (6,4), (6,5), (6,6) \implies 6/36 = 1/6$. Doublets have 6 outcomes $\implies 6/36 = 1/6$. Options: (A), (B), (C), (D).
- **Question 43**: $x^2 = x \implies x = 0, 1$. $\text{Area} = \int_0^1 (x - x^2)dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6} \approx 0.17$. Exact: `0.17`.
- **Question 44**: $2x + 2y y' = 0 \implies y' = -x/y = -3/4 = -0.75$. Exact: `-0.75` (or magnitude `0.75`).
- **Question 45**: Integration by parts: $\int_0^\pi x\sin x dx = [-x\cos x]_0^\pi + \int_0^\pi \cos x dx = \pi + 0 = \pi \implies k = 1$. Exact: `1.00`.
- **Question 46**: $\vec{a} \cdot \vec{b} = (1)(0) + (1)(1) + (0)(1) = 1$. $|\vec{a}| = \sqrt{2}, |\vec{b}| = \sqrt{2}$. $\cos\theta = \frac{1}{2} \implies \theta = 60.00^\circ$. Exact: `60.00`.
- **Question 47**: $S = \frac{a}{1-r} \implies 6 = \frac{2}{1-r} \implies 1 - r = \frac{1}{3} \implies r = \frac{2}{3} \approx 0.67$. Exact: `0.67`.
- **Question 48**: Signals taking $k$ flags: $P(5, 2) + P(5, 3) + P(5, 4) + P(5, 5) = 20 + 60 + 120 + 120 = 320$. Exact: `320.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
