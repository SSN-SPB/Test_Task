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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", "--website", type=str, help="Website")
    parser.add_argument("-user", "--logon", type=str, help="User")
    # parser.add_argument('-password', '--user_password', type=str, help='User')
    # parser.add_argument('-b', type=int, help='Second argument')
    args = vars(parser.parse_args())
    if args.get("website"):
        website = args.get("website")
    else:
        website = "http://workspace.refinitiv.com/web"
    if args.get("logon"):
        userlog = args.get("logon")
    else:
        userlog = "testio.waa20@refinitiv.com"

    # login_to_site()
    login_to_site(url=website, username=userlog)

    # login_to_site(url=args.get('website'), username=args.get('user_logon'))


def user_handling(driver_user):
    confirm_elem = driver_user.find_element_by_css_selector(
        "layout-button#accountButton"
    )
    confirm_elem.click()


def login_to_site(
    url="http://localhost:8080",
    checked_element="j_username",
    username_id="j_username",
    userpassword_id="j_password",
    submit_button_id="Submit",
    username="testio.waa20@refinitiv.comzzz",
    userpassword="Secret12",
    logout_button_id="xxx",
):

    print("username is: {}".format(username))
    print("password is: {}".format(userpassword))
    print("url is: {}".format(url))
    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    # Starting driver with Chrome
    driver = webdriver.Chrome(
        options=options,
        executable_path=r"C:\DiskD\trainings\addedToPath\chromedriver.exe",
    )
    ####### For installing the zip with chromedriver each time
    ####### driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    login_name = driver.find_element_by_css_selector("input#AAA-AS-SI1-SE003")
    login_name.clear()
    login_name.send_keys(username)

    login_pass = driver.find_element_by_css_selector("input#AAA-AS-SI1-SE006")
    login_pass.clear()
    login_pass.send_keys(userpassword)
    confirm_but = driver.find_element_by_css_selector("div#AAA-AS-SI1-SE014")
    confirm_but.click()

    # login to chart
    chart_menu = driver.find_element_by_css_selector(
        "layout-button.navButton:nth-of-type(4)"
    )
    chart_menu.click()


def cont():
    # Init action
    # <button class="btn btn-primary js-cookies-accept-all">Prihvatam</button>
    confirm_elem = driver.find_element_by_css_selector(
        "button.btn.btn-primary" ".js-cookies-accept-all"
    )
    confirm_elem.click()

    # switch to register page
    # <span class="action-text welcome-header">
    login_elem = driver.find_element_by_css_selector("span.action-text.welcome-header")
    login_elem.click()

    # Fill data at register page
    # login:
    # <input id="emailOrPhoneNumber" name="j_username"
    # class="form-control field-error" type="text" value="">
    login_name = driver.find_element_by_css_selector("input#AAA-AS-SI1-SE003")
    login_name.clear()
    login_name.send_keys("sergeisr0715001@yopmail.com")

    # password
    # <input id="password-current" name="j_password"
    # class="js-password-reveal-input js-password-input
    # form-control field-error" type="password" value="">
    login_pass = driver.find_element_by_css_selector("input#password-current")
    login_pass.clear()
    login_pass.send_keys("Sergeisr0715001@")

    # Confirm button
    confirm_but = driver.find_element_by_css_selector(
        "input.col-xs-60.col-sm-20.btn.btn-primary.js-login-submit"
    )
    # <input type="submit" class=
    # "col-xs-60 col-sm-20 btn btn-primary js-login-submit"
    # value="Prijavite se">
    confirm_but.click()


# not comleted and an issue with periodically not available element
def register():
    # register button
    # <input type="button" class="btn btn-default" value="Register">
    register_elem = driver.find_element_by_css_selector("input.btn.btn-default")
    register_elem.click()

    # fill registration form
    # <input id="contactFirstName" name="firstName" placeholder="Ime" type="text" value="">
    name_elem = driver.find_element_by_css_selector("input#contactFirstName")
    name_elem.clear()
    name_elem.send_keys("SergeiS")
    lname_elem = driver.find_element_by_css_selector("input#contactLastName")
    lname_elem.clear()
    lname_elem.send_keys("Smirnov")


def continue_test():
    name_field.clear()
    name_field.send_keys(username)
    time.sleep(3)
    if logout_button:
        print("Login is successful")
    else:
        print("Login is failed")
    time.sleep(3)
    input()


if __name__ == "__main__":
    main()

# driver.close()
