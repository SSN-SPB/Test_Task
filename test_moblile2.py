import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Helper to save screenshots ---
def save_screenshot(driver, name="screenshot"):
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")


@pytest.fixture
def driver():
    options = AppiumOptions()

    # Mandatory
    options.set_capability("browserName", "Safari")
    options.set_capability("platformName", "iOS")

    # BrowserStack specific
    options.set_capability("bstack:options", {
        "deviceName": "iPhone 14",
        "osVersion": "16",
        "realMobile": True
    })

    # Replace with your BrowserStack credentials
    driver = webdriver.Remote(
        command_executor="https://sergeismirnov_ntl4h6:i7UzS3m9WzKrfzUDM5ka@hub-cloud.browserstack.com/wd/hub",
        # command_executor="https://YOUR_USERNAME:YOUR_ACCESS_KEY@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    yield driver
    driver.quit()


def test_google_search(driver):
    """
    Detailed Test:
    1. Open Google
    2. Search for 'Appium Python'
    3. Verify the first result contains 'Appium'
    4. Take screenshots at key steps
    """
    # Step 1: Open Google
    driver.get("https://www.google.com")
    save_screenshot(driver, "google_homepage")
    read_more = driver.find_element(By.XPATH, "//*[contains(text(),'Read more')]")
    assert read_more
    read_more.click()
    read_more.click()
    read_more.click()
    read_more.click()
    read_more.click()
    # accept_all = driver.find_element(By.XPATH, "//*[contains(text(),'Accept all')]")
    # while not accept_all.is_enabled():
    #     read_more.click()
    save_screenshot(driver, "after_read_more")
    accept_all = driver.find_element(By.XPATH, "//*[contains(text(),'Accept all')]")
    assert accept_all.is_enabled()
    accept_all.click()
    save_screenshot(driver, "after_accept_all")
    # Wait for page reload and search box
    wait = WebDriverWait(driver, 15)
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    save_screenshot(driver, "search_box_visible")

    # Step 2: Find search box and enter query
    # search_box = driver.find_element("name", "q")
    search_box.send_keys("Appium Python")
    save_screenshot(driver, "entered_query")
    search_box.submit()

    # Step 3: Wait for results
    time.sleep(3)  # Simple wait; in production use WebDriverWait

    # Step 4: Verify results contain 'Appium'
    results = driver.find_elements("css selector", "h3")
    assert any("Appium" in r.text for r in results), "No result contains 'Appium'"
    # assert any("Before You" in r.text for r in results), "No result contains 'Before You'"
    save_screenshot(driver, "search_results")
# ✅ What this code does:
# Opens Google on Safari (iPhone 14, iOS 16) via BrowserStack.
# Performs a search for “Appium Python”.
# Verifies that at least one result contains the word “Appium”.
# Takes screenshots at three steps:
# Homepage
# After entering query
# After results load
# All screenshots are stored in a folder called screenshots with timestamps.
# ⚡ Tips for Production:
# Replace time.sleep() with WebDriverWait for more reliable waits.
# You can name screenshots dynamically by test step or test name.
# Use pytest hooks to capture screenshots automatically on test failures.
# If you want, I can upgrade this further into a full mini framework where:
# Tests are organized in a tests folder
# Pages use Page Object Model (POM)
# Screenshots are captured automatically on failure
# Supports parallel runs on multiple iPhones
# This would be a professional-level setup you could reuse for real QA projects.
# Do you want me to do that next?