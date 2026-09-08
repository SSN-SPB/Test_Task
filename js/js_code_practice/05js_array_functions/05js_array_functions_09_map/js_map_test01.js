// Target of this snippet is to create a new array
// that contains the sum of each element and the
// previous element in the original array.

const assert = require("node:assert");

const numbers_array = [3, 2, 4, 3, 2, 4];

const sumOfTwo = numbers_array
  .map((a, b, c) => {
    return a + c[b - 1];
  })
  .slice(1);

console.log(sumOfTwo);
assert.deepStrictEqual([5, 6, 7, 5, 6], sumOfTwo);
