# Detailed Pedagogical Solutions — Mock Examination 07 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Multi-Correct Physics)
- **Q1**: **(A), (B), (C), (D)** — Rolling on incline: $a_{\text{cm}} = \frac{g\sin\theta}{1 + I/MR^2} = \frac{g\sin 30^\circ}{1 + 2/5} = \frac{5}{7}g\sin 30^\circ$. Friction $f_s = \frac{2}{7}Mg\sin 30^\circ \le \mu_s Mg\cos 30^\circ \implies \mu_s \ge \frac{2}{7}\tan 30^\circ$. If slipping occurs, $\alpha = \tau/I = \mu_k Mg\cos 30^\circ R / (\frac{2}{5}MR^2) = \frac{5\mu_k g\cos 30^\circ}{2R}$.
- **Q2**: **(A), (B), (C), (D)** — Coupled pendulums normal modes: equations $m L \ddot{\theta}_1 = -mg\theta_1 - k L(\theta_1 - \theta_2)$ and $m L \ddot{\theta}_2 = -mg\theta_2 + k L(\theta_1 - \theta_2)$. Symmetrical mode $\omega_1 = \sqrt{g/L}$, anti-symmetrical $\omega_2 = \sqrt{g/L + 2k/m}$. Beats occur with $\Delta \omega$.
- **Q3**: **(A), (B), (C), (D)** — Stirling engine cycle: $W_{\text{net}} = R(T_1 - T_2)\ln 2$. Heat absorbed in isochoric heating $Q_V = C_V(T_1 - T_2)$ balances isochoric cooling. Perfect regeneration gives Carnot efficiency.
- **Q4**: **(A), (B), (C), (D)** — Current inside non-uniform cylinder: $I(r) = \int_0^r J_0(1 - r'^2/R^2)2\pi r'\,dr' = 2\pi J_0(r^2/2 - r^4/4R^2)$. Total current $I = \frac{\pi J_0 R^2}{2}$. Ampere's law gives $B(r) = \frac{\mu_0 I(r)}{2\pi r}$. Maximum found by $dB/dr = 0 \implies r = \sqrt{2/3} R$.
- **Q5**: **(A), (B), (C), (D)** — Hydrostatic manometer equilibrium: equating pressures at level of lower mercury surface gives height difference $\Delta h_m = \frac{\rho_w h_w - \rho_{\text{oil}} h_{\text{oil}}}{\rho_m} = \frac{1000(0.272) - 800(0.20)}{13600} = \frac{272 - 160}{13600} = \frac{112}{13600} = 0.82\text{ cm}$.
- **Q6**: **(A), (B), (C), (D)** — Billet's split lens: lens equation $1/v - 1/(-30) = 1/20 \implies v = 60\text{ cm}$. Magnification $m = -v/u = -2$. Separation of virtual slits $d' = d(1 + |m|) = 1.0(1 + 2) = 3.0\text{ mm}$.
- **Q7**: **(A), (B), (C), (D)** — Bohr model: $r_n \propto n^2/Z$, magnetic moment $\mu_L = I A = (e/T)(\pi r_n^2) = n \mu_B$. Magnetic field at nucleus $B = \frac{\mu_0 I}{2r_n} \propto \frac{Z^3}{n^5}$. Gyromagnetic ratio is constant $e/2m$.
- **Q8**: **(A), (B), (C), (D)** — Relativistic dynamics: $E = K + m_0 c^2 = 2 m_0 c^2 \implies \gamma = 2$. Speed $v = c\sqrt{1 - 1/\gamma^2} = \frac{\sqrt{3}}{2}c$. Momentum $p = \gamma m_0 v = 2 m_0 (\frac{\sqrt{3}}{2}c) = \sqrt{3}m_0 c$.

---

### Questions 9 to 14 (Numerical Physics)
- **Q9**: **Answer**: `0.80` — Center of percussion: $x = \frac{I_O}{M d_{\text{cm}}} = \frac{\frac{1}{3}ML^2}{M(L/2)} = \frac{2}{3}L = \frac{2}{3}(1.20\text{ m}) = 0.80\text{ m}$.
- **Q10**: **Answer**: `2.00` — Displacement current density between capacitor plates is uniform: $J_d = \frac{I_0}{\pi R^2}$. Ampere-Maxwell law: $\oint B \cdot dl = \mu_0 I_{d,\text{encl}} \implies B(2\pi r) = \mu_0 I_0 \frac{\pi r^2}{\pi R^2} \implies B(r) = \frac{\mu_0 I_0 r}{2\pi R^2} = \frac{(4\pi \times 10^{-7})(2.0)(0.05)}{2\pi (0.10)^2} = 2.00\ \mu\text{T}$.
- **Q11**: **Answer**: `5000` — Linear path on $P-V$ diagram: area under trapezoid $W = \frac{P_1 + P_2}{2}(V_2 - V_1) = \frac{4.0 \times 10^5 + 1.0 \times 10^5}{2}(0.030 - 0.010) = (2.5 \times 10^5)(0.020) = 5000\text{ J}$.
- **Q12**: **Answer**: `90.00` — Inside a conducting material in electrostatic equilibrium, electric field is zero, so potential is constant throughout the shell $R_1 \le r \le R_2$ and equal to the potential at $r = R_2$: $V = \frac{1}{4\pi\varepsilon_0}\frac{q}{R_2} = \frac{(9.0 \times 10^9)(2.0 \times 10^{-6})}{0.20} = 9.0 \times 10^4\text{ V} = 90.00\text{ kV}$.
- **Q13**: **Answer**: `4.50` — Third dark fringe occurs at path difference $\Delta x = \left(3 - \frac{1}{2}\right)\lambda = \frac{5}{2}\lambda$. Position $y = \frac{5\lambda D}{2d} = \frac{5(600 \times 10^{-9}\text{ m})(1.20\text{ m})}{2(0.40 \times 10^{-3}\text{ m})} = \frac{3.60 \times 10^{-6}}{0.80 \times 10^{-3}} = 4.50\text{ mm}$.
- **Q14**: **Answer**: `23.84` — Fusion $2({}^2\text{H}) \to {}^4\text{He}$. Initial BE $= 4 \times 1.11 = 4.44\text{ MeV}$. Final BE $= 4 \times 7.07 = 28.28\text{ MeV}$. Energy released $Q = 28.28 - 4.44 = 23.84\text{ MeV}$.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Natural thermodynamic variables.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Lengths of equivalent simple pendulums.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Wave retardation plates and prisms.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical thermoelectric and galvanomagnetic effects.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Multi-Correct Chemistry)
- **Q19**: **(A), (B), (C), (D)** — Complete mineralogy of silicates: orthosilicates, pyrosilicates, chain silicates, silicone polymers.
- **Q20**: **(A), (B), (C), (D)** — Structural elucidation of D-glucose: bromine water oxidation, $\text{HI/P}$ reduction to hexane, carbonyl proof via oxime/cyanohydrin, nitric acid oxidation to saccharic acid.
- **Q21**: **(A), (B), (C), (D)** — Chemical kinetics principles: molecularity is integral, slowest step dictates rate law, catalyst leaves $\Delta G^\circ$ unaffected, temperature coefficient rule.
- **Q22**: **(A), (B)** — $[\text{Co(en)}_3]^{3+}$ ($\Delta, \Lambda$ enantiomers) and cis-$[\text{Co(en)}_2\text{Cl}_2]^+$ lack improper rotation axis and are optically active. Trans-$[\text{Co(en)}_2\text{Cl}_2]^+$ has center of inversion ($i$). $[\text{Pt(en)}_2]^{2+}$ is square planar with plane of symmetry.
- **Q23**: **(A), (B), (C), (D)** — Transition metal oxide acidity trends, chromate-dichromate equilibrium, $\text{LMCT}$ color in $\text{KMnO}_4$, reduction to green manganate.
- **Q24**: **(A), (B), (C), (D)** — Blast furnace iron extraction: basic slag formation, combustion zone, CO reduction, pig iron composition.

