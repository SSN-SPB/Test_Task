# This script lists all Python files in the
# current directory using the pathlib module.
from pathlib import Path

CURRENT_DIRECTORY = Path.cwd()

list_of_file_names = [
    "test_name_one.txt",
    "test_name_two.txt",
    "test_name_three.txt",
]


def ramp_down_deleting_txt_file():
    for file_name in Path(".").glob("*.txt"):
        if file_name.is_file():
            print(f"To be deleted: {file_name}")
            file_name.unlink()


def main():
    for x in list_of_file_names:
        file_name = CURRENT_DIRECTORY / x
        with file_name.open("a", encoding="utf-8") as file:
            file.write(f"New line into {file_name}")
    for x in list(Path(".").glob("*.txt")):
        print(x)
    ramp_down_deleting_txt_file()


if __name__ == "__main__":
    main()
