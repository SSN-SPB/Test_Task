def my_fun(arg0, arg_y, *argv):
    for arg in argv:
        print(arg)
    print(arg0, " ", arg_y)


def my_fun_kwargs(*argv, **kwargs):
    for arg in argv:
        print(f"args: {arg}")
    for k, v in kwargs.items():
        print("key: {}; value: {}".format(k, v))


def main():
    my_fun(1, 2, 3, 7, 9, 17, 27)
    my_fun_kwargs(1, 2, 3, 7, 9, p=17, t=31)


if __name__ == "__main__":
    main()
