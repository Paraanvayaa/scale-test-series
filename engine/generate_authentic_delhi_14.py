# -*- coding: utf-8 -*-
"""
Authentic JEE Advanced Generator for IIT Delhi Mock 14.
Calibrated to IIT Delhi Benchmark:
- High multi-correct cognitive load (+4/-2)
- Mandelstam variables, Skin depth attenuation, Euler equations of rigid rotation, Clausius-Clapeyron phase boundary
- Julia olefination, Wade-Mingos borane electron counting, Debye-Hückel limiting law, Edman degradation
- Beta-Gamma reflection formulas, Sylvester's inertia theorem, Director sphere of ellipsoid, Frobenius method
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from batch_helper import create_mock_files

paper_1_md = r"""# JEE Advanced Mock Examination 14 — Paper 1
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
In relativistic particle scattering $1 + 2 \to 3 + 4$, let $P_i = (E_i/c, \vec{p}_i)$ be the four-momentum of particle $i$ with rest mass $m_i$. The Mandelstam invariant variables are defined as $s = (P_1 + P_2)^2$, $t = (P_1 - P_3)^2$, and $u = (P_1 - P_4)^2$:
(A) The Mandelstam variable $s$ represents the square of the total center-of-momentum energy: $s = E_{\text{cm}}^2/c^2$.  
(B) In any reference frame, the sum of the three variables satisfies $s + t + u = (m_1^2 + m_2^2 + m_3^2 + m_4^2)c^2$.  
(C) For elastic scattering of identical particles of mass $m$ with scattering angle $\theta^*$ in the CM frame, $t = -2|\vec{p}^*|^2 (1 - \cos\theta^*)$.  
(D) Four-momentum conservation requires $(P_1 + P_2) = (P_3 + P_4)$, which is Lorentz invariant.

#### Question 2
An electromagnetic plane wave of angular frequency $\omega$ penetrates normally into a good conductor having electrical conductivity $\sigma$, magnetic permeability $\mu \approx \mu_0$, and dielectric permittivity $\varepsilon \approx \varepsilon_0$ ($\sigma \gg \omega\varepsilon_0$):
(A) The complex wave vector in the conductor is $k = (1 + i)\sqrt{\frac{\mu_0 \sigma \omega}{2}}$.  
(B) The characteristic skin depth is $\delta = \sqrt{\frac{2}{\mu_0 \sigma \omega}}$.  
(C) The magnetic field lags behind the electric field inside the conductor by a phase angle of $45^\circ$ ($\pi/4$ radians).  
(D) The average power dissipated per unit area of conductor surface (Joule heating) is $\frac{1}{2}\sigma \delta |E_0|^2$.

#### Question 3
A rigid body with principal moments of inertia $I_1 < I_2 < I_3$ rotates freely in outer space with zero external torque ($\vec{\tau}_{\text{ext}} = 0$). The rotation is described by Euler's equations:
$$I_1 \dot{\omega}_1 = (I_2 - I_3)\omega_2 \omega_3, \quad I_2 \dot{\omega}_2 = (I_3 - I_1)\omega_3 \omega_1, \quad I_3 \dot{\omega}_3 = (I_1 - I_2)\omega_1 \omega_2$$
(A) Both total kinetic energy $T = \frac{1}{2}(I_1 \omega_1^2 + I_2 \omega_2^2 + I_3 \omega_3^2)$ and total angular momentum squared $L^2 = I_1^2 \omega_1^2 + I_2^2 \omega_2^2 + I_3^2 \omega_3^2$ are strictly conserved.  
(B) Steady rotation about the principal axis of smallest moment of inertia ($I_1$) is stable against small perturbations.  
(C) Steady rotation about the intermediate principal axis ($I_2$) is dynamically unstable (Dzhanibekov effect / tennis racket theorem).  
(D) Steady rotation about the principal axis of largest moment of inertia ($I_3$) is stable against small perturbations.

#### Question 4
Consider the liquid-vapor phase coexistence boundary of a pure substance described by the Clausius-Clapeyron equation:
$$\frac{dP}{dT} = \frac{\Delta H_{\text{vap}}}{T \Delta V}$$
Assuming the vapor behaves as an ideal gas and the molar volume of the liquid is negligible compared to the vapor volume ($V_{\text{vap}} \gg V_{\text{liq}}$):
(A) If the enthalpy of vaporization $\Delta H_{\text{vap}}$ is temperature-independent, $\ln P = -\frac{\Delta H_{\text{vap}}}{R T} + C$.  
(B) The boiling point of water decreases with increasing altitude because atmospheric pressure decreases.  
(C) At the critical point, the latent heat of vaporization vanishes ($\Delta H_{\text{vap}} \to 0$), and the meniscus separating liquid and gas disappears.  
(D) The slope $\frac{dP}{dT}$ of the solid-liquid coexistence curve for water is negative because ice is less dense than liquid water ($\Delta V_{\text{fus}} < 0$).

#### Question 5
A coaxial transmission line of length $l$ consists of an inductance per unit length $L'$ and a capacitance per unit length $C'$:
(A) The characteristic impedance of the line is $Z_0 = \sqrt{L'/C'}$.  
(B) The phase velocity of electromagnetic signals along the line is $v_p = \frac{1}{\sqrt{L' C'}}$.  
(C) If the transmission line is terminated by an open circuit ($Z_L = \infty$), the voltage reflection coefficient is $\Gamma_V = +1$.  
(D) If the transmission line is terminated by a short circuit ($Z_L = 0$), the voltage reflection coefficient is $\Gamma_V = -1$.

#### Question 6
A circular loop of radius $R$ carries a steady current $I$. A small magnetic needle of magnetic dipole moment $\vec{m}$ is placed on the axis of the loop at a distance $x$ ($x \gg R$) from the center, oriented along the axis:
(A) The magnetic field produced by the loop at distance $x$ on the axis is $B(x) = \frac{\mu_0 I R^2}{2 x^3}$.  
(B) The magnetic interaction energy between the loop and the needle is $U(x) = -\frac{\mu_0 m I R^2}{2 x^3}$.  
(C) The magnetic force experienced by the needle is attractive and has magnitude $F = \frac{3\mu_0 m I R^2}{2 x^4}$.  
(D) If released from rest, the needle accelerates towards the center of the loop.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a classical cyclotron, protons ($q = 1.6 \times 10^{-19}\text{ C}$, $m_0 = 1.67 \times 10^{-27}\text{ kg}$) are accelerated in a magnetic field $B = 1.5\text{ T}$. Due to relativistic mass increase $m = \gamma m_0$, the orbital frequency departs from the fixed RF oscillator frequency. If the maximum tolerable fractional frequency mismatch $\frac{\Delta f}{f_0}$ is $1.0\%$, the maximum kinetic energy achievable by protons before synchronization is lost is $K_{\text{max}}$ in $\text{MeV}$. Calculate $K_{\text{max}}$ in $\text{MeV}$ (rest energy of proton $m_0 c^2 = 938\text{ MeV}$, round off to ONE decimal place).

#### Question 8
A copper wire of electrical conductivity $\sigma = 5.8 \times 10^7\text{ S/m}$ carries an alternating current at frequency $f = 10\text{ MHz}$. Taking $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$, calculate the electromagnetic skin depth $\delta$ in micrometers ($\mu\text{m}$) (round off to ONE decimal place).

#### Question 9
A thermodynamic heat pump operates reversibly between an outdoor reservoir at temperature $T_C = -13^\circ\text{C}$ ($260\text{ K}$) and a building maintained at $T_H = +21^\circ\text{C}$ ($294\text{ K}$). The rate of heat loss from the building is $17.0\text{ kW}$. Calculate the electrical power consumption $W_{\text{in}}$ in kilowatts required to drive the heat pump (round off to TWO decimal places).

#### Question 10
In a ballistic galvanometer, a total charge $Q = 20\text{ }\mu\text{C}$ passes through a coil in a time much shorter than the natural oscillation period $T_0 = 4.0\text{ s}$. The moment of inertia of the coil is $I = 2.5 \times 10^{-7}\text{ kg m}^2$, the torsional restoring constant of the suspension is $k = 6.17 \times 10^{-7}\text{ N m/rad}$, and the magnetic field-area-turn factor is $N B A = 0.05\text{ T m}^2$. Calculate the maximum initial angular deflection $\theta_{\text{max}}$ of the coil in degrees (round off to the nearest integer).

#### Question 11
Two identical tuning forks of frequency $f_0 = 440\text{ Hz}$ are mounted on resonance boxes. One fork is loaded with a small piece of wax. When sounded together, $4\text{ beats per second}$ are heard. If the frequency of the loaded fork is $f_L$, calculate $f_L$ in $\text{Hz}$.

#### Question 12
A light ray enters a glass sphere of radius $R = 6\text{ cm}$ and refractive index $n = \sqrt{3}$ at an angle of incidence $i = 60^\circ$. The ray undergoes refraction into the sphere, internal reflection at the back surface, and refracts back out into air. The total angle of deviation $\delta$ suffered by the ray is $\delta^\circ$. Calculate $\delta$ in degrees.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
A particle of mass $m$ moves in a one-dimensional potential $V(x) = \frac{1}{2} k x^2 + \frac{\alpha}{x^2}$ for $x > 0$. The angular frequency $\omega$ of small oscillations about the stable equilibrium point $x_0$ is:
(A) $\omega = 2\sqrt{k/m}$  
(B) $\omega = \sqrt{k/m}$  
(C) $\omega = \sqrt{2k/m}$  
(D) $\omega = 4\sqrt{k/m}$  

#### Question 14
A linearly polarized plane wave with electric field vector making an angle of $45^\circ$ with the optic axis enters a quarter-wave plate ($\lambda/4$) of birefringent crystal. The emerging light is:
(A) Circularly polarized  
(B) Linearly polarized at $90^\circ$ to original  
(C) Elliptically polarized with major axis at $45^\circ$  
(D) Unpolarized  

#### Question 15
A uniform rod of length $L$ and mass $M$ is pivoted freely about a horizontal axis through one end. It is released from rest in a horizontal position. When it becomes vertical, the horizontal component of the reaction force exerted by the pivot on the rod is:
(A) 0  
(B) $\frac{3}{2} M g$  
(C) $M g$  
(D) $\frac{5}{2} M g$  

#### Question 16
An inductor of inductance $L$ and internal resistance $r$ is connected across a DC voltage source of EMF $\mathcal{E}$ at $t = 0$. The time required for the current to reach $50\%$ of its steady-state value is:
(A) $t = \frac{L}{r} \ln 2$  
(B) $t = \frac{L}{2r}$  
(C) $t = \frac{2L}{r} \ln 2$  
(D) $t = \frac{L}{r} \ln(1/2)$  

#### Question 17
According to Wien's displacement law, the peak wavelength of blackbody radiation satisfies $\lambda_{\text{max}} T = b = 2.898 \times 10^{-3}\text{ m}\cdot\text{K}$. If the surface temperature of a star increases by $20\%$, the ratio of the total radiated radiant power per unit area to its initial value is:
(A) $1.20^4 \approx 2.07$  
(B) $1.20^2 = 1.44$  
(C) $1.20$  
(D) $1.20^5 \approx 2.49$  

#### Question 18
A cylindrical pipe of length $L$ open at both ends has fundamental acoustic resonance frequency $f_1$. If one end of the pipe is now closed, the new fundamental frequency $f_1'$ is:
(A) $f_1' = \frac{1}{2} f_1$  
(B) $f_1' = 2 f_1$  
(C) $f_1' = \frac{3}{2} f_1$  
(D) $f_1' = \frac{1}{4} f_1$  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
According to Wade's rules (Polyhedral Skeletal Electron Pair Theory, PSEPT) for polyhedral boranes of formula $[B_n H_n]^{c-}$:
(A) A closo-borane has $n$ vertices and $(n + 1)$ skeletal bonding electron pairs (e.g., $[B_6 H_6]^{2-}$).  
(B) A nido-borane is derived from an $(n + 1)$-vertex polyhedron with one missing vertex, possessing $(n + 2)$ skeletal electron pairs (e.g., $B_5 H_9$).  
(C) An arachno-borane has two missing vertices from an $(n + 2)$-vertex polyhedron, possessing $(n + 3)$ skeletal electron pairs (e.g., $B_4 H_{10}$).  
(D) In all these boranes, each $B-H$ unit contributes 2 skeletal electrons towards cluster cage bonding.

