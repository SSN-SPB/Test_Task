// var existed before ES6 (2015).

// Characteristics:

// function scoped
// can be reassigned
// can be redeclared
// var in global scope is attached to the window object

var name = "John";
var name = "Tom"; // it is example of redeclaring the variable
name = "Magdalena"; // it is example of reassigning the variable
console.log("name is", { name });
