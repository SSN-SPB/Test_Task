from logger.logger import Logger


class TableValidationService:
    CELL_SELECTOR = ".cell"
    BOARD_SELECTOR = ".board-container"

    def __init__(self, page, logger=None):
        self.page = page
        self.logger = logger or Logger()

    def validate_table_has_cells(self, expected_count):
        cells = self.page.locator(self.CELL_SELECTOR)
        actual_count = cells.count()
        self.logger.info(
            f"Validating cell count: expected={expected_count}, "
            f"actual={actual_count}"
        )
        return actual_count == expected_count

    def get_all_cell_values(self):
        cells = self.page.locator(self.CELL_SELECTOR)
        count = cells.count()
        values = [cells.nth(i).inner_text() for i in range(count)]
        self.logger.info(f"Retrieved {len(values)} cell values")
        return values

    def validate_unique_numbers(self, expected_count):
        values = self.get_all_cell_values()
        unique_count = len(set(values))
        self.logger.info(
            f"Validating unique numbers: expected={expected_count}, "
            f"unique={unique_count}"
        )
        return unique_count == expected_count

    def validate_numbers_in_range(self, max_number):
        values = self.get_all_cell_values()
        expected = {str(i) for i in range(1, max_number + 1)}
        actual = set(values)
        self.logger.info(f"Validating number range 1-{max_number}")
        return actual == expected

    def validate_board_visible(self):
        is_visible = self.page.locator(self.BOARD_SELECTOR).is_visible()
        self.logger.info(f"Board visible: {is_visible}")
        return is_visible

    def get_next_expected_number(self):
        return self.page.locator(".top-bar span").text_content()

    def click_number_in_order(self, number):
        cells = self.page.locator(self.CELL_SELECTOR)
        count = cells.count()
        target = str(number)
        for i in range(count):
            if cells.nth(i).inner_text() == target:
                cells.nth(i).click()
                self.logger.info(f"Clicked cell with number {number}")
                return True
        self.logger.warning(f"Cell with number {number} not found")
        return False
