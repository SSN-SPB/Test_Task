#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import *
import os
import sys
import argparse
import time

IMPORT_FILE_MENU = '//*[@id="swagger-editor"]/div/div[1]/div/div/'\
                    'div/div[1]/div/ul/li[2]/button'


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
    # menu_file_import_file = driver.find_element_by_name('Import file')
    menu_file_import_file = driver.find_element_by_xpath(IMPORT_FILE_MENU)
    menu_file_import_file.click()


if __name__ == '__main__':
    main()
    input()
