const weakMap = new WeakMap();
console.log(weakMap);
const testObj = [{}, {}, {}];
console.log(testObj);

testObj.forEach((key, value) => weakMap.set(key, value + 1));
console.log(weakMap);
console.log(testObj);
console.log(testObj[0]);
console.log(weakMap.get(testObj[0]));

for (let i = 0; i < testObj.length; i++) {
  console.log(weakMap.get(testObj[i]));
}
const result = testObj
  .filter((key) => weakMap.has(key))
  .map((key) => weakMap.get(key) * weakMap.get(key));

console.log(result);
