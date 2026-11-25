const { Pool } = require('pg');
const pool = new Pool({
  connectionString: 'postgresql://postgres.xkemqdthtkkfxaltigii:Csesanketiiitp%231@aws-0-ap-northeast-1.pooler.supabase.com:6543/postgres',
  ssl: { rejectUnauthorized: false }
});

async function migrate() {
  console.log('Running profile fields migration...');
  await pool.query(`
    ALTER TABLE public.scale_users 
    ADD COLUMN IF NOT EXISTS target_examination VARCHAR(100) DEFAULT 'NEET 2026',
    ADD COLUMN IF NOT EXISTS account_status VARCHAR(50) DEFAULT 'ACTIVE',
    ADD COLUMN IF NOT EXISTS profile_completion_status VARCHAR(50) DEFAULT 'COMPLETE';
  `);
  console.log('Migration completed successfully.');

  const res = await pool.query("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'scale_users' ORDER BY ordinal_position");
  console.log('Updated scale_users columns:');
  res.rows.forEach(r => console.log(`  ${r.column_name}: ${r.data_type}`));

  await pool.end();
}

migrate().catch(err => {
  console.error('Migration error:', err);
  process.exit(1);
});

