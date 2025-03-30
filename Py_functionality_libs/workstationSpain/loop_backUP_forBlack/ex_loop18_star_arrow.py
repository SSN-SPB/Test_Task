# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/#h-exercise-1-print-first-10-natural-numbers-using-while-loop

def print_stars(n):
    c = 0
    test_str = ""
    while c < n:
        test_str = test_str + " " + "*"
        c += 1
    return test_str

def main():
    for x in range(1, 6):
        print(print_stars(x))
    while x > 0:
        x -= 1
        print(print_stars(x))

if __name__ == "__main__":
    main()
