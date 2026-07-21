import assert from "node:assert";
import { responses } from "./testArrayData.js";
import { isCode200 } from "./checkingFunction.js";

console.log("check response codes:");
console.log(responses.every(isCode200));

const result = responses.every(isCode200);
try {
  assert.ok(result, "The checking of 200 response code is passed");
  console.log("The test passes");
} catch {
  console.log("The test fails");
}
