# This script demonstrates that an iterator can only be used once.
# After it has been consumed, it cannot be reused.
# The example uses the `map` function to create an iterator
# that doubles the length of each string in a list.
# When we try to convert the iterator to a list a second time,
# it returns an empty list because the iterator has already been exhausted.
to_test_list = ["apple", "orange", "plum"]


def get_iterator_twice(tested_list: list):
    double_length = map(lambda x: len(x) * 2, tested_list)
    # print(type(double_length))
    # print(dir(double_length))
    # print(dir(double_length.__init__()))
    # print(double_length.__init__())
    double_length_list = list(double_length)
    # iterator is used and empty now
    double_length_list_second = list(double_length)
    return double_length_list, double_length_list_second


def main():
    result, result_two = get_iterator_twice(to_test_list)
    print(result)
    print(result_two)


if __name__ == "__main__":
    main()
