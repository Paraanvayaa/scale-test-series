# Detailed Pedagogical Solutions — Mock Examination 01 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rigid Body Dynamics, Severed Constraint, Torque about Center of Mass, Instantaneous Acceleration.
- **2. Derivation**:
  - Immediately after cutting string at $B$, tension at $A$ is $T$.
  - Equation of motion for CM: $Mg - T = M a_{\text{cm}}$.
  - Torque about CM: $T \frac{L}{2} = I_{\text{cm}} \alpha = \left(\frac{1}{12}ML^2\right)\alpha \implies \alpha = \frac{6T}{ML}$.
  - Kinematic constraint at $A$: string does not stretch instantaneously, so $a_A = a_{\text{cm}} - \alpha \frac{L}{2} = 0$.
  - Thus $a_{\text{cm}} = \alpha \frac{L}{2} = \frac{3T}{M}$.
  - Substitute into translational equation: $Mg - T = M\left(\frac{3T}{M}\right) = 3T \implies 4T = Mg \implies T = \frac{Mg}{4}$. (C) is correct.
  - $a_{\text{cm}} = \frac{3(Mg/4)}{M} = \frac{3g}{4}$. (B) is correct.
  - $\alpha = \frac{6(Mg/4)}{ML} = \frac{3g}{2L}$. (A) is correct.
  - Acceleration of end $B$: $a_B = a_{\text{cm}} + \alpha \frac{L}{2} = \frac{3g}{4} + \frac{3g}{4} = \frac{3g}{2}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Biot-Savart Law, Helmholtz Coil Principle, Axial Magnetic Field.
- **2. Derivation**:
  - For two coaxial coils separated by their radius $R$, the field at midpoint $x = R/2$ is:
    $$B = 2 \times \frac{\mu_0 I R^2}{2(R^2 + (R/2)^2)^{3/2}} = \frac{\mu_0 I R^2}{(5R^2/4)^{3/2}} = \frac{8\mu_0 I}{5\sqrt{5}R}$$
    Statement (A) is correct.
  - By symmetry, $\frac{dB}{dx} = 0$ at midpoint. (B) is correct.
  - In Helmholtz configuration with separation $d = R$, the second derivative $\frac{d^2B}{dx^2}$ also vanishes identically at the midpoint. (C) is correct.
  - Because first and second derivatives are zero, the field is extremely uniform over a broad region around the center. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Geometric Optics, Total Internal Reflection, Prisms.
- **2. Derivation**:
  - $\sin\theta_c = \frac{1}{\mu} = \frac{1}{\sqrt{2}} \implies \theta_c = 45^\circ$. (A) is correct.
  - The ray enters normally at leg 1, strikes hypotenuse at angle of incidence $i = 45^\circ = \theta_c$ (at grazing/TIR threshold). Under strict reflection condition, it reflects at $45^\circ$. (B) is correct.
  - The reflected ray hits the second leg perpendicularly (angle of incidence $0^\circ$), so it emerges undeflected. (C) is correct.
  - Total deviation angle $= 90^\circ$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Capacitors with Multiple Dielectrics in Series, Displacement Vector.
- **2. Derivation**:
  - Two capacitors in series: $C_1 = \frac{K_1 \varepsilon_0 A}{d/2} = \frac{4\varepsilon_0 A}{d}$, $C_2 = \frac{K_2 \varepsilon_0 A}{d/2} = \frac{8\varepsilon_0 A}{d}$.
  - $C_{\text{eq}} = \frac{C_1 C_2}{C_1 + C_2} = \frac{32}{12}\frac{\varepsilon_0 A}{d} = \frac{8\varepsilon_0 A}{3d}$. (A) is correct.
  - Charge $Q$ is same on both: $E_1 = \frac{Q}{K_1 \varepsilon_0 A}, E_2 = \frac{Q}{K_2 \varepsilon_0 A}$. Since $K_2 = 2K_1$, $E_1 = 2E_2$. (B) is correct.
  - Potential drops: $V_1 = E_1(d/2), V_2 = E_2(d/2)$. $V_1 = 2V_2 \implies V_1 = \frac{2}{3}V$. (C) is correct.
  - Bound surface charge density at interface $= P_1 - P_2 = \varepsilon_0(K_1 - 1)E_1 - \varepsilon_0(K_2 - 1)E_2 \ne 0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Bohr Model for Hydrogen-like Ions, Photon Absorption.
