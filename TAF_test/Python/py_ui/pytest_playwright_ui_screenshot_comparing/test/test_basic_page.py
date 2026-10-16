import logging
from pathlib import Path

from PIL import Image, ImageChops
from pytest_playwrigt_ui_basic.page_objects.base_page import StartingPage

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_google_page(page):
    """
    This test checks the Starting page availability as
    Playwright test without screenshot comparing
    by checking the presence of the "Restart" button
    and the visibility of the search box.
    """
    page_content = StartingPage(page)
    page_content.goto()

    assert "Restart" in page_content.get_restart_button_text()
    assert page_content.search_box_visible()


def test_demo_compare_screenshot(page):
    """
    This test checks the correctness of Starting page
    by comparing actual and golden/reference screenshots
    with applied mask to ignore the dynamic content of the page.
    """
    page_content = StartingPage(page)
    page_content.goto()
    # define the path for screenshots folder
    snapshots = Path("screenshots")
    # define the paths for reference, actual, mask, actual with mask,
    # and difference images
    reference_path = snapshots / "reference_snapshots" / "reference.png"
    actual_path = snapshots / "test_snapshots" / "actual_screenshot.png"
    mask_path = snapshots / "mask_snapshots" / "mask_image.png"
    actual_masked_path = snapshots / "test_snapshots" / "actual_with_mask.png"
    difference_path = (
        snapshots / "differences_snapshots" / "found_differences.png"
    )
    # make actual screenshot - should be commented to use demo screenshots
    page_content.make_screen_shot(actual_path)
    # for the demo purpose save as the actual_screenshot.png
    # one of these two files below
    # - actual_modified_for_the_test.png
    # - actual_corrupted_for_the_test.png

    # convert the image and mask into the required RGBA format
    base = Image.open(actual_path).convert("RGBA")
    mask = Image.open(mask_path).convert("RGBA")

    # apply a mask to the above image and save it to the file
    result = Image.alpha_composite(base, mask)
    result.save(actual_masked_path)

    # select reference screenshot and convert to RGB format for
    # the correct comparing
    # for the demo purpose save as reference.png one of two files
    # - reference_corrupted_for_test.png
    # - reference_modified_for_test.png
    reference_image = Image.open(reference_path).convert("RGB")
    test_image = Image.open(actual_masked_path).convert("RGB")

    # Getting the differences between reference and actual images
    diff = ImageChops.difference(test_image, reference_image)

    # Creating the image with difference (if any)
    if diff.getbbox():
        diff = diff.convert("L")
        diff = diff.point(lambda x: 255 if x > 0 else 0)
        # to decrease threshold
        # modify the value in the lambda function above e.g. 240 instead of 0

        logger.info("The difference is found")
        logger.info(f" The affected points: {diff.getbbox()}.")
        diff.save(difference_path)
        logger.info(f"See the saved file: {difference_path}")

    # expected that there is no difference between images
    # and therefore => diff.getbbox() doesn't exist
    assert not diff.getbbox()
