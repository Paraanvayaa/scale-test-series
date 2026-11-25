# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 13

---

### PART I: PHYSICS

#### Solution 1: Stern-Gerlach Gradient Deflection
1. **Core Concept / Theory**:
   The magnetic force on a dipole $\vec{\mu} = \mu_z \hat{k}$ in an inhomogeneous field $\vec{B}$ is $\vec{F} = \nabla(\vec{\mu} \cdot \vec{B}) = \mu_z \frac{\partial B_z}{\partial z} \hat{k} = \mu_B \alpha \hat{k}$.
2. **Maxwell Constraint**:
   $\nabla \cdot \vec{B} = \frac{\partial B_x}{\partial x} + \frac{\partial B_z}{\partial z} = -\alpha + \alpha = 0$, confirming physical realizability.
3. **Kinematics in Magnet**:
   Time inside field $t_1 = L/v_0$. Acceleration $a_z = \frac{\mu_B \alpha}{m}$. Exit deflection $z_1 = \frac{1}{2} a_z t_1^2 = \frac{\mu_B \alpha L^2}{2 m v_0^2}$.
4. **Drift Region**:
   Exit velocity $v_z = a_z t_1 = \frac{\mu_B \alpha L}{m v_0}$. Additional deflection in drift space $D$: $z_2 = v_z (D/v_0) = \frac{\mu_B \alpha L D}{m v_0^2}$.
   Total deflection $z_{\text{total}} = z_1 + z_2 = \frac{\mu_B \alpha L}{m v_0^2}\left(\frac{L}{2} + D\right)$.
- **Conclusion**: Statements (A), (B), (C), and (D) are all rigorously correct.
- **Correct Option**: (A, B, C, D)

#### Solution 2: Dieterici Real Gas
1. **Critical Conditions**:
   $\left(\frac{\partial P}{\partial V_m}\right)_{T_c} = 0$ and $\left(\frac{\partial^2 P}{\partial V_m^2}\right)_{T_c} = 0$.
2. **Critical Parameters**:
   Solving gives $V_c = 2b$, $T_c = \frac{a}{4 R b}$, and $P_c = \frac{a}{4 e^2 b^2}$.
3. **Compressibility Factor**:
   $Z_c = \frac{P_c V_c}{R T_c} = \frac{(a / 4 e^2 b^2)(2b)}{R (a / 4 R b)} = 2 e^{-2} \approx 0.271$.
4. **Joule-Thomson Inversion**:
   Inversion curve condition $\left(\frac{\partial T}{\partial P}\right)_H = 0 \iff T\left(\frac{\partial V}{\partial T}\right)_P - V = 0$. In dilute gas limit, this yields $T_i(V_m) = \frac{a}{R b}\left(\frac{V_m - b}{V_m}\right)$.
- **Correct Option**: (A, B, C, D)

#### Solution 3: Inhomogeneous Dielectric Capacitor
1. **Displacement Field**:
   By Gauss's law for $\vec{D}$, $\oint \vec{D} \cdot d\vec{A} = Q \implies D(r) \cdot 2\pi r L = Q \implies D(r) = \frac{Q}{2\pi r L}\hat{r}$.
2. **Electric Field**:
   $\vec{E}(r) = \frac{\vec{D}(r)}{\varepsilon(r)} = \frac{Q / (2\pi r L)}{\varepsilon_0 a / r} = \frac{Q}{2\pi \varepsilon_0 a L}\hat{r}$, completely uniform and independent of $r$.
3. **Potential Difference**:
   $V = \int_a^b E dr = \frac{Q}{2\pi \varepsilon_0 a L}(b - a)$.
4. **Capacitance**:
   $C = \frac{Q}{V} = \frac{2\pi \varepsilon_0 a L}{b - a}$.
- **Correct Option**: (A, B, C, D)

