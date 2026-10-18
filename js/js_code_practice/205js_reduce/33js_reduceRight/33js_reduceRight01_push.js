// this is a simple example of using the reduceRight method to reverse the order of elements
// in a 2D array (matrix) and push them into a new array.
// The reduceRight method iterates over the elements of the matrix from right to left,
// accumulating the elements into a new array.

const assert = require("node:assert");

const matrix = [
  [1, "a", 7],
  [2, "с", 9],
];

const result = matrix.reduceRight((acc, elem) => {
  acc.push(elem);
  return acc;
}, []);

console.log(result);
assert.deepStrictEqual(result, [
  [2, "с", 9],
  [1, "a", 7],
]);
