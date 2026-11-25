# Detailed Solutions and Pedagogical Analysis — Mock Examination 06 (Paper 1)
### Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

---

## PART I: PHYSICS

### Q1. Dielectric Wedge Interference
- **First Observation & Concept**: Thin wedge fringe spacing in reflected monochromatic light.
- **Key Insight**: Consecutive bright fringes occur when the optical path difference changes by $\lambda$. The path difference is $\Delta = 2 \mu t + \lambda/2$. The change between consecutive fringes is $2 \mu \Delta t = \lambda$.
- **Derivation**: Since $\Delta t = \beta \tan\alpha \approx \beta \alpha$, we have:
  $$\beta = \frac{\lambda}{2\mu \alpha} = \frac{600 \times 10^{-9}}{2 \times 1.50 \times 1.0 \times 10^{-4}} = \frac{600 \times 10^{-9}}{3.0 \times 10^{-4}} = 2.0 \times 10^{-3}\text{ m} = 2.0\text{ mm}$$
- **Correct Option**: **(B)**.
- **Trap / Distractor**: Forgetting the factor of $\mu$ in the denominator leads to $3.0\text{ mm}$ (C).

### Q2. Photoelectric Maximum Kinetic Energy
- **First Observation & Concept**: Photoelectric equation with multiple spectral components.
- **Key Insight**: $K_{\max}$ is determined exclusively by the highest energy photon present in the beam, i.e., the shortest wavelength $\lambda_1 = 400\text{ nm}$.
- **Derivation**:
  $$E_1 = \frac{hc}{\lambda_1} = \frac{1240}{400} = 3.10\text{ eV}$$
  $$K_{\max} = E_1 - \Phi = 3.10\text{ eV} - 2.40\text{ eV} = 0.70\text{ eV}$$
- **Correct Option**: **(B)**.
- **Trap**: Using $\lambda_2 = 500\text{ nm}$ gives $E_2 = 2.48\text{ eV} \implies K = 0.08\text{ eV}$ (A).

### Q3. Pivoted Rod Vertical Reaction
- **First Observation & Concept**: Work-energy theorem and circular dynamics of rigid bodies.
- **Key Insight**: The center of mass drops by $L/2$. By conservation of energy: $Mg(L/2) = \frac{1}{2} I \omega^2 = \frac{1}{2}(\frac{1}{3}ML^2)\omega^2 \implies \omega^2 = \frac{3g}{L}$.
- **Derivation**: At the vertical position, the centripetal acceleration of the center of mass is $a_c = \omega^2 (L/2) = \frac{3g}{2}$ upwards.
  $$N - Mg = M a_c = M\left(\frac{3g}{2}\right) \implies N = Mg + \frac{3}{2}Mg = \frac{5}{2}Mg$$
- **Correct Option**: **(D)**.

### Q4. Thermodynamic Cycle Net Work
- **First Observation & Concept**: Cyclic PV diagram work calculation.
- **Key Insight**: Net work is the sum of works in each step: isobaric expansion, isochoric cooling, and isothermal compression.
- **Derivation**:
  - Step 1 (Isobaric $P_0$): $W_1 = P_0 (2V_0 - V_0) = P_0 V_0$.
  - Step 2 (Isochoric $2V_0$): $W_2 = 0$.
  - Step 3 (Isothermal from $(P_0/2, 2V_0)$ to $(P_0, V_0)$): Since $PV = (P_0/2)(2V_0) = P_0 V_0 = \text{const}$, $T$ is constant.
    $$W_3 = nRT \ln(V_f/V_i) = P_0 V_0 \ln(V_0 / 2V_0) = -P_0 V_0 \ln 2$$
  - Net work: $W_{\text{net}} = W_1 + W_2 + W_3 = P_0 V_0(1 - \ln 2)$.
- **Correct Option**: **(A)**.

### Q5. Dielectric Insertion Work
- **First Observation & Concept**: Work done by external agent on an isolated capacitor ($Q = \text{const}$).
- **Key Insight**: $W_{\text{ext}} = \Delta U = U_f - U_i = \frac{Q^2}{2 C_f} - \frac{Q^2}{2 C_i}$.
- **Derivation**: Initial capacitance $C_i = \frac{\varepsilon_0 A}{d}$.
  With slab of thickness $d/2$, effective air gap is $d - d/2 = d/2$, and dielectric gap equivalent is $(d/2)/\kappa = d/6$.
  $$d_{\text{eff}} = \frac{d}{2} + \frac{d}{6} = \frac{2d}{3} \implies C_f = \frac{\varepsilon_0 A}{2d/3} = \frac{3\varepsilon_0 A}{2d}$$
  $$W_{\text{ext}} = \frac{Q^2}{2}\left(\frac{2d}{3\varepsilon_0 A} - \frac{d}{\varepsilon_0 A}\right) = \frac{Q^2}{2}\left(-\frac{d}{3\varepsilon_0 A}\right) = -\frac{Q^2 d}{6\varepsilon_0 A}$$
