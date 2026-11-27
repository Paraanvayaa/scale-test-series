import re

files = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

# We will apply:
# 1. Performance optimization:
#    - HTML cache: mockRenderedHtmlCache
#    - Lazy-render solutions on mobile/test-only
#    - Prewarm demo mocks 01, 21, 41
#    - Instant switching
# 2. Mobile Responsiveness:
#    - Breakpoint up to 900px
#    - Full-width workspace, sidebar strictly an off-canvas drawer
#    - Auto-close sidebar on mock tap
#    - Headers scroll away naturally on mobile (so students see 100% full view)
#    - Horizontal scrolling for equations, tables, and options
#    - Sleek floating mobile dock for instant access to Mocks, Solutions, and Top

script_content = open('mock_tests/index.html', 'r', encoding='utf-8').read()

# Let's verify Golden Rule before we start
for f in files:
    content = open(f, 'r', encoding='utf-8').read()
    assert content == script_content, f"Pre-check failed: {f} mismatch!"

print("Pre-check PASSED: all 3 files identical!")

