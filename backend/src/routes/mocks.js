const express = require('express');
const config = require('../config');
const { db } = require('../db/supabase');
const { requireAuth, optionalAuth } = require('../middleware/auth');

const router = express.Router();

// 1. Get Mock Examination Metadata & Access Check
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

// 2. Submit Answers / Progress (Revalidates session before writes)
router.post('/:mockId/submit', requireAuth, async (req, res) => {
  const mockId = parseInt(req.params.mockId, 10);
  const { responses, timeSpentSeconds, isFinal } = req.body;

  // Session has already been verified by requireAuth middleware
  // If another device logged in simultaneously, requireAuth returned 401 SESSION_REPLACED!

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

