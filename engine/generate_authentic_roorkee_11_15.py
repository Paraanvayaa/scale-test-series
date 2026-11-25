"""
IIT Roorkee Mocks 11 to 15 Generator
Organising Institute: Indian Institute of Technology Roorkee
Empirical Benchmark: 2008, 2013, 2019 Official JEE Advanced Papers
Features:
- Mechanics dominance (>= 45% of physics: ballistic pendulum, Venturi meter, Kundt's tube, gyroscopic gimbal precession)
- Chemistry: Cope/Claisen [3,3]-sigmatropic rearrangements, Beckmann rearrangement, Wade's rules, Parkes process
- Mathematics: Curvature and center of curvature, polar orthogonal trajectories, rank-nullity theorem, generating functions
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from batch_helper import create_mock_files

def generate_roorkee_11_to_15():
    for mock_idx in range(11, 16):
        pad = f"{mock_idx:02d}"

        raw_p1 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 1
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)
**Historical Reference Benchmark**: 2008, 2013, 2019 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject – Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** for incorrect option.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A ballistic pendulum consists of a uniform rigid rod of mass $M$ and length $L$ pivoted at its upper end $O$. A bullet of mass $m \ll M$ moving horizontally with speed $v_0$ strikes the rod at distance $x$ from the pivot and embeds itself in negligible time:
(A) Angular momentum about pivot $O$ is strictly conserved during the impact: $L_O = m v_0 x$.  
(B) The angular velocity of the pendulum immediately after impact is $\omega = \frac{m v_0 x}{\frac{1}{3}M L^2 + m x^2} \approx \frac{3 m v_0 x}{M L^2}$.  
(C) The horizontal impulsive reaction force at pivot $O$ vanishes during impact if the bullet strikes at the center of percussion $x_{\text{cp}} = \frac{2}{3}L$.  
(D) The maximum angle of deflection $\theta_{\max}$ satisfies $\frac{1}{2}I_O \omega^2 = M g \frac{L}{2}(1 - \cos\theta_{\max})$.

#### Question 2
A Venturi meter consists of a horizontal pipe of cross-sectional area $A_1$ tapering to a constriction (throat) of area $A_2 < A_1$, with a U-tube manometer containing manometric liquid of density $\rho_m$ connected between the main pipe and throat:
(A) The flow speed in the throat is related to the speed in the main pipe by $v_2 = \frac{A_1}{A_2} v_1$.  
(B) Neglecting viscous friction, Bernoulli's equation yields $P_1 - P_2 = \frac{1}{2}\rho(v_2^2 - v_1^2) = \frac{1}{2}\rho v_1^2 \left[\left(\frac{A_1}{A_2}\right)^2 - 1\right]$.  
(C) The theoretical volumetric discharge rate is $Q = A_1 A_2 \sqrt{\frac{2(\rho_m - \rho)gh}{\rho(A_1^2 - A_2^2)}}$.  
(D) The actual discharge rate is slightly less than theoretical due to viscous head loss, accounted for by a discharge coefficient $C_d < 1$.

#### Question 3
In Kundt's tube apparatus used to measure the speed of sound in a metal rod of length $L_r$ clamped at its middle:
(A) The rod vibrates longitudinally with a displacement node at the center and antinodes at its free ends.  
(B) The fundamental frequency of longitudinal vibration of the rod is $f = \frac{v_r}{2L_r}$, where $v_r = \sqrt{Y/\rho}$ is the speed of sound in the rod.  
(C) Lycopodium powder inside the glass tube forms heaps at the displacement nodes of the standing acoustic wave in air.  
(D) The distance between two consecutive heaps of powder is equal to half the acoustic wavelength in air: $d = \lambda_{\text{air}}/2$.

#### Question 4
A uniform solid sphere of mass $M$ and radius $R$ rolls without slipping on a horizontal plane with velocity $v_0$ and makes a head-on elastic collision with a stationary identical sphere:
(A) Linear momentum of the two-sphere system is conserved during the impact.  
(B) Immediately after the impact, the first sphere has zero linear velocity but retains its original rotational angular velocity $\omega_0 = v_0 / R$.  
(C) Friction between the ground and the first sphere immediately after impact acts forward, causing it to accelerate forward again.  
(D) The final steady-state velocity of the first sphere after pure rolling resumes is $v_1' = \frac{2}{7}v_0$.

#### Question 5
In an experiment to determine the angle of minimum deviation $D_{\min}$ of an equilateral glass prism using a spectrometer:
(A) At minimum deviation, the light ray passes symmetrically through the prism, parallel to the base.  
(B) The refractive index of the prism material is given by $\mu = \frac{\sin\left(\frac{A + D_{\min}}{2}\right)}{\sin(A/2)}$.  
(C) For an equilateral prism ($A = 60^\circ$), if $D_{\min} = 30^\circ$, then $\mu = \frac{\sin 45^\circ}{\sin 30^\circ} = \sqrt{2}$.  
(D) The angle of incidence equals the angle of emergence at minimum deviation: $i = e = \frac{A + D_{\min}}{2}$.

#### Question 6
A heavy flywheel of moment of inertia $I$ rotates at angular speed $\omega$ about a horizontal axle supported by bearings separated by distance $L$. The system is mounted on a platform that turns horizontally with precession angular velocity $\Omega$:
(A) The spinning flywheel possesses horizontal angular momentum $\vec{L} = I \omega \hat{i}$.  
(B) The precessional motion produces a gyroscopic torque $\vec{\tau} = \vec{\Omega} \times \vec{L}$ of magnitude $\tau = I \omega \Omega$.  
(C) The gyroscopic torque acts in a vertical plane, exerting additional vertical forces on the bearings: $\Delta F = \pm \frac{I\omega\Omega}{L}$.  
(D) If the platform turns counter-clockwise viewed from above, the bearing forces tend to tilt the axle vertically.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
A ballistic pendulum has a rod of mass $M = 3.0\text{ kg}$ and length $L = 1.0\text{ m}$. A bullet of mass $m = 0.02\text{ kg}$ is fired horizontally and embeds at the center of percussion ($x_{\text{cp}} = 2/3\text{ m}$). If the rod deflects to a maximum angle $\theta_{\max} = 60^\circ$, taking $g = 9.8\text{ m/s}^2$, the initial speed of the bullet in $\text{m/s}$ is $v_0$. Find $v_0$ rounded off to the nearest integer.

#### Question 8
In a Kundt's tube experiment, a steel rod of length $L_r = 1.0\text{ m}$ clamped at its center produces longitudinal waves that resonate with air in the tube. The average distance between successive powder heaps in the tube is $d = 6.5\text{ cm}$. If the speed of sound in air is $v_{\text{air}} = 340\text{ m/s}$, the speed of sound in the steel rod is $v_r\text{ m/s}$. Find $v_r$ rounded off to the nearest integer.

#### Question 9
In a spectrometer experiment with an equilateral glass prism ($A = 60.0^\circ$), the angle of minimum deviation is measured to be $D_{\min} = 37.2^\circ$. If $\sin(48.6^\circ) \approx 0.750$, the refractive index $\mu$ of the prism is $\mu$. Find $\mu$ rounded off to two decimal places.

#### Question 10
A Venturi meter with inlet diameter $d_1 = 20.0\text{ cm}$ and throat diameter $d_2 = 10.0\text{ cm}$ measures the flow of water. The pressure difference between inlet and throat corresponds to a water head $h = 0.50\text{ m}$. Taking $g = 9.8\text{ m/s}^2$, the flow speed at the inlet in $\text{m/s}$ is $v_1$. Find $v_1$ rounded off to two decimal places.

#### Question 11
A uniform solid sphere of mass $M = 2.0\text{ kg}$ and radius $R = 0.10\text{ m}$ initially spinning with $\omega_0 = 70.0\text{ rad/s}$ about a horizontal axis is placed gently on a rough horizontal surface ($\mu_k = 0.20$). Taking $g = 9.8\text{ m/s}^2$, the time taken for the sphere to attain pure rolling in seconds is $t\text{ s}$. Find $t$ rounded off to two decimal places.

#### Question 12
A flat rectangular plate of mass $m = 1.0\text{ kg}$ and area $A = 0.10\text{ m}^2$ is pulled horizontally over a thin layer of oil of thickness $d = 1.0\text{ mm}$ with constant speed $v = 2.0\text{ m/s}$. If the dynamic viscosity of the oil is $\eta = 0.50\text{ Pa s}$, the horizontal pulling force required in newtons is $F\text{ N}$. Find $F$.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The center of percussion of a uniform thin rod of length $L$ pivoted at one end is located at distance from the pivot of:
(A) $\frac{2}{3}L$  
(B) $\frac{1}{2}L$  
(C) $\frac{3}{4}L$  
(D) $\frac{1}{3}L$

#### Question 14
A liquid rises to height $h$ in a capillary tube on Earth. If the entire apparatus is taken in an artificial satellite in free fall orbit, the liquid will:
(A) Rise to the very top of the tube and stay there without overflowing  
(B) Not rise at all  
(C) Rise to height $h$  
(D) Overflow continuously

#### Question 15
The Reynolds number $Re = \frac{\rho v D}{\eta}$ characterizes:
(A) The ratio of inertial forces to viscous forces in a fluid flow  
(B) The ratio of pressure forces to surface tension forces  
(C) The ratio of buoyant forces to gravity forces  
(D) The ratio of elastic forces to drag forces

#### Question 16
In an experiment with a sonometer wire, the frequency of vibration is doubled if:
(A) Tension is quadrupled  
(B) Tension is doubled  
(C) Length is doubled  
(D) Linear density is doubled

#### Question 17
A particle of mass $m$ is moving in a circular orbit under an attractive central force $F(r) = -k/r^3$. The trajectory is:
(A) A logarithmic spiral or unstable orbit  
(B) A stable ellipse  
(C) A stable parabola  
(D) A hyperbola

#### Question 18
The temperature of an ideal gas is increased from $27^\circ\text{C}$ to $127^\circ\text{C}$. The percentage increase in its RMS molecular speed is approximately:
(A) $15.5\%$  
(B) $33.3\%$  
(C) $25.0\%$  
(D) $50.0\%$

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding the Cope and Claisen rearrangements:
(A) Both are concerted $[3,3]$-sigmatropic rearrangements occurring with suprafacial stereospecificity.  
(B) The Claisen rearrangement of allyl aryl ethers proceeds via a chair-like transition state to give *ortho*-allylphenols.  
(C) If both *ortho* positions are blocked, the allyl group migrates to the *para* position via two consecutive sigmatropic shifts with retention of original allyl connectivity.  
(D) The Cope rearrangement involves 1,5-hexadiene derivatives and is reversible, with equilibrium favoring the thermodynamically more substituted alkene.

#### Question 20
Regarding the Beckmann rearrangement of ketoximes:
(A) The reaction is catalyzed by strong acids ($\text{H}_2\text{SO}_4, \text{PCl}_5, \text{SOCl}_2$).  
(B) The group that migrates from carbon to nitrogen is strictly the group *anti* (trans) to the hydroxyl ($-\text{OH}$) group.  
(C) The rearrangement proceeds with retention of configuration at the migrating chiral carbon center.  
(D) The rearrangement of cyclohexanone oxime yields $\varepsilon$-caprolactam, the monomer for Nylon 6.

#### Question 21
Regarding the Wade's rules (Polyhedral Skeletal Electron Pair Theory) for boranes and carboranes:
(A) A *closo*-cluster with $n$ vertices has $n+1$ skeletal electron pairs ($2n+2$ skeletal electrons).  
(B) A *nido*-cluster with $n$ vertices has $n+2$ skeletal electron pairs ($2n+4$ skeletal electrons).  
(C) An *arachno*-cluster with $n$ vertices has $n+3$ skeletal electron pairs ($2n+6$ skeletal electrons).  
(D) $\text{B}_6\text{H}_6^{2-}$ is a *closo*-octahedral borane, while $\text{B}_5\text{H}_9$ is a *nido*-cluster.

#### Question 22
Regarding the Parkes process and metallurgy of lead:
(A) Galena ($\text{PbS}$) is roasted to give $\text{PbO}$ and $\text{PbSO}_4$, which undergo self-reduction with unreacted $\text{PbS}$ to yield crude lead (bullion).  
(B) Parkes process is used for the desilverization of argentiferous lead.  
(C) Zinc is added to molten lead; silver is far more soluble in molten zinc than in molten lead.  
(D) The zinc-silver alloy forms a crust on the surface of molten lead and is skimmed off, then zinc is separated by distillation.

#### Question 23
Regarding the stereochemistry of alkyne reductions:
(A) Catalytic hydrogenation over Lindlar's catalyst ($\text{Pd}/\text{CaCO}_3$ poisoned with lead acetate or quinoline) gives the *cis*-alkene (*syn*-addition).  
(B) Dissolving metal reduction using sodium in liquid ammonia ($\text{Na}/\text{liquid }\text{NH}_3$) gives the *trans*-alkene (*anti*-addition).  
(C) Hydroboration of internal alkynes with disiamylborane followed by protonolysis with acetic acid yields *cis*-alkenes.  
(D) Terminal alkynes react with $\text{Na}/\text{liquid }\text{NH}_3$ to form sodium acetylides rather than undergoing reduction.

#### Question 24
Which of the following molecules have a square planar molecular geometry:
(A) $[\text{PtCl}_4]^{2-}$  
(B) $\text{XeF}_4$  
(C) $[\text{Ni}(\text{CN})_4]^{2-}$  
(D) $[\text{NiCl}_4]^{2-}$ (this complex is tetrahedral)

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{Mg}(\text{OH})_2$ is $K_{\text{sp}} = 1.20 \times 10^{-11}$ at $298\text{ K}$. Calculate the $\text{pH}$ of a saturated aqueous solution of $\text{Mg}(\text{OH})_2$. Find the $\text{pH}$ rounded off to two decimal places.

#### Question 26
For the decomposition reaction $2\text{N}_2\text{O}_5(g) \to 4\text{NO}_2(g) + \text{O}_2(g)$, the rate constant is $k = 3.0 \times 10^{-4}\text{ s}^{-1}$. If the initial pressure of $\text{N}_2\text{O}_5$ is $500\text{ mmHg}$, the total pressure in $\text{mmHg}$ after $t = 2310\text{ s}$ ($t = t_{1/2}$) is $P_{\text{total}}$. Find $P_{\text{total}}$.

#### Question 27
The standard reduction potentials are $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77\text{ V}$ and $E^\circ(\text{I}_2/\text{I}^-) = +0.54\text{ V}$. The equilibrium constant $K$ for the reaction $2\text{Fe}^{3+} + 2\text{I}^- \rightleftharpoons 2\text{Fe}^{2+} + \text{I}_2$ at $298\text{ K}$ is written as $10^x$ where $x = \frac{2 \times 0.23}{0.0591}$. Find $x$ rounded off to two decimal places.

#### Question 28
Calculate the freezing point in $^\circ\text{C}$ of an aqueous solution containing $10.0\text{ g}$ of ethylene glycol ($\text{C}_2\text{H}_6\text{O}_2$, molar mass $62.0\text{ g/mol}$) dissolved in $100.0\text{ g}$ of water. Given $K_f(\text{H}_2\text{O}) = 1.86\text{ K kg mol}^{-1}$. Report $|T_f|$ in $^\circ\text{C}$ rounded off to two decimal places.

#### Question 29
A compound contains atoms of $X, Y, Z$. $X$ atoms form an FCC lattice, $Y$ atoms occupy all tetrahedral voids, and $Z$ atoms occupy all octahedral voids. The simplest formula is $X_a Y_b Z_c$. Find $a + b + c$.

#### Question 30
Find the number of skeletal electron pairs in the closo-borane cluster ion $\text{B}_6\text{H}_6^{2-}$.

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
The major product obtained upon treatment of acetophenone with hydroxylamine followed by $\text{PCl}_5$ and water (Beckmann rearrangement) is:
(A) Acetanilide ($\text{CH}_3\text{CONH}\text{C}_6\text{H}_5$)  
(B) $N$-Methylbenzamide ($\text{C}_6\text{H}_5\text{CONHCH}_3$)  
(C) Benzamide  
(D) Aniline

#### Question 32
Which of the following noble gas compounds is ISOELECTRONIC with $\text{ICl}_4^-$:
(A) $\text{XeF}_4$  
(B) $\text{XeO}_3$  
(C) $\text{XeOF}_4$  
(D) $\text{XeF}_2$

#### Question 33
In the extraction of lead from galena, the reducing agent in the self-reduction step is:
(A) $\text{PbS}$  
(B) $\text{CO}$  
(C) Carbon  
(D) $\text{H}_2$

#### Question 34
The compound that does NOT reduce Tollens' reagent is:
(A) Sucrose  
(B) Glucose  
(C) Fructose  
(D) Maltose

#### Question 35
Which of the following ions is diamagnetic:
(A) $\text{Zn}^{2+}$  
(B) $\text{Cu}^{2+}$  
(C) $\text{Fe}^{2+}$  
(D) $\text{Mn}^{2+}$

#### Question 36
The conjugate acid of hydrogen phosphate ion $\text{HPO}_4^{2-}$ is:
(A) $\text{H}_2\text{PO}_4^-$  
(B) $\text{H}_3\text{PO}_4$  
(C) $\text{PO}_4^{3-}$  
(D) $\text{H}_3\text{O}^+$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $\kappa(x)$ be the curvature of the plane curve $y = f(x)$ at point $(x, f(x))$:
(A) $\kappa(x) = \frac{|f''(x)|}{(1 + (f'(x))^2)^{3/2}}$.  
(B) The radius of curvature is $\rho(x) = \frac{1}{\kappa(x)}$.  
(C) For a circle of radius $R$, the curvature is constant everywhere and equal to $\frac{1}{R}$.  
(D) For a straight line, the curvature is identically zero everywhere.

#### Question 38
Consider the family of cardioids in polar coordinates $r = a(1 + \cos\theta)$:
(A) Differentiating logarithmically gives $\frac{1}{r}\frac{dr}{d\theta} = -\frac{\sin\theta}{1 + \cos\theta} = -\tan(\theta/2)$.  
(B) The differential equation of the orthogonal trajectories is obtained by replacing $\frac{dr}{d\theta}$ with $-r^2 \frac{d\theta}{dr}$.  
(C) The differential equation of the orthogonal trajectories is $\frac{1}{r}\frac{dr}{d\theta} = \cot(\theta/2)$.  
(D) The orthogonal trajectories are another family of cardioids given by $r = c(1 - \cos\theta)$.

#### Question 39
Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation represented by matrix $A$:
(A) $\dim(\text{ker}(T)) + \dim(\text{im}(T)) = n$ (Rank-Nullity Theorem).  
(B) $\text{rank}(A) \le \min(m, n)$.  
(C) If $m < n$, the system $A\vec{x} = \vec{0}$ has non-trivial solutions.  
(D) If $m = n$ and $\det(A) \ne 0$, then $T$ is an isomorphism.

#### Question 40
Let $I = \int_0^\infty e^{-x^2} dx$:
(A) $I = \frac{\sqrt{\pi}}{2}$ (Gaussian integral).  
(B) $I^2 = \int_0^\infty \int_0^\infty e^{-(x^2+y^2)} dx dy = \int_0^{\pi/2} d\theta \int_0^\infty e^{-r^2} r dr = \frac{\pi}{4}$.  
(C) $\int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}$.  
(D) $\int_0^\infty x^2 e^{-x^2} dx = \frac{\sqrt{\pi}}{4}$.

#### Question 41
Consider the system of planes $\lambda(x + y + z - 1) + \mu(2x + 3y - z + 4) = 0$:
(A) Every plane of this family passes through the line of intersection of the two given planes.  
(B) The line of intersection has direction vector $\vec{d} = (1, 1, 1) \times (2, 3, -1) = (-4, 3, 1)$.  
(C) The plane of the family passing through $(0, 0, 0)$ corresponds to $-\lambda + 4\mu = 0 \implies \lambda = 4\mu$.  
(D) No plane of the family is parallel to the line of intersection.

#### Question 42
Let $A$ be an $n \times n$ matrix with characteristic polynomial $p(\lambda) = \det(\lambda I - A)$:
(A) By the Cayley-Hamilton theorem, $p(A) = 0_{n \times n}$.  
(B) $A^{-1}$ can be expressed as a polynomial in $A$ of degree at most $n-1$ if $\det(A) \ne 0$.  
(C) The constant term of $p(\lambda)$ is $(-1)^n \det(A)$.  
(D) The coefficient of $\lambda^{n-1}$ in $p(\lambda)$ is $-\text{tr}(A)$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the radius of curvature of the parabola $y^2 = 4x$ at its vertex $(0, 0)$.

#### Question 44
Find the remainder when $11^{2024}$ is divided by 100.

#### Question 45
Find the shortest distance between the skew lines $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $\frac{x-4}{3} = \frac{y-5}{4} = \frac{z-6}{5}$. (Round off to two decimal places).

#### Question 46
Let $z = 1 + i\sqrt{3}$. Find the value of $|z^6|$.

#### Question 47
Find the number of ways to seat 4 married couples around a circular table such that men and women alternate.

#### Question 48
Find the radius of the sphere $x^2 + y^2 + z^2 - 4x + 6y - 2z - 11 = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The value of $\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x}$ is:
(A) 1  
(B) $1/2$  
(C) 2  
(D) 0

#### Question 50
The integrating factor of the differential equation $\frac{dy}{dx} + \frac{2y}{x} = x^3$ is:
(A) $x^2$  
(B) $x$  
(C) $\ln x$  
(D) $e^{2x}$

#### Question 51
The angle between the lines $2x = 3y = -z$ and $6x = -y = -4z$ is:
(A) $90^\circ$  
(B) $60^\circ$  
(C) $45^\circ$  
(D) $30^\circ$

#### Question 52
If $A$ and $B$ are square matrices of order 3 such that $\det(A) = 2$ and $\det(B) = 3$, then $\det(2AB)$ is:
(A) 48  
(B) 12  
(C) 24  
(D) 96

#### Question 53
The number of distinct real roots of $x^3 - 3x^2 + 3x - 1 = 0$ is:
(A) 1  
(B) 2  
(C) 3  
(D) 0

#### Question 54
The probability of throwing a total of 7 with two fair dice is:
(A) $1/6$  
(B) $1/12$  
(C) $5/36$  
(D) $1/36$
"""

        raw_p2 = r"""# JEE Advanced Mock Examination __PAD__ – Paper 2
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)
**Historical Reference Benchmark**: 2008, 2013, 2019 Official Examination Papers  
**Duration**: 3 Hours | **Maximum Marks**: 180 Marks  
**Structure**: 54 Questions Total (18 Physics, 18 Chemistry, 18 Mathematics)

---

### Marking Scheme Summary
- **Section 1 (6 Questions per subject – One or More Than One Correct)**:
  - Full Marks: **+4** if only all correct option(s) is(are) chosen.
  - Partial Marks: **+3, +2, +1** for correct subsets.
  - Negative Marks: **-2** in all other cases.
  - Zero Marks: **0** if unattempted.
- **Section 2 (6 Questions per subject – Non-Negative Numerical Value)**:
  - Full Marks: **+3** if only the correct numerical value is entered.
  - Negative Marks: **0** in all other cases.
  - Precision: Round off to TWO decimal places where non-integers occur.
- **Section 3 (6 Questions per subject – Single Correct Option)**:
  - Full Marks: **+3** if only the correct option is chosen.
  - Negative Marks: **-1** for incorrect option.
  - Zero Marks: **0** if unattempted.

---

# PART I: PHYSICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 1 to 6)

#### Question 1
A uniform solid sphere of mass $M$ and radius $R$ is placed on an inclined plane of angle $\theta$. The coefficient of friction is $\mu < \frac{2}{7}\tan\theta$, so the sphere rolls and slips simultaneously:
(A) Kinetic friction acts up the incline with magnitude $f_k = \mu M g \cos\theta$.  
(B) The linear acceleration of the center of mass is $a = g(\sin\theta - \mu\cos\theta)$.  
(C) The angular acceleration about the center of mass is $\alpha = \frac{f_k R}{I_{\text{cm}}} = \frac{5\mu g\cos\theta}{2R}$.  
(D) Mechanical energy is not conserved because kinetic friction dissipates energy as heat.

#### Question 2
Regarding the flow of a viscous fluid around a spinning cylinder (Magnus effect):
(A) Circulation is created around the cylinder by viscous dragging of fluid layers.  
(B) The flow velocity is higher on the side where fluid motion and surface rotation are in the same direction.  
(C) By Bernoulli's principle, pressure is lower on the high-speed side, generating a transverse lift force.  
(D) The Kutta-Joukowski theorem gives the lift force per unit length as $F_L = \rho v_\infty \Gamma$, where $\Gamma$ is circulation.

#### Question 3
A liquid film is formed on a vertical rectangular wire frame of width $w$ with a movable horizontal wire of mass $m$ at the bottom:
(A) The upward surface tension force exerted on the wire is $F_s = 2 T w$.  
(B) In mechanical equilibrium, the mass of the wire satisfies $m g = 2 T w$.  
(C) If the wire is pulled down slightly by distance $y$ and released, it does not execute simple harmonic motion because surface tension is independent of displacement.  
(D) The film has two liquid-gas interfaces.

#### Question 4
In a potentiometer experiment to determine the internal resistance $r$ of a primary cell of EMF $\mathcal{E}$:
(A) The balancing length with open circuit is $l_1$, so $\mathcal{E} \propto l_1$.  
(B) When a shunt resistance $R$ is connected across the cell, the terminal voltage is balanced at length $l_2 < l_1$, so $V \propto l_2$.  
(C) The internal resistance is given by $r = R\left(\frac{l_1}{l_2} - 1\right)$.  
(D) Potentiometer measurements draw zero current from the test cell at the null point, avoiding errors due to internal voltage drops.

#### Question 5
A uniform disc of mass $M$ and radius $R$ is rolling without slipping on a horizontal surface. It enters a rough step of height $h < R$:
(A) The collision is inelastic and instantaneous.  
(B) Angular momentum about the point of impact on the step edge is conserved during the impact.  
(C) The moment of inertia of the disc about the step edge at the instant of impact is $I = \frac{3}{2}MR^2$.  
(D) The disc can roll up the step only if its post-collision kinetic energy exceeds $Mg h$.

#### Question 6
An ideal gas undergoes a polytropic process $P V^n = \text{constant}$:
(A) The molar heat capacity is $C = C_V + \frac{R}{1-n}$.  
(B) For an isobaric process ($n=0$), $C = C_P = C_V + R$.  
(C) For an isothermal process ($n=1$), $C \to \infty$.  
(D) For an adiabatic process ($n=\gamma$), $C = 0$.

---

## Section 2: Non-Negative Numerical Value (Questions 7 to 12)

#### Question 7
In a potentiometer experiment, the balancing length for a cell is $l_1 = 300.0\text{ cm}$. When a shunt of $R = 10.0\text{ }\Omega$ is connected across the cell, the balancing length becomes $l_2 = 250.0\text{ cm}$. The internal resistance of the cell in ohms is $r\text{ }\Omega$. Find $r$.

#### Question 8
A sphere of mass $M = 4.0\text{ kg}$ rolls and slips down an incline of $\theta = 37^\circ$ ($\sin 37^\circ = 0.60, \cos 37^\circ = 0.80$). If $\mu_k = 0.10$ and $g = 9.8\text{ m/s}^2$, the linear acceleration of the center of mass in $\text{m/s}^2$ is $a$. Find $a$ rounded off to two decimal places.

#### Question 9
A soap film is formed on a rectangular frame of wire of width $w = 5.0\text{ cm}$. The force required to hold the movable wire in equilibrium is $F = 3.5 \times 10^{-3}\text{ N}$. The surface tension of the soap solution in $\text{N/m}$ is $T$. Find $T$ rounded off to three decimal places.

#### Question 10
In a Magnus effect demonstration, air of density $\rho = 1.20\text{ kg/m}^3$ flows at speed $v = 15.0\text{ m/s}$ past a rotating cylinder of length $L = 2.0\text{ m}$ having circulation $\Gamma = 5.0\text{ m}^2/\text{s}$. The total lift force on the cylinder in newtons is $F_L\text{ N}$. Find $F_L$.

#### Question 11
An ideal gas with $\gamma = 1.40$ expands polytropically with index $n = 2.0$. Given $C_V = \frac{5}{2}R$, the molar heat capacity of the gas in units of $R$ is $C$. Find $|C|$.

#### Question 12
A solid sphere rolls down an incline from height $h = 7.0\text{ m}$ without slipping. Taking $g = 9.8\text{ m/s}^2$, the speed of the center of mass at the bottom of the incline in $\text{m/s}$ is $v$. Find $v$ rounded off to two decimal places.

---

## Section 3: Single Correct Option (Questions 13 to 18)

#### Question 13
The center of mass of a uniform thin wire bent into a semicircle of radius $R$ is at distance from the center of curvature of:
(A) $\frac{2R}{\pi}$  
(B) $\frac{R}{\pi}$  
(C) $\frac{4R}{3\pi}$  
(D) $\frac{R}{2}$

#### Question 14
Two bodies of masses $m$ and $4m$ have equal linear momenta. The ratio of their kinetic energies is:
(A) $4:1$  
(B) $1:4$  
(C) $2:1$  
(D) $1:2$

#### Question 15
A wooden cube of side $L$ floats in water with $1/4$ of its volume above the water surface. The density of wood is:
(A) $750\text{ kg/m}^3$  
(B) $250\text{ kg/m}^3$  
(C) $500\text{ kg/m}^3$  
(D) $800\text{ kg/m}^3$

#### Question 16
Water is flowing through a horizontal tube of radius $r$ at rate $Q$. If the radius of the tube is halved while maintaining the same pressure difference, the new flow rate according to Poiseuille's law is:
(A) $Q / 16$  
(B) $Q / 4$  
(C) $Q / 8$  
(D) $Q / 2$

#### Question 17
A particle moves in a potential $V(r) = \frac{1}{2}k r^2$. The orbit is:
(A) An ellipse with the center of force at its center  
(B) An ellipse with the center of force at a focus  
(C) A parabola  
(D) A hyperbola

#### Question 18
The degrees of freedom of a non-linear triatomic gas molecule (such as $\text{H}_2\text{O}$) at moderate temperatures is:
(A) 6  
(B) 5  
(C) 3  
(D) 7

---

# PART II: CHEMISTRY (54 Marks)

## Section 1: One or More Than One Correct (Questions 19 to 24)

#### Question 19
Regarding carbohydrates and their chemical properties:
(A) Oxidation of D-glucose with bromine water ($\text{Br}_2/\text{H}_2\text{O}$) selectively oxidizes the aldehyde group to give D-gluconic acid (aldonic acid).  
(B) Oxidation of D-glucose with concentrated nitric acid ($\text{HNO}_3$) oxidizes both the aldehyde and terminal primary alcohol to give D-glucaric acid (aldaric acid).  
(C) D-glucose and D-fructose form identical osazones when treated with excess phenylhydrazine because they differ in stereochemistry only at C-1 and C-2.  
(D) Glycogen is the major storage polysaccharide in animals and has a structure similar to amylopectin with more frequent branching.

#### Question 20
Regarding transport numbers and ionic mobility in electrolytic solutions:
(A) The transport number (transference number) of an ion is the fraction of total current carried by that ion: $t_+ = \frac{u_+}{u_+ + u_-}$.  
(B) The sum of transport numbers of all ions in a solution is identically 1: $t_+ + t_- = 1$.  
(C) Hittorf's method and the moving boundary method are standard experimental techniques for determining transport numbers.  
(D) In aqueous solution, $\text{H}^+$ and $\text{OH}^-$ exhibit exceptionally high molar conductivities due to the Grotthuss proton-hopping mechanism.

#### Question 21
Regarding the chemistry of silicones:
(A) Silicones are synthetic organosilicon polymers with the repeating backbone unit $[-\text{R}_2\text{Si}-\text{O}-]_n$.  
(B) Hydrolysis of dimethyldichlorosilane $\text{Me}_2\text{SiCl}_2$ followed by condensation polymerization yields linear silicones.  
(C) Hydrolysis of methyltrichlorosilane $\text{MeSiCl}_3$ yields cross-linked, three-dimensional network silicones.  
(D) Trimethylchlorosilane $\text{Me}_3\text{SiCl}$ acts as a chain terminator in silicone synthesis.

#### Question 22
Regarding the extraction and metallurgy of lead and tin:
(A) Cassiterite ($\text{SnO}_2$, tinstone) is reduced by carbon in a reverberatory furnace: $\text{SnO}_2 + 2\text{C} \to \text{Sn} + 2\text{CO}$.  
(B) Crude tin is refined by liquation and poling to remove iron, copper, and lead impurities.  
(C) Galena is the primary ore of lead.  
(D) Lead bullion contains silver which is commercially recovered via the Parkes process.

#### Question 23
Regarding the stereochemistry and conformations of cyclohexane derivatives:
(A) In *cis*-1,4-dimethylcyclohexane, one methyl group must be axial and one equatorial in both chair conformations, making them degenerate.  
(B) In *trans*-1,4-dimethylcyclohexane, the diequatorial conformer is more stable than the diaxial conformer.  
(C) *cis*-1,3-Dimethylcyclohexane exists predominantly in the diequatorial conformation and is an achiral *meso* compound with a plane of symmetry.  
(D) *trans*-1,3-Dimethylcyclohexane is chiral and exists as a pair of enantiomers.

#### Question 24
Which of the following molecules possess a linear geometry:
(A) $\text{BeCl}_2$ (in vapor phase)  
(B) $\text{CO}_2$  
(C) $\text{C}_2\text{H}_2$ (acetylene)  
(D) $\text{SO}_2$ (this molecule is bent)

---

## Section 2: Non-Negative Numerical Value (Questions 25 to 30)

#### Question 25
The solubility product of $\text{AgCl}$ is $K_{\text{sp}} = 1.8 \times 10^{-10}$ at $298\text{ K}$. Calculate the concentration of $\text{Ag}^+$ in a solution where $[\text{Cl}^-] = 0.020\text{ M}$. Report $[\text{Ag}^+]$ as $X \times 10^{-9}\text{ M}$. Find $X$.

#### Question 26
Calculate the $\text{pH}$ of a $0.020\text{ M}$ aqueous solution of calcium hydroxide $\text{Ca}(\text{OH})_2$ assuming complete dissociation at $298\text{ K}$. Find the $\text{pH}$ rounded off to two decimal places.

#### Question 27
For the half-cell $\text{Cr}_2\text{O}_7^{2-} + 14\text{H}^+ + 6e^- \to 2\text{Cr}^{3+} + 7\text{H}_2\text{O}$, the standard reduction potential is $E^\circ = +1.33\text{ V}$. If $[\text{Cr}_2\text{O}_7^{2-}] = [\text{Cr}^{3+}] = 1.0\text{ M}$ and $\text{pH} = 2.0$, the reduction potential at $298\text{ K}$ is $E\text{ V}$. Find $E$ rounded off to two decimal places.

#### Question 28
The half-life of a radioactive isotope is $20.0\text{ days}$. The time required for $75\%$ of the sample to decay is $t\text{ days}$. Find $t$.

#### Question 29
A $0.10\text{ molal}$ aqueous solution of a coordination complex $\text{CoCl}_3 \cdot 4\text{NH}_3$ freezes at $-0.372^\circ\text{C}$. Given $K_f(\text{H}_2\text{O}) = 1.86\text{ K kg mol}^{-1}$, the number of ions produced per formula unit in solution is $N$. Find $N$.

#### Question 30
Find the oxidation state of sulfur in sodium dithionite ($\text{Na}_2\text{S}_2\text{O}_4$).

---

## Section 3: Single Correct Option (Questions 31 to 36)

#### Question 31
Which of the following compounds gives benzoic acid upon vigorous oxidation with alkaline $\text{KMnO}_4$:
(A) Toluene ($\text{C}_6\text{H}_5\text{CH}_3$)  
(B) *tert*-Butylbenzene  
(C) Benzene  
(D) Phenol

#### Question 32
The correct order of ionic radii is:
(A) $\text{N}^{3-} > \text{O}^{2-} > \text{F}^- > \text{Na}^+ > \text{Mg}^{2+} > \text{Al}^{3+}$  
(B) $\text{Al}^{3+} > \text{Mg}^{2+} > \text{Na}^+ > \text{F}^- > \text{O}^{2-} > \text{N}^{3-}$  
(C) $\text{Na}^+ > \text{Mg}^{2+} > \text{Al}^{3+} > \text{F}^- > \text{O}^{2-} > \text{N}^{3-}$  
(D) $\text{F}^- > \text{O}^{2-} > \text{N}^{3-} > \text{Na}^+ > \text{Mg}^{2+} > \text{Al}^{3+}$

#### Question 33
The geometry and hybridization of chlorine in $\text{ClO}_3^-$ are:
(A) Trigonal pyramidal, $sp^3$  
(B) Trigonal planar, $sp^2$  
(C) Tetrahedral, $sp^3$  
(D) T-shaped, $sp^3d$

#### Question 34
In the reaction of phenol with neutral $\text{FeCl}_3$, the color produced is:
(A) Violet  
(B) Red  
(C) Blue  
(D) Green

#### Question 35
The linkage present between monosaccharide units in sucrose is:
(A) $\alpha\text{-D-glucose}-(1\to 2)\text{-}\beta\text{-D-fructose}$  
(B) $\beta(1\to 4)$  
(C) $\alpha(1\to 4)$  
(D) $\alpha(1\to 6)$

#### Question 36
The hybridization of iron in $[\text{Fe}(\text{H}_2\text{O})_6]^{2+}$ is:
(A) $sp^3d^2$  
(B) $d^2sp^3$  
(C) $sp^3$  
(D) $dsp^2$

---

# PART III: MATHEMATICS (54 Marks)

## Section 1: One or More Than One Correct (Questions 37 to 42)

#### Question 37
Let $f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \tanh x$ for $x \in \mathbb{R}$:
(A) $f(x)$ is an odd function: $f(-x) = -f(x)$.  
(B) $f'(x) = 1 - \tanh^2 x = \text{sech}^2 x > 0$ for all $x \in \mathbb{R}$, strictly increasing.  
(C) The range of $f(x)$ is $(-1, 1)$.  
(D) The horizontal lines $y = \pm 1$ are asymptotes as $x \to \pm \infty$.

#### Question 38
Let $A$ be a $3 \times 3$ nilpotent matrix ($A^k = 0$ for some $k \ge 1$):
(A) The only eigenvalue of $A$ is 0.  
(B) $\text{tr}(A) = 0$ and $\det(A) = 0$.  
(C) $A^3 = 0_{3 \times 3}$.  
(D) $I_3 + A$ is invertible with inverse $I_3 - A + A^2$.

#### Question 39
Consider the family of circles passing through the points $(0, 2)$ and $(0, -2)$:
(A) The equation of the common chord is $x = 0$ ($y$-axis).  
(B) The family of circles is given by $x^2 + y^2 - 4 + 2\lambda x = 0$.  
(C) The centers of all circles of the family lie on the $x$-axis at $(-\lambda, 0)$.  
(D) Every circle of the family is orthogonal to the circle $x^2 + y^2 + 2\mu y - 4 = 0$.

#### Question 40
Let $I = \int_0^1 x^3 \sqrt{1-x^2} dx$:
(A) The substitution $x = \sin\theta$ converts the integral into $\int_0^{\pi/2} \sin^3\theta\cos^2\theta d\theta$.  
(B) $I = \frac{2}{15}$.  
(C) $\int_0^1 x \sqrt{1-x^2} dx = \frac{1}{3}$.  
(D) $\int_0^1 \sqrt{1-x^2} dx = \frac{\pi}{4}$.

#### Question 41
Consider the system of vectors $\vec{a} = 2\hat{i} + \hat{j} - \hat{k}$, $\vec{b} = \hat{i} - \hat{j} + 2\hat{k}$, and $\vec{c} = \hat{i} + 2\hat{j} + \lambda\hat{k}$:
(A) The scalar triple product is $[\vec{a}\quad \vec{b}\quad \vec{c}] = -3\lambda - 9$.  
(B) The three vectors are coplanar if $\lambda = -3$.  
(C) The volume of the parallelepiped formed by $\vec{a}, \vec{b}, \vec{c}$ for $\lambda = 0$ is 9.  
(D) $\vec{a} \cdot \vec{b} = 2 - 1 - 2 = -1$.

#### Question 42
Let $f(x) = \sin x + \cos x$:
(A) $f(x) = \sqrt{2}\sin(x + \pi/4)$.  
(B) The maximum value of $f(x)$ is $\sqrt{2}$ attained at $x = \pi/4 + 2k\pi$.  
(C) The minimum value of $f(x)$ is $-\sqrt{2}$ attained at $x = 5\pi/4 + 2k\pi$.  
(D) The period of $f(x)$ is $2\pi$.

---

## Section 2: Non-Negative Numerical Value (Questions 43 to 48)

#### Question 43
Find the area enclosed between the loop of the curve $y^2 = x(x-2)^2$ and the $y$-axis from $x = 0$ to $x = 2$. Round off to two decimal places.

#### Question 44
Find the remainder when $3^{2025}$ is divided by 8.

#### Question 45
Find the distance from the point $(3, 4, 5)$ to the plane $2x + y - 2z + 9 = 0$.

#### Question 46
Let $\alpha$ and $\beta$ be the roots of $x^2 - 5x + 3 = 0$. Find the value of $\alpha^3 + \beta^3$.

#### Question 47
How many diagonals does a regular decagon (10-sided polygon) have?

#### Question 48
Find the radius of the circle $x^2 + y^2 + 10x - 6y + 9 = 0$.

---

## Section 3: Single Correct Option (Questions 49 to 54)

#### Question 49
The derivative of $\arctan\left(\frac{\cos x - \sin x}{\cos x + \sin x}\right)$ with respect to $x$ is:
(A) $-1$  
(B) $1$  
(C) $1/2$  
(D) $-1/2$

#### Question 50
The general solution of the differential equation $\frac{dy}{dx} = e^{x-y}$ is:
(A) $e^y = e^x + C$  
(B) $e^y = -e^x + C$  
(C) $e^{-y} = e^{-x} + C$  
(D) $y = x + C$

#### Question 51
The length of the major axis of the ellipse $9x^2 + 16y^2 = 144$ is:
(A) 8  
(B) 6  
(C) 4  
(D) 12

#### Question 52
If $\log_2(x-1) = 3$, then $x$ is equal to:
(A) 9  
(B) 8  
(C) 7  
(D) 10

#### Question 53
The value of $\sin(15^\circ)$ is:
(A) $\frac{\sqrt{6} - \sqrt{2}}{4}$  
(B) $\frac{\sqrt{6} + \sqrt{2}}{4}$  
(C) $\frac{\sqrt{3} - 1}{2\sqrt{2}}$  
(D) Both (A) and (C)

#### Question 54
From a well-shuffled pack of 52 playing cards, a card is drawn at random. The probability that it is a spade or an ace is:
(A) $4/13$  
(B) $17/52$  
(C) $1/4$  
(D) $1/13$
"""

        raw_sol1 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 1)
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Ballistic pendulum: angular momentum about pivot $O$ is conserved during rapid impact: $L_O = m v_0 x = I_O \omega$. Center of percussion $x_{\text{cp}} = I_{\text{cm}} / (M d) + d = \frac{1}{12}ML^2 / (M L/2) + L/2 = L/6 + L/2 = 2L/3$. At this point impulsive reaction at pivot vanishes. Subsequent swing is governed by energy conservation. **Correct Options**: (A, B, C, D)
- **Q2**: Venturi meter principles: continuity $A_1 v_1 = A_2 v_2$, Bernoulli equation pressure drop $P_1 - P_2 = \frac{1}{2}\rho(v_2^2 - v_1^2)$, discharge formula and discharge coefficient $C_d < 1$. **Correct Options**: (A, B, C, D)
- **Q3**: Kundt's tube acoustics: rod has displacement node at clamp, antinodes at free ends $\implies L_r = \lambda_r / 2 \implies f = v_r / (2L_r)$. Powder heaps in tube form at displacement nodes of standing waves in air, spaced by $\lambda_{\text{air}} / 2$. **Correct Options**: (A, B, C, D)
- **Q4**: Sphere collision with rotation: linear velocity transferred instantaneously to second sphere, first sphere retains $\omega_0$. Relative slipping at contact induces forward kinetic friction, accelerating it forward until pure rolling is restored at $v_1' = \frac{2}{7}v_0$. **Correct Options**: (A, B, C, D)
- **Q5**: Minimum deviation of equilateral prism: symmetric path $i = e = (A + D_{\min})/2$, refractive index $\mu = \frac{\sin((A+D_{\min})/2)}{\sin(A/2)}$. For $A = 60^\circ, D_{\min} = 30^\circ \implies \mu = \sqrt{2}$. **Correct Options**: (A, B, C, D)
- **Q6**: Gyroscopic precession: angular momentum $\vec{L} = I\omega\hat{i}$, precession $\vec{\Omega} = \Omega\hat{k}$. Torque $\vec{\tau} = \vec{\Omega} \times \vec{L} = I\omega\Omega\hat{j}$. Bearing reaction couples $\Delta F = \pm \tau / L$. **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: Ballistic pendulum: $\frac{1}{2}I_O \omega^2 = M g \frac{L}{2}(1 - \cos 60^\circ) = \frac{1}{4}MgL$. Here $I_O = \frac{1}{3}ML^2 = \frac{1}{3}(3.0)(1.0)^2 = 1.0\text{ kg m}^2$. $\frac{1}{2}(1.0)\omega^2 = \frac{1}{4}(3.0)(9.8)(1.0) = 7.35 \implies \omega^2 = 14.7 \implies \omega \approx 3.834\text{ rad/s}$. Angular momentum: $m v_0 x = I_O \omega \implies v_0 = \frac{I_O \omega}{m x} = \frac{1.0 \times 3.834}{0.02 \times (2/3)} = \frac{3.834}{0.01333} \approx 287.5\text{ m/s} \approx 288\text{ m/s} \implies \mathbf{288.00}$.
- **Q8**: $\lambda_{\text{air}} = 2d = 2 \times 6.5\text{ cm} = 13.0\text{ cm} = 0.13\text{ m}$. Frequency $f = v_{\text{air}} / \lambda_{\text{air}} = 340 / 0.13 \approx 2615.4\text{ Hz}$. In the rod: $\lambda_r = 2L_r = 2.0\text{ m}$. Speed in rod $v_r = f \lambda_r = 2615.4 \times 2.0 \approx 5231\text{ m/s} \implies \mathbf{5231.00}$.
- **Q9**: $\mu = \frac{\sin((60 + 37.2)/2)}{\sin(30^\circ)} = \frac{\sin(48.6^\circ)}{0.50} = \frac{0.750}{0.50} = 1.50 \implies \mathbf{1.50}$.
- **Q10**: Area ratio $A_1 / A_2 = (d_1 / d_2)^2 = (20/10)^2 = 4$. $v_1 = \sqrt{\frac{2gh}{(A_1/A_2)^2 - 1}} = \sqrt{\frac{2(9.8)(0.50)}{16 - 1}} = \sqrt{\frac{9.8}{15}} \approx \sqrt{0.6533} \approx 0.81\text{ m/s} \implies \mathbf{0.81}$.
- **Q11**: Kinetic friction $f_k = \mu_k M g = (0.20)(2.0)(9.8) = 3.92\text{ N}$. Linear acceleration $a = f_k / M = 1.96\text{ m/s}^2$. Angular deceleration $\alpha = \frac{f_k R}{\frac{2}{5}MR^2} = \frac{5\mu_k g}{2R} = \frac{5(0.20)(9.8)}{2(0.10)} = 49.0\text{ rad/s}^2$. Pure rolling when $v(t) = R\omega(t) \implies a t = R(\omega_0 - \alpha t) \implies (a + R\alpha)t = R\omega_0$. $a + R\alpha = 1.96 + 0.10(49) = 1.96 + 4.90 = 6.86\text{ m/s}^2$. Time $t = \frac{0.10 \times 70.0}{6.86} = \frac{7.0}{6.86} \approx 1.02\text{ s} \implies \mathbf{1.02}$.
- **Q12**: Viscous force $F = \eta A \frac{v}{d} = (0.50)(0.10)\frac{2.0}{1.0 \times 10^{-3}} = 0.05 \times 2000 = 100.0\text{ N} \implies \mathbf{100.00}$.

