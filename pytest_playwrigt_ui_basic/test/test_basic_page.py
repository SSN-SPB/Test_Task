import os
import logging
from PIL import Image, ImageChops
from pytest_playwrigt_ui_basic.page_objects.base_page import StartingPage
from pytest_playwrigt_ui_basic.service_functions.ui import page, browser


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_google_page(page):
    page_content = StartingPage(page)
    page_content.goto()

    assert "Restart" in page_content.get_restart_button_text()
    assert page_content.search_box_visible()


def _test_compare_screenshot(page):
    page_content = StartingPage(page)
    page_content.goto()
    snapshots = "screenshots"
    actual_image = os.path.join(f".\\{snapshots}\\test_snapshots", "actual.png")
    # make actual screenshot
    page_content.make_screen_shot(actual_image)

    test_image = Image.open(f".\\{snapshots}\\test_snapshots\\actual.png").convert(
        "RGB"
    )
    reference_image = Image.open(f".\\{snapshots}\\test_snapshots\\actual.png").convert("RGB")

    # # apply mask above actual screenshot
    # base = Image.open(f".\\{snapshots}\\test_snapshots\\actual.png").convert("RGBA")
    # mask = Image.open(f".\\{snapshots}\\mask_snapshots\\mask_image.png").convert("RGBA")
    #
    # # save actual image with applied mask
    # result = Image.alpha_composite(base, mask)
    # result.save(f".\\{snapshots}\\test_snapshots\\actual_with_applied_mask.png")
    #
    # # define the reference and tested images
    # reference_image = Image.open(
    #     f".\\{snapshots}\\reference_snapshots\\reference.png"
    # ).convert("RGB")
    # test_image = Image.open(
    #     f".\\{snapshots}\\test_snapshots\\actual_with_applied_mask.png"
    # ).convert("RGB")

    # Getting the differences between reference and tested images
    diff = ImageChops.difference(test_image, reference_image)
    logger.info(f"The found difference between two images is: {diff.getbbox()}")

    # Creating the image with difference (if any)
    if diff.getbbox():
        logger.info("Detected difference between test and reference snapshots.")
        diff = diff.convert("L")  # grayscale
        diff = diff.point(lambda x: 255 if x > 0 else 0)

        diff.save(f".\\{snapshots}\\differences_snapshots\\found_differences.png")

    # assert True
    assert not diff.getbbox()
