#!/usr/bin/env python3


from selenium import webdriver
from selenium.webdriver import ChromeOptions

# import selenium exception
from selenium.common.exceptions import ElementNotInteractableException
import os
import sys
import argparse

# The working commman line
# login_local_jenkins_parsed_args.py -user admin\
# -password 488dfeefce4a432cb5666338d04db9fc -url http://localhost:8080

# get user credentials from local environment variables
USER = os.getenv("LOCAL_JENKINS_LOGON")
PASS = os.getenv("LOCAL_JENKINS_PASSWORD")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", "--website", type=str, help="Website")
    parser.add_argument("-user", "--logon", type=str, help="User")
    parser.add_argument("-password", "--user_password", type=str, help="User")
    parser.add_argument("-b", type=int, help="Second argument")
    args = vars(parser.parse_args())
    print(args)
    print(args.get("logon"))
    # login_to_site()
    login_to_site(username=USER, url=args.get("website"), userpassword=PASS)


def login_to_site(
    url="http://localhost:8080",
    checked_element="j_username",
    username_id="j_username",
    userpassword_id="j_password",
    submit_button_id="Submit",
    username="admin",
    userpassword="488dfeefce4a432cb5666338d04db9fc",
    logout_button_id="xxx",
):

    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    # Starting driver with Chrome
    driver = webdriver.Chrome(options=options)
    # define weblink
    weblink = url
    driver.get(weblink)

    # Define locators
    elem = driver.find_element_by_name(checked_element)
    name_field = driver.find_element_by_name(username_id)
    password_field = driver.find_element_by_name(userpassword_id)
    login_button = driver.find_element_by_name(submit_button_id)

    if elem:
        print("Element is found")
    else:
        print("Element is not found")
    try:
        elem.click()
    except ElementNotInteractableException:
        print(
            "The element is not clickable"
            " More detail see \n{}"
            " \na bit more details: \n{}"
            "".format(sys.exc_info()[0], sys.exc_info()[1])
        )
    # except Except:
    #     print(
    #         "The Unkown error:"
    #         " More detail see \n{}"
    #         " \na bit more details: \n{}"
    #         "".format(sys.exc_info()[0], sys.exc_info()[1])
    #     )

    # Performing login
    name_field.clear()
    name_field.send_keys(username)
    password_field.click()
    password_field.send_keys(userpassword)
    login_button.click()
    logout_button = driver.find_element_by_css_selector(logout_button_id)
    if logout_button:
        print("Login is successful")
    else:
        print("Login is failed")


if __name__ == "__main__":
    main()
