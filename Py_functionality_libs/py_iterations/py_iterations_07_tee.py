from itertools import tee

# tee is a function in the itertools module that
# allows you to create multiple independent iterators from a single iterable.
# It takes an iterable as input and returns n independent iterators,
# where n is specified by the user.
# Each iterator can be used to iterate over the original
# iterable independently, without affecting the others.


def generating_data(tee_number):
    for i in range(tee_number):
        print(f"Generating - {i}")
        yield i


test_data = generating_data(5)
print(list(test_data))


def main():
    test_data1, test_data2 = tee(generating_data(7))

    print("test_data1")
    print(list(test_data1))
    print("test_data2")
    print("without calling generator")
    print(list(test_data2))


# Output
# test_data1
# Generating - 0
# Generating - 1
# Generating - 2
# Generating - 3
# Generating - 4
# Generating - 5
# Generating - 6
# [0, 1, 2, 3, 4, 5, 6]
# test_data2
# No generating_data 2nd time
# [0, 1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    main()
