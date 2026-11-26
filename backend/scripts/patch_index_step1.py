import re

with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update data store script tag from neet_data.js to demo_mocks.js
content = re.sub(
    r'<script src="neet_data\.js"></script>',
    r'<!-- Pre-bundled offline diagnostic demo store (Mocks 01, 21, 41 only) -->\n  <script src="demo_mocks.js"></script>',
    content
)

# 2. Remove "Lifetime" from pricing and guarantee text
content = content.replace(
    'Pay once and get lifetime access through NEET 2026/2027.',
    'Pay once and get full access through NEET 2026/2027.'
)
content = content.replace(
    'Includes GST &bull; 100% Secure Checkout &bull; Lifetime Access',
    'Includes GST &bull; 100% Secure Checkout &bull; Full Access'
)

# 3. Update CSS for compact mobile navbar and smaller hero buttons
# Replace .btn-cta-lg styling
old_cta_css = """.btn-cta-lg {
      padding: 0.52rem 1.15rem;
      font-size: 0.88rem;
      font-weight: 600;
    }"""

new_cta_css = """.btn-cta-lg {
      padding: 0.42rem 0.95rem;
      font-size: 0.82rem;
      font-weight: 600;
      border-radius: 7px;
    }"""

if old_cta_css in content:
    content = content.replace(old_cta_css, new_cta_css)
else:
    print("Warning: old_cta_css not matched directly")

# Update 768px media query for navbar and hero
old_media_query = """    @media (max-width: 768px) {
      /* Mobile Navigation Header */
      .site-nav {
        border-bottom: 1px solid #e2e8f0 !important;
      }
      .nav-container {
        padding: 0.25rem 0.50rem !important;
        min-height: 40px !important;
        gap: 6px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
      }
      .brand-link {
        gap: 6px !important;
        min-width: 0 !important;
        flex-shrink: 1 !important;
      }
      .brand-logo-img {
        width: 26px !important;
        height: 26px !important;
        border-radius: 6px !important;
        flex-shrink: 0 !important;
      }
      .brand-text {
        min-width: 0 !important;
      }
      .brand-name {
        font-size: 0.88rem !important;
        font-weight: 700 !important;
        white-space: nowrap !important;
        line-height: 1.15 !important;
      }
      .brand-by {
        display: none !important;
      }
      .nav-menu {
        display: none !important;
      }
      .nav-actions {
        gap: 5px !important;
        display: flex !important;
        align-items: center !important;
        flex-shrink: 0 !important;
      }
      .nav-actions .btn-secondary {
        display: none !important;
      }
      #navUnlockBtn {
        padding: 0.25rem 0.45rem !important;
        font-size: 0.70rem !important;
        white-space: nowrap !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        flex-shrink: 0 !important;
      }
      #authBtn {
        padding: 0.25rem 0.45rem !important;
        font-size: 0.72rem !important;
        border-radius: 6px !important;
      }
      .profile-pill-btn {
        padding: 0.20rem 0.40rem !important;
        gap: 4px !important;
        border-radius: 999px !important;
      }
      .profile-avatar {
        width: 20px !important;
        height: 20px !important;
        font-size: 0.62rem !important;
      }
      .profile-name {
        font-size: 0.72rem !important;
        max-width: 75px !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }
      .profile-device-sub {
        display: none !important;
      }
      .profile-caret {
        width: 9px !important;
        height: 9px !important;
      }

      /* Mobile Landing Hero */
      .hero-section {
        padding: 2.25rem 1rem 1.75rem 1rem !important;
      }
      .hero-title {
        font-size: 1.85rem !important;
        line-height: 1.25 !important;
        margin-bottom: 0.85rem !important;
      }
      .hero-subtitle {
        font-size: 0.95rem !important;
        line-height: 1.55 !important;
        margin-bottom: 1.5rem !important;
      }
      .hero-ctas {
        flex-direction: column !important;
        width: 100% !important;
        max-width: 290px !important;
        margin: 0 auto !important;
        gap: 0.45rem !important;
      }
      .hero-ctas button {
        width: 100% !important;
        justify-content: center !important;
        padding: 0.45rem 0.85rem !important;
        font-size: 0.80rem !important;
        border-radius: 7px !important;
      }
      .hero-stats-row {
        gap: 0.75rem !important;
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
      }
    }

    @media (max-width: 480px) {
      .nav-container {
        padding: 0.20rem 0.40rem !important;
        gap: 4px !important;
      }
      .brand-link {
        gap: 4px !important;
      }
      .brand-name {
        font-size: 0.82rem !important;
      }
      .brand-logo-img {
        width: 24px !important;
        height: 24px !important;
      }
      #navUnlockBtn {
        padding: 0.20rem 0.35rem !important;
        font-size: 0.67rem !important;
      }
      #authBtn {
        padding: 0.20rem 0.35rem !important;
        font-size: 0.70rem !important;
      }
      .profile-pill-btn {
        padding: 0.18rem 0.35rem !important;
        gap: 3px !important;
      }
      .profile-name {
        max-width: 60px !important;
      }
    }"""

