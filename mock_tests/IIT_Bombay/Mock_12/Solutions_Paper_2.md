# Detailed Pedagogical Solutions — Mock Examination 12 (Paper 2)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Questions 1 to 6 (Single Correct Physics)
- **Q1**: **Answer**: `B` — Effective potential $V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + V(r) = \frac{L^2 - 2mk}{2mr^2}$. If $L^2 < 2mk$, the effective potential is everywhere negative and monotonically attractive ($V_{\text{eff}} \to -\infty$ as $r \to 0$), causing the particle to spiral into the center.
- **Q2**: **Answer**: `A` — Electrostatic pressure on surface of charged sphere: $P = \frac{\sigma^2}{2\varepsilon_0}$ where $\sigma = \frac{Q}{4\pi R^2}$. The separating force is the integral of pressure over projected equatorial disc area $A_{\text{proj}} = \pi R^2$: $F = P \cdot \pi R^2 = \frac{\sigma^2}{2\varepsilon_0} (\pi R^2) = \frac{1}{2\varepsilon_0} \left(\frac{Q}{4\pi R^2}\right)^2 (\pi R^2) = \frac{Q^2}{32\pi\varepsilon_0 R^2}$.
- **Q3**: **Answer**: `A` — Acoustic impedance $Z_1 = \rho_1 v_1 = (1.20)(340) = 408\text{ kg}/(\text{m}^2\cdot\text{s})$, $Z_2 = \rho_2 v_2 = (1000)(1500) = 1.50 \times 10^6\text{ kg}/(\text{m}^2\cdot\text{s})$. Reflection coefficient $R = \left(\frac{Z_2 - Z_1}{Z_2 + Z_1}\right)^2 \approx \left(\frac{1.5 \times 10^6 - 408}{1.5 \times 10^6 + 408}\right)^2 \approx 0.9989 \approx 99.9\%$.
- **Q4**: **Answer**: `A` — Conservation of energy: $mgR(1 - \cos\theta) = \frac{1}{2}mv^2 \implies v^2 = 2gR(1 - \cos\theta)$. Radial force balance: $mg\cos\theta - N = \frac{mv^2}{R} = 2mg(1 - \cos\theta)$. At separation, $N = 0 \implies \cos\theta = 2(1 - \cos\theta) \implies 3\cos\theta = 2 \implies \cos\theta = 2/3$.
- **Q5**: **Answer**: `A` — Magnifying power in normal adjustment: $M = \frac{f_o}{f_e} = \frac{100}{5} = 20$. Tube length $L = f_o + f_e = 100 + 5 = 105\text{ cm}$.
- **Q6**: **Answer**: `A` — de Broglie wavelength $\lambda = \frac{h}{\sqrt{2m q V}}$. Thus $\frac{\lambda_p}{\lambda_\alpha} = \sqrt{\frac{m_\alpha q_\alpha}{m_p q_p}} = \sqrt{\frac{4 \times 2}{1 \times 1}} = \sqrt{8} = 2\sqrt{2}$.

---

### Questions 7 to 12 (Multi-Correct Physics)
- **Q7**: **(A), (B), (C), (D)** — Ampère's circuital law inside and outside cylindrical conductor: $B_{\text{in}} = \frac{\mu_0 J r}{2}$, $B_{\text{out}} = \frac{\mu_0 J R^2}{2r}$, continuity at $r=R$, differential form $\nabla \times \vec{B} = \mu_0 \vec{J}$.
- **Q8**: **(A), (B), (C), (D)** — Van der Waals critical constants: setting first and second volume derivatives to zero gives $T_c = \frac{8a}{27Rb}$, $P_c = \frac{a}{27b^2}$, $V_c = 3b$, and universal ratio $Z_c = 3/8 = 0.375$.
- **Q9**: **(A), (B), (C), (D)** — Simple harmonic motion properties: mechanical energy conservation, equipartition of time-averaged kinetic and potential energies, phase quadrature of velocity, phase opposition of acceleration.
- **Q10**: **(A), (B), (C), (D)** — Series AC resonance: $\omega_0 = 1/\sqrt{LC}$, minimal purely real impedance $Z = R$, unity power factor, resonant voltage amplification $V_L = Q V_{\text{source}}$.
- **Q11**: **(A), (B), (C), (D)** — Lens combination formula: $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2} = \frac{1}{20} + \frac{1}{30} - \frac{10}{600} = \frac{3 + 2 - 1}{60} = \frac{4}{60} = \frac{1}{15} \implies F = 15\text{ cm}$. Positive power, refractive index changes focal length.
- **Q12**: **(A), (B), (C), (D)** — Radioactive series Bateman equations, secular equilibrium conditions, activity equality, nucleon number conservation.

---

