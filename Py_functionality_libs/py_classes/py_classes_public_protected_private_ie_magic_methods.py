class Counter:
    def __init__(self, counter_value=0):
        self.value1 = 15
        self.value2 = counter_value
        self.value3 = 'hello'

    def get_value1(self):
        print(f"public: {self.value1}")

    def _get_value2_protected(self):
        print(f"protected: {self.value2}")

    def __get_value3_private(self):
        print(f"private: {self.value3}")

    def __get_value3_magic__(self):
        print(f"magic: {self.value3}")


def main():
    c = Counter(19)
    c.get_value1()
    c._get_value2_protected()
    # c.__get_value3_private() # not displayed and provokes error
    c._Counter__get_value3_private()
    c.__get_value3_magic__()


if __name__ == '__main__':
    main()
