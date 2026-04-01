class MenuNavigationService {
  navigateToSize(sizeLabel) {
    cy.visit("/");
    cy.get(`button.size`).contains(sizeLabel).click();
    cy.get(".board-container").should("exist");
  }

  navigateToThreeByThree() {
    this.navigateToSize("3x3");
  }

  navigateToFourByFour() {
    this.navigateToSize("4x4");
  }

  navigateToFiveByFive() {
    this.navigateToSize("5x5");
  }

  navigateToSixBySix() {
    this.navigateToSize("6x6");
  }

  navigateToSevenBySeven() {
    this.navigateToSize("7x7");
  }

  navigateToEightByEight() {
    this.navigateToSize("8x8");
  }

  navigateToNineByNine() {
    this.navigateToSize("9x9");
  }
}

export default MenuNavigationService;
