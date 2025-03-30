# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/#h-exercise-1-print-first-10-natural-numbers-using-while-loop
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def main():
    test_str = ''
    for x in my_list:
        if my_list.index(x) % 2 != 0:
            test_str = test_str + ' ' + str(x)
    print(test_str)


if __name__ == "__main__":
    main()
