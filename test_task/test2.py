from substring_package import substring_by_index, substring_by_index_start_stop


def main():
    print(substring_by_index("a1b2c3d4e5", 3))
    print(substring_by_index_start_stop("a1b2c3d4e5", 3, 9))
    print("a1b2c3d4e5"[3:7:])


if __name__ == "__main__":
    main()
