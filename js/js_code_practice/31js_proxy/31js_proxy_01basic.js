// Proxy is used to define custom behavior for fundamental operations
// (e.g., property lookup, assignment, enumeration, function invocation, etc).


const assert = require("node:assert");

const person = { name: "John", age: 25 };

const handler = {
  get(obj, prop) {
    if (prop in obj) {
      return obj[prop];
    } else {
      return `property '${prop}' is not found`;
    }
  },
  // The set trap is used to intercept property assignments.
  // In this case, it checks if the value being assigned is a string.
  // If it is, it converts the string to uppercase before assigning it to the property.
  // If the value is not a string, it assigns the value as is.

  set(obj, prop, value) {
    if (typeof value === "string") {
      obj[prop] = value.toUpperCase();
    } else {
      obj[prop] = value;
    }
  },
};

personOne = new Proxy(person, handler);

console.log(personOne.name);
console.log(personOne.country);
// setting new property country with value FINLAND
personOne.country = "finland";
console.log(personOne.country);
assert(personOne.country === "FINLAND");
