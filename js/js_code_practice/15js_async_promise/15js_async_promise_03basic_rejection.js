const login_success = new Promise((resolve, reject) => {
  setTimeout(() => {
    const login_result = false;
    if (login_result) {
      resolve("login_success");
    } else {
      resolve("Invalid password");
    }
  }, 3000);
});

login_success
  .then((message) => console.log(message))
  .catch((error) => console.log(error));

console.log("programm continues e.g.");
const numbers = [1, 2, 3, 4, 5];
const sliced_numbers = [...numbers.slice(1, 3)];
console.log(numbers); // [ 1, 2, 3, 4, 5 ]
console.log(sliced_numbers); // [ 2, 3 ]
