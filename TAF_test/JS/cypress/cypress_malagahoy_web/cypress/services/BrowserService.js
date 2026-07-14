import Logger from "../support/Logger";

class BrowserService {

    openHomePage() {

        Logger.info("Opening Home Page");

        cy.visit("/");

    }

    waitForPageLoaded() {

        Logger.info("Waiting for page load");

        cy.get("body").should("be.visible");

    }

    getTitle() {

        return cy.title();

    }

}

export default new BrowserService();