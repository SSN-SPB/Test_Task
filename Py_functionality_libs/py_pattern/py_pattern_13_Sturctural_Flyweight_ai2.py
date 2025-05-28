class CharacterFlyweight:
    _flyweights = {}

    def __new__(cls, char, font, size, color):
        key = (char, font, size, color)
        if key not in cls._flyweights:
            cls._flyweights[key] = super(CharacterFlyweight, cls).__new__(cls)
            cls._flyweights[key].char = char
            cls._flyweights[key].font = font
            cls._flyweights[key].size = size
            cls._flyweights[key].color = color
        return cls._flyweights[key]

    def render(self, position):
        print(
            f"Rendering '{self.char}' at {position} with font={self.font}, size={self.size}, color={self.color}"
        )


class Character:
    def __init__(self, char, font, size, color):
        self.char = char
        self.font = font
        self.size = size
        self.color = color

    def render(self, position):
        print(
            f"Rendering '{self.char}' at {position} with font={self.font}, size={self.size}, color={self.color}"
        )


# Client code
if __name__ == "__main__":
    # Rendering the word "HELLO" with the same formatting
    chars = []
    for i, char in enumerate("HELLO"):
        flyweight_char = CharacterFlyweight(char, "Arial", 12, "black")
        flyweight_char.render((i, 0))
        chars.append(flyweight_char)

    # Rendering the word "WORLD" with different formatting
    for i, char in enumerate("WORLD"):
        flyweight_char = CharacterFlyweight(char, "Times New Roman", 14, "blue")
        flyweight_char.render((i, 1))
        chars.append(flyweight_char)

    """Memory Usage:

    Without Flyweight: Memory usage increases linearly with the number of
     characters, as each character, along with its attributes, 
     occupies a unique space in memory.

    With Flyweight: Memory usage is optimized by sharing common data
     among characters with identical attributes, leading to 
     a more efficient use of resources."""

    chars = []
    for i, char in enumerate("HELLO"):
        character = Character(char, "Arial", 12, "black")
        character.render((i, 0))
        chars.append(character)

    # Rendering the word "WORLD" with different formatting
    for i, char in enumerate("WORLD"):
        character = Character(char, "Times New Roman", 14, "blue")
        character.render((i, 1))
        chars.append(character)
