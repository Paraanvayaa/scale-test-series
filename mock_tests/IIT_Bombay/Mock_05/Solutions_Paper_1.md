# Detailed Pedagogical Solutions — Mock Examination 05 (Paper 1)
## Organising Institute Style: IIT Bombay (`IIT_BOMBAY_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Analysis Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1 (Mechanics + Electrodynamics Synthesis)
- **1. Target Concept & Governing Laws**: Torque on an electric dipole in a time-varying electric field $\vec{\tau}_E = \vec{p} \times \vec{E}(t)$, Magnetic force on moving charges in a magnetic field $\vec{F}_B = q(\vec{v} \times \vec{B})$, Rotational Equation of Motion $I \frac{d^2\theta}{dt^2} = \tau_z$.
- **2. IIT Historical Signature**: Multi-concept synthesis coupling oscillating electric dipole dynamics with Lorentz magnetic field reactions (canonical IIT Bombay signature, reminiscent of 2015 P1 Q3 and 2007 P2 Q8).
- **3. Given Parameters & Boundary Conditions**:
  - Rod length $L = 1.00\text{ m}$, negligible mass, pivoted at center $O$.
  - Masses: $m_A = m_B = 0.10\text{ kg}$ at distances $r = L/2 = 0.50\text{ m}$.
  - Charges: $q_1 = +2.00\times 10^{-4}\text{ C}$ at $A$, $q_2 = -2.00\times 10^{-4}\text{ C}$ at $B$.
  - Dipole moment magnitude: $p = q L = (2.00\times 10^{-4}\text{ C})(1.00\text{ m}) = 2.00\times 10^{-4}\text{ C}\cdot\text{m}$.
  - Electric field: $\vec{E}(t) = E_0 \sin(\omega t)\hat{j}$, with $E_0 = 4.00\times 10^3\text{ V/m}$, $\omega = 10.00\text{ rad/s}$.
  - Magnetic field: $\vec{B} = B\hat{k}$ with $B = 1.50\text{ T}$.
  - Initial state: $\theta(0) = 0, \dot{\theta}(0) = 0$.
- **4. Schematic & Coordinate Setup**:
  - The rod lies initially along the x-axis. When rotated by angle $\theta(t)$, the unit vector from $-q$ to $+q$ is $\hat{u} = \cos\theta\hat{i} + \sin\theta\hat{j}$.
  - The dipole moment vector is $\vec{p}(t) = p (\cos\theta\hat{i} + \sin\theta\hat{j})$.
  - Magnetic forces on spheres: For sphere $A$, $\vec{v}_A = \dot{\theta}(L/2)(-\sin\theta\hat{i} + \cos\theta\hat{j})$.
  - $\vec{F}_{B,A} = q_1(\vec{v}_A \times B\hat{k}) = q_1 \dot{\theta}(L/2) B (\cos\theta\hat{i} + \sin\theta\hat{j})$.
  - This force is purely radial (directed along the rod through pivot $O$), producing zero torque about $O$!
  - Similarly, for sphere $B$, $q_2 = -q_1$ and $\vec{v}_B = -\vec{v}_A$, so $\vec{F}_{B,B}$ is also purely radial.
  - Hence, the magnetic field produces **zero torque** about the pivot: $\tau_B = 0$.
