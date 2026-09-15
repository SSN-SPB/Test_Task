const assert = require("node:assert");

let a = 1;
let b = new Number(1);
let c = "1";

console.log(a == b); // true
console.log(a == c); // true
console.log(a === b); // false

assert.notStrictEqual(a, c);
assert.notStrictEqual(a, b);
assert.notDeepStrictEqual(a, b);
assert.notDeepStrictEqual(a, c);

assert(a == b);
assert(a == c);
assert(b == c);
assert(b !== c);
assert(b !== a);
assert(a === a);
