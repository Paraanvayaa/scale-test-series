files = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

target = """      containerEl.innerHTML = html;

      // Trigger KaTeX
      if (window.renderMathInElement) {
        renderMathInElement(containerEl, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true }
          ],
          throwOnError: false
        });
      }
      containerEl.scrollTop = 0;
    }"""

replacement = """      containerEl.innerHTML = html;

      // Trigger KaTeX
      if (window.renderMathInElement) {
        try {
          renderMathInElement(containerEl, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false },
              { left: '\\(', right: '\\)', display: false },
              { left: '\\[', right: '\\]', display: true }
            ],
            throwOnError: false
          });
        } catch(e) {
          console.warn('KaTeX render warning:', e);
        }
      }
      containerEl.scrollTop = 0;
      if (typeof onComplete === 'function') {
        onComplete(containerEl.innerHTML);
      }
    }"""

for f in files:
    content = open(f, 'r', encoding='utf-8').read()
    c_norm = content.replace('\r\n', '\n')
    t_norm = target.replace('\r\n', '\n')
    r_norm = replacement.replace('\r\n', '\n')
    assert t_norm in c_norm, f"Target not in {f}"
    c_norm = c_norm.replace(t_norm, r_norm)
    open(f, 'w', encoding='utf-8').write(c_norm)

# Verify Golden Rule
with open(files[0], 'rb') as f: c1 = f.read()
with open(files[1], 'rb') as f: c2 = f.read()
with open(files[2], 'rb') as f: c3 = f.read()

assert c1 == c2 == c3, "Mismatch!"
print("SUCCESS: onComplete hook added and all 3 files identical!")
