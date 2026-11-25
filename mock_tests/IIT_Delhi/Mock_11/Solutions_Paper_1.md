# Detailed Pedagogical Solutions — Mock Examination 11 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Relativistic Compton Scattering, Kinematics of Elastic Photon-Electron Collisions.
- **2. Derivation**:
  - Conservation of four-momentum gives $\lambda' - \lambda_0 = \frac{h}{m_e c}(1 - \cos\theta) = \lambda_C(1 - \cos\theta)$. (A) is correct.
  - Kinetic energy transferred to electron: $K_e = E_0 - E' = h\nu_0 - \frac{h c}{\lambda'} = E_0\left(1 - \frac{1}{1 + \alpha(1-\cos\theta)}\right) = \frac{E_0 \alpha(1-\cos\theta)}{1 + \alpha(1-\cos\theta)}$. (B) is correct.
  - Longitudinal and transverse momentum conservation: $p_e \cos\phi = \frac{h\nu_0}{c} - \frac{h\nu'}{c}\cos\theta$, $p_e \sin\phi = \frac{h\nu'}{c}\sin\theta$. Dividing gives $\cot\phi = (1 + \alpha)\tan(\theta/2)$. (C) is correct.
  - Compton edge occurs at $\theta = 180^\circ$ where $\cos\theta = -1 \implies K_{\text{max}} = \frac{2\alpha E_0}{1 + 2\alpha}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Coupled Oscillators, Normal Modes, Beat Phenomenon.
- **2. Derivation**:
  - Equations of motion: $m l^2 \ddot{\theta}_1 = -m g l \theta_1 - k d^2(\theta_1 - \theta_2)$, $m l^2 \ddot{\theta}_2 = -m g l \theta_2 - k d^2(\theta_2 - \theta_1)$.
  - Symmetric mode ($\theta_1 = \theta_2$): spring is unstretched, so restoring force is purely gravity, giving $\omega_1 = \sqrt{g/l}$. (A) is correct.
  - Antisymmetric mode ($\theta_1 = -\theta_2$): spring stretch is $2d\theta$, giving $\omega_2 = \sqrt{\frac{g}{l} + \frac{2k d^2}{m l^2}}$. (B) is correct.
  - Initial condition produces superposition $\theta_1(t) = \theta_0 \cos(\frac{\omega_2-\omega_1}{2}t)\cos(\frac{\omega_1+\omega_2}{2}t)$, with beat period $T_{\text{beat}} = \frac{2\pi}{\omega_2-\omega_1}$. (C) is correct.
  - As $d$ increases, the spring torque increases, raising $\omega_2$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Foucault Pendulum, Coriolis Acceleration, Non-Inertial Reference Frames.
