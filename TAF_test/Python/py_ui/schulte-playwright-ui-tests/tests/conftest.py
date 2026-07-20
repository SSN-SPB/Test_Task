import sys
from pathlib import Path

import allure
import pytest

from connectors.browser_connector import BrowserConnector
from connectors.site_connector import SiteConnector
from logger.logger import Logger

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


def pytest_addoption(parser):
    parser.addoption(
        "--run_without_ui",
        action="store",
        default="true",
        help="Yes if need to see the run x`in browser locally",
    )
    parser.addoption(
        "--browser_type",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Browser to run Playwright tests with",
    )


@pytest.fixture(scope="session")
def headless_mode(request):
    value = request.config.getoption("--run_without_ui")
    return value.lower() == "true" if isinstance(value, str) else bool(value)


@pytest.fixture(scope="session")
def select_browser(request):
    return request.config.getoption("--browser_type")


@pytest.fixture(scope="session")
def logger():
    return Logger()


@pytest.fixture(scope="session")
def browser_connector(logger, headless_mode, select_browser):
    connector = BrowserConnector(headless=headless_mode)
    connector.launch_browser(browser_type=select_browser)
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
