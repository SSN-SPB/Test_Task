import shutil


def main():
    shutil.copy("file_to_modify.txt", "file_to_modify_copied.txt")
    print("File is copied successfully")


if __name__ == "__main__":
    main()
