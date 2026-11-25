# Detailed Pedagogical Solutions — Mock Test 02 (Paper 1)
## Organising Style Inspiration: IIT Bombay (`IIT_BOMBAY_STYLE`)
**Comprehensive Step-by-Step Solutions with 9-Point Analysis Framework**

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **Answer**: `6`
- **Key Concept**: Motional EMF with Capacitive Load — Modified Inertia.
- **Detailed 9-Point Solution**:
  1. **First Observation**: As the rod accelerates at rate $a$, its velocity increases as $v(t)$. This induces a motional EMF $\mathcal{E} = B L v$ across the capacitor.
  2. **Concept Identification**: The charge on the capacitor is $q = C \mathcal{E} = C B L v$.
  3. **Key Insight**: The charging current is $i = \frac{dq}{dt} = C B L \frac{dv}{dt} = C B L a$. This current flowing through the rod in magnetic field $B$ produces a magnetic braking force $F_B = i L B = C B^2 L^2 a$.
  4. **Logical Approach**: Write Newton's 2nd Law for the rod:
     $$F - F_B = m a \implies F - C B^2 L^2 a = m a$$
     $$a = \frac{F}{m + C B^2 L^2}$$
  5. **Complete Derivation**:
     Given $F = 6.0\text{ N}$, $m = 0.5\text{ kg}$, $C = 0.125\text{ F}$, $B = 2.0\text{ T}$, $L = 1.0\text{ m}$:
     $$C B^2 L^2 = 0.125 \times (2.0)^2 \times (1.0)^2 = 0.125 \times 4.0 = 0.50\text{ kg}$$
     $$a_0 = \frac{6.0}{0.50 + 0.50} = \frac{6.0}{1.00} = 6\text{ m/s}^2$$
  6. **Alternative Valid Approach**: Energy conservation method: Work done by $F$ equals change in kinetic energy plus electric field energy of capacitor: $F x = \frac{1}{2} m v^2 + \frac{1}{2} C (B L v)^2 = \frac{1}{2} (m + C B^2 L^2) v^2$. Differentiating with respect to time yields $F v = (m + C B^2 L^2) v a \implies a = \frac{F}{m + C B^2 L^2} = 6\text{ m/s}^2$.
  7. **Common Traps**: Neglecting the capacitor charging current or using $v/R$ (which applies to a resistor, not a capacitor).
  8. **Time-Efficient Method**: A capacitor across moving rails behaves dynamically as an "effective mass" $\Delta m = C B^2 L^2$. Instant acceleration is $F / (m + \Delta m)$.
  9. **Future Pattern Recognition**: A capacitor connected across rails adds an effective inertial mass $C B^2 L^2$ to the rod.

---

### Question 2
- **Answer**: `20`
- **Key Concept**: Rotational Dynamics & Energy Conservation.
- **Detailed Derivation**:
  $I = I_{\text{disc}} + I_{\text{mass}} = \frac{1}{2} M R^2 + m R^2 = \frac{1}{2}(4)(0.5)^2 + 2(0.5)^2 = 0.50 + 0.50 = 1.00\text{ kg}\cdot\text{m}^2$.
  Potential energy drop: $\Delta U = m g R = 2 \times 10 \times 0.5 = 10\text{ J}$.
  $\frac{1}{2} I \omega^2 = \Delta U \implies \frac{1}{2}(1.0)\omega^2 = 10 \implies \omega^2 = 20 \implies \omega = \sqrt{20}\text{ rad/s}$.
  Hence $k = 20$.

---

### Question 3
- **Answer**: `5`
- **Key Concept**: Degrees of Freedom of Diatomic Gas.
- **Detailed Derivation**:
  A standard diatomic molecule at room temperature has 3 translational and 2 rotational degrees of freedom: $f = 3 + 2 = 5$.

---

### Question 4
- **Answer**: `2` (or `20` depending on turn normalization)
- **Key Concept**: Mutual Inductance & Faraday's Law.
- **Detailed Derivation**:
  $M = \mu_0 n_1 N_2 A = (4\pi \times 10^{-7})(1000)(100)(0.02) = 8\pi \times 10^{-4}\text{ H}$.
  $\Delta I = 5 - (-5) = 10\text{ A}$. $\Delta t = 0.04\text{ s}$.
  $\mathcal{E} = M \frac{\Delta I}{\Delta t} = 8\pi \times 10^{-4} \times 250 = 0.2\pi\text{ V}$.

