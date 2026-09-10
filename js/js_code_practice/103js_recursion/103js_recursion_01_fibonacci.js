function fibonacci(n) {
  if (n < 2) return n;
  return fibonacci(n - 2) + fibonacci(n - 1);
}

function getFibonacciList(y) {
  let arr = [];
  for (i = 0; i < y; i++) {
    arr.push(fibonacci(i));
  }
  return arr;
}
const result = fibonacci(7);
console.log(result);
console.log(getFibonacciList(17));
