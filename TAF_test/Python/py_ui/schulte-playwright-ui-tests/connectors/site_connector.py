class SiteConnector:
    def __init__(self, page, logger=None):
        self.page = page
        self.logger = logger
        self.base_url = "https://schultetable.web.app"

    def navigate_to_site(self):
        if self.logger:
            self.logger.info(f"Navigating to {self.base_url}")
        self.page.goto(self.base_url)

    def close_site(self):
        # Page lifecycle is managed by BrowserConnector.
        pass