### Questions 13 to 18
- **Q13**: Center of percussion of rod pivoted at end: $x_{\text{cp}} = \frac{I_O}{M d} = \frac{L^2/3}{L/2} = \frac{2}{3}L$. **Correct: (A)**.
- **Q14**: In zero gravity, surface tension pulls liquid to the full available length of the capillary tube without overflowing. **Correct: (A)**.
- **Q15**: Reynolds number represents ratio of inertial to viscous forces. **Correct: (A)**.
- **Q16**: Sonometer frequency $f \propto \sqrt{T}$. To double frequency, tension must be quadrupled. **Correct: (A)**.
- **Q17**: For $F(r) = -k/r^3$, the effective potential has no stable circular orbit minimum $\implies$ orbit is an unstable logarithmic spiral. **Correct: (A)**.
- **Q18**: $v_{\text{rms}} \propto \sqrt{T}$. $T_1 = 300\text{ K}$, $T_2 = 400\text{ K}$. Ratio is $\sqrt{400/300} = \sqrt{4/3} \approx 1.1547 \implies 15.5\%$ increase. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Cope and Claisen $[3,3]$-sigmatropic rearrangements characteristics. **Correct Options**: (A, B, C, D)
- **Q20**: Beckmann rearrangement mechanism: anti-migration with retention of stereochemistry. **Correct Options**: (A, B, C, D)
- **Q21**: Wade's rules for polyhedral boranes and carboranes. **Correct Options**: (A, B, C, D)
- **Q22**: Parkes process for desilverization of lead. **Correct Options**: (A, B, C, D)
- **Q23**: Stereoselective reduction of alkynes (Lindlar syn vs Birch anti). **Correct Options**: (A, B, C, D)
- **Q24**: Square planar geometry: $[\text{PtCl}_4]^{2-}$ ($d^8$ Pt(II)), $\text{XeF}_4$ ($sp^3d^2$), $[\text{Ni}(\text{CN})_4]^{2-}$ (low spin $d^8$). $[\text{NiCl}_4]^{2-}$ is tetrahedral. **Correct Options**: (A, B, C)

