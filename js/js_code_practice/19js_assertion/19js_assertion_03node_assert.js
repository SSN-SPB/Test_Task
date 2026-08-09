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
} catch {
  console.log("Checking error");
}
