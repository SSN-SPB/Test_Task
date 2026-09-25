const assert = require("node:assert");

const textString = "Petr Petrovich Petrov";

const testTextArray = textString.split(" ");

console.log(testTextArray);

assert.deepStrictEqual(testTextArray, ["Petr", "Petrovich", "Petrov"]);
