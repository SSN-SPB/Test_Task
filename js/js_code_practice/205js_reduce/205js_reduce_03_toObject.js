const assert = require("node:assert");
testArray = [3, 11, 35, 1, 247];

const result = testArray.reduce((acc, val) => {
  acc[val] = val + 7;
  return acc;
}, {});

console.log(result);

assert.deepStrictEqual(result, { 1: 8, 3: 10, 11: 18, 35: 42, 247: 254 });
