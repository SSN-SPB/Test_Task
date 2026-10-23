// This script demonstrates basic arithmetic operations using dot notation in JavaScript.
// It defines an object called `operations` that contains methods
// for addition, subtraction, multiplication, and division.
// The script then performs an addition operation and uses the
// `assert` module to verify that the result is as expected.

const assert = require("node:assert");

const operations = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
  divide: (a, b) => a / b,
};

console.log(operations.add(3, 5));
assert.deepStrictEqual(operations.add(3, 5), 8);
