"""Suite demonstrates polymorphism overloading in oop Python"""

# Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying data types or classes. In Python, polymorphism can be achieved through method overloading and operator overloading.
# Method overloading allows a class to have multiple methods with the same name but different parameters. However,
# Python does not support method overloading in the traditional sense as seen in languages like Java or C++.
# Instead, you can achieve similar functionality using default arguments or variable-length arguments (*args and **kwargs).


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
    # Compile-time overloading
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
