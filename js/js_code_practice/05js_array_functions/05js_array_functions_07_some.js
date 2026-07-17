// JavaScript some() method is an array method that tests whether at least one element in the
// array passes the test implemented by the provided function.
// It returns a Boolean value (true or false).

const numbers_array = [1, 21, 51, 43, 9, 3, 17];
const numbers_array2 = [1, 2, 5, 4, 9, 3, 1];

const greateThanTen = (number) => number >= 10;

const hasLargeThanTen = numbers_array.some(greateThanTen);
const hasLargeThanTen2 = numbers_array2.some(greateThanTen);

console.log(hasLargeThanTen);
console.log(hasLargeThanTen2);
