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
USER = os.getenv('LOGON_VARIABLE_PROJECT_JIRA_LOGON')
PASSWORD = os.getenv('LOGON_VARIABLE_PROJECT_JIRA_PASSWORD')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', '--website', type=str, help='Website')
    parser.add_argument('-user', '--logon', type=str, help='User')
    parser.add_argument('-password', '--user_password', type=str, help='User')
    parser.add_argument('-b', type=int, help='Second argument')
    args = vars(parser.parse_args())
    print(args)
    print(args.get('logon'))
    #login_to_site()
    login_to_site(username = USER,
                  url = args.get('website'),
                  userpassword = PASSWORD)

    # login_to_site(url=args.get('website'), username=args.get('user_logon'))


def login_to_site(url = 'https://wirecard-sg.atlassian.net/browse/WDASLANDWH-2558',
                  username_css = 'input#username',
                  password_get_css = 'span.css-t5emrf',
                  userpassword_css = 'input.Input__InputElement-sc-1o6bj35-0.bfCuIo',
                  submit_button_id = 'Submit',
                  username = 'admin',
                  userpassword = '488dfeefce4a432cb5666338d04db9fc',
                  login_button_id = 'span.Log.in'):


    print('userpassword: {}'.format(userpassword))
                  
                  
    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    # Starting driver with Chrome
    driver = webdriver.Chrome(options=options);
    # Starting driver with Firefox
    # driver = webdriver.Firefox();
    # define weblink
    weblink = url
    driver.get(weblink)
    
    # Define locators
    elem = driver.find_element_by_css_selector(username_css)
    name_field = driver.find_element_by_css_selector(username_css)
    password_get = driver.find_element_by_css_selector(password_get_css)
    
    
    if elem:
        print('Element is found')
    else:
        print('Element is not found')
    time.sleep(3)
    try:
        elem.click()
    except ElementNotInteractableException:
        print('The element is not clickable'
              ' More detail see \n{}'
              ' \na bit more details: \n{}'
              ''.format(sys.exc_info()[0], sys.exc_info()[1]))
    except:
        print('The Unkown error:'
              ' More detail see \n{}'
              ' \na bit more details: \n{}'
              ''.format(sys.exc_info()[0], sys.exc_info()[1]))

    # Performing login
    name_field.clear()
    name_field.send_keys(username)
    password_get.click()
    
    # password_field = driver.find_element_by_id('password')
    # password_field = driver.find_element_by_css_selector('inbox#password.Input__InputElement-sc-1o6bj35-0.bfCuIo')
    #password_field = driver.find_element_by_css_selector('input#password')
    # password_field = driver.find_element_by_css_selector('span.sc-Rmtcm.eVqUIr')
    # password_field = driver.find_element_by_css_selector('div.Content-ve26fj-1.hqyPWx')
    css_field= 'input#password'
    print('css_field is : {}'.format(css_field))
    password_field = driver.find_element_by_css_selector(css_field)
    if password_field:
        print('Element2 is found')
    else:
        print('Element is not found')
    # try:
    password_field.click()
    # except ElementNotInteractableException:
    #    print('The element is not clickable'
    #          ' More detail see \n{}'
    #          ' \na bit more details: \n{}'
    #          ''.format(sys.exc_info()[0], sys.exc_info()[1]))
    # except:
    #    print('The Unkown error:'
    #           ' More detail see \n{}'
    #           ' \na bit more details: \n{}'
    #          ''.format(sys.exc_info()[0], sys.exc_info()[1]))
    password_field.send_keys('zzz')
    #password_field.send_keys(userpassword)
    login_button = driver.find_element_by_name(login_button_id)
    login_button.click()
    input()

def backUp_function():
    
    time.sleep(2)
    password_get.click()
    password_field.click()
    password_field.send_keys(userpassword)
    time.sleep(3)
    # keep_logged_checkbox.click()
    time.sleep(2)
    login_button.click()
    time.sleep(2)
    
    logout_button = driver.find_element_by_css_selector(logout_button_id)
    if logout_button:
        print('Login is successful')
    else:
        print('Login is failed')
    time.sleep(3)
    input()

if __name__ == '__main__': main()

# driver.close()
