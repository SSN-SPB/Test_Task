// const - Introduced in ES6 as well

// block scoped
// cannot be reassigned
// cannot be redeclared in the same scope

const name = "John"
console.log("name is", {name})
try {
  name = "Tom"
} catch {
  console.log("TypeError: Assignment to constant variable.");
}

