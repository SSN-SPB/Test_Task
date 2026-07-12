import HomePage from "../pageObjects/HomePage";
import BrowserService from "../services/BrowserService";
import Logger from "../support/Logger";

describe("Malaga Hoy Home Page", () => {

    beforeEach(() => {

        BrowserService.openHomePage();

        BrowserService.waitForPageLoaded();

        cy.acceptCookies();

    });

    it("Verify homepage title", () => {

        cy.fixture("testData").then((data) => {

            Logger.info("Starting title verification");

            HomePage.verifyTitleContains(data.expectedTitle);

        });

    });

    it("Verify logo exists", () => {

        Logger.info("Checking logo");

        HomePage.getLogo()

            .should("be.visible");

    });

});