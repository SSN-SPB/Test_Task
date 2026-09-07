// numbers.filter((a, b, numbers) is numbers.filter((element, index_of_element, numbers)
// it means that the first parameter is the element,
// the second parameter is the index of the element,
// and the third parameter is the array itself.
// The filter method creates a new array with all elements that pass
//the test implemented by the provided function.
//In this case, it filters out elements where the sum of the element and its index is less than 7.
assert = require("node:assert");

const numbers = [1, 2, 3, 1, -5, 6, 7, 8, 9, 10];

const filterForTwo = numbers.filter((a, b, numbers) => a + b < 7);
console.log(filterForTwo);

assert.deepStrictEqual(filterForTwo, [1, 2, 3, 1, -5]);
assert.notStrictEqual(filterForTwo, [1, 2, 3, 1, -5]);