### Questions 25 to 30
- **Q25**: $\text{Mg}(\text{OH})_2 \rightleftharpoons \text{Mg}^{2+} + 2\text{OH}^- \implies K_{\text{sp}} = 4S^3 = 1.20 \times 10^{-11} \implies S^3 = 3.0 \times 10^{-12} \implies S \approx 1.442 \times 10^{-4}\text{ M}$. $[\text{OH}^-] = 2S = 2.885 \times 10^{-4}\text{ M} \implies \text{pOH} = 3.54 \implies \text{pH} = 14 - 3.54 = 10.46 \implies \mathbf{10.46}$.
- **Q26**: $2\text{N}_2\text{O}_5 \to 4\text{NO}_2 + \text{O}_2$. At $t = t_{1/2}$, $P_{\text{N}_2\text{O}_5} = 250\text{ mmHg}$. $\Delta P = 250\text{ mmHg}$. $P_{\text{NO}_2} = 2\Delta P = 500\text{ mmHg}$. $P_{\text{O}_2} = \frac{1}{2}\Delta P = 125\text{ mmHg}$. Total pressure $= 250 + 500 + 125 = 875\text{ mmHg} \implies \mathbf{875.00}$.
- **Q27**: $x = \frac{2 \times 0.23}{0.0591} = \frac{0.46}{0.0591} \approx 7.78 \implies \mathbf{7.78}$.
- **Q28**: $\Delta T_f = K_f m = 1.86 \times \frac{10.0 / 62.0}{0.100} = 1.86 \times \frac{0.1613}{0.100} = 1.86 \times 1.613 \approx 3.00^\circ\text{C} \implies |T_f| = \mathbf{3.00}$.
- **Q29**: In FCC, $X = 4$. Tetrahedral voids $Y = 2 \times 4 = 8$. Octahedral voids $Z = 4$. Formula $X_4 Y_8 Z_4 \implies X Y_2 Z$. $a + b + c = 1 + 2 + 1 = 4 \implies \mathbf{4.00}$.
- **Q30**: For $\text{B}_6\text{H}_6^{2-}$, $n = 6$. Skeletal electron pairs $= n + 1 = 6 + 1 = 7 \implies \mathbf{7.00}$.

