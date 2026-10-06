const user = {
  name: "John",
  age: 31,
  city: "London",
};

const userOne = Object.entries(user);

for (const [key, value] of Object.entries(user)) {
  console.log(`${key} - ${value}`);
}

for (const entry of userOne) {
  console.log(entry[0], entry[1]);
}

function userDetails(entry) {
  console.log("via function");
  return `${entry[0]}, ${entry[1]}`;
}
for (entry of userOne) {
  console.log(userDetails(entry));
}