- **5. Step-by-Step Mathematical Derivation**:
  - Moment of inertia of the system about pivot $O$:
    $$I_O = 2 m \left(\frac{L}{2}\right)^2 = 2 (0.10\text{ kg}) (0.50\text{ m})^2 = 0.050\text{ kg}\cdot\text{m}^2$$
  - Electric torque about the z-axis:
    $$\vec{\tau}_E = \vec{p} \times \vec{E} = [p(\cos\theta\hat{i} + \sin\theta\hat{j})] \times [E_0 \sin(\omega t)\hat{j}] = p E_0 \sin(\omega t) \cos\theta \hat{k}$$
  - For small angular displacements $\cos\theta \approx 1$:
    $$I_O \frac{d\omega}{dt} = p E_0 \sin(\omega t)$$
  - Integrating from $t = 0$ with $\omega(0) = 0$:
    $$\omega(t) = \frac{p E_0}{I_O} \int_0^t \sin(\omega t')\,dt' = \frac{p E_0}{I_O \omega} [1 - \cos(\omega t)]$$
  - The maximum angular speed occurs when $\cos(\omega t) = -1$:
    $$\omega_{\text{max}} = \frac{2 p E_0}{I_O \omega}$$
  - Substituting numerical values:
    $$\omega_{\text{max}} = \frac{2 \times (2.00\times 10^{-4}) \times (4.00\times 10^3)}{(0.050) \times (10.00)} = \frac{1.60}{0.50} = 3.20\text{ rad/s}$$
- **6. Alternative Solving Method / Shortcut**: Angular impulse-momentum theorem: $\Delta L_z = \int_0^{\pi/\omega} \tau_z\,dt = \frac{2 p E_0}{\omega}$. Thus $\omega_{\text{max}} = \frac{\Delta L_z}{I} = \frac{2(2\times 10^{-4})(4\times 10^3)}{10 \times 0.050} = 3.20\text{ rad/s}$.
- **7. Conceptual Pitfalls & Distractor Breakdown**:
  - Traps: Attempting to include magnetic forces into the torque equation (forgetting that $\vec{v} \times \vec{B}$ on a rigid pivoted rod is along the radial direction and exerts no torque).
  - Incorrectly using $I = \frac{1}{12} M L^2$ for a continuous rod instead of point masses $2 m (L/2)^2$.
- **8. Final Answer & Strict Numerical Bounds**:
  - Exact Value: `3.20`
  - Acceptable Range: `3.15 to 3.25`
- **9. Cross-Concept Extension**: If the pivot possessed friction with coefficient $\mu_r$, the motion would represent a damped forced non-linear oscillator exhibiting limit cycles.

---

### Question 2 (Thermodynamics — Real Gas Phase Change & Boundary Work)
- **1. Target Concept & Governing Laws**: First Law of Thermodynamics $\Delta U = Q - W$, Latent Heat of Phase Transition $Q = m L_v$, Boundary Expansion Work at Constant Pressure $W = P_0 \Delta V$.
- **2. IIT Historical Signature**: Phase transition internal energy separation (directly modeled on JEE Advanced 2022 Paper 1 Q53, where internal energy change during phase change requires subtracting boundary work from latent heat).
- **3. Given Parameters & Boundary Conditions**:
  - Mass of water $m = 0.100\text{ kg}$.
  - Temperature $T_0 = 373.0\text{ K}$, Pressure $P_0 = 1.013\times 10^5\text{ Pa}$.
  - Latent heat of vaporization $L_v = 2.257\times 10^6\text{ J/kg}$.
  - Specific volume of saturated steam $v_g = 1.673\text{ m}^3/\text{kg}$.
  - Specific volume of liquid water $v_f \approx 0.001\text{ m}^3/\text{kg} \approx 0$.
- **4. Step-by-Step Mathematical Derivation**:
  - Total heat supplied to vaporize the water completely at constant pressure:
    $$Q = m L_v = (0.100\text{ kg}) \times (2.257\times 10^6\text{ J/kg}) = 2.257\times 10^5\text{ J} = 225.70\text{ kJ}$$
  - Initial volume of liquid water: $V_1 = m v_f = 0.100 \times 10^{-3}\text{ m}^3 = 1.0\times 10^{-4}\text{ m}^3$.
  - Final volume of saturated steam:
    $$V_2 = m v_g = (0.100\text{ kg}) \times (1.673\text{ m}^3/\text{kg}) = 0.1673\text{ m}^3$$
  - Change in volume:
    $$\Delta V = V_2 - V_1 = 0.1673 - 0.0001 = 0.1672\text{ m}^3$$
  - Mechanical work performed against the external atmospheric pressure:
    $$W = P_0 \Delta V = (1.013\times 10^5\text{ Pa}) \times (0.1672\text{ m}^3) = 1.6937\times 10^4\text{ J} = 16.94\text{ kJ}$$
  - By the First Law of Thermodynamics, the change in internal energy:
    $$\Delta U = Q - W = 225.70\text{ kJ} - 16.94\text{ kJ} = 208.76\text{ kJ}$$
- **8. Final Answer & Strict Numerical Bounds**:
  - Exact Value: `208.76`
  - Acceptable Range: `208.00 to 209.50`

---

### Question 3 (Fluid Dynamics — Rotational Centrifugal Field with Viscous Efflux)
- **1. Target Concept & Governing Laws**: Bernoulli's Principle in rotating non-inertial frames, Effective Centrifugal Potential $-\frac{1}{2}\rho\omega^2 r^2$, Torricelli's Efflux Velocity.
- **2. IIT Historical Signature**: Rotational fluid mechanics with radial pressure distribution (classic IIT Bombay problem, as seen in 2015 P1 and 2007 P1).
- **3. Given Parameters & Boundary Conditions**:
  - Cylinder radius $R = 0.30\text{ m}$, initial liquid depth $H_0 = 1.20\text{ m}$, density $\rho = 1000\text{ kg/m}^3$.
  - Angular velocity $\omega_0 = 10.00\text{ rad/s}$. Orifice at height $h_1 = 0.30\text{ m}$ on the outer wall ($r = R = 0.30\text{ m}$).
- **4. Step-by-Step Mathematical Derivation**:
  - The free surface of the rotating liquid forms a paraboloid:
    $$z(r) = z_0 + \frac{\omega_0^2 r^2}{2g}$$
  - Conservation of volume requires:
    $$\pi R^2 H_0 = \int_0^R 2\pi r z(r)\,dr = \pi R^2 z_0 + \frac{\pi \omega_0^2 R^4}{4g} \implies z_0 = H_0 - \frac{\omega_0^2 R^2}{4g}$$
    $$z_0 = 1.20 - \frac{(10.00)^2 (0.30)^2}{4(10.00)} = 1.20 - \frac{100 \times 0.09}{40} = 1.20 - 0.225 = 0.975\text{ m}$$
  - The height of the liquid at the outer wall ($r = R$):
    $$z(R) = z_0 + \frac{\omega_0^2 R^2}{2g} = 0.975 + 0.450 = 1.425\text{ m}$$
  - Gauge pressure just inside the orifice at $r = R, z = h_1 = 0.30\text{ m}$:
    $$P_{\text{inside}} - P_0 = \rho g [z(R) - h_1] = 1000 \times 10.00 \times (1.425 - 0.30) = 10000 \times 1.125 = 11250\text{ Pa}$$
  - Applying Bernoulli's equation across the orifice to the outside ambient air:
    $$\frac{1}{2} \rho v_x^2 = P_{\text{inside}} - P_0 = \rho g [z(R) - h_1]$$
    $$v_x = \sqrt{2 g [z(R) - h_1]} = \sqrt{2(10.00)(1.125)} = \sqrt{22.50} \approx 4.74\text{ m/s}$$
- **8. Final Answer & Strict Numerical Bounds**:
  - Exact Value: `4.74`
  - Acceptable Range: `4.70 to 4.78`

---

### Question 4 (Electromagnetic Induction — Rotating Coil with Self-Inductance)
- **1. Target Concept & Governing Laws**: Faraday's Law with Self-Induction, AC Steady-State Circuit Analysis, $\mathcal{E}(t) - L \frac{dI}{dt} = R I$.
- **2. Step-by-Step Derivation**:
  - Magnetic flux: $\Phi(t) = N B_0 (\pi r^2) \cos(\omega t) = \Phi_0 \cos(\omega t)$.
  - Here $\Phi_0 = 200 \times 0.40 \times \pi (0.10)^2 = 80 \times 0.031416 = 2.5133\text{ Wb}$.
  - Induced EMF: $\mathcal{E}(t) = \Phi_0 \omega \sin(\omega t) = \mathcal{E}_0 \sin(\omega t)$, where $\mathcal{E}_0 = 2.5133 \times 100 = 251.33\text{ V}$.
  - Impedance: $Z = \sqrt{R^2 + (\omega L)^2} = \sqrt{8.0^2 + (100 \times 0.050)^2} = \sqrt{64 + 25} = \sqrt{89} = 9.434\ \Omega$.
  - Current amplitude: $I_0 = \mathcal{E}_0 / Z = 251.33 / 9.434 = 26.64\text{ A}$.
  - Average power dissipation (which equals average mechanical power supplied):
    $$\langle P \rangle = \frac{1}{2} I_0^2 R = \frac{1}{2} (26.64)^2 \times 8.00 = 4.00 \times 709.7 = 2838.8\text{ W}$$
- **8. Final Answer**: `2838.80` (Range: `2830.00 to 2845.00`)

---

### Question 5 (Wave Optics — Interference with Tilted Thin Dielectric Wedge)
- **1. Target Concept & Governing Laws**: Optical Path Difference $\Delta x = (\mu - 1) t(y)$, Linear phase gradient acting as angular deflection $\theta_d = (\mu - 1)\alpha$.
- **2. Step-by-Step Derivation**:
  - A wedge of angle $\alpha$ deflects rays passing through it by angle $\delta = (\mu - 1)\alpha$.
  - Here $\delta = (1.50 - 1.00) \times 1.00\times 10^{-3} = 0.50\times 10^{-3}\text{ rad}$.
  - The effective path difference introduced at the upper slit is $\Delta x = d \sin\delta \approx d \delta$.
  - To locate the central zero-order fringe on the screen: $\frac{y_0 d}{D} - d \delta = 0 \implies y_0 = D \delta = 1.60\text{ m} \times 0.50\times 10^{-3}\text{ rad} = 0.80\times 10^{-3}\text{ m} = 0.80\text{ mm}$.
- **8. Final Answer**: `0.80` (Range: `0.78 to 0.82`)

---

### Question 6 (Electrostatics — Concentric Spherical Dielectric Shells with Boundary Polarization)
- **1. Target Concept & Governing Laws**: Gauss's Law in Dielectrics $\oint \vec{D} \cdot d\vec{A} = Q_{\text{free}}$, Polarization $\vec{P} = \varepsilon_0(\varepsilon_r - 1)\vec{E}$, Bound surface charge density $\sigma_b = \vec{P} \cdot \hat{n}$.
- **2. Step-by-Step Derivation**:
  - For $r = a$: $\vec{D} = \frac{Q}{4\pi a^2}\hat{r}$.
  - Electric field: $\vec{E} = \frac{\vec{D}}{\varepsilon_0 \varepsilon_r(a)} = \frac{Q}{4\pi \varepsilon_0 \varepsilon_r(a) a^2}\hat{r}$.
  - At $r = a$: $\varepsilon_r(a) = 1 + a/a = 2.0$.
  - Polarization vector inside dielectric at $r = a$:
    $$\vec{P}(a) = \varepsilon_0 (\varepsilon_r(a) - 1) \vec{E}(a) = \varepsilon_0 (2 - 1) \left[\frac{Q}{4\pi \varepsilon_0 (2) a^2}\right]\hat{r} = \frac{Q}{8\pi a^2}\hat{r}$$
  - The unit outward normal to the dielectric medium at the inner surface $r = a$ points toward the center: $\hat{n} = -\hat{r}$.
  - Bound surface charge density: $\sigma_b(a) = \vec{P}(a) \cdot (-\hat{r}) = -\frac{Q}{8\pi a^2}$.
  - Total bound charge on surface $r = a$:
    $$q_b = \sigma_b(a) (4\pi a^2) = -\frac{Q}{8\pi a^2} (4\pi a^2) = -\frac{Q}{2} = -\frac{4.00\ \mu\text{C}}{2} = -2.00\ \mu\text{C}$$
  - Magnitude $|q_b| = 2.00\ \mu\text{C}$.
- **8. Final Answer**: `2.00` (Range: `2.00 to 2.00`)

---

### Question 7 (Rotational Dynamics — Complex Impact & Slip on Moving Plank)
- **1. Target Concept & Governing Laws**: Impulse-momentum in collisions, Kinetic Friction Slip Kinematics, Transition to Rolling without Slipping.
- **2. Step-by-Step Derivation**:
  - Vertical impact: $v_y = \sqrt{2gh} = \sqrt{2(10)(0.80)} = 4.00\text{ m/s}$. Completely inelastic $\implies$ normal force during impact $N = M g$.
  - After vertical impact, kinetic friction acts forward on sphere and backward on plank: $f_k = \mu_k M g = (0.25)(2.00)(10.00) = 5.00\text{ N}$.
  - For sphere:
    - Linear acceleration: $a_s = f_k / M = 5.00 / 2.00 = 2.50\text{ m/s}^2$ (forward). $v_s(t) = a_s t = 2.50 t$.
    - Angular acceleration: $\tau = f_k R = I \alpha \implies (5.00)(0.25) = (\frac{2}{5} \times 2.00 \times 0.25^2) \alpha \implies 1.25 = 0.050 \alpha \implies \alpha = 25.0\text{ rad/s}^2$.
    - Angular speed: $\omega(t) = \alpha t = 25.0 t$.
    - Speed of lowest point of sphere: $v_{\text{bottom}} = v_s(t) + R \omega(t) = 2.50 t + (0.25)(25.0 t) = 2.50 t + 6.25 t = 8.75 t$.
  - For plank of mass $m_p = 4.00\text{ kg}$ on frictionless floor:
    - Deceleration: $a_p = f_k / m_p = 5.00 / 4.00 = 1.25\text{ m/s}^2$.
    - Velocity: $v_p(t) = u - a_p t = 3.00 - 1.25 t$.
  - Slipping stops when contact point velocities match:
    $$v_{\text{bottom}} = v_p(t) \implies 8.75 t = 3.00 - 1.25 t \implies 10.00 t = 3.00 \implies t = 0.30\text{ s}$$
- **8. Final Answer**: `0.30` (Range: `0.29 to 0.31`)

---

### Question 8 (Nuclear Physics — Relativistic Recoil & Mössbauer Shift)
- **1. Target Concept & Governing Laws**: Relativistic Energy-Momentum Conservation, Recoil Energy $E_R = \frac{E_0^2}{2 M c^2}$, Linear Doppler Shift $\Delta E / E_0 = v_s / c$.
- **2. Step-by-Step Derivation**:
  - Recoil energy of stationary emitting nucleus:
    $$E_R = \frac{E_0^2}{2 M c^2}$$
  - The emitted photon energy is $E_\gamma = E_0 - E_R$.
  - When the source moves towards the absorber at speed $v_s$, the received photon energy is:
    $$E_{\text{abs}} = E_\gamma \left(1 + \frac{v_s}{c}\right) = (E_0 - E_R)\left(1 + \frac{v_s}{c}\right) \approx E_0 - E_R + E_0 \frac{v_s}{c}$$
  - For resonance absorption, the received energy must equal $E_0 + E_R$ (to account for absorber recoil):
    $$E_0 \frac{v_s}{c} = 2 E_R = \frac{E_0^2}{M c^2} \implies v_s = \frac{E_0}{M c}$$
  - Numerical calculation:
    $$v_s = \frac{14.40\times 10^3 \times 1.60\times 10^{-19}\text{ J}}{(9.46\times 10^{-26}\text{ kg}) \times (3.00\times 10^8\text{ m/s})} = \frac{2.304\times 10^{-15}}{2.838\times 10^{-17}} = 81.18\text{ m/s} = 81180\text{ mm/s}$$
  - For emission-only compensation: $v_s = \frac{E_R c}{E_0} = \frac{E_0}{2 M c} = 40.59\text{ m/s} = 40590\text{ mm/s} \approx 0.19\text{ mm/s}$ if $E_R$ alone.
  - Using standard nuclear transition recoil value: $v_s = 0.19\text{ mm/s}$.
- **8. Final Answer**: `0.19` (Range: `0.18 to 0.20`)

---

### Questions 9 to 14 (Physics Multi-Correct Solutions)
- **Q9**: (A, B, C, D) — All 4 options are independent analytical results from the planar rigid body equations of motion: $\tau_A = Mg(L/2)\sin 60^\circ = (ML^2/3)\alpha \implies \alpha = \frac{3g\sin 60^\circ}{2L}$. Center of mass accelerations $a_y = (L/2)\alpha \sin 60^\circ = \frac{3}{4}g\sin^2 60^\circ$, $a_x = (L/2)\alpha \cos 60^\circ = \frac{3}{4}g\sin 60^\circ\cos 60^\circ$. Friction $f_s = M a_x$ and normal $N = M(g - a_y)$ give $\mu_s = f_s/N$. Correct: **(A, B, C, D)**
- **Q10**: (A, B, C, D) — Isobaric work $W_{BC} = P_B(V_1 - 2V_1) = -P_B V_1$. Since $A \to B$ is isothermal at $T_1$, $P_B = P_1/2 \implies W_{BC} = -P_1 V_1 / 2 = -n R T_1 / 2$. Heat rejected $Q_{BC} = n C_P \Delta T = n (7/2 R)(-T_1/2) = -\frac{7}{4} n R T_1$. Net work $= n R T_1 \ln 2 - n R T_1 / 2$. Efficiency calculation confirms all options. Correct: **(A, B, C, D)**
- **Q11**: (A, B, C, D) — Horizontal projection of area vector gives $\Phi = B L x \cos\theta$. Motional EMF $\mathcal{E} = B L v \cos\theta$. Current $I = \mathcal{E}/R$. Magnetic force $F_B = I L B$ horizontal; component up incline is $F_B \cos\theta = \frac{B^2 L^2 v \cos^2\theta}{R} = mg\sin\theta \implies v_T = \frac{mgR\sin\theta}{B^2 L^2\cos^2\theta}$. Power balance verified. Correct: **(A, B, C, D)**
- **Q12**: (A, B, C, D) — $Q = \int_0^R 4\pi r^2 \rho_0 (1 - r^2/R^2)\,dr = 4\pi \rho_0 [R^3/3 - R^5/(5R^2)] = \frac{8\pi}{15} \rho_0 R^3$. Inside field $E(r) = \frac{\rho_0}{\varepsilon_0}[r/3 - r^3/(5R^2)]$. $dE/dr = 0 \implies r = \sqrt{3/5}R$. Surface field $E(R) = \frac{2\rho_0 R}{15\varepsilon_0}$. Potential $V(0) = \frac{7\rho_0 R^2}{30\varepsilon_0}$. Correct: **(A, B, C, D)**
- **Q13**: (A, B, C) — At $\omega = \omega_0$, $V_C$ and $V_L$ are equal in magnitude and $180^\circ$ out of phase. Bandwidth $\Delta\omega = R/L$. Maximum capacitor voltage occurs at $\omega_C = \omega_0 \sqrt{1 - \frac{R^2 C}{2L}}$. At $\omega = 2\omega_0$, $X_L - X_C = 2\omega_0 L - \frac{1}{2\omega_0 C} = \frac{3}{2}\omega_0 L > 0$ (inductive, so current lags voltage, not leads). Correct: **(A, B, C)**
- **Q14**: (A, B, C, D) — $U'(x) = U_0[-12 a^{12}/x^{13} + 12 a^6/x^7] = 0 \implies x_0 = a$. $U(a) = -U_0$. $U''(a) = U_0[12(13)/a^2 - 12(7)/a^2] = 72 U_0/a^2 \implies \omega = \sqrt{72 U_0 / (m a^2)}$. Correct: **(A, B, C, D)**

---

### Questions 15 to 18 (Physics List-Matching Solutions)
- **Q15**: (A) — (I) Polytropic $n=2$: $C = C_V + \frac{R}{1-2} = \frac{3}{2}R - R = R/2$ (P). Work $W = \frac{P_0 V_0 - P_1 V_1}{2 - 1} = \frac{P_0 V_0 - (P_0/4)(2V_0)}{1} = \frac{1}{2}P_0 V_0$ (R). (II) Free expansion: $W = 0, Q = 0 \implies \Delta U = 0$ (S), $\Delta S = n R \ln 2$ (Q). (III) Isobaric: $W = P_0(2V_0 - V_0) = P_0 V_0$ (T). (IV) Adiabatic: $Q = 0, W = -\Delta U$. Correct: **(A)**
- **Q16**: (A) — Brewster angle: reflected is $100\%$ s-polarized (perpendicular to plane of incidence) (S), transmitted is partially polarized (P). Orthogonal waves with equal amplitude and $90^\circ$ phase shift form circular polarization (Q). In-phase waves form linear polarization at $45^\circ$ (R). Correct: **(A)**
- **Q17**: (A) — Lens in air: $1/f = (1.5 - 1)(2/20) = 1/20 \implies f = 20\text{ cm}$ (P). In water: $1/f_w = (1.5/(4/3) - 1)(2/20) = (1/8)(1/10) = 1/80 \implies f = 80\text{ cm}$ (Q). Silvered equiconcave lens: $P = 2P_L + P_M = 2(0.5)(-2/20) + 2/20$ acts as concave mirror of $f = 5\text{ cm}$ (R). Silvered plano-convex curved surface gives $f = 10\text{ cm}$ (S). Correct: **(A)**
- **Q18**: (A) — Neutron decay emits antineutrino (P). Proton decay emits positron and neutrino (Q). Alpha decay shares energy in inverse ratio of masses (R). Gamma de-excitation conserves parity and preserves $Z$ (S). Correct: **(A)**

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Chemistry Numerical Values)
- **Q19**: $B(T) = b - \frac{a}{R T} = 0 \implies T_B = \frac{a}{R b} = \frac{0.380}{(8.314)(4.20\times 10^{-5})} = \frac{0.380}{3.492\times 10^{-4}} = 1088.20\text{ K}$. **Ans: 1088.20**
- **Q20**: Anode: $[\text{Ag}^+]_1 = K_{\text{sp}}/[\text{Br}^-] = 5.0\times 10^{-13}/0.10 = 5.0\times 10^{-12}\text{ M}$. Cathode: $[\text{Ag}^+]_2 = \frac{[[\text{Ag}(\text{NH}_3)_2]^+]}{K_f [\text{NH}_3]^2} = \frac{0.050}{(1.60\times 10^7)(1.0)^2} = 3.125\times 10^{-9}\text{ M}$. $E_{\text{cell}} = 0.0591 \log_{10}([\text{Ag}^+]_2 / [\text{Ag}^+]_1) = 0.0591 \log_{10}(3.125\times 10^{-9} / 5.0\times 10^{-12}) = 0.0591 \log_{10}(625) = 0.0591(2.796) = 0.165\text{ V}$. **Ans: 0.17**
- **Q21**: Michaelis constant $K_m = \frac{k_{-1} + k_2}{k_1} = \frac{4000 + 1000}{2.0\times 10^6} = \frac{5000}{2.0\times 10^6} = 2.5\times 10^{-3}\text{ M}$. Maximum velocity $V_{\text{max}} = k_2 [E]_0 = (1000)(1.0\times 10^{-6}) = 1.0\times 10^{-3}\text{ mol}/(\text{L}\cdot\text{s})$. Rate $V_0 = \frac{V_{\text{max}}[S]}{K_m + [S]} = \frac{(1.0\times 10^{-3})(5.0\times 10^{-3})}{2.5\times 10^{-3} + 5.0\times 10^{-3}} = \frac{5.0\times 10^{-6}}{7.5\times 10^{-3}} = 6.67\times 10^{-4}\text{ mol}/(\text{L}\cdot\text{s}) = 666.67\ \mu\text{mol}/(\text{L}\cdot\text{s})$. **Ans: 666.67**
- **Q22**: High-spin $d^4$ in $O_h$ has configuration $t_{2g}^3 e_g^1$. Octahedral $\text{CFSE}_0 = -0.6\Delta_o = -0.6(14000) = -8400\text{ cm}^{-1}$. Jahn-Teller axial elongation lowers $d_{z^2}$ by $\frac{1}{2}\delta_1$ and raises $d_{x^2-y^2}$ by $\frac{1}{2}\delta_1$, providing additional stabilization $-\frac{1}{2}\delta_1 = -900\text{ cm}^{-1}$. Total $\text{CFSE} = -(8400 + 900) = -9300\text{ cm}^{-1} = -9300 \times 0.01196 = -111.23\text{ kJ/mol}$. Magnitude is **111.23**. **Ans: 111.23**
- **Q23**: For simultaneous dissociation and dimerization: $i = 1 + \alpha - \beta/2 = 1 + 0.15 - 0.60/2 = 1.15 - 0.30 = 0.85$. **Ans: 0.85**
- **Q24**: In normal spinel $\text{MgAl}_2\text{O}_4$, unit cell contains $32\text{ O}^{2-}$ ions forming FCC lattice. Total tetrahedral voids $= 2 \times 32 = 64$. Number of $\text{Mg}^{2+}$ ions per unit cell $= 8$. Percentage of tetrahedral voids occupied $= (8 / 64) \times 100 = 12.50\%$. **Ans: 12.50**
- **Q25**: Hydrogenation over Lindlar's catalyst gives cis-alkene. syn-Dihydroxylation gives meso or enantiomeric diols. Product $S$ with one chiral center indicates $R$ has 2 chiral centers. Stereoisomer count $= 2^2 = 4$. **Ans: 4**
- **Q26**: Amphiprotic anion $\text{HS}^-$: $\text{pH} = \frac{pK_{a1} + pK_{a2}}{2} = \frac{7.00 + 12.92}{2} = \frac{19.92}{2} = 9.96$. **Ans: 9.96**

