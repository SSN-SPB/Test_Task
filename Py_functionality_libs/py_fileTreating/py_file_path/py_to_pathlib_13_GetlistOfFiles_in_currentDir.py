# This script lists all Python files in the
# current directory using the pathlib module.
from pathlib import Path


def main():
    for x in list(Path(".").glob("*.py")):
        print(x)


if __name__ == "__main__":
    main()
