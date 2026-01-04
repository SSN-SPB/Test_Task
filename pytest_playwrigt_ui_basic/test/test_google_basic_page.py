# from pages.google_page import GooglePage
import pytest
from pytest_playwrigt_ui_basic.page_objects_google.google_base_page import GooglePage
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
    context.add_cookies([
        {
            "name": "cookie_consent",
            "value": "true",
            "domain": "www.google.com",
            "path": "/"
        }
    ])
    page = context.new_page()
    yield page
    context.close()

def test_google_page(page):
    google = GooglePage(page)

    google.goto()

    # simplest assertion
    assert "Google" in google.get_title()

    # check that search box exists
    assert google.search_box_visible()