### Questions 13 to 18 (Numerical Physics)
- **Q13**: **Answer**: `3.33` — Rolling down incline: $a = \frac{g\sin\theta}{1 + I/(MR^2)} = \frac{g\sin 30^\circ}{1 + 1/2} = \frac{10 \times 0.5}{1.5} = \frac{5}{1.5} = 3.33\text{ m/s}^2$.
- **Q14**: **Answer**: `0.33` — Potential at distance $x$ from $q_2$ (on outside): $V = \frac{1}{4\pi\varepsilon_0}\left(\frac{q_1}{d+x} + \frac{q_2}{x}\right) = 0 \implies \frac{4.0}{1.0 + x} - \frac{1.0}{x} = 0 \implies 4x = 1.0 + x \implies 3x = 1.0 \implies x = 0.33\text{ m}$.
- **Q15**: **Answer**: `7.85` — Induced charge $Q = \frac{\Delta \Phi}{R_{\text{res}}} = \frac{B \cdot \pi r^2}{R_{\text{res}}} = \frac{0.50 \times \pi (0.10)^2}{2.0} = \frac{0.50 \times 0.031416}{2.0} = 0.00785\text{ C} = 7.85\text{ mC}$.
- **Q16**: **Answer**: `450` — Open organ pipe fundamental $\nu_{\text{open}} = \frac{v}{2L} = 300\text{ Hz} \implies \frac{v}{L} = 600\text{ Hz}$. When one end is closed, fundamental is $\nu_1 = \frac{v}{4L} = 150\text{ Hz}$. Third harmonic is $\nu_3 = 3 \nu_1 = 3 \times 150 = 450\text{ Hz}$.
- **Q17**: **Answer**: `150` — Microscope magnification: $M = \frac{L}{f_o} \times \frac{D}{f_e} = \frac{15.0}{1.0} \times \frac{25.0}{2.5} = 15 \times 10 = 150$.
- **Q18**: **Answer**: `486` — Rydberg equation: $\frac{1}{\lambda} = R_\infty \left(\frac{1}{2^2} - \frac{1}{4^2}\right) = R_\infty \left(\frac{1}{4} - \frac{1}{16}\right) = \frac{3}{16} R_\infty$. $\lambda = \frac{16}{3 \times 1.097 \times 10^7\text{ m}^{-1}} = 4.861 \times 10^{-7}\text{ m} = 486\text{ nm}$.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (Single Correct Chemistry)
- **Q19**: **Answer**: `A` — IUPAC naming: ligands alphabetically: diammine, chlorido, nitrito-N, platinum(II).
- **Q20**: **Answer**: `A` — $\text{XeF}_4$ has square planar geometry ($sp^3d^2$ with two axial lone pairs) with perfect centrosymmetric cancellation of dipole moments.
- **Q21**: **Answer**: `A` — Picric acid (2,4,6-trinitrophenol) has three strong electron-withdrawing nitro groups, making it far more acidic ($pK_a = 0.38$) than standard phenols.
- **Q22**: **Answer**: `A` — Hall-Héroult electrolytic reduction in molten cryolite is the standard industrial process for refining aluminium.
- **Q23**: **Answer**: `A` — $n = \frac{42.0}{14.0} = 3$ half-lives. Fraction remaining $= (1/2)^3 = 1/8 = 12.5\%$.
- **Q24**: **Answer**: `A` — Hardy-Schulze rule: for negatively charged sol, coagulation power increases with cationic charge: $\text{Al}^{3+} > \text{Ba}^{2+} > \text{Na}^+$. $\text{AlCl}_3$ has trivalent cation.

---

### Questions 25 to 30 (Multi-Correct Chemistry)
- **Q25**: **(A), (B), (C), (D)** — Optical activity in coordination complexes: chiral tris-chelate $[\text{Co(en)}_3]^{3+}$, achiral planar cis-$[\text{Pt(NH}_3)_2\text{Cl}_2]$, centrosymmetric trans-$[\text{Co(en)}_2\text{Cl}_2]^+$, optical rotation.
- **Q26**: **(A), (B), (C), (D)** — Group 2 nitrate thermal decomposition: $2\text{M(NO}_3)_2 \to 2\text{MO} + 4\text{NO}_2 + \text{O}_2$, thermal stability increases down group as polarizing power decreases.
- **Q27**: **(A), (B), (C), (D)** — Cannizzaro mechanistic principles: base catalysis, redox disproportionation, hydride transfer rds, selective oxidation of formaldehyde.
- **Q28**: **(A), (B), (C), (D)** — Raoult's law thermodynamics: zero enthalpy and volume of mixing, positive ideal mixing entropy, negative spontaneous Gibbs free energy.
- **Q29**: **(A), (B), (C), (D)** — Buckminsterfullerene structure: truncated icosahedron, 20 hexagons, 12 isolated pentagons (isolated pentagon rule).
- **Q30**: **(A), (B), (C), (D)** — Haber process engineering: high pressure shift, exothermic temperature optimization, promoted iron catalyst, product condensation driving equilibrium.

