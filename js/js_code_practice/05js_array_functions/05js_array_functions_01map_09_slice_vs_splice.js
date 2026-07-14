const numbers = [1, 2, 3, 4, 5];
const numbers2 = [11, 12, 13, 14, 15];

const sliced_numbers = [...numbers.slice(1, 3)];
console.log(numbers); // [ 1, 2, 3, 4, 5 ]
console.log(sliced_numbers); // [ 2, 3 ]
const sliced_numbers5 = [...numbers.slice(31, 33)];
console.log("if slice() out of index");
console.log(sliced_numbers5); // [  ]
console.log(numbers); // [ 1, 2, 3, 4, 5 ]
// splice modifies the original array, so numbers
// will be changed after this operation and includes last element of splice.
console.log("for splice");
const spliced_numbers = [...numbers.splice(1, 3)];
console.log(spliced_numbers); // [ 2, 3, 4 ]
console.log(numbers); // [ 1, 5 ]

// negative index in slice means counting from the end of the array,
// so -1 is the last element, -2 is the second last element, and so on.
console.log("for negative slice");
const sliced_numbers_negative = [...numbers2.slice(-4, -1)];
console.log(numbers2); // [ 11, 12, 13, 14, 15 ]
console.log(sliced_numbers_negative); // [ 12, 13, 14 ]
console.log("for negative slice out of index");
const sliced_numbers_negative2 = [...numbers2.slice(-1, -4)];
console.log(numbers2); // [ 11, 12, 13, 14, 15 ]
console.log(sliced_numbers_negative2); // []
// no elements will be returned if the start index is greater than the end index in slice.
const sliced_numbers_negative3 = [...numbers2.slice(-25, -14)];
console.log(numbers2); // [ 11, 12, 13, 14, 15 ]
console.log(sliced_numbers_negative3); // []
