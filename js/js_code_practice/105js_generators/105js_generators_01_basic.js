const ALPHABET_LENGTH = 26;
const FIRST_LETTER_ALPHABET = 65;

function* generateAlphabet() {
  for (let index = 0; index < ALPHABET_LENGTH; index++) {
    yield String.fromCharCode(FIRST_LETTER_ALPHABET + index);
  }
}

const alphabetGenerator = generateAlphabet();
for (let index = 0; index < 29; index++) {
  console.log(alphabetGenerator.next()["value"]);
}
