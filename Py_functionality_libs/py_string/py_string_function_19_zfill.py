# zfill() method of string objects is used to pad a numeric string
# on the left with zeros until it reaches the specified width.
# If the original string is longer than the specified width,
# it will be returned unchanged.
tested_list = ["42", "78905", "1234", "0", "-5"]


def main():
    for s in tested_list:
        original = f"Original: '{s}'"
        zfill5 = f"zfill(9): '{s.zfill(9)}'"
        zfill3 = f"zfill(3): '{s.zfill(3)}'"
        zfill2 = f"zfill(2): '{s.zfill(2)}'"
        output = f"{original} | {zfill5} | {zfill3} | {zfill2}"
        print(output)
    assert tested_list[0].zfill(7) == "0000042"
    assert tested_list[4].zfill(7) == "-000005"
    tested_list[0].zfill(7) == "0000042"
    tested_list[4].zfill(3) == "-05"


if __name__ == "__main__":
    main()
