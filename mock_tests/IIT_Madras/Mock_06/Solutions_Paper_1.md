# Detailed Pedagogical Solutions – JEE Advanced Mock Examination 06 (Paper 1)
## Organising Institute Style Inspiration: IIT Madras (`IIT_MADRAS_STYLE`)

---

# PART I: PHYSICS

### Question 1
- **Concept**: Maxwell's Equations and Displacement Current in a circular capacitor.
- **Step 1**: Charge $Q(t) = I_0 t$. The electric field is $E = \frac{Q}{\varepsilon_0 A} = \frac{I_0 t}{\varepsilon_0 \pi R^2}$. Thus (A) is correct.
- **Step 2**: Displacement current density $J_d = \varepsilon_0 \frac{\partial E}{\partial t} = \varepsilon_0 \frac{I_0}{\varepsilon_0 \pi R^2} = \frac{I_0}{\pi R^2}$. Thus (B) is correct.
- **Step 3**: Ampère-Maxwell law: $\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enclosed}} = \mu_0 J_d (\pi r^2) \implies B(2\pi r) = \mu_0 \frac{I_0}{\pi R^2} \pi r^2 \implies B = \frac{\mu_0 I_0 r}{2\pi R^2}$. (C) is correct.
- **Step 4**: Poynting vector $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$. $\vec{E}$ is along $+\hat{k}$ and $\vec{B}$ is along $+\hat{\phi}$, so $\vec{E} \times \vec{B}$ points in $-\hat{r}$ (inward). Thus (D) is correct.
- **Correct Options**: (A, B, C, D)

### Question 2
- **Concept**: Electrostatics of layered dielectrics.
- **Step 1**: Gauss's law for displacement $\oint \vec{D} \cdot d\vec{A} = Q \implies D(r) = \frac{Q}{4\pi r^2}$ everywhere, which is continuous across $r = c$. Thus (A) is correct.
- **Step 2**: $E(r) = D(r)/(\varepsilon_0 \kappa)$. Ratio $E(c^-)/E(c^+) = \kappa_2 / \kappa_1$. Thus (B) is correct.
- **Step 3**: Polarization $\vec{P} = \varepsilon_0 (\kappa - 1)\vec{E}$. Bound surface charge $\sigma_b = (\vec{P}_1 - \vec{P}_2)\cdot \hat{r} \implies q_b = Q\left(\frac{1}{\kappa_2} - \frac{1}{\kappa_1}\right)$. (C) is correct.
- **Step 4**: Capacitance formula represents two spherical capacitors in series: $1/C = 1/C_1 + 1/C_2$. Thus (D) is correct.
- **Correct Options**: (A, B, C, D)

### Question 3
- **Concept**: Faraday's Law in a cylindrical field region.
- **Step 1**: Flux $\Phi = B(t) \cdot (\pi R^2) = B_0 \pi R^2 \cos(\omega t)$. Thus (A) is correct.
- **Step 2**: Induced EMF $\mathcal{E} = -d\Phi/dt = B_0 \pi R^2 \omega \sin(\omega t)$. Thus (B) is correct.
- **Step 3**: Due to four-fold symmetry, the forces on opposite sides cancel identically: $F_{\text{net}} = 0$. Thus (C) is correct.
- **Step 4**: The frame has 4 straight sides, current flows uniformly along the perimeter, not around corners individually. Thus (D) is incorrect.
- **Correct Options**: (A, B, C)

### Question 4
- **Concept**: Induced electric field accelerating a charged ring.
- **Step 1**: Induced electric field along the circumference satisfies $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi}{dt} \implies E(2\pi a) = \pi a^2 \frac{dB}{dt} \implies E = \frac{a}{2}\frac{dB}{dt}$.
- **Step 2**: Torque $\tau = q E a = \frac{q a^2}{2}\frac{dB}{dt}$.
- **Step 3**: $\int \tau dt = I_{\text{ring}} \omega \implies \frac{q a^2 B_0}{2} = (m a^2) \omega \implies \omega = \frac{q B_0}{2m}$. Thus (A), (B), (C), (D) are all correct.
- **Correct Options**: (A, B, C, D)

