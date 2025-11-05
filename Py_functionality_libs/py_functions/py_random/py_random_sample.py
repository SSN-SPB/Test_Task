from random import sample

init_list = list(map(lambda a: a + a + a, range(0, 10, 2)))


def random_sample(tested_collection, x):
    return sample(tested_collection, x)


def main():
    print(init_list)
    print(random_sample(init_list, 3))
    assert len(random_sample(init_list, 3)) == 3
    assert type(random_sample(init_list, 3)) == type(init_list)


if __name__ == "__main__":
    main()
