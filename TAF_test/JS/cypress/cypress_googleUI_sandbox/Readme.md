## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd TAF_test\JS\cypress\cypress_googleUI_sandbox
   ```

2. **Install dependencies:**
2.1 Make sure you have Node.js (v14 or higher recommended), npx and cypress installed.
    ```bash
    node -v
    npm -v
    npx -v
   ```
2.2. Create package.json file by command
   ```bash
   npm init -y
   ```
2.3 Install cypress:
   ```bash
    npx install cypress --save-dev
   ```

2.3.1 Check version
   ```bash
    npx cypress version
   ```
2.4 Create empty support file

├── cypress/
│   ├── e2e/
│   │   └── testFile.cy.js
│   │
│   └── support/
│       └── e2e.js

## Running Tests

1. **Open Cypress Test Runner:**
   Within the project directory, run the following command to open the Cypress Test Runner:
   ```bash
   npx cypress open
   ```
   This will launch the Cypress Test Runner where you can select and run your tests.

2. **Run Tests in different modes:**
   ```bash
   npx cypress run                            - CI/CD pipelines (Jenkins, GitHub Actions, Azure DevOps)
   npx cypress run --headed 				  - Debugging from the CLI
   npx cypress run --headed --browser chrome  - Browser-specific debugging
   npx cypress run --browser edge             - Browser-specific debugging
   ```
Supported --browser chrome/electron/edge/firefox/chromium <br>
This will execute all tests in headless mode and provide a summary of the test results in the terminal.

