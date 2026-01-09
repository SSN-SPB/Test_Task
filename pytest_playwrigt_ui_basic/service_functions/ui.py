import os
import pytest

# from typing import Generator
from playwright.sync_api import Page, sync_playwright
# from utilities.imagecomp import ImageComp


# @pytest.fixture()
# def page() -> Generator:
#     """
#     Page fixture.
#     """
#     with sync_playwright() as sp:
#         browser = sp.chromium.launch(headless=os.environ["HEADLESS"] == "true")
#         page = browser.new_page()
#         page.set_viewport_size({"width": 1920, "height": 958})
#         yield page
#         browser.close()
#
#
# @pytest.fixture(scope="session")
# def ui_base_url(environment: str) -> str:
#     """
#     UI Base URL.
#     """
#     return CONFIG[environment]["ui"]["base_url"]
#
#
# @pytest.fixture()
# def login_page(page: Page, ui_base_url: str) -> LoginPage:
#     """
#     LoginPage object.
#     """
#     page.goto(url=ui_base_url)
#     return LoginPage(page)


@pytest.fixture(scope="function")
def snapshot(request) -> Generator:
    """
    Handle for taking snapshots inside the tests.
    :return: snapshot handle
    """
    ic = ImageComp(request.node.name)
    yield ic.take_snapshot