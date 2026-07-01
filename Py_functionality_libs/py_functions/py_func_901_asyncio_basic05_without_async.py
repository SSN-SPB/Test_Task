# This is a basic example demonstrating failure without asyncio
# library in Python for asynchronous tasks.
import time
import random
import threading

random_values = [random.randint(1, 100) for _ in range(1000)]


def file_creating(initial_list):
    time.sleep(5)  # Emulate delay before creating the file
    print("Creating file with random values...")
    # print(initial_list)
    with open("output.txt", "w") as file:
        for value in initial_list:
            file.write(f"Value for {initial_list.index(value)} is {value}\n")

    print("File created with random values.")
    time.sleep(17)


def file_reading(file_name):
    with open(file_name, "r") as new_file_name:
        for line in new_file_name:
            print(line.strip())


def main():
    # Run concurrently using threads to emulate the async behavior
    thread1 = threading.Thread(target=file_creating, args=(random_values,))
    thread2 = threading.Thread(target=file_reading, args=("output.txt",))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
