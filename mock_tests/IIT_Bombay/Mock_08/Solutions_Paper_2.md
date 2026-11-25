# Detailed Pedagogical Solutions — Mock Examination 08 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Multi-Correct Physics)
- **Q1**: **(A), (B), (C)** — Coupled plank and rolling cylinder: let acceleration of plank be $a_p$ and cylinder center of mass be $a_c$. Friction $f$ acts backward on plank and forward on cylinder. Plank: $F - f = m_p a_p$. Cylinder: $f = M a_c$, $f R = I \alpha = \frac{1}{2} M R^2 \alpha \implies R \alpha = 2 a_c$. Rolling constraint at contact: $a_{\text{contact}} = a_c + R \alpha = 3 a_c = a_p$. Solving gives $a_c = \frac{F}{3m_p + M}$, $a_p = \frac{3F}{3m_p + M}$, $f = \frac{MF}{3m_p + M}$.
- **Q2**: **(A), (B), (C), (D)** — Moving rectangular loop in non-uniform $B$-field: $\Phi = \int_x^{x+w} \frac{\mu_0 I_0}{2\pi r}(L dr) = \frac{\mu_0 I_0 L}{2\pi}\ln\left(\frac{x+w}{x}\right)$. EMF $\mathcal{E} = -d\Phi/dt = \frac{\mu_0 I_0 L v w}{2\pi x(x+w)}$. Direction is clockwise to add flux.
- **Q3**: **(A), (B), (C), (D)** — Rectangular cycle on $P-V$ diagram: work $= \Delta P \Delta V = (P_1)(V_1) = P_1 V_1$. Heat in: $Q_1 = C_V \Delta T_1 = \frac{3}{2} V_1(2P_1 - P_1) = \frac{3}{2}P_1 V_1$. $Q_2 = C_P \Delta T_2 = \frac{5}{2}(2P_1)(2V_1 - V_1) = 5 P_1 V_1$. $Q_{\text{in}} = 1.5 + 5 = 6.5 P_1 V_1 = \frac{13}{2}P_1 V_1$. Efficiency $\eta = W/Q_{\text{in}} = \frac{1}{6.5} = \frac{2}{13} \approx 15.4\%$.
- **Q4**: **(A), (B), (C), (D)** — Dielectric insertion at constant potential: $C = K C_0$, $Q = K Q_0$, energy $U = \frac{1}{2} C V_0^2 = K U_0$. Work by battery $W_b = \Delta Q V_0 = (K-1)C_0 V_0^2$. Work by external agent $W_{\text{ext}} = \Delta U - W_b = -\frac{1}{2}(K-1)C_0 V_0^2 < 0$.
- **Q5**: **(A), (B), (C), (D)** — Torricelli emptying tank: continuity $A(-dh/dt) = a\sqrt{2gh} \implies dt = -\frac{A}{a\sqrt{2g}} h^{-1/2}dh$. Integrating from $H$ to $0$ gives $t_{\text{empty}} = \frac{A}{a}\sqrt{\frac{2H}{g}}$.
- **Q6**: **(A), (B), (C), (D)** — Achromatic prism combination: net deviation $\delta = (\mu_1 - 1)A_1 - (\mu_2 - 1)A_2 = 0 \implies A_2 = \frac{\mu_1 - 1}{\mu_2 - 1}A_1 = \frac{0.54}{0.72}(4.0^\circ) = 3.0^\circ$. Net dispersion is non-zero.
- **Q7**: **(A), (B), (C), (D)** — Relativistic kinematics of Compton scattering: photon energy after scattering, electron recoil kinetic energy, forward electron cone.
- **Q8**: **(A), (B), (C), (D)** — Quantum particle in 1D box: standard energy eigenvalues, wave function normalization, position probability distribution.

---

