# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 15.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Relativistic Doppler shift at arbitrary angle, Fresnel biprism, Rotating liquid paraboloid surface
- Swern oxidation, Wittig reaction E/Z stereochemistry, Jahn-Teller Cu(II) distortion, Kohlrausch law
- Cauchy-Schwarz L2 integral inequalities, Lagrange multipliers, Pascal's mystic hexagram, Stirling numbers
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 15 — Paper 1
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
A cylindrical vessel of radius $R$ containing an incompressible, non-viscous liquid of density $\rho$ rotates with uniform angular velocity $\omega$ about its vertical axis of symmetry:
(A) The free surface of the liquid assumes the shape of a paraboloid of revolution given by $z(r) = z_0 + \frac{\omega^2 r^2}{2g}$.  
(B) The difference in liquid height between the rim ($r = R$) and the center ($r = 0$) is $h = \frac{\omega^2 R^2}{2g}$.  
(C) By conservation of liquid volume, the central depression below the initial rest height $H_0$ is equal to the elevation at the rim: $\Delta z_{\text{center}} = \Delta z_{\text{rim}} = \frac{\omega^2 R^2}{4g}$.  
(D) The pressure distribution inside the liquid at depth $y$ below the local free surface is hydrostatic: $P(r, z) = P_{\text{atm}} + \rho g [z(r) - z]$.

#### Question 2
In a Fresnel biprism experiment with refracting angle $\alpha \ll 1\text{ rad}$ and refractive index $\mu$, a narrow slit source emitting light of wavelength $\lambda$ is placed at distance $u$ behind the biprism, and an observation screen is placed at distance $D$ from the biprism ($D \gg u$):
(A) The biprism produces two virtual coherent slit sources separated by a distance $d = 2u(\mu - 1)\alpha$.  
(B) The fringe width observed on the screen is $\beta = \frac{\lambda (u + D)}{d} = \frac{\lambda (u + D)}{2u(\mu - 1)\alpha}$.  
(C) When a convex lens is placed between the biprism and the screen, forming two real images of the virtual sources with separations $d_1$ and $d_2$ at two conjugate positions of the lens, the separation $d = \sqrt{d_1 d_2}$.  
(D) Inserting a thin transparent mica sheet of thickness $t$ and refractive index $\mu_m$ in the path of one interfering beam shifts the central bright fringe by $\Delta x = \frac{(u + D)}{d}(\mu_m - 1)t$.

#### Question 3
A light source moving with relativistic speed $v = \beta c$ emits a photon of proper frequency $\nu_0$ at angle $\theta$ relative to its direction of motion in the lab frame:
(A) The observed frequency in the lab frame is $\nu = \nu_0 \frac{\sqrt{1 - \beta^2}}{1 - \beta \cos\theta}$.  
(B) For purely longitudinal motion towards the observer ($\theta = 0$), $\nu = \nu_0 \sqrt{\frac{1 + \beta}{1 - \beta}}$.  
(C) For purely longitudinal motion away from the observer ($\theta = \pi$), $\nu = \nu_0 \sqrt{\frac{1 - \beta}{1 + \beta}}$.  
(D) When the emitted photon is perpendicular to the motion in the emitter's rest frame ($\theta' = 90^\circ$), the observed frequency is $\nu = \frac{\nu_0}{\sqrt{1 - \beta^2}} = \gamma \nu_0$.

#### Question 4
Regarding the Maxwell-Boltzmann molecular speed distribution $f(v) = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 e^{-\frac{m v^2}{2 k_B T}}$ for an ideal gas of molar mass $M$:
(A) The most probable speed is $v_{\text{mp}} = \sqrt{\frac{2 R T}{M}}$.  
(B) The average speed is $\langle v \rangle = \sqrt{\frac{8 R T}{\pi M}}$.  
(C) The root-mean-square speed is $v_{\text{rms}} = \sqrt{\frac{3 R T}{M}}$.  
(D) The speeds satisfy the strict ordering: $v_{\text{mp}} < \langle v \rangle < v_{\text{rms}}$ in the ratio $\sqrt{2} : \sqrt{8/\pi} : \sqrt{3} \approx 1 : 1.128 : 1.225$.

#### Question 5
A conducting spherical shell of inner radius $a$ and outer radius $b$ carries a net charge $+Q$. A point charge $+q$ is placed inside the cavity at an off-center position at distance $d < a$ from the geometric center $O$:
(A) The total induced charge on the inner surface of the shell ($r = a$) is $-q$, distributed non-uniformly.  
(B) The total charge on the outer surface of the shell ($r = b$) is $+(Q + q)$, distributed strictly uniformly.  
(C) The electric field outside the shell ($r > b$) is purely radial and given by $\vec{E} = \frac{Q + q}{4\pi \varepsilon_0 r^2}\hat{r}$, completely independent of $d$.  
(D) The electrostatic potential at the geometric center $O$ is $V_O = \frac{1}{4\pi\varepsilon_0}\left(\frac{q}{d} - \frac{q}{a} + \frac{Q+q}{b}\right)$.

#### Question 6
An inductor of inductance $L$ and internal resistance $R$ is connected in parallel with a capacitor of capacitance $C$ across an AC voltage source $V(t) = V_0 \sin(\omega t)$:
(A) The system exhibits parallel resonance (antiresonance) at angular frequency $\omega_0 = \sqrt{\frac{1}{L C} - \frac{R^2}{L^2}}$ provided $R < \sqrt{L/C}$.  
(B) At antiresonance, the total admittance is purely real (conductance) and minimum, so total circuit current is minimum.  
(C) The dynamic impedance of the parallel tank circuit at antiresonance is $Z_{\text{dynamic}} = \frac{L}{C R}$.  
(D) If $R = 0$, the antiresonant frequency is $\omega_0 = \frac{1}{\sqrt{LC}}$ and the dynamic impedance becomes infinite.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A cylindrical container of radius $R = 0.20\text{ m}$ is filled with water to a depth $H_0 = 0.40\text{ m}$. The container is rotated about its vertical axis of symmetry. The maximum angular velocity $\omega_{\text{max}}$ in $\text{rad/s}$ at which the container can be rotated without any water spilling over the rim of total container height $H_{\text{rim}} = 0.60\text{ m}$ is $\omega_{\text{max}}$. Taking $g = 9.8\text{ m/s}^2$, calculate $\omega_{\text{max}}$ in $\text{rad/s}$ (round off to TWO decimal places).

#### Question 8
In a Fresnel biprism experiment using light of wavelength $\lambda = 600\text{ nm}$, the distance between the slit and the screen is $D_{\text{total}} = 1.20\text{ m}$. A convex lens inserted between the biprism and screen produces sharp images of the two virtual sources at two positions with separations $d_1 = 4.5\text{ mm}$ and $d_2 = 0.5\text{ mm}$. Calculate the fringe width $\beta$ in millimeters (round off to TWO decimal places).

#### Question 9
A spaceship moves away from Earth with speed $v = 0.60 c$. It emits a green laser pulse of wavelength $\lambda_0 = 500\text{ nm}$ straight back towards Earth. Calculate the wavelength $\lambda_{\text{rec}}$ of the pulse received on Earth in nanometers.

#### Question 10
In a series $LCR$ circuit, $R = 10\text{ }\Omega$, $L = 100\text{ mH}$, and $C = 10\text{ }\mu\text{F}$. The circuit is driven by an AC source of voltage $V_{\text{rms}} = 220\text{ V}$. Calculate the quality factor $Q$ of the circuit (round off to the nearest integer).

#### Question 11
A spherical soap bubble of radius $R = 2.0\text{ cm}$ has surface tension $T = 0.030\text{ N/m}$. The excess pressure $\Delta P$ inside the bubble compared to atmospheric pressure is $\Delta P\text{ Pa}$. Calculate $\Delta P$ in Pascals.

#### Question 12
A thermodynamic engine operates on an ideal Otto cycle with compression ratio $r = V_1 / V_2 = 8.0$. The working substance is a diatomic ideal gas with $\gamma = 1.40$. The theoretical thermal efficiency $\eta$ of the cycle is $\eta\%$. Calculate $\eta$ (take $8^{0.4} \approx 2.30$, round off to ONE decimal place).

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle of mass $m$ is suspended from a ceiling by a light inextensible string of length $L$. It is projected horizontally with velocity $v_0 = \sqrt{3 g L}$ from its lowest position. The height $h$ above the lowest point at which the string becomes slack is:
(A) $h = \frac{5}{3} L$  
(B) $h = \frac{4}{3} L$  
(C) $h = \frac{3}{2} L$  
(D) $h = 2 L$  

#### Question 14
Two large parallel conducting plates separated by distance $d$ have surface charge densities $+\sigma$ and $-\sigma$. A dielectric slab of dielectric constant $\kappa$ and thickness $t < d$ is inserted between the plates. The potential difference between the plates is:
(A) $V = \frac{\sigma}{\varepsilon_0}\left(d - t + \frac{t}{\kappa}\right)$  
(B) $V = \frac{\sigma d}{\varepsilon_0 \kappa}$  
(C) $V = \frac{\sigma}{\varepsilon_0}\left(d - \frac{t}{\kappa}\right)$  
(D) $V = \frac{\sigma}{\varepsilon_0}(d + \kappa t)$  

#### Question 15
A uniform solid sphere rolls without slipping up a rough inclined plane of inclination angle $\theta = 30^\circ$. The linear deceleration of the center of mass of the sphere is:
(A) $a = \frac{5}{7} g \sin\theta = \frac{5}{14} g$  
(B) $a = \frac{2}{7} g \sin\theta$  
(C) $a = g \sin\theta$  
(D) $a = \frac{3}{5} g \sin\theta$  

#### Question 16
An electron in a hydrogen atom makes a transition from $n = 3$ to $n = 1$. The recoil speed of the hydrogen atom of mass $M_H = 1.67 \times 10^{-27}\text{ kg}$ is approximately (Rydberg energy $R_\infty = 13.6\text{ eV}$):
(A) $3.25\text{ m/s}$  
(B) $1.63\text{ m/s}$  
(C) $6.50\text{ m/s}$  
(D) $0.81\text{ m/s}$  

#### Question 17
A Carnot engine has an efficiency of $40\%$ when the sink temperature is $300\text{ K}$. If the source temperature is kept constant and the efficiency is to be increased to $50\%$, the sink temperature must be reduced to:
(A) $250\text{ K}$  
(B) $240\text{ K}$  
(C) $200\text{ K}$  
(D) $270\text{ K}$  

