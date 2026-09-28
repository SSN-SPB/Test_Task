function concatenateString(stringToEnhance, newWord) {
  return stringToEnhance.concat(" ").concat(newWord);
}

const testString = "Hello";

console.log(concatenateString(testString, "Word"));
