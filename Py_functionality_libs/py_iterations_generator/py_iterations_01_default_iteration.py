# https://compscicenter.ru/courses/python/2015-autumn/classes/1542/
# 15:16
# iterations
import dis


class seq_iter:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = self.instance[self.idx]
        except IndexError:
            raise StopIteration

        self.idx += 1
        return res


tested_list = ["a", "b", "c"]


def iterate_list(list):
    for x in list:
        print(x)


def main():
    iterate_list(tested_list)
    dis.dis("for x in tested_list:print(x)")
    dis.dis("iterate_list(tested_list)")


if __name__ == "__main__":
    main()