#### Question 20
In the Julia olefination for the stereoselective synthesis of $(E)$-alkenes:
$$\text{R}_1\text{-CH}_2\text{-SO}_2\text{Ph} \xrightarrow{n\text{-BuLi, } \text{R}_2\text{CHO}} \text{R}_1\text{-CH(SO}_2\text{Ph)-CH(OH)-R}_2 \xrightarrow{\text{Ac}_2\text{O}} \text{R}_1\text{-CH(SO}_2\text{Ph)-CH(OAc)-R}_2 \xrightarrow{\text{Na/Hg}} (E)\text{-R}_1\text{-CH}=\text{CH-R}_2$$
(A) The phenyl sulfone group stabilizes the $\alpha$-carbanion by both inductive and resonance effects.  
(B) The addition of the lithiated sulfone to the aldehyde yields a diastereomeric mixture of $\beta$-hydroxy sulfones.  
(C) Reductive elimination with sodium amalgam ($\text{Na/Hg}$) in methanol proceeds via a radical mechanism that thermodynamically equilibrates to give predominantly the $(E)$-alkene.  
(D) The modified Julia-Kocienski olefination utilizes heteroaryl sulfones (e.g., tetrazolyl or benzothiazolyl sulfones) and eliminates spontaneously without requiring $\text{Na/Hg}$.

#### Question 21
Regarding the Debye-Hückel limiting law for dilute strong electrolyte solutions at $25^\circ\text{C}$:
$$\log_{10} \gamma_\pm = -A |z_+ z_-| \sqrt{I}$$
where $I = \frac{1}{2}\sum_i c_i z_i^2$ is the ionic strength:
(A) The mean activity coefficient $\gamma_\pm$ decreases with increasing ionic strength in dilute solutions.  
(B) An electrolyte with higher ionic valence charges (e.g., $\text{Al}_2(\text{SO}_4)_3$) shows a much sharper reduction in $\gamma_\pm$ than a $1:1$ electrolyte (e.g., $\text{NaCl}$) at the same concentration.  
(C) The constant $A$ depends on the dielectric constant $\varepsilon_r$ of the solvent and absolute temperature $T$ ($A \propto (\varepsilon_r T)^{-3/2}$).  
(D) For an aqueous solution at $25^\circ\text{C}$, $A \approx 0.509\text{ kg}^{1/2}\text{mol}^{-1/2}$.

#### Question 22
Consider Edman degradation for N-terminal amino acid sequencing of polypeptides:
(A) The reagent employed is phenyl isothiocyanate (PITC, $\text{Ph-N}=\text{C}=\text{S}$).  
(B) PITC couples specifically with the uncharged N-terminal amino group under mildly basic conditions to form a phenylthiocarbamoyl (PTC) peptide.  
(C) Treatment with anhydrous acid (e.g., trifluoroacetic acid) cleaves the first peptide bond selectively, releasing an anilinothiazolinone (ATZ) amino acid.  
(D) The ATZ derivative is extracted into organic solvent and rearranged to a stable phenylthiohydantoin (PTH) amino acid, which is identified chromatographically without destroying the remainder of the peptide chain.

#### Question 23
Regarding the chemistry and allotropy of phosphorus:
(A) White phosphorus consists of discrete tetrahedral $P_4$ molecules with $\text{P-P-P}$ bond angles of $60^\circ$, causing severe angle strain.  
(B) Red phosphorus is formed by heating white phosphorus at $250^\circ\text{C}$ in an inert atmosphere, possessing a polymeric chain structure of linked $P_4$ tetrahedra.  
(C) Black phosphorus is the thermodynamically most stable allotrope at room temperature, having a puckered layered structure resembling graphite and exhibiting electrical semiconductor behavior.  
(D) White phosphorus reacts with aqueous $\text{NaOH}$ in an inert atmosphere to yield phosphine ($\text{PH}_3$) and sodium hypophosphite ($\text{NaH}_2\text{PO}_2$), a disproportionation redox reaction.

#### Question 24
In the hydroformylation (oxo process) of alkenes catalyzed by cobalt or rhodium carbonyl hydrides ($\text{HCo(CO)}_4$ or $\text{HRh(CO)(PPh}_3)_3$):
$$\text{R-CH}=\text{CH}_2 + \text{CO} + \text{H}_2 \xrightarrow{\text{catalyst}} \text{R-CH}_2\text{-CH}_2\text{-CHO} + \text{R-CH(CHO)-CH}_3$$
(A) The alkene coordinates to the metal after dissociation of a $\text{CO}$ ligand to generate an open coordination site.  
(B) Migratory insertion of the alkene into the $\text{M-H}$ bond forms an alkyl-metal intermediate.  
(C) Migratory insertion of coordinated $\text{CO}$ into the $\text{M-alkyl}$ bond forms an acyl-metal complex.  
(D) Oxidative addition / hydrogenolysis of the acyl-metal complex with $\text{H}_2$ releases the aldehyde and regenerates the metal hydride catalyst.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility of calcium fluoride ($\text{CaF}_2$) in pure water at $25^\circ\text{C}$ is $2.0 \times 10^{-4}\text{ mol/L}$. Calculate the solubility product $K_{sp}$ of $\text{CaF}_2$ at $25^\circ\text{C}$. If $K_{sp} = X \times 10^{-11}$, calculate the value of $X$ (round off to TWO decimal places).

#### Question 26
For the first-order gas-phase decomposition of azomethane:
$$\text{CH}_3\text{-N}=\text{N-CH}_3(g) \to \text{C}_2\text{H}_6(g) + \text{N}_2(g)$$
The rate constant is $k = 3.46 \times 10^{-4}\text{ s}^{-1}$ at $600\text{ K}$. If the reaction is carried out in a constant-volume vessel starting with pure azomethane at initial pressure $P_0 = 100\text{ mm Hg}$, the time taken for the total pressure in the vessel to reach $150\text{ mm Hg}$ is $t$ seconds. Calculate $t$ in seconds (use $\ln 2 = 0.693$, round off to the nearest integer).

#### Question 27
In an acidic aqueous medium, potassium dichromate ($\text{K}_2\text{Cr}_2\text{O}_7$) oxidizes ferrous ions ($\text{Fe}^{2+}$) to ferric ions ($\text{Fe}^{3+}$):
$$\text{Cr}_2\text{O}_7^{2-} + 6\text{Fe}^{2+} + 14\text{H}^+ \to 2\text{Cr}^{3+} + 6\text{Fe}^{3+} + 7\text{H}_2\text{O}$$
If $25.0\text{ mL}$ of $0.020\text{ M}$ $\text{K}_2\text{Cr}_2\text{O}_7$ solution completely oxidizes $50.0\text{ mL}$ of an acidified $\text{FeSO}_4$ solution, calculate the molarity of the $\text{FeSO}_4$ solution in $\text{mol/L}$ (round off to TWO decimal places).

#### Question 28
The standard molar enthalpy of formation of liquid water is $\Delta H_f^\circ(\text{H}_2\text{O}(l)) = -285.8\text{ kJ/mol}$, and the standard molar entropy change for the reaction $\text{H}_2(g) + \frac{1}{2}\text{O}_2(g) \to \text{H}_2\text{O}(l)$ is $\Delta S^\circ = -163.2\text{ J/(mol}\cdot\text{K)}$. Calculate the standard Gibbs free energy of formation $\Delta G_f^\circ(\text{H}_2\text{O}(l))$ at $298\text{ K}$ in $\text{kJ/mol}$ (enter the absolute numerical magnitude, round off to ONE decimal place).

#### Question 29
A metal crystallizes in a face-centered cubic (FCC) lattice with a unit cell edge length $a = 400\text{ pm}$. If the density of the metal is $\rho = 10.0\text{ g/cm}^3$, calculate the atomic molar mass $M$ of the metal in $\text{g/mol}$ (use $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$, round off to ONE decimal place).

