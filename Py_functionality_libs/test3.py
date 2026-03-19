import pytest
from playwright.sync_api import Page
from decorators import retry, screenshot_on_fail, measure_time, login_required


@retry(times=2)
@screenshot_on_fail
@measure_time
@login_required
def test_secure_area(page: Page):
    # After login, we should be inside secure area
    assert page.url.endswith("/secure")

    # Validate UI element
    heading = page.locator("h2").inner_text()
    assert "Secure Area" in heading

    # Intentional step (can break to test retry/screenshot)
    page.locator("#non-existing-element").click()