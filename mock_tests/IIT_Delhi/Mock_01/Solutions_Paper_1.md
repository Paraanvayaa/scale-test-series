# Detailed Pedagogical Solutions — Mock Examination 01 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rigid Body Dynamics, Friction on Accelerated Plank, Newton's Second Law for Translation and Rotation ($\tau = I\alpha$), Condition for Pure Rolling without Slipping ($a_c - \alpha R = a_p$).
- **2. IIT Historical Signature**: Classic IIT Delhi multi-body friction challenge where friction between a rolling body and an accelerated base acts to enforce kinematics.
- **3. Given Parameters & Boundary Conditions**:
  - Cylinder: mass $M$, radius $R$, moment of inertia $I = \frac{1}{2}MR^2$.
  - Plank: mass $m = 2M$, smooth floor underneath.
  - Horizontal force $F$ applied at the center of the cylinder.
- **4. Schematic / Equations of Motion**:
  - Let friction on cylinder from plank be $f$ directed backward.
  - For cylinder translation: $F - f = M a_c$.
  - For cylinder rotation about CM: $f R = I \alpha = \left(\frac{1}{2}MR^2\right)\alpha \implies \alpha R = \frac{2f}{M}$.
  - By Newton's third law, friction on plank from cylinder is $f$ directed forward.
  - For plank translation: $f = m a_p = 2M a_p \implies a_p = \frac{f}{2M}$.
  - No slipping condition at contact point: $a_{\text{contact, cylinder}} = a_c - \alpha R = a_p$.
- **5. Step-by-Step Mathematical Derivation**:
  - Substitute expressions into rolling condition:
    $$a_c - \frac{2f}{M} = \frac{f}{2M} \implies a_c = \frac{5f}{2M}$$
  - From cylinder translation:
    $$F - f = M\left(\frac{5f}{2M}\right) = \frac{5}{2}f \implies F = \frac{7}{2}f \implies f = \frac{2F}{7}$$
  - Now calculate accelerations:
    $$a_p = \frac{f}{2M} = \frac{2F/7}{2M} = \frac{F}{7M}$$
    $$a_c = \frac{5f}{2M} = \frac{5(2F/7)}{2M} = \frac{5F}{7M}$$
  - Minimum friction coefficient $\mu_s$:
    $$f \le \mu_s N = \mu_s M g \implies \frac{2F}{7} \le \mu_s M g \implies \mu_s \ge \frac{2F}{7Mg}$$
  - All statements (A), (B), (C), (D) are correct.
- **6. Alternative Solving Method / Shortcut**: System Center of Mass: total external force is $F$, so $M a_c + 2M a_p = F$. Check: $M(5F/7M) + 2M(F/7M) = 5F/7 + 2F/7 = F$. Verified!
- **7. Conceptual Pitfalls & Distractor Breakdown**: Many candidates guess that friction on the plank opposes motion. On the plank, friction is the sole driving force, so it must point forward.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**
- **9. Cross-Concept Extension**: If force $F$ were applied to the plank instead of the cylinder, the partition of acceleration would change to $a_c = \frac{2F}{7M}$ and $a_p = \frac{3F}{7M}$.

---

### Question 2
- **1. Target Concept & Governing Laws**: AC Circuits, Parallel LC Resonance, Impedance, Phase Angle.
- **2. IIT Historical Signature**: IIT Delhi's high affinity for AC circuit theory and LC parallel resonance behavior.
- **3. Derivation**:
  - Admittance of parallel LC: $Y = j\omega C + \frac{1}{j\omega L} = j\left(\omega C - \frac{1}{\omega L}\right)$.
  - Impedance: $Z_{LC} = \frac{1}{Y} = \frac{-j}{\omega C - 1/(\omega L)}$.
  - At resonance $\omega_0 = 1/\sqrt{LC}$, $\omega C = 1/(\omega L)$, so $Y = 0 \implies Z_{LC} \to \infty$. Thus (A) is correct.
  - Since $Z_{LC} = \infty$, the total circuit impedance is infinite, so the source current is zero. (B) is correct.
  - For $\omega < \omega_0$: $\frac{1}{\omega L} > \omega C$, so inductive susceptance dominates $\implies$ inductive behavior. (C) is correct.
  - For $\omega > \omega_0$: $\omega C > \frac{1}{\omega L}$, so capacitive susceptance dominates $\implies$ capacitive behavior. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: First Law of Thermodynamics, Polytropic Process $P = \alpha V^2$, Work Done $W = \int P dV$, Molar Heat Capacity $C = C_V + \frac{R}{1-n}$.