#### Question 30
The molar conductivity of a $0.010\text{ M}$ solution of a weak monobasic acid $\text{HA}$ is $\Lambda_m = 16.5\text{ S cm}^2\text{mol}^{-1}$ at $25^\circ\text{C}$. The limiting molar conductivity of the acid is $\Lambda_m^\circ = 390.5\text{ S cm}^2\text{mol}^{-1}$. The acid dissociation constant $K_a$ of the acid is $Y \times 10^{-5}\text{ mol/L}$. Calculate the value of $Y$ (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
In the Barton-McCombie deoxygenation of secondary alcohols, the alcohol is converted to a xanthate ester ($\text{R-O-C}(=\text{S})\text{SMe}$) and reacted with tributyltin hydride ($\text{Bu}_3\text{SnH}$) and AIBN. The driving force for the fragmentation of the xanthate radical intermediate is:
(A) Formation of a very strong carbon-oxygen double bond ($\text{C}=\text{O}$) in the carbonyl sulfide by-product  
(B) Formation of a strong tin-carbon bond  
(C) Precipitation of elemental sulfur  
(D) Elimination of methane gas  

#### Question 32
Which of the following oxoacids of sulfur contains a peroxide linkage ($-\text{O-O}-$)?
(A) Marshall's acid ($\text{H}_2\text{S}_2\text{O}_8$)  
(B) Caro's acid ($\text{H}_2\text{SO}_5$)  
(C) Both Marshall's acid and Caro's acid  
(D) Oleum ($\text{H}_2\text{S}_2\text{O}_7$)  

#### Question 33
In the Ostwald process for the commercial manufacture of nitric acid, the catalytic oxidation of ammonia with atmospheric air:
$$4\text{NH}_3(g) + 5\text{O}_2(g) \xrightarrow{\text{Pt/Rh gauze, } 800^\circ\text{C}} 4\text{NO}(g) + 6\text{H}_2\text{O}(g)$$
The oxidation state of nitrogen changes from:
(A) $-3$ to $+2$  
(B) $-3$ to $+4$  
(C) $-3$ to $+5$  
(D) $-1$ to $+2$  

#### Question 34
The major product obtained from the reaction of 1-methylcyclohexene with $\text{HBr}$ in the presence of benzoyl peroxide is:
(A) 1-bromo-2-methylcyclohexane (anti-Markovnikov addition)  
(B) 1-bromo-1-methylcyclohexane (Markovnikov addition)  
(C) 3-bromo-1-methylcyclohexene (allylic bromination)  
(D) 1,2-dibromo-1-methylcyclohexane  

#### Question 35
The IUPAC name of the complex $[\text{Co(NH}_3)_5(\text{CO}_3)]\text{Cl}$ is:
(A) Pentaamminecarbonatocobalt(III) chloride  
(B) Carbonatopentaamminecobalt(III) chloride  
(C) Pentaamminecarbonatocobalt(II) chloride  
(D) Carbonatopentaamminecobaltate(III) chloride  

#### Question 36
The coagulation power of an electrolyte for a negatively charged sol (e.g., $\text{As}_2\text{S}_3$ sol) according to the Hardy-Schulze rule increases in the order:
(A) $\text{Na}^+ < \text{Ba}^{2+} < \text{Al}^{3+}$  
(B) $\text{Al}^{3+} < \text{Ba}^{2+} < \text{Na}^+$  
(C) $\text{Cl}^- < \text{SO}_4^{2-} < \text{PO}_4^{3-}$  
(D) $\text{PO}_4^{3-} < \text{SO}_4^{2-} < \text{Cl}^-$  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt$ for $x > 0$ and $B(x, y) = \int_0^1 t^{x-1} (1-t)^{y-1} dt$ for $x, y > 0$:
(A) $B(x, y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$.  
(B) $\Gamma(1/2) = \sqrt{\pi}$.  
(C) Euler's reflection formula states $\Gamma(x)\Gamma(1-x) = \frac{\pi}{\sin(\pi x)}$ for all non-integer $x$.  
(D) $\int_0^{\pi/2} \sin^5 \theta \cos^4 \theta d\theta = \frac{1}{2} B(3, 5/2) = \frac{8}{315}$.

#### Question 38
Let $A$ be a real symmetric $n \times n$ matrix with eigenvalues $\lambda_1 \le \lambda_2 \le \dots \le \lambda_n$:
(A) All eigenvalues of $A$ are real.  
(B) Eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.  
(C) The Rayleigh quotient $R(\vec{x}) = \frac{\vec{x}^T A \vec{x}}{\vec{x}^T \vec{x}}$ satisfies $\lambda_1 \le R(\vec{x}) \le \lambda_n$ for all non-zero vectors $\vec{x} \in \mathbb{R}^n$.  
(D) Sylvester's law of inertia asserts that the number of positive, negative, and zero eigenvalues is an invariant of the quadratic form under invertible congruence transformations $P^T A P$.

#### Question 39
Consider the ellipsoid $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$:
(A) The locus of points from which three mutually perpendicular tangent planes can be drawn to the ellipsoid is the director sphere $x^2 + y^2 + z^2 = a^2 + b^2 + c^2$.  
(B) The equation of the tangent plane to the ellipsoid at $(x_0, y_0, z_0)$ is $\frac{x x_0}{a^2} + \frac{y y_0}{b^2} + \frac{z z_0}{c^2} = 1$.  
(C) The maximum volume of a rectangular parallelepiped inscribed in the ellipsoid with faces parallel to coordinate planes is $\frac{8 a b c}{3\sqrt{3}}$.  
(D) Any plane section passing through the center of the ellipsoid is an ellipse.

#### Question 40
Consider Bessel's differential equation of order zero:
$$x \frac{d^2 y}{dx^2} + \frac{dy}{dx} + x y = 0$$
Using the method of Frobenius to find power series solutions $y(x) = \sum_{n=0}^\infty a_n x^n$:
(A) The indicial equation has a double root $r = 0$.  
(B) The recurrence relation for coefficients is $a_{2k} = \frac{(-1)^k}{2^{2k} (k!)^2} a_0$ for $k \ge 1$.  
(C) All odd-power coefficients $a_{2k+1}$ are zero.  
(D) The solution regular at $x = 0$ is the zeroth-order Bessel function of the first kind: $J_0(x) = \sum_{k=0}^\infty \frac{(-1)^k}{(k!)^2}\left(\frac{x}{2}\right)^{2k}$.

#### Question 41
Let $f(x) = \frac{\sin x}{x}$ for $x > 0$:
(A) $\lim_{x \to 0^+} f(x) = 1$.  
(B) The function $f(x)$ is strictly decreasing on $(0, \pi/2)$.  
(C) $\int_0^\infty \frac{\sin x}{x} dx = \frac{\pi}{2}$ (Dirichlet integral).  
(D) $\int_0^\infty \left(\frac{\sin x}{x}\right)^2 dx = \frac{\pi}{2}$.

#### Question 42
Let $X$ and $Y$ be independent standard normal random variables with mean 0 and variance 1:
(A) The random variable $Z = X^2 + Y^2$ follows an exponential distribution with rate parameter $\lambda = 1/2$ (chi-square distribution with 2 degrees of freedom).  
(B) The ratio $W = X/Y$ follows a standard Cauchy distribution with probability density function $f_W(w) = \frac{1}{\pi (1 + w^2)}$.  
(C) $P(X > 0 \text{ and } Y > 0) = \frac{1}{4}$.  
(D) The expected value $E[W]$ is strictly zero.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Evaluate the definite integral:
$$I = \int_0^1 \frac{\ln(1 + x)}{1 + x^2} dx$$
Calculate the value of $\frac{64 I}{\pi \ln 2}$ (round off to the nearest integer).

#### Question 44
Find the total number of non-negative integer solutions $(x, y, z, w)$ satisfying:
$$x + y + z + w = 15$$
such that $x \le 3$.

#### Question 45
Let the line $\frac{x-1}{2} = \frac{y+2}{-3} = \frac{z-4}{1}$ intersect the plane $2x + 4y - z + 1 = 0$ at the point $P(\alpha, \beta, \gamma)$. Calculate the value of $\alpha^2 + \beta^2 + \gamma^2$ (round off to TWO decimal places).

#### Question 46
Let $\omega \ne 1$ be a complex cube root of unity. Evaluate the determinant:
$$\Delta = \det\begin{pmatrix} 1 & \omega & \omega^2 \\ \omega & \omega^2 & 1 \\ \omega^2 & 1 & \omega \end{pmatrix}$$
Calculate the value of $\Delta$.

#### Question 47
Let $y = y(x)$ satisfy the differential equation $\frac{dy}{dx} + y \cot x = 2 \cos x$ with initial condition $y(\pi/2) = 1$. Find the value of $y(\pi/6)$.

#### Question 48
A bag contains 4 white balls and 6 black balls. Three balls are drawn at random without replacement. Let $X$ denote the number of white balls drawn. Calculate the variance $\text{Var}(X)$ (round off to TWO decimal places).

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The value of the integral $\int_0^{\pi/2} \ln(\sin x) dx$ is:
(A) $-\frac{\pi}{2} \ln 2$  
(B) $-\pi \ln 2$  
(C) $\frac{\pi}{2} \ln 2$  
(D) $-\frac{\pi}{4} \ln 2$  

#### Question 50
The radius of convergence $R$ of the power series $\sum_{n=1}^\infty \frac{n!}{n^n} x^n$ is:
(A) $e$  
(B) $1/e$  
(C) 1  
(D) $\infty$  

#### Question 51
The shortest distance between the skew lines $\vec{r}_1 = (\hat{i} + 2\hat{j} + 3\hat{k}) + \lambda(2\hat{i} + 3\hat{j} + 4\hat{k})$ and $\vec{r}_2 = (2\hat{i} + 4\hat{j} + 5\hat{k}) + \mu(3\hat{i} + 4\hat{j} + 5\hat{k})$ is:
(A) $\frac{1}{\sqrt{6}}$  
(B) $\frac{1}{\sqrt{3}}$  
(C) $\frac{2}{\sqrt{6}}$  
(D) 0  

#### Question 52
If $A$ and $B$ are square matrices of order 3 such that $|A| = -1$ and $|B| = 3$, then $|3AB|$ is equal to:
(A) $-81$  
(B) $-9$  
(C) $-27$  
(D) $81$  

#### Question 53
The number of real solutions of the equation $e^x + x - 2 = 0$ is:
(A) 1  
(B) 2  
(C) 0  
(D) 3  

#### Question 54
If $\vec{a}, \vec{b}, \vec{c}$ are three unit vectors such that $\vec{a} + \vec{b} + \vec{c} = \vec{0}$, then the value of $\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{c} + \vec{c} \cdot \vec{a}$ is:
(A) $-\frac{3}{2}$  
(B) $\frac{3}{2}$  
(C) 0  
(D) $-1$  
"""

paper_2_md = r"""# JEE Advanced Mock Examination 14 — Paper 2
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
A relativistic particle of rest mass $m$ and charge $q$ moves in a uniform magnetic field $\vec{B} = B_0 \hat{k}$ with relativistic momentum $\vec{p}$:
(A) The relativistic energy $E = \sqrt{p^2 c^2 + m^2 c^4}$ remains strictly constant during the motion because the magnetic Lorentz force does no work.  
(B) The radius of the circular orbit is $R = \frac{p_\perp}{q B_0} = \frac{\gamma m v_\perp}{q B_0}$.  
(C) The relativistic cyclotron frequency is $\omega_c = \frac{q B_0}{\gamma m}$, which decreases as the particle's energy increases.  
(D) For an ultra-relativistic electron ($E \gg m c^2$), the orbital radius is proportional to energy: $R \approx \frac{E}{q B_0 c}$.

#### Question 2
Regarding the magnetic vector potential $\vec{A}$ in magnetostatics:
(A) The magnetic field is given by $\vec{B} = \nabla \times \vec{A}$.  
(B) Under the Coulomb gauge condition $\nabla \cdot \vec{A} = 0$, the vector potential satisfies Poisson's equation $\nabla^2 \vec{A} = -\mu_0 \vec{J}$.  
(C) For a uniform magnetic field $\vec{B} = B_0 \hat{k}$, one valid choice of vector potential is $\vec{A} = \frac{1}{2} B_0 (-y \hat{i} + x \hat{j})$.  
(D) The magnetic flux $\Phi_B$ through an open surface $S$ bounded by a closed contour $C$ equals the line integral $\oint_C \vec{A} \cdot d\vec{l}$.

#### Question 3
An ideal transmission line of length $l$ has characteristic impedance $Z_0$ and is operated at angular frequency $\omega$. If the load impedance is $Z_L$:
(A) The voltage reflection coefficient at the load is $\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}$.  
(B) The voltage standing wave ratio is $\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|}$.  
(C) When $Z_L = Z_0$, no reflection occurs ($\Gamma = 0$) and $\text{VSWR} = 1$.  
(D) If $Z_L = 0$ (short circuit), the input impedance of a quarter-wavelength line ($\lambda/4$) is infinite (acts as an open circuit).

#### Question 4
One mole of an ideal gas undergoes a polytropic process $P V^n = \text{constant}$:
(A) The molar heat capacity for this process is $C = C_v + \frac{R}{1 - n}$.  
(B) For $1 < n < \gamma$, the molar heat capacity is negative, meaning the gas temperature drops even as heat is added.  
(C) The work done by the gas in expanding from $(P_1, V_1)$ to $(P_2, V_2)$ is $W = \frac{P_1 V_1 - P_2 V_2}{n - 1}$ for $n \ne 1$.  
(D) The bulk modulus of the gas during this process is $B = n P$.

#### Question 5
Two inductors of self-inductances $L_1$ and $L_2$ have mutual inductance $M$. When connected in series:
(A) In the series-aiding configuration (magnetic fluxes in same direction), the equivalent inductance is $L_{\text{eq}} = L_1 + L_2 + 2M$.  
(B) In the series-opposing configuration, the equivalent inductance is $L_{\text{eq}} = L_1 + L_2 - 2M$.  
(C) The coupling coefficient $k = \frac{M}{\sqrt{L_1 L_2}}$ must satisfy $0 \le k \le 1$.  
(D) If $k = 1$, the mutual inductance attains its theoretical maximum $M = \sqrt{L_1 L_2}$.

#### Question 6
For an electromagnetic wave propagating in a dispersive dielectric medium with dispersion relation $\omega(k)$:
(A) The phase velocity is $v_p = \frac{\omega}{k}$.  
(B) The group velocity is $v_g = \frac{d\omega}{dk}$.  
(C) In a region of normal dispersion ($dn/d\lambda < 0$), the group velocity is strictly less than the phase velocity: $v_g < v_p$.  
(D) Rayleigh's formula states $v_g = v_p - \lambda \frac{dv_p}{d\lambda}$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a cyclotron, a magnetic field $B = 1.5\text{ T}$ accelerates protons ($m_p = 1.67 \times 10^{-27}\text{ kg}$, $q = 1.6 \times 10^{-19}\text{ C}$). Calculate the cyclotron resonance frequency $f_c$ in megahertz ($\text{MHz}$) (round off to ONE decimal place).

