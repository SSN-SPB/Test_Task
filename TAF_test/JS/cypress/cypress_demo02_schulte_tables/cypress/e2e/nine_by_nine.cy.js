import GridPage from "../support/page_objects/grid_page";
import MenuNavigationService from "../support/services/menu_navigation_service";
import TableValidationService from "../support/services/table_validation_service";

describe("9x9 Schulte Table Page", () => {
  const SIZE_LABEL = "9x9";
  const TABLE_SIZE = 81;

  let gridPage;
  let menuService;
  let validationService;

  beforeEach(() => {
    gridPage = new GridPage(SIZE_LABEL, TABLE_SIZE);
    menuService = new MenuNavigationService();
    validationService = new TableValidationService();
  });

  it("should navigate to 9x9 grid", () => {
    menuService.navigateToNineByNine();
    gridPage.isDisplayed();
  });

  it("should have correct cell count", () => {
    gridPage.load();
    gridPage.hasCorrectNumberOfCells();
  });

  it("should contain unique numbers", () => {
    gridPage.load();
    gridPage.hasUniqueNumbers();
  });

  it("should have cell values in range 1 to 81", () => {
    gridPage.load();
    gridPage.getCellValues().then((values) => {
      const actual = new Set(values);
      const expected = gridPage.getExpectedValues();
      expect(actual).to.deep.eq(expected);
    });
  });

  it("should display correct description text", () => {
    gridPage.load();
    gridPage.getDescriptionText().should("contain", "1 to 81");
  });

  it("should show menu button as active", () => {
    gridPage.load();
    gridPage.isActive();
  });

  it("should advance to next number on correct click", () => {
    gridPage.load();
    validationService.getNextExpectedNumber().should("contain", "1");
    validationService.clickNumberInOrder(1);
    validationService.getNextExpectedNumber().should("contain", "2");
  });

  it("should reset game on restart", () => {
    gridPage.load();
    validationService.clickNumberInOrder(1);
    gridPage.clickRestart();
    validationService.getNextExpectedNumber().should("contain", "1");
  });
});
