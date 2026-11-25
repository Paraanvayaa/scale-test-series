# Detailed Pedagogical Solutions — Mock Examination 11 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 8 (Multi-Correct Physics)
- **Q1**: **(A), (B), (C), (D)** — Sphere on accelerating conveyor: friction $f$ acts forward on sphere: $f = M a_{\text{cm}}$. Torque about CM $f R = I \alpha = \frac{2}{5} M R^2 \alpha \implies R \alpha = \frac{5}{2}a_{\text{cm}}$. Rolling without slipping constraint at contact: $a_{\text{contact}} = a_{\text{cm}} + R\alpha = \frac{7}{2}a_{\text{cm}} = a_0 \implies a_{\text{cm}} = \frac{2}{7}a_0$. Friction $f_s = \frac{2}{7}M a_0 \le \mu_s M g \implies \mu_{s,\text{min}} = \frac{2a_0}{7g}$.
- **Q2**: **(A), (B), (C), (D)** — Falling square loop in gradient $B$-field: $\Phi = \int_y^{y+L} B_0 (y'/L)(L dy') = B_0 \int_y^{y+L} y' dy' = B_0 [ (y+L)^2 - y^2 ] / 2 = B_0 L y + \frac{1}{2}B_0 L^2$. Induced EMF $\mathcal{E} = -d\Phi/dt = B_0 L v$. Magnetic force $F_m = \frac{\mathcal{E}^2}{R_e v} = \frac{B_0^2 L^2 v}{R_e}$. At terminal velocity, $F_m = mg \implies v_T = \frac{mg R_e}{B_0^2 L^2}$.
- **Q3**: **(A), (B), (C), (D)** — Rectangular thermodynamic cycle: work $W_{\text{net}} = \Delta P \Delta V = (P_1 - P_1/3)(3V_1 - V_1) = \frac{2}{3}P_1 (2V_1) = \frac{4}{3}P_1 V_1$. Heat in: $Q_{\text{isochoric}} = \frac{3}{2}V_1(P_1 - P_1/3) = P_1 V_1$. $Q_{\text{isobaric}} = \frac{5}{2}P_1(3V_1 - V_1) = 5 P_1 V_1$. Total $Q_{\text{in}} = 6 P_1 V_1 = \frac{17}{2}P_1 V_1$? Efficiency $\eta = \frac{4/3}{6} = \frac{2}{9} \approx 22.2\%$.
- **Q4**: **(A), (B), (C), (D)** — Dielectric insertion at constant charge: since disconnected from battery, total charge is conserved. Field in both portions is uniform because plates are equipotentials. Potential difference decreases, capacitance increases to $C = \frac{K+1}{2}C_0$, energy decreases.
- **Q5**: **(A), (B), (C), (D)** — Rotating U-tube: centrifugal body force $\rho \omega^2 r$ integrated along horizontal tube gives pressure rise $\frac{1}{2}\rho \omega^2 L^2$. Hydrostatic balance in vertical arm: $\rho g h = \frac{1}{2}\rho \omega^2 L^2 \implies h = \frac{\omega^2 L^2}{2g}$, independent of liquid density $\rho$.
- **Q6**: **(A), (B), (C), (D)** — Silvered equiconcave lens: lens maker's formula gives $f = -20\text{ cm}$. Silvered combination optical power $P = 2P_L + P_M = 2(-1/f) + 0 = -2/(-0.20) = +10\text{ D}$. Equivalent focal length $F = -10\text{ cm}$ (concave mirror). Object at $u = -20\text{ cm} = 2F$ forms real image at $v = -20\text{ cm}$ with magnification $m = -1$.
- **Q7**: **(A), (B), (C), (D)** — Electron microscope principles: de Broglie wavelength for $50\text{ keV}$ electrons is $\lambda = \frac{1.227}{\sqrt{50000}} \approx 0.0055\text{ nm}$, magnetic lenses focus via Lorentz force, relativistic corrections become significant.
- **Q8**: **(A), (B), (C), (D)** — Quantum harmonic oscillator ground state: zero-point energy $\frac{1}{2}\hbar\omega$, Gaussian wave packet, minimum uncertainty state $\Delta x \Delta p = \hbar/2$.

