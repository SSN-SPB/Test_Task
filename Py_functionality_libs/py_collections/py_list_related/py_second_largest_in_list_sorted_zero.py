test_list2 = [10, 121, -7, 11]
n = 4


def second_maximal_in_list(test_list):
    return sorted(test_list)[-2]


def third_maximal_in_list(test_list):
    return sorted(test_list)[-3]


def n_largest_in_list(test_list, y):
    return sorted(test_list)[-y]


def main():
    print(second_maximal_in_list(test_list2))
    print(third_maximal_in_list(test_list2))
    print(n_largest_in_list(test_list2, n))
    try:
        assert 11 == second_maximal_in_list(test_list2)
        assert 10 == third_maximal_in_list(test_list2)
        assert -7 == n_largest_in_list(test_list2, n)
        print("Checking has passed")
    except AssertionError as ae:
        print("Assert has failed" + ae.args)


if __name__ == "__main__":
    main()