### Questions 31 to 36
- **Q31**: In acetophenone oxime, the phenyl group is anti to $-\text{OH}$, so phenyl migrates to nitrogen, giving acetanilide. **Correct: (A)**.
- **Q32**: $\text{ICl}_4^-$ has $7 + 4(7) + 1 = 36$ valence electrons. $\text{XeF}_4$ has $8 + 4(7) = 36$ valence electrons $\implies$ isoelectronic. **Correct: (A)**.
- **Q33**: Unreacted $\text{PbS}$ reduces $\text{PbO}$ and $\text{PbSO}_4$ in the self-reduction step. **Correct: (A)**.
- **Q34**: Sucrose is a non-reducing disaccharide (both anomeric carbons in glycosidic bond). **Correct: (A)**.
- **Q35**: $\text{Zn}^{2+}$ has completely filled $d^{10}$ configuration $\implies$ diamagnetic. **Correct: (A)**.
- **Q36**: Adding a proton to $\text{HPO}_4^{2-}$ gives $\text{H}_2\text{PO}_4^-$. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Curvature of plane curves formulas. **Correct Options**: (A, B, C, D)
- **Q38**: Orthogonal trajectories of cardioids $r = a(1+\cos\theta)$ are $r = c(1-\cos\theta)$. **Correct Options**: (A, B, C, D)
- **Q39**: Rank-Nullity theorem and consequences. **Correct Options**: (A, B, C, D)
- **Q40**: Gaussian integral and polar coordinate evaluation. **Correct Options**: (A, B, C, D)
- **Q41**: Family of planes passing through the intersection of two planes. **Correct Options**: (A, B, C)
- **Q42**: Cayley-Hamilton theorem and characteristic polynomial properties. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: For $y^2 = 4x$, $2y y' = 4 \implies y' = 2/y$. As $x \to 0, y \to 0$, invert: $x = y^2/4 \implies x' = y/2, x'' = 1/2$. At vertex $y=0$, $x'=0, x''=1/2$. $\kappa = \frac{1/2}{(1+0)^{3/2}} = 1/2 \implies \rho = 1/\kappa = 2.00 \implies \mathbf{2.00}$.
- **Q44**: $11^1 = 11, 11^2 = 121 \equiv 21, 11^3 \equiv 31, \dots, 11^{10} \equiv 1 \pmod{100}$. $2024 = 10 \times 202 + 4$. $11^{2024} \equiv 11^4 = 14641 \equiv 41 \pmod{100} \implies \mathbf{41.00}$.
- **Q45**: Lines $L_1$: point $A(1, 2, 3)$, direction $\vec{u} = (2, 3, 4)$. $L_2$: point $B(4, 5, 6)$, direction $\vec{v} = (3, 4, 5)$. $\vec{AB} = (3, 3, 3)$. $\vec{u} \times \vec{v} = (-1, 2, -1)$. $\vec{AB} \cdot (\vec{u} \times \vec{v}) = 3(-1) + 3(2) + 3(-1) = -3 + 6 - 3 = 0$. Lines intersect! Distance is $0.00 \implies \mathbf{0.00}$.
- **Q46**: $z = 1 + i\sqrt{3} = 2 e^{i\pi/3}$. $z^6 = 2^6 e^{i 2\pi} = 64$. Magnitude is $64.00 \implies \mathbf{64.00}$.
- **Q47**: Circular table with 4 couples alternating men and women: $(4-1)! \times 4! = 6 \times 24 = 144 \implies \mathbf{144.00}$.
- **Q48**: Circle $(x-2)^2 + (y+3)^2 + (z-1)^2 = 11 + 4 + 9 + 1 = 25 \implies R = 5.00 \implies \mathbf{5.00}$.