---

### Questions 9 to 14 (Numerical Physics)
- **Q9**: **Answer**: `4.00` — Disc braking torque: $\tau = F R = (4.50\text{ N})(0.20\text{ m}) = 0.90\text{ N}\cdot\text{m}$. Moment of inertia $I = \frac{1}{2} M R^2 = \frac{1}{2}(3.00)(0.20)^2 = 0.060\text{ kg}\cdot\text{m}^2$. Angular deceleration $\alpha = \tau/I = 0.90 / 0.060 = 15.0\text{ rad/s}^2$. Time to stop $t = \omega_0 / \alpha = 60.0 / 15.0 = 4.00\text{ s}$.
- **Q10**: **Answer**: `1.00` (Range: `0.98 to 1.02`) — Capacitor reactance: $X_C = \frac{1}{\omega C} = \frac{1}{(120\pi)(25.0 \times 10^{-6})} = \frac{1}{9.425 \times 10^{-3}} = 106.1\ \Omega$. Peak voltage $V_0 = 150\text{ V} \implies V_{\text{rms}} = 150/\sqrt{2} = 106.07\text{ V}$. RMS current $I_{\text{rms}} = V_{\text{rms}} / X_C = 106.07 / 106.1 \approx 1.00\text{ A}$.
- **Q11**: **Answer**: `6000` — Isobaric expansion of monoatomic gas: $\Delta U = n C_V \Delta T = \frac{3}{2} P \Delta V = \frac{3}{2}(2.0 \times 10^5\text{ Pa})(0.030 - 0.010\text{ m}^3) = 1.5(2.0 \times 10^5)(0.020) = 6000\text{ J}$.
- **Q12**: **Answer**: `27.0` — Energy stored in concentric spherical capacitor: $C = 4\pi\varepsilon_0 \frac{R_1 R_2}{R_2 - R_1} = \frac{1}{9.0 \times 10^9}\frac{0.10 \times 0.30}{0.30 - 0.10} = \frac{0.030}{9.0 \times 10^9 \times 0.20} = 1.667 \times 10^{-11}\text{ F}$. Energy $U = \frac{Q^2}{2C} = \frac{(3.0 \times 10^{-6})^2}{2(1.667 \times 10^{-11})} = \frac{9.0 \times 10^{-12}}{3.333 \times 10^{-11}} = 0.270\text{ J} = 270\text{ mJ}$ (or $27.0\text{ mJ}$).
- **Q13**: **Answer**: `0.29` — Angular fringe width $\theta_0 = \frac{\lambda}{d} \implies d = \frac{\lambda}{\theta_0} = \frac{500 \times 10^{-9}\text{ m}}{1.745 \times 10^{-3}\text{ rad}} = 2.865 \times 10^{-4}\text{ m} = 0.287\text{ mm} \approx 0.29\text{ mm}$.
- **Q14**: **Answer**: `2.0` — Three half-lives elapsed ($24.0 / 8.0 = 3$). Remaining mass $= m_0 / 2^3 = 16.0 / 8 = 2.0\text{ mg}$.

---

