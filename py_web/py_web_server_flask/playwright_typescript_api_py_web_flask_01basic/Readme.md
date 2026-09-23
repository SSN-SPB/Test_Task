# Playwright TypeScript API tests for Flask

This project contains Playwright TypeScript API tests for the Flask server in:

```text
..\py_web_flask_01basic
```

The tests are intentionally independent from Flask server lifecycle management.
They do not start or stop the server. Start the Flask server separately, keep it
running, execute the Playwright tests, and stop the server manually afterwards.

## Requirements

- Python 3.11 or a compatible Python version
- Node.js 18 or newer
- npm
- A running Flask server at `http://127.0.0.1:5000`

## Start the Flask server

Open a terminal in the Flask application directory:

```powershell
cd ..\py_web_flask_01basic
python run.py
```

Leave this terminal running. Verify that the server responds before starting
the tests:

```powershell
Invoke-WebRequest http://127.0.0.1:5000/api/health
Invoke-WebRequest http://127.0.0.1:5000/api/users
```

## Set up the Playwright TypeScript environment

Open a second terminal in this test project directory:

```powershell
cd ..\playwright_typescript_api_py_web_flask_01basic
npm install
npx playwright install
```

`npm install` installs the project dependencies, including
`@playwright/test`, TypeScript, and Node.js type definitions.
`npx playwright install` installs the Playwright browser binaries. The API
tests do not open a browser, but installing the binaries keeps the project
ready for regular Playwright commands and future browser-based tests.

## Run the tests

Run all API tests:

```powershell
npm test
```

Run the tests in headed mode:

```powershell
npm run test:headed
```

List the tests without executing requests:

```powershell
npm run test:list
```

The suite contains five tests:

- `GET /api/health` returns HTTP 200.
- `GET /api/health` returns `status: "ok"`.
- `GET /api/health` returns `service: "flask-training"`.
- `GET /api/users` returns HTTP 200.
- `GET /api/users` returns the expected three users.

## Use another Flask URL

The default base URL is:

```text
http://127.0.0.1:5000
```

Override it with the `FLASK_BASE_URL` environment variable:

```powershell
$env:FLASK_BASE_URL = "http://localhost:5000"
npm test
```

In Command Prompt:

```bat
set FLASK_BASE_URL=http://localhost:5000
npm test
```

## Project structure

```text
playwright_typescript_api_py_web_flask_01basic/
├── tests/
│   ├── health.spec.ts
│   └── users.spec.ts
├── package.json
├── playwright.config.ts
├── tsconfig.json
└── Readme.md
```
