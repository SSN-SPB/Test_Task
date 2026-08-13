import { testData } from "../../serviceData/dataToTest.js";

describe("Parameterized Cypress test to check method that sums two integers", () => {
  testData.forEach(({ x, y, expected }) => {
    it(`Check ${x} + ${y} == ${expected}`, () => {
      expect(x + y).to.equal(expected);
    });
  });
});
