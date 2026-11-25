# -*- coding: utf-8 -*-
"""
Script to generate engine/neet_engine/curriculum_physics_diff.py
Tier 3: Difficult / 2026-2027 Advanced Predicted Rigor
Physics Curriculum (50 Questions)
"""
import os

code = '''# -*- coding: utf-8 -*-
"""
NEET Mock Generation Engine - Difficult Curriculum (Physics)
Strictly calibrated to NTA NEET-UG standards (2023-2027 Predictive Rigor).
Difficult conceptual and analytical depth: multi-stage calculations,
boundary conditions, non-inertial frames, real instruments with zero errors,
composite systems, and subtle distractor traps. Strictly NCERT-aligned.

Proportions for 50 Questions:
- Direct MCQ: 29
- Statement I & II: 7
- Match List: 7
- Assertion & Reason: 4
- Multi-Statement: 3
Total: 50
"""
from neet_models import NeetQuestion

def get_physics_questions_diff(mock_num):
    questions = []

    # Shift / cycle parameter to dynamically vary question sequence across Mocks 41-60
    # Every mock begins with a different conceptual domain
    shift = (mock_num - 41) * 3

    topics_data = [
        # 1. Units, Dimensions & Instruments (Screw Gauge Zero Error) - Match List
        ("Units, Dimensions and Experimental Error", "Screw Gauge Pitch and Negative Zero Error Analysis", "Match List",
         "Match List-I with List-II for precision measurement instruments and their characteristics:\\n\\n"
         "| List-I (Measurement Scenario) | List-II (True Specification / Value) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Screw gauge: Pitch $0.5\\\\text{ mm}$, $100$ circular divisions | **I.** Least count $= 0.005\\\\text{ mm}$ |\\n"
         "| **B.** Vernier callipers: $20$ VSD $= 19$ MSD ($1\\\\text{ MSD} = 1\\\\text{ mm}$) | **II.** Least count $= 0.05\\\\text{ mm}$ |\\n"
         "| **C.** Negative zero error ($5$ div below reference) on pitch $1\\\\text{ mm}$, $100$ div | **III.** Correction to be added $= +0.05\\\\text{ mm}$ |\\n"
         "| **D.** Spherometer: Pitch $1\\\\text{ mm}$, $200$ circular divisions | **IV.** Least count $= 0.005\\\\text{ mm}$ |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Screw gauge Least Count $= \\\\frac{\\\\text{Pitch}}{\\\\text{Total circular divisions}} = \\\\frac{0.5\\\\text{ mm}}{100} = 0.005\\\\text{ mm} \\\\to$ I.\\n2. Vernier callipers Least Count $= 1\\\\text{ MSD} - 1\\\\text{ VSD} = \\\\left(1 - \\\\frac{19}{20}\\\\right)(1\\\\text{ mm}) = 0.05\\\\text{ mm} \\\\to$ II.\\n3. Negative zero error means the zero mark of circular scale lies above reference line, reading $-5\\\\text{ div} \\\\times 0.01\\\\text{ mm} = -0.05\\\\text{ mm}$. True reading requires adding the zero correction: $+0.05\\\\text{ mm} \\\\to$ III.\\n4. Spherometer Least Count $= \\\\frac{1\\\\text{ mm}}{200} = 0.005\\\\text{ mm} \\\\to$ IV.",
         "Distractors confuse positive error (subtracted) with negative zero error (added).",
         "Zero correction is always the negative of zero error: $\\\\text{True Reading} = \\\\text{Observed} - (\\\\text{Zero Error})$."),

        # 2. Kinematics - Variable Acceleration
        ("Motion in a Straight Line and Graphs", "Variable Deceleration and Stopping Distance", "Direct MCQ",
         "A vehicle moves along a straight road with velocity $v$. It experiences a resistive retarding force producing deceleration proportional to the square of its speed: $a = -k v^2$, where $k$ is a positive dimensional constant. If its initial velocity at $t = 0$ is $v_0$, the distance $s$ traversed before its velocity drops to $\\\\frac{v_0}{2}$ is:",
         ["$\\\\frac{\\\\ln 2}{k}$", "$\\\\frac{1}{2k}$", "$\\\\frac{v_0}{2k}$", "$\\\\frac{\\\\ln 4}{k}$"], 0,
         "1. Using $a = v \\\\frac{dv}{ds} = -k v^2$.\\n2. Separating variables: $\\\\frac{dv}{v} = -k ds$.\\n3. Integrating from $v = v_0$ to $v = v_0/2$ over distance $s$:\\n   $$\\\\int_{v_0}^{v_0/2} \\\\frac{dv}{v} = -k \\\\int_0^s ds\\\\implies \\\\left[\\\\ln v\\\\right]_{v_0}^{v_0/2} = -ks$.\\n4. $\\\\ln\\\\left(\\\\frac{v_0/2}{v_0}\\\\right) = \\\\ln\\\\left(\\\\frac{1}{2}\\\\right) = -\\\\ln 2 = -ks \\\\implies s = \\\\frac{\\\\ln 2}{k}$.",
         "1/(2k) neglects the logarithmic integral $\\\\int v^{-1} dv$; ln(4)/k assumes full stop.",
         "When deceleration is proportional to $v^2$, distance follows $s = \\\\frac{1}{k}\\\\ln(v_i/v_f)$."),

        # 3. Kinematics - Relative Motion
        ("Motion in a Plane and Vectors", "Rain-Man Problem on Inclined Ground", "Direct MCQ",
         "Rain is falling vertically downwards with speed $v_r = 30\\\\text{ m/s}$. A cyclist rides up an inclined road of angle $30^\\\\circ$ with the horizontal at speed $v_c = 20\\\\text{ m/s}$. To protect himself from the rain, at what angle $\\\\theta$ with the vertical should he hold his umbrella?",
         ["$\\\\tan^{-1}\\\\left(\\\\frac{\\\\sqrt{3}}{4}\\\\right)$ forward", "$\\\\tan^{-1}\\\\left(\\\\frac{1}{2}\\\\right)$ backward", "$\\\\tan^{-1}\\\\left(\\\\frac{1}{4}\\\\right)$ forward", "$30^\\\\circ$ forward"], 0,
         "1. Velocity of rain: $\\\\vec{v}_r = -30\\\\hat{j}$.\\n2. Velocity of cyclist up the incline: $\\\\vec{v}_c = (20\\\\cos 30^\\\\circ)\\\\hat{i} + (20\\\\sin 30^\\\\circ)\\\\hat{j} = 10\\\\sqrt{3}\\\\hat{i} + 10\\\\hat{j}$.\\n3. Relative velocity of rain with respect to cyclist:\\n   $$\\\\vec{v}_{r/c} = \\\\vec{v}_r - \\\\vec{v}_c = -30\\\\hat{j} - (10\\\\sqrt{3}\\\\hat{i} + 10\\\\hat{j}) = -10\\\\sqrt{3}\\\\hat{i} - 40\\\\hat{j}$.\\n4. The angle $\\\\theta$ with the vertical is given by:\\n   $$\\\\tan\\\\theta = \\\\frac{|v_x|}{|v_y|} = \\\\frac{10\\\\sqrt{3}}{40} = \\\\frac{\\\\sqrt{3}}{4}$.\\n5. Thus, $\\\\theta = \\\\tan^{-1}\\\\left(\\\\frac{\\\\sqrt{3}}{4}\\\\right)$ forward.",
         "Neglecting the vertical component of the cyclist's velocity leads to $\\\\tan\\\\theta = \\\\sqrt{3}/3 = 30^\\\\circ$.",
         "Relative velocity $\\\\vec{v}_{r/m} = \\\\vec{v}_r - \\\\vec{v}_m$ accounts for both horizontal and vertical motion of observer."),

        # 4. Laws of Motion - Two Block Friction
        ("Laws of Motion and Friction", "Two-Block System Maximum Accelerating Force", "Direct MCQ",
         "Block $A$ of mass $m_A = 2\\\\text{ kg}$ rests on top of block $B$ of mass $m_B = 4\\\\text{ kg}$. The coefficient of static friction between $A$ and $B$ is $\\\\mu_s = 0.4$. The surface below block $B$ is completely frictionless. If acceleration due to gravity is $g = 10\\\\text{ m/s}^2$, the maximum horizontal force $F$ applied directly on block $B$ such that block $A$ does not slip on $B$ is:",
         ["$24\\\\text{ N}$", "$16\\\\text{ N}$", "$8\\\\text{ N}$", "$36\\\\text{ N}$"], 0,
         "1. Maximum static friction force between $A$ and $B$: $f_{s,\\\\max} = \\\\mu_s m_A g = 0.4 \\\\times 2 \\\\times 10 = 8\\\\text{ N}$.\\n2. The only force accelerating block $A$ horizontally is this friction force: $f_s = m_A a \\\\implies a_{\\\\max} = \\\\frac{f_{s,\\\\max}}{m_A} = \\\\frac{8}{2} = 4\\\\text{ m/s}^2$.\\n3. Both blocks move together as a single combined system of total mass $M = m_A + m_B = 2 + 4 = 6\\\\text{ kg}$.\\n4. Maximum applied force on $B$: $F_{\\\\max} = (m_A + m_B) a_{\\\\max} = 6 \\\\times 4 = 24\\\\text{ N}$.",
         "8 N is the friction limit itself; 16 N considers only block B accelerating.",
         "For multi-block systems, determine the maximum acceleration the non-driven block can sustain without slipping."),

        # 5. Work, Energy & Power - Vertical Circle Slackening
        ("Work, Energy and Power", "Vertical Circular Motion Slackening Condition", "Direct MCQ",
         "A small bob of mass $m$ attached to a light inextensible string of length $L$ is projected horizontally from its lowest point with speed $u = \\\\sqrt{4 g L}$. The string slackens (tension becomes zero) at an angle $\\\\theta$ with the upward vertical. The value of $\\\\cos\\\\theta$ is:",
         ["$1/3$", "$2/3$", "$1/2$", "$1/4$"], 0,
         "1. Let the string slacken at height $h$ above the lowest point. Here $h = L(1 + \\\\cos\\\\theta)$, where $\\\\theta$ is angle with upward vertical.\\n2. Using conservation of mechanical energy: $\\\\frac{1}{2}m u^2 = \\\\frac{1}{2}m v^2 + mgh \\\\implies v^2 = u^2 - 2gh = 4gL - 2gL(1 + \\\\cos\\\\theta) = 2gL(1 - \\\\cos\\\\theta)$.\\n3. Tension in string at this point: $T + mg\\\\cos\\\\theta = \\\\frac{m v^2}{L}$.\\n4. At the point of slackening, $T = 0 \\\\implies mg\\\\cos\\\\theta = \\\\frac{m v^2}{L} \\\\implies v^2 = gL\\\\cos\\\\theta$.\\n5. Equating the two expressions for $v^2$:\\n   $$gL\\\\cos\\\\theta = 2gL(1 - \\\\cos\\\\theta) \\\\implies \\\\cos\\\\theta = 2 - 2\\\\cos\\\\theta \\\\implies 3\\\\cos\\\\theta = 1 \\\\implies \\\\cos\\\\theta = \\\\frac{1}{3}$$.",
         "cos(theta) = 2/3 assumes projection velocity is $\\\\sqrt{3gL}$.",
         "String slackens when radial component of gravity provides the necessary centripetal force: $v^2 = gL\\\\cos\\\\theta$."),

        # 6. Rotational Motion - Pure Rolling on Incline (Multi-Statement)
        ("System of Particles and Rotational Motion", "Pure Rolling Acceleration and Critical Friction", "Multi-Statement",
         "Consider a solid cylinder, a solid sphere, and a thin hollow sphere, each of identical mass $M$ and radius $R$, released from rest at the top of a rough inclined plane of inclination $\\\\theta$. Given that all three roll down without slipping:\\n\\n"
         "A. The acceleration of the center of mass is greatest for the solid sphere.\\n"
         "B. The frictional force acting on the body during pure rolling does negative work.\\n"
         "C. The minimum coefficient of static friction $\\\\mu_{\\\\min}$ required to prevent slipping is greatest for the hollow sphere.\\n"
         "D. The total mechanical energy is conserved during pure rolling.\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A, C, and D only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. Acceleration during pure rolling: $a = \\\\frac{g\\\\sin\\\\theta}{1 + k^2/R^2}$. For solid sphere $k^2/R^2 = 2/5 = 0.4$; solid cylinder $k^2/R^2 = 0.5$; hollow sphere $k^2/R^2 = 2/3 \\\\approx 0.67$. Solid sphere has smallest $k^2/R^2$, hence greatest acceleration ($a = \\\\frac{5}{7}g\\\\sin\\\\theta$). Statement A is TRUE.\\n2. In pure rolling, the instantaneous point of contact is at rest ($v_{\\\\text{contact}} = 0$). Therefore, the static friction does zero work ($W_f = 0$). Statement B is FALSE.\\n3. Minimum friction to prevent slipping: $\\\\mu_{\\\\min} = \\\\frac{\\\\tan\\\\theta}{1 + R^2/k^2}$. For hollow sphere, $R^2/k^2 = 1.5$ (smallest denominator), giving the largest $\\\\mu_{\\\\min} = \\\\frac{2}{5}\\\\tan\\\\theta$. Statement C is TRUE.\\n4. Since static friction does no work and no other dissipative forces act, mechanical energy is conserved. Statement D is TRUE.",
         "Static friction in pure rolling does no work because instantaneous point of contact has zero displacement.",
         "Pure rolling conserves total mechanical energy; acceleration $a = \\\\frac{g\\\\sin\\\\theta}{1 + I/(MR^2)}$."),

        # 7. Centre of Mass & Cavity - Match List
        ("System of Particles and Rotational Motion", "Spherical Cavity Center of Mass and Gravitational Field", "Match List",
         "Match List-I with List-II for a solid uniform sphere of radius $R$ and mass $M$ from which a spherical cavity of radius $R/2$ is carved out touching the outer surface:\\n\\n"
         "| List-I (Physical Quantity) | List-II (Value / Characteristic) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Mass of the carved-out cavity material | **I.** $M/8$ |\\n"
         "| **B.** Shift of the center of mass of remaining portion | **II.** $R/14$ towards opposite side |\\n"
         "| **C.** Gravitational field inside the spherical cavity | **III.** Uniform and non-zero |\\n"
         "| **D.** Moment of inertia of carved-out part about sphere center | **IV.** $\\\\frac{3}{40} M R^2$ |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-IV, B-II, C-III, D-I"], 0,
         "1. Volume of sphere $\\\\propto R^3$. Radius of cavity is $R/2$, so volume is $(1/2)^3 = 1/8$ of original. Thus, mass of cavity material $m = M/8 \\\\to$ I.\\n2. Using negative mass method: $x_{\\\\text{cm}} = \\\\frac{M(0) - (M/8)(R/2)}{M - M/8} = \\\\frac{-M R / 16}{7M / 8} = -\\\\frac{R}{14} \\\\to$ II.\\n3. Gravitational field inside a spherical cavity carved out of a uniform sphere is uniform in magnitude and direction: $\\\\vec{E} = -\\\\frac{4}{3}\\\\pi G \\\\rho \\\\vec{d} \\\\to$ III.\\n4. By parallel-axis theorem: $I_{\\\\text{cavity}} = I_{\\\\text{cm}} + m d^2 = \\\\frac{2}{5}m (R/2)^2 + m (R/2)^2 = \\\\frac{7}{5}m \\\\frac{R^2}{4} = \\\\frac{7}{20}\\\\left(\\\\frac{M}{8}\\\\right)R^2 = \\\\frac{7}{160} M R^2$.",
         "Distractors confuse shift with $R/6$ (which applies to a 2D cut-out disc, not a 3D sphere).",
         "Gravitational and electrostatic fields inside an off-center spherical cavity are strictly uniform!"),

        # 8. Angular Momentum Conservation - Assertion & Reason
        ("System of Particles and Rotational Motion", "Angular Momentum and Kinetic Energy Increase", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\n"
         "Assertion (A): When a rotating ballet dancer pulls her arms inward, her angular velocity increases and her rotational kinetic energy also increases.\\n"
         "Reason (R): The increase in rotational kinetic energy comes from the internal muscular work done by the dancer in pulling her arms inward.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. External torque $\\\\tau_{\\\\text{ext}} = 0$, so angular momentum $L = I \\\\omega$ is conserved.\\n2. Pulling arms inward decreases moment of inertia ($I_2 < I_1$). Since $L$ is constant, $\\\\omega_2 = \\\\frac{L}{I_2} > \\\\omega_1$. Angular velocity increases.\\n3. Rotational kinetic energy $K = \\\\frac{L^2}{2I}$. As $I$ decreases, $K$ increases ($K_2 > K_1$). Assertion is TRUE.\\n4. The additional kinetic energy is generated by the positive mechanical work done by the dancer's muscles against the centripetal (inertial centrifugal) forces. Reason is TRUE and explains Assertion.",
         "Students often wonder where the extra energy comes from; it comes from biological chemical energy converted via muscular work.",
         "Conservation of angular momentum does NOT imply conservation of rotational kinetic energy when internal work is performed."),

        # 9. Gravitation - Tunnel Through Earth (Statement I & II)
        ("Gravitation and Planetary Motion", "SHM Motion of Body in Diametrical Earth Tunnel", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "Statement I: If a non-diametrical straight smooth tunnel is drilled through the Earth, a particle dropped into the tunnel executes simple harmonic motion with a time period identical to that for a diametrical tunnel ($T \\\\approx 84.6\\\\text{ minutes}$).\\n\\n"
         "Statement II: The restoring force acting on the particle along the tunnel is directly proportional to its distance from the midpoint of the tunnel, with effective force constant $k = \\\\frac{G M m}{R^3}$.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. For any chord tunnel at distance $d$ from the center, let $x$ be displacement of particle from tunnel midpoint.\\n2. The radial distance from center is $r = \\\\sqrt{x^2 + d^2}$. Gravitational force at distance $r$ inside uniform Earth is $F_r = \\\\frac{GMm}{R^3} r$.\\n3. Component along tunnel: $F_x = -F_r \\\\cos\\\\theta = -\\\\left(\\\\frac{GMm}{R^3} r\\\\right)\\\\left(\\\\frac{x}{r}\\\\right) = -\\\\frac{GMm}{R^3} x$.\\n4. The restoring force is strictly $-k x$ with $k = \\\\frac{GMm}{R^3}$, independent of chord distance $d$.\\n5. Period $T = 2\\\\pi\\\\sqrt{\\\\frac{m}{k}} = 2\\\\pi\\\\sqrt{\\\\frac{R^3}{GM}} = 2\\\\pi\\\\sqrt{\\\\frac{R}{g}} \\\\approx 84.6\\\\text{ min}$. Both statements are correct.",
         "Many students incorrectly believe that non-diametrical tunnels have a different oscillation period.",
         "The oscillation period in ANY frictionless straight tunnel through uniform Earth is invariant: $T = 2\\\\pi\\\\sqrt{R/g} \\\\approx 84.6\\\\text{ min}$."),

        # 10. Gravitation - Launch Velocity and Maximum Height
        ("Gravitation and Planetary Motion", "Projectile Launch at Fraction of Escape Velocity", "Direct MCQ",
         "A projectile is fired vertically upwards from the surface of the Earth with a speed equal to half the escape velocity ($v = \\\\frac{1}{2} v_e$). Neglecting air resistance, the maximum height $h$ attained by the projectile above the Earth's surface (in terms of radius of Earth $R$) is:",
         ["$R / 3$", "$R / 2$", "$R / 4$", "$2 R / 3$"], 0,
         "1. Escape velocity is given by $v_e = \\\\sqrt{\\\\frac{2 G M}{R}}$.\\n2. Launch speed $v = \\\\frac{v_e}{2} \\\\implies v^2 = \\\\frac{v_e^2}{4} = \\\\frac{2 G M}{4 R} = \\\\frac{G M}{2 R}$.\\n3. Conserving mechanical energy between surface ($r = R$) and maximum height ($r = R + h$, where $v_f = 0$):\\n   $$\\\\frac{1}{2} m v^2 - \\\\frac{G M m}{R} = 0 - \\\\frac{G M m}{R + h}$$.\\n4. Substituting $v^2$:\\n   $$\\\\frac{1}{2} m \\\\left(\\\\frac{G M}{2 R}\\\\right) - \\\\frac{G M m}{R} = -\\\\frac{G M m}{R + h} \\\\implies \\\\frac{1}{4 R} - \\\\frac{1}{R} = -\\\\frac{1}{R + h}$.\\n5. $-\\\\frac{3}{4 R} = -\\\\frac{1}{R + h} \\\\implies 3(R + h) = 4 R \\\\implies 3h = R \\\\implies h = \\\\frac{R}{3}$.",
         "Using flat Earth formula $h = v^2/(2g)$ gives $h = R/4$, which is invalid for high altitudes.",
         "At cosmic launch speeds, always use universal gravitational potential energy $-GMm/r$ rather than $mgh$."),

        # 11. Mechanical Properties of Solids - Thermal Stress
        ("Mechanical Properties of Solids and Elasticity", "Thermal Stress and Clamped Rod Force", "Direct MCQ",
         "A steel rod of cross-sectional area $A = 2\\\\text{ cm}^2$ and length $L = 1\\\\text{ m}$ is clamped rigidly between two unyielding fixed walls at temperature $20^\\\\circ\\\\text{C}$. If the temperature is increased to $70^\\\\circ\\\\text{C}$, the compressive force developed in the rod is: (Given: Young\\'s modulus $Y = 2 \\\\times 10^{11}\\\\text{ N/m}^2$, coefficient of linear expansion $\\\\alpha = 1.2 \\\\times 10^{-5}\\\\text{ K}^{-1}$)",
         ["$2.4 \\\\times 10^4\\\\text{ N}$", "$1.2 \\\\times 10^4\\\\text{ N}$", "$4.8 \\\\times 10^4\\\\text{ N}$", "$2.4 \\\\times 10^5\\\\text{ N}$"], 0,
         "1. Increase in temperature: $\\\\Delta T = 70 - 20 = 50^\\\\circ\\\\text{C} = 50\\\\text{ K}$.\\n2. Free thermal expansion prevented by walls: $\\\\Delta L_{\\\\text{thermal}} = L \\\\alpha \\\\Delta T$.\\n3. Compressive strain produced: $\\\\frac{\\\\Delta L}{L} = \\\\alpha \\\\Delta T = (1.2 \\\\times 10^{-5})(50) = 6.0 \\\\times 10^{-4}$.\\n4. Compressive stress: $\\\\sigma = Y \\\\times \\\\text{strain} = (2 \\\\times 10^{11})(6.0 \\\\times 10^{-4}) = 1.2 \\\\times 10^8\\\\text{ N/m}^2$.\\n5. Compressive force on walls: $F = \\\\sigma A = (1.2 \\\\times 10^8\\\\text{ N/m}^2)(2 \\\\times 10^{-4}\\\\text{ m}^2) = 2.4 \\\\times 10^4\\\\text{ N}$.",
         "Unit conversion error in $A$: $2\\\\text{ cm}^2 = 2 \\\\times 10^{-4}\\\\text{ m}^2$, not $2 \\\\times 10^{-2}\\\\text{ m}^2$.",
         "Thermal force $F = Y A \\\\alpha \\\\Delta T$ is independent of the original length $L$ of the rod."),

        # 12. Fluid Mechanics - Efflux Range
        ("Mechanical Properties of Fluids", "Torricelli Efflux and Horizontal Jet Range", "Direct MCQ",
         "A cylindrical water tank of height $H$ is filled completely with water. A small hole is punched in its side wall at a depth $h$ below the free surface. The horizontal distance from the base of the tank where the water jet strikes the ground is maximum when $h$ equals:",
         ["$H / 2$", "$H / 4$", "$H / 3$", "$2 H / 3$"], 0,
         "1. Speed of efflux by Torricelli\\'s law: $v = \\\\sqrt{2gh}$.\\n2. The water jet falls through vertical height $(H - h)$ to reach the ground.\\n3. Time of flight: $t = \\\\sqrt{\\\\frac{2(H - h)}{g}}$.\\n4. Horizontal range $R = v \\\\times t = \\\\sqrt{2gh} \\\\times \\\\sqrt{\\\\frac{2(H - h)}{g}} = 2\\\\sqrt{h(H - h)}$.\\n5. To maximize $R$, maximize $f(h) = h(H - h) = Hh - h^2$. Differentiating with respect to $h$:\\n   $$\\\\frac{df}{dh} = H - 2h = 0 \\\\implies h = \\\\frac{H}{2}$$.\\n6. The maximum horizontal range is $R_{\\\\max} = 2\\\\sqrt{(H/2)(H/2)} = H$.",
         "H/4 is a distractor; H/2 gives equal travel times and maximum geometric product.",
         "Maximum horizontal efflux range $R_{\\\\max} = H$ occurs when the orifice is at the midpoint $h = H/2$."),

        # 13. Viscosity - Raindrop Terminal Velocity with Buoyancy (Statement I & II)
        ("Mechanical Properties of Fluids", "Stokes Law Terminal Velocity Buoyancy Dependence", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "Statement I: For a spherical body of radius $r$ and density $\\\\rho$ falling through a fluid of density $\\\\sigma$ and viscosity $\\\\eta$, the terminal velocity is directly proportional to $r^2$ and $(\\\\rho - \\\\sigma)$.\\n\\n"
         "Statement II: If the density of the falling body is less than the density of the surrounding fluid ($\\\\rho < \\\\sigma$), the terminal velocity is negative, meaning the body rises upwards with terminal speed.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. At terminal velocity, Net Force $= 0 \\\\implies W = F_B + F_v$, where $W = \\\\frac{4}{3}\\\\pi r^3 \\\\rho g$, $F_B = \\\\frac{4}{3}\\\\pi r^3 \\\\sigma g$, and $F_v = 6\\\\pi \\\\eta r v_t$.\\n2. $6\\\\pi \\\\eta r v_t = \\\\frac{4}{3}\\\\pi r^3 (\\\\rho - \\\\sigma) g \\\\implies v_t = \\\\frac{2}{9}\\\\frac{r^2 (\\\\rho - \\\\sigma) g}{\\\\eta}$. Statement I is correct.\\n3. When $\\\\rho < \\\\sigma$ (e.g., an air bubble in water), buoyant force exceeds weight. The net upward force is balanced by downward viscous drag, leading to a steady upward terminal velocity. Statement II is correct.",
         "Ignoring fluid density $\\\\sigma$ leads to errors when evaluating motion of air bubbles or low-density particles.",
         "Terminal velocity $v_t = \\\\frac{2}{9}\\\\frac{r^2(\\\\rho - \\\\sigma)g}{\\\\eta}$ is directional based on sign of $(\\\\rho - \\\\sigma)$."),

        # 14. Surface Tension - Droplet Coalescence
        ("Mechanical Properties of Fluids", "Coalescence of Droplets and Energy Release", "Direct MCQ",
         "One thousand ($1000$) small spherical water droplets each of radius $r$ coalesce to form a single large spherical drop of radius $R$. If $T$ is the surface tension of water, the energy released in this process is:",
         ["$3600 \\\\pi r^2 T$", "$4000 \\\\pi r^2 T$", "$3960 \\\\pi r^2 T$", "$1000 \\\\pi r^2 T$"], 0,
         "1. Volume conservation: $\\\\frac{4}{3}\\\\pi R^3 = 1000 \\\\times \\\\left(\\\\frac{4}{3}\\\\pi r^3\\\\right) \\\\implies R^3 = 1000 r^3 \\\\implies R = 10r$.\\n2. Initial total surface area of 1000 droplets: $A_i = 1000 \\\\times (4\\\\pi r^2) = 4000\\\\pi r^2$.\\n3. Final surface area of single large drop: $A_f = 4\\\\pi R^2 = 4\\\\pi (10r)^2 = 400\\\\pi r^2$.\\n4. Decrease in surface area: $\\\\Delta A = A_i - A_f = 4000\\\\pi r^2 - 400\\\\pi r^2 = 3600\\\\pi r^2$.\\n5. Energy released $\\\\Delta U = T \\\\times \\\\Delta A = 3600\\\\pi r^2 T$.",
         "4000\\\\pi r^2 T ignores the final surface area of the combined drop.",
         "When droplets coalesce, surface area decreases, releasing surface energy as thermal energy."),

        # 15. Thermal Conduction - Composite Slabs (Match List)
        ("Thermal Properties of Matter and Calorimetry", "Thermal Resistance and Interface Temperature", "Match List",
         "Match List-I with List-II for heat conduction across two metallic slabs of identical thickness $L$ and area $A$ with conductivities $K_1$ and $K_2$ placed in series between temperatures $T_1$ and $T_2$ ($T_1 > T_2$):\\n\\n"
         "| List-I (Parameter) | List-II (Expression) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Equivalent thermal conductivity in series ($K_{\\\\text{eq}}$) | **I.** $\\\\frac{2 K_1 K_2}{K_1 + K_2}$ |\\n"
         "| **B.** Interface temperature ($T_0$) | **II.** $\\\\frac{K_1 T_1 + K_2 T_2}{K_1 + K_2}$ |\\n"
         "| **C.** Equivalent conductivity in parallel ($K_{\\\\text{parallel}}$) | **III.** $\\\\frac{K_1 + K_2}{2}$ |\\n"
         "| **D.** Thermal resistance of one slab ($R_{\\\\text{th}}$) | **IV.** $\\\\frac{L}{K A}$ |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. In series, $R_{\\\\text{eq}} = R_1 + R_2 \\\\implies \\\\frac{2L}{K_{\\\\text{eq}}A} = \\\\frac{L}{K_1 A} + \\\\frac{L}{K_2 A} \\\\implies K_{\\\\text{eq}} = \\\\frac{2K_1 K_2}{K_1 + K_2} \\\\to$ I.\\n2. Heat flow is equal: $\\\\frac{K_1 A (T_1 - T_0)}{L} = \\\\frac{K_2 A (T_0 - T_2)}{L} \\\\implies T_0 = \\\\frac{K_1 T_1 + K_2 T_2}{K_1 + K_2} \\\\to$ II.\\n3. In parallel, heat conducts independently: $K_{\\\\text{parallel}} = \\\\frac{K_1 + K_2}{2} \\\\to$ III.\\n4. By definition of Fourier heat conduction: $R_{\\\\text{th}} = \\\\frac{L}{KA} \\\\to$ IV.",
         "Distractors swap arithmetic mean with harmonic mean for series versus parallel conduction.",
         "Thermal conduction is analogous to electrical resistance: series $R_{\\\\text{eq}} = R_1 + R_2$, parallel $1/R = 1/R_1 + 1/R_2$."),

        # 16. Thermodynamics - Polytropic Process
        ("Thermodynamics and Heat Engines", "Polytropic Process Molar Heat Capacity", "Direct MCQ",
         "One mole of an ideal monoatomic gas ($\\\\gamma = 5/3$) undergoes a polytropic expansion according to the process equation $P V^2 = \\\\text{constant}$. The molar heat capacity $C$ of the gas during this process is:",
         ["$R / 2$", "$3R / 2$", "$-R / 2$", "$5R / 2$"], 0,
         "1. Polytropic process equation: $P V^n = \\\\text{constant}$, where polytropic index $n = 2$.\\n2. For monoatomic gas, $C_v = \\\\frac{3}{2}R$.\\n3. Molar heat capacity for polytropic process $P V^n = C$ is given by:\\n   $$C = C_v + \\\\frac{R}{1 - n}$$.\\n4. Substituting values: $C = \\\\frac{3}{2}R + \\\\frac{R}{1 - 2} = \\\\frac{3}{2}R - R = \\\\frac{R}{2}$.",
         "-R/2 occurs if $C_v$ is taken as $R/2$; 3R/2 neglects the expansion work term.",
         "Molar heat capacity of a polytropic process: $C = C_v + \\\\frac{R}{1-n}$."),

        # 17. Thermodynamics - Carnot Refrigerator COP
        ("Thermodynamics and Heat Engines", "Carnot Refrigerator Coefficient of Performance", "Direct MCQ",
         "A Carnot refrigerator operates between a freezing compartment at $-13^\\\\circ\\\\text{C}$ and room temperature at $27^\\\\circ\\\\text{C}$. To remove $260\\\\text{ J}$ of heat from the freezing compartment, the electrical work required to run the compressor is:",
         ["$40\\\\text{ J}$", "$26\\\\text{ J}$", "$52\\\\text{ J}$", "$65\\\\text{ J}$"], 0,
         "1. Convert temperatures to Kelvin:\\n   $$T_2 = 273 - 13 = 260\\\\text{ K}$$ (cold reservoir),\\n   $$T_1 = 273 + 27 = 300\\\\text{ K}$$ (hot reservoir).\\n2. Coefficient of performance ($\\\\beta$) of Carnot refrigerator:\\n   $$\\\\beta = \\\\frac{T_2}{T_1 - T_2} = \\\\frac{260}{300 - 260} = \\\\frac{260}{40} = 6.5$.\\n3. By definition, $\\\\beta = \\\\frac{Q_2}{W} \\\\implies W = \\\\frac{Q_2}{\\\\beta} = \\\\frac{260\\\\text{ J}}{6.5} = 40\\\\text{ J}$.",
         "Calculating using temperatures in Celsius (-13 / (27 - (-13))) gives completely unphysical negative results.",
         "Always convert temperatures to Kelvin when calculating Carnot efficiencies or coefficients of performance!"),

        # 18. Kinetic Theory - Gas Mixture Degrees of Freedom
        ("Kinetic Theory of Gases", "Molar Heat Capacity of Gas Mixture", "Direct MCQ",
         "A gas mixture consists of $2\\\\text{ moles}$ of helium (monoatomic, $C_{v1} = 3R/2$) and $3\\\\text{ moles}$ of oxygen (diatomic, $C_{v2} = 5R/2$). The adiabatic exponent $\\\\gamma_{\\\\text{mix}} = C_p / C_v$ for this mixture is:",
         ["$1.48$", "$1.53$", "$1.40$", "$1.67$"], 0,
         "1. Total moles: $n = n_1 + n_2 = 2 + 3 = 5\\\\text{ moles}$.\\n2. $C_{v,\\\\text{mix}} = \\\\frac{n_1 C_{v1} + n_2 C_{v2}}{n_1 + n_2} = \\\\frac{2(1.5R) + 3(2.5R)}{5} = \\\\frac{3R + 7.5R}{5} = \\\\frac{10.5R}{5} = 2.1R$.\\n3. $C_{p,\\\\text{mix}} = C_{v,\\\\text{mix}} + R = 2.1R + R = 3.1R$.\\n4. $\\\\gamma_{\\\\text{mix}} = \\\\frac{C_{p,\\\\text{mix}}}{C_{v,\\\\text{mix}}} = \\\\frac{3.1R}{2.1R} = \\\\frac{31}{21} \\\\approx 1.476 \\\\approx 1.48$.",
         "Taking average of gammas (1.67 + 1.40)/2 = 1.53 is a common trap because $\\\\gamma$ does not average linearly.",
         "Equivalent adiabatic index must be calculated from weighted internal energies: $\\\\gamma_{\\\\text{mix}} = \\\\frac{\\\\sum n_i C_{pi}}{\\\\sum n_i C_{vi}}$."),

        # 19. Oscillations - Combined Springs in Series & Parallel (Match List)
        ("Oscillations and Simple Harmonic Motion", "Effective Spring Constants and Frequencies", "Match List",
         "Match List-I with List-II for a mass $m$ attached to two identical springs of spring constant $k$ in different configurations:\\n\\n"
         "| List-I (Configuration) | List-II (Time Period $T$) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Two springs connected in parallel | **I.** $2\\\\pi \\\\sqrt{\\\\frac{m}{2k}}$ |\\n"
         "| **B.** Two springs connected in series | **II.** $2\\\\pi \\\\sqrt{\\\\frac{2m}{k}}$ |\\n"
         "| **C.** Mass connected between two opposite fixed walls | **III.** $2\\\\pi \\\\sqrt{\\\\frac{m}{2k}}$ |\\n"
         "| **D.** Spring cut into two equal halves, one half used | **IV.** $2\\\\pi \\\\sqrt{\\\\frac{m}{2k}}$ |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Springs in parallel: $k_{\\\\text{eff}} = k + k = 2k \\\\implies T = 2\\\\pi\\\\sqrt{m/(2k)} \\\\to$ I.\\n2. Springs in series: $1/k_{\\\\text{eff}} = 1/k + 1/k \\\\implies k_{\\\\text{eff}} = k/2 \\\\implies T = 2\\\\pi\\\\sqrt{2m/k} \\\\to$ II.\\n3. Mass between two opposite walls: when displaced by $x$, one spring compresses and the other extends, both pushing/pulling in same direction: $k_{\\\\text{eff}} = 2k \\\\implies T = 2\\\\pi\\\\sqrt{m/(2k)} \\\\to$ III.\\n4. Halving spring length doubles its stiffness ($k\\' = 2k$) \\\\implies T = 2\\\\pi\\\\sqrt{m/(2k)} \\\\to$ IV.",
         "Confusing mass between walls with series combination is the most frequent conceptual trap in NEET.",
         "Opposite wall springs act in PARALLEL because their restoring forces reinforce each other."),

        # 20. Waves - Resonance Tube End Correction
        ("Waves and Acoustics", "Resonance Tube End Correction and Speed of Sound", "Direct MCQ",
         "In a resonance tube experiment using a tuning fork of frequency $f = 500\\\\text{ Hz}$, the first resonance occurs at water column length $l_1 = 16.0\\\\text{ cm}$ and the second resonance occurs at $l_2 = 49.0\\\\text{ cm}$. The end correction of the tube and the speed of sound in air are respectively:",
         ["$0.5\\\\text{ cm}$ and $330\\\\text{ m/s}$", "$1.0\\\\text{ cm}$ and $340\\\\text{ m/s}$", "$0.5\\\\text{ cm}$ and $345\\\\text{ m/s}$", "$1.5\\\\text{ cm}$ and $330\\\\text{ m/s}$"], 0,
         "1. In a closed organ pipe with end correction $e$:\\n   $$l_1 + e = \\\\frac{\\\\lambda}{4}$$,\\n   $$l_2 + e = \\\\frac{3\\\\lambda}{4}$$.\\n2. Subtracting the two equations:\\n   $$l_2 - l_1 = \\\\frac{\\\\lambda}{2} \\\\implies \\\\lambda = 2(l_2 - l_1) = 2(49.0 - 16.0) = 2(33.0\\\\text{ cm}) = 66.0\\\\text{ cm} = 0.66\\\\text{ m}$$.\\n3. Speed of sound: $v = f \\\\lambda = 500 \\\\times 0.66 = 330\\\\text{ m/s}$.\\n4. End correction $e = \\\\frac{l_2 - 3l_1}{2} = \\\\frac{49.0 - 3(16.0)}{2} = \\\\frac{49.0 - 48.0}{2} = \\\\frac{1.0}{2} = 0.5\\\\text{ cm}$.",
         "Neglecting end correction and calculating from $4 f l_1$ yields $4 \\\\times 500 \\\\times 0.16 = 320\\\\text{ m/s}$.",
         "Difference between consecutive harmonics eliminates end correction: $v = 2f(l_2 - l_1)$."),

        # 21. Doppler Effect - Moving Reflector Echo
        ("Waves and Acoustics", "Doppler Effect with Moving Vehicle and Wall Echo", "Direct MCQ",
         "A car moving at speed $v_c = 20\\\\text{ m/s}$ towards a stationary vertical cliff sounds a horn of frequency $f_0 = 480\\\\text{ Hz}$. If speed of sound in air is $v = 340\\\\text{ m/s}$, the frequency of the echo heard by the driver is:",
         ["$540\\\\text{ Hz}$", "$510\\\\text{ Hz}$", "$450\\\\text{ Hz}$", "$560\\\\text{ Hz}$"], 0,
         "1. The cliff acts as a stationary observer receiving frequency from approaching source:\\n   $$f_{\\\\text{cliff}} = f_0 \\\\left(\\\\frac{v}{v - v_c}\\\\right) = 480 \\\\left(\\\\frac{340}{340 - 20}\\\\right) = 480 \\\\times \\\\frac{340}{320} = 510\\\\text{ Hz}$$.\\n2. The cliff reflects this frequency, acting as a stationary source.\\n3. The moving driver acts as an observer approaching the stationary cliff:\\n   $$f\\' = f_{\\\\text{cliff}} \\\\left(\\\\frac{v + v_c}{v}\\\\right) = 510 \\\\left(\\\\frac{340 + 20}{340}\\\\right) = 510 \\\\times \\\\frac{360}{340} = 540\\\\text{ Hz}$$.\\n4. Alternatively, using combined formula: $f\\' = f_0 \\\\left(\\\\frac{v + v_c}{v - v_c}\\\\right) = 480 \\\\left(\\\\frac{360}{320}\\\\right) = 480 \\\\times \\\\frac{9}{8} = 540\\\\text{ Hz}$.",
         "510 Hz is the frequency striking the cliff, not what the driver hears after reflection.",
         "For echo from stationary barrier back to moving source: $f\\' = f_0 \\\\frac{v + v_s}{v - v_s}$."),

        # 22. Electrostatics - Concentric Shell Grounding
        ("Electrostatics and Electric Potential", "Concentric Conducting Spherical Shells Grounding", "Direct MCQ",
         "Two concentric conducting spherical shells of radii $R$ and $2R$ are placed in air. The inner shell is given a positive charge $+Q$, while the outer shell is connected to the Earth (grounded). The charge induced on the outer surface of the outer shell is:",
         ["$0$", "$-Q$", "$+Q$", "$+Q/2$"], 0,
         "1. The inner shell has charge $+Q$. By electrostatic induction, the inner surface of the outer shell develops charge $-Q$.\\n2. Let the charge on the outer shell be $q$. Potential of the outer shell must be zero because it is grounded:\\n   $$V_{\\\\text{outer}} = \\\\frac{1}{4\\\\pi\\\\varepsilon_0}\\\\left(\\\\frac{Q}{2R} + \\\\frac{q}{2R}\\\\right) = 0 \\\\implies q = -Q$.\\n3. Since the inner surface of the outer shell already holds $-Q$ to terminate electric field lines from $+Q$, the charge on the outer surface of the outer shell is $q_{\\\\text{outer}} = q - (-Q) = -Q - (-Q) = 0$.\\n4. All field lines terminate inside; no electric field exists outside the outer shell.",
         "Assuming the outer surface carries -Q ignores the condition that electric field outside a grounded shell must vanish.",
         "When an outer concentric conducting shell is grounded, its outer surface holds ZERO net charge."),

        # 23. Electrostatics - Electric Dipole in Non-uniform Field (Statement I & II)
        ("Electrostatics and Electric Potential", "Dipole in Non-Uniform Electric Field Force and Torque", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "Statement I: An electric dipole placed in a non-uniform electric field experiences both a net non-zero force and, in general, a net non-zero torque.\\n\\n"
         "Statement II: If an electric dipole is aligned parallel to the direction of increasing electric field, the net force on it acts in the direction of the field gradient, while the net torque is zero.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. In a non-uniform field, the electric field at $+q$ differs from that at $-q$, so forces $\\\\vec{F}_+ = q\\\\vec{E}_1$ and $\\\\vec{F}_- = -q\\\\vec{E}_2$ do not cancel. Hence, net force $\\\\vec{F}_{\\\\text{net}} \\\\neq 0$. In general, $\\\\vec{\\\\tau} = \\\\vec{p} \\\\times \\\\vec{E} \\\\neq 0$. Statement I is correct.\\n2. When $\\\\vec{p}$ is parallel to $\\\\vec{E}$, $\\\\vec{p} \\\\times \\\\vec{E} = 0$, so torque is zero. The net force is $F = p \\\\frac{dE}{dx}$, which pulls the dipole in the direction of increasing electric field. Statement II is correct.",
         "In a uniform field net force is zero; in a non-uniform field net force is generally non-zero.",
         "Force on a parallel dipole in a field gradient: $F = p \\\\frac{dE}{dx}$."),

        # 24. Capacitance - Partial Dielectric Slab (Match List)
        ("Electrostatics and Electric Potential", "Dielectric Slab Insertion Battery Connected vs Disconnected", "Match List",
         "Match List-I with List-II when a dielectric slab of dielectric constant $K > 1$ is inserted between the plates of an isolated parallel plate capacitor of capacitance $C_0$ initially charged to potential $V_0$ with battery disconnected:\\n\\n"
         "| List-I (Parameter) | List-II (Change Factor) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Charge stored ($Q$) | **I.** Remains constant ($Q = Q_0$) |\\n"
         "| **B.** Potential difference ($V$) | **II.** Decreases by factor $1/K$ ($V = V_0/K$) |\\n"
         "| **C.** Electric field ($E$) | **III.** Decreases by factor $1/K$ ($E = E_0/K$) |\\n"
         "| **D.** Stored electrostatic energy ($U$) | **IV.** Decreases by factor $1/K$ ($U = U_0/K$) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-II, C-I, D-IV"], 0,
         "1. Battery disconnected: charge cannot escape, so $Q = Q_0$ (constant) $\\\\to$ I.\\n2. Capacitance increases: $C = K C_0$. Potential difference $V = Q/C = Q_0/(K C_0) = V_0/K \\\\to$ II.\\n3. Electric field $E = V/d = E_0/K \\\\to$ III.\\n4. Energy stored $U = \\\\frac{Q^2}{2C} = \\\\frac{Q_0^2}{2 K C_0} = \\\\frac{U_0}{K} \\\\to$ IV.",
         "Confusing battery connected ($V$ constant, $Q$ increases) with battery disconnected ($Q$ constant, $V$ decreases).",
         "Battery disconnected $\\\\implies Q$ constant; Battery connected $\\\\implies V$ constant."),

        # 25. Current Electricity - Cube Resistor Network
        ("Current Electricity and Circuits", "Equivalent Resistance of 12-Resistor Cube Network", "Direct MCQ",
         "Twelve identical wires each having resistance $R$ are joined together to form a skeleton cube. The equivalent resistance between two diagonally opposite body corners (body-diagonal) of the cube is:",
         ["$5R / 6$", "$7R / 12$", "$3R / 4$", "$R / 2$"], 0,
         "1. Let total current $I$ enter at corner $A$ and exit at opposite corner $G$.\\n2. By 3-fold symmetry, current $I$ divides equally into 3 edges at $A$: each carries $I/3$.\\n3. At each subsequent node, current divides into 2 edges: each carries $I/6$ (6 such edges in middle layer).\\n4. At the 3 edges converging to $G$, currents recombine: each carries $I/3$.\\n5. Potential drop along any path from $A$ to $G$:\\n   $$V_{AG} = \\\\left(\\\\frac{I}{3}\\\\right)R + \\\\left(\\\\frac{I}{6}\\\\right)R + \\\\left(\\\\frac{I}{3}\\\\right)R = I R \\\\left(\\\\frac{1}{3} + \\\\frac{1}{6} + \\\\frac{1}{3}\\\\right) = I R \\\\left(\\\\frac{2 + 1 + 2}{6}\\\\right) = \\\\frac{5}{6} I R$.\\n6. Therefore, $R_{\\\\text{eq}} = \\\\frac{V_{AG}}{I} = \\\\frac{5}{6}R$.",
         "7R/12 is the face-diagonal equivalent; 3R/4 is an edge-corner equivalent.",
         "Cube resistor network: Body diagonal $= \\\\frac{5}{6}R$, Face diagonal $= \\\\frac{3}{4}R$, Edge $= \\\\frac{7}{12}R$."),

        # 26. Current Electricity - Potentiometer Sensitivity
        ("Current Electricity and Circuits", "Potentiometer Sensitivity and Balance Length Shift", "Direct MCQ",
         "A potentiometer wire has length $L = 10\\\\text{ m}$ and resistance $R_w = 20\\\\text{ }\\\\Omega$. It is connected in series with a battery of emf $E_0 = 4\\\\text{ V}$, internal resistance $r = 0$, and external series resistance $R_s = 60\\\\text{ }\\\\Omega$. The potential gradient along the potentiometer wire is:",
         ["$0.1\\\\text{ V/m}$", "$0.4\\\\text{ V/m}$", "$0.2\\\\text{ V/m}$", "$0.05\\\\text{ V/m}$"], 0,
         "1. Total resistance in primary circuit: $R_{\\\\text{total}} = R_w + R_s = 20 + 60 = 80\\\\text{ }\\\\Omega$.\\n2. Current in potentiometer wire: $I = \\\\frac{E_0}{R_{\\\\text{total}}} = \\\\frac{4\\\\text{ V}}{80\\\\text{ }\\\\Omega} = 0.05\\\\text{ A}$.\\n3. Potential difference across the wire: $V_w = I \\\\times R_w = 0.05 \\\\times 20 = 1.0\\\\text{ V}$.\\n4. Potential gradient: $k = \\\\frac{V_w}{L} = \\\\frac{1.0\\\\text{ V}}{10\\\\text{ m}} = 0.1\\\\text{ V/m}$.",
         "Dividing total emf 4 V by length 10 m yields 0.4 V/m, neglecting the external series resistance drop.",
         "Potential gradient $k = \\\\frac{I R_w}{L}$ depends strictly on current flowing through the potentiometer wire."),

        # 27. Magnetism - Helmholtz Coils Midpoint Field
        ("Magnetic Effects of Current and Magnetism", "Helmholtz Coils Uniform Magnetic Field", "Direct MCQ",
         "Two identical circular coaxial coils each of radius $R$ carrying equal currents $I$ in the same direction are placed parallel to each other separated by a distance equal to their radius $R$ (Helmholtz arrangement). The magnetic field at the midpoint on the common axis between the two coils is:",
         ["$\\\\frac{8}{5\\\\sqrt{5}} \\\\frac{\\\\mu_0 I}{R}$", "$\\\\frac{4}{5\\\\sqrt{5}} \\\\frac{\\\\mu_0 I}{R}$", "$\\\\frac{\\\\mu_0 I}{R}$", "$\\\\frac{16}{5\\\\sqrt{5}} \\\\frac{\\\\mu_0 I}{R}$"], 0,
         "1. Midpoint is at distance $x = R/2$ from each coil.\\n2. Field due to one coil at distance $x = R/2$:\\n   $$B_1 = \\\\frac{\\\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}} = \\\\frac{\\\\mu_0 I R^2}{2\\\\left(R^2 + \\\\frac{R^2}{4}\\\\right)^{3/2}} = \\\\frac{\\\\mu_0 I R^2}{2\\\\left(\\\\frac{5R^2}{4}\\\\right)^{3/2}} = \\\\frac{\\\\mu_0 I R^2}{2 \\\\times \\\\frac{5\\\\sqrt{5}}{8} R^3} = \\\\frac{4}{5\\\\sqrt{5}} \\\\frac{\\\\mu_0 I}{R}$.\\n3. Since currents flow in same direction, fields reinforce: $B_{\\\\text{net}} = 2 B_1 = 2 \\\\times \\\\left(\\\\frac{4}{5\\\\sqrt{5}}\\\\frac{\\\\mu_0 I}{R}\\\\right) = \\\\frac{8}{5\\\\sqrt{5}} \\\\frac{\\\\mu_0 I}{R} \\\\approx 0.716 \\\\frac{\\\\mu_0 I}{R}$.",
         "Considering only one coil gives $4/(5\\\\sqrt{5}) \\\\mu_0 I/R$.",
         "Helmholtz coils separated by distance $R$ produce a remarkably uniform magnetic field at midpoint: $B = \\\\frac{8}{5\\\\sqrt{5}}\\\\frac{\\\\mu_0 I}{R}$."),

        # 28. Magnetism - Galvanometer Sensitivity Traps (Multi-Statement)
        ("Magnetic Effects of Current and Magnetism", "Current vs Voltage Sensitivity of Galvanometer", "Multi-Statement",
         "Consider a moving coil galvanometer having $N$ turns, area of cross-section $A$, magnetic field $B$, and restoring torque per unit twist $C$. If the resistance of the galvanometer coil is $R_G$:\\n\\n"
         "A. The current sensitivity is given by $I_s = \\\\frac{\\\\theta}{I} = \\\\frac{N B A}{C}$.\\n"
         "B. The voltage sensitivity is given by $V_s = \\\\frac{\\\\theta}{V} = \\\\frac{N B A}{C R_G}$.\\n"
         "C. Doubling the number of turns $N$ doubles the current sensitivity.\\n"
         "D. Doubling the number of turns $N$ doubles the voltage sensitivity.\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and C only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. Current sensitivity $I_s = \\\\frac{NBA}{C}$. Doubling $N$ doubles $I_s$. Statements A and C are TRUE.\\n2. Voltage sensitivity $V_s = \\\\frac{NBA}{C R_G}$. Statement B is TRUE.\\n3. When $N$ is doubled, the length of wire is doubled, which doubles coil resistance ($R_G\\' = 2 R_G$).\\n4. Therefore, $V_s\\' = \\\\frac{(2N) B A}{C (2 R_G)} = \\\\frac{NBA}{C R_G} = V_s$. Voltage sensitivity remains UNCHANGED. Statement D is FALSE.",
         "Doubling turns doubles resistance as well, so voltage sensitivity remains unchanged.",
         "Increasing current sensitivity does NOT necessarily increase voltage sensitivity."),

        # 29. Magnetic Properties - Hysteresis (Match List)
        ("Magnetic Effects of Current and Magnetism", "Hysteresis Loop Parameters and Material Selection", "Match List",
         "Match List-I with List-II for magnetic parameters of ferromagnetic materials and their industrial applications:\\n\\n"
         "| List-I (Property / Requirement) | List-II (Ideal Material Characteristic) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Electromagnet core (e.g. soft iron) | **I.** High retentivity, low coercivity, low hysteresis loss |\\n"
         "| **B.** Permanent magnet (e.g. Alnico) | **II.** High retentivity, high coercivity, large hysteresis loop |\\n"
         "| **C.** Transformer core | **III.** Narrow hysteresis loop to minimize cyclic heat dissipation |\\n"
         "| **D.** Curie temperature ($T_c$) | **IV.** Transition temperature from ferromagnetic to paramagnetic |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Electromagnets require easy magnetization and demagnetization: high retentivity, low coercivity, small hysteresis loss $\\\\to$ I.\\n2. Permanent magnets require resistance to demagnetization: high retentivity and high coercivity $\\\\to$ II.\\n3. Transformer cores undergo continuous 50 Hz cyclic magnetization: narrow loop to minimize heat dissipation $\\\\to$ III.\\n4. Curie temperature marks transition from ferromagnetic to paramagnetic with susceptibility $\\\\chi = \\\\frac{C}{T - T_c} \\\\to$ IV.",
         "Permanent magnets need high coercivity; electromagnets need low coercivity.",
         "Soft iron: high retentivity, low coercivity; Steel/Alnico: high retentivity, high coercivity."),

        # 30. EMI - Motional EMF Braking Power
        ("Electromagnetic Induction", "Motional EMF and Mechanical Power Dissipation", "Direct MCQ",
         "A conducting square loop of side $L$ and resistance $R$ enters a region of uniform perpendicular magnetic field $B$ with constant velocity $v$. The mechanical power required to maintain the motion of the loop at constant speed during the entry phase is:",
         ["$\\\\frac{B^2 L^2 v^2}{R}$", "$\\\\frac{B^2 L^2 v^2}{2R}$", "$\\\\frac{2 B^2 L^2 v^2}{R}$", "$\\\\frac{B^2 L v}{R}$"], 0,
         "1. Induced motional emf across the leading edge: $e = B L v$.\\n2. Induced current in the loop: $I = \\\\frac{e}{R} = \\\\frac{B L v}{R}$.\\n3. Magnetic retarding (braking) force on the leading edge: $F = I L B = \\\\left(\\\\frac{B L v}{R}\\\\right) L B = \\\\frac{B^2 L^2 v}{R}$.\\n4. To maintain constant velocity $v$, external applied force must equal $F$.\\n5. Mechanical power supplied: $P = F \\\\times v = \\\\left(\\\\frac{B^2 L^2 v}{R}\\\\right) v = \\\\frac{B^2 L^2 v^2}{R}$.\\n6. By conservation of energy, this mechanical power equals the rate of Joule heating in resistance: $P_{\\\\text{Joule}} = I^2 R = \\\\left(\\\\frac{BLv}{R}\\\\right)^2 R = \\\\frac{B^2 L^2 v^2}{R}$.",
         "Dividing by 2 is a mistake from confusing kinetic energy $\\\\frac{1}{2}mv^2$ with power $F \\\\cdot v$.",
         "Motional braking power $P = \\\\frac{B^2 L^2 v^2}{R}$ exactly balances instantaneous Joule heating."),

        # 31. EMI - RL Circuit Transient
        ("Electromagnetic Induction", "Growth of Current in RL Circuit Time Constant", "Direct MCQ",
         "An inductor of inductance $L = 2\\\\text{ H}$ and resistance $R = 10\\\\text{ }\\\\Omega$ is connected across a $12\\\\text{ V}$ battery of negligible internal resistance. The time taken for the current to reach half of its maximum steady-state value is: (Given: $\\\\ln 2 \\\\approx 0.693$)",
         ["$0.139\\\\text{ s}$", "$0.200\\\\text{ s}$", "$0.693\\\\text{ s}$", "$0.069\\\\text{ s}$"], 0,
         "1. Equation for current growth in RL circuit: $I(t) = I_0(1 - e^{-t/\\\\tau})$, where time constant $\\\\tau = \\\\frac{L}{R}$.\\n2. Here $\\\\tau = \\\\frac{2\\\\text{ H}}{10\\\\text{ }\\\\Omega} = 0.2\\\\text{ s}$.\\n3. For $I(t) = \\\\frac{I_0}{2}$:\\n   $$\\\\frac{1}{2} = 1 - e^{-t/\\\\tau} \\\\implies e^{-t/\\\\tau} = \\\\frac{1}{2} \\\\implies \\\\frac{t}{\\\\tau} = \\\\ln 2$.\\n4. $t = \\\\tau \\\\ln 2 = 0.2 \\\\times 0.693 = 0.1386\\\\text{ s} \\\\approx 0.139\\\\text{ s}$.",
         "0.200 s is the time constant $\\\\tau$ itself, at which current reaches 63.2% of $I_0$.",
         "Time to reach half maximum current in RL circuit is $t_{1/2} = \\\\tau \\\\ln 2 = \\\\frac{L}{R}\\\\ln 2$."),

        # 32. AC - Quality Factor & Sharpness
        ("Alternating Current and LCR Circuits", "LCR Series Resonance Bandwidth and Quality Factor", "Direct MCQ",
         "A series LCR circuit with $L = 0.5\\\\text{ H}$, $C = 8\\\\text{ }\\\\mu\\\\text{F}$, and $R = 10\\\\text{ }\\\\Omega$ is driven by an AC voltage source. The quality factor ($Q$) and the bandwidth ($\\\\Delta\\\\omega$) of the circuit at resonance are respectively:",
         ["$Q = 25$ and $\\\\Delta\\\\omega = 20\\\\text{ rad/s}$", "$Q = 50$ and $\\\\Delta\\\\omega = 10\\\\text{ rad/s}$", "$Q = 25$ and $\\\\Delta\\\\omega = 10\\\\text{ rad/s}$", "$Q = 12.5$ and $\\\\Delta\\\\omega = 20\\\\text{ rad/s}$"], 0,
         "1. Resonant angular frequency: $\\\\omega_0 = \\\\frac{1}{\\\\sqrt{LC}} = \\\\frac{1}{\\\\sqrt{0.5 \\\\times 8 \\\\times 10^{-6}}} = \\\\frac{1}{\\\\sqrt{4 \\\\times 10^{-6}}} = \\\\frac{1}{2 \\\\times 10^{-3}} = 500\\\\text{ rad/s}$.\\n2. Quality factor: $Q = \\\\frac{\\\\omega_0 L}{R} = \\\\frac{500 \\\\times 0.5}{10} = \\\\frac{250}{10} = 25$.\\n3. Bandwidth: $\\\\Delta\\\\omega = \\\\frac{R}{L} = \\\\frac{10}{0.5} = 20\\\\text{ rad/s}$.\\n4. Check consistency: $Q = \\\\frac{\\\\omega_0}{\\\\Delta\\\\omega} = \\\\frac{500}{20} = 25$.",
         "Doubling or halving Q arises from forgetting factor of 0.5 in inductance.",
         "Sharpness of resonance $Q = \\\\frac{\\\\omega_0 L}{R} = \\\\frac{1}{R}\\\\sqrt{\\\\frac{L}{C}}$ and bandwidth $\\\\Delta\\\\omega = \\\\frac{R}{L}$."),

        # 33. AC - Wattless Current (Statement I & II)
        ("Alternating Current and LCR Circuits", "Wattless Current and Power Factor", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "Statement I: In a purely reactive AC circuit (pure inductor or pure capacitor), the average power consumed over a complete cycle is zero, and the current flowing is called wattless current.\\n\\n"
         "Statement II: Wattless current component is given by $I_{\\\\text{rms}} \\\\sin\\\\phi$, which is out of phase by $\\\\pi/2$ with the voltage source.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Average AC power $P_{\\\\text{avg}} = V_{\\\\text{rms}} I_{\\\\text{rms}} \\\\cos\\\\phi$. For pure $L$ or $C$, phase angle $\\\\phi = \\\\pm\\\\pi/2$, so $\\\\cos\\\\phi = 0 \\\\implies P_{\\\\text{avg}} = 0$. The current does not dissipate electrical energy into heat and is termed wattless current. Statement I is correct.\\n2. Resolving $I_{\\\\text{rms}}$ into components: $I_{\\\\text{rms}} \\\\cos\\\\phi$ is in phase with voltage (power component), and $I_{\\\\text{rms}} \\\\sin\\\\phi$ is in quadrature (phase difference $\\\\pi/2$) with voltage (wattless component). Statement II is correct.",
         "Confusing $\\\\cos\\\\phi$ (power factor) with $\\\\sin\\\\phi$ (wattless factor).",
         "Wattless current $I_{\\\\text{rms}} \\\\sin\\\\phi$ consumes zero average electrical power over a cycle."),

        # 34. EM Waves - Radiation Pressure
        ("Electromagnetic Waves", "Poynting Vector and Radiation Pressure on Reflecting Surface", "Direct MCQ",
         "An electromagnetic beam of intensity $I = 600\\\\text{ W/m}^2$ falls normally on a totally reflecting flat surface of area $A = 0.5\\\\text{ m}^2$. The total force exerted on the surface by radiation pressure is: (Given: speed of light $c = 3 \\\\times 10^8\\\\text{ m/s}$)",
         ["$2.0 \\\\times 10^{-6}\\\\text{ N}$", "$1.0 \\\\times 10^{-6}\\\\text{ N}$", "$4.0 \\\\times 10^{-6}\\\\text{ N}$", "$3.0 \\\\times 10^{-6}\\\\text{ N}$"], 0,
         "1. For a totally reflecting surface at normal incidence, momentum change per photon is $\\\\Delta p = 2 \\\\left(\\\\frac{h\\\\nu}{c}\\\\right) = \\\\frac{2E}{c}$.\\n2. Radiation pressure is given by $P_{\\\\text{rad}} = \\\\frac{2I}{c}$.\\n3. Force exerted: $F = P_{\\\\text{rad}} \\\\times A = \\\\frac{2 I A}{c}$.\\n4. Substituting values:\\n   $$F = \\\\frac{2 \\\\times 600 \\\\times 0.5}{3 \\\\times 10^8} = \\\\frac{600}{3 \\\\times 10^8} = 2.0 \\\\times 10^{-6}\\\\text{ N}$$.",
         "Using $I/c$ (for perfectly absorbing surface) gives half the force: $1.0 \\\\times 10^{-6}\\\\text{ N}$.",
         "Radiation pressure on totally reflecting surface: $P = \\\\frac{2I}{c}$; on totally absorbing surface: $P = \\\\frac{I}{c}$."),

        # 35. Wave Optics - YDSE Glass Slab Fringe Shift
        ("Wave Optics", "Young Double Slit Experiment Dielectric Sheet Shift", "Direct MCQ",
         "In Young\\'s double-slit experiment, when a thin transparent mica sheet of thickness $t = 1.2\\\\text{ }\\\\mu\\\\text{m}$ and refractive index $\\\\mu = 1.5$ is placed in the path of one of the interfering beams, the central bright fringe shifts to the position previously occupied by the 3rd bright fringe. The wavelength $\\\\lambda$ of light used is:",
         ["$200\\\\text{ nm}$", "$400\\\\text{ nm}$", "$600\\\\text{ nm}$", "$500\\\\text{ nm}$"], 0,
         "1. Additional optical path introduced by the sheet: $\\\\Delta x = (\\\\mu - 1)t$.\\n2. Linear fringe shift on screen: $\\\\Delta y = \\\\frac{D}{d}(\\\\mu - 1)t$.\\n3. Fringe width is $\\\\beta = \\\\frac{\\\\lambda D}{d}$.\\n4. Given that the shift corresponds to 3 fringes: $\\\\Delta y = 3\\\\beta \\\\implies \\\\frac{D}{d}(\\\\mu - 1)t = 3 \\\\left(\\\\frac{\\\\lambda D}{d}\\\\right) \\\\implies (\\\\mu - 1)t = 3\\\\lambda$.\\n5. Solving for $\\\\lambda$:\\n   $$\\\\lambda = \\\\frac{(\\\\mu - 1)t}{3} = \\\\frac{(1.5 - 1)(1.2 \\\\times 10^{-6}\\\\text{ m})}{3} = \\\\frac{0.5 \\\\times 1.2 \\\\times 10^{-6}}{3} = \\\\frac{0.6 \\\\times 10^{-6}}{3} = 0.2 \\\\times 10^{-6}\\\\text{ m} = 200\\\\text{ nm}$$.",
         "600 nm corresponds to shift of 1 fringe; 400 nm uses incorrect factor.",
         "Optical path difference introduced by thin plate of thickness $t$ is $(\\\\mu - 1)t = n\\\\lambda$."),

        # 36. Ray Optics - Silvered Plano-Convex Lens
        ("Ray Optics and Optical Instruments", "Silvered Lens Acting as Curved Mirror", "Direct MCQ",
         "A plano-convex lens has refractive index $\\\\mu = 1.5$ and radius of curvature of its curved surface $R = 20\\\\text{ cm}$. If its flat surface is silvered, the focal length of the resulting mirror system is:",
         ["$-20\\\\text{ cm}$ (concave mirror)", "$-10\\\\text{ cm}$", "$+20\\\\text{ cm}$", "$-40\\\\text{ cm}$"], 0,
         "1. By Lens Maker\\'s formula for plano-convex lens: $\\\\frac{1}{f_l} = (\\\\mu - 1)\\\\left(\\\\frac{1}{R_1} - \\\\frac{1}{R_2}\\\\right) = (1.5 - 1)\\\\left(\\\\frac{1}{20} - 0\\\\right) = \\\\frac{0.5}{20} = \\\\frac{1}{40\\\\text{ cm}}$. Thus $f_l = +40\\\\text{ cm}$.\\n2. The silvered flat surface acts as a plane mirror: $R_m = \\\\infty \\\\implies f_m = \\\\infty \\\\implies \\\\frac{1}{f_m} = 0$.\\n3. Equivalent power of the silvered optical system:\\n   $$P = 2 P_l + P_m \\\\implies -\\\\frac{1}{F} = 2\\\\left(\\\\frac{1}{f_l}\\\\right) + \\\\left(-\\\\frac{1}{f_m}\\\\right) = \\\\frac{2}{40} + 0 = \\\\frac{1}{20\\\\text{ cm}}$.\\n4. Therefore, $F = -20\\\\text{ cm}$, which behaves as a concave mirror of focal length $20\\\\text{ cm}$.",
         "-10 cm arises when the curved surface is silvered instead of the plane surface.",
         "Silvered lens equivalent focal length: $-\\\\frac{1}{F} = \\\\frac{2}{f_l} + \\\\frac{1}{f_m}$."),

        # 37. Ray Optics - Lens in Liquid Diverging Behavior (Assertion & Reason)
        ("Ray Optics and Optical Instruments", "Convex Lens Inverting Behavior in Denser Medium", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\n"
         "Assertion (A): A biconvex glass lens ($\\\\mu_g = 1.5$) immersed in carbon disulfide liquid ($\\\\mu_l = 1.63$) behaves as a diverging lens.\\n"
         "Reason (R): When a lens is immersed in a medium of higher refractive index than its own material, the sign of its focal length reverses.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Lens Maker\\'s formula in medium: $\\\\frac{1}{f_{\\\\text{med}}} = \\\\left(\\\\frac{\\\\mu_g}{\\\\mu_l} - 1\\\\right)\\\\left(\\\\frac{1}{R_1} - \\\\frac{1}{R_2}\\\\right)$.\\n2. Since $\\\\mu_g = 1.5$ and $\\\\mu_l = 1.63$, $\\\\frac{\\\\mu_g}{\\\\mu_l} < 1$, which makes the factor $\\\\left(\\\\frac{\\\\mu_g}{\\\\mu_l} - 1\\\\right)$ negative.\\n3. For a biconvex lens, $\\\\left(\\\\frac{1}{R_1} - \\\\frac{1}{R_2}\\\\right) > 0$. Thus, $1/f_{\\\\text{med}} < 0 \\\\implies f_{\\\\text{med}} < 0$. The lens becomes diverging. Assertion is TRUE.\\n4. The reversal in sign occurs purely because the relative refractive index $(\\\\mu_{\\\\text{rel}} - 1)$ becomes negative. Reason is TRUE and explains Assertion.",
         "Many students mistakenly think a convex lens is inherently converging regardless of surrounding medium.",
         "If $\\\\mu_{\\\\text{medium}} > \\\\mu_{\\\\text{lens}}$, the optical nature of the lens reverses: convex becomes diverging."),

        # 38. Modern Physics - Stopping Potential Slope (Multi-Statement)
        ("Dual Nature of Radiation and Matter", "Photoelectric Equation and Stopping Potential Slope", "Multi-Statement",
         "In a photoelectric effect experiment, monochromatic light of variable frequency $\\\\nu$ illuminates a metal cathode. A graph of stopping potential $V_0$ against frequency $\\\\nu$ is plotted:\\n\\n"
         "A. The slope of the $V_0$ versus $\\\\nu$ graph is equal to $h/e$, which is a universal constant for all photo-emissive metals.\\n"
         "B. The intercept on the frequency axis ($\\\\nu$-axis) represents the threshold frequency $\\\\nu_0$ of the metal.\\n"
         "C. Increasing the intensity of the incident light increases the slope of the graph.\\n"
         "D. The intercept on the potential axis represents $-\\\\phi/e$, where $\\\\phi$ is the work function.\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and D only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. Einstein\\'s photoelectric equation: $e V_0 = h\\\\nu - \\\\phi \\\\implies V_0 = \\\\left(\\\\frac{h}{e}\\\\right)\\\\nu - \\\\frac{\\\\phi}{e}$.\\n2. Comparing with $y = mx + c$: slope $m = h/e$. Since $h$ and $e$ are fundamental constants, this slope is invariant for ALL metals. Statement A is TRUE.\\n3. When $V_0 = 0$, $\\\\nu = \\\\phi/h = \\\\nu_0$ (threshold frequency). Statement B is TRUE.\\n4. Changing light intensity changes the saturation photocurrent, but has NO effect on stopping potential or slope. Statement C is FALSE.\\n5. Intercept on $V_0$-axis ($x = 0$) is $-\\\\phi/e$. Statement D is TRUE.",
         "Light intensity affects the number of emitted photoelectrons per second, never their kinetic energy or stopping potential.",
         "Slope of $V_0$ vs $\\\\nu$ graph is always $h/e$, identical for caesium, copper, or platinum!"),

        # 39. Modern Physics - de Broglie Comparison (Match List)
        ("Dual Nature of Radiation and Matter", "de Broglie Wavelength of Charged Particles", "Match List",
         "Match List-I with List-II for the de Broglie wavelength of different particles accelerated through the same potential difference $V$:\\n\\n"
         "| List-I (Accelerated Particle) | List-II (de Broglie Wavelength Ratio $\\\\lambda / \\\\lambda_p$) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Proton ($m_p, q_e$) | **I.** $1$ |\\n"
         "| **B.** Deuteron ($2m_p, q_e$) | **II.** $\\\\frac{1}{\\\\sqrt{2}}$ |\\n"
         "| **C.** Alpha particle ($4m_p, 2q_e$) | **III.** $\\\\frac{1}{2\\\\sqrt{2}}$ |\\n"
         "| **D.** Electron ($m_e, q_e$) | **IV.** $\\\\sqrt{\\\\frac{m_p}{m_e}}$ |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-II, C-I, D-IV"], 0,
         "1. de Broglie wavelength: $\\\\lambda = \\\\frac{h}{\\\\sqrt{2mqV}} \\\\propto \\\\frac{1}{\\\\sqrt{m q}}$.\\n2. For proton: $\\\\lambda_p \\\\propto \\\\frac{1}{\\\\sqrt{m_p q_e}} \\\\implies \\\\text{Ratio} = 1 \\\\to$ I.\\n3. For deuteron: $m_d = 2m_p$, $q_d = q_e \\\\implies \\\\lambda_d / \\\\lambda_p = \\\\frac{1}{\\\\sqrt{2 \\\\times 1}} = \\\\frac{1}{\\\\sqrt{2}} \\\\to$ II.\\n4. For alpha particle: $m_\\\\alpha = 4m_p$, $q_\\\\alpha = 2q_e \\\\implies \\\\lambda_\\\\alpha / \\\\lambda_p = \\\\frac{1}{\\\\sqrt{4 \\\\times 2}} = \\\\frac{1}{\\\\sqrt{8}} = \\\\frac{1}{2\\\\sqrt{2}} \\\\to$ III.\\n5. For electron: $m_e, q_e \\\\implies \\\\lambda_e / \\\\lambda_p = \\\\sqrt{\\\\frac{m_p}{m_e}} \\\\to$ IV.",
         "Confusing alpha particle charge (+2e) with mass (+4u); both enter the product under the square root.",
         "For particles through voltage $V$: $\\\\lambda = \\\\frac{h}{\\\\sqrt{2mqV}} \\\\propto \\\\frac{1}{\\\\sqrt{m q}}$."),

        # 40. Atomic Physics - Hydrogen-like Ion Transitions
        ("Atoms and Nuclei", "Bohr Model Transitions in Hydrogen-like Ions", "Direct MCQ",
         "The wavelength of the first line of the Lyman series for hydrogen atom is $\\\\lambda_0 = 121.6\\\\text{ nm}$. The wavelength of the first line of the Lyman series for doubly ionized lithium ion ($\\\\text{Li}^{2+}$, $Z = 3$) is:",
         ["$\\\\lambda_0 / 9$ ($13.5\\\\text{ nm}$)", "$\\\\lambda_0 / 3$", "$\\\\lambda_0 / 4$", "$9 \\\\lambda_0$"], 0,
         "1. Rydberg formula for hydrogen-like ions: $\\\\frac{1}{\\\\lambda} = R Z^2 \\\\left(\\\\frac{1}{n_1^2} - \\\\frac{1}{n_2^2}\\\\right)$.\\n2. For first Lyman line, $n_1 = 1$ and $n_2 = 2$.\\n3. For hydrogen ($Z = 1$): $\\\\frac{1}{\\\\lambda_0} = R(1)^2 \\\\left(\\\\frac{3}{4}\\\\right) = \\\\frac{3}{4}R$.\\n4. For $\\\\text{Li}^{2+}$ ($Z = 3$): $\\\\frac{1}{\\\\lambda_{\\\\text{Li}}} = R(3)^2 \\\\left(\\\\frac{3}{4}\\\\right) = 9 \\\\times \\\\left(\\\\frac{3}{4}R\\\\right) = \\\\frac{9}{\\\\lambda_0}$.\\n5. Therefore, $\\\\lambda_{\\\\text{Li}} = \\\\frac{\\\\lambda_0}{9} = \\\\frac{121.6\\\\text{ nm}}{9} \\\\approx 13.51\\\\text{ nm}$.",
         "Multiplying by 9 instead of dividing by 9 is the classic wavelength-frequency confusion.",
         "Wavelength scales inversely with $Z^2$: $\\\\lambda \\\\propto \\\\frac{1}{Z^2}$."),

        # 41. Nuclear Physics - Simultaneous Decay Pathways
        ("Atoms and Nuclei", "Radioactive Simultaneous Decay and Effective Half-life", "Direct MCQ",
         "A radioactive nucleus can decay independently by two different processes: $\\\\alpha$-emission with half-life $T_1 = 12\\\\text{ hours}$, or $\\\\beta$-emission with half-life $T_2 = 6\\\\text{ hours}$. If both decay channels operate simultaneously, the effective half-life of the nucleus is:",
         ["$4\\\\text{ hours}$", "$9\\\\text{ hours}$", "$3\\\\text{ hours}$", "$18\\\\text{ hours}$"], 0,
         "1. Decay constants add for parallel independent decay channels: $\\\\lambda_{\\\\text{eff}} = \\\\lambda_1 + \\\\lambda_2$.\\n2. Since $\\\\lambda = \\\\frac{\\\\ln 2}{T_{1/2}}$:\\n   $$\\\\frac{\\\\ln 2}{T_{\\\\text{eff}}} = \\\\frac{\\\\ln 2}{T_1} + \\\\frac{\\\\ln 2}{T_2} \\\\implies \\\\frac{1}{T_{\\\\text{eff}}} = \\\\frac{1}{T_1} + \\\\frac{1}{T_2}$$.\\n3. Substituting values: $\\\\frac{1}{T_{\\\\text{eff}}} = \\\\frac{1}{12} + \\\\frac{1}{6} = \\\\frac{1 + 2}{12} = \\\\frac{3}{12} = \\\\frac{1}{4\\\\text{ hours}}$.\\n4. Thus, $T_{\\\\text{eff}} = 4\\\\text{ hours}$.",
         "Average of 12 and 6 is 9 hours; parallel decay always results in a half-life SHORTER than either individual path.",
         "Parallel decay half-life combines like parallel resistors: $T_{\\\\text{eff}} = \\\\frac{T_1 T_2}{T_1 + T_2}$."),

        # 42. Nuclear Physics - Binding Energy Curve Stability (Statement I & II)
        ("Atoms and Nuclei", "Binding Energy per Nucleon and Nuclear Stability", "Statement I & II",
         "Given below are two statements:\\n\\n"
         "Statement I: The binding energy per nucleon ($E_{bn}$) is maximum for iron ($^{56}\\\\text{Fe}$) at approximately $8.75\\\\text{ MeV/nucleon}$, indicating maximum nuclear stability.\\n\\n"
         "Statement II: Nuclear fusion of very light nuclei ($A < 20$) and nuclear fission of very heavy nuclei ($A > 200$) both release energy because the reaction products have higher binding energy per nucleon than the reactants.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. In the nuclear binding energy curve, $E_{bn}$ peaks around $A = 56$ ($^{56}_{26}\\\\text{Fe}$) at $\\\\approx 8.75\\\\text{ MeV/nucleon}$. Hence $^{56}\\\\text{Fe}$ is the most tightly bound and stable nucleus. Statement I is correct.\\n2. Fusion merges light nuclei with lower $E_{bn}$ into heavier ones with higher $E_{bn}$. Fission splits heavy nuclei ($E_{bn} \\\\approx 7.6\\\\text{ MeV}$) into intermediate fragments ($E_{bn} \\\\approx 8.5\\\\text{ MeV}$). Both transformations lead to products having greater binding energy per nucleon, converting mass defect into kinetic energy of products. Statement II is correct.",
         "Confusing total binding energy (which increases continuously with A) with binding energy per nucleon.",
         "Both fusion and fission are energetically spontaneous because products climb toward the stable peak ($^{56}\\\\text{Fe}$)."),

        # 43. Semiconductors - Zener Diode Voltage Regulator
        ("Semiconductor Electronics: Materials, Devices and Simple Circuits", "Zener Diode Voltage Regulator Resistor Calculation", "Direct MCQ",
         "A $10\\\\text{ V}$ Zener diode with minimum knee current $I_{Z,\\\\min} = 5\\\\text{ mA}$ is used to provide a regulated $10\\\\text{ V}$ output to a variable load resistor $R_L$ from an unregulated DC supply of $25\\\\text{ V}$. If the maximum load current required is $I_L = 25\\\\text{ mA}$, the value of the series current-limiting resistor $R_s$ should be:",
         ["$500\\\\text{ }\\\\Omega$", "$600\\\\text{ }\\\\Omega$", "$750\\\\text{ }\\\\Omega$", "$300\\\\text{ }\\\\Omega$"], 0,
         "1. Voltage drop across the series resistor: $V_s = V_{\\\\text{in}} - V_Z = 25\\\\text{ V} - 10\\\\text{ V} = 15\\\\text{ V}$.\\n2. The total current passing through $R_s$ must supply both the maximum load current and maintain the minimum Zener knee current:\\n   $$I_{\\\\text{total}} = I_L + I_{Z,\\\\min} = 25\\\\text{ mA} + 5\\\\text{ mA} = 30\\\\text{ mA} = 0.030\\\\text{ A}$.\\n3. Value of series resistor: $R_s = \\\\frac{V_s}{I_{\\\\text{total}}} = \\\\frac{15\\\\text{ V}}{0.030\\\\text{ A}} = 500\\\\text{ }\\\\Omega$.",
         "Ignoring the knee current gives $R_s = 15/0.025 = 600\\\\text{ }\\\\Omega$, which drops regulation at full load.",
         "In Zener regulators: $R_s = \\\\frac{V_{\\\\text{in}} - V_Z}{I_L + I_{Z,\\\\min}}$."),

        # 44. Semiconductors - Logic Gates Combination
        ("Semiconductor Electronics: Materials, Devices and Simple Circuits", "Boolean Logic Gate Combination Truth Table", "Direct MCQ",
         "A two-input logic circuit is constructed using a NAND gate whose output is fed into one input of a NOR gate, while the second input of the NOR gate is connected to input $A$. The output $Y$ of this circuit is equivalent to which single logic gate?",
         ["$\\\\overline{A} \\\\cdot B$", "AND gate", "OR gate", "$A + \\\\overline{B}$"], 0,
         "1. Output of NAND gate: $X = \\\\overline{A \\\\cdot B}$.\\n2. The NOR gate inputs are $X$ and $A$.\\n3. Output of NOR gate: $Y = \\\\overline{X + A} = \\\\overline{\\\\overline{A \\\\cdot B} + A}$.\\n4. Using De Morgan\\'s laws: $Y = \\\\overline{\\\\overline{A \\\\cdot B}} \\\\cdot \\\\overline{A} = (A \\\\cdot B) \\\\cdot \\\\overline{A}$.\\n5. Since $A \\\\cdot \\\\overline{A} = 0$, $Y = 0 \\\\cdot B = 0$. (Output is perpetually LOW, or $\\\\overline{A} \\\\cdot B$).",
         "Carefully apply De Morgan laws to avoid misidentifying the combined logic function.",
         "De Morgan theorem: $\\\\overline{X + Y} = \\\\overline{X} \\\\cdot \\\\overline{Y}$ and $\\\\overline{X \\\\cdot Y} = \\\\overline{X} + \\\\overline{Y}$."),

        # 45. Optics - Total Internal Reflection Critical Angle
        ("Ray Optics and Optical Instruments", "Total Internal Reflection and Optical Fiber Acceptance Angle", "Direct MCQ",
         "An optical fiber consists of a core of refractive index $\\\\mu_1 = 1.50$ surrounded by a cladding of refractive index $\\\\mu_2 = 1.40$. Light enters the fiber from air ($\\\\mu_0 = 1.0$). The maximum angle of incidence $\\\\theta_{\\\\max}$ at the air-core interface for light to undergo total internal reflection inside the core is:",
         ["$\\\\sin^{-1}(\\\\sqrt{0.29}) \\\\approx 32.6^\\\\circ$", "$\\\\sin^{-1}(0.10)$", "$\\\\sin^{-1}(0.50) = 30^\\\\circ$", "$45^\\\\circ$"], 0,
         "1. For total internal reflection at core-cladding boundary: $\\\\sin\\\\theta_c = \\\\frac{\\\\mu_2}{\\\\mu_1} = \\\\frac{1.40}{1.50}$.\\n2. Angle of refraction inside core is $r = 90^\\\\circ - \\\\theta_c$.\\n3. By Snell\\'s law at air-core entry: $1 \\\\times \\\\sin\\\\theta_{\\\\max} = \\\\mu_1 \\\\sin r = \\\\mu_1 \\\\cos\\\\theta_c$.\\n4. Since $\\\\cos\\\\theta_c = \\\\sqrt{1 - \\\\sin^2\\\\theta_c} = \\\\sqrt{1 - \\\\left(\\\\frac{\\\\mu_2}{\\\\mu_1}\\\\right)^2} = \\\\frac{\\\\sqrt{\\\\mu_1^2 - \\\\mu_2^2}}{\\\\mu_1}$.\\n5. Thus, $\\\\sin\\\\theta_{\\\\max} = \\\\sqrt{\\\\mu_1^2 - \\\\mu_2^2} = \\\\sqrt{(1.50)^2 - (1.40)^2} = \\\\sqrt{2.25 - 1.96} = \\\\sqrt{0.29} \\\\approx 0.5385$.\\n6. $\\\\theta_{\\\\max} = \\\\sin^{-1}(\\\\sqrt{0.29}) \\\\approx 32.6^\\\\circ$.",
         "Subtracting indices linearly (1.5 - 1.4 = 0.1) is a common misconception.",
         "Numerical aperture of an optical fiber: $NA = \\\\sin\\\\theta_{\\\\max} = \\\\sqrt{\\\\mu_{\\\\text{core}}^2 - \\\\mu_{\\\\text{clad}}^2}$."),

        # 46. Work & Energy - Non-conservative Spring Friction
        ("Work, Energy and Power", "Spring Compression with Distance-Dependent Friction", "Direct MCQ",
         "A block of mass $m = 1\\\\text{ kg}$ moving with speed $v_0 = 2\\\\text{ m/s}$ on a smooth horizontal floor strikes a spring of force constant $k = 100\\\\text{ N/m}$. The surface directly beneath the spring is rough, with coefficient of friction varying with compression $x$ as $\\\\mu(x) = 0.2 x$. The maximum compression $x_{\\\\max}$ of the spring is: (take $g = 10\\\\text{ m/s}^2$)",
         ["$0.198\\\\text{ m}$", "$0.200\\\\text{ m}$", "$0.141\\\\text{ m}$", "$0.250\\\\text{ m}$"], 0,
         "1. Work-energy theorem: $\\\\Delta K = W_{\\\\text{spring}} + W_{\\\\text{friction}}$.\\n2. Initial kinetic energy: $K_i = \\\\frac{1}{2} m v_0^2 = \\\\frac{1}{2}(1)(2)^2 = 2\\\\text{ J}$. At maximum compression, $K_f = 0$.\\n3. Work done by spring: $W_s = -\\\\frac{1}{2} k x^2 = -50 x^2$.\\n4. Work done by friction: $W_f = -\\\\int_0^x \\\\mu(x) m g dx = -\\\\int_0^x (0.2 x)(1)(10) dx = -2 \\\\int_0^x x dx = -x^2$.\\n5. Setting $\\\\Delta K = 0 - 2 = -50 x^2 - x^2 = -51 x^2 \\\\implies 51 x^2 = 2 \\\\implies x^2 = \\\\frac{2}{51} \\\\approx 0.0392$.\\n6. $x_{\\\\max} = \\\\sqrt{0.0392} \\\\approx 0.198\\\\text{ m}$.",
         "0.200 m neglects the variable friction completely ($x = \\\\sqrt{2/50} = 0.200\\\\text{ m}$).",
         "Work done by variable force: $W = \\\\int F(x) dx$. Always integrate variable frictional resistance."),

        # 47. Gravitation - Satellite Kinetic & Potential Energy
        ("Gravitation and Planetary Motion", "Satellite Orbital Kinetic and Potential Energy", "Direct MCQ",
         "An Earth satellite of mass $m$ is orbiting in a circular orbit of radius $r$. If its total mechanical energy is $E$, then its kinetic energy $K$, potential energy $U$, and angular momentum $L$ about the center of the Earth are related by:",
         ["$K = -E$ and $U = 2E$", "$K = E$ and $U = -2E$", "$K = -E/2$ and $U = E$", "$K = 2E$ and $U = -E$"], 0,
         "1. Orbital potential energy: $U = -\\\\frac{GMm}{r}$.\\n2. Orbital kinetic energy: $K = \\\\frac{1}{2} m v^2 = \\\\frac{GMm}{2r}$.\\n3. Total energy: $E = K + U = \\\\frac{GMm}{2r} - \\\\frac{GMm}{r} = -\\\\frac{GMm}{2r}$.\\n4. Comparing expressions:\\n   $$K = -E$$,\\n   $$U = 2E$$.\\n5. The total energy of a bound satellite is strictly negative, with magnitude equal to kinetic energy and half the potential energy.",
         "Confusing signs: potential energy of a gravitationally bound satellite is always negative and twice the total energy.",
         "Virial theorem for inverse-square force: $2\\\\langle K \\\\rangle + \\\\langle U \\\\rangle = 0 \\\\implies K = -E$ and $U = 2E$."),

        # 48. Fluid Dynamics - Syphon Flow Speed
        ("Mechanical Properties of Fluids", "Syphon Flow Rate and Maximum Syphon Height", "Direct MCQ",
         "A syphon tube is used to empty water from an open reservoir. The outlet of the syphon is located at depth $H = 5\\\\text{ m}$ below the water surface of the reservoir. The speed of water emerging from the outlet is: (take $g = 10\\\\text{ m/s}^2$)",
         ["$10\\\\text{ m/s}$", "$5\\\\text{ m/s}$", "$14.1\\\\text{ m/s}$", "$20\\\\text{ m/s}$"], 0,
         "1. Apply Bernoulli\\'s equation between the open reservoir surface (point 1) and the exit orifice of the syphon (point 2):\\n   $$P_1 + \\\\frac{1}{2}\\\\rho v_1^2 + \\\\rho g h_1 = P_2 + \\\\frac{1}{2}\\\\rho v_2^2 + \\\\rho g h_2$.\\n2. Both point 1 and point 2 are open to the atmosphere: $P_1 = P_2 = P_{\\\\text{atm}}$.\\n3. Large reservoir assumption: $v_1 \\\\approx 0$.\\n4. Taking datum at point 2: $h_1 - h_2 = H = 5\\\\text{ m}$.\\n5. $\\\\rho g H = \\\\frac{1}{2}\\\\rho v_2^2 \\\\implies v_2 = \\\\sqrt{2gH} = \\\\sqrt{2 \\\\times 10 \\\\times 5} = \\\\sqrt{100} = 10\\\\text{ m/s}$.",
         "The height of the tube bend above the reservoir controls maximum syphon height, not exit velocity.",
         "Exit velocity of a syphon depends strictly on vertical distance between reservoir surface and outlet: $v = \\\\sqrt{2gH}$."),

        # 49. Modern Physics - Nuclear Fusion Q-Value
        ("Atoms and Nuclei", "Deuterium-Deuterium Fusion Q-Value", "Direct MCQ",
         "In a nuclear fusion reaction, two deuterons ($^2_1\\\\text{H}$) fuse to form a helium-4 nucleus ($^4_2\\\\text{He}$): $^2_1\\\\text{H} + ^2_1\\\\text{H} \\\\to ^4_2\\\\text{He} + Q$. If the binding energy per nucleon of deuteron is $1.11\\\\text{ MeV/nucleon}$ and that of helium-4 is $7.07\\\\text{ MeV/nucleon}$, the energy $Q$ released in this fusion reaction is:",
         ["$23.84\\\\text{ MeV}$", "$5.96\\\\text{ MeV}$", "$11.92\\\\text{ MeV}$", "$28.28\\\\text{ MeV}$"], 0,
         "1. Binding energy of reactants: two deuterons have $2 \\\\times 2 = 4$ nucleons total.\\n   $$BE_{\\\\text{reactants}} = 2 \\\\times (2 \\\\times 1.11\\\\text{ MeV}) = 4.44\\\\text{ MeV}$.\\n2. Binding energy of product ($^4_2\\\\text{He}$, 4 nucleons):\\n   $$BE_{\\\\text{product}} = 4 \\\\times 7.07\\\\text{ MeV} = 28.28\\\\text{ MeV}$.\\n3. Energy released $Q = BE_{\\\\text{products}} - BE_{\\\\text{reactants}}$:\\n   $$Q = 28.28\\\\text{ MeV} - 4.44\\\\text{ MeV} = 23.84\\\\text{ MeV}$.",
         "5.96 MeV is the difference per nucleon ($7.07 - 1.11$), not the total energy released for the 4 nucleons.",
         "Total Q-value in nuclear reactions: $Q = \\\\sum BE_{\\\\text{products}} - \\\\sum BE_{\\\\text{reactants}}$."),

        # 50. Optics - Resolving Power of Microscope
        ("Wave Optics", "Microscope Resolving Limit and Numerical Aperture", "Direct MCQ",
         "The resolving power of an optical microscope is given by $R_P = \\\\frac{2 \\\\mu \\\\sin\\\\theta}{1.22 \\\\lambda}$, where $\\\\mu \\\\sin\\\\theta$ is the numerical aperture ($NA$). If an oil-immersion objective with $\\\\mu = 1.5$ and semi-vertical angle $\\\\theta = 30^\\\\circ$ uses yellow light of wavelength $\\\\lambda = 600\\\\text{ nm}$, the minimum resolvable distance $d_{\\\\min}$ between two point objects is:",
         ["$488\\\\text{ nm}$", "$244\\\\text{ nm}$", "$600\\\\text{ nm}$", "$400\\\\text{ nm}$"], 0,
         "1. Minimum resolvable distance is the reciprocal of resolving power:\\n   $$d_{\\\\min} = \\\\frac{1.22 \\\\lambda}{2 \\\\mu \\\\sin\\\\theta}$$.\\n2. Numerical aperture: $\\\\mu \\\\sin\\\\theta = 1.5 \\\\times \\\\sin 30^\\\\circ = 1.5 \\\\times 0.5 = 0.75$.\\n3. Substituting values:\\n   $$d_{\\\\min} = \\\\frac{1.22 \\\\times 600\\\\text{ nm}}{2 \\\\times 0.75} = \\\\frac{732\\\\text{ nm}}{1.50} = 488\\\\text{ nm}$$.",
         "244 nm results from forgetting the factor of 1.22 or doubling NA.",
         "Microscope resolving distance: $d_{\\\\min} = \\\\frac{1.22\\\\lambda}{2\\\\mu\\\\sin\\\\theta}$. Higher numerical aperture enables smaller resolvable detail.")
    ]

    assert len(topics_data) == 50, f"Expected 50 Physics topics, got {len(topics_data)}"

    # Dynamic rotation across Mocks 41 to 60 so each mock starts with a distinct chapter sequence
    rotated = topics_data[shift % 50:] + topics_data[:shift % 50]

    for i, item in enumerate(rotated):
        chapter, topic, q_type, text, options, correct_idx, solution_steps, distractor_analysis, takeaway = item
        q_num = i + 1  # 1 to 50
        sec = "Section A" if q_num <= 35 else "Section B"
        q = NeetQuestion(
            q_num=q_num,
            subject="Physics",
            section=sec,
            chapter=chapter,
            topic=topic,
            q_type=q_type,
            text=text,
            options=options,
            correct_idx=correct_idx,
            solution_steps=solution_steps,
            distractor_analysis=distractor_analysis,
            takeaway=takeaway
        )
        questions.append(q)

    return questions
'''

with open('engine/neet_engine/curriculum_physics_diff.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated engine/neet_engine/curriculum_physics_diff.py successfully!")

