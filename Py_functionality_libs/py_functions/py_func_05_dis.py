# https://compscicenter.ru/courses/python/2015-autumn/classes/1542/
import dis

tested_list = ["a", "b", "c"]


def sample_function(test_list):
    for x in test_list:
        print(x)
        print(x + x)


def main():
    sample_function(tested_list)
    dis.dis(sample_function)


if __name__ == "__main__":
    main()
