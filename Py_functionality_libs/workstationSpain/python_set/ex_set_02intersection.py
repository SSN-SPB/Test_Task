# https://pynative.com/python-set-exercise-with-solutions/#h-exercise-1-add-a-list-of-elements-to-a-set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Orange", "Green", "Red.", 1]


def main():
    y = sample_set.intersection(set(sample_list))
    print(y)
    assert y == {"Orange"}


if __name__ == "__main__":
    main()
