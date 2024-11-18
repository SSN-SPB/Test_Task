from playwright.sync_api import Page

class LoginPage:
    # Initialize page and selectors
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login")

    # Actions on the login page
    def navigate(self, url: str):
        self.page.goto(url)

    def enter_username(self, username: str):
        self.username_input.fill(username)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def submit_login(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        """Composite action to perform a complete login"""
        self.enter_username(username)
        self.enter_password(password)
        self.submit_login()