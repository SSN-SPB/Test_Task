// reduceRight() method executes a reducer function (that you provide)
// on each element of the array, from right to left, resulting
// in a single output value. The reduceRight() method does not
// execute the function for empty array elements.
const assert = require("node:assert");
let expected_array = [[18], [24], [15], [27]];

function toArray(x) {
  return [x];
}

const matrix = [
  [5, 9],
  [6, 8],
];
const result = matrix.reduceRight(
  (acc, elem) => acc.concat(elem.map((num) => toArray(num * 3))), // via function
  //  (acc, elem) => acc.concat(elem.map((num) => [num * 3])),
  [],
);

console.log(result);
assert.deepStrictEqual(result, expected_array);
assert.notStrictEqual(result, expected_array);
