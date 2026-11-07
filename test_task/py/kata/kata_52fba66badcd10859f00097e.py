# https://www.codewars.com/kata/52fba66badcd10859f00097e
def disemvowel(string_):
    result_string = ""
    for x in string_:
        # if x not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        if x.lower() not in "aeiou":
            result_string += str(x)
    return result_string


def main():
    print(disemvowel("Hello world"))
    assert "Hll wrld" == disemvowel("Hello world")


def test_single():
    print(disemvowel("Hello world"))
    assert "Hll wrld" == disemvowel("Hello world")


if __name__ == "__main__":
    main()
