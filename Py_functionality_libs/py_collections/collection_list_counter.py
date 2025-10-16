from collections import Counter

list_a = ["a", "a1", "a2"]
expected_value = Counter(list_a)


def main():
    print(expected_value["a1"])
    assert expected_value["a1"] == 1
    assert expected_value["a3"] == 0


if __name__ == "__main__":
    main()
