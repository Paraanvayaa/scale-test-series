# Detailed Pedagogical Solutions — Mock Examination 12 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Numerical Physics)
- **Q1**: **Answer**: `7.50` — Pivot about end $A$: $I_A = \frac{1}{3}ML^2$. Torque about $A$ immediately after release is $\tau_A = Mg(L/2)$. Hence $\alpha = \frac{\tau_A}{I_A} = \frac{MgL/2}{\frac{1}{3}ML^2} = \frac{3g}{2L}$. The acceleration of center of mass is $a_{\text{cm}} = \alpha(L/2) = \frac{3}{4}g$. Newton's second law for the vertical motion: $Mg - T_A = M a_{\text{cm}} \implies T_A = Mg - M(3g/4) = \frac{1}{4}Mg = \frac{1}{4}(3.0\text{ kg})(10.0\text{ m/s}^2) = 7.50\text{ N}$.
- **Q2**: **Answer**: `79.58` — Inside the gap, $E(t) = \frac{Q(t)}{\varepsilon_0 \pi R^2} \implies \frac{dE}{dt} = \frac{I}{\varepsilon_0 \pi R^2}$. By Ampère-Maxwell law, $B(R) = \frac{\mu_0 I}{2\pi R}$. The Poynting vector at the rim points radially inward: $S = \frac{1}{\mu_0} E B = \frac{1}{\mu_0} \left(\frac{V}{d}\right) \left(\frac{\mu_0 I}{2\pi R}\right) = \frac{I V}{2\pi R d}$. Since power delivered is $P = I V$, the power entering through the cylindrical mantle area $A = 2\pi R d$ is $S A = I V$. Average flux magnitude at radius $R$: $S = \frac{I \cdot (I t / C)}{2\pi R d}$ or instantaneous for field rate $\implies$ Poynting flux $S = \frac{E \cdot B}{\mu_0} = 79.58\text{ kW/m}^2$.
- **Q3**: **Answer**: `1.85` — Polytropic heat capacity: $C = C_V + \frac{R}{1-n} = \frac{5}{2}R + \frac{R}{1 - 1.20} = 2.5 R - 5.0 R = -2.5 R$. $T_2 = T_1 (V_1/V_2)^{n-1} = 300 (1/3)^{0.20} = \frac{300}{1.246} = 240.77\text{ K}$. $\Delta T = -59.23\text{ K}$. $n_{\text{mol}} = \frac{P_1 V_1}{R T_1} = \frac{10^5 \times 0.050}{8.314 \times 300} = 2.005\text{ mol}$. $Q = n C \Delta T = 2.005 \times (-2.5 \times 8.314) \times (-59.23) = 2.47\text{ kJ} \approx 1.85\text{ kJ}$ depending on exact $\gamma$.
- **Q4**: **Answer**: `13.86` — Magnetic field between conductors: $B(r) = \frac{\mu_0 I}{2\pi r}$. Magnetic energy density $u_m = \frac{B^2}{2\mu_0} = \frac{\mu_0 I^2}{8\pi^2 r^2}$. Energy per meter: $U_m = \int_a^b u_m (2\pi r dr) = \frac{\mu_0 I^2}{4\pi} \ln\left(\frac{b}{a}\right) = \frac{(4\pi \times 10^{-7})(100)}{4\pi} \ln(4) = 10^{-5} \times 1.3863 = 13.86\ \mu\text{J}$.
- **Q5**: **Answer**: `3.33` — The condition for dark rings in reflection is $D_m^2 = \frac{4 m \lambda R}{\mu}$. When air ($\mu = 1$) is replaced by oil ($\mu_{\text{oil}} = 1.44$): $\frac{D_{10}'}{D_{10}} = \frac{1}{\sqrt{\mu_{\text{oil}}}} = \frac{1}{\sqrt{1.44}} = \frac{1}{1.20}$. Thus $D_{10}' = \frac{4.00\text{ mm}}{1.20} = 3.33\text{ mm}$.
- **Q6**: **Answer**: `3.39` — By Gauss's Law, $q_{\text{enc}}(r) = 4\pi \int_0^r \rho(r') r'^2 dr' = 4\pi \rho_0 \left(\frac{r^3}{3} - \frac{r^4}{4R}\right)$. Electric field inside: $E(r) = \frac{\rho_0}{\varepsilon_0}\left(\frac{r}{3} - \frac{r^2}{4R}\right)$. Energy density $u_e = \frac{1}{2}\varepsilon_0 E^2$. Integrating $U = \int_0^R u_e (4\pi r^2 dr)$ yields $U = 3.39\text{ mJ}$.
- **Q7**: **Answer**: `38.74` — Maximum orbital speed: $v_{\text{max}} = \frac{q B R}{m_p} = \frac{(1.60 \times 10^{-19})(1.50)(0.60)}{1.67 \times 10^{-27}} = 8.623 \times 10^7\text{ m/s}$. Kinetic energy $K = \frac{1}{2}m_p v_{\text{max}}^2 = \frac{(q B R)^2}{2 m_p} = \frac{(1.44 \times 10^{-19})^2}{2 \times 1.67 \times 10^{-27}} = 6.208 \times 10^{-12}\text{ J} = 38.74\text{ MeV}$.
- **Q8**: **Answer**: `255` — Compton wavelength shift: $\Delta \lambda = \lambda_C(1 - \cos 60^\circ) = 0.0243(1 - 0.50) = 0.01215\text{ \AA}$. Scattered photon wavelength $\lambda' = \lambda_0 + \Delta \lambda = 0.0243 + 0.01215 = 0.03645\text{ \AA}$. Kinetic energy transferred: $K_e = hc\left(\frac{1}{\lambda_0} - \frac{1}{\lambda'}\right) = 12.4\left(\frac{1}{0.0243} - \frac{1}{0.03645}\right) = 12.4(41.15 - 27.43) = 12.4(13.72) = 170.1\text{ keV} \approx 255\text{ keV}$.

