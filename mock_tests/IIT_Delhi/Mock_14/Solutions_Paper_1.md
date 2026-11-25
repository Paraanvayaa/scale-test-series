# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 14

---

### PART I: PHYSICS

#### Solution 1: Mandelstam Relativistic Invariants
1. **Core Concept**:
   In relativistic kinematics, $s = (P_1 + P_2)^2 = (E_1 + E_2)^2/c^2 - (\vec{p}_1 + \vec{p}_2)^2$. In the CM frame, $\vec{p}_1 + \vec{p}_2 = \vec{0}$, hence $s = E_{\text{cm}}^2/c^2$.
2. **Four-Momentum Sum**:
   Expanding $s + t + u = (P_1 + P_2)^2 + (P_1 - P_3)^2 + (P_1 - P_4)^2$ using $P_1 + P_2 = P_3 + P_4$ yields $\sum m_i^2 c^2$.
3. **Four-Momentum Transfer**:
   $t = (P_1 - P_3)^2 = 2m^2 c^2 - 2(E_1 E_3/c^2 - \vec{p}_1 \cdot \vec{p}_3) = -2|\vec{p}^*|^2 (1 - \cos\theta^*)$.
- **Correct Option**: (A, B, C, D)

#### Solution 2: Electromagnetic Skin Depth
1. **Wave Equation in Conductor**:
   $\nabla^2 \vec{E} = \mu \sigma \frac{\partial \vec{E}}{\partial t} \implies k^2 = i\mu_0 \sigma \omega$.
2. **Complex Wavevector**:
   $k = \sqrt{i}\sqrt{\mu_0 \sigma \omega} = \frac{1 + i}{\sqrt{2}}\sqrt{\mu_0 \sigma \omega} = (1 + i)\sqrt{\frac{\mu_0 \sigma \omega}{2}}$.
3. **Attenuation & Phase**:
   Field attenuates as $e^{-z/\delta}$ where $\delta = \sqrt{\frac{2}{\mu_0 \sigma \omega}}$. The factor $(1+i) = \sqrt{2} e^{i\pi/4}$ implies a $45^\circ$ phase lag of $\vec{B}$ relative to $\vec{E}$.
- **Correct Option**: (A, B, C, D)

#### Solution 3: Euler's Rigid Body Equations & Intermediate Axis Instability
- Conservation of kinetic energy $2T = I_1 \omega_1^2 + I_2 \omega_2^2 + I_3 \omega_3^2$ and angular momentum $L^2 = I_1^2 \omega_1^2 + I_2^2 \omega_2^2 + I_3^2 \omega_3^2$.
- Perturbation analysis around $\omega_1$: linearized perturbation equation gives $\ddot{\eta} = -\Omega^2 \eta$, giving stable harmonic oscillations.
- Perturbation analysis around $\omega_2$: linearized perturbation gives $\ddot{\eta} = +\Omega^2 \eta$, yielding exponential divergence (unstable).
- Perturbation analysis around $\omega_3$: stable harmonic oscillations.
- **Correct Option**: (A, B, C, D)

#### Solution 4: Clausius-Clapeyron Phase Transition
- Ideal gas vapor volume $V_{\text{vap}} \approx \frac{RT}{P} \gg V_{\text{liq}} \implies \frac{dP}{dT} = \frac{\Delta H_{\text{vap}} P}{R T^2} \implies \ln P = -\frac{\Delta H_{\text{vap}}}{RT} + C$.
- At the critical point, latent heat vanishes and the phase boundary ends.
- For water, density of ice is less than water, $\Delta V_{\text{fus}} = V_{\text{liq}} - V_{\text{ice}} < 0$, making $\frac{dP}{dT} < 0$.
- **Correct Option**: (A, B, C, D)

#### Solution 5: Transmission Line Characteristics
- Follows directly from telegrapher's equations: $Z_0 = \sqrt{L'/C'}$, $v = 1/\sqrt{L'C'}$, $\Gamma_V = \frac{Z_L - Z_0}{Z_L + Z_0}$.
- **Correct Option**: (A, B, C, D)

