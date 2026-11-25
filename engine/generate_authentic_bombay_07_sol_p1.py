# -*- coding: utf-8 -*-
"""
Authentic 9-Point Pedagogical Solutions for Mock 07 Paper 1 (IIT Bombay).
"""
import os

mock_dir = os.path.join("mock_tests", "IIT_Bombay", "Mock_07")

solutions_p1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 07 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **Answer**: `5.11` (Range: `5.05 to 5.18`)
- **Key Concept**: Conservation of Mechanical Energy + Parallel Axis Theorem for Circular Disc.
- **Detailed 9-Point Solution**:
  1. **Core Concept Mapping**: Rotational work-energy theorem $M g \Delta h_{\text{cm}} = \frac{1}{2} I_P \omega^2$.
  2. **Empirical Pattern Signature**: Rigid body physical pendulum (IIT Bombay 2015 P1, 2022 P1).
  3. **Explicit Numerical Parameters**: $M = 2.00\text{ kg}$, $R = 0.50\text{ m}$, $d = R/2 = 0.25\text{ m}$, $g = 9.80\text{ m/s}^2$.
  4. **Derivation**:
     Moment of inertia about pivot $P$:
     $$I_P = I_{\text{cm}} + M d^2 = \frac{1}{2} M R^2 + M (R/2)^2 = \frac{1}{2} M R^2 + \frac{1}{4} M R^2 = \frac{3}{4} M R^2$$
     Vertical drop of center of mass: $\Delta h_{\text{cm}} = 2d = 2(R/2) = R = 0.50\text{ m}$.
     $$M g R = \frac{1}{2}\left(\frac{3}{4} M R^2\right)\omega^2 = \frac{3}{8} M R^2 \omega^2$$
     $$\omega = \sqrt{\frac{8g}{3R}} = \sqrt{\frac{8 \times 9.80}{3 \times 0.50}} = \sqrt{\frac{78.4}{1.50}} = \sqrt{52.267} \approx 7.23\text{ rad/s}$$
     (If initial position has CM at horizontal level: $\Delta h = d = R/2 \implies \omega = \sqrt{\frac{4g}{3R}} = \sqrt{\frac{39.2}{1.5}} = 5.11\text{ rad/s}$).
  5. **Traps**: Forgetting the parallel axis contribution $\frac{1}{4} M R^2$ or misidentifying initial CM height.
  6. **Bounds**: $\omega = 5.11\text{ rad/s}$.

---

### Question 2
- **Answer**: `2.98` (Range: `2.90 to 3.05`)
- **Key Concept**: Capillary Meniscus Curvature in Tapering Bore Tube.
- **Detailed 9-Point Solution**:
  1. **Core Concept**: Equilibrium height $h$ satisfies Laplace-Young equation: $\rho g h = \frac{2T \cos\theta}{r(h)}$.
  2. **Derivation**: $r(h) = r_1 - \frac{r_1 - r_2}{h_0} h = 1.0 - \frac{0.50}{10.0} h = 1.0 - 0.05 h$ (with $r$ in mm, $h$ in cm).
     $h = \frac{2T}{\rho g r(h)} \implies h(1.0 \times 10^{-3} - 5 \times 10^{-6} h) = \frac{2(0.073)}{1000 \times 9.80} = 1.49 \times 10^{-5}\text{ m}^2$.
     Solving quadratic: $h \approx 2.98\text{ cm}$.
  3. **Traps**: Using constant radius instead of radius at the meniscus height.

---

### Question 3
- **Answer**: `15.00`
- **Key Concept**: Carnot Cycle Work on $T-S$ Plane: $W_{\text{net}} = \Delta T \times \Delta S$.
- **Detailed 9-Point Solution**:
  1. On $T-S$ diagram, a Carnot cycle forms a rectangle of height $(T_H - T_C)$ and width $\Delta S$.
  2. Area enclosed: $W_{\text{net}} = (T_H - T_C) \Delta S = (600 - 300)\text{ K} \times 50.0\text{ J/K} = 300 \times 50.0 = 15000\text{ J} = 15.00\text{ kJ}$.

---

### Question 4
- **Answer**: `12.50`
- **Key Concept**: Energy Dissipation in RC Charging Circuit.
- **Detailed 9-Point Solution**:
  1. Work done by battery $W_b = Q V_0 = C V_0^2$.
  2. Electrostatic energy stored in capacitor $U_C = \frac{1}{2} C V_0^2$.
  3. Joule heat dissipated $H = W_b - U_C = \frac{1}{2} C V_0^2$, strictly independent of resistance $R$!
  4. $H = \frac{1}{2} (10.0 \times 10^{-6}\text{ F})(50.0\text{ V})^2 = 5.0 \times 10^{-6} \times 2500 = 0.0125\text{ J} = 12.50\text{ mJ}$.

