from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

# import selenium exception
from selenium.common.exceptions import *
import time
import sys

# https://selenium-python.readthedocs.io/api.html


def checking_elem(i):
    if i:
        print("Element {} is found".format(i))
        print("Element has tag {}".format(i.tag_name))
        # print('Element has text {}'.format(i.text))
        print("Element has size {}, location: {}".format(i.size, i.location))
    else:
        print("Element {} is NOT found".format(i))


# Option to start Chrome maximized
options = ChromeOptions()
options.add_argument("--start-maximized")
# Starting driver with Chrome
driver = webdriver.Chrome(options=options)
# define weblink
####### weblink = 'https://jdi-testing.github.io/jdi-light/index.html'
############# weblink = 'http://localhost:8080'
weblink = "https://wirecard-sg.atlassian.net"
driver.get(weblink)


# test the current element


############# elem = driver.find_element_by_css_selector('svg.svg-icon.check')
elem = driver.find_element_by_css_selector("span.css-t5emrf")
# checking_elem(elem)
print("click element")
elem.click

# by <ifreame id="jdi-frame-site"
####### elem = driver.find_element_by_css_selector('iframe#jdi-frame-site')
# elem = driver.find_element_by_css_selector('input#frame-button')
####### checking_elem(elem)
# by <ifreame id="jdi-frame-site:nth-of-type(2))"
####### elem4 = driver.find_element_by_css_selector('iframe#jdi-frame-site:nth-of-type(2)')
# elem = driver.find_element_by_css_selector('input#frame-button')
####### checking_elem(elem4)

# by <div class="uui-main-container"
####### elem2 = driver.find_element_by_css_selector('div.uui-main-container')
# elem2 = driver.find_element_by_css_selector('input.btn-info')
####### checking_elem(elem2)
# <input class="btn btn-info" id="frame-button" type="button" value="Frame Button">
####### elem3 = driver.find_element_by_css_selector('[id^=frame]')
####### checking_elem(elem3)

input()


def continue_search():
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
