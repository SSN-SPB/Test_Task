import os
import pytest

from playwright.sync_api import Page, sync_playwright


# Define a pytest fixture to set up Playwright and browser instance
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


# noinspection PyTypeChecker
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
