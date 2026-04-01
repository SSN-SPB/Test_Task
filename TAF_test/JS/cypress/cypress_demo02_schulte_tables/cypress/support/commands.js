// Custom commands for Schulte Table tests

// Navigate to a specific grid size
Cypress.Commands.add("navigateToGridSize", (sizeLabel) => {
  cy.visit("/");
  cy.get("button.size").contains(sizeLabel).click();
  cy.get(".board-container").should("exist");
});

// Get all cell values as an array
Cypress.Commands.add("getCellValues", () => {
  const values = [];
  return cy.get(".cell").each(($cell) => {
    values.push($cell.text());
  }).then(() => values);
});

// Click a cell by its number value
Cypress.Commands.add("clickCellByNumber", (number) => {
  const target = String(number);
  cy.get(".cell").each(($cell) => {
    if ($cell.text() === target) {
      cy.wrap($cell).click();
      return false;
    }
  });
});
