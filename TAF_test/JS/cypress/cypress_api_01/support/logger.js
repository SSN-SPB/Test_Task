export class Logger {

  static request(method, url, body = null) {
    cy.log(`REQUEST: ${method} ${url}`);

    if (body) {
      cy.log(`BODY: ${JSON.stringify(body)}`);
    }
  }

  static response(response) {
    cy.log(`STATUS: ${response.status}`);
    cy.log(`RESPONSE: ${JSON.stringify(response.body)}`);
  }

}