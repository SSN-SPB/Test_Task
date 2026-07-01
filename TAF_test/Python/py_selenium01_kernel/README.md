# Selenium Test Script Setup Guide

This guide provides step-by-step instructions to set up ChromeDriver and run the `py_selenium_one_script_test.py` test script.

## Prerequisites

- **Python 3.x** installed on your system
- **Google Chrome** browser installed
- **pip** (Python package manager)
- Text editor or IDE

## Step 1: Install Selenium Package

Open a terminal or command prompt in the project directory and install the Selenium library:

```bash
pip install selenium
```

## Step 2: Download ChromeDriver

1. **Find your Chrome version:**
   - Open Google Chrome
   - Click the three-dot menu (⋮) in the top-right corner
   - Select **Help** → **About Google Chrome**
   - Note the version number (e.g., 120.0.6099.129)

2. **Download ChromeDriver:**
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Download the version that matches your Chrome version
   - Or use [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/) for easier downloads

3. **Extract the ChromeDriver:**
   - Extract the downloaded ZIP file
   - You'll get a `chromedriver.exe` file (on Windows) or `chromedriver` file (on Mac/Linux)

## Step 3: Add ChromeDriver to PATH

### Option A: Add to System PATH (Recommended - Windows)

1. **Locate chromedriver.exe:**
   - Note the full path where you extracted it (e.g., `C:\chromedriver\chromedriver.exe`)

2. **Add to Environment Variables:**
   - Press `Win + X` and select **System**
   - Click **Advanced system settings**
   - Click **Environment Variables** button
   - Under "System variables", select **Path** and click **Edit**
   - Click **New** and paste the directory path (e.g., `C:\chromedriver`)
   - Click **OK** to save

3. **Verify installation:**
   - Open a new Command Prompt
   - Run: `chromedriver --version`
   - You should see the version number

### Option B: Add to System PATH (Mac/Linux)

1. **Move ChromeDriver to a standard location:**
   ```bash
   sudo mv ~/Downloads/chromedriver /usr/local/bin/
   sudo chmod +x /usr/local/bin/chromedriver
   ```

2. **Verify installation:**
   ```bash
   chromedriver --version
   ```

### Option C: Local Directory (No PATH needed)

If you prefer not to modify system PATH:
1. Place `chromedriver` in the same directory as your Python script
2. Modify the script's driver initialization:
   ```python
   driver = webdriver.Chrome("./chromedriver")  # Use relative path
   ```

## Step 4: Modify the Test Script (if needed)

Edit `py_selenium_one_script_test.py` and update the URL if required:

```python
driver.get("https://www.example.com")  # Change to your target URL
```

Also update the element ID to match your target website:

```python
EC.presence_of_element_located((By.ID, "my-element"))  # Update element ID
```

## Step 5: Run the Test Script

### From Command Line:

1. **Navigate to the script directory:**
   ```bash
   cd path/to/py_selenium01_kernel
   ```

2. **Run the script:**
   ```bash
   python py_selenium_one_script_test.py
   ```

3. **Expected output:**
   - Chrome browser opens automatically
   - Page loads at the specified URL
   - Waits for the element with ID "my-element" (up to 10 seconds)
   - Prints the element's text to the console
   - Browser closes automatically

### From an IDE:

- **Visual Studio Code:** Right-click the file → Select "Run Python File in Terminal"
- **PyCharm:** Right-click the file → Select "Run 'py_selenium_one_script_test.py'"
- **Python IDLE:** Open the file and press `F5`

## Troubleshooting

### Issue: "chromedriver not found" or "'chromedriver' is not recognized"

**Solution:**
- Verify ChromeDriver is in your PATH: `chromedriver --version`
- Restart your terminal/command prompt after adding to PATH
- Use the absolute path in the script: `webdriver.Chrome("C:\\path\\to\\chromedriver")`

### Issue: "Chrome version mismatch"

**Solution:**
- Download the ChromeDriver version that matches your Chrome browser version
- Update Chrome to the latest version or downgrade ChromeDriver accordingly

### Issue: Element not found / Timeout Error

**Solution:**
- Verify the element ID "my-element" exists on the page
- Increase the wait time: `WebDriverWait(driver, 20)` (20 seconds)
- Check if the page requires JavaScript to load the element

### Issue: Connection refused

**Solution:**
- Ensure Chrome is not already running in headless mode
- Try closing all Chrome instances and restart the script

## Additional Resources

- [Selenium Documentation](https://selenium.dev/documentation/)
- [ChromeDriver Documentation](https://chromedriver.chromium.org/)
- [WebDriver Wait Documentation](https://selenium.dev/documentation/webdriver/waits/)

## Notes

- The script uses **explicit waits** (up to 10 seconds) to ensure elements are loaded before interaction
- Chrome browser window will open during test execution
- Always ensure the target website allows automated access via Selenium
- For headless operation (no visible browser), modify the script:
  ```python
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  driver = webdriver.Chrome(options=options)
  ```
