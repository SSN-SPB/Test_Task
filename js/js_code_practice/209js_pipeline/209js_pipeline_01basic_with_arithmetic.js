// This code demonstrates pipelining of functions in JavaScript.
// It defines a `pipeline` function that takes multiple functions
// as arguments and returns a new function that applies those functions
// in sequence to a given value.
const assert = require("node:assert");

const operations = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
  divide: (a, b) => a / b,
};

assert.deepStrictEqual(operations.add(3, 5), 8);

// The `pipeline` function takes multiple functions as arguments and
// returns a new function that applies those functions in sequence to a given value.
const pipeline =
  (...fns) =>
  (value) =>
    fns.reduce((acc, fn) => fn(acc), value);

const double = (x) => operations.multiply(x, 2);
const decreaseTwo = (x) => operations.subtract(x, 2);
const addFive = (x) => operations.add(x, 5);
const increaseFive = (x) => operations.multiply(x, 5);

const transform_negative = pipeline(double, decreaseTwo);
const transform_positive = pipeline(addFive, increaseFive);
const transform = pipeline(transform_negative, transform_positive);
console.log(transform_negative(15));
console.log(transform_positive(28));
console.log(transform(15));
assert.deepStrictEqual(transform(15), 165);
