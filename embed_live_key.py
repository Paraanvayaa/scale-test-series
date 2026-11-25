targets = [
    'mock_tests/index.html',
    'mock_tests/neet/index.html',
    'neet_mock_tests/index.html'
]

for target in targets:
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(
        'window.RAZORPAY_KEY_ID = localStorage.getItem(\'scale_razorpay_key\') || "";',
        'window.RAZORPAY_KEY_ID = localStorage.getItem(\'scale_razorpay_key\') || "rzp_live_Tln6miI6q4JfC1";'
    )

    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated live key in {target}")

