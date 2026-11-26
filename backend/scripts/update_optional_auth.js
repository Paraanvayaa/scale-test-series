const fs = require('fs');
const path = require('path');

const filePath = path.resolve(__dirname, '../src/middleware/auth.js');
let code = fs.readFileSync(filePath, 'utf8').replace(/\r\n/g, '\n');

code = code.replace(
  `    const session = await db.getActiveSessionByToken(rawToken);
    if (session && session.is_valid) {
      req.user = { id: session.user_id };
      req.session = session;
    } else {
      req.user = null;
      req.session = null;
    }`,
  `    const session = await db.getActiveSessionByToken(rawToken);
    if (session) {
      req.user = { id: session.user_id, is_valid: session.is_valid, reason: session.reason };
      req.session = session;
    } else {
      req.user = null;
      req.session = null;
    }`
);

fs.writeFileSync(filePath, code, 'utf8');
console.log('Updated optionalAuth in auth.js');

