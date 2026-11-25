# -*- coding: utf-8 -*-
"""
Helper to add the 10 final questions to gen_physics.py to make it 50 items.
"""
with open('engine/neet_engine/gen_physics.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace range(26, 41) with range(26, 51) so that it generates 25 dynamic items, totaling 10 + 15 + 25 = 50 items!
code = code.replace('for idx in range(26, 41):', 'for idx in range(26, 51):')

# Add 6 more rich archetypes to topics in make_dynamic_physics_q
old_topics_end = '''         "Degrees of freedom $f$ determine $\\gamma = 1 + 2/f$: Monoatomic 5/3, Diatomic 7/5, Polyatomic non-linear 4/3.")
    ]'''

new_topics_end = r'''         "Degrees of freedom $f$ determine $\gamma = 1 + 2/f$: Monoatomic 5/3, Diatomic 7/5, Polyatomic non-linear 4/3."),
        
        ("Wave Optics and Interference", "Single Slit Diffraction and Angular Width", "Conceptual MCQ",
         "In a single slit diffraction experiment, light of wavelength 600 nm illuminates a slit of width $a = 0.2\\text{ mm}$. The screen is placed at a distance $D = 2\\text{ m}$. The linear width of the central diffraction maximum observed on the screen is:",
         ["12 mm", "6 mm", "24 mm", "3 mm"],
         0,
         "1. Angular width of central diffraction maximum in single slit Fraunhofer diffraction is $\\theta = \\frac{2\\lambda}{a}$.\n2. The linear width on the screen is $W = D \\theta = \\frac{2\\lambda D}{a}$.\n3. Substitute values: $W = \\frac{2 \\times (600 \\times 10^{-9}\\text{ m}) \\times 2\\text{ m}}{0.2 \\times 10^{-3}\\text{ m}} = \\frac{2400 \\times 10^{-9}}{0.2 \\times 10^{-3}} = 12 \\times 10^{-3}\\text{ m} = 12\\text{ mm}$.",
         "Option (2) 6 mm is the half-width (distance from center to first minimum $\\lambda D/a$).\nOption (3) 24 mm doubles the width.\nOption (4) 3 mm is a division error.",
         "Central diffraction maximum linear width is $W = \\frac{2\\lambda D}{a}$, exactly twice the width of secondary maxima."),

        ("Electrostatics and Electric Potential", "Torque and Potential Energy of Electric Dipole", "Statement I & II",
         "Given below are two statements:\n\n**Statement I:** An electric dipole placed in a uniform external electric field experiences a net force of zero, but experiences a non-zero torque $\\vec{\\tau} = \\vec{p} \\times \\vec{E}$ whenever $\\vec{p}$ is not parallel or antiparallel to $\\vec{E}$.\n**Statement II:** The potential energy of an electric dipole of dipole moment $\\vec{p}$ in a uniform electric field $\\vec{E}$ is minimum (most stable equilibrium) when $\\vec{p}$ is oriented parallel to $\\vec{E}$ ($\\theta = 0^\\circ$).\n\nIn the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct", "Both Statement I and Statement II are incorrect", "Statement I is correct but Statement II is incorrect", "Statement I is incorrect but Statement II is correct"],
         0,
         "1. In a uniform electric field, the two charges $+q$ and $-q$ experience equal and opposite electrostatic forces $\\vec{F}_+ = +q\\vec{E}$ and $\\vec{F}_- = -q\\vec{E}$, so $\\vec{F}_{\\text{net}} = 0$. The forces act along different lines of action, generating torque $\\vec{\\tau} = \\vec{p} \\times \\vec{E}$. Statement I is correct.\n2. Potential energy is $U = -\\vec{p} \\cdot \\vec{E} = -p E \\cos\\theta$. Minimum energy occurs at $\\cos\\theta = +1 \\implies \\theta = 0^\\circ$, where $U = -pE$ (stable equilibrium). Maximum energy occurs at $\\theta = 180^\\circ$, where $U = +pE$ (unstable equilibrium). Statement II is correct.",
         "Both statements are core NCERT electrostatics theorems.",
         "Uniform electric field on dipole: $\\vec{F}_{\\text{net}} = 0$; $\\vec{\\tau} = \\vec{p} \\times \\vec{E}$; Stable equilibrium at $\\theta = 0^\\circ$ ($U = -pE$)."),

        ("Work, Energy and Power", "Vertical Circular Motion Critical Velocity", "Conceptual MCQ",
         "A small bob of mass $m$ attached to a light inextensible string of length $L$ is whirled in a vertical circle. The minimum speed $u$ that must be imparted to the bob at the lowest point so that it safely completes a full vertical revolution without slacking of the string is:",
         ["$\\sqrt{5gL}$", "$\\sqrt{3gL}$", "$\\sqrt{2gL}$", "$\\sqrt{gL}$"],
         0,
         "1. At the highest point (top), for the string not to slack, the tension $T_{\\text{top}} \\ge 0$. At the threshold: $m g = \\frac{m v_{\\text{top}}^2}{L} \\implies v_{\\text{top}} = \\sqrt{gL}$.\n2. By conservation of mechanical energy between lowest point and highest point:\n   $\\frac{1}{2} m u^2 = \\frac{1}{2} m v_{\\text{top}}^2 + m g (2L)$.\n3. Substitute $v_{\\text{top}}^2 = gL$:\n   $\\frac{1}{2} m u^2 = \\frac{1}{2} m (gL) + 2 m g L = \\frac{5}{2} m g L \\implies u = \\sqrt{5gL}$.",
         "Option (2) $\\sqrt{3gL}$ is the speed when the string is horizontal.\nOption (4) $\\sqrt{gL}$ is the critical speed at the topmost point, not the lowest point.\nOption (3) $\\sqrt{2gL}$ is the speed to reach the horizontal position.",
         "Vertical circle critical speeds: Lowest point $v_{\\text{bottom}} = \\sqrt{5gL}$, Horizontal $v_{\\text{mid}} = \\sqrt{3gL}$, Topmost point $v_{\\text{top}} = \\sqrt{gL}$."),

        ("Current Electricity and Electrical Instruments", "Temperature Coefficient of Resistance", "Statement I & II",
         "Given below are two statements:\n\n**Statement I:** For metallic conductors, the electrical resistivity increases with temperature because the relaxation time of conduction electrons decreases due to increased lattice vibrations.\n**Statement II:** For semiconductors, the temperature coefficient of resistivity is negative because the charge carrier density increases exponentially with temperature.\n\nIn the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct", "Both Statement I and Statement II are incorrect", "Statement I is correct but Statement II is incorrect", "Statement I is incorrect but Statement II is correct"],
         0,
         "1. Resistivity is $\\rho = \\frac{m}{n e^2 \\tau}$. In metals, carrier density $n$ is almost constant; as temperature rises, ions vibrate more vigorously, reducing relaxation time $\\tau$, so resistivity increases (positive $\\alpha$). Statement I is correct.\n2. In semiconductors, covalent bonds break as temperature increases, releasing electrons and holes exponentially ($n \\propto e^{-E_g / 2k_B T}$). The dramatic increase in carrier density far outweighs the slight reduction in $\\tau$, causing resistivity to decrease (negative $\\alpha$). Statement II is correct.",
         "Both statements are authentic NCERT Class 12 Current Electricity explanations.",
         "Metals: $\\rho \\uparrow$ with $T$ because $\\tau \\downarrow$; Semiconductors: $\\rho \\downarrow$ with $T$ because carrier density $n \\uparrow$ exponentially."),

        ("Thermal Properties of Matter and Calorimetry", "Newton's Law of Cooling", "Conceptual MCQ",
         "A body cools from $80^\\circ\\text{C}$ to $60^\\circ\\text{C}$ in 5 minutes when the surrounding temperature is $20^\\circ\\text{C}$. The time taken by the body to cool from $60^\\circ\\text{C}$ to $40^\\circ\\text{C}$ in the same surroundings is:",
         ["$\\frac{25}{3}\\text{ minutes} \\approx 8.33\\text{ min}$", "$5\\text{ minutes}$", "$6.5\\text{ minutes}$", "$10\\text{ minutes}$"],
         0,
         "1. By Newton's law of cooling in approximate form: $\\frac{T_1 - T_2}{t} = K \\left(\\frac{T_1 + T_2}{2} - T_0\\right)$.\n2. First stage ($80^\\circ\\text{C} \\to 60^\\circ\\text{C}$ in 5 min, $T_0 = 20^\\circ\\text{C}$):\n   $\\frac{80 - 60}{5} = K \\left(\\frac{80 + 60}{2} - 20\\right) \\implies \\frac{20}{5} = K(70 - 20) \\implies 4 = 50 K \\implies K = \\frac{4}{50} = \\frac{2}{25}$.\n3. Second stage ($60^\\circ\\text{C} \\to 40^\\circ\\text{C}$ in time $t$):\n   $\\frac{60 - 40}{t} = K \\left(\\frac{60 + 40}{2} - 20\\right) \\implies \\frac{20}{t} = \\left(\\frac{2}{25}\\right)(50 - 20) = \\frac{2}{25} \\times 30 = \\frac{60}{25} = \\frac{12}{5}$.\n4. Solve for $t$: $t = \\frac{20 \\times 5}{12} = \\frac{100}{12} = \\frac{25}{3}\\text{ min} \\approx 8.33\\text{ min}$.",
         "Option (2) 5 minutes assumes linear cooling rate independent of temperature gradient.\nOption (4) 10 minutes is an overestimate.",
         "Newton's law: cooling rate is proportional to temperature excess over surroundings; as excess drops, cooling slows down."),

        ("Moving Charges and Magnetism", "Magnetic Field on Axis of Circular Loop", "Conceptual MCQ",
         "A circular coil of wire of radius $R$ carries a steady current $I$. The ratio of the magnetic field at the centre of the coil to that at an axial point at a distance $x = \\sqrt{3}R$ from the centre is:",
         ["$8 : 1$", "$4 : 1$", "$2\\sqrt{2} : 1$", "$16 : 1$"],
         0,
         "1. Magnetic field on the axis of circular coil: $B_{\\text{axis}} = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}$.\n2. At the centre ($x = 0$): $B_{\\text{centre}} = \\frac{\\mu_0 I}{2R}$.\n3. At $x = \\sqrt{3}R$: $R^2 + x^2 = R^2 + 3R^2 = 4R^2$. So $(R^2 + x^2)^{3/2} = (4R^2)^{3/2} = 8 R^3$.\n4. $B_{\\text{axis}} = \\frac{\\mu_0 I R^2}{2(8R^3)} = \\frac{1}{8} \\left(\\frac{\\mu_0 I}{2R}\\right) = \\frac{1}{8} B_{\\text{centre}}$.\n5. Therefore, the ratio $B_{\\text{centre}} : B_{\\text{axis}} = 8 : 1$.",
         "Option (2) 4 : 1 forgets the power $3/2$ ($4^{3/2} = 8$, not 4).\nOption (3) uses $x = R$.\nOption (4) squares 4.",
         "On the axis of circular coil: $B(x) = \\frac{B(0)}{(1 + x^2/R^2)^{3/2}}$. For $x = \\sqrt{3}R$, $(1+3)^{3/2} = 4^{3/2} = 8$. Ratio is 8:1.")
    ]'''

code = code.replace(old_topics_end, new_topics_end)

with open('engine/neet_engine/gen_physics.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Updated gen_physics.py to 50 items!')
