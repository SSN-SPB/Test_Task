// The variable cannot point to another object, but the object's contents can change.

const person = { name: 'John' }

console.log(person)

person.name = "Tom" // it is example of changing the content of the object
console.log(person)


