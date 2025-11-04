import time

def cycle_print(value):
    for i in range(value):
        print(f"It is {i}")


def main():
    s = time.thread_time()
    cycle_print(1000000)
    e = time.thread_time()
    print(f"Totally: {e - s:.6f}")


if __name__ == "__main__":
    main()
