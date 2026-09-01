const testMap = new Map();
const test_keys = ["a", "b", "c"];

console.log(test_keys);
console.log(testMap);

test_keys.forEach((key, val) => testMap.set(key, val + 1));

console.log(test_keys);
console.log(testMap);
