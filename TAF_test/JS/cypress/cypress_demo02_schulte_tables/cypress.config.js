const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "https://schultetable.web.app",
    viewportWidth: 1280,
    viewportHeight: 720,
    defaultCommandTimeout: 5000,
    specPattern: "cypress/e2e/**/*.cy.js",
    supportFile: "cypress/support/e2e.js",
  },
});
