## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd /TAF_test/JS/cypress/cypress_demo01_saucedemo
   ```

2. **Install dependencies:**
2.1 Make sure you have Node.js (v14 or higher recommended), npx and cypress installed.
    ```bash
    node -v
    npm -v
    npx -v
    cypress -v
   ```
2.2 If not - then run the following command to install the required dependencies:
    ```bash
    npx install cypress --save-dev
    ```

## Running Tests

1. **Open Cypress Test Runner:**
   ```bash
   npx cypress open
   ```
   This will launch the Cypress Test Runner where you can select and run your tests.

2. **Run Tests in Headless Mode:**
   ```bash
   npx cypress run
   ```
   This will execute all tests in headless mode and provide a summary of the test results in the terminal.