#### Solution 4: Rotating Charged Ring
1. **Magnetic Moment**:
   Current $I = \frac{Q}{T} = \frac{Q \omega}{2\pi}$. Area $A = \pi R^2$. Dipole moment $\mu = I A = \frac{1}{2} Q \omega R^2$.
2. **Electrostatic Potential**:
   All points on ring are at distance $\sqrt{R^2 + x^2}$, so $V(x) = \frac{Q}{4\pi \varepsilon_0 \sqrt{R^2 + x^2}}$.
3. **Conservation of Energy**:
   $\Delta K = q(V(x_0) - V(0)) = q Q \frac{1}{4\pi\varepsilon_0}\left(\frac{1}{R} - \frac{1}{\sqrt{R^2 + 3R^2}}\right) = \frac{q Q}{8\pi\varepsilon_0 R}$.
   $\frac{1}{2} m v^2 = \frac{q Q}{8\pi\varepsilon_0 R} \implies v = \sqrt{\frac{q Q}{4\pi\varepsilon_0 m R}}$.
4. **Magnetic Field at Center**:
   $B = \frac{\mu_0 I}{2R} = \frac{\mu_0 (Q\omega / 2\pi)}{2R} = \frac{\mu_0 Q \omega}{4\pi R}$.
- **Correct Option**: (A, B, C, D)

#### Solution 5: Fabry-Pérot Interferometer
- All parameters (A), (B), (C), (D) follow from standard Airy formula for multi-beam interference.
- **Correct Option**: (A, B, C, D)

#### Solution 6: Rolling Sphere in Cycloidal Track
- Motion on an inverted cycloid exhibits exact isochronism (tautochrone property), even for large amplitudes.
- $T = 2\pi \sqrt{\frac{7(4R - r)}{5g}}$ accounting for rotational inertia $I = \frac{2}{5} m r^2$.
- Mechanical energy is conserved because instantaneous contact velocity is zero.
- **Correct Option**: (A, B, C, D)

#### Solution 7: LC with Variable Inductance
- Using adiabatic invariant of harmonic oscillator $E/\omega = \text{constant}$.
- Since $\omega(t) = \frac{1}{\sqrt{L(t)C}} \propto (1 + \alpha t)^{-1/2}$, energy $E(t) \propto \omega(t) \propto (1 + \alpha t)^{-1/2}$.
- Since $E = \frac{1}{2} C V_{\text{rms}}^2$, $V_{\text{rms}} \propto \sqrt{E} \propto (1 + \alpha t)^{-1/4}$.
- Therefore $\gamma = 0.25 \implies 100\gamma = 25$.
- **Answer**: 25

#### Solution 8: Gyroscope Precession
- Torque due to gravity: $\tau = M g d = 2 \times 9.8 \times 0.15 = 2.94\text{ N}\cdot\text{m}$.
- Spin angular momentum: $L_s = I \omega_s = \left(\frac{1}{2} M R^2\right) \omega_s = \frac{1}{2} (2) (0.01) (600) = 6.0\text{ kg m}^2/\text{s}$.
- Precession rate: $\Omega_p = \frac{\tau}{L_s} = \frac{2.94}{6.0} = 0.49\text{ rad/s}$.
- **Answer**: 0.49

#### Solution 9: Blackbody Radiative Cooling
- Rate of heat loss: $M s \frac{dT}{dt} = -e \sigma A T^4 \implies \frac{dT}{dt} = -\frac{4\pi R^2 \sigma}{M s} T^4$.
- Let $k = \frac{4\pi R^2 \sigma}{M s} = \frac{4\pi (0.05)^2 (5.67 \times 10^{-8})}{1.0 \times 400} = \frac{3.1416 \times 0.01 \times 5.67 \times 10^{-8}}{400} = 4.453 \times 10^{-12}\text{ K}^{-3}\text{s}^{-1}$.
- Integrating: $\int_{T_0}^{T_1} T^{-4} dT = -k t \implies \frac{1}{3}\left(\frac{1}{T_1^3} - \frac{1}{T_0^3}\right) = k t$.
- $\frac{1}{3}\left(\frac{1}{250^3} - \frac{1}{500^3}\right) = \frac{1}{3}\left(\frac{8 - 1}{500^3}\right) = \frac{7}{3 \times 1.25 \times 10^8} = 1.867 \times 10^{-8}$.
- $t = \frac{1.867 \times 10^{-8}}{4.453 \times 10^{-12}} \approx 4192\text{ s}$.
- **Answer**: 4192

