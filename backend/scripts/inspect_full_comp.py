import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos_start = text.find('class="comparison-section"')
pos_end = text.find('class="pricing-section"', pos_start)

print(text[pos_start-50:pos_end])
