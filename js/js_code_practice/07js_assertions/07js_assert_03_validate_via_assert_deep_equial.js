const assert = require('node:assert/strict');
const drivers = [
  { name: "John", experience: 5 },
  { name: "Tom", experience: 15 },
  { name: "Tim", experience: 25 },
];

const expected_object = [
  { name: "Tom", experience: 15 },
  { name: "Tim", experience: 25 },
];

function validate_stage(persons) {
  selected_persons = persons.filter((person) => person.experience !== 5);
  console.log(selected_persons);
  return selected_persons;
}

assert.deepEqual(validate_stage(drivers), expected_object); // true