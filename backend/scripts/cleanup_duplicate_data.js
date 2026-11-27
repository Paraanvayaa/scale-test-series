require('dotenv').config({ path: 'backend/.env' });
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

async function cleanup() {
  const client = await pool.connect();
  try {
    console.log('========================================================');
    console.log('STARTING CLEANUP OF DUPLICATE & TEST DATA');
    console.log('========================================================\n');

    await client.query('BEGIN');

    // 1. Identify test user IDs
    const testUsersRes = await client.query(`
      SELECT id, email, full_name 
      FROM scale_users 
      WHERE email LIKE 'verify_%' OR email LIKE 'student_%' OR email LIKE '%@example.com' OR email LIKE '%@scaletest.test'
    `);
    const testUserIds = testUsersRes.rows.map(r => r.id);
    console.log(`Identified ${testUserIds.length} test user account(s) to remove:`);
    testUsersRes.rows.forEach(r => console.log(`  - [${r.id.slice(0, 8)}] ${r.email} (${r.full_name})`));

    if (testUserIds.length > 0) {
      // Delete child records for test users
      const delSessions = await client.query('DELETE FROM scale_user_sessions WHERE user_id = ANY($1::uuid[])', [testUserIds]);
      console.log(`\nDeleted ${delSessions.rowCount} test sessions from scale_user_sessions.`);

      const delEntitlements = await client.query('DELETE FROM scale_user_entitlements WHERE user_id = ANY($1::uuid[])', [testUserIds]);
      console.log(`Deleted ${delEntitlements.rowCount} test entitlements from scale_user_entitlements.`);

      const delSuspensions = await client.query('DELETE FROM scale_account_suspensions WHERE user_id = ANY($1::uuid[])', [testUserIds]);
      console.log(`Deleted ${delSuspensions.rowCount} test suspensions from scale_account_suspensions.`);

      const delAccessLogs = await client.query('DELETE FROM scale_content_access_logs WHERE user_id = ANY($1::uuid[])', [testUserIds]);
      console.log(`Deleted ${delAccessLogs.rowCount} test logs from scale_content_access_logs.`);

      const delAudit = await client.query('DELETE FROM scale_admin_audit_logs WHERE target_user_id::text = ANY($1::text[])', [testUserIds.map(String)]);
      console.log(`Deleted ${delAudit.rowCount} test audit records from scale_admin_audit_logs.`);

      const delNotifs = await client.query('DELETE FROM scale_admin_notifications WHERE related_user_id = ANY($1::uuid[])', [testUserIds]);
      console.log(`Deleted ${delNotifs.rowCount} test notifications from scale_admin_notifications.`);

      const delNotes = await client.query('DELETE FROM scale_admin_notes WHERE student_id = ANY($1::uuid[])', [testUserIds]);
      console.log(`Deleted ${delNotes.rowCount} test notes from scale_admin_notes.`);

      const delProgress = await client.query('DELETE FROM scale_exam_progress WHERE user_id = ANY($1::uuid[])', [testUserIds]);
      console.log(`Deleted ${delProgress.rowCount} test progress records from scale_exam_progress.`);

      const delOrders = await client.query('DELETE FROM scale_orders WHERE user_id = ANY($1::uuid[])', [testUserIds]);
      console.log(`Deleted ${delOrders.rowCount} test orders from scale_orders.`);

      const delUsers = await client.query('DELETE FROM scale_users WHERE id = ANY($1::uuid[])', [testUserIds]);
      console.log(`Deleted ${delUsers.rowCount} test user accounts from scale_users.`);
    }

    // 2. Clean up duplicate older unpaid draft orders (keeping only the newest 1 order per user)
    const delDupOrders = await client.query(`
      DELETE FROM scale_orders 
      WHERE id IN (
        SELECT id FROM (
          SELECT id, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) as rn 
          FROM scale_orders 
          WHERE status = 'created'
        ) sub 
        WHERE sub.rn > 1
      )
    `);
    console.log(`\nDeleted ${delDupOrders.rowCount} duplicate older unpaid draft orders from scale_orders.`);

    // 3. Clear mock test notifications from test runs
    const delTestNotifs = await client.query(`
      DELETE FROM scale_admin_notifications 
      WHERE title LIKE '%Test NEET Aspirant%' OR title LIKE '%student_%'
    `);
    console.log(`Deleted ${delTestNotifs.rowCount} test alert notifications.`);

    // 4. Verify remaining active accounts
    const remainingUsers = await client.query(`
      SELECT id, email, full_name, role, is_suspended, created_at 
      FROM scale_users 
      ORDER BY created_at ASC
    `);

    console.log('\n========================================================');
    console.log(`CONFIRMED: ${remainingUsers.rows.length} REAL USERS REMAIN IN DATABASE`);
    console.log('========================================================');
    console.table(remainingUsers.rows.map(u => ({
      id: u.id.slice(0, 8),
      email: u.email,
      name: u.full_name,
      role: u.role,
      suspended: u.is_suspended
    })));

    // Commit transaction
    await client.query('COMMIT');
    console.log('\nSUCCESS: Database transaction committed cleanly with 0 errors.');

  } catch (error) {
    await client.query('ROLLBACK');
    console.error('ERROR during cleanup (Rolled back):', error);
  } finally {
    client.release();
    await pool.end();
  }
}

cleanup();
