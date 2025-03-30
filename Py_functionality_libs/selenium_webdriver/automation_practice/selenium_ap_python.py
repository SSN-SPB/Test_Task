#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import *
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from application.Resources.selenium_test_ap_locators import ApLocators
from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.common.action_chains import ActionChains

LS_XP_CART_POPUP = "//*/div[@class=\"shopping_cart\"]/a"
TXT_CART_POPUP = "View my shopping cart"
XP_SELECTED_PRICE = "//*/select[@id=\"selectProductSort\"]/.."
XP_PRICE_SELECTION_TEXT = "Price: Highest first"
XP_PRICE_DROPDOWN = "//*[@id=\"selectProductSort\"]"
XP_FIRST_SEARCH_ELEMENT = "(//div[@class=\"right-block\"]//a[@class=\"product-name\"])[1]"

weblink = ApLocators.WEBLINK
# Service variables
SITE_LOADING_TIMEOUT = ApLocators.SITE_LOADING_TIMEOUT
# Locators
LC_XP_HEAD_LOGO = ApLocators.XPATH_HEAD_LOGO
LC_XP_PHONE_BLOCK = ApLocators.XPATH_PHONE_BLOCK
LC_XP_PHONE_HEAD = ApLocators.XPATH_PHONE_HEAD
LC_XP_BT_SEARCH_SUBMIT = ApLocators.XPATH_MAIN_SUBMIT
LC_XP_SEARCH_TITLE = ApLocators.XPATH_SEARCH_TITLE
LC_XP_SEARCH_SORT_BY_DD = ApLocators.XPATH_SEARCH_SORT_BY_DD
LC_CLSS_MAIN_TEXT_SEARCH_BOX = ApLocators.ClS_MAIN_TEXT_SEARCH
LC_ID_MAIN_TEXT_SEARCH_BOX = ApLocators.ID_MAIN_TEXT_SEARCH
LC_XP_NOT_FOUND_SEARCH_TXT = ApLocators.XPATH_NOT_FOUND_TEXT
# Text variables
TXT_WRONG_SEARCH_TEXT = 'WrongSearchText'
TXT_VALID_SEARCH_TEXT = 'dresses'
TXT_NOT_FOUND_RESPONSE = 'No results were found for your search \"'
MAIN_PHONE_NUMBER = '0123-456-789'


def get_driver():
    # Option to start Chrome maximized
    options = ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    # Starting driver with Chrome option
    driver = webdriver.Chrome(options=options)
    return driver


def check_site_availability(driver):
    try:
        key_element = ec.presence_of_element_located(
            (By.XPATH, LC_XP_HEAD_LOGO))
        WebDriverWait(driver, SITE_LOADING_TIMEOUT).until(key_element)
        print('The site availability test PASSES')
    except TimeoutException:
        print('Timed out of waiting for page to load')
        print('The site availability test FAILS')
    except Exception as e:
        print('General exception: ' + e.args[0])
        print('General exception details: ' + str(e.__traceback__))


def check_text_search(driver):
    try:
        text_search = driver.find_element_by_id(LC_ID_MAIN_TEXT_SEARCH_BOX)
        print('The text_search presence test PASSES')
        print('initial type of textbox is {}'.format(type(text_search)))
        text_search.clear()
        text_search.send_keys('y2y2y2')
        return text_search
    except NoSuchElementException as nse:
        print('The expected element '
              '{} is not found as well'.format('Text search'))
        print(nse.args[0])
    except Exception as e:
        print('General exception: ' + e.args[0])
        print('General exception details: ' + str(e.__traceback__))


def check_text_search_submit(driver):
    try:
        text_search = driver.find_element_by_id(LC_ID_MAIN_TEXT_SEARCH_BOX)
        submit_button = driver.find_element_by_xpath(LC_XP_BT_SEARCH_SUBMIT)
        text_search.clear()
        text_search.send_keys(TXT_WRONG_SEARCH_TEXT)
        submit_button.click()
        # expected_text = 'No results were found for your search \"y5y5y5\"'
        expected_text = TXT_NOT_FOUND_RESPONSE + TXT_WRONG_SEARCH_TEXT + '\"'
        not_found = driver.find_element(By.XPATH,
                                        LC_XP_NOT_FOUND_SEARCH_TXT)
        # not_found4 = driver.find_element(By.PARTIAL_LINK_TEXT, expected_text)
        # not_found5 = driver.find_element(By.LINK_TEXT, 'No results wer')
        print('not found text is {} '.format(not_found.text))
        print('the horizontal position is {} '.format(not_found.location['x']))
        print('not found search text is found')
        # print(driver.page_source)
        if expected_text in driver.page_source:
            print('The test text submit search PASSES')
        else:
            print('The test text submit search FAILS')
        time.sleep(12)
    except NoSuchElementException as nse:
        print('The expected element '
              '{} is not found as well'.format('Text search'))
        print(nse.args[0])
    except Exception as e:
        print('General exception: ' + e.args[0])
        print('General exception details: ' + str(e.__traceback__))


