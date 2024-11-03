import pytest
from starting_page import StartingPage
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


# Test case using the StartingPage object
def test_login(page):
    login_page = StartingPage(page)
    login_page.navigate("https://demoqa.com")

    # Assertion example - page check
    assert login_page.check_loading_initial_page()
