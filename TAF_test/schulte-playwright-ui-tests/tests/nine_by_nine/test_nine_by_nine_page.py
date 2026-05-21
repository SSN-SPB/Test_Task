import allure
import pytest
from page_objects.left_menu_pages.nine_by_nine_page import NineByNinePage
from service_functions.menu_navigation_service import MenuNavigationService
from service_functions.table_validation_service import TableValidationService


@allure.feature("Schulte Table")
@allure.story("9x9 Grid")
@pytest.mark.usefixtures("setup")
class TestNineByNinePage:

    @allure.title("Navigate to 9x9 grid")
    def test_navigate_to_nine_by_nine(self, browser):
        menu_service = MenuNavigationService(browser)
        menu_service.navigate_to_nine_by_nine()
        page_obj = NineByNinePage(browser)
        assert page_obj.is_displayed(), "9x9 board is not displayed"

    @allure.title("9x9 grid has correct cell count")
    def test_table_has_correct_cell_count(self, browser):
        page_obj = NineByNinePage(browser)
        page_obj.load()
        assert page_obj.has_correct_number_of_cells(), "Board does not have 81 cells"

    @allure.title("9x9 grid cells contain unique numbers")
    def test_cells_contain_unique_numbers(self, browser):
        page_obj = NineByNinePage(browser)
        page_obj.load()
        assert page_obj.has_unique_numbers(), "Board does not contain 81 unique numbers"

    @allure.title("9x9 grid cell values are in range")
    def test_cell_values_in_range(self, browser):
        page_obj = NineByNinePage(browser)
        page_obj.load()
        values = set(page_obj.get_cell_values())
        expected = page_obj.get_expected_values()
        assert values == expected, f"Cell values {values} don't match expected {expected}"

    @allure.title("9x9 grid description text is correct")
    def test_description_text(self, browser):
        page_obj = NineByNinePage(browser)
        page_obj.load()
        desc = page_obj.get_description_text()
        assert "1 to 81" in desc, f"Description '{desc}' does not mention 1 to 81"

    @allure.title("9x9 menu button is active after selection")
    def test_menu_button_active(self, browser):
        page_obj = NineByNinePage(browser)
        page_obj.load()
        assert page_obj.is_active(), "9x9 button is not active after selection"

    @allure.title("Clicking correct number advances game on 9x9")
    def test_click_correct_number_advances(self, browser):
        page_obj = NineByNinePage(browser)
        page_obj.load()
        validation = TableValidationService(browser)
        assert validation.get_next_expected_number() == "1"
        validation.click_number_in_order(1)
        assert validation.get_next_expected_number() == "2"

    @allure.title("Restart resets game on 9x9")
    def test_restart_resets_game(self, browser):
        page_obj = NineByNinePage(browser)
        page_obj.load()
        validation = TableValidationService(browser)
        validation.click_number_in_order(1)
        page_obj.click_restart()
        assert validation.get_next_expected_number() == "1"
