# Setup Guide

## Prerequisites

1. **Java Development Kit (JDK)**
   - Download and install Java 11 or higher from [java.com](https://www.java.com) or [adoptopenjdk.net](https://adoptopenjdk.net)
   - Verify installation:
     ```
     java -version
     ```

2. **Apache Maven**
   - Download from [maven.apache.org](https://maven.apache.org/download.cgi)
   - Extract to your preferred location
   - Add Maven `bin` directory to your system PATH
   - Verify installation:
     ```
     mvn -version
     ```

## Running Tests

Once Maven and Java are installed, navigate to the project directory and run:

### Compile the project:
```bash
mvn clean compile
```

### Run all tests:
```bash
mvn test
```

### Run a specific test:
```bash
mvn test -Dtest=RestGetStatusCodeTest#testGoogleStatusCode
```

### Run with verbose output:
```bash
mvn test -X
```

## Expected Output

When tests run successfully, you should see:
```
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0
```

The framework runs 4 tests:
1. Google homepage status code test
2. Python.org homepage status code test  
3. Parameterized test for Google
4. Parameterized test for Python.org

## Troubleshooting

- **"mvn not found"**: Add Maven bin directory to your system PATH
- **Connection timeout**: Check your internet connection, as tests access external websites
- **Java version error**: Ensure Java 11+ is installed
