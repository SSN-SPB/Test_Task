// Object in javascript is a collection of key-value pairs. Each key is a string (or symbol)
// and each value can be any data type, including other objects.

const users = [
  { name: "John", age: 37, address: "Madrid" },
  { name: "Tom", age: 39, address: "Barcelona" },
  { name: "Pablo", age: 31, address: "Leon" },
];

users[2].name = "TomNew"; // it is example of changing the content of the object's property

function display_names(user) {
  let len = users.length;

  for (let i = 0; i < len; i++) {
    console.log(user[i]);
  }

  console.log("After removing age");
  for (let i = 0; i < len; i++) {
    delete user[i].age;
    console.log(user[i]);
  }
}
display_names(users);
