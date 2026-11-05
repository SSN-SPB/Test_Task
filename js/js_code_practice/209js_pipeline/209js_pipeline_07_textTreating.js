assert = require("node:assert");

const pipe = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args)),
  );

const trimText = (text) => text.trim();
const trimToLowerCase = (text) => text.toLowerCase();
const trimTextReplace = (text) => text.replace(" ", "_");

const updatedText = pipe(trimText, trimToLowerCase, trimTextReplace);

console.log(`check updating ${updatedText("HELlo WoRld")}`);
assert.deepStrictEqual(updatedText("HELlo WoRld"), "hello_world");
