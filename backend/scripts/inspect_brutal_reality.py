with open('mock_tests/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('class="comparison-cards-mobile"')
pos_end = text.find('</div>\n      </div>', pos)
print(text[pos:pos+3500])
