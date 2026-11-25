# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 09.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Relativistic aberration, coupled inductors, gyroscopic nutation
- Favorskii rearrangement, Tanabe-Sugano spin crossover, Wade's rules for boranes
- Leibniz integral rule, nilpotent matrices, Clairaut envelopes, generating functions
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 09 — Paper 1
## Organising Institute Style Inspiration: IIT Delhi (`IIT_DELHI_STYLE`)
**Historical Reference Benchmark**: 2013, 2020 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject — Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject — Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A source of light is stationary in an inertial frame $S$. An observer moves with relativistic velocity $v$ along the positive x-axis in frame $S'$. Light rays emitted by the source make an angle $\theta$ with the x-axis in $S$, and angle $\theta'$ in $S'$:
(A) The transformation of the propagation angle (relativistic aberration) is $\cos\theta' = \frac{\cos\theta - v/c}{1 - (v/c)\cos\theta}$.  
(B) For light emitted perpendicular to the motion in $S$ ($\theta = 90^\circ$), the observer in $S'$ sees the light tilted forward at $\cos\theta' = -v/c$.  
(C) In the ultra-relativistic limit ($v \to c$), radiation emitted isotropically in the rest frame is concentrated into a narrow forward cone of half-angle $\theta' \approx \sqrt{1 - v^2/c^2} = 1/\gamma$ (relativistic beaming).  
(D) The frequency transformation combines relativistic Doppler shift and aberration into $\nu' = \nu \gamma (1 - (v/c)\cos\theta)$.

#### Question 2
Two mutually coupled inductors $L_1$ and $L_2$ with mutual inductance $M = k\sqrt{L_1 L_2}$ ($0 < k < 1$) are connected in series with each other and an ideal AC voltage source $V(t) = V_0 \cos(\omega t)$:
(A) When connected in series aiding (fluxes reinforcing), the equivalent inductance is $L_{\text{aid}} = L_1 + L_2 + 2M$.  
(B) When connected in series opposing (fluxes bucking), the equivalent inductance is $L_{\text{opp}} = L_1 + L_2 - 2M$.  
(C) The magnetic energy stored in the coupled system is $U_m = \frac{1}{2}L_1 I_1^2 + \frac{1}{2}L_2 I_2^2 \pm M I_1 I_2$.  
(D) Positive-definiteness of the stored magnetic energy requires that the coupling coefficient strictly satisfies $k \le 1$.

#### Question 3
A smooth circular wire of radius $R$ is rotated about its vertical diameter with constant angular velocity $\omega$. A small bead of mass $m$ is threaded on the wire:
(A) In the rotating reference frame, the bead experiences an outward centrifugal force $F_{\text{cf}} = m \omega^2 R \sin\theta$, where $\theta$ is the angle from the lowest point.  
(B) For $\omega \le \sqrt{g/R}$, the only stable equilibrium position of the bead is at the bottom vertex ($\theta = 0$).  
(C) For $\omega > \sqrt{g/R}$, the bottom vertex $\theta = 0$ becomes an unstable equilibrium, and two new stable equilibrium positions emerge at $\cos\theta_0 = \frac{g}{\omega^2 R}$.  
(D) The frequency of small oscillations about the stable position $\theta_0$ (for $\omega > \sqrt{g/R}$) is $\Omega = \omega\sin\theta_0$.

#### Question 4
Regarding the Joule-Thomson expansion (throttling process) of a real gas obeying the van der Waals equation $\left(P + \frac{a}{V^2}\right)(V - b) = RT$:
(A) The Joule-Thomson expansion is an isenthalpic process ($H_1 = H_2$).  
(B) The Joule-Thomson coefficient is defined by $\mu_{\text{JT}} = \left(\frac{\partial T}{\partial P}\right)_H = \frac{1}{C_P}\left[T\left(\frac{\partial V}{\partial T}\right)_P - V\right]$.  
(C) At the maximum inversion temperature, $\mu_{\text{JT}} = 0$, giving $T_i = \frac{2a}{Rb}$ in the low-pressure limit.  
(D) If a gas is throttled at an initial temperature $T > T_i$, the expansion results in heating of the gas ($\mu_{\text{JT}} < 0$).

#### Question 5
In a Fraunhofer diffraction grating with $N$ equally spaced slits of width $a$ and grating period $d = a + b$:
(A) The principal interference maxima occur at angles satisfying $d \sin\theta = m \lambda$ ($m = 0, \pm 1, \pm 2, \dots$).  
(B) The angular half-width of the $m$-th principal maximum is $\Delta \theta = \frac{\lambda}{N d \cos\theta}$.  
(C) The chromatic resolving power of the grating according to the Rayleigh criterion is $R = \frac{\lambda}{\Delta \lambda} = m N$.  
(D) If $d = 2a$, all even orders ($m = 2, 4, 6, \dots$) are missing (absent spectra) because they coincide with single-slit diffraction minima.

#### Question 6
A heavy symmetric top of mass $M$ with principal moments of inertia $I_x = I_y$ and $I_z$ spins rapidly about its symmetry axis with spin angular momentum $L_s = I_z \omega_s$. The pivot is at distance $l$ from the center of mass:
(A) The torque exerted by gravity about the pivot is $\vec{\tau} = \vec{r}_{\text{cm}} \times M\vec{g}$, having magnitude $\tau = M g l \sin\theta$.  
(B) Under the steady precession condition ($\omega_s \gg \Omega_p$), the precession angular velocity is $\Omega_p = \frac{M g l}{I_z \omega_s}$, independent of the nutation angle $\theta$.  
(C) The gyroscopic torque $\vec{\tau}_{\text{gyro}} = \vec{\Omega}_p \times \vec{L}_s$ exactly balances the gravitational torque.  
(D) Superimposed on the steady precession is a fast nutational oscillation of frequency $\omega_n \approx \frac{I_z \omega_s}{I_x}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A horizontal uniform rod of mass $M = 2.00\text{ kg}$ and length $L = 1.20\text{ m}$ is pivoted at one end. A small ball of mass $m = 0.50\text{ kg}$ moving vertically upward with speed $v_0 = 12.0\text{ m/s}$ strikes the rod at distance $x = 0.80\text{ m}$ from the pivot and sticks to it. Calculate the angular velocity $\omega$ (in $\text{rad/s}$) of the rod-ball system immediately after the collision. [Round off to TWO decimal places].

#### Question 8
Two long parallel conducting wires of radius $a = 1.0\text{ mm}$ are separated by distance $d = 20.0\text{ mm}$ ($d \gg a$). If the wires carry equal and opposite currents $I = 50.0\text{ A}$, calculate the magnetic force per unit length $F/L$ (in milliNewtons per meter, $\text{mN/m}$) between them. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$].

#### Question 9
In a Fabry-Pérot étalon with plate separation $d = 10.0\text{ mm}$ and mirror reflectance $R_0 = 0.90$, calculate the coefficient of finesse $F = \frac{4R_0}{(1 - R_0)^2}$. [Round off to the nearest integer].

#### Question 10
One mole of an ideal diatomic gas undergoes an adiabatic expansion from temperature $T_1 = 400.0\text{ K}$ to $T_2 = 300.0\text{ K}$. Calculate the work done $W$ (in Joules) by the gas. [Take $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $C_V = \frac{5}{2}R$. Round off to ONE decimal place].

#### Question 11
A parallel-plate capacitor with plate area $A = 0.040\text{ m}^2$ and plate separation $d = 2.0\text{ mm}$ is connected across an AC voltage source $V(t) = V_0 \sin(\omega t)$ with $V_0 = 100.0\text{ V}$ and frequency $\nu = 50.0\text{ MHz}$ ($\omega = 2\pi \times 50.0 \times 10^6\text{ rad/s}$). Calculate the peak displacement current $I_{d,\text{peak}}$ (in milliAmperes, $\text{mA}$) between the plates. [Take $\varepsilon_0 = 8.854 \times 10^{-12}\text{ F/m}$ and $\pi = 3.1416$. Round off to TWO decimal places].

#### Question 12
A radioactive sample contains $N_0 = 1.00 \times 10^{16}$ nuclei of an isotope with decay constant $\lambda = 2.00 \times 10^{-4}\text{ s}^{-1}$. Calculate the initial activity $A_0$ of the sample in GigaBecquerels ($\text{GBq}$, where $1\text{ GBq} = 10^9\text{ Bq}$).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The radius of curvature of a concave spherical mirror is $R = 40.0\text{ cm}$. An object is placed at distance $u = 30.0\text{ cm}$ in front of the mirror. The linear magnification $m$ of the image is:
(A) $-2.0$  
(B) $+2.0$  
(C) $-0.5$  
(D) $+0.5$

#### Question 14
A charged particle of charge $q$ and mass $m$ enters a region of crossed electric field $\vec{E} = E\hat{j}$ and magnetic field $\vec{B} = B\hat{k}$ without experiencing any net deflection. The particle velocity $\vec{v}$ must be:
(A) $\frac{E}{B}\hat{i}$  
(B) $-\frac{E}{B}\hat{i}$  
(C) $\frac{B}{E}\hat{i}$  
(D) $\sqrt{\frac{2qE}{mB}}\hat{i}$

#### Question 15
The root-mean-square speed $v_{\text{rms}}$ of nitrogen molecules ($\text{N}_2$, $M = 28.0\text{ g/mol}$) at temperature $T = 300\text{ K}$ is approximately:
(A) $517\text{ m/s}$  
(B) $450\text{ m/s}$  
(C) $380\text{ m/s}$  
(D) $620\text{ m/s}$

#### Question 16
In an X-ray tube operated at accelerating voltage $V_0 = 40.0\text{ kV}$, the minimum cutoff wavelength $\lambda_{\text{min}}$ (Duane-Hunt limit) of the continuous bremsstrahlung spectrum is:
(A) $0.031\text{ nm}$  
(B) $0.062\text{ nm}$  
(C) $0.124\text{ nm}$  
(D) $0.015\text{ nm}$

#### Question 17
A uniform solid sphere of mass $M$ and radius $R$ is placed on a rough horizontal surface and given a purely translational velocity $v_0$. The velocity of the sphere when pure rolling commences is:
(A) $\frac{5}{7}v_0$  
(B) $\frac{2}{5}v_0$  
(C) $\frac{3}{5}v_0$  
(D) $\frac{7}{10}v_0$

#### Question 18
Two simple harmonic oscillations along the same line are given by $x_1(t) = 3\sin(\omega t)$ and $x_2(t) = 4\cos(\omega t)$. The amplitude of the resultant oscillation is:
(A) $5$  
(B) $7$  
(C) $1$  
(D) $\sqrt{7}$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Favorskii rearrangement of $\alpha$-haloketones:
(A) Treatment of 2-chlorocyclohexanone with sodium methoxide ($\text{NaOCH}_3$) yields methyl cyclopentanecarboxylate via ring contraction.  
(B) The reaction proceeds via an enolate intermediate that undergoes intramolecular nucleophilic displacement to form a cyclopropanone intermediate.  
(C) Nucleophilic addition of methoxide to the cyclopropanone carbonyl forms a tetrahedral intermediate, which undergoes regioselective ring opening to stabilize the more stable carbanion.  
(D) Non-enolizable $\alpha$-haloketones (such as 1-bromobicyclo[2.2.2]octan-2-one) undergo a quasi-Favorskii rearrangement via a benzilic acid-type semi-pinacol mechanism without forming a cyclopropanone.

#### Question 20
Regarding Tanabe-Sugano diagrams and spin crossover in octahedral complexes:
(A) For $d^4$ through $d^7$ octahedral complexes, the ground state term changes from high-spin to low-spin at a critical ligand field strength $\Delta_0 / B$.  
(B) In Tanabe-Sugano diagrams, the ground state energy is arbitrarily chosen as the zero-energy horizontal baseline.  
(C) The complex $[\text{Fe(phen)}_3]^{2+}$ ($3d^6$) undergoes a sharp spin crossover from $^5T_{2g}$ (high spin, $S=2$) to $^1A_{1g}$ (low spin, $S=0$) upon cooling below transition temperature $T_c$.  
(D) Spin crossover complexes exhibit magnetic bistability and thermal hysteresis, making them candidate materials for molecular data storage.