- **2. Derivation**:
  - $P = \alpha V^2$ corresponds to $P V^{-2} = \alpha$, so polytropic index $n = -2$.
  - Work done: $W = \int_{V_0}^{2V_0} \alpha V^2 dV = \frac{\alpha}{3}[(2V_0)^3 - V_0^3] = \frac{7}{3}\alpha V_0^3$. (A) is correct.
  - Ideal gas law: $T = \frac{PV}{nR} = \frac{\alpha V^3}{nR}$. At $2V_0$, $T_2 = \frac{\alpha (8V_0^3)}{nR} = 8 T_1$. (D) is correct.
  - Internal energy change: $\Delta U = n C_V \Delta T = n\left(\frac{5}{2}R\right)(7 T_1) = \frac{35}{2} n R T_1 = \frac{35}{2}\alpha V_0^3 \ne \frac{35}{4}\alpha V_0^3$. Thus (B) is incorrect.
  - Molar heat capacity: $C = C_V + \frac{R}{1 - (-2)} = \frac{5}{2}R + \frac{R}{3} = \frac{17}{6}R$. (C) is correct.
- **8. Final Answer & Correct Options**: **(A), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Electrostatics of Concentric Spherical Shells, Grounding, Charge Distribution.
- **2. Derivation**:
  - Let $q'$ be the charge remaining on the inner shell after grounding.
  - Potential of inner shell must equal zero (grounded):
    $$V_{\text{inner}} = \frac{1}{4\pi\varepsilon_0}\left[\frac{q'}{R} + \frac{2Q}{2R}\right] = 0 \implies \frac{q'}{R} + \frac{Q}{R} = 0 \implies q' = -Q$$
    Statement (A) is correct.
  - Potential of outer shell:
    $$V_{\text{outer}} = \frac{1}{4\pi\varepsilon_0}\left[\frac{q'}{2R} + \frac{2Q}{2R}\right] = \frac{1}{4\pi\varepsilon_0}\frac{-Q + 2Q}{2R} = \frac{Q}{8\pi\varepsilon_0 R} \ne \frac{Q}{4\pi\varepsilon_0 R}$$
    Thus (B) is incorrect.
  - Initial charge on inner shell was $+Q$. Final is $-Q$. Thus charge flown to ground is $Q - (-Q) = 2Q$. (C) is correct.
  - Electric field between shells: $E(r) = \frac{q'}{4\pi\varepsilon_0 r^2} = -\frac{Q}{4\pi\varepsilon_0 r^2}$.
  - Stored energy:
    $$U = \int_R^{2R} \frac{1}{2}\varepsilon_0 E^2 (4\pi r^2 dr) = \frac{Q^2}{8\pi\varepsilon_0}\left(\frac{1}{R} - \frac{1}{2R}\right) = \frac{Q^2}{16\pi\varepsilon_0 R}$$
    Statement (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Potential Energy Wells, Small Oscillations, Simple Harmonic Motion.
- **2. Derivation**:
  - $U'(x) = U_0 \left[\frac{4x^3}{a^4} - \frac{4x}{a^2}\right] = \frac{4U_0 x}{a^2}\left(\frac{x^2}{a^2} - 1\right) = 0 \implies x = 0, \pm a$.
  - $U''(x) = U_0 \left[\frac{12x^2}{a^4} - \frac{4}{a^2}\right]$.
  - At $x = 0$: $U''(0) = -\frac{4U_0}{a^2} < 0 \implies$ unstable equilibrium. (B) is correct.
  - At $x = \pm a$: $U''(\pm a) = \frac{8U_0}{a^2} > 0 \implies$ stable equilibrium. (A) is correct.
  - Angular frequency: $\omega = \sqrt{\frac{U''(\pm a)}{m}} = \sqrt{\frac{8U_0}{m a^2}} = \frac{2}{a}\sqrt{\frac{2U_0}{m}}$. (C) is correct.
  - Potential at well bottom: $U(\pm a) = U_0(1 - 2) = -U_0$. Potential as $x \to \infty$ is $+\infty$. Thus escape energy to infinity is infinite, not $U_0$ (it is $U_0$ to escape to the central hill at $x=0$). Thus (D) is incorrect.
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Electromagnetic Waves, Poynting Vector, Radiation Pressure.
- **2. Derivation**:
  - $\vec{B} = \frac{1}{c}(\hat{k} \times \vec{E}) = \frac{E_0}{c}\cos(kz - \omega t)\hat{j}$. (A) is correct.
  - $\langle \vec{S} \rangle = \frac{E_0^2}{2\mu_0 c}\hat{k} = \frac{300^2}{2(4\pi \times 10^{-7})(3 \times 10^8)}\hat{k} = \frac{90000}{753.98}\hat{k} \approx 119.37\hat{k}\text{ W/m}^2$. (B) is correct.
  - Radiation pressure on absorbing surface: $P = \frac{\langle S \rangle}{c} = \frac{119.37}{3 \times 10^8} \approx 3.98 \times 10^{-7}\text{ N/m}^2$. (C) is correct.
  - On reflection, momentum change doubles $\Delta p = 2p$, so pressure doubles $P_{\text{ref}} = 2P_{\text{abs}}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Torricelli's law with continuity: $t = \frac{A}{a}\sqrt{\frac{2H}{g}} = \frac{1.0}{2.0 \times 10^{-4}}\sqrt{\frac{2(4.90)}{9.80}} = 5000 \times 1.0 = 5000\text{ s}$. Exact: `5000.00`.
- **Question 8**: Resonance tube: $\frac{\lambda}{2} = L_2 - L_1 = 50.0 - 16.0 = 34.0\text{ cm} = 0.34\text{ m} \implies \lambda = 0.68\text{ m}$. Speed: $v = \nu \lambda = 500 \times 0.68 = 340\text{ m/s}$. Exact: `340.00`.
- **Question 9**: Conservation of energy for rotating rod: $M g \frac{L}{2} = \frac{1}{2} I \omega^2 = \frac{1}{2}\left(\frac{1}{3}ML^2\right)\omega^2 \implies \omega = \sqrt{\frac{3g}{L}} = \sqrt{\frac{3(9.80)}{1.20}} = \sqrt{24.5} \approx 4.95\text{ rad/s}$. Exact: `4.95`.
- **Question 10**: $E_{\text{photon}} = \frac{hc}{\lambda} = \frac{1240}{400} = 3.10\text{ eV}$. Stopping potential: $e V_0 = E - \Phi = 3.10 - 2.14 = 0.96\text{ eV} \implies V_0 = 0.96\text{ V}$. Exact: `0.96`.
- **Question 11**: At midpoint, fields due to opposite currents add: $B = \frac{\mu_0 I_1}{2\pi (d/2)} + \frac{\mu_0 I_2}{2\pi (d/2)} = \frac{\mu_0}{\pi d}(I_1 + I_2) = \frac{4\pi \times 10^{-7}}{\pi (0.20)}(30.0) = 20 \times 10^{-7} \times 30 = 60 \times 10^{-6}\text{ T} = 60\ \mu\text{T}$. Exact: `60.00`.
- **Question 12**: For lens 1: parallel beam converges at $f_1 = +20\text{ cm}$. Distance from lens 2: $u_2 = 20 - 10 = +10\text{ cm}$ (virtual object). Using lens formula for lens 2 ($f_2 = -10\text{ cm}$): $\frac{1}{v_2} - \frac{1}{+10} = \frac{1}{-10} \implies \frac{1}{v_2} = 0 \implies v_2 \to \infty$. But wait, parallel emergent beam! Distance is infinite, or let's specify parallel beam emergent at $\infty$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: Rolling acceleration $a = \frac{g\sin\theta}{1 + I/(mr^2)} = \frac{g\sin 30^\circ}{1 + 2/5} = \frac{g/2}{7/5} = \frac{5}{14}g$. Option (A).
- **Question 14**: $v_{\text{max}} = \omega A = \sqrt{k/m} A \implies 2.0 = \sqrt{100/1} A = 10 A \implies A = 0.20\text{ m}$. Option (B).
- **Question 15**: $\nu = c R_\infty \left(\frac{1}{1^2} - \frac{1}{3^2}\right) = (3 \times 10^8)(1.097 \times 10^7)\left(\frac{8}{9}\right) \approx 2.925 \times 10^{15}\text{ Hz}$. Option (B).
- **Question 16**: $M = N I A = 100 \times 2.0 \times \pi (0.05)^2 = 200 \times 3.1416 \times 0.0025 \approx 1.57\text{ A}\cdot\text{m}^2$. Option (A).
- **Question 17**: $\eta = 1 - \frac{300}{500} = 0.40$. Work $W = \eta Q_H = 0.40 \times 1000 = 400\text{ J}$. Option (A).
- **Question 18**: $\lambda = \frac{h}{\sqrt{3 m k_B T}} = \frac{6.63 \times 10^{-34}}{\sqrt{3(1.67 \times 10^{-27})(1.38 \times 10^{-23})(300)}} \approx 0.145\text{ nm} \approx 0.14\text{ nm}$. Option (B).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: $[Co(en)_2Cl_2]^+$ has $cis$ (optically active, chiral pair) and $trans$ (inversion center, achiral) isomers. Co is +3, coordination number 6. Options: (A), (B), (C), (D).
- **Question 20**: Inert gas at constant P increases volume, shifting toward more moles ($\text{PCl}_3 + \text{Cl}_2$). Constant V has no effect. Endothermic reaction shifts forward with temperature. $K_p$ depends only on temperature. Options: (A), (B), (C).
- **Question 21**: $E2$ on $(2R, 3R)$-2-bromo-3-methylpentane with ethoxide requires anti-coplanar transition state yielding $(E)$-3-methylpent-2-ene. It is second order. Options: (A), (B), (C).
- **Question 22**: $\text{XeF}_4$ (square planar, $\mu=0$), $\text{BF}_3$ (trigonal planar, $\mu=0$), $\text{I}_3^-$ (linear, symmetric, $\mu=0$). $\text{SF}_4$ is see-saw ($\mu \ne 0$). Options: (A), (B), (D).
- **Question 23**: For ideal binary solution: $\Delta H_{\text{mix}} = 0, \Delta V_{\text{mix}} = 0, \Delta S_{\text{mix}} > 0, \Delta G_{\text{mix}} < 0$. Options: (A), (B), (C), (D).
- **Question 24**: Group II metal cations giving black sulfides: $\text{CuS}, \text{PbS}, \text{Bi}_2\text{S}_3$ are black. $\text{CdS}$ is yellow! Options: (A), (B), (D).
- **Question 25**: $\text{pH} = pK_a + \log\frac{[\text{CH}_3\text{COO}^-]}{[\text{CH}_3\text{COOH}]} = 4.74 + \log\left(\frac{0.10}{0.20}\right) = 4.74 - 0.30 = 4.44$. Exact: `4.44`.
- **Question 26**: For first-order reaction, $t_{75\%} = 2 t_{1/2} = 2 \times \frac{0.693}{6.93 \times 10^{-3}} = 2 \times 100 = 200\text{ s}$. Exact: `200.00`.
- **Question 27**: For FCC: $4r = \sqrt{2}a \implies r = \frac{\sqrt{2}a}{4} = \frac{1.414 \times 400}{4} = 141.4\text{ pm}$. Exact: `141.42`.
- **Question 28**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = 0.34 - (-0.76) = 1.10\text{ V}$. Exact: `1.10`.
- **Question 29**: $\Delta T_f = i K_f m \implies 0.205 = i (1.86)(0.10) \implies i = \frac{0.205}{0.186} \approx 1.102$. Since $i = 1 + \alpha$, $\alpha = 0.102 = 10.2\%$. Exact: `10.22`.
- **Question 30**: $\text{Fe}^{2+}$ is $3d^6$. High spin in weak field $\text{H}_2\text{O}$ has 4 unpaired electrons. $\mu = \sqrt{4(6)} = \sqrt{24} \approx 4.90\text{ BM}$. Exact: `4.90`.
- **Question 31**: Nitrobenzene has a strongly deactivating $-\text{NO}_2$ group which complexes with $\text{AlCl}_3$, preventing Friedel-Crafts reaction. Option (A).
- **Question 32**: Acid strength increases with oxidation state of central atom: $\text{HClO} < \text{HClO}_2 < \text{HClO}_3 < \text{HClO}_4$. Option (A).
- **Question 33**: Slag formed in copper smelting is iron silicate $\text{FeSiO}_3$. Option (A).
- **Question 34**: Cannizzaro reaction. Option (A).
- **Question 35**: $\text{XeOF}_4$: Xe has 1 lone pair. Each F has 3 lone pairs ($4 \times 3 = 12$). Oxygen has 2 lone pairs. Total lone pairs = $1 + 12 + 2 = 15$. Option (C).
- **Question 36**: Vitamin C (ascorbic acid) is water-soluble. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(-x) = \frac{(-x)^2 - 1}{(-x)^2 + 1} = f(x)$ (even). Range is $[-1, 1)$. $f'(x) = \frac{4x}{(x^2+1)^2} > 0$ for $x > 0$. Horizontal asymptote $y = 1$. Options: (A), (B), (C), (D).
- **Question 38**: Orthogonal matrix with $\det M = 1$ is an element of $SO(3)$, representing 3D spatial rotation. It always has eigenvalue $\lambda = 1$, row norm 1, and $\det(M - I) = 0$. Options: (A), (B), (C), (D).
- **Question 39**: For $\frac{x^2}{16} + \frac{y^2}{9} = 1$: $a=4, b=3$. $e = \sqrt{1 - 9/16} = \frac{\sqrt{7}}{4}$. Latus rectum $= \frac{2b^2}{a} = \frac{18}{4} = \frac{9}{2}$. Product of perpendiculars from foci to any tangent is $b^2 = 9$. Director circle is $x^2 + y^2 = a^2 + b^2 = 25$. Options: (A), (B), (C), (D).
- **Question 40**: Wallis formula recurrence: $I_n = \frac{n-1}{n}I_{n-2}$. $I_4 = \frac{3}{4}\frac{1}{2}\frac{\pi}{2} = \frac{3\pi}{16}$. $I_5 = \frac{4}{5}\frac{2}{3}(1) = \frac{8}{15}$. $\lim_{n \to \infty} I_n = 0$. Options: (A), (B), (C), (D).
- **Question 41**: Circle with center $c = 3+4i$, radius $r = 2$. $|c| = 5$. Max distance $= 5+2 = 7$, min distance $= 5-2 = 3$. Point $3+2i$: $|3+2i - (3+4i)| = |-2i| = 2$. Options: (A), (B), (C), (D).
- **Question 42**: $IF = e^{\int \cot x dx} = \sin x$. Equation: $y \sin x = \int 2\cos x \sin x dx = \sin^2 x + C$. $y(\pi/2) = 1 \implies 1 = 1 + C \implies C = 0 \implies y = \sin x$. $y(\pi/6) = 1/2$. Max is 1 at $\pi/2$. Options: (A), (B), (C), (D).
- **Question 43**: Substitute $x = \tan\theta$: $I = \int_0^{\pi/4} \ln(1+\tan\theta) d\theta = \frac{\pi}{8}\ln 2$. So $k = 8$. Exact: `8.00`.
- **Question 44**: $y^2 = 4x$ and $y = 2x - 4 \implies x = \frac{y+4}{2}$. Points of intersection: $y^2 = 4\left(\frac{y+4}{2}\right) = 2y + 8 \implies y^2 - 2y - 8 = 0 \implies y = 4, -2$.
  $$\text{Area} = \int_{-2}^4 \left(\frac{y+4}{2} - \frac{y^2}{4}\right)dy = \left[\frac{y^2}{4} + 2y - \frac{y^3}{12}\right]_{-2}^4 = (4 + 8 - 16/3) - (1 - 4 + 8/12) = \frac{20}{3} - \left(-\frac{7}{3}\right) = 9.00$$
  Exact: `9.00`.
- **Question 45**: Scalar triple product:
  $$[\vec{a} \ \vec{b} \ \vec{c}] = \begin{vmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \\ 3 & 1 & 2 \end{vmatrix} = 1(6-1) - 2(4-3) + 3(2-9) = 5 - 2 - 21 = -18$$
  Volume $V = |-18| = 18.00$. Exact: `18.00`.
- **Question 46**: $P = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14} \approx 0.357 \approx 0.36$. Exact: `0.36`.
- **Question 47**: $2^x + 3^x = 5^x \implies (2/5)^x + (3/5)^x = 1$. The left-hand side is strictly decreasing with $x$, while the RHS is constant. Hence there is exactly 1 real solution ($x = 1$). Exact: `1.00`.
- **Question 48**: Taylor expansion: $\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \dots$, so $\sin x - x + \frac{x^3}{6} = \frac{x^5}{120}$. Limit is $\frac{1}{120}$. Thus $m = 120$. Exact: `120.00`.
- **Question 49**: Distance formula between skew lines: vector $\vec{d}_1 = (2, 3, 4)$, $\vec{d}_2 = (3, 4, 5)$. Cross product $\vec{d}_1 \times \vec{d}_2 = (-1, 2, -1)$. $\vec{r}_2 - \vec{r}_1 = (1, 2, 2)$. Dot product $= -1(1) + 2(2) - 1(2) = 1$. Magnitude of cross product $= \sqrt{1 + 4 + 1} = \sqrt{6}$. Distance $= \frac{1}{\sqrt{6}}$. Option (A).
- **Question 50**: $\alpha + \beta = 6, \alpha\beta = 2$. $\alpha^3 + \beta^3 = (\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta) = 216 - 3(2)(6) = 216 - 36 = 180$. Option (A).
- **Question 51**: $r \cdot r! = (r+1 - 1)r! = (r+1)! - r!$. Telescoping sum gives $(11!) - 1! = 11! - 1$. Option (A).
- **Question 52**: $A^2 - 3A + 2I = 0 \implies 2I = 3A - A^2 \implies 2A^{-1} = 3I - A \implies A^{-1} = \frac{1}{2}(3I - A)$. Option (A).
- **Question 53**: Place 5 boys in $5!$ ways. This creates 6 available spots. Choose 5 spots for girls: $\binom{6}{5} \times 5! = 6 \times 5! = 6!$. Total ways $= 5! \times 6!$. Option (A).
- **Question 54**: Triangle with vertices $(0,0), (4,0), (0,6)$ is a right-angled triangle. Its hypotenuse joins $(4,0)$ and $(0,6)$. Length of hypotenuse $= \sqrt{4^2 + 6^2} = \sqrt{52} = 2\sqrt{13}$. Circumradius is half of hypotenuse $= \sqrt{13}$. Option (A).
