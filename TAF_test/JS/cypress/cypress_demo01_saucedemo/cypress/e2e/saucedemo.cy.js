describe('SauceDemo UI Test', () => {
  it('should load the login page', () => {
    cy.visit('https://www.saucedemo.com/');
    
    // Check if login elements exist
    cy.get('#user-name').should('be.visible');
    cy.get('#password').should('be.visible');
    cy.get('#login-button').should('be.visible');
  });
});