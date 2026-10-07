// This code demonstrates different implementations of the map function in JavaScript.
// The map function is used to create a new array by applying a function to each element of an existing array.

const assert = require("node:assert");

const testArray = [1, 3, 5, 4, 1, 21, 17];

const testArrayIncreaseOne = testArray.map((a) => {
  return a + 1;
});
// ES6 arrow function syntax
const testArrayIncreaseTwo = testArray.map((a) => a + 2);

// the function increaseListByN takes an array and a value to increase each element by,
// and returns a new array with the increased values.
function increaseListByN(testlist, valueToIncrease) {
  const increasedList = testlist.map((a) => a + valueToIncrease);
  return increasedList;
}
// or by other format:
const multiplyByN = (testlist, valueToIncrease) =>
  testlist.map((a) => a * valueToIncrease);

console.log(testArrayIncreaseOne);
console.log(testArrayIncreaseTwo);
console.log(increaseListByN(testArray, 5));
console.log(multiplyByN(testArray, 5));
assert.deepStrictEqual(testArrayIncreaseOne, [2, 4, 6, 5, 2, 22, 18]);
assert.deepStrictEqual(testArrayIncreaseTwo, [3, 5, 7, 6, 3, 23, 19]);
