# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/#h-exercise-1-print-first-10-natural-numbers-using-while-loop
def calculate_cube(n):
    mylist = list(map(lambda x: x**3, range(1, n)))
    return mylist


def main():
    t = 6
    my_list = calculate_cube(t + 1)
    for x in range(1, t + 1):
        print("Current value: {} and the cube is {}".format(x, my_list[x - 1]))


if __name__ == "__main__":
    main()
