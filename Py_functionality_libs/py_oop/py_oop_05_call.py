"""Suite demonstrates call magic methods in oop Python"""


class UpdateDeata:
    def __call__(self, value):
        return self.factor * value

    def __init__(self, factor):
        self.factor = factor


def main():
    test_run = UpdateDeata(7)
    for i in range(1, 11):
        print(test_run(i))


if __name__ == "__main__":
    main()
