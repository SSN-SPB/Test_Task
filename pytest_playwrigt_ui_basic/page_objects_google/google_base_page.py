from playwright.sync_api import Page

class GooglePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = "input[name='q']"

    def goto(self):
        self.page.goto("https://www.google.com")

    def get_title(self):
        return self.page.title()

    def search_box_visible(self):
        return self.page.is_visible(self.search_input)