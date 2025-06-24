const textBoxPage = require('../pages/textBoxPage');
const testData = require('../data/textBoxData.json');

describe('DemoQA Text Box Form', () => {
  beforeAll(() => {
    browser.waitForAngularEnabled(false);
    browser.get('https://demoqa.com/text-box');
  });

  it('should fill form and validate output', async () => {
    await textBoxPage.fillForm(testData);

    expect(await textBoxPage.outputName.getText()).toBe(`Name:${testData.name}`);
    expect(await textBoxPage.outputEmail.getText()).toBe(`Email:${testData.email}`);
    expect(await textBoxPage.outputCurrentAddress.getText()).toBe(`Current Address :${testData.currentAddress}`);
    expect(await textBoxPage.outputPermanentAddress.getText()).toBe(`Permananet Address :${testData.permanentAddress}`);
  });
});