- **Correct Option**: **(A)**.

### Q6. Charge Flow Induced by Rotation
- **First Observation & Concept**: Faraday's law and total induced charge $\Delta q = \frac{\Delta \Phi}{R}$.
- **Key Insight**: Total charge flow depends only on initial and final magnetic flux, independent of the duration $\Delta t$.
- **Derivation**: $\Phi_i = B(\pi r^2)$, $\Phi_f = B(\pi r^2) \cos 180^\circ = -B(\pi r^2)$.
  $$\Delta \Phi = |\Phi_f - \Phi_i| = 2 B \pi r^2 \implies \Delta q = \frac{2\pi r^2 B}{R}$$
- **Correct Option**: **(B)**.

### Q7. Two Blocks Connected by Spring
- **Analysis**:
  - Maximum static friction on $m_1$: $f_{s,\max} = \mu m_1 g = 0.2 \times 2 \times 10 = 4\text{ N}$.
  - Block $m_1$ begins to move when spring force $k x = 4\text{ N} \implies x = 4/200 = 0.02\text{ m}$. Hence (A) and (C) are correct.
  - Work-energy theorem on $m_2$ before $m_1$ moves: $F x_{\max} = \frac{1}{2} k x_{\max}^2 \implies x_{\max} = \frac{2F}{k} = \frac{2 \times 10}{200} = 0.10\text{ m}$. Hence (B) is correct.
  - When $x = 0.03\text{ m}$, spring force on $m_2$ is $k x = 200 \times 0.03 = 6\text{ N}$. Net force on $m_2 = F - kx = 10 - 6 = 4\text{ N}$. Acceleration $a_2 = 4\text{ N} / 1\text{ kg} = 4\text{ m/s}^2$. Hence (D) is correct.
- **Correct Options**: **(A, B, C, D)**.

### Q8. Coaxial Oppositely Charged Rings
- **Analysis**: By symmetry, at midpoint $x = d/2$, potential from $+Q$ is $V_+ = \frac{kQ}{\sqrt{R^2 + (d/2)^2}}$ and from $-Q$ is $V_- = -\frac{kQ}{\sqrt{R^2 + (d/2)^2}}$. Hence $V(d/2) = 0$. (B) and (D) are correct.
- The electric field from $+Q$ points away from the positive ring (towards negative ring), and from $-Q$ points towards the negative ring. Both components point in the same direction $+x$. Thus $\vec{E}$ does NOT vanish at midpoint (A is incorrect; C is correct).
- **Correct Options**: **(B, C, D)**.

### Q9. Series LCR Circuit at $\omega > \omega_0$
- **Analysis**:
  - For $\omega > \omega_0$, $X_L = \omega L > X_C = 1/(\omega C)$. The circuit is inductive; current lags voltage by $\phi \in (0, \pi/2)$. (A is correct).
  - $Z = \sqrt{R^2 + (X_L - X_C)^2} > R$. (B is correct).
  - Inserting dielectric increases $C$, decreasing $X_C$, which makes $(X_L - X_C)$ larger, increasing the phase difference $\phi$. (C is incorrect).
  - Average power $P = I_{\text{rms}}^2 R$, which depends on $Z$ and therefore on $\omega, L, C$. (D is incorrect).
- **Correct Options**: **(A, B)**.

