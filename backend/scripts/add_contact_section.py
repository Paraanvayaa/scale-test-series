import re
import os

files = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

contact_section_html = """
    <!-- ==================== CONTACT & STUDENT SUPPORT SECTION ==================== -->
    <section class="landing-section" id="contact" style="background: #f8fafc; border-top: 1px solid #e2e8f0; padding: 4.5rem 1.5rem;">
      <div class="section-header">
        <span class="section-badge" style="background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0;">Direct Support &amp; Inquiries</span>
        <h2 class="section-title">We're Here to Help Your NEET Prep</h2>
        <p class="section-desc">Have questions about the test series, payment verification, account access, or institutional licensing? Reach out directly to our dedicated support desk.</p>
      </div>

      <div class="contact-container" style="max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1.2fr; gap: 2.5rem; align-items: start;">
        <!-- Left: Official Support Channels & Response SLA -->
        <div style="display: flex; flex-direction: column; gap: 1.25rem;">
          <!-- Primary Support Card -->
          <div style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 1.75rem; box-shadow: 0 4px 15px rgba(5, 150, 105, 0.06);">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.85rem;">
              <div style="width: 42px; height: 42px; border-radius: 10px; background: #ecfdf5; display: flex; align-items: center; justify-content: center; color: #059669; flex-shrink: 0;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              </div>
              <div>
                <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #059669;">Primary Support Email</span>
                <h3 style="font-size: 1.05rem; font-weight: 800; color: #0f172a; margin: 0;">Official Support Desk</h3>
              </div>
            </div>
            <p style="font-size: 0.88rem; color: #475569; line-height: 1.5; margin-bottom: 1rem;">
              For student assistance, payment verification, account activation, or examination content queries:
            </p>
            <div style="background: #f1f5f9; padding: 0.75rem 1rem; border-radius: 8px; border: 1px solid #cbd5e1; display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 1rem; word-break: break-all;">
              <a href="mailto:connect.paraasetuu@gmail.com" style="color: #047857; font-weight: 700; font-size: 0.95rem; text-decoration: none;">connect.paraasetuu@gmail.com</a>
              <button type="button" onclick="copyContactEmail('connect.paraasetuu@gmail.com')" class="btn-sm" style="padding: 0.3rem 0.6rem; font-size: 0.72rem; background: #ffffff; border: 1px solid #94a3b8; border-radius: 6px; cursor: pointer; white-space: nowrap;">Copy Email</button>
            </div>
            <a href="mailto:connect.paraasetuu@gmail.com?subject=Scale%20Test%20Series%20Student%20Support" class="btn-primary" style="display: inline-flex; width: 100%; justify-content: center; padding: 0.65rem; font-size: 0.88rem; font-weight: 700; border-radius: 8px; text-decoration: none; box-sizing: border-box;">
              Send Support Email &rarr;
            </a>
          </div>

          <!-- Response SLA Card -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.75rem;">
              <div style="width: 36px; height: 36px; border-radius: 8px; background: #eff6ff; display: flex; align-items: center; justify-content: center; color: #2563eb; flex-shrink: 0;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              </div>
              <div>
                <h4 style="font-size: 0.92rem; font-weight: 700; color: #0f172a; margin: 0;">Support Operating Hours</h4>
                <div style="font-size: 0.75rem; color: #059669; font-weight: 600;">⚡ Rapid Response Guarantee</div>
              </div>
            </div>
            <ul style="font-size: 0.82rem; color: #475569; line-height: 1.6; margin: 0; padding-left: 1.1rem;">
              <li><strong>Monday to Saturday:</strong> 9:00 AM &ndash; 8:00 PM IST</li>
              <li><strong>Sunday &amp; Exam Days:</strong> 10:00 AM &ndash; 4:00 PM IST</li>
              <li><strong>Average Resolution Time:</strong> Within 2 to 4 business hours</li>
            </ul>
          </div>

          <!-- Institutional Inquiry Card -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.65rem;">
              <div style="width: 36px; height: 36px; border-radius: 8px; background: #fdf4ff; display: flex; align-items: center; justify-content: center; color: #a855f7; flex-shrink: 0;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 21h18"></path><path d="M5 21V7l8-4v18"></path><path d="M19 21V11l-6-3"></path><line x1="9" y1="9" x2="9" y2="9.01"></line><line x1="9" y1="13" x2="9" y2="13.01"></line><line x1="9" y1="17" x2="9" y2="17.01"></line></svg>
              </div>
              <h4 style="font-size: 0.92rem; font-weight: 700; color: #0f172a; margin: 0;">Institutional &amp; Batch Pass Inquiries</h4>
            </div>
            <p style="font-size: 0.80rem; color: #64748b; line-height: 1.5; margin: 0;">
              Coaching centers, academies, and tuition batches can contact us directly at <strong style="color: #0f172a;">connect.paraasetuu@gmail.com</strong> with subject <em>"Institutional Licensing Inquiry"</em> for bulk pass pricing.
            </p>
          </div>
        </div>

        <!-- Right: Interactive Quick Query Form -->
        <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 16px; padding: 2.25rem 2rem; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
          <div style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.25rem; font-weight: 800; color: #0f172a; margin-bottom: 0.35rem;">Send a Quick Support Inquiry</h3>
            <p style="font-size: 0.82rem; color: #64748b; margin: 0;">Fill in your details below and we will route your inquiry directly to our academic or billing support team.</p>
          </div>

          <form id="contactSupportForm" onsubmit="handleContactSubmit(event)">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.1rem;">
              <div>
                <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #334155; margin-bottom: 0.35rem;">Your Name *</label>
                <input type="text" id="contactName" required placeholder="e.g. Sanket Gupta" style="width: 100%; box-sizing: border-box; padding: 0.65rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.88rem; outline: none;">
              </div>
              <div>
                <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #334155; margin-bottom: 0.35rem;">Your Email *</label>
                <input type="email" id="contactEmail" required placeholder="name@example.com" style="width: 100%; box-sizing: border-box; padding: 0.65rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.88rem; outline: none;">
              </div>
            </div>

            <div style="margin-bottom: 1.1rem;">
              <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #334155; margin-bottom: 0.35rem;">Inquiry Topic *</label>
              <select id="contactTopic" required style="width: 100%; box-sizing: border-box; padding: 0.65rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.88rem; background: #ffffff; outline: none;">
                <option value="General &amp; Mock Papers">General Inquiry / NEET Mock Test Series</option>
                <option value="Payment &amp; Billing">Payment Verification / Razorpay Transaction Help</option>
                <option value="Account &amp; Device Access">Account Access &amp; Device Session Support</option>
                <option value="Institutional Licensing">Coaching Center / Institutional Pass Inquiry</option>
                <option value="Technical Issue">Technical Bug / Workspace Display Problem</option>
              </select>
            </div>

            <div style="margin-bottom: 1.35rem;">
              <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #334155; margin-bottom: 0.35rem;">Describe Your Query or Issue *</label>
              <textarea id="contactMessage" required rows="4" placeholder="Please provide details so we can resolve your query as quickly as possible..." style="width: 100%; box-sizing: border-box; padding: 0.65rem 0.85rem; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.88rem; resize: vertical; outline: none; font-family: inherit;"></textarea>
            </div>

            <button type="submit" id="contactSubmitBtn" class="btn-primary" style="width: 100%; justify-content: center; padding: 0.75rem; font-size: 0.92rem; font-weight: 700; border-radius: 8px; display: inline-flex; align-items: center; gap: 6px;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
              Submit Support Inquiry &rarr;
            </button>
          </form>

          <div id="contactSuccessMsg" style="display: none; margin-top: 1.25rem; padding: 1.25rem; background: #ecfdf5; border: 1.5px solid #a7f3d0; border-radius: 10px; text-align: center;">
            <div style="font-size: 1.5rem; margin-bottom: 0.4rem;">✅</div>
            <h4 style="color: #064e3b; font-size: 1rem; font-weight: 800; margin-bottom: 0.25rem;">Inquiry Prepared!</h4>
            <p style="color: #047857; font-size: 0.82rem; margin: 0 0 0.75rem 0; line-height: 1.4;">
              Thank you! Your inquiry has been routed to <strong>connect.paraasetuu@gmail.com</strong>.
            </p>
            <a id="contactMailtoLink" href="#" class="btn-sm" style="display: inline-block; padding: 0.4rem 0.85rem; background: #059669; color: #ffffff; text-decoration: none; border-radius: 6px; font-weight: 700; font-size: 0.78rem;">
              Open in Email Client &rarr;
            </a>
          </div>
        </div>
      </div>
    </section>
"""

