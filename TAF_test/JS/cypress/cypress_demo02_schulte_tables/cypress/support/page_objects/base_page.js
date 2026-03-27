class BasePage {
  static BASE_URL = "https://schultetable.web.app";
  static CELL_SELECTOR = ".cell";
  static BOARD_SELECTOR = ".board-container";
  static RESTART_BUTTON = ".restart-button";
  static TOP_BAR = ".top-bar";
  static DESCRIPTION = ".desc";
  static NEXT_NUMBER = ".top-bar span";
  static TIMER = ".top-bar p:last-child";

  navigateTo(url) {
    cy.visit(url);
  }

  clickElement(selector) {
    cy.get(selector).click();
  }

  getText(selector) {
    return cy.get(selector).invoke("text");
  }

  waitForSelector(selector, timeout = 5000) {
    cy.get(selector, { timeout }).should("exist");
  }

  isElementVisible(selector) {
    return cy.get(selector).should("be.visible");
  }

  getBoardCells() {
    return cy.get(BasePage.CELL_SELECTOR);
  }

  getCellCount() {
    return this.getBoardCells().its("length");
  }

  getCellValues() {
    const values = [];
    return this.getBoardCells().each(($cell) => {
      values.push($cell.text());
    }).then(() => values);
  }

  clickCell(index) {
    this.getBoardCells().eq(index).click();
  }

  getNextNumber() {
    return cy.get(BasePage.NEXT_NUMBER).invoke("text");
  }

  clickRestart() {
    cy.get(BasePage.RESTART_BUTTON).click();
  }

  isBoardVisible() {
    return cy.get(BasePage.BOARD_SELECTOR).should("be.visible");
  }

  getDescriptionText() {
    return cy.get(BasePage.DESCRIPTION).invoke("text");
  }
}

export default BasePage;