### Q10. Harmonic Central Potential
- **Analysis**: Force $\vec{F} = -\nabla U = -k r \hat{r}$. Centripetal condition: $\frac{m v^2}{R_0} = k R_0 \implies v = R_0 \sqrt{k/m}$. (A is correct).
- Energy $E = K + U = \frac{1}{2} m v^2 + \frac{1}{2} k R_0^2 = \frac{1}{2} k R_0^2 + \frac{1}{2} k R_0^2 = k R_0^2$. (B is correct).
- Period $T = 2\pi R_0 / v = 2\pi \sqrt{m/k}$, independent of $R_0$. (C is correct).
- Angular momentum $L = m v R_0 = m (R_0 \sqrt{k/m}) R_0 = R_0^2 \sqrt{km}$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q11. Particle in 1D Infinite Well
- **Analysis**: $\psi_n(x) = \sqrt{2/a} \sin(n\pi x / a)$, $E_n = \frac{n^2 h^2}{8 m a^2}$.
- For odd $n$, $\sin(n\pi/2) = \pm 1$, so $|\psi|^2$ is maximum at $x = a/2$. (A is correct).
- $E_{n+1} - E_n \propto (n+1)^2 - n^2 = 2n + 1$, which increases linearly with $n$. (B is correct).
- By symmetry, $\langle x \rangle = a/2$ for all stationary states. (C is correct).
- $\lambda_n = 2a/n$ from de Broglie condition $n(\lambda/2) = a$. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q12. Combination of Convex and Concave Lenses
- **Analysis**: Parallel rays incident on $f_1 = 20\text{ cm}$ converge toward a point $20\text{ cm}$ behind the first lens, which is $20 - 10 = 10\text{ cm}$ behind the concave lens. Since $f_2 = -10\text{ cm}$, the rays are aimed directly at the focal point of the concave lens, so they emerge parallel to the axis! (A is correct).
- Combined focal length $\frac{1}{F} = \frac{1}{20} + \frac{1}{-10} - \frac{10}{(20)(-10)} = \frac{1}{20} - \frac{1}{10} + \frac{1}{20} = 0 \implies F = \infty$, Power $= 0$. (B is correct).
- The intermediate image is formed behind the second lens, acting as a virtual object (not real object) for the concave lens. (C is incorrect).
- If $d = 20\text{ cm}$, the rays focus directly on the concave lens, emerging divergent. (D is correct).
- **Correct Options**: **(A, B, D)**.

### Q13–Q18 Numerical Solutions
- **Q13**: Conservation of mechanical energy for rolling solid sphere: $Mgh = \frac{1}{2} M v^2 + \frac{1}{2} I \omega^2 = \frac{7}{10} M v^2 \implies h = \frac{7 v^2}{10 g} = \frac{7 \times 49}{10 \times 9.8} = \frac{343}{98} = 3.5\text{ m}$. **Answer: 3.5 (or 3.50)**.
- **Q14**: Fringe shift $\Delta y = \frac{D}{d}(\mu - 1)t = \frac{1.0}{0.5 \times 10^{-3}}(1.5 - 1)(6.0 \times 10^{-6}) = 2000 \times 0.5 \times 6.0 \times 10^{-6} = 6.0 \times 10^{-3}\text{ m} = 6.0\text{ mm}$. **Answer: 6.0 (or 6)**.
- **Q15**: At $t = 10\text{ h} = 1 T_{1/2}$, $N(10) = N_0 / 2 = 5.0 \times 10^{19}$. At $t = 30\text{ h} = 3 T_{1/2}$, $N(30) = N_0 / 8 = 1.25 \times 10^{19}$. Disintegrations $\Delta N = 5.0 \times 10^{19} - 1.25 \times 10^{19} = 3.75 \times 10^{19}$. Thus $A = 3.75$. **Answer: 3.75**.
- **Q16**: For two distant identical spheres of radius $r$, the potential difference for charges $+Q$ and $-Q$ is $V = \frac{Q}{4\pi\varepsilon_0 r} - \left(-\frac{Q}{4\pi\varepsilon_0 r}\right) = \frac{2Q}{4\pi\varepsilon_0 r}$. Thus $C = \frac{Q}{V} = 2\pi\varepsilon_0 r = \frac{1}{2} (4\pi\varepsilon_0 r) = \frac{0.1}{2 \times 9 \times 10^9} = 5.56 \times 10^{-12}\text{ F} = 5.56\text{ pF}$. **Answer: 5.56**.
- **Q17**: Torricelli's law: $-A \frac{dh}{dt} = a \sqrt{2gh} \implies t = \frac{A}{a}\sqrt{\frac{2H}{g}} = \frac{1.0}{1.0 \times 10^{-4}}\sqrt{\frac{2 \times 1.25}{10}} = 10^4 \times \sqrt{0.25} = 10^4 \times 0.5 = 5000\text{ s}$. **Answer: 5000**.
- **Q18**: Flux $\Phi = \int_{d}^{d+b} \frac{\mu_0 I_1}{2\pi r} a\,dr = \frac{\mu_0 I_1 a}{2\pi} \ln\left(\frac{d+b}{d}\right) = \frac{4\pi \times 10^{-7} \times 10 \times 0.10}{2\pi} \ln\left(\frac{25}{5}\right) = 2 \times 10^{-7} \times \ln 5 = 2 \times 10^{-7} \times 1.61 = 322\text{ nWb}$. **Answer: 322**.

