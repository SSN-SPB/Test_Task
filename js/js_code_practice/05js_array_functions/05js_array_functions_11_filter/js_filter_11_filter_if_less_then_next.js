// Target of this snippet is to filter the
//numbers in the array that are less than the next element
const assert = require("node:assert");

const numbers_array = [3, 2, 4, 3, 4, 2, 4];

const moreThanPrevious = numbers_array.filter((a, b, c) => {
  return a < c[b + 1];
});

console.log(moreThanPrevious);
assert.deepStrictEqual(moreThanPrevious, [2, 3, 2]);
assert.notStrictEqual(moreThanPrevious, [2, 3, 2]);
