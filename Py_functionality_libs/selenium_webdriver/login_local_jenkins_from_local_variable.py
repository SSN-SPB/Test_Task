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


# The working commman line
# login_local_jenkins_parsed_args.py -user admin\
# -password 488dfeefce4a432cb5666338d04db9fc -url http://localhost:8080

# get user credentials from local environment variables
#### directly
#### USER = os.getenv('LOGON_VARIABLE_LOCAL_JENKINS_LOGON')
#### PASSWORD = os.getenv('LOGON_VARIABLE_LOCAL_JENKINS_PASSWORD')
#### from package
USER = service_packages.get_local_variable_value(
    "LOGON_VARIABLE" "_LOCAL_JENKINS_LOGON"
)
PASSWORD = service_packages.get_local_variable_value(
    "LOGON_VARIABLE_" "LOCAL_JENKINS_PASSWORD"
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", "--website", type=str, help="Website")
    parser.add_argument("-user", "--logon", type=str, help="User")
    parser.add_argument("-password", "--user_password", type=str, help="User")
    parser.add_argument("-b", type=int, help="Second argument")
    args = vars(parser.parse_args())
    print(args)
    print(USER)
    if args.get("website"):
        website = args.get("website")
    else:
        website = "http://localhost:8080"
    # login_to_site()
    login_to_site(username=USER, url=website, userpassword=PASSWORD)

    # login_to_site(url=args.get('website'), username=args.get('user_logon'))


def login_to_site(
    username,
    userpassword,
    url,
    checked_element="j_username",
    username_id="j_username",
    userpassword_id="j_password",
    submit_button_id="Submit",
    logout_button_id="xxx",
):

    print("username is: {}".format(username))
    print("password is: {}".format(userpassword))
    print("url is: {}".format(url))
    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    # Starting driver with Chrome
    # driver = webdriver.Chrome(options=options,executable_path=r'C:\DiskD\trainings\addedToPath\chromedriver.exe')
    driver = webdriver.Chrome(options=options)
    ####### For installing the zip with chromedriver each time
    ####### driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    # Define locators
    elem = driver.find_element_by_name(username_id)
    name_field = driver.find_element_by_name(username_id)
    password_field = driver.find_element_by_name(userpassword_id)
    login_button = driver.find_element_by_name(submit_button_id)
    keep_logged_checkbox = driver.find_element_by_css_selector("svg.svg-icon.check")

    if elem:
        print("Element is found")
    else:
        print("Element is not found")
    time.sleep(3)
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

    # Performing login
    name_field.clear()
    name_field.send_keys(username)
    time.sleep(3)
    password_field.click()
    password_field.send_keys(userpassword)
    keep_logged_checkbox.click()
    time.sleep(2)
    login_button.click()
    time.sleep(2)

    logout_button = driver.find_element_by_css_selector(logout_button_id)
    if logout_button:
        print("Login is successful")
    else:
        print("Login is failed")
    time.sleep(3)
    input()


if __name__ == "__main__":
    main()

# driver.close()
