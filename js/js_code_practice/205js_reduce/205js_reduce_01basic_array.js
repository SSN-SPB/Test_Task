// This code demonstrates the use of the reduce method in JavaScript
// to create a new array
//by subtracting 1 from each element of the original array.
// The acc is the accumulator that holds the new array being built,
// and val is the current value being processed in the original array.
const testArray = [1, 3, 9, 11, 21];

const result = testArray.reduce((acc, val) => {
  acc.push(val - 1);
  console.log(acc);
  console.log(`acc: ${acc}, val: ${val}`);
  return acc;
}, []);

console.log(result);
