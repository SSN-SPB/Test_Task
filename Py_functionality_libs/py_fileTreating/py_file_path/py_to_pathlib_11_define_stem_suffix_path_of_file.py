# This code demonstrates how to use the `pathlib`
# library to define the stem and suffix of a file path.
# The `stem` attribute gives the file name without
# the suffix, while the `suffix`
# attribute provides the file extension.
# The code creates a `Path` object for
# a file named "example.txt"
# and prints the file path, stem, and suffix to the console.
# The file itself does not need to exist for this code to work,
# as it is only manipulating the path as a string.


from pathlib import Path


def main():
    file_path = Path("example.txt")
    print(f"File path: {file_path}")
    print(f"Stem: {file_path.stem}")
    print(f"Suffix: {file_path.suffix}")


if __name__ == "__main__":
    main()
