from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome driver (make sure ChromeDriver is installed and in PATH)
# The r prefix creates a raw string, so Windows backslashes
# are handled correctly without ┃needing to escape them.
driver = webdriver.Chrome(r"C:\Data\added2Path\chromedriver.exe")

try:
    # Open page
    driver.get("https://www.schultetable.com/")
    # driver.get("https://www.example.com")

    # Explicit wait for element with ID "my-element" (up to 10 seconds)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".border.bg-primary\\/80.text-base-100"))
    )

    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "my-element"))
    # )
    #
    # Print element text
    print(element.text)

finally:
    # Close browser
    driver.quit()