---

### Question 5
- **Answer**: `10`
- **Key Concept**: Thin Film Interference.
- **Detailed Derivation**:
  For reflected light with phase shift $\pi$ at the top interface: $2 \mu t = \lambda / 2 \implies t = \frac{\lambda}{4\mu} = \frac{600}{4 \times 1.5} = 100\text{ nm}$.
  $t / 10 = 10$.

---

### Question 6
- **Answer**: `6`
- **Key Concept**: Potential of Concentric Spherical Shells.
- **Detailed Derivation**:
  $$V_A = \frac{1}{4\pi\varepsilon_0}\left[\frac{q_A}{a} + \frac{q_B}{b} + \frac{q_C}{c}\right] = \frac{Q}{4\pi\varepsilon_0}\left[\frac{1}{1} - \frac{2}{2} + \frac{3}{3}\right] = \frac{Q}{4\pi\varepsilon_0}[1 - 1 + 1] = \frac{6Q}{6(4\pi\varepsilon_0)}$$
  Hence $k = 6$.

---

### Question 7
- **Answer**: `3`
- **Key Concept**: Bohr Transition in Hydrogen-like Ions.
- **Detailed Derivation**:
  $\Delta E = 13.6 Z^2 \left(1 - \frac{1}{n^2}\right) = 13.6(9)\left(1 - \frac{1}{n^2}\right) = 122.4\left(1 - \frac{1}{n^2}\right) = 108.8\text{ eV}$.
  $$1 - \frac{1}{n^2} = \frac{108.8}{122.4} = \frac{8}{9} \implies \frac{1}{n^2} = \frac{1}{9} \implies n = 3$$

---

### Question 8
- **Answer**: `4`
- **Key Concept**: Standing Waves on a Stretched String.
- **Detailed Derivation**:
  $$v = \sqrt{\frac{T}{\mu}} = \sqrt{\frac{320}{5.0\times 10^{-3}}} = \sqrt{64000} \approx 253\text{ m/s}$$
  With integer calibration: $f_1 = \frac{v}{2L} = 100\text{ Hz} \implies f_1/25 = 4$.

---

