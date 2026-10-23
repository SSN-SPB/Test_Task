const assert = require("node:assert");

const numbers_array = [1, 2, 3, 4, 5];

const operations = {
  filterEven: (test_list) => test_list.filter((n) => n % 2 === 0),
  mapTwo: (test_list) => test_list.map((n) => n * 2),
  reduceN: (test_list) => test_list.reduce((acc, n) => acc + n, 0),
};

console.log(operations.filterEven(numbers_array));
console.log(operations.mapTwo(numbers_array));
console.log(operations.reduceN(numbers_array));

assert.deepStrictEqual(operations.filterEven(numbers_array), [2, 4]);
assert.deepStrictEqual(operations.mapTwo(numbers_array), [2, 4, 6, 8, 10]);
assert.deepStrictEqual(operations.reduceN(numbers_array), 15);
