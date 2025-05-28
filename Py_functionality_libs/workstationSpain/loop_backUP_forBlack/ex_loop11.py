# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/#h-exercise-1-print-first-10-natural-numbers-using-while-loop
import sympy


def main():
    for x in range(0, 10):
        if sympy.isprime(x):
            print(x)


if __name__ == "__main__":
    main()