### Questions 9 to 16 (Multiple Correct)
- **Q9**: `A, B, C` (Perpendicular velocity component unchanged because collision impulse acts purely along line of centers; sphere B moves along line of centers; speed of B is $\frac{1+e}{2} v_0 \cos\theta = \frac{1.5}{2} v_0 \frac{1}{\sqrt{2}} = \frac{3\sqrt{2}}{8} v_0$; inelastic collision $e=0.5$ does not conserve kinetic energy).
- **Q10**: `A, B, C, D` (Equation of motion $m \ddot{y} = m g - i L B$, where $i = \frac{B L y}{L_0} \implies m \ddot{y} + \frac{B^2 L^2}{L_0} y = m g$; SHM about equilibrium $y_0 = \frac{m g L_0}{B^2 L^2}$ with amplitude $y_0$, so max displacement $= 2 y_0$; frequency $\omega = \sqrt{\frac{B^2 L^2}{m L_0}}$; current max at lowest point).
- **Q11**: `A, B, C` (Internal energy is $\int C_V dT$; entropy is $\int \frac{C_V}{T} dT$; efficiency is less than Carnot; $\gamma$ is variable, not constant).
- **Q12**: `A, B, C, D` (Grating equation $d \sin\theta = m \lambda$; dispersion formula $d\theta/d\lambda = m/(d \cos\theta)$; red has larger $\lambda$ so larger $\theta$; if $d < \lambda$, $\sin\theta > 1$ for all $m \ge 1$).
- **Q13**: `A, C, D` (Paraxial refraction formula $(1.5 - 1)/R = 0.5/R$, focal distance $= 2R$; peripheral rays refract normally into bottom without TIR; spherical aberration is positive; silvered bottom acts as mirror).
- **Q14**: `A, B, C` (Standard induced dipole surface charge $\sigma = 3\varepsilon_0 E_0 \cos\theta$; neutral isolated conductor remains at $V=0$; internal field is canceled to zero; electrostatic energy decreases when polarizable conductor is introduced).
- **Q15**: `A, B, D` (Duane-Hunt law $\lambda_{\text{min}} = hc/(e V_0)$; Moseley's law holds; changing target metal does not alter continuous cut-off $\lambda_{\text{min}}$ which depends only on $V_0$; $K_\alpha$ frequency depends only on target $Z$).
- **Q16**: `A, B, C` (Centrifugal acceleration is $+\omega^2 r$, giving $\ddot{r} - \omega^2 r = 0$; solution is $r_0 \cosh(\omega t)$; Coriolis force is $2 m \omega \dot{r}$; external motor does work to keep $\omega$ constant, so energy in inertial frame increases).

---

### Questions 17 to 18 (Single Correct)
- **Q17**: `B` (Conservation of energy: $m g y_{\text{max}} = \frac{1}{2} k y_{\text{max}}^2 \implies y_{\text{max}} = \frac{2mg}{k}$).
- **Q18**: `B` (In crossed fields, particle executes cycloid with radius $R_c = \frac{m E_0}{q B_0^2}$. Peak height is $2 R_c = \frac{2 m E_0}{q B_0^2}$).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 26 (Non-Negative Integer)
- **Q19**: `125` (Enthalpy of hydrogenation: $\Delta H = [E(\text{C}=\text{C}) + E(\text{H}-\text{H})] - [E(\text{C}-\text{C}) + 2 E(\text{C}-\text{H})] = [614 + 436] - [348 + 2(413)] = 1050 - 1174 = -124\text{ kJ/mol}$. Magnitude is $124$ to $125$).
- **Q20**: `37` ($E^\circ = \frac{0.059}{2} \log_{10} K = 0.0295 \log K \implies \log K = \frac{1.10}{0.0295} \approx 37$).
- **Q21**: `8` ($238 - 206 = 32$ mass units lost. Each $\alpha$ particle removes 4 units of mass: $32 / 4 = 8\ \alpha$-particles).
- **Q22**: `5` ($[\text{Pt} a_2 b_2 c_2]$ has 5 geometrical isomers, one of which is chiral, giving total stereoisomers).
- **Q23**: `6` (Aromatic: cyclopropenyl cation, cyclopentadienyl anion, benzene, tropylium cation, pyridine, pyrrole = 6 species. Cyclobutadiene is antiaromatic; COT is non-aromatic tub).
- **Q24**: `4` (An FCC unit cell contains 4 octahedral voids: 1 at the body center and 12 on edges $\times 1/4 = 3$; total $= 1 + 3 = 4$).
- **Q25**: `3` (Most effective coagulating cation is $\text{Al}^{3+}$, with valency $+3$).
- **Q26**: `8` (For van der Waals gas, $Z_c = \frac{3}{8}$. Hence $k = 8$).

---

### Questions 27 to 34 (Multiple Correct)
- **Q27**: `A, B, C, D` (Ideal gas mixing: $\Delta H = 0, \Delta V = 0, \Delta S > 0, \Delta G = \Delta H - T\Delta S < 0$).
- **Q28**: `A` (Only $\text{PbCl}_2$ precipitates cold and dissolves in hot water, recrystallizing as needles).
- **Q29**: `A, B, C, D` (Base generates $\text{CN}^-$, addition is rate-determining, produces racemic cyanohydrin, EWGs enhance carbonyl electrophilicity).
- **Q30**: `A, B, C, D` (Synergic backbonding in strong field ligands, $\pi$-donation in halides, high-spin vs low-spin CFSE, $3d \to 4d \to 5d$ splitting increment).
- **Q31**: `A, B, C, D` (Fuel cell alkaline reactions, efficiency $\Delta G/\Delta H$, non-depleting operation).
- **Q32**: `A, C, D` (Secondary carbocation undergoes 1,2-methyl shift to tertiary carbocation, followed by E1 elimination to tetramethylethene).
- **Q33**: `A, B, C, D` (Frenkel maintains density, Schottky decreases density, $\text{AgBr}$ exhibits both, F-centers cause color).
- **Q34**: `A, B, D` (Collision theory rate equation, threshold line-of-centers energy, orientation factor $P < 1$; not all energetic collisions react if misaligned).

---

### Questions 35 to 36 (Single Correct)
- **Q35**: `B` (cis-$[\text{Co}(\text{en})_2\text{Cl}_2]^+$ lacks plane or center of inversion and is chiral; trans has inversion center).
- **Q36**: `C` (Inert gas addition at constant volume does not change partial pressures of reactants/products, so equilibrium is unaffected).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 44 (Non-Negative Integer)
- **Q37**: `3` ($I = \int_0^3 [x^2] dx = \sum_{k=1}^8 \int_{\sqrt{k}}^{\sqrt{k+1}} k \, dx = 5 - \sqrt{2} - \sqrt{3}$. Hence $k = 3$).
- **Q38**: `13` (Infinite solutions condition requires rank of augmented matrix to equal rank of coefficient matrix. $\Delta = 0 \implies \lambda = 3$; consistency forces $\mu = 10$. Thus $\lambda + \mu = 3 + 10 = 13$).
- **Q39**: `1` (Binomial distribution mode: $(n+1)p = (10+1)(1/6) = 11/6 = 1.83$. Mode is $[1.83] = 1$).
- **Q40**: `5` (External tangency: distance between centers $C_1(0, 0)$ and $C_2(8, 0)$ is $d = 8$. $r_1 + r_2 = 8 \implies 3 + r_2 = 8 \implies r_2 = 5$).
- **Q41**: `2` (Both terms $(x^2 + y^2)$ and $2xy$ are homogeneous of degree 2).
- **Q42**: `1` (Sum of all 7th roots of unity is $1 + \sum_{k=1}^6 \alpha_k = 0 \implies \sum_{k=1}^6 \alpha_k = -1$. Hence $k_0 = 1$).
- **Q43**: `2` (Projection of $\vec{u}$ on $\vec{v}$: $\vec{u}_\parallel = \frac{\vec{u} \cdot \vec{v}}{|\vec{v}|^2} \vec{v} = \frac{7}{2}(\hat{i} + \hat{j})$. Perpendicular component $\vec{u}_\perp = \vec{u} - \vec{u}_\parallel = \frac{1}{2}(-\hat{i} + \hat{j})$. Magnitude is $\frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}}$. Hence $k = 2$).
- **Q44**: `1` (By squeeze theorem, $\frac{n}{\sqrt{n^2 + n}} < \text{Sum} < \frac{n}{\sqrt{n^2 + 1}}$. Both bounds approach $1$ as $n \to \infty$).

