const assert = require("node:assert");

function findLeadingZeroes(testString) {
  let counter = 0;

  for (const x of testString) {
    if (x === "0") {
      counter++;
    } else return counter;
  }
  return counter;
}

console.log(findLeadingZeroes("00000Hello"));
console.log(findLeadingZeroes("00000Hello0000"));
console.log(findLeadingZeroes("000000000"));

assert.deepStrictEqual(findLeadingZeroes("00000Hello0000"), 5);
assert.deepStrictEqual(findLeadingZeroes("000000000"), 9);
