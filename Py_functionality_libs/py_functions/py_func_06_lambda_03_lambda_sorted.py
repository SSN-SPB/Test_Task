points = [(1, 2, 7), (7, 1, 15, 11, 17), (5, -1, 0, 1, 15, 11)]

test_tuple = (5, -1, 0)
print(len(test_tuple))


def main():
    points_sorted = sorted(points, key=lambda point: point[1])
    print(points_sorted)
    # Output: [(5, -1, 0, 1, 15, 11), (7, 1, 15, 11, 17), (1, 2, 7)]
    points_sorted = sorted(points, key=lambda point: point[0])
    print(points_sorted)
    points_sorted = sorted(points, key=lambda point: point[2])
    print(points_sorted)
    points_sorted = sorted(points, key=lambda point: len(point))
    print(points_sorted)
    # Output: [(1, 2, 7), (7, 1, 15, 11, 17), (5, -1, 0, 1, 15, 11)]


if __name__ == "__main__":
    main()
