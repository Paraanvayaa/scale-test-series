import re

files = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

# We will update:
# 1. CSS for .site-nav, .nav-container, .brand-link, .brand-logo-img, .brand-name, .brand-by, .nav-menu, .nav-actions
# 2. Add responsive rules for 1024px and 1200px
# 3. Streamline .nav-menu HTML to prevent overflowing and wrapping

old_css_target = """    /* Top Sticky Global Navigation */
    .site-nav {
      position: sticky;
      top: 0;
      left: 0;
      right: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid #e2e8f0;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }
    .nav-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0.75rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }
    .brand-link {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: inherit;
    }
        .brand-logo-img {
      width: 42px;
      height: 42px;
      border-radius: 10px;
      object-fit: cover;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.18);
      flex-shrink: 0;
      border: 1px solid rgba(255, 255, 255, 0.3);
    }
    .brand-logo-icon {
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #059669 0%, #0d9488 100%);
      color: white;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Outfit', sans-serif;
      font-weight: 900;
      font-size: 1.3rem;
      box-shadow: 0 4px 10px rgba(5, 150, 105, 0.3);
    }
    .brand-text {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.25rem;
      color: #0f172a;
      letter-spacing: -0.02em;
      line-height: 1.1;
    }
    .brand-by {
      font-size: 0.70rem;
      color: #059669;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .nav-menu {
      display: flex;
      align-items: center;
      gap: 1.5rem;
      list-style: none;
    }
    .nav-menu a {
      text-decoration: none;
      color: #475569;
      font-weight: 600;
      font-size: 0.90rem;
      transition: color 0.15s ease;
      cursor: pointer;
    }
    .nav-menu a:hover {
      color: #059669;
    }
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }"""

new_css_replacement = """    /* Top Sticky Global Navigation - Sleek & Compact Modern Height */
    .site-nav {
      position: sticky;
      top: 0;
      left: 0;
      right: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid #e2e8f0;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
      height: 54px;
      box-sizing: border-box;
    }
    .nav-container {
      max-width: 1180px;
      margin: 0 auto;
      padding: 0 1.25rem;
      height: 54px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      box-sizing: border-box;
    }
    .brand-link {
      display: flex;
      align-items: center;
      gap: 0.55rem;
      text-decoration: none;
      color: inherit;
      flex-shrink: 0;
      white-space: nowrap;
    }
    .brand-logo-img {
      width: 32px;
      height: 32px;
      border-radius: 7px;
      object-fit: cover;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.12);
      flex-shrink: 0;
      border: 1px solid rgba(255, 255, 255, 0.4);
    }
    .brand-logo-icon {
      width: 32px;
      height: 32px;
      background: linear-gradient(135deg, #059669 0%, #0d9488 100%);
      color: white;
      border-radius: 7px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Outfit', sans-serif;
      font-weight: 900;
      font-size: 1.1rem;
      box-shadow: 0 2px 6px rgba(5, 150, 105, 0.25);
    }
    .brand-text {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.05rem;
      color: #0f172a;
      letter-spacing: -0.01em;
      line-height: 1.1;
      white-space: nowrap;
    }
    .brand-by {
      font-size: 0.64rem;
      color: #059669;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 3px;
      white-space: nowrap;
      line-height: 1;
      margin-top: 1px;
    }
    .nav-menu {
      display: flex;
      align-items: center;
      gap: 1.35rem;
      list-style: none;
      margin: 0;
      padding: 0;
      white-space: nowrap;
      flex-shrink: 0;
    }
    .nav-menu li {
      white-space: nowrap;
    }
    .nav-menu a {
      text-decoration: none;
      color: #475569;
      font-weight: 600;
      font-size: 0.84rem;
      transition: color 0.15s ease;
      cursor: pointer;
      white-space: nowrap !important;
      display: inline-block;
      line-height: 1.2;
    }
    .nav-menu a:hover {
      color: #059669;
    }
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-shrink: 0;
      white-space: nowrap;
    }
    .nav-actions .btn-secondary,
    .nav-actions .btn-primary {
      height: 34px;
      box-sizing: border-box;
      padding: 0.35rem 0.80rem;
      font-size: 0.80rem;
      border-radius: 7px;
      white-space: nowrap;
    }
    #navUnlockBtn {
      height: 34px;
      box-sizing: border-box;
      padding: 0.35rem 0.85rem;
      font-size: 0.82rem;
      border-radius: 7px;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
    }
    @media (max-width: 1160px) {
      .nav-menu {
        gap: 0.95rem;
      }
      .nav-menu a {
        font-size: 0.80rem;
      }
      .nav-legal-link {
        display: none !important;
      }
      .nav-demo-btn {
        display: none !important;
      }
    }
    @media (max-width: 960px) {
      .brand-by {
        display: none !important;
      }
      .nav-menu {
        gap: 0.75rem;
      }
      .nav-menu a {
        font-size: 0.78rem;
      }
    }"""

