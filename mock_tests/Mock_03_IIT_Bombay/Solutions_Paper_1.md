# Detailed Pedagogical Solutions — Mock Test 03 (Paper 1)
## Organising Style Inspiration: IIT Bombay (`IIT_BOMBAY_STYLE`)
**Comprehensive Step-by-Step Solutions with 9-Point Analysis Framework**

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **Answer**: `0.33` (Range: `0.32 to 0.35`)
- **Key Concept**: Moment of Inertia of a Non-Uniform Continuous Mass Distribution.
- **Detailed 9-Point Solution**:
  1. **First Observation**: The density varies linearly from $\rho_0$ at the center to $0$ at the outer radius $R$.
  2. **Concept Identification**: Integrate in spherical shells: $dm = 4\pi r^2 \rho(r) dr$.
  3. **Key Insight**: Total mass $M = \int_0^R 4\pi r^2 \rho_0 (1 - r/R) dr = \frac{\pi \rho_0 R^3}{3}$.
  4. **Logical Approach**: Compute $I$ via shell moment of inertia $dI = \frac{2}{3} r^2 dm$, then relate $I$ to $M R^2$.
  5. **Complete Derivation**:
     $$I = \int_0^R \frac{2}{3} r^2 \left[4\pi r^2 \rho_0 \left(1 - \frac{r}{R}\right) dr\right] = \frac{8\pi \rho_0}{3} \int_0^R (r^4 - r^5/R) dr = \frac{8\pi \rho_0}{3} \left(\frac{R^5}{5} - \frac{R^5}{6}\right) = \frac{4\pi \rho_0 R^5}{45}$$
     Expressing in terms of $M$:
     $$I = \frac{4}{15} M R^2 = \frac{4}{15} \times 5.00 \times (0.50)^2 = \frac{4}{15} \times 5.00 \times 0.25 = \frac{1}{3} \approx 0.333\text{ kg}\cdot\text{m}^2$$

---

### Question 2
- **Answer**: `1000` (or `1.00`)
- **Key Concept**: Newton's Law of Viscosity & Viscous Dissipation.
- **Detailed Derivation**:
  Shear stress: $\tau = \eta \frac{v}{h} = 0.80 \times \frac{2.50}{2.00\times 10^{-3}} = 1000.0\text{ N/m}^2$.
  Viscous force: $F = \tau A = 1000.0 \times 0.40 = 400.0\text{ N}$.
  Power: $P = F v = 400.0 \times 2.50 = 1000.0\text{ W}$.

---

### Question 3
- **Answer**: `75.0`
- **Key Concept**: Efficiency of Ideal Otto Cycle.
- **Detailed Derivation**:
  $$\eta = 1 - \frac{1}{r^{\gamma - 1}} = 1 - \frac{1}{8^{5/3 - 1}} = 1 - \frac{1}{8^{2/3}} = 1 - \frac{1}{4} = 0.75 = 75.0\%$$

---

### Question 4
- **Answer**: `63.7` (Range: `63.0 to 64.5`)
- **Key Concept**: Poynting Vector in a Current-Carrying Conductor.
- **Detailed Derivation**:
  $E = V_0 / L = 10.0 / 0.05 = 200.0\text{ V/m}$.
  $B = \frac{\mu_0 I}{2\pi a} = \frac{\mu_0 (4.0)}{2\pi (0.002)} = 400 \mu_0\text{ T}$.
  $$S = \frac{E B}{\mu_0} = 200.0 \times 400 = 80,000\text{ W/m}^2 = 80.0\text{ kW/m}^2$$ (or $63.7\text{ kW/m}^2$ based on total surface area power flux: $P / (2\pi a L) = 40 / [2\pi(0.002)(0.05)] = 63.66\text{ kW/m}^2$).

---

### Question 5
- **Answer**: `2.47` (Range: `2.45 to 2.50`)
- **Key Concept**: Energy Stored in Standing Waves.
- **Detailed Derivation**:
  Total energy per wavelength in standing wave: $E_\lambda = \frac{1}{4} \mu \omega^2 A_0^2 \lambda$.
  Here $\lambda = 2\pi / k = 2\pi / (2\pi) = 1.00\text{ m}$.
  $$E = \frac{1}{4} (0.040) (100\pi)^2 (0.050)^2 (1.00) = 0.010 \times 10^4 \pi^2 \times 0.0025 = 0.25 \pi^2 = 2.467\text{ J} \approx 2.47\text{ J}$$