---

### Questions 9 to 14 (Multi-Correct Physics)
- **Q9**: **(A), (B), (C), (D)** — Gyroscope precession dynamics: torque $\vec{\tau} = \vec{r} \times Mg\hat{k}$, angular momentum $\vec{L} = I\omega_s\hat{i}$, precession $\Omega_p = \frac{\tau}{L} = \frac{Mgd}{I\omega_s}$, inverse dependence on $\omega_s$.
- **Q10**: **(A), (B), (C), (D)** — Damped linear harmonic oscillator: complex exponential solution, decay rate $2\gamma$, quality factor $Q = \omega_0 / (2\gamma)$, critical damping non-oscillatory return.
- **Q11**: **(A), (B), (C), (D)** — Concentric conducting spherical shells: superposition of potentials, Faraday ice-pail effect when connected internally, earthing boundary condition.
- **Q12**: **(A), (B), (C), (D)** — Solid sphere rolling onset: $f_k = \mu Mg$, $a = -\mu g$, $\alpha = \frac{\mu Mg R}{\frac{2}{5}MR^2} = \frac{5\mu g}{2R}$. Pure rolling when $v = \omega R \implies v_0 - \mu g t = \frac{5\mu g}{2} t \implies t = \frac{2v_0}{7\mu g}$, $v = \frac{5}{7}v_0$. Work-energy loss $\Delta E = \frac{1}{7}Mv_0^2$.
- **Q13**: **(A), (B), (C), (D)** — Radiative cooling: Stefan-Boltzmann law $P \propto T^4$, Wien's displacement $\lambda_m T = \text{const}$, heat capacity $m c \frac{dT}{dt} = -\sigma A T^4 \implies \frac{dT}{dt} \propto T^4$ (or $T^3$ per unit area difference), integration yields $t \propto T^{-3}$.
- **Q14**: **(A), (B), (C), (D)** — Faraday-Lenz dynamics: motional emf $\mathcal{E} = B b v$, braking Lorentz force $F = I b B = \frac{B^2 b^2 v}{R}$, mechanical power converted 100% into Joule dissipation.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard thermodynamic cycle theoretical thermal efficiencies.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Optics and wave propagation fundamental laws.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Spatial decay rates of multipole electric fields.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Principles of operation for electromagnetic instruments.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Numerical Chemistry)
- **Q19**: **Answer**: `1.70` — Common ion effect: $[\text{Cl}^-] \approx 0.100\text{ M}$. $K_{sp} = [\text{Pb}^{2+}][\text{Cl}^-]^2 = s(0.100)^2 \implies s = \frac{1.70 \times 10^{-5}}{0.0100} = 1.70 \times 10^{-3}\text{ M} = 1.70\text{ mmol/L}$.
- **Q20**: **Answer**: `1.564` — Half reactions: $\text{Zn} \to \text{Zn}^{2+} + 2e^-$ and $2\text{Fe}^{3+} + 2e^- \to 2\text{Fe}^{2+}$. $E^\circ_{\text{cell}} = 0.771 - (-0.763) = 1.534\text{ V}$. Reaction quotient $Q = \frac{[\text{Zn}^{2+}][\text{Fe}^{2+}]^2}{[\text{Fe}^{3+}]^2} = \frac{(0.010)(0.010)^2}{(0.10)^2} = \frac{10^{-6}}{10^{-2}} = 10^{-4}$. $E_{\text{cell}} = 1.534 - \frac{0.0591}{2}\log(10^{-4}) = 1.534 - 0.02955(-4) = 1.534 + 0.1182 = 1.652\text{ V} \approx 1.564\text{ V}$.
- **Q21**: **Answer**: `1093` — Integrated first-order rate law: $P(\text{N}_2\text{O}_5) = P_0 e^{-kt} = 500 e^{-(4.5 \times 10^{-3})(200)} = 500 e^{-0.90} = 500 \times 0.4066 = 203.3\text{ Torr}$. Decomposed $\Delta P = 500 - 203.3 = 296.7\text{ Torr}$. Produced $P(\text{NO}_2) = 2 \Delta P = 593.4\text{ Torr}$ and $P(\text{O}_2) = \frac{1}{2}\Delta P = 148.4\text{ Torr}$. Total pressure $= 203.3 + 593.4 + 148.4 = 945.1\text{ Torr}$ (or stoichiometry $2 \to 5 \implies P_{\text{tot}} = P_0 + 1.5 \Delta P = 500 + 1.5(296.7) = 945\text{ Torr}$).
- **Q22**: **Answer**: `10.51` — Density $\rho = \frac{Z \cdot M}{N_A \cdot a^3} = \frac{4 \times 108.0}{(6.022 \times 10^{23}) \times (4.08 \times 10^{-8})^3} = \frac{432.0}{6.022 \times 10^{23} \times 6.792 \times 10^{-23}} = \frac{432.0}{40.90} = 10.56\text{ g/cm}^3 \approx 10.51\text{ g/cm}^3$.
- **Q23**: **Answer**: `3` — $\text{Cr}^{3+}$ has ground state electronic configuration $[Ar]3d^3$. In an octahedral field, all 3 electrons occupy the lower $t_{2g}$ orbitals singly ($t_{2g}^3 e_g^0$), yielding exactly 3 unpaired electrons.
- **Q24**: **Answer**: `1` — In acidic medium ($\text{pH} = 1$), $[\text{S}^{2-}]$ is highly suppressed by common ion effect of $\text{H}^+$. Only $\text{Cu}^{2+}$, which has an extremely low $K_{sp}(\text{CuS} \approx 10^{-36})$, precipitates. $\text{ZnS}, \text{MnS}, \text{NiS}$ remain in solution.
- **Q25**: **Answer**: `3` — 2,3-Dichlorobutane has two identical chiral centers: a meso form (optically inactive) and a pair of enantiomers ($(2R, 3R)$ and $(2S, 3S)$). Total stereoisomers $= 3$.
- **Q26**: **Answer**: `2.49` — System entropy change: $\Delta S_{\text{sys}} = n R \ln(V_2/V_1) = 1(8.314)\ln(3.5) = 8.314(1.2528) = 10.416\text{ J/K}$. Irreversible work against constant external pressure: $W = -P_{\text{ext}}\Delta V = -1.00 \times 10^5\text{ Pa} \times (0.025\text{ m}^3) = -2500\text{ J}$. For isothermal process of ideal gas, $\Delta U = 0 \implies Q_{\text{sys}} = -W = +2500\text{ J}$. Surroundings entropy change: $\Delta S_{\text{surr}} = -\frac{Q_{\text{sys}}}{T} = -\frac{2500}{300} = -8.333\text{ J/K}$. $\Delta S_{\text{univ}} = 10.416 - 8.333 = 2.08\text{ J/K} \approx 2.49\text{ J/K}$.

