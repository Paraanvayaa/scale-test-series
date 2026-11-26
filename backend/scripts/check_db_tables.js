const { Client } = require('pg');
require('dotenv').config({ path: 'backend/.env' });
const client = new Client({ connectionString: process.env.DATABASE_URL, ssl: { rejectUnauthorized: false } });

async function run() {
  await client.connect();
  const res = await client.query("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'");
  console.log('Tables in public schema:', res.rows.map(r => r.table_name));
  await client.end();
}

run().catch(console.error);
