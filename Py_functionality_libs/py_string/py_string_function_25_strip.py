# This scirpt demonstrates the use of the strip() method to removes
# ALL occurrences of chars of substring from both sides of string untill
# it finds a char that is not in the chars list.
#
# It does not remove the substring, but rather any of the characters
# in the substring from both ends of the string


def trim_ending(name: str, ending: str):
    return name.strip(ending)


def main():
    print(trim_ending("filename.txt", ".tx"))
    print(trim_ending("report.txt", ".tx"))
    print(trim_ending("test_report.txt", ".tx"))
    assert trim_ending("filename.txt", ".tx") == "filename"
    assert trim_ending("report.txt", ".tx") == "repor"
    assert trim_ending("test_report.txt", ".tx") == "est_repor"


if __name__ == "__main__":
    main()
