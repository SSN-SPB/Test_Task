const user = {
  name: "John",
  age: 37,
  address: "Madrid",
};
const user2 = {
  name2: "John2",
  age2: 19,
  address2: "Madrid2",
};
const { name, age, address } = user;

console.log(name);
console.log(age);
console.log(address);

const { age2 } = user2;

//console.log(name2);
console.log(age2);
//console.log(address2);
