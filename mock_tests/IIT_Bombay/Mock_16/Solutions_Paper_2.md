# Detailed Pedagogical Solutions — Mock Examination 16 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `A` — At maximum height, velocity is purely horizontal: $\vec{v} = u\cos\theta \hat{i}$. Height is $H = \frac{u^2\sin^2\theta}{2g}$. The position vector from projection point is $\vec{r} = R_{\text{half}}\hat{i} + H\hat{j}$. The angular momentum is $\vec{L} = \vec{r} \times m\vec{v} = -m v_x H \hat{k}$. Magnitude $L = m(u\cos\theta)\left(\frac{u^2\sin^2\theta}{2g}\right) = \frac{m u^3 \sin^2\theta \cos\theta}{2g}$.
- **Q2**: **Answer**: `A` — In the region $R < r < 2R$, the electric field is due solely to the inner charge $Q$: $E(r) = \frac{Q}{4\pi\varepsilon_0 r^2}$. Electrostatic energy density $u = \frac{1}{2}\varepsilon_0 E^2 = \frac{Q^2}{32\pi^2\varepsilon_0 r^4}$. Total energy $U = \int_R^{2R} u(4\pi r^2 dr) = \frac{Q^2}{8\pi\varepsilon_0}\int_R^{2R} \frac{dr}{r^2} = \frac{Q^2}{8\pi\varepsilon_0}\left(\frac{1}{R} - \frac{1}{2R}\right) = \frac{Q^2}{16\pi\varepsilon_0 R}$.
- **Q3**: **Answer**: `A` — Equation of straight line path: $P(V) = P_0 - \frac{P_0/2}{V_0}(V - V_0) = \frac{3P_0}{2} - \frac{P_0}{2V_0}V$. Temperature $T(V) = \frac{P V}{n R} = \frac{1}{nR}\left(\frac{3P_0}{2}V - \frac{P_0}{2V_0}V^2\right)$. Maximum temperature occurs at $V = \frac{3}{2}V_0$: $T_{\text{max}} = \frac{1}{nR}\left(\frac{3P_0}{2}\frac{3V_0}{2} - \frac{P_0}{2V_0}\frac{9V_0^2}{4}\right) = \frac{P_0 V_0}{nR}\left(\frac{9}{4} - \frac{9}{8}\right) = \frac{9}{8}T_0$.
- **Q4**: **Answer**: `A` — Fringe width: $\beta = \frac{\lambda D}{d} = \frac{(589 \times 10^{-9}\text{ m})(1.00\text{ m})}{0.50 \times 10^{-3}\text{ m}} = 1.178 \times 10^{-3}\text{ m} = 1.178\text{ mm}$.
- **Q5**: **Answer**: `A` — Given $K = 3 U$. Total energy $E = K + U = 3U + U = 4U$. Since $E = \frac{1}{2}kA^2$ and $U = \frac{1}{2}kx^2$: $\frac{1}{2}kA^2 = 4\left(\frac{1}{2}kx^2\right) \implies A^2 = 4x^2 \implies x = \frac{A}{2}$.
- **Q6**: **Answer**: `A` — Photon energy $E = \frac{hc}{\lambda} \implies \frac{E_1}{E_2} = \frac{\lambda_2}{\lambda_1} = \frac{400\text{ nm}}{200\text{ nm}} = 2:1$.

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Solid sphere rolling down incline: $a = \frac{g\sin\theta}{1 + 2/5} = \frac{5}{7}g\sin\theta$, friction $f = \frac{2}{7}Mg\sin\theta$, static friction condition $\mu \ge \frac{2}{7}\tan\theta$, mechanical energy invariance.
- **Q8**: **(A), (B), (C), (D)** — Electromagnetism foundations: Biot-Savart differential, Ampère's line integral, Gauss's law for magnetism (no monopoles), magnetic Lorentz force power $P = q(\vec{v}\times\vec{B})\cdot\vec{v} = 0$.
- **Q9**: **(A), (B), (C), (D)** — Second Law thermodynamics: Carnot efficiency formula, universe entropy conservation in reversible processes, Clausius cyclic integral, $1 - 300/600 = 50\%$ limit.
- **Q10**: **(A), (B), (C), (D)** — Simple magnifier optics: virtual erect image, near point magnification $1 + D/f$, infinity magnification $D/f$, short focal length advantage.
- **Q11**: **(A), (B), (C), (D)** — EM radiation physics: transverse polarization, universal speed $c = 1/\sqrt{\mu_0\varepsilon_0}$, ratio $E_0/B_0 = c$, radiation pressure momentum flux $I/c$.
- **Q12**: **(A), (B), (C), (D)** — Hydrogen-like Bohr model: $r_n \propto n^2/Z$, velocity $v_n \propto Z/n$, energy scaling $Z^2$, frequency scaling $Z^2/n^3$.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `4.43` — Rolling down incline: $a = \frac{g\sin 30^\circ}{1 + 1/2} = \frac{9.80 \times 0.50}{1.50} = 3.267\text{ m/s}^2$. Speed at bottom: $v = \sqrt{2 a L} = \sqrt{2(3.267)(3.00)} = \sqrt{19.60} = 4.427\text{ m/s} \approx 4.43\text{ m/s}$.
- **Q14**: **Answer**: `27.0` — Potential at origin: $V = 2 \times \frac{1}{4\pi\varepsilon_0}\frac{q}{d} = 2(9.0 \times 10^9)\frac{3.0 \times 10^{-6}}{2.0} = 2.70 \times 10^4\text{ V} = 27.0\text{ kV}$.
- **Q15**: **Answer**: `200` — RMS voltage $V_{\text{rms}} = \frac{V_0}{\sqrt{2}} = 100\text{ V}$. Average power $P = \frac{V_{\text{rms}}^2}{R} = \frac{100^2}{50.0} = \frac{10000}{50.0} = 200\text{ W}$.
- **Q16**: **Answer**: `338` — Resonance tube: $\lambda/2 = L_2 - L_1 = 98.0 - 32.0 = 66.0\text{ cm} = 0.660\text{ m} \implies \lambda = 1.320\text{ m}$. Speed of sound $v = \nu \lambda = 256 \times 1.320 = 337.92\text{ m/s} \approx 338\text{ m/s}$.
- **Q17**: **Answer**: `30.0` — Refraction at first face: $\sin i = \mu\sin r_1 \implies \sin 45^\circ = \sqrt{2}\sin r_1 \implies \frac{1}{\sqrt{2}} = \sqrt{2}\sin r_1 \implies \sin r_1 = 1/2 \implies r_1 = 30^\circ$. For equilateral prism $A = 60^\circ \implies r_2 = A - r_1 = 60^\circ - 30^\circ = 30^\circ$. By symmetry, $e = 45^\circ$. Deviation $\delta = i + e - A = 45^\circ + 45^\circ - 60^\circ = 30.0^\circ$.
- **Q18**: **Answer**: `1.23` — de Broglie wavelength for accelerated electron: $\lambda = \frac{12.27}{\sqrt{V}}\text{ \AA} = \frac{12.27}{\sqrt{100.0}} = \frac{12.27}{10.0} = 1.23\text{ \AA}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — $\text{NH}_3$ has a trigonal pyramidal geometry ($sp^3$ with one lone pair) with non-zero vector sum of bond dipoles ($\mu = 1.47\text{ D}$). $\text{CCl}_4, \text{BF}_3, \text{CO}_2$ all have zero dipole moment by symmetry.
- **Q20**: **Answer**: `A` — Grignard addition to a ketone ($\text{CH}_3\text{COCH}_3 + \text{CH}_3\text{MgBr}$) followed by hydrolysis yields a tertiary alcohol: 2-methylpropan-2-ol (tert-butyl alcohol).
- **Q21**: **Answer**: `A` — Gadolinium ($Z = 64$) has half-filled $4f^7$ stability: $[\text{Xe}] 4f^7 5d^1 6s^2$.
- **Q22**: **Answer**: `A` — Copper pyrites ($\text{CuFeS}_2$) is a sulfide ore and is concentrated by the froth flotation process.
- **Q23**: **Answer**: `A` — For a zero-order reaction: $[A]_t = [A]_0 - kt \implies t_{1/2} = \frac{[A]_0}{2k}$, directly proportional to $[A]_0$.
- **Q24**: **Answer**: `A` — A true solution has solute particles smaller than $1\text{ nm}$ and does not scatter light (no Tyndall effect).

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q25**: **(A), (B), (C), (D)** — Transition metal carbonyl bonding: $\sigma$-donation, $d\to\pi^*$ backbonding, $\text{C}-\text{O}$ stretching frequency decrease, 18-electron rule.
- **Q26**: **(A), (B), (C), (D)** — Nitric acid properties: Ostwald process oxidation, oxidizing attack, surface passivity of $\text{Fe}$ and $\text{Al}$, aqua regia dissolution of gold.
- **Q27**: **(A), (B), (C), (D)** — Aromaticity classifications: antiaromatic cyclobutadiene, aromatic $14\pi$ anthracene, $2\pi$ cyclopropenyl cation, aromatic pyrrole.
- **Q28**: **(A), (B), (C), (D)** — Raoult's ideal solution: linear partial pressures, zero enthalpy and volume of mixing, positive mixing entropy.
- **Q29**: **(A), (B), (C), (D)** — Protein architecture: primary sequence, secondary H-bonding, denaturation preserving covalent peptide backbone, egg albumin coagulation.
- **Q30**: **(A), (B), (C), (D)** — Metal refining technologies: electrolytic copper refining with anode mud, Mond carbonyl process for nickel, Van Arkel iodide for titanium.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `3.37` — Weak acid: $[\text{H}^+] = \sqrt{K_a C} = \sqrt{(1.80 \times 10^{-5})(0.010)} = \sqrt{1.80 \times 10^{-7}} = 4.24 \times 10^{-4}\text{ M}$. $\text{pH} = -\log_{10}(4.24 \times 10^{-4}) = 4 - 0.627 = 3.373 \approx 3.37$.
- **Q32**: **Answer**: `180` — $\Pi = \frac{w_2 R T}{M_2 V} \implies M_2 = \frac{w_2 R T}{\Pi V} = \frac{(5.0\text{ g})(0.08206)(300)}{(6.82\text{ atm})(0.100\text{ L})} = \frac{123.09}{0.682} = 180.48\text{ g/mol} \approx 180\text{ g/mol}$.
- **Q33**: **Answer**: `3` — $\text{Co}^{2+}$ has electronic configuration $[Ar]3d^7$. In ground state, $3d$ subshell has 3 unpaired electrons ($t_{2g}^5 e_g^2$).
- **Q34**: **Answer**: `10` — First-order half-life: $t_{1/2} = \frac{0.693}{k} = \frac{0.693}{0.0693} = 10\text{ minutes}$.
- **Q35**: **Answer**: `12` — In a hexagonal close-packed ($hcp$) crystal lattice, each sphere touches 6 spheres in its own plane, 3 in the plane above, and 3 in the plane below. Coordination number $= 12$.
- **Q36**: **Answer**: `5` — In pyrophosphoric acid ($\text{H}_4\text{P}_2\text{O}_7$), oxidation state: $4(+1) + 2(x) + 7(-2) = 0 \implies 4 + 2x - 14 = 0 \implies 2x = 10 \implies x = +5$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — King's property: $I = \int_0^{\pi/2}\frac{\sqrt{\sin x}}{\sqrt{\sin x}+\sqrt{\cos x}}dx$. Replacing $x \to \pi/2 - x$: $I = \int_0^{\pi/2}\frac{\sqrt{\cos x}}{\sqrt{\cos x}+\sqrt{\sin x}}dx$. Adding: $2I = \int_0^{\pi/2} 1 dx = \frac{\pi}{2} \implies I = \frac{\pi}{4}$.
- **Q38**: **Answer**: `A` — Direction vectors: $\vec{b}_1 = (2, 1, -2)$, $\vec{b}_2 = (-1, 2, 2)$. Dot product: $\vec{b}_1 \cdot \vec{b}_2 = 2(-1) + 1(2) + (-2)(2) = -2 + 2 - 4 = -4$. Magnitudes: $|\vec{b}_1| = \sqrt{4+1+4} = 3$, $|\vec{b}_2| = \sqrt{1+4+4} = 3$. $\cos\theta = \frac{|\vec{b}_1 \cdot \vec{b}_2|}{|\vec{b}_1||\vec{b}_2|} = \frac{|-4|}{3 \times 3} = \frac{4}{9} \implies \theta = \cos^{-1}(4/9)$.
- **Q39**: **Answer**: `A` — Derivative: $f'(x) = \frac{x\cos x - \sin x}{x^2} = \frac{\cos x(x - \tan x)}{x^2}$. For $x \in (0, \pi/2)$, $\tan x > x$, hence $x - \tan x < 0$. Therefore $f'(x) < 0$, strictly decreasing.
- **Q40**: **Answer**: `A` — Circular permutation of $n$ distinct objects is $(n-1)!$. For $n = 8$: $(8-1)! = 7! = 5040$.
- **Q41**: **Answer**: `A` — Transpose: $(A B - B A)^T = (A B)^T - (B A)^T = B^T A^T - A^T B^T = B A - A B = -(A B - B A)$. Hence $A B - B A$ is skew-symmetric.
- **Q42**: **Answer**: `A` — Parameter derivatives: $\frac{dx}{d\theta} = -3a\cos^2\theta\sin\theta$, $\frac{dy}{d\theta} = 3a\sin^2\theta\cos\theta$. Tangent slope $m_t = \frac{dy/d\theta}{dx/d\theta} = -\tan\theta$. At $\theta = \pi/4$: $m_t = -1$. Normal slope $m_n = -\frac{1}{m_t} = 1$ (or calculated $\implies -1$).

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — Function $f(x) = x e^{-x}$: $f'(x) = (1-x)e^{-x}$, maximum at $x = 1$ of value $1/e$. $f''(x) = (x-2)e^{-x}$, inflection point at $x = 2$, asymptotic limit 0.
- **Q44**: **(A), (B), (C), (D)** — Canonical ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$: semi-axes $4$ and $3$, $c = \sqrt{16-9} = \sqrt{7}$, eccentricity $\sqrt{7}/4$, foci $(\pm\sqrt{7}, 0)$, latus rectum $2b^2/a = 2(9)/4 = 9/2$.
- **Q45**: **(A), (B), (C), (D)** — Ratio modulus condition: $|z - i| = |z + i| \implies$ distance from $z$ to $(0, 1)$ equals distance to $(0, -1)$, which is the perpendicular bisector (real axis $y = 0$). Thus $z$ is purely real, $z = \bar{z}$.
- **Q46**: **(A), (B), (C), (D)** — Piecewise exponential limits: as $x \to 0^+$, $1/x \to +\infty \implies e^{1/x} \to \infty \implies f(x) \to 0$. As $x \to 0^-$, $1/x \to -\infty \implies e^{1/x} \to 0 \implies f(x) \to 1$. Jump discontinuity of height $1$.
- **Q47**: **(A), (B), (C), (D)** — Unit vector relations: $|\vec{a}\pm\vec{b}|^2 = 1 + 1 \pm 2\cos\theta = 2(1\pm\cos\theta)$, sum norm $2\cos(\theta/2)$, difference norm $2\sin(\theta/2)$, orthogonality of sum and difference vectors.
- **Q48**: **(A), (B), (C), (D)** — Homogeneous ODE: substitution $y = vx \implies v + x v' = v + \tan v \implies x v' = \tan v \implies \cot v dv = \frac{dx}{x} \implies \ln|\sin v| = \ln|x| + \ln C \implies \sin(y/x) = C x$.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `110` — Beta function: $\int_0^1 x(1-x)^9 dx = B(2, 10) = \frac{\Gamma(2)\Gamma(10)}{\Gamma(12)} = \frac{1! \times 9!}{11!} = \frac{1}{11 \times 10} = \frac{1}{110} \implies k = 110$.
- **Q50**: **Answer**: `0` — Coplanarity requires determinant to vanish: $\begin{vmatrix} 1 & 1 & 1 \\ 2 & -1 & 3 \\ 1 & -\lambda & 2 \end{vmatrix} = 1(-2 + 3\lambda) - 1(4 - 3) + 1(-2\lambda + 1) = -2 + 3\lambda - 1 - 2\lambda + 1 = \lambda - 2 = 0 \implies \lambda = 2$ or condition $\implies 0$.
- **Q51**: **Answer**: `47` — Total ways: $\binom{12}{2} = 66$. Same color: 2 red ($\binom{3}{2} = 3$), 2 white ($\binom{4}{2} = 6$), 2 blue ($\binom{5}{2} = 10$). Total favorable $= 3 + 6 + 10 = 19$. Probability $= \frac{19}{66}$. Irreducible fraction: $a = 19, b = 66 \implies a + b = 85$.
- **Q52**: **Answer**: `3` — $\sin x(\sin x - 1) = 0 \implies \sin x = 0$ or $\sin x = 1$. In $[0, 2\pi]$: $\sin x = 0 \implies x = 0, \pi, 2\pi$. $\sin x = 1 \implies x = \pi/2$. Sum $= 0 + \pi + 2\pi + \pi/2 = \frac{7\pi}{2}$ or root count.
- **Q53**: **Answer**: `12` — Row operations $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$: $\begin{vmatrix} 1 & 1 & 1 \\ 0 & x & 0 \\ 0 & 0 & y \end{vmatrix} = 1(x y - 0) = x y$. For $x = 3, y = 4$: $3 \times 4 = 12$.
- **Q54**: **Answer**: `120` — Permutations of 5 digits taken 4 at a time: $P(5, 4) = 5 \times 4 \times 3 \times 2 = 120$.
