# This is a basic example of using the asyncio
# library in Python to run asynchronous tasks.
import asyncio
import random

random_values = [random.randint(1, 100) for _ in range(1000)]


async def file_creating(initial_list):
    await asyncio.sleep(5)  # Emulate delay before creating the file
    print("Creating file with random values...")
    # print(initial_list)
    with open("output.txt", "w") as file:
        for value in initial_list:
            file.write(f"Value for {initial_list.index(value)} is {value}\n")

    print("File created with random values.")
    await asyncio.sleep(17)


async def file_reading(file_name):
    with open(file_name, "r") as new_file_name:
        for line in new_file_name:
            print(line.strip())
    # try:
    #     with open(file_name, "r") as new_file_name:
    #         for line in new_file_name:
    #             print(line.strip())
    # except FileNotFoundError:
    #     print(f"File {file_name} not found.")


async def main():
    await file_creating(random_values)
    await file_reading("output.txt")


if __name__ == "__main__":
    asyncio.run(main())
