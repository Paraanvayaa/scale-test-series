const { createClient } = require('@supabase/supabase-js');
require('dotenv').config({ path: 'backend/.env' });

const supabaseUrl = process.env.SUPABASE_URL;
const supabaseKey = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY;

async function checkStorage() {
  console.log('Connecting to Supabase Storage at:', supabaseUrl);
  if (!supabaseUrl || !supabaseKey) {
    console.log('No SUPABASE_URL or key provided.');
    return;
  }
  const supabase = createClient(supabaseUrl, supabaseKey);
  const { data: buckets, error } = await supabase.storage.listBuckets();
  if (error) {
    console.error('Storage listBuckets error:', error.message);
  } else {
    console.log('Buckets found:', buckets.map(b => ({ id: b.id, name: b.name, public: b.public })));
  }
}

checkStorage().catch(console.error);
