#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1520/
# 00:00 - 7:59


def main():
    list = [0, 1]
    list.append("x")
    print(list)  # [0, 1, 'x']
    try:
        list.append("y", "z")
    except (ValueError, ArithmeticError):
        pass
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
