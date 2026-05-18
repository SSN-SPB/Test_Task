from pathlib import Path


def main():
    file_path = Path("example.txt")
    print(f"File path: {file_path}")
    print(f"Stem: {file_path.stem}")
    print(f"Suffix: {file_path.suffix}")


if __name__ == "__main__":
    main()
