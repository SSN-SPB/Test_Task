Cypress.Commands.add("acceptCookies", () => {

    cy.get("body").then(($body) => {

        if ($body.text().includes("Aceptar")) {

            cy.contains("Aceptar").click({force:true});

        }

    });

});