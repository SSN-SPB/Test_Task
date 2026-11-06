const assert = require("node:assert");
function sumSquaresOfArrayDigits(testedArray) {
  const totalSum = testedArray.reduce((acc, val) => {
    acc = acc + val ** 2;
    console.log("current value square: " + val ** 2);
    console.log("total " + acc);
    return acc;
  });
  return totalSum;
}

console.log(sumSquaresOfArrayDigits([1, 2, 3]));
assert(sumSquaresOfArrayDigits([1, 2, 3]) === 14);
