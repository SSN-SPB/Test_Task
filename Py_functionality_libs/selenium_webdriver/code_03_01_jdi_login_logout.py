from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

# import selenium exception
from selenium.common.exceptions import *
import time
import sys

# Option to start Chrome maximized
options = ChromeOptions()
options.add_argument("--start-maximized")
# Starting driver with Chrome
driver = webdriver.Chrome(options=options)
# define weblink
weblink = "https://jdi-testing.github.io/jdi-light/index.html"
driver.get(weblink)


elem = driver.find_element_by_id("user-icon")
name_field = driver.find_element_by_id("name")
password_field = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("login-button")
# logged_user = driver.find_element_by_id('user-name')
# logout_button = driver.find_element_by_class_name('fa fa-sign-out')
# logged_user2 = driver.find_element_by_id('user-name2')

if elem:
    print("Element is found")
else:
    print("Element is not found")
time.sleep(7)
try:
    elem.click()
except ElementNotInteractableException:
    print(
        "The element is not clickable"
        " More detail see \n{}"
        " \na bit more details: \n{}"
        "".format(sys.exc_info()[0], sys.exc_info()[1])
    )
except:
    print(
        "The Unkown error:"
        " More detail see \n{}"
        " \na bit more details: \n{}"
        "".format(sys.exc_info()[0], sys.exc_info()[1])
    )

name_field.click()
name_field.send_keys("Roman2")
time.sleep(5)
# testing the clearing
name_field.clear()
name_field.send_keys("Roman")
time.sleep(3)
password_field.click()
password_field.send_keys("Jdi1234")
time.sleep(3)
login_button.click()
time.sleep(3)

logout_button = driver.find_element_by_css_selector(".fa-sign-out")
if logout_button:
    print("Login is successful")
else:
    print("Login is failed")
time.sleep(3)

driver.close()
