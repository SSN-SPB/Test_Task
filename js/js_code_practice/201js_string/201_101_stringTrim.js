const assert = require("node:assert");

const testString = "   Hello, World!   ";

const result = testString.trim();

console.log(result);
assert.deepStrictEqual(result, "Hello, World!");
