const assert = require("node:assert");

class Calculator {
  constructor(a, b) {
    this.a = a;
    this.b = b;
  }

  add() {
    return this.a + this.b;
  }

  multiply() {
    return this.a * this.b;
  }
}

calculator = new Calculator(8, 7);

console.log(calculator.multiply());
console.log(calculator.add());
assert(calculator.add() === 15);
assert(calculator.add() == 15);