---

## PART II: CHEMISTRY

### Q19. Optical Isomerism & Magnetic Moment
- **Analysis**:
  - $[\text{Ni}(\text{en})_3]^{2+}$ has $\text{Ni}^{2+}$ ($d^8$). In an octahedral field, $d^8$ has $t_{2g}^6 e_g^2$, giving 2 unpaired electrons ($\mu = \sqrt{2(4)} = 2.83\text{ BM}$).
  - Furthermore, tris-chelate complex $[M(AA)_3]^{n+}$ has $D_3$ symmetry without an improper rotation axis ($S_n$), making it chiral and optically active (existing as $\Delta$ and $\Lambda$ enantiomers).
- **Correct Option**: **(B)**.

### Q20. Arrhenius Temperature Dependence
- **Calculation**: $\ln(k_2/k_1) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) = \frac{57600}{8.314}\left(\frac{10}{300 \times 310}\right) = \frac{57600 \times 10}{8.314 \times 93000} \approx 0.745$. $k_2/k_1 = e^{0.745} \approx 2.1 \approx 2.0$.
- **Correct Option**: **(B)**.

### Q21. Macarthur-Forrest Cyanide Extraction
- **Chemistry**: $\text{Ag}_2\text{S} + 4\text{NaCN} + \frac{1}{2}\text{O}_2 + \text{H}_2\text{O} \rightarrow 2\text{Na}[\text{Ag}(\text{CN})_2] + \text{Na}_2\text{SO}_4 + 2\text{NaOH}$. Coordination number of $\text{Ag}$ is 2.
- Then $2[\text{Ag}(\text{CN})_2]^- + \text{Zn} \rightarrow [\text{Zn}(\text{CN})_4]^{2-} + 2\text{Ag}$. Coordination number of $\text{Zn}$ is 4.
- **Correct Option**: **(A)**.

### Q22. Acetal Protection and Hydride Resistance
- **Reaction**: Benzaldehyde $+ 2\text{ MeOH} \xrightarrow{\text{HCl}} \text{PhCH(OMe)}_2$ (dimethyl acetal).
- Acetals are stable to basic reagents and reducing agents like $\text{LiAlH}_4$. Thus $\text{LiAlH}_4$ does not reduce the acetal. Workup regenerates the acetal.
- **Correct Option**: **(B)**.

### Q23. Common Ion Effect on Sparingly Soluble Salt
- **Calculation**: $[X^-] = 0.01\text{ M} = 10^{-2}\text{ M}$.
  $$K_{sp} = [M^{2+}][X^-]^2 \implies 4.0 \times 10^{-12} = s (10^{-2})^2 = s (10^{-4}) \implies s = 4.0 \times 10^{-8}\text{ M}$$
- **Correct Option**: **(B)**.

### Q24. Group 15 Hydride Trends
- **Fact Verification**: Boiling point order: $\text{BiH}_3 > \text{SbH}_3 > \text{NH}_3 > \text{AsH}_3 > \text{PH}_3$. Due to strong intermolecular hydrogen bonding, $\text{NH}_3$ has a much higher boiling point than $\text{PH}_3$. Statement (D) is false and therefore the correct choice.
- **Correct Option**: **(D)**.

### Q25. Acetophenone Identification & Reactions
- **Analysis**: $\text{C}_8\text{H}_8\text{O}$ gives 2,4-DNP and iodoform test $\implies$ methyl ketone $\implies \text{Ph-CO-CH}_3$.
  - Oxidation with alkaline $\text{KMnO}_4$ yields benzoic acid (B).
  - Clemmensen reduction ($\text{Zn-Hg/HCl}$) gives ethylbenzene (C).
  - Oxime formation with $\text{NH}_2\text{OH}$ yields syn- and anti- acetophenone oxime stereoisomers (D).
- **Correct Options**: **(A, B, C, D)**.

### Q26. Crystal Structures of NaCl and CsCl
- **Analysis**:
  - In $\text{NaCl}$, $\text{Na}^+$ ions occupy all octahedral voids of FCC $\text{Cl}^-$, coordination $6:6$. (A and B correct).
  - On heating $\text{CsCl}$ ($8:8$, BCC-like), coordination decreases to $6:6$ ($\text{NaCl}$-type). (C is correct).
  - Radius ratios: $0.414 - 0.732$ for octahedral, $> 0.732$ for cubic. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q27. Electrochemical Cell with Silver Half-Cell
