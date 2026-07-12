const download = new Promise((resolve, reject) => {
  console.log("Downloading data");

  setTimeout(() => {
    const success = true;
    if (success) {
      resolve("Downloading completed");
    } else {
      reject("Downloading failed");
    }
  }, 5000);
});

download
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.log(error);
  });

console.log("programm continues e.g.");
const numbers = [1, 2, 3, 4, 5];
const sliced_numbers = [...numbers.slice(1, 3)];
console.log(numbers); // [ 1, 2, 3, 4, 5 ]
console.log(sliced_numbers); // [ 2, 3 ]
