// let - Introduced in ES6.

// block scoped
// can be reassigned
// cannot be redeclared in the same scope

if (true) {
  let y = 15;
  console.log(y);
}

try {
  console.log(y);
} catch {
  console.log("ReferenceError: y is not defined");
}

//let name = "John"; SyntaxError: Identifier 'name' has already been declared
