# Detailed Solutions and Pedagogical Analysis — Mock Examination 15 (Paper 1)
### Organising Institute Style: IIT Madras (`IIT_MADRAS_STYLE` — 2017 Benchmark)

---

## PART I: PHYSICS

### Q1. Charged Ring with Cosine Distribution
- **First Observation & Concept**: Linear charge density $\lambda(\theta) = \lambda_0 \cos\theta$.
- **Derivation**:
  - Potential at center: $V = \frac{1}{4\pi\varepsilon_0 R} \int_0^{2\pi} \lambda(\theta) R\,d\theta = \frac{\lambda_0}{4\pi\varepsilon_0} \int_0^{2\pi} \cos\theta\,d\theta = 0$.
  - Dipole moment: element $dq = \lambda_0 \cos\theta R\,d\theta$ is at position $(R\cos\theta, R\sin\theta)$.
  - $p_x = \int dq x = \int_0^{2\pi} (\lambda_0 \cos\theta R\,d\theta)(R\cos\theta) = \lambda_0 R^2 \int_0^{2\pi}\cos^2\theta\,d\theta = \pi R^2 \lambda_0$.
  - $p_y = \int dq y = \lambda_0 R^2 \int_0^{2\pi}\cos\theta\sin\theta\,d\theta = 0$.
  - Total dipole moment $p = \pi R^2 \lambda_0$.
- **Correct Option**: **(A)**.

### Q2. Magnetic Field Cancellation
- **First Observation & Concept**: Superposition of magnetic fields at the center of circular loop.
- **Derivation**:
  - $B_{\text{loop}} = \frac{\mu_0 I}{2a}$ (perpendicular to plane).
  - Straight wire is in the plane of the loop. A wire in the same plane produces a magnetic field perpendicular to the plane at the center: $B_{\text{wire}} = \frac{\mu_0 I}{2\pi d}$.
  - For total cancellation: $\frac{\mu_0 I}{2a} = \frac{\mu_0 I}{2\pi d} \implies d = \frac{a}{\pi}$.
- **Correct Option**: **(A)**.

### Q3. Maximum Rate of Magnetic Energy Storage
- **First Observation & Concept**: Magnetic energy $U = \frac{1}{2} L i^2$. Rate of energy storage $P_L = \frac{dU}{dt} = L i \frac{di}{dt}$.
- **Derivation**:
  - In $RL$ circuit: $i(t) = \frac{\mathcal{E}}{R}(1 - e^{-t/\tau})$ where $\tau = L/R$.
  - $\frac{di}{dt} = \frac{\mathcal{E}}{L} e^{-t/\tau}$.
  - $P_L(t) = L \left[\frac{\mathcal{E}}{R}(1 - e^{-t/\tau})\right] \left[\frac{\mathcal{E}}{L} e^{-t/\tau}\right] = \frac{\mathcal{E}^2}{R} (e^{-t/\tau} - e^{-2t/\tau})$.
  - Maximize $f(u) = u - u^2$ where $u = e^{-t/\tau}$: maximum occurs when $u = 1/2$.
  - $e^{-t/\tau} = 1/2 \implies t = \tau \ln 2 = \frac{L}{R} \ln 2$.
- **Correct Option**: **(A)**.

### Q4. Induced Charge on Grounded Sphere
- **First Observation & Concept**: Method of image charges for grounded conducting sphere.
- **Derivation**:
  - Image charge $q' = -q \frac{R}{d}$ placed at distance $d' = \frac{R^2}{d}$ from center.
  - The total charge induced on the grounded sphere equals the magnitude of the image charge: $q_{\text{ind}} = q' = -q \frac{R}{d}$.
- **Correct Option**: **(A)**.

