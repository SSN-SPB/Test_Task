import re


test_txt = "You find 1989 and final act is 2025"


def main():
    fount_text_list = re.findall(r'\d+', test_txt)
    print(fount_text_list)
    assert fount_text_list == ['1989', '2025']


if __name__ == "__main__":
    main()
