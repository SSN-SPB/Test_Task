# https://pynative.com/python-set-exercise-with-solutions/#h-exercise-1-add-a-list-of-elements-to-a-set
# exercise 3

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


def main():
    y = set1.intersection(set2)
    print(y)
    for x in y:
        set1.remove(x)
        set2.remove(x)
    print(set1)
    print(set2)
    set1.update(set2, y)
    print(set1)
    # assert y == {30}


if __name__ == "__main__":
    main()
