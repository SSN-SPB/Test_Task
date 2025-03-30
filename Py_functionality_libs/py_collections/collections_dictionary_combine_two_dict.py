# https://egorovegor.ru/python-merge-dict

a = {1: 'peanut', 2: 'butter', 3: 'jelly', 4: 'time'}
b = {1: 'fish', 2: 'chips'}

c = {1: ['peanut', 'butter', 'jelly', 'time'], 2: ['fish', 'chips']}
d = {1: ['fish', 'chips'], 2: ['peanut', 'butter', 'jelly', 'time']}


def main():
    # version 3.9+
    x = a | b
    print(x)
    # x {1: 'fish', 2: 'chips', 3: 'jelly', 4: 'time'}
    y = c | d
    print(y)
    # {1: ['fish', 'chips'], 2: ['peanut', 'butter', 'jelly', 'time']}
    # before 3.9
    x1 = {**a, **b}
    print(x1)
    # x {1: 'fish', 2: 'chips', 3: 'jelly', 4: 'time'}
    x2 = dict(list(a.items()) + list(b.items()))
    print(x2)
    x3 = {**a, **b}
    print('x3 = {}'.format(x3))


if __name__ == "__main__":
    main()
