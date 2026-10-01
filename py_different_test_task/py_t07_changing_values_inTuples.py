def main():
    a = 5
    b = [5]
    test_tuple = (a, b)
    a = 7
    b.append(7)
    print(a)
    print(b)
    print(test_tuple[1] is b)
    print(test_tuple[0] is a)
    assert test_tuple == (5, [5, 7])


if __name__ == "__main__":
    main()
