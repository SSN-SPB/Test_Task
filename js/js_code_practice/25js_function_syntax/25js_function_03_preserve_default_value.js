// function below does not allow modifying only some of the values,
function getSumOfValues(a = 1, b = 2, c = 3) {
  console.log(`${a}_${b}_${c}`);
  return a + b + c;
}

console.log("Default values: 1, 2, 3");
console.log(getSumOfValues());
console.log("All values modified: 111, 112, 113");
console.log(getSumOfValues(111, 112, 113));
console.log("All values modified by position, not by parameter: 11, 12, 13");
console.log(getSumOfValues((c = 11), (a = 12), (b = 13)));
console.log(getSumOfValues((b = 12), (c = 13)));

// function below allow modifying only some of the values,
// while preserving the default values for the rest
console.log("function below allow modifying only some of the values,");
console.log("while preserving the default values for the rest");
function getSumOfValuesEnhanced({ a = 1, b = 2, c = 3 } = {}) {
  console.log(`${a}_${b}_${c}`);
  return a + b + c;
}
console.log("Default values: 1, 2, 3");
console.log(getSumOfValuesEnhanced());
console.log("a: 11 modified, b and c preserved: 11, 2, 3");
console.log(getSumOfValuesEnhanced({ a: 11 }));
console.log("modified, b: 13 modified, c preserved: 12, 13, 3");
console.log(getSumOfValuesEnhanced({ b: 12 }));
console.log(
  "modified, a: 199 modified, b: 12 modified, c preserved: 199, 12, 3",
);
console.log(getSumOfValuesEnhanced({ b: 12, a: 199 }));
console.log("modified, a: 12 modified, b: 13 modified, c preserved: 12, 13, 3");
console.log(getSumOfValuesEnhanced({ b: 13, a: 12 }));