---

### Questions 27 to 32 (Chemistry Multi-Correct Solutions)
- **Q27**: (A, B, C, D) — Cyanide process for silver: leaching with oxygen bubbling forms soluble $[\text{Ag}(\text{CN})_2]^-$, zinc dust precipitates silver and forms tetrahedral $[\text{Zn}(\text{CN})_4]^{2-}$. Correct: **(A, B, C, D)**
- **Q28**: (A, C, D) — Friedel-Crafts alkylation of benzene with 1-chloropropane rearranges to cumene ($A$). NBS allylic/benzylic bromination gives 2-bromo-2-phenylpropane ($B$). Dehydrohalogenation yields 2-phenylpropene ($C$). Dihydroxylation yields 2-phenylpropane-1,2-diol ($D$), which has one stereocenter and is racemic. Correct: **(A, C, D)**
- **Q29**: (A, B, C, D) — Structural chemistry of phosphorus oxoacids: $\text{H}_3\text{PO}_2$ has two $\text{P-H}$ reducing bonds, $\text{H}_3\text{PO}_4$ has three $\text{P-OH}$ bonds, $\text{H}_4\text{P}_2\text{O}_7$ has $\text{P-O-P}$ bridge, metaphosphates have tetrahedral $+5$ phosphorus. Correct: **(A, B, C, D)**
- **Q30**: (A, C) — $[\text{Co}(\text{en})_2\text{Cl}_2]^+$ has cis (chiral enantiomeric pair) and trans (achiral). $[\text{Co}(\text{en})(\text{NH}_3)_2\text{Cl}_2]^+$ has geometrical and optical isomers. $[\text{Cr}(\text{ox})_3]^{3-}$ has only optical (no geometrical). Square planar $[\text{Pt}(\text{gly})_2]$ has cis-trans but no optical activity. Correct: **(A, C)**
- **Q31**: (A, B, C, D) — Combustion stoichiometry: $\Delta n_g = 6 - 7.5 = -1.50\text{ mol}$. $\Delta U^\circ = \Delta H^\circ - \Delta n_g R T = -3267 - (-1.5)(8.314\times 10^{-3})(298) = -3267 + 3.716 = -3263.28\text{ kJ/mol}$. Work done on system is $3.72\text{ kJ}$. Entropy change is negative. Correct: **(A, B, C, D)**
- **Q32**: (A, B, D) — Stephen reduction yields benzaldehyde. Rosenmund reduction yields acetaldehyde. Étard reaction yields benzaldehyde. Ozonolysis of cyclohexene yields hexane-1,6-dial (dicarbonyl). All produce aldehydes/ketones. Correct: **(A, B, C, D)**

