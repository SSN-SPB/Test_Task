// Object in javascript is a collection of key-value pairs. Each key is a string (or symbol)
// and each value can be any data type, including other objects.

const user = {
  name: "John",
  age: 37,
  address: "Madrid",
};

const copied_user = {
  ...user,
};

console.log(user);
console.log(copied_user);
const enhanced_user = {
  id: 1,
  ...user,
  postal_code: 21285,
};
console.log(enhanced_user);
