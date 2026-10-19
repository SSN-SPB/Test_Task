const assert = require("node:assert");

function sumTestTime(kwargs) {
  return Object.values(kwargs).reduce((acc, duration) => acc + duration);
}

const testDuration = {
  login: 2,
  search: 15,
  adding: 7,
  checkout: 9,
  payment: 16,
};

console.log(sumTestTime(testDuration));
assert.strictEqual(49, sumTestTime(testDuration));
