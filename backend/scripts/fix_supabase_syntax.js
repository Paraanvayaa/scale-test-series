const fs = require('fs');
const path = require('path');

const filePath = path.resolve(__dirname, '../src/db/supabase.js');
let code = fs.readFileSync(filePath, 'utf8');

// Replace the mispositioned methods in LocalMemoryStore
const oldClassBlock = `  // Admin In-Memory Methods
  async logContentAccess({ userId, mockId, sectionType = 'ALL', ipAddress, userAgent, accessGranted, denialReason }) {
    if (dbPool) {
      try {
        await dbPool.query(
          \`INSERT INTO public.scale_content_access_logs 
           (user_id, mock_id, section_type, ip_address, user_agent, access_granted, denial_reason)
           VALUES ($1, $2, $3, $4, $5, $6, $7)\`,
          [userId || null, mockId, sectionType, ipAddress || null, userAgent || null, accessGranted, denialReason || null]
        );
        return true;
      } catch (err) {
        console.error('[Content Access Log Error]:', err.message);
        return false;
      }
    }
    return true;
  },

  async getContentAccessLogs({ limit = 50, offset = 0, mockId = null, userId = null } = {}) {
    if (dbPool) {
      try {
        let whereClause = 'WHERE 1=1';
        const params = [];
        if (mockId) {
          params.push(mockId);
          whereClause += \` AND l.mock_id = \${params.length}\`;
        }
        if (userId) {
          params.push(userId);
          whereClause += \` AND l.user_id = \${params.length}\`;
        }
        params.push(limit);
        const limitParam = \`\${params.length}\`;
        params.push(offset);
        const offsetParam = \`\${params.length}\`;

        const logsRes = await dbPool.query(
          \`SELECT l.id, l.user_id, l.mock_id, l.section_type, l.ip_address, l.user_agent, l.access_granted, l.denial_reason, l.created_at,
                  u.email, u.full_name
           FROM public.scale_content_access_logs l
           LEFT JOIN public.scale_users u ON l.user_id = u.id
           \${whereClause}
           ORDER BY l.created_at DESC
           LIMIT \${limitParam} OFFSET \${offsetParam}\`,
          params
        );

        const countRes = await dbPool.query(\`SELECT count(*) FROM public.scale_content_access_logs l \${whereClause}\`, params.slice(0, -2));

        return {
          logs: logsRes.rows,
          total: parseInt(countRes.rows[0].count, 10)
        };
      } catch (err) {
        console.error('[Get Content Access Logs Error]:', err);
        return { logs: [], total: 0 };
      }
    }
    return { logs: [], total: 0 };
  },`;

const newClassBlock = `  // Admin In-Memory Methods
  async logContentAccess({ userId, mockId, sectionType = 'ALL', ipAddress, userAgent, accessGranted, denialReason }) {
    return true;
  }

  async getContentAccessLogs({ limit = 50, offset = 0, mockId = null, userId = null } = {}) {
    return { logs: [], total: 0 };
  }`;

code = code.replace(oldClassBlock, newClassBlock);

// Now add logContentAccess and getContentAccessLogs to the exported db object
const dbTarget = `  // Generic query pass-through for ad-hoc SQL (profile updates, etc.)`;

const dbAddition = `  async logContentAccess({ userId, mockId, sectionType = 'ALL', ipAddress, userAgent, accessGranted, denialReason }) {
    if (dbPool) {
      try {
        await dbPool.query(
          \`INSERT INTO public.scale_content_access_logs 
           (user_id, mock_id, section_type, ip_address, user_agent, access_granted, denial_reason)
           VALUES ($1, $2, $3, $4, $5, $6, $7)\`,
          [userId || null, mockId, sectionType, ipAddress || null, userAgent || null, accessGranted, denialReason || null]
        );
        return true;
      } catch (err) {
        console.error('[Content Access Log Error]:', err.message);
        return false;
      }
    }
    return localStore.logContentAccess({ userId, mockId, sectionType, ipAddress, userAgent, accessGranted, denialReason });
  },

  async getContentAccessLogs({ limit = 50, offset = 0, mockId = null, userId = null } = {}) {
    if (dbPool) {
      try {
        let whereClause = 'WHERE 1=1';
        const params = [];
        if (mockId) {
          params.push(mockId);
          whereClause += \` AND l.mock_id = $\${params.length}\`;
        }
        if (userId) {
          params.push(userId);
          whereClause += \` AND l.user_id = $\${params.length}\`;
        }
        params.push(limit);
        const limitParam = \`$\${params.length}\`;
        params.push(offset);
        const offsetParam = \`$\${params.length}\`;

        const logsRes = await dbPool.query(
          \`SELECT l.id, l.user_id, l.mock_id, l.section_type, l.ip_address, l.user_agent, l.access_granted, l.denial_reason, l.created_at,
                  u.email, u.full_name
           FROM public.scale_content_access_logs l
           LEFT JOIN public.scale_users u ON l.user_id = u.id
           \${whereClause}
           ORDER BY l.created_at DESC
           LIMIT \${limitParam} OFFSET \${offsetParam}\`,
          params
        );

        const countRes = await dbPool.query(\`SELECT count(*) FROM public.scale_content_access_logs l \${whereClause}\`, params.slice(0, -2));

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
  },

  // Generic query pass-through for ad-hoc SQL (profile updates, etc.)`;

code = code.replace(dbTarget, dbAddition);

fs.writeFileSync(filePath, code, 'utf8');
console.log('Fixed syntax and properly wired content access logs in supabase.js');

