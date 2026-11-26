import os

admin_files = [
    'mock_tests/admin/index.html',
    'mock_tests/neet/admin/index.html',
    'neet_mock_tests/admin/index.html'
]

for file_path in admin_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove admin email placeholder on login form
    content = content.replace(
        'placeholder="admin@scaletestseries.com"',
        'placeholder="Enter administrator email"'
    )

    # 2. Update password placeholder
    content = content.replace(
        'placeholder="••••••••••••"',
        'placeholder="Enter password"'
    )

    # 3. Remove hardcoded admin email in sidebar
    content = content.replace(
        '<div style="font-size: 0.75rem; color: #94a3b8; margin-bottom: 0.5rem;" id="adminUserDisplay">admin@scaletestseries.com</div>',
        '<div style="font-size: 0.75rem; color: #94a3b8; margin-bottom: 0.5rem;" id="adminUserDisplay">Administrator</div>'
    )

    # 4. In JS, display fullName or role instead of raw email
    content = content.replace(
        "document.getElementById('adminUserDisplay').innerText = currentAdmin.email;",
        "document.getElementById('adminUserDisplay').innerText = currentAdmin.fullName || currentAdmin.role || 'Administrator';"
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {file_path}")

print("All admin files updated successfully!")