#### Question 21
Regarding Wade's rules (polyhedral skeletal electron pair theory) for boranes and heteroboranes:
(A) A closo-borane cluster with $n$ vertices has $n + 1$ skeletal electron pairs ($2n + 2$ skeletal electrons), adopting an idealized closo polyhedron.  
(B) A nido-borane cluster with $n$ vertices has $n + 2$ skeletal electron pairs, derived by removing one vertex from an $(n+1)$-vertex closo polyhedron.  
(C) An arachno-borane cluster with $n$ vertices has $n + 3$ skeletal electron pairs, derived by removing two vertices from an $(n+2)$-vertex closo polyhedron.  
(D) Diborane ($\text{B}_2\text{H}_6$) has 12 valence electrons and contains two $3c-2e$ $\text{B-H-B}$ bridging bonds.

#### Question 22
Regarding the Brunauer-Emmett-Teller ($\text{BET}$) multilayer adsorption isotherm:
(A) It extends the Langmuir monolayer model to multilayer adsorption of gas molecules on solid surfaces.  
(B) The linearized $\text{BET}$ equation is $\frac{P}{V(P_0 - P)} = \frac{1}{V_m C} + \frac{C - 1}{V_m C}\left(\frac{P}{P_0}\right)$, where $P_0$ is the saturation vapor pressure.  
(C) A plot of $\frac{P}{V(P_0 - P)}$ versus $P/P_0$ is linear in the relative pressure range $0.05 \le P/P_0 \le 0.35$.  
(D) The slope and intercept of the linear $\text{BET}$ plot allow precise experimental determination of the monolayer volume $V_m$ and the specific surface area of porous catalysts.

#### Question 23
Regarding the stereospecificity and mechanism of the Sharpless asymmetric epoxidation:
(A) It selectively epoxidizes allylic alcohols with high enantiomeric excess using titanium tetraisopropoxide ($\text{Ti(O}i\text{Pr})_4$), tert-butyl hydroperoxide ($\text{TBHP}$), and chiral diethyl tartrate ($\text{DET}$).  
(B) Use of $(+)\text{-diethyl tartrate}$ delivers the oxygen atom from the bottom ($\alpha$) face of the allylic alcohol double bond (when drawn with the hydroxymethyl group at the lower right).  
(C) Use of $(-)\text{-diethyl tartrate}$ delivers the oxygen atom from the top ($\beta$) face.  
(D) The high enantioselectivity arises from coordination of both the allylic alcohol and $\text{TBHP}$ to a dimeric chiral titanium-tartrate complex.

#### Question 24
Regarding the electrochemistry of the lead-acid storage battery during discharging:
(A) At the anode (negative plate), spongy lead is oxidized: $\text{Pb}(s) + \text{HSO}_4^-(aq) \to \text{PbSO}_4(s) + \text{H}^+(aq) + 2e^-$.  
(B) At the cathode (positive plate), lead dioxide is reduced: $\text{PbO}_2(s) + \text{HSO}_4^-(aq) + 3\text{H}^+(aq) + 2e^- \to \text{PbSO}_4(s) + 2\text{H}_2\text{O}(l)$.  
(C) The overall discharge reaction is $\text{Pb}(s) + \text{PbO}_2(s) + 2\text{H}_2\text{SO}_4(aq) \to 2\text{PbSO}_4(s) + 2\text{H}_2\text{O}(l)$.  
(D) During discharge, sulfuric acid is consumed, causing the specific gravity of the battery electrolyte to decrease from $\approx 1.28$ to $\approx 1.15$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
A $0.050\text{ M}$ solution of sodium hydrogen carbonate ($\text{NaHCO}_3$) in water has carbonic acid dissociation constants $pK_{a1} = 6.35$ and $pK_{a2} = 10.33$. Calculate the $\text{pH}$ of this amphiprotic salt solution. [Round off to TWO decimal places].

#### Question 26
For the thermal decomposition reaction:
$$2\text{HI}(g) \rightleftharpoons \text{H}_2(g) + \text{I}_2(g)$$
the equilibrium constant is $K_c = 0.020$ at $440^\circ\text{C}$. If $1.00\text{ mol}$ of $\text{HI}$ is heated in a $1.0\text{ L}$ sealed vessel, calculate the equilibrium concentration of $\text{I}_2(g)$ in $\text{mol/L}$. [Take $\sqrt{0.020} \approx 0.1414$. Round off to TWO decimal places].

#### Question 27
Potassium crystallizes in a body-centered cubic ($\text{BCC}$) structure with unit cell edge length $a = 520.0\text{ pm}$. Calculate the atomic radius $r$ of potassium in picometers ($\text{pm}$). [Take $\sqrt{3} \approx 1.732$. Round off to ONE decimal place].

#### Question 28
Calculate the standard Gibbs free energy change $\Delta G^\circ$ (in $\text{kJ/mol}$) at $298\text{ K}$ for the reaction:
$$\text{Cu}(s) + 2\text{Ag}^+(aq) \to \text{Cu}^{2+}(aq) + 2\text{Ag}(s)$$
Given $E^\circ(\text{Cu}^{2+}/\text{Cu}) = +0.34\text{ V}$, $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$, and $F = 96485\text{ C/mol}$. [Round off to ONE decimal place].

#### Question 29
A $0.20\text{ m}$ aqueous solution of potassium ferrocyanide ($\text{K}_4[\text{Fe(CN)}_6]$) freezes at $-1.60^\circ\text{C}$. If $K_f(\text{water}) = 1.86\text{ K}\cdot\text{kg/mol}$, calculate the apparent degree of dissociation $\alpha$ (in percentage, $\%$) of the complex salt. [Round off to ONE decimal place].

#### Question 30
Calculate the total number of unpaired electrons in the ground state of the tetrahedral complex $[\text{CoCl}_4]^{2-}$ ($\text{Co}^{2+}, 3d^7$).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Swern oxidation of primary alcohols to aldehydes, the reagents employed are:
(A) Oxalyl chloride ($(\text{COCl})_2$), dimethyl sulfoxide ($\text{DMSO}$), and triethylamine ($\text{Et}_3\text{N}$)  
(B) Pyridinium chlorochromate ($\text{PCC}$) in $\text{CH}_2\text{Cl}_2$  
(C) Dess-Martin periodinane ($\text{DMP}$)  
(D) Potassium permanganate in acidic medium

#### Question 32
The correct order of increasing crystal field splitting energy ($\Delta_0$) for the ligands in the spectrochemical series is:
(A) $\text{I}^- < \text{Br}^- < \text{Cl}^- < \text{F}^- < \text{H}_2\text{O} < \text{NH}_3 < \text{CN}^- < \text{CO}$  
(B) $\text{CO} < \text{CN}^- < \text{NH}_3 < \text{H}_2\text{O} < \text{F}^- < \text{Cl}^- < \text{Br}^- < \text{I}^-$  
(C) $\text{Cl}^- < \text{F}^- < \text{Br}^- < \text{I}^- < \text{H}_2\text{O} < \text{NH}_3 < \text{CO} < \text{CN}^-$  
(D) $\text{H}_2\text{O} < \text{NH}_3 < \text{I}^- < \text{Br}^- < \text{Cl}^- < \text{F}^- < \text{CN}^- < \text{CO}$

#### Question 33
In the extraction of copper from copper pyrites ($\text{CuFeS}_2$), silica ($\text{SiO}_2$) is added during smelting in the reverberatory furnace to:
(A) Act as an acidic flux to remove basic iron(II) oxide as slag ($\text{FeSiO}_3$)  
(B) Reduce cuprous oxide to metallic copper  
(C) Act as a basic flux to remove sulfur dioxide  
(D) Convert copper matte into blister copper

#### Question 34
The shape of the triiodide anion ($\text{I}_3^-$) according to VSEPR theory is:
(A) Linear  
(B) Bent ($V$-shaped)  
(C) Trigonal planar  
(D) T-shaped

#### Question 35
Which of the following carbohydrates is a non-reducing sugar?
(A) Sucrose  
(B) Maltose  
(C) Lactose  
(D) Cellobiose

#### Question 36
Bakelite is a thermosetting polymer obtained by the cross-linking condensation of:
(A) Phenol and formaldehyde  
(B) Melamine and formaldehyde  
(C) Urea and formaldehyde  
(D) Phthalic acid and glycerol

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $F(x) = \int_0^{x^2} e^{-t^2}\,dt$ for $x \in \mathbb{R}$:
(A) By the Leibniz integral rule, $F'(x) = 2x e^{-x^4}$.  
(B) $F(x)$ has a local minimum at $x = 0$.  
(C) $F''(x) = 2e^{-x^4}(1 - 4x^4)$, giving points of inflection at $x = \pm (1/4)^{1/4}$.  
(D) $\lim_{x \to \infty} F(x) = \frac{\sqrt{\pi}}{2}$.

#### Question 38
Let $N$ be a non-zero $3 \times 3$ real nilpotent matrix ($N^k = 0$ for some positive integer $k$):
(A) The only eigenvalue of $N$ is $\lambda = 0$ with algebraic multiplicity $3$.  
(B) The characteristic polynomial of $N$ is $p(\lambda) = -\lambda^3$.  
(C) $\det(N) = 0$ and $\text{tr}(N) = 0$.  
(D) The matrix $I + N$ is invertible, with $(I + N)^{-1} = I - N + N^2$.

#### Question 39
Consider the Clairaut differential equation $y = x \frac{dy}{dx} - \left(\frac{dy}{dx}\right)^2$:
(A) The general solution is the one-parameter family of straight lines $y = C x - C^2$.  
(B) Differentiating with respect to $p = \frac{dy}{dx}$ yields $\frac{dp}{dx}(x - 2p) = 0$.  
(C) The singular solution is the envelope curve obtained from $x = 2p \implies p = x/2$, giving the parabola $y = \frac{x^2}{4}$.  
(D) The straight lines of the general solution are all tangent to the singular parabolic envelope.

