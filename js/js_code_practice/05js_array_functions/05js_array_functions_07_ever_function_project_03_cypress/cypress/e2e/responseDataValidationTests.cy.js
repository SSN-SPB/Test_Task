import { responses } from "../../testArrayData.js";
import { isCode200, isCode201 } from "../../checkingFunction.js";

describe("Response code validation", () => {
  it("Ensure response codes are less then 300", () => {
    console.log("Check response codes:");

    const result = responses.every((response) => response.status < 300);

    console.log("All responses have status < 300:", result);

    expect(result).to.be.true;
  });

  it("The first user has status 200", () => {
    console.log("Check response codes:");

    const result = responses[0].status === 200;

    console.log("The first user have status 200:", result);

    expect(result).to.be.true;
  });

  it("The last user has status 201", () => {
    console.log("Check response codes:");

    const result = responses[3].status === 201;

    console.log("The last user have status 201:", result);

    expect(result).to.be.true;
  });
});
