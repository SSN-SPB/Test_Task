#!/usr/bin/env python3

####### from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
# import selenium exception
from selenium.common.exceptions import *
import os
import sys
import time



# The working command line
# login_local_jenkins_parsed_args.py -user admin\Sergei_Smirnov6
# -password 488dfeefce4a432cb5666338d04db9fc/paysLip$3112 -url http://localhost:8080

# get user credentials from local environment variables
#### directly
USER = os.getenv('LOCAL_JENKINS_LOGON')
PASSWORD = os.getenv('LOCAL_JENKINS_PASSWORD')
CHECK_B0X_NAME = 'remember_me'
WEB_INTERFACE = 'http://localhost:8080'


def main():
    login_to_site(username = USER,
                  url = WEB_INTERFACE,
                  userpassword = PASSWORD)


def login_to_site(username,
                  userpassword,
                  url,
                  checked_element = 'j_username',
                  username_id = 'j_username',
                  userpassword_id = 'j_password',
                  submit_button_name = 'Submit',
                  logout_button_id = 'xxx'):                 
    print('url is: {}'.format(url)) 
    # Option to start Chrome maximized
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    # Starting driver with Chrome
    # driver = webdriver.Chrome(options=options,executable_path=r'C:\DiskD\trainings\addedToPath\chromedriver.exe')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # Define locators
    name_field = driver.find_element(By.NAME, username_id)
    password_field = driver.find_element(By.NAME, userpassword_id)
    login_button = driver.find_element(By.NAME, submit_button_name)
    keep_logged_checkbox = driver.find_element(By.NAME, CHECK_B0X_NAME)

    # Performing login
    name_field.clear()
    name_field.send_keys(username)
    password_field.click()
    password_field.send_keys(userpassword)
    # keep_logged_checkbox.click()
    driver.execute_script("arguments[0].click();", keep_logged_checkbox)
    login_button.click()
    x = input("If you would you like to complete press any button. ")
    
    
if __name__ == '__main__': main()

# driver.close()
