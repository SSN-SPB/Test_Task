#!/usr/bin/env python3
# checking variable replacing


def main():
    c = 5
    b = 7
    print("c is: {}".format(c))
    print("b is: {}".format(b))
    b, c = c, b
    print("Updated c is: {}".format(c))
    print("Updated b is: {}".format(b))

    a = 5
    d = a
    print("init a and d are {}:{}".format(a, d))
    a = 7
    print("new  a and d are {}:{}".format(a, d))

    a_boolean = True
    d_boolean = a_boolean
    print("init d is {}".format(d_boolean))
    a_boolean = False
    print("new d is {}".format(d_boolean))


if __name__ == "__main__":
    main()