contact_js = """
    function copyContactEmail(email) {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(email).then(() => {
          showToast('Support email copied: ' + email, 'success');
        }).catch(() => {
          showToast('Support Email: ' + email, 'info');
        });
      } else {
        showToast('Support Email: ' + email, 'info');
      }
    }

    function handleContactSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('contactName').value.trim();
      const email = document.getElementById('contactEmail').value.trim();
      const topic = document.getElementById('contactTopic').value;
      const message = document.getElementById('contactMessage').value.trim();
      const submitBtn = document.getElementById('contactSubmitBtn');
      const successBox = document.getElementById('contactSuccessMsg');
      const mailtoLink = document.getElementById('contactMailtoLink');

      const subject = encodeURIComponent(`Scale Test Series [${topic}] - from ${name}`);
      const body = encodeURIComponent(`Student Name: ${name}\\nStudent Email: ${email}\\nInquiry Topic: ${topic}\\n\\nMessage:\\n${message}\\n\\n---\\nScale Test Series Support Desk`);
      const mailtoUrl = `mailto:connect.paraasetuu@gmail.com?subject=${subject}&body=${body}`;

      if (mailtoLink) mailtoLink.href = mailtoUrl;
      if (successBox) successBox.style.display = 'block';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerText = 'Inquiry Prepared ✓';
        submitBtn.style.background = '#047857';
      }
      showToast('Support message prepared! Emailing connect.paraasetuu@gmail.com', 'success');
      setTimeout(() => {
        window.location.href = mailtoUrl;
      }, 400);
    }
"""

