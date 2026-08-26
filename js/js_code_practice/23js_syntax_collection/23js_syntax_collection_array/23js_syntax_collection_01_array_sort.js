/*
 * The code contains the function that returns the sorted copy of array
 */

const tested_array = [1, 7, -9, 15, 27];

function sorted_copy_of_array(arr) {
  return arr.toSorted((a, b) => a - b);
}

const sorted_version = sorted_copy_of_array(tested_array);

console.log(sorted_version);
