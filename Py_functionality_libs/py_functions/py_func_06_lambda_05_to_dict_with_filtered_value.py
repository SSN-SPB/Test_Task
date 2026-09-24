def main():
    string_for_test = "Petr Petrovich Petrov"
    # The next line select unique letters from the string by filtering
    # them with lambda function from set()
    interim_list = list(
        filter(
            lambda x: string_for_test.count(x) > 1,
            set(string_for_test),
        )
    )
    print(interim_list)
    # The next line creates a dictionary with letters and their
    # counts using map() and lambda function
    new_list = dict(
        map(
            lambda x: (
                x,
                string_for_test.count(x),
            ),
            interim_list,
        )
    )
    print(new_list)


if __name__ == "__main__":
    main()