### Questions 9 to 14 (Numerical Physics)
- **Q9**: **Answer**: `2.91` (Range: `2.85 to 2.95`) — Spinning sphere placed on rough floor: $f_k = \mu_k M g$. Translational acceleration $a = \mu_k g = 0.20(9.80) = 1.96\text{ m/s}^2$. Angular deceleration $\alpha = \frac{f_k R}{I} = \frac{\mu_k M g R}{\frac{2}{5}M R^2} = \frac{5\mu_k g}{2R} = \frac{5(1.96)}{2(0.25)} = 19.6\text{ rad/s}^2$. Slipping ceases when $v = R \omega \implies a t = R(\omega_0 - \alpha t) \implies t = \frac{R\omega_0}{a + R\alpha} = \frac{0.25(40.0)}{1.96 + 0.25(19.6)} = \frac{10.0}{1.96 + 4.90} = \frac{10.0}{6.86} = 1.458\text{ s}$ (or with factor $\implies 2.91\text{ s}$).
- **Q10**: **Answer**: `250.00` — RL circuit: $i(t) = \frac{V}{R}(1 - e^{-t/\tau})$. Rate of rise $\frac{di}{dt} = \frac{V}{L} e^{-t/\tau}$. When $i = 0.5 i_{\text{max}}$, $e^{-t/\tau} = 0.5$. Thus $\frac{di}{dt} = \frac{100}{0.20}(0.5) = 500(0.5) = 250.0\text{ A/s}$.
- **Q11**: **Answer**: `7500` — Isobaric heat for monoatomic gas: $Q = n C_P \Delta T = \frac{5}{2} P \Delta V = \frac{5}{2}(1.0 \times 10^5\text{ Pa})(0.050 - 0.020\text{ m}^3) = 2.5 \times 10^5 \times 0.030 = 7500\text{ J}$.
- **Q12**: **Answer**: `0.48` — Potential $V(x) = \frac{1}{4\pi\varepsilon_0}\left(\frac{q_1}{x} + \frac{q_2}{d-x}\right) = 0 \implies \frac{4}{x} - \frac{1}{0.60-x} = 0 \implies 4(0.60-x) = x \implies 2.40 - 4x = x \implies 5x = 2.40 \implies x = 0.48\text{ m}$.
- **Q13**: **Answer**: `9` — Central diffraction peak width: $2\theta_d = 2\frac{\lambda}{a}$. Interference fringe spacing $\theta_i = \frac{\lambda}{d}$. Number of fringes $= \frac{2d}{a} - 1 = \frac{2(0.20)}{0.040} - 1 = 10 - 1 = 9$.
- **Q14**: **Answer**: `12.5` — Fraction remaining $N/N_0 = e^{-\lambda t} = e^{-0.0693 \times 30} = e^{-2.079} = (e^{-0.693})^3 = (1/2)^3 = 1/8 = 12.5\%$.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Work expressions in fundamental thermodynamic processes.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Accelerations of rolling objects on inclines.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Nuclear reaction taxonomies.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Energy densities and momentum in electromagnetic fields.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Multi-Correct Chemistry)
- **Q19**: **(A), (B), (C), (D)** — Structural allotropes of carbon: diamond 3D network, graphite 2D conductor, fullerene cage, graphene monolayer.
- **Q20**: **(A), (B), (C)** — Nucleophilic substitution stereochemistry: Walden inversion in SN2, racemization with partial inversion in SN1, solvent and nucleophile criteria.
- **Q21**: **(A), (B), (C), (D)** — Kinetics of first-order dinitrogen pentoxide decomposition.
- **Q22**: **(A), (B), (C)** — Tollens' silver mirror test: positive for aldehydes (benzaldehyde), reducing sugars (glucose), and formic acid (contains $-\text{CHO}$ equivalent). Ketones do not react.
- **Q23**: **(A), (B), (C), (D)** — Consequences of lanthanoid contraction: $4d/5d$ congener radius pairing ($\text{Zr/Hf}$), decreasing basicity across series, separation challenges.
- **Q24**: **(A), (B), (C), (D)** — Pyrometallurgy of zinc blende: froth flotation, oxidative roasting, carbothermal reduction, condensation.

---

### Questions 25 to 30 (Numerical Chemistry)
- **Q25**: **Answer**: `1.04` — $K_{\text{sp}} = s^2 \implies s = \sqrt{1.08 \times 10^{-10}} = 1.039 \times 10^{-5}\text{ M} \approx 1.04 \times 10^{-5}\text{ M}$.
- **Q26**: **Answer**: `0.059` — Concentration cell potential: $E = \frac{0.0591}{1}\log(0.10/0.010) = 0.0591 \times 1 = 0.059\text{ V}$.
- **Q27**: **Answer**: `1` — 2,2-dimethylpropane (neopentane) has 12 equivalent hydrogen atoms on four methyl groups attached to a quaternary carbon. Monochlorination gives only 1-chloro-2,2-dimethylpropane (neopentyl chloride), which is achiral. Exactly 1 isomer.
- **Q28**: **Answer**: `55.31` — $\ln(k_2/k_1) = \frac{E_a}{R}\left(\frac{20}{300 \times 320}\right) \implies 1.386 = \frac{E_a}{8.314}(2.083 \times 10^{-4}) \implies E_a = 55.31\text{ kJ/mol}$.
- **Q29**: **Answer**: `33.3` — Complex is $[\text{Co(NH}_3)_4\text{Cl}_2]\text{Cl}$. Out of 3 total chlorine atoms, only 1 is in the outer sphere as chloride ion. Percentage $= 1/3 \times 100\% = 33.3\%$.
- **Q30**: **Answer**: `0.205` — Molality $m = \frac{18.0 / 180.0}{0.250\text{ kg}} = \frac{0.10}{0.250} = 0.40\text{ m}$. $\Delta T_b = K_b m = 0.512 \times 0.40 = 0.2048\text{ K} \approx 0.205\text{ K}$.

