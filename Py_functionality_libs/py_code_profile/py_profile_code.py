import cProfile

def my_function():
    a = 1
    b = 1
    assert a == b
    pass

cProfile.run('my_function()')


def main():
    cProfile.run('my_function()')


if __name__ == "__main__":
    main()
