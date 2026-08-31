# File Operations Testing Suite

## Overview

This directory contains a comprehensive test suite for Python file handling operations. The test suite verifies the functionality of `py_file_open_01_write_open.py`, which demonstrates best practices for file creation, reading, and manipulation using context managers and proper error handling.

## Files

- **py_file_open_01_write_open.py** - Enhanced module with file operations functions
  - `create_file_with_text()` - Creates a file and writes content to it
  - `read_file_content()` - Reads and returns file content
  - `main()` - Demonstrates the complete workflow

- **test_py_file_open_01_write_open.py** - Comprehensive pytest test suite (32 tests)

- **tested_file.txt** - Sample output file created during test runs

## Test Suite Description

### Test Statistics
- **Total Tests:** 32
- **Test Classes:** 7
- **Execution Time:** ~0.4 seconds
- **Coverage:** File creation, reading, error handling, edge cases, and integration

### Test Classes

#### 1. TestCreateFileWithText (7 tests)
Tests the `create_file_with_text()` function with various scenarios:

| Test | Description |
|------|-------------|
| `test_create_file_with_text_success` | Creates a file with content successfully |
| `test_create_file_with_empty_content` | Creates an empty file (0 bytes) |
| `test_create_file_with_special_characters` | Handles Unicode, emoji, and special chars (éàü 中文 🚀) |
| `test_create_file_with_multiline_content` | Creates files with multiple lines |
| `test_create_file_overwrites_existing` | Overwrites existing file content (w mode) |
| `test_create_file_in_nonexistent_directory_fails` | Raises IOError when directory doesn't exist |
| `test_create_file_with_large_content` | Handles large files (1MB of text) |

**Key Validations:**
- File is actually created
- Correct number of characters written
- File content matches input
- Error handling for invalid paths

#### 2. TestReadFileContent (6 tests)
Tests the `read_file_content()` function with various scenarios:

| Test | Description |
|------|-------------|
| `test_read_file_content_success` | Reads file content successfully |
| `test_read_empty_file` | Reads empty files without error |
| `test_read_file_with_special_characters` | Preserves Unicode and special characters |
| `test_read_nonexistent_file_raises_error` | Raises FileNotFoundError appropriately |
| `test_read_preserves_formatting` | Maintains original formatting (newlines, tabs, spaces) |
| `test_read_large_file` | Efficiently reads large files (1MB) |

**Key Validations:**
- File content matches expected output
- Formatting is preserved exactly
- Error handling for missing files
- Proper exception types raised

#### 3. TestCreateAndReadIntegration (3 tests)
Integration tests combining create and read operations:

| Test | Description |
|------|-------------|
| `test_create_then_read_returns_same_content` | Round-trip verification: write then read |
| `test_create_read_cycle_with_different_encodings_edge_case` | Tests various content types (ASCII, numbers, punctuation, mixed) |
| `test_create_read_with_constant` | Uses module constant HELLO_MESSAGE |

**Key Validations:**
- Data integrity through create/read cycle
- Encoding handled correctly throughout
- Module constants work as expected

#### 4. TestMainFunction (6 tests)
Tests the main workflow function:

| Test | Description |
|------|-------------|
| `test_main_creates_and_reads_file` | Main function executes complete workflow |
| `test_main_with_cleanup_removes_file` | File deleted when cleanup=True |
| `test_main_without_cleanup_keeps_file` | File preserved when cleanup=False |
| `test_main_displays_byte_count` | Correct output: "Bytes written: N" |
| `test_main_with_nonexistent_directory_raises_error` | Error handling for invalid paths |
| `test_main_default_parameters` | Works with default parameters |

**Key Validations:**
- Complete workflow executes
- Cleanup behavior is correct
- Output messages are accurate
- Parameter handling works properly

#### 5. TestEdgeCases (4 tests)
Tests edge cases and unusual scenarios:

| Test | Description |
|------|-------------|
| `test_file_with_only_whitespace` | Files containing only spaces, tabs, newlines |
| `test_file_with_very_long_line` | Single line with 10,000 characters |
| `test_file_with_null_like_content` | Content that looks like null values (None, NULL, null) |
| `test_file_permissions_error_on_read` | Permission denied handling (Unix only, skipped on Windows) |

**Key Validations:**
- Unusual content is handled correctly
- File size doesn't impact functionality
- Permission errors caught and reported

#### 6. TestByteCountAccuracy (3 tests)
Tests accuracy of character/byte count reporting:

| Test | Description |
|------|-------------|
| `test_ascii_byte_count` | ASCII characters (1 byte each) |
| `test_multibyte_character_byte_count` | UTF-8 multi-byte characters (Chinese: 你好) |
| `test_mixed_content_byte_count` | Mixed ASCII and Unicode (Hello世界) |

