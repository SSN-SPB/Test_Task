# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# Cortege slice 5:08


def main():
    person = ["Ivan", "Petrov", "June", 12, 1947]
    person2 = ("Fiodor", "Petrov", "September", 12, 1947)
    LAST_NAME, MONTH = slice(None, 1), slice(2, 5, 2)
    print(person[LAST_NAME])
    print(person2[LAST_NAME])
    print(person[MONTH])
    print(person2[MONTH])
    assert person2[MONTH] == ("September", 1947)


if __name__ == "__main__":
    main()
