import BasePage from "./base_page";

class GridPage extends BasePage {
  constructor(sizeLabel, tableSize) {
    super();
    this.sizeLabel = sizeLabel;
    this.tableSize = tableSize;
    this.gridDimension = Math.sqrt(tableSize);
    this.menuButton = `button.size:contains('${sizeLabel}')`;
  }

  load() {
    this.navigateTo("/");
    cy.get(this.menuButton).click();
    this.waitForSelector(BasePage.BOARD_SELECTOR);
  }

  isDisplayed() {
    return this.isBoardVisible();
  }

  getTableElementsCount() {
    return this.getCellCount();
  }

  hasCorrectNumberOfCells() {
    return this.getCellCount().should("eq", this.tableSize);
  }

  hasUniqueNumbers() {
    return this.getCellValues().then((values) => {
      const unique = new Set(values);
      expect(unique.size).to.eq(this.tableSize);
    });
  }

  getExpectedValues() {
    const expected = new Set();
    for (let i = 1; i <= this.tableSize; i++) {
      expected.add(String(i));
    }
    return expected;
  }

  isActive() {
    return cy.get(this.menuButton).should("have.class", "active");
  }
}

export default GridPage;
