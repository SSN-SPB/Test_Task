#!/usr/bin/env python3

####### For installing the zip with chromedriver each time
####### from selenium import webdriver
####### from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

# import selenium exception
from selenium.common.exceptions import *
import os
import sys
import argparse
import time
import ssn
from ssn import service_packages

URL_EUM = "https://admin-portal-qa2.idbs-cloud.com/hermitage-test-eu/user-admin"


def main():
    login_to_site()


def login_to_site():

    print("url is: {}".format(URL_EUM))
    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    # Starting driver with Chrome
    # driver = webdriver.Chrome(options=options,executable_path=r'C:\DiskD\trainings\addedToPath\chromedriver.exe')
    driver = webdriver.Chrome(options=options)
    ####### For installing the zip with chromedriver each time
    ####### driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL_EUM)
    time.sleep(13)

    # Define locators
    # user_field = driver.find_element_by_name('username')
    # user_field = find_elements_by_xpath('//*[@id="back_filler"]/*/input')
    # password_field = driver.find_element_by_name('password')
    # add_user = driver.find_element_by_css_selector('span#Add user')

    try:
        user_field = driver.find_element_by_name("username")
        password_field = driver.find_element_by_name("password")
        submit_field = driver.find_element_by_class_name("auth0-label-submit")
    except NoSuchElementException:
        print(
            "The element is not found"
            " More detail see \n{}"
            " \na bit more details: \n{}"
            "".format(sys.exc_info()[0], sys.exc_info()[1])
        )

    user_field.click()
    user_field.send_keys("clds_test@idbs.com")
    password_field.click()
    password_field.send_keys("cLdS1234")
    submit_field.click()
    time.sleep(13)
    add_user = driver.find_element_by_css_selector(
        'span.className[attrName="Add user"]'
    )
    add_user.click()


if __name__ == "__main__":
    main()

# driver.close()