#### Solution 10: Relativistic Threshold Energy
- In center-of-momentum frame, final state has 4 stationary protons: invariant mass squared $s = (4 m_p)^2 = 16 m_p^2$.
- In laboratory frame before collision: $s = (P_1 + P_2)^2 = m_p^2 + m_p^2 + 2(E_1 m_p - \vec{p}_1 \cdot \vec{0}) = 2 m_p^2 + 2 E_1 m_p$.
- Equating: $2 m_p^2 + 2 E_1 m_p = 16 m_p^2 \implies 2 E_1 m_p = 14 m_p^2 \implies E_1 = 7 m_p c^2$.
- Thus $k = 7$.
- **Answer**: 7

#### Solution 11: Mutual Inductance & Induced Loop Current
- Magnetic flux through outer loop of radius $b > a$ is confined to solenoid radius $a$:
  $\Phi(t) = B(t) \cdot \pi a^2 = (\mu_0 n I_0 \sin\omega t) \pi a^2$.
- Induced EMF: $\mathcal{E}(t) = -\frac{d\Phi}{dt} = -\mu_0 n \pi a^2 I_0 \omega \cos\omega t$.
- Peak EMF: $\mathcal{E}_{\text{peak}} = (4\pi \times 10^{-7}) (1000) \pi (0.04)^2 (5) (100\pi) = 4\pi^3 \times 10^{-4} \times 1.6 \times 10^{-3} \times 500 \approx 0.0099\text{ V}$.
- Peak current: $I_{\text{peak}} = \frac{\mathcal{E}_{\text{peak}}}{R_{\text{loop}}} = \frac{0.0099}{0.02} \approx 0.49\text{ A}$.
- **Answer**: 0.49

#### Solution 12: Piston Equilibrium Displacement
- Piston mass $m = 10\text{ kg}$, weight $W = mg = 98\text{ N}$.
- Area $A = 0.05\text{ m}^2$. Pressure difference $\Delta P = \frac{mg}{A} = \frac{98}{0.05} = 1960\text{ Pa}$.
- Upper gas: expands from $h_0 = 0.6\text{ m}$ to $h_0 + \Delta h$. $P_1 = P_0 \frac{h_0}{h_0 + \Delta h} \approx P_0 (1 - \Delta h / h_0)$.
- Lower gas: compresses to $h_0 - \Delta h$. $P_2 = P_0 \frac{h_0}{h_0 - \Delta h} \approx P_0 (1 + \Delta h / h_0)$.
- $P_2 - P_1 = 2 P_0 \frac{\Delta h}{h_0} = \frac{mg}{A}$.
- $\Delta h = \frac{mg h_0}{2 P_0 A} = \frac{98 \times 0.6}{2 \times 10^5 \times 0.05} = \frac{58.8}{10000} = 0.00588\text{ m} = 5.88\text{ mm}$.
- **Answer**: 5.88

#### Solution 13: Central Potential
- Effective potential $V_{\text{eff}}(r) = \frac{L^2 + 2mc}{2mr^2} - \frac{k}{r}$.
- Modifies angular frequency, leading to perihelion precession $\Delta\theta = 2\pi\left(\frac{L}{\sqrt{L^2 + 2mc}} - 1\right)$.
- **Correct Option**: (A)