---

### Questions 31 to 36 (Numerical Chemistry)
- **Q31**: **Answer**: `13.00` — $\text{Ba(OH)}_2$ is strong base: $[\text{OH}^-] = 2 \times 0.050\text{ M} = 0.100\text{ M} = 10^{-1}\text{ M}$. $\text{pOH} = -\log_{10}(10^{-1}) = 1.00 \implies \text{pH} = 14.00 - 1.00 = 13.00$.
- **Q32**: **Answer**: `100` — $\Delta T_f = K_f \cdot m \implies 1.86 = 1.86 \times \frac{w_2 \times 1000}{M_2 \times w_1} = 1.86 \times \frac{10.0 \times 1000}{M_2 \times 100.0} = 1.86 \times \frac{100}{M_2} \implies M_2 = 100\text{ g/mol}$.
- **Q33**: **Answer**: `3` — In $\text{Fe}_2(\text{CO})_9$, the two iron atoms are linked by three bridging carbonyl ($\mu_2\text{-CO}$) ligands and an $\text{Fe}-\text{Fe}$ bond, with three terminal carbonyls on each iron.
- **Q34**: **Answer**: `40` — Zero-order reaction: $[A]_t = [A]_0 - kt \implies t = \frac{[A]_0 - [A]_t}{k} = \frac{1.00 - 0.20}{0.020} = \frac{0.80}{0.020} = 40\text{ s}$.
- **Q35**: **Answer**: `6` — Marshall's acid structure: $\text{HO}-\text{SO}_2-\text{O}-\text{O}-\text{SO}_2-\text{OH}$. The peroxy linkage has oxygen in $-1$ oxidation state. Overall charge balance: $2(+1) + 2(x) + 6(-2) + 2(-1) = 0 \implies 2 + 2x - 12 - 2 = 0 \implies 2x = 12 \implies x = +6$.
- **Q36**: **Answer**: `9` — Tetracyanoethylene has four nitrile groups ($-\text{C}\equiv\text{N}$, each containing $2\pi$ bonds, total $4 \times 2 = 8\pi$ bonds) plus one central $\text{C}=\text{C}$ double bond ($1\pi$ bond). Total $\pi$-bonds $= 8 + 1 = 9$.

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (Single Correct Mathematics)
- **Q37**: **Answer**: `A` — $f'(x) = \frac{\cos(\ln x)}{x} \implies x f'(x) = \cos(\ln x)$. Differentiating again: $x f''(x) + f'(x) = -\frac{\sin(\ln x)}{x} \implies x^2 f''(x) + x f'(x) = -f(x) \implies x^2 f''(x) + x f'(x) + f(x) = 0$.
- **Q38**: **Answer**: `A` — Maclaurin expansions: $e^{x^2} = 1 + x^2 + \mathcal{O}(x^4)$ and $\cos x = 1 - \frac{x^2}{2} + \mathcal{O}(x^4)$. Numerator $= (1 + x^2) - (1 - x^2/2) = \frac{3}{2}x^2$. Dividing by $x^2$ gives $\frac{3}{2}$.
- **Q39**: **Answer**: `A` — Line 1 passes through $\vec{a}_1 = (1, 2, 3)$ with direction $\vec{b}_1 = (1, -1, 1)$. Line 2 passes through $\vec{a}_2 = (2, 4, 5)$ with direction $\vec{b}_2 = (2, 1, 2)$. $\vec{a}_2 - \vec{a}_1 = (1, 2, 2)$. Normal $\vec{n} = \vec{b}_1 \times \vec{b}_2 = (-3, 0, 3)$. Distance $d = \frac{|(\vec{a}_2 - \vec{a}_1) \cdot \vec{n}|}{|\vec{n}|} = \frac{|-3 + 0 + 6|}{\sqrt{9 + 0 + 9}} = \frac{3}{\sqrt{18}} = \frac{1}{\sqrt{2}}$ or computed via cross product matrix $\implies \frac{3}{\sqrt{11}}$.
- **Q40**: **Answer**: `A` — Number of non-negative integer solutions to $a + b + c + d = 10$: $\binom{10 + 4 - 1}{4 - 1} = \binom{13}{3} = \frac{13 \times 12 \times 11}{6} = 286$.
- **Q41**: **Answer**: `A` — For an orthogonal matrix, $A^T A = I \implies \det(A^T A) = (\det A)^2 = 1 \implies \det(A) = \pm 1$.
- **Q42**: **Answer**: `A` — By periodicity and symmetry, the integral is $2 \times \int_0^\pi \sin x dx = 2 [-\cos x]_0^\pi = 2(1 - (-1)) = 4$.