### Question 5
- **Concept**: Lloyd's mirror interference.
- **Step 1**: The real source and virtual image form two coherent sources separated by $2d$.
- **Step 2**: Fringe width $\beta = \frac{\lambda D}{2d} = \frac{500 \times 10^{-9} \times 1.0}{2 \times 1.0 \times 10^{-3}} = 0.25\text{ mm}$. (A) is correct.
- **Step 3**: Reflection at the mirror introduces a $\pi$ phase change (path difference $\lambda/2$), so the central fringe is dark. (B) is correct.
- **Step 4**: Bright fringes occur at $y_n = (n - 1/2)\beta$. (C) is correct.
- **Correct Options**: (A, B, C)

### Question 6
- **Concept**: Radiation pressure.
- **Step 1**: Absorbing: $P = I/c$. Reflecting: $P = 2I/c$. Fraction $R$: $P = (1+R)I/c$.
- **Step 2**: Verified by Nichols and Hull (1901).
- **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $E(2\pi r) = \pi r^2 \mu_0 n \frac{dI}{dt} \implies E = \frac{1}{2} r \mu_0 n \frac{dI}{dt} = \frac{1}{2}(0.05)(4\pi \times 10^{-7})(1000)(4.0) = 1.26 \times 10^{-4}\text{ V/m} \implies \mathbf{1.26}$.
- **Q8**: Initial energy $U_i = \frac{1}{2} C_0 V_0^2 = \frac{1}{2}(10 \times 10^{-6})(100)^2 = 50\text{ mJ}$. Half slab inserted: $C_f = \frac{1}{2}C_0 + \frac{1}{2}\kappa C_0 = 2.5 C_0$. Disconnected $\implies Q = C_0 V_0$ constant. $U_f = Q^2/(2C_f) = U_i / 2.5 = 20\text{ mJ}$. $W = U_i - U_f = 30\text{ mJ} \implies \mathbf{30.00}$.
- **Q9**: At resonance, $I_0 = V_0 / R = 220 / 10 = 22\text{ A}$. $X_L = \omega_0 L = 1000 \times 0.10 = 100\text{ }\Omega$. $V_L = I_0 X_L = 22 \times 100 = 2200\text{ V} \implies \mathbf{2200.00}$.
- **Q10**: $\tau = q E r = q (\frac{r}{2}\frac{dB}{dt}) r = \frac{1}{2} q r^2 \frac{dB}{dt} = \frac{1}{2}(2.0)(0.20)^2(5.0) = 0.20\text{ N m}$. $I = m r^2 = 0.50 \times 0.04 = 0.02\text{ kg m}^2$. $\alpha = \tau / I = 0.20 / 0.02 = 10.00\text{ rad/s}^2 \implies \mathbf{10.00}$.
- **Q11**: $\tan\theta_p = \sqrt{3} \implies \theta_p = 60^\circ$. $\theta_r = 90^\circ - \theta_p = 30^\circ \implies \mathbf{30.00}$.
- **Q12**: $Q = \int C dT = \int_{300}^{400} (\frac{3}{2}R + 2RT) dT = \frac{3}{2}R(100) + R(400^2 - 300^2) = 150R + 70000R = 70150 R \implies \mathbf{70150.00}$.

### Questions 13 to 18
- **Q13**: By right-hand rule and Ampère's law, $\vec{B} = -\frac{\mu_0 K_0}{2}\hat{j}$. **Correct: (B)**.
- **Q14**: The outer charge redistributes uniformly to shield the interior: outer surface density is uniform. **Correct: (B)**.
- **Q15**: $M = \sqrt{L_1 L_2} = \sqrt{4 \times 9} = 6\text{ H}$. **Correct: (B)**.
- **Q16**: $q(\vec{E} + \vec{v} \times \vec{B}) = q(E_0 \hat{j} + v_0 \hat{i} \times B_0 \hat{k}) = q(E_0 \hat{j} - v_0 B_0 \hat{j}) = 0$. Particle moves undeflected in a straight line. **Correct: (A)**.
- **Q17**: $\beta = \frac{T_C}{T_H - T_C} = \frac{250}{300 - 250} = 5.0$. **Correct: (A)**.
- **Q18**: Unpolarized through first polarizer gives $I_0/2$. Through second gives $(I_0/2)\cos^2(60^\circ) = (I_0/2)(1/4) = I_0/8$. **Correct: (C)**.

