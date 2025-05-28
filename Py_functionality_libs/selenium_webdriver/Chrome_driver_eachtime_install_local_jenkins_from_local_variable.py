#!/usr/bin/env python3

####### For installing the zip with chromedriver each time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

# import selenium exception
from selenium.common.exceptions import *


def main():
    ####### For installing the zip with chromedriver each time
    url = "https://mail.ru/"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)


if __name__ == "__main__":
    main()

# driver.close()
