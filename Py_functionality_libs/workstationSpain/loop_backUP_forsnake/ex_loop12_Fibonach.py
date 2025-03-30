# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/#h-exercise-1-print-first-10-natural-numbers-using-while-loop


def main():
    test_list = [0, 1]
    test_str = ""
    while len(test_list) < 10:
        test_list.append(test_list[len(test_list) - 1] + test_list[len(test_list) - 2])
    for x in test_list:
        test_str = test_str + " " + str(x)
    print(test_str)


if __name__ == "__main__":
    main()
