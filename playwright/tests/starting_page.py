from playwright.sync_api import Page

class StartingPage:
    # Initialize page and selectors
    def __init__(self, page: Page):
        self.page = page
        self.text_selenium = page.locator("[alt='Selenium Online Training']")


    # Actions on page
    def navigate(self, url: str):
        self.page.goto(url)


    # Get information from page
    def check_loading_initial_page(self):
        return self.text_selenium.is_visible()