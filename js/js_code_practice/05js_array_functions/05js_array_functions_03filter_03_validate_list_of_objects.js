const drivers = [
  { name: "John", experience: 5 },
  { name: "Tom", experience: 15 },
  { name: "Tim", experience: 25 },
];

selected_persons = drivers.filter((person) => person.experience !== 15);
console.log(selected_persons);

function validate_stage(persons) {
  selected_persons = persons.filter((person) => person.experience !== 5);
  console.log(selected_persons);
  return selected_persons;
}

//
//creates a new array on the right-hand side. Even if both arrays contain identical objects, they are different objects in memory.
//
//For example:
//
//[] === []          // false
//[1, 2] === [1, 2]  // false
console.log(
  validate_stage(drivers) !==
    [
      { name: "Tom", experience: 15 },
      { name: "Tim", experience: 25 },
    ],
); // true
