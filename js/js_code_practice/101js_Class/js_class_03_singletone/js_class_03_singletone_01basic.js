class Calculator {
  static instance = null;

  constructor() {
    if (Calculator.instance) {
      return Calculator.instance;
    }
    this.currentValue = 0;
    Calculator.instance = this;

  }
    addingValue (increasing) {
    this.currentValue = this.currentValue + increasing
    }
  increasing() {
    this.currentValue++;
  }
  getCurrentValue() {
    return this.currentValue;
  }
}
calculatorOne = new Calculator();
calculatorThree = new Calculator();
calculatorOne.increasing();
calculatorTwo = new Calculator();

console.log(calculatorOne);
console.log(calculatorTwo);
console.log(calculatorThree);
console.log(calculatorThree.currentValue);
console.log(calculatorThree.getCurrentValue());
calculatorTwo.addingValue(7);
console.log(calculatorThree);
