exports.config = {
  framework: 'jasmine',
  directConnect: true,
  specs: ['tests/textBoxSpec.js'], // Update the path if needed
  capabilities: {
    browserName: 'chrome',
  },
  jasmineNodeOpts: {
    defaultTimeoutInterval: 30000,
  },
  onPrepare: () => {
    browser.waitForAngularEnabled(false); // because demoqa.com is not an Angular site
    browser.manage().window().maximize();
  }
};