### Q5. Lens in Liquid Medium
- **First Observation & Concept**: Lens maker's formula $\frac{1}{f} = \left(\frac{\mu}{\mu_m} - 1\right)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$.
- **Derivation**:
  - In air: $\frac{1}{20} = (1.50 - 1) K = 0.50 K \implies K = \frac{1}{10}$.
  - In liquid: $\frac{1}{f'} = \left(\frac{1.50}{1.25} - 1\right) K = (1.20 - 1) \times \frac{1}{10} = 0.20 \times \frac{1}{10} = \frac{1}{50}$.
  - $f' = 50\text{ cm}$.
- **Correct Option**: **(A)**.

### Q6. Velocity Selector
- **First Observation & Concept**: Lorentz force $\vec{F} = q(\vec{E} + \vec{v} \times \vec{B}) = \vec{0}$.
- **Derivation**:
  - $\vec{v} \times \vec{B} = (v_0 \hat{i}) \times (B_0 \hat{k}) = -v_0 B_0 \hat{j}$.
  - Total force: $q (E_0 \hat{j} - v_0 B_0 \hat{j}) = \vec{0} \implies v_0 = E_0 / B_0$.
- **Correct Option**: **(A)**.

### Q7. Falling Loop in Magnetic Field
- **Analysis**:
  - Flux into page increases downwards, induced current creates field out of page $\implies$ counter-clockwise. (A is True)
  - Upward magnetic force: $F = I L B_0 = \left(\frac{B_0 L v}{R}\right) L B_0 = \frac{B_0^2 L^2 v}{R}$. (B is True)
  - Terminal velocity: $m g = \frac{B_0^2 L^2 v_t}{R} \implies v_t = \frac{m g R}{B_0^2 L^2}$. (C is True)
  - Energy conservation at terminal velocity: $P_{\text{Joule}} = I^2 R = \frac{B_0^2 L^2 v_t^2}{R} = (m g) v_t$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q8. Spherical Capacitor
- **Analysis**:
  - $V = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{a} - \frac{1}{b}\right) \implies C = 4\pi\varepsilon_0 \frac{ab}{b-a}$. (A is True)
  - $U = \frac{Q^2}{2C} = \frac{Q^2(b - a)}{8\pi\varepsilon_0 ab}$. (B is True)
  - When $b \to \infty$, $C \to 4\pi\varepsilon_0 a$. (C is True)
  - Gauss's law shows $E = 0$ for $r < a$ and $r > b$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q9. LCR Series AC Resonance
- **Analysis**:
  - At resonance $X_L = X_C$, $Z = R$. (A is True)
  - Inductor voltage leads current by $\pi/2$. (B is True)
  - Capacitor voltage lags current by $\pi/2$. (C is True)
  - Since $v_L(t)$ and $v_C(t)$ are $\pi$ out of phase and have equal amplitudes at resonance, $v_L(t) + v_C(t) = 0$ at all times. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q10. Electromagnetic Wave Properties
- **Analysis**:
  - In free space, $\vec{E}$ and $\vec{B}$ are in phase. (A is True)
  - $E_0 / B_0 = c = 1/\sqrt{\mu_0 \varepsilon_0}$. (B is True)
  - $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$ along $+x$. (C is True)
  - Equipartition of energy: $\langle u_E \rangle = \langle u_B \rangle = \frac{1}{4}\varepsilon_0 E_0^2$. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q11. Inverse-Cube Force
- **Analysis**:
  - Central force $\implies$ angular momentum $L$ conserved. (A is True)
  - For circular orbit: $\frac{m v^2}{r_0} = \frac{k}{r_0^3} \implies m v^2 = \frac{k}{r_0^2} \implies E_k = \frac{1}{2} m v^2 = \frac{k}{2 r_0^2}$. (B is True)
  - Potential energy: $V(r) = -\int F\,dr = -\int (-\frac{k}{r^3})\,dr = -\frac{k}{2r^2}$.
    Total energy $E = E_k + V = \frac{k}{2r_0^2} - \frac{k}{2r_0^2} = 0$. (C is True)
  - Effective potential $V_{\text{eff}}(r) = \frac{L^2}{2m r^2} - \frac{k}{2r^2} = \frac{L^2 - mk}{2m r^2}$, which has no local minimum, orbit is unstable. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q12. Photoelectric Fundamentals
- **Analysis**: All four statements are core experimental facts of the photoelectric effect.
- **Correct Options**: **(A, B, C, D)**.