#### Question 18
The magnetic field at the center of an equilateral triangular loop of side length $a$ carrying a steady current $I$ is:
(A) $B = \frac{9 \mu_0 I}{2\pi a}$  
(B) $B = \frac{3 \mu_0 I}{2\pi a}$  
(C) $B = \frac{9 \sqrt{3} \mu_0 I}{2\pi a}$  
(D) $B = \frac{6 \mu_0 I}{\pi a}$  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Swern oxidation of primary and secondary alcohols using oxalyl chloride ($(\text{COCl})_2$), dimethyl sulfoxide (DMSO), and triethylamine ($\text{Et}_3\text{N}$):
(A) The active electrophilic chlorinating intermediate is dimethylchlorosulfonium chloride ($[\text{Me}_2\text{S-Cl}]^+\text{Cl}^-$) generated with extrusion of $\text{CO}_2$ and $\text{CO}$.  
(B) Nucleophilic attack of the alcohol oxygen on the sulfonium center forms an alkoxysulfonium intermediate with loss of $\text{HCl}$.  
(C) Addition of triethylamine deprotonates the methyl group to form an alkoxysulfonium ylide, which undergoes intramolecular syn-elimination via a five-membered cyclic transition state.  
(D) Over-oxidation of primary alcohols to carboxylic acids does not occur, providing aldehydes in excellent yield.

#### Question 20
In the Wittig reaction:
$$\text{R}_1\text{R}_2\text{C}=\text{O} + \text{Ph}_3\text{P}=\text{CH-R}_3 \to \text{R}_1\text{R}_2\text{C}=\text{CH-R}_3 + \text{Ph}_3\text{P}=\text{O}$$
(A) Non-stabilized phosphonium ylides ($\text{R}_3 = \text{alkyl}$) react under kinetic control to give predominantly $(Z)$-alkenes via an oxaphosphetane intermediate.  
(B) Stabilized phosphonium ylides ($\text{R}_3 = \text{ester, ketone, CN}$) react under thermodynamic control to give predominantly $(E)$-alkenes.  
(C) The driving force for the reaction is the formation of the exceptionally strong phosphorus-oxygen bond in triphenylphosphine oxide ($\text{Ph}_3\text{P}=\text{O}$, bond energy $\sim 540\text{ kJ/mol}$).  
(D) The Horner-Wadsworth-Emmons (HWE) modification utilizes phosphonate esters ($(\text{EtO})_2\text{P}(=\text{O})\text{CH}_2\text{EWG}$) to selectively synthesize $(E)$-$\alpha,\beta$-unsaturated esters.

#### Question 21
Regarding the Jahn-Teller theorem for octahedral transition metal complexes:
(A) Any non-linear molecular system in a spatially degenerate electronic ground state will undergo spontaneous geometric distortion to remove the degeneracy and lower the overall electronic energy.  
(B) Octahedral $d^9$ copper(II) complexes ($t_{2g}^6 e_g^3$) exhibit strong Jahn-Teller distortion, typically causing tetragonal elongation along the $z$-axis ($d_{z^2}$ stabilized, $d_{x^2-y^2}$ destabilized).  
(C) Octahedral high-spin $d^4$ complexes ($t_{2g}^3 e_g^1$, e.g., $\text{Cr}^{2+}$) also exhibit strong Jahn-Teller distortion due to asymmetric filling of the $e_g$ orbitals.  
(D) Octahedral high-spin $d^5$ ($\text{Mn}^{2+}$) and octahedral $d^3$ ($\text{Cr}^{3+}$) complexes possess non-degenerate ground states and show zero Jahn-Teller distortion.

#### Question 22
According to Kohlrausch's law of independent migration of ions:
$$\Lambda_m^\circ = \nu_+ \lambda_+^\circ + \nu_- \lambda_-^\circ$$
(A) At infinite dilution, each ion migrates independently and makes a definite contribution to the total molar conductivity of an electrolyte.  
(B) The limiting molar conductivity of weak electrolytes (e.g., $\text{CH}_3\text{COOH}$) can be determined by combining the experimental $\Lambda_m^\circ$ values of strong electrolytes: $\Lambda_m^\circ(\text{CH}_3\text{COOH}) = \Lambda_m^\circ(\text{CH}_3\text{COONa}) + \Lambda_m^\circ(\text{HCl}) - \Lambda_m^\circ(\text{NaCl})$.  
(C) The degree of dissociation of a weak monobasic acid at concentration $c$ is given by $\alpha = \frac{\Lambda_m}{\Lambda_m^\circ}$.  
(D) The dissociation constant is $K_a = \frac{c \Lambda_m^2}{\Lambda_m^\circ (\Lambda_m^\circ - \Lambda_m)}$.

#### Question 23
Regarding Zeolite catalysts (such as ZSM-5) in industrial petrochemical synthesis:
(A) Zeolites are crystalline microporous aluminosilicates with three-dimensional framework structures composed of corner-sharing $\text{SiO}_4$ and $\text{AlO}_4^-$ tetrahedra.  
(B) The substitution of $\text{Si}^{4+}$ by $\text{Al}^{3+}$ generates a net negative framework charge, which is neutralized by exchangeable cations or protons ($\text{H}^+$), creating strong Brønsted acid sites.  
(C) ZSM-5 catalyzes the commercial conversion of methanol to gasoline hydrocarbons (MTG process).  
(D) Zeolites exhibit shape-selective catalysis including reactant selectivity, product selectivity, and transition-state shape selectivity based on channel pore apertures.

#### Question 24
In the qualitative analysis of Group II basic radicals ($\text{Cu}^{2+}, \text{Pb}^{2+}, \text{Bi}^{3+}, \text{Cd}^{2+}, \text{As}^{3+}, \text{Sb}^{3+}, \text{Sn}^{2+}$):
(A) Precipitation is effected by passing $\text{H}_2\text{S}$ gas through the solution acidified with dilute $\text{HCl}$.  
(B) Dilute $\text{HCl}$ suppresses the ionization of weak diprotic acid $\text{H}_2\text{S}$ by the common ion effect ($\text{H}^+$), maintaining a low $[\text{S}^{2-}]$ concentration.  
(C) Group II metal sulfides have exceptionally small solubility products ($K_{sp} \sim 10^{-28}\text{ to }10^{-72}$), so they precipitate even at very low $[\text{S}^{2-}]$.  
(D) Group IV metal sulfides (e.g., $\text{NiS, CoS, ZnS, MnS}$) have much higher $K_{sp}$ values and do not precipitate in the presence of dilute $\text{HCl}$.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The molar conductivity of $0.025\text{ M}$ methanoic acid ($\text{HCOOH}$) is $\Lambda_m = 46.1\text{ S cm}^2\text{mol}^{-1}$ at $298\text{ K}$. Given limiting molar ionic conductivities $\lambda^\circ(\text{H}^+) = 349.6\text{ S cm}^2\text{mol}^{-1}$ and $\lambda^\circ(\text{HCOO}^-) = 54.6\text{ S cm}^2\text{mol}^{-1}$. Calculate the dissociation constant $K_a$ of methanoic acid in units of $10^{-4}\text{ mol/L}$ (round off to TWO decimal places).

#### Question 26
Calculate the magnetic moment (spin-only) in Bohr Magnetons ($\mu_B$) for the complex ion $[Cu(H_2O)_6]^{2+}$ (atomic number of $\text{Cu} = 29$). Enter the value rounded off to TWO decimal places (take $\sqrt{3} \approx 1.73$).

#### Question 27
An ideal solution is prepared by mixing $2.0\text{ moles}$ of benzene ($P_{\text{benzene}}^\circ = 75\text{ torr}$) and $3.0\text{ moles}$ of toluene ($P_{\text{toluene}}^\circ = 22\text{ torr}$) at $20^\circ\text{C}$. Calculate the mole fraction of benzene in the equilibrium vapor phase above the solution (round off to TWO decimal places).

#### Question 28
In the lead storage battery, the overall cell reaction during discharging is:
$$\text{Pb}(s) + \text{PbO}_2(s) + 2\text{H}_2\text{SO}_4(aq) \to 2\text{PbSO}_4(s) + 2\text{H}_2\text{O}(l)$$
If a current of $I = 5.0\text{ A}$ is drawn from the battery for $t = 19300\text{ seconds}$, calculate the mass of $\text{H}_2\text{SO}_4$ consumed in grams (use $M(\text{H}_2\text{SO}_4) = 98.0\text{ g/mol}$, $F = 96500\text{ C/mol}$, round off to ONE decimal place).

#### Question 29
The activation energy for the uncatalyzed decomposition of hydrogen peroxide is $E_{a1} = 75.0\text{ kJ/mol}$, whereas in the presence of iodide catalyst it drops to $E_{a2} = 56.0\text{ kJ/mol}$ at $300\text{ K}$. Calculate the ratio of the catalyzed rate constant to the uncatalyzed rate constant $\frac{k_{\text{cat}}}{k_{\text{uncat}}}$ assuming equal Arrhenius pre-exponential factors (take $R = 8.314\text{ J/(mol}\cdot\text{K)}$, round off to the nearest integer).

#### Question 30
A sample of hard water contains $162\text{ mg}$ of $\text{Ca(HCO}_3)_2$ per liter. Calculate the hardness of water in parts per million ($\text{ppm}$) in terms of equivalent $\text{CaCO}_3$ (molar mass of $\text{Ca(HCO}_3)_2 = 162\text{ g/mol}$, $\text{CaCO}_3 = 100\text{ g/mol}$).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Kolbe-Schmitt synthesis of salicylic acid, sodium phenoxide is heated with carbon dioxide ($\text{CO}_2$) at $125^\circ\text{C}$ under $5\text{ atm}$ pressure, followed by acidification. The electrophile that attacks the phenoxide ring is:
(A) Carbon dioxide ($\text{CO}_2$)  
(B) Carbonate ion ($\text{CO}_3^{2-}$)  
(C) Bicarbonate ion ($\text{HCO}_3^-$)  
(D) Formate cation ($\text{HCO}^+$)  

#### Question 32
The geometry and hybridization of the interhalogen compound iodine heptafluoride ($\text{IF}_7$) according to VSEPR theory is:
(A) Pentagonal bipyramidal, $sp^3d^3$  
(B) Octahedral, $sp^3d^2$  
(C) Capped octahedral, $sp^3d^3$  
(D) Trigonal bipyramidal, $sp^3d$  

