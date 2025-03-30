# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# Cortege slice 5:08


def main():
    person = ['Ivan', 'Petrov', 'June', 12, 1947]
    person2 = ['Fiodor', 'Petrov', 'June', 12, 1947]
    print('type of (42,) is {}'.format(type(person)))
    name, birthday = person[:2], person[2:]
    LAST_NAME, MONTH = slice(None, 1), slice(2, None)
    print('name is {},\nbirthday is {}'.format(name, birthday))
    print('types name: {},\nbirthday: {}'.format(type(name), type(birthday)))
    print(person[LAST_NAME])
    print(person2[LAST_NAME])


if __name__ == "__main__":
    main()