### Q13. Work Done in Inserting Dielectric
- **Derivation**:
  - Initial energy: $U_i = \frac{1}{2} C_0 V_0^2 = \frac{1}{2} (10.0 \times 10^{-6}) (100)^2 = 0.050\text{ J} = 50.0\text{ mJ}$.
  - Charge $Q = C_0 V_0 = 10.0 \times 10^{-6} \times 100 = 1.0 \times 10^{-3}\text{ C}$.
  - After dielectric insertion: $C = K C_0 = 50.0\,\mu\text{F}$.
  - Final energy: $U_f = \frac{Q^2}{2C} = \frac{U_i}{K} = \frac{50.0}{5} = 10.0\text{ mJ}$.
  - Energy released / work done magnitude $= U_i - U_f = 40.0\text{ mJ}$.
- **Answer**: **40.0** (or **40**).

### Q14. Stored Magnetic Energy in Solenoid
- **Derivation**:
  - Inductance $L = \mu_0 n^2 A l = \mu_0 \left(\frac{N}{l}\right)^2 (\pi r^2) l = \mu_0 \frac{N^2}{l} \pi r^2$.
  - $L = (4\pi \times 10^{-7}) \times \frac{10^6}{1.0} \times 3.14 \times (0.02)^2 = 4\pi \times 10^{-1} \times 3.14 \times 4 \times 10^{-4} = 1.256 \times 1.256 \times 10^{-3} = 1.579 \times 10^{-3}\text{ H} = 1.58\text{ mH}$.
  - Energy $U = \frac{1}{2} L I^2 = \frac{1}{2} \times 1.579 \times 10^{-3} \times (2.0)^2 = 2 \times 1.579 \approx 3.16 \approx 3.2\text{ mJ}$.
- **Answer**: **3.2**.

### Q15. Rotating Rod
- **Derivation**:
  - Loss in PE $= M g \frac{L}{2}$.
  - Gain in rotational KE $= \frac{1}{2} I \omega^2 = \frac{1}{2} \left(\frac{1}{3} M L^2\right) \omega^2 = \frac{1}{6} M L^2 \omega^2$.
  - $\frac{1}{6} M L^2 \omega^2 = M g \frac{L}{2} \implies \omega = \sqrt{\frac{3g}{L}} = \sqrt{\frac{3 \times 9.8}{1.0}} = \sqrt{29.4} \approx 5.42\text{ rad/s}$.
- **Answer**: **5.42**.

### Q16. Intensity in YDSE
- **Derivation**:
  - Phase difference $\phi = \frac{2\pi}{\lambda} \Delta x = \frac{2\pi}{\lambda} \frac{\lambda}{6} = \frac{\pi}{3}$.
  - $I = I_0 \cos^2(\phi/2) = I_0 \cos^2(\pi/6) = I_0 \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{3}{4} I_0 = 0.75 I_0$.
  - $k = 0.75$.
- **Answer**: **0.75**.

### Q17. Doppler Beat Frequency
- **Derivation**:
  - Direct sound heard by observer behind receding car:
    $$f_1 = f \frac{v}{v + u} = 400 \times \frac{340}{340 + 20} = 400 \times \frac{340}{360} = 377.78\text{ Hz}$$
  - Reflected sound from stationary wall: wall receives $f_{\text{wall}} = f \frac{v}{v - u} = 400 \times \frac{340}{340 - 20} = 400 \times \frac{340}{320} = 425.0\text{ Hz}$.
  - Reflected back to stationary observer: $f_2 = f_{\text{wall}} = 425.0\text{ Hz}$.
  - Beat frequency $\Delta f = f_2 - f_1 = 425.0 - 377.78 = 47.22 \approx 47.2\text{ Hz}$.
- **Answer**: **47.2**.

### Q18. Radioactive Activity in Curies
- **Derivation**:
  - Decay constant $\lambda = \frac{\ln 2}{T_{1/2}} = \frac{0.693}{10.0 \times 86400\text{ s}} = \frac{0.693}{8.64 \times 10^5} = 8.021 \times 10^{-7}\text{ s}^{-1}$.
  - $A_0 = \lambda N_0 = 8.021 \times 10^{-7} \times 1.0 \times 10^{20} = 8.021 \times 10^{13}\text{ Bq}$.
  - In Curies: $A_0 = \frac{8.021 \times 10^{13}}{3.7 \times 10^{10}} \approx 2167.8$ Ci.
  - Wait, let's check: $N_0 = 10^{20} \implies 2167.84$ Ci.
