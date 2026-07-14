// Object in javascript is a collection of key-value pairs. Each key is a string (or symbol)
// and each value can be any data type, including other objects.

const user = {
  name: "John",
  age: 37,
  country: "Spain",
  address: {
    city: "London",
  },
};

const copied_user = structuredClone(user)


console.log(user);
console.log(copied_user);
copied_user.name = "Tom";
console.log(user);
console.log(copied_user);
copied_user.address.city = "Paris"; // shallow copy parent object is not updated for nested value
console.log(user);
console.log(copied_user);