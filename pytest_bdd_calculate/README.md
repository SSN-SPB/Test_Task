# Pytest BDD Calculate Demo

A simple demonstration of pytest BDD (Behavior-Driven Development) testing with a calculator that multiplies two numbers.

## Project Structure

```
pytest_bdd_calculate/
├── calculator.py           # Calculator business logic
├── test_multiply.py        # Step definitions for BDD tests
├── conftest.py            # Pytest configuration
├── requirements.txt       # Python dependencies
├── features/
│   └── multiply.feature   # BDD feature file with scenarios
└── README.md             # This file
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

Run the pytest BDD tests:
```bash
pytest test_multiply.py -v
```

Or run with feature file output:
```bash
pytest test_multiply.py -v --gherkin-terminal-reporter
```

## Features

The project includes 3 test scenarios:
1. **Multiply two positive numbers**: 5 × 3 = 15
2. **Multiply negative and positive numbers**: -4 × 6 = -24
3. **Multiply by zero**: 7 × 0 = 0

## How it Works

- **features/multiply.feature**: Gherkin syntax scenarios
- **test_multiply.py**: Python step definitions using `@given`, `@when`, `@then` decorators
- **calculator.py**: Pure Python calculator class with multiply logic
