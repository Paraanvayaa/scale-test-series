# -*- coding: utf-8 -*-
"""
Bundles all 60 NEET mock markdown documents into neet_data.js for 100% offline,
CORS-free local and web execution.
"""
import os
import glob
import json
import shutil

base_dirs = ['neet_mock_tests', 'mock_tests/neet']

for base in base_dirs:
    if not os.path.exists(base):
        continue
    
    data = {}
    mock_folders = sorted(glob.glob(os.path.join(base, 'Mock_*')))
    print(f"Bundling {len(mock_folders)} mocks for {base}...")
    
    for mf in mock_folders:
        pad = os.path.basename(mf)
        for fname in ['Question_Paper.md', 'Detailed_Solutions.md', 'Answer_Key_and_Analysis.md']:
            fpath = os.path.join(mf, fname)
            if os.path.exists(fpath):
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
                key = f"{pad}_{fname}"
                data[key] = content
                
    out_path = os.path.join(base, 'neet_data.js')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("window.NEET_DATA = " + json.dumps(data) + ";\n")
        
    print(f"Created {out_path} ({round(os.path.getsize(out_path)/(1024*1024), 2)} MB)")

# Also mirror to mock_tests/neet_data.js
if os.path.exists('mock_tests/neet/neet_data.js'):
    shutil.copyfile('mock_tests/neet/neet_data.js', 'mock_tests/neet_data.js')
    print("Copied to mock_tests/neet_data.js")
