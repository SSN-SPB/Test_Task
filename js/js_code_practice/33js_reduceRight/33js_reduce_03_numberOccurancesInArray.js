const assert = require("node:assert");

const nums = [1, 2, 3, 4, 5, 2, 3, 4];

const result = nums.reduce((counts, nums) => {
  counts[nums] = (counts[nums] || 0) + 1;
  // (counts[nums] || 0) - if counts[nums] is undefined, it will use 0 instead
  return counts;
}, {});

assert.deepStrictEqual(result, { 1: 1, 2: 2, 3: 2, 4: 2, 5: 1 });
console.log(result);
