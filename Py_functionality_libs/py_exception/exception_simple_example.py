import traceback
import sys


def main():
    list = [0, 1]
    list.append('x')
    print(list)      # [0, 1, 'x']
    try:
        list.append('y', 'z')
    except Exception as e:
        print(e)
        print(e.__dict__)
        print(dir(e))
#    except TypeError:
#        print('only one element can be appended to list')
#    print(list)      # [0, 1, 'x']
#    traceback.print_exc()
#    traceback.print_exception(*sys.exc_info())


if __name__ == "__main__":
    main()