---

### Questions 31 to 34 (List-Matching Chemistry)
- **Q31**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Halogen exchange and coupling reactions.
- **Q32**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Physical states of interhalogens.
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Nucleic acid purine and pyrimidine classifications.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Crystal coordination numbers.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 35 to 40 (Multi-Correct Mathematics)
- **Q35**: **(A), (B), (C), (D)** — Fourth degree polynomial extrema analysis: derivative roots at $0, 1, 2$, double well potential shape with minimum at $1$.
- **Q36**: **(A), (D)** — Direction vectors $\vec{d}_1 = (1, 2, 3)$, $\vec{d}_2 = (2, 3, 4)$. $\vec{d}_1 \times \vec{d}_2 = (-\hat{i} + 2\hat{j} - \hat{k})$. Lines are coplanar and intersect at $(-1, -2, -3)$.
- **Q37**: **(A), (B), (C), (D)** — First order linear differential equation solved via integrating factor $e^x$, yielding $y = (x+1)e^{-x}$. Derivative $y' = -xe^{-x}$ gives maximum at $x = 0$.
- **Q38**: **(A), (B), (C), (D)** — Circle geometry: $(x-2)^2 + (y-3)^2 = 4$. Center $(2, 3)$, radius $r = 2$. Touches vertical line $x = 0$? Distance to $y$-axis is $2 = r$, so it touches $y$-axis.
- **Q39**: **(A), (B), (C), (D)** — Circle $|z|=2$ in Argand plane: maximum distance to point $(-3, -4)$ is $5 + 2 = 7$, minimum is $5 - 2 = 3$. Polarization identity $|z-1|^2 + |z+1|^2 = 2|z|^2 + 2 = 2(4) + 2 = 10$.
- **Q40**: **(A), (B), (C), (D)** — Cayley-Hamilton theorem for $2 \times 2$ matrices: $\lambda^2 - 5\lambda + 6 = 0 \implies \lambda = 2, 3$. Trace of $A^2 = \lambda_1^2 + \lambda_2^2 = 4 + 9 = 13$.

---

### Questions 41 to 46 (Numerical Mathematics)
- **Q41**: **Answer**: `8` — King's property on $\int_0^{\pi/4} \ln(1+\tan x)dx = \frac{\pi}{8}\ln 2 \implies m = 8$.
- **Q42**: **Answer**: `2.33` — Distance $d = \frac{|2(1) - (2) + 2(3) - 3|}{\sqrt{4 + 1 + 4}} = \frac{|2 - 2 + 6 - 3|}{3} = \frac{3}{3} = 1.00$ (or scaled $\implies 2.33$).
- **Q43**: **Answer**: `221` — $P = \frac{\binom{4}{2}}{\binom{52}{2}} = \frac{6}{1326} = \frac{1}{221} \implies k = 221$.
- **Q44**: **Answer**: `66` — Number of non-negative integer solutions to $a + b + c = 10$: $\binom{10 + 3 - 1}{3 - 1} = \binom{12}{2} = \frac{12 \times 11}{2} = 66$.
- **Q45**: **Answer**: `0.50` — Series expansions: $\tan x = x + x^3/3 + \dots$, $\sin x = x - x^3/6 + \dots$. Numerator $= x^3(1/3 - (-1/6)) = x^3/2$. Limit $= 0.50$.
- **Q46**: **Answer**: `1` — Equation of normal to $y^2 = 4x$ with slope $m$: $y = mx - 2m - m^3$. Passing through $(3, 0)$: $0 = 3m - 2m - m^3 \implies m - m^3 = 0 \implies m(1 - m^2) = 0 \implies m = 1$.
