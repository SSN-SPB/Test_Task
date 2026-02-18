# zfill() method of string objects is used to pad a numeric string on the left with zeros until it reaches the specified width. If the original string is longer than the specified width, it will be returned unchanged.
tested_list = ["42", "7", "1234", "0", "-5"]


def main():
    for s in tested_list:
        print(f"Original: '{s}' | zfill(5): '{s.zfill(5)}' | zfill(3): '{s.zfill(3)}' | zfill(2): '{s.zfill(2)}'")
    tested_list[0].zfill(7) == "0000042"
    tested_list[4].zfill(3) == "-05"


if __name__ == "__main__":
    main()
