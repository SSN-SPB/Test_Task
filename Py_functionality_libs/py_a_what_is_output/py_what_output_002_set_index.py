var = {
    "a1",
    "a2",
    "a3",
}


def main():
    print(type(var))
    try:
        print(var[1])
    except TypeError as e:
        print(f"Set no index: {e}")


if __name__ == "__main__":
    main()