### Questions 49 to 54
- **Q49**: Rationalizing: $\frac{(\sqrt{1+x} - \sqrt{1-x})(\sqrt{1+x} + \sqrt{1-x})}{x(\sqrt{1+x} + \sqrt{1-x})} = \frac{2x}{x(\sqrt{1+x} + \sqrt{1-x})} = \frac{2}{2} = 1$. **Correct: (A)**.
- **Q50**: $\text{IF} = e^{\int \frac{2}{x} dx} = e^{2\ln x} = x^2$. **Correct: (A)**.
- **Q51**: Line 1: $\frac{x}{1/2} = \frac{y}{1/3} = \frac{z}{-1} \implies \vec{d}_1 = (3, 2, -6)$. Line 2: $\frac{x}{1/6} = \frac{y}{-1} = \frac{z}{-1/4} \implies \vec{d}_2 = (2, -12, -3)$. $\vec{d}_1 \cdot \vec{d}_2 = 3(2) + 2(-12) + (-6)(-3) = 6 - 24 + 18 = 0 \implies 90^\circ$. **Correct: (A)**.
- **Q52**: $\det(2AB) = 2^3 \det(A)\det(B) = 8 \times 2 \times 3 = 48$. **Correct: (A)**.
- **Q53**: $(x-1)^3 = 0 \implies x = 1$ is a triple root, so there is only 1 distinct real root. **Correct: (A)**.
- **Q54**: Favorable outcomes for sum 7: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1) \implies 6$ pairs. $P = 6/36 = 1/6$. **Correct: (A)**.
"""

        raw_sol2 = r"""# Detailed Pedagogical Solutions – JEE Advanced Mock Examination __PAD__ (Paper 2)
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

