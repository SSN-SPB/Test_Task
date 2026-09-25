let a = 5;
console.log(a);
function printOutVar() {
  console.log(a);
  let a = 7;
}
try {
  printOutVar();
} catch (error) {
  console.log("ReferenceError:");
  console.log(`Error name: ${error.name}`);
  console.log(`Error message: ${error.message}`);
  console.log(`Error code: ${error.code}`);
}
