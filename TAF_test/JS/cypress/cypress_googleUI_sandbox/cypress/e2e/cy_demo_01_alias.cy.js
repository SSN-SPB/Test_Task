describe("Alias cypress demo", () => {

    it("Treat alias as element", () => {

    cy.visit("https://google.com");

    cy.get('div').contains('Aceptar todo').as("searchButton");

    cy.get("@searchButton")
        .should("be.visible")
        .click();
    });

});