import re


test_txt = "You find 1989 and final now is 2025, yes"


def main():
    found_digits = re.findall(r"\d+", test_txt)
    found_up2_3_letters_words = re.findall(r"\b\w{2,3}\b", test_txt)

    print(found_digits)
    print(found_up2_3_letters_words)
    assert found_digits == ["1989", "2025"]
    assert found_up2_3_letters_words == ["You", "and", "now", "is", "yes"]


if __name__ == "__main__":
    main()
