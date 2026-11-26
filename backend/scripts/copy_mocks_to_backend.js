const fs = require('fs');
const path = require('path');

const srcBase = path.resolve(__dirname, '../../neet_mock_tests');
const destBase = path.resolve(__dirname, '../data/mocks');

if (!fs.existsSync(destBase)) {
  fs.mkdirSync(destBase, { recursive: true });
}

let copiedMocks = 0;
let copiedFiles = 0;

for (let i = 1; i <= 60; i++) {
  const pad = 'Mock_' + String(i).padStart(2, '0');
  const srcDir = path.join(srcBase, pad);
  const destDir = path.join(destBase, pad);

  if (fs.existsSync(srcDir)) {
    if (!fs.existsSync(destDir)) {
      fs.mkdirSync(destDir, { recursive: true });
    }
    const files = fs.readdirSync(srcDir);
    for (const f of files) {
      if (f.endsWith('.md')) {
        const srcFile = path.join(srcDir, f);
        const destFile = path.join(destDir, f);
        fs.copyFileSync(srcFile, destFile);
        copiedFiles++;
      }
    }
    copiedMocks++;
  }
}

console.log(`Copied ${copiedMocks} mocks (${copiedFiles} files) to backend/data/mocks`);