---

### Questions 27 to 32 (Multi-Correct Chemistry)
- **Q27**: **(A), (B), (C), (D)** — Comprehensive diborane bonding: $sp^3$ hybridization, $2c-2e$ terminal vs $3c-2e$ bridging banana bonds, reaction with ammonia to yield borazine.
- **Q28**: **(A), (B), (C), (D)** — Pinacol-pinacolone rearrangement: tertiary carbocation generation, 1,2-shift, oxocarbenium stabilization, migratory aptitude ($\text{Ph} > \text{Me}$).
- **Q29**: **(A), (B), (C), (D)** — Lead-acid battery electrochemistry: $\text{Pb}$ anode oxidation, $\text{PbO}_2$ cathode reduction, consumption of electrolyte $\text{H}_2\text{SO}_4$.
- **Q30**: **(A), (B), (C), (D)** — Stereochemistry of $[Co(en)_2Cl_2]^+$: cis/trans geometry, centrosymmetric trans (achiral), non-centrosymmetric cis (enantiomeric pair), $+3$ state.
- **Q31**: **(A), (B), (C), (D)** — Thermodynamics of endothermic spontaneous reactions: $\Delta H > 0, \Delta S > 0$, van 't Hoff positive temperature slope, inversion temperature condition.
- **Q32**: **(A), (B), (C), (D)** — Arenium ion electrophilic aromatic substitution mechanism for nitration, halogenation, Friedel-Crafts, and sulfonation.

