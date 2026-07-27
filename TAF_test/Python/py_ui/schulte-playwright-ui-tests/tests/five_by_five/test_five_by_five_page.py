import allure
import pytest

from page_objects.left_menu_pages.five_by_five_page import FiveByFivePage
from service_functions.menu_navigation_service import MenuNavigationService
from service_functions.table_validation_service import TableValidationService


@allure.feature("Schulte Table")
@allure.story("5x5 Grid")
@pytest.mark.usefixtures("setup")
class TestFiveByFivePage:

    @allure.title("Navigate to 5x5 grid")
    def test_navigate_to_five_by_five(self, browser):
        menu_service = MenuNavigationService(browser)
        menu_service.navigate_to_five_by_five()
        page_obj = FiveByFivePage(browser)
        assert page_obj.is_displayed(), "5x5 board is not displayed"

    @allure.title("5x5 grid has correct cell count")
    def test_table_has_correct_cell_count(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 5)
        assert (
            page_obj.has_correct_number_of_cells()
        ), "Board does not have 25 cells"

    @allure.title("5x5 grid cells contain unique numbers")
    def test_cells_contain_unique_numbers(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 5)
        assert (
            page_obj.has_unique_numbers()
        ), "Board does not contain 25 unique numbers"

    @allure.title("5x5 grid cell values are in range")
    def test_cell_values_in_range(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 5)
        values = set(page_obj.get_cell_values())
        expected = page_obj.get_expected_values()
        assert (
            values == expected
        ), f"Cell values {values} don't match expected {expected}"

    @allure.title("5x5 grid description text is correct")
    def test_description_text(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 5)
        desc = page_obj.get_description_text()
        assert (
            "1 to 25" in desc
        ), f"Description '{desc}' does not mention 1 to 25"

    @allure.title("5x5 menu button is active after selection")
    def test_menu_button_active(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 5)
        assert page_obj.is_active(), "5x5 button is not active after selection"

    @allure.title("Clicking correct number advances game on 5x5")
    def test_click_correct_number_advances(self, browser):
        MenuNavigationService.return_selected_grid(browser, 5)
        validation = TableValidationService(browser)
        assert validation.get_next_expected_number() == "1"
        validation.click_number_in_order(1)
        assert validation.get_next_expected_number() == "2"

    @allure.title("Restart resets game on 5x5")
    def test_restart_resets_game(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 5)
        validation = TableValidationService(browser)
        validation.click_number_in_order(1)
        page_obj.click_restart()
        assert validation.get_next_expected_number() == "1"
