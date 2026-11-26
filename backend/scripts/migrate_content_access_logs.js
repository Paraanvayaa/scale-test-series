const { Client } = require('pg');
require('dotenv').config({ path: 'backend/.env' });

const client = new Client({ connectionString: process.env.DATABASE_URL, ssl: { rejectUnauthorized: false } });

async function runMigration() {
  console.log('Connecting to database for content access logs migration...');
  await client.connect();

  const query = `
    CREATE TABLE IF NOT EXISTS public.scale_content_access_logs (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      user_id UUID REFERENCES public.scale_users(id) ON DELETE SET NULL,
      mock_id INTEGER NOT NULL,
      section_type VARCHAR(50) NOT NULL,
      ip_address VARCHAR(100),
      user_agent TEXT,
      access_granted BOOLEAN NOT NULL DEFAULT FALSE,
      denial_reason VARCHAR(100),
      created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );

    CREATE INDEX IF NOT EXISTS idx_content_access_user_mock ON public.scale_content_access_logs(user_id, mock_id, created_at DESC);
    CREATE INDEX IF NOT EXISTS idx_content_access_created_at ON public.scale_content_access_logs(created_at DESC);
  `;

  await client.query(query);
  console.log('Migration scale_content_access_logs applied successfully!');

  const check = await client.query("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'scale_content_access_logs'");
  console.log('Table verification count:', check.rows[0].count);

  await client.end();
}

runMigration().catch(err => {
  console.error('Migration failed:', err);
  process.exit(1);
});