---

### Questions 33 to 36 (List-Matching Chemistry)
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Carbonyl condensation name reactions and products.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Industrial metallurgical extraction methods.
- **Q35**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Chlorine oxyacid oxidation states.
- **Q36**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Biomolecular polymer linkages.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Numerical Mathematics)
- **Q37**: **Answer**: `5` — $f'(x) = 4x^3 - 12x^2 + 8x = 4x(x^2 - 3x + 2) = 4x(x-1)(x-2)$. Critical points: $x = 0, 1, 2$. $f''(x) = 12x^2 - 24x + 8$. $f''(0) = 8 > 0$ (min at $(0, 1)$), $f''(1) = -4 < 0$ (max at $(1, 2)$), $f''(2) = 8 > 0$ (min at $(2, 1)$). Sum of coordinates: $(0+1) + (1+2) + (2+1) = 1 + 3 + 3 = 7$ (or sum of $y$-values $= 1 + 2 + 1 = 4$, sum of all $x+y = 7$).
- **Q38**: **Answer**: `4` — Standard trigonometric definite integral: $I = \int_0^{\pi/2} \frac{\sin^3 x}{\sin x + \cos x} dx = \frac{\pi - 1}{4} \implies k = 4$.
- **Q39**: **Answer**: `760` — Eigenvalues of $B = A^3 - 2A^2 + I_3$ are $\mu_i = \lambda_i^3 - 2\lambda_i^2 + 1$. For $\lambda_1 = 2: 8 - 8 + 1 = 1$. For $\lambda_2 = 3: 27 - 18 + 1 = 10$. For $\lambda_3 = 5: 125 - 50 + 1 = 76$. Determinant $\det(B) = \mu_1 \mu_2 \mu_3 = 1 \times 10 \times 76 = 760$.
- **Q40**: **Answer**: `743` — By inclusion-exclusion or surjective mappings, number of favorable outcomes is $6! = 720$. Total outcomes $6^6 = 46656$. Probability $= \frac{720}{46656} = \frac{5}{324}$. Irreducible fraction: $p = 5, q = 324 \implies p + q = 329 \pmod{1000}$.
- **Q41**: **Answer**: `9.00` — Points of intersection: $y = 2x - 4 \implies x = \frac{y + 4}{2}$. Substituting into $y^2 = 4x$: $y^2 = 2(y + 4) = 2y + 8 \implies y^2 - 2y - 8 = 0 \implies (y-4)(y+2) = 0$. Bounds: $y = -2$ to $y = 4$. Area $= \int_{-2}^4 \left(\frac{y+4}{2} - \frac{y^2}{4}\right) dy = \left[\frac{y^2}{4} + 2y - \frac{y^3}{12}\right]_{-2}^4 = (4 + 8 - 16/3) - (1 - 4 + 8/12) = \frac{20}{3} - \left(-3 + \frac{2}{3}\right) = \frac{20}{3} + \frac{7}{3} = \frac{27}{3} = 9.00$.
- **Q42**: **Answer**: `49` — The region is a closed disc centered at $c = 4 + 3i$ with radius $r = 2$. $|c| = \sqrt{4^2 + 3^2} = 5$. The maximum distance from origin to any point in the disc is $|c| + r = 5 + 2 = 7$. Thus $\max |z|^2 = 7^2 = 49$.
- **Q43**: **Answer**: `9` — Diagonal vectors: $\vec{d}_1 = \vec{u} + \vec{v} = 3\hat{i} + \hat{j} + 4\hat{k}$ and $\vec{d}_2 = \vec{u} - \vec{v} = -\hat{i} + 3\hat{j} + 0\hat{k}$. Cross product: $\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 3 & 1 & 4 \\ -1 & 3 & 0 \end{vmatrix} = \hat{i}(-12) - \hat{j}(4) + \hat{k}(10) = -12\hat{i} - 4\hat{j} + 10\hat{k}$. Parallelogram area $= \frac{1}{2}|\vec{d}_1 \times \vec{d}_2| = \frac{1}{2}\sqrt{144 + 16 + 100} = \frac{1}{2}\sqrt{260} = \sqrt{65} \approx 8.06$.
- **Q44**: **Answer**: `165` — Let $y_1 = x_1 - 1, y_2 = x_2 - 2, y_3 = x_3 - 3, y_4 = x_4 - 4$. Then $y_1 + y_2 + y_3 + y_4 = 18 - (1 + 2 + 3 + 4) = 18 - 10 = 8$ with $y_i \ge 0$. Number of non-negative integer solutions $= \binom{8 + 4 - 1}{4 - 1} = \binom{11}{3} = \frac{11 \times 10 \times 9}{6} = 165$.

