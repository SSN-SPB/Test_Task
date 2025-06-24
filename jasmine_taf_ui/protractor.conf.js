exports.config = {
  framework: 'jasmine',
  directConnect: true,
  specs: ['tests/textBoxSpec.js'], // Update the path if needed
  // capabilities: {
  //   browserName: 'chrome',
  // },
  capabilities: {
  browserName: 'chrome',
  chromeOptions: {
    args: ['--disable-gpu', '--window-size=1920,1080']
    }
  },
chromeDriver: require('chromedriver').path,
  jasmineNodeOpts: {
    defaultTimeoutInterval: 30000,
  },
  onPrepare: () => {
    browser.waitForAngularEnabled(false); // because demoqa.com is not an Angular site
    browser.manage().window().maximize();
  }
};