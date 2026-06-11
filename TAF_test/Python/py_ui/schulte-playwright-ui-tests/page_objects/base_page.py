from logger.logger import Logger


class BasePage:
    BASE_URL = "https://schultetable.web.app"
    CELL_SELECTOR = ".cell"
    BOARD_SELECTOR = ".board-container"
    RESTART_BUTTON = ".restart-button"
    TOP_BAR = ".top-bar"
    DESCRIPTION = ".desc"
    NEXT_NUMBER = ".top-bar span"
    TIMER = ".top-bar p:last-child"

    def __init__(self, page, logger=None):
        self.page = page
        self.logger = logger or Logger()

    def navigate_to(self, url):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def click(self, selector):
        self.page.locator(selector).click()

    def get_text(self, selector):
        return self.page.locator(selector).text_content()

    def wait_for_selector(self, selector, timeout=5000):
        self.page.locator(selector).wait_for(timeout=timeout)

    def is_element_visible(self, selector):
        return self.page.locator(selector).is_visible()

    def get_board_cells(self):
        return self.page.locator(self.CELL_SELECTOR)

    def get_cell_count(self):
        return self.get_board_cells().count()

    def get_cell_values(self):
        cells = self.get_board_cells()
        count = cells.count()
        return [cells.nth(i).inner_text() for i in range(count)]

    def click_cell(self, index):
        self.get_board_cells().nth(index).click()

    def get_next_number(self):
        return self.get_text(self.NEXT_NUMBER)

    def click_restart(self):
        self.click(self.RESTART_BUTTON)

    def is_board_visible(self):
        return self.is_element_visible(self.BOARD_SELECTOR)

    def get_description_text(self):
        return self.get_text(self.DESCRIPTION)