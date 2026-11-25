# Detailed Solutions and Pedagogical Analysis — Mock Examination 13 (Paper 2)
### Organising Institute Style: IIT Kharagpur (`IIT_KHARAGPUR_STYLE`)

---

## PART I: PHYSICS

### Q1. Hemispherical Shell with Rim Mass
- **First Observation & Concept**: Equilibrium of rigid bodies, center of mass position, small oscillations.
- **Key Insight**: The center of mass of a thin uniform hemispherical shell lies on its symmetry axis at distance $R/2$ from the geometric center. In equilibrium, the combined center of mass lies vertically directly above the contact point with the floor.
- **Derivation**:
  - Distance of shell CM from center: $z_{\text{shell}} = R/2$ along axis.
  - Rim mass $m$ is at distance $R$ along the rim perpendicular to the symmetry axis.
  - Taking moments about the center or contact point:
    $$M \left(\frac{R}{2} \sin\theta\right) = m (R \cos\theta) \implies \tan\theta = \frac{2m}{M} \implies \theta = \arctan\left(\frac{2m}{M}\right)$$
  - Normal force from floor balances total weight: $N = (M + m)g$.
  - The equilibrium is stable, so small disturbances result in oscillations.
- **Correct Options**: **(A, B, C, D)**.

### Q2. Thermodynamic Non-Standard Cycle
- **First Observation & Concept**: Work done in polytropic and isobaric thermodynamic processes.
- **Key Insight**: $W = \int P\,dV$. For $1 \rightarrow 2$, $P = a V^2 \implies W_{12} = \frac{a}{3}(V_2^3 - V_1^3)$.
- **Derivation**:
  - $W_{23} = P_2 (V_1 - V_2) = -P_2(V_2 - V_1) = -a V_2^2(V_2 - V_1)$.
  - $W_{\text{net}} = W_{12} + W_{23} = \frac{a}{3}(V_2^3 - V_1^3) - a V_2^2(V_2 - V_1)$. (Option C has coefficient $2/3$, hence incorrect).
  - On the PV diagram, process $1 \rightarrow 2$ goes up and right along a parabola, $2 \rightarrow 3$ goes horizontally left at the higher pressure $P_2$, and $3 \rightarrow 1$ goes vertically down at $V_1$. Traversing $1 \rightarrow 2 \rightarrow 3 \rightarrow 1$ is counter-clockwise (refrigeration/heat pump sense). Hence (D) is incorrect.
- **Correct Options**: **(A, B)**.

### Q3. Non-Conducting Charged Slab
- **First Observation & Concept**: Gauss's law with planar symmetry for volume charge density.
- **Key Insight**: Use a cylindrical Gaussian pillbox of cross-sectional area $A$ extending from $-x$ to $+x$.
- **Derivation**:
  - Inside: $2 E A = \frac{\rho (2x A)}{\varepsilon_0} \implies E(x) = \frac{\rho x}{\varepsilon_0}$.
  - Outside: $2 E A = \frac{\rho (2d A)}{\varepsilon_0} \implies E(x) = \frac{\rho d}{\varepsilon_0}$.
  - Potential difference: $V(0) - V(d) = \int_0^d E(x)\,dx = \int_0^d \frac{\rho x}{\varepsilon_0}\,dx = \frac{\rho d^2}{2\varepsilon_0}$.
  - At $x = 0$, $E = 0$, so force on a test charge is zero.
- **Correct Options**: **(A, B, C, D)**.

### Q4. Series LCR Resonant Circuit
- **First Observation & Concept**: AC resonance, bandwidth, quality factor, and impedance frequency response.
- **Key Insight & Derivation**:
  - At resonance, $X_L = X_C \implies \omega_0 = 1/\sqrt{LC}$.
  - Half-power frequencies occur when $Z = \sqrt{2} R$, so $I = I_0 / \sqrt{2}$.
  - Quality factor $Q = \frac{\omega_0}{\Delta\omega} = \frac{\omega_0 L}{R}$.
  - When $\omega \ll \omega_0$, $X_C = \frac{1}{\omega C} \gg X_L = \omega L$, circuit impedance is capacitive.
- **Correct Options**: **(A, B, C, D)**.