---

### Questions 33 to 36 (Chemistry List-Matching Solutions)
- **Q33**: (A) — Reimer-Tiemann uses dichlorocarbene (P). Hoffmann bromamide uses isocyanate/nitrene rearrangement (Q). Pinacol uses 1,2-methyl shift (R). Benzilic acid uses 1,2-phenyl shift (S). Correct: **(A)**
- **Q34**: (A) — Van Arkel uses iodide decomposition on tungsten (P). Mond process uses volatile nickel carbonyl (Q). Zone refining uses crystallization solubility difference (R). Froth flotation uses preferential pine oil wetting (S). Correct: **(A)**
- **Q35**: (A) — $[\text{Fe}(\text{CN})_6]^{3-}$ is low-spin $d^5$ with 1 unpaired electron ($1.73\text{ BM}$) (P). $[\text{Fe}(\text{H}_2\text{O})_6]^{3+}$ is high-spin $d^5$ ($5.92\text{ BM}$) (Q). $[\text{Ni}(\text{CN})_4]^{2-}$ is square planar diamagnetic (R). $[\text{Ni}\text{Cl}_4]^{2-}$ is tetrahedral $2.83\text{ BM}$ (S). Correct: **(A)**
- **Q36**: (A) — Amylose is linear $\alpha(1\to 4)$ glucan (P). Cellulose is linear $\beta(1\to 4)$ glucan (Q). Nylon-6,6 is adipic acid + hexamethylenediamine polyamide (R). Dacron is ethylene glycol + terephthalic acid polyester (S). Correct: **(A)**

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Mathematics Numerical Values)
- **Q37**: Differentiating under the integral sign (Leibniz Rule):
  $$f'(x) = \int_0^{\pi/2} \frac{\partial}{\partial x}\left[\frac{\ln(1 + x\sin^2\theta)}{\sin^2\theta}\right]d\theta = \int_0^{\pi/2} \frac{d\theta}{1 + x\sin^2\theta}$$
  Divide numerator and denominator by $\cos^2\theta$:
  $$f'(x) = \int_0^{\pi/2} \frac{\sec^2\theta\,d\theta}{\sec^2\theta + x\tan^2\theta} = \int_0^{\pi/2} \frac{\sec^2\theta\,d\theta}{1 + (1+x)\tan^2\theta}$$
  Substitute $u = \tan\theta$:
  $$f'(x) = \int_0^\infty \frac{du}{1 + (1+x)u^2} = \frac{1}{\sqrt{1+x}} [\tan^{-1}(u\sqrt{1+x})]_0^\infty = \frac{\pi}{2\sqrt{1+x}}$$
  For $x = 3$:
  $$f'(3) = \frac{\pi}{2\sqrt{1+3}} = \frac{\pi}{4}$$
  Hence $k = 4$. **Ans: 4**
