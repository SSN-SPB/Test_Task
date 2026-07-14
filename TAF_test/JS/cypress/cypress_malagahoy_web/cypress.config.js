const { defineConfig } = require("cypress");

module.exports = defineConfig({

  e2e: {

    baseUrl: "https://www.malagahoy.es",

    viewportWidth: 1600,
    viewportHeight: 900,

    video: false,

    screenshotOnRunFailure: true

  }

});