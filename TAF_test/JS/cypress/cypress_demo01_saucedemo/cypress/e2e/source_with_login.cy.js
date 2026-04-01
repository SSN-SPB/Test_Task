describe('SauceDemo Login Test', () => {
  it('should login successfully', () => {
    cy.visit('https://www.saucedemo.com/');
    
    cy.get('#user-name').type('standard_user');
    cy.get('#password').type('secret_sauce');
    cy.get('#login-button').click();

    // Verify successful login
    cy.url().should('include', '/inventory.html');
    cy.contains('Products').should('be.visible');
  });
});