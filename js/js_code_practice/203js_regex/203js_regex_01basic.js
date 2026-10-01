const assert = require("node:assert");

const testedString = " 1 a 2 b 3 c 4 d 5 e 07";

function stringRegex(str) {
  const regex = /\d+/g;
  const matches = str.match(regex);
  return matches;
}

const result = stringRegex(testedString);
console.log(result);
console.log(result.length);
assert.strictEqual(result.length, 6);
assert.strictEqual(result[0], '1');
assert.notStrictEqual(result[0], 1);
assert.deepStrictEqual(result[0], '1');
