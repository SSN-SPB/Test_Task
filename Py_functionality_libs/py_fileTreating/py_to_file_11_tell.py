import random

random_values = [random.randint(1, 100) for _ in range(10)]


def creating_file_with_random_values(initial_list):
    print("Creating file with random values...")
    print(initial_list)
    with open("output.txt", "w") as file:
        for value in initial_list:
            file.write(f"Value for {initial_list.index(value)} is {value}\n")
        position = file.tell()
        print(f"Current position after writing: {position}")
    with open("output.txt", "r") as f:
        content = f.read(15)  # Читаем первые 15 символов
        position = f.tell()
        print(f'Content read: "{content}"')  # Вывод: "Value for 0 is"
        print(f"Current position after reading: {position}")
    print("File created with random values.")


# Write to a file
def main():
    creating_file_with_random_values(random_values)


if __name__ == "__main__":
    main()
