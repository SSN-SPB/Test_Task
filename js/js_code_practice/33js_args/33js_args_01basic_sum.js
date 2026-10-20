const assert = require("node:assert");

function sumOfArguments(...args) {
  return args.reduce((acc, nextArgument) => acc + nextArgument);
}

console.log(sumOfArguments(7, 3, 5));
assert.strictEqual(15, sumOfArguments(7, 3, 5));
console.log(sumOfArguments(71, 3, 5));
assert.strictEqual(79, sumOfArguments(71, 3, 5));