- **Answer**: **2167.84** (or **2168**).

---

## PART II: CHEMISTRY

### Q19. Cell Potential Calculation
- **Analysis**:
  - Cell reaction: $\frac{1}{2}\text{H}_2(g) + \text{AgCl}(s) \rightarrow \text{H}^+(aq) + \text{Cl}^-(aq) + \text{Ag}(s)$.
  - $Q = [\text{H}^+][\text{Cl}^-] = (0.01)(0.01) = 10^{-4}$.
  - $E = E^\circ - \frac{0.0591}{1}\log_{10}(10^{-4}) = 0.222 - 0.0591(-4) = 0.222 + 0.2364 = 0.458\text{ V}$.
- **Correct Option**: **(D)** (Wait, in question options (A) 0.340, (B) 0.222, (C) 0.104, (D) 0.458 $\implies$ D).

### Q20. CFSE of High-Spin d7 Octahedral
- **Analysis**:
  - Electron configuration: $t_{2g}^5 e_g^2$.
  - $\text{CFSE} = 5(-0.4\Delta_o) + 2(+0.6\Delta_o) = -2.0\Delta_o + 1.2\Delta_o = -0.8\Delta_o$.
- **Correct Option**: **(A)**.

### Q21. Iodoform Reaction
- **Analysis**:
  - Iodoform requires $\text{CH}_3\text{CH(OH)}-$ or $\text{CH}_3\text{C}(=\text{O})-$.
  - Butan-2-ol has $\text{CH}_3\text{CH(OH)}-\text{CH}_2\text{CH}_3$, so it gives a positive iodoform test.
- **Correct Option**: **(A)**.

### Q22. Thermal Stability of Alkaline Earth Carbonates
- **Analysis**:
  - Smaller cations have high charge density and strongly polarize the large $\text{CO}_3^{2-}$ anion, weakening the $\text{C}-\text{O}$ bond. Down the group, ionic radius increases, polarizing power decreases, stability increases.
- **Correct Option**: **(A)**.

### Q23. Time for First-Order Decomposition
- **Analysis**:
  - Fraction remaining: $\frac{0.05}{0.40} = \frac{1}{8} = \left(\frac{1}{2}\right)^3 \implies 3$ half-lives.
  - $t_{1/2} = \frac{0.693}{k} = \frac{0.693}{6.93 \times 10^{-3}} = 100\text{ s}$.
  - Total time $= 3 \times 100 = 300\text{ s}$.
- **Correct Option**: **(A)**.

### Q24. Stoichiometry of Iodometric Titration
- **Analysis**:
  - $\text{Cr}_2\text{O}_7^{2-} + 14\text{H}^+ + 6\text{I}^- \rightarrow 2\text{Cr}^{3+} + 3\text{I}_2 + 7\text{H}_2\text{O}$.
  - $3\text{I}_2 + 6\text{S}_2\text{O}_3^{2-} \rightarrow 6\text{I}^- + 3\text{S}_4\text{O}_6^{2-}$.
  - 1 mole of $\text{Cr}_2\text{O}_7^{2-}$ produces 3 moles of $\text{I}_2$, which reacts with 6 moles of $\text{S}_2\text{O}_3^{2-}$.
  - Ratio is $1 : 6$.
- **Correct Option**: **(A)**.

### Q25. Kohlrausch Law and Conductance
- **Analysis**: All four statements correctly state electrochemical principles of ionic conductivity.
- **Correct Options**: **(A, B, C, D)**.

### Q26. Stereoisomerism in Complexes
- **Analysis**: All four statements accurately describe chiral octahedral vs square planar isomers.
- **Correct Options**: **(A, B, C, D)**.