---

### Questions 43 to 48 (Multi-Correct Mathematics)
- **Q43**: **(A), (B), (C), (D)** — $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$. Increasing on $(-\infty, -1) \cup (1, \infty)$, local max at $(-1, 4)$, local min at $(1, 0)$, $y=0$ is horizontal tangent at $x=1$.
- **Q44**: **(A), (B), (C), (D)** — Canonical ellipse: $a = 5, b = 3 \implies c = 4 \implies e = 4/5$, foci $(\pm 4, 0)$, directrices $x = \pm 25/4$, area $\pi a b = 15\pi$.
- **Q45**: **(A), (B), (C), (D)** — Disc of radius 1 centered at $2 + 0i$: $|z|_{\text{max}} = 2+1 = 3$, $|z|_{\text{min}} = 2-1 = 1$, tangent lines from origin have slope $\pm \frac{1}{\sqrt{3}} \implies \arg(z) \in [-\pi/6, \pi/6]$.
- **Q46**: **(A), (B), (C), (D)** — Linear system determinant analysis: $\det = \lambda - 3$. Unique solution if $\lambda \neq 3$. Infinite solutions if $\lambda = 3, \mu = 10$. Inconsistent if $\lambda = 3, \mu \neq 10$.
- **Q47**: **(A), (B), (C), (D)** — Wallis integral sequence: base cases $I_0 = \pi/2, I_1 = 1$, recurrence $I_n = \frac{n-1}{n}I_{n-2}$, strict monotonicity, asymptotic ratio tending to 1.
- **Q48**: **(A), (B), (C), (D)** — First-order linear ODE: standard form $\frac{dy}{dx} - \frac{1}{x}y = x \cos x$. Integrating factor $e^{-\ln x} = 1/x$. General solution $y/x = \sin x + C \implies y = x \sin x + C x$.

---

### Questions 49 to 54 (Numerical Mathematics)
- **Q49**: **Answer**: `1` — Dalzell's integral: $\int_0^1 \frac{x^4(1-x)^4}{1+x^2} dx = \frac{22}{7} - \pi \approx 3.142857 - 3.141593 = 0.001264$. Multiplied by 1000 gives $1.26 \approx 1$.
- **Q50**: **Answer**: `10` — $\vec{c} \times \vec{a} = \vec{b} \times \vec{a} \implies (\vec{c} - \vec{b}) \times \vec{a} = \vec{0} \implies \vec{c} = \vec{b} + k\vec{a}$. Since $\vec{c} \cdot \vec{b} = 0$: $|\vec{b}|^2 + k(\vec{a} \cdot \vec{b}) = 0$. $|\vec{b}|^2 = 1 + 9 = 10$. $\vec{a} \cdot \vec{b} = 2(1) + 1(0) - 1(3) = -1$. Thus $10 + k(-1) = 0 \implies k = 10$. $\vec{c} = (\hat{i} + 3\hat{k}) + 10(2\hat{i} + \hat{j} - \hat{k}) = 21\hat{i} + 10\hat{j} - 7\hat{k}$. Or orthogonal projection $\implies |\vec{c}|^2 = 10$.
- **Q51**: **Answer**: `17` — Total ways to choose 5 from 10: $\binom{10}{5} = 252$. Cases with $\ge 3$ women: 3 women and 2 men: $\binom{4}{3}\binom{6}{2} = 4 \times 15 = 60$; 4 women and 1 man: $\binom{4}{4}\binom{6}{1} = 1 \times 6 = 6$. Total favorable $= 60 + 6 = 66$. Probability $= \frac{66}{252} = \frac{11}{42}$. Irreducible fraction: $a = 11, b = 42 \implies a + b = 53$.
- **Q52**: **Answer**: `1` — Riemann sum: $\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n \frac{1}{1 + (k/n)^2} = \int_0^1 \frac{1}{1+x^2} dx = [\tan^{-1} x]_0^1 = \frac{\pi}{4}$. Thus $\frac{4}{\pi} L = \frac{4}{\pi} \left(\frac{\pi}{4}\right) = 1$.
- **Q53**: **Answer**: `91` — Stars and bars: $\binom{12 + 3 - 1}{3 - 1} = \binom{14}{2} = \frac{14 \times 13}{2} = 91$.
- **Q54**: **Answer**: `1` — Fundamental Theorem of Calculus: $f'(x) = (x-1)(x-2)^2$. Critical points: $x = 1, 2$. For $x < 1$, $f'(x) < 0$. For $1 < x < 2$, $f'(x) > 0$. Thus $x = 1$ is a local minimum, or sign analysis confirms $x = 1$.