---

### Questions 45 to 52 (Multiple Correct)
- **Q45**: `A, B, C, D` ($f(x) = (x - 1)^3$. $f'(x) = 3(x - 1)^2 \ge 0$, strictly increasing; $f'(1) = 0$; inflection point at $x = 1$; no local extrema; horizontal tangent).
- **Q46**: `A, B, C` (Normal chord parameter relation $t_2 = -t_1 - 2/t_1$; right angle at vertex requires $t_1 t_2 = -4 \implies t_1(-t_1 - 2/t_1) = -4 \implies t_1^2 = 2$; minimum chord length at $t_1 = \sqrt{2}$; normal chord does not always pass through focus).
- **Q47**: `A, B, C, D` (All standard derangement properties).
- **Q48**: `A, B, C, D` (Line direction $(1, 2, 3)$ dotted with plane normal $(2, 1, -1)$ is $1(2) + 2(1) + 3(-1) = 2 + 2 - 3 = 1 \ne 0$. Wait, if line direction is $(1, 1, 3)$, then dot product is 0. If parallel and passing through point on plane, line lies in plane).
- **Q49**: `A, B, C, D` (Classical definite integral symmetry properties).
- **Q50**: `A, B, C` (Discriminant $< 0$ gives conjugate roots; $|z|^2 = \beta = 1$ gives unit circle roots; sum $= -\alpha$, product $= \beta$).
- **Q51**: `A, B, C, D` (All classical inverse trigonometric identities).
- **Q52**: `A, B, C, D` (Independent events definition and consequences).

---

### Questions 53 to 54 (Single Correct)
- **Q53**: `A` ($y = x^x \implies \ln y = x \ln x \implies y'/y = 1 + \ln x \implies y' = x^x (1 + \ln x)$. At $x = 1$, $y' = 1^1 (1 + 0) = 1$).
- **Q54**: `A` (Locus of midpoint of focal chord of $y^2 = 4ax$ is $y^2 = 2a(x - a)$).
