from playwright.sync_api import Page

class StartingPage:
    def __init__(self, page: Page):
        self.page = page
        self.field_next = ".top-bar"
        self.restart_page = ".restart-button"

    def goto(self):
        self.page.goto("https://schultetable.web.app/")

    def get_restart_button_text(self):
        # text = self.page.locator(self.restart_page).text_content()
        text = self.page.locator(self.restart_page).inner_text()
        return text
        # return self.page.content()

    def search_box_visible(self):
        return self.page.is_visible(self.field_next)

    def make_screen_shot(self, actual_image):
        self.page.screenshot(path=actual_image, full_page=True)
