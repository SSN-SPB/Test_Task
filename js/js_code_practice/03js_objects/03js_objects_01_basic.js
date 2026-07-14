// Object in javascript is a collection of key-value pairs. Each key is a string (or symbol)
// and each value can be any data type, including other objects.

const user = {
  name: "John",
  age: 37,
  address: "Madrid",
};

// js objects can be nested, meaning that an object can contain another object as a value.
// This allows for more complex data structures and better organization of related data.
const person = {
  name: "John",
  age: 37,
  address: {
    city: "Madrid",
    index: 39007,
  },
};

console.log(person.name);
console.log(person.age);
console.log(person.address.city);
console.log(person.address.index);