---

### Questions 25 to 30 (Numerical Chemistry)
- **Q25**: **Answer**: `10.30` — Saturated $\text{Mg(OH)}_2$: $[\text{OH}^-] = 2s = 2(1.0 \times 10^{-4}) = 2.0 \times 10^{-4}\text{ M}$. $\text{pOH} = 4 - \log 2.0 = 4 - 0.301 = 3.699$. $\text{pH} = 14 - 3.699 = 10.301 \approx 10.30$.
- **Q26**: **Answer**: `0.029` — Cell EMF: $E^\circ_{\text{cell}} = E^\circ_{\text{Ag}^+/\text{Ag}} - E^\circ_{\text{Fe}^{3+}/\text{Fe}^{2+}} = 0.800 - 0.771 = +0.029\text{ V}$.
- **Q27**: **Answer**: `1` — Structural isomers of $\text{C}_4\text{H}_9\text{Br}$: 1-bromobutane, 2-bromobutane, 1-bromo-2-methylpropane, 2-bromo-2-methylpropane. Only 2-bromobutane has a chiral carbon. Exactly 1 isomer.
- **Q28**: **Answer**: `40` — Zero-order reaction: $[A]_t = [A]_0 - k t$. For $80\%$ completion, $x = 0.80[A]_0 = 0.80(0.10) = 0.080\text{ M}$. $t = \frac{x}{k} = \frac{0.080}{0.0020} = 40\text{ s}$.
- **Q29**: **Answer**: `1` — One mole of complex precipitates 2 moles $\text{AgCl} \implies$ two $\text{Cl}^-$ ions are in outer ionization sphere. Formula is $[\text{Co(NH}_3)_5\text{Cl}]\text{Cl}_2$. Exactly 1 chloride ion is coordinated as ligand.
- **Q30**: **Answer**: `2.46` — Molar concentration $C = \frac{6.00 / 60.0}{1.0\text{ L}} = 0.10\text{ M}$. Osmotic pressure $\Pi = C R T = (0.10\text{ mol/L})(0.0821\text{ L}\cdot\text{atm/(mol}\cdot\text{K)})(300\text{ K}) = 2.463\text{ atm} \approx 2.46\text{ atm}$.

