const matrix = [
  [5, 9],
  [6, 8],
];
const result = matrix.reduceRight(
  (acc, elem) => acc.concat(elem.map((num) => num * 3)),
  [],
);

console.log(result);
