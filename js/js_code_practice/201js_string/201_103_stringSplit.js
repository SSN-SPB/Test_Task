const assert = require("node:assert");

const testedText = "  Hello, Word!  ";

const result = testedText.split(", ");

console.log(result);
assert.deepStrictEqual(result, ["  Hello", "Word!  "]);
