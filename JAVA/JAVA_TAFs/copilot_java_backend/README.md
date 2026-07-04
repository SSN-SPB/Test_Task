# REST API Test Automation Framework

A simple Java-based test automation framework for testing REST API endpoints with focus on HTTP response validation.

## Overview

This framework provides:
- HTTP GET request testing capabilities
- Response code validation
- Parameterized tests for testing multiple endpoints
- Maven-based project structure

## Prerequisites

- Java 11 or higher
- Maven 3.6.0 or higher

## Project Structure

```
├── pom.xml                                    # Maven configuration
├── src/
│   ├── main/java/com/restapi/test/
│   │   └── client/
│   │       └── HttpClientUtil.java           # HTTP client utility class
│   └── test/java/com/restapi/test/
│       └── RestGetStatusCodeTest.java        # Test cases
│       └── RestPostStatusCodeTest.java        # Test cases
└── README.md
```

## Building the Project

To compile the project:

```bash
mvn clean compile
```

## Running Tests

### Run all tests:
```bash
mvn test
```

### Run a specific test class:
```bash
mvn test -Dtest=RestGetStatusCodeTest
```

### Run a specific test method:
```bash
mvn test -Dtest=RestGetStatusCodeTest#testGoogleStatusCode
```

### Run tests with verbose output:
```bash
mvn test -X
```

## Test Coverage

The framework includes tests for:

1. **Google Homepage** - Validates https://www.google.com returns HTTP 200
2. **Python.org Homepage** - Validates https://www.python.org returns HTTP 200
3. **Parameterized Tests** - Runs the same test logic across multiple URLs

## Adding New Tests

### Example: Adding a new endpoint test

1. Open `src/test/java/com/restapi/test/RestGetStatusCodeTest.java`
2. Add a new test method:

```java
@Test
@DisplayName("New website should return 200 status code")
public void testNewWebsiteStatusCode() throws Exception {
    String url = "https://www.example.com";
    HttpClientUtil.HttpResponse response = HttpClientUtil.sendGetRequest(url);
    assertEquals(EXPECTED_STATUS_CODE, response.getStatusCode(),
            "New website should return HTTP 200 status code");
}
```

3. Or add to the `@ValueSource` in the parameterized test for multiple URLs

## Dependencies

- **JUnit 5** - Testing framework
- **Apache HttpClient 5** - HTTP client for making requests
- **SLF4J** - Logging framework

## Notes

- The framework handles HTTPS requests automatically
- Response body is captured but not validated in current tests
- Tests may take a few seconds due to network latency