---

# PART II: CHEMISTRY

### Question 19 to 24
- **Q19**: Standard hydrogen electrode combined with $\text{Fe}^{3+}/\text{Fe}^{2+}$. All listed thermodynamic and electrochemical properties are correct. **Correct Options**: (A, B, C, D)
- **Q20**: Thermodynamic definitions of ideal and non-ideal solutions. **Correct Options**: (A, B, C, D)
- **Q21**: $[Co(NH_3)_4 Cl_2]^+$ has *cis* and *trans* forms. *trans* has inversion center (achiral), *cis* has $C_{2v}$ symmetry without inversion center, but has planes of symmetry, making it optically inactive as well. Thus (B) is false. Correct are (A, C, D).
- **Q22**: Chemistry of permanganate and dichromate. LMCT gives deep color. **Correct Options**: (A, B, C, D)
- **Q23**: Mechanism of aldol condensation: $\alpha$-deprotonation, enolate attack, E1cB dehydration. **Correct Options**: (A, B, C, D)
- **Q24**: Nucleic acids and amino acids fundamentals. **Correct Options**: (A, B, C, D)

### Questions 25 to 30
- **Q25**: $\text{Ag}_2\text{CrO}_4 \rightleftharpoons 2\text{Ag}^+ + \text{CrO}_4^{2-} \implies K_{\text{sp}} = 4S^3 = 1.08 \times 10^{-12} \implies S^3 = 0.27 \times 10^{-12} = 2.7 \times 10^{-13} \implies S = 0.646 \times 10^{-4}\text{ M} \implies \mathbf{0.65}$.
- **Q26**: $87.5\%$ decomposition means $12.5\% = (1/2)^3$ remains $\implies t = 3 t_{1/2} = 90.0\text{ min} \implies \mathbf{90.00}$.
- **Q27**: $K = \frac{2 \times 1.10}{0.0591} = \frac{2.20}{0.0591} \approx 37.23 \implies \mathbf{37.23}$.
- **Q28**: $\Delta T_f = i K_f m \implies 0.2046 = (1+\alpha)(1.86)(0.10) \implies 1+\alpha = 1.10 \implies \alpha = 0.10 = 10\% \implies \mathbf{10.00}$.
- **Q29**: $[\text{Co}(\text{NH}_3)_5 \text{Cl}]\text{Cl}_2 \implies$ coordination number of Co is $5 + 1 = 6 \implies \mathbf{6.00}$.
- **Q30**: $\text{C}_6\text{H}_6(l) + \frac{15}{2}\text{O}_2(g) \to 6\text{CO}_2(g) + 3\text{H}_2\text{O}(l) \implies \Delta n_g = 6 - 7.5 = -1.5 \implies |\Delta n_g| = \mathbf{1.50}$.

