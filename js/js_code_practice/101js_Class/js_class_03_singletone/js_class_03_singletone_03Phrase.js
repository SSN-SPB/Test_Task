class Sentence {
  static instance = null;

  constructor() {
    if (Sentence.instance) {
      return Sentence.instance;
    }
    this.statement = "";
    Sentence.instance = this;
  }
  addWord(newWord) {
    this.statement = this.statement.concat(" ", newWord);
  }
  getStatement() {
    return this.statement;
  }
}

phraseOne = new Sentence();
phraseTwo = new Sentence();
console.log(phraseTwo);
phraseOne.addWord("Hello");
console.log(phraseTwo);
phraseTwo.addWord("Word");
console.log(phraseOne);