- **Analysis**: Anode: $\frac{1}{2}\text{H}_2 \rightarrow \text{H}^+ + e^-$. Cathode: $\text{Ag}^+ + e^- \rightarrow \text{Ag}$.
  - Overall: $\frac{1}{2}\text{H}_2(1\text{ bar}) + \text{Ag}^+(0.01\text{ M}) \rightarrow \text{H}^+(1\text{ M}) + \text{Ag}(s)$.
  - $Q = \frac{[\text{H}^+]}{[\text{Ag}^+] P_{\text{H}_2}^{1/2}} = \frac{1}{0.01} = 100$. (D is incorrect, $Q = 10^2$).
  - $E_{\text{cell}} = E^\circ - 0.06 \log(100) = 0.80 - 0.06(2) = 0.68\text{ V}$. (A is correct).
  - Increasing $P_{\text{H}_2}$ increases $E_{\text{cell}}$ (B is correct).
  - Adding $\text{NaCl}$ precipitates $\text{AgCl}$, drastically lowering $[\text{Ag}^+]$, decreasing cell potential (C is correct).
- **Correct Options**: **(A, B, C)**.

### Q28. Permanganate and Dichromate Properties
- **Analysis**:
  - Both metal ions are $d^0$ ($\text{Mn}^{7+}$ and $\text{Cr}^{6+}$), hence diamagnetic. (A is correct).
  - Colors are due to LMCT ($O^{2-} \rightarrow M$). (B is correct).
  - In $\text{Cr}_2\text{O}_7^{2-}$, terminal $\text{Cr-O}$ bonds are $163\text{ pm}$ and bridging are $179\text{ pm}$. (C is correct).
  - $2\text{CrO}_4^{2-} + 2\text{H}^+ \rightleftharpoons \text{Cr}_2\text{O}_7^{2-} + \text{H}_2\text{O}$. Acidification yields dichromate. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q29. Qualitative Analysis of Group II
- **Analysis**: All four statements correctly state classical analytical principles of Group II precipitation and separation.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Nucleophilic Substitution Mechanisms
- **Analysis**:
  - 2-bromo-2-methylpropane gives tertiary carbocation $\implies S_N1$, accompanied by racemization and inversion. (A is correct).
  - Neopentyl halides have severe $\beta$-branching hindering back-side attack. (B is correct).
  - Secondary alkyl halide in polar aprotic solvent DMF with strong nucleophile $\text{SH}^-$ proceeds via $S_N2$ with inversion. (C is correct).
  - Resonance-stabilized carbocations and low transition state energy allow allylic/benzylic halides to react via both mechanisms. (D is correct).
- **Correct Options**: **(A, B, C, D)**.

### Q31–Q36 Numerical Solutions
- **Q31**: $[\text{Fe}(\text{H}_2\text{O})_6]^{2+}$: $\text{Fe}^{2+}$ ($d^6$) weak field $\implies 4$ unpaired electrons $\implies \mu_1^2 = 4(4+2) = 24$.
  $[\text{Fe}(\text{CN})_6]^{4-}$: $\text{Fe}^{2+}$ ($d^6$) strong field $\implies t_{2g}^6 e_g^0 \implies 0$ unpaired electrons $\implies \mu_2^2 = 0$.
  $$\mu_1^2 + \mu_2^2 = 24 + 0 = 24$$
  **Answer: 24**.
- **Q32**: Acid added $= 0.02\text{ mol}$.
  $[\text{CH}_3\text{COOH}] = 0.20 + 0.02 = 0.22\text{ M}$. $[\text{CH}_3\text{COO}^-] = 0.20 - 0.02 = 0.18\text{ M}$.
  $$\text{pH} = pK_a + \log\frac{[\text{Salt}]}{[\text{Acid}]} = 4.74 + \log(0.18/0.22) = 4.74 - \log(11/9) = 4.74 - 0.088 = 4.652 \approx 4.65$$
  **Answer: 4.65**.