contact_legal_snippet = """      contact: `
        <h4>Scale Test Series Official Support</h4>
        <p>Our dedicated support team is available to assist you with any questions regarding test papers, payment verification, account access, or technical support.</p>
        <br>
        <div style="background: #ecfdf5; border: 1.5px solid #a7f3d0; border-radius: 10px; padding: 1.25rem; margin-bottom: 1rem;">
          <div style="font-size: 0.75rem; font-weight: 700; color: #047857; text-transform: uppercase; margin-bottom: 0.25rem;">Official Support Email</div>
          <a href="mailto:connect.paraasetuu@gmail.com" style="font-size: 1.05rem; font-weight: 800; color: #064e3b; text-decoration: none;">connect.paraasetuu@gmail.com</a>
          <p style="font-size: 0.80rem; color: #475569; margin: 0.5rem 0 0 0;">Response time: Within 2 to 4 business hours.</p>
        </div>
        <h4>Support Operating Hours</h4>
        <p>Monday to Saturday: 9:00 AM – 8:00 PM IST<br>Sunday & Exam Days: 10:00 AM – 4:00 PM IST</p>
        <br>
        <a href="mailto:connect.paraasetuu@gmail.com?subject=Scale%20Test%20Series%20Support" class="btn-primary" style="display: inline-flex; width: 100%; justify-content: center; padding: 0.65rem; border-radius: 8px; text-decoration: none; font-size: 0.88rem; font-weight: 700;">Open Email Client &rarr;</a>
      `,
"""

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add "Contact" to Navbar
    if '<li><a onclick="scrollToSection(\'pricing\'); return false;">Pricing</a></li>' in html and 'scrollToSection(\'contact\')' not in html:
        html = html.replace(
            '<li><a onclick="scrollToSection(\'pricing\'); return false;">Pricing</a></li>',
            '<li><a onclick="scrollToSection(\'pricing\'); return false;">Pricing</a></li>\n        <li><a onclick="scrollToSection(\'contact\'); return false;">Contact</a></li>'
        )

    # 2. Insert Contact Section before Footer
    if '<footer class="site-footer">' in html and 'id="contact"' not in html:
        html = html.replace('<footer class="site-footer">', contact_section_html + '\n    <footer class="site-footer">')

    # 3. Replace old alert in footer
    html = re.sub(
        r'<li><a onclick="alert\(\'Support:[^\']+\'\)">Support &amp; Contact</a></li>',
        '<li><a onclick="scrollToSection(\'contact\'); return false;">Support &amp; Contact</a></li>',
        html
    )
    html = re.sub(
        r'<li><a onclick="alert\(\'Support:[^\']+\'\)">Support & Contact</a></li>',
        '<li><a onclick="scrollToSection(\'contact\'); return false;">Support & Contact</a></li>',
        html
    )

    # 4. Replace institutional alert
    html = re.sub(
        r'onclick="alert\(\'Contact scaleshunyaa at support@[^\']+\'\)"',
        'onclick="scrollToSection(\'contact\')"',
        html
    )

    # 5. Replace any remaining old emails
    html = html.replace('support@scaleseries.com', 'connect.paraasetuu@gmail.com')
    html = html.replace('contact@scaleshunyaa.com', 'connect.paraasetuu@gmail.com')
    html = html.replace('support@scaleshunyaa.com', 'connect.paraasetuu@gmail.com')

    # 6. Add contact legal texts and title
    if 'refund: `' in html and 'contact: `' not in html:
        html = html.replace('refund: `', contact_legal_snippet + '      refund: `')
    if "refund: 'Refund & Cancellation Policy'" in html and "contact: 'Official Support & Contact Desk'" not in html:
        html = html.replace(
            "refund: 'Refund & Cancellation Policy'",
            "refund: 'Refund & Cancellation Policy',\n        contact: 'Official Support & Contact Desk'"
        )

    # 7. Add helper functions
    if 'function copyContactEmail' not in html:
        html = html.replace(
            'function openLegalModal(type) {',
            contact_js + '\n    function openLegalModal(type) {'
        )

    # 8. Add mobile media query for contact form
    mobile_contact_css = """      .contact-container {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
      }
      #contactSupportForm div[style*="grid-template-columns"] {
        grid-template-columns: 1fr !important;
        gap: 0.85rem !important;
      }
"""
    if '.contact-container {' not in html and '@media (max-width: 768px) {' in html:
        html = html.replace(
            '@media (max-width: 768px) {\n',
            '@media (max-width: 768px) {\n' + mobile_contact_css
        )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Updated {fpath}")

# Verify Golden Rule
with open(files[0], 'r', encoding='utf-8') as f: c1 = f.read()
with open(files[1], 'r', encoding='utf-8') as f: c2 = f.read()
with open(files[2], 'r', encoding='utf-8') as f: c3 = f.read()

if c1 == c2 and c2 == c3:
    print("PASS: All 3 index.html files remain 100% byte-for-byte identical!")
else:
    print("FAIL: HTML files mismatch!")
    exit(1)