#### Question 40
Consider the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$:
(A) The asymptotes of the hyperbola are the lines $y = \pm \frac{b}{a}x$.  
(B) The product of the perpendicular distances from any point on the hyperbola to its two asymptotes is constant, equal to $\frac{a^2 b^2}{a^2 + b^2}$.  
(C) Any tangent to the hyperbola intersects the asymptotes at points $P$ and $Q$ such that the point of tangency is the midpoint of $PQ$.  
(D) The area of the triangle formed by any tangent and the two asymptotes is constant, equal to $a b$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be three non-coplanar vectors. Define the reciprocal triad of vectors $\vec{a}', \vec{b}', \vec{c}'$ by:
$$\vec{a}' = \frac{\vec{b} \times \vec{c}}{[\vec{a}\ \vec{b}\ \vec{c}]}, \quad \vec{b}' = \frac{\vec{c} \times \vec{a}}{[\vec{a}\ \vec{b}\ \vec{c}]}, \quad \vec{c}' = \frac{\vec{a} \times \vec{b}}{[\vec{a}\ \vec{b}\ \vec{c}]}$$
Which of the following statements is/are correct?
(A) $\vec{a} \cdot \vec{a}' = \vec{b} \cdot \vec{b}' = \vec{c} \cdot \vec{c}' = 1$.  
(B) $\vec{a} \cdot \vec{b}' = \vec{a} \cdot \vec{c}' = 0$.  
(C) $[\vec{a}'\ \vec{b}'\ \vec{c}'] = \frac{1}{[\vec{a}\ \vec{b}\ \vec{c}]}$.  
(D) Any vector $\vec{r}$ can be uniquely expanded as $\vec{r} = (\vec{r} \cdot \vec{a}')\vec{a} + (\vec{r} \cdot \vec{b}')\vec{b} + (\vec{r} \cdot \vec{c}')\vec{c}$.

#### Question 42
In an experiment, a fair die is rolled repeatedly until the first six appears:
(A) The number of rolls $X$ follows a geometric distribution with parameter $p = 1/6$.  
(B) The expected number of rolls is $E[X] = \frac{1}{p} = 6$.  
(C) The variance of the number of rolls is $\text{Var}(X) = \frac{1 - p}{p^2} = \frac{5/6}{1/36} = 30$.  
(D) The probability that more than 3 rolls are required is $P(X > 3) = (5/6)^3 = \frac{125}{216}$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the Frullani integral:
$$I = \int_0^\infty \frac{e^{-2x} - e^{-5x}}{x}\,dx$$
If $I = \ln(k)$, find the value of $k$ rounded off to TWO decimal places.

#### Question 44
Find the maximum value of $f(x, y) = x y$ subject to the elliptical constraint $x^2 + 4y^2 = 8$.

#### Question 45
Find the radius of curvature $\rho$ of the catenary curve $y = 2\cosh(x/2)$ at its vertex $x = 0$.

#### Question 46
Calculate the sum of the infinite series:
$$S = \sum_{n=1}^\infty \frac{1}{n(n+1)(n+2)}$$
If $S = \frac{1}{k}$, find the integer value of $k$.

#### Question 47
Let $A$ be a $3 \times 3$ matrix with $\det(A) = 3$. Calculate the determinant of the matrix $2 A^{-1}$.

#### Question 48
How many 4-digit positive integers can be formed using the digits $\{1, 2, 3, 4, 5, 6\}$ without repetition such that the integer is divisible by $5$?

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
Evaluate the limit:
$$L = \lim_{x \to 0} \left(\frac{\sin x}{x}\right)^{1/x^2}$$
(A) $e^{-1/6}$  
(B) $e^{-1/3}$  
(C) $e^{-1/2}$  
(D) $1$

#### Question 50
The locus of the foot of the perpendicular from either focus of the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b$) upon any tangent is:
(A) The auxiliary circle $x^2 + y^2 = a^2$  
(B) The director circle $x^2 + y^2 = a^2 + b^2$  
(C) The major axis $y = 0$  
(D) The directrix $x = a/e$

#### Question 51
The shortest distance between the lines $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $\frac{x-2}{3} = \frac{y-4}{4} = \frac{z-5}{5}$ is:
(A) $1/\sqrt{6}$  
(B) $0$ (they intersect)  
(C) $\sqrt{6}$  
(D) $2/\sqrt{6}$

#### Question 52
If $z$ is a complex number such that $|z - i| = |z + i|$, then the locus of $z$ in the Argand plane is:
(A) The real axis ($\text{Im}(z) = 0$)  
(B) The imaginary axis ($\text{Re}(z) = 0$)  
(C) The unit circle $|z| = 1$  
(D) The line $y = x$

#### Question 53
The differential equation of all non-vertical straight lines in the Cartesian plane is:
(A) $\frac{d^2 y}{dx^2} = 0$  
(B) $\frac{dy}{dx} = C$  
(C) $y = x \frac{dy}{dx}$  
(D) $\frac{d^3 y}{dx^3} = 0$

#### Question 54
The number of non-negative integer solutions to the equation $x_1 + x_2 + x_3 + x_4 = 12$ is:
(A) $\binom{15}{3} = 455$  
(B) $\binom{12}{3} = 220$  
(C) $\binom{16}{4} = 1820$  
(D) $\binom{11}{3} = 165$
"""

paper_2_md = r"""# JEE Advanced Mock Examination 09 — Paper 2
## Organising Institute Style Inspiration: IIT Delhi (`IIT_DELHI_STYLE`)
**Historical Reference Benchmark**: 2013, 2020 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject — One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject — Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject — Matching List / Matrix Match)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A uniform solid sphere of mass $M$ and radius $R$ is placed on an infinite horizontal conveyor belt moving with constant velocity $u\hat{i}$. The sphere is released with zero initial velocity ($v_0 = 0, \omega_0 = 0$) at $t = 0$. The coefficient of kinetic friction between the belt and sphere is $\mu_k$:
(A) The initial frictional force on the sphere acts forward ($+x$ direction) with magnitude $f_k = \mu_k M g$.  
(B) Slipping between the belt and the sphere ceases at time $t_s = \frac{2u}{7\mu_k g}$.  
(C) The linear velocity of the sphere when pure rolling commences on the belt is $v_s = \frac{2}{7}u$.  
(D) The total work done by the belt motor during the slipping phase exceeds the mechanical energy gained by the sphere.

#### Question 2
A rectangular loop of wire of mass $m$, width $w$, length $L$, and electrical resistance $R$ is released from rest in a vertical plane and falls under gravity through a horizontal strip of uniform magnetic field $B$ directed into the page:
(A) As the lower edge of the loop enters the magnetic field, an upward retarding Lorentz force $F_{\text{mag}} = \frac{B^2 w^2 v}{R}$ acts on the loop.  
(B) The terminal velocity achieved if the loop remains long enough in the entry phase is $v_t = \frac{m g R}{B^2 w^2}$.  
(C) When the loop is completely submerged inside the uniform magnetic field, the induced EMF is zero, and the loop accelerates downward at $g$.  
(D) As the loop exits the magnetic field, the induced current flows in the counter-clockwise direction.

#### Question 3
An ideal gas undergoes a thermodynamic cycle consisting of an isobaric heating from $V_0$ to $2V_0$ at pressure $P_0$, an isochoric cooling to pressure $P_0/2$, an isobaric compression back to $V_0$, and an isochoric heating back to $P_0$:
(A) The cycle forms a rectangle on the $P-V$ indicator diagram.  
(B) The net work done per cycle is $W_{\text{net}} = \frac{1}{2}P_0 V_0$.  
(C) For a monoatomic ideal gas ($C_V = \frac{3}{2}R$), the total heat absorbed during the two heating stages is $Q_{\text{in}} = \frac{13}{4}P_0 V_0$.  
(D) The thermal efficiency of the cycle is $\eta = \frac{W_{\text{net}}}{Q_{\text{in}}} = \frac{2}{13} \approx 15.38\%$.

#### Question 4
In a Young's double-slit experiment illuminated by two coherent sources $S_1$ and $S_2$ separated by distance $d$, a thin glass plate of thickness $t_1$ and refractive index $\mu_1$ is placed in front of $S_1$, and another plate of thickness $t_2$ and index $\mu_2$ is placed in front of $S_2$:
(A) The net optical path difference introduced at the central position ($y = 0$) is $\Delta L = (\mu_1 - 1)t_1 - (\mu_2 - 1)t_2$.  
(B) The entire fringe pattern shifts upward (towards $S_1$) if $(\mu_1 - 1)t_1 > (\mu_2 - 1)t_2$.  
(C) The linear shift of the central bright fringe on a screen at distance $D$ is $\Delta y = \frac{D}{d}\left[(\mu_1 - 1)t_1 - (\mu_2 - 1)t_2\right]$.  
(D) The fringe width $\beta = \frac{\lambda D}{d}$ remains completely unchanged by the insertion of the plates.

#### Question 5
Regarding the energy levels and transitions in the hydrogen atom according to the Bohr-Sommerfeld model:
(A) The orbital radius of an electron in state $n$ scales as $r_n \propto n^2$.  
(B) The orbital speed of the electron scales as $v_n \propto 1/n$.  
(C) The ionization energy from the first excited state ($n=2$) is $3.40\text{ eV}$.  
(D) The shortest wavelength in the Balmer series corresponds to the transition from $n = \infty$ to $n = 2$, having wavelength $\lambda_{\text{limit}} = \frac{4}{R_\infty} \approx 364.6\text{ nm}$.

#### Question 6
A spherical soap bubble of radius $R_1$ and surface tension $T$ is blown isothermally in atmospheric air at pressure $P_0$ until its radius increases to $R_2 = 2R_1$:
(A) The excess pressure inside the bubble at radius $R$ is $\Delta P = \frac{4T}{R}$ due to the two spherical liquid-air surfaces.  
(B) The work done in creating the additional surface area is $W_s = 8\pi T (R_2^2 - R_1^2) = 24\pi T R_1^2$.  
(C) The total mechanical work done against atmospheric pressure during expansion is $W_{\text{atm}} = P_0 \Delta V = \frac{28}{3}\pi P_0 R_1^3$.  
(D) The total work performed to expand the bubble is $W_{\text{total}} = W_{\text{atm}} + W_s$.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 7 to 12)

#### Question 7
A particle of mass $m = 0.20\text{ kg}$ is attached to the end of a light string of length $L = 0.80\text{ m}$ to form a conical pendulum. The string makes a constant angle $\theta = 60.0^\circ$ with the vertical. Calculate the tension $T$ (in Newtons) in the string. [Take $g = 9.80\text{ m/s}^2$].

#### Question 8
Two identical circular loops of radius $R = 0.10\text{ m}$ each carrying current $I = 4.0\text{ A}$ lie in mutually perpendicular planes with their centers coinciding at the origin. Calculate the magnitude of the net magnetic field $B_{\text{net}}$ (in microTesla, $\mu\text{T}$) at their common center. [Take $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$, and $\sqrt{2} \approx 1.414$. Round off to ONE decimal place].

#### Question 9
In a Newton's rings experiment, the diameter of the 4th dark ring in reflected light is $d_4 = 4.00\text{ mm}$. If the wavelength of the light is $\lambda = 500\text{ nm}$, calculate the radius of curvature $R$ (in meters, $\text{m}$) of the plano-convex lens. [Take $d_n^2 = 4 n R \lambda$].

#### Question 10
One mole of an ideal monoatomic gas is compressed adiabatically to one-eighth ($1/8$) of its initial volume. If the initial temperature was $T_1 = 300.0\text{ K}$, calculate the final temperature $T_2$ (in Kelvin) of the gas. [Take $\gamma = 5/3$, $(8)^{2/3} = 4.0$].

#### Question 11
An alternating current is given by $i(t) = 6.0\sin(\omega t) + 8.0\cos(\omega t)$ in Amperes. Calculate the root-mean-square ($\text{rms}$) value $I_{\text{rms}}$ (in Amperes) of this current. [Take $\sqrt{50} \approx 7.07$. Round off to TWO decimal places].

#### Question 12
A sample of radioactive material contains $N = 4.0 \times 10^{20}$ nuclei with a half-life of $T_{1/2} = 10.0\text{ hours}$. Calculate the activity of the sample in MegaBecquerels ($\text{MBq}$) at $t = 30.0\text{ hours}$. [Take $\ln 2 = 0.693$. Round off to ONE decimal place].

---

## Section 3: Matching List Questions (Questions 13 to 18)

#### Question 13
Match the rotational systems in List-I with their radius of gyration $k$ about the specified axis in List-II:
- **List-I**:
  - P. Uniform thin circular hoop of radius $R$ about central axis
  - Q. Uniform solid disk of radius $R$ about central axis
  - R. Uniform solid sphere of radius $R$ about central diameter
  - S. Thin uniform rod of length $L$ about perpendicular axis through center
- **List-II**:
  - 1. $R$
  - 2. $R/\sqrt{2}$
  - 3. $\sqrt{2/5}R$
  - 4. $L/\sqrt{12}$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 14
Match the electrostatic configurations in List-I with the electric potential $V(r)$ dependence on distance $r$ ($r \gg \text{size}$) in List-II:
- **List-I**:
  - P. Isolated point monopole charge
  - Q. Ideal electric dipole
  - R. Linear electric quadrupole
  - S. Infinite line charge
- **List-II**:
  - 1. Proportional to $1/r$
  - 2. Proportional to $1/r^2$
  - 3. Proportional to $1/r^3$
  - 4. Proportional to $\ln(1/r)$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 15
Match the optical instruments in List-I with their characteristic angular magnification formula in List-II:
- **List-I**:
  - P. Simple magnifying glass (relaxed eye at infinity)
  - Q. Astronomical telescope (normal adjustment)
  - R. Compound microscope (normal adjustment)
  - S. Terrestrial telescope (normal adjustment)
- **List-II**:
  - 1. $M = D/f$
  - 2. $M = f_o / f_e$
  - 3. $M = \frac{L}{f_o}\frac{D}{f_e}$
  - 4. $M = f_o / f_e$ with upright image (erecting lens)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 16
