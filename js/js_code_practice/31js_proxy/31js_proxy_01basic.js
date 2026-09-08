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
