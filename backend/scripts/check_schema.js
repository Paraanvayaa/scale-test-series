const { Pool } = require('pg');
const pool = new Pool({
  connectionString: 'postgresql://postgres.xkemqdthtkkfxaltigii:Csesanketiiitp%231@aws-0-ap-northeast-1.pooler.supabase.com:6543/postgres',
  ssl: { rejectUnauthorized: false }
});

async function check() {
  const usersCols = await pool.query("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'scale_users' ORDER BY ordinal_position");
  console.log('scale_users columns:');
  usersCols.rows.forEach(r => console.log(`  ${r.column_name}: ${r.data_type}`));

  const allTables = await pool.query("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name");
  console.log('\nPublic tables:');
  allTables.rows.forEach(r => console.log(`  ${r.table_name}`));

  await pool.end();
}
check().catch(console.error);

