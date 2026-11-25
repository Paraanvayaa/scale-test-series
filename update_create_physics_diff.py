# -*- coding: utf-8 -*-
"""
Generate engine/neet_engine/curriculum_physics_diff.py with exact 2026 proportions:
- Direct MCQ: 29
- Statement I & II: 7
- Match List: 7
- Assertion & Reason: 4
- Multi-Statement: 3
Total: 50
"""

with open('create_physics_diff.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Item 4 with Assertion & Reason
old_4 = '''        # 4. Laws of Motion - Two Block Friction
        ("Laws of Motion and Friction", "Two-Block System Maximum Accelerating Force", "Direct MCQ",
         "Block $A$ of mass $m_A = 2\\\\text{ kg}$ rests on top of block $B$ of mass $m_B = 4\\\\text{ kg}$. The coefficient of static friction between $A$ and $B$ is $\\\\mu_s = 0.4$. The surface below block $B$ is completely frictionless. If acceleration due to gravity is $g = 10\\\\text{ m/s}^2$, the maximum horizontal force $F$ applied directly on block $B$ such that block $A$ does not slip on $B$ is:",
         ["$24\\\\text{ N}$", "$16\\\\text{ N}$", "$8\\\\text{ N}$", "$36\\\\text{ N}$"], 0,'''

new_4 = '''        # 4. Laws of Motion - Two Block Friction (Assertion & Reason)
        ("Laws of Motion and Friction", "Two-Block System Maximum Accelerating Force", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\\\n\\\\n"
         "Assertion (A): Block $A$ of mass $2\\\\text{ kg}$ rests on block $B$ of mass $4\\\\text{ kg}$ on a frictionless floor ($\\\\mu_s = 0.4$ between $A$ and $B$). The maximum horizontal force applied directly on $B$ so that $A$ does not slip is $24\\\\text{ N}$.\\\\n"
         "Reason (R): The only horizontal force accelerating block $A$ is static friction, which has a maximum value of $f_{s,\\\\max} = \\\\mu_s m_A g = 8\\\\text{ N}$, limiting the common acceleration to $4\\\\text{ m/s}^2$.\\\\n\\\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,'''

# Replace Item 11 with Statement I & II
old_11 = '''        # 11. Mechanical Properties of Solids - Thermal Stress
        ("Mechanical Properties of Solids and Elasticity", "Thermal Stress and Clamped Rod Force", "Direct MCQ",
         "A steel rod of cross-sectional area $A = 2\\\\text{ cm}^2$ and length $L = 1\\\\text{ m}$ is clamped rigidly between two unyielding fixed walls at temperature $20^\\\\circ\\\\text{C}$. If the temperature is increased to $70^\\\\circ\\\\text{C}$, the compressive force developed in the rod is: (Given: Young\\'s modulus $Y = 2 \\\\times 10^{11}\\\\text{ N/m}^2$, coefficient of linear expansion $\\\\alpha = 1.2 \\\\times 10^{-5}\\\\text{ K}^{-1}$)",
         ["$2.4 \\\\times 10^4\\\\text{ N}$", "$1.2 \\\\times 10^4\\\\text{ N}$", "$4.8 \\\\times 10^4\\\\text{ N}$", "$2.4 \\\\times 10^5\\\\text{ N}$"], 0,'''

new_11 = '''        # 11. Mechanical Properties of Solids - Thermal Stress (Statement I & II)
        ("Mechanical Properties of Solids and Elasticity", "Thermal Stress and Clamped Rod Force", "Statement I & II",
         "Given below are two statements regarding thermal stress in a clamped metallic rod:\\\\n\\\\n"
         "Statement I: When a metallic rod of cross-sectional area $A$ clamped rigidly between two unyielding fixed walls is heated through temperature $\\\\Delta T$, the compressive thermal force developed on the walls is $F = Y A \\\\alpha \\\\Delta T$.\\\\n\\\\n"
         "Statement II: The compressive thermal force developed on the rigid unyielding walls is completely independent of the original length $L$ of the rod.\\\\n\\\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,'''

# Replace Item 31 with Statement I & II
old_31 = '''        # 31. EMI - RL Circuit Transient
        ("Electromagnetic Induction", "Growth of Current in RL Circuit Time Constant", "Direct MCQ",
         "An inductor of inductance $L = 2\\\\text{ H}$ and resistance $R = 10\\\\text{ }\\\\Omega$ is connected across a $12\\\\text{ V}$ battery of negligible internal resistance. The time taken for the current to reach half of its maximum steady-state value is: (Given: $\\\\ln 2 \\\\approx 0.693$)",
         ["$0.139\\\\text{ s}$", "$0.200\\\\text{ s}$", "$0.693\\\\text{ s}$", "$0.069\\\\text{ s}$"], 0,'''

new_31 = '''        # 31. EMI - RL Circuit Transient (Statement I & II)
        ("Electromagnetic Induction", "Growth of Current in RL Circuit Time Constant", "Statement I & II",
         "Given below are two statements regarding current growth in an $RL$ circuit with time constant $\\\\tau = L/R$:\\\\n\\\\n"
         "Statement I: The time taken for the current in an $RL$ series circuit connected to a DC source to reach half of its maximum steady-state saturation value is $t_{1/2} = \\\\tau \\\\ln 2 \\\\approx 0.693 \\\\tau$.\\\\n\\\\n"
         "Statement II: After one time constant ($t = \\\\tau$), the current in the circuit reaches approximately $63.2\\\\%$ of its maximum steady-state value.\\\\n\\\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,'''

# Replace Item 48 with Assertion & Reason
old_48 = '''        # 48. Fluid Dynamics - Syphon Flow Speed
        ("Mechanical Properties of Fluids", "Syphon Flow Rate and Maximum Syphon Height", "Direct MCQ",
         "A syphon tube is used to empty water from an open reservoir. The outlet of the syphon is located at depth $H = 5\\\\text{ m}$ below the water surface of the reservoir. The speed of water emerging from the outlet is: (take $g = 10\\\\text{ m/s}^2$)",
         ["$10\\\\text{ m/s}$", "$5\\\\text{ m/s}$", "$14.1\\\\text{ m/s}$", "$20\\\\text{ m/s}$"], 0,'''

new_48 = '''        # 48. Fluid Dynamics - Syphon Flow Speed (Assertion & Reason)
        ("Mechanical Properties of Fluids", "Syphon Flow Rate and Maximum Syphon Height", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\\\n\\\\n"
         "Assertion (A): The speed of liquid discharging from the outlet of a syphon tube depends strictly on the vertical distance $H$ between the reservoir liquid surface and the tube outlet, given by $v = \\\\sqrt{2gH}$.\\\\n"
         "Reason (R): Since both the reservoir surface and the syphon outlet are open to atmospheric pressure, Bernoulli\\'s equation reduces directly to Torricelli\\'s theorem.\\\\n\\\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,'''

assert old_4 in content, 'old_4 not in create_physics_diff.py'
content = content.replace(old_4, new_4)
assert old_11 in content, 'old_11 not in create_physics_diff.py'
content = content.replace(old_11, new_11)
assert old_31 in content, 'old_31 not in create_physics_diff.py'
content = content.replace(old_31, new_31)
assert old_48 in content, 'old_48 not in create_physics_diff.py'
content = content.replace(old_48, new_48)

with open('create_physics_diff.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated create_physics_diff.py successfully!")

