const assert = require("node:assert");
function squareDigits(num) {
  const arrayOfInt = String(num).split("").map(Number);
  return arrayOfInt;
}

console.log(squareDigits(123));
assert.deepStrictEqual(squareDigits(123), [1, 2, 3]);