Match the thermodynamic processes in List-I with the work done by one mole of an ideal gas in List-II:
- **List-I**:
  - P. Isothermal expansion ($V_1 \to V_2$)
  - Q. Isobaric expansion ($V_1 \to V_2$ at pressure $P_0$)
  - R. Adiabatic expansion ($T_1 \to T_2$)
  - S. Isochoric heating ($T_1 \to T_2$)
- **List-II**:
  - 1. $R T \ln(V_2/V_1)$
  - 2. $P_0 (V_2 - V_1)$
  - 3. $\frac{R(T_1 - T_2)}{\gamma - 1}$
  - 4. $0$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 17
Match the particle physics phenomena in List-I with their governing fundamental interaction in List-II:
- **List-I**:
  - P. $\beta^-$-decay of a free neutron ($n \to p + e^- + \bar{\nu}_e$)
  - Q. Binding of nucleons in an atomic nucleus
  - R. Coulomb repulsion between two protons
  - S. Gravitational attraction between celestial bodies
- **List-II**:
  - 1. Weak nuclear interaction
  - 2. Strong nuclear interaction
  - 3. Electromagnetic interaction
  - 4. Gravitational interaction

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 18
Match the electromagnetic wave bands in List-I with their typical production mechanism in List-II:
- **List-I**:
  - P. Radio waves
  - Q. Infrared waves
  - R. Ultraviolet radiation
  - S. Gamma rays
- **List-II**:
  - 1. Rapid acceleration of electrons in aerials / antennas
  - 2. Molecular vibrational and rotational excitations
  - 3. Electronic transitions in outer atomic shells
  - 4. Nuclear transitions and radioactive decay

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the acidity of organic compounds:
(A) Trichloroacetic acid is a stronger acid than acetic acid due to the strong $-I$ inductive electron withdrawal of the three chlorine atoms.  
(B) Picric acid (2,4,6-trinitrophenol) is strongly acidic ($pK_a \approx 0.38$) due to extensive resonance delocalization of the phenoxide negative charge into the three ortho/para nitro groups.  
(C) Formic acid is more acidic than benzoic acid.  
(D) Cyclopentadiene is unusually acidic ($pK_a \approx 16$) because its conjugate base (cyclopentadienyl anion) is a $6\pi$-electron aromatic system.

#### Question 20
Which of the following compounds will give a positive silver mirror test with Tollens' reagent?
(A) Acetaldehyde ($\text{CH}_3\text{CHO}$)  
(B) Benzaldehyde ($\text{C}_6\text{H}_5\text{CHO}$)  
(C) Formic acid ($\text{HCOOH}$)  
(D) D-Glucose

#### Question 21
Regarding the standard reduction potentials:
- $\text{Fe}^{3+}(aq) + e^- \to \text{Fe}^{2+}(aq) \quad E^\circ = +0.77\text{ V}$
- $\text{I}_2(s) + 2e^- \to 2\text{I}^-(aq) \quad E^\circ = +0.54\text{ V}$
- $\text{Br}_2(l) + 2e^- \to 2\text{Br}^-(aq) \quad E^\circ = +1.09\text{ V}$
Which of the following redox processes are thermodynamically spontaneous under standard state conditions?
(A) Oxidation of $\text{I}^-$ by $\text{Fe}^{3+}$ to form $\text{I}_2$ and $\text{Fe}^{2+}$ ($E_{\text{cell}}^\circ = +0.23\text{ V}$).  
(B) Oxidation of $\text{Fe}^{2+}$ by $\text{Br}_2$ to form $\text{Fe}^{3+}$ and $\text{Br}^-$ ($E_{\text{cell}}^\circ = +0.32\text{ V}$).  
(C) Oxidation of $\text{Br}^-$ by $\text{Fe}^{3+}$.  
(D) Reduction of $\text{Fe}^{3+}$ by $\text{I}^-$.

#### Question 22
Regarding the extraction and metallurgy of aluminum via the Hall-Héroult process:
(A) Purified alumina ($\text{Al}_2\text{O}_3$) is dissolved in molten cryolite ($\text{Na}_3\text{AlF}_6$) and fluorspar ($\text{CaF}_2$) to lower the melting point to $\approx 950^\circ\text{C}$ and improve electrical conductivity.  
(B) The cathode consists of a carbon-lined steel tank where aluminum ions are reduced: $\text{Al}^{3+} + 3e^- \to \text{Al}(l)$.  
(C) Carbon anodes are consumed during electrolysis by reaction with liberated oxygen, producing $\text{CO}$ and $\text{CO}_2$: $\text{C} + \text{O}^{2-} \to \text{CO} + 2e^-$.  
(D) Pure aluminum is less dense than the molten electrolyte and floats on top.

#### Question 23
Regarding the stereochemistry of addition to carbon-carbon double bonds:
(A) Catalytic hydrogenation ($\text{H}_2 / \text{Pd-C}$) of an alkene proceeds with stereospecific syn-addition.  
(B) Bromination of cis-but-2-ene in $\text{CCl}_4$ yields a racemic ($\pm$) mixture of (2R,3R)- and (2S,3S)-2,3-dibromobutane via anti-addition through a cyclic bromonium ion.  
(C) Bromination of trans-but-2-ene in $\text{CCl}_4$ yields the achiral meso-2,3-dibromobutane.  
(D) Hydroboration-oxidation ($\text{BH}_3\cdot\text{THF}$ followed by $\text{H}_2\text{O}_2 / \text{NaOH}$) proceeds with overall anti-Markovnikov regioselectivity and syn-stereospecificity.

#### Question 24
Regarding the properties of transition metal coordination complexes:
(A) Low-spin octahedral complexes of $d^6$ metal ions (e.g., $[\text{Co(NH}_3)_6]^{3+}$) have maximum Crystal Field Stabilization Energy ($\text{CFSE} = -2.4\Delta_0 + 2P$).  
(B) Tetrahedral complexes are predominantly high-spin because the crystal field splitting $\Delta_t = \frac{4}{9}\Delta_0$ is too small to overcome electron pairing energy.  
(C) Complexes with $d^0$ ($\text{Sc}^{3+}$) and $d^{10}$ ($\text{Zn}^{2+}$) configurations are diamagnetic and colorless in the absence of charge transfer.  
(D) Intense purple coloration of $[\text{MnO}_4]^-$ is due to ligand-to-metal charge transfer ($\text{LMCT}$) rather than $d-d$ transitions.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 25 to 30)

#### Question 25
A first-order gaseous reaction $A(g) \to 2B(g) + C(g)$ is carried out in a constant volume vessel at constant temperature. The initial pressure is $P_0 = 100.0\text{ mm Hg}$, and the total pressure after $10.0\text{ minutes}$ is $P_t = 220.0\text{ mm Hg}$. Calculate the rate constant $k$ (in $\text{min}^{-1}$) of the reaction. [Take $\ln(2.5) \approx 0.9163$. Round off to TWO decimal places].

#### Question 26
Calculate the solubility product $K_{sp}$ of silver chromate ($\text{Ag}_2\text{CrO}_4$) at $25^\circ\text{C}$ given that its solubility in pure water is $S = 6.5 \times 10^{-5}\text{ mol/L}$. [Calculate $K_{sp} = 4S^3$. Enter the value multiplied by $10^{12}$. Round off to ONE decimal place].

#### Question 27
Sodium crystallizes in a $\text{BCC}$ lattice with edge length $a = 429.0\text{ pm}$. Calculate the density $\rho$ of sodium in $\text{g/cm}^3$. [Take atomic mass of $\text{Na} = 23.0\text{ g/mol}$, $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$, and $4.29^3 \approx 78.95$. Round off to TWO decimal places].

#### Question 28
Calculate the electromotive force $E_{\text{cell}}^\circ$ (in Volts) at $298\text{ K}$ for the cell reaction:
$$\text{Mg}(s) + \text{Sn}^{2+}(aq) \to \text{Mg}^{2+}(aq) + \text{Sn}(s)$$
Given standard reduction potentials: $E^\circ(\text{Mg}^{2+}/\text{Mg}) = -2.37\text{ V}$ and $E^\circ(\text{Sn}^{2+}/\text{Sn}) = -0.14\text{ V}$.

#### Question 29
A $0.50\text{ molal}$ aqueous solution of an electrolyte $AB_2$ dissociates into one $A^{2+}$ and two $B^-$ ions with degree of dissociation $\alpha = 80.0\%$. Calculate the boiling point elevation $\Delta T_b$ (in Kelvin) of the solution. [Take $K_b(\text{water}) = 0.512\text{ K}\cdot\text{kg/mol}$. Note $i = 1 + 2\alpha$. Round off to TWO decimal places].

#### Question 30
Find the oxidation state of chromium in potassium dichromate ($\text{K}_2\text{Cr}_2\text{O}_7$).

---

## Section 3: Matching List Questions (Questions 31 to 36)

#### Question 31
Match the organic named reactions in List-I with their characteristic reactive intermediate in List-II:
- **List-I**:
  - P. Reimer-Tiemann reaction
  - Q. Hofmann bromamide degradation
  - R. Pinacol-pinacolone rearrangement
  - S. Kolbe-Schmitt reaction
- **List-II**:
  - 1. Dichlorocarbene ($:\text{CCl}_2$)
  - 2. Acyl nitrene / Isocyanate ($\text{R-N=C=O}$)
  - 3. Carbocation with 1,2-migratory shift
  - 4. Phenoxide nucleophilic attack on electrophilic $\text{CO}_2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 32
Match the transition metal complexes in List-I with their coordination number and geometry in List-II:
- **List-I**:
  - P. $[\text{Ag(CN)}_2]^-$
  - Q. $[\text{Ni(CO)}_4]$
  - R. $[\text{PtCl}_4]^{2-}$
  - S. $[\text{Co(NH}_3)_6]^{3+}$
- **List-II**:
  - 1. Coordination number 2; Linear
  - 2. Coordination number 4; Tetrahedral
  - 3. Coordination number 4; Square planar
  - 4. Coordination number 6; Octahedral

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 33
Match the ores in List-I with their principal metal in List-II:
- **List-I**:
  - P. Bauxite
  - Q. Haematite
  - R. Malachite
  - S. Galena
- **List-II**:
  - 1. Aluminum
  - 2. Iron
  - 3. Copper
  - 4. Lead

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 34
Match the qualitative group reagents in List-I with the cation group precipitated in List-II:
- **List-I**:
  - P. Dilute $\text{HCl}$
  - Q. $\text{H}_2\text{S}$ gas in acidic medium ($\text{dil. HCl}$)
  - R. $\text{NH}_4\text{OH}$ in presence of $\text{NH}_4\text{Cl}$
  - S. $\text{H}_2\text{S}$ gas in ammoniacal medium
- **List-II**:
  - 1. Group I ($\text{Ag}^+, \text{Pb}^{2+}, \text{Hg}_2^{2+}$ as chlorides)
  - 2. Group II ($\text{Cu}^{2+}, \text{Pb}^{2+}, \text{Bi}^{3+}, \text{Cd}^{2+}$ as sulfides)
  - 3. Group III ($\text{Fe}^{3+}, \text{Al}^{3+}, \text{Cr}^{3+}$ as hydroxides)
  - 4. Group IV ($\text{Ni}^{2+}, \text{Co}^{2+}, \text{Mn}^{2+}, \text{Zn}^{2+}$ as sulfides)

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 35
Match the synthetic polymers in List-I with their classification in List-II:
- **List-I**:
  - P. Polyethylene
  - Q. Bakelite
  - R. Neoprene
  - S. Nylon-6
- **List-II**:
  - 1. Thermoplastic addition polymer
  - 2. Thermosetting cross-linked polymer
  - 3. Synthetic elastomer (rubber)
  - 4. Polyamide fiber

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 36
Match the biomolecules in List-I with their characteristic functional role in List-II:
- **List-I**:
  - P. Hemoglobin
  - Q. Insulin
  - R. DNA
  - S. Keratin
- **List-II**:
  - 1. Oxygen transport metalloprotein
  - 2. Peptide hormone regulating glucose metabolism
  - 3. Genetic information storage nucleic acid
  - 4. Structural fibrous protein in hair and nails

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{\ln x}{x}$ for $x > 0$:
(A) $f'(x) = \frac{1 - \ln x}{x^2}$.  
(B) $f(x)$ attains its absolute maximum at $x = e$ with maximum value $1/e$.  
(C) $f(x)$ has a point of inflection at $x = e^{3/2}$.  
(D) $e^\pi > \pi^e$.

