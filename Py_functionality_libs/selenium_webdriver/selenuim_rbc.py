#!/usr/bin/env python3
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

# import selenium exception
from selenium.common.exceptions import *
import time


weblink = "http://rbc.ru"
# Locators
USD_RATE_BLOCK = "a[title^='USD']"
XPATH_USD_RATE_TEXT = (
    "//a[contains(@title,'USD')]/span[@class=\"topline__indicators__diff\"]"
)


def main():
    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    # Starting driver with Chrome
    driver = webdriver.Chrome(options=options)
    # define weblink
    driver.get(weblink)
    time.sleep(10)

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
        usd_rate_block = driver.find_element_by_css_selector(USD_RATE_BLOCK)
        print("The expected elements {} is found".format(usd_rate_block))
        # usd_rate_text = driver.find_element_by_css_selector(USD_RATE_TEXT)
        usd_rate_texts = driver.find_element_by_xpath(XPATH_USD_RATE_TEXT)
        print("The expected elements {} are found".format(usd_rate_texts))
        for x in list(usd_rate_texts):
            print("Current USD rate is: " + x.text)
        print("The expected elements are found")
    except NoSuchElementException as nse:
        print("The expected elements are not found as well")
        print(nse)
    time.sleep(3)
    driver.close()


if __name__ == "__main__":
    main()
