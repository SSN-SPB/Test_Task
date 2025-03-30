# Task:
# Input: [1, 4, 3, 2]
# Output: 2341
#
# def reverse_a_list(a_list: list) -> str:
#     # Type your code here
#     return ""
#
#
# a = [1, 4, 3, 2]
# print(reverse_a_list(a))
a = [1, 4, 3, 2]


def reverse_a_list(a_list: list) -> str:
    # Type your code here
    # return "".join(str(element) for element in a_list[::-1])
    return " ".join(map(str, a_list[::-1]))


def main():
    print(reverse_a_list(a))


if __name__ == "__main__":
    main()
