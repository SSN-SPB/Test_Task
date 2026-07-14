// let - Introduced in ES6.

// block scoped
// can be reassigned
// cannot be redeclared in the same scope

let name = "John";
name = "Magdalena"; // it is example of reassigning the variable
console.log("name is", { name });
//let name = "John"; SyntaxError: Identifier 'name' has already been declared
