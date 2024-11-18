from playwright.sync_api import Page


class TextBoxPage:
    # Initialize page and selectors
    def __init__(self, page: Page):
        self.page = page
        self.fullNameField = page.locator("#userName")
        self.emailField = page.locator("#userEmail")
        self.currentAddressField = page.locator("#currentAddress")
        self.permanentAddressField = page.locator("#permanentAddress")
        self.submitButton = page.locator("#submit")
        self.pageLoadingIndicator = page.locator(".text-center")


    # Actions on page
    def navigate(self, url: str):
        self.page.goto(url)


    # Get information from page
    def check_loading_page(self):
        return self.pageLoadingIndicator.is_visible()