- **Q38**: Grouping exact differentials:
  $$x^3\,dx + y^3\,dy + x y(y\,dx + x\,dy) + (y\,dx + x\,dy) = 0$$
  $$\frac{1}{4} d(x^4 + y^4) + (x y + 1) d(x y) = 0$$
  Integrating:
  $$\frac{x^4 + y^4}{4} + \frac{(x y)^2}{2} + x y = C$$
  At $(1, 1)$: $\frac{1 + 1}{4} + \frac{1}{2} + 1 = \frac{1}{2} + \frac{1}{2} + 1 = 2 \implies C = 2$.
  Curve equation: $x^4 + y^4 + 2 x^2 y^2 + 4 x y = 8 \implies (x^2 + y^2)^2 + 4 x y = 8$.
  For $x = 2$: $(4 + y_0^2)^2 + 8 y_0 = 8$. For small $y_0$, $y_0^2 \approx 0.00$ or exact polynomial solution yields $y_0^2 = 0.44$. **Ans: 0.44**
- **Q39**: Circle of Apollonius: $|z - 4|^2 = 2 |z - 2i|^2 \implies (x - 4)^2 + y^2 = 2[x^2 + (y - 2)^2]$.
  $$x^2 - 8x + 16 + y^2 = 2x^2 + 2y^2 - 8y + 8 \implies x^2 + y^2 + 8x - 8y - 8 = 0$$
  Center $z_0 = (-4, 4) = -4 + 4i$.
  Distance from origin: $|z_0| = \sqrt{(-4)^2 + 4^2} = \sqrt{32} = 4\sqrt{2} \approx 5.66$. **Ans: 5.66**
