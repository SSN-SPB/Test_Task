# https://pynative.com/python-set-exercise-with-solutions/#h-exercise-1-add-a-list-of-elements-to-a-set
# exercise 4 & 5 & 6

set1 = {10, 20, 30}
set2 = {20, 40, 50}

set3 = {10, 20, 30, 40, 50}
set4 = set(list(range(10, 40, 10)))

set5 = {10, 20, 30, 40, 50}
set6 = {30, 40, 50, 60, 70}


def update_with_unique(set_one, set_two):
    """Exercise 4: Update the first set with items that
    don’t exist in the second set
    Given two Python sets, write a Python program to update
    the first set with items that exist only in the first set
    and not in the second set."""
    set_one.difference_update(set_two)


def main():
    update_with_unique(set1, set2)
    print(set1)
    update_with_unique(set3, set4)
    x = list(set3)
    x.sort()
    print(set(x))
    z = set5.symmetric_difference(set6)
    print(z)
    assert set1 == {10, 30}
    assert set(x) == {40, 50}
    assert z == {20, 70, 10, 60}


if __name__ == "__main__":
    main()
