import threading
import time
import datetime


def timer_print():
    completion_time = time.time()
    ct = datetime.datetime.fromtimestamp(completion_time).strftime("%Y_%m_%d_%H_%M_%S_%f")
    print("Hello")
    print("Completion time (raw):", completion_time)
    print("Completion time (formatted):", ct)


def main():
    timer = threading.Timer(7, timer_print)
    start_time = time.time()
    st = datetime.datetime.fromtimestamp(start_time).strftime("%Y_%m_%d_%H_%M_%S_%f")

    timer.start()
    print(start_time)
    print(st)



if __name__ == "__main__":
    main()
