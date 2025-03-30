import traceback
import sys


class CarException(Exception):
    """Raised when the speed value is too large"""
    print('Speed is too fast')
    pass


def check_speed():
    speed_of_Car = 120
    if (speed_of_Car > 60):
        raise CarException


def main():
    try:
        check_speed()
    except CarException as ce:
        print(ce.__doc__)


if __name__ == "__main__":
    main()
