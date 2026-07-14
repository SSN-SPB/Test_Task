const user2 = {
  id: 123,
  name: "John",
  age: 39,
  active: true,
};

function validate_age(user) {
  if (user.age < 18) {
    throw new Error("User is not adult");
  }
  console.log("User is adult");
}

validate_age(user2);
user2.age = 11;
try {
  validate_age(user2);
} catch (err) {
  console.log(err.name);
  console.log(err.message);
  //  console.log(err.stack);
  console.log("Validation of age has failed");
}
