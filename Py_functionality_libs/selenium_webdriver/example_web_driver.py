import time
from selenium import webdriver

# https://chromedriver.chromium.org/getting-started
# downloads: https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.69/

driver = webdriver.Chrome(
    'c:\\DiskD\\trainings\\addedToPath\\chromedriver_v81.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()
