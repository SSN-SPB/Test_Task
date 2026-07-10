// Object in javascript is a collection of key-value pairs. Each key is a string (or symbol)
// and each value can be any data type, including other objects.

const users = [
  { name: "John", age: 37, address: "Madrid" },
  { name: "Tom", age: 39, address: "Barcelona" },
  { name: "Pablo", age: 31, address: "Leon" },
];

function display_names(user) {}
let len = users.length;

for (let i = 0; i < len; i++) {
  console.log(users[i].name);
}
