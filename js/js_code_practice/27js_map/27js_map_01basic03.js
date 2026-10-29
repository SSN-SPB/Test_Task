// map in javascript is a method that creates a new array populated
// with the results of calling a provided function
// on every element in the calling array.
const asserts = require("node:assert");

const testArray = [1, 3, 7, 2, 10, 11, 2];

const defineEven = (element) => element % 2 === 0;

const checkingList = testArray.map(defineEven);

console.log(checkingList);

asserts.deepStrictEqual(checkingList, [
  false,
  false,
  false,
  true,
  true,
  false,
  true,
]);
