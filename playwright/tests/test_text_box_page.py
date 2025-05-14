import pytest
import allure
import time
# pytest --alluredir=allure-results
# allure generate allure-results --clean -o allure-report
# tests\allure-report> python -m http.server 8000
from page_objects.text_box_page import TextBoxPage
from playwright.sync_api import sync_playwright

# Define a pytest fixture to set up Playwright and browser instance
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@allure.epic("UI")
@allure.description(
    """
    Test suit checks different scenarios at Admin > Request configuration > Request forms
    for  Custom Form
    """
)
@allure.title("Check demoda/text-box folder")
def test_login(page):
    text_box_page = TextBoxPage(page)
    text_box_page.navigate("https://demoqa.com/text-box")

    # Assertion example - page check
    assert text_box_page.check_loading_page()


@allure.title("Check input name")
def test_fill_name(page):
    text_box_page = TextBoxPage(page)
    text_box_page.navigate("https://demoqa.com/text-box")
    text_box_page.fill_name()
    text_box_page.submit_input()


    # Assertion example - page check
    assert text_box_page.filled_name_value("test_name")