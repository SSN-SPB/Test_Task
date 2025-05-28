#!/usr/bin/env python3

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
from datetime import datetime
from ssn import service_packages

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL_EUM = "https://admin-portal-qa2.idbs-cloud.com/hermitage-test-eu/idp-config"


def main():
    login_to_site()


def set_driver(url):
    print("url is: {}".format(url))
    # define option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    # Starting driver with Chrome
    # driver = webdriver.Chrome(options=options, /
    # executable_path=r'C:\DiskD\trainings\addedToPath\chromedriver.exe')
    selected_driver = webdriver.Chrome(options=options)
    return selected_driver


def add_data_by_id(driver, element_id, field_value):
    field_element = driver.find_element_by_id(element_id)
    field_element.click()
    field_element.send_keys(field_value)


def field_add_data(element, field_value):
    element.click()
    element.send_keys(field_value)


def login_to_site():
    driver = set_driver(URL_EUM)
    driver.get(URL_EUM)
    time.sleep(13)

    try:
        user_field = driver.find_element_by_name("username")
        password_field = driver.find_element_by_name("password")
        submit_field = driver.find_element_by_class_name("auth0-label-submit")
    except NoSuchElementException:
        print(
            "The element is not found"
            " More detail see \n{}"
            " \na bit more details: \n{}".format(sys.exc_info()[0])
        )

    field_add_data(user_field, "clds_test@idbs.com")
    field_add_data(password_field, "cLdS1234")
    submit_field.click()
    print("Time is {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    time.sleep(15)
    print("Time after sleep is {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # selecting user management tab
    # um_tab = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[text()=\"User Management\"]")))
    um_tab = driver.find_elements_by_xpath('//div[text()="User Management"]')
    print("um_tab[0] is found type {}".format(um_tab[0]))
    um_tab[0].click()
    # time.sleep(15)

    # switch to iframe
    # backup - iframe = driver.find_element_by_id('app-iframe')
    # backup - driver.switch_to.frame(iframe)
    WebDriverWait(driver, 35).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "app-iframe"))
    )
    # define and click Add User button
    add_user = driver.find_elements_by_xpath('//span[text()="Add user"]')
    print("Element add_user is found{}".format(add_user[0]))
    add_user[0].click()

    # filling the data
    add_data_by_id(driver, "user-input-fullname", "Test User")
    add_data_by_id(driver, "user-input-userID", "TestUserId")
    add_data_by_id(driver, "user-input-email", "TestUser@email.com")
    add_data_by_id(driver, "user-input-department", "AutotestDepartment")


if __name__ == "__main__":
    main()

# driver.close()
