const { Client } = require('pg');
const fs = require('fs');
const path = require('path');

const connectionString = 'postgresql://postgres.xkemqdthtkkfxaltigii:Csesanketiiitp%231@aws-0-ap-northeast-1.pooler.supabase.com:6543/postgres';

async function main() {
  const client = new Client({
    connectionString,
    ssl: { rejectUnauthorized: false }
  });

  console.log('Connecting to Supabase PostgreSQL Database for Admin Schema Migration...');
  await client.connect();

  const sqlPath = path.join(__dirname, '../migrations/003_admin_schema.sql');
  const sql = fs.readFileSync(sqlPath, 'utf-8');

  console.log('Executing Admin Tables and Functions Migration...');
  await client.query(sql);
  console.log('Admin Schema Migration Successful!');

  // Verify created tables and columns
  const res = await client.query(`
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public' AND table_name LIKE 'scale_%'
    ORDER BY table_name;
  `);

  console.log('Verified Scale Tables in Database:');
  res.rows.forEach(r => console.log(' ->', r.table_name));

  await client.end();
}

main().catch(err => {
  console.error('Migration failed:', err);
  process.exit(1);
});

