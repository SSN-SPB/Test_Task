const user = {
  name: "John",
  age: 37,
  address: "Madrid",
  greet: function () {
    console.log("Hello, " + this.name + "!");
  },
  greet_short() {
    console.log("Hello from " + this.address + "!");
  },
};

user.greet();
user.greet_short();
