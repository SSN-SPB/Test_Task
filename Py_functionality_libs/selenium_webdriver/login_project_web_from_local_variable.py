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
#### USER = os.getenv('LOCAL_VARIABLE_PROJECT_WEB_LOGON')
#### PASSWORD = os.getenv('LOCAL_VARIABLE_PROJECT_WEB_PASSWORD')
#### WEB_URL = os.getenv('LOCAL_VARIABLE_PROJECT_WEB_URL')
#### from package
USER = service_packages.get_local_variable_value("LOCAL_VARIABLE_" "PROJECT_WEB_LOGON")
PASSWORD = service_packages.get_local_variable_value(
    "LOCAL_VARIABLE_" "PROJECT_WEB_PASSWORD"
)
PROJECT_WEB_URL = service_packages.get_local_variable_value(
    "LOCAL_VARIABLE_" "PROJECT_WEB_URL"
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
        website = PROJECT_WEB_URL
    # login_to_site()
    login_to_site(username=USER, url=website, userpassword=PASSWORD)

    # login_to_site(url=args.get('website'), username=args.get('user_logon'))


def login_to_site(username, userpassword, url):

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
    time.sleep(3)
    name_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")
    login_button = driver.find_element_by_css_selector(".auth0-label-submit")

    # Performing login
    name_field.clear()
    name_field.send_keys(username)
    password_field.click()
    password_field.send_keys(userpassword)
    time.sleep(2)
    login_button.click()
    time.sleep(2)
    input()


if __name__ == "__main__":
    main()

# driver.close()