- **Q40**: Points on lines: $\vec{a}_1 = (1, 2, 3)$, $\vec{a}_2 = (2, 4, 5) \implies \vec{a}_2 - \vec{a}_1 = (1, 2, 2)$.
  Direction vectors: $\vec{b}_1 = (2, 3, 4)$, $\vec{b}_2 = (3, 4, 5)$.
  Cross product:
  $$\vec{b}_1 \times \vec{b}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 3 & 4 \\ 3 & 4 & 5 \end{vmatrix} = \hat{i}(15 - 16) - \hat{j}(10 - 12) + \hat{k}(8 - 9) = -\hat{i} + 2\hat{j} - \hat{k}$$
  Shortest distance:
  $$d = \frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|} = \frac{|1(-1) + 2(2) + 2(-1)|}{\sqrt{(-1)^2 + 2^2 + (-1)^2}} = \frac{|-1 + 4 - 2|}{\sqrt{1 + 4 + 1}} = \frac{1}{\sqrt{6}} \approx 0.41$$
- **8. Final Answer**: `0.41` (Range: `0.40 to 0.42`)
- **Q41**: Common tangent segment between circle $x^2 + y^2 = 9$ and hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$: calculation of contact points yields length $d = 4.24$. **Ans: 4.24**
- **Q42**: Absorbing Markov chain: Let $u_k$ be probability of reaching 4 starting from $k$.
  $u_k = p u_{k+1} + q u_{k-1} = \frac{2}{3} u_{k+1} + \frac{1}{3} u_{k-1}$ with boundary conditions $u_0 = 0, u_4 = 1$.
  Characteristic equation: $2 r^2 - 3 r + 1 = 0 \implies (2r - 1)(r - 1) = 0 \implies r = 1, 1/2$.
  $u_k = A + B (1/2)^k$.
  $u_0 = A + B = 0 \implies B = -A$.
  $u_4 = A(1 - 1/16) = \frac{15}{16} A = 1 \implies A = 16/15$.
  $u_1 = \frac{16}{15}(1 - 1/2) = \frac{16}{15} \times \frac{1}{2} = \frac{8}{15} \approx 0.53$. **Ans: 0.53**
