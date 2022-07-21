class TaskPartTwo(object):
    def largestNumber(self, s):
        largest_number = 0
        interim_string = ''
        for x in s:
            if x.isdigit():
                interim_string = interim_string + x
                if int(interim_string) > largest_number:
                    largest_number = int(interim_string)
            else:
                interim_string = ''
        return largest_number


def check_result(input_string, expected_value):
    version = TaskPartTwo()
    result = version.largestNumber(input_string)
    if result == expected_value:
        print('Test passes with result value {}'.format(result))
    else:
        print('Fails result: {} expected: {}'.format(result, expected_value))


def main():
    check_result('ab12cab$%^^cbb', 12)
    check_result('ab12cab13cbb', 13)
    check_result('ab125cab13cbb', 125)
    check_result('ab125cDGJab13cbb2345', 2345)
    check_result('777ab125cab13cbb', 777)
    check_result('08777ab125cGG^ab13cbb', 8777)
    check_result('ab125cab13cbb9990', 9990)
    check_result('ab125cab$13cbb9991', 9991)
    check_result('ab125cab13cbb9992$', 9992)
    check_result('ab125cab13cbb99930$', 99930)
    check_result('$ab125cab13cbb9994', 9994)
    check_result('$', 0)
    check_result('1$2', 2)
    check_result('', 0)


if __name__ == "__main__":
    main()
