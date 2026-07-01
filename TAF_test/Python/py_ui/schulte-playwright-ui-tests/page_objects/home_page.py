from page_objects.base_page import BasePage


class HomePage(BasePage):
    SIDE_PANEL = ".side-panel-container"
    GRID_SIZE_SECTION = ".grid-size"
    GRID_SIZE_TITLE = ".grid-size .title"
    SIZE_BUTTON = "button.size"
    ACTIVE_SIZE_BUTTON = "button.size.active"
    STATS_SECTION = ".stats"
    BEST_TIME_VALUE = ".stats .value:first-of-type"
    GAMES_VALUE = ".stats .value:last-of-type"

    def __init__(self, page, logger=None):
        super().__init__(page, logger)

    def load(self):
        self.navigate_to(self.BASE_URL)
        self.wait_for_selector(self.BOARD_SELECTOR)
        self.logger.info("Home page loaded")

    def get_title(self):
        return self.page.title()

    def click_menu_item(self, item_text):
        self.logger.info(f"Clicking menu item: {item_text}")
        self.page.locator(f"button.size:has-text('{item_text}')").click()

    def get_active_size(self):
        return self.page.locator(self.ACTIVE_SIZE_BUTTON).text_content()

    def get_all_size_buttons(self):
        buttons = self.page.locator(self.SIZE_BUTTON)
        count = buttons.count()
        return [buttons.nth(i).text_content() for i in range(count)]

    def is_side_panel_visible(self):
        return self.is_element_visible(self.SIDE_PANEL)

    def get_best_time(self):
        return self.get_text(self.BEST_TIME_VALUE)

    def get_games_count(self):
        return self.get_text(self.GAMES_VALUE)

    def is_stats_visible(self):
        return self.is_element_visible(self.STATS_SECTION)