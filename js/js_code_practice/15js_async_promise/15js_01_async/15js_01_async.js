const age = 18;
console.log(age);

const age_two = 19;
console.log(age == age_two);
const age_three = "19";
console.log("Check ==");
console.log(age_three == age_two);
console.log("Check ===");
console.log(age_three === age_two);

const compareAge = (a, b) => {
  return a < b;
};

console.log("Check compareAge");
console.log(compareAge(age_two, age));

async function test_async() {
  console.log("Start");
  await console.log(compareAge(age_two, age));
  console.log("End");
}

test_async();
