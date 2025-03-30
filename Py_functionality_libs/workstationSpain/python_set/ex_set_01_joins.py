# https://pynative.com/python-set-exercise-with-solutions/#h-exercise-1-add-a-list-of-elements-to-a-set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red", 1]


def main():
    # sample_set.update(sample_list)
    print(sample_set)
    test_boolean = True
    for x in sample_list:
        if x not in sample_set:
            test_boolean = False

    print(test_boolean)
    sample_set.update(sample_list)
    test_boolean = True
    for x in sample_list:
        if x not in sample_set:
            test_boolean = False
    print(test_boolean)
    assert test_boolean


if __name__ == "__main__":
    main()
