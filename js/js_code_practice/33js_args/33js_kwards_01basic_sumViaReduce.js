// Object.values() method returns an array
// of a given object's own enumerable property values,
// in the same order as that provided by a for...in loop
// (the difference being that a for-in loop enumerates
// properties in the prototype chain as well).


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
