class Logger {

    info(message) {
        cy.log(`INFO : ${message}`);
        console.log(`INFO : ${message}`);
    }

    warning(message) {
        cy.log(`WARNING : ${message}`);
        console.warn(message);
    }

    error(message) {
        cy.log(`ERROR : ${message}`);
        console.error(message);
    }

}

export default new Logger();