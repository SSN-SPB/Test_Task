input_string = "How are you?"


def reverse_statement(test_statement):
    input_string.split()
    tested_list = test_statement.split()[::-1]
    print(tested_list)
    result_statement = ""
    for x in tested_list:
        result_statement = result_statement + x + " "
    return result_statement[:-1]


def main():
    print("," + reverse_statement(input_string) + ",")
    assert "you? are How" == reverse_statement(input_string)


if __name__ == "__main__":
    main()
