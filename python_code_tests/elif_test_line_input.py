# https://hr.gs/automationskills sample
# this is a simple fizzbuzz program that
# takes an integer input and prints "Fizz"
# for multiples of 3, "Buzz" for multiples
# of 5, and "FizzBuzz" for multiples of both
# 3 and 5. For all other numbers, it prints the number itself.


def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            # Write your code here


if __name__ == '__main__':
    n = int(input("Input integer value: ").strip())

    fizzBuzz(n)