#### Solution 14: Beat Spatial Envelope
- $\Delta k = k_1 - k_2 = \frac{2\pi}{\lambda} - \frac{2\pi}{\lambda + \Delta\lambda} \approx \frac{2\pi \Delta\lambda}{\lambda^2}$.
- Spatial envelope repeat length $\Delta x = \frac{2\pi}{\Delta k} = \frac{\lambda^2}{\Delta\lambda}$.
- **Correct Option**: (B)

#### Solution 15: Sphere on Accelerating Conveyor
- In belt frame, fictitious force $M a_0$ acts at CM. Rolling constraint: $a_{\text{rel}} = \frac{a_0}{1 + I/(MR^2)} = \frac{a_0}{1 + 2/5} = \frac{5}{7} a_0$ opposite to belt.
- In ground frame: $a_{\text{cm}} = a_0 - a_{\text{rel}} = a_0 - \frac{5}{7} a_0 = \frac{2}{7} a_0$.
- **Correct Option**: (A)

#### Solution 16: Reduced Mass Correction
- Reduced mass $\mu = \frac{m_e M}{m_e + M} = \frac{m_e (4m_e)}{5m_e} = \frac{4}{5} m_e$.
- Frequency $\nu \propto \mu \implies \nu = \frac{4}{5} \nu_\infty$.
- **Correct Option**: (A)

#### Solution 17: Falling Conducting Loop
- Motional EMF $\mathcal{E} = B_0 a v$. Induced current $I = \frac{B_0 a v}{R}$. Magnetic retarding force $F_B = I a B_0 = \frac{B_0^2 a^2 v}{R}$.
- Terminal velocity when $F_B = mg \implies v_t = \frac{mg R}{B_0^2 a^2}$.
- **Correct Option**: (A)

#### Solution 18: Doppler Effect Circular Path
- Maximum frequency occurs when velocity component directed towards observer is maximum ($\omega R$ along line of sight).
- $f_{\text{max}} = f_0 \frac{v}{v - \omega R}$.
- **Correct Option**: (A)

---

### PART II: CHEMISTRY

#### Solution 19: Zeise's Salt
- All four statements (A), (B), (C), (D) correctly articulate the Dewar-Chatt-Duncanson model and geometry of Zeise's salt.
- **Correct Option**: (A, B, C, D)

#### Solution 20: Shapiro Reaction Mechanism
- Explains the two deprotonations, nitrogen extrusion, vinyllithium formation and trapping.
- **Correct Option**: (A, B, C, D)

#### Solution 21: Langmuir Adsorption
- Note: Statement (D) is false because adsorption is exothermic ($\Delta H_{\text{ads}} < 0$), so by van 't Hoff equation, the adsorption equilibrium constant $K$ *decreases* with increasing temperature. Thus (A, B, C) are correct.
- **Correct Option**: (A, B, C)

#### Solution 22: Borazine vs Benzene
- Borazine has localized polar bonds ($\text{B}^{\delta+}-\text{N}^{\delta-}$), reacts readily with $\text{HCl}$ by addition, and hydrolyzes to $\text{H}_3\text{BO}_3$, $\text{NH}_3$, and $\text{H}_2$.
- **Correct Option**: (A, B, C, D)

#### Solution 23: Cyano Iron Complexes
- Nernst potential shift: $E^\circ = 0.77 - 0.0591 \log(10^{42}/10^{35}) = 0.77 - 0.41 = 0.36\text{ V}$.
- Electronic configurations: $t_{2g}^6$ (diamagnetic) and $t_{2g}^5$ (paramagnetic, 1 unpaired electron).
- **Correct Option**: (A, B, C, D)

#### Solution 24: Stille Coupling
- All four steps represent the classic catalytic cycle of the Stille reaction.
- **Correct Option**: (A, B, C, D)

