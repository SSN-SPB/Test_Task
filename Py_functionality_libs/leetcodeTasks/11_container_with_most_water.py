# https://leetcode.com/problems/roman-to-integer/description/ 13


def maxArea(height) -> int:
    max_size = float("-inf")
    for i in range(0, len(height) - 1):
        for y in range(i + 1, len(height)):
            max_size = max(min(height[i], height[y]) * (y - i), max_size)

        print(
            " size {} i {}, y: {}, height[i] {}, height[y] {}".format(
                max_size, i, y, height[i], height[y]
            )
        )

    return max_size


def main():
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


if __name__ == "__main__":
    main()
