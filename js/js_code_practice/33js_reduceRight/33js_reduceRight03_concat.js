// reduceRight() method executes a reducer function (that you provide)
// on each element of the array, from right to left, resulting
// in a single output value. The reduceRight() method does not
// execute the function for empty array elements.

const matrix = [
  [5, 9],
  [6, 8],
];
const result = matrix.reduceRight(
  (acc, elem) => acc.concat(elem.map((num) => num * 3)),
  [],
);

console.log(result);
