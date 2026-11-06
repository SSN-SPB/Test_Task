// https://www.codewars.com/kata/546e2562b03326a88e000020/train/javascript
const assert = require("node:assert");
function squareDigits(num) {
  const arrayOfInt = String(num).split("").map(Number);
  const modifiedArray = arrayOfInt.reduce((acc, val) => {
    acc.push(val ** 2);
    return acc;
  }, []);
  return Number(modifiedArray.join(""));
}

console.log(squareDigits(193));
assert.deepStrictEqual(squareDigits(193), 1819);