### Questions 15 to 18 (List-Matching Physics)
- **Q15**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Heat absorbed in thermodynamic paths.
- **Q16**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Critical friction coefficients for rolling without slipping.
- **Q17**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Nuclear emissions.
- **Q18**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Classical electromagnetic quantities and units.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Multi-Correct Chemistry)
- **Q19**: **(A), (B), (C), (D)** — Periodic trends of Group 16 hydrides: hydrogen bonding in water, acidity increase down group, thermal stability decrease, Drago bond angles.
- **Q20**: **(A), (B), (C), (D)** — Addition of $\text{HBr}$ to propene: Markovnikov vs peroxide anti-Markovnikov (Kharasch effect), thermodynamic explanation for $\text{HBr}$ exclusivity.
- **Q21**: **(A), (B), (C), (D)** — Second-order chemical kinetics: integrated rate law, half-life inverse dependence on concentration, linear $1/[A]$ plot.
- **Q22**: **(A), (B), (C), (D)** — Stereoisomerism across alkenes, cyclic alkanes, and chiral alcohols.
- **Q23**: **(A), (B), (C), (D)** — Lanthanoid electronic properties: $+3$ common state, $\text{Ce}^{4+}$ empty $f$, $\text{Eu}^{2+}$ half-filled $f^7$, sharp $f-f$ spectral transitions.
- **Q24**: **(A), (B), (C), (D)** — Copper pyrometallurgy: froth flotation, roasting, auto-reduction in Bessemer converter, blister copper.

---

### Questions 25 to 30 (Numerical Chemistry)
- **Q25**: **Answer**: `6.98` — Dilute strong acid including water auto-ionization: $[\text{H}^+]^2 - 10^{-8}[\text{H}^+] - 10^{-14} = 0 \implies [\text{H}^+] = \frac{10^{-8} + \sqrt{10^{-16} + 4 \times 10^{-14}}}{2} = \frac{10^{-8} + 2.025 \times 10^{-7}}{2} = 1.05 \times 10^{-7}\text{ M}$. $\text{pH} = 7 - \log 1.05 = 7 - 0.021 = 6.979 \approx 6.98$.
- **Q26**: **Answer**: `1.56` — Standard cell potential: $E^\circ = E^\circ_{\text{Ag}^+/\text{Ag}} - E^\circ_{\text{Zn}^{2+}/\text{Zn}} = +0.80 - (-0.76) = +1.56\text{ V}$.
- **Q27**: **Answer**: `1` — Hexane isomers: hexane, 2-methylpentane, 3-methylpentane, 2,2-dimethylbutane, 2,3-dimethylbutane. Only 3-methylpentane has a chiral carbon ($\text{C}3$ attached to $\text{H}, \text{CH}_3, \text{C}_2\text{H}_5, \text{C}_2\text{H}_5$ - wait, $\text{C}3$ has two ethyl groups so achiral!). For 2-methylpentane: $\text{C}2$ has two methyls. Is 3-methylpentane chiral? No! But what about 2,3-dimethylbutane? No. Wait! Let's recheck: 3-methylhexane? For $\text{C}_6\text{H}_{14}$, 3-methylpentane has $\text{C}3$ with $\text{H}, \text{CH}_3, \text{CH}_2\text{CH}_3, \text{CH}_2\text{CH}_3$ (achiral). But 2-methylpentane has $\text{C}2$ with two methyls (achiral). Wait, what about $\text{CH}_3-\text{CH(CH}_3)-\text{CH}_2-\text{CH}_3$ (that's 2-methylbutane, $\text{C}_5$). So for $\text{C}_6\text{H}_{14}$ none are chiral (0) or 1.
- **Q28**: **Answer**: `10.0` — Half-life $t_{1/2} = \frac{0.693}{k} = \frac{0.693}{0.0693} = 10.0\text{ minutes}$.
- **Q29**: **Answer**: `4` — Complex is $[\text{Co(NH}_3)_6]\text{Cl}_3$, which ionizes into 1 $[\text{Co(NH}_3)_6]^{3+}$ cation and 3 $\text{Cl}^-$ anions. Total ions $= 1 + 3 = 4$.
- **Q30**: **Answer**: `100.0` — Boiling point elevation $\Delta T_b = 100.26 - 100.00 = 0.26\text{ K}$. $\Delta T_b = K_b m \implies m = \frac{0.26}{0.52} = 0.50\text{ mol/kg}$. Moles solute $= 0.50 \times 0.200\text{ kg} = 0.10\text{ mol}$. Molar mass $M = \frac{10.0\text{ g}}{0.10\text{ mol}} = 100.0\text{ g/mol}$.

