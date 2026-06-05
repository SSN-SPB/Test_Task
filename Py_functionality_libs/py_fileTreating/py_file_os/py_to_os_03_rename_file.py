# This code demonstrates renaming a file using
# the os library in Python.
# The file_rename function takes two arguments:
# the old name of the file and the new name.
# It uses os.rename to rename the file
# and handles potential exceptions that
# may occur during the renaming process,
# such as FileNotFoundError
# if the old file does not exist.
# The main function demonstrates how to use the
# file_rename function to rename a file and then rename
# it back to its original name.

import os


def file_rename(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    except FileNotFoundError:
        print(f"File {old_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    file_rename("file_to_modify.txt", "file_to_modify_renamed.txt")
    file_rename("file_to_modify_renamed.txt", "file_to_modify.txt")


if __name__ == "__main__":
    main()
