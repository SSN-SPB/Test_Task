import { responses } from "./testArrayData.js";
import { isCode200 } from "./checkingFunction.js";

console.log("check response codes:");
console.log(responses.every(isCode200));
