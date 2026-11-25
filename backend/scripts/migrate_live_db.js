const { Client } = require('pg');
const fs = require('fs');
const path = require('path');

const connectionString = 'postgresql://postgres.xkemqdthtkkfxaltigii:Csesanketiiitp%231@aws-0-ap-northeast-1.pooler.supabase.com:6543/postgres';

async function main() {
  const client = new Client({
    connectionString,
    ssl: { rejectUnauthorized: false }
  });

  console.log('Connecting to Supabase PostgreSQL Database...');
  await client.connect();
  console.log('Connected.');

  const sqlPath = path.join(__dirname, '../migrations/002_scale_production_schema.sql');
  const sql = fs.readFileSync(sqlPath, 'utf-8');

  console.log('Executing Scale Test Series Schema Migration...');
  await client.query(sql);
  console.log('Migration executed successfully!');

  // Verify created tables
  const res = await client.query(`
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public' AND table_name LIKE 'scale_%'
    ORDER BY table_name;
  `);

  console.log('Verified Scale Test Series Tables in Database:');
  res.rows.forEach(r => console.log(' ->', r.table_name));

  await client.end();
}

main().catch(err => {
  console.error('Migration failed:', err);
  process.exit(1);
});

