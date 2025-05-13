from playwright.sync_api import Page
import allure

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

    @allure.step("Fill Name field")
    def fill_name(self):
        return self.fullNameField.fill("Test_name")

    @allure.step("Click Submit button")
    def submit_input(self):
        return self.submitButton.click()

    @allure.step("Check submitted name")
    def filled_name_value(self,expected_name):
        return self.page.locator(f"//*[@id='name' and contains(., '{expected_name}')]")