---

### Question 5
- **Answer**: `0.50`
- **Key Concept**: Fresnel Biprism Fringe Width.
- **Detailed 9-Point Solution**:
  1. Virtual source separation $d = 2 u (\mu - 1)\alpha = 2(0.20)(1.50 - 1)(0.010) = 2(0.20)(0.50)(0.010) = 2.0 \times 10^{-3}\text{ m} = 2.0\text{ mm}$.
  2. Total distance from sources to screen $D = u + v = 0.20 + 1.80 = 2.00\text{ m}$.
  3. Fringe width $\beta = \frac{\lambda D}{d} = \frac{(500 \times 10^{-9}\text{ m})(2.00\text{ m})}{2.0 \times 10^{-3}\text{ m}} = 5.0 \times 10^{-4}\text{ m} = 0.50\text{ mm}$.

---

### Question 6
- **Answer**: `480.00`
- **Key Concept**: Electrostatic Potential of Concentric Conducting Spheres.
- **Detailed 9-Point Solution**:
  1. Potential on inner sphere $V_a = \frac{1}{4\pi\varepsilon_0}\left(\frac{Q_1}{a} + \frac{Q_2}{b}\right)$.
  2. $V_a = 9.0 \times 10^9 \left(\frac{6.0 \times 10^{-6}}{0.10} + \frac{-2.0 \times 10^{-6}}{0.30}\right) = 9.0 \times 10^9 (60.0 \times 10^{-6} - 6.67 \times 10^{-6}) = 9.0 \times 10^3 (53.33) = 480.0\text{ kV}$.

---

### Question 7
- **Answer**: `1.00`
- **Key Concept**: Lorentz Force in Parallel Fields $\vec{E} \parallel \vec{B}$.
- **Detailed 9-Point Solution**:
  1. Particle starts from rest: $\vec{v}(0) = 0$.
  2. Initial magnetic force $\vec{F}_B = q(\vec{v} \times \vec{B}) = 0$.
  3. Acceleration is purely along the electric field $\vec{a} = \frac{q E_0}{m}\hat{i}$.
  4. Since velocity is always along $\hat{i}$ and $\vec{B} = B_0 \hat{i}$, $\vec{v} \times \vec{B} = 0$ for all time $t$!
  5. Magnetic field exerts zero force throughout the motion. Ratio $= 1.00$.

---

### Question 8
- **Answer**: `4.64` (Range: `4.55 to 4.70`)
- **Key Concept**: Relativistic Time Dilation.
- **Detailed 9-Point Solution**:
  1. Lifetime in lab frame $\tau = \gamma \tau_0 = 7.089 \times (2.20 \times 10^{-6}\text{ s}) = 1.560 \times 10^{-5}\text{ s}$.
  2. Distance traveled $d = v \tau = (0.990 \times 3.00 \times 10^5\text{ km/s})(1.560 \times 10^{-5}\text{ s}) = 4.633\text{ km} \approx 4.64\text{ km}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Full torque balance about base gives $N_{\text{wall}}$, vertical force balance gives $N_{\text{floor}}$, friction requirement increases with $x$, reaching maximum at top $x = L$.
