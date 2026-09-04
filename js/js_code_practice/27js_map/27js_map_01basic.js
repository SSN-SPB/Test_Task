// new Map() in JavaScript is a built-in object that allows you to store key-value pairs.
// It provides methods to add, retrieve, and delete entries,
// as well as to iterate over the keys and values.
// Unlike regular objects, Maps can have keys of any type, including objects and functions.
const testMap = new Map();
const test_keys = ["a", "b", "c"];
const test_keys2 = ["a", "c"];

console.log(test_keys);
console.log(testMap);

test_keys.forEach((key, val) => testMap.set(key, val + 1));

console.log(test_keys);
console.log(testMap);

const result = test_keys
  .filter((key) => testMap.has(key))
  .map((key) => testMap.get(key) * 3);
const result2 = test_keys2
  .filter((key) => testMap.has(key))
  .map((key) => testMap.get(key) * 3);

console.log(test_keys);
console.log(testMap);
console.log(result);
console.log(result2);
