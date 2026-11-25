const dotenv = require('dotenv');
dotenv.config();

const config = {
  port: parseInt(process.env.PORT || '4000', 10),
  nodeEnv: process.env.NODE_ENV || 'development',
  frontendOrigin: process.env.FRONTEND_ORIGIN || 'https://scaletestseries.web.app',

  // Product & Pricing Configuration (Server-Side Source of Truth)
  product: {
    code: 'SCALE_NEET_60_MOCKS',
    name: 'Scale Test Series 60 Full-Length Mocks',
    pricePaise: 99900, // ₹999 INR
    currency: 'INR',
    freeDemoMocks: [1, 21, 41]
  },

  // Supabase Configuration
  supabase: {
    url: process.env.SUPABASE_URL || 'https://mock-supabase.local',
    anonKey: process.env.SUPABASE_ANON_KEY || 'mock-anon-key',
    serviceRoleKey: process.env.SUPABASE_SERVICE_ROLE_KEY || 'mock-service-role-key'
  },

  // Razorpay Configuration
  razorpay: {
    keyId: process.env.RAZORPAY_KEY_ID || 'rzp_test_placeholder',
    keySecret: process.env.RAZORPAY_KEY_SECRET || 'secret_placeholder',
    webhookSecret: process.env.RAZORPAY_WEBHOOK_SECRET || 'webhook_secret_placeholder'
  },

  // Application Session & Cookie Settings
  session: {
    cookieName: 'app_session',
    tokenBytes: 32, // 32 bytes = 64 hex chars opaque token
    cookieMaxAgeMs: 30 * 24 * 60 * 60 * 1000 // 30 days
  }
};

module.exports = config;