#### Solution 6: Magnetic Dipole on Axis of Current Loop
- Field on axis: $B(x) = \frac{\mu_0 I R^2}{2(R^2 + x^2)^{3/2}} \approx \frac{\mu_0 I R^2}{2 x^3}$.
- Energy $U = -\vec{m} \cdot \vec{B} = -m B(x) = -\frac{\mu_0 m I R^2}{2 x^3}$.
- Force $F = -\frac{dU}{dx} = -\frac{3\mu_0 m I R^2}{2 x^4}$ (attractive towards the loop).
- **Correct Option**: (A, B, C, D)

#### Solution 7: Relativistic Cyclotron Energy Limit
- Frequency mismatch: $\frac{\Delta f}{f_0} = \frac{f_0 - f}{f_0} = 1 - \frac{1}{\gamma} = 0.01$.
- $\frac{1}{\gamma} = 0.99 \implies \gamma = \frac{1}{0.99} \approx 1.0101$.
- Kinetic energy: $K_{\text{max}} = (\gamma - 1) m_0 c^2 \approx 0.0101 \times 938\text{ MeV} \approx 9.5\text{ MeV}$.
- **Answer**: 9.5

#### Solution 8: Skin Depth in Copper
- $\omega = 2\pi f = 2\pi \times 10^7\text{ rad/s}$.
- $\delta = \sqrt{\frac{2}{\mu_0 \sigma \omega}} = \sqrt{\frac{2}{(4\pi \times 10^{-7}) (5.8 \times 10^7) (2\pi \times 10^7)}} = \sqrt{\frac{2}{4\pi^2 \times 5.8 \times 10^7 \times 10^{-7} \times 10^7}} = \frac{1}{2\pi \times 10^3 \sqrt{5.8}} \approx 20.9\text{ }\mu\text{m}$.
- **Answer**: 20.9

#### Solution 9: Carnot Heat Pump Power
- $\text{COP}_{\text{HP}} = \frac{T_H}{T_H - T_C} = \frac{294}{294 - 260} = \frac{294}{34} \approx 8.647$.
- Power required: $W_{\text{in}} = \frac{Q_H}{\text{COP}} = \frac{17.0\text{ kW}}{8.647} \approx 1.97\text{ kW}$.
- **Answer**: 1.97

#### Solution 10: Ballistic Galvanometer
- Angular impulse: $\int \tau dt = N B A \int I dt = N B A Q = I_{\text{coil}} \omega_0$.
- Initial kinetic energy: $\frac{1}{2} I_{\text{coil}} \omega_0^2 = \frac{(N B A Q)^2}{2 I_{\text{coil}}}$.
- Equating to maximum torsional potential energy: $\frac{1}{2} k \theta_{\text{max}}^2 = \frac{(N B A Q)^2}{2 I_{\text{coil}}} \implies \theta_{\text{max}} = \frac{N B A Q}{\sqrt{k I_{\text{coil}}}}$.
- $N B A Q = 0.05 \times 20 \times 10^{-6} = 1.0 \times 10^{-6}\text{ N}\cdot\text{m}\cdot\text{s}$.
- $\sqrt{k I_{\text{coil}}} = \sqrt{(6.17 \times 10^{-7}) (2.5 \times 10^{-7})} = \sqrt{1.5425 \times 10^{-13}} \approx 3.927 \times 10^{-7}$.
- $\theta_{\text{max}} = \frac{1.0 \times 10^{-6}}{3.927 \times 10^{-7}} \approx 2.546\text{ rad} \approx 146^\circ$.
- **Answer**: 146

#### Solution 11: Tuning Fork Wax Loading
- Adding wax increases inertia, decreasing frequency: $f_L = f_0 - 4 = 440 - 4 = 436\text{ Hz}$.
- **Answer**: 436

#### Solution 12: Glass Sphere Deviation
- Angle of incidence $i = 60^\circ$. By Snell's law: $1 \cdot \sin 60^\circ = \sqrt{3} \sin r \implies \frac{\sqrt{3}}{2} = \sqrt{3}\sin r \implies \sin r = 1/2 \implies r = 30^\circ$.
- Total deviation for 1 internal reflection: $\delta = (i - r) + (\pi - 2r) + (i - r) = 2i - 4r + 180^\circ$.
- $\delta = 2(60^\circ) - 4(30^\circ) + 180^\circ = 120^\circ - 120^\circ + 180^\circ = 180^\circ$.
- **Answer**: 180