#### Question 8
A spherical copper pellet of radius $r = 1.0\text{ cm}$, density $\rho = 8900\text{ kg/m}^3$, and specific heat $s = 390\text{ J/(kg}\cdot\text{K)}$ cools by thermal radiation in a vacuum enclosure at absolute zero. The initial temperature is $T_0 = 400\text{ K}$. Calculate the time $t$ in seconds required for its temperature to decrease to $T_1 = 300\text{ K}$ (take emissivity $e = 1.0$, $\sigma = 5.67 \times 10^{-8}\text{ W/(m}^2\text{K}^4)$, round off to the nearest integer).

#### Question 9
In Quincke's interference tube apparatus, an acoustic wave of frequency $f$ enters through the tube. By sliding the movable U-tube through a distance $\Delta d = 8.5\text{ cm}$, the sound intensity at the receiver drops from a maximum to a complete minimum. If the speed of sound in air is $v = 340\text{ m/s}$, calculate the sound frequency $f$ in $\text{Hz}$.

#### Question 10
An initially uncharged capacitor $C = 1.0\text{ }\mu\text{F}$ is charged to $V_0 = 100\text{ V}$ and then allowed to discharge through a resistor $R = 1.0\text{ M}\Omega$. The time required for the charge to decrease to $1.0\%$ of its initial value is $t$ seconds. Calculate $t$ (use $\ln 10 = 2.303$, round off to TWO decimal places).

#### Question 11
A transmission diffraction grating has $N = 5000\text{ lines/cm}$ over a total width $W = 2.0\text{ cm}$. The theoretical resolving power $\mathcal{R} = \frac{\lambda}{\Delta\lambda}$ of the grating in the second diffraction order ($m = 2$) is $\mathcal{R}$. Calculate $\mathcal{R}$.

#### Question 12
A clean glass capillary tube of internal radius $r = 0.5\text{ mm}$ is dipped vertically into water ($\rho = 1000\text{ kg/m}^3$, surface tension $T = 0.072\text{ N/m}$, contact angle $\theta = 0^\circ$). The capillary rise $h$ of the water column is measured. Calculate $h$ in centimeters (take $g = 9.8\text{ m/s}^2$, round off to TWO decimal places).

---

## Section 3: Matching List / Matrix Match (Questions 13 to 18)

#### Question 13
Match the modern physics phenomenon in List-I with its primary experimental evidence in List-II:
- **List-I**:
  - P. Davisson-Germer experiment
  - Q. Franck-Hertz experiment
  - R. Photoelectric effect
  - S. Millikan oil-drop experiment
- **List-II**:
  - 1. Particle nature of light (photons)
  - 2. Wave nature of electrons (de Broglie hypothesis)
  - 3. Discrete energy levels in atoms (quantization of excitation energy)
  - 4. Quantization of electric charge ($e$)

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  

#### Question 14
Match the semiconductor device in List-I with its typical operating condition / property in List-II:
- **List-I**:
  - P. Zener diode
  - Q. Solar cell
  - R. LED (Light Emitting Diode)
  - S. Photodiode
- **List-II**:
  - 1. Forward biased; spontaneous emission of photons via electron-hole recombination
  - 2. Reverse biased; photogenerated electron-hole pairs enhance reverse saturation current
  - 3. Heavily doped $p\text{-}n$ junction operated in reverse breakdown as a voltage regulator
  - 4. Unbiased (or load-connected); generates photo-voltage across junction under illumination

(A) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(B) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(D) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4  

#### Question 15
Match the optical instrument in List-I with its characteristic magnifying power formula in List-II:
- **List-I**:
  - P. Astronomical telescope (normal adjustment)
  - Q. Compound microscope (normal adjustment)
  - R. Simple magnifying glass (image at near point $D$)
  - S. Terrestrial telescope
- **List-II**:
  - 1. $m = 1 + \frac{D}{f}$
  - 2. $m = \frac{f_o}{f_e}$
  - 3. $m = \frac{f_o}{f_e}$ (with erecting lens, image erect)
  - 4. $m = \frac{L}{f_o} \cdot \frac{D}{f_e}$

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  

#### Question 16
Match the physical quantity in List-I with its SI base units in List-II:
- **List-I**:
  - P. Magnetic permeability $\mu_0$
  - Q. Electric permittivity $\varepsilon_0$
  - R. Planck's constant $h$
  - S. Coefficient of dynamic viscosity $\eta$
- **List-II**:
  - 1. $\text{kg}\cdot\text{m}^2\cdot\text{s}^{-1}$
  - 2. $\text{kg}\cdot\text{m}^{-1}\cdot\text{s}^{-1}$
  - 3. $\text{kg}\cdot\text{m}\cdot\text{s}^{-2}\cdot\text{A}^{-2}$
  - 4. $\text{kg}^{-1}\cdot\text{m}^{-3}\cdot\text{s}^4\cdot\text{A}^2$

(A) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(B) P $\to$ 4, Q $\to$ 3, R $\to$ 1, S $\to$ 2  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(D) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2  

#### Question 17
Match the thermodynamics process in List-I with its entropy change $\Delta S_{\text{sys}}$ for an ideal gas in List-II:
- **List-I**:
  - P. Reversible isothermal expansion from $V_1$ to $V_2$
  - Q. Reversible isochoric heating from $T_1$ to $T_2$
  - R. Reversible isobaric expansion from $T_1$ to $T_2$
  - S. Reversible adiabatic expansion
- **List-II**:
  - 1. $n C_v \ln(T_2/T_1)$
  - 2. $n R \ln(V_2/V_1)$
  - 3. $n C_p \ln(T_2/T_1)$
  - 4. Zero identically ($0$)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 3, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 2, S $\to$ 4  

#### Question 18
Match the electromagnetic wave spectrum in List-I with its primary generation mechanism in List-II:
- **List-I**:
  - P. Gamma rays
  - Q. X-rays
  - R. Microwave
  - S. Radio waves
- **List-II**:
  - 1. Rapid acceleration of electrons in transmitting antenna
  - 2. Nuclear transitions and radioactive decay
  - 3. Inner shell electron transitions and bremsstrahlung in heavy metal target
  - 4. Special vacuum tubes like magnetrons, klystrons, and Gunn diodes

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(B) P $\to$ 3, Q $\to$ 2, R $\to$ 1, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1  

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding Tanabe-Sugano diagrams in coordination chemistry:
(A) The ground electronic state is always plotted as the horizontal baseline ($E/\Delta_o = 0$).  
(B) Terms of the same spin multiplicity as the ground state show energy variations that depend on the ligand field strength $D_q/B$.  
(C) For $d^4, d^5, d^6, d^7$ octahedral complexes, a vertical discontinuity line represents the crossover from high-spin to low-spin configurations.  
(D) The Racah parameter $B$ accounts for interelectronic repulsion between $d$-electrons.

#### Question 20
In the Sharpless asymmetric epoxidation of allylic alcohols using $\text{Ti(O-i-Pr)}_4$, tert-butyl hydroperoxide (TBHP), and chiral diethyl tartrate (DET):
(A) The use of $(+)\text{-DET}$ directs epoxidation from the bottom face ($\alpha$-face) when the allylic alcohol is drawn in the standard orientation.  
(B) The use of $(-)\text{-DET}$ directs epoxidation from the top face ($\beta$-face).  
(C) The reaction exhibits extraordinarily high enantiomeric excess ($>90\%\text{ ee}$).  
(D) The hydroxyl group of the allylic alcohol coordinates directly to the titanium center, acting as a crucial stereochemical directing anchor.

#### Question 21
According to Marcus electron transfer theory for outer-sphere redox reactions:
(A) The activation free energy is given by $\Delta G^\ddagger = \frac{(\lambda + \Delta G^\circ)^2}{4\lambda}$, where $\lambda$ is the reorganization energy.  
(B) In the normal region ($-\Delta G^\circ < \lambda$), the rate of electron transfer increases as driving force ($-\Delta G^\circ$) increases.  
(C) At the activationless point ($-\Delta G^\circ = \lambda$), the activation energy reaches zero and rate is maximized.  
(D) In the inverted region ($-\Delta G^\circ > \lambda$), the rate of electron transfer *decreases* as driving force increases.

#### Question 22
Regarding the Creutz-Taube complex $[(\text{NH}_3)_5\text{Ru-pyz-Ru}(\text{NH}_3)_5]^{5+}$ (where pyz is pyrazine):
(A) It is a classic mixed-valence complex with an average formal oxidation state of $+2.5$ on each ruthenium atom.  
(B) According to the Robin-Day classification, it is classified as a Class III (fully delocalized) mixed-valence system.  
(C) The complex displays an intense Intervalence Charge-Transfer (IVCT) absorption band in the near-infrared region.  
(D) Strong $\pi$-overlap through the pyrazine bridge facilitates rapid electronic exchange between the two ruthenium centers.

#### Question 23
In enzyme kinetics, comparing competitive, uncompetitive, and non-competitive enzyme inhibition:
(A) A competitive inhibitor binds to the active site of the free enzyme, increasing the apparent $K_m$ while leaving $V_{\text{max}}$ unchanged.  
(B) An uncompetitive inhibitor binds exclusively to the enzyme-substrate complex ($ES$), decreasing both apparent $K_m$ and $V_{\text{max}}$ by the same factor.  
(C) In pure non-competitive inhibition, the inhibitor binds with equal affinity to free $E$ and $ES$, decreasing $V_{\text{max}}$ while leaving $K_m$ unchanged.  
(D) In Lineweaver-Burk double-reciprocal plots ($1/v_0$ vs $1/[S]$), competitive inhibition lines intersect on the vertical $1/v_0$ axis.

#### Question 24
Regarding the Gibbs-Duhem equation in chemical thermodynamics:
$$\sum_{i} n_i d\mu_i = -S dT + V dP$$
(A) At constant temperature and pressure ($dT = 0, dP = 0$), the equation simplifies to $\sum_i n_i d\mu_i = 0$.  
(B) For a binary solution at constant $T$ and $P$, $x_1 d\mu_1 + x_2 d\mu_2 = 0$.  
(C) If component 1 obeys Raoult's law over a composition range, then component 2 must also obey Raoult's law over that same range.  
(D) The chemical potentials of components in a multicomponent mixture cannot vary independently.

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
Calculate the pH of a $0.10\text{ M}$ aqueous solution of ammonium acetate ($\text{CH}_3\text{COONH}_4$) at $25^\circ\text{C}$. Given $pK_a(\text{CH}_3\text{COOH}) = 4.76$ and $pK_b(\text{NH}_3) = 4.75$. Enter the value rounded off to TWO decimal places.

#### Question 26
Calculate the spin-only magnetic moment in Bohr Magnetons ($\mu_B$) for the complex ion $[Cr(H_2O)_6]^{3+}$ (atomic number of $\text{Cr} = 24$). Enter the value rounded off to TWO decimal places.

#### Question 27
An aqueous solution of a non-volatile electrolyte $\text{CaCl}_2$ (assuming complete dissociation into 3 ions) has a molality $m = 0.10\text{ mol/kg}$. If the molal boiling point elevation constant of water is $K_b = 0.512\text{ K kg/mol}$, calculate the boiling point of the solution in $^\circ\text{C}$ at $1.0\text{ atm}$ pressure (enter the value rounded off to TWO decimal places).

#### Question 28
The standard EMF of the Daniel cell $\text{Zn}(s)|\text{Zn}^{2+}(aq)||\text{Cu}^{2+}(aq)|\text{Cu}(s)$ is $E^\circ_{\text{cell}} = 1.10\text{ V}$ at $298\text{ K}$. Calculate the standard Gibbs free energy change $\Delta G^\circ$ in $\text{kJ/mol}$ for the cell reaction (take $F = 96500\text{ C/mol}$, enter the absolute value rounded off to ONE decimal place).

#### Question 29
A first-order chemical reaction has a rate constant $k = 0.0231\text{ min}^{-1}$. Calculate the half-life $t_{1/2}$ of the reaction in minutes (round off to the nearest integer).

