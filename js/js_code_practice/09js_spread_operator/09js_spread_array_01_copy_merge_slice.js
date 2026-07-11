const numbers = [1, 2, 3, 4, 5];
const numbers2 = [11, 12, 13, 14, 15];

const copied_numbers = [...numbers];
console.log(copied_numbers);
const merged_numbers = [...numbers, ...numbers2];
console.log(merged_numbers);
const sliced_copy = [...numbers.slice(0, 3), 7, ...numbers2.slice(-2)];
console.log(sliced_copy);
console.log(numbers);
