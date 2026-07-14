import { findFailedTest } from "./findFailedTest.js";
import { testCases } from "./testCasesData.js";

// find 1st value
const failedTest = testCases.find(findFailedTest);
console.log(failedTest);

// filter find all values
const allFailedTest = testCases.filter(findFailedTest);
console.log(allFailedTest);