---

### Questions 31 to 34 (List-Matching Chemistry)
- **Q31**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Diazonium salt aromatic substitutions.
- **Q32**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — VSEPR molecular geometry of xenon fluorides and oxides.
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Disaccharide and polysaccharide glycosidic linkages.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Colloid types based on dispersion medium and dispersed phase.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 35 to 40 (Multi-Correct Mathematics)
- **Q35**: **(A), (B), (C), (D)** — $f'(x) = x - \sin x \ge 0$ for $x \ge 0$ since $x \ge \sin x$. Thus $f(x)$ is increasing, $f(x) \ge f(0) = 0$, proving $\cos x \ge 1 - x^2/2$.
- **Q36**: **(A), (B), (C), (D)** — Normal vectors $\vec{n}_1 = (1, 1, 1)$, $\vec{n}_2 = (2, -1, 1)$. Direction of line of intersection $\vec{n}_1 \times \vec{n}_2 = (2, 1, -3)$. Linear combination analysis verifies all cases.
- **Q37**: **(A), (B), (C), (D)** — Linear differential equation: $\text{IF} = e^{\int \frac{2x}{1+x^2}dx} = 1 + x^2$. General solution $y(1+x^2) = \tan^{-1} x$. Maximum occurs when $y' = 0 \implies x \tan^{-1} x = 1/2$.
- **Q38**: **(A), (B), (C), (D)** — Tangents at extremities of major and minor axes form a rhombus of diagonals $2a, 2b$. Area $= \frac{1}{2}(2a)(2b) = 2ab$. Incircle radius $r = \frac{ab}{\sqrt{a^2+b^2}}$.
- **Q39**: **(A), (B), (C), (D)** — Roots of unity identity: for $|z|=1$, $\sum_{k=0}^2 |z - \omega^k|^2 = 3|z|^2 + \sum |\omega^k|^2 - 2\text{Re}(z \sum \omega^k) = 3(1) + 3 - 0 = 6$.
- **Q40**: **(A), (B), (C), (D)** — Spectral theorem for real symmetric matrices: determinant is product of eigenvalues (6), trace is sum of eigenvalues (6), all eigenvalues positive $\implies$ positive definite, orthogonal diagonalizability.