### Q5. Finite Nuclear Mass and Positronium
- **First Observation & Concept**: Reduced mass corrections in Bohr model.
- **Key Insight**: $\mu = \frac{m_e M_n}{m_e + M_n} = m_e \left(1 + \frac{m_e}{M_n}\right)^{-1}$.
- **Derivation**:
  - $R_M \propto \mu \implies R_M = R_\infty \left(1 + \frac{m_e}{M_n}\right)^{-1}$.
  - For deuterium, $M_d \approx 2 M_p > M_p$, so $\mu_d > \mu_H$. Transition energies are slightly higher, wavelengths shorter.
  - For positronium, $M_n = m_e \implies \mu = m_e / 2$, so $R_{\text{pos}} = R_\infty / 2$.
- **Correct Options**: **(A, B, C, D)**.

### Q6. Lloyd's Mirror Interference
- **First Observation & Concept**: Wave optics, Lloyd's mirror, path difference, reflection phase change.
- **Key Insight**: Lloyd's mirror introduces a $\pi$ phase shift upon grazing reflection at the mirror surface (denser medium reflection).
- **Derivation**:
  - Central fringe corresponding to zero geometrical path difference has effective path difference $\lambda/2$, hence is dark.
  - Inserting a slab of thickness $t$ adds optical path $(\mu - 1)t$, causing fringe shift towards the slab.
- **Correct Options**: **(A, B, C, D)**.

### Q7. Rolling Up an Incline
- **First Observation & Concept**: Conservation of mechanical energy for rolling without slipping.
- **Derivation**:
  $$E = \frac{1}{2} M v^2 + \frac{1}{2} I \omega^2 = \frac{1}{2} M v^2 \left(1 + \frac{2}{5}\right) = \frac{7}{10} M v^2$$
  At peak height $h$:
  $$M g h = \frac{7}{10} M v^2 \implies h = \frac{7 v^2}{10 g} = \frac{7 \times 49}{10 \times 9.8} = \frac{343}{98} = 3.5\text{ m}$$
- **Answer**: **3.5** (or **3.50**).

### Q8. Carnot Engine Work Done
- **Derivation**:
  $$\eta = 1 - \frac{T_C}{T_H} = 1 - \frac{300}{600} = 0.50$$
  $$W = \eta Q_H = 0.50 \times 2400\text{ J} = 1200\text{ J}$$
- **Answer**: **1200**.

### Q9. Capacitance of Two Spheres
- **Derivation**:
  $$\Delta V = \frac{2Q}{4\pi\varepsilon_0}\left(\frac{1}{r} - \frac{1}{d}\right) \implies C = \frac{2\pi\varepsilon_0}{\frac{1}{r} - \frac{1}{d}} \approx 2\pi\varepsilon_0 r$$
  $$C = \frac{1}{2 \times (9.0 \times 10^9)} \times 0.01 = 0.556\times 10^{-12}\text{ F} = 0.56\text{ pF}$$
- **Answer**: **0.56**.

### Q10. Photoelectric Maximum Speed
- **Derivation**:
  $$E = \frac{hc}{\lambda} = \frac{1240}{280} = 4.429\text{ eV}$$
  $$K_{\max} = 4.429 - 2.30 = 2.129\text{ eV} = 2.129 \times 1.6 \times 10^{-19} = 3.406 \times 10^{-19}\text{ J}$$
  $$v_{\max} = \sqrt{\frac{2 K_{\max}}{m_e}} = \sqrt{\frac{2 \times 3.406 \times 10^{-19}}{9.1 \times 10^{-31}}} = 8.65 \times 10^5\text{ m/s}$$
- **Answer**: **8.65**.

### Q11. Silvered Equiconvex Lens
- **Derivation**:
  $$\frac{1}{f_L} = (1.5 - 1)\left(\frac{1}{20} - \left(-\frac{1}{20}\right)\right) = 0.5 \times \frac{2}{20} = \frac{1}{20} \implies f_L = 20\text{ cm}$$
  $$f_M = \frac{R}{2} = 10\text{ cm}$$
  $$\frac{1}{F} = \frac{2}{f_L} + \frac{1}{f_M} = \frac{2}{20} + \frac{1}{10} = \frac{2}{10} = \frac{1}{5} \implies F = 5\text{ cm}$$
