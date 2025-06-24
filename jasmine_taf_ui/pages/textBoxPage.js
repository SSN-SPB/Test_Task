class TextBoxPage {
  constructor() {
    this.fullName = element(by.id('userName'));
    this.email = element(by.id('userEmail'));
    this.currentAddress = element(by.id('currentAddress'));
    this.permanentAddress = element(by.id('permanentAddress'));
    this.submitButton = element(by.id('submit'));
    this.outputName = element(by.id('name'));
    this.outputEmail = element(by.id('email'));
    this.outputCurrentAddress = element(by.cssContainingText('p', 'Current Address'));
    this.outputPermanentAddress = element(by.cssContainingText('p', 'Permananet Address'));
  }

  async fillForm(data) {
    await this.fullName.sendKeys(data.name);
    await this.email.sendKeys(data.email);
    await this.currentAddress.sendKeys(data.currentAddress);
    await this.permanentAddress.sendKeys(data.permanentAddress);
    await this.submitButton.click();
  }
}

module.exports = new TextBoxPage();