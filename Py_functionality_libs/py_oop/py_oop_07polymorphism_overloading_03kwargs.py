# This is a simple example of function overloading
# in Python using default arguments and variable-length arguments.


def overloading(a, b=0, *agrs):
    list_of_args = []
    for i in agrs:
        list_of_args.append(i)
    return a + b + len(list_of_args), list_of_args


def overloading_kwargs(a, b=0, *agrs, **kwargs):
    list_of_args = []
    for v in kwargs.values():
        list_of_args.append(v)
    return a + b + len(list_of_args), list_of_args


def main():
    total_sum, total_list = overloading(1, 5, 7, 9)
    print(f"results are {total_sum} and {total_list}")
    total_sum, total_list = overloading(1)
    print(f"results are {total_sum} and {total_list}")
    total_sum, total_list = overloading(1, 2)
    print(f"results are {total_sum} and {total_list}")
    total_sum, total_list = overloading(1, 2, 3)
    print(f"results are {total_sum} and {total_list}")
    total_sum, total_list = overloading(1, 1, 1, 1, 1, 1)
    print(f"results are {total_sum} and {total_list}")

    total_sum, total_list = overloading_kwargs(1, 1, 1, 1, 1, 1)
    print(f"kwargs results are {total_sum} and {total_list}")

    total_sum, total_list = overloading_kwargs(1, 1, 1, 1, 1, 1, u=15, t=18)
    print(f"kwargs results2 are {total_sum} and {total_list}")

    total_sum, total_list = overloading_kwargs(7, u=115, t=118)
    print(f"kwargs results3 are {total_sum} and {total_list}")


if __name__ == "__main__":
    main()
