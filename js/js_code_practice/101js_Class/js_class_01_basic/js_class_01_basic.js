class Calculator {
  constructor(value) {
    this.value = value;
  }

  addNum(num) {
    this.value += num;
    return this;
  }

  getValue = () => this.value;
}

const unitOne = new Calculator(10);
console.log(unitOne);

unitOne.addNum(5);
console.log(unitOne.getValue());
