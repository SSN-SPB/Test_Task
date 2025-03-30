# if


def main():
    i = input("Type 'a' or 'b'\n here  ")
    depended_variable = 7 if i == "a" else 9
    print(f"Selected version is {depended_variable}")


if __name__ == "__main__":
    main()
