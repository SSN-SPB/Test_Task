#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
# import selenium exception
from selenium.common.exceptions import *
import time


url = 'https://blsspain-russia.com/peters/english/embassy_book_appointment.php'


def main():
    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    # Starting driver with Chrome
    driver = webdriver.Chrome(options=options)
    # define weblink
    driver.get(url)
    time.sleep(100)

    # Define locators
    try:
        # select_mission_dropbox = driver
        # .find_element_by_xpath('//*[@id="mission"]/option[1]')
        captcha_checkbox = driver.find_element_by_xpath('//*[@id="checkbox"]')
    except NoSuchElementException as nse:
        print('Not all elements are found')
        print(nse)
    captcha_checkbox.click()
    time.sleep(3)
    # driver.close()


if __name__ == '__main__':
    main()
