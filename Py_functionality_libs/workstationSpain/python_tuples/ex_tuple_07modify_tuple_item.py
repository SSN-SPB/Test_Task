# https://pynative.com/python-tuple-exercise-with-solutions/
tuple1 = (45, 45, 45, 45)

def

def main():
    tuple1 = (11, [22, 33], 44, 55)
    for x in tuple1:
        print(type(x))
        if type(x) is list:
            print(x)
            print(tuple1.index(x))
            tuple1[tuple1.index(x)][0] = 222
    print(tuple1)


if __name__ == "__main__":
    main()