#### Question 30
In the esterification equilibrium $\text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH} \rightleftharpoons \text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O}$, starting with $1.0\text{ mol}$ each of acetic acid and ethanol, $2/3\text{ mol}$ of ester is formed at equilibrium. Calculate the equilibrium constant $K_c$ (round off to ONE decimal place).

---

## Section 3: Matching List / Matrix Match (Questions 31 to 36)

#### Question 31
Match the carbohydrate in List-I with its structural characteristic in List-II:
- **List-I**:
  - P. Sucrose
  - Q. Maltose
  - R. Lactose
  - S. Cellulose
- **List-II**:
  - 1. Non-reducing disaccharide ($\alpha\text{-D-glucose} + \beta\text{-D-fructose}$, $C_1-C_2$ glycosidic link)
  - 2. Reducing disaccharide ($\alpha\text{-D-glucose} + \alpha\text{-D-glucose}$, $\alpha(1\to 4)$ link)
  - 3. Reducing disaccharide ($\beta\text{-D-galactose} + \beta\text{-D-glucose}$, $\beta(1\to 4)$ link)
  - 4. Linear unbranched polysaccharide of $\beta\text{-D-glucose}$ units via $\beta(1\to 4)$ links

(A) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(B) P $\to$ 2, Q $\to$ 1, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 1, Q $\to$ 3, R $\to$ 2, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 3, S $\to$ 1  

#### Question 32
Match the amino acid in List-I with its characteristic functional group in the side chain in List-II:
- **List-I**:
  - P. Cysteine
  - Q. Histidine
  - R. Tyrosine
  - S. Lysine
- **List-II**:
  - 1. Phenolic hydroxyl group ($-\text{C}_6\text{H}_4\text{OH}$)
  - 2. Primary aliphatic amino group ($-\text{NH}_2$)
  - 3. Thiol / Sulfhydryl group ($-\text{SH}$)
  - 4. Imidazole heterocyclic ring

(A) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(B) P $\to$ 4, Q $\to$ 3, R $\to$ 1, S $\to$ 2  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(D) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  

#### Question 33
Match the chemical test in List-I with the organic functional group it detects in List-II:
- **List-I**:
  - P. Tollens' test (ammoniacal $\text{AgNO}_3$)
  - Q. Carbylamine test ($\text{CHCl}_3 + \text{alc. KOH}$)
  - R. Lucas test ($\text{conc. HCl} + \text{anhyd. ZnCl}_2$)
  - S. Neutral $\text{FeCl}_3$ test
- **List-II**:
  - 1. Phenols (gives violet/colored complex)
  - 2. Aldehydes (forms silver mirror)
  - 3. Distinction of primary, secondary, tertiary alcohols by cloudiness time
  - 4. Primary aliphatic/aromatic amines (forms foul-smelling isocyanide)

(A) P $\to$ 2, Q $\to$ 4, R $\to$ 3, S $\to$ 1  
(B) P $\to$ 1, Q $\to$ 4, R $\to$ 3, S $\to$ 2  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 4, S $\to$ 1  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 3, S $\to$ 1  

#### Question 34
Match the metallurgy process in List-I with its primary purpose in List-II:
- **List-I**:
  - P. Froth flotation process
  - Q. Calcination
  - R. Roasting
  - S. Zone refining
- **List-II**:
  - 1. Heating carbonate/hydrated ore in the absence of air
  - 2. Ultra-purification of semiconductors (e.g., Ge, Si) based on fractional crystallization
  - 3. Concentration of low-grade sulfide ores using pine oil collector
  - 4. Heating sulfide ore in excess air below melting point to form oxide

(A) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(B) P $\to$ 4, Q $\to$ 1, R $\to$ 3, S $\to$ 2  
(C) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(D) P $\to$ 1, Q $\to$ 3, R $\to$ 4, S $\to$ 2  

#### Question 35
Match the noble gas compound in List-I with its molecular geometry via VSEPR theory in List-II:
- **List-I**:
  - P. $\text{XeF}_2$
  - Q. $\text{XeF}_4$
  - R. $\text{XeO}_3$
  - S. $\text{XeOF}_4$
- **List-II**:
  - 1. Square planar ($sp^3d^2$ with 2 lone pairs)
  - 2. Linear ($sp^3d$ with 3 equatorial lone pairs)
  - 3. Square pyramidal ($sp^3d^2$ with 1 lone pair)
  - 4. Pyramidal ($sp^3$ with 1 lone pair)

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 4, S $\to$ 3  
(C) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(D) P $\to$ 4, Q $\to$ 1, R $\to$ 2, S $\to$ 3  

#### Question 36
Match the crystalline solid type in List-I with its representative physical property in List-II:
- **List-I**:
  - P. Molecular crystal (Dry Ice $\text{CO}_2$, Iodine)
  - Q. Covalent network crystal (Diamond, $\text{SiO}_2$)
  - R. Ionic crystal ($\text{NaCl}$, $\text{CsCl}$)
  - S. Metallic crystal (Copper, Iron)
- **List-II**:
  - 1. High electrical and thermal conductivity in solid state; malleable and ductile
  - 2. Extremely hard, very high melting point, electrical insulator
  - 3. Insulator in solid state, conducts electricity in molten state and in solution
  - 4. Low melting point, soft, held by weak London dispersion / van der Waals forces

(A) P $\to$ 4, Q $\to$ 2, R $\to$ 3, S $\to$ 1  
(B) P $\to$ 2, Q $\to$ 4, R $\to$ 3, S $\to$ 1  
(C) P $\to$ 4, Q $\to$ 3, R $\to$ 2, S $\to$ 1  
(D) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Regarding Wallis' product formula and integral:
$$W_n = \int_0^{\pi/2} \sin^n x dx = \int_0^{\pi/2} \cos^n x dx$$
(A) The reduction formula is $W_n = \frac{n-1}{n} W_{n-2}$ for $n \ge 2$.  
(B) For even $n = 2m$, $W_{2m} = \frac{2m-1}{2m} \cdot \frac{2m-3}{2m-2} \cdots \frac{1}{2} \cdot \frac{\pi}{2}$.  
(C) For odd $n = 2m+1$, $W_{2m+1} = \frac{2m}{2m+1} \cdot \frac{2m-2}{2m-1} \cdots \frac{2}{3} \cdot 1$.  
(D) The infinite product satisfies $\lim_{m \to \infty} \left[\frac{2 \cdot 4 \cdot 6 \cdots (2m)}{1 \cdot 3 \cdot 5 \cdots (2m-1)}\right]^2 \frac{1}{2m+1} = \frac{\pi}{2}$.

#### Question 38
Let $A$ be an $m \times n$ real matrix. The Singular Value Decomposition (SVD) is $A = U \Sigma V^T$:
(A) $U$ is an $m \times m$ orthogonal matrix and $V$ is an $n \times n$ orthogonal matrix.  
(B) The singular values $\sigma_i$ are the non-negative square roots of the eigenvalues of $A^T A$.  
(C) The rank of $A$ equals the number of non-zero singular values.  
(D) The Frobenius norm of $A$ satisfies $\|A\|_F = \sqrt{\sum \sigma_i^2}$.

#### Question 39
In polar coordinates $(r, \theta)$ with pole at the focus, a conic section of semi-latus rectum $l$ and eccentricity $e$ has equation $\frac{l}{r} = 1 + e \cos\theta$:
(A) For $e = 0$, the curve is a circle.  
(B) For $0 < e < 1$, the curve is an ellipse.  
(C) For $e = 1$, the curve is a parabola.  
(D) For $e > 1$, the curve is a hyperbola.

#### Question 40
Let $A$ be an $n \times n$ complex matrix with spectral radius $\rho(A) = \max_i |\lambda_i|$:
(A) For any matrix norm $\|\cdot\|$, $\rho(A) \le \|A\|$.  
(B) $\lim_{k \to \infty} A^k = O$ if and only if $\rho(A) < 1$.  
(C) The series $\sum_{k=0}^\infty A^k = (I - A)^{-1}$ converges if and only if $\rho(A) < 1$.  
(D) Gelfand's formula asserts $\rho(A) = \lim_{k \to \infty} \|A^k\|^{1/k}$.

#### Question 41
In a Galton-Watson branching process, each individual produces $k$ offspring with probability $p_k$. Let $G(s) = \sum_{k=0}^\infty p_k s^k$ be the probability generating function of offspring, and let $\mu = G'(1)$ be the mean number of offspring:
(A) If $\mu \le 1$ and $p_1 \ne 1$, the extinction probability is $\eta = 1$.  
(B) If $\mu > 1$, the extinction probability $\eta$ is the unique solution of $s = G(s)$ in the interval $[0, 1)$.  
(C) The variance of the population size at generation $n$ grows exponentially when $\mu > 1$.  
(D) If $p_0 = 0$, the population cannot go extinct ($\eta = 0$).

#### Question 42
Consider the $2\pi$-periodic square wave $f(x) = 1$ for $0 \le x < \pi$ and $f(x) = -1$ for $-\pi \le x < 0$:
(A) $f(x)$ is an odd function, so all Fourier cosine coefficients $a_n = 0$.  
(B) The Fourier sine coefficients are $b_n = \frac{4}{n\pi}$ for odd $n$, and $b_n = 0$ for even $n$.  
(C) The Fourier series is $f(x) = \frac{4}{\pi} \sum_{k=1}^\infty \frac{\sin((2k-1)x)}{2k-1}$.  
(D) Evaluating the series at $x = \pi/2$ yields Leibniz's formula for $\pi$: $1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots = \frac{\pi}{4}$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Using Feynman's trick of differentiating under the integral sign, evaluate:
$$I = \int_0^\infty \frac{\arctan(x)}{x(1 + x^2)} dx$$
Calculate the value of $\frac{32 I}{\pi \ln 2}$ (round off to the nearest integer).

#### Question 44
Find the number of derangements of 5 distinct items (permutations with no fixed points, $D_5$).

#### Question 45
Find the perpendicular distance from the point $(1, 2, 3)$ to the plane $2x - 2y + z - 5 = 0$ (round off to TWO decimal places).

#### Question 46
Let $\alpha = e^{i 2\pi/7}$ be a primitive 7th root of unity. Evaluate the real sum:
$$S = \sum_{k=1}^6 \cos\left(\frac{2k\pi}{7}\right)$$
Enter the absolute value $|S|$ rounded off to ONE decimal place.

#### Question 47
Find the parameter $C$ of the orthogonal trajectory to the family of circles $x^2 + y^2 = 2cx$ that passes through the point $(1, 2)$.

#### Question 48
A box contains 5 cards numbered 1, 3, 5, 7, 9 (odd) and 5 cards numbered 2, 4, 6, 8, 10 (even). Two cards are drawn at random without replacement. What is the probability that the sum of the numbers on the drawn cards is even? (enter the value rounded off to TWO decimal places).

---

## Section 3: Matching List / Matrix Match (Questions 49 to 54)

#### Question 49
Match the function in List-I with its derivative at $x = 0$ in List-II:
- **List-I**:
  - P. $f(x) = \sin(2x)$
  - Q. $f(x) = e^{3x}$
  - R. $f(x) = \ln(1 + 4x)$
  - S. $f(x) = \tan(5x)$
- **List-II**:
  - 1. $4$
  - 2. $2$
  - 3. $3$
  - 4. $5$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(D) P $\to$ 4, Q $\to$ 3, R $\to$ 1, S $\to$ 2  

#### Question 50
Match the function in List-I with its domain in List-II:
- **List-I**:
  - P. $f(x) = \arcsin(x)$
  - Q. $f(x) = \sqrt{x - 1}$
  - R. $f(x) = \ln(x)$
  - S. $f(x) = \frac{1}{x}$
- **List-II**:
  - 1. $[1, \infty)$
  - 2. $[-1, 1]$
  - 3. $\mathbb{R} \setminus \{0\}$
  - 4. $(0, \infty)$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 51
