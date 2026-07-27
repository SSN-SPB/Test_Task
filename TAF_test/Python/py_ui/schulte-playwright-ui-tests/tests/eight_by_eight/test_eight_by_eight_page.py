import allure
import pytest

from page_objects.left_menu_pages.eight_by_eight_page import EightByEightPage
from service_functions.menu_navigation_service import MenuNavigationService
from service_functions.table_validation_service import TableValidationService


@allure.feature("Schulte Table")
@allure.story("8x8 Grid")
@pytest.mark.usefixtures("setup")
class TestEightByEightPage:

    @allure.title("Navigate to 8x8 grid")
    def test_navigate_to_eight_by_eight(self, browser):
        menu_service = MenuNavigationService(browser)
        menu_service.navigate_to_eight_by_eight()
        page_obj = EightByEightPage(browser)
        assert page_obj.is_displayed(), "8x8 board is not displayed"

    @allure.title("8x8 grid has correct cell count")
    def test_table_has_correct_cell_count(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 8)
        assert (
            page_obj.has_correct_number_of_cells()
        ), "Board does not have 64 cells"

    @allure.title("8x8 grid cells contain unique numbers")
    def test_cells_contain_unique_numbers(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 8)
        assert (
            page_obj.has_unique_numbers()
        ), "Board does not contain 64 unique numbers"

    @allure.title("8x8 grid cell values are in range")
    def test_cell_values_in_range(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 8)
        values = set(page_obj.get_cell_values())
        expected = page_obj.get_expected_values()
        assert (
            values == expected
        ), f"Cell values {values} don't match expected {expected}"

    @allure.title("8x8 grid description text is correct")
    def test_description_text(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 8)
        desc = page_obj.get_description_text()
        assert (
            "1 to 64" in desc
        ), f"Description '{desc}' does not mention 1 to 64"

    @allure.title("8x8 menu button is active after selection")
    def test_menu_button_active(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 8)
        assert page_obj.is_active(), "8x8 button is not active after selection"

    @allure.title("Clicking correct number advances game on 8x8")
    def test_click_correct_number_advances(self, browser):
        MenuNavigationService.return_selected_grid(browser, 8)
        validation = TableValidationService(browser)
        assert validation.get_next_expected_number() == "1"
        validation.click_number_in_order(1)
        assert validation.get_next_expected_number() == "2"

    @allure.title("Restart resets game on 8x8")
    def test_restart_resets_game(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 8)
        validation = TableValidationService(browser)
        validation.click_number_in_order(1)
        page_obj.click_restart()
        assert validation.get_next_expected_number() == "1"