- **Answer**: **5** (or **5.00**).

### Q12. Axial Magnetic Field of Circular Coil
- **Derivation**:
  $$B = \frac{\mu_0 N I r^2}{2(r^2 + x^2)^{3/2}} = \frac{4\pi \times 10^{-7} \times 50 \times 1.0 \times (0.04)^2}{2 \times (0.05)^3} = \frac{4\pi \times 10^{-7} \times 50 \times 0.0016}{2.5 \times 10^{-4}} = 0.40\text{ mT}$$
- **Answer**: **0.40**.

### Q13. Satellite Gravity
- **Derivation**: $g' = g \left(\frac{R_e}{R_e + h}\right)^2 = g \left(\frac{R_e}{2 R_e}\right)^2 = \frac{g}{4} \implies k = 4$.
- **Answer**: **4**.

### Q14. Harmonics in Open Organ Pipe
- **Derivation**: In an open organ pipe, frequencies are $f, 2f, 3f, \dots$. Third harmonic is $3f_1$, ratio is 3.
- **Answer**: **3**.

### Q15. Alpha Decay Count
- **Derivation**: $\Delta A = 238 - 206 = 32$. Each $\alpha$ particle removes 4 units of mass: $N_\alpha = 32 / 4 = 8$.
- **Answer**: **8**.

### Q16. Degrees of Freedom
- **Derivation**: Non-linear triatomic molecule has 3 translational + 3 rotational degrees of freedom = 6.
- **Answer**: **6**.

### Q17. Energy vs Amplitude in SHM
- **Derivation**: $E = \frac{1}{2} k A^2 \implies$ doubling amplitude increases energy by factor of $2^2 = 4$.
- **Answer**: **4**.

### Q18. Maximum Electrons in n = 2 Shell
- **Derivation**: $2n^2 = 2(2^2) = 8$.
- **Answer**: **8**.

---

## PART II: CHEMISTRY

### Q19. Hydrolysis of Propyl Propanoate
- **Analysis**: Ester $A$ hydrolyzes to $B$ (propanoic acid) and $C$ (propan-1-ol). Oxidation of propan-1-ol yields propanoic acid. Acid-catalyzed dehydration of propan-1-ol yields propene.
- **Correct Options**: **(A, B, C, D)**.

### Q20. NO2 - N2O4 Equilibrium
- **Analysis**:
  - Dimerization is exothermic ($\Delta H^\circ < 0$). Cooling shifts equilibrium to $\text{N}_2\text{O}_4$ (colorless), so brown color fades. Statement (A) is false.
  - Increasing pressure shifts towards fewer moles ($\text{N}_2\text{O}_4$). (B) is true.
  - $\text{NO}_2$ has 1 unpaired electron (paramagnetic), $\text{N}_2\text{O}_4$ is diamagnetic. (C) is true.
  - Dimerization pairs the odd electron. (D) is true.
- **Correct Options**: **(B, C, D)**.

### Q21. Gabriel Phthalimide Synthesis
- **Analysis**: All four statements correctly describe the scope, mechanism, and limitations of the Gabriel synthesis.
- **Correct Options**: **(A, B, C, D)**.

### Q22. Isomerism in Octahedral Complexes
- **Analysis**:
  - $[\text{Co}(\text{en})_2\text{Cl}_2]^+$ has cis (chiral/optically active) and trans (achiral).
  - $[\text{Pt}(\text{en})_2\text{Cl}_2]^{2+}$ has cis (chiral) and trans (achiral).
  - $[\text{Cr}(\text{ox})_2\text{Cl}_2]^{3-}$ has cis (chiral) and trans (achiral).
  - $[\text{Co}(\text{NH}_3)_3\text{Cl}_3]$ has fac and mer isomers; both have planes of symmetry (optically inactive).
- **Correct Options**: **(A, B, C)**.

### Q23. Metallurgy of Zinc
- **Analysis**: Roasting, reduction in vertical retort, boiling point condensation, and refining are accurately described.
- **Correct Options**: **(A, B, C, D)**.