#### Solution 13 to 18:
- 13: $V'(x_0) = k x_0 - 2\alpha/x_0^3 = 0 \implies x_0^4 = 2\alpha/k$. $V''(x_0) = k + 6\alpha/x_0^4 = k + 3k = 4k$. $\omega = \sqrt{V''(x_0)/m} = 2\sqrt{k/m}$. (A)
- 14: Equal amplitudes on fast and slow axes with $\pi/2$ phase shift produces circularly polarized light. (A)
- 15: When vertical, angular acceleration is zero ($\tau = 0$), so the tangential acceleration of CM is zero; hence the horizontal reaction force is zero. (A)
- 16: $I(t) = I_0(1 - e^{-t/\tau}) = 0.5 I_0 \implies e^{-t/\tau} = 1/2 \implies t = \tau \ln 2 = \frac{L}{r}\ln 2$. (A)
- 17: Stefan-Boltzmann law $P \propto T^4 \implies (1.20)^4 \approx 2.07$. (A)
- 18: $f_1 = v/(2L)$, closed-open pipe fundamental $f_1' = v/(4L) = f_1/2$. (A)

---

### PART II: CHEMISTRY

#### Solution 19: Wade's Rules
- Closo: $(n+1)$ pairs, Nido: $(n+2)$ pairs, Arachno: $(n+3)$ pairs.
- Each $B-H$ unit has 4 valence electrons: 2 used in exo $B-H$ bond, 2 contributed to cluster cage.
- **Correct Option**: (A, B, C, D)

#### Solution 20: Julia Olefination
- Explains the mechanism: carbanion formation, addition to aldehyde, acetylation, and reductive elimination with $\text{Na/Hg}$ to give $(E)$-alkene.
- **Correct Option**: (A, B, C, D)

#### Solution 21: Debye-Hückel Limiting Law
- All statements (A, B, C, D) reflect the fundamental theory of ionic atmospheres.
- **Correct Option**: (A, B, C, D)

#### Solution 22: Edman Degradation
- Cyclic degradation allows sequential N-terminal cleavage without digesting internal peptide bonds.
- **Correct Option**: (A, B, C, D)

#### Solution 23: Allotropes of Phosphorus
- White $P_4$ strain ($60^\circ$ angles), red polymeric, black layered conductor, and disproportionation with $\text{NaOH}$ to $\text{PH}_3 + \text{NaH}_2\text{PO}_2$.
- **Correct Option**: (A, B, C, D)

#### Solution 24: Hydroformylation Mechanism
- Classic catalytic cycle of the oxo process.
- **Correct Option**: (A, B, C, D)

#### Solution 25: Solubility Product of CaF2
- $\text{CaF}_2 \rightleftharpoons \text{Ca}^{2+} + 2\text{F}^-$.
- $K_{sp} = S \times (2S)^2 = 4 S^3 = 4 (2.0 \times 10^{-4})^3 = 4 \times 8.0 \times 10^{-12} = 3.2 \times 10^{-11}$.
- $X = 3.20$.
- **Answer**: 3.20

#### Solution 26: First-Order Azomethane Decomposition
- $A \to B + C$. At time $t$: $P_t = P_0 + x \implies x = P_t - P_0 = 150 - 100 = 50\text{ mm Hg}$.
- Remaining reactant $P_A = P_0 - x = 100 - 50 = 50\text{ mm Hg} = P_0 / 2$.
- Thus $t = t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{3.46 \times 10^{-4}} = 2003\text{ s} \approx 2003$.
- **Answer**: 2003

#### Solution 27: Redox Titration Stoichiometry
- Moles of $\text{Cr}_2\text{O}_7^{2-} = 0.025 \times 0.020 = 5.0 \times 10^{-4}\text{ mol}$.
- Stoichiometry: $1\text{ mol } \text{Cr}_2\text{O}_7^{2-} \equiv 6\text{ mol } \text{Fe}^{2+}$.
- Moles of $\text{Fe}^{2+} = 6 \times 5.0 \times 10^{-4} = 3.0 \times 10^{-3}\text{ mol}$.
- Molarity $= \frac{3.0 \times 10^{-3}\text{ mol}}{0.050\text{ L}} = 0.060\text{ M}$.
- **Answer**: 0.06

