const { test, expect } = require('@playwright/test');
const { TextBoxPage } = require('../pages/textBoxPage');
const { validUser } = require('../utils/testData');

test.describe('Text Box Form Tests', () => {
  test('should fill form and verify output', async ({ page }) => {
    const textBoxPage = new TextBoxPage(page);
    await textBoxPage.navigate();
    await textBoxPage.fillForm(validUser);

    const output = await textBoxPage.getOutput();
    expect(output.name).toContain(validUser.name);
    expect(output.email).toContain(validUser.email);
  });
});