with open('mock_tests/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the start of @media (max-width: 768px) around line 1574 (0-indexed: 1573)
start_idx = -1
for i, l in enumerate(lines):
    if '@media (max-width: 768px) {' in l and 'Mobile Navigation Header' in lines[i+1]:
        start_idx = i
        break

end_idx = -1
for i in range(start_idx, len(lines)):
    if '@media (max-width: 360px) {' in lines[i]:
        end_idx = i
        break

print(f"Replacing lines {start_idx+1} to {end_idx} (found start={start_idx}, end={end_idx})")

new_media = """    @media (max-width: 768px) {
      /* Mobile Compact Navigation Header */
      .site-nav {
        border-bottom: 1px solid #e2e8f0 !important;
        background: #ffffff !important;
      }
      .nav-container {
        padding: 0.15rem 0.40rem !important;
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
        padding: 0.18rem 0.38rem !important;
        font-size: 0.67rem !important;
        white-space: nowrap !important;
        border-radius: 5px !important;
        font-weight: 700 !important;
        line-height: 1.1 !important;
        flex-shrink: 0 !important;
        height: 26px !important;
        box-sizing: border-box !important;
      }
      #authBtn {
        padding: 0.18rem 0.38rem !important;
        font-size: 0.70rem !important;
        border-radius: 5px !important;
        line-height: 1.1 !important;
        height: 26px !important;
        box-sizing: border-box !important;
      }
      .profile-pill-btn {
        padding: 0.12rem 0.35rem !important;
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

      /* Mobile Landing Hero - Sleek Compact Buttons */
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
        padding: 0.12rem 0.28rem !important;
        min-height: 35px !important;
        height: 35px !important;
        gap: 3px !important;
      }
      .brand-link {
        gap: 3px !important;
      }
      .brand-name {
        font-size: 0.74rem !important;
      }
      .brand-logo-img {
        width: 19px !important;
        height: 19px !important;
      }
      #navUnlockBtn {
        padding: 0.15rem 0.30rem !important;
        font-size: 0.64rem !important;
        height: 24px !important;
      }
      #authBtn {
        padding: 0.15rem 0.30rem !important;
        font-size: 0.66rem !important;
        height: 24px !important;
      }
      .profile-pill-btn {
        padding: 0.10rem 0.28rem !important;
        gap: 3px !important;
        height: 24px !important;
      }
      .profile-name {
        max-width: 55px !important;
        font-size: 0.64rem !important;
      }
    }
\n"""

lines[start_idx:end_idx] = [new_media]

with open('mock_tests/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

with open('mock_tests/neet/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

with open('neet_mock_tests/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Successfully replaced mobile media query across all 3 files!")

