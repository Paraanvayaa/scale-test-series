const { Client } = require('pg');
const crypto = require('crypto');

const connectionString = 'postgresql://postgres.xkemqdthtkkfxaltigii:Csesanketiiitp%231@aws-0-ap-northeast-1.pooler.supabase.com:6543/postgres';

async function main() {
  const client = new Client({
    connectionString,
    ssl: { rejectUnauthorized: false }
  });

  const adminEmail = (process.env.INITIAL_ADMIN_EMAIL || 'admin@scaletestseries.com').toLowerCase().trim();
  const adminPassword = process.env.INITIAL_ADMIN_PASSWORD || 'SuperAdmin@Scale2026!';
  const fullName = 'Platform Super Administrator';

  const passwordHash = crypto.createHash('sha256').update(adminPassword).digest('hex');

  await client.connect();
  console.log('Connected to Database for Super Admin Provisioning...');

  // Check if admin already exists
  const existing = await client.query(
    'SELECT id, email, role FROM public.scale_users WHERE lower(email) = lower($1)',
    [adminEmail]
  );

  let adminId;
  if (existing.rows.length > 0) {
    adminId = existing.rows[0].id;
    await client.query(
      `UPDATE public.scale_users 
       SET role = 'SUPER_ADMIN', 
           password_hash = $1, 
           is_suspended = false, 
           updated_at = now() 
       WHERE id = $2`,
      [passwordHash, adminId]
    );
    console.log(`[Bootstrap] Existing account ${adminEmail} upgraded to SUPER_ADMIN.`);
  } else {
    const res = await client.query(
      `INSERT INTO public.scale_users (email, password_hash, full_name, role)
       VALUES ($1, $2, $3, 'SUPER_ADMIN')
       RETURNING id`,
      [adminEmail, passwordHash, fullName]
    );
    adminId = res.rows[0].id;
    console.log(`[Bootstrap] Created new SUPER_ADMIN account: ${adminEmail}`);
  }

  // Record initial audit log
  await client.query(
    `INSERT INTO public.scale_admin_audit_logs (
       admin_id, admin_email, admin_role, action, reason, metadata
     )
     VALUES ($1, $2, 'SUPER_ADMIN', 'SUPER_ADMIN_PROVISIONED', 'Initial Platform Setup', $3)`,
    [adminId, adminEmail, JSON.stringify({ provisioned_at: new Date().toISOString() })]
  );

  console.log('====================================================');
  console.log(' Super Admin Provisioned Successfully');
  console.log(` Email:    ${adminEmail}`);
  console.log(` Password: ${adminPassword}`);
  console.log(` Role:     SUPER_ADMIN`);
  console.log('====================================================');

  await client.end();
}

main().catch(err => {
  console.error('Bootstrap failed:', err);
  process.exit(1);
});

