import pytest
from playwright.pytest_playwright_ui_basic.page_objects_google.google_base_page import GooglePage
# from page_objects.g.google_page import GooglePage

@pytest.mark.asyncio
async def test_google_page_content(page):
    google = GooglePage(page)

    # Open Google
    await google.goto()

    # Simplest assertion: title contains "Google"
    title = await google.get_title()
    assert "Google" in title

    # Another simple assert to check UI element exists
    assert await google.is_search_box_visible()