- **Q33**: For first order, $t_{75\%} = 2 t_{1/2} = 2 \times \frac{\ln 2}{k} = 2 \times \frac{0.693}{6.93 \times 10^{-3}} = 200\text{ s}$. **Answer: 200**.
- **Q34**: Friedel-Crafts: Benzene $\rightarrow$ Acetophenone ($X$). Clemmensen: $X \rightarrow$ Ethylbenzene ($Y$). Free radical bromination: selectively brominates benzylic position $\rightarrow$ (1-bromoethyl)benzene ($Z$, $\text{C}_8\text{H}_9\text{Br}$). Total H atoms $= 9$. **Answer: 9**.
- **Q35**: $\text{CuSO}_4 = 159.5\text{ g/mol}$. Loss of mass $= 4.99 - 3.19 = 1.80\text{ g}$ of $\text{H}_2\text{O}$.
  Moles of $\text{H}_2\text{O} = 1.80 / 18 = 0.10\text{ mol}$. Moles of $\text{CuSO}_4 = 3.19 / 159.5 = 0.02\text{ mol}$.
  $x = 0.10 / 0.02 = 5$. **Answer: 5**.
- **Q36**: Let $p_{\text{CO}} = p$, then $p_{\text{CO}_2} = 5.0 - p$.
  $$K_p = \frac{p_{\text{CO}}^2}{p_{\text{CO}_2}} = \frac{p^2}{5.0 - p} = 4.0 \implies p^2 + 4p - 20 = 0$$
  $$p = \frac{-4 + \sqrt{16 + 80}}{2} = \frac{-4 + \sqrt{96}}{2} = -2 + \sqrt{24} \approx -2 + 4.90 = 2.90\text{ bar}$$
  **Answer: 2.9 (or 2.90)**.

---

## PART III: MATHEMATICS

### Q37. Definite Integral Symmetry
- **Calculation**: $I = \int_{0}^{\pi} \frac{(\pi - x) \sin x}{1 + \cos^2 x}\,dx$.
  $$2I = \pi \int_{0}^{\pi} \frac{\sin x}{1 + \cos^2 x}\,dx = 2\pi \int_{0}^{\pi/2} \frac{\sin x}{1 + \cos^2 x}\,dx = 2\pi [-\arctan(\cos x)]_0^{\pi/2} = 2\pi (0 - (-\pi/4)) = \frac{\pi^2}{2}$$
  $$I = \frac{\pi^2}{4}$$
- **Correct Option**: **(B)**.

### Q38. Determinant and Adjugate Properties
- **Calculation**: $\det(k M) = k^n \det(M)$ for $n \times n$. Here $n = 3$.
  $$\det(2 \text{adj}(3A)) = 2^3 \det(\text{adj}(3A)) = 2^3 [\det(3A)]^{n-1} = 2^3 [3^3 \det(A)]^2 = 2^3 [27 \times 3]^2 = 2^3 [81]^2 = 2^3 (3^4)^2 = 2^3 \times 3^8$$
- **Correct Option**: **(A)**.

### Q39. Shortest Distance Between Skew Lines
- **Calculation**: $\vec{a}_1 = (1, 2, 3)$, $\vec{b}_1 = (2, 3, 4)$. $\vec{a}_2 = (2, 4, 5)$, $\vec{b}_2 = (3, 4, 5)$.
  $$\vec{a}_2 - \vec{a}_1 = (1, 2, 2)$$
  $$\vec{b}_1 \times \vec{b}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 3 & 4 \\ 3 & 4 & 5 \end{vmatrix} = \hat{i}(15 - 16) - \hat{j}(10 - 12) + \hat{k}(8 - 9) = -\hat{i} + 2\hat{j} - \hat{k}$$
  $$|\vec{b}_1 \times \vec{b}_2| = \sqrt{1 + 4 + 1} = \sqrt{6}$$
  $$(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2) = 1(-1) + 2(2) + 2(-1) = -1 + 4 - 2 = 1$$
  $$d = \frac{|1|}{\sqrt{6}} = \frac{1}{\sqrt{6}}$$
- **Correct Option**: **(A)**.

### Q40. Logarithmic Equation Domain & Solutions
- **Analysis**: $\log_2(x^2 - 3x + 2) - \log_2(x - 1) = 2$.
  - Domain requires $x - 1 > 0 \implies x > 1$, and $x^2 - 3x + 2 = (x-1)(x-2) > 0 \implies x > 2$.
  - For $x > 2$: $\log_2\left(\frac{(x-1)(x-2)}{x-1}\right) = \log_2(x - 2) = 2 \implies x - 2 = 4 \implies x = 6$.
  - Sum of roots $= 6$.
- **Correct Option**: **(C)**.

