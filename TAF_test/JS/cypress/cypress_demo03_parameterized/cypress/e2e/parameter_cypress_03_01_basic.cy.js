import { testData } from "../../serviceData/dataToTest.js";
import { sumOfTwo } from "../../testedFunctions/testedFunctions_sums.js";

describe("Parameterized Cypress test to check method that sums two integers", () => {
  testData.forEach(({ x, y, expected }) => {
    it(`Check ${x} + ${y} == ${expected}`, () => {
      expect(sumOfTwo(x, y)).to.equal(expected);
      //      expect(x + y).to.equal(expected);
    });
  });
});
