# from pages.google_page import GooglePage
from pytest_playwrigt_ui_basic.page_objects_google import GooglePage
from pytest_playwrigt_ui_basic.page_objects_google import G

def test_google_page(page):
    google = GooglePage(page)

    google.goto()

    # simplest assertion
    assert "Google" in google.get_title()

    # check that search box exists
    assert google.search_box_visible()