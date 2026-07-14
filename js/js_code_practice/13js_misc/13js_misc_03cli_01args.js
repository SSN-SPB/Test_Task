// process.argv[0] = node
// process.argv[1] = script name
// process.argv[2] = first user argument

const firstValue = process.argv[2];
console.log("The fileName: " + process.argv[1]);
const scriptName = process.argv[1];
console.log("The full fileName: " + scriptName);
console.log("The input value: " + firstValue);
