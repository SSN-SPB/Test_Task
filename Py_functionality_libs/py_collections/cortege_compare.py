# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# Cortege compare, concatenate 11:43
# Compare - element by element

def main():
    x = (1, 9, 3)
    y = (1, 2, 5, 4)
    print('x < y is {}'.format(x < y))  # False
    print('  Concatenate  '.center(79, 'z'))
    z = x + y
    print(z)  # (1, 9, 3, 1, 2, 5, 4)


if __name__ == "__main__":
    main()