### Q27. Cannizzaro Reaction
- **Analysis**: Mechanism, hydride transfer as RDS, and crossed Cannizzaro selectivity are all correctly presented.
- **Correct Options**: **(A, B, C, D)**.

### Q28. Metallurgy of Iron
- **Analysis**: Blast furnace chemistry, zones, flux/slag reactions, pig iron and cast iron characteristics are correct.
- **Correct Options**: **(A, B, C, D)**.

### Q29. Thermodynamics of Equilibrium
- **Analysis**: Equilibrium conditions ($\Delta G = 0$), Trouton's rule, temperature dependence of spontaneity and equilibrium constant are standard laws.
- **Correct Options**: **(A, B, C, D)**.

### Q30. Qualitative Anion Analysis
- **Analysis**: $\text{BaSO}_4$ precipitate, brown ring complex $[\text{Fe}(\text{H}_2\text{O})_5(\text{NO})]^{2+}$ ($+1$ oxidation state of Fe), and purple nitroprusside sulfide complex are exact qualitative tests.
- **Correct Options**: **(A, B, C, D)**.

### Q31. Standard Reduction Potential Fe3+/Fe
- **Derivation**:
  - $\text{Fe}^{3+} + e^- \rightarrow \text{Fe}^{2+}\quad (\Delta G_1^\circ = -1 F E_1^\circ = -0.77 F)$
  - $\text{Fe}^{2+} + 2e^- \rightarrow \text{Fe}\quad (\Delta G_2^\circ = -2 F E_2^\circ = -2(-0.44)F = +0.88 F)$
  - $\text{Fe}^{3+} + 3e^- \rightarrow \text{Fe}\quad (\Delta G_3^\circ = \Delta G_1^\circ + \Delta G_2^\circ = -0.77 F + 0.88 F = +0.11 F)$
  - $-3 F E_3^\circ = +0.11 F \implies E_3^\circ = -\frac{0.11}{3} = -0.037 \approx -0.04\text{ V}$.
- **Answer**: **-0.04**.

### Q32. Acetate Buffer pH
- **Derivation**:
  $$\text{pH} = \text{p}K_a + \log_{10}\left(\frac{[\text{Salt}]}{[\text{Acid}]}\right) = (5 - \log_{10} 1.8) + \log_{10}(1) = 5 - 0.255 = 4.745 \approx 4.75$$
- **Answer**: **4.75**.

### Q33. Molar Mass of FCC Metal
- **Derivation**:
  - $a = 400\text{ pm} = 4.0 \times 10^{-8}\text{ cm}$.
  - $V = a^3 = 6.4 \times 10^{-23}\text{ cm}^3$.
  - In FCC, $Z = 4$.
  - $\rho = \frac{Z M}{N_A V} \implies 10.0 = \frac{4 M}{6.02 \times 10^{23} \times 6.4 \times 10^{-23}} = \frac{4 M}{38.53} \implies M = \frac{385.3}{4} \approx 96.3\text{ g/mol}$.
- **Answer**: **96.3**.

### Q34. Overall Order of Reaction
- **Derivation**:
  - Exponents in rate law: $2 + (-1) = 1$.
  - Overall order = 1.
- **Answer**: **1**.

### Q35. Molarity from Osmotic Pressure
- **Derivation**:
  $$\Pi = C R T \implies C = \frac{4.92}{0.0821 \times 300} = \frac{4.92}{24.63} = 0.20\text{ M}$$
- **Answer**: **0.20** (or **0.2**).

### Q36. Common Ion Solubility
- **Derivation**:
  - $K_{sp} = (1.0 \times 10^{-5})^2 = 1.0 \times 10^{-10}$.
  - In $0.010\text{ M } \text{BaCl}_2$, $[\text{Ba}^{2+}] = 0.010\text{ M}$.
  - $s = \frac{K_{sp}}{[\text{Ba}^{2+}]} = \frac{1.0 \times 10^{-10}}{0.010} = 1.0 \times 10^{-8}\text{ M}$.
  - $k = 1.0$.
- **Answer**: **1** (or **1.0**).

---

## PART III: MATHEMATICS

