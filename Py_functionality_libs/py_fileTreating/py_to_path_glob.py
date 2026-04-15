from pathlib import Path

def main():
    print("Hello File")
    list_of_txt_files = Path(".").glob("*.txt")
    for found_file in list_of_txt_files:
        print(found_file)


if __name__ == "__main__":
    main()
