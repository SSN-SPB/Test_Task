exports.TextBoxPage = class TextBoxPage {
  constructor(page) {
    this.page = page;
    this.fullNameInput = page.locator('#userName');
    this.emailInput = page.locator('#userEmail');
    this.currentAddressInput = page.locator('#currentAddress');
    this.permanentAddressInput = page.locator('#permanentAddress');
    this.submitButton = page.locator('#submit');
    this.outputName = page.locator('#output #name');
    this.outputEmail = page.locator('#output #email');
  }

  async navigate() {
    await this.page.goto('/text-box');
  }

  async fillForm({ name, email, currentAddress, permanentAddress }) {
    await this.fullNameInput.fill(name);
    await this.emailInput.fill(email);
    await this.currentAddressInput.fill(currentAddress);
    await this.permanentAddressInput.fill(permanentAddress);
    await this.submitButton.click();
  }

  async getOutput() {
    return {
      name: await this.outputName.textContent(),
      email: await this.outputEmail.textContent(),
    };
  }
};