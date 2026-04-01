class TableValidationService {
  static CELL_SELECTOR = ".cell";
  static BOARD_SELECTOR = ".board-container";

  validateTableHasCells(expectedCount) {
    cy.get(TableValidationService.CELL_SELECTOR).should("have.length", expectedCount);
  }

  getAllCellValues() {
    const values = [];
    return cy.get(TableValidationService.CELL_SELECTOR).each(($cell) => {
      values.push($cell.text());
    }).then(() => values);
  }

  validateUniqueNumbers(expectedCount) {
    return this.getAllCellValues().then((values) => {
      const unique = new Set(values);
      expect(unique.size).to.eq(expectedCount);
    });
  }

  validateNumbersInRange(maxNumber) {
    return this.getAllCellValues().then((values) => {
      const expected = new Set();
      for (let i = 1; i <= maxNumber; i++) {
        expected.add(String(i));
      }
      const actual = new Set(values);
      expect(actual).to.deep.eq(expected);
    });
  }

  validateBoardVisible() {
    cy.get(TableValidationService.BOARD_SELECTOR).should("be.visible");
  }

  getNextExpectedNumber() {
    return cy.get(".top-bar span").invoke("text");
  }

  clickNumberInOrder(number) {
    const target = String(number);
    cy.get(TableValidationService.CELL_SELECTOR).each(($cell) => {
      if ($cell.text() === target) {
        cy.wrap($cell).click();
        return false; // break .each()
      }
    });
  }
}

export default TableValidationService;
