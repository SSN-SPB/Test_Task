import allure
import pytest

from page_objects.left_menu_pages.seven_by_seven_page import SevenBySevenPage
from service_functions.menu_navigation_service import MenuNavigationService
from service_functions.table_validation_service import TableValidationService


@allure.feature("Schulte Table")
@allure.story("7x7 Grid")
@pytest.mark.usefixtures("setup")
class TestSevenBySevenPage:

    @allure.title("Navigate to 7x7 grid")
    def test_navigate_to_seven_by_seven(self, browser):
        menu_service = MenuNavigationService(browser)
        menu_service.navigate_to_seven_by_seven()
        page_obj = SevenBySevenPage(browser)
        assert page_obj.is_displayed(), "7x7 board is not displayed"

    @allure.title("7x7 grid has correct cell count")
    def test_table_has_correct_cell_count(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 7)
        expected_message = "Board does not have 49 cells"
        assert page_obj.has_correct_number_of_cells(), expected_message

    @allure.title("7x7 grid cells contain unique numbers")
    def test_cells_contain_unique_numbers(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 7)
        expected_message = "Board does not contain 49 unique numbers"
        assert page_obj.has_unique_numbers(), expected_message

    @allure.title("7x7 grid cell values are in range")
    def test_cell_values_in_range(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 7)
        values = set(page_obj.get_cell_values())
        expected = page_obj.get_expected_values()
        assert (
            values == expected
        ), f"Cell values {values} don't match expected {expected}"

    @allure.title("7x7 grid description text is correct")
    def test_description_text(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 7)
        desc = page_obj.get_description_text()
        assert "1 to 49" in desc, f"The '{desc}' does not mention 1 to 49"

    @allure.title("7x7 menu button is active after selection")
    def test_menu_button_active(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 7)
        assert page_obj.is_active(), "7x7 button is not active after selection"

    @allure.title("Clicking correct number advances game on 7x7")
    def test_click_correct_number_advances(self, browser):
        MenuNavigationService.return_selected_grid(browser, 7)
        validation = TableValidationService(browser)
        assert validation.get_next_expected_number() == "1"
        validation.click_number_in_order(1)
        assert validation.get_next_expected_number() == "2"

    @allure.title("Restart resets game on 7x7")
    def test_restart_resets_game(self, browser):
        page_obj = MenuNavigationService.return_selected_grid(browser, 7)
        validation = TableValidationService(browser)
        validation.click_number_in_order(1)
        page_obj.click_restart()
        assert validation.get_next_expected_number() == "1"
