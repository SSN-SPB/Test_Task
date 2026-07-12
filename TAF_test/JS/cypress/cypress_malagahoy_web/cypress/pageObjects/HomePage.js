import Logger from "../support/Logger";

class HomePage {

    getLogo() {

        return cy.get("img");

    }

    getSearchButton() {

        return cy.get("button").first();

    }

    verifyTitleContains(text) {

        Logger.info("Checking page title");

        cy.title().should("contain", text);

    }

}

export default new HomePage();