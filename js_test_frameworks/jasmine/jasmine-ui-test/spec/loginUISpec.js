console.log("✅ Loaded spec WebUI2!");
const { Builder, By, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const path = require('chromedriver').path; // Get actual path to chromedriver

describe('SauceDemo Login Test', () => {
  let driver;

  beforeAll(async (done) => {
    try {
      const service = new chrome.ServiceBuilder(path).build();
      chrome.setDefaultService(service);

      driver = await new Builder().forBrowser('chrome').build();
      await driver.get('https://www.saucedemo.com/');
      done();
    } catch (error) {
      console.error('❌ Error in beforeAll:', error);
      done.fail(error);
    }
  }, 30000);

  afterAll(async () => {
    if (driver) {
      await driver.quit();
    }
  });

  it('should log in with valid credentials', async () => {
    const usernameField = await driver.findElement(By.id('user-name'));
    const passwordField = await driver.findElement(By.id('password'));
    const loginButton = await driver.findElement(By.id('login-button'));

    await usernameField.sendKeys('standard_user');
    await passwordField.sendKeys('secret_sauce');
    await loginButton.click();

    await driver.wait(until.urlContains('inventory.html'), 5000);
    const currentUrl = await driver.getCurrentUrl();
    expect(currentUrl).toContain('inventory.html');
  });
});