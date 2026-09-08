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
