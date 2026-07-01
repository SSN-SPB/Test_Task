# Structure
```
├── e2e/
│   └── users/
│       └── createUser.cy.js
│
├── fixtures/
│   └── users.json
│
├── models/
│   └── User.js
│
├── services/
│   ├── BaseService.js
│   └── UserService.js
│
├── support/
│   ├── commands.js
│   ├── e2e.js
│   └── logger.js
│
└── utils/
    └── env.js

cypress.config.js
package.json

```
# Install dependencies
```bash
npm install
```
# Run tests
```bash
npx cypress open
``` 
# Description
This project demonstrates how to structure API tests in Cypress using a modular approach. It includes separate directories for test cases, fixtures, models, services, and support utilities. The `createUser.cy.js` file contains test cases for creating a user, while the `UserService.js` file encapsulates the logic for making API requests related to user operations. The `BaseService.js` provides common functionality for all services, and the `env.js` file manages environment variables. This structure promotes maintainability and scalability of your test suite.