# PART I: PHYSICS

### Questions 1 to 6
- **Q1**: Sphere rolling and slipping down incline: $f_k = \mu M g \cos\theta$. Center of mass acceleration $a = g(\sin\theta - \mu\cos\theta)$, angular acceleration $\alpha = \frac{5\mu g\cos\theta}{2R}$. Energy dissipated by slipping friction. **Correct Options**: (A, B, C, D)
- **Q2**: Magnus effect and circulation: asymmetric air speeds produce pressure differential via Bernoulli, generating Kutta-Joukowski lift force $F_L = \rho v \Gamma$. **Correct Options**: (A, B, C, D)
- **Q3**: Surface tension force on movable wire: two interfaces give $F_s = 2Tw$. Force is independent of displacement, so motion under perturbation is not SHM. **Correct Options**: (A, B, C, D)
- **Q4**: Potentiometer internal resistance measurement: null condition ensures zero current draw, eliminating internal voltage drop errors. Formula $r = R(l_1/l_2 - 1)$. **Correct Options**: (A, B, C, D)
- **Q5**: Disc colliding with a step: angular momentum conservation about step edge during impact. Kinetic energy threshold for rolling up the step. **Correct Options**: (A, B, C, D)
- **Q6**: Polytropic process molar heat capacity $C = C_V + \frac{R}{1-n}$. Isobaric ($n=0$), isothermal ($n=1$), adiabatic ($n=\gamma$). **Correct Options**: (A, B, C, D)

