const numbers = [1, 2, 3, 4, 5, 6, 7];

const less_then_two = numbers.filter((numbers) => {
  return numbers < 2;
});
const odd_numbers = numbers.filter((numbers) => {
  return numbers % 2 === 0;
});

const divided_by_three = numbers.filter((numbers) => numbers % 3 === 0);

console.log(numbers);
console.log(less_then_two);
console.log(odd_numbers);
console.log(divided_by_three);
