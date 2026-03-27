import BasePage from "./base_page";

class HomePage extends BasePage {
  static SIDE_PANEL = ".side-panel-container";
  static GRID_SIZE_SECTION = ".grid-size";
  static GRID_SIZE_TITLE = ".grid-size .title";
  static SIZE_BUTTON = "button.size";
  static ACTIVE_SIZE_BUTTON = "button.size.active";
  static STATS_SECTION = ".stats";
  static BEST_TIME_VALUE = ".stats .value:first-of-type";
  static GAMES_VALUE = ".stats .value:last-of-type";

  load() {
    this.navigateTo("/");
    this.waitForSelector(BasePage.BOARD_SELECTOR);
  }

  getTitle() {
    return cy.title();
  }

  clickMenuItem(itemText) {
    cy.get(`button.size`).contains(itemText).click();
  }

  getActiveSize() {
    return cy.get(HomePage.ACTIVE_SIZE_BUTTON).invoke("text");
  }

  getAllSizeButtons() {
    const buttons = [];
    return cy.get(HomePage.SIZE_BUTTON).each(($btn) => {
      buttons.push($btn.text());
    }).then(() => buttons);
  }

  isSidePanelVisible() {
    return cy.get(HomePage.SIDE_PANEL).should("be.visible");
  }

  getBestTime() {
    return cy.get(HomePage.BEST_TIME_VALUE).invoke("text");
  }

  getGamesCount() {
    return cy.get(HomePage.GAMES_VALUE).invoke("text");
  }

  isStatsVisible() {
    return cy.get(HomePage.STATS_SECTION).should("be.visible");
  }
}

export default HomePage;
