# Quick Start Guide

## What's Included

Your Java REST API Test Automation Framework includes:

```
copilot_java_backend/
├── pom.xml                              # Maven build configuration
├── README.md                            # Full documentation
├── SETUP.md                             # Installation & setup instructions
├── .gitignore                           # Git ignore rules
└── src/
    ├── main/java/com/restapi/test/
    │   └── client/
    │       └── HttpClientUtil.java      # HTTP utility for making GET requests
    └── test/java/com/restapi/test/
        └── RestGetStatusCodeTest.java   # Test cases for Google & Python.org
```

## Framework Features

✓ **3 Test Methods**
- Individual test for Google (https://www.google.com)
- Individual test for Python.org (https://www.python.org)
- Parameterized test that runs both URLs with same test logic

✓ **Technologies**
- JUnit 5 for testing framework
- Apache HttpClient 5 for HTTP requests
- Maven for build management

✓ **Assertions**
- Validates HTTP 200 response code for both websites
- Clear assertion messages for debugging

## Step-by-Step to Run Tests

1. **Install Java 11+** (if not already installed)
   ```
   java -version
   ```

2. **Install Maven** (if not already installed)
   ```
   mvn -version
   ```

3. **Navigate to project directory**
   ```
   cd copilot_java_backend
   ```

4. **Run all tests**
   ```
   mvn test
   ```

5. **Run a single test**
   ```
   mvn test -Dtest=RestGetStatusCodeTest#testGoogleStatusCode
   ```

## Test Results

All tests pass when:
- Google homepage returns HTTP 200
- Python.org returns HTTP 200

## Extending the Framework

### Add a new website test
Edit `src/test/java/com/restapi/test/RestGetStatusCodeTest.java` and add to `@ValueSource`:

```java
//@ValueSource(strings = {
//    "https://www.google.com", 
//    "https://www.python.org",
//    "https://www.new-site.com"  // Add here
//})
```

### Add response body validation
Extend `HttpClientUtil.java` to capture response body and add assertions in test methods.

### Add timeout handling
Wrap the HTTP call with timeout configuration in `HttpClientUtil.java`.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Network timeout | Check internet connection |
| HTTP 403/429 errors | Some sites block automated requests; may require headers |
| "mvn not found" | Add Maven bin to system PATH |
| "java not found" | Install Java 11+ and add to PATH |

## For More Information

- See README.md for detailed documentation
- See SETUP.md for installation requirements
