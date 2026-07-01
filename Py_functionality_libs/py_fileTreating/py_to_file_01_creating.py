import random

random_values = [random.randint(1, 100) for _ in range(10)]


def creating_file_with_random_values(initial_list):
    print("Creating file with random values...")
    print(initial_list)
    with open("output.txt", "w") as file:
        for value in initial_list:
            file.write(f"Value for {initial_list.index(value)} is {value}\n")

    print("File created with random values.")


# Write to a file
def main():
    creating_file_with_random_values(random_values)


if __name__ == "__main__":
    main()