old_nav_html = """      <ul class="nav-menu">
        <li><a onclick="scrollToSection('tiers'); return false;">3 Tiers</a></li>
        <li><a onclick="scrollToSection('demos'); return false;">Free Demos</a></li>
        <li><a onclick="scrollToSection('pricing'); return false;">Pricing</a></li>
        <li><a onclick="scrollToSection('contact'); return false;">Contact</a></li>
        <li><a onclick="openLegalModal('terms'); return false;">Terms</a></li>
        <li><a onclick="openLegalModal('refund'); return false;">Refund Policy</a></li>
      </ul>

      <div class="nav-actions">
        <button class="btn-secondary" onclick="launchDemoTest(1)">Free Demo</button>
        <button class="btn-primary" id="navUnlockBtn" onclick="handleUnlock()" style="display: inline-flex; align-items: center;">Unlock 60 Mocks &bull; ₹999</button>
        <button class="btn-secondary" id="authBtn" onclick="openAuthModal()">Sign In</button>
      </div>"""

new_nav_html = """      <ul class="nav-menu">
        <li><a onclick="scrollToSection('tiers'); return false;">3 Tiers</a></li>
        <li><a onclick="scrollToSection('demos'); return false;">Free Demos</a></li>
        <li><a onclick="scrollToSection('pricing'); return false;">Pricing</a></li>
        <li><a onclick="scrollToSection('contact'); return false;">Contact</a></li>
        <li class="nav-legal-link"><a onclick="openLegalModal('terms'); return false;">Terms</a></li>
        <li class="nav-legal-link"><a onclick="openLegalModal('refund'); return false;">Refund</a></li>
      </ul>

      <div class="nav-actions">
        <button class="btn-secondary nav-demo-btn" onclick="launchDemoTest(1)">Free Demo</button>
        <button class="btn-primary" id="navUnlockBtn" onclick="handleUnlock()">Unlock 60 Mocks &bull; ₹999</button>
        <button class="btn-secondary" id="authBtn" onclick="openAuthModal()">Sign In</button>
      </div>"""

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize line endings
    content_norm = content.replace('\r\n', '\n')
    old_css_norm = old_css_target.replace('\r\n', '\n')
    new_css_norm = new_css_replacement.replace('\r\n', '\n')
    old_nav_norm = old_nav_html.replace('\r\n', '\n')
    new_nav_norm = new_nav_html.replace('\r\n', '\n')

    if old_css_norm in content_norm:
        content_norm = content_norm.replace(old_css_norm, new_css_norm)
        print(f"Replaced CSS in {fpath}")
    else:
        print(f"WARNING: old_css_norm not found in {fpath}")

    if old_nav_norm in content_norm:
        content_norm = content_norm.replace(old_nav_norm, new_nav_norm)
        print(f"Replaced nav HTML in {fpath}")
    else:
        print(f"WARNING: old_nav_norm not found in {fpath}")

    # Restore windows CRLF
    content_final = content_norm.replace('\n', '\r\n')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content_final)

# Verify Golden Rule
with open(files[0], 'rb') as f: c1 = f.read()
with open(files[1], 'rb') as f: c2 = f.read()
with open(files[2], 'rb') as f: c3 = f.read()

if c1 == c2 == c3:
    print("SUCCESS: All 3 index.html files are 100% byte-for-byte identical!")
else:
    print("ERROR: Mismatch between index.html files!")
    exit(1)

