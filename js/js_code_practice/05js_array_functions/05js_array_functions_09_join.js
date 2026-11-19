// This function takes an array as an argument and returns a string with the array elements joined by " | ".
const assert = require("node:assert");

function returnJoined(testedArray) {
  const resultString = testedArray.join(" | ");
  return resultString;
}

console.log(returnJoined([7, 9, 11]));
console.log(typeof returnJoined([7, 9, 11]));

assert.deepStrictEqual(returnJoined([7, 9, 11]), "7 | 9 | 11");
