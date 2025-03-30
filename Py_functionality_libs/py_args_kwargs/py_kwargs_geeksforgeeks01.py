def my_fun(arg0, arg_y, *argv):
    for arg in argv:
        print(arg)
    print(arg0, " ", arg_y)


def my_fun_kwargs(**kwargs):
    for k, v in kwargs.items():
        print("key: {}; value: {}".format(k, v))


def main():
    my_fun(**kwargs)


if __name__ == "__main__":
    main()
