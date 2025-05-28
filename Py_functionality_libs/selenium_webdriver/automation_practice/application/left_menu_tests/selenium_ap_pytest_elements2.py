#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from application.Resources.selenium_test_ap_locators import ApLocators
import pytest
import time
from selenium.webdriver.support import expected_conditions as ec


ROOT_LINK = "https://demoqa.com/"
TESTED_PAGE_LINK = "https://demoqa.com/elements"
SITE_LOGO = "img[src='/images/Toolsqa.jpg']"
# ROOT_LINK = ApLocators.WEBLINK
# TESTED_PAGE_LINK = ApLocators.WEBLINK_TABS_ELEMENTS
# SITE_LOGO = ApLocators.LC_CSS_SITE_LOGO

WEBLINK = "https://demoqa.com/"
WEBLINK_TABS_ELEMENTS = "https://demoqa.com/elements"
# Locators
# XPATH_HEAD_LOGO = '//img[@class=\"img-responsive\"]'
LC_CSS_SITE_LOGO = "img[src='/images/Toolsqa.jpg']"


def teardown_function(function):
    print("Closing driver function")
    # driver.close()


@pytest.fixture()
def introduction(anytext="Test is started"):
    print(anytext)
    yield
    print("Test is finished")


def open_web_page(link):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    return driver


@pytest.mark.passed_test
def test_check_subpage_url():
    driver = open_web_page(ROOT_LINK)
    elements_tabs = driver.find_elements(By.CSS_SELECTOR, "div.card-body h5")
    print(elements_tabs[0].text)
    driver.execute_script("arguments[0].click();", elements_tabs[0])
    element_logo = driver.find_element(By.CSS_SELECTOR, ".main-header")
    element_logo_text = element_logo.text
    print(driver.current_url)
    navigated_page = driver.current_url
    driver.close()
    assert element_logo_text == "Elements"
    assert navigated_page == TESTED_PAGE_LINK


@pytest.mark.passed_test
def test_check_elements_tab_direct_link():
    driver = open_web_page(TESTED_PAGE_LINK)
    element_logo = driver.find_element(By.CSS_SELECTOR, ".main-header")
    element_logo_text = element_logo.text
    print(driver.current_url)
    navigated_page_url = driver.current_url
    # driver.close()
    assert element_logo_text == "Elements"
    assert navigated_page_url == TESTED_PAGE_LINK


@pytest.mark.left_menu
@pytest.mark.elements_menu
def test_check_not_collapsed_elements_submenu(introduction):
    # open direct submenu
    print("Open direct submenu")
    driver = open_web_page(TESTED_PAGE_LINK)
    # find test element
    text_box_text = driver.find_element(By.XPATH, '//li[@id="item-0"]/span')
    checked_text = text_box_text.text
    checked_text_enabled_before_collapse_menu = text_box_text.is_enabled()
    checked_text_displayed_before_collapse_menu = text_box_text.is_displayed()
    print("clicking element tab")
    elements_tabs = driver.find_elements(By.XPATH, '//div[@class="header-text"]/span')
    elements_tabs[0].click()
    checked_text_enabled_after_collapse_menu = text_box_text.is_enabled()
    # wait till buttons of sub-menu are collapsed
    driver.save_screenshot("03_before_collapsing_elements_menu.png")
    checked_text_not_displayed_after_collapse_menu = WebDriverWait(driver, 10).until(
        ec.invisibility_of_element_located((By.XPATH, '//li[@id="item-0"]/span'))
    )
    driver.save_screenshot("04_after_collapsing_elements_menu.png")
    # checked_text_displayed_after_collapse_menu = text_box_text.is_displayed()
    driver.close()
    # general checking
    assert checked_text == "Text Box"
    # checking before collapse menu
    assert checked_text_enabled_before_collapse_menu
    assert checked_text_displayed_before_collapse_menu
    # checking after collapse menu
    assert checked_text_enabled_after_collapse_menu
    assert checked_text_not_displayed_after_collapse_menu


@pytest.mark.under_developing
def test_elements_text_box(introduction):
    print("Open direct submenu")
    driver = open_web_page(TESTED_PAGE_LINK)
    print("Find the text-box subbutton")
    text_box_text = driver.find_element(By.XPATH, '//li[@id="item-0"]/span')
    checked_text = text_box_text.text
    print("Check the Left Text-Box button is enabled by default")
    assert text_box_text.is_enabled()
    print("Check the Left Text-Box button is displayed by default")
    # logger.info('Check3 the Left Text-Box button is displayed by default')
    assert (
        text_box_text.is_displayed()
    ), "Check2 the Left Text-Box button is displayed by default"
    # elements_tabs = driver.find_elements(By.XPATH, '//div[@class="header-text"]/span')
    print("Find text body element if subtabls of elements is not displayed")
    elements_textbox_not_selected_indicator = driver.find_element(
        By.XPATH, '//div[@class="container playgound-body"]/div[2]/div[2]'
    )
    # elements_textbox_not_selected_indicator = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]')
    print("Check the expecte available text before clicking Text-Box subbutton")
    elements_textbox_not_selected = elements_textbox_not_selected_indicator.text
    assert (
        elements_textbox_not_selected
        == "Please select an item from left to start practice."
    )
    print("Check the changed text before after clicking Left Text-Box button")
    text_box_text.click()
    full_name_textbox_selected = driver.find_element(
        By.XPATH, '//*[@id="userName-label"]'
    )
    assert full_name_textbox_selected.text == "Full Name"
    driver.close()
    # userEmail
