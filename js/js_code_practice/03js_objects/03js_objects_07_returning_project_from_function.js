function create_user(name, age) {
  return {
    name: name,
    age: age,
  };
}
const user = create_user("Tom", 29);

console.log(user);
