const assert = require("node:assert");
const object1 = { a: 1, b: 2 };
const object2 = { d: 1, b: 4 };

const mergObj = { ...object1, ...object2 };

console.log(mergObj);

assert.deepStrictEqual(mergObj, { a: 1, b: 4, d: 1 });
