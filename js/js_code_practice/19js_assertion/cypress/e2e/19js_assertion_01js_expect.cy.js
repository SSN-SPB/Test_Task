const newString = "All is fine";

const checkStringLength = (testedString) => {
  return testedString.length;
};

console.log(checkStringLength(newString));

describe("Test checks the length of string", () => {
  it("test if length > 10", () => {
    expect(checkStringLength(newString)).to.be.greaterThan(10);
  });
});
