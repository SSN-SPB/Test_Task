# Существует поле с элементами разных цветов.
# Scenario: The list with elements of different colors
# Required:
# 1 Find the longest line (vertical or horizontal) with same color
# 2 Print out color and the length of such line
# Condition: size of list and number of colors is unlimited
import sys


table = [
        ['green', 'red', 'blue', 'red'],
        ['green', 'yellow'],
        ['green', 'yellow', 'yellow', 'blue'],
        ['blue', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red']
   ]


def define(list_name):
    length = 0
    color = ''
    min_length = sys.maxsize
    for x in list_name:
        if len(x) < min_length:
            min_length = len(x)
        value_list = set(x)
        for e in value_list:
            int_counter = 0
            for i in x:
                if e == i:
                    int_counter = int_counter + 1
                    if int_counter > length:
                        length = int_counter
                        color = e
                else:
                    int_counter = 0
    print('horizontal result is color {}, length is {}'.format(color, length))
    for i in range(0, min_length):
        init_color_col = list_name[0][i]
        int_counter_col = 1
        for y in range(1, len(list_name)):
            if list_name[y][i] == init_color_col:
                int_counter_col = int_counter_col + 1
                if int_counter_col > length:
                    length = int_counter_col
                    color = init_color_col
            else:
                int_counter_col = 0
                init_color_col = list_name[y][i]
        return color, length


def main():
    color, length = define(table)
    print('Final result: color is {}, length is {}'.format(color, length))


if __name__ == "__main__":
    main()
