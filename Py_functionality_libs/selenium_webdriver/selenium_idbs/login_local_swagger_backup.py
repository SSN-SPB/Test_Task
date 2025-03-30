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
from ssn import service_packages


# The working commman line
# login_local_jenkins_parsed_args.py -user admin\
# -password 488dfeefce4a432cb5666338d04db9fc -url http://localhost:8080

# get user credentials from local environment variables
# directly
# USER = os.getenv('LOGON_VARIABLE_LOCAL_JENKINS_LOGON')
# PASSWORD = os.getenv('LOGON_VARIABLE_LOCAL_JENKINS_PASSWORD')
# from package
USER = service_packages.get_local_variable_value('LOGON_VARIABLE'
                                                 '_LOCAL_JENKINS_LOGON')
PASSWORD = service_packages.get_local_variable_value('LOGON_VARIABLE_'
                                                     'LOCAL_JENKINS_PASSWORD')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', '--website', type=str, help='Website')
    parser.add_argument('-user', '--logon', type=str, help='User')
    parser.add_argument('-password', '--user_password', type=str, help='User')
    parser.add_argument('-b', type=int, help='Second argument')
    args = vars(parser.parse_args())
    print(args)
    if args.get('website'):
        website = args.get('website')
    else:
        website = 'http://localhost:8091'
    # login_to_site()
    login_to_site(website)

    # login_to_site(url=args.get('website'), username=args.get('user_logon'))


def login_to_site(url):
    print('url is: {}'.format(url))
    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    # Starting driver with Chrome
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # Define locators
    menu_file = driver.find_element_by_css_selector('span.menu-item')
    menu_file.click()


if __name__ == '__main__':
    main()
    input()


# driver.close()
