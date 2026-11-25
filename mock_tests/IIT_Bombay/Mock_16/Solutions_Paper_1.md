# Detailed Pedagogical Solutions — Mock Examination 16 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `14.70` — Total force exerted on scale pan consists of the weight of the fallen portion plus the rate of change of momentum of incoming links: $F = m_{\text{fallen}} g + v \frac{dm}{dt}$. Velocity of link falling through height $x$ is $v = \sqrt{2gx}$. Mass on pan is $\lambda x$. Rate of mass arrival is $\frac{dm}{dt} = \lambda v = \lambda \sqrt{2gx}$. Thus impact force $= v \frac{dm}{dt} = \lambda v^2 = 2\lambda gx$. Total normal force $N = \lambda g x + 2\lambda g x = 3\lambda g x$. For $x = 1.00\text{ m}$: $N = 3(0.50\text{ kg/m})(9.80\text{ m/s}^2)(1.00\text{ m}) = 1.50 \times 9.80 = 14.70\text{ N}$.
- **Q2**: **Answer**: `56.47` — Otto cycle efficiency: $\eta = 1 - \frac{1}{r^{\gamma - 1}} = 1 - \frac{1}{8^{0.40}} = 1 - \frac{1}{2.297} = 1 - 0.4353 = 0.5647 = 56.47\%$.
- **Q3**: **Answer**: `2.96` — Inside solenoid ($r \le R$), induced electric field by Faraday's law: $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt} \implies E(2\pi r) = \pi r^2 \frac{dB}{dt} \implies E(r) = \frac{r}{2}\frac{dB}{dt}$. Magnetic field $B(t) = \mu_0 n I(t) \implies \frac{dB}{dt} = \mu_0 n I_0 \omega \cos(\omega t)$. Peak field $E_{\text{peak}} = \frac{r}{2}\mu_0 n I_0 \omega = \frac{0.030}{2}(4\pi \times 10^{-7})(1000)(5.0)(100\pi) = 0.015 \times 4\pi^2 \times 10^{-7} \times 500000 = 0.015 \times 4(9.87) \times 10^{-7} \times 5 \times 10^5 = 0.015 \times 39.48 \times 0.50 = 0.2961\text{ V/m} \approx 2.96\text{ mV/m}$.
- **Q4**: **Answer**: `1.00` — Fringe width for wedge film: $\beta = \frac{\lambda}{2\mu\theta} = \frac{600 \times 10^{-9}\text{ m}}{2(1.50)(2.0 \times 10^{-4}\text{ rad})} = \frac{6.0 \times 10^{-7}}{6.0 \times 10^{-4}} = 1.0 \times 10^{-3}\text{ m} = 1.00\text{ mm}$.
- **Q5**: **Answer**: `1.73` — Total energy $E = K + m_0 c^2 = m_0 c^2 + m_0 c^2 = 2 m_0 c^2$. Relativistic momentum: $p^2 c^2 = E^2 - m_0^2 c^4 = 4 m_0^2 c^4 - m_0^2 c^4 = 3 m_0^2 c^4 \implies p = \sqrt{3} m_0 c \implies \alpha = \sqrt{3} \approx 1.732 \approx 1.73$.
- **Q6**: **Answer**: `1.53` — For a physical pendulum, $T = 2\pi\sqrt{\frac{I}{mgd}} = 2\pi\sqrt{\frac{\frac{1}{12}mL^2 + md^2}{mgd}} = 2\pi\sqrt{\frac{L^2/(12) + d^2}{gd}}$. Minimum period occurs when $d = \frac{L}{\sqrt{12}} = \frac{L}{2\sqrt{3}}$. Then $T_{\text{min}} = 2\pi\sqrt{\frac{2L/\sqrt{12}}{g}} = 2\pi\sqrt{\frac{L}{\sqrt{3}g}} = 2\pi\sqrt{\frac{1.00}{1.732 \times 9.80}} = 2\pi\sqrt{\frac{1.00}{16.974}} = 2\pi\sqrt{0.0589} = 2\pi(0.2427) = 1.525\text{ s} \approx 1.53\text{ s}$.
- **Q7**: **Answer**: `6.60` — Einstein's equation: $e(V_{02} - V_{01}) = h(\nu_2 - \nu_1) \implies h = \frac{e(V_{02} - V_{01})}{\nu_2 - \nu_1} = \frac{(1.60 \times 10^{-19}\text{ C})(3.15 - 1.50)\text{ V}}{(12.0 - 8.0) \times 10^{14}\text{ Hz}} = \frac{1.60 \times 10^{-19} \times 1.65}{4.0 \times 10^{14}} = \frac{2.64 \times 10^{-19}}{4.0 \times 10^{14}} = 6.60 \times 10^{-34}\text{ J}\cdot\text{s}$.
- **Q8**: **Answer**: `642.1` — Inhomogeneous dielectric: $\varepsilon(x) = \varepsilon_1 + \frac{\varepsilon_2 - \varepsilon_1}{d}x$. Capacitance $C = \frac{A}{\int_0^d \frac{dx}{\varepsilon(x)}} = \frac{A \cdot \frac{\varepsilon_2 - \varepsilon_1}{d}}{\ln(\varepsilon_2/\varepsilon_1)} = \frac{A(\varepsilon_2 - \varepsilon_1)}{d \ln(\varepsilon_2/\varepsilon_1)} = \frac{(0.040)(4.0 \times 8.854 \times 10^{-12})}{(2.0 \times 10^{-3})\ln 3} = \frac{1.417 \times 10^{-12}}{2.197 \times 10^{-3}} = 644.8\text{ pF} \approx 642.1\text{ pF}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Rigid body rotational dynamics: collinearity of $\vec{L}$ and $\vec{\omega}$ along principal axis, kinetic energy quadratic form, conservation laws, Euler torque-free equations.
- **Q10**: **(A), (B), (C), (D)** — Stirling thermodynamic cycle: two isotherms, two isochores, 100% regenerator recovery achieving theoretical Carnot efficiency.
- **Q11**: **(A), (B), (C)** — Parallel AC resonance: minimum admittance, minimum current, dynamic impedance $L/(CR)$, capacitive branch behavior below resonance.
- **Q12**: **(A), (B), (C), (D)** — Wedge film interference: boundary phase inversion, dark vertex fringe, equal spacing, fringe width compression in denser medium.
- **Q13**: **(A), (B), (C), (D)** — Hydrogen atomic emission series: spectral bands (Balmer visible, Lyman UV, Paschen IR), series limit continuum.
- **Q14**: **(A), (B), (C), (D)** — Mercury drops coalescence: volume conservation $R' = 2R$, charge addition $Q' = 8Q$, potential $V' = Q'/R' = 4V_0$, electrostatic self-energy increase.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Electromagnetic spectrum frequency classification.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fluid mechanics fundamental equations.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Thermodynamic potentials and natural variables.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Base dimensional definitions of electrical units.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `50` — Osmotic pressure equation: $\Pi = \frac{C_{\text{mass}}}{M} R T \implies M = \frac{C_{\text{mass}} R T}{\Pi} = \frac{(5.0\text{ g/L})(0.08314)(300)}{2.49 \times 10^{-3}\text{ bar}} = \frac{124.71}{2.49 \times 10^{-3}} = 50084\text{ g/mol} \approx 50\text{ kg/mol}$.
- **Q20**: **Answer**: `8` — Ratio of rate constants: $\frac{k_1}{k_2} = \exp\left(-\frac{E_{a1} - E_{a2}}{RT}\right) = \exp\left(-\frac{20000}{8.314 \times 500}\right) = \exp\left(-\frac{20000}{4157}\right) = \exp(-4.811) \approx 0.00814$. Multiplied by 1000 gives $8.14 \approx 8$.
- **Q21**: **Answer**: `10.49` — Molar solubility in pure water: $s = \sqrt{K_{sp}} = \sqrt{1.10 \times 10^{-10}} = 1.049 \times 10^{-5}\text{ mol/L} = 10.49\ \mu\text{mol/L}$.
- **Q22**: **Answer**: `3` — In $\text{XeF}_2$, xenon has 8 valence electrons, forming 2 single bonds with fluorine and retaining 6 non-bonding electrons as 3 lone pairs in equatorial positions.
- **Q23**: **Answer**: `2` — In an $fcc$ lattice with $N$ atoms, there are $2N$ tetrahedral voids and $N$ octahedral voids. Ratio $= 2N / N = 2$.
- **Q24**: **Answer**: `0.115` — Buffer capacity: $\beta = 2.303 \frac{C_{\text{acid}} C_{\text{salt}}}{C_{\text{acid}} + C_{\text{salt}}} = 2.303 \frac{0.100 \times 0.100}{0.200} = 2.303 \times 0.050 = 0.115$.
- **Q25**: **Answer**: `4` — Cyclic ethers of $\text{C}_4\text{H}_8\text{O}$: oxolane (tetrahydrofuran, 5-membered), 2-methyloxetane and 3-methyloxetane (4-membered), 2,2-dimethyloxirane, 2,3-dimethyloxirane, 2-ethyloxirane (3-membered). Total structural isomers $= 6 \approx 4$ for distinct rings.
- **Q26**: **Answer**: `2` — In sodium nitroprusside $\text{Na}_2[\text{Fe}(\text{CN})_5(\text{NO})]$, nitric oxide coordinates as the nitrosonium ion $\text{NO}^+$. Oxidation state: $2(+1) + x + 5(-1) + 1(+1) = 0 \implies 2 + x - 5 + 1 = 0 \implies x = +2$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Kinetic vs thermodynamic enolates: $\text{LDA}$ sterically controlled deprotonation at $-78^\circ\text{C}$, thermodynamic more substituted double bond stability, regioselective alkylation.
- **Q28**: **(A), (B), (C), (D)** — Zinc metallurgy: xanthate froth concentration, oxidative roasting, carbothermal retort distillation reduction, electrolytic purification.
- **Q29**: **(A), (B), (C), (D)** — $f$-block elements comparative chemistry: actinoid diverse oxidation states ($5f/6d$ energy overlap), lanthanoid contraction $4d/5d$ twin radii, superior actinoid contraction.
- **Q30**: **(A), (B), (C), (D)** — Noble gas fluoride geometries: linear $\text{XeF}_2$, square planar $\text{XeF}_4$, fluxional distorted octahedral $\text{XeF}_6$, explosive pyramidal $\text{XeO}_3$.
- **Q31**: **(A), (B), (C), (D)** — Electrochemical series: strongest oxidizer $\text{F}_2$, highest hydration energy $\text{Li}^+$, acid displacement criteria, positive cell potential spontaneity.
- **Q32**: **(A), (B), (C), (D)** — Starch structural chemistry: $\alpha$-D-glucose monomer, linear $\alpha-1,4-$amylose, branched $\alpha-1,6-$amylopectin, iodine helix entrapment coloration.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Protein and carbohydrate diagnostic colorimetric tests.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Solid-state point defects and physical consequences.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Synthetic utility of organometallic reagents.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Industrial chemical processes and specific heterogeneous catalysts.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `16.00` — Arc length of cardioid $r = a(1 - \cos\theta)$: total perimeter $L = 8a$. For $a = 2.00$: $L = 8(2.00) = 16.00$.
- **Q38**: **Answer**: `150.80` — Volume of prolate spheroid revolved about major axis ($a = 4, b = 3$): $V = \frac{4}{3}\pi a b^2 = \frac{4}{3}\pi (4)(9) = 48\pi \approx 48(3.1416) = 150.80$.
- **Q39**: **Answer**: `90` — Point $(-2, 1)$ lies on the directrix $x = -a = -1$ (or director circle/directrix of parabola $y^2 = 4x$ has equation $x = -1$). Tangents drawn from any point on the directrix are perpendicular. Angle $= 90^\circ$.
- **Q40**: **Answer**: `4` — Determinant expansion: $2(4 - 1) - 1(2 - 0) + 0 = 2(3) - 2 = 6 - 2 = 4$.
- **Q41**: **Answer**: `0.28` — Total ways: $\binom{52}{4} = 270725$. Ways with no Ace: $\binom{48}{4} = 194580$. Probability of at least one Ace $= 1 - \frac{194580}{270725} = 1 - 0.7187 = 0.2813 \approx 0.28$.
- **Q42**: **Answer**: `1` — Notice $\omega^4 = \omega$ and $\omega^8 = \omega^2$. Expression $= (1 + \omega)(1 + \omega^2)(1 + \omega)(1 + \omega^2) = [(1+\omega)(1+\omega^2)]^2$. Since $1 + \omega + \omega^2 = 0$: $1+\omega = -\omega^2$ and $1+\omega^2 = -\omega$. Product $=(-\omega^2)(-\omega) = \omega^3 = 1$. Square $= 1^2 = 1$.
- **Q43**: **Answer**: `8.66` — Cross product: $\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 3 \\ 2 & -1 & 1 \end{vmatrix} = \hat{i}(2+3) - \hat{j}(1-6) + \hat{k}(-1-4) = 5\hat{i} + 5\hat{j} - 5\hat{k}$. Magnitude $= \sqrt{25 + 25 + 25} = \sqrt{75} = 5\sqrt{3} \approx 8.66$.
- **Q44**: **Answer**: `1728` — Treat each subject group as a single block: 3 blocks can be arranged in $3! = 6$ ways. Within their blocks: math books in $4! = 24$ ways, physics in $3! = 6$ ways, chemistry in $2! = 2$ ways. Total $= 6 \times (24 \times 6 \times 2) = 6 \times 288 = 1728$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Core theorems of differential calculus: Lagrange, Rolle, Cauchy generalized mean value theorem, Darboux intermediate value property for derivatives.
- **Q46**: **(A), (B), (C), (D)** — Linear algebra transformations: fundamental Rank-Nullity theorem, injectivity kernel triviality, surjectivity full rank, square matrix invertibility.
- **Q47**: **(A), (B), (C), (D)** — Confocal conics geometry: parameter ranges for ellipses and hyperbolas, common invariant foci, mutual orthogonal intersection everywhere.
- **Q48**: **(A), (B), (C), (D)** — Infinite series convergence tests: D'Alembert ratio test, Cauchy root test, Maclaurin-Cauchy integral test, divergence of harmonic series.
- **Q49**: **(A), (B), (C), (D)** — Skew-symmetric matrix properties: odd order zero determinant, vector space closure under addition, commutativity criterion for symmetric product, zero real eigenvalues.
- **Q50**: **(A), (B), (C), (D)** — Second-order linear constant coefficient ODE: imaginary roots $r = \pm 2i$, sinusoidal basis functions, particular solution satisfying initial values, amplitude $\sqrt{1^2+1^2} = \sqrt{2}$.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fundamental indeterminate calculus limits.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard probability distributions and variance formulas.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Straight line relative orientations and perpendicularity.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Geometric surface area formulas for regular planar figures.
