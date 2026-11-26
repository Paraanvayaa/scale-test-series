const fs = require('fs');
const path = require('path');

const filePath = path.resolve(__dirname, '../src/db/supabase.js');
let code = fs.readFileSync(filePath, 'utf8');

const oldBlock = `        if (mockId) {
          params.push(mockId);
          whereClause += \` AND l.mock_id = \${params.length}\`;
        }
        if (userId) {
          params.push(userId);
          whereClause += \` AND l.user_id = \${params.length}\`;
        }
        params.push(limit);
        const limitParam = \`\${params.length}\`;
        params.push(offset);
        const offsetParam = \`\${params.length}\`;`;

const newBlock = `        if (mockId) {
          params.push(mockId);
          whereClause += ' AND l.mock_id = $' + params.length;
        }
        if (userId) {
          params.push(userId);
          whereClause += ' AND l.user_id = $' + params.length;
        }
        params.push(limit);
        const limitParam = '$' + params.length;
        params.push(offset);
        const offsetParam = '$' + params.length;`;

if (code.includes(oldBlock)) {
  code = code.replace(oldBlock, newBlock);
  fs.writeFileSync(filePath, code, 'utf8');
  console.log('Fixed parameterized query string in getContentAccessLogs');
} else {
  console.error('Could not find oldBlock in supabase.js');
}