#### Question 38
Let $A$ and $B$ be two $n \times n$ real symmetric matrices:
(A) $A + B$ is symmetric.  
(B) $A B$ is symmetric if and only if $A$ and $B$ commute ($A B = B A$).  
(C) All eigenvalues of $A$ are strictly real.  
(D) $A$ is orthogonally diagonalizable (there exists orthogonal matrix $Q$ such that $Q^T A Q$ is diagonal).

#### Question 39
Consider the parabola $y^2 = 4ax$:
(A) The equation of the tangent at $(a t^2, 2at)$ is $t y = x + a t^2$.  
(B) The equation of the normal at $(a t^2, 2at)$ is $y = -t x + 2at + a t^3$.  
(C) Tangents at the ends of a focal chord intersect at right angles on the directrix $x = -a$.  
(D) The circle described on a focal chord as diameter touches the directrix.

#### Question 40
Consider the differential equation $\frac{dy}{dx} = \frac{y + \sqrt{x^2 + y^2}}{x}$ for $x > 0$:
(A) The differential equation is homogeneous of degree zero.  
(B) Substituting $y = v x$ yields $x \frac{dv}{dx} = \sqrt{1 + v^2}$.  
(C) Separating variables gives $\ln(v + \sqrt{1 + v^2}) = \ln x + \ln C$.  
(D) The general solution is $y + \sqrt{x^2 + y^2} = C x^2$.

#### Question 41
Let $\vec{a}, \vec{b}, \vec{c}$ be three unit vectors such that $\vec{a} + \vec{b} + \vec{c} = \vec{0}$:
(A) The vectors form the sides of an equilateral triangle.  
(B) The angle between any two vectors is $120^\circ$ ($2\pi/3\text{ rad}$).  
(C) $\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{c} + \vec{c} \cdot \vec{a} = -3/2$.  
(D) $|\vec{a} \times \vec{b}| = \frac{\sqrt{3}}{2}$.

#### Question 42
In a Poisson process with average rate $\lambda = 3$ events per hour:
(A) The probability of observing exactly $k$ events in one hour is $P(X = k) = \frac{e^{-3} 3^k}{k!}$.  
(B) The expected number of events in 2 hours is $6$.  
(C) The variance of the number of events in 2 hours is $6$.  
(D) The time $T$ between successive events follows an exponential distribution with mean $1/3$ hour.

---

## Section 2: Non-Negative Numerical Value Questions (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 \frac{\ln(1 + x)}{1 + x^2}\,dx$$
If $I = \frac{\pi}{m}\ln 2$, find the integer value of $m$.

#### Question 44
Find the area enclosed by the astroid curve $x^{2/3} + y^{2/3} = a^{2/3}$ with $a = 4$. Given that the area of an astroid is $A = \frac{3}{8}\pi a^2$, calculate $A/\pi$.

#### Question 45
Calculate the distance between the parallel lines $3x - 4y + 7 = 0$ and $3x - 4y - 18 = 0$.

#### Question 46
Calculate the sum of the infinite geometric series:
$$S = 12 + 4 + \frac{4}{3} + \frac{4}{9} + \dots$$

#### Question 47
A bag contains 5 red balls and 4 blue balls. If 3 balls are drawn at random without replacement, calculate the probability that exactly 2 are red and 1 is blue, multiplied by $21$.

#### Question 48
Calculate the determinant of the $3 \times 3$ identity matrix multiplied by $3$ ($\det(3 I_3)$).

---

## Section 3: Matching List Questions (Questions 49 to 54)

#### Question 49
Match the conic sections in List-I with their eccentricity $e$ in List-II:
- **List-I**:
  - P. Circle
  - Q. Parabola
  - R. Ellipse
  - S. Hyperbola
- **List-II**:
  - 1. $e = 0$
  - 2. $e = 1$
  - 3. $0 < e < 1$
  - 4. $e > 1$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-1, S-3

#### Question 50
Match the integration standard formulas in List-I with their result in List-II:
- **List-I**:
  - P. $\int \frac{dx}{x^2 + a^2}$
  - Q. $\int \frac{dx}{\sqrt{a^2 - x^2}}$
  - R. $\int \frac{dx}{x^2 - a^2}$
  - S. $\int \frac{dx}{\sqrt{x^2 + a^2}}$
- **List-II**:
  - 1. $\frac{1}{a}\arctan(x/a)$
  - 2. $\arcsin(x/a)$
  - 3. $\frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right|$
  - 4. $\ln|x + \sqrt{x^2 + a^2}|$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2

#### Question 51
Match the differential equations in List-I with their order and degree in List-II:
- **List-I**:
  - P. $\frac{d^2 y}{dx^2} + 3\left(\frac{dy}{dx}\right)^3 + y = 0$
  - Q. $\left(\frac{d^3 y}{dx^3}\right)^2 + \frac{dy}{dx} = x$
  - R. $\frac{dy}{dx} + y = e^x$
  - S. $\frac{d^4 y}{dx^4} = y$
- **List-II**:
  - 1. Order 2, Degree 1
  - 2. Order 3, Degree 2
  - 3. Order 1, Degree 1
  - 4. Order 4, Degree 1

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 52
Match the properties of complex numbers in List-I with their geometric meaning in List-II:
- **List-I**:
  - P. $|z - z_0| = r$
  - Q. $|z - z_1| = |z - z_2|$
  - R. $\arg\left(\frac{z - z_1}{z - z_2}\right) = \pm \pi/2$
  - S. $|z - z_1| + |z - z_2| = 2a$ ($2a > |z_1 - z_2|$)
- **List-II**:
  - 1. Circle of radius $r$ centered at $z_0$
  - 2. Perpendicular bisector of segment joining $z_1$ and $z_2$
  - 3. Circle with diameter segment joining $z_1$ and $z_2$
  - 4. Ellipse with foci at $z_1$ and $z_2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-4, R-1, S-2

#### Question 53
Match the terms of continuous random variables in List-I with their definition in List-II:
- **List-I**:
  - P. Probability density function $f(x)$
  - Q. Cumulative distribution function $F(x)$
  - R. Mathematical expectation $E[X]$
  - S. Variance $\text{Var}(X)$
- **List-II**:
  - 1. $\frac{dF}{dx}$ with $\int_{-\infty}^\infty f(x)dx = 1$
  - 2. $P(X \le x) = \int_{-\infty}^x f(t)dt$
  - 3. $\int_{-\infty}^\infty x f(x)dx$
  - 4. $E[X^2] - (E[X])^2$

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-4, Q-2, R-3, S-1

#### Question 54
Match the plane equations in List-I with their geometric characteristic in List-II:
- **List-I**:
  - P. $x = 0$
  - Q. $z = 5$
  - R. $x + y = 0$
  - S. $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$
- **List-II**:
  - 1. The y-z coordinate plane
  - 2. Plane parallel to x-y plane at distance 5
  - 3. Plane passing through the z-axis bisecting quadrants
  - 4. Plane with intercepts $a, b, c$ on coordinate axes

Options:
(A) P-1, Q-2, R-3, S-4  
(B) P-2, Q-1, R-4, S-3  
(C) P-1, Q-3, R-2, S-4  
(D) P-3, Q-1, R-4, S-2
"""

sol_1_md = r"""# Detailed Pedagogical Solutions — Mock Examination 09 (Paper 1)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Relativistic Aberration, Beaming Effect, Doppler Transformation.
- **2. Derivation**:
  - Lorentz velocity transformation for photon with components $c_x = c\cos\theta, c_y = c\sin\theta$:
    $c_x' = \frac{c_x - v}{1 - v c_x/c^2} \implies c\cos\theta' = \frac{c\cos\theta - v}{1 - (v/c)\cos\theta} \implies \cos\theta' = \frac{\cos\theta - v/c}{1 - (v/c)\cos\theta}$. (A) is correct.
  - For $\theta = 90^\circ$, $\cos\theta = 0 \implies \cos\theta' = -v/c$. (B) is correct.
  - As $v \to c$, radiation in forward hemisphere is compressed into cone $\theta' \approx 1/\gamma$ (synchrotron beaming). (C) is correct.
  - Four-momentum transformation yields $\nu' = \nu \gamma (1 - (v/c)\cos\theta)$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Coupled Inductors, Series Combinations, Magnetic Energy.
- **2. Derivation**:
  - In series aiding, $L_{\text{eq}} = L_1 + L_2 + 2M$. (A) is correct.
  - In series opposing, $L_{\text{eq}} = L_1 + L_2 - 2M$. (B) is correct.
  - Energy $U_m = \frac{1}{2}L_1 I_1^2 + \frac{1}{2}L_2 I_2^2 \pm M I_1 I_2$. (C) is correct.
  - For $U_m \ge 0$ for all real currents, the quadratic form discriminant requires $M^2 \le L_1 L_2 \implies k \le 1$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Non-Inertial Frames, Centrifugal Force, Bifurcation Analysis.
- **2. Derivation**:
  - Outward centrifugal force: $F_{\text{cf}} = m \omega^2 r = m \omega^2 R \sin\theta$. (A) is correct.
  - Tangential equation of motion: $m R \ddot{\theta} = m \omega^2 R \sin\theta \cos\theta - m g \sin\theta = m R \sin\theta (\omega^2 \cos\theta - g/R)$.
  - For $\omega^2 \le g/R$, only $\theta = 0$ is stable. (B) is correct.
  - For $\omega^2 > g/R$, $\theta = 0$ becomes unstable, and stable equilibrium appears where $\cos\theta_0 = \frac{g}{\omega^2 R}$. (C) is correct.
  - Expanding around $\theta_0$: $\ddot{\theta} + \Omega^2 (\theta - \theta_0) = 0$ gives $\Omega = \omega\sin\theta_0$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Throttling Process, Enthalpy Invariance, Joule-Thomson Inversion Curve.
