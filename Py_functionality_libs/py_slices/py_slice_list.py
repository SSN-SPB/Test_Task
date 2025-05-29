# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# Cortege slice 5:08


def main():
    person = ["Ivan", "Petrov", "June", 12, 1947]
    person2 = ["Fiodor", "Petrov", "July", 12, 1947]
    last_name, month = slice(None, 1), slice(2, None)
    print(person[last_name])
    print(person2[month])
    print(person[1:12:2])


if __name__ == "__main__":
    main()
