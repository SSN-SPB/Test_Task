import pytest
import allure
# pytest --alluredir=allure-results
# allure generate allure-results --clean -o allure-report
# tests\allure-report> python -m http.server 8000
from page_objects.text_box_page import TextBoxPage
from playwright.sync_api import sync_playwright

# Define a pytest fixture to set up Playwright and browser instance
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    return page


@allure.feature('Login')
@allure.story('Valid login')
# Test case using the StartingPage object
def test_login(page):
    text_box_page = TextBoxPage(page)
    text_box_page.navigate("https://demoqa.com/text-box")

    # Assertion example - page check
    assert text_box_page.check_loading_page()
