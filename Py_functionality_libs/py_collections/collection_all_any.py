# any - True if at least one element is True
# all - True if all elements is True

tested_list_one = [2, 0, 2, 5]
tested_list_two = [2, "y", 2, 5]


class CheckCollection:

    @staticmethod
    def check_any(collection):
        return any(collection)

    @staticmethod
    def check_all(collection):
        return all(collection)


def main():
    c = CheckCollection()
    print(c.check_all(tested_list_two))
    assert c.check_any(tested_list_one) == True
    assert c.check_all(tested_list_one) == False
    assert c.check_all(tested_list_two) == True


if __name__ == "__main__":
    main()