#### Solution 25: Radioactive Succession Bateman Equation
- $t_{\text{max}} = \frac{\ln(\lambda_B / \lambda_A)}{\lambda_B - \lambda_A} = \frac{\ln(0.20 / 0.04)}{0.20 - 0.04} = \frac{\ln 5}{0.16} = \frac{1.609}{0.16} = 10.06\text{ h}$.
- **Answer**: 10.06

#### Solution 26: CFSE of Low-Spin $[Co(NH_3)_6]^{3+}$
- $\text{Co}^{3+}$ is $d^6$. With strong-field $\text{NH}_3$, $\Delta_o = 23,000 > P = 19,000$, forming low-spin $t_{2g}^6 e_g^0$.
- Orbital CFSE: $6 \times (-0.4 \Delta_o) = -2.4 \Delta_o = -2.4 \times 23,000 = -55,200\text{ cm}^{-1}$.
- Net pairing energy: High-spin $d^6$ has 1 pair; low-spin has 3 pairs $\implies 2$ extra pairs $= 2 \times 19,000 = +38,000\text{ cm}^{-1}$.
- Net CFSE magnitude: $|-55,200 + 38,000| = 17,200\text{ cm}^{-1} = 17.2 \times 10^3\text{ cm}^{-1}$.
- **Answer**: 17.2

#### Solution 27: Mutarotation Equilibrium
- $K_{\text{eq}} = \frac{k_1}{k_{-1}} = \frac{0.0065}{0.0035} = \frac{13}{7} \approx 1.857$.
- Fraction of $\beta$ form: $\frac{[\beta]}{[\alpha] + [\beta]} = \frac{K}{1 + K} = \frac{13/7}{1 + 13/7} = \frac{13}{20} = 65\%$.
- **Answer**: 65

#### Solution 28: Common Ion Effect on PbI2
- $[\text{I}^-] \approx 0.10\text{ M}$.
- $K_{sp} = [\text{Pb}^{2+}][\text{I}^-]^2 \implies 7.1 \times 10^{-9} = S \times (0.10)^2 \implies S = 7.1 \times 10^{-7}\text{ M}$.
- Thus $X = 7.1$.
- **Answer**: 7.1

#### Solution 29: Faraday's Law Electrolysis
- Charge $Q = I t = 2.5 \times 3860 = 9650\text{ C}$.
- Moles of electrons: $n_e = \frac{9650}{96500} = 0.10\text{ mol}$.
- $\text{Cu}^{2+} + 2e^- \to \text{Cu}$, so moles of $\text{Cu} = 0.05\text{ mol}$.
- Mass $m = 0.05 \times 63.5 = 3.175\text{ g} \approx 3.18\text{ g}$.
- **Answer**: 3.18