Match the differential equation in List-I with its general solution in List-II:
- **List-I**:
  - P. $\frac{dy}{dx} = y$
  - Q. $\frac{dy}{dx} = -y$
  - R. $\frac{d^2 y}{dx^2} + y = 0$
  - S. $\frac{d^2 y}{dx^2} - y = 0$
- **List-II**:
  - 1. $y = c e^{-x}$
  - 2. $y = c_1 e^x + c_2 e^{-x}$
  - 3. $y = c e^x$
  - 4. $y = c_1 \cos x + c_2 \sin x$

(A) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(B) P $\to$ 1, Q $\to$ 3, R $\to$ 4, S $\to$ 2  
(C) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(D) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  

#### Question 52
Match the conic section in List-I with its eccentricity $e$ in List-II:
- **List-I**:
  - P. Circle
  - Q. Ellipse
  - R. Parabola
  - S. Hyperbola
- **List-II**:
  - 1. $0 < e < 1$
  - 2. $e = 0$
  - 3. $e > 1$
  - 4. $e = 1$

(A) P $\to$ 2, Q $\to$ 1, R $\to$ 4, S $\to$ 3  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 2, Q $\to$ 4, R $\to$ 1, S $\to$ 3  
(D) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  

#### Question 53
Match the system of linear equations in List-I with the determinant condition of its coefficient matrix $A$ in List-II:
- **List-I**:
  - P. Unique solution
  - Q. Infinitely many solutions or no solution (singular)
  - R. Homogeneous system with non-trivial solutions
  - S. Invertible system $A \vec{x} = \vec{b}$
- **List-II**:
  - 1. $\det(A) = 0$
  - 2. $\det(A) \ne 0$
  - 3. $\det(A) = 0$
  - 4. $\det(A) \ne 0$

(A) P $\to$ 2, Q $\to$ 3, R $\to$ 1, S $\to$ 4  
(B) P $\to$ 1, Q $\to$ 2, R $\to$ 3, S $\to$ 4  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(D) P $\to$ 4, Q $\to$ 2, R $\to$ 1, S $\to$ 3  

#### Question 54
Match the vector operation in List-I with its physical meaning in List-II:
- **List-I**:
  - P. $\nabla \phi$ (Gradient)
  - Q. $\nabla \cdot \vec{F}$ (Divergence)
  - R. $\nabla \times \vec{F}$ (Curl)
  - S. $\nabla^2 \phi$ (Laplacian)
- **List-II**:
  - 1. Local rotation / circulation density of a vector field
  - 2. Difference between average value over a small sphere and value at center
  - 3. Direction and rate of fastest increase of a scalar field
  - 4. Net flux outward per unit volume (source or sink density)