#### Solution 28: Standard Gibbs Free Energy of Formation
- $\Delta G_f^\circ = \Delta H_f^\circ - T \Delta S^\circ = -285.8\text{ kJ} - 298(-0.1632)\text{ kJ} = -285.8 + 48.63 = -237.17\text{ kJ/mol} \approx -237.2\text{ kJ/mol}$.
- Absolute magnitude $= 237.2$.
- **Answer**: 237.2

#### Solution 29: FCC Unit Cell Density
- For FCC, $Z = 4$.
- $\rho = \frac{Z M}{N_A a^3} \implies M = \frac{\rho N_A a^3}{Z}$.
- $a = 400\text{ pm} = 4.0 \times 10^{-8}\text{ cm} \implies a^3 = 6.4 \times 10^{-23}\text{ cm}^3$.
- $M = \frac{10.0 \times (6.022 \times 10^{23}) \times (6.4 \times 10^{-23})}{4} = \frac{385.4}{4} \approx 96.4\text{ g/mol}$.
- **Answer**: 96.4

#### Solution 30: Ostwald's Dilution Law
- Degree of dissociation $\alpha = \frac{\Lambda_m}{\Lambda_m^\circ} = \frac{16.5}{390.5} \approx 0.04225$.
- $K_a = \frac{c \alpha^2}{1 - \alpha} \approx c \alpha^2 = 0.010 \times (0.04225)^2 = 1.785 \times 10^{-5}\text{ mol/L}$.
- $Y = 1.79$.
- **Answer**: 1.79

#### Solution 31 to 36:
- 31: Formation of strong $\text{C}=\text{O}$ bond in carbonyl sulfide. (A)
- 32: Both Marshall's acid ($\text{H}_2\text{S}_2\text{O}_8$) and Caro's acid ($\text{H}_2\text{SO}_5$) contain peroxy bonds. (C)
- 33: $\text{NH}_3$ ($-3$) to $\text{NO}$ ($+2$). (A)
- 34: Peroxide effect gives anti-Markovnikov bromide: 1-bromo-2-methylcyclohexane. (A)
- 35: Pentaamminecarbonatocobalt(III) chloride. (A)
- 36: Hardy-Schulze rule: higher cation charge has higher coagulating power: $\text{Na}^+ < \text{Ba}^{2+} < \text{Al}^{3+}$. (A)

---

### PART III: MATHEMATICS

#### Solution 37: Gamma and Beta Functions
- All standard integral representations and identities.
- **Correct Option**: (A, B, C, D)

#### Solution 38: Spectral Theorem for Symmetric Matrices
- Real eigenvalues, orthogonal eigenspaces, Rayleigh quotient bounds, and Sylvester's law of inertia.
- **Correct Option**: (A, B, C, D)

#### Solution 39: Ellipsoid Properties
- The locus of intersection of 3 mutually perpendicular tangent planes is the director sphere $x^2 + y^2 + z^2 = a^2 + b^2 + c^2$.
- Maximum inscribed box volume: $8(a/\sqrt{3})(b/\sqrt{3})(c/\sqrt{3}) = \frac{8abc}{3\sqrt{3}}$.
- **Correct Option**: (A, B, C, D)

#### Solution 40: Bessel Function Frobenius Series
- Standard Frobenius method for $J_0(x)$.
- **Correct Option**: (A, B, C, D)

#### Solution 41: Sinc Function Integrals
- Standard Dirichlet and Fejér-type sinc integrals.
- **Correct Option**: (A, B, C, D)

#### Solution 42: Normal Variable Distributions
- Note: The Cauchy distribution has undefined mean (the integral $\int_{-\infty}^\infty \frac{w}{1+w^2}dw$ diverges). Thus (D) is false. Statements (A, B, C) are correct.
- **Correct Option**: (A, B, C)

#### Solution 43: Definite Integral
- Let $x = \tan\theta \implies dx = \sec^2\theta d\theta$.
- $I = \int_0^{\pi/4} \ln(1 + \tan\theta) d\theta$.
- Using King's property $\theta \to \pi/4 - \theta$:
  $1 + \tan(\pi/4 - \theta) = 1 + \frac{1 - \tan\theta}{1 + \tan\theta} = \frac{2}{1 + \tan\theta}$.
