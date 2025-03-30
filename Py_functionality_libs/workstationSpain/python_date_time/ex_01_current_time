# https://pynative.com/python-set-exercise-with-solutions/#h-exercise-1-add-a-list-of-elements-to-a-set
# exercise 9

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


def remove_not_common_elements(set_one, set_two):
    """Exercise 9: Remove items from set1 that are not common 
    to both set1 and set2"""
    set_one.intersection_update(set_two)


def main():
    remove_not_common_elements(set1, set2)
    print(set1)
    assert set1 == {40, 50, 30}


if __name__ == "__main__":
    main()