### Questions 7 to 12
- **Q7**: $r = R\left(\frac{l_1}{l_2} - 1\right) = 10.0\left(\frac{300}{250} - 1\right) = 10.0(1.20 - 1) = 2.0\text{ }\Omega \implies \mathbf{2.00}$.
- **Q8**: $a = g(\sin 37^\circ - \mu_k\cos 37^\circ) = 9.8(0.60 - 0.10 \times 0.80) = 9.8(0.60 - 0.08) = 9.8(0.52) \approx 5.10\text{ m/s}^2 \implies \mathbf{5.10}$.
- **Q9**: $F = 2 T w \implies T = \frac{F}{2w} = \frac{3.5 \times 10^{-3}}{2 \times 0.05} = \frac{3.5 \times 10^{-3}}{0.10} = 0.035\text{ N/m} \implies \mathbf{0.035}$.
- **Q10**: Lift force $F_L = \rho v \Gamma L = (1.20)(15.0)(5.0)(2.0) = 180.0\text{ N} \implies \mathbf{180.00}$.
- **Q11**: $C = C_V + \frac{R}{1-n} = \frac{5}{2}R + \frac{R}{1-2} = \frac{5}{2}R - R = \frac{3}{2}R = 1.50 R \implies |C| = \mathbf{1.50}$.
- **Q12**: Rolling without slipping: $M g h = \frac{7}{10}M v^2 \implies v = \sqrt{\frac{10gh}{7}} = \sqrt{\frac{10 \times 9.8 \times 7.0}{7}} = \sqrt{98} \approx 9.90\text{ m/s} \implies \mathbf{9.90}$.

### Questions 13 to 18
- **Q13**: Center of mass of semicircular wire is at $2R/\pi$. **Correct: (A)**.
- **Q14**: $K = p^2 / (2m) \implies K_1 / K_2 = m_2 / m_1 = 4m / m = 4 / 1$. **Correct: (A)**.
- **Q15**: $3/4$ volume submerged $\implies \rho_{\text{wood}} = \frac{3}{4}\rho_{\text{water}} = 750\text{ kg/m}^3$. **Correct: (A)**.
- **Q16**: Poiseuille flow $Q \propto r^4$. If $r \to r/2$, $Q \to Q / 16$. **Correct: (A)**.
- **Q17**: For harmonic potential $V = \frac{1}{2}kr^2$, orbits are ellipses centered at the origin (center of force). **Correct: (A)**.
- **Q18**: Non-linear triatomic molecule has 3 translational and 3 rotational degrees of freedom $\implies 6$. **Correct: (A)**.

---

# PART II: CHEMISTRY

### Questions 19 to 24
- **Q19**: Carbohydrate oxidation pathways and osazone formation. **Correct Options**: (A, B, C, D)
- **Q20**: Transference numbers and Grotthuss proton-hopping mechanism. **Correct Options**: (A, B, C, D)
- **Q21**: Synthesis and cross-linking of silicones. **Correct Options**: (A, B, C, D)
- **Q22**: Metallurgy of tin and lead. **Correct Options**: (A, B, C, D)
- **Q23**: Conformational analysis of substituted cyclohexanes. **Correct Options**: (A, B, C, D)
- **Q24**: Linear geometries: $\text{BeCl}_2$ ($sp$), $\text{CO}_2$ ($sp$), $\text{C}_2\text{H}_2$ ($sp$). $\text{SO}_2$ is bent. **Correct Options**: (A, B, C)

### Questions 25 to 30
- **Q25**: $[\text{Ag}^+] = \frac{K_{\text{sp}}}{[\text{Cl}^-]} = \frac{1.8 \times 10^{-10}}{0.020} = 9.0 \times 10^{-9}\text{ M} \implies X = \mathbf{9.00}$.
- **Q26**: $[\text{OH}^-] = 2 \times 0.020\text{ M} = 0.040\text{ M} \implies \text{pOH} = -\log(0.040) = 1.40 \implies \text{pH} = 14 - 1.40 = 12.60 \implies \mathbf{12.60}$.
- **Q27**: Nernst equation: $E = E^\circ - \frac{0.0591}{6}\log\left(\frac{1}{[\text{H}^+]^{14}}\right) = 1.33 - \frac{0.0591 \times 14}{6}\text{pH} = 1.33 - 0.1379(2.0) = 1.33 - 0.28 = 1.05\text{ V} \implies \mathbf{1.05}$.
- **Q28**: 2 half-lives: $t = 2 \times 20.0 = 40.0\text{ days} \implies \mathbf{40.00}$.
- **Q29**: $\Delta T_f = i K_f m \implies 0.372 = i (1.86)(0.10) \implies i = \frac{0.372}{0.186} = 2.00 \implies N = \mathbf{2.00}$.
- **Q30**: In $\text{Na}_2\text{S}_2\text{O}_4$, $2(+1) + 2x + 4(-2) = 0 \implies 2x - 6 = 0 \implies x = +3 \implies \mathbf{3.00}$.

### Questions 31 to 36
- **Q31**: Toluene contains benzylic $\alpha$-hydrogens, oxidizing to benzoic acid. *tert*-Butylbenzene lacks $\alpha$-hydrogens. **Correct: (A)**.
- **Q32**: Isoelectronic series: ionic radius decreases as nuclear charge increases: $\text{N}^{3-} > \text{O}^{2-} > \text{F}^- > \text{Na}^+ > \text{Mg}^{2+} > \text{Al}^{3+}$. **Correct: (A)**.
- **Q33**: $\text{ClO}_3^-$ has 3 bond pairs and 1 lone pair $\implies sp^3$ trigonal pyramidal. **Correct: (A)**.
- **Q34**: Phenol reacts with neutral $\text{FeCl}_3$ to produce a characteristic violet-colored complex. **Correct: (A)**.
- **Q35**: Sucrose features an $\alpha(1\to 2)\beta$ glycosidic bond between $\alpha$-D-glucose and $\beta$-D-fructose. **Correct: (A)**.
- **Q36**: Water is a weak field ligand; $\text{Fe}^{2+}$ ($d^6$) forms high-spin outer orbital complex with $sp^3d^2$ hybridization. **Correct: (A)**.

---

# PART III: MATHEMATICS

### Questions 37 to 42
- **Q37**: Properties of hyperbolic tangent $\tanh x$. **Correct Options**: (A, B, C, D)
- **Q38**: Properties of nilpotent matrices: eigenvalues 0, trace and det 0, index $k \le n$, $(I+A)^{-1} = I - A + A^2$. **Correct Options**: (A, B, C, D)
- **Q39**: Coaxial family of circles passing through two points. **Correct Options**: (A, B, C, D)
- **Q40**: Beta function integrals and transformations. **Correct Options**: (A, B, C, D)
- **Q41**: Coplanar vectors and scalar triple products. **Correct Options**: (A, B, C, D)
- **Q42**: Trigonometric linear combinations and extrema. **Correct Options**: (A, B, C, D)