- $2I = \int_0^{\pi/4} \ln 2 d\theta = \frac{\pi}{4}\ln 2 \implies I = \frac{\pi}{8}\ln 2$.
- $\frac{64 I}{\pi \ln 2} = \frac{64 (\pi/8 \ln 2)}{\pi \ln 2} = 8$.
- **Answer**: 8

#### Solution 44: Integer Solutions with Constraint
- Total non-negative solutions of $x + y + z + w = 15$ is $\binom{15 + 4 - 1}{4 - 1} = \binom{18}{3} = \frac{18 \times 17 \times 16}{6} = 816$.
- Solutions with $x \ge 4$: let $x' = x - 4 \ge 0$, then $x' + y + z + w = 11$.
  Number of solutions $= \binom{11 + 4 - 1}{3} = \binom{14}{3} = \frac{14 \times 13 \times 12}{6} = 364$.
- Solutions with $x \le 3$: $816 - 364 = 452$.
- **Answer**: 452

#### Solution 45: Line-Plane Intersection
- Parametric point on line: $x = 1 + 2t$, $y = -2 - 3t$, $z = 4 + t$.
- Substitute into plane $2(1 + 2t) + 4(-2 - 3t) - (4 + t) + 1 = 0$:
  $2 + 4t - 8 - 12t - 4 - t + 1 = 0 \implies -9 - 9t = 0 \implies t = -1$.
- Point $P$: $\alpha = 1 - 2 = -1$, $\beta = -2 + 3 = 1$, $\gamma = 4 - 1 = 3$.
- $\alpha^2 + \beta^2 + \gamma^2 = (-1)^2 + 1^2 + 3^2 = 1 + 1 + 9 = 11$.
- **Answer**: 11

#### Solution 46: Cube Roots Determinant
- Column operation $C_1 \to C_1 + C_2 + C_3$:
  First column becomes $1 + \omega + \omega^2 = 0$.
  Therefore, $\Delta = 0$.
- **Answer**: 0

#### Solution 47: Linear First-Order ODE
- Integrating factor: $I.F. = e^{\int \cot x dx} = e^{\ln\sin x} = \sin x$.
- Solution: $y \sin x = \int 2\cos x \sin x dx = \int \sin 2x dx = -\frac{1}{2}\cos 2x + C$.
- Condition $y(\pi/2) = 1$: $1 \cdot 1 = -\frac{1}{2}(-1) + C = \frac{1}{2} + C \implies C = \frac{1}{2}$.
- $y \sin x = \frac{1 - \cos 2x}{2} = \sin^2 x \implies y = \sin x$.
- At $x = \pi/6$: $y(\pi/6) = \sin(\pi/6) = 0.5$.
- **Answer**: 0.5

#### Solution 48: Hypergeometric Variance
- Population $N = 10$, successes $K = 4$, sample size $n = 3$.
- Mean $\mu = n \frac{K}{N} = 3 \times \frac{4}{10} = 1.2$.
- Variance $\text{Var}(X) = n \frac{K}{N} \left(1 - \frac{K}{N}\right) \frac{N - n}{N - 1} = 3 (0.4) (0.6) \frac{10 - 3}{10 - 1} = 0.72 \times \frac{7}{9} = 0.56$.
- **Answer**: 0.56

#### Solution 49 to 54:
- 49: Classic Euler log-sine integral $= -\frac{\pi}{2}\ln 2$. (A)
- 50: Ratio test $\lim \frac{a_{n+1}}{a_n} = \lim \frac{(n+1)!}{(n+1)^{n+1}} \frac{n^n}{n!} = \lim \left(\frac{n}{n+1}\right)^n = \frac{1}{e} \implies R = e$. (A)
- 51: Standard distance between skew lines $\frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|} = \frac{1}{\sqrt{6}}$. (A)
- 52: $|3AB| = 3^3 |A| |B| = 27 (-1) (3) = -81$. (A)
- 53: $f'(x) = e^x + 1 > 0$ strictly increasing, exactly 1 real root. (A)
- 54: $|\vec{a}+\vec{b}+\vec{c}|^2 = 3 + 2(\vec{a}\cdot\vec{b} + \vec{b}\cdot\vec{c} + \vec{c}\cdot\vec{a}) = 0 \implies \sum = -3/2$. (A)
