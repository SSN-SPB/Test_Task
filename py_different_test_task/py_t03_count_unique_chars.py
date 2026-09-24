def count_duplicated_letters(test_string: str):
    result = {}
    for i in test_string:
        if test_string.count(i) > 1:
            result[i] = test_string.count(i)
    return result


def main():
    string_for_test = "Petr Petrovich Petrov"
    print(count_duplicated_letters(string_for_test))
    # The next line select unique letters from the string by filtering
    # them with lambda function from set()
    interim_list = list(
        filter(lambda x: string_for_test.count(x) > 1, set(string_for_test))
    )
    print(interim_list)
    # The next line creates a dictionary with letters and their
    # counts using map() and lambda function
    new_list = dict(map(lambda x: (x, string_for_test.count(x)), interim_list))
    print(new_list)


if __name__ == "__main__":
    main()