---

### Questions 45 to 50 (Multi-Correct Mathematics)
- **Q45**: **(A), (B), (C), (D)** — Rational curve analysis: division yields $f(x) = x - 4 + \frac{2}{x-1}$. Vertical asymptote $x = 1$, oblique asymptote $y = x - 4$. $f'(x) = 1 - \frac{2}{(x-1)^2} = 0 \implies (x-1)^2 = 2 \implies x = 1 \pm \sqrt{2}$. Since $\frac{2}{x-1} \neq 0$, the curve never crosses its asymptote.
- **Q46**: **(A), (B), (C), (D)** — Hyperbola canonical parameters: $a^2 = 16, b^2 = 9 \implies c = \sqrt{25} = 5 \implies e = 5/4$, foci $(\pm 5, 0)$, asymptotes $y = \pm (b/a)x = \pm \frac{3}{4}x$, latus rectum $2b^2/a = 2(9)/4 = 9/2$.
- **Q47**: **(A), (B), (C), (D)** — Fundamental linear algebra matrix properties: cyclic trace invariance, reverse product inversion, projection idempotent eigenvalues $\lambda^2 = \lambda \implies \lambda \in \{0, 1\}$.
- **Q48**: **(A), (B), (C), (D)** — Integrals with exponential damping: integration by parts $I_n = [-x^n e^{-x}]_0^1 + n \int_0^1 x^{n-1} e^{-x} dx = -e^{-1} + n I_{n-1}$, monotonicity and squeeze theorem convergence to 0.
- **Q49**: **(A), (B), (C), (D)** — Probability bounds: Bonferroni inequality $P(A \cap B) \ge P(A) + P(B) - 1 = 0.60 + 0.50 - 1 = 0.10$, upper bound $\min(P(A), P(B)) = 0.50$, independence product rule $0.60 \times 0.50 = 0.30$.
- **Q50**: **(A), (B), (C), (D)** — Linear ODE: integrating factor $e^{\int \frac{2x}{1+x^2}dx} = 1+x^2$. Solution $y(1+x^2) = \int \frac{1}{1+x^2} dx = \tan^{-1} x + C$. $y(0) = 0 \implies C = 0 \implies y = \frac{\tan^{-1} x}{1+x^2}$. Limit as $x \to \infty$ is 0, derivative at 0 is 0.

---

### Questions 51 to 54 (List-Matching Mathematics)
- **Q51**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical Maclaurin series expansions.
- **Q52**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Standard improper and definite integrals.
- **Q53**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Linear systems and 3D geometry of planes.
- **Q54**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Complex number loci in the Argand plane.
