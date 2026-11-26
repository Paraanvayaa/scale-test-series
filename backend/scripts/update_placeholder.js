const fs = require('fs');
const path = require('path');

const files = [
  path.resolve(__dirname, '../../mock_tests/index.html'),
  path.resolve(__dirname, '../../mock_tests/neet/index.html'),
  path.resolve(__dirname, '../../neet_mock_tests/index.html')
];

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  content = content.replace('placeholder="e.g. Sanket Sharma"', 'placeholder="e.g. Sanket Gupta"');
  fs.writeFileSync(f, content, 'utf8');
  console.log('Updated placeholder in', path.relative(path.resolve(__dirname, '../../'), f));
});

// Verify Golden Rule
const c1 = fs.readFileSync(files[0], 'utf8');
const c2 = fs.readFileSync(files[1], 'utf8');
const c3 = fs.readFileSync(files[2], 'utf8');

if (c1 === c2 && c2 === c3) {
  console.log('PASS: All 3 index.html files remain 100% synchronized!');
} else {
  console.error('FAIL: Files are out of sync!');
  process.exit(1);
}
