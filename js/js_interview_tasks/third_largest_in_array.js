/**
 * Write a JS program to find the 3d largest number in an array
 */

const tested_array = [1, 7, 5, -3, 9];
const tested_array_two = [1, 7, 3, -3, 9];

function find_third_largest_in_array(arr) {
  const sorted_array = arr.toSorted((a, b) => a - b);
  return sorted_array[2];
}

const found_third = find_third_largest_in_array(tested_array);
const found_third_two = find_third_largest_in_array(tested_array_two);

console.log(found_third);
console.log(found_third_two);
