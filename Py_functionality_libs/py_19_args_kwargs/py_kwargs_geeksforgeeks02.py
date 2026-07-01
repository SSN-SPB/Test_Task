kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks", "arg5": "Geeks5"}


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


def main():
    try:
        myFun(**kwargs)
    except TypeError as te:
        print("wrong arguments: {}".format(te))


if __name__ == "__main__":
    main()