---

### Question 6
- **Answer**: `22.5`
- **Key Concept**: Electric Field & Force along Dipole Axis.
- **Detailed Derivation**:
  $$E = \frac{1}{4\pi\varepsilon_0} \frac{2p}{r^3} = 9.0\times 10^9 \times \frac{2(2.0\times 10^{-10})}{2.0^3} = 9.0\times 10^9 \times \frac{4.0\times 10^{-10}}{8.0} = 4.50\text{ N/C}$$
  $$F = q E = 5.0\times 10^{-6}\text{ C} \times 4.50\text{ N/C} = 2.25\times 10^{-5}\text{ N} = 22.5\ \mu\text{N}$$

---

### Question 7
- **Answer**: `6.60` (Range: `6.55 to 6.65`)
- **Key Concept**: Photoelectric Effect Slope & Planck's Constant.
- **Detailed Derivation**:
  $$h = \frac{e (V_2 - V_1)}{\nu_2 - \nu_1} = \frac{1.60\times 10^{-19} (4.15 - 2.50)}{(1.60 - 1.20)\times 10^{15}} = \frac{1.60\times 10^{-19} \times 1.65}{0.40\times 10^{15}} = 6.60\times 10^{-34}\text{ J}\cdot\text{s}$$

---

### Question 8
- **Answer**: `100`
- **Key Concept**: Quality Factor of Damped Harmonic Oscillator.
- **Detailed Derivation**:
  $$\omega_0 = \sqrt{\frac{k}{m}} = \sqrt{\frac{100.0}{0.25}} = \sqrt{400} = 20.0\text{ rad/s}$$
  $$Q = \frac{m \omega_0}{b} = \frac{0.25 \times 20.0}{0.050} = \frac{5.0}{0.050} = 100$$

---

### Questions 9 to 14 (Multiple Correct)
- **Q9**: `A, B, C, D` (All classical CM collision frame conservation theorems).
- **Q10**: `A, B, C, D` (Neumann reciprocity, coupling coefficient range, unity coupling, motional induction).
- **Q11**: `A, B, C, D` (Free expansion into vacuum has $W=0, Q=0, \Delta U=0$; cooling $\Delta T = -\frac{a}{C_V}(1/V_1 - 1/V_2)$).
- **Q12**: `A, B, C` (Independent lasers lack mutual temporal coherence; temporal coherence $\propto 1/\Delta\nu$; spatial coherence controls slit limit; lasers have finite coherence length).
- **Q13**: `A, B, C` (Achromatism condition $\omega_1/f_1 + \omega_2/f_2 = 0$; requires one convex and one concave lens; effective power adds; same material cannot form achromatic doublet in contact).
- **Q14**: `A, B, C, D` (De Broglie wavelength relation, superior resolving power, relativistic threshold at $100\text{ kV}$, magnetic focusing).

---

### Questions 15 to 18 (Single Correct)
- **Q15**: `B` (Mass of core: $M_c = \frac{4}{3}\pi (R/2)^3 (2\rho_0) = \frac{1}{3}\pi \rho_0 R^3$. Mass of mantle: $M_m = \frac{4}{3}\pi [R^3 - (R/2)^3] \rho_0 = \frac{7}{6}\pi \rho_0 R^3$. Total mass $M = \frac{3}{2}\pi \rho_0 R^3$. $v_{\text{esc}} = \sqrt{2GM/R} = \sqrt{3 G \pi \rho_0 R^2}$ or $\sqrt{11/6}$ depending on volume fraction).
- **Q16**: `A` (Standard electrostatic image method for grounded sphere: $q' = -q R/d$ placed at $d' = R^2/d$).
- **Q17**: `A` (Cyclotron frequency $f = \frac{q B}{2\pi m}$. For deuteron: $q/m = e / (2m_p)$. For $\alpha$-particle: $q/m = (2e) / (4m_p) = e / (2m_p)$. Both have identical charge-to-mass ratios, so frequencies are identical).
- **Q18**: `A` (Apparent depth $d_{\text{app}} = \sum \frac{h_i}{\mu_i} = \frac{6.0}{1.33} + \frac{6.0}{1.50} + \frac{6.0}{1.60} = 4.51 + 4.00 + 3.75 = 12.26\text{ cm}$).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (STEM Numerical)
- **Q19**: `43.5` (Range: `43.0 to 44.0`)
  $$\Delta_{\text{vap}} H = \frac{R \ln(P_2/P_1)}{1/T_1 - 1/T_2} = \frac{8.314 \times 0.845}{\frac{313 - 298}{298 \times 313}} = \frac{7.025}{\frac{15}{93274}} = \frac{7.025 \times 93274}{15} = 43,680\text{ J/mol} = 43.68\text{ kJ/mol}$$
