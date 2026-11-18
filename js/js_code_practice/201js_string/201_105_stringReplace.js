const assert = require("node:assert");

const testString = "  Hello, Terve!  ";

const result = testString.replace("!", "???");

console.log(result);

assert.deepStrictEqual(result, "  Hello, Terve???  ");
