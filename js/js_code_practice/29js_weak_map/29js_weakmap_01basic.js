// WeakMap is a collection of key/value pairs in which the keys are weakly referenced.
//This means that if there are no other references to the key object,
//it can be garbage collected, and the entry in the WeakMap will be removed automatically.
//WeakMaps are useful for storing private data associated with objects without preventing
//those objects from being garbage collected.


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
