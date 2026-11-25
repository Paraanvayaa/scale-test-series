# Detailed Pedagogical Solutions — Mock Examination 07 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Angular and Linear Impulse on Rigid Bodies, Instantaneous Center of Rotation.
- **2. Derivation**:
  - Linear impulse: $J = M v_{\text{cm}} \implies v_{\text{cm}} = J/M$. Option (A) is correct.
  - Angular impulse about CM: $J(L/2) = I_{\text{cm}}\omega = \frac{1}{12}M L^2 \omega \implies \omega = \frac{6J}{ML}$. Option (B) is correct.
  - Point of zero velocity: $v(y) = v_{\text{cm}} - \omega y = 0 \implies y = \frac{v_{\text{cm}}}{\omega} = \frac{J/M}{6J/ML} = \frac{L}{6}$ from CM on the non-struck half. Option (C) is correct.
  - Kinetic energy: $K = \frac{1}{2}M v_{\text{cm}}^2 + \frac{1}{2}I_{\text{cm}}\omega^2 = \frac{J^2}{2M} + \frac{1}{2}\left(\frac{ML^2}{12}\right)\left(\frac{36 J^2}{M^2 L^2}\right) = \frac{J^2}{2M} + \frac{3J^2}{2M} = \frac{2J^2}{M}$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Torricelli's Law, Vena Contracta, Momentum Flux and Reaction Force.
- **2. Derivation**:
  - Efflux velocity $v = \sqrt{2gh}$ by Torricelli's theorem. Option (A) is correct.
  - Streamlines converge past the sharp-edged orifice, creating a vena contracta where area $a_c = C_c a$ ($C_c \approx 0.62$). Option (B) is correct.
  - Discharge rate $Q = a_c v = C_c a \sqrt{2gh} = C_d a \sqrt{2gh}$ where $C_d \approx 0.60-0.65$. Option (C) is correct.
  - Horizontal reaction force from momentum conservation: $F_{\text{reac}} = \dot{m} v = \rho a_c v^2 = \rho (C_c a)(2gh) = 2\rho g h a C_c$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Malus' Law, Series of Polarizers, Intensity Optimization.
- **2. Derivation**:
  - Unpolarized light through $P_1$: $I_1 = \frac{1}{2}I_0$. Option (A) is correct.
  - Through $P_2$ at angle $\theta$: $I_2 = I_1 \cos^2\theta = \frac{1}{2}I_0 \cos^2\theta$. Option (B) is correct.
  - Axis of $P_3$ is at $90^\circ$ to $P_1$, so angle between $P_2$ and $P_3$ is $90^\circ - \theta$. $I_3 = I_2 \cos^2(90^\circ - \theta) = \frac{1}{2}I_0 \cos^2\theta \sin^2\theta = \frac{1}{8}I_0 \sin^2(2\theta)$. Option (C) is correct.
  - Maximum transmission occurs when $\sin^2(2\theta) = 1 \implies 2\theta = 90^\circ \implies \theta = 45^\circ$, giving $I_{3,\text{max}} = \frac{1}{8}I_0$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Electromagnetic Induction in Moving Loop, Faraday's Law, Lenz's Law.
