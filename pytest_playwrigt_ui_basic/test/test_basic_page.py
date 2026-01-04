# from pages.google_page import GooglePage
import pytest

# from pytest_playwrigt_ui_basic.page_objects_google.base_page import GooglePage
from pytest_playwrigt_ui_basic.page_objects.base_page import StartingPage
from playwright.sync_api import sync_playwright, expect


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
    context.add_cookies(
        [
            {
                "name": "cookie_consent",
                "value": "true",
                "domain": "schultetable.web.app",
                "path": "/",
            }
        ]
    )
    page = context.new_page()
    yield page
    context.close()


def test_google_page(page):
    page_content = StartingPage(page)
    page_content.goto()

    assert "Restart" in page_content.get_restart_button_text()
    assert page_content.search_box_visible()
