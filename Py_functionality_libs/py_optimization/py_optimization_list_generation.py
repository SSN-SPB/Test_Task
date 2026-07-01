import time
import datetime


def return_time():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%m_%d_%H_%M_%S")
    return st


def do_something():
    # bad as a list is created in memory and then printed
    print(f"Before created list {return_time()}")
    squares = [x**2 for x in range(1, 100000000)]
    print(f"After created list {return_time()}")
    print(f"Before generator {return_time()}")
    # good as a generator is created and printed one by one
    squares2 = (x**2 for x in range(1, 100000000))
    print(f"After generator {return_time()}")
    print("Type of squares: ", type(squares))
    print("Type of squares2: ", type(squares2))


def main():
    do_something()


if __name__ == "__main__":
    main()