### Q41. Conditional Probability
- **Calculation**: $P(R_1 | R_3) = \frac{P(R_1 \cap R_3)}{P(R_3)}$.
  By symmetry of random draws without replacement, $P(R_3) = P(R_1) = 4/10$.
  $P(R_1 \cap R_3) = P(R_1 \cap R_2 \cap R_3) + P(R_1 \cap B_2 \cap R_3) = \frac{4}{10}\frac{3}{9}\frac{2}{8} + \frac{4}{10}\frac{6}{9}\frac{3}{8} = \frac{24 + 72}{720} = \frac{96}{720} = \frac{4}{30}$.
  $$P(R_1 | R_3) = \frac{4/30}{4/10} = \frac{10}{30} = \frac{1}{3}$$
- **Correct Option**: **(A)**.

### Q42. Parabola and Line Enclosed Area
- **Calculation**: $y = 2x - 4 \implies x = \frac{y + 4}{2}$.
  Intersection with $y^2 = 4x = 4\left(\frac{y+4}{2}\right) = 2y + 8 \implies y^2 - 2y - 8 = 0 \implies (y - 4)(y + 2) = 0$.
  $$A = \int_{-2}^{4} \left(\frac{y + 4}{2} - \frac{y^2}{4}\right)\,dy = \left[\frac{y^2}{4} + 2y - \frac{y^3}{12}\right]_{-2}^{4} = \left(4 + 8 - \frac{16}{3}\right) - \left(1 - 4 + \frac{8}{12}\right) = \frac{20}{3} - \left(-\frac{7}{3}\right) = \frac{27}{3} = 9$$
- **Correct Option**: **(A)**.

### Q43. Strictly Increasing Function Analysis
- **Analysis**: $f'(x) = 3x^2 - 6x + 6 - 2\cos x = 3(x - 1)^2 + 3 - 2\cos x$.
  Since $\cos x \le 1$, $3 - 2\cos x \ge 1 > 0$. Since $3(x-1)^2 \ge 0$, $f'(x) \ge 1 > 0$ for all $x \in \mathbb{R}$.
  Hence $f(x)$ is strictly increasing on $\mathbb{R}$, having exactly one real root.
  $f''(x) = 6x - 6 + 2\sin x = 0 \implies 3(x - 1) = -\sin x$, which has only one intersection (not infinitely many).
- **Correct Options**: **(A, B, C)**.

### Q44. Complex Circle Modulus Bounds
- **Analysis**: $|z - z_0| = r$ with $z_0 = 3 + 4i$, $|z_0| = 5$, $r = 2$.
  - Maximum modulus $M = |z_0| + r = 5 + 2 = 7$.
  - Minimum modulus $m = |z_0| - r = 5 - 2 = 3$.
  - The points of extreme modulus lie on the line joining the origin to $z_0$.
  - Maximum point: $z_{\max} = \frac{M}{|z_0|} z_0 = \frac{7}{5}(3 + 4i)$.
  - Minimum point has the same argument $\theta = \arctan(4/3)$.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Polynomial Functional Equation
- **Analysis**: $P(0) = 0 \implies P(1) = (P(0))^2 + 1 = 1$.
  $P(2) = (P(1))^2 + 1 = 1^2 + 1 = 2$.
  $P(5) = (P(2))^2 + 1 = 2^2 + 1 = 5$.
  Thus $P(x) - x = 0$ has infinitely many solutions $x_0 = 0, x_1 = 1, x_2 = 2, x_3 = 5, \dots$ generated by $x_{k+1} = x_k^2 + 1$.
  Since a non-zero polynomial can only have finitely many roots, $P(x) - x \equiv 0 \implies P(x) = x$.
  Hence $P'(x) = 1$ everywhere.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Coplanar Vectors
- **Analysis**: $[\vec{a} \; \vec{b} \; \vec{c}] = \begin{vmatrix} 1 & 1 & 1 \\ 1 & -1 & 2 \\ x & x-2 & -1 \end{vmatrix} = 1(1 - 2x + 4) - 1(-1 - 2x) + 1(x - 2 + x) = 5 - 2x + 1 + 2x + 2x - 2 = 2x + 4 = 0 \implies x = -2$.
  - Thus $\vec{c} = -2\hat{i} - 4\hat{j} - \hat{k}$.
  - $\vec{c} \cdot \vec{a} = -2 - 4 - 1 = -7 \ne 0$ (C is incorrect).
  - $\vec{c} \cdot \vec{b} = (-2)(1) + (-4)(-1) + (-1)(2) = -2 + 4 - 2 = 0 \ne -8$ (D is incorrect).
