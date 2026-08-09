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

// via JSON.stringify(
console.log(
  JSON.stringify(validate_stage(drivers)) === JSON.stringify(expected_object),
); // true
