// Real-Time Session Revocation Manager (Server-Sent Events)
class RealtimeSessionManager {
  constructor() {
    this.connections = new Map(); // sessionId -> Set of SSE response objects
  }

  registerConnection(sessionId, res) {
    if (!this.connections.has(sessionId)) {
      this.connections.set(sessionId, new Set());
    }
    this.connections.get(sessionId).add(res);

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
      const set = this.connections.get(sessionId);
      if (set) {
        set.delete(res);
        if (set.size === 0) this.connections.delete(sessionId);
      }
    });
  }

  notifySessionRevoked(sessionId, reason = 'REPLACED_BY_NEW_DEVICE') {
    if (!sessionId) return;
    const clientSet = this.connections.get(sessionId);
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
    this.connections.delete(sessionId);
  }
}

const realtime = new RealtimeSessionManager();
module.exports = realtime;