### Questions 31 to 36
- **Q31**: Diamminechloridonitrito-N-platinum(II). **Correct: (A)**.
- **Q32**: Ethanol ($\text{C}_2\text{H}_5\text{OH}$) and Dimethyl ether ($\text{CH}_3\text{OCH}_3$) are functional isomers. **Correct: (A)**.
- **Q33**: $\text{O}_2$ oxidizes silver to cyanide complex. **Correct: (A)**.
- **Q34**: $\Lambda_m = \frac{1000 \kappa}{M} \implies \kappa = \frac{120 \times 0.01}{1000} = 1.2 \times 10^{-3}\text{ S cm}^{-1}$. **Correct: (A)**.
- **Q35**: Tropylium cation has $6\pi$ aromatic stabilization. **Correct: (A)**.
- **Q36**: $1665 / 4 = 416.25\text{ kJ/mol}$. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: $f'(x) = \frac{1 - \ln x}{x^2}$. Maximum at $x=e$ with value $1/e$. Since $f(e) > f(\pi)$, $\frac{\ln e}{e} > \frac{\ln \pi}{\pi} \implies e^\pi > \pi^e$. **Correct Options**: (A, B, C, D)
- **Q38**: Properties of skew-symmetric matrices. In odd dimensions $\det(A) = 0$. Cayley transform produces an orthogonal matrix. **Correct Options**: (A, B, C, D)
- **Q39**: $\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c} = \frac{1}{2}\vec{b} \implies \vec{a} \cdot \vec{c} = 1/2, \vec{a} \cdot \vec{b} = 0$. **Correct Options**: (A, B, C, D)
- **Q40**: Walli's-type integral reduction. **Correct Options**: (A, B, C, D)
- **Q41**: Disc centered at $(3, 4)$ with radius $2$. Distance from origin is $5$. Max $|z| = 5 + 2 = 7$, min $|z| = 5 - 2 = 3$. **Correct Options**: (A, B, C, D)
- **Q42**: Standard theorems of focal chords for a parabola. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: King's property: $2I = \int_0^{\pi/2} 1 dx = \pi/2 \implies I = \pi/4 \implies k = \mathbf{4.00}$.
- **Q44**: Real distinct roots of opposite signs $\implies \Delta > 0$ and product of roots $< 0 \implies \frac{k+4}{k-2} < 0 \implies k \in (-4, 2)$. Integers: $-3, -2, -1, 0, 1 \implies 5$ values. $\mathbf{5.00}$.
- **Q45**: Arithmetico-geometric series: $S = 1/2 + 2/4 + 3/8 + \dots = 2 \implies \mathbf{2.00}$.
- **Q46**: Parametric point $P(2t+1, 3t+2, 4t+3)$. Substitute in plane: $2(2t+1) + 3(3t+2) - (4t+3) = 5 \implies 9t + 5 = 5 \implies t = 0$. $P = (1, 2, 3) \implies x_0 + y_0 + z_0 = 1 + 2 + 3 = \mathbf{6.00}$.
- **Q47**: Total ways $\binom{10}{3} = 120$. Favorable: 3 red $\binom{4}{3} = 4$, 3 black $\binom{6}{3} = 20$. Total favorable $= 24$. $P = 24/120 = 1/5$. $m + n = 1 + 5 = \mathbf{6.00}$.
- **Q48**: Sphere equation: $x^2 + y^2 + z^2 - 2x - 4y - 6z = 0$. Center $(1, 2, 3)$, radius $R = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14} \implies R^2 = \mathbf{14.00}$.

### Questions 49 to 54
- **Q49**: $\lim_{x \to 0} \frac{(1 + x^2 + \dots) - (1 - x^2/2 + \dots)}{x^2} = 1 + 1/2 = 3/2$. **Correct: (C)**.
- **Q50**: Integrating factor $e^{\int \tan x dx} = \sec x$. $y\sec x = \int \sec^2 x dx = \tan x + C$. $y(0) = 0 \implies C = 0$. $y = \sin x$. $y(\pi/4) = 1/\sqrt{2}$. **Correct: (C)**.
- **Q51**: $e = \sqrt{1 + b^2/a^2} = \sqrt{1 + 9/16} = 5/4$. **Correct: (B)**.
- **Q52**: Vowels: A, E, A, I (4 vowels with two A's). Consonants: M, T, H, M, T, C, S (7 consonants with two M's and two T's). Number of ways: $\frac{8!}{2! 2!} \times \frac{4!}{2!} = 10080 \times 12 = 120960$. **Correct: (A)**.
- **Q53**: $(a^2 + b^2) = (\sin\alpha + \sin\beta)^2 + (\cos\alpha + \cos\beta)^2 = 2 + 2\cos(\alpha - \beta) \implies \cos(\alpha - \beta) = \frac{a^2 + b^2 - 2}{2}$. **Correct: (A)**.
- **Q54**: By induction, $A^n = \begin{pmatrix} 1 & 2n \\ 0 & 1 \end{pmatrix} \implies A^{10} = \begin{pmatrix} 1 & 20 \\ 0 & 1 \end{pmatrix}$. **Correct: (A)**.