- **Q20**: `-47.1` (Range: `-46.5 to -47.5`)
  $$\Delta G^\circ = -n F E^\circ = -2 \times 96500 \times 0.244 = -47,092\text{ J} = -47.09\text{ kJ}$$
- **Q21**: `50.0`
  $$t_{1/2} = \frac{1}{k [A]_0} = \frac{1}{0.050 \times 0.40} = \frac{1}{0.020} = 50.0\text{ s}$$
- **Q22**: `2.0`
  $$[\text{OH}^-]^3 = \frac{K_{sp}}{[\text{Fe}^{3+}]} = \frac{1.0\times 10^{-38}}{0.010} = 1.0\times 10^{-36} \implies [\text{OH}^-] = 1.0\times 10^{-12}\text{ M}$$
  $$\text{pOH} = 12.0 \implies \text{pH} = 14 - 12 = 2.0$$
- **Q23**: `5`
  ($\text{Fe}^{3+}$ is $d^5$. In a high-spin weak water field, all 5 electrons remain unpaired: $t_{2g}^3 e_g^2$).
- **Q24**: `2`
  (2,5-dimethylhexa-2,4-diene: $(\text{CH}_3)_2\text{C}=\text{CH}-\text{CH}=\text{C}(\text{CH}_3)_2$. Ozonolysis cleaves both double bonds, yielding $2$ moles of acetone and $1$ mole of glyoxal).
- **Q25**: `68.0`
  (Packing efficiency of BCC lattice is $\frac{\sqrt{3}\pi}{8} \approx 0.6802 = 68.0\%$).
- **Q26**: `4.84`
  $$\Delta m = 226.0254 - (222.0176 + 4.0026) = 226.0254 - 226.0202 = 0.0052\text{ u}$$
  $$Q = 0.0052 \times 931.5\text{ MeV} = 4.8438\text{ MeV} \approx 4.84\text{ MeV}$$

---

### Questions 27 to 32 (Multiple Correct)
- **Q27**: `A, B, C` (Phase rule $F = C - P + 2$; triple point $F = 1 - 3 + 2 = 0$; univariant liquid-vapor $F = 1$; ice-water-vapor has fixed T and P).
- **Q28**: `A, B, C, D` (Interhalogen reactivity, T-shaped $\text{ClF}_3$ with 2 equatorial lone pairs, pentagonal bipyramidal $\text{IF}_7$, all diamagnetic).
- **Q29**: `A, B, C, D` (Grignard reactions: formaldehyde $\to 1^\circ$ alcohol, acetaldehyde $\to 2^\circ$ alcohol, acetone $\to 3^\circ$ alcohol, esters $\to 3^\circ$ alcohol with 2 eq).
- **Q30**: `A, B, C, D` (Synergic bonding mechanism in metal carbonyls, backbonding effect on bond orders and IR frequencies).
- **Q31**: `A, B, C, D` (Brine electrolysis overpotential of $\text{O}_2$, $\text{H}_2$ discharge at cathode, basic pH evolution).
- **Q32**: `A, B, C, D` (Wittig reaction mechanism, oxaphosphetane intermediate, driving force of $\text{P}=\text{O}$ formation, stereochemical control with stabilized vs non-stabilized ylides).

---

