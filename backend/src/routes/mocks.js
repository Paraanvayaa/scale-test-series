const express = require('express');
const fs = require('fs');
const path = require('path');
const config = require('../config');
const { db } = require('../db/supabase');
const { requireAuth, optionalAuth } = require('../middleware/auth');

const router = express.Router();

// Memory cache for mock markdown files (fast, prevents redundant disk I/O)
const mockContentCache = new Map();

// In-memory rate limiter for content endpoint: max 40 content loads per 60s per key
const contentRateLimits = new Map();

function checkRateLimit(key, maxRequests = 40, windowMs = 60000) {
  const now = Date.now();
  let record = contentRateLimits.get(key);
  if (!record || now - record.resetTime > windowMs) {
    record = { count: 1, resetTime: now };
    contentRateLimits.set(key, record);
    return true;
  }
  record.count++;
  if (record.count > maxRequests) {
    return false;
  }
  return true;
}

// Helper to load mock markdown files from backend/data/mocks
async function loadMockDocuments(mockId) {
  const pad = 'Mock_' + String(mockId).padStart(2, '0');
  if (mockContentCache.has(pad)) {
    return mockContentCache.get(pad);
  }

  // Look in backend/data/mocks first, then neet_mock_tests as fallback
  let mockDir = path.resolve(__dirname, '../data/mocks', pad);
  if (!fs.existsSync(mockDir)) {
    mockDir = path.resolve(__dirname, '../../../neet_mock_tests', pad);
  }

  if (!fs.existsSync(mockDir)) {
    throw new Error(`Mock examination files not found for ${pad}`);
  }

  const qpPath = path.join(mockDir, 'Question_Paper.md');
  const solPath = path.join(mockDir, 'Detailed_Solutions.md');
  const keyPath = path.join(mockDir, 'Answer_Key_and_Analysis.md');

  const [qpContent, solContent, keyContent] = await Promise.all([
    fs.promises.readFile(qpPath, 'utf8'),
    fs.promises.readFile(solPath, 'utf8'),
    fs.promises.readFile(keyPath, 'utf8')
  ]);

  const docs = { qpContent, solContent, keyContent };
  mockContentCache.set(pad, docs);
  return docs;
}

// 1. Get Mock Examination Metadata & Entitlement Check
router.get('/:mockId', optionalAuth, async (req, res) => {
  const mockId = parseInt(req.params.mockId, 10);
  if (isNaN(mockId) || mockId < 1 || mockId > 60) {
    return res.status(404).json({ error: 'MOCK_NOT_FOUND', message: 'Invalid mock test number (1 - 60).' });
  }

  const isDemo = config.product.freeDemoMocks.includes(mockId);
  if (isDemo) {
    return res.json({
      mockId,
      isDemo: true,
      hasAccess: true,
      tier: mockId <= 20 ? 'Ignite' : mockId <= 40 ? 'Conquer' : 'Dominate'
    });
  }

  // Non-demo mock: Requires authenticated user AND active entitlement!
  if (!req.user) {
    return res.status(401).json({
      error: 'UNAUTHENTICATED',
      locked: true,
      mockId,
      message: 'Sign in to access this full-length examination.'
    });
  }

  const user = await db.getUserById(req.user.id);
  if (user && user.is_suspended) {
    return res.status(403).json({
      error: 'ACCOUNT_SUSPENDED',
      locked: true,
      mockId,
      message: 'Your account is suspended. Please contact platform support.'
    });
  }

  const hasAccess = await db.hasActiveEntitlement(req.user.id, config.product.code);
  if (!hasAccess) {
    return res.status(403).json({
      error: 'ENTITLEMENT_REQUIRED',
      locked: true,
      mockId,
      priceINR: config.product.pricePaise / 100,
      message: 'This mock test is locked. Unlock all 60 mocks for ₹999.'
    });
  }

  return res.json({
    mockId,
    isDemo: false,
    hasAccess: true,
    tier: mockId <= 20 ? 'Ignite' : mockId <= 40 ? 'Conquer' : 'Dominate'
  });
});

