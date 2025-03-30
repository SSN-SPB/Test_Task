# https://pynative.com/python-set-exercise-with-solutions/#h-exercise-1-add-a-list-of-elements-to-a-set
# exercise 7

set1 = {10, 20, 30, 40, 50}
set2 = {60, 10, 80, 90, 50}


def check_if_common_elements_in_set(set_one, set_two):
    """Exercise 7: Check if two sets have any elements
    in common. If yes, display the common elements"""
    new_set = set_one.intersection(set_two)
    return new_set


def main():
    result = check_if_common_elements_in_set(set1, set2)
    print(result)
    assert result == {50, 10}


if __name__ == "__main__":
    main()
