# __call__ is a special method in Python that allows an instance
# of a class to be called as if it were a function.
# When you define the __call__ method in a class,
# you can create instances of that class and call them directly,
# passing arguments to the __call__ method.


class Divider:

        def __init__(self, divisor):
            self.divisor = divisor

        def __call__(self, dividend):
            if self.divisor == 0:
                raise ValueError("Divisor cannot be zero.")
            return dividend / self.divisor

def main():
    divider_by_2 = Divider(2)
    result = divider_by_2(7)
    assert result == 3.5, f"Expected 3.5, got {result}"
    print(result)  # Output: 3.5



if __name__ == "__main__":
    main()