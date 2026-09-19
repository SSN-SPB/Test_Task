# Target of tests
Testing REST API response for launched flask server from folder <br>
..\py_web_flask_01basic

# Precondition
Flask server should be started first. <br>
See ..\py_web_flask_01basic\Readme.md

# Start tests
run command: 
```pytest```
in the root directory

# Covered endpoints

The suite contains live API tests for the following endpoints:

- `GET /api/health` checks the `200` response, status, and service name.
- `GET /api/users` checks the `200` response and the returned list of users.

The Flask server must be running at `http://127.0.0.1:5000` before starting the tests.