# https://leetcode.com/problems/container-with-most-water/ 11


def maxArea(height) -> int:
    max_size = float("-inf")
    i, y = 0, len(height) - 1
    while i < y:
        max_size = max(min(height[i], height[y]) * (y - i), max_size)
        if height[i] < height[y]:
            i += 1
        else:
            y -= 1

    return max_size


def main():
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


if __name__ == "__main__":
    main()