#### Solution 30: N2O4 Dissociation Pressure Shift
- $K_p = \frac{4\alpha^2 P}{1 - \alpha^2} = \frac{4(0.04)(1)}{0.96} = \frac{0.16}{0.96} = \frac{1}{6}\text{ atm}$.
- At $P' = 0.25\text{ atm} = 1/4\text{ atm}$:
  $\frac{4(\alpha')^2 (1/4)}{1 - (\alpha')^2} = \frac{1}{6} \implies \frac{(\alpha')^2}{1 - (\alpha')^2} = \frac{1}{6} \implies 7(\alpha')^2 = 1 \implies \alpha' = \frac{1}{\sqrt{7}} \approx 0.378$.
- $100\alpha' = 37.8$.
- **Answer**: 37.8

#### Solution 31 to 36:
- 31: Cyclopropanone intermediate. (A)
- 32: cis-$[\text{Co}(\text{en})_2\text{Cl}_2]^+$ lacks plane of symmetry and is chiral. (A)
- 33: $v_0 = \frac{V_{\text{max}}[S]}{K_m + [S]} = \frac{3}{1+3} V_{\text{max}} = 0.75 V_{\text{max}}$. (A)
- 34: Oxygen acts as the oxidizing agent. (A)
- 35: Electrophile is dichlorocarbene ($:\text{CCl}_2$). (A)
- 36: Body diagonal $a\sqrt{3} = 2(r_+ + r_-) \implies a = \frac{2}{\sqrt{3}}(1.69 + 1.81) = \frac{7.00}{1.732} \approx 4.04\text{ \AA}$. (A)

---

### PART III: MATHEMATICS

#### Solution 37: Matrix Invariants & Eigenvalues
- Minimal polynomial factors as $(\lambda - 1)(\lambda - 2)(\lambda - 3) = 0 \implies \lambda \in \{1, 2, 3\}$.
- Trace $= 1 + 2 + 3 = 6$, determinant $= 1 \times 2 \times 3 = 6$.
- Inverse from Cayley-Hamilton: $A^{-1} = \frac{1}{6}(A^2 - 6A + 11I)$.
- Trace of matrix exponential: $\text{Tr}(e^A) = e^1 + e^2 + e^3$.
- **Correct Option**: (A, B, C, D)

#### Solution 38: Frullani Integrals
- All four results follow from standard Frullani integral theorem $\int_0^\infty \frac{f(ax)-f(bx)}{x}dx = (f(0) - f(\infty))\ln(b/a)$.
- **Correct Option**: (A, B, C, D)

#### Solution 39: Confocal Conics
- Confocal conics form an orthogonal net: at every intersection point between ellipse ($\lambda < b^2$) and hyperbola ($b^2 < \lambda < a^2$), the tangents are perpendicular.
- Through any non-axial point, exactly one ellipse and one hyperbola pass.
- **Correct Option**: (A, B, C, D)

#### Solution 40: Clairaut's Equation
- General solution is the tangent family $y = cx + c^2$.
- The singular solution is the envelope $y = -x^2/4$.
- **Correct Option**: (A, B, C, D)

#### Solution 41: Convex Functions
- Standard convexity properties, support lines, and Hermite-Hadamard inequality.
- **Correct Option**: (A, B, C, D)

#### Solution 42: Coin Toss Patterns
- Classic Penney's game and Markov chain analysis.
- **Correct Option**: (A, B, C, D)

#### Solution 43: Definite Integral
- Let $I = \int_0^{\pi/2} \frac{x \sin x \cos x}{\sin^4 x + \cos^4 x} dx$.
- Using King's property $x \to \pi/2 - x$: $2I = \frac{\pi}{2} \int_0^{\pi/2} \frac{\sin x \cos x}{\sin^4 x + \cos^4 x} dx$.
- Let $u = \sin^2 x \implies du = 2\sin x \cos x dx$.
- $\int_0^1 \frac{(1/2) du}{u^2 + (1-u)^2} = \frac{1}{2} \int_0^1 \frac{du}{2u^2 - 2u + 1} = \frac{1}{4} \int_0^1 \frac{du}{(u - 1/2)^2 + 1/4} = \frac{\pi}{4}$.
- Thus $2I = \frac{\pi^2}{8} \implies I = \frac{\pi^2}{16}$.
- $\frac{32 I}{\pi^2} = \frac{32 (\pi^2 / 16)}{\pi^2} = 2$.
- **Answer**: 2

#### Solution 44: Constrained Integer Solutions
- Substitute $y_1 = x_1 - 1$, $y_2 = x_2 - 1$, so $y_1 + y_2 + x_3 + x_4 = 18$ with $0 \le y_1 \le 5$, $0 \le y_2 \le 6$, $x_3, x_4 \ge 0$.
- By inclusion-exclusion using generating functions or combinations:
  Total without upper bounds: $\binom{18 + 4 - 1}{4 - 1} = \binom{21}{3} = \frac{21 \times 20 \times 19}{6} = 1330$.
  Violate $y_1 \ge 6$: $\binom{18 - 6 + 3}{3} = \binom{15}{3} = 455$.
  Violate $y_2 \ge 7$: $\binom{18 - 7 + 3}{3} = \binom{14}{3} = 364$.
  Violate both: $\binom{18 - 13 + 3}{3} = \binom{8}{3} = 56$.
  Total valid $= 1330 - 455 - 364 + 56 = 567$.
- **Answer**: 567

#### Solution 45: Family of Planes
- Plane equation: $(x + 2y + 3z - 4) + \lambda(2x + y - z + 5) = 0 \implies (1 + 2\lambda)x + (2 + \lambda)y + (3 - \lambda)z + (-4 + 5\lambda) = 0$.
- Perpendicular to $5x + 3y + 6z + 8 = 0$:
  $5(1 + 2\lambda) + 3(2 + \lambda) + 6(3 - \lambda) = 0 \implies 5 + 10\lambda + 6 + 3\lambda + 18 - 6\lambda = 0 \implies 29 + 7\lambda = 0 \implies \lambda = -29/7$.
- Substituting $\lambda = -29/7$:
  $7(x + 2y + 3z - 4) - 29(2x + y - z + 5) = 0$
  $\implies (7 - 58)x + (14 - 29)y + (21 + 29)z + (-28 - 145) = 0$
  $\implies -51x - 15y + 50z - 173 = 0 \implies 51x + 15y - 50z + 173 = 0$.
- $\gcd(51, 15, -50) = 1$ and $A = 51 > 0$.
- $A + B + C + D = 51 + 15 - 50 + 173 = 189$.
- **Answer**: 189

#### Solution 46: Complex Number Modulus Bounds
- $|z - (3 + 4i)| \le 2$ represents a closed circular disk centered at $z_0 = 3 + 4i$ with radius $R = 2$.
- Distance of center from origin is $|z_0| = \sqrt{3^2 + 4^2} = 5$.
- Maximum $|z| = |z_0| + R = 5 + 2 = 7$.
- Minimum $|z| = |z_0| - R = 5 - 2 = 3$.
- Difference $\Delta = 7 - 3 = 4$.
- **Answer**: 4

#### Solution 47: Polynomial Determinant Coefficient
- Expanding determinant of matrix gives cubic coefficient $K = -4$.
- Magnitude $|K| = 4$.
- **Answer**: 4

#### Solution 48: Poisson Distribution Expectation
- $P(X = 1) = \lambda e^{-\lambda}$, $P(X = 2) = \frac{\lambda^2 e^{-\lambda}}{2}$.
- $\lambda = 2 \frac{\lambda^2}{2} = \lambda^2 \implies \lambda = 1$.
- $E[X^2] = \text{Var}(X) + (E[X])^2 = \lambda + \lambda^2 = 1 + 1 = 2$.
- $100 M = 100 \times 2 = 200$.
- **Answer**: 200

#### Solution 49 to 54:
- 49: Area $= \int_{-1}^1 \left(\frac{2}{1+x^2} - x^2\right)dx = 2[2\arctan(1) - 1/3] = \pi - 2/3$. (A)
- 50: $\sum \frac{n(n-1) + 3n + 1}{n!} = e + 3e + (e - 1) = 5e - 1$. (A)
- 51: For $n=3$, $\det(2A) = 2^3 \det(A) = 24$. $\det(\text{adj}(\text{adj}(M))) = (\det M)^{(n-1)^2} = (\det M)^4 = 24^4 = 3^4 \cdot 2^{12}$. (B)
- 52: For normal to meet again, $t_2 = -t_1 - \frac{2}{t_1}$. $t_2^2 = t_1^2 + \frac{4}{t_1^2} + 4 \ge 2\sqrt{4} + 4 = 8$. (A)
- 53: Riemann sum $\int_0^1 \frac{1}{1 + x^2}dx = \pi/4$. (A)
- 54: By symmetry of Polya's urn, probability remains $3/8$. (A)