### Q24. Adsorption Characteristics
- **Analysis**: Physisorption vs chemisorption fundamentals: reversibility, temperature dependence (activation energy barrier for chemisorption).
- **Correct Options**: **(A, B, C, D)**.

### Q25. Gibbs Free Energy of Lead Storage Cell
- **Derivation**: $\Delta G^\circ = -n F E^\circ = -2 \times 96500 \times 2.05\text{ V} = -395650\text{ J} = -395.7\text{ kJ/mol}$.
- **Answer**: **-395.7**.

### Q26. Enthalpy of Formation of Benzene
- **Derivation**:
  $$\Delta H_c^\circ = 6 \Delta H_f^\circ(\text{CO}_2) + 3 \Delta H_f^\circ(\text{H}_2\text{O}) - \Delta H_f^\circ(\text{C}_6\text{H}_6)$$
  $$-3267 = 6(-393.5) + 3(-285.8) - \Delta H_f^\circ = -3218.4 - \Delta H_f^\circ \implies \Delta H_f^\circ = +48.6\text{ kJ/mol}$$
- **Answer**: **48.6**.

### Q27. Hydrogen Count in Acetone
- **Derivation**: Formula $\text{C}_3\text{H}_6\text{O}$, VD 29 $\implies M = 58$. Does not reduce Tollens' but forms oxime $\implies$ ketone (propan-2-one). Number of H atoms = 6.
- **Answer**: **6**.

### Q28. Common Ion Solubility of AgCl
- **Derivation**:
  $$[\text{Ag}^+] = \frac{K_{sp}}{[\text{Cl}^-]} = \frac{1.8 \times 10^{-10}}{0.05} = 3.6 \times 10^{-9}\text{ M} = 3.6\text{ nmol/L}$$
- **Answer**: **3.6** (or **3.60**).

### Q29. Time for 90% Reaction
- **Derivation**:
  $$t_{90\%} = \frac{\ln(1/0.10)}{k} = \frac{2.303}{0.0231} \approx 99.7 \approx 100\text{ min}$$
- **Answer**: **100**.

### Q30. Molality from Freezing Point Depression
- **Derivation**: $\Delta T_f = K_f m \implies 0.372 = 1.86 \times m \implies m = 0.20\text{ mol/kg}$.
- **Answer**: **0.2** (or **0.20**).

### Q31. Oxidation State of S in Thiosulfate
- **Derivation**: In $\text{Na}_2\text{S}_2\text{O}_3$, $2(+1) + 2x + 3(-2) = 0 \implies 2x = 4 \implies x = 2$.
- **Answer**: **2**.

### Q32. Bridging Carbonyls in Fe2(CO)9
- **Derivation**: $\text{Fe}_2(\text{CO})_9$ contains 3 bridging carbonyls and 6 terminal carbonyls.
- **Answer**: **3**.

### Q33. Basicity of Trimeric Metaphosphoric Acid
- **Derivation**: Cyclic $(HPO_3)_3$ has 3 ionizable P-OH groups, basicity = 3.
- **Answer**: **3**.

### Q34. Coordination Number in BCC
- **Derivation**: Center atom touches 8 corner atoms $\implies$ coordination number = 8.
- **Answer**: **8**.

### Q35. Geometrical Isomers of [Pt(NH3)2(NO2)2]
- **Derivation**: Square planar $[M a_2 b_2]$ has 2 geometrical isomers: cis and trans.
- **Answer**: **2**.

### Q36. Pi Bonds in Naphthalene
- **Derivation**: Naphthalene has 5 conjugated double bonds $\implies$ 5 $\pi$-bonds.
- **Answer**: **5**.

---

## PART III: MATHEMATICS

### Q37. Properties of Rational Function
- **Analysis**: $f(x) = \frac{x^2}{1+x^2} = 1 - \frac{1}{1+x^2}$. Continuous, even, range $[0, 1)$, minimum at $x = 0$, horizontal asymptote $y = 1$.
- **Correct Options**: **(A, B, C, D)**.

