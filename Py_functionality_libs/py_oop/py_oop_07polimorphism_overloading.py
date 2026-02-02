"""Suite demonstrates polymorphism overloading in oop Python"""


class BaseClass:
    """__ph__"""

    def setup(self):
        print(f"from BaseClass setup {self}")
        print("make setup base")

    # imitate overloading
    @staticmethod
    def calculate_sum_three(a, b, c=0):
        return a + b + c

    # imitate overloading using *args and **kwargs
    @staticmethod
    def calculate_sum(*args, **kwargs):
        total_sum = 0

        for value in args:
            total_sum += value

        for value in kwargs.values():
            total_sum += value

        return total_sum


def main():
    bt_test = BaseClass()
    print(bt_test.calculate_sum_three(5, 7))
    print(bt_test.calculate_sum_three(5, 7, 9))
    print(f"print args: {bt_test.calculate_sum(15, 17, 19)}")
    print(f"print kwargs: {bt_test.calculate_sum(15, 17, 19, a=1, b=3)}")


if __name__ == "__main__":
    main()
