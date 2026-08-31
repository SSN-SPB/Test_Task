HELLO_MESSAGE = "Hello word"
FILE_NAME = "tested_file.txt"


def create_file_with_text(content_message: str, name_of_file: str):
    with open(name_of_file, "w+") as new_file:
        new_file.write(content_message)
        cursor_position = new_file.tell()
    new_file.close()
    return cursor_position


def read_file_content(name_of_file: str):
    with open(name_of_file, "r") as current_file:
        for x in current_file:
            print(x)
    current_file.close()


def main():
    total_symbols_in_file = create_file_with_text(HELLO_MESSAGE, FILE_NAME)
    print(total_symbols_in_file)
    read_file_content(FILE_NAME)


if __name__ == "__main__":
    main()
