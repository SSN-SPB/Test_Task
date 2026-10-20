const assert = require("node:assert");
const expectedSum = 15;

const nums = [1, 2, 3, 4, 5];

const sumOfNums = nums.reduce((acc, value) => {
  return acc + value;
}, 0);

console.log(sumOfNums);
assert.deepStrictEqual(expectedSum, sumOfNums);
assert.strictEqual(expectedSum, sumOfNums);
console.log(expectedSum == sumOfNums);
console.log(expectedSum === sumOfNums);
