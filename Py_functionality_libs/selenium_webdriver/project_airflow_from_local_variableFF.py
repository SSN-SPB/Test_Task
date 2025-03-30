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

# The working commman line
# login_local_jenkins_parsed_args.py -user admin\
# -password 488dfeefce4a432cb5666338d04db9fc -url http://localhost:8080

# get user credentials from local environment variables
USER = os.getenv('LOGON_VARIABLE_PROJECT_AIRFLOW_LOGON')
PASSWORD = os.getenv('LOGON_VARIABLE_PROJECT_AIRFLOW_PASSWORD')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', '--website', type=str, help='Website')
    parser.add_argument('-user', '--logon', type=str, help='User')
    parser.add_argument('-password', '--user_password', type=str, help='User')
    parser.add_argument('-b', type=int, help='Second argument')
    args = vars(parser.parse_args())
    print('The following arguments are found: {}'. format(args))
    
    # logining to site without arguments
    login_to_site()




def login_to_site(url = 'http://34.93.56.109:8080/',
                  username_css = 'input#username',
                  password_css = 'input#password',
                  signin_css = 'input.btn.btn-primary.btn-block'):
    
    driver = webdriver.Firefox();
    # define weblink
    weblink = url
    driver.get(weblink)
    
    # Define locators
    user_field = driver.find_element_by_css_selector(username_css)
    passoword_field = driver.find_element_by_css_selector(password_css)
    sign_btn = driver.find_element_by_css_selector(signin_css)

    
    # Performing login
    user_field.clear()
    user_field.send_keys(USER)

    time.sleep(2)
    # Setting password
    passoword_field.clear()
    passoword_field.send_keys(PASSWORD)

    sign_btn.click()
    
    input()


if __name__ == '__main__': main()

# driver.close()
