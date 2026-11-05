const assert = require("node:assert");

const numbers_array = [1, 2, 3, 4, 5];

const operations = {
  filterEven: (test_list) => test_list.filter((n) => n % 2 === 0),
  mapTwo: (test_list) => test_list.map((n) => n * 2),
  sumOfList: (test_list) => test_list.reduce((acc, n) => acc + n, 0),
};

console.log(operations.filterEven(numbers_array));
console.log(operations.mapTwo(numbers_array));
console.log(operations.sumOfList(numbers_array));

assert.deepStrictEqual(operations.filterEven(numbers_array), [2, 4]);
assert.deepStrictEqual(operations.mapTwo(numbers_array), [2, 4, 6, 8, 10]);
assert.deepStrictEqual(operations.sumOfList(numbers_array), 15);

// The `pipeline` function takes multiple functions as arguments and
// returns a new function that applies those functions in sequence to a given value.
const pipeline =
  (...fns) =>
  (value) =>
    fns.reduce((acc, fn) => fn(acc), value);

const notOdd = (test_list) => operations.filterEven(test_list);
const mapTwo = (test_list) => operations.mapTwo(test_list);
const sumForList = (test_list) => operations.sumOfList(test_list);

const transform_initial = pipeline(notOdd, mapTwo);
const transform_final = pipeline(transform_initial, sumForList);
console.log(transform_initial(numbers_array));
console.log(transform_final(numbers_array));
assert.deepStrictEqual(transform_initial(numbers_array), [4, 8]);
assert.deepStrictEqual(transform_final(numbers_array), 12);