def open_web_page():
    driver = get_driver()
    driver.get(weblink)
    return driver


@pytest.mark.bs_check
def test_site_checking():
    driver = open_web_page()
    site_head_phone = driver.find_element_by_xpath(LC_XP_PHONE_HEAD)
    print(site_head_phone.text)
    checked_value = site_head_phone.text == MAIN_PHONE_NUMBER
    driver.close()
    assert checked_value


@pytest.mark.bs_check
def test_cart_hover_popup_text():
    driver = open_web_page()
    cart_block = driver.find_element_by_xpath(LS_XP_CART_POPUP)
    cart_popup = cart_block.get_attribute("title")
    checked_value = cart_popup == TXT_CART_POPUP
    driver.close()
    assert checked_value


@pytest.mark.regression_main
@pytest.mark.regression_cart
@pytest.mark.true_hover
def test_cart_screen_shot_test():
    driver = open_web_page()
    a = ActionChains(driver)
    cart_block = driver.find_element_by_xpath(LS_XP_CART_POPUP)
    a.move_to_element(cart_block)
    driver.save_screenshot("before.png")
    a.move_to_element(cart_block).perform()
    driver.save_screenshot("after.png")
    driver.implicitly_wait(9)
    driver.close()
    assert a


@pytest.mark.negative_tests
# run with option -m negative_tests
def test_not_found_search_message():
    driver = open_web_page()
    text_input = TXT_WRONG_SEARCH_TEXT
    expected_text = TXT_NOT_FOUND_RESPONSE + TXT_WRONG_SEARCH_TEXT + '\"'
    result_text = ''
    expected_horizontal_position = 475
    expected_vertical_position = 445
    try:
        text_search = driver.find_element_by_id(LC_ID_MAIN_TEXT_SEARCH_BOX)
        submit_button = driver.find_element_by_xpath(LC_XP_BT_SEARCH_SUBMIT)
        text_search.send_keys(text_input)
        submit_button.click()
        not_found_message = driver.find_element(By.XPATH,
                                                LC_XP_NOT_FOUND_SEARCH_TXT)
        print('The all elements of test are found')
        print('The found message text is {}'.format(not_found_message.text))
        result_text = not_found_message.text
    except NoSuchElementException as nse:
        print('The expected element '
              '{} is not found as well'.format(nse.args[0]))
    except Exception as e:
        print('Something is wrong: ' + e.args[0])
        print(e.args)
        print(e)
    finally:
        found_location_x = not_found_message.location['x']
        found_location_y = not_found_message.location['y']
        driver.close()
    # Asserts
    assert result_text == expected_text
    assert found_location_x == expected_horizontal_position
    assert found_location_y == expected_vertical_position


@pytest.mark.positive_tests
@pytest.mark.search_tests
# run with option -m positive_tests
def test_found_search_message():
    driver = open_web_page()
    text_input = TXT_VALID_SEARCH_TEXT
    expected_text = '"DRESSES"'
    expected_horizontal_position = 555
    expected_vertical_position = 395
    result_text = ''
    try:
        text_search = driver.find_element_by_id(LC_ID_MAIN_TEXT_SEARCH_BOX)
        submit_button = driver.find_element_by_xpath(LC_XP_BT_SEARCH_SUBMIT)
        text_search.send_keys(text_input)
        submit_button.click()
        found_title = driver.find_element(By.XPATH, LC_XP_SEARCH_TITLE)
        print('The found text is {}'.format(found_title.text))
        result_text = found_title.text
    except NoSuchElementException as nse:
        print('The expected element '
              '{} is not found as well'.format(nse.args[0]))
    except Exception as e:
        print('Something is wrong: ' + e.args[0])
        print(e.args)
        print(e)
    found_location_x = found_title.location['x']
    found_location_y = found_title.location['y']
    driver.close()
    # Asserts
    assert result_text == expected_text
    assert found_location_x == expected_horizontal_position
    assert found_location_y == expected_vertical_position


@pytest.mark.positive_tests
@pytest.mark.search_tests
@pytest.mark.search_sort
# run with option -m positive_tests
def test_search_sort():
    driver = open_web_page()
    text_input = TXT_VALID_SEARCH_TEXT
    result_text = ''
    try:
        text_search = driver.find_element_by_id(LC_ID_MAIN_TEXT_SEARCH_BOX)
        submit_button = driver.find_element_by_xpath(LC_XP_BT_SEARCH_SUBMIT)
        text_search.send_keys(text_input)
        submit_button.click()
        found_title = driver.find_element(By.XPATH, LC_XP_SEARCH_TITLE)
        sort_dropdown = driver.find_element(By.XPATH, LC_XP_SEARCH_SORT_BY_DD)
        sort_dropdown.click()
        selecting_menu = Select(driver.find_element_by_xpath("%s" % XP_PRICE_DROPDOWN))
        selecting_menu.select_by_visible_text(XP_PRICE_SELECTION_TEXT)
        selected_search = driver.find_element_by_xpath("%s" % XP_SELECTED_PRICE)
        result_text = selected_search.text
        print('the result text is {}'.format(result_text))
    except NoSuchElementException as nse:
        print('The expected element '
              '{} is not found as well'.format(nse.args[0]))
    except Exception as e:
        print('Something is wrong: ' + e.args[0])
        print(e.args)
        print(e)
    print(type(found_title))
    driver.close()
    # Asserts
    assert result_text.startswith('Price: Highest first')
    assert result_text.endswith('Reference: Highest first')


