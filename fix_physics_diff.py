# -*- coding: utf-8 -*-
with open('engine/neet_engine/curriculum_physics_diff.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Item 4 (index 3 in topics_data)
# Change "Direct MCQ" to "Assertion & Reason"
text = text.replace(
    '("Laws of Motion and Friction", "Two-Block System Maximum Accelerating Force", "Direct MCQ",\n         "Block $A$ of mass',
    '("Laws of Motion and Friction", "Two-Block System Maximum Accelerating Force", "Assertion & Reason",\n         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\nAssertion (A): Block $A$ of mass $2\\text{ kg}$ rests on block $B$ of mass $4\\text{ kg}$ on a frictionless floor ($\\mu_s = 0.4$ between $A$ and $B$). The maximum horizontal force applied directly on $B$ so that $A$ does not slip is $24\\text{ N}$.\\nReason (R): The only horizontal force accelerating block $A$ is static friction, which has a maximum value of $f_{s,\\max} = \\mu_s m_A g = 8\\text{ N}$, limiting the common acceleration to $4\\text{ m/s}^2$.\\n\\nIn the light of the above statements, choose the correct answer from the options given below:",\n         ["Both (A) and (R) are true and (R) is the correct explanation of (A)", "Both (A) and (R) are true but (R) is not the correct explanation of (A)", "(A) is true but (R) is false", "(A) is false but (R) is true"], 0,\n         "Block $A$ of mass'
)

# Item 11 (index 10 in topics_data)
# Change "Direct MCQ" to "Statement I & II"
text = text.replace(
    '("Mechanical Properties of Solids and Elasticity", "Thermal Stress and Clamped Rod Force", "Direct MCQ",\n         "A steel rod of cross-sectional',
    '("Mechanical Properties of Solids and Elasticity", "Thermal Stress and Clamped Rod Force", "Statement I & II",\n         "Given below are two statements regarding thermal stress in a clamped metallic rod:\\n\\nStatement I: When a metallic rod of cross-sectional area $A$ clamped rigidly between two unyielding fixed walls is heated through temperature $\\Delta T$, the compressive thermal force developed on the walls is $F = Y A \\alpha \\Delta T$.\\n\\nStatement II: The compressive thermal force developed on the rigid unyielding walls is completely independent of the original length $L$ of the rod.\\n\\nIn the light of the above statements, choose the correct answer from the options given below:",\n         ["Both Statement I and Statement II are correct", "Both Statement I and Statement II are incorrect", "Statement I is correct but Statement II is incorrect", "Statement I is incorrect but Statement II is correct"], 0,\n         "A steel rod of cross-sectional'
)

# Item 31 (index 30 in topics_data)
# Change "Direct MCQ" to "Statement I & II"
text = text.replace(
    '("Electromagnetic Induction", "Growth of Current in RL Circuit Time Constant", "Direct MCQ",\n         "An inductor of inductance',
    '("Electromagnetic Induction", "Growth of Current in RL Circuit Time Constant", "Statement I & II",\n         "Given below are two statements regarding current growth in an $RL$ circuit with time constant $\\tau = L/R$:\\n\\nStatement I: The time taken for the current in an $RL$ series circuit connected to a DC source to reach half of its maximum steady-state saturation value is $t_{1/2} = \\tau \\ln 2 \\approx 0.693 \\tau$.\\n\\nStatement II: After one time constant ($t = \\tau$), the current in the circuit reaches approximately $63.2\\%$ of its maximum steady-state value.\\n\\nIn the light of the above statements, choose the correct answer from the options given below:",\n         ["Both Statement I and Statement II are correct", "Both Statement I and Statement II are incorrect", "Statement I is correct but Statement II is incorrect", "Statement I is incorrect but Statement II is correct"], 0,\n         "An inductor of inductance'
)

# Item 48 (index 47 in topics_data)
# Change "Direct MCQ" to "Assertion & Reason"
text = text.replace(
    '("Mechanical Properties of Fluids", "Syphon Flow Rate and Maximum Syphon Height", "Direct MCQ",\n         "A syphon tube is used to empty',
    '("Mechanical Properties of Fluids", "Syphon Flow Rate and Maximum Syphon Height", "Assertion & Reason",\n         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\nAssertion (A): The speed of liquid discharging from the outlet of a syphon tube depends strictly on the vertical distance $H$ between the reservoir liquid surface and the tube outlet, given by $v = \\sqrt{2gH}$.\\nReason (R): Since both the reservoir surface and the syphon outlet are open to atmospheric pressure, Bernoulli\\\'s equation reduces directly to Torricelli\\\'s theorem.\\n\\nIn the light of the above statements, choose the correct answer from the options given below:",\n         ["Both (A) and (R) are true and (R) is the correct explanation of (A)", "Both (A) and (R) are true but (R) is not the correct explanation of (A)", "(A) is true but (R) is false", "(A) is false but (R) is true"], 0,\n         "A syphon tube is used to empty'
)

with open('engine/neet_engine/curriculum_physics_diff.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated physics diff successfully!")