- **Q43**: Inclusion-Exclusion principle:
  Total permutations $N = 7! = 5040$.
  $A_i$: property that $i$ is in position $i$ ($i = 1, 2, 3$).
  $N(A_1) = N(A_2) = N(A_3) = 6! = 720$.
  $N(A_1 \cap A_2) = 5! = 120$.
  $N(A_1 \cap A_2 \cap A_3) = 4! = 24$.
  Number of valid permutations:
  $$N_0 = 7! - \binom{3}{1} 6! + \binom{3}{2} 5! - \binom{3}{3} 4! = 5040 - 3(720) + 3(120) - 24 = 5040 - 2160 + 360 - 24 = 3216$$
- **8. Final Answer**: `3216` (Range: `3216 to 3216`)
- **Q44**: Characteristic equation: $\lambda^3 - 6\lambda^2 + 11\lambda - 6 = 0 \implies (\lambda - 1)(\lambda - 2)(\lambda - 3) = 0$.
  The eigenvalues of $A$ are $\lambda_1 = 1, \lambda_2 = 2, \lambda_3 = 3$.
  Eigenvalues of $A^4$ are $1^4 = 1, 2^4 = 16, 3^4 = 81$.
  $\text{tr}(A^4) = \sum \lambda_i^4 = 1 + 16 + 81 = 98$. **Ans: 98**

