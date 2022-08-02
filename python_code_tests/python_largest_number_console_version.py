class TaskPartTwo(object):
    def largestNumber(self, s):
        largest_number = 0
        digit_found = False
        interim_string = ''
        for x in s:
            if x.isdigit():
                digit_found = True
                interim_string = interim_string + x
                if int(interim_string) > largest_number:
                    largest_number = int(interim_string)
            else:
                interim_string = ''
        if digit_found:
            return largest_number
        else:
            return None


def main():
    while True:
        input_string = input('Enter the test string or q to complete: ')
        if input_string == "q":
            exit()
        version = TaskPartTwo()
        result = version.largestNumber(input_string)
        if input_string != "" and result:
            print('The largest number in the string is {}'.format(result))
        if input_string == "":
            print('There is no input string. Enter it or q to complete')
        if input_string != "" and result is None:
            print('There is no digit in the string')


if __name__ == "__main__":
    main()
