# This code demonstrates how to search for files
# in the current directory that match a specific pattern
# (in this case, files with a .txt extension)
# using the pathlib library.
from pathlib import Path


def main():
    print("Hello File")
    list_of_txt_files = Path(".").glob("*.txt")
    for found_file in list_of_txt_files:
        print(found_file)


if __name__ == "__main__":
    main()
