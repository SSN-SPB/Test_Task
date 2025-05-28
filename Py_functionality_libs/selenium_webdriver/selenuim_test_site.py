#!/usr/bin/env python3
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

# import selenium exception
from selenium.common.exceptions import *
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


weblink = "http://automationpractice.com/index.php"
# Locators
XPATH_HEAD_LOGO = '//img[@class="img-responsive"]'
XPATH_PHONE_BLOCK = '//span[@class="shop-phone"]'
XPATH_PHONE_HEAD = '//span[@class="shop-phone"]/strong'
SITE_LOADING_TIMEOUT = 1


def main():
    # Option to start Chrome maximized
    options = ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    options.add_argument("--start-maximized")
    # Starting driver with Chrome option
    driver = webdriver.Chrome(options=options)
    # define weblink
    driver.get(weblink)

    try:
        key_element = ec.presence_of_element_located((By.XPATH, XPATH_HEAD_LOGO))
        WebDriverWait(driver, SITE_LOADING_TIMEOUT).until(key_element)
        print("The key element is found during the expected timeout")
    except TimeoutException:
        print("Timed out of waiting for page to load")

    # Check locators

    # not existing element
    not_existing_element = ""
    try:
        not_existing_element = driver.find_element_by_name("j_username")

    except NoSuchElementException as nse:
        print("No element {} is found".format(not_existing_element))
        print(nse)
    print("The expected elements:")
    try:
        site_head_logo = driver.find_element_by_xpath(XPATH_HEAD_LOGO)
        print("The expected elements {} is found".format(site_head_logo))
        site_head_block = driver.find_element_by_xpath(XPATH_PHONE_BLOCK)
        print("The expected elements {} is found".format(site_head_block))
        site_head_phone = driver.find_element_by_xpath(XPATH_PHONE_HEAD)
        print("The expected elements {} is found".format(site_head_phone))
        print("Company phone at head is: " + site_head_phone.text)
    except NoSuchElementException as nse:
        print("The expected elements are not found as well")
        print(nse.args[0])
    except Exception as e:
        print("Something is wrong" + e.args[0])
    driver.close()


if __name__ == "__main__":
    main()