### Q38. Ellipse Parameters
- **Analysis**: $\frac{x^2}{9} + \frac{y^2}{4} = 1 \implies a = 3, b = 2$. Major axis = 6, minor axis = 4, $e = \sqrt{1 - 4/9} = \sqrt{5}/3$, latus rectum $= 2b^2/a = 8/3$.
- **Correct Options**: **(A, B, C, D)**.

### Q39. Skew-Symmetric Matrices
- **Analysis**: For $3 \times 3$ skew-symmetric $A$: $\det(A) = 0$, diagonal entries 0, eigenvalues are $0, \pm i\omega$, rank can be 2.
- **Correct Options**: **(A, B, C, D)**.

### Q40. Log-Sine Definite Integrals
- **Analysis**: Standard Euler log-sine integral properties: $I = -\frac{\pi}{2}\ln 2$, $\int_0^\pi \ln(\sin x)\,dx = -\pi\ln 2$, $\int_0^{\pi/2}\ln(\tan x)\,dx = 0$.
- **Correct Options**: **(A, B, C, D)**.

### Q41. Probability Axioms and Rules
- **Analysis**: Addition rule, product rule for independence, conditional probability definition, and complementary probability are standard axioms.
- **Correct Options**: **(A, B, C, D)**.

### Q42. Triangle Vector Identities
- **Analysis**: $\vec{a} + \vec{b} + \vec{c} = \vec{0} \implies \vec{a} \times \vec{b} = \vec{b} \times \vec{c} = \vec{c} \times \vec{a}$, sum is $3(\vec{a} \times \vec{b})$, vectors are coplanar.
- **Correct Options**: **(A, B, C, D)**.

### Q43. Definite Integral
- **Derivation**:
  $$\int_0^2 (x^2 - x)\,dx = \left[\frac{x^3}{3} - \frac{x^2}{2}\right]_0^2 = \frac{8}{3} - 2 = \frac{2}{3} \approx 0.67$$
- **Answer**: **0.67**.

### Q44. Maximum Value of Linear Combination of Sine/Cosine
- **Derivation**: $\max(a\sin x + b\cos x) = \sqrt{a^2 + b^2} = \sqrt{5^2 + 12^2} = 13$.
- **Answer**: **13**.

### Q45. Distance Between Parallel Lines
- **Derivation**: $d = \frac{|c_1 - c_2|}{\sqrt{a^2 + b^2}} = \frac{|-5 - 10|}{\sqrt{3^2 + (-4)^2}} = \frac{15}{5} = 3$.
- **Answer**: **3**.

### Q46. Latus Rectum of Parabola
- **Derivation**: Parabola $y^2 = 4x$ has focal chord perpendicular to axis = latus rectum = $4a = 4(1) = 4$.
- **Answer**: **4**.

### Q47. Sum of Geometric Series
- **Derivation**: $S = \frac{a}{1 - r} = \frac{1}{1 - 1/4} = \frac{4}{3} \approx 1.33$.
- **Answer**: **1.33**.

### Q48. Orthogonal Vectors
- **Derivation**: $\vec{u} \cdot \vec{v} = 2(6) + 3(-k) = 12 - 3k = 0 \implies k = 4$.
- **Answer**: **4**.

### Q49. Permutations of "BALL"
- **Derivation**: $\frac{4!}{2!} = \frac{24}{2} = 12$.
- **Answer**: **12**.

### Q50. Order of Differential Equation
- **Derivation**: Highest derivative is $\frac{d^3 y}{dx^3}$, order is 3.
- **Answer**: **3**.

### Q51. Limit Evaluation
- **Derivation**: $\lim_{x \to 0} \frac{\tan 3x}{x} = 3 \lim_{x \to 0}\frac{\tan 3x}{3x} = 3 \times 1 = 3$.
- **Answer**: **3**.

### Q52. Real Solutions of Absolute Value
- **Derivation**: $|x| = 0 \iff x = 0$. Only 1 real solution.
- **Answer**: **1**.

### Q53. Radius of Circle
- **Derivation**: $x^2 + y^2 = 25 = 5^2 \implies R = 5$.
- **Answer**: **5**.

### Q54. Sum of Roots
- **Derivation**: For $x^2 - 10x + 21 = 0$, sum of roots is $-(-10)/1 = 10$.
- **Answer**: **10**.
