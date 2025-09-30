import threading
import time
import datetime


def timer_print():
    print("Hello")


def main():
    timer = threading.Timer(7, timer_print)
    start_time = time.time()
    st = datetime.datetime.fromtimestamp(start_time).strftime("%Y_%m_%d_%H_%M_%S_%f")

    timer.start()
    end_time = time.time()
    et = datetime.datetime.fromtimestamp(end_time).strftime("%Y_%m_%d_%H_%M_%S_%f")
    print(start_time)
    print(st)
    print(end_time)
    print(et)


if __name__ == "__main__":
    main()
