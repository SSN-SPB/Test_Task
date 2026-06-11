# Schulte Playwright UI Tests

This project contains automated UI tests for the Schulte Table application using Playwright and pytest. The tests are organized into a modular structure with Page Objects, Service Functions, Connectors, and a Logger for better maintainability and readability.

## Project Structure

```
schulte-playwright-ui-tests
├── connectors
│   ├── __init__.py
│   ├── browser_connector.py          # Manages Playwright browser lifecycle
│   └── site_connector.py             # Handles site navigation
├── logger
│   ├── __init__.py
│   └── logger.py                     # Centralized logging
├── page_objects
│   ├── __init__.py
│   ├── base_page.py                  # Base page with common selectors & methods
│   ├── home_page.py                  # Side panel, menu, stats
│   └── left_menu_pages
│       ├── __init__.py
│       ├── three_by_three_page.py
│       ├── four_by_four_page.py
│       ├── five_by_five_page.py
│       ├── six_by_six_page.py
│       ├── seven_by_seven_page.py
│       ├── eight_by_eight_page.py
│       └── nine_by_nine_page.py
├── service_functions
│   ├── __init__.py
│   ├── menu_navigation_service.py    # Navigate to grid sizes via menu
│   └── table_validation_service.py   # Validate board cells, numbers, gameplay
├── tests
│   ├── conftest.py                   # Fixtures: browser, page, setup
│   ├── three_by_three/
│   │   └── test_three_by_three_page.py
│   ├── four_by_four/
│   │   └── test_four_by_four_page.py
│   ├── five_by_five/
│   │   └── test_five_by_five_page.py
│   ├── six_by_six/
│   │   └── test_six_by_six_page.py
│   ├── seven_by_seven/
│   │   └── test_seven_by_seven_page.py
│   ├── eight_by_eight/
│   │   └── test_eight_by_eight_page.py
│   └── nine_by_nine/
│       └── test_nine_by_nine_page.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd schulte-playwright-ui-tests
   ```

2. **Install dependencies:**
   Make sure you have Python 3.7 or higher installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright Browsers:**
   After installing Playwright, you need to install the necessary browsers:
   ```bash
   playwright install
   ```

## Running Tests

To run the tests, use the following command:
```bash
pytest
```

You can also run tests for a specific page by navigating to the corresponding test folder and executing:
```bash
pytest test_<page_name>_page.py
```

## Allure Reporting

Test results are automatically saved to the `allure-results/` directory. To view the report:

1. **Install Allure CLI** (if not already installed):
   - **Windows (Scoop):** `scoop install allure`
   - **Windows (npm):** `npm install -g allure-commandline`
   - **macOS (Homebrew):** `brew install allure`
   - **Linux:** Download from [Allure releases](https://github.com/allure-framework/allure2/releases)

2. **Generate and open the report:**
   ```bash
   allure serve allure-results
   ```

   Or generate a static report:
   ```bash
   allure generate allure-results -o allure-report --clean
   allure open allure-report
   ```

The report includes:
- Test results grouped by **Feature** (Schulte Table) and **Story** (grid size)
- Human-readable test titles
- **Screenshots attached automatically on test failure**

## Project Components

- **Connectors:** Manages browser and site connections.
- **Logger:** Provides logging functionality for tracking test execution.
- **Page Objects:** Represents different pages of the application, encapsulating the interactions with those pages.
- **Service Functions:** Contains reusable functions for navigation and validation across different pages.
- **Tests:** Contains the actual test cases organized by page.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. Make sure to follow the coding standards and include tests for any new features or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

pip install -r requirements.txt
pytest
allure serve allure-results