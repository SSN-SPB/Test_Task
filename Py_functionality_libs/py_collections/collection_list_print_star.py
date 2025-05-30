list_a = ["a", "a1", "a2"]
list_b = ["b", "b1", "b2"]


def main():
    print(list_b)  # ['b', 'b1', 'b2']
    print(*list_a)  # a a1 a2 - no brackets and commas


if __name__ == "__main__":
    main()