new_media_query = """    @media (max-width: 768px) {
      /* Mobile Compact Navigation Header */
      .site-nav {
        border-bottom: 1px solid #e2e8f0 !important;
        background: #ffffff !important;
      }
      .nav-container {
        padding: 0.18rem 0.40rem !important;
        min-height: 38px !important;
        height: 38px !important;
        gap: 4px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
      }
      .brand-link {
        gap: 5px !important;
        min-width: 0 !important;
        flex-shrink: 1 !important;
        display: inline-flex !important;
        align-items: center !important;
      }
      .brand-logo-img {
        width: 22px !important;
        height: 22px !important;
        border-radius: 5px !important;
        flex-shrink: 0 !important;
      }
      .brand-text {
        min-width: 0 !important;
        display: flex !important;
        flex-direction: column !important;
      }
      .brand-name {
        font-size: 0.80rem !important;
        font-weight: 700 !important;
        white-space: nowrap !important;
        line-height: 1.1 !important;
      }
      .brand-by {
        display: none !important;
      }
      .nav-menu {
        display: none !important;
      }
      .nav-actions {
        gap: 4px !important;
        display: flex !important;
        align-items: center !important;
        flex-shrink: 0 !important;
      }
      .nav-actions .btn-secondary:not(#authBtn) {
        display: none !important;
      }
      #navUnlockBtn {
        padding: 0.20rem 0.40rem !important;
        font-size: 0.68rem !important;
        white-space: nowrap !important;
        border-radius: 5px !important;
        font-weight: 700 !important;
        line-height: 1.1 !important;
        flex-shrink: 0 !important;
        height: 26px !important;
        box-sizing: border-box !important;
      }
      #authBtn {
        padding: 0.20rem 0.40rem !important;
        font-size: 0.70rem !important;
        border-radius: 5px !important;
        line-height: 1.1 !important;
        height: 26px !important;
        box-sizing: border-box !important;
      }
      .profile-pill-btn {
        padding: 0.14rem 0.35rem !important;
        gap: 4px !important;
        border-radius: 999px !important;
        height: 26px !important;
        box-sizing: border-box !important;
      }
      .profile-avatar {
        width: 18px !important;
        height: 18px !important;
        font-size: 0.58rem !important;
      }
      .profile-name {
        font-size: 0.68rem !important;
        max-width: 68px !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }
      .profile-device-sub {
        display: none !important;
      }
      .profile-caret {
        width: 8px !important;
        height: 8px !important;
      }

      /* Mobile Landing Hero - Compact Buttons */
      .hero-section {
        padding: 1.75rem 0.85rem 1.5rem 0.85rem !important;
      }
      .hero-title {
        font-size: 1.65rem !important;
        line-height: 1.25 !important;
        margin-bottom: 0.75rem !important;
      }
      .hero-subtitle {
        font-size: 0.88rem !important;
        line-height: 1.5 !important;
        margin-bottom: 1.25rem !important;
      }
      .hero-ctas {
        flex-direction: column !important;
        width: 100% !important;
        max-width: 260px !important;
        margin: 0 auto !important;
        gap: 0.35rem !important;
      }
      .hero-ctas button, .hero-ctas .btn-cta-lg {
        width: 100% !important;
        justify-content: center !important;
        padding: 0.38rem 0.75rem !important;
        font-size: 0.78rem !important;
        border-radius: 7px !important;
        min-height: 36px !important;
        height: 36px !important;
        box-sizing: border-box !important;
        line-height: 1.2 !important;
      }
      .hero-stats-row {
        gap: 0.5rem !important;
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        margin-top: 1.25rem !important;
      }
    }

    @media (max-width: 480px) {
      .nav-container {
        padding: 0.15rem 0.30rem !important;
        min-height: 36px !important;
        height: 36px !important;
        gap: 3px !important;
      }
      .brand-link {
        gap: 4px !important;
      }
      .brand-name {
        font-size: 0.76rem !important;
      }
      .brand-logo-img {
        width: 20px !important;
        height: 20px !important;
      }
      #navUnlockBtn {
        padding: 0.18rem 0.32rem !important;
        font-size: 0.65rem !important;
        height: 24px !important;
      }
      #authBtn {
        padding: 0.18rem 0.32rem !important;
        font-size: 0.68rem !important;
        height: 24px !important;
      }
      .profile-pill-btn {
        padding: 0.12rem 0.30rem !important;
        gap: 3px !important;
        height: 24px !important;
      }
      .profile-name {
        max-width: 55px !important;
        font-size: 0.65rem !important;
      }
    }"""

if old_media_query in content:
    content = content.replace(old_media_query, new_media_query)
else:
    print("Warning: old_media_query not matched directly")

with open('mock_tests/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated mock_tests/index.html step 1 successfully.")