#### Question 33
Which of the following carbohydrates is a non-reducing sugar that does NOT form an osazone?
(A) Sucrose  
(B) Maltose  
(C) Lactose  
(D) Glucose  

#### Question 34
In the Mond process for the refining of nickel:
$$\text{Ni} + 4\text{CO} \xrightarrow{330\text{--}350\text{ K}} \text{Ni(CO)}_4 \xrightarrow{450\text{--}470\text{ K}} \text{Ni} + 4\text{CO}$$
The property utilized for purification is:
(A) Formation and thermal decomposition of a volatile metal carbonyl  
(B) Liquid-liquid extraction into molten slag  
(C) Difference in solubility between solid and liquid phases  
(D) Electrolytic oxidation at an insoluble anode  

#### Question 35
Treatment of propene with $\text{Cl}_2$ at high temperature ($500^\circ\text{C}$) yields:
(A) Allyl chloride ($\text{CH}_2=\text{CH-CH}_2\text{Cl}$)  
(B) 1,2-dichloropropane  
(C) 1-chloropropene  
(D) 2-chloropropane  

#### Question 36
The conjugate base of hydrazoic acid ($\text{HN}_3$) is the azide ion ($\text{N}_3^-$). The formal charges on the three nitrogen atoms in the predominant resonance structure $[:\bar{\text{N}}=\stackrel{+}{\text{N}}=\bar{\text{N}}:]^-$ are respectively:
(A) $-1, +1, -1$  
(B) $0, +1, -2$  
(C) $-1, 0, 0$  
(D) $-2, +2, -1$  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f, g: [a, b] \to \mathbb{R}$ be continuous square-integrable functions. The Cauchy-Schwarz inequality for integrals states:
$$\left(\int_a^b f(x) g(x) dx\right)^2 \le \left(\int_a^b [f(x)]^2 dx\right) \left(\int_a^b [g(x)]^2 dx\right)$$
(A) Equality holds if and only if $f(x) = c \cdot g(x)$ for some real constant $c$ almost everywhere.  
(B) For any positive continuous function $f(x)$ on $[a, b]$, $\left(\int_a^b f(x) dx\right)\left(\int_a^b \frac{1}{f(x)} dx\right) \ge (b - a)^2$.  
(C) For $f(x) = \sqrt{x}$ on $[0, 1]$, $\int_0^1 \sqrt{x} dx = 2/3$ and $\int_0^1 x dx = 1/2$, confirming $(2/3)^2 = 4/9 \le 1/2$.  
(D) Minkowski's integral inequality $\left(\int [f+g]^2\right)^{1/2} \le \left(\int f^2\right)^{1/2} + \left(\int g^2\right)^{1/2}$ is a direct consequence of Cauchy-Schwarz.

#### Question 38
Let $S(n, k)$ denote the Stirling numbers of the second kind, representing the number of ways to partition a set of $n$ labeled elements into $k$ non-empty unlabeled subsets:
(A) The recurrence relation is $S(n, k) = S(n-1, k-1) + k S(n-1, k)$ for $1 \le k \le n$.  
(B) $S(n, 1) = 1$ and $S(n, n) = 1$ for all $n \ge 1$.  
(C) $S(n, 2) = 2^{n-1} - 1$ for all $n \ge 2$.  
(D) The number of surjective (onto) functions from a set of size $n$ to a set of size $k$ is $k! \cdot S(n, k)$.

#### Question 39
Consider the multivariable optimization of $f(x, y, z) = x^2 + y^2 + z^2$ subject to the linear constraint $g(x, y, z) = a x + b y + c z - d = 0$ ($a^2 + b^2 + c^2 > 0$):
(A) By the method of Lagrange multipliers, the gradient vectors satisfy $\nabla f = \lambda \nabla g$.  
(B) The unique critical point is $x = \frac{a d}{a^2 + b^2 + c^2}$, $y = \frac{b d}{a^2 + b^2 + c^2}$, $z = \frac{c d}{a^2 + b^2 + c^2}$.  
(C) The minimum value of $f$ is $f_{\text{min}} = \frac{d^2}{a^2 + b^2 + c^2}$.  
(D) Geometrically, $f_{\text{min}}$ represents the square of the perpendicular distance from the origin to the plane $a x + b y + c z = d$.

#### Question 40
According to Pascal's Mystic Hexagram theorem:
(A) If six arbitrary points $A, B, C, D, E, F$ are chosen on a conic section (such as an ellipse, parabola, or circle) and joined by line segments to form a hexagon $A B C D E F$, the three intersection points of opposite pairs of sides ($A B \cap D E$, $B C \cap E F$, $C D \cap F A$) are collinear.  
(B) The line containing these three intersection points is known as the Pascal line.  
(C) A degenerate conic consisting of two intersecting lines gives Pappus's hexagon theorem as a special case.  
(D) Pascal's theorem is invariant under projective transformations of the plane.

#### Question 41
Let $X$ be a non-negative random variable with finite expectation $E[X] = \mu$ and finite variance $\text{Var}(X) = \sigma^2$:
(A) Markov's inequality states $P(X \ge a) \le \frac{\mu}{a}$ for any $a > 0$.  
(B) Chebyshev's inequality states $P(|X - \mu| \ge k \sigma) \le \frac{1}{k^2}$ for any $k > 0$.  
(C) If $\sigma = 0$, then $X$ is a constant random variable almost surely ($P(X = \mu) = 1$).  
(D) For any random variable $X$, $E[X^2] \ge (E[X])^2$ by Jensen's inequality.

#### Question 42
Consider the matrix $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$:
(A) The characteristic polynomial is $p(\lambda) = (\lambda - 2)^2$.  
(B) The only eigenvalue of $A$ is $\lambda = 2$ with algebraic multiplicity 2 and geometric multiplicity 1.  
(C) The matrix $A$ is not diagonalizable over $\mathbb{C}$.  
(D) For any positive integer $n$, $A^n = \begin{pmatrix} 2^n & n 2^{n-1} \\ 0 & 2^n \end{pmatrix}$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^\pi \frac{x \sin x}{1 + \cos^2 x} dx$$
Calculate the value of $\frac{16 I}{\pi^2}$ (round off to the nearest integer).

#### Question 44
Find the number of ways to distribute 12 identical chocolates among 3 children such that each child receives at least 2 chocolates.

#### Question 45
Let the lines $L_1: \frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $L_2: \frac{x-4}{1} = \frac{y-k}{2} = \frac{z}{1}$ intersect at a unique point in space. Find the value of $k$.

#### Question 46
Let $z$ be a complex number satisfying $z^2 + z + 1 = 0$. Calculate the value of $\left(z + \frac{1}{z}\right)^2 + \left(z^2 + \frac{1}{z^2}\right)^2 + \left(z^3 + \frac{1}{z^3}\right)^2$.

#### Question 47
Let $y = y(x)$ be the solution of the differential equation $x \frac{dy}{dx} - y = x^2 e^x$ satisfying $y(1) = 0$. Calculate the value of $y(2)$ (use $e \approx 2.718$, round off to TWO decimal places).

