function appendWord(string: string, word: string) {
  return `${string} ${word}`;
}
const testString: string = "Hello";

console.log(appendWord(testString, "Word"));