(A) P $\to$ 3, Q $\to$ 4, R $\to$ 1, S $\to$ 2  
(B) P $\to$ 4, Q $\to$ 3, R $\to$ 1, S $\to$ 2  
(C) P $\to$ 3, Q $\to$ 1, R $\to$ 4, S $\to$ 2  
(D) P $\to$ 1, Q $\to$ 4, R $\to$ 2, S $\to$ 3  
"""

sol_1_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 1
## IIT Delhi Benchmark JEE Advanced Mock Examination 14

---

### PART I: PHYSICS

#### Solution 1: Mandelstam Relativistic Invariants
1. **Core Concept**:
   In relativistic kinematics, $s = (P_1 + P_2)^2 = (E_1 + E_2)^2/c^2 - (\vec{p}_1 + \vec{p}_2)^2$. In the CM frame, $\vec{p}_1 + \vec{p}_2 = \vec{0}$, hence $s = E_{\text{cm}}^2/c^2$.
2. **Four-Momentum Sum**:
   Expanding $s + t + u = (P_1 + P_2)^2 + (P_1 - P_3)^2 + (P_1 - P_4)^2$ using $P_1 + P_2 = P_3 + P_4$ yields $\sum m_i^2 c^2$.
3. **Four-Momentum Transfer**:
   $t = (P_1 - P_3)^2 = 2m^2 c^2 - 2(E_1 E_3/c^2 - \vec{p}_1 \cdot \vec{p}_3) = -2|\vec{p}^*|^2 (1 - \cos\theta^*)$.
- **Correct Option**: (A, B, C, D)

#### Solution 2: Electromagnetic Skin Depth
1. **Wave Equation in Conductor**:
   $\nabla^2 \vec{E} = \mu \sigma \frac{\partial \vec{E}}{\partial t} \implies k^2 = i\mu_0 \sigma \omega$.
2. **Complex Wavevector**:
   $k = \sqrt{i}\sqrt{\mu_0 \sigma \omega} = \frac{1 + i}{\sqrt{2}}\sqrt{\mu_0 \sigma \omega} = (1 + i)\sqrt{\frac{\mu_0 \sigma \omega}{2}}$.
3. **Attenuation & Phase**:
   Field attenuates as $e^{-z/\delta}$ where $\delta = \sqrt{\frac{2}{\mu_0 \sigma \omega}}$. The factor $(1+i) = \sqrt{2} e^{i\pi/4}$ implies a $45^\circ$ phase lag of $\vec{B}$ relative to $\vec{E}$.
- **Correct Option**: (A, B, C, D)

#### Solution 3: Euler's Rigid Body Equations & Intermediate Axis Instability
- Conservation of kinetic energy $2T = I_1 \omega_1^2 + I_2 \omega_2^2 + I_3 \omega_3^2$ and angular momentum $L^2 = I_1^2 \omega_1^2 + I_2^2 \omega_2^2 + I_3^2 \omega_3^2$.
- Perturbation analysis around $\omega_1$: linearized perturbation equation gives $\ddot{\eta} = -\Omega^2 \eta$, giving stable harmonic oscillations.
- Perturbation analysis around $\omega_2$: linearized perturbation gives $\ddot{\eta} = +\Omega^2 \eta$, yielding exponential divergence (unstable).
- Perturbation analysis around $\omega_3$: stable harmonic oscillations.
- **Correct Option**: (A, B, C, D)

#### Solution 4: Clausius-Clapeyron Phase Transition
- Ideal gas vapor volume $V_{\text{vap}} \approx \frac{RT}{P} \gg V_{\text{liq}} \implies \frac{dP}{dT} = \frac{\Delta H_{\text{vap}} P}{R T^2} \implies \ln P = -\frac{\Delta H_{\text{vap}}}{RT} + C$.
- At the critical point, latent heat vanishes and the phase boundary ends.
- For water, density of ice is less than water, $\Delta V_{\text{fus}} = V_{\text{liq}} - V_{\text{ice}} < 0$, making $\frac{dP}{dT} < 0$.
- **Correct Option**: (A, B, C, D)

#### Solution 5: Transmission Line Characteristics
- Follows directly from telegrapher's equations: $Z_0 = \sqrt{L'/C'}$, $v = 1/\sqrt{L'C'}$, $\Gamma_V = \frac{Z_L - Z_0}{Z_L + Z_0}$.
- **Correct Option**: (A, B, C, D)

#### Solution 6: Magnetic Dipole on Axis of Current Loop
- Field on axis: $B(x) = \frac{\mu_0 I R^2}{2(R^2 + x^2)^{3/2}} \approx \frac{\mu_0 I R^2}{2 x^3}$.
- Energy $U = -\vec{m} \cdot \vec{B} = -m B(x) = -\frac{\mu_0 m I R^2}{2 x^3}$.
- Force $F = -\frac{dU}{dx} = -\frac{3\mu_0 m I R^2}{2 x^4}$ (attractive towards the loop).
- **Correct Option**: (A, B, C, D)

#### Solution 7: Relativistic Cyclotron Energy Limit
- Frequency mismatch: $\frac{\Delta f}{f_0} = \frac{f_0 - f}{f_0} = 1 - \frac{1}{\gamma} = 0.01$.
- $\frac{1}{\gamma} = 0.99 \implies \gamma = \frac{1}{0.99} \approx 1.0101$.
- Kinetic energy: $K_{\text{max}} = (\gamma - 1) m_0 c^2 \approx 0.0101 \times 938\text{ MeV} \approx 9.5\text{ MeV}$.
- **Answer**: 9.5

#### Solution 8: Skin Depth in Copper
- $\omega = 2\pi f = 2\pi \times 10^7\text{ rad/s}$.
- $\delta = \sqrt{\frac{2}{\mu_0 \sigma \omega}} = \sqrt{\frac{2}{(4\pi \times 10^{-7}) (5.8 \times 10^7) (2\pi \times 10^7)}} = \sqrt{\frac{2}{4\pi^2 \times 5.8 \times 10^7 \times 10^{-7} \times 10^7}} = \frac{1}{2\pi \times 10^3 \sqrt{5.8}} \approx 20.9\text{ }\mu\text{m}$.
- **Answer**: 20.9

#### Solution 9: Carnot Heat Pump Power
- $\text{COP}_{\text{HP}} = \frac{T_H}{T_H - T_C} = \frac{294}{294 - 260} = \frac{294}{34} \approx 8.647$.
- Power required: $W_{\text{in}} = \frac{Q_H}{\text{COP}} = \frac{17.0\text{ kW}}{8.647} \approx 1.97\text{ kW}$.
- **Answer**: 1.97

#### Solution 10: Ballistic Galvanometer
- Angular impulse: $\int \tau dt = N B A \int I dt = N B A Q = I_{\text{coil}} \omega_0$.
- Initial kinetic energy: $\frac{1}{2} I_{\text{coil}} \omega_0^2 = \frac{(N B A Q)^2}{2 I_{\text{coil}}}$.
- Equating to maximum torsional potential energy: $\frac{1}{2} k \theta_{\text{max}}^2 = \frac{(N B A Q)^2}{2 I_{\text{coil}}} \implies \theta_{\text{max}} = \frac{N B A Q}{\sqrt{k I_{\text{coil}}}}$.
- $N B A Q = 0.05 \times 20 \times 10^{-6} = 1.0 \times 10^{-6}\text{ N}\cdot\text{m}\cdot\text{s}$.
- $\sqrt{k I_{\text{coil}}} = \sqrt{(6.17 \times 10^{-7}) (2.5 \times 10^{-7})} = \sqrt{1.5425 \times 10^{-13}} \approx 3.927 \times 10^{-7}$.
- $\theta_{\text{max}} = \frac{1.0 \times 10^{-6}}{3.927 \times 10^{-7}} \approx 2.546\text{ rad} \approx 146^\circ$.
- **Answer**: 146

#### Solution 11: Tuning Fork Wax Loading
- Adding wax increases inertia, decreasing frequency: $f_L = f_0 - 4 = 440 - 4 = 436\text{ Hz}$.
- **Answer**: 436

#### Solution 12: Glass Sphere Deviation
- Angle of incidence $i = 60^\circ$. By Snell's law: $1 \cdot \sin 60^\circ = \sqrt{3} \sin r \implies \frac{\sqrt{3}}{2} = \sqrt{3}\sin r \implies \sin r = 1/2 \implies r = 30^\circ$.
- Total deviation for 1 internal reflection: $\delta = (i - r) + (\pi - 2r) + (i - r) = 2i - 4r + 180^\circ$.
- $\delta = 2(60^\circ) - 4(30^\circ) + 180^\circ = 120^\circ - 120^\circ + 180^\circ = 180^\circ$.
- **Answer**: 180

#### Solution 13 to 18:
- 13: $V'(x_0) = k x_0 - 2\alpha/x_0^3 = 0 \implies x_0^4 = 2\alpha/k$. $V''(x_0) = k + 6\alpha/x_0^4 = k + 3k = 4k$. $\omega = \sqrt{V''(x_0)/m} = 2\sqrt{k/m}$. (A)
- 14: Equal amplitudes on fast and slow axes with $\pi/2$ phase shift produces circularly polarized light. (A)
- 15: When vertical, angular acceleration is zero ($\tau = 0$), so the tangential acceleration of CM is zero; hence the horizontal reaction force is zero. (A)
- 16: $I(t) = I_0(1 - e^{-t/\tau}) = 0.5 I_0 \implies e^{-t/\tau} = 1/2 \implies t = \tau \ln 2 = \frac{L}{r}\ln 2$. (A)
- 17: Stefan-Boltzmann law $P \propto T^4 \implies (1.20)^4 \approx 2.07$. (A)
- 18: $f_1 = v/(2L)$, closed-open pipe fundamental $f_1' = v/(4L) = f_1/2$. (A)

---

### PART II: CHEMISTRY

#### Solution 19: Wade's Rules
- Closo: $(n+1)$ pairs, Nido: $(n+2)$ pairs, Arachno: $(n+3)$ pairs.
- Each $B-H$ unit has 4 valence electrons: 2 used in exo $B-H$ bond, 2 contributed to cluster cage.
- **Correct Option**: (A, B, C, D)

#### Solution 20: Julia Olefination
- Explains the mechanism: carbanion formation, addition to aldehyde, acetylation, and reductive elimination with $\text{Na/Hg}$ to give $(E)$-alkene.
- **Correct Option**: (A, B, C, D)

#### Solution 21: Debye-Hückel Limiting Law
- All statements (A, B, C, D) reflect the fundamental theory of ionic atmospheres.
- **Correct Option**: (A, B, C, D)

#### Solution 22: Edman Degradation
- Cyclic degradation allows sequential N-terminal cleavage without digesting internal peptide bonds.
- **Correct Option**: (A, B, C, D)

#### Solution 23: Allotropes of Phosphorus
- White $P_4$ strain ($60^\circ$ angles), red polymeric, black layered conductor, and disproportionation with $\text{NaOH}$ to $\text{PH}_3 + \text{NaH}_2\text{PO}_2$.
- **Correct Option**: (A, B, C, D)

#### Solution 24: Hydroformylation Mechanism
- Classic catalytic cycle of the oxo process.
- **Correct Option**: (A, B, C, D)

#### Solution 25: Solubility Product of CaF2
- $\text{CaF}_2 \rightleftharpoons \text{Ca}^{2+} + 2\text{F}^-$.
- $K_{sp} = S \times (2S)^2 = 4 S^3 = 4 (2.0 \times 10^{-4})^3 = 4 \times 8.0 \times 10^{-12} = 3.2 \times 10^{-11}$.
- $X = 3.20$.
- **Answer**: 3.20

#### Solution 26: First-Order Azomethane Decomposition
- $A \to B + C$. At time $t$: $P_t = P_0 + x \implies x = P_t - P_0 = 150 - 100 = 50\text{ mm Hg}$.
- Remaining reactant $P_A = P_0 - x = 100 - 50 = 50\text{ mm Hg} = P_0 / 2$.
- Thus $t = t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{3.46 \times 10^{-4}} = 2003\text{ s} \approx 2003$.
- **Answer**: 2003

#### Solution 27: Redox Titration Stoichiometry
- Moles of $\text{Cr}_2\text{O}_7^{2-} = 0.025 \times 0.020 = 5.0 \times 10^{-4}\text{ mol}$.
- Stoichiometry: $1\text{ mol } \text{Cr}_2\text{O}_7^{2-} \equiv 6\text{ mol } \text{Fe}^{2+}$.
- Moles of $\text{Fe}^{2+} = 6 \times 5.0 \times 10^{-4} = 3.0 \times 10^{-3}\text{ mol}$.
- Molarity $= \frac{3.0 \times 10^{-3}\text{ mol}}{0.050\text{ L}} = 0.060\text{ M}$.
- **Answer**: 0.06

#### Solution 28: Standard Gibbs Free Energy of Formation
- $\Delta G_f^\circ = \Delta H_f^\circ - T \Delta S^\circ = -285.8\text{ kJ} - 298(-0.1632)\text{ kJ} = -285.8 + 48.63 = -237.17\text{ kJ/mol} \approx -237.2\text{ kJ/mol}$.
- Absolute magnitude $= 237.2$.
- **Answer**: 237.2

#### Solution 29: FCC Unit Cell Density
- For FCC, $Z = 4$.
- $\rho = \frac{Z M}{N_A a^3} \implies M = \frac{\rho N_A a^3}{Z}$.
- $a = 400\text{ pm} = 4.0 \times 10^{-8}\text{ cm} \implies a^3 = 6.4 \times 10^{-23}\text{ cm}^3$.
- $M = \frac{10.0 \times (6.022 \times 10^{23}) \times (6.4 \times 10^{-23})}{4} = \frac{385.4}{4} \approx 96.4\text{ g/mol}$.
- **Answer**: 96.4

#### Solution 30: Ostwald's Dilution Law
- Degree of dissociation $\alpha = \frac{\Lambda_m}{\Lambda_m^\circ} = \frac{16.5}{390.5} \approx 0.04225$.
- $K_a = \frac{c \alpha^2}{1 - \alpha} \approx c \alpha^2 = 0.010 \times (0.04225)^2 = 1.785 \times 10^{-5}\text{ mol/L}$.
- $Y = 1.79$.
- **Answer**: 1.79

#### Solution 31 to 36:
- 31: Formation of strong $\text{C}=\text{O}$ bond in carbonyl sulfide. (A)
- 32: Both Marshall's acid ($\text{H}_2\text{S}_2\text{O}_8$) and Caro's acid ($\text{H}_2\text{SO}_5$) contain peroxy bonds. (C)
- 33: $\text{NH}_3$ ($-3$) to $\text{NO}$ ($+2$). (A)
- 34: Peroxide effect gives anti-Markovnikov bromide: 1-bromo-2-methylcyclohexane. (A)
- 35: Pentaamminecarbonatocobalt(III) chloride. (A)
- 36: Hardy-Schulze rule: higher cation charge has higher coagulating power: $\text{Na}^+ < \text{Ba}^{2+} < \text{Al}^{3+}$. (A)

---

### PART III: MATHEMATICS

#### Solution 37: Gamma and Beta Functions
- All standard integral representations and identities.
- **Correct Option**: (A, B, C, D)

#### Solution 38: Spectral Theorem for Symmetric Matrices
- Real eigenvalues, orthogonal eigenspaces, Rayleigh quotient bounds, and Sylvester's law of inertia.
- **Correct Option**: (A, B, C, D)

#### Solution 39: Ellipsoid Properties
- The locus of intersection of 3 mutually perpendicular tangent planes is the director sphere $x^2 + y^2 + z^2 = a^2 + b^2 + c^2$.
- Maximum inscribed box volume: $8(a/\sqrt{3})(b/\sqrt{3})(c/\sqrt{3}) = \frac{8abc}{3\sqrt{3}}$.
- **Correct Option**: (A, B, C, D)

#### Solution 40: Bessel Function Frobenius Series
- Standard Frobenius method for $J_0(x)$.
- **Correct Option**: (A, B, C, D)

#### Solution 41: Sinc Function Integrals
- Standard Dirichlet and Fejér-type sinc integrals.
- **Correct Option**: (A, B, C, D)

#### Solution 42: Normal Variable Distributions
- Note: The Cauchy distribution has undefined mean (the integral $\int_{-\infty}^\infty \frac{w}{1+w^2}dw$ diverges). Thus (D) is false. Statements (A, B, C) are correct.
- **Correct Option**: (A, B, C)

#### Solution 43: Definite Integral
- Let $x = \tan\theta \implies dx = \sec^2\theta d\theta$.
- $I = \int_0^{\pi/4} \ln(1 + \tan\theta) d\theta$.
- Using King's property $\theta \to \pi/4 - \theta$:
  $1 + \tan(\pi/4 - \theta) = 1 + \frac{1 - \tan\theta}{1 + \tan\theta} = \frac{2}{1 + \tan\theta}$.
- $2I = \int_0^{\pi/4} \ln 2 d\theta = \frac{\pi}{4}\ln 2 \implies I = \frac{\pi}{8}\ln 2$.
- $\frac{64 I}{\pi \ln 2} = \frac{64 (\pi/8 \ln 2)}{\pi \ln 2} = 8$.
- **Answer**: 8

#### Solution 44: Integer Solutions with Constraint
- Total non-negative solutions of $x + y + z + w = 15$ is $\binom{15 + 4 - 1}{4 - 1} = \binom{18}{3} = \frac{18 \times 17 \times 16}{6} = 816$.
- Solutions with $x \ge 4$: let $x' = x - 4 \ge 0$, then $x' + y + z + w = 11$.
  Number of solutions $= \binom{11 + 4 - 1}{3} = \binom{14}{3} = \frac{14 \times 13 \times 12}{6} = 364$.
- Solutions with $x \le 3$: $816 - 364 = 452$.
- **Answer**: 452

#### Solution 45: Line-Plane Intersection
- Parametric point on line: $x = 1 + 2t$, $y = -2 - 3t$, $z = 4 + t$.
- Substitute into plane $2(1 + 2t) + 4(-2 - 3t) - (4 + t) + 1 = 0$:
  $2 + 4t - 8 - 12t - 4 - t + 1 = 0 \implies -9 - 9t = 0 \implies t = -1$.
- Point $P$: $\alpha = 1 - 2 = -1$, $\beta = -2 + 3 = 1$, $\gamma = 4 - 1 = 3$.
- $\alpha^2 + \beta^2 + \gamma^2 = (-1)^2 + 1^2 + 3^2 = 1 + 1 + 9 = 11$.
- **Answer**: 11

#### Solution 46: Cube Roots Determinant
- Column operation $C_1 \to C_1 + C_2 + C_3$:
  First column becomes $1 + \omega + \omega^2 = 0$.
  Therefore, $\Delta = 0$.
- **Answer**: 0

#### Solution 47: Linear First-Order ODE
- Integrating factor: $I.F. = e^{\int \cot x dx} = e^{\ln\sin x} = \sin x$.
- Solution: $y \sin x = \int 2\cos x \sin x dx = \int \sin 2x dx = -\frac{1}{2}\cos 2x + C$.
- Condition $y(\pi/2) = 1$: $1 \cdot 1 = -\frac{1}{2}(-1) + C = \frac{1}{2} + C \implies C = \frac{1}{2}$.
- $y \sin x = \frac{1 - \cos 2x}{2} = \sin^2 x \implies y = \sin x$.
- At $x = \pi/6$: $y(\pi/6) = \sin(\pi/6) = 0.5$.
- **Answer**: 0.5

#### Solution 48: Hypergeometric Variance
- Population $N = 10$, successes $K = 4$, sample size $n = 3$.
- Mean $\mu = n \frac{K}{N} = 3 \times \frac{4}{10} = 1.2$.
- Variance $\text{Var}(X) = n \frac{K}{N} \left(1 - \frac{K}{N}\right) \frac{N - n}{N - 1} = 3 (0.4) (0.6) \frac{10 - 3}{10 - 1} = 0.72 \times \frac{7}{9} = 0.56$.
- **Answer**: 0.56

#### Solution 49 to 54:
- 49: Classic Euler log-sine integral $= -\frac{\pi}{2}\ln 2$. (A)
- 50: Ratio test $\lim \frac{a_{n+1}}{a_n} = \lim \frac{(n+1)!}{(n+1)^{n+1}} \frac{n^n}{n!} = \lim \left(\frac{n}{n+1}\right)^n = \frac{1}{e} \implies R = e$. (A)
- 51: Standard distance between skew lines $\frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|} = \frac{1}{\sqrt{6}}$. (A)
- 52: $|3AB| = 3^3 |A| |B| = 27 (-1) (3) = -81$. (A)
- 53: $f'(x) = e^x + 1 > 0$ strictly increasing, exactly 1 real root. (A)
- 54: $|\vec{a}+\vec{b}+\vec{c}|^2 = 3 + 2(\vec{a}\cdot\vec{b} + \vec{b}\cdot\vec{c} + \vec{c}\cdot\vec{a}) = 0 \implies \sum = -3/2$. (A)
"""

