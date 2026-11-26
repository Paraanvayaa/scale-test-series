with open('backend/src/db/supabase.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re

# Clean implementation of getContentAccessLogs in db object
target_regex = r'async getContentAccessLogs\(\{ limit = 50, offset = 0, mockId = null, userId = null \} = \{\}\) \{[\s\S]*?return localStore\.getContentAccessLogs\(\{ limit, offset, mockId, userId \}\);\s*\},'

clean_impl = """async getContentAccessLogs({ limit = 50, offset = 0, mockId = null, userId = null } = {}) {
    if (dbPool) {
      try {
        let whereClause = 'WHERE 1=1';
        const params = [];
        if (mockId) {
          params.push(mockId);
          whereClause += ' AND l.mock_id = $' + params.length;
        }
        if (userId) {
          params.push(userId);
          whereClause += ' AND l.user_id = $' + params.length;
        }
        params.push(limit);
        const limitParam = '$' + params.length;
        params.push(offset);
        const offsetParam = '$' + params.length;

        const logsRes = await dbPool.query(
          `SELECT l.id, l.user_id, l.mock_id, l.section_type, l.ip_address, l.user_agent, l.access_granted, l.denial_reason, l.created_at,
                  u.email, u.full_name
           FROM public.scale_content_access_logs l
           LEFT JOIN public.scale_users u ON l.user_id = u.id
           ${whereClause}
           ORDER BY l.created_at DESC
           LIMIT ${limitParam} OFFSET ${offsetParam}`,
          params
        );

        const countRes = await dbPool.query(`SELECT count(*) FROM public.scale_content_access_logs l ${whereClause}`, params.slice(0, -2));

        return {
          logs: logsRes.rows,
          total: parseInt(countRes.rows[0].count, 10)
        };
      } catch (err) {
        console.error('[Get Content Access Logs Error]:', err);
        return { logs: [], total: 0 };
      }
    }
    return localStore.getContentAccessLogs({ limit, offset, mockId, userId });
  },"""

code = re.sub(target_regex, clean_impl, code)

with open('backend/src/db/supabase.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Properly replaced getContentAccessLogs via Python")

