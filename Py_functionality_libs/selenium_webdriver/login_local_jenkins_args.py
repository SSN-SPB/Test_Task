#!/usr/bin/env python3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
# import selenium exception
from selenium.common.exceptions import *
import time
import sys

def main():
    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    # Starting driver with Chrome
    driver = webdriver.Chrome(options=options);
    # define weblink
    weblink = 'http://localhost:8080'
    driver.get(weblink)
    
    # Define locators
    elem = driver.find_element_by_name('j_username')
    name_field = driver.find_element_by_name('j_username')
    password_field = driver.find_element_by_name('j_password')
    login_button = driver.find_element_by_name('Submit')
    
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
    name_field.send_keys('admin')
    time.sleep(3)
    password_field.click()
    password_field.send_keys('488dfeefce4a432cb5666338d04db9fc')
    time.sleep(3)
    login_button.click()
    time.sleep(3)
    
    logout_button = driver.find_element_by_css_selector('.fa-sign-out')
    if logout_button:
        print('Login is successful')
    else:
        print('Login is failed')
    time.sleep(3)

if __name__ == '__main__': main()

#driver.close()