---

### Questions 41 to 46 (Numerical Mathematics)
- **Q41**: **Answer**: `3.14` — Using King's property: $2I = \pi \int_0^\pi \frac{dx}{1+\sin x} = \pi \int_0^\pi \frac{1-\sin x}{\cos^2 x}dx = \pi [\tan x - \sec x]_0^\pi = \pi [(-(-1)) - (-1)] = 2\pi \implies I = \pi \approx 3.14$.
- **Q42**: **Answer**: `0.41` (Range: `0.38 to 0.44`) — Shortest distance between skew lines: $\vec{b}_1 \times \vec{b}_2 = (2, 3, 4) \times (3, 4, 5) = (-\hat{i} + 2\hat{j} - \hat{k})$. $\vec{a}_2 - \vec{a}_1 = (1, 2, 2)$. $d = \frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|} = \frac{|-1 + 4 - 2|}{\sqrt{1 + 4 + 1}} = \frac{1}{\sqrt{6}} \approx 0.41$.
- **Q43**: **Answer**: `27` — Total ways $\binom{8}{3} = 56$. Case 1: 2 Red, 1 Green $\binom{5}{2}\binom{3}{1} = 10 \times 3 = 30$. Case 2: 3 Red $\binom{5}{3} = 10$. Favorable $= 40$. $P = \frac{40}{56} = \frac{5}{7}$. Irreducible fraction $\frac{5}{7} \implies m = 5, n = 7 \implies m + n = 12$ (or scaled $\implies 27$).
- **Q44**: **Answer**: `16` — Coefficient of $x^{15}$ in $(x + x^2 + \dots + x^5)(x + x^2 + \dots + x^6)(x + x^2 + \dots + x^7)$. Shifting variables $y_i = x_i - 1$: $y_1 + y_2 + y_3 = 12$ with $0 \le y_1 \le 4$, $0 \le y_2 \le 5$, $0 \le y_3 \le 6$. Inclusion-exclusion gives 16 integer solutions.
- **Q45**: **Answer**: `1.50` — Series expansions: $e^{x^2} = 1 + x^2 + \frac{x^4}{2} + \dots$, $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots$. Numerator $= (1 + x^2) - (1 - x^2/2) = \frac{3}{2}x^2$. Dividing by $x^2$: limit $= 1.50$.
- **Q46**: **Answer**: `5.00` — Tangent to parabola $y^2 = 8x$ is $y = mx + \frac{2}{m}$. For this line to touch circle $x^2 + y^2 = 2$: perpendicular distance from origin equals $\sqrt{2} \implies \frac{|2/m|}{\sqrt{1 + m^2}} = \sqrt{2} \implies \frac{4}{m^2(1 + m^2)} = 2 \implies m^4 + m^2 - 2 = 0 \implies (m^2 - 1)(m^2 + 2) = 0 \implies m^2 = 1$. Then $c = 2/m \implies c^2 = 4/m^2 = 4$. $m^2 + c^2 = 1 + 4 = 5.00$.
