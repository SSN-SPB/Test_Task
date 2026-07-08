import threading
import time
import datetime

# threading.Timer(interval, function, args=None, kwargs=None)
# args and kwargs are optional arguments to pass to the function
# when it is called


def display_current_time():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%m_%d_%H_%M_%S")
    print(st)


def print_hello():
    print("Hello World")
    display_current_time()


def main():
    display_current_time()
    timer = threading.Timer(3.0, print_hello)
    timer.start()
    display_current_time()


if __name__ == "__main__":
    main()
