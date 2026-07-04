#
fruits = ["apple", "banana", "orange"]


def not_enumerate(tested_list: list):
    for i in range(len(tested_list)):
        print(i, tested_list[i])


def enumerated(tested_list: list, start_index: int = 0):
    for i, fruit in enumerate(tested_list, start_index):
        print(i, fruit)


def enumerated_list(tested_list: list, start_index: int = 0):
    return list(enumerate(tested_list, start_index))


def main():
    not_enumerate(fruits)
    print("----------enumerated--------------")
    enumerated(fruits)

    print("----------enumerated-start 100----")
    enumerated(fruits, start_index=100)
    print("----------enumerated-start 100----")
    print(enumerated_list(fruits, start_index=100))


if __name__ == "__main__":
    main()