- **Correct Options**: **(A, B)**.

### Q47. First Order Linear Differential Equation
- **Analysis**: $\text{IF} = e^{\int \tan x\,dx} = \sec x$.
  $$y \sec x = \int \sec^2 x\,dx = \tan x + C$$
  $y(0) = 0 \implies C = 0 \implies y = \sin x$.
  Maximum value of $\sin x$ is $1$. $\int_{0}^{\pi/2} \sin x\,dx = [-\cos x]_0^{\pi/2} = 1$.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Divisibility of Binomial Coefficients
- **Analysis**: By Lucas' Theorem, $\binom{100}{n}$ in base 5: $100 = 400_5$.
  For any $1 \le n \le 99$, the base-5 digits of $n = (d_2 d_1 d_0)_5$ have either $d_1 > 0$ or $d_0 > 0$.
  Since the corresponding digits of 100 are $0$, by Lucas' theorem $\binom{0}{d_i} = 0$, meaning $\binom{100}{n} \equiv 0 \pmod 5$ for all $1 \le n \le 99$.
  Thus all 99 values are divisible by 5. (A and B correct).
- **Correct Options**: **(A, B)**.

### Q49–Q54 Numerical Solutions
- **Q49**: Riemann sum: $L = \lim_{n\to\infty} \frac{1}{n} \sum_{k=1}^n \frac{1}{1 + (k/n)^2} = \int_{0}^{1} \frac{dx}{1 + x^2} = \frac{\pi}{4} \approx 0.785 \approx 0.79$. **Answer: 0.79**.
- **Q50**: Let $g(x) = 3x^4 - 4x^3 - 12x^2 + 5$.
  $g'(x) = 12x(x^2 - x - 2) = 12x(x - 2)(x + 1)$.
  Critical points: $x = -1, 0, 2$.
  $g(-1) = 3 + 4 - 12 + 5 = 0$ (a root!).
  $g(0) = 5 > 0$ (local max).
  $g(2) = 48 - 32 - 48 + 5 = -27 < 0$ (local min).
  As $x \to \pm\infty$, $g(x) \to +\infty$.
  Roots: at $x = -1$ (multiplicity 2? $g'(-1) = 0$ and $g(-1) = 0$, so $x = -1$ is a double root!), one root in $(0, 2)$, and one root in $(2, \infty)$.
  Total distinct real roots $= 3$ (roots are $-1$, and two positive roots). **Answer: 3**.
- **Q51**: Equation of normal at $(5\cos\theta, 4\sin\theta)$ is $5x\sin\theta - 4y\cos\theta = (25 - 16)\sin\theta\cos\theta = 9\sin\theta\cos\theta$.
  Passing through $(0, 0) \implies 9\sin\theta\cos\theta = 0 \implies \sin\theta = 0$ or $\cos\theta = 0$.
  This gives $\theta = 0, \pi/2, \pi, 3\pi/2$ (the 4 vertices of the ellipse).
  Number of points $= 4$. **Answer: 4**.
- **Q52**: Let $C = \int_{0}^{1} t f(t)\,dt$. Then $f(x) = x + C x = (1 + C)x$.
  $$C = \int_{0}^{1} t (1 + C)t\,dt = (1 + C)\int_{0}^{1} t^2\,dt = \frac{1 + C}{3} \implies 3C = 1 + C \implies C = \frac{1}{2}$$
  $$f(x) = \left(1 + \frac{1}{2}\right)x = \frac{3}{2}x \implies f(2) = \frac{3}{2}(2) = 3$$
  **Answer: 3**.
- **Q53**: A number is divisible by 4 if its last two digits form a multiple of 4.
  Using distinct digits from $\{1, 2, 3, 4, 5, 6\}$:
  Possible 2-digit endings divisible by 4: $12, 16, 24, 32, 36, 52, 56, 64$ (8 pairs).
  For each pair, the first two digits can be chosen from the remaining 4 digits in $4 \times 3 = 12$ ways.
  Total numbers $= 8 \times 12 = 96$. **Answer: 96**.
- **Q54**: Performing row operations: $R_2 \to R_2 - R_1$, $R_3 \to R_3 - R_1$:
  $$\det(M) = \begin{vmatrix} 1 & 1 & 1 \\ 0 & x & 0 \\ 0 & 0 & y \end{vmatrix} = x y = 4 \times 5 = 20$$
  **Answer: 20**.
