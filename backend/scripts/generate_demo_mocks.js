const fs = require('fs');
const path = require('path');

const mockDir = path.join(__dirname, '..', 'data', 'mocks');
const freeMocks = [1, 21, 41];
const demoData = {};

for (const m of freeMocks) {
  const pad = String(m).padStart(2, '0');
  const mockFolder = path.join(mockDir, `Mock_${pad}`);
  
  const qpPath = path.join(mockFolder, 'Question_Paper.md');
  const solPath = path.join(mockFolder, 'Detailed_Solutions.md');
  const keyPath = path.join(mockFolder, 'Answer_Key_and_Analysis.md');

  if (fs.existsSync(qpPath)) demoData[`Mock_${pad}_Question_Paper.md`] = fs.readFileSync(qpPath, 'utf8');
  if (fs.existsSync(solPath)) demoData[`Mock_${pad}_Detailed_Solutions.md`] = fs.readFileSync(solPath, 'utf8');
  if (fs.existsSync(keyPath)) demoData[`Mock_${pad}_Answer_Key_and_Analysis.md`] = fs.readFileSync(keyPath, 'utf8');
}

const outContent = `// Free Diagnostic Demo Mocks (01, 21, 41) only.\n// Proprietary full mock series (02-20, 22-40, 42-60) is protected by backend entitlement authorization.\nwindow.DEMO_MOCKS = ${JSON.stringify(demoData)};\n`;

const outPath1 = path.join(__dirname, '..', '..', 'mock_tests', 'demo_mocks.js');
const outPath2 = path.join(__dirname, '..', '..', 'mock_tests', 'neet', 'demo_mocks.js');
const outPath3 = path.join(__dirname, '..', '..', 'neet_mock_tests', 'demo_mocks.js');

fs.writeFileSync(outPath1, outContent, 'utf8');
fs.writeFileSync(outPath2, outContent, 'utf8');
fs.writeFileSync(outPath3, outContent, 'utf8');

console.log('Successfully generated demo_mocks.js with only Mocks 01, 21, 41.');
