from pathlib import Path


def main():
    relative_path = Path("Folder with spaces in name/course2_train1.txt")
    absolute_file_path = relative_path.resolve()
    print(absolute_file_path)
    try:
        assert str(absolute_file_path).count("private_git") == 1
    except AssertionError as ae:
        print("Wrong path assertion" + ae)


if __name__ == "__main__":
    main()
