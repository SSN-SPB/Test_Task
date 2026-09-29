# This code demonstrates how to create a dictionary
# using dictionary comprehension + random choice in Python.


import random


def main():
    random_list = [
        "A" + str(i) + random.choice(["C", "D", "E"]) for i in range(3, 19, 2)
    ]
    print(random_list)


if __name__ == "__main__":
    main()
