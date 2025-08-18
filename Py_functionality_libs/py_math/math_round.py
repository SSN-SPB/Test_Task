def return_round(n, r):
    return round(n, r)


def main():
    result = round(3.14159, 3)
    print(result)
    assert result == 3.142


if __name__ == "__main__":
    main()