- **2. Derivation**:
  - $\Delta E = 13.6 Z^2 \left(1 - \frac{1}{4}\right) = 13.6 Z^2 \times \frac{3}{4} = 10.2 Z^2\text{ eV} = 40.8\text{ eV} \implies Z^2 = 4 \implies Z = 2$ ($\text{He}^+$). (A) is correct.
  - Ionization energy $= 13.6 Z^2 = 13.6(4) = 54.4\text{ eV}$. (B) is correct.
  - $r_n = \frac{n^2}{Z}a_0$. For $n = 2, Z = 2$, $r_2 = \frac{4}{2}a_0 = 2a_0 \ne a_0$. Thus (C) is incorrect.
  - De Broglie wavelength: by Bohr's postulate, $2\pi r_n = n \lambda \implies \lambda = \frac{2\pi(2a_0)}{2} = 2\pi a_0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Wave Mechanics on Stretched Strings, Energy Density and Power.
- **2. Derivation**:
  - Particle velocity $v_p = \frac{\partial y}{\partial t} = -\omega A \cos(kx - \omega t) \implies v_{p,\text{max}} = \omega A$. (A) is correct.
  - Wave velocity $v = \frac{\omega}{k} = \sqrt{\frac{T}{\mu}}$. (B) is correct.
  - Average energy per unit length: $\frac{dE}{dx} = \frac{1}{2}\mu \omega^2 A^2$. (C) is correct.
  - Power: $P = \frac{dE}{dt} = v \frac{dE}{dx} = \frac{1}{2}\mu v \omega^2 A^2$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Maximum kinetic energy equals elastic potential energy at maximum displacement: $K_{\text{max}} = \frac{1}{2}k x_0^2 = \frac{1}{2}(200)(0.10)^2 = 1.00\text{ J}$. Exact: `1.00`.
