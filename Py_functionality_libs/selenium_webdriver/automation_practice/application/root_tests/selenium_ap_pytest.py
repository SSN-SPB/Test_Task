#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys # input interaction
from application.Resources.selenium_test_ap_locators import ApLocators
import pytest

weblink = ApLocators.WEBLINK
weblink_elements = ApLocators.weblink_elements
LC_CSS_SITE_LOGO = "img[src='/images/Toolsqa.jpg']"


def get_driver():
    # Option to start Chrome maximized
    options = ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    # Starting driver with Chrome option
    driver = webdriver.Chrome(options=options)
    return driver


def open_web_page():
    driver = get_driver()
    driver.get(weblink)
    return driver


@pytest.mark.bs_check
def test_site_logo_checking():
    checked_value = False
    driver = open_web_page()
    site_image = driver.find_element(By.CSS_SELECTOR, LC_CSS_SITE_LOGO)
    if site_image:
        checked_value = True
    driver.close()
    assert checked_value


@pytest.mark.main_elements_checking
def test_site_tab_checking_elements():
    driver = open_web_page()
    # elements_tab = driver.find_element(By.LINK_TEXT, "Elements")
    elements_tab = driver.find_element(By.CSS_SELECTOR, "div.card-body h5")
    element_text = elements_tab.text
    driver.close()
    assert element_text == 'Elements'


@pytest.mark.main_elements_checking
# @pytest.mark.under_developing
def test_navigate_to_elements():
    checked_value = False
    driver = open_web_page()
    elements_tabs = driver.find_elements(By.CSS_SELECTOR, "div.card-body h5")
    print(elements_tabs[0].text)
    # elements_tabs[0].click()
    driver.execute_script("arguments[0].click();", elements_tabs[0])
    site_image = driver.find_element(By.CSS_SELECTOR, LC_CSS_SITE_LOGO)
    element_logo = driver.find_element(By.CSS_SELECTOR, ".main-header")
    element_logo_text = element_logo.text
    if site_image:
        checked_value = True
    driver.close()
    assert checked_value
    assert element_logo_text == 'Elements'


@pytest.mark.main_elements_checking
# @pytest.mark.under_developing
def test_check_tiles_text():
    driver = open_web_page()
    tiles = driver.find_elements(By.CSS_SELECTOR, "div.card-body h5")
    expected_text_list = [
        'Elements',
        'Forms',
        'Alerts, Frame & Windows',
        'Widgets',
        'Interactions',
        'Book Store Application'
    ]
    for i in range(0, len(expected_text_list)):
        print(expected_text_list[i])
        assert tiles[i].text == expected_text_list[i]


@pytest.mark.main_elements_checking
@pytest.mark.under_developing
def test_check_subpage_url():
    driver = open_web_page()
    elements_tabs = driver.find_elements(By.CSS_SELECTOR, "div.card-body h5")
    print(elements_tabs[0].text)
    # elements_tabs[0].click()
    driver.execute_script("arguments[0].click();", elements_tabs[0])
    element_logo = driver.find_element(By.CSS_SELECTOR, ".main-header")
    element_logo_text = element_logo.text
    print(driver.current_url)
    navigated_page_url = driver.current_url
    driver.close()
    assert element_logo_text == 'Elements'
    assert navigated_page_url == weblink_elements
