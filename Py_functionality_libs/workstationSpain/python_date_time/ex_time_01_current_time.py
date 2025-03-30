# https://pynative.com/python-date-and-time-exercise/#h-exercise-1-print-current-date-and-time-in-python
# exercise 1

from datetime import datetime


def print_current_time():
    """Exercise 1: Get currnt tim"""
    now = datetime.now()
    print('Current DateTime:', now)
    print('Type:', type(now))


def main():
    print_current_time()
    # assert set1 == {40, 50, 30}


if __name__ == "__main__":
    main()