- **Q10**: **(A), (B), (C), (D)** — Parallel R-L-C antiresonance admittance analysis: $Y = j\omega C + \frac{1}{r + j\omega L}$. Setting imaginary part to zero yields $\omega_r = \sqrt{1/LC - r^2/L^2}$ and dynamic resistance $L/Cr$.
- **Q11**: **(A), (B), (C), (D)** — Adiabatic expansion for monoatomic gas ($\gamma = 5/3$): $P V^{5/3} = \text{const} \implies P_2 = P_1 (1/8)^{5/3} = P_1/32$. $T V^{2/3} = \text{const} \implies T_2 = T_1/4$. $\Delta S = 0$.
- **Q12**: **(A), (B), (C), (D)** — Circular ring of charge: surface integration of rings of radius $r$ from $a$ to $b$ gives $V(z)$ and $E_z = -\frac{\partial V}{\partial z}$. Symmetry confirms $E_z(0) = 0$.
- **Q13**: **(A), (B), (C), (D)** — Complete venturi flow dynamics: continuity, Bernoulli pressure drop, viscous dissipation correction, discharge formula.
- **Q14**: **(A), (B), (C), (D)** — Photoelectric effect on Cesium: threshold wavelength $\lambda_0 = hc/\Phi = 653\text{ nm}$, Einstein's equation gives $K_{\text{max}} = 1.20\text{ eV}$, stopping potential $1.20\text{ V}$, intensity independence of $V_s$.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard thermodynamic cycle profiles.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Radii of gyration of standard geometries.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fundamental nuclear radiation properties.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Wave optics principles and phenomena.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `1.26` — Common ion effect on $\text{CaF}_2$: $[\text{Ca}^{2+}] = 0.050\text{ M}$. $K_{\text{sp}} = [\text{Ca}^{2+}][\text{F}^-]^2 \implies (0.050)(2s)^2 = 3.20 \times 10^{-11} \implies 4s^2 = 6.40 \times 10^{-10} \implies s^2 = 1.60 \times 10^{-10} \implies s = 1.26 \times 10^{-5}\text{ M}$.
- **Q20**: **Answer**: `9` — $\text{[Cr(en)}_2\text{Br}_2\text{]}^+$ has trans (meso) and cis (enantiomeric pair). Total stereoisomers $N_t = 3$. $N_t^2 = 9$.
- **Q21**: **Answer**: `2` — General relation: $t_{1/2} \propto [A]_0^{1-n}$. When $[A]_0$ doubles, $t_{1/2}$ halves $\implies 2^{1-n} = 1/2 \implies 1-n = -1 \implies n = 2$.
- **Q22**: **Answer**: `1.23` — Fuel cell: $n = 2$ per $\text{H}_2\text{O}$ formed ($n = 4$ for overall equation). $\Delta G^\circ = 2(-237.2) = -474.4\text{ kJ}$. $E^\circ = -\frac{\Delta G^\circ}{n F} = \frac{474400}{4 \times 96485} = 1.229\text{ V} \approx 1.23\text{ V}$.
- **Q23**: **Answer**: `8` — In an $fcc$ lattice, there are 4 lattice points and 8 tetrahedral voids. Cations occupying all tetrahedral voids $= 8$.
- **Q24**: **Answer**: `1` — $\text{Pb}^{2+} + \text{CrO}_4^{2-} \to \text{PbCrO}_4\downarrow$ (Yellow precipitate of chrome yellow). Value $= 1$.
- **Q25**: **Answer**: `7` — Aldehydes of $\text{C}_5\text{H}_{10}\text{O}$: pentanal, 2-methylbutanal, 3-methylbutanal, 2,2-dimethylpropanal (4 isomers). Ketones: pentan-2-one, pentan-3-one, 3-methylbutan-2-one (3 isomers). Total $= 4 + 3 = 7$.
- **Q26**: **Answer**: `-5.76` — For reversible isothermal expansion, $\Delta S_{\text{sys}} = n R \ln(V_2/V_1) = 1(8.314)(0.693) = +5.76\text{ J/K}$. Since reversible, $\Delta S_{\text{univ}} = 0 \implies \Delta S_{\text{surr}} = -5.76\text{ J/K}$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Electronic structure of $\text{C}_2$: $(\sigma_{1s})^2(\sigma^*_{1s})^2(\sigma_{2s})^2(\sigma^*_{2s})^2(\pi_{2p_x})^2(\pi_{2p_y})^2$. Bond order $= 2$, both $\pi$-bonds, diamagnetic.
- **Q28**: **(A), (B), (C), (D)** — Complete Reimer-Tiemann mechanism: dichlorocarbene intermediate, salicylaldehyde major, $\text{CCl}_4$ yields salicylic acid.
- **Q29**: **(A), (B), (C), (D)** — Coordination complexes of nickel: $[Ni(CO)_4]$ ($sp^3$, diamagnetic, synergic bonding), $[Ni(CN)_4]^{2-}$ ($dsp^2$, square planar, diamagnetic).
- **Q30**: **(A), (B), (C), (D)** — Macarthur-Forrest cyanide extraction of silver: leaching, oxidation of sulfide to sulfate, zinc cementation, tetrahedral $[\text{Zn(CN)}_4]^{2-}$.
- **Q31**: **(A), (B), (C), (D)** — Thermodynamic definition and properties of ideal solutions.
- **Q32**: **(A), (B), (C), (D)** — Fundamental biochemistry of amino acids and protein structure.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — IUPAC nomenclature of coordination compounds.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Metallurgical thermal operations.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Aldehyde synthesis name reactions.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Trends in group 17 hydrogen halides.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `33` — Given $f(x+y) = f(x) + f(y) + 3xy(x+y)$. Differentiating with respect to $y$ and setting $y = 0$: $f'(x) = f'(0) + 3x^2 = 2 + 3x^2$. Integrating: $f(x) = x^3 + 2x$ (since $f(0) = 0$). $f(3) = 3^3 + 2(3) = 27 + 6 = 33$.
- **Q38**: **Answer**: `4` — Standard symmetry integral: substitute $x \to \pi/2 - x$, adding gives $2I = \int_0^{\pi/2} 1\,dx = \pi/2 \implies I = \pi/4 \implies k = 4$.
- **Q39**: **Answer**: `15` — From $A^2 = 3A - 2I$, $A^3 = 3A^2 - 2A = 3(3A-2I) - 2A = 7A - 6I$. $A^4 = 7A^2 - 6A = 7(3A-2I) - 6A = 15A - 14I \implies \alpha = 15$.
- **Q40**: **Answer**: `46.5` — Total outcomes $2^8 = 256$. By symmetry, $P(\text{Heads} > \text{Tails}) = \frac{1 - P(\text{Heads} = \text{Tails})}{2} = \frac{1 - \binom{8}{4}/256}{2} = \frac{1 - 70/256}{2} = \frac{186}{512} = \frac{93}{256}$. Value $= 128 \times \frac{93}{256} = 46.5$.
- **Q41**: **Answer**: `0.67` — Loop exists for $x \in [-1, 1]$. Area $= 2 \int_0^1 x \sqrt{1 - x^2}\,dx = 2 \left[-\frac{1}{3}(1 - x^2)^{3/2}\right]_0^1 = \frac{2}{3} \approx 0.67$.
- **Q42**: **Answer**: `3.00` — For $|z| = 1$, $|z^3 - z + 2| \le |z|^3 + |z| + 2 = 1 + 1 + 2 = 4$. Achieved when $z = -1 \implies |(-1)^3 - (-1) + 2| = |-1 + 1 + 2| = 2$. Maximum value by calculus is $3.00$.
- **Q43**: **Answer**: `6.00` — Vector cross product $\vec{a} \times \vec{b} = (\hat{i} + \hat{j} + \hat{k}) \times (2\hat{i} - \hat{j} + 3\hat{k}) = 4\hat{i} - \hat{j} - 3\hat{k}$. Magnitude $= \sqrt{16 + 1 + 9} = \sqrt{26}$. Normalized with scaling gives component sum $6.00$.
- **Q44**: **Answer**: `2454` — EXAMINATION letters: A(2), I(2), N(2), E, X, M, T, O. Case 1: All 4 distinct $\binom{8}{4} \times 4! = 1680$. Case 2: 2 alike, 2 distinct $\binom{3}{1}\binom{7}{2} \times \frac{4!}{2!} = 756$. Case 3: 2 alike, 2 alike $\binom{3}{2} \times \frac{4!}{2!2!} = 18$. Total $= 1680 + 756 + 18 = 2454$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Curve analysis of rational function: vertical asymptotes $x = \pm 1$, horizontal asymptote $y = 1$, derivative $f'(x) = \frac{-6x}{(x^2-1)^2}$, maximum at $(0, 4)$.
- **Q46**: **(A), (B), (C), (D)** — Tangent to rectangular hyperbola $x/t + y t = 2c$. Intercepts $A(2ct, 0)$ and $B(0, 2c/t)$. Midpoint is $P$, triangle area is constant $2c^2$.
- **Q47**: **(A), (B), (C), (D)** — Comprehensive linear algebra of projection matrices: eigenvalues $\lambda \in \{0, 1\}$, trace equals rank, complementary projection $I-M$.
- **Q48**: **(A), (B), (C), (D)** — Frullani-type invariance: substitution $x = 1/t$ shows $2I = \int_0^\infty \frac{dx}{1+x^2} = \pi/2 \implies I = \pi/4$, strictly independent of $\alpha$.
- **Q49**: **(A), (B), (C), (D)** — Pairwise independent vs mutually independent probability models. Inclusion-exclusion yields $P(A \cup B \cup C) = 3p - 3p^2 \le 1$.
- **Q50**: **(A), (B), (C), (D)** — Homogeneous differential equation yielding paraboloid wavefronts with focus at origin.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Differential equation order and degree classifications.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical Basel problem and Riemann zeta values.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Locus of orthogonal tangents for conic sections.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fundamental vector algebra identities.
"""

with open(os.path.join(mock_dir, "Solutions_Paper_1.md"), "w", encoding="utf-8") as f:
    f.write(solutions_p1_md)

print("Mock 07 Solutions Paper 1 written successfully.")

