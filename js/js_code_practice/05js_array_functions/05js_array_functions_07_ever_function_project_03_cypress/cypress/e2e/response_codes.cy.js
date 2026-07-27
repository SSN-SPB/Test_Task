import { responses } from "../../testArrayData.js";
import { isCode200 } from "../../checkingFunction.js";

describe("Response code validation", () => {
  it("Ensure response codes are 200", () => {
    console.log("Check response codes:");

    const result = responses.every(isCode200);

    console.log("All responses have status 200:", result);

    expect(result).to.be.true;
  });

  it("The first user has status 200", () => {
    console.log("Check response codes:");

    const result = responses[0].status === 200;

    console.log("The first user have status 200:", result);

    expect(result).to.be.true;
  });
});
