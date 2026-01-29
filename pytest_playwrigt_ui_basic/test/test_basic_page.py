import pytest
import os
import logging
from PIL import Image, ImageChops
from pytest_playwrigt_ui_basic.page_objects.base_page import StartingPage
from playwright.sync_api import sync_playwright, expect
import time
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


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


def test_compare_screenshot(page):
    page_content = StartingPage(page)
    page_content.goto()
    dir_for_screens = "screenshots"
    actual_image = os.path.join(dir_for_screens, "actual.png")
    # make actual screenshot
    page_content.make_screen_shot(actual_image)

    # apply mask above actual screenshot
    base = Image.open(f".\\{dir_for_screens}\\actual.png").convert("RGBA")
    overlay = Image.open(f".\\{dir_for_screens}\\mask_image.png").convert("RGBA")

    # save actual image with applied mask
    result = Image.alpha_composite(base, overlay)
    result.save(f".\\{dir_for_screens}\\tested_image.png")

    reference_image = Image.open(f".\\{dir_for_screens}\\reference.png").convert("RGB")
    test_image = Image.open(f".\\{dir_for_screens}\\tested_image.png").convert("RGB")
    diff = ImageChops.difference(test_image, reference_image)
    logger.info(f"The difference between two images is: {diff.getbbox()}")
    # assert not diff.getbbox()


    if diff.getbbox():
        logger.info(
            "Detected difference between base and incoming snapshot. Proceeding with next comparison."
        )
        diff = diff.convert("L")  # grayscale
        diff = diff.point(lambda x: 255 if x > 0 else 0)

        diff.save(f".\\{dir_for_screens}\\found_differences.png")
    #     time.sleep(1)
    #     current_time = datetime.now()
    #     pass
    # else:
    #     logger.info("Snapshots matched.")
    #     return True

    assert not diff.getbbox()