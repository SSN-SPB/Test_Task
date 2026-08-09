const assert = require("node:assert");
const newString = "All is fine";
// to run node .\19js_assertion_03node_assert.js
// Code style
// correct npx prettier --write .
// check npx prettier --check .
const checkStringLength = (testedString) => {
  return testedString.length;
};

console.log(checkStringLength(newString));

try {
  assert(checkStringLength(newString) > 17);
} catch (error) {
  console.log("Checking error");
  console.log(`Error name: ${error.name}`);
  console.log(`Error message: ${error.message}`);
  console.log(`Error code: ${error.code}`);
  // console.log(`Error stack: ${error.stack}`);
}