### Q37. Locus of Complex Number
- **Derivation**:
  - $|z - 2| + |z + 2| = 6$ represents an ellipse with foci at $(\pm 2, 0)$ and major axis $2a = 6 \implies a = 3$.
  - Foci distance $2c = 4 \implies c = 2$.
  - Eccentricity $e = c/a = 2/3$.
- **Correct Option**: **(A)**.

### Q38. Definite Integral
- **Derivation**:
  - Let $I = \int_0^{\pi/2} \frac{\cos x}{1 + \sin x + \cos x}\,dx$.
  - By King's property: $I = \int_0^{\pi/2} \frac{\sin x}{1 + \cos x + \sin x}\,dx$.
  - $2I = \int_0^{\pi/2} \frac{\sin x + \cos x}{1 + \sin x + \cos x}\,dx = \int_0^{\pi/2} \left(1 - \frac{1}{1 + \sin x + \cos x}\right)\,dx = \frac{\pi}{2} - \int_0^{\pi/2}\frac{dx}{1+\sin x+\cos x}$.
  - For $J = \int_0^{\pi/2}\frac{dx}{1+\sin x+\cos x}$: substitute $t = \tan(x/2)$:
    $$J = \int_0^1 \frac{\frac{2\,dt}{1+t^2}}{1 + \frac{2t}{1+t^2} + \frac{1-t^2}{1+t^2}} = \int_0^1 \frac{2\,dt}{2 + 2t} = \int_0^1 \frac{dt}{1+t} = \ln 2$$
  - $2I = \frac{\pi}{2} - \ln 2 \implies I = \frac{\pi}{4} - \frac{1}{2}\ln 2$.
- **Correct Option**: **(A)**.

### Q39. Normal to Rectangular Hyperbola
- **Derivation**:
  - Equation: $y = c^2/x \implies \frac{dy}{dx} = -\frac{c^2}{x^2} = -\frac{1}{t^2}$.
  - Normal slope $m = t^2$.
  - Equation of normal at $(ct, c/t)$: $y - \frac{c}{t} = t^2 (x - ct) \implies y = t^2 x - c t^3 + \frac{c}{t}$.
  - Intersection with curve $xy = c^2$: substitute $x = ct', y = c/t'$:
    $$\frac{c}{t'} = t^2 (ct') - c t^3 + \frac{c}{t} \implies \frac{1}{t'} - \frac{1}{t} = t^2(t' - t) \implies \frac{t - t'}{t t'} = t^2(t' - t)$$
  - Since $t' \ne t$: $-\frac{1}{t t'} = t^2 \implies t' = -\frac{1}{t^3}$.
- **Correct Option**: **(A)**.

### Q40. Linear Differential Equation
- **Derivation**:
  - Integrating factor: $\text{IF} = e^{\int \tan x\,dx} = e^{\ln|\sec x|} = \sec x$.
  - Solution: $y \sec x = \int \sec x \sec x\,dx = \int \sec^2 x\,dx = \tan x + C$.
  - $y = \sin x + C \cos x$.
- **Correct Option**: **(A)**.

### Q41. Permutation with Grouping
- **Derivation**:
  - "PERMUTATION": 11 letters: P, E, R, M, U, T, A, T, I, O, N.
  - Vowels: E, U, A, I, O (5 vowels, all distinct).
  - Consonants: P, R, M, T, T, N (6 consonants, with two T's).
  - Treat the 5 vowels as a single block: total items $= 6 + 1 = 7$ items.
  - Number of arrangements of items $= \frac{7!}{2!}$.
  - Number of arrangements of vowels within block $= 5!$.
  - Total $= 5! \times \frac{7!}{2!}$.
- **Correct Option**: **(A)**.

### Q42. Direction Cosines
- **Derivation**:
  - $n = -(l + m) \implies n^2 = (l + m)^2 = l^2 + 2lm + m^2$.
  - Given $l^2 + m^2 - n^2 = 0 \implies l^2 + m^2 - (l^2 + 2lm + m^2) = -2lm = 0 \implies lm = 0$.
  - Case 1: $l = 0 \implies n = -m$. Direction cosines: $(0, 1, -1) / \sqrt{2}$.
  - Case 2: $m = 0 \implies n = -l$. Direction cosines: $(1, 0, -1) / \sqrt{2}$.
  - Angle: $\cos\theta = 0(1) + 1(0) + (-1)(-1) / (\sqrt{2} \times \sqrt{2}) = 1/2 \implies \theta = \pi/3$.
- **Correct Option**: **(A)**.

### Q43. Cubic Function Analysis
- **Analysis**:
  - $f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3)$. Local max at $x = 1$, local min at $x = 3$. (A, B are True)
  - $f''(x) = 6x - 12 = 0 \implies x = 2$. $f(2) = 8 - 24 + 18 + 1 = 3$. Point of inflection is $(2, 3)$. (C is True)
  - $f(1) = 1 - 6 + 9 + 1 = 5 > 0$, $f(3) = 27 - 54 + 27 + 1 = 1 > 0$. Since local minimum is positive, curve crosses x-axis only once $\implies$ exactly one real root. (D is True)