@pytest.mark.search_sort
# run with option -m positive_tests
def test_search_price_filter_apply():
    driver = open_web_page()
    text_input = TXT_VALID_SEARCH_TEXT
    result_text = ''
    try:
        text_search = driver.find_element_by_id(LC_ID_MAIN_TEXT_SEARCH_BOX)
        submit_button = driver.find_element_by_xpath(LC_XP_BT_SEARCH_SUBMIT)
        text_search.send_keys(text_input)
        submit_button.click()
        found_title = driver.find_element(By.XPATH, LC_XP_SEARCH_TITLE)
        sort_dropdown = driver.find_element(By.XPATH, LC_XP_SEARCH_SORT_BY_DD)
        sort_dropdown.click()
        selecting_menu = Select(driver.find_element_by_xpath(XP_PRICE_DROPDOWN))
        selecting_menu.select_by_visible_text(XP_PRICE_SELECTION_TEXT)
        selected_search = driver.find_element_by_xpath(XP_SELECTED_PRICE)
        result_text = selected_search.text
        print('the result text is {}'.format(result_text))
    except NoSuchElementException as nse:
        print('The expected element '
              '{} is not found as well'.format(nse.args[0]))
    except Exception as e:
        print('Something is wrong: ' + e.args[0])
        print(e.args)
        print(e)
    print(type(found_title))
    driver.close()
    # Asserts
    assert result_text.startswith('Price: Highest first')
    assert result_text.endswith('Reference: Highest first')


@pytest.mark.search_sort
@pytest.mark.search_sort_detailed
# run with option -m positive_tests
def test_search_filter_apply_affects_first_element():
    driver = open_web_page()
    text_input = TXT_VALID_SEARCH_TEXT
    result_text = ''
    try:
        text_search = driver.find_element_by_id(LC_ID_MAIN_TEXT_SEARCH_BOX)
        submit_button = driver.find_element_by_xpath(LC_XP_BT_SEARCH_SUBMIT)
        text_search.send_keys(text_input)
        submit_button.click()
        first_element_before = driver.find_element_by_xpath(
            XP_FIRST_SEARCH_ELEMENT).get_attribute("title")
        print(first_element_before)
        found_title = driver.find_element(By.XPATH, LC_XP_SEARCH_TITLE)
        sort_dropdown = driver.find_element(By.XPATH, LC_XP_SEARCH_SORT_BY_DD)
        sort_dropdown.click()
        selecting_menu = Select(driver.find_element_by_xpath(XP_PRICE_DROPDOWN))
        selecting_menu.select_by_visible_text(XP_PRICE_SELECTION_TEXT)
        # selected_search = driver.find_element_by_xpath(XP_SELECTED_PRICE)
        # result_text = selected_search.text
        first_element_after = driver.find_element_by_xpath(
            XP_FIRST_SEARCH_ELEMENT).get_attribute("title")
        print('the result text is {}'.format(result_text))
    except NoSuchElementException as nse:
        print('The expected element '
              '{} is not found as well'.format(nse.args[0]))
    except Exception as e:
        print('Something is wrong: ' + e.args[0])
        print(e.args)
        print(e)
    print(type(found_title))
    driver.close()
    # Asserts
    # assert result_text.startswith('Price: Highest first')
    # assert result_text.endswith('Reference: Highest first')
    assert first_element_before == "Printed Summer Dress"
    assert first_element_after == "Printed Dress"
    assert first_element_after != first_element_before


def main():
    driver = open_web_page()
    # initial_different_checking(driver)
    check_site_availability(driver)
    check_text_search_submit(driver)
    driver.close()


def initial_different_checking(driver):
    try:
        site_head_logo = driver.find_element_by_xpath(LC_XP_HEAD_LOGO)
        print('The expected elements {} is found'.format(site_head_logo))
        print('The elements location is {}'.format(site_head_logo.location))
        print('The elements size is {}'.format(site_head_logo.size))
        print('including: height is {} '.format(site_head_logo.size['height']))
        print('The element location is {} '.format(site_head_logo.location))
        site_head_block = driver.find_element_by_xpath(LC_XP_PHONE_BLOCK)
        print('The expected elements {} is found'.format(site_head_block))
        site_head_phone = driver.find_element_by_xpath(LC_XP_PHONE_HEAD)
        print('The expected elements {} is found'.format(site_head_phone))
        print('Company phone at head is: ' + site_head_phone.text)
        print(type(site_head_phone.text))
    except NoSuchElementException as nse:
        print('The expected elements are not found as well')
        print(nse.args[0])
    except Exception as e:
        print('Something is wrong' + e.args[0])


if __name__ == '__main__':
    main()