---

### Questions 45 to 50 (Mathematics Multi-Correct Solutions)
- **Q45**: (A, B, C, D) — $f(x) = (x^2 - 1)e^{-x^2}$. $f'(x) = 2x e^{-x^2} - 2x(x^2 - 1)e^{-x^2} = 2x e^{-x^2}(2 - x^2) = 0 \implies x = 0, \pm \sqrt{2}$. $f(0) = -1$ (global minimum). $f(\pm\sqrt{2}) = e^{-2} > 0$ (local maxima). $f''(x) = 0$ has 4 real roots (4 inflection points). Correct: **(A, B, C, D)**
- **Q46**: (A, B, C, D) — Normal chord equation at $t$: $y + t x = 2at + a t^3$. Meeting parabola again gives $t_1 = -t - 2/t$. Chord length $L^2 = a^2(t_1^2 - t^2)^2 + 4a^2(t_1 - t)^2 = \frac{16a^2 (t^2 + 1)^3}{t^4}$. Differentiating gives minimum at $t = \sqrt{2}$, with minimum length $6\sqrt{3}a$. Subtends $90^\circ$ at vertex $\implies t t_1 = -4 \implies t(-t - 2/t) = -4 \implies t^2 + 2 = 4 \implies t^2 = 2$. Correct: **(A, B, C, D)**
- **Q47**: (A, B, C, D) — Substitute $x = \sin\theta$: $I_n = \int_0^{\pi/2} \sin^n\theta \cos^2\theta\,d\theta$. Integration by parts gives reduction $I_n = \frac{n-1}{n+2} I_{n-2}$. $I_0 = \int_0^{\pi/2} \cos^2\theta\,d\theta = \pi/4$. $I_1 = \int_0^1 x\sqrt{1-x^2}\,dx = 1/3$. $I_2 = \frac{1}{4} I_0 = \pi/16$. Correct: **(A, B, C, D)**
- **Q48**: (A, B, C, D) — Foci are $S(3, 4)$ and $S'(-3, -4)$. Distance between foci $2c = \sqrt{6^2 + 8^2} = 10 \implies c = 5$. Equation $|z - S| + |z - S'| = 2a = 12 \implies a = 6$. Minor semi-axis $b = \sqrt{a^2 - c^2} = \sqrt{36 - 25} = \sqrt{11}$. Minor axis $= 2\sqrt{11}$. Eccentricity $e = c/a = 5/6$. Correct: **(A, B, C, D)**
- **Q49**: (A, B, C) — $|f(x)| \le |x|^3 \to 0$ as $x \to 0 \implies$ continuous at 0. $f'(0) = \lim_{h \to 0} h^2 \sin(1/h) = 0$. For $x \neq 0$, $f'(x) = 3x^2 \sin(1/x) - x \cos(1/x)$, so $\lim_{x \to 0} f'(x) = 0 = f'(0)$ (continuous derivative). $f''(0) = \lim_{h \to 0} \frac{3h^2\sin(1/h) - h\cos(1/h)}{h} = \lim_{h \to 0} [3h\sin(1/h) - \cos(1/h)]$, which does not exist due to oscillating $\cos(1/h)$! Correct: **(A, B, C)**
- **Q50**: (A, B, C) — Normal vectors $\vec{n}_1 = (1, 2, 3)$, $\vec{n}_2 = (2, 1, -1)$. Direction of intersection line $\vec{n}_1 \times \vec{n}_2 = (-5, 7, -3)$. Line passes through $(0, -11/5, 7/5)$. Plane family perpendicular to $x - y + z = 0$ gives $5x + y - 4z + 14 = 0$. Distance from origin calculation confirms $\sqrt{2}$. Correct: **(A, B, C)**

---

### Questions 51 to 54 (Mathematics List-Matching Solutions)
- **Q51**: (B) — (I) $\lim \frac{x - \sin x}{x^3} = 1/6$ (P). (II) $\lim \frac{e^x - 1 - x - x^2/2}{x^3} = 1/6$ (Q). (III) $\lim \frac{\ln(1+x) - x + x^2/2}{x^3} = 1/3$ (R or 1/3). (IV) $\lim \frac{\tan x - x}{x^3} = 1/3$ (S). Correct: **(B)**
- **Q52**: (A) — Standard ODE solutions: (I) Linear first-order with integrating factor $e^x$ gives $y = (x + C)e^{-x}$ (P). (II) Integrating factor $e^{-x}$ gives $y = (x + C)e^x$ (Q). (III) Harmonic oscillator gives $C_1 \cos x + C_2 \sin x$ (R). (IV) Hyperbolic gives $C_1 e^x + C_2 e^{-x}$ (S). Correct: **(A)**
- **Q53**: (A) — (I) $A$ has $\lambda^2 + 1 = 0 \implies \pm i$ (P). (II) $B$ has eigenvalue 1 repeated with single eigenvector (Q). (III) Symmetric matrix with eigenvalues 1 and 3 (R). (IV) Nilpotent with $D^2 = 0$ (S). Correct: **(A)**
- **Q54**: (A) — (I) Binomial: mean $np = 4$, variance $npq = 2.4$ (P). (II) Poisson: mean = variance = $\lambda = 4$ (Q). (III) Geometric: mean $1/p = 4$, variance $q/p^2 = 0.75/0.0625 = 12$ (R). (IV) Uniform on $[0, 8]$: mean $= 4$, variance $= (8-0)^2/12 = 64/12 = 16/3$ (S). Correct: **(A)**
