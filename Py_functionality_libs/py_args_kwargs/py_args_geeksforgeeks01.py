def my_fun(arg0, arg_y, *argv):
    for arg in argv:
        print(arg)
    print(arg0, " ", arg_y)


def main():
    my_fun("a0", "a1", "a2", "a3", "a4", "a5")


if __name__ == "__main__":
    main()