- **Question 8**: For a soap bubble with two surfaces: $\Delta P = \frac{4S}{R} = \frac{4(0.030)}{0.030} = 4.00\text{ Pa}$. Exact: `4.00`.
- **Question 9**: $\beta = \frac{\lambda D}{d} = \frac{(600 \times 10^{-9}\text{ m})(1.00\text{ m})}{0.20 \times 10^{-3}\text{ m}} = 3.0 \times 10^{-3}\text{ m} = 3.00\text{ mm}$. Exact: `3.00`.
- **Question 10**: Carnot efficiency $\eta_C = 1 - \frac{400}{800} = 0.50$ (50%). Actual efficiency $\eta = \frac{W}{Q_H} = \frac{800}{2000} = 0.40$ (40%). Second-law efficiency $= \frac{0.40}{0.50} = 0.80 = 80.00\%$. Exact: `80.00`.
- **Question 11**: Induced electric field inside solenoid: $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt} \implies E(2\pi r_1) = \pi r_1^2 \mu_0 n \frac{dI}{dt} \implies E = \frac{1}{2}\mu_0 n r_1 \frac{dI}{dt} = \frac{1}{2}(4\pi \times 10^{-7})(800)(0.020)(50.0) = 5.026 \times 10^{-4}\text{ V/m} \approx 0.50\text{ mV/m}$. Exact: `0.50`.
- **Question 12**: $T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{0.0693} = 10.00\text{ days}$. Exact: `10.00`.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: P-1, Q-4, R-2, S-3. Option (A).
- **Question 14**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 15**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 16**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 17**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 18**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS
- **Question 19**: Octahedral splitting: $t_{2g}$ lower, $e_g$ higher. Energy difference is $\Delta_o$. Strong field ligands give low spin. CFSE for low spin $d^6$ ($t_{2g}^6 e_g^0$) is $6(-0.4\Delta_o) + 2P = -2.4\Delta_o + 2P$. Options: (A), (B), (C), (D).
- **Question 20**: Iodoform test requires $\text{CH}_3\text{C=O}$ or $\text{CH}_3\text{CH(OH)}$ group. Ethanol, acetophenone, and propan-2-ol give positive test. Benzaldehyde does not. Options: (A), (B), (C).
- **Question 21**: Adsorption is exothermic ($\Delta H < 0$), decreases randomness ($\Delta S < 0$), spontaneous ($\Delta G < 0$). Physical adsorption decreases with increasing temperature. Options: (A), (B), (C), (D).
- **Question 22**: Pairs of chemically similar compounds with similar intermolecular forces form ideal solutions: Benzene + Toluene, $n$-Hexane + $n$-Heptane, Bromoethane + Chloroethane. Ethanol + Acetone shows positive deviation due to hydrogen bond disruption. Options: (A), (B), (C).
- **Question 23**: Fluorine is the most electronegative element and exhibits only -1 oxidation state. Chlorine has higher electron affinity than fluorine. $\text{Cl}_2$ bond is stronger than $\text{F}_2$ due to lone-pair repulsion in small fluorine. In water, $\text{HI}$ is a much stronger acid than $\text{HF}$ (weak acid). Options: (A), (B), (C).
- **Question 24**: Glucose, fructose, and maltose are reducing sugars (maltose has free hemiacetal group). Sucrose is a non-reducing sugar (glycosidic bond between anomeric carbons). Options: (A), (B), (C).
- **Question 25**: $S = \sqrt{K_{sp}} = \sqrt{1.0 \times 10^{-10}} = 1.0 \times 10^{-5}\text{ mol/L} \implies p = 5$. Exact: `5.00`.
- **Question 26**: $v_{\text{rms}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3(8.314)(300)}{0.032}} = \sqrt{233831.25} \approx 483.56 \approx 484\text{ m/s}$. Exact: `484.00`.
- **Question 27**: $m = \frac{M I t}{n F} = \frac{(63.5)(2.00)(965)}{2(96500)} = \frac{63.5 \times 1930}{193000} = \frac{63.5}{100} = 0.635\text{ g} \approx 0.64\text{ g}$. Exact: `0.64`.
- **Question 28**: $\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) = \frac{57500}{8.314}\left(\frac{10}{300 \times 310}\right) = \frac{575000}{773202} \approx 0.7436 \implies \frac{k_2}{k_1} = e^{0.744} \approx 2.10$. Exact: `2.10`.
- **Question 29**: $[\text{CoF}_6]^{3-}$: $\text{Co}^{3+}$ is $3d^6$. $\text{F}^-$ is a weak field ligand, so high-spin configuration $t_{2g}^4 e_g^2$. Number of unpaired electrons $= 4$. Exact: `4.00`.
- **Question 30**: $\Pi = \frac{w R T}{M V} \implies M = \frac{w R T}{\Pi V} = \frac{(1.50)(0.0821)(300)}{(3.10 \times 10^{-3})(0.100)} = \frac{36.945}{3.10 \times 10^{-4}} \approx 119177\text{ g/mol} \approx 119\text{ kg/mol}$. Exact: `119.00`.
- **Question 31**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 32**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 33**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 34**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 35**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 36**: P-1, Q-2, R-3, S-4. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS
- **Question 37**: $f(0) = 0$. $f'(x) = \cos x - 1 + \frac{x^2}{2} \ge 0$ since $\cos x \ge 1 - \frac{x^2}{2}$. Hence $f(x)$ is strictly increasing for $x > 0$. Therefore $f(x) > 0 \implies \sin x > x - \frac{x^3}{6}$ for $x > 0$. Options: (A), (B), (C), (D).
- **Question 38**: $(A+B)^T = A^T + B^T = A+B$. $(AB)^T = B^T A^T = BA = AB$ iff they commute. $(AB-BA)^T = BA - AB = -(AB-BA)$. $(A^k)^T = (A^T)^k = A^k$. Options: (A), (B), (C), (D).
- **Question 39**: Eccentricity $e = \sqrt{1 + b^2/a^2} > 1$. Asymptotes $y = \pm \frac{b}{a}x$. For rectangular hyperbola $a = b \implies e = \sqrt{2}$. Locus of feet of perpendiculars is the auxiliary circle $x^2 + y^2 = a^2$. Options: (A), (B), (C), (D).
- **Question 40**: $\frac{dy}{y^2} = dx \implies -\frac{1}{y} = x + C$. $y(0) = 1 \implies C = -1 \implies y(x) = \frac{1}{1-x}$. Continuous on $(-\infty, 1)$ and diverges to $+\infty$ as $x \to 1^-$. Options: (A), (B), (C), (D).
- **Question 41**: Vector triple product expansion: $\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c} = \frac{1}{\sqrt{2}}\vec{b} + \frac{1}{\sqrt{2}}\vec{c}$. Since $\vec{b}$ and $\vec{c}$ are non-collinear, equating coefficients gives $\vec{a} \cdot \vec{c} = \frac{1}{\sqrt{2}} \implies \theta = \pi/4$, and $\vec{a} \cdot \vec{b} = -\frac{1}{\sqrt{2}} \implies \theta = 3\pi/4$. Options: (A), (B), (C).
- **Question 42**: Binomial $n = 10, p = 0.5$. Mean $= np = 5$. Variance $= np(1-p) = 2.5$. Symmetric distribution. $P(X=5) = \binom{10}{5}(0.5)^{10} = \frac{252}{1024} = \frac{63}{256}$. Options: (A), (B), (C), (D).
- **Question 43**: $f'(x) = 3x^2 - 6x = 3x(x-2) = 0 \implies x = 0, 2$. Values: $f(0) = 5, f(2) = 8 - 12 + 5 = 1, f(3) = 27 - 27 + 5 = 5$. Absolute maximum is 5. Exact: `5.00`.
- **Question 44**: $x^3 \cos x$ is odd, so its integral from $-2$ to $2$ is 0. $\int_{-2}^2 \sqrt{4-x^2}dx$ represents the area of a semicircle of radius 2: $\frac{1}{2}\pi (2)^2 = 2\pi$. Thus $k = 2$. Exact: `2.00`.
- **Question 45**: Ratio test: $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = \lim_{n \to \infty} \frac{n+1}{3^{n+1}} \frac{3^n}{n} |x| = \frac{|x|}{3} < 1 \implies |x| < 3$. Radius of convergence $R = 3$. Exact: `3.00`.
- **Question 46**: Direction ratios: $\vec{u} = (1, 2, 2)$, $|\vec{u}| = \sqrt{1+4+4} = 3$. $\vec{v} = (2, 1, -2)$, $|\vec{v}| = \sqrt{4+1+4} = 3$. $\vec{u} \cdot \vec{v} = 1(2) + 2(1) + 2(-2) = 2 + 2 - 4 = 0$. Angle is $90^\circ$. Exact: `90.00`.
- **Question 47**: $z + \frac{1}{z} = 2\cos\theta \implies z = e^{i\theta}$. Then $z^3 + \frac{1}{z^3} = 2\cos(3\theta) = 2\cos(3 \times \pi/6) = 2\cos(\pi/2) = 0$. Exact: `0.00`.
- **Question 48**: Divisible by 5 means the last digit must be 5 (1 choice). The first 3 digits can be chosen from the remaining 5 digits $\{1, 2, 3, 4, 6\}$ in $P(5, 3) = 5 \times 4 \times 3 = 60$ ways. Exact: `60.00`.
- **Question 49**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 50**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 51**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 52**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 53**: P-1, Q-2, R-3, S-4. Option (A).
- **Question 54**: P-1, Q-2, R-3, S-4. Option (A).
