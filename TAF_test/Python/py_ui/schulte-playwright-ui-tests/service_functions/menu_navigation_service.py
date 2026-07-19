from logger.logger import Logger
from page_objects.left_menu_pages.eight_by_eight_page import EightByEightPage
from page_objects.left_menu_pages.five_by_five_page import FiveByFivePage
from page_objects.left_menu_pages.four_by_four_page import FourByFourPage
from page_objects.left_menu_pages.nine_by_nine_page import NineByNinePage
from page_objects.left_menu_pages.seven_by_seven_page import SevenBySevenPage
from page_objects.left_menu_pages.six_by_six_page import SixBySixPage
from page_objects.left_menu_pages.three_by_three_page import ThreeByThreePage


class MenuNavigationService:
    BASE_URL = "https://schultetable.web.app"
    BOARD_SELECTOR = ".board-container"

    def __init__(self, page, logger=None):
        self.page = page
        self.logger = logger or Logger()

    def _navigate_to_size(self, size_label):
        self.logger.info(f"Navigating to {size_label}")
        self.page.goto(self.BASE_URL)
        self.page.locator(f"button.size:has-text('{size_label}')").click()
        self.page.locator(self.BOARD_SELECTOR).wait_for()

    def navigate_to_three_by_three(self):
        self._navigate_to_size("3x3")

    def navigate_to_four_by_four(self):
        self._navigate_to_size("4x4")

    def navigate_to_five_by_five(self):
        self._navigate_to_size("5x5")

    def navigate_to_six_by_six(self):
        self._navigate_to_size("6x6")

    def navigate_to_seven_by_seven(self):
        self._navigate_to_size("7x7")

    def navigate_to_eight_by_eight(self):
        self._navigate_to_size("8x8")

    def navigate_to_nine_by_nine(self):
        self._navigate_to_size("9x9")

    @staticmethod
    def return_selected_grid(browser, page_number):
        if page_number == 3:
            page_obj = ThreeByThreePage(browser)
        elif page_number == 4:
            page_obj = FourByFourPage(browser)
        elif page_number == 5:
            page_obj = FiveByFivePage(browser)
        elif page_number == 6:
            page_obj = SixBySixPage(browser)
        elif page_number == 7:
            page_obj = SevenBySevenPage(browser)
        elif page_number == 8:
            page_obj = EightByEightPage(browser)
        elif page_number == 9:
            page_obj = NineByNinePage(browser)
        else:
            raise ValueError(f"Unsupported page number: {page_number}")
        page_obj.load()
        return page_obj


# def load_three_by_three(browser):
#     page_obj = ThreeByThreePage(browser)
#     page_obj.load()
#     return page_obj
