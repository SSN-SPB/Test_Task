"""Suite demonstrates abstract methods in oop Python"""

from abc import abstractmethod


class Stop:
    @abstractmethod
    def stop(self):
        print("Implement an abstract method")

    def __init__(self):
        print("Stop constructor")


class TestRun(Stop):
    """__ph__"""

    def stop2(self):
        print("stop2 from test run")

    # def stop(self):
    #     print("stop from test run")


def main():
    test_run = TestRun()
    # TypeError: Can't instantiate abstract class
    # TestRun with abstract method stop (untill adding stop(self) into TestRun
    print(test_run.stop2())


if __name__ == "__main__":
    main()