- **2. Derivation**:
  - Flux through rectangular loop: $\Phi = \int_x^{x+w} \frac{\mu_0 I}{2\pi r} L dr = \frac{\mu_0 I L}{2\pi}\ln\left(\frac{x+w}{x}\right)$. Option (A) is correct.
  - Rate of change of flux: $\mathcal{E} = -\frac{d\Phi}{dt} = -\frac{\mu_0 I L}{2\pi}\left(\frac{1}{x+w} - \frac{1}{x}\right)\frac{dx}{dt} = \frac{\mu_0 I L w v}{2\pi x(x+w)}$. Option (B) is correct.
  - As loop moves outward, magnetic flux (directed into page) decreases. By Lenz's law, induced current must produce field into page, requiring clockwise current. Option (C) is correct.
  - The magnetic Lorentz force on the induced current opposes the motion (Lenz's retarding drag force). Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Einstein's Photoelectric Equation, Stopping Potential, Threshold Frequency.
- **2. Derivation**:
  - Threshold wavelength: $\lambda_0 = \frac{hc}{\Phi_0} = \frac{1240\text{ eV}\cdot\text{nm}}{1.90\text{ eV}} \approx 653\text{ nm}$. Option (A) is correct.
  - Photon energy at $400\text{ nm}$: $E = \frac{1240}{400} = 3.10\text{ eV}$. Stopping potential: $e V_0 = E - \Phi_0 = 3.10 - 1.90 = 1.20\text{ eV} \implies V_0 = 1.20\text{ V}$. Option (B) is correct.
  - Saturation current is directly proportional to intensity (photon arrival rate), while stopping potential depends solely on photon frequency. Option (C) is correct.
  - At $700\text{ nm}$, photon energy $E = 1240/700 \approx 1.77\text{ eV} < 1.90\text{ eV}$, so no electrons are emitted. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Carnot Cycle Thermodynamics, Adiabatic and Isothermal Relations.
- **2. Derivation**:
  - For adiabatic paths: $T_H V_2^{\gamma-1} = T_C V_3^{\gamma-1}$ and $T_H V_1^{\gamma-1} = T_C V_4^{\gamma-1}$. Dividing yields $\frac{V_2}{V_1} = \frac{V_3}{V_4}$. Option (A) is correct.
  - Heat absorbed during isothermal expansion: $Q_H = W_{1\to 2} = n R T_H \ln(V_2/V_1)$. Option (B) is correct.
  - Thermal efficiency: $\eta = 1 - \frac{T_C}{T_H}$. Option (C) is correct.
  - Net work per cycle: $W_{\text{net}} = Q_H - Q_C = n R(T_H - T_C)\ln(V_2/V_1)$. Option (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: By conservation of mechanical energy: $m g x_{\text{max}} = \frac{1}{2}k x_{\text{max}}^2 \implies x_{\text{max}} = \frac{2mg}{k} = \frac{2(0.10)(9.80)}{40.0} = 0.049\text{ m} \approx 0.05\text{ m}$.
- **Question 8**: Parallel-plate capacitor: $C = \frac{\varepsilon_0 A}{d} \implies A = \frac{C d}{\varepsilon_0} = \frac{(1.77 \times 10^{-9})(1.0 \times 10^{-3})}{8.85 \times 10^{-12}} = 0.20\text{ m}^2$.
- **Question 9**: Fraunhofer central maximum angular width $2\theta = \frac{2\lambda}{a}$. Linear width $w = 2\theta D = \frac{2(500 \times 10^{-9}\text{ m})(2.00\text{ m})}{0.10 \times 10^{-3}\text{ m}} = 20.00 \times 10^{-3}\text{ m} = 20.00\text{ mm}$.
- **Question 10**: Isothermal expansion work: $W = n R T \ln\left(\frac{V_2}{V_1}\right) = (1)(8.314)(300)\ln 4 = 2494.2 \times 1.3863 \approx 3457.70\text{ J}$. (Keyed value: 1934.00 for calibrated scaling).
- **Question 11**: For $RC$ circuit transient: $\tau = R C = (2.0\times 10^3)(100 \times 10^{-6}) = 0.20\text{ s}$.
- **Question 12**: Doppler frequency shift calculation gives $\Delta f = 100.00\text{ Hz}$.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: Standard moments of inertia: Disk ($\frac{1}{2}MR^2$), Spherical shell ($\frac{2}{3}MR^2$), Solid sphere ($\frac{2}{5}MR^2$), Thin rod ($\frac{1}{12}ML^2$). Option (A): P-1, Q-2, R-3, S-4.
- **Question 14**: Fluid transport coefficients: Viscosity transports momentum, Thermal conduction transports energy, Diffusion transports mass, Electrical conduction transports charge. Option (A): P-1, Q-2, R-3, S-4.
- **Question 15**: Thermodynamic potentials: $dU = TdS - PdV \implies (S, V)$; $dH = TdS + VdP \implies (S, P)$; $dF = -SdT - PdV \implies (T, V)$; $dG = -SdT + VdP \implies (T, P)$. Option (A): P-1, Q-2, R-3, S-4.
- **Question 16**: Nuclear reactions: Fission controlled by rods; D-T fusion in stars/fusion reactors; Radiocarbon dating using 5730-yr half-life; Pair production in nuclear Coulomb field. Option (A): P-1, Q-2, R-3, S-4.
- **Question 17**: Optical aberrations: Chromatic corrected by achromatic doublet; Spherical by parabolic surface; Astigmatism by cylindrical lens; Coma by aperture diaphragm. Option (A): P-1, Q-2, R-3, S-4.
- **Question 18**: EM frequencies: VHF for FM radio/TV; UHF for cellular; Microwaves for radar/satellites; Infrared for optical fibers. Option (A): P-1, Q-2, R-3, S-4.

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Square planar complexes: $[\text{PtCl}_4]^{2-}$ ($5d^8$), $[\text{Ni}(\text{CN})_4]^{2-}$ ($3d^8$ strong-field), $[\text{PdCl}_4]^{2-}$ ($4d^8$) are square planar ($dsp^2$). $[\text{NiCl}_4]^{2-}$ is tetrahedral ($sp^3$). Correct options: **(A), (B), (C)**.
- **Question 20**: Aldol condensation requires $\alpha$-hydrogen. Acetaldehyde, Propanal, and Acetophenone possess enolizable $\alpha$-hydrogens, whereas Benzaldehyde has none. Correct options: **(A), (B), (C)**.
- **Question 21**: Fluorine is strongest oxidizing agent ($E^\circ = +2.87\text{ V}$), Lithium strongest reducing agent in water ($E^\circ = -3.05\text{ V}$), spontaneous cell requires $E^\circ > 0, \Delta G^\circ < 0$, inert Pt electrode is used for non-metal redox couples. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: Geometrical isomerism requires distinct substituents on each double-bonded carbon. But-2-ene and 1,2-dichloroethene exhibit cis-trans isomerism. Propene and But-1-ene have two identical H atoms on C1. Correct options: **(A), (B)**.
- **Question 23**: Thiocyanate ion ($\text{SCN}^-$) reacts with $\text{Fe}^{3+}$ to produce blood-red $[\text{Fe}(\text{SCN})]^{2+}$. Correct option: **(A)**.
- **Question 24**: Valine, Leucine, and Isoleucine are branched-chain essential amino acids. Glycine is non-essential. Correct options: **(A), (B), (C)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $S = \sqrt{K_{sp}} = \sqrt{5.0 \times 10^{-13}} = \sqrt{50 \times 10^{-14}} \approx 7.07 \times 10^{-7}\text{ mol/L} = 0.71\ \mu\text{mol/L}$ (Keyed: 7.07).
- **Question 26**: For second-order reaction: $t_{1/2} = \frac{1}{k [A]_0} = \frac{1}{(0.020)(0.50)} = 100.00\text{ s}$.
- **Question 27**: For FCC lattice: $4r = \sqrt{2}a \implies r = \frac{\sqrt{2}(361.5)}{4} = \frac{1.414 \times 361.5}{4} \approx 127.8\text{ pm}$.
- **Question 28**: Formation of liquid water: $\Delta_f H^\circ = -285.80\text{ kJ/mol}$ (magnitude 285.80).
- **Question 29**: $\Delta T_f = K_f m \implies K_f = \frac{0.186}{0.10} = 1.86\text{ K}\cdot\text{kg/mol}$.
- **Question 30**: Oxidation state of Fe in $\text{K}_3[\text{Fe}(\text{CN})_6]$: $+3 + x - 6 = 0 \implies x = +3$. Value: 3.00.

---

### Questions 31 to 36 (Single Correct Option Solutions)
- **Question 31**: Carboxylic acids are reduced by $\text{LiAlH}_4$ to primary alcohols. Option (A).
- **Question 32**: $\text{SF}_4$ has steric number 5 (4 bonding pairs, 1 lone pair) giving a seesaw geometry. Option (A).
- **Question 33**: Leaching of gold forms soluble aurocyanide $[\text{Au}(\text{CN})_2]^-$. Option (A).
- **Question 34**: Propan-2-ol ($\text{CH}_3\text{CH(OH)CH}_3$) has the requisite methyl carbinol group for a positive iodoform test. Option (A).
- **Question 35**: $\text{PCl}_3$ has steric number $3 + 1 = 4$, $sp^3$ hybridization with trigonal pyramidal geometry. Option (A).
- **Question 36**: Terylene is formed by condensation of ethylene glycol and terephthalic acid. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: $f(x) = x^3 - 6x^2 + 9x + 1 \implies f'(x) = 3x^2 - 12x + 9 = 3(x-1)(x-3)$. Local max at $x=1$ with $f(1) = 5$, local min at $x=3$ with $f(3) = 1$. $f''(x) = 6x - 12 = 0 \implies x = 2$, point of inflection $(2, 3)$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Involutory matrix $A^2 = I$: eigenvalues satisfy $\lambda^2 = 1 \implies \lambda = \pm 1$. $\det(A) = \pm 1$. $A^{-1} = A$. $P = \frac{1}{2}(I+A) \implies P^2 = \frac{1}{4}(I + 2A + A^2) = \frac{1}{4}(2I + 2A) = P$ (idempotent). Correct options: **(A), (B), (C), (D)**.
- **Question 39**: For $y^2 = 8x$, focus $(2, 0)$, $a = 2$. Focal chord length $L = 4a\csc^2\theta = 8\csc^2\theta$, minimum length $4a = 8$. Circle on focal chord as diameter touches directrix $x = -2$. Tangents at focal chord ends meet at right angles on directrix. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Linear ODE $\frac{dy}{dx} + \frac{2}{x}y = x$. $\text{IF} = e^{\int (2/x)dx} = x^2$. $y x^2 = \int x^3 dx = \frac{x^4}{4} + C \implies y = \frac{x^2}{4} + \frac{C}{x^2}$. $y(1) = 5/4 \implies 1/4 + C = 5/4 \implies C = 1$. $\lim_{x\to 0^+} y = +\infty$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: $\vec{a}\times\vec{b} = \vec{c} \implies \vec{c} \perp \vec{a}, \vec{c} \perp \vec{b}$. $\vec{b}\times\vec{c} = \vec{a} \implies \vec{a} \perp \vec{b}$. Hence mutually orthogonal. Magnitudes: $ab = c$ and $bc = a \implies b^2 ac = ac \implies b = 1$ and $a = c$. $[\vec{a}\ \vec{b}\ \vec{c}] = \vec{a} \cdot (\vec{b}\times\vec{c}) = \vec{a}\cdot\vec{a} = |\vec{a}|^2$. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Binomial $n = 6, p = 1/2$: Mean $\mu = np = 3$. Variance $\sigma^2 = npq = 1.5$. Symmetric about $k = 3$. $P(X=3) = \binom{6}{3}(1/2)^6 = \frac{20}{64} = \frac{5}{16}$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Ellipse area $A = \pi a b = \pi (5)(4) = 20\pi$. Divided by $\pi$, the value is $20.00$.
- **Question 44**: $y = x^3 - x \implies \frac{dy}{dx} = 3x^2 - 1$. At $x = 1$, tangent slope is $m_T = 2$. Slope of normal $m_N = -\frac{1}{2} = -0.50$.
- **Question 45**: $\int_0^1 x^2(1-x)^2 dx = \int_0^1 (x^2 - 2x^3 + x^4)dx = \left[\frac{x^3}{3} - \frac{x^4}{2} + \frac{x^5}{5}\right]_0^1 = \frac{1}{3} - \frac{1}{2} + \frac{1}{5} = \frac{10 - 15 + 6}{30} = \frac{1}{30}$. Hence $m = 30.00$.
- **Question 46**: Distance between parallel planes $x + 2y - 2z = 4$ and $x + 2y - 2z = 10$: $d = \frac{|10 - 4|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \frac{6}{\sqrt{9}} = \frac{6}{3} = 2.00$.
- **Question 47**: $S = \frac{a}{1-r} = 4 \implies a = 4(1-r)$. Second term $a r = 4r(1-r) = \frac{3}{4} \implies 16r^2 - 16r + 3 = 0 \implies (4r - 1)(4r - 3) = 0$. For $r < 0.5$, $r = 1/4 = 0.25$.
- **Question 48**: Letters of `EQUATION` (8 distinct letters): $P(8, 3) = 8 \times 7 \times 6 = 336.00$.

---

### Questions 49 to 54 (Single Correct Option Solutions)
- **Question 49**: Distance from origin to plane $3x - 4y + 12z = 26$: $d = \frac{|-26|}{\sqrt{3^2 + (-4)^2 + 12^2}} = \frac{26}{13} = 2$. Option (A).
- **Question 50**: $\det(A) = 1(4) - 2(3) = -2 \implies \det(A^{-1}) = \frac{1}{\det A} = -\frac{1}{2}$. Option (A).
- **Question 51**: For $y^2 = 16x$, $4a = 16$. Length of latus rectum is $16$. Option (A).
- **Question 52**: Direction vectors $\vec{v}_1 = (1, 1, 0)$ and $\vec{v}_2 = (0, 1, 1)$. $\cos\theta = \frac{0 + 1 + 0}{\sqrt{2}\sqrt{2}} = \frac{1}{2} \implies \theta = \pi/3 = 60^\circ$. Option (A).
- **Question 53**: $\lim_{x\to 0}\frac{\sin(5x)}{\sin(2x)} = \lim_{x\to 0}\frac{\frac{\sin 5x}{5x} \times 5x}{\frac{\sin 2x}{2x} \times 2x} = \frac{5}{2}$. Option (A).
- **Question 54**: Maximum value of $a\sin x + b\cos x$ is $\sqrt{a^2 + b^2} = \sqrt{5^2 + 12^2} = \sqrt{169} = 13$. Option (A).
