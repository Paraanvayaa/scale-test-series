// Real-Time Session & Entitlement Manager (Server-Sent Events)
class RealtimeSessionManager {
  constructor() {
    this.sessionConnections = new Map(); // sessionId -> Set of SSE response objects
    this.userConnections = new Map();    // userId -> Set of SSE response objects
  }

  registerConnection(sessionId, userId, res) {
    if (sessionId) {
      if (!this.sessionConnections.has(sessionId)) {
        this.sessionConnections.set(sessionId, new Set());
      }
      this.sessionConnections.get(sessionId).add(res);
    }

    if (userId) {
      if (!this.userConnections.has(userId)) {
        this.userConnections.set(userId, new Set());
      }
      this.userConnections.get(userId).add(res);
    }

    // Keep connection alive with heartbeat
    const heartbeat = setInterval(() => {
      try {
        res.write(': heartbeat\n\n');
      } catch {
        clearInterval(heartbeat);
      }
    }, 25000);

    res.on('close', () => {
      clearInterval(heartbeat);
      if (sessionId) {
        const set = this.sessionConnections.get(sessionId);
        if (set) {
          set.delete(res);
          if (set.size === 0) this.sessionConnections.delete(sessionId);
        }
      }
      if (userId) {
        const userSet = this.userConnections.get(userId);
        if (userSet) {
          userSet.delete(res);
          if (userSet.size === 0) this.userConnections.delete(userId);
        }
      }
    });
  }

  notifySessionRevoked(sessionId, reason = 'REPLACED_BY_NEW_DEVICE') {
    if (!sessionId) return;
    const clientSet = this.sessionConnections.get(sessionId);
    if (!clientSet || clientSet.size === 0) return;

    const payload = JSON.stringify({
      event: 'SESSION_REPLACED',
      title: 'Session Ended',
      description: 'Your account was signed in on another device. For security, this session has been logged out.',
      action: 'Sign In Again',
      reason
    });

    for (const res of clientSet) {
      try {
        res.write(`data: ${payload}\n\n`);
        res.end();
      } catch (err) {
        console.warn('[Realtime] Error sending revocation to socket:', err.message);
      }
    }
    this.sessionConnections.delete(sessionId);
  }

  notifyUserSuspended(userId, reason = 'ADMIN_SUSPENSION') {
    if (!userId) return;
    const clientSet = this.userConnections.get(userId);
    if (!clientSet || clientSet.size === 0) return;

    const payload = JSON.stringify({
      event: 'ACCOUNT_SUSPENDED',
      title: 'Account Suspended',
      description: 'Your account has been suspended by an administrator. Please contact support.',
      reason
    });

    for (const res of clientSet) {
      try {
        res.write(`data: ${payload}\n\n`);
        res.end();
      } catch (err) {
        console.warn('[Realtime] Error sending suspension to socket:', err.message);
      }
    }
    this.userConnections.delete(userId);
  }

  notifyUserEntitlement(userId, hasAccess, reason = 'ADMIN_UPDATE') {
    if (!userId) return;
    const clientSet = this.userConnections.get(userId);
    if (!clientSet || clientSet.size === 0) return;

    const payload = JSON.stringify({
      event: 'ENTITLEMENT_UPDATED',
      hasAccess: !!hasAccess,
      reason
    });

    for (const res of clientSet) {
      try {
        res.write(`data: ${payload}\n\n`);
      } catch (err) {
        console.warn('[Realtime] Error sending entitlement update to socket:', err.message);
      }
    }
  }
}

const realtime = new RealtimeSessionManager();
module.exports = realtime;
