# https://pynative.com/python-set-exercise-with-solutions/#h-exercise-1-add-a-list-of-elements-to-a-set
# exercise 8

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


def check_if_common_elements_in_set(set_one, set_two):
    """Exercise 8: Update set1 by adding items from set2, except common items"""
    set_one.symmetric_difference_update(set_two)


def main():
    check_if_common_elements_in_set(set1, set2)
    print(set1)
    assert set1 == {70, 10, 20, 60}


if __name__ == "__main__":
    main()