// 2. Protected Content Delivery Endpoint (Phase 2 & Phase 3)
// Delivers Question Paper, Detailed Solutions, and Answer Key with verified dynamic watermark
router.get('/:mockId/content', optionalAuth, async (req, res) => {
  const mockId = parseInt(req.params.mockId, 10);
  if (isNaN(mockId) || mockId < 1 || mockId > 60) {
    return res.status(404).json({ error: 'MOCK_NOT_FOUND', message: 'Invalid mock test number (1 - 60).' });
  }

  const ipAddress = req.ip || req.connection?.remoteAddress || '127.0.0.1';
  const userAgent = req.headers['user-agent'] || 'Unknown';
  const rateLimitKey = `${req.user ? req.user.id : ipAddress}:${mockId}`;

  if (!checkRateLimit(rateLimitKey)) {
    return res.status(429).json({
      error: 'RATE_LIMIT_EXCEEDED',
      message: 'Too many content requests. Please slow down and try again shortly.'
    });
  }

  const isDemo = config.product.freeDemoMocks.includes(mockId);
  let studentUser = null;

  if (req.user) {
    studentUser = await db.getUserById(req.user.id);
    if (studentUser && studentUser.is_suspended) {
      await db.logContentAccess({
        userId: req.user.id,
        mockId,
        ipAddress,
        userAgent,
        accessGranted: false,
        denialReason: 'ACCOUNT_SUSPENDED'
      });
      return res.status(403).json({
        error: 'ACCOUNT_SUSPENDED',
        message: 'Your account is currently suspended. Please contact platform support.'
      });
    }
  }

  // Non-demo mocks require authenticated session + verified active entitlement!
  if (!isDemo) {
    if (!req.user || !studentUser) {
      await db.logContentAccess({
        userId: null,
        mockId,
        ipAddress,
        userAgent,
        accessGranted: false,
        denialReason: 'UNAUTHENTICATED'
      });
      return res.status(401).json({
        error: 'UNAUTHENTICATED',
        message: 'Sign in to access this proprietary examination paper.'
      });
    }

    const hasAccess = await db.hasActiveEntitlement(req.user.id, config.product.code);
    if (!hasAccess) {
      await db.logContentAccess({
        userId: req.user.id,
        mockId,
        ipAddress,
        userAgent,
        accessGranted: false,
        denialReason: 'ENTITLEMENT_REQUIRED'
      });
      return res.status(403).json({
        error: 'ENTITLEMENT_REQUIRED',
        message: 'Active entitlement required. Unlock all 60 mocks for ₹999.'
      });
    }
  }

  try {
    const docs = await loadMockDocuments(mockId);

    // Dynamic watermark identity verified server-side
    const watermarkInfo = {
      studentName: studentUser ? (studentUser.full_name || 'NEET Aspirant') : 'Free Demo Aspirant',
      studentEmail: studentUser ? studentUser.email : 'Diagnostic Free Demo',
      studentId: studentUser ? studentUser.id.slice(0, 8).toUpperCase() : 'DEMO',
      timestamp: new Date().toISOString()
    };

    // Log authorized content delivery in security audit table
    await db.logContentAccess({
      userId: studentUser ? studentUser.id : null,
      mockId,
      ipAddress,
      userAgent,
      accessGranted: true,
      denialReason: null
    });

    // Security headers: Prevent shared public caching of proprietary examination materials
    res.setHeader('Cache-Control', 'private, no-cache, no-store, must-revalidate');
    res.setHeader('Pragma', 'no-cache');
    res.setHeader('Expires', '0');

    return res.json({
      success: true,
      mockId,
      isDemo,
      tier: mockId <= 20 ? 'Ignite' : mockId <= 40 ? 'Conquer' : 'Dominate',
      qpContent: docs.qpContent,
      solContent: docs.solContent,
      keyContent: docs.keyContent,
      watermarkInfo
    });
  } catch (err) {
    console.error(`[Mock Content Error for #${mockId}]:`, err);
    return res.status(500).json({
      error: 'CONTENT_DELIVERY_ERROR',
      message: 'Failed to retrieve examination content.'
    });
  }
});

// 3. Submit Answers / Progress (Revalidates session before writes)
router.post('/:mockId/submit', requireAuth, async (req, res) => {
  const mockId = parseInt(req.params.mockId, 10);
  const { responses, timeSpentSeconds, isFinal } = req.body;

  const isDemo = config.product.freeDemoMocks.includes(mockId);
  if (!isDemo) {
    const hasAccess = await db.hasActiveEntitlement(req.user.id, config.product.code);
    if (!hasAccess) {
      return res.status(403).json({ error: 'ENTITLEMENT_REQUIRED', message: 'Entitlement required.' });
    }
  }

  return res.json({
    success: true,
    mockId,
    userId: req.user.id,
    savedAt: new Date().toISOString(),
    status: isFinal ? 'completed' : 'in_progress'
  });
});

module.exports = router;