**Key Validations:**
- Character count accuracy (Python's write() returns character count)
- UTF-8 encoding handled correctly
- Mixed content counted properly

#### 7. TestFileNamingAndPaths (3 tests)
Tests various file naming conventions and path scenarios:

| Test | Description |
|------|-------------|
| `test_file_with_special_characters_in_name` | Filenames like "test_file-2024_v1.2.txt" |
| `test_file_with_dot_prefix` | Hidden files like ".hidden" |
| `test_file_in_nested_directory` | Nested directory structures |

**Key Validations:**
- Special characters in filenames work
- Hidden files handled correctly
- Nested paths created and accessed

## Requirements

### Python Version
- Python 3.11 or higher

### Dependencies
```bash
pytest>=7.2.0
```

### Optional - For Enhanced Output
```bash
pytest-allure-pytest>=2.13.2  # For Allure reporting
```

## Installation

1. **Ensure Python 3.11+ is installed:**
   ```bash
   python --version
   ```

2. **Install pytest (if not already installed):**
   ```bash
   pip install pytest
   ```

3. **Optionally install Allure for enhanced reporting:**
   ```bash
   pip install pytest-allure-pytest
   ```

## Running the Tests

### Quick Start - Run All Tests
```bash
pytest test_py_file_open_01_write_open.py -v
```

### Run Specific Test Class
```bash
# Run only file creation tests
pytest test_py_file_open_01_write_open.py::TestCreateFileWithText -v

# Run only file reading tests
pytest test_py_file_open_01_write_open.py::TestReadFileContent -v

# Run only integration tests
pytest test_py_file_open_01_write_open.py::TestCreateAndReadIntegration -v

# Run only main function tests
pytest test_py_file_open_01_write_open.py::TestMainFunction -v

# Run only edge case tests
pytest test_py_file_open_01_write_open.py::TestEdgeCases -v

# Run only byte count tests
pytest test_py_file_open_01_write_open.py::TestByteCountAccuracy -v

# Run only file path tests
pytest test_py_file_open_01_write_open.py::TestFileNamingAndPaths -v
```

### Run Single Test
```bash
pytest test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_with_text_success -v
```

### Run Tests Matching Pattern
```bash
# Run all tests with "cleanup" in the name
pytest test_py_file_open_01_write_open.py -k cleanup -v

# Run all tests with "unicode" or "special" in the name
pytest test_py_file_open_01_write_open.py -k "unicode or special" -v
```

### Run with Different Verbosity Levels
```bash
# Verbose output (show each test)
pytest test_py_file_open_01_write_open.py -v

# Very verbose output (more details)
pytest test_py_file_open_01_write_open.py -vv

# Quiet output (minimal)
pytest test_py_file_open_01_write_open.py -q
```

### Run with Detailed Tracebacks
```bash
# Short traceback (default)
pytest test_py_file_open_01_write_open.py --tb=short

# Long traceback (more context)
pytest test_py_file_open_01_write_open.py --tb=long

# Line traceback (minimal)
pytest test_py_file_open_01_write_open.py --tb=line

# No traceback
pytest test_py_file_open_01_write_open.py --tb=no
```

### Run with Coverage Report (requires pytest-cov)
```bash
# Install coverage
pip install pytest-cov

# Run with coverage
pytest test_py_file_open_01_write_open.py --cov=py_file_open_01_write_open
```

### Run with Allure Reporting
```bash
# Run and generate Allure results
pytest test_py_file_open_01_write_open.py --alluredir=allure-results

# View Allure report
allure serve allure-results
```

### Run Only Failing Tests from Last Run
```bash
pytest test_py_file_open_01_write_open.py --lf
```

### Run with Markers
```bash
# Stop on first failure
pytest test_py_file_open_01_write_open.py -x

# Stop after N failures
pytest test_py_file_open_01_write_open.py --maxfail=3
```

## Expected Output

### Sample Output - All Tests Pass
```
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
rootdir: C:\...\py_file_open
collected 32 items

test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_with_text_success PASSED [  3%]
test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_with_empty_content PASSED [  6%]
...
test_py_file_open_01_write_open.py::TestFileNamingAndPaths::test_file_in_nested_directory PASSED [100%]

======================== 31 passed, 1 skipped in 0.42s ========================
```

### Sample Output - Running Single Test Class
```
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
rootdir: C:\...\py_file_open
collected 7 items

test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_with_text_success PASSED [ 14%]
test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_with_empty_content PASSED [ 28%]
test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_with_special_characters PASSED [ 42%]
test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_with_multiline_content PASSED [ 57%]
test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_overwrites_existing PASSED [ 71%]
test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_in_nonexistent_directory_fails PASSED [ 85%]
test_py_file_open_01_write_open.py::TestCreateFileWithText::test_create_file_with_large_content PASSED [100%]

======================== 7 passed in 0.27s ==========================
```

## Running the Main Module

You can also run the module directly to see the functions in action:

```bash
# Run the main module (with automatic cleanup)
python py_file_open_01_write_open.py
```

**Expected Output:**
```
Bytes written: 11
File content: Hello world
Cleaned up: tested_file.txt
```

## Code Examples

### Example 1: Creating a File
```python
from py_file_open_01_write_open import create_file_with_text

# Create a file with text
bytes_written = create_file_with_text("Hello, World!", "myfile.txt")
print(f"Wrote {bytes_written} characters")
```

### Example 2: Reading a File
```python
from py_file_open_01_write_open import read_file_content

# Read file content
content = read_file_content("myfile.txt")
print(f"Content: {content}")
```

### Example 3: Using Main Function
```python
from py_file_open_01_write_open import main

# Run complete workflow with cleanup
main(file_path="test.txt", cleanup=True)
```

### Example 4: Error Handling
```python
from py_file_open_01_write_open import read_file_content

try:
    content = read_file_content("nonexistent.txt")
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"Error reading file: {e}")
```

## Test Features

### Temporary File Handling
All tests use `TemporaryDirectory()` to ensure:
- Tests don't interfere with the file system
- No leftover files after test completion
- Tests are isolated and repeatable

### Exception Testing
Tests verify proper exception handling:
- `FileNotFoundError` for missing files
- `IOError` for file operation failures
- Proper error messages

### UTF-8 Encoding
All tests explicitly use UTF-8 encoding to ensure:
- Special characters and emoji are handled correctly
- Cross-platform compatibility
- Proper byte count calculation for multi-byte characters

### Parametric Testing
Tests cover:
- Empty content
- Small content
- Large content (1MB)
- Special characters and Unicode
- Whitespace variations

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pytest'"
**Solution:** Install pytest
```bash
pip install pytest
```

### Issue: "Permission denied" error on file operations
**Solution:** Ensure the directory has write permissions
```bash
# On Linux/Mac
chmod 755 .

# On Windows, check file properties
```

### Issue: Tests pass locally but fail in CI/CD
**Possible causes:**
- Different Python version (ensure Python 3.11+)
- Missing dependencies (install from requirements.txt)
- Line ending differences (Git: `git config core.autocrlf true`)

### Issue: "test_file_permissions_error_on_read" is skipped
**Explanation:** This test is Unix-only and is skipped on Windows. This is expected behavior.

## Best Practices Demonstrated

1. **Context Managers** - Uses `with` statements for automatic file closing
2. **Error Handling** - Catches specific exceptions (FileNotFoundError, IOError)
3. **Type Hints** - Functions include parameter and return type annotations
4. **Documentation** - Comprehensive docstrings with Args, Returns, Raises
5. **Encoding** - Explicitly sets UTF-8 encoding for cross-platform compatibility
6. **Resource Cleanup** - Automatic cleanup of temporary files
7. **Testability** - Functions designed to be easily testable

## Key Improvements Over Original Code

| Aspect | Original | Enhanced |
|--------|----------|----------|
| Error Handling | None | Try/except with specific exceptions |
| Type Hints | None | Full type hints (parameters & returns) |
| Documentation | None | Comprehensive docstrings |
| Encoding | Default | Explicit UTF-8 |
| File Reading | Line-by-line loop | Efficient single read |
| Cleanup | Manual (not done) | Automatic option |
| Path Handling | String paths | pathlib.Path support |
| Return Value | Cursor position | Character count |

## Integration with CI/CD

### GitHub Actions
```yaml
- name: Run file tests
  run: |
    pip install pytest
    pytest Py_functionality_libs/py_fileTreating/py_file_open/test_py_file_open_01_write_open.py -v
```

### Jenkins
```groovy
stage('Test') {
    steps {
        sh 'cd Py_functionality_libs/py_fileTreating/py_file_open && pytest test_py_file_open_01_write_open.py -v'
    }
}
```

## Additional Resources

- [pytest Documentation](https://docs.pytest.org/)
- [Python File I/O Guide](https://docs.python.org/3/tutorial/inputoutput.html)
- [UTF-8 Encoding](https://docs.python.org/3/howto/unicode.html)
- [Context Managers](https://docs.python.org/3/library/stdtypes.html#context-manager-types)

## Summary

This test suite provides comprehensive coverage of file operations functionality with:
- ✅ 32 tests across 7 test classes
- ✅ 100% function coverage
- ✅ Edge case testing
- ✅ Error condition testing
- ✅ Integration testing
- ✅ Unicode/encoding testing
- ✅ Cross-platform compatibility

All tests pass successfully and provide a solid foundation for file handling operations in Python.