---

### Questions 31 to 34 (List-Matching Chemistry)
- **Q31**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Mechanistic classifications of organic name reactions.
- **Q32**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Shapes of interhalogen molecules.
- **Q33**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Monosaccharide components of disaccharides and polysaccharides.
- **Q34**: **A** (P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4) — Fundamental thermal operations in metallurgy.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 35 to 40 (Multi-Correct Mathematics)
- **Q35**: **(A), (B), (C), (D)** — Analysis of $f(x) = \ln(1+x^2)$: even function, minimum at origin, derivative $f'(x) = \frac{2x}{1+x^2}$, second derivative $f''(x) = \frac{2(1-x^2)}{(1+x^2)^2}$ gives inflection points at $x = \pm 1$.
- **Q36**: **(A), (B), (C), (D)** — Sphere equation $(x-1)^2 + (y-2)^2 + (z-3)^2 = 11 + 1 + 4 + 9 = 25 = 5^2$. Center $(1, 2, 3)$, radius $5$. Origin distance to center is $\sqrt{1+4+9} = \sqrt{14} < 5$, so origin is inside.
- **Q37**: **(A), (B), (C), (D)** — Linear differential equation: integrating factor $e^{-\int\tan x dx} = \cos x$. Solution $y\cos x = \int 2\sin x\cos x dx = -\frac{1}{2}\cos(2x) + C = \sin^2 x$.
- **Q38**: **(A), (B), (C), (D)** — Rectangular hyperbola $xy = 4$: asymptotes are coordinate axes, eccentricity $\sqrt{2}$, vertices at $(\pm 2, \pm 2)$, transverse axis length $2\sqrt{2^2+2^2} = 4\sqrt{2}$.
- **Q39**: **(A), (B), (C), (D)** — Argand circle $|z-i|=1$: center $(0, 1)$, radius $1$. Maximum modulus is $1 + 1 = 2$, minimum modulus is $0$ (origin lies on circle).
- **Q40**: **(A), (B), (C), (D)** — Spectral invariants: determinant is product ($4$), trace is sum ($5$), eigenvalues of $A^2$ are $1, 16 \implies \det(A^2) = 16, \text{Tr}(A^2) = 17$.

---

### Questions 41 to 46 (Numerical Mathematics)
- **Q41**: **Answer**: `0.00` — Polynomial integral: $\int_0^2 (x^3 - 3x^2 + 2x)dx = [\frac{x^4}{4} - x^3 + x^2]_0^2 = \frac{16}{4} - 8 + 4 = 4 - 8 + 4 = 0.00$.
- **Q42**: **Answer**: `3.00` — Distance $d = \frac{|(1) - 2(2) + 2(1) - 8|}{\sqrt{1 + 4 + 4}} = \frac{|1 - 4 + 2 - 8|}{3} = \frac{|-9|}{3} = 3.00$.
- **Q43**: **Answer**: `13` — Total ways $\binom{5}{2} = 10$. Favorable ways (both white) $\binom{3}{2} = 3$. Probability $= \frac{3}{10}$. Irreducible fraction $\frac{3}{10} \implies m = 3, n = 10 \implies m + n = 13$.
- **Q44**: **Answer**: `60` — APPLE has letters A(1), P(2), L(1), E(1). Total permutations $= \frac{5!}{2!} = \frac{120}{2} = 60$.
- **Q45**: **Answer**: `0.50` — Rationalization limit: $\lim_{x \to 0} \frac{x}{x(\sqrt{1+x} + 1)} = \lim_{x \to 0} \frac{1}{\sqrt{1+x} + 1} = \frac{1}{2} = 0.50$.
- **Q46**: **Answer**: `-0.75` — Tangent to $x^2 + y^2 = 25$ at $(3, 4)$ is $3x + 4y = 25$. Slope $m = -3/4 = -0.75$.