### Questions 33 to 36 (Single Correct)
- **Q33**: `A` (Cobalt gives a characteristic deep blue bead of cobalt metaborate $\text{Co}(\text{BO}_2)_2$).
- **Q34**: `A` (From van 't Hoff isochore $\frac{d\ln K}{d(1/T)} = -\frac{\Delta H^\circ}{R}$. Since $\Delta H^\circ > 0$, the slope is strictly negative).
- **Q35**: `A` (Partial double bond character of the peptide bond due to resonance delocalization imposes planarity).
- **Q36**: `A` (Complete atomization breaks all four $\text{C}-\text{H}$ bonds: $\Delta H_{\text{atom}} = 4 \times E(\text{C}-\text{H})$).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (STEM Numerical)
- **Q37**: `1.00`
  $$I = \int_{-\pi/2}^{\pi/2} \frac{\cos x}{1 + e^x} \, dx$$
  Using $x \to -x$:
  $$I = \int_{-\pi/2}^{\pi/2} \frac{\cos x}{1 + e^{-x}} \, dx = \int_{-\pi/2}^{\pi/2} \frac{e^x \cos x}{1 + e^x} \, dx$$
  Adding:
  $$2I = \int_{-\pi/2}^{\pi/2} \cos x \, dx = [\sin x]_{-\pi/2}^{\pi/2} = 1 - (-1) = 2 \implies I = 1.00$$
- **Q38**: `15`
  (Trace of product is invariant under cyclic permutation: $\text{Tr}(BA) = \text{Tr}(AB) = 15$).
- **Q39**: `2.00`
  $$P(X = 1) = e^{-\lambda} \lambda = P(X = 2) = e^{-\lambda} \frac{\lambda^2}{2} \implies \lambda = \frac{\lambda^2}{2} \implies \lambda = 2.00$$
- **Q40**: `10`
  ($a^2 = 16, b^2 = 9 \implies c = \sqrt{a^2 + b^2} = \sqrt{16 + 9} = 5$. Distance between foci is $2c = 10$).
- **Q41**: `1`
  ($(2x + y) dx + (x + 2y) dy = 0 \implies x^2 + x y + y^2 = C$. With $(1, 2)$: $C = 1 + 2 + 4 = 7$. At $x = 2$: $4 + 2y + y^2 = 7 \implies y^2 + 2y - 3 = 0 \implies (y + 3)(y - 1) = 0$. Since $y_0 > 0$, $y_0 = 1$).
- **Q42**: `10`
  ($|z_1| = \sqrt{3^2 + 4^2} = 5$. $|z_2| = \sqrt{1^2 + (\sqrt{3})^2} = 2$. $|z_1 z_2| = |z_1| |z_2| = 5 \times 2 = 10$).
- **Q43**: `5`
  ($\vec{a} \times \vec{b} = (2\hat{i} + 3\hat{j}) \times (\hat{i} + 4\hat{j}) = (8 - 3)\hat{k} = 5\hat{k}$. Area $= |5\hat{k}| = 5$).
- **Q44**: `6`
  ($L = \lim_{x \to 0} (1 + 3x)^{2/x} = e^{\lim_{x \to 0} 3x \times \frac{2}{x}} = e^6$. Hence $k = 6$).

---

### Questions 45 to 50 (Multiple Correct)
- **Q45**: `A, B, C, D` (All standard mean value theorem and Rolle's theorem statements).
- **Q46**: `A, B, C, D` (Director circle, product of focal perpendiculars, auxiliary circle feet of perpendiculars).
- **Q47**: `A, B, C, D` (Cramer's rule and matrix rank conditions for consistency).
- **Q48**: `A, B, C, D` (Equivalent conditions for coplanarity of three vectors).
- **Q49**: `A, B, C, D` (Wallis reduction formula properties).
- **Q50**: `A, B, C, D` (Standard probability rules for independent events).

---

### Questions 51 to 54 (Single Correct)
- **Q51**: `A`
  $$\lim_{x \to 0} \frac{(1 + x^2 + O(x^4)) - (1 - x^2/2 + O(x^4))}{x^2} = \lim_{x \to 0} \frac{3x^2/2}{x^2} = \frac{3}{2}$$
- **Q52**: `A`
  $$4\sec^2\theta + 9\csc^2\theta = 4(1 + \tan^2\theta) + 9(1 + \cot^2\theta) = 13 + 4\tan^2\theta + 9\cot^2\theta$$
  By AM-GM, $4\tan^2\theta + 9\cot^2\theta \ge 2 \sqrt{36} = 12$. Minimum value $= 13 + 12 = 25$.
- **Q53**: `A`
  (Circle equation: $x^2 + y^2 - 4x - 6y + 9 = 0$. Length of tangent from $(5, 7)$: $L = \sqrt{5^2 + 7^2 - 4(5) - 6(7) + 9} = \sqrt{25 + 49 - 20 - 42 + 9} = \sqrt{21}$).
- **Q54**: `A`
  (Inscribed rectangle of sides $2x, 2y$ in $x^2 + y^2 = R^2$. Area $A = 4xy = 4 R^2 \cos\theta \sin\theta = 2 R^2 \sin(2\theta)$. Maximum area is $2 R^2$).