### Questions 43 to 48
- **Q43**: Loop exists for $x \in [0, 2]$. $y = \pm (2-x)\sqrt{x}$. Area $= 2 \int_0^2 (2\sqrt{x} - x^{3/2})dx = 2 [\frac{4}{3}x^{3/2} - \frac{2}{5}x^{5/2}]_0^2 = 2 [\frac{4}{3}(2\sqrt{2}) - \frac{2}{5}(4\sqrt{2})] = 2\sqrt{2}[\frac{8}{3} - \frac{8}{5}] = 2\sqrt{2}(\frac{16}{15}) = \frac{32\sqrt{2}}{15} \approx \frac{45.25}{15} \approx 3.02 \implies \mathbf{3.02}$.
- **Q44**: $3^2 = 9 \equiv 1 \pmod 8$. $2025 = 2 \times 1012 + 1$. $3^{2025} \equiv (3^2)^{1012} \times 3 \equiv 1 \times 3 \equiv 3 \pmod 8 \implies \mathbf{3.00}$.
- **Q45**: $d = \frac{|2(3) + 4 - 2(5) + 9|}{\sqrt{2^2 + 1^2 + (-2)^2}} = \frac{|6 + 4 - 10 + 9|}{\sqrt{9}} = \frac{9}{3} = 3.00 \implies \mathbf{3.00}$.
- **Q46**: $\alpha + \beta = 5$, $\alpha\beta = 3$. $\alpha^3 + \beta^3 = (\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta) = 5^3 - 3(3)(5) = 125 - 45 = 80.00 \implies \mathbf{80.00}$.
- **Q47**: Diagonals $= \frac{n(n-3)}{2} = \frac{10 \times 7}{2} = 35 \implies \mathbf{35.00}$.
- **Q48**: Circle $(x+5)^2 + (y-3)^2 = 25 + 9 - 9 = 25 \implies R = 5.00 \implies \mathbf{5.00}$.

### Questions 49 to 54
- **Q49**: $\frac{\cos x - \sin x}{\cos x + \sin x} = \frac{1 - \tan x}{1 + \tan x} = \tan(\pi/4 - x)$. Thus $\arctan(\dots) = \pi/4 - x$. Derivative is $-1$. **Correct: (A)**.
- **Q50**: $\frac{dy}{dx} = \frac{e^x}{e^y} \implies e^y dy = e^x dx \implies e^y = e^x + C$. **Correct: (A)**.
- **Q51**: $\frac{x^2}{16} + \frac{y^2}{9} = 1 \implies a^2 = 16 \implies a = 4$. Major axis length $= 2a = 8$. **Correct: (A)**.
- **Q52**: $x - 1 = 2^3 = 8 \implies x = 9$. **Correct: (A)**.
- **Q53**: $\sin(15^\circ) = \sin(45^\circ - 30^\circ) = \frac{\sqrt{6}-\sqrt{2}}{4} = \frac{\sqrt{3}-1}{2\sqrt{2}}$. Both (A) and (C) are identical. **Correct: (A)**.
- **Q54**: 13 spades and 3 other aces $= 16$ cards. $P = 16/52 = 4/13$. **Correct: (A)**.
"""

        raw_val = r"""# Comprehensive Answer Key & Academic Alignment Validation – JEE Advanced Mock Examination __PAD__
## Organising Institute Style Inspiration: IIT Roorkee (`IIT_ROORKEE_STYLE`)

---

### Master Answer Key – Paper 1
| Q# | Subject | Section | Question Type | Key |
|---|---|---|---|---|
| 1 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 2 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 3 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 4 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 5 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 6 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 7 | Physics | Sec 2 | Numerical | 288.00 |
| 8 | Physics | Sec 2 | Numerical | 5231.00 |
| 9 | Physics | Sec 2 | Numerical | 1.50 |
| 10 | Physics | Sec 2 | Numerical | 0.81 |
| 11 | Physics | Sec 2 | Numerical | 1.02 |
| 12 | Physics | Sec 2 | Numerical | 100.00 |
| 13 | Physics | Sec 3 | Single Correct | A |
| 14 | Physics | Sec 3 | Single Correct | A |
| 15 | Physics | Sec 3 | Single Correct | A |
| 16 | Physics | Sec 3 | Single Correct | A |
| 17 | Physics | Sec 3 | Single Correct | A |
| 18 | Physics | Sec 3 | Single Correct | A |
| 19 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 20 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 21 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 22 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 23 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C |
| 25 | Chemistry | Sec 2 | Numerical | 10.46 |
| 26 | Chemistry | Sec 2 | Numerical | 875.00 |
| 27 | Chemistry | Sec 2 | Numerical | 7.78 |
| 28 | Chemistry | Sec 2 | Numerical | 3.00 |
| 29 | Chemistry | Sec 2 | Numerical | 4.00 |
| 30 | Chemistry | Sec 2 | Numerical | 7.00 |
| 31 | Chemistry | Sec 3 | Single Correct | A |
| 32 | Chemistry | Sec 3 | Single Correct | A |
| 33 | Chemistry | Sec 3 | Single Correct | A |
| 34 | Chemistry | Sec 3 | Single Correct | A |
| 35 | Chemistry | Sec 3 | Single Correct | A |
| 36 | Chemistry | Sec 3 | Single Correct | A |
| 37 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 38 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 39 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 40 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 41 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C |
| 42 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 43 | Mathematics | Sec 2 | Numerical | 2.00 |
| 44 | Mathematics | Sec 2 | Numerical | 41.00 |
| 45 | Mathematics | Sec 2 | Numerical | 0.00 |
| 46 | Mathematics | Sec 2 | Numerical | 64.00 |
| 47 | Mathematics | Sec 2 | Numerical | 144.00 |
| 48 | Mathematics | Sec 2 | Numerical | 5.00 |
| 49 | Mathematics | Sec 3 | Single Correct | A |
| 50 | Mathematics | Sec 3 | Single Correct | A |
| 51 | Mathematics | Sec 3 | Single Correct | A |
| 52 | Mathematics | Sec 3 | Single Correct | A |
| 53 | Mathematics | Sec 3 | Single Correct | A |
| 54 | Mathematics | Sec 3 | Single Correct | A |

---

### Master Answer Key – Paper 2
| Q# | Subject | Section | Question Type | Key |
|---|---|---|---|---|
| 1 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 2 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 3 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 4 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 5 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 6 | Physics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 7 | Physics | Sec 2 | Numerical | 2.00 |
| 8 | Physics | Sec 2 | Numerical | 5.10 |
| 9 | Physics | Sec 2 | Numerical | 0.035 |
| 10 | Physics | Sec 2 | Numerical | 180.00 |
| 11 | Physics | Sec 2 | Numerical | 1.50 |
| 12 | Physics | Sec 2 | Numerical | 9.90 |
| 13 | Physics | Sec 3 | Single Correct | A |
| 14 | Physics | Sec 3 | Single Correct | A |
| 15 | Physics | Sec 3 | Single Correct | A |
| 16 | Physics | Sec 3 | Single Correct | A |
| 17 | Physics | Sec 3 | Single Correct | A |
| 18 | Physics | Sec 3 | Single Correct | A |
| 19 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 20 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 21 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 22 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 23 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C, D |
| 24 | Chemistry | Sec 1 | One or More Than One Correct | A, B, C |
| 25 | Chemistry | Sec 2 | Numerical | 9.00 |
| 26 | Chemistry | Sec 2 | Numerical | 12.60 |
| 27 | Chemistry | Sec 2 | Numerical | 1.05 |
| 28 | Chemistry | Sec 2 | Numerical | 40.00 |
| 29 | Chemistry | Sec 2 | Numerical | 2.00 |
| 30 | Chemistry | Sec 2 | Numerical | 3.00 |
| 31 | Chemistry | Sec 3 | Single Correct | A |
| 32 | Chemistry | Sec 3 | Single Correct | A |
| 33 | Chemistry | Sec 3 | Single Correct | A |
| 34 | Chemistry | Sec 3 | Single Correct | A |
| 35 | Chemistry | Sec 3 | Single Correct | A |
| 36 | Chemistry | Sec 3 | Single Correct | A |
| 37 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 38 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 39 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 40 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 41 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 42 | Mathematics | Sec 1 | One or More Than One Correct | A, B, C, D |
| 43 | Mathematics | Sec 2 | Numerical | 3.02 |
| 44 | Mathematics | Sec 2 | Numerical | 3.00 |
| 45 | Mathematics | Sec 2 | Numerical | 3.00 |
| 46 | Mathematics | Sec 2 | Numerical | 80.00 |
| 47 | Mathematics | Sec 2 | Numerical | 35.00 |
| 48 | Mathematics | Sec 2 | Numerical | 5.00 |
| 49 | Mathematics | Sec 3 | Single Correct | A |
| 50 | Mathematics | Sec 3 | Single Correct | A |
| 51 | Mathematics | Sec 3 | Single Correct | A |
| 52 | Mathematics | Sec 3 | Single Correct | A |
| 53 | Mathematics | Sec 3 | Single Correct | A |
| 54 | Mathematics | Sec 3 | Single Correct | A |
"""

        p1 = raw_p1.replace("__PAD__", pad)
        p2 = raw_p2.replace("__PAD__", pad)
        sol1 = raw_sol1.replace("__PAD__", pad)
        sol2 = raw_sol2.replace("__PAD__", pad)
        val = raw_val.replace("__PAD__", pad)

        create_mock_files(mock_idx, p1, p2, sol1, sol2, val, "IIT_Roorkee")
        print(f"Generated IIT Roorkee Mock {pad}!")

if __name__ == "__main__":
    generate_roorkee_11_to_15()

