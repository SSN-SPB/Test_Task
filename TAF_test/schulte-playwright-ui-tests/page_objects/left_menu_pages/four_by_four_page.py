from page_objects.base_page import BasePage


class FourByFourPage(BasePage):
    TABLE_SIZE = 16
    GRID_DIMENSION = 4
    SIZE_LABEL = "4x4"
    MENU_BUTTON = "button.size:has-text('4x4')"

    def __init__(self, page, logger=None):
        super().__init__(page, logger)

    def load(self):
        self.navigate_to(self.BASE_URL)
        self.page.locator(self.MENU_BUTTON).click()
        self.wait_for_selector(self.BOARD_SELECTOR)
        self.logger.info("4x4 page loaded")

    def is_displayed(self):
        return self.is_board_visible()

    def get_table_elements_count(self):
        return self.get_cell_count()

    def has_correct_number_of_cells(self):
        return self.get_cell_count() == self.TABLE_SIZE

    def has_unique_numbers(self):
        values = self.get_cell_values()
        return len(set(values)) == self.TABLE_SIZE

    def get_expected_values(self):
        return {str(i) for i in range(1, self.TABLE_SIZE + 1)}

    def is_active(self):
        cls = self.page.locator(self.MENU_BUTTON).get_attribute("class") or ""
        return "active" in cls

    def get_cell_value(self, index):
        return self.get_board_cells().nth(index).inner_text()
