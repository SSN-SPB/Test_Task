const user = {
  name: "John",
  age: 37,
  address: "Madrid",
};

for (const key in user) {
  console.log(key + ": " + user[key]);
}

console.log(Object.keys(user));
console.log(Object.values(user));