- **Correct Options**: **(A, B, C, D)**.

### Q44. Confocal Conics
- **Analysis**: All four properties are classic theorems of confocal conics.
- **Correct Options**: **(A, B, C, D)**.

### Q45. Real Symmetric Matrices
- **Analysis**: Spectral theorem for real symmetric matrices: real eigenvalues, orthogonal eigenvectors, orthogonal diagonalizability, determinant is product of eigenvalues.
- **Correct Options**: **(A, B, C, D)**.

### Q46. Reciprocal Vector System
- **Analysis**: Fundamental identities of reciprocal basis vectors in $\mathbb{R}^3$.
- **Correct Options**: **(A, B, C, D)**.

### Q47. Complex Exponential Function
- **Analysis**: Standard analytic properties of $e^z = e^x(\cos y + i\sin y)$.
- **Correct Options**: **(A, B, C, D)**.

### Q48. Binomial Distribution
- **Analysis**: Mean $np$, variance $np(1-p)$, variance $< np$ since $0 < p < 1$, maximum variance at $p = 1/2$.
- **Correct Options**: **(A, B, C, D)**.

### Q49. Standard Limit
- **Derivation**:
  $$\lim_{x \to 0} \frac{x - (x - x^3/6 + \dots)}{x^3} = \frac{1}{6} \approx 0.167$$
- **Answer**: **0.167**.

### Q50. Area Between Parabola and Line
- **Derivation**:
  - Intersections: $(2x)^2 = 4x \implies 4x^2 - 4x = 0 \implies x = 0, 1$.
  - Area $= \int_0^1 (\sqrt{4x} - 2x)\,dx = \left[2 \frac{x^{3/2}}{3/2} - x^2\right]_0^1 = \frac{4}{3} - 1 = \frac{1}{3} \approx 0.33$.
- **Answer**: **0.33**.

### Q51. Standard Integral
- **Derivation**:
  $$\int_0^1 \frac{dx}{1 + x^2} = [\arctan x]_0^1 = \frac{\pi}{4} \implies k = 4$$
- **Answer**: **4**.

### Q52. Circumradius of Right-Angled Triangle
- **Derivation**:
  - $3-4-5$ triangle is right-angled. The hypotenuse is the diameter of the circumcircle: $2R = 5 \implies R = 2.5\text{ cm}$.
- **Answer**: **2.5** (or **2.50**).

### Q53. Number of Solutions
- **Derivation**:
  - $2\sin^2 x - 3\sin x + 1 = 0 \implies (2\sin x - 1)(\sin x - 1) = 0$.
  - $\sin x = 1/2 \implies x = \pi/6, 5\pi/6$ (2 solutions).
  - $\sin x = 1 \implies x = \pi/2$ (1 solution).
  - Total solutions in $[0, 2\pi]$ is $2 + 1 = 3$.
- **Answer**: **3**.

### Q54. Determinant of Matrix Power
- **Derivation**:
  - $\det(A) = 2(2) - 1(1) = 4 - 1 = 3$.
  - $\det(A^3) = (\det A)^3 = 3^3 = 27$.
- **Answer**: **27**.