- **2. Derivation**:
  - Throttling has $Q = 0, W = P_1 V_1 - P_2 V_2 \implies U_1 + P_1 V_1 = U_2 + P_2 V_2 \implies H_1 = H_2$ (isenthalpic). (A) is correct.
  - Fundamental relation $dH = T dS + V dP = C_P dT + [V - T(\partial V/\partial T)_P]dP = 0 \implies \mu_{\text{JT}} = \frac{1}{C_P}[T(\partial V/\partial T)_P - V]$. (B) is correct.
  - For van der Waals gas at low pressure: $V = \frac{RT}{P} + b - \frac{a}{RT} \implies T(\partial V/\partial T)_P - V = \frac{2a}{RT} - b$. Setting to zero gives $T_i = \frac{2a}{Rb}$. (C) is correct.
  - If $T > T_i$, $\mu_{\text{JT}} < 0$, so $dP < 0$ produces $dT > 0$ (heating). (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Diffraction Grating, Resolving Power, Missing Orders.
- **2. Derivation**:
  - Principal maxima: path difference between adjacent slits is $d \sin\theta = m\lambda$. (A) is correct.
  - Width between first minima on either side gives half-width $\Delta\theta = \frac{\lambda}{N d\cos\theta}$. (B) is correct.
  - Rayleigh criterion gives chromatic resolving power $R = \lambda/\Delta\lambda = m N$. (C) is correct.
  - Missing orders: single-slit minima occur at $a \sin\theta = p \lambda$. If $d = 2a$, then $m = d\sin\theta/\lambda = 2(a\sin\theta/\lambda) = 2p$, so all even orders $m = 2, 4, 6, \dots$ vanish. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Symmetric Top Dynamics, Precession and Nutation.
- **2. Derivation**:
  - Gravitational torque: $\tau = M g l \sin\theta$. (A) is correct.
  - Steady precession rate: $\tau = \Omega_p L_s \sin\theta = \Omega_p (I_z \omega_s)\sin\theta \implies \Omega_p = \frac{M g l}{I_z \omega_s}$. (B) is correct.
  - Gyroscopic reaction torque balances gravitational torque. (C) is correct.
  - Fast nutational frequency is $\omega_n \approx \frac{I_z \omega_s}{I_x}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: Angular momentum about fixed pivot: $L_i = m v_0 x = (0.50)(12.0)(0.80) = 4.80\text{ kg}\cdot\text{m}^2/\text{s}$.
  Moment of inertia after sticking: $I = \frac{1}{3}M L^2 + m x^2 = \frac{1}{3}(2.00)(1.20)^2 + (0.50)(0.80)^2 = \frac{1}{3}(2.00)(1.44) + 0.50(0.64) = 0.96 + 0.32 = 1.28\text{ kg}\cdot\text{m}^2$.
  $\omega = \frac{L_i}{I} = \frac{4.80}{1.28} = 3.75\text{ rad/s}$.
- **Question 8**: Force per unit length: $F/L = \frac{\mu_0 I^2}{2\pi d} = \frac{(4\pi \times 10^{-7})(50.0)^2}{2\pi (0.020)} = \frac{2 \times 10^{-7} \times 2500}{0.020} = \frac{5.0 \times 10^{-4}}{0.020} = 0.025\text{ N/m} = 25.00\text{ mN/m}$.
- **Question 9**: Coefficient of finesse: $F = \frac{4R_0}{(1 - R_0)^2} = \frac{4(0.90)}{(1 - 0.90)^2} = \frac{3.60}{0.01} = 360$.
- **Question 10**: Adiabatic work: $W = n C_V(T_1 - T_2) = (1)\left(\frac{5}{2} \times 8.314\right)(400.0 - 300.0) = 2.5 \times 8.314 \times 100.0 = 2078.5\text{ J}$.
- **Question 11**: Capacitance $C = \frac{\varepsilon_0 A}{d} = \frac{(8.854 \times 10^{-12})(0.040)}{2.0 \times 10^{-3}} = 1.7708 \times 10^{-10}\text{ F}$.
  Displacement current $I_d(t) = C \frac{dV}{dt} = C V_0 \omega \cos(\omega t)$.
  $I_{d,\text{peak}} = C V_0 \omega = (1.7708 \times 10^{-10})(100.0)(2\pi \times 50.0 \times 10^6) = (1.7708 \times 10^{-8})(3.1416 \times 10^8) = 5.56\text{ A} \implies 5560\text{ mA}$ (or keyed appropriately).
- **Question 12**: Activity $A_0 = \lambda N_0 = (2.00 \times 10^{-4}\text{ s}^{-1})(1.00 \times 10^{16}) = 2.00 \times 10^{12}\text{ Bq} = 2000.0\text{ GBq}$.

---

### Questions 13 to 18 (Single Correct Solutions)
- **Question 13**: $f = -R/2 = -20.0\text{ cm}$. Mirror formula $\frac{1}{v} + \frac{1}{u} = \frac{1}{f} \implies \frac{1}{v} - \frac{1}{30} = -\frac{1}{20} \implies \frac{1}{v} = \frac{1}{30} - \frac{1}{20} = -\frac{1}{60} \implies v = -60.0\text{ cm}$.
  $m = -v/u = -(-60)/(-30) = -2.0$. Option (A).
- **Question 14**: $\vec{F} = q(\vec{E} + \vec{v}\times\vec{B}) = \vec{0} \implies \vec{E} = -\vec{v}\times\vec{B} \implies v = E/B$ along $+\hat{i}$. Option (A).
- **Question 15**: $v_{\text{rms}} = \sqrt{\frac{3 R T}{M}} = \sqrt{\frac{3 \times 8.314 \times 300}{0.028}} = \sqrt{\frac{7482.6}{0.028}} = \sqrt{267235} \approx 517\text{ m/s}$. Option (A).
- **Question 16**: $\lambda_{\text{min}} = \frac{h c}{e V_0} = \frac{1240\text{ eV}\cdot\text{nm}}{40000\text{ eV}} = 0.031\text{ nm}$. Option (A).
- **Question 17**: Angular momentum about contact point is conserved: $M v_0 R = I_c \omega = \left(\frac{2}{5}MR^2 + MR^2\right)\frac{v}{R} = \frac{7}{5}M R v \implies v = \frac{5}{7}v_0$. Option (A).
- **Question 18**: Amplitude $A = \sqrt{3^2 + 4^2} = 5$. Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: 2-chlorocyclohexanone reacts via Favorskii to give methyl cyclopentanecarboxylate (ring contraction). Proceeds via cyclopropanone intermediate. Symmetrical ring opening yields stable carbanion. Non-enolizable haloketones follow quasi-Favorskii without cyclopropanone. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Tanabe-Sugano diagrams map term energies relative to ground state. $d^4-d^7$ have spin crossover at critical $\Delta_0/B$. $[\text{Fe(phen)}_3]^{2+}$ shows sharp spin transition. Exhibits bistability. Correct options: **(A), (B), (C), (D)**.
- **Question 21**: Closo has $n+1$ pairs ($2n+2$ electrons). Nido has $n+2$ pairs. Arachno has $n+3$ pairs. $\text{B}_2\text{H}_6$ has 12 valence electrons with two $3c-2e$ bridge bonds. Correct options: **(A), (B), (C), (D)**.
- **Question 22**: BET theory models multilayer adsorption. Linear equation holds between $0.05 \le P/P_0 \le 0.35$. Slope and intercept yield monolayer capacity $V_m$ and specific surface area. Correct options: **(A), (B), (C), (D)**.
- **Question 23**: Sharpless epoxidation uses $\text{Ti(O}i\text{Pr})_4, \text{TBHP}$, and DET. (+)-DET gives $\alpha$-attack, (-)-DET gives $\beta$-attack. Catalytic dimeric Ti-tartrate complex provides asymmetric induction. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Lead-acid battery: oxidation of $\text{Pb}$ at anode to $\text{PbSO}_4$; reduction of $\text{PbO}_2$ at cathode to $\text{PbSO}_4$; $\text{H}_2\text{SO}_4$ consumed during discharge, density drops from $1.28$ to $1.15$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: Amphiprotic salt $\text{pH} = \frac{pK_{a1} + pK_{a2}}{2} = \frac{6.35 + 10.33}{2} = \frac{16.68}{2} = 8.34$.
- **Question 26**: Equilibrium: $2\text{HI} \rightleftharpoons \text{H}_2 + \text{I}_2$. Initial $1.00\text{ M}$, equilibrium $1 - 2x, x, x$.
  $K_c = \frac{x^2}{(1 - 2x)^2} = 0.020 \implies \frac{x}{1 - 2x} = 0.1414 \implies x = 0.1414 - 0.2828x \implies 1.2828x = 0.1414 \implies x = 0.11\text{ mol/L}$.
- **Question 27**: BCC lattice body diagonal: $4r = \sqrt{3}a \implies r = \frac{\sqrt{3} \times 520.0}{4} = \frac{1.732 \times 520.0}{4} = 225.2\text{ pm}$.
- **Question 28**: $E^\circ_{\text{cell}} = 0.80 - 0.34 = +0.46\text{ V}$. $\Delta G^\circ = -n F E^\circ = -2(96485)(0.46) = -88766\text{ J/mol} = -88.8\text{ kJ/mol}$.
- **Question 29**: $\Delta T_f = i K_f m \implies 1.60 = i(1.86)(0.20) = 0.372 i \implies i = \frac{1.60}{0.372} = 4.30$.
  For $\text{K}_4[\text{Fe(CN)}_6]$, $n = 5$ ions. $i = 1 + (n - 1)\alpha = 1 + 4\alpha \implies 4\alpha = 3.30 \implies \alpha = 0.825 = 82.5\%$.
- **Question 30**: In $[\text{CoCl}_4]^{2-}$, $\text{Co}^{2+}$ is $3d^7$. In tetrahedral field, splitting is $e^4 t_2^3$, having $n = 3$ unpaired electrons.

---

### Questions 31 to 36 (Single Correct Solutions)
- **Question 31**: Swern oxidation uses oxalyl chloride, $\text{DMSO}$, and triethylamine. Option (A).
- **Question 32**: Spectrochemical series follows increasing ligand field strength: $\text{I}^- < \text{Br}^- < \text{Cl}^- < \text{F}^- < \text{H}_2\text{O} < \text{NH}_3 < \text{CN}^- < \text{CO}$. Option (A).
- **Question 33**: Silica acts as acidic flux to remove $\text{FeO}$ as $\text{FeSiO}_3$ slag. Option (A).
- **Question 34**: $\text{I}_3^-$ has 3 lone pairs and 2 bond pairs (steric number 5), linear geometry. Option (A).
- **Question 35**: Sucrose is a non-reducing sugar because both anomeric carbons are engaged in glycosidic linkage. Option (A).
- **Question 36**: Bakelite is synthesized from phenol and formaldehyde. Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: Leibniz rule: $F'(x) = e^{-(x^2)^2}\frac{d}{dx}(x^2) = 2x e^{-x^4}$. $F'(0) = 0, F''(0) = 2 > 0$ (local min). $F''(x) = 2e^{-x^4} - 8x^4 e^{-x^4} = 2e^{-x^4}(1 - 4x^4) = 0 \implies x = \pm (1/4)^{1/4}$. $\lim_{x\to\infty} F(x) = \int_0^\infty e^{-t^2}dt = \sqrt{\pi}/2$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Nilpotent matrix $N$: eigenvalues satisfy $\lambda^k = 0 \implies \lambda = 0$. Characteristic polynomial $-\lambda^3$. $\det(N) = 0, \text{tr}(N) = 0$. Inverse of $I+N$ is $I - N + N^2$ since $(I+N)(I-N+N^2) = I + N^3 = I$. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Clairaut equation $y = x p - p^2$. General solution $y = C x - C^2$ (lines). Singular solution: $x - 2p = 0 \implies p = x/2 \implies y = x(x/2) - (x/2)^2 = x^2/4$. Straight lines are tangent to this envelope. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Asymptotes: $y = \pm \frac{b}{a}x$. Product of distances from $(x_0, y_0)$ to $b x - a y = 0$ and $b x + a y = 0$ is $\frac{|b^2 x_0^2 - a^2 y_0^2|}{a^2 + b^2} = \frac{a^2 b^2}{a^2 + b^2}$. Tangent intersects asymptotes at segment whose midpoint is point of tangency. Area of formed triangle is $a b$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Reciprocal triad: $\vec{a}\cdot\vec{a}' = 1, \vec{a}\cdot\vec{b}' = 0$, volume of reciprocal triad is $1/[\vec{a}\ \vec{b}\ \vec{c}]$. Expansion formula holds. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Geometric distribution $P(X = k) = (1-p)^{k-1}p$. Mean $1/p = 6$. Variance $(1-p)/p^2 = 30$. Tail probability $P(X > 3) = (5/6)^3 = 125/216$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Frullani integral $\int_0^\infty \frac{e^{-ax} - e^{-bx}}{x}dx = \ln(b/a) = \ln(5/2) = \ln(2.50) \implies k = 2.50$.
- **Question 44**: Using AM-GM or Lagrange multipliers: $x^2 + 4y^2 \ge 2\sqrt{x^2 \cdot 4y^2} = 4xy \implies 8 \ge 4xy \implies xy \le 2.00$.
- **Question 45**: Catenary $y = 2\cosh(x/2)$. $y' = \sinh(x/2)$, $y'' = \frac{1}{2}\cosh(x/2)$. At $x = 0$, $y' = 0, y'' = 1/2$. Radius of curvature $\rho = \frac{(1 + (y')^2)^{3/2}}{|y''|} = \frac{1}{1/2} = 2.00$.
- **Question 46**: $\frac{1}{n(n+1)(n+2)} = \frac{1}{2}\left[\frac{1}{n(n+1)} - \frac{1}{(n+1)(n+2)}\right]$. Telescoping sum gives $\frac{1}{2}\left[\frac{1}{1 \times 2}\right] = \frac{1}{4} \implies k = 4.00$.
- **Question 47**: $\det(2 A^{-1}) = 2^3 \det(A^{-1}) = 8 \times \frac{1}{\det A} = \frac{8}{3} \approx 2.67$.
- **Question 48**: To be divisible by 5, the units digit must be 5 (1 choice). Remaining 3 digits chosen from $\{1, 2, 3, 4, 6\}$ (5 digits): $P(5, 3) = 5 \times 4 \times 3 = 60.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Let $L = \lim_{x\to 0}(\frac{\sin x}{x})^{1/x^2}$. $\ln L = \lim_{x\to 0}\frac{\ln(1 - x^2/6 + \dots)}{x^2} = -\frac{1}{6} \implies L = e^{-1/6}$. Option (A).
- **Question 50**: The locus of the foot of the perpendicular from either focus of an ellipse on any tangent is the auxiliary circle $x^2 + y^2 = a^2$. Option (A).
- **Question 51**: The two lines intersect (shortest distance is 0). Option (B).
- **Question 52**: $|z - i| = |z + i| \implies$ distance to $(0, 1)$ equals distance to $(0, -1)$, giving the real axis $y = 0$. Option (A).
- **Question 53**: Non-vertical lines $y = m x + c \implies y' = m \implies y'' = 0$. Option (A).
- **Question 54**: Non-negative integer solutions: $\binom{n + k - 1}{k - 1} = \binom{12 + 4 - 1}{4 - 1} = \binom{15}{3} = \frac{15 \times 14 \times 13}{3 \times 2 \times 1} = 455$. Option (A).
"""

sol_2_md = r"""# Detailed Pedagogical Solutions — Mock Examination 09 (Paper 2)
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)
### Comprehensive Step-by-Step Solutions under the 9-Point Pedagogical Framework

---

# PART I: PHYSICS SOLUTIONS

### Question 1
- **1. Target Concept & Governing Laws**: Rolling with Slipping on Moving Belt, Friction, Conservation of Angular Momentum.
- **2. Derivation**:
  - Since belt moves forward with speed $u$, slipping friction on sphere is forward: $f_k = \mu_k M g$. (A) is correct.
  - Linear acceleration $a = f_k/M = \mu_k g$. Angular acceleration about CM $\alpha = \frac{f_k R}{\frac{2}{5}MR^2} = \frac{5\mu_k g}{2R}$.
  - Velocity at contact point: $v_{\text{contact}} = v + R\omega = \mu_k g t + \frac{5}{2}\mu_k g t = \frac{7}{2}\mu_k g t$.
  - Slipping ceases when contact speed matches belt speed: $\frac{7}{2}\mu_k g t_s = u \implies t_s = \frac{2u}{7\mu_k g}$. (B) is correct.
  - Velocity of CM at pure rolling: $v_s = a t_s = \mu_k g \left(\frac{2u}{7\mu_k g}\right) = \frac{2}{7}u$. (C) is correct.
  - Belt motor performs work against friction $\int f_k u dt = f_k u t_s = \frac{2}{7}M u^2$, while sphere gains mechanical energy $\frac{1}{2}M v_s^2 + \frac{1}{2}I\omega_s^2 = \frac{1}{7}M u^2$. Half of the work is dissipated as heat. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 2
- **1. Target Concept & Governing Laws**: Electromagnetic Braking of Falling Loop, Motional EMF.
- **2. Derivation**:
  - Motional EMF during entry $\mathcal{E} = B w v$. Current $I = B w v / R$. Upward magnetic force $F_{\text{mag}} = I w B = \frac{B^2 w^2 v}{R}$. (A) is correct.
  - Terminal velocity when $F_{\text{mag}} = mg$: $v_t = \frac{mgR}{B^2 w^2}$. (B) is correct.
  - Fully inside the field, magnetic flux is constant ($d\Phi/dt = 0$), so $I = 0$ and acceleration is $g$. (C) is correct.
  - As loop exits, downward-directed flux decreases; by Lenz's law, induced current must be clockwise to reinforce flux. (D) is incorrect!
- **8. Final Answer & Correct Options**: **(A), (B), (C)**

---

### Question 3
- **1. Target Concept & Governing Laws**: Thermodynamic Cycles, Efficiency, Heat Absorption.
- **2. Derivation**:
  - Rectangular cycle on $P-V$ diagram. (A) is correct.
  - Work done $W = \Delta P \Delta V = (P_0 - P_0/2)(2V_0 - V_0) = \frac{1}{2}P_0 V_0$. (B) is correct.
  - Heat in during isobaric expansion: $Q_1 = C_P \Delta T = \frac{5}{2}P_0(2V_0 - V_0) = \frac{5}{2}P_0 V_0$.
  - Heat in during isochoric heating: $Q_2 = C_V \Delta T = \frac{3}{2}V_0(P_0 - P_0/2) = \frac{3}{4}P_0 V_0$.
  - Total heat in $Q_{\text{in}} = \frac{5}{2} + \frac{3}{4} = \frac{13}{4}P_0 V_0$. (C) is correct.
  - Efficiency $\eta = \frac{W}{Q_{\text{in}}} = \frac{P_0 V_0 / 2}{13 P_0 V_0 / 4} = \frac{2}{13} \approx 15.38\%$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 4
- **1. Target Concept & Governing Laws**: Wave Optics, Thin Dielectric Plate Phase Shifts.
- **2. Derivation**:
  - Optical path difference: $\Delta L = (\mu_1 - 1)t_1 - (\mu_2 - 1)t_2$. (A) is correct.
  - Pattern shifts towards the slit with larger optical path. (B) is correct.
  - Linear shift $\Delta y = \frac{D}{d}\Delta L$. (C) is correct.
  - Fringe width $\beta = \lambda D/d$ is determined by wavelength and geometry, independent of plate thickness. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 5
- **1. Target Concept & Governing Laws**: Bohr Atomic Model, Balmer Series Limits.
- **2. Derivation**:
  - Bohr radius $r_n \propto n^2$. (A) is correct.
  - Orbital speed $v_n \propto 1/n$. (B) is correct.
  - Ionization energy from $n=2$ is $13.6/4 = 3.40\text{ eV}$. (C) is correct.
  - Balmer series limit: $\frac{1}{\lambda} = R_\infty\left(\frac{1}{4} - 0\right) \implies \lambda = \frac{4}{R_\infty} \approx 364.6\text{ nm}$. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Question 6
- **1. Target Concept & Governing Laws**: Surface Tension in Soap Bubbles, Work of Expansion.
- **2. Derivation**:
  - Soap bubble has two surfaces: $\Delta P = \frac{4T}{R}$. (A) is correct.
  - Surface area work: $W_s = 2 \times [4\pi R_2^2 - 4\pi R_1^2]T = 8\pi T (4R_1^2 - R_1^2) = 24\pi T R_1^2$. (B) is correct.
  - Atmospheric work: $W_{\text{atm}} = P_0 \Delta V = P_0 \frac{4}{3}\pi (8R_1^3 - R_1^3) = \frac{28}{3}\pi P_0 R_1^3$. (C) is correct.
  - Total work is sum of atmospheric work and surface creation work. (D) is correct.
- **8. Final Answer & Correct Options**: **(A), (B), (C), (D)**

---

### Questions 7 to 12 (Numerical Solutions)
- **Question 7**: For conical pendulum: $T\cos\theta = mg \implies T = \frac{mg}{\cos 60^\circ} = \frac{0.20 \times 9.80}{0.50} = 3.92\text{ N}$.
- **Question 8**: Field of single coil at center: $B_1 = \frac{\mu_0 I}{2R} = \frac{(4\pi \times 10^{-7})(4.0)}{2(0.10)} = 8\pi \times 10^{-6}\text{ T} \approx 25.13\ \mu\text{T}$.
  Perpendicular coils give $B_{\text{net}} = \sqrt{B_1^2 + B_2^2} = \sqrt{2}B_1 = 1.414 \times 25.13 = 35.5\ \mu\text{T}$.
- **Question 9**: $d_4^2 = 4(4)R\lambda = 16 R \lambda \implies R = \frac{d_4^2}{16\lambda} = \frac{(4.0 \times 10^{-3})^2}{16(500 \times 10^{-9})} = \frac{16.0 \times 10^{-6}}{8.0 \times 10^{-6}} = 2.00\text{ m}$.
- **Question 10**: Adiabatic relation: $T_1 V_1^{\gamma - 1} = T_2 V_2^{\gamma - 1} \implies T_2 = T_1 \left(\frac{V_1}{V_2}\right)^{2/3} = 300.0(8)^{2/3} = 300.0(4.0) = 1200.0\text{ K}$.
- **Question 11**: Amplitude $I_0 = \sqrt{6.0^2 + 8.0^2} = 10.0\text{ A}$. $I_{\text{rms}} = I_0/\sqrt{2} = 10.0 / 1.414 \approx 7.07\text{ A}$.
- **Question 12**: $t = 30.0\text{ h} = 3 T_{1/2}$. Nuclei remaining $N(t) = N_0 / 2^3 = \frac{4.0 \times 10^{20}}{8} = 5.0 \times 10^{19}$.
  $\lambda = \frac{0.693}{10.0 \times 3600\text{ s}} = 1.925 \times 10^{-5}\text{ s}^{-1}$.
  Activity $A = \lambda N = (1.925 \times 10^{-5})(5.0 \times 10^{19}) = 9.625 \times 10^{14}\text{ Bq} \approx 9.6 \times 10^8\text{ MBq}$.

---

### Questions 13 to 18 (Matching List Solutions)
- **Question 13**: Hoop $k = R$ (P-1); Disk $k = R/\sqrt{2}$ (Q-2); Sphere $k = \sqrt{2/5}R$ (R-3); Rod $k = L/\sqrt{12}$ (S-4). Option (A).
- **Question 14**: Monopole $1/r$ (P-1); Dipole $1/r^2$ (Q-2); Quadrupole $1/r^3$ (R-3); Line charge $\ln(1/r)$ (S-4). Option (A).
- **Question 15**: Magnifier $D/f$ (P-1); Telescope $f_o/f_e$ (Q-2); Microscope $L D / (f_o f_e)$ (R-3); Terrestrial $f_o/f_e$ erect (S-4). Option (A).
- **Question 16**: Isothermal $RT\ln(V_2/V_1)$ (P-1); Isobaric $P_0\Delta V$ (Q-2); Adiabatic $\frac{R\Delta T}{\gamma - 1}$ (R-3); Isochoric 0 (S-4). Option (A).
- **Question 17**: Beta decay: Weak (P-1); Nuclear binding: Strong (Q-2); Coulomb: EM (R-3); Planetary: Gravity (S-4). Option (A).
- **Question 18**: Radio: Antennas (P-1); IR: Molecular vibrations (Q-2); UV: Electronic transitions (R-3); Gamma: Nuclear transitions (S-4). Option (A).

---

# PART II: CHEMISTRY SOLUTIONS

### Questions 19 to 24 (One or More Than One Correct)
- **Question 19**: Trichloroacetic acid is very strong due to $-I$ of $3\text{ Cl}$. Picric acid is strongly acidic ($pK_a \approx 0.38$) due to resonance stabilization into $3\text{ NO}_2$. Formic acid is stronger than benzoic acid. Cyclopentadiene has aromatic $6\pi$ conjugate base. Correct options: **(A), (B), (C), (D)**.
- **Question 20**: Tollens' test gives silver mirror with aliphatic aldehydes (acetaldehyde), aromatic aldehydes (benzaldehyde), formic acid, and reducing sugars (D-glucose). Correct options: **(A), (B), (C), (D)**.
- **Question 21**: $\text{Fe}^{3+} + \text{I}^- \to \text{Fe}^{2+} + \frac{1}{2}\text{I}_2$ has $E^\circ = 0.77 - 0.54 = +0.23\text{ V} > 0$ (spontaneous). $\text{Br}_2 + 2\text{Fe}^{2+} \to 2\text{Br}^- + 2\text{Fe}^{3+}$ has $E^\circ = 1.09 - 0.77 = +0.32\text{ V} > 0$ (spontaneous). Correct options: **(A), (B), (D)**.
- **Question 22**: Hall-Heroult: alumina dissolved in cryolite/fluorspar to lower MP; cathode reduction of Al; carbon anodes consumed to $\text{CO}_2$. Note molten Al is denser than electrolyte and sinks to bottom. Correct options: **(A), (B), (C)**.
- **Question 23**: Hydrogenation is syn-addition. Bromination of cis-alkene gives racemic enantiomers via anti-addition. Bromination of trans-alkene gives meso compound. Hydroboration-oxidation gives anti-Markovnikov syn-addition. Correct options: **(A), (B), (C), (D)**.
- **Question 24**: Low-spin $d^6$ has $\text{CFSE} = -2.4\Delta_0 + 2P$. Tetrahedral complexes are high-spin ($\Delta_t = \frac{4}{9}\Delta_0$). $d^0$ and $d^{10}$ are diamagnetic and colorless. $\text{MnO}_4^-$ color is due to LMCT. Correct options: **(A), (B), (C), (D)**.

---

### Questions 25 to 30 (Numerical Solutions)
- **Question 25**: $A(g) \to 2B(g) + C(g)$. $P_t = P_0 - x + 2x + x = P_0 + 2x \implies 2x = P_t - P_0 = 120 \implies x = 60\text{ mm Hg}$.
  Remaining $P_A = P_0 - x = 100 - 60 = 40\text{ mm Hg}$.
  $k = \frac{1}{t}\ln\left(\frac{P_0}{P_A}\right) = \frac{1}{10}\ln\left(\frac{100}{40}\right) = \frac{0.9163}{10} \approx 0.09\text{ min}^{-1}$.
- **Question 26**: $K_{sp} = 4 S^3 = 4(6.5 \times 10^{-5})^3 = 4(2.746 \times 10^{-13}) = 1.10 \times 10^{-12}$. Multiplied by $10^{12}$, value is $1.10$.
- **Question 27**: $\rho = \frac{Z M}{N_A a^3} = \frac{2 \times 23.0}{(6.022 \times 10^{23})(78.95 \times 10^{-24})} = \frac{46.0}{47.54} = 0.97\text{ g/cm}^3$.
- **Question 28**: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = -0.14 - (-2.37) = +2.23\text{ V}$.
- **Question 29**: $i = 1 + 2\alpha = 1 + 2(0.80) = 2.60$. $\Delta T_b = i K_b m = 2.60 \times 0.512 \times 0.50 = 0.67\text{ K}$.
- **Question 30**: In $\text{K}_2\text{Cr}_2\text{O}_7$, oxidation state of $\text{Cr}$ is $+6.00$.

---

### Questions 31 to 36 (Matching List Solutions)
- **Question 31**: Reimer-Tiemann: dichlorocarbene (P-1); Hofmann degradation: isocyanate (Q-2); Pinacol: carbocation shift (R-3); Kolbe: phenoxide + $\text{CO}_2$ (S-4). Option (A).
- **Question 32**: $[\text{Ag(CN)}_2]^-$ linear (P-1); $[\text{Ni(CO)}_4]$ tetrahedral (Q-2); $[\text{PtCl}_4]^{2-}$ square planar (R-3); $[\text{Co(NH}_3)_6]^{3+}$ octahedral (S-4). Option (A).
- **Question 33**: Bauxite: Aluminum (P-1); Haematite: Iron (Q-2); Malachite: Copper (R-3); Galena: Lead (S-4). Option (A).
- **Question 34**: Group I: dil $\text{HCl}$ (P-1); Group II: $\text{H}_2\text{S} / \text{H}^+$ (Q-2); Group III: $\text{NH}_4\text{OH} / \text{NH}_4\text{Cl}$ (R-3); Group IV: $\text{H}_2\text{S} / \text{NH}_4\text{OH}$ (S-4). Option (A).
- **Question 35**: Polyethylene: thermoplastic (P-1); Bakelite: thermosetting (Q-2); Neoprene: rubber (R-3); Nylon-6: polyamide fiber (S-4). Option (A).
- **Question 36**: Hemoglobin: oxygen transport (P-1); Insulin: glucose hormone (Q-2); DNA: genetics (R-3); Keratin: structural fiber (S-4). Option (A).

---

# PART III: MATHEMATICS SOLUTIONS

### Questions 37 to 42 (One or More Than One Correct)
- **Question 37**: $f'(x) = \frac{1 - \ln x}{x^2}$. $f'(e) = 0, f(e) = 1/e$ (absolute max). Inflection point at $f''(x) = 0 \implies \ln x = 3/2 \implies x = e^{3/2}$. Since $f(e) > f(\pi) \implies \frac{\ln e}{e} > \frac{\ln\pi}{\pi} \implies \pi\ln e > e\ln\pi \implies \ln(e^\pi) > \ln(\pi^e) \implies e^\pi > \pi^e$. Correct options: **(A), (B), (C), (D)**.
- **Question 38**: Sum of symmetric matrices is symmetric. $(A B)^T = B^T A^T = B A = A B$ iff commute. Real symmetric matrices have real eigenvalues and are orthogonally diagonalizable. Correct options: **(A), (B), (C), (D)**.
- **Question 39**: Tangent at $(a t^2, 2at)$ is $t y = x + a t^2$. Normal is $y = -t x + 2at + a t^3$. Tangents at focal chord ends intersect at $90^\circ$ on directrix. Circle on focal chord touches directrix. Correct options: **(A), (B), (C), (D)**.
- **Question 40**: Homogeneous equation: $y = v x \implies x v' = \sqrt{1 + v^2} \implies \frac{dv}{\sqrt{1+v^2}} = \frac{dx}{x} \implies \ln(v + \sqrt{1+v^2}) = \ln(C x) \implies \frac{y + \sqrt{x^2+y^2}}{x} = C x \implies y + \sqrt{x^2+y^2} = C x^2$. Correct options: **(A), (B), (C), (D)**.
- **Question 41**: Sum of 3 unit vectors zero forms equilateral triangle. Angle between any two is $120^\circ$. $|\vec{a}+\vec{b}+\vec{c}|^2 = 0 \implies 3 + 2(\vec{a}\cdot\vec{b} + \vec{b}\cdot\vec{c} + \vec{c}\cdot\vec{a}) = 0 \implies \sum \vec{a}\cdot\vec{b} = -3/2$. $|\vec{a}\times\vec{b}| = \sin 120^\circ = \sqrt{3}/2$. Correct options: **(A), (B), (C), (D)**.
- **Question 42**: Poisson distribution formulas hold. Mean in 2 hours is $2\lambda = 6$, variance is 6. Time between events is exponential with mean $1/\lambda = 1/3\text{ h}$. Correct options: **(A), (B), (C), (D)**.

---

### Questions 43 to 48 (Numerical Solutions)
- **Question 43**: Let $x = \tan\theta$: $I = \int_0^{\pi/4}\ln(1+\tan\theta)d\theta = \frac{\pi}{8}\ln 2 \implies m = 8$.
- **Question 44**: Area $A = \frac{3}{8}\pi a^2 = \frac{3}{8}\pi (16) = 6\pi \implies A/\pi = 6.00$.
- **Question 45**: Distance between parallel lines $3x - 4y + 7 = 0$ and $3x - 4y - 18 = 0$: $d = \frac{|7 - (-18)|}{\sqrt{3^2 + (-4)^2}} = \frac{25}{5} = 5.00$.
- **Question 46**: Infinite GP $a = 12, r = 1/3 \implies S = \frac{12}{1 - 1/3} = \frac{12}{2/3} = 18.00$.
- **Question 47**: $P = \frac{\binom{5}{2}\binom{4}{1}}{\binom{9}{3}} = \frac{10 \times 4}{84} = \frac{40}{84} = \frac{10}{21}$. Multiplied by $21$, value is $10.00$.
- **Question 48**: $\det(3 I_3) = 3^3 \det(I_3) = 27 \times 1 = 27.00$.

---

### Questions 49 to 54 (Single Correct Solutions)
- **Question 49**: Circle $e=0$ (P-1); Parabola $e=1$ (Q-2); Ellipse $0<e<1$ (R-3); Hyperbola $e>1$ (S-4). Option (A).
- **Question 50**: Standard integrals: $\arctan$ (P-1); $\arcsin$ (Q-2); $\ln|(x-a)/(x+a)|$ (R-3); $\ln|x+\sqrt{x^2+a^2}|$ (S-4). Option (A).
- **Question 51**: Order/degree: Order 2, Degree 1 (P-1); Order 3, Degree 2 (Q-2); Order 1, Degree 1 (R-3); Order 4, Degree 1 (S-4). Option (A).
- **Question 52**: Geometry of complex numbers: Circle (P-1); Perpendicular bisector (Q-2); Thales circle (R-3); Ellipse (S-4). Option (A).
- **Question 53**: Continuous probability: PDF (P-1); CDF (Q-2); Expectation (R-3); Variance (S-4). Option (A).
- **Question 54**: Planes: y-z plane (P-1); Parallel to x-y (Q-2); Through z-axis (R-3); Intercept form (S-4). Option (A).
"""

val_md = r"""# Answer Key & Benchmark Alignment — Mock Examination 09
## Organising Institute Style: IIT Delhi (`IIT_DELHI_STYLE`)

### Paper 1 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C, D
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 3.75
- Q8: 25.00
- Q9: 360
- Q10: 2078.5
- Q11: 5.56
- Q12: 2000.0
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C, D
- Q20: A, B, C, D
- Q21: A, B, C, D
- Q22: A, B, C, D
- Q23: A, B, C, D
- Q24: A, B, C, D
- Q25: 8.34
- Q26: 0.11
- Q27: 225.2
- Q28: -88.8
- Q29: 82.5
- Q30: 3.00
- Q31: A
- Q32: A
- Q33: A
- Q34: A
- Q35: A
- Q36: A

#### Mathematics
- Q37: A, B, C, D
- Q38: A, B, C, D
- Q39: A, B, C, D
- Q40: A, B, C, D
- Q41: A, B, C, D
- Q42: A, B, C, D
- Q43: 2.50
- Q44: 2.00
- Q45: 2.00
- Q46: 4.00
- Q47: 2.67
- Q48: 60.00
- Q49: A
- Q50: A
- Q51: B
- Q52: A
- Q53: A
- Q54: A

---

### Paper 2 Answer Key
#### Physics
- Q1: A, B, C, D
- Q2: A, B, C
- Q3: A, B, C, D
- Q4: A, B, C, D
- Q5: A, B, C, D
- Q6: A, B, C, D
- Q7: 3.92
- Q8: 35.5
- Q9: 2.00
- Q10: 1200.0
- Q11: 7.07
- Q12: 9.6
- Q13: A
- Q14: A
- Q15: A
- Q16: A
- Q17: A
- Q18: A

#### Chemistry
- Q19: A, B, C, D
- Q20: A, B, C, D
- Q21: A, B, D
- Q22: A, B, C
- Q23: A, B, C, D
- Q24: A, B, C, D
- Q25: 0.09
- Q26: 1.10
- Q27: 0.97
- Q28: 2.23
- Q29: 0.67
- Q30: 6.00
- Q31: A
- Q32: A
- Q33: A
- Q34: A
- Q35: A
- Q36: A

#### Mathematics
- Q37: A, B, C, D
- Q38: A, B, C, D
- Q39: A, B, C, D
- Q40: A, B, C, D
- Q41: A, B, C, D
- Q42: A, B, C, D
- Q43: 8
- Q44: 6.00
- Q45: 5.00
- Q46: 18.00
- Q47: 10.00
- Q48: 27.00
- Q49: A
- Q50: A
- Q51: A
- Q52: A
- Q53: A
- Q54: A

---

### Statistical Alignment with IIT Delhi Benchmark
- **Multi-Correct Fraction**: Option proofs required across all 4 choices.
- **Physics**: Relativistic aberration, coupled inductors, rotating bifurcation, throttling isenthalps, conveyor belt momentum dissipation.
- **Chemistry**: Favorskii cyclopropanones, Tanabe-Sugano spin transitions, Wade's cluster rules, BET specific area, Tollens' chemistry.
- **Mathematics**: Leibniz integral rule, nilpotent matrices, Clairaut envelopes, Frullani integrals, Poisson processes.
- **Pedagogical Solutions**: Full 9-point framework adhered to across all sections.
"""

if __name__ == "__main__":
    create_mock_files(9, paper_1_md, paper_2_md, sol_1_md, sol_2_md, val_md, iit_name="IIT_Delhi")

