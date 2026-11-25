const express = require('express');
const cors = require('cors');
const cookieParser = require('cookie-parser');
const helmet = require('helmet');
const config = require('./config');

const authRoutes = require('./routes/auth');
const paymentRoutes = require('./routes/payments');
const mockRoutes = require('./routes/mocks');
const adminRoutes = require('./routes/admin');

const app = express();

// Security Headers
app.use(helmet({
  contentSecurityPolicy: false,
  crossOriginResourcePolicy: { policy: "cross-origin" }
}));

// CORS Configuration with Credential Support for HttpOnly Cookies
const allowedOrigins = [
  config.frontendOrigin,
  'https://scaletestseries.web.app',
  'https://scaletestseries.firebaseapp.com',
  'http://localhost:3000',
  'http://localhost:5000',
  'http://127.0.0.1:5000',
  'http://localhost:8080'
];

app.use(cors({
  origin: (origin, callback) => {
    // Allow requests with no origin (like mobile apps, curl, server-to-server)
    if (!origin) return callback(null, true);
    if (allowedOrigins.includes(origin) || origin.endsWith('.web.app') || origin.endsWith('.firebaseapp.com')) {
      return callback(null, true);
    }
    return callback(null, true); // Permissive in dev/staging for seamless frontend testing
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With', 'x-razorpay-signature']
}));

app.use(cookieParser());

// Webhook route needs raw body for HMAC signature verification
app.use('/api/payments/webhook', express.raw({ type: '*/*' }));

// JSON parser for all other routes
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Health Check Endpoint (DEP-03 on Render)
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
    service: 'Scale Test Series Backend',
    version: '1.0.0',
    database: config.supabase.url ? 'configured' : 'in-memory-engine',
    payments: config.razorpay.keyId ? 'configured' : 'sandbox-mode'
  });
});

// Mount API Routes
app.use('/api/auth', authRoutes);
app.use('/api/payments', paymentRoutes);
app.use('/api/mocks', mockRoutes);
app.use('/api/v1/admin', adminRoutes);
app.use('/api/admin', adminRoutes);

// Static Web Hosting (Serve Admin Portal & Mock Tests UI)
const path = require('path');
const mockTestsDir = path.join(__dirname, '../../mock_tests');
app.use('/admin', express.static(path.join(mockTestsDir, 'admin')));
app.use(express.static(mockTestsDir));

// 404 Handler
app.use((req, res) => {
  res.status(404).json({ error: 'NOT_FOUND', message: `Route ${req.method} ${req.url} not found.` });
});

// Central Error Handler
app.use((err, req, res, next) => {
  console.error('[Unhandled Server Error]:', err);
  res.status(500).json({
    error: 'INTERNAL_SERVER_ERROR',
    message: err.message || 'An unexpected error occurred.'
  });
});

module.exports = app;

