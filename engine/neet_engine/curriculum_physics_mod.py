# -*- coding: utf-8 -*-
"""
NEET Mock Generation Engine - Moderate Curriculum (Physics)
Strictly calibrated to NTA NEET-UG standards (2023-2026).
Moderate analytical depth: two-step calculations, multi-concept kinematics/electrodynamics,
dimensional analysis, circuit theorems, and ray-wave optics.
No JEE Advanced material; strictly NCERT-aligned.

Proportions for 50 Questions:
- Direct MCQ: 29
- Statement I & II: 7
- Match List: 7
- Assertion & Reason: 4
- Multi-Statement: 3
Total: 50
"""
from neet_models import NeetQuestion

def get_physics_questions_mod(mock_num):
    questions = []

    topics_data = [
        # 1. Units & Dimensions
        ("Units, Dimensions and Experimental Error", "Dimensional Formulae of Physical Constants", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Physical Quantity) | List-II (Dimensional Formula) |\n"
         "| :--- | :--- |\n"
         "| **A.** Planck's constant ($h$) | **I.** $[\\text{M}^1\\text{L}^2\\text{T}^{-1}]$ |\n"
         "| **B.** Universal gravitational constant ($G$) | **II.** $[\\text{M}^{-1}\\text{L}^3\\text{T}^{-2}]$ |\n"
         "| **C.** Coefficient of viscosity ($\\eta$) | **III.** $[\\text{M}^1\\text{L}^{-1}\\text{T}^{-1}]$ |\n"
         "| **D.** Bulk modulus of elasticity ($B$) | **IV.** $[\\text{M}^1\\text{L}^{-1}\\text{T}^{-2}]$ |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. $E = h\\nu \\implies [h] = \\frac{[\\text{M}^1\\text{L}^2\\text{T}^{-2}]}{[\\text{T}^{-1}]} = [\\text{M}^1\\text{L}^2\\text{T}^{-1}] \\to$ I.\n2. $F = \\frac{G m_1 m_2}{r^2} \\implies [G] = \\frac{[\\text{M}^1\\text{L}^1\\text{T}^{-2}][\\text{L}^2]}{[\\text{M}^2]} = [\\text{M}^{-1}\\text{L}^3\\text{T}^{-2}] \\to$ II.\n3. Stokes' law: $F = 6\\pi\\eta r v \\implies [\\eta] = \\frac{[\\text{M}^1\\text{L}^1\\text{T}^{-2}]}{[\\text{L}^1][\\text{L}^1\\text{T}^{-1}]} = [\\text{M}^1\\text{L}^{-1}\\text{T}^{-1}] \\to$ III.\n4. Bulk modulus $B = -\\frac{\\Delta P}{\\Delta V/V} = \\frac{[\\text{Force}]}{[\\text{Area}]} = [\\text{M}^1\\text{L}^{-1}\\text{T}^{-2}] \\to$ IV.",
         "Distractors swap bulk modulus with viscosity dimensions.",
         "Dimensional formulas: $h = [\\text{ML}^2\\text{T}^{-1}]$, $G = [\\text{M}^{-1}\\text{L}^3\\text{T}^{-2}]$, $\\eta = [\\text{ML}^{-1}\\text{T}^{-1}]$."),

        # 2. Kinematics - 1D
        ("Motion in a Straight Line and Graphs", "Velocity-Displacement Relation Acceleration", "Direct MCQ",
         "A particle moves along a straight line such that its velocity varies with displacement $x$ as $v = \\alpha \\sqrt{x}$, where $\\alpha$ is a positive constant. The acceleration of the particle is:",
         ["α^2 / 2 (constant)", "α^2 x", "α / 2", "α^2 / x"], 0,
         "1. Acceleration formula: $a = v \\frac{dv}{dx}$.\n2. Given $v = \\alpha x^{1/2} \\implies \\frac{dv}{dx} = \\frac{1}{2}\\alpha x^{-1/2}$.\n3. $a = (\\alpha x^{1/2}) \\left(\\frac{1}{2}\\alpha x^{-1/2}\\right) = \\frac{\\alpha^2}{2}$.\n4. The acceleration is constant and independent of position $x$.",
         "Distractors differentiate with respect to time without chain rule.",
         "Acceleration in terms of position: $a = v \\frac{dv}{dx}$. For $v = \\alpha\\sqrt{x}$, $a = \\alpha^2/2$."),

        # 3. Kinematics - Projectile Motion
        ("Motion in a Plane and Projectiles", "Velocity Vector Perpendicular to Initial Velocity", "Direct MCQ",
         "A particle is projected from the ground with an initial speed $u = 20\\text{ m/s}$ at an angle of $60^\\circ$ to the horizontal. Taking $g = 10\\text{ m/s}^2$, the time $t$ after which the instantaneous velocity vector of the particle becomes perpendicular to its initial velocity vector is:",
         ["2.31 s (4 / √3 s)", "2.00 s", "3.46 s (2√3 s)", "1.15 s (2 / √3 s)"], 0,
         "1. Velocity vector at time $t$: $\\vec{v}(t) = (u\\cos\\theta)\\hat{i} + (u\\sin\\theta - gt)\\hat{j}$.\n2. Initial velocity: $\\vec{u} = (u\\cos\\theta)\\hat{i} + (u\\sin\\theta)\\hat{j}$.\n3. For $\\vec{v} \\perp \\vec{u}$, the dot product vanishes: $\\vec{v} \\cdot \\vec{u} = 0$.\n   $$u^2\\cos^2\\theta + u\\sin\\theta(u\\sin\\theta - gt) = 0 \\implies u^2(\\cos^2\\theta + \\sin^2\\theta) - ugt\\sin\\theta = 0$$.\n   $$u^2 - ugt\\sin\\theta = 0 \\implies t = \\frac{u}{g\\sin\\theta}$$.\n4. Substituting values: $t = \\frac{20}{10 \\times \\sin 60^\\circ} = \\frac{2}{\\sqrt{3}/2} = \\frac{4}{\\sqrt{3}}\\text{ s} \\approx 2.31\\text{ s}$.",
         "Distractors use total time of flight $T = \\frac{2u\\sin\\theta}{g} = 2\\sqrt{3}\\text{ s}$ or divide by $\\cos\\theta$.",
         "Velocity becomes perpendicular to initial projection velocity at $t = \\frac{u}{g\\sin\\theta}$."),

        # 4. Laws of Motion & Friction - Pulley on Incline
        ("Laws of Motion and Friction", "Pulley with Friction on Incline", "Direct MCQ",
         "A block $A$ of mass $m_1 = 4\\text{ kg}$ rests on a rough inclined plane of inclination $30^\\circ$ (coefficient of kinetic friction $\\mu_k = 0.2$). Block $A$ is connected via a light inextensible string passing over a frictionless pulley to a hanging block $B$ of mass $m_2 = 6\\text{ kg}$. Taking $g = 10\\text{ m/s}^2$ and $\\cos 30^\\circ = 0.866$, the acceleration of the system is approximately:",
         ["$3.3\\text{ m/s}^2$", "$4.5\\text{ m/s}^2$", "$2.0\\text{ m/s}^2$", "$5.1\\text{ m/s}^2$"], 0,
         "1. Normal force on incline: $N = m_1 g \\cos 30^\\circ = 4 \\times 10 \\times 0.866 = 34.64\\text{ N}$.\n2. Friction force opposing upward motion: $f_k = \\mu_k N = 0.2 \\times 34.64 = 6.93\\text{ N}$.\n3. Net driving force accelerating the system ($m_1 + m_2$):\n   $$F_{\\text{net}} = m_2 g - m_1 g \\sin 30^\\circ - f_k = 60 - (40 \\times 0.5) - 6.93 = 60 - 20 - 6.93 = 33.07\\text{ N}$$.\n4. System acceleration: $a = \\frac{F_{\\text{net}}}{m_1 + m_2} = \\frac{33.07}{10} \\approx 3.31\\text{ m/s}^2$.",
         "4.0 m/s^2 ignores friction completely; 2.0 m/s^2 subtracts $m_2$ gravity incorrectly.",
         "Net acceleration $a = \\frac{m_2 g - m_1 g \\sin\\theta - \\mu m_1 g \\cos\\theta}{m_1 + m_2}$."),

        # 5. Laws of Motion & Friction - Vertical Circle
        ("Laws of Motion and Friction", "Minimum Velocity to Loop the Vertical Loop", "Direct MCQ",
         "A small bob of mass $m$ attached to a light string of length $L$ is rotated in a vertical circle. The minimum speed $u$ that must be imparted to the bob at the lowest point so that it completes a full vertical circular loop without string slackening is:",
         ["√(5 g L)", "√(4 g L)", "√(3 g L)", "√(6 g L)"], 0,
         "1. At the highest point, tension $T \\ge 0$. The minimum condition occurs when $T = 0$, where gravity provides centripetal force: $\\frac{m v_{\\text{top}}^2}{L} = mg \\implies v_{\\text{top}} = \\sqrt{gL}$.\n2. Conserving mechanical energy between lowest point and highest point (height difference $2L$):\n   $$\\frac{1}{2}m u^2 = \\frac{1}{2}m v_{\\text{top}}^2 + mg(2L) = \\frac{1}{2}m(gL) + 2mgL = \\frac{5}{2}mgL$$.\n3. Solving for $u$: $u = \\sqrt{5gL}$. Tension at the bottom is $T_{\\text{bottom}} = 6mg$.",
         "$\\sqrt{4gL}$ forgets the minimum top velocity; $\\sqrt{3gL}$ applies to oscillation within quadrant.",
         "Minimum speed at lowest point to complete vertical loop is $u = \\sqrt{5gL}$."),

        # 6. Work, Energy & Power - Spring Compression
        ("Work, Energy and Power", "Spring-Block Collision and Maximum Compression", "Direct MCQ",
         "A block of mass $m = 2\\text{ kg}$ moving at velocity $v = 4\\text{ m/s}$ on a frictionless horizontal floor collides with the free end of an ideal massless spring of force constant $k = 800\\text{ N/m}$ fixed to a vertical wall. The maximum compression of the spring is:",
         ["0.20 m (20 cm)", "0.10 m (10 cm)", "0.40 m (40 cm)", "0.05 m (5 cm)"], 0,
         "1. Mechanical energy is conserved as the block comes to momentary rest during maximum compression $x_{\\text{max}}$.\n2. Initial kinetic energy = Final elastic potential energy:\n   $$\\frac{1}{2} m v^2 = \\frac{1}{2} k x_{\\text{max}}^2 \\implies x_{\\text{max}} = v \\sqrt{\\frac{m}{k}}$$.\n3. Calculation: $x_{\\text{max}} = 4 \\times \\sqrt{\\frac{2}{800}} = 4 \\times \\sqrt{\\frac{1}{400}} = 4 \\times \\frac{1}{20} = 0.20\\text{ m} = 20\\text{ cm}$.",
         "0.10 m divides by 40; 0.40 m forgets square root on spring constant.",
         "Maximum spring compression under impact: $x_{\\text{max}} = v \\sqrt{m/k}$."),

        # 7. Rotational Motion - Rolling on Incline
        ("System of Particles and Rotational Motion", "Rolling Motion Minimum Friction Coefficient", "Direct MCQ",
         "A solid uniform sphere of mass $M$ and radius $R$ rolls down an inclined plane of inclination $\\theta$ without slipping. The minimum coefficient of static friction $\\mu_s$ required to maintain pure rolling without slipping is:",
         ["2/7 tan θ", "1/3 tan θ", "2/5 tan θ", "5/7 tan θ"], 0,
         "1. For pure rolling down an incline, the linear acceleration is $a = \\frac{g\\sin\\theta}{1 + I/MR^2}$.\n2. For a solid sphere, $I = \\frac{2}{5}MR^2 \\implies I/MR^2 = 2/5$.\n3. Acceleration: $a = \\frac{g\\sin\\theta}{1 + 2/5} = \\frac{5}{7}g\\sin\\theta$.\n4. Friction force required: $f = Mg\\sin\\theta - Ma = Mg\\sin\\theta - \\frac{5}{7}Mg\\sin\\theta = \\frac{2}{7}Mg\\sin\\theta$.\n5. Since $f \\le \\mu_s N = \\mu_s Mg\\cos\\theta \\implies \\frac{2}{7}Mg\\sin\\theta \\le \\mu_s Mg\\cos\\theta \\implies \\mu_s \\ge \\frac{2}{7}\\tan\\theta$.",
         "2/5 tan θ uses moment of inertia ratio directly; 1/3 tan θ applies to hollow sphere.",
         "Minimum friction coefficient for pure rolling of solid sphere is $\\mu_s \\ge \\frac{2}{7}\\tan\\theta$."),

        # 8. Gravitation - Properties of Gravitational Field
        ("Gravitation and Planetary Motion", "Properties of Gravitational Field and Potential", "Multi-Statement",
         "Which of the following statements regarding the gravitational field and potential are correct?\n\n"
         "A. Gravitational force between two point masses is a conservative central force.\n"
         "B. Gravitational potential inside a uniform thin spherical shell of mass $M$ and radius $R$ is constant and equal to $-GM/R$.\n"
         "C. Gravitational potential at the centre of a uniform solid sphere of radius $R$ is $1.5$ times the potential at its surface.\n"
         "D. Escape speed from the surface of Earth depends on the mass and angle of projection of the body.\n"
         "E. Kepler's second law of planetary motion (areolar velocity is constant) is a direct consequence of conservation of angular momentum.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, C and E only",
          "A, B and D only",
          "B, C, D and E only",
          "A, C and D only"], 0,
         "Statement D is false: escape speed $v_e = \\sqrt{2GM/R} = \\sqrt{2gR}$ depends only on the mass and radius of the planet, completely independent of the mass or projection angle of the projectile. Statements A, B, C, and E are precise NCERT gravitational laws.",
         "Escape speed is independent of the mass and angle of projection.",
         "Gravitational potential inside a shell is constant; at solid sphere centre it is $1.5 V_s$."),

        # 9. Gravitation - Gravitational Potential Calculation
        ("Gravitation and Planetary Motion", "Gravitational Potential Inside Solid Sphere", "Direct MCQ",
         "Assuming the Earth to be a uniform solid sphere of mass $M$ and radius $R$, the gravitational potential $V$ at a distance $r = R/2$ from the centre of the Earth (where $V_0 = -GM/R$ is the surface potential) is:",
         ["-11/8 (GM / R)", "-3/2 (GM / R)", "-5/4 (GM / R)", "-7/8 (GM / R)"], 0,
         "1. Gravitational potential inside a uniform solid sphere at distance $r \\le R$:\n   $$V(r) = -\\frac{GM}{2R^3}(3R^2 - r^2)$$.\n2. For $r = R/2$:\n   $$V(R/2) = -\\frac{GM}{2R^3}\\left(3R^2 - \\frac{R^2}{4}\\right) = -\\frac{GM}{2R^3}\\left(\\frac{11R^2}{4}\\right) = -\\frac{11}{8}\\frac{GM}{R}$$.\n3. Note: At the centre ($r=0$), $V_c = -\\frac{3}{2}\\frac{GM}{R} = 1.5 V_{\\text{surface}}$.",
         "-3/2 GM/R is potential at center ($r=0$); -5/4 uses linear interpolation.",
         "Gravitational potential inside a solid sphere: $V(r) = -\\frac{GM}{2R^3}(3R^2 - r^2)$."),

        # 10. Mechanical Properties of Fluids - Terminal Velocity
        ("Mechanical Properties of Fluids", "Stokes' Law and Viscosity vs Temperature", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** The terminal velocity of a small spherical raindrop falling through air is directly proportional to the square of its radius ($v_t \\propto r^2$).\n\n"
         "**Statement II:** The coefficient of viscosity of liquids decreases with increase in temperature, whereas that of gases increases with increase in temperature.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Stokes' law with buoyancy gives $v_t = \\frac{2r^2(\\rho - \\sigma)g}{9\\eta} \\implies v_t \\propto r^2$. Statement I is correct.\n2. In liquids, heating weakens cohesive intermolecular bonds, decreasing viscosity. In gases, heating increases molecular speed and collision rate, increasing viscosity ($\\eta \\propto \\sqrt{T}$). Both statements are accurate NCERT facts.",
         "Viscosity of gases INCREASES with temperature, unlike liquids.",
         "Terminal speed scales as $r^2$; liquid viscosity drops with temperature while gas viscosity rises."),

        # 11. Mechanical Properties of Fluids - Torricelli's Law
        ("Mechanical Properties of Fluids", "Bernoulli's Principle and Torricelli's Law", "Direct MCQ",
         "A large cylindrical water tank open at the top has a small orifice of area $a = 1.0\\text{ cm}^2$ near the bottom at depth $h = 5.0\\text{ m}$ below the water surface. The rate of flow of water from the orifice is ($g = 10\\text{ m/s}^2$):",
         ["1.0 L/s", "10.0 L/s", "0.5 L/s", "2.0 L/s"], 0,
         "1. Speed of efflux by Torricelli's Law: $v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 5.0} = \\sqrt{100} = 10\\text{ m/s}$.\n2. Volumetric flow rate: $Q = a \\cdot v = (1.0 \\times 10^{-4}\\text{ m}^2) \\times 10\\text{ m/s} = 10^{-3}\\text{ m}^3\\text{/s}$.\n3. Since $1\\text{ m}^3 = 1000\\text{ L}$, $Q = 10^{-3} \\times 1000 = 1.0\\text{ L/s}$.",
         "10.0 L/s forgets the $10^{-4}$ unit conversion for $\\text{cm}^2$.",
         "Torricelli's efflux velocity is $v = \\sqrt{2gh}$; flow rate is $Q = a\\sqrt{2gh}$."),

        # 12. Thermodynamics - Cyclic Work Done
        ("Thermodynamics", "First Law of Thermodynamics and Cyclic Process Work", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** For any cyclic thermodynamic process, the net change in internal energy ($\\Delta U$) over a complete cycle is zero, and net heat absorbed equals the net work done ($Q_{\\text{net}} = W_{\\text{net}}$).\n\n"
         "**Statement II:** The work done by an ideal gas in an isothermal reversible expansion is always greater than the work done in an adiabatic reversible expansion between the same initial state and final volume.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Internal energy is a state function: for any closed cycle returning to initial state, $\\Delta U = 0 \\implies Q = W$.\n2. On an indicator diagram, the isothermal curve ($PV = \\text{const}$) lies above the steeper adiabatic curve ($PV^\\gamma = \\text{const}$) during expansion; therefore the area under the isothermal curve is larger, meaning $W_{\\text{iso}} > W_{\\text{adi}}$. Both statements are accurate.",
         "Isothermal expansion curve has slope $-P/V$; adiabatic has steeper slope $-\\gamma P/V$.",
         "Cyclic process: $\\Delta U = 0$ and $Q = W$. Isothermal expansion work exceeds adiabatic expansion work."),

        # 13. Thermodynamics - Indicator Diagram
        ("Thermodynamics", "Indicator Diagram Cyclic Work Done", "Direct MCQ",
         "An ideal gas undergoes a cyclic thermodynamic process consisting of an ellipse on a $P-V$ diagram. The maximum and minimum pressures are $400\\text{ kPa}$ and $200\\text{ kPa}$, and maximum and minimum volumes are $60\\text{ L}$ and $20\\text{ L}$. The net work done during one complete clockwise cycle is:",
         ["3.14 kJ (π kJ)", "6.28 kJ (2π kJ)", "1.57 kJ (π/2 kJ)", "12.56 kJ (4π kJ)"], 0,
         "1. Net work done in a cyclic process equals the area enclosed by the cycle on a $P-V$ diagram.\n2. For an ellipse, $\\text{Area} = \\pi \\cdot a \\cdot b$, where $a$ and $b$ are semi-axes.\n3. Semi-major axis in pressure: $a = \\frac{P_{\\text{max}} - P_{\\text{min}}}{2} = \\frac{400 - 200}{2} = 100\\text{ kPa} = 10^5\\text{ Pa}$.\n4. Semi-minor axis in volume: $b = \\frac{V_{\\text{max}} - V_{\\text{min}}}{2} = \\frac{60 - 20}{2} = 20\\text{ L} = 20 \\times 10^{-3}\\text{ m}^3$.\n5. $W = \\pi \\times 10^5 \\times (20 \\times 10^{-3}) = 2000\\pi\\text{ J} \\approx 3141\\text{ J} \\approx 3.14\\text{ kJ}$.",
         "6.28 kJ uses full axes instead of semi-axes ($2a \\times 2b$); 12.56 kJ multiplies by 4.",
         "Work done in cyclic process = Area enclosed on $P-V$ indicator diagram."),

        # 14. Thermodynamics - Thermodynamic Processes Match List
        ("Thermodynamics", "Thermodynamic Processes and Heat Capacities", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Thermodynamic Process) | List-II (Condition / Heat Capacity) |\n"
         "| :--- | :--- |\n"
         "| **A.** Isothermal process | **I.** $\\Delta T = 0$, molar heat capacity $C = \\infty$ |\n"
         "| **B.** Adiabatic process | **II.** $\\Delta Q = 0$, molar heat capacity $C = 0$ |\n"
         "| **C.** Isochoric process | **III.** $\\Delta V = 0, W = 0, \\Delta Q = n C_v \\Delta T$ |\n"
         "| **D.** Isobaric process | **IV.** $\\Delta P = 0, W = P\\Delta V, \\Delta Q = n C_p \\Delta T$ |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "Isothermal: $\\Delta T = 0 \\implies C = \\Delta Q/(n \\cdot 0) = \\infty$ (A-I). Adiabatic: $\\Delta Q = 0 \\implies C = 0$ (B-II). Isochoric: constant volume, work is zero (C-III). Isobaric: constant pressure, $W = P\\Delta V$ (D-IV).",
         "Isothermal heat capacity is infinite; adiabatic heat capacity is zero.",
         "Heat capacities: Isothermal ($C=\\infty$), Adiabatic ($C=0$), Isochoric ($C=C_v$), Isobaric ($C=C_p$)."),

        # 15. Oscillations - SHM Dynamics Multi-Statement
        ("Oscillations and Simple Harmonic Motion", "Simple Harmonic Motion Dynamics", "Multi-Statement",
         "For a particle executing simple harmonic motion (SHM) with displacement $x = A\\sin(\\omega t)$, which of the following statements are correct?\n\n"
         "A. The velocity leads the displacement by a phase angle of $\\pi/2$ radians.\n"
         "B. The acceleration leads the displacement by a phase angle of $\\pi$ radians ($180^\\circ$).\n"
         "C. Total mechanical energy of SHM is directly proportional to the square of frequency ($E \\propto \\nu^2$) and square of amplitude ($E \\propto A^2$).\n"
         "D. Average kinetic energy over one complete cycle equals half of total mechanical energy ($E/2$).\n"
         "E. The frequency of oscillation of kinetic energy is equal to the frequency of oscillation of displacement.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, C and D only",
          "A, B and E only",
          "B, C, D and E only",
          "A, C and E only"], 0,
         "Statement E is incorrect: kinetic energy $E_k = \\frac{1}{2}m\\omega^2 A^2 \\cos^2(\\omega t) = \\frac{1}{4}m\\omega^2 A^2 (1 + \\cos 2\\omega t)$ oscillates at TWICE the frequency of displacement ($2\\nu$). Statements A, B, C, and D are authentic NCERT facts.",
         "Frequency of kinetic and potential energy in SHM is $2\\nu$, double the displacement frequency.",
         "In SHM: velocity leads displacement by $\\pi/2$, acceleration leads by $\\pi$, KE frequency is $2\\nu$."),

        # 16. Oscillations - Energy Calculation
        ("Oscillations and Simple Harmonic Motion", "Kinetic and Potential Energy of SHM", "Direct MCQ",
         "A particle executes simple harmonic motion with amplitude $A$. At what displacement $x$ from the mean equilibrium position does the kinetic energy of the particle equal twice its potential energy ($E_k = 2 E_p$)?",
         ["x = A / √3", "x = A / 2", "x = A / √2", "x = 2A / 3"], 0,
         "1. $E_k = \\frac{1}{2}m\\omega^2(A^2 - x^2)$ and $E_p = \\frac{1}{2}m\\omega^2 x^2$.\n2. Given $E_k = 2 E_p \\implies \\frac{1}{2}m\\omega^2(A^2 - x^2) = 2 \\left(\\frac{1}{2}m\\omega^2 x^2\\right)$.\n3. $A^2 - x^2 = 2x^2 \\implies 3x^2 = A^2 \\implies x = \\frac{A}{\\sqrt{3}}$.",
         "A / 2 gives $E_p = 25\\%, E_k = 75\\% \\implies E_k = 3E_p$; A / √2 gives $E_k = E_p$.",
         "In SHM, when $E_k = n E_p$, displacement is $x = \\frac{A}{\\sqrt{n+1}}$."),

        # 17. Waves - Organ Pipe Harmonics
        ("Waves and Sound (Doppler and Organ Pipes)", "Closed Organ Pipe Harmonics", "Direct MCQ",
         "A closed organ pipe of length $L_1 = 20\\text{ cm}$ has its fundamental frequency identical to the second overtone (third harmonic) of an open organ pipe of length $L_2$. The length $L_2$ of the open organ pipe is:",
         ["120 cm", "60 cm", "80 cm", "40 cm"], 0,
         "1. Fundamental frequency of closed pipe: $f_c = \\frac{v}{4 L_1}$.\n2. Harmonics of open pipe: $f_n = n \\frac{v}{2 L_2}$ ($n=1$ is fundamental, $n=2$ is 1st overtone, $n=3$ is 2nd overtone).\n3. Given $f_c = f_{o3} \\implies \\frac{v}{4 L_1} = 3 \\left(\\frac{v}{2 L_2}\\right)$.\n4. Simplifying: $\\frac{1}{4 L_1} = \\frac{3}{2 L_2} \\implies L_2 = 6 L_1$.\n5. Calculation: $L_2 = 6 \\times 20\\text{ cm} = 120\\text{ cm}$.",
         "60 cm treats 2nd overtone as $n=2$; 80 cm confuses open and closed formulas.",
         "Closed pipe fundamental is $\\frac{v}{4L_1}$; open pipe 2nd overtone is $3\\frac{v}{2L_2} \\implies L_2 = 6L_1$."),

        # 18. Electrostatics - Conductors Statement Pair
        ("Electrostatics and Electric Potential", "Electric Field and Potential of Conductors", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** The electric field inside the cavity of a charged hollow conductor is zero, irrespective of the shape and size of the cavity and presence of external fields (electrostatic shielding).\n\n"
         "**Statement II:** The electrostatic potential is constant throughout the volume of the conductor and has the same value on its surface as inside its cavity.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. By Gauss's Law, excess charge resides entirely on the outer surface of a conductor.\n2. Inside the conductor and its empty cavity, $\\vec{E} = 0$, shielding the interior from external electrostatic influence.\n3. Since $\\vec{E} = -\\nabla V = 0$, potential $V$ is constant throughout the entire conductor and cavity.\n4. Both statements are accurate NCERT textbook assertions.",
         "Distractors falsely claim potential inside is zero rather than constant.",
         "Inside a conductor, $\\vec{E} = 0$ and electrostatic potential $V$ is constant throughout its volume."),

        # 19. Electrostatics - Potential Energy Assembly
        ("Electrostatics and Electric Potential", "Work Done in Assembling Charges on Equilateral Triangle", "Direct MCQ",
         "Three identical point charges $+q$ are placed at the vertices of an equilateral triangle of side $a$. The work done by an external agent to slowly bring the three charges closer until the side of the triangle becomes $a/2$ is:",
         ["$\\frac{3q^2}{4\\pi\\varepsilon_0 a}$", "$\\frac{q^2}{4\\pi\\varepsilon_0 a}$", "$\\frac{6q^2}{4\\pi\\varepsilon_0 a}$", "$\\frac{3}{2}\\frac{q^2}{4\\pi\\varepsilon_0 a}$"], 0,
         "1. Initial potential energy of 3 pairs: $U_i = 3 \\left(\\frac{k q^2}{a}\\right)$.\n2. Final potential energy with side $a/2$: $U_f = 3 \\left(\\frac{k q^2}{a/2}\\right) = 6 \\left(\\frac{k q^2}{a}\\right)$.\n3. External work done: $W_{\\text{ext}} = U_f - U_i = 6 \\frac{k q^2}{a} - 3 \\frac{k q^2}{a} = 3 \\frac{k q^2}{a} = \\frac{3 q^2}{4\\pi\\varepsilon_0 a}$.",
         "6 q^2 / (4πε_0 a) is final energy; q^2 / (4πε_0 a) considers only a single pair.",
         "Work done by external agent equals change in electrostatic potential energy: $W_{\\text{ext}} = \\Delta U$."),

        # 20. Capacitance - Dielectric Insertion Assertion-Reason
        ("Capacitance and Dielectric Polarization", "Capacitor with Dielectric and Energy Storage", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** When a dielectric slab of dielectric constant $K > 1$ is inserted between the plates of an isolated charged parallel-plate capacitor, the electrostatic potential energy stored in the capacitor decreases by a factor of $K$.\n\n"
         "**Reason (R):** For an isolated capacitor, the electric charge $Q$ on the plates remains conserved, and the capacitance increases to $K C_0$, resulting in $U = \\frac{Q^2}{2 K C_0} = \\frac{U_0}{K}$.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "Because the capacitor is isolated (disconnected from the battery), its charge $Q$ is constant. Capacitance increases by factor $K$. Energy $U = \\frac{Q^2}{2C} = \\frac{U_0}{K}$. The electrostatic field pulls the dielectric in, doing work and lowering stored energy. Reason directly explains Assertion.",
         "If battery remained connected, energy would INCREASE by factor $K$ ($U = \\frac{1}{2}K C V^2$).",
         "Isolated capacitor: charge is conserved, capacitance increases by $K$, energy decreases by factor $K$."),

        # 21. Current Electricity - Meter Bridge
        ("Current Electricity and Electrical Instruments", "Meter Bridge End Correction", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** In a Meter Bridge experiment, it is preferred to obtain the balance point near the middle of the wire ($40\\text{ cm}$ to $60\\text{ cm}$).\n\n"
         "**Reason (R):** The sensitivity of the Wheatstone bridge is maximum when all four arms have nearly equal resistances, which minimizes the percentage error in the determination of unknown resistance.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Meter bridge is based on Wheatstone bridge balance principle: $\\frac{R}{S} = \\frac{l}{100-l}$.\n2. The bridge achieves maximum deflection sensitivity when all four bridge arms are approximately equal in resistance ($R \\approx S \\implies l \\approx 50\\text{ cm}$).\n3. Balancing near the ends ($l < 10\\text{ cm}$ or $l > 90\\text{ cm}$) introduces high relative fractional errors due to end-strip resistances.\n4. Hence both (A) and (R) are true, and (R) is the correct explanation.",
         "Distractors claim end correction is identical at all balance positions.",
         "Wheatstone bridge has maximum sensitivity when all four arms are nearly equal, giving balance near the middle."),

        # 22. Current Electricity - Galvanometer Conversion
        ("Current Electricity and Electrical Instruments", "Galvanometer Conversion to Ammeter and Voltmeter", "Direct MCQ",
         "A galvanometer of coil resistance $G = 50\\ \\Omega$ gives full scale deflection for a current of $I_g = 2\\text{ mA}$. To convert it into a voltmeter of range $0 - 10\\text{ V}$, the resistance $R$ connected in series with the galvanometer must be:",
         ["4950 Ω", "5000 Ω", "4500 Ω", "5050 Ω"], 0,
         "1. For voltmeter conversion, a high series resistance $R$ is added: $V = I_g(G + R)$.\n2. Rearranging: $R = \\frac{V}{I_g} - G$.\n3. Calculation: $R = \\frac{10}{2 \\times 10^{-3}} - 50 = 5000 - 50 = 4950\\ \\Omega$.",
         "5000 Ω neglects the internal resistance $G = 50\\ \\Omega$; 5050 Ω adds $G$ instead of subtracting.",
         "Series resistance for voltmeter: $R = V/I_g - G$."),

        # 23. Moving Charges - Semicircular Wire Field
        ("Moving Charges and Magnetism", "Magnetic Field at Centre of Semicircular Wire", "Direct MCQ",
         "A wire carrying steady current $I$ is bent into a semicircle of radius $R$ with two straight segments extending to infinity along the axis of diameter. The magnetic field at the centre of the semicircular arc is:",
         ["μ_0 I / (4 R)", "μ_0 I / (2 R)", "μ_0 I / (8 R)", "μ_0 I / (2π R)"], 0,
         "1. By Biot-Savart Law, the straight wire sections lie along the line pointing directly to and from the centre ($\\vec{dl} \\parallel \\hat{r}$), so their cross product $\\vec{dl} \\times \\hat{r} = 0$.\n2. The semicircular arc of angle $\\pi$ radians contributes half of a full circular loop:\n   $$B = \\frac{1}{2} \\left(\\frac{\\mu_0 I}{2R}\\right) = \\frac{\\mu_0 I}{4 R}$$.\n3. Direction is perpendicular into or out of the plane by right-hand rule.",
         "μ_0 I / (2 R) is for a full circle; μ_0 I / (2π R) is for straight wire.",
         "A semicircular arc contributes exactly half of a circular loop field: $B = \\frac{\\mu_0 I}{4R}$."),

        # 24. Magnetism & Matter - Match List
        ("Magnetism and Matter (Earth Magnetism & Materials)", "Magnetic Properties of Materials Match List", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Magnetic Material) | List-II (Magnetic Susceptibility χ and Permeability μ_r) |\n"
         "| :--- | :--- |\n"
         "| **A.** Diamagnetic | **I.** $\\chi < 0$ (small and negative), $\\mu_r < 1$, independent of temperature |\n"
         "| **B.** Paramagnetic | **II.** $\\chi > 0$ (small and positive), $\\mu_r > 1$, inversely proportional to temperature ($\\chi \\propto 1/T$) |\n"
         "| **C.** Ferromagnetic | **III.** $\\chi \\gg 1$ (very large and positive), $\\mu_r \\gg 1$, obeys Curie-Weiss law above $T_c$ |\n"
         "| **D.** Superconductor | **IV.** Perfect diamagnetism with $\\chi = -1$ and $\\mu_r = 0$ (Meissner effect) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. Diamagnetic: $\\chi$ is small and negative ($-10^{-5}$ to $-10^{-9}$), independent of temperature $\\to$ I.\n2. Paramagnetic: $\\chi$ is small and positive, obeys Curie's law $\\chi = C/T \\to$ II.\n3. Ferromagnetic: $\\chi \\gg 1$, transitions to paramagnetism above Curie temperature $T_c \\to$ III.\n4. Superconductors: Expel magnetic field completely (Meissner effect), exhibiting $\\chi = -1 \\to$ IV.",
         "Distractors swap paramagnetic and diamagnetic susceptibility signs.",
         "Susceptibilities: Diamagnetic ($-1 \\le \\chi < 0$), Paramagnetic ($0 < \\chi \\ll 1$), Ferromagnetic ($\\chi \\gg 1$)."),

        # 25. Magnetism & Matter - Curie-Weiss Statement Pair
        ("Magnetism and Matter (Earth Magnetism & Materials)", "Curie-Weiss Law and Diamagnetism", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Diamagnetic materials have negative magnetic susceptibility ($\\chi < 0$) and are feebly repelled by magnetic fields, independent of temperature.\n\n"
         "**Statement II:** Ferromagnetic materials obey the Curie-Weiss law $\\chi = \\frac{C}{T - T_c}$ above their Curie temperature $T_c$, where they transition to paramagnetic behavior.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Diamagnetism originates from orbital electronic motion and induced magnetic moments opposing external field (Lenz's law); it is essentially independent of temperature.\n2. Above the Curie temperature ($T_c$), thermal agitation destroys domain alignment in ferromagnetic materials, converting them into paramagnets obeying Curie-Weiss law: $\\chi = \\frac{C}{T - T_c}$. Both statements are accurate.",
         "Paramagnetic materials obey Curie law $\\chi = C/T$; ferromagnets above $T_c$ obey Curie-Weiss law.",
         "Diamagnetism is temperature-independent; ferromagnetism transitions to paramagnetism above Curie temperature."),

        # 26. EMI - Induced EMF in Rotating Rod
        ("Electromagnetic Induction and Lenz's Law", "Motional EMF in Rotating Metallic Rod", "Direct MCQ",
         "A metal rod of length $L = 1.0\\text{ m}$ is rotated with a constant angular speed $\\omega = 100\\text{ rad/s}$ about an axis passing through one of its ends, perpendicular to its length, in a uniform magnetic field $B = 0.4\\text{ T}$ directed parallel to the axis of rotation. The induced EMF between the two ends of the rod is:",
         ["20 V", "40 V", "10 V", "80 V"], 0,
         "1. Consider an element $dr$ at distance $r$ from the axis rotating at speed $v = \\omega r$.\n2. Induced motional EMF in element: $d\\mathcal{E} = B v dr = B (\\omega r) dr$.\n3. Integrating from $r = 0$ to $r = L$:\n   $$\\mathcal{E} = \\int_0^L B \\omega r dr = \\frac{1}{2} B \\omega L^2$$.\n4. Substituting values: $\\mathcal{E} = \\frac{1}{2} \\times 0.4 \\times 100 \\times (1.0)^2 = 0.2 \\times 100 = 20\\text{ V}$.",
         "40 V forgets the factor of $1/2$ from integration ($BL^2\\omega$); 10 V divides by 4.",
         "Induced EMF in rotating rod about one end is $\\mathcal{E} = \\frac{1}{2} B \\omega L^2$."),

        # 27. AC Circuits - Match List
        ("Alternating Current and LCR Circuits", "AC Circuit Components and Phase Relations", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (AC Circuit Element) | List-II (Phase Difference Between Current and Voltage) |\n"
         "| :--- | :--- |\n"
         "| **A.** Pure Resistor ($R$) | **I.** Current and voltage are in same phase ($\\phi = 0$) |\n"
         "| **B.** Pure Inductor ($L$) | **II.** Current lags voltage by $\\pi/2$ radians ($90^\\circ$) |\n"
         "| **C.** Pure Capacitor ($C$) | **III.** Current leads voltage by $\\pi/2$ radians ($90^\\circ$) |\n"
         "| **D.** Series LCR at Resonance | **IV.** Impedance is minimum ($Z = R$) and $\\phi = 0$ |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-III, C-II, D-IV",
          "A-III, B-II, C-I, D-IV"], 0,
         "Resistor: $\\phi = 0$ (A-I). Inductor: current lags by $90^\\circ$ (B-II). Capacitor: current leads by $90^\\circ$ (C-III). LCR at resonance: $X_L = X_C \\implies Z = R$, current in phase with voltage (D-IV).",
         "CIVIL mnemonic: in Capacitor, I leads V; V leads I in Inductor.",
         "Phase: Inductor current lags by $\\pi/2$; Capacitor current leads by $\\pi/2$; Resistor is in phase."),

        # 28. AC Circuits - Power in Inductor
        ("Alternating Current and LCR Circuits", "Power Consumed in AC Inductive Circuit", "Direct MCQ",
         "An alternating voltage $V(t) = 200 \\sin(100\\pi t)\\text{ V}$ is applied across an ideal pure inductor of inductance $L = 0.5\\text{ H}$. The average power dissipated in the inductor over a complete cycle is:",
         ["0 W", "100 W", "50 W", "200 W"], 0,
         "1. In an ideal pure inductor, the alternating current lags behind the voltage by a phase angle of $\\phi = 90^\\circ$ ($\\pi/2$ radians).\n2. Power factor is $\\cos\\phi = \\cos 90^\\circ = 0$.\n3. Average power: $P_{\\text{av}} = V_{\\text{rms}} I_{\\text{rms}} \\cos\\phi = V_{\\text{rms}} I_{\\text{rms}} (0) = 0\\text{ W}$.\n4. The current is entirely wattless.",
         "Distractors compute $V^2/\\omega L$ or assume ohmic resistive dissipation.",
         "Pure inductors and pure capacitors dissipate zero average power over a complete cycle ($\\cos 90^\\circ = 0$)."),

        # 29. EM Waves - Match List
        ("Electromagnetic Waves and Spectrum", "Electromagnetic Waves and Spectrum Uses", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Electromagnetic Wave) | List-II (Primary Practical Application / Feature) |\n"
         "| :--- | :--- |\n"
         "| **A.** Microwaves | **I.** RADAR systems in aircraft navigation and microwave ovens |\n"
         "| **B.** Infrared waves | **II.** Greenhouse effect, physical therapy, and remote control controls |\n"
         "| **C.** Ultraviolet rays | **III.** LASIK eye surgery and water purification sterilizers |\n"
         "| **D.** X-rays | **IV.** Diagnostic imaging for bone fractures and crystal structure study |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-IV, B-II, C-III, D-I"], 0,
         "Microwaves: RADAR and microwave ovens (A-I). Infrared: Heat radiation and remotes (B-II). Ultraviolet: LASIK and germicidal sterilizers (C-III). X-rays: Bone imaging and crystallography (D-IV).",
         "Confusing UV (germicidal) with IR (thermal/heat) is a frequent mistake.",
         "EM spectrum: Radiowaves -> Microwaves -> Infrared -> Visible -> Ultraviolet -> X-rays -> Gamma rays."),

        # 30. EM Waves - Energy Density Ratio
        ("Electromagnetic Waves and Spectrum", "Electromagnetic Wave Energy Density Ratio", "Direct MCQ",
         "In a plane electromagnetic wave propagating through vacuum, the ratio of average energy density stored in the electric field ($u_E = \\frac{1}{2}\\varepsilon_0 E_{\\text{rms}}^2$) to that stored in the magnetic field ($u_B = \\frac{1}{2\\mu_0} B_{\\text{rms}}^2$) is:",
         ["$1 : 1$", "$c : 1$", "$1 : c^2$", "$c^2 : 1$"], 0,
         "1. Electric energy density: $u_E = \\frac{1}{2}\\varepsilon_0 E_{\\text{rms}}^2$.\n2. Since $E_{\\text{rms}} = c B_{\\text{rms}}$ and $c^2 = \\frac{1}{\\mu_0 \\varepsilon_0}$:\n   $$u_E = \\frac{1}{2}\\varepsilon_0 (c B_{\\text{rms}})^2 = \\frac{1}{2}\\varepsilon_0 c^2 B_{\\text{rms}}^2 = \\frac{1}{2}\\varepsilon_0 \\left(\\frac{1}{\\mu_0 \\varepsilon_0}\\right) B_{\\text{rms}}^2 = \\frac{B_{\\text{rms}}^2}{2\\mu_0} = u_B$$.\n3. Hence, electric and magnetic energy densities in an EM wave are exactly equal ($u_E : u_B = 1 : 1$).",
         "Distractors mistakenly think electric field stores more energy because $E_0 = c B_0$.",
         "In an electromagnetic wave, energy is divided equally between electric and magnetic fields: $u_E = u_B$ (1:1)."),

        # 31. Ray Optics - Lens Immersion
        ("Ray Optics and Optical Instruments", "Lens Maker Formula with Immersion in Liquid", "Direct MCQ",
         "A biconvex lens of glass (refractive index $\\mu_g = 1.5$) has focal length $f = 20\\text{ cm}$ in air. When completely immersed in water (refractive index $\\mu_w = 4/3$), its new focal length $f_w$ becomes:",
         ["80 cm", "40 cm", "60 cm", "10 cm"], 0,
         "1. Lens maker's formula in air: $\\frac{1}{f_a} = (\\mu_g - 1)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) = (1.5 - 1) K = 0.5 K \\implies K = \\frac{2}{f_a}$.\n2. In water: $\\frac{1}{f_w} = \\left(\\frac{\\mu_g}{\\mu_w} - 1\\right) K = \\left(\\frac{1.5}{4/3} - 1\\right) K = \\left(\\frac{9}{8} - 1\\right) K = \\frac{1}{8} K$.\n3. Dividing the two relations: $\\frac{f_w}{f_a} = \\frac{0.5}{1/8} = 4$.\n4. New focal length: $f_w = 4 \\times 20\\text{ cm} = 80\\text{ cm}$.",
         "40 cm assumes doubling; 10 cm assumes focal length decreases in medium.",
         "When a glass lens ($\\mu=1.5$) is immersed in water ($\\mu=4/3$), its focal length quadruples: $f_w = 4 f_a$."),

        # 32. Ray Optics - TIR in Optical Fibers
        ("Ray Optics and Optical Instruments", "Total Internal Reflection and Optical Fibers", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** In an optical fiber, light signals can travel through long distances with negligible loss of energy, even if the fiber is curved or bent.\n\n"
         "**Reason (R):** Optical fibers consist of a central glass core surrounded by a cladding of slightly lower refractive index, such that light entering the core undergoes repeated total internal reflections at angles greater than the critical angle.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "Optical fibers guide light via successive total internal reflections. Because $n_{\\text{core}} > n_{\\text{cladding}}$, rays incident at angles exceeding critical angle $i_c = \\sin^{-1}(n_2/n_1)$ are $100\\%$ reflected back into the core without refractive transmission loss. Both statements are true and Reason directly explains Assertion.",
         "Cladding must have LOWER refractive index than core, not higher.",
         "Total internal reflection requires: (1) denser to rarer medium ($n_{\\text{core}} > n_{\\text{clad}}$), and (2) angle of incidence $i > i_c$."),

        # 33. Ray Optics - Optical Instruments Match List
        ("Ray Optics and Optical Instruments", "Optical Instruments and Image Characteristics", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Optical Instrument) | List-II (Final Image Characteristic & Formula) |\n"
         "| :--- | :--- |\n"
         "| **A.** Simple Microscope | **I.** Virtual, erect, magnified at near point ($m = 1 + D/f$) |\n"
         "| **B.** Compound Microscope | **II.** Virtual, inverted with respect to object ($m \\approx -\\frac{L}{f_o}\\frac{D}{f_e}$) |\n"
         "| **C.** Astronomical Telescope (Normal adjustment) | **III.** Virtual, inverted at infinity ($m = -f_o/f_e$, tube length $L = f_o + f_e$) |\n"
         "| **D.** Cassegrain Reflecting Telescope | **IV.** Uses concave parabolic primary mirror and convex secondary mirror |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-II, C-I, D-IV"], 0,
         "Simple microscope: $m = 1 + D/f$ (A-I). Compound microscope: real inverted intermediate image, final magnified inverted image (B-II). Astronomical telescope in normal adjustment: image at infinity, $m = -f_o/f_e$ (C-III). Cassegrain reflector: parabolic primary and convex secondary (D-IV).",
         "Telescope has $f_o \\gg f_e$; microscope has $f_o < f_e$.",
         "Magnifications: Simple microscope ($1+D/f$), Compound microscope ($-L D / f_o f_e$), Telescope ($-f_o/f_e$)."),

        # 34. Wave Optics - YDSE Thin Sheet
        ("Wave Optics and Interference", "YDSE Fringe Shift due to Thin Sheet", "Direct MCQ",
         "In a Young's double-slit experiment using light of wavelength $\\lambda = 600\\text{ nm}$, a thin transparent glass sheet of refractive index $\\mu = 1.5$ is introduced in front of one of the slits. If the central bright fringe shifts to the position originally occupied by the $5\\text{th}$ bright fringe, the thickness of the glass sheet is:",
         ["6.0 μm", "3.0 μm", "1.5 μm", "12.0 μm"], 0,
         "1. Additional optical path difference introduced by sheet of thickness $t$: $\\Delta x = (\\mu - 1)t$.\n2. The fringe shift corresponds to 5 full fringe widths: $\\Delta x = 5\\lambda$.\n3. Equating: $(\\mu - 1)t = 5\\lambda \\implies (1.5 - 1)t = 5 \\times 600 \\times 10^{-9}\\text{ m}$.\n4. $0.5 t = 3000\\text{ nm} \\implies t = 6000\\text{ nm} = 6.0\\ \\mu\\text{m}$.",
         "3.0 μm forgets the $0.5$ factor in denominator; 1.5 μm divides by $(\\mu+1)$.",
         "Fringe shift condition in YDSE: $(\\mu - 1)t = n\\lambda$."),

        # 35. Wave Optics - Coherent Sources Statement Pair
        ("Wave Optics and Interference", "Wave Optics Coherent Sources and Interference", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Sustained interference fringes can be observed only if the two light sources are coherent, having a constant or zero phase difference.\n\n"
         "**Statement II:** Two independent sodium vapor lamps can never act as coherent sources because individual atoms emit light in independent wave-trains with random phase shifts every $10^{-10}\\text{ s}$.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Coherent sources maintain a constant phase difference; without coherence, the interference pattern shifts rapidly and washes out to a uniform intensity distribution.\n2. Independent lamps have atoms undergoing spontaneous emission independently with random phase jumps on $10^{-10}\\text{ s}$ scale; thus two independent sources cannot be mutually coherent. Both statements are correct.",
         "Two independent light bulbs produce incoherent illumination, not an interference pattern.",
         "Coherence requires constant phase difference; independent sources cannot produce sustained interference."),

        # 36. Wave Optics - Interference vs Diffraction Multi-Statement
        ("Wave Optics and Interference", "Interference and Diffraction Differences", "Multi-Statement",
         "Which of the following statements correctly distinguish Young's double-slit interference from single-slit Fraunhofer diffraction?\n\n"
         "A. Interference is the superposition of waves from two distinct coherent wave fronts, whereas diffraction is superposition of secondary wavelets originating from different parts of the same wave front.\n"
         "B. In interference, all bright fringes have equal intensity, whereas in diffraction, the central maximum has the highest intensity and subsequent secondary maxima rapidly decrease in brightness.\n"
         "C. In double-slit interference, fringe width is constant ($\\beta = \\lambda D / d$), whereas in single-slit diffraction, the central maximum width ($2\\lambda D / a$) is twice the width of secondary maxima.\n"
         "D. In interference, the minima are completely dark if source intensities are equal, whereas in diffraction, minima are never completely dark.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B and C only",
          "A and B only",
          "B, C and D only",
          "A, B, C and D"], 0,
         "Statements A, B, and C are authentic NCERT facts distinguishing interference from diffraction. Statement D is incorrect because in single-slit Fraunhofer diffraction, at angles satisfying $a\\sin\\theta = n\\lambda$ ($n = \\pm 1, \\pm 2, \\dots$), complete destructive interference occurs, yielding completely dark minima of zero intensity.",
         "Diffraction minima have exactly zero intensity at $a\\sin\\theta = n\\lambda$.",
         "Interference: equal fringe widths and equal intensities; Diffraction: central maximum is twice as wide and brightest."),

        # 37. Dual Nature - Photoelectric Effect Statement Pair
        ("Dual Nature of Radiation and Matter", "Photoelectric Stopping Potential vs Intensity and Frequency", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** For a given photosensitive material and frequency of incident radiation (above threshold frequency), the photoelectric saturation current is directly proportional to the intensity of incident light.\n\n"
         "**Statement II:** The stopping potential (and maximum kinetic energy of emitted photoelectrons) depends linearly on the frequency of incident radiation, but is independent of its intensity.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Intensity measures photon arrival rate ($N/t$). Higher intensity delivers more photons, ejecting more photoelectrons per second, thus saturation current $I \\propto \\text{Intensity}$.\n2. By Einstein's equation $eV_0 = K_{\\text{max}} = h\\nu - \\Phi_0$, the stopping potential depends solely on incident frequency $\\nu$ and material work function $\\Phi_0$, completely independent of intensity. Both statements are accurate.",
         "Intensity determines number of emitted photoelectrons, not their maximum kinetic energy.",
         "Saturation current $\\propto$ Intensity; Stopping potential depends on frequency $\\nu$ and work function $\\Phi_0$."),

        # 38. Dual Nature - Stopping Potential Calculation
        ("Dual Nature of Radiation and Matter", "Photoelectric Stopping Potential vs Frequency", "Direct MCQ",
         "In a photoelectric effect experiment, when radiation of frequency $\\nu$ is incident on a metal surface, the stopping potential is $V_1$. When frequency is doubled to $2\\nu$, the stopping potential becomes $V_2$. The relationship between $V_2$ and $V_1$ is:",
         ["$V_2 > 2 V_1$", "$V_2 = 2 V_1$", "$V_2 < 2 V_1$", "$V_2 = V_1 + \\frac{h\\nu}{e}$"], 0,
         "1. Einstein's photoelectric equation: $e V_1 = h\\nu - \\Phi_0 \\implies h\\nu = e V_1 + \\Phi_0$.\n2. For frequency $2\\nu$:\n   $$e V_2 = h(2\\nu) - \\Phi_0 = 2(h\\nu) - \\Phi_0 = 2(e V_1 + \\Phi_0) - \\Phi_0 = 2e V_1 + \\Phi_0$$.\n3. Dividing by $e$: $V_2 = 2 V_1 + \\frac{\\Phi_0}{e}$.\n4. Since work function $\\Phi_0 > 0$, it follows that $V_2 > 2 V_1$.",
         "V_2 = 2 V_1 ignores work function subtraction; V_2 < 2 V_1 inverts the inequality.",
         "Doubling incident frequency more than doubles stopping potential: $V_2 = 2V_1 + \\Phi_0/e > 2V_1$."),

        # 39. Atoms - de Broglie Wavelength of Electron
        ("Atoms and Bohr Model", "de Broglie Wavelength of Accelerated Electron", "Direct MCQ",
         "An electron is accelerated from rest through an electric potential difference of $V = 100\\text{ V}$. Its de Broglie wavelength $\\lambda$ is approximately:",
         ["0.123 nm (1.23 Å)", "1.23 nm", "0.0123 nm", "0.246 nm"], 0,
         "1. De Broglie wavelength of electron accelerated through potential $V$:\n   $$\\lambda = \\frac{h}{\\sqrt{2 m_e e V}} = \\frac{1.227}{\\sqrt{V}}\\text{ nm} = \\frac{12.27}{\\sqrt{V}}\\text{ \\AA}$$.\n2. For $V = 100\\text{ V}$:\n   $$\\lambda = \\frac{1.227}{\\sqrt{100}} = \\frac{1.227}{10} = 0.1227\\text{ nm} \\approx 0.123\\text{ nm} = 1.23\\text{ \\AA}$$.",
         "1.23 nm forgets the square root of 100 in denominator.",
         "Electron de Broglie wavelength: $\\lambda = \\frac{1.227}{\\sqrt{V}}\\text{ nm}$. For $100\\text{ V}$, $\\lambda = 0.123\\text{ nm}$."),

        # 40. Atoms - Lyman Series Wavelength Ratio
        ("Atoms and Bohr Model", "Ratio of Longest to Shortest Wavelength in Lyman Series", "Direct MCQ",
         "The ratio of the longest wavelength (first line, $\\alpha$-line) to the shortest wavelength (series limit) in the Lyman series of the hydrogen spectrum is:",
         ["4 / 3", "3 / 4", "9 / 8", "16 / 15"], 0,
         "1. Rydberg formula: $\\frac{1}{\\lambda} = R_H \\left(\\frac{1}{n_1^2} - \\frac{1}{n_2^2}\\right)$.\n2. For Lyman series, $n_1 = 1$.\n3. Longest wavelength (minimum energy, $n_2 = 2$):\n   $$\\frac{1}{\\lambda_{\\text{max}}} = R_H \\left(1 - \\frac{1}{4}\\right) = \\frac{3}{4}R_H \\implies \\lambda_{\\text{max}} = \\frac{4}{3R_H}$$.\n4. Shortest wavelength (maximum energy, series limit, $n_2 = \\infty$):\n   $$\\frac{1}{\\lambda_{\\text{min}}} = R_H (1 - 0) = R_H \\implies \\lambda_{\\text{min}} = \\frac{1}{R_H}$$.\n5. Ratio: $\\frac{\\lambda_{\\text{max}}}{\\lambda_{\\text{min}}} = \\frac{4/(3R_H)}{1/R_H} = \\frac{4}{3}$.",
         "3/4 is the inverse ratio; 9/8 applies to Balmer series.",
         "In Lyman series, $\\lambda_{\\text{max}}/\\lambda_{\\text{min}} = \\frac{4}{3}$."),

        # 41. Atoms - He+ Ionization Energy
        ("Atoms and Bohr Model", "Ionization Potential of He+ Ion", "Direct MCQ",
         "The ground state energy of hydrogen atom is $-13.6\\text{ eV}$. The ionization energy required to remove the electron from the ground state ($n=1$) of singly ionized helium ($\\text{He}^+, Z=2$) is:",
         ["54.4 eV", "27.2 eV", "13.6 eV", "122.4 eV"], 0,
         "1. Energy levels of hydrogen-like species: $E_n = -13.6 \\frac{Z^2}{n^2}\\text{ eV}$.\n2. For $\\text{He}^+$, atomic number $Z = 2$.\n3. Ground state energy ($n=1$): $E_1 = -13.6 \\times \\frac{2^2}{1^2} = -13.6 \\times 4 = -54.4\\text{ eV}$.\n4. Ionization energy is the energy required to excite from ground state to infinity: $E_{\\text{ion}} = 0 - E_1 = +54.4\\text{ eV}$.",
         "27.2 eV scales linearly with $Z$; 13.6 eV forgets $Z^2$ factor.",
         "Ionization energy of hydrogen-like ions scales as $Z^2$: for $\\text{He}^+$, it is $4 \\times 13.6 = 54.4\\text{ eV}$."),

        # 42. Nuclei - Statement Pair
        ("Nuclei, Binding Energy and Radioactivity", "Nuclear Density and Binding Energy", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** The nuclear mass density of all atomic nuclei is approximately constant (nearly $2.3 \\times 10^{17}\\text{ kg/m}^3$), independent of their mass number $A$.\n\n"
         "**Statement II:** Nuclear radius $R$ is proportional to the cube root of the mass number ($R = R_0 A^{1/3}$), so the nuclear volume increases linearly with mass number $A$.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Nuclear radius: $R = R_0 A^{1/3}$, where $R_0 \\approx 1.2\\text{ fm}$.\n2. Nuclear volume: $V = \\frac{4}{3}\\pi R^3 = \\frac{4}{3}\\pi R_0^3 A \\propto A$.\n3. Nuclear mass: $M \\approx A \\times m_N$.\n4. Density: $\\rho = \\frac{M}{V} = \\frac{A m_N}{\\frac{4}{3}\\pi R_0^3 A} = \\frac{m_N}{\\frac{4}{3}\\pi R_0^3} = \\text{constant} \\approx 2.3 \\times 10^{17}\\text{ kg/m}^3$.\n5. Both statements are scientifically accurate and Statement II explains Statement I.",
         "Distractors claim nuclear density increases with heavier nuclei like Uranium.",
         "Nuclear radius scales as $A^{1/3}$, making nuclear density approximately constant ($~2.3 \\times 10^{17}\\text{ kg/m}^3$) for all elements."),

        # 43. Nuclei - Radioactive Decay
        ("Nuclei, Binding Energy and Radioactivity", "Radioactive Decay Half-Life Fraction", "Direct MCQ",
         "A radioactive isotope has a half-life of $T_{1/2} = 5\\text{ days}$. Starting with an initial sample containing $N_0$ active nuclei, the fraction of nuclei remaining undecayed after $20\\text{ days}$ is:",
         ["1/16 (6.25%)", "1/8 (12.5%)", "1/32 (3.125%)", "1/4 (25%)"], 0,
         "1. Number of elapsed half-lives: $n = \\frac{t}{T_{1/2}} = \\frac{20\\text{ days}}{5\\text{ days}} = 4$.\n2. Law of radioactive decay: $N = N_0 \\left(\\frac{1}{2}\\right)^n$.\n3. For $n = 4$: $N = N_0 \\left(\\frac{1}{2}\\right)^4 = \\frac{N_0}{16} = 0.0625 N_0$ ($6.25\\%$).",
         "1/8 is after 3 half-lives (15 days); 1/32 is after 5 half-lives (25 days).",
         "Remaining radioactive fraction after $n$ half-lives is $(1/2)^n$."),

        # 44. Semiconductors - Diode Depletion Layer Assertion-Reason
        ("Semiconductor Electronics and Logic Gates", "Semi-conductor Depletion Layer and Reverse Bias", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** In a reverse-biased $p-n$ junction diode, the width of the depletion layer increases and practically no current flows across the junction except for a very small reverse saturation current.\n\n"
         "**Reason (R):** The applied reverse bias voltage has the same polarity as the built-in barrier potential, which drives majority charge carriers away from the junction, leaving behind uncovered immobile ionized dopant atoms.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "In reverse bias, positive terminal connects to n-side and negative to p-side. This pulls majority electrons and holes away from junction, widening the depletion region. The small reverse current is carried solely by thermally generated minority carriers. Both statements are true and Reason directly explains Assertion.",
         "Forward bias decreases depletion width and lowers junction barrier height.",
         "Reverse bias increases depletion layer width and barrier height, blocking majority carriers."),

        # 45. Semiconductors - Zener Diode Calculation
        ("Semiconductor Electronics and Logic Gates", "Zener Diode Voltage Regulator Calculation", "Direct MCQ",
         "A $10\\text{ V}$ Zener diode is used along with a series resistance $R_s = 200\\ \\Omega$ to regulate a variable unregulated DC input voltage that fluctuates between $16\\text{ V}$ and $24\\text{ V}$. If the load resistance is $R_L = 1\\ \\text{k}\\Omega$, the maximum Zener current $I_Z$ through the diode is:",
         ["60 mA", "70 mA", "50 mA", "40 mA"], 0,
         "1. Regulated load voltage across $R_L$: $V_L = V_Z = 10\\text{ V}$.\n2. Constant load current: $I_L = \\frac{V_Z}{R_L} = \\frac{10\\text{ V}}{1000\\ \\Omega} = 10\\text{ mA}$.\n3. Maximum total current from source occurs at maximum input voltage $V_{\\text{in,max}} = 24\\text{ V}$:\n   $$I_{\\text{max}} = \\frac{V_{\\text{in,max}} - V_Z}{R_s} = \\frac{24 - 10}{200\\ \\Omega} = \\frac{14}{200}\\text{ A} = 0.070\\text{ A} = 70\\text{ mA}$$.\n4. Maximum Zener current: $I_{Z,\\text{max}} = I_{\\text{max}} - I_L = 70\\text{ mA} - 10\\text{ mA} = 60\\text{ mA}$.",
         "70 mA forgets to subtract the load current; 50 mA evaluates at nominal voltage.",
         "Zener diode absorbs excess current: $I_Z = I_{\\text{total}} - I_L$."),

        # 46. Semiconductors - Universal Gates Match List
        ("Semiconductor Electronics and Logic Gates", "Universal Logic Gates Combination", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Logic Gate Configuration) | List-II (Equivalent Boolean Operation) |\n"
         "| :--- | :--- |\n"
         "| **A.** NAND gate with inputs tied together ($A = B$) | **I.** NOT gate ($Y = \\overline{A}$) |\n"
         "| **B.** NOR gate with inputs tied together ($A = B$) | **II.** NOT gate ($Y = \\overline{A}$) |\n"
         "| **C.** Two NAND gates with inverted inputs via De Morgan's theorem | **III.** OR gate ($Y = A + B$) |\n"
         "| **D.** Two NOR gates with inverted inputs via De Morgan's theorem | **IV.** AND gate ($Y = A \\cdot B$) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-IV, D-III", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. NAND with inputs tied: $Y = \\overline{A \\cdot A} = \\overline{A} \\to$ NOT gate (I).\n2. NOR with inputs tied: $Y = \\overline{A + A} = \\overline{A} \\to$ NOT gate (II).\n3. Inverted inputs into NAND: $Y = \\overline{\\overline{A} \\cdot \\overline{B}} = A + B \\to$ OR gate (III).\n4. Inverted inputs into NOR: $Y = \\overline{\\overline{A} + \\overline{B}} = A \\cdot B \\to$ AND gate (IV).",
         "Distractors swap De Morgan conversions of NAND and NOR.",
         "NAND and NOR gates are universal: tying inputs creates NOT; inverting inputs produces complementary OR/AND gates."),

        # 47. Solids - Elongation under Own Weight
        ("Mechanical Properties of Solids and Elasticity", "Young's Modulus and Elongation under Own Weight", "Direct MCQ",
         "A uniform heavy rod of mass $M$, length $L$, and cross-sectional area $A$ is suspended vertically from a rigid support. If Young's modulus of the material is $Y$, the elongation of the rod under its own weight is:",
         ["Mg L / (2 A Y)", "Mg L / (A Y)", "Mg L / (4 A Y)", "2 Mg L / (A Y)"], 0,
         "1. Tension varies linearly along the rod: at distance $x$ from bottom, tension is due only to mass below it: $T(x) = \\frac{M}{L} g x$.\n2. Elongation of elemental length $dx$: $d\\Delta L = \\frac{T(x) dx}{A Y} = \\frac{M g x dx}{L A Y}$.\n3. Integrating from $x=0$ to $x=L$:\n   $$\\Delta L = \\frac{Mg}{LAY} \\int_0^L x dx = \\frac{Mg}{LAY} \\left[\\frac{L^2}{2}\\right] = \\frac{MgL}{2AY}$$.\n4. This equals the elongation produced if a load of half its weight ($Mg/2$) were hung from the bottom.",
         "MgL / (AY) assumes the entire weight acts at the bottom.",
         "Elongation of a vertical hanging rod under its own weight is $\\Delta L = \\frac{MgL}{2AY}$."),

        # 48. Collisions - Inelastic Collision Energy Loss
        ("Work, Energy and Power", "Conservation of Momentum in Inelastic Collision", "Direct MCQ",
         "A bullet of mass $m = 20\\text{ g}$ travelling horizontally with velocity $v = 300\\text{ m/s}$ strikes a stationary wooden block of mass $M = 980\\text{ g}$ resting on a smooth surface and gets embedded in it. The kinetic energy lost in this collision is:",
         ["882 J (98%)", "900 J", "18 J", "450 J"], 0,
         "1. Initial kinetic energy: $E_{k1} = \\frac{1}{2} m v^2 = \\frac{1}{2} (0.02) (300)^2 = 0.01 \\times 90000 = 900\\text{ J}$.\n2. Conserving momentum for completely inelastic collision: $v_{\\text{final}} = \\frac{m v}{m + M} = \\frac{0.02 \\times 300}{0.02 + 0.98} = \\frac{6}{1.0} = 6\\text{ m/s}$.\n3. Final kinetic energy: $E_{k2} = \\frac{1}{2}(m+M) v_{\\text{final}}^2 = \\frac{1}{2}(1.0)(6)^2 = 18\\text{ J}$.\n4. Loss in kinetic energy: $\\Delta E_k = 900 - 18 = 882\\text{ J}$ (which is $98\\%$ lost as heat/sound).",
         "18 J is remaining energy; 900 J assumes total loss.",
         "In completely inelastic collision, loss of KE $= \\frac{1}{2}\\frac{m M}{m + M} v^2$."),

        # 49. Centre of Mass - Cut-out Disc
        ("System of Particles and Rotational Motion", "Centre of Mass of Symmetrical Cut Object", "Direct MCQ",
         "From a uniform circular disc of radius $R$, a circular hole of radius $R/2$ is cut out touching the circumference. The distance of the centre of mass of the remaining portion from the centre of the original disc is:",
         ["R / 6", "R / 4", "R / 8", "R / 3"], 0,
         "1. Let original disc have surface mass density $\\sigma$. Total mass $M = \\sigma \\pi R^2$.\n2. Cut-out disc radius is $R/2$, area is $\\pi (R/2)^2 = \\frac{\\pi R^2}{4}$, so mass is $m = M/4$.\n3. Centre of cut-out hole is at $x_1 = R/2$.\n4. Using negative mass method:\n   $$x_{\\text{cm}} = \\frac{M(0) - m(R/2)}{M - m} = \\frac{-(M/4)(R/2)}{M - M/4} = \\frac{-M R / 8}{3M / 4} = -\\frac{R}{6}$$.\n5. The centre of mass shifts by $R/6$ in the opposite direction.",
         "R/4 assumes mass is half; R/8 divides without remaining mass normalization.",
         "Shift in centre of mass using negative mass: $x_{\\text{cm}} = \\frac{-m x_1}{M - m} = R/6$."),

        # 50. Gravitation - Kepler's Law Orbit Period
        ("Gravitation and Planetary Motion", "Kepler's Third Law and Orbital Period", "Direct MCQ",
         "A geostationary satellite orbits the Earth at a height of approximately $6 R$ above the Earth's surface ($R$ = radius of Earth), having an orbital period of $24\\text{ hours}$. Another satellite orbits at a height of $2.5 R$ from the Earth's surface. The time period of this second satellite is:",
         ["6√2 hours (~8.48 h)", "12 hours", "6 hours", "4 hours"], 0,
         "1. Orbital radius: $r_1 = R + 6R = 7R$. Period $T_1 = 24\\text{ h}$.\n2. Second satellite orbital radius: $r_2 = R + 2.5R = 3.5R = r_1 / 2$.\n3. According to Kepler's Third Law: $T^2 \\propto r^3 \\implies \\frac{T_2}{T_1} = \\left(\\frac{r_2}{r_1}\\right)^{3/2} = \\left(\\frac{1}{2}\\right)^{3/2} = \\frac{1}{2\\sqrt{2}}$.\n4. $T_2 = \\frac{24}{2\\sqrt{2}} = \\frac{12}{\\sqrt{2}} = 6\\sqrt{2}\\text{ hours} \\approx 8.48\\text{ hours}$.",
         "12 hours assumes linear radius dependence; 6 hours ignores square root.",
         "Kepler's Third Law: $T \\propto r^{3/2}$. Halving orbital radius reduces period by $2\\sqrt{2}$.")
    ]

    assert len(topics_data) == 50, f"Expected 50 Physics topics, got {len(topics_data)}"

    for i, item in enumerate(topics_data):
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
