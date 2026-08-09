const assert = require("node:assert");

try {
  assert(5 == "7");
} catch (error) {
  console.log("Checking error");
  console.log(`Error name: ${error.name}`);
  console.log(`Error message: ${error.message}`);
  console.log(`Error code: ${error.code}`);
  // console.log(`Error stack: ${error.stack}`);
}
