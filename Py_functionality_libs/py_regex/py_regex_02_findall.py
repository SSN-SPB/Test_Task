#!/usr/bin/env python3
import re

allPatterns = {
    "uppercase": "[A-Z]",
    "lowercase": "[a-z]",
    "numerical_characters": "[0-9]",
    "special_characters": "[, .!?]",
}
stringTest = "ThisIsGeeksforGeeks !, 123"

# uppercase_characters = re.findall(patternAz, string)
# uppercase_characters = re.findall(r"[A-Z]", string)
# lowercase_characters = re.findall(r"[a-z]", string)
# numerical_characters = re.findall(r"[0-9]", string)
# special_characters = re.findall(r"[, .!?]", string)


def check_string(pat, str, descr):
    if re.findall(pat, str):
        print("The {} characters are {}".format(descr, re.findall(pat, str)))
        print(
            "Totally q-ty of: {}"
            " characters is {}".format(descr, len(re.findall(pat, str)))
        )
    else:
        print("not found")


def main():
    for descr, pattern in allPatterns.items():
        check_string(pattern, stringTest, descr)


if __name__ == "__main__":
    main()
