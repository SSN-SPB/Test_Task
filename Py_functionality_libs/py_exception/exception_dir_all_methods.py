import logging
logger = logging.getLogger(__name__)


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
# ['__cause__', '__class__', '__context__',\
# '__delattr__', '__dict__', '__dir__', '__doc__',\
# '__eq__', '__format__', '__ge__', '__getattribute__',\
# '__gt__', '__hash__', '__init__', '__init_subclass__',\
# '__le__', '__lt__', '__ne__', '__new__', '__reduce__',\
# '__reduce_ex__', '__repr__', '__setattr__', '__setstate__',\
# '__sizeof__', '__str__', '__subclasshook__',\
# '__suppress_context__', '__traceback__', 'args', 'with_traceback']
        print(e.args)
        print(e.with_traceback)
#    except TypeError:
#        print('only one element can be appended to list')
#    print(list)      # [0, 1, 'x']
#    traceback.print_exc()
#    traceback.print_exception(*sys.exc_info())


if __name__ == "__main__":
    main()
