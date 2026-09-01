const tested_array = [1, 4, 3, 9, 11, 23, 35];

function get_sorted_copy_of_array(arr, ascending = true) {
  if (ascending) {
    return arr.toSorted((a, b) => a - b);
  }
  return arr.toSorted((a, b) => b - a);
}

const sorted_copy = get_sorted_copy_of_array(tested_array);
const sorted_copy_desc = get_sorted_copy_of_array(tested_array, false);
const sorted_copy_desc2 = get_sorted_copy_of_array(
  tested_array,
  (ascending = false),
);

console.log(sorted_copy);
console.log(sorted_copy_desc);
console.log(sorted_copy_desc2);
