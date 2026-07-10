// The variable cannot point to another object, but the object's contents can change.

const person = { name: 'John' }

console.log(person)

person.name = "Tom"
console.log(person)


