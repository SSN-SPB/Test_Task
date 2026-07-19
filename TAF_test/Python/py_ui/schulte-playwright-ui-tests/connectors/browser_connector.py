from playwright.sync_api import sync_playwright


class BrowserConnector:
    def __init__(self, headless=False):
        # def __init__(self, logger=None, headless=False):
        # self.logger = logger
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def launch_browser(self):
        # if self.logger:
        #     self.logger.info("Launching browser")

        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def get_browser(self):
        return self.page

    def get_page(self):
        return self.page

    def close_browser(self):
        # if self.logger:
        #     self.logger.info("Closing browser")

        if self.page:
            self.page.close()
            self.page = None

        if self.context:
            self.context.close()
            self.context = None

        if self.browser:
            self.browser.close()
            self.browser = None

        if self.playwright:
            self.playwright.stop()
            self.playwright = None
