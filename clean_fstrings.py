import re

with open('engine/neet_engine/gen_physics.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace f" with " if the string contains no python variables like {mock_num} or {idx}
def fix_line(line):
    # If line has f" or f'
    if 'f"' in line:
        # Check if it has actual python variables
        # Look for {variable}
        vars_in_str = re.findall(r'\{([a-zA-Z0-9_]+)\}', line)
        allowed_vars = {'mock_num', 'idx', 'rng', 'A_prism', 'mu_prism', 'mass_roll', 'f_val'}
        if not any(v in allowed_vars for v in vars_in_str):
            line = line.replace('f"', '"')
    return line

lines = text.split('\n')
new_lines = [fix_line(l) for l in lines]
new_text = '\n'.join(new_lines)

with open('engine/neet_engine/gen_physics.py', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Cleaned f-strings!')
