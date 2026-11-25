const app = require('./app');
const config = require('./config');

const server = app.listen(config.port, () => {
  console.log(`====================================================`);
  console.log(` Scale Test Series Production Backend Running`);
  console.log(` Port: ${config.port}`);
  console.log(` Environment: ${config.nodeEnv}`);
  console.log(` Health: http://localhost:${config.port}/health`);
  console.log(`====================================================`);
});

// Graceful Shutdown
function handleShutdown(signal) {
  console.log(`\n[Server] Received ${signal}. Closing HTTP server...`);
  server.close(() => {
    console.log('[Server] HTTP server closed gracefully.');
    process.exit(0);
  });
}

process.on('SIGTERM', () => handleShutdown('SIGTERM'));
process.on('SIGINT', () => handleShutdown('SIGINT'));

module.exports = server;

