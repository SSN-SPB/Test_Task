const assert = require("node:assert");
function squaresOfDigitsInArray(testedArray) {
  const modifiedArray = testedArray.reduce((acc, val) => {
    acc.push(val ** 2);
    console.log("current value square: " + val ** 2);
    console.log("total " + acc);
    return acc;
  }, []);
  return modifiedArray;
}

console.log(squaresOfDigitsInArray([1, 2, 3]));
assert.deepStrictEqual(squaresOfDigitsInArray([1, 2, 3]), [1, 4, 9]);