- **2. Derivation**:
  - Coriolis acceleration $\vec{a}_C = -2(\vec{\Omega}\times\vec{v})$. In Northern Hemisphere, vertical component of Earth's rotation $\Omega_z = \Omega\sin\lambda$ causes clockwise precession. (A) is correct.
  - Precession rate $\Omega_p = \Omega_{\text{Earth}}\sin\lambda$. (B) is correct.
  - At $\lambda = 90^\circ$, $\Omega_p = \Omega_{\text{Earth}}$, completing $360^\circ$ in one sidereal day ($23.93\text{ h}$). (C) is correct.
  - At equator ($\lambda = 0$), $\sin\lambda = 0$, so plane of oscillation remains fixed in inertial space ($\Omega_p = 0$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Berthelot Real Gas Equation, Critical State Thermodynamics.
- **2. Derivation**:
  - Internal pressure $a/(T V^2)$ captures temperature-dependent cohesion. (A) is correct.
  - Critical conditions: $(\partial P/\partial V)_T = 0, (\partial^2 P/\partial V^2)_T = 0$.
  - Logarithmic derivative yields $V_c = 3b$. (B) is correct.
  - Second derivative yields $T_c = \sqrt{\frac{8a}{27Rb}}$. (C) is correct.
  - Substituting $V_c$ and $T_c$ gives $Z_c = \frac{P_c V_c}{R T_c} = \frac{3}{8} = 0.375$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Wave Plates, Birefringence, Optical Activity.
- **2. Derivation**:
  - QWP introduces phase difference $\delta = \frac{2\pi}{\lambda}|n_e - n_o|d = \pi/2$ ($\Delta L = \lambda/4$). (A) is correct.
  - Incident linear polarization at $45^\circ$ has equal $x$ and $y$ components, so $\pi/2$ phase shift produces circular polarization. (B) is correct.
  - HWP introduces $\pi$ phase shift, reflecting the polarization vector across the fast axis, rotating it by $2\theta$. (C) is correct.
  - Optical activity is caused by circular birefringence ($\mu_R \ne \mu_L$). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Variable Mass Dynamics, Tsiolkovsky Rocket Equation in Gravity.
- **2. Derivation**:
  - Momentum conservation on system: $(m + dm)(v + dv) + (-dm)(v - u) - m v = -m g dt \implies m dv = -u dm - m g dt$. With $dm/dt = -\alpha$, $m \frac{dv}{dt} = u \alpha - m g$. (A) is correct.
  - Integrating from $0$ to $t$: $v(t) = u \ln\left(\frac{m_0}{m_0 - \alpha t}\right) - gt$. (B) is correct.
  - Thrust force is $F_{\text{thrust}} = u \alpha$. (C) is correct.
  - For positive upward initial acceleration, $u \alpha > m_0 g$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: $\Delta\lambda = \lambda_C(1 - \cos 180^\circ) = 2\lambda_C = 2(0.0243\text{ \AA}) = 0.0486\text{ \AA}$.
  Fractional shift: $\frac{\Delta\lambda}{\lambda_0} = \frac{0.0486}{0.0500} = 0.972 \approx 0.97$.
- **Question 8**: Two capacitors in series: $C_1 = \frac{\varepsilon_0 A}{d/2} = \frac{2\varepsilon_0 A}{d}$, $C_2 = \frac{\varepsilon_0 \varepsilon_r A}{d/2} = \frac{2\varepsilon_0 \varepsilon_r A}{d}$.
  $C_{\text{eff}} = \frac{C_1 C_2}{C_1 + C_2} = \frac{2\varepsilon_0 A}{d}\frac{\varepsilon_r}{1 + \varepsilon_r} = \frac{2(8.854 \times 10^{-12})(0.040)}{2.0 \times 10^{-3}}\left(\frac{4.0}{5.0}\right) = (3.5416 \times 10^{-10})(0.80) = 2.833 \times 10^{-10}\text{ F} = 283.3\text{ pF}$.
- **Question 9**: Central diffraction minimum occurs at $a\sin\theta = \lambda \implies \sin\theta = \lambda/a$.
  Interference maxima occur at $d\sin\theta = m\lambda$. At diffraction minimum, $m = d/a = \frac{0.200}{0.040} = 5$.
  Thus orders $m = -4, -3, -2, -1, 0, 1, 2, 3, 4$ are visible within central maximum.
  Total bright fringes $= 2(4) + 1 = 9$.
- **Question 10**: $W = \int_{V_1}^{V_2} P dV = \alpha \int_{1.0}^{2.0} V^2 dV = \alpha\left[\frac{V^3}{3}\right]_1^2 = \frac{2.0 \times 10^5}{3}(8 - 1) = \frac{14.0 \times 10^5}{3} \approx 4.67 \times 10^5\text{ J} = 466.67\text{ kJ}$.
- **Question 11**: $K = q V = (2e)(1.0 \times 10^6\text{ V}) = 2.0\text{ MeV}$.
- **Question 12**: $T = 2\pi\sqrt{L/g} \implies L = \frac{g T^2}{4\pi^2} = \frac{9.80(4.00)}{4(9.87)} = \frac{9.80}{9.87} \approx 0.99\text{ m}$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $a_c = \frac{v^2}{R} = \frac{(a_t t)^2}{R} = a_t \implies \frac{a_t^2 t^2}{R} = a_t \implies t = \sqrt{\frac{R}{a_t}} = \sqrt{\frac{2.0}{3.0}} \approx 0.82\text{ s}$. Option (A).
- **Question 14**: $\vec{E} = -\nabla V = -\left(\frac{\partial V}{\partial x}\hat{i} + \frac{\partial V}{\partial y}\hat{j} + \frac{\partial V}{\partial z}\hat{k}\right) = -(8x\hat{i} - 6y\hat{j} + 4z\hat{k})$. At $(1, 1, 1)$, $\vec{E} = -8\hat{i} + 6\hat{j} - 4\hat{k}\text{ V/m}$. Option (A).
- **Question 15**: $v = \sqrt{\gamma R T / M}$. Ratio $v_1 / v_2 = \sqrt{M_2 / M_1} = \sqrt{40.0 / 4.0} = \sqrt{10} \approx 3.16$. Option (A).
- **Question 16**: $m = f_o / f_e = 100.0 / 5.0 = 20$; $L = f_o + f_e = 100.0 + 5.0 = 105.0\text{ cm}$. Option (A).
- **Question 17**: $K = U \implies \frac{1}{2}k(A^2 - x^2) = \frac{1}{2}k x^2 \implies 2x^2 = A^2 \implies x = A/\sqrt{2}$. Option (A).
- **Question 18**: Diamagnetic materials have negative, small, and temperature-independent susceptibility. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Curtius rearrangement decomposes acyl azides to isocyanates with nitrogen extrusion. Group migrates with retention of configuration. Hydrolysis yields primary amines. Schmidt reaction uses carboxylic acid and $\text{HN}_3$. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Michaelis-Menten rate law $v_0 = \frac{V_{\max}[S]}{K_m + [S]}$. Competitive inhibition increases $K_m$ ($V_{\max}$ unchanged). Non-competitive reduces $V_{\max}$ ($K_m$ unchanged). Correct options: **(A), (B), (C), (D)**.
- **Question 21**: Quinhydrone is $1:1$ complex of quinone and hydroquinone. Redox couple is $\text{Q} + 2\text{H}^+ + 2e^- \rightleftharpoons \text{QH}_2$. Potential is $E = 0.6996 - 0.0591\text{ pH}$. Fails above $\text{pH} = 8.5$ due to hydroquinone ionization. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: Oxides form CCP array. Normal spinel: $\text{A}^{2+}$ in $1/8$ tetrahedral, $\text{B}^{3+}$ in $1/2$ octahedral. Inverse spinel: $\text{Fe}^{3+}[\text{Fe}^{2+}\text{Fe}^{3+}]\text{O}_4$. Governed by octahedral CFSE gain. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Edman degradation uses PITC on N-terminus under basic conditions. Acid cleavage yields ATZ intermediate. ATZ isomerizes to PTH amino acid. Shortened peptide undergoes repetitive cycles. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Interhalogens $\text{XX}'_n$ have polar bonds, making them more reactive than pure halogens (except $\text{F}_2$). $\text{IF}_7$ is pentagonal bipyramidal ($sp^3d^3$). Hydrolysis gives halide from smaller and oxohalide from larger halogen. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $\text{Mg(OH)}_2 \rightleftharpoons \text{Mg}^{2+} + 2\text{OH}^-$. $K_{sp} = S(2S)^2 = 4S^3 \implies 4S^3 = 1.2 \times 10^{-11} \implies S^3 = 3.0 \times 10^{-12} \implies S = (3.0)^{1/3} \times 10^{-4} = 1.44 \times 10^{-4}\text{ M}$.
  $[\text{OH}^-] = 2S = 2.88 \times 10^{-4}\text{ M} \implies p\text{OH} = 4 - \log(2.88) = 4 - 0.459 = 3.541 \implies \text{pH} = 14 - 3.541 = 10.46$.
- **Question 26**: $\frac{1}{[A]} - \frac{1}{[A]_0} = k t \implies \frac{1}{0.050} - \frac{1}{0.20} = 0.050 t \implies 20.0 - 5.0 = 15.0 = 0.050 t \implies t = \frac{15.0}{0.050} = 300.0\text{ s}$.
- **Question 27**: For FCC lattice: $4r = \sqrt{2}a \implies r = \frac{\sqrt{2} \times 400.0}{4} = \frac{1.414 \times 400.0}{4} = 141.4\text{ pm}$.
- **Question 28**: $\Delta G^\circ = -n F E^\circ = -2(96485)(1.20) = -231564\text{ J/mol} = -231.6\text{ kJ/mol}$.
- **Question 29**: $\Delta T_f = i K_f m = (1.20)(1.86)(0.10) = 0.2232\text{ K} \approx 0.22\text{ K}$.
- **Question 30**: In $[Co(en)_2Cl_2]^+$, `en` is bidentate (occupies 2 coordination sites each), and two chloride ligands are monodentate. Total coordination number $= 2(2) + 2 = 6$.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Gabriel phthalimide is exclusively used for pure primary aliphatic amines. Option (A).
- **Question 32**: $[\text{Ni(CN)}_4]^{2-}$ is $dsp^2$ square planar with strong field $\text{CN}^-$, pairing all 8 $d$-electrons (diamagnetic). Option (A).
- **Question 33**: Sodium ethyl xanthate serves as a collector in froth flotation. Option (A).
- **Question 34**: $\text{ClF}_3$ has 3 bond pairs and 2 lone pairs ($sp^3d$), T-shaped. Option (A).
- **Question 35**: An $\alpha\text{-helix}$ is a classic secondary structure of proteins. Option (A).
- **Question 36**: Nylon-6,6 is formed by condensation of hexamethylenediamine and adipic acid. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Bernoulli ODE: $y' + \frac{1}{x}y = x y^2$. Dividing by $y^2$: $y^{-2}y' + \frac{1}{x}y^{-1} = x$.
  Let $v = y^{-1} \implies v' = -y^{-2}y'$. Thus $-v' + \frac{1}{x}v = x \implies v' - \frac{1}{x}v = -x$. (A) is correct.
  $\text{IF} = e^{-\int (1/x)dx} = 1/x$. (B) is correct.
  $\frac{v}{x} = \int (-1)dx = -x + C \implies v = C x - x^2$. (C) is correct.
  $y = 1/v = \frac{1}{C x - x^2}$. (D) is correct.
- **Question 38**: Similar matrices: $\det(\lambda I - P^{-1} A P) = \det(P^{-1}(\lambda I - A)P) = \det(\lambda I - A)$, preserving characteristic polynomial, eigenvalues, multiplicities, trace, determinant, and rank. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Chord of contact from $(x_0, y_0)$ is $\frac{x x_0}{a^2} - \frac{y y_0}{b^2} = 1$. Passing through focus $(a e, 0)$ gives $\frac{a e x_0}{a^2} = 1 \implies x_0 = a/e$ (directrix). Director circle is $x^2 + y^2 = a^2 - b^2$. For $a = b$, director circle reduces to single point $(0, 0)$. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Family of planes $P_1 + \lambda P_2 = 0$ contains the line of intersection. Line direction is parallel to $\vec{n}_1 \times \vec{n}_2$. Perpendicularity condition holds. Every line point satisfies both plane equations. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Catalan numbers: $C_0=1, C_1=1, C_2=2, C_3=5, C_4=14, C_5=42$. Segner recurrence holds. Dyck paths and balanced parentheses are classic interpretations. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Normal distribution: symmetric about $\mu$; inflection points at $\mu \pm \sigma$; $1\sigma$ interval contains $68.27\%$; $2\sigma$ interval contains $95.45\%$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: $\int_0^1 x^3 e^x dx = [x^3 e^x]_0^1 - 3\int_0^1 x^2 e^x dx = e - 3([x^2 e^x]_0^1 - 2\int_0^1 x e^x dx) = e - 3(e - 2(e - (e - 1))) = e - 3(e - 2) = e - 3e + 6 = 6 - 2e$. Thus $m = 2$.
- **Question 44**: $y = \ln(1 + x^2) \implies \frac{dy}{dx} = \frac{2x}{1 + x^2}$. At $x = 1$, $\frac{dy}{dx} = \frac{2(1)}{1 + 1} = \frac{2}{2} = 1.00$.
- **Question 45**: $d = \frac{|2(1) + 1(2) - 2(3) + 8|}{\sqrt{2^2 + 1^2 + (-2)^2}} = \frac{|2 + 2 - 6 + 8|}{\sqrt{9}} = \frac{6}{3} = 2.00$.
- **Question 46**: Infinite GP $a = 18, r = 1/3 \implies S = \frac{18}{1 - 1/3} = \frac{18}{2/3} = 27.00$.
- **Question 47**: Vandermonde determinant $D = (b - a)(c - a)(c - b) = (2 - 1)(4 - 1)(4 - 2) = (1)(3)(2) = 6.00$.
- **Question 48**: $P(5, 4) = 5 \times 4 \times 3 \times 2 = 120.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Maclaurin expansion $\tan x = x + x^3/3 + \dots \implies \frac{\tan x - x}{x^3} \to 1/3$. Option (A).
- **Question 50**: Ellipse $\frac{x^2}{25} + \frac{y^2}{9} = 1 \implies a = 5, b = 3$. Length of latus rectum $= 2b^2/a = 2(9)/5 = 18/5 = 3.60$. Option (A).
- **Question 51**: First plane $2x - y + 2z = 4$. Second plane $2x - y + 2z = 10$. Distance $d = \frac{|10 - 4|}{\sqrt{4 + 1 + 4}} = \frac{6}{3} = 2.00$. Option (A).
- **Question 52**: $z = \cos(\pi/3) + i\sin(\pi/3) = e^{i\pi/3} \implies z^3 = e^{i\pi} = -1$. Option (A).
- **Question 53**: $\text{IF} = e^{\int \cot x dx} = e^{\ln\sin x} = \sin x$. Option (A).
- **Question 54**: Favorable pairs summing to 8: $(2,6), (3,5), (4,4), (5,3), (6,2)$ (5 outcomes). $P = 5/36$. Option (A).
