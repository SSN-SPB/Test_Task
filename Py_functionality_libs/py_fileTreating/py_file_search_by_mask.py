from pathlib import Path


def find_file_by_mask(target_dir, tested_mask):
    found_files = Path(target_dir).glob(tested_mask)
    print(f"found files for mask {tested_mask} are {list(found_files)}")


def main():
    find_file_by_mask(target_dir="..", tested_mask="*.png")


if __name__ == "__main__":
    main()
