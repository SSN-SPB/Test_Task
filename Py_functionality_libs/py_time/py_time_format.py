import datetime
import time


def return_time():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%m_%d_%H_%M_%S")
    return st


def main():
    ts = time.time()
    print(f"Current time (raw): {ts}")
    print(f"formatted time: {return_time()}")


if __name__ == "__main__":
    main()
