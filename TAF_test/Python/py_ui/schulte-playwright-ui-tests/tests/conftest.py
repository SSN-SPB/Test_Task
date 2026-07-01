import sys
from pathlib import Path

import allure
import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from connectors.browser_connector import BrowserConnector
from connectors.site_connector import SiteConnector
from logger.logger import Logger


@pytest.fixture(scope="session")
def logger():
    return Logger()


@pytest.fixture(scope="session")
def browser_connector(logger):
    connector = BrowserConnector(logger)
    connector.launch_browser()
    yield connector
    connector.close_browser()


@pytest.fixture(scope="session")
def browser(browser_connector):
    return browser_connector.get_page()


@pytest.fixture(scope="session")
def site(browser, logger):
    site_connector = SiteConnector(browser, logger)
    site_connector.navigate_to_site()
    yield site_connector


@pytest.fixture(scope="function")
def setup(browser):
    browser.goto("https://schultetable.web.app")
    browser.locator(".board-container").wait_for()
    yield browser


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        browser = item.funcargs.get("browser")
        if browser:
            allure.attach(
                browser.screenshot(),
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
            )