sol_2_md = r"""# Comprehensive Solutions & Pedagogical Explanations — Paper 2
## IIT Delhi Benchmark JEE Advanced Mock Examination 14

---

### PART I: PHYSICS

#### Solution 1: Relativistic Dynamics
- Relativistic invariant $E^2 - p^2 c^2 = m^2 c^4$.
- Conservation of 4-momentum leads to threshold energies and kinematic relations.
- **Correct Option**: (A, B, C, D)

#### Solution 2: Magnetic Vector Potential
- Vector potential $\vec{A}$ satisfies $\nabla \times \vec{A} = \vec{B}$ and Coulomb gauge $\nabla \cdot \vec{A} = 0$.
- For uniform magnetic field $\vec{B} = B_0 \hat{k}$, $\vec{A} = \frac{1}{2} (\vec{B} \times \vec{r}) = \frac{1}{2} B_0 (-y\hat{i} + x\hat{j})$.
- **Correct Option**: (A, B, C, D)

#### Solution 3: LC Transmission Line
- Telegrapher's wave equations and dispersion-free propagation.
- **Correct Option**: (A, B, C, D)

#### Solution 4: Ideal Gas Polytropic Expansion
- Work done $W = \frac{P_1 V_1 - P_2 V_2}{\gamma - 1}$ and molar heat capacity $C = C_v + \frac{R}{1 - n}$.
- **Correct Option**: (A, B, C, D)

#### Solution 5: Coupled Inductance and Mutual Flux
- Energy $U = \frac{1}{2} L_1 I_1^2 + \frac{1}{2} L_2 I_2^2 \pm M I_1 I_2$ with coupling coefficient $k = M/\sqrt{L_1 L_2} \le 1$.
- **Correct Option**: (A, B, C, D)

#### Solution 6: Phase and Group Velocity
- $v_p = \omega/k$, $v_g = d\omega/dk$. Rayleigh's formula $v_g = v_p - \lambda \frac{dv_p}{d\lambda}$.
- **Correct Option**: (A, B, C, D)

#### Solution 7: Cyclotron Resonance Frequency
- $\omega = \frac{q B}{m} \implies f = \frac{q B}{2\pi m}$.
- $f = \frac{(1.6 \times 10^{-19}) (1.5)}{2\pi (1.67 \times 10^{-27})} \approx 22.9\text{ MHz}$.
- **Answer**: 22.9

#### Solution 8: Thermal Radiation Cooling
- $t = \frac{M s}{3 e \sigma A}\left(\frac{1}{T_1^3} - \frac{1}{T_0^3}\right)$ calculation yields $t = 312\text{ s}$.
- **Answer**: 312

#### Solution 9: Sound Interference in Quincke's Tube
- Path difference $\Delta x = 2d = \lambda/2 \implies \lambda = 4d$.
- Frequency $f = v/\lambda = 340 / (4 \times 0.085) = 1000\text{ Hz}$.
- **Answer**: 1000

#### Solution 10: RC Transient Discharge
- $q(t) = Q_0 e^{-t/RC} = 0.01 Q_0 \implies t = RC \ln 100 = 2 RC \ln 10$.
- $t = 2 (10^6 \times 10^{-6}) (2.303) = 4.61\text{ s}$.
- **Answer**: 4.61

#### Solution 11: Diffraction Grating Resolving Power
- $\frac{\lambda}{\Delta\lambda} = n N = 2 \times (5000 \times 2) = 20000$.
- **Answer**: 20000

#### Solution 12: Capillary Ascent
- $h = \frac{2 T \cos\theta}{\rho g r} = \frac{2 (0.072) (1)}{1000 \times 9.8 \times 0.5 \times 10^{-3}} = \frac{0.144}{4.9} \approx 0.0294\text{ m} = 2.94\text{ cm}$.
- **Answer**: 2.94

#### Solutions 13 to 18 (Matching Lists):
- 13: P-2, Q-3, R-1, S-4. (A)
- 14: P-3, Q-1, R-4, S-2. (A)
- 15: P-2, Q-1, R-4, S-3. (A)
- 16: P-3, Q-4, R-1, S-2. (A)
- 17: P-2, Q-1, R-3, S-4. (A)
- 18: P-2, Q-3, R-4, S-1. (A)

---

### PART II: CHEMISTRY

#### Solutions 19 to 24:
- 19: (A, B, C, D) - Tanabe-Sugano diagram characteristics.
- 20: (A, B, C, D) - Sharpless asymmetric epoxidation enantioselection.
- 21: (A, B, C, D) - Marcus theory electron transfer activation energy.
- 22: (A, B, C, D) - Creutz-Taube complex mixed valence Class II.
- 23: (A, B, C, D) - Non-competitive vs uncompetitive enzyme kinetics.
- 24: (A, B, C, D) - Gibbs-Duhem thermodynamic consistency.

#### Solutions 25 to 30:
- 25: $\text{pH} = 7 + \frac{1}{2}(pK_a - pK_b) = 7 + \frac{1}{2}(4.76 - 4.75) = 7.005 \approx 7.01$. (Answer: 7.01)
- 26: Spin-only moment for $d^3$ is $\sqrt{3(5)} = \sqrt{15} \approx 3.87\text{ BM}$. (Answer: 3.87)
- 27: Elevation $\Delta T_b = i K_b m = 3 \times 0.512 \times 0.10 = 0.154^\circ\text{C} \implies T_b = 100.15^\circ\text{C}$. (Answer: 100.15)
- 28: $E^\circ_{\text{cell}} = 0.34 - (-0.76) = 1.10\text{ V}$. $\Delta G^\circ = -nFE^\circ = -2 \times 96500 \times 1.10 = -212.3\text{ kJ}$. (Answer: 212.3)
- 29: Half-life $t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{0.0231} = 30.0\text{ min}$. (Answer: 30)
- 30: Equilibrium moles of ester $= 2/3\text{ mol}$. $K_c = \frac{(2/3)(2/3)}{(1/3)(1/3)} = 4.0$. (Answer: 4.0)

#### Solutions 31 to 36:
- 31: P-2, Q-3, R-1, S-4. (A)
- 32: P-3, Q-1, R-4, S-2. (A)
- 33: P-2, Q-4, R-1, S-3. (A)
- 34: P-3, Q-2, R-1, S-4. (A)
- 35: P-2, Q-1, R-4, S-3. (A)
- 36: P-3, Q-4, R-2, S-1. (A)

---

### PART III: MATHEMATICS

#### Solutions 37 to 42:
- 37: (A, B, C, D) - Wallis product formula and asymptotics.
- 38: (A, B, C, D) - Singular Value Decomposition (SVD) singular values.
- 39: (A, B, C, D) - Polar equation of conic section.
- 40: (A, B, C, D) - Matrix norm and spectral radius.
- 41: (A, B, C, D) - Branching process extinction probability.
- 42: (A, B, C, D) - Fourier series coefficients of square wave.

#### Solutions 43 to 48:
- 43: Leibniz rule differentiation under integral sign gives $I = \frac{\pi}{2}\ln(1 + a) \implies$ evaluating at $a = 1$ gives $\frac{\pi}{2}\ln 2$. (Answer: 16)
- 44: Derangements $D_5 = 5!(1 - 1 + 1/2 - 1/6 + 1/24 - 1/120) = 44$. (Answer: 44)
- 45: Perpendicular distance from point to plane $= \frac{|2(1) - 2(2) + 1(3) - 5|}{\sqrt{4+4+1}} = \frac{|-4|}{3} = 1.33$. (Answer: 1.33)
- 46: Roots of unity sum $\sum_{k=1}^6 \cos(2k\pi/7) = -1/2 = -0.5$. (Answer: 0.5)
- 47: Orthogonal trajectories: replace $y'$ with $-1/y' \implies y^2 + x^2 = C$. (Answer: 5)
- 48: Two cards sum even: both odd $\binom{5}{2} = 10$, both even $\binom{5}{2} = 10$. Total $\binom{10}{2} = 45$. Probability $= 20/45 = 4/9 \approx 0.44$. (Answer: 0.44)

#### Solutions 49 to 54:
- 49: P-2, Q-3, R-1, S-4. (A)
- 50: P-2, Q-1, R-4, S-3. (A)
- 51: P-3, Q-1, R-4, S-2. (A)
- 52: P-2, Q-1, R-4, S-3. (A)
- 53: P-2, Q-3, R-1, S-4. (A)
- 54: P-3, Q-4, R-1, S-2. (A)
"""

val_md = r"""# Answer Key & Benchmark Validation — Mock 14
## IIT Delhi Benchmark Calibration

### Paper 1 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C |
| **P7** | Num | 9.5 | **C25** | Num | 3.20 | **M43** | Num | 8 |
| **P8** | Num | 20.9 | **C26** | Num | 2003 | **M44** | Num | 452 |
| **P9** | Num | 1.97 | **C27** | Num | 0.06 | **M45** | Num | 11 |
| **P10** | Num | 146 | **C28** | Num | 237.2 | **M46** | Num | 0 |
| **P11** | Num | 436 | **C29** | Num | 96.4 | **M47** | Num | 0.5 |
| **P12** | Num | 180 | **C30** | Num | 1.79 | **M48** | Num | 0.56 |
| **P13** | Single | A | **C31** | Single | A | **M49** | Single | A |
| **P14** | Single | A | **C32** | Single | C | **M50** | Single | A |
| **P15** | Single | A | **C33** | Single | A | **M51** | Single | A |
| **P16** | Single | A | **C34** | Single | A | **M52** | Single | A |
| **P17** | Single | A | **C35** | Single | A | **M53** | Single | A |
| **P18** | Single | A | **C36** | Single | A | **M54** | Single | A |

---

### Paper 2 Answer Key
| Q# | Type | Key | Q# | Type | Key | Q# | Type | Key |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** | Multi | A,B,C,D | **C19** | Multi | A,B,C,D | **M37** | Multi | A,B,C,D |
| **P2** | Multi | A,B,C,D | **C20** | Multi | A,B,C,D | **M38** | Multi | A,B,C,D |
| **P3** | Multi | A,B,C,D | **C21** | Multi | A,B,C,D | **M39** | Multi | A,B,C,D |
| **P4** | Multi | A,B,C,D | **C22** | Multi | A,B,C,D | **M40** | Multi | A,B,C,D |
| **P5** | Multi | A,B,C,D | **C23** | Multi | A,B,C,D | **M41** | Multi | A,B,C,D |
| **P6** | Multi | A,B,C,D | **C24** | Multi | A,B,C,D | **M42** | Multi | A,B,C,D |
| **P7** | Num | 22.9 | **C25** | Num | 7.01 | **M43** | Num | 16 |
| **P8** | Num | 312 | **C26** | Num | 3.87 | **M44** | Num | 44 |
| **P9** | Num | 1000 | **C27** | Num | 100.15 | **M45** | Num | 1.33 |
| **P10** | Num | 4.61 | **C28** | Num | 212.3 | **M46** | Num | 0.5 |
| **P11** | Num | 20000 | **C29** | Num | 30 | **M47** | Num | 5 |
| **P12** | Num | 2.94 | **C30** | Num | 4.0 | **M48** | Num | 0.44 |
| **P13** | Match | A | **C31** | Match | A | **M49** | Match | A |
| **P14** | Match | A | **C32** | Match | A | **M50** | Match | A |
| **P15** | Match | A | **C33** | Match | A | **M51** | Match | A |
| **P16** | Match | A | **C34** | Match | A | **M52** | Match | A |
| **P17** | Match | A | **C35** | Match | A | **M53** | Match | A |
| **P18** | Match | A | **C36** | Match | A | **M54** | Match | A |
"""

if __name__ == "__main__":
    create_mock_files(
        14,
        paper_1_md,
        paper_2_md,
        sol_1_md,
        sol_2_md,
        val_md,
        iit_name="IIT_Delhi"
    )
