# -*- coding: utf-8 -*-
with open('engine/neet_engine/curriculum_physics_diff.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's replace the 4 items
# 1. Item 4: Two-block friction
item4_new = '''        # 4. Laws of Motion - Two Block Friction (Assertion & Reason)
        ("Laws of Motion and Friction", "Two-Block System Maximum Accelerating Force", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\n"
         "Assertion (A): Block $A$ of mass $2\\\\text{ kg}$ rests on block $B$ of mass $4\\\\text{ kg}$ on a frictionless floor ($\\\\mu_s = 0.4$ between $A$ and $B$). The maximum horizontal force applied directly on $B$ so that $A$ does not slip is $24\\\\text{ N}$.\\n"
         "Reason (R): The only horizontal force accelerating block $A$ is static friction, which has a maximum value of $f_{s,\\\\max} = \\\\mu_s m_A g = 8\\\\text{ N}$, limiting the common acceleration to $4\\\\text{ m/s}^2$.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Maximum static friction force between $A$ and $B$: $f_{s,\\\\max} = \\\\mu_s m_A g = 0.4 \\\\times 2 \\\\times 10 = 8\\\\text{ N}$.\\n2. The only force accelerating block $A$ horizontally is this friction force: $f_s = m_A a \\\\implies a_{\\\\max} = \\\\frac{f_{s,\\\\max}}{m_A} = \\\\frac{8}{2} = 4\\\\text{ m/s}^2$.\\n3. Both blocks move together as a single combined system of total mass $M = m_A + m_B = 2 + 4 = 6\\\\text{ kg}$.\\n4. Maximum applied force on $B$: $F_{\\\\max} = (m_A + m_B) a_{\\\\max} = 6 \\\\times 4 = 24\\\\text{ N}$. Both statements are true and Reason explains Assertion.",
         "8 N is the friction limit itself; 16 N considers only block B accelerating.",
         "For multi-block systems, determine the maximum acceleration the non-driven block can sustain without slipping."),'''

# 2. Item 11: Thermal stress
item11_new = '''        # 11. Mechanical Properties of Solids - Thermal Stress (Statement I & II)
        ("Mechanical Properties of Solids and Elasticity", "Thermal Stress and Clamped Rod Force", "Statement I & II",
         "Given below are two statements regarding thermal stress in a clamped metallic rod:\\n\\n"
         "Statement I: When a metallic rod of cross-sectional area $A$ clamped rigidly between two unyielding fixed walls is heated through temperature $\\\\Delta T$, the compressive thermal force developed on the walls is $F = Y A \\\\alpha \\\\Delta T$.\\n\\n"
         "Statement II: The compressive thermal force developed on the rigid unyielding walls is completely independent of the original length $L$ of the rod.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Increase in temperature: $\\\\Delta T = 70 - 20 = 50^\\\\circ\\\\text{C} = 50\\\\text{ K}$.\\n2. Free thermal expansion prevented by walls: $\\\\Delta L_{\\\\text{thermal}} = L \\\\alpha \\\\Delta T$.\\n3. Compressive strain produced: $\\\\frac{\\\\Delta L}{L} = \\\\alpha \\\\Delta T = (1.2 \\\\times 10^{-5})(50) = 6.0 \\\\times 10^{-4}$.\\n4. Compressive stress: $\\\\sigma = Y \\\\times \\\\text{strain} = (2 \\\\times 10^{11})(6.0 \\\\times 10^{-4}) = 1.2 \\\\times 10^8\\\\text{ N/m}^2$.\\n5. Compressive force on walls: $F = \\\\sigma A = (1.2 \\\\times 10^8\\\\text{ N/m}^2)(2 \\\\times 10^{-4}\\\\text{ m}^2) = 2.4 \\\\times 10^4\\\\text{ N}$. Both statements are correct.",
         "Unit conversion error in $A$: $2\\\\text{ cm}^2 = 2 \\\\times 10^{-4}\\\\text{ m}^2$, not $2 \\\\times 10^{-2}\\\\text{ m}^2$.",
         "Thermal force $F = Y A \\\\alpha \\\\Delta T$ is independent of the original length $L$ of the rod."),'''

# 3. Item 31: RL Circuit
item31_new = '''        # 31. EMI - RL Circuit Transient (Statement I & II)
        ("Electromagnetic Induction", "Growth of Current in RL Circuit Time Constant", "Statement I & II",
         "Given below are two statements regarding current growth in an $RL$ circuit with time constant $\\\\tau = L/R$:\\n\\n"
         "Statement I: The time taken for the current in an $RL$ series circuit connected to a DC source to reach half of its maximum steady-state saturation value is $t_{1/2} = \\\\tau \\\\ln 2 \\\\approx 0.693 \\\\tau$.\\n\\n"
         "Statement II: After one time constant ($t = \\\\tau$), the current in the circuit reaches approximately $63.2\\\\%$ of its maximum steady-state value.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Equation for current growth in RL circuit: $I(t) = I_0(1 - e^{-t/\\\\tau})$, where time constant $\\\\tau = \\\\frac{L}{R}$.\\n2. Here $\\\\tau = \\\\frac{2\\\\text{ H}}{10\\\\text{ }\\\\Omega} = 0.2\\\\text{ s}$.\\n3. For $I(t) = \\\\frac{I_0}{2}$:\\n   $$\\\\frac{1}{2} = 1 - e^{-t/\\\\tau} \\\\implies e^{-t/\\\\tau} = \\\\frac{1}{2} \\\\implies \\\\frac{t}{\\\\tau} = \\\\ln 2$.\\n4. $t = \\\\tau \\\\ln 2 = 0.2 \\\\times 0.693 = 0.1386\\\\text{ s} \\\\approx 0.139\\\\text{ s}$. Both statements are correct.",
         "0.200 s is the time constant $\\\\tau$ itself, at which current reaches 63.2% of $I_0$.",
         "Time to reach half maximum current in RL circuit is $t_{1/2} = \\\\tau \\\\ln 2 = \\\\frac{L}{R}\\\\ln 2$."),'''

# 4. Item 48: Syphon flow speed
item48_new = '''        # 48. Fluid Dynamics - Syphon Flow Speed (Assertion & Reason)
        ("Mechanical Properties of Fluids", "Syphon Flow Rate and Maximum Syphon Height", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\n"
         "Assertion (A): The speed of liquid discharging from the outlet of a syphon tube depends strictly on the vertical distance $H$ between the reservoir liquid surface and the tube outlet, given by $v = \\\\sqrt{2gH}$.\\n"
         "Reason (R): Since both the reservoir surface and the syphon outlet are open to atmospheric pressure, Bernoulli\\'s equation reduces directly to Torricelli\\'s theorem.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Apply Bernoulli\\'s equation between the open reservoir surface (point 1) and the exit orifice of the syphon (point 2):\\n   $$P_1 + \\\\frac{1}{2}\\\\rho v_1^2 + \\\\rho g h_1 = P_2 + \\\\frac{1}{2}\\\\rho v_2^2 + \\\\rho g h_2$.\\n2. Both point 1 and point 2 are open to the atmosphere: $P_1 = P_2 = P_{\\\\text{atm}}$.\\n3. Large reservoir assumption: $v_1 \\\\approx 0$.\\n4. Taking datum at point 2: $h_1 - h_2 = H = 5\\\\text{ m}$.\\n5. $\\\\rho g H = \\\\frac{1}{2}\\\\rho v_2^2 \\\\implies v_2 = \\\\sqrt{2gH} = \\\\sqrt{2 \\\\times 10 \\\\times 5} = \\\\sqrt{100} = 10\\\\text{ m/s}$. Both statements are true and Reason explains Assertion.",
         "The height of the tube bend above the reservoir controls maximum syphon height, not exit velocity.",
         "Exit velocity of a syphon depends strictly on vertical distance between reservoir surface and outlet: $v = \\\\sqrt{2gH}$."),'''

# Replace using split on section header comments
parts = text.split('# 4. Laws of Motion - Two Block Friction')
p2 = parts[1].split('# 5. Work, Energy & Power - Vertical Circle Slackening')
text = parts[0] + item4_new + '\n\n        # 5. Work, Energy & Power - Vertical Circle Slackening' + p2[1]

parts = text.split('# 11. Mechanical Properties of Solids - Thermal Stress')
p2 = parts[1].split('# 12. Fluid Mechanics - Efflux Range')
text = parts[0] + item11_new + '\n\n        # 12. Fluid Mechanics - Efflux Range' + p2[1]

parts = text.split('# 31. EMI - RL Circuit Transient')
p2 = parts[1].split('# 32. AC - Quality Factor & Sharpness')
text = parts[0] + item31_new + '\n\n        # 32. AC - Quality Factor & Sharpness' + p2[1]

parts = text.split('# 48. Fluid Dynamics - Syphon Flow Speed')
p2 = parts[1].split('# 49. Modern Physics - Nuclear Fusion Q-Value')
text = parts[0] + item48_new + '\n\n        # 49. Modern Physics - Nuclear Fusion Q-Value' + p2[1]

with open('engine/neet_engine/curriculum_physics_diff.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Calibrated physics diff cleanly!")

