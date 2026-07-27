# The folder's description and idea

                    Shared test data
                         │
                         ▼
                 testArrayData.js
                         │
                         ▼
                checkingFunction.js
                    /           \
                   /             \
                  ▼               ▼
             Cypress          Playwright
                  │               │
                  ▼               ▼
        response_codes.cy.js   response_codes.spec.js
                  │               │
                  ▼               ▼
              2 passed         2 passed

## Idea of project:
Comine two TAF in the same folder (Cypress and Playwright)<br>

## Project's structure
    05js_array_functions_07_ever_function_project_03_cypress/
    │
    ├── cypress/
    │   └── e2e/
    │       └── response_codes.cy.js
    │
    ├── tests/
    │   └── response_codes_playwright_test.spec.js
    │
    ├── checkingFunction.js
    ├── testArrayData.js
    ├── testingArrayApp.js
    │
    ├── cypress.config.js
    ├── playwright.config.js
    ├── package.json
    └── package-lock.json

## Required library installations
### Playwright
<li> npm install --save-dev @playwright/test</li>

### Cypress
<li> npm install --save-dev cypress </li>


## Required library checking
### Playwright
    npm list cypress                                            
    -- @playwright/test@1.61.1

### Cypress
    npm list @playwright/test                                   
    -- cypress@15.19.0


## Listing the tests
### Playwright
    npx playwright test --list

### Cypress
    Get-ChildItem cypress\e2e -Filter "*.cy.js"

## Configuration files
### Playwright
    playwright.config.js
    import { defineConfig } from "@playwright/test";

    export default defineConfig({
      testDir: ".",
      testMatch: "**/*.spec.js",
    });

### Cypress
    cypress.config.js
    import { defineConfig } from "cypress";
    
    export default defineConfig({
      e2e: {
        supportFile: false,
      },
    });


## package.json content
    {
      "name": "cypress-playwright-project",
      "version": "1.0.0",
      "type": "module",
      "scripts": {
        "cy:open": "cypress open",
        "cy:run": "cypress run",
        "cy:test": "cypress run --spec \"cypress/e2e/response_codes.cy.js\"",
        "pw:test": "playwright test",
        "pw:test:headed": "playwright test --headed",
        "pw:test:ui": "playwright test --ui"
      },
      "devDependencies": {
        "@playwright/test": "^1.0.0",
        "cypress": "^15.19.0"
      }

## The test suit structure
### Playwright
    test.describe(...)
    test(...)
    expect(...).toBe(true)
    expect(value).toBe(200)
    test.beforeAll()
    

### Cypress
    describe(...)
    it(...)
    expect(...).to.be.true
    expect(value).to.equal(200)
    before()

## Run tests
### Playwright
    npx playwright test
    npx playwright test response_codes.spec.js
    npm run pw:test
    

### Cypress
    npx cypress run
    npx cypress run response_codes.cy.js
    npm run cy:test

## Code Style format
    npx prettier --write .\*.js

