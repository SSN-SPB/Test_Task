function* range(start, end) {
  while (start < end) {
    yield start++;
  }
}

const viewOne = [...range(10, 15)];

function* pipeline() {
  (yield* range(100, 107), yield* range(10, 17));
}
const viewTwo = [...pipeline()];

console.log(viewOne);
console.log(viewTwo);