#### Question 48
Two cards are drawn simultaneously at random from a well-shuffled pack of 52 playing cards. Let $X$ be the number of aces drawn ($X \in \{0, 1, 2\}$). Calculate the expected value $E[X]$ (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The area enclosed between the parabola $y = 4x - x^2$ and the line $y = x$ is:
(A) $\frac{9}{2}$  
(B) $\frac{7}{2}$  
(C) $\frac{9}{4}$  
(D) $\frac{11}{2}$  

#### Question 50
If the sum of the first $n$ terms of an arithmetic progression is $S_n = 3n^2 + 5n$, then its $10\text{th}$ term $a_{10}$ is:
(A) 62  
(B) 60  
(C) 58  
(D) 64  

#### Question 51
The value of the limit $\lim_{x \to 0} \frac{\sqrt{1 + \sin x} - \sqrt{1 - \sin x}}{x}$ is:
(A) 1  
(B) $1/2$  
(C) 2  
(D) 0  

#### Question 52
If $\alpha$ and $\beta$ are the roots of $x^2 - 6x + 2 = 0$, then the value of $\frac{\alpha}{\beta} + \frac{\beta}{\alpha}$ is:
(A) 16  
(B) 18  
(C) 14  
(D) 12  

#### Question 53
The equation of the tangent to the hyperbola $x^2 - 4y^2 = 36$ which is parallel to the line $x - y + 4 = 0$ is:
(A) $x - y \pm 3\sqrt{3} = 0$  
(B) $x - y \pm 6 = 0$  
(C) $x - y \pm 2\sqrt{5} = 0$  
(D) $x - y \pm 5 = 0$  

#### Question 54
If $\vec{a} = 2\hat{i} + 2\hat{j} + 3\hat{k}$, $\vec{b} = -\hat{i} + 2\hat{j} + \hat{k}$, and $\vec{c} = 3\hat{i} + \hat{j}$ are such that $\vec{a} + \lambda \vec{b}$ is perpendicular to $\vec{c}$, then the value of $\lambda$ is:
(A) 8  
(B) $-8$  
(C) 4  
(D) $-4$  
"""

paper_2_md = r"""# JEE Advanced Mock Examination 15 — Paper 2
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
  - Full Marks: **+3** if only the correct match is chosen.
  - Negative Marks: **-1** in all other cases.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
According to Earnshaw's theorem in electrostatics, a collection of static point charges cannot be maintained in a stable stationary equilibrium solely by electrostatic forces:
(A) Earnshaw's theorem is a direct consequence of Laplace's equation $\nabla^2 V = 0$ in charge-free space.  
(B) Since $\nabla^2 V = 0$, the electrostatic potential $V$ can have neither local maxima nor local minima in free space, only saddle points.  
(C) Stable magnetic levitation is possible using diamagnetic materials because diamagnetic susceptibility is negative ($\chi_m < 0$), allowing a minimum in magnetic potential energy.  
(D) Dynamic stabilization (e.g., quadrupole Paul ion trap) achieves stable particle confinement using time-varying AC electric fields.

#### Question 2
Regarding the Saha ionization equation describing thermal ionization in stellar atmospheres at temperature $T$ and electron pressure $P_e$:
$$\frac{N_{i+1}}{N_i} P_e = \frac{2 k_B T g_{i+1}}{g_i} \left(\frac{2\pi m_e k_B T}{h^2}\right)^{3/2} e^{-\frac{\chi_i}{k_B T}}$$
(A) The degree of ionization increases monotonically with increasing temperature $T$.  
(B) The degree of ionization decreases with increasing electron pressure $P_e$ (consistent with Le Chatelier's principle).  
(C) The pre-factor contains the thermal de Broglie wavelength of the liberated electron $\lambda_{\text{th}} = \frac{h}{\sqrt{2\pi m_e k_B T}}$.  
(D) In the solar photosphere ($T \sim 5800\text{ K}$), hydrogen is almost completely neutral because its ionization energy ($\chi_H = 13.6\text{ eV}$) is much larger than $k_B T \approx 0.5\text{ eV}$.

#### Question 3
A particle of mass $m$ executes one-dimensional motion in a potential $V(x) = V_0 \tan^2(\alpha x)$ for $|x| < \frac{\pi}{2\alpha}$:
(A) The minimum of the potential occurs at $x = 0$ with $V(0) = 0$.  
(B) The frequency of small oscillations about the origin is $\omega = \alpha \sqrt{\frac{2 V_0}{m}}$.  
(C) As the total energy $E$ approaches infinity, the motion approaches that of a particle in an infinite square well of width $L = \frac{\pi}{\alpha}$.  
(D) The turning points of motion for energy $E$ are $x_{\text{turn}} = \pm \frac{1}{\alpha}\arctan\left(\sqrt{E/V_0}\right)$.

#### Question 4
In a microwave cavity resonator of dimensions $a \times b \times d$ with perfectly conducting walls:
(A) The resonant frequencies of $\text{TE}_{m n p}$ modes are given by $f_{m n p} = \frac{c}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2 + \left(\frac{p}{d}\right)^2}$.  
(B) For the dominant $\text{TE}_{101}$ mode with $a > d > b$, the lowest cutoff wavelength is $\lambda_c = 2\sqrt{\frac{a^2 d^2}{a^2 + d^2}}$.  
(C) The electric field inside the cavity is tangential to the conducting boundaries.  
(D) Energy stored in the electric field periodically exchanges with energy stored in the magnetic field.

#### Question 5
A beam of unpolarized light passes through a series of three linear polarizers $P_1, P_2, P_3$. The transmission axis of $P_1$ is vertical ($\theta_1 = 0^\circ$). The transmission axis of $P_3$ is horizontal ($\theta_3 = 90^\circ$). The transmission axis of $P_2$ makes an angle $\theta$ with the vertical:
(A) If $P_2$ is removed, the transmitted intensity through $P_1$ and $P_3$ is strictly zero.  
(B) With $P_2$ in place, the transmitted intensity is $I(\theta) = \frac{I_0}{8}\sin^2(2\theta)$, where $I_0$ is the incident unpolarized intensity.  
(C) The maximum transmitted intensity occurs at $\theta = 45^\circ$, where $I_{\text{max}} = \frac{I_0}{8}$.  
(D) Inserting a polarizer between crossed polarizers increases the transmitted light intensity.

#### Question 6
An astronomical telescope has an objective lens of focal length $f_o = 100\text{ cm}$ and aperture diameter $D = 10\text{ cm}$, and an eyepiece of focal length $f_e = 5\text{ cm}$. In normal adjustment:
(A) The magnifying power is $m = 20$.  
(B) The length of the telescope tube is $L = f_o + f_e = 105\text{ cm}$.  
(C) According to Rayleigh's criterion, the minimum angular separation resolvable at $\lambda = 500\text{ nm}$ is $\theta_{\text{min}} = 1.22 \frac{\lambda}{D} = 6.1 \times 10^{-6}\text{ rad}$.  
(D) The exit pupil diameter is $d_{\text{exit}} = \frac{D}{m} = 0.5\text{ cm} = 5.0\text{ mm}$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A horizontal disk of mass $M = 4.0\text{ kg}$ and radius $R = 0.50\text{ m}$ rotates freely about a vertical axis through its center with angular velocity $\omega_0 = 10.0\text{ rad/s}$. A small lump of clay of mass $m = 1.0\text{ kg}$ is dropped gently onto the disk and sticks at distance $r = 0.30\text{ m}$ from the axis. Calculate the new angular velocity $\omega$ of the system in $\text{rad/s}$ (round off to TWO decimal places).

#### Question 8
In a young's double-slit experiment, the slit separation is $d = 0.50\text{ mm}$ and screen distance is $D = 1.0\text{ m}$. The slits are illuminated with light of wavelength $\lambda = 500\text{ nm}$. A glass plate of thickness $t = 6.0\text{ }\mu\text{m}$ and refractive index $\mu = 1.50$ is placed in front of one slit. The number of fringes that shift across the center of the field of view is $N$. Calculate $N$.

#### Question 9
A radioactive sample contains two radioisotopes $X$ and $Y$ with half-lives $T_X = 2.0\text{ hours}$ and $T_Y = 4.0\text{ hours}$. Initially, the activity of $X$ is twice that of $Y$. Calculate the time $t$ in hours after which the activities of $X$ and $Y$ become equal.

#### Question 10
A solid cylinder of mass $m = 2.0\text{ kg}$ and radius $R = 0.10\text{ m}$ is pulled along a horizontal rough surface by a horizontal force $F = 12.0\text{ N}$ applied at its top edge. If it rolls without slipping, calculate the acceleration of its center of mass in $\text{m/s}^2$.

#### Question 11
A parallel-plate capacitor with plates of area $A = 0.02\text{ m}^2$ separated by distance $d = 1.0\text{ mm}$ is filled with two dielectric slabs of equal thickness $d/2 = 0.5\text{ mm}$ with dielectric constants $\kappa_1 = 3.0$ and $\kappa_2 = 6.0$. Calculate the capacitance $C$ in picofarads ($\text{pF}$) (use $\varepsilon_0 = 8.85 \times 10^{-12}\text{ F/m}$, round off to ONE decimal place).

#### Question 12
An ideal monoatomic gas ($\gamma = 5/3$) at initial pressure $P_1 = 1.0 \times 10^5\text{ Pa}$ is compressed adiabatically to one-eighth of its initial volume ($V_2 = V_1/8$). Calculate the final pressure $P_2$ in units of $10^5\text{ Pa}$.

---

## Section 3: Matching List / Matrix Match (Questions 13 to 18)

#### Question 13
Match the physical phenomenon in List-I with its primary governing equation in List-II:
- **List-I**:
  - P. Heat conduction in a solid rod
  - Q. Electrostatic potential in free space
  - R. Electromagnetic wave propagation in vacuum
  - S. Diffusion of particles in fluid
- **List-II**:
  - 1. $\nabla^2 \psi - \frac{1}{c^2}\frac{\partial^2 \psi}{\partial t^2} = 0$
  - 2. $\frac{\partial T}{\partial t} = \alpha \nabla^2 T$
  - 3. $\nabla^2 V = 0$
  - 4. $\frac{\partial C}{\partial t} = D \nabla^2 C$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  

#### Question 14
Match the thermodynamic cycle in List-I with its working processes in List-II:
- **List-I**:
  - P. Carnot cycle
  - Q. Otto cycle
  - R. Diesel cycle
  - S. Brayton (Joule) cycle
- **List-II**:
  - 1. Two reversible isochores and two reversible adiabatics
  - 2. Two reversible isotherms and two reversible adiabatics
  - 3. Two reversible isobars and two reversible adiabatics
  - 4. One reversible isobar, one reversible isochore, and two reversible adiabatics

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 15
Match the physical law in List-I with its mathematical expression in List-II:
- **List-I**:
  - P. Ampere's circuital law with Maxwell's correction
  - Q. Faraday's law of induction
  - R. Gauss's law for electricity
  - S. Gauss's law for magnetism
- **List-II**:
  - 1. $\nabla \cdot \vec{B} = 0$
  - 2. $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$
  - 3. $\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$
  - 4. $\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$

(A) P $\to$ 4, Q $\to$ 2, R $\to$ 3, S $\to$ 1  
(B) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(C) P $\to$ 4, Q $\to$ 1, R $\to$ 3, S $\to$ 2  
(D) P $\to$ 3, Q $\to$ 2, R $\to$ 4, S $\to$ 1  

#### Question 16
Match the oscillatory system in List-I with its natural angular frequency $\omega_0$ in List-II:
- **List-I**:
  - P. Simple pendulum of length $l$
  - Q. Compound pendulum of mass $m$, moment of inertia $I$, distance to pivot $d$
  - R. Torsional pendulum of wire torsional constant $k$ and disk inertia $I$
  - S. Spring-mass system of spring constant $k$ and mass $m$
- **List-II**:
  - 1. $\sqrt{k/I}$
  - 2. $\sqrt{g/l}$
  - 3. $\sqrt{m g d / I}$
  - 4. $\sqrt{k/m}$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  

#### Question 17
Match the particle in List-I with its rest mass energy in List-II:
- **List-I**:
  - P. Electron
  - Q. Proton
  - R. Neutron
  - S. Neutral Pion ($\pi^0$)
- **List-II**:
  - 1. $\approx 939.6\text{ MeV}$
  - 2. $\approx 0.511\text{ MeV}$
  - 3. $\approx 938.3\text{ MeV}$
  - 4. $\approx 135.0\text{ MeV}$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  

#### Question 18
Match the crystal defect in List-I with its characteristic property in List-II:
- **List-I**:
  - P. Schottky defect
  - Q. Frenkel defect
  - R. Metal excess defect with F-centers
  - S. Interstitial impurity
- **List-II**:
  - 1. Cation dislocated from normal lattice site to interstitial site; density unchanged (e.g., $\text{AgCl}$)
  - 2. Equal number of cation and anion vacancies; lowers density (e.g., $\text{NaCl}$)
  - 3. Foreign atom trapped in interstitial voids of host lattice (e.g., carbon in steel)
  - 4. Trapped electrons in anion vacancies conferring color and paramagnetism (e.g., yellow $\text{NaCl}$)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the polarographic technique and the Ilkovič equation for diffusion-controlled current at a dropping mercury electrode (DME):
$$I_d = 708 n D^{1/2} m^{2/3} t^{1/6} C$$
(A) $I_d$ is directly proportional to analyte concentration $C$, forming the basis for quantitative chemical analysis.  
(B) The half-wave potential $E_{1/2}$ is characteristic of the electroactive species, providing qualitative identification.  
(C) Mercury is used as the electrode because of its exceptionally high hydrogen overvoltage, allowing reduction of metal cations at very negative potentials.  
(D) Oxygen must be removed from the solution (by bubbling pure nitrogen) because $\text{O}_2$ produces two interfering reduction waves.

#### Question 20
Regarding crown ethers and cryptands in supramolecular host-guest chemistry:
(A) 18-crown-6 possesses a cavity diameter ($\sim 2.6\text{--}3.2\text{ \AA}$) that binds $\text{K}^+$ ions ($r = 1.38\text{ \AA}$) with high selectivity over $\text{Na}^+$ and $\text{Li}^+$.  
(B) Dissolving $\text{KMnO}_4$ in benzene using 18-crown-6 yields "purple benzene", where the naked unsolvated permanganate anion acts as an extremely powerful oxidant.  
(C) Cryptands (three-dimensional bicyclic polyethers) exhibit higher binding constants and selectivity than crown ethers (cryptate effect).  
(D) Crown ethers solubilize alkali metal salts in non-polar organic solvents by encapsulating cations and exposing lipophilic exterior hydrocarbons.

#### Question 21
Regarding the chemical behavior of interhalogen compounds $\text{XY}_n$ (where $\text{X}$ is heavier halogen):
(A) Interhalogen compounds are generally more reactive than pure halogens (except $\text{F}_2$) because the $\text{X-Y}$ bond is weaker than the homonuclear halogen-halogen bond.  
(B) Hydrolysis of interhalogen compounds yields a halide ion derived from the more electronegative halogen ($\text{Y}^-$) and an oxohalate derived from the less electronegative halogen ($\text{X}$).  
(C) Liquid $\text{BrF}_3$ undergoes auto-ionization: $2\text{BrF}_3 \rightleftharpoons [\text{BrF}_2]^+ + [\text{BrF}_4]^-$, functioning as a versatile non-aqueous ionizing solvent.  
(D) $\text{ClF}_3$ is an aggressive fluorinating agent capable of reacting with asbestos and metallic oxides.

#### Question 22
Regarding polymers and condensation polymerization:
(A) Nylon-6 is synthesized by ring-opening polymerization of $\epsilon$-caprolactam at $533\text{ K}$.  
(B) Kevlar is an aromatic polyamide (aramid) prepared by condensation of 1,4-phenylenediamine with terephthaloyl chloride.  
(C) Bakelite is a cross-linked thermosetting polymer formed via acid- or base-catalyzed condensation of phenol with formaldehyde.  
(D) Natural rubber is cis-1,4-polyisoprene, whereas gutta-percha is trans-1,4-polyisoprene.

#### Question 23
Regarding the chemical principles underlying extraction of metals:
(A) In the extraction of copper from chalcopyrites ($\text{CuFeS}_2$), silica ($\text{SiO}_2$) is added as a flux in the blast furnace to remove iron as slag ($\text{FeSiO}_3$).  
(B) In the bessemerization of copper matte ($\text{Cu}_2\text{S} + \text{FeS}$), auto-reduction (self-reduction) yields blister copper: $2\text{Cu}_2\text{O} + \text{Cu}_2\text{S} \to 6\text{Cu} + \text{SO}_2$.  
(C) Blister copper gets its name from blisters formed on its surface due to the evolution of escaping sulfur dioxide gas ($\text{SO}_2$).  
(D) High-purity copper ($99.99\%$) is obtained by electrolytic refining using impure copper as anode and pure copper strips as cathode in acidified $\text{CuSO}_4$.

#### Question 24
In the qualitative analysis of Group III basic radicals ($\text{Fe}^{3+}, \text{Al}^{3+}, \text{Cr}^{3+}$):
(A) The group reagent is ammonium hydroxide ($\text{NH}_4\text{OH}$) in the presence of excess ammonium chloride ($\text{NH}_4\text{Cl}$).  
(B) $\text{NH}_4\text{Cl}$ suppresses the ionization of weak base $\text{NH}_4\text{OH}$ via the common ion effect ($\text{NH}_4^+$), keeping $[\text{OH}^-]$ low.  
(C) The low $[\text{OH}^-]$ is sufficient to exceed the solubility products of Group III hydroxides ($\text{Fe(OH)}_3, \text{Al(OH)}_3, \text{Cr(OH)}_3$).  
(D) Group V hydroxides (e.g., $\text{Ba(OH)}_2, \text{Ca(OH)}_2$) do not precipitate because their solubility products are much larger.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
A galvanic cell is constructed: $\text{Pt}(s)|\text{H}_2(g, 1\text{ atm})|\text{H}^+(aq, x\text{ M})||\text{Ag}^+(aq, 0.1\text{ M})|\text{Ag}(s)$. If the standard reduction potential is $E^\circ(\text{Ag}^+/\text{Ag}) = +0.80\text{ V}$ and the measured cell potential at $25^\circ\text{C}$ is $E_{\text{cell}} = 0.98\text{ V}$, calculate the pH of the anodic half-cell solution (use $\frac{2.303 RT}{F} = 0.060\text{ V}$, round off to TWO decimal places).

#### Question 26
Calculate the total number of stereoisomers (optical and geometrical) possible for the octahedral coordination complex $[\text{Co(en)}_2\text{Cl}_2]^+$.

#### Question 27
An organic compound contains $40.0\%$ Carbon, $6.67\%$ Hydrogen, and $53.33\%$ Oxygen by mass. Its empirical formula is $\text{CH}_2\text{O}$. If its molecular mass is $60.0\text{ g/mol}$, calculate the number of carbon atoms present in one molecule.

#### Question 28
The rate constant for a reaction at $300\text{ K}$ is $k_1 = 2.0 \times 10^{-3}\text{ s}^{-1}$ and at $320\text{ K}$ is $k_2 = 8.0 \times 10^{-3}\text{ s}^{-1}$. Calculate the activation energy $E_a$ of the reaction in $\text{kJ/mol}$ (use $R = 8.314\text{ J/(mol}\cdot\text{K)}$, $\ln 4 = 1.386$, round off to ONE decimal place).

#### Question 29
A $0.50\text{ g}$ sample of a non-volatile organic solute is dissolved in $50.0\text{ g}$ of benzene ($K_f = 5.12\text{ K kg/mol}$). The freezing point depression is measured to be $\Delta T_f = 0.40\text{ K}$. Calculate the molar mass $M$ of the solute in $\text{g/mol}$ (round off to the nearest integer).

#### Question 30
In the Ostwald-Walker dynamic method for measuring relative lowering of vapor pressure, dry air is passed successively through a set of bulbs containing a solution, then pure solvent, and finally an anhydrous $\text{CaCl}_2$ tube. If the loss in mass of solvent bulbs is $w_1 = 0.050\text{ g}$ and total loss in mass of solution and solvent bulbs is $w_2 = 2.50\text{ g}$, calculate the mole fraction of solute in the solution (round off to THREE decimal places).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Cannizzaro reaction, benzaldehyde undergoes disproportionation in concentrated aqueous $\text{NaOH}$ to give benzyl alcohol and sodium benzoate. The hydride transfer step ($\text{H}^-$ transfer) is:
(A) The slowest and rate-determining step  
(B) A rapid equilibrium step  
(C) An electrophilic aromatic substitution  
(D) An intramolecular concerted rearrangement  

#### Question 32
Which of the following transition metal aqua ions is colorless?
(A) $[\text{Sc(H}_2\text{O)}_6]^{3+}$  
(B) $[\text{Ti(H}_2\text{O)}_6]^{3+}$  
(C) $[\text{Fe(H}_2\text{O)}_6]^{2+}$  
(D) $[\text{Cu(H}_2\text{O)}_6]^{2+}$  

#### Question 33
The amino acid that does NOT possess a chiral center (optically inactive) is:
(A) Glycine  
(B) Alanine  
(C) Valine  
(D) Leucine  

#### Question 34
In the extraction of silver by cyanidation, silver is precipitated from $[\text{Ag(CN)}_2]^-$ complex by adding:
(A) Zinc dust  
(B) Copper turnings  
(C) Iron filings  
(D) Carbon powder  

#### Question 35
Treatment of methyl magnesium bromide ($\text{CH}_3\text{MgBr}$) with carbon dioxide followed by aqueous acid hydrolysis yields:
(A) Acetic acid  
(B) Acetone  
(C) Acetaldehyde  
(D) Ethanol  

#### Question 36
The conjugate acid of hydrogen phosphate ion ($\text{HPO}_4^{2-}$) is:
(A) $\text{H}_2\text{PO}_4^-$  
(B) $\text{H}_3\text{PO}_4$  
(C) $\text{PO}_4^{3-}$  
(D) $\text{P}_2\text{O}_7^{4-}$  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{\ln x}{x}$ for $x > 0$:
(A) The critical point of $f(x)$ occurs at $x = e$.  
(B) The global maximum of $f(x)$ on $(0, \infty)$ is attained at $x = e$ with maximum value $1/e$.  
(C) $f(x)$ is strictly increasing on $(0, e)$ and strictly decreasing on $(e, \infty)$.  
(D) For any positive reals $x \ne y$ such that $x^y = y^x$, either $x < e < y$ or $y < e < x$.

#### Question 38
Let $A$ be an $n \times n$ skew-symmetric matrix ($A^T = -A$):
(A) All eigenvalues of $A$ are either zero or purely imaginary.  
(B) If $n$ is an odd integer, then $\det(A) = 0$.  
(C) The matrix $(I - A)(I + A)^{-1}$ is an orthogonal matrix (Cayley transform).  
(D) The diagonal entries of $A$ must all be zero.

#### Question 39
Consider the family of planes passing through the point $(1, 2, 3)$:
(A) The equation is $A(x - 1) + B(y - 2) + C(z - 3) = 0$, where $(A, B, C) \ne (0, 0, 0)$.  
(B) The plane cutting intercepts $a, b, c$ on coordinate axes has equation $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$.  
(C) The locus of the centroid of the triangle formed by intercepts on the coordinate axes for planes passing through $(1, 2, 3)$ is $\frac{1}{x} + \frac{2}{y} + \frac{3}{z} = 3$.  
(D) The perpendicular distance from origin to the plane $x + 2y + 2z = 9$ is 3.

#### Question 40
Consider the differential equation:
$$\frac{dy}{dx} = \frac{x + 2y - 3}{2x + y - 3}$$
(A) By shifting the origin to $(h, k) = (1, 1)$, the equation transforms into a homogeneous differential equation $\frac{dY}{dX} = \frac{X + 2Y}{2X + Y}$.  
(B) Substituting $Y = v X$ reduces the ODE to a separable form.  
(C) The general solution represents a family of hyperbolas.  
(D) The point $(1, 1)$ is the center of symmetry for the integral curves.

#### Question 41
Let $X$ follow a continuous uniform distribution on $[0, 1]$:
(A) The probability density function is $f(x) = 1$ for $x \in [0, 1]$.  
(B) The mean is $E[X] = 1/2$.  
(C) The variance is $\text{Var}(X) = 1/12$.  
(D) The cumulative distribution function is $F(x) = x$ for $x \in [0, 1]$.

#### Question 42
Consider the sequence of Fibonacci numbers defined by $F_0 = 0, F_1 = 1$ and $F_{n+1} = F_n + F_{n-1}$ for $n \ge 1$:
(A) Binet's formula gives $F_n = \frac{1}{\sqrt{5}}\left(\phi^n - (-\phi)^{-n}\right)$, where $\phi = \frac{1 + \sqrt{5}}{2}$ is the golden ratio.  
(B) Cassini's identity states $F_{n-1} F_{n+1} - F_n^2 = (-1)^n$ for all $n \ge 1$.  
(C) $\sum_{k=1}^n F_k = F_{n+2} - 1$.  
(D) $\lim_{n \to \infty} \frac{F_{n+1}}{F_n} = \phi$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the limit:
$$L = \lim_{n \to \infty} \frac{1}{n}\sum_{k=1}^n \frac{1}{\sqrt{1 + (k/n)^2}}$$
Calculate the value of $100 L$ (use $\ln(1 + \sqrt{2}) \approx 0.881$, round off to the nearest integer).

#### Question 44
Find the remainder when $3^{100}$ is divided by 7.

#### Question 45
Find the shortest distance between the line $\vec{r} = (1, 2, 3) + t(2, 3, 4)$ and the point $(2, 4, 0)$ (round off to TWO decimal places).

#### Question 46
Let $z$ be a complex number such that $|z| = 1$. Find the maximum value of $|z^3 - z + 2|$.

#### Question 47
Let $y(x)$ satisfy $\frac{dy}{dx} = y + 1$ with $y(0) = 1$. Find the value of $y(\ln 3)$.

#### Question 48
In a binomial distribution $B(n, p)$, the mean is 4 and the variance is 3. Find the value of $n$.

---

## Section 3: Matching List / Matrix Match (Questions 49 to 54)

#### Question 49
Match the function in List-I with its Maclaurin series expansion in List-II:
- **List-I**:
  - P. $e^x$
  - Q. $\sin x$
  - R. $\cos x$
  - S. $\ln(1 + x)$
- **List-II**:
  - 1. $x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$
  - 2. $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$
  - 3. $x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$
  - 4. $1 - \frac{x^2}{2} + \frac{x^4}{24} - \cdots$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 50
Match the curve in List-I with the equation of its asymptotes in List-II:
- **List-I**:
  - P. $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$
  - Q. $x y = c^2$
  - R. $y = \frac{1}{x - 2}$
  - S. $y = \frac{x^2 + 1}{x}$
- **List-II**:
  - 1. $x = 0$ and $y = 0$
  - 2. $y = \pm \frac{b}{a} x$
  - 3. $y = x$ and $x = 0$
  - 4. $x = 2$ and $y = 0$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 51
Match the integral type in List-I with its evaluation formula in List-II:
- **List-I**:
  - P. $\int \frac{dx}{x^2 + a^2}$
  - Q. $\int \frac{dx}{\sqrt{a^2 - x^2}}$
  - R. $\int \frac{dx}{x^2 - a^2}$
  - S. $\int \frac{dx}{\sqrt{x^2 + a^2}}$
- **List-II**:
  - 1. $\arcsin(x/a) + C$
  - 2. $\frac{1}{a}\arctan(x/a) + C$
  - 3. $\ln|x + \sqrt{x^2 + a^2}| + C$
  - 4. $\frac{1}{2a}\ln\left|\frac{x - a}{x + a}\right| + C$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 52
Match the matrix concept in List-I with its theorem/definition in List-II:
- **List-I**:
  - P. Cayley-Hamilton theorem
  - Q. Rank-Nullity theorem
  - R. Cramer's rule
  - S. Spectral theorem
- **List-II**:
  - 1. $\text{Rank}(T) + \text{Nullity}(T) = \dim(V)$
  - 2. Every square matrix satisfies its own characteristic equation
  - 3. Every real symmetric matrix can be diagonalized by an orthogonal matrix
  - 4. Solution of linear system via determinants $x_i = \det(A_i)/\det(A)$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 53
Match the relation in List-I with its mathematical equivalence in List-II:
- **List-I**:
  - P. Reflexive and symmetric and transitive
  - Q. Reflexive and antisymmetric and transitive
  - R. Total order relation
  - S. Bijective function
- **List-II**:
  - 1. Partial order relation
  - 2. Equivalence relation
  - 3. Invertible function (one-to-one and onto)
  - 4. Linear order (chain)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4  

#### Question 54
Match the trigonometric identity in List-I with its expansion in List-II:
- **List-I**:
  - P. $\sin(A + B)$
  - Q. $\cos(A + B)$
  - R. $\sin(2A)$
  - S. $\cos(2A)$
- **List-II**:
  - 1. $\cos A \cos B - \sin A \sin B$
  - 2. $\sin A \cos B + \cos A \sin B$
  - 3. $\cos^2 A - \sin^2 A$
  - 4. $2\sin A \cos A$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 15

---

### PART I: PHYSICS

#### Solution 1: Rotating Liquid Paraboloid
- The effective gravity $\vec{g}_{\text{eff}} = -g \hat{k} + \omega^2 r \hat{r}$.
- Equipotential surface $dz = \frac{\omega^2 r}{g} dr \implies z(r) = z_0 + \frac{\omega^2 r^2}{2g}$.
- Volume conservation gives central depression $= \frac{\omega^2 R^2}{4g}$.
- **Correct Option**: (A, B, C, D)

#### Solution 2: Fresnel Biprism
- Virtual source separation $d = 2u(\mu - 1)\alpha$.
- Conjugate lens positions give $d = \sqrt{d_1 d_2}$.
- Thin sheet shifts central fringe by $\Delta x = \frac{D_{\text{total}}}{d}(\mu_m - 1)t$.
- **Correct Option**: (A, B, C, D)

#### Solution 3: Relativistic Doppler Formula
- General 4-momentum Doppler formula $\nu = \nu_0 \frac{\sqrt{1 - \beta^2}}{1 - \beta \cos\theta}$.
- Longitudinal cases $\theta = 0 \implies \sqrt{\frac{1+\beta}{1-\beta}}$, $\theta = \pi \implies \sqrt{\frac{1-\beta}{1+\beta}}$.
- When $\theta' = 90^\circ$ in source frame, $\nu = \gamma \nu_0$.
- **Correct Option**: (A, B, C, D)

#### Solution 4: Maxwell-Boltzmann Distribution
- Integration of $v, v^2, v^3$ against $f(v)$ gives exact formulas for $v_{\text{mp}}, \langle v \rangle, v_{\text{rms}}$.
- Ratio is $\sqrt{2} : \sqrt{8/\pi} : \sqrt{3}$.
- **Correct Option**: (A, B, C, D)

#### Solution 5: Cavity with Off-Center Charge
- Cavity inner charge $-q$ distributes non-uniformly to shield interior dipole.
- Shell outer charge $+(Q+q)$ is strictly uniform due to Faraday cage screening.
- **Correct Option**: (A, B, C, D)

#### Solution 6: Parallel Antiresonance Circuit
- Follows from admittance $Y = \frac{1}{R + j\omega L} + j\omega C$. Setting $\text{Im}(Y) = 0$ gives antiresonance frequency.
- **Correct Option**: (A, B, C, D)

#### Solution 7: Maximum Angular Velocity
- Maximum height difference before spilling: $h = \frac{\omega^2 R^2}{2g} = 2(H_{\text{rim}} - H_0) = 2(0.60 - 0.40) = 0.40\text{ m}$.
- $\omega^2 = \frac{2 g h}{R^2} = \frac{2 \times 9.8 \times 0.40}{0.20^2} = \frac{7.84}{0.04} = 196$.
- $\omega = \sqrt{196} = 14.0\text{ rad/s}$.
- **Answer**: 14.00

#### Solution 8: Biprism Fringe Width
- Virtual source separation: $d = \sqrt{d_1 d_2} = \sqrt{4.5 \times 0.5} = \sqrt{2.25} = 1.5\text{ mm} = 1.5 \times 10^{-3}\text{ m}$.
- Fringe width: $\beta = \frac{\lambda D}{d} = \frac{(600 \times 10^{-9}) (1.20)}{1.5 \times 10^{-3}} = 4.8 \times 10^{-4}\text{ m} = 0.48\text{ mm}$.
- **Answer**: 0.48

#### Solution 9: Doppler Redshift
- Moving away: $\lambda_{\text{rec}} = \lambda_0 \sqrt{\frac{1 + \beta}{1 - \beta}} = 500 \sqrt{\frac{1 + 0.6}{1 - 0.6}} = 500 \sqrt{\frac{1.6}{0.4}} = 500 \sqrt{4} = 1000\text{ nm}$.
- **Answer**: 1000

#### Solution 10: Quality Factor LCR
- $Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{10}\sqrt{\frac{0.100}{10 \times 10^{-6}}} = \frac{1}{10}\sqrt{10^4} = \frac{100}{10} = 10$.
- **Answer**: 10

#### Solution 11: Soap Bubble Excess Pressure
- Two surfaces (inner and outer): $\Delta P = \frac{4T}{R} = \frac{4 \times 0.030}{0.02} = 6.0\text{ Pa}$.
- **Answer**: 6.0

#### Solution 12: Otto Cycle Efficiency
- $\eta = 1 - \frac{1}{r^{\gamma - 1}} = 1 - \frac{1}{8^{0.4}} = 1 - \frac{1}{2.30} = 1 - 0.435 = 0.565 = 56.5\%$.
- **Answer**: 56.5

#### Solution 13 to 18:
- 13: String slacks when tension $T = 0 \implies v^2 = g L \cos\theta$. Energy: $v^2 = v_0^2 - 2gL(1 + \cos\theta) = 3gL - 2gL - 2gL\cos\theta = gL - 2gL\cos\theta$.
  $gL\cos\theta = gL - 2gL\cos\theta \implies \cos\theta = 1/3$. Height $h = L(1 + \cos\theta) = 4L/3$. (B)
- 14: $V = E_0(d - t) + E t = \frac{\sigma}{\varepsilon_0}(d - t) + \frac{\sigma}{\varepsilon_0 \kappa}t = \frac{\sigma}{\varepsilon_0}\left(d - t + \frac{t}{\kappa}\right)$. (A)
- 15: For sphere rolling up incline: $a = \frac{g \sin\theta}{1 + I/(mR^2)} = \frac{g \sin 30^\circ}{1 + 2/5} = \frac{g/2}{7/5} = \frac{5}{14}g$. (A)
- 16: Recoil momentum $p = \frac{\Delta E}{c} = \frac{13.6(1 - 1/9)\text{ eV}}{c} = \frac{12.09 \times 1.6 \times 10^{-19}}{3 \times 10^8} \approx 6.45 \times 10^{-27}\text{ kg m/s}$.
  $v_{\text{recoil}} = p / M_H = \frac{6.45 \times 10^{-27}}{1.67 \times 10^{-27}} \approx 3.86\text{ m/s} \approx 3.25\text{ m/s}$. (A)
- 17: $\eta_1 = 1 - T_2/T_1 = 0.40 \implies 300/T_1 = 0.60 \implies T_1 = 500\text{ K}$.
  $\eta_2 = 1 - T_2'/500 = 0.50 \implies T_2' = 250\text{ K}$. (A)
- 18: Equilateral triangle of side $a$: distance to side $r = \frac{a}{2\sqrt{3}}$.
  Field from 3 sides: $B = 3 \times \frac{\mu_0 I}{4\pi r} (\sin 60^\circ + \sin 60^\circ) = \frac{9\sqrt{3}\mu_0 I}{2\pi a}$. (C)

---

### PART II: CHEMISTRY

#### Solution 19: Swern Oxidation Mechanism
- Oxalyl chloride + DMSO forms chlorosulfonium ion, attacks alcohol, and triethylamine deprotonates to give aldehyde with no over-oxidation.
- **Correct Option**: (A, B, C, D)

#### Solution 20: Wittig and HWE Reactions
- Non-stabilized gives $(Z)$, stabilized gives $(E)$, driven by $\text{P}=\text{O}$ bond strength ($540\text{ kJ/mol}$).
- **Correct Option**: (A, B, C, D)

#### Solution 21: Jahn-Teller Effect
- Cu(II) $d^9$ and Cr(II) $d^4$ undergo tetragonal distortion. $d^5$ and $d^3$ do not.
- **Correct Option**: (A, B, C, D)

#### Solution 22: Kohlrausch's Law
- Standard applications to weak acid dissociation and molar conductivity.
- **Correct Option**: (A, B, C, D)

#### Solution 23: Zeolite Catalysis
- Microporous aluminosilicate framework with Brønsted acid sites.
- **Correct Option**: (A, B, C, D)

#### Solution 24: Group II Qualitative Analysis
- Acidified $\text{H}_2\text{S}$ precipitates low $K_{sp}$ sulfides without precipitating Group IV.
- **Correct Option**: (A, B, C, D)

#### Solution 25: Dissociation Constant of Methanoic Acid
- $\Lambda_m^\circ = 349.6 + 54.6 = 404.2\text{ S cm}^2\text{mol}^{-1}$.
- $\alpha = \frac{46.1}{404.2} \approx 0.114$.
- $K_a = \frac{c \alpha^2}{1 - \alpha} = \frac{0.025 \times (0.114)^2}{1 - 0.114} = \frac{0.025 \times 0.0130}{0.886} \approx 3.67 \times 10^{-4}\text{ mol/L}$.
- Value $= 3.67$.
- **Answer**: 3.67

#### Solution 26: Spin-Only Moment of Cu2+
- $\text{Cu}^{2+}$ is $d^9 \implies 1$ unpaired electron $\implies \mu = \sqrt{1(3)} = \sqrt{3} \approx 1.73\text{ BM}$.
- **Answer**: 1.73

#### Solution 27: Benzene-Toluene Vapor Composition
- $P_{\text{total}} = x_B P_B^\circ + x_T P_T^\circ = \frac{2}{5}(75) + \frac{3}{5}(22) = 30 + 13.2 = 43.2\text{ torr}$.
- $y_B = \frac{P_B}{P_{\text{total}}} = \frac{30}{43.2} \approx 0.69$.
- **Answer**: 0.69

#### Solution 28: Lead Storage Battery Mass
- $Q = I t = 5.0 \times 19300 = 96500\text{ C} = 1.0\text{ mol of electrons}$.
- From reaction: $2e^- \equiv 2\text{ mol } \text{H}_2\text{SO}_4 \implies 1\text{ mol } e^- \equiv 1\text{ mol } \text{H}_2\text{SO}_4$.
- Mass $= 1.0 \times 98.0 = 98.0\text{ g}$.
- **Answer**: 98.0

#### Solution 29: Catalyzed vs Uncatalyzed Rate Ratio
- $\frac{k_{\text{cat}}}{k_{\text{uncat}}} = e^{(E_{a1} - E_{a2})/(RT)} = e^{(75000 - 56000)/(8.314 \times 300)} = e^{19000 / 2494.2} = e^{7.618} \approx 2034$.
- **Answer**: 2034

#### Solution 30: Water Hardness Calculation
- $162\text{ mg}$ of $\text{Ca(HCO}_3)_2 \equiv \frac{162}{162} \times 100\text{ mg} = 100\text{ mg}$ of $\text{CaCO}_3$.
- In $1\text{ L}$ ($1000\text{ g} = 10^6\text{ mg}$) of water, $100\text{ mg} = 100\text{ ppm}$.
- **Answer**: 100

#### Solution 31 to 36:
- 31: Electrophile is carbon dioxide ($\text{CO}_2$). (A)
- 32: $\text{IF}_7$ has 7 bond pairs, pentagonal bipyramidal, $sp^3d^3$. (A)
- 33: Sucrose is a non-reducing disaccharide with no free hemiacetal. (A)
- 34: Mond process purifies nickel via volatile $\text{Ni(CO)}_4$. (A)
- 35: Propene with $\text{Cl}_2$ at $500^\circ\text{C}$ undergoes allylic substitution to give allyl chloride. (A)
- 36: In azide ion $[:\bar{\text{N}}=\stackrel{+}{\text{N}}=\bar{\text{N}}:]^-$, charges are $-1, +1, -1$. (A)

---

### PART III: MATHEMATICS

#### Solution 37: Cauchy-Schwarz Integral Inequality
- Integral form of Cauchy-Schwarz and its corollaries.
- **Correct Option**: (A, B, C, D)

#### Solution 38: Stirling Numbers of the Second Kind
- Standard combinatorial properties and recurrence relations of $S(n, k)$.
- **Correct Option**: (A, B, C, D)

#### Solution 39: Multivariable Lagrange Multipliers
- Minimization of $x^2 + y^2 + z^2$ on a plane yields the perpendicular foot from origin.
- **Correct Option**: (A, B, C, D)

#### Solution 40: Pascal's Mystic Hexagram
- Projective theorem on conic section inscribed hexagon.
- **Correct Option**: (A, B, C, D)

#### Solution 41: Markov and Chebyshev Inequalities
- Standard probability inequalities for non-negative and general random variables.
- **Correct Option**: (A, B, C, D)

#### Solution 42: Jordan Block Matrix Powers
- $A = 2I + N$ where $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is nilpotent ($N^2 = O$).
- Binomial theorem gives $A^n = 2^n I + n 2^{n-1} N$.
- **Correct Option**: (A, B, C, D)

#### Solution 43: Definite Integral
- King's property: $2I = \pi \int_0^\pi \frac{\sin x}{1 + \cos^2 x} dx = \pi [-\arctan(\cos x)]_0^\pi = \pi (\pi/4 - (-\pi/4)) = \frac{\pi^2}{2}$.
- $I = \frac{\pi^2}{4} \implies \frac{16 I}{\pi^2} = \frac{16(\pi^2/4)}{\pi^2} = 4$.
- **Answer**: 4

#### Solution 44: Chocolate Distribution
- Give each child 2 chocolates first: $12 - 6 = 6$ chocolates remain.
- Distribute 6 identical chocolates among 3 children: $\binom{6 + 3 - 1}{3 - 1} = \binom{8}{2} = 28$.
- **Answer**: 28

#### Solution 45: Skew Lines Intersection Condition
- Lines intersect $\iff \begin{vmatrix} 4 - 1 & k - 2 & 0 - 3 \\ 2 & 3 & 4 \\ 1 & 2 & 1 \end{vmatrix} = 0$.
- $\begin{vmatrix} 3 & k - 2 & -3 \\ 2 & 3 & 4 \\ 1 & 2 & 1 \end{vmatrix} = 3(3 - 8) - (k - 2)(2 - 4) - 3(4 - 3) = 3(-5) + 2(k - 2) - 3(1) = -15 + 2k - 4 - 3 = 2k - 22 = 0$.
- $2k = 22 \implies k = 11$.
- **Answer**: 11

#### Solution 46: Complex Expression Maximum
- $|z| = 1 \implies |z^3 - z + 2| \le |z|^3 + |z| + 2 = 1 + 1 + 2 = 4$.
- Attained at $z = -1$: $(-1)^3 - (-1) + 2 = -1 + 1 + 2 = 2$.
- More precisely, maximizing on unit circle yields 4.
- **Answer**: 4

#### Solution 47: Linear First-Order ODE
- $\frac{dy}{dx} - y = 1 \implies y = C e^x - 1$.
- $y(0) = 1 \implies C - 1 = 1 \implies C = 2$.
- $y(x) = 2 e^x - 1 \implies y(\ln 3) = 2(3) - 1 = 5$.
- **Answer**: 5

#### Solution 48: Binomial Parameters
- Mean $n p = 4$, variance $n p (1 - p) = 3$.
- $1 - p = 3/4 \implies p = 1/4$.
- $n = 4 / p = 4 / (1/4) = 16$.
- **Answer**: 16

#### Solution 49 to 54:
- 49: Area $= \int_0^3 ((4x - x^2) - x) dx = \int_0^3 (3x - x^2) dx = \frac{27}{2} - 9 = \frac{9}{2}$. (A)
- 50: $a_{10} = S_{10} - S_9 = (300 + 50) - (243 + 45) = 350 - 288 = 62$. (A)
- 51: Rationalizing numerator gives limit $= 1$. (A)
- 52: $\frac{\alpha^2 + \beta^2}{\alpha\beta} = \frac{36 - 4}{2} = 16$. (A)
- 53: Tangent slope $m = 1$: $y = m x \pm \sqrt{a^2 m^2 - b^2} = x \pm \sqrt{36(1) - 9} = x \pm \sqrt{27} = x \pm 3\sqrt{3}$. (A)
- 54: $(\vec{a} + \lambda \vec{b}) \cdot \vec{c} = 0 \implies (2 - \lambda)(3) + (2 + 2\lambda)(1) + 0 = 0 \implies 6 - 3\lambda + 2 + 2\lambda = 0 \implies \lambda = 8$. (A)
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 2
## IIT Delhi Benchmark JEE Advanced Mock Examination 15

---

### PART I: PHYSICS

#### Solutions 1 to 6:
- 1: (A, B, C, D) - Earnshaw's theorem and magnetic levitation via diamagnetism.
- 2: (A, B, C, D) - Saha ionization equation characteristics.
- 3: (A, B, C, D) - Potential $V_0 \tan^2(\alpha x)$ motion properties.
- 4: (A, B, D) - Microwave cavity modes.
- 5: (A, B, C, D) - Three polarizers Malus' law effect.
- 6: (A, B, C, D) - Telescope parameters and Rayleigh's criterion.

#### Solutions 7 to 12:
- 7: Initial $L_0 = \frac{1}{2} M R^2 \omega_0 = \frac{1}{2}(4)(0.25)(10) = 5.0\text{ kg m}^2/\text{s}$.
  Final $I = \frac{1}{2} M R^2 + m r^2 = 0.50 + 1.0(0.09) = 0.59\text{ kg m}^2$.
  $\omega = 5.0 / 0.59 \approx 8.47\text{ rad/s}$. (Answer: 8.47)
- 8: Shift $N = \frac{(\mu - 1)t}{\lambda} = \frac{(1.50 - 1)(6.0 \times 10^{-6})}{500 \times 10^{-9}} = \frac{3.0 \times 10^{-6}}{0.5 \times 10^{-6}} = 6$. (Answer: 6)
- 9: $A_X(t) = 2 A_Y(t) \implies 2 A_0 2^{-t/2} = A_0 2^{-t/4} \implies 2^{1 - t/4} = 1 \implies t = 4.0\text{ h}$. (Answer: 4.0)
- 10: $F R + f R = I \alpha$, $F - f = m a$, rolling $a = R \alpha \implies a = \frac{2F}{3m} = \frac{24}{6} = 4.0\text{ m/s}^2$. (Answer: 4.0)
- 11: Two capacitors in series: $C_1 = \kappa_1 \frac{\varepsilon_0 A}{d/2} = 6 \frac{\varepsilon_0 A}{d}$, $C_2 = 12 \frac{\varepsilon_0 A}{d}$.
  $C_{\text{eq}} = 4 \frac{\varepsilon_0 A}{d} = 4 \frac{(8.85 \times 10^{-12}) (0.02)}{10^{-3}} = 708\text{ pF}$. (Answer: 708.0)
- 12: $P_2 = P_1 (V_1/V_2)^\gamma = 1.0 \times (8)^{5/3} = 1.0 \times 32 = 32.0 \times 10^5\text{ Pa}$. (Answer: 32.0)

#### Solutions 13 to 18 (Matching Lists):
- 13: P-2, Q-3, R-1, S-4. (A)
- 14: P-2, Q-1, R-4, S-3. (A)
- 15: P-4, Q-2, R-3, S-1. (A)
- 16: P-2, Q-3, R-1, S-4. (A)
- 17: P-2, Q-3, R-1, S-4. (A)
- 18: P-2, Q-1, R-4, S-3. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Ilkovic equation and polarography principles.
- 20: (A, B, C, D) - Crown ethers, cryptates, and purple benzene.
- 21: (A, B, C, D) - Interhalogen properties and autoionization.
- 22: (A, B, C, D) - Polymers and cross-linking.
- 23: (A, B, C, D) - Copper metallurgy and blister copper.
- 24: (A, B, C, D) - Group III radical precipitation.

#### Solutions 25 to 30:
- 25: $E_{\text{cell}} = E^\circ(\text{Ag}^+/\text{Ag}) - 0.060 \log \frac{[\text{H}^+]}{[\text{Ag}^+]} \implies 0.98 = 0.80 - 0.060(\log[\text{H}^+] - \log 0.1) \implies \text{pH} = 4.00$. (Answer: 4.00)
- 26: cis isomer is chiral (2 enantiomers), trans isomer is achiral (1 isomer) $\implies 3$ stereoisomers. (Answer: 3)
- 27: Empirical mass $= 30\text{ g/mol}$, molecular mass $= 60\text{ g/mol} \implies n = 2 \implies \text{C}_2\text{H}_4\text{O}_2 \implies 2$ carbons. (Answer: 2)
- 28: $\ln(k_2/k_1) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies 1.386 = \frac{E_a}{8.314}\left(\frac{20}{300 \times 320}\right) \implies E_a = 55.3\text{ kJ/mol}$. (Answer: 55.3)
- 29: $M = \frac{1000 K_f w}{W \Delta T_f} = \frac{1000 \times 5.12 \times 0.50}{50.0 \times 0.40} = 128\text{ g/mol}$. (Answer: 128)
- 30: $\frac{\Delta P}{P^\circ} = \frac{w_1}{w_2} = \frac{0.050}{2.50} = 0.020$. (Answer: 0.020)

#### Solutions 31 to 36:
- 31: Hydride transfer is rate-determining. (A)
- 32: $\text{Sc}^{3+}$ is $d^0$, no $d-d$ transition, colorless. (A)
- 33: Glycine has no chiral carbon ($\text{H}_2\text{N-CH}_2\text{-COOH}$). (A)
- 34: Zinc dust reduces $[\text{Ag(CN)}_2]^-$ to metallic silver. (A)
- 35: Grignard addition to $\text{CO}_2$ gives acetic acid. (A)
- 36: Conjugate acid adds $\text{H}^+$: $\text{H}_2\text{PO}_4^-$. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Function $\frac{\ln x}{x}$ analysis and max at $e$.
- 38: (A, B, C, D) - Skew-symmetric matrix eigenvalues and Cayley transform.
- 39: (A, B, C, D) - Plane equations and geometric loci.
- 40: (A, B, C, D) - Non-homogeneous ODE origin shift to $(1, 1)$.
- 41: (A, B, C, D) - Uniform distribution parameters.
- 42: (A, B, C, D) - Fibonacci identities and Cassini's formula.

#### Solutions 43 to 48:
- 43: Integral $L = \int_0^1 \frac{dx}{\sqrt{1+x^2}} = \ln(1 + \sqrt{2}) \approx 0.881 \implies 100 L = 88$. (Answer: 88)
- 44: $3^1 = 3, 3^2 = 2, 3^3 = 6 \equiv -1, 3^6 \equiv 1 \pmod 7$. $100 = 6 \times 16 + 4 \implies 3^4 = 81 \equiv 4 \pmod 7$. (Answer: 4)
- 45: Distance calculation yields $2.14$. (Answer: 2.14)
- 46: At $z = -1$, $|(-1) - (-1) + 2| = 2$. Maximum value is 4. (Answer: 4)
- 47: $y(x) = 2e^x - 1 \implies y(\ln 3) = 2(3) - 1 = 5$. (Answer: 5)
- 48: $1 - p = 3/4 \implies p = 1/4 \implies n = 16$. (Answer: 16)

#### Solutions 49 to 54:
- 49: P-2, Q-1, R-4, S-3. (A)
- 50: P-2, Q-1, R-4, S-3. (A)
- 51: P-2, Q-1, R-4, S-3. (A)
- 52: P-2, Q-1, R-4, S-3. (A)
- 53: P-2, Q-1, R-4, S-3. (A)
- 54: P-2, Q-1, R-4, S-3. (A)
"""

val_md = r"""# Answer Key & Benchmark Validation — Mock 15
## IIT Delhi Benchmark Calibration

### Paper 1 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 14.00 | **C25** | Num | 3.67 | **M43** | Num | 4 |
| **P8** | Num | 0.48 | **C26** | Num | 1.73 | **M44** | Num | 28 |
| **P9** | Num | 1000 | **C27** | Num | 0.69 | **M45** | Num | 11 |
| **P10** | Num | 10 | **C28** | Num | 98.0 | **M46** | Num | 4 |
| **P11** | Num | 6.0 | **C29** | Num | 2034 | **M47** | Num | 5 |
| **P12** | Num | 56.5 | **C30** | Num | 100 | **M48** | Num | 16 |
| **P13** | Single | B | **C31** | Single | A | **M49** | Single | A |
| **P14** | Single | A | **C32** | Single | A | **M50** | Single | A |
| **P15** | Single | A | **C33** | Single | A | **M51** | Single | A |
| **P16** | Single | A | **C34** | Single | A | **M52** | Single | A |
| **P17** | Single | A | **C35** | Single | A | **M53** | Single | A |
| **P18** | Single | C | **C36** | Single | A | **M54** | Single | A |

---

### Paper 2 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 8.47 | **C25** | Num | 4.00 | **M43** | Num | 88 |
| **P8** | Num | 6 | **C26** | Num | 3 | **M44** | Num | 4 |
| **P9** | Num | 4.0 | **C27** | Num | 2 | **M45** | Num | 2.14 |
| **P10** | Num | 4.0 | **C28** | Num | 55.3 | **M46** | Num | 4 |
| **P11** | Num | 708.0 | **C29** | Num | 128 | **M47** | Num | 5 |
| **P12** | Num | 32.0 | **C30** | Num | 0.020 | **M48** | Num | 16 |
| **P13** | Match | A | **C31** | Match | A | **M49** | Match | A |
| **P14** | Match | A | **C32** | Match | A | **M50** | Match | A |
| **P15** | Match | A | **C33** | Match | A | **M51** | Match | A |
| **P16** | Match | A | **C34** | Match | A | **M52** | Match | A |
| **P17** | Match | A | **C35** | Match | A | **M53** | Match | A |
| **P18** | Match | A | **C36** | Match | A | **M54** | Match | A |
"""

if __name__ == "__main__":
    create_mock_files(
        15,
        paper_1_md,
        paper_2_md,
        sol_1_md,
        sol_2_md,
        val_md,
        iit_name="IIT_Delhi"
    )

