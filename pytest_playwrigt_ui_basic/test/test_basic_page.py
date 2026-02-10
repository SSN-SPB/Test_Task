import pytest
import os
import logging
from PIL import Image, ImageChops
from pytest_playwrigt_ui_basic.page_objects.base_page import StartingPage
from playwright.sync_api import sync_playwright

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
    snapshots = "screenshots"
    actual_image = os.path.join(f".\\{snapshots}\\test_snapshots", "actual.png")
    # make actual screenshot
    page_content.make_screen_shot(actual_image)

    # apply mask above actual screenshot
    base = Image.open(f".\\{snapshots}\\test_snapshots\\actual.png").convert("RGBA")
    mask = Image.open(f".\\{snapshots}\\mask_snapshots\\mask_image.png").convert("RGBA")

    # save actual image with applied mask
    result = Image.alpha_composite(base, mask)
    result.save(f".\\{snapshots}\\test_snapshots\\actual_with_applied_mask.png")

    reference_image = Image.open(
        f".\\{snapshots}\\reference_snapshots\\reference.png"
    ).convert("RGB")
    test_image = Image.open(
        f".\\{snapshots}\\test_snapshots\\actual_with_applied_mask.png"
    ).convert("RGB")
    diff = ImageChops.difference(test_image, reference_image)
    logger.info(f"The found difference between two images is: {diff.getbbox()}")

    if diff.getbbox():
        logger.info("Detected difference between test and reference snapshots.")
        diff = diff.convert("L")  # grayscale
        diff = diff.point(lambda x: 255 if x > 0 else 0)

        diff.save(f".\\{snapshots}\\differences_snapshots\\found_differences.png")

    assert not diff.getbbox()
